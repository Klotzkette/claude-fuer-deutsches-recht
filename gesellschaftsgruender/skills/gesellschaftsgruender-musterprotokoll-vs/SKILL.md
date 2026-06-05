---
name: gesellschaftsgruender-musterprotokoll-vs
description: "Musterprotokoll VS: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Musterprotokoll VS

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Musterprotokoll VS** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-musterprotokoll-vs-satzung` | Entscheidet, ob Musterprotokoll reicht oder individuelle Satzung nötig ist. |
| `gesellschaftsgruender-notar-vorbereitung` | Notartermin für GmbH-Gründung vorbereiten: Unterlagencheck, Vollmachten, Ausweisanforderungen. Normen: §§ 2 7 GmbHG, BeurkG. Prüfraster: Gesellschafterliste, Musterprotokoll vs. individueller Gesellschaftsvertrag, Vollmachten. Output: Notartermin-Checkliste. Abgrenzung: nicht Handelsregisteranmeldung nach Beurkundung. |
| `gesellschaftsgruender-notarbriefing-onepager` | Erstellt ein Notarbriefing mit Firma, Sitz, Gegenstand, Kapital, Gesellschaftern, GF, Besonderheiten. |
| `gesellschaftsgruender-one-page-roadmap` | Erstellt eine einseitige Roadmap von Idee bis Eintragung und operativem Start. |
| `gesellschaftsgruender-online-gruendung-dirug` | Online-Gründung der GmbH nach DiRUG ohne persoenlichen Notartermin: Voraussetzungen, Verfahren, Grenzen. Normen: § 2 Abs. 3 GmbHG, DiRUG. Prüfraster: Musterprotokoll-Pflicht, Videoidentifikation, Beschraenkungen. Output: Checkliste Online-Gründung mit Verfahrensschritten. Abgrenzung: nicht individuelle Satzung (erfordert Praesenz). |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Musterprotokoll VS**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-musterprotokoll-vs-satzung`

**Fokus:** Entscheidet, ob Musterprotokoll reicht oder individuelle Satzung nötig ist.

# Musterprotokoll vs individuelle Satzung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Musterprotokoll vs individuelle Satzung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Mehrere Gründer, Vesting, Investoren, Geschäftsordnung, Vinkulierung sprechen gegen Musterprotokoll.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 2. `gesellschaftsgruender-notar-vorbereitung`

**Fokus:** Notartermin für GmbH-Gründung vorbereiten: Unterlagencheck, Vollmachten, Ausweisanforderungen. Normen: §§ 2 7 GmbHG, BeurkG. Prüfraster: Gesellschafterliste, Musterprotokoll vs. individueller Gesellschaftsvertrag, Vollmachten. Output: Notartermin-Checkliste. Abgrenzung: nicht Handelsregisteranmeldung nach Beurkundung.

# Notar-Vorbereitung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Notar-Vorbereitung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor dem Notartermin

1. Ist es eine Bargründung oder Sachgründung? Bei Sacheinlage: Sachgründungsbericht zwingend.
2. Sind alle Gesellschafter persönlich erscheinen oder sind Vollmachten erforderlich (notariell beglaubigt)?
3. Sind alle Gesellschafter deutsche oder EU-Staatsangehörige mit eID — oder sind Ausländer mit Apostille und beglaubigter Übersetzung erforderlich?
4. Ist eine Online-Gründung nach DiRUG (seit 01.08.2022) möglich und gewünscht?
5. Liegt die Bank-Bestätigung über die Stammkapital-Einzahlung vor (vor HR-Anmeldung, nicht zwingend vor Beurkundung)?
6. Ist der Firmenname vorab bei der IHK oder dem HR geprüft worden?

## Zentrale Normen

- **§ 2 GmbHG** — Beurkundungspflicht: GmbH-Gründung muss notariell beurkundet werden; Musterprotokoll möglich (§ 2a GmbHG).
- **§ 17 BeurkG** — Belehrungspflicht des Notars: Notar muss Inhalt vollständig vorlesen und erläutern; Beteiligten Zeit zu Rückfragen geben.
- **§§ 16a-d BeurkG** — Online-Beurkundung nach DiRUG: Videokonferenz-Verfahren; nur Bargründung.
- **§ 5 Abs. 4 GmbHG** — Sachgründungsbericht: bei Sacheinlage Werthaltigkeit dokumentieren.
- **§ 9 GmbHG** — Differenzhaftung: Gesellschafter haftet für Wertunterschied wenn Sacheinlage unter angemeldeten Wert fällt.
- **§ 23 AktG** — AG-Satzung: notarielle Beurkundung; höhere Anforderungen als GmbH.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kosten-Überblick (GNotKG 2026)

| Gründungsart | Stammkapital | Notar ca. | HR ca. | Gesamt ca. |
|---|---|---|---|---|
| UG Musterprotokoll | 1-5.000 EUR | 250-400 EUR | 150 EUR | 400-600 EUR |
| GmbH Musterprotokoll | 25.000 EUR | 400-600 EUR | 150 EUR | 600-800 EUR |
| GmbH individuelle Satzung | 25.000 EUR | 700-1.200 EUR | 150 EUR | 900-1.400 EUR |
| GmbH individuelle Satzung | 100.000 EUR | 1.200-2.000 EUR | 200 EUR | 1.500-2.500 EUR |
| AG-Gründung | 50.000 EUR | 2.000-5.000 EUR | 300 EUR | 3.000-6.000 EUR |
| Anteilsübertragung | Verkehrswert | 500-3.000 EUR | 100 EUR | 600-3.200 EUR |

## Musterprotokoll vs. Individuelle Satzung

| Kriterium | Musterprotokoll (§ 2a GmbHG) | Individuelle Satzung |
|---|---|---|
| Gesellschafter | Max. 3 | Unbegrenzt |
| Geschäftsführer | Max. 1 | Mehrere |
| Gestaltungsfreiheit | Keine | Voll |
| Investoren-Tauglichkeit | Eingeschränkt | Standard |
| Vesting / Klassen | Nicht möglich | Möglich |
| Notarkosten | Günstiger | Teurer |
| Geeignet für | Solo-Gründer, einfache Paar-Gründung | Mehrgründer, Investor-Vorbereitung |

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen beantworten; Gründungstyp festlegen.
2. **Notar auswählen** — gesellschaftsrechtlich erfahrenen Notar; Termin 1-2 Wochen vorab buchen.
3. **Online oder Präsenz?** — DiRUG-Online-Gründung prüfen (nur Bargründung, kein AG).
4. **Satzungsentwurf** — Notar übersendet Vorabentwurf ca. 1 Woche vorher; sorgfältig prüfen.
5. **Unterlagen-Checkliste** — alle Dokumente gemäß Template unten zusammenstellen.
6. **Test bei Online-Gründung** — technischen Test-Termin ca. 30 Min. vor Haupttermin.
7. **Beurkundungstermin** — Identität prüfen; Urkunde vorlesen; Rückfragen stellen; unterschreiben.
8. **Nach Beurkundung** — Stammkapital einzahlen; Einzahlungsbeleg an Notar; Notar meldet beim HR an.

## Output-Template Unterlagen-Checkliste Notartermin

**Adressat:** Gründer / Mandant — Tonfall anleitend-verständlich
```
UNTERLAGEN-CHECKLISTE NOTARTERMIN
Gesellschaft (geplant): [Firmenname] GmbH
Notartermin: [Datum, Uhrzeit, Ort / Video-Link]
Notar: [Name, Anschrift]
Erstellt: [Datum]

ALLE BETEILIGTEN MITBRINGEN
[ ] Gültiger Personalausweis oder Reisepass (alle Gesellschafter + GF)
[ ] Bei GmbH als Gesellschafterin: HR-Auszug (max. 4 Wochen alt) + Vollmacht
[ ] Bei Ausländern: Apostille + beglaubigte Übersetzung Gesellschaftsnachweis

BEREITS VOM NOTAR / ANWALT VORBEREITET
[ ] Satzungsentwurf — Version [Nr.], geprüft am [Datum]
[ ] Gesellschafterliste — alle Gesellschafter mit Quote und Adresse
[ ] Musterprotokoll-Variante (falls gewählt)

ZU ORGANISIEREN VOR TERMIN
[ ] IHK-Firmenvorprüfung Ergebnis: [ ] Freigegeben / [ ] Ausstehend
[ ] Stammkapital auf GmbH-Konto überwiesen: [ ] [EUR] am [Datum]
[ ] Bankbestätigung über Einzahlung: [ ] Vorhanden / [ ] Wird nachgereicht
[ ] Bei Sachgründung: Sachgründungsbericht + Werthaltigkeitsnachweis

ZEITPLAN
T-14: Notar gebucht
T-7: Satzungsentwurf finalisiert
T-3: Vorabentwurf Notar geprüft
T-2: Stammkapital überwiesen
T-0: Beurkundung
T+1: Notar meldet beim HR an (Einzahlungsbeleg vorab senden)
T+14: HR-Eintragung erwartet (Gesellschaft entsteht)
T+14: Gewerbeanmeldung + Finanzamt-Fragebogen
```

## Rote Schwellen

- Personalausweis abgelaufen → Beurkundung scheitert; Ausweisdokumente vorab prüfen.
- Vertretungsnachweis bei Gesellschafterin unvollständig → Termin muss verschoben werden.
- Sachgründungsbericht fehlt → HR-Gericht verweigert Eintragung; persönliche Differenzhaftung.
- Stampkapital noch nicht eingezahlt bei HR-Anmeldung → Anmeldevoraussetzung nicht erfüllt.
- Falscher Firmenname bei Beurkundung → spätere Firmenänderung kostet Notar + HR-Gebühren.

## Quellen und Vertiefung

- §§ 2, 2a, 5, 7, 9 GmbHG (Beurkundung, Musterprotokoll, Sachgründung)
- §§ 16a-d, 17, 40 BeurkG (Online-Beurkundung, Belehrungspflicht)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Emmerich, GmbHG, § 2 Rn. 1-30

## Übergabe an andere Skills

- `gesellschaftsgruender-gmbh-vorbereitung` — Vorbereitung vor Notartermin
- `gesellschaftsgruender-online-gruendung-dirug` — DiRUG-Online-Alternative
- `gesellschaftsgruender-stammkapital-einzahlung` — Einzahlung und Bankbestätigung
- `gesellschaftsgruender-handelsregister-anmeldung` — HR-Anmeldung nach Beurkundung

## 3. `gesellschaftsgruender-notarbriefing-onepager`

**Fokus:** Erstellt ein Notarbriefing mit Firma, Sitz, Gegenstand, Kapital, Gesellschaftern, GF, Besonderheiten.

# Notarbriefing Onepager

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Notarbriefing Onepager` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

So schreiben, dass das Notariat sofort arbeiten kann.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 4. `gesellschaftsgruender-one-page-roadmap`

**Fokus:** Erstellt eine einseitige Roadmap von Idee bis Eintragung und operativem Start.

# One-Page-Gründungsroadmap

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `One-Page-Gründungsroadmap` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Baue Timeline, Zuständigkeiten, Dokumente, Kosten und Stoppschilder.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 5. `gesellschaftsgruender-online-gruendung-dirug`

**Fokus:** Online-Gründung der GmbH nach DiRUG ohne persoenlichen Notartermin: Voraussetzungen, Verfahren, Grenzen. Normen: § 2 Abs. 3 GmbHG, DiRUG. Prüfraster: Musterprotokoll-Pflicht, Videoidentifikation, Beschraenkungen. Output: Checkliste Online-Gründung mit Verfahrensschritten. Abgrenzung: nicht individuelle Satzung (erfordert Praesenz).

# Online-Gründung nach DiRUG

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Online-Gründung nach DiRUG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Online-Gründung

1. Ist es eine Bargründung — keine Sacheinlage? (Online-Gründung setzt Bareinlage voraus, § 2 Abs. 3 GmbHG.)
2. Sind alle Gesellschafter und GF mit Personalausweis (aktiviertes eID) oder kompatiblem Reisepass identifizierbar?
3. Handelt es sich um eine GmbH oder UG — keine AG?
4. Haben alle Teilnehmer stabile Internetverbindung, Kamera und Mikrofon?
5. Ist ein Test-Termin mit dem Notar vereinbart (empfohlen: 30 Min. vor Haupttermin)?
6. Sind ausländische Gründer beteiligt, deren Identifikation unklar ist?

## Zentrale Normen

- **§ 2 Abs. 3 GmbHG** — Online-Beurkundung: zulässig für GmbH- und UG-Gründungen; nur Bargründung.
- **§§ 16a-d BeurkG** — Online-Beurkundungsverfahren: technische Standards, qualifizierte elektronische Signatur, Identifikationsanforderungen.
- **§ 17 BeurkG** — Belehrungspflicht des Notars: gilt auch bei Online-Beurkundung; Notar muss Urkunde vorlesen und erläutern.
- **§ 40 BeurkG** — Online-Beglaubigungen: HR-Anmeldungen, Anteilsübertragungen auch online möglich.
- **§ 7 GmbHG** — Einzahlungspflicht: Stammkapital vollständig eingezahlt vor HR-Anmeldung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Online vs. Präsenz — Entscheidungsmatrix

| Kriterium | Online (DiRUG) | Präsenz |
|---|---|---|
| Gründungstyp | Nur Bargründung | Bar und Sachgründung |
| Gesellschaftsform | GmbH, UG | GmbH, UG, AG, GmbH & Co. KG |
| Identifikation | eID oder Reisepass-Online | Personalausweis im Original |
| Ortsunabhängig | Ja | Nein (Notar-Büro) |
| Ausländische Gründer | Oft Probleme | Apostille + Übersetzung |
| Komplexe Satzung | Eingeschränkter Diskussionsraum | Volle Beratung vor Ort |
| Kosten | Identisch (GNotKG) | Identisch (GNotKG) |
| Dauer Termin | 30-90 Minuten | 60-120 Minuten |

## Online-Gründungs-Ablauf

### Schritt 1: Notar auswählen und Termin buchen
- Notar muss Online-Gründung anbieten (nicht alle noch aktiviert).
- Termin 1-2 Wochen vorab; Notar übersendet Zugang zu Online-System.

### Schritt 2: Satzungsentwurf
- Wie bei physischer Gründung; Notar übersendet Vorabentwurf ca. 1 Woche vorher.

### Schritt 3: Test-Termin (empfohlen)
- Ca. 30 Min. vor Haupttermin: Technik-Check, Identifikationstest, eID-Test.

### Schritt 4: Haupttermin
- Notar im Büro; alle Gründer per Videokonferenz.
- Identifikation jedes Beteiligten per eID oder Reisepass-Online.
- Verlesen der Urkunde; Erläuterung; Rückfragen.
- Unterzeichnung per qualifizierter elektronischer Signatur (qeS).

### Schritt 5: HR-Anmeldung
- Notar reicht elektronisch an HR-Gericht ein; Beglaubigung online möglich.

### Schritt 6: Stammkapital einzahlen
- Nach Beurkundung: Einzahlung auf GmbH-Konto; Bankbestätigung an Notar.

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen oben beantworten; Online vs. Präsenz entscheiden.
2. **Notar suchen** — gesellschaftsrechtlich erfahren + Online-Gründung anbieten.
3. **Satzungsentwurf** — Vorabentwurf vom Notar einholen; sorgfältig prüfen.
4. **eID vorbereiten** — Personalausweis mit aktiviertem eID; Aktivierung im Bürgeramt (bis 2 Wochen warten).
5. **Test-Termin** — Technik, Identifikation, Kamera/Mikrofon testen.
6. **Haupttermin** — Satzung wird verlesen; qeS unterzeichnen.
7. **Stammkapital einzahlen** — Bankbestätigung an Notar schicken.
8. **HR-Eintragung abwarten** — ca. 2-4 Wochen; Gewerbeanmeldung + Finanzamt danach.

## Output-Template Checkliste Online-Gründung

**Adressat:** Gründer — Tonfall anleitend-verständlich
```
CHECKLISTE ONLINE-GRÜNDUNG (DiRUG)
Gesellschaft (geplant): [Firmenname] GmbH / UG
Online-Termin: [Datum, Uhrzeit]
Notar: [Name, Online-System-URL]

VORAUSSETZUNGEN PRÜFEN
[ ] Bargründung (keine Sacheinlage) — Ja
[ ] GmbH oder UG (kein AG) — Ja
[ ] Personalausweis mit eID aktiviert — alle Gesellschafter + GF: [ ] Ja
[ ] eID-Test im Bürgeramt: [ ] erledigt / [ ] ausstehend bis [Datum]
[ ] Stabile Internetverbindung (mind. 10 Mbit/s Upload): [ ] Ja
[ ] Kamera und Mikrofon funktionsfähig: [ ] Ja
[ ] Satzungsentwurf erhalten und geprüft am: [Datum]

AUSLÄNDISCHE BETEILIGTE
[ ] Ausländische Gesellschafter vorhanden: [ ] Nein / [ ] Ja → Identifikation klären
[ ] Identifikation per Reisepass-Online beim Notar möglich: [ ] Ja / [ ] Unklar

NACH BEURKUNDUNG
[ ] Stammkapital eingezahlt: [EUR] bis [Datum]
[ ] Bankbestätigung an Notar geschickt bis: [Datum]
[ ] HR-Eintragung erwartet: ca. [Datum + 2-4 Wochen]
[ ] Gewerbeanmeldung + Finanzamt nach HR-Eintragung
```

## Rote Schwellen

- Sacheinlage bei Online-Gründung → unzulässig; Bargründung zwingend.
- eID nicht aktiviert → Termin scheitert; Aktivierung rechtzeitig veranlassen (bis 2 Wochen).
- Internetverbindung bricht ab → Termin wird abgebrochen; neuer Termin erforderlich.
- Ausländischer Gründer ohne kompatibles Identifikationsdokument → Präsenz-Gründung nötig.
- AG-Gründung geplant → Online-Gründung nicht möglich.

## Quellen und Vertiefung

- §§ 2 Abs. 3, 7 GmbHG (Online-Beurkundung, Bareinzahlungspflicht)
- §§ 16a-d, 17, 40 BeurkG (Online-Beurkundungsverfahren, qeS)
- DiRUG vom 05.07.2021 (BGBl. I S. 3338)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Emmerich, GmbHG, § 2 Rn. 25-40

## Übergabe an andere Skills

- `gesellschaftsgruender-notar-vorbereitung` — Präsenz-Alternative
- `gesellschaftsgruender-handelsregister-anmeldung` — HR-Anmeldung nach Beurkundung
- `gesellschaftsgruender-stammkapital-einzahlung` — Einzahlung nach Online-Gründung
- `gesellschaftsgruender-gmbh-vorbereitung` — Vorbereitung vor Notartermin
