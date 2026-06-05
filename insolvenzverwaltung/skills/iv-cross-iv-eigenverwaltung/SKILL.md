---
name: iv-cross-iv-eigenverwaltung
description: "IV Cross IV Eigenverwaltung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Cross IV Eigenverwaltung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Cross IV Eigenverwaltung** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-cross-border-assets-trustee-registervollzug` | Insolvenzverwaltung bei Cross-Border-Assets: ausländischer trustee, debtor in possession oder monitor verwertet deutsche GmbH-Anteile, Grundstücke oder Forderungen; Anerkennung, Inzidentprüfung, Register- und Grundbuchvollzug. |
| `iv-eigenverwaltung-sachwaltung` | Sachwalter­kontrolle und Schnittstellenmanagement bei Eigenverwaltung nach §§ 270 ff. InsO. §§ 270 274 275 InsO Sachwalterbefugnisse und Kontrollrechte. Prüfraster: Rollenabgrenzung Finanzplankontrolle Rechnungslegung Anfechtung Haftung Gläubigerinformation. Output: Sachwalterberichte Beanstandungsschreiben Haftungsnotiz. Abgrenzung: nicht für Schutzschirm (iv-schutzschirm-270d) oder Planverfahren (iv-plan-kommandocenter). |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Cross IV Eigenverwaltung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-cross-border-assets-trustee-registervollzug`

**Fokus:** Insolvenzverwaltung bei Cross-Border-Assets: ausländischer trustee, debtor in possession oder monitor verwertet deutsche GmbH-Anteile, Grundstücke oder Forderungen; Anerkennung, Inzidentprüfung, Register- und Grundbuchvollzug.

# IV Cross-Border Assets — Trustee, DIP, Registervollzug

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IV Cross-Border Assets — Trustee, DIP, Registervollzug` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill ist das Insolvenzverwaltungs-Cockpit für deutsche Assets in ausländischen Insolvenzverfahren und für ausländische Assets in deutschen Verfahren. Er fragt nicht abstrakt nach „Anerkennung“, sondern baut den tatsächlichen Vollzugsweg: Welche Person darf handeln, welches Asset ist betroffen, welche deutsche Stelle prüft, welche Urkunden fehlen und wie wird die Masse gesichert?

## Typische Startfälle

- US Chapter 11 debtor in possession will GmbH-Anteile an einer deutschen Tochter übertragen.
- US trustee verkauft ein deutsches Grundstück der US-Schuldnerin.
- Kanadischer trustee/receiver/monitor will Bankkonten, Forderungen oder IP-Rechte in Deutschland verwerten.
- Deutsche Insolvenzverwaltung muss prüfen, ob eine ausländische Verfahrensperson wirklich über ein deutsches Asset verfügen darf.
- Käufer, Notar oder Grundbuchamt blockiert, weil die Rechtsmacht nicht grundbuch- oder registertauglich nachgewiesen ist.

## Entscheidungsbaum

### 1. Asset und Schuldner trennen

- **Asset des ausländischen Schuldners:** ausländisches Insolvenzstatut kann Verfügungsbefugnis verschieben; deutscher Vollzug bleibt nach deutschem Form-/Registerrecht.
- **Asset der deutschen Tochter:** Nicht automatisch Masse der ausländischen Mutter. Der office holder kontrolliert allenfalls die Gesellschafterrechte der Mutter, nicht unmittelbar das Vermögen der Tochter.
- **GmbH-Anteile:** Asset des Gesellschafters; § 15 GmbHG, § 40 GmbHG, notarielle Liste.
- **Grundstück:** lex rei sitae Deutschland; §§ 873, 925, 311b BGB, § 29 GBO.

### 2. Rechtsmacht prüfen

- EU-Verfahren: EuInsVO prüfen, insbesondere automatische Anerkennung und Befugnisse des Verwalters, aber immer mit deutschem Vollzugsrecht koppeln.
- Drittstaaten: §§ 335 ff., 343 InsO. Kein deutsches Chapter-15-Vorschaltverfahren. Anerkennung und konkrete Befugnis werden praktisch inzident geprüft.
- Ausländisches Recht: office holder status, Umfang der Befugnis, stay, plan, court approval, creditor committee consent, ordinary-course-Grenze.

### 3. Nachweisfähigkeit bauen

Für die IV-Akte wird eine Nachweismappe angelegt:

| Register | Mindestnachweise |
| --- | --- |
| Notar | Eröffnungs-/Bestellungsurkunde, Identität, Befugnis, Übersetzung, Apostille/Legalisation, AML |
| Handelsregister/Gesellschafterliste | notarielle Abtretung, neue Liste, Einreichungsbefugnis, fremdrechtliche Vertretungsmacht |
| Grundbuch | § 29 GBO, Auflassung/Bewilligung, öffentliche Urkunden, § 346 InsO bei Verfügungsbeschränkung |
| Bank/Drittschuldner | Legitimation, Vollmacht, Kontosperren, Sanktionen/AML, Zahlungsinstruktion |
| Prozessgericht | Prozessstandschaft/Parteiwechsel, Vollmacht, Aktivlegitimation |

## Masse- und Haftungsfragen

- **Masseinteresse:** Ist die deutsche Verwertung für die Masse wirtschaftlich sinnvoll, oder verursacht sie nur Vollzugskosten?
- **Drittrechte:** Pfandrechte, Vorkaufsrechte, Absonderungsrechte, Share Pledges, negative pledge, drag/tag, consent matters.
- **Anfechtung:** Ausländische avoidance actions und deutsche Insolvenzanfechtung nicht unbesehen vermischen; Kollisionsrecht und Gerichtsstand prüfen.
- **Haftung:** Wer falsch über deutsche Assets verfügt, riskiert Registerblockade, Käuferhaftung, Notarhaftungsdiskussion, Organpflichtverletzungen und spätere Insolvenzanfechtung.

## Arbeitsprodukt

Liefere:

1. **Cross-Border-Asset-Matrix:** Asset, Eigentümer, Verfahren, office holder, deutsches Vollzugsrecht, Risiko.
2. **Urkundenfahrplan:** Was liegt vor, was fehlt, welche Form braucht die deutsche Stelle?
3. **Vollzugsroute:** Notartermin, Register-/Grundbuchantrag, Insolvenzgericht nach §§ 344 bis 346 InsO, Bankfreigabe oder Deal-Stopp.
4. **Kommunikationspaket:** Fragenkatalog an ausländische counsel und Notarbrief.
5. **Massevermerk:** Nutzen, Kosten, Dauer, Risiken, Alternativverwertung.

## Stoppschilder

- Ausländischer office holder behauptet nur „control over group“, ohne Anteilseigentum und Befugnisnachweis.
- Deutsche Tochter soll Assets verkaufen, obwohl nur die Mutter insolvent ist.
- GmbH-Anteilskauf ohne notarielle Abtretung.
- Grundbuchvollzug ohne §-29-GBO-taugliche Urkunden.
- US Chapter 11 non-ordinary-course sale ohne erkennbare court approval.
- Kanadische Rolle unklar: trustee, receiver und monitor haben nicht automatisch dieselben Befugnisse.

## Quellenregel

Tragende Normen live prüfen: InsO §§ 335 ff., 343, 346 bis 348, EuInsVO, GBO § 29, GmbHG §§ 15, 40, BGB §§ 873, 925, 311b. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `iv-eigenverwaltung-sachwaltung`

**Fokus:** Sachwalter­kontrolle und Schnittstellenmanagement bei Eigenverwaltung nach §§ 270 ff. InsO. §§ 270 274 275 InsO Sachwalterbefugnisse und Kontrollrechte. Prüfraster: Rollenabgrenzung Finanzplankontrolle Rechnungslegung Anfechtung Haftung Gläubigerinformation. Output: Sachwalterberichte Beanstandungsschreiben Haftungsnotiz. Abgrenzung: nicht für Schutzschirm (iv-schutzschirm-270d) oder Planverfahren (iv-plan-kommandocenter).

# Eigenverwaltung und Sachwaltung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eigenverwaltung und Sachwaltung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Unterstützt den Sachwalter bei Kontrolle der Eigenverwaltung und den Verwalter bei Schnittstellen aus einem Wechsel in oder aus der Eigenverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Eigenverwaltung angeordnet oder beantragt ist
- Sachwalterberichte und Kontrollmaßnahmen erforderlich sind
- Haftung, Anfechtung oder Tabellenprüfung in Eigenverwaltung relevant wird

## Eingaben

- Eigenverwaltungsplanung, Finanzplan, Beschluss
- Berichte der Schuldnerin, Buchhaltung, Zahlungsläufe
- Gläubigerausschuss- und Gerichtskommunikation

## Workflow

1. **Rolle trennen** - Schuldnerin verwaltet, Sachwalter beaufsichtigt; Befugnisse sauber markieren.
2. **Plan kontrollieren** - Finanzplan, Kosten, Rechnungslegung, Organtreue und Pflichtverstöße prüfen.
3. **Masseinteressen** - Anfechtung, Haftung, Forderungsprüfung und Gläubigerinformation verfolgen.
4. **Bericht erstellen** - Kontrollbefund mit Eskalationsoptionen formulieren.

## Ausgabe

- Sachwalter-Kontrollbericht
- Eigenverwaltungs-Ampel
- Eskalations- und Aufhebungsnotiz

## Qualitätsgates

- Sachwalter handelt nicht wie Insolvenzverwalter
- § 270f und § 280 InsO geprüft
- Zahlungsläufe stichprobenvalidiert

## Rote Schwellen

- mangelhafte Buchführung
- Haftungsansprüche gegen Organe
- Plan beruht auf unzutreffenden Tatsachen

## Interne Vorlagen

- assets/templates/eigenverwaltung-sachwalterbericht.md
- assets/templates/schutzschirm-270d.md

## Amtliche Erstquellen

- §§ 270 ff. InsO
- § 280 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (3. Kammer, Erster Senat — VARTA) — Eingriffe in Aktionärsrechte durch StaRUG-Plan im Restrukturierungsverfahren verfassungsrechtlich nicht generell ausgeschlossen; Schlechterstellungsprüfung (§ 66 Abs. 2 Nr. 3 StaRUG) entscheidend.
 <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- Zur Verzahnung Eigenverwaltung / Anfechtung: **BGH IX ZR 122/23 vom 05.12.2024** (Bargeschäft / Unlauterkeit) und **BGH IX ZR 129/22 vom 18.04.2024** (Vorsatzanfechtung).
- Konkrete BGH-Linien zu §§ 270b, 270d InsO (vorläufige Eigenverwaltung, Schutzschirm) und zur Sachwalter-Haftung vor Ausgabe über dejure.org / openjur.de mit Datum und Aktenzeichen verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
