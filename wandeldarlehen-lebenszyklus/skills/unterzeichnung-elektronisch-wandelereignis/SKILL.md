---
name: unterzeichnung-elektronisch-wandelereignis
description: "Unterzeichnung Elektronisch Wandelereignis: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Unterzeichnung Elektronisch Wandelereignis

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Unterzeichnung Elektronisch Wandelereignis** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `unterzeichnung-elektronisch-docusign` | Elektronische Unterzeichnung von Wandeldarlehensvertraegen und Begleitdokumenten organisieren. §§ 126a 126b BGB eIDAS-VO qualifizierte elektronische Signatur. Prüfraster: Formerfordernis je Dokument einfache QES oder qualifizierte Signatur Anbieterauswahl Nachweispflicht. Output: Unterzeichnungsplan Prozessbeschreibung. Abgrenzung: nur für elektronische Signatur; nicht für notarielle Beurkundung. |
| `wandelereignis-eingang` | Eingehende Wandelereignis-Notification prüfen und naechste Schritte bestimmen wenn Investor Wandlung ankündigt. §§ 488 ff. BGB Darlehensvertrag §§ 53 55 GmbHG. Prüfraster: Trigger-Typ Frist Preisbestimmung Erklärung Kapitalerhohungsbedarf Formerfordernisse. Output: Prüfprotokoll Massnahmenplan Fristen. Abgrenzung: nicht für Wandlungsmechanik-Konzeption (wandlungsmechanik-konzipieren). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Unterzeichnung Elektronisch Wandelereignis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `unterzeichnung-elektronisch-docusign`

**Fokus:** Elektronische Unterzeichnung von Wandeldarlehensvertraegen und Begleitdokumenten organisieren. §§ 126a 126b BGB eIDAS-VO qualifizierte elektronische Signatur. Prüfraster: Formerfordernis je Dokument einfache QES oder qualifizierte Signatur Anbieterauswahl Nachweispflicht. Output: Unterzeichnungsplan Prozessbeschreibung. Abgrenzung: nur für elektronische Signatur; nicht für notarielle Beurkundung.

# Elektronische Unterzeichnung (DocuSign / Adobe Sign)

## Zweck

Dieser Skill begleitet die elektronische Unterzeichnung des Wandeldarlehensvertrags über DocuSign oder Adobe Sign. Er stellt sicher, dass die Textform (§ 126b BGB) gewahrt ist, alle Parteien authentifiziert sind und der Audit Trail revisionssicher archiviert wird. Phase B des Lebenszyklus.

## Eingaben

- Unterzeichner (Name, E-Mail-Adresse, Mobilnummer für SMS-OTP)
- Gewünschte Authentifizierungsstufe (E-Mail-OTP, SMS-OTP, QES nach eIDAS)
- Unterzeichnungsreihenfolge (z. B. erst Gesellschaft, dann Gesellschafterinnen, zuletzt Lender)
- Frist für Unterzeichnung (z. B. sieben Bankarbeitstage)
- Archivierungspflicht: zehn Jahre für steuerrelevante Dokumente (§ 147 AO)

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform ausreichend; DocuSign erfüllt dies)
- § 126a BGB (Elektronische Form mit QES – höhere Stufe, nicht erforderlich für Wandeldarlehen)
- Art. 26 ff. eIDAS-VO 910/2014 (Anforderungen an elektronische Signaturen)
- § 147 AO (Aufbewahrungspflicht steuerrelevanter Unterlagen zehn Jahre)
- § 257 HGB (Aufbewahrungspflicht handelsrelevanter Unterlagen sechs Jahre)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Dokument vorbereiten
Endgültige PDF des Wandeldarlehensvertrags erstellen (kein DOCX an Unterzeichner senden). Alle Felder ausgefüllt, keine Platzhalter. Unterschriftsfelder positionieren (am Signaturblock).

### 2. DocuSign-Envelope erstellen
Empfängerreihenfolge: 1. Gesellschaft (Geschäftsführerin), 2. Gesellschafterin 1, 3. Gesellschafterin 2, 4. Darlehensgeber. Authentifizierung: SMS-OTP (Standard) oder eID. Ablaufdatum: sieben Bankarbeitstage.

### 3. Authentifizierungsstufen
| Stufe | Methode | Für Wandeldarlehen |
|---|---|---|
| E-Mail-OTP | Code per E-Mail | Ausreichend (Textform § 126b BGB) |
| SMS-OTP | Code per SMS | Empfohlen |
| QES (eIDAS) | Personalausweis-Online-Funktion | Nicht erforderlich, höchste Sicherheit |

### 4. Erinnerungsmanagement
Automatische Erinnerungen nach drei Tagen, nach fünf Tagen. Persönliche Nachfrage nach sieben Tagen. Ablauf-Eskalation an alle Parteien kommunizieren.

### 5. Audit Trail sichern
Nach Abschluss: Certificate of Completion (PDF mit Audit Trail) herunterladen. Zeitstempel, IP-Adressen, Authentifizierungsnachweis, Unterzeichnungschronologie. Archivieren: zehn Jahre revisionssicher (§ 147 AO).

### 6. Archivierung und Verteilung
Jede Partei erhält signiertes PDF per E-Mail (automatisch durch DocuSign). Zusätzlich: Ablage in Kanzleidokumentenmanagementsystem. Backup: mindestens zwei unabhängige Speicherorte.

## Checkliste Unterzeichnungsrunde

| Schritt | Erledigt |
|---|---|
| PDF final, keine Platzhalter | [ ] |
| Alle E-Mail-Adressen geprüft | [ ] |
| Mobilnummern für SMS-OTP vorhanden | [ ] |
| Reihenfolge korrekt konfiguriert | [ ] |
| Ablaufdatum gesetzt | [ ] |
| Erinnerungsintervalle konfiguriert | [ ] |
| Audit Trail archiviert | [ ] |
| Alle Parteien haben signiertes PDF | [ ] |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Unterzeichner nicht authentifiziert | Identitätszweifel, Anfechtungsrisiko | Nur E-Mail-OTP | SMS-OTP oder QES |
| Kein Audit Trail gespeichert | Beweisnot bei Streit | Audit Trail unvollständig | Vollständiger Trail archiviert |
| Aufbewahrung unter zehn Jahre | § 147 AO-Verstoß | Sechs Jahre | Zehn Jahre |
| Falsches Dokument (Entwurf) unterzeichnet | Streit über Vertragsinhalt | Versionsverwechslung möglich | Nur finale PDF |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/textform-vs-schriftform-vs-notariell/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandelereignis-eingang/SKILL.md`

## Quellen und Updates

Stand: 05/2026. eIDAS-VO 910/2014; § 147 AO. Bei Änderung eIDAS 2.0 (VO 2024/1183) aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 126 BGB (Schriftform) → § 126a BGB (elektronische Form, QES) → § 126b BGB (Textform) → Art. 3 Nr. 12, Art. 25, 26 eIDAS-VO (qualifizierte elektronische Signatur) → § 15 Abs. 3, 4 GmbHG (notarielle Form bei GmbH-Anteilsverträgen, kein elektronischer Ersatz)

## 2. `wandelereignis-eingang`

**Fokus:** Eingehende Wandelereignis-Notification prüfen und naechste Schritte bestimmen wenn Investor Wandlung ankündigt. §§ 488 ff. BGB Darlehensvertrag §§ 53 55 GmbHG. Prüfraster: Trigger-Typ Frist Preisbestimmung Erklärung Kapitalerhohungsbedarf Formerfordernisse. Output: Prüfprotokoll Massnahmenplan Fristen. Abgrenzung: nicht für Wandlungsmechanik-Konzeption (wandlungsmechanik-konzipieren).

# Wandelereignis – Eingang Wandlungserklärung

## Zweck

Dieser Skill strukturiert den nach Eingang der Wandlungserklärung des Lenders. Er prüft formelle Voraussetzungen, dokumentiert den Eingang und leitet den Prozess weiter. Phase C des Lebenszyklus.

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

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-qualified-financing/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlung-kommunikation-paketverteilung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB Zugangsregeln aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 488 BGB (Darlehensvertrag, Wandlungsrecht als Nebenabrede) → §§ 130, 132 BGB (Zugang der Wandlungsmitteilung) → § 280 BGB (Schadensersatz bei Verletzung Mitteilungspflicht) → § 55 GmbHG (Kapitalerhöhung nach Wandlungserklärung) → §§ 195, 199 BGB (Verjährung des Wandlungsrechts)
