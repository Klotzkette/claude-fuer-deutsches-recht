---
name: akteneinsicht-auswerten
description: Systematische Auswertung der beigezogenen Verwaltungs- oder Gerichtsakte — chronologische Sichtung Identifikation entscheidungserheblicher Aktenstuecke (Antrag Bescheid Widerspruch medizinische Gutachten Sachverstaendigenstellungnahmen Aktenvermerke). Erzeugt Aktenchronik Aktenliste mit Bewertung pro Eintrag (entscheidend / hilfreich / neutral / belastend) Widerspruechen zwischen Aktenteilen und Pruefkatalog fuer Folgeschriftsatz. Anschluss an Skill `widerspruch-formulieren` oder `klage-sozialgericht`.
---

# Akteneinsicht auswerten

## Zweck

Aus einer eingegangenen Akte rasch das Entscheidungserhebliche herausziehen. Was sagt die Akte was die Behörde im Bescheid weggelassen oder anders dargestellt hat?

## Eingabe

- Vollständige Verwaltungsakte (PDF; ggf. gescannt mit OCR).
- Bisheriges Analyseprotokoll aus `bescheidanalyse`.

## Ablauf

### 1. Inventarisierung

Jeder Aktenteil mit:
- laufender Nummer
- Datum
- Verfasser / Quelle
- Typ (Antrag / Bescheid / Gutachten / Vermerk / Stellungnahme / Schreiben Dritter / Beleg)
- Seitenanzahl
- Prüfer-Flag falls schlecht lesbar oder geschwaerzt

### 2. Chronologische Aktenchronik

Tabelle nach Datum sortiert mit Kurzinhalt — eine Zeile pro Aktenteil.

### 3. Inhaltsbewertung pro Aktenteil

Pro Aktenteil eine Klassifizierung:
- **entscheidend** — trägt das Ergebnis (entweder für oder gegen den Mandanten)
- **hilfreich** — stuetzt unsere Argumentation
- **neutral** — Sachverhaltsdokumentation ohne Wertung
- **belastend** — stuetzt die Behördenentscheidung
- **lücke** — verweist auf Vorgang der nicht in der Akte ist

### 4. Widerspruchsprüfung

- **Bescheid vs Aktenstand** — sagt der Bescheid Dinge die in der Akte anders stehen?
- **Verfahrensvermerke** — wurde die Anhörung geführt aktenkundig?
- **Medizinische Gutachten** — sind sie schlüssig nachvollziehbar? Wurden Befunde aus Arztbriefen überhaupt zur Kenntnis genommen?
- **Ermittlungsumfang** — hat die Behörde alles erhoben was sie hätte erheben müssen (§ 20 SGB X)?
- **Datenherkunft** — woher hat die Behörde Drittauskuenfte und durfte sie diese erheben?

### 5. Folge-Prüfkatalog

Für den nächsten Schriftsatz:
- Welche Aktenstücke zitieren wir mit Pinpoint (Seite Absatz)?
- Welche Aktenstücke widerlegen die Bescheidbegründung?
- Wo brauchen wir eine Stellungnahme des Mandanten?
- Wo brauchen wir ein eigenes Privatgutachten zur Untermauerung?
- Welche Beweisanträge könnten wir im Klageverfahren stellen?

## Ausgabe

- `aktenchronik-<mandat>.md` mit Chronik und Bewertung.
- `aktenpruefliste-<mandat>.md` mit Prüfer-Flags zur Klärung mit Mandant.
- Vorlage `schriftsatzbausteine-<mandat>.md` mit zitierfähigen Pinpoint-Verweisen aus der Akte für den Folgeschriftsatz.

## Hinweis zur Vertraulichkeit

Verwaltungs- und Sozialakten enthalten besonders sensible Daten (Gesundheit Sozialleistungen Vermögen). Verarbeitung nur in Tools mit AVV. Mandantenakte unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/mandate/<az>/` ablegen.
