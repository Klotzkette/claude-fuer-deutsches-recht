---
name: wi-insurance
description: "Für W&I-Versicherung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# W&I-Versicherung

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: W&I-Versicherung
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier W&I-Versicherung und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:kommandocenter` oder `/grosskanzlei-corporate-ma:deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

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

**3. Organ- und Zuständigkeitsprüfung.** Nur wenn der konkrete Arbeitsschritt eine Organentscheidung vorbereitet, Zuständigkeit, Zustimmungsvorbehalte, Interessenkonflikte, Informationsgrundlage und Dokumentation prüfen. Der fachlich passende Haftungs- oder Board-Paper-Skill liefert die dafür einschlägige Rechtsprechung; ARAG/Garmenbeck ist kein Universalanker.

**4. Register- und Gesellschafterlistenlogik.** Nur bei GmbH-Anteilen, Einziehung, Vollmachtskette oder streitiger Legitimation Paragraf 16 und 40 GmbHG sowie Registerstand und materielle Berechtigung getrennt prüfen. Ohne solche Title- oder Legitimationsfrage diesen Prüfstrang auslassen.

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
- `/grosskanzlei-corporate-ma:spa-apa-entwurf` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:vertragsmarkup-key-issues` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/grosskanzlei-corporate-ma:signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/grosskanzlei-corporate-ma:closing-bible-archiv` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

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

### W&I-Versicherung

## Triage

1. Ist W&I-Versicherung vom Kaeufer oder Verkaeufer beabsichtigt — Buy-side oder Sell-side Policy?
2. Liegt ein vollstaendiger Red-Flag-Report und ein ausgefuellter Disclosure Letter vor — Underwriter verlangen vollstaendige DD-Dokumentation?
3. Welche Garantien sollen versichert werden — alle Business Warranties, oder nur Title und Financial Statements?
4. Ist ein Materiality Auslesen vorgesehen — entfaellt die Materiality-Schwelle für Versicherungsansprueche?
5. Wurden Synthetic Warranties vereinbart (warranties ohne SPA-Basis, nur für Versicherungszwecke)?
6. Wurden DD-Tools mit KI-Unterstuetzung eingesetzt — Underwriter verlangen Transparenz über KI-basierte DD-Methodik?

## Zentrale Rechtsgrundlagen

- SPA-Garantien und Freistellungen einerseits sowie die W&I-Police andererseits sind getrennte Verträge. Deckung, Ausschlüsse, Selbstbehalt, Wissensdefinition und Regress folgen zuerst dem jeweiligen Wortlaut; Paragraf 443 BGB ist keine allgemeine Anspruchsgrundlage für M&A-Garantien.
- Paragrafen 19 bis 22 VVG: Vorvertraglich sind die dem Versicherungsnehmer bekannten gefahrerheblichen Umstände anzuzeigen, nach denen der Versicherer in Textform gefragt hat. Rechtsfolge, Monatsfrist, Kausalität und Arglist getrennt prüfen.
- Paragraf 20 VVG: Wird der Versicherungsvertrag durch einen Vertreter des Versicherungsnehmers geschlossen, werden für die dort genannten Vorschriften Kenntnis und Arglist des Vertreters und des Versicherungsnehmers berücksichtigt. Daraus folgt keine pauschale Zurechnung des Wissens jedes Deal-Team-Mitglieds oder Beraters.
- Paragraf 28 VVG: Die Vorschrift betrifft die Verletzung einer vertraglich vereinbarten Obliegenheit. Leistungsfreiheit oder Kürzung setzen die vertragliche Anknüpfung sowie die gesetzlichen Voraussetzungen zu Verschulden, Kausalität und gegebenenfalls Belehrung voraus; sie folgen nicht automatisch aus einer Datenraumlücke.
- Paragrafen 59 und 61 VVG: Erst die Rolle als Versicherungsvertreter oder Versicherungsmakler bestimmen; Paragraf 61 VVG regelt dessen Beratungs- und Dokumentationspflichten und ist keine Leistungsfreiheitsnorm des Versicherers.
- Paragraf 166 BGB: Wissenszurechnung setzt eine konkrete Vertretung bei der maßgeblichen Willenserklärung voraus. Organ-, Deal-Team-, Makler- und Beraterwissen nicht ohne Prüfung von Funktion, Vollmacht, Police und Knowledge-Definition zusammenziehen.
- Paragrafen 69 und 70 VVG: Empfangs- und Kenntniszurechnung betreffen den Versicherungsvertreter auf Versichererseite; sie gelten nicht ohne Rollenprüfung für Versicherungsmakler oder sonstige Underwriting-Beteiligte.
- Paragraf 123 BGB und Paragraf 22 VVG: Eine Anfechtung des Versicherungsvertrags wegen arglistiger Täuschung erfordert eine Täuschung im Versicherungsverhältnis und deren konkrete Zurechnung. Verkäuferarglist begründet nicht automatisch Arglist des Versicherungsnehmers; Regress folgt nur aus den einschlägigen Vertrags- oder Gesetzesregeln.
- Paragraf 210 VVG: Bei Großrisiken zuerst prüfen, welche VVG-Regeln abdingbar sind und welche abweichenden Police-Klauseln wirksam vereinbart wurden.

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Schritt-für-Schritt-Workflow

1. **W&I-Struktur entscheiden:** Buy-side (Kaeufer versichert sich gegen Garantienverletzung des Verkaeuf ers) vs. Sell-side (Verkaeufer versichert seine Haftung); Buy-side in Europa Standard
2. **Underwriting-Unterlagen zusammenstellen:** Vollständiger DD-Report, Red-Flag-Report, Disclosure Letter, SPA-Entwurf sowie jede in Textform gestellte Underwriting-Frage mit der freigegebenen Antwort und ihrem Wissensgeber.
3. **AI-DD-Transparenz-Erklaerung:** falls KI-gestuetzte Datenraumanalyse eingesetzt — Methodik, Prüftiefe, Human-in-the-loop-Verfahren an Underwriter kommunizieren
4. **Deckungsausschlüsse verhandeln:** Bekannte Risiken, Umwelt, Cyber, Steuern, Pensionslasten und Rechtsstreitigkeiten positionsgenau zwischen DD-Befund, Disclosure, SPA und Police abgleichen; offene Tatsachen nicht vorschnell als bekannten Schaden behandeln.
5. **Materiality Auslesen vereinbaren:** bei Auslesen wird die Materiality-Schwelle der SPA-Garantien für Versicherungsansprueche ignoriert
6. **Synthetic Warranties:** für Garantien, die nicht im SPA stehen, aber Underwriter versichern wollen; separater Synthetic Warranty Schedule
7. **Bindungsbestaetigung einholen:** Underwriter Confirmation als W&I-Closing CP
8. **Anzeige nach dem Versicherungsfall:** Police-Frist, Adressat, Form, Mindestinhalt und maßgebliche Knowledge-Personen feststellen. Eine behauptete Obliegenheitsverletzung nach Paragraf 28 VVG anschließend nach Vertragsklausel, Verschulden, Kausalität und Belehrung prüfen.

## Entscheidungsbaum

- Buy-side W&I → Kaeufer zahlt Praemie → Verkaeuf er haftet nur noch bis Basket → ggf. Seller clean exit
- Bekanntes Risiko → Disclosure Letter → Ausschluss aus W&I-Deckung → Freistellung im SPA erwaegen
- KI-gestuetzte DD → Underwriter-Transparenz-Anforderung → Methodik dokumentieren; Human-in-the-loop-Protokoll
- Synthetic Warranties → Warranty nicht im SPA → nur durch spezifischen Schedule versicherbar

## Output-Template: W&I-Underwriting-Checkliste

**Adressat:** Versicherer / Deal-Team — Tonfall sachlich-strukturiert

```
W&I-UNDERWRITING-CHECKLISTE
Deal: [DEALNAME] — Datum: [DATUM]

UNTERLAGEN FUER UNDERWRITER
[ ] Red-Flag-Report (vollstaendig, datiert)
[ ] Disclosure Letter (mit Anlagen)
[ ] DD-Scope-Beschreibung (Methodik, Tools, Human-in-the-loop)
[ ] SPA-Entwurf, letzter Stand
[ ] Fragen/Antworten DD-Prozess (Q&A-Protokoll)

DECKUNGSAUSSCHLUESSE (BEKANNTE RISIKEN)
[ ] Umwelthaftung: [BESCHREIBUNG]
[ ] Steuerrisiko: [BESCHREIBUNG]
[ ] [WEITERE AUSSCHLUESSE]

STREICHUNG DER WESENTLICHKEITSSCHWELLE: [ ] Vereinbart [ ] Nicht vereinbart
SYNTHETIC WARRANTIES: [ ] Vorhanden (Schedule: [NAME]) [ ] Nicht vorhanden

PRÄMIE: ca. [X %] der Versicherungssumme
VERSICHERUNGSSUMME: [BETRAG EUR] entspricht [X %] des Kaufpreises
BINDUNGSBESTAETIGUNG FRIST: bis [DATUM]
```

## Rote Schwellen

- Unvollständiger DD-Report: Keine automatische Anfechtung unterstellen; konkrete Textformfrage, Kenntnis des Versicherungsnehmers, Zurechnung, Police-Wortlaut und Rechte nach den Paragrafen 19 bis 22 VVG prüfen.
- Nicht offengelegtes bekanntes Risiko: Vorvertragliche Anzeige nach den Paragrafen 19 bis 22 VVG und vertragliche Obliegenheit nach Paragraf 28 VVG auseinanderhalten; Arglist, Kausalität und Großrisikenregelung gesondert prüfen.
- Versäumte Anzeige- oder Mitwirkungsfrist: Deckungsverlust nicht pauschal behaupten; wirksame Obliegenheit, Fristbeginn, Verschulden, Kausalität, Belehrung und abweichende Police-Regelung prüfen.

## Standardausgabe

- W&I-Underwriting-Checkliste
- Deckungsausschluss-Tabelle
- Notification-Protokoll

## Übergabe an andere Skills

- DD-Findings → `grosskanzlei-corporate-ma-due-diligence-legal`
- Disclosure → `grosskanzlei-corporate-ma-disclosure-schedules`
- SPA → `grosskanzlei-corporate-ma-spa-apa-entwurf`

## Vorlagen

- assets/templates/wi-versicherung-checkliste.md
- assets/templates/wi-underwriting-disclosure.md
