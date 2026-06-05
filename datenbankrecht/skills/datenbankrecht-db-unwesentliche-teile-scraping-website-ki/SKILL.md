---
name: datenbankrecht-db-unwesentliche-teile-scraping-website-ki
description: "DB Unwesentliche Teile Scraping Website KI: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Unwesentliche Teile Scraping Website KI

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Unwesentliche Teile Scraping Website KI** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-005-unwesentliche-teile-wiederholte-systematische-entnahme` | Analysiert den Kumulations-Tatbestand des § 87b Abs. 1 S. 2 UrhG: Wiederholte und systematische Entnahme unwesentlicher Teile als verbotene Umgehungsstrategie. Prüft Regelmäßigkeit, Automatisierung und wirtschaftliche Auswirkung anhand Art. 7 Abs. 5 RL 96/9/EG und EuGH-Rechtsprechung. Bewertet Crawling-Muster und erstellt Nachweisstrategie. |
| `db-006-scraping-website-datenbank-und-robots-txt` | Rechtliche Bewertung von Web-Scraping gegen Websites mit Datenbankcharakter: Prüft §§ 87a-87e UrhG, Verstoß gegen AGB (§ 307 BGB), robots.txt-Bindungswirkung, Wettbewerbsrecht (§§ 3 4 UWG) und strafrechtliche Relevanz (§ 202a StGB). Bewertet EuGH C-202/12 (Innoweb/Wegener) und erstellt Risikoampel für Betreiber und Scraper. |
| `db-008-ki-training-mit-datenbankbestand` | Rechtliche Analyse des KI-Trainings mit Datenbankbeständen: §§ 44b und 60d UrhG (Text- und Data-Mining-Schranken), Verhältnis zu §§ 87a-87e UrhG, Opt-out-Pflichten nach § 44b Abs. 3 UrhG und DSM-RL Art. 4. Bewertet kommerzielle vs. wissenschaftliche TDM-Nutzung und erstellt Compliance-Plan für KI-Unternehmen und Datenbankbetreiber. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Unwesentliche Teile Scraping Website KI**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-005-unwesentliche-teile-wiederholte-systematische-entnahme`

**Fokus:** Analysiert den Kumulations-Tatbestand des § 87b Abs. 1 S. 2 UrhG: Wiederholte und systematische Entnahme unwesentlicher Teile als verbotene Umgehungsstrategie. Prüft Regelmäßigkeit, Automatisierung und wirtschaftliche Auswirkung anhand Art. 7 Abs. 5 RL 96/9/EG und EuGH-Rechtsprechung. Bewertet Crawling-Muster und erstellt Nachweisstrategie.

# Unwesentliche Teile — wiederholte und systematische Entnahme als Verletzung

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

## Output

- Kumulationsnachweis-Tabelle (Abrufprotokoll nach Zeit und Volumen)
- Systematizitäts-Analyse (Muster, Automatisierungshinweise)
- Unterlassungs- und Auskunftsschreiben
- Sachverhaltsbeschreibung für einstweilige Verfügung
- Beweissicherungsprotokoll (technische Mittel)

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 102 UrhG Verjährung — dejure.org](https://dejure.org/gesetze/UrhG/102.html)

## 2. `db-006-scraping-website-datenbank-und-robots-txt`

**Fokus:** Rechtliche Bewertung von Web-Scraping gegen Websites mit Datenbankcharakter: Prüft §§ 87a-87e UrhG, Verstoß gegen AGB (§ 307 BGB), robots.txt-Bindungswirkung, Wettbewerbsrecht (§§ 3 4 UWG) und strafrechtliche Relevanz (§ 202a StGB). Bewertet EuGH C-202/12 (Innoweb/Wegener) und erstellt Risikoampel für Betreiber und Scraper.

# Scraping gegen Websites mit Datenbankcharakter — Rechtliche Risikoanalyse

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

## Output

- Risikoampel (Scraping-Vorhaben: grün/gelb/rot nach Datenbankschutz, AGB, Strafrecht)
- AGB- und robots.txt-Analyse-Checkliste
- Unterlassungsschreiben für betroffene Betreiber
- Compliance-Leitfaden für eigene Scraping-Aktivitäten
- Beweissicherungsprotokoll für angegriffene Datenbankbetreiber

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 4 UWG — dejure.org](https://dejure.org/gesetze/UWG/4.html)
- [§ 202a StGB — dejure.org](https://dejure.org/gesetze/StGB/202a.html)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 3. `db-008-ki-training-mit-datenbankbestand`

**Fokus:** Rechtliche Analyse des KI-Trainings mit Datenbankbeständen: §§ 44b und 60d UrhG (Text- und Data-Mining-Schranken), Verhältnis zu §§ 87a-87e UrhG, Opt-out-Pflichten nach § 44b Abs. 3 UrhG und DSM-RL Art. 4. Bewertet kommerzielle vs. wissenschaftliche TDM-Nutzung und erstellt Compliance-Plan für KI-Unternehmen und Datenbankbetreiber.

# KI-Training mit Datenbankbeständen — Datenbankrecht und TDM-Schranken

## Mandantenfall

- KI-Startup möchte eine kommerzielle Sprachmodell-Trainingsdatenbank aus lizenzierten und öffentlichen Quellen zusammenstellen und benötigt Rechtssicherheit zur TDM-Schranke.
- Datenbankbetreiber fragt, wie er sein Opt-out gegen KI-Training technisch und rechtlich wirksam dokumentieren kann.
- Forschungsinstitut will eine Datenbanksammlung für nicht-kommerzielle Textanalyse nutzen und prüft, ob § 60d UrhG die Nutzung erlaubt.

## Erste Schritte

1. Nutzungsart bestimmen: Kommerzielles KI-Training (§ 44b UrhG) oder wissenschaftliche Forschung (§ 60d UrhG)?
2. Datenbankschutz der Quelle prüfen: Greift §§ 87a ff. UrhG für die Quelldatenbank? Ist eine Lizenz oder Schranke erforderlich?
3. Opt-out der Rechteinhaber prüfen: Hat der Datenbankbetreiber einen maschinenlesbaren Opt-out erklärt (§ 44b Abs. 3 UrhG)?
4. Vertragslage analysieren: Lizenzbedingungen der Quelldatenbank, AGB, API-Nutzungsbedingungen — erlauben sie Training?
5. Technische Umsetzung des Opt-outs dokumentieren: robots.txt-Einträge, HTTP-Header, Metadaten — reichen diese als maschinenlesbarer Vorbehalt?
6. DSGVO-Schnittmenge prüfen: Enthält die Trainingsdatenbank personenbezogene Daten (§ 12 DSGVO, Art. 6 Abs. 1 DSGVO)?

## Rechtsrahmen

- § 44b UrhG: TDM-Schranke für kommerzielle Zwecke — erlaubt Vervielfältigung für TDM, es sei denn, Rechteinhaber hat Opt-out erklärt.
- § 60d UrhG: TDM-Schranke für wissenschaftliche Forschung — weitgehend zwingend, kaum Opt-out möglich.
- § 87b UrhG: Datenbankherstellerrecht — TDM-Schranken gelten auch gegenüber dem sui-generis-Recht (§ 87c Abs. 1 Nr. 4 UrhG).
- DSM-RL Art. 3-4 (RL 2019/790): Europäische Grundlage der TDM-Schranken; Art. 4 für kommerzielle TDM mit Opt-out.
- § 87c UrhG: Erlaubte Handlungen — Verweis auf § 44b und § 60d als Schranken.
- Art. 6 Abs. 1 DSGVO: Rechtsgrundlage für Verarbeitung personenbezogener Trainingsdaten.

## Prüfraster

- Dient das KI-Training einem kommerziellen oder wissenschaftlichen Zweck?
- Wurde ein wirksamer maschinenlesbarer Opt-out durch den Datenbankbetreiber erklärt?
- Enthält die Datenbank urheberrechtlich oder durch Herstellerrecht geschützte Inhalte?
- Erlauben vorhandene Lizenzverträge die Nutzung für KI-Training explizit oder schließen sie diese aus?
- Werden personenbezogene Daten für das Training verwendet — welche DSGVO-Rechtsgrundlage gilt?
- Sind die erzeugten KI-Modelle selbst als abgeleitete Datenbankwerke einzuordnen?
- Welche Dokumentationspflichten gelten für den Trainingsdatensatz (Transparenz, DSM-RL Erwägungsgrund 18)?

## Typische Fallstricke

- Opt-out nach § 44b Abs. 3 UrhG muss maschinenlesbar sein — ein allgemeines AGB-Verbot reicht nicht aus.
- Kommerzielle TDM-Schranke schützt nicht, wenn der Opt-out vor dem Abruf wirksam erklärt wurde.
- Auch öffentlich zugängliche Datenbanken können durch Herstellerrecht geschützt sein — öffentlich ≠ frei nutzbar.
- § 60d UrhG gilt nur für originär wissenschaftliche Forschung, nicht für Forschungs-Spin-offs mit kommerziellem Fokus.
- Das erzeugte KI-Modell kann Datenbankschutz der Quelldatenbank weitertragen, wenn Trainingsdaten direkt abrufbar sind.

## Output

- TDM-Compliance-Prüfbericht (kommerziell/wissenschaftlich, Opt-out-Status)
- Opt-out-Implementierungsguide für Datenbankbetreiber (robots.txt, HTTP-Header)
- Lizenz-Checkliste für Trainingsdaten-Beschaffung
- Datenschutz-Kurzprüfung (DSGVO-Rechtsgrundlage für personenbezogene Trainingsdaten)
- Vertragsmuster für KI-Trainingsdaten-Lizenz

## Quellen

- [§ 44b UrhG TDM-Schranke — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [§ 60d UrhG wissenschaftliches TDM — dejure.org](https://dejure.org/gesetze/UrhG/60d.html)
- [§ 87c UrhG erlaubte Handlungen — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [DSM-Richtlinie 2019/790 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
