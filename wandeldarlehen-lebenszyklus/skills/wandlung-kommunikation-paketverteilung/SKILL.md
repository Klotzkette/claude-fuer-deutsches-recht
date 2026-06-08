---
name: wandlung-kommunikation-paketverteilung
description: "Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung organisieren. §§ 130 132 BGB Zugang §§ 15 55 GmbHG. Prüfraster: Empfaengerliste Dokumente Zugang Fristen Bestätigung. Output: Kommunikationsplan Versandprotokoll. Abgrenzung: nicht für inhaltliche Prüfung der Wandlung (wandelereignis-eingang) im Wandeldarlehen Lebenszyklus."
---

# Wandlung – Kommunikation und Paketverteilung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Bestätigte Wandlungsberechnung (aus `wandlungspreis-berechnung`)
- Adressen aller Parteien (Lender, Gesellschaft, Gesellschafterinnen, Steuerberater, Buchhaltung)
- Datum der Wandlungserklärung und der Bestätigung
- Cap-Table Post-Money (aus `cap-table-update-pre-post`)
- Buchungsanweisungen: Ausbuchung Verbindlichkeit (Darlehensbetrag + Zinsen), Einbuchung Eigenkapital

## Rechtlicher Rahmen

### Primärnormen
- § 4.9 Wandeldarlehensvertrag (Gesellschaft beruft unverzüglich Gesellschafterversammlung ein)
- § 5 Wandeldarlehensvertrag (Mitwirkungspflichten Gesellschafterinnen)
- § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage nach Einlage der Forderung)
- § 246 HGB (Vollständigkeit der Buchführung)
- § 8 Wandeldarlehensvertrag (Vertraulichkeit – an wen darf kommuniziert werden?)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Bestätigungsschreiben an Lender
Inhalt: Bestätigung der Wandlungserklärung, Wandlungssumme (Darlehen + Zinsen), berechnete neue Anteile (Zahl, Nennwert), vorgesehener Termin Kapitalerhöhungsbeschluss, vorgesehener Notar.

### 2. Aufforderungsschreiben an Gesellschaft (Geschäftsführerin)
Inhalt: Einberufungspflicht gemäß § 4.9, Frist (unverzüglich, spätestens innerhalb zwei Wochen), Tagesordnungspunkte (Kapitalerhöhung gegen Sacheinlage, Bezugsrechtsverzicht, Aufnahme Lender), Notar-Beauftragung.

### 3. Schreiben an Gesellschafterinnen (Mitwirkungspflicht)
Inhalt: Hinweis auf § 5 des Wandeldarlehensvertrags (Mitwirkungspflicht), Einladung zur Gesellschafterversammlung, Beschlussthemen, Bitte um Anwesenheitsbestätigung oder Vollmacht.

### 4. Mitteilung an Steuerberater
Inhalt: Wandlungsdaten (Betrag, Datum, neue Gesellschafterstruktur), neue Cap-Table als Anlage, Bitte um steuerliche Würdigung (Wandlung als Tausch nach § 20 UmwStG analog?).

### 5. Buchungsanweisung an Buchhaltung
Soll-Buchung: Verbindlichkeit Wandeldarlehen (Darlehen + aufgelaufene Zinsen) auflösen. Haben-Buchung: Stammkapital (Nennbetrag neue Anteile) und Kapitalrücklage (Rest) erhöhen. Buchungssatz: per Verbindlichkeit Wandeldarlehen an Gezeichnetes Kapital und Kapitalrücklage.

### 6. Dokumentation und Archivierung
Alle Schreiben mit Sendenachweis archivieren (Textform-Anforderung). Kommunikationsstatus im Aktenstammblatt vermerken.

## Beispiel-Buchungssatz

```
Buchungstag: [Eintragungsdatum Handelsregister]

Soll:
 Verbindlichkeit Wandeldarlehen Northstar: EUR 275694

Haben:
 Gezeichnetes Kapital (§ 272 Abs. 1 HGB): EUR 7
 Kapitalrücklage (§ 272 Abs. 2 Nr. 4 HGB): EUR 275687
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Buchhaltung bucht Darlehen erst nach Fälligkeit aus | Bilanzunklarheit | Buchung verzögert | Buchung zeitnah mit Eintragung |
| Steuerberater nicht informiert | Steuerliche Risiken unerkannt | Informiert nach HR-Eintragung | Sofort informiert |
| Gesellschafterinnen nicht eingeladen | Mitwirkungspflicht verletzt | Einladung verspätet | Rechtzeitige Einladung |
| Kommunikation gegen Vertraulichkeitsklausel | § 8-Verstoß | Empfänger nicht § 8-berechtigt | Alle Empfänger § 8 lit. a berechtigt |

## Quellen und Updates

Stand: 05/2026. Bei Änderung HGB § 272 oder UmwStG § 20 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 47 Abs. 4 GmbHG (Stimmverbot eigene Sache) → § 40 GmbHG (Gesellschafterliste nach Wandlung) → § 53 Abs. 1 GmbHG (Zustimmung Gesellschafter zur Satzungsänderung) → § 16 GmbHG (Legitimationswirkung) → §§ 130, 132 BGB (Zugang Erklärungen)

