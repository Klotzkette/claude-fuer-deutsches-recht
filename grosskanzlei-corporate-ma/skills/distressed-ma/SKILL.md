---
name: distressed-ma
description: "Distressed M&A Transaktion begleiten: Anwendungsfall Unternehmen in Krise oder Insolvenz soll verkauft werden oder Investor prüft Erwerb notleidender Vermögenswerte. Paragraf 17-19 InsO Insolvenztatbestaende, Paragraf 1 StaRUG Sanierung, Paragraf 433 ff. BGB Share/Asset Deal. Prüfraster Insolvenzreife-Prüfung, Antr..."
---

# Distressed M&A

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten; BGH, 20.11.2018 - II ZR 12/17 für Gesellschafterlisten. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Distressed M&A
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Distressed M&A und brauche einen belastbaren nächsten Schritt."
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
Vor Mandatsarbeit sind Interessenkonflikte nach Paragraf 43a BRAO und Paragraf 3 BORA, Verschwiegenheit nach Paragraf 43a Abs. 2 BRAO, Vergütungsrahmen nach Paragraf 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Distressed M&A

## Triage — klaere vor Strukturentscheidung

1. Welcher Krisenstatus besteht — drohende Zahlungsunfaehigkeit (Paragraf 18 InsO), Zahlungsunfaehigkeit (Paragraf 17 InsO) oder Ueberschuldung (Paragraf 19 InsO)?
2. Wurde bereits ein Insolvenzantrag gestellt? Gibt es einen vorläufigen Insolvenzverwalter?
3. Laeuft ein StaRUG-Verfahren — Restrukturierungsplan, Restrukturierungsbeauftragter, Moratorium?
4. Welche Erwerbsstruktur ist geplant — Asset Deal aus der Insolvenz, uebertragende Sanierung, Share Deal mit Sanierungsplan, Insolvenzplan mit Debt-Equity-Swap?
5. Gibt es wesentliche Sicherheiten (Pfandrechte, Sicherungsuebereignungen, Grundpfandrechte), die in den Erwerb einbezogen werden müssen?
6. Besteht Betriebsuebergang nach Paragraf 613a BGB — welche Arbeitnehmer sollen uebernommen werden?

## Zentrale Rechtsgrundlagen

- Paragraf 17-19 InsO — Insolvenztatbestaende: Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit, Ueberschuldung
- Paragraf 15a InsO — Antragspflicht: 3 Wochen bei Zahlungsunfaehigkeit; 6 Wochen bei Ueberschuldung
- Paragraf 15b InsO — Haftung für masseschmaeIernde Zahlungen nach Insolvenzreife
- Paragraf 129-147 InsO — Insolvenzanfechtung: Nachteilsbewusstsein, Vorsatzanfechtung (Paragraf 133 InsO), Sicherungsanfechtung (Paragraf 135 InsO); Frist bis zu 10 Jahre
- Paragraf 163, 233 InsO — Uebertragender Sanierung: Veraeusserung des Unternehmens durch Insolvenzverwalter
- Paragraf 217-269 InsO — Insolvenzplan: Sanierungsplan mit Debt-Equity-Swap; Gläubigerzustimmung
- Paragraf 1-93 StaRUG — vorinsolvenzlicher Restrukturierungsrahmen: setzt drohende Zahlungsunfaehigkeit voraus; kein öffentliches Verfahren noetig
- Paragraf 613a BGB — Betriebsuebergang bei Asset Deal: Uebergang aller Arbeitsverhaeltnisse kraft Gesetzes; Widerspruchsrecht

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Schritt-für-Schritt-Workflow

1. **Krisencheck:** Insolvenztatbestand (Paragraf 17-19 InsO) bestimmen; Antragspflicht (Paragraf 15a InsO) und Fristen prüfen; Liquiditaetsvorschau anfordern
2. **Strukturwahl:** Asset Deal / uebertragende Sanierung vs. Share Deal aus der Insolvenz vs. StaRUG-Plan vs. Insolvenzplan
3. **Anfechtungsrisiko-Analyse:** Paragraf 133 InsO (Vorsatz), Paragraf 135 InsO (Sicherheiten, Gesellschafterdarlehen), Paragraf 131 InsO (kongruente/inkongruente Deckung) — kritischer Zeitraum 4 Jahre rueckwirkend
4. **Sicherheitenlage kartieren:** Pfandrechte, Sicherungsuebereignungen, Grundpfandrechte, Eigentumsvorbehalt — welche Sicherheiten werden mit erworben?
5. **Paragraf 613a BGB-Prüfung:** welche Arbeitnehmer uebernommen? Informationspflicht, Widerspruchsrecht (Frist: mind. 1 Monat); bei Nicht-Information: Schadensersatz
6. **Insolvenzverwalter-Interface:** öffentliche Bekanntmachung, Angebot, Gläubigerzustimmung, Insolvenzgericht; due diligence im eingeschraenkten Datenraum
7. **W&I und Closing-Risiko:** W&I bei Distressed meist ausgeschlossen; stattdessen: Disclosure-basierter Haftungsausschluss, MAC-Trigger im SPA
8. **Liquiditaetsampel und CP-Kalender:** Mindestliquiditaet bis Closing sichern; CPs prüfen (Insolvenzgericht-Genehmigung, Gläubigerzustimmung)

## Entscheidungsbaum

- Antrag noch nicht gestellt → Zahlungsunfaehigkeit vorhanden → Antragspflicht Paragraf 15a InsO → sofort Insolvenzverwaltung informieren
- Vorlaeufige Insolvenz → Zustimmungsvorbehalt des vorl. IV → Asset Deal nur mit dessen Zustimmung wirksam
- StaRUG laufend → kein öffentliches Verfahren → Restrukturierungsplan muss Wertpruefung bestehen
- Asset Deal → Paragraf 613a BGB → Informationspflicht → Arbeitnehmer Widerspruchsrecht 1 Monat

## Output-Template: Distressed-M&A-Timeline

**Adressat:** Deal-Team, Insolvenzverwalter, Senior Partner — Tonfall sachlich-strukturiert

```
DISTRESSED M&A TIMELINE
Deal: [DEALNAME] — Status: [Krisenphase]

PHASE 1: Krisencheck und Strukturentscheidung bis [DATUM]
 - Liquiditaetsvorschau 13 Wochen
 - Insolvenzreife-Pruefung: Paragraf 17-19 InsO
 - Strukturentscheidung: Asset Deal / StaRUG / Insolvenzplan

PHASE 2: Due Diligence und SPA-Verhandlung bis [DATUM]
 - Datenraum: eingeschraenkt
 - Anfechtungsrisiko-Analyse Paragraf 129-147 InsO
 - Paragraf 613a BGB — Arbeitnehmer-Mapping

PHASE 3: Signing und Genehmigungen bis [DATUM]
 - Insolvenzgericht-Genehmigung (Paragraf 160, 163 InsO)
 - Glaeubigerzustimmung (Paragraf 157, 244 InsO)

PHASE 4: Closing bis [DATUM]
 - Funds Flow, Freigabe Sicherheiten
 - Anmeldung HR, Transparenzregister
 - Paragraf 613a BGB Information Arbeitnehmer

OFFENE PUNKTE: [konkreter Punkt] — Verantwortlich: [Name] — Frist: [Datum]
```

## Rote Schwellen

- Insolvenzrechtlicher Status unklar: Antragspflicht Paragraf 15a InsO laeuft; Haftung Geschäftsführer Paragraf 15b InsO
- Anfechtungsrisiko nicht geprueft: Asset Deal anfechtbar; Sicherheiten fallen zurueck zur Masse
- Paragraf 613a BGB-Information unterlassen: Schadensersatz; alle Arbeitsverhaeltnisse gehen über
- Liquiditaetslücke vor Closing: MAC-Trigger im SPA; Closing-Versagung

## Standardausgabe

- Distressed-M&A-Timeline
- Deal-Strukturvergleich
- Liquiditaets- und Antragspflicht-Ampel
- Closing-Faehigkeitscheck mit Belegkette

## Übergabe an andere Skills

- Insolvenzreife-Detail → `grosskanzlei-ma-insolvenzreife`
- Liquiditaet → `grosskanzlei-ma-liquiditaetsvorschau`
- StaRUG → `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan`
- Signing/Closing CPs → `grosskanzlei-corporate-ma-signing-closing-conditions`

## Vorlagen

- assets/templates/distressed-ma-timeline.md
- assets/templates/distressed-ma-liquiditaetsampel.md
- assets/templates/insolvenzplan-ma-checklist.md
- assets/templates/cash-bridge-13-wochen.md
