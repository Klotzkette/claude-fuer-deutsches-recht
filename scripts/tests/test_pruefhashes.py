"""Tests fuer scripts/pruefhashes.py und scripts/refresh-pruefhashes-nach-hausstil.py.

Vertrag (vom Auftraggeber am 07.10.2026 bestaetigt, hier woertlich):

V8 Nur Mechanik wird nachgezogen: Ein Pruefhash wird genau dann aktualisiert, wenn der aufgezeichnete
   Hash dem Stand der Datei im letzten Commit entspricht und sich der Arbeitsstand davon
   ausschliesslich durch die Hausstil-Phrase (lang oder Kurzform), den automatisch erzeugten
   Formatblock und Leerzeilen unterscheidet. Binaere Dateien gelten nie als mechanisch geaendert.
V9 Spur bleibt: Jeder Pruefvermerk mit Urteil erhaelt beim Nachziehen genau einen datierten Eintrag
   in seiner Aenderungsliste, der die Skripte nennt; Urteil, Begruendung und Pruefdatum bleiben.
V10 Sonst nichts: Ausser Hash und Aenderungseintrag bleibt das Profil gleich, die Schluesselfolge
   eingeschlossen; Profile ohne Aktualisierung werden nicht angefasst; ein zweiter Lauf aendert nichts.
V11 Ehrlich beim Rest: Hashes, die schon im letzten Commit nicht zur Datei passten, fehlende Dateien
   und Dateien mit fachlicher Aenderung bleiben stehen und werden mit Profil und Pfad gemeldet; die
   uebrigen Stellen desselben Profils werden trotzdem bearbeitet. --check schreibt nichts und endet
   mit Status 1, wenn etwas anstehen wuerde. Die Prompts liegen im Plugin-Ordner laut Marketplace;
   ein Profil ohne Marketplace-Plugin wird gemeldet und uebersprungen.

Vor dem Lauf festgelegt (Nachbesserung nach Code-Review am 07.10.2026): Als Formatblock im
Arbeitsstand gilt nur der Block, den hausstil.formatblock erzeugt; ein Markerpaar mit anderem
Inhalt ist Fachinhalt (V8 "automatisch erzeugter Formatblock"). Ein Profil, das nicht in der
kanonischen JSON-Form von quality_lab.save steht, wuerde durch das Schreiben umformatiert; es
bleibt deshalb stehen und jede nachziehbare Stelle wird gemeldet (V10 vor V8; vom Auftraggeber
zu bestaetigen, siehe Bericht).

Als gleichwertig begruendete Mutanten (mutmut 3, 07.10.2026): decode("utf-8") und encode("utf-8")
gegen die Form ohne Codec-Angabe oder mit "UTF-8" (Standardcodec bzw. Alias). Die Kommandozeile
refresh-pruefhashes-nach-hausstil.py traegt einen Bindestrich im Dateinamen und wird hier ueber
importlib geladen; mutmut kann ihr keine Tests zuordnen und meldet ihre Mutanten als "no tests".
Sie hat deshalb keinen gemessenen Mutationswert, nur die Zeilenabdeckung der Dateitests.
"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest
from hypothesis import given
from hypothesis import strategies as st

SKRIPTE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKRIPTE.parent))
sys.path.insert(0, str(SKRIPTE))
from scripts import hausstil as hs  # noqa: E402
from scripts import pruefhashes  # noqa: E402

sys.modules["hausstil"] = hs
sys.modules["pruefhashes"] = pruefhashes
import test_hausstil as th  # noqa: E402  (Generatoren und Testprofil wiederverwenden)

ALTER_BLOCK = (hs.MARKER_BEGIN + "\n> Alter Blocktext mit Times New Roman 11 pt.\n" + hs.MARKER_END + "\n")
NEUER_BLOCK = hs.formatblock(th.STIL_A) + "\n"
VERMERK = ("2026-10-07: Hausschrift-Phrase und Formatblock mechanisch nachgezogen "
           "(scripts/apply-hausstil.py, scripts/inject-ausformulierungspflicht.py); Fachinhalt unverändert.")


def lade_kommandozeile():
    spec = importlib.util.spec_from_file_location(
        "refresh_pruefhashes", SKRIPTE / "refresh-pruefhashes-nach-hausstil.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def mit_block(zeilen: list[str], block: str, position: int, polster: bool = False) -> str:
    """Fuegt den Block an einer Zeilengrenze ein, auf Wunsch mit Leerzeilen davor und dahinter."""
    position = position % (len(zeilen) + 1)
    einschub = [block.rstrip("\n")]
    if polster:
        einschub = ["", ""] + einschub + ["", ""]
    return "\n".join(zeilen[:position] + einschub + zeilen[position:])


def digest(pfad: Path) -> str:
    return pruefhashes.lab.digest(pfad.read_bytes())


# --- V8 -------------------------------------------------------------------------------------

@given(
    zeilen=th.dokument(), alt_mit_block=st.booleans(), kurz=st.booleans(), polster=st.booleans(),
    position_alt=st.integers(min_value=0, max_value=20), position_neu=st.integers(min_value=0, max_value=20),
)
def test_v8_phrase_und_formatblock_gelten_als_mechanisch(
        zeilen, alt_mit_block, kurz, polster, position_alt, position_neu):
    """Contract: V8 (der Injektor ersetzt einen alten Block oder fuegt einen neuen ein; wo, ist egal)"""
    fachinhalt = th.als_text(zeilen)
    alt = fachinhalt
    if alt_mit_block:
        alt = mit_block(fachinhalt.split("\n"), ALTER_BLOCK, position_alt)
    neu_inhalt = hs.ersetze_schriftangaben(fachinhalt, th.STIL_A)
    if kurz:
        neu_inhalt = hs.kurzform(neu_inhalt, th.STIL_A)
    neu = mit_block(neu_inhalt.split("\n"), NEUER_BLOCK, position_neu, polster)
    assert pruefhashes.nur_mechanisch_geaendert(alt.encode("utf-8"), neu.encode("utf-8"), th.STIL_A)


@given(zeilen=th.dokument(), zusatz=st.sampled_from(th.WOERTER), position=st.integers(min_value=0, max_value=20))
def test_v8_jede_inhaltliche_aenderung_ist_nicht_mechanisch(zeilen, zusatz, position):
    """Contract: V8"""
    alt = th.als_text(zeilen)
    neu_zeilen = hs.ersetze_schriftangaben(alt, th.STIL_A).split("\n")
    position = position % len(neu_zeilen)
    neu_zeilen[position] = neu_zeilen[position] + " " + zusatz
    neu = mit_block(neu_zeilen, NEUER_BLOCK, position)
    assert not pruefhashes.nur_mechanisch_geaendert(alt.encode("utf-8"), neu.encode("utf-8"), th.STIL_A)


@given(zeilen=th.dokument(), fremdtext=st.lists(st.sampled_from(th.WOERTER), min_size=1, max_size=5),
       position=st.integers(min_value=0, max_value=20))
def test_v8_markerpaar_mit_fremdem_inhalt_ist_fachinhalt(zeilen, fremdtext, position):
    """Contract: V8 (nur der erzeugte Formatblock ist mechanisch; ein von Hand gesetztes Markerpaar
    mit anderem Text darf keinen frischen Hash bekommen)"""
    alt = th.als_text(zeilen)
    neu_inhalt = hs.ersetze_schriftangaben(alt, th.STIL_A)
    fremder_block = hs.MARKER_BEGIN + "\n> " + " ".join(fremdtext) + "\n" + hs.MARKER_END + "\n"
    neu = mit_block(neu_inhalt.split("\n"), fremder_block, position)
    assert not pruefhashes.nur_mechanisch_geaendert(alt.encode("utf-8"), neu.encode("utf-8"), th.STIL_A)


def test_v8_binaerdateien_sind_nie_mechanisch_geaendert():
    """Contract: V8"""
    assert not pruefhashes.nur_mechanisch_geaendert(b"\xff\xfe\x00PDF", b"\xff\xfe\x00PDF\x01", th.STIL_A)


# --- Dateiebene: V8 bis V11 -----------------------------------------------------------------

def git(wurzel: Path, *argumente: str) -> None:
    subprocess.run(["git", "-C", str(wurzel), *argumente], check=True, capture_output=True)


def schreibe(pfad: Path, text: str) -> None:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(text, encoding="utf-8")


def lege_repo_mit_profilen_an(wurzel: Path) -> None:
    """Plugin "plug" direkt im Repo, Plugin "tief" in einem Unterordner laut Marketplace."""
    git(wurzel, "init", "-q")
    git(wurzel, "config", "user.email", "test@example.invalid")
    git(wurzel, "config", "user.name", "Test")
    schreibe(wurzel / "hausstil.json", json.dumps({
        "standard": {"schrift": "Times New Roman", "groesse": "11 pt", "gliederung": "dezimal"},
        "bekannte_schriftnamen": list(th.NAMEN), "fremdvorgaben": [], "ausnahmen": [],
    }))
    schreibe(wurzel / ".claude-plugin" / "marketplace.json", json.dumps({"plugins": [
        {"name": "plug", "source": "./plug"}, {"name": "tief", "source": "./nest/tief"},
        {"name": "flach", "source": "./flach"}]}))
    schreibe(wurzel / "flach" / "flach-schnellstart.md", "Flach in Times New Roman 11 pt.\n")
    schreibe(wurzel / "plug" / "plug-schnellstart.md", "Export in Times New Roman 11 pt.\n")
    schreibe(wurzel / "plug" / "plug-werkstatt.md", "Werkstatt in Times New Roman 11 pt.\n")
    schreibe(wurzel / "plug" / "plug-hauptproblem.md", "Hauptproblem in Times New Roman 11 pt.\n")
    schreibe(wurzel / "plug" / "skills" / "brief" / "SKILL.md", "## 5 Ausgabe\n\n" + ALTER_BLOCK + "\nText.\n")
    schreibe(wurzel / "nest" / "tief" / "tief-schnellstart.md", "Tief in Times New Roman 11 pt.\n")
    profil = {
        "schema_version": 1, "plugin": "plug", "reviewed_on": "2026-09-01",
        "mini_review": {"verdict": "retained", "reason": "Gut.", "changes": [],
                        "sha256": digest(wurzel / "plug" / "plug-schnellstart.md"), "reviewed_on": "2026-09-01"},
        "workshop_review": {"verdict": "revised", "reason": "Auch gut.", "sha256": "0" * 64,
                            "reviewed_on": "2026-09-01"},
        "focus_review": {"verdict": "revised", "reason": "Schwerpunkt.",
                         "prompt_sha256": digest(wurzel / "plug" / "plug-hauptproblem.md"),
                         "prompt_path": "plug/plug-hauptproblem.md",
                         "skill_sha256": digest(wurzel / "plug" / "skills" / "brief" / "SKILL.md"),
                         "skill_path": "plug/skills/brief/SKILL.md"},
        "individual_skill_review": [{"path": "plug/skills/verschollen/SKILL.md", "sha256": "1" * 64,
                                     "verdict": "retained"}],
        "skill_reviews": [{"skill_path": "plug/skills/brief/SKILL.md",
                           "sha256": digest(wurzel / "plug" / "skills" / "brief" / "SKILL.md"),
                           "verdict": "revised", "reason": "Ok."}],
        "artifact_hashes": {"plug/plug-schnellstart.md": digest(wurzel / "plug" / "plug-schnellstart.md")},
        "nachher": "bleibt letzter Schluessel",
    }
    schreibe(wurzel / "quality" / "evals" / "plug.json", json.dumps(profil, ensure_ascii=False, indent=2) + "\n")
    tief = {"schema_version": 1, "plugin": "tief", "reviewed_on": "2026-09-01",
            "mini_review": {"verdict": "retained", "reason": "Tief.", "changes": [],
                            "sha256": digest(wurzel / "nest" / "tief" / "tief-schnellstart.md")}}
    schreibe(wurzel / "quality" / "evals" / "tief.json", json.dumps(tief, ensure_ascii=False, indent=2) + "\n")
    flach = {"schema_version": 1, "plugin": "flach", "reviewed_on": "2026-09-01",
             "mini_review": {"verdict": "retained", "reason": "Flach.", "changes": [],
                             "sha256": digest(wurzel / "flach" / "flach-schnellstart.md")},
             "artifact_hashes": {"flach/flach-schnellstart.md": digest(wurzel / "flach" / "flach-schnellstart.md")}}
    # kompakt geschrieben: ein solches Profil darf weder ohne noch mit Aktualisierung umformatiert werden (V10)
    schreibe(wurzel / "quality" / "evals" / "flach.json", json.dumps(flach, ensure_ascii=False))
    # verwaist: Plugin steht nicht im Marketplace, der Prompt-Ordner ist unbekannt (V11); es wird
    # alphabetisch vor den anderen Profilen gelesen, damit das Ueberspringen nicht den Lauf beendet
    schreibe(wurzel / "quality" / "evals" / "a-waise.json", json.dumps(
        {"schema_version": 1, "plugin": "waise", "mini_review": {"verdict": "retained", "sha256": "2" * 64}}))
    git(wurzel, "add", "-A")
    git(wurzel, "commit", "-q", "-m", "Stand der Pruefung")


def test_v8_bis_v11_auf_dateiebene(tmp_path, capsys):
    """Contract: V8, V9, V10, V11"""
    lege_repo_mit_profilen_an(tmp_path)
    profil_pfad = tmp_path / "quality" / "evals" / "plug.json"
    tief_pfad = tmp_path / "quality" / "evals" / "tief.json"
    phrase = hs.kanonische_phrase(th.STIL_A)
    # mechanisch: Kurzform im Schnellstart, lange Phrase im Hauptproblem, Phrase und neuer Block im Skill
    schreibe(tmp_path / "plug" / "plug-schnellstart.md", "Export in der Kanzleihausschrift.\n")
    schreibe(tmp_path / "plug" / "plug-hauptproblem.md", f"Hauptproblem in der {phrase}.\n")
    schreibe(tmp_path / "plug" / "skills" / "brief" / "SKILL.md", "## 5 Ausgabe\n\n\n" + NEUER_BLOCK + "\n\nText.\n")
    # fachlich: Werkstatt bekommt zusaetzlich einen neuen Satz (und ihr Hash passte ohnehin nie)
    schreibe(tmp_path / "plug" / "plug-werkstatt.md", f"Werkstatt in der {phrase}. Neuer Satz.\n")
    vorher = profil_pfad.read_text(encoding="utf-8")
    tief_vorher = tief_pfad.read_text(encoding="utf-8")
    kommandozeile = lade_kommandozeile()

    assert kommandozeile.main(["--repo", str(tmp_path), "--check", "--datum", "2026-10-07"]) == 1
    assert profil_pfad.read_text(encoding="utf-8") == vorher
    ausgabe = capsys.readouterr().out
    assert "plug.json: plug/plug-werkstatt.md: Hash passt nicht zum letzten Commit, bleibt stehen" in ausgabe
    assert "plug.json: plug/skills/verschollen/SKILL.md: Datei fehlt" in ausgabe
    assert "a-waise.json: Profil ohne Marketplace-Plugin, übersprungen" in ausgabe
    assert "plug.json: plug/plug-schnellstart.md\n" in ausgabe
    assert ausgabe.strip().endswith("anstehend=5 unveraendert=3 gemeldet=3")

    assert kommandozeile.main(["--repo", str(tmp_path), "--datum", "2026-10-07"]) == 0
    capsys.readouterr()
    profil = json.loads(profil_pfad.read_text(encoding="utf-8"))
    assert profil["mini_review"]["sha256"] == digest(tmp_path / "plug" / "plug-schnellstart.md")
    assert profil["artifact_hashes"]["plug/plug-schnellstart.md"] == digest(tmp_path / "plug" / "plug-schnellstart.md")
    assert profil["focus_review"]["prompt_sha256"] == digest(tmp_path / "plug" / "plug-hauptproblem.md")
    assert profil["focus_review"]["skill_sha256"] == digest(tmp_path / "plug" / "skills" / "brief" / "SKILL.md")
    assert profil["skill_reviews"][0]["sha256"] == digest(tmp_path / "plug" / "skills" / "brief" / "SKILL.md")
    assert profil["workshop_review"]["sha256"] == "0" * 64
    assert profil["individual_skill_review"][0]["sha256"] == "1" * 64
    assert profil["mini_review"]["changes"] == [VERMERK]
    assert profil["focus_review"]["changes"] == [VERMERK]
    assert profil["skill_reviews"][0]["changes"] == [VERMERK]
    assert "changes" not in profil["workshop_review"]
    for feld in ("verdict", "reason", "reviewed_on"):
        assert profil["mini_review"][feld] == json.loads(vorher)["mini_review"][feld]
    assert list(profil.keys()) == list(json.loads(vorher).keys())
    assert tief_pfad.read_text(encoding="utf-8") == tief_vorher

    nach_erstem_lauf = profil_pfad.read_text(encoding="utf-8")
    assert kommandozeile.main(["--repo", str(tmp_path), "--datum", "2026-10-08"]) == 0
    assert profil_pfad.read_text(encoding="utf-8") == nach_erstem_lauf
    assert capsys.readouterr().out.strip().endswith("aktualisiert=0 unveraendert=8 gemeldet=3")
    assert (tmp_path / "quality" / "evals" / "a-waise.json").read_text(encoding="utf-8").count("2" * 64) == 1


def test_v11_prompt_im_marketplace_ordner_wird_gefunden(tmp_path, capsys):
    """Contract: V11"""
    lege_repo_mit_profilen_an(tmp_path)
    schreibe(tmp_path / "nest" / "tief" / "tief-schnellstart.md", "Tief in der Kanzleihausschrift.\n")
    assert lade_kommandozeile().main(["--repo", str(tmp_path), "--datum", "2026-10-07"]) == 0
    assert "tief.json: nest/tief/tief-schnellstart.md\n" in capsys.readouterr().out
    profil = json.loads((tmp_path / "quality" / "evals" / "tief.json").read_text(encoding="utf-8"))
    assert profil["mini_review"]["sha256"] == digest(tmp_path / "nest" / "tief" / "tief-schnellstart.md")


def test_v11_fachliche_aenderung_bleibt_stehen_und_wird_gemeldet(tmp_path, capsys):
    """Contract: V11"""
    lege_repo_mit_profilen_an(tmp_path)
    phrase = hs.kanonische_phrase(th.STIL_A)
    schreibe(tmp_path / "plug" / "plug-schnellstart.md", f"Export in der {phrase}. Neue Pflicht.\n")
    assert lade_kommandozeile().main(["--repo", str(tmp_path), "--datum", "2026-10-07"]) == 0
    ausgabe = capsys.readouterr().out
    assert "plug.json: plug/plug-schnellstart.md: fachlich geändert, neue Prüfung nötig" in ausgabe
    assert ausgabe.strip().endswith("aktualisiert=0 unveraendert=6 gemeldet=5")
    profil = json.loads((tmp_path / "quality" / "evals" / "plug.json").read_text(encoding="utf-8"))
    assert profil["mini_review"]["changes"] == []
    assert profil["mini_review"]["sha256"] != digest(tmp_path / "plug" / "plug-schnellstart.md")


def test_v10_nicht_kanonisches_profil_bleibt_byteidentisch_und_wird_gemeldet(tmp_path, capsys):
    """Contract: V10, V11 (das Schreiben wuerde ein kompakt geschriebenes Profil umformatieren; es
    bleibt stehen, jede nachziehbare Stelle wird mit Profil und Pfad gemeldet, --check meldet nichts an)"""
    lege_repo_mit_profilen_an(tmp_path)
    schreibe(tmp_path / "flach" / "flach-schnellstart.md", "Flach in der Kanzleihausschrift.\n")
    flach_pfad = tmp_path / "quality" / "evals" / "flach.json"
    vorher = flach_pfad.read_bytes()
    meldung = "flach.json: flach/flach-schnellstart.md: Profil nicht in kanonischer JSON-Form"
    kommandozeile = lade_kommandozeile()
    assert kommandozeile.main(["--repo", str(tmp_path), "--check", "--datum", "2026-10-07"]) == 0
    assert capsys.readouterr().out.count(meldung) == 2
    assert kommandozeile.main(["--repo", str(tmp_path), "--datum", "2026-10-07"]) == 0
    ausgabe = capsys.readouterr().out
    assert ausgabe.count(meldung) == 2
    assert ausgabe.strip().endswith("aktualisiert=0 unveraendert=6 gemeldet=5")
    assert flach_pfad.read_bytes() == vorher
    # normalisiert ist das Profil nachziehbar, an beiden Stellen
    pruefhashes.lab.save(flach_pfad, pruefhashes.lab.load(flach_pfad))
    assert kommandozeile.main(["--repo", str(tmp_path), "--datum", "2026-10-07"]) == 0
    assert capsys.readouterr().out.count("flach.json: flach/flach-schnellstart.md\n") == 2
    profil = json.loads(flach_pfad.read_text(encoding="utf-8"))
    assert profil["mini_review"]["sha256"] == digest(tmp_path / "flach" / "flach-schnellstart.md")
    assert profil["artifact_hashes"]["flach/flach-schnellstart.md"] == profil["mini_review"]["sha256"]


def test_v11_datei_ohne_stand_im_letzten_commit_bleibt_stehen(tmp_path, capsys):
    """Contract: V11 (eine erst nach dem Commit angelegte Datei hat keinen geprueften Stand)"""
    lege_repo_mit_profilen_an(tmp_path)
    schreibe(tmp_path / "plug" / "plug-neu.md", "Neu, nie committet.\n")
    profil_pfad = tmp_path / "quality" / "evals" / "plug.json"
    profil = json.loads(profil_pfad.read_text(encoding="utf-8"))
    profil["reviewed_file_hashes"] = {"plug/plug-neu.md": "3" * 64}
    profil_pfad.write_text(json.dumps(profil, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    assert lade_kommandozeile().main(["--repo", str(tmp_path), "--datum", "2026-10-07"]) == 0
    assert "plug.json: plug/plug-neu.md: Hash passt nicht zum letzten Commit, bleibt stehen" in capsys.readouterr().out
    profil = json.loads(profil_pfad.read_text(encoding="utf-8"))
    assert profil["reviewed_file_hashes"]["plug/plug-neu.md"] == "3" * 64


def test_hashstellen_erfasst_alle_bekannten_formen():
    """Contract: V8 (jede Hashform wird gefunden, keine doppelt, Luecken stoeren nicht)"""
    profil = {
        "plugin": "p",
        "workshop_review": {"sha256": "b"},
        "focus_review": {"prompt_sha256": "c", "prompt_path": "p/haupt.md",
                         "skill_sha256": "d", "skill_path": "p/s.md"},
        "phase_workshop_reviews": [{"path": "p/ph.md", "sha256": "e"}],
        "individual_skill_review": [{"path": "p/i.md", "sha256": "f"}],
        "skill_reviews": [{"skill_path": "p/sk.md", "sha256": "g"}, {"sha256": "ohne pfad"}],
        "case_review": {"files": [{"path": "t/x.eml", "sha256": "h"}, {"sha256": "ohne pfad"}, {"path": "ohne hash"}]},
        "artifact_hashes": {"p/a.md": "i"}, "reviewed_file_hashes": {"p/r.md": "j"},
        "skill_hashes": {"p/s2.md": "k"},
        "sources": [{"url": "https://example.invalid", "sha256": "nicht dateibezogen"}],
    }
    stellen = pruefhashes.hashstellen(profil, "ordner/p")
    assert [(s.ziel, s.traeger[s.schluessel]) for s in stellen] == [
        ("ordner/p/p-werkstatt.md", "b"), ("p/haupt.md", "c"), ("p/s.md", "d"), ("p/ph.md", "e"),
        ("p/i.md", "f"), ("p/sk.md", "g"), ("t/x.eml", "h"), ("p/a.md", "i"), ("p/r.md", "j"), ("p/s2.md", "k")]
    assert [s.vermerk is None for s in stellen] == [False] * 6 + [True] * 4
    eigener_pfad = pruefhashes.hashstellen({"plugin": "p", "mini_review": {"sha256": "a", "path": "x/y.md"}}, "p")
    assert eigener_pfad[0].ziel == "x/y.md"


# Hashes in den echten Profilen, die keinen geprueften Repo-Text bezeichnen: Belege, Quellen, Protokolle.
KEINE_PRUEFHASHES = (
    ".sources[", ".prompt_editorial_review.", ".source_link_audit_", ".regression_review_status.",
    ".case_review.layout_update.", ".case_review.source_sha256", ".source_audit_review.",
    ".local_source_provenance[",
)
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def hashpfade(objekt, pfad: str = "") -> list[tuple[str, dict, str]]:
    """Jeder 64-stellige Hex-String im Profil mit seinem Schluesselpfad (Listenindizes als [])."""
    gefunden = []
    if isinstance(objekt, dict):
        for schluessel, wert in objekt.items():
            if isinstance(wert, str) and HEX64.match(wert):
                gefunden.append((f"{pfad}.{schluessel}", objekt, schluessel))
            gefunden.extend(hashpfade(wert, f"{pfad}.{schluessel}"))
    elif isinstance(objekt, list):
        for wert in objekt:
            gefunden.extend(hashpfade(wert, f"{pfad}[]"))
    return gefunden


def test_v8_hashstellen_deckt_jeden_dateihash_der_echten_profile():
    """Contract: V8 (eine neue Hashform im Schema von quality_lab darf nicht stumm uebergangen werden;
    jeder Hash ausserhalb der bekannten Beleg- und Protokollfelder muss eine Hashstelle sein)"""
    profile = sorted((SKRIPTE.parent / "quality" / "evals").glob("*.json"))
    assert profile, "keine Profile gefunden"
    nicht_gedeckt = []
    for profil_pfad in profile:
        profil = pruefhashes.lab.load(profil_pfad)
        gedeckt = {(id(stelle.traeger), stelle.schluessel) for stelle in pruefhashes.hashstellen(profil, "ordner")}
        for schluesselpfad, traeger, schluessel in hashpfade(profil):
            if schluesselpfad.startswith(KEINE_PRUEFHASHES):
                continue
            if (id(traeger), schluessel) not in gedeckt:
                nicht_gedeckt.append(f"{profil_pfad.name}: {schluesselpfad}")
    assert nicht_gedeckt == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
