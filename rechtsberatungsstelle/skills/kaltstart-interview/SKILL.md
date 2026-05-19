---
name: kaltstart-interview
description: >
  Einmalige Ersteinrichtung der Beratungsstelle. Führt den anleitenden Volljuristen
  durch ein strukturiertes Interview zur Konfiguration des Plugins: Beratungsstellentyp,
  Rechtsgrundlage, Fachbereiche, Aufsichtsmodell, Verschwiegenheitshinweise,
  Pädagogikhaltung. Ergebnis wird in CLAUDE.md gespeichert. Aufrufen bei Neugründung
  oder grundlegender Neuausrichtung der Beratungsstelle.
argument-hint: "[--redo zum vollständigen Neustart]"
language: de
when_to_use: |
  Trigger phrases and example requests:
  - beratungsstelle einrichten
  - ersteinrichtung
  - cold-start
  - konfiguration
  - new clinic
---

# /kaltstart-interview

1. Prüfe: Ist bereits eine `CLAUDE.md` vorhanden? Falls ja: Anbieten, abschnittsweise zu überarbeiten (`--redo`) oder Übersicht des bestehenden Profils zu zeigen.
2. Führe das Interview durch – Schritt für Schritt, nicht alles auf einmal.
3. Schreibe `CLAUDE.md` mit allen erhobenen Daten.
4. Empfehle als nächsten Schritt: `/rechtsberatungsstelle:leitfaden-erstellen` für jeden Fachbereich.

---

# Ersteinrichtung der Beratungsstelle

## Zweck

Bevor Studierende `/einarbeitung` starten und Mandate aufnehmen, muss der anleitende Volljurist die Beratungsstelle konfigurieren. Diese Konfiguration steuert:

- Welche Rechtsgrundlage die Beratung hat (§ 6 II Nr. 2 RDG? § 8 RDG? Zugelassener Anwalt?)
- Welche Fachbereiche behandelt werden
- Welches Aufsichtsmodell gilt (Prüfungsgates, Freigabestufen)
- Welche Pädagogikhaltung der Anleiter bevorzugt (ausführen / anleiten / lehren)
- Welche örtlichen Besonderheiten (Gerichte, BAMF-Außenstellen, Jobcenter-Bezirke) relevant sind

**Zielgruppe: ausschließlich der anleitende Volljurist.** Studierende starten mit `/rechtsberatungsstelle:einarbeitung`.

## Berufsrechtlicher Rahmen

- § 6 Abs. 2 Nr. 2 RDG: Die Organisation der Anleitungsstruktur muss sicherstellen, dass der Volljurist tatsächlich in der Lage ist, die Studierenden anzuleiten. „Formelle" Aufsicht ohne tatsächliche Prüfung genügt nicht; vgl. Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 52.
- § 43a Abs. 2 BRAO: Verschwiegenheitsorganisation muss bereits bei Einrichtung der Beratungsstelle mitgedacht werden (kein Mandantendaten-Upload in nicht abgesicherte Systeme).
- § 203 Abs. 4 StGB: Einbeziehung Dritter (Studierende, externe IT) erfordert vertragliche Absicherung.

## Ablauf

### Schritt 0: Bestehendes Profil prüfen

Ist eine `CLAUDE.md` vorhanden?
- Ja: „Ihr Profil ist bereits eingerichtet. Möchten Sie (a) das Profil anzeigen, (b) einen Abschnitt überarbeiten, oder (c) komplett neu starten (`--redo`)?"
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

Erfasse auch: Hochschule / Trägerin, Stadt, seit wann aktiv, Anzahl aktiver Studierender pro Semester.

### Schritt 2: Rechtsgrundlage bestätigen

Je nach Typ aus Schritt 1:

| Typ | Rechtsgrundlage | Pflichten |
|---|---|---|
| RLC / studentische Beratung | § 6 Abs. 2 Nr. 2 RDG | Unentgeltlichkeit, Anleitung durch Volljurist zwingend |
| Verbraucherzentrale | § 8 Abs. 1 Nr. 4 RDG | Trägergebundene Erlaubnis; keine Einzelfallklage |
| Sozialberatung (Verbände) | § 8 Abs. 1 Nr. 4 RDG | Satzungsgemäßer Auftrag erforderlich |
| Pro-Bono (zugelassene Anwälte) | § 1 BRAO (volle Zulassung) | BRAO/BORA voll anwendbar |

> Bestätigen Sie: „Alle Beratungsleistungen erfolgen unentgeltlich. Die Studierenden stehen unter meiner tatsächlichen Anleitung. Ich nehme meine Aufsichtspflicht wahr." (§ 6 II Nr. 2 RDG)

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

Anleiter kann Gates verschärfen (z. B. alle Dokumente) oder – für erfahrene Studierende – für bestimmte Routinedokumente lockern.

### Schritt 5: Pädagogikhaltung

> Wie lernen Studierende bei Ihnen am besten?

| Haltung | Beschreibung | Geeignet für |
|---|---|---|
| **Ausführen** | Claude erstellt vollständige Entwürfe; Studierende analysieren und übergeben | Erfahrene Studierende (3.–5. Sem.), Routinedokumente |
| **Anleiten** | Claude gibt Struktur und Schlüsselpunkte; Studierende füllen aus | Mittelstufe (2.–3. Sem.) |
| **Lehren** | Claude stellt nur Fragen; Studierende erarbeiten Lösung | Anfangssemester, neue Fachgebiete |

Default für gesamte Beratungsstelle + ggf. Übersteuern je Fachbereich / Dokumenttyp.

### Schritt 6: Verschwiegenheitsorganisation

> Wie ist die IT-Infrastruktur organisiert?

- Werden Mandantendaten in einem Cloud-System verarbeitet? → Auftragsverarbeitungsvertrag (AVV) nach Art. 28 DSGVO erforderlich.
- Wer hat Zugang zu den Mandantenakten?
- Wie werden Akten nach 5 Jahren gelöscht (§ 50 BRAO Aufbewahrungspflicht)?
- Einweisung der Studierenden in Verschwiegenheitspflichten? → Empfehlung: Schriftliche Verpflichtungserklärung zu § 203 StGB.

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
- `/rechtsberatungsstelle:einarbeitung` – Testlauf aus Studierenden-Perspektive

## Ausgabeformat

Konfigurationsdatei (`CLAUDE.md`). Kein `[KI-GESTÜTZTER ENTWURF]`-Vermerk (Anleiter-Dokument). Länge: 80–180 Zeilen.

## Risiken / typische Fehler

- **Anleitungsstruktur nur auf dem Papier:** § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche, nicht nur formelle Anleitung. Ein Anleiter, der monatlich einmal ins Büro schaut, genügt nicht.
- **Fachbereiche zu weit gefasst:** Eine Beratungsstelle, die alles anbietet, kann nichts gut anbieten. Lieber weniger Bereiche mit klarer Gate-Struktur als viele Bereiche mit Qualitätslücken.
- **IT-Sicherheit nicht mitgedacht:** Cloud-Systeme ohne AVV verletzen DSGVO Art. 28. Besonders kritisch bei Asylsuchenden (Art. 9 DSGVO: besondere Kategorien).
- **Semesterwechsel nicht organisiert:** Ohne klare Übergaberegeln fallen Mandate zwischen den Semestern durch. `/rechtsberatungsstelle:semester-uebergabe` muss im Ablaufplan verankert sein.
