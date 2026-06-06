---
name: datenbankrecht-und-machine-learning-features
description: "Datenbankrecht für ML-Feature-Stores und Trainingsdatensätze: §§ 87a-87e UrhG für Feature-Stores als Datenbankherstellerrecht, TDM-Schranken (§§ 44b 60d UrhG) für ML-Training, Schutz aggregierter Feature-Vektoren und abgeleiteter Datensätze sowie DSGVO-Anforderungen bei personenbezogenen Feature-Daten. Erstellt Compliance-Konzept für MLOps-Teams im Datenbankrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Datenbankrecht und Machine-Learning-Features — Feature Stores und Trainingsdaten

## Arbeitsbereich

Datenbankrecht für ML-Feature-Stores und Trainingsdatensätze: §§ 87a-87e UrhG für Feature-Stores als Datenbankherstellerrecht, TDM-Schranken (§§ 44b 60d UrhG) für ML-Training, Schutz aggregierter Feature-Vektoren und abgeleiteter Datensätze sowie DSGVO-Anforderungen bei personenbezogenen Feature-Daten. Erstellt Compliance-Konzept für MLOps-Teams. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Data-Science-Team eines Unternehmens hat einen umfangreichen Feature Store aufgebaut und will ihn gegen externe Nutzung durch Wettbewerber schützen.
- KI-Unternehmen hat einen eigenen Feature-Datensatz aus öffentlichen Quellen aggregiert und fragt, welches Datenbankrecht es daran hat.
- Rechtsabteilung muss klären, ob die Feature-Extraktion aus einer geschützten Datenbank für ML-Training unter die TDM-Schranke fällt.

## Erste Schritte

1. Feature-Store als Datenbank bewerten: Ist der Feature Store eine systematisch geordnete Sammlung unabhängiger Elemente mit individuellem Zugriff (§ 87a Abs. 1 UrhG)?
2. Herstellerrecht prüfen: Wesentliche Investition in Beschaffung und Aufbereitung der Feature-Vektoren — Daten aus eigenen Messungen (Datenerzeugung = kein Schutz) oder aus externen Quellen aggregiert?
3. TDM-Schranke prüfen: Dient die Feature-Extraktion aus Fremddatenbanken einem TDM-Zweck (§ 44b UrhG)?
4. Abgeleitete Datensätze bewerten: Genießen aus einer geschützten Datenbank abgeleitete Feature-Datensätze eigenes Herstellerrecht oder sind sie Verletzungsprodukte?
5. DSGVO bei personenbezogenen Features: Enthält der Feature Store personenbezogene Daten (Nutzerverhalten, biometrische Daten) — Rechtsgrundlage?
6. Schutzstrategie für Feature Store: TDM-Opt-out, AGB-Schutz, technische Zugangskontrollen.

## Rechtsrahmen

- § 87a UrhG: Feature Store als Datenbankherstellerrecht — wenn wesentliche Investition in Beschaffung und Aufbereitung der Feature-Daten.
- EuGH C-203/02 (BHB/William Hill): Investition in Datenerzeugung (eigene ML-Modelltraining-Daten) schützt nicht — nur Investition in Datenbeschaffung.
- § 44b UrhG: TDM-Schranke für kommerzielle KI-Anwendungen — Opt-out des Quelldatenbank-Inhabers ausschlaggebend.
- § 60d UrhG: Wissenschaftliche TDM-Schranke — gilt auch für akademische ML-Forschung.
- DSGVO Art. 22: Automatisierte Entscheidungen und Profiling mit Feature-Daten — Betroffenenrechte bei automatisierten Systemen.
- § 87b UrhG: Verletzung durch Extraktion wesentlicher Feature-Teile aus einer Fremddatenbank.

## Prüfraster

- Ist der Feature Store als Datenbank gemäß § 87a Abs. 1 UrhG einzustufen (systematische Ordnung, individueller Zugriff)?
- Beruht die Investition in den Feature Store auf Datenbeschaffung/-überprüfung oder nur auf Datenmodellierung/-erzeugung?
- Dient die Feature-Extraktion aus einer Fremddatenbank einem TDM-Zweck — greift § 44b UrhG?
- Enthält der Feature Store personenbezogene Merkmale — ist DSGVO Art. 22 relevant (automatisierte Entscheidungen)?
- Haben abgeleitete Feature-Datensätze (Feature Engineering) eigenes Herstellerrecht oder sind sie Verletzungsprodukte der Quelldatenbank?
- Wurde ein TDM-Opt-out für die Quelldatenbank erteilt — schließt das die TDM-Schranke aus?
- Enthält der Feature Store Daten aus lizenzierten Quellen — erlaubt die Lizenz die Nutzung für ML-Training?

## Typische Fallstricke

- Feature Stores aus selbst erhobenen ML-Trainingsdaten sind keine durch Datenbankherstellerrecht geschützten Beschaffungsinvestitionen (BHB-Doktrin).
- Feature Engineering (Transformation bestehender Daten) kann nicht das ursprüngliche Herstellerrecht der Quelldatenbank auf den Feature Store übertragen.
- TDM-Schranke gilt für Vervielfältigung zum Zweck des Mining, nicht für kommerzielle Weiterverwertung abgeleiteter Modelle.
- DSGVO Art. 22 ist relevant, wenn Feature-basierte Entscheidungen vollständig automatisiert sind und rechtliche Wirkung haben.
- Personenbezogene Features erfordern DSGVO-Rechtsgrundlage — nicht immer durch berechtigtes Interesse abgedeckt.

## Output

- Feature-Store-Datenbankherstellerrecht-Prüfbogen
- TDM-Schranken-Analyse für ML-Feature-Extraktion
- DSGVO-Compliance-Check für personenbezogene ML-Feature-Daten
- Schutzstrategie für Feature Store (AGB, Opt-out, Zugangskontrolle)
- Lizenz-Compliance-Matrix für ML-Trainingsdaten-Quellen

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [§ 60d UrhG — dejure.org](https://dejure.org/gesetze/UrhG/60d.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [DSGVO Art. 22 — dejure.org](https://dejure.org/gesetze/DSGVO/22.html)
- [DSM-Richtlinie 2019/790 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)
