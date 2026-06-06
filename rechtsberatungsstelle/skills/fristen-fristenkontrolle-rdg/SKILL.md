---
name: fristen-fristenkontrolle-rdg
description: "Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überfällige Einträge bleiben markiert bis zur ausdrücklichen Erledigung. Lädt, wenn ein Studierender oder Supervisor Fristen hinzufügen, den Fristenstatus abrufen oder eine Fristenübersicht für laufende Mandate benötigt im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Fristenverwaltung

## Arbeitsbereich

Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überfällige Einträge bleiben markiert bis zur ausdrücklichen Erledigung. Lädt, wenn ein Studierender oder Supervisor Fristen hinzufügen, den Fristenstatus abrufen oder eine Fristenübersicht für laufende Mandate benötigt. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Die gravierendste operative Gefahr einer Rechtsberatungsstelle ist eine versäumte Frist. Studierende betreuen mehrere Mandate gleichzeitig, arbeiten in Teilzeit und wechseln semesterweise. Fristen, die nur im Kopf einzelner Studierender existieren, gehen bei der Semesterübergabe verloren, werden in Prüfungsphasen vergessen oder fallen weg, wenn ein Studierender unerwartet aus der Beratungsstelle ausscheidet.

Diese Skill ist das zentrale Betriebsverzeichnis für Fristen. Der begleitende volljuristische Supervisor trägt die Verantwortung, wenn eine Frist versäumt wird. Die Skill ist auf dieses Haftungsniveau kalibriert: Warnungen greifen früh, überfällige Einträge bleiben in jeder Übersicht sichtbar, und Semesterübergaben (via `/semester-übergabe`) übertragen das Fristenregister auf die nächste Studierendenkohorte.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Modus `--eintragen` — neue Frist erfassen

1. Fall-ID + Bezeichnung abfragen.
2. Fristtyp und Beschreibung erfassen.
3. Fälligkeitsdatum aufnehmen; Quelle dokumentieren.
4. Zuständige/-n Studierende/-n zuweisen.
5. System generiert automatisch eine ID: `[fall-id]-[kurzbezeichnung]-[JJJJ-MM]`.
6. Duplikatsprüfung: existiert bereits ein Eintrag mit gleicher Fall-ID, gleichem Typ und gleichem Datum? Falls ja, Hinweis vor dem Speichern.
7. **Plausibilitätsprüfung (Pflicht):** Nach Eingabe des Datums wird das Ergebnis gegen typische Fristbänder für den gewählten Typ geprüft (z. B. Klagefrist VwGO: ca. 1 Monat nach Zustellung; Dreiwochenfrist KSchG: 21 Tage ab Zugang Kündigung; Widerspruchsfrist VwGO: 1 Monat). Liegt das eingetragene Datum außerhalb des typischen Bandes, erfolgt folgende Warnung:
 > "Das eingetragene Datum liegt außerhalb des typischen Bereichs für [Fristtyp] im deutschen Recht ([Rechtsgebiet]). Typische Dauer: ca. [Bandbreite] nach [auslösendem Ereignis]. Ihr Eintrag: [Datum], das sind [N] Tage nach [Ereignis]. Prüfen Sie Ihre Berechnung gegen [zitierte Norm aus dem Fristenband] sowie die maßgebliche Fristberechnungsregel (§ 187 f. BGB / § 222 ZPO / § 57 VwGO). Falls Ihre Berechnung korrekt ist (Sonderregelung, Hemmung, Unterbrechung, Wiedereinsetzung), bestätigen Sie; ich trage die Frist unverändert ein."
8. Gibt der/die Studierende `[PRÜFEN]` im Datumsfeld ein, wird der Eintrag mit `fällig: [PRÜFEN]` gespeichert; die Plausibilitätsprüfung läuft erst, wenn ein konkretes Datum eingetragen wird.
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

Jeder Fristeneintrag, der außerhalb des Plausibilitätsbands liegt und dennoch bestätigt wurde, erhält automatisch den Hinweis: `warnung: außerhalb-plausibilitätsband — vom Supervisor zu prüfen`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall. Alle Fristenberechnungen sind vom begleitenden Supervisor zu prüfen und freizugeben.
