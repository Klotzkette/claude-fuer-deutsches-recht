"""Gemeinsame Ziele der verschachtelten oeffentlichen Komponente."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "Klotzkette/claude-fuer-deutsches-recht"
COMPONENT = "vergaberecht-werkstatt"
PUBLIC_MARKETPLACE = "klotzkette-german-legal-skills"
VERSION = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))["version"]
RELEASE_TAG = f"{COMPONENT}-v{VERSION}"
RELEASE_BASE = f"https://github.com/{REPOSITORY}/releases/download/{RELEASE_TAG}"
BLOB_BASE = f"https://github.com/{REPOSITORY}/blob/main/{COMPONENT}"
RAW_BASE = f"https://raw.githubusercontent.com/{REPOSITORY}/main/{COMPONENT}"
DOWNLOAD_BASE = f"https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path={COMPONENT}"
PROMPT_SUFFIXES = {
    "vergabestelle-behoerden": "vergabestelle",
    "bieter-unternehmen": "bieter",
    "konkurrenten-rechtsschutz": "konkurrenten",
}

sys.path.append(str(ROOT.parent / "scripts"))
from release_routing import plugin_asset_url, validate_plugin_version


def plugin_download(name: str) -> str:
    return plugin_asset_url(name, root=ROOT.parent)


def check_plugin_version(plugin: dict) -> None:
    validate_plugin_version(plugin, VERSION, root=ROOT.parent)


def markdown_download(relative: str) -> str:
    return DOWNLOAD_BASE + "/" + quote(relative, safe="/")


def with_working_downloads(text: str, document: Path) -> str:
    """Ersetzt Arbeitsdatei-Links, ohne Navigationsseiten umzuleiten."""
    lines = text.splitlines(keepends=True)
    for token in MarkdownIt("commonmark").parse(text):
        replacements = {}
        for child in token.children or []:
            if child.type != "link_open":
                continue
            destination = child.attrGet("href") or ""
            parsed = urlsplit(destination)
            name = Path(unquote(parsed.path)).name
            if name != "SKILL.md" and not name.endswith(("-werkstatt.md", "-schnellstart.md", "-hauptproblem.md")):
                continue
            if destination.startswith(BLOB_BASE + "/"):
                relative = unquote(parsed.path.split(f"/main/{COMPONENT}/", 1)[1])
            elif destination.startswith(RAW_BASE + "/"):
                relative = unquote(parsed.path.split(f"/main/{COMPONENT}/", 1)[1])
            elif not parsed.scheme:
                target = (document.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(ROOT):
                    continue
                relative = target.relative_to(ROOT).as_posix()
            else:
                continue
            replacements[destination] = markdown_download(relative)
        if replacements and token.map:
            start, end = token.map
            block = "".join(lines[start:end])
            for destination, url in replacements.items():
                block = block.replace(f"]({destination})", f"]({url})")
            lines[start:end] = block.splitlines(keepends=True)
    return "".join(lines)


def compact_mini(text: str) -> str:
    """Entfernt nur Tabellenpolster, falls das UTF-8-Budget es erfordert."""
    if len(text.encode("utf-8")) > 7500:
        text = "\n".join(
            "|".join(cell.strip() for cell in line.split("|"))
            if line.startswith("|") else line
            for line in text.splitlines()
        ) + "\n"
    if len(text.encode("utf-8")) > 7500:
        raise ValueError("Mini-Prompt ueberschreitet 7500 UTF-8-Bytes")
    return text


def canonical_prompt(text: str, *, mini: bool = False) -> str:
    """Normalisiert nur Ueberschriften und Produktbezeichnungen der Kopie."""
    counters = [0] * 5
    output = []
    fence = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            fence = None if fence == marker else marker if fence is None else fence
            output.append(line)
            continue
        if fence:
            output.append(line)
            continue
        parts = re.split(r"(`[^`]*`)", line)
        for index in range(0, len(parts), 2):
            parts[index] = parts[index].replace("Claude-Skill", "Skill")
        line = "".join(parts)
        match = re.match(r"^(#{2,6}) (.+)$", line)
        if match:
            level = len(match[1]) - 2
            title = match[2]
            # Die Quelle markiert Unterpunkte 2.1 / 4.1 / 4.2 ebenfalls als H3.
            if level == 1 and re.match(r"^\d+\.\d+\s", title):
                level = 2
            title = re.sub(r"^Phase [A-Z]:\s*", "", title)
            title = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", title)
            counters[level] += 1
            counters[level + 1:] = [0] * (4 - level)
            if any(number == 0 for number in counters[:level]):
                raise ValueError("Ueberschriftenhierarchie ueberspringt eine Ebene")
            number = ".".join(str(value) for value in counters[:level + 1])
            line = f"{'#' * (level + 2)} {number}. {title}"
        output.append(line)
    result = "\n".join(output) + "\n"
    return compact_mini(result) if mini else result
