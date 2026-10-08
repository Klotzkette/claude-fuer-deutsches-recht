#!/usr/bin/env python3
"""run-eval.py — Schlanker Eval-Harness für das Vorlagensammlung-Repo.

Liest pro Vorlage (<bereich>/<slug>/rubric.yaml) eine Liste von Pass/Fail-
Prüfungen ein, führt sie aus und schreibt einen All-Pass-Score nach
Harvey-LAB-Vorbild.

Verwendung:
    python3 scripts/run-eval.py                                    # alle Vorlagen
    python3 scripts/run-eval.py <bereich>/<slug>                   # gezielt
    python3 scripts/run-eval.py --report                           # MD-Report nach EVAL_RESULTS.md
    python3 scripts/run-eval.py --verbose                          # zusätzlich alle PASS-Zeilen
    python3 scripts/run-eval.py --json-out runs/labelA.json --label labelA

Prüfungstypen (rubric.yaml):
- file_exists          → Datei existiert
- text_contains        → Text-Substring kommt in Datei vor
- regex_match          → Regex matcht in Datei
- file_count           → Anzahl Dateien matches glob >= N
- yaml_field_equals    → YAML-Frontmatter-Feld hat erwarteten Wert
- json_field_equals    → JSON-Feld hat erwarteten Wert
- regex_absent         → Regex matcht NICHT (Negativ-Check, z. B. Umlaut-Hygiene)
- human_review         → Manuell zu bewerten (wird als 'skipped' gewertet)
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

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import vorlagenordner  # noqa: E402
from _atomar import text_atomar_schreiben  # noqa: E402

# Die Vorlagensammlung ist nach Fachbereichen organisiert. Eine Vorlage liegt
# unter <bereich>/<vorlagen-slug>/ und enthält mindestens
# <vorlagen-slug>.md sowie README.md.
# Themenordner werden anhand der gemeinsamen kanonischen Liste ausgewählt; alles
# andere im Repo-Root (scripts/, references/, templates/, .git, …) ist nicht
# Vorlagenträger.

SUPPORTED_CHECK_TYPES = frozenset({
    "file_exists",
    "text_contains",
    "regex_match",
    "file_count",
    "yaml_field_equals",
    "json_field_equals",
    "regex_absent",
    "human_review",
})

REQUIRED_CHECK_KEYS = {
    "file_exists": ("path",),
    "text_contains": ("path", "contains"),
    "regex_match": ("path", "pattern"),
    "file_count": ("glob", "min"),
    "yaml_field_equals": ("path", "field", "equals"),
    "json_field_equals": ("path", "field", "equals"),
    "regex_absent": ("path", "pattern"),
    "human_review": (),
}

_MISSING = object()


def discover_vorlagen() -> list[tuple[str, Path]]:
    """Liefert sortierte Liste (slug, ordner_pfad) aller Vorlagen.

    Der slug ist der relative Pfad `<bereich>/<vorlagen-slug>`, also der
    eindeutige Identifier innerhalb des Repos. Erkennungsmerkmal eines
    Vorlagen-Unterordners: er enthält eine sprechend benannte Markdown-Datei.
    """
    return [
        (ordner.relative_to(REPO).as_posix(), ordner)
        for ordner in vorlagenordner(REPO)
    ]


@dataclass
class CheckResult:
    rubric_id: str
    check_type: str
    description: str
    passed: bool | None  # None = skipped (human_review)
    detail: str = ""


@dataclass
class VorlagenResult:
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


def _yaml_scalar(raw_value: str) -> Any:
    stripped = raw_value.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in {'"', "'"}:
        return stripped[1:-1]
    value: Any = stripped
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if lowered in {"null", "none", "~"}:
        return None
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    return value


def _simple_rubric_yaml(text: str) -> dict:
    """Parst das flache, listenbasierte Rubric-Format ohne PyYAML."""
    result: dict = {"checks": []}
    current = None
    for line in text.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.lstrip().startswith("- id:"):
            current = {"id": _yaml_scalar(line.split(":", 1)[1])}
            result["checks"].append(current)
        elif line.startswith("  ") and current and ":" in line:
            key, value = line.strip().split(":", 1)
            current[key.strip()] = _yaml_scalar(value)
    return result


def load_yaml(path: Path) -> dict:
    """Minimal-Parser: nutzt PyYAML, fällt auf das Rubric-Format zurück."""
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
    except ImportError:
        return _simple_rubric_yaml(text)
    return yaml.safe_load(text) or {}


def _simple_yaml_mapping(text: str) -> dict[str, Any]:
    """Parst im PyYAML-freien CI einfache, eingerückte YAML-Mappings."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            raise ValueError(f"YAML-Liste in Zeile {number} wird ohne PyYAML nicht unterstützt")
        if ":" not in stripped:
            raise ValueError(f"ungültige YAML-Zeile {number}")
        indent = len(raw) - len(raw.lstrip(" "))
        key, raw_value = stripped.split(":", 1)
        key = key.strip().strip('"').strip("'")
        raw_value = raw_value.strip()
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if not raw_value:
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
            continue
        parent[key] = _yaml_scalar(raw_value)
    return root


def _yaml_data(text: str) -> Any:
    stripped = text.lstrip("\ufeff")
    if stripped.startswith("---"):
        lines = stripped.splitlines()
        try:
            closing = lines[1:].index("---") + 1
        except ValueError as exc:
            raise ValueError("YAML-Frontmatter besitzt keinen schließenden Trenner") from exc
        stripped = "\n".join(lines[1:closing])
    try:
        import yaml  # type: ignore
    except ImportError:
        return _simple_yaml_mapping(stripped)
    return yaml.safe_load(stripped)


def _field_value(data: Any, field_name: str) -> Any:
    value = data
    for part in field_name.split("."):
        if not isinstance(value, dict) or part not in value:
            return _MISSING
        value = value[part]
    return value


def validate_rubric(rubric: Any) -> list[str]:
    """Liefert Schemafehler, damit defekte Rubrics sichtbar fehlschlagen."""
    if not isinstance(rubric, dict):
        return ["Rubric-Wurzel muss ein Mapping sein"]
    checks = rubric.get("checks")
    if not isinstance(checks, list) or not checks:
        return ["Rubric muss eine nicht leere Liste 'checks' enthalten"]

    errors: list[str] = []
    seen_ids: set[str] = set()
    for index, check in enumerate(checks, start=1):
        prefix = f"Check {index}"
        if not isinstance(check, dict):
            errors.append(f"{prefix} muss ein Mapping sein")
            continue
        cid = check.get("id")
        if not isinstance(cid, str) or not cid.strip():
            errors.append(f"{prefix} besitzt keine nicht leere id")
        elif cid in seen_ids:
            errors.append(f"{prefix} verwendet die doppelte id {cid!r}")
        else:
            seen_ids.add(cid)
        ctype = check.get("check_type")
        if ctype not in SUPPORTED_CHECK_TYPES:
            errors.append(f"{prefix} verwendet unbekannten check_type {ctype!r}")
            continue
        if not isinstance(check.get("description"), str) or not check["description"].strip():
            errors.append(f"{prefix} besitzt keine nicht leere description")
        for key in REQUIRED_CHECK_KEYS[ctype]:
            if key not in check:
                errors.append(f"{prefix} ({cid or '?'}) benötigt das Feld {key!r}")
        for key in ("path", "glob"):
            if key not in check:
                continue
            value = check[key]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix} ({cid or '?'}) benötigt einen nicht leeren {key}")
            elif not _ist_sicherer_relativpfad(value):
                errors.append(
                    f"{prefix} ({cid or '?'}) verwendet einen unsicheren {key}: {value!r}"
                )
    return errors


def _ist_sicherer_relativpfad(raw: str) -> bool:
    """Erlaubt nur vorlageninterne POSIX-Pfade und Globmuster."""
    if not raw or "\\" in raw or re.match(r"^[A-Za-z]:", raw):
        return False
    pfad = Path(raw)
    return not pfad.is_absolute() and ".." not in pfad.parts


def _hat_symlinkkomponente(basis: Path, ziel: Path) -> bool:
    """Prüft den logischen Pfad, bevor ein Linkziel gelesen wird."""
    aktuell = basis
    try:
        teile = ziel.relative_to(basis).parts
    except ValueError:
        return True
    for teil in teile:
        aktuell = aktuell / teil
        if aktuell.is_symlink():
            return True
    return False


def _sicheres_ziel(vorlage_dir: Path, raw: str) -> Path:
    if not _ist_sicherer_relativpfad(raw):
        raise ValueError(f"Pfad verlässt den Vorlagenordner oder ist nicht portabel: {raw!r}")
    basis = vorlage_dir.resolve()
    ziel = vorlage_dir / raw
    if _hat_symlinkkomponente(vorlage_dir, ziel):
        raise ValueError(f"Pfad enthält einen symbolischen Link: {raw!r}")
    try:
        ziel.resolve(strict=False).relative_to(basis)
    except ValueError as exc:
        raise ValueError(f"Pfad verlässt den Vorlagenordner: {raw!r}") from exc
    return ziel


def _read(target: Path) -> str | None:
    if not target.is_file():
        return None
    # Für ODT/DOCX: ZIP-Inhalt entpacken und alle XML-Texte konkatenieren.
    if target.suffix.lower() in (".odt", ".docx"):
        import zipfile
        try:
            with zipfile.ZipFile(target, "r") as z:
                parts = []
                for name in z.namelist():
                    if name.endswith(".xml"):
                        try:
                            parts.append(z.read(name).decode("utf-8", errors="ignore"))
                        except Exception:
                            pass
                return "\n".join(parts)
        except zipfile.BadZipFile:
            return None
    return target.read_text(encoding="utf-8", errors="ignore")


def run_check(vorlage_dir: Path, check: dict) -> CheckResult:
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
        try:
            target = _sicheres_ziel(vorlage_dir, check["path"])
        except ValueError as exc:
            return fail(str(exc))
        if target.is_file():
            return ok(f"found {target.name}")
        return fail(f"missing {check['path']}")

    if ctype == "text_contains":
        try:
            target = _sicheres_ziel(vorlage_dir, check["path"])
        except ValueError as exc:
            return fail(str(exc))
        text = _read(target)
        if text is None:
            return fail(f"file missing: {check['path']}")
        needle = check.get("contains", "")
        return ok("substring found") if needle in text else fail(f"missing substring: {needle[:60]!r}")

    if ctype == "regex_match":
        try:
            target = _sicheres_ziel(vorlage_dir, check["path"])
        except ValueError as exc:
            return fail(str(exc))
        text = _read(target)
        if text is None:
            return fail(f"file missing: {check['path']}")
        pat = check.get("pattern", "")
        try:
            matched = re.search(pat, text, re.MULTILINE)
        except re.error as exc:
            return fail(f"invalid regex {pat!r}: {exc}")
        if matched:
            return ok("regex matched")
        return fail(f"regex did not match: {pat!r}")

    if ctype == "regex_absent":
        try:
            target = _sicheres_ziel(vorlage_dir, check["path"])
        except ValueError as exc:
            return fail(str(exc))
        text = _read(target)
        if text is None:
            return fail(f"file missing: {check['path']}")
        pat = check.get("pattern", "")
        try:
            m = re.search(pat, text, re.MULTILINE)
        except re.error as exc:
            return fail(f"invalid regex {pat!r}: {exc}")
        if m is None:
            return ok("regex absent (gut)")
        return fail(f"regex unerwartet getroffen: {m.group(0)[:80]!r}")

    if ctype == "file_count":
        pattern = check.get("glob", "*")
        min_count = int(check.get("min", 1))
        if not _ist_sicherer_relativpfad(pattern):
            return fail(f"Glob verlässt den Vorlagenordner oder ist nicht portabel: {pattern!r}")
        files: list[Path] = []
        for path in vorlage_dir.glob(pattern):
            if not path.is_file():
                continue
            try:
                _sicheres_ziel(vorlage_dir, path.relative_to(vorlage_dir).as_posix())
            except ValueError as exc:
                return fail(str(exc))
            files.append(path)
        if len(files) >= min_count:
            return ok(f"found {len(files)} files matching {pattern}")
        return fail(f"only {len(files)} files matching {pattern} (need {min_count})")

    if ctype in {"yaml_field_equals", "json_field_equals"}:
        try:
            target = _sicheres_ziel(vorlage_dir, check["path"])
        except ValueError as exc:
            return fail(str(exc))
        text = _read(target)
        if text is None:
            return fail(f"file missing: {check['path']}")
        try:
            data = _yaml_data(text) if ctype == "yaml_field_equals" else json.loads(text)
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            return fail(f"structured data invalid in {check['path']}: {exc}")
        field_name = str(check["field"])
        actual = _field_value(data, field_name)
        if actual is _MISSING:
            return fail(f"field missing: {field_name}")
        expected = check["equals"]
        if actual == expected:
            return ok(f"field {field_name} equals {expected!r}")
        return fail(f"field {field_name} is {actual!r}, expected {expected!r}")

    if ctype == "human_review":
        return skip(check.get("note", "manual review required"))

    return fail(f"unknown check_type: {ctype}")


def evaluate_vorlage(slug: str, vorlage_dir: Path) -> VorlagenResult:
    result = VorlagenResult(slug=slug, has_rubric=False)
    rubric_path = vorlage_dir / "rubric.yaml"
    if not rubric_path.is_file():
        return result
    result.has_rubric = True
    try:
        rubric = load_yaml(rubric_path)
    except Exception as exc:
        result.checks.append(CheckResult(
            "rubric-schema",
            "schema",
            "Rubric ist syntaktisch lesbar",
            False,
            f"{type(exc).__name__}: {exc}",
        ))
        return result
    schema_errors = validate_rubric(rubric)
    if schema_errors:
        result.checks.append(CheckResult(
            "rubric-schema",
            "schema",
            "Rubric erfüllt das deklarative Prüfschema",
            False,
            "; ".join(schema_errors),
        ))
        return result
    for check in rubric.get("checks", []):
        try:
            result.checks.append(run_check(vorlage_dir, check))
        except Exception as exc:
            result.checks.append(CheckResult(
                str(check.get("id", "?")),
                str(check.get("check_type", "?")),
                str(check.get("description", "")),
                False,
                f"Check konnte nicht ausgeführt werden: {type(exc).__name__}: {exc}",
            ))
    return result


def select_vorlagen(
    vorlagen: list[tuple[str, Path]],
    requested_slugs: list[str],
) -> list[tuple[str, Path]]:
    if not requested_slugs:
        return vorlagen
    wanted = set(requested_slugs)
    found = {slug for slug, _ in vorlagen}
    missing = sorted(wanted - found)
    if missing:
        raise ValueError("Unbekannte Vorlagen-Slugs: " + ", ".join(missing))
    return [(slug, path) for slug, path in vorlagen if slug in wanted]


def render_report(results: list[VorlagenResult]) -> str:
    lines = ["# Eval-Results", "", f"Stand: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}", ""]
    total = len(results)
    with_rubric = [r for r in results if r.has_rubric]
    without_rubric = [r for r in results if not r.has_rubric]
    all_pass = [r for r in with_rubric if r.all_passed]
    lines.append(f"- Vorlagen gesamt: **{total}**")
    lines.append(f"- mit Rubric: **{len(with_rubric)}**")
    lines.append(f"- ohne Rubric: **{len(without_rubric)}**")
    lines.append(f"- All-Pass (alle entschiedenen Checks bestanden, ohne human_review): **{len(all_pass)}**")
    lines.append("")
    if without_rubric:
        lines.append("## Fehlende Rubrics")
        lines.append("")
        for r in without_rubric:
            lines.append(f"- `{r.slug}`")
        lines.append("")
    lines.append("## Detail pro Vorlage (nur Vorlagen mit Rubric)")
    lines.append("")
    lines.append("| Vorlage | Status | passed | failed | skipped |")
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
        lines.append("")
    skipped = [(r, c) for r in with_rubric for c in r.checks if c.passed is None]
    if skipped:
        lines.append("## human_review (manuell zu prüfen)")
        lines.append("")
        for r, c in skipped:
            lines.append(f"- `{r.slug}` :: `{c.rubric_id}`: {c.description}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*",
                    help="optional: konkrete Vorlagen-Slugs (Form <bereich>/<slug>)")
    ap.add_argument("--report", action="store_true",
                    help="Schreibt MD-Report nach EVAL_RESULTS.md")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="Gibt zusätzlich jede erfolgreiche Vorlage aus")
    ap.add_argument("--json-out", help="Schreibt JSON-Snapshot für compare-eval-runs.py")
    ap.add_argument("--label", default="run", help="Label für den JSON-Snapshot (z. B. Modellname)")
    args = ap.parse_args(argv)

    try:
        all_vorlagen = select_vorlagen(discover_vorlagen(), args.slugs)
    except ValueError as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 2

    results = [evaluate_vorlage(s, p) for s, p in all_vorlagen]
    if not results:
        print("FEHLER: Keine Vorlagen entdeckt.", file=sys.stderr)
        return 1

    rubric_count = sum(1 for r in results if r.has_rubric)
    pass_count = sum(1 for r in results if r.has_rubric and r.all_passed)
    fail_count = sum(1 for r in results if not r.has_rubric or not r.all_passed)
    print(f"Vorlagen: {len(results)} | mit Rubric: {rubric_count} | "
          f"All-Pass: {pass_count} | Fail: {fail_count}")
    for r in results:
        if not r.has_rubric:
            print(f"  [FAIL] {r.slug}  (rubric.yaml fehlt)")
            continue
        if r.all_passed and not args.verbose:
            continue
        st = r.stats
        marker = "PASS" if r.all_passed else "FAIL"
        print(f"  [{marker}] {r.slug}  ({st['passed']}/{st['passed']+st['failed']} pass, "
              f"{st['skipped']} skip)")
        if not r.all_passed:
            for check in r.checks:
                if check.passed is False:
                    print(
                        f"    - {check.rubric_id} ({check.check_type}): {check.detail}"
                    )

    if args.report:
        report = render_report(results)
        text_atomar_schreiben(REPO / "EVAL_RESULTS.md", report)
        print("Report geschrieben: EVAL_RESULTS.md")

    if args.json_out:
        snapshot = {
            "label": args.label,
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
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
        out_path = Path(args.json_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        text_atomar_schreiben(
            out_path,
            json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n",
        )
        print(f"JSON-Snapshot: {args.json_out}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
