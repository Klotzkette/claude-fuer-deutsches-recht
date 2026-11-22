"""Geprüfte Hauptskill-Fortschreibung bei unveränderten historischen Nachweisen.

Historische Hashes werden gegen die archivierte Vorfassung geprüft. Die neue
Fassung, ihre konkrete Redaktion und ihre lokalen Quellenkarten sind separat
gebunden. Dieser Nachweis behauptet weder eine Vollprüfung sämtlicher Quellen
noch einen Live-Modelltest und gilt ausschließlich für benannte Hauptskills.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from io import BytesIO
from pathlib import Path
from zipfile import BadZipFile, ZipFile

REGISTRY = "quality/hauptskills-2026-11-18/revisionen.json"
ARCHIVE = "quality/hauptskills-2026-11-18/bestand/"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inside(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("Hauptskill-Nachweis: ungültiger Pfad")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or (root / path).is_symlink():
        raise ValueError("Hauptskill-Nachweis: unzulässiger Pfad")
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("Hauptskill-Nachweis: Pfadausbruch")
    return target


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Hauptskill-Nachweis: doppeltes Feld {key}")
        result[key] = value
    return result


def load(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def index(root):
    path = root / REGISTRY
    if not path.is_file():
        return {}
    record = load(path)
    if record.get("schema_version") != 1 or record.get("method") != "main_workflow_revision":
        raise ValueError("Hauptskill-Nachweis: falsche Version oder Prüfmethode")
    result = {}
    for row in record.get("files", []):
        relative = row.get("path")
        if relative in result:
            raise ValueError("Hauptskill-Nachweis: doppelte Datei")
        inside(root, relative)
        result[relative] = row
    if not result:
        raise ValueError("Hauptskill-Nachweis: leere Fortschreibung")
    return result


def before_notariat_marketplace_count(root, path, current, *, plugin=None):
    """Rekonstruiert die zwei generierten Zähler vor Aufnahme des allgemeinen Notariats."""
    if path.name != "README.md" or b"<!-- BEGIN direkt-loslegen (autogen) -->" not in current:
        return current
    catalog = load(root / ".claude-plugin/marketplace.json")["plugins"]
    additions = {"allgemeines-notariat", "aktenanleger", "umwandlungssteuerrecht"}
    present = {row["name"] for row in catalog} & additions
    # Nur die zwei tatsächlich dokumentierten Erweiterungsstände sind umkehrbar.
    count = 315 if present == additions else 313
    sentence = f"Dieses Plugin gehört zum Marketplace mit {count} Plugins.".encode()
    if sentence not in current:
        return current
    begin = b"<!-- BEGIN direkt-loslegen (autogen) -->\n"
    end = b"\n<!-- END direkt-loslegen (autogen) -->"
    if current.count(begin) != 1 or current.count(end) != 1:
        return current
    prefix, _, rest = current.partition(begin)
    block, delimiter, suffix = rest.partition(end)
    start = b"\n" + sentence + " Für die Installation nimm das Einzel-ZIP.".encode()
    notice = b"\n> Marketplace-Hinweis: " + sentence + b" Das Sammelpaket "
    if not delimiter or block.count(start) != 1 or block.count(notice) != 1:
        return current

    if "allgemeines-notariat" not in present:
        return current
    relative = path.relative_to(root).as_posix()
    if not any((not plugin or item["name"] == plugin)
               and item["name"] not in additions
               and relative == (Path(item["source"]) / "README.md").as_posix()
               for item in catalog):
        return current
    for anchor in (start, notice):
        block = block.replace(anchor, anchor.replace(str(count).encode(), b"312"), 1)
    return prefix + begin + block + end + suffix


def before_case_index_addition(root, path, current, addition):
    """Entfernt nur den belegten Falltabelleneintrag und setzt dessen Zähler zurück."""
    from release_routing import case_asset_url

    slug = addition["slug"]
    count = addition["previous_count"]
    # Der Neuralis-Nachtrag aktualisiert auch die vier ausgeschriebenen
    # Zähler der Anleitung. Die rekonstruierte Fassung muss anschließend
    # unverändert zum bereits registrierten Hash des Tabellen-Nachtrags passen.
    if "summary_sha256" in addition and digest(current) == addition["summary_sha256"]:
        if slug != "neuralis-medtech-erlangen-gestaltungsakte" or count != 12:
            raise ValueError("Unbekannte Fortschreibung der Aktenzahlen")
        for updated, previous in (
            ("13 zugeordneten Fallakten", "zwölf zugeordneten Fallakten"),
            ("Die 13 Fallakten", "Die zwölf Fallakten"),
            ("13 practice cases", "Twelve practice cases"),
            ("13 gesonderte Fallakten", "zwölf gesonderte Fallakten"),
        ):
            if current.count(updated.encode()) != 1:
                raise ValueError("Aktenzahl im Überblick weicht vom geprüften Nachtrag ab")
            current = current.replace(updated.encode(), previous.encode(), 1)
    if (not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)
            or type(count) is not int or count < 2 or digest(current) != addition["after_sha256"]):
        raise ValueError("Unbelegte Erweiterung des Testaktenindexes")
    case = inside(root, "testakten/" + slug)
    title = (case / "README.md").read_text(encoding="utf-8").splitlines()[0]
    if title != "# " + addition["title"]:
        raise ValueError("Titel der registrierten Testakte stimmt nicht")
    base = Path(os.path.relpath(case, path.parent)).as_posix()
    cells = [f"[{title[2:]}]({base}/README.md)",
             f"[Gesamt-PDF]({base}/gesamt-pdf/{slug}_gesamt.pdf)"]
    for suffix in ("", "-einzelpdfs"):
        name = f"testakte-{slug}{suffix}.zip"
        cells.append(f"[`{name}`]({case_asset_url(slug, suffix, root=root)})")
    line = ("| " + " | ".join(cells) + " |\n").encode()
    def counter(n):
        return f"[{n} zugeordnete Akten](#zugeordnete-testakten)".encode()
    if current.count(line) != 1 or current.count(counter(count + 1)) != 1:
        raise ValueError("Fallzeile oder Aktenzähler weichen vom geprüften Index ab")
    return current.replace(line, b"", 1).replace(counter(count + 1), counter(count), 1)


def metadata_previous_bytes(root, path, *, plugin=None, expected_hash=None):
    """Nur exakte Downloadlink-/Manifestversionspflege, keine Fachtext-Ausnahme."""
    relative = path.relative_to(root).as_posix()
    registry = root / REGISTRY
    if not registry.exists():
        return None
    matches = [r for r in load(registry).get("integration_files", []) if r.get("path") == relative]
    if not matches:
        return None
    if len(matches) != 1:
        raise ValueError("Doppelte Metadatenfortschreibung")
    row = matches[0]
    if row.get("method") != "release_metadata_only" or (plugin and row.get("plugin") != plugin):
        raise ValueError("Unzulässige Metadatenfortschreibung")
    entry = next((p for p in load(root / ".claude-plugin/marketplace.json")["plugins"] if p["name"] == row["plugin"]), None)
    if entry is None:
        raise ValueError("Metadatenplugin fehlt")
    source = inside(root, entry["source"])
    if row.get("archive") != ARCHIVE + relative + ".txt":
        raise ValueError("Falscher Metadatenarchivpfad")
    old = inside(root, row["archive"]).read_bytes()
    current = path.read_bytes()
    if path == source / "README.md":
        current = before_notariat_marketplace_count(root, path, current, plugin=row["plugin"])
    addition = row.get("case_index_addition")
    if addition is not None:
        if path != source / "README.md":
            raise ValueError("Aktenindex außerhalb des Plugin-README")
        current = before_case_index_addition(root, path, current, addition)
    last_reviewed = current
    followup = row.get("publication_followup")
    if followup is not None:
        archive = "quality/paketnavigation-2026-11-19/bestand/" + relative + ".txt"
        if followup.get("previous_archive") != archive or digest(current) != followup.get("after_sha256"):
            raise ValueError("Unbelegte Fortschreibung der Paketmetadaten")
        last_reviewed = inside(root, archive).read_bytes()
    if digest(old) != row.get("before_sha256") or digest(last_reviewed) != row.get("after_sha256"):
        raise ValueError("Metadatenfortschreibung seit Prüfung verändert")
    if path == source / "README.md":
        from release_routing import scoped_asset_url
        pattern = re.compile(r"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/(?:latest/download|download/[^/\s)]+)/([a-z0-9.-]+\.zip)")
        names = {entry["name"] + suffix for suffix in (".zip", "-portable.zip")}
        expected = pattern.sub(lambda m: (scoped_asset_url(m[1], root=root) or m[0]) if m[1] in names else m[0], old.decode())
        if expected.encode() != current:
            raise ValueError("README-Fortschreibung verändert mehr als eigene Paketlinks")
    elif path in {source / p for p in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "plugin.json")}:
        before = json.loads(old, object_pairs_hook=unique_object)
        after = json.loads(current, object_pairs_hook=unique_object)
        before["version"] = entry["version"]
        if before != after or after.get("name") != entry["name"]:
            raise ValueError("Manifest-Fortschreibung verändert mehr als die Paketversion")
    else:
        raise ValueError("Keine zulässige Release-Metadatendatei")
    if addition is not None and digest(current) == expected_hash:
        return current
    if expected_hash is not None and digest(last_reviewed) == expected_hash:
        return last_reviewed
    return old


def previous_bytes(root, path, *, plugin=None):
    """Validierte Vorfassung oder None; kein allgemeines Hash-Override."""
    root, path = Path(root).resolve(), Path(path).resolve()
    relative = path.relative_to(root).as_posix()
    row = index(root).get(relative)
    if row is None:
        metadata = metadata_previous_bytes(root, path, plugin=plugin)
        if metadata is not None:
            return metadata
        from package_link_revisions import previous_bytes as package_previous_bytes
        return package_previous_bytes(root, path, plugin=plugin)
    name = row.get("plugin")
    if plugin is not None and name != plugin:
        raise ValueError(f"{relative}: Hauptskill-Nachweis gehört zu anderem Plugin")
    sources = {p["name"]: p["source"] for p in load(root / ".claude-plugin/marketplace.json")["plugins"]}
    profiles = load(root / "scripts/data/werkstatt-visualisierung-profile.json")["plugins"]
    try:
        expected = inside(root, sources[name]) / "skills" / profiles[name]["entry_skills"][0] / "SKILL.md"
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError(f"{relative}: Hauptskill ist nicht registriert") from exc
    if path != expected.resolve():
        raise ValueError(f"{relative}: Fortschreibung darf nur den registrierten Hauptskill betreffen")
    archive_name = ARCHIVE + relative + ".txt"
    if row.get("archive") != archive_name:
        raise ValueError(f"{relative}: falscher Archivpfad")
    old = inside(root, archive_name).read_bytes()
    current = path.read_bytes()
    last_reviewed = before_fachaufnahme(root, path, current, plugin=name)
    followup = row.get("publication_followup")
    if followup is not None:
        archive = "quality/paketnavigation-2026-11-19/bestand/" + relative + ".txt"
        if followup.get("previous_archive") != archive or digest(current) != followup.get("after_sha256"):
            raise ValueError("Unbelegte Fortschreibung der Paketmetadaten")
        last_reviewed = inside(root, archive).read_bytes()
    if digest(old) != row.get("before_sha256") or digest(last_reviewed) != row.get("after_sha256"):
        raise ValueError(f"{relative}: Hauptskill-Vorfassung oder Neufassung seit Prüfung verändert")
    if old == current:
        raise ValueError(f"{relative}: unveränderte Datei als Fortschreibung deklariert")
    review_path = row.get("review_path", "")
    if not review_path.startswith("quality/hauptskills-2026-11-18/") or not review_path.endswith(("-review.json", "-reviews.json", "-pruefungen.json")):
        raise ValueError(f"{relative}: unzulässiger Einzelprüfungsbeleg")
    raw = inside(root, review_path).read_bytes()
    if digest(raw) != row.get("review_sha256"):
        raise ValueError(f"{relative}: Einzelprüfungsbeleg verändert")
    reviews = json.loads(raw, object_pairs_hook=unique_object)
    matches = [r for r in reviews if r.get("path") == relative and r.get("plugin") == name]
    if len(matches) != 1:
        raise ValueError(f"{relative}: eindeutige Einzelprüfung fehlt")
    review = matches[0]
    if any(review.get(key) != row.get(key) for key in ("before_sha256", "after_sha256")):
        raise ValueError(f"{relative}: Einzelprüfung erfasst nicht die Fortschreibung")
    if (not isinstance(review.get("changes"), list) or not review["changes"]
            or any(not isinstance(s, str) or not s.strip() for s in review["changes"])):
        raise ValueError(f"{relative}: konkrete redaktionelle Änderungen fehlen")
    scenario = review.get("scenario", {})
    if any(not isinstance(scenario.get(k), str) or not scenario[k].strip()
           for k in ("input", "expected_result", "new_information")):
        raise ValueError(f"{relative}: fachlicher Fortsetzungsfall fehlt")
    if not review.get("source_scope") or not review.get("review_method"):
        raise ValueError(f"{relative}: Prüfverfahren oder Quellengrenze fehlt")
    references = row.get("references", {})
    if not references and review.get("inline_source_cards") is not True:
        raise ValueError(f"{relative}: lokale oder ausdrücklich integrierte Quellenkarte fehlt")
    if references and (review.get("reference") not in references
                       or references[review["reference"]] != review.get("reference_sha256")):
        raise ValueError(f"{relative}: Quellenkarte nicht in der Einzelprüfung gebunden")
    source = inside(root, sources[name])
    for ref, expected_hash in references.items():
        refpath = inside(root, ref)
        if not refpath.is_relative_to(source / "references") or refpath.suffix != ".md":
            raise ValueError(f"{relative}: Quellenkarte liegt außerhalb des Plugins")
        if digest(refpath.read_bytes()) != expected_hash:
            raise ValueError(f"{relative}: lokale Arbeits- und Quellenkarte verändert")
    return old


def before_fachaufnahme(root, path, current, *, plugin=None):
    """Liest die einzeln belegte Vorfassung eines redaktionell geänderten Fachtexts."""
    relative = path.relative_to(root)
    allowed = {"geldwaeschebeauftragter", "geldwaeschepraevention-aml-kyc"}
    if len(relative.parts) < 2 or relative.parts[0] not in allowed or path.suffix != ".md":
        return current
    base = "quality/fachaufnahme-2026-11-21/"
    registry = root / base / "fachtexte.json"
    if not registry.is_file():
        return current
    row = load(registry).get(relative.as_posix())
    if row is None:
        return current
    if plugin and relative.parts[0] != plugin:
        raise ValueError("Falsches Plugin der belegten Fachtextfortschreibung")
    old = inside(root, base + "bestand/" + relative.as_posix() + ".txt").read_bytes()
    if digest(current) != row["nachher"] or digest(old) != row["vorher"] or old == current:
        raise ValueError("Fachtext oder Vorfassung verändert: " + str(relative))
    return old


PRUEFER_PROOF = Path("quality/pruefer-fortschreibung-2026-11-21")
PRUEFER_MANIFEST_SHA256 = "c7372d50ab619d49c2a98070b3090bfd9a7f66c895ab9f3f001587bd4d4dd4f4"


def pruefer_release_path(relative):
    parts = relative.parts
    return (len(parts) >= 3 and parts[0] in {"arbeitszeugnispruefer", "bautraegervertrag-pruefer"}
            and (len(parts) == 3 and parts[1] == "references" and relative.suffix == ".md"
                 or len(parts) == 4 and parts[1] == "skills" and parts[3] in {"FACHINHALT.md", "SKILL.md"}))


def pruefer_release_manifest(root):
    record = (root / PRUEFER_PROOF / "nachweis.json").read_bytes()
    if digest(record) != PRUEFER_MANIFEST_SHA256:
        raise ValueError("Nachweis der Prüferfortschreibung verändert")
    return json.loads(record, object_pairs_hook=unique_object)


def pruefer_release_archive(root, proof):
    archive = (root / PRUEFER_PROOF / "vorfassungen.zip").read_bytes()
    if digest(archive) != proof["archive_sha256"]:
        raise ValueError("Archiv der Prüferfortschreibung verändert")
    return ZipFile(BytesIO(archive))


def pruefer_predecessor(files, name, row, current):
    if digest(current) != row["release_sha256"]:
        raise ValueError(f"{name}: Fachtext weicht vom veröffentlichten Prüferpaket ab")
    try:
        previous = files.read(name)
    except (BadZipFile, KeyError) as exc:
        raise ValueError(f"{name}: archivierte Vorfassung fehlt oder ist beschädigt") from exc
    if digest(previous) != row["previous_sha256"] or previous == current:
        raise ValueError(f"{name}: Vorfassung stimmt nicht mit historischem Quellhash überein")
    return previous


def validate_pruefer_release(root):
    """Prüft die vollständige Veröffentlichung, auch einen Rückbau auf alte, gültige Bytes."""
    if (not (root / PRUEFER_PROOF).exists()
            and not (root / "scripts/data/rechtsprechung-pruefer-release.json").exists()):
        return  # Kleiner Testbestand oder Stand vor der Prüferveröffentlichung.
    proof = pruefer_release_manifest(root)
    entries = proof["files"]
    with pruefer_release_archive(root, proof) as files:
        if sorted(files.namelist()) != sorted(entries):
            raise ValueError("Belegte und archivierte Prüferdateien unterscheiden sich")
        for name, row in entries.items():
            if not pruefer_release_path(Path(name)):
                raise ValueError(f"{name}: unzulässiger Fachtext im Prüferarchiv")
            current = inside(root, name).read_bytes()
            pruefer_predecessor(files, name, row, current)


def before_pruefer_release(root, path, current, expected, *, plugin=None):
    """Belegt die Vorfassung eines in der Konsolidierung erfassten Fachtextes."""
    relative = path.relative_to(root)
    if not pruefer_release_path(relative) or not (root / PRUEFER_PROOF / "nachweis.json").is_file():
        return current
    proof = pruefer_release_manifest(root)
    name = relative.as_posix()
    row = proof["files"].get(name)
    if row is None or row["previous_sha256"] != expected:
        return current
    if plugin is not None and plugin != relative.parts[0]:
        raise ValueError(f"{name}: Prüferfortschreibung gehört zu anderem Plugin")
    with pruefer_release_archive(root, proof) as files:
        return pruefer_predecessor(files, name, row, current)


def historical_bytes(root, path, expected, *, plugin=None):
    """Ein Hash passt entweder unmittelbar oder zu einer vollständig belegten Vorfassung."""
    current = Path(path).read_bytes()
    if digest(current) == expected:
        return current
    from case_navigation_revision import CASES, previous_case_readme
    root, path = Path(root).resolve(), Path(path).resolve()
    earlier = before_pruefer_release(root, path, current, expected, plugin=plugin)
    if earlier != current:
        return earlier
    earlier = before_fachaufnahme(root, path, current, plugin=plugin)
    if earlier != current and digest(earlier) == expected:
        return earlier
    prior = before_notariat_marketplace_count(root, path, current, plugin=plugin)
    if prior != current and digest(prior) == expected:
        return prior
    if path.name == "README.md" and "testakte" in path.parts:
        relative = path.relative_to(root).as_posix()
        if relative in CASES:
            if plugin and plugin != relative.split("/", 1)[0]:
                raise ValueError("Aktenseite gehört zu einem anderen Plugin")
            prior = previous_case_readme(root, relative, current)
            return prior if digest(prior) == expected else current
    old = previous_bytes(root, path, plugin=plugin)
    if old is not None and digest(old) == expected:
        return old
    if old is not None and path.name in {"README.md", "plugin.json"}:
        intermediate = metadata_previous_bytes(root, path, plugin=plugin, expected_hash=expected)
        if intermediate is not None and digest(intermediate) == expected:
            return intermediate
    return current


def validate_all(root):
    root = Path(root).resolve()
    rows = index(root)
    for relative, row in rows.items():
        previous_bytes(root, inside(root, relative), plugin=row.get("plugin"))
    if (root / REGISTRY).is_file():
        for row in load(root / REGISTRY).get("integration_files", []):
            if row.get("path") in rows:
                raise ValueError("Metadaten und Hauptskill doppelt deklariert")
            metadata_previous_bytes(root, inside(root, row["path"]), plugin=row.get("plugin"))
    from package_link_revisions import validate_all as validate_package_links
    validate_package_links(root)
    validate_pruefer_release(root)
    return len(rows)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(f"{validate_all(args.root)} Hauptskill-Fortschreibungen mit erhaltenen Vorfassungen geprüft.")
