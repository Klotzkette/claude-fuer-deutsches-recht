---
name: patentfamilien-analyse
description: "Patentfamilien-Analyse ueber INPADOC und Espacenet-Family-View. Sammelt zu einem konkreten Treffer alle Familienmitglieder weltweit DE EP US JP CN KR WO und sonstige Aemter mit gleichem Prioritaetstag. Liefert eine Familientabelle pro Familienmitglied mit Veroeffentlichungsnummer Anmeldetag Prioritaetstag Status Klassifikation Validierungsstaaten Anmelder Link. Erlaeutert den Unterschied zwischen INPADOC-Familie (gleicher Prioritaetstag) und Domestic Patent Family (gleicher Anmelder und enge technische Verwandtschaft). Markiert wann die Familie in welchem Staat noch geschuetzt ist und wann ein Mitglied bereits abgelaufen ist. Disclaimer Familiendaten koennen luekenhaft sein nicht alle Aemter melden vollstaendig."
---

# patentfamilien-analyse

## Zweck

Ein einzelnes Patentdokument steht selten allein — es ist Teil einer **Patentfamilie**, die aus der gleichen Erstanmeldung hervorgegangen ist. Für die FTO-Recherche, die Stand-der-Technik-Recherche und die Einspruchsstrategie ist es entscheidend, die ganze Familie zu kennen.

## Konzepte

### INPADOC-Familie

Definition über den **Prioritätstag**. Alle Anmeldungen weltweit, die direkt oder indirekt auf dieselbe Erstanmeldung priorisieren (Pariser Verbandsübereinkunft, Art. 4 PVÜ — 12 Monate Prioritätsfrist).

- Eine Erstanmeldung in DE am 15.03.2018.
- Innerhalb 12 Monaten Nachanmeldungen in EP, US, JP, CN, KR mit Priorität DE 15.03.2018.
- 18 Monate nach Prioritätstag (15.09.2019): Veröffentlichung der Anmeldungen.
- Alle gehören zur **INPADOC patent family** mit Stamm-Prioritätstag 15.03.2018.

INPADOC wird vom EPA gepflegt und ist über Espacenet und EPO Open Data zugänglich.

### Domestic Patent Family

Definition über **gleichen Anmelder + technische Verwandtschaft**. Continuation-in-Part, Teilanmeldung (§ 39 PatG / Art. 76 EPÜ), Zusatzanmeldung. Die Domestic Family ist enger als die INPADOC-Familie und kann anderen Anmeldetag haben.

### Simple Family

Definition über **gleichen Satz aller Prioritätsdaten**. Engere Definition als INPADOC, in Espacenet als „Simple family" gekennzeichnet.

## Ablauf

### Schritt 1: Treffer zur Recherche-Bewertung übernehmen

Aus den Recherche-Treffern (Output von `agentische-datenbank-recherche`) den Treffer auswählen, dessen Familie analysiert werden soll. Typisch: jeder X-Treffer und jeder kritische Y-Treffer aus `stand-der-technik-recherche` und jeder Rot-/Gelb-Treffer aus `freedom-to-operate-recherche`.

### Schritt 2: Espacenet Family View öffnen

In Espacenet zum Treffer navigieren, „Family list" oder „INPADOC patent family" auswählen.

URL-Schema:
```
https://worldwide.espacenet.com/patent/search/family/<family-id>/publication/<publication-no>?q=<publication-no>
```

Die Family-ID ist eine zentrale Kennzahl — sie identifiziert die INPADOC-Familie eindeutig.

### Schritt 3: Familientabelle erstellen

Pro Familienmitglied:

| Veröff.-Nr. | Anmelder | Anmeldetag | Prio | Status | Klasse | Validierung | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DE 10 2018 005 432 A1 | Siemens AG | 15.03.2018 | DE 15.03.2018 | zurückgenommen | H02J 3/14 | — | DPMAregister-Link |
| EP 3 456 789 A1 | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt | H02J 3/14 | DE FR GB | EPO-Register-Link |
| EP 3 456 789 B1 | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt 12.09.2021 | H02J 3/14 | DE FR GB IT NL | EPO-Register-Link |
| US 10,876,543 B2 | Siemens AG | 15.03.2019 | DE 15.03.2018 | erteilt 05.10.2020 | H02J 3/14 | US | USPTO-Link |
| WO 2019/127345 A1 | Siemens AG | 14.03.2019 | DE 15.03.2018 | nationale Phasen | H02J 3/14 | — | PATENTSCOPE-Link |
| CN 110123456 A | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt CN | H02J 3/14 | CN | Espacenet-CN-Link |
| JP 6789012 B2 | Siemens AG | 14.03.2019 | DE 15.03.2018 | erteilt JP | H02J 3/14 | JP | Espacenet-JP-Link |

### Schritt 4: Rechtsstand markieren

Pro Familienmitglied: ist es noch in Kraft? Wann läuft die Schutzdauer ab (= Anmeldetag + 20 Jahre)? Sind die Jahresgebühren bezahlt? — über `rechtsstand-pruefen`.

### Schritt 5: Auswertung

- **In welchen Staaten** ist die Erfindung in Kraft? Daraus ergeben sich die Territorien, in denen die Familie für FTO relevant ist.
- **In welchen Staaten** ist die Familie nie eingetreten? Dort bestehen für die Mandantin keine Verbietungsrechte.
- **In welchen Staaten** ist die Familie abgelaufen / zurückgenommen / nicht erteilt? Dort frei.
- **Continuation- / Teilanmeldungen** — sind weitere Anmeldungen aus derselben Stammanmeldung anhängig? Diese können bei Erteilung **künftige** Verbietungsrechte begründen.

### Schritt 6: Output an aufrufendes Skill

Familientabelle als strukturiertes YAML/JSON an `freedom-to-operate-recherche` oder `recherchebericht-erstellen`.

## Hinweise

- **Datenlücken.** Nicht alle Ämter melden vollständig an INPADOC. Bei JP-, CN-, KR-Patenten kann die Familie unvollständig erfasst sein. Bei kritischen Mandaten: amtliche Direktrecherche im Zielland.
- **Späte Nachanmeldungen** außerhalb der 12-Monats-Prioritätsfrist sind keine echte Familie, sondern eigenständige Anmeldungen mit eigenem Stand der Technik.
- **EP-Patente mit Einheitlichem Patent (UP).** Seit Juni 2023 gibt es das Einheitliche Patent. Erfasst alle Teilnehmer-Staaten als ein einziges Schutzrecht; in der Familienliste oft als „European patent with unitary effect" gekennzeichnet.
- **PCT-Anmeldungen** (WO …) sind keine eigentlichen Patente, sondern Anmeldewege. Erst durch nationale Phasen entstehen die einzelnen Patente.
- **Anmelderwechsel.** Familienmitglieder können verschiedene Anmelder haben (Anmelderwechsel, Konzernverschiebung). Bei FTO immer auf den **aktuellen** eingetragenen Inhaber im jeweiligen Register prüfen.

## Disclaimer

> **Hinweis zur Familienanalyse.** Diese Patentfamilien-Analyse beruht auf INPADOC-Daten und ist eine KI-gestützte Vorrecherche. Datenlücken sind insbesondere bei JP- CN- KR- und einzelnen weiteren Aemtern möglich. Continuation- und Teilanmeldungen können anhängig sein, ohne dass sie schon veröffentlicht sind. Die Familie kann durch Anmelderwechsel verschoben sein. Die finale Familie- und Rechtsstandsbewertung muss durch direkte Recherche in den nationalen Registern abgesichert werden.

## Triage-Fragen vor Patentfamilien-Analyse

Bevor die Familienanalyse begonnen wird, klaere:
1. Ist das Ausgangsdokument (Stammanmeldung oder Hauptpatent) korrekt identifiziert?
2. Sind Continuation-, Divisional- und CIP-Anmeldungen (US) oder Teilanmeldungen (EP) beruecksichtigt?
3. Wurden JP, CN, KR-Familienmitglieder direkt in den nationalen Registern nachgeprueft (INPADOC-Luecken)?
4. Gibt es ein Einheitliches Patent (UP) unter dem EP-Patent — wenn ja, welche Staaten sind abgedeckt?

## Aktuelle Rechtsprechung

> **BGH, Urt. v. 04.04.2006 — X ZR 155/03 (Ruckwirkung Prioritaet):** Die Prioritaet einer Erstanmeldung wirkt auf das Anmelde- und Prioritaetsdatum der Stammanmeldung zurueck; alle Familienmitglieder teilen dieses frueheste Prioritaetsdatum, was fuer die Neuheitspruefung von Wettbewerber-Rechten relevant ist.

> **EPA, Erweiterte Beschwerdekammer, G 2/10 (Teilanmeldung):** Eine EP-Teilanmeldung kann nur Gegenstande umfassen, die in der Stammanmeldung zum Zeitpunkt der Einreichung der Teilanmeldung offenbart waren; neue Merkmale koennen nicht nachtraeglich in eine Teilanmeldung eingefuehrt werden.

> **BGH, Urt. v. 15.02.2010 — X ZR 76/08 (PCT-Phase):** Ein PCT-Patent erhält erst nach nationaler/regionaler Phaseneintritts-Erteilung Verbietungswirkung; waehrend der internationalen Phase nach PCT besteht kein unmittelbares Schutzrecht, sondern nur ein Anwartschaftsrecht.
