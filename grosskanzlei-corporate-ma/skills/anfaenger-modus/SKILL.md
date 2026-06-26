---
name: anfaenger-modus
description: "Anfänger- und First-Year-Associate-Modus für Großkanzlei Corporate/M&A: fragt Erfahrungslevel, Deal-Phase, Aufgabe, Frist, Unterlagen und gewünschte Führung ab; erklärt Begriffe, zerlegt Aufgaben in kleine Schritte, schlägt passende Plugin-Skills vor und baut Review-Gates für Senior Review."
---

# Anfänger-Modus / First-Year-Associate

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Anfänger-Modus / First-Year-Associate
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Anfänger-Modus / First-Year-Associate und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Mandatsanfrage, Konfliktcheck, Rollenmatrix, Budget und Deal-Timeline.
- Kommunikationskanäle, Vertraulichkeitsstufen, Review-Gates und Eskalationspfade.
- Vorlagen für Deal-Karte, Workstream-Plan, Statusbericht und Billing Narrative.

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
- BRAO Paragraf 43a, BORA Paragraf 3 und BRAO Paragraf 49b für Verschwiegenheit, Konflikt und Honorar.
- GwG Paragraf 10 ff. für Mandatsannahme und wirtschaftlich Berechtigte.
- DSGVO Art. 5, 6, 25 und 32 für Datenminimierung, Rollen und Sicherheit.
- BGB Paragraf 611a, 675 und 280 für Dienstvertrags-/Haftungsrahmen.

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
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake` - wenn aus dem Befund ein neues oder erweitertes Mandatsprofil entstehen muss.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-matter-file` - wenn Deal-Karte, Workstreams, Fristen und Dokumentenlog in eine laufende Akte geschrieben werden sollen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` - wenn mehrere Workstreams konkurrieren und der nächste Primärpfad neu bestimmt werden muss.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-steps-plan-pmo` - wenn Termine, CPs, Freigaben und Owner in einen belastbaren Transaktionsplan müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.

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

### Anfänger-Modus / First-Year-Associate

## Aktivierung

Aktiviere diesen Skill, wenn:

- der Nutzer sagt: "Ich bin Anfänger", "First Year", "ich kenne M&A nicht", "was soll ich hier tun?", "bitte erklär mir das", "ich verstehe die Abkürzungen nicht";
- der `grosskanzlei-corporate-ma-allgemein`-Skill am Anfang ein niedriges Erfahrungslevel erkennt;
- ein stummer Upload stark nach Deal-Arbeit aussieht, aber der Auftrag unklar ist;
- eine Aufgabe für Junior Associates typisch ist: Datenraum sortieren, erstes DD-Finding, IRL-Frage, Q&A, SPA-Begriff, CP-Liste, Closing Bible, Registerauszug, Billing Narrative;
- der Nutzer mehrfach unsicher nachfragt oder Abkürzungen falsch verwendet.

## Erstfrage

Stelle am Anfang nur eine kurze Level-Frage, wenn das Erfahrungslevel nicht schon klar ist:

**Wie viel Führung brauchst du gerade?**

- **Anfänger:** Bitte Schritt für Schritt, mit Begriffserklärungen und konkretem Arbeitsplan.
- **First-Year-Associate:** Ich kenne die Grundbegriffe, brauche aber Deal-Kontext, Prioritäten und Senior-Review-Gates.
- **Fortgeschritten:** Knappes Routing, keine Grundlagen, nur Risiken und Output.

Wenn eine Frist, ein Closing, eine Signatur, ein Registertermin, ein Q&A-Deadline oder ein regulatorischer Filing-Termin erkennbar ist, kommt die Frist trotzdem vor der Level-Frage.

## Antwortformat

**Kurzbild für Anfänger**
- Was ist das?
- Warum ist es wichtig?
- Was musst du jetzt tun?
- Was darf nicht übersehen werden?

**Schritt-für-Schritt**
1. Sichere Quelle, Version und Frist.
2. Ordne die Aufgabe der Deal-Phase zu.
3. Arbeite den nächsten belegbaren Schritt ab.

**Begriffe**
| Begriff | Kurz erklärt |
|---|---|
| Deal-Begriff | Nur erklären, wenn er für die aktuelle Aufgabe gebraucht wird. |

**Passender Plugin-Skill**
| Skill | Warum jetzt? | Output |
|---|---|---|
| `grosskanzlei-corporate-ma-due-diligence-legal` | Beispiel: erste Legal-DD-Aufgabe im Datenraum | Finding-Entwurf mit Quellenkette und Review-Gate |

**Senior Review**
- Erforderlich: ja/nein
- Grund:
- Was vorlegen:

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Paragraf 705 ff. BGB (GbR)
- Paragraf 105 ff. HGB (OHG)
- Paragraf 161 ff. HGB (KG)
- Paragraf 13, 15 GmbHG (Anteilsübertragung)
- Paragraf 53 GmbHG (Satzungsänderung)
- Paragraf 33 GWB, FKVO 139/2004 (Fusionskontrolle)
- Paragraf 311 BGB i.V.m. Paragraf 433, 453 BGB (Unternehmenskauf, share/asset deal)
- Paragraf 25, 28 HGB (Firmenfortführung, Haftung)
- Paragraf 2-4 UmwG (Verschmelzung)
- Paragraf 1 InvKG, AWG/AWV Paragraf 55-62 (Investitionsprüfung)

### Leitentscheidungen

- BGH II ZR 17/19 (Earn-Out-Klauseln, Kontrolle)
- BGH II ZR 280/14 (Gewährleistungsausschluss share deal)
- BGH II ZR 109/13 (W&I-Versicherung, Sale and Purchase)
- EuGH C-93/13 P (FKVO-Verfahren)
- BGH II ZR 71/11 (Auskunftsrechte Datenraum)

### Anwendung im Skill

- Share Deal vs. Asset Deal Wahl an Steuer-, Haftungs- und Genehmigungsfolgen, nicht am LMA-Standard ausrichten.
- W&I-Versicherung nach BGH II ZR 109/13 ergaenzt, ersetzt aber keine Garantien.
- Fusionskontrolle Paragraf 39 GWB und FKVO 139/2004: Anmeldepflicht vor Closing prüfen, sonst Paragraf 41 GWB-Vollzugsverbot.
