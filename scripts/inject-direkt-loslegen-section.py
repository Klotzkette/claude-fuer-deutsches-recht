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
    "Rechtswegerschoepfung": "Rechtswegerschöpfung",
    "Referentenentwuerfen": "Referentenentwürfen",
    "Schluessigkeit": "Schlüssigkeit",
    "Schriftsaetze": "Schriftsätze",
    "Subsidiaritaet": "Subsidiarität",
    "Suedafrika": "Südafrika",
    "Syndikus-Anwaelten": "Syndikus-Anwälten",
    "Taetigkeiten": "Tätigkeiten",
    "Teilungserklaerung": "Teilungserklärung",
    "Umstaende": "Umstände",
    "Universitaetsstaedte": "Universitätsstädte",
    "UrhG-Bezuege": "UrhG-Bezüge",
    "VVG-Bezuege": "VVG-Bezüge",
    "Veraenderungen": "Veränderungen",
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
            return title.replace("§§", "Paragrafen").replace("§", "Paragraf")
    return akte_slug


def testakte_download_cell(plugin_name: str, directory: Path, akten_slugs: list[str]) -> str:
    pluginlocal_parts = []
    if (directory / "testakte").is_dir():
        pdf = directory / "testakte" / "gesamt-pdf" / "testakte_gesamt.pdf"
        if pdf.is_file():
            pluginlocal_parts.append("[Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf)")
        pluginlocal_parts.append(f"[`{plugin_name}-testakte.zip`]({RELEASE_BASE}/{plugin_name}-testakte.zip)")
        pluginlocal_parts.append(f"[`{plugin_name}-testakte-einzelpdfs.zip`]({RELEASE_BASE}/{plugin_name}-testakte-einzelpdfs.zip)")
    if akten_slugs:
        parts = []
        for slug in akten_slugs:
            title = get_akte_title(slug).replace("|", "-")
            pdf_rel = Path(
                relpath(TESTAKTEN_DIR / slug / "gesamt-pdf" / f"{slug}_gesamt.pdf", start=directory)
            ).as_posix()
            parts.append(
                f"{title}: "
                f"[Gesamt-PDF]({pdf_rel}), "
                f"[`testakte-{slug}.zip`]({RELEASE_BASE}/testakte-{slug}.zip), "
                f"[`testakte-{slug}-einzelpdfs.zip`]({RELEASE_BASE}/testakte-{slug}-einzelpdfs.zip)"
            )
        if pluginlocal_parts:
            parts.append("Pluginlokale Akte: " + ", ".join(pluginlocal_parts))
        return "; ".join(parts)
    if pluginlocal_parts:
        return ", ".join(pluginlocal_parts)
    return (
        f"[`alle-testakten.zip`]({RELEASE_BASE}/alle-testakten.zip) "
        f"und [`alle-testakten-einzelpdfs.zip`]({RELEASE_BASE}/alle-testakten-einzelpdfs.zip) (zentrale Sammlung)"
    )


def markdown_text(value: str) -> str:
    text = re.sub(r"\s+", " ", value).strip().replace("|", "-")
    for old, new in sorted(PROSE_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(old, new)
    return text


def block(plugin: dict, directory: Path, akten_slugs: list[str]) -> str:
    plugin_name = plugin["name"]
    stem = prompt_stem(plugin_name)
    werkstatt_file = f"{stem}-werkstatt.md"
    schnellstart_file = f"{stem}-schnellstart.md"
    raw_dir = f"{RAW_BASE}/{directory.relative_to(REPO).as_posix()}"
    werkstatt_url = f"{raw_dir}/{werkstatt_file}"
    schnellstart_url = f"{raw_dir}/{schnellstart_file}"
    testakte_cell = testakte_download_cell(plugin_name, directory, akten_slugs)
    description = markdown_text(plugin.get("description") or readme_title(directory, plugin_name))
    return f"""{BEGIN}
## Was ist das hier?

{description}

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`{plugin_name}.zip`]({RELEASE_BASE}/{plugin_name}.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="{werkstatt_url}" download><code>{werkstatt_file}</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="{schnellstart_url}" download><code>{schnellstart_file}</code></a> |
| Testakte(n) als ZIP | ZIP | {testakte_cell} |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
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


def inject(plugin: dict, akten_slugs: list[str]) -> str:
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
        + block(plugin, directory, akten_slugs)
        + "\n\n"
        + stripped[pos:].lstrip()
    )
    if new_text == text:
        return "UNCHANGED"
    readme.write_text(new_text, encoding="utf-8")
    return "UPDATED" if BEGIN in text else "INSERTED"


def main() -> int:
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    mapping = discover_testakten_mapping(plugins)
    counts = {"INSERTED": 0, "UPDATED": 0, "UNCHANGED": 0, "SKIPPED": 0}
    for plugin in plugins:
        status = inject(plugin, mapping.get(plugin["name"], []))
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
