---
name: insol-sanierungsgewinn-uebertragende
description: "Insol Sanierungsgewinn Uebertragende: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Insol Sanierungsgewinn Uebertragende

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Insol Sanierungsgewinn Uebertragende** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `insol-sanierungsgewinn-uebertragende-sanierung-asset-deal` | Uebertragende Sanierung als Asset Deal (Paragraphen 159 ff. InsO) und der Sanierungsgewinn. Beim Asset Deal entsteht kein klassischer Sanierungsertrag beim Schuldner, weil keine Forderungen erlassen werden. Stattdessen Veraeusserungsgewinn bei der Schuldnerin (stille Reserven). Steuerliche Schnittstelle: Paragraph 3a EStG meist nicht direkt anwendbar; Paragraph 75 AO Uebernehmerhaftung. Abgrenzung zur Plan-Sanierung mit Forderungsverzicht. |
| `insol-sanierungsgewinn-vergleich-mit-finanzamt-und-stundung` | Stundung Paragraph 222 AO und Erlass Paragraph 227 AO als Auffanglinien fuer den verbleibenden steuerbaren Restsanierungsertrag. Wenn Paragraph 3a EStG-Voraussetzungen nicht eindeutig erfuellt sind oder ein Restbetrag steuerpflichtig bleibt: persoenliche und sachliche Unbilligkeit begruenden, Vermoegensauflistung, Tatsaechliche Verstaendigung Paragraph 78 AO. Mustertexte Stundungs- und Erlassantrag. |
| `insol-sanierungsgewinn-verlustvortrag-und-3a-iii-vorab` | Vorab-Pruefung der Verrechnungsreihenfolge nach Paragraph 3a Absatz 3 EStG vor Insolvenzantrag oder StaRUG-Anzeige. Schritt-fuer-Schritt-Modellrechnung: laufende Verluste des Sanierungsjahres, vortragsfaehige Verluste, weitere Minderungspositionen. Wenn die Verrechnungsmasse den Sanierungsertrag aufzehrt, ist die Steuerfreiheit faktisch sichergestellt — Erlassantrag bleibt formell sinnvoll, materiell aber entbehrlich. Mit Berechnungsschemata und Excel-tauglicher Tabelle. |
| `insol-sanierungsgewinn-verzicht-bilanz-im-plan` | Bilanzielle Erfassung des Forderungsverzichts im Insolvenzplan und StaRUG-Plan. Handelsrechtliche und steuerliche Behandlung. Werthaltigkeit der verzichteten Forderung. Verzicht mit und ohne Besserungsschein. Gesellschafterverzicht versus Drittglaeubigerverzicht. Buchungsbeispiele und Auswirkungen auf das Eigenkapital. Schnittstelle zur Modellrechnung Paragraph 3a Absatz 3 EStG. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Insol Sanierungsgewinn Uebertragende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `insol-sanierungsgewinn-uebertragende-sanierung-asset-deal`

**Fokus:** Uebertragende Sanierung als Asset Deal (Paragraphen 159 ff. InsO) und der Sanierungsgewinn. Beim Asset Deal entsteht kein klassischer Sanierungsertrag beim Schuldner, weil keine Forderungen erlassen werden. Stattdessen Veraeusserungsgewinn bei der Schuldnerin (stille Reserven). Steuerliche Schnittstelle: Paragraph 3a EStG meist nicht direkt anwendbar; Paragraph 75 AO Uebernehmerhaftung. Abgrenzung zur Plan-Sanierung mit Forderungsverzicht.

# Sanierungsgewinn — Uebertragende Sanierung (Asset Deal) und ihre Steuerfolgen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Uebertragende Sanierung (Asset Deal) und ihre Steuerfolgen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Bei der uebertragenden Sanierung wird der Geschaeftsbetrieb der Schuldnerin an eine Auffanggesellschaft verkauft. Das ist **kein** Forderungsverzicht und damit **kein** klassischer Sanierungsertrag im Sinne von Paragraph 3a Absatz 1 EStG. Stattdessen entstehen bei der Schuldnerin Veraeusserungsgewinne durch die Aufdeckung stiller Reserven, und bei der Auffanggesellschaft Anschaffungskosten und ein Step-up.

Dieser Skill grenzt die Asset-Deal-Variante vom Plan-Verzicht ab und zeigt, wo das Sanierungsgewinn-Regime trotzdem indirekt mitspielen kann. Adressat: IV, Plan-Anwalt, StB, Investor-Anwalt.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Plan oder Verfahren sieht eine uebertragende Sanierung vor.
- Auffanggesellschaft soll Vermoegenswerte aus der Insolvenz kaufen.
- Steuerliche Schnittstelle zwischen Asset Deal und Sanierungsertrag muss geklaert werden.

Kaltstart-Fragen:

1. Asset Deal im Regelverfahren oder kombiniert mit Plan?
2. Kaufpreis und stille Reserven der zu uebertragenden Aktiva?
3. Wird der Kaufpreis fuer Forderungsbefriedigung verwendet oder zur Schuldentilgung?
4. Welche Verbindlichkeiten bleiben bei der Schuldnerin (Restmasse)?
5. Erwerber: Auffanggesellschaft, strategischer Investor, Schuldner-Geschaeftsleitung?

## Rechtlicher Rahmen

- Paragraphen 159 ff. InsO — Verwertung der Masse.
- Paragraph 160 InsO — Zustimmung Glaeubigerausschuss.
- Paragraph 162 InsO — Veraeusserung an besonders Interessierte.
- Paragraph 613a BGB — Betriebsuebergang.
- Paragraph 75 AO — Uebernehmerhaftung Steuern.
- Paragraph 3a EStG — Sanierungsertrag; **nicht** typischerweise auf Asset Deal anwendbar.
- Paragraph 16 EStG / Paragraph 8b KStG — Veraeusserungsgewinn.
- BFH, Urteil vom 26.02.2003 — II R 19/01.

## / Schritt fuer Schritt

1. **Asset Deal vs. Plan-Sanierung trennen.** Beim reinen Asset Deal: kein Forderungsverzicht, kein Sanierungsertrag, dafuer Veraeusserungsgewinn.
2. **Stille Reserven identifizieren.** Aktiva fuer Aktiva.
3. **Veraeusserungsgewinn berechnen** (Kaufpreis abzgl. Buchwert).
4. **Verlustvortraege zur Verrechnung pruefen.** Paragraph 10d EStG / Paragraph 10a GewStG; **nicht** Paragraph 3a EStG.
5. **Uebernehmerhaftung Paragraph 75 AO klaeren.** Erwerber haftet fuer Betriebssteuern eines Jahres vor und nach Uebergang; bei Insolvenzkauf modifiziert.
6. **Insolvenzplan-Kombination pruefen.** Wenn das Asset-Deal-Erloes durch den Plan an Glaeubiger ausgekehrt wird und ein Restverzicht entsteht, kann doch ein klassischer Sanierungsertrag entstehen — fuer den verbleibenden Glaeubiger-Verzicht.

## Trade-off-Matrix

| Variante | Wirkung Schuldner | Wirkung Erwerber | Sanierungsertrag |
|---|---|---|---|
| Reiner Asset Deal (Regelverfahren) | Veraeusserungsgewinn, normale Versteuerung | Anschaffungskosten + Step-up | typischerweise kein Paragraph 3a EStG |
| Asset Deal im Plan + Forderungsverzicht | Veraeusserungsgewinn + Sanierungsertrag (auf Restmasse-Verzichte) | Anschaffungskosten + Step-up | Sanierungsertrag fuer Forderungsverzichte; Paragraph 3a EStG-Pruefung |
| Asset Deal an Schuldner-GF (besonders Interessierte) | besondere Zustimmungserfordernisse Paragraph 162 InsO | Anschaffungskosten | dito |
| Asset Deal mit Schuldueberlassung | i.d.R. Sanierungsertrag bei der Schuldnerin, weil Erwerber Verbindlichkeiten uebernimmt | siehe Konstellation | je nach Klausel |
| Liquidation der Schuldnerin nach Asset Deal | spaetere Loeschung, Verbindlichkeiten bleiben (BFH II R 19/01) | abgewickelt | kein Sanierungsertrag, weil kein Verzicht |

## Praxistipps der alten Hasen

1. **Asset Deal ist nicht Sanierungsertrag-Ersatz.** Die Vorstellung, ein Asset Deal "produziere" einen steuerfreien Sanierungsertrag, ist falsch — er produziert einen Veraeusserungsgewinn.
2. **Stille-Reserven-Erfassung wichtig.** Bei niedrigen Buchwerten und hohem Kaufpreis kann der Veraeusserungsgewinn die Verlustvortraege ueberschreiten und Steuern auf die Masse ausloesen.
3. **Paragraph 75 AO modifiziert.** Im Insolvenzverfahren ist die Uebernehmerhaftung nach Paragraph 75 AO unterschiedlich zu beurteilen; pruefen, ob der Erwerb "aus der Insolvenzmasse" privilegiert ist.
4. **Kombination mit Plan-Restverzicht.** Wenn der Asset-Deal-Erloes ueber den Plan ausgekehrt wird und Restquoten erlassen werden, entsteht doch ein Sanierungsertrag fuer den Verzichtsteil — Paragraph 3a EStG dann anwendbar.
5. **Mehrwertsteuer** beim Asset Deal: Geschaeftsveraeusserung im Ganzen Paragraph 1 Absatz 1a UStG; Masseverbindlichkeit Paragraph 55 InsO bei Abweichung.

## Mustertexte / Berechnungsbeispiele

**Beispiel:** GmbH in Insolvenz; Buchwert Aktiva 5 Mio EUR; Kaufpreis Asset Deal 8 Mio EUR. Verbindlichkeiten 20 Mio EUR. Kaufpreis fliesst in Masse, 6 Mio EUR werden an Insolvenzglaeubiger ausgekehrt (Quote 30 %). Plan verzichtet auf die restlichen 14 Mio EUR.

```
EBENE SCHULDNERIN (1) — Asset Deal
Kaufpreis EUR 8.000.000
abzgl. Buchwert Aktiva EUR 5.000.000
= Veraeusserungsgewinn EUR 3.000.000
(regulaer steuerpflichtig; durch Verlustvortraege zu verrechnen)

EBENE SCHULDNERIN (2) — Plan-Restverzicht
Restverzicht im Plan EUR 14.000.000
=> Sanierungsertrag im Sinne von Paragraph 3a EStG, sofern vier
 Voraussetzungen erfuellt.

VERRECHNUNGSREIHENFOLGE
Sanierungsertrag EUR 14.000.000
Veraeusserungsgewinn EUR 3.000.000

Verlustvortraege werden nach Paragraph 3a Absatz 3 EStG primaer durch den
Sanierungsertrag aufgezehrt; Veraeusserungsgewinn bleibt davon getrennt.
=> Risiko: Veraeusserungsgewinn loest Steuern aus, wenn nicht ausreichend
 Verlustvortrag ueber Paragraph 10d EStG verfuegbar.
```

**Vertragstext-Geruest fuer den Asset-Deal-Vertrag (Paragraph 75 AO-Klausel):**

```
§ X Uebernehmerhaftung Paragraph 75 AO

(1) Die Parteien gehen davon aus, dass die Veraeusserung aus der
Insolvenzmasse erfolgt und die Erwerberin damit nach Paragraph 75 Absatz 2
AO von der Uebernehmerhaftung befreit ist.

(2) Der Verkaeufer (Insolvenzverwalter) versichert, dass das Verfahren
zum Zeitpunkt der Veraeusserung in der vorgesehenen Verfahrensphase
[Regelverfahren / Insolvenzplan-Vollzug] ist.

(3) Soweit Paragraph 75 AO-Haftung doch greift, stellt der Verkaeufer den
Erwerber im Verhaeltnis untereinander frei, soweit Mittel der Masse dies
erlauben.
```

## Typische Fehler

1. Asset Deal als "Sanierungsertrag" verbucht — falsch, es ist ein Veraeusserungsgewinn.
2. Stille Reserven nicht ausreichend dokumentiert.
3. Paragraph 75 AO-Klausel im Asset-Deal-Vertrag vergessen.
4. Kombination mit Plan-Restverzicht uebersehen — der zusaetzliche Sanierungsertrag verlangt eigene Paragraph 3a EStG-Pruefung.
5. Umsatzsteuer-Folge Paragraph 1 Absatz 1a UStG nicht beachtet.
6. Annahme, bei Asset Deal in der Insolvenz seien Verlustvortraege erhalten — Paragraph 8c KStG ist zu pruefen, weil der Erwerber je nach Strukturierung schaedliche Anteilsuebertragungen ausloesen kann.

## Querverweise

Im Plugin `insolvenzrecht`:

- `uebertragende-sanierung-und-asset-deals` — Plan-Variante.
- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Verzichtsmechanik.
- `insol-sanierungsgewinn-finanzamt-im-insolvenzverfahren` — FA-Position.
- `insol-sanierungsgewinn-liquidation-statt-plan-folgen` — Liquidationsalternative.

In anderen Plugins:

- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.
- `grosskanzlei-corporate-ma` — Distressed-M-und-A.
- `steuerrecht-anwalt-und-berater` — generelle Steuer-Skills.

## Quellen Stand 06/2026

- Paragraphen 159 ff. InsO, `gesetze-im-internet.de/inso/`.
- Paragraph 613a BGB, `gesetze-im-internet.de/bgb/__613a.html`.
- Paragraph 75 AO, `gesetze-im-internet.de/ao_1977/__75.html`.
- Paragraph 1 Absatz 1a UStG, `gesetze-im-internet.de/ustg_1980/__1.html`.
- Paragraph 8c KStG, `gesetze-im-internet.de/kstg_1977/__8c.html`.
- Paragraph 16 EStG.
- Paragraph 3a EStG.
- BFH, Urteil vom 26.02.2003 — II R 19/01.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 2. `insol-sanierungsgewinn-vergleich-mit-finanzamt-und-stundung`

**Fokus:** Stundung Paragraph 222 AO und Erlass Paragraph 227 AO als Auffanglinien fuer den verbleibenden steuerbaren Restsanierungsertrag. Wenn Paragraph 3a EStG-Voraussetzungen nicht eindeutig erfuellt sind oder ein Restbetrag steuerpflichtig bleibt: persoenliche und sachliche Unbilligkeit begruenden, Vermoegensauflistung, Tatsaechliche Verstaendigung Paragraph 78 AO. Mustertexte Stundungs- und Erlassantrag.

# Sanierungsgewinn — Vergleich mit Finanzamt und Stundung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Vergleich mit Finanzamt und Stundung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Auch wenn Paragraph 3a EStG nicht greift oder ein Restbetrag steuerbar bleibt, ist die Steuer noch nicht zwangslaeufig zu zahlen. Die Abgabenordnung stellt zwei Auffanglinien bereit:

- **Stundung Paragraph 222 AO** — wenn die Einziehung bei Faelligkeit eine erhebliche Haerte bedeutet und die Anspruchsverwirklichung nicht gefaehrdet ist.
- **Erlass Paragraph 227 AO** — wenn die Einziehung sachlich oder persoenlich unbillig waere.

Diese Werkzeuge sind in der Sanierungspraxis wichtig, weil sie auch dann greifen koennen, wenn Paragraph 3a EStG-Voraussetzungen nicht zweifelsfrei erfuellt sind. Adressat: StB, IV, Sachwalter, Plan-Anwalt.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Plan-Modellrechnung zeigt einen Restsanierungsertrag, der nicht zweifelsfrei unter Paragraph 3a EStG faellt.
- Finanzamt lehnt Anwendung Paragraph 3a EStG ab.
- Sanierung ist nur traegbar, wenn Steuer gestundet oder erlassen wird.

Kaltstart-Fragen:

1. Restsanierungsertrag nach Verrechnung — wie hoch?
2. Wieso greift Paragraph 3a EStG nicht (welche Voraussetzung wird angezweifelt)?
3. Vermoegenslage Schuldnerin nach Plan-Vollzug — Liquiditaetsplan vorhanden?
4. Hat das FA bereits einen Bescheid erlassen?
5. Plan-Quote der Insolvenzglaeubiger?

## Rechtlicher Rahmen

- Paragraph 222 AO — Stundung.
- Paragraph 227 AO — Erlass.
- Paragraph 78 AO — tatsaechliche Verstaendigung.
- Paragraph 76 AO — Auskuenfte und Beistand.
- Paragraph 3a EStG — Sanierungsertrag (Hauptlinie).
- Paragraph 251 AO — Insolvenzverfahren.

## / Schritt fuer Schritt

1. **Hauptantrag pruefen: Paragraph 3a EStG**. Erst wenn dieser greift, ist alles andere ueberfluessig.
2. **Hilfslinie Stundung Paragraph 222 AO** vorbereiten:
 - erhebliche Haerte bei Faelligkeit (Sanierung wuerde scheitern, Liquidation drohte).
 - Anspruch nicht gefaehrdet (Liquiditaetsplan zeigt Tilgung in Raten).
3. **Weitere Hilfslinie Erlass Paragraph 227 AO**:
 - sachliche Unbilligkeit (Gesetz zweckverfehlt, hier z. B. wenn Paragraph 3a EStG-Voraussetzung knapp nicht erfuellt).
 - persoenliche Unbilligkeit (Existenz des Unternehmens bei Vollzug bedroht).
4. **Tatsaechliche Verstaendigung Paragraph 78 AO** bei strittigen Tatsachen (z. B. Werthaltigkeit einer Gesellschafterforderung).
5. **Steuerliche Vorabauskunft Paragraph 89 AO** als Praeventions-Werkzeug.
6. **Verhandlungslinie aufbauen** — schriftliche Begruendung, Liquiditaetsplan, Sanierungskonzept beifuegen.

## Trade-off-Matrix

| Werkzeug | Wirkung | Voraussetzung | Risiko |
|---|---|---|---|
| Paragraph 3a EStG | Steuerbefreiung | vier Voraussetzungen | Pruefung FA |
| Paragraph 222 AO | Aufschub | erhebliche Haerte + nicht gefaehrdeter Anspruch | Zinsen ggf. |
| Paragraph 227 AO | endgueltig (oder teilweise) | sachliche/persoenliche Unbilligkeit | hohe Begruendungsanforderung |
| Paragraph 78 AO | Tatsachen-Fixierung | nur fuer Tatsachen, nicht Recht | nicht bindend bei spaeterer Klage gegen Tatsachen-Verstaendigung |
| Klage vor FG | richterliche Klaerung | Bescheid liegt vor | langwierig |
| Kombination Paragraph 3a EStG + hilfsweise Paragraph 227 AO | Standard | parallel zu erklaeren | kein Risiko, wenn klar getrennt |

## Praxistipps der alten Hasen

1. **Immer kaskadiert beantragen.** Hauptantrag Paragraph 3a EStG, hilfsweise Erlass Paragraph 227 AO, hilfsweise Stundung Paragraph 222 AO.
2. **Persoenliche und sachliche Unbilligkeit getrennt begruenden.** Beide Stossrichtungen.
3. **Liquiditaetsplan beifuegen.** Ohne Liquiditaetsplan ist die Stundung schlecht zu rechtfertigen.
4. **Tatsaechliche Verstaendigung** bei strittiger Werthaltigkeit (Gesellschafterverzicht): besser eine Tatsachen-Klaerung im Vorab als spaeter Streit.
5. **Schriftform.** Muendliche Zusagen der FA-Sachbearbeitung sind kein Vertrauensschutz.
6. **Gemeinde im Blick:** Bei GewSt liegt die Hebebezugsentscheidung bei der Gemeinde; Stundung dort gesondert.

## Mustertexte / Berechnungsbeispiele

**Antrag Geruest — Erlass Paragraph 227 AO (Hilfsantrag):**

```
An das Finanzamt [Ort]
Steuernummer [...]
Veranlagungszeitraum: [Jahr]

Antrag auf Erlass nach Paragraph 227 AO (Hilfsweise)
zum Hauptantrag auf Anwendung Paragraph 3a EStG

1. Sachverhalt
[Kurze Darstellung. Verweis auf bestaetigten Plan vom [Datum].]

2. Hauptantrag
Wir beantragen die Anwendung Paragraph 3a Absatz 1 EStG auf den
ermittelten Restsanierungsertrag in Hoehe von EUR [Betrag].
Begruendung siehe Schreiben vom [Datum].

3. Hilfsantrag — Erlass Paragraph 227 AO
Wir beantragen hilfsweise, die Steuer auf den Restsanierungsertrag in
Hoehe von EUR [Betrag] zu erlassen.

3.1 Sachliche Unbilligkeit
Der Gesetzgeber hat mit Paragraph 3a EStG die Steuerfreiheit des
Sanierungsertrags angeordnet. Sollte aus formalen Gruenden die
Anwendung dieser Norm nicht moeglich sein, waere die Einziehung der
Steuer mit dem gesetzlichen Telos nicht vereinbar. Eine sachliche
Unbilligkeit liegt deshalb vor.

3.2 Persoenliche Unbilligkeit
Die Antragstellerin verfuegt nach Plan-Vollzug ueber eine Liquiditaetslage,
die die Einziehung der Steuer unmittelbar in eine erneute
Zahlungsunfaehigkeit fuehren wuerde. Liquiditaetsplan vom [Datum] —
Anlage [...]. Die Sanierung wuerde damit kontraproduktiv konterkariert.

4. Weiter hilfsweise — Stundung Paragraph 222 AO
Wir beantragen weiter hilfsweise Stundung der Steuer auf den
Restsanierungsertrag fuer einen Zeitraum von [X Monaten] mit
Ratenzahlung gemaess Anlage [Tilgungsplan]. Die Anspruchsverwirklichung
ist nicht gefaehrdet (siehe Liquiditaetsplan).

5. Anlagen
[bestaetigter Plan, IDW S 6, Liquiditaetsplan, Tilgungsplan, ggf.
Aktennotiz Werthaltigkeitspruefung]
```

**Antrag Geruest — Tatsaechliche Verstaendigung Paragraph 78 AO:**

```
An das Finanzamt [Ort]
Steuernummer [...]

Antrag auf Tatsaechliche Verstaendigung Paragraph 78 AO

Wir bitten um Aufnahme eines Tatsaechlichen Verstaendigungsverfahrens zu
folgender Tatsache:

Werthaltigkeit der Forderung des Gesellschafters [Name] gegen die
Schuldnerin im Zeitpunkt des Forderungsverzichts am [Datum].

Unsere Auffassung: Werthaltigkeit [X %].
Begruendung: [...] (siehe Anlage Werthaltigkeitsgutachten WP [Name]).

Wir schlagen vor, die Werthaltigkeit einvernehmlich auf [Y %] festzulegen.
```

## Typische Fehler

1. Erlassantrag ohne Hauptantrag — falsche Reihenfolge.
2. Stundungsantrag ohne Liquiditaetsplan.
3. Persoenliche und sachliche Unbilligkeit nicht getrennt begruendet.
4. Muendliche Zusagen FA gefolgt — kein Vertrauensschutz.
5. Tatsaechliche Verstaendigung mit Rechtsfragen vermischt — Paragraph 78 AO nur fuer Tatsachen.
6. Gemeinde-Schiene (GewSt-Hebebezug) vergessen.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Hauptlinie.
- `insol-sanierungsgewinn-finanzamt-im-insolvenzverfahren` — FA-Position.
- `insol-sanierungsgewinn-7b-gewstg-im-insolvenzplan-paralleltrack` — GewSt-Parallel.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — Stundungs-/Erlassmechanik allgemein.
- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.

## Quellen Stand 06/2026

- Paragraph 222 AO, `gesetze-im-internet.de/ao_1977/__222.html`.
- Paragraph 227 AO, `gesetze-im-internet.de/ao_1977/__227.html`.
- Paragraph 78 AO, `gesetze-im-internet.de/ao_1977/__78.html`.
- Paragraph 89 AO.
- Paragraph 3a EStG.
- Paragraph 7b GewStG.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 3. `insol-sanierungsgewinn-verlustvortrag-und-3a-iii-vorab`

**Fokus:** Vorab-Pruefung der Verrechnungsreihenfolge nach Paragraph 3a Absatz 3 EStG vor Insolvenzantrag oder StaRUG-Anzeige. Schritt-fuer-Schritt-Modellrechnung: laufende Verluste des Sanierungsjahres, vortragsfaehige Verluste, weitere Minderungspositionen. Wenn die Verrechnungsmasse den Sanierungsertrag aufzehrt, ist die Steuerfreiheit faktisch sichergestellt — Erlassantrag bleibt formell sinnvoll, materiell aber entbehrlich. Mit Berechnungsschemata und Excel-tauglicher Tabelle.

# Sanierungsgewinn — Verlustvortrag und Paragraph 3a Absatz 3 EStG vorab pruefen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Verlustvortrag und Paragraph 3a Absatz 3 EStG vorab pruefen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Paragraph 3a Absatz 3 EStG ordnet eine zwingende Verrechnungsreihenfolge zwischen dem Sanierungsertrag und den Minderungspositionen an. Wer die Reihenfolge nicht vorab durchgerechnet hat, weiss nicht, wie hoch der **steuerbare Restbetrag** ist, der dann ggf. eine Steuer ausloest — und ob das Steuerrisiko ueberhaupt im sechs-, sieben- oder achtstelligen Bereich liegt.

Dieser Skill macht eine **Schritt-fuer-Schritt-Modellrechnung**, die der Steuerberater des Schuldners gemeinsam mit dem Insolvenzverwalter aufsetzt. Ziel: vor Plan-Einreichung steht eine belastbare Zahl im Raum.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Plan ist in Vorbereitung, Forderungsverzicht der Glaeubiger ist der Groesse nach umrissen.
- Insolvenzverwalter oder Sachwalter braucht eine Zahl, die er der Glaeubigerversammlung vorlegen kann.
- StB will die Wirkung der Verlustvortraege quantifizieren, bevor der Plan-Entwurf finalisiert ist.

Kaltstart-Fragen:

1. Rechtsform des Schuldners (KSt-pflichtig, EStG-pflichtig, transparente PersGes)?
2. Verlustvortraege Stand letzte Veranlagung (KSt-, GewSt-, ggf. ESt-Vortrag)?
3. Voraussichtlicher Sanierungsertrag (Bruttoforderungsverzicht im Plan)?
4. Laufende Verluste des Sanierungsjahres (geschaetzt, bis Plan-Vorlage)?
5. Stille Reserven oder stille Lasten in der Buchhaltung?
6. Mindestbesteuerung Paragraph 10d Absatz 2 EStG: spielt sie hier eine Rolle (Sanierungsertrag verdraengt nach Paragraph 3a Absatz 3 Satz 1 EStG die Mindestbesteuerung)?

## Rechtlicher Rahmen

- Paragraph 3a Absatz 1 EStG — Steuerbefreiung Sanierungsertrag.
- Paragraph 3a Absatz 3 EStG — zwingende Verrechnungsreihenfolge. Der Sanierungsertrag mindert in einer **gesetzlich festgelegten** Abfolge bestehende Verlustpositionen. Erst danach verbleibt der steuerbare Restbetrag.
- Paragraph 10d EStG — Verlustabzug; durch Paragraph 3a Absatz 3 EStG modifiziert.
- Paragraph 8 KStG — Anwendung des EStG-Verlustabzugs auf Koerperschaften.
- Paragraph 7b GewStG i.V.m. Paragraph 36 Absatz 2c GewStG — gewerbesteuerliche Parallel-Regelung mit eigenstaendiger Verrechnungsmechanik.

## / Schritt fuer Schritt

Die Verrechnungslogik laeuft in drei Stufen. Die folgende Tabelle zeigt das Grundmuster fuer Koerperschaften (GmbH, AG); fuer transparente Personengesellschaften ist die Logik auf Gesellschafterebene zu spiegeln.

| Stufe | Position | Behandlung nach Paragraph 3a Absatz 3 EStG |
|---|---|---|
| 1 | Sanierungsertrag (Bruttoforderungsverzicht) | Ausgangsbetrag |
| 2 | abzgl. nicht-betriebsbezogene Aufwendungen iZm dem Forderungsverzicht (Sanierungskosten) | Abzug |
| 2a | abzgl. laufende negative Einkuenfte / Verluste des Sanierungsjahres | Abzug (in einer gesetzlich angeordneten Reihenfolge) |
| 2b | abzgl. vortragsfaehige Verluste aus Vorjahren (Paragraph 10d Absatz 2 EStG) | Abzug |
| 2c | abzgl. ggf. nicht ausgeglichene negative Einkuenfte des Vorjahres | Abzug |
| 2d | weitere gesetzliche Minderungen | Abzug |
| 3 | = steuerbarer Restsanierungsertrag | ggf. nach Paragraph 3a Absatz 1 EStG steuerfrei, soweit Voraussetzungen erfuellt |

**Ergebnis-Szenarien:**

- **Szenario A (Verlustvortraege schlucken alles):** Restsanierungsertrag = 0 EUR. Materiell entfaellt jede Steuerlast aus dem Verzicht; der formelle Antrag bleibt sinnvoll zur Rechtssicherheit, ist materiell aber entbehrlich.
- **Szenario B (Teilabsorption):** Restsanierungsertrag groesser 0. Die vier Voraussetzungen Paragraph 3a Absatz 2 EStG muessen den verbleibenden Betrag steuerfrei stellen; sonst Erlass nach Paragraph 227 AO oder Stundung Paragraph 222 AO pruefen.
- **Szenario C (kein Verlustvortrag):** Voller Sanierungsertrag muss ueber Paragraph 3a EStG getragen werden. Hier ist die Vier-Voraussetzungs-Pruefung **vital**.

## Trade-off-Matrix

| Stellschraube | Wirkung |
|---|---|
| Verlustvortrag hoch | Restsanierungsertrag niedrig — geringes Steuerrisiko, aber Verlustvortrag ist nach Plan **verbraucht** (Paragraph 3a Absatz 3 EStG ordnet den Untergang an) |
| Verlustvortrag niedrig | Restsanierungsertrag hoch — Paragraph 3a Absatz 1 EStG muss greifen, sonst Steuerausfall der Sanierung |
| Buchwertfortfuehrung | stille Reserven verbleiben — kein zusaetzlicher Sanierungsertrag aus Bewertung |
| Aufdeckung stiller Reserven (z. B. bei uebertragender Sanierung) | zusaetzlicher Veraeusserungsgewinn, der **kein** Sanierungsertrag ist und nicht von Paragraph 3a EStG erfasst wird |
| Forderungsverzicht von Gesellschaftern | Sondersicht: Gesellschaftereinlage statt Sanierungsertrag, soweit der Verzicht gesellschaftsrechtlich veranlasst ist |

## Praxistipps der alten Hasen

1. **Erst die Bescheide, dann die Modellrechnung.** Verlustvortraege sind oft mit Vorbehalt der Nachpruefung festgestellt. Wer mit Wunschzahlen rechnet, wird in der Plan-Pruefung zerlegt.
2. **Die zwei Welten KSt und GewSt getrennt fuehren.** Paragraph 7b GewStG kennt eigene Verrechnungsmechaniken; die KSt-Tabelle eins zu eins zu uebernehmen ist falsch.
3. **Mindestbesteuerung Paragraph 10d Absatz 2 EStG entfaellt** beim Sanierungsertrag in der Verrechnungsreihenfolge nach Paragraph 3a Absatz 3 EStG — das ist eine der wichtigsten Erleichterungen. Trotzdem dokumentieren.
4. **Gesellschafter-Verzicht** ist nicht zwingend Sanierungsertrag. Wenn der Gesellschafter aus gesellschaftsrechtlicher Veranlassung verzichtet, ist der Verzicht eine Einlage (verdeckte Kapitalzufuehrung), kein Sanierungsertrag — die Modellrechnung muss diese Trennung leisten.
5. **Stille Reserven sind kein Sanierungsertrag.** Bei Aufdeckung im Plan entstehen Veraeusserungsgewinne, die regulaer steuerpflichtig sind. Trennung schon im Modell auseinanderhalten.
6. **Zinsschranke Paragraph 4h EStG / Paragraph 8a KStG** kann durch den Verzicht wieder Aktualitaet bekommen, weil Zinsvortraege ggf. zu Lasten des Sanierungsertrags genutzt werden — pruefen.

## Mustertexte / Berechnungsbeispiele

**Beispiel 1 — Szenario A:** GmbH, KSt-Verlustvortrag 8.000.000 EUR. Sanierungsertrag aus Plan 5.000.000 EUR. Stufe 1: 5.000.000. Stufe 2a Sanierungskosten 200.000. Stufe 2b KSt-Verlustvortrag verbraucht in Hoehe von 4.800.000. Restsanierungsertrag: 0. Verbleibender KSt-Verlustvortrag nach Sanierung: 3.200.000. **Materiell keine Steuer** aus dem Verzicht.

**Beispiel 2 — Szenario B:** GmbH, KSt-Verlustvortrag 1.500.000 EUR. Sanierungsertrag 5.000.000. Stufe 2a Sanierungskosten 200.000. Stufe 2b Verlustvortrag verbraucht: 1.500.000. Restsanierungsertrag: 3.300.000. Dieser Restbetrag ist nach Paragraph 3a Absatz 1 EStG steuerfrei, wenn die vier Voraussetzungen Paragraph 3a Absatz 2 EStG erfuellt sind. Andernfalls: Steuer rund 0,8 bis 1,0 Mio. EUR (KSt plus GewSt) — fuer den Plan in der Regel toedlich.

**Beispiel 3 — Szenario C:** GmbH, kein Verlustvortrag (junges Unternehmen mit hohem Forderungsverzicht). Sanierungsertrag 2.000.000. Stufe 2a Sanierungskosten 100.000. Restsanierungsertrag: 1.900.000. Nur Paragraph 3a Absatz 1 EStG schuetzt — die vier Voraussetzungen muessen wasserdicht dokumentiert sein.

**Excel-Spalten-Layout (kanzleitauglich):**

```
A: Position
B: Betrag KSt-Sphaere
C: Betrag GewSt-Sphaere
D: Belegquelle
E: Bemerkung

Zeile 1: Sanierungsertrag (Bruttoforderungsverzicht)
Zeile 2: ./. Sanierungskosten Stufe 2
Zeile 3: ./. laufende Verluste Sanierungsjahr Stufe 2a
Zeile 4: ./. Verlustvortrag (Bescheid vom ...)
Zeile 5: ./. weitere Minderungspositionen
Zeile 6: = Restsanierungsertrag
```

## Typische Fehler

1. Verlustvortraege als verlaesslich behandeln, obwohl die Bescheide unter Vorbehalt der Nachpruefung stehen oder strittig sind.
2. KSt- und GewSt-Vortrag verwechseln.
3. Stillen Reservenuntergang als Sanierungsertrag verbuchen — er ist Veraeusserungs- bzw. Bewertungsgewinn.
4. Gesellschafter-Verzicht ohne Werthaltigkeitspruefung als Sanierungsertrag fuehren.
5. Zinsschranke und Zinsvortrag uebersehen.
6. Annahme, Paragraph 3a EStG schliesse Paragraph 10d EStG aus — er **modifiziert** die Reihenfolge, schaltet sie aber nicht ab.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-fruehe-vorbereitung-vor-plan` — Zeitachse.
- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — materielle Vorrats- und Antragsmechanik.
- `insol-sanierungsgewinn-7b-gewstg-im-insolvenzplan-paralleltrack` — GewSt-Parallelitaet.
- `insol-sanierungsgewinn-iv-haftung-fuer-versaumte-3a-iv-antraege` — Haftung Verwalter bei Versaeumnis.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — allgemeine Verlustabzugs-Mechanik.
- `liquiditaetsplanung` — Schwester-Skill fuer Cash-Sicht.

## Quellen Stand 06/2026

- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraph 10d EStG, `gesetze-im-internet.de/estg/__10d.html`.
- Paragraph 8 KStG, `gesetze-im-internet.de/kstg_1977/__8.html`.
- Paragraph 7b GewStG, `gesetze-im-internet.de/gewstg/__7b.html`.
- FG Koeln, Urteil vom 04.11.2025 — 12 K 1413/25 — Antragstellung und Grenzen des steuerfreien Sanierungsgewinns. Verifikation ueber `dejure.org` und NWB-Datenbank.
- FG Koeln, Urteil vom 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977 (vorgehend zu BFH I R 34/12) — Liquidation mit nachrangigem Gesellschafterdarlehen; mit dem Erloeschen der GmbH erloeschen Verbindlichkeiten **und** Verlustvortraege, der rechentheoretisch entstehende Gewinn ist mangels Koerperschaftsteuersubjekt nicht festsetzbar. Wichtige Abgrenzung zum hier geregelten Sanierungspfad.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 4. `insol-sanierungsgewinn-verzicht-bilanz-im-plan`

**Fokus:** Bilanzielle Erfassung des Forderungsverzichts im Insolvenzplan und StaRUG-Plan. Handelsrechtliche und steuerliche Behandlung. Werthaltigkeit der verzichteten Forderung. Verzicht mit und ohne Besserungsschein. Gesellschafterverzicht versus Drittglaeubigerverzicht. Buchungsbeispiele und Auswirkungen auf das Eigenkapital. Schnittstelle zur Modellrechnung Paragraph 3a Absatz 3 EStG.

# Sanierungsgewinn — Forderungsverzicht im Plan, bilanzielle Folgen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Forderungsverzicht im Plan, bilanzielle Folgen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der Forderungsverzicht ist die typische Sanierungsmassnahme im Insolvenzplan und im StaRUG-Plan. Bilanziell loest er einen **Ertrag** aus — den **Sanierungsertrag** —, dessen steuerliche Behandlung ueber Paragraph 3a EStG laeuft. Aber bilanziell, also handelsrechtlich und in der Steuerbilanz, ist die Erfassung nicht in jedem Fall trivial: Werthaltigkeit der Forderung, Verzicht mit oder ohne Besserungsabrede, Gesellschafterverzicht versus Drittglaeubigerverzicht — jede Variante hat eigene Buchungsfolgen.

Dieser Skill ordnet die Konstellationen und liefert konkrete Buchungs-Saetze.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Plan steht vor Vollzug; Buchhaltung des Schuldners muss die Bilanzfolgen vorbereiten.
- StB muss die Steuerbilanz fuer das Sanierungsjahr aufstellen.
- IV oder Sachwalter muss dem Glaeubigerausschuss die wirtschaftlichen Folgen erklaeren.

Kaltstart-Fragen:

1. Wer verzichtet (Drittglaeubiger, Gesellschafter, Mischung)?
2. In welcher Hoehe wurde die Forderung in der Bilanz des Schuldners passiviert?
3. Ist der Verzicht endgueltig oder mit Besserungsabrede?
4. Sind die verzichteten Forderungen werthaltig (Bonitaet des Schuldners ohne Sanierung)?
5. Welcher Rechnungslegungsstandard greift (HGB, IFRS)?

## Rechtlicher Rahmen

- Paragraph 252 Absatz 1 Nr. 4 HGB — Vorsichtsprinzip.
- Paragraph 246 HGB — Vollstaendigkeit.
- Paragraph 266 HGB — Bilanzgliederung.
- Paragraph 397 BGB — Erlass.
- Paragraph 158 BGB — Bedingung (Besserungsschein).
- Paragraph 5 Absatz 1 EStG — Massgeblichkeit der Handelsbilanz.
- Paragraph 5 Absatz 2a EStG — Rangruecktritt und auflosbare Verbindlichkeit.
- Paragraph 3a EStG — steuerliche Begnadigung des Sanierungsertrags.
- BFH, Urteil vom 26.02.2003 — II R 19/01: Verbindlichkeiten bleiben zivilrechtlich ueber die Liquidation hinaus bestehen; blosse Vermoegenslosigkeit begruendet keine Ausbuchung der Verbindlichkeit — Abgrenzung zum Verzicht.

## / Schritt fuer Schritt

1. **Forderung und Bilanzposition zuordnen.** Welche Verbindlichkeit der Schuldnerin steht der verzichteten Forderung gegenueber?
2. **Verzichtsart klaeren.** Endgueltig oder unter Besserungsabrede? Drittglaeubiger oder Gesellschafter?
3. **Werthaltigkeit der Forderung pruefen** (Bonitaet ohne Sanierung): vollwerthaltig, teilwerthaltig, nicht werthaltig.
4. **Bilanzielle Buchung waehlen** (siehe Tabelle).
5. **Steuerliche Behandlung pruefen.** Sanierungsertrag versus Einlage versus auflosbare Verbindlichkeit.
6. **Schnittstelle zu Paragraph 3a Absatz 3 EStG** (Modellrechnung).

## Buchungslogik

**Standardfall: Drittglaeubiger verzichtet endgueltig auf werthaltige Forderung**

```
Soll: Verbindlichkeit gegenueber Drittglaeubiger EUR 1.000.000
Haben: ausserordentlicher Ertrag (Sanierungsertrag) EUR 1.000.000
```

Steuerlich: Sanierungsertrag, Paragraph 3a EStG anwendbar.

**Variante: Gesellschafter verzichtet (gesellschaftsrechtlich veranlasst) auf werthaltige Forderung**

```
Soll: Verbindlichkeit gegenueber Gesellschafter EUR 1.000.000
Haben: Kapitalruecklage Paragraph 272 Absatz 2 Nr. 4 HGB EUR 1.000.000
```

Steuerlich: verdeckte Einlage; **kein** Sanierungsertrag, sondern Erhoehung der Anschaffungskosten der Beteiligung beim Gesellschafter (BFH-Linie zur verdeckten Einlage).

**Variante: Gesellschafter verzichtet auf nicht werthaltige Forderung**

```
Soll: Verbindlichkeit gegenueber Gesellschafter EUR 1.000.000
Haben: Kapitalruecklage (Werthaltigkeit Tag des Verzichts) EUR 200.000
Haben: ausserordentlicher Ertrag (Sanierungsertrag) EUR 800.000
```

Steuerlich: Mischfall; nur der werthaltige Teil ist Einlage, der nicht werthaltige Teil ist Sanierungsertrag. Werthaltigkeitspruefung zwingend (BFH-Linie).

**Variante: Verzicht mit Besserungsabrede (Besserungsschein) gegenueber Drittglaeubiger**

```
Tag des Verzichts:
Soll: Verbindlichkeit EUR 1.000.000
Haben: ausserordentlicher Ertrag (Sanierungsertrag) EUR 1.000.000

Tag des Eintritts des Besserungsfalls:
Soll: ausserordentlicher Aufwand EUR x
Haben: Verbindlichkeit EUR x
```

Steuerlich: Sanierungsertrag entsteht im Verzichtsjahr; spaeterer Wiederaufleben fuehrt zu Aufwand. Wenn der Besserungsfall vor Plan-Vollzug feststeht, ist der Verzicht aufschiebend bedingt und entsteht erst mit Bedingungseintritt — abhaengig von der Klauselgestaltung.

**Variante: nur teilweiser Verzicht (Plan-Quote)**

```
Soll: Verbindlichkeit (verzichteter Teil) EUR 800.000
Haben: ausserordentlicher Ertrag EUR 800.000

Die verbleibenden 20 % bleiben passiviert und werden plangemaess bedient.
```

## Trade-off-Matrix

| Gestaltung | bilanzielle Wirkung | steuerliche Wirkung |
|---|---|---|
| Endgueltiger Verzicht Drittglaeubiger | sofortiger Ertrag | Sanierungsertrag Paragraph 3a EStG |
| Verzicht mit Besserungsschein | sofortiger Ertrag mit potenzieller Rueckbuchung | Sanierungsertrag im Verzichtsjahr; Rueckbuchung im Besserungsjahr Aufwand |
| Gesellschafter-Verzicht werthaltig | Erhoehung Kapitalruecklage | verdeckte Einlage, kein Sanierungsertrag |
| Gesellschafter-Verzicht nicht werthaltig | gemischt | werthaltiger Teil Einlage, Rest Sanierungsertrag |
| Rangruecktritt qualifiziert (Paragraph 5 Absatz 2a EStG) | Verbindlichkeit bleibt | erst bei spaeterer Aufloesung Ertrag |
| Schuldumwandlung (DES) | Verbindlichkeit wird Eigenkapital | siehe Skill DES |

## Praxistipps der alten Hasen

1. **Werthaltigkeitspruefung dokumentieren.** Beim Gesellschafterverzicht entscheidet die Werthaltigkeit der Forderung am Tag des Verzichts. Spaetere Sicht ist irrelevant.
2. **Besserungsabrede genau formulieren.** Eine missverstaendliche Klausel kann den gesamten Sanierungsertrag steuerlich nach hinten verschieben — oder umgekehrt vorziehen.
3. **HGB- und Steuerbilanz auseinander halten.** Massgeblichkeit nach Paragraph 5 Absatz 1 EStG, aber Sonderregeln greifen.
4. **Konzern-Verzichte sind heikel.** Verdeckte Einlage Mutter zugunsten Tochter laeuft anders als ueber Schwesterunternehmen.
5. **Achtung Ausbuchung mangels Schuldner.** Verbindlichkeiten bleiben nach BFH II R 19/01 ueber blosse Vermoegenslosigkeit hinaus bestehen — keine erleichterte Ausbuchung; Verzicht ist eigene Kategorie.

## Mustertexte / Berechnungsbeispiele

**Aktennotiz Werthaltigkeitspruefung Gesellschafter-Verzicht:**

```
AKTENNOTIZ WERTHALTIGKEITSPRUEFUNG
Schuldnerin: [Name]
Gesellschafter: [Name]
Forderung: EUR [Betrag]
Tag des Verzichts: [Datum]

1. Sachverhalt
Der Gesellschafter [Name] verzichtet im Rahmen des Insolvenzplans / StaRUG-
Plans auf seine Forderung in Hoehe von EUR [Betrag] gegen die Schuldnerin.

2. Werthaltigkeit am Tag des Verzichts
Zu pruefen ist, ob die Forderung am Tag des Verzichts werthaltig war.
- Vermoegenslage Schuldnerin laut Bilanz vom [Datum]: EUR [...]
- Forderungsbestand insgesamt: EUR [...]
- Hypothetische Liquidationsquote: [%]
- Forderung des Gesellschafters: EUR [Betrag]
- Hypothetisch realisierbarer Betrag: EUR [Betrag] x [%] = EUR [...]

3. Bewertung
Die Forderung war zu [%] werthaltig. Daher: verdeckte Einlage in Hoehe
EUR [...], Sanierungsertrag in Hoehe EUR [...].

4. Verbuchung
[wie oben Variante "nicht werthaltig"]
```

## Typische Fehler

1. Werthaltigkeitspruefung beim Gesellschafterverzicht uebergangen — Ertrag faelschlich als Sanierungsertrag verbucht.
2. Besserungsschein-Klausel als unmittelbaren Verzicht behandelt.
3. Konzern-Verzicht ueber Schwester ohne Beruecksichtigung der Dreiecksbeziehung verbucht.
4. HGB- und Steuerbilanz nicht abgestimmt.
5. Ausbuchung mangels Schuldner mit Verzicht verwechselt (BFH II R 19/01 nicht beachtet).
6. Bei nur teilweisem Verzicht (Plan-Quote) Buchung als Vollverzicht.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — materielle Voraussetzungen.
- `insol-sanierungsgewinn-verlustvortrag-und-3a-iii-vorab` — Verrechnung.
- `insol-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg-im-plan` — Rangruecktritt.
- `insol-sanierungsgewinn-debt-equity-swap-im-plan` — DES.
- `insol-sanierungsgewinn-massehaftungsbefreiung-und-bilanz` — Massehaftung-Bilanz-Effekte.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — Bilanzsteuerrecht.
- `grosskanzlei-corporate-ma` — Distressed-Bilanz-Themen.

## Quellen Stand 06/2026

### Normen

- Paragraphen 246, 252, 266, 272 HGB, `gesetze-im-internet.de/hgb/`.
- Paragraph 5 EStG, `gesetze-im-internet.de/estg/__5.html`.
- Paragraph 5 Absatz 2a EStG.
- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraph 6 Absatz 1 Nummer 3 EStG, Paragraph 12 Absatz 1 BewG (Nennwert).
- Paragraphen 158, 397 BGB, `gesetze-im-internet.de/bgb/`.
- Paragraph 11 KStG (Liquidationsbesteuerung).

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 26.02.2003 — II R 19/01** — Verbindlichkeiten gehen nicht allein durch Vermoegenslosigkeit unter.
- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Passivierung nur bei wirtschaftlicher Belastung.
- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — Paragraph 5 Absatz 2a EStG bei Rangruecktritt mit Tilgungsvorbehalt aus zukuenftigen Gewinnen.
- **FG Koeln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** — Os. 7: Rangruecktrittsbehaftete Verbindlichkeit bleibt bis Loeschung passiviert; rechtstheoretisch entstehender Gewinn nach Loeschung mangels Steuersubjekt nicht steuerpflichtig (vorgehend zu BFH I R 34/12).
- **BFH, Beschl. v. 05.02.2014 — I R 34/12, BFH/NV 2014, 1014** — bestaetigt FG-Koeln-Linie als „nicht evident rechtsfehlerhaft".

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfuegung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782** — ertragsteuerliche Beurteilung von Darlehensverbindlichkeiten im Abwicklungsendvermoegen; Aktualitaet vor Anwendung pruefen.
- **OFD Frankfurt a. M., Rundverfuegung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560** — Vorgaengerverfuegung.
- **OFD Nordrhein-Westfalen, Kurzinformation ESt Nr. 46/2014, akt. 22.09.2017, DB 2017, 2580** — Sichtweise NRW.

### Literatur

- Bergmann, Liquidationsbesteuerung von Kapitalgesellschaften, Diss., 2012, S. 145 ff.
- Dietrich/Weber, DStR 2019, 966, 970.
- Hageboeke, in: Roedder/Herlinghaus/Neumann, KStG, 1. Aufl. 2015, Paragraph 11 Rn. 78.

Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.
