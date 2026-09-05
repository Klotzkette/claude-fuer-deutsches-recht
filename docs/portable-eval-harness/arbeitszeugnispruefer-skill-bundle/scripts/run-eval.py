#!/usr/bin/env python3
"""run-eval.py - Schlanker Eval-Harness fuer Klotzkette German Legal Skills.

Liest pro Testakte (fixtures/<slug>/rubric.yaml) eine Liste von Pass/Fail-
Pruefungen ein, fuehrt sie aus und schreibt einen All-Pass-Score nach
Harvey-LAB-Vorbild.

Verwendung:
    python3 scripts/run-eval.py                          # alle Testakten
    python3 scripts/run-eval.py <slug1> <slug2>         # gezielt
    python3 scripts/run-eval.py --report                # MD-Report nach EVAL_RESULTS.md

Pruefungstypen (rubric.yaml):
- file_exists          ->  Datei existiert
- text_contains        ->  Text-Substring kommt in Datei vor
- regex_match          ->  Regex matcht in Datei
- file_count           ->  Anzahl Dateien matches glob >= N
- yaml_field_equals    ->  YAML-Frontmatter-Feld hat erwarteten Wert
- json_field_equals    ->  JSON-Feld hat erwarteten Wert
- human_review         ->  Manuell zu bewerten (in der Eval als 'skipped' gewertet)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TESTAKTEN = REPO / "fixtures"


@dataclass
class CheckResult:
    rubric_id: str
    check_type: str
    description: str
    passed: bool | None  # None = skipped (human_review)
    detail: str = ""


@dataclass
class AktenResult:
    slug: str
    has_rubric: bool
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def all_passed(self) -> bool:
        decided = [c for c in self.checks if c.passed is not None]
        return bool(decided) and all(c.passed for c in decided)

    @property
    def stats(self) -> dict[str, int]:
        passed = sum(1 for c in self.checks if c.passed is True)
        failed = sum(1 for c in self.checks if c.passed is False)
        skipped = sum(1 for c in self.checks if c.passed is None)
        return {"passed": passed, "failed": failed, "skipped": skipped}


def load_yaml(path: Path) -> dict:
    """Minimal-Parser: nutzt PyYAML, faellt notfalls auf einfaches Parsing zurueck."""
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except ImportError:
        # Sehr einfacher Parser fuer flache YAML-Strukturen
        result: dict = {"checks": []}
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.rstrip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("- id:"):
                current = {"id": line.split(":", 1)[1].strip()}
                result["checks"].append(current)
            elif line.startswith("  ") and current and ":" in line:
                k, v = line.strip().split(":", 1)
                current[k.strip()] = v.strip().strip('"').strip("'")
        return result


def run_check(akte_dir: Path, check: dict) -> CheckResult:
    cid = check.get("id", "?")
    ctype = check.get("check_type", "?")
    desc = check.get("description", "")

    def ok(detail=""):
        return CheckResult(cid, ctype, desc, True, detail)

    def fail(detail):
        return CheckResult(cid, ctype, desc, False, detail)

    def skip(detail):
        return CheckResult(cid, ctype, desc, None, detail)

    if ctype == "file_exists":
        target = akte_dir / check["path"]
        if target.is_file():
            return ok(f"found {target.relative_to(akte_dir)}")
        return fail(f"missing {target.relative_to(akte_dir)}")

    if ctype == "text_contains":
        target = akte_dir / check["path"]
        if not target.is_file():
            return fail(f"file missing: {target.relative_to(akte_dir)}")
        needle = check.get("contains", "")
        text = target.read_text(encoding="utf-8", errors="ignore")
        return ok("substring found") if needle in text else fail(f"missing substring: {needle[:60]!r}")

    if ctype == "regex_match":
        target = akte_dir / check["path"]
        if not target.is_file():
            return fail(f"file missing: {target.relative_to(akte_dir)}")
        pat = check.get("pattern", "")
        text = target.read_text(encoding="utf-8", errors="ignore")
        if re.search(pat, text, re.MULTILINE):
            return ok(f"regex matched")
        return fail(f"regex did not match: {pat!r}")

    if ctype == "file_count":
        pattern = check.get("glob", "*")
        min_count = int(check.get("min", 1))
        files = list(akte_dir.glob(pattern))
        if len(files) >= min_count:
            return ok(f"found {len(files)} files matching {pattern}")
        return fail(f"only {len(files)} files matching {pattern} (need {min_count})")

    if ctype == "human_review":
        return skip(check.get("note", "manual review required"))

    return fail(f"unknown check_type: {ctype}")


def evaluate_akte(slug: str) -> AktenResult:
    akte_dir = TESTAKTEN / slug
    result = AktenResult(slug=slug, has_rubric=False)
    rubric_path = akte_dir / "rubric.yaml"
    if not rubric_path.is_file():
        return result
    result.has_rubric = True
    rubric = load_yaml(rubric_path)
    for check in rubric.get("checks", []):
        result.checks.append(run_check(akte_dir, check))
    return result


def render_report(results: list[AktenResult]) -> str:
    lines = ["# Eval-Results", "", f"Stand: {datetime.utcnow().isoformat(timespec='seconds')}Z", ""]
    total = len(results)
    with_rubric = [r for r in results if r.has_rubric]
    all_pass = [r for r in with_rubric if r.all_passed]
    lines.append(f"- Testakten gesamt: **{total}**")
    lines.append(f"- mit Rubric: **{len(with_rubric)}**")
    lines.append(f"- All-Pass (alle Checks bestanden, ohne human_review): **{len(all_pass)}**")
    lines.append("")
    lines.append("## Detail pro Akte (nur Akten mit Rubric)")
    lines.append("")
    lines.append("| Akte | Status | passed | failed | skipped |")
    lines.append("| --- | --- | --- | --- | --- |")
    for r in with_rubric:
        s = r.stats
        status = "PASS" if r.all_passed else "FAIL"
        lines.append(f"| `{r.slug}` | {status} | {s['passed']} | {s['failed']} | {s['skipped']} |")
    lines.append("")
    failures = [(r, c) for r in with_rubric for c in r.checks if c.passed is False]
    if failures:
        lines.append("## Fehlende Checks")
        lines.append("")
        for r, c in failures:
            lines.append(f"- `{r.slug}` :: `{c.rubric_id}` ({c.check_type}): {c.detail}")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*", help="optional: konkrete Testakten-Slugs")
    ap.add_argument("--report", action="store_true",
                    help="Schreibt MD-Report nach EVAL_RESULTS.md")
    ap.add_argument("--json-out", help="Schreibt JSON-Snapshot fuer compare-eval-runs.py")
    ap.add_argument("--label", default="run", help="Label fuer den JSON-Snapshot (z. B. Modellname)")
    args = ap.parse_args()

    if args.slugs:
        slugs = args.slugs
    else:
        slugs = sorted(d.name for d in TESTAKTEN.iterdir() if d.is_dir())

    results = [evaluate_akte(s) for s in slugs]

    # Konsolen-Output
    rubric_count = sum(1 for r in results if r.has_rubric)
    pass_count = sum(1 for r in results if r.has_rubric and r.all_passed)
    fail_count = sum(1 for r in results if r.has_rubric and not r.all_passed)
    print(f"Testakten: {len(results)} | mit Rubric: {rubric_count} | "
          f"All-Pass: {pass_count} | Fail: {fail_count}")
    for r in results:
        if not r.has_rubric:
            continue
        st = r.stats
        marker = "PASS" if r.all_passed else "FAIL"
        print(f"  [{marker}] {r.slug}  ({st['passed']}/{st['passed']+st['failed']} pass, "
              f"{st['skipped']} skip)")

    if args.report:
        report = render_report(results)
        (REPO / "EVAL_RESULTS.md").write_text(report, encoding="utf-8")
        print(f"Report geschrieben: EVAL_RESULTS.md")

    if args.json_out:
        snapshot = {
            "label": args.label,
            "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "results": [
                {
                    "slug": r.slug,
                    "has_rubric": r.has_rubric,
                    "all_passed": r.all_passed,
                    "stats": r.stats,
                    "checks": [
                        {
                            "id": c.rubric_id,
                            "type": c.check_type,
                            "passed": c.passed,
                            "detail": c.detail,
                        }
                        for c in r.checks
                    ],
                }
                for r in results
            ],
        }
        Path(args.json_out).write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
        print(f"JSON-Snapshot: {args.json_out}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
