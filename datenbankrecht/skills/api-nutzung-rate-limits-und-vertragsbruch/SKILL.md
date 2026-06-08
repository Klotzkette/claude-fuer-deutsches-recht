---
name: api-nutzung-rate-limits-und-vertragsbruch
description: "Prüft die rechtliche Bewertung von API-Nutzung im Datenbankkontext: Vertragsbruch bei Überschreitung von Rate-Limits oder Nutzungsbedingungen, Verhältnis zu §§ 87a-87e UrhG, Schadensersatz bei unerlaubter Massenabfrage sowie Gestaltung wirksamer API-Nutzungsbedingungen. Bewertet Kündigungsrecht und Sperrbefugnis des Datenbankbetreibers im Datenbankrecht."
---

# API-Nutzung, Rate-Limits und Vertragsbruch im Datenbankrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- SaaS-Anbieter stellt fest, dass ein Geschäftskunde über seine API weit mehr Abfragen tätigt als vertraglich erlaubt, und will Schadenersatz und Kündigung prüfen.
- Startup hat eine API-Schnittstelle zu einer Fremddatenbank genutzt und überschreitet unbewusst die Rate-Limits — die Gegenseite droht mit Abmahnung.
- Unternehmen entwirft neue API-Nutzungsbedingungen und will sicherstellen, dass diese das Datenbankherstellerrecht wirksam ergänzen.

## Erste Schritte

1. Vertragliche Grundlage klären: API-Nutzungsvertrag, AGB, Developer-Agreement — welche Rate-Limits und Nutzungszwecke sind vereinbart?
2. Vertragsbruch bewerten: Überschreitung der Abfragelimits, unerlaubte Weiterverwendung, Verstoß gegen Zweckbindung — § 280 BGB, § 241 Abs. 2 BGB.
3. Urheberrechtliche Parallelprüfung: Erfüllt die Abfrageintensität den Tatbestand der wesentlichen Entnahme nach § 87b UrhG unabhängig vom Vertrag?
4. Kündigung und Sperre prüfen: Außerordentliche Kündigung (§ 314 BGB) bei schwerwiegendem Vertragsbruch; technische Sperre als berechtigte Maßnahme.
5. Schadensersatz berechnen: Überschussabfragen nach Lizenzanalogie bewerten; Nutzungsausfallschaden des Betreibers.
6. AGB-Wirksamkeit prüfen: Rate-Limit-Klauseln nach § 307 BGB; transparente Formulierung und klar definierte Folgen.

## Rechtsrahmen

- § 280 Abs. 1 BGB: Schadensersatz bei Pflichtverletzung aus dem Schuldverhältnis.
- § 314 BGB: Kündigung von Dauerschuldverhältnissen aus wichtigem Grund bei schwerwiegendem Vertragsbruch.
- § 307 BGB: AGB-Kontrolle — Rate-Limit-Klauseln müssen klar, verständlich und nicht unangemessen benachteiligend sein.
- § 87b UrhG: Urheberrechtlicher Anspruch neben dem Vertragsanspruch bei wesentlicher Entnahme.
- § 97 UrhG: Unterlassung und Schadensersatz bei Urheberrechtsverletzung — Lizenzanalogie als Berechnungsmethode.
- § 97a UrhG: Abmahnung als Voraussetzung für Erstattung von Rechtsanwaltsgebühren.

## Prüfraster

- Liegt ein wirksamer API-Nutzungsvertrag vor, und was regelt er zu Abfragevolumen, Zweck und Weiterverwendung?
- Überschreiten die tatsächlichen Abfragen die vertraglich vereinbarten Rate-Limits messbar?
- Sind die Rate-Limits technisch nachweisbar (Server-Logs, API-Gateway-Protokolle)?
- Erfüllen die Abfragen unabhängig vom Vertrag den urheberrechtlichen Verletzungstatbestand (§ 87b UrhG)?
- Hat der Betreiber vor der Kündigung abgemahnt oder eine Frist zur Abhilfe gesetzt (§ 314 Abs. 2 BGB)?
- Sind Rate-Limit-Klauseln in AGB nach § 307 BGB wirksam — sind Schwellenwerte und Rechtsfolgen transparent?
- Kann der Schaden nach Lizenzanalogie (übliche API-Lizenzgebühr) berechnet werden?

## Typische Fallstricke

- Rate-Limits ohne klare Rechtsfolge in den AGB lassen offen, ob Überschreitung Vertragsbruch oder nur technische Einschränkung ist.
- Urheberrechtliche Ansprüche laufen auch ohne Vertragsverletzung — der Betreiber kann beide Ansprüche nebeneinander geltend machen.
- Kündigung ohne vorherige Abmahnung bei erstmaligem Verstoß ist oft unwirksam (§ 314 Abs. 2 BGB).
- Technische Sperren ohne vorherige Abmahnung können ihrerseits Vertragsbruch des Betreibers darstellen (§ 280 BGB).
- Entwickler-Teams überschreiten Rate-Limits oft versehentlich — culpa levis reicht aber für vertraglichen Schadensersatzanspruch.

## Output

- Vertragsbruchanalyse mit Anspruchsübersicht (§ 280 BGB / § 97 UrhG)
- Rate-Limit-Klausel-Vorlage für wirksame AGB-Gestaltung
- Abmahnschreiben bei API-Missbrauch
- Schadensberechnung nach Lizenzanalogie
- Kündigung aus wichtigem Grund — Musterformulierung (§ 314 BGB)

## Quellen

- [§ 280 BGB — dejure.org](https://dejure.org/gesetze/BGB/280.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 87a UrhG
- § 87b UrhG
- § 87a-87e UrhG
- § 44b UrhG
- § 4 UrhG
- § 60d UrhG
- § 97 UrhG
- § 87c UrhG
- § 87d UrhG
- § 97a UrhG
- § 202a StGB
- § 5 UrhG

### Leitentscheidungen

- EuGH C-203/02
- EuGH C-202/12
- EuGH C-545/07
- EuGH C-338/02
- EuGH C-170/12

