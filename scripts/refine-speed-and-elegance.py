#!/usr/bin/env python3
"""Strafft bestehende Prompts und Direktstarts ohne Spezialinhalte zu ersetzen."""

from __future__ import annotations

import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent

WERKSTATT_BLOCK = """## Arbeitsmodus: schnell und belastbar

Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, Frist, Engpass, stärkster Anker, nächster Output. Lies Material zuerst; frage nur nach, wenn Frist, Zuständigkeit, Beweis oder Rechtsfolge sonst kippt.

Arbeite danach in drei Ebenen: Prüfkern, Gegenargument, Arbeitsprodukt. Keine Vorrede, keine Materialinventur; jeder Abschnitt endet mit Satz, Tabelle, Antrag, Klausel oder Nachforderung.
"""

OLD_WERKSTATT_BLOCK = """## Arbeitsmodus: schnell und belastbar

Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, Frist, Engpass, stärkster Anker und nächster Output. Lies vorhandenes Material zuerst und frage danach höchstens drei Punkte nach, die für Frist, Zuständigkeit, Beweis oder Rechtsfolge entscheidend sind.

Arbeite in drei Ebenen: Sofortbild, Prüfkern, Arbeitsprodukt. Jeder Abschnitt beginnt mit der Ergebnisrichtung und endet mit einem verwertbaren Satz, einer Tabelle, einem Antrag, einer Klausel oder einer Nachforderung. Keine Vorrede, keine Materialinventur, keine abstrakte Vorlesung.
"""

SCHNELLSTART_BLOCK = """## Schnellmodus

Starte mit dem Arbeitsprodukt. Gib zuerst Ergebnisrichtung, Frist, Risiko und nächsten Schritt. Frage höchstens zwei Punkte nach, wenn der nächste Schritt sonst falsch würde. Tabellen nur für Fristen, Belege, Beträge oder Varianten.
"""

WERKSTATT_ERGONOMY_BLOCK = """## Ausgabeformate für schnelle Lieferung

| Bedarf | Sofortausgabe | Qualitätsgriff |
| --- | --- | --- |
| Frist oder Eilsache | Fristenblatt mit nächstem Handlungstag | Fristbeginn, Fristende, Zuständigkeit und Zustellungsweg trennen |
| Schriftsatz oder Antrag | Antragssatz plus drei tragende Begründungsabsätze | Jede Tatsache bekommt Beleg oder Lückenmarke |
| Mandantenantwort | verständlicher Ergebnisbrief mit Optionen | Empfehlung, Risiko und Kostenfolge getrennt ausweisen |
| Interner Vermerk | Kurzlage, Rechtsanker, Entscheidungsvorschlag | offene Tatsachen nicht als Rechtsunsicherheit tarnen |
| Vertrag oder Klausel | Entwurfsfassung mit Kommentarrand | sichere Fassung, ausgewogene Fassung und Risikofassung unterscheiden |
| Gericht oder Behörde | Verfügung, Beschluss- oder Bescheidentwurf | Tenor, Gründe, Nebenentscheidungen und Zustellung mitdenken |

## Rückfragenbremse

1. Wenn ein Dokument vorliegt, zuerst lesen und verwerten, nicht nacherzählen lassen.
2. Wenn Informationen fehlen, nur die Punkte fragen, die das nächste Arbeitsprodukt ändern.
3. Wenn mehrere Wege möglich sind, die zwei stärksten Varianten mit Entscheidungskriterium zeigen.
4. Wenn eine Frist, Zuständigkeit oder Form unklar ist, zuerst diesen Engpass sichern.
5. Wenn der Nutzer nur ein Ergebnis braucht, keine Lehrbuchprüfung ausgeben; die Begründung bleibt knapp und belastbar.

## Mini-Gerüste

- Sofortvermerk: Nach derzeitigem Stand spricht mehr für [Ergebnis], weil [Norm] an [Tatbestandsmerkmal] anknüpft und [Beleg] diesen Punkt trägt. Offen bleibt [Lücke]. Nächster Schritt: [Handlung].
- Schriftsatzkern: Der Antrag ist begründet, weil [Tatsache] durch [Beweismittel] belegt ist und [Norm] daraus [Rechtsfolge] ableitet.
- Gegenposition: Die Gegenseite wird einwenden, dass [Argument]. Dagegen spricht [Beleg/Norm/Beweislast]. Prozessrisiko: [niedrig/mittel/hoch].
- Nachforderung: Bitte reichen Sie [Dokument] bis [Datum] ein; ohne diesen Beleg kann [Tatbestandsmerkmal] nicht tragfähig beurteilt werden.
- Entscheidungsvorschlag: Option A ist schneller, Option B ist belastbarer. Ich empfehle [Option], weil [entscheidender Grund].
"""

WERKSTATT_FINAL_CHECK_BLOCK = """## Schlusskontrolle für Tempo

- Erstes Ergebnis steht oben, nicht am Ende versteckt.
- Jede offene Tatsache ist als Nachforderung formuliert.
- Jede Rechtsfrage hat mindestens einen Normanker.
- Das nächste Dokument oder die nächste Handlung ist benannt.
- Der Ton passt zum Empfänger: Mandant, Gericht, Behörde, Gegner oder intern.
- Wenn zwei Wege vertretbar sind, steht die empfohlene Variante mit Grund vor der Alternative.
- Keine Nebenspur bleibt offen: erledigen, zurückstellen oder nachfordern.
"""

OLD_WERKSTATT_FINAL_CHECK_BLOCK = """## Schlusskontrolle für Tempo

- Erstes Ergebnis steht oben, nicht am Ende versteckt.
- Jede offene Tatsache ist als Nachforderung formuliert.
- Jede Rechtsfrage hat mindestens einen Normanker.
- Das nächste Dokument oder die nächste Handlung ist benannt.
- Der Ton passt zum Empfänger: Mandant, Gericht, Behörde, Gegner oder intern.
"""

DIREKTSTART_SENTENCE = (
    "Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen "
    "und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, "
    "Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur "
    "für Fristen, Belege, Beträge, Varianten oder Streitstoff."
)

STATION_PATTERN = re.compile(
    r"Eingang: Erfasse fuer diese Station alle Dokumente, Daten, Namen, Fristen, Betraege und Belege, "
    r"die den Punkt \d+ tragen\. Ordne jedes Dokument einer Tatsache und jeder Tatsache einem moeglichen "
    r"Tatbestandsmerkmal zu\.\n\n"
    r"Pruefung: Arbeite die einschlaegigen Tatbestandsmerkmale in der Reihenfolge Norm, Tatsache, Beleg, "
    r"Gegenargument, Rechtsfolge ab\. Vermeide abstrakte Belehrungen; jeder Satz muss den konkreten "
    r"Arbeitsgegenstand dieser Station voranbringen\.\n\n"
    r"Arbeitsprodukt: Liefere am Ende dieser Station einen ausformulierten Baustein fuer Memo, Schriftsatz, "
    r"Vertrag, Beschluss, Tabelle oder Entscheidungsvermerk\. Der Baustein benennt Ergebnis, Risiko und "
    r"Anschlussarbeit\."
)

FIELD_PATTERN = re.compile(
    r"Pruefe dieses Arbeitsfeld anhand der konkreten Unterlagen\. Lege fest, welcher Tatsachenkern, welche "
    r"Norm, welche Frist, welche Form und welches Beweismittel den Punkt tragen\.\n\n"
    r"Arbeitsprodukt: ein kurzer ausformulierter Ergebnisbaustein mit Risiko, Gegenargument und naechstem "
    r"Handlungsschritt\."
)


def plugin_dirs() -> list[Path]:
    return sorted(
        {p.parent.parent for p in REPO.glob("**/.claude-plugin/plugin.json") if ".git" not in p.parts}
    )


def prompt_files(suffix: str) -> list[Path]:
    out: list[Path] = []
    for directory in plugin_dirs():
        out.extend(sorted(directory.glob(f"*{suffix}")))
    return [p for p in out if p.is_file()]


def skill_files() -> list[Path]:
    out: list[Path] = []
    for directory in plugin_dirs():
        out.extend(sorted((directory / "skills").glob("*/SKILL.md")))
    return [p for p in out if p.is_file()]


def insert_before_first_h2(text: str, block: str) -> str:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if idx > 0 and line.startswith("## "):
            return "\n".join(lines[:idx]).rstrip() + "\n\n" + block.rstrip() + "\n\n" + "\n".join(lines[idx:]).lstrip() + "\n"
    return text.rstrip() + "\n\n" + block.rstrip() + "\n"


def refine_prompt(path: Path, kind: str) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    original = text

    if kind == "werkstatt":
        text = text.replace(OLD_WERKSTATT_BLOCK, WERKSTATT_BLOCK)
        if "## Arbeitsmodus: schnell und belastbar" not in text:
            text = insert_before_first_h2(text, WERKSTATT_BLOCK)
        text = STATION_PATTERN.sub(
            "Arbeite diese Station in einem Durchgang: Tatsachenkern und Belege erfassen, einschlägige Norm und Beweislast zuordnen, Gegenargument prüfen, Ergebnisbaustein mit Risiko und nächstem Schritt liefern.",
            text,
        )
        text = FIELD_PATTERN.sub(
            "Arbeitsfeld knapp prüfen: Tatsachenkern, Norm, Frist, Form, Beweis und Gegenargument. Output: Ergebnisbaustein mit Risiko und nächstem Schritt.",
            text,
        )
        if "## Ausgabeformate für schnelle Lieferung" not in text and len(text.encode("utf-8")) < 12 * 1024:
            text = text.replace(WERKSTATT_BLOCK, WERKSTATT_BLOCK.rstrip() + "\n\n" + WERKSTATT_ERGONOMY_BLOCK, 1)
        text = text.replace(OLD_WERKSTATT_FINAL_CHECK_BLOCK, WERKSTATT_FINAL_CHECK_BLOCK)
        if "## Schlusskontrolle für Tempo" not in text and len(text.encode("utf-8")) < 12 * 1024:
            text = text.rstrip() + "\n\n" + WERKSTATT_FINAL_CHECK_BLOCK
        if "## Schlusskontrolle für Tempo" in text and len(text.encode("utf-8")) < 12 * 1024 and "Keine Nebenspur bleibt offen" not in text:
            text = text.rstrip() + "\n- Keine Nebenspur bleibt offen: erledigen, zurückstellen oder nachfordern.\n"
    else:
        if "## Schnellmodus" not in text:
            text = insert_before_first_h2(text, SCHNELLSTART_BLOCK)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def refine_skill(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "## Direktstart: lesen, entscheiden, liefern" not in text:
        return False
    if DIREKTSTART_SENTENCE in text:
        return False

    marker = (
        "Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, "
        "Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. "
        "Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite "
        "unmittelbar in dessen Richtung weiter."
    )
    if marker in text:
        text = text.replace(marker, marker + "\n\n" + DIREKTSTART_SENTENCE, 1)
    else:
        text = text.replace(
            "## Direktstart: lesen, entscheiden, liefern",
            "## Direktstart: lesen, entscheiden, liefern\n\n" + DIREKTSTART_SENTENCE,
            1,
        )
    path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    changed_werkstatt = sum(refine_prompt(p, "werkstatt") for p in prompt_files("-werkstatt.md"))
    changed_schnellstart = sum(refine_prompt(p, "schnellstart") for p in prompt_files("-schnellstart.md"))
    changed_skills = sum(refine_skill(p) for p in skill_files())

    print(f"Werkstatt-Prompts geändert: {changed_werkstatt}")
    print(f"Schnellstart-Prompts geändert: {changed_schnellstart}")
    print(f"Skill-Direktstarts geändert: {changed_skills}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
