---
name: datenschutz-pruefung-bestehender-vertraege-rolemix-getrennt-vs
description: "Datenschutz Pruefung Bestehender Vertraege Rolemix Getrennt VS im Datenschutzrecht: prüft konkret Pruefung bestehender AVV-Vertraege Vendor-Inventur, Abgrenzung Rollenmix Art, TOM-Anlage zum AVV nach Art, Datenpanne nach Art."
---

# Datenschutz Pruefung Bestehender Vertraege Rolemix Getrennt VS

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `avv-pruefung-bestehender-vertraege-audit`

**Fokus:** Pruefung bestehender AVV-Vertraege Vendor-Inventur AVV-Audit und Vertragsfolgemanagement. Behandelt die systematische Durchsicht eines AVV-Bestands die Identifikation veralteter Klauseln SCC-Altmuster fehlender DPF-Bezug und sub-AV-Listenpflege. Output: Audit-Bericht und Vertragsverbesserungsplan.

### AVV-Audit – Pruefung bestehender Vertraege

## Zweck / Purpose

Systematische Inventur und Pruefung bestehender Auftragsverarbeitungsvertraege auf Aktualitaet, Vollstaendigkeit der Pflichtinhalte, Sub-AV-Pflege und Drittlandbezug. Purpose (EN): Vendor inventory and audit of existing DPAs.

## Wann dieses Modul hilft

- Mandant hat AVV-Bestand und will im Rahmen eines Compliance-Programms pruefen.
- Aufsichtsbehoerde hat eine Pruefung angekuendigt und der AVV-Bestand muss verteidigungsfaehig sein.
- Nach einer Datenpanne oder einem Aufsichtsanlass ist der AVV-Bestand systematisch nachzuziehen.
- Bei Unternehmenskauf (M&A) ist der AVV-Bestand Teil der Due Diligence.

## Rechtlicher Rahmen

- Art. 28 DSGVO – Pflicht zum AVV.
- Art. 30 DSGVO – Verarbeitungsverzeichnis.
- Art. 32 DSGVO – TOM (regelmaessig Anlage zum AVV).
- Art. 44 bis 49 DSGVO – Drittlandtransfer.
- Beschluss (EU) 2021/914 – SCC seit 27.06.2021; Altmuster (2001/497/EG, 2004/915/EG, 2010/87/EU) sind seit 27.12.2022 für Altbestand abgeloest.
- Beschluss (EU) 2023/1795 – DPF seit 10.07.2023.

## Ablauf / Checkliste

1. **Inventur.**
 - Vendor-Liste (Lieferanten mit Datenverarbeitung).
 - AVV-Status pro Vendor: vorhanden / nicht vorhanden / unklar.
 - Vertragsdatum, Vertragsversion.
 - Verarbeitungsumfang, Datenkategorien, Drittlandbezug.

2. **Rollenpruefung.**
 - Pro Vendor: ist die Rollenzuordnung korrekt (Art. 28 versus Art. 26 versus eigene Verantwortlichkeit)?
 - Querverweis: avv-rolemix-getrennt-vs-gemeinsam-verantwortlich.

3. **Pflichtinhalte-Check.**
 - Acht Pflichtklauseln nach Art. 28 Abs. 3 lit. a bis h DSGVO vollstaendig?
 - Rahmenangaben (Gegenstand, Dauer, Art, Zweck, Datenarten, Betroffene) konkret?
 - TOM-Anlage aktuell und konkret?
 - Querverweis: avv-art-28-mindestinhalte-checkliste.

4. **Sub-AV-Pflege.**
 - Liste vorhanden und aktuell?
 - Wechselbenachrichtigungsverfahren funktioniert?
 - Drittland-Sub-AV identifiziert und abgesichert?

5. **Drittlandbezug.**
 - Aktuelle SCC nach Beschluss (EU) 2021/914 oder noch Altmuster?
 - DPF-Listing aktuell?
 - TIA vorhanden und aktuell?

6. **Aktualitaet der TOM-Anlage.**
 - Letzte Pruefung?
 - Branchenuebliche Standards (ISO 27001, BSI C5, SOC 2) referenziert?
 - Pflichtmindestmassnahmen aus Art. 32 DSGVO abgedeckt?

7. **Verarbeitungsverzeichnis Art. 30 DSGVO.**
 - AVV-Vendoren im Verzeichnis dokumentiert?
 - Konsistenz zwischen Verzeichnis und AVV?

8. **Audit-Bericht.**
 - Bewertungsmatrix pro Vendor (Ampel: rot / orange / gelb / gruen).
 - Massnahmenplan mit Fristen.
 - Eskalationsverfahren bei nicht behebbaren Maengeln.

## Mustertext / Template

AVV-Audit-Matrix-Vorlage:

```
AVV-Audit Bericht – Stand [DATUM]

Vendor: [NAME]
Vertragsstand: [DATUM, VERSION]
Verarbeitungsumfang: [BESCHREIBUNG]
Drittlandbezug: [JA/NEIN, LAND]

Pruefdimension | Status | Befund / Massnahme
-------------------------------------------------|--------|-----------------------------
Rollenzuordnung (Art. 28 / 26 / sep.) | [g/y/o/r] | [...]
Pflichtangaben Art. 28 Abs. 3 Satz 2 DSGVO | [g/y/o/r] | [...]
lit. a Weisungsgebundenheit | [g/y/o/r] | [...]
lit. b Vertraulichkeit | [g/y/o/r] | [...]
lit. c TOM Art. 32 DSGVO | [g/y/o/r] | [...]
lit. d Sub-AV Art. 28 Abs. 2 und 4 | [g/y/o/r] | [...]
lit. e Unterstuetzung Betroffenenrechte | [g/y/o/r] | [...]
lit. f Unterstuetzung Art. 32-36 | [g/y/o/r] | [...]
lit. g Loeschung / Rueckgabe | [g/y/o/r] | [...]
lit. h Audit / Inspektion | [g/y/o/r] | [...]
SCC Stand Beschluss (EU) 2021/914 | [g/y/o/r] | [...]
DPF (sofern US-Anbieter) | [g/y/o/r] | [...]
TIA (sofern Drittland) | [g/y/o/r] | [...]
TOM-Anlage aktuell | [g/y/o/r] | [...]
Art. 30 DSGVO-Verzeichnis konsistent | [g/y/o/r] | [...]

Gesamtbewertung Vendor: [g/y/o/r]
Empfohlene Massnahme: [Verlaengern / Nachverhandeln / Beenden]
Frist: [DATUM]
```

## Typische Drafting-Fehler

- AVV-Bestand wird nur per Stichprobe geprueft – für aufsichtsbehoerdliche Pruefung unzureichend.
- Altbestand mit SCC-Altmustern (2001/497/EG, 2010/87/EU) nicht umgestellt.
- DPF-Listing nicht periodisch geprueft.
- TOM-Anlage Stand 2018 ohne Aktualisierung.
- Sub-AV-Liste wird nicht gepflegt – Versionskonflikt zwischen Vendor-Webseite und Vertrag.
- Verarbeitungsverzeichnis Art. 30 DSGVO und AVV-Bestand laufen auseinander.
- Bei M&A: AVV-Bestand des Targets nicht in Due Diligence gewuerdigt.

## Quellen Stand 06/2026

- Art. 28, Art. 30, Art. 32 DSGVO.
- Beschluss (EU) 2021/914 – SCC seit 27.06.2021.
- Beschluss (EU) 2023/1795 – DPF seit 10.07.2023.
- EDSA-Leitlinien 07/2020 (Final 07.07.2021).
- EDSA-Empfehlungen 01/2020 (Version 2.0 Juni 2021).
- Zitierweise: `../../../references/zitierweise.md`.

## 2. `avv-rolemix-getrennt-vs-gemeinsam-verantwortlich`

**Fokus:** Abgrenzung Rollenmix Art. 4 Nr. 7 versus Art. 26 versus Art. 28 DSGVO. Wann sind zwei Akteure getrennte Verantwortliche wann gemeinsam Verantwortliche wann Verantwortlicher und Auftragsverarbeiter. Test-Schema für Mischkonstellationen mit Indizien aus EDSA-Leitlinien 07/2020 und EuGH-Rechtsprechung. Output: Pruefvermerk zur Rollenzuordnung.

### Rollenmix – Getrennt versus gemeinsam versus Auftragsverarbeitung

## Zweck / Purpose

Strukturierte Abgrenzung zwischen drei datenschutzrechtlichen Rollenmodellen in Mehr-Akteur-Konstellationen: getrennte Verantwortliche, gemeinsame Verantwortliche (Art. 26 DSGVO), Auftragsverarbeiter (Art. 28 DSGVO). Purpose (EN): Separate vs. joint vs. processor – role allocation in multi-actor data processing under GDPR.

## Wann dieses Modul hilft

- Zwei oder mehr Akteure verarbeiten dieselben personenbezogenen Daten und es ist unklar, welches Vertragsmodell zu schliessen ist.
- Aufsichtsbehoerde fragt nach Rollenzuordnung im Verarbeitungsverzeichnis (Art. 30 DSGVO).
- Mandant geht davon aus, "wir sind nur Auftragsverarbeiter" – Pruefung, ob nicht in Wahrheit Art. 26 DSGVO einschlaegig ist.
- Vor Abschluss eines Joint-Controller-Agreement oder AVV soll die Einstufung gesichert sein.

## Rechtlicher Rahmen

- Art. 4 Nr. 7 DSGVO: Verantwortlicher entscheidet allein oder gemeinsam mit anderen ueber Zwecke und Mittel.
- Art. 26 DSGVO: Gemeinsam Verantwortliche.
- Art. 28 DSGVO: Auftragsverarbeiter.
- Art. 4 Nr. 9 DSGVO: Empfaenger.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021).
- EuGH C-25/17 (Zeugen Jehovas) – verifiziert: Mitverantwortung durch organisatorische Mittel auch ohne unmittelbaren Datenzugang.
- EuGH C-498/16 (Wirtschaftsakademie / Fanpages) – verifiziert: Fanpage-Betreiber ist gemeinsam mit Plattform verantwortlich.
- EuGH C-40/17 (Fashion ID) – verifiziert: Like-Button-Einbinder ist für Erhebung und Uebermittlung mitverantwortlich.

## Ablauf / Checkliste

1. **Zweck- und Mittelprueung.**

 | Frage | Verantwortlicher allein | Gemeinsam Verantwortlich | Auftragsverarbeiter |
 |---|---|---|---|
 | Wer legt Zweck fest? | Akteur A allein | Akteur A und Akteur B gemeinsam | Akteur A allein, Akteur B fuehrt aus |
 | Wer legt Mittel fest? | Akteur A | Beide oder Akteur B als wesentlicher Mitbestimmer | Akteur A bestimmt wesentliche Mittel, Akteur B technische Detailmittel |
 | Eigener Nutzen aus Daten? | Nur Akteur A | Beide ziehen Nutzen | Nur Akteur A |
 | Weisungsgebundenheit? | nicht relevant | nein, kollektive Entscheidung | ja, voll |

2. **EuGH-Indizienreihe.**
 - Wer entscheidet ueber Zweck der Verarbeitung? (Kerntest)
 - Wer bestimmt wesentliche Mittel (z. B. Tool-Auswahl, Speicherort, Loeschfristen)?
 - Wer profitiert wirtschaftlich von der Verarbeitung?
 - Besteht eine wechselseitige Abhaengigkeit?
 - Wird die Verarbeitung gemeinsam beworben oder organisiert?

3. **Negativindizien gegen Auftragsverarbeitung.**
 - Eigene Verarbeitung für eigene Werbung, eigenes KI-Training, eigene Statistik.
 - Eigene Anonymisierung mit nachgelagerter eigener Nutzung.
 - Eigene Rechtsdienstleistung (Inkasso, Steuerberatung, Rechtsanwaltsleistung) im Auftrag des Mandanten – meist Funktionsuebertragung statt Art. 28 (Querverweis: funktionsuebertragung-vs-auftragsverarbeitung).
 - Schaltung von Tracking-Pixeln auf eigener Webseite (regelmaessig Art. 26 mit dem Tracking-Anbieter).

4. **Negativindizien gegen Joint Control.**
 - Reiner Datenfluss zwischen zwei getrennten Geschaeften ohne abgestimmte Verarbeitung.
 - Jeder Akteur hat eigene Rechtsgrundlage und eigenen Zweck.
 - Keine gemeinsame Bewerbung oder Organisation.

5. **Pruefraster (Stufenmodell).**
 - Stufe 1: Liegt eine Verarbeitung im Sinne von Art. 4 Nr. 2 DSGVO vor? (immer ja)
 - Stufe 2: Wer entscheidet ueber Zweck? Wenn nur einer: weiter Stufe 4. Wenn mehrere: weiter Stufe 3.
 - Stufe 3: Liegt gemeinsame Entscheidung auch ueber wesentliche Mittel oder gemeinsamer Nutzen vor? Wenn ja: Art. 26 DSGVO. Wenn nein: getrennte Verantwortliche.
 - Stufe 4: Ist der ausfuehrende Akteur weisungsgebunden und ohne eigenen Zweck? Wenn ja: Art. 28 DSGVO. Wenn nein: getrennte Verantwortliche oder Funktionsuebertragung.

## Mustertext / Template

Pruefvermerk-Vorlage zur Rollenzuordnung:

```
Pruefvermerk Rollenzuordnung DSGVO
-----------------------------------
Verarbeitung: [Beschreibung]
Akteur A: [Bezeichnung, Funktion]
Akteur B: [Bezeichnung, Funktion]
Datenkategorien: [Stamm-/Verkehrs-/Inhaltsdaten/Art. 9 DSGVO]
Betroffene: [Kategorien]

1. Zweck der Verarbeitung
 Wer entscheidet? [A allein / A und B gemeinsam / nur für A]
 Begruendung: [Sachverhaltsbasis]

2. Wesentliche Mittel
 Wer entscheidet? [A allein / A und B gemeinsam / A legt fest, B fuehrt aus]
 Indizien: [Tool-Auswahl, Speicherort, Loeschfristen, Sicherheitsmassnahmen]

3. Wirtschaftlicher Nutzen
 [Nur A / beide / A nutzt für Geschaeft, B nur für Entgelt]

4. Weisungsgebundenheit B?
 [voll / teilweise / keine]

5. EuGH-Linie
 Vergleichbar mit: [C-25/17 / C-498/16 / C-40/17 / keine direkte Vergleichbarkeit]

6. Einordnung
 [ ] Akteur A allein verantwortlich (Art. 4 Nr. 7 DSGVO)
 [ ] Akteur A und B gemeinsam verantwortlich (Art. 26 DSGVO)
 [ ] Akteur A Verantwortlicher, Akteur B Auftragsverarbeiter (Art. 28 DSGVO)
 [ ] Getrennte Verantwortliche

7. Folgevertrag
 [ ] Joint-Controller-Vereinbarung Art. 26
 [ ] AVV Art. 28
 [ ] C2C-Datenuebermittlungsklausel
 [ ] kein gesonderter Vertrag erforderlich

Datum, Unterschrift Datenschutzbeauftragter
```

## Typische Drafting-Fehler

- AVV abgeschlossen, obwohl Joint Control vorliegt (Fanpage / Like-Button / Webtracking).
- Joint-Agreement abgeschlossen, obwohl getrennte Verantwortliche vorliegen (typischer Fall: Inkasso-Dienstleister).
- "Standardloesung AVV" ohne Pruefung.
- Berufsgeheimnistraeger als reine Auftragsverarbeiter behandelt (Funktionsuebertragung uebersehen).
- Tracking-Anbieter als Auftragsverarbeiter behandelt, obwohl er Daten für eigene Zwecke nutzt.

## Quellen Stand 06/2026

- Art. 4 Nr. 7, Art. 26, Art. 28 DSGVO.
- EDSA-Leitlinien 07/2020 (Final 07.07.2021), abrufbar ueber edpb.europa.eu.
- EuGH C-25/17 (Zeugen Jehovas) – verifiziert.
- EuGH C-498/16 (Wirtschaftsakademie / Fanpages) – verifiziert.
- EuGH C-40/17 (Fashion ID) – verifiziert.
- Volltexte ueber curia.europa.eu pruefen.
- Zitierweise: `../../../references/zitierweise.md`.

## 3. `avv-tom-art-32-dsgvo-anlage`

**Fokus:** TOM-Anlage zum AVV nach Art. 32 DSGVO. Strukturierte Aufstellung der technischen und organisatorischen Massnahmen mit Pseudonymisierung Verschluesselung Vertraulichkeit Integritaet Verfuegbarkeit Belastbarkeit sowie regelmäßige Pruefung. Output: Strukturierte TOM-Anlage auf Deutsch.

### TOM-Anlage Art. 32 DSGVO

## Zweck / Purpose

Strukturierte Anlage zum AVV mit den technischen und organisatorischen Massnahmen des Auftragsverarbeiters gemaess Art. 32 DSGVO und Art. 28 Abs. 3 lit. c DSGVO. Purpose (EN): German-language TOM annex to a DPA under Article 32 GDPR.

## Wann dieses Modul hilft

- TOM-Anlage zum AVV ist zu erstellen, zu pruefen oder zu aktualisieren.
- Aufsichtsbehoerde fordert Nachweis der TOM.
- Nach Datenpanne ist die TOM-Anlage auf Aktualitaet zu pruefen.
- Bei Aenderung der Verarbeitung ist die TOM-Anlage anzupassen.

## Rechtlicher Rahmen

- Art. 32 Abs. 1 DSGVO: Geeignete TOM unter Beruecksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, der Umstaende und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeit und Schwere des Risikos.
- Art. 32 Abs. 1 lit. a bis d DSGVO: Pseudonymisierung und Verschluesselung, Vertraulichkeit, Integritaet, Verfuegbarkeit, Belastbarkeit, Wiederherstellbarkeit, regelmäßige Pruefung.
- Art. 25 DSGVO: Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen.
- Art. 28 Abs. 3 lit. c DSGVO: TOM als Pflichtklausel im AVV.

## Ablauf / Checkliste

1. **Risikobewertung.**
 - Art der Daten (Stamm-, Verkehrs-, Inhaltsdaten, Art. 9 DSGVO).
 - Umfang und Zweck.
 - Eintrittswahrscheinlichkeit und Schwere des Risikos für Betroffene.

2. **Mindestkategorien (Art. 32 Abs. 1 DSGVO).**

 | Kategorie | Massnahmenbeispiele |
 |---|---|
 | Pseudonymisierung | Pseudonymisierung in Test- und Entwicklungsumgebungen, technische Trennung der Zuordnungstabelle |
 | Verschluesselung | TLS 1.3 in Transit; AES-256 at rest; Schluesselverwaltung HSM |
 | Vertraulichkeit | Zutrittskontrolle, Zugangskontrolle, Zugriffskontrolle, Trennungskontrolle |
 | Integritaet | Weitergabekontrolle, Eingabekontrolle, Logging, Hashfunktionen |
 | Verfuegbarkeit | Backup, RPO/RTO, Notfallplan, geo-redundante Speicherung |
 | Belastbarkeit | DDoS-Schutz, Lastverteilung, Failover-Verfahren |
 | Wiederherstellbarkeit | Backup-Tests, dokumentierte Wiederherstellungsverfahren |
 | Regelmäßige Pruefung | jaehrliche TOM-Audits, Penetrationstests, Vulnerability Scans |

3. **Organisatorische Massnahmen.**
 - Datenschutzbeauftragter, Datenschutzschulungen (jaehrlich), Vertraulichkeitsverpflichtungen, IT-Sicherheits-Richtlinie, Incident-Response-Plan, Need-to-Know-Prinzip, Berechtigungsverwaltung, Joiner-Mover-Leaver-Prozess.

4. **Zertifikate und Standards.**
 - ISO/IEC 27001:2022.
 - BSI IT-Grundschutz / BSI C5:2020 (Cloud-Spezifikum).
 - SOC 2 Type II Trust Services Criteria.
 - TISAX (Automotive).
 - PCI-DSS (Zahlungsverkehr).

5. **Sub-AV-Konsistenz.**
 - Sub-AV muessen mindestens dasselbe TOM-Niveau einhalten.
 - Vertragliche Durchleitung (Art. 28 Abs. 4 DSGVO).

## Mustertext / Template

TOM-Anlage (Strukturvorlage):

```
Anlage 2 zum Auftragsverarbeitungsvertrag
Technische und organisatorische Massnahmen (Art. 32 DSGVO)

Stand: [DATUM]
Auftragsverarbeiter: [NAME]
Pruefturnus: jaehrlich, unverzueglich bei wesentlicher Aenderung

1. Pseudonymisierung (Art. 32 Abs. 1 lit. a DSGVO)
 1.1 In Entwicklungs- und Testumgebungen werden personenbezogene Daten ausschliesslich in pseudonymisierter Form verarbeitet.
 1.2 Die Zuordnungstabelle wird getrennt gespeichert; Zugriff nur für den Datenschutzbeauftragten.

2. Verschluesselung (Art. 32 Abs. 1 lit. a DSGVO)
 2.1 In Transit: TLS 1.3 mit Forward Secrecy; SSL/TLS-Konfiguration gemaess BSI TR-02102.
 2.2 At Rest: AES-256 (CBC oder GCM) für alle Datenbanken und Backups.
 2.3 Schluesselverwaltung: HSM oder gleichwertige Loesung; jaehrliche Rotation.

3. Vertraulichkeit (Art. 32 Abs. 1 lit. b DSGVO)
 3.1 Zutrittskontrolle: physische Sicherung der Rechenzentren (24/7-Bewachung, Mehrfaktor-Zutritt).
 3.2 Zugangskontrolle: Multi-Faktor-Authentifizierung für alle priviligierten Konten.
 3.3 Zugriffskontrolle: rollenbasiertes Berechtigungsmodell, Least Privilege, periodische Rezertifizierung.
 3.4 Trennungskontrolle: mandantenfaehige Trennung; logische Trennung mit eigener Zugriffskontrolle.

4. Integritaet (Art. 32 Abs. 1 lit. b DSGVO)
 4.1 Weitergabekontrolle: dokumentierte Schnittstellen, Audit-Log für alle Datenexporte.
 4.2 Eingabekontrolle: nachvollziehbare Protokollierung aller Schreibvorgaenge auf personenbezogene Daten.
 4.3 Hash-Funktionen: SHA-256 oder besser für Integritaetspruefungen.

5. Verfuegbarkeit und Belastbarkeit (Art. 32 Abs. 1 lit. b DSGVO)
 5.1 Backup: taegliche inkrementelle Backups, woechentliche Vollbackups, Aufbewahrung 30 Tage.
 5.2 RPO (Recovery Point Objective): hoechstens 24 Stunden.
 5.3 RTO (Recovery Time Objective): hoechstens 8 Stunden für kritische Verarbeitungen.
 5.4 Geo-Redundanz: synchrone Replikation in mindestens zwei EU-Rechenzentren.
 5.5 DDoS-Schutz: vorgeschalteter Filter; SLA mit Provider.

6. Wiederherstellbarkeit (Art. 32 Abs. 1 lit. c DSGVO)
 6.1 Notfallhandbuch; Notfalluebungen mindestens jaehrlich.
 6.2 Dokumentierte Wiederherstellungsverfahren.
 6.3 Verifikation der Wiederherstellbarkeit durch tatsaechlichen Wiederherstellungstest mindestens halbjaehrlich.

7. Regelmäßige Pruefung (Art. 32 Abs. 1 lit. d DSGVO)
 7.1 Penetrationstest durch unabhaengige Dritte mindestens jaehrlich.
 7.2 Vulnerability Scan monatlich.
 7.3 ISMS-internes Audit jaehrlich; externes Audit nach ISO 27001 jaehrlich.
 7.4 TOM-Anlage wird mindestens jaehrlich auf Aktualitaet geprueft.

8. Organisatorische Massnahmen
 8.1 Datenschutzbeauftragter benannt; Kontaktangabe in Anlage 4.
 8.2 Verschwiegenheitsverpflichtung aller Mitarbeitenden (Art. 28 Abs. 3 lit. b DSGVO).
 8.3 Jaehrliche Datenschutzschulung; Schulungsnachweise vorhanden.
 8.4 Joiner-Mover-Leaver-Prozess; sofortiger Entzug der Zugriffsrechte bei Austritt.
 8.5 Incident-Response-Plan mit Meldewegen an den Verantwortlichen binnen 48 Stunden nach Kenntnis einer Datenpanne (Art. 33 DSGVO).

9. Zertifikate und Standards
 9.1 ISO/IEC 27001:2022 – Zertifizierungsdatum [DATUM], Zertifizierer [STELLE].
 9.2 BSI C5:2020 Typ 2 – Stand [DATUM].
 9.3 SOC 2 Type II – Berichtszeitraum [ZEITRAUM].

10. Sub-Auftragsverarbeiter
 10.1 Sub-AV unterliegen denselben oder gleichwertigen TOM gemaess Art. 28 Abs. 4 DSGVO.
 10.2 Sub-AV-Audits werden auf Verlangen vorgelegt.
```

## Typische Drafting-Fehler

- TOM-Anlage als Marketingbroschuere statt konkreter Massnahmen.
- Pauschalformulierungen ("nach Stand der Technik") ohne konkrete Beschreibung.
- Keine Aktualisierung seit Vertragsschluss.
- Pseudonymisierung als Pflicht uebergangen, obwohl Art. 32 Abs. 1 lit. a DSGVO sie explizit benennt.
- Keine RPO/RTO.
- Keine Pruefturnusangaben.
- Sub-AV-Konsistenz nicht adressiert.

## Quellen Stand 06/2026

- Art. 25, Art. 28 Abs. 3 lit. c, Art. 32 DSGVO.
- BSI TR-02102 (Kryptografische Verfahren).
- ISO/IEC 27001:2022.
- BSI C5:2020.
- SOC 2 Trust Services Criteria.
- Zitierweise: `../../../references/zitierweise.md`.

## 4. `datenpanne-meldung`

**Fokus:** Datenpanne nach Art. 33 34 DSGVO melden wenn Sicherheitsverletzung personenbezogener Daten vorliegt. Art. 33 34 DSGVO Meldepflichten § 65 BDSG. Prüfraster: Meldepflicht 72-Stunden-Frist Schwere Risikobewertung Behordenmeldung Betroffenenbenachrichtigung Dokumentation. Output: Meldeschreiben an Aufsichtsbehoerde Betroffenenbenachrichtigung Dokumentationsprotokoll. Abgrenzung: nicht für praeventive Massnahmen (dsfa-erstellung).

### Datenpannen-Meldung (Art. 33/34 DSGVO)

## Eingaben

Das Modell benötigt:

- **Beschreibung des Vorfalls**: Was ist wann und wie passiert? (Zeitpunkt der Entdeckung, vermutlicher Zeitpunkt des Eintritts)
- **Art der betroffenen Daten**: Kategorien (Art. 9/10 DSGVO?), Datenmenge, Anzahl betroffener Personen (geschätzt)
- **Betroffene Personen**: Kunden, Mitarbeiter, Minderjährige, vulnerable Gruppen?
- **Auswirkungen**: Welche Konsequenzen (Diskriminierung, Identitätsdiebstahl, finanzielle Schäden, Rufschädigung) drohen?
- **Zugang/Kontrolle**: Haben Unbefugte Daten eingesehen, kopiert, vernichtet oder verändert?
- **Bereits getroffene Maßnahmen**: Was hat der Mandant bereits unternommen?
- **Entdeckungsdatum**: Wann hat der Verantwortliche Kenntnis erlangt? (72-Stunden-Frist ab diesem Zeitpunkt)
- **Auftragsverarbeiter beteiligt?**: Liegt ein Vorfall beim AVV-Partner vor (Art. 33 Abs. 2 DSGVO)?

## Rechtlicher Rahmen

### Primärnormen

- **Art. 4 Nr. 12 DSGVO**: Definition "Verletzung des Schutzes personenbezogener Daten" – Vernichtung, Verlust, Veränderung, unbefugte Offenlegung oder Zugang zu personenbezogenen Daten.
- **Art. 33 Abs. 1 DSGVO**: Meldepflicht des Verantwortlichen an zuständige Aufsichtsbehörde; Frist: 72 Stunden nach Kenntniserlangung; bei verspäteter Meldung: Begründungspflicht.
- **Art. 33 Abs. 3 DSGVO**: Inhalt der Meldung: Beschreibung des Vorfalls, Kategorien und Anzahl Betroffener, Datenkategorien und -mengen, Kontaktdaten DPO, wahrscheinliche Folgen, ergriffene/geplante Maßnahmen.
- **Art. 33 Abs. 4 DSGVO**: Nachlieferung von Informationen in Stufen zulässig, wenn nicht alle Informationen sofort verfügbar.
- **Art. 33 Abs. 5 DSGVO**: Dokumentationspflicht aller Verletzungen, auch wenn keine Meldung erforderlich (internes Register).
- **Art. 34 DSGVO**: Benachrichtigungspflicht gegenüber betroffenen Personen, wenn Verletzung voraussichtlich hohes Risiko für Rechte und Freiheiten natürlicher Personen birgt.
- **Art. 34 Abs. 3 DSGVO**: Ausnahmen von der Benachrichtigungspflicht (geeignete Schutzmaßnahmen, Unverhältnismäßigkeit des Aufwands, behördliche Anordnung).

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### EDSA-Leitlinien

EDSA, Guidelines 9/2022 on personal data breach notification under GDPR, angenommen 28.03.2023: Enthält Fallkatalog typischer Datenpannen (Ransomware, Fehlversand, Datenverlust) mit Musterlösungen zur Risikoeinschätzung und Meldepflicht. Verbindliche Auslegungshilfe für Art. 33/34 DSGVO.

## Ablauf

**Schritt 1 – Sofortreaktion und Zeitsicherung**
- Exakten Zeitpunkt der Kenntniserlangung (durch wen, wie, wann) dokumentieren.
- 72-Stunden-Frist nach Art. 33 Abs. 1 DSGVO ab diesem Zeitpunkt berechnen.
- DPO (sofern bestellt, Art. 37 DSGVO) unverzüglich einbinden.

**Schritt 2 – Vorfallscharakterisierung**
- Prüfen: Verletzung i.S.d. Art. 4 Nr. 12 DSGVO (Vernichtung/Verlust/Veränderung/Offenlegung)?
- Art des Schadens klassifizieren: Vertraulichkeitsverletzung (Offenlegung), Integritätsverletzung (Manipulation), Verfügbarkeitsverletzung (Vernichtung/Verlust).

**Schritt 3 – Risikoeinschätzung (Schwellenwertprüfung)**
- Kein Risiko: Keine Meldepflicht (Art. 33 Abs. 1 a.E. DSGVO), nur interne Dokumentation.
- Risiko vorhanden: Meldung an Aufsichtsbehörde nach Art. 33 DSGVO.
- Hohes Risiko: Zusätzlich Benachrichtigung Betroffener nach Art. 34 DSGVO.
- Faktoren: Sensibilität der Daten (Art. 9/10 DSGVO-Kategorien erhöhen Risiko), Anzahl Betroffener, Identifizierbarkeit, finanzieller/sozialer Schaden, EDSA-Guidelines 9/2022.

**Schritt 4 – Meldung an Aufsichtsbehörde**
- Zuständige Behörde bestimmen: LfDI/LDA des Bundeslandes des Verantwortlichen (Hauptniederlassung); BfDI für Bundesbehörden und Telekommunikation.
- Online-Meldetools nutzen (jede LfDI unterhält eigenes Meldeportal).
- Inhalt nach Art. 33 Abs. 3 DSGVO: Art der Verletzung, Kategorien/Anzahl Betroffener, Datenkategorien/-mengen, Kontakt DPO/Datenschutzbeauftragter, Folgen, Maßnahmen.
- Teilmeldung zulässig (Art. 33 Abs. 4 DSGVO); Nachlieferung dokumentieren.

**Schritt 5 – Betroffenenbenachrichtigung (bei hohem Risiko)**
- Inhalt nach Art. 34 Abs. 2 DSGVO: Klare Beschreibung der Verletzung, Kontaktdaten DPO, wahrscheinliche Folgen, Abhilfemaßnahmen.
- Sprache: klar und verständlich, kein Fachjargon (Art. 12 Abs. 1 DSGVO).
- Ausnahmen prüfen: Verschlüsselung (Art. 34 Abs. 3 lit. a), öffentliche Bekanntmachung (lit. c), unverhältnismäßiger Aufwand.

**Schritt 6 – Interne Dokumentation**
- Eintrag in internes Verletzungsregister (Art. 33 Abs. 5 DSGVO): Auch bei nicht meldepflichtigen Vorfällen.
- Zeitstempel, Maßnahmen, Entscheidungsgrundlagen festhalten.

## Ausgabeformat

- **Risiko-Einschätzungsmatrix** (Tabelle): Datenkategorien × Risikograd × Meldepflicht × Benachrichtigungspflicht.
- **Meldeformular-Entwurf** (strukturierter Text nach Art. 33 Abs. 3 DSGVO).
- **Betroffenenbrief** (klare Sprache nach Art. 34 Abs. 2 DSGVO).
- **Internes Incident-Protokoll** (für Dokumentationspflicht Art. 33 Abs. 5 DSGVO).

## Beispiel

**Sachverhalt**: IT-Dienstleister des Unternehmens U meldet am 10.03.2025 um 09:00 Uhr, dass am 09.03.2025 um 22:00 Uhr unbekannte Dritte durch eine Sicherheitslücke auf eine Kundendatenbank mit 4.000 E-Mail-Adressen, Namen und Bestellhistorien zugegriffen haben.

**Gutachtenstil**:

*Fristbeginn*: Kenntniserlangung durch U am 10.03.2025 um 09:00 Uhr. Die 72-Stunden-Frist nach Art. 33 Abs. 1 DSGVO läuft bis zum 13.03.2025 um 09:00 Uhr.

*Meldepflicht*: Eine Datenschutzverletzung i.S.d. Art. 4 Nr. 12 DSGVO (unbefugte Offenlegung) liegt vor. Angesichts von 4.000 Betroffenen und personenbezogenen Daten der Bestellhistorie besteht ein Risiko für Rechte und Freiheiten; die Ausnahme "kein Risiko" greift nicht. Meldung an LfDI ist spätestens bis 13.03.2025 erforderlich (Art. 33 Abs. 1 DSGVO; EDSA Guidelines 9/2022, Beispiel 9).

*Benachrichtigungspflicht*: Ob ein hohes Risiko i.S.d. Art. 34 Abs. 1 DSGVO vorliegt, hängt davon ab, ob Dritte die Daten gezielt ausgenutzt haben (z.B. Phishing). Bei bloßem Zugriff ohne Nachweis der Datennutzung ist die Schwelle zum "hohen Risiko" nach EDSA Guidelines 9/2022 noch nicht zwingend erreicht; Einzelfallbewertung erforderlich.

*Dokumentation*: Unabhängig vom Ergebnis ist der Vorfall im internen Register nach Art. 33 Abs. 5 DSGVO zu dokumentieren.

## Risiken und typische Fehler

- **Fristversäumnis**: 72 Stunden ab Kenntniserlangung, nicht ab interner Aufklärung; Unkenntnis schützt nicht – der Verantwortliche muss organisatorisch sicherstellen, dass Vorfälle unverzüglich weitergeleitet werden.
- **Auftragsverarbeiter-Frist verwechseln**: AVV-Partner muss unverzüglich (ohne nennenswerte Verzögerung) an Verantwortlichen melden (Art. 33 Abs. 2 DSGVO); die 72-Stunden-Frist des Verantwortlichen beginnt mit dessen Kenntniserlangung.
- **Risikoeinschätzung zu lasch**: Keine Meldung trotz erkennbaren Risikos; Aufsichtsbehörden bewerten ex post streng, insb. bei Art. 9-Daten.
- **Unvollständige Meldung**: Teilmeldung ist zulässig, aber Nachlieferung muss dokumentiert und nachgereicht werden.
- **Betroffenenbenachrichtigung verzögert**: Bei hohem Risiko muss unverzüglich benachrichtigt werden (Art. 34 Abs. 1 DSGVO); keine 72-Stunden-Frist, aber kein Zuwarten auf Ermittlungsergebnis.
- **Fehlende interne Dokumentation**: Auch nicht meldepflichtige Vorfälle müssen ins interne Register; fehlendes Register ist eigenständiger Verstoß.
- **Bußgeldrisiko**: Verstöße gegen Art. 33/34 DSGVO sind nach Art. 83 Abs. 4 lit. a DSGVO mit bis zu 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes sanktionierbar.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei neuen EuGH-Entscheidungen zum Schadensersatz nach Art. 82 DSGVO, EDSA-Updates zu den Guidelines 9/2022 sowie Änderungen der nationalen Meldeportale der Aufsichtsbehörden.

## Faktische Updates (Stand 05/2026)

- **NIS-2-UmsuCG (deutsches Umsetzungsgesetz):** in Kraft seit Ende 2025 (BSIG n. F.). Bei meldepflichtigen Datenpannen, die zugleich Cyber-Sicherheitsvorfaelle bei wichtigen oder besonders wichtigen Einrichtungen sind, parallel zur DSGVO-Meldung an die Aufsichtsbehoerde die BSI-Meldung nach § 32 BSIG n. F. binnen 24 h (Fruehwarnung), 72 h (Vorfallsmeldung) und 1 Monat (Abschlussbericht) abgeben. Quelle: BGBl 2025, BSI-Portal bsi.bund.de.
- **Art. 82 DSGVO — Schadensersatz EuGH-Linie:** Der blosse Kontrollverlust kann immateriellen Schaden begruenden, ein automatischer Anspruch entsteht aber nicht. Verschulden des Verantwortlichen wird vermutet, Entlastung moeglich. Konkrete Aktenzeichen vor Zitat live ueber curia.europa.eu pruefen.
- **EDSA Guidelines 9/2022 zu Datenpannen:** Endfassung (angenommen 28.03.2023) ist verbindliche Auslegungshilfe; enthaelt Fallkatalog Ransomware, Phishing, Exfiltration, Fehlversand, Diebstahl mit konkreten Risikoampeln. Quelle: edpb.europa.eu/our-work-tools/our-documents/guidelines.
- **BfDI / Landesdatenschutzbehoerden:** Bei standortuebergreifenden Vorfaellen Federfuehrung nach Art. 56 DSGVO (One-Stop-Shop) klaeren. BfDI für Bundes- und TK-/Postwesen; LDA-Bayern, LfDI BW etc. für privatwirtschaftliche Verantwortliche.

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — bei Datenpannen mit Drittlandbezug (Benachrichtigungspflicht des Importeurs)
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — Nachträgliche DSFA-Prüfung nach Datenpanne; Vorab-Konsultation Art. 36 DSGVO
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — Meldepflicht des Auftragsverarbeiters nach Art. 33 Abs. 2 DSGVO im AVV-Kontext

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 5. `datenschutz-auskunftei-restschuldbefreiung-art17`

**Fokus:** Art. 17 DSGVO im Auskunfteifall: Interessenabwägung, öffentliche Registerfrist, Einschränkung, Widerspruch und gerichtliche Durchsetzung.

### Art. 17 DSGVO gegen Auskunftei nach Restschuldbefreiung

## Norm- und Quellenanker

DSGVO Art. 6 Abs. 1 lit. f, Art. 17, 18, 21; EuGH C-26/22/C-64/22.

## Red Flags

- pauschales Brancheninteresse
- keine Empfängerliste
- Löschung mit Berichtigung verwechselt

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

