---
name: jveg-vorschuss-kostenrisiko
description: "Vorschuss Kostenrisiko: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vorschuss Kostenrisiko

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vorschuss Kostenrisiko** im Plugin JVEG-Kostenprüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jveg-vorschuss` | Vorschuss auf JVEG-Verguetung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung: nicht Kostenfestsetzungsantrag (endgueltige Abrechnung). |
| `jveg-vorschuss-kostenrisiko-spezial` | Spezialfall Vorschuss und Kostenrisiko § 17 JVEG: Vorschussverlangen Sachverstaendiger, Verzicht des Gerichts, Folgen bei Nichteinzahlung. Pruefraster fuer Verfahrensbeteiligte. |
| `jveg-zeugenentschaedigung` | Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Prüfraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung. Abgrenzung: nicht Sachverständigenverguetung (hoehere Saetze). |

## Arbeitsweg

Im Plugin JVEG-Kostenprüfer gilt für **Vorschuss Kostenrisiko**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jveg-vorschuss`

**Fokus:** Vorschuss auf JVEG-Verguetung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung: nicht Kostenfestsetzungsantrag (endgueltige Abrechnung).

# JVEG-Vorschuss

## Fachkern: JVEG-Vorschuss
- **Spezialgegenstand:** JVEG-Vorschuss wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe Vorschussanträge nach § 3 JVEG auf Zulässigkeit und Höhe, insbesondere bei erheblichen Fahrtkosten, Übernachtungsbedarf und Teilleistungen.

## Triage — kläre vor der Prüfung

1. **Vorschussgrund:** Erhebliche Fahrtkosten, Übernachtungsbedarf oder sonstige erhebliche Aufwendungen?
2. **Zeitpunkt:** Wird der Vorschuss vor Leistungserbringung oder nach Teilleistung beantragt?
3. **Bedürftigkeit:** § 3 JVEG knüpft nicht an Bedürftigkeit an — ist das dem Antragsteller bekannt?
4. **Höhe:** Wie hoch soll der Vorschuss sein — plausibel angesichts der zu erwartenden Kosten?
5. **Anrechnung:** Wie wird der Vorschuss auf den späteren Vergütungsanspruch angerechnet?

## Speziallogik: Erhebliche Aufwendungen
§ 3 JVEG setzt keine Bedürftigkeit, sondern erhebliche zu erwartende Aufwendungen voraus. Erheblich sind insbesondere:
- Mehrtägige Reisen mit Übernachtung.
- Fahrtkosten ab ca. 50 EUR (Richtwert, einzelfallabhängig).
- Vorausleistungen für Laborkosten oder Materialien.

## Zentrale Normen
- § 3 JVEG (Vorschuss — Voraussetzungen und Höhe)
- § 4 JVEG (Festsetzung — Anrechnung des Vorschusses)
- § 8a JVEG (Risiko bei Vorschussüberschreitung)
- §§ 5–12 JVEG (Berechnung der zu erwartenden Kosten)
- § 23 JVEG (Fristen — beginnen trotz Vorschuss mit Leistungserbringung)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Sachverständiger, Zeuge oder Dolmetscher beantragt Vorschuss vor oder während der Leistungserbringung.

## Arbeitsweise
1. Erheblichkeit der zu erwartenden Aufwendungen feststellen.
2. Vorschusshöhe anhand zu erwartender Kosten berechnen.
3. Bedürftigkeitsfrage explizit ausschließen.
4. Anrechnungslogik auf spätere Festsetzung dokumentieren.
5. Vorschussantrag formulieren.

## Output-Template

| Prüfpunkt | Befund |
|---|---|
| Vorschussgrund | [Fahrtkosten / Übernachtung / Vorausleistung] |
| Erheblichkeit der Aufwendungen | Ja / Nein — [Begründung] |
| Voraussichtliche Gesamtkosten (EUR) | 00,00 |
| Beantragte Vorschusshöhe (EUR) | 00,00 |
| Bedürftigkeit erforderlich | Nein (§ 3 JVEG) |
| Anrechnungshinweis | [Vorschuss wird auf Festsetzung angerechnet] |
| Empfehlung | [Antrag stellen / Betrag anpassen] |

## Ausgabe
Vorschussprüfung mit Erheblichkeitsbewertung, Betragsberechnung und Anrechnungshinweis.

## Leitplanken
- Keine Bedürftigkeitsprüfung; nur Erheblichkeit der Aufwendungen maßgeblich.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 2. `jveg-vorschuss-kostenrisiko-spezial`

**Fokus:** Spezialfall Vorschuss und Kostenrisiko § 17 JVEG: Vorschussverlangen Sachverstaendiger, Verzicht des Gerichts, Folgen bei Nichteinzahlung. Pruefraster fuer Verfahrensbeteiligte.

# JVEG: Vorschuss Kostenrisiko

## Fachkern: JVEG: Vorschuss Kostenrisiko
- **Spezialgegenstand:** JVEG: Vorschuss Kostenrisiko wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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

## 3. `jveg-zeugenentschaedigung`

**Fokus:** Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Prüfraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung. Abgrenzung: nicht Sachverständigenverguetung (hoehere Saetze).

# JVEG-Zeugenentschaedigung

## Fachkern: JVEG-Zeugenentschaedigung
- **Spezialgegenstand:** JVEG-Zeugenentschaedigung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Berechne und plausibilisiere Zeugenentschädigungen vollständig nach §§ 19–22 JVEG: Fahrtkosten, Aufwandsentschädigung, Verdienstausfall, Haushaltführungsschaden und Zeitversäumnis.

## Triage — kläre vor der Berechnung

1. **Zeugenstatus:** Ist die Person förmlich als Zeuge geladen und erschienen?
2. **Fahrtweg:** Wie hat der Zeuge die An- und Rückreise zurückgelegt — mit eigenem Kfz oder öffentlichen Verkehrsmitteln?
3. **Verdienstausfall:** Hat der Zeuge Einkommensnachweise für die versäumte Arbeitszeit?
4. **Haushalt:** Führt der Zeuge einen Haushalt und macht er Haushaltführungsschaden geltend?
5. **Zeitversäumnis:** Wird subsidiär nur Zeitversäumnis nach § 22 JVEG beantragt?

## Zentrale Normen
- § 19 JVEG (Fahrtkosten des Zeugen — Verweis auf § 5)
- § 20 JVEG (Aufwandsentschädigung / Haushaltführungsschaden)
- § 21 JVEG (Verdienstausfall)
- § 22 JVEG (Zeitversäumnis — Auffangtatbestand)
- § 23 JVEG (Dreimonatsfrist)

## Rechtsstand 2025/2026

JVEG-Saetze fuer Zeugen wurden durch das KostRAeG 2025 zum 01.06.2025 nicht geaendert (im Unterschied zu den Sachverstaendigenhonoraren in § 9 JVEG). Es gelten weiter:

- Stundensatz Verdienstausfall § 21 JVEG: bis zu 38 EUR/Std. (Hoechstbetrag).
- Stundensatz Zeitversaeumnis § 22 JVEG: 4,50 EUR/Std.
- Kilometerpauschale Zeugen § 5 Abs. 2 JVEG: 0,35 EUR/km.

Quelle gesetze-im-internet: https://www.gesetze-im-internet.de/jveg/

## Rechtsprechung
- LG-Linie: Zeitversaeumnis nach § 22 JVEG ist subsidiaer und kann nicht kumulativ zum Verdienstausfall nach § 21 JVEG geltend gemacht werden; eine subsidiaere Alternativberechnung ist im Antrag anzubieten. Konkretes Aktenzeichen vor Schriftsatz-Verwendung ueber https://dejure.org und https://openjur.de pruefen.
- Aktuelle BGH-Rechtsprechung zu §§ 19 bis 22 JVEG ueber https://www.bundesgerichtshof.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Zeuge möchte nach dem Gerichtstermin Entschädigungsantrag stellen.

## Arbeitsweise
1. Ladungsnachweis und Erscheinen bestätigen.
2. Fahrtkosten nach § 19 i.V.m. § 5 Abs. 2 JVEG berechnen.
3. Verdienstausfall oder Haushaltführungsschaden prüfen (§§ 20/21 JVEG).
4. Bei fehlendem Nachweis: Zeitversäumnis nach § 22 JVEG als Auffangtatbestand.
5. Gesamtbetrag berechnen; Frist § 23 JVEG prüfen.

## Output-Template

| Position | Norm | Geltend (EUR) | Beleg | Anerkannt (EUR) |
|---|---|---|---|---|
| Fahrtkosten [X km × 0,35 EUR] | § 19 i.V.m. § 5 Abs. 2 JVEG | 00,00 | Routennachweis | 00,00 |
| Verdienstausfall [X Std.] | § 21 JVEG | 00,00 | Arbeitgeberbeschein. | 00,00 |
| Haushaltführungsschaden | § 20 JVEG | 00,00 | Eidesstattl. Erkl. | 00,00 |
| Zeitversäumnis [X Std.] | § 22 JVEG | 00,00 | — | 00,00 |
| **Gesamt** | | **00,00** | | **00,00** |

**Dreimonatsfrist § 23 JVEG:** Fristende TT.MM.JJJJ

## Ausgabe
Vollständige Zeugenentschädigungsberechnung mit Positionsprüfung und Fristennotiz.

## Leitplanken
- Zeugen-Kilometersatz (§ 5 Abs. 2 JVEG) niedriger als Sachverständigensatz.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
