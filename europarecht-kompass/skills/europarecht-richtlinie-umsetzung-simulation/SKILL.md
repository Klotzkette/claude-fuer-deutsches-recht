---
name: europarecht-richtlinie-umsetzung-simulation
description: "Richtlinie Umsetzung Simulation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richtlinie Umsetzung Simulation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Richtlinie Umsetzung Simulation** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `europarecht-richtlinie-umsetzung` | EU-Richtlinie in nationales Recht umsetzen oder Umsetzungsdefizit prüfen. Art. 288 AEUV Richtlinienwirkung Art. 267 AEUV Vorabentscheidung. Prüfraster: Umsetzungsfrist Umsetzungsdefizit Direktwirkung richtlinienkonforme Auslegung Staatshaftung Francovich. Output: Umsetzungsanalyse Defizit-Memo Handlungsempfehlung. Abgrenzung: nicht für Verordnungen (europarecht-verordnung-beschluss-soft-law). |
| `europarecht-simulation-behoerde-gericht` | Verhandlung vor EU-Behoerde oder nationalem Gericht mit EU-Rechtsbezug simulieren und Argumentation testen. Art. 267 AEUV Art. 263 AEUV EuGH-Verfahren. Prüfraster: Argumente Gegenargumente Vorlageentscheidung Richterperspektive Schwachstellen. Output: Simulationsprotokoll Argumentation-Feinschliff. Abgrenzung: nicht für Klageentwuerfe (europarecht-klagearten-eugh). |
| `europarecht-verordnung-beschluss-soft-law` | EU-Verordnungen Beschluesse und Soft-Law-Instrumente einordnen und deren Verbindlichkeit prüfen. Art. 288 AEUV EU-Rechtsquellen. Prüfraster: Rechtsquellentyp Verbindlichkeit Direktwirkung nationaler Anpassungsbedarf zeitlicher Geltungsbereich. Output: Rechtsquellen-Einordnungs-Memo. Abgrenzung: nicht für Richtlinien (europarecht-richtlinie-umsetzung). |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **Richtlinie Umsetzung Simulation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `europarecht-richtlinie-umsetzung`

**Fokus:** EU-Richtlinie in nationales Recht umsetzen oder Umsetzungsdefizit prüfen. Art. 288 AEUV Richtlinienwirkung Art. 267 AEUV Vorabentscheidung. Prüfraster: Umsetzungsfrist Umsetzungsdefizit Direktwirkung richtlinienkonforme Auslegung Staatshaftung Francovich. Output: Umsetzungsanalyse Defizit-Memo Handlungsempfehlung. Abgrenzung: nicht für Verordnungen (europarecht-verordnung-beschluss-soft-law).

# Richtlinie und Umsetzung

## Zweck

Richtlinien werden nicht wie Verordnungen behandelt; Umsetzungsdefizite und gold plating werden sichtbar.

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

## Triage vor Umsetzungspruefung

Bevor losgelegt wird, klaere:
1. Welche Richtlinie — Umsetzungsfrist und Stand der nationalen Umsetzung bekannt?
2. Ist die Frist abgelaufen — wenn ja: unmittelbare Wirkung oder Staatshaftung pruefbar?
3. Hat der nationale Gesetzgeber den Umsetzungsspielraum ausgeschoepft oder ueberschossen (Gold-Plating)?
4. Besteht eine Auslegungsfrage ob das nationale Recht richtlinienkonform interpretiert werden kann?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette Richtlinienumsetzung

- **Art. 288 Abs. 3 AEUV** — Richtlinie: verbindliches Ziel; Form und Mittel den MS ueberlassen
- **Art. 4 Abs. 3 EUV** — Umsetzungspflicht; Loyalitaetsgebot
- **Art. 267 AEUV** — Vorabentscheidungsverfahren bei Auslegungsfragen
- **§ 4a TMG / § 29b UStG etc.** — nationale Umsetzungsgesetze (Bsp. DSGVO-Ergaenzungsgesetze)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Umsetzungspruefung Richtlinie

**Adressat:** Kanzlei-intern
**Tonfall:** Analytisch; Fristen pruefen

```
RICHTLINIENUMSETZUNGS-PRUEFUNG
Richtlinie: [RL 20XX/XX/EU — CELEX-Nr. / Kurztitel]
Umsetzungsfrist: [DATUM]
Stand nationale Umsetzung: [vollstaendig / unvollstaendig / nicht umgesetzt]
Relevante nationale Norm: [§ X Gesetz Y]

A. UMSETZUNGSPRUEFUNG
Umsetzungsfrist abgelaufen: [JA seit DATUM / NEIN — laeuft bis DATUM]
Korrekte Umsetzung: [JA / TEILWEISE — Luecke: [Beschreibung] / NEIN]

B. UNMITTELBARE WIRKUNG
Voraussetzungen (klar, unbedingt, verstreicht Frist): [erfuellt / nicht erfuellt]
Anwendung nur gg. Staat (vertikal): [JA / NEIN — Privatperson Gegner]

C. RICHTLINIENKONFORME AUSLEGUNG
Moeglich: [JA / contra legem-Grenze erreicht]
Ergebnis Auslegung: [...]

D. STAATSHAFTUNG (falls Umsetzung fehlt/fehlerhaft)
Qualifizierter Verstoß: [JA / NEIN]
Schaden: EUR [X]
Klage gegen: [Bundesrepublik vor LG Berlin (§ 839 BGB / EU-SH)]

E. VORLAGE EuGH (falls Auslegungsfrage)
Fragebeschreibung: [...]
Zustaendiges Gericht fuer Vorlage: [...]
```

## 2. `europarecht-simulation-behoerde-gericht`

**Fokus:** Verhandlung vor EU-Behoerde oder nationalem Gericht mit EU-Rechtsbezug simulieren und Argumentation testen. Art. 267 AEUV Art. 263 AEUV EuGH-Verfahren. Prüfraster: Argumente Gegenargumente Vorlageentscheidung Richterperspektive Schwachstellen. Output: Simulationsprotokoll Argumentation-Feinschliff. Abgrenzung: nicht für Klageentwuerfe (europarecht-klagearten-eugh).

# Simulation Behörde, Gericht und Kommission

## Zweck

Fiktive Verfahren trainieren Beihilfe, Richtlinienumsetzung, Vorlagefrage, Charta und Vertragsverletzung.

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

## Triage Simulation

Bevor losgelegt wird, klaere:
1. Wird eine Behoerden- oder Gerichts-Reaktion simuliert — welche Seite?
2. Welches Argument wird auf EU-Recht-Konformitaet geprueft?
3. Wie realistisch soll die Simulation sein — Planspiel oder praezise Einschaetzung?

## Output-Template: Simulations-Protokoll

```
SIMULATIONS-PROTOKOLL EU-RECHT
Datum: [DATUM] — Mandant: [NAME]

Simulierte Rolle: [BEHOERDE — [NAME] / GERICHT — [INSTANZ]]
EU-Recht-Bezug: [Art. X AEUV / VO / RL]
Rechtsfrage: [FORMULIERUNG]

SIMULIERTES ERGEBNIS
a) Aus Sicht Behoerde: [Bescheid-Ergebnis mit Begruendung]
b) Aus Sicht Gericht 1. Instanz: [Urteil und Begruendung]
c) Vorlage Art. 267 AEUV: [wahrscheinlich / nicht wahrscheinlich — Begründung]
d) Gegenargument Mandant: [...]

HANDLUNGSEMPFEHLUNG:
[...]
```

## 3. `europarecht-verordnung-beschluss-soft-law`

**Fokus:** EU-Verordnungen Beschluesse und Soft-Law-Instrumente einordnen und deren Verbindlichkeit prüfen. Art. 288 AEUV EU-Rechtsquellen. Prüfraster: Rechtsquellentyp Verbindlichkeit Direktwirkung nationaler Anpassungsbedarf zeitlicher Geltungsbereich. Output: Rechtsquellen-Einordnungs-Memo. Abgrenzung: nicht für Richtlinien (europarecht-richtlinie-umsetzung).

# Verordnung, Beschluss und Soft Law

## Zweck

Bindungswirkung, Adressat, Durchführungsrecht und Soft-Law-Wirkung werden sauber getrennt.

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

## Vertiefung: Abgrenzung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage Rechtsakt-Klassifikation

Bevor losgelegt wird, klaere:
1. Verordnung (unmittelbar anwendbar), Richtlinie (Umsetzung), Beschluss (individuell adressiert) oder Soft Law?
2. Ist Soft Law (Leitlinie, Mitteilung, Empfehlung) fuer den Mandanten faktisch bindend?
3. Koennte Soft Law anfechtbar sein (faktische Rechtswirkung)?

## Normen-Kette

- **Art. 288 AEUV** — Verordnung (allg. verbindl.), Richtlinie, Beschluss, Empfehlung, Stellungnahme
- **Art. 263 Abs. 1 AEUV** — Anfechtbarkeit von Beschluessen und Akten mit Rechtswirkung

## Output-Template: Rechtsakt-Einordnung

```
RECHTSAKT-EINORDNUNG
Rechtsakt: [CELEX-Nr. / Titel]
Kategorie: [ ] VO [ ] RL [ ] Beschluss [ ] Empfehlung [ ] Mitteilung
Verbindlichkeit: [allgemein / adressatenbezogen / keine]
Unmittelbare Anwendung: [JA / nein — Umsetzung bis DATUM]
Anfechtbarkeit Art. 263: [JA — faktische Rechtswirkung / NEIN]
```
