---
name: freundlicher-copilot-gesellschaftsrecht
description: "Freundlicher Copilot Gesellschaftsrecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Freundlicher Copilot Gesellschaftsrecht

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Freundlicher Copilot Gesellschaftsrecht** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-freundlicher-copilot` | Freundlicher Corporate-Copilot: Einstiegshilfe für alle Corporate/M&A-Aufgaben. Erklärt Fachbegriffe, gibt Überblicke zu Transaktionsstrukturen, beantwortet Erstfragen und leitet zu passenden Fach-Skills weiter. |
| `corporate-kanzlei-gesellschaftsrecht-register` | Gesellschaftsrechtliche Registeranmeldungen und Satzungsaenderungen durchführen: Handelsregister-Anmeldung von GF-Bestellung, Kapitalerhoehung, Satzungsaenderung, Verschmelzung. Normen: §§ 39-45 GmbHG, §§ 36-39 AktG, HRV, §§ 8-15 HGB. Prüfraster: Anmeldepflicht, Notarerfordernis, Fristen, Registerinhalt, Eintragungshindernisse. Output Anmeldungs-Entwurf, Checkliste Registerunterlagen, Eingabe-Protokoll. Abgrenzung: Umwandlungsrecht siehe umwandlungsrecht-skill; Handelsregister-Analyse bestehender Eintraege siehe handelsregisterabruf. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Freundlicher Copilot Gesellschaftsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-freundlicher-copilot`

**Fokus:** Freundlicher Corporate-Copilot: Einstiegshilfe für alle Corporate/M&A-Aufgaben. Erklärt Fachbegriffe, gibt Überblicke zu Transaktionsstrukturen, beantwortet Erstfragen und leitet zu passenden Fach-Skills weiter.

# Freundlicher Corporate-Copilot

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freundlicher Corporate-Copilot` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freundlicher Corporate-Copilot

- **Corporate-Aufgabe (Freundlicher Corporate-Copilot):** Einstiegshilfe für alle Corporate/M&A-Aufgaben. Erklärt Fachbegriffe, gibt Überblicke zu Transaktionsstrukturen, beantwortet Erstfragen und leitet zu passenden Fach-Skills weiter.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Freundlicher Corporate-Copilot und brauche einen belastbaren nächsten Schritt."
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
- `/corporate-kanzlei:corporate-kanzlei-steps-plan-pmo` - wenn Termine, Beschlüsse, CPs, Freigaben und Owner in einen belastbaren Plan müssen.
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

# Freundlicher Corporate-Copilot

## Zweck

Erste Anlaufstelle fuer alle Corporate/M&A-Fragen. Beantwortet Einstiegsfragen, erklaert Konzepte und leitet an die richtigen Fach-Skills weiter.

## Haeufige Erstfragen und kurze Antworten

### Was ist ein Share Deal vs. Asset Deal?
- **Share Deal:** Kaeufer erwirbt Anteile der Gesellschaft. Alle Verbindlichkeiten gehen mit. Steuerneutral fuer Verkaefer (§ 8b KStG). GmbH: notariell (§ 15 GmbHG).
- **Asset Deal:** Kaeufer erwirbt einzelne Wirtschaftsgueter. Verbindlichkeiten nur soweit vereinbart. § 613a BGB beachten. Steuerlich: AfA-Neustart moeglich fuer Kaeufer.

### Was ist eine MAC-Klausel?
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Was ist die Business Judgment Rule (BJR)?
§ 93 I 2 AktG: Vorstand haftet nicht bei unternehmerischen Entscheidungen, wenn er angemessen informiert im Unternehmensinteresse gehandelt hat. Wichtig: Board Paper erstellen; Informationsgrundlage dokumentieren.

### Was ist W&I-Versicherung?
Warranty & Indemnity Insurance sichert Garantie-Verletzungsansprueche gegen den Versicherer ab. Kaeufer-Policy: Kaeufer klagt direkt Versicherer. Sinnvoll ab ca. 15-20 Mio. EUR EV. Praemie: ca. 1 % der Versicherungssumme.

### Was ist ein Squeeze-Out?
Mehrheitsaktionaer mit >95 % (AktG §§ 327a-f) kann Minderheitsaktionaere gegen Barabfindung ausschliessen. Spruchverfahren moeglich. WpUeG-Squeeze-Out: nach Uebernahme ab 90 % (§§ 39a-c WpUeG).

### Was ist Locked Box vs. Closing Accounts?
- **Locked Box:** Kaufpreis fixiert auf historische Bilanz; Leakage-Schutz; einfacher
- **Closing Accounts:** Kaufpreis passt sich an tatsaechliche Bilanz beim Closing an; genauer; mehr Streitpotenzial

## Routing: Welcher Skill hilft weiter?

| Frage | Empfohlener Skill |
|---|---|
| Neues Mandat aufsetzen | `corporate-kanzlei-kaltstart` |
| Due Diligence starten | `corporate-kanzlei-due-diligence-legal` |
| SPA verhandeln | `corporate-kanzlei-spa-apa-entwurf` |
| Kartell-/FDI-Check | `corporate-kanzlei-regulatory-fdi-merger-control` |
| Closing vorbereiten | `corporate-kanzlei-signing-closing-conditions` |
| GmbH-Gruendung | `gesellschaftsgruender-gmbh-vorbereitung` |
| Gesellschafterstreit | `gesellschafterstreit-loesungsstrategie` |
| GF-Haftung | `geschaeftsfuehrer-haftung-43-gmbhg` |
| Konzernrecht | `gesellschaftsrecht-mandat-arbeitsbereich` |

## Aktuelle Rechtsprechung (Grundbegriffe)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rote Schwellen

- Unbekannte Materie → an Fach-Skill oder Senior Partner weiterleiten
- Mandatsgeheimnis: keine vertraulichen Details an unberechtigte Dritte
- Fristen immer mit Kalender absichern; Verjährung und CP-Fristen sind kritisch

## 2. `corporate-kanzlei-gesellschaftsrecht-register`

**Fokus:** Gesellschaftsrechtliche Registeranmeldungen und Satzungsaenderungen durchführen: Handelsregister-Anmeldung von GF-Bestellung, Kapitalerhoehung, Satzungsaenderung, Verschmelzung. Normen: §§ 39-45 GmbHG, §§ 36-39 AktG, HRV, §§ 8-15 HGB. Prüfraster: Anmeldepflicht, Notarerfordernis, Fristen, Registerinhalt, Eintragungshindernisse. Output Anmeldungs-Entwurf, Checkliste Registerunterlagen, Eingabe-Protokoll. Abgrenzung: Umwandlungsrecht siehe umwandlungsrecht-skill; Handelsregister-Analyse bestehender Eintraege siehe handelsregisterabruf.

# Gesellschaftsrecht und Register

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschaftsrecht und Register` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Gesellschaftsrecht und Register

- **Corporate-Aufgabe (Gesellschaftsrecht und Register):** Handelsregister-Anmeldung von GF-Bestellung, Kapitalerhoehung, Satzungsaenderung, Verschmelzung.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Gesellschaftsrecht und Register und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- Registerauszüge, Gesellschafterliste, Satzung, Geschäftsordnungen und Vollmachten.
- Organbeschlüsse, Zustimmungskataloge, Vollmachtsketten, Protokolle und Notartermine.
- Cap Table, Beteiligungskette, Umwandlungs- oder Carve-out-Plan.

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
- GmbHG §§ 15, 16, 40, 46, 47 und 48 für Anteilsübertragung, Gesellschafterliste und Beschlüsse.
- AktG §§ 76, 93, 111, 116, 179a und 186 für Leitung, Aufsicht, Business Judgment und Strukturmaßnahmen.
- HGB §§ 8 ff., 15 und §§ 161 ff. für Registerpublizität und Personengesellschaften.
- UmwG §§ 2, 123, 190 ff. für Verschmelzung, Spaltung und Formwechsel.

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
- `/corporate-kanzlei:corporate-kanzlei-handelsregisterabruf` - wenn der offizielle Registerstand belegt werden muss.
- `/corporate-kanzlei:corporate-kanzlei-transaktionsstruktur` - wenn Share Deal, Asset Deal, Carve-out, Umwandlung oder Holdingstruktur verglichen werden.
- `/corporate-kanzlei:corporate-kanzlei-umwandlungsrecht` - wenn Verschmelzung, Spaltung, Formwechsel oder Ausgliederung strukturiert werden.
- `/corporate-kanzlei:corporate-kanzlei-board-paper-business-judgment` - wenn Organentscheidung und Business-Judgment-Dokumentation vorbereitet werden.

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

# Gesellschaftsrecht und Register

## Triage — klaere vor Beginn

1. Welche Aenderung soll angemeldet werden: GF-Wechsel, Satzungsaenderung, Kapitalerhoehung, Sitzverlegung, Firmennamensaenderung?
2. GmbH oder AG? (Verfahren unterschiedlich; AG braucht AR-Beschluss und HV bei Satzungsaenderung)
3. Notar: Erforderlich fuer notarielle Beurkundung und Anmeldung (§ 8 I GmbHG)?
4. Eintragungspflichtige und freiwillige Eintragungen unterscheiden?
5. Fristen: Manche Aenderungen muessen unverzueglich (§ 39 I GmbHG) angemeldet werden.
6. Auslaendische Gesellschafter: Apostille, Legalisation, Uebersetzung von Vollmachten?

## Zentrale Normen

- **§§ 39-45 GmbHG** — GF-Anmeldung; Satzungsaenderung; Kapitalerhoehung; Liquidation
- **§§ 36-39 AktG** — Vor-AG; Anmeldung; Eintragungsvoraussetzungen
- **§§ 179-180 AktG** — Satzungsaenderung bei AG; HV-Beschluss; 3/4-Mehrheit; Eintragung
- **§ 184 AktG** — Kapitalerhoehung gegen Einlagen; Anmeldung
- **§§ 8-10 HGB** — Handelsregister; Eintragungspflicht; Bekanntmachungspflicht
- **§§ 3-6 HRV (Handelsregisterverordnung)** — Anmeldeformulare; elektronische Einreichung
- **§ 15 GmbHG** — Anteilsuebertragung; Gesellschafterliste (neue Fassung); Notar

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anmelde-Checkliste: GF-Wechsel (GmbH)

1. Gesellschafterversammlungs-Beschluss ueber Abberufung altes GF / Bestellung neues GF
2. Ggf. Annahme der Bestellung durch neuen GF
3. Nicht-Vorliegen von Bestellungshindernissen (§ 6 II GmbHG: keine Vorstrafe wegen Wirtschaftsdelikten)
4. Notarielle Anmeldung durch neuen GF (oder Notar in Vollmacht)
5. Handelsregisteranmeldung mit: vollstaendige Name, Geburtsdatum, Wohnort, Vertretungsbefugnis (Einzel/Gesamt)
6. Muster der Unterschrift des neuen GF in notariell beglaubigter Form

## Anmelde-Checkliste: Satzungsaenderung (GmbH)

1. Beschluss der Gesellschafterversammlung mit 3/4-Mehrheit (oder Satzungsmehrheit)
2. Protokoll (notariell wenn Satzungsaenderung Kapital betrifft; sonst beurkundet oder einfach — je nach Satzung)
3. Notarielle Beurkundung des Aenderungsbeschlusses (§ 53 II GmbHG)
4. Vollstaendiger Satzungstext in geaenderter Fassung (keine blossen Aenderungsmarkierungen)
5. Anmeldung durch saemtliche GF
6. Einreichung beim Registergericht

## Schritt-fuer-Schritt-Workflow

1. **Handlungsbedarf identifizieren** — welche Aenderung; welche Organbeschluesse erforderlich
2. **Notar beauftragen** — fuer Beurkundung Beschluss und Anmeldung
3. **Unterlagen vorbereiten** — Beschlussprotokoll; aktueller HR-Auszug; Vollmachten; ggf. Apostille
4. **Beurkundung / Beglaubigung** — Notartermin; alle Unterschriften
5. **Handelsregisteranmeldung** — elektronisch durch Notar (ERV; § 12 HGB)
6. **Eintragungsfrist monitoring** — Registergericht: 4-8 Wochen; Erinnerung nach 3 Wochen
7. **HR-Auszug post-Eintragung** — aktuellen Auszug einholen; in Closing-Bible ablegen
8. **Folgehandlungen** — Bank informieren; interne Systeme aktualisieren; Transparenzregister pruefen

## Output-Template HR-Anmeldungsschreiben (Vorlage Notar)

```
ANMELDUNG ZUM HANDELSREGISTER
Amtsgericht [STANDORT]
Handelsregister-Abteilung B
[ADRESSE]

Betreff: [FIRMA GmbH] — HRB [NUMMER]
 Aenderung der Geschaeftsfuehrung

Wir melden als Geschaeftsfuehrer der [FIRMA GmbH] zur Eintragung in das Handelsregister an:

1. ABBERUFUNG:
 [ALTER GF: Name, Geburtsdatum, Wohnort] ist als Geschaeftsfuehrer abberufen worden.
 Beschluss der Gesellschafterversammlung vom [DATUM].

2. NEUBESTELLUNG:
 Zum neuen Geschaeftsfuehrer ist bestellt worden:
 [NEUER GF: Name, Geburtsdatum, Wohnort]
 Vertretungsbefugnis: Einzelvertretungsberechtigung / Gesamtvertretungsberechtigung
 Beschluss der Gesellschafterversammlung vom [DATUM].

 Befreiung von §181 BGB: [Ja / Nein]

3. VERSICHERUNG GEMAESS § 8 III GMBHG
 Der Unterzeichner versichert, dass kein Bestellungshindernis nach § 6 II GmbHG vorliegt.

[FIRMA GMBH]
[NEUER GF NAME]
[DATUM, ORT]

Notariell beglaubigte Unterschrift des neuen GF (Anlage)
```

## Rote Schwellen

- Anmeldung durch nicht mehr amtierenden GF → Zurueckweisung durch Registergericht
- Satzungsaenderung ohne notarielle Beurkundung → § 53 II GmbHG; Nichtigkeit des Beschlusses
- Gesellschafterliste nicht aktualisiert nach Anteilsuebertragung → gutglaeubiger Erwerb durch Dritten moeglich
- Auslaendische Vollmacht ohne Apostille → Registergericht akzeptiert nicht
- Frist fuer Anmeldung verpasst → Ordnungswidrigkeitengeld (§ 79 GmbHG); Zwangsgeld

## Quellen

- §§ 39-45 GmbHG; §§ 179-184 AktG; §§ 8-10 HGB; § 12 HGB (elektronische Anmeldung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
