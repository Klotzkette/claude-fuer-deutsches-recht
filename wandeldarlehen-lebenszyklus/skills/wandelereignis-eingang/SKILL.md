---
name: wandelereignis-eingang
description: "Eingehende Wandelereignis-Notification prüfen und naechste Schritte bestimmen wenn Investor Wandlung ankündigt. §§ 488 ff. BGB Darlehensvertrag §§ 53 55 GmbHG. Prüfraster: Trigger-Typ Frist Preisbestimmung Erklärung Kapitalerhohungsbedarf Formerfordernisse. Output: Prüfprotokoll Massnahmenplan Fristen. Abgrenzung: nicht für Wandlungsmechanik-Konzeption (wandlungsmechanik-konzipieren) im Wandeldarlehen Lebenszyklus."
---

# Wandelereignis – Eingang Wandlungserklärung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Wandlungserklärung (Dokument oder E-Mail) des Lenders
- Wandeldarlehensvertrag (§§ 4.1, 4.4 zur Fristenprüfung)
- Datum der Wandlungsmitteilung der Gesellschaft (falls bereits erfolgt)
- Datum des Wandlungsereignisses (Qualified Financing, Maturity, Liquidation Event)

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform: Wandlungserklärung muss in Textform erfolgen)
- § 130 BGB (Zugang der Willenserklärung: Erklärung wirksam bei Zugang beim Empfänger)
- § 132 BGB (Zugang bei Verweigerung der Annahme)
- § 4.4 Wandeldarlehensvertrag (Frist: ein Monat nach Zugang Wandlungsmitteilung)
- § 286 BGB (Verzug bei Fristversäumnis der Gesellschaft)
- Zugangsfiktion bei einfachem Brief: seit Postrechtsmodernisierungsgesetz (PostModG, 1.1.2025) gilt regelmäßig **vier-Tage-Frist** ab Aufgabe zur Post (zuvor drei Tage); maßgeblich bei Berechnung der Wandlungsfrist, wenn Wandlungserklärung oder Wandlungsmitteilung postalisch verschickt wird

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Eingang dokumentieren
Datum und Uhrzeit des Eingangs (E-Mail-Eingang im Postfach oder Briefeingang). Screenshot oder Eingangsbestätigung erstellen. Eingangsstempel anbringen.

### 2. Formelle Prüfung (Vier-Augen-Prinzip)
a) Textform (§ 126b BGB): Ist die Erklärung in lesbarer Form auf dauerhaftem Datenträger (E-Mail, PDF)?
b) Person des Erklärenden: Ist der Lender (oder sein Bevollmächtigter) eindeutig erkennbar?
c) Inhalt: Erklärung der Wandlungsabsicht für den gesamten offenen Betrag?
d) Frist: Innerhalb eines Monats nach Zugang der Wandlungsmitteilung (§ 4.4)?
e) Empfänger: An die Gesellschaft adressiert?

### 3. Inhaltliche Vollständigkeit prüfen
Enthält die Erklärung den Wandlungsbetrag (Darlehen + Zinsen), das Wandlungsereignis und den Stichtag? Falls nicht vollständig: Rückfrage an Lender.

### 4. Eingangsbestätigung senden
Bestätigung an Lender: "Ihre Wandlungserklärung vom [Datum] ist bei uns am [Datum] eingegangen und wird geprüft." Kein Anerkenntnis inhaltlicher Berechtigung.

### 5. Interne Weiterleitung
Weitergabe an zuständige Stellen: Gesellschaft (Geschäftsführerin), Gesellschafterinnen (Mitwirkungspflicht § 5 aktivieren), Steuerberater, Buchhaltung. Fristenkalender aktualisieren.

### 6. Nächste Schritte einleiten
Je nach Trigger-Typ: Skill `wandlungspruefung-trigger-qualified-financing`, `wandlungspruefung-trigger-maturity` oder `wandlungspruefung-trigger-liquidation` aufrufen.

## Beispiel-Eingangsbestätigung

```
Betreff: Eingangsbestätigung Wandlungserklärung vom [Datum]
An: Northstar Pre-Seed Partners GmbH & Co. KG

Sehr geehrte Damen und Herren,

wir bestätigen den Eingang Ihrer Wandlungserklärung vom [Datum] per E-Mail
am [Datum, Uhrzeit]. Ihre Erklärung wird formell und inhaltlich geprüft.
Wir melden uns innerhalb von fünf Bankarbeitstagen mit dem Ergebnis.

Mit freundlichen Grüßen
Dr. Mira Schoeneck, Geschäftsführerin
Sonnenglas Solartechnologie UG (haftungsbeschränkt)
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Wandlungserklärung nach Fristablauf | Erklärung verfristet, unwirksam für dieses Ereignis | Frist grenzwertig | Innerhalb der Frist |
| Erklärung nicht in Textform | Formunwirksamkeit | Mündliche Erklärung mit schriftlicher Bestätigung | Textform gewahrt |
| Betrag fehlerhaft | Nachklärung erforderlich | Kleinere Abweichung | Betrag vollständig korrekt |
| Kein Zugang nachweisbar | Zugangsproblematik | Einwurf-Einschreiben fehlt | Zugangsbeweis vorhanden |

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB Zugangsregeln aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 488 BGB (Darlehensvertrag, Wandlungsrecht als Nebenabrede) → §§ 130, 132 BGB (Zugang der Wandlungsmitteilung) → § 280 BGB (Schadensersatz bei Verletzung Mitteilungspflicht) → § 55 GmbHG (Kapitalerhöhung nach Wandlungserklärung) → §§ 195, 199 BGB (Verjährung des Wandlungsrechts)

