"""Insert and check notices immediately above test-case download groups."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from testakte_disclaimer import NOTICE_MARKDOWN


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
HEADING = re.compile(r"^#{1,6}\s")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


class DownloadLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.destinations: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self.destinations.extend(value for key, value in attrs if key == "href" and value)


def is_case_download(destination: str, *, case_readme: bool = False) -> bool:
    parsed = urlsplit(destination)
    path = unquote(parsed.path).lower()
    name = path.rsplit("/", 1)[-1]
    parts = path.split("/")
    if name.endswith(".zip"):
        return "testakte" in name or name == "alles-komplettpaket.zip"
    if not name.endswith(".pdf"):
        return False
    return (
        "gesamt-pdf" in parts
        or "testakten" in parts
        or "testakte" in parts
        or (case_readme and not parsed.netloc)
    )


def has_case_download(block: str, *, case_readme: bool = False) -> bool:
    parser = DownloadLinks()
    parser.feed(block)
    destinations = parser.destinations
    for match in MARKDOWN_LINK.finditer(block):
        raw = match.group(1).strip()
        if not raw:
            continue
        destination = raw[1:raw.index(">")] if raw.startswith("<") and ">" in raw else raw.split()[0]
        destinations.append(destination)
    return any(is_case_download(url, case_readme=case_readme) for url in destinations)


def download_group_starts(text: str, *, case_readme: bool = False) -> list[int]:
    """Keep contiguous table rows or link paragraphs together, excluding code."""
    starts: list[int] = []
    offset = 0
    start = 0
    lines: list[str] = []
    kind = ""
    fence = ""

    def finish() -> None:
        if lines and has_case_download("".join(lines), case_readme=case_readme):
            starts.append(start)
        lines.clear()

    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        marker = FENCE.match(line)
        if fence:
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                fence = ""
        elif marker:
            finish()
            fence = marker.group(1)
        elif not stripped or HEADING.match(line) or stripped.startswith("<!--"):
            finish()
        else:
            next_kind = "table" if stripped.startswith("|") else "paragraph"
            if lines and next_kind != kind:
                finish()
            if not lines:
                start = offset
                kind = next_kind
            lines.append(line)
        offset += len(line)
    finish()
    return starts


def missing_notice_positions(text: str, *, case_readme: bool = False) -> list[int]:
    return [
        start
        for start in download_group_starts(text, case_readme=case_readme)
        if not text[:start].rstrip().endswith(NOTICE_MARKDOWN)
    ]


def ensure_download_notices(text: str, *, case_readme: bool = False) -> str:
    for start in reversed(missing_notice_positions(text, case_readme=case_readme)):
        prefix = text[:start]
        spacing = "" if not prefix or prefix.endswith("\n\n") else "\n"
        text = prefix + spacing + NOTICE_MARKDOWN + "\n\n" + text[start:]
    return text


def download_readmes(root: Path) -> list[Path]:
    """Only README/download documentation, never skills or source documents."""
    paths = {root / "README.md", root / "ASSET_INDEX.md"}
    paths.update(root.glob("*/README.md"))
    paths.update((root / "testakten").rglob("README.md"))
    marketplace = root / ".claude-plugin" / "marketplace.json"
    if marketplace.is_file():
        for plugin in json.loads(marketplace.read_text(encoding="utf-8"))["plugins"]:
            directory = root / plugin["source"].removeprefix("./")
            paths.add(directory / "README.md")
            paths.update((directory / "testakte").rglob("README.md"))
    return sorted(path for path in paths if path.is_file())


def is_case_readme(path: Path, root: Path) -> bool:
    return bool({"testakte", "testakten"} & set(path.relative_to(root).parts[:-1]))


def update_download_readmes(root: Path) -> int:
    changed = 0
    for path in download_readmes(root):
        text = path.read_text(encoding="utf-8")
        updated = ensure_download_notices(text, case_readme=is_case_readme(path, root))
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed
