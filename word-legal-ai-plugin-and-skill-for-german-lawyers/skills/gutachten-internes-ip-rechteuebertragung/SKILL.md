---
name: gutachten-internes-ip-rechteuebertragung
description: "Gutachten Internes IP Rechteuebertragung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gutachten Internes IP Rechteuebertragung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Gutachten Internes IP Rechteuebertragung** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gutachten-memo-internes-drafting` | Internes Memo und Gutachten im Gutachtenstil. Standardstruktur: Sachverhalt knapp; Frage(n); Kurzantwort in einem Satz; rechtliche Bewertung im Gutachtenstil; Gesamtergebnis; Risiken und offene Punkte; Quellenverzeichnis. Anspruchsgrundlagenprüfung in der Reihenfolge Vertrag bis Bereicherung. Vier klassische Auslegungsmethoden plus verfassungs- und unionsrechtskonforme Auslegung. Mit Mustertext-Auszug eines Memos und typischen Drafting-Fehlern wie Subsumtion ohne Obersatz und Ergebnis vor Begründung. |
| `ip-rechteuebertragung-und-lizenzen` | Drafting von IP-Klauseln. Urheberrecht (UrhG) kennt keine vollständige Übertragung des Stammrechts (§ 29 UrhG); zulässig ist nur die Einräumung von Nutzungsrechten als einfache oder ausschließliche Lizenz mit räumlicher, zeitlicher und inhaltlicher Beschränkung. Marken und Patente sind dagegen vollständig übertragbar. Behandelt Software-Lizenzen mit Erschöpfungsgrundsatz (BGH UsedSoft), Sub-Lizenzen, Rückrufrechte nach § 41 UrhG und Open-Source-Compliance. Liefert Mustertexte für Lizenzklausel (Marke) und Urheberrechtsklausel (Werk und Software). |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Gutachten Internes IP Rechteuebertragung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gutachten-memo-internes-drafting`

**Fokus:** Internes Memo und Gutachten im Gutachtenstil. Standardstruktur: Sachverhalt knapp; Frage(n); Kurzantwort in einem Satz; rechtliche Bewertung im Gutachtenstil; Gesamtergebnis; Risiken und offene Punkte; Quellenverzeichnis. Anspruchsgrundlagenprüfung in der Reihenfolge Vertrag bis Bereicherung. Vier klassische Auslegungsmethoden plus verfassungs- und unionsrechtskonforme Auslegung. Mit Mustertext-Auszug eines Memos und typischen Drafting-Fehlern wie Subsumtion ohne Obersatz und Ergebnis vor Begründung.

# Gutachten und internes Memo

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

## 2. `ip-rechteuebertragung-und-lizenzen`

**Fokus:** Drafting von IP-Klauseln. Urheberrecht (UrhG) kennt keine vollständige Übertragung des Stammrechts (§ 29 UrhG); zulässig ist nur die Einräumung von Nutzungsrechten als einfache oder ausschließliche Lizenz mit räumlicher, zeitlicher und inhaltlicher Beschränkung. Marken und Patente sind dagegen vollständig übertragbar. Behandelt Software-Lizenzen mit Erschöpfungsgrundsatz (BGH UsedSoft), Sub-Lizenzen, Rückrufrechte nach § 41 UrhG und Open-Source-Compliance. Liefert Mustertexte für Lizenzklausel (Marke) und Urheberrechtsklausel (Werk und Software).

# IP-Rechteübertragung und Lizenzen

## Zweck

Dieser Skill unterstützt Sie beim Drafting von Klauseln, mit denen Rechte des Geistigen Eigentums (IP, Intellectual Property) übertragen oder lizenziert werden. Der wichtigste Befund vorab: Urheberrechte und Marken-/Patentrechte folgen unterschiedlicher Dogmatik. Wer beides nach demselben Schema regelt, riskiert nichtige Klauseln.

## Eingaben

- Welche Schutzrechte sind betroffen (Urheberrecht, Marke, Patent, Geschmacksmuster, Topographien, Geschäftsgeheimnis)?
- Soll übertragen oder lizenziert werden?
- Konstellation (Auftragsarbeit, Lieferantenwerk, Co-Development, Konzernlizenz, Open-Source-Komponenten).
- Räumlicher, zeitlicher und inhaltlicher Umfang der gewünschten Nutzung.
- Vergütungsstruktur (Einmalbetrag, royalty, gestaffelt).
- Sub-Lizenz-Bedarf? Übertragung der Lizenz an Konzerngesellschaften oder Erwerber?

## Rechtlicher und methodischer Rahmen

- **Urheberrecht (UrhG):**
 - § 29 I UrhG: Das Urheberrecht ist nicht übertragbar, mit Ausnahme der Übertragung von Todes wegen.
 - § 29 II UrhG: Zulässig sind die Einräumung von Nutzungsrechten (§ 31 UrhG), Rechtsgeschäfte über Urheberpersönlichkeitsrechte (begrenzt) und schuldrechtliche Einwilligungen.
 - § 31 UrhG: Einfache und ausschließliche Nutzungsrechte, räumlich, zeitlich, inhaltlich beschränkbar.
 - § 31a UrhG: Unbekannte Nutzungsarten benötigen Schriftform.
 - § 32 UrhG: Anspruch auf angemessene Vergütung.
 - § 34 UrhG: Übertragung von Nutzungsrechten nur mit Zustimmung des Urhebers, außer Betriebsübergang.
 - § 35 UrhG: Einräumung weiterer Nutzungsrechte (Sub-Lizenz) bei ausschließlichem Recht nur mit Zustimmung des Urhebers.
 - § 41 UrhG: Rückrufrecht wegen Nichtausübung.
 - § 69a ff. UrhG: Sonderregeln für Software, insbesondere § 69b UrhG (Computerprogramme im Arbeitsverhältnis: ausschließliches Nutzungsrecht beim Arbeitgeber).
- **Marke und Patent:**
 - § 27 MarkenG: Marke ist vollständig übertragbar.
 - § 30 MarkenG: Lizenz möglich (ausschließlich, einfach, räumlich, zeitlich, art-, mengen- oder qualitätsbezogen beschränkt).
 - § 15 PatG: Patent ist übertragbar, lizenzierbar.
- **Erschöpfungsgrundsatz Software:** BGH "UsedSoft" und EuGH-Rechtsprechung erlauben den Weiterverkauf erschöpfter Programmkopien; Klauselverbote des Weiterverkaufs erschöpfter Kopien sind unwirksam. Exakte Fundstelle vom Nutzer zu verifizieren.
- **Open-Source-Compliance:** Mit Open-Source-Komponenten verbundene Lizenzpflichten (insbesondere Copyleft bei GPL) können auf das Gesamtwerk durchschlagen. Drafting muss Open-Source-Inventar und Lizenzpflichten adressieren.
- **Arbeitsverhältnisse:** Computerprogramme nach § 69b UrhG; sonstige Werke außerhalb von Software: keine automatische Rechtseinräumung an den Arbeitgeber, vertragliche Regelung notwendig.
- **AGB-Recht:** Pauschale Buy-out-Klauseln in AGB sind unter § 307 BGB häufig unwirksam, insbesondere bei freischaffenden Urhebern.

## Ablauf / Checkliste

1. Schutzgegenstand identifizieren; bei Werken Werkqualität nach § 2 UrhG prüfen.
2. Übertragungs- vs. Lizenzmodell wählen, abhängig vom Schutzrecht.
3. Bei Urheberrecht: Nutzungsrechte vollständig spezifizieren (räumlich, zeitlich, inhaltlich, Verbreitungs-, Vervielfältigungs-, Bearbeitungs-, öffentliche Wiedergabe-Recht).
4. Einfache oder ausschließliche Lizenz wählen; Auswirkungen auf Sub-Lizenzfähigkeit (§ 35 UrhG) bedenken.
5. Unbekannte Nutzungsarten regeln (§ 31a UrhG: Schriftform und Widerrufsrecht).
6. Vergütung festlegen, ggf. Audit-Recht.
7. Sub-Lizenzrecht klarstellen, Konzernweitergabe, Übertragbarkeit nach § 34 UrhG.
8. Open-Source-Komponenten offenlegen, Inventar pflegen, Pflichten allokieren.
9. Rückrufrechte nach § 41 UrhG kontrahieren (Schutzfristen, Voraussetzungen).
10. Garantie und Haftung: Inhaber- und Freiheitsgarantie, IP-Indemnity (Freistellung wegen Schutzrechtsverletzung).
11. Beendigungsfolgen: Nutzungsrecht erlischt, Auslauf, Restbestand, Quellcode-Hinterlegung.

## Typische Drafting-Fehler

- "Sämtliche Urheberrechte werden übertragen": nichtig nach § 29 I UrhG; richtige Formulierung: ausschließliches, übertragbares, unterlizenzierbares Nutzungsrecht für alle bekannten Nutzungsarten.
- Pauschale "alle Nutzungsarten": Zweckübertragungslehre (§ 31 V UrhG) führt zu enger Auslegung, soweit nicht spezifiziert.
- Vergessen, Bearbeitungsrechte und Recht zur Übertragung an Dritte einzuräumen.
- Open-Source-Komponenten nicht offengelegt: Haftungsfalle für den Lieferanten.
- Sub-Lizenz ohne Zustimmung des Urhebers bei ausschließlicher Lizenz (§ 35 UrhG).
- Markenlizenz ohne Qualitätskontrollvorbehalt: Markenfunktion gefährdet (§ 30 MarkenG).
- Buy-out in AGB ohne Vergütungsregelung: Verstoß gegen § 32 UrhG.

## Ausgabeformat

- Klauselentwürfe getrennt nach Schutzrechtstyp.
- Querverweis-Architektur (Definitionen, Anlagen mit Schutzrechtsverzeichnis).
- Risikoliste mit Open-Source-Hinweisen.
- Vergütungs- und Audit-Anhänge nach Bedarf.

## Beispiel

Mustertext (Urheberrechtsklausel, Auftragswerk, B2B):

> § X Nutzungsrechte
> (1) Der Auftragnehmer räumt dem Auftraggeber an allen im Rahmen dieses Vertrages geschaffenen Werken (einschließlich Vorstudien, Entwürfen und Zwischenergebnissen) das ausschließliche, zeitlich, räumlich und inhaltlich unbeschränkte, übertragbare und unterlizenzierbare Nutzungsrecht für sämtliche bekannten Nutzungsarten ein. Eingeschlossen sind insbesondere Vervielfältigung, Verbreitung, öffentliche Wiedergabe einschließlich öffentlicher Zugänglichmachung, Bearbeitung und Umgestaltung.
> (2) Für unbekannte Nutzungsarten gilt § 31a UrhG; der Auftragnehmer wird hierzu auf Anfrage eine gesonderte Vereinbarung in Schriftform abschließen.
> (3) Das Recht zur Bearbeitung schließt das Recht zur Verbindung mit eigenen oder fremden Werken ein. Eine Namensnennung des Auftragnehmers erfolgt nur auf gesonderte Vereinbarung.
> (4) Mit der vertraglich vereinbarten Vergütung sind alle Nutzungsrechte abgegolten; § 32 UrhG bleibt unberührt.

Mustertext (Markenlizenz, einfache Lizenz, B2B):

> § Y Markenlizenz
> (1) Der Lizenzgeber räumt dem Lizenznehmer für die Vertragsdauer eine einfache, nicht übertragbare, nicht unterlizenzierbare Lizenz an der Marke "ABC" (DPMA-Registernummer ...) für das Gebiet der Bundesrepublik Deutschland zur Kennzeichnung der unter Anlage 1 aufgeführten Produkte ein.
> (2) Der Lizenznehmer verwendet die Marke ausschließlich in der eingetragenen Form. Der Lizenzgeber kann die Qualität der lizenzierten Waren prüfen und Mängel beanstanden.

## Querverweise

- `definitionen-klauseln-stringent` – Definitionen für "Schutzrechte" und "Werk".
- `boilerplate-klauseln-katalog` – Übertragbarkeit und Rechtsnachfolge.
- `geheimhaltung-nda-vertraulichkeit` – Schutz nicht eingetragenen Know-hows.
- `agb-konforme-klauseln-305-310-bgb` – Buy-out-Risiko in AGB.

## Quellen (Stand 05/2026)

- §§ 2, 29, 31, 31a, 32, 34, 35, 41, 69a ff. UrhG.
- §§ 27, 30 MarkenG; § 15 PatG.
- BGH "UsedSoft" und EuGH-Rechtsprechung zum Erschöpfungsgrundsatz Software sind vom Nutzer fundstellengenau zu verifizieren.
- Zitierweise: `references/zitierweise.md`.
