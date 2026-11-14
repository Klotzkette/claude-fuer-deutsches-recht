#!/usr/bin/env python3
"""Nachgewiesene externe Paketverweise berichtigen, ohne Fachtexte umzuschreiben.

Zentrale Testakten und Recherchebestände bleiben im Repository; eigenständige
Prompts bleiben bei den bestehenden Pages-Downloads. Nur vorhandene Ziele
werden verlinkt. Jeder Eingriff bleibt aus der SourceMap bytegenau umkehrbar.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
from pathlib import Path
import runpy
from urllib.parse import quote, unquote

from prompt_profiles import PROMPT_SUFFIXES

ROOT = Path(__file__).resolve().parents[1]
I = runpy.run_path(str(Path(__file__).with_name("integrate-skill-cap.py")))
E = I["ENGINE"]
spec = importlib.util.spec_from_file_location("quality_release", Path(__file__).with_name("build-skill-quality-release.py"))
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
WEB = "https://github.com/Klotzkette/claude-fuer-deutsches-recht"
PAGES = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="


def destination_url(root: Path, directory: Path, path: Path, raw: str) -> str:
    raw_path, separator, anchor = raw.partition("#")
    target = (path.parent / unquote(raw_path)).resolve()
    if not target.is_relative_to(root) or not target.exists() or target.is_symlink():
        raise ValueError(f"Kein belegtes Repository-Ziel: {path.relative_to(root)} -> {raw}")
    relative = target.relative_to(root)
    if target.is_file() and target.name.endswith(PROMPT_SUFFIXES):
        return PAGES + quote(relative.as_posix(), safe="/") + separator + anchor
    local_parts = target.relative_to(directory).parts if target.is_relative_to(directory) else ()
    is_case = relative.parts[0] in {"testakten", "recherche", "quality"} or any(p in {"testakte", "testakten"} for p in local_parts)
    is_navigation = relative.as_posix() in {"README.md", "SKILLS.md", "ASSET_INDEX.md"}
    if not is_case and not is_navigation:
        raise ValueError(f"Paketabhängigkeit verlangt eigene Prüfung statt externen Ersatzlink: {path.relative_to(root)} -> {raw}")
    kind = "tree" if target.is_dir() else "blob"
    return f"{WEB}/{kind}/main/{quote(relative.as_posix(), safe='/')}" + separator + anchor


def file_plan(root: Path, directory: Path) -> list[dict]:
    files = B.source_files(root, directory)
    records = []
    for name, path in files.items():
        if path.suffix != ".md" or not name.startswith(("skills/", "references/")):
            continue
        before = path.read_bytes()
        text = before.decode("utf-8")
        replacements = []
        for match in E["LINK"].finditer(text):
            value = match["path"]
            bracketed = value.startswith("<")
            raw = value.strip("<>")
            target = raw.partition("#")[0]
            if not target or ":" in target or target.startswith("/"):
                continue
            local = os.path.normpath(os.path.join(os.path.dirname(name), unquote(target))).replace(os.sep, "/")
            if local in files or (not local.startswith("../") and any(n.startswith(local.rstrip("/") + "/") for n in files)):
                continue
            url = destination_url(root, directory, path, raw)
            new = f"<{url}>" if bracketed else url
            replacements.append((len(text[:match.start("path")].encode()), len(text[:match.end("path")].encode()), new.encode()))
        after, edits = E["exact_edits"](before, replacements)
        if edits:
            records.append({"path": path.relative_to(root).as_posix(), "kind": "verified_package_navigation",
                            "original_sha256": E["sha"](before), "sha256": E["sha"](after), "edits": edits})
    return records


def prepare(root: Path, source_map: dict, scope: dict | None = None) -> dict:
    failures = E["verify_source_map"](root, source_map)
    if failures:
        raise ValueError("SourceMap vor Fortschreibung ungültig: " + "; ".join(failures[:5]))
    files = []
    plugins = [{"name": p["name"], "source": p["source"]} for p in source_map["plugins"]]
    known = {p["name"] for p in plugins}
    sources = E["marketplace_sources"](root)
    for plugin in (scope or {}).get("plugins", []):
        if plugin["name"] not in known:
            plugins.append({"name": plugin["name"], "source": sources[plugin["name"]].removeprefix("./"), "additional_unchanged_plugin": True})
    for plugin in plugins:
        files.extend(file_plan(root, (root / plugin["source"]).resolve()))
    return {"schema_version": 1, "scope": "Nur vorhandene zentrale Belege und eigenständige Prompt-Downloads verlinken; keine fachliche Neubewertung",
            "source_map_before_sha256": E["sha"](E["json_bytes"](source_map)), "checked_plugins": plugins, "files": files}


def apply(root: Path, source_map: dict, plan: dict, audit_path: str) -> tuple[dict, dict]:
    if E["sha"](E["json_bytes"](source_map)) != plan["source_map_before_sha256"]:
        raise ValueError("SourceMap seit Planerzeugung geändert")
    updated = copy.deepcopy(source_map)
    records = {r["path"]: r for field in ("files", "integration_inventory", "shared_dependencies") for r in updated.get(field, [])}
    delta = {"files": [], "integration_inventory": [], "plugins": plan.get("checked_plugins", source_map["plugins"]), "migrations": []}
    # Vorbedingungen und kombinierte inverse Deltas komplett vor Schreibbeginn.
    for change in plan["files"]:
        path = E["safe_path"](root, change["path"])
        before = path.read_bytes()
        if E["sha"](before) != change["original_sha256"]:
            raise ValueError(f"Quelle seit Plan geändert: {change['path']}")
        after = I["apply_record"](before, change)
        record = records.get(change["path"])
        if record is None:
            extra = next((p for p in plan.get("checked_plugins", []) if p.get("additional_unchanged_plugin") and change["path"].startswith(p["source"] + "/")), None)
            if extra is None:
                raise ValueError(f"Paketquelle ist nicht in der ursprünglichen SourceMap: {change['path']}")
            record = {"original_path": change["path"], "path": change["path"],
                      "original_sha256": change["original_sha256"], "sha256": change["original_sha256"], "edits": [],
                      "preservation_phase": "additional_unchanged_plugin_package_link"}
            updated["files"].append(record)
        if record["sha256"] != change["original_sha256"]:
            raise ValueError(f"SourceMap-Endhash passt nicht zum Folgeeingriff: {change['path']}")
        original = E["restore_original"](before, record.get("edits", []))
        if E["sha"](original) != record["original_sha256"]:
            raise ValueError(f"Ursprünglicher Fachtext nicht rekonstruierbar: {change['path']}")
        combined = I["diff_record"](change["path"], original, after, "preserved_source")
        record["sha256"], record["edits"] = combined["sha256"], combined["edits"]
        delta["files"].append({"original_path": change["path"], **change})
    I["apply_plan"](root, plan)
    quality_changes, pending, quality_files = [], [], []
    for path in sorted((root / "quality/evals").glob("*.json")):
        before = path.read_bytes()
        profile = json.loads(before)
        result, changes, open_reviews = I["migrate_quality"](profile, root, delta)
        if result != profile:
            quality_files.append(I["diff_record"](path.relative_to(root).as_posix(), before, E["json_bytes"](result), "mechanically_verified_review_binding"))
        quality_changes.extend({"profile": path.name, **r} for r in changes)
        pending.extend({"profile": path.name, **r} for r in open_reviews)
    I["apply_plan"](root, {"files": quality_files})
    updated.setdefault("followups", []).append({"audit": audit_path, "kind": "package_navigation", "files": [r["path"] for r in plan["files"]]})
    failures = E["verify_source_map"](root, updated)
    if failures:
        raise ValueError("SourceMap nach Verweiskorrektur ungültig: " + "; ".join(failures[:5]))
    for plugin in plan.get("checked_plugins", updated["plugins"]):
        directory = (root / plugin["source"]).resolve()
        B.verify_reachability(B.source_files(root, directory))
    final = {**plan, "quality_files": quality_files, "review_binding_changes": quality_changes,
             "pending_reviews": pending, "isolated_package_link_errors": 0,
             "source_map_after_sha256": E["sha"](E["json_bytes"](updated))}
    return updated, final


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--source-map", type=Path, required=True)
    parser.add_argument("--scope", type=Path, help="Zusätzlich vorhandene unveränderte Plugins des Release-Scopes einbeziehen")
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    source_map = json.loads(args.source_map.read_text())
    if args.apply:
        source_map, plan = apply(root, source_map, json.loads(args.plan.read_text()), args.plan.resolve().relative_to(root).as_posix())
        args.source_map.write_bytes(E["json_bytes"](source_map))
    else:
        plan = prepare(root, source_map, json.loads(args.scope.read_text()) if args.scope else None)
    args.plan.parent.mkdir(parents=True, exist_ok=True)
    args.plan.write_bytes(E["json_bytes"](plan))
    print(f"{len(plan['files'])} Paketquellen {'nachgewiesen korrigiert; 0 isolierte Paketverweisfehler' if args.apply else 'zur exakten Linkkorrektur vorbereitet; keine Quelle geändert'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
