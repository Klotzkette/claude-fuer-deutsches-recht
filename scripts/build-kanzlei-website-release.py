#!/usr/bin/env python3
"""Baut ausschließlich die Kanzlei-Website-Komponente, ohne Veröffentlichungszugriff."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "kanzlei-website-redaktion"
NAME = PLUGIN.name
PROMPTS = [f"{NAME}-werkstatt.md", f"{NAME}-schnellstart.md"]


def build(dist: Path) -> None:
    if dist.exists() and any(dist.iterdir()):
        raise ValueError("Ausgabeordner muss leer sein")
    manifests = [json.loads((PLUGIN / p).read_text()) for p in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")]
    if len({(m["name"], m["version"], m["description"]) for m in manifests}) != 1:
        raise ValueError("Manifeste stimmen nicht überein")
    if manifests[0]["name"] != NAME or len(list((PLUGIN / "skills").glob("*/SKILL.md"))) != 10:
        raise ValueError("Pluginname oder Skillzahl falsch")
    mini = (PLUGIN / PROMPTS[1]).read_bytes()
    if len(mini) > 7500 or len(mini.decode("utf-8")) > 7500:
        raise ValueError("Mini überschreitet Umfangsgrenze")
    sources = [p for p in sorted(PLUGIN.rglob("*")) if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name not in PROMPTS]
    if any(p.is_symlink() for p in sources):
        raise ValueError("Symbolische Links sind kein Paketinhalt")
    dist.mkdir(parents=True, exist_ok=True)
    for portable in (False, True):
        target = dist / f"{NAME}{'-portable' if portable else ''}.zip"
        prefix = f"{NAME}/" if portable else ""
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sources:
                info = zipfile.ZipInfo(prefix + path.relative_to(PLUGIN).as_posix(), (2026, 10, 8, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(target) as archive:
            if archive.testzip() is not None:
                raise ValueError("Defektes ZIP")
            if len([n for n in archive.namelist() if n.endswith('/SKILL.md')]) != 10:
                raise ValueError("Falsche Skillzahl im ZIP")
            if any(n.endswith(tuple(PROMPTS)) for n in archive.namelist()):
                raise ValueError("Eigenständiger Prompt im Plugin-ZIP")
    for rel in PROMPTS + ["assets/kanzlei-website-start.md", "assets/freigabe-beispiel.json"]:
        path = PLUGIN / rel
        (dist / path.name).write_bytes(path.read_bytes())
    sums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in sorted(dist.iterdir()))
    (dist / "checksums-sha256.txt").write_text(sums, encoding="utf-8")
    print(json.dumps({"version": manifests[0]["version"], "files": [p.name for p in sorted(dist.iterdir())]}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", required=True, type=Path)
    build(parser.parse_args().dist)
