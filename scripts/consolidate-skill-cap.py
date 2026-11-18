#!/usr/bin/env python3
"""Fachlich zugeordnete Skills verlustfrei in höchstens 21 Auswahlwege überführen.

Ohne --apply wird das Repository niemals geändert. --check prüft die Registry;
--output erzeugt die ausgewählten Plugins in einem leeren Zielverzeichnis.
Die Zuordnung erfolgt ausschließlich durch die geprüfte Registry, nicht durch
eine verdeckte Schlüsselwortklassifikation. Alte Inhalte bleiben am bisherigen
Ort als FACHINHALT.md erhalten. Exakte Verweisänderungen sind invertierbar und
werden zusammen mit den ursprünglichen und endgültigen SHA-256 dokumentiert.
"""
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import shutil
import sys
from urllib.parse import unquote

from skill_source_replacements import validate_replacements
from skill_limits import MAX_ACTIVE_SKILLS_PER_PLUGIN


REPO = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9-]{1,64}\Z")
FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---(?:\r?\n|$)", re.S)
LINK = re.compile(r"(?P<prefix>\]\()(?P<path><[^>]+>|[^)\s]+)(?P<suffix>[^)]*\))")
INVOCATION = re.compile(r"/([a-z0-9-]+):([a-z0-9-]+)(?![a-z0-9-])")
DOC_SUFFIXES = {".md", ".txt", ".html"}
MAX_SKILLS = MAX_ACTIVE_SKILLS_PER_PLUGIN
REPOSITORY_WEB = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/"
VERGABE_OUTPUT_BLOCK = """<!-- BEGIN output-format-block (autogen) -->

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->"""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def safe_path(root: Path, value: str) -> Path:
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Pfad liegt außerhalb des Repositories: {value}")
    return path


def marketplace_sources(repo: Path) -> dict[str, str]:
    path = repo / ".claude-plugin/marketplace.json"
    if not path.is_file():
        return {}
    return {p["name"]: p["source"] for p in json.loads(path.read_text())["plugins"]}


def keep_suggestions(repo: Path) -> dict:
    """Schutzgründe vorschlagen, nicht sämtliche bisherigen Review-Ziele sperren."""
    profile_path = repo / "scripts/data/werkstatt-visualisierung-profile.json"
    profiles = json.loads(profile_path.read_text()).get("plugins", {}) if profile_path.exists() else {}
    runtime_path = repo / "scripts/validate-runtime-performance.py"
    runtime = runpy.run_path(str(runtime_path)).get("RUNTIME_ROUTERS", {}) if runtime_path.exists() else {}
    result = []
    for name, source in sorted(marketplace_sources(repo).items()):
        directory = safe_path(repo, source)
        paths = {p.parent.name: p for p in (directory / "skills").glob("*/SKILL.md")}
        if len(paths) <= MAX_SKILLS:
            continue
        reasons = defaultdict(list)
        for slug in profiles.get(name, {}).get("entry_skills", []):
            reasons[slug].append("Bestehender Hauptworkflow/Visualisierungseinstieg")
        qpath = repo / "quality/evals" / (name + ".json")
        quality = json.loads(qpath.read_text()) if qpath.exists() else {}
        target = quality.get("selection", {}).get("target_skill")
        if target:
            reasons[target].append("Geprüfter Auswahl-Schwerpunkt")
        focus_path = quality.get("focus_review", {}).get("skill_path", "")
        if focus_path:
            reasons[Path(focus_path).parent.name].append("Geprüfter Hauptproblem-Skill")
        for slug in runtime.get(name, set()):
            reasons[slug].append("Bereits verdichteter Laufzeitrouter")
        for slug, path in paths.items():
            extras = [p for p in path.parent.rglob("*") if p.is_file()
                      and p.suffix not in {".md", ".txt", ".json", ".csv", ".pyc"}
                      and "__pycache__" not in p.parts]
            if extras:
                reasons[slug].append("Lokales Werkzeug oder strukturierte Vorlage")
        if name == "liquiditaetsplanung":
            for slug in ("liquiditaetsvorschau-3wochen", "liquiditaetsvorschau-3-6-12-monate", "liquiditaetsvorschau-insolvenzrechtlich"):
                reasons[slug].append("Öffentlich validierter Liquiditätsworkflow")
        missing = sorted(set(reasons) - set(paths))
        result.append({"name": name, "source": source, "before": len(paths),
                       "keep": sorted(set(reasons) & set(paths)),
                       "reasons": {s: reasons[s] for s in sorted(reasons)},
                       "missing_protected_targets": missing})
    return {"schema_version": 1, "plugins": result}


def validate_registry(repo: Path, registry: dict, *, migrated: bool = False) -> list[str]:
    errors = []
    if registry.get("schema_version") != 1 or not isinstance(registry.get("plugins"), list):
        return ["Registry benötigt schema_version 1 und eine Plugin-Liste"]
    sources = marketplace_sources(repo)
    profiles = {}
    # Heutige Einstiegspunkte schützen den nächsten Umbau. Eine Prüfung bereits
    # migrierter Quellen darf historische Zuordnungen nicht rückwirkend ändern.
    profile_path = repo / "scripts/data/werkstatt-visualisierung-profile.json"
    if not migrated and profile_path.is_file():
        try:
            data = json.loads(profile_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            return [f"Einstiegsprofile nicht lesbar: {exc}"]
        if (not isinstance(data, dict) or type(data.get("schema_version")) is not int
                or data.get("schema_version") != 1
                or not isinstance(data.get("plugins"), dict)):
            return ["Einstiegsprofile benötigen schema_version 1 und eine Plugin-Zuordnung"]
        profiles = data["plugins"]
    replacement_archives, replacement_errors = validate_replacements(repo) if migrated else ({}, [])
    errors.extend(replacement_errors)
    consolidation_path = repo / "scripts/plugin-consolidations.json"
    retired = {row["legacy"]: row["canonical"] for row in json.loads(consolidation_path.read_text())["consolidations"]} if consolidation_path.is_file() else {}
    seen_plugins = set()
    for plugin in registry["plugins"]:
        name, source = plugin.get("name", ""), plugin.get("source", "")
        if not isinstance(name, str) or not SLUG.fullmatch(name) or name in seen_plugins:
            errors.append(f"Ungültiges oder doppeltes Plugin: {name!r}")
            continue
        seen_plugins.add(name)
        retained = (plugin.get("retained_source_archive") == retired.get(name)
                    and name in retired and name not in sources and retired[name] in sources
                    and source.removeprefix("./") == name)
        if sources and sources.get(name) != source and not retained:
            errors.append(f"{name}: Quelle stimmt nicht mit Marketplace.source überein")
        try:
            directory = safe_path(repo, source)
        except (ValueError, TypeError) as exc:
            errors.append(f"{name}: {exc}")
            continue
        existing = {p.parent.name for p in (directory / "skills").glob("*/SKILL.md")}
        keep, routes = plugin.get("keep", []), plugin.get("routes", [])
        if not isinstance(keep, list) or not isinstance(routes, list) or not routes:
            errors.append(f"{name}: keep und nichtleere routes müssen Listen sein")
            continue
        if len(keep) != len(set(keep)) or any(not isinstance(s, str) or not SLUG.fullmatch(s) for s in keep):
            errors.append(f"{name}: ungültige oder doppelte keep-Slugs")
        if len(keep) + len(routes) > MAX_SKILLS:
            errors.append(f"{name}: {len(keep) + len(routes)} Auswahlwege überschreiten {MAX_SKILLS}")
        if set(keep) - existing:
            errors.append(f"{name}: geschützte Skills fehlen: {sorted(set(keep) - existing)}")
        if name in profiles:
            profile = profiles[name]
            entries = profile.get("entry_skills") if isinstance(profile, dict) else None
            if (not isinstance(entries, list)
                    or not 1 <= len(entries) <= 3
                    or any(not isinstance(slug, str) or not SLUG.fullmatch(slug) for slug in entries)
                    or len(entries) != len(set(entries))):
                errors.append(f"{name}: entry_skills müssen ein bis drei eindeutige gültige Skill-Namen sein")
            else:
                missing = set(entries) - existing
                omitted = set(entries) - set(keep)
                if missing:
                    errors.append(f"{name}: deklarierte Einstiegsskills fehlen: {sorted(missing)}")
                if omitted:
                    errors.append(f"{name}: deklarierte Einstiegsskills müssen in keep bleiben: {sorted(omitted)}")
        assigned = list(keep)
        new_slugs = set()
        for route in routes:
            slug = route.get("slug", "")
            if not isinstance(slug, str) or not SLUG.fullmatch(slug) or slug in new_slugs or slug in keep:
                errors.append(f"{name}: ungültiger oder doppelter Routenslug {slug!r}")
            new_slugs.add(slug)
            if not migrated and (directory / "skills" / slug).exists():
                errors.append(f"{name}/{slug}: neue Route würde einen bestehenden Ordner überschreiben")
            for field in ("title", "description", "purpose"):
                if not isinstance(route.get(field), str) or not route[field].strip():
                    errors.append(f"{name}/{slug}: {field} fehlt")
            if len(route.get("description", "")) > 1024:
                errors.append(f"{name}/{slug}: description überschreitet 1024 Zeichen")
            if route.get("document_style") not in (None, "vergaberecht"):
                errors.append(f"{name}/{slug}: unbekannter document_style")
            for field in ("inputs", "steps", "outputs", "examples", "members"):
                values = route.get(field)
                if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
                    errors.append(f"{name}/{slug}: {field} muss eine nichtleere Textliste sein")
            if "step_titles" in route:
                titles = route["step_titles"]
                steps = route.get("steps")
                if (not isinstance(titles, list) or not isinstance(steps, list)
                        or len(titles) != len(steps)
                        or any(not isinstance(title, str) or not title.strip()
                               or "\n" in title or "\r" in title for title in titles)):
                    errors.append(f"{name}/{slug}: step_titles benötigt eine einzeilige Überschrift je Schritt")
            members = route.get("members", [])
            assigned.extend(members)
            if any(not SLUG.fullmatch(s) for s in members if isinstance(s, str)):
                errors.append(f"{name}/{slug}: ungültiger Fachinhalt-Slug")
        if len(assigned) != len(set(assigned)):
            errors.append(f"{name}: Fachinhalt mehrfach zugeordnet")
        if migrated:
            if existing != set(keep) | new_slugs:
                errors.append(f"{name}: aktive Auswahlwege stimmen nicht mit Registry überein")
            for slug in set(assigned) - set(keep):
                original = directory / "skills" / slug / "FACHINHALT.md"
                archived = replacement_archives.get(name, {}).get(relative(original, repo))
                if not original.is_file() and archived is None:
                    errors.append(f"{name}/{slug}: erhaltener Fachinhalt fehlt")
        elif set(assigned) != existing:
            errors.append(f"{name}: Zuordnung unvollständig: fehlen={sorted(existing - set(assigned))}; unbekannt={sorted(set(assigned) - existing)}")
    return errors


def source_title(data: bytes, fallback: str) -> str:
    text = FRONTMATTER.sub("", data.decode("utf-8"), count=1)
    title = re.search(r"^#\s+(.+)$", text, re.M)
    return title[1].strip() if title else fallback


def render_route(route: dict, source_data: dict[str, bytes]) -> bytes:
    style = route.get("document_style")
    if style not in (None, "vergaberecht"):
        raise ValueError(f"Unbekannter document_style: {style}")

    def visible(value: str) -> str:
        # Nur neu erzeugte sichtbare Beschriftungen normalisieren. Originale
        # Fachtexte, Dateiziele und das Marketplace-Frontmatter bleiben unberührt.
        if style == "vergaberecht":
            value = re.sub(r"\b(?:Paragrafen|Paragraphen)\s+(?=\d)", "§§ ", value, flags=re.I)
            value = re.sub(r"\b(?:Paragraf|Paragraph)(\s+|-)(?=\d)", lambda m: "§" + ("-" if m[1] == "-" else " "), value, flags=re.I)
        return value

    def bullets(values):
        return "\n".join(f"- {visible(value)}" for value in values)
    title, slug = route["title"], route["slug"]
    step_titles = route.get("step_titles")
    parts = ["---", f"name: {slug}", "description: " + json.dumps(route["description"], ensure_ascii=False), "---", "", f"# {visible(title)}", "",
             "## 1. Zweck und Anwendungsfall", "", visible(route["purpose"]), ""]
    # Benannte Schritte gehören zu einem ausformulierten Einstieg mit eigener Prüffolge.
    if step_titles is None:
        parts += ["Bearbeite den konkreten Auftrag bis zum nutzbaren Arbeitsprodukt. Übernimm bereits vorliegende Angaben, benenne entscheidungserhebliche Lücken und arbeite an den davon unabhängigen Teilen weiter.", ""]
        step_titles = ["Arbeitsschritt"] * len(route["steps"])
    parts += ["## 2. Eingaben", "", bullets(route["inputs"]), "", "## 3. Ablauf", ""]
    for index, (step_title, step) in enumerate(zip(step_titles, route["steps"], strict=True), 1):
        parts += [f"### 3.{index}. {visible(step_title)}", "", visible(step), ""]
    parts += [f"### 3.{len(route['steps']) + 1}. Fachvertiefungen gezielt laden", "",
              "Wähle anhand des Auftrags nur die einschlägigen Vertiefungen. Lies deren vollständige Fachanweisungen vor der jeweiligen Teilprüfung; berücksichtige die dort verknüpften lokalen Werkzeuge, Vorlagen und Belege. Die folgenden Dateien sind Fachinhalte dieses Arbeitswegs, keine zusätzlichen auswählbaren Skills.", ""]
    for member in route["members"]:
        label = visible(source_title(source_data[member], member)).replace("[", "").replace("]", "")
        parts += [f"- [{label}](../{member}/FACHINHALT.md)"]
    parts += ["", "## 4. Quellenpflicht", "",
              "Trenne vorgelegte Tatsachen, eigene Berechnungen und rechtliche oder fachliche Wertungen. Prüfe entscheidungstragende Normen, Rechtsprechung und sonstige Quellen anhand zugänglicher Primärquellen auf Geltungszeitpunkt, Aussage und Übertragbarkeit. Historische Quellen sind in ihrem zeitlichen Zusammenhang auszuwerten. Eine Quellenangabe im Fachinhalt ersetzt keine aktuelle Einzelfallprüfung; behaupte keine nicht durchgeführte Verifikation.", "",
              "## 5. Ausgabeformat", ""]
    if style == "vergaberecht":
        parts += [VERGABE_OUTPUT_BLOCK, ""]
    parts += [bullets(route["outputs"]), "",
              "Liefere das beauftragte Dokument vollständig in ausformuliertem Text mit Dezimalgliederung. Für juristische Schriftsätze und Gutachten ist die Zieltypografie Times New Roman 11 pt; Tabellen und Grafiken ergänzen die Begründung. Wähle zur Aufgabe passende Vergleiche, Zeitleisten oder andere Visualisierungen. Nutze eine interaktive Ansicht nur, wenn die Laufzeit sie tatsächlich bereitstellt; stelle sonst eine unmittelbar lesbare Tabelle oder Grafik bereit. Kennzeichne fehlende Daten und offene Prüfungen an der betroffenen Stelle und schließe mit dem konkreten nächsten Arbeitsschritt.", "",
              "## 6. Beispiele", "", bullets(route["examples"]), ""]
    return "\n".join(parts).encode("utf-8")


def exact_edits(data: bytes, replacements: list[tuple[int, int, bytes]]) -> tuple[bytes, list[dict]]:
    """Nicht überlappende Byte-Spans anwenden; jeder Schritt bleibt invertierbar."""
    edits, result, cursor = [], bytearray(), 0
    for start, end, new in sorted(replacements):
        if start < cursor:
            raise ValueError("Überlappende Verweisänderungen")
        old = data[start:end]
        result.extend(data[cursor:start])
        final_start = len(result)
        result.extend(new)
        if old != new:
            edits.append({"before_offset": start, "after_offset": final_start,
                          "before": old.decode("utf-8"), "after": new.decode("utf-8")})
        cursor = end
    result.extend(data[cursor:])
    return bytes(result), edits


def edit_bytes(edit: dict, key: str) -> bytes:
    """Große Textrevisionen bleiben Daten; ihre historischen Links sind keine Navigation."""
    encoding = edit.get("encoding", "utf-8")
    if encoding == "base64":
        return base64.b64decode(edit[key], validate=True)
    if encoding != "utf-8":
        raise ValueError(f"Unbekannte Änderungskodierung: {encoding}")
    return edit[key].encode("utf-8")


def restore_original(data: bytes, edits: list[dict]) -> bytes:
    result = bytearray(data)
    for edit in reversed(edits):
        start = edit["after_offset"]
        after, before = edit_bytes(edit, "after"), edit_bytes(edit, "before")
        if result[start:start + len(after)] != after:
            raise ValueError("Verweisänderung passt nicht zum erhaltenen Fachtext")
        result[start:start + len(after)] = before
    return bytes(result)


def rewrite_document(data: bytes, document: str, source_map: dict[str, str], owners: dict[tuple[str, str], str], plugin_sources: dict[str, str], *, origin_document: str | None = None) -> tuple[bytes, list[dict]]:
    """Lokale/explizite Repo-Pfade und Aufrufe exakt, ohne Textklassifikation ändern."""
    text = data.decode("utf-8")
    origin_document = origin_document or document
    replacements = []
    # Zeichenpositionen erst beim Erzeugen der Spans in UTF-8-Bytepositionen umrechnen.
    def edit(start, end, replacement):
        if text[start:end] != replacement:
            replacements.append((len(text[:start].encode("utf-8")), len(text[:end].encode("utf-8")), replacement.encode("utf-8")))
    plugin_name = next((n for n, s in plugin_sources.items() if document.startswith(s.rstrip("/") + "/")), None)
    map_intervals = []
    map_start = None
    map_depth = None
    offset = 0
    for line in text.splitlines(keepends=True):
        heading = re.match(r"^(#{1,6})\s+(.+)", line)
        if heading:
            if map_start is not None and len(heading[1]) <= map_depth:
                map_intervals.append((map_start, offset))
                map_start = None
            if re.match(r"(?:\d+(?:\.\d+)*\.?\s+)?Fachlandkarte\b", heading[2]):
                map_start, map_depth = offset, len(heading[1])
        offset += len(line)
    if map_start is not None:
        map_intervals.append((map_start, len(text)))
    active_document = document.endswith("/SKILL.md")
    for match in LINK.finditer(text):
        raw = match["path"]
        bracketed = raw.startswith("<")
        value = raw[1:-1] if bracketed else raw
        path, sep, fragment = value.partition("#")
        target = None
        absolute_web = "://" in path
        if absolute_web:
            for boundary in re.finditer("/", path):
                old = path[boundary.end():]
                if old in source_map:
                    target = path[:boundary.end()] + source_map[old]
                    break
        elif path and not path.startswith(("#", "mailto:", "/")):
            resolved = os.path.normpath(os.path.join(os.path.dirname(origin_document), unquote(path))).replace(os.sep, "/")
            if resolved in source_map:
                new = source_map[resolved]
                if active_document and plugin_name and any(a <= match.start() < b for a, b in map_intervals):
                    old_slug = Path(resolved).parent.name
                    route = owners.get((plugin_name, old_slug))
                    if route:
                        new = plugin_sources[plugin_name] + "/skills/" + route + "/SKILL.md"
                        sep, fragment = "", ""
                target = new if "://" in new else os.path.relpath(new, os.path.dirname(document)).replace(os.sep, "/")
                if path.startswith("./") and not target.startswith(".") and "://" not in target:
                    target = "./" + target
        if target:
            target += sep + fragment
            edit(match.start("path"), match.end("path"), f"<{target}>" if bracketed else target)
    # Anleitungen enthalten auch Pfade in Code-Spannen statt Markdown-Links.
    # Bereits bearbeitete Link-Spans nicht ein zweites Mal verändern.
    for match in re.finditer(r"`([^`\n]+/SKILL\.md)`", text):
        value = match[1]
        resolved = os.path.normpath(os.path.join(os.path.dirname(origin_document), value)).replace(os.sep, "/")
        old = resolved if resolved in source_map else value.removeprefix("./")
        if old in source_map:
            new = source_map[old]
            if old == resolved:
                new = os.path.relpath(new, os.path.dirname(document)).replace(os.sep, "/")
                if value.startswith("./") and not new.startswith("."):
                    new = "./" + new
            edit(match.start(1), match.end(1), new)
    for match in INVOCATION.finditer(text):
        new = owners.get((match[1], match[2]))
        if new:
            # Der neue Weg führt mehrere Gegenstände. Die frühere Auswahl ist
            # deshalb ein ausdrückliches Fachthema im Aufruf, kein zweiter Alias.
            edit(match.start(), match.end(), f"/{match[1]}:{new} Thema: {match[2]}")
    if active_document and plugin_name:
        for start, end in map_intervals:
            for match in re.finditer(r"(?m)^\s*(?:[-*+]\s+|\|\s*)`([a-z0-9-]+)`", text[start:end]):
                new = owners.get((plugin_name, match[1]))
                if new:
                    edit(start + match.start(1) - 1, start + match.end(1) + 1,
                         f"`{new}` (Fachthema: {match[1]})")
    return exact_edits(data, replacements)


def local_link_errors(path: Path, package_root: Path, *, strict: bool = True) -> list[str]:
    """Pluginlokale Dateiverweise prüfen; Weblinks und reine Anker sind ausgenommen."""
    errors = []
    text = path.read_text(encoding="utf-8")
    for match in LINK.finditer(text):
        value = match["path"].strip("<>").partition("#")[0]
        if not value or ":" in value or value.startswith("/"):
            continue
        target = (path.parent / unquote(value)).resolve()
        if not target.is_relative_to(package_root.resolve()):
            if strict:
                errors.append(f"{path}: Verweis verlässt das installierbare Plugin: {value}")
        elif not target.exists():
            errors.append(f"{path}: lokales Verweisziel fehlt: {value}")
    return errors


def shared_dependencies(repo: Path, plugin: Path) -> dict[str, str]:
    """Nur vorhandene zentrale Fachreferenzen samt Quellennachweisen lokalisieren.

    Dies repariert bereits bestehende ../../../references-Verweise. Kein
    Nachbarplugin und kein unbekannter Pfad wird als Ersatzquelle erraten.
    """
    allowed = ((repo / "references").resolve(), (repo / "quality/source-audits").resolve())
    pending = list((plugin / "skills").rglob("*.md")) + list((plugin / "references").rglob("*.md"))
    seen, mapping = set(), {}
    while pending:
        path = pending.pop().resolve()
        if path in seen:
            continue
        seen.add(path)
        for match in LINK.finditer(path.read_text(encoding="utf-8")):
            value = match["path"].strip("<>").partition("#")[0]
            if not value or ":" in value or value.startswith("/"):
                continue
            linked = (path.parent / unquote(value)).resolve()
            if linked.is_relative_to(plugin) or not any(linked.is_relative_to(a) for a in allowed) or not linked.is_file():
                continue
            old = relative(linked, repo)
            new = relative(plugin / "references/repository" / old, repo)
            mapping[old] = new
            if linked.suffix.lower() == ".md":
                pending.append(linked)
    return mapping


def integration_file(path: str, plugin_sources: dict[str, str]) -> bool:
    """Katalog/Version/Startdokumente werden anschließend zuständig regeneriert.

    Ihr vollständiges Vorher-Inventar bleibt im Bericht. Fachbibliothek,
    Werkzeuge, Vorlagen und Testakten sind dagegen dauerhaft bytegebunden.
    """
    source = next((s for s in plugin_sources.values() if path.startswith(s + "/")), None)
    if source is None:
        return False
    parts = Path(path[len(source) + 1:]).parts
    return (parts[0] in {".claude-plugin", ".codex-plugin", ".cursor-plugin"}
            or (len(parts) == 1 and Path(parts[0]).suffix.lower() in {".md", ".txt", ".json"}))


def verify_source_map(repo: Path, report: dict, *, strict_links: bool = False, include_integration: bool = False) -> list[str]:
    from main_skill_revisions import historical_bytes

    errors = []
    items = report.get("files", []) + report.get("shared_dependencies", []) + (report.get("integration_inventory", []) if include_integration else [])
    for item in items:
        path = safe_path(repo, item["path"])
        if not path.is_file():
            errors.append(f"{item['path']}: erhaltene Datei fehlt")
            continue
        try:
            preserved = historical_bytes(repo, path, item["sha256"], plugin=item.get("plugin"))
            if sha(preserved) != item["sha256"]:
                errors.append(f"{item['path']}: Endhash stimmt nicht")
            edits = item.get("edits", [])
            original_sha = sha(restore_original(preserved, edits)) if edits else sha(preserved)
            if original_sha != item["original_sha256"]:
                errors.append(f"{item['path']}: ursprünglicher Dateiinhalt ist nicht bytegleich rekonstruierbar")
        except (OSError, ValueError, KeyError) as exc:
            errors.append(f"{item['path']}: {exc}")
    plugins = report.get("plugins", [])
    revised_routes = any("original_sha256" in route for plugin in plugins for route in plugin["routes"])
    registry_routes = {}
    if revised_routes:
        registry_path = repo / "scripts/data/skill-cap-registry.json"
        if not registry_path.is_file() or file_sha(registry_path) != report.get("registry_sha256"):
            errors.append("Registry für die fortgeschriebenen Arbeitswege fehlt oder stimmt nicht mit dem Nachweis überein")
        else:
            registry_routes = {
                (plugin["name"], route["slug"]): route
                for plugin in json.loads(registry_path.read_text(encoding="utf-8"))["plugins"]
                for route in plugin["routes"]
            }
    for plugin in plugins:
        directory = safe_path(repo, plugin["source"])
        active = {p.parent.name for p in (directory / "skills").glob("*/SKILL.md")}
        if active != set(plugin["active_skills"]) or len(active) > MAX_SKILLS:
            errors.append(f"{plugin['name']}: aktive Auswahlwege weichen ab oder überschreiten {MAX_SKILLS}")
        for route in plugin["routes"]:
            path = directory / "skills" / route["slug"] / "SKILL.md"
            if not path.is_file():
                continue
            try:
                current = historical_bytes(repo, path, route["sha256"], plugin=plugin["name"])
            except (OSError, ValueError, KeyError) as exc:
                errors.append(f"{path}: {exc}")
                continue
            if sha(current) != route["sha256"]:
                errors.append(f"{path}: erzeugter Workflow weicht ab")
            if "original_sha256" in route:
                try:
                    if sha(restore_original(current, route["edits"])) != route["original_sha256"]:
                        errors.append(f"{path}: früherer Workflow ist nicht bytegleich rekonstruierbar")
                    recipe = registry_routes[(plugin["name"], route["slug"])]
                    if recipe["members"] != route["members"]:
                        errors.append(f"{path}: Fachmodule der Registry weichen vom Nachweis ab")
                    bodies = {
                        member: safe_path(directory, f"skills/{member}/FACHINHALT.md").read_bytes()
                        for member in route["members"]
                    }
                    if render_route(recipe, bodies) != current:
                        errors.append(f"{path}: fortgeschriebener Workflow lässt sich aus der Registry nicht reproduzieren")
                except (KeyError, OSError, ValueError) as exc:
                    errors.append(f"{path}: Nachweis des fortgeschriebenen Workflows fehlt: {exc}")
            errors.extend(local_link_errors(path, directory))
        if strict_links:
            for path in (directory / "skills").rglob("*.md"):
                errors.extend(local_link_errors(path, directory))
            for path in (directory / "references/repository").rglob("*.md"):
                errors.extend(local_link_errors(path, directory))
    return errors


def migrate(repo: Path, target: Path, registry: dict) -> dict:
    """Nur nach vollständiger Registryprüfung aufrufen; CLI kontrolliert Schreibziel."""
    repo, target = repo.resolve(), target.resolve()
    errors = validate_registry(repo, registry)
    if errors:
        raise ValueError("\n".join(errors))
    in_place = repo.resolve() == target.resolve()
    if not in_place:
        if target.exists() and any(target.iterdir()):
            raise ValueError("Das Ausgabeziel muss leer sein")
        target.mkdir(parents=True, exist_ok=True)
    source_map, owners, plugin_sources, shared_maps = {}, {}, {}, {}
    navigation_links = {name: REPOSITORY_WEB + name for name in ("README.md", "ASSET_INDEX.md", "SKILLS.md")
                        if (repo / name).is_file()}
    originals = {}
    for plugin in registry["plugins"]:
        source = relative(safe_path(repo, plugin["source"]), repo)
        plugin_sources[plugin["name"]] = source
        directory = repo / source
        shared_maps[plugin["name"]] = shared_dependencies(repo, directory)
        if not in_place:
            shutil.copytree(directory, target / source, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for path in directory.rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                originals[relative(path, repo)] = file_sha(path)
        for route in plugin["routes"]:
            for member in route["members"]:
                old = f"{source}/skills/{member}/SKILL.md"
                source_map[old] = f"{source}/skills/{member}/FACHINHALT.md"
                owners[(plugin["name"], member)] = route["slug"]
    # Alle ursprünglichen Fachdateien zuerst lesen; keine Quelle aus einem bereits
    # umgebauten Skill ableiten und keine Hilfsdatei oder Unterstruktur entfernen.
    for old, new in sorted(source_map.items()):
        destination = target / new
        if destination.exists():
            raise ValueError(f"FACHINHALT-Ziel existiert bereits: {new}")
    shared_staged = []
    for plugin_name, mapping in shared_maps.items():
        for old, new in sorted(mapping.items()):
            original = (repo / old).read_bytes()
            data, edits = (rewrite_document(original, new, {**source_map, **mapping}, owners, plugin_sources, origin_document=old)
                           if Path(old).suffix.lower() in DOC_SUFFIXES else (original, []))
            path = target / new
            if path.exists() and path.read_bytes() != data:
                raise ValueError(f"Zentrale Referenz würde eine vorhandene lokale Datei ersetzen: {new}")
            shared_staged.append((path, data, {"plugin": plugin_name, "original_path": old, "path": new,
                                             "original_sha256": sha(original), "sha256": sha(data), "edits": edits}))
    for old, new in sorted(source_map.items()):
        (target / old).rename(target / new)
    report = {"schema_version": 1, "registry_sha256": sha(json_bytes(registry)),
              "plugins": [], "files": [], "shared_dependencies": [], "integration_inventory": [], "migrations": []}
    for path, data, record in shared_staged:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        report["shared_dependencies"].append(record)
    for plugin in registry["plugins"]:
        source = plugin_sources[plugin["name"]]
        row = {"name": plugin["name"], "source": source,
               "active_skills": sorted(plugin["keep"] + [r["slug"] for r in plugin["routes"]]), "routes": []}
        for route in plugin["routes"]:
            bodies = {m: (target / source / "skills" / m / "FACHINHALT.md").read_bytes() for m in route["members"]}
            data = render_route(route, bodies)
            path = target / source / "skills" / route["slug"] / "SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_bytes(data)
            row["routes"].append({"slug": route["slug"], "sha256": sha(data), "members": route["members"]})
            for member in route["members"]:
                report["migrations"].append({"plugin": plugin["name"], "old": member, "new": route["slug"],
                                             "reference": f"../{member}/FACHINHALT.md"})
        report["plugins"].append(row)
    # Der globale Pfadplan gilt für alle ausgewählten Plugins. Außerhalb liegende
    # Katalog-/Testdateien werden bewusst durch deren zuständige Generatoren
    # aktualisiert und erscheinen nicht als scheinbar erhaltene Fachquellen.
    for old, original_sha in sorted(originals.items()):
        new = source_map.get(old, old)
        path = target / new
        edits = []
        final_sha = file_sha(path)
        if final_sha != original_sha:
            raise ValueError(f"Quelle während der Migration geändert: {old}")
        if path.suffix.lower() in DOC_SUFFIXES:
            original = path.read_bytes()
            plugin_name = next(n for n, s in plugin_sources.items() if new.startswith(s + "/"))
            data, edits = rewrite_document(original, new, {**source_map, **shared_maps[plugin_name], **navigation_links}, owners, plugin_sources)
            if edits:
                path.write_bytes(data)
            if restore_original(data, edits) != original:
                raise AssertionError(f"Nicht verlustfreie Umstellung: {old}")
            final_sha = sha(data)
        scope = "integration_inventory" if integration_file(old, plugin_sources) else "files"
        report[scope].append({"original_path": old, "path": new, "original_sha256": original_sha,
                              "sha256": final_sha, "edits": edits})
    errors = verify_source_map(target, report, include_integration=True)
    if errors:
        raise ValueError("\n".join(errors))
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=REPO)
    parser.add_argument("--registry", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--source-map", type=Path, help="Prüfbericht; Standard im Ausgabeziel oder unter scripts/data")
    parser.add_argument("--verify", type=Path, help="SourceMap einschließlich reversibler Inhaltsnachweise prüfen")
    parser.add_argument("--strict-links", action="store_true", help="Zusätzlich sämtliche Fachinhalt-Links auf Paketautarkie prüfen")
    parser.add_argument("--include-integration", action="store_true", help="Auch ursprüngliche Start-/Manifestdateien vor späterer Katalogregeneration unverändert verlangen")
    parser.add_argument("--suggest-keep", action="store_true", help="Schutzgründe als JSON ausgeben; keine Mutation")
    args = parser.parse_args()
    repo = args.repo.resolve()
    if args.suggest_keep:
        print(json.dumps(keep_suggestions(repo), ensure_ascii=False, indent=2))
        return 0
    if args.verify:
        errors = verify_source_map(repo, json.loads(args.verify.read_text()), strict_links=args.strict_links, include_integration=args.include_integration)
        for error in errors:
            print(f"FEHLER: {error}")
        print(f"Inhalts- und Paketprüfung: {len(errors)} Fehler")
        return bool(errors)
    if not args.registry:
        parser.error("--registry ist erforderlich")
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    errors = validate_registry(repo, registry)
    if errors:
        for error in errors:
            print(f"FEHLER: {error}")
        return 1
    if args.check or not (args.output or args.apply):
        print(f"Registry geprüft: {len(registry['plugins'])} Plugins; keine Dateien geändert")
        return 0
    if args.apply and args.output:
        parser.error("--apply und --output schließen sich aus")
    target = repo if args.apply else args.output.resolve()
    if not args.apply and target.is_relative_to(repo):
        parser.error("Temporäres Ausgabeziel muss außerhalb des Quellrepositories liegen")
    report = migrate(repo, target, registry)
    report_path = args.source_map or (repo / "scripts/data/skill-cap-source-map.json" if args.apply else target / "skill-cap-source-map.json")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_bytes(json_bytes(report))
    print(f"{len(report['plugins'])} Plugins und {len(report['files']) + len(report['integration_inventory'])} ursprüngliche Dateien geprüft; SourceMap: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
