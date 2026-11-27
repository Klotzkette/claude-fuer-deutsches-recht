"""Rekonstruiert die belegten Aktenfassungen vor der Fallnavigation und den freigegebenen Aktenausgaben."""

from functools import lru_cache
from hashlib import sha256
import json
import lzma
from pathlib import Path

NACHWEIS = Path("quality/plugin-consolidation/2026-11-27")
REGISTER_SHA256 = "f3b1da69d4f7a69de2a2d989100b8c54f5e6624e584bd1f641e6f30899d6bc85"


@lru_cache(maxsize=4)
def _lesen(pfad, groesse, mtime, ctime, erwartet):
    data = pfad.read_bytes()
    if sha256(data).hexdigest() != erwartet:
        raise ValueError(f"Akten-Erhaltungsnachweis beschädigt: {pfad.name}")
    if pfad.suffix == ".xz":
        return lzma.decompress(data)
    return json.loads(data)


def geprueft(pfad, digest):
    stat = pfad.stat()
    return _lesen(pfad, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns, digest)


def register(root):
    ort = root / NACHWEIS
    if not ort.exists():
        return {}
    return geprueft(ort / "bestand.json", REGISTER_SHA256)


def vorher(root, name, data):
    nachweis = register(root)
    zeile = nachweis.get("dateien", {}).get(name, {})
    for stufe in ("fallausgabe", "basis"):
        if stufe not in zeile:
            continue
        beleg = zeile[stufe]
        if sha256(data).hexdigest() != beleg["nachher"]:
            raise ValueError(f"{name}: Fassung von der freigegebenen Akte abweichend ({stufe})")
        if "rueckweg" in beleg:
            teile = []
            pos = 0
            for start, ende, vormals in beleg["rueckweg"]:
                if not pos <= start <= ende <= len(data):
                    raise ValueError(f"{name}: beschädigte Position im Nachweis")
                teile.extend([data[pos:start], vormals.encode("utf-8")])
                pos = ende
            data = b"".join([*teile, data[pos:]])
        elif "archivpfad" in beleg:
            pfad = (root / beleg["archivpfad"]).resolve()
            if not pfad.is_relative_to(root.resolve()):
                raise ValueError(f"{name}: Archivpfad außerhalb des Repositorys")
            data = pfad.read_bytes()
        else:
            urkunden = geprueft(root / NACHWEIS / "urkunden.xz", nachweis["archiv_sha256"])
            start, umfang = beleg["archivposition"]
            if start < 0 or umfang < 1 or start + umfang > len(urkunden):
                raise ValueError(f"{name}: beschädigte Urkundenposition")
            data = urkunden[start:start + umfang]
        if sha256(data).hexdigest() != beleg["vorher"]:
            raise ValueError(f"{name}: Vorfassung der Fallakte nicht bytegleich erhalten ({stufe})")
    return data
