#!/usr/bin/env python3
"""Fuehrt die fallbezogenen Pass/Fail-Rubrics aller Testakten aus.

Eine fehlende oder strukturell unbrauchbare ``rubric.yaml`` ist ein harter
Fehler. Damit kann eine neue Testakte nicht mehr unbemerkt ohne fachliche
Regressionstests in ein Release gelangen.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
TESTAKTEN = REPO / "testakten"
SKIP_DIRS = {"megaprompts"}
CHECK_TYPES = {
    "file_exists",
    "text_contains",
    "regex_match",
    "file_count",
    "yaml_field_equals",
    "json_field_equals",
    "human_review",
}
REQUIRED_CHECK_FIELDS = {
    "file_exists": {"path"},
    "text_contains": {"path", "contains"},
    "regex_match": {"path", "pattern"},
    "file_count": {"glob", "min"},
    "yaml_field_equals": {"path", "field", "equals"},
    "json_field_equals": {"path", "field", "equals"},
    "human_review": {"note"},
}
ALLOWED_PLUGINS = {
    "vergabestelle-behoerden",
    "bieter-unternehmen",
    "konkurrenten-rechtsschutz",
    "rollenverbund",
}


@dataclass
class CheckResult:
    rubric_id: str
    check_type: str
    description: str
    passed: bool | None
    detail: str = ""


@dataclass
class AktenResult:
    slug: str
    has_rubric: bool
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def all_passed(self) -> bool:
        decided = [check for check in self.checks if check.passed is not None]
        return bool(decided) and all(check.passed for check in decided)

    @property
    def stats(self) -> dict[str, int]:
        return {
            "passed": sum(check.passed is True for check in self.checks),
            "failed": sum(check.passed is False for check in self.checks),
            "skipped": sum(check.passed is None for check in self.checks),
        }


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_scalar(raw: str) -> Any:
    value = raw.strip().strip('"').strip("'")
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    """Liest YAML; der Fallback deckt das flache Rubric-Format ab."""
    try:
        import yaml  # type: ignore

        try:
            loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            raise ValueError(f"ungueltiges YAML in {path.name}: {exc}") from exc
        return loaded if isinstance(loaded, dict) else {}
    except ImportError:
        result: dict[str, Any] = {"checks": []}
        current: dict[str, Any] | None = None
        in_checks = False
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            stripped = raw_line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped == "checks:":
                in_checks = True
                continue
            if in_checks and stripped.startswith("- id:"):
                current = {"id": parse_scalar(stripped.split(":", 1)[1])}
                result["checks"].append(current)
                continue
            if in_checks and current is not None and ":" in stripped:
                key, value = stripped.split(":", 1)
                current[key.strip()] = parse_scalar(value)
                continue
            if not in_checks and ":" in stripped:
                key, value = stripped.split(":", 1)
                result[key.strip()] = parse_scalar(value)
        return result


def safe_target(akte_dir: Path, raw: str) -> Path:
    target = (akte_dir / raw).resolve()
    try:
        target.relative_to(akte_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"Pfad verlaesst die Testakte: {raw}") from exc
    return target


def nested_value(data: Any, dotted_field: str) -> Any:
    value = data
    for part in dotted_field.split("."):
        if isinstance(value, dict) and part in value:
            value = value[part]
        elif isinstance(value, list) and part.isdigit() and int(part) < len(value):
            value = value[int(part)]
        else:
            raise KeyError(dotted_field)
    return value


def markdown_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("YAML-Frontmatter fehlt")
    raw = text.split("---", 2)[1]
    try:
        import yaml  # type: ignore
    except ImportError:
        value = {
            key.strip(): parse_scalar(raw_value)
            for line in raw.splitlines()
            if ":" in line
            for key, raw_value in [line.split(":", 1)]
        }
    else:
        try:
            value = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            raise ValueError(f"ungueltiges YAML-Frontmatter in {path.name}: {exc}") from exc
    return value if isinstance(value, dict) else {}


def validate_rubric(rubric: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(rubric.get("name"), str) or not rubric["name"].strip():
        errors.append("name fehlt")
    plugin = rubric.get("plugin")
    if plugin not in ALLOWED_PLUGINS:
        errors.append(f"plugin ungueltig: {plugin!r}")
    checks = rubric.get("checks")
    if not isinstance(checks, list):
        return errors + ["checks ist keine Liste"]
    ids: set[str] = set()
    automated = 0
    for number, check in enumerate(checks, start=1):
        if not isinstance(check, dict):
            errors.append(f"Check {number} ist kein Objekt")
            continue
        cid = check.get("id")
        ctype = check.get("check_type")
        if not isinstance(cid, str) or not cid:
            errors.append(f"Check {number}: id fehlt")
        elif cid in ids:
            errors.append(f"Check-ID doppelt: {cid}")
        else:
            ids.add(cid)
        if ctype not in CHECK_TYPES:
            errors.append(f"{cid or number}: unbekannter check_type {ctype!r}")
            continue
        if ctype != "human_review":
            automated += 1
        missing = REQUIRED_CHECK_FIELDS[ctype] - check.keys()
        if missing:
            errors.append(f"{cid or number}: Pflichtfelder fehlen: {', '.join(sorted(missing))}")
        if not isinstance(check.get("description"), str) or not check["description"].strip():
            errors.append(f"{cid or number}: description fehlt")
    if automated < 5:
        errors.append(f"nur {automated} automatisierte Checks; mindestens 5 erforderlich")
    return errors


def run_check(akte_dir: Path, check: dict[str, Any]) -> CheckResult:
    cid = str(check.get("id", "?"))
    ctype = str(check.get("check_type", "?"))
    desc = str(check.get("description", ""))

    def result(passed: bool | None, detail: str) -> CheckResult:
        return CheckResult(cid, ctype, desc, passed, detail)

    try:
        if ctype == "file_exists":
            target = safe_target(akte_dir, str(check["path"]))
            return result(target.is_file(), f"{'gefunden' if target.is_file() else 'fehlt'}: {check['path']}")

        if ctype in {"text_contains", "regex_match"}:
            target = safe_target(akte_dir, str(check["path"]))
            if not target.is_file():
                return result(False, f"Datei fehlt: {check['path']}")
            text = target.read_text(encoding="utf-8", errors="ignore")
            if ctype == "text_contains":
                needle = str(check["contains"])
                return result(needle in text, "Text gefunden" if needle in text else f"Text fehlt: {needle[:80]!r}")
            pattern = str(check["pattern"])
            matched = re.search(pattern, text, re.MULTILINE) is not None
            return result(matched, "Regex gefunden" if matched else f"Regex ohne Treffer: {pattern!r}")

        if ctype == "file_count":
            pattern = str(check["glob"])
            if Path(pattern).is_absolute() or ".." in Path(pattern).parts:
                return result(False, f"unsicheres Glob-Muster: {pattern}")
            count = sum(1 for path in akte_dir.glob(pattern) if path.is_file())
            minimum = int(check["min"])
            return result(count >= minimum, f"{count} Dateien; mindestens {minimum} verlangt")

        if ctype in {"yaml_field_equals", "json_field_equals"}:
            target = safe_target(akte_dir, str(check["path"]))
            if not target.is_file():
                return result(False, f"Datei fehlt: {check['path']}")
            if ctype == "json_field_equals":
                data = json.loads(target.read_text(encoding="utf-8"))
            elif target.suffix.lower() == ".md":
                data = markdown_frontmatter(target)
            else:
                data = load_yaml(target)
            actual = nested_value(data, str(check["field"]))
            expected = check["equals"]
            return result(actual == expected, f"Ist {actual!r}; erwartet {expected!r}")

        if ctype == "human_review":
            return result(None, str(check["note"]))
    except (OSError, ValueError, KeyError, TypeError, re.error, json.JSONDecodeError) as exc:
        return result(False, f"Check konnte nicht ausgefuehrt werden: {exc}")

    return result(False, f"unbekannter check_type: {ctype}")


def evaluate_akte(slug: str) -> AktenResult:
    akte_dir = TESTAKTEN / slug
    result = AktenResult(slug=slug, has_rubric=False)
    if not akte_dir.is_dir():
        result.checks.append(CheckResult("rubric-akte", "schema", "Testakte existiert", False, "Ordner fehlt"))
        return result
    rubric_path = akte_dir / "rubric.yaml"
    if not rubric_path.is_file():
        result.checks.append(CheckResult("rubric-fehlt", "schema", "Rubric vorhanden", False, "rubric.yaml fehlt"))
        return result
    result.has_rubric = True
    try:
        rubric = load_yaml(rubric_path)
    except (OSError, ValueError) as exc:
        result.checks.append(CheckResult("rubric-lesbar", "schema", "Rubric lesbar", False, str(exc)))
        return result
    schema_errors = validate_rubric(rubric)
    for number, error in enumerate(schema_errors, start=1):
        result.checks.append(CheckResult(f"rubric-schema-{number}", "schema", "Rubric-Schema", False, error))
    if schema_errors:
        return result
    for check in rubric["checks"]:
        result.checks.append(run_check(akte_dir, check))
    return result


def render_report(results: list[AktenResult]) -> str:
    lines = ["# Eval-Results", "", f"Stand: {utc_now()}", ""]
    with_rubric = [result for result in results if result.has_rubric]
    all_pass = [result for result in results if result.all_passed]
    lines.extend([
        f"- Testakten gesamt: {len(results)}",
        f"- mit Rubric: {len(with_rubric)}",
        f"- All-Pass: {len(all_pass)}",
        "",
        "## Detail pro Akte",
        "",
        "| Akte | Rubric | Status | bestanden | fehlgeschlagen | manuell |",
        "| --- | --- | --- | ---: | ---: | ---: |",
    ])
    for result in results:
        stats = result.stats
        lines.append(
            f"| `{result.slug}` | {'ja' if result.has_rubric else 'nein'} | "
            f"{'PASS' if result.all_passed else 'FAIL'} | {stats['passed']} | "
            f"{stats['failed']} | {stats['skipped']} |"
        )
    failures = [(result, check) for result in results for check in result.checks if check.passed is False]
    if failures:
        lines.extend(["", "## Fehler", ""])
        lines.extend(
            f"- `{result.slug}` / `{check.rubric_id}`: {check.detail}"
            for result, check in failures
        )
    return "\n".join(lines) + "\n"


def discover_slugs() -> list[str]:
    return sorted(
        path.name for path in TESTAKTEN.iterdir()
        if path.is_dir() and path.name not in SKIP_DIRS
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slugs", nargs="*", help="konkrete Testakten-Slugs")
    parser.add_argument("--report", action="store_true", help="EVAL_RESULTS.md schreiben")
    parser.add_argument("--json-out", help="JSON-Snapshot fuer compare-eval-runs.py")
    parser.add_argument("--label", default="run", help="Label fuer den JSON-Snapshot")
    args = parser.parse_args()

    slugs = args.slugs or discover_slugs()
    results = [evaluate_akte(slug) for slug in slugs]
    failures = [result for result in results if not result.all_passed]
    print(
        f"Testakten: {len(results)} | mit Rubric: {sum(r.has_rubric for r in results)} | "
        f"All-Pass: {len(results) - len(failures)} | Fail: {len(failures)}"
    )
    for result in results:
        stats = result.stats
        print(
            f"  [{'PASS' if result.all_passed else 'FAIL'}] {result.slug} "
            f"({stats['passed']}/{stats['passed'] + stats['failed']} pass, {stats['skipped']} manuell)"
        )

    if args.report:
        (REPO / "EVAL_RESULTS.md").write_text(render_report(results), encoding="utf-8")
        print("Report geschrieben: EVAL_RESULTS.md")
    if args.json_out:
        snapshot = {
            "label": args.label,
            "timestamp": utc_now(),
            "results": [
                {
                    "slug": result.slug,
                    "has_rubric": result.has_rubric,
                    "all_passed": result.all_passed,
                    "stats": result.stats,
                    "checks": [
                        {
                            "id": check.rubric_id,
                            "type": check.check_type,
                            "passed": check.passed,
                            "detail": check.detail,
                        }
                        for check in result.checks
                    ],
                }
                for result in results
            ],
        }
        Path(args.json_out).write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON-Snapshot: {args.json_out}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
