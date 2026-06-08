---
name: scraping-website-datenbank-und-robots-txt
description: "Rechtliche Bewertung von Web-Scraping gegen Websites mit Datenbankcharakter: Prüft §§ 87a-87e UrhG, Verstoß gegen AGB (§ 307 BGB), robots.txt-Bindungswirkung, Wettbewerbsrecht (§§ 3 4 UWG) und strafrechtliche Relevanz (§ 202a StGB). Bewertet EuGH C-202/12 (Innoweb/Wegener) und erstellt Risikoampel für Betreiber und Scraper im Datenbankrecht."
---

# Scraping gegen Websites mit Datenbankcharakter — Rechtliche Risikoanalyse

## Arbeitsbereich

Rechtliche Bewertung von Web-Scraping gegen Websites mit Datenbankcharakter: Prüft §§ 87a-87e UrhG, Verstoß gegen AGB (§ 307 BGB), robots.txt-Bindungswirkung, Wettbewerbsrecht (§§ 3 4 UWG) und strafrechtliche Relevanz (§ 202a StGB). Bewertet EuGH C-202/12 (Innoweb/Wegener) und erstellt Risikoampel für Betreiber und Scraper. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Preisvergleich-Startup will Produktdaten von Händlerwebsites automatisiert abrufen und fragt nach dem rechtlichen Risiko.
- Betreiber eines Immobilienportals entdeckt, dass ein Mitbewerber Exposés systematisch abgreift, und will Unterlassungsansprüche geltend machen.
- KI-Unternehmen plant, öffentlich zugängliche Websites als Trainingsdaten zu harvesten, und benötigt eine rechtliche Bewertung der Zulässigkeit.

## Erste Schritte

1. Datenbankcharakter der Zielwebsite prüfen: Sind die Daten systematisch geordnet und über Suchabfragen individuell zugänglich (§ 87a Abs. 1 UrhG)?
2. Investitionsnachweis der Website-Betreiber abschätzen: Ressourcenaufwand für Sammlung, Pflege und Darstellung der Daten.
3. robots.txt und AGB analysieren: Verbieten sie automatisiertes Abrufen? Ist robots.txt ein verbindliches Vertragsangebot oder nur technische Empfehlung?
4. Verletzungstatbestand bestimmen: Wesentliche Entnahme (§ 87b UrhG) oder Kumulationstatbestand (§ 87b Abs. 1 S. 2 UrhG)?
5. Wettbewerbsrechtliche Prüfung: Gezielte Behinderung (§ 4 Nr. 4 UWG), Schmarotzen an fremder Leistung?
6. Strafrecht prüfen: § 202a StGB (Ausspähen von Daten) nur bei Überwindung technischer Zugangssicherungen.

## Rechtsrahmen

- §§ 87a-87b UrhG: Datenbankherstellerrecht gegen Entnahme und Weiterverwendung wesentlicher Teile.
- § 307 BGB: AGB-Kontrolle für scraping-verbietende Nutzungsbedingungen — Verbote können wirksam sein, wenn hinreichend klar formuliert.
- § 4 Nr. 4 UWG: Gezielte Behinderung — Abfangen von Kunden oder Datenmissbrauch zum Nachteil des Wettbewerbers.
- § 202a StGB: Ausspähen von Daten — nur relevant, wenn Zugangssicherungen (Passwort, CAPTCHA, technische Sperre) überwunden werden.
- EuGH C-202/12 (Innoweb/Wegener): Meta-Suchmaschine durchsucht Stellenbörsendatenbank in Echtzeit — wesentliche Weiterverwendung bejaht.
- RL 96/9/EG Art. 6 Abs. 1: Zugriffsrecht des rechtmäßigen Nutzers — gilt nicht für unbefugte Nutzer.

## Prüfraster

- Ist die Zielwebsite als Datenbank nach § 87a Abs. 1 UrhG zu qualifizieren?
- Hat der Website-Betreiber eine wesentliche Investition in Beschaffung, Überprüfung oder Darstellung getätigt?
- Verbieten robots.txt oder AGB ausdrücklich automatisiertes Abrufen oder Scraping?
- Handelt es sich um einen rechtmäßigen Nutzer (z. B. mit Account) oder einen Unbefugten?
- Überwindet das Scraping-Tool technische Schutzmaßnahmen (CAPTCHA, Login-Gate, Rate-Limit-Sperre)?
- Wird ein wesentlicher Teil entnommen, oder kumulieren wiederholte Abrufe?
- Liegt ein wirtschaftlicher Schaden oder eine Wettbewerbsverzerrung vor?

## Typische Fallstricke

- robots.txt hat keine unmittelbar gesetzliche Bindungswirkung — entscheidend ist, ob AGB auf sie Bezug nehmen oder ein Vertragsangebot vorliegt.
- Öffentlich zugängliche Daten sind nicht automatisch frei entnehmbar — das Datenbankherstellerrecht schützt unabhängig von einer Zugangssperre.
- Scrapers, die einen Nutzer-Login voraussetzen, verstoßen zusätzlich gegen §§ 307 BGB, 202a StGB.
- Aggregator-Dienste, die Echtzeit-Suche auf Fremddatenbanken betreiben, erfüllen nach Innoweb/Wegener den Weiterverwendungstatbestand.
- Wettbewerbsrechtliche Ansprüche (UWG) unterliegen kürzerer Verjährung (§ 11 UWG: 6 Monate) als urheberrechtliche.

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 4 UWG — dejure.org](https://dejure.org/gesetze/UWG/4.html)
- [§ 202a StGB — dejure.org](https://dejure.org/gesetze/StGB/202a.html)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

