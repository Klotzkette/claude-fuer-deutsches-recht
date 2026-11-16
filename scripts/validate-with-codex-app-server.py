#!/usr/bin/env python3
"""Prüft den lokalen Marketplace und seine Skills mit der laufenden Codex-App-Laufzeit."""

import argparse
import json
from pathlib import Path
from queue import Empty, Queue
import shutil
import subprocess
import sys
from threading import Thread
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]


def audit(child, market_path, market):
    replies = Queue()

    def read_replies():
        try:
            for line in child.stdout:
                replies.put(json.loads(line))
        finally:
            replies.put(None)

    Thread(target=read_replies, daemon=True).start()

    def request(method, params, request_id=None):
        message = {"method": method, "params": params}
        if request_id is not None:
            message["id"] = request_id
        child.stdin.write(json.dumps(message) + "\n")
        child.stdin.flush()
        if request_id is None:
            return None
        deadline = monotonic() + 20
        while monotonic() < deadline:
            try:
                reply = replies.get(timeout=max(0, deadline - monotonic()))
            except Empty:
                break
            if reply is None:
                raise RuntimeError(f"Codex hat die Verbindung vor {method} beendet")
            if reply.get("id") == request_id:
                if "error" in reply:
                    raise RuntimeError(f"{method}: {reply['error']['message']}")
                return reply["result"]
        raise RuntimeError(f"Zeitlimit für {method} überschritten")

    runtime = request("initialize", {
        "clientInfo": {"name": "marketplace-pruefung", "version": "1"},
        "capabilities": {"experimentalApi": True},
    }, 1)
    request("initialized", {})
    catalogs = request("plugin/list", {"cwds": [str(ROOT)], "marketplaceKinds": ["local"]}, 2)
    matching = [row for row in catalogs["marketplaces"]
                if row["name"] == market["name"] and row.get("path") == str(market_path)]
    if len(matching) != 1:
        raise RuntimeError(f"Marketplace am erwarteten Pfad nicht eindeutig geladen: {market_path}")

    errors = [row["message"] for row in catalogs.get("marketplaceLoadErrors", [])
              if row.get("marketplacePath") == str(market_path)]
    expected_plugins = {row["name"] for row in market["plugins"]}
    actual_plugins = [row["name"] for row in matching[0]["plugins"]]
    if len(expected_plugins) != len(market["plugins"]):
        errors.append("Erwarteter Marketplace enthält doppelte Plugin-Namen")
    if len(actual_plugins) != len(expected_plugins) or set(actual_plugins) != expected_plugins:
        errors.append("Plugin-Liste weicht vom Marketplace ab")

    skill_count = 0
    for request_id, entry in enumerate(market["plugins"], 3):
        name = entry["name"]
        directory = (ROOT / entry["source"]).resolve()
        expected_skills = {f"{name}:{path.parent.name}": str(path.resolve())
                           for path in (directory / "skills").glob("*/SKILL.md")}
        detail = request("plugin/read", {"marketplacePath": str(market_path), "pluginName": name}, request_id)["plugin"]
        summary = detail["summary"]
        if summary.get("localVersion") != entry["version"]:
            errors.append(f"{name}: Codex meldet eine abweichende Pluginversion")
        if summary.get("source", {}).get("path") != str(directory):
            errors.append(f"{name}: Codex meldet eine abweichende Pluginquelle")
        if summary.get("availability") != "AVAILABLE":
            errors.append(f"{name}: Codex bietet das Plugin nicht an")
        actual_skills = {skill["name"]: skill.get("path")
                         for skill in detail["skills"] if skill["enabled"]}
        if actual_skills != expected_skills or len(actual_skills) != len(detail["skills"]):
            differences = sorted(key for key in actual_skills.keys() | expected_skills.keys()
                                 if actual_skills.get(key) != expected_skills.get(key))
            errors.append(f"{name}: Skillbestand weicht ab ({', '.join(differences) or 'doppelt oder deaktiviert'})")
        skill_count += len(actual_skills)

    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Codex-Ladeprüfung OK ({len(actual_plugins)} Plugins, {skill_count} Skills)")
    print(runtime["userAgent"])
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--executable", default="codex", help="Codex-CLI der zu prüfenden Installation")
    args = parser.parse_args()
    executable = shutil.which(args.executable)
    if not executable:
        parser.error("Codex-CLI fehlt. Die Ladeprüfung wird nicht übersprungen.")
    market_path = ROOT / ".claude-plugin/marketplace.json"
    try:
        market = json.loads(market_path.read_text(encoding="utf-8"))
        # Nur der Prüflauf behandelt das eigene Repository als vertrauenswürdig.
        # Die zwei Abfragen registrieren oder installieren keine Plugins.
        command = [executable, "app-server", "--stdio", "-c", "analytics.enabled=false",
                   "-c", f'projects.{json.dumps(str(ROOT), ensure_ascii=False)}.trust_level="trusted"']
        with subprocess.Popen(command, cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              text=True, encoding="utf-8") as child:
            try:
                return audit(child, market_path, market)
            finally:
                child.terminate()
                try:
                    child.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    child.kill()
    except (OSError, KeyError, RuntimeError, ValueError) as error:
        print(f"Codex-Ladeprüfung fehlgeschlagen: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
