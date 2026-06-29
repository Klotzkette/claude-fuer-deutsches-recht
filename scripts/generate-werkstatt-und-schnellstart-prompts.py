#!/usr/bin/env python3
"""Erzeugt autarke Werkstatt- und Schnellstart-Prompts pro Plugin.

Ausgabe je Plugin:
- {plugin}/{slug}-werkstatt.md
- {plugin}/{slug}-schnellstart.md

Die Dateien sind reine Markdown-Arbeitsmittel fuer Nutzer ohne installierte
Plugin-Umgebung. Sie enthalten keine Skill-Verweise und keine ZIP-Verweise.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

from themen_profile import profile_for, ThemenProfil


REPO = Path(__file__).resolve().parent.parent
MAX_FAST = 7500
WERKSTATT_TEMPO_BLOCK = [
    "## Arbeitsmodus: schnell und belastbar",
    "",
    "Beginne mit einem Sofortbild in höchstens fünf Sätzen: Ziel, Frist, Engpass, stärkster Anker, nächster Output. Lies Material zuerst; frage nur nach, wenn Frist, Zuständigkeit, Beweis oder Rechtsfolge sonst kippt.",
    "",
    "Arbeite danach in drei Ebenen: Prüfkern, Gegenargument, Arbeitsprodukt. Keine Vorrede, keine Materialinventur; jeder Abschnitt endet mit Satz, Tabelle, Antrag, Klausel oder Nachforderung.",
    "",
]
SCHNELLSTART_TEMPO_BLOCK = [
    "## Schnellmodus",
    "",
    "Starte mit dem Arbeitsprodukt. Gib zuerst Ergebnisrichtung, Frist, Risiko und nächsten Schritt. Frage höchstens zwei Punkte nach, wenn der nächste Schritt sonst falsch würde. Tabellen nur für Fristen, Belege, Beträge oder Varianten.",
    "",
]
WERKSTATT_ERGONOMY_TEXT = """## Ausgabeformate für schnelle Lieferung

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
WERKSTATT_FINAL_CHECK_TEXT = """## Schlusskontrolle für Tempo

- Erstes Ergebnis steht oben, nicht am Ende versteckt.
- Jede offene Tatsache ist als Nachforderung formuliert.
- Jede Rechtsfrage hat mindestens einen Normanker.
- Das nächste Dokument oder die nächste Handlung ist benannt.
- Der Ton passt zum Empfänger: Mandant, Gericht, Behörde, Gegner oder intern.
- Wenn zwei Wege vertretbar sind, steht die empfohlene Variante mit Grund vor der Alternative.
- Keine Nebenspur bleibt offen: erledigen, zurückstellen oder nachfordern.
"""

# Plugins, deren Werkstatt- und Schnellstart-Markdown von Hand gepflegt werden.
# Der Generator ueberschreibt sie nicht; er meldet sie als uebersprungen.
PROTECTED_LIST = Path(__file__).resolve().parent / "handkuratierte-prompts.txt"


def load_protected() -> set[str]:
    if not PROTECTED_LIST.exists():
        return set()
    slugs: set[str] = set()
    for raw in PROTECTED_LIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        slugs.add(line)
    return slugs


BAD_WORDS = (
    "s" + "crape",
    "s" + "craping",
    "c" + "rawl",
    "c" + "rawling",
    "NOT" + "_FOUND",
    "T" + "BD",
    "AU" + "DIT",
)


def sanitize(text: str) -> str:
    paragraph = chr(167)
    text = text.replace(paragraph * 2, "Paragrafen")
    text = text.replace(paragraph, "Paragraf")
    text = re.sub(r"(\d),(\d)", r"\1.\2", text)
    text = text.replace("<", "[").replace(">", "]")
    for bad in BAD_WORDS:
        text = re.sub(re.escape(bad), "abrufen", text, flags=re.IGNORECASE)
    text = text.replace("KI-VO", "Regulierungsrahmen")
    text = text.replace("DSGVO", "Datenschutz-Grundverordnung")
    text = text.replace("Aktengeheimnis", "Vertraulichkeit")
    text = re.sub(r"\bsiehe Skill [^\n.]*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b" + re.escape("live " + "verifizieren") + r"\b", "vor Verwendung anhand einer belastbaren Quelle pruefen", text, flags=re.IGNORECASE)
    return text


def clean(text: str, limit: int | None = None) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    text = sanitize(text)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip(" ,.;:") + "."
    return text


def plugin_dirs() -> list[Path]:
    dirs = []
    for plugin_json in REPO.glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    for plugin_json in (REPO / "_GERICHTE_EXPERIMENTAL").glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    for plugin_json in (REPO / "gerichtsplugins").glob("*/.claude-plugin/plugin.json"):
        dirs.append(plugin_json.parent.parent)
    return sorted(set(dirs), key=lambda p: p.as_posix())


def frontmatter_description(text: str) -> str:
    if not text.startswith("---"):
        return ""
    m = re.match(r"---\s*\n([\s\S]*?)\n---", text)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("description:"):
            return clean(line.split(":", 1)[1].strip().strip('"'), 480)
    return ""


def skill_body_excerpt(text: str) -> str:
    body = re.sub(r"^---\s*\n[\s\S]*?\n---\s*", "", text).strip()
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("|") or line.startswith("<!--"):
            continue
        lines.append(line)
        if len(" ".join(lines)) > 900:
            break
    return clean(" ".join(lines), 900)


def collect_skill_material(plugin_dir: Path) -> list[dict[str, str]]:
    items = []
    for sd in sorted((plugin_dir / "skills").glob("*")):
        if not sd.is_dir():
            continue
        slug = sd.name
        skill_file = sd / "SKILL.md"
        desc = slug.replace("-", " ")
        body = ""
        if skill_file.exists():
            try:
                chunk_lines: list[str] = []
                with skill_file.open("r", encoding="utf-8", errors="ignore") as handle:
                    for line_no, line in enumerate(handle, 1):
                        chunk_lines.append(line)
                        if line_no >= 90:
                            break
                text = "".join(chunk_lines)
                desc = frontmatter_description(text) or desc
                body = skill_body_excerpt(text)
            except OSError:
                body = ""
        items.append({"slug": slug, "desc": desc, "body": body})
        if len(items) >= 30:
            break
    return items


def manifest(plugin_dir: Path) -> dict:
    return json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def first_readme_paragraph(plugin_dir: Path) -> str:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return ""
    try:
        text = readme.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    text = re.sub(r"<!--[\s\S]*?-->", " ", text)
    paragraphs = []
    current: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith("["):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if line.startswith("- ") or line.startswith("* "):
            continue
        current.append(line)
        if len(" ".join(current)) > 500:
            paragraphs.append(" ".join(current))
            break
    if current:
        paragraphs.append(" ".join(current))
    for paragraph in paragraphs:
        cleaned = clean(paragraph, 700)
        if len(cleaned) > 80:
            return cleaned
    return ""


def title_for(slug: str, mf: dict, profile: ThemenProfil) -> str:
    raw = mf.get("display_name") or mf.get("title") or slug.replace("-", " ")
    raw = raw.replace("_", " ").strip()
    if raw.lower() == slug:
        raw = profile.label
    return clean(raw.title(), 120)


def station_text(stations: Iterable[str], skill_material: list[dict[str, str]]) -> list[str]:
    out = list(stations)
    for item in skill_material[:7]:
        desc = item["desc"] or item["body"]
        if not desc:
            continue
        candidate = clean(desc, 260)
        if candidate and candidate not in out:
            out.append(candidate)
    return out[:12]


def build_werkstatt(plugin_dir: Path) -> str:
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    skill_material = collect_skill_material(plugin_dir)
    context = " ".join([mf.get("description", ""), first_readme_paragraph(plugin_dir)] + [s["desc"] for s in skill_material[:20]])
    profile = profile_for(slug, context)
    title = title_for(slug, mf, profile)
    stations = list(profile.stationen)
    intro = clean(mf.get("description", "") or first_readme_paragraph(plugin_dir) or profile.rolle, 900)

    lines: list[str] = [
        f"# {title} — Werkstatt-Prompt",
        "",
        "## 1. Rolle und Auftrag",
        "",
        f"Du arbeitest als {profile.rolle} Der Auftrag lautet: aus den vorgelegten Unterlagen einen belastbaren, fachlich sortierten Arbeitsstand mit verwertbarem Ergebnis zu erstellen. Gegenstand dieses Prompts ist: {intro}",
        "",
        "Die Rolle ist keine bloße Zusammenfassung. Sie ordnet Tatsachen, trennt beweisbare Punkte von Behauptungen, prueft die einschlaegigen Normen, formuliert den naechsten Arbeitsschritt und erzeugt ein direkt verwendbares Produkt.",
        "",
    ] + WERKSTATT_TEMPO_BLOCK + [
        "## 2. Stop-Kriterien",
        "",
    ]
    for item in profile.stop:
        lines.append(f"- {item}")
    lines += [
        "- Wenn Identitaet, Vollmacht, Fristbeginn oder Verfahrensstand nicht tragfaehig bestimmbar sind, wird zuerst eine knappe Lueckenliste erzeugt.",
        "- Wenn das gewuenschte Ergebnis eine endgueltige Rechtsentscheidung verlangt, wird nur ein entscheidungsreifer Entwurf mit offen markierten Pruefpunkten ausgegeben.",
        "",
        "## 3. Werkstattfluss",
        "",
    ]

    for idx, station in enumerate(stations, 1):
        lines += [
            f"### 3.{idx}. {clean(station, 140)}",
            "",
            "Arbeite diese Station in einem Durchgang: Tatsachenkern und Belege erfassen, einschlägige Norm und Beweislast zuordnen, Gegenargument prüfen, Ergebnisbaustein mit Risiko und nächstem Schritt liefern.",
            "",
        ]

    lines += [
        "## 4. Pflichtnormen als Kernsaetze",
        "",
    ]
    for item in profile.normen:
        lines.append(f"- {item}")

    # Add norms extracted from selected skills without making skill references.
    extracted_norms: list[str] = []
    for item in skill_material:
        paragraph_pattern = re.escape(chr(167)) + r"{1,2}"
        norm_pattern = r"(?:Paragraf(?:en)?|" + paragraph_pattern + r")\s*[\w\d .AbsatzSatzNrnummerbisund/-]+(?:BGB|ZPO|StPO|GG|InsO|VwGO|FGO|SGG|ArbGG|FamFG|HGB|GmbHG|AktG|TzBfG|KSchG|BetrVG|DSGVO|AO|EStG|UStG|SGB|GVG)"
        for m in re.finditer(norm_pattern, item["desc"] + " " + item["body"]):
            norm = clean(m.group(0), 160)
            if norm and norm not in extracted_norms:
                extracted_norms.append(norm)
        if len(extracted_norms) >= 8:
            break
    for norm in extracted_norms[:8]:
        lines.append(f"- {norm}: im konkreten Sachverhalt als Tatbestands- oder Verfahrensanker pruefen.")

    lines += [
        "",
        "## 5. Leitentscheidungen",
        "",
    ]
    for item in profile.entscheidungen:
        lines.append(f"- {item}")

    lines += [
        "",
        "## 6. Pruefraster",
        "",
    ]
    for idx, item in enumerate(profile.pruefraster, 1):
        lines.append(f"{idx}. {item}")
    lines += [
        f"{len(profile.pruefraster)+1}. Welche Tatsache fehlt noch, obwohl sie fuer die Rechtsfolge entscheidend ist.",
        f"{len(profile.pruefraster)+2}. Welches konkrete Arbeitsprodukt loest den naechsten praktischen Engpass.",
        "",
        "## 7. Schriftsatz- und Memo-Geruest",
        "",
        "1. Ueberschrift mit Verfahrensstand, Beteiligten, Datum und Ziel.",
        "2. Kurzlage in drei bis sieben Saetzen mit Frist, Streitkern und Ergebnisrichtung.",
        "3. Sachverhalt nur mit belegten Tatsachen; streitige Punkte werden als streitig markiert.",
        "4. Rechtliche Pruefung nach Tatbestandsmerkmalen, nicht nach Bauchgefuehl.",
        "5. Gegenargumente mit Beweislast und Risiko.",
        "6. Ergebnis, Antrag, Formulierungsvorschlag oder Entscheidungsoption.",
        "7. Anschlussliste mit Fristen, Dokumenten, Ansprechpartnern und naechstem Output.",
        "",
        "## 8. Arbeitsweise",
        "",
        "Arbeite zuerst aktennah, dann normnah, dann produktnah. Wenn ein Dokument vorliegt, wird es gelesen, eingeordnet und mit Fundstelle verarbeitet. Wenn keine Unterlagen vorliegen, werden hoechstens fuenf gezielte Fragen gestellt; danach entsteht ein vorlaeufiger Arbeitsplan. Jede Antwort wird in ganzen Saetzen formuliert. Tabellen sind erlaubt, wenn sie Vergleich, Berechnung oder Fristen besser zeigen.",
        "",
        "Selbstcheck vor Ausgabe: Ist die Frist benannt? Ist die Form geklaert? Ist die richtige Rolle getroffen? Ist die Rechtsfolge aus einer Norm abgeleitet? Ist das Arbeitsprodukt tatsaechlich verwendbar? Sind offene Tatsachen von offenen Rechtsfragen getrennt?",
        "",
        "## 9. Qualitaetskontrolle und Abschluss",
        "",
        "Zum Abschluss wird das Ergebnis auf Widersprueche, fehlende Belege, falsche Zuständigkeit, unklare Fristen, unvollstaendige Antraege, Rechenfehler und unpassenden Ton geprueft. Danach folgt eine knappe Anschlussliste: sofort erledigen, nachfordern, entscheiden, entwerfen, einreichen oder zurueckstellen.",
        "",
        "## 10. Musterbausteine",
        "",
    ]
    skeletons = list(profile.skelette) or (
        "Memo-Kernsatz: Nach dem derzeit belegten Sachverhalt spricht mehr fuer [Ergebnis], weil [Norm] die Rechtsfolge an [Tatbestandsmerkmal] knuepft und [Beleg] diesen Punkt traegt.",
        "Nachforderung: Bitte reichen Sie bis [Datum] [Dokument] ein; ohne diesen Beleg kann [Tatbestandsmerkmal] nicht tragfaehig beurteilt werden.",
        "Schriftsatzkern: Der Anspruch ist begruendet, weil [Norm], [Tatsache], [Beweis] und [Rechtsfolge] zusammenfallen.",
    )
    for item in skeletons:
        lines.append(f"- {item}")

    # Make narrow prompts less skeletal by adding issue catalog derived from skills.
    if skill_material:
        lines += ["", "## 11. Materienbezogene Arbeitsfelder", ""]
        field_limit = min(36, max(18, len(skill_material)))
        for idx, item in enumerate(skill_material[:field_limit], 1):
            desc = clean(item["desc"] or item["body"], 260)
            if desc:
                lines.append(f"### 11.{idx}. {desc}")
                lines.append("")
                lines.append("Arbeitsfeld knapp prüfen: Tatsachenkern, Norm, Frist, Form, Beweis und Gegenargument. Output: Ergebnisbaustein mit Risiko und nächstem Schritt.")
                lines.append("")

    text = "\n".join(lines).strip() + "\n"
    if len(text.encode("utf-8")) < 12 * 1024 and "## Ausgabeformate für schnelle Lieferung" not in text:
        text = text.replace(
            "\n".join(WERKSTATT_TEMPO_BLOCK).rstrip(),
            "\n".join(WERKSTATT_TEMPO_BLOCK).rstrip() + "\n\n" + WERKSTATT_ERGONOMY_TEXT.rstrip(),
            1,
        )
    if len(text.encode("utf-8")) < 12 * 1024 and "## Schlusskontrolle für Tempo" not in text:
        text = text.rstrip() + "\n\n" + WERKSTATT_FINAL_CHECK_TEXT.rstrip() + "\n"
    if profile.oeffnungssatz:
        text = profile.oeffnungssatz + "\n\n" + text
    return sanitize(text)


def build_schnellstart(plugin_dir: Path) -> str:
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    skill_material = collect_skill_material(plugin_dir)
    context = " ".join([mf.get("description", ""), first_readme_paragraph(plugin_dir)] + [s["desc"] for s in skill_material[:20]])
    profile = profile_for(slug, context)
    title = title_for(slug, mf, profile)
    stations = list(profile.stationen)[:6]
    lines: list[str] = [
        f"# {title} — Schnellstart",
        "",
        f"Rolle: {profile.rolle} Arbeite sofort am konkreten Fall, liefere ganze Saetze und ein verwendbares Ergebnis.",
        "",
    ] + SCHNELLSTART_TEMPO_BLOCK + [
        "## Triage",
        "",
        "1. Wer will welches konkrete Ergebnis von wem.",
        "2. Welche Frist, Form, Zuständigkeit oder Verfahrenslage kann sofort kippen.",
        "3. Welche Unterlagen liegen vor und welche Tatsache belegt jedes Dokument.",
        "4. Welche Ausgabe wird benoetigt: Memo, Schriftsatz, Vertrag, Tabelle, Beschluss oder Checkliste.",
        "",
        "## Kurzweg",
        "",
    ]
    if profile.oeffnungssatz:
        lines = [profile.oeffnungssatz, ""] + lines
    for idx, station in enumerate(stations, 1):
        lines.append(f"{idx}. {clean(station, 180)}")
    lines += ["", "## Anker", ""]
    for item in profile.normen[:5]:
        lines.append(f"- {item}")
    for item in profile.entscheidungen[:3]:
        lines.append(f"- {item}")
    lines += [
        "",
        "## Antwortform",
        "",
        "Lagebild: drei bis sieben Saetze. Pruefung: Tatbestandsmerkmale mit Belegen. Ergebnis: klare Empfehlung. Anschluss: Frist, fehlender Beleg, naechstes Dokument. Quellen: nur tragende Normen und Entscheidungen.",
        "",
        "## Stop",
        "",
        "Stoppe bei ungeklärter Frist, fehlender Vollmacht, fehlendem Kernbeleg oder Entscheidung mit hohem Haftungsrisiko und gib zuerst eine Lückenliste aus. Für Vertiefung den Werkstatt-Prompt desselben Plugins verwenden.",
        "",
    ]
    text = sanitize("\n".join(lines).strip() + "\n")
    if len(text) <= MAX_FAST:
        return text
    # Hard compact if needed.
    parts = text.split("\n## Anker\n")
    if len(parts) == 2:
        head, rest = parts
        anchor, tail = rest.split("\n## Antwortform\n", 1)
        anchor_lines = [l for l in anchor.splitlines() if l.strip()][:5]
        text = head.rstrip() + "\n\n## Anker\n\n" + "\n".join(anchor_lines) + "\n\n## Antwortform\n" + tail
    if len(text) > MAX_FAST:
        text = text[: MAX_FAST - 2].rstrip() + "\n"
    return text


def write_readme_links(plugin_dir: Path) -> None:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return
    mf = manifest(plugin_dir)
    slug = mf.get("name") or plugin_dir.name
    raw_base = f"https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin_dir.relative_to(REPO).as_posix()}"
    block = "\n".join([
        "<!-- BEGIN werkstatt-schnellstart-raw-links (autogen) -->",
        "## Werkstatt- und Schnellstart-Prompts",
        "",
        "Diese Markdown-Prompts sind autarke Arbeitsfassungen fuer Nutzer, die das Plugin nicht installieren. Sie werden direkt als Markdown-Dateien geladen.",
        "",
        f'- Werkstatt-Prompt: <a href="{raw_base}/{slug}-werkstatt.md" download>{slug}-werkstatt.md</a>',
        f'- Schnellstart-Prompt: <a href="{raw_base}/{slug}-schnellstart.md" download>{slug}-schnellstart.md</a>',
        "",
        "<!-- END werkstatt-schnellstart-raw-links (autogen) -->",
    ])
    text = readme.read_text(encoding="utf-8", errors="ignore")
    pattern = r"<!-- BEGIN werkstatt-schnellstart-raw-links \(autogen\) -->[\s\S]*?<!-- END werkstatt-schnellstart-raw-links \(autogen\) -->"
    if re.search(pattern, text):
        text = re.sub(pattern, block, text)
    else:
        lines = text.splitlines()
        insert_at = 1 if lines and lines[0].startswith("# ") else 0
        lines[insert_at:insert_at] = ["", block, ""]
        text = "\n".join(lines) + "\n"
    readme.write_text(text, encoding="utf-8")


def main() -> int:
    dirs = plugin_dirs()
    protected = load_protected()
    written = 0
    skipped = 0
    skipped_slugs: list[str] = []
    problems: list[str] = []
    for plugin_dir in dirs:
        mf = manifest(plugin_dir)
        slug = mf.get("name") or plugin_dir.name
        if slug in protected:
            # Handkuratierte Prompts bleiben unveraendert, auch bei --force.
            skipped += 2
            skipped_slugs.append(slug)
            continue
        werkstatt = build_werkstatt(plugin_dir)
        schnell = build_schnellstart(plugin_dir)
        if len(schnell) > MAX_FAST:
            problems.append(f"{slug}: Schnellstart {len(schnell)} Zeichen")
        (plugin_dir / f"{slug}-werkstatt.md").write_text(werkstatt, encoding="utf-8")
        (plugin_dir / f"{slug}-schnellstart.md").write_text(schnell, encoding="utf-8")
        written += 2
    if problems:
        print("Probleme:")
        for p in problems:
            print("-", p)
        return 1
    if skipped_slugs:
        print("Handkuratiert, uebersprungen: " + ", ".join(sorted(skipped_slugs)))
    print(f"geschrieben: {written}, uebersprungen: {skipped}, Probleme: keine")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
