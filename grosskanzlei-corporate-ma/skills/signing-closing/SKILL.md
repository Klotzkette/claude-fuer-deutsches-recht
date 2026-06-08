---
name: signing-closing
description: "Signing-to-Closing-Prozess mit Conditions Precedent für M&A-Transaktionen: Anwendungsfall nach Signing muessen alle Closing-Bedingungen erfuellt und Closing Deliverables koordiniert werden. SPA Closing Conditions, § 179a AktG Hauptversammlungsvorbehalt, §§ 35 ff. GWB Kartellfreigabe. Prüfraster alle CPs identifiziert und zugeordnet, Ordinary-Course-Covenants überwacht, Bring-down-Condition aktuell, Funds Flow koordiniert. Output CP-Tracker mit Owner Frist Status und Closing-Checkliste. Abgrenzung zu Regulatory-FDI-Merger-Control und zu Closing-Bible für Archivierung."
---

# Signing, Closing und Conditions Precedent

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Signing, Closing und Conditions Precedent
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Zweck
Dieser Skill führt ein Big-Law Corporate/M&A-Mandat durch den Arbeitsbereich **SPA/APA, Disclosure, Signing, Closing und Post-Closing-Mechanik**. Er übersetzt die vorhandenen Unterlagen in einen verwertbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und zwingt zu einem senior-review-fähigen nächsten Schritt. Adressaten sind Partner, Counsel, Associates, Legal-Operations-Team und Inhouse-Counsel in großvolumigen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Signing, Closing und Conditions Precedent und brauche einen belastbaren nächsten Schritt."
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

## Pruefraster im Gutachtenstil
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

### Signing, Closing und Conditions Precedent

## Zweck

Fuehrt Signing-to-Closing-Prozess: Conditions Precedent (CPs), Ordinary Course Covenants, Bring-down-Condition, Closing Deliverables, Funds Flow und Closing Bible. Stellt sicher, dass alle Closing-Voraussetzungen zeitgerecht erfullt sind und der Closing-Ablauf reibungslos vollzogen wird.

## Triage — klaere vor Signing

1. Welche Conditions Precedent sind im SPA vereinbart — Regulatorisch (Kartell, FDI), Gesellschaftsrechtlich (Beschluesse, Genehmigungen), W&I-Deckungsbestaetigung?
2. Welche Ordinary Course Covenants gelten zwischen Signing und Closing — Veraeußerungsverbote, Investitionskoerbe, Personalaenderungen?
3. Wer ist verpflichtet, jede CP zu erfullen — Kaeufer, Verkaeufer, Zielgesellschaft? Welche Frist gilt?
4. Was ist das Longstop Date — Datum, bis zu dem alle CPs erfullt sein muessen, andernfalls Ruecktrittsrecht?
5. Welche Bring-down-Bedingung gilt — sind alle Garantien beim Closing noch zutreffend (Material Adverse Change-Pruefung)?
6. Welcher Notar/Treuhander begleitet das Signing und das Closing?

## Zentrale Rechtsgrundlagen

- §§ 158, 159 BGB — aufschiebende und aufloesende Bedingung; CPs als suspensive Bedingung; Rechtsfolge: Vertrag schwebend wirksam
- § 275 BGB — Unmoeglichkeit der CP-Erfullung: Ruecktritt bei dauerhafter Unmoeglichkeit (Closing-Versagung)
- § 323 BGB — Ruecktritt bei Nichterfuellung der Closing Conditions; Frist und Ruecktrittserklaerung
- § 15 Abs. 3 GmbHG — notarielle Beurkundung bei GmbH-Anteilen: Closing erst nach vollstaendiger Beurkundung wirksam
- § 40 GmbHG — Gesellschafterliste binnen eines Monats nach Closing; Eintrag durch Notar
- §§ 35-44 GWB; Art. 4 FKVO — kartellrechtliche Fusionskontrolle: aufschiebende Wirkung; Vollzugsverbot bis zur Freigabe
- § 55 ff. AWV — FDI-Screening: Investitionspruefung; aufschiebende Wirkung bei priifpflichtigen Transaktionen
- §§ 346-348 BGB — Rueckgewahr bei Ruecktritt vom Vertrag; Nutzungsersatz, Wertminderung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **CP-Register anlegen:** alle CPs aus SPA extrahieren; je CP: Owner, Faelligkeit, Nachweis (Behördenbescheid, Beschluss, Zertifikat), Eskalationsstufe
2. **Kartell- und FDI-Timeline:** bei Fusionskontrollpflicht §§ 35 ff. GWB: Filing-Datum plus 4 Wochen (Phase I) oder Phase-II-Risiko einkalkulieren; FDI § 55 AWV: 2-4 Monate
3. **Ordinary Course Covenants ueberwachen:** wochentliche Kontrolle Veraeusserungsverbote, Investitionskoerbe, wesentliche Vertragsaenderungen, Personalentscheidungen
4. **Bring-down-Check:** Tage vor Closing alle SPA-Garantien gegen Ist-Zustand pruefen; MAC-Pruefung; eventuelle Closing-Verweigerung dokumentieren
5. **Closing Deliverables vorbereiten:** Gesellschafterliste, Vollmachten, Organschaftsbeschluesse, Bankbestaetigung, W&I-Deckungszusage, Funds Flow Statement
6. **Funds Flow koordinieren:** Kaufpreis, Auszahlungsanweisung, Bankfreigaben, Escrow; Timing: T-0 Überweisungsnachweis vor Closing-Vollzug
7. **Closing-Ablauf durchfuhren:** Zug-um-Zug (§ 322 BGB analog) — Dokumente gegen Kaufpreiszahlung; Notar oder Treuhander als Closing Agent
8. **Post-Closing-Pflichten:** Gesellschafterliste (§ 40 GmbHG), Transparenzregister, Registeranmeldungen, W&I-Notification-Fristen

## Entscheidungsbaum

- Kartell-CP → GWB-Filing erforderlich → Vollzugsverbot bis Freigabe → Gun Jumping vermeiden
- FDI-CP → § 55 AWV → Genehmigung abwarten → bei Verstoß: Nichtigkeit des Vollzugs
- Bring-down scheitert → MAC ausgeloest → Kaeufer hat Ruecktrittsrecht → Pruefung und Dokumentation sofort
- Longstop Date erreicht ohne CP → Ruecktrittsrecht → Frist 2 Wochen für Ruecktrittserklaerung (§ 349 BGB)

## Output-Template: CP-Tracker

**Adressat:** Deal-Team intern — Tonfall sachlich-strukturiert

```
CP-TRACKER
Deal: [DEALNAME] — Signing: [DATUM] — Longstop: [DATUM]

| Nr. | CP-Bezeichnung | Owner | Faelligkeit | Nachweistyp | Status |
|----|---------------|-------|------------|-------------|--------|
| 1 | Kartellfreigabe (BKartA) | [KAEUFER] | [DATUM] | Behördenbescheid | Ausstehend |
| 2 | FDI-Freigabe § 55 AWV | [KAEUFER] | [DATUM] | BMWi-Schreiben | Ausstehend |
| 3 | Gesellschafterbeschluss Verkaeufer | [VERKAEUFER] | [DATUM] | Notarielles Protokoll | OK |
| 4 | W&I Deckungszusage | [VERKAEUFER] | [DATUM] | Versicherer-Schreiben | TODO |

AMPEL: [ ] Alle CPs gruen [ ] CPs ausstehend — Eskalation erforderlich
```

## Rote Schwellen

- Vollzug vor Kartell-Freigabe (Gun Jumping): Bussgeld bis 10 % des Konzernumsatzes (Art. 14 FKVO)
- Bring-down-Check nicht durchgefuehrt: Kaeufer verliert MAC-Ruecktrittsrecht
- Funds Flow unklar vor Closing: Kaufpreis-Auszahlungsrisiko; Closing vertagen
- Longstop Date uebersehen: automatisches Ruecktrittsrecht entsteht; Vertragsende

## Standardausgabe

- CP-Tracker mit Ampel
- Closing Deliverables-Checkliste
- Bring-down-Protokoll

## Uebergabe an andere Skills

- Kartell/FDI → `grosskanzlei-corporate-ma-regulatory-fdi-merger-control`
- Closing Bible → `grosskanzlei-corporate-ma-closing-bible-archiv`
- Post-Closing → `grosskanzlei-corporate-ma-post-closing-integration`
- Fristen → `grosskanzlei-ma-fristen-cp-kalender`

## Vorlagen

- assets/templates/cp-tracker-signing-closing.md
- assets/templates/closing-deliverables-register.md

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
