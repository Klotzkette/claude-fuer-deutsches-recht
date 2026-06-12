---
name: deal-team-staffing
description: "Deal-Team-Besetzung und Staffing-Plan für Corporate/M&A-Transaktionen: Anwendungsfall Senior-Partner oder Team-Lead muss Workstreams Anwalt, Counsel, Associate, Paralegals und externe Spezialisten zuweisen. §§ 43a BRAO Interessenkonflikte, § 3a RVG Budget. Prüfraster Workstream-Anforderungen, Erf..."
---

# Deal-Team und Staffing

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Deal-Team und Staffing
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Team und Staffing und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Board-/Shareholder-Approvals.
- Disclosure Letter, Knowledge-Definition, W&I-Underwriting-Liste.

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
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

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
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-spa-apa-entwurf` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-vertragsmarkup-key-issues` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-closing-bible-archiv` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

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

### Deal-Team und Staffing

## Arbeitsmodus

- Workstreams Recht, Tax, Finance, ESG, IP/IT, Employment, Regulatory, Litigation, Real Estate und PMI anlegen.
- Owner, Reviewer, Partner, Mandant und Deadline je Workstream bestimmen.
- Follow-the-sun oder Multi-Jurisdiction-Setup abbilden.
- Überlastung und Review-Lücken sichtbar machen.

## Rote Schwellen

- Kein Senior Review für Red Flags.
- Keine klare Mandantenfreigabe.
- Materiality-Schwellen ohne Owner.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/deal-team-staffing-plan.md
- assets/templates/authority-matrix.md

## Triage

1. Was ist die Deal-Komplexitaet — Groß-Transaktion (Cross-border, Multi-Jurisdiktion) oder Standard-M&A?
2. Welche Workstreams sind zu besetzen — Corporate, Steuer, Arbeitsrecht, IP, Real Estate, Regulatory, Finance?
3. Welche Kapazitaeten sind intern verfuegbar — Senior Associate, Associate, Partner?
4. Sind externe Co-Counsel oder lokale Kanzleien für andere Jurisdiktionen erforderlich?
5. Was ist das Honorarbudget und die Abrechnungsstruktur — Time-Based, Capped Fee, Success Fee?

## Zentrale Rechtsgrundlagen

- § 43a BRAO — Interessenkonflikt innerhalb des Deal-Teams: jeder Teamanwalt muss conflicts-geprueft sein
- §§ 10, 11 GwG — GwG-Pflichten gelten für alle eingebundenen Berufsträger; Teamleiter traegt Gesamtverantwortung
- § 49b BRAO — Honorarvereinbarung: bei M&A-Mandaten vertragliche Vereinbarung über Abrechnungsmodalitaeten; schriftliche Basis empfohlen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Workstream-Matrix erstellen:** je Workstream: Leader, Reviewer, Associate, Deadline
2. **Kapazitaetspruefung:** interne Verfuegbarkeit prüfen; bei Engpass: Co-Counsel-Einbindung
3. **Conflicts-Check für gesamtes Team:** § 43a BRAO; alle Teamanwaltseintragungen im Conflicts-System
4. **Eskalationswege definieren:** wer entscheidet bei Red Flag, Deal-Breaker, Media-Anfragen?
5. **Honorarstruktur abstimmen:** Budget-Tracking, weekly Status, Kunden-Reporting

## Rote Schwellen

- Workstream ohne qualifizierten Spezialisten: Haftungsrisiko
- Kein Conflicts-Check für Team-Mitglieder: § 43a BRAO-Verstoß
