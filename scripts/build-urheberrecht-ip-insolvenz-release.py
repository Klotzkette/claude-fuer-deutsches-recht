#!/usr/bin/env python3
"""Baut die drei getrennten IP-Insolvenz-Aktenpakete für den Komponentenrelease."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = ROOT / "testakten"
SLUGS = (
    "filmrechte-sicherungsuebertragung-insolvenz-schwetzingen",
    "kurpfalz-taxware-software-ip-insolvenz",
    "markenrechte-sicherungsuebertragung-insolvenz-mannheim",
)


def expected_names() -> set[str]:
    return {
        *(f"testakte-{slug}.zip" for slug in SLUGS),
        *(f"testakte-{slug}-einzelpdfs.zip" for slug in SLUGS),
        *(f"{slug}_gesamt.pdf" for slug in SLUGS),
        "SHA256SUMS.txt",
    }


def load_script(filename: str, module_name: str):
    path = ROOT / "scripts" / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Skript nicht ladbar: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_destination(raw_dist: Path) -> Path:
    if raw_dist.is_symlink():
        raise ValueError(f"Ausgabeordner darf kein Symlink sein: {raw_dist}")
    dist = raw_dist.expanduser().resolve()
    protected = (ROOT, *ROOT.parents)
    if dist in protected:
        raise ValueError(f"Geschützter Ausgabeordner: {dist}")
    if dist.is_relative_to(ROOT) and not dist.is_relative_to(ROOT / "dist"):
        raise ValueError(f"Ausgabe im Repository ist nur unter dist/ zulässig: {dist}")
    if dist.exists():
        if not dist.is_dir() or dist.is_symlink():
            raise ValueError(f"Ausgabeziel ist kein normaler Ordner: {dist}")
        entries = list(dist.iterdir())
        if any(not entry.is_file() or entry.is_symlink() for entry in entries):
            raise ValueError(f"Ausgabeordner enthält Unterordner oder Symlinks: {dist}")
        unexpected = {entry.name for entry in entries} - expected_names()
        if unexpected:
            raise ValueError(f"Ausgabeordner enthält fremde Dateien: {sorted(unexpected)}")
    return dist


def build_into(dist: Path) -> list[Path]:
    source = load_script("build-testakten-release-zips.py", "ip_source_archives")
    individual = load_script("build-testakten-einzelpdf-zips.py", "ip_individual_archives")
    outputs: list[Path] = []
    for slug in SLUGS:
        folder = TESTAKTEN / slug
        combined = folder / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        if not combined.is_file():
            raise FileNotFoundError(combined)
        source_zip, source_count = source.build_single(folder, dist)
        individual_zip, individual_count = individual.build_single(folder, dist)
        if source_count < 2 or individual_count < 1:
            raise RuntimeError(f"{slug}: unvollständiger Paketbau")
        copied_pdf = dist / combined.name
        shutil.copy2(combined, copied_pdf)
        outputs.extend((source_zip, individual_zip, copied_pdf))
    checksums = dist / "SHA256SUMS.txt"
    checksums.write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in sorted(outputs)),
        encoding="utf-8",
    )
    outputs.append(checksums)
    return outputs


def build(raw_dist: Path) -> list[Path]:
    dist = validate_destination(raw_dist)
    dist.parent.mkdir(parents=True, exist_ok=True)
    stage: Path | None = Path(tempfile.mkdtemp(prefix=f".{dist.name}.staging-", dir=dist.parent))
    backup: Path | None = None
    try:
        staged_outputs = build_into(stage)
        if {path.name for path in staged_outputs} != expected_names():
            raise RuntimeError("Gebauter Assetumfang ist unvollständig")
        if dist.exists():
            backup = Path(tempfile.mkdtemp(prefix=f".{dist.name}.backup-", dir=dist.parent))
            backup.rmdir()
            dist.rename(backup)
        stage.rename(dist)
        stage = None
        if backup is not None:
            for entry in backup.iterdir():
                entry.unlink()
            backup.rmdir()
        return [dist / path.name for path in staged_outputs]
    except Exception:
        if backup is not None and backup.exists() and not dist.exists():
            backup.rename(dist)
        raise
    finally:
        if stage is not None and stage.exists():
            shutil.rmtree(stage)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path, default=ROOT / "dist" / "urheberrecht-ip-insolvenz")
    args = parser.parse_args()
    outputs = build(args.dist)
    print(f"{len(outputs)} Release-Dateien in {args.dist}")
    for path in outputs:
        print(path.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
