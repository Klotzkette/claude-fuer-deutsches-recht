#!/usr/bin/env python3
"""Ergänzt drei veröffentlichte Akten-ZIPs um die Belege der Praxisrunde."""
import argparse
import hashlib
import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/pluginakten-praxis-2026-11-19"
# Hashes der unveränderten Originalausgaben auf GitHub (v445.35.3).
BASIS = {
    "arbeitszeugnisgenerator": "b4b2e458d8c6933ef4646b9ee256d33d1eea20249725e0ad723c5a883731609d",
    "arbeitszeugnispruefer": "b4b2e458d8c6933ef4646b9ee256d33d1eea20249725e0ad723c5a883731609d",
    "bautraegervertragspruefer": "68550e7d53693f9257ea9220bfd7433167c95eb230ae170fb3be7a8a2b158bbf",
}
NOTICE = ("Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.\n\n"
          "This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.\n\n")
INTRO = {
    "arbeitszeugnisgenerator": (
        "Arbeitsauftrag für das Personalbüro\n\n"
        "Würzburg: Welchen Beitrag zur Heimversorgung können Sie Gunhilde Brachvogel-Riemenschneider im Endzeugnis persönlich zuschreiben? "
        "Prüfen Sie ihre Zuständigkeit, die Aussage des Inhabers und die Vergleichszeiträume im Kassenjournal. "
        "Marktredwitz: Entwerfen Sie für Reinhilde Eisenträger ein Zwischenzeugnis zur bevorstehenden Elternzeit. "
        "Prüfen Sie, welche Kreditentscheidungen sie selbst treffen durfte. Lesen Sie bei der zweiten Bearbeitung die Journalnachträge. "
        "Die zehn früheren Personalakten mit internen Bewertungsnotizen und die Zeugnisse liegen getrennt von den offenen Eingangsbelegen."
    ),
    "arbeitszeugnispruefer": (
        "Arbeitsauftrag zur Zeugnisprüfung\n\n"
        "Vergleichen Sie Greifenklaus Zeugnis 08 mit dem Schichtjournal aus Bautzen. Wer hat die Notlösung entwickelt und wer hat sie an diesem Nachmittag umgesetzt? "
        "Nehmen Sie die E-Mail der Direktorin erst zur zweiten Runde hinzu. Der Floristikvorgang betrifft eine andere Person und ein anderes Unternehmen. "
        "Prüfen Sie dort, wer die Kasse gezählt hat und was beim Schichtwechsel dokumentiert wurde. Errechnen Sie die mögliche Restdifferenz am Beleg. "
        "Die spätere Nachricht über den Umschlag stammt aus der Buchhaltung. Die historischen Vollvermerke liegen separat."
    ),
    "bautraegervertragspruefer": (
        "Arbeitsauftrag zum Bauträgererwerb\n\n"
        "Berlin: Stellen Sie für Wohnung 4.27 aus Vertrag, Bankbuchung und Datenraumprotokoll fest, welche Abreden und Unterlagen vor der Beurkundung belegbar sind. "
        "Hamburg: Klären Sie für C-2.14, welchen Betrag die Buchhaltung anfordert, wo die Reservierung erscheint, welche Baustelle die Fotos betreffen und welche Mitteilungen noch fehlen. "
        "Die getrennten UR-Nummern und Parteien bleiben während der gesamten Prüfung maßgeblich. "
        "Geben Sie die Unterlagen unter Nachreichungen erst nach der ersten Einschätzung frei."
    ),
}


def package(plugin, basis, target):
    source = basis / f"{plugin}-testakte.zip"
    if hashlib.sha256(source.read_bytes()).hexdigest() != BASIS[plugin]:
        raise ValueError(f"Falsche Originalausgabe: {source}")
    with ZipFile(source) as original:
        files = {name: original.read(name) for name in original.namelist()}
        if len(files) != len(original.infolist()):
            raise ValueError(f"Doppelte Originalpfade: {plugin}")
    # Die historische README bleibt im Bestand bytegleich zugänglich.
    files["Historie/README.txt"] = files.pop("README.txt")
    files["README.txt"] = (NOTICE + INTRO[plugin] + "\n").encode()
    local = ROOT / plugin / "testakte"
    # Die historische ZIP-Auswahl ließ Markdown-Quelldokumente weg. Zur
    # Vorführung werden sie neben den bestehenden Office-/PDF-Fassungen benötigt.
    for path in sorted(local.rglob("*.md")):
        if path.name != "README.md":
            folder = "Personalunterlagen" if "personalakten-fuer-zeugniserstellung" in path.parts else "Historische_Fachunterlagen"
            files[f"{folder}/{path.relative_to(local).as_posix()}"] = path.read_bytes()
    for path in sorted((DATA / plugin).rglob("*")):
        if path.is_file():
            name = path.relative_to(DATA / plugin).as_posix()
            if name in files or path.read_bytes() in files.values():
                raise ValueError(f"Nachtrag kollidiert mit dem Bestand: {name}")
            files[name] = path.read_bytes()

    target.mkdir(parents=True, exist_ok=True)
    final = target / f"{plugin}-mit-nachtrag.zip"
    with tempfile.NamedTemporaryFile(dir=target, delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        with ZipFile(tmp_path, "w") as archive:
            for name, content in sorted(files.items()):
                member = ZipInfo(name, (2026, 11, 19, 0, 0, 0))
                member.compress_type = ZIP_DEFLATED
                member.create_system = 3
                member.external_attr = 0o100644 << 16
                archive.writestr(member, content)
        with ZipFile(tmp_path) as archive:
            if archive.testzip() or archive.namelist() != sorted(files):
                raise ValueError(f"Fehler im ZIP-Verzeichnis: {plugin}")
            if any(archive.read(name) != content for name, content in files.items()):
                raise ValueError(f"Geänderter Dateiinhalt: {plugin}")
        os.replace(tmp_path, final)
    finally:
        tmp_path.unlink(missing_ok=True)
    print(f"{final.name}: {len(files)} Dateien")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--basis", type=Path, required=True, help="Ordner mit drei Original-ZIPs aus v445.35.3")
    parser.add_argument("--dist", type=Path, required=True, help="Zielordner für die drei Vollakten")
    args = parser.parse_args()
    for plugin in BASIS:
        package(plugin, args.basis, args.dist)


if __name__ == "__main__":
    main()
