---
name: drafting-prinzipien-finaler-writing
description: "Drafting Prinzipien Finaler Writing: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Drafting Prinzipien Finaler Writing

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Drafting Prinzipien Finaler Writing** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `drafting-prinzipien-klarheit-bestimmtheit-praezision` | Die drei Leitwerte juristischen Drafting sauber operationalisieren. Klarheit (Adressat versteht), Bestimmtheit (Subsumtion moeglich; § 253 Abs. 2 Nr. 2 ZPO; AGB-Transparenzgebot § 307 Abs. 1 Satz 2 BGB) und Praezision (kein ueberfluessiges Wort) als pruefbare Anforderungen umsetzen. Mit Anti-Beispielen aus typischen Klauselsuenden, Faustregel max 25 Woerter je Satz, Aktiv vor Passiv und einer Umformulierungstabelle schwammig zu praezise. |
| `finaler-writing-quality-gate` | Finales Quality Gate für juristische Texte vor Versand. Prüft Rechtsfrage, Antrag oder Klauselzweck, Adressat, Stil, Zitate, Normen, Anlagen, Beweise, Fristen, Platzhalter, Zahlen, Namen, Datenschutz, Metadaten, Word-Hygiene und Versandfassung. Liefert Freigabeampel und letzte Reparaturliste. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Drafting Prinzipien Finaler Writing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `drafting-prinzipien-klarheit-bestimmtheit-praezision`

**Fokus:** Die drei Leitwerte juristischen Drafting sauber operationalisieren. Klarheit (Adressat versteht), Bestimmtheit (Subsumtion moeglich; § 253 Abs. 2 Nr. 2 ZPO; AGB-Transparenzgebot § 307 Abs. 1 Satz 2 BGB) und Praezision (kein ueberfluessiges Wort) als pruefbare Anforderungen umsetzen. Mit Anti-Beispielen aus typischen Klauselsuenden, Faustregel max 25 Woerter je Satz, Aktiv vor Passiv und einer Umformulierungstabelle schwammig zu praezise.

# Drafting-Prinzipien: Klarheit, Bestimmtheit, Praezision

## Zweck

Drei Werte tragen jedes juristische Dokument: Klarheit, Bestimmtheit und Praezision. Sie sind keine Stilvorlieben, sondern Wirksamkeitsfaktoren. Eine unklare Vertragsklausel ist nach § 305c Abs. 2 BGB im Zweifel gegen den Verwender auszulegen. Ein unbestimmter Klageantrag ist nach § 253 Abs. 2 Nr. 2 ZPO unzulaessig. Eine intransparente AGB-Klausel ist nach § 307 Abs. 1 Satz 2 BGB unwirksam.

Dieser Skill operationalisiert die drei Werte als pruefbare Anforderungen. Sie liefern keine philosophische Begruendung, sondern eine Checkliste pro Satz, pro Klausel, pro Antrag. Er verweist auf die Fachmodule, sobald die Pruefung Schwerpunkte ergibt.

## Eingaben

- Klausel-, Antrags- oder Satzentwurf, der gepruefet werden soll
- Kontext: Vertrag (B2B oder B2C), AGB-Verwender, Klageantrag, Anwaltsschreiben
- Optional: Adressat (Mandant, Gegenseite, Gericht)

## Rechtlicher und methodischer Rahmen

- § 253 Abs. 2 Nr. 2 ZPO: Bestimmtheit des Klageantrags. Wer einen unbestimmten Antrag stellt, riskiert die Unzulaessigkeit.
- § 307 Abs. 1 Satz 2 BGB: Transparenzgebot. AGB-Klauseln muessen klar und verstaendlich sein.
- § 305c Abs. 2 BGB: Unklarheitenregel zulasten des Verwenders.
- § 138 Abs. 2 ZPO: Substantiierungslast im Prozess; Praezision dient der Substantiierungslast.
- Methode: Gutachtenstil verlangt Begruendung, Urteilsstil verlangt Knappheit. Beide verlangen Bestimmtheit.

## Ablauf / Checkliste

1. **Klarheit pruefen.** Versteht der Adressat den Satz beim ersten Lesen? Ohne Rueckfrage? Wenn nicht, umformulieren.
2. **Bestimmtheit pruefen.** Ist der Tatbestand subsumtionsfaehig? Sind die Rechtsfolgen eindeutig?
3. **Praezision pruefen.** Streichen Sie jedes Wort, das nichts traegt. "Saemtliche Vertragsparteien" ist nicht praeziser als "die Parteien".
4. **Satzlaenge messen.** Faustregel: maximal 25 Woerter pro Satz. Ueberlange Saetze trennen.
5. **Aktiv vor Passiv.** "Der Verkaeufer liefert" statt "es wird vom Verkaeufer geliefert".
6. **Defined Terms anwenden.** Ein Begriff einmal definieren, dann konsistent verwenden. Siehe `definitionen-klauseln-stringent`.
7. **Doppelte Negation streichen.** "Nicht ausgeschlossen ist" wird zu "moeglich ist".
8. **Konjunktiv vermeiden.** Operative Klauseln im Indikativ. Konjunktiv nur fuer Bedingungssaetze.

### Anti-Beispiele und Umformulierung

| Schwammig | Praezise |
|---|---|
| "Die Parteien werden bestrebt sein, sich zu verstaendigen." | "Die Parteien verhandeln innerhalb von 14 Tagen nach schriftlicher Anzeige." |
| "Soweit moeglich, ist die Leistung rechtzeitig zu erbringen." | "Die Leistung ist bis zum 31. Maerz 2027 zu erbringen." |
| "Eine angemessene Frist." | "Eine Frist von 14 Tagen." |
| "Im Falle des Falles." | "Bei Eintritt der in § 5 genannten Bedingung." |
| "Alle damit zusammenhaengenden Kosten." | "Saemtliche Kosten der Vertragsdurchfuehrung, einschliesslich Steuern und Notarkosten." |
| "Es wird darauf hingewiesen, dass" | streichen |
| "Es ist zu beachten, dass" | streichen |

### Bestimmtheitsmuster

Jeder operative Satz traegt Antwort auf vier Fragen:

1. Wer (Subjekt der Pflicht)
2. Was (Leistungspflicht oder Unterlassungspflicht)
3. Wann (Frist oder Bedingung)
4. Wie (Form, Ort, Modalitaet)

## Typische Drafting-Fehler

- **Floskel-Inflation.** "Saemtliche im Vorstehenden bezeichneten" tut nichts. Streichen.
- **Modalfehler.** "kann" statt "muss"; "soll" statt "ist verpflichtet". Modalverben sind keine Stilfrage.
- **Schwammige Standards.** "angemessen", "ortsueblich", "branchenueblich" nur dort, wo gesetzlich vorgegeben oder unausweichlich.
- **Verkettete Konjunktive.** "wuerde", "haette", "koennte" in operativen Klauseln.
- **Substantivketten.** "Vertragsdurchfuehrungskostenuebernahmeverpflichtung" zerlegen.
- **Mehrfach-Negationen.** "nicht ohne vorherige Zustimmung" wird zu "nur mit vorheriger Zustimmung".

## Ausgabeformat

- Bewerteter Originaltext mit Markierungen je Satz: K (Klarheit), B (Bestimmtheit), P (Praezision).
- Umformulierter Vorschlag.
- Vergleichstabelle alt zu neu.

## Beispiel

**Original:** "Im Falle, dass die Lieferung nicht ordnungsgemaess erfolgt, koennen vom Besteller alle ihm hieraus erwachsenden Anspruechee gegenueber dem Lieferanten geltend gemacht werden, wobei der Lieferant darauf hingewiesen wird, dass derartige Anspruechee insbesondere auch Schadensersatzanspruechee umfassen koennen."

**Pruefung:**
- Klarheit: schlecht. 41 Woerter, mehrere Einschuebe.
- Bestimmtheit: schwach. "nicht ordnungsgemaess" ohne Definition. "alle Anspruechee" ohne Aufzaehlung.
- Praezision: schlecht. "wobei der Lieferant darauf hingewiesen wird" ist Lehrbuchprosa, keine Klausel.

**Umformulierung:** "Liefert der Lieferant mangelhaft oder verspaetet, kann der Besteller die Rechte aus § 7 (Maengelhaftung) und § 8 (Verzug) geltend machen. Schadensersatzanspruechee bleiben unberuehrt."

**Resultat:** 31 Woerter in zwei Saetzen. Tatbestand und Rechtsfolge sind getrennt. Verweise sind eindeutig.

## Querverweise

- `definitionen-klauseln-stringent`
- `anspruchsgrundlage-und-rechtsfolgen-klauseln`
- `transparenzgebot-307-bgb` (Fachmodul fuer AGB-Transparenz)
- `stil-und-ton-juristische-texte`

## Quellen (Stand 05/2026)

- § 253 Abs. 2 Nr. 2 ZPO; § 305c Abs. 2 BGB; § 307 Abs. 1 Satz 2 BGB; § 138 Abs. 2 ZPO; siehe gesetze-im-internet.de.
- Rechtsprechung zum AGB-Transparenzgebot: vom Nutzer zu verifizieren. Keine Aktenzeichen aus Modellwissen.
- `references/zitierweise.md` fuer Belegpflicht.

## 2. `finaler-writing-quality-gate`

**Fokus:** Finales Quality Gate für juristische Texte vor Versand. Prüft Rechtsfrage, Antrag oder Klauselzweck, Adressat, Stil, Zitate, Normen, Anlagen, Beweise, Fristen, Platzhalter, Zahlen, Namen, Datenschutz, Metadaten, Word-Hygiene und Versandfassung. Liefert Freigabeampel und letzte Reparaturliste.

# Finaler Writing Quality Gate

## Zweck

Dieser Skill ist der letzte Blick vor Versand. Er prüft nicht noch einmal alles dogmatisch von vorne, sondern fragt: Kann dieser Text jetzt so an Mandant, Gericht, Gegenseite oder Partnerin gehen?

## Ampelprüfung

| Ampel | Bedeutung |
|---|---|
| Grün | sendefähig nach kleiner Schlusskontrolle |
| Gelb | sendefähig nach konkreten Reparaturen |
| Rot | nicht versenden; Risiko, Fehler oder Lücke zu groß |

## Prüffelder

1. **Zweck:** Ist klar, was der Text erreichen soll?
2. **Adressat:** Passt Ton und Tiefe?
3. **Rechtsanker:** Sind Normen, Klauseln und Begriffe korrekt und nötig?
4. **Zitate:** Gibt es nur überprüfbare Rechtsprechung mit Gericht, Datum und Aktenzeichen?
5. **Sachverhalt:** Stimmen Namen, Daten, Beträge, Fristen und Rollen?
6. **Belege:** Stimmen Anlagenverweise und Beweisangebote?
7. **Struktur:** Ergebnis vorne, keine Wiederholungen, sinnvolle Überschriften.
8. **Sprache:** Keine Polemik, keine Platzhalter, keine leeren Floskeln.
9. **Word:** Formatvorlagen, Nummerierung, Track Changes, Kommentare, Metadaten.
10. **Versand:** richtige Fassung, richtiger Dateiname, richtige Anlagen.

## Harte Stopper

- Platzhalter im Text.
- Unverifizierte Rechtsprechungsfundstelle.
- Falscher Mandantenname oder falsche Parteirolle.
- Unklare Frist.
- Sichtbare interne Kommentare, wenn Clean Version versendet werden soll.
- Widerspruch zwischen Antrag und Begründung.
- Anlagenverweis auf nicht vorhandene Anlage.

## Output

```text
Freigabeampel: Gelb

Vor Versand reparieren:
1. ...
2. ...
3. ...

Kann danach raus als:
- clean PDF
- redline DOCX
- Mandantenmemo
```

## Querverweise

- `word-dokument-finish-und-layout`
- `deutscher-kanzleistil-kalibrieren`
- `schriftsatz-ueberarbeiten-richterlesbar`
- `englischer-vertrag-deutsches-recht`


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
