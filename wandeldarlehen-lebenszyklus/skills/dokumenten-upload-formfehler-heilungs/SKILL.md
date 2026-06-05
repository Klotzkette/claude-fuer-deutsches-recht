---
name: dokumenten-upload-formfehler-heilungs
description: "Dokumenten Upload Formfehler Heilungs: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dokumenten Upload Formfehler Heilungs

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Dokumenten Upload Formfehler Heilungs** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dokumenten-upload-extraktion` | Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger Laufzeit Sonderrechte. Output: strukturiertes Datenmemo mit Extraktionsergebnis. Abgrenzung: Extraktion und Triage; Detailprüfung in Spezialist-Skills. |
| `formfehler-heilungs-timeline` | Formfehler in Wandeldarlehen oder Kapitalerhohungsdokumenten identifizieren und Heilungsmassnahmen planen. §§ 125 311b BGB Nichtigkeit §§ 15 55 GmbHG Formerfordernisse. Prüfraster: Formmangel Nichtigkeit Heilung Nachbeurkundung Fristen. Output: Fehlerliste Heilungsplan Fristenkalender. Abgrenzung: nicht für allgemeine Beurkundungsprüfung (beurkundungserfordernis-prüfung). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Dokumenten Upload Formfehler Heilungs**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dokumenten-upload-extraktion`

**Fokus:** Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger Laufzeit Sonderrechte. Output: strukturiertes Datenmemo mit Extraktionsergebnis. Abgrenzung: Extraktion und Triage; Detailprüfung in Spezialist-Skills.

# Dokumenten-Upload und Datenextraktion

## Zweck

Dieser Skill extrahiert aus hochgeladenen Transaktionsdokumenten (Term Sheet, SPA, IRA, SHA) alle für die Wandlungsrechnung relevanten Zahlen und Parameter. Phase C des Lebenszyklus.

## Eingaben

- Hochgeladene Dokumente: Term Sheet, Share Purchase Agreement (SPA), Investor Rights Agreement (IRA), Shareholders Agreement (SHA), Beteiligungsvertrag
- Gesuchte Parameter: Pre-Money, Post-Money, Investitionsvolumen, Anteilsklassen, Nennwert, Vesting, ESOP, Liquidationspräferenzen, Anti-Dilution

## Rechtlicher Rahmen

### Primärnormen
- § 15 GmbHG (Anteilsklassen und Übertragung)
- § 272 HGB (Eigenkapitalausweis nach Klassen)
- § 194 AktG analog (Wandelschuldverschreibungen und Klassen – Orientierung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Dokumententyp identifizieren
Term Sheet: Enthält Rahmenbedingungen (Pre-Money, Anteilsklassen, Liquidationspräferenz, Anti-Dilution, ESOP, Board-Rechte). SPA: Enthält Kaufpreis (als Post-Money oder implizit), Warranties, CP-Liste. IRA/SHA: Enthält Informationsrechte, Vetorechte, Drag-Along/Tag-Along.

### 2. Pre-Money-Bewertung extrahieren
Suche nach "pre-money valuation", "Pre-Money-Bewertung", "company valuation before investment". Umrechnung falls nur Post-Money angegeben: Pre-Money = Post-Money − Investitionsvolumen.

### 3. Investitionsvolumen extrahieren
"Investment amount", "aggregate investment", "total subscription amount". Achtung: Aufteilen nach Investorengruppen falls mehrere.

### 4. Anteilsklassen extrahieren
Bestehende und neue Anteilsklassen (Ordinary Shares, Preferred Shares A, B). Wandlungsrechte, Liquidationspräferenzen je Klasse, Dividendenpräferenzen. Einfluss auf vollverwässerte Anteile.

### 5. ESOP-Pool extrahieren
"Employee Option Pool", "Management Option Programme". Größe in Anteilen oder Prozent. Vor- oder nach-Kapitalerhöhung? (Beeinflusst vollverwässerte Basis für Wandlungspreis).

### 6. Strukturierten Extrakt ausgeben
Tabelle mit allen extrahierten Werten, Quellenangabe (Dokument, Seite, Klausel), offene Fragen markiert. Übergabe an `wandlungspreis-berechnung`.

## Beispiel-Extrakt Term Sheet

| Parameter | Wert | Quelle |
|---|---|---|
| Pre-Money-Bewertung | EUR 6000000 | Term Sheet Cl. 2.1 |
| Investitionsvolumen | EUR 1000000 | Term Sheet Cl. 2.1 |
| Anteilsklassen | Ordinary + Series A Preferred | Term Sheet Cl. 3 |
| Liquidationspräferenz Series A | 1x non-participating | Term Sheet Cl. 4 |
| ESOP-Pool | zehn Prozent (post-money) | Term Sheet Cl. 5 |
| Anti-Dilution | Broad-based weighted average | Term Sheet Cl. 6 |
| Qualifiziertes Financing nach WDV | Pre-Money ≥ EUR 4 Mio, Vol. ≥ EUR 500000 | WDV § 4.2 lit. a |
| Ist Qualified Financing? | Ja (beide Schwellen erfüllt) | Prüfung |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Term Sheet nur als Absichtserklärung | Zahlen unverbindlich | Term Sheet mit Bindungswirkung unklar | Verbindliches Term Sheet |
| ESOP-Pool post-money ohne Klarstellung | Vollverwässerte Basis falsch berechnet | Unklar ob pre/post | Eindeutig pre-money |
| Liquidationspräferenz höher als 1x | Lender-Barausschüttung bevorzugt | Participating Preferred | Non-participating 1x |
| Kein Pre-Money im Dokument | Berechnung nicht möglich | Nur Post-Money | Pre-Money explizit |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-qualified-financing/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG/HGB-Eigenkapitalausweis aktualisieren.

## Vertiefung — Relevante Normen

### Normen-Ergänzung und Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen

§ 12 HGB i.V.m. § 12 HRV (elektronische Einreichung Handelsregister) → Art. 25 eIDAS-VO (qualifizierte elektronische Signatur) → § 378 FamFG (Zurückweisung bei Formmängeln) → § 40 GmbHG (Einreichungspflicht Gesellschafterliste)

## 2. `formfehler-heilungs-timeline`

**Fokus:** Formfehler in Wandeldarlehen oder Kapitalerhohungsdokumenten identifizieren und Heilungsmassnahmen planen. §§ 125 311b BGB Nichtigkeit §§ 15 55 GmbHG Formerfordernisse. Prüfraster: Formmangel Nichtigkeit Heilung Nachbeurkundung Fristen. Output: Fehlerliste Heilungsplan Fristenkalender. Abgrenzung: nicht für allgemeine Beurkundungsprüfung (beurkundungserfordernis-prüfung).

# Formfehler und Heilungs-Timeline

## Zweck

Bei Wandeldarlehen sind Form-Fragen oft komplex (Textform reicht für Verpflichtung, Notar für Übertragung neu-emittierter Anteile). Verzögerung der Heilung birgt Insolvenz-/Anfechtungs-Risiken. Dieses Skill strukturiert die Heilungs-Timeline.

## Eingaben

- Wandeldarlehensvertrag (Form und Datum)
- Wandlungs-Erklärung (falls erfolgt)
- Bisherige Beurkundungs-Schritte
- Insolvenz-Lage Gesellschaft (drohend? eröffnet?)
- Verhältnis Gesellschaft-Lender (vertrauensvoll? streitig?)

## Schritt 1 — Form-Stufen-Übersicht

### Form-Hierarchie

| Form | Norm | Anwendungsbereich |
|---|---|---|
| Mündlich | – | Selten (Rangrücktritt nicht möglich) |
| Textform | § 126b BGB | Mindest bei Verbraucher Vertragsschluss |
| Schriftform | § 126 BGB | Beweis-Funktion Standard |
| Elektronische Form | § 126a BGB | Qualifizierte elektronische Signatur |
| Notarielle Beurkundung | § 128 BGB iVm § 15 GmbHG | Anteils-Übertragungs-Verpflichtung |

### Schriftform vs. Elektronische Form

- **§ 126a BGB** — qualifizierte elektronische Signatur (QES) ersetzt Schriftform
- **SMS-OTP** / **DocuSign-Standard** — fortgeschrittene Signatur (Art. 26 eIDAS), nicht qualifiziert
- **Bei Schriftform-Erfordernis** ist QES erforderlich
- **eIDAS 2.0** VO 2024/1183 — EU-weite Anerkennung

## Schritt 2 — Wandeldarlehensvertrag Form

### Verpflichtungs-Geschäft (Wandeldarlehensvertrag)

- **Textform § 126b BGB** ausreichend (Lenders Beweis-Sicherheit)
- **Schriftform empfohlen** für Rangrücktritt-Klarheit
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Verfügungs-Geschäft (Anteils-Übertragung bei Wandlung)

- **Notarielle Beurkundung** zwingend § 15 Abs. 3 GmbHG bei Verfügung über existierende Anteile
- **Bei Wandlung durch Kapitalerhöhung** Kapitalerhöhungs-Beschluss notariell zu beurkunden § 53 Abs. 2 GmbHG
- **Übernahme-Erklärung** beim Notar
- **Handelsregister-Anmeldung** notariell beglaubigt § 12 Abs. 1 HGB

### Konkrete Sequenz bei Wandlung

1. Lender erklärt Wandlung schriftlich
2. Geschäftsführer beruft Gesellschafterversammlung ein
3. Kapitalerhöhungs-Beschluss notariell beurkundet
4. Übernahme-Erklärung des Lenders notariell beurkundet (am gleichen Termin möglich)
5. Anmeldung HR notariell beglaubigt
6. Eintragung HR
7. Aktualisierung Gesellschafterliste

## Schritt 3 — Heilungs-Tatbestände

### Form-Mangel beim Wandeldarlehens-Vertrag

#### Bei mündlich vereinbartem Vertrag

- **Beweisbarkeit fragwürdig**
- **Rangrücktritt nicht wirksam** § 39 Abs. 2 InsO erfordert Schriftform für klaren Inhalt
- **Heilung** durch schriftliche Bestätigung
- **Nachträgliche Schriftform** ist möglich, aber Wirkungs-Tag (ex tunc oder ex nunc?) streitig

#### Bei Textform/E-Mail

- **Grundsätzlich wirksam** für Verpflichtungsgeschäft
- **Bei Rangrücktritt fragwürdig** — Streit-Risiko
- **Empfehlung Schriftform-Heilung** durch Nachvertrag

### Form-Mangel bei Wandlungs-Erklärung

- **Empfangsbedürftige Willenserklärung** Lender → Gesellschaft
- **Form nach Vertrag** — typisch Schriftform empfohlen
- **Bei fehlender Schriftform** Heilung durch nachträgliche Bestätigung

### Form-Mangel bei Beschluss

- **Notarielle Beurkundung** Pflicht
- **Bei fehlender Beurkundung** Beschluss nichtig § 125 BGB
- **Heilung nur durch erneuten beurkundeten Beschluss**

## Schritt 4 — Heilungs-Timeline kritisch

### Beispiel-Fall

```
Tag 0: Wandeldarlehens-Vertrag unterzeichnet
 (Textform via DocuSign mit SMS-OTP)
Tag 1-7: Auszahlung Darlehen
Tag 8: Gesellschaft uebermittelt Quartals-Bericht
 Liquiditaets-Schwierigkeiten erkennbar
Tag 9: Geschaeftsfuehrer-Sitzung — Sanierungs-Plan
 Pruefung Zahlungs-Unfaehigkeit § 17 InsO
Tag 14: Insolvenz-Antrag droht
Tag 15: Insolvenz-Antrag eingereicht
```

#### Risiko-Konstellation

- **Wandeldarlehens-Vertrag in Textform** möglicherweise nicht qualifiziert für Rangrücktritt-Wirkung
- **In Insolvenz** Rangrücktritt-Klausel ggf. nicht wirksam — Lender als ungesicherter Gläubiger statt nachrangiger Gläubiger
- **Heilung nicht mehr möglich** nach Insolvenz-Eröffnung
- **Anfechtungs-Risiko** § 130 ff. InsO bei nachträglicher Sicherheits-Bestellung

#### Empfehlung

- **Schriftform-Heilung sofort** bei Vertragsschluss
- **QES-Signatur** wenn elektronisch
- **Notar-Vorab-Konsultation** für Wandlungs-Beschluss bei späteren Trigger

## Schritt 5 — Heilungs-Vorgehensweise

### Schritt 5a — Form-Mangel-Identifikation

- Vertrags-Prüfung
- Unterschriften-Form
- Datum-Stempel
- Vollmachts-Form

### Schritt 5b — Heilungs-Vereinbarung

```
Bestaetigung des Wandeldarlehens-Vertrags vom [Datum]

Die Parteien bestaetigen hiermit den am [Datum] (oder
in [Form]) abgeschlossenen Wandeldarlehens-Vertrag.

Die Bestaetigung erfolgt in Schriftform gem. § 126 BGB
zur Sicherstellung der Beweis- und Rangruecktritt-Funktion.

Die wesentlichen Vertragsinhalte:
[Wiedergabe Inhalt]

Die Heilung wirkt rueckwirkend auf den urspruenglichen
Vertrags-Schluss.

[Ort Datum]
[Lender-Unterschrift] [Gesellschaft-Unterschrift]
```

### Schritt 5c — Notarielle Beurkundung

- Bei Wandlungs-Beschluss
- Beim Notar Termin vereinbart
- Vorabe-Konsultation
- Beurkundungs-Kosten klären

## Schritt 6 — Anfechtungs-Risiken § 130 ff. InsO

### Konstellationen

- **§ 130 InsO** Kongruenz-Anfechtung — wenn Bestellung nach Insolvenz-Antrag-Stellung
- **§ 131 InsO** Inkongruenz-Anfechtung — wenn keine entsprechende Gegenleistung
- **§ 132 InsO** unmittelbar nachteilige Rechtsgeschäfte
- **§ 133 InsO** Vorsatz-Anfechtung — bei Vorsatz auf Gläubiger-Benachteiligung

### Heilungs-Maßnahmen kurz vor Insolvenz

- **Risiko hoch** dass Heilung selbst angefochten wird
- **Anwalts-Beratung** spezifisch Anfechtung
- **Dokumentation** Vorab-Vereinbarung

### Schutz-Strategie

- **Frühe Heilung** vor Krise
- **Bargeschäft-Klausel** wenn Heilung zugleich mit Auszahlung
- **Rangrücktritt** klar als qualifiziert formuliert

## Schritt 7 — Insolvenz-Sonderfall

### Wenn Insolvenz droht

- **Sofortige Form-Heilung** sicherstellen
- **Beratung mit Skill** `mandat-triage-insolvenzrecht`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wandlung erwägen** vor Insolvenz-Eröffnung

### Nach Insolvenz-Eröffnung

- **Wandlung praktisch ausgeschlossen** Gesellschaft-Verfügung Insolvenz-Verwalter
- **Lender als Insolvenz-Gläubiger** mit Rang nach § 39 Abs. 2 InsO (bei wirksamen qualifiziertem Rangrücktritt)
- **Forderungs-Anmeldung** bei Insolvenz-Tabelle § 174 InsO

## Schritt 8 — Notar-Kommunikation

### Vorab-Konsultation

- **Inhalts-Klärung** Wandlungs-Beschluss
- **Form-Anforderungen** klären
- **Vollmachts-Prüfung**
- **Termin-Vorbereitung**

### Notar-Auftrag

```
Sehr geehrte/r Notar/in,

wir benoetigen Beurkundungs-Termin fuer:

- Kapitalerhoehungs-Beschluss § 53 Abs. 2 GmbHG
- Uebernahme-Erklaerung Wandeldarlehens-Lender
- HR-Anmeldung

Wandeldarlehens-Vertrag vom [Datum] (Kopie als Anlage)
Wandlungs-Erklaerung Lender vom [Datum] (Kopie als Anlage)
Gesellschafterliste aktuell (Kopie als Anlage)

Termin-Vorschlag: [Datum-Vorschlaege]
```

### Termin-Logistik

- Notar wählt Datum
- Vorab-Entwürfe versenden
- Mandanten-Vorbereitung (Vollmachten Ausweise)
- Notar-Beurkundungs-Gebühren GNotKG

## Schritt 9 — Häufige Form-Fehler in der Praxis

### Fehler 1: Fehlende Unterschriften aller Parteien

- Heilung durch Nachunterzeichnung
- Wenn nicht möglich: Vertragsbestätigung

### Fehler 2: Datum-Lücken

- Bei undatierter Unterschrift Vermutung Unterzeichnungs-Datum
- Klärung durch Nachbestätigung

### Fehler 3: Vertretungs-Mangel

- Vollmacht-Vorlage erforderlich
- Heilung durch Genehmigung § 177 BGB

### Fehler 4: Elektronische Signatur ohne QES

- Heilung durch Schriftform-Nachvertrag

### Fehler 5: Vergessen Wandlungs-Beschluss

- Bei Wandlung ohne Beschluss — Wandlung nichtig
- Heilung durch nachfolgenden beurkundeten Beschluss

## Schritt 10 — Compliance-Workflow

### Vor Vertragsschluss

- Form-Check (Schrift Notar wenn nötig)
- QES-Signatur wenn elektronisch
- Notar-Vorab-Beratung

### Bei Vertragsschluss

- Alle Unterschriften vollständig
- Datum klar
- Vertretungs-Vollmachten

### Vor Wandlung

- Notar-Termin früh vereinbaren
- Beschluss-Entwurf vorab
- Lender-Übernahme-Erklärung vorab

### Bei Wandlung

- Beurkundung an einem Termin (Beschluss + Übernahme)
- HR-Anmeldung
- Gesellschafterliste-Update

### Nach Wandlung

- HR-Eintragung abwarten
- Aktualisierung Cap-Table
- Steuer-Meldung wenn relevant

## Verzahnung mit anderen Skills

- `beurkundungserfordernis-pruefung` — Detail Beurkundungs-Prüfung
- `textform-vs-schriftform-vs-notariell` — Form-Stufen
- `unterzeichnung-elektronisch-docusign` — eIDAS-Detail
- `wandelereignis-trigger-dispatcher` — Wandlungs-Ereignis-Master
- `gesellschafterbeschluss-kapitalerhoehung` — Beschluss-Inhalt
- `notar-paket-uebermittlung` — Notar-Kommunikation
- `rangruecktritt-formulieren` — Insolvenz-Aspekt

## Ausgabe

- `formfehler-timeline-{az}.md` mit Form-Audit Risiko-Fenster Heilungs-Plan
- Heilungs-Vereinbarung-Entwurf
- Notar-Termin-Vorbereitung
- Bei Insolvenz-Risiko: Eskalations-Memo
- Anfechtungs-Risiko-Memo
- Frist im Fristenbuch (Heilung sofort)

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- BGB §§ 125 126 126a 126b 128 177
- GmbHG §§ 15 53
- HGB § 12
- InsO §§ 39 130 131 132 133 174
- eIDAS-VO 910/2014 und 2024/1183
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- GNotKG
