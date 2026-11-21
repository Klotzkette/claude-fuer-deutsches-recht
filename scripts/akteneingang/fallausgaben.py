"""Originalakte, Lesefassung und Einzel-PDFs aus redaktionellen Fallquellen."""
import io
from collections import Counter
from datetime import date
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, NOTICE_MARKDOWN
from .ausgabe import archive
from .korrespondenz import poststuecke
from .quellen import digest


def case_material(spec):
    docs = spec["unterlagen"]
    counts = Counter(d["ordner"] for d in docs)
    if (
        set(counts) != {"Grundakte", "Nachreichungen", "Vorlagen"}
        or counts["Grundakte"] < 8
        or counts["Nachreichungen"] < 2
    ):
        raise ValueError("Unvollständige Aktenstufen: " + spec["id"])
    for i, doc in enumerate(docs, 1):
        date.fromisoformat(doc["datum"])
        if doc["ordner"] == "Vorlagen" and doc["typ"] not in {"notiz", "tabelle"}:
            raise ValueError("Arbeitsvorlage muss bearbeitbar sein")
        for ref in ("anlage_nr", "antwort_auf"):
            if (
                ref in doc
                and doc["ordner"] == "Grundakte"
                and docs[doc[ref] - 1]["ordner"] != "Grundakte"
            ):
                raise ValueError("Vorgriff auf spätere Belege: " + doc["titel"])
        if not doc["text"] or not all(
            isinstance(p, str) and p.strip() for p in doc["text"]
        ):
            raise ValueError("Unvollständiges Aktenstück: " + str(i))
    native, prints = {}, {}
    combined = PdfWriter()
    pages = 0
    for doc, (stem, ext, blob, printed) in zip(
        docs,
        poststuecke(spec["id"], [{**r, "_fachfassung": True} for r in docs]),
        strict=True,
    ):
        name = doc["ordner"] + "/" + stem
        native[name + "." + ext] = blob
        prints[name.replace("/", "__") + ".pdf"] = printed
        reader = PdfReader(io.BytesIO(printed))
        combined.append(reader, outline_item=doc["titel"], import_outline=False)
        pages += len(reader.pages)
    out = io.BytesIO()
    combined.add_metadata({"/Title": spec["titel"]})
    combined.write(out)
    combined.close()
    start = (
        NOTICE_BYTES
        + (
            "\n"
            + spec["titel"]
            + "\n\n"
            + spec["einstieg"]
            + "\n\n"
            + spec["auftrag"]
            + "\n\nÖffnen Sie zuerst den Ordner Grundakte. In der zweiten Runde kommen die Nachreichungen hinzu. Im Ordner Vorlagen liegen bearbeitbare Arbeitsblätter.\n"
        ).encode()
    )
    return (
        archive({NOTICE_FILENAME: start, **native}),
        archive({NOTICE_FILENAME: NOTICE_BYTES, **prints}),
        out.getvalue(),
        pages,
    )


def case_files(spec, layout, write, previous, *, source, prefix, overview):
    slug = spec["id"]
    folder = layout / slug
    n = prefix + slug
    paths = (
        "downloads/" + n + ".zip",
        "downloads/" + n + "-einzelpdfs.zip",
        "gesamt-pdf/" + n + "_gesamt.pdf",
    )
    if write:
        raw, single, combined, pages = case_material(spec)
        assets = dict(zip(paths, (raw, single, combined), strict=True))
    else:
        assets = {rel: (folder / rel).read_bytes() for rel in paths}
        pages = len(PdfReader(io.BytesIO(assets[paths[2]])).pages)
    evidence = {
        "quelle_sha256": digest(source.read_bytes()),
        "aktenstuecke": len(spec["unterlagen"]),
        "seiten": pages,
        "sha256": {rel: digest(b) for rel, b in assets.items()},
    }
    if not write and evidence != previous:
        raise ValueError("Aktenstand passt nicht zur ausgewiesenen Quelle: " + slug)
    rows = [
        f"# {spec['titel']}",
        "",
        spec["einstieg"],
        "",
        spec["auftrag"],
        "",
        "Öffnen Sie zuerst die Grundakte im Originalformat-ZIP. Die Nachreichungen und bearbeitbaren Vorlagen haben jeweils einen eigenen Ordner.",
        "",
        NOTICE_MARKDOWN,
        "",
        "| Originalunterlagen | Gesamtakte | Einzel-PDFs |",
        "| --- | --- | --- |",
        f"| [Arbeits-ZIP](downloads/{n}.zip) | [Gesamt-PDF](gesamt-pdf/{n}_gesamt.pdf) | [Einzel-PDF-ZIP](downloads/{n}-einzelpdfs.zip) |",
        "",
        f"[{overview}](../README.md)",
        "",
    ]
    files = {**assets, "README.md": "\n".join(rows).encode()}
    for rel, data in files.items():
        path = folder / rel
        if write:
            path.parent.mkdir(exist_ok=True, parents=True)
            path.write_bytes(data)
        elif not path.is_file() or digest(path.read_bytes()) != digest(data):
            raise ValueError("Abweichung zum abgelegten Aktenstand: " + str(path))
    return {Path(k).name: v for k, v in assets.items()}, evidence
