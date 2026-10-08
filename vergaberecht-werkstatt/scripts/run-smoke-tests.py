#!/usr/bin/env python3
"""Fuehrt die aus Markdown gelesene Smoke-Pruefkette robust aus.

Aufrufe:
  python3 scripts/run-smoke-tests.py
  python3 scripts/run-smoke-tests.py --quick
  python3 scripts/run-smoke-tests.py --section 1,14,18 --fail-fast

Abschnitte koennen mit ``<!-- smoke: release -->`` als teuer bzw.
releasebezogen markiert werden. ``--quick`` laesst nur diese Abschnitte aus.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time


REPO = Path(__file__).resolve().parent.parent
SMOKE_FILE = REPO / "tests" / "smoke-tests.md"
SECTION_RE = re.compile(r"^## (\d+)\.\s*(.+)$")
FENCE_OPEN_RE = re.compile(r"^```bash\s*$")
FENCE_CLOSE_RE = re.compile(r"^```\s*$")
MODE_RE = re.compile(r"^<!--\s*smoke:\s*(release|manual)\s*-->$")
DEFAULT_TIMEOUT_SECONDS = 300


class SmokeParseError(ValueError):
    """Die Markdown-Pruefkette ist strukturell nicht eindeutig."""


@dataclass
class Section:
    number: int
    title: str
    blocks: list[str] = field(default_factory=list)
    mode: str = "normal"


def parse_sections(text: str) -> list[Section]:
    """Parst nummerierte Abschnitte und lehnt stille Markdown-Drift ab."""
    sections: list[Section] = []
    current: Section | None = None
    block: list[str] | None = None
    block_start = 0

    for lineno, line in enumerate(text.splitlines(), 1):
        if block is not None:
            if FENCE_CLOSE_RE.fullmatch(line):
                if current is None:  # pragma: no cover - durch Startlogik ausgeschlossen
                    raise SmokeParseError(f"Zeile {lineno}: Bash-Block ohne Abschnitt")
                script = "\n".join(block).strip()
                if not script:
                    raise SmokeParseError(f"Zeile {block_start}: leerer Bash-Block")
                current.blocks.append(script)
                block = None
            else:
                block.append(line)
            continue

        section_match = SECTION_RE.fullmatch(line)
        if section_match:
            if current is not None:
                sections.append(current)
            current = Section(int(section_match.group(1)), section_match.group(2).strip())
            continue

        if current is None:
            continue

        if FENCE_OPEN_RE.fullmatch(line):
            block = []
            block_start = lineno
            continue

        mode_match = MODE_RE.fullmatch(line)
        if mode_match:
            if current.mode != "normal":
                raise SmokeParseError(f"Zeile {lineno}: Abschnittsmodus doppelt gesetzt")
            current.mode = mode_match.group(1)

    if block is not None:
        raise SmokeParseError(f"Zeile {block_start}: ungeschlossener Bash-Block")
    if current is not None:
        sections.append(current)
    if not sections:
        raise SmokeParseError("keine '## N.'-Abschnitte gefunden")

    numbers = [section.number for section in sections]
    if len(numbers) != len(set(numbers)):
        duplicates = sorted(number for number in set(numbers) if numbers.count(number) > 1)
        raise SmokeParseError(f"doppelte Abschnittsnummern: {duplicates}")
    expected = list(range(1, len(sections) + 1))
    if numbers != expected:
        raise SmokeParseError(f"Abschnitte nicht lueckenlos sortiert: {numbers}; erwartet {expected}")
    for section in sections:
        if section.mode == "manual" and section.blocks:
            raise SmokeParseError(f"Abschnitt {section.number}: manuell markiert, enthaelt aber Bash")
    return sections


def run_block(script: str, timeout_seconds: int) -> tuple[int, str]:
    env = os.environ.copy()
    env["PATH"] = os.pathsep.join((str(Path(sys.executable).parent), env.get("PATH", "")))
    proc = subprocess.Popen(
        ["bash", "-e", "-o", "pipefail", "-c", script],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=REPO,
        env=env,
        start_new_session=True,
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout_seconds or None)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            stdout, stderr = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            stdout, stderr = proc.communicate()
        output = (stdout + stderr).strip()
        suffix = f"\nZeitlimit von {timeout_seconds} Sekunden überschritten"
        return 124, (output + suffix).strip()
    return proc.returncode, (stdout + stderr).strip()


def parse_selection(value: str) -> set[int]:
    try:
        selected = {int(part.strip()) for part in value.split(",") if part.strip()}
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Abschnitte als kommagetrennte Zahlen angeben") from exc
    if not selected or min(selected) < 1:
        raise argparse.ArgumentTypeError("mindestens eine positive Abschnittsnummer angeben")
    return selected


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true", help="releasebezogene, teure Abschnitte auslassen")
    parser.add_argument("--section", type=parse_selection, help="nur diese Abschnitte ausfuehren, z. B. 1,14")
    parser.add_argument("--fail-fast", action="store_true", help="nach dem ersten Fehler abbrechen")
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help="Zeitlimit je Bash-Block in Sekunden; 0 deaktiviert es (Standard: 300)",
    )
    return parser.parse_args()


def main() -> int:
    args = arguments()
    if args.timeout < 0:
        print("FEHLER: --timeout darf nicht negativ sein", file=sys.stderr)
        return 2
    try:
        sections = parse_sections(SMOKE_FILE.read_text(encoding="utf-8"))
    except (OSError, SmokeParseError) as exc:
        print(f"FEHLER: {SMOKE_FILE.relative_to(REPO)}: {exc}", file=sys.stderr)
        return 2

    known = {section.number for section in sections}
    if args.section:
        unknown = args.section - known
        if unknown:
            print(f"FEHLER: unbekannte Abschnitte: {sorted(unknown)}", file=sys.stderr)
            return 2

    failed: list[str] = []
    manual: list[str] = []
    skipped: list[str] = []
    executed = 0
    t_start = time.perf_counter()
    for section in sections:
        label = f"{section.number:>2}. {section.title}"
        if args.section and section.number not in args.section:
            continue
        if section.mode == "manual" or not section.blocks:
            manual.append(label)
            print(f"  MANUELL  {label}")
            continue
        if args.quick and section.mode == "release":
            skipped.append(label)
            print(f"  SCHNELL  {label} (ausgelassen)")
            continue

        executed += 1
        t0 = time.perf_counter()
        last_output = ""
        rc_total = 0
        for script in section.blocks:
            rc_total, last_output = run_block(script, args.timeout)
            if rc_total != 0:
                break
        ms = (time.perf_counter() - t0) * 1000
        if rc_total == 0:
            print(f"  OK       {label} ({ms:.0f} ms)")
        else:
            failed.append(label)
            print(f"  FEHLER   {label} ({ms:.0f} ms)")
            for line in last_output.splitlines()[:20]:
                print(f"           | {line}")
            if args.fail_fast:
                break

    total_ms = (time.perf_counter() - t_start) * 1000
    print(
        f"run-smoke-tests: {executed - len(failed)}/{executed} ausgefuehrte Abschnitte OK, "
        f"{len(skipped)} schnell ausgelassen, {len(manual)} manuell, {total_ms:.0f} ms gesamt"
    )
    if failed:
        print(f"  Fehlgeschlagen: {', '.join(failed)}", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
