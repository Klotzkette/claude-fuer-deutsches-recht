---
name: legistik-werkstatt-folgenabschaetzung-erfuellungsaufwand
description: "Folgenabschaetzung Erfuellungsaufwand: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Folgenabschaetzung Erfuellungsaufwand

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Folgenabschaetzung Erfuellungsaufwand** im Plugin Legistik Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik Leitfaden BMJ BMI Statistisches Bundesamt Fallzahlen Bearbeitungszeit Lohnsatz. Pro Vorschrift pro Adressat Bagatell-Schwelle KMU-Aspekt mittelstandsrelevant. One-in-one-out-Regel der Bundesregierung. Output Erfuellungsaufwand-Tabelle Vorblatt Begründung Empfehlung NKR-Vorlage. Abgrenzung zu folgenabschaetzung-nachhaltigkeit SDG-Folgen. |
| `folgenabschaetzung-nachhaltigkeit` | Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen Bewertung positiv neutral negativ. Demografiecheck Wirkung auf aeltere Buerger Familien. Gleichstellungspolitischer Check Art. 3 GG Equal Pay. Klimacheck Treibhausgasemissionen Ressourcenverbrauch. Soziale Folgen Inklusion Teilhabe. Output Folgenmatrix Vorblatt Abschnitt G Begründung A.VI.6. Abgrenzung zu folgenabschaetzung-erfuellungsaufwand Buerokratiekosten. |
| `formulierungshilfe-bauen` | Formulierungshilfen, Aenderungsantraege, Gesetzentwuerfe aus der Mitte des Bundestages oder Landtages, Entschliessungsantraege und parlamentarische Antraege bauen. Anwendungsfall Bundesministerium liefert fachlich zu, Koalitionsfraktion will einen laufenden Gesetzentwurf aendern, Oppositionsfraktion baut einen eigenen Antrag oder Entwurf, Landtagsfraktion braucht eine landesspezifische Vorlage. Klaert formalen Initiator, fachlichen Verfasser, Parlament, Bundesland, Drucksache, Ausschuss, Lesung, GO-BT oder Landtags-GO. Output einreichungsfaehiger Antrag mit Normtext, Begruendung, Kurzvermerk, Synopse-Hinweis und Pflichtquercheck. |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73 GG. Konkurrierende Kompetenz Art. 72 i.V.m. 74 GG Erforderlichkeitsklausel Abweichung Laender. Auffangkompetenz Laender Art. 70 GG Sperrwirkung Bundesrecht. Annexkompetenz Kompetenz kraft Sachzusammenhangs BVerfGE 3/407. Bei Landesgesetzen zusaetzlich Landesverfassung. Output Gutachten ein bis zwei Seiten Empfehlung Tragfähigkeit. Abgrenzung zu normhierarchie-routing Normebenenwahl. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Folgenabschaetzung Erfuellungsaufwand**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `folgenabschaetzung-erfuellungsaufwand`

**Fokus:** Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik Leitfaden BMJ BMI Statistisches Bundesamt Fallzahlen Bearbeitungszeit Lohnsatz. Pro Vorschrift pro Adressat Bagatell-Schwelle KMU-Aspekt mittelstandsrelevant. One-in-one-out-Regel der Bundesregierung. Output Erfuellungsaufwand-Tabelle Vorblatt Begründung Empfehlung NKR-Vorlage. Abgrenzung zu folgenabschaetzung-nachhaltigkeit SDG-Folgen.


# Folgenabschätzung - Erfüllungsaufwand

> Was kostet die neue Norm den Bürger, die Wirtschaft, die Verwaltung?

## Methodik

Leitfaden zur Ermittlung und Darstellung des Erfüllungsaufwands (BMJ / BMI / DESTATIS, Stand laufend aktualisiert).

## Drei Adressaten

### Bürger
Aufwand: Lese-, Antrags-, Beleg-Pflichten. Bemessung: Zeitkosten (oft 28 EUR/h Standard).

### Wirtschaft
Aufwand: betriebliche Umsetzung, IT-Anpassung, Dokumentation, Prüfung. Bemessung: Lohnkosten plus Sachkosten plus einmalige Umstellungskosten.

### Verwaltung
Aufwand: Personal, IT, Sachmittel. Bemessung: Vollkostenrechnung des Bundes / Landes / Gemeinde.

## Ermittlung

1. **Fallzahlen ermitteln**: wie viele Adressaten? Wie oft pro Jahr?
2. **Pro Fall Bearbeitungszeit**: in Minuten oder Stunden
3. **Lohnsatz**: nach DESTATIS oder geschätzt
4. **Multiplikation**

Beispiel:

| Vorschrift | Adressat | Fallzahl/Jahr | Bearbeitungszeit | Lohnsatz | Erfüllungsaufwand/Jahr |
|---|---|---|---|---|---|
| Paragraf 33a HGB neu | Unternehmen | 1.4 Mio | 30 min/Fall einmalig | 41 EUR/h | 28.7 Mio EUR (einmalig) |
| Paragraf 33a HGB neu | Unternehmen | 1.4 Mio | 5 min/Jahr | 41 EUR/h | 4.8 Mio EUR p.a. |

## Bagatellschwelle

Wenn Erfüllungsaufwand unter 1 Mio EUR p.a. - in der Regel "kein nennenswerter Aufwand". Dennoch dokumentieren.

## KMU-Prüfung

Wenn KMU betroffen: Prüfung Verhältnismaessigkeit. Ggf. Schwellenwerte einführen, ggf. Übergangsregelungen, ggf. Ausnahmen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 44a, 62 GGO (Erfuellungsaufwand-Berechnung, Folgenabschaetzung) — §§ 1-4 SKMBericht (Statistisches Bundesamt, Standardkosten-Modell) — Art. 5 Abs. 4 EUV (EU-Verhaeltnismaessigkeit) — § 39a VwVfG (Vorwegbegruendung bei Massenverfahren)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Tabelle plus Beschreibung in Vorblatt-Abschnitt E und in Begründung-Abschnitt A.VI.4.

## Anschluss

`folgenabschaetzung-nachhaltigkeit`, `normenkontrollrat-kmu-check`.

## 2. `folgenabschaetzung-nachhaltigkeit`

**Fokus:** Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen Bewertung positiv neutral negativ. Demografiecheck Wirkung auf aeltere Buerger Familien. Gleichstellungspolitischer Check Art. 3 GG Equal Pay. Klimacheck Treibhausgasemissionen Ressourcenverbrauch. Soziale Folgen Inklusion Teilhabe. Output Folgenmatrix Vorblatt Abschnitt G Begründung A.VI.6. Abgrenzung zu folgenabschaetzung-erfuellungsaufwand Buerokratiekosten.


# Folgenabschätzung - Nachhaltigkeit

> Was bewirkt das Vorhaben jenseits des unmittelbaren Regelungsziels?

## Pruefdimensionen

### A - Nachhaltigkeit nach UN-SDG

17 Sustainable Development Goals der UN, Resolution 70/1 von 2015. Pro Vorhaben Prüfung:

- SDG 1 Keine Armut - betroffen ja/nein, positiv/negativ
- SDG 3 Gesundheit
- SDG 4 Bildung
- SDG 5 Geschlechtergleichheit
- SDG 8 Würdige Arbeit
- SDG 10 Weniger Ungleichheit
- SDG 13 Klimaschutz
- SDG 16 Frieden, Gerechtigkeit, starke Institutionen

### B - Demografiecheck

- aeltere Bürger
- Kinder und Jugendliche
- Familien
- Single-Haushalte

### C - Gleichstellungspolitischer Check

- Wirkung auf Frauen vs. Männer
- Care-Arbeit
- Equal Pay
- Gewaltschutz

### D - Klimacheck

Klimaschutzgesetz Paragraf 13. Wirkung auf Treibhausgasemissionen direkt und indirekt.

### E - Soziale Folgen

- Inklusion behinderte Menschen
- Migration / Integration
- Armut / Wohnungslosigkeit

### F - Wirkung auf laendliche Räume

- gleichwertige Lebensverhältnisse Art. 72 Abs. 2 GG

### G - Wirkung auf KMU

(Querverweis `normenkontrollrat-kmu-check`)

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 3-6 UVPG (Umweltvertraeglichkeitspruefung) — Art. 20a GG (Staatsziel Umweltschutz) — §§ 4-6 KSG (Klimaschutzziele, Sektorziele) — DNK Deutsche Nachhaltigkeitsstrategie — § 65 GGO (Nachhaltigkeitspruefung in Begruendung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Folgenmatrix als Tabelle plus Text für Vorblatt G und Begründung A.VI.6.

## Anschluss

`inkrafttreten-uebergangsrecht`.

## 3. `formulierungshilfe-bauen`

**Fokus:** Formulierungshilfen, Aenderungsantraege, Gesetzentwuerfe aus der Mitte des Bundestages oder Landtages, Entschliessungsantraege und parlamentarische Antraege bauen. Anwendungsfall Bundesministerium liefert fachlich zu, Koalitionsfraktion will einen laufenden Gesetzentwurf aendern, Oppositionsfraktion baut einen eigenen Antrag oder Entwurf, Landtagsfraktion braucht eine landesspezifische Vorlage. Klaert formalen Initiator, fachlichen Verfasser, Parlament, Bundesland, Drucksache, Ausschuss, Lesung, GO-BT oder Landtags-GO. Output einreichungsfaehiger Antrag mit Normtext, Begruendung, Kurzvermerk, Synopse-Hinweis und Pflichtquercheck.


# Formulierungshilfe und parlamentarische Vorlage bauen

> Für Ministerialzulieferung, Koalitionsänderung, Oppositionsantrag und Landtagsvorlage. Formal sauber, politisch brauchbar, rechtsförmlich prüfbar.

## Was dieser Skill abdeckt

| Modus | Wer steuert typischerweise? | Ergebnis | Besonderheit |
|---|---|---|---|
| Ministerielle Formulierungshilfe | Bundes- oder Landesministerium liefert fachlich zu | Änderungsantrag, Ausschussfassung, Kurzbegründung, Hintergrundvermerk | Fachlicher Verfasser und formaler parlamentarischer Initiator sind getrennt zu dokumentieren. |
| Gesetzentwurf aus der Mitte des Bundestages | Fraktion oder Abgeordnete in der erforderlichen Stärke | Vollständiger Gesetzentwurf mit Begründung und Synopse-Hinweis | Art. 76 GG und GO-BT beachten; keine Regierungsvorlage vortäuschen. |
| Gesetzentwurf aus der Mitte eines Landtags | Landtagsfraktion, Gruppe oder Abgeordnete nach Landesrecht | Landesgesetzentwurf mit landesspezifischem Format | Bundesland, Landesverfassung und Landtags-GO sind Pflichtfelder. |
| Änderungsantrag | Koalition, Opposition, Ausschuss oder Fraktion im laufenden Verfahren | Präziser Änderungsbefehl mit kurzer Begründung | Bezug zur Drucksache, Lesung und Ausschussberatung muss stimmen. |
| Antrag / Entschließungsantrag | Fraktion, Gruppe oder Abgeordnete | Beschlussvorschlag ohne zwingenden Normtext | Politische Forderung, Prüfauftrag oder Aufforderung an Regierung klar formulieren. |

## Intake

Vor dem Entwurf diese Punkte klären. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und weiterarbeiten.

| Punkt | Frage |
|---|---|
| Parlament | Bundestag oder welcher Landtag? |
| Bundesland | Nur bei Landtag/Landesregierung: welches Bundesland und welche Landes-GO? |
| Formaler Initiator | Bundesregierung/Bundesrat? Fraktion? Gruppe? Abgeordnete in erforderlicher Stärke? Ausschuss? |
| Fachlicher Verfasser | Ministerium, Fraktion, wissenschaftlicher Dienst, Verband, Anwalt, Arbeitsgruppe? |
| Politische Rolle | Koalition, Opposition, Regierung, Ausschussmehrheit, Minderheitenposition? |
| Verfahrensstand | Drucksache, 1./2./3. Lesung, Ausschuss, Anhörung, Vermittlung, Landtagsstadium? |
| Zieltyp | Normtext ändern, neuer Gesetzentwurf, Entschließungsantrag, Antrag, Prüfbitte, Haushalts-/Vollzugsauftrag? |
| Frist | Drucksachenschluss, Ausschussfrist, Plenartermin, Kabinetts- oder Fraktionssitzung? |
| Risiko | Kompetenz, Verfassungsrecht, EU-Recht, Haushalt, Vollzug, NKR/Erfüllungsaufwand, politische Angreifbarkeit? |

## Grundregeln

1. **Formalen Absender nicht verwischen.** Ein Ministerium kann fachlich zuliefern, aber eine Vorlage "aus der Mitte des Bundestages" wird parlamentarisch eingebracht.
2. **Oppositionsvorhaben eigenständig behandeln.** Keine Kabinetts-, Ressort- oder NKR-Prüfung als formale Einreichungsvoraussetzung behaupten; trotzdem Kompetenz, Grundrechte, EU-Recht, Haushalt und Vollzug prüfen.
3. **Landesvorhaben nicht im Bundesformat schreiben.** Bundesland, Landesverfassung, Landtags-GO, Zitierstil, Verkündungsblatt und Haushaltsregeln abfragen.
4. **Änderungsbefehle präzise halten.** Jede Änderung braucht Normstelle, Befehl, neuen Wortlaut und Begründung.
5. **Bei Eile Minimalprüfung festhalten.** Wenn keine Zeit für Vollprüfung bleibt, Ergebnis als "vorläufig, zu verifizieren" kennzeichnen und die offenen Punkte auflisten.

## Wann welcher Modus passt

- **Formulierungshilfe:** Es gibt ein laufendes Verfahren und der Text soll als Änderungsantrag oder Ausschussformulierung in dieses Verfahren hinein.
- **Gesetzentwurf aus der Mitte:** Es soll ein vollständiges Gesetz als parlamentarische Initiative eingebracht werden, auch durch eine Oppositionsfraktion.
- **Änderungsantrag:** Ein bestehender Entwurf soll punktuell oder systematisch geändert werden.
- **Entschließungsantrag:** Das Parlament soll eine politische Erwartung, Prüfbitte oder Aufforderung beschließen.
- **Antrag:** Das Parlament soll einen eigenständigen Beschluss fassen, ohne unmittelbar Gesetzestext zu ändern.

## Output-Muster

### A. Änderungsantrag

```text
Der Ausschuss für ... wolle beschließen:

Zu dem Gesetzentwurf auf Drucksache ... wird Artikel ... wie folgt geändert:

1. ...
2. ...

Begründung
Die Änderung ...
```

### B. Gesetzentwurf aus der Mitte des Bundestages oder Landtages

```text
Entwurf eines Gesetzes ...

A. Problem und Ziel
...

B. Lösung
...

Der Bundestag / Landtag hat das folgende Gesetz beschlossen:
...

Begründung
A. Allgemeiner Teil
B. Besonderer Teil
```

Bei Bundesgesetzen zusätzlich prüfen, ob eine Synopse beizufügen ist und ob Art. 76 GG/GO-BT-Anforderungen erfüllt sind. Bei Landesgesetzen die landesspezifische Drucksachen- und Begründungsstruktur verwenden.

### C. Antrag oder Entschließungsantrag

```text
Der Bundestag / Landtag wolle beschließen:

I. Der Bundestag / Landtag stellt fest:
...

II. Der Bundestag / Landtag fordert die Bundesregierung / Landesregierung auf:
1. ...
2. ...

Begründung
...
```

### D. Interner Kurzvermerk

Immer mitliefern, wenn das praktisch hilft:

- Verfahrensstand und Drucksache
- formaler Initiator und fachlicher Verfasser
- Kompetenzgrundlage
- Verfassungs- und EU-Kurzcheck
- Haushalts- und Vollzugseffekte
- Synopse-/Lesefassungsbedarf
- offene Prüf- und Abstimmungspunkte

## Pflichtquercheck

Auch bei schnellen parlamentarischen Texten intern prüfen und sichtbar dokumentieren:

- `gesetzgebungskompetenz-pruefen` - Bund/Land und Kompetenzgrundlage
- `verfassungsmaessigkeit-quercheck` - Grundrechte, Bestimmtheit, Verhältnismäßigkeit, Wesentlichkeit
- `europarechtskonformitaet` - EU-Recht, Notifizierung 2015/1535, Beihilfe, Richtlinienumsetzung
- `folgenabschaetzung-erfuellungsaufwand` - auch wenn NKR formal nicht der Einreichungspfad ist, Erfüllungsaufwand als politisches Risiko erfassen
- `synopse-erstellen` - bei Änderungen an geltendem Recht
- `dokumente-rendern-docx-pdf` - am Ende für BT-/Landtagsdrucksachen- oder Ministeriumsformat

## Arbeitsgrundlagen

- Art. 76 Abs. 1 GG: Bundesregierung, Mitte des Bundestages und Bundesrat als Initiativberechtigte im Bund.
- GO-BT, insbesondere Vorschriften zu Vorlagen von Mitgliedern des Bundestages, Anträgen und Synopsen bei Änderung geltender Gesetze.
- GGO, insbesondere Regelungen zur Zusammenarbeit mit Bundestag/Bundesrat und zu Formulierungshilfen.
- Landesverfassungen und Geschäftsordnungen der Landtage für landesspezifische Initiativen.
- Handbuch der Rechtsförmlichkeit des BMJ als Formulierungs- und Strukturmaßstab, soweit passend oder als Bundesstandard übernommen.

## Zentrale Normen (Paragrafenkette)

Art. 76 Abs. 1 GG — GO-BT Vorlagen/Anträge — Art. 70-74 GG — Art. 20 Abs. 3 GG — Art. 103 Abs. 2 GG bei Straf- oder Bußgeldnormen — Landesverfassung und Landtags-GO bei Landesvorhaben — GGO bei ministerieller Zulieferung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- `Parlamentarische_Vorlage_[Kurztitel].md` mit Normtext oder Antrag, Begründung und internem Kurzvermerk
- optional `Synopse_[Kurztitel].md`
- optional Render-Paket für `dokumente-rendern-docx-pdf`

## Anschluss

`gesetzgebungskompetenz-pruefen`, `verfassungsmaessigkeit-quercheck`, `europarechtskonformitaet`, `synopse-erstellen`, `dokumente-rendern-docx-pdf`.

## 4. `gesetzgebungskompetenz-pruefen`

**Fokus:** Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73 GG. Konkurrierende Kompetenz Art. 72 i.V.m. 74 GG Erforderlichkeitsklausel Abweichung Laender. Auffangkompetenz Laender Art. 70 GG Sperrwirkung Bundesrecht. Annexkompetenz Kompetenz kraft Sachzusammenhangs BVerfGE 3/407. Bei Landesgesetzen zusaetzlich Landesverfassung. Output Gutachten ein bis zwei Seiten Empfehlung Tragfähigkeit. Abgrenzung zu normhierarchie-routing Normebenenwahl.


# Gesetzgebungskompetenz prüfen

> Kompetenz vor Inhalt. Ohne Kompetenz ist der ganze Entwurf umsonst.

## Pruefstation 1 - Bund oder Land?

- Bestimmung der **Materie**: was wird geregelt? Materielles Recht, Verfahrensrecht, Organisation, oder Mischung?
- Suche in **Art. 73 GG** (ausschließliche Bundeskompetenz, 14 Nummern): von Außenpolitik über Verteidigung, Staatsangehoerigkeit, Wahrungseinheit, Bundeseisenbahnen, Postwesen, Telekommunikation, Bundeskriminalpolizei, Zoelle bis zu Atomenergie.
- Suche in **Art. 74 GG** (konkurrierende Kompetenz, 33 Nummern): von Bürgerlichem Recht (Nr. 1), Strafrecht (Nr. 1), Aufenthaltsrecht, öffentliche Fürsorge, Arbeitsrecht, Wirtschaft, Recht der Bodenverteilung, Wohnungswesen, Straßenverkehr, Atomenergie-Förderung, Boden- und Tierschutz, Lebensmittel- und Bedarfsgegenstände, Hochschulrahmenrecht, Umweltvertraeglichkeitsprüfung, Krankenhaus, Gentechnik, Schienenwegeplanung, etc.

Wenn nichts passt: Landeskompetenz Art. 70 Abs. 1 GG.

## Pruefstation 2 - Erforderlichkeitsklausel Art. 72 Abs. 2 GG

Bei den in Art. 72 Abs. 2 GG aufgezaehlten Materien (z.B. Aufenthalt, öffentliche Fürsorge, Wirtschaft, Hochschulen, Straßenverkehr) braucht der Bund eine zusätzliche Erforderlichkeit:

- "wenn und soweit die Herstellung gleichwertiger Lebensverhältnisse im Bundesgebiet oder die Wahrung der Rechts- oder Wirtschaftseinheit im gesamtstaatlichen Interesse eine bundesgesetzliche Regelung erforderlich macht"

Erforderlichkeitsprüfung in die Begründung des Entwurfs (Abschnitt A I 4) aufnehmen.

## Pruefstation 3 - Abweichungskompetenz Art. 72 Abs. 3 GG

Bei sechs Materien (Jagdwesen, Naturschutz, Bodenverteilung, Raumordnung, Wasserhaushalt, Hochschulzulassung) duerfen Länder abweichende Regelungen treffen. Bundesgesetz muss damit rechnen und eine Anwendungsvorschrift gegen die Abweichung enthalten.

## Pruefstation 4 - Annexkompetenz, Kompetenz kraft Sachzusammenhangs

BVerfGE 3 / 407 (Baurecht): Bund darf in einer Materie Bestimmungen treffen, die nicht ausdruecklich zu seinen Kompetenzen zaehlen, wenn das für den Vollzug der ihm zugewiesenen Materie erforderlich ist. Annexkompetenzen sind eng auszulegen.

## Pruefstation 5 - Sperrwirkung

Hat der Bund von seiner konkurrierenden Kompetenz Gebrauch gemacht? Dann Sperrwirkung für Länder (Art. 72 Abs. 1 GG). Es sei denn: Bund hat ausdruecklich Lückenraum gelassen.

## Pruefstation 6 - Landesverfassung

Wenn Landesgesetz: Prüfung der Landesverfassung. Hat das Land Selbstverwaltung der Kommunen zu wahren (Art. 28 Abs. 2 GG analog Landesverfassungen)? Greift das Gesetz in ein landesverfassungsrechtliches Grundrecht ein (z.B. Bayerische Verfassung Art. 101 Wohnungswesen)?

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 70 GG (Auffangkompetenz Laender) — Art. 71-73 GG (ausschliessliche Bundeskompetenz) — Art. 72-74 GG (konkurrierende Kompetenz, Erforderlichkeit) — Art. 72 Abs. 3 GG (Abweichungskompetenz) — Art. 80 GG (Verordnungsermaechtigung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Gutachten ein bis zwei Seiten mit:

1. Materie (in zwei Sätzen)
2. Norm im GG bzw. Landesverfassung
3. Prüfung Erforderlichkeitsklausel (falls einschlaegig)
4. Prüfung Sperrwirkung (falls Land)
5. Empfehlung tragfähig / nicht tragfähig / mit Modifikation tragfähig

## Anschluss

Wenn tragfähig: weiter mit `normenkartierung`.
Wenn nicht tragfähig: zurueck zu `legistik-auftragsaufnahme` und Norm-Ebene wechseln.
