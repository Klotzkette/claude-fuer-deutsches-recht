---
name: datenbankrecht-db-oeffentliche-register-wissenschaftsdaten
description: "DB Oeffentliche Register Wissenschaftsdaten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Oeffentliche Register Wissenschaftsdaten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Oeffentliche Register Wissenschaftsdaten** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-020-oeffentliche-register-handelsregister-grundbuch-transpare` | Datenbankrecht für öffentliche Register (Handelsregister, Grundbuch, Transparenzregister): Schutzfähigkeit nach §§ 87a-87e UrhG und § 5 UrhG, Weiterverwendungsrecht nach IWG und Open-Data-RL 2019/1024, massenhafte Registerabfragen als Verletzung sowie DSGVO-Grenzen bei personenbezogenen Registereinträgen. Erstellt Compliance-Konzept für Datenaggregationsdienste. |
| `db-021-wissenschaftsdaten-forschungsdatenbank` | Datenbankrecht für Forschungsdatenbanken und Wissenschaftsdaten: § 60d UrhG (TDM-Schranke für wissenschaftliche Forschung), §§ 87a-87e UrhG für Forschungsdatenbanken, Open-Access-Pflichten nach BMBF-Richtlinien und DSM-RL Art. 3, Rechtslage bei Hochschul-Spin-offs und Forschungsdaten-Lizenzen (CC0, CC BY). Erstellt Rechtsgutachten und Datenpublikationskonzept. |
| `db-022-kartendaten-geodaten-und-luftbilder` | Datenbankrecht für Geodatenbanken, Kartendienste und Luftbilder: §§ 87a-87e UrhG für topografische Datenbanken, OpenStreetMap-ODbL-Lizenz, BKG-Nutzungsbedingungen, Verhältnis zu § 2 UrhG (Kartenwerke als Werke) und Open-Geodata-Anforderungen nach GeoZG. Bewertet Nutzung von Google Maps-, HERE- und OSM-Daten für kommerzielle Anwendungen. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Oeffentliche Register Wissenschaftsdaten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-020-oeffentliche-register-handelsregister-grundbuch-transpare`

**Fokus:** Datenbankrecht für öffentliche Register (Handelsregister, Grundbuch, Transparenzregister): Schutzfähigkeit nach §§ 87a-87e UrhG und § 5 UrhG, Weiterverwendungsrecht nach IWG und Open-Data-RL 2019/1024, massenhafte Registerabfragen als Verletzung sowie DSGVO-Grenzen bei personenbezogenen Registereinträgen. Erstellt Compliance-Konzept für Datenaggregationsdienste.

# Öffentliche Register — Handelsregister, Grundbuch und Transparenzregister

## Mandantenfall

- Fintech-Unternehmen will Handelsregisterdaten massenhaft abrufen und für eine Unternehmens-Datenbank verwenden — fragt nach Zulässigkeit und Grenzen.
- Datenaggregationsdienst hat Grundbuchdaten über Abfragen zusammengestellt und erhält eine Abmahnung von der registerführenden Behörde.
- Datenschutzbehörde kritisiert ein Transparenzregister-Scraping-Dienst, der personenbezogene Daten von wirtschaftlich Berechtigten weiterverwendet.

## Erste Schritte

1. Schutzrechtslage des Registers prüfen: Behörden können Datenbankherstellerrecht nach § 87a UrhG geltend machen, wenn wesentliche Investition in Aufbau und Pflege; § 5 UrhG schützt amtliche Werke nicht.
2. Weiterverwendungsrecht nach IWG klären: Handels- und Transparenzregister sind öffentliche Stellen — gilt das Recht auf Weiterverwendung nach § 3 IWG?
3. Massenabfragen als Verletzung prüfen: Systematische Massenabfragen können wesentliche Teile entnehmen (§ 87b UrhG) oder den Registerbetrieb stören.
4. DSGVO-Prüfung: Transparenzregister enthält personenbezogene Daten von wirtschaftlich Berechtigten — welche Zweckbindung und Weiterverwendungsschranken gelten?
5. Nutzungsbedingungen der Register analysieren: Bundesanzeiger-AGB, Grundbuch-Zugangsbedingungen, GBO-Anforderungen.
6. Zulässige Registernutzung abgrenzen: Einzelabrufe zu berechtigtem Interesse vs. systematische Gesamtabfragen.

## Rechtsrahmen

- § 87a UrhG: Öffentliche Stellen als Datenbankherstellerinnen — Investition in Registeraufbau und -pflege kann wesentlich sein.
- § 5 UrhG: Amtliche Werke (Gesetzestexte, Verordnungen) ohne Urheberrechtsschutz — gilt nicht für strukturierte Registerdatenbanken.
- IWG § 3: Recht auf Weiterverwendung von Informationen öffentlicher Stellen — Ausnahme bei Schutzrechten Dritter.
- § 12 GBO: Einsichtsrecht in das Grundbuch nur bei berechtigtem Interesse — systematische Massenabfragen nicht erfasst.
- Art. 30 Abs. 5a GWG: Öffentlicher Zugang zum Transparenzregister — aber personenbezogene Daten mit DSGVO-Zweckbindung.
- Art. 6 Abs. 1 lit. e DSGVO: Verarbeitung personenbezogener Registerdaten im öffentlichen Interesse — Zweckbindungspflicht.

## Prüfraster

- Hat die registerführende Behörde eine wesentliche Investition in Aufbau und Pflege der Registerdatenbank getätigt?
- Überschreiten die Abfragen die erlaubte Einzelnutzung und stellen systematische Massenentnahmen dar?
- Gilt das IWG für das betreffende Register, und erlaubt es die geplante Weiterverwendung?
- Enthält das Register personenbezogene Daten (Transparenzregister, Grundbuch) — welche DSGVO-Rechtsgrundlage und Zweckbindung gilt?
- Haben die Registerbehörden AGB oder Nutzungsbedingungen für digitale Abfragen erlassen?
- Besteht ein berechtigtes Interesse für die geplante Registernutzung (§ 12 GBO, § 30 GWG)?
- Wird die abgefragte Datenmenge als wesentlicher Teil der Registerdatenbank zu qualifizieren sein?

## Typische Fallstricke

- Öffentlich zugänglich ≠ frei verwendbar in großem Umfang — das Datenbankherstellerrecht gilt unabhängig von der Öffentlichkeit des Registers.
- IWG-Weiterverwendungsrecht schließt personenbezogene Daten nicht ohne weiteres ein — DSGVO-Zweckbindung bleibt.
- Massenabfragen beim Handelsregister verstoßen gegen Bundesanzeiger-AGB und können zu Sperren und Schadensersatzforderungen führen.
- Transparenzregister-Daten dürfen nur zur Bekämpfung von Geldwäsche und Terrorismusfinanzierung genutzt werden — andere Zwecke sind DSGVO-widrig.
- „Screen-Scraping" von Registerportalen kann § 202a StGB erfüllen, wenn Zugangssperren überwunden werden.

## Output

- Rechtsgutachten zur Zulässigkeit der Registernutzung
- IWG-Weiterverwendungsantrag-Vorlage
- DSGVO-Zweckbindungs-Prüfbogen für Registerdaten
- Abmahnschreiben gegen unerlaubtes Register-Massenabgreifen
- Compliance-Konzept für Datenaggregationsdienste mit Registerdaten

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 5 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/5.html)
- [IWG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/iwg/index.html)
- [§ 12 GBO — dejure.org](https://dejure.org/gesetze/GBO/12.html)
- [Open-Data-Richtlinie 2019/1024 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1024)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)

## 2. `db-021-wissenschaftsdaten-forschungsdatenbank`

**Fokus:** Datenbankrecht für Forschungsdatenbanken und Wissenschaftsdaten: § 60d UrhG (TDM-Schranke für wissenschaftliche Forschung), §§ 87a-87e UrhG für Forschungsdatenbanken, Open-Access-Pflichten nach BMBF-Richtlinien und DSM-RL Art. 3, Rechtslage bei Hochschul-Spin-offs und Forschungsdaten-Lizenzen (CC0, CC BY). Erstellt Rechtsgutachten und Datenpublikationskonzept.

# Wissenschaftsdaten und Forschungsdatenbanken — Datenbankrecht und TDM-Schranke

## Mandantenfall

- Forschungseinrichtung will ihre Biodiversitätsdatenbank unter CC0 veröffentlichen und fragt, wie sie trotzdem das Herstellerrecht schützen und Missbrauch ahnden kann.
- Hochschule möchte wissen, ob ein Spin-off-Unternehmen berechtigt ist, die Forschungsdatenbank der Universität kommerziell zu nutzen.
- Wissenschaftsjournalist will Forschungsdaten einer institutionellen Datenbank für eine Analyse nutzen und fragt, ob § 60d UrhG TDM-Schranke gilt.

## Erste Schritte

1. Datenbankherstellerrecht für Forschungsdatenbank prüfen: Wesentliche Investition in Beschaffung und Aufbereitung wissenschaftlicher Daten (§ 87a UrhG)?
2. TDM-Schranke § 60d UrhG anwenden: Wissenschaftliche Forschung, nicht-kommerziell — Vervielfältigung für Textanalysen zulässig, aber Löschpflicht nach Forschungsabschluss.
3. Open-Access-Pflichten klären: BMBF- und DFG-Förderrichtlinien, Horizon Europe Data Management Plans — was muss öffentlich zugänglich gemacht werden?
4. Lizenzwahl bewerten: CC0 (Public Domain), CC BY (Attribution), ODbL für Datenbanken — Auswirkungen auf Datenbankherstellerrecht und Herstelleransprüche.
5. Spin-off und Hochschulrecht: Verwertungsrechte an Hochschulforschungsdaten — Arbeitgeber/Diensterfindung analog, §§ 42 f. ArbEG.
6. Datenpublikation und Repositorien: Rechtliche Anforderungen für Veröffentlichung auf Zenodo, PANGAEA, DRYAD — Lizenzkompatibilität.

## Rechtsrahmen

- § 60d UrhG: TDM-Schranke für wissenschaftliche Forschung — erlaubt Vervielfältigung, Löschpflicht nach Abschluss.
- § 87a UrhG: Wesentliche Investition in Beschaffung und Aufbereitung von Forschungsdaten als Herstellerrecht.
- DSM-RL Art. 3 (RL 2019/790): Wissenschaftliche TDM-Schranke — zwingend, keine Opt-out-Möglichkeit.
- § 87c UrhG: Erlaubte Handlungen — § 60d UrhG als gesetzliche Schranke auch gegenüber Datenbankherstellerrecht.
- §§ 42-43 ArbEG (analog): Verwertungsrechte an Hochschulerfindungen — Forschungsdaten sind keine Erfindungen, aber ähnliche Problematik.
- CC0 / CC BY 4.0: Lizenzmodelle für Forschungsdaten — Wirkung auf Datenbankherstellerrecht und Weiterverwendungsansprüche.

## Prüfraster

- Liegt eine wissenschaftliche Forschungsdatenbank mit wesentlicher Investition in Beschaffung und Aufbereitung vor?
- Dient die geplante TDM-Nutzung wissenschaftlicher Forschung im Sinne des § 60d UrhG — kommerzieller oder nicht-kommerzieller Zweck?
- Wurde ein Open-Access-Mandat durch Fördergeber verpflichtend gemacht — welche Lizenz ist vorzusehen?
- Schließt die gewählte CC-Lizenz das Datenbankherstellerrecht ein, oder bleibt es daneben bestehen?
- Wer ist Hersteller der Forschungsdatenbank — Hochschule, Forschungseinrichtung, einzelner Forscher?
- Ist das Spin-off-Unternehmen berechtigt, die Hochschuldatenbank zu nutzen — wurde ein Lizenzverhältnis begründet?
- Sind Datenlöschpflichten nach § 60d Abs. 1 S. 2 UrhG in den internen Prozessen berücksichtigt?

## Typische Fallstricke

- § 60d UrhG gilt nur für nicht-kommerzielle wissenschaftliche Forschung — Spin-offs mit kommerziellem Fokus fallen nicht darunter.
- CC0-Lizenz hebt das Datenbankherstellerrecht nicht auf, wenn der Lizenzgeber das nicht ausdrücklich erklärt (CC0 erfasst explizit auch sui-generis-Datenbankrechte — aber Prüfung im Einzelfall).
- Fördergeber-Anforderungen (BMBF, DFG) zu Open Access sind keine gesetzlichen Pflichten, aber Vertragspflichten — bei Verstoß droht Rückforderung.
- Forschungsdaten, die personenbezogene Informationen enthalten, dürfen unter CC0 nur mit DSGVO-Grundlage veröffentlicht werden.
- Hochschulen haben selten klare IP-Policies für Forschungsdatenbanken — interne Regelungslücken führen zu Streit bei Ausgründungen.

## Output

- Datenbankherstellerrecht-Gutachten für Forschungsdatenbank
- TDM-Schranken-Analyse nach § 60d UrhG
- Lizenzwahlhilfe (CC0 vs. CC BY vs. ODbL) für Forschungsdaten
- Open-Access-Compliance-Checkliste für Förderprojekte
- Spin-off-Lizenzvertrag-Vorlage für Hochschuldatenbanknutzung

## Quellen

- [§ 60d UrhG — dejure.org](https://dejure.org/gesetze/UrhG/60d.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [DSM-Richtlinie 2019/790 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [Art. 3 DSM-RL — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)

## 3. `db-022-kartendaten-geodaten-und-luftbilder`

**Fokus:** Datenbankrecht für Geodatenbanken, Kartendienste und Luftbilder: §§ 87a-87e UrhG für topografische Datenbanken, OpenStreetMap-ODbL-Lizenz, BKG-Nutzungsbedingungen, Verhältnis zu § 2 UrhG (Kartenwerke als Werke) und Open-Geodata-Anforderungen nach GeoZG. Bewertet Nutzung von Google Maps-, HERE- und OSM-Daten für kommerzielle Anwendungen.

# Kartendaten, Geodaten und Luftbilder — Datenbankrecht für Geodatenbanken

## Mandantenfall

- App-Entwickler will Kartendaten aus OpenStreetMap für eine kommerzielle Navigationsanwendung nutzen und fragt nach den ODbL-Pflichten.
- Unternehmen hat Luftbilder und Topografiedaten zu einer eigenen Geodatenbank kombiniert und möchte wissen, welche Schutzrechte bestehen.
- Behörde stellt fest, dass ein Privatunternehmen BKG-Geobasisdaten (Bundesamt für Kartographie) ohne Lizenz in seine Produkte integriert hat.

## Erste Schritte

1. Schutzrechtslage der Quelldatenbank bestimmen: OSM (ODbL), BKG-Daten (kommerzielle Lizenz oder Open-Data), proprietäre Anbieter (HERE, TomTom, Google)?
2. ODbL-Anforderungen prüfen: OpenStreetMap-Daten unter ODbL — Sharealike-Pflicht für abgeleitete Datenbanken, Namensnennung, Offenlegung von Änderungen.
3. Datenbankherstellerrecht für eigene Geodatenbank: Wesentliche Investition in Sammlung von Geodaten (Vermessung, Luftbilder, Georeferenzierung)?
4. Urheberrecht an Kartendarstellungen: § 2 UrhG — topografische Karten können Werke sein, wenn schöpferische Gestaltung (Symbolisierung, Generalisierung).
5. GeoZG und Open-Geodata prüfen: Geodatenzugangsgesetz, INSPIRE-RL — Pflicht zur Bereitstellung öffentlicher Geodaten.
6. Lizenzkompatibilität prüfen: Kombinierbarkeit von OSM (ODbL), BKG (dl-de/by) und proprietären Daten in einer Applikation.

## Rechtsrahmen

- § 87a UrhG: Geodatenbanken als Datenbankherstellerrecht — wesentliche Investition in systematische Erfassung und Darstellung von Geodaten.
- § 2 Abs. 1 Nr. 7 UrhG: Kartenwerke als Werke der bildenden Kunst, wenn schöpferische Gestaltung (Generalisierung, Symbolisierung) vorliegt.
- ODbL (Open Database Licence): Sharealike-Lizenz für OpenStreetMap — abgeleitete Datenbanken müssen ebenfalls unter ODbL veröffentlicht werden.
- GeoZG: Geodatenzugangsgesetz — Bereitstellungspflichten für öffentliche Geodaten; INSPIRE-Richtlinie 2007/2/EG.
- RL 96/9/EG Art. 7: Europäischer Datenbankschutz für Geodatenbanken mit wesentlicher Investition.
- § 5 UrhG: Amtliche Kartenwerke ohne Urheberrechtsschutz — aber Datenbankherstellerrecht kann daneben bestehen.

## Prüfraster

- Unter welcher Lizenz stehen die verwendeten Geodaten (OSM/ODbL, BKG, proprietär)?
- Löst die Nutzung die Sharealike-Pflicht der ODbL aus — wird eine abgeleitete Datenbank erstellt?
- Hat der Datenbankbetreiber eine wesentliche Investition in die Geodatenbeschaffung/-überprüfung getätigt?
- Sind die Kartendarstellungen als Werke nach § 2 UrhG schutzfähig (schöpferische Gestaltung)?
- Sind mehrere Quelldatenbanken mit unterschiedlichen Lizenzen kombiniert — wie ist die Lizenzkompatibilität?
- Besteht eine Pflicht nach GeoZG oder INSPIRE-RL, die Geodaten öffentlich bereitzustellen?
- Werden Luftbilder eingesetzt — wer hat die Investition in Befliegung und Georeferenzierung getätigt?

## Typische Fallstricke

- ODbL-Sharealike gilt für die Datenbank, nicht für einzelne Darstellungen (Map-Tiles) — Grenze zwischen Datenbank und Produit bestimmen.
- BKG-Daten sind häufig unter dl-de/by lizenziert und erfordern Namensnennung — wird oft vergessen.
- Proprietäre Geodaten (Google Maps, HERE) sind auch bei Nutzung über APIs datenbankschutzrechtlich relevant — API-Nutzungsbedingungen beachten.
- Amtliche topografische Karten sind nach § 5 UrhG urheberrechtsfrei, können aber als Datenbankwerk oder durch Herstellerrecht geschützt sein.
- Drohnen-Luftbilder ohne Genehmigung verletzen nicht nur Datenbankrecht, sondern auch Luftverkehrsrecht (LuftVO).

## Output

- Geodaten-Lizenz-Kompatibilitätsmatrix (OSM/BKG/proprietär)
- ODbL-Compliance-Checkliste für OSM-basierte Anwendungen
- Datenbankherstellerrecht-Gutachten für eigene Geodatenbank
- GeoZG-Bereitstellungspflichten-Übersicht für Behörden
- Luftbild-Rechteprofil (Urheberrecht + Datenbankschutz + Luftverkehrsrecht)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 2 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/2.html)
- [GeoZG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geozg/index.html)
- [INSPIRE-Richtlinie 2007/2/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32007L0002)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [§ 5 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/5.html)
