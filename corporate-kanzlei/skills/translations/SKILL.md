---
name: translations
description: "Mehrsprachige Transaktionsdokumente in DE/EN erstellen und prüfen: Internationale M&A-Transaktion erfordert konsistente Terminologie in beiden Sprachen. Normen: § 184 GVG (Deutsch als Gerichtssprache), EGBGB Art. 10 ff. (Sprache des Rechtsgeschäfts), Governing-Language-Klauseln. Prüfraster: Terminologie-Konsistenz, Governing-Language, Notarerfordernis Übersetzung, Divergenz-Risiken. Output Mehrsprachiges Dokument, Terminologie-Glossar, Gouvernance-Language-Klausel. Abgrenzung: Reine Übersetzung ohne Rechtsinhalt ist kein Rechtsfall; substantielle Aenderungen siehe spa-apa-entwurf."
---

# Multijurisdiktionale Uebersetzungen und Dokumente

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Multijurisdiktionale Uebersetzungen und Dokumente

- **Corporate-Aufgabe (Multijurisdiktionale Uebersetzungen und Dokumente):** Internationale M&A-Transaktion erfordert konsistente Terminologie in beiden Sprachen.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Multijurisdiktionale Uebersetzungen und Dokumente und brauche einen belastbaren nächsten Schritt."
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

### Multijurisdiktionale Uebersetzungen und Dokumente

## Triage — klaere vor Erstellung

1. Welche Sprachen: Deutsch, Englisch, oder weitere Jurisdiktionen (FR, NL, PL)?
2. Governing Language: Welche Sprachfassung ist verbindlich bei Widerspruechen?
3. Notarieller Beglaubigungsbedarf: Notarielle Uebersetzung erforderlich (z.B. für ausl. Handelsregister)?
4. Welche Terminologie-Konventionen: Deutsche Rechtsbegriffe, englisches Common-Law-Aequivalent, oder neutrale Begriffe?
5. Wer prueft Uebersetzung: zugelassener Dolmetscher, Kanzlei, Mutterhaus?
6. Wann muessen Dokumente vorliegen: Signing-Termin mit internationalem Notar?

## Zentrale Normen

- **§ 184 GVG** — Gerichtssprache Deutsch; in deutschen Verfahren muss Schriftverkehr deutsch sein
- **Art. 10 ff. EGBGB** — Internationales Privatrecht; Vertragsstatut; welche Rechtsordnung und Sprache gilt
- **Art. 3 I Rom-I-VO (EG 593/2008)** — freie Rechtswahl; auch Sprachenwahl im internationalen Vertrag
- **§ 189 ZPO** — Vorlage von Urkunden in Originalsprache; Uebersetzung als Anlage
- **§ 30 BeurkG** — notarielle Urkunden muessen in Deutschland in deutscher Sprache errichtet werden; Zweisprachigkeit moeglich (§ 5 BeurkG)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Terminologie-Mapping: Deutsch / Englisch

| Deutscher Begriff | Englische Entsprechung (DE-Recht-Bezug) | Common Law-Aequivalent |
|---|---|---|
| Gesellschaft mit beschraenkter Haftung (GmbH) | limited liability company (GmbH) | private limited company (Ltd.) [UK] |
| Aktiengesellschaft (AG) | stock corporation (AG) | public limited company (plc) [UK] |
| Geschaeftsfuehrer | managing director | managing director [UK]; CEO/president [US] |
| Hauptversammlung | general meeting | general meeting [UK]; shareholder meeting [US] |
| Aufsichtsrat | supervisory board | board of directors (if one-tier) |
| Gewinnabfuehrungsvertrag | profit and loss transfer agreement | (no direct equivalent) |
| Handelsregister | commercial register | Companies House [UK]; business register |
| Verschmelzung | merger (by way of absorption) | merger [US]; amalgamation [UK] |
| Ausgliederung | hive-down (contribution in kind) | hive-down [UK] |
| Gesamtrechtsnachfolge | universal succession | not a common-law concept |

## Governing-Language-Klausel

Empfohlene Formulierung (SPA):
> "This Agreement has been prepared in the German language, which shall be the authoritative and governing language for all purposes, including in the event of any dispute or ambiguity. Any translation into another language is for convenience only and shall not affect the interpretation of this Agreement."

Gegenformulierung (Kaeufer bevorzugt English):
> "This Agreement is prepared in both the German and English language. In the event of any inconsistency between the two versions, the English version shall prevail."

## Schritt-für-Schritt-Workflow

1. **Sprachanforderungen klaeren** — Governing Language, Uebersetzungsbedarf, Notarpflicht
2. **Erstfassung erstellen** — immer in Mutterrechtssprache; dann Uebersetzung
3. **Terminologie-Check** — kritische Rechtsbegriffe einheitlich uebersetzen
4. **Vier-Augen-Pruefung** — muttersprachlicher Anwalt oder Dolmetscher mit Rechtskenntnissen
5. **Konsistenzcheck** — alle Definitionen in beiden Sprachfassungen identisch
6. **Governing Language definieren** — explizite Klausel einfuegen
7. **Beglaubigung pruefen** — wenn auslaendisches Register: vereidigter Dolmetscher erforderlich

## Output-Template Zweisprachige Vollmacht (Ausschnitt)

```
VOLLMACHT / POWER OF ATTORNEY

Der Unterzeichner, [NAME], handelnd als Geschaeftsfuehrer / The undersigned, [NAME], acting as managing director
der [FIRMA GmbH] / of [FIRMA GmbH]
erteilt hiermit / hereby grants

[BEVOLLMAECHTIGTER NAME] / [NAME OF ATTORNEY-IN-FACT]

folgende Vollmacht / the following power of attorney:

...den Kaufvertrag ueber alle Geschaeftsanteile zu unterzeichnen und alle Massnahmen
zu ergreifen, die für den Vollzug der Transaktion erforderlich sind...

...to sign the share purchase agreement for all shares and to take all actions
required for the completion of the transaction...

Diese Vollmacht ist in der deutschen Sprache abgefasst; die englische Uebersetzung
dient nur zur Information. Im Zweifelsfall gilt die deutsche Fassung.
/ This power of attorney is drawn up in German; the English translation is for information
purposes only. In case of doubt, the German version shall prevail.

[ORT / PLACE], [DATUM / DATE]
[UNTERSCHRIFT / SIGNATURE]
```

## Rote Schwellen

- Keine Governing-Language-Klausel → Auslegungsstreit bei Widerspruechen zwischen Sprachfassungen
- Terminologie inkonsistent (z.B. Aufsichtsrat mal supervisory board, mal board of directors) → Auslegungsrisiko
- Eigene Kanzlei-Uebersetzung für ausl. Handelsregister → nicht verwendbar ohne beeidigten Dolmetscher
- Zeitdruck: Uebersetzung ohne angemessene Pruefung → Fehler in bindenden Dokumenten

## Quellen

- § 184 GVG; Art. 3 Rom-I-VO; Art. 10 ff. EGBGB; § 30 BeurkG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
