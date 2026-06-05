---
name: streitwert-verkehrsunfall-vollstreckung
description: "Streitwert Verkehrsunfall Vollstreckung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Streitwert Verkehrsunfall Vollstreckung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Streitwert Verkehrsunfall Vollstreckung** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `streitwert` | Streitwert für zivilrechtliche Klagen berechnen: Hauptforderung, Nebenforderungen, Gerichts- und Anwaltsgebühren. Normen: §§ 3 9 ZPO, GKG, RVG. Prüfraster: Streitwertbemessung, Nebenforderungen, Kostenfolge. Output: Streitwertberechnung mit Kostentabelle. Abgrenzung: nicht Anspruchstabelle (Inhalt der Ansprüche). |
| `verkehrsunfall` | Verkehrsunfall-Mandat im Zivilprozess vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz. Normen: §§ 7 18 StVG, §§ 823 253 BGB, § 115 VVG. Prüfraster: Haftungsquote, Schadensposten, Verjaebrung, Regulierungsablauf. Output: Klageschrift Verkehrsunfall oder Klageerwiderung. Abgrenzung: nicht Strafrecht oder Ordnungswidrigkeiten. |
| `vollstreckung` | Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: §§ 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: Vollstreckungsauftrag und Pfaendungsbeschluss-Antrag. Abgrenzung: nicht AnfG-Anfechtung. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Streitwert Verkehrsunfall Vollstreckung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `streitwert`

**Fokus:** Streitwert für zivilrechtliche Klagen berechnen: Hauptforderung, Nebenforderungen, Gerichts- und Anwaltsgebühren. Normen: §§ 3 9 ZPO, GKG, RVG. Prüfraster: Streitwertbemessung, Nebenforderungen, Kostenfolge. Output: Streitwertberechnung mit Kostentabelle. Abgrenzung: nicht Anspruchstabelle (Inhalt der Ansprüche).

# Streitwertfestsetzung – GKG / RVG

## Zweck

Dieser Skill unterstützt bei der Berechnung des Streitwerts für gerichtliche
Verfahren (§§ 39 ff. GKG), des anwaltlichen Gegenstandswerts (§ 23 RVG) sowie
bei der Erstellung von Kostenfestsetzungsanträgen (§ 104 ZPO). Er dient ferner
der Überprüfung vorläufiger Streitwertfestsetzungen des Gerichts und der
Vorbereitung von Streitwertbeschwerden (§ 68 GKG).

Typischer Mandatskontext: Klagepartei oder Beklagte möchten die voraussichtlichen
Prozesskosten einschätzen; Kostenerstattungsstreit nach obsiegendem Urteil;
Gebührennote im Außerverhältnis.

## Eingaben

Das Modell benötigt folgende Informationen:

1. **Streitgegenstand** – Leistungsklage (§ 3 ZPO), Feststellungsklage (§ 256 ZPO;
 Abschlag i. d. R. 20–25 % vom Leistungsantrag), einstweilige Verfügung
 (i. d. R. 1/3 bis 1/2 des Hauptsachewerts).
2. **Gericht und Instanz** – Landgericht (Kammer für Handelssachen), Oberlandesgericht,
 BGH; Instanz bestimmt Gerichtsgebühr (Anlage 1 GKG).
3. **Hauptantrag und Hilfsantrag** – Wert der Hilfsanträge bleibt außer Betracht,
 solange sie nicht beschieden werden (§ 45 Abs. 1 Satz 2 GKG; Mehrwert nur bei
 Entscheidung, § 45 Abs. 1 Satz 3 GKG).
4. **Nebenforderungen** – Zinsen und Früchte nach § 43 Abs. 1 GKG nicht streitwerterhöhend
 (außer wenn sie Hauptgegenstand sind).
5. **Aufrechnung** – § 45 Abs. 3 GKG: Aufrechnung erhöht den Streitwert bis zur
 Höhe des Klageanspruchs, nicht darüber hinaus.
6. **Anwaltsgebühren** – Gegenstandswert nach § 23 Abs. 1 Satz 1 RVG entspricht
 dem Streitwert; § 23 Abs. 3 RVG bei Sonderregeln (z. B. Wohnraum).

## Rechtlicher Rahmen

### Zentrale Normen

- **§§ 39–48 GKG** – Allgemeine Grundsätze der Streitwertberechnung im Zivilprozess.
- **§ 3 ZPO** – Streitwertschätzung durch das Gericht nach freiem Ermessen.
- **§ 45 GKG** – Hilfsanträge und Aufrechnung.
- **§ 43 GKG** – Zinsen, Früchte, Nutzungen nicht streitwerterhöhend.
- **§ 68 GKG** – Streitwertbeschwerde; Frist: 6 Monate nach Rechtskraft.
- **§ 23 RVG** – Gegenstandswert für anwaltliche Vergütung.
- **§ 104 ZPO** – Kostenfestsetzungsverfahren; Antrag beim Urkundsbeamten.
- **§ 103 ZPO** – Kostenfestsetzungsantrag, Kostentitel Voraussetzung.

### Aenderungen ab 01.01.2026

Mit dem Gesetz zur Aenderung des Zustaendigkeitsstreitwerts der Amtsgerichte (BGBl. 2025 I Nr. 318 vom 11.12.2025) gelten ab 01.01.2026:

- Sachliche Zustaendigkeit Amtsgericht (§ 23 Nr. 1 GVG): bis 10.000 EUR (vorher 5.000 EUR).
- Berufungssumme (§ 511 Abs. 2 Nr. 1 ZPO): 1.000 EUR (vorher 600 EUR).
- Wertgrenze Nichtzulassungsbeschwerde (§ 26 EGZPO bzw. § 544 Abs. 2 Nr. 1 ZPO): 25.000 EUR (vorher 20.000 EUR).
- Uebergangsvorschrift: § 47 EGZPO. Massgeblich ist, ob die angegriffene Entscheidung bis 31.12.2025 verkuendet/zugestellt war oder die muendliche Verhandlung vorher geschlossen war.

Quellen:
- BRAK Mitteilung zur Wertgrenzenreform: https://www.brak.de/newsroom/news/zivilgerichtsbarkeit-hoehere-wertgrenzen-fuer-zustaendigkeit-und-rechtsmittel-ab-112026/
- Anwaltsblatt zur Praxis: https://anwaltsblatt.anwaltverein.de/de/themen/recht-gesetz/zustaendigkeitsstreitwert-2026
- § 47 EGZPO bei dejure: https://dejure.org/gesetze/EGZPO/47.html
- § 511 ZPO bei dejure: https://dejure.org/gesetze/ZPO/511.html

### Leitentscheidungen

- Streitwertbemessung bei Feststellungsantraegen neben Leistungsantraegen: kein Mehrwert, wenn Feststellungsantrag wirtschaftlich in Leistungsantrag aufgeht. Aktenzeichen vor Schriftsatzverwendung ueber https://dejure.org pruefen.
- Streitwertbemessung im Unterlassungsrechtsstreit: bei Kerntheorie-Reichweite ist der wirtschaftliche Wert des Verbots massgeblich, nicht nur der konkret angegriffene Verletzungsfall. Aktenzeichen ueber https://dejure.org und https://openjur.de verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Hauptforderung bestimmen** – Nennwert bei Leistungsklage; bei Feststellungsklage
 Abschlag von i. d. R. 20 % (Ermessen, vgl. § 3 ZPO).

2. **Nebenforderungen ausscheiden** – Zinsen, Früchte, Kosten des Verfahrens nach
 § 43 Abs. 1 GKG nicht mitrechnen, sofern Nebenforderungen.

3. **Hilfsanträge prüfen** – Kein Ansatz im Ausgangsverfahren (§ 45 Abs. 1 Satz 2
 GKG); bei Stattgabe des Hilfsantrags Mehrwert nach § 45 Abs. 1 Satz 3 GKG
 nachträglich festsetzen.

4. **Aufrechnung einbeziehen** – Widerklageforderung oder Aufrechnungsforderung erhöht
 Streitwert nach § 45 Abs. 3 GKG nur bis zur Klageforderungshöhe.

5. **Gerichtsgebühren berechnen** – Aus dem festgesetzten Streitwert die Gerichtsgebühr
 nach GKG Anlage 1 und 2 ermitteln (Tabelle §§ 34, 35 GKG).

6. **Anwaltsgebühren berechnen** – Gegenstandswert für Verfahrensgebühr (Nr. 3100 VV
 RVG), Terminsgebühr (Nr. 3104 VV RVG), Einigungsgebühr (Nr. 1000 VV RVG)
 aus der Vergütungstabelle (Anlage 2 RVG) ableiten.

7. **Kostenfestsetzungsantrag stellen** – Nach Vorliegen eines zur Zwangsvollstreckung
 geeigneten Kostentitels (§ 103 ZPO) Antrag nach § 104 ZPO beim Urkundsbeamten;
 Glaubhaftmachung der Auslagen durch Kostenrechnung und Belege.

8. **Streitwertbeschwerde** – Binnen 6 Monaten nach Rechtskraft (§ 68 Abs. 1 Satz 3
 GKG); beschwerdeberechtigt: Parteien und Staatskasse; Gericht, das die
 angegriffene Entscheidung erlassen hat, entscheidet zuerst (§ 68 Abs. 1
 Satz 1 GKG); dann ggf. Beschwerdegericht.

## Ausgabeformat

- **Streitwert-Memo** (Gutachtenstil): Struktur Hauptantrag → Hilfsanträge →
 Nebenforderungen → Ergebniswert; mit Norm- und Rspr.-Nachweisen.
- **Kostennote** (Tabelle): Gebührenart | Gegenstandswert | Gebührensatz
 (VV-Nr.) | Betrag | USt.; Gesamt.
- **Kostenfestsetzungsantrag** (Schriftsatz): Adressat Urkundsbeamter; Bezugnahme
 auf Kostentitel; Auflistung erstattungsfähiger Kosten; Unterschrift.

## Beispiel

*Sachverhalt:* Klägerin macht 80.000 € Schadensersatz geltend (Leistungsklage).
Hilfsantrag auf Feststellung künftiger Schadensersatzpflicht. Beklagte rechnet
mit einer Gegenforderung von 30.000 € auf.

*Streitwertberechnung (Urteilsstil):*

Der Streitwert beläuft sich auf 110.000 €. Die Leistungsklage hat einen Wert
von 80.000 € (§ 3 ZPO). Der Hilfsantrag bleibt nach § 45 Abs. 1 Satz 2 GKG
außer Betracht, da das Gericht über ihn nicht zu entscheiden hat, solange der
Hauptantrag Erfolg verspricht. Die Aufrechnung mit 30.000 € erhöht den
Streitwert gemäß § 45 Abs. 3 GKG um 30.000 €, da sie 80.000 € nicht übersteigt.
Zinsen auf die Klageforderung sind nach § 43 Abs. 1 GKG nicht anzusetzen.

Gerichtsgebühr (3,0-fach, § 34 GKG, Nr. 1210 KV GKG): aus einem Streitwert
von 110.000 € = 3 × 1.476 € = 4.428 €.

Anwaltsgebühren (Verfahrensgebühr 1,3 aus 110.000 € = 1,3 × 2.471 € = 3.212,30 €
zzgl. USt.) nach Nr. 3100 VV RVG i. V. m. Anlage 2 RVG.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
in: Hartmann, KostenG, 54. Aufl. 2024, § 45 GKG Rn. 18.)*

## Risiken und typische Fehler

- **Frist Streitwertbeschwerde:** § 68 Abs. 1 Satz 3 GKG – 6 Monate nach
 Rechtskraft der Hauptsacheentscheidung; Versäumnis führt zum Verlust des
 Rechtsbehelfs.
- **Hilfsantragsmehrwert:** Wird irrtümlich sofort angesetzt, obwohl das Gericht
 über ihn nicht entschieden hat – Fehler mit Kostennachforderungsrisiko.
- **Aufrechnung überschreitet Klageforderung:** § 45 Abs. 3 GKG begrenzt den
 Mehrwert auf die Klageforderungshöhe; Überschreitung wird nicht berücksichtigt.
- **Zinsen als Hauptforderung:** Sind Zinsen ausnahmsweise selbst Streitgegenstand
 (z. B. Zinsklage), sind sie streitwertrelevant – § 43 Abs. 1 GKG greift dann
 nicht.
- **Berufsrecht:** Fehlerhafte Gebührennoten können eine Pflichtverletzung
 (§ 43a BRAO) darstellen; Vergütungsvereinbarungen müssen § 3a RVG entsprechen.
- **Datenschutz:** Mandantenunterlagen dürfen nicht ohne Einwilligung in externe
 KI-Tools eingegeben werden (§ 43a Abs. 2 BRAO, § 203 StGB).
- **Keine KI-Garantie:** Gebührentabellen und Gegenstandswerte sind anhand der
 aktuellen GKG-Anlage und RVG-Anlage 2 manuell zu prüfen.

## Quellenpflicht

Jede Aussage zu Streitwert, Gebühren oder Kostenerstattung ist zu belegen nach
den Vorgaben in `references/zitierweise.md`. Gesetz vor Rechtsprechung vor
Kommentar. Bei streitiger Streitwertbemessung (z. B. Feststellungsabschlag)
h. M. und Gegenauffassung kenntlich machen. Tabellenwerte (GKG Anlage 2, RVG
Anlage 2) stets auf Aktualität prüfen – Gesetzesänderungen fließen nicht
automatisch ein.

## 2. `verkehrsunfall`

**Fokus:** Verkehrsunfall-Mandat im Zivilprozess vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz. Normen: §§ 7 18 StVG, §§ 823 253 BGB, § 115 VVG. Prüfraster: Haftungsquote, Schadensposten, Verjaebrung, Regulierungsablauf. Output: Klageschrift Verkehrsunfall oder Klageerwiderung. Abgrenzung: nicht Strafrecht oder Ordnungswidrigkeiten.

# Verkehrsunfall – Haftung, Schaden und Schadensausgleich

## Zweck

Dieser Skill begleitet die vollständige rechtliche Aufarbeitung eines Verkehrsunfalls:
Haftungsgrundlagen (§§ 7, 17, 18 StVG; § 823 BGB), Quotenbildung bei Mitverschulden,
Direktanspruch gegen den Haftpflichtversicherer (§ 115 VVG) und vollständige Schadensaufstellung
für Sachschäden sowie Personenschäden (Schmerzensgeld). Mandate reichen von der ersten Beratung
nach Unfall über die Regulierung mit dem Versicherer bis zur Klage.

## Eingaben

Das Modell benötigt:

1. **Unfallhergang**: Datum, Ort, beteiligte Fahrzeuge, Unfallablauf (eigene Darstellung;
 Polizeiprotokoll, soweit vorhanden)
2. **Fahrzeugdaten**: Hersteller, Typ, Erstzulassung, Laufleistung; aktueller Zeitwert
3. **Schäden**: Reparaturkostenvoranschlag oder Gutachten; Totalschadensfeststellung;
 Wertminderung; Abschlepp-, Gutachterkosten; Mietwagen oder Nutzungsausfallbegehren
4. **Personenschäden**: Verletzungsart, Behandlungsdauer, Attest; Arbeitsfähigkeitsverlust
5. **Versicherungsdaten**: Haftpflichtversicherer des Gegners; Schadennummer
6. **Mitverschulden**: Gibt es Hinweise auf ein Mitverschulden des Mandanten (Vorfahrt,
 Geschwindigkeit, Sicherheitsgurt)?

## Rechtlicher Rahmen

### Normen

- **§ 7 StVG** – Halterhaftung (Gefährdungshaftung; kein Verschuldensnachweis erforderlich;
 Entlastung nur bei höherer Gewalt § 7 Abs. 2 StVG oder unabwendbarem Ereignis § 17 Abs. 3 StVG)
- **§ 17 StVG** – Gesamtschuldnerausgleich zwischen Fahrzeughaltern; Abwägung der Verursachungs-
 und Verschuldensbeiträge (Betriebsgefahr + konkretes Verschulden)
- **§ 18 StVG** – Fahrerhaftung (Verschuldenshaftung; Beweislastumkehr: Fahrer muss fehlende
 Fahrlässigkeit beweisen)
- **§ 823 Abs. 1 BGB** – Deliktische Haftung (Leben, Körper, Gesundheit, Eigentum)
- **§ 253 Abs. 2 BGB** – Schmerzensgeld bei Körper- oder Gesundheitsverletzung
- **§ 115 Abs. 1 S. 1 Nr. 1 VVG** – Direktanspruch des Geschädigten gegen den KFZ-
 Haftpflichtversicherer (ohne Umweg über den Versicherungsnehmer)
- **§ 3 PflVG** – Pflichtversicherung; Bindungswirkung des Versicherungsschutzes
- **§ 249 BGB** – Naturalrestitution; Recht auf Reparatur oder Geldersatz
- **§ 251 BGB** – Wertersatz bei Unverhältnismäßigkeit der Herstellung
- **§ 254 BGB** – Mitverschulden (Quotenbildung); Schadensminderungsobliegenheit

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Der Geschädigte kann Reparaturkosten bis zu 130 % des Wiederbeschaffungswerts verlangen,
 wenn er das Fahrzeug tatsächlich repariert und es mindestens 6 Monate weiternutzt; maßgeblich
 ist das Integritätsinteresse.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 entschädigung; der Geschädigte hat Anspruch auf Nutzungsausfallentschädigung (nach Tabelle
 Sanden/Danner/Küppersbusch), sofern er auf das Fahrzeug angewiesen war; bloße Freizeitnutzung
 genügt nicht für Nutzungsausfall, wohl aber gewerbliche und Alltagsnutzung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 eine merkantile Wertminderung entsteht durch das Bekanntwerden eines Unfallschadens auch bei
 fachgerechter Reparatur; Berechnungsmethode Ruhkopf/Sahm.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Sicherung der Beweise** (unmittelbar nach Unfall): Fotos, Polizeiprotokoll, Zeugenangaben,
 Skizze; Sachverständigengutachten beauftragen (§ 249 BGB: Gutachterkosten erstattungsfähig).
2. **Haftungsanalyse** (§§ 7, 17, 18 StVG):
 - Grundhaftung aus § 7 StVG (Gefährdungshaftung, kein Verschulden nötig)
 - Mitverschuldensprüfung § 17 StVG + § 254 BGB: Betriebsgefahr + konkretes Fehlverhalten
 - Quotenbildung: z. B. Auffahrunfall ohne erkennbaren Grund → volle Haftung des Auffahrenden;
 mit Mitverschulden (Abruptes Bremsen ohne Grund) → Quote.
3. **Direktanspruch** (§ 115 VVG): Schreiben an gegnerischen Versicherer mit Schadensnummer;
 Frist 3 Monate für Stellungnahme (§ 17 Abs. 1 PflVG).
4. **Schadensaufstellung**:
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 bei Totalschaden: Wiederbeschaffungswert abzügl. Restwert
 b. *Wertminderung*: Methode Ruhkopf/Sahm; merkantil nur bei jungen Fahrzeugen sinnvoll
 c. *Nutzungsausfall oder Mietwagen*: Tabelle Sanden/Danner/Küppersbusch; oder konkrete
 Mietwagenkosten (erforderliche Klasse)
 d. *Abschleppkosten, Gutachterkosten, Unkostenpauschale* (EUR 25–30, h. M.)
 e. *Personenschaden*: Behandlungskosten, Verdienstausfall, Haushaltsführungsschaden
5. **Schmerzensgeld** (§ 253 Abs. 2 BGB): Verletzungsdokumentation; Orientierung an
 Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
 Genugtuungsfunktion.
6. **Verhandlung mit Versicherer**: Anspruchsschreiben mit vollständiger Aufstellung; Fristsetzung
 2–4 Wochen; ggf. Mahnung (§ 286 BGB) für Verzugszinsen.
7. **Klage** beim zuständigen AG/LG: bei Ablehnung oder unzureichendem Angebot; Prozesskostenhilfe
 für einkommenschwache Mandanten prüfen.

## Ausgabeformat

- **Regulierungsschreiben** an Versicherer (vollständige Schadensaufstellung, Fristsetzung)
- **Schadenstabelle** (Excel/Tabelle: Schadensposten, Betrag, Dokumentation, Quotierung)
- **Rechtliches Memo** zur Haftungsquote und 130%-Grenze
- **Klageschrift** bei Scheitern der außergerichtlichen Regulierung

## Beispiel

**Sachverhalt**: Mandant M (Halter, Fahrer) wird beim Abbiegen von Fahrzeug G angefahren.
Reparaturkosten laut Gutachten EUR 8.200; Wiederbeschaffungswert EUR 7.500; Fahrzeug ist 2 Jahre alt.
M war 2 Tage arbeitsunfähig; Halswirbelverletzung.

**Prüfung (Gutachtenstil)**:

*Haftungsgrundlage*: G haftet als Halter nach § 7 Abs. 1 StVG aus Betriebsgefahr; als Fahrer
nach § 18 Abs. 1 StVG (Verschulden wird vermutet; G kann sich nicht entlasten). M selbst haftet
nach § 7 StVG ebenfalls aus Betriebsgefahr; eine konkrete Verkehrspflichtverletzung ist nicht
nachgewiesen → Haftungsquote 100 % G (vorbehaltlich genauer Unfallrekonstruktion).

*130%-Grenze (§ 249 BGB)*: Reparaturkosten EUR 8.200 = 109 % des WBW (EUR 7.500). Unter der
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
wirtschaftlich vertretbar; M kann Reparaturkostenersatz verlangen.

Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
Attest.

## Risiken und typische Fehler

- **130%-Grenze nicht beachtet**: Mandant lässt Fahrzeug für EUR 10.000 reparieren bei WBW
 EUR 7.000 (143 %) → nur WBW minus Restwert erstattungsfähig; Mandant trägt Differenz.
- **Restwert zu niedrig ausgewiesen**: Gegnerversicherer kann höheren Restwert durch Aufkäufer
 nachweisen; Beweislast bei Versicherer, aber Mandant kann sich nicht blind auf Gutachten
 verlassen.
- **Mitverschulden übersehen** (§ 254 BGB): Mandant nicht angeschnallt, Mitschuld an Verletzung;
 Schmerzensgeld- und Schadensersatzkürzung.
- **Nutzungsausfall ohne Nahraumnahme**: Kein Anspruch, wenn Mandant kein Bedürfnis nach
 Nutzung hatte (Zweitfahrzeug vorhanden).
- **Verjährung**: 3 Jahre ab Kenntnis (§ 195, § 199 BGB); spätestens 10 Jahre absolut; kein
 Hemmungstatbestand → Klage oder Mahnbescheid rechtzeitig.
- **Berufsrecht**: Medizinische Unterlagen (Atteste) unterliegen § 203 StGB; nur in gesicherter
 Umgebung bearbeiten; Honorarrecht RVG beachten.

## Quellenpflicht

Jede Aussage zur Haftungsquote, 130%-Grenze, Nutzungsausfall und Schmerzensgeldbemessung ist
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
Beck'sche Tabelle) als eigenständige Quellen mit Auflage und Jahr zitieren.

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 184/10 (NJW 2011, 3237) – WRONG_TOPIC; tatsächlich: Schadensersatz Gemeinde aus Gefährdungshaftung für Ölspurbeseitigung (StVG), nicht Direktanspruch § 115 VVG. Fundstelle: NVwZ-RR 2011, 925 (nicht NJW 2011, 3237).
Maßnahme: Ersetzt durch BGH VI ZR 226/16, 14.03.2017, NJW 2017, 2271 (§ 115 Abs. 2 S. 3 VVG, Direktanspruch, verifiziert auf dejure.org).
Quelle: https://dejure.org/2011,636
-->

## 3. `vollstreckung`

**Fokus:** Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: §§ 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: Vollstreckungsauftrag und Pfaendungsbeschluss-Antrag. Abgrenzung: nicht AnfG-Anfechtung.

# Zwangsvollstreckung – Überblick und Praxis

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Dieser Skill bleibt der prozessrechtliche Überblick. Für die operative Durchführung – Antragsformulare,
Drittschuldnerwahl, P-Konto-Berechnung, ZVollstrDigitG-Übergänge 2026/2027, notarielle Urkunde § 800 ZPO,
Tabellenauszug § 201 InsO, Räumung § 885 ZPO, Schuldnerschutz – lädt das freistehende Plugin
`zwangsvollstreckung` mit 17 spezialisierten Skills (`zv-kommandocenter`, `zv-titel-klausel-zustellung`,
`zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-pfueb-mieter-finanzamt`, `zv-vermoegensauskunft-gv`,
`zv-kontensuche-drittschuldner`, `zv-notarielle-urkunde-grundschuld`, `zv-zvg-antrag-glaeubiger`,
`zv-tabellenauszug-201-inso`, `zv-mobiliar-gv-auftrag`, `zv-raeumung-885`, `zv-abwehr-schuldner`,
`zv-pfaendungstabelle-2025`, `zv-elektronische-zustellung-2027`, `zv-mahnbescheid-online`,
`zv-vollstreckungsbescheid-folge`). Dieser Hub-Skill ist die richtige Adresse für die dogmatische
Gesamtschau; das Plugin ist die richtige Adresse für die einzelne Vollstreckungsmaßnahme.

## Zweck

Dieser Skill begleitet die Durchführung der Zwangsvollstreckung aus Urteilen, Beschlüssen,
Vollstreckungsbescheiden, notariellen Urkunden und anderen Titeln. Er deckt alle wesentlichen
Vollstreckungsarten ab: Mobiliarvollstreckung (Pfändung körperlicher Sachen), Geldvollstreckung
in Forderungen (PfÜB), Immobiliarvollstreckung (ZVG), Vermögensauskunft, Räumungsvollstreckung
und Herausgabevollstreckung. Auf der Schuldnerseite: Abwehr rechtswidriger Vollstreckung,
Vollstreckungsgegenklage, Drittwiderspruchsklage.

## Eingaben

Das Modell benötigt:

1. **Vollstreckungstitel**: Art (Urteil, Beschluss, VB, notarielle Urkunde, Vergleich),
 Datum, Gericht/Notar, Rechtskraft/Vollstreckbarkeit
2. **Vollstreckungsklausel**: Liegt eine vollstreckbare Ausfertigung vor? (§ 724 ZPO)
3. **Zustellung**: Wurde der Titel dem Schuldner zugestellt? (§ 750 ZPO – Voraussetzung!)
4. **Vollstreckungsgegenstand**: Geld/Mobilien/Forderungen/Immobilie/Herausgabe/Räumung
5. **Bekannte Vermögenswerte**: Kontonummern, Arbeitgeber, Grundstücke, Kfz
6. **Schuldnersituation**: Privatperson oder Unternehmen; Pfändungsfreigrenzen beachten

## Rechtlicher Rahmen

### Normen

- **§§ 704–707 ZPO** – Vollstreckungstitel und allgemeine Voraussetzungen (Titel, Klausel,
 Zustellung = "drei Säulen")
- **§ 724 ZPO** – vollstreckbare Ausfertigung (Klausel); § 725 ZPO – Klauselerteilung durch
 Urkundsbeamten; § 732 ZPO – Erinnerung gegen Klauselerteilung
- **§ 750 ZPO** – Zustellungserfordernis vor Beginn der Vollstreckung
- **§ 767 ZPO** – Vollstreckungsgegenklage (materielle Einwendungen gegen den Anspruch selbst)
- **§ 771 ZPO** – Drittwiderspruchsklage (Eigentum oder Recht eines Dritten an Vollstreckungs-
 gegenstand)
- **§ 802a–802l ZPO** – Vermögensauskunft (§ 802c: Abgabe durch Schuldner; § 802d: Sperrfrist
 2 Jahre; § 802l: Abruf beim Gerichtsvollzieher aus Schuldnerverzeichnis)
- **§ 808 ZPO** – Pfändung körperlicher Sachen (Mobiliarpfändung durch GV; Gewahrsam des
 Schuldners; Pfändungsprotokoll)
- **§§ 811, 811c ZPO** – Unpfändbare Sachen (Hausrat, Arbeitsgeräte, Sozialgeräte)
- **§ 829 ZPO** – Forderungspfändung (Pfändungs- und Überweisungsbeschluss = PfÜB; Beschluss
 durch Vollstreckungsgericht; Zustellung an Drittschuldner und Schuldner)
- **§§ 850–850k ZPO** – Pfändungsschutz für Arbeitseinkommen und P-Konto (§ 850c ZPO –
 Pfändungstabelle; § 850k ZPO – Pfändungsschutzkonto)
- **§ 883 ZPO** – Herausgabevollstreckung beweglicher Sachen
- **§ 885 ZPO** – Räumungsvollstreckung (durch GV; Androhung 3 Wochen vor Termin)
- **ZVG** – Zwangsversteigerung und Zwangsverwaltung von Grundstücken (§§ 15 ff. ZVG
 Antrag beim AG; §§ 35 ff. ZVG Versteigerungstermin)
- **§§ 900–915h ZPO** – Insolvenzantrag als ultima ratio; § 17 InsO – Zahlungsunfähigkeit

### Leitentscheidungen und Normfassungen

- BGH VII. ZS Linie zur Klauselpruefung: Die Pruefungstiefe im Klauselerteilungsverfahren ist formal eng begrenzt; materielle Einwendungen sind im Wege der Vollstreckungsgegenklage (§ 767 ZPO) oder Erinnerung (§ 766 ZPO) geltend zu machen. Aktuelle Aktenzeichen (z.B. BGH, Beschl. v. 30.01.2025 – Az. VII ZB 10/24) vor Verwendung ueber https://www.bundesgerichtshof.de und https://dejure.org verifizieren.
- BGH-Linie zu § 850k ZPO P-Konto-Schutz: Pfaendungsschutz wirkt automatisch gegenueber dem Glaeubiger; nachtraegliche Aufhebung erfordert gesonderten Antrag. Aktenzeichen vor Schriftsatzverwendung pruefen.
- Vollstreckungsvoraussetzung § 750 ZPO: Vollstreckungsmassnahmen ohne vorherige Zustellung sind rechtswidrig und auf Erinnerung hin aufzuheben (staendige Rechtsprechung).

### Rechtsstand 2025/2026

- Pfaendungsfreigrenzenbekanntmachung 2025 (BGBl. 2025 I Nr. 110): Grundfreibetrag 1.555 EUR ab 01.07.2025 bis 30.06.2026. Quelle: https://www.recht.bund.de/bgbl/1/2025/110/VO.html
- Justizstandort-Staerkungsgesetz (BGBl. 2025 I Nr. 318 vom 11.12.2025): Wertgrenzenreform ab 01.01.2026 mit Auswirkungen auf Beschwerdesummen § 511 Abs. 2 ZPO (jetzt 1.000 EUR) und § 23 GVG (AG 10.000 EUR).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### A. Geldvollstreckung – Mobiliarpfändung (§ 808 ZPO)

1. **Voraussetzungen prüfen**: Titel + Klausel + Zustellung; Wartefrist § 750 Abs. 1 ZPO
 (i. d. R. 2 Wochen nach Zustellung)
2. **GV beauftragen**: Vollstreckungsauftrag an Gerichtsvollzieher; Angabe bekannter Vermögens-
 werte; ggf. Auftrag zur Vermögensauskunft kombinieren
3. **Pfändung**: GV pfändet körperliche Sachen im Gewahrsam des Schuldners; Unpfändbarkeit
 §§ 811 ff. ZPO beachten; Pfändungsprotokoll ausstellen

### B. Forderungspfändung – PfÜB (§§ 829, 835 ZPO)

1. **Antrag beim Vollstreckungsgericht** (AG am Wohnsitz des Schuldners): Bezeichnung von
 Forderung und Drittschuldner (Bank, Arbeitgeber, Mieter)
2. **Erlass des PfÜB**: Gericht prüft nur formal → PfÜB wird erlassen
3. **Zustellung**: Zunächst an Drittschuldner (Pfändungswirkung), dann an Schuldner
4. **Drittschuldnererklärung** § 840 ZPO: Drittschuldner muss binnen 2 Wochen Auskunft geben
5. **Überweisung** § 835 ZPO: zur Einziehung oder an Zahlungs Statt

### C. Vermögensauskunft (§ 802c ZPO)

1. **Antrag beim GV**: wenn Vollstreckung erfolglos; GV lädt Schuldner vor
2. **Abgabe der Vermögensauskunft** unter Versicherung der Vollständigkeit (§ 802c Abs. 3 ZPO)
3. **Eintragung ins Schuldnerverzeichnis** § 882c ZPO bei Verweigerung oder Verletzung

### D. Räumungsvollstreckung (§ 885 ZPO)

1. **Titel**: rechtskräftiges Räumungsurteil oder vorläufig vollstreckbares Urteil mit
 Sicherheitsleistung
2. **Androhung**: GV setzt Termin (mind. 3 Wochen Vorlauf, § 885 Abs. 1 ZPO)
3. **Durchführung**: GV räumt; Hab und Gut des Schuldners wird eingelagert oder bei Wertlosigkeit
 vernichtet

## Ausgabeformat

- **PfÜB-Antragsentwurf** (vollständig für das Vollstreckungsgericht)
- **Rechtliches Memo** zu Vollstreckungsvoraussetzungen und Pfändungsschutz
- **Checkliste** (Titel/Klausel/Zustellung; Pfändungsschutz; Drittschuldner)
- **Muster-Vermögensauskunfts-Aufforderung** für außergerichtliche Nutzung

## Beispiel

**Sachverhalt**: Gläubigerin G hat ein rechtskräftiges Urteil gegen Schuldner S über EUR 12.000
(inkl. Zinsen). S ist Arbeitnehmer bei der Musterfirma GmbH; sein Nettolohn beträgt EUR 2.400/Monat.

**Prüfung (Urteilsstil)**:

*Voraussetzungen*: Titel (Urteil), vollstreckbare Ausfertigung (§ 724 ZPO), Zustellung an S
liegt vor (§ 750 ZPO). Vollstreckung ist zulässig.

*Forderungspfändung Arbeitseinkommen (§§ 829, 850 ff. ZPO)*: Pfändbar ist das Arbeitseinkommen
oberhalb des Pfändungsfreibetrags (§ 850c ZPO; bei Nettolohn EUR 2.400/Monat ohne Unterhaltspflichten
ca. EUR 264/Monat pfändbar nach aktueller Pfändungstabelle). PfÜB ist beim Vollstreckungsgericht
am Wohnsitz des S zu beantragen; Drittschuldnerin ist die Musterfirma GmbH.

*Empfehlung*: Zusätzlich Kontopfändung bei bekannter Hausbank (§ 829 ZPO); Cave: P-Konto-
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken und typische Fehler

- **Fehlende Zustellung** (§ 750 ZPO): Vollstreckung rechtswidrig; Erinnerung § 766 ZPO
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **P-Konto übersehen**: Pfändung auf Girokonto leer, wenn Schuldner P-Konto führt;
 Freibeträge sind automatisch geschützt (§ 850k ZPO).
- **Falsche Pfändungsfreigrenze**: Bei Unterhaltspflichten des Schuldners erhöhte Freigrenze
 (§ 850c Abs. 2 ZPO); Überpfändung macht Gläubiger schadensersatzpflichtig.
- **Drittwiderspruchsklage** § 771 ZPO: Gepfändeter Gegenstand gehört Dritten → Klage suspendiert
 Vollstreckung; materiell-rechtliches Eigentum des Dritten prüfen.
- **Vollstreckungsgegenklage** § 767 ZPO: Schuldner hat nach Titelerlass erfüllenden Umstand
 (Zahlung, Aufrechnung, Stundung) → Klage beim Prozessgericht.
- **Berufsrecht**: Vollstreckungsaufträge mit Vermögensdaten des Schuldners unterliegen
 § 43a Abs. 2 BRAO, § 203 StGB.

## Quellenpflicht

Jede Aussage zu Vollstreckungsvoraussetzungen, Pfändungsfreigrenzen und Rechtsbehelfen ist
nach `references/zitierweise.md` zu belegen. BGH-Beschlüsse vollständig mit Datum, Az.,
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Stöber/Rellermeyer) Autoren, Titel, Aufl., Jahr, Rn. zitieren.

<!-- AUDIT 27.05.2026
Datum 01.07.2010 (nicht 20.05.2010), aber mit falschem Thema: real handelt das Urteil von
Vorteilsausgleichung/Steuervorteile, nicht von Drittwiderspruchsklage § 771 ZPO (WRONG_TOPIC).
Halluzinierte Referenz geloescht. Keine Ersatzquelle fuer § 771 ZPO-Leitentscheidung ergaenzt.
-->
