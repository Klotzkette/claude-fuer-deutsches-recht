---
name: wesentlicher-teil-qualitativ-quantitativ-bestimmen
description: "Bestimmt, ob eine Entnahme oder Weiterverwendung einen wesentlichen Teil einer Datenbank betrifft (§ 87b Abs. 1 UrhG / Art. 7 RL 96/9/EG). Analysiert quantitativen Umfang und qualitativen Wert des entnommenen Teils anhand EuGH C-203/02 und C-545/07. Erstellt Verletzungsmatrix und bewertet Beweislast für Hersteller und Verletzer im Datenbankrecht."
---

# Wesentlicher Teil einer Datenbank: qualitativ und quantitativ bestimmen

## Arbeitsbereich

Bestimmt, ob eine Entnahme oder Weiterverwendung einen wesentlichen Teil einer Datenbank betrifft (§ 87b Abs. 1 UrhG / Art. 7 RL 96/9/EG). Analysiert quantitativen Umfang und qualitativen Wert des entnommenen Teils anhand EuGH C-203/02 und C-545/07. Erstellt Verletzungsmatrix und bewertet Beweislast für Hersteller und Verletzer. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Betreiber einer Reisedatenbank entdeckt, dass ein Konkurrent täglich mehrere Tausend Datensätze automatisiert abruft und fragt, ob dies einen wesentlichen Teil darstellt.
- Beklagter im Datenbankrechtsstreit argumentiert, die entnommenen Datensätze seien nur ein geringer Prozentsatz der Gesamtdatenbank.
- Rechtsabteilung will vor Abmahnung prüfen, ob der eigene Datenabruf bei einem Drittanbieter die Wesentlichkeitsschwelle überschreitet.

## Erste Schritte

1. Quantitativen Anteil bestimmen: Wie viele Datensätze wurden entnommen im Verhältnis zum Gesamtbestand der Datenbank?
2. Qualitativen Wert bestimmen: Welchen wirtschaftlichen oder inhaltlichen Wert haben die entnommenen Daten für die Datenbank (z. B. Kerndatensätze, exklusive Einträge)?
3. EuGH-Maßstab anlegen: Qualitativer Maßstab misst Investitionsanteil der entnommenen Teile; quantitativer Maßstab misst Volumen (EuGH C-203/02 Rn. 70-71).
4. Technische Nachweise sichern: Server-Logs, Crawling-Protokolle, API-Aufrufhistorien, Datenbank-Diffs.
5. Zeitraum analysieren: Einmalige Entnahme oder systematisch wiederholte Entnahme unwesentlicher Teile (§ 87b Abs. 1 S. 2 UrhG)?
6. Beweiswürdigung vorbereiten: Sachverständigengutachten über Datenbankgröße und Entnahmevolumen einplanen.

## Rechtsrahmen

- § 87b Abs. 1 S. 1 UrhG: Entnahme oder Weiterverwendung wesentlicher Teile verboten ohne Erlaubnis des Herstellers.
- § 87b Abs. 1 S. 2 UrhG: Wiederholte und systematische Entnahme unwesentlicher Teile ist wesentlicher Entnahme gleichgestellt.
- Art. 7 Abs. 1 RL 96/9/EG: Schutz gegen Entnahme und/oder Weiterverwendung wesentlicher Teile nach Qualität oder Quantität.
- Art. 7 Abs. 5 RL 96/9/EG: Verbot der kumulativen Teilentnahmen als Umgehungstatbestand.
- EuGH C-203/02 (BHB/William Hill) Rn. 70-78: Definition des wesentlichen Teils nach quantitativem Volumen und qualitativem Investitionsanteil.
- EuGH C-545/07 (Apis/Lakorda) Rn. 62-76: Wesentlichkeit bei Rechtsdatenbankteilen und Abschnittsentnahmen.

## Prüfraster

- Wie groß ist die Gesamtdatenbank (Datensatzanzahl, Dateigröße, Investitionsvolumen)?
- Wie viele Datensätze/welchen Dateivolumenanteil hat der Verletzer entnommen (quantitativ)?
- Welcher Anteil der Gesamtinvestition steckt in den entnommenen Daten (qualitativ)?
- Handelt es sich um Kerndaten mit besonderem wirtschaftlichem Wert (Exklusivdaten, tagesaktuelle Inhalte)?
- Liegt eine einmalige oder eine systematisch wiederholte Entnahme vor?
- Summieren sich mehrere Teilentnahmen zeitlich zu einem wesentlichen Gesamtumfang?
- Lassen sich Entnahmezeitpunkt und -umfang durch technische Mittel lückenlos dokumentieren?

## Typische Fallstricke

- Ein Verletzer, der nur 10 % der Datensätze entnimmt, kann dennoch einen wesentlichen Teil treffen, wenn diese 10 % den Kernwert der Datenbank ausmachen.
- Tagesaktuelle oder exklusive Daten sind qualitativ besonders wertvoll — selbst geringe Mengen können Wesentlichkeitsgrenze überschreiten.
- Ohne serverseitige Protokollierung ist der Nachweis der Entnahmemenge im Prozess schwierig; frühzeitige Beweissicherung ist entscheidend.
- Die Kumulations-Regel (§ 87b Abs. 1 S. 2 UrhG) wird von Verletzern oft ignoriert; Verteidiger übersehen sie gleichermaßen.
- Gegendarstellung des Verletzers über eigene Datenquellen kann die Kausalität bestreiten — Provenienznachweis vorbereiten.

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-545/07 Apis/Lakorda — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-545/07)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 97 UrhG Schadensersatz — dejure.org](https://dejure.org/gesetze/UrhG/97.html)

