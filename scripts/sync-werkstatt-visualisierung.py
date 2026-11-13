#!/usr/bin/env python3
"""Synchronisiert fachliche Oberflächenführung ohne bestehende Fachtexte zu ersetzen.

Ohne --write nur Drift prüfen. --record-review bindet ausschließlich die hier
geprüfte, byteerhaltende Ergänzung an bestehende redaktionelle Dateiprüfungen.
Es erneuert keine Rechtsquellenprüfung und behauptet keinen Live-Modelllauf.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re

from prompt_profiles import enabled, formats, standalone_kinds
import werkstatt_visualisierung as visual

ROOT = Path(__file__).resolve().parents[1]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def output_path(root: Path, path: Path) -> Path:
    """Ausgaben bleiben im kanonischen Repo und folgen keinen Dateiverknüpfungen."""
    resolved = path.resolve()
    if not resolved.is_relative_to(root) or path.is_symlink():
        raise ValueError(f"Verknüpfter oder außerhalb liegender Ausgabepfad: {path}")
    for parent in path.parents:
        if parent.resolve() == root:
            break
        if parent.is_symlink():
            raise ValueError(f"Verknüpfter Ausgabeordner: {parent}")
    return resolved


def prompt_inventory():
    spec = importlib.util.spec_from_file_location("visual_prompt_inventory", ROOT / "scripts/audit-prompt-profile-routing.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.expected_prompt_files


def plan(root: Path = ROOT, profiles: dict | None = None) -> tuple[dict[Path, bytes], dict]:
    root = root.resolve()
    profiles = visual.load_profiles() if profiles is None else profiles
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))["plugins"]
    if set(profiles) != {p["name"] for p in market}:
        raise ValueError("Visualisierungsprofile decken den Marketplace nicht exakt ab")
    expected_prompts = prompt_inventory()
    outputs = {}
    report = {"schema_version": 1, "method": "desk_review", "plugins": {}}
    for plugin in market:
        slug = plugin["name"]
        directory = (root / plugin["source"]).resolve()
        if not directory.is_relative_to(root):
            raise ValueError(f"Pluginquelle außerhalb des Repositories: {slug}")
        entry = profiles[slug]
        if entry["mode"] not in {"app", "prompt"} or not 1 <= len(entry["entry_skills"]) <= 3:
            raise ValueError(f"Ungültiger Einstieg: {slug}")
        if len(set(entry["entry_skills"])) != len(entry["entry_skills"]) or any(
            not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) for name in entry["entry_skills"]
        ):
            raise ValueError(f"Ungültige oder doppelte Einstiegsskills: {slug}")
        if (entry["mode"] == "app") != (not standalone_kinds(slug)):
            raise ValueError(f"App-/Prompt-Grenze stimmt nicht: {slug}")
        visual.family(entry["theme"])
        rows = []
        paths = [(directory / "skills" / name / "SKILL.md", "skill") for name in entry["entry_skills"]]
        prompt_paths = expected_prompts(slug, directory)
        paths += [(p, "workshop") for kind, p in prompt_paths.items() if kind.startswith("werkstatt")]
        focus = directory / f"{slug}-hauptproblem.md"
        if enabled(slug, "hauptproblem") and focus.is_file():
            prompt_paths["hauptproblem"] = focus
        # Kurz- und Schwerpunktprompts behalten ihr verbindliches 7.500-Byte-Budget.
        # Die ausführliche Oberflächenführung liegt in Werkstatt und Hauptskill.
        for kind in ("schnellstart", "hauptproblem"):
            if kind not in prompt_paths:
                continue
            path = output_path(root, prompt_paths[kind])
            if not path.is_file():
                raise ValueError(f"Veröffentlichter Kurzprompt fehlt: {path}")
            content = visual.remove_block(path.read_bytes().decode("utf-8")).encode("utf-8")
            outputs[path] = content
            if "txt" in formats(slug) and kind in standalone_kinds(slug):
                outputs[output_path(root, path.with_suffix(".txt"))] = content
        mega = root / "testakten/megaprompts" / f"{slug}.md"
        if enabled(slug, "megaprompt") and mega.is_file():
            paths.append((mega, "workshop"))
        for path, kind in paths:
            path = output_path(root, path)
            if not path.is_file() or path.is_symlink():
                raise ValueError(f"Fehlender oder verknüpfter Zielpfad: {path}")
            before = path.read_bytes()
            text = before.decode("utf-8")
            after = visual.block(text, slug, kind=kind, profiles=profiles).encode("utf-8")
            if visual.remove_block(after.decode("utf-8")) != visual.remove_block(text):
                raise ValueError(f"Fachtext außerhalb der Ergänzung verändert: {path}")
            outputs[path] = after
            rows.append({"path": path.relative_to(root).as_posix(), "kind": kind,
                         "preserved_body_sha256": sha(visual.remove_block(text).encode("utf-8")),
                         "sha256": sha(after)})
            if kind == "workshop" and path.parent == directory and "txt" in formats(slug):
                # Nur tatsächlich publizierte Standalone-Kopien, keine neuen Nebenformate.
                relative_kind = path.stem.removeprefix(slug + "-")
                if relative_kind in standalone_kinds(slug):
                    outputs[output_path(root, path.with_suffix(".txt"))] = after
        ref = directory / "references" / visual.REFERENCE
        outputs[output_path(root, ref)] = visual.reference(slug, entry).encode("utf-8")
        report["plugins"][slug] = {**entry, "family": visual.family_for(slug, entry["theme"]), "files": rows}
    return outputs, report


def reviewed_profiles(root: Path, outputs: dict[Path, bytes]) -> dict[Path, bytes]:
    """Nur bestehende, exakt passende Hashbindungen für den Zusatz fortschreiben."""
    root = root.resolve()
    canonical_outputs = {}
    for path, content in outputs.items():
        target = output_path(root, path)
        if target in canonical_outputs and canonical_outputs[target] != content:
            raise ValueError(f"Widersprüchliche Ausgaben für denselben Pfad: {path}")
        canonical_outputs[target] = content
    outputs = canonical_outputs
    updates = {}
    for path in sorted((root / "quality/evals").glob("*.json")):
        path = output_path(root, path)
        profile = json.loads(path.read_text(encoding="utf-8"))
        slug = profile.get("plugin")
        entry = visual.load_profiles().get(slug)
        if not entry:
            continue
        affected = []
        pending = []

        def advance(holder, key, target):
            if not target.is_file() or target not in outputs or outputs[target] == target.read_bytes():
                return
            old = sha(target.read_bytes())
            if holder.get(key) != old:
                pending.append(target.relative_to(root).as_posix())
                return
            holder[key] = sha(outputs[target])
            affected.append(target.relative_to(root).as_posix())

        mapping = json.loads((root / ".claude-plugin/marketplace.json").read_text())["plugins"]
        source = next(p["source"] for p in mapping if p["name"] == slug)
        directory = (root / source).resolve()
        for kind, key in (("werkstatt", "workshop_review"), ("schnellstart", "mini_review")):
            if key in profile:
                advance(profile[key], "sha256", directory / f"{slug}-{kind}.md")
        focus = profile.get("focus_review", {})
        for kind in ("prompt", "skill"):
            if focus.get(f"{kind}_path"):
                advance(focus, f"{kind}_sha256", (root / focus[f"{kind}_path"]).resolve())
        for field in ("skill_hashes", "reviewed_file_hashes", "artifact_hashes"):
            for name in profile.get(field, {}):
                advance(profile[field], name, (root / name).resolve())
        if affected:
            profile["visual_workflow_review"] = {
                "method": "desk_review", "date": "2026-11-13",
                "scope": "Fachlich zugeordnete Visualisierungsführung, belegte Auswahl und Fortsetzung; Fachtext außerhalb des Zusatzes bytegleich.",
                "files": sorted(set(affected) | set(profile.get("visual_workflow_review", {}).get("files", []))),
                "limits": "Keine erneute Rechtsquellenverifikation und kein Live-Modelltest. Bereits offene Prüfungen bleiben offen.",
                "pending_prior_changes": sorted(set(pending)),
            }
            updates[path] = (json.dumps(profile, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return updates


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--record-review", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    if args.write and args.check or args.record_review and not args.write:
        parser.error("--write/--check sind alternativ; --record-review benötigt --write")
    outputs, report = plan()
    if args.record_review:
        outputs.update(reviewed_profiles(ROOT, outputs))
    changed = [p for p, data in outputs.items() if not p.is_file() or p.read_bytes() != data]
    if args.write:
        for path in changed:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(outputs[path])
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Visualisierungsführung: {len(report['plugins'])} Plugins, {len(outputs)} Dateien, {len(changed)} {'geschrieben' if args.write else 'abweichend'}")
    if changed and not args.write:
        for path in changed[:15]:
            print(path.relative_to(ROOT))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
