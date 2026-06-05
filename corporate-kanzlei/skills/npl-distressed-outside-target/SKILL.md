---
name: npl-distressed-outside-target
description: "NPL Distressed Outside Target: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# NPL Distressed Outside Target

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **NPL Distressed Outside Target** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-npl-distressed-loan-transfer` | Prüft Erwerb/Verkauf notleidender Darlehen im Corporate-Kontext: KrZwMG-Rollen, Datenschutz, Sicherheiten, Borrower Notices, Portfolio-DD und Enforcement. |
| `corporate-kanzlei-outside-in-target-screening` | Outside-In-Zielunternehmen-Screening aus öffentlichen Quellen für M&A-Vorprüfung: M&A-Team benoetigt schnellen Überblick über Target ohne Datenraumzugang. Normen: § 3 GwG (UBO-Identifikation), DSGVO, WpHG §§ 33 ff. (Stimmrechtsmitteilungen). Prüfraster: Handelsregister, Bundesanzeiger, LinkedIn/XING, Presse, Kartellverfahren, Sanktionslisten. Output Target-Profil mit Gesellschaftsstruktur, Umsatz/EBITDA-Schaetzung, Risikoflaggen. Abgrenzung: Vertiefte DD nach NDA siehe due-diligence-legal; Registeranalyse siehe handelsregisterabruf. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **NPL Distressed Outside Target**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-npl-distressed-loan-transfer`

**Fokus:** Prüft Erwerb/Verkauf notleidender Darlehen im Corporate-Kontext: KrZwMG-Rollen, Datenschutz, Sicherheiten, Borrower Notices, Portfolio-DD und Enforcement.

# Corporate: NPL und Distressed Loan Transfer

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Corporate: NPL und Distressed Loan Transfer` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Wofür dieser Arbeitsgang da ist

Fokus auf PE/Distressed-Investoren, Banken, Portfoliounternehmen und Loan-to-own-Szenarien.

## Rechts- und Praxisanker

Kreditzweitmarktgesetz, BGB Abtretung, DSGVO, Sicherheiten, InsO/StaRUG, ZVG.

## Workflow

1. Hochgeladenes Finanzierungsdokument, Schuldschein, Transfer Notice, LMA Facility Agreement oder NPL-Portfolio zuerst identifizieren.
2. Parteiperspektive, Deal-Ziel, Fristen, Consent-Erfordernisse, Sicherheiten und Datenschutzfragen klären.
3. Übertragungsweg, Rechtswirkung, offene Dokumente und Risiken in einer Closing-/Verfahrensmatrix darstellen.
4. Bei Insolvenz-/Krisenbezug Rang, Anfechtung, Planrechte, Enforcement und Geschäftsleiterpflichten gesondert prüfen.

## Output

- Transfer-Memo
- Closing-Checkliste
- Risikoampel mit Unterlagenliste
- Notice-/Q&A-Entwurf, falls genügend Angaben vorliegen

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 2. `corporate-kanzlei-outside-in-target-screening`

**Fokus:** Outside-In-Zielunternehmen-Screening aus öffentlichen Quellen für M&A-Vorprüfung: M&A-Team benoetigt schnellen Überblick über Target ohne Datenraumzugang. Normen: § 3 GwG (UBO-Identifikation), DSGVO, WpHG §§ 33 ff. (Stimmrechtsmitteilungen). Prüfraster: Handelsregister, Bundesanzeiger, LinkedIn/XING, Presse, Kartellverfahren, Sanktionslisten. Output Target-Profil mit Gesellschaftsstruktur, Umsatz/EBITDA-Schaetzung, Risikoflaggen. Abgrenzung: Vertiefte DD nach NDA siehe due-diligence-legal; Registeranalyse siehe handelsregisterabruf.

# Outside-In Target Screening

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Outside-In Target Screening` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Outside-In Target Screening

- **Corporate-Aufgabe (Outside-In Target Screening):** M&A-Team benoetigt schnellen Überblick über Target ohne Datenraumzugang.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Outside-In Target Screening und brauche einen belastbaren nächsten Schritt."
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

## Pruefraster im Gutachtenstil
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

# Outside-In Target Screening

## Triage — klaere vor Screening

1. Asset-Klasse: Strategischer Erwerb, Private Equity Add-On, Minderheitsbeteiligung, Distressed?
2. Sektor und Jurisdiktion des Targets?
3. Genehmigungen vorab eingeholen? (Insider-Log wenn Ziel borsennotiert)
4. Welche oeffentlichen Quellen verfuegbar: Handelsregister, Bundesanzeiger, HR-Auszug, Jahresabschluss?
5. Bewertungsrahmen: Multiples-basiert, DCF, Vergleichstransaktionen?
6. Zweck: Vorab-Screening vor Kontaktaufnahme oder Vor-DD?

## Zentrale Normen

- **§ 3 GwG** — UBO-Identifizierung; wirtschaftlich Berechtigter; auch im Screening erfassen
- **Art. 14 DSGVO** — Informationspflicht bei Datenerhebung von Dritten; Grenzen oeffentlicher Quellen
- **§§ 33 ff. WpHG** — Stimmrechtsmitteilungen bei börsennotierten Gesellschaften; BaFin-Datenbank
- **§ 325 HGB** — Offenlegungspflicht Jahresabschluss; Abrufbar im Bundesanzeiger
- **§ 9 HGB** — Handelsregister-Einsichtsrecht; jedermann kann einsehen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Outside-In-Quellen-Matrix

| Quelle | Informationen | Verfuegbarkeit | Verlaesslichkeit |
|---|---|---|---|
| Handelsregister (HRB) | GF, Satzung, Kapital, Jahresabschluss-Hinterlegung | Kostenpflichtig (EUR 4.50 je Abruf) | Sehr hoch (amtlich) |
| Bundesanzeiger | Jahresabschluesse, Bekanntmachungen | Kostenlos | Hoch (Pflichtveroeffentlichung) |
| Transparenzregister | Wirtschaftlich Berechtigter | Kostenpflichtig; berufliche Legitimation | Hoch (gesetzlich) |
| BaFin-Datenbank | Stimmrechtsmitteilungen, Insolvenzbekanntmachungen | Kostenlos | Hoch (BaFin) |
| LinkedIn / XING | Management-Team, Wachstum, Karrieremuster | Kostenlos | Mittel (selbst deklariert) |
| Pressearchiv (Factiva, LexisNexis) | Meldungen, Rechtsstreitigkeiten, Krisen | Kostenpflichtig | Mittel-Hoch |
| Branchenberichte (Statista, IBISWorld) | Marktgroesse, Wettbewerb, Trends | Kostenpflichtig | Hoch |
| Patentdatenbank (DPMA, EPO) | IP-Portfolio, Schutzrechte | Kostenlos | Sehr hoch (amtlich) |

## Finanzanalyse aus oeffentlichen Quellen

### Aus dem Bundesanzeiger
- Umsatz, EBITDA, EBIT, Jahresueberschuss
- Bilanzsumme, Eigenkapitalquote
- Mitarbeiterzahl
- Abhaengigkeit von Hauptkunden (Anmerkungen im Anhang)
- Risikobericht

### Bewertungsrahmen (Multiples-Ansatz)

EV = EBITDA x Branchenm-Multiple

Typische Multiples nach Sektor (indikativ):
- Software/SaaS: 8-15x EBITDA oder 3-8x Revenue
- Industrieproduktion: 5-8x EBITDA
- Handel/Distribution: 4-7x EBITDA
- Gesundheitswesen: 8-12x EBITDA
- Immobilien: nettomietrendite-basiert

### Red Flags im Screening

| Signal | Moegliches Problem |
|---|---|
| Jahresabschluss nicht eingereicht | § 325 HGB Verstos; finanzielle Probleme; Compliance |
| GF-Wechsel haeufig | Managementkrise; Gesellschafterstreit |
| Sinkende Eigenkapitalquote | Finanzierungsengpass; Kreditfaelligkeit |
| Rueckstellungen stark gestiegen | Versteckte Risiken; Litigation |
| Abschluss viele Monate spaet | Finanzierungsprobleme; Prueferstreit |

## Schritt-fuer-Schritt-Workflow

1. **Handelsregister-Abruf** — GmbH oder AG; GF-Daten; Kapitalstruktur; Satzung
2. **Bundesanzeiger-Analyse** — letzte 3 Jahresabschluesse; EBITDA-Trend; Bilanzqualitaet
3. **UBO-Identifizierung** — Transparenzregister-Abfrage; Gesellschafterliste falls verfuegbar
4. **Stimmrechts-Check** — bei borsennotierten Gesellschaften: BaFin-Stimmrechtsdatenbank
5. **Management-Recherche** — LinkedIn, Xing, Pressearchiv; CEO/CFO-Profil; Branchenerfahrung
6. **IP-Screening** — DPMA-Recherche; Patentportfolio; Markenschutzrechte
7. **Litigation-Check** — Pressearchiv; Insolvenzbekanntmachungen; BaFin-Sanktionen
8. **Bewertungsrahmen** — EV-Schaetzung auf Basis Multiples; Vergleichstransaktionen
9. **Screening-Memo** — Zusammenfassung; Empfehlung: Kontaktaufnahme ja/nein; naechste Schritte

## Output-Template Target-Screening-Memo

**Adressat:** Investment Committee / Management — Tonfall klar, faktenbasiert

```
TARGET-SCREENING-MEMO
Zielgesellschaft: [NAME, Sitz, Rechtsform, HRB-Nr.]
Datum: [DATUM]
Erstellt von: [KANZLEI / DEAL-TEAM]
VERTRAULICH

1. UNTERNEHMENSUEBERBLICK
 Gruendungsjahr: [Jahr]
 Hauptgesellschafter: [Namen / Wirtschaftlich Berechtigter]
 Geschaeftsfuehrung: [Namen, Amtsdauer]
 Mitarbeiter: ca. [Zahl] (Quelle: Bundesanzeiger [Jahr])
 Hauptstandorte: [Staedte]

2. FINANZIELLE KENNZAHLEN (aus Bundesanzeiger)
 | Jahr | Umsatz | EBITDA | EK-Quote | Bilanzsumme |
 |------|--------|--------|----------|-------------|
 | 2022 | [EUR Mio.] | [EUR Mio.] | [%] | [EUR Mio.] |
 | 2023 | [EUR Mio.] | [EUR Mio.] | [%] | [EUR Mio.] |

3. BEWERTUNGSINDIKATION (Multiples-Schaetzung)
 Angenommenes EBITDA: [EUR Mio.]
 Branchenm-Multiple: [x-y]x
 Indikative EV-Range: EUR [X] — EUR [Y] Mio.

4. VORHANDENE RISIKEN
 - [Risiko 1: z.B. Jahresabschluss 2023 noch nicht veroeffentlicht]
 - [Risiko 2: z.B. GF-Wechsel 2x in 3 Jahren]

5. STRATEGISCHE FIT-BEWERTUNG
 [2-3 Saetze: Synergien, Marktposition, Komplementaritaet]

6. EMPFEHLUNG
 [ ] Kontaktaufnahme empfohlen
 [ ] Weitere Analyse erforderlich: [Punkt]
 [ ] Kein Fit: [Begruendung]

7. NAECHSTE SCHRITTE
 [Konkrete Handlungen mit Datum und Owner]
```

## Rote Schwellen

- UBO ungeklärt → GwG-Pflicht; keine Mandatsannahme ohne vollständige UBO-Klärung
- Jahresabschluss fehlt → grosses Risiko; § 325 HGB-Verstoss als Red Flag
- Screening ohne Transparenzregister-Abfrage → wirtschaftlich Berechtigter unbekannt
- DSGVO: Personendaten aus Screening speichern ohne Zweck → unzulaessige Verarbeitung (Art. 5 DSGVO)
- Insider-Probleme bei börsennotierten Targets → Art. 14, 17, 18 MAR; Insider-Liste und Ad-hoc-Prüfung anlegen

## Quellen

- § 3 GwG; § 9 HGB; § 325 HGB; §§ 33 ff. WpHG; Art. 14 DSGVO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 1
