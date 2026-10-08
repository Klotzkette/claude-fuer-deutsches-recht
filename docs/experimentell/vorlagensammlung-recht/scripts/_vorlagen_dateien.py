"""Gemeinsamer Helper: findet die sprechende MD- und ODT-Datei einer Vorlage.

Repo-Regel ab Juni 2026: Jede Vorlage liegt in genau einem Unterordner und
trägt den Unterordner-Slug als Dateistamm, etwa
`grundschuldbestellung-notariell.md` und
`grundschuldbestellung-notariell.odt`.

Generische Dateinamen wie `vertrag.md`, `text.odt`, `vorlage.md`,
`VORLAGE.odt`, `SKILL.md` oder `SkillMD` sind für Vorlagen nicht zulässig.
"""
from __future__ import annotations
from pathlib import Path

THEMENORDNER = (
    "agb-recht",
    "allgemeines-und-bereichsuebergreifendes",
    "arbeitsrecht",
    "aufsichtsrecht-und-bafin",
    "bank-und-kapitalmarktrecht",
    "bau-und-architektenrecht",
    "beamten-und-soldatenrecht",
    "erbrecht",
    "europarecht",
    "familienrecht",
    "gewerblicher-rechtsschutz",
    "handels-und-gesellschaftsrecht",
    "informationstechnologierecht",
    "insolvenzrecht",
    "internationales-wirtschaftsrecht",
    "kartell-und-marktrecht",
    "medizinrecht",
    "mietrecht-und-wohnungseigentumsrecht",
    "migrationsrecht",
    "oeffentliches-baurecht",
    "restrukturierungsrecht-starug",
    "sozialrecht",
    "sportrecht",
    "steuerrecht",
    "strafrecht",
    "strafvollzugsrecht",
    "transport-und-speditionsrecht",
    "urheber-und-medienrecht",
    "verfassungsrecht",
    "vergaberecht",
    "verkehrsrecht",
    "versicherungsrecht",
    "verwaltungsrecht",
    "weltraumrecht",
    "zoll-und-aussenwirtschaftsrecht",
    "energierecht",
    "umweltrecht-und-emissionshandel",
    "vertriebs-und-handelsrecht",
    "mergers-and-acquisitions",
    "ki-und-plattformregulierung",
    "prozessvorlagen",
)

ALTE_INHALTSTYPEN = (
    "vertrag", "antrag", "klage", "schreiben", "erklaerung", "protokoll",
    "text", "beschluss", "bogen", "zeugnis", "rechnung", "plan",
    "vermerk", "testament", "plaedoyer", "frachtbrief", "bericht",
    "ladungsschein",
)

GENERISCHE_STEMS = {s.lower() for s in ALTE_INHALTSTYPEN} | {
    "vorlage", "vorschlag", "muster", "template", "skill", "skillmd",
    "skill-md", "skill_md",
}

# Rückwärtskompatibler Export für ältere Hilfsskripte. Neue Checks dürfen
# diese Liste nicht mehr als zulässige Vorlagendateinamen verstehen.
INHALTSTYPEN = ALTE_INHALTSTYPEN


def ist_generischer_stem(stem: str) -> bool:
    return stem.lower() in GENERISCHE_STEMS


def md_in(ordner: Path) -> Path | None:
    """Liefert die eine Vorlagen-Markdown-Datei im Ordner oder None."""
    cand = list(ordner.glob("*.md"))
    cand = [p for p in cand if p.name not in ("README.md",)]
    return cand[0] if len(cand) == 1 else None


def odt_in(ordner: Path) -> Path | None:
    """Liefert die zur Markdown-Datei gehörende ODT-Datei oder None."""
    md = md_in(ordner)
    if md is not None:
        p = md.with_suffix(".odt")
        if p.is_file():
            return p
    cand = list(ordner.glob("*.odt"))
    return cand[0] if len(cand) == 1 else None


def ist_vorlagen_ordner(ordner: Path) -> bool:
    return md_in(ordner) is not None


def _wirkt_wie_vorlagenordner(ordner: Path) -> bool:
    """Erkennt Vorlagenordner auch dann, wenn ihre Struktur noch defekt ist."""
    if not ordner.is_dir():
        return False
    return any(
        pfad.is_file()
        and (
            (pfad.suffix == ".md" and pfad.name != "README.md")
            or pfad.suffix == ".odt"
            or pfad.name.endswith(".md.zip")
            or pfad.name == "rubric.yaml"
        )
        for pfad in ordner.iterdir()
    )


def pruefe_bestandsstruktur(repo: Path) -> None:
    """Verhindert, dass Bestandsverbraucher ganze Bereiche still auslassen."""
    fehlend = [
        name
        for name in THEMENORDNER
        if not (repo / name).is_dir() or (repo / name).is_symlink()
    ]
    if fehlend:
        raise RuntimeError(
            "Kanonische Themenordner fehlen: " + ", ".join(fehlend)
        )

    unerwartet: list[str] = []
    for wurzel in sorted(pfad for pfad in repo.iterdir() if pfad.is_dir()):
        if (
            wurzel.name in THEMENORDNER
            or wurzel.name == "vorlagen-gerichtsleitend"
            or wurzel.name.startswith(".")
        ):
            continue
        if any(
            _wirkt_wie_vorlagenordner(kind)
            for kind in wurzel.iterdir()
            if kind.is_dir()
        ):
            unerwartet.append(wurzel.name)
    if unerwartet:
        raise RuntimeError(
            "Vorlagen liegen außerhalb der kanonischen Themenliste: "
            + ", ".join(unerwartet)
        )


def themenpfade(repo: Path) -> list[Path]:
    """Liefert die vorhandenen Hauptthemen in stabiler Reihenfolge.

    Die Top-Level-Struktur enthält auch Werkzeuge, Indizes und Sonderbereiche.
    Bestandsscripte dürfen deshalb nicht durch eigene Ausschlusslisten erraten,
    welche Ordner Hauptvorlagen enthalten. `THEMENORDNER` ist die einzige
    kanonische Quelle.
    """
    pruefe_bestandsstruktur(repo)
    return [repo / name for name in THEMENORDNER]


def vorlagenordner(repo: Path) -> list[Path]:
    """Liefert sämtliche Hauptvorlagenordner aus den kanonischen Themen."""
    ergebnis: list[Path] = []
    for bereich in themenpfade(repo):
        for ordner in sorted(pfad for pfad in bereich.iterdir() if pfad.is_dir()):
            if ordner.is_symlink():
                raise RuntimeError(
                    f"Vorlagenordner darf kein symbolischer Link sein: "
                    f"{ordner.relative_to(repo)}"
                )
            verknuepfungen = sorted(
                pfad.name for pfad in ordner.iterdir() if pfad.is_symlink()
            )
            if verknuepfungen:
                raise RuntimeError(
                    f"Vorlagendateien dürfen keine symbolischen Links sein: "
                    f"{ordner.relative_to(repo)} ({', '.join(verknuepfungen)})"
                )
            erwartet = ordner / f"{ordner.name}.md"
            markdown_dateien = sorted(
                pfad for pfad in ordner.glob("*.md") if pfad.name != "README.md"
            )
            if markdown_dateien != [erwartet]:
                gefunden = ", ".join(pfad.name for pfad in markdown_dateien) or "keine"
                raise RuntimeError(
                    f"Uneindeutige Vorlagenquelle in {ordner.relative_to(repo)}: "
                    f"erwartet {erwartet.name}, gefunden {gefunden}"
                )
            ergebnis.append(ordner)
    return ergebnis
