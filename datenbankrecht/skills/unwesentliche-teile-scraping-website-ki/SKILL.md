---
name: unwesentliche-teile-scraping-website-ki
description: "Analysiert den Kumulations-Tatbestand des § 87b Abs. 1 S. 2 UrhG: Wiederholte und systematische Entnahme unwesentlicher Teile als verbotene Umgehungsstrategie. Prüft Regelmäßigkeit, Automatisierung und wirtschaftliche Auswirkung anhand Art. 7 Abs. 5 RL 96/9/EG und EuGH-Rechtsprechung. Bewertet Crawling-Muster und erstellt Nachweisstrategie im Datenbankrecht."
---

# Unwesentliche Teile — wiederholte und systematische Entnahme als Verletzung

## Arbeitsbereich

Analysiert den Kumulations-Tatbestand des § 87b Abs. 1 S. 2 UrhG: Wiederholte und systematische Entnahme unwesentlicher Teile als verbotene Umgehungsstrategie. Prüft Regelmäßigkeit, Automatisierung und wirtschaftliche Auswirkung anhand Art. 7 Abs. 5 RL 96/9/EG und EuGH-Rechtsprechung. Bewertet Crawling-Muster und erstellt Nachweisstrategie. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber stellt fest, dass ein Wettbewerber täglich kleine Mengen an Datensätzen abruft, die einzeln unterhalb der Wesentlichkeitsschwelle liegen, aber in Summe den Datenbankbestand duplizieren.
- Startup betreibt einen Preisvergleichsdienst und ist unsicher, ob sein automatisiertes Abrufen kleiner Datenpakete den Kumulations-Tatbestand erfüllt.
- Anwalt möchte für einen Mandanten prüfen, ob eine technische Drosselung der API-Abfragen (rate limiting) die rechtliche Problematik beseitigt.

## Erste Schritte

1. Entnahmemuster dokumentieren: Häufigkeit, Zeitintervalle, Volumen pro Abruf und Gesamtvolumen über den gesamten Zeitraum erfassen.
2. Systematik nachweisen: Automatisierter Prozess? Regelmäßige Intervalle? Ziel der Vollständigkeitsduplizierung erkennbar?
3. Wirtschaftliche Auswirkung beurteilen: Ersetzt die kumulative Entnahme die Nutzung der Originaldatenbank oder konkurriert sie wirtschaftlich?
4. Abgrenzung zur erlaubten Nutzung: § 87c UrhG (zulässige Entnahmen), Vertragslage, Schranken prüfen.
5. Technische Beweise sichern: API-Logs, Crawling-Protokolle, IP-Adressen, User-Agent-Strings, Zeitstempel.
6. Unterlassungsanspruch formulieren: Kumulative Entnahme als eigenständiger Verletzungstatbestand darlegen.

## Rechtsrahmen

- § 87b Abs. 1 S. 2 UrhG: Wiederholte und systematische Entnahme unwesentlicher Teile gleichgestellt mit Entnahme wesentlicher Teile.
- Art. 7 Abs. 5 RL 96/9/EG: Europäische Grundlage des Kumulationstatbestands — verhindert Umgehung durch Stückelung.
- § 87b Abs. 1 S. 1 UrhG: Haupttatbestand der wesentlichen Entnahme als Vergleichsmaßstab.
- § 87c UrhG: Schranken des Datenbankherstellerrechts — zulässige Entnahmen für rechtmäßige Nutzer.
- EuGH C-203/02 (BHB/William Hill) Rn. 86-92: Kumulationsverbot bei systematischer Entnahme kleiner Teile.
- Art. 8 RL 96/9/EG: Rechte und Pflichten rechtmäßiger Nutzer — Grenze zwischen zulässigem Zugriff und verbotener Entnahme.

## Prüfraster

- Sind die einzelnen Entnahmen für sich unwesentlich, kumulieren sie aber über Zeit zu einer wesentlichen Gesamtentnahme?
- Ist ein systematisches Muster erkennbar (Automatisierung, feste Intervalle, Vollständigkeitsziel)?
- Orientiert sich die Entnahmetätigkeit erkennbar daran, eine eigene Datenbank mit demselben Inhalt aufzubauen?
- Beeinträchtigt die kumulative Entnahme die normale Auswertung der Datenbank oder die berechtigten Interessen des Herstellers?
- Liegt ein Vertrag (AGB, Lizenz) vor, der bestimmte Entnahmen erlaubt oder verbietet?
- Hat der Hersteller robots.txt, API-Nutzungsbedingungen oder technische Schutzmaßnahmen eingesetzt?
- Sind die Entnahmen auf mehrere IP-Adressen oder Accounts verteilt, um Erkennung zu verschleiern?

## Typische Fallstricke

- Rate-Limiting-Compliance entbindet nicht von der Kumulations-Prüfung: Auch kleine erlaubte Einzelabrufe können kumulativ verboten sein, wenn sie auf Vollständigkeitskopie zielen.
- Vertragliche Erlaubnis für einzelne Abrufe schließt den gesetzlichen Kumulationstatbestand nicht zwingend aus.
- Technische Verschleierung (rotierende IPs, verschiedene User-Agents) ist kein rechtfertigender Umstand, verschärft aber Vorsatz-Indiz.
- Zeitlicher Nachweis der Systematik erfordert lückenlose Logs über längere Zeiträume — Einmalsicherungen sind unzureichend.
- Anspruch verjährt nach § 102 UrhG (regelmäßige Verjährungsfrist § 195 BGB, 3 Jahre) — Fristbeginn ab Kenntnis prüfen.

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 102 UrhG Verjährung — dejure.org](https://dejure.org/gesetze/UrhG/102.html)

