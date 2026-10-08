#!/usr/bin/env python3
"""Validate plugin release ZIPs before publishing them."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

from testakte_notices import README_NOTICE
from public_release import COMPONENT


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"validate-release-zips failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def zip_names(zip_path: Path) -> set[str]:
    try:
        with zipfile.ZipFile(zip_path) as archive:
            bad_member = archive.testzip()
            if bad_member is not None:
                fail(f"{zip_path}: corrupt member {bad_member}")
            entries = [name.replace("\\", "/") for name in archive.namelist()]
            if len(entries) != len(set(entries)):
                fail(f"{zip_path}: duplicate ZIP entries")
            for name in entries:
                parts = Path(name).parts
                if name.startswith("/") or ".." in parts:
                    fail(f"{zip_path}: unsafe ZIP entry {name!r}")
            return set(entries)
    except zipfile.BadZipFile as exc:
        fail(f"{zip_path}: invalid ZIP: {exc}")


# Cowork-/Marketplace-Upload-Limit liegt offiziell bei 50 MB. Die frühere
# Hypothese eines 1-MB-Limits war falsch — der eigentliche Bug war eine
# Zahl-Komma-Zahl-Sequenz im description-Feld (siehe validate-plugin-structure.mjs).
# Wir bleiben mit einem komfortablen Sicherheitsabstand bei 10 MB.
MAX_ZIP_BYTES = 10 * 1024 * 1024

COMMON_PLUGIN_REFERENCES = {
    "references/OUTPUT-FORMAT.md",
    "references/leitentscheidungen-anker.md",
    "references/methodik-vergaberecht.md",
    "references/netto-null-technologien-vergabe-2026.md",
    "references/praxisrechtsprechung-vk-2016-2026.md",
    "references/quellenhygiene.md",
    "references/veroeffentlichungswege.md",
    "references/zitierweise.md",
    "references/zuschlag-nicht-nur-preis.md",
}

REFERENCE_LINK_RE = re.compile(r"(?:\.\./\.\./)?references/([A-Za-z0-9_.-]+\.md)")

ROOT_PROMPTS = {
    "vergaberecht-arbeitsprompt-bieter.md",
    "vergaberecht-arbeitsprompt-konkurrenten.md",
    "vergaberecht-arbeitsprompt-vergabestelle.md",
    "vergaberecht-kurzprompt-bieter.md",
    "vergaberecht-kurzprompt-konkurrenten.md",
    "vergaberecht-kurzprompt-vergabestelle.md",
}

WORKSHOP_PROMPTS = {
    "bieter-unternehmen.md",
    "konkurrenten-rechtsschutz.md",
    "vergabestelle-behoerden.md",
}


def validate_plugin_zip(dist_dir: Path, plugin_name: str) -> None:
    zip_path = dist_dir / f"{plugin_name}.zip"
    if not zip_path.exists():
        fail(f"{zip_path}: missing plugin ZIP")

    size = zip_path.stat().st_size
    if size > MAX_ZIP_BYTES:
        fail(
            f"{zip_path}: {size} bytes überschreitet Cowork-Uploadgrenze ({MAX_ZIP_BYTES} bytes). "
            "Große Binärdateien (z. B. PDFs) entfernen und durch Online-Verweise ersetzen."
        )

    names = zip_names(zip_path)
    if ".claude-plugin/plugin.json" not in names:
        fail(f"{zip_path}: .claude-plugin/plugin.json must be at ZIP root")
    if f"{plugin_name}/.claude-plugin/plugin.json" in names:
        fail(f"{zip_path}: ZIP is nested under {plugin_name}/; upload ZIPs must be flat")
    if any(name.startswith(f"{plugin_name}/") for name in names):
        fail(f"{zip_path}: contains nested {plugin_name}/ root")
    if "CLAUDE.md" in names:
        fail(f"{zip_path}: root CLAUDE.md must not be shipped; Claude Code treats it as a warning and Cowork upload may reject it")
    if any("__pycache__/" in name or name.endswith(".pyc") for name in names):
        fail(f"{zip_path}: contains Python cache files")
    if any(name.endswith(("-werkstatt.md", "-schnellstart.md", "llm-judge-eval.py")) for name in names):
        fail(f"{zip_path}: Standalone-Prompt oder externer Entwicklungshelfer im Plugin")
    if any(re.search(r" [2-9](?:\.[^/.]+)?$", name.rsplit("/", 1)[-1]) for name in names):
        fail(f"{zip_path}: contains local suffix artifact such as 'SKILL 2.md'")
    missing_common = sorted(COMMON_PLUGIN_REFERENCES - names)
    if missing_common:
        fail(f"{zip_path}: missing common plugin reference(s): {missing_common}")
    if "references/methodik-buergerliches-recht.md" in names:
        fail(f"{zip_path}: enthält die veraltete zivilrechtliche Methodikreferenz")

    with zipfile.ZipFile(zip_path) as archive:
        manifest = json.loads(archive.read(".claude-plugin/plugin.json"))
        for filename in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
            if filename not in names or archive.read(filename) != (ROOT / filename).read_bytes():
                fail(f"{zip_path}: {filename} fehlt oder wurde veraendert")
        for name in sorted(n for n in names if n.startswith("skills/") and n.endswith("/SKILL.md")):
            text = archive.read(name).decode("utf-8")
            if "../../../references/" in text:
                fail(f"{zip_path}:{name}: uses repo-root reference path; plugin ZIPs must be self-contained")
            for match in REFERENCE_LINK_RE.finditer(text):
                ref_name = f"references/{match.group(1)}"
                if ref_name not in names:
                    fail(f"{zip_path}:{name}: referenced {ref_name} is missing in plugin ZIP")
    if manifest.get("name") != plugin_name:
        fail(f"{zip_path}: manifest name {manifest.get('name')!r} does not match {plugin_name!r}")
    source_manifest = json.loads(
        (ROOT / plugin_name / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    if manifest != source_manifest:
        fail(f"{zip_path}: plugin.json differs from current repository source")
    description = manifest.get("description", "")
    if len(description) > 300:
        fail(f"{zip_path}: manifest description has {len(description)} chars; Cowork bevorzugt <= 300")
    # Letzte Verteidigung gegen den 'Zahl-Komma-Zahl'-Validator-Bug.
    if re.search(r"\d\s*,\s*\d", description):
        fail(f"{zip_path}: manifest description enthaelt Zahl-Komma-Zahl-Sequenz; nutze 'Rn', 'und' oder '/'")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist_dir", nargs="?", type=Path, default=ROOT / "dist")
    parser.add_argument(
        "marketplace",
        nargs="?",
        type=Path,
        default=ROOT / ".claude-plugin" / "marketplace.json",
    )
    args = parser.parse_args()
    dist_dir = args.dist_dir.resolve()
    marketplace_path = args.marketplace.resolve()

    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    plugins = [plugin["name"] for plugin in marketplace["plugins"]]
    for plugin_name in plugins:
        validate_plugin_zip(dist_dir, plugin_name)

    marketplace_zip_copy = dist_dir / "marketplace.json"
    if not marketplace_zip_copy.exists():
        fail(f"{marketplace_zip_copy}: missing marketplace.json release asset")
    marketplace_copy = json.loads(marketplace_zip_copy.read_text(encoding="utf-8"))
    if marketplace_copy != marketplace:
        fail(f"{marketplace_zip_copy}: differs from current marketplace source")

    for plugin_name in plugins:
        skill_bundle = dist_dir / f"{plugin_name}-skills-markdown.zip"
        if skill_bundle.exists():
            names = zip_names(skill_bundle)
            if any("mini-prompt" in name or name.endswith(("-schnellstart.md", "-werkstatt.md")) for name in names):
                fail(f"{skill_bundle}: Standalone-Prompt im Skills-ZIP")

    complete_bundle = dist_dir / "alles-komplettpaket.zip"
    if complete_bundle.exists():
        complete_names = zip_names(complete_bundle)
        with zipfile.ZipFile(complete_bundle) as archive:
            if "README.txt" not in complete_names or not archive.read("README.txt").decode("utf-8").startswith(README_NOTICE):
                fail(f"{complete_bundle}: Warnhinweis auf ZIP-Wurzelebene fehlt")
        required_workshop = {
            f"{COMPONENT}/testakten/megaprompts/{name}"
            for name in WORKSHOP_PROMPTS
        }
        required_workshop.update(
            f"{COMPONENT}/{plugin}/{plugin}-{kind}.md"
            for plugin in plugins for kind in ("werkstatt", "schnellstart")
        )
        missing = sorted(required_workshop - complete_names)
        if missing:
            fail(f"{complete_bundle}: missing workshop prompt(s): {missing}")

    print(f"validate-release-zips OK ({len(plugins)} plugin ZIPs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
