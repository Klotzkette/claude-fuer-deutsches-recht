---
name: europarecht-grundfreiheiten-binnenmarkt
description: "Grundfreiheiten Binnenmarkt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Grundfreiheiten Binnenmarkt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Grundfreiheiten Binnenmarkt** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `europarecht-grundfreiheiten-binnenmarkt` | Grundfreiheiten des Binnenmarkts prüfen wenn grenzüberschreitende Wirtschaftstätigkeit oder nationale Beschraenkung in Frage steht. Art. 34 45 49 56 63 AEUV Warenverkehr Personenfreizuegigkeit Niederlassungsfreiheit. Prüfraster: Anwendungsbereich Beschraenkung Rechtfertigung Verhältnismäßigkeit Cassis-Doktrin. Output: Grundfreiheiten-Prüfschema Prüfmemo. Abgrenzung: nicht für EU-Beihilfen (europarecht-beihilfen-vergaben). |
| `europarecht-grundrechte-charta` | EU-Grundrechtecharta anwenden wenn EU-Recht vollzogen wird oder Mitgliedstaat im Anwendungsbereich des EU-Rechts handelt. Art. 51 GRC Anwendungsbereich Art. 6 EUV. Prüfraster: Anwendungsbereich Art. 51 GRC beruertes Recht Einschraenkung Art. 52 GRC Wesensgehalt Verhältnismäßigkeit. Output: GRC-Prüfschema Prüfmemo. Abgrenzung: nicht für EMRK oder nationales Grundgesetz. |
| `europarecht-klagearten-eugh` | Klagemoglichkeiten vor dem EuGH und EuG einordnen und Zulassigkeitsvoraussetzungen prüfen. Art. 263 265 268 340 AEUV Nichtigkeitsklage Untätigkeitsklage Schadensersatz. Prüfraster: Klageart Klagebefugnis Fristen Zuständigkeit Zulässigkeit Begründung. Output: Klagearten-Prüfschema Zulässigkeitsanalyse. Abgrenzung: nicht für Vertragsverletzungsverfahren (europarecht-vertragsverletzung-durchsetzung). |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **Grundfreiheiten Binnenmarkt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `europarecht-grundfreiheiten-binnenmarkt`

**Fokus:** Grundfreiheiten des Binnenmarkts prüfen wenn grenzüberschreitende Wirtschaftstätigkeit oder nationale Beschraenkung in Frage steht. Art. 34 45 49 56 63 AEUV Warenverkehr Personenfreizuegigkeit Niederlassungsfreiheit. Prüfraster: Anwendungsbereich Beschraenkung Rechtfertigung Verhältnismäßigkeit Cassis-Doktrin. Output: Grundfreiheiten-Prüfschema Prüfmemo. Abgrenzung: nicht für EU-Beihilfen (europarecht-beihilfen-vergaben).

# Grundfreiheiten und Binnenmarkt

## Zweck

Binnenmarktprüfung ohne Art.-12-GG-Autopilot, mit Grenzbezug, Beschränkung und Rechtfertigung.

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
1. Welche Grundfreiheit ist betroffen — Warenverkehr, Dienstleistungen, Niederlassung, Kapital, Personen?
2. Ist der Sachverhalt grenzueberschreitend (rein inlaendischer Sachverhalt wird nicht erfasst)?
3. Liegt eine staatliche oder staatsaehnliche Maßnahme vor (Mitgliedstaat, Behoerde, halboeffentliche Stellen)?
4. Koennte die Beschraenkung gerechtfertigt sein (Art. 36, 45 Abs. 3, 52 AEUV; zwingende Erfordernisse)?
5. Verhältnismaessigkeitspruefung: Geeignetheit, Erforderlichkeit, Angemessenheit?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette Grundfreiheiten

- **Art. 34-36 AEUV** — Freier Warenverkehr; Mengenmassige Beschraenkungen und Massnahmen gleicher Wirkung; Rechtfertigungsgruende Art. 36
- **Art. 45-48 AEUV** — Arbeitnehmerfreizuegigkeit; Diskriminierungsverbot; Art. 45 Abs. 3 Ausnahme oeffentl. Ordnung
- **Art. 49-55 AEUV** — Niederlassungsfreiheit; Sekundaerniederlassung; Art. 52 Rechtfertigungsgruende
- **Art. 56-62 AEUV** — Dienstleistungsfreiheit; voruebergehende Erbringung; DLF-RL 2006/123
- **Art. 63-66 AEUV** — Kapitalverkehrsfreiheit; umfassendste Grundfreiheit; auch gg. Drittlaender

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Grundfreiheiten-Pruefung

**Adressat:** Kanzlei-intern oder Mandant
**Tonfall:** Systematisch-analytisch

```
GRUNDFREIHEITEN-KURZPRUEFUNG
Datum: [DATUM] — Mandant: [NAME]
Sachverhalt: [KURZBESCHREIBUNG]

1. BETROFFENE GRUNDFREIHEIT
[ ] Warenverkehr Art. 34 AEUV
[ ] Arbeitnehmerfreizuegigkeit Art. 45 AEUV
[ ] Niederlassungsfreiheit Art. 49 AEUV
[ ] Dienstleistungsfreiheit Art. 56 AEUV
[ ] Kapitalverkehrsfreiheit Art. 63 AEUV

2. GRENZUEBERSCHREITENDER BEZUG: [JA / NEIN]

3. BESCHRAENKUNG: [Beschreibung]
 Diskriminierung: [offene / versteckte / keine]
 Marktzugangshemmnis: [JA / NEIN — Begruendung]

4. RECHTFERTIGUNG
 Art. [36 / 45 Abs. 3 / 52] AEUV: [Sicherheit / Gesundheit / oeffentl. Ordnung]
 Zwingende Erfordernisse (Cassis): [Verbraucherschutz / Umwelt / ...]
 Verhaeltnismaessigkeit: [geeignet / erforderlich / angemessen — je JA/NEIN]

5. ERGEBNIS
[ ] Keine Beschraenkung
[ ] Beschraenkung — gerechtfertigt
[ ] Beschraenkung — nicht gerechtfertigt — EU-Rechtsverstoß
```

## 2. `europarecht-grundrechte-charta`

**Fokus:** EU-Grundrechtecharta anwenden wenn EU-Recht vollzogen wird oder Mitgliedstaat im Anwendungsbereich des EU-Rechts handelt. Art. 51 GRC Anwendungsbereich Art. 6 EUV. Prüfraster: Anwendungsbereich Art. 51 GRC beruertes Recht Einschraenkung Art. 52 GRC Wesensgehalt Verhältnismäßigkeit. Output: GRC-Prüfschema Prüfmemo. Abgrenzung: nicht für EMRK oder nationales Grundgesetz.

# EU-Grundrechte und Charta

## Zweck

Die Charta wird nur im Anwendungsbereich des Unionsrechts aktiviert und nicht als Allzweckgrundrecht eingesetzt.

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

## Triage vor Charta-Pruefung

Bevor losgelegt wird, klaere:
1. Handelt der Mitgliedstaat in Durchfuehrung von EU-Recht (Art. 51 GRCh — dann Charta anwendbar)?
2. Welches Grundrecht der GRCh ist einschlaegig (Art. 1-54 GRCh)?
3. Besteht ein entsprechendes EMRK-Recht — Wechselwirkung Art. 52 Abs. 3 GRCh?
4. Ist der Eingriff durch Art. 52 GRCh gerechtfertigt (Gesetzesvorbehalt, Wesensgehalt, Verhältnismaessigkeit)?

## Vertiefung: Rechtsprechung und Leitsaetze

Rechtsprechung live über [curia.europa.eu](https://curia.europa.eu/) verifizieren — keine Az. aus Modellwissen.

Aktuelle Linien zu Art. 7, 8 GRCh (Datenschutz / Privatleben) — relevant für Mandate Q4 2025 - Q2 2026:

- EuGH, Urt. v. 02.12.2025 — C-492/23 (Russmedia) — DSGVO geht DSA vor; Plattformen müssen vor Veröffentlichung von Inhalten mit besonderen Datenkategorien Identität des Posters prüfen und Rechtsgrundlage prüfen; Hosting-Privileg gilt nicht für DSGVO-Verstöße.
- EuGH, Urt. v. 13.02.2025 — C-383/23 (ILVA) — DSGVO-Bußgelder können auf Konzernumsatz (Art. 83 Abs. 4-6 DSGVO) bezogen werden; "Unternehmen" im Sinne des EU-Wettbewerbsrechts (Art. 101, 102 AEUV) auch für DSGVO-Geldbußenobergrenze einschlägig.
- EuGH, Urt. v. 19.03.2026 — C-526/24 (Brillen Rottler) — Erstmaliger Auskunftsantrag (Art. 15 DSGVO) kann als rechtsmissbräuchlich zurückgewiesen werden; Beweislast trägt der Verantwortliche.
- EGMR, Urt. v. 09.04.2024 — Verein KlimaSeniorinnen gegen Schweiz, Bf-Nr. 53600/20 — Art. 8 EMRK-Schutzpflicht des Staates gegen Folgen des Klimawandels (relevant über Art. 52 Abs. 3 GRCh).

## Normen-Kette GRCh

- **Art. 7 GRCh** — Achtung des Privat- und Familienlebens (EMRK Art. 8 entspricht)
- **Art. 8 GRCh** — Datenschutz; Verarbeitung personenbezogener Daten
- **Art. 17 GRCh** — Eigentumsrecht; Art. 41 — Recht auf gute Verwaltung
- **Art. 47 GRCh** — Recht auf wirksamen Rechtsbehelf und unparteiisches Gericht
- **Art. 51 GRCh** — Anwendungsbereich: nur bei Durchfuehrung von EU-Recht durch MS
- **Art. 52 GRCh** — Tragweite und Auslegung der Rechte; Verhältnismaessigkeit; EMRK-Parallelnorm

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: GRCh-Grundrechtepruefung

**Adressat:** Kanzlei-intern
**Tonfall:** Systematisch-juristisch

```
GRCh-GRUNDRECHTEPRUEFUNG
Datum: [DATUM] — Mandant: [NAME]

1. ANWENDBARKEIT GRCh ART. 51
MS fuehrt EU-Recht durch: [JA — Bezug: [VO/RL] / NEIN — nur GG/EMRK]

2. EINSCHLAEGIGES GRUNDRECHT
Art. [X] GRCh: [Bezeichnung]
EMRK-Entsprechung Art. 52 Abs. 3: Art. [Y] EMRK

3. EINGRIFF
Beschreibung: [...]
Intensitaet: [gering / mittel / schwerwiegend]

4. RECHTFERTIGUNG ART. 52 ABS. 1 GRCh
a) Gesetzesvorbehalt: [gesetzliche Grundlage: ...]
b) Wesensgehalt unberuehrt: [JA / NEIN]
c) Verhältnismaessigkeit: geeignet [JA/NEIN] erforderlich [JA/NEIN] angemessen [JA/NEIN]

5. ERGEBNIS
[ ] Kein Eingriff
[ ] Eingriff — gerechtfertigt
[ ] Eingriff — NICHT gerechtfertigt — EU-Grundrechtsverletzung
Empfehlung: [Vorabentscheidung / Verfassungsbeschwerde / Klage EuGH]
```

## 3. `europarecht-klagearten-eugh`

**Fokus:** Klagemoglichkeiten vor dem EuGH und EuG einordnen und Zulassigkeitsvoraussetzungen prüfen. Art. 263 265 268 340 AEUV Nichtigkeitsklage Untätigkeitsklage Schadensersatz. Prüfraster: Klageart Klagebefugnis Fristen Zuständigkeit Zulässigkeit Begründung. Output: Klagearten-Prüfschema Zulässigkeitsanalyse. Abgrenzung: nicht für Vertragsverletzungsverfahren (europarecht-vertragsverletzung-durchsetzung).

# EuGH-Klagearten und Rechtsschutz

## Zweck

Direkter EuG/EuGH-Zugang wird nicht überschätzt; Fristen und Zulässigkeit werden früh geprüft.

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

## Triage vor Klage-/Rechtswegprüfung

Bevor losgelegt wird, klaere:
1. Welche Handlung ist angegriffen — EU-Verordnung, EU-Richtlinie, Kommissionsbeschluss, Untaetigkeit?
2. Wer klagt — Mitgliedstaat (privilegierter Klager), Institution, natuerliche oder juristische Person (nicht privilegierter Klager)?
3. Ist direkte individuelle Betroffenheit nachweisbar (bei nicht privilegierten Klaegern Art. 263 Abs. 4 AEUV)?
4. Ist die 2-Monats-Frist Art. 263 Abs. 6 AEUV noch offen?
5. Besteht Vorlagemoeglichkeit beim nationalen Gericht als Alternative (Art. 267 AEUV)?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette EuGH-Klagearten

- **Art. 263 AEUV** — Nichtigkeitsklage; Fristen; Klagebefugnis privilegierter/nicht-privilegierter Klager
- **Art. 265 AEUV** — Untaetigkeitsklage; Voraussetzungen: vorherige Aufforderung + 2 Monate Nichtreagieren
- **Art. 268 AEUV iVm Art. 340 AEUV** — Amtshaftungsklage; hinreichend qualifizierter Rechtsverstoss; Schaden; Kausalitaet
- **Art. 267 AEUV** — Vorabentscheidungsverfahren als indirekter Rechtsschutz-Weg fuer Private
- **Art. 278 AEUV** — Vorlaufiger Rechtsschutz beim EuGH (Antrag auf Aussetzung)
- **EuGH-Satzung Art. 56** — Frist Rechtsmittel gegen EuG-Urteile: 2 Monate

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Klagebefugnis-Pruefmemo

**Adressat:** Kanzlei-intern / Mandant
**Tonfall:** Sachlich-juristisch; Zulässigkeit klärend

```
KLAGEBEFUGNIS-MEMO EuGH / EuG
Datum: [DATUM] — Mandant: [NAME]
Angegriffener EU-Rechtsakt: [CELEX-Nr. / Art der Maßnahme]

A. KLAGEARTENWAHL
[ ] Nichtigkeitsklage Art. 263 AEUV — Frist: 2 Monate ab [DATUM BEKANNTGABE]
[ ] Untaetigkeitsklage Art. 265 AEUV — Aufforderung an [INSTITUTION] am [DATUM]
[ ] Amtshaftung Art. 268/340 AEUV — Schaden: EUR [X]; Kausalitaet: [ja/nein]
[ ] Vorabentscheidung Art. 267 AEUV (nur via nationales Gericht)

B. KLAGEBEFUGNIS (bei Art. 263 Abs. 4)
Privileg. Klager (MS / Inst.): [ja / nein]
Unmittelbare Betroffenheit: [ja — Beschluss ohne Durchfuehrungsmaßnahmen / nein]
Individuelle Betroffenheit (Plaumann): [ja — [SPEZ. GRÜNDE] / FRAGLICH]
Eigene Rechtsinstrumente (Regelungsakt): [ja / nein]

C. FRIST
Klagefrist Art. 263 Abs. 6: 2 Monate ab [DATUM] = letzter Tag [DATUM]
Fristwahrung: [gesichert / gefaehrdet — Antrag Fristerstreckung EuGH?]

D. ERGEBNIS
[ ] Klage zulaessig — weiter mit Begruendung
[ ] Klage unzulaessig — Alternative: Vorabentscheidungsverfahren Art. 267 AEUV
[ ] Weitere Klaerung erforderlich: [Punkt]
```
