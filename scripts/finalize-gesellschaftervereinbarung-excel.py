#!/usr/bin/env python3
"""Ergänzt das Druckprofil der drei Kapitalblätter ohne Änderung ihrer Formeln."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "scripts/build-bau-rundum-excel.py"
spec = importlib.util.spec_from_file_location("print_profile", source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
path = (
    ROOT
    / "testakten/gesellschaftervereinbarung-drohnenfriseur-berlin/22_Kapital_und_Finanzierungsplan.xlsx"
)
module.print_profile(
    path,
    {
        "date": "09.10.2026",
        "sheets": [
            {
                "name": name,
                "columns": [{"width": 18} for _ in range(9)],
                "rows": [None] * 11,
            }
            for name in ("Kapital", "Tranchen", "Budget")
        ],
    },
)
path.with_suffix(path.suffix + ".inspect.ndjson").unlink(missing_ok=True)
