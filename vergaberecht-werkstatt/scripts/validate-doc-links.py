#!/usr/bin/env python3
"""Prueft lokale Markdown-Links in jeder versionierten Markdown-Datei.

Externe URLs werden nicht aufgerufen, damit der Smoke-Test schnell und offline
lauffaehig bleibt. Der breite Scan verhindert, dass defekte Links in Skills,
Testakten oder Referenzseiten von einer reinen README-Pruefung uebersehen werden.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")
SKIP_PARTS = {".git", ".venv", "dist", "node_modules"}
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
ATX_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
HTML_ANCHOR_RE = re.compile(r"<(?:a\s+[^>]*(?:id|name)|[^>]+\s+id)=[\"']([^\"']+)[\"']", re.IGNORECASE)


def discover_docs() -> list[Path]:
    docs: set[Path] = set()
    for path in REPO.rglob("*.md"):
        rel = path.relative_to(REPO)
        if not SKIP_PARTS.intersection(rel.parts):
            docs.add(rel)
    return sorted(docs, key=lambda path: path.as_posix())


def parse_target(raw: str) -> tuple[str, str] | None:
    target = raw.strip()
    if not target or target.startswith(EXTERNAL_PREFIXES[:-1]):
        return None
    if target.startswith("<"):
        closing = target.find(">")
        if closing == -1:
            return target, ""
        target = target[1:closing].strip()
    else:
        title_match = re.match(
            r"^(.*?)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))$",
            target,
        )
        if title_match:
            target = title_match.group(1).strip()
    path_part, separator, fragment = target.partition("#")
    path_part = urllib.parse.unquote(path_part.split("?", 1)[0].strip())
    fragment = urllib.parse.unquote(fragment.strip()) if separator else ""
    return path_part, fragment


def github_slug(value: str) -> str:
    """Nähert GitHubs Überschriftenanker für deutschsprachige Dokumente an."""
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").replace("*", "").replace("_", "")
    value = value.casefold().strip()
    value = "".join(char for char in value if char.isalnum() or char in {" ", "-"})
    return re.sub(r"\s+", "-", value)


def markdown_anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors = {match.group(1).casefold() for match in HTML_ANCHOR_RE.finditer(text)}
    counts: dict[str, int] = {}
    in_fence = False
    fence_char = ""
    previous = ""
    for line in text.splitlines():
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
            previous = ""
            continue
        if in_fence:
            continue
        heading = ATX_HEADING_RE.match(line)
        title = heading.group(1) if heading else ""
        if not title and previous.strip() and re.fullmatch(r"\s*(?:=+|-+)\s*", line):
            title = previous.strip()
        if title:
            base = github_slug(title)
            if base:
                duplicate = counts.get(base, 0)
                anchors.add(base if duplicate == 0 else f"{base}-{duplicate}")
                counts[base] = duplicate + 1
        previous = line
    return anchors


def main() -> int:
    docs = discover_docs()
    broken: list[tuple[Path, str]] = []
    missing_docs = [doc for doc in docs if not (REPO / doc).is_file()]
    if missing_docs:
        for doc in missing_docs:
            print(f"FEHLT: {doc}", file=sys.stderr)
        return 1

    repo_resolved = REPO.resolve()
    public_navigation = {
        (REPO.parent / relative).resolve()
        for relative in ("README.md", "SKILLS.md", "ASSET_INDEX.md", "testakten/README.md",
                         "skills-index/vergabestelle-behoerden.md", "skills-index/bieter-unternehmen.md",
                         "skills-index/konkurrenten-rechtsschutz.md")
    }
    anchor_cache: dict[Path, set[str]] = {}
    for doc in docs:
        text = (REPO / doc).read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            parsed = parse_target(match.group(1))
            if parsed is None:
                continue
            normalized, fragment = parsed
            candidate = (
                (REPO / doc).resolve()
                if not normalized
                else ((REPO / doc).parent / normalized).resolve()
            )
            try:
                candidate.relative_to(repo_resolved)
            except ValueError:
                if candidate not in public_navigation or not candidate.is_file():
                    broken.append((doc, match.group(1)))
                continue
            if not candidate.exists():
                broken.append((doc, match.group(1)))
                continue
            markdown_target = candidate / "README.md" if candidate.is_dir() else candidate
            if fragment and markdown_target.suffix.casefold() == ".md":
                anchors = anchor_cache.setdefault(
                    markdown_target,
                    markdown_anchors(markdown_target),
                )
                if fragment.casefold() not in anchors:
                    broken.append((doc, match.group(1)))

    if broken:
        print("Kaputte lokale Markdown-Links:", file=sys.stderr)
        for doc, target in broken:
            print(f"  {doc}: {target}", file=sys.stderr)
        return 1

    print(f"validate-doc-links OK ({len(docs)} Dateien)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
