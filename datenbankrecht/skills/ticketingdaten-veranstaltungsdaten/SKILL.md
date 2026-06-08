---
name: ticketingdaten-veranstaltungsdaten
description: "Datenbankrecht für Veranstaltungsdatenbanken und Ticketing-Plattformen: §§ 87a-87e UrhG für Veranstaltungskalender, Abgrenzung zur selbsterzeugten Eventdaten-Problematik nach EuGH C-203/02, Schutz gegen Aggregatoren und Konkurrenzportale sowie Lizenzmodelle für Veranstaltungsdaten-APIs. Bewertet Datenschutzaspekte bei Käuferdaten im Datenbankrecht."
---

# Ticketing-Daten, Veranstaltungsdaten und Kalender — Datenbankrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Ticketing-Plattform stellt fest, dass ein Konkurrent alle Veranstaltungsdaten täglich aus ihrer Datenbank übernimmt und auf dem eigenen Portal zeigt.
- Kulturveranstalter fragt, ob seine in einer Datenbank gepflegten Konzert- und Festivaltermine gegen systematische Übernahme durch Eventkalender-Apps geschützt sind.
- Startup will eine Veranstaltungsaggregator-App entwickeln und muss verstehen, welche Daten es frei verwenden darf und wo Lizenzen erforderlich sind.

## Erste Schritte

1. BHB/William Hill-Prüfung für Eventdaten: Erzeugt der Veranstalter die Daten selbst (Programmplanung) oder beschafft er sie aus Quellen? Investition in Datenerzeugung schützt nicht.
2. Separate Datenbankpflege-Investition nachweisen: Systematische Erfassung, Kategorisierung, Überprüfung und Darstellung von Veranstaltungsdaten als eigenständige Investition.
3. Ticketing-Datenbank prüfen: Verkaufsdaten, Sitzplatzpläne, Käuferdaten — welche Teile sind durch § 87a UrhG geschützt?
4. Verletzungsanalyse für Aggregatoren: Wesentliche Entnahme oder Kumulation von Eventdaten ohne Lizenz (§ 87b UrhG)?
5. Lizenzmodell entwickeln: Datenlizenz für Event-API, Nutzungsumfang (Veranstaltungsdetails, Bilder, Ticketverfügbarkeit), Vergütung.
6. DSGVO für Käuferdaten: Personenbezogene Käufer- und Buchungsdaten — Rechtsgrundlage, Zweckbindung, Datenweitergabe an Dritte.

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht für Eventdatenbanken — Investition in Beschaffung und Darstellung von Veranstaltungsdaten von Dritten.
- EuGH C-203/02 (BHB/William Hill): Selbst erzeugte Daten begründen kein Herstellerrecht — gilt auch für eigene Veranstaltungen.
- § 87b UrhG: Verbot der Entnahme wesentlicher Teile; Kumulationstatbestand bei wiederholtem Abgreifen von Eventdaten.
- Art. 6 Abs. 1 lit. b DSGVO: Vertragliche Rechtsgrundlage für Verarbeitung von Käuferdaten im Ticketing.
- § 307 BGB: AGB-Gestaltung für Event-API-Nutzungsbedingungen und Scraping-Verbote.
- EuGH C-202/12 (Innoweb/Wegener): Aggregatoren, die Echtzeit-Suche auf Fremddatenbanken betreiben, verwenden wesentliche Teile weiter.

## Prüfraster

- Hat die Ticketing-Plattform oder das Veranstaltungsportal eine separate wesentliche Investition in Datenbeschaffung (Einholung von Eventdaten von Veranstaltern) getätigt?
- Handelt es sich bei den abgegriffenen Eventdaten um wesentliche Teile der Datenbank (quantitativ oder qualitativ)?
- Betreibt der Aggregator eine systematische Echtzeit-Abfrage der Datenbank (Innoweb-Tatbestand)?
- Sind Sitzplatzpläne, Ticketpreise oder Kapazitätsdaten als besonders wertvolle Kerndaten anzusehen?
- Enthält die Datenbank Käuferdaten (personenbezogen) — welche DSGVO-Grundlage und Zweckbindung gilt?
- Schließen AGB und robots.txt automatisierte Abfragen wirksam aus?
- Gibt es bereits ein Lizenzmodell für Eventdaten-Feeds — schließt es die geplante Nutzung ein oder aus?

## Typische Fallstricke

- Veranstalter, die ihre eigenen Events in die Datenbank eintragen, erzeugen die Daten selbst — kein Herstellerrecht für diesen Teil.
- Portale, die Eventdaten von Veranstaltern aktiv einsammeln und qualitätsprüfen, haben separates Herstellerrecht.
- DSGVO-Weitergabe von Käuferdaten an externe Eventkalender-Apps ist ohne Einwilligung oder berechtigtes Interesse der Nutzer unzulässig.
- Aggregatoren mit Deeplinks zu Ticketportalen können Unterlassung wegen technischer Schutzmaßnahmenumgehung riskieren.
- Eventdaten werden oft von mehreren Stellen gepflegt (Veranstalter, Portal, Agentur) — Inhaberschaft des Herstellerrechts klären.

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)

