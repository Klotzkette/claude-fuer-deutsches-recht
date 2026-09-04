---
name: umwandlungsrecht
description: "Prüft Verschmelzung, Spaltung, Ausgliederung und Formwechsel nach dem UmwG, ordnet Berichte, Beschlüsse, Schutzrechte und Registervollzug und erstellt einen belastbaren Vollzugsplan."
---

# Umwandlungsrecht

## Fachlicher Anker

- **Normenradar:** Paragraf 15, 16, 40, 43, 46 GmbHG; Paragraf 76, 93, 111 AktG; HGB-, UmwG-, GWB- und AWV-Bezug nur, wenn der konkrete Vorgang ihn trägt.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Umwandlungsrecht
- **Prüfachse:** Ordne den konkreten Auftrag nach Gesellschaftsform, Dokument, Entscheidungsträger, Form, Frist, Beleg und Rechtsfolge; Spezialnormen nur nennen, wenn sie den Fall tragen.
- **Entscheidende Weiche:** Trenne Sachverhalt, Zuständigkeit, Zustimmung, Haftung, Vollzug und taktischen nächsten Schritt.
- **Arbeitsprodukt:** Liefere eine verwertbare Matrix mit `Tatsache / Norm / Beleg / Wertung / Gegenargument / nächster Schritt` und bei Bedarf einen ausformulierten Textbaustein.

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

### Umwandlungsrecht

## Triage — klaere vor Strukturentscheidung

1. Welche Umwandlungsart ist geplant — Verschmelzung (Paragrafen 2 bis 38 UmwG), Spaltung oder Ausgliederung (Paragrafen 123 bis 173 UmwG) oder Formwechsel (Paragrafen 190 bis 304 UmwG)?
2. Welche Rechtsformen sind beteiligt — GmbH, AG, KGaA, GmbH & Co. KG, SE, Genossenschaft?
3. Welche Schlussbilanz- und Rückwirkungsfrist gilt? Bei der Verschmelzung darf der Bilanzstichtag nach Paragraf 17 Absatz 2 UmwG höchstens acht Monate vor der Registeranmeldung liegen; Paragraf 2 Absatz 1 UmwStG knüpft den steuerlichen Übertragungsstichtag daran. Für Sacheinlagen gilt die Achtmonatsgrenze des Paragrafen 20 Absatz 6 UmwStG.
4. Gibt es eine Vorwegausgliederung als Deal-Preparation — ist der Carve-out-Zeitplan mit der Signing-Deadline vereinbar?
5. Welche Gläubigerschutzmaßnahmen sind erforderlich — Paragraf 22 UmwG Sicherheitsleistung bei Verschmelzung?
6. Welche Arbeitnehmer- und Betriebsratsrechte sind zu beachten — bei Verschmelzungen Paragraf 35a UmwG, bei Spaltungen die Verweisung in Paragraf 125 UmwG, jeweils zusammen mit Paragraf 613a BGB?

## Zentrale Rechtsgrundlagen

- Paragrafen 2 bis 38 UmwG — Verschmelzung: Vertrag, Bericht, Prüfung, Beschluss, Anmeldung und Gesamtrechtsnachfolge
- Paragrafen 123 bis 173 UmwG — Aufspaltung, Abspaltung und Ausgliederung; Vertrag oder Plan, Beschluss, Anmeldung und partielle Gesamtrechtsnachfolge
- Paragrafen 135 bis 137 UmwG — Spaltung zur Neugründung; bei der Ausgliederung zur Neugründung entfällt nach Paragraf 135 Absatz 3 UmwG der Spaltungsbericht
- Paragrafen 190 bis 213 UmwG — Formwechsel: keine Vermögensübertragung, sondern Identitätswahrung des Rechtsträgers
- Paragraf 22 UmwG — Gläubigerschutz: auf Verlangen Sicherheitsleistung für ungesicherte Gläubiger
- Spruchverfahrensgesetz zusammen mit der für die konkrete Umwandlungsart einschlägigen UmwG-Vorschrift — gerichtliche Überprüfung von Zuzahlung, Barabfindung oder Umtauschverhältnis; keine pauschale Verweisung auf Paragraf 325 UmwG
- Paragraf 35a UmwG bei Verschmelzungen und Paragraf 125 UmwG bei Spaltungen, jeweils zusammen mit Paragraf 613a BGB — Zuordnung und Übergang von Arbeitsverhältnissen
- Paragraf 17 Absatz 2 UmwG, Paragraf 2 Absatz 1 und Paragraf 20 Absatz 6 UmwStG — Schlussbilanz und steuerlicher Übertragungsstichtag; regulär höchstens acht Monate Rückbezug

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Schritt-für-Schritt-Workflow

1. **Umwandlungstyp bestimmen:** Verschmelzung, Abspaltung, Ausgliederung, Formwechsel — massgeblich für Form und Gremien
2. **Zeitplan aufstellen:** Notartermin, Beschlussfassung und Registeranmeldung rückwärts planen; die Achtmonatsgrenze für Schlussbilanz und steuerlichen Rückbezug nach Paragraf 17 Absatz 2 UmwG sowie Paragraf 2 Absatz 1 und Paragraf 20 Absatz 6 UmwStG als harte Datumsprüfung führen
3. **Beschlüsse vorbereiten:** Für jede Umwandlungsart Rechtsform, Zustimmungserfordernisse, Mehrheit und Form gesondert prüfen. Bei der Verschmelzung einer GmbH verlangt Paragraf 50 Absatz 1 UmwG grundsätzlich mindestens drei Viertel der abgegebenen Stimmen; strengere gesellschaftsvertragliche Vorgaben bleiben zu beachten.
4. **Berichtserfordernis bestimmen:** Verschmelzungs- oder Spaltungsbericht nach Paragraf 8 beziehungsweise Paragraf 127 UmwG vorbereiten, sofern er nicht aufgrund einer gesetzlichen Ausnahme oder eines wirksamen Verzichts entfällt. Bei der Ausgliederung zur Neugründung ist nach Paragraf 135 Absatz 3 UmwG kein Spaltungsbericht erforderlich. Eine Prüfung nur einplanen, wenn sie für die konkrete Umwandlungsart erforderlich ist und nicht wirksam entfallen kann.
5. **Gläubigerschutz sicherstellen:** Paragraf 22 UmwG — Gläubiger können Sicherheitsleistung verlangen; Ankuendigung und Frist beachten
6. **Arbeitnehmerinformation:** Paragraf 35a UmwG bei Verschmelzungen und Paragraf 125 UmwG bei Spaltungen zusammen mit Paragraf 613a BGB prüfen; betroffene Arbeitnehmer, Zuordnung, Unterrichtung und Beteiligung des Betriebsrats dokumentieren
7. **Anmeldung zum HR:** notariell beglaubigte Anmeldung zum Handelsregister; Eintragung konstitutiv
8. **Steuerliche Rückwirkung sichern:** Bilanzstichtag, Registeranmeldung, Einbringungsvertrag und Übergang des wirtschaftlichen Eigentums in einer Datumsachse erfassen; reguläre Achtmonatsgrenze für jeden einschlägigen Tatbestand gesondert berechnen

## Entscheidungsbaum

- Verschmelzung → Gesamtrechtsnachfolge → alle Verträge gehen über → Change-of-Control-Klauseln prüfen
- Ausgliederung → partielle Gesamtrechtsnachfolge nach Paragraf 131 Absatz 1 Nummer 1 UmwG → Vermögenszuordnung im Vertrag präzisieren; nicht übertragbare Erlaubnisse und vertragliche Zustimmungsvorbehalte gesondert prüfen
- Formwechsel → Identitaetswahrung → kein Betriebsuebergang, aber Abfindungsangebot nach Paragraf 207 UmwG
- Gewünschter Rückwirkungsstichtag → mehr als acht Monate vor dem maßgeblichen Anmelde-, Vertrags- oder Übergangszeitpunkt? → Rückbezug auf diesen Stichtag unzulässig; Stichtag und Zeitplan anpassen, Buchwertvoraussetzungen davon getrennt prüfen

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
Glaeubigerschutz Paragraf 22 UmwG | [NAME] | [DATUM] | [ ]
Arbeitnehmer-Info Paragraf 613a BGB | [NAME] | [DATUM] | [ ]
HR-Anmeldung | Notar [NAME] | [DATUM] | [ ]
Steuerl. Schlusspunkt UmwStG | Steuer [NAME] | [DATUM] | [ ]
```

## Rote Schwellen

- Beschluss-/Berichtserfordernis offen: Eintragung durch Registergericht abgelehnt
- Steuerliche Rueckwirkung oder Sperrfrist nicht geprueft: stille Reserven werden aufgedeckt; Steuerbelastung
- Spruchverfahrensrisiko nicht einkalkuliert: Prozesskosten und Nachzahlungen können erheblich sein

## Standardausgabe

- Umwandlungs-Checkliste mit Zeitplan, Owner und Status
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe
- Belegkette: Normen, Beschlüsse, Registerschritte

## Übergabe an andere Skills

- Steuer → `grosskanzlei-corporate-ma-umwandlungssteuerrecht`
- Gesellschaftsrecht/Register → `grosskanzlei-corporate-ma-gesellschaftsrecht-register`
- Transaktionsstruktur → `grosskanzlei-corporate-ma-transaktionsstruktur`

## Vorlagen

- assets/templates/umwandlungsrecht-checkliste.md
- assets/templates/verschmelzung-spaltung-formwechsel-plan.md
