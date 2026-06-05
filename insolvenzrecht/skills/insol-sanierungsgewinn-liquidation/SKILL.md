---
name: insol-sanierungsgewinn-liquidation
description: "Insol Sanierungsgewinn Liquidation: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Insol Sanierungsgewinn Liquidation

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Insol Sanierungsgewinn Liquidation** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `insol-sanierungsgewinn-liquidation-statt-plan-folgen` | Wahlentscheidung Insolvenzplan versus Liquidation und die Steuerfolgen. Bei Liquidation: kein Sanierungsertrag, aber Aufdeckung stiller Reserven, Veraeusserungsgewinn aus Verwertung. Bei der GmbH-Liquidation: Verbindlichkeiten bleiben nach BFH II R 19/01 ueber blosse Vermoegenslosigkeit bestehen. OFD Frankfurt: Liquidationsbeschluss allein ist kein konkludenter Verzicht. Entscheidungsmatrix mit Steuersicht und Mustertexte. |
| `insol-sanierungsgewinn-mandantenwarnung-iv-und-cro` | Mandantenbrief an Insolvenzverwalter, Sachwalter, CRO und Schuldner zur rechtzeitigen Einbeziehung steuerlicher Beratung beim Sanierungsgewinn. Standardisierter Brief: was steuerlich VOR der Plan-Vorlage zu klaeren ist, welche Haftung droht bei Versaeumnis (Paragraph 60 InsO, ggf. Paragraph 130 OWiG, Paragraph 69 AO), wie der Berater eingebunden wird. Erste Antwort knapp, dann sofort Briefentwurf. |
| `insol-sanierungsgewinn-massenpriorisierung-261-vs-3a-estg` | Massevorrang Paragraph 53 InsO und seine Spannung zum Sanierungsantrag nach Paragraph 3a EStG. Wenn aus dem Restsanierungsertrag eine Steuer entsteht und die Steuer eine Masseverbindlichkeit Paragraph 55 InsO ist, geht sie der Quote vor. Risiko: bestaetigter Plan scheitert, weil die Steuer die Masse aufzehrt. zur Modellierung und Mustertexte fuer Glaeubigerausschuss-Brief. |
| `insol-sanierungsgewinn-restschuldbefreiung-und-3a-estg` | Restschuldbefreiung Paragraphen 286 ff. InsO bei natuerlichen Personen und ihre Schnittstelle zum Sanierungsertrag Paragraph 3a EStG. Bei natuerlichen Personen Unterscheidung unternehmensbezogene vs. unternehmerbezogene Sanierung. Paragraph 3a EStG erfasst nur unternehmensbezogene Sanierung. Restschuldbefreiung erlischt Verbindlichkeiten zivilrechtlich; steuerlich kann gleichwohl ein Ertrag entstehen. Mustertexte und Pruefraster. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Insol Sanierungsgewinn Liquidation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `insol-sanierungsgewinn-liquidation-statt-plan-folgen`

**Fokus:** Wahlentscheidung Insolvenzplan versus Liquidation und die Steuerfolgen. Bei Liquidation: kein Sanierungsertrag, aber Aufdeckung stiller Reserven, Veraeusserungsgewinn aus Verwertung. Bei der GmbH-Liquidation: Verbindlichkeiten bleiben nach BFH II R 19/01 ueber blosse Vermoegenslosigkeit bestehen. OFD Frankfurt: Liquidationsbeschluss allein ist kein konkludenter Verzicht. Entscheidungsmatrix mit Steuersicht und Mustertexte.

# Sanierungsgewinn — Liquidation statt Plan, Steuer-Folgen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Liquidation statt Plan, Steuer-Folgen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der Mandant hat im Krisenfall meist die Wahl zwischen Plan-Sanierung und Liquidation. Steuerlich sind das zwei sehr unterschiedliche Welten:

- **Plan-Sanierung:** Forderungsverzicht moeglich, Sanierungsertrag, Paragraph 3a EStG-Antrag, Unternehmensfortfuehrung.
- **Liquidation:** Verwertung der Aktiva, Auskehrung an Glaeubiger nach Quote, Restverbindlichkeiten bleiben (bei juristischer Person) zivilrechtlich bestehen, ueber Loeschung im Handelsregister hinaus (BFH, Urteil vom 26.02.2003 — II R 19/01).

Die Liquidation produziert **keinen Sanierungsertrag**, weil keine Verbindlichkeit erlassen wird. Wenn die GmbH spaeter Vermoegen erhaelt oder ein Glaeubiger sich noch meldet, leben Verbindlichkeiten wieder auf. Eine Verlautbarung der OFD Frankfurt a. M. stellt zudem klar: der Liquidationsbeschluss allein ist nicht als konkludenter Forderungsverzicht zu deuten. Adressat: Beratungs-Anwalt der Geschaeftsleitung, IV, StB.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Mandant ueberlegt, statt Sanierung den Geschaeftsbetrieb einzustellen.
- Insolvenzverwalter fragt, ob Plan oder Liquidation steuerlich besser ist.
- StB plant die Steuererklaerung des letzten Geschaeftsjahres.

Kaltstart-Fragen:

1. Rechtsform Schuldnerin (GmbH, AG, GmbH und Co. KG, Einzelunternehmer)?
2. Stille Reserven auf Aktiva?
3. Verlustvortraege?
4. Plan-Quote-Schaetzung vs. Liquidations-Quote-Schaetzung?
5. Soll die Schuldnerin (juristische Person) erloeschen oder fortbestehen?

## Rechtlicher Rahmen

- Paragraphen 199 ff. InsO — Verteilung und Schlussverteilung.
- Paragraph 207 InsO — Einstellung mangels Masse.
- Paragraph 60 GmbHG, Paragraph 262 AktG — Aufloesung der Gesellschaft.
- Paragraph 11 KStG — Liquidationsbesteuerung.
- Paragraph 16 EStG — Veraeusserungs-/Aufgabegewinn.
- Paragraph 3a EStG — Sanierungsertrag (Negativ-Abgrenzung).
- BFH, Urteil vom 26.02.2003 — II R 19/01.
- OFD Frankfurt a. M.: Liquidationsbeschluss allein ist kein konkludenter Forderungsverzicht (Verlautbarung der OFD — Az/Datum vom Anwender mit aktueller OFD-Veroeffentlichung zu pruefen).

## / Schritt fuer Schritt

1. **Entscheidungsmatrix Plan vs. Liquidation** aus betriebs- und steuerwirtschaftlicher Sicht aufstellen.
2. **Stille Reserven bewerten** — bei Liquidation werden sie aufgedeckt; bei Plan-Buchwertfortfuehrung nicht.
3. **Verlustvortraege:** Bei Liquidation Paragraph 11 KStG-Phase (3 Jahre); bei Plan Paragraph 3a Absatz 3 EStG.
4. **Restverbindlichkeiten:** Bei juristischer Person bleibt die Schuld zivilrechtlich bestehen (BFH II R 19/01); erst spaetere Vermoegenslosigkeit oder ein expliziter Verzicht erlischt sie.
5. **OFD Frankfurt-Linie beachten:** Der Liquidationsbeschluss allein ist nicht als Verzicht zu lesen. Wer einen Sanierungsertrag aus der Liquidation herleiten will, muss eine ausdrueckliche Verzichtserklaerung der Glaeubiger nachweisen.
6. **Steuererklaerung Liquidation:** Paragraph 11 KStG Liquidationszeitraum.

## Plan vs. Liquidation — Entscheidungsmatrix

| Punkt | Plan-Sanierung | Liquidation |
|---|---|---|
| Forderungsverzicht | typisch | nein |
| Sanierungsertrag | ja, Paragraph 3a EStG | nein |
| Stille Reserven | Buchwertfortfuehrung moeglich | Aufdeckung |
| Verlustvortrag | nach Paragraph 3a Absatz 3 EStG ggf. verbraucht | abbaubar im Liquidationszeitraum Paragraph 11 KStG |
| Unternehmen fortgefuehrt | ja | nein |
| Restverbindlichkeiten | nach Plan-Bestaetigung erlischt nicht-Plan-Verzichts-Teil ggf. weiter passiviert | bei juristischer Person bleiben bestehen (BFH II R 19/01) |
| Erloeschen der juristischen Person | nein | mit Loeschung im Handelsregister, aber Verbindlichkeiten bleiben |
| Bei spaeterer Vermoegenslosigkeit | irrelevant | Verbindlichkeiten erloeschen erst bei expliziter Verzichtserklaerung oder Eintritt der Verjaehrung |
| Steueraufwand | Paragraph 3a EStG-Pruefung | Veraeusserungsgewinne + Liquidations-Phase |
| Geschwindigkeit | mehrere Monate Plan-Verfahren | je nach Verwertung |
| Kosten | typisch hoeher | typisch niedriger |
| Sanierungsbeduerftigkeit-Dokumentation | erforderlich | nicht |

## Trade-off-Matrix Steuer

| Konstellation | Plan | Liquidation |
|---|---|---|
| Hohe Verlustvortraege, geringe stille Reserven | Paragraph 3a Absatz 3 EStG verbraucht Vortraege | Vortraege koennen Aufgabegewinn verrechnen |
| Geringe Verlustvortraege, hohe stille Reserven | Restsanierungsertrag muss durch Paragraph 3a Absatz 1 EStG getragen werden; stille Reserven bleiben | Aufdeckung der stillen Reserven ergibt Aufgabegewinn ohne Verrechnung |
| Hohe stille Reserven + hohe Verlustvortraege | Plan tendenziell vorteilhaft | Liquidation moeglich, aber Vortraege werden anders verrechnet |
| Sanierungspotenzial des Unternehmens hoch | Plan | nicht zielfuehrend |
| Sanierungspotenzial gering | Plan kann scheitern | Liquidation realistisch |

## Praxistipps der alten Hasen

1. **Steuermodellrechnung beide Wege.** Vergleichszahl in EUR liefern — die Mandanten wollen einen Vergleich, nicht Theorie.
2. **Restverbindlichkeiten der GmbH nach Liquidation:** BFH II R 19/01 lesen. Wer glaubt, mit der Loeschung im Handelsregister sei alles weg, wird beim Glaeubiger-Wiederantrag ueberrascht.
3. **OFD Frankfurt-Verlautbarung.** Liquidationsbeschluss ist kein Verzicht — wer den Sanierungsertrag aus reiner Liquidation herleitet, hat schlechte Karten.
4. **Bei Personengesellschaft:** Gesellschafter haften persoenlich (Paragraph 128 HGB); Liquidation der GbR/oHG ist nicht das Ende der Schulden.
5. **Vor Liquidationsbeschluss Steuermodellrechnung.** Manchmal ist die Plan-Sanierung wirtschaftlich besser, auch wenn die GF lieber einen "sauberen Schnitt" macht.
6. **Liquidationszeitraum Paragraph 11 KStG:** drei Jahre als Bemessungsgrundlage, dann Schlussbescheid.

## Mustertexte / Berechnungsbeispiele

**Vergleichsrechnung Plan vs. Liquidation (Geruest):**

```
VERGLEICHSRECHNUNG PLAN VS. LIQUIDATION
Mandant: [Schuldnerin]
Stichtag: [Datum]

I. PLAN-SZENARIO
Forderungsverzicht EUR 5.000.000
Sanierungsertrag EUR 5.000.000
abzgl. Verrechnung Paragraph 3a III EUR 1.500.000
= Restbetrag EUR 3.500.000
=> Paragraph 3a Absatz 1 EStG anwendbar (vier Voraussetzungen)
Steuer Erwartungswert EUR 300.000 (Restrisiko)
Verbleibendes EK nach Plan EUR 1.200.000
Unternehmen fortgefuehrt

II. LIQUIDATIONS-SZENARIO
Verwertungserloese Aktiva EUR 4.000.000
Buchwert Aktiva EUR 3.000.000
= Aufgabegewinn EUR 1.000.000
abzgl. Verlustvortrag (Paragraph 10d) EUR 1.000.000
= zu versteuern EUR 0
Verteilung an Insolvenzglaeubiger (Quote ca. 18%)
Verbindlichkeiten bleiben zivilrechtlich (BFH II R 19/01) bestehen
Schuldnerin erlischt mit Loeschung im Handelsregister

III. ENTSCHEIDUNG
Plan steuerlich teurer im Restrisiko, aber Unternehmen lebt weiter.
Liquidation steuerlich glatt, aber Unternehmen weg + Verbindlichkeiten
bleiben formell bestehen.
Empfehlung: [...]
```

**Brief an Glaeubigerausschuss (Auszug):**

```
Mit dem im Plan vorgesehenen Forderungsverzicht entsteht ein
Sanierungsertrag im Sinne von Paragraph 3a EStG; bei erfuellten vier
Voraussetzungen bleibt dieser steuerfrei. Bei alternativer Liquidation
entstuende kein Sanierungsertrag; stattdessen wuerden stille Reserven
aufgedeckt und ein Veraeusserungs-/Aufgabegewinn entstehen.

Wichtig: Auch bei Liquidation bleiben die Restverbindlichkeiten der
Schuldnerin (juristische Person) zivilrechtlich grundsaetzlich bestehen
(BFH II R 19/01); die Loeschung im Handelsregister beendet die
Verbindlichkeit nicht automatisch.

Eine Verlautbarung der OFD Frankfurt a. M. stellt zudem klar, dass der
Liquidationsbeschluss allein nicht als konkludenter Forderungsverzicht
zu deuten ist. Wer einen steuerfreien Sanierungsertrag aus reiner
Liquidation herleiten will, hat schlechte Karten.
```

## Typische Fehler

1. Annahme, Liquidation produziere automatisch einen Sanierungsertrag — falsch.
2. Liquidationsbeschluss als Verzicht interpretieren — OFD Frankfurt verneint das.
3. Vergessen, dass Restverbindlichkeiten der GmbH nach Loeschung im Handelsregister zivilrechtlich bestehen bleiben (BFH II R 19/01).
4. Vergleichsrechnung Plan vs. Liquidation nicht angestellt.
5. Bei Personengesellschaft die Gesellschafter-Haftung Paragraph 128 HGB vergessen.
6. Paragraph 11 KStG-Liquidationszeitraum nicht beachtet.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-uebertragende-sanierung-asset-deal` — Asset Deal als Hybrid.
- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Plan-Schiene.
- `insol-sanierungsgewinn-finanzamt-im-insolvenzverfahren` — FA-Position.
- `insol-sanierungsgewinn-restschuldbefreiung-und-3a-estg` — natuerliche Person.

In anderen Plugins:

- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.
- `steuerrecht-anwalt-und-berater` — Liquidationsbesteuerung.
- `grosskanzlei-corporate-ma` — Distressed-M-und-A.

## Quellen Stand 06/2026

- Paragraphen 199, 207 InsO.
- Paragraph 60 GmbHG, `gesetze-im-internet.de/gmbhg/__60.html`.
- Paragraph 262 AktG.
- Paragraph 11 KStG, `gesetze-im-internet.de/kstg_1977/__11.html`.
- Paragraph 16 EStG.
- Paragraph 3a EStG.
- BFH, Urteil vom 26.02.2003 — II R 19/01.
- OFD Frankfurt a. M.: Liquidationsbeschluss allein ist kein konkludenter Verzicht (Verlautbarung der OFD — Aktenzeichen/Datum vom Anwender mit aktueller OFD-Veroeffentlichung zu pruefen).
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 2. `insol-sanierungsgewinn-mandantenwarnung-iv-und-cro`

**Fokus:** Mandantenbrief an Insolvenzverwalter, Sachwalter, CRO und Schuldner zur rechtzeitigen Einbeziehung steuerlicher Beratung beim Sanierungsgewinn. Standardisierter Brief: was steuerlich VOR der Plan-Vorlage zu klaeren ist, welche Haftung droht bei Versaeumnis (Paragraph 60 InsO, ggf. Paragraph 130 OWiG, Paragraph 69 AO), wie der Berater eingebunden wird. Erste Antwort knapp, dann sofort Briefentwurf.

# Sanierungsgewinn — Mandantenwarnung an Insolvenzverwalter / CRO / Schuldner

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Mandantenwarnung an Insolvenzverwalter / CRO / Schuldner` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Wer in der Insolvenz oder im StaRUG-Verfahren arbeitet, lebt mit knappen Fristen. Der Sanierungsgewinn nach Paragraph 3a EStG faellt typischerweise erst spaet auf den Schirm — oft erst dann, wenn der Plan praktisch fertig ist und nicht mehr ohne weiteres aufgemacht werden kann. Dieser Skill liefert einen **Mustermandantenbrief**, mit dem der Berater (RA, StB, Plan-Anwalt) gegenueber dem Insolvenzverwalter, dem Sachwalter, dem CRO oder dem Schuldnerunternehmen frueh und schriftlich auf die steuerliche Vorarbeit hinweist — und damit zugleich die eigene Beratungsdokumentation absichert.

Adressat: Berater, der gegenueber IV/CRO/Schuldner kommunizieren muss. Tonfall: nuechtern, kanzleitauglich, ohne Drohgebaerden, aber mit klarer Haftungs-Signalsetzung.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sie sind als Berater neu im Mandat oder werden nur fuer den Steuerteil hinzugezogen.
- Sie befuerchten, dass der Plan-Anwalt oder der IV den Sanierungsgewinn nicht ausreichend behandelt.
- Sie wollen die Mandantenkommunikation zum Sanierungsgewinn formell ausloesen.

Kaltstart-Fragen:

1. An wen geht der Brief (IV namentlich, CRO, Geschaeftsfuehrung, Sachwalter)?
2. Mandatsstand (Forderungsverzicht im Plan in welcher Groessenordnung)?
3. Wie ist der Berater im Mandat verankert (eigenes Mandat, Subbeauftragung, Massehaftung Kostenuebernahme)?
4. Wie steht die Zeitachse (Plan in Vorbereitung, Plan eingereicht, Plan bestaetigt)?

Wenn die Fragen 1 und 4 beantwortet sind, beginnt der Brief.

## Rechtlicher Rahmen

- Paragraph 60 InsO — Schadensersatzpflicht des Insolvenzverwalters bei schuldhafter Pflichtverletzung. Der Verwalter haftet auch gegenueber der Masse fuer steuerliche Versaeumnisse.
- Paragraph 69 AO — Haftung der gesetzlichen Vertreter fuer Steuerschulden.
- Paragraph 130 OWiG — Aufsichtspflichtverletzung; relevant fuer Geschaeftsfuehrer und CRO.
- Paragraph 89 AO — verbindliche Auskunft (Kostenfrage).
- Paragraph 43a Absatz 2 BRAO, Paragraph 203 StGB — Mandantengeheimnis bei Kommunikation; AVV bei Tools.
- Paragraph 3a EStG, Paragraph 7b GewStG — die materiellen Sanierungsgewinn-Normen.

## / Schritt fuer Schritt

1. **Adressat klaeren.** IV/CRO/Schuldner — drei verschiedene Briefe in unterschiedlichen Tonfaellen.
2. **Sachverhalts-Bezug einfuegen.** Welche konkrete Krisensituation? Welcher Plan-Stand?
3. **Drei Kern-Punkte heraus arbeiten:** Verlustvortrag-Pruefung, Vier-Voraussetzungen-Dokumentation, Antrag Paragraph 3a EStG und Paragraph 7b GewStG.
4. **Frist setzen.** Konkrete Frist fuer Rueckmeldung (typisch 14 Tage).
5. **Honorarklarheit.** RVG-Hinweis (bei RA) oder StBVV (bei StB), bei Massehaftung Hinweis auf Paragraph 55 Absatz 1 Nr. 1 InsO.
6. **Verteiler.** CC an alle steuerlich Beteiligten (StB Schuldner, ggf. eigener Mitarbeiter im Mandat).

## Trade-off-Matrix

| Variante | wann sinnvoll |
|---|---|
| Brief an IV | wenn der Berater extern angesprochen ist und Versaeumnis des IV vorbeugen will |
| Brief an Schuldner-Geschaeftsfuehrung | wenn Eigenverwaltung oder Schutzschirm laeuft und GF entscheidungsbefugt ist |
| Brief an CRO | wenn der CRO im StaRUG-Verfahren oder Eigenverwaltung verantwortlich ist |
| Aktennotiz statt Brief | wenn der Berater bereits im Beraterkreis ist und kein "Eskalations"-Schreiben noetig |
| Stellungnahme Glaeubigerausschuss | wenn der Berater zugleich Mitglied oder Berater des Ausschusses ist |

## Mustertexte / Berechnungsbeispiele

**Variante A — Brief an Insolvenzverwalter:**

```
[Briefkopf Berater]

Sehr geehrte Frau Rechtsanwaeltin/Herr Rechtsanwalt [Name],

in dem Verfahren [Aktenzeichen] ueber das Vermoegen der [Schuldner], in dem
Sie zum Insolvenzverwalter bestellt sind, weise ich Sie pflichtgemaess auf
die folgenden steuerlichen Punkte hin, die VOR der Vorlage des Plan-Entwurfs
beim Insolvenzgericht zu klaeren sind. Hintergrund ist die Steuerfreiheit des
Sanierungsertrags nach Paragraph 3a EStG, deren Voraussetzungen frueh
dokumentiert sein muessen.

1. VERLUSTVORTRAG-PRUEFUNG
Bitte lassen Sie durch den steuerlichen Berater des Schuldners eine
Modellrechnung nach Paragraph 3a Absatz 3 EStG aufsetzen. Solange diese nicht
vorliegt, ist nicht abschaetzbar, ob aus dem geplanten Forderungsverzicht
tatsaechlich ein steuerbarer Restbetrag verbleibt.

2. VIER VORAUSSETZUNGEN PARAGRAPH 3a ABSATZ 2 EStG
Sanierungsbeduerftigkeit, Sanierungsfaehigkeit, Sanierungseignung und
Sanierungsabsicht der Glaeubiger sollten getrennt belegbar sein. Sanierungs-
absicht laesst sich am besten durch protokollierte Aussagen aus der
Glaeubigerversammlung oder vergleichbare Akten dokumentieren.

3. PARALLEL GEWERBESTEUER PARAGRAPH 7b GewStG
Die gewerbesteuerliche Antragsmechanik ist eigenstaendig und wird in der
Praxis haeufig uebersehen.

4. HAFTUNGSHINWEIS
Ich weise darauf hin, dass Versaeumnisse in der steuerlichen Vorbereitung
eines Sanierungsplans den Verwalter dem Risiko der Haftung nach Paragraph 60
InsO aussetzen koennen, ohne dass damit eine konkrete Pflichtverletzung
behauptet sein soll.

5. NAECHSTE SCHRITTE
Bitte teilen Sie mir bis zum [Datum + 14 Tage] mit, ob ein steuerlicher
Berater mit der Vorab-Modellrechnung beauftragt ist und welcher Zeithorizont
fuer die vier Voraussetzungs-Belege vorgesehen ist.

Honorarhinweis: Meine Taetigkeit als [RA / StB] erfolgt auf Basis [RVG /
StBVV / Stundenvereinbarung]; ich biete an, das Mandat ueber Paragraph 55
Absatz 1 Nr. 1 InsO als Massehaftung abzurechnen, soweit Sie das fuer
sachgerecht halten.

Mit freundlichen kollegialen Gruessen
[Unterschrift mit Berufsbezeichnung]
```

**Variante B — Brief an Geschaeftsfuehrung / CRO in Eigenverwaltung:**

```
[Briefkopf]

In dem Restrukturierungsverfahren / der Eigenverwaltung ueber das Vermoegen
der [Schuldner]

Sehr geehrte Damen und Herren,

der von Ihnen vorbereitete Restrukturierungsplan / Insolvenzplan sieht einen
Forderungsverzicht in der Groessenordnung von EUR [Betrag] vor. Dieser
Forderungsverzicht loest einen Sanierungsertrag aus. Damit dieser
Sanierungsertrag steuerfrei bleibt, sind drei Punkte vor der Plan-Vorlage
zu klaeren:

1. Modellrechnung der Verrechnungsreihenfolge nach Paragraph 3a Absatz 3 EStG
2. Dokumentation der vier Voraussetzungen Paragraph 3a Absatz 2 EStG
3. Parallel-Antrag Paragraph 7b GewStG

Wir empfehlen, hierfuer den steuerlichen Berater des Unternehmens [Name]
sofort einzubinden. Bitte teilen Sie uns bis zum [Datum] mit, ob das
geschehen ist.

Wir weisen vorsorglich darauf hin, dass die Geschaeftsleitung in
Eigenverwaltung und der CRO bei Versaeumnissen einer entsprechenden
Haftungs- bzw. Sanktionssituation ausgesetzt sein koennen (Paragraph 60
InsO entsprechend, Paragraph 69 AO, Paragraph 130 OWiG).

Kostenhinweis nach RVG/StBVV: [...]

Mit freundlichen Gruessen
[Unterschrift]
```

## Praxistipps der alten Hasen

1. **Brief in die Akte legen.** Ein solcher Brief ist primaer Haftungsdokumentation. Er gehoert auch in die eigene Handakte.
2. **CC an StB des Schuldners.** Wer den Brief gleich an den StB mitschickt, schliesst die Kommunikationslucke.
3. **Frist setzen, aber nicht ueberreizen.** 14 Tage sind im normalen Verfahren angemessen; im Schutzschirmverfahren ggf. kuerzer.
4. **Keine Drohung, sondern Hinweispflicht.** Tonfall sachlich; die Haftungsformulierung soll mahnen, nicht eskalieren.
5. **Wenn der IV nicht reagiert,** Briefkette dokumentieren und ggf. an den vorlaeufigen Glaeubigerausschuss eskalieren.

## Typische Fehler

1. Brief nur muendlich abgesetzt — keine Beweisspur.
2. Adressat falsch (Brief an Schuldner, obwohl IV bereits bestellt ist).
3. Fristlose Eskalations-Sprache, die den IV verbrennt.
4. Honorarklarheit fehlt — Auftrag bleibt schwebend.
5. Vergessen, die GewSt-Schiene (Paragraph 7b GewStG) anzusprechen.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-fruehe-vorbereitung-vor-plan` — Zeitachse.
- `insol-sanierungsgewinn-verlustvortrag-und-3a-iii-vorab` — Modellrechnung.
- `insol-sanierungsgewinn-iv-haftung-fuer-versaumte-3a-iv-antraege` — Haftungs-Vertiefung.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — generelle Steuerberatungs-Mandantenkommunikation.
- `grosskanzlei-corporate-ma` — falls Investor-Seite mitbetreut wird.

## Quellen Stand 06/2026

- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraph 7b GewStG, `gesetze-im-internet.de/gewstg/__7b.html`.
- Paragraph 60 InsO, Paragraph 55 InsO, `gesetze-im-internet.de/inso/`.
- Paragraphen 69, 89 AO, `gesetze-im-internet.de/ao_1977/`.
- Paragraph 130 OWiG, `gesetze-im-internet.de/owig_1968/__130.html`.
- FG Koeln, Urteil vom 04.11.2025 — 12 K 1413/25 — Antragstellung. Verifikation ueber `dejure.org`.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 3. `insol-sanierungsgewinn-massenpriorisierung-261-vs-3a-estg`

**Fokus:** Massevorrang Paragraph 53 InsO und seine Spannung zum Sanierungsantrag nach Paragraph 3a EStG. Wenn aus dem Restsanierungsertrag eine Steuer entsteht und die Steuer eine Masseverbindlichkeit Paragraph 55 InsO ist, geht sie der Quote vor. Risiko: bestaetigter Plan scheitert, weil die Steuer die Masse aufzehrt. zur Modellierung und Mustertexte fuer Glaeubigerausschuss-Brief.

# Sanierungsgewinn — Massenpriorisierung Paragraphen 53/261 InsO vs. Paragraph 3a EStG

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Massenpriorisierung Paragraphen 53/261 InsO vs. Paragraph 3a EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Die Insolvenzmasse ist begrenzt. Wenn aus dem Restsanierungsertrag eine Steuer entsteht — etwa weil Paragraph 3a EStG-Voraussetzungen nicht zweifelsfrei erfuellt sind — dann ist diese Steuer regelmaessig eine **Masseverbindlichkeit** (Paragraph 55 InsO). Masseverbindlichkeiten gehen den Insolvenzforderungen vor (Paragraph 53 InsO). Damit kann es sein, dass die Plan-Quote zu Lasten der Quote-Glaeubiger geht — oder dass der Plan praktisch scheitert, weil die Masse die Steuer nicht traegt.

Dieser Skill modelliert den Konflikt. Adressat: IV/Sachwalter, Plan-Anwalt, Glaeubigerausschuss.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Modellrechnung Paragraph 3a Absatz 3 EStG zeigt einen Restsanierungsertrag mit moeglicher Steuer.
- Plan steht vor Vorlage; Plan-Quote zu Lasten der Glaeubiger soll abgesichert werden.
- Glaeubigerausschuss fragt: koennen wir uns auf die Sanierungsquote verlassen, wenn die Steuer im Hintergrund wartet?

Kaltstart-Fragen:

1. Restsanierungsertrag nach Verrechnung?
2. Gibt es Anhaltspunkte, dass Paragraph 3a EStG scheitert?
3. Wieviel "Polster" hat die Masse fuer eine etwaige Steuer (Liquiditaetspuffer)?
4. Liegt eine Vorabauskunft Paragraph 89 AO vor?
5. Wie sind die Plan-Quote und der Vorrang der Masse-Steuer modelliert?

## Rechtlicher Rahmen

- Paragraph 53 InsO — Vorrang der Masseverbindlichkeiten.
- Paragraph 55 InsO — Masseverbindlichkeiten.
- Paragraph 209 InsO — Befriedigungsreihenfolge bei Masseunzulaenglichkeit.
- Paragraph 261 InsO — Erfuellung des Insolvenzplans (Aufhebung Verfahren nach Bestaetigung).
- Paragraph 251 AO — Steuern in der Insolvenz.
- Paragraph 3a EStG.

## / Schritt fuer Schritt

1. **Sanierungs-Modellrechnung.** Hauptantrag Paragraph 3a EStG: wie hoch der Restbetrag?
2. **Sensitivitaetsanalyse: was wenn Paragraph 3a EStG scheitert?** Steuerbetrag berechnen (KSt, GewSt).
3. **Steuer als Masseverbindlichkeit verbuchen** (Paragraph 55 InsO).
4. **Plan-Quote pruefen.** Reicht die Masse nach Abzug der Steuer fuer die zugesagte Quote?
5. **Plan-Klausel zur Vermeidung der Massenpriorisierung pruefen.** Hilfsweise Stundung Paragraph 222 AO oder Erlass Paragraph 227 AO als Bedingung im Plan.
6. **Glaeubigerausschuss informieren** — der Ausschuss muss das Steuerrisiko kennen.
7. **Bei Masseunzulaenglichkeit (Paragraph 208 InsO) Anzeige beim Gericht.**

## Trade-off-Matrix

| Konstellation | Wirkung auf Quote | Strategie |
|---|---|---|
| Paragraph 3a EStG greift voll | keine Steuer; Quote wie geplant | Standard |
| Paragraph 3a EStG greift zum Teil | Steuer auf Restbetrag; Quote ggf. niedriger | Stundung/Erlass-Hilfslinie aktivieren |
| Paragraph 3a EStG greift nicht | volle Steuer; Quote gefaehrdet | Plan ggf. nicht traegfaehig |
| Stundung Paragraph 222 AO erfolgreich | Steuer in Raten nach Plan; Quote tragbar | Tilgungsplan dem FA vorlegen |
| Erlass Paragraph 227 AO erfolgreich | keine Steuer; Quote wie geplant | sachliche/persoenliche Unbilligkeit begruenden |
| Plan-Klausel macht Anwendung Paragraph 3a EStG zur Bedingung des Plan-Vollzugs | Plan haengt von FA-Entscheidung ab | nur bei Vorabauskunft empfehlenswert |
| Masseunzulaenglichkeit Paragraph 208 InsO | Quote sinkt zwingend | Plan praktisch gescheitert |

## Praxistipps der alten Hasen

1. **Worst-Case rechnen.** Auch wenn Paragraph 3a EStG sehr wahrscheinlich greift: was passiert bei Ablehnung? Quote ueberlebt?
2. **Plan-Quote mit Reservepolster.** Die Plan-Quote nicht so eng kalibrieren, dass eine Reststeuer den Plan kippt.
3. **Vorabauskunft Paragraph 89 AO** ist hier besonders wertvoll, weil sie das Restrisiko quantifiziert.
4. **Stundungsantrag als Plan-Anlage.** Wer den Stundungsantrag schon mit dem Plan einreicht, signalisiert vorausschauende Planung.
5. **Glaeubigerausschuss-Beschluss** zur Risikoeinschaetzung explizit einholen.
6. **Bei Eigenverwaltung** gilt die Massenpriorisierung sinngemaess: GF/CRO tragen die Verantwortung.

## Mustertexte / Berechnungsbeispiele

**Beispiel:** GmbH-Insolvenz; Masse 6 Mio EUR; Plan-Quote 25% auf 20 Mio Insolvenzforderungen = 5 Mio EUR Auskehrung. Restsanierungsertrag 3 Mio EUR.

```
SZENARIO A (Paragraph 3a EStG greift voll):
Masse EUR 6.000.000
abzgl. Verfahrenskosten EUR 500.000
abzgl. weitere Massehaft. EUR 500.000
= verteilbar EUR 5.000.000
Plan-Quote 25% einhaltbar.

SZENARIO B (Paragraph 3a EStG scheitert; KSt + GewSt rd. 30% auf 3.000.000):
Steuer auf Sanierungsertrag EUR 900.000
Masse EUR 6.000.000
abzgl. Verfahrenskosten EUR 500.000
abzgl. weitere Massehaft. EUR 500.000
abzgl. Steuer-Masseverbind. EUR 900.000
= verteilbar EUR 4.100.000
Plan-Quote bei 25% verlangt 5.000.000 -> nicht einhaltbar.
=> Plan-Anpassung erforderlich oder Hilfslinie Paragraph 222/227 AO.

SZENARIO C (Stundung Paragraph 222 AO erfolgreich, Tilgung in 36 Monaten):
Steuer wird ueber 36 Monate aus laufender Geschaeftstaetigkeit getragen.
Masse bleibt fuer Plan-Quote frei.
=> Plan-Quote einhaltbar, aber Tilgungsplan ist Pflicht.
```

**Brief an Glaeubigerausschuss (Geruest):**

```
[Briefkopf IV]

An die Mitglieder des Glaeubigerausschusses
Verfahren [AZ]

Sanierungsertrag-Risiko und Plan-Quote

Sehr geehrte Damen und Herren,

zur Vorbereitung der Sitzung am [Datum] erlaube ich mir folgenden Hinweis:

Aus dem geplanten Forderungsverzicht in Hoehe von EUR [Betrag] resultiert
nach Verrechnung gemaess Paragraph 3a Absatz 3 EStG ein Restsanierungsertrag
in Hoehe von EUR [Betrag]. Hierauf greift Paragraph 3a Absatz 1 EStG bei
erfuellten vier Voraussetzungen.

Sensitivitaetsanalyse:
- Szenario A (Paragraph 3a EStG greift voll): Plan-Quote [%] einhaltbar.
- Szenario B (Paragraph 3a EStG scheitert): Mehr-Steuer ca. EUR [Betrag]
 als Masseverbindlichkeit Paragraph 55 InsO; Plan-Quote nicht einhaltbar.

Risikominderungsstrategie:
1. Vorabauskunft Paragraph 89 AO wird beantragt (Zeitschiene: [Monate]).
2. Plan enthaelt Hilfslinie Stundung Paragraph 222 AO; Tilgungsplan in
 Anlage [...].
3. Plan-Quote enthaelt Polster von EUR [Betrag] fuer Restrisiken.

Ich bitte um Beratung und ggf. Beschluss zum Vorgehen.

Mit freundlichen Gruessen
[IV]
```

## Typische Fehler

1. Plan-Quote ohne Reservepolster — Steuer-Restrisiko kippt den Plan.
2. Vorabauskunft Paragraph 89 AO ignoriert.
3. Glaeubigerausschuss nicht informiert.
4. Stundungsantrag erst nach Bescheid, nicht parallel zum Plan.
5. Bei Eigenverwaltung Verantwortung verschoben — sie bleibt bei GF/CRO.
6. Masseunzulaenglichkeitsanzeige Paragraph 208 InsO vergessen.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Hauptlinie.
- `insol-sanierungsgewinn-vergleich-mit-finanzamt-und-stundung` — Stundung/Erlass.
- `insol-sanierungsgewinn-finanzamt-im-insolvenzverfahren` — FA-Position.
- `insol-sanierungsgewinn-iv-haftung-fuer-versaumte-3a-iv-antraege` — Haftung.
- `inso-massearmut-massekostenmangel-spezial` — Massearmut.

In anderen Plugins:

- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.
- `steuerrecht-anwalt-und-berater` — generelle Steuerthemen.

## Quellen Stand 06/2026

- Paragraphen 53, 55, 208, 209, 261 InsO, `gesetze-im-internet.de/inso/`.
- Paragraph 251 AO.
- Paragraphen 222, 227 AO.
- Paragraph 3a EStG.
- Paragraph 7b GewStG.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 4. `insol-sanierungsgewinn-restschuldbefreiung-und-3a-estg`

**Fokus:** Restschuldbefreiung Paragraphen 286 ff. InsO bei natuerlichen Personen und ihre Schnittstelle zum Sanierungsertrag Paragraph 3a EStG. Bei natuerlichen Personen Unterscheidung unternehmensbezogene vs. unternehmerbezogene Sanierung. Paragraph 3a EStG erfasst nur unternehmensbezogene Sanierung. Restschuldbefreiung erlischt Verbindlichkeiten zivilrechtlich; steuerlich kann gleichwohl ein Ertrag entstehen. Mustertexte und Pruefraster.

# Sanierungsgewinn — Restschuldbefreiung und Paragraph 3a EStG bei natuerlichen Personen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Restschuldbefreiung und Paragraph 3a EStG bei natuerlichen Personen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Bei natuerlichen Personen (Einzelunternehmer, Freiberufler, Gesellschafter einer Personengesellschaft) ist die Sanierungsgewinn-Mechanik komplexer als bei Koerperschaften, weil:

- Paragraph 3a EStG nur die **unternehmensbezogene** Sanierung erfasst — nicht die rein **unternehmerbezogene** Sanierung der natuerlichen Person als solche.
- Die Restschuldbefreiung Paragraph 286 ff. InsO erlischt die Verbindlichkeit zivilrechtlich; sie ist aber **kein Sanierungsertrag** im Sinne von Paragraph 3a EStG, sondern eine eigene Konstellation.
- Steuerlich kann gleichwohl ein Ertrag entstehen, der versteuert werden muss.

Dieser Skill ordnet die Konstellationen und liefert Pruefraster. Adressat: IV, Sachwalter, StB, Schuldnervertretung.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Mandant ist natuerliche Person (Einzelunternehmer, Freiberufler).
- Restschuldbefreiung wurde angekuendigt oder ist anhaengig.
- Plan-Sanierung wird fuer den Einzelunternehmer geprueft.

Kaltstart-Fragen:

1. Rechtsstellung: Einzelunternehmer, Freiberufler, Gesellschafter Personengesellschaft, Verbraucher?
2. Welche Verbindlichkeiten (geschaeftlich, privat, gemischt)?
3. Verfahrensphase (eroeffnet, Wohlverhaltensphase, vor Erteilung Restschuldbefreiung)?
4. Liegt ein Sanierungsplan vor oder reine Restschuldbefreiung?
5. Erwerbsteuerlich relevante Einkuenfte (Gewinnermittlung Paragraphen 4, 5 EStG)?

## Rechtlicher Rahmen

- Paragraphen 286 ff. InsO — Restschuldbefreiung.
- Paragraph 287 InsO — Antrag.
- Paragraph 290 InsO — Versagungsgruende.
- Paragraph 301 InsO — Wirkung der Restschuldbefreiung.
- Paragraph 3a EStG — Sanierungsertrag.
- Paragraph 4 Absatz 1, Paragraph 5 EStG — Gewinnermittlung.
- BFH, Urteil vom 26.02.2003 — II R 19/01.
- Paragraph 251 AO.

## / Schritt fuer Schritt

1. **Verbindlichkeiten klassifizieren:** geschaeftlich vs. privat. Nur geschaeftlich loest Sanierungsertrag aus.
2. **Sanierungs-Modus:**
 - Plan-Sanierung (mit Forderungsverzicht): Sanierungsertrag moeglich.
 - reine Restschuldbefreiung: zivilrechtliches Erloeschen der Verbindlichkeit; steuerlich aber bilanziell Ertrag, falls die Verbindlichkeit zuvor passiviert war.
3. **Vier Voraussetzungen Paragraph 3a Absatz 2 EStG** pruefen, wenn unternehmensbezogen.
4. **Unternehmerbezogene Sanierung** abgrenzen — sie ist nicht von Paragraph 3a EStG erfasst; hier Hilfslinie Paragraph 227 AO.
5. **Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG**: Verlustvortraege der natuerlichen Person.
6. **Antrag mit der Einkommensteuererklaerung** des Sanierungsjahres.

## Unternehmensbezogen vs. unternehmerbezogen

| Kriterium | unternehmensbezogen | unternehmerbezogen |
|---|---|---|
| Sanierungszweck | Erhalt des Unternehmens | Entlastung der Person |
| Paragraph 3a EStG anwendbar | ja | nein |
| Typischer Fall | Einzelunternehmer setzt Betrieb fort | Einzelunternehmer beendet Betrieb, will privat schuldenfrei |
| Hilfslinie | Paragraph 3a Absatz 1 EStG | Paragraph 227 AO (Billigkeitserlass) |
| Restschuldbefreiung allein | keine Sanierungsertrag-Folge | siehe naechster Abschnitt |

## Restschuldbefreiung und steuerlicher Ertrag

Die Restschuldbefreiung erlischt die Verbindlichkeit (Paragraph 301 Absatz 1 InsO). Wenn die Verbindlichkeit in der Bilanz oder Einnahmen-Ueberschuss-Rechnung passiviert oder als Aufwand erfasst war, entsteht durch das Erloeschen ein Ertrag — dieser ist **nicht** automatisch ein Sanierungsertrag im Sinne von Paragraph 3a EStG.

| Konstellation | steuerliche Folge |
|---|---|
| Verbindlichkeit war geschaeftlich, Sanierung unternehmensbezogen | Sanierungsertrag, Paragraph 3a EStG-Pruefung |
| Verbindlichkeit war geschaeftlich, Sanierung unternehmerbezogen | Ertrag, kein Paragraph 3a EStG; Hilfslinie Paragraph 227 AO |
| Verbindlichkeit war privat | kein steuerlicher Ertrag, weil keine Betriebsausgabe |
| Verbindlichkeit war gemischt | Aufteilung |

## Trade-off-Matrix

| Variante | Wirkung |
|---|---|
| Plan-Sanierung (Forderungsverzicht im Plan) bei Unternehmensfortfuehrung | Paragraph 3a EStG anwendbar |
| Restschuldbefreiung bei Betriebsaufgabe | Paragraph 3a EStG meist nicht; Paragraph 227 AO als Auffanglinie |
| Restschuldbefreiung bei Verbraucherinsolvenz | meist kein steuerlicher Ertrag (Privatschulden) |
| Mischfall Einzelunternehmer + Privatschulden | getrennt rechnen |
| Wechsel von Plan zu Restschuldbefreiung | steuerlich Wechsel der Regime |

## Praxistipps der alten Hasen

1. **Verbindlichkeiten klassifizieren.** Eine Excel-Tabelle mit "geschaeftlich/privat/gemischt" pro Forderung ist die Basis.
2. **Bei Einzelunternehmer immer pruefen, ob Plan oder Restschuldbefreiung das richtige Werkzeug ist.** Plan ist steuerlich tendenziell besser, weil Paragraph 3a EStG greifen kann.
3. **Erlassantrag Paragraph 227 AO** fuer den unternehmerbezogenen Anteil vorbereiten.
4. **Verbraucherinsolvenz-Mandat:** Steueranfall pruefen, aber selten relevant.
5. **Wohlverhaltensphase laeuft drei Jahre.** Plan im Vorfeld kann die Wohlverhaltensphase umgehen.
6. **Versagungsgruende Paragraph 290 InsO** im Auge behalten — die Restschuldbefreiung ist nicht selbstverstaendlich.

## Mustertexte / Berechnungsbeispiele

**Beispiel:** Einzelunternehmer, Betriebsschulden 800.000, Privatschulden 50.000. Plan-Forderungsverzicht 600.000 auf Betriebsschulden, Plan-Quote 25 % auf Restbetrag. Privat: Restschuldbefreiung.

```
EBENE BETRIEBSSCHULDEN (Plan-Sanierung unternehmensbezogen)
Forderungsverzicht EUR 600.000
abzgl. Verlustvortrag (Annahme) EUR 200.000
abzgl. Sanierungskosten EUR 20.000
= Restsanierungsertrag EUR 380.000
=> Paragraph 3a EStG anwendbar, falls vier Voraussetzungen.

EBENE PRIVATSCHULDEN (Restschuldbefreiung)
50.000 EUR Privatschulden erloeschen mit Restschuldbefreiung.
Kein steuerlicher Ertrag.

GESAMT
Steuerlich relevant: Restsanierungsertrag 380.000 EUR (Paragraph 3a EStG).
```

**Brief an Mandant Einzelunternehmer:**

```
Sehr geehrter Herr / Frau [Name],

in Ihrem Verfahren ueber das Vermoegen Ihres Einzelunternehmens [Name]
sind aus steuerlicher Sicht zwei Schichten zu trennen:

1. Geschaeftsschulden, die im Plan teilweise erlassen werden:
Forderungsverzicht in Hoehe EUR [Betrag] loest einen Sanierungsertrag
aus. Wir werden hierfuer den Antrag nach Paragraph 3a EStG stellen.

2. Privatschulden, die mit Erteilung der Restschuldbefreiung erloeschen:
Keine steuerlichen Folgen.

Sofern Paragraph 3a EStG nicht in vollem Umfang greift, werden wir
hilfsweise Erlassantrag nach Paragraph 227 AO und Stundungsantrag nach
Paragraph 222 AO stellen.

Mit freundlichen Gruessen
[Berater]
```

## Typische Fehler

1. Annahme, Restschuldbefreiung sei "Sanierungsertrag" — sie ist eine eigene zivilrechtliche Wirkung mit eigenen steuerlichen Folgen.
2. Privat- und Betriebsschulden nicht getrennt.
3. Unternehmerbezogene Sanierung als unternehmensbezogen verkauft.
4. Verlustvortrag der natuerlichen Person uebersehen (Paragraph 10d EStG).
5. Versagungsgruende Paragraph 290 InsO uebersehen.
6. Bei Personengesellschaft: Gesellschafter-Ebene und Gesellschafts-Ebene durcheinander.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Hauptlinie Plan.
- `insol-sanierungsgewinn-vergleich-mit-finanzamt-und-stundung` — Hilfslinien.
- `inso-restschuldbefreiung-und-versagungsgruende` — Restschuldbefreiungs-Mechanik.
- `inso-verbraucherinsolvenz-leitfaden` — Verbraucherinsolvenz.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — generelle Steuer.
- `fachanwalt-insolvenz-sanierungsrecht` — fachanwaltliche Vertiefung.

## Quellen Stand 06/2026

- Paragraphen 286, 287, 290, 301 InsO.
- Paragraph 3a EStG.
- Paragraph 4 EStG.
- Paragraph 5 EStG.
- Paragraph 10d EStG.
- Paragraph 227 AO.
- BFH, Urteil vom 26.02.2003 — II R 19/01.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.
