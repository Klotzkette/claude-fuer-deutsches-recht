# Deutsche juristische Zitierweise und Quellenprüfung (v4.1)

> Diese Datei ist die zentrale Referenz für alle Skills, Agenten und Cookbooks in diesem Repository. Sie ersetzt die frühere kommentar- und aufsatzfreundliche Fassung.
>
> **Leitlinie:** Keine Blindzitate. Das Repository soll anwaltliche Arbeit unterstützen, nicht Fundstellen erfinden. Rechtsprechung darf zitiert werden, wenn sie mit Gericht, Entscheidungsform, Datum, Aktenzeichen und einer prüfbaren Quelle abgesichert ist. Literatur wird nur verwendet, wenn sie vom Nutzer bereitgestellt wurde oder über einen lizenzierten Live-Zugriff wirklich vorliegt.

## 1. Harte Sperren

Diese Regeln sind verbindlich:

1. **Kein BeckRS aus dem Modell heraus.** `BeckRS 2024, 12345` darf nur übernommen werden, wenn der Nutzer die Fundstelle selbst liefert oder ein lizenzierter Live-Zugriff sie verifiziert. Sonst weglassen.
2. **Keine Kommentar-Blindzitate.** Keine Rn. aus Grüneberg, MüKo, BeckOK, Staudinger, Erman, ErfK, Schaub, HWK, Maunz/Dürig, BeckOGK usw. erfinden.
3. **Keine Aufsatz-Blindzitate.** Keine NJW-, NZA-, ZIP-, GRUR-, MMR-, ZD-, DStR- oder sonstigen Aufsatzfundstellen behaupten, wenn der konkrete Beitrag nicht vorliegt.
4. **Kein aktueller Palandt/Pahlen.** Der frühere Palandt heißt seit der 81. Auflage 2022 Grüneberg. Historische Palandt-Zitate nur verwenden, wenn genau diese Altauflage vom Nutzer bereitgestellt wurde. `Pahlen` ist kein Ersatz. In neu erzeugten Arbeitsergebnissen wird nicht mehr auf `Palandt` umgestellt, nur weil Alttexte das so vormachen.
5. **Keine Rechtsprechung ohne Mindestdaten.** Gericht, Entscheidungsform, Datum und Aktenzeichen sind Pflicht. Fehlt eines davon, nicht als gesichertes Zitat ausgeben.
6. **Keine Datenbanknummer als Ersatz für Prüfung.** BeckRS, juris, openJur, dejure oder sonstige Datenbankhinweise ersetzen nicht Datum und Aktenzeichen.
7. **Keine erfundenen Parallelfundstellen.** NJW, NZA, ZIP, GRUR usw. nur als Parallelfundstelle nennen, wenn sie sicher bekannt oder verifiziert ist.

## 2. Rechtsprechung: Mindeststandard

**Schema:**

`<Gericht>, <Entscheidungsform> v. <Datum> - Az. <Aktenzeichen>, <Fundstelle oder freie Quelle> Rn. <Randnummer>.`

`Az.` steht direkt vor dem Aktenzeichen. Wenn eine zitierfähige Randnummer vorhanden ist, wird auf `Rn.` verwiesen. Wenn nur Seiten verfügbar sind, nur dann Seiten verwenden.

**Vor Ausgabe prüfen:**

- Gericht und Spruchkörper plausibel?
- Entscheidungsform vorhanden: Urt., Beschl., Vorlagebeschl., Hinweisbeschl.?
- Datum im Format `TT.MM.JJJJ`?
- Aktenzeichen vollständig und typgerecht?
- Freie oder amtliche Quelle vorhanden?
- Randnummer/Seite aus der Quelle übernommen, nicht geraten?
- Thema der Entscheidung passt zur Aussage?

## 3. Kostenlose und amtliche Quellen

Bevorzugt werden frei zugängliche Primärquellen:

- Bundesverfassungsgericht: `bundesverfassungsgericht.de`
- Bundesgerichtshof: `bundesgerichtshof.de`
- Bundesarbeitsgericht: `bundesarbeitsgericht.de`
- Bundesverwaltungsgericht: `bverwg.de`
- Bundesfinanzhof: `bfh.bund.de`
- Bundessozialgericht: `bsg.bund.de`
- Gerichtshof der Europäischen Union: `curia.europa.eu`
- Europäischer Gerichtshof für Menschenrechte: `hudoc.echr.coe.int`
- Sozialgerichtsbarkeit der Länder: `sozialgerichtsbarkeit.de`
- Landesrechtsprechungsdatenbanken, soweit amtlich oder gerichtsnah

Frei zugängliche Sekundärdatenbanken wie openJur oder dejure können als Such- und Auffindehilfe dienen. Sie sind nützlich, aber nicht dasselbe wie eine amtliche Primärquelle. Wenn keine amtliche Quelle verfügbar ist, deutlich machen, worauf die Verifikation beruht.

## 4. Umgang mit BeckRS, juris und Datenbankzitaten

`BeckRS` und `juris` sind keine frei verifizierbaren Universalquellen. Sie dürfen nicht aus Sprachmodellwissen generiert werden.

**Wenn eine bestehende Fundstelle im Altbestand auftaucht:**

1. Gericht, Datum und Aktenzeichen herausziehen.
2. Freie Originalquelle suchen.
3. Wenn gefunden: BeckRS entfernen oder nur als vom Nutzer gelieferte Parallelfundstelle kennzeichnen.
4. Wenn nicht gefunden: Zitat als `nicht frei verifiziert` markieren oder ganz entfernen.

**Formulierung bei fehlender Verifikation:**

`Diese Entscheidung ist im verfügbaren Material nicht frei verifiziert. Vor Verwendung in Schriftsatz, Gutachten oder Mandantenmemo bitte Originalquelle anhand von Gericht, Datum und Aktenzeichen prüfen.`

## 5. Literatur nur mit echter Quelle

Kommentare, Handbücher, Monographien und Aufsätze bleiben in der deutschen Praxis wichtig. Dieses Repository darf sie aber nicht blind zitieren.

**Zulässig ist Literatur nur, wenn:**

- der Nutzer den Auszug, Scan, Link oder Datenbankexport bereitstellt,
- ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt besteht,
- oder es nur um einen neutralen Recherchehinweis ohne Fundstellenbehauptung geht.

**Unzulässig ist:**

- aus dem Modell eine Randnummer zu Grüneberg, MüKo, BeckOK, Staudinger usw. zu erzeugen,
- eine Auflage oder Edition zu behaupten, ohne sie geprüft zu haben,
- einen Aufsatz mit Jahrgang/Seite zu zitieren, wenn der Beitrag nicht vorliegt.
- ein Rechercheergebnis so zu formulieren, als sei ein Kommentar- oder Aufsatzzitat bereits geprüft, obwohl nur eine Erinnerungs- oder Modellwissensspur besteht.

**Zulässiger Recherchehinweis:**

`Literatur nur prüfen, wenn Zugriff besteht: aktueller BGB-Kommentar zu § 126 BGB; arbeitsrechtlicher Kommentar zu § 109 GewO. Keine Fundstelle ohne Verifikation ausgeben.`

## 6. Gesetze, Materialien und Behördenquellen

Gesetze und amtliche Materialien sind bevorzugte Quellen.

- Normen: `§ 433 Abs. 1 Satz 1 BGB`; `Art. 6 Abs. 1 lit. f DSGVO`.
- Mehrere Normen: `§§ 280 Abs. 1, 281 Abs. 1 und Abs. 2 BGB`.
- Gesetzgebungsmaterialien: Herausgeber, Drucksachennummer, Datum oder Wahlperiode, Pinpoint und Link.
- Behördenmaterialien: Behörde, Titel, Stand/Datum, Abschnitt/Randnummer und Link.

Amtliche Startpunkte:

- Bundesrecht: `gesetze-im-internet.de`
- Bundestagsdrucksachen: `dserver.bundestag.de`
- EU-Recht: `eur-lex.europa.eu`
- Behörden: jeweilige amtliche Domain, etwa `bafin.de`, `bsi.bund.de`, `bfdi.bund.de`, `bundesnetzagentur.de`.

## 7. Reihenfolge mehrerer Rechtsprechungsbelege

Bei mehreren Entscheidungen zuerst nach Gerichtsebene sortieren, danach nach Relevanz oder chronologisch absteigend. Die gewählte Ordnung muss im Dokument konsistent sein.

Gerichtsebene:

1. BVerfG
2. EuGH und EGMR, soweit unions- oder konventionsrechtlich tragend
3. BGH, BAG, BSG, BFH, BVerwG
4. OLG, LAG, LSG, FG, OVG, VGH
5. LG, ArbG, SG, VG
6. AG

## 8. Ausgabeformate

**Sicher verifiziertes Zitat:**

`BGH, Urt. v. TT.MM.JJJJ - Az. ... , [amtliche/freie Quelle] Rn. ... .`

**Noch nicht frei verifiziert:**

`[Rechtsprechung prüfen: Gericht, Entscheidung v. TT.MM.JJJJ - Az. ...; freie Quelle noch nicht gefunden.]`

**Literatur nur als Nutzerquelle:**

`[Nutzerquelle: Auszug aus ..., vom Nutzer bereitgestellt, dort Rn. ...]`

**BeckRS im Alttext:**

`[BeckRS-Fundstelle entfernt: vor Verwendung freie Quelle zu Gericht, Datum und Aktenzeichen prüfen.]`

## 9. Checkliste vor jeder juristischen Ausgabe

- [ ] Keine BeckRS-Nummer generiert?
- [ ] Keine Kommentar- oder Aufsatzfundstelle ohne Nutzerquelle oder lizenzierten Live-Zugriff?
- [ ] Keine Palandt-/Pahlen-Aktualzitate?
- [ ] Rechtsprechung mit Gericht, Entscheidungsform, Datum und Aktenzeichen?
- [ ] Freie/amtliche Quelle oder klarer Prüfvermerk?
- [ ] Randnummer/Seite nur aus Quelle übernommen?
- [ ] Thema der Entscheidung passt zur rechtlichen Aussage?
- [ ] Gesetzesstand und Übergangsvorschriften geprüft?
- [ ] Offene Unsicherheit ausdrücklich markiert?

## 10. Skill-Hardening gegen Scheinpräzision

Jeder Skill, der juristische Aussagen ausgibt, trennt drei Ebenen:

1. **Gesichert:** Normtext, Nutzerdokument, amtliche/freie Quelle oder dokumentierter Livezugriff.
2. **Plausibel, aber zu prüfen:** bekannte Linie oder Arbeitshypothese ohne gerade geöffneten Volltext.
3. **Nicht verwenden:** Datenbanknummer, Kommentar-Randnummer, Aufsatzfundstelle oder Parallelfundstelle aus bloßem Modellwissen.

Wenn eine Entscheidung, Fundstelle oder Behördenpraxis nicht gerade geprüft wurde, ist die Ausgabe als Prüfpunkt zu formulieren. Das ist kein Makel, sondern saubere anwaltliche Arbeitsweise.

## 11. Kurzregel für Skills

Wenn ein Skill juristische Quellen ausgibt, gilt:

`Norm zuerst. Dann verifizierte Rechtsprechung. Literatur nur bei bereitgestellter oder live verifizierter Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate.`
