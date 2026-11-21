#!/usr/bin/env python3
"""Legt eine neue lokale Arbeitsakte als ZIP an. Benötigt ausschließlich Python 3."""

import argparse
import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROLLEN = {
    "anwalt": "Mandatsakte",
    "notar": "Notarielle_Nebenakte",
    "buero": "Buerovorgang",
    "klaerung": "Geschuetzter_Pruefeingang",
}


def lese_stamm(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    fields = ("aktenzeichen", "kurzrubrum", "rolle", "auftrag", "zustaendig", "konfliktstatus")
    if not isinstance(data, dict) or any(not isinstance(data.get(k), str) or not data[k].strip() for k in fields):
        raise ValueError("Der Aktenstamm braucht " + ", ".join(fields) + ".")
    if data["rolle"] not in ROLLEN or data["konfliktstatus"] not in {"offen", "geprueft", "hindernis"}:
        raise ValueError("Rolle oder Konfliktstatus ist ungültig.")
    offene_punkte = data.get("offene_punkte", [])
    if not isinstance(offene_punkte, list) or any(not isinstance(s, str) or not s.strip() for s in offene_punkte):
        raise ValueError("Offene Punkte müssen als Liste von Texten vorliegen.")
    if data["rolle"] != "klaerung" and data["konfliktstatus"] != "geprueft":
        raise ValueError("Bei ungeklärter Berechtigung oder einem Hindernis nur die Rolle klaerung verwenden.")
    return data


def akte_anlegen(stamm, eingang, ausgabe):
    data = lese_stamm(stamm)
    if not eingang.is_dir() or eingang.is_symlink():
        raise ValueError("Ein eigener Eingangsordner mit den ausgewählten Originalen ist erforderlich.")
    if ausgabe.suffix.lower() != ".zip" or not ausgabe.parent.is_dir():
        raise ValueError("Für die ZIP-Datei einen bestehenden Zielordner angeben.")
    eingang = eingang.resolve()
    if any(eingang == p or eingang in p.parents for p in (ausgabe.resolve(), stamm.resolve())):
        raise ValueError("Aktenstamm und neue ZIP-Datei müssen außerhalb des Eingangsordners liegen.")
    root = ROLLEN[data["rolle"]] + "/"
    belegliste = []
    namen = set()
    with tempfile.TemporaryDirectory(dir=ausgabe.parent) as tmp:
        temp = Path(tmp) / "arbeitsakte.zip"
        with ZipFile(temp, "w", compression=ZIP_DEFLATED) as archive:
            for path in sorted(eingang.rglob("*")):
                rel = path.relative_to(eingang)
                if rel.name in {".DS_Store", "Thumbs.db"}:
                    continue
                if any(p.startswith(".") for p in rel.parts):
                    raise ValueError("Versteckten Eintrag vor dem Export zuordnen: " + str(rel))
                if path.is_symlink() or not (path.is_file() or path.is_dir()):
                    raise ValueError("Nur reguläre Originaldateien sind zulässig: " + str(rel))
                if path.is_dir():
                    continue
                key = rel.as_posix()
                if any(ord(c) < 32 or c in "\\:" for c in key) or key.casefold() in namen:
                    raise ValueError("Dateiname ist im Austauschformat nicht eindeutig: " + key)
                namen.add(key.casefold())
                digest = hashlib.sha256()
                count = 0
                with path.open("rb") as src, archive.open(root + "01_Eingang/" + key, "w", force_zip64=True) as dst:
                    start = os.fstat(src.fileno())
                    if not stat.S_ISREG(start.st_mode):
                        raise ValueError("Keine reguläre Datei: " + key)
                    for block in iter(lambda: src.read(1024 * 1024), b""):
                        dst.write(block)
                        digest.update(block)
                        count += len(block)
                    end = os.fstat(src.fileno())
                    if count != start.st_size or start.st_mtime_ns != end.st_mtime_ns:
                        raise ValueError("Original wurde beim Einlesen verändert: " + key)
                belegliste.append({"datei": key, "bytes": count, "sha256": digest.hexdigest()})
            for name, value in (("Aktenstamm", data), ("Originalverzeichnis", belegliste)):
                archive.writestr(root + name + ".json", (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode())
            aufgaben = ["Offene Aufgaben", "", *["- " + p for p in data.get("offene_punkte", [])]]
            archive.writestr(root + "02_Bearbeitung/Offene_Aufgaben.txt", ("\n".join(aufgaben) + "\n").encode())
        # Die neue Datei erscheint vollständig oder gar nicht, auch bei zwei gleichzeitigen Anlagen.
        temp.chmod(0o600)
        os.link(temp, ausgabe)
    return len(belegliste)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for option in ("stamm", "eingang", "ausgabe"):
        parser.add_argument("--" + option, type=Path, required=True)
    args = parser.parse_args()
    try:
        anzahl = akte_anlegen(args.stamm, args.eingang, args.ausgabe)
    except FileExistsError:
        parser.exit(1, "Die Zieldatei existiert bereits. Einen freien Namen verwenden.\n")
    except (OSError, ValueError) as exc:
        parser.exit(1, str(exc) + "\n")
    print(f"{args.ausgabe}: Arbeitsakte mit {anzahl} Originaldateien angelegt.")


if __name__ == "__main__":
    main()
