---
name: gesellschaftsgruender-handelsregister
description: "Handelsregister: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Handelsregister

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Handelsregister** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-handelsregister-anmeldung` | Erstanmeldung der GmbH zum Handelsregister vorbereiten: Notarauftrag, Eintragungsvoraussetzungen, Gründungsunterlagen. Normen: §§ 7 ff. GmbHG, §§ 12 ff. HGB. Prüfraster: Einzahlungsnachweis, Notarbeglaubigung, Gesellschafterliste, HR-Formblatt. Output: Checkliste Handelsregisteranmeldung GmbH. Abgrenzung: nicht laufende HR-Aenderungen nach Gründung. |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK-Pflichtmitgliedschaft und Berufsgenossenschafts-Anmeldung nach GmbH-Gründung erledigen. Normen: §§ 2 ff. IHKG, §§ 150 ff. SGB VII. Prüfraster: Branchenzuordnung BG, IHK-Beitragspflicht, Fristen. Output: Checkliste IHK-Anmeldung und BG-Anmeldung. Abgrenzung: nicht Gewerbeamt-Anmeldung. |
| `gesellschaftsgruender-investor-dd-vorbereiten` | Baut Datenraum für Investor-DD: Corporate, Finance, IP, HR, Datenschutz, Verträge. |
| `gesellschaftsgruender-ip-einbringung` | Prüft, ob Software, Marken, Designs, Domains und Know-how sauber in die Gesellschaft gelangen. |
| `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` | Kapitalerhöhung der GmbH mit und ohne Bezugsrecht der Gesellschafter durchführen. Normen: §§ 55 56 56a GmbHG. Prüfraster: Gesellschafterbeschluss, Bezugsrechtsausschluss, Einlageverpflichtung, Handelsregisteranmeldung. Output: Beschlussvorlage Kapitalerhöhung und HR-Checkliste. Abgrenzung: nicht genehmigtes Kapital. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Handelsregister**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-handelsregister-anmeldung`

**Fokus:** Erstanmeldung der GmbH zum Handelsregister vorbereiten: Notarauftrag, Eintragungsvoraussetzungen, Gründungsunterlagen. Normen: §§ 7 ff. GmbHG, §§ 12 ff. HGB. Prüfraster: Einzahlungsnachweis, Notarbeglaubigung, Gesellschafterliste, HR-Formblatt. Output: Checkliste Handelsregisteranmeldung GmbH. Abgrenzung: nicht laufende HR-Aenderungen nach Gründung.

# Handelsregister-Anmeldung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Handelsregister-Anmeldung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Anmeldung

1. Handelt es sich um eine Neu-Gründung (konstitutive Wirkung) oder eine Änderung (Satzungsänderung, GF-Wechsel, Kapitalerhöhung)?
2. Sind alle GF persönlich anwesend oder durch Vollmacht vertreten — für Versicherungen nach § 8 Abs. 2 GmbHG?
3. Liegt die Bankbestätigung über die Stammkapital-Einzahlung vor?
4. Bei Sachgründung: ist der Sachgründungsbericht fertiggestellt und werthaltig?
5. Liegen alle erforderlichen Genehmigungen vor (bei genehmigungspflichtigem Gegenstand)?
6. Sind Handelsregister-Gebühren eingeplant (ca. 150-200 EUR Eintragungskosten)?

## Zentrale Normen

- **§§ 7, 8 GmbHG** — Anmeldevoraussetzungen: Stammkapital-Einzahlung; Versicherungen der GF; Anlagen.
- **§ 11 GmbHG** — Konstitutive Wirkung: GmbH entsteht erst mit HR-Eintragung; davor Vor-GmbH mit Vorbelastungshaftung.
- **§ 78 GmbHG** — Anmeldefähigkeit: alle GF in vertretungsberechtigter Zahl.
- **§ 82 GmbHG** — Strafbarkeit falscher Versicherungen bei HR-Anmeldung; Freiheitsstrafe bis 3 Jahre.
- **§ 40 GmbHG** — Gesellschafterliste: nach jeder Änderung unverzüglich neue Liste einreichen.
- **§§ 106-108 HGB** — Anmeldung OHG / KG: alle Gesellschafter; Hafteinlage Kommanditisten.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflicht-Anlagen und Checkliste

| Anlage | Pflicht | Besonderheit |
|---|---|---|
| Satzung / Gesellschaftsvertrag (notarielles Original) | Ja | Musterprotokoll oder individuelle Satzung |
| Gesellschafterliste (§ 8 Abs. 1 Nr. 3 GmbHG) | Ja | Namen, Adressen, Nennbeträge |
| Versicherungen der GF (§ 8 Abs. 2 GmbHG) | Ja | falsche Angabe: § 82 GmbHG |
| Bankbestätigung Stammkapital-Einzahlung | Ja | mind. 12.500 EUR Bareinlage |
| Sachgründungsbericht (bei Sacheinlage) | Nur bei Sachgründung | Werthaltigkeit nachweisen |
| Werthaltigkeitsnachweis Sacheinlage | Nur bei Sacheinlage | ggf. Gutachter |
| Genehmigungen (bei genehmigungspflichtigem Gegenstand) | Je nach Gegenstand | BaFin, Ordnungsamt, etc. |
| Vollmachten (bei Vertretung) | Ggf. | notariell beglaubigt |

## Versicherungen GF § 8 Abs. 2 GmbHG — Inhalt

Jeder GF muss folgendes versichern:

1. Stammkapital vollständig eingezahlt und dem GF frei verfügbar.
2. Kein GF ist vorbestraft wegen Insolvenzverschleppung, Betrug, Untreue oder anderer GmbHG-relevanter Tatbestände in den letzten 5 Jahren.
3. Kein gerichtliches oder behördliches Berufsverbot für GF-Tätigkeiten.
4. Keine Insolvenz- oder Verwertungsverfahren gegen GF persönlich.

→ Falsche Versicherung: Strafbarkeit § 82 GmbHG (bis 3 Jahre Freiheitsstrafe).

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen oben beantworten.
2. **Unterlagen zusammenstellen** — Checkliste oben abarbeiten; Bankbestätigung besorgen.
3. **Notar kontaktieren** — Anmeldungsunterlagen übergeben; Notar bereitet Anmeldeformular vor.
4. **GF-Versicherungen** — alle GF unterzeichnen eidesstattliche Versicherungen.
5. **Elektronische Einreichung** — Notar sendet elektronisch ans HR-Gericht (EGVP / BRAK-System).
6. **Prüfung durch HR-Gericht** — Formalkontrolle; Firma-Check; ggf. Zwischenverfügung.
7. **Eintragung** — nach 2-4 Wochen; Eintragungsbekanntmachung (kostenpflichtig ca. 25 EUR).
8. **Gesellschafterliste** — Notar legt Gesellschafterliste in HR-Akte ab; bei späteren Änderungen: unverzüglich neue Liste einreichen (§ 40 GmbHG).

## Output-Template Anmeldungs-Checkliste

**Adressat:** Notar / Mandant — Tonfall sachlich-präzise
```
HANDELSREGISTER-ANMELDUNG CHECKLISTE
Gesellschaft: [Firmenname] GmbH / UG
Notar: [Name, Ort]
Anmeldedatum (geplant): [Datum]

UNTERLAGEN VOLLSTÄNDIG?
[ ] Satzung (notarielles Original) — Version [Nr.], Datum [Datum]
[ ] Gesellschafterliste — [N] Gesellschafter, Stand [Datum]
[ ] GF-Versicherungen — alle [N] GF unterschrieben
[ ] Bankbestätigung Stammkapital — [EUR] eingezahlt am [Datum], Bank [Bank]
[ ] Sachgründungsbericht — [N/A / Anlage X]
[ ] Genehmigungen — [N/A / Art: X]

GF-VERSICHERUNGEN
| GF | Versicherung vorliegt | Datum Unterschrift |
|----|----------------------|-------------------|
| [Name 1] | Ja / Nein | [Datum] |
| [Name 2] | Ja / Nein | [Datum] |

ZEITPLAN
Beurkundung: [Datum]
Einzahlung Stammkapital bis: [Datum]
Einreichung beim HR: [Datum]
Erwartete Eintragung: ca. [Datum + 2-4 Wochen]

KOSTEN
Notargebühren HR-Anmeldung: ca. [EUR]
HR-Eintragungsgebühren: ca. 150-200 EUR
Bekanntmachungskosten: ca. 25 EUR
```

## Rote Schwellen

- Stammkapital nicht vollständig eingezahlt → Anmeldevoraussetzung fehlt; HR-Gericht verweigert Eintragung.
- GF-Versicherung unrichtig → Strafbarkeit § 82 GmbHG; HR kann Eintragung verweigern.
- Sachgründung ohne Sachgründungsbericht → Zwischenverfügung; Differenzhaftung (§ 9 GmbHG).
- Firma Verwechslungsgefahr → Zwischenverfügung des HR-Gerichts; Fristverlängerung nötig.
- Vorbelastung der Vor-GmbH bei Eintragung nicht abgedeckt → Gesellschafter haften persönlich.

## Fristen und Gebühren

| Posten | Betrag / Frist | Basis |
|---|---|---|
| HR-Eintragungsgebühr GmbH | ca. 150-200 EUR | GNotKG |
| Notar-Gebühr für HR-Anmeldung | ca. 100-200 EUR | GNotKG |
| Bekanntmachungsgebühr | ca. 25 EUR | — |
| Eintragungsdauer | 2-4 Wochen nach Einreichung | — |
| Zwischenverfügung Frist | typisch 2 Wochen | — |

## Quellen und Vertiefung

- §§ 7, 8, 11, 40, 78, 82 GmbHG (HR-Anmeldung, Versicherungen, Strafbarkeit)
- §§ 106-108 HGB (KG/OHG Anmeldung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Emmerich, GmbHG, § 8 Rn. 1-25

## Übergabe an andere Skills

- `gesellschaftsgruender-notar-vorbereitung` — Notarsitzung vor HR-Anmeldung
- `gesellschaftsgruender-stammkapital-einzahlung` — Einzahlungsnachweis für Bankbestätigung
- `gesellschaftsgruender-gewerbeanmeldung-finanzamt` — nächste Schritte nach HR-Eintragung
- `gesellschaftsgruender-transparenzregister` — Transparenzregistermeldung nach HR-Eintragung

## 2. `gesellschaftsgruender-ihk-und-berufsgenossenschaft`

**Fokus:** IHK-Pflichtmitgliedschaft und Berufsgenossenschafts-Anmeldung nach GmbH-Gründung erledigen. Normen: §§ 2 ff. IHKG, §§ 150 ff. SGB VII. Prüfraster: Branchenzuordnung BG, IHK-Beitragspflicht, Fristen. Output: Checkliste IHK-Anmeldung und BG-Anmeldung. Abgrenzung: nicht Gewerbeamt-Anmeldung.

# IHK und Berufsgenossenschaft

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IHK und Berufsgenossenschaft` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre beim Erstgespräch

1. Handelt es sich um ein Gewerbe (→ IHK), ein Handwerk nach Anlage A HwO (→ Handwerkskammer) oder einen Freiberufler (→ Berufskammer)?
2. Gibt es Mitarbeiter oder nur den GF allein? (BG-Beitrag hängt u.a. von Lohnsumme ab)
3. Ist der GF selbst gegen Arbeitsunfall versichert oder nur das Personal?
4. Gibt es genehmigungspflichtige Tätigkeiten (§ 34 GewO, § 34a GewO, § 12 GastG), die besondere IHK-Nachweise erfordern?
5. Sind Beitragskosten IHK und BG im Budgetplan eingeplant?

## Zentrale Normen

- **§ 2 IHKG** — Pflichtmitgliedschaft aller Gewerbetreibenden und kaufmännisch betriebenen Unternehmen; Beitragspflicht.
- **§ 3 IHKG** — Beitragsfestsetzung durch IHK; Grundbeitrag + Umlage auf Gewerbeertrag.
- **§ 192 SGB VII** — Anzeigepflicht des Unternehmers bei Berufsgenossenschaft: binnen einer Woche nach Aufnahme der Tätigkeit.
- **§ 150 SGB VII** — Beitragspflicht BG: Gefahrklassen × Lohnsumme.
- **§ 90 HwO** — Pflichtmitgliedschaft in Handwerkskammer bei Handwerksbetrieb.
- **§ 14 GewO** — Gewerbeanmeldepflicht; Mitteilung an IHK erfolgt automatisch.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## IHK — Mitgliedschaft und Beitrag

### Pflichtmitgliedschaft

- **Automatisch** mit Gewerbeanmeldung oder HR-Eintragung.
- Keine separate Anmeldung erforderlich; IHK sendet Beitrittsbescheid.
- Gilt für GmbH, UG, KG, OHG, Einzelkaufmann — nicht für reine Freiberufler.

### Beitrag Struktur

| Beitragskomponente | Grundlage | Betrag (ca.) |
|---|---|---|
| Grundbeitrag | Fixbetrag je Rechtsform | 50-300 EUR/Jahr |
| Umlage | % des Gewerbeertrags (0,1-0,3 % je nach IHK) | Variabel |
| Neuling-Rabatt | Erstes oder zweites Jahr | oft 50 % Reduzierung |
| Kleinstbetrieb-Befreiung | Ertrag unter Schwelle (oft 5.000 EUR) | Befreiung möglich |

### Leistungen der IHK

- Kostenlose Beratung (Gründung, Außenhandel, Recht).
- Aus- und Weiterbildungszeugnisse (Ausbildungsbetriebe-Zertifizierung).
- Sachverständige und Schlichter.
- Außenhandel: Carnet ATA, Ursprungszeugnisse, Exportkontrolle.

## Berufsgenossenschaft — Pflichtmitgliedschaft

### Pflicht und Frist

- **Binnen einer Woche** nach Betriebsaufnahme anmelden (§ 192 SGB VII).
- Zuständige BG richtet sich nach Branche (Holz, Bau, VBG für Verwaltung, usw.).
- Online-Anmeldung auf www.bg-.de der zuständigen BG.

### Welche BG ist zuständig

| Branche | Berufsgenossenschaft |
|---|---|
| Handel / Dienstleistung | BG ETEM / BGHW |
| IT / Medien / Bildung | VBG |
| Bau | BG BAU |
| Lebensmittel / Gaststätten | BGN |
| Gesundheit / Wohlfahrt | BGW |
| Energie / Entsorgung | BG ETEM |
| Holz / Metall | Holz-BG / BG Metall |

### Beitrag BG

- Berechnung: **Lohnsumme × Gefahrklasse × Beitragsfuß** (in Promille).
- Gefahrklasse richtet sich nach Unfallrisiko der Branche.
- Erste Meldung: jährlich bis 15.02. des Folgejahres (Lohnsumme des Vorjahres).
- Mindestbeitrag: i.d.R. 50-200 EUR/Jahr auch ohne Lohnzahlungen.

### GF-Versicherung

- Gesellschafter-GF mit Mehrheit: **freiwillige BG-Versicherung** möglich; Antrag bei BG.
- Fremd-GF (Angestellter): gesetzlich BG-versichert.
- Empfehlung: freiwillige BG-Versicherung für GF in Berufen mit Unfallrisiko abschließen.

## Schritt-für-Schritt-Workflow

1. **Triage** — Gewerbe, Handwerk oder Freiberufler? Mitarbeiter vorhanden?
2. **IHK-Kontakt** — Beitrittsbescheid abwarten; Grundbeitrag und Umlage prüfen; ggf. Befreiungsantrag.
3. **BG ermitteln** — zuständige Berufsgenossenschaft anhand der Branche identifizieren.
4. **BG-Anmeldung** — binnen einer Woche; Online-Formular; Lohnsumme schätzen.
5. **Beitragsberechnung** — Lohnsumme × Gefahrklasse; Budget-Planung.
6. **GF-BG-Versicherung prüfen** — freiwillige Versicherung bei Unfallrisiko sinnvoll.
7. **Jahresmeldung** — jährlich bis 15.02. Lohnsumme des Vorjahres melden.

## Output-Template Pflichtmeldungen nach HR-Eintragung

**Adressat:** Mandant/Gründer — Tonfall anleitend-strukturiert
```
PFLICHTMELDUNGEN NACH HR-EINTRAGUNG
Gesellschaft: [Firmenname]
HR-Eintragung: [Datum]
Erstellt: [Datum]

IHK
Zuständige IHK: [Name, Ort]
Mitgliedschaft automatisch: Ja
Beitrittsbescheid erwartet bis: [Datum + ca. 4 Wochen]
Grundbeitrag (geschätzt): [EUR] / Jahr
Kleinstbetrieb-Befreiung prüfen: [ ] Ja, Antrag gestellt / [ ] Nein

BERUFSGENOSSENSCHAFT
Zuständige BG: [BG-Name]
Anmeldepflicht bis: [Datum HR + 1 Woche = Datum]
Online-Anmeldung: www.[BG-Website].de
Lohnsumme Jahr 1 (geschätzt): [EUR]
Beitrag (geschätzt): [EUR] / Jahr
GF-freiwillige Versicherung: [ ] Antrag gestellt / [ ] Nicht erforderlich

HANDWERKSKAMMER (falls Handwerk)
Zuständige lizenzpflichtige Literaturquelle: [Name, Ort]
Eintragung Handwerksrolle: [ ] beantragt / [ ] nicht erforderlich

STATUS PFLICHTMELDUNGEN
[ ] IHK-Beitrittsbescheid erhalten und geprüft
[ ] BG-Anmeldung eingereicht bis [Datum]
[ ] Erste Lohnsummenmeldung BG: bis 15.02.[JJJJ]
```

## Rote Schwellen

- BG-Anmeldung vergessen → Bußgeld; unversicherter Betrieb bei Arbeitsunfällen; Haftungsrisiko GF.
- Falsche BG-Zuordnung → Nachzahlungen und Strafbeiträge; BG prüft rückwirkend.
- Handwerksrolle nicht eingetragen bei zulassungspflichtigem Handwerk → Betrieb unzulässig; Bußgeld.
- Freiberufler irrtümlich IHK-Beitrag gezahlt → Rückerstattung möglich; Antrag stellen.

## Quellen und Vertiefung

- §§ 2, 3 IHKG (IHK-Pflichtmitgliedschaft, Beitrag)
- §§ 150, 192 SGB VII (BG-Beitrag, Anzeigepflicht)
- § 90 HwO (Handwerkskammer)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Übergabe an andere Skills

- `gesellschaftsgruender-kommandocenter` — Master-Gründung
- `gesellschaftsgruender-gewerbeanmeldung-finanzamt` — Gewerbeanmeldung vor IHK
- `gesellschaftsgruender-gf-sozialversicherungs-status` — SV-Status GF und Beschäftigte

## 3. `gesellschaftsgruender-investor-dd-vorbereiten`

**Fokus:** Baut Datenraum für Investor-DD: Corporate, Finance, IP, HR, Datenschutz, Verträge.

# Investor Due Diligence vorbereiten

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Investor Due Diligence vorbereiten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Lückenliste und Red-Flag-Ampel.

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

## 4. `gesellschaftsgruender-ip-einbringung`

**Fokus:** Prüft, ob Software, Marken, Designs, Domains und Know-how sauber in die Gesellschaft gelangen.

# IP-Einbringung und Rechtekette

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IP-Einbringung und Rechtekette` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Erfasse Urheber, Arbeitnehmer, Freelancer, Open Source, Abtretung, Lizenz.

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

## 5. `gesellschaftsgruender-kapitalerhoehung-bezugsrecht`

**Fokus:** Kapitalerhöhung der GmbH mit und ohne Bezugsrecht der Gesellschafter durchführen. Normen: §§ 55 56 56a GmbHG. Prüfraster: Gesellschafterbeschluss, Bezugsrechtsausschluss, Einlageverpflichtung, Handelsregisteranmeldung. Output: Beschlussvorlage Kapitalerhöhung und HR-Checkliste. Abgrenzung: nicht genehmigtes Kapital.

# Kapitalerhöhung und Bezugsrecht

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kapitalerhöhung und Bezugsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Bei Erhöhung des Stammkapitals müssen die bestehenden Gesellschafter **Bezugsrechte** erhalten (Paragraf 55 II GmbHG). Ausschluss ist möglich, aber begründungsbedürftig. Streit über Bezugsrecht / Bezugsrechtsausschluss ist klassischer Konflikt-Auslöser.

## 1) Rechtsgrundlagen

- **Paragraf 55 GmbHG**: Erhöhung des Stammkapitals
- **Paragraf 55 II GmbHG**: Bezugsrecht
- **Paragraf 55 IV GmbHG**: Bezugsrechtsausschluss
- **Paragraf 56 GmbHG**: Sacheinlage

## 2) Bezugsrecht — Grundsatz

### Pro-Rata-Recht

- Jeder Gesellschafter hat das Recht, einen seiner Beteiligungsquote entsprechenden Teil der neuen Anteile zu erwerben
- Vermeidet Verwässerung

### Beispiel

```
Vor Erhoehung:
- Gruender A: 60 % (15.000 Anteile)
- Gruender B: 40 % (10.000 Anteile)
Stammkapital: 25.000 EUR

Kapitalerhoehung: + 10.000 EUR (10.000 neue Anteile)

Bezugsrecht:
- Gruender A: 6.000 neue Anteile (60 %)
- Gruender B: 4.000 neue Anteile (40 %)

Nach Erhoehung (alle ziehen mit):
- Gruender A: 21.000 / 35.000 = 60 %
- Gruender B: 14.000 / 35.000 = 40 %
-> Anteilsquoten unveraendert
```

## 3) Wenn nicht alle mitziehen

### Konstellation

- Gesellschafter B kann oder will nicht mitziehen
- Gründer A zieht voll mit
- Investor I AG nimmt die nicht-ausgeuebten Anteile

### Auswirkung

```
Vor Erhoehung:
- A: 15.000 (60 %)
- B: 10.000 (40 %)

Erhoehung 10.000 Anteile:
- A nimmt 6.000 (Bezugsrecht voll)
- B verzichtet
- Investor I AG nimmt 4.000 (statt B)

Nach Erhoehung:
- A: 21.000 / 35.000 = 60 %
- B: 10.000 / 35.000 = 28,57 % (verwaessert)
- Investor I AG: 4.000 / 35.000 = 11,43 %
```

### Konsequenz für B

- **Anteilsquote sinkt** von 40 % auf 28,57 %
- **Stimmrechte sinken** entsprechend
- Bei vorherigen Sondermehrheits-Schwellen: ggf. nicht mehr erreicht

## 4) Bezugsrechtsausschluss Paragraf 55 IV GmbHG

### Voraussetzungen

- **75 %-Mehrheits-Beschluss** in GV (Paragraf 53 II GmbHG)
- **Sachliche Rechtfertigung**
- **Verhältnismaessigkeit**
- **Angemessenheit**

### Sachliche Rechtfertigung

Bei Series-A-Investor:
- Investor bringt strategisches Know-how oder Marktzugang
- Kapital-Bedürfnis kann nicht durch bestehende Gesellschafter gedeckt werden
- Investor verlangt Mindest-Anteil als Voraussetzung des Einstiegs

Bei Mitarbeiter-Beteiligung:
- ESOP-Programm zur Mitarbeiter-Bindung
- Sachlich gerechtfertigt, wenn Pool angemessen (typisch 5-15 %)

### Anfechtungsrisiko

- Bezugsrechtsausschluss ohne sachliche Rechtfertigung: anfechtbar (BGH-Linie Kali+Salz)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 5) Streit-Konstellation

### Typisch

- **Mehrheits-Gesellschafter** wollen Investor-Eintritt mit Bezugsrechtsausschluss
- **Minderheits-Gesellschafter** lehnen ab — Verwässerungs-Angst
- **75 %-Beschluss** wird gefasst (Mehrheits-Gesellschafter haben 75 %)
- **Minderheits-Gesellschafter** klagt auf Anfechtung des Beschlusses

### Eilrechtsschutz

- **Einstweilige Verfügung** auf Anmeldungs-Sperre (Paragraf 16 II HGB)
- Antrag beim **Landgericht** (Gesellschafts-Sitz)
- Glaubhaftmachung von:
 - Wahrscheinlichkeit der Anfechtbarkeit (sachliche Rechtfertigung fehlt)
 - Eilbedürftigkeit (Eintragung würde Verwässerung unwiderruflich)

→ `gesellschaftsgruender-gesellschafterstreit-eilantraege`

## 6) Beschluss-Vorlage Bezugsrechtsausschluss

```
TOP X — Kapitalerhoehung um 10.000 EUR mit
Bezugsrechtsausschluss

Beschluss-Vorlage:
"Die Gesellschafterversammlung beschliesst,

a) das Stammkapital der Gesellschaft um 10.000 EUR
 auf 35.000 EUR durch Ausgabe von 10.000 neuen
 Geschaeftsanteilen der Class A zu erhoehen,

b) das Bezugsrecht der bestehenden Gesellschafter
 gemaess Paragraf 55 IV GmbHG ganz auszuschliessen,

c) zur Uebernahme der neuen Anteile die Investor I AG
 mit Sitz in [Ort], eingetragen im HR [HRB X], zu
 ermaechtigen, gegen Bareinlage des
 Nennwerts plus Aufgeld i.H.v. 90.000 EUR pro Anteil
 (Gesamtbetrag 100.000 EUR pro Anteil),

d) die naeheren Bedingungen folgen aus dem
 Subscription Agreement zwischen der Gesellschaft
 und Investor I AG vom [Datum].

Sachliche Rechtfertigung des Bezugsrechtsausschlusses:
- Investor I AG ist strategischer Investor mit
 Marktzugang in Sektor X.
- Der Eintritt des Investors ist Voraussetzung fuer
 die Geschaeftsentwicklung in [Markt].
- Die bestehenden Gesellschafter haben kein
 vergleichbares strategisches Engagement.
- Verwaesserung der bestehenden Gesellschafter
 betraegt 22 %, was im Rahmen angemessen ist."
```

## 7) Bei Sondervetorecht / Golden Share

### Konstellation

- Bezugsrechtsausschluss verlangt 75 %-Mehrheit
- Aber: Golden-Share-Inhaber hat Sondervetorecht
- Auch bei 100 %-Zustimmung der anderen kann das Veto den Beschluss blockieren

→ `gesellschaftsgruender-golden-share-und-vetorechte`

## 8) Verwässerungs-Schutz im SHA

### Anti-Dilution-Klauseln

Bei späterer Erhöhung zu niedrigerem Preis als Erstausgabe:

- **Full Ratchet**: rueckwirkende Preisanpassung
- **Weighted Average broad-based**: gewichteter Mittelwert

→ `gesellschaftsgruender-gesellschaftervereinbarung`

### Pflicht zur Mitteilung

- Bezugsrechte müssen den Gesellschaftern **mit Frist** angeboten werden
- Frist typisch 14-28 Tage
- Bei Verstoß: Anfechtungs-Risiko

## 9) Typische Erhöhungs-Fehler

1. **Bezugsrecht nicht offeriert**, sondern automatisch ausgeschlossen ohne Beschluss. Anfechtbar.
2. **Sachliche Rechtfertigung fehlt**. Anfechtbar.
3. **Aufgeld zu niedrig** (Down Round ohne Anti-Dilution-Anpassung). Investor I AG koennte Anpassung verlangen.
4. **75 %-Mehrheit knapp verfehlt** (z.B. durch Stimmverbot Paragraf 47 IV GmbHG). Beschluss unwirksam.
5. **Sacheinlage ohne Werthaltigkeits-Nachweis**. Differenzhaftung.
6. **Anmeldung HR ohne abgeschlossene Einzahlung**. HR beanstandet.

## 10) Verfahrens-Ablauf

| Schritt | Aktion |
|---|---|
| 1 | GV-Einladung mit Beschluss-Vorlage (Frist 1 Woche+) |
| 2 | GV mit Beschluss (Notar bei Satzungsaenderung) |
| 3 | Einzahlung Bareinlage (mind. 12.500 EUR vor Anmeldung) |
| 4 | Anmeldung HR durch Notar |
| 5 | Eintragung HR |
| 6 | Aktualisierte Gesellschafterliste |
| 7 | Transparenzregister-Update |
| 8 | Aktualisierter Cap Table |

## Anschluss

- `gesellschaftsgruender-genehmigtes-kapital` — bei Vorratsbeschluss
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — bei Streit
- `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` — Protokoll
- `gesellschaftsgruender-cap-table` — Verwässerungs-Berechnung

## Triage zu Beginn

Klaere vor Bearbeitung einer Kapitalerhoehung:

1. **Art der Erhoehung?** Bareinlage (Cash) oder Sacheinlage (Assets, IP, Forderungen)?
2. **Bezugsrecht ausgeschlossen oder gewahrt?** Neuer Investor: typisch Ausschluss; interne Erhoehung: typisch gewahrt.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **75%-Mehrheit gesichert?** Stimmverbot § 47 IV GmbHG pruefen; Golden-Share-Veto pruefen.
5. **Anti-Dilution-Klauseln in SHA?** Bestehende Investoren-Schutzrechte koennen durch neue Runde ausgeloest werden.
6. **Stamm- oder Nennkapital nach Erhoehung?** Handelsregister-Eintragung erst nach vollstaendiger Einzahlung moeglich.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Kapitalerhoehungs-Beschluss

**Adressat:** Gesellschafterversammlung GmbH — Tonfall rechtspraezise

```
BESCHLUSS der Gesellschafterversammlung
der [FIRMA] GmbH vom [DATUM]

TOP [N]: Kapitalerhoehung mit Bezugsrechtsausschluss

Die Gesellschafterversammlung beschliesst:

1. Das Stammkapital der Gesellschaft wird um [BETRAG] EUR
 auf [NEUES KAPITAL] EUR erhoeht durch Ausgabe von
 [ANZAHL] neuen Geschaeftsanteilen (Class [X]) mit
 einem Nennwert von je 1 EUR.

2. Das Bezugsrecht der bestehenden Gesellschafter
 wird gemaess § 55 Abs. 4 GmbHG ausgeschlossen.
 Sachliche Rechtfertigung: [BEGRUENDUNG].

3. Zur Uebernahme der neuen Anteile wird [INVESTOR]
 zugelassen gegen Bareinlage von [BETRAG] EUR
 (Nennwert [BETRAG] EUR + Aufgeld [BETRAG] EUR).

4. Einzahlungsfrist: [DATUM].

Abstimmung: [N] Ja / [N] Nein / [N] Enthaltungen
(= [%] %; erforderlich 75 % = [N] Stimmen)
Beschluss: [ANGENOMMEN / ABGELEHNT]
```
