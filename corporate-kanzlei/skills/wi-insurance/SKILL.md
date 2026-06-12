---
name: wi-insurance
description: "W&I-Versicherung (Warranty & Indemnity Insurance) strukturieren und prüfen: M&A-Berater braucht Policen-Analyse oder Underwriting-Vorbereitung. Normen: SPA Reps & Warranties, VVG, englisches Insurance-Recht (Lloydserfahrung). Prüfraster: Kaeufer- vs. Verkaeufer-Policy, Underwriting-Prozess, No-Cl..."
---

# W&I-Versicherung (Warranty & Indemnity Insurance)

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: W&I-Versicherung (Warranty & Indemnity Insurance)

- **Corporate-Aufgabe (W&I-Versicherung (Warranty & Indemnity Insurance)):** M&A-Berater braucht Policen-Analyse oder Underwriting-Vorbereitung.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier W&I-Versicherung (Warranty & Indemnity Insurance) und brauche einen belastbaren nächsten Schritt."
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

### W&I-Versicherung (Warranty & Indemnity Insurance)

## Triage — klaere vor Beginn

1. Kaeufer-Policy (haeufiger) oder Verkaefer-Policy (seltener)?
2. Dealgroesse und Transaktionsvolumen — Mindestpraemie ca. 150-200 TEUR; W&I sinnvoll ab ca. 15-20 Mio. EUR EV
3. Welche Workstreams sind im Scope der W&I (Legal, Tax, Environmental, Financial)?
4. Kenntnis-Definition: "Best Knowledge" oder "Actual Knowledge" des Verkaefers?
5. Retention / Selbstbehalt: De-Minimis, Basket (Tipping vs. Deductible), Cap (Underwriting Limit)?
6. Underwriting-Zeitplan: Minimum 2 Wochen für Underwriting nach vollstaendigem DD-Report?
7. Sind Fundamental Warranties (Title, Authority, Kapitalstruktur) mit laengerem Zeitlimit versichert?

## Zentrale Regelwerke

- **Versicherungsvertragsgesetz (VVG)** — §§ 1-20 VVG allgemeine Versicherungspflichten; § 21 VVG vorvertragliche Anzeigepflicht
- **W&I-Marktstandard (deutsch/englisch)** — Keine gesetzliche Spezialregelung; Marktstandard nach BIPAR, LMA, GDV
- **SPA-Schnittstelle** — Vertragsklausel: "Kaeufer-Policy erhaeltlich; Verkaefer-Haftung auf Betrag X beschraenkt (Excess unter Policy)"
- **Tax W&I / Tax-Indemnity** — separates Instrument für bekannte Steuerrisiken; nicht unter allgemeiner W&I

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## W&I-Versicherungsstruktur: Übersicht

### Kaeufer-Policy (Buyer-Side)
- Kaeufer ist Versicherungsnehmer und Beguenstigter
- Verkaefer haftet nur noch in Höhe des Selbstbehalts (Excess) — oft 0 EUR bei Nil-Seller-Liability-Strukturen
- Praemie: 0.8-1.5 % der Versicherungssumme (Stand 2024)
- Vorteile: Kaeufer-Kontrolle; kein Schritt gegen Verkaefer; PE-Seller bevorzugt (Clean Exit)

### Verkaefer-Policy (Seller-Side)
- Verkaefer ist Versicherungsnehmer; Kaeufer haelt direkten Anspruch gegen Verkaefer
- Verkaefer leitet Anspruch an Versicherer weiter
- Heute selten; meist ersetzt durch Kaeufer-Policy

### Ablauf Underwriting-Prozess

| Schritt | Dauer | Inhalt |
|---|---|---|
| Brokerauftrag und NDA | Tag 1 | Broker, Versicherer und Deal-Team identifizieren |
| Info-Memo an Underwriter | Tag 1-3 | Deal-Summary, DD-Scope, Draft SPA |
| Non-Binding Indications | Tag 3-5 | Praemienrahmen; Deckungsumfang; Ausschluesse |
| Binder-Verhandlung | Tag 5-10 | Underwriting-Workshop; Fragen zu DD; Warranty-Review |
| No-Claims Declaration | Kurz vor Signing | Kein bekanntes Ereignis das Claim ausloest |
| Policy Bound | Signing | Versicherungsschutz ab Signing; ggf. Bringdown |

## Wichtige Deckungsluecken (Ausschluesse)

| Ausschluss | Beschreibung | Ausweg |
|---|---|---|
| Known Facts | Versicherte hat Kenntnis des Risikos | Erhoehtes Pricing; separate Indemnity |
| Forward-Looking Reps | Reps über Zukunftserwartungen | Kein Schutz; earmarked risks |
| Environmental / Umwelt | Bodenkontamination; Altlasten | Separate Umwelt-Policy; Environmental Indemnity |
| Purchase Price Adjustment | Working Capital/Net Debt-Anpassungen | Separate Purchase Price-Mechanismus |
| Pension Deficits | Unterdeckung bei Pensionsverpflichtungen | Separate Pension Indemnity im SPA |
| Tax W&I | Nur allgemein; bekannte Tax-Risiken | Separate Tax-Indemnity im SPA |

## Schritt-für-Schritt-Workflow

1. **W&I-Entscheidung** — sinnvoll? Transaktionsvolumen, Verkaefer-Typ (PE), DD-Qualitaet
2. **Broker beauftragen** — spezialisierter W&I-Broker (Willis, AON, Lockton, Marsh)
3. **Underwriting-Info-Memo** — Deal-Summary; DD-Report; Entwurf SPA
4. **Non-Binding Indications** — Praemienvergleich mind. 2-3 Angebote
5. **Underwriting-Workshop** — Underwriter stellen DD-Fragen; bekannte Risiken offen erläutern
6. **SPA-Abstimmung** — Warranty-Wording im SPA muss mit Policy-Wording uebereinstimmen
7. **No-Claims Declaration** — kurz vor Signing; alle am Prozess Beteiligten bestaetigen keine Kenntnis von Claims
8. **Policy binden** — gleichzeitig mit Signing; Deckungsbeginn
9. **Enhanced Disclosure Closing** — wenn neue Fakten zwischen Signing und Closing: Versicherer informieren
10. **Claim-Prozess** — bei Warranty-Verletzung: Versicherer informieren, Claim-Dokumentation aufbauen

## Entscheidungsbaum: W&I sinnvoll?

```
Transaktionsvolumen > 15 Mio. EUR EV?
 → Ja: Verkaefer = PE-Fonds oder Insolvenzmasse?
 → Ja: W&I fast immer sinnvoll (PE will Clean Exit)
 → Nein: DD-Ergebnis: Erhebliche bekannte Risiken?
 → Ja: W&I für unbekannte Risiken; Indemnities für bekannte
 → Nein: W&I als kosteneffizienter Ersatz für Haeftungsrisiko
 → Nein: W&I wirtschaftlich meist nicht sinnvoll (Mindestpraemie)
```

## Output-Template W&I-Praemienvergleich

**Adressat:** Mandant / Deal-Team — Tonfall klar, vergleichend

```
W&I-PRAEMIENVERGLEICH
Transaktion: [DEAL-NAME]
Stand: [DATUM]
Versicherungssumme: [EUR] (= [X]% des Kaufpreises)

| Versicherer | Praemie (% der Versicherungssumme) | Retention / Basket | Cap | Besondere Bedingungen |
|-------------|-----------------------------------|-------------------|-----|----------------------|
| [Versicherer A] | [X%] | [EUR] | [X Mio. EUR] | [z.B. keine Umwelt] |
| [Versicherer B] | [X%] | [EUR] | [X Mio. EUR] | [...] |

EMPFEHLUNG: [Versicherer X — Begruendung]

NO-CLAIMS-DECLARATION: aufgelistete Personen
- [NAME, Funktion]
Datum der Abgabe: [DATUM]
```

## Rote Schwellen

- DD-Report-Luecken nicht an Underwriter gemeldet → Deckungsablehnung wegen non-disclosure
- Warranty-Wording in SPA weicht von Policy-Wording ab → Deckungsluecke
- Bekannte Risiken (Known Facts) nicht durch separate Indemnity abgesichert → kein W&I-Schutz
- No-Claims Declaration unvollstaendig (nicht alle Beteiligte) → Formmangel; Claim-Risiko
- Post-Signing neue Fakten nicht an Versicherer gemeldet → Deckungsausschluss

## Quellen

- VVG (Versicherungsvertragsgesetz): https://www.gesetze-im-internet.de/vvg_2008/
- VVG § 19 (vorvertragliche Anzeigepflicht): https://www.gesetze-im-internet.de/vvg_2008/__19.html
- W&I-Marktstandard: LMA-Modellklauseln, GDV-Hinweise (Stand prüfen).
- Im SPA-Kontext: §§ 311 II, 280 BGB (W&I deckt regelmaessig Garantieverletzungen § 311 I BGB oder vertragliche Schadensersatzregelungen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
