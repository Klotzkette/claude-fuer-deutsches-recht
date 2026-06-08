---
name: kg-personengesellschaften
description: "KG und Personengesellschaften im Corporate/M&A-Kontext begleiten: Anteilsuebertragung, Haftungsstruktur, Ergebnisverwendung bei KG, GmbH & Co. KG, Partnerschaft und GbR nach MoPeG 2024. Normen: HGB §§ 105-177a, MoPeG 2024, AktG (Kommanditaktionaer). Prüfraster: Komplementaerhaftung, Kommanditeinlage, Einheitsbilanz, Steuerliche Sonderformen. Output Strukturierungsempfehlung, Anteilsuebertragungsvertrag-Entwurf, Haftungsmatrix. Abgrenzung: GmbH/AG siehe gesellschaftsrecht-register; Steuer siehe umwandlungssteuerrecht."
---

# KG und Personengesellschaften — Corporate/M&A

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: KG und Personengesellschaften — Corporate/M&A

- **Corporate-Aufgabe (KG und Personengesellschaften — Corporate/M&A):** Anteilsuebertragung, Haftungsstruktur, Ergebnisverwendung bei KG, GmbH & Co. KG, Partnerschaft und GbR nach MoPeG 2024.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier KG und Personengesellschaften — Corporate/M&A und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- 13-Wochen-Liquiditätsplanung, Insolvenzreife-Check und Fortbestehensprognose.
- Asset-/Share-Deal-Struktur, Verwalter-/Eigenverwaltungsrolle und Zahlungsfluss.
- Anfechtungs-, Haftungs-, Steuer- und Closing-Sicherungsfragen.

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
- InsO §§ 15a, 17, 18, 19, 129 ff., 270 ff. für Insolvenzreife, Antragspflicht und Anfechtung.
- StaRUG §§ 1, 9 ff. und 49 ff. für Früherkennung, Plan und Stabilisierung.
- BGB §§ 134, 138, 280, 311 Abs. 2 und 826 für Haftungs- und Sittenwidrigkeitsfragen.
- UmwStG §§ 20 bis 24 und § 8c KStG nur mit Steuerteam verifizieren.

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
- `/corporate-kanzlei:corporate-kanzlei-distressed-ma` - wenn Krise, Antragspflicht, Anfechtung oder Liquiditätsplanung entscheidend werden.
- `/corporate-kanzlei:corporate-kanzlei-restructuring-starug-insolvenzplan` - wenn StaRUG, Planoptionen oder Insolvenzplanstruktur geprüft werden.
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

### KG und Personengesellschaften — Corporate/M&A

## Triage — klaere vor Beginn

1. Welche Personengesellschaft: OHG, KG, GmbH & Co. KG, PartG, GbR (nach MoPeG 2024)?
2. M&A-Kontext: Erwerb von Kommanditanteilen, Generationswechsel, Konzernintegration?
3. Gesellschaftsvertrag: Abweichende Regelungen zu HGB? Vinkulierung von Kommanditanteilen?
4. Steuerliche Struktur: Mitunternehmerschaft; gewerbliche Infizierung; Transparenzprinzip?
5. Haftung: Kommanditist haftet bis Einlage; Komplementaer unbeschraenkt — wer uebernimmt welche Rolle post-Closing?
6. Nach MoPeG (ab 01.01.2024): GbR im Register; Rechtsfaehigkeit; Vertretung?

## Zentrale Normen

- **§§ 105-177a HGB** — OHG, KG; Gesellschaftsvertrag; Ergebnisverteilung; Ausscheiden, Kluendigung
- **§§ 161-177a HGB** — KG spezifisch; Kommanditist; beschraenkte Haftung (§ 171 HGB)
- **§§ 705-740c BGB n.F. (MoPeG)** — GbR-Reform ab 01.01.2024; Rechtsfaehigkeit der GbR; Register moeglich
- **§ 15 EStG** — Mitunternehmerschaft; gewerbliche Einkuenfte; Sonderbetriebsvermoegen
- **§ 24 UmwStG** — Einbringung in Personengesellschaft; Buchwertfortfuehrung
- **§ 6 III EStG** — Unentgeltliche Uebertragung von Mitunternehmeranteilen; keine Aufdeckung stiller Reserven

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anteilsuebertragung bei Personengesellschaften

| Form | OHG/KG/GmbH & Co. KG | GbR (nach MoPeG) |
|---|---|---|
| Formpflicht | Keine gesetzliche Form; Ausnahmen in Gesellschaftsvertrag | Keine gesetzliche Form; Registereintragung GbR moeglich |
| Zustimmung Mitgesellschafter | Grundsaetzlich alle Gesellschafter; Vinkulierungsklausel beachten | Nach Gesellschaftsvertrag |
| Aufnahme ins Register | Handelsregister-Abteilung A | GbR-Register moeglich (freiwillig bis verpflichtend) |
| Steuerfolgen | § 6 III EStG; § 24 UmwStG | Wie bei KG; Transparenzprinzip |

## GmbH & Co. KG: Besonderheiten

- **Komplementaer-GmbH:** GmbH ist einziger Komplementaer; haftet nach § 13 II GmbHG mit Stammkapital
- **Kommanditisten:** Natuerliche oder juristische Personen; Haftung = Einlage
- **Geschaeftsfuehrung:** GmbH fuehrt KG-Geschaefte; GmbH-GF = handelnde Person
- **Jahresabschluss:** Konsolidierungspflicht ab bestimmter Groesse; oeffentlichkeitspflichtig nach § 325 HGB
- **Vorteil:** Kombination der Vorteile von KG (Steuer: transparentes Mitunternehmer) und GmbH (Haftungsbeschraenkung)

## Schritt-für-Schritt-Workflow

1. **Gesellschaftsvertrag analysieren** — Vinkulierungsklauseln; Abtretungsvoraussetzungen; Zustimmungserfordernisse
2. **Steuerliche Struktur pruefen** — Mitunternehmerschaft; Sonderbetriebsvermoegen; Transparenzprinzip
3. **Haftungsanalyse** — Wer ist Komplementaer? Wie hoch sind Kommanditisten-Einlagen?
4. **UBO-Identifizierung** — Treuhander-Strukturen; GwG-CDD bei KG-Transaktionen
5. **Anteilsuebertragung gestalten** — Notarielle Beurkundung nur wenn Gesellschaftsvertrag es vorschreibt
6. **MoPeG-Kompatibilitaet** — GbR-Vertrag seit 01.01.2024 ggf. anpassen (Rechtsfaehigkeit, Register)
7. **Post-Closing HR-Anmeldung** — Aenderungen in Kommanditanteilen beim Handelsregister-A melden

## Output-Template Kommanditanteil-Abtretungsvertrag (Ausschnitt)

```
ABTRETUNGSVERTRAG
Kommanditanteil an [FIRMA KG]

Parteien: [VERAEUSSERER] / [ERWERBER]
Datum: [DATUM]

1. GEGENSTAND
 Der Veraeusserer uebertraegt hiermit seinen Kommanditanteil an der [FIRMA KG]
 (HRA-Nummer: [Nr.], Amtsgericht [Ort])
 im Nominalwert von EUR [BETRAG] an den Erwerber.

2. KAUFPREIS
 EUR [BETRAG]; zahlbar bis [DATUM].

3. ZUSTIMMUNGEN
 Die uebrigen Gesellschafter haben der Abtretung am [Datum] zugestimmt.
 [Gesellschaftsvertrag § X: Vinkulierungsklausel beachtet]

4. STEUERLICHE REGELUNGEN
 [Buchwertfortfuehrung nach § 6 III EStG; oder § 24 UmwStG]

5. HANDELSREGISTERANMELDUNG
 Der Erwerber verpflichtet sich, die Aenderung unverzueglich beim Handelsregister anzumelden.
```

## Rote Schwellen

- Vinkulierungsklausel im GV nicht beachtet → Abtretung unwirksam; kein Eigentuemerwechsel
- Steuerliche Mitunternehmerschaft-Eigenschaft bei Erwerb nicht geprueft → ggf. gewerbliche Infizierung
- GwG-UBO bei Treuhander-Strukturen → wirtschaftlich Berechtigter hinter Treuhander identifizieren
- MoPeG seit 01.01.2024 ignoriert → GbR-Recht grundlegend geaendert; alte Strukturen ggf. anpassen

## Quellen

- §§ 105-177a HGB; §§ 705-740c BGB n.F. (MoPeG); § 15 EStG; § 24 UmwStG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
