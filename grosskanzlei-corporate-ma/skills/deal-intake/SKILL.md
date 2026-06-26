---
name: deal-intake
description: "Nimmt ein neues M&A-Mandat strukturiert auf: Rolle, Deal-Typ, Parteien, Zielgesellschaft, Timing, Konflikte, Workstreams, Freigaben und erstes Partner-Memo."
---

# Deal-Intake

## Aktenstart statt Formularstart

Wenn zum Deal Intake bereits Unterlagen, ein Ordner, ein PDF-Bündel, E-Mails, Screenshots, Tabellen oder Entwürfe vorliegen, lies diese zuerst aus. Bilde eine Arbeitshypothese zu Beteiligten, Mandantenrolle, Transaktionsstruktur, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und nächstem sinnvollen Output. Frage nicht routinemäßig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Anker

- **Mandatsaufnahme und Konflikt:** Paragraf 43a BRAO, Paragraf 3 BORA, Paragraf 3a RVG, GwG-Sorgfaltspflichten und Vertraulichkeitsrahmen.
- **Corporate Authority:** Paragraf 15, 16, 40, 46 GmbHG; Paragraf 76, 93, 111 AktG; Registerlage, Vollmachtskette und Organbeschlüsse.
- **Regulatorische Dealbreaker:** Paragraf 35 bis 41 GWB, AWG/AWV, sektorspezifische Freigaben, MAR-Bezug bei kapitalmarktnahen Vorgängen.
- **Leitentscheidungen:** BGH, 21.04.1997 - II ZR 175/95 für entscheidungsreife Organunterlagen; BGH, 20.11.2018 - II ZR 12/17 für Listen- und Legitimationsfragen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Deal-Intake
- **Entscheidende Weiche:** Buy-side, Sell-side, Target, Management, Lender oder neutraler Koordinator; Phase vor IOI, NBO, BO, Signing, Closing oder Post-Closing.
- **Deal-Landkarte:** Parteien, Beteiligungskette, Zielgesellschaft, Transaktionsgegenstand, Preislogik, Freigaben, Datenraum, Signing-/Closing-Taktung, Spezialistenbedarf.
- **Arbeitsprodukt:** Liefere eine `Thema / Tatsache / Beleg / Risiko / Owner / nächster Schritt`-Matrix und auf Wunsch ein erstes Partner- oder Mandantenmemo.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Intake und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-matter-file`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Registerauszüge, Gesellschafterliste, Satzung, Geschäftsordnungen und Vollmachten.
- Organbeschlüsse, Zustimmungskataloge, Vollmachtsketten und Notartermine.
- Cap Table, Beteiligungskette, Umwandlungs- oder Carve-out-Plan.

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
- GmbHG Paragraf 15, 16, 40 und 46 für Anteilsübertragung, Gesellschafterliste und Beschlüsse.
- AktG Paragraf 76, 93, 111, 179a und 186 für Leitung, Business Judgment und Strukturmaßnahmen.
- HGB Paragraf 8 ff., 15 und Paragraf 161 ff. für Registerpublizität und Personengesellschaften.
- UmwG Paragraf 2, 123, 190 ff. für Verschmelzung, Spaltung und Formwechsel.

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
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-gesellschaftsrecht-register` - wenn Registerstand, Gesellschafterliste, Organstellung oder Vollmachtskette geprüft werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-handelsregisterabruf` - wenn Registerstand, Gesellschafterliste, Organstellung oder Vollmachtskette geprüft werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-transaktionsstruktur` - als fachlicher Anschluss-Skill.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-umwandlungsrecht` - wenn Verschmelzung, Spaltung, Formwechsel oder Carve-out gesellschaftsrechtlich strukturiert werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-board-paper-business-judgment` - wenn Organentscheidung und Business-Judgment-Dokumentation vorbereitet werden.

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

### Deal-Intake

## Arbeitsmodus

- Parteien, Zielgesellschaft, Deal-Typ, Jurisdiktionen, Zeitplan, Vertraulichkeit und erste rote Flaggen extrahieren.
- Konfliktcheck, Sanktionen, Insider-/Clean-Room-Fragen und Mandatsumfang anstoßen.
- Fehlende Kerninformationen als kurze IRL anlegen.
- Akte und Deal-Namen vorschlagen.

## Rote Schwellen

- Keine Konfliktprüfung.
- Insiderinformation oder Marktgeruecht in offenem Kanal.
- Datenraumzugang ohne NDA oder Need-to-know.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/deal-intake-sheet.md
- assets/templates/matter-opening-checklist.md

## Triage — klaere beim Erstkontakt

1. Wer sind Verkaeufer und Kaeufer — natuerliche Person, GmbH, AG, ausl. Gesellschaft?
2. Was ist das Kaufobjekt — GmbH-Anteile, AG-Aktien, Asset-Portfolio, Immobilien, IP?
3. Welcher Transaktionsstatus — erster Kontakt, NDA, Term Sheet, LOI, fortgeschrittene Verhandlung?
4. Gibt es Insiderinformationen — boersennotierte Zielgesellschaft → MAR-Pflichten sofort prüfen
5. Welches Budget und welcher Zeitplan sind angegeben?

## Zentrale Rechtsgrundlagen

- Paragraf 43a Abs. 4 BRAO — Interessenkonfliktpruefung vor Mandatsannahme; Pflicht zur Conflicts-Prüfung
- Paragraf 10, 11 GwG — Sorgfaltspflichten bei Mandatsannahme; Identifizierung aller Parteien und wirtschaftlich Berechtigter
- Art. 7, 17 MAR — bei boersennotierter Zielgesellschaft: Insiderinformation und Ad-hoc-Pflicht sofort beachten
- Paragraf 17-18 GeschGehG — Vertraulichkeitspflicht; NDA muss vor Informationsaustausch vorliegen
- Paragraf 49b BRAO — Honorarvereinbarung: bei M&A-Mandaten auch Erfolgshonorar nach RVG möglich; schriftliche Vereinbarung empfohlen

## Aktuelle Rechtsprechung

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Schritt-für-Schritt-Workflow

1. **Parteien extrahieren:** Verkaeufer, Kaeufer, Zielgesellschaft, Intermediar, Finanzier — volle Bezeichnung, Sitz, HR-Nummer
2. **Conflicts-Check ausfuehren:** Paragraf 43a BRAO; GwG-Screening (Sanktionen, PEP)
3. **Mandatsinformation erfassen:** Deal-Typ, Wert, Zeitplan, Vertraulichkeitsstufe, Partner-Zuordnung
4. **NDA-Status prüfen:** NDA unterzeichnet? Falls nicht: Einleitung vor weiterem Informationsaustausch
5. **Insiderinformations-Check:** boersennotiert → MAR-Insiderliste einleiten; Ad-hoc-Prüfung
6. **Deal-Karte erstellen:** Phase, Rolle, Owner, Frist, Risiko, naechste Aktion, Freigabegrad
7. **Aktenanlage und Mandatsvereinbarung:** Aktenzeichen vergeben; Honorarvereinbarung (Paragraf 49b BRAO)

## Rote Schwellen

- Keine Conflicts-Prüfung vor Mandatsannahme: Paragraf 43a BRAO, Haftung
- GwG-Sorgfaltspflichten verletzt: Bussgeld
- Insiderinformation ohne MAR-Protokoll: aufsichtsrechtliche Konsequenzen
