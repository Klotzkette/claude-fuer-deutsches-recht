#!/usr/bin/env python3
"""Baut editierbare Fallkorrespondenz, Druckfassungen und den Quellenbestand."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from aktenarbeit_inhalte import akte, postquellen
from aktenbestand import ROOT, fallquellen
from testakten_schriftstueck_satz import render_pair

ZIEL = Path("docs/downloads/aktenarbeit")


def schreiben(ziel, inhalt):
    if not ziel.is_file() or ziel.read_bytes() != inhalt:
        ziel.parent.mkdir(parents=True, exist_ok=True)
        handle = NamedTemporaryFile(dir=ziel.parent, prefix=".schriftstueck-", delete=False)
        tmp = Path(handle.name)
        try:
            with handle:
                handle.write(inhalt)
            tmp.replace(ziel)
        finally:
            tmp.unlink(missing_ok=True)


def main():
    faelle = []
    posts = postquellen(ROOT)
    for key, quelle in fallquellen().items():
        try:
            titel, korrespondenz, vermerk, familie, belege = akte(ROOT, key, quelle, posts)
            dateien = []
            for typ, document in (("korrespondenz", korrespondenz), ("arbeitsvermerk", vermerk)):
                for ext, payload in zip(("docx", "pdf"), render_pair(document)):
                    ziel = ZIEL / quelle["id"] / (typ + "." + ext)
                    schreiben(ROOT / ziel, payload)
                    dateien.append({
                        "pfad": ziel.as_posix(), "typ": typ, "format": ext,
                        "sha256": hashlib.sha256(payload).hexdigest(),
                    })
            faelle.append({
                "id": quelle["id"], "titel": titel, "quelle": quelle["seite"],
                "fallpfad": key, "familie": familie, "dateien": dateien, "fundstellen": belege,
            })
        except Exception as exc:
            raise RuntimeError(f"Akte {key}: {exc}") from exc
        if len(faelle) % 100 == 0:
            print(f"{len(faelle)} Akten gesetzt", flush=True)
    manifest = {"schema_version": 1, "faelle": faelle}
    schreiben(ROOT / ZIEL / "bestand.json", (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode())
    print(f"{len(faelle)} Akten mit {sum(len(f['dateien']) for f in faelle)} Schriftfassungen.")


if __name__ == "__main__":
    main()
