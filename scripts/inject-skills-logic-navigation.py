#!/usr/bin/env python3
"""Fügt Plugin-READMEs eine thematische Skill-Navigation hinzu.

Der Block nutzt nur Skillordner-Namen. Skillinhalte, Skillnamen und die
bestehende alphabetische Komplettliste bleiben unverändert.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
BEGIN = "<!-- BEGIN SKILLS-LOGIC (auto-generated) -->"
END = "<!-- END SKILLS-LOGIC (auto-generated) -->"
SKILLS_OVERVIEW_BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="
DISPLAY_OMIT = ("chatgpt", "codex", "assistant", "perplexity", "openai")

GROUPS: list[tuple[str, tuple[str, ...]]] = [
    ("1. Einstieg und Fallrouting", ("kaltstart", "triage", "erstberatung", "ersttermin", "fallaufnahme", "intake", "eingang", "route", "routing", "navigator", "start", "mandat", "mandatsaufnahme", "orientierung", "zielbild")),
    ("2. Unterlagen, Sachverhalt und Quellen", ("akte", "akten", "dokument", "unterlage", "sachverhalt", "beweis", "beleg", "nachweis", "quelle", "recherche", "auskunft", "daten", "matrix", "konto", "verlauf", "luecke", "gutachten", "formular", "auszug")),
    ("3. Prüfung, Anspruch und Subsumtion", ("pruefung", "pruefer", "anspruch", "subsumtion", "tatbestand", "norm", "analyse", "bewertung", "haftung", "risiko", "status", "klassifikation", "check", "rentenbescheid", "altersrente", "erwerbsminderung", "erwerbsminderungsrente", "hinterbliebenenrente", "witwen", "waisen", "grundrente", "abzuege")),
    ("4. Gestaltung, Strategie und Verhandlung", ("gestaltung", "strategie", "vertrag", "klausel", "verhandlung", "vergleich", "plan", "planung", "struktur", "sanierung", "compliance", "konzept", "option", "varianten", "fahrplan", "nachzahlung", "freiwillige", "ausgleich", "abfindung", "betriebsrente", "private-rentenversicherung", "mehrsaeulen")),
    ("5. Verfahren, Behörde und Gericht", ("klage", "widerspruch", "einspruch", "bescheid", "gericht", "sozialgericht", "verfahren", "antrag", "schriftsatz", "urteil", "beschluss", "verfuegung", "vollstreckung", "frist", "register", "behoerde")),
    ("6. Ergebnis, Schreiben und Kommunikation", ("schreiben", "brief", "mandantenbrief", "memo", "vermerk", "entwurf", "bericht", "output", "kommunikation", "antwort", "stellungnahme", "redaktion", "praesentation", "sprechzettel")),
    ("7. Kontrolle, Qualität und Gegenprüfung", ("review", "red-team", "kontrolle", "gegen", "fehler", "plausibil", "validierung", "audit", "qualitaet", "korrektur")),
]

PRIORITY_GROUPS: list[tuple[str, tuple[str, ...]]] = [
    ("7. Kontrolle, Qualität und Gegenprüfung", ("red-team", "qualitygate", "qualitaetsgate")),
    ("6. Ergebnis, Schreiben und Kommunikation", ("versandmappe-endfertig",)),
    ("3. Prüfung, Anspruch und Subsumtion", ("rentenbescheid", "altersrente", "erwerbsminderung", "erwerbsminderungsrente", "hinterbliebene", "hinterbliebenenrente", "grundrente", "kvdr", "uebergangsgeld")),
    ("4. Gestaltung, Strategie und Verhandlung", ("hinzuverdienst", "teilrente", "weiterarbeit", "nachzahlung", "ausgleich", "betriebsrente", "riester", "basisrente", "mehrsaeulen")),
    ("2. Unterlagen, Sachverhalt und Quellen", ("kontenklaerung", "versicherungsverlauf", "auslandszeiten", "kindererziehungszeiten", "pflegezeiten")),
]

EXACT_GROUPS: dict[str, str] = {
    "juristischer-argumentationskern": "3. Prüfung, Anspruch und Subsumtion",
    "einfuehrung-mandantenanliegen": "1. Einstieg und Fallrouting",
    "rollen-und-harness-wahl": "1. Einstieg und Fallrouting",
    "zeugnisart-einfach": "1. Einstieg und Fallrouting",
    "zeugnisart-qualifiziert": "1. Einstieg und Fallrouting",
    "zeugnisart-zwischenzeugnis": "1. Einstieg und Fallrouting",
    "zeugnisart-ausbildungszeugnis-16-bbig": "1. Einstieg und Fallrouting",
    "zeugnisart-praktikum": "1. Einstieg und Fallrouting",
    "stammdaten-erhebung": "2. Unterlagen, Sachverhalt und Quellen",
    "taetigkeitsbeschreibung-erheben": "2. Unterlagen, Sachverhalt und Quellen",
    "besondere-leistungen-projekte": "2. Unterlagen, Sachverhalt und Quellen",
    "mehrere-positionen-im-zeugnis": "2. Unterlagen, Sachverhalt und Quellen",
    "langzeit-arbeitsverhaeltnis": "2. Unterlagen, Sachverhalt und Quellen",
    "bag-leitentscheidungen-beweislast": "3. Prüfung, Anspruch und Subsumtion",
    "bag-leitentscheidungen-notenstufen": "3. Prüfung, Anspruch und Subsumtion",
    "rechtlicher-anker-109-gewo": "3. Prüfung, Anspruch und Subsumtion",
    "notenwahl-modus": "3. Prüfung, Anspruch und Subsumtion",
    "note-1-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-2-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-3-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-4-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "note-5-formeln-leistung": "3. Prüfung, Anspruch und Subsumtion",
    "belastbarkeit-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "engagement-motivation-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "teamarbeit-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "fuehrungskraft-bewertung": "3. Prüfung, Anspruch und Subsumtion",
    "verhalten-vorgesetzte-kollegen-kunden": "3. Prüfung, Anspruch und Subsumtion",
    "compliance-integritaet-formeln": "3. Prüfung, Anspruch und Subsumtion",
    "frequenzadverbien-katalog": "4. Gestaltung, Strategie und Verhandlung",
    "steigerungsadverbien-katalog": "4. Gestaltung, Strategie und Verhandlung",
    "beendigungsgrund-formulieren": "4. Gestaltung, Strategie und Verhandlung",
    "schlussformel-baukasten": "4. Gestaltung, Strategie und Verhandlung",
    "schlussformel-notenwirkung": "4. Gestaltung, Strategie und Verhandlung",
    "revision-und-aenderungswuensche": "5. Verfahren, Behörde und Gericht",
    "auslassungen-vermeiden": "7. Kontrolle, Qualität und Gegenprüfung",
    "geheimcodes-vermeiden": "7. Kontrolle, Qualität und Gegenprüfung",
    "drift-und-schaufenster-vermeiden": "7. Kontrolle, Qualität und Gegenprüfung",
    "zeugnisklarheit-objektiver-empfaengerhorizont": "7. Kontrolle, Qualität und Gegenprüfung",
    "wohlwollensgrundsatz-und-wahrheit": "7. Kontrolle, Qualität und Gegenprüfung",
    "kopfdaten-und-aussere-form": "7. Kontrolle, Qualität und Gegenprüfung",
    "teilzeit-elternzeit-darstellung": "7. Kontrolle, Qualität und Gegenprüfung",
    "versandmappe-endfertigen": "1. Einstieg und Fallrouting",
    "ordneraufnahme-und-produktionsmatrix": "2. Unterlagen, Sachverhalt und Quellen",
    "hauptdokument-pdf-endfertigen": "2. Unterlagen, Sachverhalt und Quellen",
    "anlagen-konvertieren-und-sichtpruefen": "2. Unterlagen, Sachverhalt und Quellen",
    "anlagen-nummerieren-und-stempeln": "4. Gestaltung, Strategie und Verhandlung",
    "signaturweg-und-absender-pruefen": "5. Verfahren, Behörde und Gericht",
    "stoerung-und-nachreichung-dokumentieren": "5. Verfahren, Behörde und Gericht",
    "dateinamen-und-paketgrenzen-pruefen": "7. Kontrolle, Qualität und Gegenprüfung",
    "versandfreigabe-und-eingang-sichern": "7. Kontrolle, Qualität und Gegenprüfung",
}


def natural_key(text: str) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", text.lower())]


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    return REPO / source.removeprefix("./")


def skill_slugs(directory: Path) -> list[str]:
    skills = directory / "skills"
    if not skills.is_dir():
        return []
    return sorted([d.name for d in skills.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()], key=natural_key)


def classify(slug: str) -> str:
    lower = slug.lower()
    if lower in EXACT_GROUPS:
        return EXACT_GROUPS[lower]
    for label, needles in PRIORITY_GROUPS:
        if any(needle in lower for needle in needles):
            return label
    for label, needles in GROUPS:
        if any(needle in lower for needle in needles):
            return label
    return "8. Spezialmodule und Schnittstellen"


def markdown_download_url(repo_path: str) -> str:
    return DOWNLOAD_BASE + quote(repo_path, safe="/")


def format_slugs(slugs: list[str], source: str, limit: int = 18) -> str:
    displayable = [slug for slug in slugs if not any(part in slug.lower() for part in DISPLAY_OMIT)]
    if not displayable:
        return "Siehe alphabetische Komplettliste unten."
    shown = displayable[:limit]
    text = ", ".join(
        f"[`{slug}`]({markdown_download_url(f'{source}/skills/{slug}/SKILL.md')})"
        for slug in shown
    )
    rest = len(displayable) - len(shown)
    if rest > 0:
        text += f", ... plus {rest} weitere"
    return text


def build_block(slugs: list[str], source: str) -> str:
    if len(slugs) < 4:
        return ""
    grouped: dict[str, list[str]] = {}
    for slug in slugs:
        grouped.setdefault(classify(slug), []).append(slug)
    labels = [label for label, _ in GROUPS] + ["8. Spezialmodule und Schnittstellen"]
    lines = [
        BEGIN,
        "",
        "## Orientierung nach Arbeitslogik",
        "",
        "Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.",
        "",
        "English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.",
        "",
        "| Arbeitsphase | Typische Skills |",
        "| --- | --- |",
    ]
    for label in labels:
        items = grouped.get(label)
        if items:
            lines.append(f"| {label} | {format_slugs(items, source)} |")
    lines.extend(["", END])
    return "\n".join(lines)


def inject(readme: Path, block: str) -> bool:
    if not block or not readme.is_file():
        return False
    original = readme.read_text(encoding="utf-8")
    text = original
    if BEGIN in text and END in text:
        start = text.find(BEGIN)
        end = text.find(END, start) + len(END)
        text = text[:start] + block + text[end:]
    elif SKILLS_OVERVIEW_BEGIN in text:
        text = text.replace(SKILLS_OVERVIEW_BEGIN, block + "\n\n" + SKILLS_OVERVIEW_BEGIN, 1)
    else:
        sep = "" if text.endswith("\n\n") else ("\n" if text.endswith("\n") else "\n\n")
        text = text + sep + block + "\n"
    if text == original:
        return False
    readme.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    changed = 0
    total = 0
    for plugin in market["plugins"]:
        directory = plugin_dir(plugin)
        source = directory.relative_to(REPO).as_posix()
        slugs = skill_slugs(directory)
        if not slugs:
            continue
        total += 1
        if inject(directory / "README.md", build_block(slugs, source)):
            changed += 1
            print(f"  UPD {plugin['name']}", flush=True)
    print(f"Fertig: {changed}/{total} READMEs mit Arbeitslogik-Navigation aktualisiert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
