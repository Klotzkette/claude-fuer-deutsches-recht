---
name: signing-closing-conditions
description: "Signing und Closing Conditions verwalten: M&A-Transaktion naehert sich Signing oder Closing und alle CPs muessen erledigt sein. Normen: § 158 BGB (Bedingungseintritt), SPA Conditions Precedent, § 41 GWB (Vollzugsverbot). Prüfraster: CP-Checkliste, Behördengenehmigungen, Eigentumsuebergang, MAC-Kl..."
---

# Signing und Closing Conditions

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Signing und Closing Conditions

- **Corporate-Aufgabe (Signing und Closing Conditions):** M&A-Transaktion naehert sich Signing oder Closing und alle CPs müssen erledigt sein.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Signing und Closing Conditions und brauche einen belastbaren nächsten Schritt."
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

### Signing und Closing Conditions

## Triage — klaere vor Beginn

1. Welche Closing Conditions sind im SPA definiert?
2. Wer ist CP-Owner für jede Bedingung (Kaeufer, Verkaefer, beide)?
3. Behordliche Genehmigungen: Kartellrecht, FDI, Sektorregulierung — Fristen?
4. Dritte Zustimmungen: Change-of-Control-Klauseln, Bankenkonsortium, Schlüssel-Kunden?
5. Long Stop Date: Wann verfaellt das SPA automatisch wenn CPs nicht erfuellt?
6. MAC-Klausel: Gibt es ein Ruecktrittsrecht bei Material Adverse Change?
7. Interim Operating Covenants: Welche Beschraenkungen gelten zwischen Signing und Closing?

## Zentrale Normen

- **§ 158 BGB** — aufschiebende und aufloesende Bedingungen; Suspensivbedingung
- **§ 160 BGB** — Pflicht zur Erhaltung des Bedingungseintritts; Nichterfuellung schadet
- **§ 162 BGB** — treuwidrige Herbeiführung oder Verhinderung des Bedingungseintritts
- **§ 41 GWB** — fusionskontrollrechtliches Vollzugsverbot; gun jumping
- **§ 56 AWV** — AWW-Investitionspruefung; Meldefrist und Prüfdauer
- **§§ 154, 155 BGB** — offener Einigungsmangel; Formpflicht beim Vertragsschluss

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Standard-Closing-Conditions-Matrix

| CP-Typ | Typischer Inhalt | CP-Owner | Prüfung | Frist |
|---|---|---|---|---|
| Regulatorisch | Kartellfreigabe GWB/FKVO; FDI-Genehmigung | Kaeufer | Behördenschreiben | Long Stop Date |
| Corporate | GV/AR-Beschluss; Unterschriften; vollstaendige Execution | Beide | Protokoll + Anlagen | Signing |
| Dritte Zustimmungen | CoC-Consents; Banken (Change-of-Control-Covenant); Schlüssel-Kunden | Meist Verkaefer | Consent Letters | Long Stop Date |
| Representations True & Correct | Keine wesentliche Unrichtigkeit der Reps zum Closing | Verkaefer | Bring-Down Certificate | Closing Day |
| No MAC | Kein Material Adverse Change eingetreten | Verkaefer | MAC Certificate | Closing Day |
| No Legal Proceedings | Kein Gerichtsentscheid oder einstweilige Verfuegung | Beide | Anwaltsbestaetigung | Closing Day |
| Deliver Closing Documents | Alle Deliverables vollstaendig | Beide | Closing Checklist | Closing Day |

## Closing-Deliverables-Checkliste

### Verkaefer-Deliverables
- [ ] Signed und datiertes SPA (Execution Version)
- [ ] Anteilsuebertragungsvertrag (GmbH: notariell; AG: Abtretungserklaerung)
- [ ] Resignationsschreiben Geschäftsführer/Vorstand (falls vereinbart)
- [ ] Bring-Down Certificate (Reps weiterhin richtig)
- [ ] No-MAC-Certificate
- [ ] Consents (CoC, Banken, Schlüsselkunden)
- [ ] Gesellschafterliste aktualisiert (GmbH: beim Notar)
- [ ] Handelsregister-Vollmacht
- [ ] Datenraumzugang dauerhaft sichergestellt oder CD-Archiv

### Kaeufer-Deliverables
- [ ] Signed SPA
- [ ] Kaufpreiszahlung SWIFT-Bestaetigung
- [ ] Kartellfreigabe-Schreiben (Original oder Kopie)
- [ ] FDI-Freigabe/Nichtuntersagungsbestaetigung
- [ ] W&I-Policy-Commitment Letter (wenn W&I-Versicherung)
- [ ] Firmen-Vollmacht Unterschriftsberechtigte (Handelsregisterauszug)

## Schritt-für-Schritt-Workflow

1. **CP-Liste im SPA auswerten** — jede Bedingung mit Owner, Frist und Nachweiserfordernis erfassen
2. **CP-Tracker aufbauen** — Spreadsheet mit Status, Owner, Frist, Fruehindikatoren, Eskalationsstufe
3. **Behoerdliche Anmeldungen** — Kartellrecht, FDI sofort nach Signing einleiten; Deadlines im Kalender
4. **Dritte Zustimmungen besorgen** — Consents bei CoC-Klauseln; Bankenkonsortium informieren
5. **Interim Covenants monitoren** — Verkaefer darf keine wesentlichen Änderungen ohne Zustimmung vornehmen
6. **Closing-Datum vorschlagen** — sobald alle CPs absehbar erfuellt; Notartermin (GmbH) reservieren
7. **Pre-Closing-Meeting** — alle Deliverables gegenchecken; Protokoll vorab zirkulieren
8. **Closing-Call/Meeting** — gleichzeitiger Austausch Deliverables und Kaufpreiszahlung
9. **Post-Closing-Bestaetigung** — Closing Certificate; Registereintragung initiieren

## Entscheidungsbaum: Was tun wenn CP nicht rechtzeitig erfuellt?

```
CP-Erfullung verzoegert sich?
 → Regulatorisch (Kartell/FDI)?
 → Kurze Verzoegerung: Long Stop Date verlaengern (Amendment); Behörde aktiv unterstuetzen
 → Untersagung droht: Abhilfemassnahmen (Remedies/Divestitures) verhandeln
 → Dritte Consent nicht eingeholt?
 → Wesentlich für Business: nachverhandeln; ggf. Kaufpreisabschlag
 → Unwesentlich: Waiver durch Kaeufer einholen
 → Bring-Down nicht clean (Rep-Verletzung)?
 → MAC-Schwelle erreicht: Ruecktrittsrecht pruefen (§ 162 BGB)
 → Nicht wesentlich: Waiver oder Abschlag
 → Long Stop Date erreicht?
 → Automatischer Ruecktritt per SPA-Klausel; Schadensersatz pruefen
```

## Output-Template CP-Tracker

**Adressat:** Deal-Team / PMO — Tonfall priorisiert, statusorientiert

```
CLOSING CONDITIONS TRACKER
Transaktion: [DEAL-NAME]
Stand: [DATUM]
Long Stop Date: [DATUM]

| Nr. | CP-Beschreibung | Owner | Status | Frist | Naechste Aktion | Eskalation |
|-----|----------------|-------|--------|-------|----------------|------------|
| 1 | Kartellfreigabe GWB | Kaeufer | In Pruefung | [Datum] | Follow-up Bundeskartellamt | Partner |
| 2 | FDI-Nichtuntersagung BMWK | Kaeufer | Angemeldet | [Datum] | Antwort abwarten | Partner |
| 3 | CoC-Consent Kunden-A | Verkaefer | Offen | [Datum] | Gespraeche laufend | Managing Partner |
| 4 | Bring-Down Certificate | Verkaefer | Vorbereitet | Closing Day | Am Closing-Tag ausstellen | — |
| 5 | Kaufpreiszahlung | Kaeufer | Bereit | Closing Day | SWIFT-Bestaetigung vorbereiten | — |

AMPELSTATUS: [GRUEN / GELB / ROT]
VORAUSSICHTLICHES CLOSING: [DATUM]
```

## Rote Schwellen

- Vollzugsverbot missachtet (Gun Jumping) — Bussgeld bis 10 % Weltumsatz; § 41 GWB
- Long Stop Date verstrichen ohne Verlaengerungsvereinbarung → automatischer Ruecktritt
- Bring-Down-Verletzung ignoriert → Closing ohne valide Grundlage; Ruecktrittsanspruch Kaeufer
- Dritte Consent vergessen → CoC-Kuendigung wesentlicher Verträge post-Closing
- Interim Covenants verletzt (z.B. Verkaefer verkauft Schlüsselasset vor Closing) → Schadensersatz; ggf. Ruecktritt

## Quellen

- § 158, 160, 162 BGB; § 41 GWB; § 56 AWV
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
