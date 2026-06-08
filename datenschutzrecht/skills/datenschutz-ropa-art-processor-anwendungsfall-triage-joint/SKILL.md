---
name: datenschutz-ropa-art-processor-anwendungsfall-triage-joint
description: "Datenschutz Ropa ART Processor Anwendungsfall Triage Joint im Datenschutzrecht: prüft konkret Vollvorlage für das Verzeichnis von, Datenschutzrechtlichen Sachverhalt einordnen und, Joint-Controller-Vereinbarung nach Art, Grundtatbestand der Auftragsverarbeitung nach Art."
---

# Datenschutz Ropa ART Processor Anwendungsfall Triage Joint

## Aktenstart statt Formularstart

Wenn zu **Datenschutz Ropa Art Processor Anwendungsfall Triage Joint** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Datenschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `ropa-art-30-processor-deutsch-vorlage`

**Fokus:** Vollvorlage für das Verzeichnis von Verarbeitungstaetigkeiten des Auftragsverarbeiters nach Art. 30 Abs. 2 DSGVO. Vier Mindestinhalte, Auftraggeberliste, Verarbeitungskategorien, Drittlandtransfer, TOM-Verweis. Beispiele für Hosting, Steuerberatung, Lohnbuchhaltung.

### RoPA-Vorlage Auftragsverarbeiter (Processor) – Deutsch

## Wann dieses Modul hilft

- Auftragsverarbeiter baut sein RoPA erstmalig auf.
- Kanzlei taetigt für Mandanten Datenverarbeitung im Auftrag (z. B. Lohnbuchhaltung, IT-Outsourcing) und ist insoweit Processor.
- Audit eines bestehenden Processor-RoPA.
- Aufsichtsbehoerde verlangt nach Art. 30 Abs. 4 DSGVO Vorlage.

## Rechtlicher Rahmen

Art. 30 Abs. 2 DSGVO – Pflichtinhalte für Processor:

a) Name und Kontaktdaten des Auftragsverarbeiters und jedes Verantwortlichen, in dessen Auftrag er taetig ist, sowie ggf. eines Vertreters des Verantwortlichen oder des Auftragsverarbeiters und eines Datenschutzbeauftragten;
b) Kategorien der im Auftrag jedes Verantwortlichen durchgefuehrten Verarbeitungen;
c) ggf. Uebermittlungen in ein Drittland oder an eine internationale Organisation, einschliesslich Angabe des betreffenden Drittlands sowie bei Uebermittlungen gemaess Art. 49 Abs. 1 Unterabs. 2 Dokumentierung der geeigneten Garantien;
d) wenn moeglich, allgemeine Beschreibung der TOMs gemaess Art. 32 Abs. 1 DSGVO.

Wichtig: Pro Auftraggeber eine Zeile. Mehrere Verarbeitungskategorien koennen zusammengefasst werden, wenn TOMs identisch sind.

## Ablauf / Checkliste

1. Stammdaten Auftragsverarbeiter eintragen (Deckblatt).
2. Liste der Auftraggeber pflegen.
3. Pro Auftraggeber Verarbeitungskategorien beschreiben (nicht Einzelaktivitaeten).
4. Drittlandtransfers identifizieren und Garantie eintragen.
5. TOMs nicht im RoPA wiederholen, sondern auf TOM-Konzept verweisen.
6. Subverarbeiter (Art. 28 Abs. 4 DSGVO) gesondert dokumentieren, soweit ihr Einsatz mit Drittlandtransfer verbunden ist.
7. Versionierung und Review-Datum am Fuss.

## Mustertext / Template

### Deckblatt

```
Auftragsverarbeiter: [Firmenname]
Anschrift: [...]
Vertreter (Art. 27): [falls anwendbar]
Datenschutzbeauftragter: [Name, Kontakt]
Erstellt: [Datum]
Letzte Aenderung: [Datum]
Version: [v1.0]
```

### Tabelle (Pflichtspalten)

| Nr. | Auftraggeber (Verantwortlicher) | Verarbeitungskategorie | Drittland / Garantie | TOM-Verweis |
|---|---|---|---|---|
| 1 | [Mandant A GmbH] | Hosting Buchhaltungssoftware, Backup, Patch-Management | nein | TOM-Anhang A |
| 2 | [Mandant B AG] | Lohnbuchhaltung, Lohnsteueranmeldung, Sozialversicherungsmeldungen | nein | TOM-Anhang A |
| 3 | [Mandant C KG] | E-Mail-Hosting, Spam-Filterung | USA – Subprozessor (SCC + TIA in Anhang B) | TOM-Anhang A |
| 4 | [Mandant D e.V.] | Mitgliederverwaltung, Beitragsabbuchung | nein | TOM-Anhang A |

### Subverarbeiterliste (Anhang)

| Subverarbeiter | Sitz | Leistung | Transferinstrument |
|---|---|---|---|
| [Hyperscaler-Cloud] | USA | Infrastructure as a Service | EU-US DPF (Aktiv-Listing in Anhang B) |
| [E-Mail-Filterdienst] | Irland | Spam-Filter | EU/EWR – keine Garantien noetig |
| [Backup-Dienstleister] | Deutschland | Offsite-Backup | EU/EWR – keine Garantien noetig |

### Versionierungs-Footer

```
Version 1.0 – Erstanlage – [Datum, Bearbeiter]
Version 1.1 – [Aenderung] – [Datum, Bearbeiter]
```

## Typische Fehler

- "Verarbeitungskategorie" wird mit "Zweck" verwechselt – Zwecke bestimmt der Verantwortliche.
- Subverarbeiter fehlen, obwohl Drittlandtransfer ueber sie laeuft.
- Pro Auftraggeber separate TOMs dokumentiert, obwohl Mandantenbasis identisch ist – Redundanz vermeiden.
- Auftraggeber-DSB nicht erfasst.
- TOM-Spalte mit Wiederholung der Anlage 32 – besser Verweis.
- Drittlandtransfer in zweiter Stufe (Sub-Subprozessor) uebersehen.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 30 Abs. 2, Art. 28.
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).
- DSK-Kurzpapier Nr. 13 "Auftragsverarbeitung" (Stand 16.01.2018).

## 2. `anwendungsfall-triage`

**Fokus:** Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter Drittland. Output: Triage-Memo Bearbeitungsroute Normenmap. Abgrenzung: Einstieg und Triage; Detailarbeit in Spezialist-Skills.

### Datenschutz-Triage neuer Verarbeitungsvorgänge

## Eingaben

- Beschreibung des Verarbeitungsvorgangs (Datenarten, Zweck, Betroffenenkreis)
- Datenkategorien (Art. 4 Nr. 1, Art. 9 DSGVO); Beschäftigtendaten (§ 26 BDSG)?
- Neu erhoben oder Zweckänderung bei vorhandenen Daten (Art. 5 Abs. 1 lit. b DSGVO)?
- Auftragsverarbeiter / Drittland-Übermittlung?
- Automatisierte Entscheidungsfindung (Art. 22 DSGVO)?
- Cookies / Endgerätezugriff (§§ 24 ff. TDDDG)?

## Rechtlicher Rahmen

### Kernvorschriften

- **DSGVO:** Art. 5 (Grundsätze), Art. 6 (Rechtsgrundlagen), Art. 9 (besondere
 Kategorien), Art. 13/14 (Informationspflichten), Art. 17 (Löschrecht), Art. 22
 (automatisierte Entscheidungen), Art. 25 (Privacy by Design/Default), Art. 28 (AVV),
 Art. 30 (Verarbeitungsverzeichnis), Art. 32 (TOM), Art. 35 (DSFA), Art. 44 ff.
 (Drittlandtransfer).
- **BDSG:** § 22 (Gesundheits-/Sozialdaten), § 26 (Beschäftigtendatenschutz), § 38
 (betrieblicher DSB).
- **TDDDG (ehem. TTDSG):** §§ 24 ff. — Einwilligung für Cookies/Endgerätezugriffe.
- **Art. 35 Abs. 4 DSGVO** i. V. m. DSK-Positivliste — nationale Pflichttatbestände.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Ungültigkeit EU-US-Privacy-Shield; Standardvertragsklauseln erfordern Transfer
 Impact Assessment; maßgeblich für Art. 44 ff. DSGVO.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Automatisiertes Scoring als Entscheidung i. S. d. Art. 22 DSGVO, wenn Dritte
 maßgeblich darauf abstellen; zentral für Triage von KI-/Scoring-Vorhaben.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Datenschutzrechtliche Haftung Art. 82 DSGVO; Beweislastverteilung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 *(Recht auf Vergessen I)* — Datenschutz als Teil des allgemeinen Persönlichkeitsrechts
 (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG); Abwägung mit Kommunikationsfreiheiten.

### Kommentare

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 — DSFA-Pflicht, Schwellenwerte, Verhältnis zu nationalen Listen.
- `Simitis/Hornung/Spiecker (Hrsg.), DSGVO, 2. Aufl. 2022, Art. 6 Rn. 30 ff.`
 — Rechtsgrundlagen; berechtigtes Interesse als Auffangtatbestand.
- `Gola (Hrsg.), DSGVO, 3. Aufl. 2022, Art. 22 Rn. 5 ff.`
 — Automatisierte Entscheidungsfindung; Abgrenzung zu Profiling.
- `Paal/Pauly (Hrsg.), DS-GVO BDSG, 3. Aufl. 2021, Art. 25 DSGVO Rn. 7 ff.`
 — Privacy by Design und Privacy by Default als Entwurfspflicht.
- `Ehmann/Selmayr (Hrsg.), DS-GVO, 2. Aufl. 2018, Art. 35 Rn. 25 ff.`
 — Anwendungsbereich der DSFA; Verhältnis zu Art. 5, 25 DSGVO.

## Ablauf

### Schritt 1: Verarbeitungsvorgang klären

Bei vager Beschreibung zuerst nachfragen: Datenkategorien (Art. 9?), Betroffenenkreis
(Beschäftigte → § 26 BDSG!), Zweck, Neu oder Zweckänderung, Auftragsverarbeiter,
automatisierte Entscheidung (Art. 22), Endgerätezugriff (§ 24 TDDDG).

### Schritt 2: Hausinternes DSA-Raster

Konfiguriertes Prüfraster aus CLAUDE.md lesen. Trigger erfüllt → mindestens
**DSA ERFORDERLICH**. Nicht erfüllt → weiter mit Schritt 3.

### Schritt 3: DSFA-Pflichtprüfung (Art. 35 DSGVO)

**Pflichttatbestände (Art. 35 Abs. 3, DSK-Positivliste):**
- Systematische automatisierte Bewertung persönlicher Aspekte inkl. Profiling mit
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Umfangreiche Verarbeitung besonderer Datenkategorien (Art. 9 DSGVO).
- Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche.

**Starke Indikatoren (kein Pflichttatbestand, aber DSFA dringend empfohlen):**
neue Technologie, Kinderdaten, Zusammenführung getrennter Datensätze,
Diskriminierungspotenzial, Cross-Context-Tracking, verhaltensbasierte Werbung.

Pflichttatbestand erfüllt → **DSFA PFLICHT**. Nur Indikatoren → **DSA ERFORDERLICH**.

### Schritt 4: Datenschutzrichtlinien-Abgleich

Vorhaben gegen konfigurierte Richtlinien prüfen. Typische Konflikte:
Datenkategorie nicht in Richtlinie erfasst; Drittlandweitergabe ohne Grundlage
(Art. 44 ff. DSGVO); Löschfristen (Art. 17) überschritten; Zweckbindung (Art. 5
Abs. 1 lit. b) verletzt; Betroffenenrechte unvollständig.

Direkter Konflikt → **STOPP**. Konflikt muss aufgelöst sein vor Fortführung.

### Schritt 5: Klassifikation und Ausgabe

```
Kurzergebnis: [DSFA PFLICHT / DSA ERFORDERLICH / FREIGABE / STOPP — ein Satz]

VORGANG: [wie verstanden]
KLASSIFIKATION: [...]
Hausinternes DSA-Raster ausgelöst? [Ja / Nein]
DSFA-Pflicht (Art. 35 DSGVO)? [Ja — Tatbestand / Nein / N/A]
Richtlinienkonflikt? [Keiner / Ja — konkreter Konflikt]
Begründung: [1–3 Sätze]
```

*Voraussetzungen bei DSA / DSFA:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| Datenschutzprüfung / DSFA (Art. 35 DSGVO) | DSB | ☐ |
| Berechtigtes-Interesse-Abwägung (Art. 6 Abs. 1 lit. f) | DSB / Legal | ☐ |
| DSB-Konsultation (DSFA-Pflichtverfahren) | DSB | ☐ |
| AVV (Art. 28 DSGVO) | Legal | ☐ |
| Richtlinienaktualisierung vor Launch | DSB | ☐ |
| Eintrag Verarbeitungsverzeichnis (Art. 30) | DSB | ☐ |

**Rechtsgrundlage (Art. 6 DSGVO):** [lit. a Einwilligung / lit. b Vertrag /
lit. c rechtliche Verpflichtung / lit. f berechtigte Interessen — oder "unklar"]

Nach Klassifikation immer anbieten: "Soll ich jetzt direkt mit der DSFA beginnen?"

*Bei STOPP:*
Konflikt benennen. Optionen: (A) Vorhaben umgestalten, (B) Richtlinie aktualisieren
(Vereinbarkeit mit Rechtsgrundlage prüfen). Keinen Weg vorschlagen, wenn keiner besteht.

### Schritt 6: Weiterleitung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 KI-Folgenabschätzung erwägen.
- **Beschäftigtendatenschutz:** § 26 BDSG und Mitbestimmung (§§ 87 Abs. 1 Nr. 6,
 94 BetrVG) prüfen.

## Beispiel

**Vorgang:** ML-basiertes Kreditscoring für Bestandskunden; Ergebnis fließt in
automatisierte Kreditentscheidung.

**Klassifikation:** DSFA PFLICHT — Art. 35 Abs. 3 lit. a DSGVO: systematische
automatisierte Bewertung persönlicher Aspekte mit erheblichen Auswirkungen
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Schufa-Scoring) reicht es, dass Dritte maßgeblich auf das Scoring abstellen.
DSB-Konsultation und Verarbeitungsverzeichnis-Eintrag (Art. 30) zwingend.

## Risiken und typische Fehler

- **"Anonymisiert" = FREIGABE:** Pseudonymisierte Daten bleiben personenbezogen
 (Art. 4 Nr. 1 DSGVO). Re-Identifikationsrisiko konkret prüfen.
- **"Wir machen das ähnlich":** Bestehende, nie geprüfte Verarbeitungen legitimieren
 keine neue. Bei anderem Umfang/Zweck/Kategorie: neu triagen.
- **"Nur ein Pilot":** Pilot mit echten Personendaten unterliegt denselben Anforderungen.
- **"Der Anbieter regelt Datenschutz":** AVV nach Art. 28 zwingend; Triage bleibt beim
 Verantwortlichen (Art. 4 Nr. 7 DSGVO).
- **Inferred Data übersehen:** Score, Risikoklasse, Präferenz = personenbezogenes Datum.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jede Klassifikation muss nennen: einschlägige DSGVO-/BDSG-Normen mit Artikel/Absatz,
DSK-Listenfundstelle bei DSFA-Pflicht, einschlägige Rechtsprechung in korrekter
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

Beispiel Rechtsprechung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Beispiel Kommentar:
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen der DSK-Blacklist/Whitelist (Art. 35 Abs. 4/5 DSGVO), neuen EDSA-Leitlinien zur DSFA sowie KI-VO-Umsetzungsakten.

**Querverweise:**
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — vollständige DSFA bei positiver Triage
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — bei Drittlandbezug in der Triage
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — bei Auftragsverarbeitung als Verarbeitungsbestandteil

## Aktuelle Rechtsprechung (Ergaenzung v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template — Triage-Ergebnis

**Adressat:** Datenschutzbeauftragter / Prozessverantwortlicher — Tonfall: sachlich-strukturiert

```
Datenschutz-Triage-Ergebnis [DATUM]
Verarbeitungsvorgang: [BEZEICHNUNG]
Beschreibung: [KURZBESCHREIBUNG]

Einstufung: FREIGABE / DSA ERFORDERLICH / DSFA PFLICHT / STOPP

Rechtsgrundlage: Art. [X] DSGVO [§ BDSG optional]
Verantwortlichkeit: Art. 24 (allein) / Art. 26 (gemeinsam) / Art. 28 (Auftragsverarbeitung)
Drittlandbezug: ja (→ Drittlandprüfung) / nein
DSFA-Pflicht: ja (Grund: [...]) / nein (Begründung: [...])

Naechste Schritte:
1. [AKTION]
2. [AKTION]

Frist: [DATUM]
Verantwortlich: [PERSON / ROLLE]
```

## 3. `avv-art-26-joint-controllership-deutsch`

**Fokus:** Joint-Controller-Vereinbarung nach Art. 26 DSGVO in deutscher Vertragssprache. Behandelt Aufgabenverteilung Anlaufstelle für Betroffene Transparenz Innenregress und EuGH-Rechtsprechung zu Fanpages Like-Button und Zeugen Jehovas. Output: deutscher Klauselsatz für Joint-Controller-Vereinbarung.

### Joint-Controller-Vereinbarung Art. 26 DSGVO – deutsche Vertragsfassung

## Zweck / Purpose

Klauselgeruest für eine Joint-Controller-Vereinbarung nach Art. 26 DSGVO in deutscher Vertragssprache, mit Aufgabenverteilung, Anlaufstelle für Betroffene und Innenregress. Purpose (EN): Joint controller agreement template under Article 26 GDPR in German.

## Wann dieses Modul hilft

- Zwei oder mehr Akteure entscheiden gemeinsam ueber Zwecke und Mittel der Verarbeitung.
- Typische Konstellationen: Fanpage und Plattformbetreiber, Co-Branding-Aktionen, Konsortien, Marktplaetze, Tracking-Anbieter und Webseitenbetreiber.
- Eine Aufsichtsbehoerde fragt nach der Vereinbarung gem. Art. 26 Abs. 1 DSGVO.

## Rechtlicher Rahmen

- Art. 26 Abs. 1 DSGVO: Wenn zwei oder mehr Verantwortliche gemeinsam die Zwecke und Mittel festlegen, legen sie in transparenter Form ihre jeweiligen Verantwortlichkeiten in einer Vereinbarung fest.
- Art. 26 Abs. 2 DSGVO: Wesentliche Aspekte der Vereinbarung muessen den Betroffenen zur Verfuegung gestellt werden.
- Art. 26 Abs. 3 DSGVO: Betroffene koennen unabhaengig von der Vereinbarung ihre Rechte gegenueber jedem Verantwortlichen geltend machen.
- Art. 82 Abs. 4 DSGVO: Gesamtschuldnerische Haftung.
- EuGH C-25/17 (Zeugen Jehovas) – verifiziert.
- EuGH C-498/16 (Wirtschaftsakademie / Fanpages) – verifiziert.
- EuGH C-40/17 (Fashion ID) – verifiziert.

## Ablauf / Checkliste

1. **Konstellation klaeren.**
 - Welche Akteure?
 - Welche Verarbeitung ist betroffen?
 - Welche Zwecke werden gemeinsam verfolgt?

2. **Aufgabenverteilung.**
 - Informationspflichten Art. 13/14 DSGVO – wer informiert wen?
 - Betroffenenrechte Art. 15 bis 22 DSGVO – wer bearbeitet?
 - Sicherheitsmassnahmen Art. 32 DSGVO – wer trifft was?
 - Meldepflichten Art. 33, 34 DSGVO – wer meldet was?
 - DSFA Art. 35 DSGVO – wer fuehrt durch?
 - Vorabkonsultation Art. 36 DSGVO – wer fuehrt durch?
 - Verarbeitungsverzeichnis Art. 30 DSGVO – wer fuehrt?

3. **Anlaufstelle festlegen.**
 - Eine zentrale Anlaufstelle für Betroffene oder mehrere?
 - Empfehlung: zentrale Anlaufstelle, um Art. 26 Abs. 3 DSGVO praktisch handhabbar zu machen.

4. **Transparenz nach Art. 26 Abs. 2 DSGVO.**
 - "Wesentliche Aspekte" der Vereinbarung muessen den Betroffenen zugaenglich gemacht werden.
 - Praxis: Veroeffentlichung in der Datenschutzerklaerung oder als eigenes Dokument auf der Webseite.

5. **Innenregress.**
 - Trotz Gesamtschuld nach Art. 82 Abs. 4 DSGVO koennen die Parteien intern den Verschuldensanteil regeln.
 - Cap-Diskussion analog zum AVV (Querverweis: avv-haftung-risikoallokation-art-82-dsgvo).

## Mustertext / Template

> "Vereinbarung ueber gemeinsame Verantwortlichkeit gemaess Art. 26 DSGVO
>
> zwischen
> [Partei A], (im Folgenden 'Partei A') und
> [Partei B], (im Folgenden 'Partei B')
> – nachfolgend gemeinsam 'Parteien' und einzeln 'gemeinsam Verantwortlicher' im Sinne von Art. 26 DSGVO –
>
> Praeambel
>
> Die Parteien fuehren die in Anlage 1 beschriebenen Verarbeitungstaetigkeiten gemeinsam durch und legen die Zwecke und Mittel der Verarbeitung gemeinsam fest. Sie sind daher gemeinsam Verantwortliche im Sinne von Art. 26 DSGVO und beabsichtigen mit dieser Vereinbarung ihre jeweiligen datenschutzrechtlichen Verantwortlichkeiten transparent festzulegen.
>
> § 1 Gegenstand der gemeinsamen Verarbeitung
> Die gemeinsame Verarbeitung umfasst die in Anlage 1 beschriebenen Verarbeitungstaetigkeiten, Datenarten, Kategorien Betroffener und Empfaengergruppen.
>
> § 2 Rollenverteilung
> (1) Partei A ist verantwortlich für
> a) die Bereitstellung der Verarbeitungsinfrastruktur;
> b) die Erfuellung der Informationspflichten gemaess Art. 13 und 14 DSGVO gegenueber den ueber Partei A erreichten Betroffenen;
> c) die Bearbeitung von Betroffenenanfragen nach Art. 15 bis 22 DSGVO, die ueber Partei A eingehen;
> d) die Erfuellung der Meldepflichten gemaess Art. 33 und 34 DSGVO im Hinblick auf Verarbeitungsteile, die Partei A allein steuert.
> (2) Partei B ist verantwortlich für
> a) die Erhebung und Erstuebermittlung der Daten an Partei A;
> b) die Erfuellung der Informationspflichten gemaess Art. 13 und 14 DSGVO gegenueber den ueber Partei B erreichten Betroffenen;
> c) die Bearbeitung von Betroffenenanfragen nach Art. 15 bis 22 DSGVO, die ueber Partei B eingehen;
> d) die Erfuellung der Meldepflichten gemaess Art. 33 und 34 DSGVO im Hinblick auf Verarbeitungsteile, die Partei B allein steuert.
> (3) Die Parteien fuehren gemeinsam durch:
> a) die Durchfuehrung einer etwaig erforderlichen DSFA gemaess Art. 35 DSGVO;
> b) die Festlegung der Loeschfristen;
> c) die Festlegung der technischen und organisatorischen Massnahmen gemaess Art. 32 DSGVO.
>
> § 3 Anlaufstelle für Betroffene
> Anlaufstelle für Anfragen Betroffener ist Partei A. Partei A leitet Anfragen, die in den Verantwortungsbereich von Partei B fallen, unverzueglich an Partei B weiter. Art. 26 Abs. 3 DSGVO bleibt unberuehrt: Betroffene koennen ihre Rechte gegenueber jeder Partei geltend machen.
>
> § 4 Transparenz gegenueber Betroffenen (Art. 26 Abs. 2 DSGVO)
> Die Parteien stellen den Betroffenen die wesentlichen Aspekte dieser Vereinbarung in ihrer jeweiligen Datenschutzerklaerung zur Verfuegung. Anlage 2 enthaelt eine zur Veroeffentlichung geeignete Kurzfassung.
>
> § 5 Sicherheit und Meldepflichten
> Die Parteien stimmen sich bei einer Datenpanne unverzueglich, spaetestens innerhalb von vierundzwanzig (24) Stunden ab Kenntnis, ueber Meldepflichten gegenueber der Aufsichtsbehoerde und gegenueber Betroffenen ab. Die Federfuehrung für die Meldung an die Aufsichtsbehoerde liegt bei der Partei, in deren Verantwortungsbereich der Vorfall faellt; bei gemeinsamem Bereich uebernimmt Partei A die Federfuehrung.
>
> § 6 Haftung und Innenregress
> Die Parteien haften gegenueber Betroffenen gesamtschuldnerisch nach Art. 82 Abs. 4 DSGVO. Im Innenverhaeltnis tragen die Parteien den Schaden im Verhaeltnis ihres jeweiligen Verschuldensanteils gemaess Art. 82 Abs. 5 DSGVO. Die Haftung im Innenverhaeltnis ist auf [BETRAG] EUR pro Schadensfall begrenzt; die Begrenzung gilt nicht bei Vorsatz und grober Fahrlaessigkeit sowie nicht für Schaeden aus der Verletzung des Lebens, des Koerpers oder der Gesundheit.
>
> § 7 Aufsichtsbehoerden
> Die Parteien unterstuetzen einander bei Anfragen und Kontrollen durch die Aufsichtsbehoerden.
>
> § 8 Laufzeit und Beendigung
> Diese Vereinbarung wird auf unbestimmte Zeit geschlossen und kann von jeder Partei mit einer Frist von sechs (6) Monaten zum Quartalsende gekuendigt werden.
>
> Anlage 1: Beschreibung der Verarbeitung
> Anlage 2: Kurzfassung zur Veroeffentlichung gemaess Art. 26 Abs. 2 DSGVO"

## Typische Drafting-Fehler

- Es wird ein AVV statt eines Joint-Agreement abgeschlossen.
- Aufgabenverteilung pauschal "beide gemeinsam".
- Keine Anlaufstelle definiert.
- Wesentliche Aspekte werden den Betroffenen nicht zugaenglich gemacht (Verstoss gegen Art. 26 Abs. 2 DSGVO).
- Innenregress nicht geregelt.
- Bei Webtracking: keine Beruecksichtigung der Erstuebermittlungsphase.

## Quellen Stand 06/2026

- Art. 26, Art. 13, Art. 14, Art. 82 Abs. 4 und Abs. 5 DSGVO.
- EDSA-Leitlinien 07/2020 (Final 07.07.2021).
- EuGH C-25/17 – verifiziert.
- EuGH C-498/16 – verifiziert.
- EuGH C-40/17 – verifiziert.
- Volltexte ueber curia.europa.eu pruefen.
- Zitierweise: `../../../references/zitierweise.md`.

## 4. `avv-art-28-dsgvo-grundtatbestand`

**Fokus:** Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO. Klaert Rollenzuordnung Verantwortlicher gegen Auftragsverarbeiter wenn ein Dienstleister personenbezogene Daten im fremden Auftrag verarbeitet. Wann gilt Art. 28 wann Art. 26 wann Funktionsuebertragung. Output: Pruefvermerk zur Rollenzuordnung und AVV-Pflicht.

### Auftragsverarbeitung Art. 28 DSGVO – Grundtatbestand

## Zweck / Purpose

Strukturierte Pruefung, ob ein Vertragsverhaeltnis dem Grundtatbestand der Auftragsverarbeitung nach Art. 28 DSGVO unterfaellt und damit ein Auftragsverarbeitungsvertrag (AVV / Data Processing Agreement, DPA) abzuschliessen ist. Purpose (EN): Determine whether a contractual relationship triggers Art. 28 GDPR data processing on behalf of a controller and therefore requires a DPA.

## Wann dieses Modul hilft

- Mandant bezieht einen IT-/Cloud-/SaaS-Dienst und ist unsicher, ob AVV erforderlich ist.
- Mandant ist Anbieter und prueft, ob er als Auftragsverarbeiter einzustufen ist.
- Es bestehen Zweifel, ob nicht stattdessen Art. 26 DSGVO (gemeinsame Verantwortlichkeit) oder eine eigenstaendige Verantwortlichkeit (Funktionsuebertragung, separate Verantwortliche) vorliegt.
- Eine Aufsichtsbehoerde fragt nach Rollenzuordnung im Verarbeitungsverzeichnis (Art. 30 DSGVO).

## Rechtlicher Rahmen

- Art. 4 Nr. 7 DSGVO: Verantwortlicher entscheidet ueber Zwecke und Mittel.
- Art. 4 Nr. 8 DSGVO: Auftragsverarbeiter verarbeitet im Auftrag des Verantwortlichen.
- Art. 28 Abs. 1 DSGVO: Auswahl nur solcher Auftragsverarbeiter, die hinreichende Garantien bieten.
- Art. 28 Abs. 3 DSGVO: AVV in Schriftform oder elektronisch; Mindestinhalte lit. a bis h.
- Art. 28 Abs. 10 DSGVO: Eigenstaendige Verantwortlichkeit des Auftragsverarbeiters bei Ueberschreiten der Weisungen.
- Art. 29 DSGVO: Weisungsgebundenheit der Verarbeitung.
- § 62 BDSG: Spezialnormen für öffentliche Stellen.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (angenommen 07.07.2021).

## Ablauf / Checkliste

1. **Sachverhalt erfassen.**
 - Welche personenbezogenen Daten werden verarbeitet?
 - Welcher Akteur entscheidet ueber Zweck (Wozu?) und Mittel (Wie?)?
 - Gibt es Weisungsmoeglichkeiten und Weisungsrechte?
 - Welchen wirtschaftlichen Vorteil zieht jeder Akteur aus der Verarbeitung?

2. **Drei-Stufen-Test für Rollenzuordnung.**

 | Frage | Indiz für Auftragsverarbeitung | Indiz gegen Auftragsverarbeitung |
 |---|---|---|
 | Wer legt Zweck fest? | Verantwortlicher allein | Dienstleister mitbestimmend |
 | Wer legt wesentliche Mittel fest? | Verantwortlicher | Dienstleister bestimmt Architektur und Datenlogik |
 | Eigene Datennutzung des Dienstleisters? | Nein, nur weisungsgebunden | Ja, für eigene Zwecke (Werbung, KI-Training, Statistik) |
 | Wirtschaftliches Interesse | Verantwortlicher | Dienstleister hat eigenes Interesse an Daten |
 | Berufsbild | Reiner Auftragnehmer | Eigene Rechtsdienstleistung, Berufstraegerstellung |

3. **Negativabgrenzung.**
 - **Funktionsuebertragung:** Bei Berufsgeheimnistraegern (Steuerberater, Rechtsanwaelte, Aerzte), Inkassodienstleistern und Wirtschaftspruefern ist die Rollenzuordnung wegen § 203 StGB und § 43a Abs. 2 BRAO besonders kritisch (Querverweis: funktionsuebertragung-vs-auftragsverarbeitung).
 - **Gemeinsame Verantwortlichkeit (Art. 26 DSGVO):** Wenn beide Akteure gemeinsam ueber Zwecke und Mittel entscheiden – EuGH C-210/16 Wirtschaftsakademie, EuGH C-40/17 Fashion ID, EuGH C-25/17 Zeugen Jehovas.
 - **Getrennte Verantwortlichkeit:** Wenn jeder Akteur dieselben Daten für eigene Zwecke mit eigener Rechtsgrundlage verarbeitet.

4. **Rechtsfolge feststellen.**
 - Auftragsverarbeitung bejaht: AVV-Pflicht nach Art. 28 Abs. 3 DSGVO.
 - Keine Verarbeitung im Auftrag, sondern Art. 26 DSGVO: Joint-Controller-Vereinbarung (Querverweis: avv-art-26-joint-controllership-deutsch).
 - Funktionsuebertragung: Eigener Vertragstyp, ggf. Datenuebermittlungsklausel und Geheimhaltungsvereinbarung statt AVV.

5. **Dokumentation.**
 - Im Verarbeitungsverzeichnis Art. 30 DSGVO: Rolle eintragen.
 - AVV als Anlage zum Hauptvertrag oder eigenstaendig.

## Mustertext / Template

Praeambel-Klausel für einen AVV nach Art. 28 DSGVO:

> "Der Auftraggeber (im Folgenden 'Verantwortlicher' im Sinne des Art. 4 Nr. 7 DSGVO) beauftragt den Auftragnehmer (im Folgenden 'Auftragsverarbeiter' im Sinne des Art. 4 Nr. 8 DSGVO) mit der Verarbeitung personenbezogener Daten im Auftrag und nach Weisung des Verantwortlichen. Gegenstand, Dauer, Art und Zweck der Verarbeitung, die Art der personenbezogenen Daten sowie die Kategorien betroffener Personen sind in Anlage 1 abschliessend beschrieben. Der Auftragsverarbeiter verarbeitet die personenbezogenen Daten ausschliesslich auf dokumentierte Weisung des Verantwortlichen, soweit nicht eine Verarbeitungspflicht nach Unionsrecht oder dem Recht der Mitgliedstaaten besteht; in diesem Fall teilt der Auftragsverarbeiter dem Verantwortlichen diese rechtliche Verpflichtung vor der Verarbeitung mit, sofern das betreffende Recht eine solche Mitteilung nicht wegen eines wichtigen öffentlichen Interesses verbietet."

## Typische Drafting-Fehler

- AVV abgeschlossen, obwohl tatsaechlich Art. 26 DSGVO (gemeinsame Verantwortlichkeit) gegeben ist – falsche Rollenzuordnung wird durch AVV nicht geheilt.
- Pauschalverweis auf "Datenschutz" statt konkreter Mindestinhalte nach Art. 28 Abs. 3 lit. a bis h DSGVO.
- AVV mit Berufstraegern ohne Beruecksichtigung von § 203 StGB.
- Vermischung mit allgemeinen Geheimhaltungsklauseln; AVV-Pflichten sind eigenstaendig.
- AVV erst nach Verarbeitungsbeginn abgeschlossen (Art. 28 Abs. 9 DSGVO Form).

## Quellen Stand 06/2026

- DSGVO Art. 4 Nr. 7, Nr. 8, Art. 28, Art. 29.
- BDSG § 62.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021); abrufbar ueber edpb.europa.eu.
- EuGH C-25/17 (Zeugen Jehovas) – verifiziertes Aktenzeichen; Volltext ueber curia.europa.eu pruefen.
- EuGH C-210/16 (Wirtschaftsakademie / Fanpages) – Aktenzeichen verifiziert.
- EuGH C-40/17 (Fashion ID) – Aktenzeichen verifiziert.
- Verbindlich zur Zitierweise: `../../../references/zitierweise.md`.
- Kommentar-, Handbuch- und Aufsatzfundstellen nur, wenn der Mandant die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## 5. `avv-art-28-mindestinhalte-checkliste`

**Fokus:** Vollstaendige Pflichtinhalte-Checkliste für einen AVV nach Art. 28 Abs. 3 lit. a bis h DSGVO. Jede der acht Pflichtklauseln mit Sollformulierung Fallback-Position und Auditfrage. Geeignet für das Drafting eines neuen AVV oder das Auditing eines bestehenden AVV. Output: Klausel-für-Klausel-Pruefraster.

### AVV-Mindestinhalte nach Art. 28 Abs. 3 DSGVO – Klauselcheckliste

## Zweck / Purpose

Pflichtinhalte-Checkliste für Auftragsverarbeitungsvertraege nach Art. 28 Abs. 3 DSGVO – Klausel für Klausel mit Soll-Position, Fallback und Pruefkriterium. Purpose (EN): Mandatory-content checklist for DPAs under Art. 28 (3) GDPR, clause by clause.

## Wann dieses Modul hilft

- Beim Drafting eines neuen AVV ist sicherzustellen, dass alle acht Pflichtinhalte vollstaendig sind.
- Beim Auditing eines vorgelegten AVV ist zu pruefen, ob jede Pflichtklausel ihren Mindestanforderungen genuegt.
- Bei Aufsichtsbehoerden-Pruefungen ist der vollstaendige Pflichtkatalog nachweisbar zu dokumentieren.

## Rechtlicher Rahmen

- Art. 28 Abs. 3 Satz 1 DSGVO: Vertrag oder anderes Rechtsinstrument in Schriftform, einschliesslich elektronisch.
- Art. 28 Abs. 3 Satz 2 DSGVO: Gegenstand und Dauer, Art und Zweck der Verarbeitung, Datenkategorien und Kategorien Betroffener, Pflichten und Rechte des Verantwortlichen.
- Art. 28 Abs. 3 Satz 2 lit. a bis h DSGVO: Acht Pflichtklauseln.

## Ablauf / Checkliste

### Rahmenangaben (Art. 28 Abs. 3 Satz 2 DSGVO)

| Pflichtangabe | Pruefkriterium |
|---|---|
| Gegenstand der Verarbeitung | Konkret benannt, nicht "Datenschutz allgemein" |
| Dauer | Vertragslaufzeit, ggf. Verlaengerung |
| Art und Zweck | Operative Funktion und Geschaeftszweck |
| Art der personenbezogenen Daten | Datenarten katalogisiert (Stammdaten, Verkehrsdaten, Inhaltsdaten, besondere Kategorien Art. 9 DSGVO) |
| Kategorien Betroffener | Mitarbeitende, Mandanten, Kinder, Patienten etc. |
| Pflichten und Rechte des Verantwortlichen | Mindestens Weisungsrechte, Kontrollrechte, Beendigungsrechte |

### Die acht Pflichtklauseln (Art. 28 Abs. 3 Satz 2 lit. a bis h DSGVO)

**lit. a – Weisungsgebundenheit.** Verarbeitung nur auf dokumentierte Weisung des Verantwortlichen, einschliesslich Drittlandtransfer. Auditfrage: Wer fuehrt das Weisungsregister?

**lit. b – Vertraulichkeit.** Personen, die zur Verarbeitung befugt sind, haben sich zur Vertraulichkeit verpflichtet oder unterliegen einer angemessenen gesetzlichen Verschwiegenheitspflicht. Auditfrage: Liegen Vertraulichkeitserklaerungen vor?

**lit. c – Technische und organisatorische Massnahmen (TOM, Art. 32 DSGVO).** Auftragsverarbeiter trifft alle erforderlichen Massnahmen nach Art. 32 DSGVO. Auditfrage: TOM-Anlage aktuell und konkret? (Querverweis: avv-tom-art-32-dsgvo-anlage)

**lit. d – Sub-Auftragsverarbeiter (Art. 28 Abs. 2 und Abs. 4 DSGVO).** Einsatz nur mit allgemeiner oder besonderer schriftlicher Genehmigung; bei allgemeiner Genehmigung Informationspflicht ueber geplanten Wechsel. Auditfrage: Aktuelle Liste vorhanden? Widerspruchsfrist angemessen?

**lit. e – Unterstuetzung Betroffenenrechte (Art. 12 bis 23 DSGVO).** Geeignete technische und organisatorische Massnahmen, um Erfuellung der Betroffenenrechte zu unterstuetzen (Auskunft, Loeschung, Berichtigung, Datenuebertragbarkeit). Auditfrage: SLA für Betroffenenanfragen?

**lit. f – Unterstuetzung Art. 32 bis 36 DSGVO.** Unterstuetzung bei TOM, Meldepflicht (Art. 33 DSGVO), Benachrichtigung Betroffener (Art. 34 DSGVO), DSFA (Art. 35 DSGVO), Konsultation Aufsichtsbehoerde (Art. 36 DSGVO). Auditfrage: Meldewege definiert?

**lit. g – Loeschung oder Rueckgabe.** Nach Wahl des Verantwortlichen alle personenbezogenen Daten loeschen oder zurueckgeben nach Ende des Auftrags, ausser gesetzliche Aufbewahrungspflichten. Auditfrage: Format der Rueckgabe definiert? (Querverweis: avv-loeschung-rueckgabe-nach-vertragsende)

**lit. h – Audit und Nachweis.** Alle erforderlichen Informationen zum Nachweis bereitstellen; Ueberpruefungen einschliesslich Inspektionen durch Verantwortlichen oder Pruefer ermoeglichen. Auditfrage: Frequenz, Form, Kosten geregelt? (Querverweis: avv-audit-und-kontrollrechte)

## Mustertext / Template

Konsolidierte Pflichtklausel-Liste (Kurzform für Vertragsanlage):

```
§ X Pflichten des Auftragsverarbeiters
(1) Weisungsgebundenheit (Art. 28 Abs. 3 lit. a DSGVO).
(2) Vertraulichkeit (Art. 28 Abs. 3 lit. b DSGVO).
(3) Technische und organisatorische Massnahmen gemaess Anlage TOM (Art. 28 Abs. 3 lit. c i.V.m. Art. 32 DSGVO).
(4) Sub-Auftragsverarbeiter nach Massgabe von § Y (Art. 28 Abs. 3 lit. d i.V.m. Abs. 2 und Abs. 4 DSGVO).
(5) Unterstuetzung bei Betroffenenrechten (Art. 28 Abs. 3 lit. e DSGVO).
(6) Unterstuetzung bei Sicherheit, Meldepflicht, Benachrichtigung, DSFA, Vorabkonsultation (Art. 28 Abs. 3 lit. f DSGVO).
(7) Rueckgabe oder Loeschung nach Vertragsende gemaess Anlage Loeschkonzept (Art. 28 Abs. 3 lit. g DSGVO).
(8) Audit- und Kontrollrechte gemaess § Z (Art. 28 Abs. 3 lit. h DSGVO).
```

## Typische Drafting-Fehler

- Rahmenangaben fehlen oder sind zu allgemein ("Daten unserer Kunden").
- lit. a wird auf "Vertragserfuellung" reduziert ohne Weisungsregister.
- lit. b wird mit allgemeiner Geheimhaltungsklausel verwechselt; spezifische Vertraulichkeit für Verarbeitungsbefugte fehlt.
- TOM-Anlage (lit. c) ist Marketingbroschuere statt konkrete Massnahmen.
- lit. d laesst Sub-AV-Wechsel ohne Widerspruchsfrist zu.
- lit. e ohne SLA und ohne Kostenregelung.
- lit. g ohne klare Wahlmoeglichkeit (Loeschung oder Rueckgabe) und ohne Format.
- lit. h verweist auf Zertifikate, ohne eigenes Audit-Recht zuzulassen.

## Quellen Stand 06/2026

- Art. 28 Abs. 3 DSGVO – Pflichtinhalte des Vertrags.
- Art. 28 Abs. 2, Abs. 4 DSGVO – Sub-Auftragsverarbeiter.
- Art. 28 Abs. 9 DSGVO – Schriftform inklusive elektronisch.
- Art. 29 DSGVO – Weisungsgebundenheit.
- EDSA-Leitlinien 07/2020 – Final 07.07.2021; abrufbar ueber edpb.europa.eu.
- Zitierweise: `../../../references/zitierweise.md`.

