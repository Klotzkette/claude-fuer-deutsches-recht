#!/usr/bin/env python3
"""Erzeugt pro Plugin einen kompakten Unified Mini Prompt.

Ziel:
- eine einzelne Markdown-Datei pro Plugin,
- maximal 7.500 Zeichen inkl. Leerzeichen,
- direkt als Release-Asset herunterladbar,
- nutzbar in ChatGPT, Claude, Gemini, Mistral, Le Chat usw.,
- keine installierbare Plugin-Datei und kein Ersatz für die vollständigen
  Skills.

Ausgabe:
    unified-mini-prompts/<plugin>.md
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from public_release import RELEASE_BASE, compact_mini

from skill_routing_priorities import MINI_SKILL_SUMMARIES, PLUGIN_PRIORITY_SKILLS, PLUGIN_TRIGGER_ROUTES


REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "unified-mini-prompts"
MAX_CHARS = 7500
SOFT_MAX = 7350


PRIORITY_RE = re.compile(
    r"(einstieg|kaltstart|triage|routing|workflow|mandat|erstpruefung|erstprüfung|"
    r"checkliste|fristen|quality|red-team|risiko|strategie|startbildschirm|dashboard|padlet|canvas|applet|"
    r"belegmatrix|wertungsmatrix|zuschlagsmatrix|zuschlagskriter|wertungsschema|formatexport|akte|akten|"
    r"bietergemeinschaft|ausschluss|ausschlussgrund|steuerschuld|steuer|sozialabgabe|selbstreinigung|"
    r"schwellen|wertgrenz|reform|direktauftrag|bund-laender|bundesland|laender|"
    r"gaeb|datenformat|leistungsverzeichnis|preisblatt|angebot|bekanntmachung|"
    r"legacy|sap|erp|crm|ava|dms|sharepoint|sftp|api|odata|idoc|bapi|csv|json|hash|mcp|"
    r"wirklichkeitsdaten|zustandsdaten|bestandsdaten|bauwerksregister|pms|bms|bim|nachtrag|bauzeit|klima|umwelt|genehmigung|szenario|buendel|bündel|skaleneffekt|portfolio|"
    r"tragfaehigkeit|tragfähigkeit|mobilitaet|mobilität|korridor|direktbeauftragung|beschleunigung|oep|öpp|capex|fertigteil|serienloesung|serienlösung|"
    r"wirtschaftlich|preisqualitaet|preisqualität|preis-leistung|lebenszyklus|bestwertung|bestangebot|preisautomatismus|"
    r"qualitaet|qualität|konzeptwertung|servicelevel|lieferzeit|ausfuehrungszeit|ausführungszeit|nebenangebot|"
    r"qualitaetsvorsprung|qualitätsvorsprung|billigzuschlag|billigangebot|"
    r"dyka|sof medica|instituto cervantes|produktneutral|technische|spezifikation|gleichwertig|material|schnittstelle|"
    r"gener[aá]ln[ií]|exklusiv|alleinanbieter|direktvergabe|lock-in|"
    r"kolin|qingdao|drittstaat|mara|lianakis|dimarso|"
    r"fastweb|pfe|randstad|polismyndigheten|fastned|pressetext|advania|"
    r"insolvenz|auftragnehmerwechsel|sanierung|restrukturierung|132|"
    r"ruege|rüge|nachpruef|nachprüf|vergabekammer|vergabesenat|olg|beschwerde|"
    r"zuschlagssperre|akteneinsicht|beiladung|vergleich|streit|konkurrent|wettbewerber|unterlegen|"
    r"berichtigung|upload|schnittstelle|eforms|ted|dval|portal)",
    re.IGNORECASE,
)

PINNED_SKILLS = PLUGIN_PRIORITY_SKILLS


def sanitize_import_language(text: str) -> str:
    """Verhindert, dass verwertetes Altmaterial als drittes Plugin erscheint."""
    legacy_role = "Fach" + "anwalt"
    legacy_branch = "Fach" + "anwaltschaft"
    legacy_slug = "fach" + "anwalt-vergaberecht"
    replacements = [
        (rf"`{legacy_slug}`", "`vergaberecht-werkstatt`"),
        (rf"Plugin\s+{legacy_role}\s+für\s+Vergaberecht", "Vergaberecht-Werkstatt"),
        (rf"Plugin\s+{legacy_role}\s+Vergaberecht", "Vergaberecht-Werkstatt"),
        (rf"{legacy_role}\s+für\s+Vergaberecht", "Vergaberecht"),
        (rf"{legacy_role}\s+Vergaberecht", "Vergaberecht"),
        (rf"{legacy_role}srecht\s+Vergaberecht", "Vergaberecht"),
        (rf"{legacy_branch}\s+Vergaberecht", "Vergaberecht"),
        (legacy_branch, "anwaltliche Vertiefung"),
        (rf"{legacy_slug}-Plugin", "Vergaberecht-Werkstatt"),
        (rf"Plugin\s+{legacy_slug}", "Vergaberecht-Werkstatt"),
        (r"mandantenpadlet-vergabe-canvas", "bieter-dashboard-canvas"),
        (r"Mandantenpadlet Vergabe", "Vergabe-Dashboard"),
        (r"Mandantenpadlet", "Vergabe-Dashboard"),
        (legacy_slug, "vergaberecht-werkstatt"),
        (rf"{legacy_role}:\s*", ""),
        (r"Bau-/Architektenrecht-Schnittstelle", "Bau-/Architektenrecht-Schnittstelle"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def strip_markdown_link(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_display_text(text: str) -> str:
    text = text.replace("—", "-").replace("–", "-")
    text = text.replace("“", '"').replace("”", '"').replace("„", '"')
    text = text.replace("‘", "'").replace("’", "'")
    norm_suffix = r"(?:\s+Abs\.\s*[0-9]+)?(?:\s+Satz\s*[0-9]+)?(?:\s+S\.\s*[0-9]+)?(?:\s+Nr\.\s*[0-9]+)?(?:\s+Buchstabe\s+[a-z])?"
    text = re.sub(r"\b(?:Paragrafen|Paragraphen)\s+([0-9]+(?:\s*(?:-|bis|und)\s*[0-9]+)?(?:\s*ff\.?)?)", r"§§ \1", text)
    text = re.sub(rf"\b(?:Paragraf|Paragraph)\s+([0-9]+[a-zA-Z]?{norm_suffix})", r"§ \1", text)
    text = re.sub(r"\bParagraf-(?=[0-9])", "§-", text)
    return text


def shorten_text(text: str, max_len: int) -> str:
    """Kuerzt Anzeigetext ohne Ellipsen und moeglichst an Satz- oder Wortgrenzen."""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    window = text[:max_len].strip()
    min_len = min(80, max_len * 2 // 3)
    sentence_breaks = [m.end() for m in re.finditer(r"[.!?](?:\s|$)", window)]
    usable_breaks = [pos for pos in sentence_breaks if pos >= min_len]
    if usable_breaks:
        return window[: usable_breaks[-1]].strip()
    cut = window.rsplit(" ", 1)[0].strip().rstrip(" ,.;:-")
    dangling = {
        "und", "oder", "sowie", "mit", "ohne", "für", "fuer", "bei", "nach",
        "vor", "von", "im", "in", "am", "an", "als", "der", "die", "das",
        "den", "dem", "des", "ein", "eine", "einem", "eines", "bzw", "bzw.",
        "fokus", "output", "norm", "normen", "frist", "fristen", "konkret",
        "rote", "roten", "offene", "offenen", "einschlaegige", "einschlaegigen",
        "insbesondere", "import", "export", "upload", "rechts", "vergaberechtliche", "§", "§§",
    }
    while cut.split():
        last = cut.split()[-1].strip(" ,.;:()[]").lower()
        if last in dangling:
            cut = " ".join(cut.split()[:-1]).rstrip(" ,.;:-")
            continue
        break
    if cut and cut[-1] not in ".!?":
        cut += "."
    return cut


def clean(text: str, max_len: int | None = None) -> str:
    text = sanitize_import_language(text)
    text = strip_markdown_link(text)
    text = normalize_display_text(text)
    text = re.sub(r"\b[Nn]utze diesen Skill\b", "Einsetzen", text)
    text = re.sub(r"\b[Nn]utze den Skill\b", "Einsetzen", text)
    text = text.replace("|", "/")
    text = re.sub(r"\s+", " ", text).strip()
    if max_len and len(text) > max_len:
        return shorten_text(text, max_len)
    return text


def humanize_slug(slug: str) -> str:
    legacy_slug = "fach" + "anwalt-vergaberecht"
    legacy_branch = "fach" + "anwaltschaft"
    slug = re.sub(rf"^{legacy_slug}-", "", slug)
    slug = slug.replace("mandantenpadlet-vergabe-canvas", "bieter-dashboard-canvas")
    slug = slug.replace(legacy_branch, "anwaltliche-vertiefung")
    words = [w for w in re.split(r"[-_]+", slug) if w]
    lowercase_words = {"und", "in", "im", "mit", "auf", "von", "fuer", "nach", "der", "die", "das"}
    parts = []
    for word in words:
        if word in lowercase_words:
            parts.append(word)
        elif len(word) > 3:
            parts.append(word.capitalize())
        else:
            parts.append(word.upper())
    title = " ".join(parts)
    replacements = {
        "Ruege": "Rüge",
        "Ruegeschriftsatz": "Rügeschriftsatz",
        "Nachpruefungsantrag": "Nachprüfungsantrag",
        "Nachpruefungsverfahren": "Nachprüfungsverfahren",
        "Nachpruefung": "Nachprüfung",
        "Schwaerzung": "Schwärzung",
        "Produktneutralitaet": "Produktneutralität",
        "Dokumentationsluecken": "Dokumentationslücken",
        "Angebotsoeffnung": "Angebotsöffnung",
        "Preisqualitaet": "Preisqualität",
        "Qualitaet": "Qualität",
        "Qualitaetsvorsprung": "Qualitätsvorsprung",
        "Ungewoehnlich": "Ungewöhnlich",
        "Eignungspruefung": "Eignungsprüfung",
        "Praequalifikation": "Präqualifikation",
        "Erklaerung": "Erklärung",
        "Erklaerungen": "Erklärungen",
        "Ausschlussgruende": "Ausschlussgründe",
        "Pruefung": "Prüfung",
        "Pruef": "Prüf",
        "Behoerden": "Behörden",
        "Oeffentlich": "Öffentlich",
        "Fuer": "für",
        "Waehlen": "wählen",
        "Eforms": "eForms",
        "Ted": "TED",
        "Dval": "DVAL",
        "Eu": "EU",
        "Gaeb": "GAEB",
        "Xml": "XML",
        "Pdf": "PDF",
        "Zip": "ZIP",
        "LV": "LV",
    }
    for old, new in replacements.items():
        title = re.sub(rf"\b{old}\b", new, title)
    return title


def frontmatter_description(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return ""
    m = re.match(r"---\s*\n([\s\S]*?)\n---", text)
    if not m:
        return ""
    fm = m.group(1)
    line = next((line for line in fm.splitlines() if line.startswith("description:")), "")
    if not line:
        return ""
    desc = line.split(":", 1)[1].strip()
    if len(desc) >= 2 and desc[0] == desc[-1] and desc[0] in {'"', "'"}:
        desc = desc[1:-1]
    return clean(desc, 260)


def collect_skills(plugin_dir: Path) -> list[dict[str, str | int]]:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []
    items = []
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        slug = skill_md.parent.name
        desc = frontmatter_description(skill_md)
        score = 0
        if PRIORITY_RE.search(slug):
            score += 1000
        if PRIORITY_RE.search(desc):
            score += 500
        score += min(len(desc), 400)
        items.append({"slug": slug, "title": humanize_slug(slug), "desc": desc, "score": score})
    pinned = PINNED_SKILLS.get(plugin_dir.name, [])
    pin_index = {slug: idx for idx, slug in enumerate(pinned)}

    def keyfn(item: dict[str, str | int]) -> tuple[int, int, str]:
        slug = str(item["slug"])
        return (pin_index.get(slug, 999), -int(item["score"]), slug)

    return sorted(items, key=keyfn)


def marketplace() -> dict:
    return json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))


ROLE_LABELS = {
    "vergabestelle-behoerden": "Vergabestellen",
    "bieter-unternehmen": "Bieter und Bewerber",
    "konkurrenten-rechtsschutz": "Konkurrentenrechtsschutz",
}

ROLE_STARTERS = {
    "vergabestelle-behoerden": (
        "Neuer Vergabestellenfall. Prüfe die beigefügten Unterlagen vollständig, "
        "sichere Fristen und Rechtsregime und erstelle den nächsten "
        "entscheidungsreifen Behördenoutput."
    ),
    "bieter-unternehmen": (
        "Neue Bewerbung. Prüfe die beigefügten Vergabeunterlagen vollständig, "
        "sichere Abgabefrist und Ausschlussrisiken und erstelle den nächsten "
        "abgabefertigen Angebotsoutput."
    ),
    "konkurrenten-rechtsschutz": (
        "Neuer Konkurrentenfall. Prüfe die beigefügten Unterlagen vollständig, "
        "sichere sofort Rüge- und Zuschlagsfristen und erstelle den stärksten "
        "fristgerechten Rechtsbehelf."
    ),
}

ROLE_FIRST_VIEW = {
    "vergabestelle-behoerden": "Akte",
    "bieter-unternehmen": "Angebot",
    "konkurrenten-rechtsschutz": "Angriff",
}


def role_label(name: str) -> str:
    return ROLE_LABELS.get(name, name.replace("-", " "))


ROLE_NOTES = {
    "vergabestelle-behoerden": "Arbeitskern: Bedarf, LV, Kriterien, Wertung, Bekanntmachung und Streitakte auf das wirtschaftlichste Angebot nach § 127 GWB ausrichten. Rechtsprechung steuert Entscheidungen, keine Zitatblöcke.",
    "bieter-unternehmen": "Arbeitskern: Angebot, Belege, Bieterfragen, Rüge und VK-Antrag so bauen, dass Qualitätsvorsprung, Formatfehler, Ausschluss, Unterpreis und Zuschlagschance konkret nachweisbar werden. Rechtsprechung steuert Antrag und Beleg.",
    "konkurrenten-rechtsschutz": "Arbeitskern: Angriff als fristgebundene Rechtsverletzung mit Aktenbeleg, Kausalität, Zuschlagschance und Antrag führen. Rechtsprechung steuert Angriff und Akteneinsicht.",
}


ROLE_FALLCARD_LINES = {
    "vergabestelle-behoerden": [
        "## Fallkarte",
        "",
        "Vor Langtext: Falltyp, Norm, Tatbestand, Beweislast, Quellenstatus und Output.",
        "",
        "| Feld | Vergabestellenkern |",
        "|---|---|",
        "| Falltyp | Bestwertung, LV/Format, Direktvergabe, Billigangebot, VK/OLG, Unterschwelle |",
        "| Norm | § 127 GWB, §§ 14, 31, 60 VgV, §§ 160 ff. GWB; BVerfG 1 BvR 1160/03 |",
        "| Tatbestand | Qualität/Tempo, Gleichwertigkeit, Lock-in, Preisabstand, Rüge/Frist |",
        "| Beweislast | Aktenbeleg, Marktsuche, Wertungsmatrix, Aufklärungs-/Schwärzungsvermerk |",
        "| Rechtsfolge/Output | Matrix, Berichtigung, Aufklärung, Abhilfe/Nichtabhilfe oder VK-Stellungnahme |",
    ],
    "bieter-unternehmen": [
        "## Fallkarte",
        "",
        "Fallkarte vor Langtext: Falltyp, Norm, Tatbestand, Darlegung, Quellenstatus, Rechtsfolge, Output.",
        "",
        "| Feld | Bieterkern |",
        "|---|---|",
        "| Falltyp | Qualitätsvorsprung, sperrendes LV/Format, Billigkonkurrent, Ausschluss/BG, VK/OLG |",
        "| Norm | § 127, § 31, § 60, §§ 123-125, §§ 160 ff. GWB/VgV; BVerfG 1 BvR 1160/03 für Unterschwelle |",
        "| Tatbestand | Mehrwert, Gleichwertigkeit, Preisabstand, Nachweis-/Steuermangel, Zuschlagschance |",
        "| Darlegung | Bieter braucht Fundstelle, eigenen Beleg, Schaden, Abhilfeantrag, Geheimnisschutz |",
        "| Rechtsfolge/Output | Punktebrücke, Bieterfrage, Rüge, VK-Antrag, Akteneinsicht, Vergleichsfenster |",
    ],
    "konkurrenten-rechtsschutz": [
        "## Fallkarte",
        "",
        "Fallkarte vor Langtext: Falltyp, Norm, Tatbestand, Beweislast, Quellenstatus, Rechtsfolge, Output.",
        "",
        "| Feld | Konkurrentenkern |",
        "|---|---|",
        "| Falltyp | Billigzuschlag, Produktbindung, Direktauftrag, ungeeigneter Konkurrent, Schwärzung, Unterschwelle |",
        "| Norm | § 127, § 31, § 60, §§ 123-125, §§ 135, 160, 165, 169 GWB; BVerfG 1 BvR 1160/03 |",
        "| Tatbestand | Preisautomatismus, Sperre, Lock-in, Register-/Referenzmangel, entscheidende Aktenstelle |",
        "| Beweislast | Konkurrent braucht Frist, Aktenfundstelle, Kausalität, Zuschlagschance, konkreten Antrag |",
        "| Rechtsfolge/Output | Rüge, VK-Antrag, Eilantrag, Akteneinsicht, neue Wertung, Ausschlussantrag |",
    ],
}


ROLE_WORKFLOW_LINES = {
    "vergabestelle-behoerden": [
        "## Sofortworkflow",
        "",
        "Fünf Takte: Intake, Regime, Fachpfad, Arbeitsprodukt, Kontrolle.",
        "1. Intake: Akte, Systeme, Feldautorität, Schlüssel, Stand/Einheit, Portal, Fristen und Freigaben erfassen.",
        "2. Regime: Auftraggeber, Auftragsart, Wert/Lose, Schwelle, Landesrecht, Verfahren und Rechtsweg.",
        "3. Fachpfad: Bestangebot, Bekanntmachung, LV, Wertung, Ausschluss, Rüge/VK oder Upload.",
        "4. Output: Vermerk, Matrix, eForms-/DVAL-Liste, LV-/Formatpaket, Rügeerwiderung oder VK-Stellungnahme.",
        "5. Kontrolle: Tatsache, Annahme, Norm, Entscheidung, Beleg, Gegenargument, Freigabe und Rückkanal.",
        "",
        "## Output-Weiche",
        "",
        "| Lage | Sofort liefern |",
        "|---|---|",
        "| vor Veröffentlichung | Bestwertungsplan, Zuschlagsmatrix, LV-/Formatcheck, Bekanntmachungs-Feldliste |",
        "| Einwand berechtigt | Berichtigungsentscheidung, Fristverlängerung, Uploadauftrag, Aktenvermerk |",
        "| Rüge oder VK | Fristenampel, Verteidigungslinien, Akteneinsichts-/Schwärzungsliste, Antragserwiderung |",
        "| Legacy-/Wirklichkeitsdaten | Feldautorität, Entscheidungsbrücke, Mapping/Hash/Delta, Freigabe und Rückkanal |",
    ],
    "bieter-unternehmen": [
        "## Sofortworkflow",
        "",
        "Arbeite immer in fünf Takten: Intake, Angebotsroute, Belegroute, Output, Freigabe.",
        "1. Intake: Bekanntmachung, Unterlagen, LV, Rückgabeformat, Unternehmensquellen, Angebotsfreeze, Portalfrist, Eignung, Zuschlagskriterien und Dateiversionen erfassen.",
        "2. Angebotsroute: Go/No-Go, Eignung, Preisblatt, Konzepte, Qualitätsvorsprung, Nebenangebot und Signatur trennen.",
        "3. Belegroute: jede Punktebehauptung mit Referenz, Anlage, Personal, Terminplan, SLA, Kalkulationsbrücke oder Zertifikat verbinden.",
        "4. Output: Angebotscheckliste, Konzeptgliederung, Uploadpaket, Bieterfrage, Rüge, VK-Antrag oder Vergleichsvorschlag ausgeben.",
        "5. Freigabe und Quittungsabgleich: Freeze-Datei, Hash, Portaldateiliste, Serverzeit, Geschäftsgeheimnis, Vier-Augen-Check und nächster Upload-/DMS-/MCP-Schritt.",
        "",
        "## Output-Weiche",
        "",
        "| Lage | Sofort liefern |",
        "|---|---|",
        "| Unterlagenpaket liegt vor | Dokumentenmatrix, LV-/Formatinventar, Rügefenster, Angebotsroute |",
        "| teurer aber besser | Punktebrücke, Belegmatrix, Konzeptgliederung, Wirtschaftlichkeitsargument |",
        "| Abgabe naht | Upload-/Formatexport-Check, Hashliste, Signaturcheck, Freigabeauftrag |",
        "| Nichtabhilfe oder § 134 GWB | Fristenampel, Rüge-/VK-Pfad, Anlagenverzeichnis, Kostenblick |",
    ],
    "konkurrenten-rechtsschutz": [
        "## Sofortworkflow",
        "",
        "Arbeite immer in fünf Takten: Frist sichern, Angriff wählen, Beweis bauen, Antrag formulieren, Eskalation prüfen.",
        "1. Frist sichern: Angebotsfrist, Kenntnis, Rüge, Nichtabhilfe, Stillhaltefrist, VK-Eingang und OLG-Frist berechnen.",
        "2. Angriff wählen: Unterlagenänderung, Billigzuschlag, Produktvorgabe, Konkurrentenausschluss, neue Wertung oder § 135 GWB.",
        "3. Beweis bauen: Herkunftszone, Zugangsgrund, Original, Arbeitskopie, Transformation und Tatsachenkern mit Portalnachricht, LV-Position, Hash und Aktenfundstelle mappen.",
        "4. Antrag formulieren: Rüge, VK-Antrag, Eilantrag, Akteneinsicht, OLG-Beschwerde, Vergleich oder Kostenmemo.",
        "5. Eskalation prüfen: Zulässigkeit, Präklusion, Kausalität, Zuschlagschance, Geschäftsgeheimnisse und Gegenargumente.",
        "",
        "## Output-Weiche",
        "",
        "| Lage | Sofort liefern |",
        "|---|---|",
        "| § 134 GWB oder drohender Zuschlag | Stillhalte-/Rügefrist, Eilblock, VK-Antragsgerüst |",
        "| billigster gewinnt | Billigzuschlag-Angriff, Aufklärungsrüge, Bestwertungs- und Preisformeltest |",
        "| Produkt-/Formatvorgabe | Gleichwertigkeitsangriff, LV-Fundstellen, Berichtigungsantrag |",
        "| Beweis liegt in Portal/Systemexport | Herkunftszone, Tatsachenkern, Gegenhypothese, Hash-/Transformationsmanifest, Akteneinsichtsziel und Anlagenpaket |",
    ],
}


ROLE_CASELAW_LINES = {
    "vergabestelle-behoerden": [
        "## Rechtsprechungs- und Normkern",
        "",
        "| Falltyp | Norm/Anker | Pflichtarbeit |",
        "|---|---|---|",
        "| Bestangebot | § 127 GWB, § 58 VgV; Mara C-769/23 schafft kein Nur-Preis-Verbot; AESTE C-210/24 nur enges Sozialkriterium | Qualität/Tempo/LZK und Bestwertungsmatrix |",
        "| Typ, LV, System, Format | § 31 VgV; EuGH 16.04.2026 C-568/24 Sof Medica, ECLI:EU:C:2026:305; C-424/23 DYKA Plastics | Unvermeidbarkeit, funktionale Gleichwertigkeit, GAEB/XML/Excel/PDF-Roundtrip |",
        "| Planungswettbewerb | §§ 78 bis 80 VgV; C-888/24 Adão da Fonseca, ECLI:EU:C:2026:560 | Anonymität und gleicher Klarstellungsdialog; kein Anhörungsanspruch vor Rangfolge |",
        "| Bestands-/Systemdaten | §§ 8, 41, 53 VgV; Verg 2/24, 47/18, 34/20; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe | Bestand/Migration, Zugang, Wertungsgrund, Rückgabe-Freeze |",
        "| Direktvergabe/Exklusivität | § 14 VgV, § 135 GWB; EuGH 09.01.2025 C-578/23, ECLI:EU:C:2025:4 | Lock-in-Historie, Marktsuche, Ausnahmevermerk oder Berichtigung |",
        "| Konzession/Privatinitiative | C-810/24 Urban Vision, ECLI:EU:C:2026:69 | kein nachträgliches Matching-Privileg; Informationsausgleich und gleiche Zuschlagsregeln, aber kein Pauschalverbot privater Initiativen |",
        "| Billigangebot | § 60 VgV; BGH 31.01.2017 X ZB 10/16 | Preisabstand, Aufklärung, Geschäftsgeheimnis, Wertungsfolge |",
        "| Inhouse/ÖPNV/Sanktionen | § 108 GWB; C-692/23; C-856/24, ECLI:EU:C:2026:569; C-313/24; C-590/24, ECLI:EU:C:2026:41 | Konzernumsatz, Betriebsrisiko, Kontrolle; C-590/24 nur Geldbuße, Ausschlussfragen unzulässig |",
        "| EU-Förderung | konkreter Förderakt und Vertrag; C-186/25, ECLI:EU:C:2026:567 | Vollzug, Finanzbezug, Begründung und Korrektur proportional prüfen; kein allgemeiner Rückforderungsautomatismus |",
        "| Bundeswehr | §§ 1 bis 19 BwBBG; § 19 Übergang | Bedarf/Auftraggeber/Schwelle/Zeit, Sondernorm, Drittstaaten, VK Bund, § 10/§ 17; §-16-Verweisfehler nicht ergänzen |",
        "| Netto-Null | Art. 25 VO (EU) 2024/1735; VO (EU) 2026/718 | Windrotorblätter 70 Prozent; Baupflicht, Art.-29-Feststellung, GPA und Ausnahme prüfen |",
        "| Bundestariftreue | §§ 1, 5, 14, 16 BTTG; § 160 Abs. 2 Satz 2 GWB | seit 1. Mai 2026; Bundes-Bau/Dienstleistung/Konzession ab 50.000 Euro, nicht reine Lieferung; §-5-Status, §-13-Feststellung und ArbGG-Vorentscheidung prüfen |",
        "| VK/OLG/Akteneinsicht/§ 132 | §§ 160, 165, 169, 171, 187, 132 GWB; Antea/Varec; Advania/pressetext; C-820/24 Strominator | Normfassung, Fristenampel, Schwärzungsmatrix, Laufzeit-/Änderungs-/Insolvenzvermerk |",
    ],
    "bieter-unternehmen": [
        "## Rechtsprechungs- und Normkern",
        "",
        "| Falltyp | Norm/Anker | Pflichtarbeit |",
        "|---|---|---|",
        "| Teurer, aber besser | § 127 GWB, § 58 VgV und veröffentlichte Matrix; C-769/23 Mara, ECLI:EU:C:2025:984, schafft keine zusätzlichen Kriterien; C-210/24 AESTE, ECLI:EU:C:2026:145, nur bei passendem Sozialkriterium | Punktebrücke: Kriterium, Nachweis, Mehrwert, Preisnachteil, Wertungsauswirkung |",
        "| Unterlagen/LV/Format sperren | § 31 VgV; EuGH 16.04.2026 C-568/24 Sof Medica; C-424/23 DYKA Plastics; OLG Düsseldorf Verg 2/24 | Fundstelle, Unvermeidbarkeit, Anschluss-/Migrationsalternative, Bieterfrage oder Rüge |",
        "| Planungswettbewerb | §§ 78 bis 80 VgV; C-888/24 Adão da Fonseca, ECLI:EU:C:2026:560 | vollständiger anonymer Entwurf; nur konkreten Verfahrensfehler angreifen |",
        "| Live-System/Abgabe | § 53 VgV; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe; Verg 47/18 | Angebotsfreeze, feste Uploads, Hashliste, direkter Unterlagenzugang, Quittungsabgleich |",
        "| Billigkonkurrent/Unterpreis | § 60 VgV; BGH 31.01.2017 X ZB 10/16 | Aufklärungsangriff, Qualitätsentwertung, Zuschlagschance |",
        "| Ausschluss/BG/Sanktionen | §§ 123 bis 125 GWB; §§ 13 bis 16 BTTG; § 160 Abs. 2 Satz 2 GWB; Vossloh; C-268/25 nur Schlussanträge; C-313/24; C-590/24 | §-5-Status, §-13-Feststellung, ArbGG-Vorentscheidung; Selbstreinigung/BG/Kontrolle; C-590/24 nur Geldbuße |",
        "| Konzession/Privatinitiative | § 105 GWB, KonzVgV; C-810/24 Urban Vision, ECLI:EU:C:2026:69 | Betriebsrisiko und nachträgliches Matching-Privileg prüfen; private Initiative nicht pauschal verbieten |",
        "| Bundeswehr | §§ 1 bis 19 BwBBG; § 11, § 15 Abs. 2 | Zugang, Finanzierung, Nachforderung, Vorab-Rüge, VK Bund/OLG; §-16-Verweisfehler nicht ergänzen |",
        "| Netto-Null | Art. 25 VO (EU) 2024/1735; VO (EU) 2026/718 | LV-Position, Starttag, Windquote, Fälligkeit, Baupflicht, Art.-29-Feststellung und GPA mappen |",
        "| VK/OLG/ÖPNV/§ 132 | §§ 160, 169, 171, 187, 132 GWB; C-820/24; C-856/24 | Frist/Schaden/Antrag; Bus-Sonderroute braucht Betriebsrisiko, Inhouse bleibt getrennt |",
    ],
    "konkurrenten-rechtsschutz": [
        "## Rechtsprechungs- und Normkern",
        "",
        "| Angriff | Norm/Anker | Pflichtarbeit |",
        "|---|---|---|",
        "| Billigzuschlag/Preis-only | §§ 127, 160 GWB, § 60 VgV; C-769/23 Mara, ECLI:EU:C:2025:984, nur bei konkreter Sonderregel; BGH X ZB 10/16 | veröffentlichte Matrix, Sonderregel und Niedrigpreisaufklärung getrennt; Kausalität und passende Rechtsfolge |",
        "| Produkt-/Formatbindung | § 31 VgV; EuGH 16.04.2026 C-568/24 Sof Medica; C-424/23 DYKA Plastics; OLG Düsseldorf Verg 2/24 | LV-Fundstelle, Unvermeidbarkeit, Anschluss-/Migrationsalternative, Berichtigungs- oder Rügeantrag |",
        "| Planungswettbewerb | §§ 78 bis 80 VgV; C-888/24 Adão da Fonseca, ECLI:EU:C:2026:560 | Anonymitätsbruch, Kriterienabweichung oder ungleicher Klarstellungsdialog; kein allgemeines Anhörungsrecht |",
        "| System-/Portalbeweis | § 41, § 53 VgV, § 165 GWB; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe; Verg 47/18, Verg 34/20, Verg 36/23 | Herkunftszone, Tatsachenkern, Hash/Transformation, Gegenhypothese, Akteneinsichtsziel |",
        "| Direktauftrag/ÖPNV/Änderung | §§ 132, 135, 160 GWB; C-578/23; C-820/24; C-856/24; C-810/24 | Lock-in/Laufzeit/Betriebsrisiko; C-810/24 gegen zweite Zuschlagschance, nicht private Initiative allgemein |",
        "| Ausschluss/BG/BTTG | §§ 123 bis 125 GWB; §§ 13 bis 16 BTTG; § 160 Abs. 2 Satz 2 GWB; C-268/25 nur Schlussanträge; C-313/24; C-590/24 | §-13-Feststellung, ArbGG-Vorentscheidung; Selbstreinigung/BG/Kontrolle; C-590/24 nur Geldbuße, Ausschlussfragen unzulässig |",
        "| Bundeswehr | §§ 1 bis 19 BwBBG; § 11, § 15 Abs. 2 | Zugang/Antragsbefugnis, Vorab-Rüge, Ausnahme, VK Bund, §-10-Sanktion, OLG; §-16-Verweisfehler nicht ergänzen |",
        "| Netto-Null | Art. 25 VO (EU) 2024/1735; VO (EU) 2026/718 | Windquote, Analogie, Baupflicht, Art.-29-Feststellung, GPA, Ausnahme und Rückversetzung |",
        "| Akteneinsicht/Schwärzung | § 165 GWB; Antea, Klaipedos, Varec | entscheidungserhebliche Information, Geheimnisschutz, Begründungsersatz |",
        "| VK/OLG | §§ 160, 169, 171, 173, 187 GWB; Fastweb/PFE/Randstad | Verfahrensbeginn, alte oder neue Normfassung, Rüge, Schaden, Zuschlagswirkung, Antrag |",
    ],
}


def build_prompt(plugin: dict, plugin_dir: Path, max_modules: int, desc_len: int) -> str:
    name = plugin["name"]
    manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    description = clean(plugin.get("description") or manifest.get("description") or "", 520)
    skills = collect_skills(plugin_dir)

    selected = skills[:max_modules]
    label = role_label(name)

    lines: list[str] = [
        f"# Autarker Mini-Prompt: {label}",
        "",
        f"Du arbeitest für {label}: fallbezogen, quellenbewusst und ohne generische Fülltexte.",
        "",
        "## Claude-Skill-Modus",
        "",
        "Mit Repo-Skills den passenden Slug aus der Tabelle laden; sonst vollständig autark arbeiten.",
        "",
        "| Trigger | Exakter Skill-Slug |",
        "|---|---|",
    ]
    for trigger, slug in PLUGIN_TRIGGER_ROUTES.get(name, []):
        lines.append(f"| {clean(trigger, 70)} | `{slug}` |")
    lines += ["", "## Auftrag", ""]
    role_note = ROLE_NOTES.get(name)
    if role_note:
        lines.append(clean(role_note, 330))
    else:
        lines.append(description or f"Bearbeite Fälle und Dokumente im Zuschnitt {label}.")

    starter = ROLE_STARTERS[name]
    first_view = ROLE_FIRST_VIEW[name]
    lines += [
        "",
        "## Start",
        "",
        f"Startsatz: `{starter}`",
        "",
        f"Ordner, ZIP oder Dateien ohne Skillwahl auslesen; sofort fünf Zeilen liefern: `Lage | Rot | {first_view} | Rechtsweiche | Jetzt`.",
        "Mit markierten Annahmen fortfahren. Höchstens drei echte Blockerfragen erst nach dem Arbeitsstand bündeln. Pro Durchgang Orchestrator plus höchstens drei Fachskills nutzen; bei Großakten Prioritätsdateien und nächsten Checkpoint nennen.",
        "",
    ]
    workflow_lines = ROLE_WORKFLOW_LINES.get(name)
    fallcard_lines = ROLE_FALLCARD_LINES.get(name)
    if fallcard_lines:
        lines.extend(fallcard_lines)
        lines.append("")
    if workflow_lines:
        lines.extend(workflow_lines)
        lines.append("")
    caselaw_lines = ROLE_CASELAW_LINES.get(name)
    if caselaw_lines:
        lines.extend(caselaw_lines)
        lines.append("")

    lines += [
        "## Arbeitsregeln",
        "",
        "- Deutsches Recht ist Standard; EU-/Landesrecht fallbezogen. Normen konkret, keine Scheinzitate.",
        "- Bei seit 1. Juli 2026 geändertem GWB § 187 Abs. 2 prüfen; Altverfahren samt Rechtsschutz bleiben im alten Recht.",
        "- Schwellenwerte 2026/2027: 2025/2152 klassisch, 2025/2150 Sektoren, 2025/2151 Konzessionen, 2025/2487 Verteidigung/Sicherheit.",
        "- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, Status und prüfbarer Quelle; Unsicheres markieren, nichts erfinden.",
        "- Matrix, Vermerk, Schriftsatz oder Checkliste liefern; bei Frist, Streit oder hohem Risiko menschlich endprüfen.",
        "",
        "## Arbeitsmodule",
        "",
    ]
    if selected:
        for item in selected:
            title = clean(str(item["title"]), 72)
            desc_source = MINI_SKILL_SUMMARIES.get(str(item["slug"]), str(item["desc"]))
            desc = clean(desc_source, desc_len) or "Bearbeite diesen Teilbereich anhand der Akte, der einschlägigen Normen, Fristen, Beweisfragen und des gewünschten Outputs."
            lines.append(f"- Skill `{item['slug']}` ({title}): {desc}")
    else:
        lines.append("- Autarker Arbeitsmodus: Sachverhalt strukturieren, Normen und Risiken bestimmen, verwertbaren Output erstellen und Quellenhygiene beachten.")

    lines += [
        "",
        "## Ausgabeformat",
        "",
        "Plattform-, Kammer- oder Gerichtsvorgaben gehen vor; sonst Times New Roman 11 pt und lückenlose Dezimalgliederung.",
        "Kurzdiagnose, Arbeitsprodukt, dann Selbstkontrolle zu Tatsachen, Fristen, Quellen, Gegenargument und nächstem Schritt.",
    ]
    return "\n".join(lines).strip() + "\n"


def fit_prompt(plugin: dict, plugin_dir: Path) -> str:
    for max_modules, desc_len in [(24, 160), (20, 145), (16, 135), (12, 130), (10, 120), (8, 115), (6, 110), (5, 105), (4, 120), (3, 95), (2, 80), (1, 70), (0, 0)]:
        text = build_prompt(plugin, plugin_dir, max_modules=max_modules, desc_len=desc_len)
        if len(text) <= SOFT_MAX:
            return compact_mini(text)
    text = build_prompt(plugin, plugin_dir, max_modules=0, desc_len=0)
    if len(text) <= MAX_CHARS:
        return compact_mini(text)
    raise ValueError(
        f"{plugin['name']}: vollständiger Mini-Prompt hat selbst ohne Zusatzmodule "
        f"{len(text)} Zeichen; Limit {MAX_CHARS}"
    )


def render_readme(plugins: list[dict]) -> str:
    lines = [
        "# Unified Mini Prompts",
        "",
        "[Repo-Start](../README.md) | [Dateikatalog](../README.md#dateikatalog) | "
        "[Downloads](../README.md#sofort-downloads) | "
        "[Vergabestelle](../vergabestelle-behoerden/README.md) | "
        "[Bieter](../bieter-unternehmen/README.md) | "
        "[Konkurrent](../konkurrenten-rechtsschutz/README.md) | "
        "[Alle Skills](../SKILLS.md) | [Testakten](../testakten/README.md) | "
        "[Rechtsprechung](../references/leitentscheidungen-anker.md)",
        "",
        "Ein kompakter autarker Markdown-Prompt pro Marktrolle, jeweils auf maximal 7.500 Zeichen inkl. Leerzeichen begrenzt. Diese Dateien sind für Nutzerinnen und Nutzer gedacht, die einen schnellen Ein-Datei-Prompt in einem beliebigen Chatbot verwenden wollen.",
        "",
        "Die Mini-Prompts sind bewusst Sparvarianten, aber nicht generisch: sie enthalten je Marktrolle einen Rechtsprechungs- und Normkern, konkrete vergaberechtliche Falltypen, exaktes Skill-Routing, Dashboardlogik und eine verdichtete Auswahl der wichtigsten Arbeitsmodule. Ohne installierte Skills funktionieren sie autark.",
        "",
        "## In einem Schritt verwenden",
        "",
        "Genau einen rollenpassenden Mini-Prompt zusammen mit den Fallunterlagen anhängen und den Startsatz aus der Tabelle senden. Keine Skillnamen und keinen gewünschten Output vorgeben; der Prompt liefert sofort den Fünf-Zeilen-Stand und stellt erst danach höchstens drei Blockerfragen. Bei installiertem Plugin wird der Mini-Prompt nicht zusätzlich benötigt.",
        "",
        "`Ansehen` öffnet den Prompt im Browser. `Herunterladen` liefert die einzelne Markdown-Datei aus dem aktuellen Release.",
        "",
        "| Marktrolle | Startsatz | Ansehen | Herunterladen |",
        "| --- | --- | --- | --- |",
    ]
    for plugin in plugins:
        name = plugin["name"]
        lines.append(
            f"| {role_label(name)} | `{ROLE_STARTERS[name]}` | [`{name}.md`](./{name}.md) | "
            f"[`{name}-unified-mini-prompt.md`]({RELEASE_BASE}/{name}-unified-mini-prompt.md) |"
        )
    lines.append("")
    return "\n".join(lines)


def write_prompt_file(name: str, text: str) -> Path:
    out_path = OUT_DIR / f"{name}.md"
    for stale in OUT_DIR.glob(f"{name} [0-9]*.md"):
        if stale.is_file():
            stale.unlink()
    out_path.write_text(text, encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="nur Frische der eingecheckten Dateien pruefen")
    args = parser.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plugins = marketplace()["plugins"]
    expected = {p["name"] for p in plugins}

    unexpected = [old for old in OUT_DIR.glob("*.md") if old.name != "README.md" and old.stem not in expected]
    if not args.check:
        for old in unexpected:
            old.unlink()

    too_long: list[tuple[str, int]] = []
    stale: list[Path] = list(unexpected)
    rendered: dict[str, str] = {}
    for plugin in plugins:
        name = plugin["name"]
        plugin_dir = REPO_ROOT / name
        prompt = fit_prompt(plugin, plugin_dir)
        if len(prompt.encode("utf-8")) > MAX_CHARS:
            too_long.append((name, len(prompt.encode("utf-8"))))
        rendered[name] = prompt
        out_path = OUT_DIR / f"{name}.md"
        if args.check:
            if not out_path.is_file() or out_path.read_text(encoding="utf-8") != prompt:
                stale.append(out_path)
        else:
            write_prompt_file(name, prompt)

    readme_text = render_readme(plugins)
    readme_path = OUT_DIR / "README.md"
    if args.check:
        if not readme_path.is_file() or readme_path.read_text(encoding="utf-8") != readme_text:
            stale.append(readme_path)
    else:
        readme_path.write_text(readme_text, encoding="utf-8")
    if too_long:
        for name, length in too_long:
            print(f"ZU LANG: {name} {length}")
        raise SystemExit(1)

    if stale:
        for path in sorted(set(stale)):
            print(f"VERALTET: {path.relative_to(REPO_ROOT)}")
        return 1

    sizes = [len(rendered[p["name"]].encode("utf-8")) for p in plugins]
    verb = "geprüft" if args.check else "erstellt"
    print(
        f"Unified Mini Prompts {verb}: {len(plugins)} | "
        f"max={max(sizes)} UTF-8-Bytes | avg={sum(sizes)//len(sizes)} UTF-8-Bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
