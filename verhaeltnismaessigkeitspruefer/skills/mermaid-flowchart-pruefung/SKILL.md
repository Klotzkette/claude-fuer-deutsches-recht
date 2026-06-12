---
name: mermaid-flowchart-pruefung
description: Mermaid-Flowchart fuer die Verhältnismäßigkeitspruefung mit Stufen Entscheidungsknoten und Pfaden bei Scheitern auf Stufe 1 bis 4. Mit Codebeispielen Anwendungshinweisen und Tipps zur Einbettung in Markdown.
---

# Mermaid Flowchart Prüfung

## Grundgeruest

```mermaid
flowchart TD
    A[Eingriff in Grundrecht] --> B{Stufe 1 Legitimer Zweck}
    B -->|verboten| Z1[Verstoss]
    B -->|legitim| C{Stufe 2 Geeignetheit}
    C -->|ungeeignet| Z2[Verstoss]
    C -->|geeignet| D{Stufe 3 Erforderlichkeit}
    D -->|milderes Mittel| Z3[Verstoss]
    D -->|erforderlich| E{Stufe 4 Angemessenheit}
    E -->|unangemessen| Z4[Verstoss]
    E -->|angemessen| OK[Verhaeltnismaessig]
```

## Variante mit absoluten Grenzen

```mermaid
flowchart TD
    A[Eingriff] --> B[Absolute Grenze pruefen]
    B -->|Wuerde Wesensgehalt| ABS[Ohne Abwaegung verfassungswidrig]
    B -->|kein Verstoss| C{Stufe 1 Zweck}
    C -->|legitim| D{Stufe 2 Geeignet}
    D -->|geeignet| E{Stufe 3 Erforderlich}
    E -->|erforderlich| F{Stufe 4 Angemessen}
    F -->|angemessen| OK[Zulaessig]
```

## Variante Schutzpflicht (Untermassverbot)

```mermaid
flowchart TD
    A[Schutzpflicht aus Grundrecht] --> B{Schutzkonzept evident unzureichend?}
    B -->|Ja| Z[Untermassverbot verletzt]
    B -->|Nein| C{Konzept effektiv geprueft?}
    C -->|effektiv| OK[Schutzpflicht erfuellt]
    C -->|ineffektiv| Z2[Nachbesserungspflicht]
```

## Anwendungstipps

- In Markdown-Datei zwischen drei Backticks mit mermaid einbetten.
- GitHub rendert Mermaid automatisch in Wiki und in normalen Repos.
- Bei Klausur als Skizze auf Papier reproduzierbar.
- Knoten mit Fallnummern beschriften für den jeweils zu prüfenden
  Sachverhalt.
