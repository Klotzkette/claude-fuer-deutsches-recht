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


def component_release(root: Path = ROOT) -> dict:
    """Die importierte Akten-/Spezialausgabe folgt ihrem eigenen Herkunftsnachweis."""
    record = json.loads((root / "source-import.json").read_text(encoding="utf-8"))
    if (record.get("schema_version") != 1 or record.get("component") != COMPONENT
            or not re.fullmatch(re.escape(COMPONENT) + r"-v\d+\.\d+\.\d+", str(record.get("release", "")))):
        raise ValueError("Keine eindeutige Komponentenrelease-Zuordnung in source-import.json")
    for key in ("plugins", "cases"):
        values = record.get(key)
        if (not isinstance(values, list) or not values
                or any(not isinstance(value, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value) for value in values)
                or len(values) != len(set(values))):
            raise ValueError(f"Keine eindeutige {key}-Zuordnung in source-import.json")
    if set(record["plugins"]) != set(PROMPT_SUFFIXES):
        raise ValueError("Komponentenrelease muss genau die drei Vergaberollen enthalten")
    return record


# Akten und Spezialassets bleiben an die importierte Ausgabe gebunden;
# RELEASE_TAG/BASE behalten für neue Paketbauten ihre Marketplace-Semantik.
COMPONENT_RELEASE_TAG = component_release()["release"]
COMPONENT_RELEASE_BASE = f"https://github.com/{REPOSITORY}/releases/download/{COMPONENT_RELEASE_TAG}"

sys.path.append(str(ROOT.parent / "scripts"))
from release_routing import plugin_asset_url, scoped_asset_url, validate_plugin_version, verified_scoped_package_version
from quality_lab import validate_prompt_review


def reviewed_prompt(path: Path, review: dict) -> str:
    """Erhält die redigierte Fassung nur bei gültigem dateigebundenem Prüfnachweis."""
    validate_prompt_review(review, "Rollenprompt-Prüfung", path)
    return path.read_text(encoding="utf-8")


def expected_role_prompt(role: str, kind: str) -> str:
    """Verwendet geprüfte Einzelfassungen, sonst die bisherige Generatorquelle."""
    if role not in PROMPT_SUFFIXES or kind not in {"werkstatt", "schnellstart"}:
        raise ValueError("Unbekannte Rollenprompt-Zuordnung")
    profile = ROOT.parent / "quality" / "evals" / f"{role}.json"
    if profile.is_file():
        review = json.loads(profile.read_text(encoding="utf-8"))
        key = "workshop_review" if kind == "werkstatt" else "mini_review"
        target = ROOT / role / f"{role}-{kind}.md"
        return reviewed_prompt(target, review.get(key))
    source = (
        ROOT / f"vergaberecht-arbeitsprompt-{PROMPT_SUFFIXES[role]}.md"
        if kind == "werkstatt" else ROOT / "unified-mini-prompts" / f"{role}.md"
    )
    return canonical_prompt(source.read_text(encoding="utf-8"), mini=kind == "schnellstart")


def plugin_download(name: str) -> str:
    return plugin_asset_url(name, root=ROOT.parent)


def check_plugin_version(plugin: dict) -> None:
    parent = ROOT.parent
    marketplace = json.loads((parent / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    role = plugin["name"]
    entries = [entry for entry in marketplace["plugins"] if entry["name"] == role]
    if len(entries) != 1 or entries[0].get("source") != f"./{COMPONENT}/{role}":
        raise ValueError(f"{role}: eindeutige öffentliche Rollenquelle fehlt")
    if plugin.get("version") != entries[0].get("version"):
        raise ValueError(f"{role}: lokale und öffentliche Rollenfassung weichen ab")
    validate_plugin_version(plugin, marketplace["version"], root=parent)
    asset = f"{role}.zip"
    route = scoped_asset_url(asset, root=parent)
    if route is None:
        raise ValueError(f"{role}: exakte Komponentenroute fehlt")
    tag = route.rsplit("/", 2)[-2]
    if not (tag.endswith(f"-v{plugin['version']}") or
            verified_scoped_package_version(asset, tag, plugin["version"], root=parent)):
        raise ValueError(f"{role}: Komponentenroute passt nicht zur Rollenfassung")


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
