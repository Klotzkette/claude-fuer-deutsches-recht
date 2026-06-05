---
name: simulation-bidder-steps-plan
description: "Simulation Bidder Steps Plan: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Simulation Bidder Steps Plan

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Simulation Bidder Steps Plan** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-simulation-bidder-process` | Auktionsprozess und Bieter-Perspektive in M&A-Transaktionen simulieren: Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor. Normen: SPA, WpueG (Public M&A), Marktstandard M&A-Auktion. Prüfraster: Process Letter, Bieteranforderungen, NBO-Vergleich, Final Bid Instructions, Exklusivitaet. Output Process-Letter-Entwurf, Bieter-Vergleichsmatrix, NBO-Template. Abgrenzung: SPA-Entwurf siehe spa-apa-entwurf; Public M&A siehe public-ma-kapitalmarkt-mar. |
| `corporate-kanzlei-steps-plan-pmo` | Steps Plan und Transaktions-PMO für M&A-Mandate erstellen: Deal-Team benoetigt Gesamtprojektplan mit Workstream-Koordination, CP-Tracking und Status-Reporting. Normen: SPA Closing Conditions, § 158 BGB. Prüfraster: Workstream-Matrix (Legal, Tax, Financial, Regulatory, Commercial), Zeitplan, CP-Tracker, Weekly-Status-Template. Output Steps-Plan, Workstream-Matrix, CP-Tracker, Weekly-Status-Report. Abgrenzung: Monitoring einzelner Fristen siehe automation-monitoring; Signing-Closing siehe signing-closing-conditions. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Simulation Bidder Steps Plan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-simulation-bidder-process`

**Fokus:** Auktionsprozess und Bieter-Perspektive in M&A-Transaktionen simulieren: Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor. Normen: SPA, WpueG (Public M&A), Marktstandard M&A-Auktion. Prüfraster: Process Letter, Bieteranforderungen, NBO-Vergleich, Final Bid Instructions, Exklusivitaet. Output Process-Letter-Entwurf, Bieter-Vergleichsmatrix, NBO-Template. Abgrenzung: SPA-Entwurf siehe spa-apa-entwurf; Public M&A siehe public-ma-kapitalmarkt-mar.

# Simulation Bieter-Prozess

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Simulation Bieter-Prozess` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Simulation Bieter-Prozess

- **Corporate-Aufgabe (Simulation Bieter-Prozess):** Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Simulation Bieter-Prozess und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Gesellschafter-/Organfreigaben.
- Disclosure Letter, Knowledge-Definition, W&I- oder Garantie-Struktur.

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

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Corporate-Schritt gesellschaftsrechtlich wirksam, registerfähig, organschaftlich vertretbar und für die Mandatsseite praktisch umsetzbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird: Gesellschaft, Organmitglied, Gesellschafter, Investor, Käufer, Verkäufer oder Konzernmutter. Ist die Rolle unklar, darf kein parteilicher Beschluss-, Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Zuständigkeit, Form und Corporate Authority.** Bei Anteils-, Beschluss- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Mehrheit, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

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
- `/corporate-kanzlei:corporate-kanzlei-spa-apa-entwurf` - wenn der Befund in SPA/APA-Entwurf oder Klausellogik einfließen soll.
- `/corporate-kanzlei:corporate-kanzlei-vertragsmarkup-key-issues` - wenn Markup-Abweichungen in Key Issues und Verhandlungslinien übersetzt werden müssen.
- `/corporate-kanzlei:corporate-kanzlei-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/corporate-kanzlei:corporate-kanzlei-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/corporate-kanzlei:corporate-kanzlei-closing-bible-archiv` - wenn executed documents, Registerbelege und Closing Bible gesichert werden müssen.

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

# Simulation Bieter-Prozess

## Triage — klaere vor Simulation

1. Buy-Side (Kaeufer) oder Sell-Side (Verkaefer/Investmentbank)?
2. Auktionsprozess: breiter Prozess (5+ Bieter) oder bilateraler Deal?
3. Phase: Process Letter, Indicative Offer, Final Bid, Exklusivitaet?
4. Asset-Klasse: Unternehmensverkauf, Immobilien-Portfolio, Distressed-Sale?
5. Zeitplan: Wie viele Wochen bis Final Bid?
6. Stimmrecht-/Kontrollanalyse: Gibt es Vorabstimmungserfordernisse bei Gesellschaftern?

## Zentrale Normen

- **§§ 154, 155 BGB** — Einigung ueber alle wesentlichen Punkte; Letter of Intent als Vorvertrag-Pruefung
- **§ 311 II BGB** — vorvertragliche Schutzpflichten; Exklusivitaet; culpa in contrahendo
- **§ 241 II BGB** — Ruecksichtnahmepflicht; bei laufenden Verhandlungen schuetzwuerdiges Vertrauen
- **§§ 307, 305 BGB** — AGB-Kontrolle; Process-Dokumente koennen AGB-Charakter haben
- **Art. 18 MAR** — bei borsennotierten Zielgesellschaften: Insider-Log fuer alle Bieter

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Auktionsprozess: Phasen und Zeitplan

| Phase | Typische Dauer | Inhalt | Ergebnis |
|---|---|---|---|
| 1. Vorbereitung | 4-8 Wochen | Teaser, IM, NDA-Entwurf, Datenraum aufbauen | Prozessbereit |
| 2. Erster Kontakt | 2-4 Wochen | Teaser an selektierte Bieter; NDA unterzeichnen | Qualifizierte Interessenten |
| 3. Phase-I-DD | 4-6 Wochen | IM, begrenzter Datenraum, Management Presentation | Non-Binding Offers (NBO) |
| 4. Shortlist / Selection | 1-2 Wochen | NBO-Vergleich; Auswahl 2-4 Finalbieter | Shortlist-Brief |
| 5. Phase-II-DD | 4-8 Wochen | Vollstaendiger Datenraum, Expert Sessions, Q&A, Management Access | Binding Offers (BO) |
| 6. Final Bids | 1-2 Wochen | Binding Offer inkl. marktfaehigem SPA-Entwurf | Preferred Bidder |
| 7. Exklusivitaet | 2-6 Wochen | Finale SPA-Verhandlung; Signing | Signing |

## Process Letter: Typische Pflichtinhalte

```
INFORMATION MEMORANDUM / PROCESS LETTER — [DEAL-NAME]
STRENG VERTRAULICH

1. UEBERSICHT TRANSAKTION
 Zielgesellschaft: [NAME, Sitz, Beschreibung]
 Transaktionsgegenstand: [100 % / X % Anteile / Assets]
 Angestrebtes Closing: [QUARTAL / DATUM]

2. PROZESS-KALENDER
 NDA-Unterzeichnung bis: [DATUM]
 Non-Binding Offer bis: [DATUM]
 Management-Presentation: [KW]
 Binding Offer bis: [DATUM]
 Exklusivitaet: ab [DATUM], Dauer [X Wochen]

3. ANGEBOTSANFORDERUNGEN
 Das Angebot muss enthalten:
 a) Indikativen oder bindenden Kaufpreis (Enterprise Value und Equity Value)
 b) Transaktionsstruktur (Share Deal / Asset Deal)
 c) Wesentliche Vollzugsbedingungen (Kartellrecht, FDI, sonstige)
 d) Finanzierungsnachweis / Funding Commitment
 e) Geplantes Management-Konzept / Integrationsplan
 f) Markierter SPA-Entwurf (Phase II)

4. KONTAKTINFORMATION
 Prozessbevollmaechtigter: [INVESTMENTBANK / KANZLEI]
 Kontakt: [E-Mail]

5. HINWEISE
 - Alle Anfragen nur ueber die Prozessbeauftragten
 - Kein direkter Kontakt zum Management ohne Erlaubnis
 - Vertraulichkeit gemaess NDA; keine Weitergabe von Prozessinformationen
```

## Bieter-Bewertungsmatrix

| Kriterium | Gewichtung | Bieter A | Bieter B | Bieter C |
|---|---|---|---|---|
| Kaufpreis (EV) | 40 % | [EUR] | [EUR] | [EUR] |
| Vollzugssicherheit (Funding, Regulatorik) | 25 % | [Hoch/Mittel] | [Hoch] | [Mittel] |
| Closing-Timeline | 10 % | [Wochen] | [Wochen] | [Wochen] |
| SPA-Qualitaet / Markup | 15 % | [Wenig Markup] | [Kaeufer-freundlich] | [Neutral] |
| Management-Konzept / Synergien | 10 % | [Intern] | [Extern] | [Eigenst.] |
| Gesamtbewertung | 100 % | [Punkte] | [Punkte] | [Punkte] |

## NBO-Vergleich: Vorlage

```
NON-BINDING OFFER SUMMARY
Transaktion: [DEAL-NAME]
Stand: [DATUM]

| Punkt | Bieter A | Bieter B | Bieter C | Benchmark |
|-------|----------|----------|----------|-----------|
| Enterprise Value | EUR [X] | EUR [X] | EUR [X] | EUR [Zielwert] |
| Equity Value (adj.) | EUR [X] | EUR [X] | EUR [X] | |
| Kaufpreismechanik | Locked Box | Closing Acc. | Locked Box | |
| Kartellrecht | Bundeskartellamt | EU-Komm. | — | |
| Vollzugsrisiko | Niedrig | Mittel | Niedrig | |
| Binding Offer: SPA | Ja | Nein | Ja | Ja erforderlich |
| Management-Fortf. | Ja | Nein | Offen | |

EMPFEHLUNG: [Bieter X auf die Shortlist; Begruendung]
```

## Schritt-fuer-Schritt-Workflow

1. **Prozess-Design** — Breite oder schmale Auktion; Zeitplan; Datenraum-Readiness
2. **Bieter-Qualifikation** — strategische vs. Finanzinvestoren; regulatorische Risiken vorab pruefen
3. **Process Letter versenden** — an qualifizierte Interessenten nach NDA-Unterzeichnung
4. **Phase-I-DD organisieren** — IM; erste Datenraum-Zugaenge; Management Presentation
5. **NBO einsammeln und vergleichen** — Bewertungsmatrix; Shortlist-Entscheidung
6. **Phase-II-DD** — vollstaendiger Datenraum; Q&A; Expert Sessions; SPA-Entwurf verteilen
7. **Final Bids auswerten** — Preis, Struktur, Vollzugssicherheit, SPA-Markup
8. **Preferred Bidder auswaehlen** — Exklusivitaetsvereinbarung; Signing-Verhandlungen
9. **Signing** — SPA final; CPs identifiziert; Closing-Timeline

## Rote Schwellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- MAR-Insider-Vorschriften bei borsennotierten Zielgesellschaften nicht eingehalten → Art. 14 MAR
- Bieter direkt kontaktiert Management ohne Prozessbevollmaechtigten → Informationsungleichgewicht; Diskriminierungsrisiko
- SPA-Entwurf nicht standardisiert → Bieter-Markups schwer vergleichbar; Zeitverlust

## Quellen

- §§ 154, 311 II, 241 II BGB; Art. 18 MAR
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 2

## 2. `corporate-kanzlei-steps-plan-pmo`

**Fokus:** Steps Plan und Transaktions-PMO für M&A-Mandate erstellen: Deal-Team benoetigt Gesamtprojektplan mit Workstream-Koordination, CP-Tracking und Status-Reporting. Normen: SPA Closing Conditions, § 158 BGB. Prüfraster: Workstream-Matrix (Legal, Tax, Financial, Regulatory, Commercial), Zeitplan, CP-Tracker, Weekly-Status-Template. Output Steps-Plan, Workstream-Matrix, CP-Tracker, Weekly-Status-Report. Abgrenzung: Monitoring einzelner Fristen siehe automation-monitoring; Signing-Closing siehe signing-closing-conditions.

# Steps Plan und Deal-PMO

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Steps Plan und Deal-PMO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Steps Plan und Deal-PMO

- **Corporate-Aufgabe (Steps Plan und Deal-PMO):** Deal-Team benoetigt Gesamtprojektplan mit Workstream-Koordination, CP-Tracking und Status-Reporting.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Steps Plan und Deal-PMO und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- Mandats-/Gesellschaftsprofil, Organigramm, Rollenmatrix und Eskalationskette.
- Kommunikationskanäle, Vertraulichkeitsstufen, Review-Gates und Beschlusskalender.
- Vorlagen für Board Paper, Beschlussvorlage, Statusbericht und Billing Narrative.

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

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Corporate-Schritt gesellschaftsrechtlich wirksam, registerfähig, organschaftlich vertretbar und für die Mandatsseite praktisch umsetzbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird: Gesellschaft, Organmitglied, Gesellschafter, Investor, Käufer, Verkäufer oder Konzernmutter. Ist die Rolle unklar, darf kein parteilicher Beschluss-, Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Zuständigkeit, Form und Corporate Authority.** Bei Anteils-, Beschluss- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Mehrheit, Form und Registerlage zu prüfen. Relevanter Kern:
- BRAO § 43a, BORA § 3 und BRAO § 49b für Verschwiegenheit, Konflikt und Honorar.
- GwG §§ 10 ff. für Mandatsannahme und wirtschaftlich Berechtigte.
- DSGVO Art. 5, 6, 25 und 32 für Datenminimierung, Rollen und Sicherheit.
- BGB §§ 611a, 675 und 280 für Beratungs- und Haftungsrahmen.

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
- `/corporate-kanzlei:corporate-kanzlei-deal-intake` - wenn ein neues Corporate- oder Transaktionsmandat vollständig aufgenommen werden muss.
- `/corporate-kanzlei:corporate-kanzlei-matter-file` - wenn Gesellschaftsprofil, Workstreams, Fristen und Dokumentenlog in eine laufende Akte geschrieben werden sollen.
- `/corporate-kanzlei:corporate-kanzlei-kommandocenter` - wenn mehrere Corporate-Workstreams konkurrieren und der nächste Primärpfad neu bestimmt werden muss.
- `/corporate-kanzlei:corporate-kanzlei-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.

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

# Steps Plan und Deal-PMO

## Triage — klaere vor Beginn

1. Transaktionsphase: Pre-Signing, Zwischen Signing und Closing, Post-Closing Integration?
2. Welche Workstreams sind aktiv: Legal, Tax, Financial, Regulatory, Commercial?
3. Wer ist das Core-Deal-Team: federf. Partner, Senior/Junior, Investmentbank, Steuerberater?
4. Signing- und Closing-Zieldaten bekannt? Long Stop Date?
5. Kartellrecht und FDI: Anmeldedaten und Pruefdauern bekannt?
6. Weekly-Meeting Turnus und Status-Report-Empfaenger?

## Zentrale Normen & Fristen

- **§§ 35-43 GWB** — Fusionskontrolle; Phase I 4-6 Wochen; Phase II bis 5 Monate
- **§ 56 AWV** — FDI-Pruefung; Anmeldefrist 2 Monate nach Vertragsschluss; Pruefdauer 4 Monate
- **§§ 158, 162 BGB** — Closing Conditions; Fristen und Bedingungen; treuwidrige Verhinderung
- **§ 41 GWB** — Vollzugsverbot; gun jumping; Bussgeld bis 10 % Weltumsatz
- **Art. 7 FKVO** — EU-Vollzugsverbot

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Steps Plan Struktur

Ein Steps Plan listet alle Aktionen zur vollstaendigen Transaktionsdurchfuehrung:

| Schritt | Beschreibung | Owner | Abhaengigkeit | Datum |
|---|---|---|---|---|
| 1 | Term Sheet / LOI unterzeichnen | Deal-Team | — | [Datum] |
| 2 | NDA unterzeichnen | Beide Parteien | — | [Datum] |
| 3 | DD starten (Legal, Tax, FIN, COM) | DD-Teams | NDA | [Datum] |
| 4 | DD-Reports finalisieren | Workstream-Leads | DD-Daten | [Datum] |
| 5 | SPA-Entwurf erstellen | Legal Team | DD-Reports | [Datum] |
| 6 | SPA verhandeln | Parteien / Anwaelte | SPA-Entwurf | [Datum] |
| 7 | Signing | Parteien, Notar | Alle CPs pre-Signing | [Datum] |
| 8 | Kartellrecht anmelden | Kaeufer / Legal | Signing | [Datum] |
| 9 | FDI-Anmeldung | Kaeufer / Legal | Signing | [Datum] |
| 10 | CP-Tracking und Monitoring | PMO | Laufend | Bis Closing |
| 11 | Closing | Notar, Parteien | Alle CPs erfuellt | [Datum] |
| 12 | Post-Closing-Massnahmen | PMO, Recht, Tax | Closing | [Datum] |

## Weekly-Status-Report Vorlage

```
WEEKLY DEAL-STATUS-REPORT
Transaktion: [DEAL-NAME]
KW: [Nr.] / Datum: [DATUM]
Erstellt von: [PMO-Lead]

1. AMPELSTATUS: [GRUEN / GELB / ROT]
 GRUEN: Alle Workstreams planmaessig
 GELB: [Beschreibung des Problems / Risikos]
 ROT: [Kritisches Problem; sofortige Eskalation]

2. MILESTONE-STATUS
 | Milestone | Faellig | Status | Naechste Aktion |
 |-----------|---------|--------|----------------|
 | Signing | [Datum] | [On track / Delayed] | [Massnahme] |
 | Kartellfreigabe | [Datum] | [Angemeldet / Phase I] | [Follow-up] |
 | FDI-Nichtuntersagung | [Datum] | [Angemeldet] | [...] |
 | Closing | [Datum] | [Auf Kurs] | [...] |

3. WORKSTREAM-STATUS
 | Workstream | Lead | Status | Offene Punkte |
 |-----------|------|--------|---------------|
 | Legal DD | [Name] | Abgeschlossen | Litigation-Frage offen |
 | Tax DD | [Name] | 90 % | Betriebspruefungs-Details ausstehend |
 | Regulatory | [Name] | Phase I | BKartA-Rueckfrage am [Datum] |

4. RISIKEN
 | Risiko | Eintrittswahr. | Auswirkung | Massnahme |
 |--------|----------------|-----------|-----------|
 | [Risiko 1] | [%] | [Hoch] | [Massnahme] |

5. ENTSCHEIDUNGSBEDARF
 - [Offener Punkt] → Entscheidung durch [NAME] bis [DATUM]

6. NAECHSTE WOCHE
 | Aktion | Owner | Datum |
 |--------|-------|-------|
 | [Aktion 1] | [Name] | [Datum] |
```

## Schritt-fuer-Schritt-Workflow

1. **Kickoff-Meeting** — alle Workstream-Leads; Steps Plan erstellen; Rollen klaeren
2. **Steps Plan finalisieren** — Abhaengigkeiten kartieren; kritischer Pfad identifizieren
3. **Wochentakt** — Weekly-Call; Status-Update; Risiken; Entscheidungen
4. **CP-Tracker fuehren** — taeglich aktualisieren; Ampelstatus; Eskalation
5. **Signing-Vorbereitung** — Pre-Closing-Checkliste 1 Woche vorher; alles checken
6. **Closing-Koordination** — Notartermin; Kaufpreis-Zahlung; Deliverables-Exchange
7. **Post-Closing-Protokoll** — Closing-Bestaetigung; PMI-Plan uebergeben

## Output-Template Workstream-Matrix

```
WORKSTREAM-MATRIX
Transaktion: [DEAL-NAME]
Stand: [DATUM]

| Workstream | Lead Kaeufer | Lead Verkaefer | Scope | Status |
|-----------|-------------|---------------|-------|--------|
| Legal DD | [Name, Kanzlei] | [Name, Kanzlei] | Full Scope | [%] |
| Tax DD | [Steuerberater] | [Steuerberater] | Full | [%] |
| Financial DD | [WP-Gesellschaft] | — | Limited | [%] |
| SPA-Verhandlung | [Name] | [Name] | Full | [Version] |
| Regulatory | [Name] | [Name] | Kartell, FDI | Phase I |
| HR/PMI | [Name] | [Name] | Post-Closing | Nicht gestartet |
```

## Rote Schwellen

- Steps Plan ohne kritischen Pfad → Zeitplan-Fehler bei Abhaengigkeiten nicht erkannt
- Kein Weekly-Meeting → Workstream-Divergenz; unerkannte Risiken
- CP-Tracker veraltet → Closing-Ueberraschung bei nicht erfuellter Bedingung
- Gun-Jumping wegen falscher Timeline → § 41 GWB; Bussgeld
- PMI-Plan fehlt → Post-Closing-Chaos; Vertragspflichten verpasst

## Quellen

- §§ 35-43 GWB; § 56 AWV; §§ 158, 162 BGB; Art. 7 FKVO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9
