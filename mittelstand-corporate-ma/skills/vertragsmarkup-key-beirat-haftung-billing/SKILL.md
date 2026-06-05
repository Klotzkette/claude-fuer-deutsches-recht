---
name: vertragsmarkup-key-beirat-haftung-billing
description: "Vertragsmarkup KEY Beirat Haftung Billing: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertragsmarkup KEY Beirat Haftung Billing

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Vertragsmarkup KEY Beirat Haftung Billing** im Plugin Mittelstand Corporate Ma. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mittelstand-corporate-ma-vertragsmarkup-key-issues` | Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschlaege nach Parteiperspektive. |
| `beirat-haftung` | GmbH-Beirat im Plugin mittelstand-corporate-ma: Beirat Haftung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `mittelstand-corporate-ma-billing-narratives` | Kanzlei erstellt Rechnung für M&A-Mandat und braucht praezise zeitgerechte Leistungsbeschreibungen: Time Narratives Phasenbudgets Workstream-Rechnungen Cap/Success-Fee-Berechnung. Normen RVG §§ 1 ff. BRAO § 49b AO-Steuerrecht. Prüfraster Workstream-Zeiterfassung Phasenzuordnung Korrektur Mandantsfreigabe. Output Narratives-Dokument Workstream-Abrechnung Rechnungsentwurf. Abgrenzung zu mittelstand-ma-erechnung-gobd (GoBD/XRechnung-Format). |
| `mittelstand-corporate-ma-tabellenreview-3d-datenraum` | 3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft. |

## Arbeitsweg

Im Plugin Mittelstand Corporate Ma gilt für **Vertragsmarkup KEY Beirat Haftung Billing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mittelstand-corporate-ma-vertragsmarkup-key-issues`

**Fokus:** Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschlaege nach Parteiperspektive.

# Markup und Key Issues

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Markup und Key Issues` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Markup und Key Issues
- **Spezialgegenstand:** Markup und Key Issues wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck
Dieser Skill führt ein Mittelstands-Corporate/M&A-Mandat durch den Arbeitsbereich **SPA/APA, Disclosure, Signing, Closing und Post-Closing-Mechanik**. Er macht aus unvollständigen Unternehmerunterlagen einen belastbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und übersetzt juristische Risiken in einen nächsten praktischen Schritt. Adressaten sind Partner, Counsel, Associates, Steuerberater, Inhouse-Verantwortliche und Unternehmer in mittelständischen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Markup und Key Issues und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:mittelstand-corporate-ma-matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Gesellschafter-/Beiratsfreigaben.
- Disclosure Letter, Knowledge-Definition, W&I- oder Verkäufergarantie-Struktur.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Mittelstandsrealität abbilden.** Prüfe, ob Gesellschafter, Geschäftsführung, Familie, Hausbank, Steuerberater, Notar oder Beirat faktisch mitentscheiden. Dokumentiere informelle Absprachen als Risiko, nicht als Rechtsgrundlage.
4. **Materiality-Schwelle setzen.** Fehlt eine vertragliche Schwelle, arbeite mit pragmatischer Ampel: Dealbreaker, Kaufpreis-/Freistellungsfolge, Closing-Bedingung, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein kurzes Partner-/Mandantenmemo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Mandantenmail, Notarcheckliste oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite wirtschaftlich sinnvoll steuerbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Beirats- oder Gesellschafterentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Vermieterzustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Kündigungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Mittelstand regelmäßig: nicht unterschreiben, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner, Steuerteam oder Spezialist freigegeben hat.

## Output-Module
- **Mandantenvermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Finding, Quelle, Risiko, Vertragsfolge, Kaufpreis-/Freistellungsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Gegenseite, Steuerberater, Notar oder Datenraum-Team.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Mandantenmail.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-spa-apa-entwurf` - wenn der Befund in SPA/APA-Entwurf oder Klausellogik einfließen soll.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-closing-bible-archiv` - wenn executed documents, Registerbelege und Closing Bible gesichert werden müssen.

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

# Markup und Key Issues

## Zweck

Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive.

## Arbeitsmodus

- Änderungen nach wirtschaftlicher Relevanz und Rechtsrisiko clustern.
- Position Buy-side/Sell-side transparent halten.
- Rote Linien, Konzessionen und Verhandlungsstrategie trennen.
- Gegenentwurf nur als Vorschlag mit Review-Status ausgeben.

## Rote Schwellen

- Gegenseitenmarkup falsch gelesen.
- Marktüblichkeit ohne eigene Präzedenz- oder Quellenbasis behauptet.
- Risk shift ohne Mandantenentscheidung.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/key-issues-list.md
- assets/templates/markup-response-sheet.md

## Triage

1. Welches Dokument wird markiert — SPA, APA, NDA, Shareholders Agreement, Process Letter?
2. Welche Parteiperspektive — Kaeufer (Buy-side) oder Verkaeufer (Sell-side)?
3. Welche Klauseln sind vorrangig — Garantien, Haftungsbeschraenkungen (Cap, Basket), MAC, Earn-Out, CPs?
4. Liegt ein aktueller Term Sheet vor, auf den sich das Markup stuetzt?

## Zentrale Rechtsgrundlagen

- §§ 305-310 BGB — AGB-Inhaltskontrolle: Haftungsausschluesse und ungewoehnliche Klauseln koennen unwirksam sein
- §§ 443, 311 BGB — Garantievereinbarung: Formulierung entscheidet ueber Haftungsumfang; "Best Knowledge" vs. "actual knowledge" hat unterschiedliche Rechtsfolgen
- §§ 195, 199 BGB — Verjaehrungsfristen: vertragliche Abkuerzung auf 18-24 Monate ueblich; laengere Fristen bei Tax und Title

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Key Issues List erstellen:** alle nicht geklarten Punkte aus Term Sheet extrahieren; Prioritaet festlegen
2. **Markup nach Parteiperspektive erstellen:** Buy-side: staerkere Garantien, laengere Fristen, hoehere Caps; Sell-side: Beschraenkungen, kurze Fristen, Caps
3. **Redlines dokumentieren:** je Klausel: aktuelle Fassung, Markup, Begruendung, Kompromissvorschlag
4. **Human-in-the-loop:** alle Deal-Breaker-Markups → Partner-Freigabe vor Uebersendung

## Rote Schwellen

- Arglist-Ausnahme nicht geklauselt: Cap ggf. unwirksam fuer arglistige Taeusching
- Verjaehrung nicht abgegrenzt: Tax Warranties koennen unter kurzfristiger Gewaehrleistung fallen

## 2. `beirat-haftung`

**Fokus:** GmbH-Beirat im Plugin mittelstand-corporate-ma: Beirat Haftung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Beirat Haftung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beirat Haftung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Beirat Haftung
- **Spezialgegenstand:** Beirat Haftung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist GmbH-Beiratsarchitekt. Du übersetzt die große Gestaltungsfreiheit in Satzung, Geschäftsordnung, Zustimmungsvorbehalte, Informationsrechte, Haftungsbegrenzung und konfliktfeste Beschlusslogik.

Dieser Skill ist für **Beirat Haftung** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Beiratshaftung nach Funktion, Organähnlichkeit, übernommenen Aufgaben und faktischer Einflussnahme prüfen.
- Interessenkonflikte offenlegen, Stimmverbote/Enthaltungen regeln und Protokollspur schaffen.
- Vergütung und D&O/Haftungsfreistellung nur mit transparenter Grundlage und Gesellschafterbeschluss.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GmbHG §§ 37, 43, 46, 47, 48, 52, 53; BGB §§ 133, 157, 241 Abs. 2, 242; MitbestG/DrittelbG bei Abgrenzung zum obligatorischen Aufsichtsrat; Satzung, Geschäftsordnung, Gesellschafterbeschluss; GeschGehG/DSGVO bei Vertraulichkeit und Datenzugriff.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Beiratsmatrix mit Satzungsgrundlage, Kompetenz, Grenze, Risiko und Formulierung.
- Musterklausel, Beschluss- oder Protokollbaustein.
- Geschäftsordnungs-Redline mit Eskalationsmechanik.
- Risikovermerk für Gesellschafter, Geschäftsführung und Beiratsmitglieder.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 3. `mittelstand-corporate-ma-billing-narratives`

**Fokus:** Kanzlei erstellt Rechnung für M&A-Mandat und braucht praezise zeitgerechte Leistungsbeschreibungen: Time Narratives Phasenbudgets Workstream-Rechnungen Cap/Success-Fee-Berechnung. Normen RVG §§ 1 ff. BRAO § 49b AO-Steuerrecht. Prüfraster Workstream-Zeiterfassung Phasenzuordnung Korrektur Mandantsfreigabe. Output Narratives-Dokument Workstream-Abrechnung Rechnungsentwurf. Abgrenzung zu mittelstand-ma-erechnung-gobd (GoBD/XRechnung-Format).

# Mittelstandsmandat Billing Narratives

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mittelstandsmandat Billing Narratives` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Mittelstandsmandat Billing Narratives
- **Spezialgegenstand:** Mittelstandsmandat Billing Narratives wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck
Dieser Skill führt ein Mittelstands-Corporate/M&A-Mandat durch den Arbeitsbereich **Mandatsaufnahme, Deal-PMO, Unternehmerkommunikation, Staffing und Budgetsteuerung**. Er macht aus unvollständigen Unternehmerunterlagen einen belastbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und übersetzt juristische Risiken in einen nächsten praktischen Schritt. Adressaten sind Partner, Counsel, Associates, Steuerberater, Inhouse-Verantwortliche und Unternehmer in mittelständischen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Mittelstandsmandat Billing Narratives und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:mittelstand-corporate-ma-matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- Mandatsanfrage, Konfliktcheck, Rollenmatrix, Budget und Deal-Timeline.
- Kommunikationskanäle, Vertraulichkeitsstufen, Review-Gates und Eskalationspfade.
- Vorlagen für Deal-Karte, Workstream-Plan, Unternehmer-Statusbericht und Billing Narrative.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Mittelstandsrealität abbilden.** Prüfe, ob Gesellschafter, Geschäftsführung, Familie, Hausbank, Steuerberater, Notar oder Beirat faktisch mitentscheiden. Dokumentiere informelle Absprachen als Risiko, nicht als Rechtsgrundlage.
4. **Materiality-Schwelle setzen.** Fehlt eine vertragliche Schwelle, arbeite mit pragmatischer Ampel: Dealbreaker, Kaufpreis-/Freistellungsfolge, Closing-Bedingung, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein kurzes Partner-/Mandantenmemo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Mandantenmail, Notarcheckliste oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite wirtschaftlich sinnvoll steuerbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BRAO § 43a, BORA § 3 und BRAO § 49b für Verschwiegenheit, Konflikt und Honorar.
- GwG §§ 10 ff. für Mandatsannahme und wirtschaftlich Berechtigte.
- DSGVO Art. 5, 6, 25 und 32 für Datenminimierung, Rollen und Sicherheit.
- BGB §§ 611a, 675 und 280 für Beratungs- und Haftungsrahmen.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Beirats- oder Gesellschafterentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Vermieterzustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Kündigungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Mittelstand regelmäßig: nicht unterschreiben, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner, Steuerteam oder Spezialist freigegeben hat.

## Output-Module
- **Mandantenvermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Finding, Quelle, Risiko, Vertragsfolge, Kaufpreis-/Freistellungsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Gegenseite, Steuerberater, Notar oder Datenraum-Team.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Mandantenmail.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-deal-intake` - wenn das Mandatsprofil, Rollen, Fristen und Budget sauber aufgenommen werden müssen.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-matter-file` - wenn Deal-Karte, Workstreams, Fristen und Dokumentenlog in eine laufende Akte geschrieben werden sollen.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` - wenn mehrere Workstreams konkurrieren und der nächste Primärpfad neu bestimmt werden muss.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-steps-plan-pmo` - wenn Termine, CPs, Freigaben und Owner in einen belastbaren Transaktionsplan müssen.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.

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

# Mittelstandsmandat Billing Narratives

## Zweck

Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. Für GoBD, XRechnung und ZUGFeRD liegt der freistehende interne `mittelstand-ma-erechnung-gobd` im selben Plugin.

## Arbeitsmodus

- Tätigkeiten nach Phase, Workstream und Deliverable erfassen.
- Narratives knapp, mandantentauglich und prüfbar formulieren.
- Budgetabweichungen und Scope Creep markieren.
- WIP, Cap, Success Fee, Auslagen, Rabatte und Steuerlogik als eigene Prüfpunkte führen.
- Bei Rechnungsreife an `mittelstand-ma-erechnung-gobd` übergeben.

## Rote Schwellen

- Narrative enthält Mandatsgeheimnis unnötig detailliert.
- Budgetwarnung fehlt.
- Leistung ohne Akte/Workstream.
- Rechnungsnummer, Umsatzsteuerlogik oder E-Rechnungsformat unklar.

## Standardausgabe

- Billing Narrative Ledger.
- Budgetstatus nach Workstream.
- Rechnungsreife-Ampel.
- Übergabe an E-Rechnung/GoBD mit Belegkette.

## Vorlagen

- assets/templates/billing-narrative-ledger.md
- assets/templates/erechnung-gobd-billing.md

## Rechtliche Einbettung und Praxiswissen

### Zentrale Normen
- § 43a BRAO — anwaltliche Pflichten: vollstaendige Mandatsfuehrung; Sorgfaltspflichten gelten auch fuer automatisierte Prozesse
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung; gilt auch fuer Organisation und Monitoring
- § 49b BRAO — Honorarvereinbarung: Abrechnungsmodalitaeten muessen transparent und schriftlich vereinbart sein
- §§ 93, 116 AktG; § 43 GmbHG — Business Judgment Rule: Entscheidung auf ausreichender Informationsgrundlage; Dokumentationspflicht

### Leitsaetze
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen automatisierten Ausgaben
- Dokumentation: Datum, Methodik, Human-Check-Protokoll

## 4. `mittelstand-corporate-ma-tabellenreview-3d-datenraum`

**Fokus:** 3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft.

# 3D-Tabellenreview im Datenraum

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `3D-Tabellenreview im Datenraum` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: 3D-Tabellenreview im Datenraum
- **Spezialgegenstand:** 3D-Tabellenreview im Datenraum wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck
Dieser Skill führt ein Mittelstands-Corporate/M&A-Mandat durch den Arbeitsbereich **Datenraum, Legal Due Diligence und pragmatische Information-Request-Steuerung**. Er macht aus unvollständigen Unternehmerunterlagen einen belastbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und übersetzt juristische Risiken in einen nächsten praktischen Schritt. Adressaten sind Partner, Counsel, Associates, Steuerberater, Inhouse-Verantwortliche und Unternehmer in mittelständischen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier 3D-Tabellenreview im Datenraum und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:mittelstand-corporate-ma-matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll und MAR-Insiderliste falls Public-M&A-Bezug.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Mittelstandsrealität abbilden.** Prüfe, ob Gesellschafter, Geschäftsführung, Familie, Hausbank, Steuerberater, Notar oder Beirat faktisch mitentscheiden. Dokumentiere informelle Absprachen als Risiko, nicht als Rechtsgrundlage.
4. **Materiality-Schwelle setzen.** Fehlt eine vertragliche Schwelle, arbeite mit pragmatischer Ampel: Dealbreaker, Kaufpreis-/Freistellungsfolge, Closing-Bedingung, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein kurzes Partner-/Mandantenmemo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Mandantenmail, Notarcheckliste oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite wirtschaftlich sinnvoll steuerbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 bei börsennotierter Zielgesellschaft.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Beirats- oder Gesellschafterentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Vermieterzustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Kündigungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Mittelstand regelmäßig: nicht unterschreiben, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner, Steuerteam oder Spezialist freigegeben hat.

## Output-Module
- **Mandantenvermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Finding, Quelle, Risiko, Vertragsfolge, Kaufpreis-/Freistellungsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Gegenseite, Steuerberater, Notar oder Datenraum-Team.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Mandantenmail.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-datenraum-gap-clean-room` - wenn Informationslücken, Wettbewerberdaten oder Clean-Room-Grenzen geklärt werden müssen.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-due-diligence-legal` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-qa-information-requests` - wenn Findings in Information Requests und Seller-Q&A übersetzt werden müssen.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-due-diligence-reporting` - wenn ein adressatengerechter DD-Report entstehen soll.

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

# 3D-Tabellenreview im Datenraum

## Zweck

Dieser Skill bleibt als M&A-Datenraum-Variante erhalten und nutzt ausschließlich interne Vorlagen dieses Plugins. Für den generischen freistehenden Review-Würfel steht zusätzlich `grosskanzlei-ma-tabellenreview` bereit.

## Arbeitsmodus

- Spaltenprompts für Datenpunkte formulieren.
- Zeilen als Dokumente oder Vertragscluster definieren.
- Blätter für Legal, Tax, Finance, ESG, Regulatory und PMI anlegen.
- Kreuzblatt-Widersprüche, fehlende Anlagen und Belegketten ausgeben.
- Ergebnisse in Q&A, Red-Flag-Report, Disclosure Schedules und SPA Issues überführen.

## Rote Schwellen

- Keine Belegkette.
- Formel- oder CSV-Export nicht nachvollziehbar.
- Materiality-Schwellen uneinheitlich.
- Clean-Room-Daten werden mit offenem Datenraum vermischt.

## Standardausgabe

- Review-Setup mit Zeilen, Spalten, Blättern und Materiality.
- Review Grid mit Belegstelle, Risiko, Owner und Follow-up.
- Liste der Widersprüche und fehlenden Dokumente.
- Übergabe an `grosskanzlei-ma-tabellenreview` bei großen Tabellenläufen.

## Vorlagen

- assets/templates/tabellenreview-3d-ma-setup.md
- assets/templates/tabellenreview-workbook.md
- assets/templates/tabellenreview-column-prompts.md
- assets/templates/tabellenreview-row-prompts.md
- assets/templates/data-quality-gate.md

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Pflichten: Sorgfalt, Vollstaendigkeit, Unabhaengigkeit
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung
- § 17 GeschGehG — Schutz von Geschaeftsgeheimnissen; gilt fuer alle Mandatsinhalte
- Art. 17 MAR — bei boersennotierten Zielobjekten: Ad-hoc-Pflicht und Vertraulichkeit

### Leitsaetze aus der Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior
