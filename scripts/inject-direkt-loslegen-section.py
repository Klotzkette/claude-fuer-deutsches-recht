#!/usr/bin/env python3
"""Fügt pro Plugin einen Direkt-loslegen-Block für Prompt-Downloads ein.

Der Block steht direkt nach dem H1.
Alte Megaprompt-Hinweisblöcke werden entfernt, damit die README nicht zwei
konkurrierende Ein-Datei-Pfade beschreibt.
"""

from __future__ import annotations

import json
import re
from os.path import relpath
from pathlib import Path

from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
TESTAKTEN_DIR = REPO / "testakten"

BEGIN = "<!-- BEGIN direkt-loslegen (autogen) -->"
END = "<!-- END direkt-loslegen (autogen) -->"
OLD_MEGA_BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
OLD_MEGA_END = "<!-- END megaprompt-und-vorlagen (autogen) -->"
OLD_SOFORT_BEGIN = "<!-- BEGIN plugin-sofort-download-section (autogen) -->"
OLD_SOFORT_END = "<!-- END plugin-sofort-download-section (autogen) -->"
RELEASE_BASE = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"
RAW_BASE = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"
DISALLOWED_ABBR = chr(75) + chr(73)
DISALLOWED_MIXED = chr(75) + "i"
PROSE_REPLACEMENTS = {
    "Abwaegung": "Abwägung",
    "Aerzte": "Ärzte",
    "Aktenlektuere": "Aktenlektüre",
    "Ampel-Einschaetzung": "Ampel-Einschätzung",
    "Anwaelte": "Anwälte",
    "Anwaelten": "Anwälten",
    "Ausfluegen": "Ausflügen",
    "Bautraegervertraege": "Bauträgerverträge",
    "Bautraeger": "Bauträger",
    "Beschluesse": "Beschlüsse",
    "Bewaehrung": "Bewährung",
    "Big-Law-Anfaenger": "Big-Law-Anfänger",
    "Buergergeld": "Bürgergeld",
    "Bruessel": "Brüssel",
    "Duesseldorfer": "Düsseldorfer",
    "EPUe": "EPÜ",
    "Eigentuemerversammlung": "Eigentümerversammlung",
    "Einschaetzung": "Einschätzung",
    "Entschaedigung": "Entschädigung",
    "Erfuellungsaufwand": "Erfüllungsaufwand",
    "Ergaenzend": "Ergänzend",
    "Erklaerungen": "Erklärungen",
    "Ermittlungsfuehrung": "Ermittlungsführung",
    "Empfaenger": "Empfänger",
    "Geschaeftsgeheimnis": "Geschäftsgeheimnis",
    "Gesetzentwuerfen": "Gesetzentwürfen",
    "Guetetermin": "Gütetermin",
    "Hinweisverfuegung": "Hinweisverfügung",
    "IP-Lizenzvertraege": "IP-Lizenzverträge",
    "Loeschung": "Löschung",
    "Luecken-Ampel": "Lücken-Ampel",
    "Lueckenliste": "Lückenliste",
    "Luecken": "Lücken",
    "Maengelhaftung": "Mängelhaftung",
    "Mieterhoehungs-Widerspruch": "Mieterhöhungs-Widerspruch",
    "Parteivortraege": "Parteivorträge",
    "Patentanwaelte": "Patentanwälte",
    "Plaedoyer": "Plädoyer",
    "Praezedenzarbeit": "Präzedenzarbeit",
    "Prueft": "Prüft",
    "fuehrt": "führt",
    "Rechtswegerschoepfung": "Rechtswegerschöpfung",
    "Referentenentwuerfen": "Referentenentwürfen",
    "Schluessigkeit": "Schlüssigkeit",
    "Schriftsaetze": "Schriftsätze",
    "Subsidiaritaet": "Subsidiarität",
    "Suedafrika": "Südafrika",
    "Syndikus-Anwaelten": "Syndikus-Anwälten",
    "Taetigkeiten": "Tätigkeiten",
    "Taetigkeitsbild": "Tätigkeitsbild",
    "Teilungserklaerung": "Teilungserklärung",
    "Umstaende": "Umstände",
    "Universitaetsstaedte": "Universitätsstädte",
    "UrhG-Bezuege": "UrhG-Bezüge",
    "VVG-Bezuege": "VVG-Bezüge",
    "Veraenderungen": "Veränderungen",
    "Verknuepft": "Verknüpft",
    "Versaeumnisurteil": "Versäumnisurteil",
    "Verspaetung": "Verspätung",
    "Verstoessen": "Verstößen",
    "Widersprueche": "Widersprüche",
    "Wuerfel": "Würfel",
    "Zwischenverfuegung": "Zwischenverfügung",
    "Zwoelf-Monats-Liquidität": "Zwölf-Monats-Liquidität",
    "außergewoehnliche": "außergewöhnliche",
    "buergerlichen": "bürgerlichen",
    "ergaenzbar": "ergänzbar",
    "europaeische": "europäische",
    "foermlich": "förmlich",
    "fuenf": "fünf",
    "fuer": "für",
    "gefuehrte": "geführte",
    "hoefliche": "höfliche",
    "prueft": "prüft",
    "papsttreues": "papsttreues",
}
SKIP_TESTAKTEN_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}
PLUGIN_ALIASES = {
    "bauplanungsrecht": ["normenkontrolle-bauleitplanung"],
    "cisg-handelskauf": ["urteilsbauer-relationsmacher"],
    "dsgvo": ["datenschutzrecht"],
    "internationales-privatrecht": ["urteilsbauer-relationsmacher"],
}


def prompt_stem(plugin_name: str) -> str:
    return plugin_name


def human_title(slug: str) -> str:
    words = [w for w in re.split(r"[-_]+", slug) if w]
    out = []
    for word in words:
        if word in {"und", "oder", "mit", "im", "am", "zur", "zum", "der", "die", "das"}:
            out.append(word)
        elif word == "fuer":
            out.append("für")
        elif len(word) <= 3:
            out.append(word.upper())
        else:
            out.append(word[:1].upper() + word[1:])
    return " ".join(out)


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def readme_title(directory: Path, fallback: str) -> str:
    readme = directory / "README.md"
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return human_title(fallback)


def add_mapping(mapping: dict[str, set[str]], plugin_names: set[str], slug: str, text: str) -> None:
    tokens = set(re.findall(r"`([^`]+)`", text))
    for token in tokens:
        if token in plugin_names:
            mapping.setdefault(token, set()).add(slug)
        for alias_target in PLUGIN_ALIASES.get(token, []):
            if alias_target in plugin_names:
                mapping.setdefault(alias_target, set()).add(slug)


def discover_testakten_mapping(plugins: list[dict]) -> dict[str, list[str]]:
    mapping: dict[str, set[str]] = {}
    plugin_names = {p["name"] for p in plugins}
    if not TESTAKTEN_DIR.exists():
        return {}
    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir() or sub.name in SKIP_TESTAKTEN_DIRS:
            continue
        readme = sub / "README.md"
        if readme.is_file():
            add_mapping(mapping, plugin_names, sub.name, readme.read_text(encoding="utf-8"))
    overview = TESTAKTEN_DIR / "README.md"
    if overview.is_file():
        for line in overview.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\| \[`([^/]+)/`\]\(\./\1/\) \|", line)
            if m:
                add_mapping(mapping, plugin_names, m.group(1), line)
    return {plugin: sorted(akten) for plugin, akten in mapping.items()}


def get_akte_title(akte_slug: str) -> str:
    readme = TESTAKTEN_DIR / akte_slug / "README.md"
    if not readme.is_file():
        return akte_slug
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            title = re.sub(
                r"^(Akte|Beispielakte|Testakte|Mandantenakte)\s*[:–-]\s*",
                "",
                title,
                flags=re.IGNORECASE,
            )
            return title.replace(chr(167) * 2, "Paragrafen").replace(chr(167), "Paragraf")
    return akte_slug


def display_akte_title(title: str) -> str:
    text = title.replace("|", "-")
    text = text.replace(DISALLOWED_ABBR + "-Training", "Trainingsdaten")
    text = text.replace(DISALLOWED_ABBR + " Training", "Trainingsdaten")
    text = text.replace("Musik " + DISALLOWED_MIXED + " Songstreit", "Musik-Songstreit")
    text = re.sub(r"\b" + re.escape(DISALLOWED_ABBR) + r"\b", "digitale Systeme", text)
    text = re.sub(r"\b" + re.escape(DISALLOWED_MIXED) + r"\b", "digitale Systeme", text)
    return text


def relative_link(directory: Path, target: Path) -> str:
    return Path(relpath(target, start=directory)).as_posix()


def navigation(plugin_name: str, directory: Path) -> str:
    root = relative_link(directory, REPO / "README.md")
    skills = relative_link(directory, REPO / "SKILLS.md")
    detail = relative_link(directory, REPO / "skills-index" / f"{plugin_name}.md")
    assets = relative_link(directory, REPO / "ASSET_INDEX.md")
    testakten = relative_link(directory, TESTAKTEN_DIR / "README.md")
    return (
        "Direktnavigation: "
        "[30-Sekunden-Start](#in-30-sekunden-starten) · "
        f"[Startseite]({root}) · "
        f"[Plugin-Katalog]({root}#was-ist-drin) · "
        f"[Skill-Gesamtübersicht]({skills}) · "
        f"[Skills dieses Plugins]({detail}) · "
        "[Plugin-Dateien](.) · "
        f"[Download-Index]({assets}) · "
        f"[Testakten]({testakten})"
    )


def compact_prompt_fragment(value: str, limit: int = 210) -> str:
    text = re.sub(r"[`*_#]", "", value)
    text = re.sub(r"\s+", " ", text).strip().rstrip(" .;:")
    if len(text) <= limit:
        return text
    clipped = text[: limit + 1].rsplit(" ", 1)[0].rstrip(" ,;:")
    return clipped + " ..."


HANDCURATED_FIRST_PRODUCTS = {
    "mietrecht": "eine Anspruchs- und Fristenmatrix mit nächstem Schreiben",
    "arbeitsrecht": "Antrag, Sachverhalt, Beweisplan und nächste Frist",
    "fachanwalt-familienrecht": "eine Rechnung, Verfahrensroute oder einen antragsfähigen Text",
    "fachanwalt-erbrecht": "eine Erbfolge-, Auskunfts- oder Pflichtteilsroute",
    "richter-familiengericht": "eine verfahrensleitende Verfügung oder einen belastbaren Entscheidungsentwurf",
    "staatsanwaltschaft-amtsanwaltschaft": "eine Dezernatsverfügung mit Tat-, Beweis- und Fristenkontrolle",
    "bautraegervertragspruefer": "eine Klauselmatrix mit Mandantengutachten und Änderungswünschen",
    "bautraegervertrag-pruefer": "eine Klauselmatrix mit Mandantenvermerk und Verhandlungsposition",
    "urteilsbauer-relationsmacher": "eine Zergliederung, Relation oder einen Entscheidungsentwurf",
    "anlagen-zu-schriftsaetzen": "eine Produktionsmatrix und kontrollierte Gerichtsmappe",
    "schriftsatz-versandwerkstatt": "eine Produktionsmatrix und kontrollierte Versandmappe",
}


def first_product(directory: Path, plugin_name: str) -> str:
    if plugin_name in HANDCURATED_FIRST_PRODUCTS:
        return HANDCURATED_FIRST_PRODUCTS[plugin_name]
    path = directory / f"{plugin_name}-schnellstart.md"
    if not path.is_file():
        return "einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument"
    text = path.read_text(encoding="utf-8", errors="ignore")
    patterns = (
        r"^\d+\. Erstes Arbeitsprodukt liefern:\s*(.+?)\.?$",
        r"^\d+\.\d+\. Ausgang:\s*(.+?)\.?$",
        r"Das Endprodukt ist\s+(.+?)\.",
        r"Ergebnis ist\s+(.+?)\.",
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE)
        if match:
            product = re.sub(r"\s+liefern;.*$", "", match.group(1), flags=re.IGNORECASE)
            return compact_prompt_fragment(product)
    return "einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument"


def quickstart_section(plugin_name: str, directory: Path) -> str:
    title = readme_title(directory, plugin_name)
    product = first_product(directory, plugin_name)
    detail = relative_link(directory, REPO / "skills-index" / f"{plugin_name}.md")
    return f"""## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste]({detail}) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für {title}:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet. Beginne mit folgendem Arbeitsschritt: {product}. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen."""


def has_plugin_local_testakte(directory: Path) -> bool:
    testakte = directory / "testakte"
    return testakte.is_dir() and bool(
        working_dump_flat_pairs(testakte, include_gesamt_pdf=False)
    )


def testakte_count(directory: Path, akten_slugs: list[str]) -> int:
    return len(akten_slugs) + int(has_plugin_local_testakte(directory))


def testakte_download_cell(directory: Path, akten_slugs: list[str]) -> str:
    count = testakte_count(directory, akten_slugs)
    if count:
        label = "eine zugeordnete Akte" if count == 1 else f"{count} zugeordnete Akten"
        return f"[{label}](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs"
    return (
        f"[`alle-testakten.zip`]({RELEASE_BASE}/alle-testakten.zip) und "
        f"[`alle-testakten-einzelpdfs.zip`]({RELEASE_BASE}/alle-testakten-einzelpdfs.zip) "
        "(zentrale Sammlung)"
    )


def testakten_section(plugin_name: str, directory: Path, akten_slugs: list[str]) -> str:
    if not testakte_count(directory, akten_slugs):
        return ""

    lines = [
        "## Zugeordnete Testakten",
        "",
        "Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.",
        "",
        "| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |",
        "| --- | --- | --- | --- |",
    ]
    if has_plugin_local_testakte(directory):
        pdf = directory / "testakte" / "gesamt-pdf" / "testakte_gesamt.pdf"
        pdf_link = "[Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf)" if pdf.is_file() else "nicht vorhanden"
        lines.append(
            "| Pluginlokale Akte | "
            f"{pdf_link} | "
            f"[`{plugin_name}-testakte.zip`]({RELEASE_BASE}/{plugin_name}-testakte.zip) | "
            f"[`{plugin_name}-testakte-einzelpdfs.zip`]({RELEASE_BASE}/{plugin_name}-testakte-einzelpdfs.zip) |"
        )
    for slug in akten_slugs:
        title = display_akte_title(get_akte_title(slug)).replace("[", "").replace("]", "")
        pdf_rel = relative_link(
            directory,
            TESTAKTEN_DIR / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf",
        )
        lines.append(
            f"| [{title}]({relative_link(directory, TESTAKTEN_DIR / slug / 'README.md')}) | "
            f"[Gesamt-PDF]({pdf_rel}) | "
            f"[`testakte-{slug}.zip`]({RELEASE_BASE}/testakte-{slug}.zip) | "
            f"[`testakte-{slug}-einzelpdfs.zip`]({RELEASE_BASE}/testakte-{slug}-einzelpdfs.zip) |"
        )
    testakten_overview = relative_link(directory, TESTAKTEN_DIR / "README.md")
    lines.extend(["", f"[Alle Testakten und Fachzuordnungen]({testakten_overview})"])
    return "\n".join(lines)


def markdown_text(value: str) -> str:
    text = re.sub(r"\s+", " ", value).strip().replace("|", "-")
    text = text.replace(chr(167) * 2, "Paragrafen").replace(chr(167), "Paragraf")
    for old, new in sorted(PROSE_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(old, new)
    return text


def block(plugin: dict, directory: Path, akten_slugs: list[str], marketplace_count: int) -> str:
    plugin_name = plugin["name"]
    stem = prompt_stem(plugin_name)
    werkstatt_file = f"{stem}-werkstatt.md"
    schnellstart_file = f"{stem}-schnellstart.md"
    raw_dir = f"{RAW_BASE}/{directory.relative_to(REPO).as_posix()}"
    werkstatt_url = f"{raw_dir}/{werkstatt_file}"
    schnellstart_url = f"{raw_dir}/{schnellstart_file}"
    testakte_cell = testakte_download_cell(directory, akten_slugs)
    description = markdown_text(plugin.get("description") or readme_title(directory, plugin_name))
    assets = relative_link(directory, REPO / "ASSET_INDEX.md")
    testakten = testakten_section(plugin_name, directory, akten_slugs)
    testakten_block = f"\n\n{testakten}" if testakten else ""
    quickstart = quickstart_section(plugin_name, directory)
    return f"""{BEGIN}
## Was ist das hier?

{description}

Dieses Plugin gehört zum Marketplace mit {marketplace_count} Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

{navigation(plugin_name, directory)}

{quickstart}

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`{plugin_name}.zip`]({RELEASE_BASE}/{plugin_name}.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="{schnellstart_url}" download><code>{schnellstart_file}</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="{werkstatt_url}" download><code>{werkstatt_file}</code></a> |
| Zugeordnete Testakten | PDF / ZIP | {testakte_cell} |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit {marketplace_count} Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`]({RELEASE_BASE}/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index]({assets}); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.{testakten_block}
{END}"""


def strip_old_blocks(text: str) -> str:
    for begin, end in [(BEGIN, END), (OLD_MEGA_BEGIN, OLD_MEGA_END), (OLD_SOFORT_BEGIN, OLD_SOFORT_END)]:
        if begin in text and end in text:
            text = re.sub(
                r"\n*" + re.escape(begin) + r"[\s\S]*?" + re.escape(end) + r"\n*",
                "\n",
                text,
                count=1,
            )
    return text


def insert_position(text: str) -> int:
    match = re.search(r"^# .+$", text, flags=re.MULTILINE)
    if not match:
        return 0
    pos = match.end()
    while pos < len(text) and text[pos] == "\n":
        pos += 1
    return pos


def inject(plugin: dict, akten_slugs: list[str], marketplace_count: int) -> str:
    name = plugin["name"]
    directory = plugin_dir(plugin)
    readme = directory / "README.md"
    if not readme.is_file():
        return "SKIPPED"
    text = readme.read_text(encoding="utf-8")
    stripped = strip_old_blocks(text)
    pos = insert_position(stripped)
    new_text = (
        stripped[:pos].rstrip()
        + "\n\n"
        + block(plugin, directory, akten_slugs, marketplace_count)
        + "\n\n"
        + stripped[pos:].lstrip()
    )
    if new_text == text:
        return "UNCHANGED"
    readme.write_text(new_text, encoding="utf-8")
    return "UPDATED" if BEGIN in text else "INSERTED"


def main() -> int:
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    marketplace_count = len(plugins)
    mapping = discover_testakten_mapping(plugins)
    counts = {"INSERTED": 0, "UPDATED": 0, "UNCHANGED": 0, "SKIPPED": 0}
    for plugin in plugins:
        status = inject(plugin, mapping.get(plugin["name"], []), marketplace_count)
        counts[status] += 1
        if status in {"INSERTED", "UPDATED"}:
            print(f"{status:8s} {plugin['name']}")
    print(
        f"Fertig: {counts['INSERTED']} neu, {counts['UPDATED']} aktualisiert, "
        f"{counts['UNCHANGED']} unveraendert, {counts['SKIPPED']} uebersprungen"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
