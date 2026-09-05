#!/usr/bin/env python3
"""Sperrt erkennbare Lösungsschlüssel auch außerhalb der Exportauswahl."""

from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "akten_dokumentqualitaet", ROOT / "scripts/validate-testakten-dokumentqualitaet.py"
)
QUALITY = importlib.util.module_from_spec(spec)
spec.loader.exec_module(QUALITY)

ANSWER_KEY = re.compile(
    r"\b(?:l[öo]e?sungsmatrix|antwortmatrix|musterl[öo]e?sung|"
    r"l[öo]e?sungsskizze|erwartungshorizont|dozentenhinweis|"
    r"pr[üu]e?ferhinweis|kandidatenl[öo]e?sung)\b", re.IGNORECASE
)
TEXT_FORMATS = QUALITY.EXPORT_TEXT_EXTS | {".md", ".odt", ".yaml", ".yml", ".ics", ".abc"}
REVIEW_FILE = ROOT / "scripts/testakte-context-review.json"


def reviewed_context(path: Path, review: dict) -> bool:
    """Nur der unveränderte, einzeln geprüfte Quellstand ist ausgenommen."""
    relative = path.relative_to(ROOT).as_posix()
    entry = review.get(relative)
    return bool(entry and entry.get("reason") and entry.get("sha256") == hashlib.sha256(path.read_bytes()).hexdigest())


def case_directories(root: Path = ROOT) -> list[Path]:
    directories = [
        path for path in sorted((root / "testakten").iterdir())
        if path.is_dir() and path.name not in {"megaprompts", "formatvorlagen-paradebeispiele"}
    ]
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    for plugin in marketplace["plugins"]:
        for name in ("testakte", "testakten"):
            path = root / plugin["source"] / name
            if path.is_dir():
                directories.append(path)
    return directories


def source_files(directory: Path):
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory)
        if not path.is_file() or any(part.startswith(".") for part in relative.parts):
            continue
        if "gesamt-pdf" in relative.parts or "__pycache__" in relative.parts:
            continue
        if path.name.lower() in {"readme.md", "readme.txt", "rubric.yaml"}:
            continue
        if path.suffix.lower() in TEXT_FORMATS:
            yield path


def text_of(path: Path) -> str:
    if path.suffix.lower() == ".odt":
        with zipfile.ZipFile(path) as archive:
            return " ".join(ET.fromstring(archive.read("content.xml")).itertext())
    return QUALITY.export_text(path)


def problems(path: Path, text: str) -> list[str]:
    found = sorted({match.group(0) for match in ANSWER_KEY.finditer(text)})
    title = path.stem.replace("_", " ").replace("-", " ")
    found.extend(match.group(0) for match in ANSWER_KEY.finditer(title))
    return sorted(set(found))


def main() -> int:
    errors = []
    scanned = set()
    image_only = []
    directories = case_directories()
    reviewed = json.loads(REVIEW_FILE.read_text(encoding="utf-8"))
    for directory in directories:
        for path in source_files(directory):
            if path in scanned:
                continue
            scanned.add(path)
            try:
                text = text_of(path)
                if not text.strip() and path.suffix.lower() == ".pdf":
                    image_only.append(path)
                markers = problems(path, text)
                if markers and reviewed_context(path, reviewed):
                    continue
                for marker in markers:
                    errors.append(f"{path.relative_to(ROOT)}: Lösungsschlüssel {marker}")
            except Exception as exc:
                errors.append(f"{path.relative_to(ROOT)}: Inhalt nicht lesbar: {exc}")
    if errors:
        print("validate-testakten-ohne-loesungen: FEHLER", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validate-testakten-ohne-loesungen OK ({len(directories)} Aktenordner, {len(scanned)} Quelldateien)")
    if image_only:
        print(f"Zusätzlich visuell zu prüfen: {len(image_only)} Bild-PDFs ohne Textebene; keine automatische Inhaltsfreigabe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
