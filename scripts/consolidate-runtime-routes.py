#!/usr/bin/env python3
"""Verdichtet überbreite Skill-Routen ohne Verlust der Fachinhalte.

Die Skill-Metadaten jedes aktivierten Plugins stehen schon beim Sitzungsstart zur
Auswahl bereit. Dieses Skript entfernt deshalb nur nachweislich doppelte Routen
und klar abgegrenzte Serien. Die bisherigen Inhalte bleiben als bedarfsgeladene
Referenzen erhalten; ein enger Fachrouter entscheidet, welche davon benötigt wird.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
MAX_REFERENCE_BYTES = 38 * 1024
ALIAS_PREFIXES = ("spezial-", "dsv-", "gk-", "anw-", "rom-neu-")


@dataclass(frozen=True)
class SkillSource:
    slug: str
    title: str
    description: str
    body: str
    directory: Path


@dataclass(frozen=True)
class ReferenceGroup:
    key: str
    title: str
    trigger: str


def marketplace_plugin_dirs() -> list[Path]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    result: list[Path] = []
    for plugin in data.get("plugins", []):
        source = str(plugin.get("source") or f"./{plugin['name']}")
        directory = (REPO / source).resolve()
        if directory.is_dir() and (directory / "skills").is_dir():
            result.append(directory)
    return sorted(set(result))


def split_skill(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        raise ValueError("Skill ohne YAML-Frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("Skill mit offenem YAML-Frontmatter")
    frontmatter = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    description = description_match.group(1).strip() if description_match else ""
    if len(description) >= 2 and description[0] == description[-1] and description[0] in {'"', "'"}:
        description = description[1:-1]
    heading = next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), "")
    return description, heading, body


def load_source(skill_file: Path) -> SkillSource:
    description, heading, body = split_skill(skill_file.read_text(encoding="utf-8"))
    return SkillSource(
        slug=skill_file.parent.name,
        title=heading or skill_file.parent.name.replace("-", " ").title(),
        description=description,
        body=body.rstrip() + "\n",
        directory=skill_file.parent,
    )


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def demote_headings(text: str, levels: int = 1) -> str:
    def repl(match: re.Match[str]) -> str:
        marks = match.group(1)
        return "#" * min(6, len(marks) + levels) + " "

    return re.sub(r"^(#{1,5})\s+", repl, text, flags=re.MULTILINE)


def rewrite_relative_links(text: str, source_dir: Path, destination_dir: Path) -> str:
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def repl(match: re.Match[str]) -> str:
        label, href = match.groups()
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        href_path = href.split("#", 1)[0]
        anchor = "#" + href.split("#", 1)[1] if "#" in href else ""
        target = (source_dir / href_path).resolve()
        source_references = (source_dir / "references").resolve()
        if target == source_references or source_references in target.parents:
            return label
        relative = os.path.relpath(target, destination_dir).replace(os.sep, "/")
        if not relative.startswith("."):
            relative = "./" + relative
        return f"[{label}]({relative}{anchor})"

    return pattern.sub(repl, text)


def source_payload(source: SkillSource, destination_dir: Path | None = None) -> str:
    body = source.body
    if destination_dir is not None:
        body = rewrite_relative_links(body, source.directory, destination_dir)
    chunks = [
        f"## {source.title}",
        "",
        f"Auswahlsignal: {source.description}",
        "",
        demote_headings(body, 2).strip(),
    ]
    references = sorted((source.directory / "references").glob("*.md"))
    for reference in references:
        chunks.extend(
            [
                "",
                f"### Ergänzende Vertiefung aus {reference.stem.replace('-', ' ')}",
                "",
                demote_headings(reference.read_text(encoding="utf-8"), 3).strip(),
            ]
        )
    return "\n".join(chunks).rstrip() + "\n"


def append_reference_pointer(base_file: Path, source: SkillSource, reference_name: str) -> None:
    text = base_file.read_text(encoding="utf-8")
    target = f"./references/{reference_name}"
    if target in text:
        return
    heading = "## Vertiefung bei Bedarf"
    pointer = (
        f"- Bei `{source.slug}` beziehungsweise {source.title}: "
        f"[die zusätzliche Vertiefung laden]({target})."
    )
    if heading in text:
        insert_at = text.find("\n## ", text.find(heading) + len(heading))
        if insert_at == -1:
            text = text.rstrip() + "\n" + pointer + "\n"
        else:
            text = text[:insert_at].rstrip() + "\n" + pointer + "\n\n" + text[insert_at + 1 :]
    else:
        text = text.rstrip() + f"\n\n{heading}\n\n{pointer}\n"
    base_file.write_text(text, encoding="utf-8")


def consolidate_exact_aliases() -> dict[str, str]:
    aliases: dict[str, str] = {}
    for plugin_dir in marketplace_plugin_dirs():
        skills_dir = plugin_dir / "skills"
        names = {path.parent.name for path in skills_dir.glob("*/SKILL.md")}
        for alias in sorted(names):
            prefix = next((item for item in ALIAS_PREFIXES if alias.startswith(item)), None)
            if not prefix:
                continue
            base = alias[len(prefix) :]
            if base not in names:
                continue
            alias_dir = skills_dir / alias
            extra = [path for path in alias_dir.rglob("*") if path.is_file() and path.name != "SKILL.md"]
            if extra:
                raise ValueError(f"{alias_dir.relative_to(REPO)} enthält unerwartete Zusatzdateien")
            source = load_source(alias_dir / "SKILL.md")
            base_dir = skills_dir / base
            references = base_dir / "references"
            references.mkdir(exist_ok=True)
            reference_name = f"vertiefung-{alias}.md"
            (references / reference_name).write_text(
                source_payload(source, references), encoding="utf-8"
            )
            append_reference_pointer(base_dir / "SKILL.md", source, reference_name)
            shutil.rmtree(alias_dir)
            aliases[f"{plugin_dir.relative_to(REPO).as_posix()}:{alias}"] = base
    return aliases


def chunk_sources(sources: list[SkillSource], destination_dir: Path) -> list[list[SkillSource]]:
    chunks: list[list[SkillSource]] = []
    current: list[SkillSource] = []
    current_size = 0
    for source in sources:
        size = len(source_payload(source, destination_dir).encode("utf-8"))
        if current and current_size + size > MAX_REFERENCE_BYTES:
            chunks.append(current)
            current = []
            current_size = 0
        current.append(source)
        current_size += size
    if current:
        chunks.append(current)
    return chunks


def compact_topic(source: SkillSource) -> str:
    title = source.title.rstrip(" .")
    if source.slug.startswith("jurisdiktion-"):
        title = source.slug.removeprefix("jurisdiktion-").removesuffix("-competition-authority")
        title = title.replace("-", " ").title()
    elif source.slug.startswith("dba-") and source.slug in DBA_COUNTRY_SLUGS:
        title = source.slug.removeprefix("dba-").replace("-", " ").title()
    elif source.slug.startswith("lph-") and ":" in title:
        title = title.rsplit(":", 1)[1].strip()
    title = re.sub(r"\s+", " ", title)
    return title[:72].rstrip(" ,;:.-")


def concise_topics(sources: list[SkillSource], limit: int = 5) -> str:
    topics = [compact_topic(source) for source in sources[:limit]]
    text = ", ".join(topics)
    if len(sources) > limit:
        text += f" und {len(sources) - limit} weitere Module"
    return text[:260].rstrip(" ,;:.-")


def write_reference_chunks(
    router_dir: Path,
    family_title: str,
    grouped_sources: list[tuple[ReferenceGroup, list[SkillSource]]],
) -> list[tuple[str, str, str]]:
    references = router_dir / "references"
    references.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str]] = []
    for group, sources in grouped_sources:
        if not sources:
            continue
        source_chunks = chunk_sources(sorted(sources, key=lambda item: item.slug), references)
        for index, chunk in enumerate(source_chunks, start=1):
            suffix = f"-{index:02d}" if len(source_chunks) > 1 else ""
            filename = f"{group.key}{suffix}.md"
            lines = [
                f"# {family_title}: {group.title}",
                "",
                "Diese Datei wird nur geladen, wenn der konkrete Vorgang in diese Fallgruppe fällt.",
                "",
            ]
            for source in chunk:
                lines.extend([source_payload(source, references).rstrip(), ""])
            content = "\n".join(lines).rstrip() + "\n"
            if len(content.encode("utf-8")) > 96 * 1024:
                raise ValueError(f"{filename}: Referenzdatei überschreitet 96 KiB")
            (references / filename).write_text(content, encoding="utf-8")
            label = group.title + (f" {index}" if suffix else "")
            rows.append((label, filename, f"{group.trigger}; enthält {concise_topics(chunk)}"))
    return rows


def build_router(
    plugin_dir: Path,
    router_slug: str,
    title: str,
    description: str,
    sources: list[SkillSource],
    groups: list[ReferenceGroup],
    group_for: Callable[[SkillSource], str],
    direct_start: str,
    output: str,
    preserve_router_body: bool = False,
) -> None:
    skills_dir = plugin_dir / "skills"
    router_dir = skills_dir / router_slug
    original_router: SkillSource | None = None
    if (router_dir / "SKILL.md").is_file():
        if not preserve_router_body:
            raise ValueError(f"Router existiert bereits: {router_dir.relative_to(REPO)}")
        original_router = load_source(router_dir / "SKILL.md")
    router_dir.mkdir(parents=True, exist_ok=True)

    grouped: dict[str, list[SkillSource]] = {group.key: [] for group in groups}
    for source in sources:
        key = group_for(source)
        if key not in grouped:
            raise ValueError(f"{source.slug}: unbekannte Referenzgruppe {key}")
        grouped[key].append(source)
    if original_router:
        grouped[groups[0].key].insert(0, original_router)

    rows = write_reference_chunks(
        router_dir,
        title,
        [(group, grouped[group.key]) for group in groups],
    )
    lines = [
        "---",
        f"name: {router_slug}",
        f"description: {yaml_quote(description)}",
        "---",
        "",
        f"# {title}",
        "",
        "## 1. Direktstart",
        "",
        direct_start,
        "",
        "1. Vorhandene Unterlagen zuerst lesen und bereits erkennbare Angaben übernehmen.",
        "2. Sachthema, Zeitraum, Verfahrensstand und gewünschtes Arbeitsprodukt bestimmen.",
        "3. Genau eine passende Referenz aus der folgenden Tabelle laden; nur bei einer echten Schnittstelle eine zweite.",
        "4. Nach der Vertiefung unmittelbar das Arbeitsprodukt erstellen und nur entscheidungserhebliche Lücken nachfragen.",
        "",
        "## 2. Bedarfsgeladene Vertiefungen",
        "",
        "| Fallgruppe | Referenz | Nur laden bei |",
        "| --- | --- | --- |",
    ]
    for label, filename, trigger in rows:
        lines.append(f"| {label} | [{filename}](./references/{filename}) | {trigger} |")
    lines.extend(
        [
            "",
            "## 3. Arbeitsprodukt",
            "",
            output,
            "",
            "## 4. Geschwindigkeitsregel",
            "",
            "Nicht den gesamten Referenzbestand lesen. Sobald Norm, Beleg, Gegenposition und gewünschter Output tragfähig feststehen, schreiben; weitere Vertiefungen nur für eine konkret benannte Lücke öffnen.",
            "",
        ]
    )
    (router_dir / "SKILL.md").write_text("\n".join(lines), encoding="utf-8")

    for source in sources:
        if source.directory.resolve() == router_dir.resolve():
            continue
        shutil.rmtree(source.directory)


def hoai_group(source: SkillSource) -> str:
    slug = source.slug
    if any(
        needle in slug
        for needle in (
            "input-und-zielcheck",
            "grundleistung-besondere-leistung",
            "vertrag-und-beauftragungsumfang",
            "honorar-und-prozentwert",
            "bauherrnfreigabe",
            "oeffentlicher-auftraggeber",
            "verbraucher-privater-bauherr",
            "fachplaner-schnittstellen",
        )
    ):
        return "auftrag-und-schnittstellen"
    if any(
        needle in slug
        for needle in (
            "kostensteuerung",
            "terminsteuerung",
            "planfreigabe",
            "bim-und-datenraum",
            "dokumentation-und-belegakte",
            "kommunikation-baustelle-behoerde",
            "genehmigungen-und-auflagen",
            "foerdermittel-und-nachweis",
        )
    ):
        return "steuerung-und-nachweise"
    return "risiko-und-output"


HOAI_PHASES = {
    1: ("Grundlagenermittlung", "Bedarf, Aufgabenstellung, Ortsbesichtigung, Beratung und Entscheidungsgrundlage"),
    2: ("Vorplanung", "Planungsvarianten, Voruntersuchung, Kostenrahmen, Termine und Behördenabstimmung"),
    3: ("Entwurfsplanung", "durchgearbeiteter Entwurf, Kostenberechnung, Schnittstellen und Freigabe"),
    4: ("Genehmigungsplanung", "Genehmigungsunterlagen, Anträge, Nachforderungen, Auflagen und Bescheide"),
    5: ("Ausführungsplanung", "ausführungsreife Pläne, Detailkoordination, Versionierung und Planfreigabe"),
    6: ("Vorbereitung der Vergabe", "Leistungsbeschreibung, Mengen, Leistungsverzeichnis, Kostenanschlag und Vergabereife"),
    7: ("Mitwirkung bei der Vergabe", "Angebotsprüfung, Preisspiegel, Bietergespräch, Vergabevorschlag und Auftrag"),
    8: ("Objektüberwachung", "Bauüberwachung, Bautagebuch, Mängel, Nachträge, Rechnungen, Abnahme und Dokumentation"),
    9: ("Objektbetreuung", "Gewährleistungsfristen, Mängelverfolgung, Objektbegehung und Abschlussdokumentation"),
}


def consolidate_hoai() -> None:
    plugin = REPO / "hoai-leistungsphasen-praxis"
    for phase, (name, focus) in HOAI_PHASES.items():
        router_slug = f"lph-{phase:02d}-arbeitsrouter"
        sources = [
            load_source(path)
            for path in sorted((plugin / "skills").glob(f"lph-{phase:02d}-*/SKILL.md"))
            if path.parent.name != router_slug
        ]
        if not sources:
            continue
        build_router(
            plugin,
            router_slug,
            f"Leistungsphase {phase}: {name}",
            f"Für HOAI-Leistungsphase {phase} {name}: routet {focus}; lädt nur das einschlägige Fachmodul und liefert den nächsten prüffähigen Projektbaustein.",
            sources,
            [
                ReferenceGroup("auftrag-und-schnittstellen", "Auftrag und Schnittstellen", "Auftrag, Leistungsbild, Honorar, Bauherr oder Fachplaner"),
                ReferenceGroup("steuerung-und-nachweise", "Steuerung und Nachweise", "Kosten, Termine, Planung, Genehmigung, BIM, Kommunikation oder Förderung"),
                ReferenceGroup("risiko-und-output", "Risiko und Output", "Mangel, Nachtrag, Haftung, Abnahme, Rechnung, Streit, Qualität oder Bericht"),
            ],
            hoai_group,
        f"Arbeite ausschließlich in Leistungsphase {phase} ({name}), solange Unterlagen und Auftrag keine belastbare Schnittstelle zu einer anderen Phase zeigen. {focus[0].upper() + focus[1:]} bilden den Einstieg.",
            "Liefere je nach Auftrag einen Prüfvermerk, eine Freigabevorlage, ein Protokoll, eine Kosten- oder Terminentscheidung, einen Nachtrags- oder Mangelbaustein beziehungsweise ein phasengerechtes Abschlussblatt mit Belegen und offenem nächsten Schritt.",
        )


def alpha_group(source: SkillSource) -> str:
    stem = source.slug.split("-", 1)[1] if "-" in source.slug else source.slug
    first = stem[0].lower()
    for lo, hi, key in (
        ("a", "b", "a-b"),
        ("c", "f", "c-f"),
        ("g", "k", "g-k"),
        ("l", "m", "l-m"),
        ("n", "p", "n-p"),
        ("q", "s", "q-s"),
        ("t", "z", "t-z"),
    ):
        if lo <= first <= hi:
            return key
    return "t-z"


def consolidate_kartell_jurisdictions() -> None:
    plugin = REPO / "kartellrecht-marktabgrenzung-pruefung"
    sources = [load_source(path) for path in sorted((plugin / "skills").glob("jurisdiktion-*/SKILL.md"))]
    if not sources:
        return
    groups = [ReferenceGroup(key, key.upper(), f"Staat oder Jurisdiktion mit Anfangsbuchstaben {key.upper()}") for key in ("a-b", "c-f", "g-k", "l-m", "n-p", "q-s", "t-z")]
    build_router(
        plugin,
        "internationale-kartellrechts-jurisdiktionen",
        "Internationale Kartellrechtsjurisdiktionen",
        "Für internationale Fusionskontrolle, Kartellverfahren und Competition-Authority-Fragen: wählt Staat und Behörde, lädt nur die Länderreferenz und liefert Zuständigkeits-, Fristen- und Anmeldepfad.",
        sources,
        groups,
        alpha_group,
        "Bestimme zuerst betroffene Staaten, Umsatz- oder Transaktionsbezug, Verhalten, Vollzugszeitpunkt und gewünschten Behördenkontakt. Länderangaben sind Arbeitsanker; Schwellen, Behördenzuständigkeit und Formulare werden vor Verwendung aus Primärquellen aktualisiert.",
        "Liefere eine Jurisdiktionsmatrix mit Behörde, Rechtsgrundlage, Schwelle oder Anknüpfung, Frist, Vollzugsverbot, Formular, Sprache, lokalem Beratungsbedarf und offenem Quellencheck.",
    )


DATA_AUTHORITY_SLUGS = {
    "meldung-baylda",
    "meldung-bfdi",
    "meldung-bln-bdi",
    "meldung-hbdi",
    "meldung-hmbbfdi",
    "meldung-lda-brandenburg",
    "meldung-ldi-nrw",
    "meldung-lfd-niedersachsen",
    "meldung-lfd-sachsen-anhalt",
    "meldung-lfdi-bremen",
    "meldung-lfdi-bw",
    "meldung-lfdi-mv",
    "meldung-lfdi-rlp",
    "meldung-lfdi-saarland",
    "meldung-saechsdsb",
    "meldung-tlfdi",
    "meldung-uld-sh",
}


def consolidate_data_authorities() -> None:
    plugin = REPO / "datenschutzrecht"
    sources = [
        load_source(plugin / "skills" / slug / "SKILL.md")
        for slug in sorted(DATA_AUTHORITY_SLUGS)
        if (plugin / "skills" / slug / "SKILL.md").is_file()
    ]
    if not sources:
        return
    build_router(
        plugin,
        "meldung-deutsche-aufsichtsbehoerde",
        "Meldung an die zuständige deutsche Datenschutzaufsicht",
        "Für Datenpannenmeldungen an BfDI oder Landesaufsicht: bestimmt Zuständigkeit und Meldeweg, lädt nur das Behördenmodul und liefert fristgerechte Erst- oder Nachmeldung mit Nachweisakte.",
        sources,
        [ReferenceGroup("aufsichtsbehoerden", "Bund und Länder", "BfDI oder eine deutsche Landesdatenschutzaufsicht")],
        lambda _source: "aufsichtsbehoerden",
        "Sichere zuerst Entdeckungszeitpunkt, Verantwortlichen, Niederlassung, betroffene Verarbeitung, Risiko und bereits getroffene Maßnahmen. Danach wähle anhand Verantwortlichem, Hauptniederlassung und sektoraler Zuständigkeit genau die zuständige Behörde.",
        "Liefere Zuständigkeitsvermerk, 72-Stunden-Fristenblatt, Erst- oder Nachmeldung, Pflichtangabenmatrix, Versandnachweis und Liste noch offener Tatsachen; keine parallelen Mehrfachmeldungen ohne begründete Zuständigkeitsunsicherheit.",
    )


DBA_COUNTRY_SLUGS = {
    "dba-belgien",
    "dba-bulgarien",
    "dba-daenemark",
    "dba-estland",
    "dba-finnland",
    "dba-frankreich-1959",
    "dba-griechenland",
    "dba-grossbritannien-2010",
    "dba-irland",
    "dba-island",
    "dba-israel-2014",
    "dba-italien",
    "dba-kanada-2001",
    "dba-kroatien",
    "dba-lettland",
    "dba-litauen",
    "dba-luxemburg-2012",
    "dba-malta-2001",
    "dba-niederlande-2012",
    "dba-norwegen",
    "dba-oesterreich",
    "dba-polen",
    "dba-portugal",
    "dba-rumaenien",
    "dba-schweden",
    "dba-schweiz",
    "dba-serbien-montenegro",
    "dba-slowakei",
    "dba-slowenien",
    "dba-spanien-2011",
    "dba-tschechien",
    "dba-tuerkei-2011",
    "dba-ukraine",
    "dba-ungarn",
    "dba-usa-1989-protokoll-2006",
    "dba-zypern-2011",
}


def consolidate_dba_countries() -> None:
    plugin = REPO / "steuerrecht-anwalt-und-berater"
    sources = [
        load_source(plugin / "skills" / slug / "SKILL.md")
        for slug in sorted(DBA_COUNTRY_SLUGS)
        if (plugin / "skills" / slug / "SKILL.md").is_file()
    ]
    if not sources:
        return
    build_router(
        plugin,
        "dba-alle-abkommen-laendermatrix-2026",
        "DBA-Länderprüfung",
        "Für länderspezifische Doppelbesteuerungsabkommen: routet Staat, Zeitraum, Einkunftsart, Ansässigkeit, Betriebsstätte und Methodenartikel; lädt nur die Länderreferenz und liefert ein quellengeprüftes DBA-Memo.",
        sources,
        [ReferenceGroup(key, key.upper(), f"DBA-Staat mit Anfangsbuchstaben {key.upper()}") for key in ("a-b", "c-f", "g-k", "l-m", "n-p", "q-s", "t-z")],
        alpha_group,
        "Bestimme beide Staaten, Zeitraum, Person oder Rechtsträger, Einkunftsart, innerstaatliche Anknüpfung, Ansässigkeit und möglichen Quellenstaat. Prüfe danach Originalabkommen, Protokoll, Änderungsstand, MLI-Wirkung und Verwaltungsvereinbarungen aus Primärquellen.",
        "Liefere ein DBA-Routingblatt mit nationalem Besteuerungstatbestand, einschlägigen Abkommensartikeln, Zuweisung, Methode, Quellensteuer, Verfahrensweg, Belegen und gesondert markiertem Aktualitätscheck.",
        preserve_router_body=True,
    )


def tax_family_group(source: SkillSource) -> str:
    slug = source.slug
    if any(word in slug for word in ("grundlage", "aufbau", "aufnahme", "onboarding", "vertrag", "monatsabschluss")):
        return "grundlagen"
    if any(word in slug for word in ("meldung", "elster", "elstam", "sv-", "berufsgenossenschaft", "umlage", "mindestlohn", "mini", "midi", "aufzeichnung")):
        return "meldung"
    if any(word in slug for word in ("dienstwagen", "jobticket", "firmenrad", "sachbez", "veranstaltung", "ausflug", "bav", "altersversorgung", "direktversicherung", "vermoegenswirksam")):
        return "leistungen"
    return "sonderfall"


def consolidate_tax_family(prefix: str, router_slug: str, title: str, description: str, direct_start: str, output: str) -> None:
    plugin = REPO / "steuerrecht-anwalt-und-berater"
    sources = [load_source(path) for path in sorted((plugin / "skills").glob(f"{prefix}*/SKILL.md")) if path.parent.name != router_slug]
    if not sources:
        return
    if prefix == "lohn-":
        groups = [
            ReferenceGroup("grundlagen", "Mandat und Abrechnung", "Onboarding, Arbeitsvertrag, Abrechnung oder Monatsabschluss"),
            ReferenceGroup("meldung", "Meldungen und Sozialversicherung", "ELStAM, Lohnsteuer, Sozialversicherung, Mindestlohn oder Prüfung"),
            ReferenceGroup("leistungen", "Sachbezüge und Zusatzleistungen", "Dienstwagen, Mobilität, Betriebsveranstaltung, bAV oder Sachbezug"),
            ReferenceGroup("sonderfall", "Beschäftigungs- und Sonderfälle", "Krankheit, Elternzeit, Kurzarbeit, Praktikum, Überstunden, Abfindung oder Streit"),
        ]
        grouper = tax_family_group
    elif prefix == "bwa-":
        groups = [
            ReferenceGroup("bwa", "BWA, Kennzahlen und Mandantenbericht", "BWA-Aufbau, Kontenrahmen, Kennzahl, Vergleich, Cashflow oder Bericht")
        ]
        grouper = lambda _source: "bwa"
    else:
        groups = [
            ReferenceGroup("tatbestand", "Steuerbefreiung und Tatbestand", "Paragraf 3a EStG, Sanierungsbedürftigkeit, Sanierungsfähigkeit oder Sanierungsabsicht"),
            ReferenceGroup("folge", "Steuerfolgen und Verlustreihenfolge", "Paragraf 3c EStG, Gewerbesteuer, Verlustnutzung oder Zuständigkeit"),
            ReferenceGroup("gestaltung", "Verzicht, Rangrücktritt und Gestaltung", "Forderungsverzicht, Rangrücktritt, Debt-Equity-Swap, Bilanzierung oder Vermeidung"),
            ReferenceGroup("sonderfall", "Sonderfälle und Verfahrenslage", "Personengesellschaft, Betriebsstätte, Liquidation, BMF-Linie, Frühwarnung oder Mandantenhinweis"),
        ]

        def grouper(source: SkillSource) -> str:
            slug = source.slug
            if any(word in slug for word in ("3a-", "grundtatbestand", "unternehmens-vs-person")):
                return "tatbestand"
            if any(word in slug for word in ("3c-", "gewstg", "verlust", "zustaendigkeit", "koerperschaft")):
                return "folge"
            if any(word in slug for word in ("verzicht", "rangruecktritt", "stehengelass", "vermeid", "5-abs")):
                return "gestaltung"
            return "sonderfall"

    build_router(plugin, router_slug, title, description, sources, groups, grouper, direct_start, output)


def consolidate_tax_families() -> None:
    consolidate_tax_family(
        "lohn-",
        "lohnabrechnung-und-arbeitgeberpflichten",
        "Lohnabrechnung und Arbeitgeberpflichten",
        "Für Lohnsteuer, Entgeltabrechnung und Sozialversicherung: routet ELStAM, Meldungen, Sachbezüge, bAV, Minijob, Dienstwagen, DRV-Prüfung und Beschäftigungssonderfälle in genau das benötigte Fachmodul.",
        "Lies Abrechnungsmonat, Arbeitnehmerstammdaten, Vertrag, Lohnkonto, Meldestatus und konkrete Abweichung zuerst. Trenne Steuer, Sozialversicherung und Arbeitsrecht und sichere jede kalenderabhängige Grenze anhand des betroffenen Zeitraums.",
        "Liefere Abrechnungskorrektur, Melde- und Fristenplan, Berechnungsblatt, Mandantenhinweis oder Prüfungsakte mit Rechtsgrund, Zeitraum, Rechenweg, Beleg und nächstem Versand- oder Buchungsschritt.",
    )
    consolidate_tax_family(
        "bwa-",
        "bwa-analyse-und-mandantenbericht",
        "BWA-Analyse und Mandantenbericht",
        "Für BWA, DATEV-Auswertung und betriebswirtschaftliche Monatsanalyse: routet Kontenrahmen, Ergebnis, Cashflow, Kennzahlen, Soll-Ist- und Vorjahresvergleich und liefert prüfbaren Mandantenbericht.",
        "Lies BWA, Summen- und Saldenliste, Kontenrahmen, Zeitraum und Vergleichswerte. Trenne Buchungsstand, betriebswirtschaftliche Aussage und steuerliche Würdigung; kennzeichne fehlende Abschlussbuchungen und Sondereffekte.",
        "Liefere Zahlenbrücke, Kennzahlentabelle mit Quellenspalte, Abweichungsanalyse, Liquiditätshinweis und einen verständlichen Mandantenbericht ohne Scheingenauigkeit.",
    )
    consolidate_tax_family(
        "sanierungsgewinn-",
        "sanierungsgewinn-steuerpruefung",
        "Steuerprüfung des Sanierungsgewinns",
        "Für Forderungsverzicht und Sanierungsgewinn: routet Paragraf 3a und Paragraf 3c EStG, Paragraf 7b GewStG, Rangrücktritt, Verlustreihenfolge, Bilanzierung und Sonderfälle in die passende Vertiefung.",
        "Lies Verzichts-, Rangrücktritts- oder Umwandlungsdokument, Bilanzansatz, Sanierungskonzept, Verluststände, Steuerart und Verfahrensstand. Trenne Entstehung des Gewinns, Steuerbefreiung, korrespondierende Aufwandkürzung und gewerbesteuerliche Folge.",
        "Liefere Tatbestandsmatrix, Steuerarten- und Verlustreihenfolge, Buchungs- und Deklarationshinweis, Belegliste sowie einen belastbaren Entwurf für Mandant, Finanzamt oder Betriebsprüfung.",
    )


def beirat_group(source: SkillSource) -> str:
    slug = source.slug
    if any(word in slug for word in ("satzung", "abgrenzung", "kontroll", "beratungs", "entscheidungsbefug", "mitbestimmung", "register", "musterklaus")):
        return "grundlage"
    if any(word in slug for word in ("bestellung", "abberufung", "amtszeit", "geschaeftsordnung", "sitzung", "protokoll", "verguetung", "verschwiegen", "information")):
        return "gremium"
    if any(word in slug for word in ("zustimmung", "veto", "deadlock", "interessenkonflikt", "beschluss", "streit", "geschaeftsfuehrer")):
        return "konflikt"
    return "sonderlage"


def consolidate_beirat() -> None:
    plugin = REPO / "grosskanzlei-corporate-ma"
    router_slug = "beirat-gestaltung-und-governance"
    sources = [
        load_source(path)
        for path in sorted((plugin / "skills").glob("beirat-*/SKILL.md"))
        if path.parent.name != router_slug
    ]
    if not sources:
        return
    build_router(
        plugin,
        router_slug,
        "Beirat: Gestaltung und Governance",
        "Für GmbH-, Familien-, Startup- oder Investorenbeiräte: routet Satzung, Kompetenzen, Zustimmungskatalog, Bestellung, Sitzung, Haftung, Konflikte, Sanierung und Transaktion in die passende Vertiefung.",
        sources,
        [
            ReferenceGroup("grundlage", "Rechtsgrundlage und Kompetenz", "Satzung, Abgrenzung, Funktion, Kompetenz, Mitbestimmung oder Register"),
            ReferenceGroup("gremium", "Besetzung und Gremienarbeit", "Bestellung, Amtszeit, Geschäftsordnung, Sitzung, Protokoll, Information oder Vergütung"),
            ReferenceGroup("konflikt", "Zustimmung und Konflikt", "Zustimmungskatalog, Veto, Deadlock, Beschlussmangel, Geschäftsführer oder Gesellschafterstreit"),
            ReferenceGroup("sonderlage", "Sonderlagen und Transaktionen", "Familiengesellschaft, Investor, Bank, Sanierung, Insolvenz, Compliance, Datenschutz, Nachfolge oder M&A"),
        ],
        beirat_group,
        "Lies Satzung, Gesellschaftervereinbarung, Geschäftsordnung, Beteiligungsstruktur und konkrete Entscheidung zuerst. Bestimme danach, ob der Beirat nur berät, kontrolliert oder gesellschaftsvertraglich bindende Zustimmungskompetenzen erhält.",
        "Liefere je nach Auftrag Satzungs- oder Geschäftsordnungsklauseln, Zustimmungskatalog, Kompetenz- und Konfliktmatrix, Beschluss- oder Protokollentwurf sowie Vollzugs- und Haftungshinweise.",
    )


def bho_group(source: SkillSource) -> str:
    match = re.match(r"bho-(\d+)", source.slug)
    number = int(match.group(1)) if match else 999
    if number <= 22:
        return "01-22"
    if number <= 59:
        return "23-59"
    if number <= 99:
        return "60-99"
    return "100-plus"


def consolidate_bho() -> None:
    plugin = REPO / "haushaltsrecht-bho-bund-laender"
    router_slug = "bho-normen-und-titelpruefung"
    sources = [
        load_source(path)
        for path in sorted((plugin / "skills").glob("bho-*/SKILL.md"))
        if path.parent.name != router_slug
    ]
    if not sources:
        return
    build_router(
        plugin,
        router_slug,
        "BHO-Normen und Titelprüfung",
        "Für Bundeshaushaltsordnung, Haushaltstitel und Vollzugsfragen: routet BHO-Norm, Veranschlagung, Sperre, Deckung, Zuwendung, Vertrag, Vermögen und Rechnungshofprüfung in die passende Vertiefung.",
        sources,
        [
            ReferenceGroup("01-22", "BHO 1 bis 22", "Haushaltsplan, Veranschlagung, Deckung, Sperre oder Verpflichtungsermächtigung"),
            ReferenceGroup("23-59", "BHO 23 bis 59", "Zuwendung, Bauausgabe, überplanmäßige Ausgabe, Gewährleistung, Vergabe, Vertrag oder Forderung"),
            ReferenceGroup("60-99", "BHO 60 bis 99", "Vermögen, Unternehmen, Kasse, Rechnungslegung oder Bundesrechnungshof"),
            ReferenceGroup("100-plus", "Titel- und Sonderfallmodule", "Verteidigung, Sondervermögen, Zins, Personal, Förderung, EU-Mittel, Transfer oder Geheimschutz"),
        ],
        bho_group,
        "Lies Einzelplan, Kapitel, Titel, Haushaltsvermerk, Erläuterung, Bewirtschaftungsstand und beabsichtigte Maßnahme zuerst. Bestimme dann Norm, haushaltsmäßige Ermächtigung, Zuständigkeit, zeitliche Bindung und erforderlichen Nachweis.",
        "Liefere Titelprüfblatt, Normen- und Zuständigkeitsmatrix, Deckungs- oder Sperrentscheidung, Zuwendungs- oder Vertragsvermerk, BRH-feste Belegliste und den nächsten Vollzugsschritt.",
    )


def split_reference_document(text: str) -> tuple[str, list[str]]:
    matches = list(re.finditer(r"^##\s+.+$", text, flags=re.MULTILINE))
    if not matches:
        return text.rstrip() + "\n", []
    header = text[: matches[0].start()].rstrip() + "\n\n"
    modules: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        modules.append(text[match.start() : end].strip() + "\n")
    return header, modules


def module_topic(module: str) -> str:
    heading = module.splitlines()[0].removeprefix("## ").strip()
    if ":" in heading and heading.lower().startswith("lph "):
        heading = heading.rsplit(":", 1)[1].strip()
    replacements = {
        "Bho": "BHO",
        "Brh": "BRH",
        "Pruefen": "Prüfen",
        "Pruefung": "Prüfung",
        "Aenderung": "Änderung",
        "Faehigkeit": "Fähigkeit",
        "Erlaeuterung": "Erläuterung",
        "Uebertragbarkeit": "Übertragbarkeit",
        "Ueberplanmaessig": "Überplanmäßig",
        "Vermoegen": "Vermögen",
        "Foerderung": "Förderung",
        "Laender": "Länder",
        "Massnahmen": "Maßnahmen",
    }
    for old, new in replacements.items():
        heading = re.sub(rf"\b{old}\b", new, heading)
    return heading[:72].rstrip(" ,;:.-")


def rechunk_router_references(router_dir: Path) -> None:
    skill_file = router_dir / "SKILL.md"
    if not skill_file.is_file():
        return
    text = skill_file.read_text(encoding="utf-8")
    table_start = text.find("| Fallgruppe | Referenz | Nur laden bei |")
    table_end = text.find("\n\n## 3.", table_start)
    if table_start == -1 or table_end == -1:
        return
    table_lines = text[table_start:table_end].splitlines()
    if len(table_lines) < 3:
        return

    entries: list[dict[str, object]] = []
    by_key: dict[str, dict[str, object]] = {}
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3:
            continue
        label, link, trigger = cells
        match = re.search(r"\]\(\./references/([^)]+)\)", link)
        if not match:
            continue
        filename = match.group(1)
        stem = Path(filename).stem
        label_base = re.sub(r"\s+\d+$", "", label)
        has_chunk_suffix = label_base != label and bool(re.search(r"-\d{2}$", stem))
        key = stem[:-3] if has_chunk_suffix else stem
        if router_dir.name == "bho-normen-und-titelpruefung":
            if stem == "23" or stem.startswith("23-"):
                key, label_base = "23-59", "BHO 23 bis 59"
            elif stem == "60" or stem.startswith("60-"):
                key, label_base = "60-99", "BHO 60 bis 99"
            elif stem == "01" or stem.startswith("01-"):
                key, label_base = "01-22", "BHO 1 bis 22"
        item = by_key.get(key)
        if item is None:
            item = {
                "key": key,
                "label": label_base,
                "trigger": trigger.split("; enthält", 1)[0],
                "header": "",
                "modules": [],
                "files": [],
            }
            by_key[key] = item
            entries.append(item)
        reference = router_dir / "references" / filename
        if not reference.is_file():
            raise ValueError(f"Fehlende Routerreferenz: {reference.relative_to(REPO)}")
        header, modules = split_reference_document(reference.read_text(encoding="utf-8"))
        if not item["header"]:
            item["header"] = header
        item["modules"].extend(modules)
        item["files"].append(reference)

    new_rows: list[str] = []
    for item in entries:
        header = str(item["header"])
        modules = list(item["modules"])
        chunks: list[list[str]] = []
        current: list[str] = []
        current_size = len(header.encode("utf-8"))
        for module in modules:
            size = len(module.encode("utf-8")) + 1
            if current and current_size + size > MAX_REFERENCE_BYTES:
                chunks.append(current)
                current = []
                current_size = len(header.encode("utf-8"))
            current.append(module)
            current_size += size
        if current:
            chunks.append(current)
        if not chunks:
            continue

        for path in item["files"]:
            path.unlink()
        for index, chunk in enumerate(chunks, start=1):
            suffix = f"-{index:02d}" if len(chunks) > 1 else ""
            filename = f"{item['key']}{suffix}.md"
            content = header + "\n".join(module.rstrip() for module in chunk).rstrip() + "\n"
            (router_dir / "references" / filename).write_text(content, encoding="utf-8")
            label = str(item["label"]) + (f" {index}" if suffix else "")
            topics = ", ".join(module_topic(module) for module in chunk[:5])
            if len(chunk) > 5:
                topics += f" und {len(chunk) - 5} weitere Module"
            topics = topics[:260].rstrip(" ,;:.-")
            new_rows.append(
                f"| {label} | [{filename}](./references/{filename}) | "
                f"{item['trigger']}; enthält {topics} |"
            )

    new_table = "\n".join(table_lines[:2] + new_rows)
    skill_file.write_text(text[:table_start] + new_table + text[table_end:], encoding="utf-8")


def generated_router_dirs() -> list[Path]:
    return [
        *(REPO / "hoai-leistungsphasen-praxis" / "skills").glob("lph-??-arbeitsrouter"),
        REPO / "kartellrecht-marktabgrenzung-pruefung" / "skills" / "internationale-kartellrechts-jurisdiktionen",
        REPO / "datenschutzrecht" / "skills" / "meldung-deutsche-aufsichtsbehoerde",
        REPO / "steuerrecht-anwalt-und-berater" / "skills" / "dba-alle-abkommen-laendermatrix-2026",
        REPO / "steuerrecht-anwalt-und-berater" / "skills" / "lohnabrechnung-und-arbeitgeberpflichten",
        REPO / "steuerrecht-anwalt-und-berater" / "skills" / "bwa-analyse-und-mandantenbericht",
        REPO / "steuerrecht-anwalt-und-berater" / "skills" / "sanierungsgewinn-steuerpruefung",
        REPO / "grosskanzlei-corporate-ma" / "skills" / "beirat-gestaltung-und-governance",
        REPO / "haushaltsrecht-bho-bund-laender" / "skills" / "bho-normen-und-titelpruefung",
    ]


def rechunk_generated_routers() -> None:
    for router in generated_router_dirs():
        rechunk_router_references(router)


def repair_generated_reference_links() -> None:
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for router in generated_router_dirs():
        for path in sorted((router / "references").glob("*.md")):
            text = path.read_text(encoding="utf-8")

            def repl(match: re.Match[str]) -> str:
                label, href = match.groups()
                if href.startswith(("http://", "https://", "mailto:", "#")):
                    return match.group(0)
                href_path = href.split("#", 1)[0]
                anchor = "#" + href.split("#", 1)[1] if "#" in href else ""
                target = (path.parent / href_path).resolve()
                if target.exists():
                    return match.group(0)
                if Path(href_path).name.startswith("vertiefung-"):
                    return label
                candidate = (path.parent / ".." / href_path).resolve()
                if candidate.exists():
                    relative = os.path.relpath(candidate, path.parent).replace(os.sep, "/")
                    return f"[{label}]({relative}{anchor})"
                return match.group(0)

            updated = pattern.sub(repl, text)
            if updated != text:
                path.write_text(updated, encoding="utf-8")


def refresh_hoai_direct_starts() -> None:
    skills = REPO / "hoai-leistungsphasen-praxis" / "skills"
    for phase, (name, focus) in HOAI_PHASES.items():
        path = skills / f"lph-{phase:02d}-arbeitsrouter" / "SKILL.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        replacement = (
            f"Arbeite ausschließlich in Leistungsphase {phase} ({name}), solange Unterlagen und Auftrag "
            "keine belastbare Schnittstelle zu einer anderen Phase zeigen. "
            f"{focus[0].upper() + focus[1:]} bilden den Einstieg."
        )
        text = re.sub(
            rf"Arbeite ausschließlich in Leistungsphase {phase} \({re.escape(name)}\),.*?bilden den Einstieg\.",
            replacement,
            text,
            count=1,
        )
        path.write_text(text, encoding="utf-8")


def main() -> int:
    before = sum(1 for directory in marketplace_plugin_dirs() for _ in (directory / "skills").glob("*/SKILL.md"))
    aliases = consolidate_exact_aliases()
    consolidate_hoai()
    consolidate_kartell_jurisdictions()
    consolidate_data_authorities()
    consolidate_dba_countries()
    consolidate_tax_families()
    consolidate_beirat()
    consolidate_bho()
    rechunk_generated_routers()
    repair_generated_reference_links()
    refresh_hoai_direct_starts()
    after = sum(1 for directory in marketplace_plugin_dirs() for _ in (directory / "skills").glob("*/SKILL.md"))
    print(f"Doppelte Routen konsolidiert: {len(aliases)}")
    print(f"Direkte Skills vorher: {before}")
    print(f"Direkte Skills nachher: {after}")
    print(f"Direkte Routen eingespart: {before - after}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
