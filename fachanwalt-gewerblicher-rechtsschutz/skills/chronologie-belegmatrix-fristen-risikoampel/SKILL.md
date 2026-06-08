---
name: chronologie-belegmatrix-fristen-risikoampel
description: "Chronologie Belegmatrix Fristen Risikoampel im Plugin Fachanwalt Gewerblicher Rechtsschutz: prüft konkret Chronologie und Belegmatrix im gewerblichen Rechtsschutz, Fristen und Risikoampel im gewerblichen Rechtsschutz, Mandantenkommunikation im gewerblichen Rechtsschutz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Chronologie Belegmatrix Fristen Risikoampel

## Arbeitsbereich

**Chronologie Belegmatrix Fristen Risikoampel** ordnet den Fall über die tragenden Prüfungslinien: Chronologie und Belegmatrix im gewerblichen Rechtsschutz, Fristen und Risikoampel im gewerblichen Rechtsschutz, Mandantenkommunikation im gewerblichen Rechtsschutz. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im gewerblichen Rechtsschutz: Zeitachse aufbauen, Dokumente chronologisch sortieren, Lücken identifizieren, Beweiskette strukturieren für Verletzungsverfahren, EV, Klagschrift und Mandantenakte. |
| `workflow-fristen-und-risikoampel` | Fristen und Risikoampel im gewerblichen Rechtsschutz: systematischer Fristencheck, Risikoampel Grün/Gelb/Rot für alle Verfahrensarten (Marke, Patent, Design, UWG, EV, Klage), Fristenkalender und Eskalationshinweise. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im gewerblichen Rechtsschutz: Mandantenbriefe, Entscheidungsvorlagen, Statusberichte, Kostenaufklärung, Beratungsprotokoll, Tonalität und BRAO-Informationspflichten. Mustertexte für alle Phasen des Mandats. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im gewerblichen Rechtsschutz: Zeitachse aufbauen, Dokumente chronologisch sortieren, Lücken identifizieren, Beweiskette strukturieren für Verletzungsverfahren, EV, Klagschrift und Mandantenakte.

# Chronologie und Belegmatrix

## Aufgabe
Diese Prüfungslinie hilft beim strukturierten Aufbau der Zeitachse und Belegmatrix: Sachverhalts-Chronologie, Dokumentenordnung und Beweiskette für anwaltliche Verfahren im gewerblichen Rechtsschutz.

## Warum Chronologie und Belegmatrix?

Eine präzise Zeitachse und lückenlose Belegmatrix sind die Basis für:
- **EV-Anträge:** Glaubhaftmachung des Kenntnisdatums (Dringlichkeit); Verletzungsdatum.
- **Klagschriften:** Lückenloser Sachverhaltsvortrag nach § 253 ZPO.
- **Schadensersatzberechnung:** Verletzungszeitraum, Mengen, Umsätze.
- **Widerspruchs- / Löschungsverfahren:** Prioritätsdaten, Erstbenutzungsdaten.
- **Mandantenkommunikation:** Nachvollziehbare Aktenlage für Übergabe.

## Chronologie-Schema

```
[Datum] Ereignis Dokument / Beleg Status
─────────────────────────────────────────────────────────────
[Anmeldetag] Schutzrecht angemeldet DPMA-Eingangsbeleg ✓ vorhanden
[Eintragungs- Schutzrecht eingetragen Registerauszug DPMA ✓ vorhanden
 datum]
[Datum] Verletzungshandlung Screenshot URL+Datum ✓ vorhanden
 erstmalig erkannt
[Datum] Kenntnis Mandant E-Mail Mandant an Kanzlei ✓ vorhanden
[Datum] Beweissicherung Testkauf mit Quittung ✓ vorhanden
[Datum] Abmahnung versandt Einschreiben-Rückschein ✓ vorhanden
[Datum] Frist Abmahnung Fristkalender ✓ offen
[Datum] Reaktion Gegenseite UE / Ablehnung / Keine ○ ausstehend
[Datum] EV-Antrag beA-Sendeprotokoll ○ ausstehend
```

## Belegmatrix

| Nr. | Dokument | Datum | Bezug im Vortrag | Format | Vorhanden? |
|---|---|---|---|---|---|
| 1 | Registerauszug DPMA | [Datum] | Schutzrecht aktiv | PDF | ✓ |
| 2 | Screenshot Verletzung | [Datum] | Verletzungshandlung | PNG/PDF | ✓ |
| 3 | Testkauf-Quittung | [Datum] | Beweissicherung | Original | ✓ |
| 4 | E-Mail Mandant (Kenntnis) | [Datum] | Dringlichkeit | PDF | ✓ |
| 5 | Abmahnung (Entwurf / Kopie) | [Datum] | Abmahnvoraussetzung | PDF | ✓ |
| 6 | Rückschein / beA-Protokoll | [Datum] | Zustellungsnachweis | Scan | ○ |
| 7 | Eidesstattliche Versicherung | [Datum] | Glaubhaftmachung | Original | ○ |
| 8 | UE der Gegenseite | [Datum] | Wiederholungsgefahr | Original | ○ |
| … | … | … | … | … | ○ |

## Lückenidentifikation

Häufige Dokumentenlücken und Schließungsstrategie:

| Lücke | Schließung |
|---|---|
| Kein Nachweis Erstbenutzung Marke | Alte Rechnungen, Kataloge, Fotos mit Datum beschaffen |
| Verletzungsdatum unklar | Wayback Machine ([web.archive.org](https://web.archive.org)); Notarprotokoll |
| Kenntnisdatum nicht dokumentiert | E-Mail-Korrespondenz suchen; Zeugen befragen; eV Mandant |
| Registerauszug veraltet | Aktuell herunterladen (DPMA-Online); Datum im Auszug sichtbar |
| Testkauf nicht organisiert | Sofortiger Testkauf mit Quittung, Versandbestätigung |
| Schutzschrift (ZSSR) nicht geprüft | [zssr.de](https://www.zssr.de) sofort prüfen |

## Checkliste Chronologie

| Schritt | Erledigt? |
|---|---|
| Anmeldetag / Entstehungsdatum Schutzrecht dokumentiert | ☐ |
| Eintragungsdatum und Verlängerungen im Register | ☐ |
| Erstbenutzungsdatum belegt (§ 4 Nr. 2, § 26 MarkenG) | ☐ |
| Verletzungsdatum und -ort konkret und datiert | ☐ |
| Kenntnisdatum Mandant belegt (Dringlichkeit EV) | ☐ |
| Beweissicherung vollständig (Testkauf, Screenshots) | ☐ |
| Abmahnungsdatum und Zustellungsnachweis | ☐ |
| Reaktion Gegenseite protokolliert | ☐ |
| Verfahrensdaten (EV, Klage) eingetragen | ☐ |

## Anwendungsbeispiel: Markenverletzung

```
Zeitachse Markenverletzung

2020-03-15 Marke "BEISPIEL" beim DPMA angemeldet (Aktenzeichen [XX])
2020-09-01 Eintragung; Registerauszug vom 2020-09-01 vorhanden
2023-11-12 Website Gegenseite: Zeichen "BEISPIEL" auf Startseite entdeckt
 → Beleg: Screenshot Anlage 1 (URL, Datum)
2023-11-12 Mandant informiert Kanzlei via E-Mail
 → Beleg: E-Mail-Ausdruck Anlage 2
2023-11-14 Testkauf von verletzendem Produkt
 → Beleg: Quittung, Foto, eV Anlage 3
2023-11-17 Abmahnung versandt per Einschreiben + beA
 → Beleg: Rückschein, beA-Protokoll Anlage 4
2023-11-24 Fristablauf (10 Tage UE-Frist)
2023-11-25 EV-Antrag beim LG Hamburg
```

## Einstieg
1. Welcher Fall liegt vor und in welchem Stadium?
2. Welche Dokumente sind bereits vorhanden?
3. Wo sind Lücken in der Zeitachse?
4. Für welchen Zweck wird die Chronologie benötigt (EV / Klageschrift / Mandantenbrief)?
5. Output: Zeitachse aufgefüllt, Belegmatrix, Lückenliste, nächster Schritt?

## Anschluss-Skills
- `workflow-dokumentenintake` – Dokumentenerfassung.
- `spezial-gewerblichen-tatbestand-beweis-und-belege` – Beweismitteldetails.
- `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` – Qualitätsgate EV.

## Quellenregel
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Wayback Machine: [web.archive.org](https://web.archive.org).
- ZSSR: [zssr.de](https://www.zssr.de).
- Register: [dpma.de](https://www.dpma.de), [euipo.europa.eu](https://euipo.europa.eu).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Lücken ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine Bewertung ohne vollständige Zeitachse.
- Kein Ersatz für vollständige Mandantenberatung.

## 2. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen und Risikoampel im gewerblichen Rechtsschutz: systematischer Fristencheck, Risikoampel Grün/Gelb/Rot für alle Verfahrensarten (Marke, Patent, Design, UWG, EV, Klage), Fristenkalender und Eskalationshinweise.

# Fristen und Risikoampel

## Aufgabe
Diese Prüfungslinie führt einen systematischen Fristencheck durch und bewertet das Risiko mit einer Ampel: Grün (sicher), Gelb (Handlungsbedarf), Rot (Eskalation sofort).

## Risikoampel-Systematik

| Ampel | Bedeutung | Handlung |
|---|---|---|
| 🟢 Grün | Alle Fristen sicher gewahrt; kein unmittelbarer Handlungsbedarf | Laufende Überwachung |
| 🟡 Gelb | Frist läuft in < 2 Wochen; Handlung vorzubereiten | Unverzüglich vorbereiten |
| 🔴 Rot | Frist läuft heute oder morgen, oder bereits abgelaufen | Sofortiger Handlungsbedarf / Schadensminimierung |

## Fristenkatalog – Gewerblicher Rechtsschutz

### EV-Vollziehungsfristen

| Frist | Norm | Laufzeit | Ampel prüfen |
|---|---|---|---|
| Vollziehungsfrist EV | § 929 Abs. 2 ZPO | 1 Monat ab Beschluss-Zustellung | → Wann Zustellung? |
| Dringlichkeit UWG | § 12 Abs. 1 UWG | ~4 Wochen nach Kenntnis | → Kenntnis seit wann? |
| Widerspruch EV | § 924 ZPO | Im Titel angegeben | → Titel vorhanden? |

### Marken-Verfahrensfristen

| Frist | Norm | Laufzeit | Auslöser |
|---|---|---|---|
| Widerspruch DPMA | § 42 Abs. 1 MarkenG | 3 Monate | Bekanntmachung Markenblatt |
| Beschwerde BPatG | § 66 Abs. 2 MarkenG | 1 Monat | Zustellung DPMA-Bescheid |
| Benutzungspflicht | § 26 MarkenG | 5 Jahre | Eintragungsdatum |
| Verlängerung Marke | MarkenG | Vor Ablauf 10 Jahre | Anmeldetag |

### Patent-Verfahrensfristen

| Frist | Norm | Laufzeit | Auslöser |
|---|---|---|---|
| Einspruch EPA | Art. 99 EPÜ | 9 Monate | Erteilungstag |
| Jahresgebühr Patent | § 17 PatG | Jährlich ab 3. Jahr | Anmeldetag |
| Nachzahlungsfrist Jahresgebühr | § 17 Abs. 4 PatG | + 2 Monate | Fälligkeit |
| Nichtigkeitsklage BPatG | § 81 PatG | Keine absolute Frist; Verjährung beachten | – |

### Design-Fristen

| Frist | Norm | Laufzeit | Auslöser |
|---|---|---|---|
| Verlängerung Design | § 27 DesignG | Vor Ablauf 5-Jahres-Periode | Anmeldetag |
| Nichtigkeitsantrag DPMA | § 33 DesignG | Keine absolute Frist | – |
| Schutzfrist nicht eingetragenes GGM | Art. 11 GGV | 3 Jahre ab Offenbarung | Offenbarungsdatum |

### Zivilprozess-Fristen

| Frist | Norm | Laufzeit | Auslöser |
|---|---|---|---|
| Berufung | § 517 ZPO | 1 Monat | Zustellung Urteil |
| Berufungsbegründung | § 520 Abs. 2 ZPO | 2 Monate | Zustellung Urteil |
| Revision | § 548 ZPO | 1 Monat | Zustellung Urteil |
| Verjährung Unterlassung UWG | § 11 Abs. 1 UWG | 6 Monate | Kenntnis |
| Verjährung Schadensersatz | §§ 195, 199 BGB | 3 Jahre | Ende des Jahres der Kenntnis |

## Fristenkontroll-Tabelle (Ausfüllmuster)

| Verfahren / Frist | Fristauslöser (Datum) | Fristende | Erledigt? | Ampel |
|---|---|---|---|---|
| Widerspruch DPMA (Marke X) | [Bekanntmachung] | +3 Monate | ☐ | |
| EV-Vollziehung | [Beschluss-Zustellung] | +1 Monat | ☐ | |
| EPA-Einspruch Patent Y | [Erteilungsdatum] | +9 Monate | ☐ | |
| Verlängerung Marke Z | [Anmeldetag] | [Ablauf] | ☐ | |
| Berufungsfrist | [Urteil-Zustellung] | +1 Monat | ☐ | |

## Eskalationshinweise bei Rot

**Wenn eine Frist bereits abgelaufen ist:**
1. Sofortige Schadensminimierung (Wiedereinsetzung § 91a ZPO / § 123 MarkenG?).
2. Mandant informieren; Haftungsrisiko dokumentieren.
3. Rechtsmittel gegen Fristversäumnis prüfen (Wiedereinsetzung in den vorigen Stand).
4. Anwaltliche Haftpflichtversicherung informieren (§ 51 BRAO).

**Wenn Dringlichkeit (EV) selbst widerlegt:**
1. Prüfen, ob Untätigkeit begründbar (komplexer Sachverhalt, laufende Verhandlungen).
2. Abmahnstrategie ohne EV; Hauptsacheklage.
3. Schadensbegrenzung dokumentieren.

## Einstieg
1. Welches Verfahren / welche Fristen sind zu prüfen?
2. Liegen Auslöse-Daten vor (Bekanntmachungsdatum, Zustellungsdatum, Kenntnisdatum)?
3. Gibt es bereits einen Kalender oder soll einer erstellt werden?
4. Welche Fristen laufen als nächstes ab (Top 3)?
5. Output: Fristenkontroll-Tabelle ausgefüllt, Risikoampel je Frist, Eskalationshinweise?

## Anschluss-Skills
- `spezial-rechtsschutz-fristen-form-und-zuständigkeit` – Normen zu Fristen.
- `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung` – EV-Fristen.
- `gr-portfolio-pflege-workflow` – Portfolio-Fristen.

## Quellenregel
- ZPO, MarkenG, PatG, DesignG, EPÜ: [gesetze-im-internet.de](https://www.gesetze-im-internet.de), [epo.org](https://www.epo.org).
- DPMA: [dpma.de](https://www.dpma.de); BPatG: [bundespatentgericht.de](https://www.bundespatentgericht.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine automatische Fristberechnung ohne vollständige Eingangsdaten.
- Kein Ersatz für vollständige Mandantenberatung und laufende Fristenüberwachung.

## 3. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im gewerblichen Rechtsschutz: Mandantenbriefe, Entscheidungsvorlagen, Statusberichte, Kostenaufklärung, Beratungsprotokoll, Tonalität und BRAO-Informationspflichten. Mustertexte für alle Phasen des Mandats.

# Mandantenkommunikation

## Aufgabe
Diese Prüfungslinie unterstützt die gesamte Mandantenkommunikation im gewerblichen Rechtsschutz: von der Erstberatung über laufende Statusberichte bis zur Mandatsabschluss-Kommunikation.

## BRAO-Informationspflichten

| Pflicht | Norm | Inhalt |
|---|---|---|
| Aufklärung über Kosten | § 49b BRAO; § 10 RVG | Vor der Mandatsübernahme; Vergütungshinweis |
| Interessenkonflikte | § 43a BRAO | Keine Vertretung widerstreitender Interessen |
| Sachgerechte Information | § 11 BORA | Aktuelle, zutreffende Informationen zum Stand |
| Fristmitteilung | Allgemeine Sorgfaltspflicht | Fristen proaktiv mitteilen |
| Keine irreführende Darstellung | BRAO allg. | Erfolgschancen nicht übertreiben |

## Kommunikationsphasen

### Phase 1: Erstberatung

**Inhalt:**
- Kurzer Sachverhaltsüberblick (was der Mandant schildert).
- Einschätzung (Risikoampel: Grün / Gelb / Rot).
- Handlungsoptionen mit Vor-/Nachteilen.
- Kostenaufklärung (Streitwert-Schätzung, Gebühren, Gerichtskosten, Risiko).
- Klare Frage: Mandat erteilt? Welche Option?

**Tonalität:** Ruhig, klar, keine Panik; realistische Einschätzung.

### Phase 2: Laufende Bearbeitung

**Statusbericht (Muster):**

```
Statusbericht Mandat [Aktenzeichen]
Stand: [Datum]

I. Sachstand
[1–2 Sätze: Wo stehen wir]

II. Letzte Aktivitäten
- [Datum]: [Maßnahme] → Ergebnis: [...]
- [Datum]: [Maßnahme] → Ergebnis: [...]

III. Nächste Schritte
- [Maßnahme] bis [Datum]: Verantwortlich: [Name]

IV. Offene Punkte (Ihre Mithilfe benötigt)
- [Bitte um Unterlagen / Entscheidung / Freigabe]

V. Kosten aktuell
Bislang entstanden: EUR [Betrag]
Voraussichtlich gesamt: EUR [Schätzung]
```

### Phase 3: Entscheidungsvorlagen

Bei jeder wichtigen Weichenstellung:

```
Entscheidungsvorlage – [Thema]
Mandat: [Aktenzeichen] – Datum: [Datum]

Sachverhalt: [2 Sätze]

Option A: [Beschreibung]
 Vorteil: ...
 Nachteil / Risiko: ...
 Kosten: ca. EUR [Betrag]

Option B: [Beschreibung]
 Vorteil: ...
 Nachteil / Risiko: ...
 Kosten: ca. EUR [Betrag]

Unsere Empfehlung: Option [A/B], weil [Begründung in 2 Sätzen].

Bitte geben Sie uns bis [Datum, Uhrzeit] Ihre Entscheidung bekannt.
```

### Phase 4: Mandatsabschluss

**Abschlussbrief (Muster):**

```
Abschlussbrief Mandat [Aktenzeichen]

Sehr geehrte/r [Mandant],

das Mandat ist abgeschlossen. Zusammenfassung:

Ergebnis: [Kurze Beschreibung: Unterlassung / Vergleich / Urteil / Einigung]
Kosten gesamt: EUR [Betrag] (davon Ihr Anteil: EUR [Betrag])
Zahlungseingang: [Datum]

Hinweise für die Zukunft:
- [z.B. Benutzungsnachweis der Marke weiterführen]
- [z.B. Portfoliopflege – nächste Verlängerung am ...]

Wir danken für das Vertrauen und stehen für künftige Mandate gerne zur Verfügung.

[Kanzlei]
```

## Tonalitäts-Leitfaden

| Situation | Tonalität |
|---|---|
| Erste Kontaktaufnahme | Professionell, offen, keine Panik |
| Eilsituation (Frist läuft) | Klar, direkt, handlungsorientiert |
| Schlechte Nachricht (Klage abgewiesen) | Ehrlich, ruhig, Alternativen aufzeigen |
| Gute Nachricht (EV erwirkt) | Positiv, aber nüchtern; nächste Schritte sofort |
| Kostenüberschreitung | Frühzeitig informieren; Gründe erläutern |

## Checkliste Mandantenkommunikation

| Schritt | Erledigt? |
|---|---|
| Kostenaufklärung vor Mandatsübernahme | ☐ |
| Interessenkonflikt-Check | ☐ |
| Erstbewertung (Risikoampel) kommuniziert | ☐ |
| Fristen proaktiv mitgeteilt | ☐ |
| Entscheidungsvorlagen bei Weichenstellungen | ☐ |
| Statusberichte in regelmäßigen Abständen | ☐ |
| Abschlussbrief versandt | ☐ |
| Originalunterlagen zurückgegeben / archiviert | ☐ |

## Einstieg
1. In welcher Phase des Mandats befindet sich die Kommunikation?
2. Welche Botschaft soll übermittelt werden (Sachstand / Entscheidungsvorlage / Kosten)?
3. Welche Tonalität ist angemessen (neutral / dringend / positiv / kritisch)?
4. Liegt Material vor, das in den Brief eingearbeitet werden soll?
5. Output: Mandantenbrief, Statusbericht, Entscheidungsvorlage, Abschlussbrief?

## Anschluss-Skills
- `spezial-einstweilige-mandantenkommunikation-entscheidungsvorlage` – EV-Entscheidungsvorlage.
- `spezial-schadensersatz-abschlussprodukt-und-uebergabe` – Abschluss-Memo.
- `spezial-bezuege-zahlen-schwellen-und-berechnung` – Kostenabschätzung.

## Quellenregel
- BRAO, BORA, RVG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Keine inhaltlichen Urteile in diesem Skill (nur Kommunikationsstruktur).
- Annahmen und Lücken ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine inhaltliche Rechtsprüfung (das machen die Fachmodule).
- Kein Ersatz für vollständige Mandantenberatung und individuelle Aufklärung.
