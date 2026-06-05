---
name: verkehrsplanung-verkehrswende
description: "Verkehrsplanung Verkehrswende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verkehrsplanung Verkehrswende

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verkehrsplanung Verkehrswende** im Plugin Verkehr-/Infrastrukturrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehr-infrastrukturrecht-verkehrsplanung` | Verkehrsplanung rechtlich begleiten: Kommune oder Verband plant Strassen- oder Radverkehrs-Massnahme und muss Beteiligung und Beschluss vorbereiten. Normen: § 45 StVO (Verkehrsanordnungen), FStrG, StrWG (Landesrecht), ROG §§ 4 ff. (Raumordnung), BauGB §§ 1 ff. (Bauleitplanung), UVPG. Prüfraster: Varianten, Betroffenheiten, Beteiligungsverfahren, Beschluss-Begründung, Abwaegungsgebot. Output Projektfahrplan, Begründungsbausteine, Beteiligungsunterlagen. Abgrenzung: Planfeststellung siehe verkehr-infrastrukturrecht-planfeststellung; Verkehrswende siehe verkehr-infrastrukturrecht-verkehrswende. |
| `verkehr-infrastrukturrecht-verkehrswende` | Verkehrswende-Massnahmen rechtssicher gestalten: Kommune plant Fussgaengerzone, Tempo-30-Zone oder Radverkehrs-Foerderung. Normen: § 45 Abs. 1 StVO (Fussgaengerzone, Tempo-30), ERA 2010 (Empfehlungen Radverkehr), VwGO (Anfechtbarkeit durch Kfz-Nutzer). Prüfraster: Rechtsgrundlage Verkehrsanordnung, Verhältnismäßigkeit, Anfechtungsrisiken durch Anwohner/Gewerbetreibende, Beteiligung. Output Rechtsgutachten zur Massnahme, Begründungsbausteine für Beschluss. Abgrenzung: Allgemeine Verkehrsplanung siehe verkehr-infrastrukturrecht-verkehrsplanung; Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung. |
| `verkehr-infrastrukturrecht-wirtschaftsverkehr` | Wirtschaftsverkehr und Lieferverkehr in der Stadt rechtlich gestalten: Logistikunternehmen oder Kommune plant Lieferzonen, Beschilderung oder Ausnahmegenehmigungen. Normen: § 12 StVO (Haltverbot), § 45 StVO (Sonderregelungen), § 46 StVO (Ausnahmegenehmigungen), VwV-StVO (Ladezonen). Prüfraster: Lieferflaechen, Ladezonen, Logistikkonzepte, Anliegerrechte, Ausnahmegenehmigungen. Output Rechts-Memo Ausnahmegenehmigung, Lieferflaechen-Konzept-Prüfung. Abgrenzung: Sondernutzung siehe verkehr-infrastrukturrecht-sondernutzung; Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung. |

## Arbeitsweg

Im Plugin Verkehr-/Infrastrukturrecht gilt für **Verkehrsplanung Verkehrswende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehr-infrastrukturrecht-verkehrsplanung`

**Fokus:** Verkehrsplanung rechtlich begleiten: Kommune oder Verband plant Strassen- oder Radverkehrs-Massnahme und muss Beteiligung und Beschluss vorbereiten. Normen: § 45 StVO (Verkehrsanordnungen), FStrG, StrWG (Landesrecht), ROG §§ 4 ff. (Raumordnung), BauGB §§ 1 ff. (Bauleitplanung), UVPG. Prüfraster: Varianten, Betroffenheiten, Beteiligungsverfahren, Beschluss-Begründung, Abwaegungsgebot. Output Projektfahrplan, Begründungsbausteine, Beteiligungsunterlagen. Abgrenzung: Planfeststellung siehe verkehr-infrastrukturrecht-planfeststellung; Verkehrswende siehe verkehr-infrastrukturrecht-verkehrswende.

# Verkehrsplanung und Projektstrategie

## Triage zu Beginn — klaere zuerst

1. Wer ist Mandant: oeffentlicher Trager, Investor, Anlieger, Verband oder Bürgerinitiative?
2. Welche Planungsstufe: informelle Konzeption, Ratsvorlage, Bauleitplanung oder Planfeststellung?
3. Gibt es eine UVP-Pflicht (Anlage 1 UVPG, § 5 UVPG)?
4. Welche Fristen gelten: Auslegungsfrist, Einwendungsfrist, Ratsbeschluss?
5. Liegt ein Raumordnungsverfahren (§ 15 ROG) vor?
6. Welche Eigentumsrechte und Laermschutzansprueche sind betroffen?

## Zentrale Normen

- § 45 StVO — Anordnungsbefugnis und Ermessen der Strassenverkehrsbehoerde
- § 1 FStrG — Widmung Bundesfernstrassen; Strassenrecht der Laender (z.B. StrWG NRW)
- §§ 1-5 BauGB — Bauleitplanung, Abwaegungsgebot, Entwicklungsgebot
- § 214 BauGB — beachtliche Verfahrensfehler im Bauleitplanverfahren
- § 15 ROG — Raumordnungsverfahren bei raumbedeutsamen Massnahmen
- § 5 UVPG, Anlage 1 UVPG — UVP-Pflicht bei Strassenbauvorhaben
- Art. 14 GG — Eigentumsgarantie; Enteignung nur gegen Entschaedigung (Art. 14 III GG)
- § 74 VwVfG — Planfeststellungsbeschluss als rechtsgestaltender Verwaltungsakt

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Projekttyp bestimmen:** informelle Planung, Bauleitplanung (FNP/B-Plan) oder Planfeststellung (§ 74 VwVfG)
2. **UVP-Screening:** Anlage 1 UVPG pruefen; ggf. allgemeine Vorpruefung (§ 7 UVPG) veranlassen
3. **Raumordnungsverfahren:** § 15 ROG — ist Vorhaben raumbedeutsam? ROV-Pflicht abklaeren
4. **Bauleitplanung wenn noetig:** FNP-Aenderung, B-Plan-Aufstellung; Beteiligung nach §§ 3, 4 BauGB
5. **Betroffenheitsanalyse:** Eigentumsrechte (Art. 14 GG), Laerm (16. BImSchV), Naturschutz (BNatSchG)
6. **Unterlagen zusammenstellen:** Erlaeuterungsbericht, Lageplan, Querschnitte, Laermprognose, UVP-Bericht
7. **Beteiligungsverfahren durchfuehren:** Auslegung nach § 73 VwVfG (4 Wochen); Einwendungen erfassen
8. **Einwendungen aufbereiten:** sortieren, rechtlich bewerten, Erwidernde formulieren
9. **Planfeststellungsbeschluss pruefen:** Abwaegungsfehler, Nebenbestimmungen, Auflagen
10. **Klagemoglichkeiten nach Beschluss:** Anfechtung beim OVG (§ 48 VwGO); Klagefrist 1 Monat

## Entscheidungsbaum Planungsverfahren

```
Vorhaben geplant
 |
Raumbedeutsam? (§ 15 ROG)
 Ja ──→ Raumordnungsverfahren ──→ Landesplanungsbehoerde
 Nein ──→ weiter
 |
UVP-pflichtig? (Anlage 1 UVPG)
 Ja ──→ UVP einbeziehen (§§ 18-25 UVPG)
 Nein/Vorpruefung ──→ weiter
 |
Strassenneu- oder -ausbau?
 Bundesfernstrasse ──→ Planfeststellung nach FStrG, Planfeststellungsbehoerde beim Fernstrassenamt
 Landesstrasse / kommunal ──→ Planfeststellung nach LandesStrG oder B-Plan-Verfahren (BauGB)
 |
Planfeststellungsbeschluss ergeht
 |
Klagemoglichkeit: OVG (§ 48 VwGO) binnen 1 Monat
```

## Output-Template Einwendungsschreiben

**Adressat:** Planfeststellungsbehoerde — Tonfall: sachlich-juristisch, rechtswahrend

```
[KANZLEI], [ADRESSE] [ORT], [DATUM]

An die [PLANFESTSTELLUNGSBEHOERDE]
[ADRESSE]

Einwendungen im Planfeststellungsverfahren
[VORHABENBEZEICHNUNG]

Mandant/in: [NAME], [ADRESSE], Eigentuemet/in Flur [X] Parzelle [Y]

Sehr geehrte Damen und Herren,

namens unseres Mandanten/unserer Mandantin erheben wir folgende Einwendungen
gegen die ausgelegten Planunterlagen:

1. Eigentumsbetroffenheit (Art. 14 GG)
 Das Vorhaben erfordert die dauerhafte Inanspruchnahme von [X] m² Grund-
 stuecksflaeche. Eine Enteignungsvoraussetzung (Art. 14 III GG, § 19 FStrG)
 liegt mangels Entschaedigungsangebot noch nicht vor. [...]

2. Laermbetroffenheit (16. BImSchV)
 Die vorgelegte Laermprognose unterschreitet die Schwellenwerte der 16. BImSchV
 nicht. Unsere Messung ergibt [X] dB(A) tags / [X] dB(A) nachts. [...]

3. Abwaegungsdefizit
 Die Trassenvariante [X] wurde nicht ausreichend untersucht. [...]

Wir beantragen:
- Volle Entschaedigung nach §§ 19 ff. FStrG
- Laermschutzauflagen (aktiv: Laermschutzwall; passiv: Schallschutzfenster)
- Erneute Variantenabwaegung

[UNTERSCHRIFT]
```

## Harte Leitplanken

- Einwendungsfrist (§ 73 IV VwVfG) unbedingt wahren — spaetere Praeklusion (§ 73 IV 3 VwVfG)
- UVP-Pflicht immer vorschalten — Fehler ist absoluter Verfahrensfehler
- Abwaegungsgebot (§ 1 VII BauGB, § 74 VwVfG) muss alle Belange erfassen
- Keine Trassenfestlegung ohne Variantenvergleich
- Naturschutzrechtliche Eingriffsregelung (§§ 14 ff. BNatSchG) beachten

## 2. `verkehr-infrastrukturrecht-verkehrswende`

**Fokus:** Verkehrswende-Massnahmen rechtssicher gestalten: Kommune plant Fussgaengerzone, Tempo-30-Zone oder Radverkehrs-Foerderung. Normen: § 45 Abs. 1 StVO (Fussgaengerzone, Tempo-30), ERA 2010 (Empfehlungen Radverkehr), VwGO (Anfechtbarkeit durch Kfz-Nutzer). Prüfraster: Rechtsgrundlage Verkehrsanordnung, Verhältnismäßigkeit, Anfechtungsrisiken durch Anwohner/Gewerbetreibende, Beteiligung. Output Rechtsgutachten zur Massnahme, Begründungsbausteine für Beschluss. Abgrenzung: Allgemeine Verkehrsplanung siehe verkehr-infrastrukturrecht-verkehrsplanung; Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung.

# Verkehrswende und Verkehrsberuhigung — Rechtliche Umsetzung

## Triage zu Beginn — klaere zuerst

1. Welche Massnahme steht im Fokus: Tempo 30, Fussgaengerzone, Radstreifen, Lieferzone, Einbahnstrasse?
2. Wer ist Mandant: Gemeinde/Strassenverkehrsbehoerde, Anlieger, Gewerbetreibender, Verband?
3. Gibt es einen anfechtenden Dritten (z.B. Anlieger gegen Tempo-30)?
4. Ist die Massnahme verkehrsrechtlich (StVO) oder planerisch (B-Plan, Widmungsaenderung)?
5. Welche wirtschaftlichen Interessen sind betroffen (Erreichbarkeit, Lieferfrequenz)?
6. Bestehen laermschutzrechtliche oder behindertenrechtliche Anforderungen?

## Zentrale Normen

- § 45 I StVO — allgemeine Anordnungsbefugnis der Strassenverkehrsbehoerde
- § 45 I b Nr. 5 StVO — Tempo-30-Zone aus Gruenden des Laermschutzes
- § 45 I b Nr. 6 StVO — Tempo-30 vor Schulen, Kindergaerten, Senioreneinrichtungen
- § 45 I c StVO — Laermaktionsplan der Gemeinde als Grundlage
- Zeichen 250, 253, 260, 325, 326 StVO-Anlagen — Verkehrsverbote und Sondernutzung
- VwV-StVO zu § 45 — Ermessensrichtlinien, Anordnungsvoraussetzungen
- § 8 StVO — Vorfahrtregelung bei Verkehrsberuhigung
- STVO-Bussgeldkatalog — Sanktionen bei Verstoss

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Massnahme qualifizieren:** reine Verkehrszeichen-Anordnung (§ 45 StVO) oder Strassenplanung (BauGB/StrWG)?
2. **Rechtsgrundlage bestimmen:** welche Ziffer des § 45 I, I b oder I c StVO greift?
3. **Begruendung dokumentieren:** Laermgutachten, Unfallstatistik, Schulwegplaene, Laermaktionsplan
4. **Verhaeltnismaessigkeit pruefen:** milderes Mittel vorhanden (Geschwindigkeitsdaempfer statt Vollsperrung)?
5. **Betroffene Belange erfassen:** Anlieger, Gewerbe, OEPNV, Lieferverkehr, Feuerwehr/Rettungsdienste
6. **Sondernutzungsregelung treffen:** Lieferzeitfenster, Ausnahmegenehmigungen (§ 46 StVO)
7. **Beschilderung konzipieren:** VwV-StVO Zeichen- und Aufstellungsanforderungen
8. **Evaluation planen:** Verkehrszaehlung vor/nach, Laermmessung, Beschwerdemanagement
9. **Anfechtungsrisiko einschaetzen:** Widerspruch durch Anlieger oder Gewerbetreibende wahrscheinlich?

## Entscheidungsbaum Massnahmentyp

```
Verkehrsberuhigung geplant
 |
Flaeche: oeffentliche Strasse?
 Nein ──→ privatrechtliche Regelung (Grundstueckseigentuemer)
 Ja ──→ weiter
 |
Anordnung per Verkehrszeichen (§ 45 StVO)?
 Ja ──→ Strassenverkehrsbehoerde; keine Planfeststellung
 Nein (Umbau Fahrbahn) ──→ ggf. StrWG-Widmungsaenderung oder B-Plan
 |
Begruendung ausreichend?
 Laerm/Unfall nachgewiesen ──→ Anordnung tragfaehig
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 |
Ausnahmen noetig?
 Lieferverkehr ──→ zeitliche Freigabe + Zeichen 1026-37
 Anlieger ──→ Sondergenehmigung § 46 StVO
```

## Output-Template Anordnung / Bescheid

**Adressat:** Strassenverkehrsbehoerde intern oder an Anlieger — Tonfall: behoerdlich-begruendend

```
[BEHOERDE]
[ADRESSE]

Verkehrsrechtliche Anordnung nach § 45 I b Nr. 5 StVO

Aktenzeichen: [AZ]

Betreff: Einrichtung Tempo-30-Zone [STRASSENBEZEICHNUNG]

Aufgrund § 45 I b Nr. 5 StVO wird fuer den Streckenabschnitt [VON] bis [BIS]
eine Tempo-30-Zone (Zeichen 274.1 StVO) angeordnet.

Begruendung:
Gemaess dem Laermaktionsplan der Stadt [ORT] vom [DATUM] werden an dem genannten
Streckenabschnitt Laermwerte von [X] dB(A) tags gemessen, die den Richtwert der
16. BImSchV von 59 dB(A) tags uebersteigen. Die Anordnung ist das mildeste Mittel
zur nachhaltigen Laermreduzierung.

Ausnahme (§ 46 StVO): Lieferverkehr werktags 06:00-10:00 Uhr gestattet.

Rechtsbehelfsbelehrung: Gegen diese Anordnung kann binnen eines Monats nach
Bekanntgabe Widerspruch eingelegt werden.

[UNTERSCHRIFT BEHOERDE]
```

## Harte Leitplanken

- Tempo-30 braucht konkrete Begruendung (Laerm/Unfall) — politischer Wille allein reicht nicht
- Verhaeltnismaessigkeit: stets pruefen ob milderes Mittel ausreicht
- Lieferverkehr nie vollstaendig ausschliessen — wirtschaftliche Grundversorgung sichern
- Ausnahmegenehmigungen (§ 46 StVO) fuer Anlieger mit Behinderung / Gewerbe einplanen
- Anfechtungsrecht der Anlieger bei Vollsperrungen: Eilrechtsschutz § 80 V VwGO wahrscheinlich

## 3. `verkehr-infrastrukturrecht-wirtschaftsverkehr`

**Fokus:** Wirtschaftsverkehr und Lieferverkehr in der Stadt rechtlich gestalten: Logistikunternehmen oder Kommune plant Lieferzonen, Beschilderung oder Ausnahmegenehmigungen. Normen: § 12 StVO (Haltverbot), § 45 StVO (Sonderregelungen), § 46 StVO (Ausnahmegenehmigungen), VwV-StVO (Ladezonen). Prüfraster: Lieferflaechen, Ladezonen, Logistikkonzepte, Anliegerrechte, Ausnahmegenehmigungen. Output Rechts-Memo Ausnahmegenehmigung, Lieferflaechen-Konzept-Prüfung. Abgrenzung: Sondernutzung siehe verkehr-infrastrukturrecht-sondernutzung; Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung.

# Wirtschaftsverkehr — Liefer- und Ladezonen, Logistikrecht

## Triage zu Beginn — klaere zuerst

1. Wer ist Mandant: Gewerbetreibender mit Lieferproblemen, Gemeinde mit Logistikkonzept, Spediteur?
2. Geht es um Einrichtung neuer Ladezonen oder Anfechtung bestehender Beschraenkungen?
3. Welcher Strassentyp: Fussgaengerzone, eingeschraenktes Halteverbot, Lieferzone (Zeichen 286)?
4. Gibt es eine aktuelle Sondernutzungsgenehmigung oder nur informelle Duldung?
5. Wirken sich OEPNV-Trassen, Radwege oder Laermschutz auf den Lieferbereich aus?
6. Zeitfenster erwuenscht oder ganztaegige Regelung?

## Zentrale Normen

- § 12 StVO — Haltverbot; absolute und eingeschraenkte Haltverbotszonen
- § 45 I StVO — Anordnungsbefugnis Strassenverkehrsbehoerde
- § 46 StVO — Ausnahmen vom Fahrverbot / Haltverbot fuer bestimmte Fahrzeuge oder Zwecke
- Zeichen 286 StVO — eingeschraenktes Halteverbot (Lieferzone mit Zusatzzeichen)
- Zeichen 250, 253 StVO — Durchfahrtverbote mit Lieferausnahme-Zusatzzeichen
- §§ 11 ff. StrWG NRW (bzw. Landesrecht) — Sondernutzung oeffentlicher Strassen
- § 21a StVZO — Ladungssicherung; Haftung bei Ladungsrutsch
- VO (EG) 561/2006 — Lenk- und Ruhezeiten Gueterverkehr
- § 22 StVO — Ladung; Hoechstgewicht, Breite, Laenge

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Bedarf analysieren:** Welche Betriebe brauchen Lieferflaeche, welche Frequenz, welche Fahrzeugklassen?
2. **Bestandsaufnahme:** vorhandene Haltverbote, Parkraumbewirtschaftung, Fussgaengerzonen abgleichen
3. **Standort pruefen:** Sichtweite, Kreuzungsabstand (§ 12 I Nr. 1 StVO 5m-Regel), OEPNV-Haltestelle
4. **Rechtsgrundlage waehlen:** Haltverbotsaufhebung (§ 45 StVO), Lieferzone Zeichen 286, Sondernutzung
5. **Zeitfenster festlegen:** Hauptlieferzeit 06:00-11:00 Uhr; Abendlieferung ggf. mit Laermbeschraenkung
6. **Ausnahmegenehmigung beantragen (§ 46 StVO):** Antrag bei Strassenverkehrsbehoerde, Fahrzeugliste, Nachweis gewerblicher Notwendigkeit
7. **Beschilderung konzipieren:** Zeichen 286 + Zusatzzeichen Zeitfenster + Fahrleistungsbegrenzung
8. **Sondernutzungsvertrag (wenn noetig):** Abschluss mit Gemeinde nach StrWG; Jahresgebuehr
9. **Ladungssicherung sicherstellen:** § 22 StVO, VDI 2700; Unterweisung Fahrer
10. **Evaluation:** Verkehrsbeobachtung 3 Monate nach Einrichtung; Anpassung wenn Dauerstau

## Entscheidungsbaum Lieferzonenstrategie

```
Lieferbedarf identifiziert
 |
Bestehende Lieferzone vorhanden?
 Ja ──→ Ausnahme § 46 StVO beantragen; Zeitfenster pruefen
 Nein ──→ neue Lieferzone einrichten
 |
Einrichtung durch Behoerde (§ 45 StVO)
 Oeffentliche Strasse ──→ Verkehrszeichen-Anordnung
 Privateigentum ──→ Sondernutzungsvertrag (§§ 11 ff. StrWG)
 |
Zeitlich beschraenkt?
 Ja ──→ Zusatzzeichen Zeitfenster (z.B. Mo-Sa 6-10 Uhr)
 Nein ──→ unbefristete Haltezone (selten genehmigt in Innenstadt)
 |
Groessere Fahrzeuge (>7,5 t)?
 Ja ──→ zusaetzliche Ausnahmegenehmigung §§ 29 46 StVO
 Nein ──→ Standardregelung
```

## Output-Template Antrag Ausnahmegenehmigung

**Adressat:** Strassenverkehrsbehoerde — Tonfall: sachlich-antragstellend

```
[KANZLEI / UNTERNEHMEN]
[ADRESSE] [ORT], [DATUM]

An die Strassenverkehrsbehoerde [ORT]
[ADRESSE]

Antrag auf Ausnahmegenehmigung nach § 46 StVO

Antragsteller/in: [FIRMA / NAME], [ADRESSE], USt-IdNr. [X]

Sehr geehrte Damen und Herren,

wir beantragen fuer unser Unternehmen eine Ausnahmegenehmigung fuer die
Einfahrt in die Fussgaengerzone / Nutzung des eingeschraenkten Haltverbots
in der [STRASSE], [PLZ ORT]:

Fahrzeuge: [KENNZEICHEN / FAHRZEUGKLASSE]
Zeitraum: [DATUM VON] bis [DATUM BIS]
Zeitfenster: werktags [VON] bis [BIS] Uhr
Zweck: Belieferung der Geschaftsraeume [BEZEICHNUNG], [ADRESSE]

Begruendung:
Eine anderweitige Belieferung ist aus folgenden Gruenden nicht moeglich: [...]
Das Mindestlieferzeitfenster betraegt [X] Stunden pro Tag.

Anlagen:
- Gewerbeanmeldung
- Fahrzeugliste mit Kennzeichen
- Lageplan

Mit freundlichen Gruessen
[UNTERSCHRIFT]
```

## Harte Leitplanken

- § 46 StVO-Genehmigung ist Ermessensentscheidung — kein Rechtsanspruch, aber Anspruch auf fehlerfreie Ermessensausuebung
- Sichtdreiecke und 5-m-Abstands-Regel (§ 12 I Nr. 1 StVO) bei Lieferzonen-Standort unbedingt einhalten
- Ladungssicherung (§ 22 StVO, VDI 2700) vor Beginn jeder Auslieferung pruefen
- OEPNV-Haltestellen und Radwege freihalten — Busverkehr geht vor
- Sondernutzungsgebuehren vertraglich absichern und kalkulieren

---

<!-- AUDIT 27.05.2026 -->
> **Audit-Hinweis (27.05.2026):** BGH VI ZR 281/13, NJW 2014, 2878 entfernt. Tatsaechliches Thema: BGH VI ZR 281/13 (Urt. v. 17.06.2014) betrifft kein Mitverschulden (§ 254 BGB) eines Fahrradfahrers wegen Nichttragens eines Fahrradhelms, NJW 2014, 2493 — kein Bezug zu Frachtfuehrer-Haftung oder Verkehrssicherungspflicht beim Entladen. NJW 2014, 2878 gehoert nicht zu diesem Urteil. Quelle: dejure.org/2014,13360.
