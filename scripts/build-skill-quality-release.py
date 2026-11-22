#!/usr/bin/env python3
"""Begrenzte Qualitätsrunde: vorhandene Pluginformate und Prompt-Snapshots.

Keine Testakte wird erzeugt oder als Release-Asset mitveröffentlicht. Native
Plugins bleiben flach; bereits vorhandene portable Varianten behalten ihren
Plugin-Unterordner. Für die Paket-README wird die Navigation anhand des
Archivinhalts und des Quellcommits gesetzt. Alle übrigen Dateien bleiben bytegleich.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import zipfile

from package_edition import edition_routes, planned_links
from package_readme import render_readme
from prompt_profiles import PROMPT_SUFFIXES
from release_asset_common import expected_asset_metadata, read_checksums, sha256_file, write_checksums
from release_routing import PAKETPFLEGE_TAG, check_asset_limit, scoped_asset_url, validate_plugin_version
from release_rate_limits import require_download_budget
from skill_limits import MAX_ACTIVE_SKILLS_PER_PLUGIN

ROOT = Path(__file__).resolve().parents[1]
SCOPE = ROOT / "scripts/data/skill-quality-release-scope.json"
MANIFESTS = (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "plugin.json")
SKIP_PARTS = {".git", ".venv", "node_modules", "__pycache__", "testakte", "testakten"}
STAMP = (2026, 11, 14, 0, 0, 0)
SLUG = re.compile(r"[a-z0-9-]{1,64}\Z")
SKILL = re.compile(r"skills/[^/]+/SKILL\.md\Z")
LINK = re.compile(r"\]\(([^)\s]+)\)")
REPORT = "release-bestand.json"
CHECKSUMS = "checksums-sha256.txt"
HANDBOOK_ASSETS = {"ki-native-kanzlei-skills-handbuch.pdf", "ki-native-kanzlei-skills-einzelpdfs.zip"}
from anfechtung_werkstatt_contract import ASSETS as ANFECHTUNG_ASSETS, EVIDENCE as ANFECHTUNG_EVIDENCE


def load_module(filename: str):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECKS = load_module("validate-release-zips.py")


def package_path(name: str) -> bool:
    path = Path(name)
    return (not SKIP_PARTS.intersection(path.parts) and name != "CLAUDE.md"
            and path.name != ".DS_Store" and path.suffix != ".pyc"
            and not path.name.endswith(PROMPT_SUFFIXES))


def inventory(root: Path, names: list[str]) -> dict:
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entries = {p["name"]: p for p in market["plugins"]}
    plugins = []
    for name in sorted(names):
        entry = entries[name]
        directory = (root / entry["source"]).resolve()
        variants = ["native"]
        if scoped_asset_url(f"{name}-portable.zip", root=root):
            variants.append("portable")
        prompts = [f"{name}-{kind}.{ext}" for kind in ("werkstatt", "schnellstart", "hauptproblem")
                   for ext in ("md", "txt") if (directory / f"{name}-{kind}.{ext}").is_file()]
        plugins.append({"name": name, "variants": variants, "prompts": prompts,
                        "manifests": [path for path in MANIFESTS if (directory / path).is_file()]})
    return {"plugins": plugins, "assets": sum(len(p["variants"]) + len(p["prompts"]) for p in plugins) + 2}


def paketpflege_scope(tag: str, root: Path) -> dict:
    """Leitet eine Paketnachauflage aus den exakten ZIP-Routen am Quellcommit ab."""
    match = PAKETPFLEGE_TAG.fullmatch(tag)
    if not match:
        raise ValueError(f"Ungültiger Tag für eine Paketnachauflage: {tag}")
    routes = edition_routes(root, tag.rsplit("-v", 1)[0])
    routed = {asset for asset, (_, release) in routes.items() if release == tag}
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entries = {entry["name"]: entry for entry in marketplace["plugins"]}
    names = sorted(name for name in entries if name + ".zip" in routed)
    plugins = inventory(root, names)["plugins"]
    archived = set()
    for item in plugins:
        name = item["name"]
        if entries[name]["version"] != match[1]:
            raise ValueError(f"{name}: Versionsgruppe der Paketnachauflage stimmt nicht")
        for variant in item["variants"]:
            archived.add(name + ("-portable" if variant == "portable" else "") + ".zip")
        directory = root / entries[name]["source"]
        item["preserved_prompts"] = {prompt: sha256_file(directory / prompt) for prompt in item["prompts"]}
        item["prompts"] = []
    if not names or archived != routed:
        raise ValueError(f"{tag}: Native und zugehörige portable Pakete müssen vollständig zusammengehören")
    return {"schema_version": 1, "tag": tag, "version": match[1],
            "title": f"Plugin-Anleitungen und Downloads · Paketversion {match[1]}", "plugins": plugins}


def validate_scope(scope: dict, root: Path) -> dict[str, dict]:
    if scope.get("schema_version") != 1 or not re.fullmatch(r"\d+\.\d+\.\d+", str(scope.get("version", ""))):
        raise ValueError("Scope benötigt schema_version 1 und eine semantische Version")
    edition = PAKETPFLEGE_TAG.fullmatch(str(scope.get("tag", "")))
    if edition:
        if scope != paketpflege_scope(scope["tag"], root):
            raise ValueError("Paketnachauflage weicht von den registrierten Ausgaben oder Quellen ab")
    elif scope.get("tag") != f"qualitaetsrunde-v{scope['version']}":
        raise ValueError("Komponententag passt nicht zur Qualitätsrunde")
    if not isinstance(scope.get("plugins"), list) or not scope["plugins"]:
        raise ValueError("Expliziter nichtleerer Plugin-Scope erforderlich")
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entries = {p["name"]: p for p in market["plugins"]}
    seen, assets = set(), {REPORT, CHECKSUMS}
    for plugin in scope["plugins"]:
        name = plugin.get("name", "")
        if not SLUG.fullmatch(name) or name in seen or name not in entries:
            raise ValueError(f"Unbekanntes oder doppeltes Plugin im Scope: {name}")
        seen.add(name)
        variants = plugin.get("variants", [])
        if variants not in (["native"], ["native", "portable"]):
            raise ValueError(f"{name}: nur native und ausdrücklich vorhandene portable Variante zulässig")
        for variant in variants:
            asset = name + ("-portable" if variant == "portable" else "") + ".zip"
            if not edition and scoped_asset_url(asset, root=root) != f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{scope['tag']}/{asset}":
                raise ValueError(f"{asset}: exakte Komponentenroute fehlt")
            assets.add(asset)
        prompts = plugin.get("prompts")
        if not isinstance(prompts, list) or len(prompts) != len(set(prompts)):
            raise ValueError(f"{name}: konkrete eindeutige Prompt-Dateinamen erforderlich")
        for filename in prompts:
            if not re.fullmatch(re.escape(name) + r"-(?:werkstatt|schnellstart|hauptproblem)\.(?:md|txt)", filename):
                raise ValueError(f"{name}: unzulässiger Prompt-Snapshot {filename}")
            assets.add(filename)
        directory = (root / entries[name]["source"]).resolve()
        if not directory.is_relative_to(root.resolve()):
            raise ValueError(f"{name}: Quelle liegt außerhalb des Repositorys")
        actual_prompts = {f"{name}-{kind}.{ext}" for kind in ("werkstatt", "schnellstart", "hauptproblem")
                          for ext in ("md", "txt") if (directory / f"{name}-{kind}.{ext}").is_file()}
        # Unveränderte eigenständige Prompts brauchen bei einer reinen Skillrunde
        # keinen weiteren Download. Sie bleiben vollständig deklariert und an
        # ihren geprüften Quellstand gebunden; kein stilles Weglassen.
        retained = plugin.get("preserved_prompts", {})
        if not isinstance(retained, dict) or set(retained) & set(prompts):
            raise ValueError(f"{name}: ungültiger oder doppelt deklarierter erhaltener Promptbestand")
        if set(prompts) | set(retained) != actual_prompts:
            raise ValueError(f"{name}: bestehender Promptbestand ist nicht vollständig deklariert: {sorted(actual_prompts ^ (set(prompts) | set(retained)))}")
        for filename, expected in retained.items():
            if (not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected)
                    or sha256_file(directory / filename) != expected):
                raise ValueError(f"{name}: erhaltener Prompt wurde verändert und muss neu veröffentlicht werden: {filename}")
        validate_plugin_version(entries[name], market["version"], root=root)
        if entries[name]["version"] != scope["version"]:
            raise ValueError(f"{name}: Marketplace-Version passt nicht zum Scope")
    if scope.get("required_main_workflow_reviews") is not None:
        if scope["required_main_workflow_reviews"] is not True:
            raise ValueError("Hauptworkflow-Nachprüfung muss ausdrücklich true sein")
        from main_skill_revisions import validate_all, index
        validate_all(root)
        reviewed_plugins = {row["plugin"] for row in index(root).values()}
        if seen != reviewed_plugins:
            raise ValueError("Release-Scope und geprüfte Hauptworkflow-Fortschreibungen weichen ab")
    required_reviews = scope.get("required_file_reviews", {})
    if (not isinstance(required_reviews, dict) or not set(required_reviews) <= seen
            or any(type(count) is not int or count < 1 for count in required_reviews.values())):
        raise ValueError("Geforderte Dateireviews müssen Plugin und positive Dateizahl des Release-Scope nennen")
    if required_reviews:
        from quality_lab import load, pending_file_reviews
        for name, count in required_reviews.items():
            profile = load(root / "quality/evals" / (name + ".json"))
            if not isinstance(profile, dict) or profile.get("plugin") != name:
                raise ValueError(f"{name}: Nachprüfungsprofil gehört nicht zum Plugin im Release-Scope")
            review = profile.get("file_review_status")
            if (not isinstance(review, dict) or review.get("status") != "reviewed"
                    or not isinstance(review.get("files"), list) or len(review["files"]) != count):
                raise ValueError(f"{name}: {count} vollständige belegte Dateinachprüfungen sind vor dem Release erforderlich")
            if pending_file_reviews(profile, root):
                raise ValueError(f"{name}: offene Nachprüfung verhindert Veröffentlichung")
    extras = scope.get("additional_assets", [])
    extra_names = {r.get("name") for r in extras} if isinstance(extras, list) else set()
    if "insolvenzanfechtung" in seen and scope["version"] == "445.36.2" and extra_names != ANFECHTUNG_ASSETS:
        raise ValueError("Insolvenzanfechtung 445.36.2 benötigt das vollständige geprüfte Werkstattpaar")
    if not isinstance(extras, list) or (extras and extra_names not in (HANDBOOK_ASSETS, ANFECHTUNG_ASSETS)):
        raise ValueError("Zusatzassets sind ausschließlich das vollständige geprüfte KI-native-Handbuchpaar oder Anfechtungs-Werkstattpaar")
    if len({r.get("name") for r in extras}) != len(extras):
        raise ValueError("Doppelte Zusatzassets")
    if extra_names == HANDBOOK_ASSETS and "ki-native-kanzlei" not in seen:
        raise ValueError("Handbuchpaar benötigt das zugehörige Plugin im Release-Scope")
    if extra_names == ANFECHTUNG_ASSETS and "insolvenzanfechtung" not in seen:
        raise ValueError("Werkstattpaar benötigt Insolvenzanfechtung im Release-Scope")
    expected_evidence = ANFECHTUNG_EVIDENCE if extra_names == ANFECHTUNG_ASSETS else "quality/ki-native-kanzlei/umfang.json"
    for row in extras:
        for field in ("source", "evidence"):
            relative = Path(row.get(field, ""))
            if relative.is_absolute() or ".." in relative.parts or not relative.parts:
                raise ValueError(f"Ungültiger Zusatzassetpfad: {row}")
            path = root / relative
            if not path.resolve().is_relative_to(root.resolve()) or path.is_symlink() or not path.is_file():
                raise ValueError(f"Zusatzassetquelle fehlt oder liegt außerhalb des Repositories: {relative}")
        if row["evidence"] != expected_evidence or not re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256", ""))):
            raise ValueError("Konkreter Quellen-/Umfangsnachweis und SHA-256 erforderlich")
        if sha256_file(root / row["source"]) != row["sha256"]:
            raise ValueError(f"Zusatzasset stimmt nicht mit dem geprüften Hash überein: {row['name']}")
        assets.add(row["name"])
    check_asset_limit(assets)
    return entries


def verify_handbooks(scope: dict, root: Path, asset_directory: Path | None = None) -> dict:
    extras = scope.get("additional_assets", [])
    if not extras:
        return {}
    if {row["name"] for row in extras} == ANFECHTUNG_ASSETS:
        from anfechtung_werkstatt_contract import validate_exports
        paths = {row["name"]: (asset_directory / row["name"] if asset_directory else root / row["source"]) for row in extras}
        evidence_path = root / ANFECHTUNG_EVIDENCE
        evidence_bytes = evidence_path.read_bytes()
        evidence = validate_exports(root, evidence_path,
                                    paths["insolvenzanfechtung-tatbestandswerkstaetten.zip"],
                                    paths["insolvenzanfechtung-tatbestandswerkstaetten.pdf"])
        if evidence["version"] != scope["version"]:
            raise ValueError("Werkstattpaar benötigt die passende Release-Version")
        return {row["name"]: {"source": row["source"], "sha256": row["sha256"], "evidence": row["evidence"],
                               "evidence_sha256": hashlib.sha256(evidence_bytes).hexdigest()} for row in extras}
    from pypdf import PdfReader
    contract = load_module("ki_kanzlei_release_contract.py")
    evidence_path = root / "quality/ki-native-kanzlei/umfang.json"
    evidence_bytes = evidence_path.read_bytes()
    evidence = json.loads(evidence_bytes)
    rows = contract.validate_module_report(evidence)
    if evidence["version"] != scope["version"] or evidence.get("font") != "Times New Roman":
        raise ValueError("Handbuch benötigt die passende Version und den dokumentierten TNR-Satz")
    active = {p.parent.name for p in (root / "ki-native-kanzlei/skills").glob("*/SKILL.md")}
    if active != set(evidence["active_skills"]) or len(active) != evidence["active_skill_count"]:
        raise ValueError("Handbuchnavigation passt nicht zu den tatsächlichen Arbeitswegen")
    for row in rows:
        path = (root / row["source"]).resolve()
        if not path.is_relative_to((root / "ki-native-kanzlei/skills").resolve()) or not path.is_file() or sha256_file(path) != row["source_sha256"]:
            raise ValueError(f"Handbuch-Fachmodul weicht vom aktuellen Quelltext ab: {row['source']}")
    paths = {row["name"]: (asset_directory / row["name"] if asset_directory else root / row["source"]) for row in extras}
    handbook = paths["ki-native-kanzlei-skills-handbuch.pdf"]
    if sha256_file(handbook) != evidence["handbook_sha256"] or len(PdfReader(handbook).pages) != evidence["handbook_pages"]:
        raise ValueError("Handbuch-PDF stimmt nicht mit Quellen-/Seitenumfangsnachweis überein")
    with zipfile.ZipFile(paths["ki-native-kanzlei-skills-einzelpdfs.zip"]) as archive:
        names = archive.namelist()
        expected = {row["pdf"] for row in rows} | {"README.txt", "umfang.json"}
        if len(names) != len(set(names)) or set(names) != expected or archive.read("umfang.json") != evidence_bytes:
            raise ValueError("Einzel-PDF-ZIP stimmt nicht mit dem vollständigen Modul-/Umfangsbestand überein")
        if not archive.read("README.txt").strip():
            raise ValueError("Einzel-PDF-ZIP benötigt seinen Leserhinweis")
        for row in rows:
            data = archive.read(row["pdf"])
            if hashlib.sha256(data).hexdigest() != row["pdf_sha256"] or len(PdfReader(io.BytesIO(data)).pages) != row["pages"]:
                raise ValueError(f"Einzel-PDF stimmt nicht mit Quellen-/Seitenumfangsnachweis überein: {row['pdf']}")
    return {row["name"]: {"source": row["source"], "sha256": row["sha256"], "evidence": row["evidence"],
                           "evidence_sha256": hashlib.sha256(evidence_bytes).hexdigest()} for row in extras}


def source_files(root: Path, directory: Path) -> dict[str, Path]:
    files = {}
    for path in sorted(directory.rglob("*")):
        name = path.relative_to(directory).as_posix()
        if not package_path(name):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink wird nicht paketiert: {path}")
        if path.is_file():
            files[name] = path
    for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
        if name not in files and (root / name).is_file() and not (root / name).is_symlink():
            files[name] = root / name
    return files


def check_manifests(files: dict[str, Path], name: str, version: str) -> list[str]:
    if ".claude-plugin/plugin.json" not in files:
        raise ValueError(f"{name}: natives Manifest fehlt")
    manifests = [path for path in MANIFESTS if path in files]
    for path in manifests:
        value = json.loads(files[path].read_text())
        if (value.get("name"), value.get("version")) != (name, version):
            raise ValueError(f"{name}/{path}: Identität oder Version weicht ab")
    return manifests


def verify_reachability(files: dict[str, Path]) -> list[str]:
    active = sorted(name for name in files if SKILL.fullmatch(name))
    if not 1 <= len(active) <= MAX_ACTIVE_SKILLS_PER_PLUGIN:
        raise ValueError(f"Paket benötigt 1 bis {MAX_ACTIVE_SKILLS_PER_PLUGIN} echte SKILL.md-Dateien, gefunden: {len(active)}")
    links = {}
    for name, path in files.items():
        if path.suffix != ".md" or not name.startswith(("skills/", "references/")):
            continue
        targets = []
        for raw in LINK.findall(path.read_text(encoding="utf-8")):
            target = raw.partition("#")[0]
            if not target or ":" in target or target.startswith("/"):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(name), target)).replace(os.sep, "/")
            if resolved.startswith("../") or (resolved not in files and not any(n.startswith(resolved.rstrip("/") + "/") for n in files)):
                raise ValueError(f"Paketverweis fehlt oder verlässt das Plugin: {name} -> {raw}")
            targets.append(resolved)
        links[name] = targets
    pending, reachable = list(active), set()
    while pending:
        name = pending.pop()
        if name in reachable:
            continue
        reachable.add(name)
        pending.extend(links.get(name, []))
    orphaned = {name for name in files if name.endswith("/FACHINHALT.md")} - reachable
    if orphaned:
        raise ValueError(f"Fachinhalt nicht von aktivem Skill erreichbar: {sorted(orphaned)[:4]}")
    return active


def document_contents(root, directory, files, commit, routes):
    """Render included READMEs from their own folders and pin the planned download buttons."""
    contents = {}
    for name, path in files.items():
        if path.name == "README.md":
            data = render_readme(root, directory, files, commit, name=name)
        elif routes and path.suffix.lower() == ".html":
            data = path.read_bytes()
        else:
            continue
        if routes:
            data = planned_links(data.decode("utf-8"), routes).encode("utf-8")
        if data != path.read_bytes():
            contents[name] = data
    return contents


def write_zip(target: Path, files: dict[str, Path], prefix: str = "", *, readme: bytes | None = None, documents=None) -> None:
    rendered = dict(documents or {})
    if readme is not None:
        rendered["README.md"] = readme
    with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, path in sorted(files.items()):
            item = zipfile.ZipInfo(prefix + name, STAMP)
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = (stat.S_IFREG | stat.S_IMODE(path.stat().st_mode)) << 16
            archive.writestr(item, rendered[name] if name in rendered else path.read_bytes())


def verify_zip(target: Path, files: dict[str, Path], prefix: str = "", *, readme: bytes | None = None, documents=None) -> dict[str, str]:
    rendered = dict(documents or {})
    if readme is not None:
        rendered["README.md"] = readme
    with zipfile.ZipFile(target) as archive:
        expected = {prefix + name: path for name, path in files.items()}
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise ValueError(f"{target.name}: Dateiliste weicht vom Quellstand ab")
        hashes = {}
        for name, path in sorted(expected.items()):
            data = archive.read(name)
            if data != (rendered[name[len(prefix):]] if name[len(prefix):] in rendered else path.read_bytes()):
                raise ValueError(f"{target.name}/{name}: Inhalt weicht vom Quellstand ab")
            hashes[name] = hashlib.sha256(data).hexdigest()
        return hashes


def checkout_state(root: Path, expected_commit: str | None = None) -> dict:
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, text=True, capture_output=True)
    status = subprocess.run(["git", "status", "--porcelain"], cwd=root, text=True, capture_output=True)
    commit = head.stdout.strip() if head.returncode == 0 else None
    clean = head.returncode == status.returncode == 0 and not status.stdout.strip()
    if expected_commit and (not re.fullmatch(r"[a-f0-9]{40}", expected_commit) or commit != expected_commit or not clean):
        raise ValueError("Veröffentlichungsbau benötigt den exakten sauberen Checkout des freigegebenen Commits")
    return {"commit": commit, "clean": clean}


def validate_assets(dist: Path, scope: dict, root: Path, *, expected_commit: str | None = None) -> dict:
    entries = validate_scope(scope, root)
    routes = edition_routes(root, scope["tag"].rsplit("-v", 1)[0]) if PAKETPFLEGE_TAG.fullmatch(scope["tag"]) else {}
    expected = {REPORT, CHECKSUMS}
    for plugin in scope["plugins"]:
        expected.update(plugin["prompts"])
        expected.update(plugin["name"] + ("-portable" if v == "portable" else "") + ".zip" for v in plugin["variants"])
    expected.update(row["name"] for row in scope.get("additional_assets", []))
    if {p.name for p in dist.iterdir()} != expected or any(not p.is_file() or p.is_symlink() for p in dist.iterdir()):
        raise ValueError("Releasebestand weicht vom expliziten Scope ab")
    report = json.loads((dist / REPORT).read_text())
    if report.get("tag") != scope["tag"] or report.get("version") != scope["version"]:
        raise ValueError("Release-Nachweis passt nicht zu Tag und Version")
    if report.get("scope_sha256") != hashlib.sha256(json.dumps(scope, ensure_ascii=False, sort_keys=True).encode()).hexdigest():
        raise ValueError("Release-Nachweis passt nicht zum vollständigen Scope")
    if expected_commit and report.get("source_state") != {"commit": expected_commit, "clean": True}:
        raise ValueError("Release-Nachweis stammt nicht vom freigegebenen sauberen Commit")
    commit = checkout_state(root, expected_commit)["commit"]
    checksums = read_checksums(dist / CHECKSUMS)
    if set(checksums) != expected - {CHECKSUMS}:
        raise ValueError("Prüfsummenbestand ist unvollständig oder enthält zusätzliche Dateien")
    for name, digest in checksums.items():
        if sha256_file(dist / name) != digest:
            raise ValueError(f"Prüfsumme weicht ab: {name}")
    for plugin in scope["plugins"]:
        name = plugin["name"]
        directory = (root / entries[name]["source"]).resolve()
        files = source_files(root, directory)
        manifests = check_manifests(files, name, scope["version"])
        active = verify_reachability(files)
        documents = document_contents(root, directory, files, commit, routes)
        evidence = report["plugins"][name]
        if evidence["skills"] != active or evidence["manifests"] != manifests:
            raise ValueError(f"{name}: Skill-/Manifestnachweis stimmt nicht")
        for variant in plugin["variants"]:
            filename = name + ("-portable" if variant == "portable" else "") + ".zip"
            hashes = verify_zip(dist / filename, files, name + "/" if variant == "portable" else "", documents=documents)
            if evidence["archives"][filename] != hashes:
                raise ValueError(f"{filename}: Quellhashinventar stimmt nicht")
        CHECKS.validate_plugin_zip(dist, name, scope["version"])
        CHECKS.validate_skill_sources(dist / f"{name}.zip", directory, rendered_readmes=documents)
        CHECKS.validate_focus_skill(dist / f"{name}.zip", directory, root / "quality/evals" / f"{name}.json")
        for filename in plugin["prompts"]:
            if (dist / filename).read_bytes() != (directory / filename).read_bytes():
                raise ValueError(f"Prompt-Snapshot weicht ab: {filename}")
            if report["prompts"][filename] != sha256_file(directory / filename):
                raise ValueError(f"Promptnachweis weicht ab: {filename}")
    additional = verify_handbooks(scope, root, dist)
    if report.get("additional_assets", {}) != additional:
        raise ValueError("Zusatzasset-Nachweis weicht ab")
    for row in scope.get("additional_assets", []):
        if sha256_file(dist / row["name"]) != row["sha256"]:
            raise ValueError(f"Zusatzasset weicht vom Quellhash ab: {row['name']}")
    return report


def build(dist: Path, scope: dict, root: Path = ROOT, *, expected_commit: str | None = None) -> dict:
    root, dist = root.resolve(), dist.resolve()
    if dist.is_relative_to(root):
        raise ValueError("Buildziel muss außerhalb des Quellrepositories liegen")
    entries = validate_scope(scope, root)
    routes = edition_routes(root, scope["tag"].rsplit("-v", 1)[0]) if PAKETPFLEGE_TAG.fullmatch(scope["tag"]) else {}
    state = checkout_state(root, expected_commit)
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError("Releaseverzeichnis muss leer sein; bestehende Assets bleiben unverändert")
    report = {"schema_version": 1, "tag": scope["tag"], "version": scope["version"],
              "source_state": state,
              "scope_sha256": hashlib.sha256(json.dumps(scope, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
              "plugins": {}, "prompts": {}, "additional_assets": verify_handbooks(scope, root)}
    for plugin in scope["plugins"]:
        name = plugin["name"]
        directory = (root / entries[name]["source"]).resolve()
        files = source_files(root, directory)
        manifests = check_manifests(files, name, scope["version"])
        active = verify_reachability(files)
        documents = document_contents(root, directory, files, state["commit"], routes)
        evidence = {"source": entries[name]["source"], "skills": active, "manifests": manifests, "archives": {}}
        for variant in plugin["variants"]:
            filename = name + ("-portable" if variant == "portable" else "") + ".zip"
            prefix = name + "/" if variant == "portable" else ""
            write_zip(dist / filename, files, prefix, documents=documents)
            evidence["archives"][filename] = verify_zip(dist / filename, files, prefix, documents=documents)
        report["plugins"][name] = evidence
        for filename in plugin["prompts"]:
            source = directory / filename
            if source.is_symlink():
                raise ValueError(f"Promptquelle ist ein Symlink: {filename}")
            shutil.copyfile(source, dist / filename)
            report["prompts"][filename] = sha256_file(source)
    for row in scope.get("additional_assets", []):
        shutil.copyfile(root / row["source"], dist / row["name"])
    (dist / REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_checksums(dist)
    expected_asset_metadata(dist)
    validate_assets(dist, scope, root, expected_commit=expected_commit)
    return report


def verify_download(dist: Path, scope: dict, root: Path, repo: str, expected_commit: str) -> None:
    validate_assets(dist, scope, root, expected_commit=expected_commit)
    require_download_budget(len(list(dist.iterdir())))
    with tempfile.TemporaryDirectory(prefix="skill-quality-download-") as folder:
        target = Path(folder)
        subprocess.run(["gh", "release", "download", scope["tag"], "--repo", repo, "--dir", str(target)], check=True, timeout=1800)
        validate_assets(target, scope, root, expected_commit=expected_commit)
        for path in dist.iterdir():
            if sha256_file(path) != sha256_file(target / path.name):
                raise ValueError(f"Heruntergeladenes Release-Asset weicht ab: {path.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--scope", type=Path, default=SCOPE)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--expected-commit")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--verify-download", action="store_true")
    parser.add_argument("--repo", default="Klotzkette/claude-fuer-deutsches-recht")
    args = parser.parse_args()
    scope = json.loads(args.scope.read_text())
    if args.verify_download:
        if not args.expected_commit:
            parser.error("Downloadprüfung benötigt --expected-commit")
        verify_download(args.dist, scope, args.root, args.repo, args.expected_commit)
    elif args.verify:
        validate_assets(args.dist, scope, args.root, expected_commit=args.expected_commit)
    else:
        build(args.dist, scope, args.root, expected_commit=args.expected_commit)
    print(f"{scope['tag']}: {len(scope['plugins'])} Plugins; {len(list(args.dist.iterdir()))} Assets vollständig geprüft")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
