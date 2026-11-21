#!/usr/bin/env python3
"""Prüft die tatsächlichen Aktenstücke, ihre Ablage, Mailanlagen, vollständigen PDF-Ausgaben und Kursmappe."""

import argparse
import json
from pathlib import Path

from akteneingang.fallpruefung import check, inspect_case
from akteneingang.quellen import ROOT, Sources, digest, members
from testakte_disclaimer import NOTICE_FILENAME, NOTICE_BYTES


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--dist", type=Path)
    cli.add_argument("--cache", type=Path)
    cli.add_argument("--local-index", type=Path)
    args = cli.parse_args()
    dist = args.dist
    master = {}
    if dist:
        checks = {
            n: h
            for h, n in (
                r.split("  ", 1)
                for r in (dist / "checksums-sha256.txt").read_text().splitlines()
            )
        }
        check(
            len(checks) == 28
            and set(checks)
            == {p.name for p in dist.iterdir()} - {"checksums-sha256.txt"},
            "Releaseumfang",
        )
        for name, h in checks.items():
            check(digest((dist / name).read_bytes()) == h, name + " Prüfsumme")
        master = members(
            (dist / "allgemeines-notariat-alle-testakten.zip").read_bytes()
        )
        check(master.pop(NOTICE_FILENAME).startswith(NOTICE_BYTES), "Kursmappenhinweis")
        plugin = members((dist / "allgemeines-notariat.zip").read_bytes())
        for n in (
            ".claude-plugin/plugin.json",
            ".codex-plugin/plugin.json",
            "plugin.json",
        ):
            check(
                json.loads(plugin[n])["name"] == "allgemeines-notariat", "Paketmanifest"
            )
        check(
            len([p for p in plugin if p.endswith("/SKILL.md")]) == 10
            and not any(p.startswith("testakten/") for p in plugin),
            "Installationsumfang",
        )
    data = ROOT / "scripts/data"
    cases = sorted((data / "allgemeines-notariat").glob("*.json"))
    check(len(cases) == 7, "Fallzahl")
    total = pages = 0
    for source in cases:
        case = json.loads(source.read_text())
        files, count = inspect_case(case, dist, suite=ROOT / "allgemeines-notariat/testakten", prefix="testakte-notariat-")
        total += len(files) - 1
        pages += count
        if dist:
            for name, b in files.items():
                check(
                    master.pop("Amtsgeschaefte/" + case["id"] + "/" + name) == b, name
                )
    if dist:
        passed = Sources(args.cache, args.local_index)
        stock = json.loads((data / "notariat-bestandsakten.json").read_text())
        check(len(stock) == 13, "Bestandsaktenzahl")
        for key, record in stock.items():
            for name, b in members(passed.read(record)).items():
                check(
                    master.pop("Weitere_Notariatsakten/" + key + "/" + name) == b, name
                )
        check(not master, "Fremddateien in der Kursmappe")
    print(
        f"Sieben Amtsgeschäfte: {total} Arbeitsunterlagen, {pages} PDF-Seiten, alle Nachrichten, Anlagen und Arbeitsvorlagen geprüft."
    )
    if dist:
        print(
            "13 mitgelieferte Bestandsakten byteweise abgeglichen, 29 Freigabedateien geprüft."
        )


if __name__ == "__main__":
    main()
