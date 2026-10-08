#!/usr/bin/env python3
"""Baut die eigenständige Immobilien-Übernahme aus dem belegten Quellstand."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "rechtsabteilung-forderungsmanagement-immobilienunternehmen"
COMPANION = "schriftsatzwerkstatt-bea"
PROJECT = ROOT / "projekte" / PLUGIN
SNAPSHOT = PROJECT / "quellstand-v5.27.1.zip"
SOURCE_SHA256 = "bd8b53ae84a99ddff064102fa219dd1f9f5172c98b751f2df0bdaa50975af8bc"
TITLE = "Rechtsabteilung Forderungsmanagement Immobilienunternehmen"
CASES = {
    "mieterhoehung-becker-tempelhof": (
        "Becker: Mieterhöhung",
        "Teilzustimmung, Wohnfläche und belegte Mietspiegelmerkmale statt pauschalem Erhöhungsbetrag.",
    ),
    "mieterklage-schimmel-schulz-verteidigung": (
        "Schulz: Schimmelklage",
        "Zugestellte Mieterklage, technische Gegenbelege, Zutritt und konkrete Verteidigungsfrist.",
    ),
    "mietrueckstand-demir-fuenf-raten-absichtlich": (
        "Demir: fünf offene Mieten",
        "Bewusster Zahlungsstopp, streitiges Fenster, Minderungsbasis und Kündigungsnachweis.",
    ),
    "mietrueckstand-lange-zwei-raten-versehen": (
        "Lange: Bankwechsel und Kulanz",
        "Zwei Mietraten, angekündigte und echte Zahlung sowie eine mehrfach eingereichte Bankanzeige.",
    ),
    "mietrueckstand-meier-wilhelmstrasse": (
        "Meier: Mietrückstand",
        "Vertrag, Mietkonto, Mahnung und Klageentwurf mit getrennter Kündigungsprüfung.",
    ),
    "mietspiegel-berlin": (
        "Berliner Mietspiegel",
        "Referenzmaterial zur Einordnung; konkrete Wohnung, Merkmale und geltenden Stand gesondert prüfen.",
    ),
    "nebenkosten-braun-nachzahlung-unbezahlt": (
        "Braun: Betriebskostennachforderung",
        "Vorauszahlungen, Kostenverteilung, elektronische Belegeinsicht und fehlende Leistungsnachweise.",
    ),
    "raeumungsklage-kowalski-friedrichshain": (
        "Kowalska: Räumung und Zahlung",
        "Kündigung, Räumung, Schonfrist und Zahlung nach Klage mit passender Prozessreaktion.",
    ),
    "ratenplan-riedel-gebrochen": (
        "Riedel: gebrochener Ratenplan",
        "Laufende Miete von Altlasten trennen; neuer Ratenvorschlag ist noch keine Annahme.",
    ),
    "vollstreckung-krueger-titel-teilzahlung": (
        "Krüger: Titel und Teilzahlung",
        "Urteil, Kostenfestsetzung, Tilgungsjournal und beleggebundener Vollstreckungsnachlauf.",
    ),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_member(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, date_time=(2026, 10, 7, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, data)


def unpack_snapshot(destination: Path) -> dict[str, str]:
    if digest(SNAPSHOT.read_bytes()) != SOURCE_SHA256:
        raise ValueError(
            "Quellarchiv stimmt nicht mit dem freigegebenen Importstand überein"
        )
    hashes = {}
    with zipfile.ZipFile(SNAPSHOT) as archive:
        for item in archive.infolist():
            if item.is_dir():
                continue
            relative = PurePosixPath(item.filename)
            if (
                relative.is_absolute()
                or ".." in relative.parts
                or "\\" in item.filename
            ):
                raise ValueError("Unsicherer Quellarchivpfad")
            if item.file_size > 20 * 1024 * 1024:
                raise ValueError("Unerwartet große Quelldatei")
            data = archive.read(item)
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            hashes[item.filename] = digest(data)
    if len(hashes) != 373:
        raise ValueError("Vollkopie muss alle 373 getrackten Dateien enthalten")
    return hashes


def adapt_case_zip(source: Path, target: Path, *, pdf_only: bool) -> int:
    allowed = {".pdf"} if pdf_only else {".docx", ".xlsx", ".pdf"}
    seen = set()
    with zipfile.ZipFile(source) as original, zipfile.ZipFile(target, "w") as output:
        write_member(output, "README.txt", NOTICE_BYTES)
        for item in original.infolist():
            name = item.filename
            if item.is_dir() or "/" in name or "\\" in name or not name.isascii():
                raise ValueError(f"Nicht flacher Arbeitsdateiname: {name}")
            if Path(name).suffix.lower() not in allowed or name.casefold() in seen:
                raise ValueError(f"Unerwartete oder doppelte Arbeitsdatei: {name}")
            seen.add(name.casefold())
            write_member(output, name, original.read(item))
    return len(seen)


def build_cases() -> list[dict]:
    downloads = PROJECT / "downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="immo-import-") as temporary:
        source = Path(temporary)
        hashes = unpack_snapshot(source)
        built = source / "dist"
        subprocess.run(
            [
                sys.executable,
                str(source / "scripts/build-testakten-release-zips.py"),
                str(built),
            ],
            check=True,
            timeout=300,
            cwd=source,
        )
        records = []
        for slug, (title, purpose) in CASES.items():
            base = f"testakte-{slug}"
            native_count = adapt_case_zip(
                built / f"{base}.zip", downloads / f"{base}.zip", pdf_only=False
            )
            pdf_count = adapt_case_zip(
                built / f"{base}-einzel-pdfs.zip",
                downloads / f"{base}-einzel-pdfs.zip",
                pdf_only=True,
            )
            if native_count != pdf_count:
                raise ValueError(
                    f"{slug}: Arbeitsdateien und Einzel-PDFs unvollständig"
                )
            shutil.copyfile(
                built / f"{base}-gesamt.pdf", downloads / f"{base}-gesamt.pdf"
            )
            records.append(
                {
                    "slug": slug,
                    "title": title,
                    "purpose": purpose,
                    "documents": native_count,
                }
            )
        if sum(row["documents"] for row in records) != 174:
            raise ValueError("Erwartet werden 174 Aktenstücke")
        provenance = {
            "title": TITLE,
            "source_repository": "Klotzkette/immobilien-forderungsmanagement",
            "source_tag": "v5.27.1",
            "source_commit": "25475e54dd019ba54242e8ba13c44bdb9042402a",
            "copied_on": "2026-10-07",
            "snapshot_sha256": SOURCE_SHA256,
            "source_files": hashes,
            "cases": records,
            "scope": "Vollständiger getrackter Dateistand, ohne Git-Historie, lokale Ausgaben oder Zugangsdaten. Aktive Marketplace-Fassung separat angepasst.",
        }
        (PROJECT / "herkunft.json").write_text(
            json.dumps(provenance, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    lines = [
        "# Testakten der Immobilien-Rechtsabteilung",
        "",
        "[Projektübersicht](./README.md) · [Fachplugin](../../"
        + PLUGIN
        + "/README.md)",
        "",
        "Zehn Akten, 174 Aktenstücke. Pro Fall nur eine Darreichungsform in denselben Testlauf laden; sonst erscheinen dieselben Belege mehrfach. Die Arbeits-ZIPs enthalten DOCX, XLSX und PDF sowie ausschließlich den vorgeschriebenen Hinweis als README.txt. Beide ZIP-Arten sind flach.",
        "",
        NOTICE_MARKDOWN,
        "",
        "| Fall | Worum es geht | Stücke | Gesamt-PDF | Arbeitsdateien | Einzel-PDFs |",
        "|---|---|---:|---|---|---|",
    ]
    for row in records:
        base = f"./downloads/testakte-{row['slug']}"
        lines.append(
            f"| {row['title']} | {row['purpose']} | {row['documents']} | [PDF]({base}-gesamt.pdf) | [ZIP]({base}.zip) | [ZIP]({base}-einzel-pdfs.zip) |"
        )
    lines.extend(
        [
            "",
            "## Erster Test",
            "",
            "Mit Lange beginnen: Arbeits-ZIP entpacken, Fachplugin aktivieren, Ordner übergeben. Auftrag: `Gleiche Bankanzeige und Mietkonto ab und formuliere die Kulanzantwort.` Die Bankanzeige ist kein zweiter Zahlungseingang. Noch offene Juni-Miete gesondert ausweisen. Für Braun anschließend Kostenverteilung und Belegeinsicht getrennt prüfen; keine automatische Klagefreigabe allein aus dem Systemsaldo.",
            "",
            "Die vollständigen ursprünglichen Fall-READMEs, Quellen und Prüfskripte bleiben in der [Vollkopie](./quellstand-v5.27.1.zip). Sie dokumentieren den damaligen Bearbeitungsstand; die aktiven Einstiege und Downloads stehen hier im großen Repository.",
            "",
        ]
    )
    (PROJECT / "TESTAKTEN.md").write_text("\n".join(lines), encoding="utf-8")
    return records


def build_packages(dist: Path) -> None:
    dist.mkdir(parents=True, exist_ok=True)
    for name in (PLUGIN, COMPANION):
        directory = ROOT / name
        with zipfile.ZipFile(dist / f"{name}.zip", "w") as archive:
            for path in sorted(directory.rglob("*")):
                if (
                    not path.is_file()
                    or path.is_symlink()
                    or "__pycache__" in path.parts
                ):
                    continue
                if (
                    path.name.endswith(("-werkstatt.md", "-schnellstart.md"))
                    or path.name == ".DS_Store"
                ):
                    continue
                write_member(
                    archive, path.relative_to(directory).as_posix(), path.read_bytes()
                )
    # Das Gesamtpaket ist ein Offline-Projekt, kein zusätzlich installierbares Plugin.
    with zipfile.ZipFile(dist / f"{PLUGIN}-vollstaendig.zip", "w") as archive:
        write_member(
            archive,
            "README.txt",
            NOTICE_BYTES
            + b"\nStart: projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md\n",
        )
        start = f"# {TITLE}\n\n[Projekt, Vollkopie und Testakten](./projekte/{PLUGIN}/README.md)\n\nDieses Archiv enthält nur das Immobilienprojekt, nicht die gesamte Rechtssammlung.\n"
        write_member(archive, "README.md", start.encode())
        write_member(archive, "ASSET_INDEX.md", start.encode())
        write_member(archive, "SKILLS.md", start.encode())
        for name in (PLUGIN, COMPANION):
            index = ROOT / "skills-index" / f"{name}.md"
            write_member(archive, f"skills-index/{name}.md", index.read_bytes())
        cases_index = f"# Testakten\n\n[Zehn Immobilienakten](../projekte/{PLUGIN}/TESTAKTEN.md)\n"
        write_member(archive, "testakten/README.md", cases_index.encode())
        install = (
            start
            + f"\n## Installation\n\nFür den Fachprozess das Plugin `{PLUGIN}` verwenden; für die technische Endfertigung `{COMPANION}`. Die jeweiligen installierbaren ZIPs werden separat angeboten. Alternativ einen der beiden Markdown-Prompts aus dem Fachplugin-Verzeichnis öffnen und mit dem Aktenordner bereitstellen. Das Gesamtprojekt-ZIP nicht als zusätzliches Plugin importieren.\n"
        )
        write_member(archive, "INSTALLATION_EINFACH.md", install.encode())
        for directory in (ROOT / PLUGIN, ROOT / COMPANION, PROJECT):
            for path in sorted(directory.rglob("*")):
                if (
                    path.is_file()
                    and not path.is_symlink()
                    and "__pycache__" not in path.parts
                    and path.name != ".DS_Store"
                ):
                    write_member(
                        archive, path.relative_to(ROOT).as_posix(), path.read_bytes()
                    )
    for kind in ("werkstatt", "schnellstart"):
        name = f"{PLUGIN}-{kind}.md"
        shutil.copyfile(ROOT / PLUGIN / name, dist / name)
    for path in sorted((PROJECT / "downloads").glob("*")):
        shutil.copyfile(path, dist / ("rechtsabteilung-immobilien-" + path.name))
    files = sorted(
        path
        for path in dist.iterdir()
        if path.is_file() and path.name != "checksums-sha256.txt"
    )
    (dist / "checksums-sha256.txt").write_text(
        "".join(f"{digest(path.read_bytes())}  {path.name}\n" for path in files),
        encoding="utf-8",
    )
    print(f"Immobilienpaket: {len(files) + 1} Assets in {dist}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cases",
        action="store_true",
        help="Akten aus der geprüften Vollkopie neu bauen",
    )
    parser.add_argument(
        "--dist", type=Path, default=ROOT / "dist" / "rechtsabteilung-immobilien"
    )
    args = parser.parse_args()
    if args.cases:
        build_cases()
    if not (PROJECT / "herkunft.json").is_file():
        parser.error("Zuerst mit --cases die vollständige Aktenkopie erstellen")
    build_packages(args.dist.resolve())


if __name__ == "__main__":
    main()
