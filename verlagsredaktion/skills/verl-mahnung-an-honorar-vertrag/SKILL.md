---
name: verl-mahnung-an-honorar-vertrag
description: "Verl Mahnung AN Honorar Vertrag: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verl Mahnung AN Honorar Vertrag

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Verl Mahnung AN Honorar Vertrag** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verl-mahnung-an-autor-zahlung-frist` | Mahnung an Autor bei Rueckforderung von Vorschuss oder ueberzahltem Honorar: Stufenmodell, Nachfrist gemaess BGB § 286 und § 323, Verjaehrungspruefung, Mustertexte und gerichtliche Geltendmachung. |
| `honorar-vertrag-royalties-triage` | Triage fuer Autor:innenvertrag, Honorar, Tantiemen, Pauschale, Nebenrechte, Abrechnung, Nutzungsarten und Eskalation an Justiziariat. |
| `verl-honorarvertrag-templates-und-abweichungen` | Honorarvertragstemplates fuer juristische Werke: Standardvertrag Aufsatz, Buch, Kommentar, Herausgeberwerk. Abweichungspruefung gegen UrhG § 32 angemessene Verguetung. |
| `verl-haftungsfreistellung-autor-verlag` | Haftungsfreistellung zwischen Autor und Verlag: Klauselbaustein im Verlagsvertrag, Reichweite, AGB-Schranken, Versicherungsfragen, Praxis bei Abmahnung und Klage. |
| `buchprojekt-kapitelkoordination` | Steuert Buchprojekte, Kapitel, Autor:innen, Herausgeber:innen, Register, Abbildungen, Vorwort, Fristen und Produktionsstand. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Verl Mahnung AN Honorar Vertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verl-mahnung-an-autor-zahlung-frist`

**Fokus:** Mahnung an Autor bei Rueckforderung von Vorschuss oder ueberzahltem Honorar: Stufenmodell, Nachfrist gemaess BGB § 286 und § 323, Verjaehrungspruefung, Mustertexte und gerichtliche Geltendmachung.

# Mahnung an Autor

## Worum geht es konkret

Der Verlag muss Geld vom Autor zurueckfordern: ueberzahlte Tantiemen (z. B. nach Retoure-Bereinigung), nicht abgegoltener Vorschuss bei Manuskript-Verzug, Rueckforderung wegen mangelhafter Werkleistung, doppelte Auszahlung. Der Skill beschreibt das Stufenmodell der Mahnung, die Anforderungen an einen Schuldnerverzug, die Verjaehrungspruefung und die gerichtliche Geltendmachung (Mahnbescheid, Klage).

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche Forderung in welcher Hoehe (EUR, Faelligkeit, Rechtsgrund)?
2. Gibt es eine schriftliche Anerkennung (Vertrag, Abrechnung)?
3. Hat der Autor schon reagiert (gar nicht, Ablehnung, Teilzahlung, Vergleichsangebot)?
4. Verjaehrungslage (Frist nach BGB § 195 grundsaetzlich 3 Jahre)?
5. Ist der Autor Verbraucher oder Unternehmer (BGB § 13/14)?
6. Eilbedarf (Zahlungsunfaehigkeitsgefahr, Vermoegensverfall)?
7. Mahnung allein oder Eskalation an Inkasso / Justiziariat?

## Rechtlicher und sachlicher Rahmen

- BGB § 286 - Schuldnerverzug; Mahnung erforderlich, soweit kein Termin nach dem Kalender bestimmt ist; nach 30 Tagen ab Faelligkeit Verzug ohne Mahnung bei Verbrauchern nur mit Hinweis nach BGB § 286 Abs. 3.
- BGB § 288 - Verzugszinsen: 5 Prozentpunkte ueber Basiszinssatz bei Verbrauchern, 9 Prozentpunkte ueber Basiszinssatz bei B2B.
- BGB § 195 - Regelverjaehrung 3 Jahre; Beginn nach BGB § 199.
- BGB § 812 - Rueckforderung wegen Bereicherung bei ueberzahlten Tantiemen.
- VerlG § 33 - Rueckforderung von Vorschuss bei Ruecktritt.
- ZPO §§ 688 ff. - Mahnverfahren; ZPO § 690 - Antrag auf Erlass eines Mahnbescheids.
- BGB § 309 Nr. 5 - Pauschalierter Schadensersatz und Mahnkosten in AGB (AGB-Schranke!).

## Praxisleitfaden / Schritt fuer Schritt

1. **Forderung sauber ermitteln.** Hoehe, Faelligkeit, Rechtsgrund, Belege.
2. **Verjaehrungspruefung.** Wann begann die Verjaehrung? Drohen Massnahmen vor Jahresende?
3. **Erste Zahlungsaufforderung** (freundlich, ohne juristische Drohung). Frist 14 Tage.
4. **Zweite Zahlungsaufforderung** mit Nachfristsetzung gemaess BGB § 286. Ankuendigung der Verzugszinsen.
5. **Dritte Mahnung** - letzte Mahnung mit Ankuendigung gerichtlicher Schritte. Frist 14 Tage.
6. **Mahnbescheid (ZPO §§ 688 ff.)** beim Mahngericht (oertlich zustaendig nach Wohnsitz). Kosten gering, hemmt Verjaehrung.
7. **Bei Widerspruch:** Streitige Verfahren - Klage einreichen oder Klage abgeben.
8. **Vollstreckungsbescheid** bei keinem Widerspruch nach 2 Wochen; Titel fuer Zwangsvollstreckung.
9. **Parallel:** Vergleichsangebot pruefen (siehe `verl-vergleichsverhandlung-mit-autor`).

## Trade-off-Matrix

| Aspekt | Schnelle gerichtliche Geltendmachung | Lange aussergerichtliche Mahnung |
|---|---|---|
| Verjaehrungssicher | Hoch | Niedrig |
| Beziehung zum Autor | Belastet | Geschont |
| Kosten | Vorab Mahn-/Gerichtskosten | Niedriger |
| Image | "Hartleibig" | "Geduldig" |
| Erfolgswahrscheinlichkeit | Hoch bei klarem Anspruch | Variabel |

## Praxistipps der alten Redaktion

- Mahnbescheid kurz vor Verjaehrungsende einreichen, wenn der Autor nicht reagiert.
- Vorletzte Mahnung immer per Einschreiben - bei Bestreiten der Zustellung Beweis.
- Verzugszinsen nicht vergessen - die Buchhaltung uebersieht sie oft.
- Bei Verbraucher-Autor (Privatperson) Verzug erst nach Mahnung; bei B2B Schuldnerverzug 30 Tage nach Faelligkeit, auch ohne Mahnung (BGB § 286 Abs. 3).
- Mahnkosten als Pauschale (5 EUR Verbraucher, 40 EUR B2B nach BGB § 288 Abs. 5) sind zulaessig.
- Bei mehreren Forderungen: Tilgungsbestimmung (BGB § 366) klaeren, sonst Anrechnung auf aelteste.

## Mustertexte / Vorlagen

**Erste Zahlungsaufforderung**

```
Betreff: Zahlungsaufforderung - [Bezug, z. B. Rueckforderung Vorschuss]

Sehr geehrte Frau/Herr [Autorenname],

aus der mit Datum [...] vorgenommenen Abrechnung des Werks "[Titel]"
ergibt sich zu Ihren Lasten ein Saldo in Hoehe von EUR [Betrag].

Wir bitten Sie, den Betrag bis zum [Datum, 14 Tage] auf folgendes
Konto zu ueberweisen:
[Bankdaten]
Verwendungszweck: [Aktenzeichen]

Bei Fragen zur Abrechnung steht Ihnen [Ansprechpartner] zur
Verfuegung.

Mit freundlichen Gruessen
[Name]
```

**Mahnung mit Nachfristsetzung**

```
Betreff: Mahnung - Ihre Schuld in Hoehe von EUR [Betrag]

Sehr geehrte Frau/Herr [Autorenname],

trotz unserer Zahlungsaufforderung vom [Datum] ist der offene Betrag
in Hoehe von EUR [Betrag] bis heute nicht eingegangen.

Wir setzen Ihnen hiermit eine letzte Nachfrist bis zum [Datum,
14 Tage]. Sollte die Zahlung bis dahin nicht eingegangen sein, geraten
Sie in Schuldnerverzug (BGB § 286). Wir machen dann Verzugszinsen
in Hoehe von [9/5] Prozentpunkten ueber dem Basiszinssatz sowie
die Mahnpauschale von EUR [40/5] geltend.

Behalten Sie uns ueberdies die Einleitung des gerichtlichen
Mahnverfahrens vor.

Mit freundlichen Gruessen
[Name]
```

**Letzte Mahnung mit Ankuendigung des Mahnbescheids**

```
Betreff: Letzte Mahnung vor gerichtlichen Schritten

Sehr geehrte Frau/Herr [Autorenname],

unsere Mahnung vom [Datum] ist unbeantwortet geblieben. Der offene
Betrag in Hoehe von EUR [Betrag] zuzueglich Verzugszinsen ist nach
wie vor nicht beglichen.

Wir setzen Ihnen letztmals eine Frist bis zum [Datum, 14 Tage].
Sollte die Zahlung bis dahin nicht erfolgen, werden wir ohne weitere
Ankuendigung einen Antrag auf Erlass eines Mahnbescheids (ZPO §§ 688 ff.)
beim zustaendigen Mahngericht einreichen. Die hierdurch entstehenden
Mehrkosten haben Sie dann zu tragen.

Wir empfehlen Ihnen, sich kurzfristig mit uns in Verbindung zu setzen.

Mit freundlichen Gruessen
[Name]
```

## Typische Fehler / Pitfalls

- Mahnung ohne klare Fristsetzung - kein Verzugseintritt.
- Verjaehrung uebersehen - Anspruch wird unerfuellbar (Einrede).
- Mahnpauschale falsch bemessen - Korrektur erforderlich.
- Mahnbescheid bei oertlich falschem Mahngericht - Verzoegerung.
- Doppelmahnung an verschiedene Adressen, ohne Tilgungsbestimmung.
- Bei juristischer Person als Autor (z. B. Sozietaet) falsche Empfaengerbezeichnung.

## Querverweise

- `workflow-kaltstart-und-routing` - Eingangsroutung der Forderung.
- `workflow-fristen-und-risikoampel` - Verjaehrungs- und Verzugsampel.
- `verl-vorschuss-pruefung-buecher` - bei Vorschussrueckforderungen.
- `verl-tantieme-abrechnung-jaehrlich` - bei ueberzahlten Tantiemen.
- `verl-vergleichsverhandlung-mit-autor` - aussergerichtliche Loesung.
- `verl-eskalation-bei-deadline-konflikt` - bei kombinierter Leistungs- und Zahlungsstoerung.

## Quellen Stand 06/2026

- BGB §§ 195, 199, 286, 288, 309 Nr. 5, 366, 812 - Verjaehrung, Verzug, Verzugszinsen, AGB-Schranke, Tilgungsbestimmung, Bereicherung.
- VerlG § 33 - Folgen Nichtlieferung; Rueckforderung Vorschuss.
- ZPO §§ 688-703d - Mahnverfahren, Vollstreckungsbescheid.
- Basiszinssatz (Deutsche Bundesbank, halbjaehrliche Anpassung) unter bundesbank.de.

## 2. `honorar-vertrag-royalties-triage`

**Fokus:** Triage fuer Autor:innenvertrag, Honorar, Tantiemen, Pauschale, Nebenrechte, Abrechnung, Nutzungsarten und Eskalation an Justiziariat.

# Honorar, Vertrag und Royalties

## Ziel

Redaktionelle Vorprüfung, keine Vertragsrechtsberatung aus dem Stand.

## Prüfpunkte

- Vertrag vorhanden?
- Werkumfang und Abgabetermin.
- Honorar pauschal oder prozentual.
- Print, E-Book, Online, Datenbank, Übersetzung, Hörbuch.
- Abrechnungsturnus.
- Nebenrechte.
- Rücktritt, Verzug, Kürzung.

## Output

- Vertragsdatenkarte.
- offene Punkte.
- rote Flaggen.
- Fragen an Rechte/Justiziariat.
- Mail an Autor:in.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `verl-honorarvertrag-templates-und-abweichungen`

**Fokus:** Honorarvertragstemplates fuer juristische Werke: Standardvertrag Aufsatz, Buch, Kommentar, Herausgeberwerk. Abweichungspruefung gegen UrhG § 32 angemessene Verguetung.

# Honorarvertrags-Templates

## Worum geht es konkret

Verlage halten Standardvertraege vor: Aufsatzvertrag, Lehrbuchvertrag, Kommentarvertrag, Herausgebervertrag, Loseblattvertrag. Der Skill systematisiert die Templates, listet die haeufigsten Verhandlungsabweichungen und prueft jede Abweichung gegen die Pflicht zur angemessenen Verguetung (UrhG § 32) sowie typische Streitpunkte aus der Vertragspraxis.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welches Werktyp soll vertraglich abgebildet werden (Aufsatz, Buch, Kommentar, Festschrift, Loseblatt, Online)?
2. Einzelautorin oder Mehrautoren / Herausgeberwerk?
3. Pauschalhonorar oder Tantieme?
4. Sublizenzierung an Datenbanken (juris, beck-online) vorgesehen?
5. Bearbeitungspflicht / Aktualisierungspflicht (Folgeauflagen)?
6. Karenzklausel / Konkurrenzschutz?
7. Welche Abweichung will der Autor durchsetzen?

## Rechtlicher und sachlicher Rahmen

- VerlG §§ 1-29 - Verlagsvertrag, Pflichten Verfasser und Verlag.
- UrhG §§ 31, 31a - Einraeumung von Nutzungsrechten, unbekannte Nutzungsarten (Schriftform).
- UrhG § 32 - angemessene Verguetung; § 32a Bestsellerklausel; § 32d Auskunftspflicht.
- UrhG § 40a - Recht der anderweitigen Verwertung nach 10 Jahren bei pauschaler Verguetung.
- UrhG § 41 - Rueckruf wegen Nichtausuebung.
- BGB §§ 305 ff. - AGB-Kontrolle bei vorformulierten Vertraegen, auch zwischen Unternehmern eingeschraenkt.
- WissZeitVG-Bezug bei Hochschulautoren (Nebentaetigkeitsrecht, Dienstpflichten).

## Praxisleitfaden / Schritt fuer Schritt

1. **Template auswaehlen.** Nach Werktyp - falsche Vorlage erzeugt unsaubere Klauseln.
2. **Pflichtklauseln pruefen.**
 - Werkbeschreibung (Titel, Umfang, Termine).
 - Honorar (Pauschale / Tantiemestaffel / Vorschuss).
 - Nutzungsrechte (raeumlich, zeitlich, inhaltlich, Sublizenz).
 - Bearbeitungspflicht (Folgeauflagen, Aktualisierungen).
 - Druck und Vertrieb (Auflage, Erscheinungstermin, Aboerstreckung).
 - Imprimaturrecht und Mitwirkungspflichten.
 - Ruecktritts- und Verzugsregelungen.
 - Karenz / Konkurrenzschutz (zeitlich begrenzen!).
 - Datenschutz und Werbenutzung des Namens.
3. **Verhandlungsabweichungen aufnehmen.** In Aenderungsvermerk-Tabelle: Klausel - alt - neu - Begruendung des Autors - Verlagsantwort.
4. **Angemessenheitspruefung.** Bei stark abweichenden Saetzen Vergleich mit branchenueblichen Verguetungsregeln (z. B. Hinweise Boersenverein, Verbandsempfehlungen Wissenschaftsverlage).
5. **Justiziariat einbinden** bei: Pauschalverguetung trotz hoher Auflagenerwartung, Total-Buy-Out, ungewoehnlicher Karenz, internationalem Bezug.
6. **Schlussfassung erstellen.** Reinschrift, beidseits paraphieren und unterschreiben.

## Trade-off-Matrix

| Aspekt | Pauschalhonorar | Tantieme |
|---|---|---|
| Planungssicherheit Verlag | Hoch | Niedrig |
| Anreiz Autor an Vermarktung | Niedrig | Hoch |
| Buchhalterischer Aufwand | Einmalig | Jaehrlich |
| Risiko § 32a-Anpassung | Hoeher | Geringer |
| Eignung Aufsatz | Standard | Unueblich |
| Eignung Lehrbuch / Kommentar | Selten | Standard |

## Praxistipps der alten Redaktion

- Pauschalhonorar nur fuer Aufsaetze und kleine Werke; ab Lehrbuch Tantieme.
- Nutzungsrechte einzeln benennen: Print, E-Book, Datenbank, Online-Kommentar, Hoerbuch, Uebersetzung, Bearbeitung.
- Karenzklausel niemals laenger als zwei Jahre nach Vertragsende - sonst kartell- und berufsrechtlich problematisch.
- Sublizenzgewinne (Datenbank-Eintrag) zumindest teilweise an Autorin auskehren - sonst spaeter § 32a.
- Bei Hochschullehrer: Nebentaetigkeitsregelung der Universitaet beachten, sonst hat der Dienstherr ein Wort mitzureden.
- Co-Autoren-Werk: Kapitelplan und Verteilungsschluessel zwingend mitvereinbaren.

## Mustertexte / Vorlagen

**Klauselbaustein Nutzungsrechte (Lehrbuch)**

```
§ [n] Nutzungsrechte

(1) Der Autor raeumt dem Verlag das ausschliessliche, raeumlich,
 zeitlich und inhaltlich unbeschraenkte Recht ein, das Werk zu
 vervielfaeltigen, zu verbreiten, oeffentlich wiederzugeben und
 in koerperlicher und unkoerperlicher Form zu nutzen, insbesondere
 in folgenden Nutzungsarten:
 a) Print (Buchausgabe, Sonderausgabe, Lizenzausgabe);
 b) E-Book (EPUB, PDF, alle gaengigen Vertriebsplattformen);
 c) Datenbank-Einstellung (juris, beck-online, vergleichbare
 Anbieter);
 d) Online-Kommentar-Plattformen;
 e) Bearbeitung und Uebersetzung in fremde Sprachen;
 f) Werbung und Vorabdruck.

(2) Unbekannte Nutzungsarten im Sinne von § 31a UrhG werden gesondert
 schriftlich vereinbart.

(3) Die Einraeumung umfasst auch das Recht zur Vergabe von
 Sublizenzen. Die hieraus erzielten Einnahmen werden gemaess § [n]
 zwischen den Parteien geteilt.
```

**Pruefraster Abweichungsantrag des Autors**

```
Klausel: [Nummer]
Standardfassung: [Text]
Aenderungswunsch Autor: [Text]
Begruendung des Autors: [Text]
Verlagsantwort (Pruefer): [zustimmend / Gegenvorschlag / ablehnen]
Begruendung: [Text]
Auswirkung auf andere Klauseln: [...]
Justiziariat einbinden? [ja/nein]
```

**Karenzklausel (Beispielsformulierung)**

```
§ [n] Konkurrenzschutz

(1) Der Autor verpflichtet sich, fuer die Dauer von 24 Monaten nach
 Erscheinen der jeweils aktuellen Auflage des Werks kein
 konkurrierendes Werk vergleichbaren Inhalts und vergleichbaren
 Adressatenkreises bei einem anderen Verlag zu veroeffentlichen.
(2) Aufsaetze und Beitraege zu Festschriften gelten nicht als
 konkurrierende Werke.
(3) Diese Klausel endet spaetestens mit Ablauf von vier Jahren nach
 Vertragsschluss.
```

## Typische Fehler / Pitfalls

- Total-Buy-Out fuer alle Nutzungsarten mit Pauschale - § 32a-Risiko.
- Sublizenzen ohne Erloesteilung - Anpassungsdruck.
- Karenzklausel ohne Zeit- oder Reichweitenbegrenzung - unwirksam.
- Unbekannte Nutzungsarten ohne Schriftform - § 31a UrhG-Falle.
- Bearbeitungspflicht ohne Honorierung der Neuauflage.
- Datenschutzklausel zur Werbenutzung des Autorennamens fehlt.

## Querverweise

- `workflow-kaltstart-und-routing` - Einordnung des Vertragsanlasses.
- `honorar-vertrag-royalties-triage` - schnelle Triage der Vertragslage.
- `verl-vorschuss-pruefung-buecher` - Vorschussklausel im Vertrag.
- `verl-zweitverwertungsrechte-pauschal` - Behandlung der Nebenrechte.
- `verl-abstimmung-mit-rechtsabteilung-pruefung` - Justiziariatsabstimmung.
- `rechtecheck-urhg-verlg` - Detailpruefung urheber- und verlagsrechtlicher Klauseln.

## Quellen Stand 06/2026

- VerlG §§ 1-29 - Pflichten der Vertragsparteien.
- UrhG §§ 31, 31a, 32, 32a, 32d, 40a, 41 - Nutzungsrechte und Verguetung.
- BGB §§ 305 ff. - AGB-Kontrolle.
- Gemeinsame Verguetungsregeln (z. B. Boersenverein, Verband deutscher Schriftsteller); aktuelle Fassungen unter den Verbandsseiten.
- BGH-Rechtsprechung zu § 32a UrhG (Volltexte unter bundesgerichtshof.de).

## 4. `verl-haftungsfreistellung-autor-verlag`

**Fokus:** Haftungsfreistellung zwischen Autor und Verlag: Klauselbaustein im Verlagsvertrag, Reichweite, AGB-Schranken, Versicherungsfragen, Praxis bei Abmahnung und Klage.

# Haftungsfreistellung Autor / Verlag

## Worum geht es konkret

Bei Veroeffentlichung urheberrechtlich oder aeusserungsrechtlich kritischer Beitraege koennen Ansprueche Dritter (Abmahnung, Schadensersatz, Unterlassung) den Verlag treffen. Vertraglich wird in der Regel eine Haftungsfreistellung mit dem Autor vereinbart: der Autor versichert die Rechtekonformitaet und stellt den Verlag von berechtigten Ansprueche Dritter frei. Der Skill beschreibt Reichweite, AGB-Schranken und Praxis bei Eintritt des Versicherungsfalls.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welches Werk und welche Rechtegrundlage (Zitate, Bilder, Daten, Persoenlichkeitsrecht)?
2. Welcher Vertragstyp (Aufsatz, Buch, Kommentar, Webinar)?
3. Steht eine konkrete Abmahnung oder Klage im Raum?
4. Ist der Autor Verbraucher oder Unternehmer (AGB-Pruefung)?
5. Liegt eine Verlagshaftpflichtversicherung vor?
6. Wie weit reicht die Klausel im Vertrag des Verlags (Standard, individuell verhandelt)?
7. Bestaetigt der Autor die Rechtekonformitaet bei Manuskript-Einreichung (Manuskripterklaerung)?

## Rechtlicher und sachlicher Rahmen

- BGB §§ 280, 311 - Verletzung vertraglicher Nebenpflichten; vorvertragliche Aufklaerung.
- BGB §§ 305 ff. - AGB-Kontrolle; unangemessene Benachteiligung des Autors als Verbraucher (BGB § 307); bei B2B eingeschraenkt.
- BGB § 426 - Innenausgleich bei Gesamtschuldnerschaft (Autor + Verlag).
- UrhG §§ 97, 97a - Schadensersatz, Abmahnung; UrhG § 100 Restitutionsklage.
- UWG § 8 Abs. 4 - Verbot des Missbrauchs der Abmahnung.
- VVG (Versicherungsvertragsgesetz) - Anzeigepflichten und Obliegenheiten gegenueber Verlagshaftpflicht.

## Praxisleitfaden / Schritt fuer Schritt

1. **Standardklausel pruefen.** Wie weit ist die Haftungsfreistellung des Autors formuliert (Rechte am Werk, Zitierfreiheit, Bildrechte, Persoenlichkeitsrechte, Datenrechte)?
2. **AGB-Grenze.** Bei Verbraucher-Autor (Privatperson, kein Unternehmer): Klausel darf nicht ueber typische, vorhersehbare Risiken hinausgehen; bei B2B weitere Reichweite.
3. **Manuskripterklaerung** vor Drucklegung: kurze Bestaetigung des Autors, dass alle Quellen rechtekonform verwendet wurden.
4. **Versicherung.** Verlagshaftpflicht mit Vermoegensschadenbaustein pruefen; Selbstbehalt klaeren.
5. **Bei Eintritt des Anspruchs.** Anzeige an Versicherung innerhalb der vertraglichen Frist; Autor informieren; gemeinsame Verteidigung mit Justiziariat.
6. **Aussergerichtliche Loesung.** Kommunikation mit Anspruchsteller; ggf. Vergleich; Innenausgleich Autor/Verlag nach BGB § 426.
7. **Gerichtsverfahren.** Streitverkuendung an Autor (ZPO § 72), Versicherungsdeckung in Anspruch nehmen.

## Trade-off-Matrix

| Aspekt | Weite Haftungsfreistellung | Enge Haftungsfreistellung |
|---|---|---|
| Verlagsschutz | Hoch | Niedrig |
| AGB-Risiko | Hoch (unwirksam) | Niedrig |
| Autorenakzeptanz | Niedrig (verhandlungsbeladen) | Hoch |
| Versicherungskosten | Niedrig | Hoeher |
| Streitfreudigkeit | Niedrig | Hoeher |

## Praxistipps der alten Redaktion

- Standardklausel niemals als Eckwert hinstellen; verhandelbar machen.
- Manuskripterklaerung in Lektoratsprozess fest verankern.
- Bei Bildmaterial des Autors Lizenznachweis pflichtmaessig einholen.
- Versicherungsfall sofort melden, sonst Deckungslosigkeit.
- Bei Abmahnung den Autor nicht "ausschliessen", sondern einbinden - er ist oft die beste Informationsquelle.
- Streitverkuendung sichert spaeteren Regress.
- Innenausgleich nach Verschuldensanteil rechnen, nicht "automatisch 100 Prozent beim Autor".

## Mustertexte / Vorlagen

**Klauselbaustein Haftungsfreistellung**

```
§ [n] Zusicherungen und Haftungsfreistellung

(1) Der Autor versichert, dass er das Werk selbststaendig verfasst
 und nicht in unzulaessiger Weise von Dritten uebernommen hat.
 Er versichert weiter, dass er ueber alle erforderlichen
 urheberrechtlichen Befugnisse verfuegt, einschliesslich der
 Zustimmung Dritter zur Verwendung deren Werkteilen, Abbildungen,
 Tabellen und Daten.

(2) Der Autor versichert, dass das Werk weder das Persoenlichkeits-
 recht Dritter noch sonstige Rechte Dritter verletzt und keine
 strafbaren Inhalte enthaelt.

(3) Soweit der Verlag aus berechtigten Ansprueche Dritter wegen
 Verletzung der vorstehenden Zusicherungen in Anspruch genommen
 wird, stellt der Autor den Verlag von diesen Ansprueche frei,
 insbesondere von angemessenen Kosten der Rechtsverteidigung
 (gesetzliche Gebuehren des Anwalts und Gerichtskosten).

(4) Der Verlag wird den Autor unverzueglich nach Kenntnis von einem
 geltend gemachten Anspruch informieren und ihm Gelegenheit zur
 Stellungnahme geben. Die Verteidigung wird gemeinsam abgestimmt.

(5) Die Freistellung gilt nicht, soweit der Autor nachweist, dass
 die Inanspruchnahme auf einem ausschliesslichen Verschulden des
 Verlags beruht.
```

**Manuskripterklaerung (vor Drucklegung)**

```
MANUSKRIPTERKLAERUNG

zum Werk: [Titel]
Vertrag vom: [Datum]

Ich versichere hiermit:

1. Das Manuskript ist mein urheberrechtlich geschuetztes Werk. Soweit
 ich Werkteile, Tabellen, Schaubilder oder Daten Dritter verwendet
 habe, habe ich die erforderlichen Nutzungsrechte eingeholt.
2. Die im Manuskript enthaltenen Aussagen ueber Personen sind sorgfaeltig
 recherchiert. Ich habe weder Persoenlichkeitsrechte Dritter noch
 Aeusserungsrecht in unzulaessiger Weise verletzt.
3. Bei Verwendung von Abbildungen liegen mir die schriftlichen
 Lizenznachweise vor, die ich auf Anforderung dem Verlag uebermittele.
4. Bei Personenbildern liegt mir die schriftliche Einwilligung der
 abgebildeten Personen vor.

Ort, Datum, Unterschrift Autor
```

**Anschreiben an Autor bei Abmahnung**

```
Betreff: Abmahnung wegen [Werk] - Bitte um Stellungnahme bis [Datum]

Sehr geehrte Frau/Herr [Autorenname],

am [Datum] ist beim Verlag eine Abmahnung der Frau/Herrn [...]
eingegangen. Beanstandet wird folgende Passage in Ihrem Werk
"[Titel]":

[Zitat]

Anhand der Abmahnung wird vorgetragen, dass [...].

Wir bitten Sie um eine sachliche Stellungnahme bis zum [Datum]. Bitte
teilen Sie uns insbesondere mit:
1. Quellen und Belege fuer die beanstandete Passage.
2. Lizenznachweise (sofern Bildmaterial).
3. Ihre Sicht auf die rechtliche Bewertung.

Wir werden auf Basis Ihrer Stellungnahme die Verteidigung mit unserem
Justiziariat abstimmen. Bitte beachten Sie die in unserem Verlagsvertrag
vereinbarte Haftungsfreistellung (§ [n]).

Mit freundlichen Gruessen
[Name]
```

## Typische Fehler / Pitfalls

- Pauschalfreistellung im AGB-Vertrag mit Verbraucher-Autor - unwirksam.
- Versicherung zu spaet informiert - Deckungsverlust.
- Streitverkuendung versaeumt - kein Regress.
- Autor "uebergeht" - bei Streit fehlt Information.
- Manuskripterklaerung nicht eingeholt - vor Gericht Beweisnot.
- Innenausgleich pauschal "100 Prozent Autor" - ohne Verschuldensanalyse unhaltbar.

## Querverweise

- `workflow-kaltstart-und-routing` - Eingangsroutung der Abmahnung.
- `workflow-fristen-und-risikoampel` - Abmahnfrist und Versicherungsfrist.
- `verl-honorarvertrag-templates-und-abweichungen` - Klauseltemplate.
- `verl-abstimmung-mit-rechtsabteilung-pruefung` - Justiziariatspflicht.
- `verl-rueckruf-fehlerbeitrag-spaet-erkannt` - bei kombinierten Massnahmen.
- `rechtecheck-urhg-verlg` - vertiefte urheberrechtliche Pruefung.

## Quellen Stand 06/2026

- BGB §§ 280, 305 ff., 307, 311, 426 - Pflichtverletzung, AGB-Kontrolle, vorvertragliche Aufklaerung, Innenausgleich.
- UrhG §§ 97, 97a, 100 - Schadensersatz, Abmahnung, Restitution.
- UWG § 8 Abs. 4 - Missbrauchsverbot Abmahnung.
- VVG - Versicherungsvertragsgesetz, insb. Anzeigepflicht.
- ZPO § 72 - Streitverkuendung.
- BGH-Rechtsprechung zur Haftungsfreistellungsklausel (Volltexte unter bundesgerichtshof.de).

## 5. `buchprojekt-kapitelkoordination`

**Fokus:** Steuert Buchprojekte, Kapitel, Autor:innen, Herausgeber:innen, Register, Abbildungen, Vorwort, Fristen und Produktionsstand.

# Buchprojekt- und Kapitelkoordination

## Ziel

Ein Buchprojekt als Projektkarte sichtbar machen.

## Output

- Kapitelmatrix.
- Autor:innenstatus.
- Fehlteile.
- Rechteampel.
- Abbildungsstatus.
- Register-/Stichwortliste.
- Vorwort-/Titelei-Check.
- Produktionsübergabe.

## Ampel

Grün: lieferbar. Gelb: Rückfrage. Rot: blockiert.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?

## Startfragen

Wenn Material oder Ziel unklar sind, stelle hoechstens drei Fragen: Was soll veroeffentlicht oder uebergeben werden? Fuer wen ist es bestimmt? Bis wann muss es freigegeben sein? Danach mit einer belastbaren Arbeitsfassung beginnen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
