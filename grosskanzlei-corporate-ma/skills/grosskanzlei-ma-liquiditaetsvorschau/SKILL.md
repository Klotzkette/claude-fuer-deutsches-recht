---
name: grosskanzlei-ma-liquiditaetsvorschau
description: "Freistehende Liquiditaetsvorschau fuer Corporate M&A und Distressed M&A: Anwendungsfall Kaeufer Verkaeufer oder Vorstand braucht kurzfristige Zahlungsfaehigkeits-Uebersicht 3-Wochen bis 13-Wochen-Horizont. § 17 InsO Zahlungsunfaehigkeit, § 19 InsO Ueberschuldung, § 1 StaRUG Sanierung. Pruefraster 3-Wochen-Liquiditaet, 13-Wochen-Cash-Bridge, Runway-Berechnung, OPOS offene Posten, Bankdaten Kreditlinien Insolvenzschwellen. Output Liquiditaetsplan mit Zeitreihe Ampelstatus und Handlungsempfehlungen. Abgrenzung zu Insolvenzreife-Skill fuer Antragspflicht-Pruefung und zu Fortbestehensprognose-Plugin."
---

# Freistehende Liquiditätsvorschau

## Kernsachverhalt

Die Liquiditätsvorschau ist das zentrale Instrument zur Beurteilung der kurzfristigen Zahlungsfähigkeit eines Unternehmens. In M&A-Transaktionen dient sie dem Käufer zur Risikoeinschätzung (Distressed M&A, Going-Concern-Prüfung), dem Verkäufer zur Darstellung der Finanzkraft und dem Vorstand als Instrument zur Erfüllung der Antragspflicht (§ 15a InsO). In Krisenszenarien ist die 3-Wochen-Vorschau der maßgebliche Indikator für Zahlungsunfähigkeit (§ 17 InsO). Die 13-Wochen-Cash-Bridge ist Standard in Distressed-M&A-Prozessen und wird von Banken, Restrukturierungsberatern und Gerichten als Planungsgrundlage verlangt. Fehler in der Liquiditätsvorschau führen zu falschen Managemententscheidungen, Haftungsrisiken und — im schlimmsten Fall — zur Insolvenzverschleppung.

## Kaltstart-Rückfragen

1. Welcher Planungshorizont ist erforderlich — 3 Wochen (Zahlungsunfähigkeitsprüfung), 13 Wochen (Cash-Bridge), 26 oder 52 Wochen (Runway, Going Concern)?
2. Welche Datenquellen stehen zur Verfügung — Bankkontoauszüge (aktuell), OPOS Kreditoren, OPOS Debitoren, Lohnliste, Steuerbescheide, Mietverträge, Kreditverträge?
3. Existiert ein Management Forecast? Wie plausibel ist er angesichts der Bankdaten und OPOS?
4. Gibt es Cash Pools, Treuhandkonten, Intercompany-Forderungen oder gebundene Konten, die nicht frei verfügbar sind?
5. Bestehen Zahlungsstockungen, Rücklastschriften, Covenants-Verletzungen oder Kreditkündigungen?
6. Handelt es sich um eine Krisenprüfung (§§ 17–19 InsO) oder um eine normale Buy/Sell-Side-DD?
7. Welche Szenarien sollen modelliert werden — Base Case, Downside, No-Funding-Case, Closing Delay?
8. Wer empfängt die Vorschau — internes Board Paper, externe Banken, Insolvenzgericht, DD-Bericht?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte

| Norm | Regelungsinhalt (Auszug) |
|---|---|
| § 17 InsO | Zahlungsunfähigkeit: Schuldner nicht in der Lage, fällige Zahlungspflichten zu erfüllen; bei mehr als 10 % Liquiditätslücke über 3 Wochen in der Regel anzunehmen |
| § 18 InsO | Drohende Zahlungsunfähigkeit: voraussichtlich nicht in der Lage, Verbindlichkeiten bei Fälligkeit zu erfüllen (Prognosezeitraum 24 Monate für StaRUG) |
| § 19 InsO | Überschuldung: Vermögen deckt Verbindlichkeiten nicht; Fortbestehensprognose als Korrektiv |
| § 15a InsO | Antragspflicht des Geschäftsführers / Vorstands; Frist 3 Wochen (Zahlungsunfähigkeit) / 6 Wochen (Überschuldung) |
| § 15b InsO | Zahlungsverbote nach Insolvenzreife; Haftung für masseschmälernde Zahlungen; Rückforderungsanspruch des Insolvenzverwalters |
| §§ 91, 91a AktG; § 43 GmbHG | Pflicht zur Einrichtung eines Frühwarnsystems; Geschäftsführerhaftung bei Pflichtverletzung |
| § 321a HGB | Berichtspflicht des Abschlussprüfers über bestandsgefährdende Risiken |

### Leitentscheidungen

| Gericht | Az. | Datum | Leitsatz (kurz) |
|---|---|---|---|
| BGH | II ZR 277/16 | 19.06.2018 | Zahlungsunfähigkeit beginnt bei Liquiditätslücke > 10 %; Geschäftsführer muss Liquiditätsstatus laufend überwachen; Unwissenheit schützt nicht |
| BGH | IX ZR 61/12 | 19.12.2013 | Fortbestehensprognose für § 19 InsO: überwiegende Wahrscheinlichkeit des Fortbestehens; Prognose muss auf plausiblen Annahmen beruhen |
| BGH | II ZR 252/13 | 14.10.2014 | § 15b InsO-Vorgänger: Geschäftsführer haftet für nach Eintritt Insolvenzreife geleistete Zahlungen; Sorgfaltsmaßstab erhöht |
| IDW S 11 | — | 2022 | IDW-Standard zur Beurteilung des Vorliegens von Insolvenzeröffnungsgründen; Methodik Liquiditätsstatus und Fortbestehensprognose |
| OLG München | 7 U 2345/20 | 14.04.2021 | Cash Pools: Konzerninterne Verrechnungen sind nicht als freie Liquidität anzusetzen, wenn Rückforderungsrecht des Mutterunternehmens besteht |

## Prüfschema Liquiditätsvorschau


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Startliquidität bestimmen | Bankkontoauszüge (Stichtag); Cash Pools (nur freier Anteil); Treuhandkonten separat; Intercompany: Rückforderungsrisiko prüfen | Startliquidität EUR [X] |
| 2 | Fällige Verbindlichkeiten (OPOS Kreditoren) | Fälligkeitsliste aus OPOS: Lieferanten, Mieten, Löhne, Steuern, Sozialversicherung, Debt Service, Litigation-Rückstellungen | Auszahlungsplan erstellt |
| 3 | Erwartete Einzahlungen (OPOS Debitoren) | Forderungsbestand, Fälligkeit, Ausfallwahrscheinlichkeit, Zahlungsverhalten der Top-5-Kunden | Einzahlungsplan erstellt |
| 4 | 3-Wochen-Vorschau | Woche 1–3: Anfangsbestand, Einzahlungen, Auszahlungen, Endbestand, Deckungslücke, Ampel | Ampel: grün / gelb / rot |
| 5 | 13-Wochen-Cash-Bridge | Wochen 1–13: Detailplanung je Woche; Brückenfinanzierungsbedarf identifizieren | Bridge-Bedarf EUR [X] |
| 6 | 26-/52-Wochen-Runway | Monatliche Planung; Going-Concern-Horizont; Board-Paper-Grundlage | Runway: [X] Monate |
| 7 | Szenarien modellieren | Base Case, Downside (Umsatzrückgang -20 %), No-Funding-Case, Closing Delay | Szenario-Tabelle |
| 8 | SPA-Liquiditätsprüfung | Locked Box vs. Completion Accounts; Net Debt-Definition; Cash-like Items, Debt-like Items; Working Capital-Mechanik | SPA-Liquidität klar |
| 9 | Covenant- und MAC-Check | Bank-Covenants, Financial Covenants, MAC-Klausel; Default-Risiko identifizieren | Covenant-Status |
| 10 | Management-Forecast-Plausibilisierung | Forecast vs. Bankdaten; historische Abweichungen; unrealistische Annahmen markieren | Forecast-Qualität bewertet |
| 11 | Passiva II sichtbar machen | Eventualverbindlichkeiten, Bürgschaften, Patronatserklärungen, Pensionsrückstellungen | Passiva II dokumentiert |
| 12 | Steuer- und SV-Rückstand prüfen | Rückstände Finanzamt, Krankenkassen, Berufsgenossenschaft; Vollstreckungsrisiko | Steuer/SV-Status |
| 13 | Quellenlog und Annahmenbuch | Jede Zahl belegen; unklare Posten als TODO mit Owner und Frist | Quellenlog vollständig |
| 14 | Insolvenzreife-Schwelle prüfen | Bei Liquiditätslücke > 10 % über 3 Wochen: § 17 InsO; → Übergabe an `grosskanzlei-ma-insolvenzreife` | Schwellen klar |
| 15 | Freigabe und Senior Review | Board Paper-Version; Senior-Review-Gate; Human-in-the-loop-Eskalation | Freigabe dokumentiert |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Zahlungsunfähigkeit (§ 17 InsO) | Insolvenzverwalter / Gläubiger | Bankkontoauszüge, OPOS-Listen, Liquiditätsstatus |
| Drohende Zahlungsunfähigkeit (§ 18 InsO) | Schuldner (Antragsteller) | Management Forecast, Finanzmodell, Gutachter |
| Plausibilität der Fortbestehensprognose | Geschäftsführung | Auftragsbestand, Finanzierungszusagen, Budgetplanung |
| Masseschmälernde Zahlung (§ 15b InsO) | Insolvenzverwalter | Buchungsbelege, Überweisungsbelege, Zeitpunkt der Insolvenzreife |

## Fristen und Verjährung

| Fristtyp | Dauer | Norm | Hinweis |
|---|---|---|---|
| Antragspflicht bei Zahlungsunfähigkeit | 3 Wochen | § 15a Abs. 1 InsO | Absolute Frist; kein Aufschub |
| Antragspflicht bei Überschuldung | 6 Wochen | § 15a Abs. 1 InsO | Bei positiver Fortbestehensprognose kein Antrag nötig |
| § 15b-Haftung | Verjährung 3 Jahre ab Kenntnis | §§ 195, 199 BGB | Insolvenzverwalter geltend machen |
| Insolvenzanfechtung (§§ 130–134 InsO) | 1, 4, 10 Jahre je nach Tatbestand | §§ 130–134 InsO | Rückforderungsansprüche des Insolvenzverwalters |

## Typische Gegenargumente

| Argument | Erwiderung |
|---|---|
| Liquiditätslücke ist nur vorübergehend | Mehr als 3 Wochen andauernde Lücke > 10 % begründet nach BGH II ZR 277/16 Zahlungsunfähigkeit; keine Ausnahme für Saisonschwankungen ohne konkrete Abhilfemaßnahmen |
| Cash Pool ist verfügbar | OLG München 7 U 2345/20: Cash Pool-Guthaben nur ansetzen, wenn kein Rückforderungsrecht des Poolführers besteht und Rückzahlung nicht kurzfristig gefordert wird |
| Forecast zeigt Erholung in 6 Monaten | Für § 17 InsO zählt nur aktuelle Fälligkeit; Erholung in der Zukunft ändert nichts an gegenwärtiger Zahlungsunfähigkeit |
| Geschäftsführer hatte keinen Überblick | Keine Entlastung: Pflicht zur Liquiditätsüberwachung ist organschaftliche Kermpflicht (BGH II ZR 277/16) |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Liquiditaetsvorschau fuer M-and-A erstellen | Vorschau nach Schema; Schriftsatz unten |
| Variante A — Kurzfristige Liquiditaet noetig 4 Wochen | Kurzfrist-Liquiditaet als Teilbereich der Vorschau |
| Variante B — Insolvenzreife droht Vorschau fuer Dokumentation | Insolvenz-Skill parallel; Dokumentation fuer Haftungsschutz |
| Variante C — Mandant will Vorschau fuer Bankengespraeche | Bankgespraeche-Format mit Zusammenfassung anpassen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Liquiditätsvorschau-Tabelle (3 Wochen)

```
LIQUIDITÄTSVORSCHAU — VERTRAULICH — Projekt [Deal-Code]
Stichtag: [TT.MM.JJJJ]   Erstellt von: [Name]

| Position           | Woche 1     | Woche 2     | Woche 3     |
|--------------------|-------------|-------------|-------------|
| Anfangsbestand     | EUR [X]     | EUR [Y]     | EUR [Z]     |
| + Einzahlungen     | EUR [...]   | EUR [...]   | EUR [...]   |
|   davon Debitoren  | EUR [...]   | EUR [...]   | EUR [...]   |
|   davon sonstige   | EUR [...]   | EUR [...]   | EUR [...]   |
| - Auszahlungen     | EUR [...]   | EUR [...]   | EUR [...]   |
|   davon Löhne/GH   | EUR [...]   | EUR [...]   | EUR [...]   |
|   davon Lieferant. | EUR [...]   | EUR [...]   | EUR [...]   |
|   davon Steuern/SV | EUR [...]   | EUR [...]   | EUR [...]   |
|   davon Debt Serv. | EUR [...]   | EUR [...]   | EUR [...]   |
| Endbestand         | EUR [Y]     | EUR [Z]     | EUR [A]     |
| Deckungslücke      | EUR 0       | EUR 0       | EUR [B]     |
| AMPEL              | GRÜN        | GRÜN        | ROT         |

HINWEIS: Woche 3 zeigt Deckungslücke EUR [B]. Prüfung § 17 InsO erforderlich.
TODO [Owner] bis [Datum]: Brückenfinanzierung sicherstellen oder StaRUG-Anzeige prüfen.
```

### Baustein 2 — Annahmen-Memo für Management Forecast-Plausibilisierung

```
ANNAHMENBUCH — Liquiditätsvorschau — Projekt [Deal-Code]
Stand: [Datum]

A. EINZAHLUNGEN
1. Debitoren-OPOS: EUR [X] fällig in Woche [X]. Ausfallwahrscheinlichkeit [Y] %.
   Quelle: OPOS-Liste vom [Datum]. NICHT BELEGBAR: [Posten] — TODO [Owner].
2. Anzahlungen Auftrag [Nr.]: EUR [X], Zahlungseingang [Datum] lt. Auftragsbestätigung.
   Quelle: Auftragsbestätigung Anlage [X].

B. AUSZAHLUNGEN
1. Löhne: EUR [X], Fälligkeit [Datum]. Quelle: Lohnliste [Datum].
2. Steuerrückstand: EUR [X], Fälligkeit [Datum] lt. Bescheid [AZ].
   Risiko: Vollstreckung bei Nichtzahlung. TODO [Owner] bis [Datum]: Ratenzahlungsantrag.

C. KRITISCHE ANNAHMEN
- Kreditlinie Bank [Name]: EUR [X] verfügbar. Covenant-Verletzung ab [Datum] möglich.
  TODO: Bankgespräch bis [Datum].
- Management-Forecast-Umsatz Q2 +15 %: NICHT PLAUSIBEL auf Basis OPOS.
  Korrektur: -8 % angesetzt.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Streitwert und Kosten

| Posten | Ansatz | Hinweis |
|---|---|---|
| Haftung nach § 15b InsO | Summe aller nach Insolvenzreife geleisteten Zahlungen | Direktanspruch gegen Geschäftsführer |
| Kosten Restrukturierungsberater | EUR 50.000–500.000 je nach Komplexität | Cash-Bridge-Erstellung ist Kernleistung |
| Insolvenzverwalterkosten | § 2 InsVV: gestaffelt nach Masse | Minimierung durch frühzeitige StaRUG-Nutzung |
| W&I-Ausschluss bei Liquiditätsrisiken | Prämienerhöhung oder Ausschluss von Liquiditätsmangel-Garantien | Versicherbarkeit prüfen |

## Strategische Empfehlung

| Akteur | Empfehlung |
|---|---|
| Geschäftsführung | Liquiditätsstatus wöchentlich überwachen; Quellenprotokoll führen; bei Deckungslücke sofort Rechtsrat holen |
| Käufer (DD) | Liquiditätsvorschau als Closing Condition verlangen; Locked Box bevorzugen bei Volatilität; Mac-Klausel mit konkretem Liquiditätsschwellenwert |
| Berater | Annahmenbuch immer anlegen; Forecast nie unkritisch übernehmen; Ampelsystem für Deal-Karte verwenden |

## Anschluss-Skills

- `grosskanzlei-ma-insolvenzreife` — Insolvenzreife-Prüfung bei roter Ampel
- `corporate-kanzlei-restructuring-starug-insolvenzplan` — StaRUG-Anzeige und Plangestaltung
- `grosskanzlei-ma-aktenanlage` — Dokumentation in Deal-Akte einpflegen
- `grosskanzlei-ma-tabellenreview` — Liquiditätstabellen reviewen
- `anw-insolvenzreife-pruefung-17-19-inso` — Detailprüfung Insolvenztatbestände

## Quellen

- BGH, Urt. v. 19.06.2018, Az. II ZR 277/16 (Zahlungsunfähigkeit, 10 %-Schwelle)
- BGH, Urt. v. 19.12.2013, Az. IX ZR 61/12 (Fortbestehensprognose)
- BGH, Urt. v. 14.10.2014, Az. II ZR 252/13 (Masseschmälernde Zahlungen)
- OLG München, Urt. v. 14.04.2021, Az. 7 U 2345/20 (Cash Pool)
- IDW S 11 (2022): Beurteilung des Vorliegens von Insolvenzeröffnungsgründen
- §§ 17, 18, 19, 15a, 15b InsO; §§ 91, 91a AktG; § 43 GmbHG; § 321a HGB

## Ergaenzende Rechtsprechung (v14.2)

- BGH, Urt. v. 22.10.2020 - IX ZR 208/17, NJW 2021, 538 — Liquiditaetsplanung und Insolvenzreife: Geschaeftsfuehrer muss eine 13-Wochen-Liquiditaetsplanung fuehren; Fehleinschaetzungen koennen § 15b InsO-Haftung ausloesen; Liquiditaetsplanung muss belastbar und dokumentiert sein
