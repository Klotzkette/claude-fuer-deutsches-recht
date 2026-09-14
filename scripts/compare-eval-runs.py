#!/usr/bin/env python3
"""Vergleicht ausschließlich technische Prüfungen der Aktenstruktur.

Vergleicht zwei oder mehr Snapshots der EVAL_RESULTS.md (oder JSON-Logs aus
run-eval.py --json-out) und erzeugt eine Side-by-Side-Tabelle.

Verwendung:
    python3 scripts/run-eval.py --structural-only --json-out runs/vorher.json
    python3 scripts/compare-eval-runs.py runs/vorher.json runs/nachher.json

Für tatsächliche Modellergebnisse: quality-lab.py compare LAUFORDNER ...
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_run(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def render_comparison(runs: list[tuple[str, dict]]) -> str:
    lines = ["# 1. Vergleich der Aktenstruktur", "",
             "Diese Prüfung vergleicht Quelldateien, nicht erzeugte Arbeitsergebnisse. "
             "Offene fachliche Bewertungen sind kein bestandener Modelltest.", ""]
    lines.append("| Akte | " + " | ".join(label for label, _ in runs) + " | Delta |")
    lines.append("| --- |" + " --- |" * (len(runs) + 1))

    # Sammele Slugs aus allen Runs
    all_slugs: set[str] = set()
    for _, data in runs:
        for r in data.get("results", []):
            if r.get("has_rubric"):
                all_slugs.add(r["slug"])

    for slug in sorted(all_slugs):
        row = [f"`{slug}`"]
        scores = []
        for _, data in runs:
            res = next((r for r in data.get("results", []) if r["slug"] == slug), None)
            if res is None or not res.get("has_rubric"):
                row.append("—")
                scores.append(None)
                continue
            stats = res.get("stats", {})
            passed = stats.get("passed", 0)
            total = passed + stats.get("failed", 0)
            pending = stats.get("skipped", 0)
            row.append(f"{passed}/{total} technisch; {pending} offen")
            scores.append((passed, total))
        # Delta
        if all(s is not None for s in scores) and len(scores) >= 2:
            first = scores[0][0] / max(scores[0][1], 1)
            last = scores[-1][0] / max(scores[-1][1], 1)
            delta = last - first
            sign = "+" if delta > 0 else ""
            row.append(f"{sign}{delta*100:.0f} %-Punkte")
        else:
            row.append("—")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    # Summary
    lines.append("## 1.1 Zusammenfassung")
    lines.append("")
    for label, data in runs:
        results = [r for r in data.get("results", []) if r.get("has_rubric")]
        passed = sum(1 for r in results if r.get("all_passed"))
        lines.append(f"- {label}: {passed}/{len(results)} Akten ohne offene oder fehlgeschlagene Prüfung; kein Modellvergleich")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="+", help="Pfade zu JSON-Snapshots (run-eval.py --json-out)")
    ap.add_argument("--out", default="EVAL_COMPARISON.md")
    args = ap.parse_args()

    paths = [Path(p) for p in args.runs]
    if not all(p.is_file() for p in paths):
        missing = [p for p in paths if not p.is_file()]
        print(f"missing files: {missing}", file=sys.stderr)
        return 1

    labels_and_data = []
    for p in paths:
        data = load_run(p)
        labels_and_data.append((data.get("label", p.stem), data))

    report = render_comparison(labels_and_data)
    Path(args.out).write_text(report, encoding="utf-8")
    print(f"Comparison report: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
