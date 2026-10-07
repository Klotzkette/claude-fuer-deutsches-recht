"""Eigenschaftstests fuer scripts/hausstil.py und die beiden Kommandozeilen.

Vertrag (vom Auftraggeber am 07.10.2026 bestaetigt, hier woertlich):

V1 Einzige Quelle: Der neutrale Standard steht nur in hausstil.json. Jeder andere Text im
   Repo, der eine Schrift nennt, tut das in der daraus erzeugten kanonischen Formulierung
   oder an einer eingetragenen Ausnahme.
V2 Kanzleivorrang: Die kanonische Formulierung sagt, dass das Kanzleiprofil Vorrang hat und
   der Standard nur ohne Profil gilt.
V3 Idempotenz: Nochmaliges Anwenden auf einen bereits angewendeten Stand aendert keine Datei.
V4 Quelle schlaegt durch: Nach Aenderung des Standards in hausstil.json und erneutem Anwenden
   nennt kein Text ausserhalb der Ausnahmen mehr den alten Schriftnamen.
V5 Nur die Schriftangabe wird ersetzt: Alles ausserhalb der Schriftangabe bleibt zeichengleich
   erhalten, JSON-Dateien bleiben gueltig.
V6 Ausnahmen explizit und wirksam: Dateien unter Ausnahmepfaden werden weder veraendert noch
   beanstandet. Nicht eingetragene Schriftnamen meldet der Validator mit Datei und Zeile und
   Fehlerstatus, auch in abweichender Schreibweise.
V7 Repo kennt Raleway nicht: Raleway steht nur im Kanzleiprofil ausserhalb des Repos; ein
   "Raleway" im Repo laesst den Validator fehlschlagen.
V12 (vom Auftraggeber am 07.10.2026 bestaetigt) Schnellstart- und
   Hauptproblem-Prompts (*-schnellstart.md, *-hauptproblem.md und ihre byteidentischen TXT-Kopien)
   tragen statt der langen Phrase die Kurzform "Kanzleihausschrift" ohne Schriftnamen, weil sie eine
   Bytegrenze von 7500 Bytes haben; die lange Form steht in Werkstatt-Prompts, Skills und References.
   Auch die Kurzform laesst den Validator schweigen.

Spezifikation vor dem ersten Lauf: Schriftangaben ohne Groesse ("Times New Roman oder Arial")
werden nicht ersetzt, sondern gemeldet (Docstring von ersetze_schriftangaben). V4 wird deshalb
auf Dokumenten ohne solche Angaben und ohne Fremdvorgaben geprueft; V6 prueft, dass genau diese
Zeilen gemeldet werden. Ebenso vor dem Lauf festgelegt (Nachbesserung nach Code-Review am
07.10.2026, Vertrag unveraendert): Name und Groesse muessen auf einer Zeile stehen, eine ueber
den Zeilenumbruch verteilte Angabe gilt als Angabe ohne Groesse (V5: Zeilenzahl bleibt); eine
Phrase mit Betonung im Inneren ("ohne Profil **Arial 11 pt**") ist keine kanonische Phrase, wird
nicht noch einmal ersetzt und vom Validator gemeldet; eine Datei, die kein UTF-8 ist, wird von
apply gemeldet und uebersprungen, der Validator liest sie trotzdem; Zeilenenden (CRLF) bleiben.

Als gleichwertig begruendete Mutanten (mutmut 3, Lauf vom 07.10.2026): encoding "utf-8" gegen "UTF-8"
oder None beim Lesen und Dekodieren (Codec-Alias; None nimmt die Systemlocale, die hier UTF-8 ist und
im Test nicht umgeschaltet wird) sowie der Fuelltext in finde_verstoesse, mit dem Phrase und
Fremdvorgaben ueberdeckt werden: jeder Fuelltext ohne Zeilenumbruch und ohne Schriftnamen verhaelt
sich gleich, weil nur Zeilennummern und Schriftnamen zaehlen. Die Kommandozeilen apply-hausstil.py,
audit-hausstil.py und inject-ausformulierungspflicht.py tragen Bindestriche im Dateinamen und werden
hier ueber importlib geladen; mutmut kann ihnen keine Tests zuordnen und meldet ihre Mutanten als
"no tests". Sie haben keinen gemessenen Mutationswert, nur die Zeilenabdeckung der Dateitests.
"""
from __future__ import annotations

import fnmatch
import importlib.util
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, replace
from pathlib import Path

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

SKRIPTE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKRIPTE.parent))
from scripts import hausstil as hs  # noqa: E402

# Die Kommandozeilen importieren "hausstil" ueber ihren eigenen Ordner. Damit sie dasselbe
# Modulobjekt sehen wie dieser Test (wichtig fuer die Mutationsmessung), wird es hier eingetragen.
sys.modules["hausstil"] = hs

settings.register_profile("standard", max_examples=150, deadline=None)
settings.register_profile(
    "mutmut", max_examples=150, deadline=None, suppress_health_check=[HealthCheck.differing_executors]
)
settings.load_profile(os.environ.get("HYPOTHESIS_PROFILE", "standard"))


def lade_kommandozeile(dateiname: str):
    spec = importlib.util.spec_from_file_location(dateiname.replace("-", "_").replace(".py", ""), SKRIPTE / dateiname)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


NAMEN = ("Times New Roman", "Raleway", "Garamond", "Arial", "Noto Sans", "Noto Sans Mono")
FREMDVORGABEN = ("Times New Roman 11/12 pt", "arial-sonderfall")
AUSNAHMEN = ("scripts/", "quality/source-audits/", "CHANGELOG.md", "*/werkzeuge/*")
STIL_A = hs.Hausstil(
    schrift="Times New Roman", groesse="11 pt", gliederung="dezimal",
    bekannte_schriftnamen=NAMEN, fremdvorgaben=FREMDVORGABEN, ausnahmepfade=AUSNAHMEN,
)
STIL_B = replace(STIL_A, schrift="Garamond", groesse="12 pt")

WOERTER = ["Vertrag", "Mandantin", "Klage", "Frist", "Gliederung", "Export", "Dokument", "soweit",
           "technisch", "möglich", "und", "in", "mit", "dezimale", "ausschließlich", "Sätze", "Hinweis"]


@dataclass(frozen=True)
class Segment:
    text: str
    art: str  # prosa, frei, kanonisch, fremd, nackt


@st.composite
def groessenangabe(draw) -> str:
    zahl = draw(st.integers(min_value=9, max_value=14))
    einheit = draw(st.sampled_from(["pt", "Punkt"]))
    leerzeichen = draw(st.sampled_from([" ", ""]))
    return f"{zahl}{leerzeichen}{einheit}"


@st.composite
def prosa(draw) -> Segment:
    return Segment(" ".join(draw(st.lists(st.sampled_from(WOERTER), min_size=1, max_size=6))), "prosa")


@st.composite
def freie_angabe(draw) -> Segment:
    name = draw(st.sampled_from(NAMEN))
    verbinder = draw(st.sampled_from([" ", ", ", " in ", " mit ", ", Schriftgröße ", " Schriftgröße "]))
    kern = f"{name}{verbinder}{draw(groessenangabe())}"
    if draw(st.booleans()):
        kern = f"**{kern}**"
    if draw(st.booleans()):
        kern = "in " + kern
    return Segment(kern, "frei")


@st.composite
def kanonisch(draw) -> Segment:
    name = draw(st.sampled_from(NAMEN))
    kern = f"{hs.PHRASE_ANFANG}{name} {draw(groessenangabe())}"
    if draw(st.booleans()):
        kern = "in der " + kern
    return Segment(kern, "kanonisch")


def fremdvorgabe() -> st.SearchStrategy[Segment]:
    return st.sampled_from(FREMDVORGABEN).map(lambda text: Segment(text, "fremd"))


def schreibweise_variieren(name: str, variante: str) -> str:
    if variante == "klein":
        return name.lower()
    if variante == "gross":
        return name.upper()
    if variante == "ohne-leerzeichen":
        return name.replace(" ", "")
    if variante == "bindestrich":
        return name.replace(" ", "-")
    if variante == "unterstrich":
        return name.replace(" ", "_")
    return name


@st.composite
def nackte_nennung(draw) -> Segment:
    """Schriftname ohne Groesse, auch in abweichender Schreibweise (V6)."""
    name = schreibweise_variieren(draw(st.sampled_from(NAMEN)), draw(st.sampled_from(
        ["original", "klein", "gross", "ohne-leerzeichen", "bindestrich", "unterstrich"])))
    form = draw(st.sampled_from(["{}", "{} oder Arial", "Schriftart {}", "({})"]))
    return Segment(form.format(name), "nackt")


@st.composite
def phrase_mit_betonung_innen(draw) -> Segment:
    """Keine kanonische Phrase: die Betonung steht hinter "ohne Profil". Fuer apply unantastbar,
    fuer den Validator eine nackte Nennung."""
    name = draw(st.sampled_from(NAMEN))
    sterne = draw(st.sampled_from(["*", "**"]))
    return Segment(f"{hs.PHRASE_ANFANG}{sterne}{name} {draw(groessenangabe())}{sterne}", "nackt")


ALLE_SEGMENTE = st.one_of(prosa(), freie_angabe(), kanonisch(), fremdvorgabe(), nackte_nennung(),
                          phrase_mit_betonung_innen())
NUR_ERSETZBARE_SEGMENTE = st.one_of(prosa(), freie_angabe(), kanonisch())


@st.composite
def dokument(draw, segmente=ALLE_SEGMENTE) -> list[list[Segment]]:
    """Zeilen aus Segmenten; die Zeilenstruktur bleibt erhalten, damit Zeilennummern pruefbar sind."""
    return draw(st.lists(st.lists(segmente, min_size=1, max_size=4), min_size=1, max_size=6))


def als_text(zeilen: list[list[Segment]]) -> str:
    return "\n".join(" ".join(segment.text for segment in zeile) for zeile in zeilen)


NAMEN_ALTERNATION = "|".join(re.escape(name) for name in sorted(NAMEN, key=len, reverse=True))
ANGABE = (
    r"(?:" + re.escape(hs.PHRASE_ANFANG) + r"(?:" + NAMEN_ALTERNATION + r") \d{1,2} ?(?:pt|Punkt)\b"
    + r"|(?:" + NAMEN_ALTERNATION + r"),?[ \t]+(?:in |mit )?(?:Schriftgröße )?\d{1,2} ?(?:pt|Punkt)\b)"
)
SCHRIFTANGABE = re.compile(ANGABE)
# Das "in" vor einer Angabe gehoert zur Angabe (V5: es darf zu "in der" werden), auch wenn eine
# Markdown-Betonung dazwischensteht. Die Sternchen selbst bleiben im Text und muessen erhalten bleiben.
IN_VOR_ANGABE = re.compile(r"\bin (?:der )?(?=\*{0,2}" + ANGABE + r")")


def ohne_schriftangaben(text: str) -> str:
    """Erhaltungssatz: der Text ohne jede Schriftangabe mit Groesse und ohne das "in" davor."""
    return SCHRIFTANGABE.sub("", IN_VOR_ANGABE.sub("", text))


# --- V2 -------------------------------------------------------------------------------------

@given(schrift=st.text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ", min_size=1).filter(str.strip),
       groesse=st.integers(min_value=6, max_value=20))
def test_v2_phrase_nennt_kanzleiprofil_vorrang_und_standard(schrift, groesse):
    """Contract: V2"""
    stil = replace(STIL_A, schrift=schrift, groesse=f"{groesse} pt")
    phrase = hs.kanonische_phrase(stil)
    assert phrase.startswith("Hausschrift laut Kanzleiprofil, ohne Profil ")
    assert phrase.endswith(f"{schrift} {groesse} pt")
    assert hs.formatsatz(stil) == phrase + ", ausschließlich dezimale Gliederung"


# --- V3 -------------------------------------------------------------------------------------

@given(zeilen=dokument())
def test_v3_zweites_anwenden_aendert_nichts(zeilen):
    """Contract: V3"""
    einmal = hs.ersetze_schriftangaben(als_text(zeilen), STIL_A)
    zweimal = hs.ersetze_schriftangaben(einmal, STIL_A)
    assert zweimal == einmal


# --- V4 -------------------------------------------------------------------------------------

@given(zeilen=dokument(NUR_ERSETZBARE_SEGMENTE))
def test_v4_neuer_standard_verdraengt_alten_schriftnamen(zeilen):
    """Contract: V4"""
    mit_a = hs.ersetze_schriftangaben(als_text(zeilen), STIL_A)
    mit_b = hs.ersetze_schriftangaben(mit_a, STIL_B)
    assert hs.finde_verstoesse(mit_b, STIL_B) == []
    assert "Times New Roman" not in mit_b
    assert ("Garamond" in mit_b) == any(segment.art != "prosa" for zeile in zeilen for segment in zeile)


# --- V5 -------------------------------------------------------------------------------------

@given(zeilen=dokument())
def test_v5_alles_ausser_schriftangaben_bleibt_zeichengleich(zeilen):
    """Contract: V5 (Erhaltungssatz, gilt ueber alle Zweige)"""
    vorher = als_text(zeilen)
    nachher = hs.ersetze_schriftangaben(vorher, STIL_A)
    assert ohne_schriftangaben(nachher) == ohne_schriftangaben(vorher)
    assert nachher.count("\n") == vorher.count("\n")


@given(zeilen=dokument(), ascii_sicher=st.booleans())
def test_v5_json_bleibt_gueltig_und_traegt_denselben_text(zeilen, ascii_sicher):
    """Contract: V5"""
    text = als_text(zeilen)
    rohdatei = json.dumps({"rubrik": text}, ensure_ascii=ascii_sicher)
    ersetzt = hs.ersetze_schriftangaben(rohdatei, STIL_A)
    geladen = json.loads(ersetzt)
    assert geladen["rubrik"] == hs.ersetze_schriftangaben(text, STIL_A)
    nackt_vorhanden = any(segment.art == "nackt" for zeile in zeilen for segment in zeile)
    assert bool(hs.finde_verstoesse(ersetzt, STIL_A)) == nackt_vorhanden


@given(zeilen=dokument(), stelle=st.integers(min_value=0, max_value=10_000))
def test_v5_in_vor_schriftangabe_wird_in_der(zeilen, stelle):
    """Contract: V5 (die Angabe selbst darf 'in' zu 'in der' machen, sonst nichts)"""
    text = als_text(zeilen)
    nachher = hs.ersetze_schriftangaben(text, STIL_A)
    phrase = hs.kanonische_phrase(STIL_A)
    treffer = [m.start() for m in re.finditer(re.escape(phrase), nachher)]
    if not treffer:
        return
    position = treffer[stelle % len(treffer)]
    davor = nachher[max(0, position - 7):position].rstrip("*")
    assert not davor.endswith(" in "), "ein nacktes 'in' vor der Phrase darf nicht stehen bleiben, auch nicht vor '**'"


@given(zeilen=dokument())
def test_v5_jede_freie_angabe_wird_genau_eine_phrase(zeilen):
    """Contract: V5, V3 (eine Angabe hinter "ohne Profil" ist Teil einer Phrase und wird nicht verdoppelt)"""
    vorher = als_text(zeilen)
    nachher = hs.ersetze_schriftangaben(vorher, STIL_A)
    phrase = hs.kanonische_phrase(STIL_A)
    freie = sum(segment.art == "frei" for zeile in zeilen for segment in zeile)
    kanonische = sum(segment.art == "kanonisch" for zeile in zeilen for segment in zeile)
    assert nachher.count(phrase) == freie + kanonische
    assert nachher.count(hs.PHRASE_ANFANG) == vorher.count(hs.PHRASE_ANFANG) + freie


@given(name=st.sampled_from(NAMEN), groesse=groessenangabe(), komma=st.booleans(), davor=prosa(), danach=prosa())
def test_v5_umbruch_zwischen_name_und_groesse_bleibt(name, groesse, komma, davor, danach):
    """Contract: V5 (Zeilenzahl bleibt: Name und Groesse auf zwei Zeilen werden nicht zusammengezogen),
    V6 (die Namenszeile wird gemeldet)"""
    text = f"{davor.text} {name}{',' if komma else ''}\n{groesse} {danach.text}"
    assert hs.ersetze_schriftangaben(text, STIL_A) == text
    assert [nummer for nummer, _ in hs.finde_verstoesse(text, STIL_A)] == [1]


GEBUNDENE_BUILDER = (
    "generate-formatvorlagen.py", "build-bauwirtschaft-werkstatt-handbuch.py",
    "render-startup-gruender-werkstatt.py", "render-registerwerkstaetten.py",
    "build-ki-verordnung-hochrisiko-pruefer.py",
)


@pytest.mark.parametrize("builder", GEBUNDENE_BUILDER)
def test_v1_gebundene_builder_lesen_den_standard_aus_hausstil_json(builder):
    """Contract: V1 (die DOCX/ODT-Builder ausserhalb der Testakten-Nachbildungen nennen keine Schrift)"""
    quelle = (SKRIPTE / builder).read_text(encoding="utf-8")
    assert "hausstil.lade_hausstil()" in quelle
    assert hs.finde_verstoesse(quelle, hs.lade_hausstil(SKRIPTE.parent / "hausstil.json")) == []


@given(zahl=st.integers(min_value=6, max_value=30), halb=st.booleans())
def test_v1_grundgroesse_kommt_als_zahl_aus_der_quelle(zahl, halb):
    """Contract: V1 (ganze Groessen kommen als int, damit QA-Protokolle 11 und nicht 11.0 aufzeichnen)"""
    ganz = hs.groesse_in_punkt(replace(STIL_A, groesse=f"{zahl} pt"))
    assert ganz == zahl and isinstance(ganz, int)
    assert hs.groesse_in_punkt(replace(STIL_A, groesse=f"{zahl}.5 pt")) == zahl + 0.5
    # Die Fehlermeldung nennt die falsche Einheit, damit der Befund in hausstil.json auffindbar ist.
    with pytest.raises(ValueError, match="px"):
        hs.groesse_in_punkt(replace(STIL_A, groesse=f"{zahl} px"))


# --- V12 ------------------------------------------------------------------------------------

@given(zeilen=dokument())
def test_v12_kurzform_nennt_keine_schrift_und_bleibt_validatorstill(zeilen):
    """Contract: V12"""
    lang = hs.ersetze_schriftangaben(als_text(zeilen), STIL_A)
    kurz = hs.kurzform(lang, STIL_A)
    assert hs.kanonische_phrase(STIL_A) not in kurz
    assert kurz.count("Kanzleihausschrift") == lang.count(hs.kanonische_phrase(STIL_A))
    gemeldete_zeilen = [nummer for nummer, _ in hs.finde_verstoesse(kurz, STIL_A)]
    assert gemeldete_zeilen == [nummer for nummer, _ in hs.finde_verstoesse(lang, STIL_A)]
    assert hs.ersetze_schriftangaben(kurz, STIL_A) == kurz


# --- V6 / V1 --------------------------------------------------------------------------------

@given(zeilen=dokument())
def test_v6_validator_meldet_genau_die_zeilen_mit_nackten_nennungen(zeilen):
    """Contract: V6, V1"""
    text = hs.ersetze_schriftangaben(als_text(zeilen), STIL_A)
    gemeldet = hs.finde_verstoesse(text, STIL_A)
    erwartet = {nummer for nummer, zeile in enumerate(zeilen, start=1) if any(s.art == "nackt" for s in zeile)}
    assert {nummer for nummer, _ in gemeldet} == erwartet
    zeilen_im_text = text.split("\n")
    for nummer, zeilentext in gemeldet:
        assert zeilentext == zeilen_im_text[nummer - 1].strip()


PFADTEILE = st.sampled_from(["a", "skill", "werkzeuge", "tools", "SKILL.md", "x.json", "evals", "scripts"])


@given(ausnahme=st.sampled_from(AUSNAHMEN), rest=st.lists(PFADTEILE, min_size=1, max_size=3))
def test_v6_pfade_unter_ausnahmen_sind_ausgenommen(ausnahme, rest):
    """Contract: V6"""
    suffix = "/".join(rest)
    if ausnahme.endswith("/"):
        assert hs.ist_ausgenommen(ausnahme + suffix, STIL_A)
    elif "*" in ausnahme:
        assert hs.ist_ausgenommen(f"plugin/{suffix}/werkzeuge/{suffix}", STIL_A)
    else:
        assert hs.ist_ausgenommen(ausnahme, STIL_A)


@given(teile=st.lists(PFADTEILE, min_size=1, max_size=4))
def test_v6_andere_pfade_sind_nicht_ausgenommen(teile):
    """Contract: V6"""
    pfad = "/".join(teile)
    muster_trifft = any(
        fnmatch.fnmatchcase(pfad, a) for a in AUSNAHMEN if "*" in a
    )
    praefix_trifft = any(pfad.startswith(a) for a in AUSNAHMEN if a.endswith("/"))
    datei_trifft = pfad in AUSNAHMEN
    assert hs.ist_ausgenommen(pfad, STIL_A) == (muster_trifft or praefix_trifft or datei_trifft)


def test_v6_dateiausnahme_gilt_nur_fuer_genau_diese_datei():
    """Contract: V6"""
    assert hs.ist_ausgenommen("CHANGELOG.md", STIL_A)
    assert not hs.ist_ausgenommen("CHANGELOG.md.bak", STIL_A)
    assert not hs.ist_ausgenommen("scriptsX/a.md", STIL_A)
    assert not hs.ist_ausgenommen("quality/evals/a.json", STIL_A)


# --- V7 -------------------------------------------------------------------------------------

@given(variante=st.sampled_from(["original", "klein", "gross", "bindestrich"]))
def test_v7_raleway_wird_immer_gemeldet(variante):
    """Contract: V7"""
    text = f"Export in {schreibweise_variieren('Raleway', variante)}, 11 pt.\nZweite Zeile."
    assert [nummer for nummer, _ in hs.finde_verstoesse(text, STIL_A)] == [1]


# --- Laden und Kommandozeilen (V1, V6) ------------------------------------------------------

def test_lade_hausstil_liest_alle_felder(tmp_path):
    """Contract: V1"""
    datei = tmp_path / "hausstil.json"
    datei.write_text(json.dumps({
        "standard": {"schrift": "Cambria", "groesse": "10 pt", "gliederung": "dezimal"},
        "bekannte_schriftnamen": ["Cambria", "Raleway"],
        "fremdvorgaben": [{"text": "Cambria 9/10 pt", "grund": "x"}],
        "ausnahmen": [{"grund": "y", "pfade": ["a/", "b.md"]}, {"grund": "z", "pfade": ["*/c/*"]}],
    }), encoding="utf-8")
    stil = hs.lade_hausstil(datei)
    assert stil == hs.Hausstil(
        "Cambria", "10 pt", "dezimal", ("Cambria", "Raleway"), ("Cambria 9/10 pt",), ("a/", "b.md", "*/c/*"))
    assert hs.claude_md_nennt_phrase("Regel: Hausschrift laut Kanzleiprofil, ohne Profil Cambria 10 pt.", stil)
    assert not hs.claude_md_nennt_phrase("Regel: Cambria 10 pt.", stil)


def lege_testrepo_an(wurzel: Path) -> None:
    subprocess.run(["git", "init", "-q", str(wurzel)], check=True)
    (wurzel / "hausstil.json").write_text(json.dumps({
        "standard": {"schrift": "Times New Roman", "groesse": "11 pt", "gliederung": "dezimal"},
        "bekannte_schriftnamen": list(NAMEN),
        "fremdvorgaben": [],
        "ausnahmen": [{"grund": "Builder", "pfade": ["scripts/", "*/werkzeuge/*"]}],
    }), encoding="utf-8")
    (wurzel / "CLAUDE.md").write_text(
        "Regel: Hausschrift laut Kanzleiprofil, ohne Profil Times New Roman 11 pt.\n", encoding="utf-8")
    (wurzel / "frei.md").write_text("Export in Times New Roman 11 pt und dezimale Gliederung.\n", encoding="utf-8")
    (wurzel / "schon.md").write_text(
        "Hausschrift laut Kanzleiprofil, ohne Profil Times New Roman 11 pt bleibt.\n", encoding="utf-8")
    (wurzel / "x-schnellstart.md").write_text("Kurz: Export in Times New Roman 11 pt.\n", encoding="utf-8")
    (wurzel / "x-schnellstart.txt").write_text("Kurz: Export in Times New Roman 11 pt.\n", encoding="utf-8")
    (wurzel / "x-hauptproblem.md").write_text("Kurz: Export in Times New Roman 11 pt.\n", encoding="utf-8")
    (wurzel / "scripts").mkdir()
    (wurzel / "scripts" / "build.py").write_text('SCHRIFT = "Times New Roman"\n', encoding="utf-8")
    (wurzel / "plugin" / "werkzeuge").mkdir(parents=True)
    (wurzel / "plugin" / "werkzeuge" / "render.py").write_text('SCHRIFT = "Arial"\n', encoding="utf-8")
    (wurzel / "bild.png").write_bytes(b"\x89PNG Times New Roman")
    (wurzel / "crlf.md").write_bytes(b"Zeile eins in Arial 12 pt.\r\nZeile zwei.\r\n")
    (wurzel / "latin1.md").write_bytes("Notiz ohne Schrift \xe4\n".encode("latin-1"))
    subprocess.run(["git", "-C", str(wurzel), "add", "-A"], check=True)
    (wurzel / "neu.md").write_text("Unversioniert, aber nicht ignoriert: Garamond 12 pt.\n", encoding="utf-8")


def test_kommandozeilen_wenden_an_pruefen_und_melden(tmp_path, capsys):
    """Contract: V1, V3, V6, V7 (Dateiebene)"""
    lege_testrepo_an(tmp_path)
    quelle_vorher = (tmp_path / "hausstil.json").read_text(encoding="utf-8")
    anwenden = lade_kommandozeile("apply-hausstil.py")
    pruefen = lade_kommandozeile("audit-hausstil.py")

    assert anwenden.main(["--repo", str(tmp_path), "--check"]) == 1
    ausgabe = capsys.readouterr().out
    assert "frei.md" in ausgabe and "neu.md" in ausgabe and "x-schnellstart.md" in ausgabe
    assert "latin1.md: keine UTF-8-Datei, übersprungen" in ausgabe
    assert "schon.md" not in ausgabe
    assert (tmp_path / "frei.md").read_text(encoding="utf-8").startswith("Export in Times New Roman")

    assert anwenden.main(["--repo", str(tmp_path)]) == 0
    assert (tmp_path / "frei.md").read_text(encoding="utf-8") == (
        "Export in der Hausschrift laut Kanzleiprofil, ohne Profil Times New Roman 11 pt und dezimale Gliederung.\n")
    assert (tmp_path / "x-schnellstart.md").read_text(encoding="utf-8") == "Kurz: Export in der Kanzleihausschrift.\n"
    assert (tmp_path / "crlf.md").read_bytes() == (
        b"Zeile eins in der Hausschrift laut Kanzleiprofil, ohne Profil Times New Roman 11 pt.\r\nZeile zwei.\r\n")
    assert (tmp_path / "latin1.md").read_bytes() == "Notiz ohne Schrift \xe4\n".encode("latin-1")
    assert (tmp_path / "x-schnellstart.txt").read_bytes() == (tmp_path / "x-schnellstart.md").read_bytes()
    assert (tmp_path / "x-hauptproblem.md").read_bytes() == (tmp_path / "x-schnellstart.md").read_bytes()
    assert (tmp_path / "scripts" / "build.py").read_text(encoding="utf-8") == 'SCHRIFT = "Times New Roman"\n'
    assert (tmp_path / "hausstil.json").read_text(encoding="utf-8") == quelle_vorher
    assert anwenden.main(["--repo", str(tmp_path), "--check"]) == 0
    capsys.readouterr()

    assert pruefen.main(["--repo", str(tmp_path)]) == 0
    assert capsys.readouterr().out.strip().endswith(
        "verstoesse=0 phrase='Hausschrift laut Kanzleiprofil, ohne Profil Times New Roman 11 pt'")

    (tmp_path / "streuner.md").write_text("Zeile eins.\nHier steht Raleway ohne Profil.\n", encoding="utf-8")
    (tmp_path / "streuner-latin1.md").write_bytes("Arial \xe4\n".encode("latin-1"))
    (tmp_path / "CLAUDE.md").write_text("Regel ohne Phrase.\n", encoding="utf-8")
    assert pruefen.main(["--repo", str(tmp_path)]) == 1
    ausgabe = capsys.readouterr().out
    assert "streuner.md:2: Hier steht Raleway ohne Profil." in ausgabe
    assert "streuner-latin1.md:1: Arial" in ausgabe
    assert "CLAUDE.md: kanonische Phrase fehlt" in ausgabe


def test_v6_dateiliste_bricht_ab_wenn_git_fehlt(tmp_path):
    """Contract: V6 (ein Fehler von git darf nicht wie "keine Dateien" aussehen)"""
    with pytest.raises(subprocess.CalledProcessError):
        hs.repo_textdateien(tmp_path, (".md",))


def test_repo_textdateien_liefert_nur_textdateien_mit_endung(tmp_path):
    """Contract: V6 (Binaerdateien und fremde Endungen bleiben aussen vor)"""
    lege_testrepo_an(tmp_path)
    dateien = hs.repo_textdateien(tmp_path, (".md",))
    assert dateien == ["CLAUDE.md", "crlf.md", "frei.md", "latin1.md", "neu.md", "schon.md",
                       "x-hauptproblem.md", "x-schnellstart.md"]
    assert "bild.png" not in hs.repo_textdateien(tmp_path, hs.ENDUNGEN_PRUEFEN)


# --- Injektor (V1) --------------------------------------------------------------------------

ALTER_MARKERBLOCK = (hs.MARKER_BEGIN + "\n> Alter Hinweis mit Times New Roman 11 pt.\n" + hs.MARKER_END)


def test_v1_injektor_hebt_jedes_markerpaar_auf_den_block_aus_hausstil_json(tmp_path):
    """Contract: V1 (der Block entsteht aus hausstil.json; jedes Markerpaar in jeder Markdown-Datei
    traegt dieselbe Fassung, auch in References mit mehreren Paaren; neu eingefuegt nur in SKILL.md)"""
    injektor = lade_kommandozeile("inject-ausformulierungspflicht.py")
    injektor.REPO = tmp_path
    skill = tmp_path / "plug" / "skills" / "vertrag-entwerfen" / "SKILL.md"
    skill.parent.mkdir(parents=True)
    skill.write_text('---\nname: vertrag-entwerfen\ndescription: "Entwirft einen Vertrag"\n---\n'
                     "## Ausgabeformat\n\nText.\n", encoding="utf-8")
    referenz = skill.parent / "references" / "vertiefung.md"
    referenz.parent.mkdir()
    referenz.write_text("# A\n\n" + ALTER_MARKERBLOCK + "\n\n# B\n\n" + ALTER_MARKERBLOCK + "\n", encoding="utf-8")
    notiz = tmp_path / "plug" / "notiz.md"
    notiz.write_text("Keine Marker, keine Skill-Datei.\n", encoding="utf-8")
    changelog = tmp_path / "CHANGELOG.md"
    changelog.write_text("# v1\n\n" + ALTER_MARKERBLOCK + "\n", encoding="utf-8")

    injektor.main()

    block = hs.formatblock(hs.lade_hausstil())
    assert block == injektor.BLOCK
    assert skill.read_text(encoding="utf-8").count(block) == 1
    assert referenz.read_text(encoding="utf-8") == "# A\n\n" + block + "\n\n# B\n\n" + block + "\n"
    assert notiz.read_text(encoding="utf-8") == "Keine Marker, keine Skill-Datei.\n"
    assert changelog.read_text(encoding="utf-8") == "# v1\n\n" + ALTER_MARKERBLOCK + "\n"
    assert "„Kanzleiprofil“" in block and '„Kanzleiprofil"' not in block
    assert hs.finde_verstoesse(skill.read_text(encoding="utf-8"), hs.lade_hausstil()) == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
