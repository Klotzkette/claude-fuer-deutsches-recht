#!/usr/bin/env python3
"""Ersetzt Komma-Zahl-Sequenzen in SKILL.md und plugin.json descriptions.

Hintergrund: Der Cowork-Plugin-Validator bricht bei Sequenzen wie `Zahl, Zahl`
im description-Feld (z. B. `BGHZ 217, 129` oder `§§ 5, 6 DDG`). Dieses Skript
ersetzt das Komma in solchen Sequenzen durch ein Wort (`und`) oder eine
Randnummern-Notation (`Rn`), abhaengig vom Kontext.

Regeln:
- `BGHZ <Zahl>, <Zahl>`        -> `BGHZ <Zahl> Rn <Zahl>`
- `§§ <Zahl>, <Zahl>`          -> `§§ <Zahl> und <Zahl>`
- generisch `<Zahl>, <Zahl>`   -> `<Zahl> und <Zahl>`

Wird nur auf die `description`-Zeile im YAML-Frontmatter von SKILL.md und auf
das `description`-Feld in plugin.json angewandt.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Order matters: BGHZ first, then §§, then generic.
PATTERNS = [
    (re.compile(r"(BGHZ\s+\d+)\s*,\s*(\d+)"), r"\1 Rn \2"),
    (re.compile(r"(§§\s*\d+[a-z]?)\s*,\s*(\d+[a-z]?)"), r"\1 und \2"),
    (re.compile(r"(\b\d+[a-z]?)\s*,\s*(\d+[a-z]?\b)"), r"\1 und \2"),
]


def fix_text(text: str) -> str:
    # Apply each pattern repeatedly until stable, to chain through lists.
    for pat, repl in PATTERNS:
        prev = None
        while prev != text:
            prev = text
            text = pat.sub(repl, text)
    return text


def fix_skill_md(path: Path) -> bool:
    src = path.read_text(encoding="utf-8")
    lines = src.split("\n")
    if not lines or lines[0].strip() != "---":
        return False
    changed = False
    in_fm = True
    out = [lines[0]]
    i = 1
    while i < len(lines):
        line = lines[i]
        if in_fm and line.strip() == "---":
            in_fm = False
            out.append(line)
            i += 1
            continue
        if in_fm and line.startswith("description:"):
            # description value may be quoted on one line
            m = re.match(r'^(description:\s*)(.*)$', line)
            if m:
                prefix, value = m.group(1), m.group(2)
                fixed = fix_text(value)
                if fixed != value:
                    changed = True
                out.append(prefix + fixed)
                i += 1
                continue
        out.append(line)
        i += 1
    if changed:
        path.write_text("\n".join(out), encoding="utf-8")
    return changed


def fix_plugin_json(path: Path) -> bool:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    desc = data.get("description")
    if not isinstance(desc, str):
        return False
    fixed = fix_text(desc)
    if fixed == desc:
        return False
    data["description"] = fixed
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    changed_skills = []
    for p in REPO.rglob("SKILL.md"):
        if any(part in {"node_modules", ".git"} for part in p.parts):
            continue
        if fix_skill_md(p):
            changed_skills.append(p.relative_to(REPO))
    changed_plugins = []
    for p in REPO.glob("*/.claude-plugin/plugin.json"):
        if fix_plugin_json(p):
            changed_plugins.append(p.relative_to(REPO))
    print(f"SKILL.md geaendert: {len(changed_skills)}")
    for p in changed_skills:
        print(f"  - {p}")
    print(f"plugin.json geaendert: {len(changed_plugins)}")
    for p in changed_plugins:
        print(f"  - {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
