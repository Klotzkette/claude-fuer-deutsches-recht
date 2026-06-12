---
name: billing-narratives
description: "Corporate Billing Narratives: Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. Normen: RVG (wenn anwendbar), Stundenhonorar-Vereinbarung, BRAO § 49b."
---

# Corporate Billing Narratives

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Corporate Billing Narratives

- **Corporate-Aufgabe (Corporate Billing Narratives):** Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Corporate Billing Narratives und brauche einen belastbaren nächsten Schritt."
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

## Prüfraster im Gutachtenstil
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

### Corporate Billing Narratives

## Triage — klaere vor Erstellung

1. Honorarvereinbarung: Stundenhonorar (haefig bei M&A), Pauschalhonorar, Cap, Success Fee?
2. Rechnungsempfaenger: Mandant direkt, Finanzierer (Financing Bank), PE-Fonds?
3. E-Rechnung-Pflicht (seit 2025 für B2B ab bestimmter Groesse; §§ 14 ff. UStG)?
4. Welche Workstreams werden einzeln abgerechnet: Legal DD, SPA, Regulatory, W&I?
5. Vertraulichkeit: Darf die Narrative Details offenbaren oder nur pauschal beschreiben?
6. Budget-Abweichung: Ist der Rahmen ueberschritten? Mandant fruehzeitig informieren?

## Zentrale Normen

- **§ 49b BRAO** — Vergaberrecht; Erfolgshonorar; Sittenwidrigkeits-Grenzen
- **§§ 14, 14a UStG** — Rechnungsausstellung; E-Rechnung-Pflicht ab 2025 (B2B)
- **§§ 3a, 4 BORA** — Vergaeregelung; transparente Abrechnung
- **§ 675 BGB** — Auftragsverhaeltnis; Auslagenpflicht; Rechenschaftspflicht
- **GoBD (Grundsaetze ordnungsmäßiger Buchfuehrung)** — elektronische Rechnungsarchivierung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Narrative-Typen und Formulierungen

### Allgemeine Time-Narrative-Formel

**Verboten:** "Aktenstudium", "Telefonat", "Recherche" (zu vage)
**Empfohlen:** Konkrete, phase-bezogene Beschreibungen

| Phase | Mustertextbaustein |
|---|---|
| DD-Phase | "Analyse der Vertragsdokumentation im Datenraum (Workstream: Wesentliche Verträge); Prüfung Change-of-Control-Klauseln für 28 Verträge; Red-Flag-Memo-Beitrag Corporate/Litigation" |
| SPA-Phase | "Verhandlung Haftungsklauseln §§ 8-11 SPA; Markup-Runde 3; Abstimmung W&I-Wording mit Underwriter-Beratern; interne Koordination mit Steuerberatern" |
| Regulatory | "Vorbereitung und Einreichung Fusionskontrollantrag beim Bundeskartellamt; Beantwortung Ruckfragen Phase I (Schreiben vom [Datum]); Koordination mit Mandant und Investmentbank" |
| Closing | "Vorbereitung Closing-Checkliste; Review aller Deliverables; Closing-Meeting Koordination; Notartermin Begleitung" |

## Schritt-für-Schritt-Workflow

1. **Zeitererfassung nach Workstream** — taeglich; keine monatliche Nacherfassung
2. **Narrative-Qualitaet prüfen** — mandantentaugliche Beschreibung; kein anwaltliches Privileg gefaehrden
3. **Budget-Tracking** — woechentlich; Warnung bei >80 % verbraucht
4. **Phasenrechnung erstellen** — nach Signing, nach Closing, oder monatlich nach Vereinbarung
5. **Review durch Kanzlei-Finance** — Konsistenz; E-Rechnung-Format; MwSt-Hinweis
6. **Versand mit Mandanten-Beziehungspflege** — kurze Erläuterung der Leistungen; offen für Rueckfragen

## Output-Template Rechnungsnarrativ (Ausschnitt)

```
RECHNUNG / INVOICE
[KANZLEI]
[ADRESSE]
An: [MANDANT FIRMA, ADRESSE]
Rechnungsdatum: [DATUM]
Rechnungsnummer: [NR.]
Leistungszeitraum: [VON - BIS]

Matter: [DEAL-CODENAME], Matter-Nr.: [NR.]

LEISTUNGEN:

Phase: Legal Due Diligence — [DATUM - DATUM]
Partner [NAME]: [h] x EUR [Stundensatz] = EUR [Betrag]
 Narrative: "Leitung und Review Legal-DD-Workstreams: Corporate/Title, Wesentliche
 Vertraege (CoC-Analyse), Litigation; Abstimmung mit Verkaefer-Kanzlei;
 Red-Flag-Memo-Freigabe; DD-Report-Review und Signoff"

Senior Associate [NAME]: [h] x EUR [Stundensatz] = EUR [Betrag]
 Narrative: "DD-Workstream Vertraege: Pruefung und Indexierung 47 Vertraege;
 Q&A-Bearbeitung 12 Fragen; SPA-Reps-Mapping für Material-Contracts-Warranty"

Summe Phase DD: EUR [Betrag] netto
Mehrwertsteuer 19 %: EUR [Betrag]
Gesamt Phase DD: EUR [Betrag]

[Weitere Phasen analogisch...]

GESAMT-HONORAR: EUR [Betrag] netto
USt 19 %: EUR [Betrag]
Rechnungsbetrag brutto: EUR [BETRAG]

Zahlungsziel: 14 Tage nach Rechnungsdatum
IBAN: [IBAN]
```

## Rote Schwellen

- Narrative enthaelt mandatsgeheimnisrelevante Details → § 43a BRAO; Vertraulichkeitspflicht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechnungsadresse falsch (Fonds statt Portfolio-Gesellschaft) → Mehrwertsteuer-Problem
- E-Rechnung-Pflicht ab 2025 nicht beachtet → § 14a UStG-Verstoss; Abzugsfaehigkeit fraglich

## Quellen

- § 49b BRAO; §§ 14, 14a UStG; §§ 3a, 4 BORA; GoBD
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
