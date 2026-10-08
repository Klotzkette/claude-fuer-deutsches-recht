#!/usr/bin/env python3
"""Erzeugt den repoweiten Direktdownloadindex für Haupt- und Sondervorlagen."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import md_in, odt_in, vorlagenordner  # type: ignore  # noqa: E402
from _atomar import text_atomar_schreiben  # type: ignore  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
ZIEL = REPO / "DOWNLOADS.md"
RAW_BASIS = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht"
RELEASE_BASIS = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist"
def h1(datei: Path, fallback: str) -> str:
    if datei.is_file():
        for zeile in datei.read_text(encoding="utf-8").splitlines():
            if zeile.startswith("# "):
                return zeile[2:].strip()
    return fallback


def tabellentext(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def rubric_typ(ordner: Path) -> str:
    rubric = ordner / "rubric.yaml"
    if rubric.is_file():
        for zeile in rubric.read_text(encoding="utf-8").splitlines():
            if zeile.startswith("typ:"):
                wert = zeile.split(":", 1)[1].strip().strip("\"'")
                return {
                    "vertrag": "Vertraglich",
                    "schriftsatz": "Prozessual/Formular",
                    "sonstiges": "Arbeitshilfe",
                    "plan": "Plan/Arbeitsdokument",
                    "vermerk": "Vermerk/Prüfdokument",
                    "text": "AGB/Standardtext",
                }.get(wert, wert)
    return "Nicht zugeordnet"


def bereiche() -> list[tuple[Path, list[Path]]]:
    gruppiert: dict[Path, list[Path]] = {}
    for ordner in vorlagenordner(REPO):
        gruppiert.setdefault(ordner.parent, []).append(ordner)
    return [
        (bereich, sorted(vorlagen))
        for bereich, vorlagen in sorted(
            gruppiert.items(),
            key=lambda eintrag: eintrag[0].name,
        )
    ]


def sonderbereiche() -> list[tuple[Path, list[Path]]]:
    basis = REPO / "vorlagen-gerichtsleitend"
    ergebnis: list[tuple[Path, list[Path]]] = []
    for bereich in sorted(pfad for pfad in basis.iterdir() if pfad.is_dir()):
        vorlagen = sorted(
            datei for datei in bereich.glob("*.md")
            if datei.name != "README.md"
        )
        if vorlagen:
            ergebnis.append((bereich, vorlagen))
    return ergebnis


def render() -> str:
    alle_bereiche = bereiche()
    alle_sonderbereiche = sonderbereiche()
    gesamt = sum(len(vorlagen) for _, vorlagen in alle_bereiche)
    sonder = sum(len(vorlagen) for _, vorlagen in alle_sonderbereiche)
    zeilen = [
        "# Gesamtindex und Direktdownloads",
        "",
        "Dieser Index führt zu jeder Hauptvorlage, ihrer Menüseite und beiden bearbeitbaren Downloadfassungen. Er erschließt außerdem jede gerichtsleitende, staatsanwaltschaftliche und amtsanwaltschaftliche Markdown-Vorlage einzeln. Er wird mit `python3 scripts/build-download-index.py` aus dem kanonischen Bestand erzeugt; einzelne Einträge werden nicht von Hand gepflegt.",
        "",
        "**Navigation:** [Startseite](README.md) · [Nach Dokumenttyp](kategorien/) · [Prozesspakete](prozessvorlagen/) · [Gerichtsleitender Sonderbereich](vorlagen-gerichtsleitend/INDEX.md) · [Arbeitsabläufe](WORKFLOWS.md)",
        "",
        "## Komplettpakete",
        "",
        f"- [Alle ODT-Arbeitsfassungen herunterladen]({RELEASE_BASIS}/vorlagensammlung-recht-odt.zip)",
        f"- [Alle Markdown-Hauptvorlagen herunterladen]({RELEASE_BASIS}/vorlagensammlung-recht-markdown.zip)",
        f"- [Alle gerichtsleitenden Markdown-Vorlagen herunterladen]({RELEASE_BASIS}/vorlagen-gerichtsleitend-markdown.zip)",
        "- [Vollständiges Repository als ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-gesamt.zip)",
        "- [Neueste Veröffentlichung und Prüfsummen öffnen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/docs/experimentell/vorlagensammlung-recht/dist)",
        "",
        f"**Bestand: {gesamt} Hauptvorlagen in {len(alle_bereiche)} Rechtsbereichen sowie {sonder} gerichtsleitende Sondervorlagen.**",
        "",
        "ODT ist die Büroarbeitsfassung. Das Markdown-ZIP enthält die gleichnamige prüfbare Quelle. Vor Verwendung sind immer die Hinweise in der verlinkten Vorlagen-README zu lesen. Im Browser führt `Strg+F` oder `Cmd+F` unmittelbar zu einem Vorlagennamen, Rechtsgebiet oder Suchbegriff.",
        "",
        '<a id="schnellzugriff"></a>',
        "",
        "## Rechtsgebiete im Schnellzugriff",
        "",
        "| Rechtsgebiet | Bestand | Bereichsmenü | Direktdownloads |",
        "| --- | ---: | --- | --- |",
    ]
    for bereich, vorlagen in alle_bereiche:
        bereich_titel = tabellentext(h1(bereich / "README.md", bereich.name))
        zeilen.append(
            f"| {bereich_titel} | {len(vorlagen)} | "
            f"[Menü]({bereich.name}/) | [Downloads](#haupt-{bereich.name}) |"
        )
    zeilen.extend([
        f"| Gerichtsleitender Sonderbereich | {sonder} | "
        "[Gesamtindex](vorlagen-gerichtsleitend/INDEX.md) | "
        "[Einzeldownloads](#gerichtsleitender-sonderbereich) |",
        "",
        "## Hauptvorlagen nach Rechtsbereich",
        "",
    ])
    for bereich, vorlagen in alle_bereiche:
        bereich_titel = h1(bereich / "README.md", bereich.name)
        zeilen.extend([
            f'<a id="haupt-{bereich.name}"></a>',
            "",
            f"### {bereich_titel}",
            "",
            f"[Bereichsmenü öffnen]({bereich.name}/) · {len(vorlagen)} Vorlagen",
            "",
            "| Vorlage | Dokumenttyp | ODT | Markdown |",
            "| --- | --- | --- | --- |",
        ])
        sortiert = sorted(
            vorlagen,
            key=lambda ordner: h1(ordner / "README.md", ordner.name).casefold(),
        )
        for ordner in sortiert:
            md = md_in(ordner)
            odt = odt_in(ordner)
            if md is None or odt is None:
                raise RuntimeError(f"Unvollständige Vorlage: {ordner.relative_to(REPO)}")
            rel = ordner.relative_to(REPO).as_posix()
            titel = tabellentext(h1(ordner / "README.md", h1(md, ordner.name)))
            typ = tabellentext(rubric_typ(ordner))
            zeilen.append(
                f"| [{titel}]({rel}/) | {typ} | "
                f"[ODT]({RAW_BASIS}/{rel}/{odt.name}) | "
                f"[Markdown-ZIP]({RAW_BASIS}/{rel}/{md.name}.zip) |"
            )
        zeilen.extend([
            "",
            "[Zum Schnellzugriff](#schnellzugriff)",
            "",
        ])
    zeilen.extend([
        '<a id="gerichtsleitender-sonderbereich"></a>',
        "",
        "## Gerichtsleitender Sonderbereich",
        "",
        f"Die {sonder} gerichtlichen, staatsanwaltschaftlichen und amtsanwaltschaftlichen Vorlagen sind Markdown-only. Der [gerichtsleitende Gesamtindex](vorlagen-gerichtsleitend/INDEX.md) erläutert ihren Anwendungsbereich; das [gebündelte Markdown-Paket]({RELEASE_BASIS}/vorlagen-gerichtsleitend-markdown.zip) enthält den vollständigen Sonderbestand. Die folgenden Links laden jede Datei auch einzeln unverändert herunter.",
        "",
        "| Bereich | Bestand | Bereichsmenü | Einzeldownloads |",
        "| --- | ---: | --- | --- |",
    ])
    for bereich, vorlagen in alle_sonderbereiche:
        rel_bereich = bereich.relative_to(REPO).as_posix()
        bereich_titel = tabellentext(h1(bereich / "README.md", bereich.name))
        zeilen.append(
            f"| {bereich_titel} | {len(vorlagen)} | "
            f"[Menü]({rel_bereich}/) | [Downloads](#sonder-{bereich.name}) |"
        )
    zeilen.append("")
    for bereich, vorlagen in alle_sonderbereiche:
        rel_bereich = bereich.relative_to(REPO).as_posix()
        bereich_titel = h1(bereich / "README.md", bereich.name)
        zeilen.extend([
            f'<a id="sonder-{bereich.name}"></a>',
            "",
            f"### {bereich_titel}",
            "",
            f"[Bereichsmenü öffnen]({rel_bereich}/) · {len(vorlagen)} Vorlagen",
            "",
            "| Vorlage | Markdown |",
            "| --- | --- |",
        ])
        for datei in sorted(vorlagen, key=lambda pfad: h1(pfad, pfad.stem).casefold()):
            rel = datei.relative_to(REPO).as_posix()
            titel = tabellentext(h1(datei, datei.stem))
            zeilen.append(
                f"| [{titel}]({rel}) | "
                f"[Direkt herunterladen]({RAW_BASIS}/{rel}) |"
            )
        zeilen.extend([
            "",
            "[Zum Schnellzugriff](#schnellzugriff)",
            "",
        ])
    zeilen.extend([
        "Lizenz: Apache-2.0 OR MIT.",
        "",
    ])
    return "\n".join(zeilen)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Nur prüfen, ob DOWNLOADS.md aktuell ist.")
    args = parser.parse_args()
    erwartet = render()
    if args.check:
        if not ZIEL.is_file() or ZIEL.read_text(encoding="utf-8") != erwartet:
            print("build-download-index: DOWNLOADS.md ist nicht aktuell", file=sys.stderr)
            return 1
        print("build-download-index OK (DOWNLOADS.md aktuell)")
        return 0
    text_atomar_schreiben(ZIEL, erwartet)
    print("build-download-index OK (DOWNLOADS.md aktualisiert)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
