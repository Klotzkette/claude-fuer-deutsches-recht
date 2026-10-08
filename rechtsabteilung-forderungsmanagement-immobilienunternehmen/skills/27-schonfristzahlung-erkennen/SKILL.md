---
name: 27-schonfristzahlung-erkennen
description: "Schonfristzahlung erst nach Rechtshängigkeit der Räumungsklage prüfen. Jobcenter-Zahlung, vollständige Befriedigung, fristlose und ordentliche Kündigung, Kostenpfad und Klageumstellung trennen. Zahlung vor Zustellung als eigenes Kostenereignis aussondern. Output Vermerk."
---

# Schonfristzahlung erkennen

## Zweck und Anwendungsfall

Dieser Skill erkennt eine Schonfristzahlung und steuert die prozessuale Reaktion. Anwendungsfall ist eine Zahlung des Mieters oder einer öffentlichen Stelle nach Rechtshängigkeit der Räumungsklage. Zahlung vor Zustellung ist kein Schonfristfall; zuerst werden Chronologie, Vorverzug, Kenntnisstand, Kostenweg und nötige Antragsreaktion geklärt. Die technische Einreichungswerkstatt folgt erst danach.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- SAP-Mietkonto mit Zahlungseingängen.
- Datum der Rechtshängigkeit (Zustellung der Klage an den Mieter).
- Angaben zu früheren Schonfristfällen der letzten zwei Jahre.

## Ablauf / Checkliste

1. Tatbestand nach Paragraf 569 Abs. 3 Nr. 2 BGB prüfen: Wird die Vermieterin spätestens bis zum Ablauf von zwei Monaten nach Rechtshängigkeit des Räumungsanspruchs hinsichtlich der fälligen Miete und der fälligen Nutzungsentschädigung nach Paragraf 546a Abs. 1 BGB vollständig befriedigt oder verpflichtet sich eine öffentliche Stelle hierzu verbindlich, wird die fristlose Kündigung wegen Zahlungsverzugs unwirksam. Eine bloße Ankündigung genügt nicht; außerdem darf in den vorangegangenen zwei Jahren keine Kündigung bereits nach dieser Vorschrift unwirksam geworden sein.
2. Wirkung beachten: Die hilfsweise ausgesprochene ordentliche Kündigung nach Paragraf 573 Abs. 2 Nr. 1 BGB wird durch die Schonfristzahlung nicht automatisch unwirksam (BGH 23.07.2025 — VIII ZR 287/23; BGH 09.04.2025 — VIII ZR 145/24; BGH 05.10.2022 — VIII ZR 307/21; BGH, Urteil vom 13.10.2021 — VIII ZR 91/20; BGH 16.02.2005 — VIII ZR 6/04). Die Zahlung bleibt bei Verschulden, Erheblichkeit und Sozialklausel-Risiko zu würdigen.
3. Gesetzgebungsstatus hart trennen: BT-Drs. 21/6807 schlägt eine einmalige Übertragung der Schonfristwirkung auf die ordentliche Kündigung vor, ist am 09.08.2026 aber nur Ausschussvorlage und nicht geltendes Recht. Diese Entwurfsfolge weder in Schriftsatz noch Entscheidungsvorschlag übernehmen. Erst nach Verkündung sind endgültiger Wortlaut, Inkrafttreten und Übergangsrecht neu zu prüfen.
4. Renofa-Prüfung durchführen: Zahlungseingang im SAP-Mietkonto prüfen; Datum der Rechtshängigkeit feststellen; Differenz von höchstens zwei Monaten prüfen; prüfen, ob die Zahlung die komplette Forderung deckt; vergangene Schonfristfälle der letzten zwei Jahre prüfen; Teilleistung, Kostenrückstand oder laufende Neuverzugsposten gesondert ausweisen.
5. Aktion bei vollständiger Schonfristzahlung: Für die Räumung wegen fristloser Kündigung Erledigung nach Paragraf 91a ZPO vorbereiten, aber nicht blind absenden. Vor jeder Erledigung oder Rücknahme Kostenpfad prüfen: Zeitpunkt vor/nach Rechtshängigkeit, vollständige/teilweise Erledigung, Vorverzug, Forderungs- und Kenntnisstand bei Einreichung sowie Kausalität der Klagekosten. Materiell-rechtliche Kostenerstattung nur für den tragfähig belegten Anteil prüfen.
6. Die ordentliche Kündigung nur weiterverfolgen, wenn Verschulden, Erheblichkeit, Frist und Sozialklausel-Risiko nach Aktenlage tragfähig bleiben; andernfalls Erledigung insgesamt oder anwaltliche Freigabe empfehlen.
7. Bei Zahlung vor Zustellung oder sonstigem Wegfall des Rechtsschutzbedürfnisses Chronologie in Skill `05`, Vorverzug und Klagekosten in Skill `11` sowie Kostenpfad und Antragsreaktion in Skills `37` und `38` prüfen. BGH III ZR 156/12 anhand des amtlichen Volltexts verifizieren. Vor Erklärung an das Gericht RA-Freigabe über Skill `08` einholen; Skill `23` baut erst danach das fachlich freigegebene geänderte Einreichungspaket.
8. Für jeden Schriftsatz zur Erledigung, Antragsumstellung oder Fortführung eine getrennte Freigabekarte erstellen: Zahlungsdatum, Rechtshängigkeit, Heilungsumfang, verbleibender Antrag, ordentliche Kündigung, Kostenpfad, Anlagen, Frist und Freigabeperson. Status bis zur dokumentierten Freigabe `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für die mietrechtliche BGH-Kontrollspur siehe `references/gepruefte-bgh-anker-mietrecht.md`; für BT-Drs. 21/6807 gilt das Entwurfs-Gate in `references/rechtsstand-2026-verfahren-vollstreckung.md`.

## Ausgabeformat

Aktenvermerk zur Schonfristlage, Forderungsupdate, Kostenpfad-Matrix, getrennte interne Freigabekarte, Schriftsatz zur teilweisen Erledigung oder Klageumstellung und Entscheidungsvorschlag zur ordentlichen Kündigung. Vermerk und Schriftsatz werden in vollständigen, ausformulierten Sätzen geliefert (Ausformulierungspflicht).

## Beispiele

- Jobcenter zahlt sechs Wochen nach Zustellung den vollen Rückstand: fristlose Kündigung wird unwirksam; Teilerledigung der Zahlung, Kostenpfad und Weiterverfolgung der Räumung aus der ordentlichen Kündigung werden getrennt.
- Nur Teilzahlung innerhalb der Frist: keine Heilung; Forderung wird aktualisiert und der Verzugsrest gesondert ausgewiesen.
