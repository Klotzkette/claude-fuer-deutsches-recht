---
name: kommandocenter
description: "Deal-Kommandocenter Corporate/M&A: Schnellstart für Mandate. Erkennt Dealtyp, Phase und Parteiperspektive; erzeugt Deal-Karte mit Ampel, Rollen, naechster Aktion und Freigabegrad. Routet an passenden Fachmodul (SPA, DD, StaRUG, Kapitalmarkt, Register)."
---

# Deal-Kommandocenter — Corporate/M&A

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Deal-Kommandocenter — Corporate/M&A

- **Corporate-Aufgabe (Deal-Kommandocenter — Corporate/M&A):** Schnellstart für Mandate. Erkennt Dealtyp, Phase und Parteiperspektive; erzeugt Deal-Karte mit Ampel, Rollen, naechster Aktion und Freigabegrad. Routet an passenden Fachmodul (SPA, DD, StaRUG, Kapitalmarkt, Register).
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Deal-Kommandocenter — Corporate/M&A und brauche einen belastbaren nächsten Schritt."
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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/corporate-kanzlei:corporate-kanzlei-deal-intake` - wenn ein neues Corporate- oder Transaktionsmandat vollständig aufgenommen werden muss.
- `/corporate-kanzlei:corporate-kanzlei-matter-file` - wenn Gesellschaftsprofil, Workstreams, Fristen und Dokumentenlog in eine laufende Akte geschrieben werden sollen.
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

### Deal-Kommandocenter — Corporate/M&A

## Triage — kläre beim Mandatseingang

1. Dealtyp: Share Deal, Asset Deal, Kapitalerhöhung, Umwandlung, Distressed M&A, StaRUG/Insolvenz, Registervorgang?
2. Parteiperspektive: Buy-side, Sell-side, Target-Management, W&I-Versicherer, Finanzierungsbank, Aufsichtsrat?
3. Deal-Phase: Origination, Vorbereitung/NDA, Datenraum-Aufbau, Due Diligence, Vertragsverhandlung, Signing, Closing, Post-Merger-Integration, Streit/Restrukturierung?
4. Zeitkritisch? Signing-/Closing-Datum, behördliche Fristen (Fusionskontrolle, FDI), Insolvenzantragspflicht §§ 15a, 15b InsO?
5. Besondere Sensibilität: Clean-Room-Anforderung, Insiderinformation (MAR), Sanktionsrecht, Mandatsgeheimnis?

## Zentrale Normen

- **§ 15a InsO** — Insolvenzantragspflicht; Frist 6 Wochen (Überschuldung) / 3 Wochen (Zahlungsunfähigkeit).
- **§§ 17-19 InsO** — Insolvenztatbestände; Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit, Überschuldung.
- **Art. 7 ECMR / § 36 GWB** — Fusionskontrolle; Vollzugsverbot vor Freigabe.
- **§ 40 AWG / §§ 55 ff. AWV** — Außenwirtschaftsrechtliche Investitionsprüfung (FDI); Vollzugsverbote.
- **Art. 17 MAR / § 26 WpHG** — Ad-hoc-Pflicht; Insiderinformation im M&A-Prozess.
- **§§ 2 ff. StaRUG** — Restrukturierungsrahmen; Anzeigepflicht und Planverfahren bei drohender Zahlungsunfähigkeit.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Deal-Routing-Matrix

| Dealtyp / Thema | Primärer Fachmodul | Sekundärer Fachmodul |
|---|---|---|
| SPA / APA Entwurf und Verhandlung | `corporate-kanzlei-spa-apa-entwurf` | `corporate-kanzlei-vertragsmarkup-key-issues` |
| Legal Due Diligence | `corporate-kanzlei-due-diligence-legal` | `corporate-kanzlei-due-diligence-reporting` |
| Datenraum Aufbau | `corporate-kanzlei-datenraum-aufbau` | `corporate-kanzlei-datenraum-gap-clean-room` |
| Transaktionsstruktur | `corporate-kanzlei-transaktionsstruktur` | `corporate-kanzlei-umwandlungsrecht` |
| Signing und Closing | `corporate-kanzlei-signing-closing-conditions` | `corporate-kanzlei-output-versand-signing` |
| W&I-Versicherung | `corporate-kanzlei-wi-insurance` | `corporate-kanzlei-disclosure-schedules` |
| Public M&A / Kapitalmarkt | `corporate-kanzlei-public-ma-kapitalmarkt-mar` | `corporate-kanzlei-regulatory-fdi-merger-control` |
| Restrukturierung / StaRUG | `corporate-kanzlei-restructuring-starug-insolvenzplan` | `corporate-kanzlei-distressed-ma` |
| KG / Personengesellschaft | `corporate-kanzlei-kg-personengesellschaften` | — |
| Umwandlungssteuerrecht | `corporate-kanzlei-umwandlungssteuerrecht` | `corporate-kanzlei-transaktionsstruktur` |
| Handelsregister / Register | `corporate-kanzlei-handelsregisterabruf` | `corporate-kanzlei-gesellschaftsrecht-register` |
| Konflikt / GwG / Sanktionen | `corporate-kanzlei-conflict-gwg-sanctions` | — |
| Datenqualität | `corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle` | — |
| Billing / Narratives | `corporate-kanzlei-billing-narratives` | — |

## Schritt-für-Schritt-Workflow

1. **Dealtyp erkennen** — aus Eingabetext (Term Sheet, NDA, Markup, Sachverhaltsangabe) den primären Dealtyp bestimmen.
2. **Parteiperspektive klären** — Buy-side oder Sell-side; Target-Management, Aufsichtsrat oder Finanzierungspartei?
3. **Deal-Phase bestimmen** — welche Phase ist aktiv; was ist die unmittelbare nächste Aktion?
4. **Zeitkritische Elemente identifizieren** — Signing/Closing-Datum, behördliche Fristläufe, Insolvenzantragspflicht?
5. **Routing-Entscheidung** — passenden Fachmodul aus Deal-Routing-Matrix auswählen.
6. **Deal-Karte erstellen** — Standardausgabe mit Ampel, Rollen, Owner, Deadline, Risiko, Freigabegrad.
7. **Rote Schwellen prüfen** — Stop bei Insiderinformation, Clean-Room-Problem, unklarem Closing-Datum oder Insolvenzantragspflicht.
8. **An Fachmodul übergeben** — Deal-Karte und Sachverhalt weitergeben; offene Punkte als TODO mit Owner und Frist.

## Output-Template Deal-Karte

**Adressat:** Deal-Team intern — Tonfall sachlich-präzise
```
DEAL-KARTE
Mandat: [Mandatsname / Kürzel]
Datum: [Datum]
Ersteller: [Name, Funktion]

ÜBERSICHT
Dealtyp: [Share Deal / Asset Deal / Umwandlung / Distressed / Kapitalerhöhung]
Parteiperspektive:[Buy-side / Sell-side / Target-Management / W&I / Financing]
Deal-Phase: [Origination / Vorbereitung / DD / Verhandlung / Signing / Closing / PMI]
Signing: [Datum oder "ausstehend"]
Closing: [Datum oder "ausstehend — Bedingungen offen"]

AMPELSTATUS
| Workstream | Status | Owner | Nächste Aktion | Deadline |
|-----------|--------|-------|----------------|---------|
| Legal DD | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| SPA Verh. | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| Regulatory| 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| Closing | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |
| PMI | 🟢/🟡/🔴 | [Name] | [Aktion] | [Datum] |

ROTE SCHWELLEN (aktiv)
[ ] Frist oder Closing-Datum unklar
[ ] Insiderinformation / Clean-Room-Problem
[ ] Insolvenzantragspflicht möglicherweise ausgelöst
[ ] Fusionskontrolle / FDI-Freigabe ausstehend

ROUTING
Primärer Fachmodul: [Skill-Name]
Sekundärer Skill: [Skill-Name oder —]

OFFENE PUNKTE (TODO)
| Nr. | Punkt | Owner | Frist | Eskalation |
|----|-------|-------|-------|------------|
| 1 | [Punkt] | [Name] | [Datum] | [Stufe] |

FREIGABEGRAD: [Entwurf / Freigegeben durch Partner / Vertraulich — nur intern]
```

## Rote Schwellen

- Signing- oder Closing-Datum unklar → Deal-Karte unvollständig; Datum klären bevor Routing.
- Insiderinformation oder Clean-Room-Anforderung erkannt → Stop; Informationsbarriere aufbauen; Compliance informieren.
- Insolvenzantragspflicht (§ 15a InsO) möglicherweise ausgelöst → sofort Eskalation an Partner; keine unkoordinierten Handlungen.
- Analytisches Ergebnis soll ungeprüft in Board Paper oder DD-Bericht einfließen → Qualitätskontrolle (`corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle`) vorschalten.
- Fusionskontrolle oder FDI-Freigabe ausstehend, Deal-Vollzug geplant → Gun-Jumping-Risiko; Regulatory-Skill einschalten.

## Quellen und Vertiefung

- §§ 15a, 15b, 17-19 InsO (Insolvenzantragspflicht und -tatbestände)
- Art. 7 ECMR; § 36 GWB (Fusionskontrolle)
- § 40 AWG; §§ 55 ff. AWV (FDI-Investitionsprüfung)
- Art. 17 MAR; § 26 WpHG (Insiderinformation)
- §§ 2 ff. StaRUG (Restrukturierungsanzeige)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
