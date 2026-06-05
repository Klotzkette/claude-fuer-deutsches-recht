---
name: jveg-gate-rechenblatt
description: "Gate Rechenblatt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gate Rechenblatt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gate Rechenblatt** im Plugin JVEG-Kostenprüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jveg-quality-gate` | Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht JVEG. Abgrenzung: nicht Einzelberechnungs-Skill. |
| `jveg-rechenblatt` | JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgrenzung: nicht Antragsgenerator. |
| `jveg-sachverstaendigenrechnung` | Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte Sachverständigenrechnung. Abgrenzung: nicht Zeugenentschaedigung. |

## Arbeitsweg

Im Plugin JVEG-Kostenprüfer gilt für **Gate Rechenblatt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jveg-quality-gate`

**Fokus:** Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht JVEG. Abgrenzung: nicht Einzelberechnungs-Skill.

# JVEG-Quality-Gate

## Fachkern: JVEG-Quality-Gate
- **Spezialgegenstand:** JVEG-Quality-Gate wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Führe eine abschließende Qualitätsprüfung aller JVEG-Dokumente durch, bevor sie versandt oder eingereicht werden.

## Triage — kläre vor der Prüfung

1. **Dokumenttyp:** Welches Dokument wird geprüft — Antrag, Rechenblatt, Beschwerdeschrift oder Antwortschreiben?
2. **Mathcheck:** Sind alle Rechenoperationen (Summen, Teilbeträge) nachvollziehbar und korrekt?
3. **Belegcheck:** Sind alle zitierten Belege tatsächlich als Anlage beigefügt?
4. **Doppelposten:** Wird dieselbe Position doppelt abgerechnet (z.B. Reisezeit und Wartezeit überschneidend)?
5. **Ton und Antrag:** Ist der Antragssatz eindeutig formuliert, ohne missverständliche Alternativen?

## Speziallogik: Stopp bei roten Punkten
Das Quality Gate stoppt den Prozess, wenn folgende rote Punkte erkannt werden:
- Rechenfehlerin der Summenzeile.
- Fehlender Pflichtbeleg (§ 5, § 11, § 16 JVEG).
- Überschreitung der Dreimonatsfrist ohne Wiedereinsetzungsantrag.
- Doppelabrechnung einer Position.
- Unklar formulierter oder fehlender Antrag.

## Zentrale Normen
- § 4 JVEG (Festsetzungsantrag — Formerfordernis)
- § 23 JVEG (Dreimonatsfrist)
- § 8 JVEG (Sachverständigenvergütung — Berechnung)
- § 5 JVEG (Fahrtkosten — Belegpflicht)
- § 16 JVEG (Übersetzer — Zeilennachweise)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Jedes fertiggestellte JVEG-Dokument vor Versand.

## Arbeitsweise
1. Mathcheck: Alle Summen nachrechnen.
2. Belegcheck: Anlagenliste mit Belegen abgleichen.
3. Doppelpostencheck: Jede Position auf Überschneidung prüfen.
4. Fristcheck: § 23 JVEG-Frist bestätigen.
5. Antragssatz prüfen: eindeutig, vollständig, mit Betrag.
6. Bei rotem Punkt: Prozess stoppen und Fehler benennen.

## Output-Template

| Prüfpunkt | Status | Befund |
|---|---|---|
| Mathcheck | Gruen / Rot | [Befund] |
| Belegcheck | Gruen / Rot | [Befund] |
| Doppelposten | Gruen / Rot | [Befund] |
| Fristcheck § 23 JVEG | Gruen / Rot | [Befund] |
| Antragssatz | Gruen / Rot | [Befund] |
| **Gesamtergebnis** | **Gruen / Rot** | [Freigabe / Stopp] |

## Ausgabe
Qualitätsbericht mit Ampelstatus; roter Punkt hält Dokument zurück.

## Leitplanken
- Freigabe erst nach vollständig grünem Prüfbericht.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 2. `jveg-rechenblatt`

**Fokus:** JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgrenzung: nicht Antragsgenerator.

# JVEG-Rechenblatt

## Fachkern: JVEG-Rechenblatt
- **Spezialgegenstand:** JVEG-Rechenblatt wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Erstelle ein vollständig nachvollziehbares Rechenblatt für JVEG-Vergütungsansprüche mit Normbezug, Eingabewert, Kappungsgrenze, Belegverweis und Rechenergebnis je Position.

## Triage — kläre vor der Erstellung

1. **Positionen:** Welche Vergütungspositionen sollen im Rechenblatt erfasst werden?
2. **Honorargruppe:** Bei Sachverständigen — welche Honorargruppe nach § 9 JVEG?
3. **Zeitnachweise:** Liegen dokumentierte Zeitangaben (Beginn/Ende) für die Tätigkeit vor?
4. **Kappungsgrenzen:** Gibt es Höchstbeträge (z.B. Tagesgeld, Übernachtungspauschale)?
5. **Vorschussabzug:** Ist ein bereits ausgezahlter Vorschuss in Abzug zu bringen?

## Zentrale Normen
- § 8 JVEG (Sachverständigenvergütung — Stundensatz)
- § 9 JVEG (Honorargruppen-Tabelle)
- § 10 JVEG (Reisezeit)
- § 5 JVEG (Fahrtkosten — Kilometer × Satz)
- § 11 JVEG (Übernachtungsgeld — Kappungsgrenze)
- § 12 JVEG (Tagegeld)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Fertigstellung der Positionserfassung (jveg-aktenstripper); vor Antragserstellung.

## Arbeitsweise
1. Jede Position mit Eingabewert und Norm erfassen.
2. Kappungsgrenzen anwenden.
3. Rechenweg Schritt für Schritt dokumentieren.
4. Belegverweis pro Zeile eintragen.
5. Summe bilden; Vorschuss abziehen; Restforderung ausweisen.

## Output-Template

| Position | Norm | Eingabewert | Kappung | Rechenschritt | Beleg | Ergebnis (EUR) |
|---|---|---|---|---|---|---|
| Stunden Honorar [X Std. × Y EUR] | § 8 i.V.m. § 9 JVEG | X Std. | — | X × Y = | Anlage 1 | 00,00 |
| Reisezeit [X Std. × Y EUR] | § 10 JVEG | X Std. | — | X × Y = | Anlage 2 | 00,00 |
| Fahrtkosten [X km × Y EUR] | § 5 JVEG | X km | — | X × Y = | Anlage 3 | 00,00 |
| Übernachtung | § 11 JVEG | 1 Nacht | 00,00 EUR | Beleg | Anlage 4 | 00,00 |
| **Brutto** | | | | | | **00,00** |
| ./. Vorschuss | § 3 JVEG | | | | | -00,00 |
| **Restforderung** | | | | | | **00,00** |

## Ausgabe
Vollständiges Rechenblatt; dient als Anlage zum Festsetzungsantrag.

## Leitplanken
- Jede Zeile braucht Norm + Beleg; leere Felder blockieren die Ausgabe.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 3. `jveg-sachverstaendigenrechnung`

**Fokus:** Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte Sachverständigenrechnung. Abgrenzung: nicht Zeugenentschaedigung.

# JVEG-Sachverstaendigenrechnung

## Fachkern: JVEG-Sachverstaendigenrechnung
- **Spezialgegenstand:** JVEG-Sachverstaendigenrechnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe Sachverständigenrechnungen vollständig nach §§ 8–10 JVEG: Honorargruppe, erforderliche Zeit, Reisezeit, Nebenkosten, § 8a-Kürzungsrisiken und Vorschusssaldo.

## Triage — kläre vor der Prüfung

1. **Honorargruppe:** Welcher Honorargruppe nach § 9 JVEG ist der Sachverständige zugeordnet?
2. **Erforderliche Zeit:** Wie viele Stunden werden abgerechnet — sind diese als erforderlich belegt?
3. **Reisezeit:** Werden Reisezeiten nach § 10 JVEG getrennt abgerechnet?
4. **§ 8a-Risiken:** Gibt es Anhaltspunkte für Gutachtenmängel, fehlende Hinweise oder Vorschussüberschreitung?
5. **Nebenkosten:** Werden Schreibauslagen, Kopien, Literatur oder sonstige Kosten geltend gemacht?

## Zentrale Normen
- § 8 JVEG (Sachverständigenvergütung — Stundensatz)
- § 8a JVEG (Kürzung/Wegfall)
- § 9 JVEG (Honorargruppen, Anlage 1)
- § 10 JVEG (Reisezeit)
- § 12 JVEG (Nebenkosten)
- § 3 JVEG (Vorschuss)

## Rechtsstand 2025/2026 — KostRAeG 2025

Mit dem KostRAeG 2025 wurden die Saetze des § 9 JVEG in Anlage 1 zum 01.06.2025 pauschal um 9 Prozent erhoeht. Anwendbar nur auf Auftraege ab 01.06.2025; in Altverfahren bleiben die Stundensaetze nach JVEG 2021 unveraendert.

- Synopse der neuen Saetze: https://ifsforum.de/fileadmin/user_upload/Aktuelles/Synopse_JVEG__2025.pdf
- Hinweise praxis-grundstuecksbewertung: https://praxis-grundstuecksbewertung.de/wissenswert/gesetzgebung/jveg-verguetung-sachverstaendige/
- DGuSV-Hinweise: https://www.dgusv.de/news-blog/mehr-geld-fuer-sachverstaendige-was-die-neuen-verguetungssaetze-seit-juni-2025-wirklich-bedeuten/

## Rechtsprechung
- Rechtsprechung zu §§ 8, 9, 12 JVEG (Erforderlichkeit, Plausibilitaetspruefung, Schwierigkeitsbewertung) ueber https://dejure.org und https://openjur.de verifizieren.
- BGH-Linie zu § 8a JVEG (Kuerzung wegen Pflichtverletzung) vor Ausgabe pruefen; Aktenzeichen und Datum nicht aus Modellwissen einsetzen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Eingang einer Sachverständigenrechnung zur Festsetzung nach § 4 JVEG.

## Arbeitsweise
1. Honorargruppe und Stundensatz verifizieren.
2. Erforderliche Zeit objektiv bewerten.
3. Reisezeit separat prüfen (§ 10 JVEG).
4. Nebenkosten auf Notwendigkeit und Belege prüfen.
5. § 8a-Risiken bewerten; Vorschusssaldo berechnen.

## Output-Template

| Position | Geltend (EUR) | Norm | Befund | Anerkannt (EUR) |
|---|---|---|---|---|
| Honorar [X Std. × Y EUR, Gr. Z] | 00,00 | § 8 i.V.m. § 9 JVEG | [Befund] | 00,00 |
| Reisezeit [X Std. × Y EUR] | 00,00 | § 10 JVEG | [Befund] | 00,00 |
| Nebenkosten | 00,00 | § 12 JVEG | [Befund] | 00,00 |
| **Brutto** | **00,00** | | | **00,00** |
| ./. Vorschuss | | § 3 JVEG | | -00,00 |
| **Restforderung** | **00,00** | | | **00,00** |

**§ 8a-Risikoeinschätzung:** [Keine / Teilkürzung / Vollkürzung]

## Ausgabe
Positionsgenaues Prüfergebnis mit § 8a-Risikoeinschätzung und Vorschusssaldo.

## Leitplanken
- Honorargruppe immer zuerst prüfen; falscher Ansatz infiziert gesamte Berechnung.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
