---
name: regulatory-fdi-restructuring-starug
description: "Regulatory FDI Restructuring Starug: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Regulatory FDI Restructuring Starug

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Regulatory FDI Restructuring Starug** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-regulatory-fdi-merger-control` | Anmeldepflichten Fusionskontrolle und FDI prüfen: M&A-Transaktion erfordert Clearance. Normen: §§ 35 ff. GWB (deutsches Fusionskontrollrecht), Art. 1 ff. FKVO (EU-Fusionskontrolle), AWG/AWV (Investitionsprüfung), SektSchV (Sektorschutz), TKG, EnWG. Prüfraster: Umsatzschwellen, Marktanteile, Vollzugsverbot § 41 GWB, FDI-Meldepflichten nach AWV § 56 ff. Output Regulatory-Memo, Melde-Zeitplan, CP-Tracker. Abgrenzung: Kartellrecht laufende Verfahren siehe kartellrecht-Skill; Vollzugsbedingungen siehe signing-closing-conditions. |
| `corporate-kanzlei-restructuring-starug-insolvenzplan` | StaRUG-Restrukturierungsplan und Insolvenzplan für distressed Unternehmen: Schuldner oder Berater plant außergerichtliche Sanierung oder Insolvenzplanverfahren. Normen: §§ 7 ff. StaRUG (Planarchitektur), §§ 217 ff. InsO (Insolvenzplan), §§ 21 ff. StaRUG. Prüfraster: Gläubiger-Gruppen, Planbetroffenheit, Mehrheitserfordernisse, Cram-Down, Schlechterstellungsverbot § 30 StaRUG. Output Restrukturierungsplan-Entwurf, Gruppenbildungs-Memo, Zeitplan. Abgrenzung: Krisenfrueherkennung siehe krisenfrueherkennung-starug-Plugin; Distressed M&A siehe distressed-ma. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Regulatory FDI Restructuring Starug**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-regulatory-fdi-merger-control`

**Fokus:** Anmeldepflichten Fusionskontrolle und FDI prüfen: M&A-Transaktion erfordert Clearance. Normen: §§ 35 ff. GWB (deutsches Fusionskontrollrecht), Art. 1 ff. FKVO (EU-Fusionskontrolle), AWG/AWV (Investitionsprüfung), SektSchV (Sektorschutz), TKG, EnWG. Prüfraster: Umsatzschwellen, Marktanteile, Vollzugsverbot § 41 GWB, FDI-Meldepflichten nach AWV § 56 ff. Output Regulatory-Memo, Melde-Zeitplan, CP-Tracker. Abgrenzung: Kartellrecht laufende Verfahren siehe kartellrecht-Skill; Vollzugsbedingungen siehe signing-closing-conditions.

# Regulatory, FDI und Fusionskontrolle

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Regulatory, FDI und Fusionskontrolle` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Regulatory, FDI und Fusionskontrolle

- **Corporate-Aufgabe (Regulatory, FDI und Fusionskontrolle):** M&A-Transaktion erfordert Clearance.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Regulatory, FDI und Fusionskontrolle und brauche einen belastbaren nächsten Schritt."
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

# Regulatory, FDI und Fusionskontrolle

## Triage — klaere vor Beginn

1. Umsatzschwellen erreicht? → Bundeskartellamt (§§ 35 ff. GWB) oder EU-Kommission (Art. 1 FKVO)?
2. Auslaendischer Erwerber aus Nicht-EU-Land? → AWG/AWV-Investitionspruefung pruefen
3. Branche: Ruestung, Verteidigung, Kritische Infrastruktur, Medien, Gesundheit, Cloud? → SektSchV oder besondere Pruefpflichten
4. Timeline: Vollzugsverbot (Standstill Obligation) bis Freigabe; Gunst-Jumping-Risiko?
5. Mehrere Jurisdiktionen (USA HSR Act, UK NSI Act, China SAMR)? → Multijurisdiktioneller Koordinationsbedarf
6. FDI-Screening: Meldepflicht oder nur Pruefmoeglichkeit des BMWK?

## Zentrale Normen

- **§§ 35-43 GWB** — Zusammenschlusskontrolle; Aufgreifschwellen; Anmeldepflicht
- **§ 36 GWB** — Untersagungsvoraussetzungen; erhebliche Behinderung wirksamen Wettbewerbs
- **§ 41 GWB** — Vollzugsverbot; bis zur Freigabe kein Vollzug; Bussgeld bis 10 % Weltumsatz
- **Art. 1-21 FKVO (EG) 139/2004** — EU-Fusionskontrolle; Aufgreifschwellen; Alleinzustaendigkeit
- **§§ 55 ff. AWG i.V.m. §§ 55 ff. AWV** — Aussenhandelsgesetz; Investitionspruefung
- **SektSchV (Sicherheitsueberprueefungsverordnung)** — Sektoren Kritische Infrastruktur; KRITIS-Unternehmen
- **§ 56 AWV** — Meldefrist 2 Monate ab sicherem Abschluss; Erwerb ab 10 % bei kritischen Sektoren
- **Verordnung (EU) 2019/452** — EU-FDI-Screening-Rahmen; nationale Stellen melden an EU-Kommission

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Fusionskontrolle: Aufgreifschwellen

### Bundeskartellamt (§ 35 GWB)
- Kombinierter Weltumsatz aller Beteiligten > 500 Mio. EUR UND
- Mindestens ein Beteiligter > 25 Mio. EUR Inlandsumsatz UND
- Ein weiterer Beteiligter > 5 Mio. EUR Inlandsumsatz
- ODER: 3. Aufgreifschwelle: Kaufpreis > 400 Mio. EUR + erhebliche Inlandstaetigkeit (§ 35 Ia GWB)

### EU-Kommission (Art. 1 FKVO)
- Tier 1: Weltumsatz > 5 Mrd. EUR + EU-Umsatz > 250 Mio. EUR fuer mind. zwei Beteiligte
- Tier 2: Weltumsatz > 2.5 Mrd. EUR + EU-Umsatz > 100 Mio. EUR in mind. drei Mitgliedstaaten

### Vollzugsverbot (§ 41 GWB / Art. 7 FKVO)
Kein Vollzug bis zur Freigabe oder Ablauf der Pruefdauer. Ausnahme: vorherige Genehmigung (Dispensantrag).

## FDI-Screening (AWG/AWV): Sektoren und Schwellen

| Sektor | Aufgreifschwelle | Rechtsgrundlage |
|---|---|---|
| Kritische Infrastruktur (Energie, Wasser, IT, Verkehr) | 10 % Stimmrechte | § 56 AWV |
| Medien | 10 % | § 56 AWV |
| Gesundheit / Pharma | 10 % | § 56 AWV |
| Verteidigung / Ruestung | 10 % | § 60 AWV; SektSchV |
| KI / autonome Fahrzeuge / Robotik | 10 % | § 56 Ia AWV |
| Sonstige Unternehmen | 25 % | § 55 AWV |

Meldefrist: 2 Monate nach Vertragsschluss. Pruefdauer: 4 Monate (verlaengerbar).

## Schritt-fuer-Schritt-Workflow

1. **Schwellentest** — Umsatzzahlen beider Parteien errechnen; GWB/FKVO/Drittlaender-Schwellen pruefen
2. **FDI-Check** — Nationalitaet des Erwerbers; Sektor der Zielgesellschaft; AWV-Schwellen
3. **Timeline festlegen** — Anmeldezeitpunkt (post-Signing); Pruefdauer Phase I (4 Wochen GWB; 25 Werktage FKVO)
4. **Gun-Jumping-Protokoll** — Informationsaustausch beschraenken bis Freigabe; Clean Team wenn noetig
5. **Anmeldungsformulare** — Bundeskartellamt: Formular A/B; EU-Kommission: Form CO/Short Form
6. **Pre-notification Contacts** — informelle Voranfrage bei Behoerde; Zeitplan abklaeren
7. **Anmeldung einreichen** — mit vollstaendigen Informationen; Kooperationspflicht
8. **Phase-II-Risiko bewerten** — wenn Bedenken: Abhilfemassnahmen (Auflagen) verhandeln
9. **Freigabe-Erlangung dokumentiert** → dann Closing freigeben

## Entscheidungsbaum: Zustaendigkeit

```
Umsaetze erreichen EU-Schwellen (FKVO Tier 1 oder 2)?
 → Ja: EU-Kommission zustaendig (One-Stop-Shop)
 → Ausnahme: Art. 9 FKVO Verweisung an nationale Behoerde beantragt?
 → Nein: GWB-Schwellen erreicht?
 → Ja: Bundeskartellamt; ggf. simultane Nicht-EU-Anmeldungen
 → Nein: Keine Anmeldepflicht — trotzdem FDI-Screening pruefen!
```

## Output-Template Regulatory-Memo

**Adressat:** Deal-Team / Mandant — Tonfall praezise, entscheidungsorientiert

```
REGULATORY MEMO — FUSIONSKONTROLLE UND FDI
Transaktion: [DEAL-NAME]
Datum: [DATUM]

1. FUSIONSKONTROLLE
 GWB-Schwellen: [Erreicht Ja/Nein; Details]
 FKVO-Schwellen: [Erreicht Ja/Nein; Details]
 Drittlaender-Anmeldungen: [USA HSR / UK / China / Sonstige]
 Vollzugsverbot: [Ja/Nein; ab wann aufgehoben]
 Erste-Phase-Dauer: [X Wochen]

2. FDI-SCREENING
 Erwerber-Nationalitaet: [Land]
 Zielsektor: [Sektor; AWV-Schwelle]
 Meldefrist: [Datum]
 Genehmigungspflicht: [Ja/Nein/Unsicher]

3. TIMELINE
 | Meilenstein | Datum | Zustaendigkeit |
 |------------|-------|---------------|
 | Signing | [Datum] | Deal-Team |
 | Anmeldung | [Datum] | Kartellrecht-Team |
 | Phase-I-Frist | [Datum] | Behoerde |
 | Voraussichtliches Closing | [Datum] | Alle |

4. EMPFEHLUNG
 [Strategie; Auflagen-Risiko; Zeitplan-Risiken]
```

## Rote Schwellen

- Vollzugsverbot missachtet — Gun Jumping; Bussgeld bis 10 % Weltumsatz
- FDI-Meldefrist verpasst (2 Monate nach Vertragsschluss) → BMWK kann nachtraegliche Untersagung erwaegen
- Phase-II-Risiko unterschaetzt → Closing verzoegert sich 6-18 Monate
- Drittland-Anmeldungen (USA, China) vergessen → Separates Vollzugsverbot in diesen Laendern
- SektSchV-Pruefung bei Ruestungsunternehmen vergessen → Genehmigungspflicht verpasst

## Quellen

- §§ 35-43 GWB; Art. 1-21 FKVO (EG) 139/2004; §§ 55, 56, 60 AWV; Verordnung (EU) 2019/452
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Immenga/Mestmaecker GWB (6. Aufl. 2020) §§ 35 ff.; Ohler AWG/AWV (2021)

## 2. `corporate-kanzlei-restructuring-starug-insolvenzplan`

**Fokus:** StaRUG-Restrukturierungsplan und Insolvenzplan für distressed Unternehmen: Schuldner oder Berater plant außergerichtliche Sanierung oder Insolvenzplanverfahren. Normen: §§ 7 ff. StaRUG (Planarchitektur), §§ 217 ff. InsO (Insolvenzplan), §§ 21 ff. StaRUG. Prüfraster: Gläubiger-Gruppen, Planbetroffenheit, Mehrheitserfordernisse, Cram-Down, Schlechterstellungsverbot § 30 StaRUG. Output Restrukturierungsplan-Entwurf, Gruppenbildungs-Memo, Zeitplan. Abgrenzung: Krisenfrueherkennung siehe krisenfrueherkennung-starug-Plugin; Distressed M&A siehe distressed-ma.

# StaRUG und Insolvenzplan

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `StaRUG und Insolvenzplan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Das Gesetz über den Stabilisierungs- und Restrukturierungsrahmen für Unternehmen (StaRUG, in Kraft seit 01.01.2021) eröffnet Unternehmen in drohender Zahlungsunfähigkeit (§ 18 InsO) ein vorinsolvenzliches Sanierungsverfahren ohne öffentliche Bekanntmachung. Der Restrukturierungsplan kann Gläubiger mehrheitlich binden, ohne dass Einzelne zustimmen müssen. Der Insolvenzplan nach §§ 217 ff. InsO bietet ein ähnliches Instrument im eröffneten Insolvenzverfahren. Beide Instrumente sind zentrales Handwerkszeug bei Distressed-M&A-Transaktionen. Entscheidend ist die korrekte Klasseneinteilung der Planbetroffenen, die Erreichung der Mehrheiten und die Beherrschung der Zeitachse — Führungskräfte haften persönlich, wenn Antragspflichten (§§ 15a, 15b InsO) missachtet werden.

## Kaltstart-Rückfragen

1. Liegt drohende Zahlungsunfähigkeit (§ 18 InsO) vor, oder besteht bereits Zahlungsunfähigkeit (§ 17 InsO) oder Überschuldung (§ 19 InsO)?
2. Welche Instrumente des StaRUG wurden oder sollen genutzt werden — Restrukturierungsplan, Stabilisierungsanordnung, Moratorium, Planbestätigung durch Gericht?
3. Welche Gläubiger sind planbetroffene Parteien, und wie werden die Klassen gebildet (§ 9 StaRUG)?
4. Welche Mehrheiten sind in den einzelnen Klassen realistisch erreichbar? Gibt es Sperrminoritäten?
5. Besteht Insolvenzantragspflicht nach § 15a InsO — wer ist zur Antragstellung verpflichtet (GmbH-Geschäftsführer, Vorstand)?
6. Ist eine Distressed-M&A-Transaktion geplant — Insolvenzplan mit übertragendem Restrukturierungsträger oder Unternehmensverkauf aus der Insolvenz?
7. Welche Sicherheiten (Grundpfandrechte, Pfandrechte, Sicherungsübereignung) bestehen, und wie wirken sie auf die Klassenbildung?
8. Welcher Zeitplan ist für den Plan realistisch — Abstimmungstermin, Gerichtsbestätigung, Vollzug?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte

| Norm | Regelungsinhalt (Auszug) |
|---|---|
| §§ 1–93 StaRUG | Stabilisierungs- und Restrukturierungsrahmen: Restrukturierungsplan, Anzeigepflicht, Planbetroffenheit, Klasseneinteilung, Abstimmung, Bestätigung, Stabilisierungsanordnung |
| § 18 InsO | Drohende Zahlungsunfähigkeit: Schuldner wird voraussichtlich nicht in der Lage sein, bestehende Verbindlichkeiten bei Fälligkeit zu erfüllen (Prognosezeitraum 24 Monate bei StaRUG) |
| § 17 InsO | Zahlungsunfähigkeit: Schuldner ist nicht in der Lage, fällige Verbindlichkeiten zu erfüllen (Faustregel: Liquiditätslücke > 10 % über 3 Wochen) |
| § 19 InsO | Überschuldung: Vermögen deckt Verbindlichkeiten nicht, außer bei positiver Fortführungsprognose |
| § 15a InsO | Insolvenzantragspflicht: Geschäftsführer/Vorstand der haftungsbeschränkten Gesellschaft; Frist 6 Wochen (Überschuldung) bzw. 3 Wochen (Zahlungsunfähigkeit) |
| § 15b InsO | Zahlungsverbote nach Insolvenzreife; Haftung für masseschmälernde Zahlungen |
| §§ 217–269 InsO | Insolvenzplan: Gestaltender Teil, erläuternder Teil, Planbetroffene, Klassenbildung, Abstimmung, Bestätigung, Aufhebung des Verfahrens |
| § 245 InsO | Obstruktionsverbot: Planzustimmung einer Klasse kann bei Schlechterstellungsverbot ersetzt werden |
| § 251 InsO | Minderheitenschutz: Einzelner Gläubiger kann Bestätigung ablehnen, wenn er durch Plan schlechter gestellt wird als bei Liquidation |

### Leitentscheidungen

| Gericht | Az. | Datum | Leitsatz (kurz) |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Krisenphase bestimmen | Drohende Zahlungsunfähigkeit (§ 18 InsO), Zahlungsunfähigkeit (§ 17), Überschuldung (§ 19)? | Krisenphase dokumentiert |
| 2 | Antragspflicht prüfen | § 15a InsO: Frist läuft? Wer ist verpflichtet? Droht persönliche Haftung nach § 15b InsO? | Pflicht-Status klar |
| 3 | StaRUG vs. InsO-Plan abwägen | Öffentlichkeit, Zeitplan, Kontrolle, Gläubigerbreite, M&A-Optionen vergleichen | Instrument gewählt |
| 4 | Restrukturierungsanzeige (StaRUG) | Anzeige beim zuständigen Restrukturierungsgericht (§ 31 StaRUG); Voraussetzungen: § 18 InsO | Anzeige erstattet |
| 5 | Planbetroffenheit definieren | Welche Gläubiger werden in den Plan einbezogen? Ausnahmen: dinglich gesicherte Gläubiger, operative Lieferanten, Arbeitnehmer? | Planbetroffene Liste |
| 6 | Klassenbildung | § 9 StaRUG / § 222 InsO: getrennte Klassen nach Rechtsstellung und Interessen; Absonderungsberechtigte, ungesicherte, nachrangige Gläubiger | Klasseneinteilung steht |
| 7 | Mehrheiten berechnen | § 25 StaRUG: 75 % der Stimmen je Klasse; § 244 InsO: 50 % der Köpfe und 50 % der Forderungen je Klasse | Mehrheits-Prognose erstellt |
| 8 | Obstruktionsverbot prüfen | § 26 StaRUG / § 245 InsO: ablehnende Klasse überstimmbar, wenn Plan fair und diskriminierungsfrei | Obstruktionsfall bewertet |
| 9 | Minderheitenschutz (§ 251 InsO) | Einzelner Gläubiger darf durch Plan nicht schlechter stehen als bei Liquidation; Vergleichsrechnung nötig | Liquidationswert ermittelt |
| 10 | Stabilisierungsanordnung | § 49 StaRUG: Vollstreckungsschutz für bis zu 3 Monate; Voraussetzungen und Verlängerung | Moratorium beantragt |
| 11 | Distressed M&A einbetten | Übertragende Sanierung (Asset Deal), ESUG-Eigenverwaltung, Debt-to-Equity-Swap; Timing im Planrahmen | M&A-Pfad fixiert |
| 12 | Planannahme durch Gericht | Gerichtliche Planbestätigung nach § 60 StaRUG / § 248 InsO; Versagungsgründe prüfen | Bestätigung vorbereitet |
| 13 | Steuerliche Behandlung | Sanierungsgewinn (§ 3a EStG, § 7b GewStG): Steuerfreistellung und Steuerminderungsfolge für Verlustvorträge; Finanzbehörde einbinden | Steuer-Clearance besorgt |
| 14 | Vollzug und Monitoring | Plan-Implementierung, Restrukturierungsbeauftragter, Reporting, Covenants | Vollzugsplan steht |
| 15 | Dokumentation und Eskalation | Deal-Karte aktualisieren; Haftungsrisiken Geschäftsführung dokumentieren; Senior Review | Dokumentation abgeschlossen |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Drohende Zahlungsunfähigkeit (§ 18 InsO) | Schuldner (Antragsteller) | Liquiditätsplanung, Finanzmodell, Gutachter |
| Zahlungsunfähigkeit / Überschuldung (§§ 17, 19 InsO) | Insolvenzverwalter / Gläubiger | Bilanz, BWA, Bankkonten, SuSa |
| Schlechterstellung durch Plan (§ 251 InsO) | Gläubiger (Widerspruchsführer) | Liquidationsrechnung, Sachverständigengutachten |
| Vorsatz bei Antragsverschleppung (§ 15a InsO) | Staatsanwaltschaft / Insolvenzkläger | Protokolle, E-Mails, Buchhaltung, Zeugen |
| Kenntnis des Erwerbers bei Anfechtung | Insolvenzverwalter | Korrespondenz, Due-Diligence-Protokoll |

## Fristen und Verjährung

| Fristtyp | Dauer | Norm | Hinweise |
|---|---|---|---|
| Antragspflicht bei Zahlungsunfähigkeit | 3 Wochen | § 15a Abs. 1 InsO | Strafbarkeit nach § 15a Abs. 4 InsO |
| Antragspflicht bei Überschuldung | 6 Wochen | § 15a Abs. 1 InsO | Verlängerung seit COVID-Gesetzgebung wieder zurückgenommen |
| StaRUG-Anzeige: Laufzeit Restrukturierungsrahmen | Grundsätzlich 12 Monate; Verlängerung bis 24 Monate möglich | §§ 31, 33 StaRUG | Erneute Anzeige möglich |
| Stabilisierungsanordnung | Bis 3 Monate; Verlängerung bis 8 Monate gesamt | § 49 StaRUG | Verlängerung erfordert Fortschritt |
| Insolvenzanfechtung | 10 Jahre (Vorsatzanfechtung), 4 Jahre, 1 Jahr je nach Tatbestand | §§ 130–134 InsO | Fristen ab Rechtshandlung |
| Planbestätigung (InsO) | Kein gesetzlicher Zeitrahmen, faktisch 2–6 Monate ab Anmeldung | § 248 InsO | Long-Stop-Date im Plan vereinbaren |
| Haftung nach § 15b InsO (masseschmälernde Zahlungen) | Verjährung 3 Jahre ab Kenntnis | §§ 195, 199 BGB analog | Direkthaftung Geschäftsführer |

## Typische Gegenargumente

| Gegenargument (Gläubiger) | Erwiderung (Schuldner / Berater) |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Plan stellt uns schlechter als Liquidation | Vergleichsrechnung nach § 251 InsO muss Liquidationsszenario realistisch darstellen; Sachverständiger bestellen |
| Antragspflicht war schon früher fällig | Nachweis, dass drohende Zahlungsunfähigkeit erst zu einem späteren Zeitpunkt erkennbar war; Dokumentation der Prognosen |
| StaRUG greift in Eigentumsrechte ein | Art. 14 GG: Eingriff gerechtfertigt, wenn Schlechterstellungsverbot gewahrt und Sanierungsziel legitim |
| Distressed-M&A-Käufer ist Insolvenzverschlepper | Verkauf aus dem Plan / aus der Eigenverwaltung ist gesetzlich vorgesehen; Anfechtungsrisiko durch korrekte Verfahrensgestaltung minimieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — StaRUG-Anzeige oder Insolvenzplan vorbereiten | Schriftsatzbausteine unten nach Baustein 1-3 |
| Variante A — Schuldner bevorzugt aussergerichtliche Loesung | StaRUG-Anzeige und stiller Restrukturierungsrahmen pruefen |
| Variante B — Glaeubigerwiderstands hoch | Planbestaetigungsverfahren mit Cram-down § 26 StaRUG erwaegen |
| Variante C — Insolvenz unvermeidbar | Direkter Weg in regulaere Insolvenz; StaRUG nicht mehr sinnvoll |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Anzeige nach § 31 StaRUG an das Restrukturierungsgericht

```
An das Amtsgericht [Ort] — Restrukturierungsgericht —
[Ort], [Datum]

Anzeige gemäß § 31 StaRUG

In der Restrukturierungssache der [Firma], [Adresse], [Registergericht, HRB ...],

vertreten durch Geschäftsführer/Vorstand [Name],

zeigen wir an, dass die Schuldnerin von ihrem Recht Gebrauch macht, den
Restrukturierungsrahmen des StaRUG in Anspruch zu nehmen.

1. Krisenindikator: Die Schuldnerin befindet sich im Zustand der drohenden
Zahlungsunfähigkeit gemäß § 18 InsO. Zahlungsunfähigkeit (§ 17 InsO) oder
Überschuldung (§ 19 InsO) liegen nach derzeitigem Stand nicht vor.

2. Restrukturierungsziel: Restrukturierung der Finanzverbindlichkeiten in Höhe
von EUR [Betrag] durch Forderungsverzicht/Laufzeitverlängerung/Debt-to-Equity-Swap.

3. Planbetroffene Gläubigerklassen: [Klasse 1: Banken / Klasse 2: Anleihegläubiger /
Klasse 3: Nachrangige Gläubiger].

4. Beabsichtigte Restrukturierungsinstrumente: Restrukturierungsplan gemäß §§ 2 ff.
StaRUG; ggf. Stabilisierungsanordnung gemäß § 49 StaRUG.

Anlagen: Liquiditätsplanung, Finanzierungsübersicht, Gesellschaftsunterlagen.

[Kanzlei, Unterschrift]
```

### Baustein 2 — Antrag auf Planbestätigung (§ 60 StaRUG)

```
An das Amtsgericht [Ort] — Restrukturierungsgericht —
[Ort], [Datum]

Antrag auf gerichtliche Planbestätigung gemäß § 60 StaRUG

In der Restrukturierungssache [Firma], Az. [X]:

Die Schuldnerin beantragt die Bestätigung des Restrukturierungsplans gemäß § 60
Abs. 1 StaRUG.

Zur Begründung wird ausgeführt:

1. Der Plan wurde gemäß §§ 17 ff. StaRUG ordnungsgemäß erstellt und den
planbetroffenen Gläubigern gemäß § 17 StaRUG zugeleitet.

2. Die Abstimmung hat folgendes Ergebnis ergeben:
 Klasse 1 (Banken): [X] % Zustimmung — Mehrheit erreicht
 Klasse 2 (Anleihegläubiger): [X] % Zustimmung — Mehrheit erreicht
 [ggf.] Klasse 3 (Nachrangige): Mehrheit verfehlt — Obstruktionsverbot gemäß
 § 26 StaRUG beantragt (Nichtschlechterstellung nachgewiesen durch Vergleichsrechnung
 Anlage [X]).

3. Versagungsgründe nach § 63 StaRUG liegen nicht vor.

Anlagen: Abstimmungsniederschrift, Vergleichsrechnung (Liquidationswert), Planentwurf.
```

### Baustein 3 — Widerspruch Gläubiger gegen Planbestätigung (§ 64 Abs. 2 StaRUG)

```
An das Amtsgericht [Ort] — Restrukturierungsgericht —
[Ort], [Datum]

Widerspruch gegen die Planbestätigung gemäß § 64 Abs. 2 StaRUG

In der Restrukturierungssache [Firma], Az. [X]:

Namens und in Vollmacht des Gläubigers [Name], Forderungshöhe EUR [Betrag],
erheben wir Widerspruch gegen die Bestätigung des Restrukturierungsplans.

Begründung:

Der Gläubiger wird durch den Plan schlechter gestellt als bei einer Liquidation der
Schuldnerin (§ 64 Abs. 1 Nr. 2 StaRUG). Bei einer Liquidation hätte der Gläubiger
eine Befriedigungsquote von mindestens [X] % erzielt (Sachverständigengutachten Anlage K [X]).
Der Plan sieht lediglich eine Quote von [Y] % vor. Die Schlechterstellung beträgt
EUR [Betrag].

Wir beantragen: Die Bestätigung des Plans ist zu versagen; hilfsweise ist dem Gläubiger
ein Ausgleich in Höhe von EUR [Betrag] gemäß § 64 Abs. 3 StaRUG zuzusprechen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Streitwert und Kosten

| Posten | Berechnung / Ansatz | Hinweis |
|---|---|---|
| Restrukturierungsbeauftragter | Vergütung nach § 76 StaRUG: stundensatzbasiert oder pauschal; Vorschuss durch Schuldner | Auswahl durch Gericht, aber Einfluss möglich |
| Insolvenzverwalter | § 2 InsVV: Berechnungsbasis Insolvenzmasse; gestaffelte Prozentsätze | Regelmäßig 1–3 % der Masse |
| Gerichtsgebühren (Restrukturierung) | § 357 Abs. 1 InsO analog; Planbestätigung: Festgebühr | Vergleichsweise gering |
| Beraterkosten | Restrukturierungsberater + Anwalt: je nach Komplexität EUR 500.000 – mehrere Mio. | Budgetplanung zwingend |
| Distressed-M&A-Transaktionskosten | Wie reguläres M&A, zzgl. Insolvenzverwalterhonorar und Due-Diligence-Zuschlag | Zeitdruck erhöht Kosten |

## Strategische Empfehlung

| Akteur | Empfehlung |
|---|---|
| Geschäftsführung / Vorstand | Bei drohender Zahlungsunfähigkeit frühzeitig StaRUG prüfen; Insolvenzantragspflicht im Blick behalten; persönliche Haftung durch Dokumentation vermeiden |
| Hauptgläubiger | Frühzeitig in Verhandlungen einbinden; Sicherheitenpaket als Verhandlungsmasse nutzen; Debt-to-Equity-Swap als Exit-Option erwägen |
| Distressed-M&A-Käufer | Übertragung aus InsO-Plan oder Eigenverwaltung schützt vor Altverbindlichkeiten; § 613a BGB modifiziert; Anfechtungsrisiko durch sorgfältige Dokumentation minimieren |
| Berater | Zeitplanung mit Pufferfristen; Restrukturierungsgericht früh informieren; Steuerberater für § 3a EStG-Bescheinigung einbinden |

## Anschluss-Skills

- `corporate-kanzlei-kommandocenter` — Gesamtkoordination und Eskalation
- `corporate-kanzlei-transaktionsstruktur` — Distressed-M&A-Strukturentscheidungen
- `corporate-kanzlei-board-paper-business-judgment` — Vorstandsdokumentation bei Krise
- `anw-insolvenzreife-pruefung-17-19-inso` — Detailprüfung Insolvenztatbestände

## Quellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- §§ 1–93 StaRUG; §§ 15a, 15b, 17–19, 217–251 InsO; § 3a EStG; § 7b GewStG

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
