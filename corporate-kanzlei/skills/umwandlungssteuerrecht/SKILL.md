---
name: umwandlungssteuerrecht
description: "Umwandlungssteuerrecht: Begleitet Verschmelzung, Spaltung und Formwechsel nach UmwStG auf Steuerneutralitaet, Buchwertfortführung, Sperrfristen, Verlustnutzung und Grunderwerbsteuer. Normen: §§ 11-25 UmwStG, §§ 1 ff. GrEStG, § 8c KStG."
---

# Umwandlungssteuerrecht

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Umwandlungssteuerrecht

- **Corporate-Aufgabe (Umwandlungssteuerrecht):** Begleitet Verschmelzung, Spaltung und Formwechsel nach UmwStG auf Steuerneutralitaet, Buchwertfortführung, Sperrfristen, Verlustnutzung und Grunderwerbsteuer.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Umwandlungssteuerrecht und brauche einen belastbaren nächsten Schritt."
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

### Umwandlungssteuerrecht

## Triage — klaere vor Beginn

1. Welche Umwandlungsart: Verschmelzung, Spaltung, Ausgliederung, Formwechsel?
2. Beteiligte Rechtsformen: KapGes auf KapGes, KapGes auf PersGes, PersGes auf KapGes?
3. Buchwertfortfuehrung gewuenscht (§§ 11, 20, 24 UmwStG)? Dann Antrag noetig.
4. Auslandsbezug: EU/EWR oder Drittland → § 1 IV UmwStG-Beschraenkungen?
5. Verlustvortraege bei der uebertragenden Gesellschaft? → § 12 III UmwStG; § 8c KStG Risiko?
6. Grundstuecke im uebergehenden Vermögen? → GrESt-Befreiung prüfbar (§ 6a GrEStG)?
7. Umwandlung innerhalb Konzern oder mit Dritten?

## Zentrale Normen

- **§§ 11-13 UmwStG** — Verschmelzung KapGes auf KapGes; Buchwert- oder gemeiner Wert; Antrag Buchwertfortfuehrung
- **§§ 15-16 UmwStG** — Spaltung KapGes; Aufspaltung/Abspaltung/Ausgliederung
- **§ 17 UmwStG** — Anteile an uebertragender KapGes beim Gesellschafter
- **§§ 20-23 UmwStG** — Einbringung; Anteilstausch; Buchwertfortfuehrung; Sperrfrist
- **§ 24 UmwStG** — Einbringung in Personengesellschaft
- **§ 8c KStG** — Verlustuntergang bei schaedlichem Beteiligungserwerb; Sanierungsklausel § 8c Ia KStG
- **§ 6a GrEStG** — Konzernprivileg; Befreiung von GrESt bei Umstrukturierung im Konzern
- **§ 1 II GrEStG** — Grundstuecksuebertragung bei Asset Deal; Begruendung § 1 IIa, III, IIIa GrEStG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Steuerneutralitaet: Voraussetzungen der Buchwertfortfuehrung

| Voraussetzung | Rechtsgrundlage | Prüfung |
|---|---|---|
| Antrag auf Buchwertfortfuehrung | §§ 11 I, 20 II, 24 II UmwStG | Antrag vor Abgabe Steuererklaerung; spaetestens mit Steuerklaerung für Uebertragungsjahr |
| Uebertragende Gesellschaft EU/EWR | § 1 II, IV UmwStG | Drittland-Umwandlungen ausgeschlossen |
| Betrieb/Teilbetrieb oder Anteil | §§ 20, 24 UmwStG | Einzelwirtschaftsgut reicht nicht für § 20 |
| Keine Entstrickung | §§ 11, 13 UmwStG | Deutsches Besteuerungsrecht bleibt erhalten |
| Sperrfrist eingehalten | § 22 UmwStG | 7 Jahre bei Einbringung; jaehrliche Meldepflicht |

## Sperrfrist-Management (§ 22 UmwStG)

Die 7-jaehrige Sperrfrist nach § 22 UmwStG erfordert jaehrliche Meldungen. Bei Verstos kommt es zur rueckwirkenden Besteuerung des anteiligen Einbringungsgewinns. Praxis-Checkliste:
- Datum der Einbringung notieren
- Sperrfrist-Ende = 7 Jahre nach Ablauf des Jahres der Einbringung
- Jaehrliche Meldung an Finanzamt durch Einbringenden
- Keine Weiterveraeusserung der eingebrachten Anteile vor Fristablauf ohne Steuerfolge-Analyse

## GrESt-Befreiung: § 6a GrEStG

Das Konzernprivileg befreit Umstrukturierungen im Konzern von der GrESt, wenn:
1. Herrschendes Unternehmen unmittelbar oder mittelbar zu mind. 95 % an der uebertragenden und aufnehmenden Gesellschaft beteiligt ist
2. Vorbehaltefrist: 5 Jahre vor der Umwandlung bestehende Beteiligung
3. Nachbehaltefrist: 5 Jahre Beteiligung nach der Umwandlung

Praxisproblem: Konzernumstrukturierungen können GrESt-Befreiung durch spaetere Anteilsveraeusserungen innerhalb der Nachbehaltefrist verlieren.

## Schritt-für-Schritt-Workflow

1. **Strukturplanung mit Steuerberater** — Umwandlungsart und Steueroptimierung abstimmen; LOI/Term Sheet prüfen
2. **Buchwertfortfuehrungsantrag vorbereiten** — Form und Inhalt gemäß §§ 11, 20, 24 UmwStG
3. **Verlustvortraege prüfen** — § 8c KStG Risiko bei Anteilsaenderungen; Sanierungsklausel?
4. **GrESt-Analyse** — § 6a GrEStG Konzernprivileg; Vorbehalte- und Nachbehaltefrist-Kalender
5. **Entstrickungsrisiko ausschliessen** — deutsches Besteuerungsrecht bleibt erhalten?
6. **Steuererklaerung für Uebertragungsjahr** — Antrag auf Buchwert bis Abgabe stellen
7. **Sperrfrist-Kalender anlegen** — jaehrliche Meldepflichten eintragen
8. **Post-Closing Monitoring** — Einhaltung Sperrfristen; GrESt-Nachbehaltefristen; änderungen unverzueglich analysieren

## Output-Template Umwandlungssteuer-Checkbogen

**Adressat:** Steuerberatung / Mandant — Tonfall praezise, listenorientiert

```
UMWANDLUNGSSTEUERRECHT — CHECKBOGEN
Transaktion: [DEAL-NAME]
Umwandlungsart: [Verschmelzung / Spaltung / Ausgliederung / Formwechsel]
Datum: [DATUM]

BUCHWERTFORTFUEHRUNG
[ ] § 11/20/24 UmwStG anwendbar
[ ] Antrag gestellt am: [DATUM]
[ ] EU/EWR-Gesellschaften beteiligt: [Ja/Nein]
[ ] Entstrickungsrisiko ausgeschlossen: [Ja/Nein]

SPERRFRIST (§ 22 UmwStG)
[ ] Einbringungsdatum: [DATUM]
[ ] Sperrfristende: [DATUM]
[ ] Jaehrliche Meldungen im Kalender: [Ja/Nein]

GREST-ANALYSE (§ 6a GrEStG)
[ ] Grundstueck im uebergehenden Vermoegen: [Ja/Nein]
[ ] Konzernprivileg anwendbar: [Ja/Nein]
[ ] Vorbehaltsfrist: [Von — Bis]
[ ] Nachbehaltsfrist-Ende: [DATUM]

VERLUSTVORTRAEGE (§ 8c KStG)
[ ] Verlustvortraege bei uebertragender Gesellschaft: [EUR]
[ ] Schaedlicher Beteiligungserwerb: [Ja/Nein]
[ ] Sanierungsklausel (§ 8c Ia KStG): [geprueft/nicht anwendbar]

OFFENE PUNKTE
[ ] [TODO 1: Owner, Frist]
[ ] [TODO 2: Owner, Frist]
```

## Rote Schwellen

- Buchwertantrag vergessen → Aufdeckung stiller Reserven; sofortige Besteuerung
- Sperrfrist-Verletzung ohne vorherige Steueranalyse → rueckwirkende Besteuerung 7 Jahre
- § 6a GrEStG-Nachbehaltsfrist unterschaetzt → unerwartete GrESt-Zahlung
- § 8c KStG-Risiko nicht erkannt → Verlustvortraege weg; hoehere Steuerlast
- Auslandsumwandlung ohne EWR-Bezug → keine Steuerneutralitaet möglich

## Quellen

- §§ 11-25 UmwStG; § 8c KStG; § 6a GrEStG; § 1 II GrEStG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Haritz/Menner/Bilitewski UmwStG (5. Aufl. 2019); Tipke/Lang § 17
