---
name: beweiswuerdigung-richter-cisg-dsgvo
description: "Beweiswuerdigung Richter CISG DSGVO: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beweiswuerdigung Richter CISG DSGVO

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beweiswuerdigung Richter CISG DSGVO** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beweiswuerdigung-mit-richter-input` | Strukturierte Beweiswürdigung nach § 286 ZPO schreiben: Richter hat Beweise erhoben und will Entscheidungsgründe-Abschnitt verfassen. Normen: § 286 ZPO (freie Beweiswürdigung), § 261 ZPO (Beweislast), §§ 414 ff. ZPO (Sachverständige). Prüfraster: Glaubwürdigkeit, Glaubhaftigkeit, Aussagekonstanz, Realkennzeichen, Widersprueche, Sachverständigen-Bewertung. Output Beweiswürdigung-Abschnitt für Entscheidungsgründe. Abgrenzung: Beweisbeschluss vorher siehe beweisbeschluss-vorbereiten; Entscheidungsgründe gesamt siehe entscheidungsgründe-zivil-schreiben. |
| `cisg-pruefen` | UN-Kaufrecht (CISG) auf Anwendbarkeit und Eingreifen prüfen: Internationaler Kaufvertrag mit Auslandsbezug und Vertragsstreit. Normen: CISG Art. 1-6 (Anwendungsbereich), Art. 25 (wesentliche Vertragsverletzung), Art. 35 (Vertragsmäßigkeit), Art. 38-39 (Untersuchungs-/Ruegeobliegenheit), Art. 49 (Aufhebung). Prüfraster: sachlicher/persoenlicher/räumlicher/zeitlicher Anwendungsbereich, Ausschluss Art. 6, Rechtsbehelfe. Output CISG-Prüfschema, Anspruchs-Memo. Abgrenzung: IPR-Fragen siehe internationales-privatrecht; Incoterms siehe incoterms-und-gefahruebergang. |
| `dsgvo-rechtswidriges-produkt` | Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit prüfen: Richter oder Anwalt muss beurteilen ob Smartglasses oder IoT-Produkt DSGVO-konform ist. Normen: Art. 3 DSGVO (räumlicher Anwendungsbereich), Art. 5 Abs. 1 lit. c (Datensparsamkeit), Art. 6 (Rechtsgrundlage), Art. 9 (biometrische Daten), Art. 13-14 (Informationspflichten), Art. 44 ff. (Drittlandtransfer), Art. 22 (automatisierte Entscheidung). Prüfraster: Anwendbarkeit, Rechtsgrundlage, Sonderkateg. Daten, Drittlandtransfer. Output DSGVO-Prüfschema mit Ergebnis und Empfehlung. Abgrenzung: allgemeine DSGVO-Beratung siehe datenschutzrecht-Plugin; DSA siehe dsa-dma-Plugin. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Beweiswuerdigung Richter CISG DSGVO**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beweiswuerdigung-mit-richter-input`

**Fokus:** Strukturierte Beweiswürdigung nach § 286 ZPO schreiben: Richter hat Beweise erhoben und will Entscheidungsgründe-Abschnitt verfassen. Normen: § 286 ZPO (freie Beweiswürdigung), § 261 ZPO (Beweislast), §§ 414 ff. ZPO (Sachverständige). Prüfraster: Glaubwürdigkeit, Glaubhaftigkeit, Aussagekonstanz, Realkennzeichen, Widersprueche, Sachverständigen-Bewertung. Output Beweiswürdigung-Abschnitt für Entscheidungsgründe. Abgrenzung: Beweisbeschluss vorher siehe beweisbeschluss-vorbereiten; Entscheidungsgründe gesamt siehe entscheidungsgründe-zivil-schreiben.

# Beweiswürdigung mit haendischem Richter-Input

Die Beweiswürdigung ist Kernkompetenz der Richterin oder des Richters. Sie laesst sich nicht automatisieren - aber strukturieren.


## Triage zu Beginn

1. Welche Beweismittel wurden erhoben — Zeugen, Sachverständiger, Augenschein, Urkunden?
2. Hat die Richterin/der Richter konkrete Eindrücke zur Glaubwürdigkeit der Zeugen?
3. Widersprechen sich Zeugenaussagen oder Urkunde und Aussage?
4. Ist das Sachverständigengutachten vollständig oder besteht Ergänzungsbedarf (§ 411 ZPO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026: BGH VI ZR 96/11 geloescht – AZ auf dejure.org nicht auffindbar (NOT_FOUND). BGH VI ZR 113/17 korrigiert – Thema war falsch angegeben (Parteivernehmung § 448 ZPO statt Beweismaß § 287 ZPO) und NJW-Fundstelle korrigiert (2019, 2092 statt 2019, 1668). -->

## Zentrale Normen

- § 286 ZPO — freie Beweiswürdigung, Vollüberzeugung
- § 313 Abs. 2 S. 2 ZPO — Bezugnahme auf Aussagen und Gutachten im Tatbestand
- § 373 ff. ZPO — Zeugenbeweis
- § 402, 411 ZPO — Sachverständiger, Ergänzungsgutachten
- § 448 ZPO — Parteivernehmung von Amts wegen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Beweismittel auflisten:** chronologische Liste aller erhobenen Beweismittel aus dem Protokoll.
2. **Richter-Input einholen (MANUELL):** Richterin/Richter gibt strukturiert ein:
 - Glaubwürdigkeit jedes Zeugen (Eigeninteresse, persönlicher Eindruck)
 - Glaubhaftigkeit der Aussage (Konstanz, Detailreichtum, Realkennzeichen)
 - Widersprüche zu anderen Beweismitteln
3. **Würdigung formulieren:** Aus dem Input vollständige Sätze für die Entscheidungsgründe.
4. **Bezugnahme einfügen:** Verweis auf Protokoll und Gutachten nach § 313 Abs. 2 S. 2 ZPO.
5. **Feststellung zusammenfassen:** "Das Gericht hat sich davon überzeugt, dass ..."

## Output-Template

**Adressat:** Entscheidungsgründe → Abschnitt Beweiswürdigung — Tonfall: sachlich-juristisch

```
## Beweiswürdigung

Das Gericht hat die Klägerin (Parteivernehmung, Protokoll v. [DATUM]) und die Zeugen
[ZEUGE1] und [ZEUGE2] vernommen sowie das schriftliche Sachverständigengutachten
des Sachverständigen [NAME] v. [DATUM] verwertet.

Der Zeuge [ZEUGE1] hat ausgesagt, [ZUSAMMENFASSUNG]. Das Gericht hält diese Aussage
für glaubhaft. Sie war in sich konsistent, detailreich und widersprach nicht den
urkundlichen Belegen (Anlage K3). Eigeninteresse des Zeugen war nicht erkennbar.

Dem Sachverständigengutachten folgt das Gericht, soweit es [PUNKT]. Im Übrigen
hat der Sachverständige in seiner Ergänzung v. [DATUM] klargestellt, dass [PUNKT].

Das Gericht stellt fest: [FESTGESTELLTE TATSACHE].
```

## Vorgehen

1. **Schritt 1 (automatisierbar)**: Beweismittel sortieren - Zeuge / Sachverständiger / Augenschein / Urkunde / Parteivernehmung. Inhalte aus dem Sitzungsprotokoll übernehmen.
2. **Schritt 2 (haendisch)**: Die Richterin / der Richter trifft die Würdigung. Das Plugin fragt strukturiert ab:
 - **Glaubwürdigkeit des Zeugen**: persönliche Verhältnisse, Eigeninteresse, Belastungsmotivation
 - **Glaubhaftigkeit der Aussage**: Aussagekonstanz, Detailreichtum, Realkennzeichen, raumzeitliche Verknuepfungen, ungewoehnliche Detailangaben, Selbstkorrekturen, eigene Beteiligung
 - **Widersprüche** zu anderen Beweismitteln / Akten
3. **Schritt 3 (automatisierbar)**: Aus der Würdigung den Beweiswürdigungsteil der Entscheidungsgründe formulieren - in vollständigen Sätzen, mit Bezug auf die konkrete Beweisaufnahme.

## Form

Im Urteil immer:
- klare Aussage zur Beweiserhebung
- konkrete Inhaltsangabe der Aussage (kurz)
- die Würdigung mit den oben genannten Kriterien
- Ergebnis (festgestellt / nicht festgestellt)

## Bezugnahme

Auf das Sitzungsprotokoll und auf das Sachverständigengutachten ist nach Paragraf 313 II 2 ZPO konkret Bezug zu nehmen.

## Output

Strukturierte Datei `beweiswuerdigung.md` mit den Aussagen, der Würdigung und der zusammenfassenden Feststellung.

## 2. `cisg-pruefen`

**Fokus:** UN-Kaufrecht (CISG) auf Anwendbarkeit und Eingreifen prüfen: Internationaler Kaufvertrag mit Auslandsbezug und Vertragsstreit. Normen: CISG Art. 1-6 (Anwendungsbereich), Art. 25 (wesentliche Vertragsverletzung), Art. 35 (Vertragsmäßigkeit), Art. 38-39 (Untersuchungs-/Ruegeobliegenheit), Art. 49 (Aufhebung). Prüfraster: sachlicher/persoenlicher/räumlicher/zeitlicher Anwendungsbereich, Ausschluss Art. 6, Rechtsbehelfe. Output CISG-Prüfschema, Anspruchs-Memo. Abgrenzung: IPR-Fragen siehe internationales-privatrecht; Incoterms siehe incoterms-und-gefahruebergang.

# CISG-Prüfung

Das UN-Kaufrecht (Wiener Übereinkommen vom 11. April 1980 über Verträge über den internationalen Warenkauf) ist ein direkt anwendbares Einheitskaufrecht und geht dem IPR vor, soweit es eingreift.


## Triage zu Beginn

1. Sind beide Parteien Kaufleute mit Niederlassung in verschiedenen Vertragsstaaten des CISG?
2. Ist der Gegenstand eine bewegliche körperliche Sache (kein Konsumkauf, keine Dienstleistung)?
3. Haben die Parteien die Anwendung des CISG wirksam ausgeschlossen (Art. 6 CISG — ausdrücklicher Ausschluss nötig)?
4. Welche Rügefrist gilt — ist die Rügeobliegenheit nach Art. 38, 39 CISG gewahrt?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- Art. 1 CISG — sachlicher, persönlicher, räumlicher Anwendungsbereich
- Art. 6 CISG — Ausschluss durch Vereinbarung (muss ausdrücklich sein)
- Art. 25 CISG — wesentliche Vertragsverletzung
- Art. 35 CISG — Vertragsgemäßheit der Ware
- Art. 38, 39 CISG — Untersuchungs- und Rügeobliegenheit
- Art. 49 CISG — Aufhebungsrecht des Käufers
- Art. 74-78 CISG — Schadensersatz und Zinsen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Anwendbarkeit prüfen:** Vertragsstaaten? Warenkauf? Kein Konsumkauf? Kein wirksamer Ausschluss?
2. **Vertragsgemäßheit prüfen (Art. 35 CISG):** War die Ware vertragsgemäß geliefert?
3. **Rüge geprüft (Art. 38, 39 CISG):** Wurde innerhalb angemessener Frist gerügt? (Bei Fristversäumnis: Verlust der Mängelrechte.)
4. **Wesentliche Vertragsverletzung (Art. 25 CISG):** Nur dann Vertragsaufhebung (Art. 49 CISG).
5. **Rechtsbehelfe prüfen:** Minderung, Schadensersatz (Art. 74 ff. CISG), Zinsen (Art. 78 CISG).

## Output-Template

**Adressat:** Entscheidungsgründe — Tonfall: sachlich-juristisch

```
## CISG-Prüfung

**Anwendbarkeit:** Das CISG ist anwendbar, weil [PARTEI A] ihre Niederlassung in [STAAT A]
und [PARTEI B] ihre Niederlassung in [STAAT B] hat, beides CISG-Vertragsstaaten (Art. 1 Abs. 1 lit. a CISG).
Ein Ausschluss nach Art. 6 CISG liegt nicht vor. [Alternativ: CISG ausgeschlossen durch Klausel ...]

**Vertragsgemäßheit (Art. 35 CISG):** Die Ware war [vertragsgemäß / nicht vertragsgemäß], weil [BEGRÜNDUNG].

**Rügeobliegenheit (Art. 38, 39 CISG):** [Die Rüge erfolgte am DATUM, innerhalb angemessener Frist.
/ Die Rüge erfolgte nicht fristgerecht, so dass Käufer seine Mängelrechte verloren hat.]

**Ergebnis:** [PARTEI] hat Anspruch auf [Minderung / Schadensersatz / Aufhebung] nach Art. [NORM] CISG.
```

## Anwendungsbereich

1. **Sachlich** (Artikel 1-5 CISG): Kauf von Waren (bewegliche koerperliche Sachen). Ausnahmen: Konsumkauf, Versteigerung, Wertpapiere, Geld, Schiffe, Luftfahrzeuge, Elektrizitaet.
2. **Persönlich** (Artikel 1 CISG): Parteien haben ihre Niederlassung in verschiedenen Vertragsstaaten ODER IPR führt zur Anwendung des Rechts eines Vertragsstaates.
3. **Raeumlich**: Beide Parteien in Vertragsstaaten (Deutschland, Schweiz, USA, China, Frankreich, Italien, alle EU außer UK seit Brexit, ...).
4. **Zeitlich**: nach 1. Januar 1991 für Deutschland.

## Ausschluss

- Artikel 6 CISG: Parteien koennen die Anwendung ganz oder teilweise ausschließen.
- Wirksamer Ausschluss erfordert klare Vereinbarung. **Nicht ausreichend** ist die blosse Rechtswahl "deutsches Recht" - CISG ist Teil des deutschen Rechts. Erforderlich: ausdruecklicher Ausschluss ("unter Ausschluss des UN-Kaufrechts").

## Wichtige Vorschriften

- **Artikel 25 CISG** - wesentliche Vertragsverletzung
- **Artikel 35 CISG** - Vertragsmaessigkeit der Ware
- **Artikel 38 und 39 CISG** - Untersuchungs- und Ruegeobliegenheit; kurze Frist
- **Artikel 49 CISG** - Aufhebung des Vertrages bei wesentlicher Vertragsverletzung
- **Artikel 74-77 CISG** - Schadensersatz
- **Artikel 78 CISG** - Zinsen ab Fälligkeit (Höhe nach nationalem Recht)

## Kollisionsfälle

Wenn die Parteien gleichzeitig deutsches und Schweizer Recht wählen (kollidierende AGB), greift in der Regel CISG, weil beide Staaten Vertragsstaaten sind und die Rechtswahl in beiden Fällen auf einen Vertragsstaat führt. Falls eine Partei den Ausschluss in ihren AGB hat und die andere nicht, ist nach der Theorie der Resstgültigkeit / Knock-out-Doktrin (Artikel 19 CISG, herrschende Meinung in Deutschland) der Ausschluss nicht wirksam vereinbart.

## 3. `dsgvo-rechtswidriges-produkt`

**Fokus:** Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit prüfen: Richter oder Anwalt muss beurteilen ob Smartglasses oder IoT-Produkt DSGVO-konform ist. Normen: Art. 3 DSGVO (räumlicher Anwendungsbereich), Art. 5 Abs. 1 lit. c (Datensparsamkeit), Art. 6 (Rechtsgrundlage), Art. 9 (biometrische Daten), Art. 13-14 (Informationspflichten), Art. 44 ff. (Drittlandtransfer), Art. 22 (automatisierte Entscheidung). Prüfraster: Anwendbarkeit, Rechtsgrundlage, Sonderkateg. Daten, Drittlandtransfer. Output DSGVO-Prüfschema mit Ergebnis und Empfehlung. Abgrenzung: allgemeine DSGVO-Beratung siehe datenschutzrecht-Plugin; DSA siehe dsa-dma-Plugin.

# DSGVO-rechtswidriges Produkt

Pruefschema, wenn ein technisches Produkt aus dem Ausland nach DSGVO als rechtswidrig zu bewerten ist und der Kaeufer Rückabwicklung will.


## Triage zu Beginn

1. Unterliegt das Produkt dem räumlichen Anwendungsbereich der DSGVO (Art. 3 Abs. 1 oder Abs. 2 DSGVO)?
2. Welche Kategorien personenbezogener Daten werden verarbeitet — biometrische Daten (Art. 9 DSGVO)?
3. Werden Daten in Drittländer übermittelt ohne SCC oder anderen Mechanismus (Art. 44 ff. DSGVO)?
4. Hat der Käufer wirksame Einwilligung erteilt oder scheidet Einwilligung aus (Art. 7 DSGVO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- Art. 3 DSGVO — räumlicher Anwendungsbereich (Niederlassungs- und Marktortprinzip)
- Art. 6 DSGVO — Rechtsgrundlagen für Verarbeitung
- Art. 7 DSGVO — wirksame Einwilligung
- Art. 9 DSGVO — besondere Kategorien (biometrische Daten, Gesundheitsdaten)
- Art. 44 ff. DSGVO — Drittlandübermittlung (SCC, Angemessenheitsbeschluss)
- Art. 82 DSGVO — Schadensersatz (materiell und immateriell)
- § 134 BGB — Nichtigkeit bei Verstoß gegen Verbotsgesetz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Anwendbarkeit DSGVO prüfen (Art. 3):** Niederlassungsprinzip oder Marktortprinzip.
2. **Verarbeitungsarten inventarisieren:** Welche Daten werden vom Produkt verarbeitet?
3. **Rechtsgrundlage prüfen (Art. 6, 7, 9):** Für jede Verarbeitungsart.
4. **Drittlandübermittlung (Art. 44 ff.):** SCC vorhanden? Angemessenheitsbeschluss?
5. **Privatrechtliche Konsequenzen:** Nichtigkeit § 134 BGB? Sachmangel § 434 BGB? CISG Art. 35?
6. **Schadensersatz (Art. 82 DSGVO):** Materiell und immateriell — konkreten Schaden darlegen.

## Output-Template

**Adressat:** Entscheidungsgründe — Tonfall: sachlich-juristisch

```
## DSGVO-Prüfung

**Anwendbarkeit Art. 3 DSGVO:** Ja, weil [Niederlassungsprinzip / Marktortprinzip: Produkt
richtet sich an Personen in der EU].

**Verarbeitungsarten:** [Produkt X] verarbeitet [DATENART, z.B. biometrische Daten nach Art. 9 DSGVO].

**Rechtsgrundlage Art. 6 DSGVO:** Keine wirksame Rechtsgrundlage, weil [BEGRÜNDUNG].

**Folge:** [Sachmangel § 434 BGB / Nichtigkeit § 134 BGB / Schadensersatz Art. 82 DSGVO].
```

## Pruefstationen

### A - Anwendbarkeit der DSGVO

- Art. 3 Abs. 1 DSGVO: Niederlassungsprinzip
- Art. 3 Abs. 2 DSGVO: Marktortprinzip - Anbieten von Waren oder Dienstleistungen an Personen in der Union ODER Verhaltensbeobachtung in der Union
- DSGVO ist Eingriffsnorm im Sinne Art. 9 Rom-I (deutsche Gerichte wenden sie auch dann an, wenn das Vertragsstatut ausländisch ist)

### B - Verstöße prüfen

1. **Art. 5 Abs. 1 DSGVO** - Grundsätze (Rechtmäßigkeit, Treu und Glauben, Transparenz, Zweckbindung, Datenminimierung, Richtigkeit, Speicherbegrenzung, Integritaet, Rechenschaftspflicht)
2. **Art. 6 DSGVO** - Rechtsgrundlage
3. **Art. 7 DSGVO** - Einwilligung (informiert, freiwillig, widerrufbar)
4. **Art. 9 DSGVO** - besondere Kategorien (Gesundheits-, biometrische Daten)
5. **Art. 13 und 14 DSGVO** - Informationspflichten
6. **Art. 22 DSGVO** - automatisierte Entscheidung im Einzelfall
7. **Art. 25 DSGVO** - privacy by design und by default
8. **Art. 32 DSGVO** - Sicherheit der Verarbeitung
9. **Art. 44 ff DSGVO** - Datenübermittlung in Drittlaender

### C - Folgen für den Privatrechtsstreit

- Verstoß gegen ein Verbotsgesetz (Art. 6 DSGVO i. V. m. nationaler Norm)? -> Nichtigkeit nach Paragraf 134 BGB?
- Sachmangel im Sinne Paragraf 434 BGB i. V. m. Art. 6 ProduktsicherheitsVO 2023?
- Mangel im Sinne Art. 35 CISG (Vertragsmaessigkeit)?

## Smartglasses und Wearables - typische Verstöße

- heimliche Aufzeichnung Dritter ohne deren Wissen (Verletzung Persönlichkeitsrecht aller in der Umgebung)
- Live-Streaming der Kameraperspektive ohne Hinweis-LED
- Gesichtserkennung in Echtzeit
- Datenübertragung in Drittlaender ohne SCC oder anderen Mechanismus

## Im Urteil

Im Tatbestand auf das Gutachten verweisen. In den Entscheidungsgründen konkret die verletzten DSGVO-Artikel benennen und subsumieren.

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 39/20 (claimed: DSGVO-Versto\u00dfe Schadensersatz Art. 82, NJW 2021, 3041): NOT_FOUND auf dejure.org. NJW 2021, 3041 gehoert zu BGH VI ZR 40/20 (VW-Abgasskandal §826 BGB) – thematisch unverwandt. Eintrag geloescht. DSGVO-Schadensersatz wird durch bereits vorhandene EuGH-Zitate C-300/21 und C-340/21 abgedeckt. -->
