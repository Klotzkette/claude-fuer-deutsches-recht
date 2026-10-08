#!/usr/bin/env python3
"""
Baut pro Plugin ein ZIP-Bundle mit allen Skill-Markdown-Dateien (SKILL.md).
Standalone-Prompts werden nur als einzelne Markdown-Dateien angeboten.
Diese ZIPs werden als Release-Assets unter
dem versionierten Komponenten-Release veroeffentlicht, damit
echte Datei-Downloads möglich sind (statt browser-rendered Markdown auf
GitHub).

Aufruf:
    python3 scripts/build-skills-markdown-bundles.py <output-dir>

Erzeugt:
    <output-dir>/<plugin>-skills-markdown.zip   (pro Plugin)
    <output-dir>/alle-skills-markdown.zip       (eines mit allen Plugins)
"""
import argparse
import json
from pathlib import Path

from reproducible_zip import write_archive


def list_plugins(repo_root: Path) -> list[str]:
    """Lese die Plugin-Liste aus marketplace.json."""
    manifest = json.loads(
        (repo_root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    return sorted(p["name"] for p in manifest.get("plugins", []))


def collect_skill_files(plugin_dir: Path) -> list[Path]:
    """Alle SKILL.md unter <plugin>/skills/ einsammeln."""
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(skills_dir.glob("*/SKILL.md"))


def build_plugin_bundle(plugin: str, repo_root: Path, out_dir: Path) -> tuple[Path, int]:
    plugin_dir = repo_root / plugin
    skills = collect_skill_files(plugin_dir)

    # Plugin-README als Index mitnehmen
    plugin_readme = plugin_dir / "README.md"

    bundle_path = out_dir / f"{plugin}-skills-markdown.zip"
    members: list[tuple[Path, str]] = []
    if plugin_readme.is_file():
        members.append((plugin_readme, f"{plugin}/README.md"))
    for skill_md in skills:
        rel = skill_md.relative_to(repo_root)
        members.append((skill_md, rel.as_posix()))
    members += [(repo_root / name, name) for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE")]
    n_files = write_archive(bundle_path, members)
    return bundle_path, n_files


def build_combined_bundle(individual_bundles: list[Path], out_dir: Path) -> Path:
    combined = out_dir / "alle-skills-markdown.zip"
    write_archive(combined, ((bundle, bundle.name) for bundle in individual_bundles))
    return combined


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", nargs="?", type=Path, default=repo_root / "dist")
    args = parser.parse_args()
    out_dir = args.output_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    plugins = list_plugins(repo_root)
    print(f"Plugins gefunden: {len(plugins)}")

    individual = []
    total_files = 0
    empty = []
    for plugin in plugins:
        bundle_path, n_files = build_plugin_bundle(plugin, repo_root, out_dir)
        if n_files == 0:
            empty.append(plugin)
            bundle_path.unlink()
            continue
        individual.append(bundle_path)
        total_files += n_files

    print(f"Individual bundles erzeugt: {len(individual)}")
    print(f"Skill-Paketdateien gesamt: {total_files}")
    if empty:
        print(f"Plugins ohne Skills (kein ZIP): {len(empty)}")
        for p in empty:
            print(f"  - {p}")

    combined = build_combined_bundle(individual, out_dir)
    size_mb = combined.stat().st_size / 1024 / 1024
    print(f"Combined bundle: {combined.name} ({size_mb:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
