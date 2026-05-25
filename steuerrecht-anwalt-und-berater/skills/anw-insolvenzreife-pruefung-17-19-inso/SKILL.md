---
name: anw-insolvenzreife-pruefung-17-19-inso
description: "Anwaltliche Pruefung der Insolvenzreife einer GmbH/UG aus Steueranwalts-Sicht. Erstellt strukturiertes Pruefgutachten zu Zahlungsunfaehigkeit § 17 InsO (10-Prozent-/3-Wochen-Schema BGH IX ZB 50/03) und Ueberschuldung § 19 InsO (zweistufig nach IDW S 11 mit Fortbestehensprognose 24 Monate SanInsKG). Steuerspezifischer Schwerpunkt — wie Steuerschulden Lohnsteuer Umsatzsteuer Sozialversicherungsabgaben als Passiva I einzustellen sind und wie AdV nach § 361 AO bzw. Stundung § 222 AO die Faelligkeit beeinflusst. Trigger bei Mandant-GF einer Krisengesellschaft mit Steuerrueckstaenden. Endet mit Antragspflicht-Bewertung § 15a InsO und Belehrungs-Anschluss an anw-haftungswarn-15a-inso-mandant."
---

# Anwaltliche Insolvenzreife-Prüfung §§ 17, 19 InsO (Steueranwalts-Sicht)

## Zweck

Strukturiertes **anwaltliches Prüfgutachten** zur Insolvenzreife einer GmbH/UG, wenn der Steueranwalt im Mandat — typisch bei Einspruchsverfahren mit hohen Steuerrückständen, Selbstanzeige-Mandat oder AdV-Lage — erkennt, dass die Gesellschaft möglicherweise zahlungsunfähig oder überschuldet ist.

Im Gegensatz zum StB-Skill `stb-ueberschuldungspruefung-19-inso` (technische Indikation mit Ampel als Grundlage für den Mandantenhinweis) liefert dieser Skill die **vollständige rechtliche Beurteilung** mit Subsumtion, Beweiswürdigung und unmittelbarer Antragspflicht-Bewertung.

> ℹ️ **Rollenabgrenzung zu `anw-haftungswarn-15a-inso-mandant`:** Dieser Skill ist **analytisch-diagnostisch** (Prüfgutachten Insolvenzreife). Das nachgelagerte **präventiv-belehrende** Warnschreiben an den GF (§ 11 BORA-Dokumentation der Belehrung über § 15a InsO-Antragspflicht und ihre Folgen) erstellt `anw-haftungswarn-15a-inso-mandant`. Standardablauf: erst dieser Skill (Diagnose Insolvenzreife), dann `anw-haftungswarn-15a-inso-mandant` (Mandantenbelehrung + Dokumentation).

> ℹ️ **Abgrenzung Steueranwalt vs. Fachanwalt Insolvenzrecht:** Der Steueranwalt kann die Insolvenzreife rechtlich beurteilen und den Mandanten belehren (§ 3 BRAO, kein Vorbehalt für Fachanwalt). Für gerichtsfeste insolvenzrechtliche Sanierungsbegleitung, Schutzschirmverfahren (§ 270b InsO), StaRUG-Restrukturierungsplan oder Insolvenzantragstellung **Übergabe an Fachanwalt Insolvenz-/Sanierungsrecht** empfehlen. Das Power-Plugin `insolvenzrecht` (insbesondere `ueberschuldung-pruefung-19-inso`, `zahlungsunfaehigkeit-pruefung-17-inso`, `antragspflicht-15a-inso`) ist hier die fachliche Vertiefung.

## Kaltstart-Rückfragen

1. Welche Gesellschaftsform (GmbH, UG, AG, GmbH & Co. KG) — und wer ist antragspflichtig (§ 15a Abs. 1 vs. Abs. 2 InsO)?
2. Stichtag der Prüfung (heutiger Tag, oder rückwirkend ab erkennbarem Krisensignal)?
3. Bestehen aktuell Stundungsanträge oder AdV-Verfügungen für Steuerschulden? Wenn ja, welche Beträge und welche Bescheide?
4. Liegen ungezahlte Lohnsteuer- oder Sozialversicherungsabgaben vor (Sonderfall — § 266a StGB zusätzlich relevant)?
5. Aktuelle Liquiditätslage — kann die Gesellschaft die fälligen Verbindlichkeiten in den nächsten drei Wochen bedienen?
6. Existieren Sanierungskonzept, Rangrücktrittserklärungen, Gesellschafterdarlehen, Patronate?
7. Wurde durch Steuerberater oder Sanierungsberater bereits eine § 19 InsO-Prüfung durchgeführt? Wenn ja, mit welchem Ergebnis?

## Rechtlicher Rahmen

### Primärnormen

- **§ 17 InsO** — Zahlungsunfähigkeit als Eröffnungsgrund: Schuldner nicht in der Lage, fällige Zahlungspflichten zu erfüllen. Vermutung bei Zahlungseinstellung (§ 17 Abs. 2 S. 2 InsO).
- **§ 18 InsO** — Drohende Zahlungsunfähigkeit (nur bei Eigenantrag; ergibt Eigenantragsoption mit § 270b InsO Schutzschirm).
- **§ 19 InsO** — Überschuldung: Vermögen deckt die bestehenden Verbindlichkeiten nicht, **es sei denn** Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich.
- **§ 19 Abs. 2 S. 1 InsO i.V.m. SanInsKG** — Prognosezeitraum 24 Monate für Anträge bis 31.12.2026.
- **§ 15a Abs. 1 S. 1 InsO** — Antragspflicht GF/Liquidator: drei Wochen ab Zahlungsunfähigkeit, sechs Wochen ab Überschuldung.
- **§ 15a Abs. 4 InsO** — Strafbarkeit der Insolvenzverschleppung (Freiheitsstrafe bis drei Jahre).
- **§ 15b InsO** — Zahlungsverbote nach Eintritt der Insolvenzreife (löste § 64 GmbHG a.F. ab; SanInsFoG, 1.1.2021).

### Steuer-spezifische Normen

- **§ 222 AO** — Stundung von Steuerforderungen. **Wirkung auf Insolvenzreife:** Eine schriftlich bewilligte Stundung schiebt die Fälligkeit hinaus — entsprechend nicht als fällige Verbindlichkeit in den Liquiditätsstatus einzustellen. Mündliche Zusagen oder bloße Anträge ohne Bescheid genügen **nicht**.
- **§ 361 AO** — Aussetzung der Vollziehung. **Wirkung:** Die Vollziehung wird gehemmt, die Steuerforderung bleibt aber materiell bestehen und entsteht. Im Liquiditätsstatus bleibt sie als Passivum I berücksichtigungspflichtig, soweit die AdV nicht zur Fälligkeitsverschiebung führt. Bei AdV mit Sicherheitsleistung ist die Liquiditätswirkung zusätzlich von der Sicherheitsleistung mitbeeinflusst.
- **§ 226 AO i.V.m. § 387 BGB** — Aufrechnung im Steuerrecht. Vorsteuerguthaben können gegen Steuerforderungen aufgerechnet werden, im Insolvenznähebereich aber Anfechtungsrisiko nach §§ 129 ff. InsO.
- **§ 69 AO** — Haftung des Geschäftsführers für Steuerschulden der Gesellschaft. Bleibt nach Eröffnung des Insolvenzverfahrens bestehen, ggf. zusätzlich zu § 15b InsO-Haftung.
- **§ 266a Abs. 1 StGB** — Vorenthalten von Arbeitnehmer-Anteilen zur Sozialversicherung. **Strafbar** bereits bei Nichtabführung am Fälligkeitstag; trifft GF persönlich; Tatbestandsverwirklichung schon vor Insolvenzantragspflicht denkbar.
- **§ 41a EStG** — Lohnsteueranmeldung und -abführung. Anmeldungspflicht bleibt auch in der Krise; Nichtabführung führt zur GF-Haftung nach § 69 AO und ggf. § 370 AO (Steuerhinterziehung).

### Leitentscheidungen

- BGH, Beschl. v. 19.7.2007 — **IX ZB 50/03**, BGHZ 173, 286 (Zahlungsunfähigkeit: 10-Prozent-Schwelle der fälligen Verbindlichkeiten; nicht erfüllt für Dauer von **3 Wochen** zum Stichtag).
- BGH, Urt. v. 24.5.2005 — **IX ZR 123/04**, BGHZ 163, 134 (Zahlungseinstellung; auch ein einzelner gewichtiger Indizfall genügt; Forderungen der Sozialkasse besonders gewichtig).
- BGH, Urt. v. 19.11.2019 — **II ZR 233/18**, NJW 2020, 1809 (Fortbestehensprognose: tragfähiges Unternehmenskonzept plus Finanzplan; Maßstab überwiegende Wahrscheinlichkeit).
- BGH, Urt. v. 19.12.2017 — **II ZR 88/16**, BGHZ 217, 129 (Passiva II — verzahnt mit Liquiditätsprognose).
- BGH, Urt. v. 9.10.2012 — **II ZR 298/11**, BGHZ 195, 42 (insolvenzrechtliche Überschuldung; Abgrenzung handelsbilanziell vs. insolvenzrechtlich).
- BFH, Urt. v. 14.6.2016 — **VII R 24/15**, BStBl. II 2017, 88 (Haftung GF § 69 AO für Lohnsteuer in der Krise; Grundsatz anteiliger Tilgung).
- BGH, Urt. v. 14.5.2020 — **IX ZR 207/18** (Anfechtung von Steuerzahlungen; § 130 Abs. 1 InsO bei Kenntnis der Zahlungsunfähigkeit).

### Berufsständischer Hintergrund

- **IDW S 11** (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen, Stand 12.8.2021).
- **IDW S 6** (Anforderungen an Sanierungskonzepte).

## Prüfung Zahlungsunfähigkeit § 17 InsO

### Schritt 1 — Liquiditätsstatus zum Stichtag

| Aktiva I (sofort verfügbar) | Betrag |
|---|---|
| Kasse, Bankguthaben (Saldo nach Aufrechnung Kontokorrentlinie) | … EUR |
| Bestehende Kreditlinien (Stand zum Stichtag, abzüglich gesperrter Beträge) | … EUR |
| Fällige, unbestrittene Forderungen mit Eingangserwartung 14 Tage | … EUR |

| Passiva I (fällig zum Stichtag) | Betrag |
|---|---|
| Verbindlichkeiten LuL — fällig | … EUR |
| Lohn und Gehalt — laufende Periode | … EUR |
| Sozialversicherungsabgaben — fällig (Drittelung Arbeitnehmer-/Arbeitgeber-Anteil dokumentieren) | … EUR |
| Lohnsteuer und Solidaritätszuschlag — fällig nach § 41a EStG | … EUR |
| Umsatzsteuer — fällig laut Voranmeldung | … EUR |
| Sonstige Steuerverbindlichkeiten (ESt, KSt, GewSt) — fällig **abzüglich** schriftlich bewilligter Stundungen § 222 AO (Stundungsbescheid muss Fälligkeit über den Stichtag hinaus verschieben). **AdV nach § 361 AO bleibt Passiva I** — sie hemmt nur die Vollziehung, lässt die Forderung materiell fällig (siehe Abschnitt "AdV nach § 361 AO und Insolvenzreife" unten). | … EUR |
| Kreditraten und Zinsen — fällig | … EUR |
| Sonstige fällige Verbindlichkeiten | … EUR |

**Deckungslücke = Passiva I − Aktiva I.**

### Schritt 2 — BGH-Schema anwenden

| Deckungslücke | Klassifikation | Rechtsfolge |
|---|---|---|
| < 10 Prozent der Passiva I | **Zahlungsstockung** | Keine Zahlungsunfähigkeit, soweit Beseitigung binnen drei Wochen überwiegend wahrscheinlich |
| ≥ 10 Prozent, beseitigbar binnen drei Wochen | **Zahlungsstockung** | Keine Zahlungsunfähigkeit, aber Liquiditätsplan dokumentieren |
| ≥ 10 Prozent, **nicht** beseitigbar binnen drei Wochen | **Zahlungsunfähigkeit § 17 InsO** | **Antragspflicht GF binnen drei Wochen** |

### Schritt 3 — Beweiswürdigung Zahlungseinstellung

Auch ohne rechnerische Deckungslücke kann **Zahlungseinstellung** (§ 17 Abs. 2 S. 2 InsO) vorliegen. Indizien (BGH IX ZR 123/04):

- Schleppende oder ausbleibende Sozialversicherungsabgaben über zwei und mehr Monate (besonders gewichtig).
- Wiederholte Stundungsanträge oder Vollstreckungsabwehr Finanzamt.
- Lohnzahlungen nur noch Teil-/Verspätet.
- Lieferantenanforderungen nur gegen Vorkasse.
- Kreditkündigungen oder Sperrungen.
- Eigene Erklärung GF gegenüber Dritten, nicht mehr zahlen zu können.

Bereits **ein** gewichtiges Indiz kann genügen, wenn nicht widerlegt.

## Prüfung Überschuldung § 19 InsO

### Stufe 1 — Fortbestehensprognose (Primärprüfung nach IDW S 11)

Reihenfolge: **Erst Prognose, dann Status.** Bei positiver Prognose ist § 19 InsO ausgeschlossen.

Voraussetzungen für positive Prognose:

1. **Tragfähiges Unternehmenskonzept** (IDW S 6).
2. **Integrierte Planung** über 24 Monate (Ertrag, Liquidität, Bilanz).
3. **Überwiegende Wahrscheinlichkeit** (mehr als 50 Prozent), dass das Unternehmen seine fälligen Zahlungspflichten im Prognosezeitraum erfüllen kann.

→ Bei negativer Prognose: Stufe 2 zwingend.

Methodische Tiefe für die anwaltliche Begutachtung der Prognose siehe `insolvenzrecht/skills/ueberschuldung-pruefung-19-inso` und `fortbestehensprognose` (Power-Plugin) — dort gerichtsfest aufgebaut.

### Stufe 2 — Rechnerische Überschuldung (Liquidationswerte)

Bilanz wird zu Liquidationswerten umbewertet. Detail-Methode wie in `stb-ueberschuldungspruefung-19-inso`.

**Steuerspezifische Besonderheiten der Passiva-Seite:**

- **Steuerrückstände FA:** Nennwert anzusetzen, auch bei AdV (die AdV hemmt nur die Vollziehung, lässt die Forderung materiell bestehen). Bei schriftlicher Stundung § 222 AO mit Laufzeit **nach** dem Bewertungsstichtag entsprechend Bilanzierungsregel.
- **Lohnsteuer und SV-Abgaben:** immer mit Nennwert, **keine** Aufrechnung mit Vorsteuerguthaben möglich (BGH-Anfechtungsrisiko).
- **Vorsteuerguthaben:** als Aktivum (Forderung gegen FA) mit Realisierungswahrscheinlichkeit; Bedingung: kein Anfechtungstatbestand § 130, § 142 InsO.
- **Gesellschafterdarlehen mit qualifiziertem Rangrücktritt** (§ 19 Abs. 2 S. 3 InsO): **nicht** anzusetzen. Klausel-Prüfung Pflicht — qualifiziert heißt: Rangrücktritt bis zur Beseitigung der Krise und nur aus freiem Vermögen rückzahlbar.

## Wechselwirkung Antragspflicht § 15a InsO

| § 17 | § 19 (Stufe 1 + 2) | Frist § 15a InsO | Hinweis |
|---|---|---|---|
| Zahlungsunfähig | (irrelevant) | **drei Wochen** ab Eintritt | Strafbarkeit § 15a Abs. 4 InsO; Belehrung Pflicht |
| Nicht zahlungsunfähig | Überschuldet | **sechs Wochen** ab Eintritt | dito |
| Zahlungsunfähig **und** überschuldet | beide | **drei Wochen** (kürzere greift) | dito |
| Nur Krisenindikatoren, beide negativ | beide negativ | keine Frist | Beobachtungspflicht § 102 StaRUG |

**Beachte:** Bei juristischen Personen ist die Antragspflicht des § 15a InsO auch bei drohender Zahlungsunfähigkeit (§ 18 InsO) **nicht** Pflicht — § 18 InsO ist **Eigenantragsoption** (mit Schutzschirm § 270b InsO oder StaRUG-Restrukturierung als Alternative).

## Ergebnis-Klassifikation und Anschluss

| Ergebnis | Folge im Mandat |
|---|---|
| Beide negativ | Krisenfrüherkennung dokumentieren (§ 102 StaRUG), Wiedervorlage 4 Wochen |
| § 18 InsO drohende Zahlungsunfähigkeit | Schutzschirmverfahren § 270b InsO oder StaRUG-Restrukturierung prüfen — **Übergabe Fachanwalt Insolvenzrecht** |
| § 17 InsO | **Sofortige** Belehrung GF (drei Wochen Frist) — `anw-haftungswarn-15a-inso-mandant` ausführen |
| § 19 InsO | **Sofortige** Belehrung GF (sechs Wochen Frist) — `anw-haftungswarn-15a-inso-mandant` ausführen |
| Beide | Belehrung mit dreiwöchiger Frist; gleichzeitig steuerstrafrechtliche Sonderlagen prüfen (§ 266a StGB, § 370 AO bei Lohnsteuer-Nichtabführung) |

## Steuer-spezifische Sonderlagen

### AdV nach § 361 AO und Insolvenzreife

Eine erfolgreich gewährte AdV verschiebt die Vollziehung, nicht die Fälligkeit der materiellen Steuerforderung. Im Liquiditätsstatus § 17 InsO: **AdV-Beträge bleiben Passiva I**, sofern nicht zugleich eine Stundung § 222 AO mit Fälligkeitsverschiebung bewilligt ist. Anders herum: die AdV verhindert die Vollstreckung, beseitigt aber **nicht** den Insolvenzgrund. Mandant darauf hinweisen, dass eine AdV den Insolvenzantrag nicht abwendet.

### Stundung § 222 AO und Insolvenzreife

Schriftlich bewilligte Stundungsbescheide mit Fälligkeitstermin nach dem Bewertungsstichtag dürfen aus Passiva I herausgenommen werden — soweit die Stundung sicher gewährt und nicht widerruflich ist. **Mündliche Zusagen oder bloße Anträge ohne Bescheid genügen nicht** und sind voll als fällig zu führen.

### Lohnsteuer und Sozialversicherungsabgaben in der Krise

Auch bei Liquiditätsengpässen müssen Lohnsteuer und SV-Beiträge **vorrangig** bedient werden — sonst:

- **§ 69 AO** GF-Haftung für Lohnsteuer (anteilige Tilgungsregel BFH VII R 24/15).
- **§ 266a StGB** Strafbarkeit für vorenthaltene Arbeitnehmer-Anteile zur Sozialversicherung.
- Bei späterer Insolvenz: Anfechtungsrisiko der Sozialkasse nach § 130 InsO ist gering (BGH erkennt Sozialkasse als bevorrechtigt im Krisenkontext).

### Selbstanzeige und Insolvenzreife — Konfliktlage

Ist der Mandant zugleich in Verhandlung über Selbstanzeige (§ 371 AO) und Insolvenzreife absehbar:

- Selbstanzeige **vor** Insolvenzantrag wirkt als strafbefreiend (sofern Nachzahlung trotz Insolvenz binnen Frist § 371 Abs. 3 AO möglich).
- Insolvenzanmeldung des FA als Sperrgrund § 371 Abs. 2 Nr. 1 AO prüfen.
- Detail-Workflow `anw-selbstanzeige-371` und `anw-steuerstrafverteidigung-verstaendigung`.

## Versand und Dokumentation

- Internes Prüfgutachten zu Akte (datiert, mit Datengrundlage).
- Bei festgestellter Insolvenzreife: Anwaltliches Belehrungsschreiben über `anw-haftungswarn-15a-inso-mandant` — schriftlich, mit Empfangsbestätigung (Einschreiben mit Rückschein oder beA an Mandantenvertretung; **kein ELSTER**, da nicht Empfänger Finanzbehörde).
- Aktenvermerk Mandantengespräch über § 15a InsO-Belehrung mit Datum und ggf. Zeugen.

## Querverweise

### Innerhalb Steuer-Plugin

- `stb-bwa-sus-bilanz-pruefung` — vorgelagerte Auswertung (StB-Seite).
- `stb-ueberschuldungspruefung-19-inso` — StB-technische Indikation; löst diesen Anwalts-Skill aus, wenn Mandant zum Steueranwalt kommt.
- `stb-liquiditaetsvorschau-3wochen` — Datengrundlage § 17 InsO.
- `anw-haftungswarn-15a-inso-mandant` — nachgelagerte anwaltliche Belehrung GF.
- `anw-aussetzung-vollziehung` — Wechselwirkung AdV mit Insolvenzreife.
- `anw-selbstanzeige-371` — Konfliktlage Selbstanzeige und Insolvenz.

### Power-Plugins (fachliche Vertiefung — Übergabe-Empfehlung)

- `insolvenzrecht/skills/ueberschuldung-pruefung-19-inso` — gerichtsfeste insolvenzrechtliche Prüfung Stufe 1 plus Stufe 2.
- `insolvenzrecht/skills/zahlungsunfaehigkeit-pruefung-17-inso` — vollständiges § 17 InsO-Gutachten.
- `insolvenzrecht/skills/antragspflicht-15a-inso` — vertiefte § 15a InsO-Antragspflicht- und Verschleppungs-Analyse.
- `fortbestehensprognose` — separates Power-Plugin: IDW S 6/S 11-konforme Prognose mit Kaltstart bis Zusammenführung.
- `krisenfrueherkennung-starug` — § 102 StaRUG Krisenfrüherkennung und Hinweispflichten.
- `liquiditaetsplanung/skills/liquiditaetsvorschau-insolvenzrechtlich` — gerichtsfeste insolvenzrechtliche Liquiditätsbilanz BGH-Passiva-II-Schema.
- `fachanwalt-insolvenz-sanierungsrecht` — Übergabe für Fachanwalt-Tätigkeit (Schutzschirm, Antragstellung, Plan).

## Quellen und Updates

Stand: 05/2026. Maßgebliche Reformen berücksichtigt: SanInsKG (24-Monats-Prognose bis 31.12.2026), SanInsFoG (§ 15b InsO statt § 64 GmbHG a.F.), JStG 2024 (§ 87a Abs. 1 S. 2 AO n.F. — ELSTER-Pflicht gegenüber Finanzbehörde). Bei Verlängerung oder Auslaufen des SanInsKG ab 1.1.2027 Prognosezeitraum-Default zurück auf 12 Monate — bitte Stichtag prüfen.
