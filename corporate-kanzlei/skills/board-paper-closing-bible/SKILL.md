---
name: board-paper-closing-bible
description: "Board Paper Closing Bible: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Board Paper Closing Bible

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Board Paper Closing Bible** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-board-paper-business-judgment` | Board Paper und Business Judgment Rule (§ 93 AktG, § 43 GmbHG) erstellen: Vorlage für Vorstand/Geschäftsführung/Aufsichtsrat bei M&A-Entscheidungen, Strukturwahl, Risikotransaktionen. Prüfraster: Informationsgrundlage, Entscheidungsalternativen, Interessenkonflikte, KI-Einsatztransparenz. Output strukturiertes Board Paper mit Beschlussempfehlung, Risikoabwaegung, BJR-Dokumentation. Abgrenzung: nicht für Hauptversammlungs-Beschluesse (siehe Gesellschaftsrecht-Register) und nicht für Insolvenz-Entscheidungen (siehe StaRUG-Skill). |
| `corporate-kanzlei-closing-bible-archiv` | Closing Bible und Deal-Archiv nach M&A-Closing erstellen: Mandant oder Partner benoetigt vollständige Vertragsdokumentation mit Signaturketten, Registerbelegen, Notarbestätigungen und Anlagen. Normen: SPA Deliverables-Checkliste, § 15 GmbHG, § 130 AktG. Prüfraster Vollständigkeit aller Closing-Dokumente, Versionierung, Zugriffsrechte. Output Closing Bible (PDF/ZIP), Deal-Memo, Archivierungsprotokoll. Abgrenzung: Vorstufe ist signing-closing-conditions; für Handelsregisteranmeldungen siehe gesellschaftsrecht-register. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Board Paper Closing Bible**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-board-paper-business-judgment`

**Fokus:** Board Paper und Business Judgment Rule (§ 93 AktG, § 43 GmbHG) erstellen: Vorlage für Vorstand/Geschäftsführung/Aufsichtsrat bei M&A-Entscheidungen, Strukturwahl, Risikotransaktionen. Prüfraster: Informationsgrundlage, Entscheidungsalternativen, Interessenkonflikte, KI-Einsatztransparenz. Output strukturiertes Board Paper mit Beschlussempfehlung, Risikoabwaegung, BJR-Dokumentation. Abgrenzung: nicht für Hauptversammlungs-Beschluesse (siehe Gesellschaftsrecht-Register) und nicht für Insolvenz-Entscheidungen (siehe StaRUG-Skill).

# Board Paper und Business Judgment

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Board Paper und Business Judgment` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Vorstand, Geschäftsführung und Aufsichtsrat müssen Entscheidungen auf der Grundlage angemessener Information und in gutem Glauben treffen (§ 93 Abs. 1 S. 2 AktG — Business Judgment Rule; § 43 Abs. 1 GmbHG). Ein Board Paper dokumentiert die Entscheidungsgrundlage, die geprüften Alternativen, die Risikoabwägung und die Beschlussfassung. Fehlt diese Dokumentation, kann der Vorstand/GF im Haftungsfall den safe harbour der BJR nicht in Anspruch nehmen.

## Kaltstart-Rückfragen

1. Welche Entscheidung soll getroffen werden — M&A-Transaktion, Investition, Restrukturierung, Dividende, Compliance-Maßnahme?
2. Wer ist das Entscheidungsorgan — Vorstand, GF, Aufsichtsrat, Gesellschafterversammlung?
3. Liegt ein Freigabevorbehalt des Aufsichtsrats vor (§ 111 Abs. 4 AktG; Satzung; Geschäftsordnung)?
4. Welche Informationsquellen wurden herangezogen — externe Berater, DD-Bericht, Sachverständige, interne Fachbereiche?
5. Welche Alternativen wurden ernsthaft erwogen?
6. Wurden Interessenkonflikte (§ 112 AktG, §§ 100, 105 AktG) geprüft?
7. Sind besondere Legalitätspflichten relevant — Kartellrecht, MAR/WpHG, Export-Control, Sanktionen?
8. Soll das Board Paper als Anlage zum Protokoll (§ 107 Abs. 2 AktG) gefasst werden?

## Rechtlicher Rahmen

### Business Judgment Rule

**§ 93 Abs. 1 S. 2 AktG** — Eine Pflichtverletzung liegt nicht vor, wenn das Vorstandsmitglied bei einer unternehmerischen Entscheidung vernünftigerweise annehmen durfte, auf der Grundlage angemessener Information zum Wohle der Gesellschaft zu handeln.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§ 111 Abs. 4 AktG** — Aufsichtsrat kann Vorbehaltsgeschäfte festlegen; ohne Zustimmung keine wirksame Entscheidung.

**§ 107 Abs. 2 AktG** — Vorstandsprotokolle und Unterlagen als Pflichtanlage; Aufsichtsratsprotokolle.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Board Paper / BJR-Safe-Harbour

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Entscheidungsgegenstand | Klare Definition der zu treffenden Entscheidung; Zuständigkeit (GF, Vorstand, AR, GV) | Zuständigkeit geprüft |
| 2 | Legalitätspflicht | Rechtliche Zulässigkeit der Entscheidung (Kartellrecht, MAR, Export-Control, Sanktionsrecht) | Vorabprüfung |
| 3 | Freigabevorbehalt | Satzung, GeschOVorstand, § 111 Abs. 4 AktG; AR-Zustimmung erforderlich? | Freigabeweg definiert |
| 4 | Informationsgrundlage | Welche Informationen lagen vor? Welche wurden angefordert? Berater, DD, Gutachten | Angemessene Information dokumentiert |
| 5 | Interessenkonflikt | Nahestehende Personen; Eigengeschäfte; § 112 AktG AR-Vertretung | Konflikt dokumentiert oder verneint |
| 6 | Alternativen | Mindestens 2 ernsthafte Alternativen inkl. Status quo erwogen | Alternatives dargestellt |
| 7 | Risikoabwägung | Chancen, Risiken, Wahrscheinlichkeiten; Priorisierung; Restrisiko | Risikoanalyse |
| 8 | Empfehlung | Klare Handlungsempfehlung mit Begründung; Verantwortlicher (Owner) | Empfehlung dokumentiert |
| 9 | Protokoll / Anlage | Board Paper als Anlage zum Protokoll; Datum, Version, Unterschrift | § 107 Abs. 2 AktG |
| 10 | Wiedervorlage / Follow-up | Monitoring-Plan; Eskalationsschwellen; nächster Review-Termin | Kontrollfunktion |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Angemessene Information | GF / Vorstand (trägt nach § 93 Abs. 2 S. 2 AktG Beweislast für BJR-Voraussetzungen) | Board Paper, Beratermandate, DD-Berichte, Protokolle |
| Interessenkonflikt bestand nicht | GF / Vorstand | Offenlegungs-Dokumentation; Sitzungsprotokoll |
| Freigabe AR vorhanden | GF / Vorstand | AR-Protokoll; Umlaufbeschluss; Genehmigungsdokument |

## Standardausgabe Board Paper

```
BOARD PAPER
Entscheidungsvorlage [Nr.]
Gesellschaft: [Name]
Datum: [Datum]
Vertraulichkeitsstufe: [Intern / Streng vertraulich]
Organ: [Vorstand / Geschäftsführung / Aufsichtsrat]

1. EXECUTIVE SUMMARY
 Empfehlung: [Handlungsempfehlung in 2–3 Sätzen]
 Entscheidungsbedarf bis: [Datum]
 Freigabeerfordernis: [AR-Zustimmung / keine / GV-Beschluss]

2. SACHVERHALT
 [Ausgangssituation; Anlass; wesentliche Fakten]

3. RECHTLICHE RAHMENBEDINGUNGEN
 [Normen; Zustimmungsvorbehalte; Legalitätsrisiken]

4. ALTERNATIVEN
 | Alternative | Vorteile | Nachteile | Risikobewertung |
 |-------------|----------|-----------|-----------------|
 | A: [Option] | [Pro] | [Con] | [Hoch/Mittel/Niedrig] |
 | B: [Option] | [Pro] | [Con] | [Hoch/Mittel/Niedrig] |
 | C: Status quo | [Pro] | [Con] | [Hoch/Mittel/Niedrig] |

5. INFORMATIONSGRUNDLAGE
 - Externe Berater: [Kanzlei, Mandat-Nr., Datum]
 - DD-Bericht: [Titel, Version, Datum]
 - Interne Fachbereiche: [Bericht, Datum]
 - Gutachten: [Gutachter, Datum]
 [Hinweis auf KI-Nutzung bei Analyse sofern eingesetzt:
 Tool, Zweck, Plausibilisierung durch wen]

6. RISIKEN UND RISIKOABWÄGUNG
 | Risiko | Eintrittswahrsch. | Schaden | Minderung |
 |--------|-------------------|---------|-----------|
 | [Risiko 1] | [%] | [EUR] | [Maßnahme] |

7. EMPFEHLUNG
 [Klare Empfehlung mit Begründung]
 Owner: [Name/Funktion]
 Zeitplan: [Meilensteine]

8. OFFENE PUNKTE (TODO)
 | Nr. | Punkt | Owner | Frist | Eskalation |
 |----|-------|-------|-------|------------|
 | 1 | [Punkt] | [Name] | [Datum] | [Stufe] |

9. ANLAGEN
 - [Anlage 1: Beschreibung]
 - [Anlage 2: Beschreibung]

Erstellungsdatum: [Datum]
Version: [Nr.]
Ersteller: [Name, Funktion]
Freigabe (AR/GV): [Datum, Protokoll-Nr.]
```

## Rote Schwellen

- Entscheidungsvorlage ohne dokumentierte Informationsgrundlage → BJR-Safe-Harbour entfällt.
- Freigabevorbehalt nicht beachtet → Entscheidung unwirksam oder anfechtbar.
- Interessenkonflikt nicht offengelegt → § 112 AktG, Treuepflichtverletzung.
- Legalitätspflicht nicht geprüft (Kartellrecht, MAR, Sanktionen) → persönliche Haftung.
- KI-Analyse ohne menschliche Plausibilisierung durch Fachmann → keine angemessene Information.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Eilentscheidung ohne AR-Genehmigung | Nachträgliche Genehmigung sicherstellen; Umlaufbeschluss; Notfall-Ausnahme in GeschO verankern |
| Interessenkonflikt bei GF | Enthaltung; AR oder GV entscheidet; § 112 AktG AR-Vertretung bei Vorstandssache |
| Externe Berater wurden herangezogen | Beratermandate und Berichte stets in Board Paper dokumentieren und als Anlage beifügen |
| DD-Bericht zeigt erhebliche Risiken | Risikodarstellung im Board Paper verpflichtend; Restrisiko-Entscheidung explizit dokumentieren |

## Übergabe an andere Skills

- `corporate-kanzlei-transaktionsstruktur` — Strukturoptionen für Board Paper zu M&A-Entscheidungen
- `corporate-kanzlei-restructuring-starug-insolvenzplan` — Restrukturierungsentscheidungen Board Paper
- `corporate-kanzlei-outside-in-target-screening` — Vorab-Analyse als Informationsgrundlage

## Quellen

- AktG §§ 93, 107, 111, 112
- GmbHG § 43
- MAR / WpHG (Insiderrecht)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 2. `corporate-kanzlei-closing-bible-archiv`

**Fokus:** Closing Bible und Deal-Archiv nach M&A-Closing erstellen: Mandant oder Partner benoetigt vollständige Vertragsdokumentation mit Signaturketten, Registerbelegen, Notarbestätigungen und Anlagen. Normen: SPA Deliverables-Checkliste, § 15 GmbHG, § 130 AktG. Prüfraster Vollständigkeit aller Closing-Dokumente, Versionierung, Zugriffsrechte. Output Closing Bible (PDF/ZIP), Deal-Memo, Archivierungsprotokoll. Abgrenzung: Vorstufe ist signing-closing-conditions; für Handelsregisteranmeldungen siehe gesellschaftsrecht-register.

# Closing Bible und Archiv

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Closing Bible und Archiv` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Closing Bible und Archiv

- **Corporate-Aufgabe (Closing Bible und Archiv):** Mandant oder Partner benoetigt vollständige Vertragsdokumentation mit Signaturketten, Registerbelegen, Notarbestätigungen und Anlagen.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Closing Bible und Archiv und brauche einen belastbaren nächsten Schritt."
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

# Closing Bible und Archiv

## Triage — klaere vor Beginn

1. Welche Dokumente bilden die Closing Bible (SPA, Anlagen, Disclosure Letter, Closing Certificate, Anmeldungen)?
2. Elektronisch signiert (qualifizierte elektronische Signatur) oder handschriftlich?
3. Gibt es notarielle Dokumente (GmbH-Anteilsuebertragung), die im Original vorliegen muessen?
4. Wer archiviert das Original: Kanzlei, Mandant, Notar, gemeinsam?
5. Vertraulichkeitsstufe und Zugriffskonzept: need-to-know?
6. Ist eine Long-Term-Archivierung vertraglich vereinbart (z.B. 10 Jahre)?

## Zentrale Normen & Anforderungen

- **§ 199 BGB** — Verjährungsbeginn 31.12.; bei Warranty-Verletzung oft 18-24 Monate ab Closing oder Kenntnis
- **§§ 257 f. HGB** — Aufbewahrungspflicht Handelsbuecher 10 Jahre; Geschaeftsbriefe 6 Jahre
- **§ 147 AO** — steuerliche Aufbewahrungspflicht bis zu 10 Jahre
- **§ 15 IV GmbHG** — notariell beurkundete Anteilsuebertragung; Original beim Notar; Ausfertigung an Kanzlei
- **GoB / GoBD** — ordnungsgemaesse Buchfuehrung; elektronische Archivierung muss unveraenderbar sein (revisionssichere Aufbewahrung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Closing Bible: Standard-Inhaltsverzeichnis

| Nr. | Dokument | Datum | Version | Signatur | Fundstelle |
|---|---|---|---|---|---|
| 1 | Share Purchase Agreement | [Datum] | Final | Handschriftlich / eSign | Tab 1 |
| 2 | Disclosure Letter | [Datum] | Final | [Unterzeichner] | Tab 2 |
| 3 | Anteilsuebertragungsvertrag / Notarielle Beurkundung | [Datum] | Original | Notar [Name] | Tab 3 |
| 4 | Closing Certificate Verkaefer | [Datum] | — | [GF-Name] | Tab 4 |
| 5 | Bring-Down Certificate | [Datum] | — | [GF-Name] | Tab 5 |
| 6 | Resignationsschreiben Organmitglieder | [Datum] | — | [Namen] | Tab 6 |
| 7 | Kartellfreigabe | [Datum] | Behoerdl. Original | Bundeskartellamt | Tab 7 |
| 8 | FDI-Nichtuntersagung | [Datum] | — | BMWK | Tab 8 |
| 9 | CoC-Consents | [Datum] | — | [Vertragspartner] | Tab 9 |
| 10 | SWIFT-Bestaetigung Kaufpreiszahlung | [Datum] | — | Bank | Tab 10 |
| 11 | Gesellschafterliste (aktualisiert) | [Datum] | HR-Version | Notar | Tab 11 |
| 12 | Handelsregisterauszug post-Closing | [Datum] | — | HR-Gericht | Tab 12 |
| 13 | W&I-Versicherungspolice | [Datum] | — | Versicherer | Tab 13 |

## Schritt-fuer-Schritt-Workflow

1. **Deliverables-Liste finalisieren** — alle CP-Checklisten-Punkte sind Basis der Closing Bible
2. **Pre-Closing-Review** — einen Tag vor Closing alle vorbereiteten Dokumente pruefen; fehlende Signaturen anmahnen
3. **Closing-Meeting** — gleichzeitiger Austausch; jedes Dokument gegen Index abgehakt
4. **Offene Punkte post-Closing** — Handelsregisteranmeldung; HR-auszug; ggf. ausstehende Consents
5. **Closing Bible zusammenstellen** — digitale und physische Version; Index und Tabs; versioniert
6. **Intern verteilen** — Mandant (Leitung/GF), Kanzlei-Akte, Steuerberater (relevante Teile), Notar (seine Stuecke)
7. **Archivierungskonzept umsetzen** — GoBD-konforme elektronische Archivierung; Zugriffsschutz; Backup
8. **Fristeninformation** — Verjährungsfristen fuer Warranties (Closing + Laufzeit); im Kalender eintragen

## Output-Template Closing-Bestaetigungs-Protokoll

**Adressat:** Beide Parteien — Tonfall sachlich, abschliessend dokumentierend

```
CLOSING-PROTOKOLL
Transaktion: [DEAL-NAME]
Closing-Datum und -Uhrzeit: [DATUM, UHRZEIT]
Ort: [KANZLEI / NOTARIAT / VIDEOKONFERENZ]

ANWESENDE PARTEIEN:
Verkaefer: [NAME, VERTRETER, KANZLEI]
Kaeufer: [NAME, VERTRETER, KANZLEI]
Notar: [NAME] (soweit anwesend)

DOKUMENTENUEBERGABE — STATUS:
[x] SPA (Execution Copy) — ubergeben
[x] Disclosure Letter — ubergeben
[x] Anteilsuebertragungsvertrag — beurkundet am [Datum] durch Notar [Name]
[x] Closing Certificate Verkaefer — ubergeben
[x] Kartellfreigabe — ubergeben (Datum Bescheid: [Datum])
[x] FDI-Nichtuntersagung — ubergeben
[x] Kaufpreiszahlung SWIFT — erhalten; Betrag: [EUR]
[x] Gesellschafterliste aktualisiert — eingereicht bei Notar

HANDELSREGISTERANMELDUNG:
Eingereicht am: [Datum] durch Notar [Name], URNr. [Nr.]
Voraussichtliche Eintragung: [Datum]

OFFENE PUNKTE NACH CLOSING:
| Nr. | Punkt | Owner | Frist |
|-----|-------|-------|-------|
| 1 | [Punkt] | [Name] | [Datum] |

Erstellt von: [KANZLEI]
```

## Rote Schwellen

- Closing Bible fehlt Signaturseiten oder Anlagen → juristisch angreifbares Exemplar
- Keine revisionssichere Archivierung → GoBD-Verstoss; steuerliche Aufbewahrungspflicht verletzt
- Verjährungsfristen nicht im Kalender → unbemerkte Praeklusion von Warranty-Anspruechen
- Originaldokumente beim Notar nicht abgeholt oder Ausfertigung nicht gesichert
- Kaeufer-Mandate erhalt keine vollstaendige Kopie → Beweisproblem bei Warranty-Streit

## Quellen

- § 199 BGB; §§ 257 f. HGB; § 147 AO; § 15 IV GmbHG; GoBD
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 12
