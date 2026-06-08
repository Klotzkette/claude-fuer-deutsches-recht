---
name: umwandlungssteuerrecht-buchwertantrag
description: "Umwandlungssteuerrecht Buchwertantrag steuerliche Rückwirkung und Verlustuntergang prüfen: Anwendungsfall Corporate-Team und Steuerteam muessen umwandlungssteuerliche Strukturentscheidung abstimmen. §§ 20-24 UmwStG Einbringung, § 8c KStG Verlustuntergang, § 6a GrEStG Grunderwerbsteuer-Ergaenzungstatbestand. Prüfraster Buchwertantrag-Voraussetzungen, steuerliche Rückwirkung Siebenmonatsfrist, § 8c KStG Schaedlichkeitsprüfung, GrESt-Befreiung und Nachbehaltefristen. Output Steuerliche Strukturmatrix mit Buchwertantrag und Risikobewertung. Abgrenzung zu Umwandlungsrecht für gesellschaftsrechtliche Seite und zu Transaktionsstruktur."
---

# Umwandlungssteuerrecht

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Umwandlungssteuerrecht
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Zweck
Dieser Skill führt ein Big-Law Corporate/M&A-Mandat durch den Arbeitsbereich **Distressed M&A, StaRUG/Insolvenz, Liquidität und steuerliche Strukturfolgen**. Er übersetzt die vorhandenen Unterlagen in einen verwertbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und zwingt zu einem senior-review-fähigen nächsten Schritt. Adressaten sind Partner, Counsel, Associates, Legal-Operations-Team und Inhouse-Counsel in großvolumigen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Umwandlungssteuerrecht und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- 13-Wochen-Liquiditätsplanung, Insolvenzreife-Check und Fortbestehensprognose.
- Asset-/Share-Deal-Struktur, Insolvenzverwalter- oder Eigenverwaltungsrolle.
- Anfechtungs-, Haftungs-, Steuer- und Closing-Sicherungsfragen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- InsO §§ 15a, 17, 18, 19, 129 ff., 270 ff. für Insolvenzreife, Antragspflicht und Anfechtung.
- StaRUG §§ 1, 9 ff. und 49 ff. für Früherkennung, Plan und Stabilisierung.
- BGB §§ 134, 138, 280, 311 Abs. 2 und 826 für Haftungs- und Sittenwidrigkeitsfragen.
- UmwStG §§ 20 bis 24 und § 8c KStG nur mit Steuerteam verifizieren.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-distressed-ma` - wenn Krise, Antragspflicht, Anfechtung oder Liquiditätsplanung entscheidend werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan` - wenn Krise, Antragspflicht, Anfechtung oder Liquiditätsplanung entscheidend werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Umwandlungssteuerrecht

## Zweck

Erfasst und bewertet umwandlungssteuerliche Strukturfragen als Arbeitsmatrix für Steuerteam und Corporate-Team. Fokus: Buchwertantrag, steuerliche Rueckwirkung, Verlustuntergang nach § 8c KStG, Grunderwerbsteuer-Ergaenzungstatbestand und Einbringung nach §§ 20-24 UmwStG.

## Triage — klaere mit Steuerteam vor Strukturentscheidung

1. Soll die Umwandlung zu Buchwerten erfolgen — §§ 11, 13 UmwStG (Verschmelzung), §§ 15, 20 UmwStG (Spaltung/Einbringung)? Antrag erforderlich?
2. Ist die steuerliche Rueckwirkungsfrist einzuhalten — § 2 Abs. 1 UmwStG: maximal 12 Monate vor Anmeldung beim HR?
3. Gibt es steuerliche Verlustvortraege — § 8c KStG Verlustuntergang bei mehr als 50 % Anteilserwerb in 5 Jahren; Sanierungsklausel § 8c Abs. 1a KStG anwendbar?
4. Ist der Grunderwerbsteuer-Ergaenzungstatbestand ausgeloct — § 1 Abs. 2a, 2b GrEStG: 90 % Anteilsuebergang an grundbesitzender Gesellschaft = GrESt-Pflicht?
5. Welche Sperrfristen sind zu beachten — § 22 UmwStG: 7 Jahre nach Einbringung kein schaedlicher Anteilsverkauf (sonst rueckwirkende Entstrickung)?
6. Gibt es Organschaft (§§ 14-19 KStG) — koennte Umwandlung Organschaft beenden?

## Zentrale Rechtsgrundlagen

- §§ 11-13 UmwStG — Verschmelzung: Ansatz Buchwert/Zwischenwert/gemeiner Wert; Antrag für Buchwert beim Finanzamt; spaetestens mit Einreichung Steuererklarung
- §§ 15, 16 UmwStG — Spaltung: Teilbetriebsvoraussetzung für Buchwertansatz; Ausschlussfrist
- §§ 20-24 UmwStG — Einbringung: Einzeluebertragung oder Ausgliederung gegen Anteile; Buchwert nur wenn qualifizierter Teilbetrieb; Sperrfrist 7 Jahre
- § 22 UmwStG — Sperrfrist-Verletzung: rueckwirkende Entstrickung; Einbringungsgewinn I/II
- § 8c KStG — Verlustuntergang: mehr als 50 % Anteilsuebergang (schaedlicher Beteiligungserwerb) in 5 Jahren fuehrt zum vollstaendigen Verlustuntergang; Ausnahmen: Konzernklausel, stille-Reserven-Klausel, Sanierungsklausel
- §§ 1 Abs. 2a, 2b GrEStG — Grunderwerbsteuer-Ergaenzungstatbestand: 90 % Anteilsuebergang an grundbesitzender Gesellschaft loest GrESt aus; Steuersatz je nach Bundesland 3,5-6,5 %
- § 3a EStG — steuerfreier Sanierungsertrag bei Forderungsverzicht im Sanierungsplan; Voraussetzungen: Sanierungsabsicht, Sanierungseignung, Sanierungsbeitraege aller Glaeubiger

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Zielstruktur mit Corporate-Team abstimmen:** welche Umwandlungsform (Verschmelzung, Ausgliederung, Formwechsel) ist beabsichtigt?
2. **Verlustvortraege kartieren:** § 8c KStG-Pruefung — bisherige Anteilsuebertragungen der letzten 5 Jahre; Schwellenwerte berechnen; Sanierungsklausel pruefen
3. **Buchwert-Antrag planen:** Antrag beim zuständigen Finanzamt; Frist (§§ 11 Abs. 1, 20 Abs. 2 UmwStG); ohne Antrag: gemeiner Wert = stille Reserven werden aufgedeckt
4. **Rueckwirkungsfristen einhalten:** steuerlicher Abschlussstichtag bestimmen; maximal 12 Monate rueckwirkend (§ 2 Abs. 1 UmwStG); HR-Anmeldung als Fristbeginn
5. **Grunderwerbsteuer pruefen:** grundbesitzende Gesellschaft? § 1 Abs. 2a, 2b GrEStG Schwelle 90 %? Steuersatz; Steuerbefreiung Konzernklausel § 6a GrEStG?
6. **Sperrfrist-Management:** nach Einbringung nach § 20 UmwStG keine schaedliche Veraeusserung für 7 Jahre; § 22 UmwStG Monitoring einrichten
7. **Organschaft-Auswirkungen:** Umwandlung koennte Organschaft beenden; Verlustausgleich und Ergebnisabfuehrungsvertrag pruefen
8. **Steuer-Rueckstellung und Haftungsrisiken im SPA adressieren:** Tax Warranties, Tax Indemnity, Steuer-Freistellungsklausel

## Entscheidungsbaum

- Verlustvortraege vorhanden + mehr als 50 % Anteilserwerb → § 8c KStG → Verlustuntergang → Sanierungsklausel prufen?
- Einbringung ohne Teilbetrieb → § 20 UmwStG Buchwert nicht moeglich → stille Reserven aufzudecken → Steuerbelastung
- GrEStG § 1 Abs. 2a/2b → 90 % Schwelle → GrESt-Pflicht → Konzernklausel § 6a GrEStG greifen?
- Sperrfrist-Verletzung → Einbringungsgewinn I oder II → rueckwirkende Steuer bis zu 7 Jahre

## Output-Template: Steuerliche Strukturmatrix

**Adressat:** Steuerteam und Corporate-Team — Tonfall sachlich-analytisch

```
STEUERLICHE STRUKTURMATRIX
Deal: [DEALNAME] — Datum: [DATUM]

| Aspekt | Analyse | Risiko | Massnahme |
|--------|---------|--------|-----------|
| § 8c KStG Verlustuntergang | [Anteil X % in Y Jahren] | [Hoch/Mittel/Gering] | [Antrag/Gestaltung] |
| Buchwertansatz UmwStG | [Antrag moeglich/nicht moeglich] | [Entstrickung] | [Antragstellung bis DATUM] |
| GrESt-Ergaenzungstatbestand | [90 % Schwelle erreicht/nicht] | [GrESt X EUR] | [Konzernklausel] |
| Sperrfrist § 22 UmwStG | [7-Jahres-Frist bis DATUM] | [Einbringungsgewinn] | [Monitoring] |
| Organschaft | [Besteht/Endet durch Umwandlung] | [EAV-Kündigung] | [...] |

Offene Fragen an Steuerteam: [TODO Owner Datum]
```

## Rote Schwellen

- Steuerliche Annahme ungeprüft: sofortiger Abstimmungsbedarf mit Steuerteam vor Signing
- Buchwertantrag vergessen: stille Reserven werden aufgedeckt; Steuerlast kann Transaktion gefaehrden
- § 8c KStG Verlustuntergang nicht erkannt: erhebliche steuerliche Belastung des Kaeufers
- Sperrfrist-Verletzung: Einbringungsgewinn I/II; rueckwirkende Entstrickungssteuer

## Standardausgabe

- Steuerliche Strukturmatrix mit Risikobewertung
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe
- Belegkette: Normen, BFH-Urteile, Finanzamts-Korrespondenz

## Uebergabe an andere Skills

- Umwandlungsrecht → `grosskanzlei-corporate-ma-umwandlungsrecht`
- Transaktionsstruktur → `grosskanzlei-corporate-ma-transaktionsstruktur`
- Insolvenzreife → `grosskanzlei-ma-insolvenzreife`

## Vorlagen

- assets/templates/steuerliche-strukturmatrix.md
- assets/templates/umwandlungssteuer-checkliste.md

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- §§ 705 ff. BGB (GbR)
- §§ 105 ff. HGB (OHG)
- §§ 161 ff. HGB (KG)
- §§ 13, 15 GmbHG (Anteilsübertragung)
- § 53 GmbHG (Satzungsänderung)
- § 33 GWB, FKVO 139/2004 (Fusionskontrolle)
- § 311 BGB i.V.m. §§ 433, 453 BGB (Unternehmenskauf, share/asset deal)
- §§ 25, 28 HGB (Firmenfortführung, Haftung)
- §§ 2-4 UmwG (Verschmelzung)
- § 1 InvKG, AWG/AWV §§ 55-62 (Investitionsprüfung)

### Leitentscheidungen

- BGH II ZR 17/19 (Earn-Out-Klauseln, Kontrolle)
- BGH II ZR 280/14 (Gewährleistungsausschluss share deal)
- BGH II ZR 109/13 (W&I-Versicherung, Sale and Purchase)
- EuGH C-93/13 P (FKVO-Verfahren)
- BGH II ZR 71/11 (Auskunftsrechte Datenraum)

### Anwendung im Skill

- Share Deal vs. Asset Deal Wahl an Steuer-, Haftungs- und Genehmigungsfolgen, nicht am LMA-Standard ausrichten.
- W&I-Versicherung nach BGH II ZR 109/13 ergaenzt, ersetzt aber keine Garantien.
- Fusionskontrolle § 39 GWB und FKVO 139/2004: Anmeldepflicht vor Closing pruefen, sonst § 41 GWB-Vollzugsverbot.
