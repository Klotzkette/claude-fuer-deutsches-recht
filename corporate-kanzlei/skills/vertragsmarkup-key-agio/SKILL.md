---
name: vertragsmarkup-key-agio
description: "Vertragsmarkup KEY Agio: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertragsmarkup KEY Agio

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Vertragsmarkup KEY Agio** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-vertragsmarkup-key-issues` | Juristischen Markup für M&A-Vertraege und Key-Issues-Memo erstellen: Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden. Normen: §§ 305 ff. BGB (AGB-Kontrolle im B2B), Marktstandard DE/UK M&A. Prüfraster: Abweichungen vom Marktstandard, kritische Klauseln (MAC, Indemnification, Reps Survival), Red-Lines vs. Nice-to-have. Output Markup mit Kommentaren, Key-Issues-Memo, Verhandlungs-Prioritaetenliste. Abgrenzung: SPA-Ersterstellung siehe spa-apa-entwurf; AGB-Prüfung allgemein siehe Vertragsrecht-Plugin. |
| `corporate-kanzlei-agio-und-kapitalerhoehungsstruktur` | Strukturierung von Kapitalerhöhungen mit Agio bei VC-Finanzierungsrunden Holding-Aufbauten und M&A-Sekundärfinanzierungen. Übersetzung US-Term-Sheet-Begriffe (Original Purchase Price Par Value APIC Liquidation Preference) in deutsche Kategorien (Ausgabebetrag Nennbetrag Kapitalrücklage Vorzugsrecht). Differenzierung echtes vs. unechtes Agio. Sachagio im Rahmen des qualifizierten Anteilstauschs § 21 UmwStG. Eintragungshindernisse beim Handelsregister vermeiden. Schnittstellen zu Notar Steuerberater Investor Counsel. Lädt bei VC-Runden Series A/B/C Anteilstauschen Bridge-Finanzierungen und Convertible-Wandlungen. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Vertragsmarkup KEY Agio**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-vertragsmarkup-key-issues`

**Fokus:** Juristischen Markup für M&A-Vertraege und Key-Issues-Memo erstellen: Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden. Normen: §§ 305 ff. BGB (AGB-Kontrolle im B2B), Marktstandard DE/UK M&A. Prüfraster: Abweichungen vom Marktstandard, kritische Klauseln (MAC, Indemnification, Reps Survival), Red-Lines vs. Nice-to-have. Output Markup mit Kommentaren, Key-Issues-Memo, Verhandlungs-Prioritaetenliste. Abgrenzung: SPA-Ersterstellung siehe spa-apa-entwurf; AGB-Prüfung allgemein siehe Vertragsrecht-Plugin.

# Vertragsmarkup und Key Issues

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vertragsmarkup und Key Issues` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Vertragsmarkup und Key Issues

- **Corporate-Aufgabe (Vertragsmarkup und Key Issues):** Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Vertragsmarkup und Key Issues und brauche einen belastbaren nächsten Schritt."
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

# Vertragsmarkup und Key Issues

## Triage — klaere vor Markup

1. Welcher Vertragstyp: SPA, APA, SHA, NDA, LOI, Term Sheet, GAV, TSA?
2. Mandant Kaeufer oder Verkaefer? (Markup-Perspektive)
3. Governing Law: Deutsches Recht, englisches Recht, hybrid?
4. Version: erster Entwurf (Gegenpartei) oder eigener Erstentw. der zurueckgekommen ist?
5. Schwerpunkte: Kaufpreismechanik, Haftung, Garantien, CoC, Kartellrecht?
6. Frist fuer Markup-Rueckgabe?

## Zentrale Normen

- **§§ 305-310 BGB** — AGB-Kontrolle; Klauseln koennen bei unangemessener Benachteiligung unwirksam sein
- **§ 307 BGB** — Generalklausel; Transparenzgebot; unklar formulierte Klauseln Kaeufer-nachteilig
- **§ 444 BGB** — Arglist; keine Freizeichnung moeglich
- **§ 449 BGB** — Eigentumsvorbehalt
- **§ 138 BGB** — Sittenwidrigkeit bei wucheraehnlichen Haftungsausschluessen
- **§ 276 III BGB** — Haftung fuer Vorsatz kann nicht vertraglich ausgeschlossen werden

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Key Issues Abweichungen vom Marktstandard

### Haftungsregime

| Klausel | Marktstandard | Kaeufer-freundlich | Verkaefer-freundlich |
|---|---|---|---|
| De-Minimis | 25-50 TEUR | 10-25 TEUR | 100+ TEUR |
| Basket (Tipping) | 0.5-1.0 % des KP | 0.25-0.5 % | 1.0-1.5 % |
| Cap (allg. Warranties) | 20-30 % des KP | 50-100 % | 10-15 % |
| Cap (Title/Fundamental) | 100 % des KP | 100 % oder mehr | 50-100 % |
| Verjährung (allg.) | 18-24 Monate | 36 Monate | 12 Monate |
| Verjährung (Tax) | 5-7 Jahre | 7 Jahre | 5 Jahre |
| Verjährung (Titel) | Unbegrenzt | Unbegrenzt | Verjährungsausschluss moeglich |

### Anti-Sandbagging

- Kaeufer-freundlich: Anspruch auch bei Kaeufer-Kenntnis; § 442 BGB verdraengt
- Verkaefer-freundlich: Kenntnis des Kaeufers fuehrt zu Anspruchsverlust
- Marktstandard DE: eher kaeufer-freundlich (§ 442 BGB durch SPA-Klausel verdraengt)

### Earn-Out

- Marktstandard: Fixierung der Accounting-Methodik; Non-Frustration-Klausel
- Kaeufer-Risiko: keine feste Methodology; keine Foerderpflicht
- Verkaefer-Risiko: Milestone-Definition zu ungenau; Kaeufer kann leicht verfehlen

## Markup-Praxis: Haeufige Red-Marks

### Typische Verkaefer-Entwurfs-Klauseln die Markup brauchen

1. **Kenntnis-Qualifikation auf alle Warranties** → Kaeufer: kein "Knowledge" fuer Titel-Warranties; nur fuer Business Warranties
2. **Cap = 10 % des KP** → Kaeufer: Counter-Markup auf 20-30 % mindestens; Fundamental Warranties: 100 %
3. **Verjährung 12 Monate** → Kaeufer: 24 Monate allg.; Tax 5 Jahre; Titel unbegrenzt
4. **Sandbagging: Verkaefer-Klausel** → Kaeufer: Anti-Sandbagging streichen oder Kaeufer-freundliche Formulierung einfuegen
5. **Materality-Qualifier auf alle Business Reps** → Kaeufer: "Materiality Scrape" einfuegen (fuer Haftungsberechnung ignoriert)
6. **Indemnity-Ausschluss bei Versicherungsleistung** → Kaeufer: bei W&I-Policy sinnvoll aber nur dann
7. **Schiedsklausel: nur an einem Ort** → sicherstellen: klar definiert, ICC/DIS, Frankfurt oder Muenchen, 3 Schiedsrichter

## Schritt-fuer-Schritt-Workflow

1. **Vertragstype und Kontext** — was liegt vor; Perspektive; Governing Law
2. **Gesamtlesedurchgang** — Struktur, Kernklauseln, ersten Eindruck
3. **Key-Issues-Identifikation** — Abweichungen vom Marktstandard markieren; Liste erstellen
4. **Markup erstellen** — Tracked Changes; klare Kommentare warum; nicht nur Korrektur sondern Begruendung
5. **Key Issues Memo** — Zusammenfassung der wichtigsten Punkte fuer Mandanten; Prioritaetsstufen: Deal-Breaker / High Priority / Negotiation Position / Market Standard
6. **Klientenfreigabe** — Mandant gibt Business-Entscheidungen frei; Anwalt setzt um
7. **Verhandlung** — Gespraeche zu allen offenen Punkten; Kompromissoptionen vorbereiten
8. **Finalversion** — Clean Copy; alle geeinigten Punkte eingearbeitet; Signaturseiten pruefen

## Output-Template Key Issues Memo (Auszug)

**Adressat:** Mandant — Tonfall klar, handlungsorientiert

```
KEY ISSUES MEMO — MARKUP [VERTRAGSTYP]
Transaktion: [DEAL-NAME]
Stand: [DATUM / VERSION]
Erstellt von: [KANZLEI]
VERTRAULICH

EXECUTIVE SUMMARY
[2-3 Saetze: Gesamteindruck; kritischste Punkte]

PRIORITAET 1 — DEAL-BREAKER/ENTSCHEIDUNGSBEDARF

1.1 Haftungs-Cap: § X des SPA sieht Cap von [X %] des Kaufpreises vor.
 Marktstandard: 20-30 %; unsere Position: mindestens 25 %.
 Markup: "[NEUE FORMULIERUNG]"
 Empfehlung: Harte Verhandlungsposition.

1.2 Verjährung Tax Indemnity: Nur 3 Jahre vorgesehen; bei steuerlichen Nachhaftungsrisiken aus Betriebspruefungen zu kurz.
 Empfehlung: 7 Jahre fuer Tax-Themen; unbegrenzt fuer Steuerhinterziehung.

PRIORITAET 2 — HOHE PRIORITAET

2.1 [Klausel]
 Problem: [Beschreibung]
 Markup: [Vorschlag]

PRIORITAET 3 — VERHANDLUNGSPOSITION

3.1 [...]

NAECHSTE SCHRITTE
- [Datum]: Markup an Gegenseite senden
- [Datum]: Verhandlungsgespraeche
```

## Rote Schwellen

- Markup ohne Begruendung — Gegenseite versteht Motiv nicht; Verhandlung ineffektiv
- AGB-Kontrolle vergessen — unangemessene Klauseln koennen im deutschen Recht unwirksam sein
- Cap fuer alle Warranties gleichgesetzt — Fundamental-Warranties brauchen hoeheren oder keinen Cap
- Schiedsvereinbarung unklar — Vollstreckung im Ausland scheitert an Unwirksamkeit
- Anti-Sandbagging nicht verhandelt — bei Kaeufer-Kenntnis aus DD kein Warranty-Anspruch

## Quellen

- §§ 305-310, 307, 444, 276 III BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 2. `corporate-kanzlei-agio-und-kapitalerhoehungsstruktur`

**Fokus:** Strukturierung von Kapitalerhöhungen mit Agio bei VC-Finanzierungsrunden Holding-Aufbauten und M&A-Sekundärfinanzierungen. Übersetzung US-Term-Sheet-Begriffe (Original Purchase Price Par Value APIC Liquidation Preference) in deutsche Kategorien (Ausgabebetrag Nennbetrag Kapitalrücklage Vorzugsrecht). Differenzierung echtes vs. unechtes Agio. Sachagio im Rahmen des qualifizierten Anteilstauschs § 21 UmwStG. Eintragungshindernisse beim Handelsregister vermeiden. Schnittstellen zu Notar Steuerberater Investor Counsel. Lädt bei VC-Runden Series A/B/C Anteilstauschen Bridge-Finanzierungen und Convertible-Wandlungen.

# Agio und Kapitalerhöhungsstruktur in der Corporate-Praxis

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Agio und Kapitalerhöhungsstruktur in der Corporate-Praxis` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Vor dem ersten Term-Sheet-Markup klären:

1. **Dealtyp:** Erste VC-Runde Folgerunde Bridge Convertible-Wandlung Anteilstausch nach § 21 UmwStG oder Sekundärtransaktion mit Kapitalmaßnahme?
2. **Beteiligungsstruktur des Lead Investors:** Deutsche GmbH KG US-LP Luxemburg-SCS oder andere Auslandsstruktur? Beeinflusst Beurkundungsbedarf und Steuerlogik.
3. **Stammkapital aktuell und post-money:** Wie viel zusätzliches Stammkapital wird ausgegeben wie viel Agio? Standardmuster bei VC-Runden 99 Prozent Agio.
4. **Agio-Charakter:** Echtes (korporatives) oder unechtes (schuldrechtliches) Agio? Beim qualifizierten Anteilstausch § 21 UmwStG ist echtes Agio Voraussetzung für Buchwertfortführung.
5. **Fälligkeit des Agios:** Bei Closing in voller Höhe (Fall 1) oder gestaffelt (Fall 2)? Bei Fall 2 muss das Agio in den aktualisierten Satzungstext sonst Eintragungshindernis.
6. **Liquidation Preference:** Bezugsgröße Ausgabebetrag (Nennbetrag plus Agio) oder fälschlich nur Nennbetrag?
7. **Steuerliche Strukturierung:** Soll das Agio in das steuerliche Einlagekonto § 27 KStG fließen für spätere steuerneutrale Rückgewähr?

## Zentrale Schnittstellen

- **Notar** (Beurkundung Kapitalerhöhungsbeschluss Übernahmeerklärung Satzungsneufassung).
- **Steuerberater** (UmwStG-Konformität § 27 KStG-Erfassung Buchwertfortführung).
- **Investor Counsel** (oft US- oder UK-Kanzlei mit Delaware-Denke).
- **CFO und Tax** der Mandantin (Cashflow-Planung Bilanzaufstellung).
- **Handelsregister** (Anmeldung neue Anteilsstruktur Gesellschafterliste § 40 GmbHG).

## Standardmuster Series-A-Runde

| Komponente | Typische Größenordnung |
|---|---|
| Stammkapital vor Runde | EUR 25.000 bis 50.000 |
| Investitionsvolumen | EUR 3 bis 20 Mio |
| Nennbetrag je neuem Geschäftsanteil | EUR 1,00 |
| Anzahl neuer Geschäftsanteile | 5.000 bis 30.000 |
| Ausgabebetrag je Anteil | abhängig von Pre-Money und Cap Table |
| Agio je Anteil | Ausgabebetrag minus EUR 1,00 |
| Agio-Anteil an Investition | typisch 99 bis 99,9 Prozent |
| Stammkapital nach Runde | EUR 35.000 bis 75.000 |

Das ist nicht atypisch sondern Standard. Wer mit einem Lead Investor verhandelt der das Agio vermeiden will hat in den meisten Fällen einen Atypiker am Tisch oder einen Investor der die deutsche GmbH-Struktur nicht versteht.

## Übersetzungstabelle US-Term-Sheet zu deutscher Satzung

| US-Begriff | Deutsche Entsprechung | Häufige Fehler |
|---|---|---|
| Original Purchase Price (OPP) | Ausgabebetrag je Geschäftsanteil | wird mit Kaufpreis übersetzt — falsch |
| Original Issue Price (OIP) | Ausgabebetrag je Geschäftsanteil | wie OPP |
| Par Value | Nennbetrag § 5 Abs. 2 GmbHG | wird mit Nennwert übersetzt — akzeptabel aber nicht juristisch präzise |
| Additional Paid-In Capital (APIC) | Kapitalrücklage § 272 Abs. 2 Nr. 1 HGB | wörtlich Zusätzliches eingezahltes Kapital — falsche Bilanzposition |
| Premium over par | Agio Aufgeld | wird mit Aufpreis übersetzt — umgangssprachlich nicht falsch aber unpräzise |
| Stated Capital | Gezeichnetes Kapital Stammkapital | manchmal mit Grundkapital verwechselt (das ist AG-Begriff § 6 AktG) |
| Issued Shares | Ausgegebene Geschäftsanteile | bei der GmbH gibt es keine Shares im US-Sinne |
| Outstanding Shares | Ausgegebene und nicht eingezogene Geschäftsanteile | dasselbe wie Issued Shares minus Treasury Shares (in DE selten relevant) |
| Authorized Capital | Genehmigtes Kapital — bei der AG § 202 AktG, bei der GmbH seit MoMiG ausdrücklich § 55a GmbHG (für VC-Runden zunehmend genutzt; eigener Skill gesellschaftsgruender-genehmigtes-kapital im Repo) | gelegentlich mit Stammkapital verwechselt; früher verbreiteter Irrtum, GmbH kenne kein genehmigtes Kapital |
| Pre-Money Valuation | Pre-Money-Bewertung Vor-Investitionsbewertung | unkritisch |
| Post-Money Valuation | Post-Money-Bewertung | unkritisch |
| Liquidation Preference 1x OPP | Einfache Liquidationspräferenz auf den Ausgabebetrag | wird oft als 1x Nennbetrag interpretiert — katastrophal für den Investor |
| Anti-Dilution Adjustment | Anti-Dilution-Anpassung des Ausgabebetrags | wird oft als Anpassung der Nennbeträge missverstanden — § 5 Abs. 2 GmbHG verbietet das |
| Conversion Price | Wandlungspreis | unkritisch |
| Conversion Ratio | Wandlungsverhältnis | unkritisch |

## Strukturierungsentscheidungen mit Kostenrelevanz

### Wieviel Stammkapital wird ausgegeben?

Die Versuchung des unerfahrenen Berators ist groß, das Stammkapital möglichst hoch anzusetzen — etwa weil der Investor mehr Stammkapital als ehrenhafter ansieht. Das ist ein Fehler:

- Hohes Stammkapital = dauerhafte Kapitalbindung § 30 GmbHG.
- Kapitalherabsetzung später nur über §§ 58 ff. GmbHG mit Sperrjahr Gläubigeraufruf und 6-Monats-Frist.
- Geschäftsführerhaftung steigt mit der Stammkapitalhöhe wegen § 43 Abs. 3 GmbHG in Verbindung mit § 30 GmbHG.

Praxismuster: Nennbetrag je Anteil bei EUR 1,00 belassen Stammkapital nur um Anzahl der neuen Anteile erhöhen — der Rest als Agio in die Kapitalrücklage.

### Echtes oder unechtes Agio?

| Anwendungsfall | Empfehlung |
|---|---|
| VC-Runde mit Lead Investor | Echtes Agio |
| Bridge-Finanzierung durch Altgesellschafter | Echtes Agio einfacher zu erklären |
| Convertible-Wandlung | Echtes Agio (Wandlungspreis als Ausgabebetrag) |
| Quersubventionierung zwischen Gesellschaftern | Unechtes Agio (schuldrechtliche Nebenabrede) |
| Holding-Strukturierung § 21 UmwStG | Echtes Sachagio zwingend für Buchwertfortführung |
| Mitarbeiterbeteiligung (ESOP) | Hängt vom Modell ab — bei echter Anteilsausgabe echtes Agio bei virtueller Beteiligung kein Agio |

### Fälligkeit des Agios

Standardmuster: Fälligkeit bei Eintragung der Kapitalerhöhung in das Handelsregister. Damit greift Fall 1 — keine Aufnahme des Agios in den Satzungstext erforderlich Kapitalerhöhungsbeschluss und Übernahmeerklärung genügen.

Abweichende Konstellationen bei denen Fall 2 (Aufnahme in Satzungstext) angezeigt ist:

- Staged Closings (z.B. Tranche bei Closing Tranche bei Erreichen von Milestones).
- Earn-out-ähnliche Strukturen mit nachgelagertem Agio.
- Bridge-to-Series-A-Strukturen mit Wandlungsverzögerung.
- Sachagio mit nachgelagerter Werthaltigkeitsprüfung.

Bei Fall 2 unbedingt in den neuen § 3a oder § 4 der Satzung aufnehmen sonst Eintragungshindernis und doppelter Notartermin.

## Schnittstellenmanagement im Deal

### Notar

- Notar verlangt deutsche Beurkundungssprache § 5 BeurkG. Term Sheet bleibt englisch Satzung wird zweisprachig oder deutsch.
- Notar muss Agio in Kapitalerhöhungsbeschluss und Übernahmeerklärung sauber wiederfinden — sonst Beanstandung.
- Bei Sachagio: Sachgründungsbericht analog § 5 Abs. 4 GmbHG mit Werthaltigkeitsbeleg.
- Vor dem Notartermin: Liste der zu beurkundenden Dokumente mit dem Notariat abstimmen.

### Steuerberater

- Bestätigung dass Buchwertfortführung nach § 21 UmwStG möglich ist (qualifizierter Anteilstausch).
- Bestätigung dass das Agio korrekt in das steuerliche Einlagekonto § 27 KStG fließt.
- Bei Verlustvorträgen Prüfung des § 8c KStG (schädlicher Beteiligungserwerb bei mehr als 50 Prozent Übergang).
- Bei US-Investoren mit LP-Struktur: Quellensteuerprüfung DBA-Anwendung.

### Investor Counsel

- US- oder UK-Kanzlei denkt in Delaware-Kategorien — Par Value 0,0001 USD APIC selbstverständlich.
- Erklärungsbedarf für deutsche Spezialitäten: notarielle Beurkundung Vinkulierung § 15 Abs. 5 GmbHG keine echten Anteilsklassen Sonderrechte über Satzungsautonomie und § 35 BGB analog.
- Investor Counsel will oft Liquidation Preference 1x non-participating preferred. Das ist sauber zu übersetzen als einfache Liquidationspräferenz auf den Ausgabebetrag mit Catch-up oder ohne.

### CFO der Mandantin

- Cashflow-Planung: wann fließt das Agio? Voll bei Closing oder gestaffelt?
- Bilanzielle Behandlung: Erhöhung Kapitalrücklage § 272 Abs. 2 Nr. 1 HGB nicht Stammkapital.
- Reporting an Bestandsgesellschafter: wie wird die Verwässerung kommuniziert?

## Häufige Streitpunkte und ihre Lösung

### Liquidation Preference auf Nennbetrag oder Ausgabebetrag

Standard: **Ausgabebetrag** (Nennbetrag plus Agio). Eine Liquidation Preference 1x Nennbetrag wäre für den Investor wirtschaftlich katastrophal — bei einem 99 Prozent Agio bleiben dem Investor 1 Prozent seiner Investition als Vorrecht. Das ist kein Markt.

### Anti-Dilution mit Folgewirkung auf Liquidation Preference

Wenn der Anti-Dilution-Mechanismus den Conversion Price (deutsch: Wandlungspreis) anpasst muss die Liquidation Preference darauf reagieren. Häufig anzutreffen: Weighted Average broad-based oder narrow-based oder Full Ratchet. Bei der GmbH wird das technisch über Anpassung des wirtschaftlichen Bezugswertes umgesetzt nicht über Anpassung des Nennbetrags (§ 5 Abs. 2 GmbHG verbietet Nennbeträge unter EUR 1).

### Pari-passu oder Senior bei mehreren Series

In Series-B-Runden stellt sich die Frage ob die Series-B-Liquidation-Preference pari passu mit Series A oder senior dazu ist. Pari passu ist Markt für Bestandsinvestoren senior typisch für Lead-getriebene B-Runden. Die Satzung muss das eindeutig formulieren — andernfalls Auslegungsstreit.

### Bezugsrechtsausschluss bei Down-Rounds

Bei Down-Rounds (Pre-Money unter letztem Post-Money) ist ein Bezugsrechtsausschluss zugunsten des Lead Investors oft notwendig. Sachliche Rechtfertigung nach Kali+Salz-Grundsatz (BGHZ 71, 40) erforderlich. Das Agio in der Down-Round ist niedriger als in der Vorrunde oder Null — ein **negatives Agio ist rechtlich ausgeschlossen**, weil eine Ausgabe unter pari (Ausgabebetrag unter Nennbetrag) gegen § 9 Abs. 1 GmbHG / § 5 Abs. 2 GmbHG verstößt (Verbot der Unter-pari-Emission). Wirtschaftlich erreicht man die Verwässerung in einer Down-Round durch (i) sehr niedriges oder Null-Agio bei gleichem Nennbetrag, (ii) Ausgabe einer größeren Stückzahl neuer Geschäftsanteile zum reduzierten Preis je Anteil oder (iii) flankierende Instrumente (Wandeldarlehen, Anti-Dilution-Anpassung der bestehenden Series). Wer einem Mandanten ein negatives Agio vorschlägt, beschließt eine nichtige Kapitalerhöhung.

## Anfängerfehler im Corporate-Kontext

- Annahme Lead Investor will hohes Stammkapital. Falsch — Lead Investor will hohe Liquidation Preference und niedriges Stammkapital um spätere Rückgewähr zu erleichtern.
- Annahme das Agio ist ein steuerlicher Trick. Falsch — Agio ist zivilrechtlich begründet steuerlich nur die Erfassung folgt automatisch.
- Annahme jeder Kapitalerhöhungsbeschluss muss das Agio in der Satzung verankern. Falsch — Differenzierung nach Fälligkeit (Fall 1 nein Fall 2 ja).
- Übersetzung der Liquidation Preference auf Nennbetrag. Falsch — Bezugsgröße Ausgabebetrag.
- Versuch das Agio durch Sondervergünstigungen an einzelne Gesellschafter zu umgehen. Riskant — meist kapitalerhaltungswidrig (§ 30 GmbHG) und steuerlich als verdeckte Gewinnausschüttung qualifizierbar.

## Aktuelle Rechtsprechung

- BGH Urt. v. 15.10.2007 — II ZR 216/06 GmbHR 2008, 147 (Sachagio bei Gründung § 3 Abs. 2 GmbHG zwingend).
- BGH Urt. v. 16.02.1981 — II ZR 168/79 BGHZ 80, 129 (Sachkapitalerhöhung Beschluss mit satzungsändernder Wirkung).
- BGH Urt. v. 13.03.1978 — II ZR 142/76 BGHZ 71, 40 (Kali+Salz Bezugsrechtsausschluss).
- BFH Urt. v. 27.05.2009 — I R 53/08 BFHE 226, 500 BStBl II 2010, 1004 (Aufgeld als Anschaffungskosten).
- BFH Urt. v. 03.05.2023 — IX R 12/22 (Überpari-Emission kein § 42 AO-Missbrauch).
- Rechtsprechung: keine weitere Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht Entscheidungsform Datum Aktenzeichen und tragender Aussage verifizieren.

## Verwaltungspraxis

- UmwSt-Erlass v. 11.11.2011 BStBl. I 2011, 1314 Rn. 21.09 ff. (qualifizierter Anteilstausch und Sachagio).

## Outputs

- Term-Sheet-Markup mit Übersetzungstabelle Original Purchase Price etc.
- Memo zur Strukturierung der Kapitalerhöhung mit Empfehlung Stammkapitalhöhe und Agio-Aufteilung.
- Kapitalerhöhungsbeschluss-Entwurf für den Notar.
- Übernahmeerklärung-Entwurf je neuem Gesellschafter.
- Satzungsneufassung mit oder ohne Aufnahme des Agios je nach Fall 1 oder Fall 2.
- Steuerliche Stellungnahme zur Erfassung im Einlagekonto und zur Buchwertfortführung.
- Cap-Table-Update mit Pre-Money Post-Money und Verwässerungsrechnung.
- Closing-Checkliste mit allen Conditions Precedent (siehe corporate-kanzlei-signing-closing-conditions).

## Abgrenzung

- Gesellschaftsrechtliche Dogmatik des Agios siehe Skill agio-und-kapitalruecklage im Plugin gesellschaftsrecht.
- Bewertung des Sachagio-Gegenstands siehe Skill mittelstand-corporate-ma-transaktionsstruktur.
- Steuerliche Vertiefung siehe Plugin steuerrecht-anwalt-und-berater.
- Signing- und Closing-Mechanik siehe Skill corporate-kanzlei-signing-closing-conditions.

## Senior-Review-Gate

Kein Term-Sheet-Markup geht an den Investor Counsel bevor der Senior das Agio-Konzept abgezeichnet hat. Bei Holding-Strukturierung und qualifiziertem Anteilstausch ist ein gemeinsamer Termin mit Steuerberater Notar und Investor Counsel obligatorisch — die Schnittstellen zwischen Gesellschaftsrecht Steuerrecht Bilanzrecht und Notariat sind hier eng und fehleranfällig.
