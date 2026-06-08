---
name: datenraum-gap-clean-room
description: "Gap-Analyse des Datenraums und Clean-Room-Protokoll für M&A-Transaktionen: Identifiziert fehlende Dokumente, verwaltet IRL-Status (Information Request List), trennt sensible Wettbewerberdaten. Normen: DSGVO, GWB Clean-Team-Grundsaetze, MAR. Prüfraster: je Workstream fehlende Belege, IRL-Antwortstand, Clean-Room-Zugangsliste. Output Gap-Tabelle mit Priorisierung, IRL-Update, Clean-Room-Protokoll. Abgrenzung: Aufbau des DR siehe datenraum-aufbau; inhaltliche Vertragsprüfung siehe due-diligence-commercial-contracts."
---

# Datenraum Gap-Analyse und Clean Room

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Datenraum Gap-Analyse und Clean Room

- **Corporate-Aufgabe (Datenraum Gap-Analyse und Clean Room):** Identifiziert fehlende Dokumente, verwaltet IRL-Status (Information Request List), trennt sensible Wettbewerberdaten.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Datenraum Gap-Analyse und Clean Room und brauche einen belastbaren nächsten Schritt."
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

### Datenraum Gap-Analyse und Clean Room

## Triage — klaere vor Beginn

1. Welche Datenraum-Plattform? Welche Dokument-Kategorien fehlen noch?
2. Wie weit ist die IRL (Information Request List) abgearbeitet? Quantifizieren.
3. Welche Workstreams sind zeitkritisch (z.B. Steuer vor DD-Abschluss)?
4. Gibt es kartellrechtliche Clean-Room-Anforderungen (GWB Clean Team für Wettbewerber)?
5. Welche sensiblen Daten (HR, Kunden-Namen, Betriebsgeheimnisse) brauchen eingeschraenkten Zugang?
6. Sind W&I-Underwriter im Prozess? (Underwriter-Zugriffsrechte separat regeln)

## Zentrale Normen

- **Art. 5, 28 DSGVO** — Datensparsamkeit; Auftragsverarbeitung; keine unnoetigen Personal-Daten im DR
- **§§ 1, 19 GWB** — kartellrechtliche Clean-Room-Anforderung bei Wettbewerber-Transaktionen; Informationsaustausch verboten bis Freigabe
- **§ 17 UWG** — Geschaeftsgeheimnis; Schutz sensibler Informationen auch im DD-Prozess
- **Art. 18 MAR** — Insider-Log für jeden mit Datenraum-Zugang bei borsennotierten Zielgesellschaften

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bundeskartellamt, Leitfaden Clean Team 2019 — kartellrechtlicher Clean Team-Betrieb; nur ausgewaehlte, operativ unabhaengige Personen erhalten Zugang zu wettbewerbssensiblen Informationen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Gap-Analyse: Bewertungsmatrix

| Status | Bedeutung | Handlung |
|---|---|---|
| Vorhanden und vollstaendig | Dokument hochgeladen, aktuell, vollstaendig | Keine Aktion |
| Vorhanden, unvollstaendig | Nur Teilversion; fehlende Anlagen | IRL-Frage; Nachforderung |
| Angekuendigt aber ausstehend | Verkaefer hat Lieferung zugesagt | Follow-up; Eskalation wenn > 48h |
| Nicht vorhanden | Existenz unbekannt | Direkte IRL-Frage; ggf. Alternative anfordern |
| Verweigert | Verkaefer lehnt Offenlegung ab | Begrenzung des Disclosure Letter; Risiko im DD-Report |

## Clean-Room-Protokoll: Kartellrechtliche Anforderungen

Bei Transaktionen zwischen Wettbewerbern prueft das Bundeskartellamt den Informationsaustausch. Ein Clean Room beschraenkt sensible Informationen (Preise, Kunden, Produktionskapazitaeten) auf ein separates Team.

**Clean-Team-Anforderungen:**
1. Mitglieder operativ unabhaengig vom Wettbewerbsbetrieb (keine Einkauf, Vertrieb, Pricing)
2. Schriftliche Verpflichtung jedes Clean-Team-Mitglieds
3. Separate Raeumlichkeiten oder locked-down IT-Umgebung
4. Ergebnisse nur in aggregierter/anonymisierter Form an das Verhandlungsteam
5. Protokollierung aller Clean-Team-Aktivitaeten

## Schritt-für-Schritt-Workflow

1. **Ausgangsstatus erfassen** — Datenraum-Index gegen IRL spiegeln; fehlende Positionen markieren
2. **Prioritaeten festlegen** — kritische Pfade (Tax, Litigation, wesentliche Vertraege) zuerst
3. **Follow-up-IRL** — priorisierte Nachforderung; kurze Fristen; klare Formulierung
4. **Kartellrechtliche Pruefung** — Clean-Room-Erfordernis bei Wettbewerber-Transaktionen?
5. **Clean-Team einrichten** — Mitglieder benennen; Verpflichtung unterschreiben lassen
6. **Zugriffsebenen anpassen** — Clean-Room-Ordner im DR separat; keine Cross-Contamination
7. **DSGVO-Massnahmen** — Personaldaten anonymisieren; AVV mit Plattformanbieter pruefen
8. **Gap-Report erstellen** — Statusbericht an Deal-Team; kritische Luecken hervorheben

## Output-Template IRL-Tracker (Ausschnitt)

**Adressat:** Deal-Team / DD-Koordinator — Tonfall strukturiert, actionable

```
IRL-TRACKER (INFORMATION REQUEST LIST)
Transaktion: [DEAL-NAME]
Stand: [DATUM]

| Nr. | Workstream | Dokument | Erwartet von | Faellig | Status | Datenraum-ID |
|-----|-----------|---------|-------------|---------|--------|-------------|
| 1.1 | Corporate | Aktuelle Gesellschafterliste | [Verkaefer] | [Datum] | Offen | — |
| 1.2 | Corporate | Satzung (aktuell) | [Verkaefer] | [Datum] | Vorhanden | Tab 1.1 |
| 2.1 | Finanzen | JA 2022 geprueft | [Verkaefer] | [Datum] | Ausstehend | — |
| 3.1 | Vertraege | Top-10-Kundenvertraege | [Verkaefer] | [Datum] | Teilw. vorhanden | Tab 3.1-3.7 |
| 6.1 | Litigation | Klage LG Frankfurt Az. X | [Verkaefer] | [Datum] | Verweigert | — |

KRITISCHE LUECKEN:
- [Nr.]: [Beschreibung] — Eskalation an [NAME] bis [Datum]

CLEAN-ROOM-STATUS:
Team: [NAMEN]
Zugriffsrechte seit: [Datum]
Verpflichtungen unterschrieben: [Ja/Nein]
```

## Rote Schwellen

- Clean-Room-Verletzung (Wettbewerbsinfo ohne Clean-Team) → § 1 GWB; Kartellbusse moeglich
- Personaldaten ungeschwetzt im Datenraum → DSGVO-Bussgeld; Betriebsrat-Rechte verletzt
- Wesentliche Dokumente nicht hochgeladen bis DD-Deadline → DD-Report-Luecken; Seller-Haftungsrisiko
- Keine Download-Protokollierung → kein Nachweis Kaeufer-Kenntnis bei spaeterem Streit

## Quellen

- Art. 5, 28 DSGVO; §§ 1, 19 GWB; § 17 UWG; Art. 18 MAR
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 5
