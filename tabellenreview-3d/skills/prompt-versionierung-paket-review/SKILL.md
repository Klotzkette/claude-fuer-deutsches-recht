---
name: prompt-versionierung-paket-review
description: "Prompt Versionierung Paket Review: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Prompt Versionierung Paket Review

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Prompt Versionierung Paket Review** im Plugin Tabellenreview 3D. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `prompt-versionierung` | Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output: Prompt-Versionsprotokoll. Abgrenzung: nicht Prompt-Erstellung. |
| `pruefer-uebergabe-paket` | Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für naechsten Prüfer. Abgrenzung: nicht Audit-Trail. |
| `review-durchfuehren` | 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung. Output: Ausgefuellte 3D-Review-Tabelle. Abgrenzung: nicht Wuerfel-Aufbau (Vorbereitung). |

## Arbeitsweg

Im Plugin Tabellenreview 3D gilt für **Prompt Versionierung Paket Review**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `prompt-versionierung`

**Fokus:** Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output: Prompt-Versionsprotokoll. Abgrenzung: nicht Prompt-Erstellung.

# /tabellenreview-3d:prompt-versionierung


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Wenn der Spaltenprompt 'Change-of-Control' heute leicht anders formuliert ist als gestern dann sind die heutigen Zellen mit den gestrigen nicht vergleichbar. Dieser Skill macht den Unterschied explizit.

## Versionierungsschema

Semantische Versions-ID pro Prompt: `<spalte-id>@<major>.<minor>.<patch>`

### Patch (`x.y.Z+1`)

- Wortlautfeinheiten ohne Sinnänderung (Tippfehler / Stilkorrektur / Beispiel ergänzt)
- Vorhandene Zellen NICHT invalidiert
- Empfehlung: bestehende Zellen behalten

### Minor (`x.Y+1.0`)

- Antworttyp geändert (z. B. Freitext zu Ja-Nein)
- Ampelregel geändert (Schwelle verschoben)
- Antwortdimension hinzugefügt (z. B. zusätzlich Schwelle in EUR abfragen)
- Vorhandene Zellen werden auf `nachprüfen` gesetzt
- Empfehlung: betroffene Spalten erneut laufen lassen (Teil-Rerun)

### Major (`X+1.0.0`)

- Pruefdimension geändert (z. B. Spalte 'AGB-Wirksamkeit' splittet zu 'Wirksam' und 'Anwendbares-AGB-Regime')
- Spalte umbenannt oder zusammengelegt
- Vorhandene Zellen werden invalidiert
- Empfehlung: betroffene Zellen komplett neu berechnen

## Aktivierung und Deaktivierung

- Nur eine Version pro Spalte ist gleichzeitig aktiv (`aktive-prompts.yaml`)
- Alte Versionen liegen im `prompt-historie.yaml` mit `gültig-bis`-Datum
- Wer den aktiven Prompt ändert trägt zwingend den Migrationspfad für bestehende Zellen ein

## Pflichtfelder pro Prompt-Version

```yaml
- spalte-id: change-of-control
 version: "2.1.0"
 wortlaut: |
 Enthält der Vertrag eine Klausel die bei Kontrollwechsel ...
 antworttyp: zitat-mit-fundstelle-und-schwelle
 ampel-regel:
 rot: "Klausel vorhanden + harte Kündigungsfolge ohne Heilung"
 gelb: "Zustimmungsvorbehalt mit unklarer Schwelle"
 gruen: "Keine Klausel oder branchenübliche Schwelle"
 geaendert-am: "2026-05-20"
 geaendert-von: "anwalt-x"
 migrationspfad: "Patch-Änderung — bestehende Zellen behalten gültig."
```

## Integration mit Audit-Trail

Jede Prompt-Änderung erzeugt einen `prompt.geändert` Eintrag im `audit-trail-protokoll` mit Versionsnummer und Begründung.

## Grenzen

Versionierung verhindert keine schlechten Prompts — sie macht sie nur sichtbar. Der Prüfer entscheidet ob Migration noetig ist.

## 2. `pruefer-uebergabe-paket`

**Fokus:** Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für naechsten Prüfer. Abgrenzung: nicht Audit-Trail.

# /tabellenreview-3d:prüfer-übergabe-paket


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Das Plugin liefert nicht das fertige Mandatsergebnis. Es liefert das Prüfer-Paket — alles was der zugelassene Rechtsanwalt braucht um in vertretbarer Zeit die Endabnahme machen zu können. Dieser Skill schnuert das Paket.

## Bestandteile

### 1. Hauptdatei

- `<projekt>-wuerfel.xlsx` aus `excel-multi-sheet-export` mit allen Tabellenreitern.

### 2. Erzählfassung

- `<projekt>-bericht.pdf` aus `pdf-bericht-erzeugen` mit Deckblatt Management-Summary und Anhang.

### 3. Belegkette

- `belegkette.csv` aus `belegkette-rueckverfolgung` — Pflichtanhang für Reproduzierbarkeit.

### 4. Audit

- `audit-trail-auszug.md` aus `audit-trail-protokoll` — die letzten N Ereignisse, mindestens aber Lauf-Start Lauf-Ende Prompt-Versionen und Prüfer-Flags.

### 5. Prompt-Versionen

- `prompt-historie.yaml` aus `prompt-versionierung` — welche Versionen aktiv waren beim Lauf.

### 6. Widersprüche

- `widerspruchsbericht.md` aus `kreuzblatt-konsistenzpruefung` — Konflikte zwischen Arbeitsblättern.

### 7. Ampel-Aggregat

- `ampel-aggregat.md` aus `risikoampel-aggregation` — Gesamtbild auf Würfel- Arbeitsblatt- Spalten- und Zeilenebene.

### 8. Prüfer-Flag-Arbeitsliste

- `pruefer-flags.xlsx` — Liste aller Zellen die menschliche Prüfung brauchen. Spalten: Zeile Arbeitsblatt Spalte Grund Antwortvorschlag Entscheidung (leer).

### 9. Begleitschreiben

- `begleitschreiben.md` — eine Seite. Was wurde gemacht. Wie viele Dokumente. Wie viele Hotspots. Wie viele Prüfer-Flags. Erwartete Pruefdauer. Ablauf der Abnahme.

## Zusammenstellung

Alles in einem ZIP: `<projekt>-prüfer-paket-<zeitstempel>.zip`

## Abnahme

Der Prüfer:

1. Liest das Begleitschreiben.
2. Geht die Prüfer-Flag-Arbeitsliste durch — Entscheidung pro Flag.
3. Stichprobenprüfung an gelben und grünen Zellen.
4. Prüfung der roten Zellen und Hotspots vollständig.
5. Unterschrift im Audit-Trail (`prüferabnahme.eingegeben`).

## Erst nach Abnahme

Erst nach dokumentierter Prüfer-Abnahme darf das Paket (oder Auszüge davon) an den Mandanten gehen. Das Plugin sperrt die Mandantenausgabe per Schwellenwert: ohne `prüferabnahme.eingegeben` im Audit-Trail wird der Skill `mandant-versenden` (sofern in der Praxis vorgesehen) verweigert.

## Begründung

- BRAO Paragraph 43a Absatz 2 — Verschwiegenheit
- StGB Paragraph 203 — Privatgeheimnisse
- RDG Paragraph 2 — Rechtsdienstleistung darf nur durch Rechtsanwalt erbracht werden — der Würfel ist Vorbereitung, die Abnahme ist die Rechtsdienstleistung

## 3. `review-durchfuehren`

**Fokus:** 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung. Output: Ausgefuellte 3D-Review-Tabelle. Abgrenzung: nicht Wuerfel-Aufbau (Vorbereitung).

# /tabellenreview-3d:review-durchführen


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Das ist der Hauptlauf. Wenn der Würfel 25 Spalten 200 Zeilen und 5 Arbeitsblätter hat sind das 25.000 Zellen. Jede Zelle braucht: Antwort + wörtliches Zitat + Fundstelle + Ampel + Prüfer-Flag.

## Eingaben

- `wuerfel-schema.yaml`
- `spaltenprompts.yaml`
- `zeilenprompts.yaml`
- `arbeitsblaetter.yaml`
- `zeilen-inventar.yaml`
- Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md`

## Ablauf pro Zelle

1. **Prompt zusammenführen:** Arbeitsblatt-Perspektive vor Spaltenprompt vor Zeilenprompt. Konflikte protokollieren.
2. **Quelldokument öffnen:** Pfad + Hash gegen Inventar abgleichen — falls Hash abweicht: Belegkette unterbrochen Prüfer-Flag setzen.
3. **Antwort extrahieren:** Antworttyp aus Spaltenprompt-Definition beachten (Freitext / zitat-mit-fundstelle / ja-nein / Datum / Geldbetrag / Aufzählung).
4. **Belegkette schreiben:** wörtliches Zitat in Anführungszeichen, danach Fundstelle (Datei-ID + Seite + Absatz + ggf. Ziffer).
5. **Ampel setzen:** anhand `ampel-regel` aus dem Spaltenprompt (rot / gelb / grün).
6. **Prüfer-Flag setzen wenn:**
 - OCR-Konfidenz unter 90 Prozent
 - Antworttyp `zitat-mit-fundstelle` aber kein Zitat extrahierbar
 - Konflikt zwischen Spalten- und Zeilenprompt
 - Mehrdeutigkeit (mehrere plausible Antworten im Dokument)
7. **Querweis aufbauen:** wenn Zellen-Ergebnis auf anderen Vertrag referenziert (`siehe Anlage 7 zu Vertrag X`) als Cross-Ref vermerken.
8. **Cache prüfen:** bei Quasi-Duplikaten (Ähnlichkeit über 95 Prozent) zur Zelle eines bereits geprüften Dokuments Cache-Treffer vorschlagen — Prüfer entscheidet ob übernommen.

## Ausgabeformat

- `wuerfel.parquet` (oder JSON) mit einer Zeile pro Zelle:

```
arbeitsblatt-id, zeile-id, spalte-id, antwort, woertliches-zitat, fundstelle, ampel, prüfer-flag, prompt-version, lauf-zeitstempel
```

- `lauf-zusammenfassung.md` — Anzahl Zellen pro Ampel, Anzahl Prüfer-Flags, Anzahl Cache-Treffer, Laufdauer, Modell-Version, Audit-Trail-Eintrag-ID.

## Reihenfolge

Standard: Arbeitsblatt-außen, Zeile-mittel, Spalte-innen. Optional: Spalte-außen wenn Spaltenprompt aufwaendig (z. B. Volltext-Indexierung) und über den Stapel gemeinsam profitiert.

## Grenzen

Jede Zelle ist ein Hinweis kein Befund. Prüfer-Flags sind die wichtigste Ausgabe — sie sagen wo der menschliche Prüfer hinschauen muss. Untermarkierung ist eine Einbahnstraße; Übermarkierung ist eine Zweiwegtür die ein Anwalt in 30 Sekunden schließt.
