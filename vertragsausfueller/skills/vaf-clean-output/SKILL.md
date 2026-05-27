---
name: vaf-clean-output
description: "Sauberen finalen Vertragsentwurf mit Ausfüllprotokoll erstellen: Anwendungsfall alle Felder sind ausgefüllt und Quality Gate hat grüne Ampel ergeben; nun wird bereinigte Clean-Version für Unterschrift oder Versand erstellt. §§ 125 ff. BGB Schriftform, § 550 BGB bei Mietverträgen. Pruefraster alle Platzhalter aufgelöst, Anlagenverzeichnis vollstaendig, Format-Konsistenz geprueft, Track Changes entfernt. Output Clean-Entwurf mit Ausfüllprotokoll, Annahmenregister und offener-Punkte-Liste. Abgrenzung zu Quality-Gate fuer Vorabpruefung und zu Track-Changes-Skill."
---

# Clean-Output


## Triage zu Beginn

1. Sind alle Pflichtfelder gefüllt und alle Platzhalter aufgelöst?
2. Hat das Quality Gate (vaf-quality-gate) eine grüne Ampel ergeben?
3. Ist das Ausgabeformat bestimmt — Word (.docx), PDF oder beides?
4. Wird Track Changes / Redline gewünscht — wenn ja: ausdrückliche Bestätigung eingeholt?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 07.03.2005 - II ZR 194/03, NJW 2005, 2061 — Vertragstext muss aus sich heraus vollstreckbar und verständlich sein; Verweise auf externe Dokumente ohne Übergabe sind unwirksam (§ 305c BGB).
- BGH, Urt. v. 27.04.2016 - VIII ZR 61/15, NJW 2016, 1881 — AGB-Klauseln in Muster verträgen sind nach ihrem objektivierten Verständnis auszulegen; Unklarheiten gehen zu Lasten des Verwenders (§ 305c Abs. 2 BGB).
- BGH, Urt. v. 12.10.2017 - VII ZR 37/17, NJW 2018, 375 — Vergütungsklausel muss klar und bestimmt sein; pauschale Verweisung auf Preisliste ohne Übergabe genügt nicht.
- BGH, Urt. v. 25.03.2015 - VIII ZR 243/13, NJW 2015, 1510 — Salvatorische Klausel kann Teilnichtigkeit nicht heilen, wenn die unwirksame Klausel wesentlicher Bestandteil ist.

## Zentrale Normen

- § 305 BGB — Einbeziehungsvoraussetzungen AGB
- § 305c BGB — überraschende Klauseln, Unklarheitenregel
- § 126 BGB — Schriftform (wo erforderlich)
- § 127 BGB — gewillkürte Schriftform

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 305 Rn. 1-30 (Einbeziehung)
- MüKo-BGB/Basedow, 9. Aufl. 2022, § 305c Rn. 1-20 (Unklarheitenregel)

## Aufgabe

Der Skill liefert den ersten belastbaren Vertragsentwurf. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Nur freigegebene Werte einsetzen und offene Werte sichtbar markieren.
2. Ein Ausfüllprotokoll mit Quelle je Wert erzeugen.
3. Anlagenliste und Signaturblock vervollständigen.
4. Den Vertrag in einer Weise ausgeben, die in Word weiterverarbeitet werden kann.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.
