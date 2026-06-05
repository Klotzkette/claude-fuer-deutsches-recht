---
name: gesellschaftsgruender-gmbh-vorbereitung
description: "Gmbh Vorbereitung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gmbh Vorbereitung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Gmbh Vorbereitung** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-gmbh-vorbereitung` | GmbH-Gründung vorbereiten: Gründerprüfung, Kapitalplanung, Notar-Auftrag, Gesellschafterliste. Normen: §§ 2 3 5 7 GmbHG. Prüfraster: Mindestkapital 25000 Euro, Einzahlungsnachweis, Gesellschafterkreis, Geschäftsführereignung. Output: Vorbereitungscheckliste GmbH-Gründung. Abgrenzung: nicht UG-Gründung (eigener Skill). |
| `gesellschaftsgruender-golden-share-und-vetorechte` | Golden Shares und Vetorechte in GmbH oder AG satzungsmäßig absichern: Sonderrechte, Sperrminoritaeten. Normen: §§ 35 45 GmbHG, §§ 23 ff. AktG. Prüfraster: Satzungsgestaltung, Grenzen der Satzungsautonomie, Bestandsschutz, Vinkulierung. Output: Satzungsklausel Golden Share und Vetorechte. Abgrenzung: nicht Gesellschaftervereinbarung (nur schuldrechtlich). |
| `gesellschaftsgruender-gruenderrollen-konfliktcheck` | Klärt Rollen, Beiträge, Erwartungen, Streitpunkte und Exit-Szenarien vor Satzungsentwurf. |
| `gesellschaftsgruender-gv-einladung-tagesordnung` | Gesellschafterversammlungs-Einladung und Tagesordnung nach GmbHG erstellen: Fristen, Formen, Mindestinhalt. Normen: §§ 49 51 GmbHG. Prüfraster: Ladungsfrist, Schriftform, Tagesordnungspunkte, Beschlussfähigkeit. Output: GV-Einladungsschreiben mit Tagesordnung. Abgrenzung: nicht GV-Protokoll. |
| `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` | Gesellschafterversammlungs-Protokoll anfertigen und Versammlungsleitung durchführen. Normen: §§ 48 ff. GmbHG. Prüfraster: Protokollierungspflicht, Abstimmungsergebnis, Unterschriften, Formfehler. Output: GV-Protokoll-Vorlage. Abgrenzung: nicht GV-Einladung und Tagesordnung. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Gmbh Vorbereitung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-gmbh-vorbereitung`

**Fokus:** GmbH-Gründung vorbereiten: Gründerprüfung, Kapitalplanung, Notar-Auftrag, Gesellschafterliste. Normen: §§ 2 3 5 7 GmbHG. Prüfraster: Mindestkapital 25000 Euro, Einzahlungsnachweis, Gesellschafterkreis, Geschäftsführereignung. Output: Vorbereitungscheckliste GmbH-Gründung. Abgrenzung: nicht UG-Gründung (eigener Skill).

# GmbH-Vorbereitung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `GmbH-Vorbereitung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Notarsitzung

1. Wie viele Gesellschafter — Solo, Paar oder Team? Bei bis zu 3 Gesellschaftern und einem GF: Musterprotokoll möglich.
2. Stammkapital: Bargründung oder Sachgründung? Sacheinlage erfordert Sachgründungsbericht (§ 5 Abs. 4 GmbHG) und löst Differenzhaftung (§ 9 GmbHG) aus.
3. Ist eine Holding-Struktur sinnvoll (Gesellschafter hält über UG/GmbH Holding statt direkt)?
4. Ist Investoren-Aufnahme in den nächsten 12-24 Monaten geplant — dann individuelle Satzung, nicht Musterprotokoll.
5. Liegt ein genehmigungspflichtiger Unternehmensgegenstand vor (Bank, Versicherung, Spielhalle, Apotheke)?
6. Sind alle Gesellschafter und Geschäftsführer persönlich anwesend oder werden Vollmachten benötigt?

## Zentrale Normen

- **§ 5 GmbHG** — Stammkapital mindestens 25.000 EUR; Mindestbetrag je Anteil 1 EUR; Sachgründung erfordert Sachgründungsbericht.
- **§ 5a GmbHG** — UG-Sondervariante (Mindestkapital 1 EUR; Thesaurierungspflicht 25 %).
- **§ 7 GmbHG** — Anmeldevoraussetzungen: Einzahlung mindestens 12.500 EUR (Bargründung) bzw. volle Sacheinlage.
- **§ 9 GmbHG** — Differenzhaftung: Gesellschafter haftet für den Wertunterschied, wenn Sacheinlage unter angemeldeten Wert liegt.
- **§§ 17 ff. HGB / § 30 HGB** — Firmenbildung: Kennzeichnungskraft, keine Irreführung, keine Verwechslungsgefahr.
- **§ 53 Abs. 2 GmbHG** — Satzungsänderung erfordert 75 %-Mehrheit.
- **§§ 2, 2a GmbHG** — Beurkundungsform; Musterprotokoll bei einfachen Gründungen.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Sieben-Bausteine-Prüfschema

| Baustein | Kernfrage | Fallstrick | Ergebnis |
|---|---|---|---|
| 1 Firma | IHK-Vorprüfung, Verwechslungsgefahr (§ 30 HGB), DPMA-Markencheck | Ähnliche Firma im HR-Bezirk → Eintragungsversagung | Firma freigegeben |
| 2 Sitz | Satzungssitz Inland; ladungsfähige Geschäftsadresse | Briefkasten-Sitz unzulässig; tatsächliche Erreichbarkeit | Sitz bestätigt |
| 3 Gegenstand | § 3 Abs. 1 Nr. 2 GmbHG: konkret genug, weit genug | Zu eng: Pivot erfordert Satzungsänderung; zu veit: HR-Beanstandung | Gegenstand formuliert |
| 4 Stammkapital | Bar oder Sach? 25.000 EUR Minimum; Einzahlung 12.500 EUR vor Anmeldung | Sacheinlage: Differenzhaftung § 9 GmbHG | Kapitalstruktur festgelegt |
| 5 Gesellschafter | Quoten; Mehrheit; 75-%-Schwelle für Satzungsänderung; Holding-Überlegung | Falsche Quotenplanung vor Investoren-Runde | Gesellschafterstruktur fixiert |
| 6 Geschäftsführer | Einzel- oder Gesamtvertretung; § 181 BGB Befreiung; Anstellungsvertrag | GF ohne Anstellungsvertrag = unklares SV-Verhältnis | GF-Parameter festgelegt |
| 7 Satzungswahl | Musterprotokoll (§ 2a GmbHG, max. 3 Gesellschafter) oder individuelle Satzung | Musterprotokoll bei Investoren-Plan: teure Nachänderung | Satzungstyp gewählt |

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen oben beantworten; Gründungs-Typ bestimmen.
2. **Firmencheck** — IHK-Vorprüfung; HR-Recherche; DPMA-Markenrecherche; Domain-Check.
3. **Kapitalstruktur** — Bar oder Sach? Einzahlungsplan; Konto eröffnen; bei Sacheinlage Sachgründungsbericht beauftragen.
4. **Gesellschafterstruktur** — Quoten festlegen; Holding-Frage klären; Vesting/Vorkaufsrecht in individuelle Satzung.
5. **Satzungsentwurf** — Musterprotokoll oder individuelle Satzung; GF-Parameter (Vertretung, § 181 BGB).
6. **Notartermin** — Unterlagen-Checkliste abarbeiten (siehe unten); alle Anwesenden mit Personalausweis.
7. **Einzahlung** — nach Beurkundung: Stammkapital auf Gesellschaftskonto; Einzahlungsbeleg an Notar.
8. **HR-Anmeldung** — Notar meldet beim Handelsregister an; bei genehmigungspflichtigem Gegenstand: Genehmigung vorlegen.
9. **Folgeakte** — Gewerbeanmeldung, Finanzamt-Fragebogen, IHK-Mitgliedschaft, Transparenzregister (sofern nicht bereits eingetragen).

## Output-Template Notarcheckliste

**Adressat:** Gründer und Mandant — Tonfall verständlich-erklärend
```
NOTARCHECKLISTE GMBH-GRÜNDUNG
Mandant: [Name(n) der Gründer]
Firma (geplant): [Firmenname] GmbH
Notartermin: [Datum, Uhrzeit, Ort]
Erstellt: [Datum]

VOR DEM TERMIN — bitte mitbringen
[ ] Gültiger Personalausweis / Reisepass — alle Gesellschafter + GF
[ ] Bei GmbH als Gesellschafterin: Handelsregisterauszug (max. 3 Monate alt) + Vollmacht GF
[ ] Nachweis Firmennamen-Vorprüfung (IHK-Bescheinigung, sofern eingeholt)
[ ] Formulierte Satzung / Musterprotokoll-Variante (vom Anwalt vorbereitet)
[ ] Gegenstand des Unternehmens — exakter Wortlaut
[ ] Gesellschafterliste mit Quoten und Adresse
[ ] Anschrift des Geschäftssitzes (ladungsfähig)
[ ] Bei Sachgründung: Sachgründungsbericht, Sachwertgutachten
[ ] Genehmigungsunterlagen (sofern genehmigungspflichtiger Gegenstand)

NACH DER BEURKUNDUNG — nächste Schritte
[ ] Stammkapital auf neu eröffnetes GmbH-Konto einzahlen ([BETRAG] EUR)
[ ] Einzahlungsbeleg an Notar schicken bis [Datum]
[ ] Handelsregisteranmeldung — Notar veranlasst
[ ] Geschäftskonto-Eröffnung (Firmenname + HR-Nummer nach Eintragung)
[ ] Gewerbeanmeldung — zuständige Behörde: [Ordnungsamt/Gewerbeamt ORTS]
[ ] Fragebogen zur steuerlichen Erfassung — Finanzamt [Finanzamt ORT]
[ ] Transparenzregister — wirtschaftlich Berechtigte eintragen (TraFinG)
[ ] GF-Anstellungsvertrag abschließen (separat)

GESELLSCHAFTERSTRUKTUR
| Gesellschafter | Quote | Anteil-EUR | Einzahlung | Bareinlage/Sacheinlage |
|---------------|-------|-----------|-----------|----------------------|
| [Name 1] | [%] | [EUR] | [Datum] | Bar |
| [Name 2] | [%] | [EUR] | [Datum] | Bar |

GESCHÄFTSFÜHRER
Name: [GF-Name]
Vertretung: [Einzelvertretung / Gesamtvertretung]
§ 181 BGB Befreiung: [Ja / Nein]
Anstellungsvertrag: [vorhanden / noch abzuschließen]
```

## Rote Schwellen

- Sacheinlage ohne Sachgründungsbericht → HR verweigert Eintragung; persönliche Differenzhaftung (§ 9 GmbHG).
- Firma nicht vorab geprüft → Eintragungsversagung durch Handelsregister; Verzögerung 4-8 Wochen.
- Musterprotokoll bei geplantem Investoren-Einstieg → spätere Satzungsänderung kostet mehr als initiale individuelle Satzung.
- Stammkapital nicht vollständig eingezahlt vor Anmeldung → Anmeldevoraussetzung fehlt; persönliche Haftung GF.
- Genehmigungspflichtiger Gegenstand ohne Genehmigung → Eintragung verzögert oder verweigert.

## Typische Gründungsfehler

1. Firmenname nicht geprüft → Marken- oder HR-Konflikt nach Eintragung.
2. Geschäftsgegenstand zu eng → Pivot erfordert 75-%-Satzungsänderung.
3. Musterprotokoll bei Investoren-Plänen → Nachänderung teuer.
4. GF-Anstellungsvertrag vergessen → unklares Sozialversicherungsverhältnis.
5. Holding-Frage zu spät → spätere Umstrukturierung teuer (Grunderwerbsteuer, GrESt-Klausel).
6. § 181 BGB-Befreiung vergessen → In-sich-Geschäfte des GF schwebend unwirksam.

## Quellen und Vertiefung

- §§ 2, 5, 7, 9, 53 GmbHG (Gründung, Stammkapital, Differenzhaftung, Satzungsänderung)
- §§ 17-18, 30 HGB (Firmenrecht, Verwechslungsgefahr)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Emmerich, GmbHG, § 5 Rn. 1-50
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Übergabe an andere Skills

- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — individuelle Satzung ausarbeiten
- `gesellschaftsgruender-geschaeftsfuehrervertrag` — GF-Anstellungsvertrag
- `gesellschaftsgruender-notar-vorbereitung` — Notarsitzung vorbereiten
- `gesellschaftsgruender-stammkapital-einzahlung` — Einzahlungsnachweis
- `gesellschaftsgruender-handelsregister-anmeldung` — HR-Eintragungsablauf
- `gesellschaftsgruender-online-gruendung-dirug` — DiRUG-Online-Gründung

## 2. `gesellschaftsgruender-golden-share-und-vetorechte`

**Fokus:** Golden Shares und Vetorechte in GmbH oder AG satzungsmäßig absichern: Sonderrechte, Sperrminoritaeten. Normen: §§ 35 45 GmbHG, §§ 23 ff. AktG. Prüfraster: Satzungsgestaltung, Grenzen der Satzungsautonomie, Bestandsschutz, Vinkulierung. Output: Satzungsklausel Golden Share und Vetorechte. Abgrenzung: nicht Gesellschaftervereinbarung (nur schuldrechtlich).

# Golden Share und Sondervetorechte

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Golden Share und Sondervetorechte` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere vor Gestaltung von Vetorechten:

1. **Wessen Schutz?** Gruender gegen Investoren, Investor gegen Gruender, Familie gegen Nachfolger-Generation?
2. **Umfang des Vetorechts?** Voller Block (alle Beschluesse) oder selektive Themen (Restrukturierung, Satzungsaenderung, Verkauf)?
3. **Personenbezogen oder anteilsbezogen?** Personenbezogenes Vetorecht erlischt bei Anteilsabtretung; anteilsbezogenes geht mit dem Anteil ueber.
4. **Insolvenzantragspflicht bekannt?** § 15a InsO: Pflicht des GF antragzustellen unabhaengig von Golden Share — Vetorecht entbindet GF NICHT.
5. **Sitzverteilung im Beirat?** Gruender-Schutz kann auch ueber Beirats-Veto statt Golden Share strukturiert werden.
6. **Handelsregister-Publikation?** Satzungsklausel wird mit Satzung beim HR hinterlegt; oeffentlich.

## Zentrale Normen

- **§ 3 II GmbHG** — Satzungsautonomie; Sonderrechte und Vorzugsklassen zulässig
- **§ 47 GmbHG** — Beschlussfassung; Mehrheitsprinzip; Abweichung durch Satzung moeglich
- **§ 47 IV GmbHG** — Stimmverbot bei Eigen-Interesse; gilt auch fuer Vetorechts-Inhaber
- **§ 15a InsO** — Insolvenzantragspflicht des GF; wird durch Gesellschafter-Veto nicht beseitigt
- **§ 31 StaRUG** — Antrag auf Restrukturierungsverfahren; freiwillig; Veto-Klausel hier wirksam
- **§§ 133, 157 BGB** — Auslegung von Satzungs-Vetoklauseln bei Streit
- **§ 138 BGB** — Sittenwidrigkeit: Veto ueber alle Beschluesse kann nichtig sein

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Golden Share-Gestaltung

| Schritt | Frage | Norm | Ergebnis |
|---|---|---|---|
| 1 | Personenbezogen oder anteilsbezogen? | § 15 GmbHG | Bei Anteilsabtretung: erlischt oder geht ueber? |
| 2 | Umfang sachlich begrenzt? | § 138 BGB | Kein Pauschal-Veto; selektive Themen |
| 3 | Stimmverbot bei Eigeninteresse beachtet? | § 47 IV GmbHG | Veto-Inhaber bei Eigen-Sache: kein Stimmrecht |
| 4 | Insolvenzantragspflicht gecheckt? | § 15a InsO | GF muss bei Insolvenzreife stellen; Veto greift nicht |
| 5 | StaRUG-Veto sinnvoll? | § 31 StaRUG | Freiwilliges Verfahren; Veto hier wirksam |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 7 | SHA-Stimmverpflichtung ergaenzend? | § 242 BGB | Schuldrechtliche Sicherung bei Verstoss |

## Schritt-fuer-Schritt-Workflow

1. **Schutzinteresse definieren:** Wen schuetzen wir (Gruender, Investor, Familie) und wovor?
2. **Katalog der Veto-Themen festlegen:** Selektiv; maximal 5-8 klar definierte Anlaesse.
3. **Satzungs-Klausel entwerfen:** Personenbezogen vs. anteilsbezogen; Erloesch-Klausel formulieren.
4. **§ 15a InsO-Warnung einbauen:** Explizit im Vertrag und Erlaeuterungsprotokoll dokumentieren, dass Insolvenzantragspflicht des GF unberuehrt bleibt.
5. **SHA-Stimmverpflichtung** als schuldrechtliche Ergaenzung: fuer Faelle, die satzungsmaessig nicht erfasst sind.
6. **Notar-Beurkundung** der Satzungsaenderung (bei Verankerung in Satzung).
7. **Monitoring:** Jaehrliche Pruefung ob Veto-Klausel noch zum Unternehmens-Stadium passt.

## Output-Template: Satzungs-Klausel Golden Share

**Adressat:** Gesellschaftsvertrag / Satzungsaenderung — Tonfall praezise

```
§ [X] Sondervetorecht (Golden Share)

(1) Die Inhaberin / Der Inhaber des Anteils Nr. [N]
([NAME], geb. [DATUM]) hat zusaetzlich zu den
allgemeinen Stimmrechten ein Sondervetorecht.
Folgende Beschluesse beduerfen ihrer / seiner
ausdruecklichen Zustimmung:

a) Aenderung der Satzung;
b) Wesentliche Aenderung des Unternehmensgegenstands;
c) Veraeusserung von mehr als 20 % des
 Bilanzvermoegens;
d) Stellung eines Antrags auf Restrukturierungs-
 verfahren nach § 31 StaRUG;
e) Aufloesung der Gesellschaft;
f) Aufnahme neuer Gesellschafter mit Sonderrechten.

(2) Die Insolvenzantragspflicht der Geschaeftsfuehrung
nach § 15a InsO bleibt von Abs. 1 lit. d) unberuehrt.
Das Sondervetorecht entbindet die Geschaeftsfuehrung
nicht von der gesetzlichen Antragspflicht.

(3) Das Sondervetorecht ist personenbezogen und
nicht uebertragbar. Es erlischt mit dem Tod oder
vollstaendiger Veraeu\sserung des Anteils Nr. [N].

(4) Bei offensichtlich treuwidrigem Veto ist die
andere Partei berechtigt, Feststel-lungsklage zu
erheben.
```

## Rote Schwellen

- Veto in der Insolvenzsituation: GF MUSS nach § 15a InsO stellen; Veto schuetzt GF nicht vor Strafbarkeit
- Pauschal-Veto ueber alle Beschluesse: Nichtigkeit nach § 138 BGB moeglich (OLG Frankfurt 2021)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Personenbezogenes Veto bei Erbfall: pruefen ob Erben das Vetorecht erben sollen oder es erloeschen soll

## Quellen und Vertiefung

- §§ 3, 47, 47 IV GmbHG; §§ 138, 242 BGB; § 15a InsO; § 31 StaRUG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-share-classes-a-b-c` — Verbindung mit Klassen-Strukturen
- `gesellschaftsgruender-sha-satzung-stimmverpflichtung` — Stimmverpflichtungs-Klauseln
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Konfliktfall; einstweilige Verfuegung
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Satzungs-Gestaltung

## 3. `gesellschaftsgruender-gruenderrollen-konfliktcheck`

**Fokus:** Klärt Rollen, Beiträge, Erwartungen, Streitpunkte und Exit-Szenarien vor Satzungsentwurf.

# Gründerrollen und Konfliktcheck

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gründerrollen und Konfliktcheck` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Erfasse Geld, Arbeit, IP, Netzwerk, Vesting, Krankheit, Kündigung, Deadlock.

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

## 4. `gesellschaftsgruender-gv-einladung-tagesordnung`

**Fokus:** Gesellschafterversammlungs-Einladung und Tagesordnung nach GmbHG erstellen: Fristen, Formen, Mindestinhalt. Normen: §§ 49 51 GmbHG. Prüfraster: Ladungsfrist, Schriftform, Tagesordnungspunkte, Beschlussfähigkeit. Output: GV-Einladungsschreiben mit Tagesordnung. Abgrenzung: nicht GV-Protokoll.

# Einladung zur Gesellschafterversammlung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Einladung zur Gesellschafterversammlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere vor Erstellung der Einladung:

1. **Ordentliche oder ausserordentliche GV?** Ordentliche: jaehrliche Pflichtversammlung (§ 42a GmbHG); ausserordentliche: anlassbezogen.
2. **Wer ist einberufungsberechtigt?** GF (§ 49 I GmbHG); Gesellschafter mit ≥ 10 % (§ 50 GmbHG); sonst: Amtsgericht anrufen.
3. **Welche Fristen gelten?** Gesetzlich: 1 Woche (§ 51 I GmbHG); Satzungsverlaengerung pruefen.
4. **Elektronischer Versand zugelassen?** Nur wenn Satzung das vorsieht (§ 51 II GmbHG).
5. **Streitige Versammlung erwartet?** Notar hinzuziehen; eingeschriebener Brief mit Rueckschein.
6. **Auslaendische Gesellschafter?** Bilinguale Einladung; § 5 BeurkG fuer Beurkundungen.

## Zentrale Normen

- **§ 49 I GmbHG** — Einberufung durch Geschaeftsfuehrer
- **§ 49 II GmbHG** — Pflichtversammlung bei Verlust der Haelfte des Stammkapitals
- **§ 50 GmbHG** — Einberufungsrecht von Gesellschaftern mit mindestens 10 % der Anteile
- **§ 51 I GmbHG** — Form und Frist: schriftlich, mindestens 1 Woche Vorlauf
- **§ 51 II GmbHG** — Elektronische Form nur bei Satzungs-Ermaechtigung
- **§ 51 III GmbHG** — Heilung von Einberufungsmaengeln durch Vollversammlung (alle Gesellschafter einverstanden)
- **§ 42a GmbHG** — Vorlage Jahresabschluss; Feststellung durch Gesellschafter
- **§§ 246, 248 AktG analog** — Anfechtungs- und Nichtigkeitsklage bei Beschlussmangel

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Einladungs-Rechtmaessigkeit

| Schritt | Pruefpunkt | Norm | Ergebnis |
|---|---|---|---|
| 1 | Alle Gesellschafter eingeladen? | § 51 GmbHG | Nein: Nichtigkeit der Beschluesse |
| 2 | Frist eingehalten? (≥ 1 Woche; Satzung beachten) | § 51 I GmbHG | Nein: Anfechtbarkeit |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 4 | Elektronischer Versand satzungskonform? | § 51 II GmbHG | Nein: Anfechtbarkeit |
| 5 | Beschlussvorlagen beigefuegt? | Satzung (haeufig) | Fehlen kann Anfechtungsrisiko erhoehen |
| 6 | Jahresabschluss bei ordentl. GV beigefuegt? | § 42a GmbHG | Fehlende Unterlage = Anfechtbarkeit |

## Schritt-fuer-Schritt-Workflow

1. **Termin festlegen:** Raeumliche und zeitliche Kapazitaet; Mindestfrist (≥ 1 Woche + 3 Tage Poststlaufzeit) rueckwaerts rechnen.
2. **Tagesordnung entwerfen:** Jeden Beschluss konkret benennen; keine Generalklauseln.
3. **Beschluss-Vorlagen formulieren:** Klarer Beschlusstext; bei Satzungsaenderung: neuer Wortlaut als Anlage.
4. **Anlagen zusammenstellen:** Jahresabschluss (ordentliche GV), Satzungsaenderungs-Entwurf, Berichte.
5. **Versand:** Einschreiben mit Rueckschein an alle Gesellschafter; bei elektronischem Versand: Satzung pruefen.
6. **Frist-Dokumentation:** Versanddatum notieren; Zustellungsfiktion (3. Tag nach Aufgabe) rechnen.
7. **Vor der Versammlung:** Beschlussfaehigkeit pruefen; Quorum in Satzung nachschlagen.
8. **Waehrend der Versammlung:** Versammlungsleiter waehlen; Beschlussfaehigkeit protokollieren; Beschluesse klar formulieren.

## Output-Template: Ordentliche GV-Einladung

**Adressat:** Gesellschafter der GmbH — Tonfall sachlich-foermlich

```
[BRIEFKOPF DER GESELLSCHAFT]
[ORT], [DATUM]

An die Gesellschafter der [FIRMA] GmbH

EINLADUNG ZUR ORDENTLICHEN GESELLSCHAFTERVERSAMMLUNG

Sehr geehrte Damen und Herren,

hiermit lade ich Sie gemaess § 49 Abs. 1 GmbHG und
§ [X] der Satzung zur ordentlichen Gesellschafter-
versammlung ein:

Datum: [WOCHENTAG], [DATUM]
Uhrzeit: [UHRZEIT] Uhr
Ort: [ADRESSE / VIDEO-LINK falls Satzung erlaubt]

TAGESORDNUNG:

TOP 1: Eroefffnung, Feststellung der Beschlussfaehigkeit
 und Wahl des Versammlungsleiters

TOP 2: Feststellung des Jahresabschlusses zum
 [DATUM JAHRESENDE]
 Beschlussvorlage: "Der Jahresabschluss wird
 festgestellt."

TOP 3: Beschluss ueber Gewinnverwendung
 Beschlussvorlage: "Der Jahresueberschuss von
 [BETRAG] EUR wird [thesauriert / ausgeschuettet]."

TOP 4: Entlastung der Geschaeftsfuehrung fuer das
 Geschaeftsjahr [JAHR]
 Beschlussvorlage: "Den Geschaeftsfuehrern wird
 Entlastung erteilt."

TOP 5: Sonstiges

Anlagen:
- Jahresabschluss zum [DATUM]
- Lagebericht [JAHR]
- Gewinnverwendungsvorschlag

Mit freundlichen Gruessen

[UNTERSCHRIFT GESCHAEFTSFUEHRER]
[NAME, Stellung]
```

## Output-Template: Ausserordentliche GV-Einladung

**Adressat:** Gesellschafter — Tonfall sachlich-praezise

```
[BRIEFKOPF]
[ORT], [DATUM]

An die Gesellschafter der [FIRMA] GmbH

EINLADUNG ZUR AUSSERORDENTLICHEN
GESELLSCHAFTERVERSAMMLUNG

Sehr geehrte Damen und Herren,

aus dringendem Anlass lade ich Sie zur ausserordentlichen
Gesellschafterversammlung ein:

Datum: [DATUM] | Uhrzeit: [UHRZEIT] | Ort: [ADRESSE]

Anlass: [KONKRETER ANLASS: z.B. Bestellung eines weiteren GF]

TAGESORDNUNG:

TOP 1: Feststellung Beschlussfaehigkeit; Versammlungsleiter
TOP 2: [KONKRETER BESCHLUSSPUNKT]
 Beschlussvorlage: "[GENAUE FORMULIERUNG]"
TOP 3: Sonstiges

Anlage: [RELEVANTE DOKUMENTE]

[UNTERSCHRIFT]
```

## Rote Schwellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Vage Tagesordnung fuer wichtige Beschluesse: Anfechtbarkeit (OLG Muenchen 2022)
- Elektronischer Versand ohne Satzungs-Ermaechtigung: Anfechtbarkeit (§ 51 II GmbHG)

## Quellen und Vertiefung

- §§ 49, 50, 51, 51a, 42a GmbHG; §§ 241 ff. AktG analog
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` — Protokoll der GV
- `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` — Pflichtversammlung
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — bei Konfliktversammlung
- `gesellschaftsgruender-bilinguale-dokumente` — DE/EN-Vorlagen

## 5. `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter`

**Fokus:** Gesellschafterversammlungs-Protokoll anfertigen und Versammlungsleitung durchführen. Normen: §§ 48 ff. GmbHG. Prüfraster: Protokollierungspflicht, Abstimmungsergebnis, Unterschriften, Formfehler. Output: GV-Protokoll-Vorlage. Abgrenzung: nicht GV-Einladung und Tagesordnung.

# Protokoll der Gesellschafterversammlung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Protokoll der Gesellschafterversammlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere vor Erstellung und Pruefung des Protokolls:

1. **Notarielle Beurkundung erforderlich?** Bei Satzungsaenderung, Kapitalerhoehung, Aufloesung: Notar zwingend (§ 53 GmbHG).
2. **Streitige Versammlung?** Notar als neutralen Zeugen einladen; eingeschriebener Brief als Zustellungsnachweis.
3. **Alle Gesellschafter anwesend?** Vollversammlungs-Heilung (§ 51 III GmbHG) nur bei Einverstaendnis aller.
4. **Stimmverbote beachten?** § 47 IV GmbHG: bei Eigen-Interesse kein Stimmrecht; im Protokoll vermerken.
5. **HR-Anmeldung erforderlich?** Beschluesse zur Bestellung / Abberufung GF, Satzungsaenderung: Notar-Einreichung.
6. **Beschlusstext eindeutig?** Vage Beschluesse koennen bei HR-Anmeldung beanstandet werden.

## Zentrale Normen

- **§ 47 GmbHG** — Abstimmung; Mehrheitsprinzip; Stimmrecht nach Anteilen
- **§ 47 IV GmbHG** — Stimmverbot bei eigenen Angelegenheiten
- **§ 51 III GmbHG** — Heilung von Einberufungsmaengeln durch Vollversammlung
- **§ 53 GmbHG** — Beschluss zur Satzungsaenderung; notarielle Beurkundung zwingend
- **§ 60 I Nr. 2 GmbHG** — Aufloesung durch Gesellschafterbeschluss
- **§§ 241, 246, 249 AktG analog** — Nichtigkeit und Anfechtbarkeit von Beschluessen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Protokoll-Rechtmaessigkeit

| Schritt | Pruefpunkt | Norm | Ergebnis |
|---|---|---|---|
| 1 | Alle Gesellschafter eingeladen und anwesend/vertreten? | § 51 GmbHG | Fehlt: Nichtigkeit |
| 2 | Versammlungsleiter gewaehlt und protokolliert? | Satzung | Fehlt: Anfechtungsrisiko |
| 3 | Beschlussfaehigkeit festgestellt? | Satzung | Fehlt: Anfechtungsrisiko |
| 4 | Stimmverbot § 47 IV GmbHG geprueft? | § 47 IV | Verletzung: Beschluss anfechtbar |
| 5 | Mehrheit korrekt berechnet? | §§ 47, 53 GmbHG | Falsche Berechnung: Anfechtbarkeit |
| 6 | Notarielle Beurkundung bei Satzungsaenderung? | § 53 GmbHG | Fehlt: Nichtigkeit |
| 7 | Beschlusstext klar und eindeutig? | HR-Anforderungen | Vage: Beanstandung bei Eintragung |

## Schritt-fuer-Schritt-Workflow

1. **Vorbereitung:** Anwesenheits-Liste mit Anteilen und Stimmrechten erstellen; Stimmverbot-Pruefung pro Gesellschafter pro TOP.
2. **Eroeffnung:** Feststellung Beschlussfaehigkeit und ordnungsgemae Einladung protokollieren.
3. **Versammlungsleiter-Wahl:** Abstimmung fuer Versammlungsleiter; Ergebnis protokollieren.
4. **Pro TOP:** Beschlussvorlage im Wortlaut; kurze Diskussion zusammenfassen; Stimmen zaehlen und aufschlüsseln.
5. **Beschlussformulierung:** Klarer, vollstaendiger Beschlusstext; bei HR-relevanten Beschluessen: exakter Wortlaut.
6. **Schluss:** Schluss der Versammlung protokollieren; Protokoll sofort vom Versammlungsleiter unterschreiben.
7. **HR-Anmeldung** bei erforderlichen Beschluessen: Notar einschalten; Protokoll + Beurkundung einreichen.
8. **Aufbewahrung:** 10 Jahre (§ 257 HGB); Original-Unterzeichnung sichern.

## Output-Template: GV-Protokoll (Standard)

**Adressat:** Gesellschafter; Handelsregister — Tonfall sachlich-praezise

```
PROTOKOLL der [ordentlichen / ausserordentlichen]
Gesellschafterversammlung der [FIRMA] GmbH

Datum: [DATUM] | Ort: [ORT] | Beginn: [UHRZEIT]

ANWESENHEIT:
[NAME 1], [ANTEILE] EUR (= [%] %; [STIMMEN] Stimmen)
[NAME 2], [ANTEILE] EUR (= [%] %; [STIMMEN] Stimmen)
Gesamt anwesend: [SUMME] EUR ([%] % des Stammkapitals)

Tagesordnung (wie eingeladen):
[LISTE DER TOPs]

TOP 1 — Eroeffnung und Versammlungsleiter
Feststellung: ordnungsgemae Einladung; alle Gesellschafter
anwesend; Versammlung beschlussfaehig.
Vorschlag und Wahl Versammlungsleiter: [NAME]
Abstimmung: einstimmig.

TOP [N] — [BEZEICHNUNG]
Beschlussvorlage (im Wortlaut):
"[GENAUER BESCHLUSSTEXT]"

Diskussion: [KURZE ZUSAMMENFASSUNG]

Abstimmung:
 [NAME 1] ([N] Stimmen): Ja / Nein / Enthaltung
 [NAME 2] ([N] Stimmen): Ja / Nein / Enthaltung

Ergebnis: [N] Ja-Stimmen / [N] Nein-Stimmen / [N] Enthaltungen
Beschluss: [ANGENOMMEN / ABGELEHNT]
Erforderliche Mehrheit: [EINFACH / 75% etc.] — [ERREICHT / NICHT ERREICHT]

Schluss der Versammlung: [UHRZEIT]

Versammlungsleiter: ___________ [NAME]
Schriftfuehrer: ___________ [NAME]
```

## Rote Schwellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Satzungsaenderung ohne Notar: NICHTIGKEIT (§ 53 GmbHG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Beschlusstext vage: HR beanstandet Eintragung; Nacharbeit und erneute Beurkundung noetig

## Quellen und Vertiefung

- §§ 47, 47 IV, 51, 53, 60 GmbHG; §§ 241, 246, 249 AktG analog
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-gv-einladung-tagesordnung` — Einladung vorab
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — bei Streit ueber Beschluesse
- `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` — Pflichtversammlung-Protokoll
- `gesellschaftsgruender-share-classes-a-b-c` — Klassen-Stimmrechts-Berechnung
