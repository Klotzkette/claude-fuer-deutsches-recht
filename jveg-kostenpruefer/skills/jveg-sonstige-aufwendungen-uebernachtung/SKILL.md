---
name: jveg-sonstige-aufwendungen-uebernachtung
description: "Sonstige Aufwendungen Uebernachtung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sonstige Aufwendungen Uebernachtung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Sonstige Aufwendungen Uebernachtung** im Plugin JVEG-Kostenprüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jveg-sonstige-aufwendungen-belege` | Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Hoehe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG. Abgrenzung: nicht Fahrtkosten oder Übernachtung. |
| `jveg-uebernachtung-aufwand` | Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output: Übernachtungskosten-Nachweis JVEG. Abgrenzung: nicht Fahrtkosten § 5 JVEG. |
| `jveg-verdienstausfall-haushalt-zeit` | Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output: Verdienstausfall-Berechnung JVEG. Abgrenzung: nicht Sachverständigenverguetung. |

## Arbeitsweg

Im Plugin JVEG-Kostenprüfer gilt für **Sonstige Aufwendungen Uebernachtung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jveg-sonstige-aufwendungen-belege`

**Fokus:** Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Hoehe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG. Abgrenzung: nicht Fahrtkosten oder Übernachtung.

# JVEG-Sonstige-Aufwendungen-Belege

## Fachkern: JVEG-Sonstige-Aufwendungen-Belege
- **Spezialgegenstand:** JVEG-Sonstige-Aufwendungen-Belege wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe sonstige Aufwendungen und bare Auslagen (Begleitpersonen, Kopien, Dateien, Vertretungskosten) auf Notwendigkeit, Normkonformität und Belegfähigkeit nach JVEG.

## Triage — kläre vor der Prüfung

1. **Aufwendungsart:** Kopien, Dateien, Begleitperson, Vertretungskosten oder sonstige bare Auslagen?
2. **Notwendigkeit:** Waren die Aufwendungen für die Auftragserfüllung notwendig (Wirtschaftlichkeitsgebot)?
3. **Belege:** Liegen Originalquittungen oder sonstige Belege vor?
4. **Begleitperson:** Ist die Mitnahme einer Begleitperson medizinisch oder faktisch notwendig nachgewiesen?
5. **Normgrundlage:** Ist die konkrete Aufwendung im JVEG geregelt oder nur analog zu behandeln?

## Zentrale Normen
- § 7 Abs. 2 JVEG (Reisenebenkosten, bare Auslagen)
- § 12 JVEG (Nebenkosten Sachverständige: Kopien, Dateien, Lichtbilder)
- § 5 Abs. 4 JVEG (Parkkosten und Sonderreisenebenkosten)
- § 6 JVEG (Sonderfall Begleitperson bei Reise)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Rechnung enthält Positionen jenseits von Honorar, Reisezeit und Fahrtkosten.

## Arbeitsweise
1. Jede sonstige Position isolieren.
2. Normgrundlage im JVEG bestimmen.
3. Notwendigkeit und Wirtschaftlichkeit prüfen.
4. Beleg vorhanden/fehlend markieren.
5. Erstattungsfähigen Betrag berechnen.

## Output-Template

| Position | Norm | Betrag geltend (EUR) | Beleg | Notwendig | Anerkannt (EUR) |
|---|---|---|---|---|---|
| Kopien [X × Y EUR] | § 12 JVEG | 00,00 | Ja/Nein | Ja/Nein | 00,00 |
| Begleitperson | § 6 JVEG | 00,00 | Ja/Nein | Ja/Nein | 00,00 |
| Sonstige bare Auslagen | § 7 Abs. 2 JVEG | 00,00 | Ja/Nein | Ja/Nein | 00,00 |
| **Gesamt** | | **00,00** | | | **00,00** |

## Ausgabe
Prüfergebnis für Sammelposition sonstige Aufwendungen mit Belegstatus.

## Leitplanken
- Kein Ansatz ohne Normgrundlage; Analogie nur in engen Grenzen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 2. `jveg-uebernachtung-aufwand`

**Fokus:** Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output: Übernachtungskosten-Nachweis JVEG. Abgrenzung: nicht Fahrtkosten § 5 JVEG.

# JVEG-Uebernachtung-Aufwand

## Fachkern: JVEG-Uebernachtung-Aufwand
- **Spezialgegenstand:** JVEG-Uebernachtung-Aufwand wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe Ansprüche auf Tagegeld und Übernachtungsgeld nach §§ 11–12 JVEG auf Notwendigkeit, Obergrenzen und Belegpflicht unter Berücksichtigung des BRKG.

## Triage — kläre vor der Prüfung

1. **Reisedauer:** Wie viele Tage und Nächte umfasst die Reise — ist Übernachtung notwendig oder nur wünschenswert?
2. **BRKG-Anknüpfung:** Gilt das Bundesreisekostengesetz als Obergrenze für Tagegeld und Übernachtung?
3. **Belegpflicht:** Liegt eine Hotelrechnung im Original vor?
4. **Obergrenzen:** Überschreitet die Übernachtungsrechnung die gerichtliche Höchstgrenze?
5. **Tagegelder:** Sind Anreise- und Abreisetag korrekt mit reduziertem Tagegeld angesetzt?

## Zentrale Normen
- § 11 JVEG (Tagegeld — Verweis auf BRKG)
- § 12 JVEG (Übernachtungsgeld — Höchstbetrag)
- BRKG § 9 (Tagegeld-Staffelung)
- BRKG § 8 (Übernachtungskosten — Bundesreisekostenrecht)
- § 5 JVEG (Fahrtkostenabgrenzung)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Reise-/Übernachtungsposition in JVEG-Rechnung oder Kostenfestsetzungsantrag.

## Arbeitsweise
1. Reisedauer und Notwendigkeit der Übernachtung feststellen.
2. BRKG-Obergrenzen für Tagegeld ermitteln.
3. Tagegeld für An-/Abreisetag gesondert berechnen.
4. Übernachtungsbeleg prüfen und mit Obergrenze vergleichen.
5. Erstattungsfähigen Betrag berechnen.

## Output-Template

| Position | Geltend (EUR) | Norm | Obergrenze | Beleg | Anerkannt (EUR) |
|---|---|---|---|---|---|
| Tagegeld Tag 1 (An-) | 00,00 | § 11 JVEG, BRKG § 9 | 00,00 | — | 00,00 |
| Tagegeld Tag 2 | 00,00 | § 11 JVEG, BRKG § 9 | 00,00 | — | 00,00 |
| Tagegeld Tag 3 (Ab-) | 00,00 | § 11 JVEG, BRKG § 9 | 00,00 | — | 00,00 |
| Übernachtung Nacht 1 | 00,00 | § 12 JVEG | 00,00 | Anlage X | 00,00 |
| **Gesamt** | **00,00** | | | | **00,00** |

## Ausgabe
Prüfergebnis für Tagegeld und Übernachtung mit BRKG-Abgleich und Belegnachweisen.

## Leitplanken
- BRKG-Obergrenzen sind zwingend; Überschreitung ohne besondere Begründung wird nicht anerkannt.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 3. `jveg-verdienstausfall-haushalt-zeit`

**Fokus:** Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output: Verdienstausfall-Berechnung JVEG. Abgrenzung: nicht Sachverständigenverguetung.

# JVEG-Verdienstausfall-Haushalt-Zeit

## Fachkern: JVEG-Verdienstausfall-Haushalt-Zeit
- **Spezialgegenstand:** JVEG-Verdienstausfall-Haushalt-Zeit wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Trenne und berechne die Ansprüche auf Verdienstausfallentschädigung, Haushaltführungsschaden und Zeitversäumnis nach §§ 20–22 JVEG und verhindere Doppelerfassung.

## Triage — kläre vor der Prüfung

1. **Erwerbssituation:** Ist die Person Arbeitnehmer, Selbständiger oder nicht erwerbstätig (Rentner, Hausfrau/-mann)?
2. **Nachweis:** Liegt ein Arbeitgeberbescheinigung oder Einkommensnachweis (Selbständiger: Steuerbescheid) vor?
3. **Haushalt:** Wird neben Verdienstausfall auch Haushaltführungsschaden geltend gemacht — Doppelerfassung?
4. **Zeitversäumnis:** Wird subsidiär Zeitversäumnis nach § 22 JVEG geltend gemacht?
5. **Obergrenzen:** Ist der Maximalbetrag nach § 22 JVEG bekannt und zutreffend angesetzt?

## Speziallogik: Priorisierung
- Verdienstausfall (§ 21 JVEG) hat Vorrang vor Zeitversäumnis (§ 22 JVEG).
- Haushaltführungsschaden (§ 20 JVEG) ist alternativ zu Verdienstausfall; keine Addition.
- Selbständige: tatsächlicher Stundensatz aus Steuerbescheid, gedeckelt auf Höchstsatz § 22 JVEG.

## Zentrale Normen
- § 20 JVEG (Haushaltführungsschaden)
- § 21 JVEG (Verdienstausfall — Arbeitnehmer und Selbständige)
- § 22 JVEG (Zeitversäumnis — Auffangtatbestand)
- § 19 JVEG (Zeugenfahrtkosten — abzugrenzen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. LG München I, Beschl. v. 15.04.2019 — Die Kombination von § 20 (Haushalt) und § 21 (Verdienstausfall) für verschiedene Zeiträume ist zulässig, sofern keine zeitliche Überschneidung besteht.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Zeuge oder Zeugensachwalter meldet sich wegen Verdienstausfall, Haushaltführungsschaden oder Zeitversäumnis.

## Arbeitsweise
1. Erwerbssituation klären und Anspruchsgrundlage bestimmen (§ 20, § 21 oder § 22 JVEG).
2. Doppelerfassung ausschließen.
3. Zeitraum und Stundenzahl mit Beleg dokumentieren.
4. Stundensatz berechnen und auf Höchstsatz kappen.
5. Gesamtanspruch ausweisen.

## Output-Template

| Anspruch | Norm | Stunden | Stundensatz (EUR) | Beleg | Anerkannt (EUR) |
|---|---|---|---|---|---|
| Verdienstausfall | § 21 JVEG | X | Y | Anlage X | 00,00 |
| Haushaltführungsschaden | § 20 JVEG | X | Y | Anlage X | 00,00 |
| Zeitversäumnis | § 22 JVEG | X | Max. | — | 00,00 |
| **Gesamt** | | | | | **00,00** |

**Doppelerfassungscheck:** [Keine Überschneidung / Überschneidung: [Beschreibung]]

## Ausgabe
Bereinigter Anspruch ohne Doppelerfassung, mit Stundensatzberechnung und Belegnachweisen.

## Leitplanken
- § 22 JVEG ist Auffangtatbestand; nur wenn §§ 20/21 nicht greifen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
