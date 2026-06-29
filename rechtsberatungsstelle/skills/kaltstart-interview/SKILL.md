---
name: kaltstart-interview
description: "Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet werden. BeratungsHiG § 1 Erlaubnisnorm, BRAO Aufsicht, Beratungsordnung der Hochsch..."
---

# /kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Triage zu Beginn
1. Handelt es sich um eine Neugründung oder eine grundlegende Neuausrichtung der bestehenden Beratungsstelle?
2. Welche Rechtsgrundlage gilt für die Beratungsstellenarbeit: § 6 Abs. 2 Nr. 2 RDG, § 8 RDG oder Tätigkeit unter zugelassenem Anwalt?
3. Welche Fachbereiche sollen von Anfang an eingerichtet werden (Mietrecht, Sozialrecht, Aufenthaltsrecht)?
4. Ist bereits eine CLAUDE.md vorhanden, die abschnittsweise ueberarbeitet werden soll?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Voraussetzungen für erlaubnisfreie Rechtsberatung in Beratungsstellen: Anleitungserfordernis und Unentgeltlichkeit
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des Anleiters: muss von Beginn an organisatorisch sichergestellt werden
- § 203 Abs. 4 StGB — Einbeziehung Dritter (Studenten): Verschwiegenheitsvereinbarungen als Pflichtbestandteil der Ersteinrichtung
- Art. 30 DSGVO — Verarbeitungsverzeichnis: muss vor Beginn der Datenverarbeitung erstellt werden

## Berufsrechtlicher Rahmen

- § 6 Abs. 2 Nr. 2 RDG: Die Organisation der Anleitungsstruktur muss sicherstellen, dass der Volljurist tatsächlich in der Lage ist, die Studentenn anzuleiten. "Formelle" Aufsicht ohne tatsächliche Prüfung genügt nicht; vgl. Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 52.
- § 43a Abs. 2 BRAO: Verschwiegenheitsorganisation muss bereits bei Einrichtung der Beratungsstelle mitgedacht werden (kein Mandantendaten-Upload in nicht abgesicherte Systeme).
- § 203 Abs. 4 StGB: Einbeziehung Dritter (Studenten, externe IT) erfordert vertragliche Absicherung.

## Ablauf

### Schritt 0: Bestehendes Profil prüfen

Ist eine `CLAUDE.md` vorhanden?
- Ja: "Ihr Profil ist bereits eingerichtet. Möchten Sie (a) das Profil anzeigen, (b) einen Abschnitt überarbeiten, oder (c) komplett neu starten (`--redo`)?"
- Nein: Mit Schritt 1 beginnen.

### Schritt 1: Beratungsstellentyp

> Welche Art von Beratungsstelle richten Sie ein?

Optionen (Mehrfachauswahl möglich):
1. **Universitäre Refugee Law Clinic (RLC)** – Schwerpunkt Asyl/Aufenthaltsrecht; § 6 II Nr. 2 RDG
2. **Studentische Rechtsberatung allgemein** – SGB II, Mietrecht, Verbraucherrecht; § 6 II Nr. 2 RDG
3. **AnwVer / DAV Pro-Bono-Programm** – Zugelassene Anwälte, kein RDG-Problem
4. **Verbraucherzentrale** – § 8 Abs. 1 Nr. 4 RDG (Sondererlaubnis)
5. **Wohlfahrtsverband / Sozialberatung** (AWO, Caritas, Diakonie, DRK, Paritätischer) – § 8 Abs. 1 Nr. 4 RDG
6. **Sonstiges** – Bitte beschreiben.

Erfasse auch: Hochschule / Trägerin, Stadt, seit wann aktiv, Anzahl aktiver Studentenr pro Semester.

### Schritt 2: Rechtsgrundlage bestätigen

Je nach Typ aus Schritt 1:

| Typ | Rechtsgrundlage | Pflichten |
|---|---|---|
| RLC / studentische Beratung | § 6 Abs. 2 Nr. 2 RDG | Unentgeltlichkeit, Anleitung durch Volljurist zwingend |
| Verbraucherzentrale | § 8 Abs. 1 Nr. 4 RDG | Trägergebundene Erlaubnis; keine Einzelfallklage |
| Sozialberatung (Verbände) | § 8 Abs. 1 Nr. 4 RDG | Satzungsgemäßer Auftrag erforderlich |
| Pro-Bono (zugelassene Anwälte) | § 1 BRAO (volle Zulassung) | BRAO/BORA voll anwendbar |

> Bestätigen Sie: "Alle Beratungsleistungen erfolgen unentgeltlich. Die Studentenn stehen unter meiner tatsächlichen Anleitung. Ich nehme meine Aufsichtspflicht wahr." (§ 6 II Nr. 2 RDG)

### Schritt 3: Fachbereiche

> Welche Rechtsgebiete deckt Ihre Beratungsstelle ab?

Optionen (Mehrfachauswahl):
- [ ] Asyl- und Flüchtlingsrecht (AsylG, AufenthG)
- [ ] Aufenthaltsrecht allgemein (AufenthG, FreizügG/EU)
- [ ] SGB II / Bürgergeld
- [ ] SGB XII / Grundsicherung im Alter
- [ ] SGB IX / Eingliederungshilfe (inkl. § 76b SGB IX Geflüchtete)
- [ ] Rentenrecht / SGB VI
- [ ] Mietrecht (privat)
- [ ] Mietrecht (Sozialwohnung / WoBindG)
- [ ] Verbraucherrecht / AGB
- [ ] Arbeitsrecht (Kündigung, KSchG)
- [ ] Familienrecht (Unterhalt, Sorgerecht)
- [ ] Strafrecht (nur eingeschränkt – an Fachanwälte verweisen)
- [ ] Sonstiges: [Freitext]

### Schritt 4: Aufsichtsmodell

> Wie möchten Sie das Aufsichtsmodell einrichten?

**Prüfungsgates (Default, anpassbar):**

| Dokument | Default-Gate |
|---|---|
| Widerspruch (Fristen < 2 Wochen) | Sofortige Anleiterkonsultation |
| Widerspruch (Frist > 2 Wochen) | Anleiter prüft vor Versand |
| Klageschrift | Anleiter prüft und gibt frei (zwingend) |
| Mandantenbrief mit Rechtsrat | Anleiter prüft vor Versand |
| Intake-Protokoll | Anleiter nimmt Kenntnis |
| Memo / Rechtsgutachten | Anleiter prüft inhaltlich |
| Semesterübergabe | Anleiter muss bestätigen |

Anleiter kann Gates verschärfen (z. B. alle Dokumente) oder – für erfahrene Studenten – für bestimmte Routinedokumente lockern.

### Schritt 5: Pädagogikhaltung

> Wie lernen Studenten bei Ihnen am besten?

| Haltung | Beschreibung | Geeignet für |
|---|---|---|
| **Ausführen** | Das System erstellt vollständige Entwürfe; Studenten analysieren und übergeben | Erfahrene Studenten (3.–5. Sem.), Routinedokumente |
| **Anleiten** | Das System gibt Struktur und Schlüsselpunkte; Studenten füllen aus | Mittelstufe (2.–3. Sem.) |
| **Lehren** | Das System stellt nur Fragen; Studenten erarbeiten Lösung | Anfangssemester, neue Fachgebiete |

Default für gesamte Beratungsstelle + ggf. Übersteuern je Fachbereich / Dokumenttyp.

### Schritt 6: Verschwiegenheitsorganisation

> Wie ist die IT-Infrastruktur organisiert?

- Werden Mandantendaten in einem Cloud-System verarbeitet? → Auftragsverarbeitungsvertrag (AVV) nach Art. 28 DSGVO erforderlich.
- Wer hat Zugang zu den Mandantenakten?
- Wie werden Akten nach 5 Jahren gelöscht (§ 50 BRAO Aufbewahrungspflicht)?
- Einweisung der Studentenn in Verschwiegenheitspflichten? → Empfehlung: Schriftliche Verpflichtungserklärung zu § 203 StGB.

### Schritt 7: Örtliche Besonderheiten

> Welche örtlichen Kontexte sind wichtig?

- Zuständige BAMF-Außenstelle?
- Zuständige Ausländerbehörde?
- Jobcenter-Bezirke / Träger (kommunal oder BA)?
- Sozialgerichte / Verwaltungsgerichte mit Zuständigkeit?
- Kooperationspartner (Dolmetscherdienste, andere Beratungsstellen, Pro-Bono-Initiativen)?
- Qualifizierter Mietspiegel vorhanden? (Relevant: Berlin, Hamburg, München, Frankfurt, Köln)

### Schritt 8: CLAUDE.md schreiben

Ausgabe: vollständige, aktualisierte `CLAUDE.md` mit allen erhobenen Konfigurationswerten. Struktur wie im CLAUDE.md-Template vorgegeben.

Anschließend empfehlen:
- `/rechtsberatungsstelle:leitfaden-erstellen` für jeden konfigurierten Fachbereich
- `/rechtsberatungsstelle:einarbeitung` – Testlauf aus Studentenn-Perspektive

## Risiken / typische Fehler

- **Anleitungsstruktur nur auf dem Papier:** § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche, nicht nur formelle Anleitung. Ein Anleiter, der monatlich einmal ins Büro schaut, genügt nicht.
- **Fachbereiche zu weit gefasst:** Eine Beratungsstelle, die alles anbietet, kann nichts gut anbieten. Lieber weniger Bereiche mit klarer Gate-Struktur als viele Bereiche mit Qualitätslücken.
- **IT-Sicherheit nicht mitgedacht:** Cloud-Systeme ohne AVV verletzen DSGVO Art. 28. Besonders kritisch bei Asylsuchenden (Art. 9 DSGVO: besondere Kategorien).
- **Semesterwechsel nicht organisiert:** Ohne klare Übergaberegeln fallen Mandate zwischen den Semestern durch. `/rechtsberatungsstelle:semester-übergabe` muss im Ablaufplan verankert sein.

---

<!-- AUDIT-HINWEIS 27.05.2026: Halluzinierte BGH-Zitate entfernt (NOT_FOUND oder WRONG_TOPIC gemäß dejure.org-Prüfung). Betroffene AZ siehe inline-Kommentare. Frontmatter unveraendert. -->
