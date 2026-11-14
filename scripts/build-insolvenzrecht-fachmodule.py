#!/usr/bin/env python3
"""Bündelt kuratierte Fachmodule reproduzierbar im eigenständigen Hauptplugin.

Die vier kompatiblen Einzelpakete bleiben redaktionelle Quellen. Die Registry
ordnet jeden Quellskill ausdrücklich einer Fachroute zu; neue Skills werden
nicht stillschweigend importiert. Keine zusätzlichen SKILL.md oder Manifeste.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
REGISTRY = Path("scripts/data/insolvenzrecht-fachmodule.json")
PLUGIN = Path("insolvenzrecht")
GITHUB = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/"
RUNTIME_DIRS = ("skills", "references", "assets", "commands")
LINK = re.compile(r"(?P<open>!?\[[^\]\n]*\]\()(?P<href>[^)\n]+)(?P<close>\))")
RESOURCE_PATH = re.compile(r"(?<![\w/.-])(?:assets|references|skills)/[\w./-]+\.(?:md|csv|html|json|py|pdf|docx|xlsx)(?![\w./-])")


def digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def relative(target: Path, parent: Path) -> str:
    return os.path.relpath(target, parent).replace(os.sep, "/")


def repo_url(path: Path) -> str:
    return GITHUB + quote(path.as_posix(), safe="/")


def body_and_title(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        _, separator, body = text[4:].partition("\n---\n")
        if not separator:
            raise ValueError("Offene Frontmatter in Fachquelle")
        text = body.lstrip("\n")
    title = next((line[2:] for line in text.splitlines() if line.startswith("# ")), "Fachreferenz")
    return text, title


def source_files(root: Path, source: Path) -> list[Path]:
    result = []
    for folder in RUNTIME_DIRS:
        base = root / source / folder
        for path in sorted(base.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Keine Symlinks in Fachquellen: {path}")
            if path.is_file() and "__pycache__" not in path.parts:
                result.append(path.relative_to(root))
    return result


def generate(root: Path = ROOT) -> dict[Path, bytes]:
    """Liefert nur Dateien relativ zum Zielordner; verändert keine Quelle."""
    registry_raw = (root / REGISTRY).read_bytes()
    registry = json.loads(registry_raw)
    if registry.get("schema") != 1:
        raise ValueError("Unbekannte Fachmodul-Registry")
    base = Path(registry["destination"])
    if base != PLUGIN / "references/fachmodule":
        raise ValueError("Fachmodule dürfen nur in ihr eigenes Zielverzeichnis schreiben")
    main_route = Path(registry["main_route"])
    if not (root / main_route).is_file():
        raise ValueError("Gemeinsamer Hauptworkflow fehlt")
    groups = registry["groups"]
    mappings: dict[Path, dict] = {}
    outputs: dict[Path, bytes] = {}
    titles: dict[Path, str] = {}
    plan = Path(registry["plan_plugin"])

    def add(source: Path, target: Path | str, mode: str, reason: str, **extra) -> None:
        if source in mappings:
            raise ValueError(f"Doppelte Quellzuordnung: {source}")
        if not (root / source).is_file():
            raise ValueError(f"Quelle fehlt: {source}")
        mappings[source] = dict(source=source.as_posix(), source_sha256=digest((root / source).read_bytes()),
                                target=str(target), mode=mode, reason=reason, **extra)

    # Gemeinsame Quellen werden nur einmal mitgeführt. Eine vorhandene,
    # byteidentische Hauptplugin-Datei bleibt das kanonische lokale Ziel.
    for name in registry["shared_references"]:
        source = Path(name)
        existing = PLUGIN / source
        target = existing if (root / existing).is_file() and (root / existing).read_bytes() == (root / source).read_bytes() else base / "gemeinsam" / source.name
        add(source, target, "shared-reference", "Gemeinsame Quellen- und Arbeitsregel; keine erneute Aktenaufnahme.")

    for module, spec in registry["modules"].items():
        source = Path(spec["source"])
        actual = {p.parent.name for p in (root / source / "skills").glob("*/SKILL.md")}
        declared = set(spec["skills"])
        if actual != declared:
            raise ValueError(f"{source}: Registry-Lücke; neu={sorted(actual-declared)}, fehlt={sorted(declared-actual)}")
        for slug, rule in spec["skills"].items():
            if rule["group"] not in groups or rule["mode"] not in {"reference", "main-route", "separate-plan"} or not rule["reason"].strip():
                raise ValueError(f"Unvollständige Auswahlregel: {source}/{slug}")
        for file in source_files(root, source):
            rel = file.relative_to(source)
            mode = "reference"
            reason = "Paketlokale Fachquelle oder Arbeitsvorlage für das zugeordnete Modul."
            target = base / module / rel
            extra = {"module": module}
            if rel.parts[:3] == ("assets", "templates", "planwerkstatt"):
                canonical = plan / "assets/templates" / rel.name
                if not (root / canonical).is_file() or (root / canonical).read_bytes() != (root / file).read_bytes():
                    raise ValueError(f"Planvorlage ist nicht mehr identisch; fachlich zuordnen: {file}")
                add(file, repo_url(canonical), "separate-plan-template", "Byteidentische Vorlage verbleibt ausschließlich im eigenständigen Planplugin.",
                    canonical_source=canonical.as_posix(), canonical_sha256=digest((root / canonical).read_bytes()), module=module)
                continue
            if rel.parts[:2] == ("assets", "vorschau"):
                add(file, repo_url(file), "legacy-preview", "Vorschauseite der kompatiblen Einzelausgabe; kein benötigtes Arbeitsmaterial.", module=module)
                continue
            if rel.parts[0] == "skills":
                slug = rel.parts[1]
                rule = spec["skills"][slug]
                extra.update(group=rule["group"], selection_reason=rule["reason"])
                if rel.name == "SKILL.md":
                    target = base / module / "vertiefungen" / f"{slug}.md"
                    mode, reason = rule["mode"], rule["reason"]
                    _, title = body_and_title((root / file).read_text())
                    titles[file] = title
                    if mode == "main-route":
                        extra["material_target"] = target.as_posix()
                        target = main_route
                    elif mode == "separate-plan":
                        extra["material_target"] = target.as_posix()
                        target = repo_url(plan / "README.md")
                else:
                    target = base / module / "vertiefungen" / slug / Path(*rel.parts[2:])
            elif rel.parts[0] == "references":
                target = base / module / "quellen" / Path(*rel.parts[1:])
                common = Path("references") / rel.name
                if common in mappings and (root / common).read_bytes() == (root / file).read_bytes():
                    target = Path(mappings[common]["target"])
                    mode = "shared-reference"
                    reason = "Byteidentische gemeinsame Quellenregel wird einmal paketlokal vorgehalten."
            elif rel.parts[0] == "assets":
                target = base / module / "vorlagen" / Path(*rel.parts[1:])
                mode = "asset"
                reason = "Vollständige originale Arbeitsvorlage einschließlich konkreter Felder und Berechnungsdaten."
            elif rel.parts[0] == "commands":
                target = main_route
                mode = "compatibility-command"
                reason = "Bisheriger Chat-Kurzbefehl ist im Hauptpaket durch den gemeinsamen Einstieg ersetzt."
            add(file, target, mode, reason, **extra)

    def resolved_link(href: str, source: Path, destination: Path, plain: bool = False) -> str:
        original_href = href
        href = registry.get("link_aliases", {}).get(source.as_posix(), {}).get(href, href)
        if href != original_href:
            change = {"from": original_href, "to": href, "reason": "Explizit registrierte Korrektur eines bestehenden Dateinamens."}
            changes = mappings[source].setdefault("link_corrections", [])
            if change not in changes:
                changes.append(change)
        url = urlsplit(href)
        if url.scheme or href.startswith(("#", "//")):
            return href
        raw = unquote(url.path)
        if not raw:
            return href
        candidate = (root / source.parent / raw).resolve()
        # Ältere Quellen nennen paketwurzel-relative Vorlagen auch in Fließtext.
        if plain or not candidate.exists():
            for spec in registry["modules"].values():
                source_root = Path(spec["source"])
                if source.is_relative_to(source_root):
                    possible = (root / source_root / raw).resolve()
                    if possible.exists():
                        candidate = possible
                    break
            if not candidate.exists() and (root / raw).exists():
                candidate = (root / raw).resolve()
        if not candidate.is_relative_to(root.resolve()):
            raise ValueError(f"Quelllink verlässt Repository: {source}: {href}")
        candidate = candidate.relative_to(root.resolve())
        mapping = mappings.get(candidate)
        if mapping:
            target = mapping["target"]
            # Ursprüngliche Abschnittsanker eines alten Routers gehören nicht
            # automatisch zur zusammengeführten Hauptsteuerung.
            fragment = "" if mapping["mode"] in {"main-route", "compatibility-command", "separate-plan"} else ("#" + url.fragment if url.fragment else "")
            return (target if target.startswith("https://") else relative(Path(target), destination.parent)) + fragment
        if not (root / candidate).exists():
            raise ValueError(f"Nicht auflösbare Quellreferenz: {source}: {href}")
        if candidate.is_relative_to(PLUGIN):
            return relative(candidate, destination.parent) + ("#" + url.fragment if url.fragment else "")
        # Testakten, Einzelausgaben und eigenständige Prompts bleiben bewusst
        # Downloads im Repository, keine vorausgesetzte Geschwisterinstallation.
        return repo_url(candidate) + ("#" + url.fragment if url.fragment else "")

    def rewrite(text: str, source: Path, destination: Path) -> str:
        # Führe auch bisher nur als Text genannte Vorlagen auf tatsächliche lokale
        # Dateien. Markdown-Linkziele nicht nochmals als Ressourcenpfad behandeln.
        parts = []
        last = 0
        for match in LINK.finditer(text):
            chunk = text[last:match.start()]
            parts.append(RESOURCE_PATH.sub(lambda m: resolved_link(m.group(0), source, destination, plain=True), chunk))
            href = match.group("href")
            parts.append(match.group("open") + resolved_link(href, source, destination) + match.group("close"))
            last = match.end()
        parts.append(RESOURCE_PATH.sub(lambda m: resolved_link(m.group(0), source, destination, plain=True), text[last:]))
        return "".join(parts)

    for source, row in mappings.items():
        target_str = row.get("material_target", row["target"])
        if target_str.startswith("https://") or row["mode"] == "compatibility-command":
            continue
        target = Path(target_str)
        if not target.is_relative_to(base):
            row["target_sha256"] = digest((root / target).read_bytes())
            continue
        raw = (root / source).read_bytes()
        if source.suffix == ".md":
            text = raw.decode()
            if source.name == "SKILL.md":
                text, title = body_and_title(text)
                notice = (
                    "Ergänzende Fachreferenz des Hauptplugins. Den bereits geklärten Auftrag, die Rolle, Aktenfundstellen und Fristen übernehmen. "
                    "Keinen zweiten Intake starten und keine zusätzliche Installation voraussetzen. "
                )
                if row["mode"] == "main-route":
                    notice += "Die Auftragssteuerung erfolgt ausschließlich über den gemeinsamen Hauptworkflow; hier bleiben nur dessen fachliche Kontext- und Übergaberegeln nachschlagbar. "
                elif row["mode"] == "separate-plan":
                    notice += "Nur die Vorbereitung und Prüfung der Übergabe gehört zu diesem Modul. Die vollständige Planerstellung bleibt bei der eigenständigen Insolvenzplan- und StaRUG-Planwerkstatt. "
                notice += "Weitere Referenzen nur für eine konkrete offene Fachfrage laden."
                text = text.replace("\n", "\n\n> " + notice + "\n", 1)
            raw = rewrite(text, source, target).encode()
        if target in outputs and outputs[target] != raw:
            raise ValueError(f"Widersprüchliche Zielbelegung: {target}")
        outputs[target] = raw
        row["material_sha256" if "material_target" in row else "target_sha256"] = digest(raw)

    def link_to(row: dict, parent: Path, context: bool = False) -> str:
        target = row.get("material_target", row["target"]) if context else row["target"]
        return target if target.startswith("https://") else relative(Path(target), parent)

    for module, spec in registry["modules"].items():
        index = base / module / "INDEX.md"
        lines = [f"# {spec['title']}", "", spec["when"], "", "## 1. Auftrag gezielt fortsetzen", "",
                 "Die Rolle und die geklärten Angaben aus dem Hauptworkflow übernehmen. In der folgenden Auswahl genau die passende Produktgruppe öffnen, dort zunächst eine Fachreferenz. Weitere Texte nur für eine benannte Beweis-, Rechts- oder Rechenfrage lesen.", "",
                 "| Auftrag / konkrete Entscheidung | Unterlagen und Ergebnis | Auswahl |", "| --- | --- | --- |"]
        for group, group_spec in groups.items():
            members = [(slug, rule) for slug, rule in spec["skills"].items() if rule["group"] == group]
            if not members or group == "hauptroute":
                continue
            group_file = base / module / f"{group}.md"
            lines.append(f"| {group_spec['when']} | {group_spec['product']} | [{group_spec['title']}]({group}.md) |")
            detail = [f"# {group_spec['title']}", "", group_spec["when"], "", f"**Arbeitsprodukt:** {group_spec['product']}", "",
                      "Die Auswahl ist keine Liste zusätzlich auszuführender Prüfungen. Nur den vom Auftrag betroffenen Fachtext öffnen; bei Überschneidungen eine führende Referenz wählen und gesicherte Ergebnisse übernehmen.", "",
                      "| Fachfrage | Referenz |", "| --- | --- |"]
            if group == "plan-uebergabe":
                detail[4:4] = [f"Die [eigenständige Planwerkstatt]({repo_url(plan / 'README.md')}) bleibt für die vollständige Planarbeit zuständig. Folgende lokale Texte dienen nur der fachlichen Übergabe; die 22 identischen Planvorlagen werden hier nicht nochmals verteilt.", ""]
            for slug, rule in members:
                source = Path(spec["source"]) / "skills" / slug / "SKILL.md"
                row = mappings[source]
                detail.append(f"| {titles[source]} | [Fachkontext]({link_to(row, group_file.parent, context=True)}) |")
            outputs[group_file] = ("\n".join(detail) + "\n").encode()
        lines.extend(["", "## 2. Originale Arbeitsvorlagen", "", "Die folgenden Vorlagen sind vollständig im Hauptpaket vorhanden. Nur die für das bestellte Produkt benötigte Vorlage verwenden; Originalbelege und Platzhalter auseinanderhalten.", ""])
        assets = [(source, row) for source, row in mappings.items() if row.get("module") == module and row["mode"] == "asset"]
        lines.extend(f"- [{source.name}]({link_to(row, index.parent)})" for source, row in assets)
        if not assets:
            lines.append("Die ausformulierten Arbeitsprodukte und ihre Felder stehen in den ausgewählten Fachreferenzen.")
        lines.extend(["", "## 3. Gemeinsame Auftragssteuerung und besondere Kontextregeln", "",
                      f"Der [Hauptworkflow]({relative(main_route, index.parent)}) führt Intake, Rolle, Rückfragen, Freigaben und Fortsetzung einmalig. Die bisherigen Steuerungstexte sind keine weiteren Einstiegspunkte. Sie werden nur geöffnet, wenn eine besondere Übergaberegel oder Produktkennung daraus benötigt wird.", ""])
        for slug, rule in spec["skills"].items():
            if rule["mode"] == "main-route":
                source = Path(spec["source"]) / "skills" / slug / "SKILL.md"
                lines.append(f"- [{titles[source]}: fachlicher Kontext]({link_to(mappings[source], index.parent, context=True)})")
        outputs[index] = ("\n".join(lines) + "\n").encode()

    index = ["# Insolvenzrecht: integrierte Fachmodule", "",
             "Das Hauptplugin bearbeitet anwaltliche Insolvenzmandate, Insolvenzverwaltung, laufende Sachbearbeitung und Berichte mit lokal enthaltenen Fachtexten und Vorlagen. Für diese Aufgaben ist keine Installation der früheren Einzelpakete erforderlich.", "",
             "## 1. Rolle und bestelltes Arbeitsprodukt entscheiden", "",
             "Die Akte zuerst lesen und den bereits geklärten Stand fortschreiben. Genau ein führendes Modul öffnen. Ein zweites Modul nur für einen konkreten Übergabepunkt hinzunehmen; keine neue Aktenaufnahme beginnen.", "",
             "| Ausgangslage | Modul |", "| --- | --- |"]
    for module, spec in registry["modules"].items():
        index.append(f"| {spec['when']} | [{spec['title']}]({module}/INDEX.md) |")
    index.extend(["", "## 2. Eigenständige Spezialwerkzeuge", "",
                  "Eine eigene Gläubigerforderung anmelden, den Eintritt der Zahlungsunfähigkeit oder Überschuldung vollständig rekonstruieren oder einen Insolvenzplan beziehungsweise StaRUG-Plan erstellen: Diese drei Aufträge bleiben bei den dafür separat angebotenen Spezialwerkzeugen. Den geklärten Aktenstand, Zahlen, Belege und offenen Fragen dorthin übergeben. Eine gewünschte externe Anwendung muss tatsächlich verfügbar sein; andernfalls das Übergabepaket und den erreichbaren Download bereitstellen.", "",
                  "## 3. Herkunft und Aktualität", "",
                  "Die Fachmodule werden aus ausdrücklich zugeordneten Bestandsquellen reproduzierbar gebaut. Die Auswahl befindet sich in `scripts/data/insolvenzrecht-fachmodule.json`; [SOURCE_MAP.json](SOURCE_MAP.json) weist jede Quelldatei mit Hash, Ziel, Auswahlgrund und Übernahmeart aus. Die Kopie ist keine erneute materielle Rechtsprüfung. Tragende Normen und Rechtsprechung vor Anwendung anhand aktueller amtlicher Quellen prüfen. Die redaktionelle Änderung erfolgt an der ausgewiesenen Quelle, anschließend wird das Hauptpaket neu erzeugt.", ""])
    outputs[base / "INDEX.md"] = "\n".join(index).encode()
    inventory = {path.relative_to(PLUGIN).as_posix(): digest(data) for path, data in sorted(outputs.items())}
    source_map = dict(schema=1, registry=REGISTRY.as_posix(), registry_sha256=digest(registry_raw),
                      main_route=main_route.relative_to(PLUGIN).as_posix(),
                      main_route_sha256=digest((root / main_route).read_bytes()),
                      source_skills=sum(len(s["skills"]) for s in registry["modules"].values()),
                      disposition_counts=dict(sorted(Counter(row["mode"] for row in mappings.values()).items())),
                      files=[dict(row) for _, row in sorted(mappings.items())], generated_files=inventory)
    outputs[base / "SOURCE_MAP.json"] = json_bytes(source_map)
    return {path.relative_to(base): data for path, data in outputs.items()}


def check_tree(directory: Path, expected: dict[Path, bytes]) -> list[str]:
    actual = {p.relative_to(directory) for p in directory.rglob("*") if p.is_file()} if directory.exists() else set()
    errors = [f"fehlt: {p}" for p in sorted(set(expected) - actual)]
    errors += [f"unerwartet: {p}" for p in sorted(actual - set(expected))]
    errors += [f"veraltet: {p}" for p in sorted(actual & set(expected)) if (directory / p).read_bytes() != expected[p]]
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Quell- und Paketdrift prüfen, nichts schreiben")
    parser.add_argument("--output", type=Path, help="Alternativer Fachmodule-Zielordner, z.B. in einem leeren temporären Verzeichnis")
    args = parser.parse_args()
    expected = generate()
    registry = json.loads((ROOT / REGISTRY).read_text())
    target = args.output or ROOT / registry["destination"]
    if args.check:
        errors = check_tree(target, expected)
        if errors:
            raise SystemExit("Fachmodule weichen ab:\n" + "\n".join(errors[:30]))
    else:
        # Niemals fremde Dateien oder ältere Artefakte stillschweigend löschen.
        actual = {p.relative_to(target) for p in target.rglob("*") if p.is_file()} if target.exists() else set()
        stale = actual - set(expected)
        if stale:
            raise SystemExit("Nicht mehr zugeordnete Dateien gezielt prüfen: " + ", ".join(map(str, sorted(stale))))
        for path, data in expected.items():
            dest = target / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
    count = sum(len(module["skills"]) for module in registry["modules"].values())
    print(f"Insolvenzrecht-Fachmodule: {len(expected)} Dateien {'geprüft' if args.check else 'erzeugt'}, {count} Quellskills, keine zusätzlichen Runtime-Skills.")


if __name__ == "__main__":
    main()
