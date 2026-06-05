---
name: handelsregisterabruf-ki-governance
description: "Handelsregisterabruf KI Governance: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Handelsregisterabruf KI Governance

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Handelsregisterabruf KI Governance** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-handelsregisterabruf` | Handelsregister-Daten abrufen und analysieren: Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister. Normen: §§ 8-15 HGB, § 9 GmbHG, §§ 67-68 AktG, GwG §§ 18-20 (Transparenzregister). Prüfraster: Gesellschafterliste, Jahresabschluesse, Prokura, Eintragungsketten, UBO-Identifikation. Output Registerauszug-Analyse, Struktur-Memo, Risikobewertung Offenlegung. Abgrenzung: Anmeldungen siehe gesellschaftsrecht-register; Zielunternehmen-Screening siehe outside-in-target-screening. |
| `corporate-kanzlei-ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Rechtliche Rahmenbedingungen für den Einsatz von KI-Werkzeugen in Kanzleien. EU-KI-VO (AI Act), BRAO-Verschwiegenheit, Mandanteninformation, Haftung, Qualitaetssicherung. Dokumentation für BJR-Schutz. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Handelsregisterabruf KI Governance**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-handelsregisterabruf`

**Fokus:** Handelsregister-Daten abrufen und analysieren: Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister. Normen: §§ 8-15 HGB, § 9 GmbHG, §§ 67-68 AktG, GwG §§ 18-20 (Transparenzregister). Prüfraster: Gesellschafterliste, Jahresabschluesse, Prokura, Eintragungsketten, UBO-Identifikation. Output Registerauszug-Analyse, Struktur-Memo, Risikobewertung Offenlegung. Abgrenzung: Anmeldungen siehe gesellschaftsrecht-register; Zielunternehmen-Screening siehe outside-in-target-screening.

# Handelsregisterabruf und -analyse

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Handelsregisterabruf und -analyse` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Handelsregisterabruf und -analyse

- **Corporate-Aufgabe (Handelsregisterabruf und -analyse):** Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Handelsregisterabruf und -analyse und brauche einen belastbaren nächsten Schritt."
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

# Handelsregisterabruf und -analyse

## Triage — klaere vor Beginn

1. Handelsregister-Abteilung: HRA (Einzelkaufleute, Personengesellschaften) oder HRB (Kapitalgesellschaften)?
2. Vollstaendiger Abruf (Chronologischer Ausdruck) oder nur aktueller Stand?
3. Transparenzregister-Abfrage erforderlich (UBO-Identifizierung)?
4. Bundesanzeiger: Jahresabschluesse hinterlegt? (Pflicht nach § 325 HGB ab einer bestimmten Groesse)
5. Auslaendische Gesellschaften: Welches Register? (UK: Companies House; FR: RCS; NL: KVK)
6. Zweck: M&A-DD, GwG-CDD, Kreditpruefung, Lieferanten-Compliance?

## Zentrale Normen

- **§§ 8-10 HGB** — Handelsregister; Eintragungsrecht und -pflicht; Oeffentlichkeit des Registers
- **§ 15 HGB** — negative Publizitaet; Dritte koennen auf den eingetragenen Inhalt vertrauen; nicht eingetragene Tatsachen koennen Dritten nicht entgegengehalten werden
- **§ 16 GmbHG** — Gesellschafterliste; eingetragener Gesellschafter gilt als legitimiert; gutglaeubiger Erwerb
- **§ 325 HGB** — Offenlegungspflicht Jahresabschluss; Fristen; Ordnungsgeldbescheid (§ 335 HGB) bei Versaeum.
- **§§ 18-20 GwG** — Transparenzregister; wirtschaftlich Berechtigter; UBO-Fiktionsfiktion (§ 20 II GwG) wenn Handelsregister-Eintragung
- **§ 9 GwG** — Abfragepflicht aus Transparenzregister bei bestimmten Pflichtigen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## HR-Ausdruck: Analysepunkte

### Fuer GmbH (HRB)
- **Gruendung:** Datum, Gruender, Stammkapital
- **Satzung/Gesellschaftsvertrag:** Aktuelle Fassung; Aenderungschronologie
- **Geschaeftsfuehrer:** Aktuelle und historische GF; Vertretungsbefugnis; § 181 BGB-Befreiung
- **Stammkapital:** Nominal; Veraenderungen (Erhoehungen, Herabsetzungen)
- **Gesellschafterliste:** Aktuell eingetragene Gesellschafter; Anteilsgroessen; Aenderungen
- **Prokuristen / Vollmachten:** Erteilte und erloeschene Prokuren
- **Satzungsaenderungen:** Chronologie; wesentliche Aenderungen

### Fuer AG (HRB)
- **Grundkapital:** Nominal; Aktienarten (Inhaber, Namenaktie, vinkuliert)
- **Vorstand:** Aktuelle Mitglieder; Einzelvertretung vs. Gesamtvertretung
- **Aufsichtsrat:** Mitglieder; Vorsitzender
- **Hauptversammlung:** Zuletzt genehmigte KE; Genehm. Kapital; Genehmigungen
- **Bekanntmachungen:** Kapitalerhoehungen; Satzungsaenderungen; HV-Beschluesse

### Red Flags im HR-Ausdruck

| Signal | Bedeutung |
|---|---|
| Haeufige GF-Wechsel (> 2x in 3 Jahren) | Managementkrise; Gesellschafterstreit |
| Kapitalherabsetzung ohne sichtbaren Grund | Verluste; Reorganisation |
| Eintragungsloeschungen | Insolvenzen, Aufloesung in Vergangenheit |
| Pfandrechte auf Anteile eingetragen | Kreditbesicherung; finanzielle Schwierigkeiten |
| Gesellschafterliste alt (> 1 Jahr) | Aenderungen nicht angemeldet; CoC-Risiko |

## Schritt-fuer-Schritt-Workflow

1. **Vollstaendigen HR-Auszug abrufen** — elektronisch via www.handelsregister.de oder beA; Kosten ca. EUR 4.50
2. **Chronologischen Ausdruck anfordern** — alle historischen Eintragungen (nicht nur aktuell)
3. **Gesellschafterliste pruefen** — aktuell? Widersprueche mit Transaktionsunterlagen?
4. **Transparenzregister abfragen** — UBO identifizieren; Fiktionswirkung pruefen (§ 20 II GwG)
5. **Bundesanzeiger-Recherche** — Jahresabschluesse; Kapitalmarktmitteilungen; Insolvenzen
6. **Prokuren-Check** — wer ist handlungsbevollmaechtig; relevant fuer Vertragsunterschriften
7. **Red Flags dokumentieren** — strukturierter Kommentar mit Handlungsempfehlungen
8. **In DD-Report einfliessen lassen** — Corporate-Workstream aufbauen

## Output-Template HR-Analyse

```
HANDELSREGISTER-ANALYSE
Gesellschaft: [FIRMA GmbH / AG]
HRB-Nummer: [Nr.] — Amtsgericht [Ort]
Abruf-Datum: [DATUM]
Chronologischer Ausdruck: [Ja / Nein]

1. BASISINFORMATIONEN
 Rechtsform: [GmbH / AG]
 Gruendungsdatum: [DATUM]
 Sitz: [ADRESSE]
 Stammkapital/Grundkapital: EUR [BETRAG]

2. AKTUELLE ORGANE
 Geschaeftsfuehrer / Vorstand:
 - [NAME, Geburtsdatum, Vertretungsbefugnis, Befreiung § 181 BGB]
 Aufsichtsrat (falls vorhanden):
 - [NAMEN]

3. GESELLSCHAFTERSTRUKTUR
 [QUELLE: Gesellschafterliste; Stand: Datum]
 - [Gesellschafter 1]: [Anteile, %]
 - [Gesellschafter 2]: [Anteile, %]

4. JAHRESABSCHLUESSE (BUNDESANZEIGER)
 Veroeffentlicht: [Jahre]
 Nicht veroeffentlicht: [Jahren] — RISIKO: § 335 HGB Ordnungsgeld

5. RED FLAGS
 [Liste; Keine wenn keine vorhanden]

6. TRANSPARENZREGISTER
 UBO: [NAME, Nationalitaet, %-Anteil oder Fiktionswirkung]

7. EMPFEHLUNG
 [Ggf. Nachforschung; GwG-Enhanced Sorgfalt; Korrekte Gesellschafterliste einfordern]
```

## Rote Schwellen

- HR-Auszug veraltet → aktuelle Eintragungslage unbekannt; Vollmachtspruefung fehlerhaft
- Gesellschafterliste nicht aktuell → UBO unklar; GwG-CDD unvollstaendig
- Keine Jahresabschluesse veroeffentlicht → § 335 HGB-Verstos; finanzielle Intransparenz
- Gesellschafterliste in den Haenden einer anderen Person als GF → Verdacht auf Treuhander-Struktur

## Quellen

- §§ 8-15 HGB; § 16 GmbHG; § 325 HGB; §§ 18-20 GwG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 2. `corporate-kanzlei-ki-governance-berufsrecht`

**Fokus:** KI-Governance und Berufsrecht: Rechtliche Rahmenbedingungen für den Einsatz von KI-Werkzeugen in Kanzleien. EU-KI-VO (AI Act), BRAO-Verschwiegenheit, Mandanteninformation, Haftung, Qualitaetssicherung. Dokumentation für BJR-Schutz.

# KI-Governance und Berufsrecht

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KI-Governance und Berufsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: KI-Governance und Berufsrecht

- **Corporate-Aufgabe (KI-Governance und Berufsrecht):** Rechtliche Rahmenbedingungen für den Einsatz von KI-Werkzeugen in Kanzleien. EU-KI-VO (AI Act), BRAO-Verschwiegenheit, Mandanteninformation, Haftung, Qualitaetssicherung. Dokumentation für BJR-Schutz.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier KI-Governance und Berufsrecht und brauche einen belastbaren nächsten Schritt."
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
- `/corporate-kanzlei:corporate-kanzlei-gesellschaftsrecht-register` - wenn Registerstand, Gesellschafterliste, Organstellung oder Vollmachtskette geprüft werden müssen.
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

# KI-Governance und Berufsrecht

## Triage — klaere vor KI-Einsatz

1. Welche KI-Werkzeuge werden eingesetzt (generative KI, Dokumentenanalyse, Recherche)?
2. Welche Mandatsdaten werden verarbeitet (anonym, pseudonymisiert, im Klartext)?
3. Werden Daten an externe Server uebertragen? (Datenschutz; Mandatsgeheimnis)
4. Muss der Mandant ueber KI-Einsatz informiert werden?
5. Wer traegt Verantwortung fuer KI-generierte Ergebnisse (Qualitatskontrolle)?
6. EU-KI-VO (AI Act): In welche Risikoklasse faellt der Anwendungsfall?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 43a BRAO** — Verschwiegenheitspflicht; mandatsrelevante Daten duerfen nicht an Dritte weitergegeben werden
- **§ 2 BORA** — Berufsrechtliche Sorgfalt; KI-Ergebnisse muessen qualitaetsgesichert werden
- **Art. 6, 9 DSGVO** — Rechtsgrundlage fuer Datenverarbeitung; besondere Kategorien; Auftragsverarbeitung (Art. 28)
- **EU-KI-VO (AI Act, Verordnung (EU) 2024/1689)** — Hochrisiko-KI-Systeme (Art. 6); verbotene KI (Art. 5); Transparenzpflichten
- **§ 93 AktG / § 43 GmbHG** — BJR: Entscheidungen auf KI-Basis muessen angemessen begruendet und kontrolliert sein

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- CCBE/BRAK Stellungnahme 2023 — Berufsrechtliche Hinweise zu KI in Kanzleien: Mandanteninformation empfohlen; keine Verarbeitung mandatsrelevanter Daten ohne Einwilligung in Drittland-KI-Dienste

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## KI-Risikoklassen (EU-KI-VO): Relevanz fuer Kanzleien

| Risikoklasse | Beispiele | Anforderungen |
|---|---|---|
| Unakzeptables Risiko (verboten) | Social Scoring; biometrische Identifizierung Echtzeit | Kein Einsatz |
| Hochrisiko (Art. 6) | Rechtspflege-Entscheidungen; Zugang zu Dienstleistungen | Konformitaetsbewertung; Registrierung; Protokollierung |
| Begrenzte Transparenz | Generative KI (Chatbots); Deepfake | Kennzeichnungspflicht; Transparenz |
| Minimales Risiko | Recherche-Werkzeuge; Textbearbeitung; Zusammenfassung | Freiwillig; keine zwingenden Pflichten |

Kanzlei-Anwendungen (Dokumentenanalyse, Rechercheassistenz): meist minimales bis begrenztes Risiko, wenn kein Endentscheid delegiert wird.

## DSGVO-Compliance fuer KI-Werkzeuge

| Pruefpunkt | Anforderung | Massnahme |
|---|---|---|
| Rechtsgrundlage | Art. 6 I DSGVO | Berechtigtes Interesse oder Einwilligung |
| Auftragsverarbeitung | Art. 28 DSGVO | AVV mit KI-Anbieter abschliessen |
| Datenuebertragung Drittland | Art. 44 ff. DSGVO | Standardvertragsklauseln (SCC); ggf. Anonymisierung |
| Auskunft Betroffener | Art. 15 DSGVO | Mandant kann Auskunft verlangen |
| Privacy by Design | Art. 25 DSGVO | Keine unnoetigen Daten; Pseudonymisierung |

## Schritt-fuer-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


1. **KI-Werkzeug evaluieren** — Anbieter; Rechenzentrum; Daten-Policies; EU-KI-VO-Einordnung
2. **AVV abschliessen** — mit Anbieter nach Art. 28 DSGVO; Drittland-SCC falls noetig
3. **Mandanteninformation** — bei Verarbeitung personenbezogener oder mandatsrelevanter Daten informieren
4. **Pseudonymisierungs-Protokoll** — Mandantennamen ersetzen; Sachverhalte entpersonalisieren bevor Eingabe in KI
5. **Qualitaetssicherung** — jedes KI-Ergebnis durch Anwalt inhaltlich pruefen; kein blindes Uebernehmen
6. **Dokumentation** — wann wurde KI eingesetzt; wie wurde Ergebnis geprueft; Akte dokumentiert
7. **Fehlerprotokoll** — bei KI-Irrtum: korrigieren; Mandant informieren; Verbesserung

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — KI-Tool-Einsatz in Kanzlei dokumentieren | Einsatz-Dokumentation nach Template unten |
| Variante A — nur Research-Einsatz ohne Mandantendaten | Vereinfachte Dokumentation; DSGVO-Risiko gering |
| Variante B — Mandantendaten werden verarbeitet | Volle Risikoanalyse; AVV und Mandantenhinweis noetig |
| Variante C — KI generiert Schriftsaetze | Pruefpflicht des Anwalts hervorheben; Haftungsklausel erwaegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template KI-Einsatzdokumentation

```
KI-EINSATZDOKUMENTATION
Mandat: [MATTER-NR.]
Aufgabe: [Beschreibung z.B. "Dokumentenanalyse 45 Vertraege im Datenraum"]
KI-Werkzeug: [WERKZEUGNAME, Anbieter, Version]
Datum: [DATUM]

VERWENDETE DATEN:
[ ] Mandatsrelevante Daten verarbeitet — Pseudonymisierung erfolgt am [DATUM]
[ ] Nur allgemeine Rechts-/Sachinformationen

AVV MIT ANBIETER: [Ja, vom DATUM / Nein, bitte nachtragen]

QUALITAETSSICHERUNG:
KI-Output reviewed von: [NAME, Funktion]
Methode: [Stichprobenpruefung X % / Vollpruefung]
Abweichungen von KI-Output: [Keine / Beschreibung der Korrekturen]

MANDANTENINFORMATION:
[ ] Mandant informiert ueber KI-Einsatz am [DATUM]
[ ] Nicht informiert — Begruendung: [Nur allg. Recherche; keine mandantenspez. Daten]

FAZIT: KI-Ergebnisse wurden angemessen geprueft; Eigenverantwortung des Anwalts gewahrt.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Rote Schwellen

- Mandatsrelevante Daten ohne AVV in Drittland-KI-Dienst → DSGVO-Verstoss; Bussgelder
- KI-Ergebnis ohne Qualitaetspruefung weitergegeben → Anwaltshaftung; § 2 BORA
- KI-gestutzte Entscheidung ohne Dokumentation → kein BJR-Schutz (§ 93 AktG)
- EU-KI-VO Hochrisiko-System ohne Konformitaetsbewertung → ab 2026 Bussgeld bis 30 Mio. EUR oder 6 % Weltumsatz

## Quellen

- § 43a BRAO; Art. 6, 9, 28 DSGVO; EU-KI-VO (EU) 2024/1689; § 93 AktG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
