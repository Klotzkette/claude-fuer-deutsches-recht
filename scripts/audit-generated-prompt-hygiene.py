#!/usr/bin/env python3
"""Prueft generierte Werkstatt- und Schnellstart-Prompts auf Quellenrauschen."""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROTECTED_LIST = REPO / "scripts" / "handkuratierte-prompts.txt"

NOISE_BITS = (
    "Tragende Normen verifizieren",
    "Fundstellen über",
    "Fundstellen ueber",
    "gesetze-im-internet.de",
    "dejure.org",
    "openJur",
    "openjur",
    "keine Modellwissen-Zitate",
    "live prüfen",
    "live pruefen",
)

PROSE_ASCII_BITS = (
    "Arbeitsverhaeltnis",
    "Schuldverhaeltnis",
    "auslaendisch",
    "Auslaendisch",
    "Bruessel",
    "Kausalitaet",
    "Zulaessig",
    "zulaessig",
    "Rechtmaessig",
    "rechtmaessig",
    "Uebereinkommen",
    "Identitaet",
    "Ermaechtigungsgrundlage",
    "Tatbestaende",
    "Einraeumung",
    "Schoepfung",
    "endgueltig",
    "grundsaetzlich",
    "Menschenwuerde",
    "Loeschung",
    "Verguetung",
    "Aenderung",
    "geschuetzte",
    "Strafhoehe",
    "Faellen",
    "Geschaeftsfuehrer",
    "Verhaeltnismaessigkeit",
    "Insolvensnaehe",
    "Insolvenznaehe",
    "Bargeschaeftsnaehe",
    "Schoepfungshoehe",
    "Heranfuehrung",
    "Begruendung",
    "begruendung",
    "Folgenabschaetzung",
    "Verspaetung",
    "Pfaendung",
    "Gefahrerhoehung",
    "Betriebsgroesse",
    "Auskuenfte",
    "Beiraete",
    "Adhaesion",
    "Klaeger",
    "Versorgungstraeger",
    "Schoeff",
    "Bandzaehl",
    "Aktenstueck",
    "Interoperabilitaet",
    "Datenportabilitaet",
    "Tonalitaet",
    "aussergewoehnlich",
    "Jaehrlich",
    "Grossplattform",
    "Luecken-Fuelung",
    "überhoeh",
    "Überhoeh",
    "Verhältnismaess",
    "Vollstaendigkeitsgrundsatz",
)

COURT_BITS = ("BGH", "BVerfG", "BVerwG", "BAG", "BFH", "BSG", "EuGH", "OLG", "LG", "ArbG", "LAG")
TRUNCATED_CASE_END = re.compile(
    r"(?:\beingeleiteter|\bersetzt|\bstärkt|\bstatt einer|\bnicht der|"
    r"\bQuelle|\bBestandteil der Verpflichtung)\.?\s*(?:\|)?$",
    flags=re.IGNORECASE,
)
ROUTE_PREFIXES = (
    "Bearbeitungsauftrag:",
    "Prüfschritte:",
    "Norm- oder Entscheidungsbezug aus dem Fachmaterial:",
)
TRUNCATED_LEGAL_END = re.compile(
    r"\b(?:Paragraf|Artikel|Absatz|Satz|Nummer|S\.|Rn\.|Urt\.|Beschl\.)\s*$",
    flags=re.IGNORECASE,
)
TRUNCATED_ROUTE_PROSE_END = re.compile(
    r"\b(?:Abs|Art|lit|Anh|vom|dann|erzeugt|bewertet|aktive|verwertbarer|"
    r"technisch|unbefristetes|Beweisangebot|Dauer\s+max|Bei\s+alten)\.?$",
    flags=re.IGNORECASE,
)
GENERIC_ROUTE_BITS = (
    "Was soll sofort entstehen:",
    "Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht",
)


def protected_slugs() -> set[str]:
    if not PROTECTED_LIST.exists():
        return set()
    out: set[str] = set()
    for raw in PROTECTED_LIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            out.add(line)
    return out


def prompt_files() -> list[Path]:
    files: list[Path] = []
    marketplace = json.loads(
        (REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    for entry in marketplace.get("plugins", []):
        source = entry.get("source", "")
        if not isinstance(source, str) or not source.startswith("./"):
            continue
        plugin_dir = REPO / source[2:]
        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        if not manifest_path.exists():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        slug = manifest.get("name") or plugin_dir.name
        files.extend(
            (
                plugin_dir / f"{slug}-werkstatt.md",
                plugin_dir / f"{slug}-schnellstart.md",
            )
        )
    return sorted(files, key=lambda p: p.as_posix())


def main() -> int:
    protected = protected_slugs()
    problems: list[str] = []
    for path in prompt_files():
        if not path.exists():
            problems.append(f"{path.relative_to(REPO)}: erwarteter Prompt fehlt")
            continue
        plugin_slug = path.parent.name
        if plugin_slug in protected:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if path.name.endswith("-werkstatt.md"):
            section_six = re.search(
                r"^## 6\. Rechtsprechungsanker, Quellenstatus und Rechtsfolgen\s*$"
                r"(?P<body>[\s\S]*?)(?=^## 7\.)",
                text,
                flags=re.MULTILINE,
            )
            section_eight = re.search(
                r"^## 8\. Leitentscheidungen\s*$"
                r"(?P<body>[\s\S]*?)(?=^## 9\.)",
                text,
                flags=re.MULTILINE,
            )
            if section_six and section_eight:
                full_cases: dict[str, str] = {}
                for bullet in section_eight.group("body").splitlines():
                    if not bullet.startswith("- ") or ":" not in bullet:
                        continue
                    head, tail = bullet[2:].split(":", 1)
                    full_cases[head.strip()] = tail.strip().rstrip(".")
                for row in section_six.group("body").splitlines():
                    if not row.startswith("|") or "Profilanker" not in row and "extrahierter Anker" not in row:
                        continue
                    cells = [cell.strip() for cell in row.strip("|").split("|")]
                    if len(cells) != 3:
                        continue
                    head, _status, tail = cells
                    expected = full_cases.get(head)
                    if expected is not None and tail.rstrip(".") != expected:
                        rel = path.relative_to(REPO)
                        problems.append(
                            f"{rel}: Rechtsprechungstabelle kürzt den Aussagekern zu {head}"
                        )
                        break
        for bit in NOISE_BITS:
            if bit in text:
                rel = path.relative_to(REPO)
                problems.append(f"{rel}: Quellenrauschen gefunden: {bit}")
                break
        for bit in PROSE_ASCII_BITS:
            if bit in text:
                rel = path.relative_to(REPO)
                problems.append(f"{rel}: unechter Umlaut in Prosa gefunden: {bit}")
                break
        for line_no, line in enumerate(text.splitlines(), start=1):
            # URLs dürfen in eckigen Klammern stehen. Für die Klammerbilanz
            # wird deshalb die vollständige Fundstelle einschließlich der
            # optionalen Einfassung entfernt.
            without_code = re.sub(
                r"`[^`]*`|\[?https?://[^\s\]]+\]?",
                "",
                line,
            )
            if without_code.count("(") != without_code.count(")") or without_code.count("[") != without_code.count("]"):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: unausgeglichene Klammer in Promptzeile"
                )
                break
            if re.search(r"[,:];\s+im (?:konkreten )?Sachverhalt", line):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: abgebrochener Normenanker vor Prüfsatz"
                )
                break
            if line.startswith(ROUTE_PREFIXES) and TRUNCATED_LEGAL_END.search(line):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: Norm- oder Entscheidungsanker endet als Fragment"
                )
                break
            if line.startswith(ROUTE_PREFIXES) and TRUNCATED_ROUTE_PROSE_END.search(line):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: Fachroute endet als unvollständiger Satz"
                )
                break
            if line.startswith("Bearbeitungsauftrag:") and any(
                bit in line for bit in GENERIC_ROUTE_BITS
            ):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: austauschbarer Fachrouten-Auftakt"
                )
                break
            if any(court in line for court in COURT_BITS) and TRUNCATED_CASE_END.search(line):
                rel = path.relative_to(REPO)
                problems.append(
                    f"{rel}:{line_no}: Rechtsprechungsanker endet als Satzfragment"
                )
                break
    if problems:
        print("audit-generated-prompt-hygiene: FEHLER")
        for problem in problems[:80]:
            print(f"- {problem}")
        if len(problems) > 80:
            print(f"- ... {len(problems) - 80} weitere Treffer")
        return 1
    print(f"audit-generated-prompt-hygiene OK ({len(prompt_files())} Prompt-Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
