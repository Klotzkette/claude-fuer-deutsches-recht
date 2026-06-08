---
name: conflict-gwg
description: "Mandatsannahme-Prüfung im Corporate/M&A-Mandat: Interessenkonflikte nach § 43a BRAO, Geldwäschegesetz-Prüfung wirtschaftlich Berechtigter nach § 3 GwG, Sanktionsscreening nach AWG und EU-Verordnungen. Anwendungsfall neue Transaktionsmandate mit PEP-Verdacht, Sektorrisiken oder konzernverbundenen Gegenparteien. Prüfraster Interessenkonflikt-Check, UBO-Identifikation, Sanktionslisten-Abgleich, Mittelherkunft, Länderrisiko. Output Annahmevermerk mit Ampelstatus, Dokumentationsprotokoll und ggf. Mandatsablehnungs-Schreiben. Abgrenzung zu KI-Governance-Berufsrecht Skill und zu Datenraum-Aufbau."
---

# Konflikt-, GwG- und Sanktionscheck

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Konflikt-, GwG- und Sanktionscheck
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Zweck
Dieser Skill führt ein Big-Law Corporate/M&A-Mandat durch den Arbeitsbereich **Datenraum, Legal Due Diligence und Information-Request-Steuerung**. Er übersetzt die vorhandenen Unterlagen in einen verwertbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und zwingt zu einem senior-review-fähigen nächsten Schritt. Adressaten sind Partner, Counsel, Associates, Legal-Operations-Team und Inhouse-Counsel in großvolumigen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Konflikt-, GwG- und Sanktionscheck und brauche einen belastbaren nächsten Schritt."
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

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 für Insiderinformationen, Ad-hoc-Prüfung und Insiderlisten.

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
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Konflikt-, GwG- und Sanktionscheck

## Zweck

Fuehrt Annahme- und Begleitpruefung für Corporate/M&A-Mandate: Interessenkonflikte nach § 43a BRAO, wirtschaftlich Berechtigte nach GwG, Sanktionen nach AWG/EU-Verordnungen, PEP-Status, Mittelherkunft und Länder-/Sektorrisiken.

## Triage — klaere vor Mandatsannahme

1. Sind alle Parteien (Kaeufer, Verkaeufer, Zielgesellschaft, Garantiegeber, Finanziers) und ihre wirtschaftlich Berechtigten identifiziert?
2. Besteht ein bestehender oder frueherer Mandatsbezug zu einer der Gegenparteien oder zur Zielgesellschaft?
3. Stehen Parteien oder wirtschaftlich Berechtigte auf Sanktionslisten (EU-Sanktionsregister, OFAC SDN, UK OFSI)?
4. Liegt PEP-Status vor (politisch exponierte Person, § 1 Abs. 12 GwG)?
5. Ist die Herkunft der Transaktionsmittel nachvollziehbar (Equity, Kredit, Fonds, Family Office)?
6. Sind Sektoren oder Ziellaender betroffen, die erhoehtem Risiko unterliegen (Dual Use, Verteidigung, kritische Infrastruktur, FDI-Screening)?

## Zentrale Rechtsgrundlagen

- § 43a Abs. 4 BRAO — anwaltliches Verbot der Vertretung widerstreitender Interessen; gilt auch bei verbundenen Unternehmen
- §§ 10-17 GwG — Sorgfaltspflichten: Identifizierung, wirtschaftlich Berechtigter, Herkunft von Vermoegenswerten, kontinuierliche Ueberwachung
- § 43 Abs. 1 GwG — Meldepflicht bei Geldwaescheverdacht an FIU; Schweigegebot § 47 GwG
- Art. 7 EU-Verordnung 833/2014 (Russland-Sanktionen) sowie VO 269/2014, 765/2006 und weitere EU-Sanktionsregimes — Bereitstellungsverbot, Umgehungsverbot
- §§ 17, 18 AWG i.V.m. AWV — Strafbarkeit bei vorsaetzlicher Sanktionsumgehung
- § 4 Abs. 6 GwG — Pflicht zur Risikoklassifizierung; verstaerkte Sorgfaltspflichten bei hohem Risiko
- § 2 Abs. 1 Nr. 10 GwG — Rechtsanwaelte als Verpflichtete bei bestimmten Transaktionsberatungen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Parteien-Screening:** alle Parteien inkl. wirtschaftlich Berechtigter (mind. 25 % Beteiligungsschwelle, § 3 GwG) identifizieren und in internem Conflicts-System abgleichen
2. **Sanktions-Screening:** EU-Sanktionsdatenbank, OFAC SDN, UK OFSI, UN-Liste pruefen; Treffer → sofortige Eskalation an Partner/Compliance
3. **Interessenkonflikt-Pruefung:** laufende und frueheres Mandate pruefen; bei positivem Treffer: Screening-Protokoll, ggf. Waiver-Einholung oder Mandatsablehnung
4. **PEP-Pruefung:** § 1 Abs. 12 GwG — bei Treffer: verstaerkte Sorgfalt (§ 15 GwG), Geschaftsfuehrungsebene einschalten
5. **Mittelherkunfts-Pruefung:** Funds Flow Confirmation, Bankauszuege, Fondsstruktur dokumentieren; bei Verdacht → FIU-Meldepflicht pruefen
6. **Sektoren-/FDI-Check:** § 55 ff. AWV, Art. 4 EU-FDI-Screening-VO — betrifft kritische Infrastruktur, Verteidigung, Energie, Telekommunikation
7. **Dokumentation:** Akte mit Screening-Protokoll, Entscheidungsgrunden, Datum und verantwortlichem Partner abschliessen

## Entscheidungsbaum

- Sanktionstreffer → JA: Mandatsannahme verboten; sofort an Compliance; NEIN: weiter
- Interessenkonflikt → JA ohne Waiver-Moeglichkeit: ablehnen; JA mit Waiver: dokumentieren; NEIN: weiter
- PEP-Status → verstaerkte Sorgfalt § 15 GwG; Genehmigung der Geschaftsfuehrung
- Unklare Mittelherkunft → Nachfrage; keine Annahme vor Klaerung; bei Verdacht FIU-Meldepflicht

## Output-Template: Conflicts- und GwG-Pruefungsprotokoll

**Adressat:** Partner, Compliance — Tonfall sachlich-intern

```
CONFLICTS & GWG SCREENING PROTOKOLL
Deal: [DEALNAME] — Mandat-Nr.: [AKTENZEICHEN]
Datum: [DATUM] — Bearbeiter: [NAME]

PARTEIEN
 Kaeufer: [NAME], WB: [NAME, ANTEIL %]
 Verkaeufer: [NAME], WB: [NAME, ANTEIL %]
 Zielgesellschaft: [NAME], WB: [NAME, ANTEIL %]

SANKTIONS-SCREENING
 Ergebnis: [ ] Kein Treffer [ ] Treffer → Eskalation
 Datenbank: EU, OFAC, OFSI — Datum: [DATUM]

CONFLICTS-CHECK
 Ergebnis: [ ] Kein Konflikt [ ] Konflikt → Waiver / Ablehnung
 Fruehere Mandate: [LISTE]

PEP-STATUS
 [ ] Nein [ ] Ja → verstaerkte Sorgfalt (§ 15 GwG)

MITTELHERKUNFT
 [ ] Dokumentiert — Quelle: [BANK/FONDS]
 [ ] Offen → Nachfrage bis [DATUM]

ERGEBNIS: [ ] Mandat annehmbar [ ] Eskalation erforderlich [ ] Ablehnung
Freigabe: [PARTNER] am [DATUM]
```

## Rote Schwellen

- Sanktionstreffer ohne Eskalation: unmittelbarer Verstoß gegen Bereitstellungsverbot (Strafbarkeit AWG)
- Interessenkonflikt ohne Waiver: § 43a Abs. 4 BRAO; Haftung der Sozietaet
- Fehlende GwG-Dokumentation: Bussgeld bis 1 Mio. EUR (§ 56 Abs. 1 GwG)
- FIU-Meldepflicht verletzt: § 43 GwG; Strafbarkeit

## Standardausgabe

- Screening-Protokoll mit Datum, Parteien, Ergebnis, Freigabe
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe
- Bei Treffer: sofortige Senior-Review und Partner-Freigabe

## Uebergabe an andere Skills

- Transparenzregister nach Closing → `grosskanzlei-corporate-ma-gesellschaftsrecht-register`
- FDI/AWV-Screening → `grosskanzlei-corporate-ma-regulatory-fdi-merger-control`
- Deal-Intake-Daten → `grosskanzlei-corporate-ma-deal-intake`

## Vorlagen

- assets/templates/conflicts-gwg-sanctions-protokoll.md
- assets/templates/sorgfaltspflichten-geldwaesche.md

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
