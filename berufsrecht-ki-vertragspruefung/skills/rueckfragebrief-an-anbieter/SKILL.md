---
name: rueckfragebrief-an-anbieter
description: "Erstelle einen strukturierten Rueckfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen Pflichten. Aufbau Anschreiben Kontext drei Fragenbloecke (Verschwiegenheit Subunternehmer TOM und Drittstaat) Fragen zu Zertifizierungen und Versprechungen Frist Unterschrift. Klare praezise Fragen die der Anbieter beantworten kann."
---

# Rückfragebrief an Anbieter

## Disclaimer

Diese Forprüfung ist keine Rechtsberatung, sondern strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Zweck

Der Rückfragebrief operationalisiert die im Gutachten festgestellten Lücken in konkrete, präzise Fragen an den Anbieter. Er ist die zentrale Schnittstelle zwischen interner Bewertung und externer Verhandlung.

## Aufbau

### Briefkopf

- Absender: Kanzlei mit Berufsbezeichnung
- Empfänger: Anbieter, vertretungsberechtigte Person
- Datum
- Betreff: "Berufsrechtliche und strafrechtliche Anforderungen — Vertrag [Produktname]"

### Anschreiben

Kurze Einleitung — die Kanzlei prüft den Einsatz des KI-Produkts und benötigt vor Vertragsschluss bzw. zur Fortsetzung des Vertragsverhältnisses Klarstellungen zu den berufsrechtlichen Anforderungen aus §§ [Norm-Adapter] und § 203 StGB.

### Inhaltliche Blöcke

#### Block 1 — Verschwiegenheit und Belehrung

- Wo und wie ist die Verschwiegenheit Ihres Hauses gegenüber der Kanzlei vertraglich geregelt? Bitte konkrete Fundstelle.
- Gilt die Verschwiegenheit gegenüber jedermann und zeitlich unbegrenzt?
- Wie haben Sie Ihre Mitarbeiter zur Verschwiegenheit verpflichtet (Textform nach § 126b BGB)?
- Wie werden Mitarbeiter und Subunternehmer über die strafrechtlichen Folgen einer Pflichtverletzung nach §§ 203, 204 StGB belehrt? Liegt der Normtext als Anlage zu den Mitarbeiterverträgen vor?

#### Block 2 — Subunternehmer

- Bitte legen Sie die aktuelle, abschließende Liste aller Subunternehmer (insbesondere Modellanbieter und Hoster) mit Sitz, Funktion und Verarbeitungsstandort vor.
- Wie werden Subunternehmer vertraglich auf die Verschwiegenheit verpflichtet und über §§ 203, 204 StGB belehrt?
- Welche Vorabinformations- und Zustimmungsrechte hat die Kanzlei bei Hinzunahme oder Wechsel von Subunternehmern?
- Falls Microsoft Azure oder AWS oder Google Cloud zum Einsatz kommt: Welche Region wird genutzt? Wo liegen Backups?

#### Block 3 — Erforderlichkeit, no training, Speicherdauer

- Welche konkreten Datenkategorien werden bei der Nutzung Ihres Dienstes verarbeitet?
- Werden eingegebene Daten zum Training Ihres Modells oder eines Drittmodells verwendet? Bitte vertragliche "no training"-Zusicherung mit Fundstelle.
- Wie lange werden Eingaben gespeichert? Liegt eine Zero-Retention-Klausel vor?
- Wie erfolgt die Löschung am Vertragsende? Erhalten wir ein Löschprotokoll?

#### Block 4 — Strafprozessuale Absicherung

- Wie verhält sich Ihr Haus bei behördlichen Auskunftsverlangen, Durchsuchungs- oder Beschlagnahmeanordnungen?
- Werden Sie die Kanzlei unverzüglich vorab informieren (soweit gesetzlich zulässig)?
- Werden Sie sich gegen unzulässige Beschlagnahmen mit Hinweis auf §§ 53a, 97 StPO zur Wehr setzen?
- Gilt deutsches Recht? Ist der Gerichtsstand Deutschland?

#### Block 5 — TOM und Zertifizierungen

- Welche aktuellen Zertifikate liegen vor (ISO 27001, BSI C5 Typ 2, SOC 2 Typ 2)? Bitte Geltungsbereich, Zertifizierungsstelle und Ausstellungsdatum.
- Wo werden Daten gespeichert (Verarbeitungsstandort und Backupstandort)?
- Welche Verschlüsselung wird im Transport und im Ruhezustand eingesetzt?
- Welche Audit-Logs werden geführt? Wie lange?
- Welche Meldefrist gilt für Sicherheitsvorfälle?

#### Block 6 — Drittstaaten und CLOUD Act

- Sind Sie ein US-Konzern oder eine US-Tochter? Findet US-Recht (CLOUD Act, FISA) auf Ihre Daten Anwendung?
- Liegen Daten oder Backups in Drittstaaten?
- Sind Sie bereit, ein Professional Secrecy Addendum zu unterzeichnen, das US-Auskunftsverlangen anficht und uns informiert?

### Fristsetzung und Hinweise

- Konkrete Frist (typisch zwei bis vier Wochen)
- Hinweis, dass ohne Klarstellung ein Vertragsschluss bzw. eine Fortsetzung berufsrechtlich nicht möglich ist
- Hinweis auf Vertraulichkeit der Anfrage

### Unterschrift

- Name, Funktion (Partner, Compliance-Officer)
- Berufsbezeichnung

## Ton

Sachlich, präzise, keine Anschuldigungen. Der Anbieter soll motiviert sein zu antworten. Die Kanzlei dokumentiert dadurch zugleich die Sorgfalt nach Abs. 2 der Dienstleisterregelung.

## Output

Vollständiger Briefentwurf im Markdown. PDF-Export möglich.

## Disclaimer im Brief

Der Brief ist eine berufsrechtliche und strafrechtliche Anfrage, keine zivilrechtliche Geltendmachung. Eine zivilrechtliche oder gar strafrechtliche Geltendmachung ist im Streitfall einem spezialisierten Rechtsanwalt vorbehalten.

## Aktuelle Rechtsprechung

- BGH, Urt. v. 25.03.2021 — VII ZR 94/20, NJW 2021, 1954 Rn. 28: Vertragsklauseln, die den Anbieter nicht eindeutig an berufsrechtliche Anforderungen binden, sind im Zweifel eng auszulegen — daher müssen Klauseln im Vertragstext stehen, nicht nur in FAQs oder Trust-Center-Versprechen.
- BGH, Urt. v. 19.03.2019 — XI ZR 9/18, NJW 2019, 2080 Rn. 45: Textformklausel nach § 126b BGB; schriftliche Rückfrageantworten des Anbieters erfüllen Textform und können als vertragliche Zusicherungen gewertet werden.
- OLG Köln, Urt. v. 14.01.2020 — 19 U 93/19, NJW-RR 2020, 678 Rn. 22: Zur Haftung für unrichtige vorvertragliche Angaben; Anbieterauskünfte im Rückfrageverfahren können vorvertragliche Aufklärungspflichten nach §§ 241 Abs. 2, 311 Abs. 2 BGB begründen.
- BGH, Urt. v. 08.10.2020 — III ZR 1/20, NJW 2021, 156 Rn. 38: Zum Vorrang verhandelter Individualklauseln (§ 305b BGB) gegenüber AGB; Rückfrageantworten können zu Individualvereinbarungen werden, wenn sie konkret und für den Vertrag bindend sind.

## Zentrale Normen (Paragrafenkette)

- §§ 241 Abs. 2, 311 Abs. 2 BGB — Vorvertragliche Aufklärungspflichten
- § 305b BGB — Vorrang der Individualabrede
- § 126b BGB — Textform
- § 43e Abs. 3 BRAO, § 62a Abs. 3 StBerG etc. — Vertragsinhalt der Dienstleisterregelung

## Kommentarliteratur

- Grüneberg/Grüneberg BGB, 83. Aufl. 2024, § 305b Rn. 1–15: Zum Vorrang von Individualabreden; wie Rückfrageantworten Vertragsbestandteil werden.
- Henssler/Prütting BRAO, 5. Aufl. 2023, § 43e Rn. 30–45: Pflichtinhalte des Dienstleistervertrags; was schriftlich (Textform) festgehalten werden muss.

## Triage zu Beginn

1. Welche Lücken hat die bisherige Vertragsprüfung ergeben (Ampel: gelb/rot)?
2. Welche Fragen sind klärungsbedürftig (Subunternehmer, Training, Drittstaat)?
3. Ist ein Fristdruck vorhanden (laufende Pilotprojekte, Vertragsbeginn)?
4. Soll die Antwort des Anbieters als vertragliche Zusicherung eingestuft werden?

## Output-Template — Rückfragebrief

**Adressat:** KI-Anbieter — Tonfall: sachlich-präzise, fristsetzend

```
[KANZLEINAME]
[ANSCHRIFT]
[DATUM]

An: [ANBIETER, RECHTSABTEILUNG / DATENSCHUTZTEAM]
Betr.: Rückfrageverfahren berufsrechtliche Compliance — [PRODUKTNAME]
Unser Aktenzeichen: [AZ]

Sehr geehrte Damen und Herren,

wir pruefen den Einsatz von [PRODUKT] in unserer Kanzlei im Hinblick auf die 
berufsrechtlichen Anforderungen nach § [NORM] [GESETZ] sowie §§ 203, 204 StGB.
Dazu bitten wir um Beantwortung der folgenden Fragen bis zum [FRIST + 14 TAGE]:

Frageblock 1 — Verschwiegenheit
F1: Sind Ihre Mitarbeiter und alle Subunternehmer in Textform zur Verschwiegenheit 
    ueber alle von uns eingegebenen Daten verpflichtet?
F2: Gilt diese Verpflichtung auch nach Vertragsende zeitlich unbegrenzt?

Frageblock 2 — Subunternehmer
F3: Welche Subunternehmer (Modellanbieter, Hoster, Support-Dienstleister) haben 
    Zugriff auf von uns eingegebene Daten?
    Bitte vollstaendige Liste: Name, Sitz, Funktion, Verarbeitungsstandort.
F4: Werden wir vor Wechsel oder Hinzunahme von Subunternehmern vorab in Textform 
    informiert?

Frageblock 3 — Training und Drittstaat
F5: Werden von uns eingegebene Daten zu Trainingszwecken genutzt? 
    (Auch aggregiert oder anonymisiert?)
F6: Wo werden unsere Daten verarbeitet und gespeichert? 
    Werden US-Server oder US-Subunternehmer eingesetzt (CLOUD-Act-Risiko)?

Wir bitten um Beantwortung in Textform.

Mit freundlichen Gruessen
[UNTERSCHRIFT]
```
