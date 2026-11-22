"""Erzeugt die vollständige Arbeitsakte und passende Druckunterlagen aus den geprüften Bezugsfassungen."""

from __future__ import annotations

import importlib.util
import io
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

from .arbeitsfassungen import ergaenze
from .dokumente import add_member, render
from .korrespondenz import poststuecke
from .quellen import ROOT, digest, localpath, members, safe_member


def archive(files):
    out = io.BytesIO()
    with ZipFile(out, "w") as stream:
        for name, content in files.items():
            add_member(stream, safe_member(name), content)
    return out.getvalue()


def include(files, name, content, provenance):
    if name not in files or files[name] == content:
        files[name] = content
        return
    alternate = provenance + "/" + name
    if alternate in files and files[alternate] != content:
        raise ValueError("Nicht eindeutiges Aktenstück: " + alternate)
    files[alternate] = content


def intake_path(name):
    for old in ("Praxisnachtrag/Grundakte/", "01_Grundakte_ohne_Loesung/"):
        if name.startswith(old):
            prefix = (
                "Grundakte/Praxisnachtrag/"
                if old.startswith("Praxis")
                else "Grundakte/"
            )
            return prefix + name.removeprefix(old)
    return name


def aggregate(name):
    return Path(name).name.lower().endswith(("_gesamt.pdf", "-gesamt.pdf"))


def add_native_version(files, version, label):
    known = {digest(content) for content in files.values()}
    for name, content in version.items():
        if name == NOTICE_FILENAME or aggregate(name):
            continue
        # Gleiche Dokumente behalten ihre ursprüngliche fachliche Ablage in der führenden Fassung.
        if label != "Hauptfassung" and digest(content) in known:
            continue
        include(files, intake_path(name), content, "Weitere_Aktenstaende/" + label)


def add_print_version(files, version, label):
    known = {digest(content) for content in files.values()}
    for name, content in version.items():
        if name == NOTICE_FILENAME or aggregate(name):
            continue
        if not name.lower().endswith(".pdf"):
            raise ValueError("Nicht-PDF in der Lesefassung: " + name)
        if label != "Hauptfassung" and digest(content) in known:
            continue
        include(files, name.replace("/", "__"), content, label)


def original_manuscript(path, content):
    # Historische Aktenstücke einzelner Plugins existieren nur als Satzmanuskripte.
    lines = content.decode("utf-8-sig").strip().splitlines()
    title = lines[0].lstrip("# ").strip()
    blocks = [
        re.sub(r"^#{1,6}\s+", "", p).replace("**", "") for p in lines[1:] if p.strip()
    ]
    return render(
        {
            "typ": "notiz",
            "titel": title,
            "von": "Aktenausfertigung",
            "an": "Sachakte",
            "text": blocks,
        },
        str(path),
    )


def as_print(name, data):
    if name.lower().endswith(".pdf"):
        return data
    script = ROOT / "scripts/build-testakten-einzelpdf-zips.py"
    spec = importlib.util.spec_from_file_location("lesedokumente", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / Path(name).name
        path.write_bytes(data)
        printed = module.render_document_pdf(path, path.parent)
    if not printed:
        raise ValueError("Fehlende Druckfassung: " + name)
    return printed


def original_set(case, record, sources):
    native, printed = {}, {}
    native_versions = [v for v in ("praxis", "source", "vertieft") if v in record]
    prior_versions = {}
    for index, version in enumerate(native_versions):
        prior_versions[version] = members(sources.read(record[version]))
        add_native_version(
            native, prior_versions[version], "Hauptfassung" if index == 0 else version
        )
    for version in ("print", "vertieft_print"):
        if version in record:
            add_print_version(
                printed,
                members(sources.read(record[version])),
                "Hauptfassung" if version == "print" else "Vertiefung",
            )
    for ref in record.get("lesestuecke", []):
        printed[Path(ref["path"]).name] = sources.read(ref)
    for ref in record.get("originale", []):
        native[Path(ref["path"]).name] = sources.read(ref)
    for ref in record.get("manuskripte", []):
        path = Path(ref["path"])
        ext, word, pdf = original_manuscript(path, sources.read(ref))
        native[path.stem + "." + ext] = word
        printed[path.stem + ".pdf"] = pdf
    for bundle in record.get("auswahlen", []):
        subset = members(sources.read(bundle["quelle"]))
        for name in bundle["dateien"]:
            if name in native and native[name] == subset[name]:
                continue
            native[name] = subset[name]
            printed[str(Path(name).with_suffix(".pdf")).replace("/", "__")] = as_print(
                name, subset[name]
            )
    if not record.get("nur_original"):
        if "praxis" in prior_versions:
            base_hashes = {digest(b) for b in prior_versions.get("source", {}).values()}
            extra = {
                name: blob
                for name, blob in prior_versions["praxis"].items()
                if digest(blob) not in base_hashes
                and name != NOTICE_FILENAME
                and not aggregate(name)
            }
            slug = case.split("/")[-1]
            appendix = (
                ROOT
                / "docs/testakten-praxisnachtraege"
                / (slug + "-nachtrag-einzelpdfs.zip")
            )
            if appendix.exists():
                add_print_version(
                    printed, members(appendix.read_bytes()), "Praxisnachtrag"
                )
            elif extra:
                for name, blob in extra.items():
                    printed[str(Path(name).with_suffix(".pdf")).replace("/", "__")] = (
                        as_print(name, blob)
                    )
        if not printed and native:
            for name, blob in native.items():
                include(
                    printed,
                    str(Path(name).with_suffix(".pdf")).replace("/", "__"),
                    as_print(name, blob),
                    "Weitere",
                )
    return native, printed


def check_reference(case, name, native):
    local = localpath(case)
    if "!" in name:
        package, member = name.split("!", 1)
        candidate = (
            localpath(str(local.relative_to(ROOT) / package))
            if local.is_dir()
            else local
        )
        if candidate.is_file() and member.lstrip("/") in members(
            candidate.read_bytes()
        ):
            return
    elif (
        local.is_dir()
        and (local / name).resolve().is_relative_to(local)
        and (local / name).is_file()
    ):
        return
    name = safe_member(name.split("!")[-1].lstrip("/"))
    if not any(
        n == name
        or n.endswith(("/" + name, "/" + Path(name).name))
        or n == name.replace("/", "__")
        for n in native
    ):
        raise ValueError("Quellbeleg nicht gefunden: " + case + " / " + name)


def build(case, record, redaktion, sources):
    native, printed = original_set(case, record, sources)
    return build_from_documents(case, record, redaktion, native, printed)


def build_from_documents(case, record, redaktion, native, printed):
    if not native:
        raise ValueError("Leerer Ausgangsbestand: " + case)
    for reference in redaktion["bezug"]:
        check_reference(case, reference, native)
    # In bislang flachen Akten kommen nur positiv bezeichnete frühe Belege zur Eingangspost.
    if not any(n.startswith("Grundakte/") for n in native):
        for name in record.get("eingang", []):
            native["Grundakte/" + name] = native.pop(name)
    if redaktion.get("fortschreibungen"):
        ergaenze(native, printed, redaktion["fortschreibungen"])
    added_native, added_print = {}, {}
    docs = redaktion["unterlagen"]
    if len(docs) < 2 or len({d["typ"] for d in docs}) < 2 or not redaktion["bezug"]:
        raise ValueError("Unvollständige Eigenredaktion: " + case)
    for stem, ext, original, pdf in poststuecke(case, docs):
        name = "Grundakte/00_Posteingang/" + stem + "." + ext
        if name in native:
            raise ValueError("Namenskollision: " + name)
        added_native[name] = original
        added_print["Grundakte__00_Posteingang__" + stem + ".pdf"] = pdf
    fachpost = [
        f"  {number}. {doc['von']} an {doc['an']} – {doc['titel']}"
        for number, doc in enumerate(docs, 1)
    ]
    erste = [name for name in native if name.startswith("Grundakte/")][:4]
    beschreibung = [
        "",
        "Am Anfang der Akte",
        "==================",
        "",
        "In Grundakte/00_Posteingang finden Sie diese Unterlagen:",
        *fachpost,
    ]
    if erste:
        beschreibung += [
            "",
            "Weitere bereits vorliegende Belege (Auswahl):",
            *["  " + n for n in erste],
        ]
    beschreibung += [
        "",
        "Für die Erstbearbeitung den Ordner Grundakte öffnen. Der übrige Bestand ist für die Weiterarbeit zugänglich.",
        "",
    ]
    notice = NOTICE_BYTES + "\n".join(beschreibung).encode("utf-8")
    native = {NOTICE_FILENAME: notice, **added_native, **native}
    if record.get("nur_original"):
        return archive(native), None, None, len(native) - 1, len(added_native)
    printed = {**added_print, **{n.replace("/", "__"): b for n, b in printed.items()}}
    merged = PdfWriter()
    pages = 0
    for name, data in printed.items():
        reader = PdfReader(io.BytesIO(data), strict=False)
        if not reader.pages:
            raise ValueError("Leere PDF: " + case + " / " + name)
        pages += len(reader.pages)
        merged.append(reader, outline_item=Path(name).stem, import_outline=False)
    combined = io.BytesIO()
    merged.add_metadata(
        {"/Title": "Gesamtakte – " + record.get("id", case.split("/")[-1])}
    )
    merged.write(combined)
    if len(merged.pages) != pages:
        raise ValueError("Fehlende Seiten: " + case)
    merged.close()
    return (
        archive(native),
        archive({NOTICE_FILENAME: NOTICE_BYTES, **printed}),
        combined.getvalue(),
        len(native) - 1,
        len(added_native),
    )
