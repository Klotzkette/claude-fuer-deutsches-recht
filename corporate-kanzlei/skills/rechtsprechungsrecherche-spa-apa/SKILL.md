---
name: rechtsprechungsrecherche-spa-apa
description: "Rechtsprechungsrecherche SPA APA: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsprechungsrecherche SPA APA

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Rechtsprechungsrecherche SPA APA** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-rechtsprechungsrecherche` | Corporate-Rechtsprechungsrecherche: Sucht und bewertet Urteile für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. Liefert Fundstellenliste mit Aktenzeichen, Datum, Leitsatz-Paraphrase und Verwertungsnotiz für Vertrag, Memo oder Board Paper. |
| `corporate-kanzlei-spa-apa-entwurf` | SPA (Share Purchase Agreement) oder APA (Asset Purchase Agreement) entwerfen und strukturieren aus Term Sheet und DD-Findings. Normen: §§ 433 ff. BGB (Kaufrecht), § 444 BGB (Gewaehrleistung), §§ 311 Abs. 2 und 280 BGB. Prüfraster: Kaufpreismechanik (Locked Box vs. Closing Accounts), MAC-Klausel, Representations & Warranties, Indemnification, Earn-Out, W&I-Insurance-Schnittstelle, Signaturformalien. Output SPA/APA-Ersterstellung oder Markup mit Key Issues. Abgrenzung: SPA-Markup siehe vertragsmarkup-key-issues; Disclosure Schedules siehe disclosure-schedules. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Rechtsprechungsrecherche SPA APA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-rechtsprechungsrecherche`

**Fokus:** Corporate-Rechtsprechungsrecherche: Sucht und bewertet Urteile für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. Liefert Fundstellenliste mit Aktenzeichen, Datum, Leitsatz-Paraphrase und Verwertungsnotiz für Vertrag, Memo oder Board Paper.

# Corporate-Rechtsprechungsrecherche

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Corporate-Rechtsprechungsrecherche` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Recherche

1. Welches Rechtsgebiet / Thema — BJR/Organhaftung, M&A-Gewährleistung, Fusionskontrolle, Umwandlungsrecht, Insolvenz/StaRUG, Kapitalmarkt (MAR/WpHG), Gesellschaftsrecht (GmbH/AG/KG)?
2. Welcher Verwendungszweck — Vertrag (Klausel belegen), Board Paper (Legalitätspflicht), DD-Report (Risikohinweis), Schriftsatz (Klagegrundlage), interner Vermerk (Rechtslageübersicht)?
3. Welcher Zeitraum — nur aktuelle Entscheidungen (ab 2020), oder auch ältere Grundsatzentscheidungen?
4. Welche Gerichte — BGH, BVerfG, BAG, BFH, OLG, EuGH, oder auch Instanzgerichte?
5. Sind bereits Aktenzeichen oder Fundstellen bekannt, die verifiziert werden sollen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Recherchequellen

| Quelle | Inhalt | Qualität | Nutzung |
|---|---|---|---|
| bundesgerichtshof.de | BGH-Entscheidungen (Volltext) | Amtlich | Primärquelle; immer bevorzugen |
| bundesverfassungsgericht.de | BVerfG-Entscheidungen | Amtlich | Primärquelle |
| bundesarbeitsgericht.de | BAG-Entscheidungen | Amtlich | Primärquelle Arbeitsrecht |
| bundesfinanzhof.de | BFH-Entscheidungen | Amtlich | Primärquelle Steuerrecht |
| dejure.org / openjur.de | Instanzgerichte, OLG, LG | Halbamtlich | Ergänzend; Fundstelle immer verifizieren |
| beck-online.de / juris.de | Volltext + Kommentar | Kommerziell | Preferred für Fundstellenverifizierung |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |

## Rechtsprechungs-Kanon Corporate/M&A

### Organpflichten / Business Judgment Rule
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Insolvenzantragspflicht / § 15a InsO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### StaRUG / Insolvenzplan
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### M&A-Gewährleistung / SPA
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Fusionskontrolle / FDI
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kapitalmarkt / MAR
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Thema und Verwendungszweck klären** — Triage-Fragen oben beantworten.
2. **Kanonische Entscheidungen prüfen** — zunächst in Rechtsprechungs-Kanon oben nachsehen.
3. **Primärquelle aufrufen** — Entscheidung auf amtlicher Website des Gerichts oder in Zeitschrift verifizieren.
4. **Fundstelle erfassen** — Aktenzeichen, Datum, Gericht, Zeitschrift, Jahrgang, Seite/Randnummer.
5. **Leitsatz paraphrasieren** — eigene Paraphrase in 1-2 Sätzen; NICHT wörtlich kopieren (Urheberrecht).
6. **Verwertungsnotiz schreiben** — wie passt Entscheidung auf konkreten Sachverhalt?
7. **Nicht-verifizierbare Fundstellen markieren** — als unverified kennzeichnen; nicht in Board Paper oder Schriftsatz verwenden.
8. **Ergebnisliste übergeben** — im Output-Template unten; an Ziel-Skill routen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Rechtsprechung zu Corporate/M&A-Frage recherchieren | Recherche-und Ausgabeliste nach Template unten |
| Variante A — Fragestellung sehr spezifisch und aktuell | Direkt in beck-online / juris suchen; Template als Ausgabeformat |
| Variante B — Grundsatzfrage mit langer Rechtsprechungslinie | Kanoentabelle aufbauen; historische Entwicklung darstellen |
| Variante C — auslaendisches oder EU-Recht relevant | Parallele Recherche EU-Ebene; EuGH-Urteile gesondert auflisten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Rechtsprechungsliste

**Adressat:** Deal-Team intern / Schriftsatzentwurf — Tonfall sachlich-juristisch
```
RECHTSPRECHUNGSRECHERCHE
Thema: [Rechtsgebiet / spezifische Frage]
Verwendungszweck: [Vertrag / Board Paper / DD-Report / Schriftsatz / Vermerk]
Erstellt: [Datum]
Ersteller: [Name, Funktion]

RECHERCHEERGEBNISSE

Nr. | Gericht | Aktenzeichen | Datum | Fundstelle | Leitsatz (Paraphrase) | Verwertungsnotiz | Status
----|--------|-------------|-------|-----------|----------------------|-----------------|-------
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2 | Rechtsprechung live pruefen | Gericht, Datum und Aktenzeichen erst nach freier/amtlicher Quelle eintragen | [Paraphrase] | [Relevanz] | verifiziert
3 | [Gericht] | [Az.] | [Datum] | [Fundstelle] | [Paraphrase] | [Relevanz] | UNVERIFIED — bitte prüfen

NICHT GEFUNDEN / LÜCKEN
- [Rechtsgebiet X]: Keine aktuelle BGH-Entscheidung ab 2020; ältester Bezug: [Az.]
- [Rechtsgebiet Y]: Nur Instanzgericht-Entscheidung verfügbar; OLG [Ort] [Az.]

OFFENE RECHERCHEFRAGEN (TODO)
| Nr. | Frage | Owner | Frist | Eskalation |
|----|-------|-------|-------|------------|
| 1 | [Frage] | [Name] | [Datum] | [Stufe] |

ROUTING
Ergebnisse verwendbar für:
- `corporate-kanzlei-board-paper-business-judgment` — Abschnitt Leitentscheidungen
- `corporate-kanzlei-spa-apa-entwurf` — Gewährleistungsklauseln
- [weiterer Ziel-Skill]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Rote Schwellen

- Nicht verifizierte Fundstelle → als UNVERIFIED markieren; nicht in Schriftsatz oder Board Paper verwenden.
- Aktenzeichen ohne auffindbare Primärquelle → Vorsicht; konservative Alternative aus bekannten Klassikern wählen.
- Paraphrase weicht von tatsächlichem Leitsatz ab → erneut prüfen; Original-Randnummer angeben.
- Entscheidung aus Instanzgericht bei verfügbarer BGH-Entscheidung → BGH bevorzugen.
- Zu altes Urteil (vor 2000) ohne Überprüfung ob überholt → Folgerechtsprechung prüfen.

## Übergabe an andere Skills

- `corporate-kanzlei-board-paper-business-judgment` — Leitentscheidungen für Vorstandsdokumentation
- `corporate-kanzlei-spa-apa-entwurf` — Rechtsprechung zu Gewährleistung und Haftung
- `corporate-kanzlei-restructuring-starug-insolvenzplan` — StaRUG/InsO-Rechtsprechung
- `corporate-kanzlei-public-ma-kapitalmarkt-mar` — Kapitalmarktrechtsprechung
- `corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle` — Verifizierungspflicht für Fundstellen

## Quellen und Vertiefung

- bundesgerichtshof.de (amtliche BGH-Datenbank)
- bundesverfassungsgericht.de (amtliche BVerfG-Datenbank)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `corporate-kanzlei-spa-apa-entwurf`

**Fokus:** SPA (Share Purchase Agreement) oder APA (Asset Purchase Agreement) entwerfen und strukturieren aus Term Sheet und DD-Findings. Normen: §§ 433 ff. BGB (Kaufrecht), § 444 BGB (Gewaehrleistung), §§ 311 Abs. 2 und 280 BGB. Prüfraster: Kaufpreismechanik (Locked Box vs. Closing Accounts), MAC-Klausel, Representations & Warranties, Indemnification, Earn-Out, W&I-Insurance-Schnittstelle, Signaturformalien. Output SPA/APA-Ersterstellung oder Markup mit Key Issues. Abgrenzung: SPA-Markup siehe vertragsmarkup-key-issues; Disclosure Schedules siehe disclosure-schedules.

# SPA/APA-Entwurf

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `SPA/APA-Entwurf` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — klaere vor Entwurfsbeginn

1. Share Deal oder Asset Deal? (Steuerfolgen, Haftungsuebergang, Vertragsuebergang)
2. Kaufpreismechanik: Locked Box oder Closing Accounts? (Stichtag, Leakage-Definition)
3. Gibt es DD-Findings, die spezifische Garantieeinschraenkungen erfordern?
4. W&I-Versicherung geplant? (Beeinflusst Garantiemechanik, De-Minimis, Cap)
5. Earn-Out-Komponente? (Zahlungsstruktur, Milestones, Anti-Sandbagging)
6. Jurisdiktion und anwendbares Recht — deutsches Recht, englisches Recht, hybrid?
7. Verkauf von/an Private Equity oder strategischen Kaeufer?
8. Notar erforderlich? (§ 15 GmbHG bei GmbH-Anteilen immer; AktG bei AG Depot/Legitimationsabtretung)

## Zentrale Anspruchsgrundlagen & Normen

- **§ 433 ff. BGB** — Kaufvertrag; Mietvertrag-, Aufhebungs-, Abtretungsregeln
- **§ 453 BGB** — Rechtskauf, Anteilskauf
- **§ 444 BGB** — Arglistiges Verschweigen; keine vertragliche Haftungsfreizeichnung moeglich
- **§ 15 GmbHG** — Abtretung von GmbH-Anteilen; Notarpflicht
- **§ 929 ff. BGB** — Eigentumsuebergang Asset Deal
- **§ 613a BGB** — Betriebsuebergang; Arbeitnehmeruebergang Asset Deal
- **§§ 306 ff. BGB** — AGB-Kontrolle bei standardisierten Vertragsklauseln
- **§§ 241 II, 311 II BGB** — Culpa in contrahendo; Informationspflichten pre-Signing
- **§ 123 BGB** — Anfechtung wegen arglistiger Taeuschung
- **§ 439 ff. BGB** — Nacherfuellung; Ruecktritt; Schadensersatz (wenn keine individuelle Regelung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Praxiswissen: Kaufpreismechanik

### Locked Box
- Stichtag: Bilanzdatum (meist letzter Jahresabschluss)
- Leakage-Definition: Dividenden, Management Fees, unerlaubte Vermoegensverlagerungen
- Permitted Leakage: normal course payments, Geschaeftsfuehrergehalt
- Vorteile: Preissicherheit, kein Closing Accounts-Streit
- Risiko: Seller traegt kein Upside; Kaeufer muss Leakage-Periode ueberwachen

### Closing Accounts
- Bilanzstichtag: Closing-Datum; Erstellung innerhalb 60-90 Tage
- Adjust-Mechanismus: Net Debt, Working Capital, Cash
- Streitpotenzial: Accounting-Wahlrechte, Bewertungsunterschiede
- Schiedsverfahren (Wirtschaftspruefer als Expert) als Eskalation

## Reps & Warranties — Standardkatalog

| Kategorie | Kerngarantien | Typische Einschraenkung |
|---|---|---|
| Corporate | Gruendung, Anteilsstruktur, Satzung, Vollmachten | Disclosure Letter |
| Financial | Jahresabschluss ordnungsgemaess, kein Material Adverse Change | Wesentlichkeitsschwelle |
| Business | Vertraege, IP, Kunden, Lizenzen, Behoerdenerlaubnisse | Knowledge qualifier |
| Employment | Arbeitsvertraege, BR, Pensionen, Change-of-Control | Kollektivarbeitsrecht |
| Tax | Steuern vollstaendig bezahlt, keine offenen Betriebspruefungen | Tax Disclosure |
| Legal | Keine wesentlichen Rechtsstreitigkeiten | Pending/Threatened |
| Compliance | AML/GwG, Sanktionen, Kartellrecht, ESG-Kriterien | Best Knowledge |

## Indemnification vs. Warranty-Breach

- **Indemnity (Freistellung):** Dollar-for-dollar, unabhaengig von Kausalitaet; fuer bekannte Risiken (steuerliche Nachzahlungen, Altlasten, Prozessrisiken)
- **Warranty Breach:** Schadensersatz nach § 311 I BGB oder vertragl. Schadensliquidation; Kaeufer muss Schaden an Unternehmenswert nachweisen
- **Anti-Sandbagging:** Seller haftet auch bei Kaeufer-Kenntnis, wenn vertraglich so vereinbart; ohne Klausel ggf. § 442 BGB

## Schritt-fuer-Schritt-Workflow

1. **Term Sheet analysieren** — Kaufpreis, Struktur, Closing Conditions, Exklusivitaet
2. **DD-Findings mapping** — jedes Material Finding einem Vertragsmechanismus zuordnen (Garantie, Indemnity, Kosten-Anpassung, Deal-Breaker)
3. **Strukturentscheidung** — Share Deal/Asset Deal; Locked Box/Closing Accounts; W&I ja/nein
4. **Vertragsgeruest aufbauen** — Definitionen, Kaufpreis, Closing Conditions, Representations, Warranties, Covenants, Indemnities, Haftungslimite, Governing Law, Dispute Resolution
5. **Key Issues Memo** — offene Business- und Rechtsentscheidungen mit Optionen und Empfehlung
6. **Verhandlungsrunden** — Markup-Schleife; Leadsatz beachten; Disclosure Schedule parallel fuellen
7. **Signing-Vorbereitung** — Execution Version, Anlagen, Disclosure Letter, W&I-Deckungsbestaetigung
8. **Closing Mechanics** — Conditions Precedent-Checkliste, CP-Satisfaction-Protokoll, Kaufpreiszahlung, Anteilsuebertragung (Notar)

## Entscheidungsbaum: Notar erforderlich?

```
Gegenstand: GmbH-Anteile?
 → Ja: Notarielle Beurkundung zwingend (§ 15 III GmbHG)
 → Vorkaufsrecht der Mitgesellschafter? → ja: Angebotsverfahren beachten
 → Nein: AG-Aktien?
 → vinkulierte Namensaktien: Zustimmungsvorbehalt pruefen (§ 68 II AktG)
 → Inhaberaktien: kein Notar noetig; Depot-Uebertragung
 → Asset Deal: kein Notar fuer Vertragstext, aber Grundstuecke -> notarielle Auflassung (§ 925 BGB)
```

## Output-Template Key Issues Memo

**Adressat:** Mandant / Deal-Team — Tonfall sachlich-juristisch, entscheidungsorientiert

```
KEY ISSUES MEMO
Transaktion: [DEAL-NAME]
Stand: [DATUM]
Version: [Nr.]
Erstellt von: [NAME, FUNKTION]

1. OFFENE BUSINESS-ENTSCHEIDUNGEN
 | Nr. | Thema | Option A | Option B | Empfehlung |
 |----|-------|----------|----------|-----------|
 | 1 | Kaufpreismechanik | Locked Box | Closing Accounts | [Empfehlung] |
 | 2 | W&I-Versicherung | Ja (Kaeufer-Policy) | Nein | [Empfehlung] |

2. DD-FINDING-MATRIX
 | Finding | Vertragsmechanismus | Owner | Status |
 |---------|---------------------|-------|--------|
 | [Finding 1] | Spezifische Indemnity | [Partei] | Offen/Geschlossen |

3. HAFTUNGSREGIME
 - De-Minimis: [Betrag EUR]
 - Basket (Tipping/Deductible): [Betrag EUR]
 - Cap: [% des Kaufpreises]
 - Verjährung: [allg. 18-24 Monate; Tax 5-7 Jahre; Titel unbegrenzt]

4. CLOSING CONDITIONS
 - Kartellrecht: [Anmeldung bei / Freigabe bis]
 - Aussenhandel/FDI: [AWG/ATSG/SektSchV-Pruefung]
 - Dritte Zustimmungen: [Change-of-Control-Klauseln]

5. NAECHSTE SCHRITTE
 | Schritt | Owner | Frist |
 |---------|-------|-------|
 | [Massnahme 1] | [Name] | [Datum] |
```

## Output-Template SPA-Struktur (Outline)

```
SHARE PURCHASE AGREEMENT — INHALTSVERZEICHNIS
Parteien: [VERKAEUFER], [KAEUFER], [ZIELGESELLSCHAFT]
Datum: [DATUM]

1. Definitionen und Auslegung
2. Kauf und Verkauf der Anteile
 2.1 Kaufgegenstand
 2.2 Kaufpreis und Kaufpreismechanik (Locked Box / Closing Accounts)
 2.3 Kaufpreisanpassung
3. Vollzugsbedingungen (Closing Conditions / Conditions Precedent)
 3.1 Kartellfreigabe [§§ 35 ff. GWB / EU-Fusionskontrolle]
 3.2 [Weitere CPs]
4. Vollzug (Closing)
 4.1 Closing-Datum
 4.2 Vollzugshandlungen (Deliverables)
5. Representations and Warranties des Verkaefers
 5.1 Corporate/Title
 5.2 Financial Statements
 5.3 [...]
6. Representations and Warranties des Kaeufers
7. Covenants pre-Closing (Interim Operating Covenants)
8. Covenants post-Closing
9. Haftung und Rechtsfolgen von Warranty-Verletzungen
 9.1 Haftungslimite (De-Minimis, Basket, Cap)
 9.2 Verjährung
 9.3 Anti-Sandbagging
10. Specific Indemnities (Freistellungen)
11. MAC-Klausel / Material Adverse Change
12. Ruecktrittsrechte
13. Vertraulichkeit / Oeffentlichkeitsarbeit
14. Geheimhaltung / NDA-Integration
15. Sonstiges (Kosten, Notifikationen, Schiedsklausel)
16. Anwendbares Recht / Gerichtsstand
Anlagen: Disclosure Letter, Locked-Box-Bilanz, CP-Liste, W&I-Term Sheet
```

## Rote Schwellen

- Kaufpreismechanik nicht abgestimmt → Streit ueber Earn-Out oder Working Capital obligatorisch
- DD-Finding ohne vertragliche Reaktion → Indemnity-Luecke; kein Seller-Schutz und kein Kaeufer-Schutz
- MAC-Klausel fehlt → keine Ruecktrittsoption bei wesentlicher Verschlechterung vor Closing
- Notarpflicht (§ 15 GmbHG) uebersehen → formnichtige Anteilsuebertragung
- W&I-Policy-Bedingungen nicht mit Vertragsklauseln abgestimmt → Deckungsluecken

## Vertiefung

### MAC-Klausel — Abgrenzung Material/Nicht-Material

Die MAC-Klausel ist das wichtigste Ruecktrittsvehikel. Kernanforderung: Die Verschlechterung muss (a) wesentlich, (b) dauerhaft und (c) auf die Zielgesellschaft bezogen sein. Allgemeine Markt- oder Branchenrisiken (Systemkrise, Pandemie als solche) sind typischerweise ausgegrenzt — ausser der Zielgesellschaft trifft es ueberproportional.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Earn-Out — Praxisrisiken

Earn-Out-Klauseln sind streitanfaellig. Kaeufer-Risiken: Manipulation durch Accounting-Wahlrechte, Senkung des EBITDA durch konzerninterne Umlagen. Verkaeufer-Risiken: Kaeufer aendert Geschaeftsstrategie, was Milestones unmoeglich macht.

Best Practice: (a) Accounting-Methodology einfrieren; (b) Nicht-Beeintrachtigungs-Covenant ("Non-Frustration"); (c) klare Earn-Out-Statementerstellung mit Schiedsklausel; (d) OLG Frankfurt-Rspr. beachten: Kaeufer hat aktive Foerderpflicht.

## Quellen

- § 433 BGB: https://www.gesetze-im-internet.de/bgb/__433.html
- § 453 BGB (Rechtskauf/Anteilskauf): https://www.gesetze-im-internet.de/bgb/__453.html
- § 444 BGB (Arglist): https://www.gesetze-im-internet.de/bgb/__444.html
- § 613a BGB (Betriebsuebergang Asset Deal): https://www.gesetze-im-internet.de/bgb/__613a.html
- § 15 GmbHG (Abtretung GmbH-Anteile, Notarpflicht): https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 68 AktG (Vinkulierung Namensaktien): https://www.gesetze-im-internet.de/aktg/__68.html
- §§ 35 ff. GWB (Fusionskontrolle Bundeskartellamt): https://www.gesetze-im-internet.de/gwb/__35.html
- FKVO (VO (EG) Nr. 139/2004 EU-Fusionskontrolle): https://eur-lex.europa.eu/eli/reg/2004/139
- AWG §§ 4-6, AWV §§ 55 ff. (Investitionspruefung): https://www.gesetze-im-internet.de/awv_2013/
- EU FSR (VO 2022/2560; M&A-Notifizierungspflicht ab 12.10.2023): https://eur-lex.europa.eu/eli/reg/2022/2560
- MoPeG (in Kraft 01.01.2024) — Asset/Share Deal bei Personengesellschaften, neue eGbR-Eintragung: https://www.gesetze-im-internet.de/bgb/__705.html
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
