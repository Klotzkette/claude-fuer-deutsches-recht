---
name: umwandlungsrecht
description: "Umwandlungsrecht Verschmelzung Spaltung Formwechsel und Carve-outs nach UmwG bearbeiten: Anwendungsfall Mandant plant Verschmelzung zweier GmbHs Ausgliederung eines Geschäftsbereichs oder Formwechsel AG zu GmbH im Rahmen einer Transaktion. §§ 2-38 UmwG Verschmelzung, §§ 123-173 UmwG Spaltung, §§..."
---

# Umwandlungsrecht

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Umwandlungsrecht
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Umwandlungsrecht und brauche einen belastbaren nächsten Schritt."
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

### Umwandlungsrecht

## Triage — klaere vor Strukturentscheidung

1. Welche Umwandlungsart ist geplant — Verschmelzung (§§ 2-38 UmwG), Spaltung/Ausgliederung (§§ 123-173 UmwG) oder Formwechsel (§§ 190-304 UmwG)?
2. Welche Rechtsformen sind beteiligt — GmbH, AG, KGaA, GmbH & Co. KG, SE, Genossenschaft?
3. Sind steuerliche Rueckwirkungszeitraeume einzuhalten (§§ 2 Abs. 1, 20 Abs. 5 UmwStG: maximal 12 Monate Rueckwirkung)?
4. Gibt es eine Vorwegausgliederung als Deal-Preparation — ist der Carve-out-Zeitplan mit der Signing-Deadline vereinbar?
5. Welche Gläubigerschutzmaßnahmen sind erforderlich — § 22 UmwG Sicherheitsleistung bei Verschmelzung?
6. Welche Arbeitnehmer- und Betriebsratsrechte sind zu beachten — § 324 UmwG i.V.m. § 613a BGB?

## Zentrale Rechtsgrundlagen

- §§ 2-38 UmwG — Verschmelzung: Vertrag, Bericht, Prüfung, Beschluss, Anmeldung; Gesamtrechtsnachfolge
- §§ 123-137 UmwG — Spaltung (Aufspaltung, Abspaltung, Ausgliederung): Spaltungsplan, Beschluss
- §§ 311-312 UmwG — Ausgliederung zur Neugründung: erleichterte Form für Carve-out
- §§ 190-213 UmwG — Formwechsel: keine Vermögensuebertragung; Identitaetswahrung des Rechtsträgers
- § 22 UmwG — Gläubigerschutz: auf Verlangen Sicherheitsleistung für ungesicherte Gläubiger
- § 325 UmwG — Spruchverfahren: Barabfindung und Abfindungsangebot bei Formwechsel und Ausgliederung
- § 324 UmwG i.V.m. § 613a BGB — Arbeitnehmeruebergang kraft Gesetzes bei Ausgliederung; Unterrichtungspflicht
- §§ 2 Abs. 1, 20 Abs. 5 UmwStG — steuerliche Rueckwirkung bei Verschmelzung und Einbringung: maximal 12 Monate

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Umwandlungstyp bestimmen:** Verschmelzung, Abspaltung, Ausgliederung, Formwechsel — massgeblich für Form und Gremien
2. **Zeitplan aufstellen:** Notartermin, Beschlussfassung, Registereintragung (i.d.R. 2-4 Monate ab Beschluss); Steuerliche Rueckwirkungsfrist einhalten (§§ 2 Abs. 1, 20 Abs. 5 UmwStG)
3. **Beschlüsse vorbereiten:** Gesellschafterversammlung/Hauptversammlung mit notarieller Beurkundung; Mehrheitserfordernisse prüfen (§ 50 UmwG: 75 % bei GmbH)
4. **Bericht erstellen:** Geschäftsführung/Vorstand muss Umwandlungsbericht erstellen (§§ 8, 127 UmwG); bei Prüfungspflicht: externer Prüfer
5. **Gläubigerschutz sicherstellen:** § 22 UmwG — Gläubiger können Sicherheitsleistung verlangen; Ankuendigung und Frist beachten
6. **Arbeitnehmerinformation:** § 324 UmwG i.V.m. § 613a BGB — schriftliche Unterrichtung der uebernommenen Arbeitnehmer; Betriebsrat informieren
7. **Anmeldung zum HR:** notariell beglaubigte Anmeldung zum Handelsregister; Eintragung konstitutiv
8. **Steuerliche Rueckwirkung sichern:** Massgeblichkeitsstichtag für steuerliche Bilanz festlegen; Frist maximal 12 Monate rueckwirkend ab Abschlussstichtag

## Entscheidungsbaum

- Verschmelzung → Gesamtrechtsnachfolge → alle Verträge gehen über → Change-of-Control-Klauseln prüfen
- Ausgliederung → Einzelrechtsnachfolge je uebertragener Position → Zustimmung Gläubiger bei Schulduebertragung?
- Formwechsel → Identitaetswahrung → kein Betriebsuebergang, aber Abfindungsangebot nach § 207 UmwG
- Steuerrueckwirkung → mehr als 12 Monate? → kein Buchwertansatz; stille Reserven aufzudecken

## Output-Template: Umwandlungs-Checkliste

**Adressat:** Deal-Team, Notar, Steuerteam — Tonfall sachlich-juristisch

```
UMWANDLUNGS-CHECKLISTE
Art: [VERSCHMELZUNG / AUSGLIEDERUNG / FORMWECHSEL]
Rechtsträger: [UEBERTR. RT] → [AUFNEHMENDER RT]
Zieldatum Eintragung: [DATUM]

SCHRITT | VERANTWORTLICHER | TERMIN | STATUS
Umwandlungsvertrag/-plan | [NAME] | [DATUM] | [ ]
Umwandlungsbericht | [NAME] | [DATUM] | [ ]
Pruefung (falls pflichtig) | [PRUEFER] | [DATUM] | [ ]
GV-/HV-Beschluss (75 %) | Notar [NAME] | [DATUM] | [ ]
Glaeubigerschutz § 22 UmwG | [NAME] | [DATUM] | [ ]
Arbeitnehmer-Info § 613a BGB | [NAME] | [DATUM] | [ ]
HR-Anmeldung | Notar [NAME] | [DATUM] | [ ]
Steuerl. Schlusspunkt UmwStG | Steuer [NAME] | [DATUM] | [ ]
```

## Rote Schwellen

- Beschluss-/Berichtserfordernis offen: Eintragung durch Registergericht abgelehnt
- Steuerliche Rueckwirkung oder Sperrfrist nicht geprueft: stille Reserven werden aufgedeckt; Steuerbelastung
- Spruchverfahrensrisiko nicht einkalkuliert: Prozesskosten und Nachzahlungen können erheblich sein

## Standardausgabe

- Umwandlungs-Checkliste mit Zeitplan, Owner und Status
- Offene Punkte als `TODO` mit Eskalationsstufe
- Belegkette: Normen, Beschlüsse, Registerschritte

## Übergabe an andere Skills

- Steuer → `grosskanzlei-corporate-ma-umwandlungssteuerrecht`
- Gesellschaftsrecht/Register → `grosskanzlei-corporate-ma-gesellschaftsrecht-register`
- Transaktionsstruktur → `grosskanzlei-corporate-ma-transaktionsstruktur`

## Vorlagen

- assets/templates/umwandlungsrecht-checkliste.md
- assets/templates/verschmelzung-spaltung-formwechsel-plan.md
