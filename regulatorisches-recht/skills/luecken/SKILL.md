---
name: luecken
description: "Für Aufsichtsrechtlichen Gap-Tracker führen: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Aufsichtsrechtlichen Gap-Tracker führen

## 1. Zweck

Dieser Skill verwaltet bereits fachlich begründete Gap-Befunde. Er ersetzt keine Primärquellenprüfung. Neue fachliche Lücken zuerst mit `luecken-aufzeiger` belegen; danach hier Verantwortlichkeit, Bearbeitungsstand und Abschlussnachweis steuern.

## 2. Datenquelle

1. Tracker: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml`.
2. Optionaler Filter: Status, Risikoklasse, Verantwortlicher, Termin oder Regelwerk.
3. Optionaler Änderungsauftrag mit Gap-ID.

Existiert der Tracker nicht, eine leere, valide Struktur anlegen und auf den fachlichen Erstlauf mit `luecken-aufzeiger` verweisen. Keine Beispieldaten als echte Befunde speichern.

## 3. Mindestfelder

```yaml
gap:
  id: "GAP-2026-001"
  quelle: "MaRisk RS 06/2024 (BA), AT 6 Tz. 2"
  quellstatus: "Aufsichtspraxis"
  befund: "Interne Frist von vier Jahren unterschreitet den fünfjährigen Grundsatz"
  risiko: "ROT"
  terminbasis: "laufende Pflicht; interner Zieltermin 2026-08-31"
  verantwortlich: "Compliance"
  status: "offen"
  nachweis: null
  zuletzt_geaendert: "2026-07-12"
```

Ein interner Zieltermin darf nicht als gesetzliche oder aufsichtsrechtliche Übergangsfrist bezeichnet werden.

## 4. Arbeitsablauf

### 4.1 Lesen und validieren

1. Doppelte Gap-IDs erkennen.
2. Fehlende Primärfundstelle markieren.
3. Überholte Quellenfassungen zur erneuten Fachprüfung zurückgeben.
4. Termine in ausdrückliche externe Frist, laufende Pflicht und internen Zieltermin trennen.
5. Geschlossene Gaps ohne Nachweis wieder auf `Nachweis offen` setzen.

### 4.2 Sortieren

Sortiere zuerst nach überfälligem externem Termin, dann ROT, ORANGE, GELB, GRÜN und GRAU, innerhalb der Klasse nach nächstem belegtem Termin. Fehlende Verantwortliche stehen vor zugewiesenen Einträgen derselben Klasse.

### 4.3 Aktualisieren

Erlaubte Statusfolge:

1. `offen`
2. `in Bearbeitung`
3. `zur Wirksamkeitsprüfung`
4. `geschlossen`
5. `wiedereröffnet`

Eine Lücke erst schließen, wenn geänderte Regel, Umsetzungsbeleg und Wirksamkeitsnachweis oder eine fachlich freigegebene Nichtanwendbarkeitsentscheidung vorliegen.

## 5. Ausgabe

### 5.1 Statuskopf

```text
Gap-Übersicht zum [DATUM]
Offen: [N] | In Bearbeitung: [N] | Wirksamkeitsprüfung: [N]
Überfällig nach externer Frist: [N] | Ohne Verantwortlichen: [N]
Quelle zur Aktualitätsprüfung fällig: [N]
```

### 5.2 Arbeitstabelle

| Gap-ID | Fundstelle | Befund | Risiko | Terminbasis | Verantwortlicher | Status | nächster Nachweis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GAP-2026-001 | MaRisk AT 6 Tz. 2 | vier statt grundsätzlich fünf Jahre | ROT | interner Zieltermin | Compliance | in Bearbeitung | freigegebene Richtlinie |

### 5.3 Eskalationsnotiz

Bei ROT, externer Fristüberschreitung oder fehlendem Verantwortlichen eine kurze Eskalationsnotiz mit Befund, Quelle, Auswirkung, bereits erfolgten Maßnahmen und konkreter Entscheidungsvorlage erstellen.

## 6. Fehlerbremsen

1. Keine Entscheidung, Norm oder Frist aus der Tracker-Kurzbeschreibung ergänzen.
2. MaRisk AT 6 mit grundsätzlich fünf Jahren wiedergeben; längere Spezialfristen getrennt prüfen.
3. Historische MaRisk- oder xAIT-Fassungen nicht als aktuelle Quelle fortschreiben.
4. Ampelfarbe ohne Begründung nicht verändern.
5. Abschlussdatum und Wirksamkeitsnachweis revisionsfest protokollieren.
