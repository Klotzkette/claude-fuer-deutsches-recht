"""Nachziehen von Pruefhashes in quality/evals nach einer rein mechanischen Textaenderung.

Die Prueprofile halten SHA-256-Hashes der gepruften Prompts und Skills fest. Wird der
neutrale Hausstil geaendert (hausstil.json, dann scripts/inject-ausformulierungspflicht.py und
scripts/apply-hausstil.py), aendern sich diese Dateien mechanisch, ohne dass ihr Fachinhalt
beruehrt ist. Dieses Modul erkennt genau diesen Fall am Vergleich mit dem letzten Commit und
zieht nur dann den Hash nach; jeder Pruefvermerk mit Urteil bekommt einen datierten Eintrag in
seiner Aenderungsliste. Alles andere bleibt stehen und wird gemeldet.

Als Formatblock gilt im Arbeitsstand nur der Block, den hausstil.formatblock gerade erzeugt;
ein Markerpaar mit anderem Inhalt ist Fachinhalt. Ein Profil wird nur geschrieben, wenn es in
der kanonischen JSON-Form von quality_lab.save steht; sonst wuerde das Schreiben es umformatieren
und der Hash-Nachzug waere im Diff nicht mehr als solcher erkennbar.
"""
from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import hausstil as hs
import quality_lab as lab

MARKERBLOCK = re.compile(re.escape(hs.MARKER_BEGIN) + r"[\s\S]*?" + re.escape(hs.MARKER_END) + r"\n?")
PROMPTVERMERKE = (("mini_review", "schnellstart"), ("workshop_review", "werkstatt"), ("focus_review", "hauptproblem"))
VERMERKLISTEN = ("phase_workshop_reviews", "individual_skill_review", "skill_reviews")
HASHTABELLEN = ("artifact_hashes", "reviewed_file_hashes", "skill_hashes")


@dataclass
class Hashstelle:
    traeger: dict           # das Objekt, das den Hash unter `schluessel` haelt
    schluessel: str
    ziel: str               # Pfad der gepruften Datei, relativ zum Repo
    vermerk: dict | None    # Pruefvermerk, der den Aenderungseintrag bekommt (None bei reinen Hashtabellen)


@dataclass
class Bilanz:
    aktualisiert: list[str] = field(default_factory=list)
    gemeldet: list[str] = field(default_factory=list)
    unveraendert: int = 0


def hashstellen(profil: dict, verzeichnis: str) -> list[Hashstelle]:
    """Alle Stellen eines Profils, an denen ein Dateihash steht, mit der zugehoerigen Datei.
    `verzeichnis` ist der Plugin-Ordner laut Marketplace, relativ zum Repo (dort liegen die Prompts)."""
    slug = profil["plugin"]
    stellen = []
    for art, dateiart in PROMPTVERMERKE:
        vermerk = profil.get(art)
        if not isinstance(vermerk, dict):
            continue
        if "sha256" in vermerk:
            ziel = vermerk.get("path", f"{verzeichnis}/{slug}-{dateiart}.md")
            stellen.append(Hashstelle(vermerk, "sha256", ziel, vermerk))
        if "prompt_sha256" in vermerk:
            stellen.append(Hashstelle(vermerk, "prompt_sha256", vermerk["prompt_path"], vermerk))
        if "skill_sha256" in vermerk:
            stellen.append(Hashstelle(vermerk, "skill_sha256", vermerk["skill_path"], vermerk))
    for art in VERMERKLISTEN:
        for vermerk in profil.get(art) or []:
            ziel = vermerk.get("path") or vermerk.get("skill_path")
            if "sha256" in vermerk and ziel:
                stellen.append(Hashstelle(vermerk, "sha256", ziel, vermerk))
    fallpruefung = profil.get("case_review")
    if isinstance(fallpruefung, dict):
        for eintrag in fallpruefung.get("files") or []:
            if "sha256" in eintrag and "path" in eintrag:
                stellen.append(Hashstelle(eintrag, "sha256", eintrag["path"], None))
    for art in HASHTABELLEN:
        tabelle = profil.get(art)
        if isinstance(tabelle, dict):
            for ziel in tabelle:
                stellen.append(Hashstelle(tabelle, ziel, ziel, None))
    return stellen


def letzter_commit(repo: Path, ziel: str) -> bytes | None:
    """Inhalt der Datei im letzten Commit; None, wenn sie dort nicht existiert."""
    ergebnis = subprocess.run(["git", "-C", str(repo), "show", f"HEAD:{ziel}"], capture_output=True)
    if ergebnis.returncode != 0:
        return None
    return ergebnis.stdout


def _ohne_leerzeilen(text: str) -> str:
    zeilen = [zeile for zeile in text.split("\n") if zeile.strip()]
    return "\n".join(zeilen)


def ohne_formatbloecke(text: str) -> str:
    """Der gepruefte Stand aus dem Commit ohne jeden Markerblock und ohne Leerzeilen. Was damals
    zwischen den Markern stand, hat der Injektor erzeugt; es zaehlt nicht als Fachinhalt."""
    return _ohne_leerzeilen(MARKERBLOCK.sub("", text))


def ohne_erzeugten_formatblock(text: str, block: str) -> str:
    """Der Arbeitsstand ohne den gerade erzeugten Block und ohne Leerzeilen. Ein Markerpaar mit
    anderem Inhalt bleibt stehen und zaehlt als Fachinhalt."""
    return _ohne_leerzeilen(text.replace(block, ""))


def nur_mechanisch_geaendert(alt: bytes, neu: bytes, stil: hs.Hausstil) -> bool:
    """Wahr, wenn sich neu von alt allein durch Hausstil-Phrase (lang oder Kurzform), den erzeugten
    Formatblock und Leerzeilen unterscheidet. Binaere Dateien werden nie als mechanisch geaendert gewertet."""
    alt_text = alt.decode("utf-8", errors="replace")
    neu_text = neu.decode("utf-8", errors="replace")
    erwartet_lang = hs.ersetze_schriftangaben(ohne_formatbloecke(alt_text), stil)
    erwartet_kurz = hs.kurzform(erwartet_lang, stil)
    jetzt = ohne_erzeugten_formatblock(neu_text, hs.formatblock(stil))
    return jetzt in (erwartet_lang, erwartet_kurz)


def vermerktext(datum: str) -> str:
    return (f"{datum}: Hausschrift-Phrase und Formatblock mechanisch nachgezogen "
            "(scripts/apply-hausstil.py, scripts/inject-ausformulierungspflicht.py); Fachinhalt unverändert.")


def plugin_verzeichnisse(repo: Path) -> dict[str, str]:
    """Plugin-Name -> Ordner relativ zum Repo, wie der Marketplace ihn fuehrt."""
    verzeichnisse = {}
    for name, ordner in lab.marketplace(repo).items():
        verzeichnisse[name] = ordner.resolve().relative_to(repo.resolve()).as_posix()
    return verzeichnisse


def ist_kanonisch(profil_pfad: Path, profil: dict) -> bool:
    """Wahr, wenn quality_lab.save das Profil byteidentisch wieder schreiben wuerde."""
    return profil_pfad.read_bytes() == lab.dumps(profil).encode("utf-8")


def nachziehen(repo: Path, stil: hs.Hausstil, datum: str, schreiben: bool) -> Bilanz:
    bilanz = Bilanz()
    verzeichnisse = plugin_verzeichnisse(repo)
    for profil_pfad in sorted((repo / "quality" / "evals").glob("*.json")):
        profil = lab.load(profil_pfad)
        if profil["plugin"] not in verzeichnisse:
            bilanz.gemeldet.append(f"{profil_pfad.name}: Profil ohne Marketplace-Plugin, übersprungen")
            continue
        verzeichnis = verzeichnisse[profil["plugin"]]
        kanonisch = ist_kanonisch(profil_pfad, profil)
        aktualisiert_vorher = len(bilanz.aktualisiert)
        for stelle in hashstellen(profil, verzeichnis):
            datei = repo / stelle.ziel
            ort = f"{profil_pfad.name}: {stelle.ziel}"
            if not datei.is_file():
                bilanz.gemeldet.append(f"{ort}: Datei fehlt")
                continue
            jetzt = lab.digest(datei.read_bytes())
            aufgezeichnet = stelle.traeger[stelle.schluessel]
            if jetzt == aufgezeichnet:
                bilanz.unveraendert += 1
                continue
            im_commit = letzter_commit(repo, stelle.ziel)
            if im_commit is None or lab.digest(im_commit) != aufgezeichnet:
                bilanz.gemeldet.append(f"{ort}: Hash passt nicht zum letzten Commit, bleibt stehen")
                continue
            if not nur_mechanisch_geaendert(im_commit, datei.read_bytes(), stil):
                bilanz.gemeldet.append(f"{ort}: fachlich geändert, neue Prüfung nötig")
                continue
            if not kanonisch:
                bilanz.gemeldet.append(
                    f"{ort}: Profil nicht in kanonischer JSON-Form, zuerst normalisieren (quality_lab.save), bleibt stehen")
                continue
            stelle.traeger[stelle.schluessel] = jetzt
            if stelle.vermerk is not None and "verdict" in stelle.vermerk:
                aenderungen = stelle.vermerk.setdefault("changes", [])
                if vermerktext(datum) not in aenderungen:
                    aenderungen.append(vermerktext(datum))
            bilanz.aktualisiert.append(ort)
        if schreiben and len(bilanz.aktualisiert) > aktualisiert_vorher:
            lab.save(profil_pfad, profil)
    return bilanz
