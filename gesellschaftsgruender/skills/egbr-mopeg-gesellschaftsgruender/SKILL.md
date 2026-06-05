---
name: egbr-mopeg-gesellschaftsgruender
description: "Egbr Mopeg Gesellschaftsgruender: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Egbr Mopeg Gesellschaftsgruender

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Egbr Mopeg Gesellschaftsgruender** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§ 707 ff. BGB Gesellschaftsregister. Prüfraster: Eintragungsvoraussetzungen, Gesellschafterverzeichnis, Vertretungsregeln, Haftungsfolgen. Output: eGbR-Gründungsunterlagen. Abgrenzung: nicht GmbH-Gründung mit Notar und HRB. |
| `gesellschaftsgruender-familiengesellschaft` | Prüft Familien-GbR/GmbH/KG für Vermögen, Nachfolge, Minderjährige und Stimmrechte. |
| `gesellschaftsgruender-finanzierungsrunde-seed` | Führt durch Seed-Runde: Term Sheet, Bewertung, Verwässerung, Cap Table, Satzung, SHA, Closing. |
| `gesellschaftsgruender-firmenname-pruefung` | Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 HGB, § 4 GmbHG. Prüfraster: Unterscheidungskraft, Irreführungsverbot, Handelsregisterfähigkeit, Markenrecherche-Empfehlung. Output: Prüfergebnis Firmenname mit Handlungsempfehlung. Abgrenzung: nicht Markenanmeldung beim DPMA. |
| `gesellschaftsgruender-founder-vesting` | Entwirft Founder-Vesting mit Cliff, Good/Bad Leaver und Rückübertragung. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Egbr Mopeg Gesellschaftsgruender**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-egbr-mopeg`

**Fokus:** GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§ 707 ff. BGB Gesellschaftsregister. Prüfraster: Eintragungsvoraussetzungen, Gesellschafterverzeichnis, Vertretungsregeln, Haftungsfolgen. Output: eGbR-Gründungsunterlagen. Abgrenzung: nicht GmbH-Gründung mit Notar und HRB.

# eGbR und GbR nach MoPeG 2024

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `eGbR und GbR nach MoPeG 2024` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere bei jedem eGbR-Mandat zuerst:

1. **Pflicht-Eintragung?** Grundstueckserwerb/-veraeusserung (Paragraf 707b BGB) oder GmbH-Anteilsbeteiligung (Paragraf 40 GmbHG)? Dann SOFORT Eintragung vor Notar-Termin.
2. **Innen-GbR oder Aussen-GbR?** Innen-GbR (kein Aussenauftritt): keine Pflicht. Aussen-GbR mit Rechtsverkehrsteilnahme: rechtsfaehig nach Paragraf 705 II BGB.
3. **Handelsgeschaeft oder Freiberuf?** OHG fuer Kaufleute; eGbR fuer Nicht-Kaufleute und Freiberufler.
4. **Haftungsbeschraenkung gewuenscht?** eGbR schafft keine Haftungsbeschraenkung; fuer begrenzte Haftung -> GmbH oder KG.
5. **Zeitrahmen?** Eintragung beim Amtsgericht dauert 2-6 Wochen; Notar-Termin fuer Grundstuecksgeschaeft erst nach Eintragung.
6. **Bestehendes Grundbuch-Eintrag "GbR bestehend aus A, B, C"?** Muss auf eGbR umgestellt werden.

## Zentrale Normen

- **§ 705 II BGB** — Rechtsfaehige GbR bei Teilnahme am Rechtsverkehr; gesetzliche Anerkennung
- **§ 707 BGB** — Freiwillige Eintragung in das Gesellschaftsregister (eGbR)
- **§ 707a II BGB** — Pflicht-Namenszusatz "eGbR" / "eingetragene Gesellschaft buergerlichen Rechts"
- **§ 707a III BGB** — Vertrauensschutz Dritter auf Registerpublizitaet (analog Paragraf 15 HGB)
- **§ 707b BGB** — Pflicht-Eintragung bei Grundstuecksgeschaeften; Grundbuchverfahren
- **§ 720 I BGB** — Grundsatz der Gesamtvertretung; Satzungsabweichung moeglich
- **§ 721 BGB** — Gesamtschuldnerische Aussenhaftung aller Gesellschafter (unbeschraenkt)
- **§ 723 BGB** — Fortbestand der Gesellschaft bei Ausscheiden eines Gesellschafters (Kernneuerung MoPeG)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: eGbR-Eintragungsentscheidung

| Schritt | Frage | Norm | Ergebnis |
|---|---|---|---|
| 1 | Aussen-GbR mit Rechtsverkehrsteilnahme? | § 705 II BGB | Ja: rechtsfaehig. Nein: Innen-GbR |
| 2 | Grundstuecksgeschaeft geplant? | § 707b BGB | Ja: Pflicht-Eintragung VOR Notar-Termin |
| 3 | GmbH-Anteilsbeteiligung? | § 40 GmbHG | Ja: eGbR-Eintragung Voraussetzung |
| 4 | Handelsgeschaeft? | § 1 HGB | Ja: OHG statt eGbR (Handelsregister) |
| 5 | Haftungsbeschraenkung gewuenscht? | § 721 BGB | eGbR bietet keine; GmbH/KG pruefen |
| 6 | Vertrauensschutz fuer Geschaeftspartner gewuenscht? | § 707a III BGB | Eintragung schafft Publizitaet |
| 7 | Bestehendes Grundbuch auf alte GbR? | § 47 GBO | Umschreibung auf eGbR nach Eintragung |

## Schritt-fuer-Schritt-Workflow

1. **Qualifikation:** Innen-GbR oder Aussen-GbR? Handelsgeschaeft oder nicht? Freiberufler-Sozietaet?
2. **Pflicht pruefen:** Grundstueck oder GmbH-Anteil betroffen? Dann Eintragung zwingend.
3. **Gesellschaftsvertrag entwerfen** (formfrei, aber schriftlich empfohlen): Gegenstand, Einlagen, Vertretung, Gewinnverteilung, Ausscheiden, Fortbestandsklausel (§ 723 BGB).
4. **Anmeldung beim Amtsgericht:** Alle Gesellschafter; notarielle Beglaubigung der Unterschriften; Gebuehr ca. 80-150 EUR.
5. **Eintragung abwarten:** Veröffentlichung im Bundesanzeiger; Namenszusatz "eGbR" ab sofort zu fuehren.
6. **Grundbuch-Umschreibung:** Bei bestehendem Grundbuch-Eintrag auf alte GbR: Berichtigungsantrag stellen.
7. **Folge-Anmeldungen:** Gewerbeamt, Finanzamt, Transparenzregister (§ 20 GwG).
8. **Gesellschafterwechsel:** Bei Eintritt / Ausscheiden: Registeraenderung + ggf. neuer Grundbucheintrag.

## Output-Template: Anmeldung eGbR

**Adressat:** Amtsgericht (Gesellschaftsregister) — Tonfall sachlich-formal

```
An das Amtsgericht [ORT]
— Gesellschaftsregister —

Anmeldung der eingetragenen Gesellschaft buergerlichen Rechts (eGbR)
nach § 707 BGB

Wir, die unterzeichneten Gesellschafter der Gesellschaft buergerlichen
Rechts, melden zur Eintragung in das Gesellschaftsregister an:

1. Name: [GESELLSCHAFTSNAME] eGbR
2. Sitz: [ADRESSE]
3. Gegenstand: [GEGENSTAND]
4. Gesellschafter:
 a) [NAME 1], geb. [DATUM], [ADRESSE]
 b) [NAME 2], geb. [DATUM], [ADRESSE]
5. Vertretungsbefugnis: [Gesamtvertretung / Einzelvertretung gemaess
 Gesellschaftsvertrag § X]

Anlagen:
- Gesellschaftsvertrag vom [DATUM]
- Notarielle Beglaubigungs-Urkunde Nr. [NR.]

[ORT], [DATUM]
Unterschriften aller Gesellschafter (notariell beglaubigt)
```

## Rote Schwellen

- Grundstueckskauf ohne eGbR-Eintragung: Auflassung scheitert; Notartermin nicht durchfuehrbar. Hinweis: BGH-Linie ueber das Voreintragungserfordernis nach MoPeG ist mittlerweile durch erste obergerichtliche und BGH-Entscheidungen gefestigt (siehe Vertiefung). Konkrete Aktenzeichen vor Verwendung live verifizieren.
- Namenszusatz "eGbR" vergessen nach Eintragung: Ordnungswidrigkeit; Haftungsfolgen
- Eintragung = Haftungsbeschraenkung: FALSCH. Alle Gesellschafter haften weiter unbeschraenkt (§ 721 BGB)
- GbR als GmbH-Gesellschafter ohne eGbR: Eintragung in Gesellschafterliste nicht moeglich (§ 40 GmbHG)

## Quellen und Vertiefung

- §§ 705-740 BGB (MoPeG-Fassung ab 01.01.2024): https://www.gesetze-im-internet.de/bgb/__705.html
- §§ 707, 707a, 707b BGB (Gesellschaftsregister; Voreintragungserfordernis Grundstuecksgeschaefte): https://www.gesetze-im-internet.de/bgb/__707.html
- §§ 720, 721, 723, 728b BGB: https://www.gesetze-im-internet.de/bgb/__721.html
- § 40 GmbHG (Gesellschafterliste; eGbR-Eintragung als Voraussetzung der Listung als Gesellschafterin): https://www.gesetze-im-internet.de/gmbhg/__40.html
- MoPeG (BGBl. I 2021, 3436): https://www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger_BGBl&start=//*[@attr_id=%27bgbl121s3436.pdf%27]
- BGH, Beschl. v. 03.07.2025 — V ZB 17/24 (Voreintragung der GbR im Gesellschaftsregister vor Grundbuchaenderung; ECLI:DE:BGH:2025:030725BVZB17.24.0): https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=142513
- Weitere obergerichtliche Linien zur Firmierung "eGbR" und identitaetswahrenden Umwandlung GbR -> KG/OHG (Beispiele aus 2024, vor Verwendung Aktenzeichen pruefen):
 - OLG Hamburg, Beschl. v. 22.04.2024 — 11 W 19/24
 - OLG Koeln, Beschl. v. 22.04.2024 — 4 Wx 4/24
 - OLG Muenchen, Beschl. v. 2024 — 34 Wx 71/24 e
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Uebergabe an andere Skills

- `gesellschaftsgruender-rechtsformwahl` — Vergleich zu anderen Formen (GmbH, KG, OHG)
- `gesellschaftsgruender-handelsregister-anmeldung` — bei Umwandlung in OHG
- `gesellschaftsgruender-transparenzregister` — wirtschaftlich Berechtigte
- `gesellschaftsgruender-kommandocenter` — Gesamtablauf

## 2. `gesellschaftsgruender-familiengesellschaft`

**Fokus:** Prüft Familien-GbR/GmbH/KG für Vermögen, Nachfolge, Minderjährige und Stimmrechte.

# Familiengesellschaft und Nachfolge

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Familiengesellschaft und Nachfolge` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Route zu Erbrecht/Steuer.

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

## 3. `gesellschaftsgruender-finanzierungsrunde-seed`

**Fokus:** Führt durch Seed-Runde: Term Sheet, Bewertung, Verwässerung, Cap Table, Satzung, SHA, Closing.

# Seed-Finanzierungsrunde

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Seed-Finanzierungsrunde` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Anfängerfreundlich mit Begriffsübersetzung.

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

## 4. `gesellschaftsgruender-firmenname-pruefung`

**Fokus:** Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 HGB, § 4 GmbHG. Prüfraster: Unterscheidungskraft, Irreführungsverbot, Handelsregisterfähigkeit, Markenrecherche-Empfehlung. Output: Prüfergebnis Firmenname mit Handlungsempfehlung. Abgrenzung: nicht Markenanmeldung beim DPMA.

# Firmenname-Prüfung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Firmenname-Prüfung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere mindestens 2 Wochen vor Notar-Termin:

1. **3-5 Wunsch-Firmen bereit?** Immer Alternativen vorbereiten; Plan A kann beanstandet werden.
2. **Branchenbezeichnung im Namen?** Pruefen ob Zulassung erforderlich (Bank: BaFin; Steuer: StBerG; Rechts: RAK).
3. **Personenname im Firmennamen?** Eigener Name: unproblematisch; fremder Name: Berechtigung pruefen (§ 12 BGB).
4. **Marken-Relevanz?** Bei Startup oder Brand mit Aussenauftritt: DPMA/EUIPO-Recherche vor Eintragung.
5. **Internationale Aktivitaet?** Bedeutung des Namens in Zielmaerkten pruefen; schwer aussprechbare Namen vermeiden.
6. **Domain bereits gesichert?** Domain VOR Notar-Termin sichern; nachtraeglich oft nicht mehr verfuegbar.

## Zentrale Normen

- **§ 17 HGB** — Firma ist der Name, unter dem Kaufmann im Handelsverkehr auftritt
- **§ 18 I HGB** — Kennzeichnungsgeeignetheit der Firma
- **§ 18 II HGB** — Irreführungsverbot; keine Firma, die zur Taeuschung geeignet ist
- **§ 19 HGB** — Pflicht-Rechtsform-Zusatz (GmbH, AG, OHG, KG usw.)
- **§ 30 HGB** — Verwechslungsgefahr; am Ort Pflicht zur Unterscheidbarkeit von bestehenden Firmen
- **§ 12 BGB** — Namensrecht; Schutz des Namensrechts bei Verwendung fremder Namen
- **§ 14 MarkenG** — Verletzung einer eingetragenen Marke durch Firmenname; Unterlassungsanspruch

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Firmennamen-Check

| Schritt | Pruefung | Stelle | Ergebnis |
|---|---|---|---|
| 1 | Handelsregister-Suche bundesweit | gemeinsam.handelsregister.de | Konflikt? Wenn ja, Name anpassen |
| 2 | IHK-Firmenvorpruefung beantragt | Oertliche IHK | Bescheinigung erhalten? |
| 3 | Kennzeichnungseignung geprueft | Selbst / Anwalt | Nicht generisch; Unterscheidungskraft vorhanden |
| 4 | Irrefuehrungs-Check | Selbst | Keine falsche Branchenangabe; keine Zulassungs-Vortaeuschung |
| 5 | Rechtsform-Zusatz vorhanden | Selbst | GmbH / UG / AG / OHG explizit angegeben |
| 6 | DPMA-Marken-Recherche | dpma.de | Kein identischer / aehnlicher Markenname |
| 7 | EUIPO-Marken-Recherche | euipo.europa.eu | EU-Marken-Konflikt? |
| 8 | Domain .de gesichert | DENIC / Registrar | Verfuegbar und gesichert VOR Notar |
| 9 | Domain .com gesichert | Registrar | Verfuegbar und gesichert |
| 10 | Personenname-Berechtigung | Selbst | Eigener Name oder nachgewiesene Berechtigung |
| 11 | Branchenbezeichnung-Zulassung | Berufsrecht | Bank, Steuer, Rechts, Arzt: Zulassung geprueft |
| 12 | Internationale Bedeutung geprueft | Selbst | Keine negativen Konnotationen in Zielmaerkten |

## Schritt-fuer-Schritt-Workflow

1. **T-14 (2 Wochen vor Notar):** 3-5 Wunsch-Namen listen; HR-Suche nationwide; DPMA-Stichprobe.
2. **T-10:** IHK-Vorpruefung beantragen (oft binnen 2-5 Werktagen); Domain-Verfuegbarkeit pruefen.
3. **T-7:** IHK-Bescheinigung liegt vor; Domain bei Verfuegbarkeit SOFORT sichern; ggf. Marken-Anmeldung einleiten.
4. **T-3:** Alle Alternativen bereit halten; Marken-Recherche abgeschlossen.
5. **T (Notar-Termin):** Beurkundung mit gewaehltem Namen; IHK-Bescheinigung dem Notar vorlegen.
6. **T+5 bis T+14 (HR-Pruefung):** HR-Gericht prueft; bei Beanstandung: Satzungsaenderung und erneute Beurkundung (Kosten ca. 300-600 EUR).
7. **Nach Eintragung:** Marken-Anmeldung auf Gesellschaft umschreiben (falls zuvor auf Gruender angemeldet).

## Output-Template: Firmenname-Pruefprotokoll

**Adressat:** Interne Dokumentation / Anwaltsakte

```
FIRMENNAME-PRUEFPROTOKOLL
Mandant: [NAME] | Datum: [DATUM] | Notar-Termin: [DATUM]

Gewuenschte Firmennamen (Prioritaetsreihenfolge):
1. [NAME 1] GmbH
2. [NAME 2] GmbH
3. [NAME 3] GmbH

Pruef-Ergebnisse:

| Pruefung | Name 1 | Name 2 | Name 3 |
|---------------------------|-------------|-------------|-------------|
| HR-Suche (HR-Bezirk) | OK / Konflikt| OK / Konflikt| OK / Konflikt|
| IHK-Vorpruefung | Bestätigt | Ausstehend | - |
| DPMA Marken | OK | Konflikt | OK |
| EUIPO Marken | OK | OK | OK |
| Domain .de | Gesichert | Vergeben | Verfuegbar |
| Domain .com | Verfuegbar | Vergeben | Verfuegbar |
| Irrefuehrungs-Check | OK | - | - |
| Branchenbezeichnung-Zulass.| n/a | - | - |

Empfehlung: [NAME 1] GmbH (keine Konflikte, Domain gesichert)
Fallback: [NAME 3] GmbH

Naechste Schritte:
[ ] IHK-Bescheinigung fuer [NAME 1] einholen
[ ] Domain [name1].de registriert am [DATUM]
[ ] Marken-Anmeldung DPMA fuer [NAME 1] einleiten?
```

## Rote Schwellen

- Branchenbezeichnung "Bank", "Versicherung", "Steuerberatung" ohne Zulassung: Beanstandung und Ordnungswidrigkeitsverfahren
- Verwechslungsgefahr mit bestehender Firma im Registerbereich: Beanstandung HR-Gericht (§ 30 HGB)
- Fremder Name ohne Berechtigung: Namensklage nach § 12 BGB; Unterlassung und Schadenersatz
- Marken-Verletzung durch Firmennamen: Unterlassungsklage; Umfirmierungspflicht; erhebliche Kosten

## Quellen und Vertiefung

- §§ 17-30 HGB (Firmenrecht), § 12 BGB, § 14 MarkenG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Uebergabe an andere Skills

- `gesellschaftsgruender-gmbh-vorbereitung` — Firmenname als Baustein der Vorbereitung
- `gesellschaftsgruender-notar-vorbereitung` — IHK-Bescheinigung vorlegen
- `gesellschaftsgruender-handelsregister-anmeldung` — HR-Pruefung durch Registergericht

## 5. `gesellschaftsgruender-founder-vesting`

**Fokus:** Entwirft Founder-Vesting mit Cliff, Good/Bad Leaver und Rückübertragung.

# Founder Vesting

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Founder Vesting` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Satzung/SHA/Arbeitsvertrag verbinden.

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
