#!/usr/bin/env python3
"""Build an auditable beA pleading package from a strict JSON order."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import unicodedata
from datetime import datetime
from pathlib import Path
from types import ModuleType
from typing import Any

from bea_common import (
    APPROVAL_CONFIRMATIONS,
    APPROVAL_SCHEMA_VERSION,
    ContractError,
    MANIFEST_SCHEMA_VERSION,
    MAX_PDF_BYTES,
    digest_json,
    exhibit_filename,
    load_json,
    main_filename,
    package_fingerprint,
    read_stable,
    validate_pdf_dimensions,
    validate_pdf_page_count,
    validate_order,
)

try:
    from pypdf import PdfReader
except ImportError as exc:  # pragma: no cover - exercised by release/runtime setup
    raise SystemExit(
        "Fehlende PDF-Abhängigkeit. Installiere die Abhängigkeiten aus dem "
        "Repository-Stamm mit `python3 -m pip install -r requirements.txt` "
        "(pypdf und reportlab), bevor ein beA-Paket gebaut wird."
    ) from exc


REGISTER_COLUMNS = [
    "reihenfolge",
    "anlage",
    "bezeichnung",
    "quelldatei",
    "versanddatei",
    "fundstelle_im_schriftsatz",
    "seiten",
    "sha256_original",
    "sha256_versand",
    "konvertierung",
    "ocr",
    "stempel",
    "freigabe",
    "bemerkung",
]
_TOOL_CACHE: dict[str, ModuleType] = {}


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Erzeugt aus einem validierten Paketauftrag atomar original/arbeit/versand/kontrolle, "
            "Anlagenverzeichnis, Hashliste, Manifest und Freigabevorlage."
        )
    )
    parser.add_argument("order", nargs="?", type=Path, help="bea-paketauftrag.json")
    parser.add_argument("--output", type=Path, help="neuer Zielordner des beA-Pakets")
    parser.add_argument("--selftest", action="store_true")
    return parser


def _load_tool(name: str, filename: str) -> ModuleType:
    cached = _TOOL_CACHE.get(filename)
    if cached is not None:
        return cached
    path = Path(__file__).resolve().with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ContractError(f"Werkzeug kann nicht geladen werden: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except SystemExit as exc:
        raise ContractError(f"Werkzeug kann nicht geladen werden: {path}: {exc}") from exc
    _TOOL_CACHE[filename] = module
    return module


def _write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    descriptor = os.open(path, flags, 0o600)
    try:
        with os.fdopen(descriptor, "wb", closefd=False) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        os.close(descriptor)


def _write_text(path: Path, content: str) -> None:
    _write_bytes(path, content.encode("utf-8"))


def _resolve_source(order_path: Path, source_value: str) -> Path:
    candidate = Path(source_value).expanduser()
    if not candidate.is_absolute():
        candidate = order_path.parent / candidate
    requested = candidate.absolute()
    if requested.is_symlink():
        raise ContractError(f"Quelldatei darf kein symbolischer Link sein: {requested}")
    try:
        resolved = requested.resolve(strict=True)
    except OSError as exc:
        raise ContractError(f"Quelldatei fehlt: {requested}") from exc
    if resolved.suffix.casefold() != ".pdf":
        raise ContractError(f"Quelldatei muss vor Paketbau als PDF vorliegen: {resolved}")
    return resolved


def _pdf_page_count(content: bytes, location: str) -> int:
    try:
        reader = PdfReader(io.BytesIO(content), strict=True)
        if reader.is_encrypted:
            raise ContractError(f"{location}: verschlüsseltes PDF ist unzulässig")
        pages = validate_pdf_page_count(len(reader.pages), f"{location}.Seitenzahl")
        for index, page in enumerate(reader.pages, start=1):
            validate_pdf_dimensions(
                page.mediabox.width,
                page.mediabox.height,
                f"{location}.Seite[{index}].MediaBox",
            )
            validate_pdf_dimensions(
                page.cropbox.width,
                page.cropbox.height,
                f"{location}.Seite[{index}].CropBox",
            )
    except ContractError:
        raise
    except Exception as exc:
        raise ContractError(f"{location}: PDF kann nicht zuverlässig gelesen werden: {exc}") from exc
    return pages


def _csv_safe(value: object) -> str:
    text = str(value).replace("\r", " ").replace("\n", " ").replace("\x00", "")
    text = "".join(
        " " if unicodedata.category(character).startswith("C") else character
        for character in text
    )
    text = " ".join(text.split())
    probe = unicodedata.normalize("NFKC", text).lstrip()
    if probe.startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def _md(value: object) -> str:
    text = str(value).replace("\r", " ").replace("\n", " ")
    text = html.escape(" ".join(text.split()), quote=False)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("`", "&#96;")


def _write_register(path: Path, rows: list[list[object]]) -> None:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(REGISTER_COLUMNS)
    for row in rows:
        writer.writerow([_csv_safe(value) for value in row])
    _write_text(path, stream.getvalue())


def _control_markdown(manifest: dict[str, Any]) -> str:
    matter = manifest["matter"]
    docket = matter["docket"] or "Neueingang"
    lines = [
        "# beA-Versandkontrolle",
        "",
        "**Status:** `FREIGABE_AUSSTEHEND`",
        "",
        "## Vorgang",
        "",
        "| Feld | Wert |",
        "| --- | --- |",
        f"| Gericht | {_md(matter['court'])} |",
        f"| Aktenzeichen oder Neueingang | {_md(docket)} |",
        f"| Parteirolle | {_md(matter['role'])} |",
        f"| Schriftsatzart | {_md(matter['document_type'])} |",
        f"| Frist | {_md(matter['deadline'] or 'keine im Auftrag')} |",
        f"| Verantwortliche Person | {_md(matter['responsible_person'])} |",
        f"| Signatur-/Versandweg | {_md(matter['signature_route'])} |",
        f"| Paket-Fingerprint | `{manifest['package_fingerprint']}` |",
        "",
        "## Inhaltliche und visuelle Freigabe",
        "",
        "- [ ] Hauptdokument ist die freigegebene Endfassung; Hash stimmt mit dem Auftrag überein.",
        "- [ ] Rubrum, Anträge, Tatsachen, Rechtsausführungen, Gericht, Aktenzeichen und Datum sind geprüft.",
        "- [ ] Jede Anlagenbezugnahme ist vollständig und eindeutig einer Versanddatei zugeordnet.",
        "- [ ] Stempel, Dateiname, Bezugnahme und Anlagenverzeichnis sind deckungsgleich.",
        "- [ ] Jede PDF wurde gerendert und auf Seitenfolge, Orientierung, Vollständigkeit und Lesbarkeit geprüft.",
        "- [ ] Frist, Empfänger, Aktenzeichen und Signatur-/Versandweg sind geprüft.",
        "",
        "## Technische Produktion",
        "",
        "- [x] Originale und Versandkopien sind getrennt; SHA-256-Werte sind dokumentiert.",
        "- [x] Das Paketmanifest bindet Metadaten, Bezugnahmen, Dateinamen, Größen und Hashes.",
        "- [ ] `bea-paket-pruefer.py` nach Anlage von `kontrolle/freigabe.json` erneut ausführen.",
        "",
        "## beA-Handkontrolle nach Freigabe",
        "",
        "- [ ] Richtigen Empfänger, Nachrichtart und Aktenzeichen/Neueingang im beA auswählen.",
        "- [ ] Alle und nur die freigegebenen Dateien aus `versand/` in dokumentierter Reihenfolge anhängen.",
        "- [ ] Einfache/qES-Signatur und persönliche Versendung durch die verantwortende Person prüfen.",
        "- [ ] Nach Versand automatisierte gerichtliche Eingangsbestätigung kontrollieren und speichern.",
        "",
        "Die strukturierte Freigabe ist ein interner Kontrollnachweis, keine elektronische Signatur und kein Versandnachweis.",
        "",
    ]
    return "\n".join(lines)


def _approval_template(fingerprint: str) -> dict[str, Any]:
    return {
        "schema_version": APPROVAL_SCHEMA_VERSION,
        "package_fingerprint": fingerprint,
        "approved_by": "[AUSZUFUELLEN]",
        "approved_at": "[ISO-ZEITPUNKT-MIT-ZEITZONE]",
        "confirmations": {key: False for key in APPROVAL_CONFIRMATIONS},
    }


def _manifest_file(name: str, kind: str, label: str | None, content: bytes) -> dict[str, Any]:
    return {
        "name": name,
        "kind": kind,
        "label": label,
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
    }


def build_package(order_path: Path, output_path: Path) -> dict[str, Any]:
    requested_order = order_path.expanduser().absolute()
    if requested_order.is_symlink():
        raise ContractError("Paketauftrag darf kein symbolischer Link sein")
    order = validate_order(load_json(requested_order))
    order_hash = digest_json(order)

    output = output_path.expanduser().absolute()
    if output.exists() or output.is_symlink():
        raise ContractError(f"Zielordner existiert bereits; kein Überschreiben: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.parent.is_symlink():
        raise ContractError(f"Zielordner-Elternpfad darf kein symbolischer Link sein: {output.parent}")

    stamper = _load_tool("bea_anlagenstempel_builder", "bea-anlagenstempel.py")
    checker = _load_tool("bea_paket_pruefer_builder", "bea-paket-pruefer.py")

    main_source = _resolve_source(requested_order, order["main_document"]["source"])
    exhibit_sources = [
        _resolve_source(requested_order, exhibit["source"]) for exhibit in order["exhibits"]
    ]
    source_identities: dict[tuple[int, int], str] = {}
    total_source_bytes = 0
    for label, source in [
        ("Hauptdokument", main_source),
        *(
            (f"Anlage {order['matter']['exhibit_prefix']}{exhibit['number']}", source)
            for exhibit, source in zip(order["exhibits"], exhibit_sources)
        ),
    ]:
        status = source.stat()
        identity = (status.st_dev, status.st_ino)
        if identity in source_identities:
            raise ContractError(
                f"{label}: dieselbe Quelldatei/Hardlink ist bereits als {source_identities[identity]} zugeordnet"
            )
        source_identities[identity] = label
        if status.st_size > MAX_PDF_BYTES:
            raise ContractError(f"{label}: Quelldatei überschreitet {MAX_PDF_BYTES} Bytes")
        total_source_bytes += status.st_size
    if total_source_bytes > MAX_PDF_BYTES:
        raise ContractError(
            f"Quelldateien umfassen {total_source_bytes} Bytes und überschreiten die 200-MB-Paketgrenze"
        )

    temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}.bau-", dir=output.parent))
    try:
        original_dir = temporary / "original"
        work_dir = temporary / "arbeit"
        send_dir = temporary / "versand"
        control_dir = temporary / "kontrolle"
        for directory in (original_dir, work_dir, send_dir, control_dir):
            directory.mkdir()

        matter = order["matter"]
        main_raw, main_digest = read_stable(main_source, max_bytes=MAX_PDF_BYTES)
        consumed_source_bytes = len(main_raw)
        if main_digest != order["main_document"]["approved_sha256"]:
            raise ContractError(
                "Hauptdokument-Hash weicht vom anwaltlich freigegebenen approved_sha256 ab"
            )
        _pdf_page_count(main_raw, "Hauptdokument")
        main_original_name = "00_Hauptdokument_Original.pdf"
        main_send_name = main_filename(matter)
        _write_bytes(original_dir / main_original_name, main_raw)
        _write_bytes(send_dir / main_send_name, main_raw)

        files = [_manifest_file(main_send_name, "hauptdokument", None, main_raw)]
        main_manifest = {
            "source_name": main_source.name,
            "original_name": main_original_name,
            "versand_name": main_send_name,
            "input_sha256": main_digest,
            "versand_sha256": main_digest,
            "bytes": len(main_raw),
        }
        exhibit_manifests: list[dict[str, Any]] = []
        register_rows: list[list[object]] = []
        total_exhibits = len(order["exhibits"])
        width = max(2, len(str(max(total_exhibits, 1))))

        for index, (exhibit, source) in enumerate(
            zip(order["exhibits"], exhibit_sources), start=1
        ):
            source_raw, source_digest = read_stable(source, max_bytes=MAX_PDF_BYTES)
            consumed_source_bytes += len(source_raw)
            if consumed_source_bytes > MAX_PDF_BYTES:
                raise ContractError(
                    "tatsächlich gelesene Quelldateien überschreiten die 200-MB-Paketgrenze"
                )
            if source_digest != exhibit["expected_sha256"]:
                raise ContractError(
                    f"Anlage {matter['exhibit_prefix']}{exhibit['number']}: Quell-Hash weicht vom Auftrag ab"
                )
            input_pages = _pdf_page_count(
                source_raw, f"Anlage {matter['exhibit_prefix']}{exhibit['number']}"
            )
            order_token = f"{index:0{width}d}"
            label = f"Anlage {matter['exhibit_prefix']}{exhibit['number']}"
            original_name = f"{order_token}_Anlage_{matter['exhibit_prefix']}{exhibit['number']}_Original.pdf"
            send_name = exhibit_filename(index, total_exhibits, exhibit, matter["exhibit_prefix"])
            original_copy = original_dir / original_name
            work_copy = work_dir / send_name
            _write_bytes(original_copy, source_raw)

            if exhibit["stamp_mode"] == "already_stamped":
                _write_bytes(work_copy, source_raw)
                stamp_audit = {
                    "schema_version": "1.0.0",
                    "input": f"original/{original_name}",
                    "output": f"arbeit/{send_name}",
                    "label": label,
                    "pages_mode": "already_stamped",
                    "input_pages": input_pages,
                    "output_pages": input_pages,
                    "input_sha256": source_digest,
                    "output_sha256": source_digest,
                    "signed_input_hint": b"/ByteRange" in source_raw,
                    "original_unchanged": True,
                    "visual_qa_required": True,
                }
            else:
                try:
                    stamp_audit = stamper.stamp_pdf(
                        original_copy,
                        work_copy,
                        label,
                        exhibit["stamp_mode"],
                        10.0,
                        24.0,
                        False,
                        False,
                    )
                except Exception as exc:
                    raise ContractError(f"{label}: Stempelproduktion fehlgeschlagen: {exc}") from exc
                stamp_audit["input"] = f"original/{original_name}"
                stamp_audit["output"] = f"arbeit/{send_name}"
            work_raw, work_digest = read_stable(work_copy, max_bytes=MAX_PDF_BYTES)
            output_pages = _pdf_page_count(work_raw, label)
            if stamp_audit["output_sha256"] != work_digest:
                raise ContractError(f"{label}: Stempel-Audit und Arbeitskopie weichen ab")
            _write_bytes(send_dir / send_name, work_raw)
            _write_text(
                control_dir / f"{matter['exhibit_prefix']}{exhibit['number']}_stempel_audit.json",
                json.dumps(stamp_audit, ensure_ascii=False, indent=2) + "\n",
            )
            file_entry = _manifest_file(send_name, "anlage", label, work_raw)
            files.append(file_entry)
            exhibit_manifest = {
                "order": index,
                "number": exhibit["number"],
                "label": label,
                "title": exhibit["title"],
                "document_date": exhibit["document_date"],
                "reference": exhibit["reference"],
                "source_name": source.name,
                "original_name": original_name,
                "versand_name": send_name,
                "input_sha256": source_digest,
                "versand_sha256": work_digest,
                "bytes": len(work_raw),
                "input_pages": input_pages,
                "output_pages": output_pages,
                "stamp_mode": exhibit["stamp_mode"],
                "visual_qa_required": True,
            }
            exhibit_manifests.append(exhibit_manifest)
            register_rows.append(
                [
                    index,
                    f"{matter['exhibit_prefix']}{exhibit['number']}",
                    exhibit["title"],
                    source.name,
                    send_name,
                    exhibit["reference"],
                    f"{input_pages}/{output_pages}",
                    source_digest,
                    work_digest,
                    "unverändert" if exhibit["stamp_mode"] == "already_stamped" else "Stempelkopie",
                    "nein",
                    exhibit["stamp_mode"],
                    "ausstehend",
                    "visuelle PDF-Abnahme erforderlich",
                ]
            )

        manifest = {
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "order_sha256": order_hash,
            "matter": matter,
            "main_document": main_manifest,
            "exhibits": exhibit_manifests,
            "files": files,
            "package_fingerprint": "0" * 64,
        }
        manifest["package_fingerprint"] = package_fingerprint(manifest)
        _write_text(
            control_dir / "paketauftrag-normalisiert.json",
            json.dumps(order, ensure_ascii=False, indent=2) + "\n",
        )
        _write_text(
            control_dir / "paket-manifest.json",
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        )
        _write_register(control_dir / "anlagenverzeichnis.csv", register_rows)
        hashes = "".join(f"{item['sha256']}  {item['name']}\n" for item in files)
        _write_text(control_dir / "versanddateien-sha256.txt", hashes)
        _write_text(control_dir / "versandkontrolle.md", _control_markdown(manifest))
        _write_text(
            control_dir / "freigabe-vorlage.json",
            json.dumps(_approval_template(manifest["package_fingerprint"]), ensure_ascii=False, indent=2) + "\n",
        )

        report = checker.validate_package(
            temporary,
            matter["role"],
            matter["exhibit_prefix"],
            matter["first_exhibit_number"],
            matter["docket"],
        )
        if report["status"] != "FREIGABE_AUSSTEHEND" or report["errors"] or report["warnings"]:
            raise ContractError(f"gebautes Paket besteht die Eigenprüfung nicht: {report}")

        final_report = report
        final_report["package"] = str(output / "versand")
        final_report["manifest"]["path"] = str(output / "kontrolle" / "paket-manifest.json")
        final_report["manifest"]["order_path"] = str(
            output / "kontrolle" / "paketauftrag-normalisiert.json"
        )
        checker.write_report(
            temporary / "kontrolle" / "bea-pruefbericht.json",
            json.dumps(final_report, ensure_ascii=False, indent=2) + "\n",
            temporary / "versand",
        )
        result = {
            "status": "FREIGABE_AUSSTEHEND",
            "package": str(output),
            "package_fingerprint": manifest["package_fingerprint"],
            "files": len(files),
            "bytes": sum(item["bytes"] for item in files),
            "next_step": (
                "PDFs visuell prüfen, freigabe-vorlage.json als freigabe.json vollständig bestätigen "
                "und bea-paket-pruefer.py erneut ausführen."
            ),
        }
        if output.exists() or output.is_symlink():
            raise ContractError(f"Zielordner wurde während des Paketbaus angelegt: {output}")
        os.replace(temporary, output)
        return result
    except Exception:
        raise
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def selftest() -> None:
    try:
        from reportlab.pdfgen import canvas
    except ImportError as exc:
        raise ContractError("reportlab fehlt für den Paketbauer-Selbsttest") from exc

    with tempfile.TemporaryDirectory(prefix="bea-paket-bauer-test-") as raw:
        root = Path(raw)
        inputs = root / "input"
        inputs.mkdir()
        main = inputs / "Replik final.pdf"
        exhibit = inputs / "Kaufvertrag.pdf"
        for path, text in ((main, "Freigegebene Replik"), (exhibit, "Kaufvertrag vom 14. Mai 2020")):
            pdf = canvas.Canvas(str(path), pagesize=(595, 842))
            pdf.drawString(54, 760, text)
            pdf.save()
        main_hash = hashlib.sha256(main.read_bytes()).hexdigest()
        exhibit_hash = hashlib.sha256(exhibit.read_bytes()).hexdigest()
        order = {
            "schema_version": "1.0.0",
            "matter": {
                "court": "Landgericht Stuttgart",
                "docket": "16 O 123/24",
                "new_filing": False,
                "role": "K",
                "document_type": "Replik",
                "document_date": "2026-07-14",
                "deadline": "2026-07-15",
                "responsible_person": "Rechtsanwältin Test",
                "signature_route": "einfach_signiert_persoenliches_beA",
                "exhibit_prefix": "K",
                "first_exhibit_number": 12,
            },
            "main_document": {
                "source": "input/Replik final.pdf",
                "approved_sha256": main_hash,
            },
            "exhibits": [
                {
                    "number": 12,
                    "source": "input/Kaufvertrag.pdf",
                    "expected_sha256": exhibit_hash,
                    "title": "Kaufvertrag",
                    "document_date": "2020-05-14",
                    "reference": "Replik S. 3 Abs. 2",
                    "stamp_mode": "first",
                }
            ],
        }
        order_path = root / "bea-paketauftrag.json"
        order_path.write_text(json.dumps(order, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        output = root / "bea-paket"
        built = build_package(order_path, output)
        assert built["status"] == "FREIGABE_AUSSTEHEND"
        assert len(list((output / "versand").glob("*.pdf"))) == 2
        approval = load_json(output / "kontrolle" / "freigabe-vorlage.json")
        approval["approved_by"] = "Rechtsanwältin Test"
        approval["approved_at"] = load_json(output / "kontrolle" / "paket-manifest.json")[
            "created_at"
        ]
        approval["confirmations"] = {key: True for key in APPROVAL_CONFIRMATIONS}
        (output / "kontrolle" / "freigabe.json").write_text(
            json.dumps(approval, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        checker = _load_tool("bea_paket_pruefer_builder_selftest", "bea-paket-pruefer.py")
        final = checker.validate_package(output, "K", "K", 12, "16 O 123/24")
        assert final["status"] == "VERSANDFERTIG", final
        main_send = next((output / "versand").glob("00_K_*.pdf"))
        main_send.write_bytes(main_send.read_bytes() + b"\n")
        tampered = checker.validate_package(output, "K", "K", 12, "16 O 123/24")
        assert tampered["status"] == "NICHT_VERSANDFERTIG"
        assert any("weicht ab" in item for item in tampered["errors"])
        duplicate = inputs / "Kaufvertrag_Duplikat.pdf"
        os.link(exhibit, duplicate)
        duplicate_order = json.loads(json.dumps(order))
        duplicate_order["exhibits"].append(
            {
                "number": 13,
                "source": "input/Kaufvertrag_Duplikat.pdf",
                "expected_sha256": exhibit_hash,
                "title": "Kaufvertrag Duplikat",
                "document_date": "2020-05-14",
                "reference": "Replik S. 4 Abs. 1",
                "stamp_mode": "first",
            }
        )
        duplicate_order_path = root / "bea-paketauftrag-duplikat.json"
        duplicate_order_path.write_text(
            json.dumps(duplicate_order, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        try:
            build_package(duplicate_order_path, root / "bea-paket-duplikat")
        except ContractError as exc:
            assert "Quelldatei/Hardlink" in str(exc)
        else:
            raise AssertionError("doppelt zugeordneter Quellen-Hardlink hätte gesperrt werden müssen")
    print("bea-paket-bauer selftest OK (Inputvertrag, Paketbau, Freigabe, Manipulationssperre)")


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    if args.selftest:
        try:
            selftest()
        except (OSError, ContractError, ValueError) as exc:
            print(f"FEHLER: {exc}", file=sys.stderr)
            return 1
        return 0
    if args.order is None or args.output is None:
        parser.error("order und --output sind erforderlich")
    try:
        result = build_package(args.order, args.output)
    except (OSError, ContractError, ValueError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
