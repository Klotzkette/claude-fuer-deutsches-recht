#!/usr/bin/env python3
"""Expliziter Integrationsplan für eine bereits geprüfte Skill-Migration.

Standard: nur Plan erstellen. --apply wendet einen vorher erzeugten Plan nach
vollständigem Vorhash-Abgleich an. Keine neue fachliche Reviewfreigabe, kein
Prüfdatum und kein needs_review-Status wird aus einer Pfadänderung abgeleitet.
"""
from __future__ import annotations

import argparse
import copy
import difflib
import json
import os
from pathlib import Path
import re
import runpy
import subprocess


ROOT = Path(__file__).resolve().parents[1]
ENGINE = runpy.run_path(str(Path(__file__).with_name("consolidate-skill-cap.py")))
sha = ENGINE["sha"]
file_sha = ENGINE["file_sha"]
json_bytes = ENGINE["json_bytes"]


def rewrite_maps(report: dict) -> tuple[dict, dict, dict]:
    files = report.get("files", []) + report.get("integration_inventory", [])
    paths = {r["original_path"]: r["path"] for r in files if r["original_path"] != r["path"]}
    owners = {(r["plugin"], r["old"]): r["new"] for r in report["migrations"]}
    sources = {r["name"]: r["source"] for r in report["plugins"]}
    return paths, owners, sources


def flatten_migrations(existing: list[dict], report: dict, repo: Path) -> list[dict]:
    paths, _, sources = rewrite_maps(report)
    sources = {**ENGINE["marketplace_sources"](repo), **sources}
    rows = existing + report["migrations"]
    edges = {}
    for row in rows:
        key = (row["plugin"], row["old"])
        if key in edges:
            raise ValueError(f"Doppelte historische Umstellung: {key}")
        edges[key] = row
    output = []
    for row in rows:
        plugin, old, intermediate = row["plugin"], row["old"], row["new"]
        source = Path(sources.get(plugin, plugin))
        skills = source / "skills"
        target, seen = intermediate, {old}
        first_reference = row.get("reference")
        reference_path = (skills / intermediate / first_reference) if first_reference else None
        while (plugin, target) in edges:
            if target in seen:
                raise ValueError(f"Zyklus in historischen Umstellungen: {plugin}/{old}")
            seen.add(target)
            next_row = edges[(plugin, target)]
            if reference_path is None:
                # Der ursprüngliche Zwischen-Skill bleibt jetzt als Fachtext
                # erhalten und ist präziser als ein unspezifischer Gesamtweg.
                old_skill_path = (skills / target / "SKILL.md").as_posix().removeprefix("./")
                if old_skill_path in paths:
                    reference_path = Path(paths[old_skill_path])
                elif next_row.get("reference"):
                    reference_path = skills / next_row["new"] / next_row["reference"]
            target = next_row["new"]
        if target == old:
            raise ValueError(f"Selbstbezug in historischen Umstellungen: {plugin}/{old}")
        result = {**row, "new": target}
        if reference_path is not None:
            normalized = os.path.normpath(reference_path).replace(os.sep, "/")
            normalized = paths.get(normalized, normalized)
            resolved = ENGINE["safe_path"](repo, normalized)
            plugin_root = ENGINE["safe_path"](repo, str(source))
            if not resolved.is_relative_to(plugin_root) or not resolved.is_file():
                raise ValueError(f"Historischer Fachnachweis fehlt oder verlässt das Plugin: {plugin}/{old}: {normalized}")
            result["reference"] = os.path.relpath(normalized, skills / target).replace(os.sep, "/")
        output.append(result)
    return sorted(output, key=lambda r: (r["plugin"], r["old"]))


def safe_review_binding(repo: Path, old_path: str, old_hash: str, records: dict) -> tuple[str, str, str | None]:
    """Nur exakt bewiesene Link-/Pfadänderungen übernehmen, keine Altprüfung heilen."""
    record = records.get(old_path)
    if record is None:
        return old_path, old_hash, None
    new_path = record["path"]
    if old_hash != record["original_sha256"]:
        return new_path, old_hash, "Vorhandene Reviewbindung passt nicht zum Vorher-Hash; Prüfung bleibt offen"
    path = ENGINE["safe_path"](repo, new_path)
    if not path.is_file() or file_sha(path) != record["sha256"]:
        return new_path, old_hash, "Aktuelle Datei ist nicht die exakt dokumentierte mechanische Transformation"
    try:
        restored = ENGINE["restore_original"](path.read_bytes(), record.get("edits", []))
    except ValueError:
        return new_path, old_hash, "Transformationsnachweis ist nicht invertierbar"
    if sha(restored) != old_hash:
        return new_path, old_hash, "Originaltext lässt sich aus dem Transformationsnachweis nicht bestätigen"
    return new_path, record["sha256"], None


def migrate_quality(profile: dict, repo: Path, report: dict) -> tuple[dict, list[dict], list[dict]]:
    value = copy.deepcopy(profile)
    paths, owners, sources = rewrite_maps(report)
    records = {r["original_path"]: r for r in report.get("files", []) + report.get("integration_inventory", [])}
    plugin = profile["plugin"]
    source = sources.get(plugin, ENGINE["marketplace_sources"](repo).get(plugin, plugin)).removeprefix("./")
    changes, pending = [], []

    def binding(node, path_field, hash_field, old_path, location):
        if not isinstance(node.get(hash_field), str):
            return
        new_path, new_hash, problem = safe_review_binding(repo, old_path, node[hash_field], records)
        if path_field:
            node[path_field] = new_path
        if problem:
            pending.append({"location": location, "path": old_path, "reason": problem,
                            "previous_sha256": node[hash_field]})
        elif node[hash_field] != new_hash or old_path != new_path:
            changes.append({"location": location, "old_path": old_path, "path": new_path,
                            "old_sha256": node[hash_field], "sha256": new_hash,
                            "scope": "Nur invertierbare Verweisänderung beziehungsweise Pfadwechsel; keine neue fachliche Prüfung"})
            node[hash_field] = new_hash

    def visit(node, location=""):
        if isinstance(node, list):
            for index, item in enumerate(node):
                visit(item, f"{location}/{index}")
            return
        if not isinstance(node, dict):
            return
        handled_hashes = set()
        bindings = []
        for path_field, hash_field in (("skill_path", "skill_sha256"), ("prompt_path", "prompt_sha256"),
                                       ("path", "sha256"), ("prompt_path", "sha256"), ("skill_path", "sha256")):
            if isinstance(node.get(path_field), str) and hash_field in node and hash_field not in handled_hashes:
                # Schwerpunktreviews führen sha256 als Prompt-Alias neben den
                # getrennten Prompt-/Skill-Hashes. Alle Originalpfade sichern,
                # bevor die erste Bindung einen davon mechanisch fortschreibt.
                bindings.append((path_field, hash_field, node[path_field]))
                handled_hashes.add(hash_field)
        for path_field, hash_field, original_path in bindings:
            binding(node, path_field, hash_field, original_path, location)
        for key, item in list(node.items()):
            if key in {"previous_hashes", "previous_reviews", "review_history", "history"} or re.search(r"_\d{4}_\d{2}_\d{2}$", key):
                # Historische Momentaufnahmen sind Belege des damaligen Standes,
                # keine aktive Hashbindung und keine neue offene Reviewaufgabe.
                continue
            if key == "target_skill" and isinstance(item, str) and (plugin, item) in owners:
                node[key] = owners[(plugin, item)]
                changes.append({"location": f"{location}/{key}", "old_target": item, "target": node[key],
                                "scope": "Bestehender Prüffall wird dem umfassenden Arbeitsweg zugeordnet; unveränderte Sollkriterien"})
            elif key == "files" and isinstance(item, list):
                node[key] = [paths.get(x, x) if isinstance(x, str) else x for x in item]
                visit(node[key], f"{location}/{key}")
            else:
                visit(item, f"{location}/{key}")

    for review_key, suffix in (("mini_review", "schnellstart"), ("workshop_review", "werkstatt")):
        if isinstance(value.get(review_key), dict):
            binding(value[review_key], None, "sha256", f"{source}/{plugin}-{suffix}.md", "/" + review_key)
    visit(value)
    # Ein früherer Review für einen demotierten Fachtext bescheinigt nicht die
    # Qualität des neuen Routers. Der bestehende Nachweis bleibt ausdrücklich
    # beim Fachinhalt, nicht unter den aktiven Skill-Reviews.
    if isinstance(value.get("skill_reviews"), list):
        active, archived = [], list(value.get("reference_reviews", []))
        for review in value["skill_reviews"]:
            if str(review.get("skill_path", "")).endswith("/FACHINHALT.md"):
                archived.append(review)
            else:
                active.append(review)
        value["skill_reviews"] = active
        if archived:
            value["reference_reviews"] = archived
    return value, changes, pending


def diff_record(path: str, before: bytes, after: bytes, kind: str) -> dict:
    old, new = before.decode("utf-8").splitlines(keepends=True), after.decode("utf-8").splitlines(keepends=True)
    old_offsets = [0]
    for line in old:
        old_offsets.append(old_offsets[-1] + len(line.encode("utf-8")))
    replacements = []
    for tag, i, j, a, b in difflib.SequenceMatcher(None, old, new, autojunk=True).get_opcodes():
        if tag != "equal":
            replacements.append((old_offsets[i], old_offsets[j], "".join(new[a:b]).encode("utf-8")))
    actual, edits = ENGINE["exact_edits"](before, replacements)
    if actual != after:
        raise AssertionError("Integrationsdelta stimmt nicht")
    return {"path": path, "kind": kind, "original_sha256": sha(before), "sha256": sha(after), "edits": edits}


def apply_record(before: bytes, record: dict) -> bytes:
    replacements = []
    for edit in record["edits"]:
        start = edit["before_offset"]
        old = ENGINE["edit_bytes"](edit, "before")
        if before[start:start + len(old)] != old:
            raise ValueError(f"Integrationsdelta passt nicht: {record['path']}")
        replacements.append((start, start + len(old), ENGINE["edit_bytes"](edit, "after")))
    after, _ = ENGINE["exact_edits"](before, replacements)
    if sha(after) != record["sha256"]:
        raise ValueError(f"Integrationsdelta erreicht nicht den geprüften Zielhash: {record['path']}")
    return after


def tracked_docs(repo: Path) -> list[Path]:
    result = subprocess.run(["git", "ls-files", "-z"], cwd=repo, capture_output=True)
    if result.returncode:
        return sorted(p for p in repo.rglob("*") if p.is_file() and p.suffix.lower() in ENGINE["DOC_SUFFIXES"])
    return sorted(repo / item.decode() for item in result.stdout.split(b"\0") if item and Path(item.decode()).suffix.lower() in ENGINE["DOC_SUFFIXES"])


def prepare_plan(repo: Path, report: dict) -> dict:
    errors = ENGINE["verify_source_map"](repo, report)
    if errors:
        raise ValueError("SourceMap vor Integration nicht gültig: " + "; ".join(errors[:8]))
    paths, owners, sources = rewrite_maps(report)
    covered = {r["path"] for r in report.get("files", []) + report.get("integration_inventory", [])}
    plan = {"schema_version": 1, "source_map_sha256": sha(json_bytes(report)), "files": [],
            "review_binding_changes": [], "pending_reviews": [], "unchanged_non_utf8_documents": []}
    for path in tracked_docs(repo):
        name = path.relative_to(repo).as_posix()
        if name in covered or name.startswith('quality/') or not path.is_file() or any(part in {".git", "node_modules", "__pycache__"} for part in path.parts):
            # Historische Prüfprotokolle und aufgezeichnete Anwendungsproben
            # bleiben Belege ihres damaligen Standes. Aktive JSON-Bindungen
            # werden unten gesondert und nur mit Hashnachweis behandelt.
            continue
        before = path.read_bytes()
        try:
            before.decode('utf-8')
        except UnicodeDecodeError as exc:
            if b'SKILL.md' in before or re.search(rb'/[a-z0-9-]+:[a-z0-9-]+', before):
                raise ValueError(f'Nicht-UTF8-Datei mit möglichem Skillverweis muss gesondert geprüft werden: {name}') from exc
            plan['unchanged_non_utf8_documents'].append({
                'path': name, 'sha256': sha(before),
                'reason': 'Originalkodierung bleibt unverändert; keine Skillpfade oder Skillaufrufe enthalten.',
            })
            continue
        after, edits = ENGINE["rewrite_document"](before, name, paths, owners, sources)
        if edits:
            plan["files"].append({"path": name, "kind": "global_document_links", "original_sha256": sha(before), "sha256": sha(after), "edits": edits})
    migration_file = repo / "scripts/skill-selection-migrations.json"
    if migration_file.is_file():
        before = migration_file.read_bytes()
        after = json_bytes(flatten_migrations(json.loads(before), report, repo))
        if before != after:
            plan["files"].append(diff_record("scripts/skill-selection-migrations.json", before, after, "flattened_migrations"))
    for path in sorted((repo / "quality/evals").glob("*.json")):
        before = path.read_bytes()
        profile = json.loads(before)
        after_profile, changes, pending = migrate_quality(profile, repo, report)
        if after_profile != profile:
            plan["files"].append(diff_record(path.relative_to(repo).as_posix(), before, json_bytes(after_profile), "quality_bindings"))
        plan["review_binding_changes"].extend({"profile": path.name, **item} for item in changes)
        plan["pending_reviews"].extend({"profile": path.name, **item} for item in pending)
    return plan


def apply_plan(repo: Path, plan: dict) -> None:
    changes = []
    seen = set()
    for record in plan["files"]:
        if record["path"] in seen:
            raise ValueError("Doppelte Datei im Integrationsplan")
        seen.add(record["path"])
        path = ENGINE["safe_path"](repo, record["path"])
        before = path.read_bytes()
        if sha(before) != record["original_sha256"]:
            raise ValueError(f"Datei seit Planerzeugung geändert: {record['path']}")
        changes.append((path, apply_record(before, record)))
    # Alle Vorbedingungen sind geprüft, bevor die erste Datei geschrieben wird.
    for path, after in changes:
        path.write_bytes(after)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--source-map", type=Path)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.apply:
        plan = json.loads(args.plan.read_text())
        apply_plan(args.repo.resolve(), plan)
        print(f"{len(plan['files'])} geprüfte Integrationsdateien aktualisiert; {len(plan['pending_reviews'])} zuvor offene Bindungen unverändert offen")
    else:
        if not args.source_map:
            parser.error("--source-map ist zum Planen erforderlich")
        plan = prepare_plan(args.repo.resolve(), json.loads(args.source_map.read_text()))
        args.plan.write_bytes(json_bytes(plan))
        print(f"Plan: {len(plan['files'])} Dateien; {len(plan['review_binding_changes'])} belegte Verweis-/Hashbindungen; {len(plan['pending_reviews'])} offene Altbindungen. Keine Repository-Datei geändert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
