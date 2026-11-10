#!/usr/bin/env python3
"""Erzeugt die bearbeitbaren Originale für die Hamelner Auskunftsübung ME-36."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).with_name("data") / "compliance-hameln-auskunft.json"


def build(output_root: Path, node: Path, node_modules: Path, previews: Path | None) -> None:
    content = json.loads(DATA.read_text(encoding="utf-8"))
    if content["schema_version"] != 1 or len(content["cases"]) != 1:
        raise ValueError("Erwartet wird genau eine Akte im Schema 1.")
    case = content["cases"][0]
    if case["id"] != "ME-36" or case["slug"] != "compliance-hameln-auskunft-mit-schwaerzungen":
        raise ValueError("Fallkennung und Zielordner stimmen nicht überein.")
    documents = {record["filename"]: record for record in case["documents"]}
    if len(documents) != len(case["documents"]):
        raise ValueError("Doppelte Dateinamen im Vorgang.")

    spec = importlib.util.spec_from_file_location(
        "hameln_native_writer", ROOT / "scripts" / "build-projekteinkauf-baubranche-akten.py"
    )
    writer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(writer)
    directory = output_root / "testakten" / case["slug"]
    directory.mkdir(parents=True, exist_ok=True)
    workbooks = []
    emails = []
    for filename, record in documents.items():
        if not re.fullmatch(r"\d{2}_[A-Za-z0-9_]+\.(docx|eml|csv|xlsx)", filename):
            raise ValueError("Ungültiger Dateiname: " + filename)
        path = directory / filename
        match path.suffix:
            case ".docx":
                writer.write_docx(path, record, case)
            case ".csv":
                with path.open("w", newline="", encoding="utf-8") as stream:
                    csv.writer(stream, lineterminator="\n").writerows(writer.rows(record))
            case ".xlsx":
                for sheet in record["sheets"]:
                    writer.rows(sheet)
                workbooks.append({"path": str(path), "caseId": case["id"], "sheets": record["sheets"]})
            case ".eml":
                emails.append((path, record))
    writer.write_workbooks(workbooks, node, node_modules, previews)
    for path, record in emails:
        writer.write_eml(path, record, case, directory, documents)
    print(f"{case['id']}: {len(documents)} bearbeitbare Originale in {directory}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    parser.add_argument("--node", type=Path, required=True)
    parser.add_argument("--node-modules", type=Path, required=True)
    parser.add_argument("--xlsx-previews", type=Path)
    args = parser.parse_args()
    build(args.output_root.resolve(), args.node.resolve(), args.node_modules.resolve(), args.xlsx_previews)
