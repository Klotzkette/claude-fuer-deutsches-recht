#!/usr/bin/env python3
"""Validiert die Vorlagensammlung.

Prüfungen:
- Zu jeder sprechend benannten Markdown-Datei existiert eine gleichnamige ODT-Datei.
- Markdown und ODT tragen den Vorlagenordner-Slug als Dateistamm.
- Jeder Vorlagen-Unterordner enthält eine README.md.
- Das Wurzel-README verlinkt jeden Themenordner; jedes Bereichs-README verlinkt jede Vorlage.
- Jede Vorlagen-README enthält exakte ODT- und Markdown-ZIP-Downloads sowie lokale Vorschauen.
- Jede Vorlagen-Markdown-Datei enthält den kurzen Pflicht-Hinweis (BRAO, StGB, DSGVO, Lizenz).
- Jede Vorlagen-Markdown-Datei verweist knapp auf Experiment, Unverbindlichkeit und Eigengefahr.
- Jede Vorlagen-Markdown-Datei enthält einen Rubrum-/Adressatenkopf und einen Schluss-/Unterzeichnungsblock.
- Warnhinweise bezeichnen den Dokumenttyp nicht widersprüchlich als Vertrag oder Schriftsatz.
- Der repoweite Direktdownloadindex ist aktuell und im Wurzel-README verlinkt.
- Relative Markdown-Links im nutzerseitigen Bestand führen auf vorhandene Dateien oder Ordner.
- Jede Vorlagen-Markdown-Datei bleibt frei von langen Hinweisabschnitten, die in die README gehören.
- Frühere generische Anlagenhüllen und redundante Universalrubren kehren nicht zurück.
- Platzhalter in Vorlagen-Markdown-Dateien sind eindeutig und nicht ineinander verschachtelt.
- Keine gängigen Umlaut-Umschreibungen in deutschen Texten (Heuristik).
- 40 erwartete Themenordner sind vorhanden.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _vorlagen_dateien import (  # noqa: E402
    THEMENORDNER,
    ist_generischer_stem,
    md_in as _md_in,
    odt_in as _odt_in,
    pruefe_bestandsstruktur,
)

ERWARTETE_THEMEN = set(THEMENORDNER)

PFLICHT_TOKENS = [
    "43a",        # BRAO
    "203",        # StGB
    "DSGVO",
    "Apache-2.0", # Lizenz
    "MIT",
    "experimenteller Text",
    "eigene Gewähr",
    "eigene Gefahr",
    "keine Rechtsberatung",
    "unverbindlich",
]

README_PFLICHT_TOKENS = list(PFLICHT_TOKENS)

VERBOTENE_TEMPLATE_ABSCHNITTE = [
    "## Einschlägige Normen",
    "## Normen- und Quellenanker",
    "## Normen / Legal Framework",
    "## Normen und Quellen / Legal Framework",
    "## Besondere Warnhinweise",
    "## Zweck und Einsatzbereich",
    "## Zweck / Purpose",
    "## Typische Prüfpunkte",
    "## Einsatzgrenzen",
    "## Bearbeitungshinweise",
    "## Spezifische Hinweise",
    "## Hinweise",
    "## Mandatsreife Prüfmatrix",
    "### Mandatsreife Prüfmatrix",
]

VERBOTENE_GENERIK_BAUSTEINE = {
    "generische Anlagenherkunft":
        "Echtheit und Herkunft: [Quelle / Aussteller / Abrufdatum / Übermittlungsweg]",
    "generische Anlagenkurzbeschreibung":
        "Inhaltliche Kurzbeschreibung: [konkreter Inhalt, Zeitraum, Betrag, Frist, technische Daten oder Korrespondenz]",
    "generische Anlagenabgrenzung":
        "Abgrenzung: [nicht enthaltene Punkte / streitige Teile / nachzureichende Unterlagen]",
    "generische Anlagenfreigabe":
        "Identität, Vertretung und Berechtigung geprüft: [ja / nein / offen]",
    "generische Anlagenakte":
        "Tatsachen, Beträge, Fristen und Erklärungen werden nur aus der Akte übernommen.",
    "generische Belegprüfung":
        "Jede Position ist durch einen Beleg oder eine nachvollziehbare Berechnung gedeckt.",
    "redundantes Universalrubrum":
        "Gericht / Behörde / Stelle: [Bezeichnung, Anschrift, Spruchkörper oder Referat, soweit bekannt].",
    "generischer Einreichungsblock":
        "**Einreichende oder versendende Seite:** [Partei / Kanzlei / Behörde / Gremium]",
    "generische Absenderrolle":
        "Absenderin / Auftraggeberin / vertretene Partei: [vollständiger Name oder Firma, Anschrift, Vertretung].",
    "generische Empfängerrolle":
        "Adressatin / Gegnerin / Behörde: [vollständiger Name oder Firma, Anschrift, Referat oder Stelle].",
    "generischer Metadatenkopf":
        "Adressat oder Verwendungszweck: [Gericht / Behörde / Vertragspartner / intern / Mandantin oder Mandant].",
    "generische Vertragsparteien":
        "[vollständiger Name oder Firma der ersten Vertragspartei, Rechtsform, Register, Sitz, Anschrift und Vertretung]",
    "generischer Freigabekopf":
        "**Weitere Zustimmung / notarielle oder registerrechtliche Freigabe:**",
    "generische Beteiligten-Sammelrolle":
        "Weitere Beteiligte, Sicherheitengeber, Berater oder Zustimmungsberechtigte sind [Name, Rolle, Vertretung / keine].",
    "zweisprachiger Metatext":
        "Diese zweisprachige Vorlage betrifft",
    "generischer Vollzugskern":
        "2. Ausfüll- und Vollzugskern",
    "leere Anlagenzwischenüberschrift":
        "1. Inhalt der Anlage",
    "generischer energierechtlicher Anlagenbezug":
        "1.2 Energierechtlicher Bezug: [Netzanschluss / Lieferstelle / Messkonzept / Konzessionsgebiet / Abrechnung / regulatorische Frist].",
    "generischer Verfahrensleitungskern":
        "Dokumentspezifischer Kern für Verfahrensleitung: [konkreter Entscheidungsgegenstand, beteiligte Personen, Fristen, Zustellung, Entscheidungsmaßstab und Vollzug].",
    "generischer Platzhalter-Freigabehinweis":
        "Bei der Verfahrensleitung muss jeder Platzhalter durch eine aktenkundige Tatsache, eine konkrete Frist oder eine bewusst gestrichene Alternative ersetzt werden; ungefüllte Platzhalter sind ein Freigabehindernis.",
    "generischer Bedienhinweis":
        "Platzhalter in eckigen Klammern sind vor Verwendung zu füllen oder bewusst zu streichen. Keine Akteninhalte in nicht freigegebene Systeme eingeben.",
    "generischer Zugangs- und Verwahrungsblock":
        "**Zugang / Verwahrung / Bekanntgabe:** [Empfängerin oder Empfänger], [Übermittlungsweg], [Datum], [Nachweis].",
    "generischer Vollmachtsumfang":
        "Hiermit bevollmächtigt die unterzeichnende Person [Kanzlei / Rechtsanwältin / Rechtsanwalt], sie in der Angelegenheit [Gegenstand] außergerichtlich und gerichtlich zu vertreten.",
    "generische Vertragsleistungshaftung":
        "Jede Partei haftet für schuldhafte Verletzungen ihrer Vertragspflichten nach §§ 280 Abs. 1, 241 Abs. 2 und 276 BGB, soweit diese Vereinbarung keine wirksame abweichende Regelung enthält.",
    "generische Leistungsstörungsanzeige":
        "Leistungsstörungen werden in Textform angezeigt. Die Anzeige bezeichnet Pflichtverletzung, Abhilfemaßnahme, Frist und Rechtsfolge. Unbestimmte Beanstandungen lösen keine Rückabwicklung aus.",
    "generische Compliance-Sammelklausel":
        "Die Parteien beachten Datenschutz, Geschäftsgeheimnisse, Berufsgeheimnisse, Sanktionen, Geldwäscheprävention, Exportkontrolle und Aufsichtsrecht, soweit einschlägig.",
    "generische Datenschutz-Sammelklausel":
        "Personenbezogene Daten werden nur verarbeitet, soweit eine Rechtsgrundlage besteht. Auftragsverarbeitung, gemeinsame Verantwortlichkeit, Drittlandtransfer und Löschung sind vor Vollzug zu dokumentieren.",
    "generische Vertragslaufzeit":
        "Diese Vereinbarung beginnt mit Unterzeichnung und läuft bis [Datum / Ereignis / vollständige Abwicklung].",
    "generische Kündigungsheilung":
        "Jede Partei kann aus wichtigem Grund kündigen, wenn die andere Partei eine wesentliche Pflicht verletzt und die Pflichtverletzung trotz Abmahnung nicht binnen [zehn Bankarbeitstagen] heilt.",
    "generische Beendigungsfolgen":
        "Nach Beendigung bleiben Vertraulichkeit, Datenschutz, Herausgabe, Abrechnung, Freistellung, Haftung und Streitbeilegung bestehen, soweit ihr Zweck dies erfordert.",
    "generisches Anlageninventar":
        "Register-, Rechte-, Forderungs-, Daten- oder Projektnachweise: [Liste]",
    "generische Anlagenprüfung":
        "Steuer-, Aufsichts-, Datenschutz- und Sanktionsprüfung: [Stand]",
    "generische Vollzugskontrolle":
        "Vollzug und Kontrolle: [Zustellung oder Bekanntgabe, Fristbeginn, Fristablauf, Wiedervorlage, Rechtsmittel- oder Beschwerdebelehrung, falls erforderlich].",
}

RUBRUM_MARKER = [
    "### Rubrum,",
    "### Notarieller Urkundseingang",
    "### Vertragseingang",
    "### Verantwortlicher, betroffene Person und Informationsstand",
    "### Steuerpflichtiger, Prüfverantwortung und Bearbeitungsstand",
    "### Anschriftenfeld und Betreff",
    "### Checkliste vor der Anmeldung",
    "### 1. Gegenstand",
    "## 1. Antrag oder Eingabe",
    "\nzwischen\n",
    "\nZwischen\n",
    "\nAn das\n",
    "\nAn die\n",
    "\nAn den\n",
    "\nAn die:\n",
    "\n**An das**\n",
    "\n**An die**\n",
    "\n**An den ",
    "\n**An die ",
    "\n**An das ",
    "**zwischen**",
    "| zwischen | between |",
    "| **zwischen** | **between** |",
    "wird geschlossen zwischen",
    "wird vereinbart zwischen",
    "wird folgende Betriebsvereinbarung geschlossen",
    "gemeinsam die „Parteien",
    "gemeinsam: **„Parteien",
    "Vor mir,",
    "Verhandelt zu",
    "Sehr geehrte Damen und Herren,",
    "Sehr geehrte/r",
    "**REMONSTRATION**",
]

SCHLUSS_MARKER = [
    "### Schluss,",
    "### 20. Beurkundungsabschluss",
    "Unterschriften:",
    "\n[Unterschrift]\n",
    "[Unterschrift",
    "Mit freundlichen Grüßen",
    "_____________________________",
]

WORTDOPPLUNG_RE = re.compile(r"(?i)\b([A-Za-zÄÖÜäöüß]{3,})[ \t]+\1\b")
ABKUERZUNGS_DOPPLUNG_RE = re.compile(
    r"(?:\b(?:Az\.|Nr\.|Abs\.|Art\.|UR-Nr\.)\s+(?:Az\.|Nr\.|Nummer|Abs\.|Art\.)\b"
    r"|\b(?:IBAN IBAN|ISIN ISIN|BIC BIC|EUR EUR)\b)"
)
LEERE_ALTERNATIVE_RE = re.compile(r"\[\s*/|/\s*\]")
KAPUTTE_FETTSCHRIFT_RE = re.compile(r"\*\*\*[^*\n]+\*\*(?!\*)")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
UNTERSCHRIFTSLINIE_RE = re.compile(r"_{20,}")
ADRESSATENZEILE_RE = re.compile(
    r"(?im)^(?:\*\*)?(?:an\s+(?:das|die|den)\s+)?"
    r"(?:\[[^\]\n]*(?:gericht|behörde|amt|kammer|verband)[^\]\n]*\]"
    r"|(?:amts|land|oberlandes|arbeits|sozial|verwaltungs|finanz|bundesfinanz|"
    r"bundesarbeits|bundessozial|bundesverwaltungs|bundesverfassungs)gericht[^\n]*"
    r"|finanzamt[^\n]*|staatsanwaltschaft[^\n]*|vergabekammer[^\n]*"
    r"|bundeskartellamt[^\n]*|bundesamt[^\n]*|[^\n]*rechtsausschuss[^\n]*)"
    r"(?:\*\*)?$"
)
DOPPELTER_TRENNER_RE = re.compile(r"(?m)^---[ \t]*\n(?:[ \t]*\n)*---[ \t]*$")
UEBERMAESSIGE_LEERZEILEN_RE = re.compile(r"\n(?:[ \t]*\n){3,}")
HTML_ABSTAND_RE = re.compile(r"&(?:emsp|nbsp);|<br\s*/?>", re.IGNORECASE)
WORTDOPPLUNG_AUSNAHMEN = {
    "die", "der", "das", "dem", "den", "ein", "eine", "einer", "eines", "einem",
    "und", "von", "zur", "zum", "für", "mit", "bei", "auf", "ist", "sind", "hat",
    "haben", "des", "sie",
}


def zeilen_mit_verschachtelten_platzhaltern(text: str) -> list[int]:
    """Ermittelt Zeilen, in denen ein eckiger Platzhalter einen weiteren enthält."""
    fundstellen: list[int] = []
    for zeilennummer, zeile in enumerate(text.splitlines(), start=1):
        tiefe = 0
        for zeichen in zeile:
            if zeichen == "[":
                tiefe += 1
                if tiefe > 1:
                    fundstellen.append(zeilennummer)
                    break
            elif zeichen == "]" and tiefe:
                tiefe -= 1
    return fundstellen


def inhaltswort_dopplungen(text: str) -> list[tuple[int, str]]:
    """Findet versehentlich doppelt gesetzte Inhaltswörter innerhalb einer Zeile."""
    fundstellen: list[tuple[int, str]] = []
    for zeilennummer, zeile in enumerate(text.splitlines(), start=1):
        for treffer in WORTDOPPLUNG_RE.finditer(zeile):
            wort = treffer.group(1)
            if wort.lower() not in WORTDOPPLUNG_AUSNAHMEN:
                fundstellen.append((zeilennummer, wort))
    return fundstellen


def markdown_tabellenfehler(text: str) -> list[tuple[int, str]]:
    """Prüft Tabellen auf verschobene Abschlussklammern und wechselnde Spaltenzahlen."""
    fehler: list[tuple[int, str]] = []
    erwartete_trenner: int | None = None
    for zeilennummer, zeile in enumerate(text.splitlines(), start=1):
        stripped = zeile.strip()
        if stripped.startswith("|") and stripped.endswith("|]"):
            fehler.append((zeilennummer, "Platzhalter umspannt Tabellenzellen"))
            erwartete_trenner = None
            continue
        if not (stripped.startswith("|") and stripped.endswith("|")):
            erwartete_trenner = None
            continue
        trenner = 0
        maskiert = False
        code = False
        for zeichen in stripped:
            if maskiert:
                maskiert = False
            elif zeichen == "\\":
                maskiert = True
            elif zeichen == "`":
                code = not code
            elif zeichen == "|" and not code:
                trenner += 1
        if erwartete_trenner is None:
            erwartete_trenner = trenner
        elif trenner != erwartete_trenner:
            fehler.append(
                (zeilennummer, f"Tabellenbreite {trenner - 1} statt {erwartete_trenner - 1} Spalten")
            )
    return fehler


def syntaxartefakte(text: str) -> list[tuple[int, str]]:
    """Findet bekannte Platzhalter- und Markdown-Artefakte aus früheren Importen."""
    fundstellen: list[tuple[int, str]] = []
    for zeilennummer, zeile in enumerate(text.splitlines(), start=1):
        if ABKUERZUNGS_DOPPLUNG_RE.search(zeile):
            fundstellen.append((zeilennummer, "verdoppelte Abkürzung"))
        if LEERE_ALTERNATIVE_RE.search(zeile):
            fundstellen.append((zeilennummer, "leere Alternative"))
        if KAPUTTE_FETTSCHRIFT_RE.search(zeile):
            fundstellen.append((zeilennummer, "unausgeglichener Fettschriftmarker"))
        if HTML_ABSTAND_RE.search(zeile):
            fundstellen.append((zeilennummer, "rendererabhängiger HTML-Abstand"))
    for treffer in DOPPELTER_TRENNER_RE.finditer(text):
        fundstellen.append((text[:treffer.start()].count("\n") + 1, "doppelte Markdown-Trennlinie"))
    for treffer in UEBERMAESSIGE_LEERZEILEN_RE.finditer(text):
        fundstellen.append((text[:treffer.start()].count("\n") + 1, "mehr als zwei Leerzeilen"))
    return fundstellen


def rubric_typ(vorlage_dir: Path) -> str | None:
    """Liest den einfachen typ-Wert der Baseline-Rubric ohne YAML-Abhängigkeit."""
    rubric = vorlage_dir / "rubric.yaml"
    if not rubric.is_file():
        return None
    for zeile in rubric.read_text(encoding="utf-8").splitlines():
        if zeile.startswith("typ:"):
            return zeile.split(":", 1)[1].strip().strip('"\'')
    return None


def warnhinweis_typfehler(text: str, typ: str | None) -> str | None:
    """Findet offenkundige Vertrag-/Schriftsatz-Verwechslungen im Kopfbereich."""
    kopfbereich = "\n".join(text.splitlines()[:40])
    if typ == "vertrag" and (
        "nicht Schriftsatzbestandteil" in kopfbereich
        or "noch keinen Schriftsatz" in kopfbereich
    ):
        return "Vertragsvorlage bezeichnet den Warnhinweis oder Entwurf als Schriftsatz"
    if typ == "schriftsatz" and (
        "nicht Vertragsbestandteil" in kopfbereich
        or "noch keinen Vertrag" in kopfbereich
    ):
        return "Schriftsatzvorlage bezeichnet den Warnhinweis oder Entwurf als Vertrag"
    return None


def generik_altbausteine(text: str) -> list[str]:
    """Findet ausschließlich bekannte, vollständig generische Altbausteine."""
    return [
        bezeichnung
        for bezeichnung, baustein in VERBOTENE_GENERIK_BAUSTEINE.items()
        if baustein in text
    ]


def hat_rubrum_oder_adressat(text: str) -> bool:
    """Erkennt ausdrücklich bezeichnete Adressaten ohne ein Universalrubrum zu verlangen."""
    kopf = "\n".join(text.splitlines()[:120])
    return (
        any(marker in text for marker in RUBRUM_MARKER)
        or ADRESSATENZEILE_RE.search(kopf) is not None
        or "Einreichung zum zentralen Schutzschriftenregister" in kopf
        or "### Variante A: Plädoyer-/Antragsbaustein" in kopf
    )


def markdown_anker(text: str) -> set[str]:
    """Ermittelt explizite IDs und GitHub-kompatible Überschriftenanker."""
    anker = set(re.findall(r'<a\s+(?:[^>]*?\s)?id=["\']([^"\']+)["\']', text, re.I))
    zaehler: dict[str, int] = {}
    for zeile in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", zeile)
        if match is None:
            continue
        titel = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", match.group(1))
        titel = re.sub(r"<[^>]+>", "", titel)
        titel = re.sub(r"[`*_~]", "", titel).casefold()
        basis = re.sub(r"[^\w\- ]", "", titel, flags=re.UNICODE).replace(" ", "-")
        if not basis:
            continue
        nummer = zaehler.get(basis, 0)
        anker.add(basis if nummer == 0 else f"{basis}-{nummer}")
        zaehler[basis] = nummer + 1
    return anker


def exakte_repo_pfade() -> dict[str, str]:
    """Inventarisiert Linkziele einmalig, ohne in Git- oder Builddaten abzusteigen."""
    ergebnis: dict[str, str] = {"": ""}
    for wurzel, ordner, dateien in os.walk(REPO):
        ordner[:] = [name for name in ordner if name not in {".git", "runs", "dist"}]
        basis = Path(wurzel)
        for name in [*ordner, *dateien]:
            relativ = (basis / name).relative_to(REPO).as_posix()
            ergebnis[unicodedata.normalize("NFC", relativ).casefold()] = relativ
    return ergebnis


def markdown_linkziel(rohes_ziel: str) -> str:
    """Trennt ein Linkziel von einem optionalen Markdown-Titel."""
    ziel = rohes_ziel.strip()
    if ziel.startswith("<"):
        ende = ziel.find(">")
        if ende >= 0:
            return ziel[1:ende]
    return ziel.split(maxsplit=1)[0].strip("<>") if ziel else ""


def relative_linkfehler() -> list[str]:
    """Prüft Ziel, exakte Schreibweise und Fragmente relativer Markdown-Links."""
    fehler: list[str] = []
    anker_cache: dict[Path, set[str]] = {}
    ziel_cache: dict[str, tuple[Path, bool]] = {}
    repo_basis = REPO.absolute()
    repo_aufgeloest = repo_basis.resolve()
    exakte_pfade = exakte_repo_pfade()
    for datei in REPO.rglob("*.md"):
        if any(teil in {".git", "runs", "dist"} for teil in datei.parts):
            continue
        text = datei.read_text(encoding="utf-8")
        for ziel in MARKDOWN_LINK_RE.findall(text):
            ziel = markdown_linkziel(ziel)
            if not ziel or ziel.startswith(("http://", "https://", "mailto:")):
                continue
            pfadtext, _, fragment = ziel.partition("#")
            pfadtext = unquote(pfadtext.split("?", 1)[0])
            fragment = unquote(fragment)
            pfad = datei if not pfadtext else Path(
                os.path.normpath(str(datei.parent / pfadtext))
            )
            try:
                relativ = pfad.relative_to(repo_basis)
            except ValueError:
                fehler.append(f"{datei.relative_to(REPO)} -> {ziel} (verlässt das Repository)")
                continue
            relativtext = "" if not relativ.parts else relativ.as_posix()
            schluessel = unicodedata.normalize("NFC", relativtext).casefold()
            exakter_relativtext = exakte_pfade.get(schluessel)
            if exakter_relativtext is None:
                fehler.append(f"{datei.relative_to(REPO)} -> {ziel}")
                continue
            if exakter_relativtext != relativtext:
                fehler.append(
                    f"{datei.relative_to(REPO)} -> {ziel} "
                    "(Groß-/Kleinschreibung des Zielpfads stimmt nicht)"
                )
                continue
            if exakter_relativtext not in ziel_cache:
                exakter_pfad = (
                    repo_basis
                    if not exakter_relativtext
                    else repo_basis / exakter_relativtext
                )
                aufgeloest = exakter_pfad.resolve()
                try:
                    aufgeloest.relative_to(repo_aufgeloest)
                    gueltig = exakter_pfad.exists()
                except ValueError:
                    gueltig = False
                ziel_cache[exakter_relativtext] = (exakter_pfad, gueltig)
            pfad, gueltig = ziel_cache[exakter_relativtext]
            if not gueltig:
                fehler.append(f"{datei.relative_to(REPO)} -> {ziel} (ungültiges Linkziel)")
                continue
            ankedatei = pfad / "README.md" if pfad.is_dir() else pfad
            if fragment and ankedatei.suffix.lower() == ".md":
                if ankedatei not in anker_cache:
                    anker_cache[ankedatei] = markdown_anker(
                        ankedatei.read_text(encoding="utf-8")
                    )
                if fragment not in anker_cache[ankedatei]:
                    fehler.append(
                        f"{datei.relative_to(REPO)} -> {ziel} "
                        "(Markdown-Anker fehlt)"
                    )
    return fehler


def main() -> int:
    errors: list[str] = []

    try:
        pruefe_bestandsstruktur(REPO)
    except RuntimeError as exc:
        errors.append(str(exc))

    vorhandene = {p.name for p in REPO.iterdir() if p.is_dir() and not p.name.startswith(".")}
    fehlend = ERWARTETE_THEMEN - vorhandene
    if fehlend:
        errors.append(f"fehlende Themenordner: {sorted(fehlend)}")

    root_readme = REPO / "README.md"
    if not root_readme.is_file():
        errors.append("README.md fehlt")
        root_readme_text = ""
    else:
        root_readme_text = root_readme.read_text(encoding="utf-8")

    if "](DOWNLOADS.md)" not in root_readme_text:
        errors.append("README.md verlinkt DOWNLOADS.md nicht")
    for asset in (
        "vorlagensammlung-recht-odt.zip",
        "vorlagensammlung-recht-markdown.zip",
        "vorlagen-gerichtsleitend-markdown.zip",
        "SHA256SUMS.txt",
    ):
        if f"raw/main/docs/experimentell/vorlagensammlung-recht/dist/{asset}" not in root_readme_text:
            errors.append(f"README.md ohne Komplettpaket-Link {asset}")

    index_pruefung = subprocess.run(
        [sys.executable, "scripts/build-download-index.py", "--check"],
        cwd=REPO,
        text=True,
        capture_output=True,
        check=False,
    )
    if index_pruefung.returncode != 0:
        details = (index_pruefung.stdout + index_pruefung.stderr).strip()
        errors.append(f"DOWNLOADS.md ist nicht aktuell: {details}")

    md_count = 0
    for thema in sorted(ERWARTETE_THEMEN & vorhandene):
        tdir = REPO / thema
        thema_readme = tdir / "README.md"
        if not thema_readme.is_file():
            errors.append(f"{thema}/README.md fehlt")
            thema_readme_text = ""
        else:
            thema_readme_text = thema_readme.read_text(encoding="utf-8")
            thema_tabellenfehler = markdown_tabellenfehler(thema_readme_text)
            if thema_tabellenfehler:
                errors.append(f"{thema}/README.md: beschädigte Tabelle {thema_tabellenfehler}")
            bereichsdownload = f"](../DOWNLOADS.md#haupt-{thema})"
            if bereichsdownload not in thema_readme_text:
                errors.append(
                    f"{thema}/README.md verlinkt den bereichsspezifischen Downloadindex nicht"
                )
        if f"]({thema}/)" not in root_readme_text:
            errors.append(f"README.md verlinkt den Themenordner {thema}/ nicht")
        for vorlage_dir in sorted(p for p in tdir.iterdir() if p.is_dir()):
            md = _md_in(vorlage_dir)
            odt = _odt_in(vorlage_dir)
            readme = vorlage_dir / "README.md"
            if md is None or not md.is_file():
                errors.append(f"{vorlage_dir.relative_to(REPO)}: keine Vorlagen-Markdown-Datei gefunden")
                continue
            md_count += 1
            vorlagen_link_anzahl = thema_readme_text.count(f"]({vorlage_dir.name}/)")
            if vorlagen_link_anzahl != 1:
                errors.append(
                    f"{thema}/README.md muss die Vorlage {vorlage_dir.name}/ genau einmal "
                    f"verlinken (gefunden: {vorlagen_link_anzahl})"
                )
            if odt is None or not odt.is_file():
                errors.append(f"{vorlage_dir.relative_to(REPO)}: keine gleichnamige ODT-Datei gefunden (aus MD erzeugen)")
            expected_stem = vorlage_dir.name
            if md.stem != expected_stem:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: Markdown-Dateiname muss {expected_stem}.md heißen, nicht {md.name}"
                )
            if ist_generischer_stem(md.stem):
                errors.append(f"{vorlage_dir.relative_to(REPO)}: generischer Markdown-Dateiname verboten: {md.name}")
            if odt is not None:
                if odt.stem != md.stem:
                    errors.append(f"{vorlage_dir.relative_to(REPO)}: ODT-Dateiname passt nicht zur Markdown-Datei: {odt.name}")
                if ist_generischer_stem(odt.stem):
                    errors.append(f"{vorlage_dir.relative_to(REPO)}: generischer ODT-Dateiname verboten: {odt.name}")
            if not readme.is_file():
                errors.append(f"{vorlage_dir.relative_to(REPO)}: README.md fehlt")
                readme_text = ""
            else:
                readme_text = readme.read_text(encoding="utf-8")
                missing_readme_tokens = [tok for tok in README_PFLICHT_TOKENS if tok not in readme_text]
                if missing_readme_tokens:
                    errors.append(
                        f"{vorlage_dir.relative_to(REPO)}: README.md ohne Pflicht-Token {missing_readme_tokens}"
                    )
                readme_dopplungen = inhaltswort_dopplungen(readme_text)
                if readme_dopplungen:
                    errors.append(
                        f"{vorlage_dir.relative_to(REPO)}: README.md enthält verdoppelte "
                        f"Inhaltswörter {readme_dopplungen}"
                    )
                readme_tabellenfehler = markdown_tabellenfehler(readme_text)
                if readme_tabellenfehler:
                    errors.append(
                        f"{vorlage_dir.relative_to(REPO)}: README.md enthält beschädigte "
                        f"Tabellen {readme_tabellenfehler}"
                    )
                readme_syntaxartefakte = syntaxartefakte(readme_text)
                if readme_syntaxartefakte:
                    errors.append(
                        f"{vorlage_dir.relative_to(REPO)}: README.md enthält Syntaxartefakte "
                        f"{readme_syntaxartefakte}"
                    )
                rel = vorlage_dir.relative_to(REPO).as_posix()
                md_zip_link = (
                    "https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/"
                    f"{rel}/{md.name}.zip"
                )
                if md_zip_link not in readme_text:
                    errors.append(
                        f"{vorlage_dir.relative_to(REPO)}: README.md ohne Markdown-ZIP-Direktdownload"
                    )
                if f"]({md.name})" not in readme_text:
                    errors.append(
                        f"{vorlage_dir.relative_to(REPO)}: README.md ohne lokale Markdown-Vorschau"
                    )
                if odt is not None:
                    odt_link = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/{rel}/{odt.name}"
                    if odt_link not in readme_text:
                        errors.append(f"{vorlage_dir.relative_to(REPO)}: README.md ohne ODT-Direktdownload")
                    if f"]({odt.name})" not in readme_text:
                        errors.append(
                            f"{vorlage_dir.relative_to(REPO)}: README.md ohne lokale ODT-Vorschau"
                        )
            text = md.read_text(encoding="utf-8")
            warnhinweis_fehler = warnhinweis_typfehler(text, rubric_typ(vorlage_dir))
            if warnhinweis_fehler:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: {md.name}: {warnhinweis_fehler}"
                )
            template_dopplungen = inhaltswort_dopplungen(text)
            if template_dopplungen:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: {md.name} enthält verdoppelte "
                    f"Inhaltswörter {template_dopplungen}"
                )
            template_tabellenfehler = markdown_tabellenfehler(text)
            if template_tabellenfehler:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: {md.name} enthält beschädigte "
                    f"Tabellen {template_tabellenfehler}"
                )
            template_syntaxartefakte = syntaxartefakte(text)
            if template_syntaxartefakte:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: {md.name} enthält Syntaxartefakte "
                    f"{template_syntaxartefakte}"
                )
            verschachtelte_platzhalter = zeilen_mit_verschachtelten_platzhaltern(text)
            if verschachtelte_platzhalter:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: {md.name} enthält verschachtelte "
                    f"Platzhalter in Zeile {verschachtelte_platzhalter}"
                )
            verbotene = [heading for heading in VERBOTENE_TEMPLATE_ABSCHNITTE if heading in text]
            if verbotene:
                errors.append(f"{vorlage_dir.relative_to(REPO)}: {md.name} enthält lange Hinweisabschnitte {verbotene}")
            generik = generik_altbausteine(text)
            if generik:
                errors.append(
                    f"{vorlage_dir.relative_to(REPO)}: {md.name} enthält generische "
                    f"Altbausteine {generik}"
                )
            missing = [tok for tok in PFLICHT_TOKENS if tok not in text]
            if missing:
                errors.append(f"{vorlage_dir.relative_to(REPO)}: {md.name} ohne Pflicht-Token {missing}")
            if not hat_rubrum_oder_adressat(text):
                errors.append(f"{vorlage_dir.relative_to(REPO)}: {md.name} ohne Rubrum-/Adressatenkopf")
            if not any(marker in text for marker in SCHLUSS_MARKER) and not UNTERSCHRIFTSLINIE_RE.search(text):
                errors.append(f"{vorlage_dir.relative_to(REPO)}: {md.name} ohne Schluss-/Unterzeichnungsblock")

    tote_links = relative_linkfehler()
    if tote_links:
        errors.append(f"relative Markdown-Links ohne Ziel: {tote_links}")

    if errors:
        print("validate-vorlagen: FEHLER")
        for e in errors:
            print(" -", e)
        return 1
    print(f"validate-vorlagen OK ({md_count} Vorlagen, {len(ERWARTETE_THEMEN)} Themenordner)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
