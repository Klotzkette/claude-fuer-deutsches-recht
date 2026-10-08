#!/usr/bin/env python3
"""Sichert zentrale Rechtsstandsanker des Vergaberechtsschutzes ab."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from legal_artifact_text import binary_legal_files, read_binary_legal_text


ROOT = Path(__file__).resolve().parents[1]
LEGAL_TEXT_SUFFIXES = {".md", ".eml", ".txt", ".csv", ".xml", ".json", ".html"}

COMPLAINT_FILES = (
    "bieter-unternehmen/skills/25-sofortige-beschwerde-olg-paragraf-171/SKILL.md",
    "bieter-unternehmen/skills/olg-sofortige-beschwerde/SKILL.md",
    "bieter-unternehmen/skills/vertiefung-olg-sofortige-beschwerde/SKILL.md",
    "vergabestelle-behoerden/skills/24-vorlage-an-den-vergabesenat/SKILL.md",
    "konkurrenten-rechtsschutz/skills/sofortige-beschwerde-olg-vergabesenat/SKILL.md",
)

PROTECTION_FILES = (
    "bieter-unternehmen/skills/nachpruefungsantrag-vk/SKILL.md",
    "bieter-unternehmen/skills/nachpruefungsverfahren-vk/SKILL.md",
    "bieter-unternehmen/skills/zuschlagsverbot-paragraf-169-gwb/SKILL.md",
    "bieter-unternehmen/skills/24-eilantrag-zuschlagssperre-paragraf-169/SKILL.md",
    "bieter-unternehmen/skills/vergabe-nachpruefung-aussicht/SKILL.md",
    "konkurrenten-rechtsschutz/skills/eilantrag-zuschlagssperre-169/SKILL.md",
)

FORBIDDEN_CASES = {
    "C-521/18": "betrifft Postsektortätigkeiten und darf hier nicht als De-facto-Anker erscheinen",
    "C-376/21": "betrifft das Verhandlungsverfahren nach erfolglosem Wettbewerb und war fehlzugeordnet",
    "C-66/20": "betrifft die Europäische Ermittlungsanordnung und ist kein Vergaberechtsanker",
    "C-465/15": "betrifft Energiesteuer und ist kein Referenzlisten-Anker",
    "C-292/15": "betrifft öffentlichen Personenverkehr und ist kein Unterschwellen-Transparenzanker",
    "C-218/11": "betrifft wirtschaftliche und finanzielle Leistungsfähigkeit und ist kein Referenzvolumen-Anker",
    "C-264/03": "betrifft den Zugang zu Projektsteuerungsaufträgen und ist kein Standortkriterium-Anker",
    "C-388/12": "betrifft Strukturfonds und ist kein Leitfall für die Übertragung des Betriebsrisikos",
    "VK 2-19/22": "amtliche Fundstelle und behauptete Aussage konnten nicht verifiziert werden",
    "VK 2-89/21": "amtliche Fundstelle und behauptete Referenz-Prozentregel konnten nicht verifiziert werden",
    "Z3-3-3194-1-46-11/23": "amtliche Fundstelle und behauptete Aussage konnten nicht verifiziert werden",
}

FORBIDDEN_PATTERNS = {
    r"Zuschlagsverbot ab Eingang (?:des )?Nachprüfungsantrags": (
        "§ 169 Abs. 1 GWB knüpft an die VK-Unterrichtung des Auftraggebers an"
    ),
    r"aufschiebende Wirkung entsteht erst mit Eingang des Nachprüfungsantrags": (
        "§ 169 Abs. 1 GWB knüpft an die VK-Unterrichtung des Auftraggebers an"
    ),
    r"Mit Zustellung des Nachprüfungsantrags an den Auftraggeber tritt": (
        "die aktuelle Norm nennt die Unterrichtung durch Vorsitz oder hauptamtlichen Beisitzer"
    ),
    r"§ 134 VgV": "der Vergabevermerk folgt § 8 VgV; § 134 VgV existiert nicht",
    r"§ 158 Abs\. 3 GWB \(Vergleich": "§ 158 GWB ist keine Vergleichsgrundlage",
    r"§ 168 GWB[^\n]{0,30}Akteneinsicht": "Akteneinsicht richtet sich nach § 165 GWB",
    r"§ 163 GWB[^\n]{0,45}Akteneinsicht": "Untersuchungsgrundsatz und Akteneinsicht trennen",
    r"§ 179 GWB[^\n]{0,20}Schadensersatz": (
        "§ 179 GWB regelt Bindungswirkung und Vorlage, nicht die Anspruchsgrundlage"
    ),
    r"(?:C-14/17[^\n]{0,80}(?:ESPD|EEE)|(?:ESPD|EEE)[^\n]{0,80}C-14/17)": (
        "C-14/17 VAR betrifft technische Spezifikationen und Nachweiszeitpunkt, nicht die EEE"
    ),
    r"VII-?Verg 17/16[^\n]{0,80}(?:Heilung|Form|Signatur|Aufklärung)": (
        "VII-Verg 17/16 betrifft eine ÖPNV-Direktvergabe"
    ),
    r"VII-?Verg 26/17[^\n]{0,80}(?:Preisangab|Preisblatt|Leistungsverzeichnis)": (
        "VII-Verg 26/17 betrifft eine ÖPNV-Direktvergabe"
    ),
    r"VII-?Verg 28/17[^\n]{0,80}(?:Mindestumsatz|Umsatz|Eignungsleihe)": (
        "VII-Verg 28/17 betrifft Auftraggebereigenschaft und De-facto-Vergabe"
    ),
    r"VII-?Verg 19/17[^\n]{0,80}(?:Nichtabhilfe|Erwiderung)": (
        "VII-Verg 19/17 ist kein Nichtabhilfe-Anker"
    ),
    r"VII-?Verg 24/12[^\n]{0,80}Markterkund": (
        "VII-Verg 24/12 ist kein Markterkundungs-Anker"
    ),
    r"Verg 12/20[^\n]{0,100}(?:Referenz|30[^\n]{0,10}50\s*(?:%|Prozent))": (
        "Verg 12/20 trägt keine allgemeine Referenzwert-Prozentgrenze"
    ),
    r"C-561/12[^\n]{0,80}Mindestanforderungen": (
        "Nordecon betrifft Änderungen zwingender Anforderungen im Verhandlungsverfahren; Mindestanforderungsanker ist C-421/01"
    ),
    r"C-19/00[^\n]{0,80}(?:Auftragswert|Schätzgrundlage|Schätzung)": (
        "SIAC Construction betrifft Zuschlagswertung, nicht Auftragswertschätzung"
    ),
    r"C-19/13[^\n]{0,60}(?:zu|als)\s+De-?fakto-?Vergabe": (
        "C-19/13 betrifft die Unwirksamkeitsausnahme bei freiwilliger Ex-ante-Transparenz"
    ),
    r"EuGH-Linie\s+zu\s+Selbstreinigung[^\n]{0,120}C-41/18": (
        "C-41/18 Meca betrifft die vorgelagerte Zuverlässigkeitsprüfung, nicht primär Selbstreinigung"
    ),
}

ESPD_FILES = (
    "bieter-unternehmen/skills/05-espd-ausfuellen/SKILL.md",
    "vergabestelle-behoerden/skills/09-eignungsformular-espd/SKILL.md",
)

NET_ZERO_FILES = (
    "vergabestelle-behoerden/skills/netto-null-technologien-vergabe/SKILL.md",
    "bieter-unternehmen/skills/netto-null-technologien-vergabe/SKILL.md",
    "konkurrenten-rechtsschutz/skills/netto-null-technologien-vergabe/SKILL.md",
)

PUBLIC_TRANSPORT_FILES = (
    "vergabestelle-behoerden/skills/inhouse-interkommunal/SKILL.md",
    "vergabestelle-behoerden/skills/konzessionsvergabe-konzvgv/SKILL.md",
    "bieter-unternehmen/skills/de-facto-vergabe-klage/SKILL.md",
    "konkurrenten-rechtsschutz/skills/de-facto-vergabe-135-gwb/SKILL.md",
)

BUNDESWEHR_FILES = (
    "references/bundeswehrbeschaffung-bwbbg-2026.md",
    "vergabestelle-behoerden/skills/bundeswehrbeschaffung-bwbbg-2026/SKILL.md",
    "bieter-unternehmen/skills/bundeswehrbeschaffung-bwbbg-2026/SKILL.md",
    "konkurrenten-rechtsschutz/skills/bundeswehrbeschaffung-bwbbg-2026/SKILL.md",
)

APPROVED_OLG_SKILL_CASES = {
    "Verg 28/14",
    "Verg 2/24",
    "Verg 47/18",
    "Verg 34/20",
    "Verg 36/23",
}
OLG_CASE_RE = re.compile(
    r"OLG[^\n]{0,120}\b((?:VII-)?Verg\s+\d+/\d+|\d+\s+Verg\s+\d+/\d+)",
    flags=re.IGNORECASE,
)
NEW_LAW_MARKER_RE = re.compile(
    r"(?:seit|ab)\s+(?:dem\s+)?1\.\s*Juli\s+2026|"
    r"Neu(?:verfahren|es\s+Recht)[^\n]{0,80}1\.\s*Juli\s+2026",
    flags=re.IGNORECASE,
)


def legal_text_files() -> list[Path]:
    ignored = {"dist", ".git", "node_modules"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in LEGAL_TEXT_SUFFIXES
        and not any(part in ignored for part in path.relative_to(ROOT).parts)
    ]


def require_terms(path_text: str, path: str, groups: tuple[tuple[str, ...], ...]) -> list[str]:
    errors: list[str] = []
    lowered = path_text.lower()
    for alternatives in groups:
        if not any(term.lower() in lowered for term in alternatives):
            errors.append(f"{path}: Pflichtanker fehlt: {' oder '.join(alternatives)}")
    return errors


def main() -> int:
    errors: list[str] = []
    files = legal_text_files()
    binary_files = binary_legal_files(ROOT, {".git", "dist", "node_modules"})
    contents: dict[Path, str] = {
        path: path.read_text(encoding="utf-8", errors="ignore") for path in files
    }
    for path in binary_files:
        try:
            contents[path] = read_binary_legal_text(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: Binärartefakt nicht lesbar: {exc}")

    for path, text in contents.items():
        relative = path.relative_to(ROOT)
        for case, reason in FORBIDDEN_CASES.items():
            if case in text:
                errors.append(f"{relative}: fehlzugeordneter Fall {case}: {reason}")
        for pattern, reason in FORBIDDEN_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"{relative}: veraltetes Rechtsmuster /{pattern}/: {reason}")
        if "skills" in relative.parts and path.name == "SKILL.md":
            for match in OLG_CASE_RE.finditer(text):
                case = re.sub(r"\s+", " ", match.group(1)).strip()
                if case not in APPROVED_OLG_SKILL_CASES:
                    line = text.count("\n", 0, match.start()) + 1
                    errors.append(
                        f"{relative}:{line}: OLG-Fall nicht im amtlich geprüften Skill-Allowlist: {case}"
                    )
        if (
            path != ROOT / "README.md"
            and NEW_LAW_MARKER_RE.search(text)
            and "§ 187" not in text
            and "Paragraf 187" not in text
        ):
            errors.append(
                f"{relative}: Rechtsstand ab 1. Juli 2026 ohne Geltungsweiche nach § 187 Abs. 2 GWB"
            )

    complaint_groups = (
        ("notfrist",),
        ("zwei wochen", "zwei-wochen"),
        ("zugleich",),
        ("begründen", "begründung"),
        ("keine aufschiebende wirkung",),
        ("1. juli 2026",),
        ("§ 187", "paragraf 187"),
    )
    for relative in COMPLAINT_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: Pflichtdatei fehlt")
            continue
        errors.extend(require_terms(path.read_text(encoding="utf-8"), relative, complaint_groups))

    protection_groups = (
        ("unterricht", "informiert"),
        ("§ 169",),
        ("§ 173",),
        ("§ 187", "paragraf 187"),
    )
    for relative in PROTECTION_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: Pflichtdatei fehlt")
            continue
        errors.extend(require_terms(path.read_text(encoding="utf-8"), relative, protection_groups))

    for relative in ESPD_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: Pflichtdatei fehlt")
            continue
        errors.extend(require_terms(path.read_text(encoding="utf-8"), relative, (("C-812/24",),)))

    net_zero_groups = (
        ("2024/1735",),
        ("2026/718",),
        ("70 prozent", "70-prozent"),
        ("30. juni 2026",),
        ("gpa",),
        ("kommissionsfeststellung", "artikel 29"),
    )
    for relative in NET_ZERO_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: Pflichtdatei fehlt")
            continue
        errors.extend(require_terms(path.read_text(encoding="utf-8"), relative, net_zero_groups))

    public_transport_groups = (
        ("C-856/24",),
        ("ECLI:EU:C:2026:569",),
        ("betriebsrisiko",),
        ("1370/2007",),
    )
    for relative in PUBLIC_TRANSPORT_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: Pflichtdatei fehlt")
            continue
        errors.extend(
            require_terms(path.read_text(encoding="utf-8"), relative, public_transport_groups)
        )

    bundeswehr_groups = (
        ("14. februar 2026",),
        ("§ 11 bwbbg",),
        ("§ 15 abs. 2 bwbbg",),
        ("§ 19",),
        ("§ 10 bwbbg",),
        ("§ 17 bwbbg",),
        ("§ 16 abs. 4",),
        ("nicht vorhandenen § 15 abs. 7",),
    )
    for relative in BUNDESWEHR_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: Pflichtdatei fehlt")
            continue
        errors.extend(require_terms(path.read_text(encoding="utf-8"), relative, bundeswehr_groups))

    anchor = ROOT / "references" / "leitentscheidungen-anker.md"
    if anchor.exists():
        errors.extend(
            require_terms(
                anchor.read_text(encoding="utf-8"),
                str(anchor.relative_to(ROOT)),
                (
                    ("1. juli 2026",),
                    ("§ 172", "paragraf 172"),
                    ("§ 173", "paragraf 173"),
                    ("§ 187", "paragraf 187"),
                    ("§ 108 abs. 8",),
                    ("§ 40 abs. 1 satz 2 vgv",),
                    ("bundeskanzleramt",),
                    ("§ 135 abs. 4 gwb",),
                    ("C-856/24",),
                    ("ECLI:EU:C:2026:569",),
                    ("C-590/24",),
                    ("ECLI:EU:C:2026:41",),
                    ("C-810/24",),
                    ("ECLI:EU:C:2026:69",),
                    ("C-186/25",),
                    ("ECLI:EU:C:2026:567",),
                    ("bwbbg",),
                    ("uvgo-reformentwurf", "nur als entwurf"),
                ),
            )
        )
    else:
        errors.append("references/leitentscheidungen-anker.md: Pflichtdatei fehlt")

    if errors:
        for error in errors:
            print(f"FEHLER: {error}", file=sys.stderr)
        print(f"validate-rechtsstand-2026: {len(errors)} Fehler", file=sys.stderr)
        return 1

    print(
        "validate-rechtsstand-2026 OK "
        f"({len(files)} Textdateien, {len(binary_files)} Binärartefakte, "
        f"{len(COMPLAINT_FILES)} Beschwerdekerne)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
