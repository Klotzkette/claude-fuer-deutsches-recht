#!/usr/bin/env python3
"""Strafft bestehende Prompts und Direktstarts ohne Spezialinhalte zu ersetzen."""

from __future__ import annotations

import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MAX_WERKSTATT_BYTES = 22 * 1024

WERKSTATT_BLOCK = """### 1.1. Arbeitsmodus: schnell und belastbar

Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, Frist, Engpass, stärkster Anker, nächster Output. Lies Material zuerst; frage nur nach, wenn Frist, Zuständigkeit, Beweis oder Rechtsfolge sonst kippt. Wenn der Zwischenstand trägt, gib ihn sofort aus und markiere die Vertiefung.

Arbeite danach in drei Ebenen: Prüfkern, Gegenargument, Arbeitsprodukt. Keine Vorrede, keine Materialinventur; jeder Abschnitt endet mit Satz, Tabelle, Antrag, Klausel oder Nachforderung.
"""

OLD_WERKSTATT_BLOCK = """## Arbeitsmodus: schnell und belastbar

Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, Frist, Engpass, stärkster Anker und nächster Output. Lies vorhandenes Material zuerst und frage danach höchstens drei Punkte nach, die für Frist, Zuständigkeit, Beweis oder Rechtsfolge entscheidend sind.

Arbeite in drei Ebenen: Sofortbild, Prüfkern, Arbeitsprodukt. Jeder Abschnitt beginnt mit der Ergebnisrichtung und endet mit einem verwertbaren Satz, einer Tabelle, einem Antrag, einer Klausel oder einer Nachforderung. Keine Vorrede, keine Materialinventur, keine abstrakte Vorlesung.
"""

SCHNELLSTART_BLOCK = """## 1. Schnellmodus

Starte mit dem Arbeitsprodukt. Gib zuerst Ergebnisrichtung, Frist, Risiko und nächsten Schritt. Bei umfangreichen Unterlagen zuerst eine belastbare Kurzfassung mit Fundstellenlinie liefern, danach vertiefen. Frage höchstens zwei Punkte nach, wenn der nächste Schritt sonst falsch würde. Tabellen nur für Fristen, Belege, Beträge oder Varianten.
"""

WERKSTATT_ERGONOMY_BLOCK = """### 1.2. Ausgabeformate für schnelle Lieferung

| Bedarf | Sofortausgabe | Qualitätsgriff |
| --- | --- | --- |
| Frist oder Eilsache | Fristenblatt mit nächstem Handlungstag | Fristbeginn, Fristende, Zuständigkeit und Zustellungsweg trennen |
| Schriftsatz oder Antrag | Antragssatz plus drei tragende Begründungsabsätze | Jede Tatsache bekommt Beleg oder Lückenmarke |
| Mandantenantwort | verständlicher Ergebnisbrief mit Optionen | Empfehlung, Risiko und Kostenfolge getrennt ausweisen |
| Interner Vermerk | Kurzlage, Rechtsanker, Entscheidungsvorschlag | offene Tatsachen nicht als Rechtsunsicherheit tarnen |
| Vertrag oder Klausel | Entwurfsfassung mit Kommentarrand | sichere Fassung, ausgewogene Fassung und Risikofassung unterscheiden |
| Gericht oder Behörde | Verfügung, Beschluss- oder Bescheidentwurf | Tenor, Gründe, Nebenentscheidungen und Zustellung mitdenken |

### 1.3. Rückfragenbremse

1. Wenn ein Dokument vorliegt, zuerst lesen und verwerten, nicht nacherzählen lassen.
2. Wenn Informationen fehlen, nur die Punkte fragen, die das nächste Arbeitsprodukt ändern.
3. Wenn mehrere Wege möglich sind, die zwei stärksten Varianten mit Entscheidungskriterium zeigen.
4. Wenn eine Frist, Zuständigkeit oder Form unklar ist, zuerst diesen Engpass sichern.
5. Wenn der Nutzer nur ein Ergebnis braucht, keine Lehrbuchprüfung ausgeben; die Begründung bleibt knapp und belastbar.

### 1.4. Mini-Gerüste

- Sofortvermerk: Nach derzeitigem Stand spricht mehr für [Ergebnis], weil [Norm] an [Tatbestandsmerkmal] anknüpft und [Beleg] diesen Punkt trägt. Offen bleibt [Lücke]. Nächster Schritt: [Handlung].
- Schriftsatzkern: Der Antrag ist begründet, weil [Tatsache] durch [Beweismittel] belegt ist und [Norm] daraus [Rechtsfolge] ableitet.
- Gegenposition: Die Gegenseite wird einwenden, dass [Argument]. Dagegen spricht [Beleg/Norm/Beweislast]. Prozessrisiko: [niedrig/mittel/hoch].
- Nachforderung: Bitte reichen Sie [Dokument] bis [Datum] ein; ohne diesen Beleg kann [Tatbestandsmerkmal] nicht tragfähig beurteilt werden.
- Entscheidungsvorschlag: Option A ist schneller, Option B ist belastbarer. Ich empfehle [Option], weil [entscheidender Grund].
"""

WERKSTATT_FINAL_CHECK_LINES = """- Erstes Ergebnis steht oben, nicht am Ende versteckt.
- Jede offene Tatsache ist als Nachforderung formuliert.
- Jede Rechtsfrage hat mindestens einen Normanker.
- Das nächste Dokument oder die nächste Handlung ist benannt.
- Der Ton passt zum Empfänger: Mandant, Gericht, Behörde, Gegner oder intern.
- Wenn zwei Wege vertretbar sind, steht die empfohlene Variante mit Grund vor der Alternative.
- Keine Nebenspur bleibt offen: erledigen, zurückstellen oder nachfordern.
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

TEMPO_LABELS = {
    "Arbeitsmodus: schnell und belastbar",
    "Ausgabeformate für schnelle Lieferung",
    "Rückfragenbremse",
    "Mini-Gerüste",
}


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


def normalize_werkstatt_headings(text: str) -> str:
    replacements = (
        (r"^#{2,3}[ \t]+(?:0\.|1\.1\.)?[ \t]*Arbeitsmodus: schnell und belastbar[ \t]*$", "### 1.1. Arbeitsmodus: schnell und belastbar"),
        (r"^#{2,3}[ \t]+(?:0\.1\.|1\.2\.)?[ \t]*Ausgabeformate für schnelle Lieferung[ \t]*$", "### 1.2. Ausgabeformate für schnelle Lieferung"),
        (r"^#{2,3}[ \t]+(?:0\.2\.|1\.3\.)?[ \t]*Rückfragenbremse[ \t]*$", "### 1.3. Rückfragenbremse"),
        (r"^#{2,3}[ \t]+(?:0\.3\.|1\.4\.)?[ \t]*Mini-Gerüste[ \t]*$", "### 1.4. Mini-Gerüste"),
    )
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
    for heading in (
        "### 1.1. Arbeitsmodus: schnell und belastbar",
        "### 1.2. Ausgabeformate für schnelle Lieferung",
        "### 1.3. Rückfragenbremse",
        "### 1.4. Mini-Gerüste",
    ):
        text = re.sub(rf"^({re.escape(heading)})\n(?!\n)", r"\1\n\n", text, flags=re.MULTILINE)
    return text


def heading_label(line: str) -> str | None:
    match = re.match(r"^#{1,6}[ \t]+(?:(?:\d+(?:\.\d+)*\.?)[ \t]+)?(.+?)[ \t]*$", line)
    if not match:
        return None
    return match.group(1)


def remove_werkstatt_tempo_block(text: str) -> tuple[str, bool]:
    lines = text.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if heading_label(line) == "Arbeitsmodus: schnell und belastbar":
            start = idx
            break
    if start is None:
        return text, False

    end = start + 1
    while end < len(lines):
        label = heading_label(lines[end])
        if lines[end].startswith("#") and label not in TEMPO_LABELS:
            break
        end += 1

    before = lines[:start]
    after = lines[end:]
    while before and not before[-1].strip():
        before.pop()
    while after and not after[0].strip():
        after.pop(0)
    rebuilt = before
    if before and after:
        rebuilt.append("")
    rebuilt.extend(after)
    return "\n".join(rebuilt).rstrip() + "\n", True


def werkstatt_tempo_block(first_subnumber: int) -> str:
    block = WERKSTATT_BLOCK.rstrip() + "\n\n" + WERKSTATT_ERGONOMY_BLOCK.rstrip()
    replacements = (
        (r"^### 1\.1\. Arbeitsmodus: schnell und belastbar$", f"### 1.{first_subnumber}. Arbeitsmodus: schnell und belastbar"),
        (r"^### 1\.2\. Ausgabeformate für schnelle Lieferung$", f"### 1.{first_subnumber + 1}. Ausgabeformate für schnelle Lieferung"),
        (r"^### 1\.3\. Rückfragenbremse$", f"### 1.{first_subnumber + 2}. Rückfragenbremse"),
        (r"^### 1\.4\. Mini-Gerüste$", f"### 1.{first_subnumber + 3}. Mini-Gerüste"),
    )
    for pattern, replacement in replacements:
        block = re.sub(pattern, replacement, block, flags=re.MULTILINE)
    return block


def werkstatt_mode_block(first_subnumber: int) -> str:
    return re.sub(
        r"^### 1\.1\. Arbeitsmodus: schnell und belastbar$",
        f"### 1.{first_subnumber}. Arbeitsmodus: schnell und belastbar",
        WERKSTATT_BLOCK.rstrip(),
        flags=re.MULTILINE,
    )


def insert_werkstatt_tempo_under_role(text: str) -> str:
    role_match = re.search(r"^## 1\. Rolle und Auftrag[ \t]*$", text, flags=re.MULTILINE)
    if not role_match:
        full = insert_before_first_h2(text, werkstatt_tempo_block(1))
        if len(full.encode("utf-8")) <= MAX_WERKSTATT_BYTES:
            return full
        return insert_before_first_h2(text, werkstatt_mode_block(1))

    next_h2 = re.search(r"^##[ \t]+", text[role_match.end():], flags=re.MULTILINE)
    insert_at = role_match.end() + next_h2.start() if next_h2 else len(text)
    role_section = text[role_match.start():insert_at]
    used = [int(match.group(1)) for match in re.finditer(r"^###[ \t]+1\.(\d+)\.", role_section, flags=re.MULTILINE)]
    first_subnumber = max(used, default=0) + 1
    full_block = werkstatt_tempo_block(first_subnumber)
    full = text[:insert_at].rstrip() + "\n\n" + full_block + "\n\n" + text[insert_at:].lstrip()
    if len(full.encode("utf-8")) <= MAX_WERKSTATT_BYTES:
        return full
    short_block = werkstatt_mode_block(first_subnumber)
    return text[:insert_at].rstrip() + "\n\n" + short_block + "\n\n" + text[insert_at:].lstrip()


def ensure_werkstatt_tempo_block(text: str) -> str:
    text, _ = remove_werkstatt_tempo_block(text)
    return insert_werkstatt_tempo_under_role(text)


def normalize_schnellstart_headings(text: str) -> str:
    replacements = (
        (r"^##[ \t]+(?:0\.|1\.)?[ \t]*Schnellmodus[ \t]*$", "## 1. Schnellmodus"),
        (r"^##[ \t]+(?:2\.)?[ \t]*Triage[ \t]*$", "## 2. Triage"),
        (r"^##[ \t]+(?:3\.)?[ \t]*Kurzweg[ \t]*$", "## 3. Kurzweg"),
        (r"^##[ \t]+(?:4\.)?[ \t]*Anker[ \t]*$", "## 4. Anker"),
        (r"^##[ \t]+(?:5\.)?[ \t]*Antwortform[ \t]*$", "## 5. Antwortform"),
        (r"^##[ \t]+(?:6\.)?[ \t]*Stop[ \t]*$", "## 6. Stop"),
    )
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
    for heading in (
        "## 1. Schnellmodus",
        "## 2. Triage",
        "## 3. Kurzweg",
        "## 4. Anker",
        "## 5. Antwortform",
        "## 6. Stop",
    ):
        text = re.sub(rf"^({re.escape(heading)})\n(?!\n)", r"\1\n\n", text, flags=re.MULTILINE)
    return text


def next_top_level_number(text: str) -> int:
    numbers = []
    for line in text.splitlines():
        match = re.match(r"##\s+(\d+)\.\s+", line)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def werkstatt_final_check_block(text: str) -> str:
    return f"## {next_top_level_number(text)}. Schlusskontrolle für Tempo\n\n{WERKSTATT_FINAL_CHECK_LINES.rstrip()}\n"


def normalize_werkstatt_final_check(text: str) -> str:
    heading = re.search(
        r"^##\s+(?:(?:\d+(?:\.\d+)*\.?)\s+)?Schlusskontrolle für Tempo\s*$",
        text,
        flags=re.MULTILINE,
    )
    if not heading:
        return text
    next_heading = re.search(r"^##\s+", text[heading.end():], flags=re.MULTILINE)
    section_end = heading.end() + next_heading.start() if next_heading else len(text)
    before = text[: heading.start()].rstrip()
    after = text[section_end:].lstrip("\n")
    rebuilt = before + "\n\n" + werkstatt_final_check_block(before).rstrip()
    if after:
        rebuilt += "\n\n" + after
    return rebuilt.rstrip() + "\n"


def refine_prompt(path: Path, kind: str) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    original = text

    if kind == "werkstatt":
        text = normalize_werkstatt_headings(text)
        text = text.replace(OLD_WERKSTATT_BLOCK, WERKSTATT_BLOCK)
        text = normalize_werkstatt_headings(text)
        text = ensure_werkstatt_tempo_block(text)
        text = STATION_PATTERN.sub(
            "Arbeite diese Station in einem Durchgang: Tatsachenkern und Belege erfassen, einschlägige Norm und Beweislast zuordnen, Gegenargument prüfen, Ergebnisbaustein mit Risiko und nächstem Schritt liefern.",
            text,
        )
        text = FIELD_PATTERN.sub(
            "Arbeitsfeld knapp prüfen: Tatsachenkern, Norm, Frist, Form, Beweis und Gegenargument. Output: Ergebnisbaustein mit Risiko und nächstem Schritt.",
            text,
        )
        if "Schlusskontrolle für Tempo" in text:
            text = normalize_werkstatt_final_check(text)
        elif len(text.encode("utf-8")) < 12 * 1024:
            text = text.rstrip() + "\n\n" + werkstatt_final_check_block(text)
    else:
        text = normalize_schnellstart_headings(text)
        if "Schnellmodus" not in text:
            text = insert_before_first_h2(text, SCHNELLSTART_BLOCK)
        text = normalize_schnellstart_headings(text)

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
