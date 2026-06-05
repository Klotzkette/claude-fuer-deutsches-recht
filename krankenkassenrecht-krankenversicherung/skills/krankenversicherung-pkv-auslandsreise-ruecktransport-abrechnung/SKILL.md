---
name: krankenversicherung-pkv-auslandsreise-ruecktransport-abrechnung
description: "PKV Auslandsreise Ruecktransport Abrechnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PKV Auslandsreise Ruecktransport Abrechnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **PKV Auslandsreise Ruecktransport Abrechnung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-036-pkv-auslandsreise-und-ruecktransport` | PKV-Leistungen auf Auslandsreisen: Geltungsbereich, medizinisch notwendige Behandlung im Ausland, Rücktransport und Koordination mit Reisekrankenversicherung. |
| `kv-037-abrechnung-goae-goz-und-erstattung` | Ärztliche (GOÄ) und zahnärztliche (GOZ) Abrechnung: Steigerungsfaktoren, Analogleistungen, Begründungspflichten und Erstattungsansprüche in der PKV und Beihilfe. |
| `kv-038-heilpraktiker-alternative-medizin-und-tarifbedingungen` | Erstattung von Heilpraktiker-Behandlungen und alternativer Medizin in PKV und GKV: Tarif­bedingungen, Leistungsumfang, Evidenzanforderungen und Ablehnungsgründe. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **PKV Auslandsreise Ruecktransport Abrechnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-036-pkv-auslandsreise-und-ruecktransport`

**Fokus:** PKV-Leistungen auf Auslandsreisen: Geltungsbereich, medizinisch notwendige Behandlung im Ausland, Rücktransport und Koordination mit Reisekrankenversicherung.

# PKV: Auslandsreise und Rücktransport

## Skill-Zweck

Die PKV deckt Behandlungen auch im Ausland ab, aber mit Einschränkungen. Dieser Skill klärt **Geltungsbereich, Rücktransport und das Verhältnis zur Reisekrankenversicherung**.

## Rechtlicher Rahmen

- **§ 192 VVG i.V.m. MB/KK 2009 § 1 Abs. 3** – Weltweiter Versicherungsschutz bei vielen Tarifen
- **MB/KK 2009 § 10** – Umfang und Grenzen im Ausland
- **Tarif-AVB** (Allgemeine Versicherungsbedingungen): konkrete Auslandsklauseln
- **§ 193 VVG** – Versicherungspflicht schließt Auslandsbehandlung ein
- BGH IV ZR 119/09 (medizinisch notwendige Behandlung im Ausland), BGH IV ZR 166/05

## Leistungsumfang im Ausland

| Leistungstyp | PKV-Leistungspflicht | Einschränkungen |
|-------------|---------------------|-----------------|
| Ambulante Behandlung | Ja, in der Regel | Medizinisch notwendig; nicht elektiv |
| Stationäre Behandlung | Ja, in der Regel | Notfall oder Unaufschiebbarkeit |
| Rücktransport | Nur wenn im Tarif | Explizit prüfen; oft Zusatztarif |
| Geplante Behandlung im Ausland | Nein (ohne Genehmigung) | Tourismus-Medizin ausgeschlossen |
| Zahnbehandlung Notfall | Begrenzt | Schmerzbehandlung ja; Zahnersatz nein |

## Prüfprogramm

### Schritt 1 – Tarif-Geltungsbereich
- MB/KK oder Tarif-AVB: Weltweit? Europa? Ausnahmen (z.B. USA nur begrenzt)?
- Viele Tarife: weltweiter Schutz für bis zu 6 Wochen; längerer Aufenthalt: separate Prüfung
- Expatriates/Langzeitaufenthalt: separate Auslandskrankenversicherung empfehlen

### Schritt 2 – Medizinische Notwendigkeit im Ausland
- Gleicher Maßstab wie im Inland: medizinisch notwendige Heilbehandlung
- Nicht elektiv: keine geplanten Schönheitsoperationen im Ausland
- Notfall: immer versichert (auch bei USA-Aufenthalt mit hohen Kosten)

### Schritt 3 – Rücktransport
- Oft NICHT im Standardtarif enthalten; separater Rücktransport-Baustein oder Reiseschutzversicherung nötig
- PKV-Rücktransport wenn medizinisch notwendig: Behandlung in Deutschland zwingend besser?
- Praxis: Reisekrankenversicherung (z.B. ADAC, Allianz) übernimmt Rücktransport

### Schritt 4 – USA und Hochkostenländer
- Ärztliches Honorar USA: GOÄ-Niveau gilt nicht; PKV erstattet „ortsübliche Vergütung"
- Klinik-Rechnung: oft erheblich höher als Kassenleistung; Differenz möglicherweise selbst zu tragen
- Kostenvoranschlag anfordern; Vorauszahlung mit Kreditkarte; PKV informieren

### Schritt 5 – Koordination Reisekrankenversicherung
- Reisekrankenversicherung: Lücken der PKV im Ausland schließen (Rücktransport, Hochkostenschutz)
- Keine Doppelerstattung: PKV zahlt zuerst; Reiseschutz als Ergänzung
- Auslandsbehandlungs-Kostenerstattung: Rechnungen im Original; ggf. übersetzen lassen

## Typische Fallen

- **6-Wochen-Grenze**: Nach 6 Wochen im Ausland kann Versicherungsschutz enden; Kasse informieren bei Langzeitaufenthalt.
- **GOÄ-Bindung**: Im Ausland gilt GOÄ nicht; PKV erstattet nur „angemessene" oder „ortsübliche" Kosten.
- **Impfungen vor Reise**: Reiseimpfungen nicht automatisch PKV-Leistung; Tarif prüfen.
- **Zahnbehandlung im Urlaub**: Notfallbehandlung ja; Prothetik oder Zahnersatz im Ausland nein.

## Output-Formate

- Auslandskrankenversicherungs-Checkliste
- PKV-Auskunftsverlangen (Tarifumfang Ausland)
- Kostenerstattungsantrag Auslandsbehandlung
- Rücktransport-Antrag (PKV/Reiseschutz)
- USA-Behandlungskosten-Kalkulation

## Quellen

- [§ 192 VVG – Leistungspflicht PKV](https://www.gesetze-im-internet.de/vvg_2008/__192.html)
- [MB/KK 2009 Auslandsklausel](https://www.pkv.de/service/broschueren/)
- [BGH IV ZR 119/09](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV Ausland – EHIC](https://ec.europa.eu/social/main.jsp?catId=559)
- [dejure.org § 192 VVG](https://dejure.org/gesetze/VVG/192.html)
- [ADAC Auslandskrankenschutz](https://www.adac.de/reise-ziel/auslandsschutz/)
## Hinweis: Kostendeckungslimits und Selbstbehalt

- Viele Tarife begrenzen Rücktransportkosten auf einen Höchstbetrag (z.B. 10.000–30.000 €)
- Selbstbehalt-Tarife: Auslandsleistungen zählen oft gegen den Jahresselbstbehalt
- Zusatzversicherungen (Reisekrankenversicherung) können PKV-Schutz sinnvoll ergänzen
- Im Leistungsfall immer Vorab-Kostenübernahmeerklärung einholen

## Weiterführende Quellen

- [§ 192 VVG – Leistungspflicht PKV](https://www.gesetze-im-internet.de/vvg_2008/__192.html)
- [MB/KK 2009 – Musterbedingungen](https://www.pkv.de/service/rechner-und-services/musterbedingungen/)
- [PKV-Ombudsmann](https://www.pkv-ombudsmann.de)

## 2. `kv-037-abrechnung-goae-goz-und-erstattung`

**Fokus:** Ärztliche (GOÄ) und zahnärztliche (GOZ) Abrechnung: Steigerungsfaktoren, Analogleistungen, Begründungspflichten und Erstattungsansprüche in der PKV und Beihilfe.

# Abrechnung GOÄ/GOZ und Erstattung

## Skill-Zweck

PKV und Beihilfe erstatten ärztliche Honorare nach GOÄ und GOZ. Dieser Skill prüft **Abrechnungsrichtigeit, Steigerungsfaktoren, Analogleistungen und Erstattungsansprüche**.

## Rechtlicher Rahmen

- **GOÄ** (Gebührenordnung für Ärzte) §§ 1–12 + Gebührenverzeichnis
- **GOZ** (Gebührenordnung für Zahnärzte) §§ 1–12 + Gebührenverzeichnis
- **§ 4 GOÄ** – Allgemeine Bestimmungen zu Steigerungsfaktoren (1,0 bis 3,5-fach)
- **§ 6 GOÄ** – Analogleistungen (nicht im Verzeichnis gelistete Leistungen)
- **§ 12 GOÄ** – Rechnungspflichtangaben (fehlende Angaben → Rechnung anfechtbar)
- BGH III ZR 17/18 (GOÄ-Abrechnung, Steigerungsfaktor), BGH III ZR 62/18
- BVerfG 1 BvR 2084/05 (GOÄ und PKV-Erstattung)

## GOÄ-Steigerungsfaktoren

| Faktor | Schwellenwert | Begründungspflicht |
|--------|--------------|-------------------|
| 1,0-fach | Mindestsatz (selten) | Nein |
| 1,8-fach (Regelfall) | Durchschnittliche Schwierigkeit | Nein |
| 2,3-fach | Obergrenze ohne Begründung | Nein |
| > 2,3-fach | Erhöhter Schwellenwert | Ja (auf Rechnung) |
| 3,5-fach | Absolutes Maximum | Ja, ausführlich |

## Prüfprogramm

### Schritt 1 – Rechnungsprüfung formal
- Enthält Rechnung alle Pflichtangaben (§ 12 GOÄ): Datum, Diagnose, Leistungsnummer, Steigerungsfaktor, Begründung bei > 2,3?
- Fehlende Pflichtangaben: Rechnung zurückweisen, neue vollständige Rechnung verlangen
- Digitale Rechnung: muss gleiche Pflichtangaben enthalten

### Schritt 2 – Leistungsverzeichnis prüfen
- Gebührennummer korrekt? GOÄ-Nummernverzeichnis konsultieren
- Doppelabrechnung: GOÄ-Nr. schließt bestimmte andere aus (Ausschlusshinweise im Verzeichnis)
- Zielleistungsprinzip: bei operativen Eingriffen schließen manche Leistungen andere ein (§ 4 Abs. 2a GOÄ)

### Schritt 3 – Steigerungsfaktor prüfen
- > 2,3-fach: Begründung auf Rechnung erforderlich; pauschale Begründungen unzureichend (BGH)
- BGH III ZR 17/18: individuelle Begründung für konkrete Behandlungssituation notwendig
- PKV kann Abzug bei nicht begründetem Faktor vornehmen; Erstattungskürzung

### Schritt 4 – Analogleistungen (§ 6 GOÄ)
- Nicht im Verzeichnis: Abrechnung analog zu ähnlicher Leistung
- Arzt muss in Rechnung kennzeichnen: „analog § 6 GOÄ"
- PKV-Erstattung: PKV prüft ob Analoganwendung plausibel; Ablehnung möglich
- Neue Methoden: oft nur Analogabrechnung möglich bis GOÄ-Reform

### Schritt 5 – Erstattungskürzung durch PKV/Beihilfe
- PKV kürzt: Einzelne Nummern nicht erstattet, Steigerungsfaktor reduziert
- Arzt haftet: keine direkte Haftung gegen PKV; aber Arzt muss Rechnung nicht neu stellen
- Differenz: Versicherter trägt Differenz zwischen Arztrechnung und PKV-Erstattung
- Beihilfe: eigene Erstattungsgrenzen; oft konservativer als PKV

## Typische Fallen

- **Privatarzt-Honorar vor Behandlung**: GOÄ-Honorarvereinbarung schriftlich vor Behandlung; nachträglich unwirksam.
- **IGeL und GOÄ**: IGeL kann nach GOÄ abgerechnet werden; aber Patient muss vorher informiert und einverstanden sein.
- **GOÄ 2024-Reform**: Neue GOÄ in Vorbereitung; Übergangsrecht beachten.
- **Zahnersatz GOZ**: GOZ-Abrechnung für Zahnersatz häufig fehleranfällig; Festzuschuss GKV beachten wenn auch GKV-Mitglied.

## Output-Formate

- GOÄ-Rechnungsprüfungs-Protokoll
- Reklamationsschreiben an Arzt (fehlende Begründung)
- PKV-Erstattungskürzungs-Widerspruch
- Analogleistungs-Überprüfungsanfrage
- GOÄ-Steigerungsfaktor-Begründungs-Checkliste

## Quellen

- [GOÄ – Gebührenordnung Ärzte](https://www.gesetze-im-internet.de/go__1982/)
- [GOZ – Gebührenordnung Zahnärzte](https://www.gesetze-im-internet.de/goz_1988/)
- [§ 12 GOÄ – Rechnungspflicht](https://www.gesetze-im-internet.de/go__1982/__12.html)
- [BGH III ZR 17/18](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [Bundesärztekammer GOÄ](https://www.bundesaerztekammer.de)
- [dejure.org GOÄ](https://dejure.org/gesetze/GO%C3%84)

## 3. `kv-038-heilpraktiker-alternative-medizin-und-tarifbedingungen`

**Fokus:** Erstattung von Heilpraktiker-Behandlungen und alternativer Medizin in PKV und GKV: Tarif­bedingungen, Leistungsumfang, Evidenzanforderungen und Ablehnungsgründe.

# Heilpraktiker, Alternative Medizin und Tarifbedingungen

## Skill-Zweck

Heilpraktiker und alternative Medizin werden zunehmend nachgefragt. Dieser Skill klärt **wann PKV und GKV zahlen**, welche Tarif­bedingungen gelten und wie Ablehnungen angegriffen werden.

## Rechtlicher Rahmen

- **§ 192 VVG i.V.m. Tarifbedingungen** – PKV-Leistungspflicht für Heilpraktikerbehandlungen
- **MB/KK 2009 § 1** – Heilpraktikerbehandlung: nur wenn Tarif einschließt
- **HeilprG** (Heilpraktikergesetz) – Erlaubnis zur Ausübung der Heilkunde
- **§ 2 SGB V** – GKV: Leistungen müssen Qualität und Wirksamkeit entsprechen (keine alternativen Methoden ohne Nachweis)
- **§ 11 Abs. 6 SGB V** – Satzungsleistungen: GKV kann Heilpraktikerleistungen als freiwillige Leistung anbieten
- BGH IV ZR 84/11 (Heilpraktiker PKV, Tarifauslegung), BGH IV ZR 267/14

## PKV vs. GKV bei Alternativer Medizin

| System | Heilpraktiker | Alternative Methoden |
|--------|--------------|---------------------|
| PKV (wenn Tarif) | Erstattungsfähig bis Tarifhöchstbetrag | Akupunktur, Homöopathie etc. wenn tarif­lich |
| GKV (Pflicht) | Grundsätzlich NICHT erstattungsfähig | Nur wenn G-BA-Methode |
| GKV (Satzung) | Ggf. als Satzungsleistung | Kassenabhängig |

## Prüfprogramm

### Schritt 1 – PKV-Tarif prüfen
- Enthält Tarif „Heilpraktikerleistungen"? Welche Methoden? Welches Höchstlimit?
- Typische Formulierung: „Behandlungen durch Heilpraktiker bis max. 500 €/Jahr"
- Ausschlüsse: manche Tarife schließen bestimmte alternative Methoden aus (Homöopathie umstritten)

### Schritt 2 – PKV-Erstattungsvoraussetzungen
- Behandlung durch zugelassenen Heilpraktiker (HeilprG-Erlaubnis)
- Rechnung nach GebüH (Gebührenverzeichnis für Heilpraktiker): Prüfung wie GOÄ
- Medizinische Notwendigkeit: auch bei Heilpraktiker; obwohl Schwelle niedriger als bei Schulmedizin

### Schritt 3 – Evidenzanforderungen (GKV)
- GKV: nur Methoden mit wissenschaftlich erwiesener Wirksamkeit (§ 2 Abs. 1 Satz 3 SGB V)
- G-BA: Akupunktur für Rücken- und Knieschmerzen als GKV-Leistung anerkannt (seit 2007)
- Homöopathie: keine G-BA-Anerkennung; GKV zahlt nur als Satzungsleistung

### Schritt 4 – Ablehnung durch PKV
- PKV lehnt Heilpraktikerrechnung ab: Tarif enthält keine Klausel?
- Oder: Tarif enthält Klausel, aber PKV bestreitet Notwendigkeit oder Zulässigkeit der Methode
- BGH IV ZR 84/11: Tarif muss klar und transparent formuliert sein; Unklarheiten gehen zu Lasten des Versicherers

### Schritt 5 – GKV-Satzungsleistung Heilpraktiker
- Bestimmte Kassen bieten Heilpraktiker-Leistungen als Satzungsleistung an
- Jährlicher Zuschuss, z.B. 200–500 €
- Antrag an Kasse mit Heilpraktiker-Rechnung

## Typische Fallen

- **GebüH-Rechnung falsch**: Heilpraktiker rechnet keine GebüH ab → PKV kann ablehnen; korrekte Abrechnung ist Voraussetzung.
- **Homöopathie und PKV**: Viele PKV schließen Homöopathie nach Beweisstreitigkeiten aus oder limitieren stark.
- **Naturheilkunde vs. Heilpraktiker**: Vertragsarzt kann ebenfalls Akupunktur (Kassenleistung für Rücken) oder Naturheilkunde anbieten.
- **Komplementärmedizin in Klinik**: Wenn stationär verabreicht, PKV-Leistung auch ohne Heilpraktiker-Tarif.

## Output-Formate

- PKV-Tarifprüfungs-Checkliste
- Ablehnungs-Widerspruch (Heilpraktiker)
- GKV-Satzungsleistungsantrag
- GebüH-Rechnungsprüfung
- Tarif-Auslegungsanalyse

## Quellen

- [§ 2 SGB V – Leistungsqualität](https://www.gesetze-im-internet.de/sgb_5/__2.html)
- [HeilprG – Heilpraktikergesetz](https://www.gesetze-im-internet.de/heilprag/)
- [BGH IV ZR 84/11](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [G-BA Akupunktur-Beschluss](https://www.g-ba.de/beschluesse/)
- [MB/KK 2009](https://www.pkv.de/service/broschueren/)
- [dejure.org § 2 SGB V](https://dejure.org/gesetze/SGB_V/2.html)
## Hinweis: Erstattungsgrenzen und Abrechnungspraxis

- Heilpraktikertarife erstatten oft nach Gebührenverzeichnis für Heilpraktiker (GebüH)
- Höchstsatz je Behandlungstag kann gedeckelt sein (z.B. 30–60 € je Sitzung)
- Jahreshöchstgrenzen beachten (z.B. 500–1.000 € p.a.)
- Rechnungen müssen GebüH-Ziffern ausweisen; Pauschalabrechnungen werden oft abgelehnt

## Weiterführende Quellen

- [§ 192 VVG – Leistungspflicht PKV](https://www.gesetze-im-internet.de/vvg_2008/__192.html)
- [Gebührenverzeichnis für Heilpraktiker (GebüH)](https://www.heilpraktiker.org)
- [PKV-Ombudsmann Beschwerdeverfahren](https://www.pkv-ombudsmann.de)
