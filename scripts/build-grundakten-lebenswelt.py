#!/usr/bin/env python3
"""Baut einzelne vollständige Akten, Druckpakete und ihren fallbezogenen Bestandsnachweis."""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

from akteneingang.ausgabe import build
from akteneingang.quellen import DATA, Sources, catalogs, digest
from akteneingang.vertiefung import fachauswahl
from akteneingang.verweise import routes
from release_routing import case_asset_url
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

SHEETS = ("a-f", "g-q", "r-z", "lokal", "weitere")


def einzelquellen(records, requested):
    """Übernimmt einzeln veröffentlichte Original- und PDF-ZIPs für ausgewählte Fachakten."""
    editions = json.loads((DATA.parent / "grundakten-vertiefung/einzelausgaben.json").read_text(encoding="utf-8"))
    selected = records.copy()
    for key, checksums in editions.items():
        if key not in records:
            continue
        slug = records[key].get("id", key.split("/")[-1])
        if slug not in requested:
            continue
        record = records[key].copy()
        for field, suffix in (("source", ""), ("print", "-einzelpdfs")):
            record[field] = {**checksums[field], "url": case_asset_url(slug, suffix)}
        selected[key] = record
    return selected


def write_bytes(path, data):
    tmp = path.with_suffix(path.suffix + ".part")
    tmp.write_bytes(data)
    tmp.replace(path)


def single(job):
    key, record, row, slug, stage, dist, cache, index, version = job
    folder = stage / slug
    folder.mkdir(exist_ok=True)
    inventory = folder / "bestand.json"
    original = dist / ("lebensakte-" + slug + ".zip")
    data_sig = digest(
        json.dumps([version, record, row], ensure_ascii=False, sort_keys=True).encode()
    )
    if inventory.exists():
        prev = json.loads(inventory.read_text())
        if (
            prev["redaktion"] == data_sig
            and original.is_file()
            and digest(original.read_bytes()) == prev["original"]["sha256"]
            and all((folder / k).is_file() for k in prev["druck"])
        ):
            return slug, None
    try:
        native, print_zip, combined, count, added = build(
            key, record, row, Sources(cache, index)
        )
        write_bytes(original, native)
        result = {
            "redaktion": data_sig,
            "aktenpfad": key,
            "aktenstuecke": count,
            "eingangspost": added,
            "original": {
                "datei": original.name,
                "sha256": digest(native),
                "bytes": len(native),
            },
            "druck": {},
        }
        if print_zip is not None:
            for name, data in (
                ("Einzel-PDFs.zip", print_zip),
                ("Gesamtakte.pdf", combined),
            ):
                write_bytes(folder / name, data)
                result["druck"][name] = {"sha256": digest(data), "bytes": len(data)}
        write_bytes(
            inventory,
            (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode(),
        )
        return slug, None
    except (ValueError, KeyError, OSError, RuntimeError) as exc:
        return slug, repr(exc)


def package(dest, paths):
    with ZipFile(dest.with_suffix(".part"), "w") as z:
        for name, p in [(NOTICE_FILENAME, None), *paths]:
            data = NOTICE_BYTES if p is None else p.read_bytes()
            info = ZipInfo(name, (2000, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data, compress_type=ZIP_STORED)
    dest.with_suffix(".part").replace(dest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for arg in ("dist", "stage", "cache", "local-index"):
        parser.add_argument("--" + arg, type=Path, required=arg in ("dist", "stage"))
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--redaktion", choices=SHEETS, nargs="+", default=SHEETS)
    parser.add_argument("--akte", action="append", default=[],
                        help="Einzelakte nach Slug. Mit --vertiefung gilt ihre jüngste registrierte Einzelausgabe.")
    parser.add_argument("--historisch", action="store_true",
                        help="Mit --vertiefung --akte die Bezugsfassung der historischen Fachsammlung verwenden.")
    parser.add_argument("--paketieren", action="store_true")
    parser.add_argument(
        "--vertiefung",
        action="store_true",
        help="Fachausgabe mit erweiterten Originalen und weiterem Schriftwechsel",
    )
    parser.add_argument(
        "--platzsparend",
        action="store_true",
        help="Geprüfte temporäre Druckdateien nach der Paketierung freigeben",
    )
    args = parser.parse_args()
    if args.historisch and not (args.vertiefung and args.akte):
        parser.error("--historisch erfordert --vertiefung und --akte")
    for d in (args.stage, args.dist):
        d.mkdir(parents=True, exist_ok=True)
    records = catalogs()
    targets = routes(records)
    articles = {}
    for name in args.redaktion:
        for k, v in json.loads((DATA / (name + ".json")).read_text()).items():
            key = k if "/" in k else "testakten/" + k
            if key in articles:
                raise ValueError("Doppelte Akte: " + key)
            articles[key] = v
    if args.vertiefung:
        if args.paketieren and set(articles) != set(records):
            raise ValueError("Paketierung erfordert die vollständige Redaktion")
        records, articles, targets = fachauswahl(records, articles)
        if args.akte and not (args.historisch or args.paketieren):
            records = einzelquellen(records, args.akte)
    source_dir = Path(__file__).parent
    version = digest(
        b"".join(
            (source_dir / part).read_bytes()
            for part in (
                "akteneingang/ausgabe.py",
                "akteneingang/dokumente.py",
                "akteneingang/korrespondenz.py",
                "akteneingang/vertiefung.py",
                "akteneingang/arbeitsfassungen.py",
            )
        )
    )
    jobs = []
    for key, row in articles.items():
        slug, part = targets[key]
        if not args.akte or slug in args.akte:
            jobs.append(
                (
                    key,
                    records[key],
                    row,
                    slug,
                    args.stage,
                    args.dist,
                    args.cache,
                    args.local_index,
                    version,
                )
            )
    if args.paketieren and (set(articles) != set(records) or len(jobs) != len(records)):
        raise ValueError("Paketierung setzt die gesamte Redaktion voraus")
    failures = []
    with ProcessPoolExecutor(args.jobs) as executor:
        for i, (slug, error) in enumerate(executor.map(single, jobs), 1):
            if error:
                failures.append(slug)
                print("FEHLER", slug, error, flush=True)
            if i % 25 == 0:
                print(f"{i}/{len(jobs)}", flush=True)
    if failures:
        raise SystemExit(f"{len(failures)} Akten mit Fehlern")
    if not args.paketieren:
        return
    inventory = {}
    groups = {}
    for key, (slug, part) in targets.items():
        directory = args.stage / slug
        row = json.loads((directory / "bestand.json").read_text())
        if row["druck"]:
            row["lesepaket"] = part
            for name, ref in row["druck"].items():
                src = directory / name
                if digest(src.read_bytes()) != ref["sha256"]:
                    raise ValueError(str(src))
                groups.setdefault(part, []).append((slug + "/" + name, src))
        inventory[slug] = row
    for part, paths in groups.items():
        package(args.dist / part, paths)
        with ZipFile(args.dist / part) as z:
            if (
                z.read(NOTICE_FILENAME) != NOTICE_BYTES
                or len(z.namelist()) != len(paths) + 1
            ):
                raise ValueError("Unvollständiges Lesepaket: " + part)
            for name, path in paths:
                if digest(z.read(name)) != digest(path.read_bytes()):
                    raise ValueError("Abweichende PDF im Paket: " + name)
        if args.platzsparend:
            for _, path in paths:
                path.unlink()
    write_bytes(
        args.dist / "release-bestand.json",
        (json.dumps(inventory, indent=2, ensure_ascii=False) + "\n").encode(),
    )
    expected = (
        {v["original"]["datei"] for v in inventory.values()}
        | set(groups)
        | {"release-bestand.json"}
    )
    unexpected = (
        {p.name for p in args.dist.iterdir()} - expected - {"checksums-sha256.txt"}
    )
    if unexpected:
        raise ValueError("Fremddateien im Ziel: " + str(unexpected))
    checksums = "".join(
        f"{digest((args.dist / name).read_bytes())}  {name}\n"
        for name in sorted(expected)
    )
    write_bytes(args.dist / "checksums-sha256.txt", checksums.encode())
    print(f"{len(inventory)} Akten, {len(groups)} Druckpakete", flush=True)


if __name__ == "__main__":
    main()
