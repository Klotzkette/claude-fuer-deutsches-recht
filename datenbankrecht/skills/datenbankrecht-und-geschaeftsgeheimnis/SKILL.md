---
name: datenbankrecht-und-geschaeftsgeheimnis
description: "Analysiert das Verhältnis zwischen Datenbankherstellerrecht (§§ 87a-87e UrhG) und Geschäftsgeheimnisschutz nach GeschGehG / EU-RL 2016/943. Prüft kumulative Schutzfähigkeit von Datenbanken als Geschäftsgeheimnisse, angemessene Schutzmaßnahmen (§ 2 Nr. 1 GeschGehG) und Handlungsoptionen bei unbefugter Offenlegung oder Nutzung im Datenbankrecht."
---

# Datenbankrecht und Geschäftsgeheimnisschutz — Kumulative Schutzstrategie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Pharmaunternehmen hat eine Wirkstoffdatenbank aufgebaut, die als Betriebsgeheimnis behandelt wird — jetzt hat ein ausgeschiedener Mitarbeiter Teile weitergegeben.
- Technologieunternehmen fragt, ob seine proprietäre Kundendatenbank als Geschäftsgeheimnis einstufbar ist und welche Schutzmaßnahmen erforderlich sind.
- Startup-Investor will vor Beteiligung prüfen, ob die Datenbank des Zielunternehmens urheberrechtlich und als Geschäftsgeheimnis ausreichend geschützt ist.

## Erste Schritte

1. Datenbankschutz nach UrhG prüfen: §§ 87a ff. (Herstellerrecht) und § 4 Abs. 2 UrhG (Datenbankwerk) — welcher Tatbestand ist erfüllt?
2. Geschäftsgeheimniseigenschaft prüfen: § 2 Nr. 1 GeschGehG — Information nicht allgemein bekannt, wirtschaftlicher Wert, angemessene Geheimhaltungsmaßnahmen.
3. Geheimhaltungsmaßnahmen dokumentieren: Zugangsbeschränkungen, NDA-Klauseln, technische Sicherung, Zugriffsprotokollierung.
4. Verletzungshandlung bestimmen: § 4 GeschGehG — rechtswidrige Erlangung, Nutzung oder Offenlegung; welche Handlung liegt vor?
5. Ansprüche kombinieren: Unterlassung, Schadensersatz, Auskunft und Vernichtung nach GeschGehG §§ 6-8 neben UrhG-Ansprüchen.
6. Beweissicherung: Digitale Forensik, Zugriffslogdaten, Kommunikationsnachweise sichern.

## Rechtsrahmen

- § 2 Nr. 1 GeschGehG: Geschäftsgeheimnis — nicht allgemein bekannt/zugänglich, wirtschaftlicher Wert, angemessene Geheimhaltungsmaßnahmen.
- § 4 GeschGehG: Verbotene Handlungen — rechtswidrige Erlangung, Nutzung oder Offenlegung.
- §§ 6-8 GeschGehG: Unterlassung, Schadensersatz, Auskunft, Vernichtung als Rechtsfolgen.
- §§ 87a-87e UrhG: Datenbankherstellerrecht — kumulativer Schutz neben Geschäftsgeheimnisrecht möglich.
- EU-RL 2016/943: Europäische Grundlage des Geschäftsgeheimnisschutzes — Trade Secrets Directive.
- § 17 UWG a.F. (heute GeschGehG): Verrat von Geschäftsgeheimnissen — Übergangsrecht beachten.

## Prüfraster

- Ist die Datenbankstruktur oder ihr Inhalt nicht allgemein bekannt und wirtschaftlich wertvoll?
- Wurden angemessene Geheimhaltungsmaßnahmen ergriffen (NDA, Zugangsbeschränkungen, Verschlüsselung)?
- Ist die Verletzungshandlung einer der Kategorien des § 4 GeschGehG zuzuordnen?
- Sind Datenbankschutz (§§ 87a ff. UrhG) und Geschäftsgeheimnisschutz (GeschGehG) kumulativ anwendbar?
- Gibt es Beweise für die Verletzungshandlung (Logs, E-Mails, exportierte Dateien)?
- Wurde das Geheimnis durch einen ehemaligen Mitarbeiter oder externen Dienstleister verletzt — welche Vertragsgrundlage besteht?
- Besteht Pflicht zur Abmahnung vor Klageerhebung oder gerichtlichem Eilantrag?

## Typische Fallstricke

- Fehlende schriftliche Geheimhaltungsmaßnahmen (keine NDA, keine Zugriffskontrollen) können den GeschGehG-Schutz vollständig entfallen lassen.
- Daten, die in einer öffentlichen Datenbank erscheinen, verlieren den Geheimnischarakter — auch wenn die eigene Datenbank weiterhin geschützt sein kann.
- GeschGehG und UrhG haben unterschiedliche Verjährungsfristen — Ansprüche dürfen nicht verwechselt werden.
- Reverse Engineering ist nach § 3 Abs. 1 Nr. 2 GeschGehG grundsätzlich erlaubt — der Datenbankschutz kann hier stärker greifen.
- Beweislastverteilung im GeschGehG-Prozess ist komplex; vorprozessuale Dokumentation der Geheimhaltungsmaßnahmen ist entscheidend.

## Quellen

- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [EU-RL 2016/943 Trade Secrets — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943)
- [§ 4 GeschGehG — dejure.org](https://dejure.org/gesetze/GeschGehG/4.html)
- [§§ 6-8 GeschGehG — dejure.org](https://dejure.org/gesetze/GeschGehG/6.html)
- [§ 307 BGB AGB-Kontrolle — dejure.org](https://dejure.org/gesetze/BGB/307.html)

