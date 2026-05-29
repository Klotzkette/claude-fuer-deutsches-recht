---
name: vaf-plausibilitaetscheck
description: "Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden. §§ 305 ff. BGB Klausel-Konsistenz, § 550 BGB Schriftformhürde. Prüfraster Betraege Netto/Brutto konsistent, Fristen rechtlich zulässig, Anlagenverzeichnis vollständig, Parteidaten aktuell, Umsatzsteuer-Option konsistent. Output Plausibilitätsprotokoll mit Fehlerampel und Korrekturbedarf. Abgrenzung zu Quality-Gate für Gesamtprüfung und zu Clean-Output."
---

# Plausibilitätscheck

## Triage zu Beginn

1. Sind alle Geldbeträge konsistent (Netto + Umsatzsteuer = Brutto; Gesamtmiete = Kaltmiete + Nebenkosten)?
2. Sind alle Fristen kalendergenau und rechtlich zulässig (z.B. keine unzulässig kurzen Widerrufsfristen)?
3. Stimmen Anlagenverzeichnis und Anlagenbezugnahmen im Text überein?
4. Sind Parteidaten vollständig und aktuell (Handelsregistereintrag, Vertreter)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 551 BGB — Höchstgrenze Kaution (3 Monatskaltmieten)
- § 556 BGB — Betriebskosten Abrechnung (Jahresfrist)
- § 288 BGB — Verzugszinsen (§ 288 Abs. 1: 5 Prozentpunkte B2C; § 288 Abs. 2: 9 Prozentpunkte B2B)
- § 269 BGB — Leistungsort (relevant für Fristberechnung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

---

<!-- AUDIT 27.05.2026
Bundle: bundle_047.json
-->
