#!/usr/bin/env python3
"""Prüft Inhalt, Offenheit und die drei getrennten Auslieferungsformen."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
import tempfile
import zipfile
from email.parser import BytesParser
from email.policy import default
from email.utils import getaddresses, parsedate_to_datetime
from pathlib import Path

from pypdf import PdfReader

from testakte_disclaimer import NOTICE_FILENAME, notice_text_errors, pdf_content_errors
from testakte_download_notices import missing_notice_positions
from testakte_einzelpdf_common import expected_arcnames as expected_individual_names
from testakte_zip_common import source_zip_includes_gesamt_pdf, working_dump_expected_arcnames


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "scripts" / "data"
MODULES = (
    DATA / "urheberrecht_ip_insolvenz_marken.py",
    DATA / "urheberrecht_ip_insolvenz_software.py",
    DATA / "urheberrecht_ip_insolvenz_film.py",
)
ARTIFACT_MANIFEST = ROOT / "quality" / "legal" / "urheberrecht-ip-insolvenz-artifact-manifest.json"
MINIMUM_DOCUMENTS = {
    "markenrechte-sicherungsuebertragung-insolvenz-mannheim": 28,
    "kurpfalz-taxware-software-ip-insolvenz": 40,
    "filmrechte-sicherungsuebertragung-insolvenz-schwetzingen": 30,
}
ALLOWED_KINDS = {"docx", "pdf", "xlsx", "csv", "eml"}
PROHIBITED_SOLUTION_TEXT = re.compile(
    r"Musterlösung|fertiges Gutachten|Lösungsskizze|abschließende Anspruchsstrategie",
    re.IGNORECASE,
)
DECIMAL_HEADING = re.compile(r"^\d+(?:\.\d+)*\.?\s+\S")


def load_case(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Modul nicht ladbar: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CASE


def load_script(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Skript nicht ladbar: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def nested_text(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return "\n".join(nested_text(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return "\n".join(nested_text(item) for item in value)
    return str(value)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def spec_sha256(document: dict) -> str:
    payload = json.dumps(
        document,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def assert_artifact_manifest(cases: list[dict]) -> None:
    assert ARTIFACT_MANIFEST.is_file(), ARTIFACT_MANIFEST
    manifest = json.loads(ARTIFACT_MANIFEST.read_text(encoding="utf-8"))
    assert manifest.get("schema_version") == 1
    expected_slugs = {case["slug"] for case in cases}
    assert set(manifest.get("cases", {})) == expected_slugs
    for case in cases:
        slug = case["slug"]
        folder = ROOT / "testakten" / slug
        record = manifest["cases"][slug]
        rows = {row["path"]: row for row in record["documents"]}
        assert set(rows) == {document["path"] for document in case["documents"]}
        for document in case["documents"]:
            row = rows[document["path"]]
            assert row["spec_sha256"] == spec_sha256(document), (slug, document["path"], "spec")
            assert row["artifact_sha256"] == sha256_file(folder / document["path"]), (slug, document["path"], "artifact")
        combined = folder / "gesamt-pdf" / f"{slug}_gesamt.pdf"
        assert record["combined_pdf_sha256"] == sha256_file(combined), (slug, "combined")


def assert_readme_surfaces(cases: list[dict]) -> None:
    overview = (ROOT / "testakten" / "README.md").read_text(encoding="utf-8")
    plugin = (ROOT / "fachanwalt-urheber-medienrecht" / "README.md").read_text(encoding="utf-8")
    for case in cases:
        slug = case["slug"]
        source_asset = f"testakte-{slug}.zip"
        individual_asset = f"testakte-{slug}-einzelpdfs.zip"
        combined = f"./{slug}/gesamt-pdf/{slug}_gesamt.pdf"
        assert all(value in overview for value in (combined, source_asset, individual_asset)), slug
        assert all(value in plugin for value in (slug, source_asset, individual_asset)), slug


def assert_release_destination_safety() -> None:
    release = load_script(ROOT / "scripts" / "build-urheberrecht-ip-insolvenz-release.py", "ip_release_safety")
    for protected in (ROOT, ROOT / "testakten", ROOT / "scripts"):
        try:
            release.validate_destination(protected)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Gefährliches Ausgabeziel zugelassen: {protected}")
    with tempfile.TemporaryDirectory(prefix="ip-release-safety-") as raw:
        destination = Path(raw) / "release"
        destination.mkdir()
        (destination / "fremd.txt").write_text("nicht löschen", encoding="utf-8")
        try:
            release.validate_destination(destination)
        except ValueError:
            pass
        else:
            raise AssertionError("Fremd befüllter Ausgabeordner zugelassen")


def assert_source_case(case: dict) -> None:
    slug = case["slug"]
    documents = case["documents"]
    assert slug in MINIMUM_DOCUMENTS, slug
    assert len(documents) >= MINIMUM_DOCUMENTS[slug], (slug, len(documents))
    paths = [document["path"] for document in documents]
    assert len(paths) == len(set(paths)), f"{slug}: doppelte Pfade"
    assert all(document["kind"] in ALLOWED_KINDS for document in documents)
    assert all(Path(document["path"]).suffix.lower() == f'.{document["kind"]}' for document in documents)
    assert not PROHIBITED_SOLUTION_TEXT.search(nested_text(documents)), f"{slug}: Lösungstext"

    headings = [
        section["heading"]
        for document in documents
        for section in document.get("sections", [])
        if section.get("heading")
    ]
    assert headings, f"{slug}: keine gegliederten Dokumente"
    bad_headings = [heading for heading in headings if not DECIMAL_HEADING.match(heading)]
    assert not bad_headings, f"{slug}: nichtdezimal: {bad_headings[:5]}"

    for document in documents:
        if document["kind"] != "eml":
            continue
        addresses = [document["from"], *document.get("to", []), *document.get("cc", [])]
        parsed = [address for _, address in getaddresses(addresses)]
        assert parsed and all(address.lower().endswith(".example") for address in parsed), (slug, addresses)
        for attachment in document.get("attachments", []):
            assert attachment in paths, f"{slug}: fehlende E-Mail-Anlage {attachment}"

    assert any("unterschrieben" in path.lower() or "unterzeichnet" in path.lower() for path in paths), f"{slug}: unterzeichneter Deal fehlt"
    assert any(document["kind"] == "eml" and ("vollzug" in nested_text(document).lower() or "verwertung" in nested_text(document).lower()) for document in documents), f"{slug}: Vollzugsankündigung fehlt"
    if slug == "kurpfalz-taxware-software-ip-insolvenz":
        contracts = [path for path in paths if "arbeitsvertrag" in path.lower()]
        assert len(contracts) >= 5, contracts
        assert "69b" in nested_text(documents), "Softwareakte: Paragraf 69b fehlt"
    if slug == "filmrechte-sicherungsuebertragung-insolvenz-schwetzingen":
        text = nested_text(documents).lower()
        assert all(term in text for term in ("festplatte", "lizenzforderung", "filmhersteller")), "Filmakte: Gegenstandstrennung unvollständig"


def assert_built_case(case: dict, dist: Path | None) -> None:
    slug = case["slug"]
    folder = ROOT / "testakten" / slug
    assert (folder / "README.md").is_file()
    assert (folder / "rubric.yaml").is_file()
    for document in case["documents"]:
        path = folder / document["path"]
        assert path.is_file() and path.stat().st_size > 0, path
        if document["kind"] == "eml":
            message = BytesParser(policy=default).parsebytes(path.read_bytes())
            assert message["Subject"] == document["subject"], path
            assert message["Message-ID"] and str(message["Message-ID"]).startswith("<"), path
            message_date = parsedate_to_datetime(str(message["Date"]))
            assert message_date is not None and message_date.tzinfo is not None, path
            attachments = {part.get_filename(): part for part in message.iter_attachments()}
            for attachment in document.get("attachments", []):
                name = Path(attachment).name
                assert name in attachments, (path, name)
                if name.lower().endswith(".eml"):
                    part = attachments[name]
                    assert part.get_content_type() == "message/rfc822", (path, name)
                    nested = part.get_content()
                    expected = next(item for item in case["documents"] if item["path"] == attachment)
                    assert nested["Subject"] == expected["subject"], (path, name)
    combined = folder / "gesamt-pdf" / f"{slug}_gesamt.pdf"
    assert combined.is_file() and combined.stat().st_size > 0, combined
    assert not pdf_content_errors(combined.read_bytes()), slug
    reader = PdfReader(str(combined))
    assert len(reader.pages) >= 60, f"{slug}: nur {len(reader.pages)} Seiten"

    readme = (folder / "README.md").read_text(encoding="utf-8")
    assert "Akten-ZIP (Originalformate, ohne Gesamt-PDF)" in readme
    assert "Die Akte selbst enthält keine Musterlösung" in readme
    assert not missing_notice_positions(readme, case_readme=True), slug
    assert not source_zip_includes_gesamt_pdf(folder)

    if dist is None:
        return
    source_zip = dist / f"testakte-{slug}.zip"
    individual_zip = dist / f"testakte-{slug}-einzelpdfs.zip"
    assert source_zip.is_file() and individual_zip.is_file()

    with zipfile.ZipFile(source_zip) as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        assert names[0] == NOTICE_FILENAME
        assert not notice_text_errors(archive.read(NOTICE_FILENAME))
        assert sorted(names) == sorted(working_dump_expected_arcnames(folder, include_gesamt_pdf=False))
        assert not any("_gesamt.pdf" in name.lower() for name in names)
        assert not any(name.lower().endswith(".md") for name in names)
        assert not any("lösung" in name.lower() or "loesung" in name.lower() for name in names)
        assert not any("/" in name for name in names)

    with zipfile.ZipFile(individual_zip) as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        assert names[0] == NOTICE_FILENAME
        assert not notice_text_errors(archive.read(NOTICE_FILENAME))
        assert sorted(names) == sorted([NOTICE_FILENAME, *expected_individual_names(folder)])
        assert all(name == NOTICE_FILENAME or name.lower().endswith(".pdf") for name in names)
        for name in names:
            if name.lower().endswith(".pdf"):
                assert not pdf_content_errors(archive.read(name)), (slug, name)


def main() -> int:
    dist = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None
    cases = [load_case(path) for path in MODULES]
    assert {case["slug"] for case in cases} == set(MINIMUM_DOCUMENTS)
    assert_artifact_manifest(cases)
    assert_readme_surfaces(cases)
    assert_release_destination_safety()
    for case in cases:
        assert_source_case(case)
        assert_built_case(case, dist)
    if dist is not None:
        expected_release = {
            *(f"testakte-{slug}.zip" for slug in MINIMUM_DOCUMENTS),
            *(f"testakte-{slug}-einzelpdfs.zip" for slug in MINIMUM_DOCUMENTS),
            *(f"{slug}_gesamt.pdf" for slug in MINIMUM_DOCUMENTS),
            "SHA256SUMS.txt",
        }
        assert {path.name for path in dist.iterdir()} == expected_release
    print(f"OK: {len(cases)} IP-Insolvenzakten geprüft")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
