---
name: kartendaten-geodaten-und-luftbilder
description: "Datenbankrecht für Geodatenbanken, Kartendienste und Luftbilder: §§ 87a-87e UrhG für topografische Datenbanken, OpenStreetMap-ODbL-Lizenz, BKG-Nutzungsbedingungen, Verhältnis zu § 2 UrhG (Kartenwerke als Werke) und Open-Geodata-Anforderungen nach GeoZG. Bewertet Nutzung von Google Maps-, HERE- und OSM-Daten für kommerzielle Anwendungen im Datenbankrecht."
---

# Kartendaten, Geodaten und Luftbilder — Datenbankrecht für Geodatenbanken

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 2 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/2.html)
- [GeoZG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geozg/index.html)
- [INSPIRE-Richtlinie 2007/2/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32007L0002)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [§ 5 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/5.html)

