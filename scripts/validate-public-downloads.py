#!/usr/bin/env python3
"""Prüft Release-Links in Downloadtabellen ohne Anmeldung bei GitHub.

Ergänzt die Offline-Prüfung: Ein Draft oder ein noch nicht hochgeladenes Asset
ist kein öffentlicher Download. Archivinhalt und Prüfsummen prüft dieses Skript
nicht; dafür bleiben die bestehenden Build- und Release-Validatoren zuständig.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen

from release_routing import REPOSITORY, RELEASE_BASE, ROOT
from testakte_download_notices import download_readmes

LINK = re.compile(
    re.escape(RELEASE_BASE)
    + r"/(?:latest/download|download/(?P<tag>[^/\s<>\"']+))/"
    + r"(?P<asset>[^\s<>\"'()?#]+)"
)


def release_links(paths: list[Path]) -> dict[tuple[str, str], list[str]]:
    links: dict[tuple[str, str], list[str]] = defaultdict(list)
    for path in paths:
        text = html.unescape(path.read_text(encoding="utf-8"))
        for match in LINK.finditer(text):
            key = (unquote(match.group("tag") or "latest"), unquote(match.group("asset")))
            line = text.count("\n", 0, match.start()) + 1
            links[key].append(f"{path}:{line}")
    return dict(links)


def public_json(resource: str):
    # Absichtlich weder gh noch einen Token verwenden: Besucher sehen keine Drafts.
    request = Request(
        f"https://api.github.com/repos/{REPOSITORY}/{resource}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "release-download-check"},
    )
    try:
        with urlopen(request, timeout=20) as response:
            return json.load(response)
    except HTTPError as exc:
        exc.close()
        if exc.code == 404:
            detail = "öffentlich nicht erreichbar (HTTP 404; fehlt oder ist noch ein Entwurf)"
        elif exc.code in (403, 429):
            detail = f"Prüfung nicht möglich (HTTP {exc.code}; Zugriff oder API-Limit prüfen)"
        else:
            detail = f"GitHub antwortet mit HTTP {exc.code}"
        raise ValueError(detail) from exc
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        raise ValueError(f"öffentliche Abfrage fehlgeschlagen: {exc}") from exc


def public_assets(tag: str) -> dict[str, dict]:
    endpoint = "releases/latest" if tag == "latest" else f"releases/tags/{quote(tag, safe='')}"
    release = public_json(endpoint)
    if not isinstance(release, dict) or release.get("draft") is not False or not release.get("published_at"):
        raise ValueError("Release ist nicht als veröffentlicht bestätigt")
    release_id = release.get("id")
    if type(release_id) is not int or release_id <= 0:
        raise ValueError("Release-ID fehlt oder ist ungültig")
    if tag != "latest" and release.get("tag_name") != tag:
        raise ValueError("Release-Tag stimmt nicht mit dem Downloadlink überein")
    assets: dict[str, dict] = {}
    # Pagination ist nötig: Der Begleitrelease hat deutlich mehr als 100 Assets.
    for page in range(1, 12):
        batch = public_json(f"releases/{release_id}/assets?per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("Assetliste ist ungültig")
        for asset in batch:
            if not isinstance(asset, dict) or not isinstance(asset.get("name"), str) or not asset["name"]:
                raise ValueError("Asset ohne gültigen Dateinamen")
            name = asset["name"]
            if name in assets:
                raise ValueError(f"Doppeltes Asset: {name}")
            assets[name] = asset
        if len(batch) < 100:
            return assets
    raise ValueError("Assetliste überschreitet die Sicherheitsgrenze")


def validate(links: dict[tuple[str, str], list[str]]) -> list[str]:
    errors: list[str] = []
    by_tag: dict[str, list[str]] = defaultdict(list)
    for tag, name in links:
        by_tag[tag].append(name)
    for tag, names in sorted(by_tag.items()):
        try:
            assets = public_assets(tag)
        except ValueError as exc:
            errors.append(f"{tag}: {exc}; betrifft {len(names)} Downloadziele, z. B. {links[tag, names[0]][0]}")
            continue
        for name in sorted(names):
            asset = assets.get(name)
            if asset is None:
                reason = "Datei fehlt"
            elif asset.get("state") != "uploaded":
                reason = "Upload nicht abgeschlossen"
            elif type(asset.get("size")) is not int or asset["size"] <= 0:
                reason = "Datei ist leer oder Größenangabe ungültig"
            else:
                continue
            errors.append(f"{tag}/{name}: {reason}; {links[tag, name][0]}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="Ohne Pfade: alle README-Downloadtabellen und der Asset-Index")
    args = parser.parse_args()
    try:
        links = release_links(args.files or download_readmes(ROOT))
        errors = validate(links) if links else ["Keine Release-Downloadlinks gefunden"]
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors[:80]:
            print(f" - {error}", file=sys.stderr)
        print(f"validate-public-downloads: {len(errors)} Fehler", file=sys.stderr)
        return 1
    print(f"validate-public-downloads OK ({len(links)} öffentliche Release-Assets; keine Inhaltsprüfung)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
