"""Nachziehen von Pruefhashes in quality/evals nach einer rein mechanischen Textaenderung.

Die Prueprofile halten SHA-256-Hashes der gepruften Prompts und Skills fest. Wird der
neutrale Hausstil geaendert (hausstil.json, dann scripts/apply-hausstil.py und
scripts/inject-ausformulierungspflicht.py), aendern sich diese Dateien mechanisch, ohne dass
ihr Fachinhalt beruehrt ist. Dieses Modul erkennt genau diesen Fall am Vergleich mit dem
letzten Commit und zieht nur dann den Hash nach; jeder Pruefvermerk mit Urteil bekommt einen
datierten Eintrag in seiner Aenderungsliste. Alles andere bleibt stehen und wird gemeldet.
"""
from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import hausstil as hs
import quality_lab as lab

FORMATBLOCK = re.compile(
    r"<!-- BEGIN ausformulierungspflicht \(autogen\) -->[\s\S]*?<!-- END ausformulierungspflicht \(autogen\) -->\n?"
)
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


def ohne_mechanik(text: str) -> str:
    """Text ohne Formatblock und ohne Leerzeilen, so dass nur der Fachinhalt verglichen wird."""
    text = FORMATBLOCK.sub("", text)
    zeilen = [zeile for zeile in text.split("\n") if zeile.strip()]
    return "\n".join(zeilen)


def nur_mechanisch_geaendert(alt: bytes, neu: bytes, stil: hs.Hausstil) -> bool:
    """Wahr, wenn sich neu von alt allein durch Hausstil-Phrase (lang oder Kurzform), Formatblock und
    Leerzeilen unterscheidet. Binaere Dateien werden nie als mechanisch geaendert gewertet."""
    alt_text = alt.decode("utf-8", errors="replace")
    neu_text = neu.decode("utf-8", errors="replace")
    erwartet_lang = hs.ersetze_schriftangaben(ohne_mechanik(alt_text), stil)
    erwartet_kurz = hs.kurzform(erwartet_lang, stil)
    return ohne_mechanik(neu_text) in (erwartet_lang, erwartet_kurz)


def vermerktext(datum: str) -> str:
    return (f"{datum}: Hausschrift-Phrase und Formatblock mechanisch nachgezogen "
            "(scripts/apply-hausstil.py, scripts/inject-ausformulierungspflicht.py); Fachinhalt unverändert.")


def plugin_verzeichnisse(repo: Path) -> dict[str, str]:
    """Plugin-Name -> Ordner relativ zum Repo, wie der Marketplace ihn fuehrt."""
    verzeichnisse = {}
    for name, ordner in lab.marketplace(repo).items():
        verzeichnisse[name] = ordner.resolve().relative_to(repo.resolve()).as_posix()
    return verzeichnisse


def nachziehen(repo: Path, stil: hs.Hausstil, datum: str, schreiben: bool) -> Bilanz:
    bilanz = Bilanz()
    verzeichnisse = plugin_verzeichnisse(repo)
    for profil_pfad in sorted((repo / "quality" / "evals").glob("*.json")):
        profil = lab.load(profil_pfad)
        if profil["plugin"] not in verzeichnisse:
            bilanz.gemeldet.append(f"{profil_pfad.name}: Profil ohne Marketplace-Plugin, übersprungen")
            continue
        verzeichnis = verzeichnisse[profil["plugin"]]
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
            stelle.traeger[stelle.schluessel] = jetzt
            if stelle.vermerk is not None and "verdict" in stelle.vermerk:
                aenderungen = stelle.vermerk.setdefault("changes", [])
                if vermerktext(datum) not in aenderungen:
                    aenderungen.append(vermerktext(datum))
            bilanz.aktualisiert.append(ort)
        if schreiben and len(bilanz.aktualisiert) > aktualisiert_vorher:
            lab.save(profil_pfad, profil)
    return bilanz
