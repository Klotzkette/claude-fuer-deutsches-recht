#!/usr/bin/env python3
"""Lesende Fachdaten-/Artefaktregression ohne Fonts, Office oder ArtifactTool."""
from __future__ import annotations
import argparse
import ast
import csv
from datetime import datetime
from email import policy
from email.parser import BytesParser
import io
import json
from pathlib import Path
import re
import posixpath
import shutil
import tempfile
import zipfile
import xml.etree.ElementTree as ET

from docx import Document
from openpyxl import load_workbook
from PIL import Image
from pypdf import PdfReader
import pdfplumber

from bav_konzern_verify import verify_inventory, INVENTORY, sha
from testakte_file_filter import include_in_working_dump
from testakte_grundakte import check_intake_member
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
ERRORS = {"#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A", "#NUM!", "#NULL!", "#SPILL!", "#CALC!"}


def independent_formula(formula, values):
    """Unabhängige Auswertung des bewusst einfachen Rechenumfangs der Falltabellen."""
    expression = formula[1:].replace("$", "")
    def total(match):
        return str(sum(float(cell.value or 0) for row in values[match[1]] for cell in row))
    expression = re.sub(r"SUM\(([A-Z]+\d+:[A-Z]+\d+)\)", total, expression)
    expression = re.sub(r"\b[A-Z]+\d+\b", lambda m: str(values[m[0]].value), expression)
    def walk(node):
        if isinstance(node, ast.Expression): return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)): return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -walk(node.operand)
        if isinstance(node, ast.BinOp):
            left, right = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            if isinstance(node.op, ast.Mult): return left * right
            if isinstance(node.op, ast.Div): return left / right
            if isinstance(node.op, ast.Pow): return left ** right
        raise ValueError(f"Ungeprüfte Formeloperation: {formula}")
    return walk(ast.parse(expression, mode="eval"))


def norm(text):
    return re.sub(r"\s+", "", text).replace("\u00ad", "")


def office_text(path):
    with zipfile.ZipFile(path) as z:
        texts = []
        assert len(z.namelist()) == len(set(z.namelist())), path
        for name in z.namelist():
            if name.endswith(".rels"):
                rels = ET.fromstring(z.read(name))
                ids = [r.attrib["Id"] for r in rels]
                assert len(ids) == len(set(ids)), f"Doppelte Office-Relationship: {path}:{name}"
                owner = posixpath.dirname(posixpath.dirname(name))
                for relation in rels:
                    if relation.get("TargetMode") == "External": continue
                    target = relation.get("Target", "")
                    member = posixpath.normpath(target.lstrip("/") if target.startswith("/") else posixpath.join(owner, target))
                    assert member in z.namelist(), f"Defekte Office-Relationship {path}:{name}->{member}"
            if name.endswith(".xml"):
                root = ET.fromstring(z.read(name))
                texts.append(" ".join(root.itertext()))
        return "\n".join(texts)


def check_native(root):
    counts = []
    for fp in sorted((root / "scripts/data/bav-konzern-faelle").glob("*.json")):
        case = json.loads(fp.read_text())
        directory = root / "testakten" / case["slug"]
        items = [x for k in ("documents", "workbooks", "slides") for x in case.get(k, [])]
        assert 35 <= len(items) <= 50, (case["slug"], len(items))
        assert len({i["path"] for i in items}) == len(items)
        assert {Path(i["path"]).suffix for i in items} >= {".pdf", ".docx", ".xlsx", ".eml", ".csv", ".png", ".pptx"}
        for item in items:
            path = directory / item["path"]
            assert path.is_file(), path
            assert include_in_working_dump(path, directory), f"Exportfilter blockiert {path}"
            data = path.read_bytes()
            if item["path"].startswith("Grundakte/"):
                check_intake_member(item["path"], data)
            suffix = path.suffix.lower()
            if suffix in {".docx", ".xlsx", ".pptx"}:
                text = office_text(path)
            elif suffix == ".pdf":
                reader = PdfReader(path)
                assert reader.pages
                text = "\n".join(p.extract_text() or "" for p in reader.pages)
                with pdfplumber.open(path) as layout:
                    body_text = "\n".join(p.crop((0, 110, p.width, p.height - 60)).extract_text() or "" for p in layout.pages)
                for paragraph in item.get("body", []):
                    assert norm(paragraph) in norm(body_text), f"PDF-Inhalt verloren: {path}: {paragraph[:70]}"
                fonts = [str(f.get_object().get("/BaseFont", "")) for f in reader.pages[0]["/Resources"]["/Font"].get_object().values()]
                assert any("TimesNewRoman" in font for font in fonts), f"TNR fehlt: {path}: {fonts}"
            elif suffix == ".eml":
                message = BytesParser(policy=policy.default).parsebytes(data)
                assert all(message[h] for h in ("From", "To", "Date", "Subject", "Message-ID"))
                text = message.get_body(preferencelist=("plain",)).get_content()
                expected = {Path(r).name: (directory / r).read_bytes() for r in item.get("attachments", [])}
                actual = {a.get_filename(): a.get_payload(decode=True) for a in message.iter_attachments()}
                assert actual == expected, f"MIME-Anlage nicht byteidentisch: {path}"
            elif suffix == ".csv":
                text = data.decode("utf-8-sig")
                rows = list(csv.reader(io.StringIO(text), delimiter=";"))
                expected = item.get("csv", item)
                assert rows[0] == expected["columns"]
                assert rows[1:] == [[str(v) for v in row] for row in expected["rows"]]
            elif suffix == ".png":
                with Image.open(path) as image:
                    image.verify()
                text = "\n".join(item.get("body", []))
            else:
                text = data.decode()
            assert not re.search(r"yamamoto|kyoto|[\uFFFD]", text, re.I), f"Altname/Zeichenfehler: {path}"
            assert "Diese Testakte wurde mit KI generiert" not in text, path
            if suffix == ".docx":
                document = Document(path)
                assert document.styles["Normal"].font.name == "Times New Roman"
                assert document.styles["Normal"].font.size.pt == 11
                assert [p.text for p in document.paragraphs if p.style.name == "Title"] == [item.get("subject") or item["title"]]
                body = "\n".join(p.text for p in document.paragraphs)
                for paragraph in item["body"]:
                    assert paragraph in body
            if suffix == ".xlsx":
                formulas = load_workbook(path, data_only=False)
                values = load_workbook(path, data_only=True)
                assert formulas.sheetnames == [s["name"] for s in item["sheets"]]
                for source in item["sheets"]:
                    sh, val = formulas[source["name"]], values[source["name"]]
                    for i, row in enumerate(source["rows"], 6):
                        for j, expected in enumerate(row, 1):
                            actual = sh.cell(i, j).value
                            expected_cell = datetime.fromisoformat(expected) if isinstance(expected, str) and (re.fullmatch(r"\d{4}-\d{2}-\d{2}", expected) or source.get("formats", {}).get(source["columns"][j-1]) == "date") else expected
                            assert actual == expected_cell or expected == "" and actual is None, (path, source["name"], i, j, actual, expected)
                            if isinstance(expected, str) and expected.startswith("="):
                                assert val.cell(i, j).value is not None, f"Formelcache fehlt {path}:{i}:{j}"
                                independent = independent_formula(expected, val)
                                assert abs(val.cell(i, j).value - independent) < .005, f"Falscher Formelwert {path}:{i}:{j}"
                            assert val.cell(i, j).value not in ERRORS
                for control in item.get("controls", []):
                    actual = values[control["sheet"]][control["cell"]].value
                    assert abs(actual - control["expected"]) < .005, (path, control, actual)
                formulas.close()
                values.close()
            if suffix == ".pptx":
                with zipfile.ZipFile(path) as z:
                    slides = [n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
                    assert len(slides) == len(item["slides"])
        if case["slug"] == "bav-strategie-konzern-meissner-rheinwerk-ag":
            control = case["controls"]
            rows = case["workbooks"][0]["sheets"][0]["rows"]
            assert len(rows) == control["order_count"] == 14
            assert sum(sum(r[3:6]) for r in rows) == control["population_total"] == 9686
            assert sum(r[6] for r in rows) == control["ifrs_total_eur"] == 1682000000
            people = case["workbooks"][1]["sheets"][0]["rows"]
            assert len(people) == control["selected_persons"] == 48
            assert sum(r[5] for r in people) == control["selected_salary_total_eur"]
            assert all(r[4] >= r[3] + 16 for r in people), "Unplausibles Eintrittsalter"
        if case["slug"] == "bav-carve-out-rheinbogen-automation":
            control = case["controls"]
            people = case["workbooks"][0]["sheets"][0]["rows"]
            assert len(people) == control["selected_persons"] == 60
            assert sum(r[5] == "2019 Holding-Wechsel" for r in people) == control["holding_special_persons"] == 12
            rows = case["workbooks"][0]["sheets"][1]["rows"][:3]
            assert [r[1] for r in rows] == [control["active_total"], control["deferred_total"], control["retired_total"]]
            assert sum(r[2] for r in rows) == control["operating_obligation_eur"] == 46800000
            assert control["cta_operating_eur"] + control["cta_holding_eur"] == control["cta_total_eur"] == 28000000
        if case["slug"] == "bav-rentnergesellschaft-rheinhafen-logistik":
            control = case["controls"]
            selected = next(d["csv"]["rows"] for d in case["documents"] if "Detailbestand_48" in d["path"])
            assert len(selected) == control["selected_persons"] == 48
            rows = case["workbooks"][1]["sheets"][1]["rows"][:3]
            assert sum(r[1] for r in rows) == control["population_total"] == 1426
            assert sum(r[2] for r in rows) == control["monthly_pensions_eur"] == 620000
            assert 12 * sum(r[2] for r in rows) == control["annual_pensions_eur"] == 7440000
            assert sum(r[3] for r in rows) == control["plan_obligation_eur"] == 86400000
            assets = case["workbooks"][0]["sheets"][0]["rows"][:4]
            assert sum(r[1] - r[2] for r in assets) == control["initial_assets_eur"] == 84000000
            assert control["property_old_eur"] - control["property_debt_eur"] - control["property_repair_eur"] == control["property_arithmetic_net_eur"] == 8500000
        if case["slug"] == "bav-pensionskasse-niederrhein-verbund":
            control = case["controls"]
            rows = case["workbooks"][0]["sheets"][0]["rows"][:3]
            assert sum(r[1] for r in rows) == control["pensioners"] == 680
            assert sum(r[2] for r in rows) == control["guarantee_before_monthly_eur"] == 300000
            assert sum(r[4] for r in rows) == control["guarantee_after_monthly_eur"] == 282000
            assert sum(r[3] for r in rows) == control["surplus_before_monthly_eur"] == 60000
            assert sum(r[5] for r in rows) == control["surplus_after_monthly_eur"] == 55000
            assert sum(r[2] - r[4] for r in rows) == control["guarantee_gap_monthly_eur"] == 18000
            assert sum(r[2] + r[3] - r[4] - r[5] for r in rows) == control["total_gap_monthly_eur"] == 23000
            people = next(d["csv"]["rows"] for d in case["documents"] if "42" in d["path"] and d["path"].endswith(".csv"))
            assert len(people) == control["selected_persons"] == 42
            portfolio = case["workbooks"][1]["sheets"][2]["rows"][:3]
            assert sum(r[1] for r in portfolio) == control["active"] == 1460
            assert sum(r[2] for r in portfolio) == control["deferred"] == 320
        counts.append({"slug": case["slug"], "documents": len(items)})
    assert len(counts) == 4, "Vier bAV-Akten erforderlich"
    return counts


def check_reading_copies(root):
    """Native Word-/Folieninhalte müssen auch im tatsächlich ausgelieferten PDF stehen."""
    for fp in sorted((root / "scripts/data/bav-konzern-faelle").glob("*.json")):
        case = json.loads(fp.read_text())
        directory = root / "testakten" / case["slug"]
        names = dict(document_arcname_pairs(directory))
        archive = root / "bav-strategie-konzern/testakten/downloads" / f"testakte-{case['slug']}-einzelpdfs.zip"
        with zipfile.ZipFile(archive) as z:
            for item in case["documents"]:
                if not item["path"].endswith(".docx"):
                    continue
                data = z.read(names[directory / item["path"]])
                with pdfplumber.open(io.BytesIO(data)) as pdf:
                    body = "\n".join(p.crop((0, 110, p.width, p.height - 60)).extract_text() or "" for p in pdf.pages)
                for paragraph in [item.get("subject") or item["title"], *item["body"]]:
                    assert norm(paragraph) in norm(body), f"Word-Lesefassung verliert Inhalt: {item['path']}: {paragraph[:80]}"
            for item in case["slides"]:
                pdf = PdfReader(io.BytesIO(z.read(names[directory / item["path"]])))
                assert len(pdf.pages) == len(item["slides"])
                for page, slide in zip(pdf.pages, item["slides"]):
                    text = norm(page.extract_text() or "")
                    for paragraph in [slide["title"], *slide["bullets"]]:
                        assert norm(paragraph) in text, f"Folien-Lesefassung verliert Inhalt: {item['path']}: {paragraph}"


def mutation_regression(root):
    """Beweist Ablehnung alter Quellen und manipulierter PDF-Innenbytes."""
    with tempfile.TemporaryDirectory(prefix="bav-regression-") as temp:
        copy = Path(temp)
        inventory = json.loads((root / INVENTORY).read_text())
        paths = {INVENTORY, *(r["path"] for r in inventory["generators"])}
        for c in inventory["cases"]:
            paths.update(r["path"] for r in c["sources"])
            paths.update([c["fixture"]["path"], c["pdf_zip"]["path"], c["gesamt_pdf"]["path"]])
        for relative in paths:
            target = copy / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / relative, target)
        verify_inventory(copy)
        def rejected():
            try:
                verify_inventory(copy)
            except ValueError:
                return
            raise AssertionError("Manipulation wurde nicht erkannt")
        source = copy / inventory["cases"][0]["sources"][0]["path"]
        original = source.read_bytes()
        source.write_bytes(original + b" stale")
        rejected()
        source.write_bytes(original)
        archive = copy / inventory["cases"][0]["pdf_zip"]["path"]
        with zipfile.ZipFile(archive) as z:
            contents = {n: z.read(n) for n in z.namelist()}
        name = next(n for n in contents if n.endswith(".pdf"))
        contents[name] += b"\n% changed PDF bytes\n"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
            for n, data in contents.items():
                z.writestr(n, data)
        inventory["cases"][0]["pdf_zip"]["sha256"] = sha(archive.read_bytes())
        (copy / INVENTORY).write_text(json.dumps(inventory))
        rejected()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--skip-inventory", action="store_true")
    args = parser.parse_args()
    counts = check_native(args.root)
    if not args.skip_inventory:
        verify_inventory(args.root)
        check_reading_copies(args.root)
        mutation_regression(args.root)
    print(json.dumps({"cases": counts, "inventory": not args.skip_inventory, "mutations_rejected": not args.skip_inventory}, ensure_ascii=False))


if __name__ == "__main__":
    main()
