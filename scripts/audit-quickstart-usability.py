#!/usr/bin/env python3
"""Prüft alle Schnellstarts auf einen vollständigen, reibungsarmen Einstieg."""

from __future__ import annotations

import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
PROTECTED = REPO / "scripts" / "handkuratierte-prompts.txt"
MAX_BYTES = 7500


def protected_slugs() -> set[str]:
    return {
        line.strip()
        for line in PROTECTED.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def plugin_entries() -> list[tuple[str, Path]]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entries: list[tuple[str, Path]] = []
    for plugin in data.get("plugins", []):
        slug = plugin.get("name", "")
        source = plugin.get("source", "")
        if not slug or not isinstance(source, str) or not source.startswith("./"):
            continue
        entries.append((slug, REPO / source[2:] / f"{slug}-schnellstart.md"))
    return entries


def has_all(text: str, alternatives: tuple[str, ...]) -> bool:
    lowered = text.casefold()
    return any(part.casefold() in lowered for part in alternatives)


def main() -> int:
    protected = protected_slugs()
    problems: list[str] = []
    entries = plugin_entries()
    for slug, path in entries:
        rel = path.relative_to(REPO)
        if not path.is_file():
            problems.append(f"{rel}: fehlt")
            continue
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        if len(raw) >= MAX_BYTES:
            problems.append(f"{rel}: {len(raw)} Bytes, Grenze ist kleiner als {MAX_BYTES}")
        if len(raw) < 2500:
            problems.append(f"{rel}: nur {len(raw)} Bytes, fachlicher Schnellstart zu dünn")
        if not text.startswith("# "):
            problems.append(f"{rel}: H1 steht nicht am Dateianfang")
        if "[!--" in text or "<!--" in text:
            problems.append(f"{rel}: technischer Marker im sichtbaren Prompt")
        if slug in protected:
            if "Bedienregel: Dateien und Ordner zuerst lesen." not in text:
                problems.append(f"{rel}: handkuratierte Bedienregel fehlt")
        elif "## 1. Sofortstart nach Eingangslage" not in text:
            problems.append(f"{rel}: fachbezogener Sofortstart fehlt")

        checks = (
            (
                "Dateien zuerst",
                (
                    "Dateien oder Ordner",
                    "Dateien und Ordner zuerst",
                    "Unterlagen zuerst",
                    "Dateien zuerst",
                ),
            ),
            (
                "Direktproduktion",
                ("konkreter Auftrag", "verlangten Dokument", "starte mit dem Arbeitsprodukt"),
            ),
            (
                "begrenzte Rückfrage",
                ("gebündelte Frage", "höchstens zwei", "höchstens eine", "frage nur"),
            ),
            (
                "große Ordner",
                ("großen Ordnern", "große Ordner", "umfangreichen Unterlagen"),
            ),
            (
                "Teilstand",
                ("Teilstand", "belastbare Kurzfassung", "sofortbild"),
            ),
            (
                "Fortsetzung ohne Neustart",
                ("ohne Neustart", "nicht neu beginnen", "beginne die Prüfung nicht erneut"),
            ),
            (
                "interne Fachroute",
                ("fachskills laufen intern", "fachskills intern", "fachskill intern"),
            ),
            (
                "Abbruchgrenze",
                ("stop", "unterbrich", "unterbrechen", "qualitätsgate", "abbruch"),
            ),
        )
        for label, alternatives in checks:
            if not has_all(text, alternatives):
                problems.append(f"{rel}: {label} fehlt")

        headings = [
            int(match.group(1))
            for match in re.finditer(r"^## (\d+)\. ", text, flags=re.MULTILINE)
        ]
        if headings and headings != list(range(1, len(headings) + 1)):
            problems.append(f"{rel}: H2-Gliederung ist nicht fortlaufend dezimal")
        stripped = text.rstrip()
        if not stripped or stripped[-1] not in ".!?`)]":
            problems.append(f"{rel}: Dateiende wirkt abgeschnitten")
        if re.search(r"\b(?:Paragraf|Artikel|Absatz|Satz|Nummer)\s*$", stripped):
            problems.append(f"{rel}: Dateiende bricht in einem Rechtsanker ab")

    if problems:
        print("audit-quickstart-usability: FEHLER")
        for problem in problems[:100]:
            print(f"- {problem}")
        if len(problems) > 100:
            print(f"- ... {len(problems) - 100} weitere Treffer")
        return 1
    print(f"audit-quickstart-usability OK ({len(entries)} Schnellstarts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
