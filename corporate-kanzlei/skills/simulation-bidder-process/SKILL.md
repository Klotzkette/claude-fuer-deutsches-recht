---
name: simulation-bidder-process
description: "Auktionsprozess und Bieter-Perspektive in M&A-Transaktionen simulieren: Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor. Normen: SPA, WpueG (Public M&A), Marktstandard M&A-Auktion. Prüfraster: Process Letter, Bieteranforderungen, NBO-Vergleich, Final Bid Instructions, Exklusivitaet. Output Process-Letter-Entwurf, Bieter-Vergleichsmatrix, NBO-Template. Abgrenzung: SPA-Entwurf siehe spa-apa-entwurf; Public M&A siehe public-ma-kapitalmarkt-mar."
---

# Simulation Bieter-Prozess

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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

### Simulation Bieter-Prozess

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
- **§ 241 II BGB** — Rücksichtnahmepflicht; bei laufenden Verhandlungen schuetzwuerdiges Vertrauen
- **§§ 307, 305 BGB** — AGB-Kontrolle; Process-Dokumente koennen AGB-Charakter haben
- **Art. 18 MAR** — bei borsennotierten Zielgesellschaften: Insider-Log für alle Bieter

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

## Schritt-für-Schritt-Workflow

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
