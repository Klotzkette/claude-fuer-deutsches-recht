#!/usr/bin/env python3
"""Synchronisiert Rollenprompts und Warnhinweise innerhalb dieser Komponente."""

import argparse
from pathlib import Path

from public_release import PROMPT_SUFFIXES, ROOT, canonical_prompt, with_working_downloads
from testakte_notices import with_case_warnings


def expected_files() -> dict[Path, str]:
    expected = {}
    for role, suffix in PROMPT_SUFFIXES.items():
        expected[ROOT / role / f"{role}-werkstatt.md"] = canonical_prompt((
            ROOT / f"vergaberecht-arbeitsprompt-{suffix}.md"
        ).read_text(encoding="utf-8"))
        expected[ROOT / role / f"{role}-schnellstart.md"] = canonical_prompt(
            (ROOT / "unified-mini-prompts" / f"{role}.md").read_text(encoding="utf-8"), mini=True
        )
    readmes = [ROOT / "README.md", ROOT / "SKILLS.md"]
    readmes += [ROOT / role / "README.md" for role in PROMPT_SUFFIXES]
    readmes += list((ROOT / "testakten").glob("*/README.md"))
    readmes += [ROOT / "testakten/README.md"]
    readmes += list((ROOT / "skills-index").glob("*.md"))
    for path in readmes:
        expected[path] = with_working_downloads(with_case_warnings(path.read_text(encoding="utf-8")), path)
    return expected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, text in expected_files().items():
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            stale.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.write_text(text, encoding="utf-8")
    print(f"Rollenprompts/Downloadhinweise: {len(stale)} " + ("veraltet" if args.check else "aktualisiert"))
    if stale:
        print("\n".join(stale))
    return int(args.check and bool(stale))


if __name__ == "__main__":
    raise SystemExit(main())
