---
name: fristen
description: >
  Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende
  Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen.
  Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überfällige
  Einträge bleiben markiert bis zur ausdrücklichen Erledigung. Lädt, wenn ein
  Studierender oder Supervisor Fristen hinzufügen, den Fristenstatus abrufen oder
  eine Fristenübersicht für laufende Mandate benötigt.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Frist eintragen
  - Fristenübersicht
  - Notfrist
  - Wiedereinsetzung
  - Klagefrist
  - VwVfG Frist
  - ZPO Frist
  - Fristenkontrolle
  - was ist diese Woche fällig
---

# Fristenverwaltung

## Zweck

Die gravierendste operative Gefahr einer Rechtsberatungsstelle ist eine versäumte Frist. Studierende betreuen mehrere Mandate gleichzeitig, arbeiten in Teilzeit und wechseln semesterweise. Fristen, die nur im Kopf einzelner Studierender existieren, gehen bei der Semesterübergabe verloren, werden in Prüfungsphasen vergessen oder fallen weg, wenn ein Studierender unerwartet aus der Beratungsstelle ausscheidet.

Diese Skill ist das zentrale Betriebsverzeichnis für Fristen. Der begleitende volljuristische Supervisor trägt die Verantwortung, wenn eine Frist versäumt wird. Die Skill ist auf dieses Haftungsniveau kalibriert: Warnungen greifen früh, überfällige Einträge bleiben in jeder Übersicht sichtbar, und Semesterübergaben (via `/semester-uebergabe`) übertragen das Fristenregister auf die nächste Studierendenkohorte.

## Eingaben

- **Fall-ID + Bezeichnung** — um welches Mandat handelt es sich?
- **Rechtsgebiet** — z. B. Mietrecht, Aufenthaltsrecht, Verbraucherrecht
- **Fristtyp** — Einreichungsfrist / Gerichtstermin / Verjährungsfrist / Widerspruchsfrist / Klagefrist / Wiedereinsetzungsfrist / Sonstige
- **Beschreibung** — eine Zeile: was ist fällig?
- **Fälligkeitsdatum** (ggf. Uhrzeit)
- **Quelle** — Grundlage der Frist (z. B. Zustellungsurkunde v. 20.04.2026, § 74 VwGO, § 276 Abs. 1 ZPO, Mietvertrag § 7)
- **Zuständige/-r Studierende/-r**

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 186–193 BGB** — Berechnung von Fristen und Terminen; § 193 BGB: Fristende am nächsten Werktag, wenn Fälligkeit auf Samstag, Sonntag oder gesetzlichen Feiertag fällt.
- **§§ 217–222 ZPO** — Prozessuale Fristberechnung (Beginn, Ende, Verlängerung, Notfristen).
- **§§ 233–238 ZPO** — Wiedereinsetzung in den vorigen Stand: bei unverschuldeter Fristversäumung binnen zwei Wochen nach Wegfall des Hindernisses zu beantragen (§ 234 ZPO); bei Notfristen und Frist zur Begründung der Revision beachte § 233 S. 2 ZPO.
- **§§ 31, 32 VwVfG / §§ 57–60 VwGO** — Fristberechnung im Verwaltungsverfahren und verwaltungsgerichtlichen Verfahren; Wiedereinsetzung nach § 60 VwGO.
- **§ 74 VwGO** — Klagefrist von einem Monat nach Zustellung des Widerspruchsbescheids.
- **§ 80 Abs. 5 VwGO** — Antrag auf Wiederherstellung der aufschiebenden Wirkung (einstweiliger Rechtsschutz).
- **§ 4 KSchG** — Dreiwochenfrist zur Erhebung der Kündigungsschutzklage (Notfrist); § 5 KSchG Wiedereinsetzung (nachträgliche Zulassung).
- **§§ 195 ff. BGB** — Verjährungsfristen: Regelverjährung 3 Jahre (§ 195 BGB), Beginn mit Schluss des Entstehungsjahres (§ 199 Abs. 1 BGB).
- **§§ 12–17 BeratungshilfeG (BerHG)** — Verfahren bei Beratungshilfe; Beratungshilfeschein vor Mandatsbeginn einholen.
- **§§ 114–127a ZPO** — Prozesskostenhilfe (PKH): Antrag vor oder mit Klageerhebung, keine Unterbrechung laufender Fristen durch PKH-Antrag (§ 204 Abs. 1 Nr. 14 BGB beachten).

### Leitentscheidungen

- BGH, Beschl. v. 15.12.2021 – XII ZB 557/20, NJW 2022, 614 Rn. 10 ff. — Sorgfaltspflichten bei elektronischer Fristennotierung; Kanzleipflicht zur Ausgangskontrolle gilt auch für studentische Beratungsstellen sinngemäß.
- BGH, Beschl. v. 08.02.2022 – XI ZB 43/20, NJW-RR 2022, 647 Rn. 8 — Wiedereinsetzungsantrag: Glaubhaftmachung nach § 236 Abs. 2 ZPO erfordert vollständige und in sich schlüssige Darlegung des Fristversäumnisses.
- BVerwG, Beschl. v. 12.06.2019 – 2 B 53/18, NVwZ-RR 2019, 879 Rn. 5 — Fristwahrung im verwaltungsgerichtlichen Verfahren; Zugangsfiktion bei Bekanntgabe nach § 41 Abs. 2 VwVfG.
- BAG, Urt. v. 26.06.2014 – 2 AZR 594/13, NZA 2014, 1303 Rn. 14 — Drei-Wochen-Frist des § 4 KSchG als Ausschlussfrist; keine Hemmung durch laufende Verhandlungen.

### Kommentarliteratur

- Jaspersen, in: BeckOK ZPO, 53. Ed. (Stand 01.03.2025), § 233 Rn. 15 — Voraussetzungen der Wiedereinsetzung; unverschuldetes Hindernis.
- Stackmann, in: MüKoZPO, 6. Aufl. 2020, § 217 Rn. 5 — Fristberechnung, Beginn der Notfrist.
- Kopp/Schenke, VwGO, 29. Aufl. 2023, § 60 Rn. 1 — Wiedereinsetzung im Verwaltungsprozessrecht (Doppelautoren-Kommentar).
- Ellenberger, in: Grüneberg, BGB, 84. Aufl. 2025, § 186 Rn. 1 — Fristberechnung nach §§ 186–193 BGB.

## Ablauf

### Modus `--eintragen` — neue Frist erfassen

1. Fall-ID + Bezeichnung abfragen.
2. Fristtyp und Beschreibung erfassen.
3. Fälligkeitsdatum aufnehmen; Quelle dokumentieren.
4. Zuständige/-n Studierende/-n zuweisen.
5. System generiert automatisch eine ID: `[fall-id]-[kurzbezeichnung]-[JJJJ-MM]`.
6. Duplikatsprüfung: existiert bereits ein Eintrag mit gleicher Fall-ID, gleichem Typ und gleichem Datum? Falls ja, Hinweis vor dem Speichern.
7. **Plausibilitätsprüfung (Pflicht):** Nach Eingabe des Datums wird das Ergebnis gegen typische Fristbänder für den gewählten Typ geprüft (z. B. Klagefrist VwGO: ca. 1 Monat nach Zustellung; Dreiwochenfrist KSchG: 21 Tage ab Zugang Kündigung; Widerspruchsfrist VwGO: 1 Monat). Liegt das eingetragene Datum außerhalb des typischen Bandes, erfolgt folgende Warnung:
   > „Das eingetragene Datum liegt außerhalb des typischen Bereichs für [Fristtyp] im deutschen Recht ([Rechtsgebiet]). Typische Dauer: ca. [Bandbreite] nach [auslösendem Ereignis]. Ihr Eintrag: [Datum], das sind [N] Tage nach [Ereignis]. Prüfen Sie Ihre Berechnung gegen [zitierte Norm aus dem Fristenband] sowie die maßgebliche Fristberechnungsregel (§ 187 f. BGB / § 222 ZPO / § 57 VwGO). Falls Ihre Berechnung korrekt ist (Sonderregelung, Hemmung, Unterbrechung, Wiedereinsetzung), bestätigen Sie; ich trage die Frist unverändert ein."
8. Gibt der/die Studierende `[PRÜFEN]` im Datumsfeld ein, wird der Eintrag mit `faellig: [PRÜFEN]` gespeichert; die Plausibilitätsprüfung läuft erst, wenn ein konkretes Datum eingetragen wird.
9. **Die Skill berechnet keine Fristen.** Die Berechnung obliegt dem/der Studierenden und dem Supervisor; die Skill trägt das Ergebnis ein.

### Modus `--bericht` (Standard) — gesamtübergreifende Übersicht

Liest `deadlines.yaml` und erzeugt folgende Tabelle:

```markdown
# Fristenübersicht — [heute]

**Aktive Fristen:** [N]
**Überfällig:** [N] ⚠
**Fällig diese Woche (nächste 7 Tage):** [N]

---

## Überfällig (sofortige Bearbeitung erforderlich)

| ID | Fall | Typ | Fällig | Zuständig | Tage überfällig |
|---|---|---|---|---|---|

## Fällig heute / in den nächsten 3 Tagen

| ID | Fall | Typ | Fällig | Zuständig |
|---|---|---|---|---|

## Fällig in 4–7 Tagen

| ID | Fall | Typ | Fällig | Zuständig |
|---|---|---|---|---|

## Fällig in 8–14 Tagen

[Liste]

## Über 14 Tage (Anzahl — Details mit `--bericht --horizont=30`)

---

## Nach Zuständigen (Arbeitsbelastung)

| Studierende/-r | Überfällig | Nächste 7 Tage | Nächste 14 Tage | Gesamt aktiv |
|---|---|---|---|---|

## Nach Rechtsgebiet

[gleiche Tabelle, nach Rechtsgebiet gruppiert]

## Nicht zugewiesene Fristen

[Liste — Warnung, wenn aktive Fristen ohne Zuständige vorhanden sind]
```

### Modus `--aktualisieren [id]` — bestehende Frist ändern

Typische Aktualisierungen: Fristdatum geändert (Terminverlegung durch Gericht), Zuständige/-r gewechselt (Neuzuweisung), Notiz hinzugefügt. Jede Änderung wird mit Datum protokolliert; der Verlauf bleibt im Eintrag sichtbar.

### Modus `--erledigt [id]` — als abgeschlossen markieren

- Setzt `status: erledigt`, `erledigungsdatum: [heute]`.
- Bestätigt mit dem/der Studierenden, dass die Handlung tatsächlich vorgenommen und (soweit erforderlich) eingereicht wurde.
- Verschwindet aus aktiven Berichten, bleibt aber in der YAML-Datei erhalten.

### Modus `--schliessen [id]` — ohne Erledigung schließen

Für Fristen, die nicht mehr relevant sind (Fall einvernehmlich beendet, Antrag zurückgenommen, Mandant hat Beratungsstelle abgewählt). Erfordert zwingend einen Eintrag in `notizen:` mit Begründung.

## Ausgabeformat

Strukturierte Markdown-Tabellen gemäß dem Bericht-Modus oben. Jeder Eintrag enthält ID, Fall, Typ, Fälligkeitsdatum, Zuständige/-n und Quellnorm. Überfällige Einträge werden visuell hervorgehoben und bleiben in jedem Bericht sichtbar, bis sie ausdrücklich erledigt oder geschlossen werden.

## Beispiel

**Szenario:** Studierende Maria hat eine Kündigung des Mietverhältnisses erhalten. Kündigung wurde am 08.04.2026 zugestellt. Widerspruchsfrist (§ 574 BGB i. V. m. § 542 BGB) läuft am 08.05.2026 ab.

```
/fristen --eintragen
Fall: Mueller-Mietrecht-2026
Typ: Klagefrist
Beschreibung: Widerspruch gegen Kündigung, § 574 BGB
Fällig: 08.05.2026
Quelle: Zustellung der Kündigung 08.04.2026, § 574 BGB
Zuständig: stud. Berater Schmidt
```

Ausgabe: Eintrag `mueller-mietrecht-widerspruch-2026-05` wird gespeichert. Plausibilitätsprüfung: 30 Tage nach Zustellung — im typischen Band für Widerspruchsfristen im Mietrecht. Eintrag übernommen.

## Risiken und typische Fehler

- **Frist falsch berechnet:** Die Skill trägt ein, was der/die Studierende eingibt; sie berechnet nicht selbst. Besonders kritisch bei: § 222 ZPO (Wochenfrist), § 193 BGB (Sonn-/Feiertagsverschiebung), § 57 VwGO, Sonderfälle bei Zustellungsfiktion nach § 41 Abs. 2 VwVfG.
- **Notfrist verwechselt mit verlängerbarer Frist:** ZPO-Notfristen (z. B. Notfrist Berufung, § 548 ZPO; Revisionsfrist, § 548 ZPO) sind nicht verlängerbar. Fristverlängerungsanträge bei Notfristen sind unwirksam. Immer beim Supervisor klären.
- **PKH-Antrag hemmt Frist nicht automatisch:** Die Einreichung eines PKH-Antrags unterbricht keine Klagefrist. Ausnahme: § 204 Abs. 1 Nr. 14 BGB (Verjährungshemmung durch PKH-Antrag bei Verjährungsfristen); nicht bei prozessualen Ausschlussfristen.
- **Keine Zuweisung:** Aktive Fristen ohne Zuständige/-n werden im Bericht besonders hervorgehoben. Unzugewiesene Fristen sind Hochrisikopositionen.
- **Frist nur im Kopf des Studierenden:** Wird nicht in der YAML-Datei eingetragen und nicht an die nächste Kohorte übergeben.

## Quellenpflicht

Jede eingetragene Frist muss eine **Quellnorm** enthalten (Gesetz, Gerichtsurteil, Vertrag, behördlicher Bescheid). Fristen ohne Quellangabe erhalten den Warnstatus `warnung: keine-quelle`. Die Quellnorm ist die Grundlage, gegen die der Supervisor die Berechnung prüft.

Jeder Fristeneintrag, der außerhalb des Plausibilitätsbands liegt und dennoch bestätigt wurde, erhält automatisch den Hinweis: `warnung: ausserhalb-plausibilitaetsband — vom Supervisor zu prüfen`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall. Alle Fristenberechnungen sind vom begleitenden Supervisor zu prüfen und freizugeben.
