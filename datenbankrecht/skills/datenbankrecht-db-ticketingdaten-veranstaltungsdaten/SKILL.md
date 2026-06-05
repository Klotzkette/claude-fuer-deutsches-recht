---
name: datenbankrecht-db-ticketingdaten-veranstaltungsdaten
description: "DB Ticketingdaten Veranstaltungsdaten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Ticketingdaten Veranstaltungsdaten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Ticketingdaten Veranstaltungsdaten** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-023-ticketingdaten-veranstaltungsdaten-und-kalender` | Datenbankrecht für Veranstaltungsdatenbanken und Ticketing-Plattformen: §§ 87a-87e UrhG für Veranstaltungskalender, Abgrenzung zur selbsterzeugten Eventdaten-Problematik nach EuGH C-203/02, Schutz gegen Aggregatoren und Konkurrenzportale sowie Lizenzmodelle für Veranstaltungsdaten-APIs. Bewertet Datenschutzaspekte bei Käuferdaten. |
| `db-024-stellenanzeigen-jobportal-und-scraping` | Datenbankrecht für Jobportale und Stellenanzeigen-Datenbanken nach EuGH C-202/12 (Innoweb/Wegener): Wesentliche Investition in Stellenanzeigen-Sammlung, Schutz gegen Konkurrenz-Jobsuchmaschinen und Aggregatoren, AGB-Scraping-Verbote sowie DSGVO-Pflichten bei Bewerber- und Arbeitgeberdaten. Erstellt Schutzkonzept und Lizenzstruktur für Jobportale. |
| `db-025-rezeptdaten-gesundheitsdaten-und-sozialdaten` | Datenbankrecht für Gesundheitsdatenbanken: §§ 87a-87e UrhG für Arzneimitteldatenbanken und Patientenregister, besonderer Schutz nach Art. 9 DSGVO für Gesundheitsdaten, DSGVO-Zweckbindung und Weitergabe, Forschungsschranken nach § 27 BDSG und KI-Nutzung von Gesundheitsdaten. Erstellt Rechts-Compliance-Konzept für HealthTech-Anbieter und Kliniken. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Ticketingdaten Veranstaltungsdaten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-023-ticketingdaten-veranstaltungsdaten-und-kalender`

**Fokus:** Datenbankrecht für Veranstaltungsdatenbanken und Ticketing-Plattformen: §§ 87a-87e UrhG für Veranstaltungskalender, Abgrenzung zur selbsterzeugten Eventdaten-Problematik nach EuGH C-203/02, Schutz gegen Aggregatoren und Konkurrenzportale sowie Lizenzmodelle für Veranstaltungsdaten-APIs. Bewertet Datenschutzaspekte bei Käuferdaten.

# Ticketing-Daten, Veranstaltungsdaten und Kalender — Datenbankrecht

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

## Output

- Datenbankherstellerrecht-Gutachten für Eventdatenbank
- Aggregator-Risikobewertung (§ 87b UrhG + Innoweb-Test)
- Event-API-Lizenzvertrag-Vorlage
- DSGVO-Prüfbogen für Käuferdaten (Ticketing)
- AGB-Klausel-Empfehlung gegen Scraping von Eventdaten

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)

## 2. `db-024-stellenanzeigen-jobportal-und-scraping`

**Fokus:** Datenbankrecht für Jobportale und Stellenanzeigen-Datenbanken nach EuGH C-202/12 (Innoweb/Wegener): Wesentliche Investition in Stellenanzeigen-Sammlung, Schutz gegen Konkurrenz-Jobsuchmaschinen und Aggregatoren, AGB-Scraping-Verbote sowie DSGVO-Pflichten bei Bewerber- und Arbeitgeberdaten. Erstellt Schutzkonzept und Lizenzstruktur für Jobportale.

# Stellenanzeigen, Jobportale und Scraping — Datenbankrecht nach Innoweb

## Mandantenfall

- Jobportal-Betreiber stellt fest, dass eine neue Jobsuchmaschine alle Stellenanzeigen in Echtzeit aus seiner Datenbank abfragt und eigene Suchergebnisse anzeigt — Grundlage der EuGH-Innoweb-Entscheidung.
- Recruiter-Startup will Stellenanzeigen aus mehreren Jobportalen aggregieren und fragt, welche Lizenzen es benötigt.
- Unternehmen hat eine interne Jobdatenbank aufgebaut und möchte diese extern lizenzieren — wie definiert es den Nutzungsumfang?

## Erste Schritte

1. Innoweb-Entscheidung anwenden: EuGH C-202/12 — Meta-Jobsuchmaschine, die Echtzeitsuche auf Fremddatenbank ausführt, verwendet wesentliche Teile weiter.
2. Datenbankherstellerrecht des Jobportals prüfen: Wesentliche Investition in Sammlung (Einholung von Arbeitgeberdaten), Überprüfung (Qualitätsprüfung, Kategorisierung) und Darstellung?
3. Verletzungsanalyse: Handelt der Aggregator in Echtzeit (Innoweb) oder ruft er periodisch Daten ab (Kumulationstatbestand)?
4. AGB-Scraping-Verbot prüfen: Ist das Verbot wirksam, klar formuliert und nach § 307 BGB nicht unangemessen?
5. DSGVO-Prüfung: Stellenanzeigen können personenbezogene Daten von Ansprechpartnern enthalten — Zweckbindung bei Weitergabe.
6. Lizenzmodell für Stellendaten-Feed: Welche Nutzung darf der Aggregator käuflich erwerben, und welche Verbote bleiben im Vertrag?

## Rechtsrahmen

- EuGH C-202/12 (Innoweb/Wegener): Meta-Jobsuchmaschine, die Fremddatenbank in Echtzeit durchsucht, verweist Nutzer zur Fremddatenbank — wesentliche Weiterverwendung bejaht.
- § 87a UrhG: Jobportal als Datenbankherstellerin — wesentliche Investition in Beschaffung und Darstellung von Stellenanzeigen.
- § 87b UrhG: Wesentliche Entnahme und Weiterverwendung ohne Lizenz des Jobportals untersagt.
- Art. 7 Abs. 2 lit. b RL 96/9/EG: Weiterverwendung — auch mittelbare Nutzung erfasst.
- § 307 BGB: AGB-Scraping-Klausel wirksam bei klarer Formulierung und verhältnismäßiger Rechtsfolge.
- Art. 6 Abs. 1 lit. f DSGVO: Berechtigtes Interesse als Rechtsgrundlage für Verarbeitung von Arbeitgeberkontakten in Stellenanzeigen.

## Prüfraster

- Hat das Jobportal eine wesentliche Investition in Beschaffung von Stellenanzeigen (aktives Einwerben von Arbeitgebern) und Darstellung getätigt?
- Führt der Aggregator eine Echtzeit-Suche durch die Fremddatenbank aus (Innoweb-Test) oder archiviert er Daten periodisch?
- Ist das AGB-Scraping-Verbot wirksam einbezogen und hinreichend bestimmt?
- Kumuliert der Aggregator bei periodischen Abfragen systematisch wesentliche Teile?
- Sind Ansprechpartner-Kontaktdaten in Stellenanzeigen personenbezogen — welche DSGVO-Rechtsgrundlage gilt für deren Weitergabe?
- Bietet das Jobportal bereits ein API-Lizenzmodell an, und schließt der Aggregator die dort definierten Bedingungen ein?
- Besteht wettbewerbsrechtliche gezielte Behinderung (§ 4 Nr. 4 UWG) durch den Aggregator?

## Typische Fallstricke

- Innoweb-Entscheidung gilt spezifisch für Echtzeit-Meta-Suche — periodische Crawling-Abfragen werden anders bewertet.
- Stellenanzeigen-Portale, die nur von Arbeitgebern befüllte Formulare anzeigen, haben möglicherweise weniger Investition in Beschaffung als vermutet.
- Arbeitgeber können eigene Urheberrechte an Stellenanzeigentexten behalten — Jobportal lizenziert nur das Datenbankherstellerrecht.
- DSGVO-Grundlage für Kontaktdaten in Stellenanzeigen ist berechtigtes Interesse — aber Weitergabe an Dritte ohne weitere Rechtsgrundlage problematisch.
- Aggregatoren können sich auf § 87c UrhG (zulässige Handlungen) berufen — prüfen, ob Ausnahmen einschlägig sind.

## Output

- Innoweb-Verletzungsanalyse (Echtzeit-Meta-Suche vs. periodisches Crawling)
- Datenbankherstellerrecht-Gutachten für Jobportal
- AGB-Klausel-Vorlage für Scraping-Verbot
- Jobdaten-Lizenzvertrag-Muster (API-Feed)
- DSGVO-Prüfbogen für Kontaktdaten in Stellenanzeigen

## Quellen

- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 4 UWG — dejure.org](https://dejure.org/gesetze/UWG/4.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 3. `db-025-rezeptdaten-gesundheitsdaten-und-sozialdaten`

**Fokus:** Datenbankrecht für Gesundheitsdatenbanken: §§ 87a-87e UrhG für Arzneimitteldatenbanken und Patientenregister, besonderer Schutz nach Art. 9 DSGVO für Gesundheitsdaten, DSGVO-Zweckbindung und Weitergabe, Forschungsschranken nach § 27 BDSG und KI-Nutzung von Gesundheitsdaten. Erstellt Rechts-Compliance-Konzept für HealthTech-Anbieter und Kliniken.

# Rezeptdaten, Gesundheitsdaten und Sozialdaten — Datenbankrecht und Datenschutz

## Mandantenfall

- HealthTech-Startup will anonymisierte Patientendaten einer Klinikdatenbank für KI-Modell-Training nutzen und fragt nach dem rechtlichen Rahmen.
- Pharmaunternehmen hat eine Arzneimitteldatenbank aufgebaut und will diese an Forschungseinrichtungen lizenzieren — welche Rechte können übertragen werden?
- Krankenkasse möchte ihre Rezeptdatenbank für Versorgungsforschung zugänglich machen und fragt nach DSGVO-Anforderungen und Datenbankschutz.

## Erste Schritte

1. Datenbankherstellerrecht prüfen: Wesentliche Investition in Aufbau und Pflege der Gesundheitsdatenbank (§ 87a UrhG)?
2. Besondere Kategorien nach Art. 9 DSGVO prüfen: Gesundheitsdaten sind besondere Kategorien — erhöhte Anforderungen an Rechtsgrundlage (Art. 9 Abs. 2 DSGVO).
3. Anonymisierungs- und Pseudonymisierungsgrad bewerten: Sind die Daten tatsächlich anonym oder nur pseudonymisiert — welche Datenschutzpflichten verbleiben?
4. Forschungsschranken klären: § 27 BDSG für wissenschaftliche Forschung, Art. 9 Abs. 2 lit. j DSGVO — erlaubte Verarbeitung für Gesundheitsforschung.
5. Zweckbindungspflicht bei Lizenzierung: Gesundheitsdaten dürfen nur für vereinbarte Zwecke genutzt werden — vertragliche Zweckbindungsklausel.
6. KI-Training mit Gesundheitsdaten: § 44b UrhG TDM-Schranke und Art. 9 DSGVO — erhöhter Schutzstandard beachten.

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht für Gesundheitsdatenbanken — Investition in Beschaffung, Überprüfung und Darstellung von Patientendaten.
- Art. 9 DSGVO: Besondere Kategorien personenbezogener Daten — Verarbeitung von Gesundheitsdaten erfordert explizite Ausnahme.
- Art. 9 Abs. 2 lit. j DSGVO: Verarbeitung für Forschungszwecke im öffentlichen Interesse mit angemessenen Schutzmaßnahmen.
- § 27 BDSG: Verarbeitung für wissenschaftliche Forschung — nationale Umsetzung der Forschungsschranke.
- § 44b UrhG: TDM-Schranke auch für Gesundheitsdatenbanken — aber DSGVO-Anforderungen bei personenbezogenen Daten bleiben.
- SGB V §§ 284 ff.: Datenschutzrecht für Sozialdaten (Krankenversicherungsdaten) — besondere gesetzliche Schranken.

## Prüfraster

- Liegt eine wesentliche Investition in die Gesundheitsdatenbank vor (Erhebungsaufwand, Qualitätsprüfung, Kodierung)?
- Sind die Daten wirklich anonymisiert, oder handelt es sich um Pseudonymisierung mit Reidentifikationsrisiko?
- Liegt eine Rechtsgrundlage nach Art. 9 Abs. 2 DSGVO für die geplante Nutzung vor?
- Gilt die Forschungsschranke nach § 27 BDSG — ist der Zweck wissenschaftliche Forschung im öffentlichen Interesse?
- Ist die Zweckbindung bei Lizenzierung an externe Forschungseinrichtungen vertraglich abgesichert?
- Werden KI-Modelle mit den Gesundheitsdaten trainiert — greifen TDM-Schranke und DSGVO gleichzeitig?
- Liegen Sozialdaten (SGB-Daten) vor — gelten besondere gesetzliche Schranken des Sozialgeheimnisses?

## Typische Fallstricke

- Pseudonymisierte Daten sind keine anonymisierten Daten — DSGVO gilt weiterhin, besondere Kategorien ebenfalls.
- Forschungsschranke nach § 27 BDSG setzt echten wissenschaftlichen Zweck voraus — kommerzielle KI-Entwicklung reicht nicht.
- Lizenznehmer können mit den Daten Sekundärprodukte entwickeln, die nicht mehr von der Zweckbindung erfasst sind — klare Verbote erforderlich.
- Reidentifikation aus anonymisierten Gesundheitsdaten ist durch moderne KI-Methoden möglich — Risikoanalyse nach Art. 35 DSGVO (DSFA) erforderlich.
- Sozialdaten der Krankenkassen unterliegen dem Sozialgeheimnis (§ 35 SGB I) — Weitergabe an Private fast immer unzulässig.

## Output

- Datenbankherstellerrecht-Gutachten für Gesundheitsdatenbank
- Art. 9 DSGVO-Rechtsgrundlagen-Check für Gesundheitsdatennutzung
- Zweckbindungs-Lizenzklausel für Gesundheitsdatenbank-Lizenzvertrag
- Anonymisierungs-/Pseudonymisierungs-Risikoanalyse
- Forschungsschranken-Prüfbogen (§ 27 BDSG / Art. 9 Abs. 2 lit. j DSGVO)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [Art. 9 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/9.html)
- [§ 27 BDSG — dejure.org](https://dejure.org/gesetze/BDSG/27.html)
- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [Art. 35 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/35.html)
