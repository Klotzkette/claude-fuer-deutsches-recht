#!/usr/bin/env python3
"""
Baut pro Plugin ein ZIP-Bundle mit allen Skill-Markdown-Dateien (SKILL.md),
ihren unterstützenden Markdown-Referenzen und dem Plugin-README. Werkstatt-
und Schnellstart-Prompts bleiben bewusst außerhalb aller ZIPs als einzelne
Markdown-Downloads. Die Plugin-Bundles werden im Komplettpaket mitgeführt;
als Release-Asset liegt wegen der Asset-Grenze nur das Sammel-ZIP
alle-skills-markdown.zip oben.

Aufruf:
    python3 scripts/build-skills-markdown-bundles.py <output-dir>

Erzeugt:
    <output-dir>/<plugin>-skills-markdown.zip   (pro Plugin)
    <output-dir>/alle-skills-markdown.zip       (eines mit allen Plugins)
"""
import json
import sys
import zipfile
from pathlib import Path


def list_plugins(repo_root: Path) -> list[dict[str, str]]:
    """Lese die Plugin-Liste aus marketplace.json."""
    manifest = json.loads((repo_root / ".claude-plugin" / "marketplace.json").read_text())
    plugins = []
    for plugin in manifest.get("plugins", []):
        name = plugin["name"]
        plugins.append({"name": name, "source": plugin.get("source") or f"./{name}"})
    return sorted(plugins, key=lambda p: p["name"])


def resolve_plugin_dir(repo_root: Path, source: str) -> Path:
    """Loese marketplace source relativ zum Repo-Root auf."""
    if source.startswith("./"):
        source = source[2:]
    return repo_root / source


def collect_skill_files(plugin_dir: Path) -> list[Path]:
    """Alle Markdown-Dateien der Skills samt Referenzen einsammeln."""
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(path for path in skills_dir.rglob("*.md") if path.is_file())


def build_plugin_bundle(plugin: dict[str, str], repo_root: Path, out_dir: Path) -> tuple[Path, int]:
    plugin_name = plugin["name"]
    plugin_dir = resolve_plugin_dir(repo_root, plugin["source"])
    skills = collect_skill_files(plugin_dir)

    # Plugin-README als Index mitnehmen
    plugin_readme = plugin_dir / "README.md"

    bundle_path = out_dir / f"{plugin_name}-skills-markdown.zip"
    n_files = 0
    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        if plugin_readme.is_file():
            zf.write(plugin_readme, arcname=f"{plugin_name}/README.md")
            n_files += 1
        for skill_markdown in skills:
            # arcname: <plugin>/skills/<skill-slug>/SKILL.md beziehungsweise references/...
            rel = skill_markdown.relative_to(plugin_dir)
            zf.write(skill_markdown, arcname=f"{plugin_name}/{rel}")
            n_files += 1
    return bundle_path, n_files


def build_combined_bundle(individual_bundles: list[Path], out_dir: Path) -> Path:
    combined = out_dir / "alle-skills-markdown.zip"
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED) as zf:
        for b in individual_bundles:
            zf.write(b, arcname=b.name)
    return combined


def main():
    if len(sys.argv) != 2:
        print("Usage: build-skills-markdown-bundles.py <output-dir>", file=sys.stderr)
        sys.exit(2)
    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Repo-Root: Script liegt unter scripts/
    repo_root = Path(__file__).resolve().parent.parent

    plugins = list_plugins(repo_root)
    print(f"Plugins gefunden: {len(plugins)}")

    individual = []
    total_files = 0
    empty = []
    for plugin in plugins:
        bundle_path, n_files = build_plugin_bundle(plugin, repo_root, out_dir)
        if n_files == 0:
            empty.append(plugin["name"])
            bundle_path.unlink()
            continue
        individual.append(bundle_path)
        total_files += n_files

    print(f"Individual bundles erzeugt: {len(individual)}")
    print(f"README- und Skill-Dateien gesamt: {total_files}")
    if empty:
        print(f"Plugins ohne README oder Skills (kein ZIP): {len(empty)}")
        for p in empty:
            print(f"  - {p}")

    combined = build_combined_bundle(individual, out_dir)
    size_mb = combined.stat().st_size / 1024 / 1024
    print(f"Combined bundle: {combined.name} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
