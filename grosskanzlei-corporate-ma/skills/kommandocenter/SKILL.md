---
name: kommandocenter
description: "Deal-Kommandocenter Corporate/M&A: Schnellstart und Fallrouting für alle Transaktionsphasen. Anwendungsfall Anwalt gibt Kuerzel, Dokument oder Sachverhaltssatz ein und wird in richtigen Deal-Skill geleitet. SPA Share Purchase Agreement, Due Diligence Datenraum, Signing Closing. Prüfraster Deal-Ph..."
---

# Deal-Kommandocenter

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Deal-Kommandocenter
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Kommandocenter und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll, MAR-Insiderliste falls Public-M&A-Bezug.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

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

## Prüfraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB Paragraf 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG Paragraf 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB Paragraf 35 ff. und Paragraf 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 für Insiderinformationen, Ad-hoc-Prüfung und Insiderlisten.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist Paragraf 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `Paragraf 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `Paragraf 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

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
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-gap-clean-room` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-legal` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-qa-information-requests` - wenn Findings in Information Requests und Seller-Q&A übersetzt werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-reporting` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach Paragraf 43a BRAO und Paragraf 3 BORA, Verschwiegenheit nach Paragraf 43a Abs. 2 BRAO, Vergütungsrahmen nach Paragraf 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Deal-Kommandocenter

## Arbeitsmodus

- Dealtyp und Parteiperspektive erkennen: Buy-side, Sell-side, Management, W&I-Versicherer, Public M&A oder Restrukturierung.
- Maximal drei Rückfragen stellen, danach mit vorsichtigen Annahmen weiterarbeiten und offene Punkte ausdrücklich markieren.
- Deal-Phase bestimmen: Origination, Vorbereitung, Datenraum, Due Diligence, Vertrag, Signing/Closing, Integration oder Streit/Restrukturierung.
- Den passenden internen Fachmodul routen und rote Schwellen sichtbar machen.
- Anfängerfreundlich bleiben: fehlende Begriffe erklären, aber den Arbeitsfluss nicht aufhalten.

## Interne Routing-Karte

| Signal | Interner Skill |
| --- | --- |
| Neue Anfrage, Aktenzeichen, Datenraum-Einladung | `grosskanzlei-ma-aktenanlage` |
| Datenraumliste, CSV, Excel, Review Grid | `grosskanzlei-ma-tabellenreview` |
| Cash, OPOS, Bank, Runway, Distressed | `grosskanzlei-ma-liquiditaetsvorschau` |
| Zahlungsunfähigkeit, Überschuldung, StaRUG | `grosskanzlei-ma-insolvenzreife` |
| Signing, Closing, CP, Long Stop Date | `grosskanzlei-ma-fristen-cp-kalender` |
| Rechnung, Narrative, XRechnung, ZUGFeRD | `grosskanzlei-ma-erechnung-gobd` |
| Textentwurf, Report, SPA, Board Paper | `grosskanzlei-ma-schreibcanvas` |
| Register, HRB/HRA, Gesellschafterliste | `grosskanzlei-corporate-ma-handelsregisterabruf` |
| Rechtsprechung und amtliche Quellen | `grosskanzlei-corporate-ma-rechtsprechungsrecherche` |

## Rote Schwellen

- Frist, Signing oder Closing unklar.
- Mandatsgeheimnis, Clean Room oder Insiderinformation betroffen.
- KI-Ergebnis soll ungeprüft als Rechtsrat, DD-Finding oder Board-Grundlage verwendet werden.
- Liquiditätslücke, Insolvenzantragspflicht, Sanktionstreffer oder GwG-Risiko sichtbar.

## Standardausgabe

- Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe.
- Senior-Review-Hinweis bei hohen Risiken.

## Vorlagen

- assets/templates/workflow-deal-kommandocenter.md
- assets/templates/cowork-ma-dashboard.md
- assets/templates/workflow-freigabeampel.md

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- Paragraf 43a BRAO — anwaltliche Sorgfaltspflichten: vollstaendige Mandatsfuehrung; Unterlassen kann Haftung ausloesen
- Paragraf 675, 280 BGB — Beratungsvertrag und Schadensersatz: Anwalt haftet bei Pflichtverletzung; gilt auch für Organisation und Kommunikation
- Paragraf 2 GmbHG; Paragraf 15 GmbHG — gesellschaftsrechtliche Grundlagen GmbH: relevant für alle Corporate-Mandate
- Paragraf 29-33 HGB — Handelsregisterpublizitaet: Wissen über eintragungspflichtige Tatsachen wird konstruktiv zugerechnet

### Leitsaetze aus der Rechtsprechung
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Alle Ergebnisse: Human-in-the-loop bei High-Risk-Findings
- Senior Review vor Weiterleitung an Mandant oder Gegenseite
- Dokumentation: Datum, Bearbeiter, Version, Freigabe
