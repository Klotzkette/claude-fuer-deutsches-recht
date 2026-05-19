#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plugin_aus_hausregeln.py — Plugin-Generator der Klagewerkstatt.

Packt aus den im Lernlauf gewonnenen Hausregeln (`hausregeln.json`) und der
hauseigenen Standardvorlage (`standardklage.md`) ein eigenständiges, in
Claude Code direkt installierbares Mini-Plugin als ZIP-Datei.

Aufruf:
    python scripts/plugin_aus_hausregeln.py \
        --kanzlei "Kanzlei Mustermann" \
        --vorlage assets/vorlagen-leer/standardklage.md \
        --regeln  hausregeln.json \
        --ziel    /pfad/klagewerkstatt-mustermann.zip

Layout des erzeugten Plugins:

    klagewerkstatt-<slug>/
        .claude-plugin/plugin.json
        skills/klage-erstellen/SKILL.md
        assets/vorlage/standardklage.md
        references/hausregeln.json
        references/belegmuster.md
        references/anlagenliste.md
        references/zustaendigkeit-quellen.md
        README.md

Lizenz: Apache-2.0 OR MIT (Auswahl beim Empfänger). Autor: Klotzkette.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import zipfile
from datetime import date
from pathlib import Path


# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------


def slugify(name: str) -> str:
    """Erzeugt einen URL-/Plugin-tauglichen Kurznamen aus einem Kanzleinamen."""
    s = name.strip().lower()
    s = re.sub(r"[äÄ]", "ae", s)
    s = re.sub(r"[öÖ]", "oe", s)
    s = re.sub(r"[üÜ]", "ue", s)
    s = re.sub(r"[ß]", "ss", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "kanzlei"


def lese_json(pfad: Path) -> dict:
    if not pfad.exists():
        raise SystemExit(f"Hausregeln nicht gefunden: {pfad}")
    try:
        return json.loads(pfad.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise SystemExit(f"Hausregeln {pfad} sind kein gültiges JSON: {err}")


def lese_text(pfad: Path) -> str:
    if not pfad.exists():
        raise SystemExit(f"Vorlage nicht gefunden: {pfad}")
    return pfad.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Dateiinhalte für das erzeugte Plugin
# ---------------------------------------------------------------------------


def plugin_json(slug: str, kanzlei: str) -> str:
    manifest = {
        "name": f"klagewerkstatt-{slug}",
        "version": "0.1.0",
        "description": (
            f"Hauseigenes Klage-Plugin der Kanzlei {kanzlei}. "
            "Erzeugt aus der eigenen Standardvorlage und den extrahierten Hausregeln "
            "durch die Klagewerkstatt (forderungsmanagement-klagewerkstatt). "
            "Nimmt im Laufzeitbetrieb nur noch Sachverhalt und Beklagtenadresse entgegen, "
            "prüft online die sachliche und örtliche Zuständigkeit "
            "(justizadressen.nrw.de und justiz.de Gerichtssuche; "
            "§§ 12, 13, 29, 29c ZPO; §§ 23, 71 GVG) und liefert die fertige "
            "Klageschrift als DOCX und Markdown in der hauseigenen Formatvorlage."
        ),
        "license": "Apache-2.0 OR MIT",
        "author": {"name": "Klotzkette"},
        "homepage": "https://github.com/Klotzkette/claude-fuer-deutsches-recht",
        "keywords": [
            "klage",
            "forderungsmanagement",
            "inkasso",
            "zpo",
            "klagewerkstatt",
            "hauskanzlei",
            "bea",
            "zustaendigkeit",
            slug,
        ],
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def skill_md(slug: str, kanzlei: str, regeln: dict) -> str:
    zinsantrag_b2b = regeln.get("standardklauseln", {}).get(
        "zinsantrag_b2b", "9 Prozentpunkte über Basiszinssatz, § 288 Abs. 2 BGB"
    )
    zinsantrag_b2c = regeln.get("standardklauseln", {}).get(
        "zinsantrag_b2c", "5 Prozentpunkte über Basiszinssatz, § 288 Abs. 1 BGB"
    )
    anlagensigel = regeln.get("stil", {}).get("anlagensigel", "K")
    return f"""---
name: klage-erstellen
description: Hauseigener Klage-Skill der Kanzlei {kanzlei}. Erzeugt Forderungsklagen direkt in der hauseigenen Standardvorlage. Nimmt nur Sachverhalt und Beklagtenadresse entgegen, prüft online die sachliche und örtliche Zuständigkeit (justizadressen.nrw.de und justiz.de Gerichtssuche; §§ 12, 13, 29, 29c ZPO; §§ 23, 71 GVG), füllt die hinterlegte Vorlage und liefert die Klageschrift als DOCX und Markdown. Keine Extraktion, kein Lernlauf.
language: de
license: Apache-2.0 OR MIT
when_to_use: |
  Trigger phrases and example requests:
  - neue Klage in Hausvorlage {kanzlei}
  - Forderungsklage erstellen
  - Klage in unserer Standardvorlage
  - Inkasso-Klage ohne Lernlauf
  - {slug} klage
---

# Klage-Erstellen — {kanzlei}

## Zweck

Hauseigener Laufzeit-Skill. Setzt die Hausregeln und die Standardvorlage der
Kanzlei {kanzlei} fest verdrahtet voraus. Erzeugt aus Sachverhalt und
Beklagtenadresse eine vollständige Forderungsklage in der hauseigenen Form.

## Ablauf

**1. Sachverhalt einsammeln (eine Liste, einmal):**

- Forderungsgrund (Kauf, Werkvertrag, Dienstvertrag, Darlehen, Miete, sonstiges)
  mit kurzer Vertragsbeschreibung.
- Beklagte(r): Name, Anschrift, Rechtsform, ggf. gesetzliche Vertretung;
  **Anschrift exakt** für die Zuständigkeitsprüfung.
- Hauptforderung in EUR, Fälligkeitsdatum, etwaige Teilzahlungen.
- Mahnungen mit Datum und Inhalt; Mahnverzugseintritt.
- Vorgerichtliche Rechtsanwaltskosten als Nebenforderung
  (Geschäftsgebühr Nr. 2300 VV RVG, Anrechnung Vorbem. 3 Abs. 4 VV RVG).
- Beweismittel (Urkunden, Zeugen, Sachverständige, Parteivernehmung).
- Besonderheiten: Verbraucher (§ 29c ZPO), AGB-Gerichtsstand (§ 38 ZPO),
  Erfüllungsort (§ 29 ZPO), grenzüberschreitender Bezug (Brüssel Ia VO).

Dokumenten-Drop akzeptieren (Rechnungen, Mahnungen, Korrespondenz) und
Felder automatisch belegen.

**2. Zuständigkeit online prüfen (Pflicht):**

1. **Sachlich** rechnerisch: ≤ 5.000 EUR → AG (§ 23 Nr. 1 GVG);
   > 5.000 EUR → LG (§ 71 GVG). Sondertatbestände beachten
   (Wohnraummiete § 23 Nr. 2a GVG; Handelssachen §§ 95, 96 GVG).
2. **Örtlich** rechtlich: §§ 12, 13 ZPO Allgemeiner Gerichtsstand;
   § 29 ZPO Erfüllungsort; § 29c ZPO Verbraucherverträge;
   § 38 ZPO Gerichtsstandsvereinbarung (gegenüber Verbrauchern unwirksam).
3. **Online-Adressrecherche** (immer ausführen):
   - `pplx content fetch "https://www.justizadressen.nrw.de/de/justiz/suche?suchbegriff=<PLZ_oder_Ort>"`
   - bundesweit `pplx content fetch "https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php"`
   - Treffer übernehmen: Bezeichnung, Postanschrift, ggf. BeA-SAFE-ID
     (sonst Hinweis: „über beA-Adressbuch nachtragen").
4. Quelle und Abrufdatum in Anlage **Zuständigkeitsprüfung** dokumentieren.

**3. Klage erzeugen:**

- Vorlage `assets/vorlage/standardklage.md` befüllen.
- DOCX über `office/docx` rendern. Dateiname `Klage-<Beklagte>-<YYYYMMDD>.docx`.
- Anlagenliste aus `references/anlagenliste.md`; Sigel `{anlagensigel}1`, `{anlagensigel}2`, …
- Zinsantrag: B2B `{zinsantrag_b2b}`; B2C `{zinsantrag_b2c}`.

**4. Memo (nur auf Anfrage):**

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Anspruchsgrundlagen,
> Beweislage und Prozessrisiken erstellen?

## Rechtlicher Rahmen

- **Pflichtinhalte**: § 253 ZPO; **Form**: §§ 130, 130a, 130d ZPO (beA-Pflicht
  für Rechtsanwältinnen und Rechtsanwälte); **Anwaltszwang**: § 78 ZPO.
- **Sachliche Zuständigkeit**: §§ 23, 71 GVG.
- **Örtliche Zuständigkeit**: §§ 12, 13, 17, 24, 29, 29c, 38 ZPO; grenzüber-
  schreitend Brüssel Ia VO (EU) 1215/2012, insb. Art. 7 Nr. 1.
- **Anspruchsgrundlagen** (Auswahl): §§ 433 II, 535 II, 488, 611a II, 631 I BGB.
- **Verzug**: §§ 286, 288 BGB; **RA-Kosten als Verzugsschaden**: § 280 BGB.

## Leitentscheidungen (siehe `references/belegmuster.md`)

- BGH, Urt. v. 25.06.2020 – VII ZR 308/19, NJW 2020, 2884
- BGH, Urt. v. 22.01.2008 – VIII ZR 6/06, NJW 2008, 1888
- BGH, Urt. v. 04.10.2007 – III ZR 180/06, NJW 2008, 50
- BGH, Beschl. v. 23.06.2022 – V ZB 12/22
- BGH, Beschl. v. 31.01.2023 – XI ZB 23/22

## Ausgabeformat

1. Klageschrift als DOCX (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und Markdown-Spiegel.
2. Anlage Zuständigkeitsprüfung mit Online-Quellen und Abrufdatum.
3. Memo nur auf Anfrage.

## Übergabe

- Bei drohender Zahlungsunfähigkeit der Beklagten an Liquiditätsplanung (`liquiditaetsplanung`).
- Bei einstweiligem Rechtsschutz / Mahnverfahren an `prozessrecht`.
- Wenn die Hausvorlage veraltet wirkt, zurück an den Schwester-Skill
  `klagevorlage-aus-eigenen-mustern` im Plugin `forderungsmanagement-klagewerkstatt`
  zum aktualisierten Lernlauf.
"""


def belegmuster_md(regeln: dict) -> str:
    sb = regeln.get("standardbeleg", {})
    zeilen = ["# Belegmuster — hauseigene Standardfundstellen", ""]
    for thema, beleg in sb.items():
        zeilen.append(f"- **{thema}**: {beleg}")
    zeilen.extend(
        [
            "",
            "## Weitere Leitentscheidungen",
            "",
            "- BGH, Urt. v. 25.06.2020 – VII ZR 308/19, NJW 2020, 2884 (§ 288 Abs. 5 BGB).",
            "- BGH, Urt. v. 22.01.2008 – VIII ZR 6/06, NJW 2008, 1888 (RA-Kosten als Verzugsschaden).",
            "- BGH, Urt. v. 04.10.2007 – III ZR 180/06, NJW 2008, 50 (Mahnung).",
            "- BGH, Beschl. v. 23.06.2022 – V ZB 12/22 (§ 130a ZPO).",
            "- BGH, Beschl. v. 31.01.2023 – XI ZB 23/22 (beA-Sorgfalt).",
            "- BGH, Urt. v. 22.04.2009 – VIII ZR 156/07, NJW 2009, 2197 (Erfüllungsort § 29 ZPO).",
            "- EuGH, Urt. v. 14.09.2023 – C-393/22 (Art. 7 Nr. 1 lit. b Brüssel Ia VO).",
            "",
            "Pinpoint-Zitat mit Randnummer; jüngere Entscheidungen zuerst.",
            "",
        ]
    )
    return "\n".join(zeilen)


def anlagenliste_md(regeln: dict) -> str:
    sigel = regeln.get("stil", {}).get("anlagensigel", "K")
    eintraege = regeln.get("anlagen_default", []) or [
        "Rechnung mit Fälligkeit",
        "1. Mahnung",
        "2. Mahnung mit Frist und Verzugsfolgenhinweis",
        "Auftragsbestätigung / Vertrag",
        "Lieferschein / Leistungsnachweis",
        "AGB (sofern einbezogen)",
    ]
    zeilen = ["# Anlagenliste — Standard der Kanzlei", ""]
    for i, e in enumerate(eintraege, 1):
        zeilen.append(f"- **{sigel}{i}** {e}")
    zeilen.extend(
        [
            "",
            "Reihenfolge an den Sachverhalt anpassen; weitere Anlagen fortlaufend nummerieren.",
            "",
        ]
    )
    return "\n".join(zeilen)


def zustaendigkeit_quellen_md(regeln: dict) -> str:
    z = regeln.get("zustaendigkeit", {}) or {}
    primaer = z.get("quelle_primaer", "https://www.justizadressen.nrw.de/de/justiz/suche")
    bund = z.get(
        "quelle_bundesweit",
        "https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php",
    )
    return f"""# Online-Quellen für die Zuständigkeitsprüfung

Pflicht in jedem Klagelauf. Beide Quellen abrufen und das Abrufdatum dokumentieren.

## Primärquelle

- **Justiz-Adressen NRW**: <{primaer}>
  - Suchfeld PLZ oder Ortsname der Beklagten-Anschrift.
  - Liefert zuständiges Amtsgericht, Landgericht, Oberlandesgericht,
    Staatsanwaltschaft samt Postanschrift.

## Bundesweit ergänzend

- **Justizportal Gerichtsverzeichnis**: <{bund}>
- **Bundeseinheitliche Mahngerichte**: <https://www.mahngerichte.de>

## BeA-EGVP-Adressbuch (SAFE-ID)

Die SAFE-ID des Empfangsgerichts wird im **beA-Adressbuch** geführt. Bei
elektronischer Einreichung (§ 130d ZPO) wird sie beim Versand aus beA gewählt;
in der Klage genügt regelmäßig die Postanschrift. Falls eine SAFE-ID nicht
öffentlich gelistet ist, im Output mit dem Hinweis
„über beA-Adressbuch zu ergänzen" markieren.
"""


def readme_md(slug: str, kanzlei: str) -> str:
    heute = date.today().isoformat()
    return f"""# Klagewerkstatt — {kanzlei}

Hauseigenes Klage-Plugin. Erzeugt aus der eigenen Standardvorlage und den
extrahierten Hausregeln direkt die nächste Forderungsklage in der gewohnten
Formatvorlage.

**Erzeugt am:** {heute}
**Quelle:** Klagewerkstatt (forderungsmanagement-klagewerkstatt) der
[Klotzkette German Legal Skills](https://github.com/Klotzkette/claude-fuer-deutsches-recht).

## Installation in Claude Code

1. Diese ZIP-Datei (`klagewerkstatt-{slug}.zip`) herunterladen.
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skill `klage-erstellen` ist sofort verfügbar.

## Verwendung

> „Neue Forderungsklage in Hausvorlage."

Das Plugin fragt dann strukturiert nach Sachverhalt und Beklagtenadresse, prüft
**online** sachliche und örtliche Zuständigkeit über
[justizadressen.nrw.de](https://www.justizadressen.nrw.de/de/justiz/suche) und
das bundesweite [Justizportal](https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php)
und liefert die fertige Klageschrift als DOCX und Markdown.

## Inhalt

- `.claude-plugin/plugin.json`
- `skills/klage-erstellen/SKILL.md`
- `assets/vorlage/standardklage.md`
- `references/hausregeln.json`
- `references/belegmuster.md`
- `references/anlagenliste.md`
- `references/zustaendigkeit-quellen.md`

## Pflege

Wenn sich Standardklauseln, Belegmuster oder Layout ändern: einfach den
Lernlauf-Skill `klagevorlage-aus-eigenen-mustern` im Mutter-Plugin neu starten
und das aktualisierte ZIP überschreibend installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.
"""


# ---------------------------------------------------------------------------
# ZIP-Aufbau
# ---------------------------------------------------------------------------


def baue_zip(
    ziel: Path,
    slug: str,
    kanzlei: str,
    regeln: dict,
    vorlage_text: str,
) -> None:
    base = f"klagewerkstatt-{slug}"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as zf:
        def add(name: str, data: str) -> None:
            zf.writestr(f"{base}/{name}", data)

        add(".claude-plugin/plugin.json", plugin_json(slug, kanzlei))
        add("skills/klage-erstellen/SKILL.md", skill_md(slug, kanzlei, regeln))
        add("assets/vorlage/standardklage.md", vorlage_text)
        add(
            "references/hausregeln.json",
            json.dumps(regeln, ensure_ascii=False, indent=2) + "\n",
        )
        add("references/belegmuster.md", belegmuster_md(regeln))
        add("references/anlagenliste.md", anlagenliste_md(regeln))
        add("references/zustaendigkeit-quellen.md", zustaendigkeit_quellen_md(regeln))
        add("README.md", readme_md(slug, kanzlei))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Generiert ein hauseigenes Klage-Plugin als ZIP.",
    )
    ap.add_argument("--kanzlei", required=True, help="Kanzleiname (z. B. 'Kanzlei Mustermann').")
    ap.add_argument("--vorlage", required=True, type=Path, help="Pfad zur Standardvorlage (.md).")
    ap.add_argument("--regeln", required=True, type=Path, help="Pfad zur hausregeln.json.")
    ap.add_argument("--ziel", required=True, type=Path, help="Pfad zur Ausgabe-ZIP.")
    ap.add_argument(
        "--slug",
        default=None,
        help="Optionaler Slug. Default: aus --kanzlei abgeleitet.",
    )
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    regeln = lese_json(args.regeln)
    vorlage_text = lese_text(args.vorlage)
    slug = args.slug or slugify(args.kanzlei)
    baue_zip(args.ziel, slug, args.kanzlei, regeln, vorlage_text)
    print(f"OK: {args.ziel} (klagewerkstatt-{slug}.zip-Struktur)")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
