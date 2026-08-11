#!/usr/bin/env python3
"""Validiert zentrale Übersichtsangaben gegen Marketplace und Aktenbestand."""

from __future__ import annotations

import json
import re
from pathlib import Path

from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
PLUGIN_META_DIR = ".cla" + "ude-plugin"
MARKETPLACE = REPO / PLUGIN_META_DIR / "marketplace.json"
SKIP_TESTAKTEN = {"formatvorlagen-paradebeispiele", "megaprompts"}
CATALOG_BEGIN = "<!-- BEGIN PLUGIN-KATALOG (auto-generated) -->"
CATALOG_END = "<!-- END PLUGIN-KATALOG (auto-generated) -->"
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="


def load_marketplace() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def plugin_source(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    return REPO / source.removeprefix("./")


def count_values(marketplace: dict) -> dict[str, int | str]:
    plugins = marketplace["plugins"]
    skill_files = []
    pluginlocal_testakten = []
    for plugin in plugins:
        directory = plugin_source(plugin)
        skill_files.extend((directory / "skills").glob("*/SKILL.md"))
        testakte = directory / "testakte"
        if testakte.is_dir() and working_dump_flat_pairs(testakte, include_gesamt_pdf=False):
            pluginlocal_testakten.append(testakte)

    central_testakten = []
    root = REPO / "testakten"
    if root.is_dir():
        central_testakten = [
            child
            for child in root.iterdir()
            if child.is_dir() and child.name not in SKIP_TESTAKTEN
        ]

    return {
        "plugins": len(plugins),
        "skills": len(skill_files),
        "central_testakten": len(central_testakten),
        "testakten": len(central_testakten) + len(pluginlocal_testakten),
        "version": f"v{marketplace['version']}",
    }


def require(pattern: str, text: str, label: str) -> re.Match[str]:
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        raise AssertionError(f"{label}: Angabe fehlt")
    return match


def sequence_error(label: str, actual: list[str], expected: list[str]) -> list[str]:
    if actual == expected:
        return []
    missing = [value for value in expected if value not in actual]
    extra = [value for value in actual if value not in expected]
    first = next(
        (
            index
            for index, (left, right) in enumerate(zip(actual, expected))
            if left != right
        ),
        min(len(actual), len(expected)),
    )
    detail = f"erste Abweichung an Position {first + 1}"
    if missing:
        detail += f", fehlt: {', '.join(missing[:5])}"
    if extra:
        detail += f", zusätzlich: {', '.join(extra[:5])}"
    return [f"{label}: Reihenfolge oder Vollständigkeit stimmt nicht ({detail})"]


def natural_key(text: str) -> list[object]:
    normalized = text.lower()
    if re.match(r"^lph\d", normalized):
        normalized = f"lphz-{normalized}"
    normalized = re.sub(r"(?<=[a-z])(?=\d)", "-", normalized)
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", normalized)]


def check_sorted_inventories(marketplace: dict) -> list[str]:
    errors: list[str] = []
    plugins = marketplace["plugins"]
    names = [plugin["name"] for plugin in plugins]
    expected_names = sorted(names, key=str.lower)
    errors += sequence_error("marketplace.json Plugins", names, expected_names)

    root_readme = (REPO / "README.md").read_text(encoding="utf-8")
    if CATALOG_BEGIN not in root_readme or CATALOG_END not in root_readme:
        errors.append("README Plugin-Katalog: Generator-Markierungen fehlen")
    else:
        catalog = root_readme.split(CATALOG_BEGIN, 1)[1].split(CATALOG_END, 1)[0]
        root_names = re.findall(r"^\| \[`([^`]+)`\]\(\./[^)]+\) \|", catalog, re.MULTILINE)
        errors += sequence_error("README Plugin-Katalog", root_names, expected_names)

    skills = (REPO / "SKILLS.md").read_text(encoding="utf-8")
    skills_names = re.findall(r"^\| \*\*([^*]+)\*\* \| \d+ \|", skills, re.MULTILINE)
    errors += sequence_error("SKILLS.md Plugin-Liste", skills_names, expected_names)

    skills_index = (REPO / "skills-index" / "README.md").read_text(encoding="utf-8")
    detail_names = re.findall(r"^- \[([^]]+)\]\(\./[^)]+\.md\) \(\d+ Skills\)$", skills_index, re.MULTILINE)
    errors += sequence_error("skills-index/README.md", detail_names, expected_names)

    asset_index = (REPO / "ASSET_INDEX.md").read_text(encoding="utf-8")
    asset_names = re.findall(r"^\| \[`([^`]+)`\]\([^)]+/README\.md\) \|", asset_index, re.MULTILINE)
    errors += sequence_error("ASSET_INDEX.md Plugin-Liste", asset_names, expected_names)

    coverage = (REPO / "docs" / "werkstatt-und-schnellstart-coverage.md").read_text(encoding="utf-8")
    if "## Werkstatt-Prompts" not in coverage or "## Schnellstart-Prompts" not in coverage:
        errors.append("Prompt-Coverage: getrennte Werkstatt- und Schnellstart-Listen fehlen")
    else:
        werkstatt, schnellstart = coverage.split("## Schnellstart-Prompts", 1)
        werkstatt = werkstatt.split("## Werkstatt-Prompts", 1)[1]
        werkstatt_names = re.findall(r"^\| `([^`]+)` \|", werkstatt, re.MULTILINE)
        schnellstart_names = re.findall(r"^\| `([^`]+)` \|", schnellstart, re.MULTILINE)
        errors += sequence_error("Werkstatt-Prompt-Liste", werkstatt_names, expected_names)
        errors += sequence_error("Schnellstart-Prompt-Liste", schnellstart_names, expected_names)

    testakten_root = REPO / "testakten"
    expected_akten = sorted(
        path.name
        for path in testakten_root.iterdir()
        if path.is_dir() and (path / "README.md").is_file()
    )
    testakten_readme = (testakten_root / "README.md").read_text(encoding="utf-8")
    listed_akten = re.findall(
        r"^\| \[`([^`/]+)/`\]\(\./\1/\) \|",
        testakten_readme,
        re.MULTILINE,
    )
    errors += sequence_error("testakten/README.md Akten-Liste", listed_akten, expected_akten)

    for plugin in plugins:
        directory = plugin_source(plugin)
        readme = directory / "README.md"
        text = readme.read_text(encoding="utf-8")
        begin = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
        end = "<!-- END SKILLS-OVERVIEW (auto-generated) -->"
        if begin not in text or end not in text:
            errors.append(f"{plugin['name']}: alphabetische Skill-Komplettliste fehlt")
            continue
        overview = text.split(begin, 1)[1].split(end, 1)[0]
        actual_skills = re.findall(
            rf"^\| \[`([^`]+)`\]\({re.escape(DOWNLOAD_BASE)}[^)]*/skills/\1/SKILL\.md\) \|",
            overview,
            re.MULTILINE,
        )
        expected_skills = sorted(
            (path.parent.name for path in (directory / "skills").glob("*/SKILL.md")),
            key=natural_key,
        )
        errors += sequence_error(f"{plugin['name']} Skill-Liste", actual_skills, expected_skills)

    return errors


def check_root_readme(values: dict[str, int | str]) -> list[str]:
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    errors: list[str] = []

    plugin_count = int(require(r"\| \*\*Plugins\*\* \| (\d+)\b", readme, "README Plugins").group(1))
    if plugin_count != values["plugins"]:
        errors.append(f"README Plugins: {plugin_count} statt {values['plugins']}")

    skill_count = int(require(r"\| \*\*Skills \(SKILL\.md\)\*\* \| (\d+)\b", readme, "README Skills").group(1))
    if skill_count != values["skills"]:
        errors.append(f"README Skills: {skill_count} statt {values['skills']}")

    testakten = require(
        r"\| \*\*Testakten\*\* \| (\d+) zentral / (\d+) gesamt \|",
        readme,
        "README Testakten",
    )
    central = int(testakten.group(1))
    total = int(testakten.group(2))
    if central != values["central_testakten"] or total != values["testakten"]:
        errors.append(
            "README Testakten: "
            f"{central} zentral / {total} gesamt statt "
            f"{values['central_testakten']} zentral / {values['testakten']} gesamt"
        )

    version = require(
        r"\| \*\*Plugin-Version / Arbeitsstand\*\* \| `(v\d+\.\d+\.\d+)`",
        readme,
        "README Version",
    ).group(1)
    if version != values["version"]:
        errors.append(f"README Version: {version} statt {values['version']}")

    return errors


def check_generated_overviews(values: dict[str, int | str]) -> list[str]:
    errors: list[str] = []

    skills = (REPO / "SKILLS.md").read_text(encoding="utf-8")
    skills_match = require(
        r"Gesamtübersicht aller \*\*(\d+) Skills\*\* in \*\*(\d+) Plugins\*\*",
        skills,
        "SKILLS Kopf",
    )
    if int(skills_match.group(1)) != values["skills"]:
        errors.append(f"SKILLS Skills: {skills_match.group(1)} statt {values['skills']}")
    if int(skills_match.group(2)) != values["plugins"]:
        errors.append(f"SKILLS Plugins: {skills_match.group(2)} statt {values['plugins']}")
    skills_version = require(r"Stand: `(v\d+\.\d+\.\d+)`", skills, "SKILLS Version").group(1)
    if skills_version != values["version"]:
        errors.append(f"SKILLS Version: {skills_version} statt {values['version']}")

    skills_index = (REPO / "skills-index" / "README.md").read_text(encoding="utf-8")
    index_version = require(r"Stand: `(v\d+\.\d+\.\d+)`", skills_index, "Skills-Index Version").group(1)
    if index_version != values["version"]:
        errors.append(f"Skills-Index Version: {index_version} statt {values['version']}")

    asset_index = (REPO / "ASSET_INDEX.md").read_text(encoding="utf-8")
    asset_version = require(r"Stand: (v\d+\.\d+\.\d+),", asset_index, "Asset-Index Version").group(1)
    if asset_version != values["version"]:
        errors.append(f"Asset-Index Version: {asset_version} statt {values['version']}")

    testakten = (REPO / "testakten" / "README.md").read_text(encoding="utf-8")
    testakten_match = require(
        r"Stand (v\d+\.\d+\.\d+): (\d+) zentrale Testakten",
        testakten,
        "Testakten-README Stand",
    )
    if testakten_match.group(1) != values["version"]:
        errors.append(f"Testakten-README Version: {testakten_match.group(1)} statt {values['version']}")
    if int(testakten_match.group(2)) != values["central_testakten"]:
        errors.append(
            "Testakten-README Zählung: "
            f"{testakten_match.group(2)} statt {values['central_testakten']}"
        )

    return errors


def main() -> int:
    marketplace = load_marketplace()
    values = count_values(marketplace)
    errors = (
        check_root_readme(values)
        + check_generated_overviews(values)
        + check_sorted_inventories(marketplace)
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "validate-root-readme-overview OK "
        f"({values['plugins']} Plugins, {values['skills']} Skills, "
        f"{values['central_testakten']} zentrale Testakten, Stand {values['version']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
