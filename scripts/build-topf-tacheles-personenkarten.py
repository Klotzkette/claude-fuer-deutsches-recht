#!/usr/bin/env python3
"""Erzeugt sieben klar fiktive Datenblätter als JPG, keine Ausweisnachbildungen."""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SLUG = "gesellschaftsgruender-topf-tacheles-berlin"


def font(size, bold=False):
    names = (["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf"] if bold else
             ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/System/Library/Fonts/Supplemental/Arial.ttf"])
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    raise RuntimeError("DejaVu Sans oder Arial wird für lesbare Datenkarten benötigt.")


def build(facts, output):
    output.mkdir(parents=True, exist_ok=True)
    ink, green, muted = "#193b32", "#dfece4", "#4e5c56"
    for index, person in enumerate(facts["personen"], start=9):
        im = Image.new("RGB", (1500, 1800), "#ffffff")
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 1500, 195), fill=ink)
        d.text((90, 48), "FIKTIVE PERSONENDATEN", font=font(53, True), fill="white")
        d.text((90, 125), "KEIN AUSWEIS - KEIN IDENTITÄTSNACHWEIS", font=font(31), fill="white")
        d.text((90, 245), "Topf & Tacheles | Gründungsvorbereitung", font=font(37, True), fill=ink)
        d.text((90, 305), "Stand: 30. September 2026", font=font(29), fill=muted)
        d.rounded_rectangle((90, 395, 330, 560), radius=15, fill=green)
        d.text((125, 445), person["id"], font=font(65, True), fill=ink)
        d.text((375, 420), "Zuordnung in den Entwürfen", font=font(29), fill=muted)
        d.text((375, 475), "Persönliche Angaben", font=font(44, True), fill=ink)

        fields = [
            ("Vorname", person["vorname"]),
            ("Nachname", person["nachname"]),
            ("Geburtsdatum", person["geburtsdatum"]),
            ("Geburtsort", person["geburtsort"]),
            ("Staatsangehörigkeit", person["staatsangehoerigkeit"]),
            ("Anschrift", person["anschrift"]),
        ]
        y = 640
        for label, value in fields:
            d.text((90, y), label.upper(), font=font(25, True), fill=muted)
            value_font = font(44)
            while d.textbbox((0, 0), value, font=value_font)[2] > 1310:
                value_font = font(value_font.size - 1)
            d.text((90, y + 43), value, font=value_font, fill=ink)
            y += 133
        d.rectangle((90, 1490, 1410, 1715), fill="#f1f5f2")
        d.text((120, 1520), "Alle Angaben auf dieser Karte sind erfunden.", font=font(32, True), fill=ink)
        d.text((120, 1585), "Datenblatt für die Vertragsbearbeitung.", font=font(30), fill=muted)
        d.text((120, 1640), "Keine amtliche Gestaltung und keine Identitätsprüfung.", font=font(30), fill=muted)
        target = output / f"{index:02d}_{person['id']}_Personendaten.jpg"
        im.save(target, format="JPEG", quality=94, subsampling=0, dpi=(200, 200))
        print(target.relative_to(ROOT) if target.is_relative_to(ROOT) else target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--facts", type=Path, default=ROOT / "scripts/data/topf-tacheles/fakten.json")
    parser.add_argument("--output", type=Path, default=ROOT / "testakten" / SLUG)
    args = parser.parse_args()
    build(json.loads(args.facts.read_text(encoding="utf-8")), args.output)
