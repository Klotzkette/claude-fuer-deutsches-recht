---
name: gerichtsschreiben-kuerzung-wegfall
description: "Jveg Gerichtsschreiben Prüfung, Jveg Kommandocenter, Jveg Kuerzung Wegfall 8a: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Jveg Gerichtsschreiben Prüfung, Jveg Kommandocenter, Jveg Kuerzung Wegfall 8A

## Arbeitsbereich

Dieser Skill bündelt **Jveg Gerichtsschreiben Prüfung, Jveg Kommandocenter, Jveg Kuerzung Wegfall 8A** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `jveg-gerichtsschreiben-pruefung` | Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben gegen JVEG-Kuerzung. Abgrenzung: nicht formelle Beschwerde. |
| `jveg-kommandocenter` | Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis zum richtigen JVEG-Skill. Abgrenzung: kein inhaltlicher Berechnungs-Skill. |
| `jveg-kuerzung-wegfall-8a` | Kuerzung oder Wegfall der JVEG-Verguetung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit Begründung. Abgrenzung: nicht Dreimonatsfrist § 2 JVEG. |

## Arbeitsweg

Für **Jveg Gerichtsschreiben Prüfung, Jveg Kommandocenter, Jveg Kuerzung Wegfall 8A** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `jveg-kostenpruefer` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `jveg-gerichtsschreiben-pruefung`

**Fokus:** Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben gegen JVEG-Kuerzung. Abgrenzung: nicht formelle Beschwerde.

# JVEG-Gerichtsschreiben-Pruefung

## Fachkern: JVEG-Gerichtsschreiben-Pruefung
- **Spezialgegenstand:** JVEG-Gerichtsschreiben-Pruefung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Analysiere Schreiben des Kostenbeamten oder des Gerichts zu JVEG-Vergütungsansprüchen und identifiziere Tatbestandsfehler, Ermessensfehler und unrechtmäßige Beleganforderungen.

## Triage — kläre vor der Prüfung

1. **Schreibentyp:** Anforderungsschreiben, Kürzungsmitteilung, Festsetzungsbeschluss oder Ablehnungsbescheid?
2. **Beanstandete Positionen:** Welche Vergütungspositionen sind gekürzt oder abgelehnt worden?
3. **Begründung des Gerichts:** Auf welche Normen und Tatsachen stützt das Gericht seine Entscheidung?
4. **Beleganforderungen:** Werden Belege verlangt, die über das JVEG-Erforderliche hinausgehen?
5. **Fristen:** Besteht Antwort- oder Rechtsmittelfrist?

## Speziallogik: Zerlegung in prüfbare Aussagen
Jede Aussage des Gerichtsschreibens wird als prüfbare Hypothese behandelt:
1. Normaussage: Ist die zitierte Norm korrekt angewandt?
2. Tatsachenaussage: Stimmen die angenommenen Tatsachen mit dem Sachverhalt überein?
3. Rechtsfolgenaussage: Ist die gezogene Rechtsfolge (Kürzung, Wegfall) normkonform?

## Zentrale Normen
- § 4 JVEG (Festsetzung)
- § 8 JVEG (Sachverständigenvergütung)
- § 8a JVEG (Kürzung/Wegfall)
- § 5 JVEG (Fahrtkosten)
- § 23 JVEG (Fristen)
- § 286 ZPO (Freie Beweiswürdigung — Prüfmaßstab für Tatsachenfeststellungen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Eingang eines Schreibens des Kostenbeamten oder Gerichts zu JVEG-Positionen.

## Arbeitsweise
1. Schreiben in einzelne Aussagen zerlegen.
2. Jede Aussage auf Normkonformität und Tatsachenbasis prüfen.
3. Fehler kategorisieren (Tatbestand / Ermessen / Rechtsfolge).
4. Antwortbedarf und Frist festhalten.
5. Gegendarstellung vorbereiten.

## Output-Template

| Aussage des Gerichts | Normgrundlage | Prüfbefund | Fehlertyp | Handlungsbedarf |
|---|---|---|---|---|
| [Aussage 1] | § X JVEG | [Befund] | [Tatbestand/Ermessen/Rechtsfolge] | [Ja/Nein] |
| [Aussage 2] | § Y JVEG | [Befund] | — | — |

**Frist für Antwort/Beschwerde:** TT.MM.JJJJ
**Empfehlung:** [Gegendarstellung / Beschwerde / Keine Maßnahme]

## Ausgabe
Strukturierte Schreibenanalyse mit Fehlertypen, Normverweisen und Handlungsempfehlung.

## Leitplanken
- Jede Aussage einzeln prüfen; keine Pauschalzustimmung.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 2. `jveg-kommandocenter`

**Fokus:** Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis zum richtigen JVEG-Skill. Abgrenzung: kein inhaltlicher Berechnungs-Skill.

# JVEG-Kommandocenter

## Fachkern: JVEG-Kommandocenter
- **Spezialgegenstand:** JVEG-Kommandocenter wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Erfasse alle Parameter eines JVEG-Kostenvorgangs und erstelle eine vollständige Kostenlandkarte, die den Prüfvorgang strukturiert und an die passendes Fachmoduls weiterleitet.

## Triage — kläre vor dem Start

1. **Anspruchsberechtigter:** Welche Rolle hat die Person (§ 2 JVEG)?
2. **Leistungsart:** Sachverständigengutachten, Dolmetscherleistung, Zeugnis, Übersetzung?
3. **Gewünschter Output:** Prüfmatrix, Antragsschreiben, Beschwerdeschrift oder Rechenblatt?
4. **Fristen:** Dreimonatsfrist § 23 JVEG — noch offen oder bereits versäumt?
5. **Vorschussstand:** Wurde ein Vorschuss gewährt, und wenn ja, in welcher Höhe?

## Speziallogik: Kostenlandkarte
Das Kommandocenter baut zu Beginn eine strukturierte Übersicht aller Anspruchspositionen:
- Jede Position wird einer Normengruppe zugeordnet.
- Offene Fragen und fehlende Belege werden markiert.
- Die Landkarte dient als Steuerungsgrundlage für nachgelagerte Skills.

## Zentrale Normen
- § 1 JVEG (Anwendungsbereich)
- § 2 JVEG (Anspruchsberechtigte)
- § 3 JVEG (Vorschuss)
- § 4 JVEG (Festsetzung)
- § 23 JVEG (Dreimonatsfrist)
- §§ 5–22 JVEG (Vergütungsgruppen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Jeder neue JVEG-Kostenvorgang oder wenn Überblick über einen laufenden Vorgang gefragt ist.

## Arbeitsweise
1. Rolle und Anspruchsart nach § 2 JVEG klären.
2. Alle geltend gemachten Positionen erfassen.
3. Kostenlandkarte erstellen (Positionen → Normen → offene Punkte).
4. Frist § 23 JVEG prüfen.
5. An Fachmodule weiterleiten (Fahrtkosten, Sachverständige, Dolmetscher, Zeugen).

## Output-Template

**Kostenlandkarte — JVEG-Vorgang**

| Position | Betrag (EUR) | Norm | Beleg vorhanden | Spezialist-Skill |
|---|---|---|---|---|
| [Position 1] | 00,00 | § X JVEG | Ja/Nein | jveg-fahrtkosten |
| [Position 2] | 00,00 | § Y JVEG | Ja/Nein | jveg-sachverstaendigenrechnung |
| **Gesamtbetrag** | **00,00** | | | |

**Fristenstatus § 23 JVEG:** [Fristende TT.MM.JJJJ]
**Vorschussstand:** [EUR / Kein Vorschuss]
**Nächste Schritte:** [Skill-Weiterleitungen]

## Ausgabe
Vollständige Kostenlandkarte mit Normenzuordnung, Belegstatus und Skill-Routing.

## Leitplanken
- Kostenlandkarte immer zuerst; keine Position ohne Normbezug.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 3. `jveg-kuerzung-wegfall-8a`

**Fokus:** Kuerzung oder Wegfall der JVEG-Verguetung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit Begründung. Abgrenzung: nicht Dreimonatsfrist § 2 JVEG.

# JVEG-Kuerzung-Wegfall-8a

## Fachkern: JVEG-Kuerzung-Wegfall-8a
- **Spezialgegenstand:** JVEG-Kuerzung-Wegfall-8a wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe, ob und in welchem Umfang die Sachverständigenvergütung nach § 8a JVEG gekürzt oder vollständig versagt werden kann, und identifiziere die maßgeblichen Kürzungsrisiken.

## Triage — kläre vor der Prüfung

1. **Gutachtenmängel:** Welche konkreten Mängel werden dem Gutachten vorgeworfen (Unvollständigkeit, Methodenfehler, fehlende Begründung)?
2. **Verwertbarkeit:** Ist das Gutachten für das Verfahren verwertbar oder nicht (Kernfrage für § 8a JVEG)?
3. **Hinweisobliegenheit:** Hat der Sachverständige das Gericht rechtzeitig auf Probleme oder Mehrstunden hingewiesen?
4. **Vorschussüberschreitung:** Wurde der bewilligte Vorschuss überschritten — hat der Sachverständige vorher um Erhöhung nachgefragt?
5. **Befangenheit:** Liegt ein rechtskräftig festgestellter Befangenheitsgrund vor?

## Zentrale Normen
- § 8a JVEG (Kürzung/Wegfall der Sachverständigenvergütung)
- § 8 JVEG (Sachverständigenvergütung: Grundlage)
- § 9 JVEG (Honorargruppen)
- § 3 JVEG (Vorschuss — Überschreitung)
- § 407a ZPO (Hinweisobliegenheit des Sachverständigen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Gutachten liegt vor und Kostenbeamter oder Gericht erwägt Kürzung nach § 8a JVEG.

## Arbeitsweise
1. Gutachten auf Vollständigkeit und Verwertbarkeit bewerten.
2. Hinweisobliegenheiten und Vorschusssituation prüfen.
3. Befangenheitsprotokoll einsehen.
4. Kürzungsrisiko kategorisieren (keine / teilweise / vollständige Kürzung).
5. Kürzungsbetrag berechnen und Begründung formulieren.

## Output-Template

| Kürzungsrisiko | Norm | Befund | Risikograd | Kürzungsbetrag (EUR) |
|---|---|---|---|---|
| Verwertbarkeit | § 8a JVEG | [Befund] | [Gering/Mittel/Hoch] | 00,00 |
| Hinweisobliegenheit | § 407a ZPO | [Befund] | [Gering/Mittel/Hoch] | 00,00 |
| Vorschussüberschreitung | § 3 JVEG | [Befund] | [Gering/Mittel/Hoch] | 00,00 |
| Befangenheit | § 8a JVEG | [Befund] | [Gering/Mittel/Hoch] | 00,00 |
| **Gesamtkürzung** | | | | **00,00** |

## Ausgabe
Risikoübersicht mit Kürzungsbeträgen, Normbezug und Begründungsentwurf.

## Leitplanken
- § 8a JVEG ist Ausnahmetatbestand; Kürzungen müssen konkret begründet werden.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
