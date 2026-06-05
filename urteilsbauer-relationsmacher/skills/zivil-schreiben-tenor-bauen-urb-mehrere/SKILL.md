---
name: zivil-schreiben-tenor-bauen-urb-mehrere
description: "Zivil Schreiben Tenor Bauen URB Mehrere: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zivil Schreiben Tenor Bauen URB Mehrere

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Zivil Schreiben Tenor Bauen URB Mehrere** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tatbestand-zivil-schreiben` | Tatbestand eines Zivilurteils nach § 313 Abs. 2 ZPO schreiben: Richter muss den Prozessstoff sachlich und knapp wiedergeben. Normen: § 313 Abs. 2 ZPO (Tatbestand-Anforderungen), § 314 ZPO (Beweiskraft des Tatbestands). Prüfraster: Einleitungssatz, unstreitiger Sachverhalt, streitiges Klaegervorbringen mit Antrag, Beklagtenvorbringen mit Antrag, Bezugnahmen auf Anlagen. Output Tatbestand-Entwurf: knapp, nuechtern, objektiv im Urteilsstil. Abgrenzung: Entscheidungsgründe siehe entscheidungsgründe-zivil-schreiben; Relation (Vorstufe) siehe relation-zivil. |
| `tenor-bauen-zivil` | Tenor eines Zivilurteils konstruieren: Richter muss Hauptsache-Entscheidung, Kosten und Vollstreckbarkeit klar tenorieren. Normen: §§ 91 ff. ZPO (Kosten), §§ 708-720a ZPO (vorlaeufige Vollstreckbarkeit), § 511 ZPO (Berufungszulassung), Bestimmtheitsgebot. Prüfraster: Zahlungsantrag mit Zinsen ab, Kostenquote, vorlaeufige Vollstreckbarkeit mit/ohne Sicherheitsleistung, Streitwertfestsetzung, Berufungszulassung. Output Tenor-Entwurf vollständig und vollstreckbar. Abgrenzung: Entscheidungsgründe siehe entscheidungsgründe-zivil-schreiben; Kostenentscheidung detail siehe kostenentscheidung-bauen. |
| `urb-mehrere-streitgegenstaende-spezial` | Spezialfall mehrere Streitgegenstaende und Eventualantraege: Reihenfolge der Pruefung, Tenor, Kostenverteilung. Pruefraster fuer komplexe Verfahren. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Zivil Schreiben Tenor Bauen URB Mehrere**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tatbestand-zivil-schreiben`

**Fokus:** Tatbestand eines Zivilurteils nach § 313 Abs. 2 ZPO schreiben: Richter muss den Prozessstoff sachlich und knapp wiedergeben. Normen: § 313 Abs. 2 ZPO (Tatbestand-Anforderungen), § 314 ZPO (Beweiskraft des Tatbestands). Prüfraster: Einleitungssatz, unstreitiger Sachverhalt, streitiges Klaegervorbringen mit Antrag, Beklagtenvorbringen mit Antrag, Bezugnahmen auf Anlagen. Output Tatbestand-Entwurf: knapp, nuechtern, objektiv im Urteilsstil. Abgrenzung: Entscheidungsgründe siehe entscheidungsgründe-zivil-schreiben; Relation (Vorstufe) siehe relation-zivil.

# Tatbestand schreiben

Form und Inhalt: Paragraf 313 Abs. 2 ZPO. Knapp, nuechtern, objektiv, im Praesens, nicht im Perfekt.

## Triage zu Beginn

1. Ist die Beweisaufnahme abgeschlossen — alle Aussagen und Gutachten protokolliert?
2. Sind alle streitigen und unstreitigen Tatsachen aus dem Aktenintake eindeutig getrennt?
3. Hat das Gericht Hinweisbeschlüsse nach § 139 ZPO erlassen — wurden sie befolgt?
4. Gibt es Widerklage oder Hilfsanträge — müssen im Tatbestand vollständig erscheinen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 313 Abs. 2 ZPO — Tatbestand: gedrängter Überblick über Vorbringen beider Parteien, Bezugnahme auf Anlagen
- § 314 ZPO — Beweiskraft des Tatbestands
- § 320 ZPO — Tatbestandsberichtigung auf Antrag
- § 286 ZPO — Beweiswürdigung (gehört in Entscheidungsgründe, nicht Tatbestand)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Einleitungssatz formulieren:** "Die Parteien streiten über [STREITGEGENSTAND] aus [VERTRAGSART/DELIKT]."
2. **Unstreitige Tatsachen:** Chronologisch — Vertragsschluss, Lieferung, Zahlung etc.
3. **Streitiges Klägervorbringen:** Eingeleitet mit "Der Kläger behauptet, ..." — nicht als Tatsache darstellen.
4. **Klageantrag:** Wörtlich einfügen oder durch Bezugnahme auf Schriftsatz.
5. **Streitiges Beklagtenvorbringen:** "Die Beklagte beträgt, ..."
6. **Beklagtenantrag:** "Die Beklagte beantragt, die Klage abzuweisen."
7. **Beweisaufnahme:** "Das Gericht hat Beweis erhoben durch Vernehmung der Zeugen [NAMEN]. Wegen der Einzelheiten wird auf das Sitzungsprotokoll vom [DATUM] Bezug genommen."

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Tatbestand fuer Zivilurteil schreiben | Tatbestand nach Schema; Template unten |
| Variante A — Sachverhalt sehr komplex viele Beteiligte | Komprimierter Tatbestand; Anlage fuer Details verwenden |
| Variante B — Partien sind einig nur formale Niederlegung noetig | Vereinfachter Tatbestand; nur wesentliche streitige Punkte |
| Variante C — Tatbestand wird angesteuert auf Revision | Revisionssichere Tatbestandsdarstellung; alle relevanten Tatsachen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Urteil → Tatbestand — Tonfall: nüchtern-objektiv, Präsens

```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Tatbestand

Die Parteien streiten über [STREITGEGENSTAND] aus einem [Kauf- / Werk- / Miet-]vertrag
vom [DATUM].

Der Kläger erwarb von der Beklagten [WARE/LEISTUNG] zum Preis von [BETRAG] EUR (Anlage K1).
Die Beklagte lieferte am [DATUM].

Der Kläger behauptet, [STREITIGE TATSACHE KLÄGER].

Der Kläger beantragt,
 die Beklagte zu verurteilen, an ihn [BETRAG] EUR nebst Zinsen zu zahlen.

Die Beklagte behauptet, [STREITIGE TATSACHE BEKLAGTE].

Die Beklagte beantragt,
 die Klage abzuweisen.

Das Gericht hat Beweis erhoben durch Vernehmung des Zeugen [NAME] sowie durch Einholung
eines schriftlichen Sachverständigengutachtens des Sachverständigen [NAME] vom [DATUM].
Wegen der Einzelheiten wird auf das Sitzungsprotokoll vom [DATUM] und das Gutachten Bezug genommen.
```

## Aufbau

1. **Einleitungssatz**: "Die Parteien streiten über ... aus einem ... Vertrag" / "... wegen ... aus einem ... Unfall"
2. **Unstreitiger Sachverhalt** - chronologisch
3. **Streitiges Klägervorbringen** - eingeleitet mit "Der Kläger behauptet, ..." oder "Der Kläger ist der Ansicht, ..."
4. **Antrag des Klägers** - wörtlich (mit Antrags-Einrueckung) oder durch Bezugnahme
5. **Streitiges Beklagtenvorbringen** - "Die Beklagte behauptet, ... Sie ist der Ansicht, ..."
6. **Antrag des Beklagten** - "Die Beklagte beantragt, die Klage abzuweisen."
7. **Beweisaufnahme** - "Das Gericht hat Beweis erhoben durch Vernehmung der Zeugen X und Y sowie durch Einholung eines schriftlichen Sachverständigengutachtens des Sachverständigen Dr. Z. Wegen der Einzelheiten der Beweisaufnahme wird auf das Sitzungsprotokoll vom 14. Mai 2026 und auf das Gutachten vom 28. Februar 2026 Bezug genommen."

## Bezugnahmen

Auf Anlagen, Schriftsätze, Protokolle nach Paragraf 313 Abs. 2 Satz 2 ZPO konkret Bezug nehmen: "Wegen der Einzelheiten wird auf die Anlage K3 (Bl. 18 der Akte) Bezug genommen."

## Konventionen

- Parteien werden als "Kläger" / "Beklagte" bezeichnet (nicht namentlich, außer zur Unterscheidung mehrerer Beklagter)
- Streitwertangaben im Tatbestand vermeiden (gehören in den Tenor / Streitwertbeschluss)
- "Wegen ..." gehört in den Einleitungssatz, nicht in das Rubrum

## 2. `tenor-bauen-zivil`

**Fokus:** Tenor eines Zivilurteils konstruieren: Richter muss Hauptsache-Entscheidung, Kosten und Vollstreckbarkeit klar tenorieren. Normen: §§ 91 ff. ZPO (Kosten), §§ 708-720a ZPO (vorlaeufige Vollstreckbarkeit), § 511 ZPO (Berufungszulassung), Bestimmtheitsgebot. Prüfraster: Zahlungsantrag mit Zinsen ab, Kostenquote, vorlaeufige Vollstreckbarkeit mit/ohne Sicherheitsleistung, Streitwertfestsetzung, Berufungszulassung. Output Tenor-Entwurf vollständig und vollstreckbar. Abgrenzung: Entscheidungsgründe siehe entscheidungsgründe-zivil-schreiben; Kostenentscheidung detail siehe kostenentscheidung-bauen.

# Tenor bauen Zivilurteil

Der Tenor ist das Herzstück des Urteils. Er muss vollstreckbar sein.


## Triage zu Beginn

1. Welche Anträge wurden gestellt — Hauptantrag, Hilfsantrag, Widerklage?
2. Ist der Kläger voll, teilweise oder gar nicht erfolgreich?
3. Welcher Zinssatz gilt — 5 Prozentpunkte über Basiszinssatz (§ 288 Abs. 1 BGB) oder 9 Prozentpunkte (§ 288 Abs. 2 BGB, B2B)?
4. Ist vorläufige Vollstreckbarkeit mit oder ohne Sicherheitsleistung anzuordnen (§ 708 Nr. 11 oder § 709 ZPO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 253 Abs. 2 Nr. 2 ZPO — Bestimmtheitsgebot für den Antrag (gilt spiegelbildlich für Tenor)
- § 288 Abs. 1 BGB — Verzugszinssatz (5 Prozentpunkte über Basiszinssatz)
- § 288 Abs. 2 BGB — Verzugszinssatz im B2B-Bereich (9 Prozentpunkte über Basiszinssatz)
- § 291 BGB — Rechtshängigkeitszinsen (ab Klageerhebung)
- § 708 Nr. 11 ZPO — Vollstreckbarkeit ohne Sicherheit bis 1.500 EUR
- § 709 ZPO — Vollstreckbarkeit gegen Sicherheitsleistung von 110 Prozent
- § 713 ZPO — Vollstreckbarkeit ohne Sicherheit bei fehlendem Rechtsmittel

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Hauptsacheantrag prüfen:** Zahlungsbetrag, Zinssatz, Zinsbeginn — konkret und vollstreckbar formulieren.
2. **Hilfsanträge/Widerklage:** Reihenfolge wie im Klageantrag; Hilfsantrag mit "hilfsweise:" kennzeichnen.
3. **Kostenentscheidung:** § 91 ZPO (voller Sieg) oder § 92 ZPO (Quotelung).
4. **Vorläufige Vollstreckbarkeit:** Passende Norm wählen (§ 708, 709 oder 713 ZPO).
5. **Streitwertbeschluss:** Im Tenor oder separat (§ 63 GKG).

## Output-Template

**Adressat:** Urteil → Tenor — Tonfall: formal-amtlich

```
## Tenor

1. Die Beklagte wird verurteilt, an den Kläger [BETRAG] EUR nebst Zinsen in Höhe von
 fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem [DATUM] zu zahlen.
 [Im Übrigen wird die Klage abgewiesen.]

2. Die [Beklagte / Kosten werden gequotelt: Kläger X von Hundert, Beklagte Y von Hundert]
 trägt die Kosten des Rechtsstreits.

3. Das Urteil ist vorläufig vollstreckbar [gegen Sicherheitsleistung in Höhe von
 einhundertzehn Prozent des jeweils zu vollstreckenden Betrages].

4. Der Streitwert wird auf [BETRAG] EUR festgesetzt.
```

## Aufbau

1. **Hauptsache** (Verurteilung / Klageabweisung)
 - bezifferter Zahlungsantrag mit Zinsen "ab" Datum / "seit" Datum
 - bei Mehrforderungen: Reihenfolge wie im Antrag, mit Hilfsanträgen kenntlich machen
2. **Kosten** (Paragraf 91 ff ZPO)
 - bei vollem Obsiegen: "Der Beklagte traegt die Kosten des Rechtsstreits."
 - bei teilweisem Obsiegen: Quote nach Paragraf 92 ZPO
 - bei mehreren Beklagten: Paragraf 100 ZPO
3. **Vorläufige Vollstreckbarkeit** (Paragraf 708 ff ZPO)
 - Standardformel: "Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn Prozent des jeweils zu vollstreckenden Betrages."
 - Bei Beschwer unter 600 EUR: Paragraf 713 ZPO - ohne Sicherheit
 - Bei Versäumnisurteil: Paragraf 708 Nr. 2 ZPO
4. **Streitwert** (gesonderter Beschluss oder im Tenor)
5. **Berufungszulassung** (Paragraf 511 Abs. 4 ZPO bei AG-Urteilen mit Beschwer unter 600 EUR)

## Bestimmtheitsgebot

Der Tenor muss aus sich heraus vollstreckbar sein. Keine Bezugnahmen auf den Tatbestand.

## Beispiele

- "Die Beklagte wird verurteilt, an den Kläger ein Komma fünffünfsiebenzig Euro (genauer: 1577 EUR oder 1577.00 EUR) nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem 15. Januar 2026 zu zahlen."
- "Die Klage wird abgewiesen."
- "Die Kosten des Rechtsstreits traegt die Beklagte."
- "Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn Prozent des jeweils zu vollstreckenden Betrages."
- "Der Streitwert wird auf 1577 Euro festgesetzt."

Im Repository werden Geldbetraege im Fliesstext mit Punkt geschrieben (Repo-Konvention).

---
<!-- AUDIT 27.05.2026: BGH VII ZR 213/10 (NJW 2011, 2885) auf dejure.org nicht auffindbar (NOT_FOUND) — Eintrag ersatzlos geloescht. Uebrige Rechtsprechungseintraege wurden nicht geprueft. -->

## 3. `urb-mehrere-streitgegenstaende-spezial`

**Fokus:** Spezialfall mehrere Streitgegenstaende und Eventualantraege: Reihenfolge der Pruefung, Tenor, Kostenverteilung. Pruefraster fuer komplexe Verfahren.

# Urb: Mehrere Streitgegenstaende

## Spezialwissen: Urb: Mehrere Streitgegenstaende
- **Spezialgegenstand:** Urb: Mehrere Streitgegenstaende / urb mehrere streitgegenstaende spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
