---
name: verl-tantieme-abrechnung-themenscout
description: "Verl Tantieme Abrechnung Themenscout: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verl Tantieme Abrechnung Themenscout

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Verl Tantieme Abrechnung Themenscout** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verl-tantieme-abrechnung-jaehrlich` | Jaehrliche Tantieme-Abrechnung fuer Autoren juristischer Werke: Stueck- und Umsatzbeteiligung, Loseblatt-Ergaenzungslieferungen, Online-Nutzung, Verrechnung mit Vorschuss, Pflichten nach UrhG § 32d. |
| `verl-themenscout-rechtsentwicklung` | Identifiziert Trends in BGH-/EuGH-/BVerfG-/BMF-Rechtsprechung und Gesetzgebungsverfahren als Themenkandidaten fuer Aufsaetze und Heftaufmacher. |
| `verl-trend-radar-rechtsgebiete` | Beobachtet rechtsgebietsuebergreifende Trends (Digitalisierung, ESG, KI-Recht, EU-Reformen) als Themen-Frueherkennung fuer mehrere Zeitschriften und Reihen. |
| `verl-vergleichsverhandlung-mit-autor` | Vergleichsverhandlung mit Autor: Aufbau einer Verhandlungslinie bei Honorar-, Tantieme- oder Rueckforderungsstreit, BATNA, Eskalationsstufen, schriftlicher Vergleich und Abgeltungsklausel. |
| `verl-vlb-katalog-pflege-jur` | VLB-Katalog (Verzeichnis lieferbarer Buecher) pflegen: ONIX-Metadaten, Schlagworte, Klappentext, Reihen, Preisbindung, Erscheinungstermin-Pflege. Konsistenz mit Webshop, beck-online und Buchhandel. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Verl Tantieme Abrechnung Themenscout**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verl-tantieme-abrechnung-jaehrlich`

**Fokus:** Jaehrliche Tantieme-Abrechnung fuer Autoren juristischer Werke: Stueck- und Umsatzbeteiligung, Loseblatt-Ergaenzungslieferungen, Online-Nutzung, Verrechnung mit Vorschuss, Pflichten nach UrhG § 32d.

# Tantieme jaehrlich abrechnen

## Worum geht es konkret

Autorinnen und Autoren juristischer Werke erhalten typischerweise eine Beteiligung an Verkauf oder Nutzung (Tantieme). Die Abrechnung wird einmal jaehrlich ausgekehrt, bei Loseblatt und Online ggf. quartalsweise. UrhG § 32d schafft eine spezialgesetzliche Auskunftspflicht. Der Skill fuehrt durch die Abrechnungslogik, die UStG-Behandlung und die Eskalation, wenn der Autor die Abrechnung beanstandet.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Vertragsart: Lehrbuch, Kommentar, Loseblatt, Festschrift, Online-Kommentar?
2. Honorarmodell: pro verkauftem Stueck, prozentual vom Nettoladenpreis, prozentual vom Nettoumsatz, Mischmodell?
3. Vorschuss gezahlt? Wie hoch, wann?
4. Abrechnungszeitraum: Kalenderjahr oder Verlagsgeschaeftsjahr?
5. Mehrere Autorinnen mit Verteilungsschluessel?
6. Welche Auswertungsdaten liegen vor (Verkaufsstatistik, Abosystem, Klickdaten)?
7. Frist: vertraglich vereinbarte Abrechnungsfrist?

## Rechtlicher und sachlicher Rahmen

- UrhG § 32 - angemessene Verguetung; Pflicht zur Anpassung bei Unangemessenheit.
- UrhG § 32a - sogenannte "Bestsellerklausel"; Anpassungsanspruch bei auffaelligem Missverhaeltnis.
- UrhG § 32d - jaehrliche Auskunftspflicht des Verlags ueber Umfang der Nutzung und erzielte Ertraege.
- UrhG § 32e - Auskunft auch von Lizenznehmer in der Lizenzkette.
- VerlG §§ 25, 26 - Abrechnung und Rechenschaftslegung im Verlagsverhaeltnis.
- BGB § 259 - Pflicht zur ordnungsgemaessen Rechenschaftslegung mit geordneter Aufstellung.
- BGB § 273 - Zurueckbehaltungsrecht des Autors bei unvollstaendiger Abrechnung.

## Praxisleitfaden / Schritt fuer Schritt

1. **Stichtag setzen.** Standard 31.12., Abrechnung bis 30.06. des Folgejahres (vertraglich pruefen).
2. **Datenbasis ziehen.** Verkaufszahlen, Retouren, Mengenrabatte, Frei- und Belegexemplare, Online-Nutzung (Klicks, Aufrufe nach Vertragsdefinition).
3. **Nettoladenpreis / Nettoumsatz korrekt rechnen.** Buchpreisbindung beachten; Rabatte und Buchhaendlerkonditionen anhand der Verlagskalkulation.
4. **Vorschuss verrechnen.** Tantieme wird gegen offenen Vorschuss verrechnet, danach Auszahlung.
5. **Verteilung mehrerer Autoren.** Nach vereinbartem Schluessel (Seitenanteil, Kapitelzuordnung, gleichmaessig).
6. **Steuerliche Behandlung.** Honorar = Verguetung fuer Rechteeinraeumung; 7 Prozent UStG-Satz (§ 12 Abs. 2 Nr. 7 lit. c UStG). KSK-Meldung nicht vergessen.
7. **Abrechnungsdokument erstellen.** Tabelle pro Werk, kumulierter Stand, Auszahlungsbetrag.
8. **Auskunftsschreiben gemaess UrhG § 32d.** Bei Verlangen auch Detailaufstellung Lizenzeinnahmen.
9. **Versand und Frist zur Beanstandung.** Standard 30 Tage; sonst gilt Abrechnung als anerkannt (nur bei vertraglicher Klausel).

## Trade-off-Matrix

| Aspekt | Detaillierte Abrechnung | Verdichtete Abrechnung |
|---|---|---|
| Vertrauen | Hoch | Niedrig |
| Aufwand Verlag | Hoch | Niedrig |
| Risiko Streit | Niedrig | Hoeher |
| Risiko § 32a-Anpassungsanspruch | Erkennbar fruehzeitig | Verspaetet |

## Praxistipps der alten Redaktion

- Erlaeuternder Begleittext beugt Rueckfragen vor; pro Werk eine Zeile zum Vertrieb (z. B. "Auflage 8 ausverkauft Q3, Auflage 9 ausgeliefert Q4").
- Frei- und Werbeexemplare separat ausweisen, sonst Argwohn.
- Bei E-Book/Datenbank: Nutzungseinheiten (Aufrufe, Volltextabrufe) vertraglich definieren; sonst Streit ueber Bezugsgroesse.
- Bei Loseblatt: Abonnementbestand zum Stichtag, nicht reine Verkaufszahl.
- Reklamationen aus den letzten 3 Jahren in CRM dokumentieren; Muster erkennbar.
- Bei hohem Anstieg eines Werks proaktiv Auskunft anbieten - sonst kommt der Anwalt mit § 32a.

## Mustertexte / Vorlagen

**Anschreiben zur Jahresabrechnung**

```
Betreff: Tantieme-Abrechnung [Jahr] - [Werktitel]

Sehr geehrte Frau/Herr [Autorenname],

anliegend uebersenden wir Ihnen die Jahresabrechnung Ihrer Tantiemen
fuer den Zeitraum [Datum] bis [Datum].

Auf einen Blick:
- Werk: [Titel], [Auflage]
- Verkaufte Einheiten Print: [n] (davon Retouren: [n])
- Nutzungsereignisse Online: [n] (Volltextabrufe gemaess Vertrag § [n])
- Brutto-Tantieme: EUR [Betrag]
- Vorschuss-Verrechnung: EUR [Betrag]
- Auszahlung an Sie: EUR [Betrag]

Die Detailaufstellung finden Sie in Anlage 1. Auf Wunsch stellen wir
Ihnen die Daten gemaess UrhG § 32d in vertiefter Form bereit; bitte
melden Sie sich unter [Kontakt].

Die Auszahlung erfolgt bis zum [Datum] auf das uns hinterlegte Konto.

Mit freundlichen Gruessen
[Name, Funktion]
```

**Tabelle Detail-Abrechnung (Beispiel)**

```
Werk: [Titel] - Auflage [n] - Erscheinungstermin [Datum]
Tantiemesatz: [Prozent vom Nettoladenpreis]
Stueckzahl verkauft: [n]
Stueckzahl retourniert: [n]
Netto-Verkaufseinheiten: [n]
Nettoladenpreis: EUR [Betrag]
Bruttohonorar: EUR [Betrag]
USt 7 %: EUR [Betrag]
Bruttosumme: EUR [Betrag]
Verrechnung Vorschuss: EUR [Betrag]
Auszahlung: EUR [Betrag]
```

**Antwort auf Auskunftsverlangen nach UrhG § 32d**

```
Sehr geehrte Frau/Herr [Anwaltsname],

auf Ihr Auskunftsverlangen nach UrhG § 32d uebersenden wir Ihnen fuer
das Werk [Titel] folgende Aufstellung fuer den Zeitraum [...]:

[Tabelle mit Vertriebszahlen, Lizenzeinnahmen, Sublizenzen]

Weitergehende Ansprueche (UrhG § 32a) sehen wir auf Basis der
nachgewiesenen Vergleichsverguetungen [...] nicht als gerechtfertigt an.

Mit freundlichen Gruessen
[Name]
```

## Typische Fehler / Pitfalls

- Retouren nicht ausgewiesen - Differenz zur Marktstatistik faellt auf.
- Verteilung bei Co-Autoren nicht dokumentiert - jaehrlicher Streit.
- Frei- und Pflichtexemplare in Verkaufszahlen versteckt.
- Tantieme verrechnet, aber keine Klarheit ueber Vorschussstand - Vertrauensbruch.
- UrhG § 32d-Pflicht ignoriert - kann zu Auskunftsklage fuehren.
- KSK-Meldung der Tantieme vergessen.

## Querverweise

- `workflow-kaltstart-und-routing` - Einstieg bei Reklamationen.
- `honorar-vertrag-royalties-triage` - Triage zur Vertragslage.
- `verl-honorarrechnung-erstellen-pruefen` - rechnungsformale Behandlung.
- `verl-vorschuss-pruefung-buecher` - Vorschussverrechnung.
- `verl-vergleichsverhandlung-mit-autor` - bei Streit ueber Anpassungsanspruch.

## Quellen Stand 06/2026

- UrhG §§ 32, 32a, 32d, 32e - Verguetung und Auskunftspflichten.
- VerlG §§ 25, 26 - Rechenschaft und Abrechnung.
- BGB §§ 259, 273 - Rechenschaftslegung, Zurueckbehaltungsrecht.
- UStG § 12 Abs. 2 Nr. 7 lit. c - ermaessigter Steuersatz fuer Rechteeinraeumung.
- KSVG - Abgabepflicht; aktueller Satz unter kuenstlersozialkasse.de.
- BGH-Rechtsprechung zu § 32a UrhG (Volltexte zur amtlichen Pruefung unter bundesgerichtshof.de und dejure.org).

## 2. `verl-themenscout-rechtsentwicklung`

**Fokus:** Identifiziert Trends in BGH-/EuGH-/BVerfG-/BMF-Rechtsprechung und Gesetzgebungsverfahren als Themenkandidaten fuer Aufsaetze und Heftaufmacher.

# Themenscout Rechtsentwicklung

## Worum geht es konkret

Eine Fachzeitschrift lebt davon, fruehzeitig die Themen zu sehen, ueber die in 4-12 Wochen alle reden werden. Der Themenscout-Skill systematisiert diese Frueherkennung: Welche BGH-Vorlagebeschluesse koennen Sprengkraft entwickeln? Welche EuGH-Schlussantraege deuten auf Rechtsprechungsaenderungen? Welches BMF-Schreiben aendert die Beraterpraxis?

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn fuer die periodische Themenfindung (woechentlich / monatlich) oder bei punktueller Frage "was sollte ins Heft 09/2026?". Klaeren Sie:

1. Welches Rechtsgebiet / welche Zeitschriften (NJW Allgemein, NZA Arbeitsrecht, ZIP Insolvenz, BB Wirtschaft)?
2. Welcher Zeithorizont (4 Wochen Aufmacher, 12 Wochen Quartalsplanung)?
3. Welcher Lesertyp (Anwalt, Richter, Steuerberater, Lehre)?
4. Vorhandene Watchlist mit Aktenzeichen?

## Material- bzw. Sachrahmen

- Watchlist anhaengige Verfahren (BGH-Vorlageaktenzeichen, EuGH-Verfahren).
- Newsticker BVerfG, BGH, EuGH, BSG, BAG, BFH, BVerwG.
- Veroeffentlichte Schlussantraege / Gutachten.
- Gesetzgebungsverfahren auf Bundes- und EU-Ebene.
- BMF-Schreiben, BAFin-Mitteilungen, BNetzA-Verfuegungen.

## Praxisleitfaden / Schritt fuer Schritt

1. **Quellenscan periodisch.** Frei zugaengliche Quellen: bundesgerichtshof.de Pressemitteilungen; bundesverfassungsgericht.de Entscheidungen und anhaengige Verfahren; curia.europa.eu fuer EuGH; bmf.de Schreiben; bundesregierung.de Gesetzentwuerfe.
2. **Klassifikation.** Pro Treffer: Aktenzeichen, Datum, Gegenstand in einem Satz, Bedeutung (1-5), Eilbeduerftigkeit (1-5), Verlagseignung (Aufsatz / Anmerkung / Editorial).
3. **Trendlinien aufspueren.** Mehrere Entscheidungen zum gleichen Themenkreis innerhalb 6-12 Monaten? Hinweise auf Linienaenderung der Rspr.?
4. **Autoren-Matching.** Wer ist dafuer prädestiniert? Profilseite Autorin, vorherige Aufsaetze.
5. **Themenbrief.** Konzentrat fuer die Redaktionssitzung: Thema, Anlass, mögliche Autorin, Format, Heft.
6. **Triage-Entscheidung in der Sitzung** (siehe `verl-redaktionssitzung-vorbereiten`).

## Trade-off-Matrix

| Pfad | A: Aktuelle Hot-Topics (Vorlageverfahren BGH) | B: Strukturierter Trend (Reformprozess) | Empfehlung |
|------|-----------------------------------------------|----------------------------------------|------------|
| Reichweite | hoch kurzfristig | hoch langfristig | beides parallel |
| Auflagensog | hoch | mittel | A bei Newsletter, B bei Jahresheft |
| Risiko | Aktualitaet vergeht schnell | Reform versandet | beides |

## Praxistipps der alten Redaktion

- "Schauen Sie nicht nur auf das Urteil, sondern auf die Schlussantraege - sechs Monate Vorlauf."
- BFH-Themen brauchen oft BMF-Schreiben als Anlass.
- Bei Rspr.-Linien achten Sie auf Wendepunkte (anderer Senat, anderer Berichterstatter, EuGH-Vorlage).
- Konkurrenzbeobachtung: NJW hat Thema X? Dann nicht doppelt, sondern Anmerkung oder Gegenposition.

## Mustertexte / Vorlagen

**Themenbrief-Vorlage:**

```
Themenbrief Nr. 23/2026 - Themenscout NJW
Stand: 02.06.2026

Thema 1: BGH zur AGB-Kontrolle bei Plattformvertraegen
Anlass: Vorlagebeschluss vom 15.05.2026, Az. [Az. - im Tagebuch der Schriftleitung]
Bedeutung: 5 / Eilbeduerftigkeit: 4
Vorschlag: Aufmacher Heft 14/2026
Autorin: [Name], Verfuegbarkeit angefragt
Format: Aufsatz, ~28 kZ

Thema 2: ...
```

**Watchlist-Eintrag:**

```
Az.: [Az.]
Gericht: BGH II. Zivilsenat
Gegenstand: AGB-Kontrolle Plattformvertraege
Verfahrensstand: Vorlage von OLG Karlsruhe vom 12.04.2026
Veroeffentlichungs-Erwartung: Q4/2026
Verlagsaktion: bei Verkuendung: Aufmacher + Pressemeldung
Quellen-URL: https://www.bundesgerichtshof.de/...
```

## Typische Fehler / Pitfalls

- BGH-Vorlagebeschluesse uebersehen, weil sie nicht in der Hauptpressemitteilung sind.
- EuGH-Schlussantraege als "noch nicht relevant" abgetan - 70 % werden uebernommen.
- Gesetzgebungsverfahren in Ausschussberatung uebersehen.
- Trendlinien aus drei Entscheidungen falsch hochgerechnet, ohne Senatsbesetzung zu pruefen.
- Eigene Watchlist nicht aktualisiert - alter Stand wirkt blamabel.

## Querverweise

- `verl-trend-radar-rechtsgebiete` - rechtsgebietsuebergreifender Trend.
- `verl-redaktionssitzung-vorbereiten` - Themen bringen in die Sitzung.
- `verl-redaktionsmemo-jahresplanung` - fuer Jahresplanung.
- `verl-ideenpool-und-priorisierung` - Backlog-Verwaltung.
- `entscheidungsmonitor-rechtsstand` - laufender Monitor (bestehender Skill).

## Quellen Stand 06/2026

- BGH, [https://www.bundesgerichtshof.de](https://www.bundesgerichtshof.de) (Pressemitteilungen, anhaengige Verfahren).
- BVerfG, [https://www.bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) (Entscheidungen, Vorschau).
- EuGH / Curia, [https://curia.europa.eu](https://curia.europa.eu) (Verfahrensregister, Schlussantraege).
- dejure.org, [https://dejure.org](https://dejure.org) (Recherche).
- BMF-Schreiben, [https://www.bundesfinanzministerium.de](https://www.bundesfinanzministerium.de).
- Bundesgesetzblatt online, [https://www.recht.bund.de/bgbl/](https://www.recht.bund.de/bgbl/).
- Bundesrat / Bundestag Drucksachen, [https://dip.bundestag.de](https://dip.bundestag.de).
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016.

## 3. `verl-trend-radar-rechtsgebiete`

**Fokus:** Beobachtet rechtsgebietsuebergreifende Trends (Digitalisierung, ESG, KI-Recht, EU-Reformen) als Themen-Frueherkennung fuer mehrere Zeitschriften und Reihen.

# Trend-Radar Rechtsgebiete

## Worum geht es konkret

Anders als der Themenscout (der einzelne Entscheidungen scannt) sucht der Trend-Radar nach uebergeordneten Bewegungen: KI-Regulierung quer durch Zivilrecht, Strafrecht, Arbeitsrecht; ESG-Pflichten quer durch Gesellschaftsrecht, Steuerrecht, Umweltrecht; EU-Reformen, die Folgewellen in nationalen Rechtsgebieten ausloesen. Dieser Skill systematisiert die Querschnittsbeobachtung fuer Verlagsprogramme.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn fuer Programm- und Produktstrategie: neue Reihen, neue Zeitschriften, neue Loseblattwerke, neue Online-Kommentare. Klaeren Sie:

1. Welcher Beobachtungszeitraum (rolling 24 Monate Standard)?
2. Welche Rechtsgebiete im Scope (selektiv oder Vollscan)?
3. Auf welche Verlagsprodukte sollen die Erkenntnisse einzahlen (Zeitschriften, Buchreihen, Online)?
4. Eskalationsschwelle (ab wann wird ein Trend zum Programmthema)?

## Material- bzw. Sachrahmen

- Newsticker BGH, BVerfG, EuGH, EuG, EGMR.
- Gesetzgebungstrends national und EU (Dossier-Ebene).
- Wissenschaftliche Diskussion (Vortragsthemen Tagungen, Habilitationsthemen, Sammelbaende).
- Beraterperspektive (was fragen Mandanten in welcher Branche?).
- Wirtschafts-/Sozialdaten (Insolvenzstatistik, Klagezahlen).

## Praxisleitfaden / Schritt fuer Schritt

1. **Topic-Cluster definieren.** 6-10 Querschnittsthemen (z. B. "KI-Regulierung", "ESG", "Plattformrecht", "Energierecht 3.0").
2. **Quellenfaecher pro Cluster.** Pro Cluster: 4-6 zentrale Quellen, freie Tickerlinks, Verbandsstimmen.
3. **Quartalsweise Sichtung.** Pro Cluster ein einseitiger Quartalsbericht: was war, wohin laeuft es, naechste Wegmarken.
4. **Querverbindungen.** Welche zwei Cluster kreuzen sich (z. B. KI im Steuerrecht)? Querhinweise im Memo.
5. **Programm-Konsequenzen.** Pro Cluster: welche Verlagsprodukte koennen reagieren (neuer Aufsatz, neue Online-Kommentar-Ressource, neue Reihe)?
6. **Briefing fuer Verlagsleitung** mit klarer Empfehlung "weiterbeobachten" / "Aufbau eigener Reihe" / "in bestehende Reihe integrieren".

## Trade-off-Matrix

| Pfad | A: 10 Cluster mit jeweils flachem Scan | B: 4 Cluster mit tieferem Scan | Empfehlung |
|------|--------------------------------------|--------------------------------|------------|
| Reichweite | breit | schmal | A bei breiter Verlagsprogrammgrundlage |
| Tiefe | gering | hoch | B bei strategischer Produktentscheidung |
| Personalbedarf | mittel | hoch | abhaengig von Verlagsgroesse |

## Praxistipps der alten Redaktion

- "Ein Trend ist erst dann ein Trend, wenn drei unabhaengige Anzeichen ihn stuetzen - eine Konferenz reicht nicht."
- Querschnittsthemen verlangen Querschnittsautorinnen - die sind selten; lieber Co-Autorenschaften zwischen Rechtsgebieten.
- Eigener Beraterkreis (Anwaltschaft, Justiz) als Fruehwarnsystem - kurzes Quartalsgespraech.
- EU-Reformen brauchen oft 18-36 Monate, bis nationales Recht reagiert - Trend ist also langlebig, lohnt sich.

## Mustertexte / Vorlagen

**Cluster-Briefing-Vorlage:**

```
Cluster: KI-Regulierung
Beobachtungszeitraum: Q2/2026
Hauptbewegungen:
- AI Act: Vollanwendung ab 02.08.2026 (Art. 113 AI Act)
- Sektor-Specifica: BAFin-Konsultation Q1/2026
- Rspr.: BAG zu KI-gestuetzter Bewerberauswahl (anhaengig)
Querverbindungen: Datenschutz (Cluster 3), Arbeitsrecht (Cluster 5)
Programm-Empfehlung:
- Zeitschrift NZA: 2 Aufsaetze, 1 Anmerkung
- Online-Kommentar: neue Lemmata AI Act
- Buchreihe: Kandidat fuer Loseblattwerk "AI Act Praxiskommentar"
```

**Trendindikator-Tabelle:**

| Indikator | Schwellwert | Aktueller Stand | Trendrichtung |
|-----------|-------------|------------------|---------------|
| Konferenzthemen p.a. | 5+ | 12 | steigend |
| Habilitationen | 2+ | 4 angekuendigt | steigend |
| BGH-Vorlagen | 1+ | 0 (eine BVerwG-Vorlage anhaengig) | beobachten |
| Verbandsstimmen | 3+ | 5 | steigend |

## Typische Fehler / Pitfalls

- Trend nur in einer Quelle gesehen - falsche Hochrechnung.
- Querverbindungen uebersehen - Trend "KI" ohne Datenschutz und Arbeitsrecht ist halb.
- Programm-Konsequenz nicht formuliert - Trend-Radar wird zur Beobachtungsspielwiese.
- EU-Reformen unterschaetzt - oft langlebige Trends mit Folgewellen.
- Beraterperspektive ausgeklammert - das raecht sich am Markt.

## Querverweise

- `verl-themenscout-rechtsentwicklung` - einzelne Entscheidungen.
- `verl-redaktionsmemo-jahresplanung` - Jahresarchitektur.
- `verl-ideenpool-und-priorisierung` - Trends in Backlog uebertragen.
- `verl-loseblattwerk-spezial` - bei Reihenbildung.
- `verl-online-kommentar-update-spezial` - bei Online-Kommentar-Anpassung.

## Quellen Stand 06/2026

- BGH, [https://www.bundesgerichtshof.de](https://www.bundesgerichtshof.de).
- BVerfG, [https://www.bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de).
- EuGH / Curia, [https://curia.europa.eu](https://curia.europa.eu).
- EUR-Lex, [https://eur-lex.europa.eu](https://eur-lex.europa.eu).
- Bundesregierung Vorhabenplaner, [https://www.bundesregierung.de](https://www.bundesregierung.de).
- AI Act, VO (EU) 2024/1689, [https://eur-lex.europa.eu/eli/reg/2024/1689/oj](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016.

## 4. `verl-vergleichsverhandlung-mit-autor`

**Fokus:** Vergleichsverhandlung mit Autor: Aufbau einer Verhandlungslinie bei Honorar-, Tantieme- oder Rueckforderungsstreit, BATNA, Eskalationsstufen, schriftlicher Vergleich und Abgeltungsklausel.

# Vergleichsverhandlung mit Autor

## Worum geht es konkret

Ein Honorarstreit, eine Vorschuss-Rueckforderung, ein Anpassungsverlangen nach UrhG § 32a oder ein Manuskript-Verzug eskaliert. Bevor man zum Anwalt geht, lohnt der schriftlich oder muendlich gefuehrte Vergleich. Der Skill liefert Verhandlungslinie, Argumentationsraster, Mustertext fuer einen schriftlichen Vergleich mit Abgeltungsklausel und Hinweise auf typische Fallstricke.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Was ist der Streitgegenstand (Summe X, Manuskriptrueckgabe, Nutzungsrechte zurueck, Tantiemenanpassung)?
2. Wer ist Verhandlungsfuehrer auf jeder Seite (Autor, Anwalt, Verlagsleitung, Justiziariat)?
3. Liegt eine Klage vor oder steht eine Klage bevor?
4. Gibt es eine Verjaehrungsfrist im Hintergrund?
5. Welches BATNA (Best Alternative To a Negotiated Agreement) hat jede Seite?
6. Gibt es Vertraulichkeitsbedarf (Marktwirkung, andere Autoren)?
7. Wieviel Zeitfenster fuer den Vergleich (vor Gerichtstermin)?

## Rechtlicher und sachlicher Rahmen

- BGB § 779 - Vergleich; nur wirksam, wenn beide Parteien wechselseitig nachgeben.
- ZPO §§ 278, 794 Abs. 1 Nr. 1 - gerichtlicher Vergleich, Vollstreckungstitel; ausserhalb der Streitsache als reine Privatvereinbarung.
- UrhG § 32, 32a - Verguetung und Anpassungsanspruch; nicht durch Vergleich vollstaendig abdingbar.
- UrhG § 79b - bei Ueberlassung von Nutzungsrechten; pauschale Abgeltung mit Einschraenkungen.
- BGB §§ 145 ff. - Angebot und Annahme; Schweigen ist grundsaetzlich keine Annahme.
- BGB §§ 305 ff. - AGB-Kontrolle bei vorformulierten Vergleichsklauseln gegenueber Verbraucher-Autoren.
- DSGVO Art. 6, 17 - bei Vergleich ueber Loeschung personenbezogener Daten.

## Praxisleitfaden / Schritt fuer Schritt

1. **Streitgegenstand sauber formulieren.** "Worueber streiten wir?" - getrennt von "Wer hat angefangen?"
2. **BATNA bilden.** Was passiert, wenn der Vergleich scheitert? (Klage mit Kosten X, Zeitverlust Y, Imagewirkung Z.)
3. **ZOPA (Zone of Possible Agreement) abstecken.** Max- und Minimalposition jeder Seite.
4. **Optionen entwickeln.** Geld plus Sachleistung (z. B. Werbeplatz, Anschlussauftrag, Belegexemplare); Stufenplan; Zahlungsplan; Tantiemenanpassung mit Stichtag.
5. **Verhandlung fuehren.** Erst Sachverhalt, dann Interesse, dann Position; nicht umgekehrt.
6. **Schriftlich fixieren.** Vergleichstext mit Praeambel, Leistungspflichten, Abgeltungsklausel, Vertraulichkeitsklausel, Gerichtsstand.
7. **Erfuellung kontrollieren.** Wiedervorlage in CRM/Akte; Quittungen fuer Zahlungen, Manuskriptueberreichung in Empfang nehmen.

## Trade-off-Matrix

| Aspekt | Frueher Vergleich | Spaeter Vergleich |
|---|---|---|
| Kosten | Niedrig | Hoeher (Anwalts-/Gerichtskosten) |
| Image | Diskret | Oeffentlich |
| Beweislage | Offen | Verfestigt |
| Verhandlungsmacht | Symmetrisch | Asymmetrisch (wer im Recht ist) |
| Loesungsraum | Breit (auch Sachleistung) | Eng (Geld, Kosten) |

## Praxistipps der alten Redaktion

- Vergleich nie "in der Hitze" abschliessen - mindestens 24 Stunden Bedenkzeit.
- Sachleistung kann mehr wert sein als Geld (Buchanzeige, Festschriftsbeitrag, Nachfolgekommentar).
- Bei Anwaltsbeteiligung des Autors: Auch eigene Vertretung pruefen, sonst Schieflage.
- Vergleichstext immer beidseitig unterschreiben lassen, nicht "stillschweigend gelebt".
- Vertraulichkeit nur ausdruecklich; sonst kann der Autor die Konditionen weitererzaehlen.
- "Sachen verhandeln, Personen schonen." Beziehung erhalten lohnt sich oft fuer Folgewerke.

## Mustertexte / Vorlagen

**Anschreiben Vergleichsangebot**

```
Betreff: Vergleichsangebot in Sachen [Werk/Vorgang]

Sehr geehrte Frau/Herr [Autorenname],

wir bedauern, dass die Sachfrage [Streitgegenstand] zwischen uns
ungeloest ist. Bevor beide Seiten weitere Schritte einleiten, schlagen
wir folgenden Vergleich vor:

1. Der Verlag zahlt an Sie EUR [Betrag] bis [Datum].
2. Sie ueberreichen das ueberarbeitete Manuskript bis [Datum] / oder:
 Sie verzichten auf weitere Tantiemenforderungen aus dem Werk [Titel]
 bis [Datum].
3. Mit Erfuellung sind saemtliche wechselseitigen Ansprueche aus dem
 Vertrag vom [Datum] erledigt (Abgeltungsklausel).
4. Die Konditionen dieses Vergleichs werden vertraulich behandelt.

Wir erbitten Ihre Rueckaeusserung bis zum [Datum]. Bei Annahme wird
ein schriftlicher Vergleich beigefuegt.

Mit freundlichen Gruessen
[Name]
```

**Vergleichstext (Muster)**

```
VERGLEICH

zwischen
[Verlag], vertreten durch [Name]
- nachfolgend "Verlag" -

und
[Autor], wohnhaft [Adresse]
- nachfolgend "Autor" -

Praeambel
Die Parteien streiten ueber [Streitgegenstand]. Zur Vermeidung weiterer
Auseinandersetzungen und ohne Anerkennung einer Rechtspflicht
vereinbaren sie folgenden Vergleich:

§ 1 Leistungen
(1) Der Verlag zahlt an den Autor EUR [Betrag] (in Worten: [...]) bis
 [Datum] auf das Konto [...].
(2) Der Autor [liefert / verzichtet auf / uebertraegt ...].

§ 2 Abgeltungsklausel
Mit vollstaendiger Erfuellung der vorstehenden Leistungen sind
saemtliche wechselseitigen Ansprueche der Parteien aus oder im
Zusammenhang mit dem Verlagsvertrag vom [Datum] und dem Werk
[Titel] erledigt. Hiervon ausgenommen sind Ansprueche aus UrhG
§ 32a, soweit sie kraft Gesetzes nicht abdingbar sind.

§ 3 Vertraulichkeit
Die Parteien behandeln Inhalt und Tatsache dieses Vergleichs
vertraulich. Ausnahme: gesetzliche und steuerliche Offenbarungs-
pflichten.

§ 4 Gerichtsstand und Recht
Es gilt deutsches Recht. Gerichtsstand ist [Ort].

§ 5 Schriftform / Nebenabreden
Aenderungen und Ergaenzungen beduerfen der Schriftform.

Ort, Datum Ort, Datum
_________________ _________________
Verlag Autor
```

## Typische Fehler / Pitfalls

- Abgeltungsklausel zu weit gefasst - kann unwirksam sein (z. B. zukuenftige UrhG § 32a-Ansprueche).
- Keine Zahlungsfrist im Vergleich - Streit ueber Faelligkeit.
- Vergleich ohne Schriftform - bei Bestreiten kaum beweisbar.
- Vertraulichkeitsklausel ohne Sanktion - faktisch wirkungslos.
- Steuerliche Behandlung der Zahlung uebersehen (Schadensersatz, Honorar, Vergleichssumme).
- Vergleich ohne Beteiligung des Justiziariats bei rechtlich komplexer Lage.

## Querverweise

- `workflow-kaltstart-und-routing` - Eingangsroutung des Streits.
- `workflow-fristen-und-risikoampel` - Bewertung der Klagewahrscheinlichkeit.
- `verl-abstimmung-mit-rechtsabteilung-pruefung` - vor Unterzeichnung.
- `verl-eskalation-bei-deadline-konflikt` - vorgelagerte Eskalationsstufen.
- `verl-tantieme-abrechnung-jaehrlich` - bei Anpassungsstreit.
- `honorar-vertrag-royalties-triage` - Triage der Vertragslage.

## Quellen Stand 06/2026

- BGB §§ 145 ff., 305 ff., 779 - Angebot, AGB-Kontrolle, Vergleich.
- ZPO §§ 278, 794 - Vergleichsmoeglichkeit im Prozess, Vollstreckungstitel.
- UrhG §§ 32, 32a, 79b - Verguetung, Anpassung, Nichtabdingbarkeit.
- DSGVO Art. 6, 17 - bei Datenloeschung als Vergleichsleistung.
- BGH-Rechtsprechung zur Reichweite von Abgeltungsklauseln (Volltexte unter bundesgerichtshof.de und dejure.org).

## 5. `verl-vlb-katalog-pflege-jur`

**Fokus:** VLB-Katalog (Verzeichnis lieferbarer Buecher) pflegen: ONIX-Metadaten, Schlagworte, Klappentext, Reihen, Preisbindung, Erscheinungstermin-Pflege. Konsistenz mit Webshop, beck-online und Buchhandel.

# VLB-Katalog (Verzeichnis lieferbarer Buecher)

## Worum geht es konkret

Das VLB ist die zentrale Datenbank des Buchhandels in Deutschland. Wer dort nicht oder falsch eintraegt, wird im Buchhandel nicht gefunden. Der Skill fuehrt durch ONIX-Pflichtfelder, Schlagwortlogik, Klappentextpflege, Preisbindung, Erscheinungstermin-Updates und stellt sicher, dass VLB-Daten mit Webshop, beck-online und Vertriebspartnern konsistent sind.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Neueintrag, Pflegeaktualisierung oder Abkuendigung?
2. Werktyp (Buch, Loseblatt, E-Book, Hoerbuch, Online-Kommentar)?
3. ISBN bereits vergeben?
4. Erscheinungstermin definitiv oder vorlaeufig?
5. Preisbindung (Buch und E-Book unter BuchPrG) oder freier Preis (Webinar, Datenbank)?
6. Reihenzuordnung vorhanden?
7. Wer pflegt redaktionell (Vertrieb, Lektorat, Marketing)?

## Rechtlicher und sachlicher Rahmen

- BuchPrG - Buchpreisbindungsgesetz; Verlag setzt den Endkundenpreis, Buchhandel ist gebunden. Geltung fuer Print und E-Book.
- HGB § 24 - Firmenfortfuehrung bei Verlagsverkauf, fuer Imprint-Wechsel.
- UrhG §§ 22, 23 - Bildnisrecht bei Coverabbildungen mit Personen.
- DSGVO Art. 6 - bei Verarbeitung von Autorenkontaktdaten in VLB-Profilen.
- ONIX 3.0 - Standardformat fuer bibliografische Daten; VLB akzeptiert ONIX 3.0.
- BVA (Buchwissenschaftliches Verlagshaus / Boersenverein) - Verlagsdienstleister fuer VLB-Eintragungen.

## Praxisleitfaden / Schritt fuer Schritt

1. **Pflichtfelder pruefen.**
 - ISBN, Titel, Autor (mit GND-Nummer wenn moeglich).
 - Untertitel, Reihentitel, Bandzaehlung.
 - Erscheinungstermin (Tag, Monat, Jahr).
 - Verlag, Verlagsanschrift, Imprint.
 - Sprache, Originalsprache, Uebersetzer.
 - Format (Hardcover, Paperback, EPUB, PDF), Seitenzahl.
 - Preis brutto, Waehrung.
 - Warengruppe (juristische Werke: 750-789 nach VLB-Schluessel).
2. **Schlagwoerter setzen.** GND-Schlagworte bevorzugen; freie Schlagworte zusaetzlich; Thema-Klassifikation (Thema 1.4 international, LB-Codes verlagsintern).
3. **Klappentext pflegen.** Max. 2500 Zeichen; SEO-optimiert; mit den ersten 160 Zeichen den Kern fassen (Google-Snippet).
4. **Cover hochladen.** RGB, 300 dpi, mindestens 1500 px hohe Kante; ohne Anschnitt.
5. **Inhaltsverzeichnis und Leseprobe.** Als PDF, freigegeben durch Autor und Hersteller.
6. **Preisbindung.** Endkundenpreis fuer Print und E-Book in EUR, MwSt. eingeschlossen; bei Aenderung Boersenverein melden (BuchPrG § 5).
7. **Erscheinungstermin.** Bei Verschiebung VLB unverzueglich aktualisieren - sonst Vorbestellprobleme.
8. **Abkuendigung.** Bei Auslaufen "ng" (= nicht mehr lieferbar) oder "vg" (vergriffen) setzen; bei Neuauflage "ohne Nachfolger" oder Verweis auf Nachfolgeauflage.
9. **Konsistenz pruefen** mit Webshop, beck-online, Amazon, Thalia, Hugendubel, Buchhandelsdienst-Anbietern.

## Trade-off-Matrix

| Aspekt | Aufwendige Pflege | Minimaleintrag |
|---|---|---|
| Findbarkeit | Hoch | Niedrig |
| Vertriebserfolg | Hoeher | Niedriger |
| Pflegeaufwand | Hoch | Niedrig |
| Update-Notwendigkeit | Reduzierend | Verschlimmernd |
| Backbone fuer Marketing | Stark | Schwach |

## Praxistipps der alten Redaktion

- VLB-Eintrag spaetestens 12 Wochen vor Erscheinung; sonst keine Vorbestelllisten.
- Coverdatei muss in den Spezifikationen sein, sonst lehnt VLB ab.
- Bei juristischen Werken Warengruppe sehr genau setzen; 758 (BGB allg.) vs. 769 (Steuerrecht).
- Schlagworte aus der Sicht der Suchenden, nicht aus Verlagssicht ("Mietminderung Schimmel" statt "Mietminderungsproblematik").
- Klappentext im Praesens, aktive Saetze, keine Floskeln.
- Auflagen-Wechsel: Vorgaengerauflage auf "ng" setzen, ISBN der neuen Auflage als Nachfolger eintragen.
- Preisaenderung mit Stichtag und Begruendung melden - Buchpreisbindungstreuhaender prueft.

## Mustertexte / Vorlagen

**Klappentext-Geruest (juristisches Werk)**

```
[Titel]
[Untertitel]

Das Werk bietet [Zielgruppe, Anwaltschaft/Justiz/Wissenschaft] eine
[Kommentierung / Darstellung / Praxisleitfaden] zu [Norm/Themenfeld].
Die [n]. Auflage beruecksichtigt:

- [Reform/Gesetz, Datum]
- [Wichtige BGH-Entscheidung mit Az., Datum]
- [Praktische Auswirkungen, ein Satz]

Mit [Praxistipps / Mustertexten / Checklisten / Beispielsfaellen]
laesst sich das Werk auch im Mandatsalltag direkt nutzen.

Die Autorinnen und Autoren sind [kurze Vorstellung, max. 2 Saetze].
```

**ONIX-Mindesteintrag-Checkliste**

```
ISBN-13: [978-...]
Titel: [...]
Untertitel: [...]
Reihe (Codeliste): [...]
Autor: [Name, GND, Funktion]
Verlag/Imprint: [...]
Erscheinungsdatum: [TT.MM.JJJJ]
Sprache: ger
Format: [HC/PB/EB], [Hoehe x Breite] mm
Seitenzahl: [n]
Warengruppe: [VLB-Code]
GND-Schlagworte: [Liste]
Thema-Klassifikation: [Code]
Preis: EUR [...], inkl. 7 % MwSt. (Buch) / 7 % (E-Book)
Klappentext: [siehe oben]
Cover-Datei: [Pfad/URL, 300 dpi RGB]
Inhaltsverzeichnis: [PDF]
```

**Anschreiben Boersenverein bei Preisaenderung**

```
Betreff: Aenderung des gebundenen Endkundenpreises [Titel], ISBN [...]

Sehr geehrte Damen und Herren,

hiermit zeigen wir die Aenderung des nach BuchPrG gesetzten
Endkundenpreises fuer folgendes Werk an:

ISBN: [...]
Titel: [...]
Bisheriger Preis: EUR [...]
Neuer Preis: EUR [...]
Stichtag: [Datum]
Begruendung: [...]

Mit freundlichen Gruessen
[Name, Funktion]
```

## Typische Fehler / Pitfalls

- Erscheinungstermin verschoben, VLB nicht aktualisiert - Vorbesteller verlieren.
- Klappentext ohne Schlagworte - schlechte Findbarkeit.
- Coverdatei in falscher Aufloesung - Eintragung wird abgelehnt.
- Preisbindung versaeumt zu melden - Buchpreisbindungstreuhaender mahnt.
- Reihenzuordnung falsch oder fehlt - Suchen Reihe leer.
- Bei E-Book und Print abweichende Klappentexte - Marketing inkonsistent.
- Auflagenwechsel ohne Verweis auf Nachfolger - alte ISBN bleibt aktiv.

## Querverweise

- `workflow-kaltstart-und-routing` - Einordnung des Pflegevorgangs.
- `metadaten-seo-klappentext` - Konsistenz mit Klappentext.
- `sales-katalog-vlb-buchhandel` - vertriebliche Begleitung.
- `verl-pressetext-rechtsthemen` - PM zum Erscheinen.
- `verl-buchprojekt-bauleiter` - Bauleitung Projekt.

## Quellen Stand 06/2026

- BuchPrG - Buchpreisbindungsgesetz.
- ONIX-Standard 3.0 - editeur.org.
- VLB-Hinweise und Codelisten - vlb.de (Boersenverein).
- BVA-Verlagsdienstleister - mvb-online.de.
- GND - Gemeinsame Normdatei der Deutschen Nationalbibliothek (dnb.de).
