---
name: deal-intake-team
description: "Corporate Kanzlei Deal Intake, Corporate Kanzlei Deal Team Staffing: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Corporate Kanzlei Deal Intake, Corporate Kanzlei Deal Team Staffing

## Arbeitsbereich

Dieser Skill bündelt **Corporate Kanzlei Deal Intake, Corporate Kanzlei Deal Team Staffing** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `corporate-kanzlei-deal-intake` | Neues Transaktionsmandat strukturiert aufnehmen aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message oder DR-Einladung. Anwendungsfall: Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen. Normen: BRAO § 43a, GwG §§ 10 ff. (KYC), WpHG/MAR Insider-Register. Prüfraster: Parteienerfassung, Dealtyp, Phase, Konflikt- und GwG-Check, Insider-Log. Output Deal-Karte, IRL-Startliste, Conflict-Check-Protokoll. Abgrenzung: Routet danach an Fachmodule (SPA, DD, Regulatory); für laufendes Mandat siehe kommandocenter. |
| `corporate-kanzlei-deal-team-staffing` | Transaktionsteam zusammenstellen und Workstreams verteilen für M&A-Mandate: Senior Associate braucht Team-Plan oder Partner will Kapazitaeten ueberprüfen. Normen: BRAO § 43a (Interessenkonflikte), RVG/Stundenhonorar, Budget-Richtlinien. Prüfraster: Workstream-Matrix, Kapazitaetsplanung, Eskalationspfade, Stunden-Reporting. Output Team-Staffing-Plan, Workstream-Zuweisung, Budget-Controlling-Template. Abgrenzung: PMO-Gesamtplanung siehe steps-plan-pmo; Konflikt-Check siehe conflict-gwg-sanctions. |

## Arbeitsweg

Für **Corporate Kanzlei Deal Intake, Corporate Kanzlei Deal Team Staffing** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `corporate-kanzlei` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `corporate-kanzlei-deal-intake`

**Fokus:** Neues Transaktionsmandat strukturiert aufnehmen aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message oder DR-Einladung. Anwendungsfall: Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen. Normen: BRAO § 43a, GwG §§ 10 ff. (KYC), WpHG/MAR Insider-Register. Prüfraster: Parteienerfassung, Dealtyp, Phase, Konflikt- und GwG-Check, Insider-Log. Output Deal-Karte, IRL-Startliste, Conflict-Check-Protokoll. Abgrenzung: Routet danach an Fachmodule (SPA, DD, Regulatory); für laufendes Mandat siehe kommandocenter.

# Deal-Intake

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Deal-Intake` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Deal-Intake

- **Corporate-Aufgabe (Deal-Intake):** Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Intake und brauche einen belastbaren nächsten Schritt."
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
- `/corporate-kanzlei:corporate-kanzlei-matter-file` - wenn Gesellschaftsprofil, Workstreams, Fristen und Dokumentenlog in eine laufende Akte geschrieben werden sollen.
- `/corporate-kanzlei:corporate-kanzlei-kommandocenter` - wenn mehrere Corporate-Workstreams konkurrieren und der nächste Primärpfad neu bestimmt werden muss.
- `/corporate-kanzlei:corporate-kanzlei-steps-plan-pmo` - wenn Termine, Beschlüsse, CPs, Freigaben und Owner in einen belastbaren Plan müssen.
- `/corporate-kanzlei:corporate-kanzlei-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.

## Was dieser Skill nicht macht
- Er ersetzt keine Partner-, Organ- oder Mandantenentscheidung über Beschluss, Signing, Registeranmeldung oder Closing.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Registergericht, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht Corporate-Befund, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

# Deal-Intake

## Triage — klaere zu Beginn

1. Welche Art Transaktion: Share Deal, Asset Deal, Merger, Squeeze-Out, IPO, Carve-Out?
2. Mandant: Kaeufer oder Verkaefer? (Perspektive des Skill-Aufrufs)
3. Gibt es bereits ein NDA / Confidentiality Agreement? Falls nein: sofort anlegen.
4. Sind Insiderinformationen im Spiel? → MAR-Pflichten pruefen (WpHG § 13); Insider-Log anlegen.
5. Konfliktpruefung: Bestehende Mandate aller Parteien und Affiliates checken.
6. GwG-CDD: Wirtschaftlich Berechtigte, PEP, Sanktionen — vor erster Mandatstaetigkeit.
7. Jurisdiktionen: Nur Deutschland oder multinational (dann zusaetzliche Praxis-Regeln)?

## Zentrale Normen

- **§§ 43, 45 BRAO** — Interessenkollision und Verschwiegenheitspflicht; Pflicht zur Konfliktpruefung
- **§§ 2, 10-17 GwG** — Geldwaeschepraevention; CDD vor Annahme; wirtschaftlich Berechtigter
- **Art. 18 MAR / § 13 WpHG** — Insiderliste; Ad-Hoc-Pflicht; Marktmissbrauch; vertrauliche Behandlung
- **§§ 3-5 BORA** — Berufspflichten; Interessenwiderstreit; Need-to-know
- **§ 675 BGB** — Mandate als Dienstvertrag; Pflicht zur vollstaendigen Information des Mandanten

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Deal-Intake-Checkliste

### A. Erste Informationen sichern

| Punkt | Inhalt | Status |
|---|---|---|
| Parteien | Kaeufer, Verkaefer, Zielgesellschaft (vollstaendige Firmennamen, Sitz, Rechtsform) | |
| Deal-Typ | Share Deal / Asset Deal / Merger / IPO / Squeeze-Out | |
| Jurisdiktionen | Hauptsitz, Tochtergesellschaften, Governing Law SPA | |
| Zeitplan | Signing-Ziel; Long Stop Date; exklusive Phase | |
| Volumen | Transaktionsvolumen; EV/Equity Value — vertraulich | |
| Berater-Team | Investmentbank, Steuerberater, andere Kanzleien | |
| Ansprechpartner | Name, Funktion, E-Mail, Mobilnummer | |

### B. Compliance-Checks

| Check | Ergebnis | Datum |
|---|---|---|
| Konfliktpruefung (§ 43a BRAO) | Frei / Konflikt: [Beschreibung] | |
| GwG-CDD | Wirtschaftl. Berechtigter identifiziert; PEP: Ja/Nein; Sanktionen: Frei | |
| Insider-Pruefung (MAR) | Insiderinformation: Ja/Nein; Insider-Log angelegt: Ja/Nein | |
| Clean-Room-Anforderung | Ja/Nein; wenn Ja: Clean-Team-Protokoll | |
| NDA unterzeichnet | Datum; Parteien | |

## Schritt-fuer-Schritt-Workflow

1. **Erstgesprach / Erstkontakt** — Deal-Parameter erfassen; Vertraulichkeit sicherstellen
2. **Konfliktpruefung** — alle Parteien und bekannte Affiliates im Konfliktsystem pruefen; Senior Partner entscheidet
3. **GwG-CDD anlegen** — Identifizierung wirtschaftlich Berechtigter; PEP-Check; Mittelherkunft
4. **Insider-Log anlegen** — bei borsennotierter Gesellschaft: MAR-konformes Insider-Log; Need-to-know-Liste
5. **Akte anlegen** — Deal-Name, Matter-Nummer, Aktenstruktur, Zugriffsrechte
6. **IRL aufstellen** — erste Information Request List nach Workstreams
7. **Teamzusammenstellung** — federführender Partner, Senior Associate, Junior; Budget-Freigabe
8. **NDA sichern** — falls nicht vorhanden: Standardform schicken; kein Informationsaustausch vorher
9. **Kick-Off-Call** — Agenda, Zeitplan, Workstreams, erste Informationslieferung

## Entscheidungsbaum: Insider-Pflichten

```
Zielgesellschaft borsennotiert oder Konzernteil einer Boersengesellschaft?
 → Ja: Insiderinformation vorhanden?
 → Ja: Insider-Log anlegen (Art. 18 MAR); Ad-Hoc ggf. erforderlich
 → Vertraulichkeit von Mandant einfordern (NDA/MAR-Pflicht)
 → Nein: laufend pruefen; Transaktionsbekanntgabe kann Insiderinformation werden
 → Nein: GwG-Standard-CDD; keine MAR-Pflichten im engeren Sinne
 → aber: Marktmanipulation (Art. 12 MAR) auch bei nicht-borsennotierten moeglich
```

## Output-Template Deal-Karte

**Adressat:** Deal-Team intern — Tonfall praegnant, strukturiert

```
DEAL-KARTE
Deal-Name: [CODENAME]
Matter-Nr.: [NUMMER]
Datum: [DATUM]
Vertraulichkeit: [Streng vertraulich / Need-to-know]

PARTEIEN:
Kaeufer: [NAME, Sitz, Rechtsform]
Verkaefer: [NAME, Sitz, Rechtsform]
Zielgesellschaft: [NAME, Sitz, HRB-Nr., Rechtsform]

DEAL-TYP: [Share Deal / Asset Deal / Merge / IPO]
TRANSAKTIONSVOLUMEN: ca. [EUR] (streng vertraulich)
GOVERNING LAW: [Deutsches Recht / Englisches Recht]

TIMELINE:
Signing-Ziel: [DATUM]
Closing-Ziel: [DATUM]
Long Stop Date: [DATUM]

COMPLIANCE-STATUS:
Konfliktpruefung: [Frei | Konflikt: ...]
GwG-CDD: [Vollstaendig | Ausstehend: ...]
Insider-Log: [Angelegt | Nicht erforderlich]

DEAL-TEAM:
Federf. Partner: [NAME]
Senior Associate: [NAME]
Junior: [NAME]
Budget: [EUR]

NAECHSTE AKTION: [TODO mit Datum und Owner]
```

## Rote Schwellen

- Konfliktpruefung nicht vor Mandatsannahme → § 43a BRAO; sofortige Niederlegung; Schadensersatz
- Insiderinformation ohne Log und Vertraulichkeitssicherung → Art. 14 MAR; Bussgeld
- GwG-CDD unvollstaendig → § 17 GwG; Ordnungswidrigkeit; Behoerdenverfahren
- NDA nicht unterzeichnet vor Informationsaustausch → vertrauliche Daten ungeschuetzt
- Akte ohne Zugriffsschutz → Clean-Room-Erfordernis missachtet

## Quellen

- §§ 43, 43a, 45 BRAO; §§ 2-17 GwG; Art. 18 MAR; § 13 WpHG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.

## 2. `corporate-kanzlei-deal-team-staffing`

**Fokus:** Transaktionsteam zusammenstellen und Workstreams verteilen für M&A-Mandate: Senior Associate braucht Team-Plan oder Partner will Kapazitaeten ueberprüfen. Normen: BRAO § 43a (Interessenkonflikte), RVG/Stundenhonorar, Budget-Richtlinien. Prüfraster: Workstream-Matrix, Kapazitaetsplanung, Eskalationspfade, Stunden-Reporting. Output Team-Staffing-Plan, Workstream-Zuweisung, Budget-Controlling-Template. Abgrenzung: PMO-Gesamtplanung siehe steps-plan-pmo; Konflikt-Check siehe conflict-gwg-sanctions.

# Deal-Team-Staffing

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Deal-Team-Staffing` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Deal-Team-Staffing

- **Corporate-Aufgabe (Deal-Team-Staffing):** Senior Associate braucht Team-Plan oder Partner will Kapazitaeten ueberprüfen.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Team-Staffing und brauche einen belastbaren nächsten Schritt."
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

## Was dieser Skill nicht macht
- Er ersetzt keine Partner-, Organ- oder Mandantenentscheidung über Beschluss, Signing, Registeranmeldung oder Closing.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Registergericht, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht Corporate-Befund, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

# Deal-Team-Staffing

## Triage — klaere vor Teamaufstellung

1. Welche Workstreams sind erforderlich: Legal, Tax, Financial, Regulatory, HR?
2. Transakitionsgrösse und Zeitrahmen → Kapazitaetsbedarf einschaetzen
3. Interessenkonflikt-Check fuer alle Teammitglieder durchgefuehrt?
4. Externe Berater erforderlich: Investmentbank, Steuerberater, WP-Gesellschaft?
5. Budget-Freigabe vorhanden? Stundenrahmen pro Workstream?
6. Need-to-know-Restriktionen: Wer darf auf welche Informationen zugreifen (Insider-Log, Clean Room)?

## Zentrale Normen

- **§ 43a BRAO** — Interessenwiderstreit; kein Team-Mitglied darf Gegenpartei vertreten
- **§ 45 BRAO** — Taetigkeitsverbot; bei frueherer Mandatsbeziehung zur Gegenpartei
- **§ 3 BORA** — Vertretung widersteitender Interessen; auch innerhalb einer Kanzlei
- **Art. 18 MAR / § 13 WpHG** — Insider-Liste muss alle Teammitglieder mit Zugang zu kursrelevanten Informationen enthalten
- **§§ 666, 675 BGB** — Auskunftspflicht des Auftragnehmers; Rechenschaftspflicht; Kostenvorschuss

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Team-Staffing-Matrix

| Workstream | Seniorität | Verantwortlich | Stunden (Plan) | Status |
|---|---|---|---|---|
| Deal-Lead / Managing Partner | Partner | [NAME] | [h] | Aktiv |
| Legal DD — Corporate | Senior Assoc. | [NAME] | [h] | Aktiv |
| Legal DD — HR/Compliance | Assoc. | [NAME] | [h] | Aktiv |
| SPA-Verhandlung | Partner + Senior Assoc. | [NAMEN] | [h] | Aktiv |
| Regulatory (Kartell, FDI) | Senior Assoc. | [NAME] | [h] | Aktiv |
| Tax (extern) | Steuerberater [Firm] | [NAME] | [h] | Koordiniert |
| Financial DD (extern) | WP [Firm] | [NAME] | [h] | Koordiniert |
| PMO / Koordination | Senior Assoc. | [NAME] | [h] | Aktiv |

## Schritt-fuer-Schritt-Workflow

1. **Mandatsskizze erstellen** — Scope, Zeitplan, Komplexitaet abschaetzen
2. **Konfliktpruefung fuer alle Kandidaten** — § 43a BRAO; alle Parteien und Affiliates checken
3. **Team-Auswahl** — nach Expertise, Kapazitaet, Insider-Log-Faehigkeit
4. **Rollenverteilung und Briefing** — jeder weiss seinen Scope; Need-to-know-Restriktionen
5. **Stundenplan und Budget** — wochentliche Stunden-Reports; Abweichungen frueh melden
6. **Insider-Liste pflegen** — alle Team-Mitglieder eintragen; Datum des Zugangs dokumentieren
7. **Wochentliches Team-Meeting** — Status, offene Punkte, Ressourcenbedarf
8. **Eskalationsprotokoll** — bei Kapazitaetsproblem oder Interessenkonflikt sofort Partner informieren

## Output-Template Staffing-Karte

```
DEAL-TEAM-STAFFING
Transaktion: [DEAL-NAME]
Datum: [DATUM]

KERN-TEAM:
- Deal-Lead: [NAME, Partner], [EMAIL]
- Senior Associate: [NAME], Workstream: [Legal DD / SPA]
- Associate: [NAME], Workstream: [Regulatory / HR]
- PMO-Koordination: [NAME]

EXTERNE BERATER:
- Investmentbank: [FIRM, Kontakt]
- Steuerberater: [FIRM, Kontakt]
- WP-Gesellschaft: [FIRM, Kontakt]

KONFLIKTPRUEFUNG: [Frei / Konflikt: Beschreibung]
INSIDER-LOG AKTIV: [Ja / Nein]

BUDGET:
Interne Stunden: [h] geplant
Externe Berater: [EUR] geplant
Verfuegbarer Rahmen: [EUR]

ESKALATIONSPFAD:
Kapazitaetsprobleme → [Managing Partner NAME]
Interessenkonflikt → [COLP (Compliance Officer)]
Strategische Fragen → [Fuehrender Partner NAME]
```

## Rote Schwellen

- Konfliktpruefung nicht fuer alle Teammitglieder → § 43a BRAO Kanzlei-Haftung
- Insider-Log unvollstaendig → Art. 18 MAR; BaFin-Bussgeld; Compliance-Risiko
- Kein Need-to-know-Protokoll → Clean-Room-Verletzung; Kartellrecht-Risiko
- Budget-Ueberschreitung nicht fruehzeitig kommuniziert → Mandantenunzufriedenheit; Honorarstreit

## Quellen

- §§ 43a, 45 BRAO; § 3 BORA; Art. 18 MAR; §§ 666, 675 BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
