#!/usr/bin/env python3
r"""Echter YAML-Parser-Check für alle SKILL.md im Repo.

Faengt genau das ab, was 'claude plugin validate --strict' moniert:
- Unescapte " innerhalb von "..."-Strings (Quote-Sweep-Fehler)
- \& oder andere ungueltige YAML-Escapes
- Defektes Frontmatter generell
- Pflichtfeld-Fehlen, ungueltige name-/description-Werte

Parallelisiert ueber multiprocessing.Pool — bei 20k+ Skills deutlich
schneller als die fruehere serielle Variante.

Aufruf: python3 scripts/validate-yaml-frontmatter.py
Exit 0 bei OK, 1 bei Fehlern.
"""
from __future__ import annotations

import os
import re
import sys
from multiprocessing import Pool, cpu_count

try:
    import yaml
except ImportError:  # pragma: no cover
    print("FEHLER: pyyaml fehlt. Installation: pip3 install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

FORBIDDEN_FIELDS = {
    "triggers", "when_to_use", "language", "rechtsgebiet", "license",
    "argument-hint", "user-invocable", "allowed_tools", "tools", "model",
    "adapted_from", "version", "related_skills",
}
ALLOWED_FIELDS = {"name", "description", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
XML_TAG_RE = re.compile(r"<[a-zA-Z]")
COMMA_NUMBER_RE = re.compile(r"\d\s*,\s*\d")


def discover_skill_files() -> list[str]:
    skills: list[str] = []
    for root, dirs, files in os.walk("."):
        if ".git" in dirs:
            dirs.remove(".git")
        if "node_modules" in dirs:
            dirs.remove("node_modules")
        if "SKILL.md" in files:
            skills.append(os.path.join(root, "SKILL.md"))
    return skills


def check_one(path: str) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    warns: list[str] = []
    try:
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
    except OSError as e:
        errs.append(f"{path}: konnte nicht gelesen werden: {e}")
        return errs, warns
    if not content.startswith("---"):
        errs.append(f"{path}: keine Frontmatter")
        return errs, warns
    try:
        end_idx = content.index("\n---", 3)
    except ValueError:
        errs.append(f"{path}: Frontmatter nicht terminiert (--- fehlt)")
        return errs, warns
    fm_str = content[4:end_idx]
    try:
        fm = yaml.safe_load(fm_str)
    except yaml.YAMLError as e:
        errs.append(f"{path}: YAML-Parse-Fehler: {e}")
        return errs, warns
    if not isinstance(fm, dict):
        errs.append(f"{path}: Frontmatter ist kein Dict")
        return errs, warns
    if "name" not in fm:
        errs.append(f"{path}: 'name' fehlt")
    if "description" not in fm:
        errs.append(f"{path}: 'description' fehlt")
    name = fm.get("name", "")
    if not isinstance(name, str):
        errs.append(f"{path}: 'name' muss String sein, ist {type(name).__name__}")
    elif not NAME_RE.match(name):
        errs.append(f"{path}: 'name' '{name}' invalid (kebab-case, max 64)")
    skill_dir = os.path.basename(os.path.dirname(path))
    if isinstance(name, str) and name and name != skill_dir:
        errs.append(f"{path}: 'name' '{name}' != Ordnername '{skill_dir}'")
    desc = fm.get("description", "")
    if not isinstance(desc, str):
        errs.append(f"{path}: 'description' muss String sein, ist {type(desc).__name__}")
    else:
        if len(desc) > 1024:
            errs.append(f"{path}: 'description' zu lang ({len(desc)} > 1024)")
        elif len(desc) == 0:
            errs.append(f"{path}: 'description' leer")
        if XML_TAG_RE.search(desc):
            warns.append(f"{path}: 'description' enthaelt moeglicherweise XML-Tags")
        if COMMA_NUMBER_RE.search(desc):
            errs.append(f"{path}: 'description' enthaelt Zahl-Komma-Zahl (Cowork bricht)")
    for vk in FORBIDDEN_FIELDS:
        if vk in fm:
            errs.append(f"{path}: verbotenes Feld '{vk}'")
    for k in fm:
        if k not in ALLOWED_FIELDS and k not in FORBIDDEN_FIELDS:
            warns.append(f"{path}: unbekanntes Feld '{k}'")
    return errs, warns


def check_plugin_root_claude_md() -> list[str]:
    errs: list[str] = []
    for d in sorted(os.listdir(".")):
        if not os.path.isdir(d) or d.startswith("."):
            continue
        if not os.path.isfile(os.path.join(d, ".claude-plugin", "plugin.json")):
            continue
        if os.path.isfile(os.path.join(d, "CLAUDE.md")):
            errs.append(
                f"{d}/CLAUDE.md: Plugin-Root-CLAUDE.md wird nicht geladen "
                f"\u2014 als Skill verschieben oder loeschen"
            )
    return errs


def main() -> int:
    skills = discover_skill_files()
    workers = max(1, min(cpu_count(), 8))
    errors: list[str] = []
    warnings: list[str] = []
    if skills:
        chunksize = max(50, len(skills) // (workers * 4))
        with Pool(workers) as pool:
            for e, w in pool.imap_unordered(check_one, skills, chunksize=chunksize):
                if e:
                    errors.extend(e)
                if w:
                    warnings.extend(w)
    errors.extend(check_plugin_root_claude_md())

    print(f"validate-yaml-frontmatter: {len(errors)} Fehler, {len(warnings)} Warnungen")
    for w in warnings[:20]:
        print(f"  WARN: {w}")
    if errors:
        for e in errors:
            print(f"  FEHLER: {e}", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
