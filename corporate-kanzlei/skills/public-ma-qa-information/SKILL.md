---
name: public-ma-qa-information
description: "Public MA QA Information: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Public MA QA Information

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Public MA QA Information** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-public-ma-kapitalmarkt-mar` | Public M&A und Kapitalmarkt: Begleitet Öffentliche Angebote (WpueG), Pflichtangebote, Squeeze-Out und Delisting. Normen: WpueG, AktG §§ 327a-f, WpHG/MAR Ad-hoc, §§ 39a-c WpueG. Leitsaetze BGH und BaFin-Praxis. |
| `corporate-kanzlei-qa-information-requests` | Q&A- und Information-Request-Management in M&A-Transaktionen: DD-Team erhaelt schriftliche Datenraum-Fragen und muss konsistente Antworten mit Disclosure-Wirkung erstellen. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis SPA, MAR Insider-Abgrenzung. Prüfraster: Konsistenz mit Disclosure Schedules, Freigabeprozess, Protokollierung, Wirkung als Disclosure-Erweiterung. Output Q&A-Log, Antwort-Protokoll, Disclosure-Ergaenzungs-Memo. Abgrenzung: Datenraum-Aufbau siehe datenraum-aufbau; Disclosure Schedules siehe disclosure-schedules. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Public MA QA Information**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-public-ma-kapitalmarkt-mar`

**Fokus:** Public M&A und Kapitalmarkt: Begleitet Öffentliche Angebote (WpueG), Pflichtangebote, Squeeze-Out und Delisting. Normen: WpueG, AktG §§ 327a-f, WpHG/MAR Ad-hoc, §§ 39a-c WpueG. Leitsaetze BGH und BaFin-Praxis.

# Public M&A und Kapitalmarkt / MAR

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Public M&A und Kapitalmarkt / MAR` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — klaere vor Beginn

1. Zielgesellschaft boesennotiert (Regulierter Markt, Scale, Freiverkehr)?
2. Art des Angebots: freiwilliges Angebot, Pflichtangebot (§§ 29 ff. WpUeG) oder Squeeze-Out?
3. Kontrollschwelle: Wurde oder wird 30 % Stimmrechtsanteil erreicht?
4. Aktuelle Beteiligungsquote des Bieters / beabsichtigte Ziel-Quote?
5. Insiderhandels-/Ad-hoc-Analyse: Kursrelevante Information vorhanden?
6. BaFin-Voranmeldung und Angebotsdokument: Timeline?
7. Fairness Opinion / Unabhaengiger Gutachter fuer Angemessenheits-Pruefung erforderlich?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§§ 1-68 WpUeG** — Wertpapieruebernahmegesetz; freiwillige und Pflicht-Angebote; Angebotsunterlagen; BaFin-Pruefung
- **§§ 29-39 WpUeG** — Pflichtangebot ab 30 % Stimmrechtsanteil; Mindestpreisregel; 3 Monate Referenzperiode
- **§§ 39a-c WpUeG** — Squeeze-Out nach Uebernahme; Ausschluss Minderheit; Gerichtliches Spruchverfahren
- **§§ 327a-f AktG** — aktienrechtlicher Squeeze-Out; Hauptgesellschafter 95 %; angemessene Barabfindung; Spruchverfahren
- **§§ 33 ff. WpHG** — Stimmrechtsmitteilungen; Schwellenwerte 5, 10, 15, 20, 25, 30, 50, 75 %
- **Art. 17 MAR** — Ad-hoc-Publizität; unverzüglich; Aufschub möglich (Insider-Liste), nationale Sanktionen nach WpHG
- **Art. 14-16 MAR** — Insiderhandelsverbot; Marktmanipulation
- **§ 39 BoeRsG / DelistingVO** — Delisting; Pflichtangebot und Mindestpreis auch beim Rueckzug

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BaFin, Bescheid vom 27.01.2023 (veroeffentl. BaFin-Jahresbericht 2023) — Pflichtangebot: Erwerb von Stimmrechten durch Konsortium als gemeinsam handelnde Person iSd § 2 V WpUeG; Zusammenrechnung der Anteile

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prozessablauf: Oeffentliches Uebernahmeangebot (WpUeG)

| Phase | Inhalt | Norm | Frist |
|---|---|---|---|
| 1 | Voranmeldung (obligatorisch) | § 10 WpUeG | Unverzueglich nach Entscheidung |
| 2 | Angebotsunterlage erstellen | §§ 11-14 WpUeG | Innerhalb 4 Wochen nach Voranmeldung |
| 3 | BaFin-Einreichung und -Pruefung | § 14 WpUeG | BaFin: 10 Werktage Pruefung |
| 4 | Veroeffentlichung Angebot | § 14 WpUeG | Unverzueglich nach BaFin-Freigabe |
| 5 | Annahmefrist | § 16 WpUeG | Mindestens 4 Wochen; max. 10 Wochen |
| 6 | Weitere Annahmefrist | § 16 II WpUeG | 2 Wochen nach Vollzug |
| 7 | Vollzug | § 23 WpUeG | Veroeffentlichung Ergebnis; Kaufpreis-Zahlung |
| 8 | Squeeze-Out (falls 95 %) | §§ 39a-c WpUeG | Antrag beim Landgericht |

## Pflichtangebot: Mindestpreis-Regelung (§ 31 WpUeG)

- Mindestpreis = hoeher von: (a) volumengewichteter Durchschnittskurs der letzten 3 Monate und (b) hoechster Preis, den Bieter in letzten 6 Monaten gezahlt hat
- BaFin prueft Berechnung und veroeffentlicht Mindestpreis
- Fairness Opinion nicht gesetzlich vorgeschrieben aber Marktpraxis bei grosseren Deals

## Squeeze-Out: §§ 327a-f AktG vs. §§ 39a-c WpUeG

| Merkmal | AktG §§ 327a-f | WpUeG §§ 39a-c |
|---|---|---|
| Schwelle | 95 % Grundkapital und Stimmrechte | 90 % Stimmrechte nach Uebernahme |
| Beschluss | HV-Beschluss erforderlich | Gerichtliches Verfahren |
| Abfindung | Barabfindung; IDW S1-Pruefung | Mindestpreis aus Angebot (wenn angemessen) |
| Spruchverfahren | SpruchG | SpruchG |
| Bekaempfbarkeit | Anfechtungsklage; dann Freigabeverfahren | Geringere Anfechtbarkeit |

## Ad-hoc-Publizitaet: MAR-Analyse (Art. 17 MAR)

Im Public M&A ist jede kursrelevante Information potenzielle Ad-hoc. Kursrelevant ist Information, wenn ein verstaendiger Anleger sie bei seiner Investitionsentscheidung beruecksichtigen wuerde.

**Aufschub (Art. 17 IV MAR):** Emittent kann Veroeffentlichung zulaessig aufzuschieben, wenn:
- Unverzuegliche Offenlegung berechtigte Interessen schaedigt (z.B. laufende Verhandlungen)
- Kein Irrefuehrungs-Risiko
- Geheimhaltung sichergestellt (Insider-Liste gepflegt)

Beim Signing des SPA: Pflicht zur sofortigen Ad-hoc-Meldung (kein Aufschub mehr moeglich).

## Schritt-fuer-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


1. **Strukturanalyse** — Kontrollschwelle, Stimmrechtsanteile; Pflichtangebot-Pflicht abchecken
2. **Insider-Management** — Insider-Liste anlegen; Kommunikations-Protokoll; Marktmissbrauchs-Risiko
3. **Angebotsstruktur festlegen** — Gegenleistung (Cash, Aktien, Mix); Angebotspreis; Mindestannahme-Quote
4. **Voranmeldung BaFin** — § 10 WpUeG; unverzueglich nach Vorstandsentscheidung
5. **Angebotsunterlage** — nach §§ 11-14 WpUeG; BaFin-Muster; Fairness Opinion beschaffen
6. **Gegengesellschaft-Statement** — Zielgesellschaft muss binnen 2 Wochen Stellungnahme abgeben (§ 27 WpUeG)
7. **BaFin-Pruefung** — Kooperation; Rueckfragen beantworten; ggf. Nachbesserung
8. **Veroeffentlichung und Annahmefrist** — Boersenbekanntmachung; Aktionaer-Information
9. **Ergebnis-Veroeffentlichung** — Annahmequote; Vollzug; Weitere Annahmefrist
10. **Squeeze-Out-Analyse** — wenn >90 % (WpUeG) oder >95 % (AktG): Ausschluss-Verfahren einleiten

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — oeffentliches Uebernahmeangebot nach WpUeG | Prozessablauf und Ad-hoc-Meldung nach Template unten |
| Variante A — Pflichtangebot ausgeloest (30-Prozent-Schwelle) | Mindestpreisberechnung § 31 WpUeG priorisieren |
| Variante B — feindliche Uebernahme | Abwehrmassnahmen (Poison Pill etc.) evaluieren |
| Variante C — MAR-Insiderkontrolle vorrangig | Ad-hoc-Pflicht zeitlich sichern; Insiderlisten anlegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Ad-hoc-Meldung (Auszug)

**Adressat:** Kapitalmarkt / BaFin / Boersenpublikum — Tonfall kurz, kursrelevant

```
AD-HOC-MITTEILUNG
gemaess Art. 17 MAR

[EMITTENT]
[SITZ]
[WKN / ISIN]

[DATUM], [UHRZEIT]

[FIRMA] hat heute einen Share Purchase Agreement ueber den Erwerb von [X] % der Anteile
an [ZIELGESELLSCHAFT] unterzeichnet. Das Transaktionsvolumen betraegt ca. [EUR].
Die Transaktion steht unter dem Vorbehalt der fusionskontrollrechtlichen Freigabe und
weiterer ueblicher Vollzugsbedingungen. Der Vollzug wird fuer [QUARTAL] erwartet.

[FIRMA]
[KONTAKT]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Rote Schwellen

- Pflichtangebot-Schwelle (30 %) ueberschritten ohne Veroeffentlichung → WpUeG-Verstos; BaFin-Massnahmen
- Ad-hoc-Meldung verzoegert nach Signing → Art. 17 MAR; Bussgeld bis 15 Mio. EUR oder 2.5 % Weltumsatz
- Insider-Liste unvollstaendig → Art. 18 MAR; Compliance-Risiko bei Insiderhandel-Vorwurf
- Squeeze-Out-Abfindung unangemessen → Spruchverfahren; Nachbesserungspflicht
- Voranmeldung vergessen (§ 10 WpUeG) → BaFin-Bussgeld; Verfahren unterbrochen

## Vertiefung: Delisting-Linie Macrotron/Frosta

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- WpUeG: https://www.gesetze-im-internet.de/wp_g/
- §§ 327a-f AktG: https://www.gesetze-im-internet.de/aktg/__327a.html
- WpHG: https://www.gesetze-im-internet.de/wphg/ ; §§ 33 ff. WpHG (Stimmrechtsmitteilungen): https://www.gesetze-im-internet.de/wphg/__33.html
- MAR (VO (EU) Nr. 596/2014, konsolidiert): https://eur-lex.europa.eu/eli/reg/2014/596
- SpruchG: https://www.gesetze-im-internet.de/spruchg/
- DelistingVO und Boersenrecht § 39 BoerseG: https://www.gesetze-im-internet.de/b_rsg_2007/__39.html
- BVerfG, Beschl. v. 27.04.1999 — 1 BvR 1613/94 (DAT/Altana; BVerfGE 100, 289) — Boersenkurs als Untergrenze: https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/1999/04/rs19990427_1bvr161394.html
- BaFin-Merkblaetter MAR/Ad-hoc: https://www.bafin.de/DE/Aufsicht/BoersenMaerkte/Marktmissbrauch/marktmissbrauch_node.html
- Listing Act (Verordnung (EU) 2024/2809 zur Aenderung MAR/Prospekt-VO/MiFIR; in Kraft 04.12.2024 mit gestaffelten Anwendungsdaten — Inkrafttretensdaten je Artikel pruefen): https://eur-lex.europa.eu/eli/reg/2024/2809/oj
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `corporate-kanzlei-qa-information-requests`

**Fokus:** Q&A- und Information-Request-Management in M&A-Transaktionen: DD-Team erhaelt schriftliche Datenraum-Fragen und muss konsistente Antworten mit Disclosure-Wirkung erstellen. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis SPA, MAR Insider-Abgrenzung. Prüfraster: Konsistenz mit Disclosure Schedules, Freigabeprozess, Protokollierung, Wirkung als Disclosure-Erweiterung. Output Q&A-Log, Antwort-Protokoll, Disclosure-Ergaenzungs-Memo. Abgrenzung: Datenraum-Aufbau siehe datenraum-aufbau; Disclosure Schedules siehe disclosure-schedules.

# Q&A und Information Requests

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Q&A und Information Requests` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Q&A und Information Requests

- **Corporate-Aufgabe (Q&A und Information Requests):** DD-Team erhaelt schriftliche Datenraum-Fragen und muss konsistente Antworten mit Disclosure-Wirkung erstellen.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Q&A und Information Requests und brauche einen belastbaren nächsten Schritt."
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
- `/corporate-kanzlei:corporate-kanzlei-datenraum-gap-clean-room` - wenn Informationslücken, Wettbewerberdaten oder Clean-Room-Grenzen geklärt werden müssen.
- `/corporate-kanzlei:corporate-kanzlei-due-diligence-legal` - wenn aus Unterlagen ein Corporate-/Legal-DD-Befund gebaut werden soll.
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

# Q&A und Information Requests

## Triage — klaere vor Beginn

1. Wer beantwortet Fragen: Mandant direkt, Kanzlei im Auftrag, Steuerberater, Management?
2. Datenraum-Q&A oder direkter Informationsaustausch (E-Mail, Call)?
3. Haben alle Antworten Freigabe-Pflicht (Review durch Partner vor Versand)?
4. Gibt es eingeschraenkte Fragen (Clean Room, Need-to-know)?
5. Werden Antworten archiviert und in Disclosure Letter uebergefuehrt?
6. Mehrere Bieter erhalten gleiche Antworten? (Konsistenz-Pflicht bei Auktionsprozess)

## Zentrale Normen

- **§§ 311 II, 241 II BGB** — Q&A-Antworten binden vorvertraglich; falsche Antworten = c.i.c.-Haftung
- **§ 444 BGB** — Arglist kann durch Q&A-Antworten nicht ausgeschlossen werden; vollstaendige Offenlegung noetig
- **Art. 18 MAR** — bei borsennotierten Zielgesellschaften: Q&A koennen Insider-Infos enthalten; nur autorisierte Personen duerfen antworten
- **§ 17 UWG** — Geschaeftsgeheimnis; manche Fragen zielen auf vertrauliche Informationen ab

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Q&A-Prozess: Standardablauf

| Schritt | Inhalt | Owner | Frist |
|---|---|---|---|
| Frage eingeht | Bieter stellt schriftliche Frage im DR-System | Bieter | — |
| Eingang bestaetigten | Quittung und Pruefdatum | Verkaefer-PMO | Sofort |
| Zustaendigen bestimmen | Wer beantwortet diese Frage: Legal, Tax, Management? | PMO | 24h |
| Antwort entwerfen | Entwurf durch Zustaendigen | Workstream-Lead | 48-72h |
| Review | Kanzlei oder Partner prueft Antwort; vollstaendig? Haftungsrisiko? | Partner | 24h |
| Freigabe Mandant | Bei heiklen Fragen: Mandant gibt frei | Management | 24h |
| Antwort hochladen | Im DR-System; dokumentiert | PMO | Sofort nach Freigabe |
| Q&A-Log aktualisieren | Frage, Datum, Antwort, Bearbeiter protokollieren | PMO | Sofort |

## Haeufige Fragetypen und Antwort-Empfehlungen

| Fragetyp | Vorgehen | Risiko |
|---|---|---|
| Klarstellung zu bestehendem Dokument | Vollstaendig antworten; auf Quelldokument hinweisen | Niedrig |
| Ergaenzende Informationen zu Litigation | Sorgfaeltig; vollstaendig offenbaren; keine Minimerung | Hoch (§ 444 BGB) |
| Kundenkonzentration / Umsatz-Split | Mit Mandant abstimmen; ggf. anonymisiert | Mittel |
| Zukunftsaussichten / Forecasts | Klar als Prognose kennzeichnen; keine Garantie | Mittel |
| Clean-Room-Informationen | Nur Clean-Team-Mitglieder erhalten Antwort | Mittel (Kartell) |
| Steuer-Betriebspruefungs-Details | Nur mit Steuerberater abstimmen | Hoch |

## Schritt-fuer-Schritt-Workflow

1. **Q&A-System in Datenraum einrichten** — Kategorisierung; automatische Eingangsbestaetigung
2. **Fragenkatalog erfassen** — alle Fragen taeglich auflisten; Zustaendigkeit zuweisen
3. **Antworten entwerfen** — klar, vollstaendig, keine Halbwahrheiten
4. **Freigabe-Prozess** — kritische Antworten an Senior Partner; Mandant bei Strategiefragen
5. **Konsistenz zwischen Bietern** — gleiche Frage von Bieter A und B muss gleich beantwortet werden
6. **Q&A-Log exportieren** — vollstaendiges Log vor Signing; Anlage zum Closing-Bible
7. **Disclosure-Abgleich** — welche Q&A-Antworten beeinflussen Warranties? → Disclosure Letter aktualisieren
8. **Archivierung** — Q&A-Log als Teil des DD-Archivs; 10 Jahre aufbewahren

## Output-Template Q&A-Log

**Adressat:** Deal-Team intern / PMO — laufend aktualisiert

```
Q&A-LOG
Transaktion: [DEAL-NAME]
Stand: [DATUM] / [VERSION]

| Nr. | Datum Frage | Bieter | Frage | Workstream | Antwort-Owner | Antwortdatum | Status | Antwort-Kurzfassung |
|-----|------------|--------|-------|------------|---------------|--------------|--------|---------------------|
| 1 | [Datum] | [Bieter A] | [Frage] | Legal | [Name] | [Datum] | Beantwortet | [Kurz] |
| 2 | [Datum] | [Bieter B] | [Frage] | Tax | [Steuerberater] | Ausstehend | Offen | — |

OFFENE FRAGEN: [Anzahl]
BEANTWORTET: [Anzahl]
DURCHSCHNITTLICHE ANTWORTZEIT: [Tage]
```

## Rote Schwellen

- Unvollstaendige Antwort auf Litigation-Frage → § 444 BGB; kein Haftungsausschluss moeglich
- Unterschiedliche Antworten an verschiedene Bieter → Diskriminierungsvorwurf; Vertrauensschutz gestort
- Q&A-Log nicht archiviert → kein Beweis fuer Kaeufer-Kenntnis im Streitfall
- Insider-Informationen im Q&A ohne MAR-Kontrolle → Art. 14 MAR; BaFin-Risiko
- Antwort ohne Management-Freigabe → unrichtige Information ohne Mandanten-Kontrolle

## Quellen

- §§ 311 II, 444 BGB; Art. 18 MAR; § 17 UWG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 6
