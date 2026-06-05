---
name: dealteam-zusammenfassung
description: "Dealteam Zusammenfassung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dealteam Zusammenfassung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Dealteam Zusammenfassung** im Plugin Gesellschaftsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dealteam-zusammenfassung` | Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update, Deal-Team-Summary. |
| `gesellschafterbeschluss` | Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG analog) und Anfechtbarkeit (246 AktG analog). Laedt bei Mandaten zur Beschlussfassung, Anfechtungsklage oder Nichtigkeitsfeststellung. |
| `gesellschafterstreit-loesungsstrategie` | Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38 GmbHG. Normen § 34 GmbHG Einziehung § 140 HGB analog Ausschluss-Klage § 48 GmbHG Gesellschafterversammlung. Prüfraster Wertbestimmungs-Verfahren Abfindungsberechnung BGH Verkehrswert Schiedsklausel DIS. Output Konflikt-Strategie-Memo mit Verhandlungskonzept Klageoption und Kostenfolge. Abgrenzung: gesellschafterbeschluss für Beschlussfassung mandat-triage für Erst-Abfrage. |
| `gesellschafts-compliance` | Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger und Rechtsordnung und zeigt auf, was in den nächsten 30/60/90 Tagen fällig ist. Trigger: "Gesellschafts-Compliance", "Einreichungsfristen", "Bilanzpublizität", "Transparenzregister", "Jahresabschluss einreichen", "was ist fällig". |
| `gesellschaftsrecht-anpassen` | Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A / Governance / Kapitalmarkt / Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Beschlussformat oder Mandatsworkspace-Pfade anpassen. Lädt, wenn der Nutzer "Profil ändern", "Konfiguration aktualisieren", "Einstellung anpassen" oder vergleichbare Formulierungen verwendet. |

## Arbeitsweg

Im Plugin Gesellschaftsrecht gilt für **Dealteam Zusammenfassung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dealteam-zusammenfassung`

**Fokus:** Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update, Deal-Team-Summary.

# Deal-Team-Zusammenfassung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Deal-Team-Zusammenfassung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Deal-Team-Zusammenfassung
- **Spezialgegenstand:** Deal-Team-Zusammenfassung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor der Erstellung des Briefings klären:

1. **Ebene bestimmen:** Welche Ebene wird zuerst benötigt — GF-Kurzfassung, Deal-Lead-Briefing oder Arbeitsteam-Vollständigkeit?
2. **DD-Stand:** Sind alle DD-Kategorien abgeschlossen oder nur Teilbereiche?
3. **Vollzugsstatus:** Ist die Vollzugscheckliste aktuell gepflegt?
4. **Adressat:** Wer erhält welche Ebene? (GF-Kurzfassung häufig nach außen; Ebene 3 bleibt im Privilegierungskreis)
5. **Zeitdruck:** Ist Signing in weniger als 48 Stunden (dann Ebene 1 und 2 prioritär)?
6. **Preisrelevanz:** Gibt es blockierende Findings, die eine Kaufpreisanpassung erfordern?

## Zentrale Normen

§§ 311 Abs. 2, 241 Abs. 2 BGB (vorvertragliche Aufklärungspflichten) — §§ 443, 444 BGB (Garantien, Haftungsausschluss) — § 442 BGB (Kenntnis des Käufers) — §§ 35 ff. GWB (Fusionskontrolle) — §§ 55 ff. AWV, § 5 AWG (FDI-Investitionsprüfung) — § 15 GmbHG (Abtretung) — § 613a BGB (Betriebsübergang)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

M&A-Teams brauchen je nach Ebene unterschiedliche Informationstiefe: Die Geschäftsführung will drei Sätze und eine Risikobewertung. Der Deal-Lead will kritischen Pfad und offene Punkte. Das Arbeitsteam will alle Findings mit Quellen. Dieser Skill erstellt alle drei Ebenen aus denselben DD-Quellen.

## Eingaben

- DD-Issue-Extraktions-Findings aus dem laufenden Mandat
- Vollzugscheckliste (aktueller Status)
- Wesentliche-Verträge-Anlage (wenn vorhanden)
- Deal-Kontext: Parteien, Transaktionsstruktur, Kaufpreis, Zieldatum Vollzug
- Praxisprofil: `## M&A → Deal-Team-Briefing` (Rhythmus, Format, Adressat)

## Schritt-fuer-Schritt-Workflow

### Schritt 1: Quellen zusammenführen

Aus dem Mandatsordner lesen:
- `mandate/[code]/dd-issues-[kategorie].md` (alle Kategorien)
- `mandate/[code]/vollzugs-checkliste.yaml`
- `mandate/[code]/wesentliche-vertraege-anlage.md` (falls vorhanden)
- `mandate/[code]/deal-kontext.md`

Gesamtbild: Anzahl Findings je Schweregrad; blockierende Vollzugspunkte; kritischer Pfad.

### Schritt 2: Drei Briefing-Ebenen erstellen

**Ebene 1 – GF-Kurzfassung (max. 1 Seite):** Kernrisiken, Vollzugsstatus, Handlungsempfehlung.

**Ebene 2 – Deal-Lead-Briefing (2-4 Seiten):** Alle Kategorien mit Findings-Tabelle, kritischer Pfad, offene Fragen.

**Ebene 3 – Arbeitsteam-Vollständigkeit:** Alle Findings mit Quellen, sortiert nach Schweregrad.

### Schritt 3: Vollzugs-Handlungs-Abgleich

Nach Erstellung: prüfen, ob neue Vollzugspunkte aufgedeckt wurden, die in der Vollzugscheckliste fehlen. Falls ja: als Übergabe-Items für den Vollzugscheckliste-Skill markieren.

## Output-Template

**Adressat je Ebene; Tonfall:** Ebene 1 verständlich-entscheidungsorientiert; Ebene 2+3 sachlich-juristisch

### Ebene 1 — GF-Kurzfassung

```
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

# [DEAL-CODE] — Statusbericht — [DATUM]

Transaktion: Erwerb [ZIELGESELLSCHAFT] durch [KAEUFER]; Kaufpreis: [X] EUR;
Vollzug geplant: [DATUM].

Gesamteinschätzung: [Erhebliche offene Punkte / Klärungsbedarf / Auf Kurs]

Kernrisiken:
1. [RISIKO] — [Implikation in einem Satz]
2. [RISIKO] — [Implikation in einem Satz]
3. [RISIKO] — [Implikation in einem Satz]

Vollzugsstatus: [N] von [N] VB erfüllt. Kritischer Pfad: [PUNKT + DATUM].

Empfehlung: [Fortsetzen / Preis anpassen / Klärung einholen / Abbruch erwägen]
```

### Ebene 2 — Deal-Lead-Briefing

```
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

# [DEAL-CODE] — Deal-Lead-Briefing — [DATUM]

## Transaktionsübersicht
[Parteien, Struktur, Preis, Timeline]

## DD-Ergebnisse nach Kategorie

| Kategorie | Rot | Orange | Gelb | Gruen | Top-Finding |
|---|---|---|---|---|---|
| Gesellschaftsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| Wesentliche Verträge | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
| IP / Technologie | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
| Arbeitsrecht | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |
| Umwelt / Regulatorisch | [N] | [N] | [N] | [N] | [KURZBESCHREIBUNG] |

## Vollzugsblockaden (Blockierend)
[Jeder blockierende Punkt mit Verantwortlichem und Fälligkeit]

## Kritischer Pfad
[Liste mit Fälligkeiten; gefährdete Punkte hervorgehoben]

## Offene Fragen für Entscheidung
1. [FRAGE] — Entscheidung bis [DATUM] benötigt

## Preisanpassung / Risikoreservierung
[Falls blockierende Findings preisrelevant sind: quantifizierte Risikoschätzung]
```

## Rote Schwellen

- Blockierende Findings ohne Vollzugsplan → sofortige Eskalation an GF/Investoren
- Kritischer Pfad-Punkt mit weniger als 14 Tagen Restzeit → tägliches Tracking
- Neue Vollzugsbedingungen nach Signing entdeckt → SPA-Parteien informieren
- Ebene 3 an Gegenseite gesandt → Mandatsgeheimnis (§ 43a Abs. 2 BRAO) gefährdet

## Quellen und Zitierweise

Normen-Basis je nach DD-Findings. Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Risiken / typische Fehler

- **Ebenenverwirrung:** GF-Kurzfassung niemals mit Arbeitsteam-Vollständigkeit mischen.
- **Preisanpassung ohne Quantifizierung:** Blockierende Findings ohne Risikowert lassen die GF ohne Entscheidungsgrundlage.
- **Vollzugspunkte nicht an Checkliste übergeben:** Diese Zusammenfassung ist der letzte Filter vor dem Vollzug.
- **Verteilungskreis:** Ebene 3 bleibt im Privilegierungskreis; nie an Gegenpartei senden.

---
## Audit-Hinweis (27.05.2026)

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC — das Urteil betrifft Prospekthaftung wegen falscher Darstellung eines Vorgängerfonds (Medienfonds ApolloProMedia, NJW-RR 2010, 911), nicht Aufklaerungspflicht beim Unternehmenskauf.
Maßnahme: Beide Nennungen entfernt (Rechtsprechungsabschnitt und Quellenabschnitt). Kein Ersatz eingefuegt; die verbleibenden drei Urteile decken Due Diligence und Vollzugsverbot zutreffend ab.

## 2. `gesellschafterbeschluss`

**Fokus:** Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG analog) und Anfechtbarkeit (246 AktG analog). Laedt bei Mandaten zur Beschlussfassung, Anfechtungsklage oder Nichtigkeitsfeststellung.

# Gesellschafterbeschluss – GmbH und AG

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafterbeschluss – GmbH und AG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Gesellschafterbeschluss – GmbH und AG
- **Spezialgegenstand:** Gesellschafterbeschluss – GmbH und AG. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor der Bearbeitung folgende Fragen klären:

1. **Rechtsform:** GmbH (§§ 47, 48 GmbHG), AG (§§ 121 ff., 133 ff. AktG) oder GmbH & Co. KG?
2. **Beschlussgegenstand:** Was soll beschlossen werden (Satzungsänderung, Kapitalmaßnahme, GF-Bestellung, Gewinnverteilung)?
3. **Ziel des Mandats:** Beschlussvorbereitung, Wirksamkeitsprüfung eines gefassten Beschlusses oder Anfechtungsklage?
4. **Stimmrechte und Quorum:** Liegt der Gesellschaftsvertrag vor? Sonderregeln zu Mehrheiten?
5. **Stimmverbote:** § 47 Abs. 4 GmbHG oder § 136 AktG einschlägig?
6. **Anfechtungsfrist:** Wann wurde der Beschluss gefasst? (1-Monat-Frist analog § 246 Abs. 1 AktG läuft!)

## Zentrale Normen

§ 46 GmbHG (Zuständigkeitskatalog GV) — § 47 GmbHG (Abstimmung; Stimmrechtsausschluss Abs. 4) — § 48 GmbHG (Versammlung; Umlaufverfahren Abs. 2) — § 51 GmbHG (Einberufung; Frist 1 Woche) — § 53 GmbHG (Satzungsänderung; 3/4-Mehrheit; notarielle Beurkundung) — § 121 AktG (Einberufung HV) — § 133 AktG (Mehrheitsprinzip AG) — § 136 AktG (Stimmrechtsverbot AG) — § 241 AktG (Nichtigkeitsgründe; abschließend) — § 243 AktG (Anfechtbarkeit) — § 246 AktG (Anfechtungsklage; 1-Monat-Frist) — § 249 AktG (Nichtigkeitsklage)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Gesellschafterbeschluss

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Einberufung | Ladungsform (GmbH: eingeschriebener Brief § 51; AG: § 121 AktG); Ladungsfrist (GmbH: 1 Woche; AG: 30 Tage § 123); Tagesordnung vollständig? | Einberufungsmangel → anfechtbar; Heilung möglich |
| 2 | Beschlussfähigkeit | Quorum aus GV/Satzung; bei GmbH ohne Satzungsregelung: jede ordnungsgemäß einberufene GV beschlussfähig | Quorum-Mangel → Beschluss ungültig |
| 3 | Stimmrechte ermitteln | GmbH: je 1 EUR = 1 Stimme (§ 47 Abs. 2); AG: je Aktie (§ 134 Abs. 1) | Stimmrechtsverteilung festgestellt |
| 4 | Stimmrechtsausschluss | § 47 Abs. 4 GmbHG: Entlastung, Befreiung von Verbindlichkeit, Rechtsverfolgung; § 136 AktG analog | Stimmen stimmbefangener Gesellschafter nicht zählen |
| 5 | Mehrheit berechnen | Einfache Mehrheit (§ 47 Abs. 1 GmbHG; § 133 Abs. 1 AktG); qualifizierte 3/4-Mehrheit bei Satzungsänderung (§ 53 Abs. 2 GmbHG; § 179 Abs. 2 AktG) | Mehrheit erreicht? |
| 6 | Protokollierung | GmbH: Protokoll mit Abstimmungsergebnis; Satzungsänderung notariell beurkunden (§ 53 Abs. 2); AG: § 130 AktG notarielle Beurkundung | Formfehler → § 241 Nr. 2 AktG Nichtigkeit |
| 7 | Anfechtbarkeit | Kausalität des Mangels für Beschlussergebnis (Relevanztheorie Quellenprüfung § 243 Rn. 8)? | Anfechtbar aber nicht nichtig |
| 8 | Nichtigkeit | § 241 AktG analog: fehlende Form, Sittenwidrigkeit, zwingende Gesetzesvorschriften verletzt | Nichtig von Anfang an; jedermann kann einwenden |
| 9 | Anfechtungsklage | Frist: 1 Monat ab Beschlussfassung analog § 246 Abs. 1 AktG; Klage gegen Gesellschaft; LG am Sitz | Fristnotiz anlegen! |
| 10 | Heilung | § 242 AktG (Einberufungsmängel nach 3 Jahren); nicht bei § 241 Nr. 3 und 5 AktG | Heilung möglich → Abwarten sinnvoll? |

## Schritt-fuer-Schritt-Workflow

1. **Sachverhalt aufnehmen:** Gesellschaftsvertrag/Satzung lesen; Gesellschafterkreis und Stimmrechte ermitteln.
2. **Einberufung prüfen:** Ladungsform, Ladungsfrist, Tagesordnung auf Vollständigkeit.
3. **Beschlussfähigkeit feststellen:** Quorum aus GV/Satzung; alle Gesellschafter erschienen?
4. **Stimmverbote screenen:** § 47 Abs. 4 GmbHG systematisch für jeden TOP durchgehen.
5. **Mehrheit berechnen:** Gesamtstimmen (ohne stimmbefangene); Mehrheitserfordernis je Beschlussgegenstand.
6. **Beschlusstext formulieren:** Präzise, vollständig, widerspruchsfrei; Abstimmungsergebnis als Zahl.
7. **Protokoll vorbereiten:** TOP-Nummerierung, Beschlusstext, Abstimmungsergebnis, Unterschrift Versammlungsleiter; bei Satzungsänderung Notar beauftragen.
8. **Anfechtbarkeit screenen:** Bei vorhandenen Mängeln Kausalität prüfen (Relevanztheorie).
9. **Fristen notieren:** 1-Monat-Frist analog § 246 AktG sofort kalendarisch sichern.
10. **Ausgabe:** Beschlussvorlage oder Anfechtungs-Memo je nach Mandatsinhalt.

## Output-Template

**Adressat:** Gesellschaft / Gesellschafter / Gericht — **Tonfall:** sachlich-juristisch / präzise

### Beschlussvorlage

```
# Gesellschafterbeschluss
[GESELLSCHAFTSNAME], [HRB-NUMMER]
Gesellschafterversammlung vom [DATUM]

## TOP [N]: [BEZEICHNUNG DES TAGESORDNUNGSPUNKTS]

[Beschlusstext — präzise, vollständig]

Abstimmungsergebnis:
Ja-Stimmen: [N] ([PROZENT] %)
Nein-Stimmen: [N] ([PROZENT] %)
Enthaltungen: [N]
Stimmbefangen: [NAME(N)] gem. § 47 Abs. 4 GmbHG wegen [GRUND]

Der Beschluss ist [angenommen / abgelehnt].

[ORT], den [DATUM]

_________________________________
[VERSAMMLUNGSLEITER]
```

### Anfechtungs-Memo

```
# Anfechtungs-Memo: Beschluss [GESELLSCHAFT] v. [DATUM]

Beschlussgegenstand: [BESCHLUSSINHALT]

Mängel:
1. [MANGEL 1] — Norm: [§] — Kausalität: [ja/nein]
2. [MANGEL 2] — Norm: [§] — Kausalität: [ja/nein]

Anfechtungsklage:
Frist: 1 Monat ab [DATUM] = [ABLAUFDATUM]
Klage gegen: [GESELLSCHAFT] (§ 246 Abs. 2 AktG analog)
Zuständiges Gericht: LG [ORT AM SITZ]

Risikobewertung:
[Anfechtungserfolg: hoch/mittel/gering — Begründung]

Empfehlung:
[Klage unverzüglich einreichen / weitere Sachverhaltsaufklärung / Abstehen]
```

## Rote Schwellen

- Anfechtungsfrist 1 Monat analog § 246 Abs. 1 AktG — sofortige Fristnotiz nach Mandatsannahme
- Fehlende notarielle Beurkundung bei Satzungsänderung → Nichtigkeit nach § 241 Nr. 2 AktG analog
- Stimmrechtsausschluss übersehen → Anfechtbarkeit; Heilung nur möglich wenn kein Berechtigter klagt
- Beschlussfähigkeit nicht festgestellt → gesamter Beschluss ungültig; Sitzung zu wiederholen

## Quellen und Zitierweise

- GmbHG §§ 46, 47, 48, 51, 53, 54
- AktG §§ 121, 130, 133, 134, 136, 179, 241, 243, 246, 249

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Uebergabe an andere Skills

- `gesellschaftsrecht:aufsichtsrat-protokoll` — Protokollierung des Beschlusses
- `gesellschaftsrecht:geschaeftsfuehrer-haftung-43-gmbhg` — wenn Beschluss GF-Entlastung betrifft
- `gesellschaftsrecht:gesellschafterstreit-loesungsstrategie` — wenn Beschluss Teil eines Gesellschafterkonflikts ist

---
## Audit-Hinweis (27.05.2026)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: NOT_FOUND — dejure.org findet zum Datum 10.02.2021 kein Urteil unter diesem Aktenzeichen; NZG 2021, 418 nicht verifizierbar.
Maßnahme: Zitat entfernt. Kein Ersatz eingefügt; die gesetzliche Regelung (§ 48 Abs. 2 GmbHG sowie seit 2022 § 48 Abs. 1 S. 2 GmbHG) ist im Skill durch Normtexte abgedeckt.

## 3. `gesellschafterstreit-loesungsstrategie`

**Fokus:** Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38 GmbHG. Normen § 34 GmbHG Einziehung § 140 HGB analog Ausschluss-Klage § 48 GmbHG Gesellschafterversammlung. Prüfraster Wertbestimmungs-Verfahren Abfindungsberechnung BGH Verkehrswert Schiedsklausel DIS. Output Konflikt-Strategie-Memo mit Verhandlungskonzept Klageoption und Kostenfolge. Abgrenzung: gesellschafterbeschluss für Beschlussfassung mandat-triage für Erst-Abfrage.

# Gesellschafterstreit — Lösungsstrategie

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafterstreit — Lösungsstrategie` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Gesellschafterstreit — Lösungsstrategie
- **Spezialgegenstand:** Gesellschafterstreit — Lösungsstrategie. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor dem Start der strategischen Analyse folgende Fragen klären:

1. **Mandantenrolle:** Mehrheitsgesellschafter, Minderheitsgesellschafter, GF als Beklagter oder Erbe?
2. **Konflikttypus:** Two-Tier-50/50, Mehrheit gegen Minderheit, GF-Konflikt oder Familiengesellschaft?
3. **Eskalationsstufe:** Frühphase (persönlich, lösbar) oder fortgeschrittene Eskalation (Klage droht/läuft)?
4. **Existenzgefahr:** Ist die Gesellschaft durch den Streit in ihrer Existenz bedroht?
5. **Schiedsklausel:** Gibt es eine wirksame Schiedsklausel in der Satzung? (Ordentlicher Rechtsweg ggf. gesperrt)
6. **Anfechtungsfrist:** Falls Beschlussfehler relevant — läuft die 1-Monat-Frist analog § 246 AktG?
7. **Abfindungsrelevanz:** Gibt es bereits konkrete Wertvorstellungen oder Satzungsklauseln zur Abfindung?

## Zentrale Normen

§ 38 GmbHG (Abberufung GF; jederzeit möglich) — § 34 GmbHG (Einziehung von Geschäftsanteilen; Satzungserfordernis) — § 47 GmbHG (Abstimmung; Stimmrechtsausschluss) — § 46 Nr. 8 GmbHG (Gesellschafterbeschluss über Klage gegen GF) — § 140 HGB analog (Ausschlusskiage; auf GmbH analog angewendet) — § 626 BGB (außerordentliche Kündigung; auch GF-Anstellungsvertrag) — §§ 241, 243, 246 AktG analog für GmbH (Beschlussmängelrecht) — §§ 935, 940 ZPO (einstweilige Verfügung) — § 1029 ZPO (Schiedsvereinbarung) — § 313 BGB (Störung der Geschäftsgrundlage)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Gesellschafterstreit-Strategie

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Konflikt-Diagnose | Konflikttypus und Eskalationsstufe bestimmen | Strategierahmen festgelegt |
| 2 | Schiedsklausel | Satzungs-Schiedsklausel vorhanden und wirksam? | Ordentlicher Rechtsweg gesperrt → Schiedsgericht |
| 3 | Fristenlage | Beschluss-Anfechtungsfrist (1 Monat analog § 246 AktG); Abberufungsfrist | Sofortige Fristnotiz |
| 4 | Mediation | Mittlere Eskalation oder Unternehmensexistenz bedroht → Mediation prüfen | Mediationsvorrang oder sofortige Eskalation |
| 5 | Beschluss-Anfechtung | Formfehler? Stimmrechtsausschluss verletzt? Treuepflicht-Verstoß? | Anfechtungsklage analog § 246 AktG |
| 6 | GF-Abberufung | § 38 GmbHG: jederzeit möglich; wichtiger Grund bei § 38 Abs. 2 GmbHG; Anstellungsvertrag separat kündigen | Beschluss GV + Kündigung |
| 7 | Einziehung § 34 GmbHG | Satzungsklausel vorhanden? Einziehungsgrund? Beschluss der GV; Abfindung Verkehrswert | Einziehungsklage vorbereiten |
| 8 | Ausschlussklage | § 140 HGB analog: wichtiger Grund unzumutbar; Klage der Gesellschaft; Abfindung | Klageentwurf |
| 9 | Abfindungsberechnung | Verkehrswert (IDW S 1 Ertragswert) vs. Buchwert-Klausel; Satzungsklausel prüfen auf Sittenwidrigkeit | Wertgutachten beauftragen |
| 10 | Einstweiliger Rechtsschutz | § 935 ZPO: Verfügungsanspruch (Beschlussfehler) und Verfügungsgrund (Eilbedürftigkeit) | Einstweilige Verfügung vorbereiten |
| 11 | BATNA / ZOPA | BATNA beider Seiten; ZOPA ermitteln; wirtschaftliche Folgen ohne Einigung | Verhandlungsrahmen abstecken |
| 12 | Buy-Sell-Klauseln | Russian Roulette / Texas Shootout vorhanden? Aktivierung sinnvoll? | Klausel analysieren und Ablauf simulieren |

## Schritt-fuer-Schritt-Workflow

1. **Sachverhalt aufnehmen:** Satzung, Gesellschafterliste, Beschlussprotokoll, Anstellungsvertrag GF, Wirtschaftsstatus.
2. **Schiedsklausel prüfen:** DIS/ICC/Ad-hoc; bei wirksamer Klausel Schiedsgericht statt ordentliches Gericht.
3. **Fristen sichern:** Anfechtungsfrist 1 Monat analog § 246 AktG sofort kalendarisch sichern.
4. **Mandantenrolle analysieren:** Welche Instrumente stehen dem Mandanten zur Verfügung?
5. **Mediation erwägen:** Bei mittlerer Eskalation und Unternehmensinteresse immer als Erstweg anbieten.
6. **Optionen-Matrix erstellen:** Alle rechtlichen Instrumente mit Vor-/Nachteilen, Zeitrahmen, Kosten gegenüberstellen.
7. **Strategie festlegen:** Welche Kombination von Instrumenten (Anfechtung + einstweilige Verfügung, Einziehung + Abberufung)?
8. **Abfindungsrahmen abstecken:** IDW S 1-Gutachten beauftragen; Buchwert-Klausel auf Sittenwidrigkeit prüfen.
9. **Verhandlungsposition aufbauen:** BATNA beider Seiten; Verhandlungsziele und Roten Linien festlegen.
10. **Klage oder Vergleich:** Wenn Mediation scheitert: Klageentwurf; Vergleichsangebot parallel vorbereiten.

## Output-Template

**Adressat:** Mandant / Kanzlei intern — **Tonfall:** sachlich-strategisch

```
# Gesellschafterstreit-Strategie
Gesellschaft: [FIRMA / HRB-NUMMER]
Mandant: [NAME + ROLLE]
Bearbeitungsstand: [DATUM]

## Konflikt-Diagnose
Konflikttypus: [Two-Tier / Mehrheit-Minderheit / GF-Konflikt / Familie]
Eskalationsstufe: [Früh / Mittel / Hoch / Existenzgefährdend]
Schiedsklausel: [ja/nein; wenn ja: Ordnung + Ort]

## Fristen (KRITISCH)
Anfechtungsfrist: Beschluss v. [DATUM] → Ablauf [DATUM + 1 Monat]
Weitere Fristen: [AUFLISTUNG]

## Optionen-Matrix

| Option | Instrument | Zeitrahmen | Kosten | Risiko |
|---|---|---|---|---|
| Mediation | Neutral | 4-8 Wochen | mittel | Ergebnisoffen |
| Beschluss-Anfechtung | § 246 AktG analog | 6-18 Monate | mittel-hoch | Kausalität |
| GF-Abberufung | § 38 GmbHG + § 626 BGB | 2-4 Wochen | mittel | Anstellungsvertrag |
| Einziehung | § 34 GmbHG | 3-6 Monate | hoch | Abfindungsstreit |
| Ausschlussklage | § 140 HGB analog | 12-24 Monate | hoch | Beweislast |
| Buy-Sell | Satzungsklausel | 30-90 Tage | abhängig | Liquidität |

## Empfohlene Strategie
[Primärempfehlung + Begründung + Zeitplan]

## Abfindungsrahmen
Buchwert (Satzungsklausel): [X EUR]
Verkehrswert (IDW S 1 Schätzung): [Y EUR]
Sittenwidrigkeitsprüfung: [ja/nein]

## Nächste Schritte
1. [MASSNAHME] bis [DATUM]
2. [MASSNAHME] bis [DATUM]
```

## Rote Schwellen

- Anfechtungsfrist 1 Monat analog § 246 AktG läuft → sofortige Klage oder bewusstes Abstehen dokumentieren
- Gesellschaft zahlungsunfähig während des Konflikts → § 15a InsO; sofort Insolvenzrecht einbeziehen
- Existenzgefährdung durch Pattsituation → einstweilige Verfügung § 935 ZPO prüfen
- Abfindungsklausel Buchwert und Differenz zum Verkehrswert mehr als 50 % → Sittenwidrigkeit § 138 BGB prüfen

## Quellen und Vertiefung

- GmbHG §§ 34, 38, 39, 46, 47
- HGB § 140
- BGB §§ 138, 626, 738
- AktG §§ 241, 246
- ZPO §§ 935, 1029
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/K. Schmidt, GmbHG, 12. Aufl. 2021, § 34 Rn. 1 ff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsrecht:gesellschafterbeschluss` — Beschlussanfechtung und Nichtigkeitsklage
- `gesellschaftsrecht:geschaeftsfuehrer-haftung-43-gmbhg` — wenn GF-Haftungsvorwürfe Teil des Konflikts
- `gesellschaftsrecht:aufsichtsrat-protokoll` — wenn AR-Gremium in Konflikt involviert
- `gesellschaftsrecht:mandat-triage-gesellschaftsrecht` — Mandatsaufnahme bei neuem Streit

---
## Audit-Hinweis (27.05.2026)

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC — das Urteil betrifft die Zulaessigkeit von Hinauskuendigungsklauseln in Form einer Vesting-Regelung (Managermodell, BGHZ 164, 98), nicht den Ausschluss analog § 140 HGB. Die Fundstelle NJW 2005, 3569 ist nicht korrekt.
Maßnahme: Beide Nennungen entfernt. Kein Ersatz eingefuegt; der Ausschlussklagen-Stoff ist ueber BGH II ZR 25/82 (Abfindung/Sittenwidrigkeit) und den Normenhinweis § 140 HGB analog teilweise abgedeckt.

## 4. `gesellschafts-compliance`

**Fokus:** Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger und Rechtsordnung und zeigt auf, was in den nächsten 30/60/90 Tagen fällig ist. Trigger: "Gesellschafts-Compliance", "Einreichungsfristen", "Bilanzpublizität", "Transparenzregister", "Jahresabschluss einreichen", "was ist fällig".

# Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)
- **Spezialgegenstand:** Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister). Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Kernsachverhalt

Kapitalgesellschaften und Personengesellschaften unterliegen einer Vielzahl periodisch wiederkehrender gesellschaftsrechtlicher und handelsrechtlicher Pflichten: Jahresabschluss-Offenlegung beim Unternehmensregister (§ 325 HGB), Einreichung der aktuellen Gesellschafterliste beim Handelsregister (§ 40 GmbHG), Meldung wirtschaftlich Berechtigter beim Transparenzregister (§ 20 GwG) sowie — bei prüfungspflichtigen Gesellschaften — Jahresabschlussprüfung (§ 316 HGB). Verstöße gegen diese Pflichten haben unterschiedliche Konsequenzen: Ordnungsgeldverfahren (§ 335 HGB), Bußgelder (§§ 56 f. GwG), strafrechtliche Risiken (§ 331 HGB) und — bei veralteter Gesellschafterliste — Gefährdung des gutgläubigen Erwerbs (§ 16 Abs. 3 GmbHG).

Dieser Skill pflegt einen einzigen YAML-Tracker für alle Gesellschaften eines Mandanten und berechnet, was wann und für wen fällig ist.

## Kaltstart-Rückfragen

Vor der Tracker-Initialisierung sind folgende Angaben erforderlich:

1. **Gesellschaftstabelle:** Welche Gesellschaften sind zu erfassen (Name, Rechtsform, Handelsregisternummer, Registergericht, Gründungsdatum, Geschäftsjahresende)?
2. **Größenklassen:** Bilanzsumme, Umsatzerlöse, Arbeitnehmerzahl für jede GmbH/AG (§ 267 HGB) — um Prüfungspflicht und Offenlegungsumfang zu bestimmen?
3. **Letzter Einreichungsstand:** Wann wurde der Jahresabschluss zuletzt beim Bundesanzeiger eingereicht? Liegt die aktuelle Gesellschafterliste beim Handelsregister?
4. **Transparenzregister:** Sind wirtschaftlich Berechtigte (§ 3 GwG) im Transparenzregister eingetragen oder gilt eine Eintragungsausnahme nach § 20 Abs. 2 GwG (Eintragung im Handelsregister)?
5. **Konzernstruktur:** Gibt es Mutter-Tochter-Verhältnisse, die einen Konzernabschluss nach §§ 290 ff. HGB auslösen könnten?
6. **Ruhende oder aufzulösende Gesellschaften:** Sind Gesellschaften betrieblich inaktiv? Sollen sie aufgelöst werden (§ 65 GmbHG, §§ 264 ff. AktG)?
7. **Ausländische Tochtergesellschaften:** Gibt es § 325a HGB-Pflichten für ausländische Tochtergesellschaften?
8. **Berichtszeitraum:** 30, 60 oder 90 Tage für den Fälligkeitsbericht?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte mit Auszügen

**§ 325 Abs. 1 HGB — Bilanzpublizität (Offenlegungspflicht)**
> "Die gesetzlichen Vertreter von Kapitalgesellschaften haben [...] den Jahresabschluss und den Lagebericht [...] beim Betreiber des Bundesanzeigers elektronisch einzureichen."

Frist: § 325 Abs. 1a HGB — spätestens 12 Monate nach Ende des Geschäftsjahres. Kleine Kapitalgesellschaften (§ 267 Abs. 1 HGB) können vereinfachte Unterlagen einreichen; nur Bilanz und Anhang, kein GuV-Ausweis.

**§ 335 HGB — Ordnungsgeldverfahren**
> Wer § 325 HGB verletzt, kann vom Bundesamt für Justiz (BfJ) zur Einreichung angehalten und mit Ordnungsgeld belegt werden. Mindestordnungsgeld: 2.500 EUR; Maximum: 25.000 EUR je Verstoß. Verfahren beginnt von Amts wegen, sobald fristgerecht keine Einreichung erfolgt.

**§ 40 GmbHG — Gesellschafterliste**
> "Notare, die in Angelegenheiten der Gesellschaft tätig werden, haben [...] eine von ihnen unterschriebene, aktualisierte Gesellschafterliste [...] zum Handelsregister einzureichen."

Frist: unverzüglich nach jeder Änderung (Abtretung, Kapitalerhöhung, Erbfolge). Pflicht des Notars bei notarieller Beurkundung; sonst Geschäftsführer (§ 40 Abs. 2 GmbHG). Konsequenz veralteter Liste: Gutgläubiger Erwerb nach § 16 Abs. 3 GmbHG kann zustande kommen, wenn Erwerber auf die unrichtige Liste vertraut.

**§ 16 Abs. 3 GmbHG — Gutgläubiger Erwerb**
> "Ist die im Handelsregister eingetragene Gesellschafterliste unrichtig, so kann ein Erwerber, der auf die Richtigkeit der Liste vertraut, gutgläubig Anteile erwerben."

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§§ 18 ff., 20 GwG — Transparenzregister**
> § 20 GwG verpflichtet juristische Personen des Privatrechts und eingetragene Personengesellschaften, die wirtschaftlich Berechtigten (§ 3 GwG) beim Transparenzregister anzumelden.

Frist: 2 Wochen nach Änderung der Beteiligungsverhältnisse. Ausnahme: § 20 Abs. 2 GwG — Eintragungspflicht gilt nicht, wenn die wirtschaftlich Berechtigten bereits aus öffentlich zugänglichen Registern (Handelsregister, Genossenschaftsregister) erkennbar sind. Seit 01.08.2021 ist das Transparenzregister ein Vollregister (keine reine Auffangfunktion mehr); § 59 Abs. 1 GwG: Übergangsfrist bis 31.03.2022 für GmbH.

**§ 267 HGB — Größenklassen**

| Klasse | Bilanzsumme | Umsatzerlöse | Arbeitnehmer (Jahresdurchschnitt) |
|---|---|---|---|
| Klein (§ 267 Abs. 1 HGB) | ≤ 7.500.000 EUR | ≤ 15.000.000 EUR | ≤ 50 |
| Mittelgroß (§ 267 Abs. 2 HGB) | ≤ 25.000.000 EUR | ≤ 50.000.000 EUR | ≤ 250 |
| Groß (§ 267 Abs. 3 HGB) | > 25.000.000 EUR | > 50.000.000 EUR | > 250 |

Zwei von drei Merkmalen müssen an zwei aufeinanderfolgenden Abschlussstichtagen erfüllt sein (§ 267 Abs. 4 HGB). `[Modellwissen — Schwellenwerte beim BfJ/Unternehmensregister bestätigen]`

**§ 316 HGB — Prüfungspflicht**
> "Der Jahresabschluss und der Lagebericht von Kapitalgesellschaften, die nicht kleine Kapitalgesellschaften sind, sind durch einen Abschlussprüfer zu prüfen."

Gilt für alle AG (keine Größenklassenausnahme). GmbH: Prüfungspflicht ab mittelgroß. Ohne Testierung darf der Abschluss nicht festgestellt werden.

**§ 290 HGB — Konzernabschlusspflicht**
> "Die gesetzlichen Vertreter einer Kapitalgesellschaft haben einen Konzernabschluss und einen Konzernlagebericht aufzustellen, wenn diese Kapitalgesellschaft auf eine andere Gesellschaft einen beherrschenden Einfluss ausüben kann."

**§ 325a HGB — Zweigniederlassungen ausländischer Gesellschaften**
> Bestimmte ausländische Gesellschaften mit Zweigniederlassung in Deutschland müssen Jahresabschlüsse in Deutschland offenlegen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Compliance-Initialisierung und laufender Betrieb


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Gesellschaftserfassung | Alle Gesellschaften mit Rechtsform, HR-Nummer, Gründungsdatum, GJ-Ende erfasst? | Vollständige Gesellschaftsliste als Basis des Trackers |
| 2 | Größenklassenbestimmung | § 267 HGB: Bilanzsumme, Umsatz, Arbeitnehmer für jede GmbH/AG; zwei-Kriterien-Test an zwei aufeinanderfolgenden Stichtagen | Festlegung der Offenlegungspflicht und des Prüfungsumfangs |
| 3 | Prüfungspflicht | § 316 HGB: AG (immer); GmbH mittelgroß/groß; Stiftungen / Genossenschaften nach §§ 340, 341 HGB? | Bestellung Abschlussprüfer vor GJ-Ende; Listenmandant: Jahresplan |
| 4 | Offenlegungsfrist § 325 HGB | 12 Monate nach GJ-Ende; bei börsennotierter AG: 4 Monate (§ 325 Abs. 4 HGB)? | Fälligkeitsdaten in Tracker eintragen; Frühwarnung 90 Tage vor Frist |
| 5 | Gesellschafterliste § 40 GmbHG | Letzte Einreichung beim HR; Änderungen seit letzter Einreichung (Abtretungen, Kapitalerhöhungen, Erbfolgen)? | Unverzügliche Einreichung bei Änderung; Stichtag des aktuellen Standes notieren |
| 6 | Transparenzregister § 20 GwG | Wirtschaftlich Berechtigte eingetragen? Eintragungsausnahme § 20 Abs. 2 GwG geprüft? | Bei fehlender oder veralteter Eintragung: 2-Wochen-Frist nach Änderung beachten |
| 7 | Konzernabschluss § 290 HGB | Beherrschender Einfluss auf andere Gesellschaften? Befreiungsmöglichkeit §§ 291–293 HGB (Konzern-Muttergesellschaft im Ausland)? | Konzernabschluss-Pflicht oder Befreiungssachverhalt dokumentieren |
| 8 | Ruhende Gesellschaften | Gesellschaft operativ inaktiv? Auflösung geplant? Tragekosten berechnet (HR-Gebühren, Steuer, RA-Honorar)? | Auflösung bei wirtschaftlich sinnloser Fortführung empfehlen (§ 65 GmbHG) |
| 9 | Ordnungsgeldgefahr | Einreichungsfrist überschritten ohne Einreichung? BfJ-Verfahren bereits eingeleitet? | Sofortige Nachreichung + Stellungnahme zum Ordnungsgeldantrag |
| 10 | Status-Pflege | Alle erledigten Pflichten im Tracker mit Datum und Nachweis (Bundesanzeiger-Veröffentlichungsnummer, HR-Eintragungsdatum) aktualisiert? | Lückenloser Einreichungsnachweis für M&A-Due-Diligence und Behörden |
| 11 | 30/60/90-Tage-Vorschau | Welche Pflichten werden in den nächsten 30, 60 oder 90 Tagen fällig? | Fälligkeitsbericht für Mandant und Kanzleikalender |
| 12 | Jahresabschluss-Feststellung | Feststellung des Jahresabschlusses vor Offenlegung: bei GmbH durch Gesellschafterversammlung (§ 46 Nr. 1 GmbHG); bei AG durch Vorstand + AR oder HV (§§ 172 f. AktG)? | Organübergreifende Terminplanung: Prüfung → Feststellung → Offenlegung |
| 13 | Jahresabschluss-Feststellungsfrist | § 264 Abs. 1 HGB: Kaufmännischer Jahresabschluss muss innerhalb der einem ordnungsgemäßen Geschäftsgang entsprechenden Zeit aufgestellt werden | Bei GmbH: spätestens in 3 Monaten nach GJ-Ende (§ 264 Abs. 1 S. 3 HGB, i.d.F. BilMoG) |
| 14 | Export und Reporting | Tracker exportiert als CSV / Tabelle für Mandant, Steuerberater, WP? | Jahresplanung mit externen Beratern abgestimmt |
| 15 | Audit-Nachverfolgung | Letzte Audit-Überprüfung > 12 Monate zurück? Transparenzregister nicht geprüft? | Gesundheits-Audit durchführen (Modus 4) |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Fristgerechte Offenlegung § 325 HGB | Gesellschaft / gesetzlicher Vertreter | Nachweis durch Bundesanzeiger-Veröffentlichungsnummer und Datum |
| Gutgläubiger Erwerb § 16 Abs. 3 GmbHG | Erwerber muss Gutgläubigkeit darlegen | Unrichtigkeit der Liste: objektiv; Kenntnis des Erwerbers: subjektiv (Erwerber muss fehlendes Wissen beweisen) |
| Ordnungsgemäße Transparenzregister-Eintragung | Gesellschaft (Transparenzregister-Auszug als Nachweis) | Bußgeldverfahren: Behörde trägt Beweislast für den Verstoß; Gesellschaft muss Eintragung nachweisen |
| Prüfungspflicht besteht nicht (§ 316 HGB) | Gesellschaft (Nachweis Kleinunternehmen nach § 267 HGB) | Nachweis durch Jahresabschluss der zwei vorangegangenen Geschäftsjahre |
| Gesellschafterliste aktuell (§ 40 GmbHG) | Notar / Geschäftsführer | Nachweis durch aktuellen HR-Auszug mit Datumsangabe der letzten Änderung |

## Fristen und Verjährung

| Pflicht | Frist | Norm | Konsequenz bei Versäumnis |
|---|---|---|---|
| Jahresabschluss-Offenlegung | 12 Monate nach GJ-Ende | § 325 Abs. 1a HGB | Ordnungsgeldverfahren BfJ (§ 335 HGB); mind. 2.500 EUR |
| Jahresabschluss-Offenlegung börsennotierte AG | 4 Monate nach GJ-Ende | § 325 Abs. 4 HGB | Zusätzlich WpHG-Sanktionen, MAR-Pflichten |
| Gesellschafterliste | Unverzüglich nach Änderung | § 40 GmbHG | Gutgläubiger Erwerb (§ 16 Abs. 3 GmbHG); Haftung Geschäftsführer |
| Transparenzregister-Eintragung | 2 Wochen nach Änderung | § 20 GwG | Bußgeld §§ 56 f. GwG bis 1.000.000 EUR (vorsätzlich) oder 500.000 EUR (fahrlässig) |
| Jahresabschluss-Aufstellung GmbH | 3 Monate nach GJ-Ende | § 264 Abs. 1 S. 3 HGB | Pflichtverletzung Geschäftsführer; Schadensersatz § 43 GmbHG |
| HV-Einberufung AG | Binnen 8 Monate nach GJ-Ende | § 175 AktG | Ordnungswidrigkeitenrisiko; Aktionärsrechte gefährdet |
| Konzernabschluss-Offenlegung | 12 Monate nach GJ-Ende | § 325 HGB i.V.m. § 290 HGB | Ordnungsgeldverfahren BfJ |
| Ordnungsgeld-Widerspruch | 1 Monat nach Zustellung | § 335 Abs. 3 HGB | Ordnungsgeld wird bestandskräftig |
| Verjährung Ordnungsgeldbescheid | 3 Jahre (Verjährungsfrist OWiG) | § 31 OWiG | Nach Ablauf kein Vollzug mehr |

## Typische Gegenargumente

| Einwand | Begründung Gegenseite | Erwiderung |
|---|---|---|
| Kleine GmbH muss keinen GuV offenlegen | § 326 HGB: kleine GmbH nur Bilanz + Anhang | Richtig — aber Bilanz + Anhang müssen trotzdem fristgerecht eingereicht werden; häufig wird auch die verkürzte Offenlegung versäumt |
| Gesellschafterliste ist aktuell — Notar hat nicht gehandelt | Pflicht liegt beim Notar (§ 40 Abs. 1 GmbHG) | Bei eigener Erkenntnis der Änderung trifft den Geschäftsführer Subsidiärpflicht (§ 40 Abs. 2 GmbHG); Haftungsrisiko des GF prüfen |
| Transparenzregister-Eintragung entbehrlich wegen HR-Eintragung | § 20 Abs. 2 GwG: Mitteilung entbehrlich, wenn Angaben aus anderen Registern erkennbar | Seit 01.08.2021 Vollregister; Ausnahme gilt nur noch für exakt übereinstimmende Angaben; im Zweifel aktiv eingetragen lassen |
| Offenlegung verspätet, aber Ordnungsgeldverfahren noch nicht eingeleitet | Kein Schaden eingetreten | BfJ leitet Verfahren von Amts wegen ein; nachträgliche Einreichung mindert das Ordnungsgeld, hebt es aber nicht auf; unverzügliche Nachreichung + Erklärung einreichen |
| GJ nicht zum 31.12 — Frist läuft anders | Richtig: 12 Monate nach individuellem GJ-Ende | Tracker muss GJ-Ende je Gesellschaft individuell erfassen; Standardannahme 31.12. kann falsch sein |
| Prüfungspflicht entfällt, weil Gesellschaft geschrumpft | § 267 Abs. 4 HGB: Größenklassenwechsel erst nach zwei aufeinanderfolgenden Abschlussstichtagen | Prüfungspflicht besteht noch ein weiteres Jahr nach Unterschreiten der Schwellen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Compliance-Programm initialisierten oder pruefen | Compliance-Schema nach Checkliste; Template unten |
| Variante A — Kleines Unternehmen kein Budget fuer umfangreiches Programm | Minimalanforderungen-Compliance-Set statt Vollprogramm |
| Variante B — Branchenspezifische Anforderungen GwG DSGVO | Branchen-spezifisches Compliance-Modul einsetzen |
| Variante C — Bereits Ermittlungsverfahren laeuft | Compliance-Untersuchung als Verteidigung; Kooperation mit Behoerden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Widerspruch gegen Ordnungsgeldbescheid (§ 335 HGB)

```
An das
Bundesamt für Justiz
Referat IV 4
53094 Bonn

[Mandant / Gesellschaft]
[Anschrift]

[Ort, Datum]

Az. [Ordnungsgeldaktenzeichen]

Widerspruch gegen den Ordnungsgeldbescheid vom [Datum]

Sehr geehrte Damen und Herren,

wir vertreten die [Gesellschaft], [HR-Nummer], [Anschrift], in der oben bezeichneten
Angelegenheit. Gegen den Ordnungsgeldbescheid vom [Datum], der unserer Mandantin am
[Datum] zugegangen ist, legen wir hiermit

 W i d e r s p r u c h

ein.

Begründung:

Der Jahresabschluss der [Gesellschaft] für das Geschäftsjahr [Jahr] wurde am [Datum] beim
Betreiber des Bundesanzeigers eingereicht. Der Bundesanzeiger-Veröffentlichungscode lautet:
[Code].

Die verspätete Einreichung ist auf [konkrete Begründung: Prüfungsverzögerung durch
Wirtschaftsprüfer / IT-Umstellung / externe Umstände] zurückzuführen, für die der
gesetzliche Vertreter keine Verantwortung trägt. Wir bitten, dies bei der
Ordnungsgeldbemessung zu berücksichtigen.

Wir bitten höflich, das Ordnungsgeldverfahren einzustellen und den Bescheid aufzuheben.

Mit freundlichen Grüßen
[Kanzlei / Name]
Rechtsanwalt / Rechtsanwältin

Anlage: Bundesanzeiger-Veröffentlichungsbestätigung vom [Datum]
```

### Baustein 2: Aufforderungsschreiben an Geschäftsführer zur Einreichung Gesellschafterliste

```
An den Geschäftsführer
[Name GmbH]
[Anschrift]

[Ort, Datum]

Handelsregister-Einreichung der Gesellschafterliste (§ 40 GmbHG) — dringende Fristsetzung

Sehr geehrter Herr/Frau [Name],

in Ihrer Eigenschaft als Geschäftsführer der [Name GmbH] sind Sie gemäß § 40 Abs. 2
GmbHG verpflichtet, nach jeder Änderung der Beteiligungsverhältnisse eine aktualisierte
Gesellschafterliste unverzüglich zum Handelsregister einzureichen.

Die Abtretung der Geschäftsanteile des Herrn [Name] an [Erwerber] wurde am [Datum]
notariell beurkundet und ist noch nicht in der beim Handelsregister hinterlegten
Gesellschafterliste (Stand: [Datum]) eingetragen.

Wir fordern Sie auf, spätestens bis zum [Datum = 10 Tage] die aktualisierte
Gesellschafterliste beim Amtsgericht [Registergericht] zur Aufnahme in das
Handelsregister einzureichen.

Wir weisen darauf hin, dass eine nicht ordnungsgemäß eingetragene Gesellschafterliste
das Risiko eines gutgläubigen Erwerbs gemäß § 16 Abs. 3 GmbHG begründet.

Mit freundlichen Grüßen
[Kanzlei / Name]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


### Baustein 3: Gesellschafts-Compliance-Tracker YAML (vollständig)

```yaml
# Gesellschafts-Compliance-Tracker
# Erstellt: [JJJJ-MM-TT]
# Zuletzt aktualisiert: [JJJJ-MM-TT]
# HINWEIS: Fristen sind nur Referenz — beim Bundesanzeiger/HR/TR bestätigen

metadaten:
 unternehmen: "[Konzern- / Mandantenname]"
 erstellt: "[Datum]"
 zuletzt_aktualisiert: "[Datum]"
 letztes_audit: null

gesellschaften:
 - name: "Alpha GmbH"
 typ: "GmbH"
 handelsregisternummer: "HRB 12345"
 registergericht: "Amtsgericht München"
 gruendungsdatum: "2015-01-10"
 status: "aktiv"
 groessenklasse: "mittelgroß § 267 Abs. 2 HGB"
 geschaeftsjahr_ende: "12-31"
 abschlusspruefung_pflicht: "ja"
 gesellschafter_liste_aktuell: "2025-11-15"
 notizen: "Abtretung März 2026 noch nicht eingetragen"

 pflichten:
 - typ: "Jahresabschluss § 325 HGB"
 faellig: "2026-12-31"
 faelligkeits_grundlage: "GJ-Ende 31.12.2025 + 12 Monate"
 zuletzt_eingereicht: "2025-10-15"
 status: "aktuell"
 notizen: "GJ 2025 bis 31.12.2026 einzureichen"

 - typ: "Gesellschafterliste § 40 GmbHG"
 faellig: "2026-04-05"
 faelligkeits_grundlage: "Unverzüglich nach Abtretung März 2026"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Abtretung v. 20.03.2026 noch nicht eingetragen; GF aufgefordert"

 - typ: "Transparenzregister § 20 GwG"
 faellig: "2026-04-03"
 faelligkeits_grundlage: "Änderung wirtschaftlich Berechtigter März 2026 + 2 Wochen"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Neuer wirtschaftlich Berechtigter nach Abtretung"

 - typ: "Jahresabschlussprüfung § 316 HGB"
 faellig: "2026-05-31"
 faelligkeits_grundlage: "Vor Feststellung und Offenlegung GJ 2025"
 zuletzt_eingereicht: null
 status: "bald_fällig"
 notizen: "Prüfungsauftrag an KPMG erteilt 01.02.2026"
```

## Tracker-Datei (technische Beschreibung)

Pfad: `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/gesellschaften/compliance-tracker.yaml`

**Status-Werte:**
- `aktuell` — eingereicht für laufende Periode; nichts fällig in 90 Tagen
- `bald_fällig` — fällig innerhalb von 90 Tagen
- `überfällig` — Fälligkeitsdatum überschritten ohne eingetragenes Einreichungsdatum
- `unbekannt` — keine Information; manuelle Bestätigung erforderlich

## Wichtiger Hinweis zu Fristen

> Die Einreichungsfristen spiegeln öffentlich verfügbare gesetzliche Anforderungen wider. Fristen und Anforderungen können sich ändern. **Fristen immer mit dem Bundesamt für Justiz (§ 335 HGB), dem Handelsregister oder dem Transparenzregister direkt bestätigen, bevor sie für Compliance-Zwecke verwendet werden.** `[Modellwissen — prüfen]`

## Modus 1: Initialisierung

Ohne Tracker oder mit `--rebuild`.

### Schritt 1: Gesellschaftstabelle laden

Aus Praxisprofil `## Gesellschafts-Compliance` → Gesellschaftstabelle. Falls vorhanden: direkt verwenden. Falls nicht: Kaltstart-Rückfragen stellen.

### Schritt 2: Für jede Gesellschaft Pflichten ermitteln

**GmbH — Standardpflichten:**

| Pflicht | Norm | Frist | Konsequenz bei Verstoß |
|---|---|---|---|
| Jahresabschluss Offenlegung | § 325 Abs. 1 HGB | 12 Monate nach GJ-Ende | Ordnungsgeld BfJ § 335 HGB (mind. 2.500 EUR) |
| Gesellschafterliste | § 40 GmbHG | Unverzüglich nach Änderung | Gutgläubiger Erwerb § 16 Abs. 3 GmbHG; Haftung GF § 43 GmbHG |
| Transparenzregister | § 20 GwG | 2 Wochen nach Änderung | Bußgeld §§ 56 f. GwG bis 1.000.000 EUR |
| Jahresabschlussprüfung | § 316 HGB | Vor Offenlegung (mittelgroß/groß) | Strafbarkeit § 331 HGB; keine Testierung |

**AG — Standardpflichten:**

| Pflicht | Norm | Frist |
|---|---|---|
| Jahresabschluss Offenlegung | § 325 HGB | 12 Monate; börsennotiert: 4 Monate |
| Prüfpflicht | § 316 HGB | Alle AG (keine Größenausnahme) |
| HV-Einberufung (Jahresabschluss) | § 175 AktG | Binnen 8 Monate nach GJ-Ende |
| Transparenzregister | § 20 GwG | 2 Wochen nach Änderung |

### Schritt 3: Tracker schreiben

Compliance-Tracker mit allen Gesellschaften und berechneten Pflichten generieren.

## Modus 2: Bericht

```
/gesellschaftsrecht:gesellschafts-compliance --bericht [--tage 30|60|90|180]
```

```
GESELLSCHAFTS-COMPLIANCE-BERICHT — [Datum]
[Unternehmensname]

ÜBERFÄLLIG ([N]):
 [Gesellschaft] / [Pflicht] — war fällig am [Datum]

FÄLLIG INNERHALB [N] TAGE ([N]):
 [Gesellschaft] / [Pflicht] — fällig [Datum]

KÜRZLICH EINGEREICHT ([N] in letzten 90 Tagen):
 [Gesellschaft] / [Pflicht] — eingereicht [Datum]

UNBEKANNTER STATUS ([N]):
 [Gesellschaft] / [Pflicht] — keine Information; direkt beim Registerführer bestätigen

TRANSPARENZREGISTER:
 Zuletzt geprüft: [Datum]
 Gesellschaften mit aktueller Eintragung: [N] von [N]
 Gesellschaften ohne Prüfung in letzten 12 Monaten: [Liste]
```

## Modus 3: Update

### Folgenreiche-Handlung-Sperre (Einreichung)

Falls Rolle **Nichtjurist**:
> Eine Jahresabschluss-Einreichung beim Bundesanzeiger oder eine Handelsregistereintragung hat rechtliche Konsequenzen. Vor Einreichung mit einem Rechtsanwalt oder Steuerberater besprechen. `[Prüfen]`

Manuelles Update:
> "Jahresabschluss der Alpha GmbH zum 31.12.2025 am 05.03.2026 beim Bundesanzeiger eingereicht."

Massen-Update: Wirtschaftsprüfer-Bericht oder HR-Auszug hochladen; Matching-Gesellschaften automatisch aktualisieren.

## Modus 4: Gesundheits-Audit

```
/gesellschaftsrecht:gesellschafts-compliance --audit
```

**Einreichungs-Compliance:** Überfällige und unbekannte Punkte.

**Gesellschaftsgesundheit:**
- Ruhende Gesellschaften: Auflösung (§ 65 GmbHG) sinnvoller als Weiterbetrieb?
- Fehlende Gründungsdaten: Fristberechnung unzuverlässig.
- Gesellschafterliste veraltet: Risiko gutgläubiger Erwerb (§ 16 Abs. 3 GmbHG).

**Transparenzregister-Lücken:** Gesellschaften ohne Eintragung oder ohne geprüfte Ausnahme.

**Bilanzpublizitäts-Lücken:** Offenlegung > 12 Monate zurück = Ordnungsgeldgefahr.

**Konzern-Pflichten:** § 290 HGB-Konzernabschluss-Pflicht; § 325a HGB für ausländische Töchter.

```
GESELLSCHAFTS-GESUNDHEITS-AUDIT — [Datum]

EINREICHUNGS-COMPLIANCE
 Überfällig: [N]
 Unbekannter Status: [N]

RUHENDE GESELLSCHAFTEN ([N])
 [Liste mit Alter und jährlichen Tragekosten]

TRANSPARENZREGISTER
 Nicht eingetragen / geprüft: [N] Gesellschaften

BILANZPUBLIZITÄT § 325 HGB
 Überfällig (>12 Monate): [N] Gesellschaften
 Ordnungsgeldgefahr BfJ: [Liste]

EMPFOHLENE MASSNAHMEN
 1. [Höchste Priorität]
 2. [etc.]
```

## Modus 5: Export

```
/gesellschaftsrecht:gesellschafts-compliance --export [--format csv|tabelle]
```

CSV-Spalten: `Gesellschaftsname, Typ, HR-Nummer, Registergericht, Gründungsdatum, Status, Größenklasse, GJ-Ende, Pflicht, Fällig, Zuletzt eingereicht, Notizen`

## Streitwert und Kosten

| Verstoß | Sanktionsrahmen | Rechtsgrundlage |
|---|---|---|
| Verspätete Offenlegung § 325 HGB | Ordnungsgeld 2.500 – 25.000 EUR je Verstoß; Wiederholung möglich | § 335 HGB |
| Verletzung Transparenzregisterpflicht (vorsätzlich) | Bußgeld bis 1.000.000 EUR | § 56 Abs. 1 GwG |
| Verletzung Transparenzregisterpflicht (fahrlässig) | Bußgeld bis 500.000 EUR | § 56 Abs. 1 GwG |
| Falsche Jahresabschlussunterlagen § 331 HGB | Freiheitsstrafe bis 3 Jahre oder Geldstrafe | § 331 HGB |
| Haftung GF für veraltete Gesellschafterliste | Schadensersatz nach § 43 GmbHG | § 43 GmbHG; § 16 Abs. 3 GmbHG |
| RA-Beratungshonorar Ordnungsgeldwiderspruch | Gegenstandswert = Ordnungsgeldbetrag; 2 Gebühren (§§ 13, 14 RVG) | RVG Nr. 2300 |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Mandant hat 10+ Gesellschaften und keine strukturierte Fristübersicht | Compliance-Tracker initialisieren; jährlicher Audit-Termin im Kanzleikalender; automatische 90-Tage-Frühwarnung |
| BfJ-Ordnungsgeldverfahren läuft | Sofortige Nachreichung + Widerspruch mit Begründung der Verspätungsursache; Ordnungsgeld wird bei unverzüglicher Nachreichung häufig reduziert |
| Abtretung ohne Notar / ohne Gesellschafterlisten-Update | Notar beauftragen; Gesellschafterliste unverzüglich einreichen; Transparenzregister-Meldung binnen 2 Wochen |
| M&A-Due-Diligence: Gesellschafterliste veraltet | Verkäufer-Garantie für ordnungsgemäße Gesellschafterliste verlangen; gutgläubigen Erwerb durch Dritte ausschließen; Closing-Bedingung: aktuelle HR-Liste |
| Größenklassenwechsel in Sichtweite | § 267 Abs. 4 HGB-Zweijahresregel prüfen; wenn zweites Jahr unter Schwellen: Prüfungspflicht entfällt; Prüfungsvertrag ggf. nicht verlängern |
| Ruhende Gesellschaft seit > 3 Jahren | Formale Auflösung (§ 65 GmbHG) prüfen; Kostenersparnis (HR-Gebühren, Buchhaltung, Steuern) gegen Auflösungsaufwand abwägen |

## Output-Template

**Adressat:** Mandant / Geschaeftsfuehrer / Complianceverantwortlicher — Tonfall: sachlich-strukturiert, handlungsorientiert

```
GESELLSCHAFTS-COMPLIANCE-BERICHT
Mandat/Praxis: [MANDATSCODE / PRAXISNAME]
Erstellt von: [NAME], [KANZLEI]
Datum: [TT.MM.JJJJ]
Berichtszeitraum: [DATUM] bis [DATUM]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.

--- PORTFOLIOÜBERSICHT ---
Gesellschaften gesamt: [N]
Status aktiv: [N] | ruhend: [N] | unbekannt: [N]

--- BILANZPUBLIZITAET § 325 HGB ---
Frist 12 Monate nach Geschaeftsjahresende

| Gesellschaft | GJ-Ende | Offenlegungsfrist | Eingereicht | Status |
|---|---|---|---|---|
| [NAME GmbH] | [TT.MM.JJJJ] | [TT.MM.JJJJ] | [TT.MM.JJJJ / OFFEN] | [OK / UEBERFAELLIG / ORDNUNGSGELD] |

Ordnungsgeldgefahr (§ 335 HGB): [N] Gesellschaften
Hoechstes Risiko: [NAME], ueberfaellig seit [N] Tagen (drohendes Ordnungsgeld: bis [BETRAG] EUR)

--- GESELLSCHAFTERLISTE § 40 GmbHG ---
Zuletzt eingereicht: [DATUM] / noch nicht eingereicht
Aendering: [BESCHREIBUNG] am [DATUM]
Handlungsbedarf: [JA — Notar beauftragen bis TT.MM.JJJJ / NEIN]

--- TRANSPARENZREGISTER §§ 18 ff. GwG ---
Beguenstigter(wirtschaftlich Berechtigter): [NAME], [BETEILIGUNG] %
Letztes Update: [DATUM]
Status: [AKTUELL / AENDERUNG ERFORDERLICH bis TT.MM.JJJJ]

--- PRÜFUNGSPFLICHT § 316 HGB ---
| Gesellschaft | Groessenklasse | Pruefungspflichtig | Pruefungsauftrag erteilt |
|---|---|---|---|
| [NAME] | [Gross / Mittel / Klein] | [JA / NEIN] | [DATUM / OFFEN] |

--- EMPFOHLENE MASSNAHMEN (PRIORISIERT) ---
1. [HOECHSTE PRIORITAET] — Frist: [DATUM] — verantwortlich: [PERSON]
2. [MITTLERE PRIORITAET] — Frist: [DATUM] — verantwortlich: [PERSON]
3. [NIEDRIGE PRIORITAET] — keine akute Frist

--- NAECHSTER AUDIT-TERMIN ---
[DATUM] (Empfehlung: jaehrlich, 90 Tage vor GJ-Ende)
```

## Rote Schwellen

- **Bilanzpublizitaet § 325 HGB > 12 Monate ueberfaellig** — Ordnungsgeldverfahren BfJ laeuft oder droht (§ 335 HGB: bis 25.000 EUR je Verstoß); sofort Jahresabschluss erstellen und einreichen.
- **Gesellschafterliste § 40 GmbHG nach Abtretung > 3 Wochen nicht eingereicht** — gutglaeuber Erwerb durch Dritte moeglich (§ 16 Abs. 3 GmbHG); Notar sofort beauftragen.
- **Transparenzregister-Eintrag nach Beteiligungsaenderung > 2 Wochen nicht aktualisiert** — Bußgeld bis 1.000.000 EUR (§ 56 Abs. 1 GwG).
- **Groessenklassenwechsel zur grossen Kapitalgesellschaft nicht erkannt** — Prüfungspflicht § 316 HGB gilt ab zweitem Jahr in Folge (§ 267 Abs. 4 HGB); Prüfungsauftrag erteilen.

## Anschluss-Skills

- `gesellschaftsrecht:gesellschaftsrecht-mandat-arbeitsbereich` — Mandatsworkspace für die betroffene Gesellschaft
- `gesellschaftsrecht:vollzugs-checkliste` — Gesellschafterliste und Transparenzregister als Vollzugspflicht bei M&A
- `gesellschaftsrecht:aufsichtsrat-protokoll` — Jahresabschluss-Billigung nach § 172 AktG protokollieren
- `gesellschaftsrecht:tabellenpruefung` — Compliance-Tabelle aus Jahresabschlussdaten prüfen

## Quellen und Zitierweise

- § 325 HGB (Bilanzpublizität / Offenlegungspflicht)
- § 335 HGB (Ordnungsgeldverfahren Bundesamt für Justiz)
- § 40 GmbHG (Gesellschafterliste)
- §§ 18 ff., 20 GwG (Transparenzregister)
- § 267 HGB (Größenklassen)
- § 316 HGB (Prüfungspflicht)
- § 16 Abs. 3 GmbHG (Gutgläubiger Erwerb)
- § 290 HGB (Konzernabschlusspflicht)
- § 264 Abs. 1 HGB (Aufstellungsfrist)

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Scholz, GmbHG, 12. Aufl. 2018, § 40 Rn. 3 ff. (Gesellschafterliste).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Was dieser Skill nicht tut

- Er reicht keine Dokumente ein. Ausgabe ist Tracker und Aufgabenliste; Einreichung erfolgt durch Anwalt/Steuerberater.
- Er ruft keine Registerauszüge ab; er verfolgt, wann sie zuletzt bestätigt wurden.
- Er bestimmt nicht, ob eine Konzernabschluss-Pflicht besteht — das erfordert eine Analyse der tatsächlichen Konzernverhältnisse.
- Er ersetzt keine Steuerberatung (§ 316 HGB-Prüfung = Steuerberater/Wirtschaftsprüfer).

## 5. `gesellschaftsrecht-anpassen`

**Fokus:** Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A / Governance / Kapitalmarkt / Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Beschlussformat oder Mandatsworkspace-Pfade anpassen. Lädt, wenn der Nutzer "Profil ändern", "Konfiguration aktualisieren", "Einstellung anpassen" oder vergleichbare Formulierungen verwendet.

# Praxisprofil anpassen

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Praxisprofil anpassen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Praxisprofil anpassen
- **Spezialgegenstand:** Praxisprofil anpassen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor der Profilanpassung klaeren:

1. **Profil vorhanden?** Existiert eine CLAUDE.md mit abgeschlossenem Kaltstart-Interview? Falls nicht: `gesellschaftsrecht-kaltstart-interview` zuerst ausfuehren.
2. **Was soll geaendert werden?** Ein Abschnitt (Wesentlichkeitsschwelle, Modul, Risikoprofil, Person) oder mehrere Abschnitte? — Pro Durchlauf nur eine Aenderung.
3. **Modul-Aktivierung?** Wird ein bisher inaktives Modul aktiviert (z.B. Kapitalmarkt)? Dann sind Folge-Einrichtungsfragen zu stellen.
4. **Rechtsrelevante Aenderung?** Betrifft die Aenderung Normschwellen (z.B. Wesentlichkeitsschwelle M&A) oder Verfahrensregeln (z.B. Beschlussformat)? Dann rechtliche Downstream-Konsequenz erklaeren.
5. **Downstream-Wirkung?** Welche anderen Skills werden von der Aenderung beeinflusst? (Tabelle der konfigurierbaren Bereiche zeigen)

## Zweck

Der Nutzer möchte eine einzelne Einstellung im Praxisprofil ändern — ein Risikoprofil, einen Eskalationskontakt, einen Modulschalter, ein Ausgabeformat — ohne das vollständige Ersteinrichtungs-Interview zu wiederholen und ohne YAML manuell zu bearbeiten.

## Eingaben

- Aktuelle CLAUDE.md (Praxisebene) und ggf. Unternehmensprofil
- Beschreibung der gewünschten Änderung (Freitext oder Abschnittsbenennung)
- Bei modulspezifischen Änderungen: ggf. neue Seed-Dokumente

## Rechtlicher Rahmen

Das Praxisprofil bildet den rechtlichen Rahmen der vom Nutzer betreuten Mandate ab. Änderungen an Wesentlichkeitsschwellen, Modulen oder Eskalationslogiken haben unmittelbare Auswirkungen auf sämtliche Skill-Ausgaben.

Relevante Vorschriften je Bereich (Referenz für Konsistenzprüfung):
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mitbestimmung: MitbestG, DrittelbG — eine Moduländerung, die ein mitbestimmungspflichtiges Unternehmen betrifft, ist zu flaggen
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Ablauf

### Schritt 1: Praxisprofil lesen

CLAUDE.md und Unternehmensprofil lesen. Falls das Plugin-Profil nicht existiert oder noch `[PLATZHALTER]`-Werte enthält:

> Sie haben die Ersteinrichtung noch nicht abgeschlossen. Führen Sie zunächst `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview` aus — die Anpassungsfunktion setzt ein bestehendes Praxisprofil voraus.

### Schritt 2: Anpassungsübersicht zeigen

Liste der konfigurierbaren Bereiche mit aktuellen Werten:

- **Unternehmen / Wer Sie sind** — Name, Branche, Rechtsform, Sitz, Tätigkeitssetting *(gemeinsam genutzt über alle Plugins — Änderungen wirken in `unternehmens-profil.md`)*
- **Aktive Module** — welche von M&A, Governance/Beschlussfassung, Kapitalmarkt, Gesellschaftsverwaltung aktiv sind. Ein- und Ausschalten ändert, welche Skills Setup-Hinweise einblenden.
- **Risikoprofil** — konservativ / ausgewogen / progressiv; Bedeutung für Due-Diligence-Wesentlichkeit und Offenlegungsumfang
- **Personen** — Transaktionsteam, verantwortlicher Geschäftsführer/Vorstand, Gesellschaftsverwaltungsverantwortlicher, Eskalationskette
- **M&A-Modul** — Wesentlichkeitsschwellen (Vertragswert, Mitarbeiteranzahl, Umsatz), zugelassene VDR-Plattformen, KI-Massenreview-Vertrauensstufe, Briefing-Turnus des Transaktionsteams
- **Governance-Modul** — Hausbeschlussformat, bevorzugte Unterzeichner, Ausschussstruktur, Notaranforderungen
- **Kapitalmarkt-Modul** — Berichterstattungskalender, BaFin-Meldepflichten, Hauptversammlungs-Turnus
- **Gesellschaftsverwaltungs-Modul** — Gesellschaftstabelle, Registerführung, Jahresabschluss-Pflichten
- **Ablauf** — Mandatsworkspaces, Schließungscheckliste, VDR-Pfad
- **Integrationen** — Box / Intralinks / Datasite / Handelsregister / Datenraum-Status und Fallbacks

### Schritt 3: Änderungswunsch erfragen

> Was möchten Sie anpassen? Wählen Sie einen Abschnitt, oder beschreiben Sie die Änderung in eigenen Worten.

### Schritt 4: Änderung durchführen

Aktuellen Wert zeigen, neuen Wert abfragen, Downstream-Auswirkungen erläutern, bestätigen, in die Konfiguration schreiben.

Beispiele:
- *Wesentlichkeitsschwelle 250.000 EUR → 500.000 EUR:* "`/Due-Diligence-Extraktion` und `/Material-Vertragsverzeichnis` verwenden künftig 500.000 EUR als Grenzwert. Bestehende Findings bleiben unverändert; bei rückwirkender Anwendung bitte neu ausführen."
- *Kapitalmarkt-Modul aktivieren:* "Beim nächsten Aufruf eines kapitalmarktrechtlichen Skills werden Sie nach Berichterstattungskalender und BaFin-Pflichten gefragt."
- *KI-Massenreview-Vertrauen "jede Zeile prüfen" → "10 % Stichprobe":* "`/KI-Tool-Übergabe` prüft künftig eine 10 %-Stichprobe statt jeder Extraktion."

### Schritt 5: Änderungen an Unternehmensprofil

Bei Änderungen an Unternehmensname, Branche, Sitz, Tätigkeitssetting, Rechtsform: in `unternehmens-profil.md` schreiben und hinweisen:

> Diese Änderung betrifft alle Plugins — jedes Plugin, das Ihren Jurisdiktionsbereich liest, sieht ab sofort [neuer Wert].

### Schritt 6: Abschluss

> Fertig. Ihre nächste Ausgabe spiegelt die Änderung wider. Weitere Anpassungen? Sie können `/gesellschaftsrecht:gesellschaftsrecht-anpassen` jederzeit erneut aufrufen.

## Ausgabeformat

- Bestaetigung der Aenderung mit Vorher-/Nachher-Wert
- Hinweis auf betroffene Skills
- Ggf. Inkonsistenzwarnung (s. u.)

## Output-Template

**Adressat:** Praxis-Nutzer / Kanzlei-intern — Tonfall: sachlich-bestaedigend, handlungsanleitend

```
PROFILANPASSUNG GESELLSCHAFTSRECHT
Datum: [TT.MM.JJJJ]
Geaenderter Abschnitt: [ABSCHNITTSNAME]

--- AENDERUNG ---
VORHER: [ALTER WERT]
NACHHER: [NEUER WERT]

--- BETROFFENE SKILLS ---
Diese Aenderung wirkt auf folgende Skills:
- [SKILL 1]: [BESCHREIBUNG DER AUSWIRKUNG]
- [SKILL 2]: [BESCHREIBUNG DER AUSWIRKUNG]
Rueckwirkende Anwendung auf bestehende Daten: [NEIN / NUR AUF ANFRAGE]

--- INKONSISTENZ-PRUEFUNG ---
[KEIN KONFLIKT ERKANNT]
oder:
Konflikt erkannt: [BESCHREIBUNG] — Empfehlung: [HANDLUNGSHINWEIS]

--- BESTAEIGUNG ---
Praxisprofil gespeichert. Naechste Ausgabe verwendet den neuen Wert.
Weitere Anpassungen: `/gesellschaftsrecht:gesellschaftsrecht-anpassen` erneut aufrufen.
```

## Rote Schwellen

- **Wesentlichkeitsschwelle M&A auf null oder sehr niedrig gesetzt** — alle Vertraege werden als wesentlich geflaggt; DD-Tools werden unbrauchbar; Wert ueberdenken.
- **Modul deaktiviert, obwohl aktive Mandate dieses Modul nutzen** — laufende Mandate koennen Skills nicht mehr laden; erst nach Abschluss aller Mandate in diesem Bereich deaktivieren.
- **Schutzfunktionen (\"pruefen\"-Flags, Quellenhinweise) entfernt** — haftungsrechtliches Risiko; vor Entfernung Trade-off ausfuehrlich erklaeren.
- **Mehrere Abschnitte in einem Durchlauf geaendert** — Downstream-Konflikte schwer nachverfolgbar; eine Aenderung pro Durchlauf.

## Beispiel

**Szenario:** Wesentlichkeitsschwelle für Vertragsreview von 100.000 EUR auf 250.000 EUR erhöhen.

Ausgabe: "Wesentlichkeitsschwelle geändert: 100.000 EUR → 250.000 EUR. `/Due-Diligence-Extraktion` und `/Material-Vertragsverzeichnis` wenden den neuen Wert an. Bestehende Findings bleiben unverändert."

## Risiken und typische Fehler

- **Abschnitte löschen.** Wenn der Nutzer etwas "entfernen" möchte, Wert auf `[Nicht konfiguriert]` setzen und Auswirkung erläutern.
- **Interne Inkonsistenz ignorieren.** Wenn die Änderung das Profil inkonsistent macht (z.B. Kapitalmarkt-Modul deaktiviert + "BaFin-Kontakt" in Eskalationsmatrix; oder konservatives Risikoprofil + sehr hohe Schwellenwerte), Spannung flaggen.
- **Schutzfunktionen degradieren.** Das `[überprüfen]`-Flag, Quellenangaben auf abgerufenen Dokumenten und `[verifizieren]`-Tags auf zitierten Entscheidungen sind inhaltlich tragende Elemente — Trade-off vor Entfernung erläutern.
- **Mehrere Änderungen gleichzeitig.** Eine Änderung pro Durchlauf, kein Re-Interview.

## Quellenpflicht

Bei Änderungen, die rechtliche Schwellenwerte oder Verfahrensregeln betreffen:
- Einschlägige Norm zitieren: `§ 48 Abs. 2 GmbHG`, `Art. 17 Abs. 1 MAR`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
