---
name: vaf-plausibilitaetscheck
description: "Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden. §§ 305 ff. BGB Klausel-Konsistenz, § 550 BGB Schriftformhürde. Pruefraster Betraege Netto/Brutto konsistent, Fristen rechtlich zulässig, Anlagenverzeichnis vollständig, Parteidaten aktuell, Umsatzsteuer-Option konsistent. Output Plausibilitätsprotokoll mit Fehlerampel und Korrekturbedarf. Abgrenzung zu Quality-Gate fuer Gesamtpruefung und zu Clean-Output."
---

# Plausibilitätscheck


## Triage zu Beginn

1. Sind alle Geldbeträge konsistent (Netto + Umsatzsteuer = Brutto; Gesamtmiete = Kaltmiete + Nebenkosten)?
2. Sind alle Fristen kalendergenau und rechtlich zulässig (z.B. keine unzulässig kurzen Widerrufsfristen)?
3. Stimmen Anlagenverzeichnis und Anlagenbezugnahmen im Text überein?
4. Sind Parteidaten vollständig und aktuell (Handelsregistereintrag, Vertreter)?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 10.11.2009 - VIII ZR 318/08, NJW 2010, 337 — Nebenkosten in Mietverträgen: Abrechnungspflicht erfordert korrekte Gesamtbeträge; Rechenfehler in Nebenkostenabrechnung führen zu Unwirksamkeit.
- BGH, Urt. v. 23.09.2009 - VIII ZR 300/08, NJW 2010, 1 — Fristen für Betriebskostenabrechnung (§ 556 Abs. 3 BGB): Einhaltung der Jahresfrist; verspätete Abrechnung verwirkt Nachforderungsrecht.
- BGH, Urt. v. 25.07.2012 - VIII ZR 143/11, NJW 2012, 3029 — Kaution: mehr als 3 Monatskaltmieten unzulässig (§ 551 BGB); Plausibilitätsprüfung zwingend.
- BGH, Urt. v. 19.09.2018 - XII ZR 69/17, NJW 2019, 51 — Schriftformheilung in Gewerbemietvertrag: Nachtragsvereinbarung muss Bezug auf Hauptvertrag enthalten.

## Zentrale Normen

- § 551 BGB — Höchstgrenze Kaution (3 Monatskaltmieten)
- § 556 BGB — Betriebskosten Abrechnung (Jahresfrist)
- § 288 BGB — Verzugszinsen (§ 288 Abs. 1: 5 Prozentpunkte B2C; § 288 Abs. 2: 9 Prozentpunkte B2B)
- § 269 BGB — Leistungsort (relevant für Fristberechnung)

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. 2022, § 551 Rn. 1-20 (Kaution)
- Grüneberg, BGB, 83. Aufl. 2024, § 288 Rn. 1-15 (Verzugszinsen)

## Aufgabe

Der Skill härtet den Entwurf vor Versand oder Verhandlung. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Gesamtmiete gegen Kaltmiete und Nebenkosten rechnen.
2. Kaution gegen Monatsmieten, Mietbeginn gegen Laufzeitende und Optionsfristen prüfen.
3. Verweise auf Anlagen, Klauseln und Signaturblöcke kontrollieren.
4. Unplausibles als rote Rückfrage markieren, nicht still korrigieren.

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
