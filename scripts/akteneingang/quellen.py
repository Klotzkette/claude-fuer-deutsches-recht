"""Prüft, lädt und öffnet die fest veröffentlichte Bezugsfassung einer Arbeitsakte."""

from __future__ import annotations

import hashlib
import io
import json
import os
import time
from pathlib import Path, PurePosixPath
from urllib.request import Request, urlopen
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "scripts/data/grundakten-lebenswelt"
URL = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def localpath(relative):
    path = (ROOT / relative).resolve()
    if (
        Path(relative).is_absolute()
        or not path.is_relative_to(ROOT)
        or ".." in Path(relative).parts
    ):
        raise ValueError("Unzulässiger Quellpfad: " + str(relative))
    return path


def safe_member(name):
    p = PurePosixPath(name)
    if (
        not name
        or name != p.as_posix()
        or p.is_absolute()
        or ".." in p.parts
        or "\\" in name
        or any(ord(c) < 32 for c in name)
    ):
        raise ValueError("Unzulässiger Archivpfad: " + name)
    return name


class Sources:
    def __init__(self, cache=None, local_index=None):
        self.cache = Path(cache) if cache else None
        self.index = json.loads(Path(local_index).read_text()) if local_index else {}
        if self.cache:
            self.cache.mkdir(parents=True, exist_ok=True)

    def read(self, record):
        if "path" in record:
            data = localpath(record["path"]).read_bytes()
        else:
            remote = record["url"]
            if not remote.startswith(URL):
                raise ValueError("Unbekannter Herausgeber: " + remote)
            name = remote.split("/")[-1]
            target = self.cache / record["sha256"] if self.cache else None
            for candidate in ([target] if target else []) + [
                Path(p) for p in self.index.get(name, [])
            ]:
                if candidate.is_file() and candidate.stat().st_size == record["size"]:
                    data = candidate.read_bytes()
                    if digest(data) == record["sha256"]:
                        return data
            for attempt in range(4):
                try:
                    req = Request(
                        remote, headers={"User-Agent": "Klotzkette-Testakten/1.0"}
                    )
                    with urlopen(req, timeout=100) as response:
                        data = response.read()
                    break
                except OSError:
                    if attempt == 3:
                        raise
                    time.sleep(2**attempt)
            if target and digest(data) == record["sha256"]:
                tmp = target.with_suffix("." + str(os.getpid()) + ".tmp")
                tmp.write_bytes(data)
                tmp.replace(target)
        if digest(data) != record["sha256"] or len(data) != record["size"]:
            raise ValueError("Abweichende Bezugsfassung: " + str(record))
        return data


def members(data):
    with ZipFile(io.BytesIO(data)) as z:
        result = {}
        for item in z.infolist():
            if item.is_dir():
                continue
            name = safe_member(item.filename)
            if name in result:
                raise ValueError("Doppelter Archivname: " + name)
            result[name] = z.read(item)
        return result


def catalogs():
    central = json.loads((DATA / "basis-zentral.json").read_text())
    local = json.loads((DATA / "basis-lokal.json").read_text())
    return {
        **{"testakten/" + slug: record for slug, record in central.items()},
        **local,
    }


def editorial():
    result = {}
    for fname in ("a-f", "g-q", "r-z", "lokal", "weitere"):
        data = json.loads((DATA / (fname + ".json")).read_text())
        for name, record in data.items():
            key = "testakten/" + name if "/" not in name else name
            if key in result:
                raise ValueError("Doppelte Redaktion: " + key)
            result[key] = record
    return result
