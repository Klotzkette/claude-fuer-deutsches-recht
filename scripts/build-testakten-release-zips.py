#!/usr/bin/env python3
"""Baut die Testakten-ZIPs fuer Releases.

Die ZIPs enthalten die Arbeitsdateien, das Gesamt-PDF und die verbindliche
zweisprachige README.txt, aber keine Markdown-, Download- oder Vorfuehrseiten.
Alle Dateien liegen ohne Unterordner unmittelbar auf der Wurzelebene.

Aufruf:
  python3 scripts/build-testakten-release-zips.py [dist]            # alle Testakten
  python3 scripts/build-testakten-release-zips.py [dist] <name> ... # gezielt
"""

from __future__ import annotations

import sys
import shutil
import zipfile
from pathlib import Path

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_zip_common import working_dump_flat_pairs

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {
    "megaprompts",
}
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def write_file(zipf: zipfile.ZipFile, path: Path, arcname: str) -> None:
    """Schreibt eine Datei streamend mit stabilen ZIP-Metadaten."""
    info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    with path.open("rb") as source, zipf.open(info, "w") as target:
        shutil.copyfileobj(source, target, length=1024 * 1024)


def write_bytes(zipf: zipfile.ZipFile, data: bytes, arcname: str) -> None:
    """Schreibt erzeugten Inhalt mit stabilen ZIP-Metadaten."""
    info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zipf.writestr(info, data)


def add_testakte(zipf: zipfile.ZipFile, testakte_dir: Path) -> int:
    write_bytes(zipf, NOTICE_BYTES, NOTICE_FILENAME)
    count = 1
    for path, arcname in working_dump_flat_pairs(
        testakte_dir,
        include_gesamt_pdf=True,
    ):
        write_file(zipf, path, arcname)
        count += 1
    return count


def build_single(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    out = dist / f"testakte-{testakte_dir.name}.zip"
    temporary = out.with_name(f".{out.name}.tmp")
    try:
        with zipfile.ZipFile(
            temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1
        ) as zipf:
            count = add_testakte(zipf, testakte_dir)
        if count == 0:
            temporary.unlink(missing_ok=True)
            out.unlink(missing_ok=True)
        else:
            temporary.replace(out)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return out, count


def _is_testakte_name(arg: str) -> bool:
    return "/" not in arg and "\\" not in arg and (TESTAKTEN / arg).is_dir()


def main() -> None:
    argv = sys.argv[1:]
    dist = REPO_ROOT / "dist"
    targets: list[str] = []
    for arg in argv:
        if _is_testakte_name(arg):
            targets.append(arg)
        elif dist == REPO_ROOT / "dist":
            dist = Path(arg)
        else:
            targets.append(arg)
    dist.mkdir(parents=True, exist_ok=True)
    all_dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS)
    dirs = all_dirs
    if targets:
        unknown = sorted(set(targets) - {d.name for d in dirs})
        if unknown:
            raise SystemExit(f"Unbekannte Testakten: {unknown}")
        dirs = [d for d in dirs if d.name in targets]
    if not dirs:
        print("Keine Testakten gefunden.")
        return

    total_files = 0
    built: list[Path] = []
    for d in dirs:
        out, count = build_single(d, dist)
        if count == 0:
            raise SystemExit(f"{d}: keine exportfaehigen Dateien")
        total_files += count
        built.append(out)
        print(f"Baue {out.name}: {count} Dateien")

    bundle_archives = [dist / f"testakte-{d.name}.zip" for d in all_dirs]
    missing_archives = [path.name for path in bundle_archives if not path.is_file()]
    if missing_archives:
        raise SystemExit(
            "Zentralarchiv unvollstaendig; zuerst fehlende Einzelarchive bauen: "
            + ", ".join(missing_archives[:10])
        )

    all_out = dist / "alle-testakten.zip"
    all_temporary = all_out.with_name(f".{all_out.name}.tmp")
    try:
        with zipfile.ZipFile(
            all_temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1
        ) as zipf:
            for archive in bundle_archives:
                write_file(zipf, archive, archive.name)
        all_temporary.replace(all_out)
    except Exception:
        all_temporary.unlink(missing_ok=True)
        raise
    print(f"Baue {all_out.name}: {len(bundle_archives)} flache Einzel-ZIPs")
    print(f"Fertig: {len(dirs)} Einzel-ZIPs, {total_files} Dateien")


if __name__ == "__main__":
    main()
