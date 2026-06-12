---
name: padlet-vier-stufen-tafel
description: Padlet-Tafel im Shelf-Format mit den vier Spalten Legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit echt anlegen statt nur zu beschreiben. Drei Pfade Padlet Public API v1, eingeloggter Browser, manueller Aufbau mit fertigem Karten-Markdown. Mit Ampelfarben, Karten-Templates und Verz...
---

# Echte Padlet-Tafel anlegen, nicht nur vorschlagen

> **Arbeite auf ein echtes Padlet hin, nicht nur auf eine Beschreibung.** Wenn keiner der unten genannten Wege funktioniert, wird das ehrlich benannt und es wird **konkret** gefragt, welcher Weg gewaehlt werden soll. Es wird **nie** ein selbst gerendertes Shelf-Board als Ersatz für ein echtes Padlet ausgegeben.

## Pfad 1: Padlet Public API v1 (bevorzugt)

Padlet betreibt eine offizielle REST-API. Voraussetzung ist ein bezahltes Padlet-Abo und ein API-Key aus dem Dashboard (Settings → Personal Account → Developer → Generate).

**Schritte:**

1. **API-Key beschaffen.** Prüfen, ob unter den eigenen Custom-Credentials bereits ein Eintrag `padlet.com` vorhanden ist. Wenn ja, wird er über `api_credentials=["custom-cred:padlet.com"]` automatisch als Bearer-Token gesetzt. Wenn nein: einmalig in der Computer-Oberflaeche unter Einstellungen → Custom Credentials → Add ablegen.
2. **Board anlegen.** Aktuell legt die Public API v1 noch keine ganzen Boards an, sondern nur Posts auf bestehenden Boards. Das leere Shelf-Board mit den vier Spalten muss daher vorab existieren. Wenn noch keines da ist: in der eigenen Padlet-Oberflaeche neues Padlet → Format "Shelf" → vier Spalten benennen ("Legitimer Zweck", "Geeignetheit", "Erforderlichkeit", "Angemessenheit") → Board-ID aus der URL kopieren.
3. **Posts erstellen** über den Endpoint `POST /api/1/boards/{boardId}/posts`. Pro Karte ein Aufruf. Felder: `subject`, `body`, `section` (= Spaltenname oder Spalten-ID), Farbe per `color`-Attribut oder Tag.
4. **Sektion zuordnen.** Die Spalten heissen in der API "Sections". Die Section-IDs erhaelt man über `GET /api/1/boards/{boardId}` aus dem `sections`-Array.
5. **Antwort prüfen.** Bei HTTP 201 die zurueckgegebene Post-ID festhalten, damit Änderungen oder Loeschungen möglich sind.

**Beispiel als Pseudo-Curl** (api_credentials uebernehmen das Authorization-Header-Setting):

```
POST https://api.padlet.com/api/1/boards/{boardId}/posts
Content-Type: application/json

{
  "subject": "Stufe 1 / A1",
  "body": "Vorgetragener Zweck: oeffentliche Sicherheit und Marktentzerrung",
  "sectionId": "<section-id-aus-board-get>",
  "color": "green"
}
```

## Pfad 2: Eingeloggter Browser (Fallback ohne API-Key)

Wenn kein API-Key verfuegbar ist oder kein Padlet-Abo besteht, das Padlet über die eingeloggte Browser-Session anlegen.

**Schritte:**

1. `browser_task` mit `use_local_browser.local=true` und `url=https://padlet.com` starten.
2. Im Padlet-Dashboard "Make a Padlet" -> Format "Shelf" -> Titel "Verhältnismäßigkeit Stufenpruefung" setzen.
3. Vier Spalten benennen: "1 · Legitimer Zweck", "2 · Geeignetheit", "3 · Erforderlichkeit", "4 · Angemessenheit".
4. Karten je Stufe per Plus-Button anlegen, Farbe über das Karten-Menue setzen.
5. Sichtbarkeit auf "secret link" oder "private" stellen.
6. Geteilten Link aus dem Share-Panel ausgeben.

Der Browser-Pfad ist langsamer, aber sichtbar und nachvollziehbar. Falls eine Bestaetigungsaktion wie das Veroeffentlichen ansteht, muss diese im Browser-Task vorab im Approval-Prompt mitgenannt werden.

## Pfad 3: Manueller Aufbau mit fertigem Karten-Markdown

Wenn weder API-Key noch eingeloggter Browser verfuegbar sind, wird **kein** Shelf-Board selbst gerendert. Stattdessen wird der User aktiv durch das Anlegen gefuehrt:

1. **Konkrete Anleitung** zum Anlegen des leeren Shelf-Boards in eigener Padlet-Oberflaeche.
2. **Karten-Inhalte als Markdown-Block** ausgegeben, sortiert nach Spalte, mit Ampelfarben und Quellenverweisen. Format pro Karte:

```
Spalte: 1 · Legitimer Zweck
Farbe: gruen
Titel: A1
Inhalt: oeffentliche Sicherheit und Marktentzerrung; Schranke einfach
Quellen: Apotheken-Urteil BVerfGE 7, 377
```

3. **Hinweis** an den User: ein Padlet-CSV-Import für Posts existiert nicht; die offizielle Backpack-Funktion importiert nur ganze Padlets von einer Padlet-Instanz in eine andere.

## Spaltenstruktur und Karten-Vorlage

### Spalte 1 · Legitimer Zweck
- Karte 1: Vorgetragener Zweck.
- Karte 2: Schrankentyp (einfach, qualifiziert, verfassungsimmanent).
- Karte 3: Tragfaehigkeit aus Gesetzesmaterialien.
- Karte 4: Verbotene Zweckanteile (Mehrheitsmoral, Bevormundung, Diskriminierung).

### Spalte 2 · Geeignetheit
- Karte 1: Wirkmechanismus Mittel auf Zweck.
- Karte 2: Empirische Evidenz oder Prognose.
- Karte 3: Kontrolldichte (Evidenz, Vertretbarkeit, intensive Kontrolle).

### Spalte 3 · Erforderlichkeit
- Karte 1: Alternative 1 (Effektivitaet, Eingriffsschwere).
- Karte 2: Alternative 2 (Effektivitaet, Eingriffsschwere).
- Karte 3: Alternative 3 (Effektivitaet, Eingriffsschwere).
- Karte 4: Begruendung, warum gewaehltes Mittel mildestes ist.

### Spalte 4 · Angemessenheit
- Karte 1: Eingriffsseite (Rang, Intensitaet, Dauer, Reversibilitaet).
- Karte 2: Zweckseite (Rang, Wahrscheinlichkeit, Schadensgroesse).
- Karte 3: Verfahrenssicherungen und Ausgleichsmechanismen.
- Karte 4: Absolute Grenzen (Menschenwuerde, Wesensgehalt, Existenzminimum).
- Karte 5: Gesamtwertung.

## Ampelfarben

- **Gruen**: Stufe unproblematisch.
- **Gelb**: Stufe braucht Wertung.
- **Rot**: Stufe scheitert oder ist hochstreitig.

## ASCII-Vorschau als Begleitung (nicht als Ersatz)

Die ASCII-Vorschau wird **zusaetzlich** zum echten Padlet ausgegeben, damit der Zustand offline lesbar bleibt:

```
+ Spalte 1 (Zweck)  + Spalte 2 (Geeignet) + Spalte 3 (Erforderlich) + Spalte 4 (Angemessen) +
| A1 gruen          | A1 gruen            | A1 rot                  | A1 rot                |
| A2 gelb           | A2 gelb             | A2 gelb                 | A2 gelb               |
| A3 gruen          | A3 gruen            | A3 gruen                | A3 gruen              |
+-------------------+---------------------+-------------------------+-----------------------+
```

## Verwandt

- `stufenbaum-ascii-art` für die druckbare Stufen-Visualisierung.
- `mermaid-flowchart-pruefung` für das Flussdiagramm.
- `ascii-pruefungsschema` für die kompakte Tabellenvariante.
