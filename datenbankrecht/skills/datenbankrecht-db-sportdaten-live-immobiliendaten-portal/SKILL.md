---
name: datenbankrecht-db-sportdaten-live-immobiliendaten-portal
description: "DB Sportdaten Live Immobiliendaten Portal: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Sportdaten Live Immobiliendaten Portal

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Sportdaten Live Immobiliendaten Portal** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-013-sportdaten-live-daten-fixtures-und-ergebnislisten` | Bewertet Datenbankschutz für Sportdaten nach EuGH C-203/02 (BHB/William Hill): Keine wesentliche Investition in Beschaffung von selbst erzeugten Spielplänen und Ergebnissen. Analysiert Schutz von Statistikdatenbanken durch §§ 87a-87e UrhG oder Wettbewerbsrecht, Lizenzmodelle für Live-Daten und Rechte von Sportligen und Veranstaltern. |
| `db-014-immobiliendaten-portal-und-lead-datenbank` | Datenbankrecht für Immobilienportale und Lead-Datenbanken: Prüft §§ 87a-87e UrhG für Exposé-Datenbanken, Schutz gegen systematisches Abgreifen von Angeboten, DSGVO-Anforderungen bei personenbezogenen Kontaktdaten und wettbewerbsrechtliche Aspekte (§§ 3 4 UWG). Erstellt Schutzstrategie für Portal-Betreiber und bewertet Lead-Datenbanklizenzen. |
| `db-015-produktdaten-pim-datenkatalog-hersteller` | Datenbankrecht für Produktdatenbanken und PIM-Systeme: Prüft §§ 87a-87e UrhG für Produktkataloge und Datenkataloge von Herstellern, Schutz gegen Übernahme durch Händler oder Wettbewerber, Lizenzmodelle für Produktdaten-Feeds und Verhältnis zu § 4 UrhG (Datenbankwerk). Analysiert Inhaberschaft bei arbeitsteilig erstellten Produktdatenbanken. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Sportdaten Live Immobiliendaten Portal**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-013-sportdaten-live-daten-fixtures-und-ergebnislisten`

**Fokus:** Bewertet Datenbankschutz für Sportdaten nach EuGH C-203/02 (BHB/William Hill): Keine wesentliche Investition in Beschaffung von selbst erzeugten Spielplänen und Ergebnissen. Analysiert Schutz von Statistikdatenbanken durch §§ 87a-87e UrhG oder Wettbewerbsrecht, Lizenzmodelle für Live-Daten und Rechte von Sportligen und Veranstaltern.

# Sportdaten, Live-Daten und Ergebnislisten — Datenbankrecht im Sport

## Mandantenfall

- Sportwettenanbieter fragt, ob er Spielpläne und Ergebnisse einer Fußballliga ohne Lizenz nutzen darf, nachdem die Liga Datenbankherstellerrecht geltend macht.
- Sportdaten-Aggregator verkauft Live-Statistikdaten und will wissen, ob der Datenbankschutz seine Datenbank gegen Wettbewerber absichert.
- Bundesliga-Klub lizenziert seine Spieler- und Spieldatenbank an einen App-Anbieter und muss den Vertragsumfang definieren.

## Erste Schritte

1. BHB/William Hill-Doktrin anwenden: Investition in Schaffung der Sportdaten (Spielbetrieb) vs. Investition in Beschaffung und Überprüfung bestehender Daten trennen.
2. Datenbankcharakter prüfen: Spielpläne, Ergebnislisten, Statistikdatenbanken — systematisch geordnete Sammlung mit individuellem Zugriff (§ 87a Abs. 1 UrhG)?
3. Investitionsnachweis für Statistikdatenbanken: Separate Datenerfassung, Überprüfung und Aufbereitung von Spielerstatistiken kann eigenständige Investition darstellen.
4. Wettbewerbsrechtliche Alternativen prüfen: Leistungsschutz über § 4 Nr. 3 UWG (Schmarotzen) oder Hausrecht des Veranstalters?
5. Lizenzmodell entwickeln: Welche Daten werden lizenziert, in welchem Umfang, zu welchen Konditionen für Echtzeitnutzung vs. historische Daten?
6. Vertragliche Absicherung: Nutzungsbedingungen für Daten-Feeds, API-Verträge, Sublizenzierungsverbote.

## Rechtsrahmen

- §§ 87a-87e UrhG: Datenbankherstellerrecht — Investition in Beschaffung, Überprüfung oder Darstellung erforderlich.
- EuGH C-203/02 (BHB/William Hill): Pferderenndaten werden vom Veranstalter erzeugt, nicht beschafft — kein Herstellerrecht.
- EuGH C-338/02 (Fixtures Marketing/Svenska AB): Spielpläne von Fußballligen sind eigene Daten — kein Datenbankherstellerrecht.
- § 4 Nr. 3 UWG: Nachahmungsschutz als wettbewerbsrechtliche Alternative bei kumulativen Voraussetzungen.
- § 87a Abs. 2 UrhG: Hersteller trägt Investitionsrisiko — Verein vs. Liga vs. Datendienstleister.
- Art. 7 RL 96/9/EG: Qualitative oder quantitative Wesentlichkeit der entnommenen Teile.

## Prüfraster

- Erzeugt der Anspruchsteller die Sportdaten selbst (Spielbetrieb), oder beschafft er sie aus externen Quellen?
- Liegt eine separate, wesentliche Investition in Beschaffung und Überprüfung von Spielstatistiken vor, die über die Erzeugung der Daten hinausgeht?
- Ist die Datenbank systematisch geordnet und bietet sie individuellen Datenzugriff?
- Handelt es sich um Live-Daten (hohe Aktualitätsinvestition) oder historische Daten (Archivierungsinvestition)?
- Besteht ein Wettbewerbsrechtlicher Schutz (§ 4 Nr. 3 UWG) als Auffangtatbestand?
- Ist das Lizenzmodell wettbewerbsrechtlich zulässig — kein Marktmissbrauch durch Exklusivlizenz?
- Welcher Anteil der Datenbank wird genutzt — wesentlicher Teil (§ 87b Abs. 1 UrhG)?

## Typische Fallstricke

- Ligabetreiber und Veranstalter irren häufig, wenn sie eigene Spielpläne und Ergebnisse automatisch als datenbankgeschützt betrachten — BHB/William Hill verneint dies klar.
- Separate Statistikdienste können eigenes Datenbankherstellerrecht erwerben, wenn sie Daten eigenständig beschaffen und aufbereiten.
- Wettbewerbsrechtlicher Leistungsschutz (§ 4 Nr. 3 UWG) ist subsidiär und setzt Nachahmung eines konkreten Produkts voraus.
- Exklusive Datenlizenzierungsverträge können kartellrechtliche Probleme aufwerfen, wenn ein Veranstalter marktbeherrschende Stellung hat.
- Historische Datenbankbestände genießen oft anderen Schutz als tagesaktuelle Live-Daten — Schutzdauer (§ 87d UrhG) prüfen.

## Output

- Datenbankschutz-Gutachten für Sportdaten (BHB/William Hill-Subsumtion)
- Investitionsnachweis-Schema für Statistikdatenbanken
- Lizenzvertrag-Vorlage für Live-Sportdaten-APIs
- Wettbewerbsrechtliche Alternativanalyse (§ 4 Nr. 3 UWG)
- Marktmissbrauchs-Risikocheck für exklusive Sportdatenlizenz

## Quellen

- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-338/02 Fixtures Marketing — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-338/02)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 4 UWG — dejure.org](https://dejure.org/gesetze/UWG/4.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 2. `db-014-immobiliendaten-portal-und-lead-datenbank`

**Fokus:** Datenbankrecht für Immobilienportale und Lead-Datenbanken: Prüft §§ 87a-87e UrhG für Exposé-Datenbanken, Schutz gegen systematisches Abgreifen von Angeboten, DSGVO-Anforderungen bei personenbezogenen Kontaktdaten und wettbewerbsrechtliche Aspekte (§§ 3 4 UWG). Erstellt Schutzstrategie für Portal-Betreiber und bewertet Lead-Datenbanklizenzen.

# Immobiliendaten, Portale und Lead-Datenbanken — Datenbankrecht

## Mandantenfall

- Immobilienportal-Betreiber stellt fest, dass ein Konkurrent täglich Exposés automatisiert abruft und in ein eigenes Portal übernimmt.
- Maklerunternehmen hat eine Lead-Datenbank mit Interessentendaten aufgebaut und will sie an einen Käufer verkaufen — welche Rechte können übertragen werden?
- PropTech-Startup will Immobilienangebote mehrerer Portale aggregieren und fragt nach dem rechtlichen Risiko gegenüber den Portal-Betreibern.

## Erste Schritte

1. Datenbankherstellerrecht für das Portal prüfen: Wesentliche Investition in Sammlung, Qualitätsprüfung und Darstellung der Exposés (§ 87a UrhG)?
2. Systematisches Abgreifen bewerten: Wesentliche Entnahme oder kumulierte Teilentnahmen (§ 87b UrhG), AGB-Verstoß, UWG-Tatbestand?
3. DSGVO-Prüfung für Lead-Datenbank: Enthält die Datenbank personenbezogene Kontaktdaten? Rechtsgrundlage nach Art. 6 DSGVO?
4. Datenbankübertragung bei Lead-Datenbank: Welche Rechte (Herstellerrecht, Urheberrecht an Inseraten) können verkauft werden — und welche DSGVO-Pflichten gehen über?
5. Aggregator-Risiko bewerten: EuGH Innoweb/Wegener — Weiterverwendung durch Meta-Suchmaschine ist verboten (C-202/12).
6. Schutzmaßnahmen empfehlen: robots.txt, AGB, technische Sperren, Honey-Pot-Einträge als Beweisinstrument.

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht für Immobilienportale — wesentliche Investition in Sammlung und Darstellung von Exposés.
- § 87b UrhG: Verbot der Entnahme wesentlicher Teile; Kumulationstatbestand bei wiederholtem Abgreifen.
- EuGH C-202/12 (Innoweb/Wegener): Meta-Suchmaschine, die eine Datenbank in Echtzeit durchsucht, verwendet wesentliche Teile weiter.
- Art. 6 Abs. 1 lit. f DSGVO: Berechtigtes Interesse als Rechtsgrundlage für Lead-Datenbanken — Interessenabwägung erforderlich.
- § 4 Nr. 4 UWG: Gezielte Behinderung durch systematisches Abgreifen von Wettbewerberdaten.
- § 307 BGB: AGB-Scraping-Verbote — wirksam, wenn transparent und verhältnismäßig formuliert.

## Prüfraster

- Hat das Portal eine wesentliche Investition in Beschaffung (Maklerinserate einsammeln), Überprüfung (Qualitätskontrolle) und Darstellung (Suchmasken, Filterfunktionen) getätigt?
- Sind die abgegriffenen Exposés wesentliche Teile der Datenbank — qualitativ (Exklusivinserate) oder quantitativ (hoher Anteil)?
- Handelt der Aggregator systematisch und regelmäßig (Kumulationstatbestand § 87b Abs. 1 S. 2 UrhG)?
- Enthält die Lead-Datenbank personenbezogene Daten, und auf welcher DSGVO-Rechtsgrundlage wurden sie erhoben?
- Liegt ein wirksames AGB-Verbot für automatisiertes Abrufen vor?
- Wurde Honey-Pot-Datensätze oder Wasserzeichen in den Inseraten als Beweisinstrument eingesetzt?
- Besteht bei Lead-Datenbankübertragung eine DSGVO-konforme Rechtsgrundlage für die Weitergabe?

## Typische Fallstricke

- Portale, die Inserate lediglich von Maklern entgegennehmen und veröffentlichen, investieren primär in Darstellung — nicht in Beschaffung; Herstellerrecht kann dennoch begründet sein.
- Einzelne Maklerinserate können eigenen Urheberrechtsschutz der Texte/Fotos genießen — Portalrecht und Inseratrecht trennen.
- Lead-Datenbankverkauf ohne DSGVO-Grundlage ist Datenschutzverstoß — Bußgeld bis 4 % des Jahresumsatzes (Art. 83 DSGVO).
- Honey-Pot-Einträge sind effektives Beweismittel, müssen aber rechtssicher eingesetzt werden (keine Täuschung Dritter).
- Aggregatoren können argumentieren, sie nutzten nur öffentlich zugängliche Daten — Innoweb/Wegener-Entscheidung entgegnet dem.

## Output

- Datenbankschutzanalyse für das Immobilienportal (§ 87a UrhG-Gutachten)
- Schutzmaßnahmen-Empfehlung (AGB, robots.txt, Honey-Pots)
- Abmahnschreiben gegen Aggregator (§ 87b UrhG + § 4 Nr. 4 UWG)
- DSGVO-Compliance-Check für Lead-Datenbank
- Datenbankübertragungsvertrag-Checkliste (M&A / Lead-Datenkauf)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 4 UWG — dejure.org](https://dejure.org/gesetze/UWG/4.html)
- [Art. 83 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/83.html)

## 3. `db-015-produktdaten-pim-datenkatalog-hersteller`

**Fokus:** Datenbankrecht für Produktdatenbanken und PIM-Systeme: Prüft §§ 87a-87e UrhG für Produktkataloge und Datenkataloge von Herstellern, Schutz gegen Übernahme durch Händler oder Wettbewerber, Lizenzmodelle für Produktdaten-Feeds und Verhältnis zu § 4 UrhG (Datenbankwerk). Analysiert Inhaberschaft bei arbeitsteilig erstellten Produktdatenbanken.

# Produktdaten, PIM-Systeme und Datenkataloge — Datenbankrecht für Hersteller

## Mandantenfall

- Hersteller stellt fest, dass sein vollständiger Produktkatalog von einem Großhändler in dessen eigenes System übertragen wurde, ohne Lizenz und ohne Namensnennung.
- E-Commerce-Dienstleister hat ein PIM-System mit Produktdaten vieler Hersteller aufgebaut und fragt, wer Datenbankinhaber ist — er oder die Hersteller?
- Unternehmen will einen Produktdaten-Feed an Händler lizenzieren und benötigt eine Klausel, die Weiterverwendung in Preisvergleichsportalen ausschließt.

## Erste Schritte

1. Herstellereigenschaft klären: Wer hat die wesentliche Investition in die Produktdatenbank getätigt — der Hersteller, der Dienstleister oder das Handelsunternehmen?
2. Datenbankschutz für Produktkatalog prüfen: Wesentliche Investition in Beschaffung (Produktfotos, Spezifikationen erfassen), Überprüfung (Qualitätskontrolle, Normkonformität) und Darstellung (PIM-Struktur, Kategorisierung)?
3. Verletzungsanalyse: Systematische Übernahme des Produktkatalogs — wesentlicher Teil (§ 87b UrhG)?
4. Inhaberschaft bei arbeitsteiliger Erstellung: Wer hat welchen Teil der Investition getragen? Vertragliche Regelung?
5. Lizenzvertrag für Produktdaten-Feed entwickeln: Nutzungsumfang, Weiterverwendungsverbote, Audit-Recht, Preisvergleichsportal-Ausschluss.
6. Urheberrecht an Produktfotografien und Texten prüfen: Separate Schutzrechte der Einzelelemente neben Datenbankschutz.

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht für Produktdatenbanken — wesentliche Investition in systematisch geordnete Produktdaten.
- § 87b UrhG: Verbot der Entnahme und Weiterverwendung wesentlicher Teile des Produktkatalogs.
- § 4 Abs. 2 UrhG: Datenbankwerk, wenn Auswahl oder Anordnung der Produkte schöpferisch ist (z. B. redaktionell kuratierter Katalog).
- § 31 UrhG: Einräumung von Nutzungsrechten an Produktdaten-Feeds — Spezifizierungspflicht.
- § 307 BGB: AGB-Wirksamkeit von Weiterverwendungsverboten in Produktdaten-Lizenzen.
- Art. 7 RL 96/9/EG: Europarechtliche Grundlage; gilt auch für Produktdatenbanken mit wesentlicher Investition.

## Prüfraster

- Wer hat die wesentliche Investition in den Produktkatalog getätigt — Hersteller, Dienstleister oder Händler?
- Sind Produktdaten (Spezifikationen, Fotos, Beschreibungen) systematisch geordnet und einzeln zugänglich?
- Übersteigt der Erstellungsaufwand des Katalogs die bloße Datenerzeugung (Produktionsdaten) und betrifft Beschaffung/Überprüfung?
- Stellt die Übernahme des Produktkatalogs eine Entnahme wesentlicher Teile dar?
- Sind Urheberrechte an Produktfotos und -texten separat zu klären (§ 2 UrhG, § 72 UrhG für Lichtbilder)?
- Enthält der Lizenzvertrag klare Verbote für Weiterverwendung in Preisvergleichsportalen?
- Ist eine arbeitsteilig entstandene Investitionsstruktur vertraglich klar auf Hersteller oder Dienstleister zugewiesen?

## Typische Fallstricke

- Produktspezifikationen, die der Hersteller selbst erstellt hat, sind erzeugte Daten — das Herstellerrecht entsteht erst durch separate Datenbankpflege.
- Produktdaten-Feeds ohne klare Lizenzstruktur gelten oft als implizit freigegeben für die Händlernutzung — explizite Einschränkungen sind unerlässlich.
- Übertragung der Datenbankrechte an Dienstleister ohne Rückübertragungsklausel führt dazu, dass der Hersteller keinen eigenen Schutzanspruch mehr hat.
- AGB-Weiterverwendungsverbote ohne hinreichende Bestimmtheit sind nach § 307 BGB unwirksam.
- Produktdaten aus Drittquellen (z. B. GS1-Datenbanken) können eigene Schutzrechte Dritter tragen — Lizenzprüfung nötig.

## Output

- Datenbankherstellerrecht-Gutachten für Produktkatalog
- Produktdaten-Lizenzvertrag mit Weiterverwendungsverbot-Klausel
- Inhaberschafts-Matrix für arbeitsteilig erstellte PIM-Datenbanken
- Abmahnschreiben bei unerlaubter Katalogübernahme
- Feed-Lizenz-AGB-Vorlage mit Preisvergleichsportal-Ausschluss

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 4 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/4.html)
- [§ 31 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/31.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
