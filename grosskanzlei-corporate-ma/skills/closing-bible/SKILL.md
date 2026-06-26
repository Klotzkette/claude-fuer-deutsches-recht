---
name: closing-bible
description: "Erstellt Closing Bible und Deal-Archiv mit executed Agreements, Signaturseiten, Registerbelegen, CP-Nachweisen, Payments und Post-Closing-Pflichten."
---

# Closing Bible und Archiv

## Fachlicher Anker

- **Vollzug und Nachweis:** Paragraf 158, 362, 433, 453 BGB; Closing Conditions, Zahlungen, Deliverables und Erfüllungsnachweise.
- **GmbH-Share-Deal:** Paragraf 15, 16, 40 GmbHG für Abtretung, Gesellschafterliste und Legitimationsfolge.
- **Archiv und Belege:** Paragraf 257 HGB, Registerunterlagen, Notarbestätigungen, Board- und Shareholder-Approvals.
- **Leitentscheidungen:** BGH, 20.11.2018 - II ZR 12/17 für Bedeutung der Gesellschafterliste; BGH, 21.04.1997 - II ZR 175/95 für dokumentierte Organentscheidung.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Closing Bible und Archiv
- **Entscheidende Weiche:** Executed Version, Signing Evidence, CP Evidence, Closing Deliverable, Payment Evidence, Register Evidence und Post-Closing Covenant getrennt ablegen.
- **Archivlogik:** Jede Datei braucht Dokumenttyp, Datum, Parteien, Version, Unterschriftenstatus, Quelle, Vertraulichkeit und offenen Restpunkt.
- **Arbeitsprodukt:** Liefere eine Closing-Bible-Struktur mit Missing-Documents-Liste und Post-Closing-Hand-off.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Closing Bible und Archiv und brauche einen belastbaren nächsten Schritt."
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
- BGB Paragraf 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG Paragraf 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG Paragraf 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB Paragraf 158 für Closing Conditions und Bedingungseintritt.

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-spa-apa-entwurf` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-vertragsmarkup-key-issues` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

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

### Closing Bible und Archiv

## Triage — klaere vor Zusammenstellung

1. Welche Dokumente sind als "final executed" markiert — SPA, aller Anhange, Disclosure Schedules?
2. Liegen alle Signaturseiten im Original oder als beglaubigte Kopie vor?
3. Welche Registeranmeldungen sind erforderlich — GmbH-Anteilsuebertragung, Handelsregistereintrag, Transparenzregister-Update?
4. Sind Notarkosten und Vollzugspflichten aus dem beurkundeten SPA bereits abgearbeitet (Paragraf 15 Abs. 3 GmbHG, Paragraf 2 GmbHG)?
5. Welche Closing-Deliverables sind noch offen — Resolutions, Closing Certificates, Funds Flow, Bankfreigaben?

## Zentrale Rechtsgrundlagen

- Paragraf 15 Abs. 3 u. 4 GmbHG — notarielle Beurkundungspflicht für GmbH-Anteils- und SPA-Uebertragungen
- Paragraf 40 GmbHG — Gesellschafterliste nach Anteilsuebertragung innerhalb eines Monats; Pflicht des Notars oder Geschäftsführers
- Paragraf 20 TranspRG i.V.m. Paragraf 19 Abs. 1 GwG — Transparenzregistermeldung nach Gesellschafterwechsel innerhalb von zwei Wochen
- Paragraf 41 GmbHG — Pflicht zur Buchfuehrung nach Registereintragung
- Paragraf 179 AktG — Satzungsaenderung erfordert notarielle Beurkundung und HR-Anmeldung

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Schritt-für-Schritt-Workflow

1. **Closing-Deliverables-Register anlegen:** alle SPA-Deliverables aus Schedule/Annex extrahieren, Owner und Faelligkeitsdatum zuordnen
2. **Signaturketten prüfen:** für jeden signierten Vertrag: Originalunterschriften, Vollmachten, Vertretungsmacht gemäß Handelsregisterstand prüfen
3. **Notarpflichten abarbeiten:** SPA-Beurkundung, Anteilsuebertragung gemäß Paragraf 15 Abs. 3 GmbHG, Anlagen mitbeurkundet?
4. **Registeranmeldungen:** Gesellschafterliste gemäß Paragraf 40 GmbHG, HR-Anmeldung Geschäftsführerwechsel/Satzungsaenderung, Transparenzregister gemäß Paragraf 20 TranspRG
5. **Funds Flow und Closing Payments prüfen:** Kaufpreistransfernachweise, Bankbestaetigung, Freistellung von Sicherheiten
6. **Closing Bible zusammenstellen:** Inhaltsverzeichnis mit Tab-Struktur, je Dokument: Bezeichnung, Parteien, Datum, Fassung, Datenraum-Referenz
7. **Offene Punkte als Post-Closing Obligations:** Fristen, Owner, Eskalationsstufe
8. **Archivierung:** Deal-Archiv anlegen mit Zugriffskonzept, Vertraulichkeitsstufen, Retention Policy (Paragraf 257 HGB: 10 Jahre)

## Entscheidungsbaum

- GmbH-Anteilsuebertragung → Paragraf 15 Abs. 3 GmbHG → notarielle Beurkundung erforderlich → ohne Beurkundung: Nichtigkeit
- AG-Aktien vinkuliert → Zustimmung Hauptversammlung/AR-Beschluss prüfen → Eintrag Aktienbuch
- Transparenzregisterpflicht → Paragraf 19 GwG Wirtschaftlich Berechtigte neu? → Frist 2 Wochen ab Closing
- Registeranmeldung Namenswechsel/Satzungsaenderung → notarielle Form → Registergericht

## Output-Template: Closing Bible Index

**Adressat:** Deal-Team intern und Notar — Tonfall sachlich-strukturiert

```
CLOSING BIBLE
Transaction: [DEALNAME]
Closing Date: [DATUM]
Prepared by: [KANZLEI/PARTNER]

TAB A — TRANSACTION DOCUMENTS
 A-1 SPA, datiert [DATUM], Parteien: [KAEUFER] / [VERKAEUFER]
 A-2 Disclosure Schedules
 A-3 Signing Protocol / Notarakt Nr. [XX/XXXX]

TAB B — CORPORATE APPROVALS
 B-1 Gesellschafterbeschluss Verkaeufer [DATUM]
 B-2 Aufsichtsratsbeschluss [DATUM]
 B-3 Board Resolution Erwerber

TAB C — CLOSING DELIVERABLES
 C-1 Gesellschafterliste neu (Paragraf 40 GmbHG), eingereicht [DATUM]
 C-2 Transparenzregister-Meldung [DATUM]
 C-3 Funds Flow Confirmation [DATUM]
 C-4 Freigabe Bankpfandrecht [DATUM]

TAB D — POST-CLOSING OBLIGATIONS
 D-1 [MASSNAHME] — Owner: [NAME] — Faellig: [DATUM]
```

## Rote Schwellen

- Signaturseite ohne Original-Vollmacht: Human-in-the-loop verlangen, vor Archivabschluss Senior Review
- Gesellschafterliste nicht eingereicht (Paragraf 40 GmbHG): Frist laeuft; Stimmrecht des Erwerbers gefaehrdet (Paragraf 16 Abs. 1 GmbHG)
- Transparenzregistermeldung unterlassen: Bussgeld bis 100.000 EUR (Paragraf 56 GwG)
- Funds Flow nicht belegt: Zahlungsnachweis zwingend vor Closing-Bible-Freigabe

## Standardausgabe

- Closing Bible Index mit Tab-Struktur, Parteien, Datum, Datenraum-ID
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe
- Belegkette: Dokument, Datum, Version, Fundstelle
- Bei hohem Risiko immer Human-in-the-loop und Senior Review

## Übergabe an andere Skills

- Registerpunkte → `grosskanzlei-corporate-ma-gesellschaftsrecht-register`
- Notartermin, Beurkundungsfragen → `grosskanzlei-corporate-ma-output-versand-signing`
- Transparenzregister, GwG → `grosskanzlei-corporate-ma-conflict-gwg-sanctions`

## Vorlagen

- assets/templates/closing-bible-index.md
- assets/templates/closing-deliverables-register.md
