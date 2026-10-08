#!/usr/bin/env python3
"""Baut reproduzierbare Komplettpakete für das GitHub-Release."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import sys
import tempfile
import unicodedata
import zipfile
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import (  # type: ignore  # noqa: E402
    md_in,
    odt_in,
    vorlagenordner,
)
from _atomar import text_atomar_schreiben  # type: ignore  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
ZEIT = (2026, 1, 1, 0, 0, 0)
WURZELDOKUMENTE = {
    "CHANGELOG.md", "CLAUDE.md", "CONTRIBUTING.md", "DISCLAIMER.md",
    "DOWNLOADS.md", "EVAL_RESULTS.md", "README.md", "RECHTLICHE-HINWEISE.md",
    "WORKFLOWS.md", "LICENSE-APACHE", "LICENSE-MIT", "IMPORT.json",
}
RELEASE_DATEIEN = (
    "vorlagensammlung-recht-odt.zip",
    "vorlagensammlung-recht-markdown.zip",
    "vorlagen-gerichtsleitend-markdown.zip",
    "vorlagensammlung-recht-gesamt.zip",
    "SHA256SUMS.txt",
)


@dataclass(frozen=True)
class IndexEintrag:
    """Ein maschinen- und browserlesbarer Eintrag eines Release-Pakets."""

    rechtsgebiet: str
    dokumenttyp: str
    titel: str
    datei: str
    hinweise: str
    suchbegriffe: str
    dateigroesse_bytes: int
    sha256: str


def hauptvorlagen() -> list[Path]:
    return vorlagenordner(REPO)


def relative(dateien: set[Path]) -> list[Path]:
    ergebnis: list[Path] = []
    repo_aufgeloest = REPO.resolve()
    for datei in sorted(dateien):
        try:
            rel = datei.relative_to(REPO)
        except ValueError as exc:
            raise RuntimeError(f"Paketdatei liegt außerhalb des Repositories: {datei}") from exc
        if not datei.is_file():
            raise RuntimeError(f"Paketdatei fehlt oder ist keine Datei: {rel}")
        aktuell = REPO
        for teil in rel.parts:
            aktuell = aktuell / teil
            if aktuell.is_symlink():
                raise RuntimeError(f"Symbolischer Link in Release-Paket verboten: {rel}")
        try:
            datei.resolve(strict=True).relative_to(repo_aufgeloest)
        except ValueError as exc:
            raise RuntimeError(f"Paketdatei verweist aus dem Repository: {rel}") from exc
        ergebnis.append(rel)
    return ergebnis


def h1(datei: Path, fallback: str) -> str:
    if datei.is_file():
        for zeile in datei.read_text(encoding="utf-8").splitlines():
            if zeile.startswith("# "):
                return zeile[2:].strip()
    return fallback


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


def suchschluessel(text: str) -> str:
    """Gleicht Umlaute, ASCII-Umschriften und Satzzeichen für die Suche an."""
    zerlegt = unicodedata.normalize("NFKD", text.casefold())
    ohne_akzente = "".join(zeichen for zeichen in zerlegt if not unicodedata.combining(zeichen))
    vereinheitlicht = (
        ohne_akzente.replace("ß", "ss")
        .replace("ae", "a")
        .replace("oe", "o")
        .replace("ue", "u")
    )
    return " ".join(
        "".join(zeichen if zeichen.isalnum() else " " for zeichen in vereinheitlicht).split()
    )


SUCH_STOPPWOERTER = {
    "aber", "alle", "allem", "allen", "aller", "alles", "auch", "auf", "aus",
    "bei", "beim", "bereits", "bis", "dabei", "dadurch", "dafur", "damit", "dann",
    "dass", "dem", "den", "der", "des", "die", "dies", "diese", "diesem", "diesen",
    "dieser", "durch", "eine", "einem", "einen", "einer", "eines", "erst", "fur",
    "gegen", "hat", "haben", "hier", "hinweise", "ihre", "ihren", "ihres", "ist",
    "kann", "mit", "muss", "nach", "nicht", "noch", "oder", "sich", "sind", "sowie",
    "uber", "und", "unter", "verwendung", "vom", "von", "vor", "vorlage", "werden",
    "wie", "wird", "zur", "zum",
}
KURZE_RECHTSBEGRIFFE = {
    "ao", "bfh", "bgh", "bsg", "eu", "eugh", "gg", "ki", "sgb", "stgb", "vg",
}


@lru_cache(maxsize=1)
def aktuelle_version() -> str:
    """Liest den obersten SemVer-Eintrag aus dem Changelog."""
    changelog = (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## (v\d+\.\d+\.\d+)\b", changelog, re.MULTILINE)
    if match is None:
        raise RuntimeError("CHANGELOG.md enthält keinen Versionskopf")
    return match.group(1)


@lru_cache(maxsize=None)
def fachliche_suchbegriffe(*dateien: Path, limit: int = 140) -> str:
    """Verdichtet Hinweise und Muster zu schnellen, vorlagenspezifischen Treffern."""
    teile: list[str] = []
    for datei in dateien:
        if not datei.is_file() or datei.suffix.lower() != ".md":
            continue
        text = datei.read_text(encoding="utf-8")
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"https?://\S+", " ", text)
        fachstart = min(
            (position for marker in ("## Einschlägige Normen", "## Anwendungsbereich")
             if (position := text.find(marker)) >= 0),
            default=0,
        )
        fachtext = text[fachstart:]
        prioritaet = "\n".join(
            zeile for zeile in fachtext.splitlines()
            if zeile.startswith("#") or "§" in zeile or "Art." in zeile or "`" in zeile
        )
        teile.extend((prioritaet, fachtext))
    woerter = suchschluessel("\n".join(teile)).split()
    eindeutig: list[str] = []
    gesehen: set[str] = set()
    for wort in woerter:
        if wort in gesehen or wort in SUCH_STOPPWOERTER:
            continue
        if len(wort) < 3 and wort not in KURZE_RECHTSBEGRIFFE and not wort.isdigit():
            continue
        gesehen.add(wort)
        eindeutig.append(wort)
        if len(eindeutig) == limit:
            break
    return " ".join(eindeutig)


@lru_cache(maxsize=None)
def dateimetadaten(datei: Path) -> tuple[int, str]:
    inhalt = datei.read_bytes()
    return len(inhalt), hashlib.sha256(inhalt).hexdigest()


def navigationsdateien() -> set[Path]:
    dateien = {REPO / name for name in WURZELDOKUMENTE}
    dateien.update(REPO.glob("*/README.md"))
    dateien.update((REPO / "references").glob("*.md"))
    dateien.add(REPO / "vorlagen-gerichtsleitend" / "INDEX.md")
    return dateien


def markdown_dateien(vorlagen: list[Path]) -> list[Path]:
    dateien = navigationsdateien()
    for ordner in vorlagen:
        md = md_in(ordner)
        if md is not None:
            dateien.add(md)
        dateien.add(ordner / "README.md")
    dateien.update((REPO / "kategorien").rglob("README.md"))
    return relative(dateien)


def odt_dateien(vorlagen: list[Path]) -> list[Path]:
    dateien = navigationsdateien()
    for ordner in vorlagen:
        odt = odt_in(ordner)
        if odt is not None:
            dateien.add(odt)
        dateien.add(ordner / "README.md")
    dateien.update(REPO.glob("*.odt"))
    return relative(dateien)


def gerichtsleitende_dateien() -> list[Path]:
    basis = REPO / "vorlagen-gerichtsleitend"
    return relative(set(basis.rglob("*.md")))


def gesamt_dateien() -> list[Path]:
    """Kopiert Dokumente und Hilfsdateien, nie Git-Daten, Ausgaben oder Caches."""
    endungen = {".md", ".odt", ".zip", ".yaml", ".yml", ".json", ".py", ".sh"}
    dateien = set()
    for datei in REPO.rglob("*"):
        teile = datei.relative_to(REPO).parts
        if any(teil in {"dist", "__pycache__"} for teil in teile):
            continue
        if any(teil.startswith(".") and teil not in {".github", ".gitignore", ".gitkeep"} for teil in teile):
            continue
        if datei.is_file() and (datei.suffix in endungen or datei.name in {"LICENSE-MIT", "LICENSE-APACHE", ".gitignore", ".gitkeep"}):
            dateien.add(datei)
    return relative(dateien)


def offline_index(titel: str, eintraege: list[IndexEintrag]) -> bytes:
    eintraege = sorted(
        eintraege,
        key=lambda eintrag: (eintrag.rechtsgebiet.casefold(), eintrag.titel.casefold()),
    )
    rechtsgebiete = sorted({eintrag.rechtsgebiet for eintrag in eintraege}, key=str.casefold)
    dokumenttypen = sorted({eintrag.dokumenttyp for eintrag in eintraege}, key=str.casefold)
    version = aktuelle_version()
    zeilen = [
        "<!doctype html>",
        '<html lang="de">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{html.escape(titel)} · {html.escape(version)}</title>",
        "  <style>",
        "    :root { color-scheme: light; font-family: Aptos, 'Segoe UI', Arial, sans-serif; }",
        "    * { box-sizing: border-box; }",
        "    body { margin: 0; color: #17202a; background: #f4f6f7; line-height: 1.55; }",
        "    .sprunglink { position: absolute; left: 14px; top: -60px; z-index: 10; padding: 10px 14px; background: #ffffff; border: 2px solid #154360; color: #154360; }",
        "    .sprunglink:focus { top: 12px; }",
        "    header { padding: 30px max(20px, calc((100% - 1180px) / 2)); background: #ffffff; border-bottom: 1px solid #ccd1d1; }",
        "    main { max-width: 1180px; margin: 0 auto; padding: 24px 20px 40px; }",
        "    h1 { margin: 0 0 8px; font-size: 28px; letter-spacing: 0; }",
        "    p { margin: 0; max-width: 82ch; }",
        "    header p + p { margin-top: 8px; }",
        "    .filterbereich { padding: 16px; border: 1px solid #ccd1d1; background: #ffffff; }",
        "    label { display: block; margin-bottom: 8px; font-weight: 700; }",
        "    .filter { display: grid; grid-template-columns: minmax(280px, 2fr) minmax(180px, 1fr) minmax(180px, 1fr) auto; gap: 14px; align-items: end; }",
        "    input, select, button { width: 100%; min-height: 44px; padding: 10px 12px; border: 1px solid #7f8c8d; border-radius: 4px; background: #ffffff; color: inherit; font: inherit; }",
        "    button { width: auto; cursor: pointer; font-weight: 700; white-space: nowrap; }",
        "    button:disabled { cursor: default; color: #6c7378; background: #eef0f1; border-color: #bdc3c7; }",
        "    input:focus-visible, select:focus-visible, button:focus-visible, a:focus-visible { outline: 3px solid #2e86c1; outline-offset: 2px; }",
        "    .suchhilfe { margin-top: 8px; color: #5d6d7e; font-size: 14px; }",
        "    .status { margin: 12px 0 0; color: #4d5656; font-variant-numeric: tabular-nums; }",
        "    .leer { margin: 18px 0; padding: 18px; border: 1px solid #d5d8dc; background: #ffffff; font-weight: 700; }",
        "    .table-wrap { margin-top: 18px; overflow-x: auto; border: 1px solid #ccd1d1; background: #ffffff; }",
        "    table { width: 100%; border-collapse: collapse; }",
        "    caption { padding: 10px 12px; text-align: left; font-weight: 700; background: #d6eaf8; }",
        "    th, td { padding: 10px 12px; border-bottom: 1px solid #e5e7e9; text-align: left; vertical-align: top; }",
        "    th { position: sticky; top: 0; background: #eaf2f8; }",
        "    tbody tr:nth-child(even) { background: #f8f9f9; }",
        "    tbody tr:hover, tbody tr:focus-within { background: #eef6fb; }",
        "    tr:last-child td { border-bottom: 0; }",
        "    td:nth-child(3) { min-width: 260px; }",
        "    td:last-child { white-space: nowrap; }",
        "    a { color: #154360; font-weight: 700; text-decoration-thickness: 1px; text-underline-offset: 0.14em; }",
        "    a:hover { text-decoration-thickness: 2px; }",
        "    [hidden] { display: none; }",
        "    @media (max-width: 820px) { .filter { grid-template-columns: 1fr 1fr; } .filter-suche { grid-column: 1 / -1; } }",
        "    @media (max-width: 680px) {",
        "      header { padding-top: 22px; padding-bottom: 22px; }",
        "      main { padding: 18px 14px 30px; }",
        "      .filterbereich { padding: 13px; }",
        "      .filter { grid-template-columns: 1fr; }",
        "      .filter-suche { grid-column: auto; }",
        "      button { width: 100%; }",
        "      .table-wrap { overflow: visible; border: 0; background: transparent; }",
        "      table, tbody, tr, td { display: block; width: 100%; }",
        "      caption { display: block; width: 100%; margin-bottom: 10px; border: 1px solid #ccd1d1; }",
        "      thead { display: none; }",
        "      tbody tr { margin-bottom: 12px; border: 1px solid #ccd1d1; background: #ffffff; }",
        "      tbody tr:nth-child(even) { background: #ffffff; }",
        "      td { display: grid; min-width: 0; grid-template-columns: minmax(112px, 38%) minmax(0, 1fr); gap: 10px; padding: 9px 11px; border-bottom: 1px solid #e5e7e9; overflow-wrap: anywhere; }",
        "      td::before { content: attr(data-label); color: #4d5656; font-weight: 700; }",
        "      td a { min-width: 0; overflow-wrap: anywhere; }",
        "      td:nth-child(3) { min-width: 0; }",
        "      td:last-child { white-space: normal; }",
        "      td:last-child { border-bottom: 0; }",
        "    }",
        "    @media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; } }",
        "    @media print {",
        "      body { background: #ffffff; color: #000000; font-size: 10pt; }",
        "      header, main { max-width: none; padding: 0; }",
        "      .filterbereich, .suchhilfe, .status, .leer { display: none; }",
        "      .table-wrap { overflow: visible; border-color: #777777; }",
        "      th { position: static; background: #eeeeee; }",
        "      a { color: #000000; text-decoration: none; }",
        "      tr { break-inside: avoid; }",
        "    }",
        "  </style>",
        "</head>",
        "<body>",
        '<a class="sprunglink" href="#vorlagenliste">Direkt zur Vorlagenliste</a>',
        "<header>",
        f"  <h1>{html.escape(titel)}</h1>",
        f"  <p><strong>Stand {html.escape(version)}</strong> · {len(eintraege)} Dateien. Suchfeld verwenden und die gewünschte Datei direkt aus dem entpackten Paket öffnen.</p>",
        "  <p>Die Vorlagen sind unverbindliche Muster. Vor jeder Verwendung zuerst die verlinkten Hinweise lesen und den Text fachkundig auf Sachverhalt und aktuellen Rechtsstand prüfen.</p>",
        "</header>",
        '<main id="vorlagenliste">',
        '  <section class="filterbereich" aria-label="Vorlagen filtern">',
        '  <div class="filter" role="search">',
        '    <div class="filter-suche"><label for="suche">Suchbegriffe</label><input id="suche" type="search" placeholder="Kündigung Arbeitsrecht oder Erbschein" autocomplete="off" aria-controls="vorlagen" aria-describedby="suchhilfe trefferstatus"><p id="suchhilfe" class="suchhilfe">Mehrere Wörter werden unabhängig von ihrer Reihenfolge verknüpft. Umlaute und Umschriften wie „ü“ und „ue“ führen zum selben Treffer. Taste / setzt den Fokus.</p></div>',
        '    <div><label for="rechtsgebiet">Rechtsgebiet</label><select id="rechtsgebiet" aria-controls="vorlagen"><option value="">Alle Rechtsgebiete</option>',
    ]
    zeilen.extend(
        f'      <option value="{html.escape(suchschluessel(rechtsgebiet), quote=True)}">{html.escape(rechtsgebiet)}</option>'
        for rechtsgebiet in rechtsgebiete
    )
    zeilen.extend([
        "    </select></div>",
        '    <div><label for="dokumenttyp">Dokumenttyp</label><select id="dokumenttyp" aria-controls="vorlagen"><option value="">Alle Dokumenttypen</option>',
    ])
    zeilen.extend(
        f'      <option value="{html.escape(suchschluessel(dokumenttyp), quote=True)}">{html.escape(dokumenttyp)}</option>'
        for dokumenttyp in dokumenttypen
    )
    zeilen.extend([
        "    </select></div>",
        '    <button id="zuruecksetzen" type="button" aria-controls="vorlagen" disabled>Filter zurücksetzen</button>',
        "  </div>",
        f'  <p id="trefferstatus" class="status" aria-live="polite" aria-atomic="true">{len(eintraege)} Dateien angezeigt</p>',
        "  </section>",
        '  <p id="leer" class="leer" hidden>Keine Vorlage passt zu diesen Filtern. Suchbegriffe kürzen oder Filter zurücksetzen.</p>',
        '  <div class="table-wrap">',
        "    <table>",
        "      <caption>Vorlagen nach Rechtsgebiet</caption>",
        "      <thead><tr><th scope=\"col\">Rechtsgebiet</th><th scope=\"col\">Dokumenttyp</th><th scope=\"col\">Vorlage und Hinweise</th><th scope=\"col\">Arbeitsdatei</th></tr></thead>",
        '      <tbody id="vorlagen">',
    ])
    for eintrag in eintraege:
        suchtext = html.escape(
            suchschluessel(
                f"{eintrag.rechtsgebiet} {eintrag.dokumenttyp} {eintrag.titel} "
                f"{eintrag.datei} {eintrag.suchbegriffe}"
            ),
            quote=True,
        )
        rechtsgebiet = html.escape(suchschluessel(eintrag.rechtsgebiet), quote=True)
        dokumenttyp = html.escape(suchschluessel(eintrag.dokumenttyp), quote=True)
        href = html.escape(eintrag.datei, quote=True)
        hinweis_href = html.escape(eintrag.hinweise, quote=True)
        link_titel = html.escape(eintrag.titel, quote=True)
        zeilen.append(
            f'        <tr data-search="{suchtext}" data-rechtsgebiet="{rechtsgebiet}" data-dokumenttyp="{dokumenttyp}">'
            f'<td data-label="Rechtsgebiet">{html.escape(eintrag.rechtsgebiet)}</td>'
            f'<td data-label="Dokumenttyp">{html.escape(eintrag.dokumenttyp)}</td>'
            f'<td data-label="Vorlage"><a href="{hinweis_href}" aria-label="Hinweise zu {link_titel} lesen">{html.escape(eintrag.titel)}</a></td>'
            f'<td data-label="Arbeitsdatei"><a href="{href}" aria-label="Arbeitsdatei {link_titel} öffnen">Datei öffnen</a></td></tr>'
        )
    zeilen.extend([
        "      </tbody>",
        "    </table>",
        "  </div>",
        "</main>",
        "<script>",
        "  const feld = document.getElementById('suche');",
        "  const rechtsgebiet = document.getElementById('rechtsgebiet');",
        "  const dokumenttyp = document.getElementById('dokumenttyp');",
        "  const zuruecksetzen = document.getElementById('zuruecksetzen');",
        "  const zeilen = [...document.querySelectorAll('tbody tr')];",
        "  const trefferstatus = document.getElementById('trefferstatus');",
        "  const leer = document.getElementById('leer');",
        f"  const gesamt = {len(eintraege)};",
        "  let geplanterLauf = 0;",
        "  function normalisieren(text) {",
        "    return text.toLocaleLowerCase('de').normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').replace(/ß/g, 'ss').replace(/ae/g, 'a').replace(/oe/g, 'o').replace(/ue/g, 'u').replace(/[^a-z0-9]+/g, ' ').trim();",
        "  }",
        "  function filtern() {",
        "    const begriffe = normalisieren(feld.value).split(' ').filter(Boolean);",
        "    const gebiet = rechtsgebiet.value;",
        "    const typ = dokumenttyp.value;",
        "    const filterAktiv = begriffe.length > 0 || Boolean(gebiet) || Boolean(typ);",
        "    let sichtbar = 0;",
        "    for (const zeile of zeilen) {",
        "      const passt = begriffe.every(begriff => zeile.dataset.search.includes(begriff)) && (!gebiet || zeile.dataset.rechtsgebiet === gebiet) && (!typ || zeile.dataset.dokumenttyp === typ);",
        "      zeile.hidden = !passt;",
        "      if (passt) sichtbar += 1;",
        "    }",
        "    trefferstatus.textContent = filterAktiv ? `${sichtbar} von ${gesamt} Dateien angezeigt` : `${gesamt} Dateien angezeigt`;",
        "    leer.hidden = sichtbar !== 0;",
        "    zuruecksetzen.disabled = !filterAktiv;",
        "  }",
        "  function filternPlanen() {",
        "    window.clearTimeout(geplanterLauf);",
        "    geplanterLauf = window.setTimeout(filtern, 80);",
        "  }",
        "  feld.addEventListener('input', filternPlanen);",
        "  rechtsgebiet.addEventListener('change', filtern);",
        "  dokumenttyp.addEventListener('change', filtern);",
        "  zuruecksetzen.addEventListener('click', () => { window.clearTimeout(geplanterLauf); feld.value = ''; rechtsgebiet.value = ''; dokumenttyp.value = ''; filtern(); feld.focus(); });",
        "  document.addEventListener('keydown', ereignis => {",
        "    const eingabeAktiv = ['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName);",
        "    if (ereignis.key === '/' && !eingabeAktiv && !ereignis.metaKey && !ereignis.ctrlKey && !ereignis.altKey) { ereignis.preventDefault(); feld.focus(); }",
        "    if (ereignis.key === 'Escape' && eingabeAktiv && !zuruecksetzen.disabled) { zuruecksetzen.click(); }",
        "  });",
        "</script>",
        "</body>",
        "</html>",
        "",
    ])
    return "\n".join(zeilen).encode("utf-8")


def haupt_eintraege(vorlagen: list[Path], endung: str) -> list[IndexEintrag]:
    eintraege: list[IndexEintrag] = []
    for ordner in vorlagen:
        bereich = ordner.parent
        bereich_titel = h1(bereich / "README.md", bereich.name)
        name = h1(ordner / "README.md", ordner.name)
        datei = odt_in(ordner) if endung == "odt" else md_in(ordner)
        if datei is None:
            raise RuntimeError(f"Fehlende {endung.upper()}-Datei: {ordner.relative_to(REPO)}")
        groesse, digest = dateimetadaten(datei)
        eintraege.append(IndexEintrag(
            rechtsgebiet=bereich_titel,
            dokumenttyp=rubric_typ(ordner),
            titel=name,
            datei=datei.relative_to(REPO).as_posix(),
            hinweise=(ordner / "README.md").relative_to(REPO).as_posix(),
            suchbegriffe=fachliche_suchbegriffe(ordner / "README.md"),
            dateigroesse_bytes=groesse,
            sha256=digest,
        ))
    return eintraege


def sonder_eintraege() -> list[IndexEintrag]:
    basis = REPO / "vorlagen-gerichtsleitend"
    eintraege: list[IndexEintrag] = []
    for bereich in sorted(pfad for pfad in basis.iterdir() if pfad.is_dir()):
        bereich_titel = h1(bereich / "README.md", bereich.name)
        if bereich.name == "amtsanwaltschaft":
            dokumenttyp = "Amtsanwaltschaftlich"
        elif bereich.name.startswith("staatsanwaltschaft-"):
            dokumenttyp = "Staatsanwaltschaftlich"
        else:
            dokumenttyp = "Gerichtsleitend"
        for datei in sorted(
            pfad for pfad in bereich.glob("*.md") if pfad.name != "README.md"
        ):
            groesse, digest = dateimetadaten(datei)
            eintraege.append(IndexEintrag(
                rechtsgebiet=bereich_titel,
                dokumenttyp=dokumenttyp,
                titel=h1(datei, datei.stem),
                datei=datei.relative_to(REPO).as_posix(),
                hinweise=(bereich / "README.md").relative_to(REPO).as_posix(),
                suchbegriffe=fachliche_suchbegriffe(datei, bereich / "README.md"),
                dateigroesse_bytes=groesse,
                sha256=digest,
            ))
    return eintraege


def manifest(titel: str, eintraege: list[IndexEintrag]) -> bytes:
    sortiert = sorted(
        eintraege,
        key=lambda eintrag: (eintrag.rechtsgebiet.casefold(), eintrag.titel.casefold()),
    )
    daten = {
        "schema_version": 2,
        "version": aktuelle_version(),
        "titel": titel,
        "anzahl": len(sortiert),
        "lizenz": "Apache-2.0 OR MIT",
        "integritaet": "sha256 bezeichnet jeweils die entpackte Arbeitsdatei",
        "eintraege": [asdict(eintrag) for eintrag in sortiert],
    }
    return (json.dumps(daten, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def pruefe_indexziele(paketname: str, dateien: list[Path], eintraege: list[IndexEintrag]) -> None:
    paketpfade = {datei.as_posix() for datei in dateien}
    gesehen: set[str] = set()
    doppelt: set[str] = set()
    for eintrag in eintraege:
        if eintrag.datei in gesehen:
            doppelt.add(eintrag.datei)
        gesehen.add(eintrag.datei)
    if doppelt:
        raise RuntimeError(f"Doppelte Indexziele in {paketname}: {', '.join(sorted(doppelt))}")
    fehlend = sorted(
        pfad
        for eintrag in eintraege
        for pfad in (eintrag.datei, eintrag.hinweise)
        if pfad not in paketpfade
    )
    if fehlend:
        raise RuntimeError(f"Indexziele fehlen in {paketname}: {', '.join(fehlend)}")


def zip_schreiben(
    ziel: Path,
    dateien: list[Path],
    zusaetzliche_dateien: dict[str, bytes] | None = None,
) -> None:
    archivnamen = [pfad.as_posix() for pfad in dateien]
    archivnamen.extend((zusaetzliche_dateien or {}).keys())
    normiert: dict[str, str] = {}
    for name in archivnamen:
        pfad = PurePosixPath(name)
        teile = name.split("/")
        windows_laufwerk = (
            bool(teile)
            and len(teile[0]) == 2
            and teile[0][0].isalpha()
            and teile[0][1] == ":"
        )
        windows_unzulaessig = any(
            teil.endswith((" ", "."))
            or any(ord(zeichen) < 32 or zeichen in '<>:"|?*' for zeichen in teil)
            for teil in teile
        )
        if (
            not name
            or "\x00" in name
            or "\\" in name
            or pfad.is_absolute()
            or any(teil in ("", ".", "..") for teil in teile)
            or windows_laufwerk
            or windows_unzulaessig
        ):
            raise RuntimeError(f"Unsicherer Pfad im Release-Paket: {name!r}")
        schluessel = unicodedata.normalize("NFC", name).casefold()
        if schluessel in normiert:
            raise RuntimeError(
                "Doppelter oder plattformabhängig kollidierender Pfad im "
                f"Release-Paket: {normiert[schluessel]!r} und {name!r}"
            )
        normiert[schluessel] = name

    ziel.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=ziel.parent,
        prefix=f".{ziel.name}.",
        suffix=".tmp",
        delete=False,
    ) as temporaer:
        temp_pfad = Path(temporaer.name)
    try:
        with zipfile.ZipFile(temp_pfad, "w", compression=zipfile.ZIP_DEFLATED) as archiv:
            for rel in dateien:
                info = zipfile.ZipInfo(rel.as_posix(), date_time=ZEIT)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (0o644 & 0xFFFF) << 16
                archiv.writestr(info, (REPO / rel).read_bytes())
            for name, inhalt in sorted((zusaetzliche_dateien or {}).items()):
                info = zipfile.ZipInfo(name, date_time=ZEIT)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (0o644 & 0xFFFF) << 16
                archiv.writestr(info, inhalt)
        with zipfile.ZipFile(temp_pfad, "r") as pruefung:
            defekt = pruefung.testzip()
            if defekt is not None:
                raise RuntimeError(f"CRC-Fehler im neuen Paket {ziel.name}: {defekt}")
        temp_pfad.chmod(0o644)
        temp_pfad.replace(ziel)
    finally:
        if temp_pfad.exists():
            temp_pfad.unlink()


def paketset_bauen(ausgabe: Path) -> int:
    """Baut ein vollständiges Release-Paketset in ein leeres Staging-Verzeichnis."""
    ausgabe.mkdir(parents=True, exist_ok=True)
    vorlagen = hauptvorlagen()
    odt_eintraege = haupt_eintraege(vorlagen, "odt")
    markdown_eintraege = haupt_eintraege(vorlagen, "md")
    gerichtsleitende_eintraege = sonder_eintraege()
    pakete = {
        "vorlagensammlung-recht-odt.zip": (
            odt_dateien(vorlagen),
            "ODT-Vorlagen – Offline-Index",
            odt_eintraege,
        ),
        "vorlagensammlung-recht-markdown.zip": (
            markdown_dateien(vorlagen),
            "Markdown-Vorlagen – Offline-Index",
            markdown_eintraege,
        ),
        "vorlagen-gerichtsleitend-markdown.zip": (
            gerichtsleitende_dateien(),
            "Gerichtsleitende Vorlagen – Offline-Index",
            gerichtsleitende_eintraege,
        ),
        "vorlagensammlung-recht-gesamt.zip": (
            gesamt_dateien(),
            "Vollständige Vorlagensammlung – Offline-Index",
            markdown_eintraege + gerichtsleitende_eintraege,
        ),
    }
    summen: list[str] = []
    for name, (dateien, titel, eintraege) in pakete.items():
        if not dateien:
            raise RuntimeError(f"Leeres Release-Paket: {name}")
        pruefe_indexziele(name, dateien, eintraege)
        ziel = ausgabe / name
        zusatz = {
            "index.html": offline_index(titel, eintraege),
            "manifest.json": manifest(titel, eintraege),
        }
        zip_schreiben(ziel, dateien, zusatz)
        digest = hashlib.sha256(ziel.read_bytes()).hexdigest()
        summen.append(f"{digest}  {name}")
        print(f"OK  {name} ({len(dateien)} Dateien, index.html und manifest.json)")
    text_atomar_schreiben(
        ausgabe / "SHA256SUMS.txt",
        "\n".join(summen) + "\n",
        encoding="ascii",
    )
    return len(vorlagen)


def paketset_veroeffentlichen(staging: Path, ausgabe: Path) -> None:
    """Ersetzt das komplette Paketset mit Rückfall auf die letzte gute Fassung."""
    ausgabe.mkdir(parents=True, exist_ok=True)
    fehlend = [name for name in RELEASE_DATEIEN if not (staging / name).is_file()]
    if fehlend:
        raise RuntimeError("Staging unvollständig: " + ", ".join(fehlend))
    with tempfile.TemporaryDirectory(
        dir=ausgabe.parent,
        prefix=f".{ausgabe.name}.sicherung.",
    ) as sicherung_name:
        sicherung = Path(sicherung_name)
        vorhanden: set[str] = set()
        for name in RELEASE_DATEIEN:
            ziel = ausgabe / name
            if ziel.is_file():
                shutil.copy2(ziel, sicherung / name)
                vorhanden.add(name)
        ersetzt: list[str] = []
        try:
            for name in RELEASE_DATEIEN:
                (staging / name).replace(ausgabe / name)
                ersetzt.append(name)
        except OSError:
            for name in ersetzt:
                ziel = ausgabe / name
                if name in vorhanden:
                    (sicherung / name).replace(ziel)
                elif ziel.exists():
                    ziel.unlink()
            raise


def release_bauen(ausgabe: Path) -> int:
    """Baut erst vollständig im Staging und veröffentlicht danach als Paketset."""
    ausgabe.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        dir=ausgabe.parent,
        prefix=f".{ausgabe.name}.staging.",
    ) as staging_name:
        staging = Path(staging_name)
        anzahl = paketset_bauen(staging)
        paketset_veroeffentlichen(staging, ausgabe)
    return anzahl


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="dist", help="Ausgabeverzeichnis, standardmäßig dist/.")
    args = parser.parse_args()
    ausgabe = (REPO / args.output_dir).resolve()
    anzahl = release_bauen(ausgabe)
    print(
        "build-release-assets OK "
        f"({anzahl} Hauptvorlagen, 4 Pakete und SHA256SUMS.txt)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
