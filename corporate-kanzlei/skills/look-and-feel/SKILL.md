---
name: look-and-feel
description: "Corporate-Cowork-Design: Definiert die visuelle Oberflaeche für Partner, Counsel und Associates. Ruhig, edel, blaeulich-silbern; Orange für Entscheidungspunkte. Statuskarten, Ampeln und dichte Deal-Information statt Marketing. Keine Spielerei, keine Dekoration."
---

# Corporate-Cowork-Look — Design und Ausgabestandard

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Corporate-Cowork-Look — Design und Ausgabestandard

- **Corporate-Aufgabe (Corporate-Cowork-Look — Design und Ausgabestandard):** Definiert die visuelle Oberflaeche für Partner, Counsel und Associates. Ruhig, edel, blaeulich-silbern; Orange für Entscheidungspunkte. Statuskarten, Ampeln und dichte Deal-Information statt Marketing. Keine Spielerei, keine Dekoration.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Corporate-Cowork-Look — Design und Ausgabestandard und brauche einen belastbaren nächsten Schritt."
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

### Corporate-Cowork-Look — Design und Ausgabestandard

## Triage — kläre vor der Ausgabegestaltung

1. Wer ist der Adressat — Partner/Counsel intern, Mandant, Gegenpartei, Aufsichtsrat oder Gericht?
2. Welches Ausgabeformat ist gefordert — Deal-Karte, Statusbericht, Präsentation, Protokoll, Schriftsatz?
3. Vertraulichkeitsstufe — intern, mandantenvertraulich, nur Partner?
4. Enthält die Ausgabe rote Schwellen oder Risiken, die optisch hervorgehoben werden müssen?
5. Ist die Ausgabe für ein Board Meeting oder Gremium bestimmt, das besonders klare Struktur braucht?

## Designprinzipien

### Farbpalette

| Element | Farbe / Stil | Verwendung |
|---|---|---|
| Hintergrund Hauptfläche | Sehr helles Blaugrau (#F0F4F8) | Standardhintergrund aller Ausgaben |
| Primärtext | Tiefdunkelblau (#1A2B4A) | Fließtext, Tabelleninhalt, Überschriften |
| Akzent — Entscheidungspunkte | Warmes Orange (#E87722) | Rote Schwellen, TODO, Deadlines, Freigabe |
| Akzent — Navigation / Links | Mittelblau (#2B6CB0) | Skill-Links, Anker, Querverweise |
| Tabellenhintergrund (gerade Zeilen) | Sehr helles Blau (#EBF4FF) | Lesbarkeit bei dichten Tabellen |
| Statusampel Grün | #38A169 | Workstream auf Kurs |
| Statusampel Gelb | #D69E2E | Verzögerung, Klärungsbedarf |
| Statusampel Rot | #E53E3E | Kritisch, rote Schwelle ausgelöst |
| Vertraulich-Markierung | Orange auf Dunkelblau | Deckblatt, Kopfzeile |

### Typografie

- **Überschriften (H1-H3):** Serifenlos, Gewicht Bold/SemiBold; keine kursiven Überschriften.
- **Fließtext:** Serifenlos, Regular; Zeilenlänge max. 90 Zeichen.
- **Tabellenkopf:** Bold, Kleinschrift ODER Normalschrift mit Unterstreichung.
- **Hervorhebungen:** Fett für Norm-/Aktenzeichen und Entscheidungspunkte; kursiv nur für Zitate.
- **Zahlen / Beträge:** Tausenderpunkt (`1.000`), Dezimalkomma (`12,82 EUR`), kein Apostroph.

### Struktur und Layout

- Statuskarten bevorzugen: kompakte Tabelle mit Phase / Owner / Deadline / Risiko / Aktion.
- Kein Fließtext-Wust: maximal 3 Sätze pro Absatz; dann Tabelle oder Liste.
- Aufzählungen mit genau einem Gedanken pro Zeile; keine Schachtelsätze.
- Jeder Ausgabeblock hat eine sichtbare Überschrift (H2 oder H3).
- Deal-Karten immer mit Ampelstatus; Risikostatus immer explizit.

## Ausgabestandards nach Adressat

| Adressat | Tonfall | Länge | Besonderheit |
|---|---|---|---|
| Partner / Counsel intern | Sachlich-juristisch, präzise | Kurz bis mittel | Deal-Karte + offene Punkte; keine Erklärungen |
| Associate intern | Anleitend, strukturiert | Mittel | Workflow-Schritte; Hinweise auf Normen und Muster |
| Mandant | Verständlich-erklärend | Mittel bis lang | Kein Fachjargon ohne Erläuterung; Handlungsempfehlung klar |
| Aufsichtsrat / Gremium | Sachlich, executive | Kurz | Executive Summary zuerst; Details in Anlage |
| Gegenpartei | Sachlich oder scharf-fristsetzend | Kurz bis mittel | Keine Konzessionen außer explizit gewünscht |
| Gericht | Formal-juristisch | Variabel | Schriftsatz-Format; Anträge zuerst |

## Schritt-für-Schritt-Workflow

1. **Adressat und Format bestimmen** — Ausgabe auf Tabelle oben anpassen.
2. **Vertraulichkeitsstufe prüfen** — Deckblatt oder Kopfzeile mit Vertraulichkeitsmarkierung.
3. **Risikoelemente identifizieren** — rote Schwellen und TODO farblich abheben (Orange).
4. **Struktur aufbauen:** Executive Summary → Statusampel → Hauptinhalt → Offene Punkte → Freigabegrad.
5. **Tabellen bevorzugen** — überall wo mehr als 3 Items verglichen werden.
6. **Qualitätscheck:** Text ohne Fließtextblöcke > 5 Zeilen? Ampelstatus sichtbar? Freigabegrad angegeben?
7. **Ausgabe finalisieren** — Version, Datum, Ersteller, Freigabestatus im Footer.

## Output-Template Standardausgabe Deal-Dokument

**Adressat:** Deal-Team / Mandant (anpassen) — Tonfall sachlich-präzise
```
[VERTRAULICH — NUR FÜR INTERNE VERWENDUNG / MANDANTENVERTRAULICH]

TITEL: [Bezeichnung des Dokuments]
Mandat: [Mandatsname / Kürzel]
Datum: [TT.MM.JJJJ]
Version: [Nr.]
Ersteller: [Name, Funktion]
Freigabe: [Name, Funktion, Datum oder "ausstehend"]

─────────────────────────────────────────────────────────────
EXECUTIVE SUMMARY
[2-3 Sätze: Kernbotschaft, wichtigste Risiken, empfohlene Aktion]
─────────────────────────────────────────────────────────────

STATUSÜBERSICHT
| Workstream | Status | Owner | Nächste Aktion | Deadline |
|-----------|--------|-------|----------------|---------|
| [WS 1] | GRÜN | [Name]| [Aktion] | [Datum] |
| [WS 2] | GELB | [Name]| [Aktion] | [Datum] |
| [WS 3] | ROT | [Name]| [Aktion — DRINGEND] | [Datum] |

─────────────────────────────────────────────────────────────
HAUPTINHALT
[Abschnitte mit H2-Überschriften; Tabellen bevorzugen]
─────────────────────────────────────────────────────────────

ROTE SCHWELLEN / ENTSCHEIDUNGSPUNKTE
[ ] [Schwelle 1: Beschreibung — Owner, Frist]
[ ] [Schwelle 2: Beschreibung — Owner, Frist]

OFFENE PUNKTE (TODO)
| Nr. | Punkt | Owner | Frist | Eskalation |
|----|-------|-------|-------|------------|
| 1 | [Punkt] | [Name] | [Datum] | [Stufe] |

─────────────────────────────────────────────────────────────
Freigabegrad: [Entwurf / Freigegeben / Vertraulich]
Nächste Review: [Datum]
```

## Rote Schwellen (Design)

- Text überlappt Tabellen oder Karten → Struktur korrigieren; Tabelle in eigenem Block.
- Ampel- oder Freigabestatus fehlt → Deal-Karte unvollständig; Ampelzeile ergänzen.
- Unerklärte Farben oder dekorative Flächen ohne Informationsgehalt → entfernen; Farbe hat semantische Bedeutung.
- Fließtextblock > 5 Zeilen ohne Strukturierung → in Tabelle oder nummerierte Liste umwandeln.
- Vertraulichkeitskennzeichnung fehlt bei mandantenvertraulichem Dokument → sofort ergänzen.

## Übergabe an andere Skills

- `corporate-kanzlei-kommandocenter` — Deal-Karte im Corporate-Cowork-Format
- `corporate-kanzlei-board-paper-business-judgment` — Board Paper in diesem Design-Standard
- `corporate-kanzlei-billing-narratives` — Billing-Output gemäß Design-Standard
- `corporate-kanzlei-output-versand-signing` — Versandpaket im Corporate-Cowork-Format

## Quellen und Vertiefung

- Keine spezifischen Rechtsnormen; Design-Standard ist prozessual, nicht materiell-rechtlich.
- Referenz: Corporate-Cowork-Designsystem (`assets/templates/cowork-ma-designsystem.md`)
- Vorlagen: `assets/templates/cowork-ma-dashboard.md`, `assets/templates/workflow-statuskarte.md`
