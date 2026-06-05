---
name: umwandlungsrecht-wi-insurance
description: "Umwandlungsrecht WI Insurance: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Umwandlungsrecht WI Insurance

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Umwandlungsrecht WI Insurance** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-umwandlungsrecht` | Umwandlungsrecht: Begleitet Verschmelzung, Spaltung, Formwechsel und Vermögensuebertragung nach UmwG. Normen: §§ 2-122 UmwG (Verschmelzung), §§ 123-173 UmwG (Spaltung), §§ 190-304 UmwG (Formwechsel). Schluesselentscheidungen BGH und BayObLG. |
| `corporate-kanzlei-wi-insurance` | W&I-Versicherung (Warranty & Indemnity Insurance) strukturieren und prüfen: M&A-Berater braucht Policen-Analyse oder Underwriting-Vorbereitung. Normen: SPA Reps & Warranties, VVG, englisches Insurance-Recht (Lloydserfahrung). Prüfraster: Kaeufer- vs. Verkaeufer-Policy, Underwriting-Prozess, No-Claims-Declaration, Deckungsluecken, Enhanced-Disclosure. Output Policy-Review-Memo, Gap-Analyse Deckung vs. SPA-Exposure, Underwriting-Information-Pack. Abgrenzung: SPA-Reps siehe spa-apa-entwurf; Disclosure Schedules siehe disclosure-schedules. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Umwandlungsrecht WI Insurance**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-umwandlungsrecht`

**Fokus:** Umwandlungsrecht: Begleitet Verschmelzung, Spaltung, Formwechsel und Vermögensuebertragung nach UmwG. Normen: §§ 2-122 UmwG (Verschmelzung), §§ 123-173 UmwG (Spaltung), §§ 190-304 UmwG (Formwechsel). Schluesselentscheidungen BGH und BayObLG.

# Umwandlungsrecht — Verschmelzung, Spaltung, Formwechsel

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Umwandlungsrecht — Verschmelzung, Spaltung, Formwechsel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — klaere vor Beginn

1. Welche Umwandlungsart: Verschmelzung (§§ 2 ff. UmwG), Spaltung (§§ 123 ff. UmwG), Formwechsel (§§ 190 ff. UmwG) oder Vermoegensuebertragung (§§ 174 ff. UmwG)?
2. Welche Rechtsformen sind beteiligt: GmbH, AG, KG, GbR (nach MoPeG)?
3. Grenzueberschreitend? → Sondernormen SEVIC, UmwandlungsRL 2019/2121/EU, Umsetzung durch UmwG-Novelle 2023
4. Steuerlich gewuenschte Behandlung: steuerneutraler Uebergang (§§ 11 ff. UmwStG) oder Realisierung?
5. Minderheitsgesellschafter: Ausstiegsrecht, Abfindung, Andienungspflicht?
6. Arbeitnehmer: § 613a BGB analog; Information und Beratung Betriebsrat (§§ 5, 21 UmwG)?
7. Insolvenzfall: Umwandlung in der Krise nach StaRUG oder InsO?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§§ 2-122 UmwG** — Verschmelzung (Aufnahme und Neugründung); Verschmelzungsvertrag, Verschmelzungsbericht, HV/GV-Beschluss 3/4-Mehrheit
- **§§ 123-173 UmwG** — Spaltung (Aufspaltung, Abspaltung, Ausgliederung); partieller Vermoegensuebertrag
- **§§ 190-304 UmwG** — Formwechsel; Identitaet der Gesellschaft bleibt erhalten; Anteilsneubegründung
- **§§ 174-189 UmwG** — Vermoegensuebertragung auf oeffentliche Hand
- **§§ 11-25 UmwStG** — Steuerneutrale Umwandlung; Ansatz von Buchwerten; Sperrfrist 5 Jahre
- **§ 613a BGB** — Betriebsuebertragung bei Spaltung/Ausgliederung; Arbeitnehmeruebertritt
- **§§ 5, 21, 29 UmwG** — Pflichten gegenueber Arbeitnehmern; Auskunftsrechte; Widerspruchsrecht
- **Richtlinie (EU) 2019/2121** — Grenzueberschreitende Umwandlungen; Umgesetzt in §§ 305 ff. UmwG (n.F.)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pruefungsschema: Verschmelzung (§§ 2 ff. UmwG)

| Schritt | Inhalt | Norm | Frist/Formalitaet |
|---|---|---|---|
| 1 | Verschmelzungsvertrag oder -plan | §§ 4-6 UmwG | Notarielle Beurkundung |
| 2 | Verschmelzungsbericht | § 8 UmwG | Pruefung durch unabh. Pruefer |
| 3 | Pruefung durch Verschmelzungspruefer | § 9 UmwG | Bestellung durch Gericht |
| 4 | Einberufung HV/GV | § 47 UmwG | 30 Tage vor Beschluss |
| 5 | HV/GV-Beschluss | § 13 UmwG | 3/4-Mehrheit (Kapital+Stimmen) |
| 6 | Ggf. Klageverzichtsfrist | §§ 14 ff. UmwG | 1 Monat; Freigabeverfahren |
| 7 | Anmeldung Handelsregister | § 16 UmwG | Notarielle Anmeldung beider Gesellschaften |
| 8 | Eintragung → Wirksamkeit | § 20 UmwG | Gesamtrechtsnachfolge wirksam |
| 9 | Arbeitnehmer-Information | §§ 5, 21 UmwG | Spaetest. 1 Monat vor HV/GV |

## Spaltungsarten im Ueberblick

| Art | Rechtsfolge | Typischer Anwendungsfall |
|---|---|---|
| Aufspaltung (§ 123 I UmwG) | Uebertragende Gesellschaft erloscht; gesamtes Vermoegen geht auf mind. 2 aufnehmende ueber | Konzernaufloesung, Carve-Out |
| Abspaltung (§ 123 II UmwG) | Uebertragende Gesellschaft besteht fort; Teil des Vermoegens geht auf aufnehmende ueber | Ausgliederung einer Geschaeftssparte |
| Ausgliederung (§ 123 III UmwG) | Wie Abspaltung, aber Gegenleistung sind Anteile an der aufnehmenden Gesellschaft — kommen der uebertragenden Gesellschaft, nicht den Gesellschaftern zu | Holdingstruktur aufbauen; Tochtergesellschaft gruenden |

## Schritt-fuer-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


1. **Umwandlungsart und Zielstruktur bestimmen** — Verschmelzung, Spaltung, Formwechsel; Steuerberatung einbeziehen (UmwStG)
2. **Timeline aufstellen** — Gesamtdauer Verschmelzung: typisch 3-5 Monate (Vertrag → HV → Registereintragung)
3. **Vertragsentwurf erstellen** — Verschmelzungsvertrag/Spaltungsplan; Notar einbinden
4. **Sachverstaendigenpruefung** — Verschmelzungspruefer durch Gericht bestellt; unabhaengige Bewertung
5. **Arbeitnehmer informieren** — § 5 UmwG Protokoll; Betriebsrat konsultieren; Widerspruchsrecht nach § 613a VI BGB
6. **HV/GV-Beschluesse** — Einberufung, Beschluss mit qualifizierter Mehrheit; Protokoll notariell
7. **Anmeldung Handelsregister** — Notarielle Anmeldung; Freigabeverfahren wenn Klage eingereicht
8. **Steuerneutralitaet sichern** — UmwStG-Antrag auf Buchwertfortfuehrung; Sperrfrist 5 Jahre beachten
9. **Post-Umwandlung** — Vertragsanpassungen (neue Firma, IBAN, Steuernummer); Gesellschafter- und Glaeubigerschutz

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Verschmelzung nach UmwG vorbereiten | Pruefschema und Verschmelzungsvertrag-Outline nach Template unten |
| Variante A — Spaltung statt Verschmelzung vorzugsweise | Spaltungsarten vergleichen; Abspaltung oder Ausgliederung waehlen |
| Variante B — steuerliche Optimierung vorrangig | § 15 UmwStG pruefen; Buchwertfortfuehrung sichern |
| Variante C — Umwandlung mit Auslandsbezug | Grenzueberschreitende Verschmelzung; SE-Option und UmwRL pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Verschmelzungsvertrag Outline

**Adressat:** Notar / Gesellschafter — Tonfall sachlich-juristisch

```
VERSCHMELZUNGSVERTRAG
gemaess §§ 4-6 UmwG

Urkundennummer: [Nr.]
Datum: [DATUM]
Notar: [NAME, ADRESSE]

PRAEMBEL

1. VERTRAGSPARTEIEN
 Uebertragende Gesellschaft (1): [FIRMA, Sitz, HRB-Nr.]
 Aufnehmende Gesellschaft: [FIRMA, Sitz, HRB-Nr.]

2. GEGENSTAND DER VERSCHMELZUNG
 Die uebertragende Gesellschaft uebertraegt ihr Vermoegen einschliesslich aller Verbindlichkeiten
 im Wege der Verschmelzung durch Aufnahme auf die aufnehmende Gesellschaft.

3. GEWAEHRUNG VON ANTEILEN (§ 5 UmwG)
 Umtauschverhaeltnis: [X Anteile an aufnehmender Gesellschaft fuer Y Anteile an uebertragender]
 Zuzahlung: [keine / [Betrag EUR]]

4. BEWERTUNGSSTICHTAG UND BUCHWERT
 Stichtag: [DATUM]; Buchwertfortfuehrung nach § 11 UmwStG: [Ja / Nein]

5. RECHTE DER INHABER BESONDERER RECHTE

6. MASSNAHMEN FUER ARBEITNEHMER (§ 5 Nr. 8 UmwG)

7. GLAEUBIGERBENACHRICHTIGUNG (§ 22 UmwG)

8. VERSCHMELZUNGSZEITPUNKT (§ 5 Nr. 6 UmwG)

9. KOSTEN

10. SONSTIGES
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Rote Schwellen

- Bewertungsstichtag nicht mehr als 8 Monate vor Anmeldung (§ 17 II UmwG) → Pruefungserfordernis
- Arbeitnehmer nicht fristgerecht informiert (§ 5 UmwG) → Beschluss anfechtbar
- Steuerneutralitaet vergessen → UmwStG-Buchwertfortfuehrungsantrag nachholen nicht moeglich
- Fusionskontrolle uebersehen → Verschmelzung ggf. untersagt; Entflechtung
- Sperrfrist UmwStG (5 Jahre) nicht beachtet → rueckwirkende Steuerpflicht

## Vertiefung: Spruchverfahren nach Umwandlung

Minderheitsgesellschafter koennen im Spruchverfahren (§§ 2, 34 ff. SpruchG) eine angemessene Barabfindung nach § 29 UmwG oder Verbesserung des Umtauschverhaeltnisses verlangen. Bewertung nach IDW S1 (Ertragswertmethode). Verfahrensdauer: typisch 2-5 Jahre, ggf. laenger.

## Quellen

- §§ 2-304 UmwG; §§ 11-25 UmwStG; § 613a BGB; SpruchG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 2. `corporate-kanzlei-wi-insurance`

**Fokus:** W&I-Versicherung (Warranty & Indemnity Insurance) strukturieren und prüfen: M&A-Berater braucht Policen-Analyse oder Underwriting-Vorbereitung. Normen: SPA Reps & Warranties, VVG, englisches Insurance-Recht (Lloydserfahrung). Prüfraster: Kaeufer- vs. Verkaeufer-Policy, Underwriting-Prozess, No-Claims-Declaration, Deckungsluecken, Enhanced-Disclosure. Output Policy-Review-Memo, Gap-Analyse Deckung vs. SPA-Exposure, Underwriting-Information-Pack. Abgrenzung: SPA-Reps siehe spa-apa-entwurf; Disclosure Schedules siehe disclosure-schedules.

# W&I-Versicherung (Warranty & Indemnity Insurance)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `W&I-Versicherung (Warranty & Indemnity Insurance)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


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

# W&I-Versicherung (Warranty & Indemnity Insurance)

## Triage — klaere vor Beginn

1. Kaeufer-Policy (haeufiger) oder Verkaefer-Policy (seltener)?
2. Dealgroesse und Transaktionsvolumen — Mindestpraemie ca. 150-200 TEUR; W&I sinnvoll ab ca. 15-20 Mio. EUR EV
3. Welche Workstreams sind im Scope der W&I (Legal, Tax, Environmental, Financial)?
4. Kenntnis-Definition: "Best Knowledge" oder "Actual Knowledge" des Verkaefers?
5. Retention / Selbstbehalt: De-Minimis, Basket (Tipping vs. Deductible), Cap (Underwriting Limit)?
6. Underwriting-Zeitplan: Minimum 2 Wochen fuer Underwriting nach vollstaendigem DD-Report?
7. Sind Fundamental Warranties (Title, Authority, Kapitalstruktur) mit laengerem Zeitlimit versichert?

## Zentrale Regelwerke

- **Versicherungsvertragsgesetz (VVG)** — §§ 1-20 VVG allgemeine Versicherungspflichten; § 21 VVG vorvertragliche Anzeigepflicht
- **W&I-Marktstandard (deutsch/englisch)** — Keine gesetzliche Spezialregelung; Marktstandard nach BIPAR, LMA, GDV
- **SPA-Schnittstelle** — Vertragsklausel: "Kaeufer-Policy erhaeltlich; Verkaefer-Haftung auf Betrag X beschraenkt (Excess unter Policy)"
- **Tax W&I / Tax-Indemnity** — separates Instrument fuer bekannte Steuerrisiken; nicht unter allgemeiner W&I

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## W&I-Versicherungsstruktur: Uebersicht

### Kaeufer-Policy (Buyer-Side)
- Kaeufer ist Versicherungsnehmer und Beguenstigter
- Verkaefer haftet nur noch in Hoehe des Selbstbehalts (Excess) — oft 0 EUR bei Nil-Seller-Liability-Strukturen
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
| Forward-Looking Reps | Reps ueber Zukunftserwartungen | Kein Schutz; earmarked risks |
| Environmental / Umwelt | Bodenkontamination; Altlasten | Separate Umwelt-Policy; Environmental Indemnity |
| Purchase Price Adjustment | Working Capital/Net Debt-Anpassungen | Separate Purchase Price-Mechanismus |
| Pension Deficits | Unterdeckung bei Pensionsverpflichtungen | Separate Pension Indemnity im SPA |
| Tax W&I | Nur allgemein; bekannte Tax-Risiken | Separate Tax-Indemnity im SPA |

## Schritt-fuer-Schritt-Workflow

1. **W&I-Entscheidung** — sinnvoll? Transaktionsvolumen, Verkaefer-Typ (PE), DD-Qualitaet
2. **Broker beauftragen** — spezialisierter W&I-Broker (Willis, AON, Lockton, Marsh)
3. **Underwriting-Info-Memo** — Deal-Summary; DD-Report; Entwurf SPA
4. **Non-Binding Indications** — Praemienvergleich mind. 2-3 Angebote
5. **Underwriting-Workshop** — Underwriter stellen DD-Fragen; bekannte Risiken offen erlaeutern
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
 → Ja: W&I fuer unbekannte Risiken; Indemnities fuer bekannte
 → Nein: W&I als kosteneffizienter Ersatz fuer Haeftungsrisiko
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
- W&I-Marktstandard: LMA-Modellklauseln, GDV-Hinweise (Stand pruefen).
- Im SPA-Kontext: §§ 311 II, 280 BGB (W&I deckt regelmaessig Garantieverletzungen § 311 I BGB oder vertragliche Schadensersatzregelungen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
