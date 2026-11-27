"""Findet die Fallablagen des Repositories und prüft ihre lokal verfügbaren Belege."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from email import policy
from email.parser import BytesHeaderParser
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
UFERWERK = "arbeitsrecht-kuendigungsschutzklagewerkstatt/testakte"
FLORISTIK = "scripts/data/pluginakten-praxis-2026-11-19/arbeitszeugnispruefer/Grundakte/Floristik"
GVB = "weitere-unterlagen/sektorenvergabe-gvb-berlin"
KEINE_EINZELAKTEN = {"megaprompts", "formatvorlagen-paradebeispiele"}
WORD = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def archivfolge(path):
    name = path.name.lower()
    return ("pdf" in name or name.startswith("druckakte-"), "nachtrag" in name, len(name), path.as_posix())


def fallquellen(root: Path = ROOT) -> dict[str, dict]:
    """Ordnet jeder selbstständig bearbeitbaren Fallablage ihre lokalen Quellen zu.

    Alle Pfade sind relativ zu root. Das erste Archiv ist bevorzugt die native
    Fassung. Eine Sammelseite oder ein gemeinsamer Downloadordner ist keine Akte.
    Ein Sachverhalt kann in mehreren fachlich getrennten Bearbeitungen vorkommen.
    """
    root = Path(root)
    basis = root / "scripts/data/grundakten-lebenswelt"
    katalog = {}
    for name in ("basis-lokal.json", "basis-zentral.json"):
        file = basis / name
        if file.is_file():
            entries = json.loads(file.read_text(encoding="utf-8"))
            if name == "basis-zentral.json":
                entries = {f"testakten/{k}": v for k, v in entries.items()}
            katalog.update(entries)
    for parent in (root / "testakten").glob("*"):
        if parent.name not in KEINE_EINZELAKTEN and (parent / "README.md").is_file():
            katalog.setdefault(parent.relative_to(root).as_posix(), {})

    archive = sorted(root.glob("**/*.zip"), key=archivfolge)
    bezug = defaultdict(list)
    weitere_ausgaben = defaultdict(list)
    for bundle in archive:
        # Native Falldownloads außerhalb der zentralen Ablage, daneben Druck-
        # und Anlagenpakete derselben Akte. Vorlagensammlungen sind keine Fälle.
        if bundle.is_relative_to(root / "docs/downloads"):
            stem = bundle.stem
            if stem.startswith(("lebensakte-", "druckakte-")):
                weitere_ausgaben[stem.split("-", 1)[1]].append(bundle)
            elif stem.endswith("-mit-nachtrag"):
                weitere_ausgaben[stem.removesuffix("-mit-nachtrag")].append(bundle)
        if "downloads" not in bundle.parts or not bundle.stem.startswith("testakte-"):
            continue
        slug = bundle.stem.removeprefix("testakte-")
        slug = re.sub(r"-(einzel-?pdfs|prozessunterlagen|anlagen-k1-k14|originaldateien)$", "", slug)
        bezug[slug].append(bundle)
        parent = bundle.parent.parent
        if (parent / "README.md").is_file() and parent.parent.name in (
            "testakten", "Interstate AG", "Patentanmelder"
        ):
            key = parent.relative_to(root).as_posix()
            prefix = {"Interstate AG": "interstate-", "Patentanmelder": "patentanmelder-"}
            katalog.setdefault(key, {"id": prefix.get(parent.parent.name, "") + slug})
    marketplace = root / ".claude-plugin/marketplace.json"
    if marketplace.is_file():
        plugins = json.loads(marketplace.read_text(encoding="utf-8"))["plugins"]
        for plugin in plugins:
            suite = root / plugin.get("source", plugin["name"]) / "testakten"
            for page in suite.glob("*/README.md"):
                folder = page.parent
                if folder.name not in KEINE_EINZELAKTEN and any(
                    p.is_file() and p.suffix.lower() in {".docx", ".eml", ".pdf", ".xlsx"}
                    for p in folder.rglob("*")
                ):
                    katalog.setdefault(folder.relative_to(root).as_posix(), {"id": folder.name})
    if (root / GVB / "README.md").is_file():
        katalog[GVB] = {"id": "sektorenvergabe-gvb-berlin"}

    faelle = {}
    for key, record in sorted(katalog.items()):
        path = root / key
        ident = record.get("id", path.name)
        folder = path if path.is_dir() else None
        readme = path / "README.md"
        bundles = []
        extras = []
        if folder:
            bundles.extend(folder.glob("*.zip"))
            bundles.extend((folder / "downloads").glob("*.zip"))
        else:
            bundles.extend(bezug.get(path.stem.removeprefix("testakte-"), []))
            readme = path.parent.parent / "TESTAKTEN.md"
        if key.startswith("testakten/"):
            bundles.extend(bezug[ident])
            bundles.extend((root / "docs/testakten-praxisnachtraege").glob(ident + "-nachtrag*.zip"))
            if ident.startswith("insolvenzreife-"):
                nachlieferungen = root / "docs/workshops/insolvenzreife-nachlieferungen/downloads"
                bundles.extend(nachlieferungen.glob(ident.removeprefix("insolvenzreife-") + "-mit-nachlieferung.zip"))
        if key == UFERWERK:
            readme = path / "uferwerk-berufung/README.md"
            folder = None
            bundles = bezug[ident]
        bundles.extend(weitere_ausgaben[ident])
        if record.get("nur_original") and path.name == "tomasius-solo":
            bundles.extend((root / "docs/testakten-praxisnachtraege").glob("tomasius-solo-nachtrag.zip"))
        if key == FLORISTIK:
            readme = root / "arbeitszeugnispruefer/testakte/arbeitszeugnis-analyse-bluehendes-leben/README.md"
            extras.append(path.parent.parent / "Nachreichungen/Floristik")
        if "personalakten-fuer-zeugniserstellung" in path.parts:
            readme = path.parent / "README.md"
            extras.append(root / "arbeitszeugnispruefer/testakte/arbeitszeugnis-analyse-bluehendes-leben" / path.name)
        for field in ("source", "print"):
            ref = record.get(field, {}).get("path")
            if ref and ref.endswith(".zip"):
                bundles.append(root / ref)
        use = "standard"
        if record.get("nur_original"):
            use = "nur-original"
        if key == UFERWERK:
            use = "nur-pdf"
        faelle[key] = {
            "id": ident,
            "seite": readme.relative_to(root).as_posix(),
            "ordner": folder.relative_to(root).as_posix() if folder else None,
            "weitere_ordner": [p.relative_to(root).as_posix() for p in extras],
            "archive": [p.relative_to(root).as_posix() for p in sorted(set(bundles), key=archivfolge)],
            "format": use,
        }
    return faelle


def zaehlung(root: Path = ROOT) -> dict[str, int]:
    faelle = fallquellen(root)
    zentral = sum(key.startswith("testakten/") for key in faelle)
    return {"central_testakten": zentral, "weitere_testakten": len(faelle) - zentral, "testakten": len(faelle)}


def farbwert(element):
    attribute = {
        "color": "val", "shd": "fill", "top": "color", "bottom": "color",
        "left": "color", "right": "color", "start": "color", "end": "color",
        "insideH": "color", "insideV": "color",
    }
    art = element.tag.removeprefix(WORD)
    if art not in attribute:
        return False
    value = element.get(WORD + attribute[art], "")
    if re.fullmatch(r"[0-9a-fA-F]{6}", value):
        rgb = [int(value[i:i + 2], 16) for i in (0, 2, 4)]
        return max(rgb) - min(rgb) >= 24
    return False


def wordmerkmale(data):
    with ZipFile(BytesIO(data)) as doc:
        body = ET.fromstring(doc.read("word/document.xml")).find(WORD + "body")
        if body is None:
            raise ValueError("Word-Datei ohne Dokumentkörper")
        headers = [
            ET.fromstring(doc.read(member)) for member in doc.namelist()
            if re.fullmatch(r"word/header\d+\.xml", member)
        ]
        # Im Fließtext gesetzte Köpfe sind häufig. Ein Farbwert kann auch zu
        # einer Überschrift gehören. Deshalb kein automatisches Briefkopfurteil.
        head = headers + list(body)[:4]
        return {
            "word_mit_text": any((e.text or "").strip() for e in body.iter(WORD + "t")),
            "word_mit_kopfzeile": any(
                any((e.text or "").strip() for e in node.iter(WORD + "t"))
                or node.find(".//" + WORD + "drawing") is not None for node in headers
            ),
            "word_mit_farbwert_im_kopfbereich": any(farbwert(e) for node in head for e in node.iter()),
            "word_mit_grafik_im_kopfbereich": any(
                node.find(".//" + WORD + "drawing") is not None or node.find(".//" + WORD + "pict") is not None
                for node in head
            ),
        }


def belege(root, fall, fehler):
    """Liest nur Dokumente; ZIP-Pfade werden niemals auf die Platte entpackt."""
    suffixe = {".docx", ".pdf", ".eml", ".doc", ".rtf", ".odt", ".xlsx", ".csv", ".ods", ".jpg", ".jpeg", ".png", ".msg", ".txt", ".md"}
    for folder in [fall["ordner"], *fall["weitere_ordner"]]:
        if not folder:
            continue
        for file in sorted((root / folder).rglob("*")):
            if file.suffix.lower() in suffixe and file.is_file():
                yield str(file.relative_to(root)), file.read_bytes()
    for bundle in fall["archive"]:
        try:
            with ZipFile(root / bundle) as archive:
                for member in archive.infolist():
                    if not member.is_dir() and Path(member.filename).suffix.lower() in suffixe:
                        yield f"{bundle}!{member.filename}", archive.read(member)
        except (BadZipFile, OSError, RuntimeError) as exc:
            fehler.append(f"{bundle}: {exc}")


def pruefe_quellen(root=ROOT, *, nur=None):
    root = Path(root)
    quellen = fallquellen(root)
    ids = Counter(v["id"] for v in quellen.values())
    fehler = [f"Doppelte Fall-ID: {i}" for i, n in ids.items() if n > 1]
    faelle = {}
    for key, fall in quellen.items():
        if nur and fall["id"] not in nur:
            continue
        if not (root / fall["seite"]).is_file():
            fehler.append("Fehlender Akteneinstieg: " + fall["seite"])
        for ordner in [fall["ordner"], *fall["weitere_ordner"]]:
            if ordner and not (root / ordner).is_dir():
                fehler.append("Fehlender Aktenordner: " + ordner)
        merkmale = Counter()
        formate = Counter()
        gelesen = set()
        absender = set()
        for name, data in belege(root, fall, fehler):
            ext = Path(name).suffix.lower()
            # Derselbe Beleg in Ordner, Originalpaket und Druckpaket zählt nur
            # einmal pro Fall. Eine Word-Datei und ihre PDF-Fassung zählen separat.
            checksum = hashlib.sha256(data).digest()
            if (checksum, ext) in gelesen:
                continue
            gelesen.add((checksum, ext))
            formate[ext.removeprefix(".")] += 1
            try:
                if ext == ".docx":
                    merkmale.update(k for k, vorhanden in wordmerkmale(data).items() if vorhanden)
                    if re.search(r"(blanko|formatvorlag|arbeitsvorlag|[/_]vorlagen[/_])", name, re.I):
                        merkmale["word_im_vorlagenbestand"] += 1
                elif ext == ".pdf":
                    if b"%PDF-" not in data[:1024] or b"%%EOF" not in data[-2048:]:
                        raise ValueError("PDF-Signatur oder Dateiende fehlt")
                    if re.search(r"gesamt[-_]?pdf|[_-]gesamt\.pdf$", name, re.I):
                        merkmale["pdf_mit_sammelbezeichnung"] += 1
                elif ext == ".eml":
                    mail = BytesHeaderParser(policy=policy.default).parsebytes(data)
                    if all(mail.get(k) for k in ("From", "To", "Subject")):
                        merkmale["mail_mit_absender_empfaenger_betreff"] += 1
                        # Ein Funktionspostfach kann mehrere Personen vertreten.
                        absender.update(a.addr_spec.casefold() for a in mail["From"].addresses if a.addr_spec)
            except (BadZipFile, ET.ParseError, KeyError, ValueError, IndexError, AttributeError) as exc:
                fehler.append(f"{name}: {exc}")
        if not formate:
            fehler.append("Keine lokalen Aktenunterlagen: " + key)
        merkmale["mail_absenderadressen"] = len(absender)
        faelle[key] = {"id": fall["id"], "format": fall["format"], "dateien": dict(sorted(formate.items())), "merkmale": dict(sorted(merkmale.items()))}
    if nur:
        fehler.extend("Unbekannte Fall-ID: " + i for i in sorted(nur - ids.keys()))
    return faelle, fehler


def pruefe_fundstellen(root, faelle, quellen):
    """Löst jeden Quellenbezug auf und prüft seine Zuordnung zur Fallablage."""
    root = Path(root)
    redaktion = {}
    anzahl = 0
    for fall in faelle:
        key = fall["fallpfad"]
        quelle = quellen[key]
        ordner = [Path(s) for s in [quelle["ordner"], *quelle["weitere_ordner"]] if s]
        if not fall["fundstellen"]:
            raise ValueError(f"Schriftstücke ohne Quellenbezug: {key}")
        for adresse in fall["fundstellen"]:
            datei, marke, zeiger = adresse.partition("#/")
            if marke:
                abschnitte = [s.replace("~1", "/").replace("~0", "~") for s in zeiger.split("/")]
                if (Path(datei).parent != Path("scripts/data/grundakten-lebenswelt")
                        or len(abschnitte) != 3 or abschnitte[1] != "unterlagen"
                        or abschnitte[0] not in {key, key.removeprefix("testakten/")}
                        or not abschnitte[2].isdecimal()):
                    raise ValueError(f"Fremder oder unvollständiger Redaktionsbeleg: {adresse}")
                if datei not in redaktion:
                    redaktion[datei] = json.loads((root / datei).read_text(encoding="utf-8"))
                record = redaktion[datei][abschnitte[0]]["unterlagen"][int(abschnitte[2])]
                if not record.get("titel") or not record.get("text"):
                    raise ValueError(f"Leerer Redaktionsbeleg: {adresse}")
            else:
                name, *mitglieder = datei.split("!")
                path = Path(name)
                if (path.is_absolute() or ".." in path.parts
                        or not (name in quelle["archive"] or any(path.is_relative_to(p) for p in ordner))):
                    raise ValueError(f"Fundstelle gehört nicht zur Akte {key}: {adresse}")
                daten = (root / path).read_bytes()
                for mitglied in mitglieder:
                    member = Path(mitglied)
                    if member.is_absolute() or ".." in member.parts:
                        raise ValueError(f"Unzulässiges Archivmitglied: {adresse}")
                    with ZipFile(BytesIO(daten)) as archive:
                        daten = archive.read(mitglied)
                if not daten:
                    raise ValueError(f"Leerer Originalbeleg: {adresse}")
            anzahl += 1
    return anzahl


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fall", action="append", help="Auswertung auf diese Fall-ID beschränken (wiederholbar)")
    parser.add_argument("--json", type=Path, help="Detailbericht je Akte als JSON schreiben")
    args = parser.parse_args()
    faelle, fehler = pruefe_quellen(nur=set(args.fall or []))
    counts = Counter()
    for fall in faelle.values():
        for ext in ("docx", "pdf", "eml"):
            if fall["dateien"].get(ext):
                counts[f"mit_{ext}"] += 1
        for k, n in fall["merkmale"].items():
            if n:
                counts[k] += 1
    print(json.dumps({"akten": len(faelle), "akten_mit_merkmal": counts, "fehler": len(fehler)}, ensure_ascii=False, indent=2))
    if args.json:
        args.json.write_text(json.dumps({"akten": faelle, "fehler": fehler}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if fehler:
        print("\n".join(fehler))
    return int(bool(fehler))


if __name__ == "__main__":
    raise SystemExit(main())
