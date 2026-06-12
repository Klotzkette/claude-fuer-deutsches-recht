---
name: vertragsmarkup-key-issues
description: "Juristischen Markup für M&A-Vertraege und Key-Issues-Memo erstellen: Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden. Normen: §§ 305 ff. BGB (AGB-Kontrolle im B2B), Marktstandard DE/UK M&A. Prüfraster: Abweichungen vom Marktstandard, kritische Klauseln (MAC, Indemni"
---

# Vertragsmarkup und Key Issues

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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

## Prüfraster im Gutachtenstil
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

### Vertragsmarkup und Key Issues

## Triage — klaere vor Markup

1. Welcher Vertragstyp: SPA, APA, SHA, NDA, LOI, Term Sheet, GAV, TSA?
2. Mandant Kaeufer oder Verkaefer? (Markup-Perspektive)
3. Governing Law: Deutsches Recht, englisches Recht, hybrid?
4. Version: erster Entwurf (Gegenpartei) oder eigener Erstentw. der zurueckgekommen ist?
5. Schwerpunkte: Kaufpreismechanik, Haftung, Garantien, CoC, Kartellrecht?
6. Frist für Markup-Rueckgabe?

## Zentrale Normen

- **§§ 305-310 BGB** — AGB-Kontrolle; Klauseln können bei unangemessener Benachteiligung unwirksam sein
- **§ 307 BGB** — Generalklausel; Transparenzgebot; unklar formulierte Klauseln Kaeufer-nachteilig
- **§ 444 BGB** — Arglist; keine Freizeichnung möglich
- **§ 449 BGB** — Eigentumsvorbehalt
- **§ 138 BGB** — Sittenwidrigkeit bei wucheraehnlichen Haftungsausschluessen
- **§ 276 III BGB** — Haftung für Vorsatz kann nicht vertraglich ausgeschlossen werden

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
| Verjährung (Titel) | Unbegrenzt | Unbegrenzt | Verjährungsausschluss möglich |

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

1. **Kenntnis-Qualifikation auf alle Warranties** → Kaeufer: kein "Knowledge" für Titel-Warranties; nur für Business Warranties
2. **Cap = 10 % des KP** → Kaeufer: Counter-Markup auf 20-30 % mindestens; Fundamental Warranties: 100 %
3. **Verjährung 12 Monate** → Kaeufer: 24 Monate allg.; Tax 5 Jahre; Titel unbegrenzt
4. **Sandbagging: Verkaefer-Klausel** → Kaeufer: Anti-Sandbagging streichen oder Kaeufer-freundliche Formulierung einfuegen
5. **Materality-Qualifier auf alle Business Reps** → Kaeufer: "Materiality Scrape" einfuegen (für Haftungsberechnung ignoriert)
6. **Indemnity-Ausschluss bei Versicherungsleistung** → Kaeufer: bei W&I-Policy sinnvoll aber nur dann
7. **Schiedsklausel: nur an einem Ort** → sicherstellen: klar definiert, ICC/DIS, Frankfurt oder Muenchen, 3 Schiedsrichter

## Schritt-für-Schritt-Workflow

1. **Vertragstype und Kontext** — was liegt vor; Perspektive; Governing Law
2. **Gesamtlesedurchgang** — Struktur, Kernklauseln, ersten Eindruck
3. **Key-Issues-Identifikation** — Abweichungen vom Marktstandard markieren; Liste erstellen
4. **Markup erstellen** — Tracked Changes; klare Kommentare warum; nicht nur Korrektur sondern Begruendung
5. **Key Issues Memo** — Zusammenfassung der wichtigsten Punkte für Mandanten; Prioritaetsstufen: Deal-Breaker / High Priority / Negotiation Position / Market Standard
6. **Klientenfreigabe** — Mandant gibt Business-Entscheidungen frei; Anwalt setzt um
7. **Verhandlung** — Gespraeche zu allen offenen Punkten; Kompromissoptionen vorbereiten
8. **Finalversion** — Clean Copy; alle geeinigten Punkte eingearbeitet; Signaturseiten prüfen

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
 Empfehlung: 7 Jahre für Tax-Themen; unbegrenzt für Steuerhinterziehung.

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
- AGB-Kontrolle vergessen — unangemessene Klauseln können im deutschen Recht unwirksam sein
- Cap für alle Warranties gleichgesetzt — Fundamental-Warranties brauchen hoeheren oder keinen Cap
- Schiedsvereinbarung unklar — Vollstreckung im Ausland scheitert an Unwirksamkeit
- Anti-Sandbagging nicht verhandelt — bei Kaeufer-Kenntnis aus DD kein Warranty-Anspruch

## Quellen

- §§ 305-310, 307, 444, 276 III BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
