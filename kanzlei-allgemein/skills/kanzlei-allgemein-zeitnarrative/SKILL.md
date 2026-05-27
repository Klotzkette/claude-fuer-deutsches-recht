---
name: kanzlei-allgemein-zeitnarrative
description: "Zeiterfassung mit abrechenbaren Narrativen fuer Kanzlei-Mandate. Anwendungsfall Anwalt hat Taetigkeit ausgeubt und will Zeit mit praezisem Narrativ erfassen fuer spaetere Rechnungsstellung. Normen § 10 RVG Pflichtangaben Narrative GoBD-Zeitstempel. Pruefraster Akte Dauer Takt 6-Minuten-Bloecke Bearbeiter Taetigkeit Honorargrundlage Abrechenbarkeit Datenschutzreduktion. Output Zeiterfassungsprotokoll mit Narrativ Abrechenbarkeit und Rechnungsvorbereitungsnotiz. Abgrenzung zu timesheet-aktenzeitung (Gesamtzeittabelle) und kanzlei-allgemein-rechnung."
---

# Zeitnarrative und Timesheet


## Triage zu Beginn
1. Fuer welche Akte und welchen Bearbeiter soll der Zeiteintrag erfasst werden?
2. Ist die Taetigkeit nach RVG oder nach Stundensatz abrechenbar — oder intern (nicht abrechenbar)?
3. Gibt es eine genaue Zeitangabe oder soll die Dauer aus dem Workflow-Verlauf geschaetzt werden?
4. Soll der Eintrag sofort in die Rechnung oder erst in das interne Timesheet?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 29.07.2021 - IX ZR 5/21, NJW 2021, 3320 — Honorarvereinbarung nach Stundensatz erfordert detaillierte Zeitaufzeichnungen; pauschalierte Taetigkeitsbeschreibung reicht nicht fuer Nachvollziehbarkeit nach § 10 RVG analog.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Anwaltliches Honorar muss spezifiziert werden; Rechnung ohne nachvollziehbare Taetigkeitsangabe ist nicht fällig.
- BGH, Urt. v. 17.01.2019 - IX ZR 52/18, NJW 2019, 1232 — Mandant kann Zeitaufzeichnung verlangen (§ 10 RVG analog); Kanzlei muss Taetigkeitsliste fuehren und auf Anforderung herausgeben.
- BFH, Urt. v. 24.06.2020 - X R 23/18, BStBl. II 2021, 170 — Zeitnachweis als Betriebsausgabenbeleg: Zeitaufzeichnungen muessen GoBD-konform unveraenderbar sein.

## Zentrale Normen
- § 10 RVG — Pflichtangaben auf der Rechnung: Taetigkeitsnachweis als Faelligkeitsvoraussetzung
- § 3a RVG — Honorarvereinbarung: Stundensatz-Abrechnung und Dokumentationspflicht
- § 147 AO — Aufbewahrungspflicht: Zeiterfassungsbelege 10 Jahre
- § 238 HGB — Buchfuehrungspflicht: Zeitnarrative als Teil der betrieblichen Aufzeichnungen

## Kommentarliteratur
- Mueckenberger/Meiling RVG § 10 Rn. 1-25 (Taetigkeitsnachweis und Faelligkeit)
- Gerold/Schmidt RVG § 3a Rn. 1-20 (Stundensatz-Vereinbarung und Dokumentation)

## Zweck

Dieser Skill macht aus Arbeitsschritten abrechenbare oder interne Zeitnarrative. Er fragt nach, welcher Akte die Tätigkeit zugeordnet werden soll, und erzeugt klare Zeiteinträge, die später in Rechnung, E-Rechnung, Prüfprotokoll oder interne Controlling-Auswertung übernommen werden können.

## Standardfrage

> Soll ich für die letzte Stunde einen Zeiteintrag vorbereiten? Ich habe folgende mögliche Tätigkeiten erkannt: ... Welcher Akte soll ich das zuordnen?

## Ablauf

1. Beobachtete oder geschilderte Tätigkeit zusammenfassen.
2. Aktenzuordnung vorschlagen und Unsicherheit markieren.
3. Bearbeiter, Rolle und Verantwortlichen erfassen.
4. Start, Ende, Dauer, Mindesttakt und Rundung erfragen oder vorschlagen.
5. Tätigkeit klassifizieren: Intake, Aktenprüfung, Frist, Recherche, Schriftsatz, Telefonat, Mandantenkontakt, Gegnerkontakt, Gerichtskontakt, beA, Rechnung, intern.
6. Abrechenbarkeit markieren: abrechenbar, nicht abrechenbar, pro bono, intern, Pauschale enthalten, RVG-Nachweis.
7. Honorargrundlage: RVG, Stundenhonorar, Pauschale, Vorschuss, Rechtsschutz, Kulanz.
8. Rechnungsfähigkeit prüfen: mandantenfähig, verständlich, quellenbasiert, ohne unnötige Geheimnisse.
9. Narrative formulieren: knapp, mandatsbezogen, prüfbar.
10. Freigabe abfragen.
11. Übergabe an `kanzlei-allgemein-rechnung` vormerken, wenn abrechnungsreif.

## Narrative-Stil

Gut:

- „Prüfung beA-Eingang und Fristnotierung; Entwurf Rückfrage an Mandant.“
- „Analyse Klageerwiderung und Strukturierung der Gegenargumente.“
- „Telefonat mit Mandant zur Sachverhaltsergänzung und Abstimmung der nächsten Schritte.“
- „Entwurf und Überarbeitung Schriftsatzantwort einschließlich Anlagenabgleich.“

Nicht gut:

- interne Gedankengänge,
- überflüssige Geheimnisse,
- unsichere Spekulationen,
- personenbezogene Details ohne Abrechnungsnutzen.

## Granularität

Für Rechnungen lieber mehrere saubere Einträge als einen Sammelblock erzeugen:

- beA-Eingang prüfen.
- Frist und Vorfrist notieren.
- Anlagen sichten.
- Rechtsfrage prüfen.
- Mandantenrückfrage entwerfen.
- Schriftsatz entwerfen.
- Schriftsatz finalisieren.
- Versand vorbereiten.

Nicht künstlich zersplittern, wenn ein zusammenhängender Arbeitsblock fachlich besser passt. Ziel ist prüfbare, verständliche Abrechnung.

## Datenschutzreduktion

Narrative sollen genug Inhalt für Rechnung und Prüfung enthalten, aber keine unnötigen Mandatsgeheimnisse offenlegen. Namen Dritter, Gesundheitsdaten, Bankdaten, Kinder, Strafvorwürfe und interne Prozessstrategie nur aufnehmen, wenn sie für die Abrechnung wirklich erforderlich sind.

## Rechnungsschnittstelle

Jeder freigegebene abrechenbare Eintrag bekommt:

- Rechnungsstatus: offen, gesperrt, abgerechnet, nicht abrechenbar.
- Rechnungsposition oder RVG-Nachweis.
- Leistungszeitraum.
- Bearbeiter.
- Nettofähige Beschreibung.
- Hinweis, ob die Narrative in eine Anlage zur E-Rechnung übernommen werden darf.

## Ausgabe

`assets/templates/zeit-narrative-ledger.md` verwenden.

## Automationshinweis

Wenn Automationen verfügbar sind, nach Zustimmung stündliche Erinnerung vorschlagen. Keine stille Dauerüberwachung.
