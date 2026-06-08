---
name: datenbankrecht-bei-finanzmarktdaten
description: "Datenbankrecht für Finanzmarktdaten: §§ 87a-87e UrhG für Börsen- und Kursdatenbanken, EuGH C-203/02 (BHB/William Hill) und Börsen als Datenbankherstellerinnen (Investition in Kursfeststellung vs. Datenbeschaffung), MiFID-II-Datentransparenzpflichten, Lizenzmodelle für Marktdaten-Feeds und DSGVO bei personenbezogenen Transaktionsdaten im Datenbankrecht."
---

# Datenbankrecht bei Finanzmarktdaten — Börsen, Kurse und Marktdaten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- FinTech-Unternehmen will Echtzeit-Kursdaten einer Börse ohne Lizenz in seine App integrieren und fragt, ob das datenbankherstellerrechtlich zulässig ist.
- Börse stellt fest, dass ein Datenaggregator ihre historischen Kursdatenbank vollständig kopiert und verkauft — welche Ansprüche bestehen?
- Investmentbank möchte Marktdaten-Feeds von Bloomberg und Reuters lizenzieren und muss den rechtlichen Rahmen (Datenbankrecht, MiFID II) verstehen.

## Erste Schritte

1. BHB/William Hill-Einwand für Börsen prüfen: Erzeugt die Börse die Kurse selbst (Handelsgeschäfte) oder beschafft sie Daten? Wenn Kurse durch eigenen Handelsbetrieb entstehen — Einschränkung des Herstellerrechts nach EuGH-Doktrin?
2. Separate Datenbankpflege-Investition: Historische Kursdatenbank, Tick-Datensammlung, Indexberechnungen — separate Investition in Beschaffung und Aufbereitung?
3. MiFID-II-Transparenzpflichten prüfen: Art. 64-65 MiFID II — Nachhandels-Transparenz, Pflicht zur Marktdatenbereitstellung zu angemessenen Konditionen.
4. Lizenzmodell für Marktdaten-Feeds: Echtzeit vs. verzögert, Terminal-Lizenzen, Redistributionsverbote, Snapshots — differenzierte Lizenzstruktur.
5. Aggregator-Verletzung bewerten: Wesentliche Entnahme historischer Kursdaten (§ 87b UrhG) — Kumulation bei täglichem Abruf?
6. DSGVO bei Transaktionsdaten: Transaktionsdaten von identifizierbaren Personen (Privatanleger) — Rechtsgrundlage und Zweckbindung.

## Rechtsrahmen

- § 87a UrhG: Börsen-Datenbankherstellerrecht — Investition in Kursdaten-Sammlung, historische Tick-Daten, Indexberechnungen.
- EuGH C-203/02 (BHB/William Hill): Selbst erzeugte Daten (eigene Handelspreise) schützt kein Herstellerrecht — separate Datenbankpflege-Investition erforderlich.
- § 87b UrhG: Verbot der wesentlichen Entnahme aus Börsendatenbanken ohne Lizenz.
- MiFID II Art. 65 (RL 2014/65/EU): Pflicht zur Veröffentlichung von Handelsdaten zu angemessenen kommerziellen Bedingungen.
- DSGVO Art. 4 Nr. 1: Transaktionsdaten von identifizierbaren Personen sind personenbezogene Daten.
- RL 96/9/EG Art. 7: Europäischer Schutz für Börsendatenbanken mit wesentlicher Investition.

## Prüfraster

- Beruht das Herstellerrecht der Börse auf Investition in Datenbeschaffung/-überprüfung oder nur in eigene Kursfeststellung (BHB-Einwand)?
- Gibt es eine separate wesentliche Investition in die historische Kursdatenbank (Tick-Daten, Zeitreihen)?
- Entsteht der Verletzungstatbestand durch Echtzeit-Abruf (Innoweb-Test) oder durch historische Batch-Entnahme?
- Erfüllt das Lizenzmodell die MiFID-II-Anforderungen (angemessene, nichtdiskriminierende Preise)?
- Sind FinTech-App-Nutzer Privatanleger — liegen personenbezogene Transaktionsdaten vor?
- Ist der Datenaggregator vertraglich gebunden (Redistributionsverbot) oder agiert er außerhalb jeder Lizenz?
- Welche Lizenzgebühr gilt als Lizenzanalogie für unerlaubten historischen Kursdaten-Zugriff?

## Typische Fallstricke

- Börsen irren häufig, wenn sie behaupten, ihre eigenen Handelsdaten seien automatisch datenbankherstellerrechtlich geschützt — BHB/William Hill schränkt das ein.
- MiFID-II-Pflicht zur fairen Preisgestaltung für Marktdaten kann überhöhte Lizenzgebühren einschränken — kartellrechtliche Parallele.
- Historische Kursdatenbanken können eigenes Herstellerrecht haben, selbst wenn Echtzeit-Preise nicht geschützt sind.
- Kumulationsregel (§ 87b Abs. 1 S. 2 UrhG) trifft FinTechs, die täglich kleine Datenpakete abrufen.
- DSGVO-Transaktionsdaten dürfen nicht unbeschränkt für Analytics-Zwecke verarbeitet werden — Zweckbindung beachten.

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [MiFID-II-Richtlinie 2014/65/EU — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014L0065)
- [DSGVO Art. 4 — dejure.org](https://dejure.org/gesetze/DSGVO/4.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

