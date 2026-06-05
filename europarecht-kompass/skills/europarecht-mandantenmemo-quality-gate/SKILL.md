---
name: europarecht-mandantenmemo-quality-gate
description: "Mandantenmemo Quality Gate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenmemo Quality Gate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenmemo Quality Gate** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `europarecht-kommandocenter` | Einstiegspunkt für Europarechtsmandate: Rechtsgebiet bestimmen relevante Normen identifizieren Bearbeitungsroute festlegen. AEUV EUV GRC EU-Sekundaerrecht. Prüfraster: Sachverhalt EU-Rechtsbezug Rechtsgebiet Route Zeitdruck Mandantensprache. Output: Mandat-Steckbrief Normenmap naechste Schritte. Abgrenzung: Einstieg und Triage; Detailarbeit in Spezialist-Skills. |
| `europarecht-mandantenmemo` | Mandantenmemo zu EU-Rechtsfragen verstaendlich und praxisorientiert verfassen. AEUV EUV EU-Sekundaerrecht Grundfreiheiten. Prüfraster: Sachverhaltszusammenfassung Rechtslage Handlungsoptionen Risiken Empfehlung Mandantensprache. Output: strukturiertes Mandantenmemo. Abgrenzung: nicht für interne Vermerke oder Schriftsaetze. |
| `europarecht-quality-gate` | EU-Rechtsgutachten oder -Schriftsatz auf typische Fehler und Luecken prüfen vor Versand. Art. 267 AEUV EuGH-Judikatur Vorrangprinzip. Prüfraster: Vorlagepflicht uebersehen Direktwirkung verkannt Normhierarchie fehlerhaft Richtlinienkonformität fehlend. Output: Fehlerprotokoll Korrekturempfehlungen. Abgrenzung: Quality Gate für alle Europarechts-Skills. |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **Mandantenmemo Quality Gate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `europarecht-kommandocenter`

**Fokus:** Einstiegspunkt für Europarechtsmandate: Rechtsgebiet bestimmen relevante Normen identifizieren Bearbeitungsroute festlegen. AEUV EUV GRC EU-Sekundaerrecht. Prüfraster: Sachverhalt EU-Rechtsbezug Rechtsgebiet Route Zeitdruck Mandantensprache. Output: Mandat-Steckbrief Normenmap naechste Schritte. Abgrenzung: Einstieg und Triage; Detailarbeit in Spezialist-Skills.

# Europarecht-Kommandocenter

## Zweck

Einstieg für jedes Mandat, in dem deutsches Recht, Unionsrecht, Behördenpraxis, nationale Umsetzung oder EuGH-Rechtsprechung ineinandergreifen.

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

## Vertiefung: Kernentscheidungen EU-Recht

Rechtsprechung live über [curia.europa.eu](https://curia.europa.eu/) verifizieren — Aktenzeichen nicht aus Modellwissen.

Aktuelle Linien Q4 2025 - Q2 2026 (für Triage):

- EuGH, Urt. v. 02.12.2025 — C-492/23 (Russmedia) — DSGVO geht DSA vor; kein Hosting-Provider-Privileg bei DSGVO-Verstößen durch nutzergenerierte Inhalte; Plattformen müssen besondere Datenkategorien proaktiv vor Veröffentlichung prüfen. Verifikation [curia.europa.eu](https://curia.europa.eu/).
- EuGH, Urt. v. 19.03.2026 — C-526/24 (Brillen Rottler) — Auch ein erstmaliger DSGVO-Auskunftsantrag (Art. 15 DSGVO) kann als rechtsmissbräuchlich zurückgewiesen werden, wenn er nur im Hinblick auf Schadensersatzansprüche aus Art. 82 DSGVO gestellt wird; Beweislast trägt der Verantwortliche.
- EuGH, Urt. v. 01.08.2025 — C-600/23 (RFC Seraing) — Nationale Gerichte in EU-Mitgliedstaaten dürfen CAS-Schiedssprüche auf Vereinbarkeit mit Unionsrecht überprüfen.
- EuGH, Urt. v. 05.03.2026 — C-458/24 (Daraa) — Dublin-III: Zuständigkeitsübergang nach Ablauf 6-Monatsfrist; einseitige Aussetzung der Rücknahme bewirkt keinen automatischen Übergang.
- **KI-Verordnung (EU) 2024/1689:** Hauptanwendung Pflichten Hochrisiko-KI ab 02.08.2026; Verbote (Art. 5) bereits ab 02.02.2025 anwendbar; Allgemeine KI-Modelle (GPAI) ab 02.08.2025.

## Triage Kommandocenter

Bevor losgelegt wird, klaere:
1. Welches EU-Rechtsgebiet — Beihilfe, Grundfreiheiten, Kartell, Richtlinie, GRCh, Schiedsrecht?
2. Welches Output-Ziel — Memo, Schriftsatz, Compliance-Check, Vorabentscheidungsantrag?
3. Zeitdruck — Frist Art. 263 AEUV 2 Monate, Eilantrag, Vorlage?

## Normen-Kern EU-Recht

- **Art. 101-109 AEUV** — Wettbewerbsrecht; Beihilfen
- **Art. 263, 267-268 AEUV** — Klagen; Vorabentscheidung; Haftung
- **Art. 288-291 AEUV** — Handlungsformen; delegierte Akte
- **GRCh Art. 47, 51** — Rechtsschutz; Anwendungsbereich

## Output-Template: Aktionsplan EU-Recht

```
EU-RECHT AKTIONSPLAN
Datum: [DATUM] — Mandant: [NAME]

1. Rechtsgebiet: [BEIHILFE / KARTELL / GRUNDFREIHEITEN / RICHTLINIE / GRCh]
2. Klaerbedarf: [unmittelbare Wirkung / Vorrang / Klagebefugnis / Freistellung]
3. Frist: [Art. 263 AEUV 2 Monate ab [DATUM] / sonstige Frist: [DATUM]]
4. Zustaendiges Gericht: [LG / VG / EuG / EuGH]
5. Rechtsmittel: [Klage / Vorlageanregung / Beschwerde Kommission / Staatshaftung]
6. Naechste Schritte: [...]
```

## 2. `europarecht-mandantenmemo`

**Fokus:** Mandantenmemo zu EU-Rechtsfragen verstaendlich und praxisorientiert verfassen. AEUV EUV EU-Sekundaerrecht Grundfreiheiten. Prüfraster: Sachverhaltszusammenfassung Rechtslage Handlungsoptionen Risiken Empfehlung Mandantensprache. Output: strukturiertes Mandantenmemo. Abgrenzung: nicht für interne Vermerke oder Schriftsaetze.

# Mandantenmemo und Executive Briefing

## Zweck

Business-taugliche EU-Memos liefern Rechtsquellenstatus, Risikoampel, Maßnahmenplan und Denkfehler-Hinweis.

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

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage vor Mandantenmemo

Bevor losgelegt wird, klaere:
1. Adressat — Mandant direkt (verstaendlich) oder Gericht (juristisch praezise)?
2. Dringlich — Frist EU-Recht (Art. 263 AEUV 2 Monate) oder Zeit vorhanden?
3. Niveau — Kurzmemo (1 Seite) oder vollstaendige Rechtslage (5 Seiten)?

## Output-Template: Mandantenmemo EU-Recht

**Adressat:** Mandant
**Tonfall:** Verstaendlich-erklaerend; Rechtslage klar ohne Jargon

```
MANDANTENMEMO EU-RECHT
Kanzlei: [KANZLEI] — Datum: [DATUM]
Mandant: [NAME]
Betreff: [THEMA IN EINEM SATZ]

I. SACHVERHALT IN KURZE
[3-5 Saetze]

II. RECHTLICHE EINORDNUNG
Die Frage betrifft [EU-Recht — Art. X AEUV / VO / RL].
Fuer Sie bedeutet das: [klare Aussage ohne Jargon].

III. RISIKEN UND CHANCEN
Risiko: [...]
Chance: [z.B. Schadensersatz nach Francovich-Doktrin]

IV. EMPFEHLUNG
Wir empfehlen: [Klage / Vorlage / Beschwerde Kommission / Abwarten]
Frist: [DATUM]
Kosten: [Schaetzung]

V. NAECHSTE SCHRITTE
1. [Schritt — Owner — Frist]
2. [Schritt]
```

## 3. `europarecht-quality-gate`

**Fokus:** EU-Rechtsgutachten oder -Schriftsatz auf typische Fehler und Luecken prüfen vor Versand. Art. 267 AEUV EuGH-Judikatur Vorrangprinzip. Prüfraster: Vorlagepflicht uebersehen Direktwirkung verkannt Normhierarchie fehlerhaft Richtlinienkonformität fehlend. Output: Fehlerprotokoll Korrekturempfehlungen. Abgrenzung: Quality Gate für alle Europarechts-Skills.

# Europarecht-Qualitätstor

## Zweck

Keine finale Freigabe ohne CELEX/Curia/EUR-Lex, Status, Anwendungsbeginn, nationale Umsetzung und Verfahrensweg.

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

## Vertiefung: Pruefpunkte und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage Quality Gate

Bevor losgelegt wird, klaere:
1. Ist jede CELEX-Nummer verifiziert (EUR-Lex oder Curia)?
2. Ist der Anwendungsbereich GRCh Art. 51 korrekt geprueft?
3. Sind alle Fristen aufgefuehrt (Klage-, Widerruf-, Einreichungsfristen)?
4. Werden Denkfehler (Direktwirkung Richtlinie zwischen Privaten) vermieden?

## Output-Template: Quality-Gate-Checkliste

```
QUALITY GATE EU-RECHT
Dokument: [BEZEICHNUNG] — Datum: [DATUM]

[ ] Alle CELEX-Nummern in EUR-Lex/Curia verifiziert
[ ] Keine erfundenen EuGH-Aktenzeichen oder Fundstellen
[ ] Anwendungsbereich GRCh Art. 51 korrekt geprueft
[ ] Fristen vollstaendig und korrekt (Art. 263 AEUV 2 Monate / Sonderfristen)
[ ] Vorrang-Konsequenz korrekt formuliert (nicht "Nichtigkeit" sondern "Nichtanwendung")
[ ] Direktwirkung Richtlinie: nur vertikal wenn Frist abgelaufen
[ ] Keine unzulaessige horizontale Direktwirkung Richtlinie zwischen Privaten
[ ] Quellenstand aktuell (letzte EU-Aenderungen einbezogen)
[ ] Offene Fragen und Unsicherheiten dokumentiert

Ergebnis: [ ] Freigabe [ ] Nacharbeit erforderlich — [Punkt]
```
