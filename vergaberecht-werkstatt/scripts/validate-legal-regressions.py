#!/usr/bin/env python3
"""Sperrt bekannte, besonders folgenreiche Vergaberechts-Regressionen."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from legal_artifact_text import binary_legal_files, read_binary_legal_text

ROOT = Path(__file__).resolve().parents[1]
SCHWERIN = ROOT / "testakten" / "it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung"
SKIP_PARTS = {".git", ".venv", "dist", "node_modules", "audits", "tests"}
LEGAL_TEXT_SUFFIXES = {".md", ".eml", ".txt", ".csv", ".xml", ".json", ".html"}
EUGH_JUDGMENT_METADATA = {
    "C-652/22": ("22.10.2024", "ECLI:EU:C:2024:910"),
    "C-424/23": ("16.01.2025", "ECLI:EU:C:2025:15"),
    "C-578/23": ("09.01.2025", "ECLI:EU:C:2025:4"),
    "C-266/22": ("13.03.2025", "ECLI:EU:C:2025:178"),
    "C-452/23": ("29.04.2025", "ECLI:EU:C:2025:284"),
    "C-534/23 P": ("03.07.2025", "ECLI:EU:C:2025:523"),
    "C-539/23 P": ("03.07.2025", "ECLI:EU:C:2025:523"),
    "C-282/24": ("16.10.2025", "ECLI:EU:C:2025:790"),
    "C-769/23": ("18.12.2025", "ECLI:EU:C:2025:984"),
    "C-692/23": ("15.01.2026", "ECLI:EU:C:2026:4"),
    "C-812/24": ("22.01.2026", "ECLI:EU:C:2026:38"),
    "C-590/24": ("22.01.2026", "ECLI:EU:C:2026:41"),
    "C-810/24": ("05.02.2026", "ECLI:EU:C:2026:69"),
    "C-313/24": ("12.02.2026", "ECLI:EU:C:2026:91"),
    "C-210/24": ("05.03.2026", "ECLI:EU:C:2026:145"),
    "C-568/24": ("16.04.2026", "ECLI:EU:C:2026:305"),
    "C-820/24": ("04.06.2026", "ECLI:EU:C:2026:452"),
    "C-186/25": ("09.07.2026", "ECLI:EU:C:2026:567"),
    "C-856/24": ("09.07.2026", "ECLI:EU:C:2026:569"),
    "C-888/24": ("09.07.2026", "ECLI:EU:C:2026:560"),
}


def compile_eugh_citation_patterns() -> dict[str, tuple[re.Pattern[str], re.Pattern[str]]]:
    """Kompiliert die teuren Zitatmuster einmal statt je Datei und Fundstelle."""
    patterns: dict[str, tuple[re.Pattern[str], re.Pattern[str]]] = {}
    for case_number in EUGH_JUDGMENT_METADATA:
        escaped_case = re.escape(case_number)
        patterns[case_number] = (
            re.compile(
                rf"EuGH,?\s+Urteil\s+vom\s+(?P<date>\d{{2}}\.\d{{2}}\.\d{{4}})"
                rf"(?:(?!EuGH|C-\d+/\d+).){{0,120}}?{escaped_case}",
                re.I,
            ),
            re.compile(
                rf"{escaped_case}(?:(?![;|\n]).){{0,180}}?"
                rf"(?P<ecli>ECLI:EU:C:\d{{4}}:\d+)",
                re.I,
            ),
        )
    return patterns


EUGH_CITATION_PATTERNS = compile_eugh_citation_patterns()
REQUIRED_CURRENT_LAW = {
    ROOT / "bieter-unternehmen" / "skills" / "nachpruefungsverfahren-paragraf-160-gwb" / "SKILL.md": (
        "§ 160 Abs. 3 Satz 1 Nr. 5 GWB",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§ 98 Abs. 4 Satz 1 ArbGG",
        "§ 180 Abs. 2 GWB",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "ruegeschriftsatz-erstellen" / "SKILL.md": (
        "§ 160 Abs. 3 Satz 1 Nr. 5 GWB",
        "§ 180 Abs. 2 GWB",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "losbildung-mittelstandsfoerderung" / "SKILL.md": (
        "§ 97a Abs. 3",
        "§ 97a Abs. 4",
        "§ 97a Abs. 5",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "vertiefung-losbildung-mittelstandsfoerderung" / "SKILL.md": (
        "§ 97a Abs. 3",
        "§ 97a Abs. 4",
        "§ 97a Abs. 5",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "inhouse-interkommunal" / "SKILL.md": (
        "C-692/23",
        "§ 108 Abs. 7",
        "§ 108 Abs. 8 GWB",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "vertiefung-inhouse-interkommunal" / "SKILL.md": (
        "C-692/23",
        "§ 108 Abs. 7 GWB",
        "§ 108 Abs. 8 GWB",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "vertragsaenderung-132-gwb-change-control" / "SKILL.md": (
        "C-820/24",
        "endgültig abgenommen",
        "Schlussrechnung",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "27-vertragsanpassung-paragraf-132-gwb" / "SKILL.md": (
        "C-820/24",
        "endgültig abgenommen",
        "Schlussrechnung",
    ),
    ROOT / "konkurrenten-rechtsschutz" / "skills" / "de-facto-vergabe-135-gwb" / "SKILL.md": (
        "C-820/24",
        "endgültig abgenommen",
        "Schlussrechnung",
        "unstatthaft",
        "§ 135 Abs. 4 GWB",
        "Geldsanktion",
        "Laufzeitverkürzung",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "12-ausschlussgruende-pruefen" / "SKILL.md": (
        "C-313/24",
        "C-590/24",
        "ECLI:EU:C:2026:41",
        "Vorlagefragen zum automatischen Vergabeausschluss waren unzulässig",
        "faktische Kontroll",
        "Mittelumleitung",
        "§ 14 BTTG",
        "§ 14 ist von den Regelgrenzen des § 1 Abs. 1 und 3 BTTG ausgenommen",
        "unanfechtbar nach § 13 Abs. 1 BTTG",
        "§ 16 BTTG",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§ 98 Abs. 4 Satz 1 ArbGG",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "14-eu-erklaerungen-ausschlussgruende" / "SKILL.md": (
        "C-313/24",
        "C-590/24",
        "ECLI:EU:C:2026:41",
        "Fragen zum automatischen Vergabeausschluss hat der EuGH nicht in der Sache entschieden",
        "Mittelumleitungsrisiko",
        "§ 14 BTTG",
        "§ 14 ist von den Regelgrenzen des § 1 Abs. 1 und 3 BTTG ausgenommen",
        "§ 16 BTTG",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§ 98 Abs. 4 Satz 1 ArbGG",
    ),
    ROOT / "konkurrenten-rechtsschutz" / "skills" / "eignungs-und-ausschlussangriff-konkurrent" / "SKILL.md": (
        "C-313/24",
        "C-590/24",
        "ECLI:EU:C:2026:41",
        "Vorlagefragen zum automatischen Vergabeausschluss waren unzulässig",
        "Nationalitätsautomatismus",
        "§ 14 BTTG",
        "unanfechtbare Feststellung nach § 13 Abs. 1 BTTG",
        "§ 14 ist von den Regelgrenzen des § 1 Abs. 1 und 3 BTTG ausgenommen",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§ 98 Abs. 4 Satz 1 ArbGG",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "nachhaltigkeit-tariftreue-lksg-cbam" / "SKILL.md": (
        "EuGH, Urteil vom 05.03.2026, C-210/24",
        "ECLI:EU:C:2026:145",
        "seit 1. Mai 2026",
        "§ 16 BTTG",
        "50.000 Euro netto",
        "Reine Lieferaufträge fallen nicht darunter",
        "Verordnungsbestand nach § 5 BTTG",
        "Abrufdatum sichern",
        "§ 11 BTTG",
        "§ 14 BTTG",
        "§ 14 ist vom Regelanwendungsbereich des § 1 Abs. 1 und 3 BTTG ausgenommen",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§ 98 Abs. 4 Satz 1 ArbGG",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "09-angebotskalkulation-stueckpreise" / "SKILL.md": (
        "seit 1. Mai 2026 geltende Bundestariftreuegesetz",
        "§ 16 BTTG",
        "reine Lieferaufträge fallen nicht",
        "BTTG-Verordnungsstatus beim BMAS mit Abrufdatum sichern",
        "§ 160 Abs. 2 Satz 2 GWB",
        "§ 98 Abs. 4 Satz 1 ArbGG",
    ),
    ROOT / "references" / "zuschlag-nicht-nur-preis.md": (
        "C-769/23",
        "unionsweites Nur-Preis-Verbot",
        "C-210/24",
    ),
    ROOT / "references" / "leitentscheidungen-anker.md": (
        "C-568/24",
        "nicht vollständig vorab veröffentlicht",
        "C-888/24",
        "kein",
        "Anhörung",
        "C-820/24",
        "C-692/23",
        "C-313/24",
        "C-590/24",
        "ECLI:EU:C:2026:41",
        "C-810/24",
        "ECLI:EU:C:2026:69",
        "C-186/25",
        "ECLI:EU:C:2026:567",
        "Kein allgemeiner deutscher Rückforderungs- oder §-132-Automatismus",
        "§ 97a Abs. 4 GWB",
        "C-268/25",
        "ECLI:EU:C:2026:382",
        "Noch kein EuGH-Urteil",
        "## Bundestariftreuegesetz seit 1. Mai 2026",
        "§ 14 BTTG ist ausdrücklich von den Regelgrenzen des § 1 Abs. 1 und 3 BTTG ausgenommen",
        "§ 160 Abs. 2 Satz 2 GWB",
        "Verordnungsbestand nach § 5 BTTG",
        "Abrufdatum sichern",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "freiberufliche-leistungen-hoai" / "SKILL.md": (
        "C-888/24",
        "nicht verlangen",
        "anonymitätswahrenden Dialog",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "architektenrecht-compliance-dokumentation-und-akte" / "SKILL.md": (
        "C-888/24",
        "keine Anhörung",
    ),
    ROOT / "konkurrenten-rechtsschutz" / "skills" / "wertungsangriff-und-dokumentationsluecken" / "SKILL.md": (
        "C-888/24",
        "kein Anspruch auf Anhörung",
        "C-810/24",
        "ECLI:EU:C:2026:69",
        "Keine allgemeine Unzulässigkeit",
    ),
    ROOT / "testakten" / "03-bauleistung-stadthalle-musterstadt" / "01_bekanntmachung_pruefnotiz.md": (
        "erst aus den Vergabeunterlagen erkennbar",
        "§ 160 Abs. 3 Satz 1 Nr. 3 GWB",
    ),
    ROOT / "testakten" / "03-bauleistung-stadthalle-musterstadt" / "daten" / "fristenmatrix.csv": (
        "§ 160 Abs. 3 Satz 1 Nr. 3 GWB",
        "spätestens bis Angebotsfrist",
    ),
    ROOT / "testakten" / "05-insolvenz-auftragnehmerwechsel-132-gwb" / "10_vk_fristen_und_kosten.csv": (
        "Kenntnis DataPortus,29.10.2026",
        "Rüge DataPortus,03.11.2026",
        "Nichtabhilfe zugegangen,05.11.2026",
        "VK-Antrag,10.11.2026",
        "§ 160 GWB; § 169 Abs. 3 GWB",
        "keine automatische Zuschlagssperre unterstellen",
    ),
    ROOT / "references" / "veroeffentlichungswege.md": (
        "§ 40 Abs. 1 Satz 2 VgV",
        "angegebenen späteren Veröffentlichungstag",
        "tatsächliche Publikationsbestätigung",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "13-angebotsoeffnung-protokoll" / "SKILL.md": (
        "§ 55 VgV",
        "§ 17 Abs. 15 VgV",
        "§ 57 Abs. 1 Nr. 1 VgV",
        "elektronischen Angeboten",
        "dauerhafte Vollständigkeit und Unverändertheit",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "vergaberechtliche-pruefung-anwaltlich" / "SKILL.md": (
        "§ 17 Abs. 15 VgV",
        "§ 56 VgV",
        "§ 57 Abs. 1 Nr. 1 VgV",
        "es sei denn, der Bieter hat den Mangel nicht zu vertreten",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "vergaberechtliche-pruefung-anwaltlich" / "SKILL.md": (
        "§ 17 Abs. 15 VgV",
        "§ 56 VgV",
        "§ 57 Abs. 1 Nr. 1 VgV",
        "es sei denn, der Bieter hat den Mangel nicht zu vertreten",
        "§ 187 Abs. 2 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "references" / "BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md": (
        "§ 55 Abs. 2 BHO",
        "§ 3a Abs. 2",
        "BAnz AT 16.12.2025 B7",
        "2026-05-16",
        "§ 6 SHVgVO",
        "ThürVVöA",
        "BAnz AT 18.06.2026 B3",
        "BAnz AT 18.06.2026 B4",
        "BAnz AT 18.06.2026 B5",
        "keine allgemein geltenden gesetzlichen Wertgrenzen",
    ),
    ROOT / "bieter-unternehmen" / "references" / "BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md": (
        "§ 55 Abs. 2 BHO",
        "§ 3a Abs. 2",
        "BAnz AT 16.12.2025 B7",
        "2026-05-16",
        "§ 6 SHVgVO",
        "ThürVVöA",
        "BAnz AT 18.06.2026 B3",
        "BAnz AT 18.06.2026 B4",
        "BAnz AT 18.06.2026 B5",
        "keine allgemein geltenden gesetzlichen Wertgrenzen",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "19-vorabinformation-paragraf-134" / "SKILL.md": (
        "§ 134 Abs. 3 GWB",
        "besonderer Dringlichkeit",
        "Rahmenvereinbarung",
        "dynamischen Beschaffungssystem",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "aufklaerung-nachforderung-56-vgv" / "SKILL.md": (
        "§ 56 Abs. 2 VgV",
        "§ 56 Abs. 3 VgV",
        "keine pauschale Fünf-Tage-Frist",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "14-aufklaerung-unangemessen-niedrige-preise" / "SKILL.md": (
        "§ 60 Abs. 3 Satz 1 VgV",
        "Zwingend ablehnen",
        "§ 128 Abs. 1 GWB",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "sektorenvergabe-sektvo" / "SKILL.md": (
        "§ 52 SektVO",
        "§ 53 SektVO",
        "§ 31 SektVO betrifft ausschließlich",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "konzessionsvergabe-konzvgv" / "SKILL.md": (
        "§ 152 Abs. 3 GWB",
        "§ 31 KonzVgV",
        "§ 3 KonzVgV",
        "C-810/24",
        "Kein Vorkaufs-, Matching- oder Anpassungsrecht",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "vertiefung-konzessionsvergabe-konzvgv" / "SKILL.md": (
        "§ 154 Nr. 3 GWB",
        "§ 31 KonzVgV",
        "§ 16 KonzVgV betrifft nicht",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "foerdermittelvergabe-rueckforderung" / "SKILL.md": (
        "C-186/25",
        "ECLI:EU:C:2026:567",
        "keine allgemeine deutsche Rückforderungsnorm",
        "Keine automatische Vertragsänderung",
        "25-Prozent-Korrektur",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "konzvgv-risikoampel-und-gegenargumente" / "SKILL.md": (
        "C-810/24",
        "ECLI:EU:C:2026:69",
        "nicht als allgemeines Verbot",
    ),
    ROOT / "references" / "bundeswehrbeschaffung-bwbbg-2026.md": (
        "seit 14. Februar 2026",
        "§ 19 BwBBG",
        "§ 15 Abs. 2 BwBBG",
        "§ 10 BwBBG",
        "§ 17 BwBBG",
        "nicht vorhandenen § 15 Abs. 7",
        "zehn Prozent",
    ),
    ROOT / "vergabestelle-behoerden" / "skills" / "bundeswehrbeschaffung-bwbbg-2026" / "SKILL.md": (
        "§ 19 BwBBG",
        "§ 15 Abs. 2 BwBBG",
        "§ 10 BwBBG",
        "C-820/24",
        "nicht vorhandenen § 15 Abs. 7",
    ),
    ROOT / "bieter-unternehmen" / "skills" / "bundeswehrbeschaffung-bwbbg-2026" / "SKILL.md": (
        "§ 19",
        "§ 11 BwBBG",
        "§ 15 Abs. 2 BwBBG",
        "VK Bund",
        "nicht vorhandenen § 15 Abs. 7",
    ),
    ROOT / "konkurrenten-rechtsschutz" / "skills" / "bundeswehrbeschaffung-bwbbg-2026" / "SKILL.md": (
        "§ 11 BwBBG",
        "§ 15 Abs. 2 BwBBG",
        "§ 10 BwBBG",
        "VK-Antrag",
        "nicht vorhandenen § 15 Abs. 7",
    ),
}

REQUIRED_THRESHOLD_SOURCES = (
    ROOT / "CLAUDE.md",
    ROOT / "README.md",
    ROOT / "testakten" / "README.md",
    ROOT / "vergabestelle-behoerden" / "skills" / "schwellenwerte-2026-2027-livecheck" / "SKILL.md",
    ROOT / "bieter-unternehmen" / "skills" / "schwellenwerte-2026-2027-livecheck" / "SKILL.md",
    ROOT / "vergabestelle-behoerden" / "skills" / "eu-schwelle-vergabeordnung-richtlinie-2014-24" / "SKILL.md",
    ROOT / "bieter-unternehmen" / "skills" / "eu-schwelle-vergabeordnung-richtlinie-2014-24" / "SKILL.md",
)
REQUIRED_THRESHOLD_MARKERS = (
    "2025/2150",
    "2025/2151",
    "2025/2152",
    "2025/2487",
)


def legal_text_files(root: Path = ROOT) -> list[Path]:
    return sorted(
        path for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in LEGAL_TEXT_SUFFIXES
        if not SKIP_PARTS.intersection(path.relative_to(ROOT).parts)
    )


RULES: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "Schwellenwert-VO 2025/2150 faelschlich klassischen Vergaben zugeordnet",
        re.compile(r"2025/2150\s+(?:für\s+)?(?:klassisch|RL\s*2014/24)", re.I),
    ),
    (
        "Schwellenwert-VO 2025/2151 faelschlich Sektorenvergaben zugeordnet",
        re.compile(r"2025/2151\s+(?:für\s+)?(?:Sektor|RL\s*2014/25)", re.I),
    ),
    (
        "Schwellenwert-VO 2025/2152 faelschlich Konzessionen zugeordnet",
        re.compile(r"2025/2152\s+(?:für\s+)?(?:Konzession|RL\s*2014/23)", re.I),
    ),
    (
        "Sof Medica faelschlich als Pflicht zur vollstaendigen Vorabveroeffentlichung der Begruendung dargestellt",
        re.compile(
            r"(?:Sof Medica|C-568/24)[^\n]{0,180}"
            r"(?:Begründung|Rechtfertigung|Sachgrund)\s+muss\s+"
            r"(?![^\n]{0,50}\bnicht\b)[^\n]{0,80}(?:bereits|vollständig)"
            r"[^\n]{0,60}(?:Vergabeunterlagen|Auftragsunterlagen|Bekanntmachung)",
            re.I,
        ),
    ),
    (
        "AESTE C-210/24 mit falschem Urteilsdatum zitiert",
        re.compile(
            r"EuGH,?\s+Urteil\s+vom\s+(?!05\.03\.2026\b)\d{2}\.\d{2}\.\d{4}"
            r"[^\n]{0,100}C-210/24",
            re.I,
        ),
    ),
    (
        "AESTE C-210/24 mit falschem ECLI zitiert",
        re.compile(
            r"C-210/24[^\n]{0,160}ECLI:EU:C:(?!2026:145\b)\d{4}:\d+",
            re.I,
        ),
    ),
    (
        "SektVO-Zuschlagskriterien faelschlich § 31 statt § 52 zugeordnet",
        re.compile(
            r"(?:Wertung|Zuschlagskriterien?)\s+(?:nach\s+)?§\s*31\s+SektVO|"
            r"§\s*31\s+SektVO\s*\((?:Wertung|Zuschlag)",
            re.I,
        ),
    ),
    (
        "KonzVgV-Zuschlagskriterien faelschlich § 16 statt § 31 zugeordnet",
        re.compile(
            r"(?:Wertung|Zuschlagskriterien?)\s+(?:nach\s+)?§\s*16\s+KonzVgV|"
            r"§\s*16\s+KonzVgV\s*\((?:Wertung|Zuschlag)",
            re.I,
        ),
    ),
    (
        "§ 135 GWB unzulaessig auf 30 Tage ab blosser Kenntnis verkuerzt",
        re.compile(r"(?:§\s*135[^\n]{0,100})?30\s+(?:Kalendertage|Tage)(?:-Frist)?\s+(?:ab|nach)\s+(?:der\s+)?Kenntnis", re.I),
    ),
    (
        "§ 135 GWB durch mehrdeutige Kenntnis-/Frist-Kurzformel verkuerzt",
        re.compile(r"Kenntnis,\s*30\s*Tage|30-Tage/6-Monats-Fristen", re.I),
    ),
    (
        "BTTG-Verordnungsstatus mit schnell veraltendem Tagesstand festgeschrieben",
        re.compile(
            r"Stand\s+14\.\s*Juli\s+2026[^\n]{0,120}(?:keine|noch\s+keine)\s+"
            r"Rechtsverordnung\s+nach\s+§\s*5\s+BTTG|"
            r"keine\s+§-5-Verordnung\s+am\s+14\.\s*Juli\s+2026",
            re.I,
        ),
    ),
    (
        "erfundene Gebuehrentabelle zu § 182 GWB",
        re.compile(r"Anlage\s+zu\s+§\s*182\s+GWB|§\s*182[^\n]{0,100}(?:0,5\s*%|1\s*%\s+des\s+Mehrbetrags)", re.I),
    ),
    (
        "OLG-Streitwert mit Nettoauftragswert oder Kammermindestgebuehr verwechselt",
        re.compile(r"Streitwert\s*=\s*Netto-Auftragswert|Mindestwert\s+2\.500\s+Euro", re.I),
    ),
    (
        "§ 160 Abs. 3 Nr. 2 oder 3 faelschlich an Kenntnis geknuepft",
        re.compile(r"§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*[23][^\n]{0,80}(?:ab|mit)\s+Kenntnis", re.I),
    ),
    (
        "§ 160 Abs. 3 Nr. 2 oder 3 faelschlich als Unverzueglichkeitsfrist behandelt",
        re.compile(
            r"(?:unverzüglich|unverzueglich)[^\n]{0,100}§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*[23]|"
            r"§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*[23][^\n]{0,100}(?:unverzüglich|unverzueglich)",
            re.I,
        ),
    ),
    (
        "§ 160 Abs. 3 Nr. 2 faelschlich einem Unterlagenverstoß zugeordnet",
        re.compile(
            r"^(?![^\n]*(?:Nr\.?\s*3|(?:oder|und)\s*3))(?=[^\n]*(?:Vergabeunterlagen|Ausschreibungsunterlagen|Unterlagenfehler))"
            r"[^\n]*§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*2[^\n]*$|"
            r"^(?![^\n]*(?:Nr\.?\s*3|(?:oder|und)\s*3))(?=[^\n]*§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*2)"
            r"[^\n]*(?:Vergabeunterlagen|Ausschreibungsunterlagen|Unterlagenfehler)[^\n]*$",
            re.I | re.M,
        ),
    ),
    (
        "§ 160 Abs. 3 Nr. 3 faelschlich einem Bekanntmachungsverstoß zugeordnet",
        re.compile(
            r"^(?![^\n]*(?:Nr\.?\s*2|(?:oder|und)\s*2))(?=[^\n]*Bekanntmachungsverstoß)"
            r"[^\n]*§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*3[^\n]*$|"
            r"^(?![^\n]*(?:Nr\.?\s*2|(?:oder|und)\s*2))(?=[^\n]*§\s*160\s+Abs\.\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*3)"
            r"[^\n]*Bekanntmachungsverstoß[^\n]*$",
            re.I | re.M,
        ),
    ),
    (
        "Rügefrist faelschlich in Werktagen oder als Unverzueglichkeit bezeichnet",
        re.compile(r"(?:10|zehn)\s+Werktage[^\n]{0,100}§\s*160|3\.\s*Werktag\s*=\s*unverzüglich", re.I),
    ),
    (
        "Rüge faelschlich von qualifizierter Signatur abhaengig gemacht",
        re.compile(r"E-Mail\s+ohne\s+QES\s+nur|Form\s+Schriftform\s+oder\s+qualifiziert", re.I),
    ),
    (
        "Antragsbefugnis der falschen Vorschrift zugeordnet",
        re.compile(
            r"Antragsbefugnis[^\n]{0,120}§\s*160\s+Abs\.\s*1\s+GWB|"
            r"§\s*160\s+Abs\.\s*1\s+GWB[^\n]{0,120}Antragsbefugnis",
            re.I,
        ),
    ),
    (
        "Schadensmerkmal der Antragsbefugnis faelschlich § 160 Abs. 1 zugeordnet",
        re.compile(
            r"(?:drohender|eingetretener|entstandener)\s+Schaden[^\n]{0,120}§\s*160\s+Abs\.\s*1|"
            r"§\s*160\s+Abs\.\s*1[^\n]{0,120}(?:drohender|eingetretener|entstandener)\s+Schaden",
            re.I,
        ),
    ),
    (
        "Rügeobliegenheit faelschlich § 160 Abs. 2 zugeordnet",
        re.compile(
            r"^(?![^\n]*§\s*160\s+Abs\.\s*3)[^\n]*"
            r"(?:§\s*160\s+Abs\.\s*2[^\n]{0,120}(?:vorherige\s+Rüge|Rügeobliegenheit|Präklusion)|"
            r"(?:vorherige\s+Rüge|Rügeobliegenheit|Präklusion)[^\n]{0,120}§\s*160\s+Abs\.\s*2)[^\n]*$",
            re.I | re.M,
        ),
    ),
    (
        "§ 97 Abs. 4 GWB faelschlich als Aufspaltungsverbot bezeichnet",
        re.compile(r"Aufspaltungsverbot[^\n]{0,60}§\s*97\s+Abs\.\s*4\s+GWB", re.I),
    ),
    (
        "Schadensersatz faelschlich § 179 GWB zugeordnet",
        re.compile(r"(?:Schadensersatz|Verjährung)[^\n]{0,100}§\s*179\s+GWB", re.I),
    ),
    (
        "§ 126 GWB mit falscher Drei-/Zweijahreskombination",
        re.compile(r"(?:3|drei)\s+Jahre\s+§\s*123|(?:2|zwei)\s+Jahre\s+§\s*124", re.I),
    ),
    (
        "§ 126 GWB mit vertauschten zwingenden und fakultativen Hoechstzeiten",
        re.compile(r"(?:3|drei)\s*\(zwingend\)[^\n]{0,100}(?:5|fünf|fuenf)\s*\(fakultativ\)", re.I),
    ),
    (
        "BZRG-Tilgung pauschal mit vergaberechtlichem Fristablauf gleichgesetzt",
        re.compile(r"Tilgung\s+im\s+BZRG\s+entspricht\s+Ablauf\s+der\s+Ausschlussdauer", re.I),
    ),
    (
        "Fuenfjahresdauer faelschlich § 123 Abs. 3 statt § 126 Nr. 1 zugeordnet",
        re.compile(r"Wirkungsdauer[^\n]{0,100}§\s*123[^\n]{0,160}§\s*123\s+Abs\.\s*3", re.I),
    ),
    (
        "Unterschwellenrechtsschutz pauschal ausgeschlossen",
        re.compile(r"Kein\s+Primärrechtsschutz\s*[—-]\s*nur\s+Aufsicht", re.I),
    ),
    (
        "Erkennbare Bekanntmachungs- oder Unterlagenfehler faelschlich sofort zu ruegen",
        re.compile(r"(?:Bekanntmachung|Vergabeunterlagen)[^\n]{0,100}sofort\s+rügen", re.I),
    ),
    (
        "§ 40 Abs. 1 Satz 2 VgV durch pauschalen Vorrang des Absendedatums uebergangen",
        re.compile(
            r"Für\s+den\s+Fristlauf\s+zählt\s+das\s+Absendedatum,\s+nicht\s+der\s+Tag\s+der\s+(?:TED-)?Veröffentlichung|"
            r"Mindestfristen\s+laufen\s+nicht\s+ab\s+der\s+Veröffentlichung",
            re.I,
        ),
    ),
    (
        "35-Tage-Angebotsfrist faelschlich § 15 Abs. 1 statt Abs. 2 VgV zugeordnet",
        re.compile(
            r"(?:§|Paragraf)\s*15\s+Abs\.?\s*1\s+VgV[^\n]{0,100}"
            r"(?:35\s+Tage|Mindestfrist|Angebotsfrist|Absendung)|"
            r"(?:35\s+Tage|Mindestfrist|Angebotsfrist|Absendung)[^\n]{0,100}"
            r"(?:§|Paragraf)\s*15\s+Abs\.?\s*1\s+VgV",
            re.I,
        ),
    ),
    (
        "§ 135-Antrag als unmittelbare OLG-Feststellungsklage bezeichnet",
        re.compile(r"Feststellungsklage\s+(?:beim|zum)\s+Oberlandesgericht|Unwirksamkeits-?Klage\s+§\s*135", re.I),
    ),
    (
        "altes BSIG als aktuelles Recht verwendet",
        re.compile(r"(?:nach|gemäß|gem\.)\s+§\s*(?:8a|8b|9b)\s+BSIG|§\s*(?:8a|8b|9b)\s+BSIG\s+[—-]", re.I),
    ),
    (
        "NIS2-Umsetzung faelschlich als noch ausstehend bezeichnet",
        re.compile(r"NIS2\s+gilt\s+noch\s+nicht|NIS2UmsuCG\s*\(in\s+Kraft\s+ab\s+2025/2026\)", re.I),
    ),
    (
        "§ 50 VgV faelschlich freiberuflichen Leistungen zugeordnet",
        re.compile(r"(?:Freiberufliche\s+Leistungen\s*\(§\s*50\s+VgV\)|§\s*50\s+VgV\s*\(Freiberufliche\s+Leistungen\)|Paragraf\s+50\s+VgV\s*\(Freiberufliche\s+Leistungen\))", re.I),
    ),
    (
        "§ 168 BGB faelschlich als Grundlage des Zuschlags oder Vertragsschlusses verwendet",
        re.compile(r"(?:§\s*168|Paragraf\s+168)\s+BGB", re.I),
    ),
    (
        "Verbot kuenstlicher Aufteilung faelschlich § 3 Abs. 7 VgV zugeordnet",
        re.compile(r"^(?![^\n]*§\s*3\s+Abs\.?\s*2\s+VgV)[^\n]*(?:(?:künstlich|kuenstlich|Aufspaltungsverbot)[^\n]{0,100}§\s*3\s+Abs\.?\s*7\s+VgV|§\s*3\s+Abs\.?\s*7\s+VgV[^\n]{0,100}(?:künstlich|kuenstlich|Aufspaltungsverbot))[^\n]*$", re.I | re.M),
    ),
    (
        "Markterkundung faelschlich § 5 UVgO zugeordnet",
        re.compile(r"(?:Markterkund|Marktsond)[^\n]{0,100}(?:§|Paragraf)\s*5\s+UVgO|(?:§|Paragraf)\s*5\s+UVgO[^\n]{0,100}(?:Markterkund|Marktsond)", re.I),
    ),
    (
        "Rechnerische Pruefung faelschlich § 16 UVgO zugeordnet",
        re.compile(
            r"(?:rechnerisch|Rechenprüfung|Einheitspreis)[^\n]{0,120}(?:§{1,2}|Paragraf)\s*16\s+UVgO|"
            r"(?:§{1,2}|Paragraf)\s*16\s+UVgO[^\n]{0,120}(?:rechnerisch|Rechenprüfung|Einheitspreis)",
            re.I,
        ),
    ),
    (
        "Offenes Verfahren faelschlich als alleiniger Regelfall nach § 119 Abs. 2 GWB",
        re.compile(r"(?:offene?s?\s+Verfahren[^\n]{0,150}(?:ist\s+der\s+Regelfall|als\s+Regel|vorrangig)|§\s*119\s+Abs\.?\s*2[^\n]{0,140}offene?s?\s+Verfahren[^\n]{0,60}(?:Regelfall|vorrangig))", re.I),
    ),
    (
        "Losgrundsatz nach 2026 ohne § 97a GWB beschrieben",
        re.compile(r"^(?![^\n]*§\s*97a(?:\s+Abs\.?\s*\d+)?\s+GWB)[^\n]*(?:Losgrundsatz|Fach-?\s*und\s*Teillose|Gesamtvergabe)[^\n]*§\s*97\s+Abs\.?\s*4\s+GWB[^\n]*$|^(?![^\n]*§\s*97a(?:\s+Abs\.?\s*\d+)?\s+GWB)[^\n]*§\s*97\s+Abs\.?\s*4\s+GWB[^\n]*(?:Losgrundsatz|Fach-?\s*und\s*Teillose|Gesamtvergabe)[^\n]*$", re.I | re.M),
    ),
    (
        "Losbildung faelschlich § 5 VgV zugeordnet",
        re.compile(r"(?:Losweise|Losbildung|Fachlose|Teillose)[^\n]{0,100}§\s*5\s+VgV|§\s*5\s+VgV[^\n]{0,100}(?:Losweise|Losbildung|Fachlose|Teillose)", re.I),
    ),
    (
        "§ 118 GWB faelschlich Inhouse oder Verteidigung zugeordnet",
        re.compile(r"§\s*118\s+GWB[^\n]{0,120}(?:Inhouse|Verteidigung)|(?:Inhouse|Verteidigung)[^\n]{0,120}§\s*118\s+GWB", re.I),
    ),
    (
        "§ 119 GWB faelschlich wirtschaftlichen Verbindungen zugeordnet",
        re.compile(r"§\s*119\s+GWB[^\n]{0,100}(?:wirtschaftliche|finanzielle)\s+(?:Verbindung|Verflechtung)", re.I),
    ),
    (
        "§ 122 Abs. 2 GWB mit vier Eignungskategorien beschrieben",
        re.compile(r"(?:§\s*122\s+Abs\.?\s*2\s+GWB[^\n]{0,100}vier\s+Eignungskategorien|vier\s+Eignungskategorien[^\n]{0,100}§\s*122\s+Abs\.?\s*2\s+GWB)", re.I),
    ),
    (
        "Mindestumsatz faelschlich § 45 Abs. 4 VgV zugeordnet",
        re.compile(r"(?:Mindest(?:jahres)?umsatz|Zweifache)[^\n]{0,100}§\s*45\s+Abs\.?\s*4\s+VgV|§\s*45\s+Abs\.?\s*4\s+VgV[^\n]{0,100}(?:Mindest(?:jahres)?umsatz|Zweifache)", re.I),
    ),
    (
        "Eingangsbestaetigung faelschlich § 53 Abs. 4 VgV zugeordnet",
        re.compile(r"Eingangsbestätigung\s*\(§\s*53\s+Abs\.?\s*4\s+VgV\)", re.I),
    ),
    (
        "Nicht existente E-Abgabe-Kombination mit § 41 Abs. 1 Nr. 6 VgV",
        re.compile(r"§\s*41\s+Abs\.?\s*1\s+Nr\.?\s*6\s+VgV", re.I),
    ),
    (
        "Aufklaerung faelschlich § 58 Abs. 2 Satz 1 VgV zugeordnet",
        re.compile(r"§\s*58\s+Abs\.?\s*2\s+Satz\s*1\s+VgV[^\n]{0,80}Aufklärung|Aufklärung[^\n]{0,80}§\s*58\s+Abs\.?\s*2\s+Satz\s*1\s+VgV", re.I),
    ),
    (
        "Starre 20-Prozent-Grenze fuer Niedrigpreisaufklaerung behauptet",
        re.compile(r"(?:klassisch|mindestens|Schwelle|Schwellenwert)[^\n]{0,50}20\s*(?:Prozent|%)[^\n]{0,100}(?:§\s*60\s+VgV|Aufklärung|nächstplatziert)|20-Prozent-Schwelle", re.I),
    ),
    (
        "Wettbewerbsregisterpflicht veraltet ab 30.000 EUR angesetzt",
        re.compile(r"(?:Wettbewerbsregister|WRegG)[^\n]{0,100}(?:ab\s*)?30[. ]?000", re.I),
    ),
    (
        "§ 160 Abs. 3 GWB veraltet auf vier Unzulaessigkeitsgruende begrenzt",
        re.compile(r"§\s*160\s+Abs\.?\s*3[^\n]{0,100}(?:vier\s+(?:alternative\s+)?(?:Rügeobliegenheiten|Unzulässigkeits)|Nummern?\s+1\s+bis\s+4\s+getrennt)", re.I),
    ),
    (
        "§ 181 GWB faelschlich Rechtsmissbrauch zugeordnet",
        re.compile(r"§\s*181\s+GWB[^\n]{0,100}Rechtsmissbrauch|Rechtsmissbrauch[^\n]{0,100}§\s*181\s+GWB", re.I),
    ),
    (
        "§ 181 GWB und § 280 BGB faelschlich als kombinierte Anspruchsgrundlage",
        re.compile(r"§\s*181\s+GWB\s+(?:iVm|i\.\s*V\.\s*m\.)\s+§\s*280\s+BGB", re.I),
    ),
    (
        "Gebuehrenvorschuss nach § 182 GWB faelschlich als Antragspflicht",
        re.compile(r"(?:Vorschussgebühr|Gebührenvorschuss)\s*(?:nach\s+)?§\s*182\s+GWB|Vorschussgebühr\s+(?:eingezahlt|zahlen|erforderlich)", re.I),
    ),
    (
        "Dienstleistungsreferenzen pauschal fuer fuenf Jahre verlangt",
        re.compile(r"§\s*46\s+Abs\.?\s*3\s+Nr\.?\s*1\s+VgV[^\n]{0,140}(?:grundsätzlich\s+)?(?:für\s+)?fünf\s+Jahre|Qualifikationsnachweise[^\n]{0,120}fünf\s+Jahre\s+anzuerkennen", re.I),
    ),
    (
        "HOAI-Altvertragsurteil BGH VII ZR 174/19 inhaltlich umgekehrt",
        re.compile(r"VII\s+ZR\s+174/19[^\n]{0,120}(?:nicht\s+zwingend|unverbindlich)", re.I),
    ),
    (
        "§ 132 Abs. 3 GWB faelschlich als Nummer 5 De-minimis dargestellt",
        re.compile(r"Nr\.?\s*5[^\n]{0,40}(?:De-?Minimis|10\s*Prozent|15\s*Prozent)", re.I),
    ),
    (
        "Verstoss gegen § 134 GWB faelschlich automatisch schwebend unwirksam",
        re.compile(r"Zuschlag[^\n]{0,100}schwebend\s+unwirksam", re.I),
    ),
    (
        "C-66/22 mit falschem Fallnamen Toscca",
        re.compile(r"C-66/22[^\n]{0,50}Toscca|Toscca[^\n]{0,50}C-66/22", re.I),
    ),
    (
        "Niedrigpreispruefung faelschlich § 56 statt § 60 VgV zugeordnet",
        re.compile(r"^(?![^\n]*statt\s+§\s*56\s+VgV)[^\n]*(?:§\s*56\s+VgV[^\n]{0,100}(?:ungewöhnlich\s+niedrig|Niedrigpreis|Auskömmlichkeit)|(?:ungewöhnlich\s+niedrig|Niedrigpreis|Auskömmlichkeit)[^\n]{0,100}§\s*56\s+VgV)[^\n]*$", re.I | re.M),
    ),
    (
        "Schweigen der Vergabestelle faelschlich an gesetzliche Zehn-Tage-Folge geknuepft",
        re.compile(r"Schweigen\s+(?:mehr\s+als\s+)?10\s+Kalendertage[^\n]{0,80}Nachprüfungsantrag", re.I),
    ),
    (
        "§ 181 GWB mit BGB-Anspruechen als einheitliche Grundlage verknuepft",
        re.compile(r"§\s*181\s+GWB\s+(?:iVm|i\.\s*V\.\s*m\.)\s+§{1,2}\s*280", re.I),
    ),
    (
        "§ 50 Abs. 2 VgV zu absolut auf Nachweise nur des Zuschlagsempfaengers verkuerzt",
        re.compile(r"Einzelnachweise\s+nur\s+vom\s+(?:voraussichtlichen\s+)?Zuschlagsempfänger", re.I),
    ),
    (
        "§ 122 Abs. 1 und 2 GWB in ihrer Funktion vertauscht",
        re.compile(
            r"§\s*122\s+Abs\.?\s*1\s+GWB[^\n]{0,180}(?:Kriterien\s+zu\s+Befähigung|drei\s+Eignungskategorien)|"
            r"§\s*122\s+Abs\.?\s*2\s+GWB[^\n]{0,180}(?:durch\s+den\s+Auftragsgegenstand\s+gerechtfertigt|in\s+Verbindung\s+mit\s+dem\s+Auftragsgegenstand)",
            re.I,
        ),
    ),
    (
        "§ 47 VgV mit falscher Haftungsregel fuer bauliche oder spezifische Leistungen",
        re.compile(r"(?:baulichen|spezifischen)\s+Leistungen[^\n]{0,80}Haftungs(?:übernahme|pflicht)|Haftungs(?:übernahme|pflicht)[^\n]{0,80}(?:baulichen|spezifischen)\s+Leistungen", re.I),
    ),
    (
        "Mindestumsatzgrenze faelschlich allein § 122 Abs. 4 GWB zugeordnet",
        re.compile(r"§\s*122\s+Abs\.?\s*4\s+GWB[^\n]{0,100}Mindestjahresumsatz[^\n]{0,100}(?:Zweifachen|zweifach)", re.I),
    ),
    (
        "§ 56 Abs. 3 VgV zu absolut auf alle leistungsbezogenen Unterlagen erstreckt",
        re.compile(r"Keine\s+Nachforderung\s+leistungsbezogener\s+(?:Erklärungen|Unterlagen)", re.I),
    ),
    (
        "EEE fuer Eignungsleiher trotz C-812/24 ausnahmslos verlangt",
        re.compile(r"(?:Bei\s+Eignungsleihe\s+)?Drittunternehmen\s+(?:ebenfalls\s+)?ESPD|ESPD\s+des\s+Drittunternehmens", re.I),
    ),
    (
        "Nichterfuellte Eignung faelschlich § 57 Abs. 1 Nr. 1 VgV zugeordnet",
        re.compile(r"§\s*57\s+Abs\.?\s*1\s+Nr\.?\s*1\s+VgV[^\n]{0,120}(?:Eignungskriter|§\s*122\s+GWB)|(?:Eignungskriter|§\s*122\s+GWB)[^\n]{0,120}§\s*57\s+Abs\.?\s*1\s+Nr\.?\s*1\s+VgV", re.I),
    ),
    (
        "§ 181 GWB faelschlich von subjektivem Vertrauen abhaengig gemacht",
        re.compile(r"§\s*181\s+GWB[^\n]{0,140}(?:bei|setzt)\s+Vertrauen\s+auf\s+(?:die\s+)?Einhaltung", re.I),
    ),
    (
        "BGH X ZB 15/13 ausserhalb seines Hauptthemas als Standardanker verwendet",
        re.compile(
            r"(?:X\s+ZB\s+15/13[^\n]{0,160}(?:objektive\s+Auslegung|Empfängerhorizont)|"
            r"(?:objektive\s+Auslegung|Empfängerhorizont)[^\n]{0,160}X\s+ZB\s+15/13)",
            re.I,
        ),
    ),
    (
        "heutige Inhouse-80-Prozent-Quote faelschlich Carbotermo zugeschrieben",
        re.compile(
            r"(?:mindestens|mehr\s+als)\s+80\s*(?:Prozent|%)[^\n]{0,120}"
            r"\(\s*(?:EuGH\s+)?C-340/04\s+Carbotermo\s*\)",
            re.I,
        ),
    ),
    (
        "heutige Kooperations-20-Prozent-Grenze faelschlich Hamburg-Stadtreinigung zugeschrieben",
        re.compile(
            r"weniger\s+als\s+20\s*(?:Prozent|%)[^\n]{0,140}"
            r"\(\s*(?:EuGH\s+)?C-480/06\s+Hamburg-Stadtreinigung\s*\)",
            re.I,
        ),
    ),
    (
        "Mara faelschlich als Punktebruecke oder eigenstaendiger Billigzuschlagsanker verwendet",
        re.compile(
            r"Mara\s+C-769/23\s+führt\s+die\s+Punktebrücke|"
            r"Mara\s+C-769/23[^\n]{0,80}trägt[^\n]{0,40}Billigzuschlag|"
            r"Mara[^\n]{0,160}darf\s+die\s+Vergabe[^\n]{0,80}Qualität\s+nicht",
            re.I,
        ),
    ),
    (
        "140000-EUR-Schwelle nach neuem § 106 GWB pauschal dem Bund oder Bundesbehoerden zugeordnet",
        re.compile(
            r"^(?![^\n]*(?:Bundeskanzleramt|Bundesministerien))[^\n]*(?:Bund|Bundesbehörden|Bundesbehoerden)[^\n]{0,100}(?:140000|140\.000)|"
            r"^(?![^\n]*(?:Bundeskanzleramt|Bundesministerien))[^\n]*(?:140000|140\.000)[^\n]{0,100}(?:Bund|Bundesbehörden|Bundesbehoerden)[^\n]*$",
            re.I | re.M,
        ),
    ),
    (
        "aktuelle Leistungsbeschreibung mit veraltetem Erschoepfend-Merkmal beschrieben",
        # § 121 GWB wurde geändert; § 7 und § 7 EU VOB/A verwenden das Merkmal weiterhin.
        re.compile(
            r"(?:§|Paragraf)\s*121(?:\s*(?:Abs\.?|Absatz)\s*1)?(?:\s*GWB)?"
            r"[^\n]{0,160}erschöpfend|"
            r"erschöpfend[^\n]{0,160}(?:§|Paragraf)\s*121(?:\s*GWB)?",
            re.I,
        ),
    ),
    (
        "EEE faelschlich als allgemeines Pflichtformat behandelt",
        re.compile(
            r"(?:EEE|Einheitliche\s+Europäische\s+Eigenerklärung)[^\n]{0,80}als\s+Pflichtformat|"
            r"Pflichtformat[^\n]{0,80}(?:EEE|Einheitliche\s+Europäische\s+Eigenerklärung)",
            re.I,
        ),
    ),
    (
        "§ 56 VgV faelschlich mit pauschaler Fuenf-Tage-Nachforderungsfrist verbunden",
        re.compile(
            r"(?:§\s*56\s+VgV|Nachforder(?:ung|ungsfrist))[^\n]{0,120}(?:regelhaft|standardmäßig|stets)\s+(?:fünf|5)\s+(?:Kalender)?tage|"
            r"(?:fünf|5)\s+(?:Kalender)?tage[^\n]{0,120}§\s*56\s+VgV",
            re.I,
        ),
    ),
    (
        "§ 167 GWB mit alter Soll-Frist oder ueberlanger Verlaengerung beschrieben",
        re.compile(
            r"Entscheidung\s+soll\s+(?:binnen|innerhalb)\s+fünf\s+Wochen|"
            r"5-Wochen-Regel:\s*Entscheidung\s+soll|"
            r"§\s*167[^\n]{0,180}mehrere\s+Wochen\s+überschreiten",
            re.I,
        ),
    ),
    (
        "§ 60 Abs. 3 VgV auf automatischen Ausschluss nach jeder mangelhaften Aufklaerung verkuerzt",
        re.compile(r"Bei\s+mangelhafter\s+Aufklärung\s+Ausschluss", re.I),
    ),
    (
        "Quotenberechnung nach aktuellem § 108 GWB faelschlich Absatz 7 zugeordnet",
        re.compile(
            r"^(?![^\n]*§\s*108\s+Abs\.?\s*8\s+GWB)[^\n]*"
            r"(?:(?:Berechnung|Bezugszeitraum|Tätigkeitsindikator|20-Prozent-Grenze|80-Prozent-Quote)[^\n]{0,140}"
            r"§\s*108\s+Abs\.?\s*7\s+GWB|"
            r"§\s*108\s+Abs\.?\s*7\s+GWB[^\n]{0,140}(?:Berechnung|Bezugszeitraum|Tätigkeitsindikator|Quote|Grenze))",
            re.I | re.M,
        ),
    ),
    (
        "Form- oder Fristverstoss pauschal ohne § 57-Ausnahme als Zwangsausschluss behandelt",
        re.compile(
            r"Nachgereichte\s+oder\s+verspätete\s+Angebote\s*:\s*zwingender\s+Ausschluss|"
            r"Verspätete\s+Angebote\s+nicht\s+zu\s+berücksichtigen",
            re.I,
        ),
    ),
    (
        "Losverzicht nach neuem § 97a GWB ohne Infrastruktur-Zeitroute verkuerzt",
        re.compile(r"Zulässig\s+nur,\s+wenn\s+wirtschaftliche\s+oder\s+technische\s+Gründe\s+dies\s+erfordern", re.I),
    ),
    (
        "Schleswig-Holstein mit dem vor dem 16. Mai 2026 geltenden Wertgrenzenstand beschrieben",
        re.compile(r"Schleswig-Holstein[^\n]*Keine\s+aktuelle\s+landesspezifische\s+Erhöhung", re.I),
    ),
    (
        "Thüringer Liefer- und Dienstleistungsgrenze statisch mit dem alten EU-Wert 221000 Euro angegeben",
        re.compile(r"(?:Thüringen|Thueringen)[^\n]*221[. ]?000\s+Euro", re.I),
    ),
    (
        "geltender Bundes-Direktauftrag nur als kuenftiger Reformanker behandelt",
        re.compile(
            r"Direktauftrag\s+Bund:\s+ab\s+Inkrafttreten\s+als\s+Reformanker|"
            r"Ab\s+2026-07-01\s+Reformtext\s+prüfen",
            re.I,
        ),
    ),
    (
        "C-268/25 faelschlich als EuGH-Urteil statt als Schlussantraege bezeichnet",
        re.compile(
            r"EuGH(?:,)?\s+Urteil[^\n]{0,120}C-268/25|"
            r"C-268/25[^\n]{0,120}EuGH(?:,)?\s+Urteil",
            re.I,
        ),
    ),
    (
        "geltendes Bundestariftreuegesetz faelschlich als kuenftiges Gesetz behandelt",
        re.compile(
            r"Bundestariftreuegesetz[^\n]{0,120}(?:soll\s+(?:gelten|in Kraft treten)|noch\s+nicht\s+in\s+Kraft|künftig\s+in\s+Kraft)|"
            r"(?:künftig|zukünftig)[^\n]{0,80}Bundestariftreuegesetz",
            re.I,
        ),
    ),
    (
        "Bundestariftreuegesetz faelschlich auf reine Lieferauftraege erstreckt",
        re.compile(
            r"BTTG[^\n]{0,120}(?:Bau-,?\s*Liefer-\s*und\s*Dienstleistungsaufträge|Lieferaufträge[^\n]{0,50}(?:erfasst|gilt))|"
            r"Bundestariftreuegesetz[^\n]{0,120}(?:Bau-,?\s*Liefer-\s*und\s*Dienstleistungsaufträge|Lieferaufträge[^\n]{0,50}(?:erfasst|gilt))",
            re.I,
        ),
    ),
    (
        "§ 14 BTTG ohne unanfechtbare Feststellung als Ausschlussautomatismus behandelt",
        re.compile(
            r"(?:§\s*14\s+BTTG|Bundestariftreuegesetz)[^\n]{0,120}(?:automatischer|zwingender)\s+Ausschluss|"
            r"(?:Tariftreueverstoß|BTTG-Verstoß)[^\n]{0,120}(?:automatisch|zwingend)\s+aus(?:schließen|geschlossen)",
            re.I,
        ),
    ),
    (
        "C-590/24 faelschlich als Entscheidung ueber Vergabeausschluss verwendet",
        re.compile(
            r"C-590/24[^\n]{0,180}(?:entschied|bestätigt|verbietet|untersagt|erlaubt)"
            r"[^\n]{0,100}(?:automatischen?\s+)?(?:Vergabe)?ausschluss",
            re.I,
        ),
    ),
    (
        "C-186/25 faelschlich als allgemeiner Rueckforderungs- oder §-132-Automatismus verwendet",
        re.compile(
            r"C-186/25[^\n]{0,180}(?:begründet|schafft|gilt\s+als|liefert)"
            r"[^\n]{0,100}(?:allgemein(?:e|en|er)|automatisch(?:e|en|er))"
            r"[^\n]{0,80}(?:Rückforderung|Finanzkorrektur|§\s*132)",
            re.I,
        ),
    ),
    (
        "C-810/24 faelschlich als allgemeines Verbot privater Initiativen verwendet",
        re.compile(
            r"C-810/24[^\n]{0,180}(?:verbietet|untersagt)\s+"
            r"(?:jede|alle|generell|allgemein)[^\n]{0,100}"
            r"(?:Markterkundung|private(?:n|r|s)?\s+(?:Initiative|Projektvorschlag)|Kostenerstattung)",
            re.I,
        ),
    ),
    (
        "nicht vorhandener § 15 Abs. 7 BwBBG mit erfundenem Inhalt belegt",
        re.compile(
            r"§\s*15\s+Abs\.?\s*7\s+BwBBG[^\n]{0,50}"
            r"(?:regelt|bestimmt|erlaubt|verlangt|sieht\s+vor|gewährt)",
            re.I,
        ),
    ),
    (
        "operatives Bundeswehrbeschaffungsbeschleunigungsgesetz faelschlich als BwPBBG abgekuerzt",
        re.compile(
            r"Bundeswehrbeschaffungsbeschleunigungsgesetz\s*(?:-|–|\()\s*BwPBBG",
            re.I,
        ),
    ),
)

# Jeder Hinweis ist ein zwingend im Treffer vorkommendes Literal. Dadurch
# werden die komplexen Muster nur auf thematisch mögliche Dateien angewandt.
# Die Mengenprüfung verhindert, dass neue Regeln ohne sicheren Hinweis laufen.
RULE_PREFILTERS: dict[str, tuple[str, ...]] = {
    "Schwellenwert-VO 2025/2150 faelschlich klassischen Vergaben zugeordnet": ("2025/2150",),
    "Schwellenwert-VO 2025/2151 faelschlich Sektorenvergaben zugeordnet": ("2025/2151",),
    "Schwellenwert-VO 2025/2152 faelschlich Konzessionen zugeordnet": ("2025/2152",),
    "Sof Medica faelschlich als Pflicht zur vollstaendigen Vorabveroeffentlichung der Begruendung dargestellt": ("sof medica", "c-568/24"),
    "AESTE C-210/24 mit falschem Urteilsdatum zitiert": ("c-210/24",),
    "AESTE C-210/24 mit falschem ECLI zitiert": ("c-210/24",),
    "SektVO-Zuschlagskriterien faelschlich § 31 statt § 52 zugeordnet": ("sektvo",),
    "KonzVgV-Zuschlagskriterien faelschlich § 16 statt § 31 zugeordnet": ("konzvgv",),
    "§ 135 GWB unzulaessig auf 30 Tage ab blosser Kenntnis verkuerzt": ("135",),
    "§ 135 GWB durch mehrdeutige Kenntnis-/Frist-Kurzformel verkuerzt": ("135",),
    "BTTG-Verordnungsstatus mit schnell veraltendem Tagesstand festgeschrieben": ("14. juli 2026",),
    "erfundene Gebuehrentabelle zu § 182 GWB": ("182",),
    "OLG-Streitwert mit Nettoauftragswert oder Kammermindestgebuehr verwechselt": ("streitwert",),
    "§ 160 Abs. 3 Nr. 2 oder 3 faelschlich an Kenntnis geknuepft": ("160",),
    "§ 160 Abs. 3 Nr. 2 oder 3 faelschlich als Unverzueglichkeitsfrist behandelt": ("160",),
    "§ 160 Abs. 3 Nr. 2 faelschlich einem Unterlagenverstoß zugeordnet": ("160",),
    "§ 160 Abs. 3 Nr. 3 faelschlich einem Bekanntmachungsverstoß zugeordnet": ("160",),
    "Rügefrist faelschlich in Werktagen oder als Unverzueglichkeit bezeichnet": ("werktag",),
    "Rüge faelschlich von qualifizierter Signatur abhaengig gemacht": ("qes", "qualifiziert"),
    "Antragsbefugnis der falschen Vorschrift zugeordnet": ("antragsbefugnis",),
    "Schadensmerkmal der Antragsbefugnis faelschlich § 160 Abs. 1 zugeordnet": ("schaden",),
    "Rügeobliegenheit faelschlich § 160 Abs. 2 zugeordnet": ("160",),
    "§ 97 Abs. 4 GWB faelschlich als Aufspaltungsverbot bezeichnet": ("aufspaltungsverbot",),
    "Schadensersatz faelschlich § 179 GWB zugeordnet": ("179",),
    "§ 126 GWB mit falscher Drei-/Zweijahreskombination": ("jahre",),
    "§ 126 GWB mit vertauschten zwingenden und fakultativen Hoechstzeiten": ("zwingend",),
    "BZRG-Tilgung pauschal mit vergaberechtlichem Fristablauf gleichgesetzt": ("bzrg",),
    "Fuenfjahresdauer faelschlich § 123 Abs. 3 statt § 126 Nr. 1 zugeordnet": ("wirkungsdauer",),
    "Unterschwellenrechtsschutz pauschal ausgeschlossen": ("primärrechtsschutz",),
    "Erkennbare Bekanntmachungs- oder Unterlagenfehler faelschlich sofort zu ruegen": ("sofort",),
    "§ 40 Abs. 1 Satz 2 VgV durch pauschalen Vorrang des Absendedatums uebergangen": ("veröffentlichung",),
    "35-Tage-Angebotsfrist faelschlich § 15 Abs. 1 statt Abs. 2 VgV zugeordnet": ("35",),
    "§ 135-Antrag als unmittelbare OLG-Feststellungsklage bezeichnet": ("feststellungsklage", "unwirksamkeits"),
    "altes BSIG als aktuelles Recht verwendet": ("bsig",),
    "NIS2-Umsetzung faelschlich als noch ausstehend bezeichnet": ("nis2",),
    "§ 50 VgV faelschlich freiberuflichen Leistungen zugeordnet": ("50",),
    "§ 168 BGB faelschlich als Grundlage des Zuschlags oder Vertragsschlusses verwendet": ("168",),
    "Verbot kuenstlicher Aufteilung faelschlich § 3 Abs. 7 VgV zugeordnet": ("künstlich", "kuenstlich", "aufspaltungsverbot"),
    "Markterkundung faelschlich § 5 UVgO zugeordnet": ("markterkund", "marktsond"),
    "Rechnerische Pruefung faelschlich § 16 UVgO zugeordnet": ("uvgo",),
    "Offenes Verfahren faelschlich als alleiniger Regelfall nach § 119 Abs. 2 GWB": ("offene verfahren", "offenes verfahren"),
    "Losgrundsatz nach 2026 ohne § 97a GWB beschrieben": ("97",),
    "Losbildung faelschlich § 5 VgV zugeordnet": ("losweise", "losbildung", "fachlose", "teillose"),
    "§ 118 GWB faelschlich Inhouse oder Verteidigung zugeordnet": ("118",),
    "§ 119 GWB faelschlich wirtschaftlichen Verbindungen zugeordnet": ("119",),
    "§ 122 Abs. 2 GWB mit vier Eignungskategorien beschrieben": ("122",),
    "Mindestumsatz faelschlich § 45 Abs. 4 VgV zugeordnet": ("mindestumsatz", "mindestjahresumsatz"),
    "Eingangsbestaetigung faelschlich § 53 Abs. 4 VgV zugeordnet": ("eingangsbestätigung",),
    "Nicht existente E-Abgabe-Kombination mit § 41 Abs. 1 Nr. 6 VgV": ("41",),
    "Aufklaerung faelschlich § 58 Abs. 2 Satz 1 VgV zugeordnet": ("aufklärung",),
    "Starre 20-Prozent-Grenze fuer Niedrigpreisaufklaerung behauptet": ("20",),
    "Wettbewerbsregisterpflicht veraltet ab 30.000 EUR angesetzt": ("wettbewerbsregister", "wregg"),
    "§ 160 Abs. 3 GWB veraltet auf vier Unzulaessigkeitsgruende begrenzt": ("160",),
    "§ 181 GWB faelschlich Rechtsmissbrauch zugeordnet": ("181",),
    "§ 181 GWB und § 280 BGB faelschlich als kombinierte Anspruchsgrundlage": ("181",),
    "Gebuehrenvorschuss nach § 182 GWB faelschlich als Antragspflicht": ("vorschussgebühr", "gebührenvorschuss"),
    "Dienstleistungsreferenzen pauschal fuer fuenf Jahre verlangt": ("fünf jahre",),
    "HOAI-Altvertragsurteil BGH VII ZR 174/19 inhaltlich umgekehrt": ("vii zr 174/19",),
    "§ 132 Abs. 3 GWB faelschlich als Nummer 5 De-minimis dargestellt": ("132",),
    "Verstoss gegen § 134 GWB faelschlich automatisch schwebend unwirksam": ("schwebend",),
    "C-66/22 mit falschem Fallnamen Toscca": ("c-66/22",),
    "Niedrigpreispruefung faelschlich § 56 statt § 60 VgV zugeordnet": ("niedrigpreis", "auskömmlichkeit", "ungewöhnlich niedrig"),
    "Schweigen der Vergabestelle faelschlich an gesetzliche Zehn-Tage-Folge geknuepft": ("schweigen",),
    "§ 181 GWB mit BGB-Anspruechen als einheitliche Grundlage verknuepft": ("181",),
    "§ 50 Abs. 2 VgV zu absolut auf Nachweise nur des Zuschlagsempfaengers verkuerzt": ("einzelnachweise",),
    "§ 122 Abs. 1 und 2 GWB in ihrer Funktion vertauscht": ("122",),
    "§ 47 VgV mit falscher Haftungsregel fuer bauliche oder spezifische Leistungen": ("haftung",),
    "Mindestumsatzgrenze faelschlich allein § 122 Abs. 4 GWB zugeordnet": ("mindestjahresumsatz",),
    "§ 56 Abs. 3 VgV zu absolut auf alle leistungsbezogenen Unterlagen erstreckt": ("nachforderung",),
    "EEE fuer Eignungsleiher trotz C-812/24 ausnahmslos verlangt": ("espd", "drittunternehmen"),
    "Nichterfuellte Eignung faelschlich § 57 Abs. 1 Nr. 1 VgV zugeordnet": ("57",),
    "§ 181 GWB faelschlich von subjektivem Vertrauen abhaengig gemacht": ("vertrauen",),
    "BGH X ZB 15/13 ausserhalb seines Hauptthemas als Standardanker verwendet": ("x zb 15/13",),
    "heutige Inhouse-80-Prozent-Quote faelschlich Carbotermo zugeschrieben": ("carbotermo",),
    "heutige Kooperations-20-Prozent-Grenze faelschlich Hamburg-Stadtreinigung zugeschrieben": ("hamburg-stadtreinigung",),
    "Mara faelschlich als Punktebruecke oder eigenstaendiger Billigzuschlagsanker verwendet": ("mara",),
    "140000-EUR-Schwelle nach neuem § 106 GWB pauschal dem Bund oder Bundesbehoerden zugeordnet": ("140000", "140.000"),
    "aktuelle Leistungsbeschreibung mit veraltetem Erschoepfend-Merkmal beschrieben": ("erschöpfend",),
    "EEE faelschlich als allgemeines Pflichtformat behandelt": ("eee", "einheitliche europäische eigenerklärung"),
    "§ 56 VgV faelschlich mit pauschaler Fuenf-Tage-Nachforderungsfrist verbunden": ("tage",),
    "§ 167 GWB mit alter Soll-Frist oder ueberlanger Verlaengerung beschrieben": ("entscheidung soll", "5-wochen-regel", "167"),
    "§ 60 Abs. 3 VgV auf automatischen Ausschluss nach jeder mangelhaften Aufklaerung verkuerzt": ("mangelhafter",),
    "Quotenberechnung nach aktuellem § 108 GWB faelschlich Absatz 7 zugeordnet": ("108",),
    "Form- oder Fristverstoss pauschal ohne § 57-Ausnahme als Zwangsausschluss behandelt": ("verspätete angebote", "nachgereichte oder verspätete angebote"),
    "Losverzicht nach neuem § 97a GWB ohne Infrastruktur-Zeitroute verkuerzt": ("zulässig nur",),
    "Schleswig-Holstein mit dem vor dem 16. Mai 2026 geltenden Wertgrenzenstand beschrieben": ("schleswig-holstein",),
    "Thüringer Liefer- und Dienstleistungsgrenze statisch mit dem alten EU-Wert 221000 Euro angegeben": ("221000", "221.000"),
    "geltender Bundes-Direktauftrag nur als kuenftiger Reformanker behandelt": ("direktauftrag",),
    "C-268/25 faelschlich als EuGH-Urteil statt als Schlussantraege bezeichnet": ("c-268/25",),
    "geltendes Bundestariftreuegesetz faelschlich als kuenftiges Gesetz behandelt": ("bundestariftreuegesetz",),
    "Bundestariftreuegesetz faelschlich auf reine Lieferauftraege erstreckt": ("bttg", "bundestariftreuegesetz"),
    "§ 14 BTTG ohne unanfechtbare Feststellung als Ausschlussautomatismus behandelt": ("bttg", "bundestariftreuegesetz"),
    "C-590/24 faelschlich als Entscheidung ueber Vergabeausschluss verwendet": ("c-590/24",),
    "C-186/25 faelschlich als allgemeiner Rueckforderungs- oder §-132-Automatismus verwendet": ("c-186/25",),
    "C-810/24 faelschlich als allgemeines Verbot privater Initiativen verwendet": ("c-810/24",),
    "nicht vorhandener § 15 Abs. 7 BwBBG mit erfundenem Inhalt belegt": ("15 abs. 7 bwbbg",),
    "operatives Bundeswehrbeschaffungsbeschleunigungsgesetz faelschlich als BwPBBG abgekuerzt": ("bundeswehrbeschaffungsbeschleunigungsgesetz", "bwpbbg"),
}

if set(RULE_PREFILTERS) != {label for label, _ in RULES}:
    raise RuntimeError("Rechtsregressions-Regeln und sichere Vorfilter sind nicht synchron")


def main() -> int:
    errors: list[str] = []
    files = legal_text_files()
    binary_files = binary_legal_files(ROOT, SKIP_PARTS)
    contents: dict[Path, str] = {
        path: path.read_text(encoding="utf-8", errors="ignore") for path in files
    }
    for path in binary_files:
        try:
            contents[path] = read_binary_legal_text(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: Binärartefakt nicht lesbar: {exc}")

    for path, text in contents.items():
        casefolded_text = text.casefold()
        for label, pattern in RULES:
            if not any(hint in casefolded_text for hint in RULE_PREFILTERS[label]):
                continue
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: {label}")

        upper_text = text.upper()
        for case_number, (expected_date, expected_ecli) in EUGH_JUDGMENT_METADATA.items():
            if case_number.upper() not in upper_text:
                continue
            dated_citation, ecli_citation = EUGH_CITATION_PATTERNS[case_number]
            for match in dated_citation.finditer(text):
                if match.group("date") != expected_date:
                    line = text.count("\n", 0, match.start()) + 1
                    errors.append(
                        f"{path.relative_to(ROOT)}:{line}: {case_number} mit falschem "
                        f"Urteilsdatum {match.group('date')} statt {expected_date}"
                    )

            for match in ecli_citation.finditer(text):
                if match.group("ecli").upper() != expected_ecli:
                    line = text.count("\n", 0, match.start()) + 1
                    errors.append(
                        f"{path.relative_to(ROOT)}:{line}: {case_number} mit falschem "
                        f"ECLI {match.group('ecli')} statt {expected_ecli}"
                    )

    for path, markers in REQUIRED_CURRENT_LAW.items():
        if not path.is_file():
            errors.append(f"{path.relative_to(ROOT)}: Pflichtdatei fehlt")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in markers:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)}: aktueller Normanker fehlt: {marker}")

    for path in REQUIRED_THRESHOLD_SOURCES:
        if not path.is_file():
            errors.append(f"{path.relative_to(ROOT)}: Pflichtdatei für Schwellenwertquellen fehlt")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in REQUIRED_THRESHOLD_MARKERS:
            if marker not in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: Schwellenwertquelle 2026/2027 fehlt: {marker}"
                )

    nr5_pattern = re.compile(r"§\s*160\s+Abs\.?\s*3\s+(?:Satz\s*1\s+)?Nr\.?\s*5\s+GWB", re.I)
    transition_pattern = re.compile(r"§\s*187\s+Abs\.?\s*2\s+GWB", re.I)
    for path, text in contents.items():
        if nr5_pattern.search(text) and not transition_pattern.search(text):
            errors.append(
                f"{path.relative_to(ROOT)}: § 160 Abs. 3 Satz 1 Nr. 5 GWB ohne Übergangsweiche des § 187 Abs. 2 GWB"
            )

    forbidden_schwerin = {
        "Vergabekammer des Bundes": "falsche Bundeszustaendigkeit",
        "OLG Düsseldorf": "falsches Beschwerdegericht",
        "Oberlandesgericht Düsseldorf": "falsches Beschwerdegericht",
        "VK 1-32/26": "falsches Bundesaktenzeichen",
        "vk@bundeskartellamt.de": "falsche Bundesgeschäftsstelle",
        "09_nachpruefungsantrag_vk_bund.md": "veralteter Dateiname",
        "17_beschluss_vk_bund.md": "veralteter Dateiname",
        "18_sofortige_beschwerde_olg_duesseldorf.md": "veralteter Dateiname",
        "20_de_facto_vergabe_klage.md": "falscher Rechtsweg im Dateinamen",
    }
    schwerin_contents = {
        path: text
        for path, text in contents.items()
        if SCHWERIN in path.parents
    }
    for path, text in schwerin_contents.items():
        for needle, label in forbidden_schwerin.items():
            if needle in text:
                line = text[: text.index(needle)].count("\n") + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: {label}: {needle}")

    required_schwerin = (
        "09_nachpruefungsantrag_vk_mv.md",
        "17_beschluss_vk_mv.md",
        "18_sofortige_beschwerde_olg_rostock.md",
        "20_de_facto_vergabe_nachpruefungsantrag.md",
    )
    for name in required_schwerin:
        if not (SCHWERIN / name).is_file():
            errors.append(f"{SCHWERIN.relative_to(ROOT)}: Pflichtdatei fehlt: {name}")

    if errors:
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        print(f"validate-legal-regressions: {len(errors)} Fehler", file=sys.stderr)
        return 1
    print(
        "validate-legal-regressions OK "
        f"({len(files)} Textdateien, {len(binary_files)} Binärartefakte)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
