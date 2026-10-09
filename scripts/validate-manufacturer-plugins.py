#!/usr/bin/env python3
"""Prüft Katalog und sämtliche eingetragenen Plugins mit der strikten Herstellerprüfung."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--executable", default="claude")
    args = parser.parse_args()
    executable = shutil.which(args.executable)
    if not executable:
        parser.error("Hersteller-Prüfprogramm fehlt; Prüfung wird nicht übersprungen.")
    market = ROOT / ".claude-plugin/marketplace.json"
    entries = json.loads(market.read_text(encoding="utf-8"))["plugins"]
    targets = [("Marketplace", market)] + [(p["name"], ROOT / p["source"]) for p in entries]
    failures = []
    for name, path in targets:
        try:
            result = subprocess.run([executable, "plugin", "validate", str(path), "--strict"],
                                    cwd=ROOT, capture_output=True, text=True, timeout=30)
            if result.returncode:
                failures.append(name)
                print(f"{name}: {result.stdout}\n{result.stderr}", flush=True)
        except subprocess.TimeoutExpired:
            failures.append(name)
            print(f"{name}: Zeitlimit der Prüfung überschritten", flush=True)
    print(f"Strikte Herstellerprüfung: {len(targets) - len(failures)}/{len(targets)} bestanden.")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
