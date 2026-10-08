#!/usr/bin/env python3
"""Prüft Vorlagen auf missverständliche Rechtsprechungs-Formulierungen.

Der Check verhindert keine juristischen Fehler. Er blockiert aber Formulierungen,
die im Vorlagenkontext eine nicht belegte Quellenprüfung behaupten oder
Aktenzeichen aus Modellwissen wie fertige Zitate wirken lassen.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# Begriffe in Nachbarschaft, die das `verifiziert`-Adjektiv juristisch
# aufladen: Rechtsprechung, Entscheidung(en), Aktenzeichen, Az., Urteil,
# Beschluss, Fundstelle(n), Zitat(e), Anker, Senatsrechtsprechung, Rspr.
NACHBAR = (
    r"Rechtsprechung|Senatsrechtsprechung|Rspr\.|Entscheidung(?:en)?|"
    r"Aktenzeichen|Az\.|Urteil(?:e)?|Beschluss|Beschlüsse|"
    r"Fundstelle(?:n)?|Zitat(?:e)?|Anker"
)

VERBOTENE_MUSTER = [
    # Ursprungsmuster bleiben
    (re.compile(r"Rechtsprechung\s*\(verifiziert\)", re.I), "nicht 'verifiziert' behaupten"),
    (re.compile(r"BGHZ\s+vorgesehen", re.I), "keine nicht verifizierte Fundstelle ankündigen"),
    (re.compile(r"Az\.\s+nach\s+offiziellem\s+Verzeichnis", re.I), "Aktenzeichen nicht halb zitieren"),
    (re.compile(r"keine\s+aktuellen\s+.+\s+verifiziert", re.I), "negative Verifikationsbehauptung vermeiden"),
    (
        re.compile(r"(?:Aktenzeichen|Az\.)[^.\n]{0,40}(?:nach\s+Nutzer(?:hinweis|angabe)|-ähnliche\s+Linie)", re.I),
        "Nutzerangaben und aktenzeichenähnliche Linien sind keine belastbaren Fundstellen",
    ),
    (
        re.compile(r"\b(?:Urteil|Beschluss|Entscheidung)[^.\n]{0,80}\bnach\s+Nutzer(?:hinweis|angabe)\b", re.I),
        "Entscheidungen nicht aus ungeprüften Nutzerangaben zitieren",
    ),
    # Verbreiterte Verifikationsbehauptung: inflektiert (verifiziert,
    # verifizierte, verifizierten, verifizierter, verifiziertes) in Nachbarschaft
    # zu einem juristisch geladenen Begriff. Erfasst auch die umgekehrte
    # Wortstellung (`Rechtsprechung ... verifiziert`).
    (
        re.compile(
            rf"\bverifiziert(?:e|en|er|es)?\b[^.\n]{{0,40}}\b(?:{NACHBAR})\b",
            re.I,
        ),
        "keine Selbst-Verifikation der Rechtsprechung in der Vorlage",
    ),
    (
        re.compile(
            rf"\b(?:{NACHBAR})\b[^.\n]{{0,40}}\bverifiziert(?:e|en|er|es)?\b",
            re.I,
        ),
        "keine Selbst-Verifikation der Rechtsprechung in der Vorlage",
    ),
]


def git_ls_files(pattern: str) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            pattern,
        ],
        cwd=REPO,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return [REPO / line for line in result.stdout.splitlines() if " 2." not in line]


# Dateien, die der Check nicht beachtet:
# - EVAL_RESULTS.md ist generierter Eval-Report und nennt den Rubric-Namen
#   `r90-az-live-verifiziert` lediglich als Prüffeldnamen.
# - CHANGELOG.md beschreibt vergangene Korrekturen, dort darf das Wort
#   `verifiziert` in der Versionshistorie stehen, ohne dass eine Vorlage selbst
#   eine Verifikation behauptet.
AUSGENOMMEN = {"EVAL_RESULTS.md", "CHANGELOG.md"}

# Auf derselben Zeile entwertet einer dieser Marker den Treffer:
# - Negationen ("keine verifizierten", "nicht verifiziert", "unverifiziert")
# - Normative Anweisungen ("muss verifiziert", "vor Übernahme verifizieren",
#   "live verifizieren", "verifizieren" als Imperativ).
# Direkt vor dem `verifiziert`-Wort (innerhalb von ~20 Zeichen) stehende
# Marker, die den Treffer entkräften. Wir prüfen lokal (Fensterbreite), damit
# eine Zeile, in der gleichzeitig ein Boast ("als verifiziert übernommen")
# UND ein Imperativ ("verifizieren") steht, den Boast nicht durch den
# Imperativ verdeckt sieht.
LOKAL_NEGIERT = re.compile(
    r"(?:\bkein(?:e[nrms]?)?\b|\bnicht\b|\bniemals\b|\bunverifiziert\b|"
    r"\bmuss\b|\bsoll\b|\bist\s+zu\b|\bsind\s+zu\b|\blive\b|"
    r"\bnur[,\s]+wenn\b|\bnur\s+verifizierte?\b|\blieber\s+weglassen\b|"
    r"\bvor\s+\u00dcbernahme\b|\bvor\s+Verwendung\b)",
    re.I,
)


def main() -> int:
    fehler: list[str] = []
    gesehen: set[tuple[str, int, str]] = set()
    for pfad in git_ls_files("*.md"):
        rel = pfad.relative_to(REPO)
        if rel.name in AUSGENOMMEN or rel.parts[0] == "scripts":
            continue
        text = pfad.read_text(encoding="utf-8")
        for zeilennummer, zeile in enumerate(text.splitlines(), start=1):
            for muster, hinweis in VERBOTENE_MUSTER:
                m = muster.search(zeile)
                if not m:
                    continue
                # Negierte oder normative Verwendung des Wortes `verifiziert`
                # ist kein Verstoss. Die spezifischen Muster aus dem Original
                # (z. B. `Rechtsprechung (verifiziert)`) bleiben strikt.
                if hinweis == "keine Selbst-Verifikation der Rechtsprechung in der Vorlage":
                    # Lokal um die Trefferregion: 25 Zeichen davor prüfen.
                    start = max(0, m.start() - 25)
                    umgebung = zeile[start:m.end()]
                    if LOKAL_NEGIERT.search(umgebung):
                        continue
                schluessel = (str(rel), zeilennummer, hinweis)
                if schluessel in gesehen:
                    continue
                gesehen.add(schluessel)
                fehler.append(f"{rel}:{zeilennummer}: {hinweis}: {zeile.strip()[:160]}")

    # Die zentrale Ankerliste darf keine bloßen Aktenzeichen mehr verteilen.
    # Jede dort genannte Entscheidung muss unmittelbar auf eine amtliche oder
    # primäre Quelle verlinken; dadurch bleiben Rechtsgebiet und Prüfgegenstand
    # am überprüfbaren Volltext ausgerichtet.
    ankerdatei = REPO / "references" / "leitentscheidungen-anker.md"
    for zeilennummer, zeile in enumerate(ankerdatei.read_text(encoding="utf-8").splitlines(), start=1):
        if not zeile.startswith("- "):
            continue
        if not re.search(r"\b(?:BVerfG|BVerwG|BGH|BAG|BSG|BFH|EuGH|EuG)\b", zeile):
            continue
        if not re.search(r"\]\(https?://", zeile):
            fehler.append(
                "references/leitentscheidungen-anker.md:"
                f"{zeilennummer}: Entscheidungsanker ohne unmittelbaren Primärquellenlink: "
                f"{zeile[:160]}"
            )

    if fehler:
        print("check-rechtsprechungshygiene: FEHLER")
        for eintrag in fehler:
            print(" -", eintrag)
        return 1
    print("check-rechtsprechungshygiene OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
