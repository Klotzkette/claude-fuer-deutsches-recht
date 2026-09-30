#!/usr/bin/env python3
"""Add a top-right exhibit label to a PDF submission copy."""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import stat
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any

from bea_common import (
    MAX_PDF_BYTES,
    ensure_bool,
    finite_number,
    hash_stable,
    read_stable,
    validate_pdf_dimensions,
    validate_pdf_page_count,
    validate_stamp_parameters,
)

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.errors import PyPdfError
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.pdfgen import canvas
except ImportError as exc:  # pragma: no cover - exercised by release environment
    raise SystemExit(
        "Fehlende PDF-Abhängigkeit. Installiere die Abhängigkeiten aus dem "
        "Repository-Stamm mit `python3 -m pip install -r requirements.txt` "
        "(pypdf und reportlab)."
    ) from exc


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Stempelt eine PDF-Versandkopie rechts oben als Anlage K1, B1 usw."
    )
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--label", help="Bezeichnung, z. B. 'Anlage K12'")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--pages", choices=("first", "all", "cover"), default="first")
    parser.add_argument("--font-size", type=float, default=10.0)
    parser.add_argument("--margin", type=float, default=24.0)
    parser.add_argument("--audit", type=Path, help="JSON-Audit mit Hashes schreiben")
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--allow-signed-copy",
        action="store_true",
        help="Signaturhinweis bewusst übergehen; Originalsignatur bleibt nur in der Originaldatei beweiskräftig",
    )
    parser.add_argument("--selftest", action="store_true")
    return parser


def _label_overlay(width: float, height: float, label: str, font_size: float, margin: float) -> bytes:
    stream = io.BytesIO()
    pdf = canvas.Canvas(stream, pagesize=(width, height))
    font = "Helvetica-Bold"
    text_width = stringWidth(label, font, font_size)
    padding_x = 5
    padding_y = 3
    box_width = text_width + 2 * padding_x
    box_height = font_size + 2 * padding_y
    if width < box_width + 2 * margin or height < box_height + 2 * margin:
        raise ValueError("PDF-Seite ist für Stempel und gewählten Rand zu klein")
    x = width - margin - box_width
    y = height - margin - box_height
    pdf.setFillColorRGB(1, 1, 1)
    pdf.setStrokeColorRGB(0, 0, 0)
    pdf.rect(x, y, box_width, box_height, fill=1, stroke=1)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont(font, font_size)
    pdf.drawString(x + padding_x, y + padding_y, label)
    pdf.save()
    return stream.getvalue()


def _fit_text(value: str, font: str, font_size: float, max_width: float) -> str:
    if max_width <= 0:
        raise ValueError("PDF-Seite ist für Deckblatttext zu schmal")
    if stringWidth(value, font, font_size) <= max_width:
        return value
    suffix = "..."
    shortened = value
    while shortened and stringWidth(shortened + suffix, font, font_size) > max_width:
        shortened = shortened[:-1]
    if not shortened:
        raise ValueError("Deckblatttext passt nicht auf die PDF-Seite")
    return shortened + suffix


def _visible_box(page: Any) -> tuple[float, float, float, float]:
    box = page.cropbox
    left = finite_number(box.left, "sichtbare PDF-Seite.linker Rand")
    bottom = finite_number(box.bottom, "sichtbare PDF-Seite.unterer Rand")
    width, height = validate_pdf_dimensions(box.width, box.height, "sichtbare PDF-Seite")
    return left, bottom, width, height


def _cover_page(width: float, height: float, label: str, source: Path, digest: str, font_size: float, margin: float) -> bytes:
    if width < 360 or height < 260:
        raise ValueError("PDF-Seite ist für ein Anlagen-Deckblatt zu klein")
    stream = io.BytesIO()
    pdf = canvas.Canvas(stream, pagesize=(width, height))
    overlay = PdfReader(
        io.BytesIO(_label_overlay(width, height, label, font_size, margin)), strict=True
    ).pages[0]
    # Draw the cover content first; the label overlay is merged by the caller.
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(54, height - 110, "Anlagen-Deckblatt")
    pdf.setFont("Helvetica", 10)
    safe_name = "".join(
        " "
        if unicodedata.category(character).startswith("C")
        or unicodedata.category(character) in {"Zl", "Zp"}
        else character
        for character in source.name
    )
    safe_name = " ".join(safe_name.split())[:90]
    source_line = _fit_text(f"Quelldatei: {safe_name}", "Helvetica", 10, width - 108)
    pdf.drawString(54, height - 140, source_line)
    pdf.drawString(54, height - 158, f"SHA-256 Original: {digest}")
    pdf.drawString(54, height - 194, "Das unveränderte Original wird in der Kontrollakte aufbewahrt.")
    pdf.save()
    cover_reader = PdfReader(io.BytesIO(stream.getvalue()), strict=True)
    cover = cover_reader.pages[0]
    cover.merge_page(overlay)
    writer = PdfWriter()
    writer.add_page(cover)
    output = io.BytesIO()
    writer.write(output)
    return output.getvalue()


def _file_identity(value: os.stat_result) -> tuple[int, int, int, int, int]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )


def _stable_source(path: Path) -> tuple[Path, bytes, str, os.stat_result]:
    requested = path.expanduser().absolute()
    if requested.is_symlink():
        raise ValueError("Eingabedatei darf kein symbolischer Link sein")
    before = requested.lstat()
    raw, digest = read_stable(requested, max_bytes=MAX_PDF_BYTES)
    after = requested.lstat()
    if _file_identity(before) != _file_identity(after) or len(raw) != before.st_size:
        raise ValueError("Eingabedatei wurde während des Lesens verändert")
    return requested, raw, digest, before


def _same_existing_file(first: Path, second: Path) -> bool:
    try:
        return first.exists() and second.exists() and first.samefile(second)
    except OSError:
        return False


def _publish_pdf(temporary: Path, output: Path, force: bool) -> None:
    if force:
        os.replace(temporary, output)
        return
    try:
        os.link(temporary, output)
    except FileExistsError as exc:
        raise ValueError(f"Ausgabedatei existiert bereits: {output}") from exc
    temporary.unlink()


def _write_atomic_text(path: Path, text: str, *, force: bool = False) -> None:
    requested = path.expanduser().absolute()
    if requested.is_symlink():
        raise ValueError("Auditpfad darf kein symbolischer Link sein")
    if requested.exists():
        status = requested.lstat()
        if not stat.S_ISREG(status.st_mode):
            raise ValueError("Auditpfad muss eine reguläre Datei sein")
        if not force:
            raise ValueError(f"Auditdatei existiert bereits: {requested}")
    requested.parent.mkdir(parents=True, exist_ok=True)
    descriptor, raw_temp = tempfile.mkstemp(prefix=f".{requested.name}.", suffix=".tmp", dir=requested.parent)
    temporary = Path(raw_temp)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        if force:
            os.replace(temporary, requested)
        else:
            try:
                os.link(temporary, requested)
            except FileExistsError as exc:
                raise ValueError(f"Auditdatei existiert bereits: {requested}") from exc
            temporary.unlink()
    finally:
        temporary.unlink(missing_ok=True)


def _validate_audit_path(audit: Path, source: Path, output: Path, *, force: bool = False) -> None:
    requested = audit.expanduser().absolute()
    if requested.is_symlink():
        raise ValueError("Auditpfad darf kein symbolischer Link sein")
    audit_target = audit.expanduser().absolute().resolve(strict=False)
    source_target = source.expanduser().absolute().resolve(strict=False)
    output_target = output.expanduser().absolute().resolve(strict=False)
    if audit_target in {source_target, output_target}:
        raise ValueError("Auditpfad darf weder Original noch Ausgabe-PDF überschreiben")
    if _same_existing_file(audit_target, source_target) or _same_existing_file(audit_target, output_target):
        raise ValueError("Auditpfad verweist auf Original oder Ausgabe-PDF")
    if requested.exists():
        if not stat.S_ISREG(requested.lstat().st_mode):
            raise ValueError("Auditpfad muss eine reguläre Datei sein")
        if not force:
            raise ValueError(f"Auditdatei existiert bereits: {requested}")


def _page_rotation(page: Any) -> int:
    value = page.get("/Rotate", 0) or 0
    numeric = finite_number(value, "PDF-Seitenrotation")
    if not numeric.is_integer() or int(numeric) % 90:
        raise ValueError("PDF-Seitenrotation muss ein endliches Vielfaches von 90 Grad sein")
    return int(numeric) % 360


def stamp_pdf(
    source: Path,
    output: Path,
    label: str,
    pages_mode: str,
    font_size: float,
    margin: float,
    force: bool,
    allow_signed_copy: bool,
) -> dict[str, Any]:
    label, pages_mode, font_size, margin = validate_stamp_parameters(
        label, pages_mode, font_size, margin
    )
    force = ensure_bool(force, "force")
    allow_signed_copy = ensure_bool(allow_signed_copy, "allow_signed_copy")
    requested_output = output.expanduser().absolute()
    if requested_output.is_symlink():
        raise ValueError("Ausgabedatei darf kein symbolischer Link sein")
    if requested_output.suffix.casefold() != ".pdf":
        raise ValueError("Ausgabedatei muss die Endung .pdf haben")
    if requested_output.exists():
        if not stat.S_ISREG(requested_output.lstat().st_mode):
            raise ValueError("Ausgabepfad muss eine reguläre PDF-Datei sein")
        if not force:
            raise ValueError(f"Ausgabedatei existiert bereits: {requested_output}")
    output = requested_output.resolve(strict=False)
    source, raw, source_digest, source_stat = _stable_source(source)
    if source == output or _same_existing_file(source, output):
        raise ValueError("Original darf nicht überschrieben werden")
    if re.match(rb"^%PDF-(?:1\.[0-7]|2\.0)(?:\r?\n|\r)", raw) is None:
        raise ValueError("Eingabedatei hat keinen unterstützten PDF-Dateikopf")
    if b"%%EOF" not in raw[-2048:]:
        raise ValueError("Eingabedatei hat keine PDF-Endemarkierung am Dateiende")
    signed_hint = re.search(rb"/ByteRange\b", raw) is not None
    if signed_hint and not allow_signed_copy:
        raise ValueError(
            "Quelldatei enthält einen Signaturhinweis. Nicht neu serialisieren; "
            "Original sichern und Deckblatt-/Versandlösung anwaltlich festlegen."
        )

    reader = PdfReader(io.BytesIO(raw), strict=True)
    if reader.is_encrypted:
        raise ValueError("Verschlüsseltes PDF kann nicht gestempelt werden")
    input_pages = validate_pdf_page_count(len(reader.pages), "Eingabe-PDF")
    expected_pages = validate_pdf_page_count(
        input_pages + (1 if pages_mode == "cover" else 0), "Ausgabe-PDF"
    )
    writer = PdfWriter()

    if pages_mode == "cover":
        first = reader.pages[0]
        width, height = validate_pdf_dimensions(
            first.mediabox.width, first.mediabox.height, "erste PDF-Seite"
        )
        cover = PdfReader(
            io.BytesIO(
                _cover_page(width, height, label, source, source_digest, font_size, margin)
            ),
            strict=True,
        ).pages[0]
        writer.add_page(cover)

    for index, page in enumerate(reader.pages):
        rotation = _page_rotation(page)
        if rotation and hasattr(page, "transfer_rotation_to_content"):
            page.transfer_rotation_to_content()
        should_stamp = pages_mode == "all" or (pages_mode == "first" and index == 0)
        if should_stamp:
            left, bottom, width, height = _visible_box(page)
            overlay = PdfReader(
                io.BytesIO(_label_overlay(width, height, label, font_size, margin)),
                strict=True,
            ).pages[0]
            page.merge_translated_page(overlay, left, bottom)
        writer.add_page(page)

    writer.add_metadata(
        {
            "/Title": label,
            "/Subject": "Anlagenkopie für elektronischen Rechtsverkehr",
            "/Creator": "dieselgate bea-anlagenstempel",
        }
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, raw_temp = tempfile.mkstemp(prefix=f".{output.name}.", suffix=".tmp", dir=output.parent)
    os.close(descriptor)
    temporary = Path(raw_temp)
    try:
        with temporary.open("wb") as handle:
            writer.write(handle)
            handle.flush()
            os.fsync(handle.fileno())
        output_size, output_digest = hash_stable(temporary, max_bytes=MAX_PDF_BYTES)
        if output_size < 1:
            raise ValueError("Ausgabe-PDF ist leer")
        with temporary.open("rb") as handle:
            check = PdfReader(handle, strict=True)
            if check.is_encrypted:
                raise ValueError("Ausgabe-PDF ist unerwartet verschlüsselt")
            actual_output_pages = validate_pdf_page_count(len(check.pages), "Ausgabe-PDF")
        if actual_output_pages != expected_pages:
            raise ValueError("Seitenzahl der Ausgabe weicht unerwartet ab")
        current_size, current_digest = hash_stable(source, max_bytes=MAX_PDF_BYTES)
        current = source.lstat()
        if (
            _file_identity(current) != _file_identity(source_stat)
            or current_size != len(raw)
            or current_digest != source_digest
        ):
            raise ValueError("Original wurde während der Verarbeitung verändert; Ausgabe verworfen")
        _publish_pdf(temporary, output, force)
    finally:
        temporary.unlink(missing_ok=True)
    return {
        "schema_version": "1.0.0",
        "input": str(source),
        "output": str(output),
        "label": label,
        "pages_mode": pages_mode,
        "input_pages": input_pages,
        "output_pages": actual_output_pages,
        "input_sha256": source_digest,
        "output_sha256": output_digest,
        "signed_input_hint": signed_hint,
        "original_unchanged": True,
        "visual_qa_required": True,
    }


def selftest() -> None:
    with tempfile.TemporaryDirectory(prefix="bea-stempel-test-") as raw:
        root = Path(raw)
        source = root / "original.pdf"
        output = root / "anlage.pdf"
        pdf = canvas.Canvas(str(source), pagesize=(595, 842))
        pdf.setFont("Helvetica", 12)
        pdf.drawString(54, 760, "Kaufvertrag vom 14. Mai 2020")
        pdf.showPage()
        pdf.drawString(54, 760, "Seite 2")
        pdf.save()
        report = stamp_pdf(source, output, "Anlage K12", "first", 10, 24, False, False)
        assert report["input_pages"] == 2
        assert report["output_pages"] == 2
        assert report["original_unchanged"]
        assert report["output_sha256"] == hash_stable(output, max_bytes=MAX_PDF_BYTES)[1]
        extracted = PdfReader(output, strict=True).pages[0].extract_text() or ""
        assert "Anlage K12" in extracted
        cover_output = root / "anlage_mit_deckblatt.pdf"
        cover = stamp_pdf(source, cover_output, "Anlage K13", "cover", 10, 24, False, False)
        assert cover["output_pages"] == 3
        assert "Anlage K13" in (
            PdfReader(cover_output, strict=True).pages[0].extract_text() or ""
        )
        signed = root / "signiert.pdf"
        signed.write_bytes(source.read_bytes() + b"\n/ByteRange [0 1 2 3]\n")
        try:
            stamp_pdf(signed, root / "signiert_neu.pdf", "Anlage K14", "first", 10, 24, False, False)
        except ValueError as exc:
            assert "Signaturhinweis" in str(exc)
        else:
            raise AssertionError("signiertes PDF hätte gesperrt werden müssen")
        for invalid_mode, invalid_font, invalid_margin in (
            ("invalid", 10, 24),
            ("first", float("nan"), 24),
            ("first", 10, float("inf")),
        ):
            try:
                stamp_pdf(source, root / f"invalid-{invalid_mode}.pdf", "Anlage K15", invalid_mode, invalid_font, invalid_margin, False, False)
            except ValueError:
                pass
            else:
                raise AssertionError("ungültige Stempelparameter hätten gesperrt werden müssen")
        try:
            _validate_audit_path(output, source, output)
        except ValueError:
            pass
        else:
            raise AssertionError("Audit-/PDF-Pfadkollision hätte gesperrt werden müssen")
        existing = root / "existing.pdf"
        existing.write_bytes(b"do not overwrite")
        try:
            stamp_pdf(source, existing, "Anlage K16", "first", 10, 24, False, False)
        except ValueError:
            assert existing.read_bytes() == b"do not overwrite"
        else:
            raise AssertionError("bestehende Ausgabe hätte ohne --force gesperrt werden müssen")
        linked = root / "original-hardlink.pdf"
        os.link(source, linked)
        try:
            stamp_pdf(source, linked, "Anlage K17", "first", 10, 24, True, False)
        except ValueError as exc:
            assert "Original" in str(exc)
        else:
            raise AssertionError("Hardlink auf Original hätte gesperrt werden müssen")
        for invalid_label in (
            "Anlage K0",
            "Anlage K01",
            "Anlage K1000000",
            "Anlage K١",
            "Anlage K\u200b1",
        ):
            try:
                stamp_pdf(
                    root / "fehlt.pdf",
                    root / "ungueltig.pdf",
                    invalid_label,
                    "first",
                    10,
                    24,
                    False,
                    False,
                )
            except ValueError as exc:
                assert "label" in str(exc)
            else:
                raise AssertionError("ungültiges Anlagenlabel hätte vor Datei-I/O scheitern müssen")
        assert validate_stamp_parameters("Anlage ABCDEF999999", "all", 6, 100) == (
            "Anlage ABCDEF999999",
            "all",
            6.0,
            100.0,
        )
        try:
            _page_rotation({"/Rotate": 10**10_000})
        except ValueError:
            pass
        else:
            raise AssertionError("überlaufende PDF-Rotation hätte kontrolliert scheitern müssen")
        oversized = root / "zu-gross.pdf"
        with oversized.open("wb") as handle:
            handle.truncate(MAX_PDF_BYTES + 1)
        try:
            stamp_pdf(
                oversized,
                root / "zu-gross-ausgabe.pdf",
                "Anlage K18",
                "first",
                10,
                24,
                False,
                False,
            )
        except ValueError as exc:
            assert "Größengrenze" in str(exc)
        else:
            raise AssertionError("übergroße Eingabe hätte gesperrt werden müssen")
        audit_path = root / "kontrolle" / "audit.json"
        _write_atomic_text(audit_path, '{"ok":true}\n')
        assert audit_path.read_text(encoding="utf-8") == '{"ok":true}\n'
        try:
            _write_atomic_text(audit_path, '{"ok":false}\n')
        except ValueError as exc:
            assert "existiert bereits" in str(exc)
            assert audit_path.read_text(encoding="utf-8") == '{"ok":true}\n'
        else:
            raise AssertionError("bestehendes Audit hätte ohne --force erhalten bleiben müssen")
        _write_atomic_text(audit_path, '{"ok":false}\n', force=True)
        assert audit_path.read_text(encoding="utf-8") == '{"ok":false}\n'
    print("bea-anlagenstempel selftest OK")


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return 0
    if args.input is None or args.label is None:
        parser.error("input und --label sind erforderlich")
    output = args.output or args.input.with_name(f"{args.input.stem}_gestempelt.pdf")
    try:
        if args.audit is not None:
            _validate_audit_path(args.audit, args.input, output, force=args.force)
        report = stamp_pdf(
            args.input,
            output,
            args.label,
            args.pages,
            args.font_size,
            args.margin,
            args.force,
            args.allow_signed_copy,
        )
        rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.audit:
            _write_atomic_text(args.audit, rendered, force=args.force)
    except (OSError, ValueError, PyPdfError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
