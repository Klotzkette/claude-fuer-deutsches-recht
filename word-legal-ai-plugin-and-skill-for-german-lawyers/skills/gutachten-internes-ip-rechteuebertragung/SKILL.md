---
name: gutachten-internes-ip-rechteuebertragung
description: "Internes Memo und Gutachten im Gutachtenstil. Standardstruktur: Sachverhalt knapp; Frage(n); Kurzantwort in einem Satz; rechtliche Bewertung im Gutachtenstil; Gesamtergebnis; Risiken und offene Punkte; Quellenverzeichnis. Anspruchsgrundlagenprüfung in der Reihenfolge Vertrag bis Bereicherung. Vier klassische Auslegungsmethoden plus verfassungs- und unionsrechtskonforme Auslegung. Mit Mustertext-Auszug eines Memos und typischen Drafting-Fehlern wie Subsumtion ohne Obersatz und Ergebnis vor Begründung im Word Legal Ai Plugin And Skill For German Lawyers: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Gutachten und internes Memo

## Arbeitsbereich

Internes Memo und Gutachten im Gutachtenstil. Standardstruktur: Sachverhalt knapp; Frage(n); Kurzantwort in einem Satz; rechtliche Bewertung im Gutachtenstil; Gesamtergebnis; Risiken und offene Punkte; Quellenverzeichnis. Anspruchsgrundlagenprüfung in der Reihenfolge Vertrag bis Bereicherung. Vier klassische Auslegungsmethoden plus verfassungs- und unionsrechtskonforme Auslegung. Mit Mustertext-Auszug eines Memos und typischen Drafting-Fehlern wie Subsumtion ohne Obersatz und Ergebnis vor Begründung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Das interne Memo ist die Standard-Antwortform auf juristische Mandantenfragen. Es zwingt zur sauberen Trennung von Sachverhalt, Frage und rechtlicher Bewertung. Es ist die Grundlage für jeden weiteren Schriftsatz, jedes Beratungsgespräch und jeden Vergleichsvorschlag. Das Memo trägt seine Quellen und ist auditfähig.

Dieser Skill operationalisiert die in der Repository-CLAUDE.md vorgesehene Standardstruktur. Er führt durch den Aufbau, gibt einen Mustertext-Auszug und schützt vor den klassischen Drafting-Fehlern.

## Eingaben

- Mandantenfrage (eine oder wenige präzise Fragen)
- Sachverhalt (knapp; eigentliche Mandatsakten verbleiben in der Akte)
- Adressat (Mandant, Partner-Anwältin, Rechtsabteilung, Gericht)
- Rechtsgebiet
- Frist und Vertraulichkeitsstufe
- Vorhandene Quellen (Verträge, Korrespondenz, Vermerke)

## Rechtlicher und methodischer Rahmen

- Standardstruktur nach CLAUDE.md: Sachverhalt, Frage(n), Kurzantwort, rechtliche Bewertung, Gesamtergebnis, Risiken und offene Punkte, Quellenverzeichnis.
- Gutachtenstil: Obersatz, Definition, Subsumtion, Ergebnis je Tatbestandsmerkmal. Ergebnis steht am Ende.
- Anspruchsgrundlagenprüfung in der Reihenfolge: Vertrag, c.i.c., Geschäftsführung ohne Auftrag, dingliche Ansprüche, Delikt, Bereicherung.
- Auslegungsmethoden: grammatikalisch, systematisch, historisch, teleologisch; zusätzlich verfassungskonform (Art. 1 Abs. 3 GG) und unionsrechtskonform (Art. 4 Abs. 3 EUV).
- Quellen nach `references/zitierweise.md`. Keine Kommentar- oder Aufsatzfundstellen aus Modellwissen.
- § 43a BRAO und § 203 StGB für Vertraulichkeit; Memos sind interne Arbeitsergebnisse.

## Ablauf / Checkliste

1. **Sachverhalt strukturieren.** Chronologisch oder thematisch. Tatsachen nur, soweit für die Frage relevant.
2. **Frage(n) präzise formulieren.** Eine Frage pro Anspruch. Mehrere Fragen nummerieren.
3. **Kurzantwort schreiben.** Ein bis zwei Sätze. Sie sagt das Ergebnis ohne Begründung.
4. **Anspruchsgrundlagen identifizieren.** Reihenfolge Vertrag bis Bereicherung einhalten.
5. **Pro Anspruchsgrundlage Gutachtenstil.** Obersatz nennt Norm und Tatbestandsmerkmale. Jedes Merkmal wird definiert und subsumiert. Zwischenergebnis je Merkmal.
6. **Auslegungsmethoden anwenden, soweit nötig.** Vier klassische Methoden plus verfassungs- und unionsrechtskonforme Auslegung.
7. **Gesamtergebnis.** Knappe Aussage zur juristischen Lage.
8. **Risiken und offene Punkte.** Was wir nicht wissen, was anders gesehen werden kann, was noch zu klären ist.
9. **Quellenverzeichnis.** Normen, verifizierte Rechtsprechung, vom Nutzer bereitgestellte Literatur.

### Struktur des Memos

| Abschnitt | Pflicht? | Stil |
|---|---|---|
| 1. Sachverhalt | Pflicht | knapp; ohne Wertung |
| 2. Frage(n) | Pflicht | präzise; nummeriert |
| 3. Kurzantwort | Pflicht | ein bis zwei Sätze |
| 4. Rechtliche Bewertung | Pflicht | Gutachtenstil |
| 5. Gesamtergebnis | Pflicht | drei bis fünf Sätze |
| 6. Risiken und offene Punkte | Pflicht | Liste |
| 7. Quellenverzeichnis | Pflicht | nach zitierweise.md |

## Typische Drafting-Fehler

- **Subsumtion ohne Obersatz.** Wer zuerst subsumiert, ohne den Tatbestand der Norm zu nennen, springt die Methodik.
- **Definitionen fehlen.** Jedes auslegungsbedürftige Merkmal verlangt eine Definition vor der Subsumtion.
- **Ergebnis vor Begründung.** Im Gutachtenstil steht das Ergebnis am Ende; nur in der Kurzantwort am Anfang.
- **"Im Ergebnis"-Floskel ohne Subsumtion.** "Im Ergebnis ist davon auszugehen, dass" ersetzt keine Prüfung.
- **Reihenfolgefehler.** Bereicherung vor Vertrag prüfen ist methodisch falsch.
- **Quellenarmut.** Eine juristische Aussage ohne Beleg ist eine Vermutung.
- **Sachverhaltsausschmückung.** Memo ist kein Roman. Tatsachen, die nicht relevant sind, gehören in die Akte.

## Ausgabeformat

- Vollständiges Memo nach Standardstruktur.
- Bei Konzeptphase: nur Kurzantwort plus Skizze der Prüfungsschritte.
- Quellenverzeichnis ans Ende.

## Beispiele

### Mustertext-Auszug Memo (gekürzt)

```
INTERNES MEMO

An: RA Stern (Akte 2026 023)
Von: RA Beispiel
Datum: 30. Mai 2026
Betreff: Anspruch der Mandantin auf Kaufpreis 25.000 Euro

1. Sachverhalt

Unsere Mandantin Frau Muster schloss am 15. Januar 2026 mit der Beklagt
GmbH einen Kaufvertrag über zehn Maschinen Typ A-100 zum Gesamtpreis
von 25.000 Euro netto. Die Lieferung erfolgte am 1. Februar 2026. Eine
Zahlung ist nicht erfolgt. Die Beklagt GmbH macht geltend, drei Maschinen
seien bei Lieferung mit Korrosionsschäden behaftet gewesen.

2. Frage

Hat die Mandantin gegen die Beklagt GmbH einen Anspruch auf Zahlung des
Kaufpreises in Höhe von 25.000 Euro?

3. Kurzantwort

Ja, dem Grunde nach. Die Beklagte kann jedoch ein Zurückbehaltungsrecht
nach § 320 BGB geltend machen, soweit eine Mangelhaftigkeit dreier
Maschinen bewiesen wird.

4. Rechtliche Bewertung

a) Anspruch aus § 433 Abs. 2 BGB

Die Mandantin könnte gegen die Beklagte einen Anspruch auf Zahlung des
Kaufpreises aus § 433 Abs. 2 BGB haben.

aa) Wirksamer Kaufvertrag

Voraussetzung ist ein wirksamer Kaufvertrag. Ein Kaufvertrag setzt zwei
übereinstimmende Willenserklärungen gerichtet auf die Verschaffung einer
Sache gegen Zahlung eines Kaufpreises voraus (§ 433 Abs. 1, Abs. 2 BGB).

Hier liegt eine schriftliche Vereinbarung vom 15. Januar 2026 vor.
Beide Parteien haben unterzeichnet. Ein wirksamer Kaufvertrag ist damit
zustande gekommen.

bb) Fälligkeit

Die Kaufpreisforderung ist mit Lieferung am 1. Februar 2026 fällig
geworden (§ 271 Abs. 1 BGB). Eine Stundungsabrede wurde nicht behauptet.

cc) Einrede des nicht erfüllten Vertrags (§ 320 BGB)

Die Beklagte kann jedoch das Zurückbehaltungsrecht aus § 320 BGB
geltend machen, wenn ein Mangel nach §§ 433 Abs. 1 Satz 2, 434 BGB
vorliegt. Hierzu wäre die Behauptung der Korrosionsschäden zu beweisen.

[...weitere Prüfung der Anspruchsgrundlagen und Einreden gekürzt...]

5. Gesamtergebnis

Dem Grunde nach besteht der Anspruch. Im Prozess wird die Beklagte ein
Zurückbehaltungsrecht aus § 320 BGB geltend machen. Die Beweislast für
die Mangelhaftigkeit liegt nach § 363 BGB bei der Beklagten, soweit die
Mandantin die Erfüllung als Lieferung beweisen kann.

6. Risiken und offene Punkte

- Beweislage zur Mangelhaftigkeit. Mandantin hat keine eigene Anlage
 zur Mangelfreiheit der gelieferten Maschinen.
- Die Mängelanzeige der Beklagten erfolgte am 8. Februar 2026. Frist
 nach § 377 HGB einhalten, falls Handelskauf.
- Mögliche Aufrechnung mit Gegenforderung der Beklagten nicht beziffert.

7. Quellenverzeichnis

- §§ 271 Abs. 1, 320, 363, 433 BGB; gesetze-im-internet.de.
- § 377 HGB für Untersuchungs- und Rügepflicht bei Handelskauf.
- references/methodik-buergerliches-recht.md
- BGH-Rechtsprechung zur Beweislast bei behaupteten Mängeln
 (vom Nutzer zu verifizieren).
```

## Querverweise

- `klage-drafting-253-zpo` als nächster Schritt nach Bejahung des Anspruchs
- `klageerwiderung-substantiiertes-bestreiten` als Verteidigungspendant
- `anwaltsschreiben-aussergerichtlich` für die Mandanten- oder Gegenseitenkommunikation
- `drafting-prinzipien-klarheit-bestimmtheit-praezision` für sprachliche Hygiene

## Quellen (Stand 05/2026)

- `references/methodik-buergerliches-recht.md` für Anspruchsgrundlagenprüfung und Auslegungsmethoden.
- CLAUDE.md des Repositories für die Standardstruktur des Memos.
- `references/zitierweise.md` für Belegpflicht.
- § 43a BRAO und § 203 StGB für Vertraulichkeit interner Memos.
