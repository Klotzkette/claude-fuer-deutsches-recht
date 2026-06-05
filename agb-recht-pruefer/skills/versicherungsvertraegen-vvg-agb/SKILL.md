---
name: versicherungsvertraegen-vvg-agb
description: "Versicherungsvertraegen VVG AGB: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versicherungsvertraegen VVG AGB

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Versicherungsvertraegen VVG AGB** im Plugin AGB-Klausel- und Verbraucherschutzprüfung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `agb-bei-versicherungsvertraegen-vvg` | AGB-Kontrolle bei Versicherungsvertraegen (VVG). Skill behandelt das Spannungsverhaeltnis zwischen den Allgemeinen Versicherungsbedingungen (AVB) und § 307 BGB. Klaert das Transparenzgebot Risikoausschluesse Obliegenheitsverletzungen Sanktion bei Falschangaben Sondervorschriften des VVG. Liefert Pruefraster und Klauselentwurf. |
| `agb-im-konzernverbund` | AGB im Konzernverbund. Skill behandelt die AGB-rechtliche Pruefung von Konzernvereinbarungen Service-Level-Agreements zwischen Mutter und Tochter sowie Standardklauseln bei konzerninternen Vertraegen. Aktuelle Themen: Cash-Pooling Cross-Cluster-Services Konzernverrechnungspreise und § 307 BGB. Liefert Pruefraster. |
| `agb-im-mietrecht-wohnraum-vs-gewerbe` | AGB im Mietrecht: Wohnraum- und Gewerberaummiete. Skill differenziert die AGB-rechtliche Behandlung typischer Mietklauseln Schoenheitsreparaturen Quotenklauseln Endrenovierung Mieterhoehungsvereinbarungen Versetzungsklauseln Anpassungsklauseln. Behandelt die strenge BGH-Linie im Wohnraummietrecht und die weicheren Kontrollen im Gewerberaummietrecht. Liefert Klauselentwurf und Pruefraster. |
| `agb-in-kapitalanlagen-effektenhandel` | AGB im Kapitalanlage- und Effektenhandel. Skill klaert die AGB-rechtliche Pruefung der Allgemeinen Geschaeftsbedingungen fuer Wertpapiergeschaefte (Sonderbedingungen) der Spar- und Tagesgeldbedingungen sowie der Anforderungen aus MiFID II und WpHG. Liefert Pruefraster. |
| `agb-preisanpassung-energie-stromgvv-gasgvv` | AGB-Preisanpassung Energieversorgung StromGVV GasGVV. Skill klaert die rechtlichen Anforderungen an Preisanpassungsklauseln in Energielieferungsvertraegen Grundversorgung (StromGVV GasGVV) und Sonderkundenvertraege. Behandelt EuGH-Linie zur Transparenz BGH-Folgejudikate zur Verfassungsmaessigkeit. Liefert Klauselentwurf und Pruefraster. |

## Arbeitsweg

Im Plugin AGB-Klausel- und Verbraucherschutzprüfung gilt für **Versicherungsvertraegen VVG AGB**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `agb-bei-versicherungsvertraegen-vvg`

**Fokus:** AGB-Kontrolle bei Versicherungsvertraegen (VVG). Skill behandelt das Spannungsverhaeltnis zwischen den Allgemeinen Versicherungsbedingungen (AVB) und § 307 BGB. Klaert das Transparenzgebot Risikoausschluesse Obliegenheitsverletzungen Sanktion bei Falschangaben Sondervorschriften des VVG. Liefert Pruefraster und Klauselentwurf.

# Agb Bei Versicherungsvertraegen Vvg

## Fachkern: Agb Bei Versicherungsvertraegen Vvg

- **Klauselproblem (Agb Bei Versicherungsvertraegen Vvg):** AGB-Kontrolle bei Versicherungsvertraegen (VVG). Skill behandelt das Spannungsverhaeltnis zwischen den Allgemeinen Versicherungsbedingungen (AVB) und § 307 BGB. Klaert das Transparenzgebot Risikoausschluesse Obliegenheitsverletzungen Sanktion bei Falschangaben Sondervorschriften des VVG. Liefert Pruefraster und Klauselentwurf.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Norm

- VVG (Versicherungsvertragsgesetz) als Sondergesetz.
- §§ 305-310 BGB anwendbar, soweit VVG nicht abschliessend regelt.
- BGH-Rechtsprechung zur AGB-Kontrolle von AVB ist umfangreich.

## Typische Problemklauseln

### Risikoausschluss
- Risikoausschluss ist Hauptleistungsbestimmung, keine reine Modalitaetsklausel.
- Inhaltskontrolle nach § 307 BGB nur eingeschraenkt.
- Transparenzgebot § 307 Abs. 1 Satz 2 BGB voll anwendbar.
- BGH IV ZR 76/11: unklar formulierte Risikoausschluesse sind unwirksam.

### Obliegenheitsverletzungen
- § 28 VVG: bei vorsaetzlicher Obliegenheitsverletzung Leistungsfreiheit; bei grober Fahrlaessigkeit Quotelung.
- AGB-Klauseln, die strenger sind als § 28 VVG, sind unwirksam.

### Anpassungsklauseln
- Anpassung der Praemien an Schadensentwicklung wirksam, wenn Berechnungsformel transparent.
- BGH IV ZR 17/02 zur Beitragsanpassung in der PKV.

### Vorvertragliche Anzeigepflicht
- §§ 19 ff. VVG: spezifische Sanktionen.
- AGB-Klauseln zur erweiterten Anzeigepflicht sind regelmaessig unwirksam.

## Pruefraster

1. Welche AVB-Klausel ist im Streit?
2. Risikoausschluss oder Modalitaet?
3. Transparenzgebot erfuellt?
4. VVG-Spezialnorm vorrangig?
5. BGH-Linie konsultieren.

## Output

- Memo zur AVB-Klausel.
- Klauselentwurf.

## 2. `agb-im-konzernverbund`

**Fokus:** AGB im Konzernverbund. Skill behandelt die AGB-rechtliche Pruefung von Konzernvereinbarungen Service-Level-Agreements zwischen Mutter und Tochter sowie Standardklauseln bei konzerninternen Vertraegen. Aktuelle Themen: Cash-Pooling Cross-Cluster-Services Konzernverrechnungspreise und § 307 BGB. Liefert Pruefraster.

# Agb Im Konzernverbund

## Fachkern: Agb Im Konzernverbund

- **Klauselproblem (Agb Im Konzernverbund):** Cash-Pooling Cross-Cluster-Services Konzernverrechnungspreise und § 307 BGB. Liefert Pruefraster.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Norm

- § 305 Abs. 1 BGB: AGB-Eigenschaft setzt Stellung fuer "Vielzahl von Vertraegen" voraus.
- In Konzernvertraegen oft vorformuliert, aber individuell ausgehandelt.
- § 310 Abs. 1 BGB: B2B-Wertungen.

## Typische Konzernklauseln

### Service-Level-Agreements (SLA)
- Standardisierte Leistungsbeschreibungen mit Sanktionen bei Nichterfuellung.
- AGB-rechtliche Pruefung der Haftungsbegrenzung.

### Cash-Pooling-Vereinbarungen
- BGH II ZR 102/07 zu Cash-Pool-Risiken.
- Haftungsausschluesse muessen § 307 BGB standhalten.

### Konzernverrechnungspreise
- Steuerlich Transferpreise nach OECD-RL.
- AGB-rechtlich Transparenzgebot.

### Cross-Cluster-Services
- Vertraege zwischen verschiedenen Konzernteilen ueber gemeinsame Dienstleistungen (IT, HR, Finance).
- Standardisierung typisch — § 305 BGB greift.

## Pruefraster

1. Vorformulierung fuer Vielzahl von Vertraegen?
2. Individuell ausgehandelt?
3. § 307 BGB-Risiko?
4. Steuerliche und kartellrechtliche Wechselwirkung?

## Output

- Klauselraster.
- Memo zur konzerninternen AGB-Gestaltung.

## 3. `agb-im-mietrecht-wohnraum-vs-gewerbe`

**Fokus:** AGB im Mietrecht: Wohnraum- und Gewerberaummiete. Skill differenziert die AGB-rechtliche Behandlung typischer Mietklauseln Schoenheitsreparaturen Quotenklauseln Endrenovierung Mieterhoehungsvereinbarungen Versetzungsklauseln Anpassungsklauseln. Behandelt die strenge BGH-Linie im Wohnraummietrecht und die weicheren Kontrollen im Gewerberaummietrecht. Liefert Klauselentwurf und Pruefraster.

# Agb Im Mietrecht Wohnraum Vs Gewerbe

## Fachkern: Agb Im Mietrecht Wohnraum Vs Gewerbe

- **Klauselproblem (Agb Im Mietrecht Wohnraum Vs Gewerbe):** Wohnraum- und Gewerberaummiete. Skill differenziert die AGB-rechtliche Behandlung typischer Mietklauseln Schoenheitsreparaturen Quotenklauseln Endrenovierung Mieterhoehungsvereinbarungen Versetzungsklauseln Anpassungsklauseln. Behandelt die strenge BGH-Linie im Wohnraummietrecht und die weicheren Kontrollen im Gewerberaummietrecht. Liefert Klauselentwurf und Pruefraster.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Wohnraummietrecht

### Schoenheitsreparaturen
- BGH VIII ZR 196/06 und Folgejudikate: starre Fristenplaene unwirksam.
- "Quotenabgeltungsklausel" generell unwirksam — BGH VIII ZR 242/13.
- "Endrenovierungsklausel" unwirksam — BGH VIII ZR 178/13.

### Mieterhoehung
- Klauseln, die einseitige Mieterhoehung ohne gesetzliche Voraussetzungen erlauben, sind unwirksam (§ 558 BGB als Maximalrahmen).
- Indexmiete (§ 557b BGB) wirksam, wenn ordnungsgemaess vereinbart.
- Staffelmiete (§ 557a BGB) zulaessig.

### Modernisierungszuschlag
- § 559 BGB: 8 Prozent der Modernisierungskosten p.a., Kappungsgrenze.
- AGB-Klauseln, die diese Grenze ueberschreiten, sind unwirksam.

### Kaution
- § 551 BGB: maximal 3 Nettomonatsmieten, separat anzulegen.
- AGB-Klauseln zur Hoehe oder zur Anlage gegen § 551 BGB sind unwirksam.

## Gewerberaummietrecht

- § 310 Abs. 1 BGB: § 308/309 BGB grundsaetzlich nicht direkt anwendbar.
- § 307 BGB als Massstab.
- Schoenheitsreparaturen in Gewerbe-AGB grundsaetzlich uebertragbar — BGH XII ZR 168/15.
- Indexierungsklauseln im Gewerbe zulaessig, soweit angemessen.
- Konkurrenzschutzklauseln zulaessig.

## Versetzungsklauseln

- Wohnraum: keine, nicht erforderlich.
- Gewerbe: Filialmietvertraege bei Konzernen — Recht zur Verlagerung intern.

## Pruefraster

1. Wohnraum oder Gewerbe?
2. Welche Klausel konkret?
3. BGH-Linie aktuell?
4. § 558-559 BGB-Grenze?
5. Lebenszyklusfrage (Beginn / Verlauf / Ende der Miete)?

## Output

- Klauselraster Wohnraum vs. Gewerbe.
- Schriftsatzbaustein.

## 4. `agb-in-kapitalanlagen-effektenhandel`

**Fokus:** AGB im Kapitalanlage- und Effektenhandel. Skill klaert die AGB-rechtliche Pruefung der Allgemeinen Geschaeftsbedingungen fuer Wertpapiergeschaefte (Sonderbedingungen) der Spar- und Tagesgeldbedingungen sowie der Anforderungen aus MiFID II und WpHG. Liefert Pruefraster.

# Agb In Kapitalanlagen Effektenhandel

## Aufgabe

Prüfe Sonderbedingungen für Wertpapiergeschäfte, Depot-/Broker-AGB, Spar-/Tagesgeldbedingungen und digitale Trading-AGB so, dass AGB-Recht, WpHG/MiFID-II-Pflichten und tatsächlicher Orderprozess zusammenpassen.

## Norm

- BGB §§ 305 bis 310, insbesondere Transparenz, Änderungsklauseln, Haftungsbegrenzung, Entgeltklauseln und einseitige Leistungsbestimmung.
- WpHG, MiFID II/MiFIR und Delegierte Rechtsakte für Geeignetheit, Angemessenheit, Best Execution, Kostentransparenz und Zuwendungen.
- BGB §§ 675c ff. nur bei Zahlungsdienste-/Kontoschnittstellen; DepotG/KWG/BaFin-Hinweise je nach Produkt und Anbieterrolle.
- Rechtsprechung zu Bankentgelten/Änderungsklauseln nur mit Gericht, Datum, Aktenzeichen und freier Quelle zitieren.

## Standardbedingungen

- Sonderbedingungen fuer Wertpapiergeschaefte Stand 01.01.2024.
- AGB der DZ Bank, Sparkassen, Privatbanken.

## Klauseltypen

### Anlageberatung
- Pflicht zur Geeignetheitspruefung (§ 64 WpHG).
- Geeignetheitserklaerung schriftlich.
- AGB dürfen Beratungs-/Dokumentationspflichten nicht durch pauschale "Kunde entscheidet allein"-Formeln entleeren.

### Beratungsfreies Geschaeft
- Sondervorschriften fuer Execution-Only.
- Product Governance, Zielmarkt, Warnhinweise und Kenntnisse/Erfahrungen sauber vom Beratungsverzicht trennen.

### Ausfuehrungsbedingungen
- Best Execution (§ 82 WpHG).
- Ausführungsplätze, Weisungen, Teilausführungen, Handelsaussetzungen, Systemausfälle und Orderstreichungen konkret regeln.

### Provisionen und Zuwendungen
- Offenlegungspflichten (§§ 70 WpHG).
- Retrozessionen, Kickbacks, Payment for Order Flow und Konzerninteressen als Transparenz- und Interessenkonfliktthema behandeln.

## Pruefraster

1. Anlageberatung oder beratungsfrei?
2. Geeignetheitsdokumentation?
3. Provisionsoffenlegung?
4. AGB-Inhaltskontrolle?
5. Orderprozess und App-Oberfläche identisch mit Klausellogik?
6. Haftungsbegrenzung bei Systemausfall, Marktdatenfehler oder Handelsstopp wirksam?
7. Produktfreigabe/Zielmarkt für komplexe Produkte dokumentiert?

## Output

- Klauselraster mit AGB-Risiko, WpHG-Pflicht, Prozessschritt, Kundendisclosure, Beleg und Änderungsvorschlag.
- Schriftsatz-/Abhilfebaustein für Bank, Broker, Verbraucher oder Rechtsabteilung.

## 5. `agb-preisanpassung-energie-stromgvv-gasgvv`

**Fokus:** AGB-Preisanpassung Energieversorgung StromGVV GasGVV. Skill klaert die rechtlichen Anforderungen an Preisanpassungsklauseln in Energielieferungsvertraegen Grundversorgung (StromGVV GasGVV) und Sonderkundenvertraege. Behandelt EuGH-Linie zur Transparenz BGH-Folgejudikate zur Verfassungsmaessigkeit. Liefert Klauselentwurf und Pruefraster.

# Agb Preisanpassung Energie Stromgvv Gasgvv

## Fachkern: Agb Preisanpassung Energie Stromgvv Gasgvv

- **Klauselproblem (Agb Preisanpassung Energie Stromgvv Gasgvv):** AGB-Preisanpassung Energieversorgung StromGVV GasGVV. Skill klaert die rechtlichen Anforderungen an Preisanpassungsklauseln in Energielieferungsvertraegen Grundversorgung (StromGVV GasGVV) und Sonderkundenvertraege. Behandelt EuGH-Linie zur Transparenz BGH-Folgejudikate zur Verfassungsmaessigkeit. Liefert Klauselentwurf und Pruefraster.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Norm

- StromGVV und GasGVV: Grundversorgungs-Verordnungen.
- § 41 EnWG.
- §§ 305-310 BGB AGB-Recht.

## EuGH-Linie

- EuGH C-92/11 (Schulz / Egbringhoff): Preisanpassung in Energiegrundversorgung muss transparent sein; einfache Bezugnahme auf gesetzliche Tarifaenderungen unzureichend.

## BGH-Folgejudikate

- BGH VIII ZR 178/08 zu unwirksamer Preisanpassung.
- BGH VIII ZR 244/10 zur Folgeanalyse.
- BGH VIII ZR 295/13 zur Grundversorgung.

## Anforderungen

- Konkrete Berechnungsformel.
- Anpassungstrigger (Kostenbestandteile aus EnWG, EEG, KWKG).
- Kuendigungsrecht des Kunden.
- Vorabhinweis mit Frist (typischerweise 6 Wochen).

## Pruefraster

1. Grundversorgung oder Sonderkundenvertrag?
2. Klausel transparent?
3. Kostenbestandteile getrennt aufgelistet?
4. Kuendigungsrecht?
5. EuGH-Linie eingehalten?

## Output

- Klauselentwurf.
- Schriftsatzbaustein Rueckforderung.
