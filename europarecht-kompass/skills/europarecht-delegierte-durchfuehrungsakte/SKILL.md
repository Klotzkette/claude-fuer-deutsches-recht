---
name: europarecht-delegierte-durchfuehrungsakte
description: "Delegierte Durchfuehrungsakte: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Delegierte Durchfuehrungsakte

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Delegierte Durchfuehrungsakte** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `europarecht-delegierte-durchfuehrungsakte` | Delegierte Rechtsakte und Durchführungsrechtsakte der EU einordnen und deren Verbindlichkeit prüfen. Art. 290 291 AEUV Delegierung. Prüfraster: Kategorie Widerruf Einwand Verbindlichkeit nationaler Umsetzungsbedarf Direktwirkung. Output: Einordnungs-Memo Verbindlichkeitsanalyse. Abgrenzung: nicht für primaeres EU-Recht oder Richtlinien (europarecht-richtlinie-umsetzung). |
| `europarecht-deutscher-denkfehler-scanner` | Typische deutsche Denkfehler im Umgang mit EU-Recht erkennen und korrigieren. Art. 267 AEUV Vorrangprinzip EuGH-Judikatur. Prüfraster: fehlende Europarechtskonformität verkannte Direktwirkung uebergangene Vorlagepflicht falsche Richtlinienauslegung. Output: Denkfehler-Liste Korrekturempfehlungen. Abgrenzung: Qualitaets-Skill für alle Europarechts-Mandate. |
| `europarecht-gesetzgebung-trilog` | Europaeisches Gesetzgebungsverfahren und Trilog-Verhandlungen einordnen wenn EU-Regelung in Entstehung ist. Art. 289 294 AEUV ordentliches Gesetzgebungsverfahren. Prüfraster: Verfahrensstand Kompromisstext Ratspositionen EP-Positionen Zeitplan Umsetzungspflichten. Output: Verfahrensstand-Memo Stellungnahme-Empfehlung. Abgrenzung: nicht für erlassene Verordnungen oder Richtlinien. |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **Delegierte Durchfuehrungsakte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `europarecht-delegierte-durchfuehrungsakte`

**Fokus:** Delegierte Rechtsakte und Durchführungsrechtsakte der EU einordnen und deren Verbindlichkeit prüfen. Art. 290 291 AEUV Delegierung. Prüfraster: Kategorie Widerruf Einwand Verbindlichkeit nationaler Umsetzungsbedarf Direktwirkung. Output: Einordnungs-Memo Verbindlichkeitsanalyse. Abgrenzung: nicht für primaeres EU-Recht oder Richtlinien (europarecht-richtlinie-umsetzung).

# Delegierte und Durchführungsakte

## Zweck

Moderne EU-Regulierung wird über Basisrechtsakt, Folgeakt, technische Standards und Aufsichtspraxis gelesen.

## Wann verwenden

- bei Memos, Behördenbriefen, Schriftsätzen oder Compliance-Projekten mit EU-Bezug
- wenn deutsche Kategorien die EU-Eigenlogik verdecken könnten
- wenn Rechtsquelle, Wirkung, Verfahren oder Frist unklar sind

## Arbeitsweise

1. **Rechtsquelle fixieren.** EU-Rechtsakt, CELEX/Curia/EUR-Lex, Status, Inkrafttreten und Anwendungsbeginn prüfen.
2. **Wirkung bestimmen.** Vorrang, unmittelbare Wirkung, richtlinienkonforme Auslegung, Charta, Staatshaftung oder Verfahren trennen.
3. **Deutsche Denkfehler markieren.** Nationale Kategorien nur nutzen, wenn sie unionsrechtlich passen.
4. **Verfahrensweg planen.** Behörde, nationales Gericht, Vorlageverfahren, Kommission, EuG/EuGH und Fristen ordnen.
5. **Qualitätstor setzen.** Quellenstand, nationale Umsetzung, offene Vorlagefrage und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Vorrang nicht mit Nichtigkeit der nationalen Norm gleichsetzen.
- Richtlinie, Verordnung, Beschluss und Soft Law nicht vermischen.
- Charta nicht ohne Durchführung von Unionsrecht anwenden.
- Keine CELEX- oder EuGH-Fundstelle erfinden.

## Ton

Europarecht-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage vor Pruefung

Bevor losgelegt wird, klaere:
1. Handelt es sich um einen delegierten Rechtsakt (Art. 290 AEUV — Ergaenzung/Aenderung nicht wesentlicher Teile) oder Durchfuehrungsrechtsakt (Art. 291 AEUV — einheitliche Umsetzungsbedingungen)?
2. Wurde die Ermaechtigung im Basisrechtsakt korrekt erteilt (wesentliche Elemente nur durch Gesetzgeber)?
3. Koennen Rat oder EP widersprechen / widerrufen (Art. 290 Abs. 2 AEUV)?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette

- **Art. 290 AEUV** — Delegierte Rechtsakte; EP/Rat-Widerrufsrecht; Kontrollmechanismus
- **Art. 291 AEUV** — Durchfuehrungsrechtsakte; Komitologie-VO (EU) 182/2011
- **Komitologie-VO (EU) 182/2011** — Beratungs-, Untersuchungs-, Kontrollverfahren

## Output-Template: Rechtsakts-Klassifikationsmemo

```
RECHTSAKT-KLASSIFIKATION
Rechtsakt: [Titel / CELEX-Nr.]
Art. 290 (delegiert): [JA — Ermaechtigungsnorm im Basisrechtsakt: Art. X VO Y]
Art. 291 (Durchfuehrung): [JA — einheitliche Durchfuehrungsbedingungen]
Widerspruchsrecht EP/Rat: [JA — Frist X Wochen / NEIN]
Moegliche Anfechtung: [Art. 263 AEUV — Frist 2 Monate ab Bekanntmachung]
```

## 2. `europarecht-deutscher-denkfehler-scanner`

**Fokus:** Typische deutsche Denkfehler im Umgang mit EU-Recht erkennen und korrigieren. Art. 267 AEUV Vorrangprinzip EuGH-Judikatur. Prüfraster: fehlende Europarechtskonformität verkannte Direktwirkung uebergangene Vorlagepflicht falsche Richtlinienauslegung. Output: Denkfehler-Liste Korrekturempfehlungen. Abgrenzung: Qualitaets-Skill für alle Europarechts-Mandate.

# Deutscher-Denkfehler-Scanner

## Zweck

Deutsche Dogmatik wird genutzt, aber nicht als Schablone für EU-Rechtsquellen, Wirkung und Rechtsschutz missbraucht.

## Wann verwenden

- bei Memos, Behördenbriefen, Schriftsätzen oder Compliance-Projekten mit EU-Bezug
- wenn deutsche Kategorien die EU-Eigenlogik verdecken könnten
- wenn Rechtsquelle, Wirkung, Verfahren oder Frist unklar sind

## Arbeitsweise

1. **Rechtsquelle fixieren.** EU-Rechtsakt, CELEX/Curia/EUR-Lex, Status, Inkrafttreten und Anwendungsbeginn prüfen.
2. **Wirkung bestimmen.** Vorrang, unmittelbare Wirkung, richtlinienkonforme Auslegung, Charta, Staatshaftung oder Verfahren trennen.
3. **Deutsche Denkfehler markieren.** Nationale Kategorien nur nutzen, wenn sie unionsrechtlich passen.
4. **Verfahrensweg planen.** Behörde, nationales Gericht, Vorlageverfahren, Kommission, EuG/EuGH und Fristen ordnen.
5. **Qualitätstor setzen.** Quellenstand, nationale Umsetzung, offene Vorlagefrage und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Vorrang nicht mit Nichtigkeit der nationalen Norm gleichsetzen.
- Richtlinie, Verordnung, Beschluss und Soft Law nicht vermischen.
- Charta nicht ohne Durchführung von Unionsrecht anwenden.
- Keine CELEX- oder EuGH-Fundstelle erfinden.

## Ton

Europarecht-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Vertiefung: Typische Denkfehler und Korrekturen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Denkfehler 3: Charta gilt immer.** Falsch. GRCh Art. 51 — nur wenn MS EU-Recht durchfuehrt; sonst gilt das GG/EMRK.
- **Denkfehler 4: EuGH-Zugang offen fuer Private.** Eng begrenzt. Art. 263 Abs. 4 AEUV: Plaumann-Formel sehr streng; individuelle Betroffenheit kaum nachweisbar. Regelweg: Vorlage Art. 267 AEUV ueber nationales Gericht.
- **Denkfehler 5: Vollzugsdefizit = Verstoß.** Differenzieren: Anwendungsermessen vs. kein Ermessen; Kommission vs. nationale Behoerde; Art. 258 vs. Staatshaftung.

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage vor Einsatz

Bevor losgelegt wird, klaere:
1. Welche konkrete Kategorie EU-Recht — Verordnung, Richtlinie, Charta, AEUV-Grundfreiheit?
2. Handelt ein Privatmann oder der Staat — unterschiedliche Pruefmuster!
3. Rechtsfolge: Direktwirkung, Vorrang, Staatshaftung, Vorlage?

## Output-Template: Denkfehler-Pruefliste

```
EU-RECHT DENKFEHLER-SCAN
Sachverhalt: [KURZBESCHREIBUNG]

1. Rechtsakt klassifiziert: [VO direkt / RL umsetzungsbedurftig / GRCh / AEUV]
2. Anwendungsbereich geprueft:
 - GRCh Art. 51: MS fuehrt EU-Recht durch? [JA / NEIN]
 - Charta gilt: [JA / NUR GG]
3. Vorrang-Konsequenz:
 - Nicht: Nichtigkeit. Sondern: Nichtanwendung § X im Einzelfall
4. Direktwirkung:
 - Richtlinie: Frist abgelaufen [JA/NEIN] + nur gg. Staat
 - Verordnung: immer
5. EuGH-Klage:
 - Privilegierter Klager? [ja/nein]
 - Plaumann-Formel erfuellt? [fraglich — Vorlage empfohlen]
6. Ergebnis: [Keine deutschen Fehler entdeckt / PROBLEM: ...]
```

## 3. `europarecht-gesetzgebung-trilog`

**Fokus:** Europaeisches Gesetzgebungsverfahren und Trilog-Verhandlungen einordnen wenn EU-Regelung in Entstehung ist. Art. 289 294 AEUV ordentliches Gesetzgebungsverfahren. Prüfraster: Verfahrensstand Kompromisstext Ratspositionen EP-Positionen Zeitplan Umsetzungspflichten. Output: Verfahrensstand-Memo Stellungnahme-Empfehlung. Abgrenzung: nicht für erlassene Verordnungen oder Richtlinien.

# EU-Gesetzgebung und Trilog

## Zweck

Politischer Entwurf, angenommener Rechtsakt, Inkrafttreten, Anwendung und nationale Umsetzung werden getrennt.

## Wann verwenden

- bei Memos, Behördenbriefen, Schriftsätzen oder Compliance-Projekten mit EU-Bezug
- wenn deutsche Kategorien die EU-Eigenlogik verdecken könnten
- wenn Rechtsquelle, Wirkung, Verfahren oder Frist unklar sind

## Arbeitsweise

1. **Rechtsquelle fixieren.** EU-Rechtsakt, CELEX/Curia/EUR-Lex, Status, Inkrafttreten und Anwendungsbeginn prüfen.
2. **Wirkung bestimmen.** Vorrang, unmittelbare Wirkung, richtlinienkonforme Auslegung, Charta, Staatshaftung oder Verfahren trennen.
3. **Deutsche Denkfehler markieren.** Nationale Kategorien nur nutzen, wenn sie unionsrechtlich passen.
4. **Verfahrensweg planen.** Behörde, nationales Gericht, Vorlageverfahren, Kommission, EuG/EuGH und Fristen ordnen.
5. **Qualitätstor setzen.** Quellenstand, nationale Umsetzung, offene Vorlagefrage und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Vorrang nicht mit Nichtigkeit der nationalen Norm gleichsetzen.
- Richtlinie, Verordnung, Beschluss und Soft Law nicht vermischen.
- Charta nicht ohne Durchführung von Unionsrecht anwenden.
- Keine CELEX- oder EuGH-Fundstelle erfinden.

## Ton

Europarecht-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Vertiefung: Gesetzgebungsverfahren und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage vor Gesetzgebungsfrage

Bevor losgelegt wird, klaere:
1. Welches Verfahren — ordentliches (Art. 294 AEUV) oder besonderes Gesetzgebungsverfahren?
2. In welcher Phase — Kommissionsvorschlag, 1. Lesung EP, 2. Lesung, Trilog, Vermittlungsausschuss?
3. Hat Mandant Interesse an Einfluss — Lobby-Kontakt, Petition EP, Konsultation Kommission?

## Normen-Kette

- **Art. 289 AEUV** — Gesetzgebungsverfahren (ordentlich/besonderes); Art. 293 AEUV — Aenderungen Kommissionsvorschlag
- **Art. 294 AEUV** — Ordentliches Gesetzgebungsverfahren Ablauf (Lesungen, Trilog)
- **Art. 296 AEUV** — Begruendungspflicht EU-Rechtsakte; Art. 297 — Bekanntmachung, Inkrafttreten

## Output-Template: Legislationstrackin-Memo

```
LEGISLATIVES TRACKING-MEMO
Rechtsakt: [Kurzbezeichnung / COM-Nr.]
Status: [Kommissionsvorschlag / 1. Lesung EP / Trilog / verabschiedet / in Kraft]
Anwendungsbeginn: [DATUM oder X Monate nach Inkrafttreten]
Betroffener Bereich Mandant: [BESCHREIBUNG]
Handlungsbedarf: [Lobbyarbeit / Ausnahmeregelung pruefen / Umsetzung vorbereiten]
Naechste Schritte: [...]
```
