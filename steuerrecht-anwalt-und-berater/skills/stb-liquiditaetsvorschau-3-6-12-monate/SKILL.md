---
name: stb-liquiditaetsvorschau-3-6-12-monate
description: "Rollierende Liquiditaetsvorschau 3-6-12 Monate fuer GmbH oder UG erstellen mit insolvenzrechtlicher Fortbestehensprognose. Anwendungsfall Steuerberater begleitet Krisenmandat und benoetigt strukturierte Zahlungsplanung fuer Insolvenzreife-Pruefung. Methodisch nach IDW S 6 Sanierungskonzept und IDW S 11 Insolvenzoeffnungsgruende. Wochenraster Pruefung Zahlungsunfaehigkeit § 17 InsO 10-Prozent-Luecke drei Wochen Ueberschuldung § 19 InsO. Output rollierende Tabelle Ampel-Bewertung Excel-Export. Abgrenzung zu stb-liquiditaetsvorschau-3wochen Kurzfristversion."
---

# Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose (§§ 17, 19 InsO)

## Kernsachverhalt

Krisenhafte GmbH/UG-Mandanten benötigen eine strukturierte, wöchentlich rollierte Liquiditätsvorschau als Grundlage für die insolvenzrechtliche Prüfung nach § 17 InsO und für die Fortführungsprognose nach § 19 InsO. Der Skill erzeugt diese Planung aus dem typischen unstrukturierten Steuerberater-Material (BWA, SuSa, offene Posten, Kontoauszüge) und generiert automatisch eine insolvenzrechtliche Ampel pro Woche.

## Kaltstart-Rückfragen

1. Welche Stammdaten — Rechtsform, Branche, Mitarbeiterzahl, Jahresumsatz, Stichtag, Hausbank?
2. Welche Liquiditätsdaten liegen vor — Kontostand, Kreditlinien (Stand und Limit), offene Forderungen-Liste?
3. Welche offenen Verbindlichkeiten bestehen — Kreditorenliste mit Fälligkeitsdatum und Mahnstufe?
4. Welche Dauerverpflichtungen — Miete, Lohn, SV-Beiträge (Drittellast), Lohnsteuer, Leasing, Versicherungen?
5. Welche Steuerverbindlichkeiten — USt-Voranmeldungsturnus, Körperschaft- und Gewerbesteuer-Vorauszahlungen, Rückstände?
6. Welcher Auftragsbestand — zugesagte Aufträge mit Zahlungserwartung, Abschläge, Zahlungsziel?
7. Gibt es Kreditverträge mit Covenants (EK-Quote, Leverage) und wann sind diese zu messen?
8. Liegt ein Sanierungskonzept IDW S 6 vor oder soll die Vorschau Grundlage dafür sein?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Primärnormen

**§ 17 InsO** — Zahlungsunfähigkeit: Liquiditätslücke ≥ 10 %, nicht beseitigbar binnen 3 Wochen (BGH BGHZ 163, 134 Rn. 12 ff.).

**§ 18 InsO** — Drohende Zahlungsunfähigkeit: voraussichtliche Unfähigkeit im 24-Monats-Horizont; Grundlage Eigenantragsoption.

**§ 19 InsO** — Überschuldung: Fortbestehensprognose primär; bei negativer Prognose Liquidationswerte-Status. Prognosezeitraum nach SanInsKG 24 Monate (für Anträge bis 31.12.2026).

**§ 15a InsO** — Antragspflicht: 3 Wochen (§ 17), 6 Wochen (§ 19).

**§ 102 StaRUG** — Hinweispflicht des Steuerberaters; Liquiditätsvorschau als technisches Instrument der Krisenfrüherkennung.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| BGH IX ZR 123/04 | BGHZ 163, 134 | 24.05.2005 | Definition Zahlungsunfähigkeit; 10-%-Lücke; 3-Wochen-Frist |
| BGH IX ZR 228/03 | NJW 2007, 78 | 12.10.2006 | Indizienkatalog: SV-Rückstände, Stundungen, Rücklastschriften |
| BGH II ZR 233/18 | NJW 2020, 1809 | 19.11.2019 | Fortbestehensprognose; tragfähiges Konzept + Finanzplan; überwiegende Wahrscheinlichkeit |
| BGH II ZR 298/11 | BGHZ 195, 42 | 09.10.2012 | Insolvenzrechtliche Überschuldung; Fortführungs- vs. Liquidationswerte |
| BGH IX ZR 48/21 | IX ZR 48/21 | 10.02.2022 | 10-%-Schwelle bei Zahlungsunfähigkeit; Klarstellung Passivseite |
| BGH IX ZR 229/22 | IX ZR 229/22 | 15.09.2023 | Titulierte Forderungen mit Nennwert als Passiva I; keine Abzinsung |
| BGH II ZR 139/23 | II ZR 139/23 | 12.03.2024 | Objektive Beurteilung der Zahlungsunfähigkeit; kein subjektives Element erforderlich |

## Prüfschema Liquiditätsvorschau


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Datenaufnahme | BWA, SuSa, Kontoauszüge, Kreditorenliste, Debitorenliste, Dauerverpflichtungen | Datenbasis vollständig |
| 2 | Eröffnungsbestand Liquidität | Kontostand, ungenutzte Kreditlinie (ziehungsfähig), Tagesgeld | Aktiva I-Basis |
| 3 | Einzahlungs-Buckets | Kundenforderungen nach Eingangswahrscheinlichkeit; USt-Erstattung; sonstige | Einzahlungsplan |
| 4 | Auszahlungs-Buckets | Personal (Lohn × 1.28 inkl. AG-SV); USt-Zahlung; KSt/GewSt-Vorauszahlungen; Miete; Leasing; Zins+Tilgung; Lieferanten | Auszahlungsplan |
| 5 | Wochenraster 13 Wochen | Spalten: KW, Anfangsbestand, Einzahlungen, Auszahlungen, Endbestand, fällige VB Folgewoche, 3-Wochen-Lücke (kumuliert), Quote, Ampel | Primäres Instrument § 17 InsO |
| 6 | 3-Wochen-Test § 17 InsO | Quote = Lücke_3W / fällige VB ≥ 10 %? Nicht binnen 3 Wochen schließbar? | Ampel Rot/Gelb/Grün |
| 7 | SV- und Lohnsteuer-Position | SV-Beiträge (AG+AN-Anteil Drittellast); Lohnsteuer § 41a EStG; separate Zeile; nie aufrechnen | Passiva I korrekt |
| 8 | Steuerforderungen Passiva I | FA-Forderungen; Stundung § 222 AO → außen lassen; AdV § 361 AO → bleibt Passiva I | BGH II ZR 298/11 |
| 9 | Sensitivitätsanalyse | Best/Base/Worst: Zahlungseingang 100 %/80 %/60 %; Auftragserfüllung wie geplant/−10 %/−25 % | Risikoszenario |
| 10 | Mittel- und Langfristhorizont | 26 Wochen (monatlich aggregiert ab Monat 4), 52 Wochen; Fortführungsprognose-Grundlage | § 18 und § 19 InsO |
| 11 | Fortführungsprognose IDW S 6 | Krisenstadium; Konzept; integrierte Planung; überwiegende Wahrscheinlichkeit | § 19 InsO Stufe 1 |
| 12 | Abgrenzung HGB vs. InsO | EK-Negativsaldo ≠ Insolvenzreife; Überschuldungsstatus separat; Stille Reserven/Lasten | BGH BGHZ 195, 42 |
| 13 | Indizienkatalog prüfen | SV-Rückstände, Stundungsanträge, Lastschriftrückläufer, eingestellte Lieferantenzahlungen | Zahlungseinstellung ohne Deckungslücke möglich |
| 14 | Ergebnis-Memo | Ampel-Zusammenfassung; frühester Rot-Eintritt (KW-Angabe); Handlungsempfehlung; § 102 StaRUG | Mandantenkommunikation |
| 15 | Excel-Export | Sheets: 13W, 26W, 52W, Fortführungsprognose, Annahmen; Ampel bedingte Formatierung | Arbeitsunterlage |

## Wochenraster-Struktur (Excel-Vorlage)

```
LIQUIDITÄTSVORSCHAU — [Firma] GmbH
Stand: [Datum]

| KW | Anfangs-  | + Einzah- | − Auszah- | End-    | Fäll. VB | 3W-Lücke | Quote | Ampel |
|    | bestand   | lungen    | lungen    | bestand | Folge-KW | kumuliert |  %    |       |
|----+-----------|-----------|-----------|---------|----------|----------|-------|-------|
| 21 | 18.500    | 42.000    | 47.200    | 13.300  | 61.800   | 48.500   | 78 %  | ROT   |
| 22 | 13.300    | 51.000    | 45.600    | 18.700  | 38.200   |          |       |       |
| 23 | 18.700    | 145.000*  | 44.100    | 119.600 |          |          | GRÜN  |       |
     *Großauftrag-Eingang; Zahlungseingang-Risiko: Base 100 %, Worst 60 %
```

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Zahlungsunfähigkeit zum Stichtag | Insolvenzverwalter / Kläger im Nachhinein | Liquiditätsvorschau als Indiz; BGH NJW 2007, 78 |
| Zahlungseingang-Wahrscheinlichkeit | GF / StB | Debitorenliste, Mahnstand, DA-Liste |
| Kreditlinie ziehungsfähig | GF | Bankbescheinigung über Limit und Valuta |
| SV-Rückstände | Offen aus Buchhaltung; BG-/KK-Bescheide | Konto-Auszüge SV-Beitragskonten |
| Fortführungsprognose positiv | GF / IDW S 6-Gutachter | Integrierter Finanzplan; Konzept |

## Fristen und zeitliche Warnschwellen

| Horizont | Insolvenzrechtliche Bedeutung | Handlungspflicht |
|---|---|---|
| Woche 0–3 | § 17 InsO-Stichtag; 3-Wochen-Test | Sofortige Prüfung Antragspflicht |
| Woche 0–13 | Zahlungsunfähigkeit; 3-Wochen-Test wöchentlich rollierend | Wöchentliche Aktualisierung |
| Woche 0–26 | Mittelfristhorizont; Finanzierungsbedarf | Bankgespräch; Gesellschafterdarlehen |
| Woche 0–52 | Fortbestehensprognose § 19 InsO; IDW S 6-Grundlage | Sanierungskonzept |
| Monate 0–24 | § 18 InsO drohende ZU; SanInsKG | Eigenantragsoption; StaRUG |

## Typische Fehler

| Fehler | Korrekte Vorgehensweise |
|---|---|
| Negativem EK als Insolvenzreife gleichsetzen | Handelsbilanzielle Unterdeckung ≠ Insolvenzreife; Überschuldungsstatus separat (BGH BGHZ 195, 42) |
| Kreditlinie vollständig als Aktiva I | Nur ziehungsfähiger, nicht gesperrter oder bereits ausgeschöpfter Teil |
| Auftragseingang zu optimistisch ansetzen | Sensitivitätsanalyse: Worst-Case-Szenario immer einbeziehen; BGH verlangt realistische Annahmen |
| USt-Voranmeldung fehlt in Auszahlungen | USt monatlich oder quartalsweise je nach Turnus; Dauerfristverlängerung berücksichtigen |
| AdV als Passiva I-Entlastung | Falsch: AdV § 361 AO hemmt Vollziehung, lässt Forderung materiell bestehen (§ 17 InsO-Relevant) |
| Lohnzahlungen ohne AG-SV-Anteil | Drittellast: Lohn × 1.28 für Personal-Gesamtkosten |
| 3-Wochen-Frist ab Erkenntnis (StB-Sicht) | Frist läuft ab Eintritt der Zahlungsunfähigkeit, nicht ab Erstellung der Vorschau |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Liquiditaetsvorschau fuer 3 bis 12 Monate erstellen | Vorschau nach Schema; Schriftsatz unten |
| Variante A — Kurzfristige Liquiditaet kritisch Woche noetig | Kurzfrist-Vorschau separat; dann Mittelfrist ergaenzen |
| Variante B — Saisonales Unternehmen | Saisonalitaets-Hinweise in Vorschau einarbeiten |
| Variante C — Bankfinanzierung laeuft aus Prolongation noetig | Bankgespraeche-Version der Vorschau; Stresstest anfuegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Memo an GF — Liquiditätsvorschau-Ergebnis

```
MEMO — VERTRAULICH
An: Geschäftsführung [Firma] GmbH
Von: [Steuerberater/Kanzlei]
Datum: [Datum]

Betreff: Ergebnis Liquiditätsvorschau 13-Wochen — § 17 InsO-Prüfung

1. Ergebnis Ampel-Übersicht:
   KW [x]: GRÜN (Quote [y] %)
   KW [x+1]: GELB (Quote [z] % — Zahlungsstockung, voraussichtlich
              lösbar durch Eingang Rechnung [Rn.] EUR [x] in KW [x+2])
   KW [x+3]: ROT (Quote [a] % — Zahlungsunfähigkeit § 17 InsO
              droht, falls Eingang Großauftrag ausbleibt)

2. Früheste § 17-InsO-Relevanz: KW [x+3] — [Datum]

3. Handlungsempfehlung:
   a) Sofortige anwaltliche Prüfung der Insolvenzreife beauftragen.
   b) Bankgespräch zur Linienerweiterung bis [Datum].
   c) Auftragseingang [Bezeichnung] sichern/beschleunigen.
   d) Bis KW [x+2] Liquiditätslage neu auswerten.

Wir stehen für ein persönliches Besprechungsgespräch zur Verfügung.
Bitte bestätigen Sie Kenntnisnahme dieses Memos schriftlich.
```

### Baustein 2: Fortführungsprognose — Ergebnisübersicht IDW S 6

```
FORTFÜHRUNGSPROGNOSE — [Firma] GmbH — [Datum]

1. Krisenstadium (IDW S 6):
   [Liquiditätskrise / Ertragskrise / Strategiekrise — begründen]

2. Krisenursachen:
   Intern: [z.B. gesunkene Marge, Personalkosten]
   Extern: [z.B. Nachfragerückgang, Rohstoffpreise]

3. Leitbild des sanierten Unternehmens:
   [Kerngeschäft; Restrukturierungsmaßnahmen; Ziel-Geschäftsmodell]

4. Maßnahmen zur Krisenbewältigung:
   Innenfinanzierung: [Forderungsabbau, WC-Reduzierung]
   Außenfinanzierung: [Gesellschafterdarlehen, Bankgespräch]
   Leistungswirtschaftlich: [Kostenabbau, Produktsortiment]

5. Integrierte 24-Monats-Planung:
   Monat 1–12: Ergebnis [x]; Cashflow [y]; EK [z]
   Monat 13–24: Ergebnis [a]; Cashflow [b]; EK [c]

6. Ergebnis Fortführungsprognose:
   [ ] Positiv — überwiegende Wahrscheinlichkeit der Fortführung
   [ ] Negativ — Fortführung nicht überwiegend wahrscheinlich
   Begründung: [...]

7. Rechtsfolge für § 19 InsO:
   Positiv: keine Überschuldung, auch bei negativem Eigenkapital.
   Negativ: Überschuldungsstatus mit Liquidationswerten erforderlich.
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

| Position | Berechnung | Hinweis |
|---|---|---|
| Liquiditätsplanung (laufend) | Zeithonorar StB; typisch EUR 500–2.000 je Monat | Als eigenständige Leistung vereinbaren |
| Sanierungskonzept IDW S 6 | EUR 10.000–50.000+ je nach Komplexität | WP/StB mit Sanierungserfahrung |
| Insolvenzreife-Gutachten Anwalt | § 34 RVG oder Stundensatz; typisch EUR 2.000–8.000 | Wird durch Liquiditätsvorschau als Datenbasis vorbereitet |
| Excel-Vorlage Erstellung | Einmalig ca. 4–8 Stunden; dann rollierend 1–2 h/Woche | — |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Grüne Ampeln, kein § 17-Risiko | Monatliche Aktualisierung; § 102 StaRUG-Hinweispflicht dokumentiert erfüllt |
| Gelbe Ampeln — Zahlungsstockung absehbar lösbar | Bankgespräch; Gesellschafterdarlehen; Debitoren-Beschleunigung; wöchentliche Aktualisierung |
| Rote Ampele — § 17 InsO-Schwelle | Sofortige anwaltliche Beratung; Antragspflicht-Check; § 102 StaRUG-Warnschreiben |
| Großauftrag als einziger Ausweg | Worst-Case-Szenario ohne Auftrag ausarbeiten; nicht auf Eingang vertrauen ohne Vertrag |
| Kreditlinien ausgeschöpft | Neue Finanzierungsquellen (Factoring, Gesellschafter, Sale-and-Lease-back) prüfen |

## Anschluss-Skills

- `anw-insolvenzreife-pruefung-17-19-inso` — anwaltliche Insolvenzreife-Prüfung mit Datenbasis aus Liquiditätsvorschau
- `stb-bwa-sus-bilanz-pruefung` — vorgelagerte BWA/SuSa-Prüfung
- `stb-warnschreiben-krisensignale` — § 102 StaRUG-Pflichthinweis an GF

## Quellen

- InsO §§ 17, 18, 19, 15a, 15b
- StaRUG §§ 1, 102
- SanInsKG (Prognosezeitraum 24 Monate bis 31.12.2026)
- BGH IX ZR 123/04 = BGHZ 163, 134
- BGH IX ZR 228/03 = NJW 2007, 78
- BGH II ZR 233/18 = NJW 2020, 1809
- BGH II ZR 298/11 = BGHZ 195, 42
- BGH IX ZR 48/21 (10-%-Schwelle)
- BGH IX ZR 229/22 (titulierte Forderungen Nennwert)
- BGH II ZR 139/23 (objektive Beurteilung)
- IDW S 6 (Sanierungskonzept); IDW S 11 (Insolvenzeröffnungsgründe)
- K. Schmidt/Herchen, InsO § 17 Rn. 5–35
- Uhlenbruck/Mock, InsO § 19 Rn. 47–95
- Pape/Schaltke, StaRUG § 102 Rn. 8–35
