#!/usr/bin/env python3
"""Prüft alle Schnellstarts auf einen vollständigen, reibungsarmen Einstieg."""

from __future__ import annotations

import json
import re
from pathlib import Path

from quality_lab import load, validate_profile
from prompt_limits import MAX_MINI_BYTES


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
PROTECTED = REPO / "scripts" / "handkuratierte-prompts.txt"

MAX_BYTES = MAX_MINI_BYTES


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
        if len(raw) > MAX_BYTES:
            problems.append(f"{rel}: {len(raw)} Bytes, Grenze ist höchstens {MAX_BYTES}")
        if len(raw) < 2500:
            problems.append(f"{rel}: nur {len(raw)} Bytes, fachlicher Schnellstart zu dünn")
        if not text.startswith("# "):
            problems.append(f"{rel}: H1 steht nicht am Dateianfang")
        if "[!--" in text or "<!--" in text:
            problems.append(f"{rel}: technischer Marker im sichtbaren Prompt")
        review_path = REPO / "quality" / "evals" / f"{slug}.json"
        individually_reviewed = review_path.is_file()
        if individually_reviewed:
            try:
                validate_profile(load(review_path), slug, path.parent, REPO)
            except (ValueError, OSError, TypeError, KeyError) as exc:
                problems.append(f"{rel}: ungültige individuelle Prüfung: {exc}")
        elif slug in protected:
            if "Bedienregel: Dateien und Ordner zuerst gezielt lesen." not in text:
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
                ("konkreter Auftrag", "konkrete Aufträge direkt", "verlangten Dokument", "starte mit dem Arbeitsprodukt"),
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
                "eigenständige Fachroute ohne Pluginzwang",
                ("Ohne weitere Skills hier weiterarbeiten",),
            ),
            (
                "Abbruchgrenze",
                ("stop", "unterbrich", "unterbrechen", "qualitätsgate", "abbruch"),
            ),
        )
        # Wortgleichheit ist kein Nachweis fachlicher Qualität. Individuelle
        # Profile werden strukturell geprüft; Ergebnistests bleiben gesondert.
        for label, alternatives in (() if individually_reviewed else checks):
            if not has_all(text, alternatives):
                problems.append(f"{rel}: {label} fehlt")

        headings = [
            int(match.group(1))
            for match in re.finditer(r"^## (\d+)\. ", text, flags=re.MULTILINE)
        ]
        if not individually_reviewed and headings and headings != list(range(1, len(headings) + 1)):
            problems.append(f"{rel}: H2-Gliederung ist nicht fortlaufend dezimal")
        if individually_reviewed:
            labels = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
            numbers = []
            for label in labels:
                number = re.match(r"(\d+(?:\.\d+)*)(?:\.)?\s+\S", label)
                if number is None:
                    problems.append(f"{rel}: nicht dezimale Überschrift: {label}")
                else:
                    numbers.append(tuple(map(int, number.group(1).split('.'))))
            if not numbers or numbers != sorted(set(numbers)):
                problems.append(f"{rel}: fehlende, doppelte oder ungeordnete Abschnittsnummern")
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
    print(f"audit-quickstart-usability OK ({len(entries)} Schnellstarts; Strukturprüfung, kein Modelltest)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
