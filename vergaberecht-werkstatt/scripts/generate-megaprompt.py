#!/usr/bin/env python3
"""Erzeugt pro Plugin einen autarken, kompakten Werkstattprompt.

Ausgabe: testakten/megaprompts/<plugin>.md

Die Prioritaetsliste bestimmt die enthaltenen Fachmodule. Der in jedem Skill
identische, automatisch gepflegte Outputblock wird beim Zusammenstellen
entfernt und einmal zentral ausgegeben. ``--check`` prueft, ob die
eingecheckten Prompts frisch sind, ohne Dateien zu veraendern.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

from skill_routing_priorities import MEGAPROMPT_MODULE_LIMITS, PLUGIN_PRIORITY_SKILLS, PLUGIN_TRIGGER_ROUTES, MINI_SKILL_SUMMARIES

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / 'testakten' / 'megaprompts'

EXCLUDE_PLUGINS: set[str] = set()

# Hinweis: Der Disclaimer- und Verwendungs-Block steht im jeweiligen
# Plugin-README, nicht im Megaprompt-Markdown selbst — der Megaprompt
# soll möglichst rauschfrei in einen Chat-Agenten kopierbar sein.


def extract_frontmatter_and_body(text: str) -> tuple[str, str]:
    """Trennt YAML-Frontmatter vom Body."""
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return '', text.strip()


def get_description(frontmatter: str) -> str:
    m = re.search(r'description:\s*(.+)', frontmatter)
    if not m:
        return ''
    desc = m.group(1).strip()
    if len(desc) >= 2 and desc[0] == desc[-1] and desc[0] in {'"', "'"}:
        desc = desc[1:-1]
    return desc.strip()


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


def collect_skills(plugin_dir: Path) -> list[tuple[str, Path, str, str]]:
    """Liefert (slug, path, description, body) je Skill, sortiert nach Wichtigkeit."""
    out = []
    skills_dir = plugin_dir / 'skills'
    if not skills_dir.is_dir():
        return []
    priority_first = PLUGIN_PRIORITY_SKILLS.get(
        plugin_dir.name,
        [
            'vergabe-os-master-orchestrator',
            'konkurrenzrechtsschutz-orchestrator',
            'startbildschirm-konkurrentenangriff',
            'workflow-kaltstart-und-routing',
            'einstieg-routing',
            'output-waehlen',
            'dokumente-intake',
            'workflow-chronologie-und-belegmatrix',
            'legacy-systeme-integration',
            'kaltstart-triage',
            'mandat-triage',
            'erstgespraech-mandatsannahme',
            'erstpruefung-und-mandatsziel',
        ],
    )
    skills = []
    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir():
            continue
        skill_md = sd / 'SKILL.md'
        if not skill_md.is_file():
            continue
        text = skill_md.read_text(encoding='utf-8', errors='ignore')
        fm, body = extract_frontmatter_and_body(text)
        desc = get_description(fm)
        skills.append((sd.name, skill_md, desc, body))

    # Sortierung: Prioritaeten zuerst, dann Description-Länge (= Substanz-Proxy)
    def keyfn(item):
        slug = item[0]
        prio_idx = next((i for i, p in enumerate(priority_first)
                         if p == slug or p in slug), 999)
        return (prio_idx, -len(item[2]))

    skills.sort(key=keyfn)
    return skills


ROLE_LABELS = {
    "vergabestelle-behoerden": "Vergabestellen",
    "bieter-unternehmen": "Bieter und Bewerber",
    "konkurrenten-rechtsschutz": "Konkurrentenrechtsschutz",
}


ROLE_WORKSHOP_MODE = {
    "vergabestelle-behoerden": [
        "## Null-Konfigurations-Start",
        "",
        "Fallunterlagen anhängen und senden: `Neuer Vergabestellenfall. Prüfe die beigefügten Unterlagen vollständig, sichere Fristen und Rechtsregime und erstelle den nächsten entscheidungsreifen Behördenoutput.`",
        "",
        "Der Satz ist ein vollständiger Auftrag. Sichtbare Angaben selbst auslesen, keine Skill- oder Outputwahl verlangen und sofort genau fünf Zeilen `Lage | Rot | Akte | Rechtsweiche | Jetzt` liefern. Danach mit markierten Annahmen weiterarbeiten und höchstens drei echte Blockerfragen gesammelt stellen. Pro Durchgang höchstens drei Fachmodule für leitende Rechtsfrage, Beleg oder Format und konkreten Behördenoutput aktivieren. Bei großen Akten zuerst Umfang, Prioritätsdateien und nächsten Checkpoint anzeigen.",
        "",
        "## Werkstattablauf",
        "",
        "1. Erst Akten-, Quellen- und Systeminventar mit Feldautorität bilden: Dokument, Originalschlüssel, Stand, Einheit, Fachsystem, Version, Hash, Lücke.",
        "2. Dann Regime und Verfahren festlegen: Auftraggeber, Auftragsart, Schwelle, Landesrecht, Lose, Rechtsweg.",
        "3. Danach genau einen Fachpfad wählen: Bestwertung, Bekanntmachung, Unterlagen/LV, Wertung, Register/Ausschluss, Rüge/VK oder Upload.",
        "4. Sofort ein verwertbares Produkt liefern: Vermerk, Matrix, Feldliste, LV-/Formatpaket, Rügeerwiderung, VK-Stellungnahme oder Uploadauftrag.",
        "5. Abschließend Entscheidungsbrücke und Rückkanal kontrollieren: Tatsache, Annahme, Norm, Entscheidung, Aktenbeleg, Gegenargument, Freigabe und nächster Systemschritt.",
        "",
        "## Fallkarte vor Langtext",
        "",
        "| Feld | Behördlicher Arbeitsinhalt |",
        "|---|---|",
        "| Falltyp | Bestwertung, LV/Format, Direktvergabe, Billigangebot, VK/OLG, Unterschwelle |",
        "| Normenanker | Paragraf 127 GWB, Paragraf 31 VgV, Paragraf 14 VgV, Paragraf 60 VgV, Paragrafen 160 ff. GWB; BVerfG 1 BvR 1160/03 zur Rechtsweggrenze |",
        "| Tatbestandswichtigkeiten | Qualität/Tempo/Lebenszyklus, Gleichwertigkeit, selbst geschaffener Lock-in, Preisabstand, Rügekenntnis, Fristbeginn |",
        "| Beweislastmerker | Vergabestelle braucht Aktenbeleg, Marktsuche, Wertungsmatrix, Aufklärungsvermerk, Schwärzungsbegründung und Freigabe |",
        "| Quellenstatus | EuGH/BGH/BVerfG nur mit Gericht, Datum, Aktenzeichen, ECLI soweit vorhanden und tragender Aussage; C-268/25 nur Schlussanträge |",
        "| Rechtsfolge und Output | Matrix schärfen, Berichtigung, Aufklärung, Abhilfe/Nichtabhilfe, VK-Stellungnahme, OLG-Erwiderung oder Uploadauftrag |",
        "",
        "## Rechtsprechungsfester Kern",
        "",
        "- Bestwertung: Mara C-769/23 bestätigt nur die Zulässigkeit einer nationalen Beschränkung der Nur-Preis-Wertung; das Urteil schafft kein allgemeines Verbot. AESTE C-210/24 erlaubt im entschiedenen Sozialdienstleistungsfall ein enges Lohnsummenkriterium.",
        "- Verfahren und Vertragsänderung: Adão da Fonseca C-888/24 verneint im Planungswettbewerb den Anhörungsanspruch vor der Rangfolge. Urban Vision C-810/24 sperrt ein nachträgliches Anpassungsprivileg des privaten Projektinitiators, nicht private Initiativen allgemein. AVR-Afvalverwerking C-692/23 verlangt bei einer Inhouse-Konzernmutter den Gruppenumsatz. Sad Trasporto Locale II C-856/24 verlangt für die ÖPNV-Sonderroute übertragenes Betriebsrisiko. Strominator C-820/24 begrenzt § 132 GWB auf noch laufende Aufträge.",
        "- Sanktion und EU-Förderung: Opera Laboratori C-313/24 verlangt faktische Kontrolle und Mittelumleitungsrisiko statt Nationalitätsautomatismus. AK Dlhopolec C-590/24 betrifft verhältnismäßige Geldbußen; die Vergabeausschlussfragen waren unzulässig. Institut po ribni resursi Varna C-186/25 verlangt im konkreten EU-Förderregime individualisierte Unregelmäßigkeits-, Finanzwirkungs- und Korrekturprüfung; kein allgemeiner Rückforderungsautomatismus.",
        "- Bundeswehrbeschaffung: Seit 14. Februar 2026 gilt das BwBBG mit §-19-Übergang, punktuellen Verfahrens-, Los-, Nachweis-, Drittstaaten-, Rechtsschutz- und Änderungsregeln. Bedarf, Auftraggeber, Schwelle und Zeit zuerst belegen; regulären Ausgang und einzelne Sondernorm trennen. Den fehlerhaften Verweis in § 16 Abs. 4 auf einen nicht vorhandenen § 15 Abs. 7 offenlegen, nie mit erfundenem Inhalt schließen.",
        "- Bundestariftreue: Das BTTG gilt seit 1. Mai 2026 im §-1-Regelbereich ab 50.000 Euro netto für Bau- und Dienstleistungsaufträge sowie Konzessionen des Bundes, nicht für reine Lieferaufträge. § 14 liegt außerhalb dieser Regelgrenzen, verlangt aber eine unanfechtbare Feststellung nach § 13. § 16 schützt bis 1. Mai eingeleitete Verfahren; den Status einer Rechtsverordnung nach § 5 am Prüfungstag verifizieren. § 160 Abs. 2 Satz 2 GWB sperrt einen Verordnungsangriff ohne rechtskräftigen Beschluss nach § 98 Abs. 4 Satz 1 ArbGG.",
        "- Technik und Wertung: Sof Medica C-568/24 und DYKA C-424/23 steuern Typ-, Format- und Schnittstellengleichwertigkeit; OLG Düsseldorf Verg 2/24 verlangt konkrete System- und Migrationsbelege. Instituto Cervantes C-534/23 P und C-539/23 P betrifft EU-Eigenvergabe und dient hier nur als Integritätsanker neben § 53 VgV. OLG Düsseldorf Verg 34/20 verlangt Gründe statt bloßer Systempunkte.",
        "- Netto-Null-Technologien: Artikel 25 VO (EU) 2024/1735 und VO (EU) 2026/718 verlangen seit Sommer 2026 einen eigenen Richtlinien-, Technologie- und Starttagtest. Für Windrotorblätter mindestens 70 Prozent Rezyklierbarkeit nach Gewicht vorsehen; Bau-Zusatzpflichten, Kommissionsfeststellung, GPA und Ausnahmen getrennt dokumentieren.",
    ],
    "bieter-unternehmen": [
        "## Null-Konfigurations-Start",
        "",
        "Vergabeunterlagen anhängen und senden: `Neue Bewerbung. Prüfe die beigefügten Vergabeunterlagen vollständig, sichere Abgabefrist und Ausschlussrisiken und erstelle den nächsten abgabefertigen Angebotsoutput.`",
        "",
        "Der Satz ist ein vollständiger Auftrag. Sichtbare Angaben selbst auslesen, keine Skill- oder Outputwahl verlangen und sofort genau fünf Zeilen `Lage | Rot | Angebot | Rechtsweiche | Jetzt` liefern. Danach mit markierten Annahmen weiterarbeiten und höchstens drei echte Blockerfragen gesammelt stellen. Pro Durchgang höchstens drei Fachmodule für Angebots- oder Rechtsfrage, Beleg oder Format und konkreten Bieteroutput aktivieren. Bei großen Akten zuerst Umfang, Prioritätsdateien und nächsten Checkpoint anzeigen.",
        "",
        "## Werkstattablauf",
        "",
        "1. Erst Unterlagen-, Fristen- und Formatdiagnose bilden: Bekanntmachung, LV, Rückgabeformat, Unternehmensquellen, Angebotsfreeze, Portal, Eignung, Zuschlagsmatrix.",
        "2. Dann Angebotsroute festlegen: Go/No-Go, Eignung, Preisblatt, Konzepte, Qualitätsvorsprung, Nebenangebot, Signatur.",
        "3. Danach jede Punktebehauptung mit Beleg verbinden: Referenz, Anlage, Personal, SLA, Terminplan, Kalkulationsbrücke, Zertifikat.",
        "4. Sofort ein verwertbares Produkt liefern: Angebotscheckliste, Konzeptgliederung, Uploadpaket, Bieterfrage, Rüge oder VK-Antrag.",
        "5. Abschließend Quittungsabgleich kontrollieren: Freeze-Datei, Frist, Hash, Portaldateiliste, Geschäftsgeheimnis, Freigabe und nächster Portal-/DMS-/MCP-Schritt.",
        "",
        "## Fallkarte vor Langtext",
        "",
        "| Feld | Bieter-Arbeitsinhalt |",
        "|---|---|",
        "| Falltyp | Qualitätsvorsprung, sperrendes LV/Format, Billigkonkurrent, Ausschluss/BG, Nichtabhilfe, VK/OLG |",
        "| Normenanker | Paragraf 127 GWB, Paragraf 31 VgV, Paragraf 60 VgV, Paragrafen 123 bis 125 GWB, Paragrafen 160 ff. GWB; BVerfG 1 BvR 1160/03 zur Unterschwelle |",
        "| Tatbestandswichtigkeiten | eigener Mehrwert, Gleichwertigkeit, Preisabstand, Nachweis-/Steuermangel, Rügekenntnis, Zuschlagschance |",
        "| Darlegungs- und Beweislast | Bieter braucht Fundstelle, eigenen Beleg, Schaden, Abhilfeantrag, Geheimnisschutz und konkreten Antrag |",
        "| Quellenstatus | EuGH/BGH/BVerfG nur mit Gericht, Datum, Aktenzeichen, ECLI soweit vorhanden und tragender Aussage; C-268/25 nur Schlussanträge |",
        "| Rechtsfolge und Output | Punktebrücke, Bieterfrage, Rüge, VK-Antrag, Akteneinsichtsantrag, OLG-Briefing oder Vergleichsvorschlag |",
        "",
        "## Rechtsprechungsfester Kern",
        "",
        "- Punktebrücke: Der Nachweis für nicht billig, aber besser folgt ausschließlich aus der veröffentlichten Matrix; Mara C-769/23 schafft keine zusätzlichen Kriterien. AESTE C-210/24 hilft nur bei einem passend bekannt gemachten sozialen Kriterium.",
        "- Verfahren und Vertragsänderung: Adão da Fonseca C-888/24 verlangt im Planungswettbewerb einen vollständigen anonymen Entwurf und gewährt keine Anhörung vor der Rangfolge. Urban Vision C-810/24 sperrt ein nachträgliches Matching-Privileg des Projektinitiators. Sad Trasporto Locale II C-856/24 eröffnet bei Bus-ÖPNV den Angriff auf die Sonderroute, wenn kein Betriebsrisiko übertragen wird. Strominator C-820/24 sperrt eine Vertragsänderung nach vollständiger Leistung, endgültiger Abnahme und Schlussrechnung.",
        "- Ausschluss und Sanktion: Opera Laboratori C-313/24 schützt nicht vor einer Tatsachenprüfung, aber vor dem bloßen Nationalitätsautomatismus. AK Dlhopolec C-590/24 betrifft verhältnismäßige Geldbußen; die Fragen zum Vergabeausschluss waren unzulässig und schaffen keine Ausschlussfreiheit.",
        "- Bundeswehrbeschaffung: Seit 14. Februar 2026 gilt das BwBBG auch nach seinem §-19-Übergang. Teilnahme nach § 11, Finanzierung, Vorschuss, Nachforderung, Vorab-Rüge nach § 15 Abs. 2, VK Bund und OLG-Reserve konkret prüfen. Aus dem fehlerhaften Verweis in § 16 Abs. 4 auf einen nicht vorhandenen § 15 Abs. 7 keinen Norminhalt ableiten.",
        "- Bundestariftreue: Im §-1-Regelbereich gilt das BTTG seit 1. Mai 2026 ab 50.000 Euro netto für Bau- und Dienstleistungsaufträge sowie Konzessionen des Bundes, nicht für reine Lieferaufträge. § 14 liegt außerhalb dieser Regelgrenzen, verlangt aber eine unanfechtbare Feststellung nach § 13. § 16 und den Status einer Rechtsverordnung nach § 5 am Prüfungstag prüfen. Ein Verordnungsangriff braucht nach § 160 Abs. 2 Satz 2 GWB zuvor einen rechtskräftigen Beschluss nach § 98 Abs. 4 Satz 1 ArbGG.",
        "- Technik und Zugang: Sof Medica C-568/24 und DYKA C-424/23 tragen Gleichwertigkeit; OLG Düsseldorf Verg 2/24 verlangt eine belastbare Anschluss- oder Migrationsalternative. Instituto Cervantes C-534/23 P und C-539/23 P betrifft EU-Eigenvergabe und dient hier nur als Integritätsanker neben § 53 VgV. OLG Düsseldorf Verg 47/18 trägt den Zugangsangriff.",
        "- Netto-Null-Technologien: Bei Artikel 25 VO (EU) 2024/1735 und VO (EU) 2026/718 LV-Position, Technologie, Starttag, Windrotorblattquote, Nachweisfälligkeit, Bau-Zusatzpflicht, Kommissionsfeststellung und GPA in eine Angebots- oder Rügematrix überführen.",
    ],
    "konkurrenten-rechtsschutz": [
        "## Null-Konfigurations-Start",
        "",
        "Streitunterlagen anhängen und senden: `Neuer Konkurrentenfall. Prüfe die beigefügten Unterlagen vollständig, sichere sofort Rüge- und Zuschlagsfristen und erstelle den stärksten fristgerechten Rechtsbehelf.`",
        "",
        "Der Satz ist ein vollständiger Auftrag. Sichtbare Angaben selbst auslesen, keine Skill-, Angriffs- oder Schriftsatzwahl verlangen und sofort genau fünf Zeilen `Lage | Rot | Angriff | Rechtsweiche | Jetzt` liefern. Danach mit markierten Annahmen weiterarbeiten und höchstens drei echte Blockerfragen gesammelt stellen. Pro Durchgang höchstens drei Fachmodule für Angriff, Beweis oder Akteneinsicht und konkreten Rechtsbehelf aktivieren. Bei großen Akten zuerst Umfang, Prioritätsdateien und nächsten Checkpoint anzeigen.",
        "",
        "## Werkstattablauf",
        "",
        "1. Erst Fristen sichern: § 134 GWB, Kenntnis, Rüge, Nichtabhilfe, VK-Eingang, § 135 GWB und OLG-Frist.",
        "2. Dann Angriff wählen: Unterlagenänderung, Billigzuschlag, Produktvorgabe, Eignung/Ausschluss, neue Wertung oder de-facto-Vergabe.",
        "3. Danach Beweis mit Herkunftszone und Tatsachenkern bauen: Zugangsgrund, Original, Arbeitskopie, Transformation, Portalnachricht, LV-Position, Zeitstempel, Hash und Aktenfundstelle.",
        "4. Sofort ein verwertbares Produkt liefern: Rüge, VK-Antrag, Eilantrag, Akteneinsicht, OLG-Beschwerde, Vergleich oder Kostenmemo.",
        "5. Abschließend kontrollieren: Zulässigkeit, Präklusion, Kausalität, Zuschlagschance, Geheimnisschutz, Kosten und Gegenargument.",
        "",
        "## Fallkarte vor Langtext",
        "",
        "| Feld | Konkurrenten-Arbeitsinhalt |",
        "|---|---|",
        "| Falltyp | Billigzuschlag, Produktbindung, Direktauftrag, ungeeigneter Konkurrent, Schwärzung, Unterschwelle |",
        "| Normenanker | Paragraf 127 GWB, Paragraf 31 VgV, Paragraf 60 VgV, Paragrafen 123 bis 125, 135, 160, 165, 169 GWB; BVerfG 1 BvR 1160/03 |",
        "| Tatbestandswichtigkeiten | Preisautomatismus, technische Sperre, Lock-in, Register-/Referenzmangel, entscheidende Aktenstelle, Fristbeginn |",
        "| Darlegungs- und Beweislast | Konkurrent braucht Aktenfundstelle, Kausalität, Zuschlagschance, Frist, Geheimnisschutz und konkreten Antrag |",
        "| Quellenstatus | EuGH/BGH/BVerfG nur mit Gericht, Datum, Aktenzeichen, ECLI soweit vorhanden und tragender Aussage; C-268/25 nur Schlussanträge |",
        "| Rechtsfolge und Output | Rüge, VK-Antrag, Eilantrag, Akteneinsicht, neue Wertung, Ausschlussantrag, Kostenmemo |",
        "",
        "## Rechtsprechungsfester Kern",
        "",
        "- Billigzuschlag: Drei Pfade trennen: veröffentlichte Wertungskriterien, konkrete Sonderregel und Niedrigpreisaufklärung nach BGH X ZB 10/16. Mara C-769/23 allein trägt keinen Angriff.",
        "- Verfahren und Vertragsänderung: Adão da Fonseca C-888/24 trägt im Planungswettbewerb nur Anonymitäts-, Kriterien- oder Klarstellungsfehler, kein allgemeines Anhörungsrecht. Urban Vision C-810/24 sperrt die zweite Zuschlagschance des privaten Projektinitiators, nicht private Initiativen allgemein. Sad Trasporto Locale II C-856/24 verlangt auf der Bus-ÖPNV-Sonderroute Betriebsrisiko. Strominator C-820/24 trägt den Änderungsangriff nur nach Beleg von Leistung, endgültiger Abnahme und Schlussrechnung.",
        "- Sanktion und Ausschluss: Opera Laboratori C-313/24 verlangt konkrete Kontroll- oder Mittelumleitungsindizien. AK Dlhopolec C-590/24 betrifft die Geldbußenbemessung; die Vergabeausschlussfragen waren unzulässig und tragen keinen Ausschlussangriff.",
        "- Bundeswehrbeschaffung: Das seit 14. Februar 2026 geltende BwBBG verlangt ein eigenes Zugangs- und Antragsbefugnis-Gate nach § 11, Vorab-Rügeprüfung nach § 15 Abs. 2 und den beschleunigten VK-Bund-/OLG-Pfad. Den Verweisfehler in § 16 Abs. 4 offenlegen und nie durch erfundenen Inhalt ersetzen.",
        "- Bundestariftreue: Seit 1. Mai 2026 liegt § 14 BTTG außerhalb der §-1-Regelgrenzen, braucht aber eine unanfechtbare Feststellung nach § 13 statt bloßer Tarifbindungs- oder Verdachtsbehauptung; § 16 und Selbstreinigung prüfen. § 160 Abs. 2 Satz 2 GWB sperrt den Verordnungsangriff ohne rechtskräftigen Beschluss nach § 98 Abs. 4 Satz 1 ArbGG.",
        "- Technik und Beweis: Sof Medica C-568/24 und DYKA C-424/23 tragen Typ- und Formatangriffe; OLG Düsseldorf Verg 2/24 ist das Kompatibilitäts-Gegenargument. Instituto Cervantes C-534/23 P und C-539/23 P betrifft EU-Eigenvergabe und dient hier nur als Integritätsanker. OLG Düsseldorf Verg 47/18, Verg 34/20 und Verg 36/23 steuern Zugang, Wertungsdaten und Indizienvortrag.",
        "- Netto-Null-Technologien: Artikel 25 VO (EU) 2024/1735 und VO (EU) 2026/718 nur nach Richtlinien-, Technologie- und Starttagtest angreifen. Fehlende Windrotorblattquote, überschießende Analogie, fehlende Bau-Zusatzpflicht, unbelegte Kommissionsfeststellung, GPA-Verstoß und Ausnahmebeleg führen zu unterschiedlichen Anträgen.",
    ],
}


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
        (rf"{legacy_slug}-", ""),
        (legacy_slug, "vergaberecht-werkstatt"),
        (rf"{legacy_role}:\s*", ""),
        (r"mandantenpadlet-vergabe-canvas", "bieter-dashboard-canvas"),
        (r"Mandantenpadlet Vergabe", "Vergabe-Dashboard"),
        (r"Mandantenpadlet", "Vergabe-Dashboard"),
        (r"Bau-/Architektenrecht-Schnittstelle", "Bau-/Architektenrecht-Schnittstelle"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def normalize_display_text(text: str) -> str:
    """Formatiert generierte Arbeitsdokumente lesbarer, ohne Quell-Skills zu ändern."""
    text = sanitize_import_language(text)
    replacements = {
        "—": "-",
        "–": "-",
        "“": '"',
        "”": '"',
        "„": '"',
        "‘": "'",
        "’": "'",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    norm_suffix = r"(?:\s+Abs\.\s*[0-9]+)?(?:\s+Satz\s*[0-9]+)?(?:\s+S\.\s*[0-9]+)?(?:\s+Nr\.\s*[0-9]+)?(?:\s+Buchstabe\s+[a-z])?"
    text = re.sub(r"\b(?:Paragrafen|Paragraphen)\s+([0-9]+(?:\s*(?:-|bis|und)\s*[0-9]+)?(?:\s*ff\.?)?)", r"§§ \1", text)
    text = re.sub(rf"\b(?:Paragraf|Paragraph)\s+([0-9]+[a-zA-Z]?{norm_suffix})", r"§ \1", text)
    text = re.sub(r"\bParagraf-(?=[0-9])", "§-", text)
    return text


def role_label(plugin: str) -> str:
    return ROLE_LABELS.get(plugin, plugin.replace("-", " "))


def module_title(slug: str, body: str = "") -> str:
    heading = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    if heading:
        return sanitize_import_language(heading.group(1).strip())

    text = display_slug(slug).replace("-", " ")
    replacements = {
        "ruege": "Rüge",
        "ruegeschriftsatz": "Rügeschriftsatz",
        "nachpruefungsantrag": "Nachprüfungsantrag",
        "nachpruefungsverfahren": "Nachprüfungsverfahren",
        "nachpruefung": "Nachprüfung",
        "schwaerzung": "Schwärzung",
        "produktneutralitaet": "Produktneutralität",
        "dokumentationsluecken": "Dokumentationslücken",
        "angebotsoeffnung": "Angebotsöffnung",
        "preisqualitaet": "Preisqualität",
        "qualitaet": "Qualität",
        "ungewoehnlich": "Ungewöhnlich",
        "eignungspruefung": "Eignungsprüfung",
        "praequalifikation": "Präqualifikation",
        "erklaerung": "Erklärung",
        "erklaerungen": "Erklärungen",
        "ausschlussgruende": "Ausschlussgründe",
        "pruefung": "Prüfung",
        "pruef": "Prüf",
        "behoerden": "Behörden",
        "oeffentlich": "Öffentlich",
        "fuer": "für",
        "waehlen": "wählen",
        "gwb": "GWB",
        "vgv": "VgV",
        "uvgo": "UVgO",
        "eu": "EU",
        "vob": "VOB",
        "olg": "OLG",
        "vk": "VK",
        "gaeb": "GAEB",
        "xml": "XML",
        "pdf": "PDF",
        "lv": "LV",
        "ted": "TED",
        "dval": "DVAL",
        "eforms": "eForms",
    }
    lowercase_words = {"und", "oder", "im", "in", "mit", "für", "fuer", "nach", "der", "die", "das", "von", "zu"}
    words = []
    for index, word in enumerate(text.split()):
        lower = word.lower()
        if index > 0 and lower in lowercase_words:
            words.append("für" if lower == "fuer" else lower)
        else:
            words.append(replacements.get(lower, word.capitalize()))
    return " ".join(words)


def autark_prompt_text(text: str) -> str:
    """Entfernt interne Plugin-/Skill-Verweise aus Ein-Datei-Prompts."""
    text = normalize_display_text(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    reference_names = {
        "quellenhygiene.md": "Quellenhygiene",
        "zitierweise.md": "Zitierregeln",
        "OUTPUT-FORMAT.md": "Ausgaberegeln",
    }
    for filename, label in reference_names.items():
        text = re.sub(rf"`?(?:\.\./)*references/{re.escape(filename)}`?", label, text)
    text = re.sub(r"`?(?:\.\./)*references/[A-Za-z0-9_.\-/]+`?", "einschlägige Referenz", text)
    replacements = [
        (r"\b[Nn]utze diesen Skill\b", "Nutze dieses Arbeitsmodul"),
        (r"\b[Nn]utze den Skill\b", "Nutze das Arbeitsmodul"),
        (r"\bDiesen Arbeitsmodul\b", "Dieses Arbeitsmodul"),
        (r"\bdiesen Arbeitsmodul\b", "dieses Arbeitsmodul"),
        (r"den passenden Arbeitsmodul", "das passende Arbeitsmodul"),
        (r"passenden Arbeitsmodul", "passendes Arbeitsmodul"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    text = re.sub(
        r"Bei Detailprüfung die einschlägigen Quellenhygiene- und Zitierregeln heranziehen\.",
        "Bei Detailprüfung die vertieften Prüfpunkte dieses Prompts anwenden.",
        text,
    )
    text = re.sub(r"\bnach die einschlägige", "nach der einschlägigen", text)
    text = re.sub(r"\b(?:Quellenhygiene\s+und\s+Zitierregeln)(?:\s+und\s+Quellenhygiene\s+und\s+Zitierregeln)+", "Quellenhygiene und Zitierregeln", text)
    return text


def display_slug(slug: str) -> str:
    legacy_slug = "fach" + "anwalt-vergaberecht"
    legacy_branch = "fach" + "anwaltschaft"
    slug = re.sub(rf"^{legacy_slug}-", "", slug)
    slug = slug.replace("mandantenpadlet-vergabe-canvas", "bieter-dashboard-canvas")
    return slug.replace(legacy_branch, "anwaltliche-vertiefung")


def strip_managed_output_block(body: str) -> str:
    """Entfernt den in allen Skills identischen, verwalteten Outputblock."""
    return re.sub(
        r"\n?<!-- BEGIN output-format-block \(autogen\) -->[\s\S]*?"
        r"<!-- END output-format-block \(autogen\) -->\n?",
        "\n",
        body,
    ).strip()


def demote_markdown_headings(text: str, levels: int = 2) -> str:
    """Ordnet eingebettete Skill-Überschriften unter dem Arbeitsmodul ein."""
    output: list[str] = []
    in_fence = False
    fence_char = ""
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
            output.append(line)
            continue
        if not in_fence:
            heading = re.match(r"^(#{1,6})(\s+.*)$", line)
            if heading:
                level = min(6, len(heading.group(1)) + levels)
                line = "#" * level + heading.group(2)
        output.append(line)
    return "\n".join(output)


def build_megaprompt(plugin_dir: Path) -> str | None:
    """Erzeugt Megaprompt-Markdown für ein Plugin. None bei skip."""
    plugin = plugin_dir.name
    if plugin in EXCLUDE_PLUGINS:
        return None
    all_skills = collect_skills(plugin_dir)
    if not all_skills:
        return None
    skills = all_skills
    n_total = len(skills)
    configured_limit = MEGAPROMPT_MODULE_LIMITS.get(plugin)
    if configured_limit is None and plugin in MEGAPROMPT_MODULE_LIMITS:
        coverage = f"alle {n_total} Arbeitsmodule"
    elif configured_limit:
        skills = skills[:configured_limit]
        coverage = f"die {configured_limit} priorisierten Arbeitsmodule von insgesamt {n_total}"
    elif n_total > 100:
        # Sehr große Plugins: top-18, damit Kernrouting plus operative Fachmodule sichtbar bleiben.
        skills = skills[:18]
        coverage = f"die 18 priorisierten Arbeitsmodule von insgesamt {n_total} (für Chat-Fenster gestrafft)"
    elif n_total > 60:
        # Große Plugins (z.B. insolvenzrecht): top-10
        skills = skills[:10]
        coverage = f"die 10 priorisierten Arbeitsmodule von insgesamt {n_total}"
    elif n_total > 20:
        skills = skills[:15]
        coverage = f"die 15 priorisierten Arbeitsmodule von insgesamt {n_total}"
    else:
        coverage = f"alle {n_total} Arbeitsmodule"

    lines = []
    label = role_label(plugin)
    lines.append(f'# Autarker Megaprompt: {label}')
    lines.append('')
    lines.append(f'## Zusammensetzung')
    lines.append('')
    lines.append(f'Dieser Megaprompt ist ein eigenständiger Arbeitsmodus für {label}. Er enthält {coverage}. Wenn Claude-Skills dieses Repos verfügbar sind, zuerst den passenden Skill-Slug laden; ohne Skills funktioniert der Prompt autark.')
    lines.append('')
    lines.extend(ROLE_WORKSHOP_MODE.get(plugin, []))
    if lines[-1] != '':
        lines.append('')
    lines.append('## Verbindliche Rechtsstandsweiche')
    lines.append('')
    lines.append('Vor jeder Anwendung der §§ 169 bis 173 GWB zuerst § 187 Abs. 2 GWB prüfen und den Beginn des Vergabeverfahrens belegen. Vor dem 1. Juli 2026 begonnene Vergabeverfahren bleiben einschließlich anschließender Nachprüfungs- und Beschwerdeverfahren im alten Recht. Nur Verfahren ab dem 1. Juli 2026 folgen der Neufassung; dort hat die Beschwerde nach Ablehnung des Nachprüfungsantrags gemäß § 173 Abs. 1 GWB keine aufschiebende Wirkung. Im fortgeltenden Altrecht einen Verlängerungsantrag nach dem früheren § 173 Abs. 1 Satz 3 GWB nur bei dessen Tatbestand verwenden.')
    lines.append('Schwellenwerte 2026/2027 nicht als ungeordnete Verordnungsliste behandeln: Delegierte VO (EU) 2025/2152 gilt für klassische Vergaben, 2025/2150 für Sektoren, 2025/2151 für Konzessionen und 2025/2487 für Verteidigungs- und Sicherheitsvergaben. Zuordnung, Geltungszeitraum und Wert am Schätzstichtag live prüfen.')
    lines.append('')
    lines.append('## Claude-Skill-Routing')
    lines.append('')
    lines.append('| Trigger | Exakter Skill-Slug |')
    lines.append('|---|---|')
    for trigger, slug in PLUGIN_TRIGGER_ROUTES.get(plugin, []):
        lines.append(f'| {trigger} | `{slug}` |')
    lines.append('')
    lines.append('## Sichtbare Skill-Slugs')
    lines.append('')
    lines.append('Die folgenden Fachmodule sind in diesem Ein-Datei-Prompt vollständig enthalten; weitere Pluginskills bleiben über das Routing erreichbar.')
    lines.append('')
    for slug, _, desc, _ in skills:
        summary = MINI_SKILL_SUMMARIES.get(slug, autark_prompt_text(desc))
        lines.append(f'- `{slug}`: {shorten_text(autark_prompt_text(summary), 180)}')
    lines.append('')
    lines.append('## Inhaltsverzeichnis')
    lines.append('')
    for i, (slug, _, desc, body) in enumerate(skills, 1):
        short_desc = autark_prompt_text(desc)
        short = shorten_text(short_desc, 120)
        lines.append(f'{i}. `{slug}` - {module_title(slug, body)} - {short}')
    lines.append('')
    lines.append('---')
    lines.append('')

    for slug, _, desc, body in skills:
        lines.append(f'## Arbeitsmodul: {module_title(slug, body)}')
        lines.append('')
        if desc:
            lines.append(f'_{autark_prompt_text(desc)}_')
            lines.append('')
        module_body = autark_prompt_text(strip_managed_output_block(body))
        lines.append(demote_markdown_headings(module_body))
        lines.append('')
        lines.append('---')
        lines.append('')

    lines.append('## Verbindliches Ausgabeformat')
    lines.append('')
    lines.append('1. Mit Kurzdiagnose, Rechtsstandsweiche und Fristenampel beginnen.')
    lines.append('2. Tatsachen, Annahmen, Rechtsfragen und fehlende Belege getrennt ausweisen.')
    lines.append('3. Gericht, Datum, Aktenzeichen, ECLI soweit vorhanden, Entscheidungsstatus und tragende Aussage angeben; unsichere Fundstellen nicht verwenden.')
    lines.append('4. Das gewählte Arbeitsprodukt vollständig liefern: insbesondere Vermerk, Matrix, Bieterfrage, Rüge, Antrag, Erwiderung, Upload- oder Übergabepaket.')
    lines.append('5. Mit Gegenargument, Rechtsfolge, Verantwortlichkeit, Freigabepunkt und nächstem Schritt schließen.')
    lines.append('')
    lines.append('## Anwendungshinweise')
    lines.append('')
    lines.append('1. Diesen Megaprompt als Kontext in den Chat einfügen oder als Datei hochladen.')
    lines.append('2. Den eigentlichen juristischen Fall beschreiben.')
    lines.append('3. Den Chat-Agent bitten, sich anhand der oben aufgeführten Arbeitsmodule zu orientieren.')
    lines.append('4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.')
    lines.append('')
    return normalize_display_text('\n'.join(lines) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='nur Frische der eingecheckten Prompts pruefen')
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    stale_outputs: list[Path] = []
    for plugin_dir in sorted(REPO.iterdir()):
        if not plugin_dir.is_dir():
            continue
        # nur echte Plugin-Verzeichnisse (mit .claude-plugin/plugin.json)
        if not (plugin_dir / '.claude-plugin' / 'plugin.json').is_file():
            continue
        if plugin_dir.name in EXCLUDE_PLUGINS:
            skipped += 1
            continue
        mp = build_megaprompt(plugin_dir)
        if mp is None:
            skipped += 1
            continue
        out_path = OUT / f'{plugin_dir.name}.md'
        if args.check:
            if not out_path.is_file() or out_path.read_text(encoding='utf-8') != mp:
                stale_outputs.append(out_path)
            size_kb = len(mp.encode('utf-8')) / 1024
        else:
            for stale in OUT.glob(f'{plugin_dir.name} [0-9]*.md'):
                if stale.is_file():
                    stale.unlink()
            out_path.write_text(mp, encoding='utf-8')
            size_kb = out_path.stat().st_size / 1024
        if size_kb > 200:
            print(f'  WARN {plugin_dir.name}: {size_kb:.0f} KB (groß für Chat-Fenster)')
        created += 1
    if stale_outputs:
        print('Veraltete Megaprompts:')
        for path in stale_outputs:
            print(f'- {path.relative_to(REPO)}')
        return 1
    verb = 'geprüft' if args.check else 'erstellt'
    print(f'Megaprompts {verb}: {created} | übersprungen: {skipped}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
