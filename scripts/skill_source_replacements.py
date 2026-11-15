"""Validiert ausdrücklich ersetzte Fachbestände und ihre externen Originalarchive.

Keine globale Ausnahme für fehlende Fachdateien: Nur exakt registrierte und
bytegeprüfte Originalpfade dürfen als historisch ersetzt behandelt werden.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

REGISTRY = "scripts/data/skill-source-replacements.json"
SLUG = re.compile(r"[a-z0-9-]{1,64}\Z")
LINK = re.compile(r"\]\(([^)\s]+)\)")


def safe_path(root: Path, relative: str) -> Path:
    if (not isinstance(relative, str) or not relative or "\\" in relative
            or relative.startswith("/") or any(p in {"", ".", ".."} for p in relative.split("/"))):
        raise ValueError(f"Unzulässiger Ersatzregisterpfad: {relative!r}")
    result = root.resolve()
    for part in relative.split("/"):
        result /= part
        if result.is_symlink():
            raise ValueError(f"Symlink im Ersatzregisterpfad: {relative}")
    if not result.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Ersatzregisterpfad verlässt Repository: {relative}")
    return result


def reachable_chapters(skills: list[Path], plugin_root: Path) -> set[Path]:
    pending, seen = list(skills), set()
    while pending:
        file = pending.pop()
        if file in seen or not file.is_file():
            continue
        seen.add(file)
        for link in LINK.findall(file.read_text(encoding="utf-8")):
            raw = link.partition("#")[0]
            if not raw or ":" in raw or raw.startswith("/"):
                continue
            target = (file.parent / raw).resolve()
            if target.is_relative_to(plugin_root) and target.suffix == ".md":
                pending.append(target)
    return seen


def validate_replacements(repo: Path) -> tuple[dict[str, dict[str, Path]], list[str]]:
    """Liefert je validiertem Plugin originaler Repo-Pfad -> geprüfter Archivpfad."""
    repo = repo.resolve()
    registry = repo / REGISTRY
    if not registry.is_file():
        return {}, []
    try:
        data = json.loads(registry.read_text(encoding="utf-8"))
        if (not isinstance(data, dict) or data.get("schema_version") != 1
                or not isinstance(data.get("plugins"), dict)):
            raise ValueError("Unbekannte oder ungültige Ersatzregisterfassung")
        market = json.loads((repo / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        sources = {row["name"]: row["source"] for row in market["plugins"]}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return {}, [f"{REGISTRY}: {exc}"]
    valid, errors = {}, []
    for name, entry in data["plugins"].items():
        try:
            if not SLUG.fullmatch(name) or not isinstance(entry, dict):
                raise ValueError("Ungültiger Plugin-Ersatz")
            source = entry.get("source")
            plugin_root = safe_path(repo, source)
            if name not in sources or sources[name] != "./" + source:
                raise ValueError("Ersatzquelle stimmt nicht exakt mit aktivem Marketplace überein")
            skills = sorted((plugin_root / "skills").glob("*/SKILL.md"))
            expected = entry.get("active_skills")
            if (not isinstance(expected, list) or not expected
                    or any(not isinstance(s, str) or not SLUG.fullmatch(s) for s in expected)
                    or len(expected) != len(set(expected))
                    or {p.parent.name for p in skills} != set(expected)):
                raise ValueError("Aktiver Skillbestand stimmt nicht exakt mit Ersatzregister überein")
            for skill in skills:
                safe_path(repo, skill.relative_to(repo).as_posix())
            chapters = entry.get("chapters")
            if (not isinstance(chapters, list) or not chapters
                    or any(not isinstance(c, str) for c in chapters)
                    or len(chapters) != len(set(chapters))):
                raise ValueError("Nichtleere eindeutige Fachkapitelliste fehlt")
            chapter_paths = []
            for chapter in chapters:
                file = safe_path(repo, source + "/" + chapter)
                if not file.is_file() or file.suffix != ".md":
                    raise ValueError(f"Fachkapitel fehlt: {chapter}")
                chapter_paths.append(file)
            if not set(chapter_paths) <= reachable_chapters(skills, plugin_root):
                raise ValueError("Registriertes Fachkapitel ist von keinem aktiven Skill erreichbar")
            manifest = safe_path(repo, entry.get("archive_manifest"))
            if not manifest.is_relative_to(repo / "quality"):
                raise ValueError("Originalarchiv muss außerhalb des installierten Plugins unter quality liegen")
            archive = json.loads(manifest.read_text(encoding="utf-8"))
            rows = archive.get("files") if isinstance(archive, dict) else None
            if not isinstance(rows, list) or not rows:
                raise ValueError("Originalarchiv enthält keine Dateizuordnung")
            originals, targets = {}, set()
            for row in rows:
                if not isinstance(row, dict):
                    raise ValueError("Ungültige Archivzeile")
                old, new = row.get("old_path"), row.get("new_path")
                old_path, new_path = safe_path(repo, old), safe_path(repo, new)
                if not old_path.is_relative_to(plugin_root / "skills"):
                    raise ValueError(f"Archiv enthält fremden Fachquellpfad: {old}")
                if new_path != manifest.parent / old or new_path.is_relative_to(plugin_root):
                    raise ValueError(f"Archivziel passt nicht zur erhaltenen Originalstruktur: {new}")
                if old in originals or new in targets:
                    raise ValueError("Doppelte Archivquelle oder doppeltes Archivziel")
                digest, size = row.get("sha256"), row.get("bytes")
                if (not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)
                        or not isinstance(size, int) or isinstance(size, bool) or size < 0):
                    raise ValueError(f"Ungültiger Archivnachweis: {old}")
                content = new_path.read_bytes()
                if len(content) != size or hashlib.sha256(content).hexdigest() != digest:
                    raise ValueError(f"Archivbytes stimmen nicht: {new}")
                originals[old] = new_path
                targets.add(new)
            valid[name] = originals
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"{REGISTRY}:{name}: {exc}")
    return valid, errors
