#!/usr/bin/env python3
"""Prüft die vier Plugin-Zusammenführungen und den unveränderten Aktenbestand."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = "scripts/plugin-consolidations.json"
INVENTORY = "quality/plugin-consolidation/2026-11-15/erhaltungsbestand.json"


def inside(root: Path, name: str) -> Path:
    path = root / name
    if not name or Path(name).is_absolute() or ".." in Path(name).parts or path.is_symlink():
        raise ValueError(f"Unzulässiger Erhaltungspfad: {name}")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Erhaltungspfad verlässt Repository: {name}")
    return path


def git_blob(path: Path) -> str:
    size = path.stat().st_size
    result = hashlib.sha1(f"blob {size}\0".encode())
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def same_stored_blob(path: Path, expected: str, root: Path, name: str, baseline: str | None) -> bool:
    """Vergleicht Bytes; berücksichtigt nur deklarierte Git-Zeilenendennormalisierung.

    Ein CRLF-Checkout einer ausdrücklich als Text markierten E-Mail hat andere
    Bytes als ihr gespeicherter LF-Blob. Maßgeblich sind ausschließlich die
    Attribute des Ausgangscommits, nicht nachträglich gelockerte Arbeitsattribute.
    Weder automatische Binärerkennung noch beliebige Clean-Filter werden benutzt.
    """
    if git_blob(path) == expected:
        return True
    if not baseline:
        return False
    result = subprocess.run(
        ["git", "-C", str(root), "check-attr", f"--source={baseline}", "-z", "text", "eol", "--", name],
        capture_output=True, check=False,
    )
    if result.returncode:
        return False
    parts = result.stdout.decode("utf-8").rstrip("\0").split("\0")
    if len(parts) != 6:
        return False
    attrs = {parts[index + 1]: parts[index + 2] for index in (0, 3)}
    if attrs.get("text") == "unset":
        return False
    explicit_text = attrs.get("text") == "set"
    explicit_eol = attrs.get("eol") in {"lf", "crlf"}
    if not (explicit_text or explicit_eol):
        return False
    content = path.read_bytes()
    # Auch bei versehentlich falschem Textattribut bleiben binäre Inhalte exakt.
    if b"\0" in content:
        return False
    normalized = content.replace(b"\r\n", b"\n")
    return hashlib.sha1(f"blob {len(normalized)}\0".encode() + normalized).hexdigest() == expected


def check(root: Path, registry: dict, inventory: dict) -> list[str]:
    errors = []
    if registry.get("schema_version") != 1 or inventory.get("schema_version") != 1:
        return ["Unbekannte Erhaltungs- oder Zusammenführungsfassung"]
    pairs = registry.get("consolidations", [])
    baseline = inventory.get("baseline_commit")
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    active = {row["name"]: row for row in marketplace["plugins"]}
    old_names = [row["legacy"] for row in pairs]
    new_names = [row["canonical"] for row in pairs]
    if len(set(old_names)) != len(old_names) or len(set(new_names)) != len(new_names):
        errors.append("Doppelte Zusammenführungszuordnung")
    for row in pairs:
        old, new = row["legacy"], row["canonical"]
        if old in active or new not in active or old == new:
            errors.append(f"{old}: genau das gemeinsame Ziel {new} muss im Marketplace stehen")
            continue
        source = inside(root, active[new]["source"].removeprefix("./"))
        skills = list((source / "skills").glob("*/SKILL.md"))
        if len(skills) != row["active_skills"] or not 1 <= len(skills) <= 20:
            errors.append(f"{new}: aktive Skill-Auswahl stimmt nicht oder überschreitet 20")
        for name in (old, new):
            path = inside(root, name + "/README.md")
            if not path.is_file():
                errors.append(f"{name}: dauerhafter Einstieg fehlt")
        legacy_readme = inside(root, old + "/README.md")
        if legacy_readme.is_file() and f"../{new}/README.md" not in legacy_readme.read_text():
            errors.append(f"{old}: Wegweiser auf {new} fehlt")
        readme = (source / "README.md").read_text()
        for case in row.get("case_entries", []):
            if case not in readme:
                errors.append(f"{new}: früherer Akteneinstieg fehlt: {case}")
        for path in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "plugin.json"):
            manifest = source / path
            if manifest.is_file():
                data = json.loads(manifest.read_text())
                if (data.get("name"), data.get("version")) != (new, registry["version"]):
                    errors.append(f"{new}/{path}: gemeinsame Identität/Version stimmt nicht")

    protected = inventory.get("protected_files", [])
    if not protected:
        errors.append("Leerer Akten-Erhaltungsnachweis")
    seen = set()
    for row in protected:
        name = row["path"]
        if name in seen:
            errors.append(f"Doppelter Erhaltungspfad: {name}")
        seen.add(name)
        path = inside(root, name)
        if not path.is_file():
            errors.append(f"Geschützte Akten-/Originaldatei fehlt: {name}")
        elif not same_stored_blob(path, row["git_blob"], root, name, baseline):
            errors.append(f"Geschützte Akten-/Originaldatei verändert: {name}")

    # Alte Dateien und Quellenstände bleiben erhalten. Nur der Einstieg wird
    # ersetzt; seine vollständige frühere Fassung liegt unmittelbar daneben.
    for row in inventory.get("plugin_source_files", []):
        name = row["path"]
        if name.split("/", 1)[0] not in old_names:
            continue
        check_name = name.removesuffix("README.md") + "README-bestand.md" if name in {n + "/README.md" for n in old_names} else name
        path = inside(root, check_name)
        if not path.is_file() or not same_stored_blob(path, row["git_blob"], root, name, baseline):
            errors.append(f"Ursprünglicher Quellbestand nicht bytegleich erhalten: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    registry = json.loads((args.root / REGISTRY).read_text())
    inventory = json.loads((args.root / INVENTORY).read_text())
    try:
        errors = check(args.root, registry, inventory)
    except (ValueError, KeyError, OSError) as exc:
        errors = [str(exc)]
    if errors:
        print("\n".join(errors[:40]))
        print(f"{len(errors)} Fehler in Zusammenführung/Erhaltung")
        return 1
    print(f"Plugin-Zusammenführung OK ({len(registry['consolidations'])} Paare; {len(inventory['protected_files'])} Originaldateien unverändert)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
