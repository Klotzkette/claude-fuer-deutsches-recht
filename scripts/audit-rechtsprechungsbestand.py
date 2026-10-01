#!/usr/bin/env python3
"""Inventar und Änderungsabgleich; kein Nachweis juristischer Richtigkeit."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / "quality/source-audits/2026-09-25"
DOCKET = re.compile(
    r"\b(?:[IVX]+\s+(?:ZR|ZB|ARZ|R|B)|\d+\s+(?:AZR|AZB|ABR|StR|BvR|BvL|BvE)|"
    r"B\s+\d+\s+[A-Z]{1,4})\s+\d+/\d{2}(?:\s+R\b)?|"
    r"\b[CT][–-]\d+/\d{2}\b|\b\d+\s+[CBF]\s+\d+\.\d{2}\b"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-files", action="store_true", help="Vollständige Dateiliste für lokale Detailanalyse einschließen")
    parser.add_argument("--baseline-inventory", type=Path, help="Früheres bestand.json statt der Ausgangssnapshots vom 25.09.2026 vergleichen")
    args = parser.parse_args()
    if args.baseline_inventory:
        previous = json.loads(args.baseline_inventory.read_text())["plugins"]
        old_profiles = {x["plugin"]: {"sha256": x["profile_sha256"]} for x in previous}
        old_prompts = {x["path"]: x for plugin in previous for x in plugin["prompt_files"]}
        baseline_label = args.baseline_inventory.as_posix()
    else:
        old_profiles = {x["plugin"]: x for x in json.loads((BASELINE / "profile-snapshot.json").read_text())}
        old_prompts = {x["path"]: x for x in json.loads((BASELINE / "prompt-snapshot.json").read_text())}
        baseline_label = "2026-09-25"
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    rows = []
    for plugin in sorted(market["plugins"], key=lambda x: x["name"]):
        slug = plugin["name"]
        directory = ROOT / plugin["source"].removeprefix("./")
        files = set(directory.glob("*-werkstatt.md")) | set(directory.glob("*-schnellstart.md")) | set(directory.glob("*-hauptproblem.md"))
        for folder in (directory / "skills", directory / "references"):
            if folder.exists():
                files.update(folder.rglob("*.md"))
        mega = ROOT / "testakten/megaprompts" / (slug + ".md")
        if mega.exists():
            files.add(mega)
        file_rows = []
        dockets = set()
        for path in sorted(files):
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            found = sorted({re.sub(r"\s+", " ", m.group()).replace("–", "-") for m in DOCKET.finditer(text)})
            dockets.update(found)
            sha = digest(path)
            baseline = old_prompts.get(relative)
            file_rows.append({"path": relative, "sha256": sha, "dockets_detected": found,
                              "baseline_comparison": ("unchanged" if baseline["sha256"] == sha else "changed") if baseline else "not_in_prompt_baseline"})
        profile_path = ROOT / "quality/evals" / (slug + ".json")
        profile = json.loads(profile_path.read_text())
        sha = digest(profile_path)
        old = old_profiles.get(slug)
        decisions = profile.get("prompt_editorial_review", {}).get("decisions", [])
        rows.append({"plugin": slug, "directory": directory.relative_to(ROOT).as_posix(),
                     "profile_sha256": sha,
                     "profile_baseline_comparison": ("unchanged" if old["sha256"] == sha else "changed") if old else "new",
                     "profile_anchors": decisions,
                     "profile_anchors_dated_2026": [d for d in decisions if re.search(r"(?:\d{2}\.\d{2}\.2026|\d+\.\s+\w+\s+2026)", d.get("citation", ""))],
                     "files_scanned": len(files), "unique_dockets_detected": sorted(dockets),
                     "file_inventory_sha256": hashlib.sha256(json.dumps(file_rows, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
                     "prompt_files": [f for f in file_rows if "/skills/" not in f["path"] and "/references/" not in f["path"]],
                     **({"files": file_rows} if args.include_files else {})})
    data = {"method": "automated_inventory_and_baseline_diff_not_legal_verification",
            "baseline": baseline_label, "plugin_count": len(rows),
            "file_count": sum(x["files_scanned"] for x in rows),
            "limits": "Aktenzeichen-Erkennung ist heuristisch; weder Vollständigkeit noch Gültigkeit oder Entscheidungsjahr folgen aus einem Treffer. Unveränderte Dateien behalten nur ihren früher dokumentierten Prüfstatus. Quellenprüfung und 2026-Recherche stehen getrennt in den Fachberichten.",
            "plugins": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"plugins": len(rows), "files": data["file_count"],
                      "profiles": {k: sum(x["profile_baseline_comparison"] == k for x in rows) for k in ("unchanged", "changed", "new")}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
