---
name: expansion-aktualisierung
description: >
  Aktualisiert den Status eines laufenden Expansionsprojekts — ermittelt,
  welche Punkte nun freigegeben sind, kennzeichnet überfällige Positionen und
  benennt die nächsten Prioritäten. Lädt, wenn seit der letzten Sitzung
  Fortschritte erzielt wurden und der Tracker den aktuellen Stand widerspiegeln
  soll.
language: de
triggers:
  - "Expansion aktualisieren"
  - "Tracker update"
  - "Status Expansion"
  - "was ist noch offen"
  - "nächste Schritte Auslandseinstellung"
  - "Expansionsprojekt fortschreiben"
  - "was hat sich geändert"
---

# Expansions-Update (Arbeitsrecht)

## Zweck

Diese Skill kehrt zu einem laufenden Expansions-Tracker zurück und aktualisiert
den Bearbeitungsstand anhand der seit der letzten Sitzung eingetretenen
Entwicklungen. Sie berechnet neu, welche Punkte jetzt angegangen werden können,
kennzeichnet überfällige Positionen und benennt die nächsten Prioritäten.

Lädt, wenn Fortschritte bei einer laufenden Auslandseinstellung zu dokumentieren
sind und der Tracker aktualisiert werden soll.

## Eingaben

- Zielland (ggf. aus bestehendem Tracker automatisch erkannt)
- Beschreibung der eingetretenen Änderungen seit der letzten Sitzung
- Neue Punkte oder geänderte Fristen (falls zutreffend)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 7 SGB IV: Beschäftigungsverhältnis und Scheinselbständigkeit — bei
  Verlängerung eines EOR-Verhältnisses weiterhin zu prüfen
- § 1 Abs. 1b AÜG: Gesetzliche Höchstüberlassungsdauer von 18 Monaten —
  bei andauernder EOR-Nutzung kontinuierlich zu überwachen
- § 8 AÜG: Equal-Pay-Gebot nach neun Monaten Überlassung — Ausnahme nur
  durch einschlägigen Tarifvertrag
- Art. 8 Rom I-VO: Fortlaufende Relevanz des Beschäftigungsstatuts bei
  grenzüberschreitenden Arbeitsverhältnissen
- §§ 17, 18 KSchG: Massenentlassungsanzeige bei Erreichung der
  Schwellenwerte im Rahmen des Aufbaus

**Leitentscheidungen:**

- BAG, Urt. v. 02.06.2010 – 7 AZR 946/08, NZA 2010, 1289 Rn. 18 ff.:
  Rechtsfolgen fehlender AÜG-Erlaubnis; Entstehung eines Arbeitsverhältnisses
  zum Entleiher kraft Gesetzes — Relevanz, wenn EOR ohne korrekte AÜG-Struktur
  fortgeführt wird
- BAG, Urt. v. 30.09.2014 – 1 AZR 1083/12, NZA 2015, 121 Rn. 25 ff.:
  Interessenausgleich und Sozialplan bei Betriebsänderungen infolge
  Auslandsexpansion — zu beachten, wenn durch den Aufbau im Ausland
  inländische Strukturen betroffen werden
- BSG, Urt. v. 29.03.2022 – B 12 KR 2/20 R, NZA 2022, 1254:
  Gesamtbetrachtung bei der Statusfeststellung nach § 7a SGB IV

**Kommentarliteratur:**

- Schüren/Hamann, AÜG, 5. Aufl. 2022, § 1 Abs. 1b Rn. 10 ff.:
  Fristberechnung und Unterbrechungsregeln bei der 18-Monats-Grenze
- Erfurter Kommentar/Wank, 24. Aufl. 2024, § 611a BGB Rn. 80 ff.:
  Folgen einer Umklassifizierung als Arbeitnehmer
- Rieble/Junker, Münchener Handbuch zum Arbeitsrecht, Bd. 1, 5. Aufl. 2021,
  § 19 Rn. 22 ff.: Statusänderungen in laufenden grenzüberschreitenden
  Projekten

## Ablauf

**Schritt 1 — Tracker identifizieren**

Lese `CLAUDE.md` im Plugin-Verzeichnis. Identifiziere die Tracker-Datei
`expansion-[slug].yaml`. Falls sie nicht existiert:

> Für [Land] ist kein Expansions-Tracker vorhanden. Starten Sie mit
> `/arbeitsrecht:expansion-auftakt [Land]`.

**Schritt 2 — Aktuellen Stand anzeigen**

Lese den Tracker. Zeige den Gesamtstatus:

```
[Land] Expansion — zuletzt aktualisiert: [Datum]
Offen: [N] | In Bearbeitung: [N] | Erledigt: [N] | Blockiert: [N]

Nächste Prioritäten (offene Punkte nach Fälligkeit / Abhängigkeit):
  [Punkt] — Verantwortung: [Person/Funktion]
  [Punkt] — Verantwortung: [Person/Funktion]
  [Punkt] — Verantwortung: [Person/Funktion]
```

**Schritt 3 — Änderungen abfragen**

Frage alle Änderungen in einem einzigen Block ab:

> Welche Punkte haben sich seit der letzten Sitzung bewegt? Bitte schildern
> Sie kurz die Änderungen (z. B. „EOR-Entscheidung getroffen — Anbieter ist
> Deel", „externe Arbeitsrechtler beauftragt — Erstgespräch nächste Woche",
> „Betriebsstättenanalyse noch offen, Steuerberater wartet auf Mandatserteilung").
> Neue Punkte oder geänderte Fristen können ebenfalls mitgeteilt werden.

**Schritt 4 — Updates anwenden**

Trage alle Änderungen in den Tracker ein. Wenn ein Punkt als erledigt markiert
wird, prüfe, ob er andere Punkte freischaltet, und kennzeichne diese als
jetzt bearbeitbar.

**Schritt 5 — Überfällige Punkte kennzeichnen**

Wenn ein Punkt eine abgelaufene Frist hat und noch den Status `offen` oder
`in Bearbeitung` trägt:

```
Überfällig: [Punkt] — Fälligkeit war [Datum], Verantwortung: [Person/Funktion]
```

**Schritt 6 — AÜG-Fristcheck**

Wenn der Tracker einen aktiven EOR-Einsatz enthält: Prüfe, ob die
18-Monats-Grenze des § 1 Abs. 1b AÜG oder das Equal-Pay-Gebot nach § 8 AÜG
(9 Monate ohne tarifvertragliche Ausnahme) in den nächsten 60 Tagen greift.
Falls ja, flagge explizit.

**Schritt 7 — Tracker speichern und bestätigen**

```
Tracker aktualisiert — [N] Punkte geschlossen, [N] noch offen.
Nächste Priorität: [oberster offener Punkt].
```

## Ausgabeformat

Statusanzeige nach Schritt 2 (Tabellenform), gefolgt von freiem Abfrageblock,
dann Bestätigungsnachricht nach Update. Bei AÜG-Fristwarnung: gesonderter
Warnblock über der Bestätigung.

## Beispiel

```
/arbeitsrecht:expansion-aktualisierung Polen
```

```
/arbeitsrecht:expansion-aktualisierung
(fragt nach dem Land, wenn mehrere Tracker existieren)
```

Beispiel-Ausgabe bei laufendem EOR-Einsatz seit 14 Monaten:

> AÜG-Fristwarnung: Der EOR-Einsatz für [Mitarbeiterin] läuft seit
> 14 Monaten. Die gesetzliche Höchstüberlassungsdauer von 18 Monaten
> (§ 1 Abs. 1b AÜG) wird am [Datum] erreicht. Ohne tarifvertragliche
> Verlängerungsklausel oder Umwandlung in ein direktes Arbeitsverhältnis
> droht Rechtsfolge nach § 10 Abs. 1 AÜG.

## Risiken und typische Fehler

- **18-Monats-Grenze übersehen**: Die AÜG-Frist läuft unabhängig davon,
  ob die Parteien die Überlassung bewusst als solche strukturiert haben.
  Frühzeitige Planung der Folgeoption (Direkteinstellung oder neuer EOR-Vertrag
  mit echtem Unterbrechungszeitraum) ist erforderlich.
- **Equal-Pay vergessen**: Nach neun Monaten ununterbrochener Überlassung
  gilt das Equal-Pay-Gebot (§ 8 AÜG), sofern kein einschlägiger TV gilt.
  Budgetauswirkung für Finance vorab modellieren.
- **Tracker nicht gepflegt**: Ein veralteter Tracker führt zu fehlerhafter
  Priorisierung. Update zeitnah nach jeder relevanten Entwicklung.
- **Statusänderungen nicht auf Abhängigkeiten geprüft**: Wird z. B. die
  EOR-Entscheidung getroffen, schaltet dies typischerweise Punkte für
  Steuer, Finance und HR frei — diese dürfen nicht übersehen werden.

## Quellenpflicht

Bei AÜG-relevanten Warnungen zitieren:
- § 1 Abs. 1b AÜG (Höchstüberlassungsdauer)
- § 8 AÜG (Equal-Pay-Gebot)
- § 10 Abs. 1 AÜG (Fiktion des Arbeitsverhältnisses)
- BAG, Urt. v. 02.06.2010 – 7 AZR 946/08, NZA 2010, 1289

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
