---
name: vollrelation-langfassung-vorlaeufige
description: "Vollrelation Langfassung Vorlaeufige: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vollrelation Langfassung Vorlaeufige

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vollrelation Langfassung Vorlaeufige** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vollrelation-langfassung` | Vollständige Relation im Schulstandard für Referendar-/Assessorprüfung ausformulieren: Kandidat benoetigt Langfassung mit gutachterlichem Stil. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Auslegung Streitgegenstand, jede Station (Zulässigkeit, Schluessigkeit, Erheblichkeit, Replik, Beweisstation, Tenorierung) als eigener Abschnitt mit ORSA (Obersatz, Regel, Subsumtion, Abschluss). Output Vollrelation bis 20 Seiten, alle Stationen. Abgrenzung: Kurzfassung für Praxis siehe relation-zivil; Schulung siehe schulung-urteilsbauer. |
| `vorlaeufige-vollstreckbarkeit` | Anordnung zur vorlaeufigen Vollstreckbarkeit nach §§ 708-720a ZPO bestimmen: Richter muss die richtige Vollstreckbarkeitsermaechtigungs-Formel formulieren. Normen: § 709 ZPO (Sicherheitsleistung 110%), § 711 ZPO (Schutzantrag Schuldner), § 713 ZPO (vereinfachte Vollstreckbarkeit), § 708 Nr. 2 ZPO (Versaeumnisurteil). Prüfraster: Beschwerdehoehedifferenz, Sicherheitsleistungs-Pflichtteil, Schutzantrag. Output Vollstreckbarkeits-Formel. Abgrenzung: Kostenentscheidung siehe kostenentscheidung-bauen; Berufung siehe berufungsfest-prüfen. |
| `zulaessigkeit-pruefen` | Zulässigkeit der Zivilklage systematisch prüfen: Richter oder Referendar prüft Prüfstation Zulässigkeit. Normen: § 13 GVG (Rechtsweg), EuGVVO Bruessel Ia (internationale Zuständigkeit), §§ 12 ff. ZPO (örtliche Zuständigkeit), § 23 GVG (sachliche Zuständigkeit), §§ 1 ff. GKG (Streitwert). Prüfraster: Rechtsweg, internationale Zuständigkeit, örtliche und sachliche Zuständigkeit, Partei-/Prozessfähigkeit, Rechtsschutzbedürfnis, besondere Verfahrensarten. Output Zulässigkeits-Prüfungsschema. Abgrenzung: Meritorische Prüfung siehe anspruchsgrundlagen-prüfen; Verwaltungsgericht siehe fachanwalt-verwaltungsrecht-Plugin. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Vollrelation Langfassung Vorlaeufige**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vollrelation-langfassung`

**Fokus:** Vollständige Relation im Schulstandard für Referendar-/Assessorprüfung ausformulieren: Kandidat benoetigt Langfassung mit gutachterlichem Stil. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Auslegung Streitgegenstand, jede Station (Zulässigkeit, Schluessigkeit, Erheblichkeit, Replik, Beweisstation, Tenorierung) als eigener Abschnitt mit ORSA (Obersatz, Regel, Subsumtion, Abschluss). Output Vollrelation bis 20 Seiten, alle Stationen. Abgrenzung: Kurzfassung für Praxis siehe relation-zivil; Schulung siehe schulung-urteilsbauer.

# Vollrelation Langfassung - Schulstandard für Prüfung

**Vorsicht: hiermit bitte nicht mogeln im Studium.** Dieser Skill schreibt eine ausformulierte Vollrelation auf Prüfungsstandard. Genau deswegen ist die Verwendung als eingereichte Klausur- oder Hausarbeitsleistung im juristischen Vorbereitungsdienst eine Prüfungstaeuschung (Paragraf 14 JAG NRW Paragraf 12 JAPO Bayern und vergleichbare Vorschriften der Länder). Folge: Nichtbestehen Aberkennung Disziplinarverfahren. Erlaubt und sinnvoll: Erst selbst schreiben dann mit dieser Vollrelation abgleichen und Schwaechen finden.

Dieser Skill schreibt eine ausformulierte Vollrelation in der Form wie sie im Referendariat und in der Assessor/-innen-Prüfung verlangt wird. Im Gegensatz zur Praxis-Kurzform werden alle Stationen ausgeschrieben als Fliesstext mit Obersatz Definition Subsumtion Ergebnis (Gutachtenstil im Sachverhalt-Teil; Urteilsstil nur dort wo am Ende übernommen wird).

Laenge: 8 bis 20 Seiten je nach Aktenumfang. Schreibstil: gutachterlich klar normverankert. Jedes Zitat einer Norm in der Form **Paragraf 433 BGB** oder **Artikel 35 CISG**.

## Aufbau (zwingend in dieser Reihenfolge)

### Teil A Sachbericht

Chronologischer neutraler Bericht. Unstreitiges im Indikativ Perfekt. Streitiges in der Form **Die Klägerin behauptet ...** und **Die Beklagte bestreitet ...**. Anträge im Originalwortlaut zitieren.

Laenge: ein bis vier Seiten je nach Aktenumfang.

### Teil B Auslegung

Genau bezeichnen welcher Streitgegenstand vorliegt. Bei Klagehaeufung jeden Antrag einzeln auslegen. Hilfsantrag prozessualer Eventualantrag.

### Teil C Zulässigkeit

Jeden Pruefpunkt mit eigenem Absatz. Beispielstruktur:

> **Internationale Zuständigkeit.** Die internationale Zuständigkeit deutscher Gerichte ergibt sich aus Artikel 7 Nummer 1 b der Verordnung Nummer 1215 2012 (EuGVVO). Danach kann eine Person die ihren Wohnsitz im Hoheitsgebiet eines Mitgliedstaats hat in einem anderen Mitgliedstaat vor dem Gericht des Erfüllungsorts verklagt werden. Erfüllungsort ist nach Artikel 7 Nummer 1 b erster Spiegelstrich der Ort der vertraglichen Lieferung. Hier wurde die Brille nach Hamburg geliefert. Die internationale Zuständigkeit ist gegeben.

Für jeden Pruefpunkt einen solchen Absatz schreiben. Bei nicht problematischen Punkten kurz halten (eine Zeile genuegt).

### Teil D Schlüssigkeit

Die Schlüssigkeitsprüfung ist das Herzstück. Schreibe in dieser Form:

> **Anspruch der Klägerin gegen die Beklagte auf Zahlung von 1197 EUR Zug um Zug gegen Rueckgabe nach Artikel 81 Absatz 2 CISG.**
>
> Die Klägerin koennte einen Anspruch auf Rückzahlung des Kaufpreises gegen die Beklagte aus Artikel 81 Absatz 2 CISG haben. Voraussetzungen sind ein wirksamer Kaufvertrag im Anwendungsbereich des CISG eine wesentliche Vertragsverletzung der Beklagten und eine wirksame Aufhebungserklärung der Klägerin.
>
> **a) Anwendbarkeit des CISG.** Das CISG ist anwendbar gemäß Artikel 1 Absatz 1 a CISG ...
> **b) Wirksamer Kaufvertrag.** ...
> **c) Vertragsmaessigkeit der Ware.** Nach Artikel 35 Absatz 1 CISG ...
> **d) Wesentliche Vertragsverletzung Artikel 25 CISG.** ...
> **e) Aufhebungserklärung Artikel 26 CISG.** ...
>
> **Zwischenergebnis Schlüssigkeit:** Bei unterstellter Richtigkeit des Klägervortrags hat die Klägerin einen Anspruch aus Artikel 81 Absatz 2 CISG auf Zahlung von 1197 EUR Zug um Zug gegen Rueckgabe der Brille. Die Klage ist schlüssig.

Wenn die Klage unschlüssig ist: Klar herausarbeiten an welchem Tatbestandsmerkmal es hängt; dann Hinweis nach Paragraf 139 ZPO erwaegen.

### Teil E Erheblichkeit

Für jeden Beklagteneinwand einen eigenen Absatz:

> **Einwand 1: AGB-Gerichtsstandsvereinbarung Zuerich.** Die Beklagte beruft sich auf Ziffer 18.1 ihrer AGB. Diese Klausel waere nur wirksam wenn sie nach Artikel 25 EuGVVO formgerecht vereinbart waere und nicht durch eine kollidierende Klausel der Klägerin verdraengt würde. Hier liegt der Knock-out-Fall vor (BGH siehe oben). Damit ist der Einwand unerheblich.
>
> **Einwand 2: CISG-Ausschluss durch AGB.** Die Beklagte beruft sich auf Ziffer 17.1. ...
>
> **Einwand 3: kein Sachmangel.** ...
>
> **Einwand 4: Gefahrübergang FOB Galway.** ...

Für jeden Einwand am Ende festhalten: **erheblich** oder **unerheblich** und warum.

### Teil F Replik

Die Repliken der Klägerin durchgehen und wie in Teil E klassifizieren.

### Teil G Beweisstation

Tabelle mit allen verbleibenden streitigen Tatsachen Beweislast Beweismittel Beweismass.

### Teil H Tenorierungsvarianten

Drei Varianten ausschreiben:

> **Variante A** (Klage vollständig begründet): Tenor lautet ...
> **Variante B** (Klage teilweise begründet): Tenor lautet ...
> **Variante C** (Klage abzuweisen): Tenor lautet ...

Die wahrscheinlichste Variante markieren und kurz begründen.

### Teil I Nebenentscheidungen

Kosten vorläufige Vollstreckbarkeit Streitwert Zinsen Rechtsmittelzulassung. Wie in Skill `relation-zivil` Station 9 aber ausformuliert.

### Teil J Selbstkontrolle

Fragenkatalog am Ende:

- Sind alle Anträge beschieden?
- Sind alle erheblichen Einwendungen abgearbeitet?
- Ist der Tenor vollstreckungsfähig?
- Sind die Kosten richtig verteilt?
- Ist die vorläufige Vollstreckbarkeit korrekt?
- Ist die Rechtsmittelbelehrung erforderlich?

## Stilfragen

- Keine Wertungen im Sachbericht.
- Konjunktiv I für Parteivortrag (Die Klägerin behauptet die Brille zeichne ...).
- Indikativ für Unstreitiges (Die Klägerin hat die Brille am 19. Februar 2026 erhalten).
- Normzitate ausgeschrieben (Paragraf 433 Absatz 1 Satz 1 BGB).
- Keine Abkürzungen wie BGH BVerfG sondern Bundesgerichtshof Bundesverfassungsgericht beim ersten Auftreten ausschreiben.

## Ausgabeformat

Markdown mit klaren Hierarchien (## A Sachbericht ## B Auslegung ...). Bei DOCX-Render-Wunsch kann das Ergebnis mit dem Skill `dokumente-rendern-urteil-docx` als Relations-Dokument im Schul-Layout ausgegeben werden (separater Modus --typ relation).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `vorlaeufige-vollstreckbarkeit`

**Fokus:** Anordnung zur vorlaeufigen Vollstreckbarkeit nach §§ 708-720a ZPO bestimmen: Richter muss die richtige Vollstreckbarkeitsermaechtigungs-Formel formulieren. Normen: § 709 ZPO (Sicherheitsleistung 110%), § 711 ZPO (Schutzantrag Schuldner), § 713 ZPO (vereinfachte Vollstreckbarkeit), § 708 Nr. 2 ZPO (Versaeumnisurteil). Prüfraster: Beschwerdehoehedifferenz, Sicherheitsleistungs-Pflichtteil, Schutzantrag. Output Vollstreckbarkeits-Formel. Abgrenzung: Kostenentscheidung siehe kostenentscheidung-bauen; Berufung siehe berufungsfest-prüfen.

# Vorläufige Vollstreckbarkeit


## Triage zu Beginn

1. Welcher Entscheidungstyp liegt vor — Endurteil, Versäumnisurteil, Anerkenntnisurteil, Beschluss?
2. Wie hoch ist der Verurteilungsbetrag — bis 1.500 EUR (§ 708 Nr. 11 ZPO) oder darüber (§ 709 ZPO)?
3. Ist Berufung statthaft (Beschwer > 600 EUR) — wenn nein: § 713 ZPO (ohne Sicherheit)?
4. Hat die unterlegene Partei einen Schutzantrag nach § 711 ZPO gestellt?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 708 ZPO — Vollstreckbarkeit ohne Sicherheitsleistung (Nr. 1-11 Aufzählung)
 - Nr. 2: Versäumnisurteil
 - Nr. 4: Anerkenntnisurteil
 - Nr. 11: Endurteile bis 1.500 EUR
- § 709 ZPO — Vollstreckbarkeit gegen Sicherheitsleistung von 110 Prozent (Regel)
- § 711 ZPO — Schutzantrag der unterliegenden Partei
- § 713 ZPO — keine Sicherheit bei fehlendem Rechtsmittel (Beschwer ≤ 600 EUR)
- § 719 ZPO — Einstellung der Vollstreckung bei Berufung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Entscheidungsbaum

```
Entscheidungstyp?
├── Versäumnisurteil → § 708 Nr. 2 ZPO (ohne Sicherheit)
├── Anerkenntnisurteil → § 708 Nr. 4 ZPO (ohne Sicherheit)
├── Endurteil bis 1.500 EUR → § 708 Nr. 11 ZPO (ohne Sicherheit)
└── Endurteil über 1.500 EUR:
 ├── Berufung statthaft (Beschwer > 600 EUR)? → § 709 ZPO (110 Prozent Sicherheit)
 │ └── Schutzantrag § 711 ZPO gestellt? → § 711 ZPO Formulierung ergänzen
 └── Berufung nicht statthaft (Beschwer ≤ 600 EUR, keine Zulassung)? → § 713 ZPO (ohne Sicherheit)
```

## Output-Template

**Adressat:** Urteil → Tenor (Ziff. 3) — Tonfall: formal-amtlich

```
## Vorläufige Vollstreckbarkeit

**Standardfall § 709 ZPO:**
"Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn
Prozent des jeweils zu vollstreckenden Betrages."

**Bei § 713 ZPO (keine Berufung):**
"Das Urteil ist ohne Sicherheitsleistung vorläufig vollstreckbar."

**Bei Schutzantrag § 711 ZPO:**
"Der Beklagten wird nachgelassen, die Vollstreckung gegen Sicherheitsleistung in Höhe von
einhundertzehn Prozent des jeweils zu vollstreckenden Betrages abzuwenden, wenn nicht die
Klägerin vor der Vollstreckung Sicherheit in gleicher Höhe leistet."
```

## Standardregelung

Paragraf 709 ZPO - vorläufige Vollstreckbarkeit gegen Sicherheitsleistung von 110 von hundert (110 Prozent) des jeweils zu vollstreckenden Betrages.

## Wann andere Regelung

- Paragraf 708 Nr. 1 ZPO - urkundliche Mahnsachen
- Paragraf 708 Nr. 2 ZPO - Versäumnisurteile - ohne Sicherheit
- Paragraf 708 Nr. 4 ZPO - Anerkenntnisurteile
- Paragraf 708 Nr. 11 ZPO - bestimmte Endurteile bis 1500 EUR (Repo-Konvention Punkt)
- Paragraf 711 ZPO - Schutzantrag der unterliegenden Partei (Sicherheitsleistung wegen unverhältnismaessigen Schadens)
- Paragraf 713 ZPO - Beschwer unter 600 EUR und keine Berufung - ohne Sicherheit
- Paragraf 719 ZPO - Aufhebung bei Berufung

## Formulierung

- "Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn Prozent des jeweils zu vollstreckenden Betrages."
- "Das Urteil ist vorläufig vollstreckbar."
- Bei Schutzantrag: "Der Beklagten wird nachgelassen, die Vollstreckung gegen Sicherheitsleistung in Höhe von 110 von hundert des jeweils zu vollstreckenden Betrages abzuwenden, wenn nicht der Kläger Sicherheit in Höhe des jeweils zu vollstreckenden Betrages leistet."


---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

Dieser Skill wurde im Rahmen von Bundle 046 auf halluzinierte Rechtsprechungsnachweise geprüft und korrigiert.

## 3. `zulaessigkeit-pruefen`

**Fokus:** Zulässigkeit der Zivilklage systematisch prüfen: Richter oder Referendar prüft Prüfstation Zulässigkeit. Normen: § 13 GVG (Rechtsweg), EuGVVO Bruessel Ia (internationale Zuständigkeit), §§ 12 ff. ZPO (örtliche Zuständigkeit), § 23 GVG (sachliche Zuständigkeit), §§ 1 ff. GKG (Streitwert). Prüfraster: Rechtsweg, internationale Zuständigkeit, örtliche und sachliche Zuständigkeit, Partei-/Prozessfähigkeit, Rechtsschutzbedürfnis, besondere Verfahrensarten. Output Zulässigkeits-Prüfungsschema. Abgrenzung: Meritorische Prüfung siehe anspruchsgrundlagen-prüfen; Verwaltungsgericht siehe fachanwalt-verwaltungsrecht-Plugin.

# Zulässigkeit der Zivilklage

Schritt-für-Schritt Prüfung der Zulässigkeit nach klassischem Schema.

## Triage zu Beginn

1. Liegt internationaler Bezug vor — ist EuGVVO (Brüssel Ia, VO Nr. 1215/2012) anwendbar?
2. Was ist der Streitwert — sachliche Zuständigkeit AG (bis 10.000 EUR, § 23 Nr. 1 GVG n. F. für Neufälle seit 01.01.2026) oder LG (über 10.000 EUR, § 71 GVG)? Übergangsfälle live prüfen.
3. Ist der Kläger Verbraucher — besonderer Gerichtsstand nach Art. 17 ff. EuGVVO?
4. Gibt es eine ausschließliche Gerichtsstandsvereinbarung (§ 38 ZPO, Art. 25 EuGVVO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 13 GVG — ordentlicher Rechtsweg
- § 23 Nr. 1 GVG — sachliche Zuständigkeit AG (bis 10.000 EUR in der aktuellen Fassung für Neufälle seit 01.01.2026)
- § 71 Abs. 1 GVG — sachliche Zuständigkeit LG (regelmäßig über 10.000 EUR, Sonderzuständigkeiten prüfen)
- § 12 ZPO — allgemeiner Gerichtsstand (Wohnsitz)
- § 29 ZPO — besonderer Gerichtsstand Erfüllungsort
- § 38 ZPO — Gerichtsstandsvereinbarung (B2B)
- Art. 4, 7, 17 EuGVVO (VO Nr. 1215/2012) — internationale Zuständigkeit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Rechtsweg (§ 13 GVG):** Ist die ordentliche Gerichtsbarkeit eröffnet (kein Arbeits-, Verwaltungs- oder Sozialrecht)?
2. **Internationale Zuständigkeit:** Auslandsbezug → EuGVVO oder nationales IPR-Zuständigkeitsrecht.
3. **Örtliche Zuständigkeit (§§ 12 ff. ZPO):** Allgemeiner oder besonderer Gerichtsstand?
4. **Sachliche Zuständigkeit (§§ 23, 71 GVG):** Streitwert bestimmen → AG oder LG?
5. **Partei- und Prozessfähigkeit (§§ 50, 51 ZPO):** Beide Parteien rechtsfähig und prozessfähig?
6. **Anwaltszwang (§ 78 ZPO):** Vor LG und höheren Gerichten zwingend.
7. **Rechtsschutzbedürfnis:** Allgemeines Feststellungsinteresse (§ 256 ZPO) — nur bei Feststellungsklage.

## Output-Template

**Adressat:** Entscheidungsgründe → Abschnitt Zulässigkeit — Tonfall: sachlich-juristisch

```
## I. Zulässigkeit

Die Klage ist zulässig.

**Rechtsweg:** Der ordentliche Rechtsweg nach § 13 GVG ist eröffnet. [Alternativ: Verwiesen nach § 281 ZPO.]

**Sachliche Zuständigkeit:** Das Amtsgericht [ORT] ist sachlich zuständig nach § 23 Nr. 1 GVG,
da der Streitwert [BETRAG] EUR beträgt und damit die aktuelle Grenze von 10.000 EUR nicht überschreitet; Übergangsfälle und Sonderzuständigkeiten sind gesondert geprüft.

**Örtliche Zuständigkeit:** Das Amtsgericht [ORT] ist örtlich zuständig nach § 29 ZPO
(Erfüllungsort [ORT]).

**Partei- und Prozessfähigkeit:** Beide Parteien sind partei- und prozessfähig nach §§ 50, 51 ZPO.
```

## Pruefpunkte

1. **Rechtsweg** Paragraf 13 GVG, Verweisung Paragraf 17 GVG
2. **Internationale Zuständigkeit** EuGVVO Brüssel Ia (Verordnung Nr. 1215 2012), Luganer Übereinkommen, autonomes Recht (Paragraf 12 ff ZPO entsprechend)
3. **Örtliche Zuständigkeit** Paragrafen 12 ff ZPO (allgemeine), Paragrafen 21 ff ZPO (besondere), Paragraf 24 ZPO (ausschließliche)
4. **Sachliche Zuständigkeit** § 23 GVG (AG bis 10.000 EUR in der aktuellen Fassung für Neufälle), § 71 GVG (LG darüber); Alt- und Übergangsfälle gesondert prüfen.
5. **Streitwert** Paragraf 3 ZPO, Paragraf 1 GKG, Anlage 1 zum GKG
6. **Partei- und Prozessfähigkeit** Paragraf 50 ff ZPO
7. **Vertretung** Paragraf 51 ZPO, Paragraf 78 ZPO (Anwaltszwang)
8. **Streitgenossenschaft** Paragraf 59 ff ZPO
9. **Rechtsschutzbedürfnis**
10. **Anhaengigkeit / Rechtshaengigkeit** Paragraf 261 ZPO, Verbot anderweitiger Rechtshaengigkeit

## Sonderfälle

- Verbraucherklage in B2C-Sachen: Artikel 17 ff Brüssel Ia
- Arrest / einstweilige Verfügung: Paragrafen 916 ff, 935 ff ZPO
- Familiensachen: FamFG
- Mahnverfahren: Paragrafen 688 ff ZPO

## Ausgabe

Tabelle: Pruefpunkt / Norm / Ergebnis / Begründung.
