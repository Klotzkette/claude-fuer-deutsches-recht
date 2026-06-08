---
name: parteien-erfassen
description: "Vertragsparteien eines Wandeldarlehens vollständig identifizieren und dokumentieren. §§ 13 17 GmbHG Gesellschafter §§ 305 ff. BGB AGB bei mehreren Darlehensgebern. Prüfraster: Darlehensgeberin Darlehensnehmerin vertretungsberechtigte Organe Handelsregisterstand. Output: Parteiendossier für Vertragskopf. Abgrenzung: Einstiegs-Skill; vor Vertragserstellung zu verwenden im Wandeldarlehen Lebenszyklus."
---

# Parteien erfassen – KYC und Vertretungsmacht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Gesellschaft: Firmenname vollständig, Rechtsform, HRB-Nummer, Amtsgericht, Sitz, Geschäftsanschrift, Name Geschäftsführerin / Geschäftsführer mit Allein- oder Gesamtvertretung
- Gesellschafterin 1: Vor- und Nachname, Geburtsdatum, Wohnanschrift, Anteilszahl und Nennwert
- Gesellschafterin 2 (falls vorhanden): gleiche Daten
- Darlehensgeber: bei Privatperson Vor- und Nachname, Geburtsdatum, Wohnanschrift; bei juristischer Person Firma, HRB, Sitz, Vertreter mit Vollmachtsnachweis
- Sanktionslistenabfrage: EU-Amtsblatt Konsolidierte Liste, OFAC SDN, UN Security Council, HM Treasury

## Rechtlicher Rahmen

### Primärnormen
- § 164 BGB (Stellvertretung), § 167 BGB (Vollmacht)
- § 35 GmbHG (Vertretung GmbH durch Geschäftsführung)
- §§ 1, 2, 3, 4, 10, 11 GwG (KYC-Pflichten, wirtschaftlich Berechtigte, PEP)
- § 19 GwG (Transparenzregister)
- § 43 GmbHG (Pflichten der Geschäftsführung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Handelsregisterauszug anfordern / prüfen
Aktueller HR-Auszug nicht älter als drei Monate: Firma, Sitz, Stammkapital, Geschäftsführung, Vertretungsregelung, aktuelle Gesellschafterliste (§ 40 GmbHG).

### 2. Gesellschafterinnen identifizieren
Abgleich mit Gesellschafterliste. Vollständige Adressen und Geburtsdaten erfassen. Privatpersonen: Personalausweis oder Reisepass als Lichtbildausweis.

### 3. Darlehensgeber-KYC
Privatperson: Lichtbildausweis + ggf. Vollmacht. Juristische Person: HR-Auszug + Vertreternachweis + Gesellschafterliste für wirtschaftlich Berechtigte (§ 3 GwG: natürliche Person mit mehr als 25 Prozent).

### 4. Sanktionslistenabfrage
Alle Parteien gegen EU-Konsolidierte Liste (Art. 2 VO 765/2006), OFAC SDN, UN-Sicherheitsratsliste und HM Treasury Financial Sanctions screenen. Ergebnis dokumentieren.

### 5. PEP-Status prüfen
Politisch exponierte Person (§ 1 Abs. 12 GwG)? Prominente Amtsträger, Familienmitglieder? Erhöhte Sorgfalt bei Treffer.

### 6. Vertragsparteien-Sektion vorbereiten
Strukturierte Textblöcke für den Vertragskopf: Gesellschaft, Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber – mit allen Pflichtangaben.

## Beispiel-Parteiblock (DE)

```
(1) Sonnenglas Solartechnologie UG (haftungsbeschränkt)
 Geschäftsanschrift: Musterstraße 12, 10115 Berlin
 eingetragen im Handelsregister des Amtsgerichts Charlottenburg unter HRB 123456 B,
 vertreten durch ihre alleinvertretungsberechtigte Geschäftsführerin Dr. Mira Schoeneck,
 – nachstehend die "Gesellschaft" –

(2) Dr. Mira Schoeneck, geboren [Datum], Musterstraße 12, 10115 Berlin
 – nachstehend die "Gesellschafterin 1" –

(3) Lina Habersaat, geboren [Datum], Beispielweg 5, 20095 Hamburg
 – nachstehend die "Gesellschafterin 2" –

(4) Northstar Pre-Seed Partners GmbH & Co. KG
 Geschäftsanschrift: Venture-Allee 1, 60329 Frankfurt am Main
 eingetragen im Handelsregister des Amtsgerichts Frankfurt am Main unter HRA 99999,
 vertreten durch ihre Komplementärin Northstar Management GmbH, diese vertreten durch [●]
 – nachstehend der "Darlehensgeber" –
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sanktionslistentreffer | Vertrag nicht abschließen | Namensähnlichkeit ohne Treffer | Alle Checks negativ |
| PEP-Status | Verstärkte Sorgfaltspflichten, ggf. GF-Freigabe | Familienmitglied PEP | Kein PEP |
| Vollmacht fehlt | Vertrag schwebend unwirksam | Vollmacht in Vorbereitung | Vollmacht vorgelegt |
| HR-Auszug veraltet (über 3 Monate) | Vertretungsrisiko | 3 bis 6 Monate alt | Aktuell |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GwG/GmbHG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 10, 11 GwG (Identifizierung wirtschaftlich Berechtigter) → §§ 18, 19 GwG (Transparenzregister) → § 40 GmbHG (Gesellschafterliste: Angaben Gesellschafter) → § 15 GmbHG (Abtretung, Übergang Anteile) → § 313 BGB (Identitätsbezeichnung in notariellen Urkunden)

