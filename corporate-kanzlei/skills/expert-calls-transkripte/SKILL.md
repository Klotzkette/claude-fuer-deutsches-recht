---
name: expert-calls-transkripte
description: "Expert Calls und Transkript-Auswertung in M&A-Due-Diligence: DD-Team führt Experten-Interviews durch und will strukturierte Findings extrahieren. Normen: § 17 UWG (Geschäftsgeheimnis), DSGVO Art. 6, MAR Insider-Abgrenzung, Expert Network Compliance. Prüfraster: Insider-Risiko-Check, Wettbewerbsre..."
---

# Expert Calls und Transkripte

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Expert Calls und Transkripte

- **Corporate-Aufgabe (Expert Calls und Transkripte):** DD-Team führt Experten-Interviews durch und will strukturierte Findings extrahieren.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Expert Calls und Transkripte und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll und MAR-Insiderliste falls börsennotierte Gesellschaft betroffen ist.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

Arbeite mit diesen Variablen: `gesellschaft`, `rolle`, `organ`, `beschlussdatum`, `registerstand`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Corporate-Kontext fixieren.** Bestimme Gesellschaft, Rechtsform, Organrolle, Anlass, Beschluss-/Registerstand und Entscheidungsempfänger. Wenn Rolle oder Rechtsform fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste Dokumente mit Datum, Version, Quelle, Register-/Urkunden-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Organ- und Kompetenzebene trennen.** Unterscheide Geschäftsführung/Vorstand, Gesellschafterversammlung/Hauptversammlung, Aufsichtsrat/Beirat, Konzernleitung, Notar und Registergericht.
4. **Materiality-Schwelle setzen.** Fehlt eine Vorgabe, arbeite mit Ampel: Nichtigkeit/Unwirksamkeit, Anfechtungs-/Haftungsrisiko, Registerhindernis, Zustimmungserfordernis, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Corporate-Schritt: Zuständigkeit, Form, Frist, Mehrheit, Vollmacht, Registerfähigkeit, Haftung und Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn Registerauszug, BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, Rechtsfolge, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder eine Partner-/Organvorlage mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Beschlussentwurf, Board Paper, Registeranmeldung, SPA-Markup, CP-Tracker, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Prüfraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Corporate-Schritt gesellschaftsrechtlich wirksam, registerfähig, organschaftlich vertretbar und für die Mandatsseite praktisch umsetzbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird: Gesellschaft, Organmitglied, Gesellschafter, Investor, Käufer, Verkäufer oder Konzernmutter. Ist die Rolle unklar, darf kein parteilicher Beschluss-, Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Zuständigkeit, Form und Corporate Authority.** Bei Anteils-, Beschluss- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Mehrheit, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 bei börsennotierter Gesellschaft.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Aufsichtsrats- oder Beiratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Beschlussfähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Satzungszustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Registerhindernis? Beschlussmangel? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Haftungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 46 GmbHG Zustimmung erforderlich?` nur bejahen, wenn Satzung, Geschäftsordnung und Maßnahme geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Corporate-Kontext: nicht beschließen, nicht anmelden, nicht signieren, nicht closen oder nicht extern versenden, bevor Partner, Organ oder Spezialist freigegeben hat.

## Output-Module
- **Corporate-Vermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Beschluss-/Board-Paper-Modul:** Zuständigkeit, Beschlussvorschlag, Informationsgrundlage, BJR-Dokumentation, Anlagenliste.
- **Issue List:** Finding, Quelle, Risiko, Rechtsfolge, Register-/Vertragsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Organ, Notar, Registerteam, Steuerberater oder Gegenseite.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/corporate-kanzlei:corporate-kanzlei-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/corporate-kanzlei:corporate-kanzlei-datenraum-gap-clean-room` - wenn Informationslücken, Wettbewerberdaten oder Clean-Room-Grenzen geklärt werden müssen.
- `/corporate-kanzlei:corporate-kanzlei-due-diligence-legal` - wenn aus Unterlagen ein Corporate-/Legal-DD-Befund gebaut werden soll.
- `/corporate-kanzlei:corporate-kanzlei-qa-information-requests` - wenn Findings in Information Requests und Q&A übersetzt werden müssen.
- `/corporate-kanzlei:corporate-kanzlei-due-diligence-reporting` - wenn ein adressatengerechter DD-Report entstehen soll.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partner-, Organ- oder Mandantenentscheidung über Beschluss, Signing, Registeranmeldung oder Closing.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Registergericht, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht Corporate-Befund, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Expert Calls und Transkripte

## Triage — klaere vor Expert Call

1. Welches Ziel hat der Expert Call: Branchenverstaendnis, Wettbewerbs-Assessment, Management-Einschaetzung, technische Frage?
2. Experten-Status: Externer Branchenexperte, ehemaliger Mitarbeiter, oder aktueller Insider der Zielgesellschaft?
3. Insider-Risiko: Koennte der Experte Insiderinformationen offenbaren? → MAR-Compliance
4. Vertraulichkeit: Unter NDA? Expert-Network-Protokoll (z.B. Glenbrook/Guidepoint/GLG)?
5. Transkript-Weiterverwendung: Nur intern oder in DD-Report?
6. DSGVO: Personenbezogene Daten des Experten wie behandeln?

## Zentrale Normen

- **Art. 14, 15 MAR** — Insiderhandelsverbot; Marktmanipulation; Expert der Insiderinfos hat darf diese nicht weitergeben; Kaeufer darf keine Insiderinfos intentional bekommen
- **§ 17 UWG** — Geschäftsgeheimnis des Zielunternehmens; ehemaliger Mitarbeiter darf keine Geheimnisse offenbaren
- **Art. 6 I DSGVO** — Rechtsgrundlage für Aufnahme und Verarbeitung von Expert-Call-Gespraechen
- **§ 201 StGB** — Verletzung der Vertraulichkeit des Wortes; Aufnahme ohne Einwilligung verboten in Deutschland

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Expert-Call-Compliance-Protokoll

Vor dem Call:
1. Expert-NDA abschliessen (oder Expert-Network-Protokoll verwenden)
2. Expert auf Insider-Pflichten hinweisen: keine nicht-öffentlichen Informationen zur Zielgesellschaft
3. Einwilligung für Aufnahme/Transkription einholen (§ 201 StGB)
4. Vorbereitung: Fragen-Katalog; Themen-Grenzen definieren

Waehrend des Calls:
5. Erinnerung an Insider-Regelung zu Beginn
6. Bei Insider-Info-Verdacht: Call unterbrechen; Compliance-Konsultation
7. Keine Nennung konkreter Personen-Namen der Zielgesellschaft

Nach dem Call:
8. Transkript erstellen (mit KI-Tool: anonymisiert)
9. Insider-Check: Enthaelt Transkript potenziell Insider-Informationen? → Compliance
10. Findings extrahieren und in DD-Report einarbeiten

## Schritt-für-Schritt-Workflow

1. **Expert identifizieren** — via Expert-Network (GLG, Guidepoint, Glenbrook) oder eigenes Netzwerk
2. **Compliance-Vorpruefung** — aktuelle Insider-Status prüfen; ex-Mitarbeiter: § 17 UWG-Abgrenzung
3. **Call-Vorbereitung** — Fragenkatalog; Themen-Scope; Grenzen definieren
4. **NDA/Expert-Protokoll** — Einwilligung schriftlich; Aufnahme-Einwilligung
5. **Call durchfuehren** — strukturiert; Protokoll; bei Insider-Alarm: Unterbrechung
6. **Transkript auswerten** — Findings extrahieren; Risiken kennzeichnen
7. **Integration in DD** — Brancheneinschaetzung; Wettbewerber-Assessment; Management-Einschaetzung

## Output-Template Call-Transkript-Summary

```
EXPERT-CALL-SUMMARY
Transaktion: [DEAL-NAME]
Call-Datum: [DATUM], [DAUER]
Expert: [Funktion / Titel; kein Name wenn anonym]
Expert-Netzwerk: [GLG / Guidepoint / Direkt]
Interviewer: [NAME, KANZLEI/INVESTOR]
Einwilligung Aufnahme: [Ja / Nein → kein Transkript moeglich]

INSIDER-STATUS: [Kein Insider-Verdacht / Vorsicht: potenzielle Insider-Info bei Thema X]

KERN-FINDINGS:
1. [Thema]: [Erkenntnis in 2-3 Saetzen]
2. [Thema]: [Erkenntnis]
3. [Thema]: [Erkenntnis]

RELEVANZ FUER DD:
- Workstream: [Commercial DD / Branche / Management Assessment]
- Risikobewertung: [Bestaetigt Befund X / Neue Information Y / Widerspruch zu Datenraum]

INSIDER-COMPLIANCE-CHECK:
[ ] Keine Insiderinformation offenbart
[ ] Potenzielle Insiderinformation: [Beschreibung] → Compliance-Review am [Datum]
```

## Rote Schwellen

- Insider-Information im Call erhalten und nicht gemeldet → Art. 14 MAR; Strafbarkeit
- Aufnahme ohne Einwilligung → § 201 StGB; Verwertbarkeit fraglich
- § 17 UWG: Geschäftsgeheimnis der Zielgesellschaft weitergegeben → UWG-Klage; Schadensersatz
- Transkript in DD-Report ohne Anonymisierung → DSGVO-Risiko; Persoenlichkeitsrechtsverletzung

## Quellen

- Art. 14, 15 MAR; § 17 UWG; § 201 StGB; Art. 6 DSGVO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Ohly/Sosnitza UWG § 17; Assmann/Schneider/Muelbert WpHG Art. 14 MAR
