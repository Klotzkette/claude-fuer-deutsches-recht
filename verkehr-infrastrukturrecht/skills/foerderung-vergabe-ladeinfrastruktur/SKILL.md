---
name: foerderung-vergabe-ladeinfrastruktur
description: "Foerderung Vergabe Ladeinfrastruktur: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Foerderung Vergabe Ladeinfrastruktur

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Foerderung Vergabe Ladeinfrastruktur** im Plugin Verkehr-/Infrastrukturrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehr-infrastrukturrecht-foerderung-vergabe` | Foerderrecht und Vergabe für Verkehrsinfrastruktur-Projekte: Kommune oder Vorhabentraeger beantragt GVFG-Mittel oder schreibt öffentlichen Auftrag aus. Normen: GVFG (Bundesanteil und Laenderanteil), BHO §§ 23 und 44 (Zuwendungsrecht), GWB §§ 97 ff., VgV, UVgO (Vergaberecht). Prüfraster: Foerderfähigkeit nach BVWP, EU-Schwellenwerte, Ruegepflicht § 160 GWB, Vergabekammer, Zuwendungsbescheid Nebenbestimmungen, Zweckbindungsfristen. Output Foerderantrag-Prüfung, Vergabe-Kurzgutachten. Abgrenzung: Planfeststellung Bau siehe verkehr-infrastrukturrecht-planfeststellung; Vergaberecht detail siehe fachanwalt-vergaberecht-Plugin. |
| `verkehr-infrastrukturrecht-ladeinfrastruktur` | Ladeinfrastruktur für Elektromobilitaet rechtlich begleiten: Betreiber plant Ladepunkte oder Netzanschluss wird verweigert. Normen: AFIR-VO (EU) 2023/1804 (Mindestanforderungen Ladeinfrastruktur), Ladesaeulenverordnung LSV, § 8 EnWG (Netzanschlusspflicht), LBO (Genehmigungspflicht). Prüfraster: Genehmigungspflichten LBO, Netzanschlusspflicht EnWG, Betreibermodelle öffentliche/private Flaechen, Foerderung BAFA/KfW, WEG/Mietrecht. Output Rechts-Memo Genehmigungsweg, Netzanschluss-Anspruch, Foerder-Check. Abgrenzung: Planfeststellung Energietrassen siehe energietrassen-planfeststellung-rechtsschutz; Vergabe siehe verkehr-infrastrukturrecht-foerderung-vergabe. |
| `verkehr-infrastrukturrecht-planfeststellung` | Planfeststellung für Strassenbau, Schienenstrecken und OEPNV-Infrastruktur begleiten oder anfechten: Vorhabentraeger benoetigt Planfeststellungsbeschluss oder Anlieger klagt dagegen. Normen: § 17 FStrG (Bundesstrasse), § 18 AEG (Eisenbahn), § 28 PBefG (Strassenbahn), § 17 VwVfG (Abwaegungsgebot), BVerwG-Rspr Abwaegungsfehler. Prüfraster: Einwendungsfristen, Eroerrterungstermin, Klagebefugnis § 42 Abs. 2 VwGO, UmwRG-Verbandsklage, Eilrechtsschutz. Output Einwendungsschrift oder Klageschrift-Entwurf. Abgrenzung: Normenkontrolle Bauleitplan siehe normenkontrolle-bauleitplanung-Plugin; Energietrassen siehe energietrassen-planfeststellung-rechtsschutz. |

## Arbeitsweg

Im Plugin Verkehr-/Infrastrukturrecht gilt für **Foerderung Vergabe Ladeinfrastruktur**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehr-infrastrukturrecht-foerderung-vergabe`

**Fokus:** Foerderrecht und Vergabe für Verkehrsinfrastruktur-Projekte: Kommune oder Vorhabentraeger beantragt GVFG-Mittel oder schreibt öffentlichen Auftrag aus. Normen: GVFG (Bundesanteil und Laenderanteil), BHO §§ 23 und 44 (Zuwendungsrecht), GWB §§ 97 ff., VgV, UVgO (Vergaberecht). Prüfraster: Foerderfähigkeit nach BVWP, EU-Schwellenwerte, Ruegepflicht § 160 GWB, Vergabekammer, Zuwendungsbescheid Nebenbestimmungen, Zweckbindungsfristen. Output Foerderantrag-Prüfung, Vergabe-Kurzgutachten. Abgrenzung: Planfeststellung Bau siehe verkehr-infrastrukturrecht-planfeststellung; Vergaberecht detail siehe fachanwalt-vergaberecht-Plugin.

# Foerderrecht und Vergabe — Verkehrsinfrastruktur

## Triage zu Beginn

1. **Foerderung oder Vergabe?** — Foerderrecht: Zuwendungsbescheid nach GVFG/LStrG/BVWP; Vergaberecht: Ausschreibung und Zuschlag bei oeffentlichen Auftraggebern.
2. **EU-Schwellenwert ueberschritten?** — Vergabe: EU-weit ab 5.382.000 EUR (Bauleistungen 2024), 221.000 EUR (Liefer-/Dienstleistungen Kommunen), 143.000 EUR (Bundesbehörden) — beeinflusst welches Vergaberecht gilt.
3. **Ruegefrist nach § 160 GWB beachtet?** — Ruege muss unverzueglich nach Erkennbarkeit des Verstosses bei dem Auftraggeber eingelegt werden; Praeklusion!
4. **Zweckbindungsfrist?** — GVFG-gefoerderte Anlagen typischerweise 25 Jahre Zweckbindung; vorzeitige Aenderung erfordert Zustimmung.
5. **Widerspruch gegen Zuwendungsbescheid?** — Nebenbestimmungen, Auflagen, Abruf-Fristen pruefen.

## Zentrale Normen

- **§ 3 GVFG** — Foerderung von Nahverkehrsinfrastruktur; Bundesmittel
- **§§ 23, 44 BHO** — Allgemeines Zuwendungsrecht des Bundes; Nebenbestimmungen
- **§§ 97 ff. GWB** — Vergaberecht; Grundsaetze des Vergabeverfahrens
- **§§ 106 ff. GWB** — Schwellenwerte
- **§ 160 GWB** — Nachpruefungsverfahren Vergabekammer; Ruegepflicht
- **§ 169 GWB** — Zuschlagsverbot nach Ruege
- **§§ 1 ff. VgV** — Vergabeverordnung; Verfahrensarten
- **§§ 1 ff. UVgO** — Unterschwellenvergabeordnung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Vergabe

1. **Schwellenwert pruefen:** EU-weite Ausschreibung oder national?
2. **Vergabebekanntmachung analysieren:** Eignungskriterien, Zuschlagskriterien, Fristen.
3. **Angebot oder Ruege?** — Wenn Ausschreibungsfehler erkennbar: Ruege sofort (§ 160 Abs. 3 GWB — "unverzueglich").
4. **Zuschlag-Vorab-Information (§ 134 GWB):** 15 Tage Wartefrist vor Zuschlag.
5. **Nachpruefungsantrag:** Vergabekammer beim Bundeskartellamt (EU-Schwellenwert) oder Landesvergabebehoerde.
6. **Beschwerde OLG:** gegen Entscheidung der Vergabekammer.

## Schritt-fuer-Schritt-Foerderung

1. **Foerderantrag pruefen:** Vollstaendigkeit, Fristen, Nachweise.
2. **Zuwendungsbescheid erhalten:** Nebenbestimmungen pruefen (Auflagen, Bedingungen, Widerrufsvorbehalt).
3. **Zweckbindungsfrist dokumentieren:** Foerdergegenstand definieren und schriftlich festhalten.
4. **Verwendungsnachweis rechtzeitig einreichen:** GVFG-Fristen beachten.
5. **Bei Rueckforderung:** Anhoerung, Widerspruch, Verwaltungsgerichtsklage.

## Harte Leitplanken

- Vergaberechtliche Ruege muss "unverzueglich" sein — nie laenger als 7-10 Tage nach Kenntnisnahme warten.
- Zuwendungsrecht: Zweckbindungsfristen genau dokumentieren, vorzeitige Nutzungsaenderungen genehmigen lassen.
- EU-Schwellenwerte regelmaessig aktualisieren (alle 2 Jahre neue EU-Verordnung).
- Anwaltliche Endkontrolle bei Ruge und Nachpruefungsantrag.

## 2. `verkehr-infrastrukturrecht-ladeinfrastruktur`

**Fokus:** Ladeinfrastruktur für Elektromobilitaet rechtlich begleiten: Betreiber plant Ladepunkte oder Netzanschluss wird verweigert. Normen: AFIR-VO (EU) 2023/1804 (Mindestanforderungen Ladeinfrastruktur), Ladesaeulenverordnung LSV, § 8 EnWG (Netzanschlusspflicht), LBO (Genehmigungspflicht). Prüfraster: Genehmigungspflichten LBO, Netzanschlusspflicht EnWG, Betreibermodelle öffentliche/private Flaechen, Foerderung BAFA/KfW, WEG/Mietrecht. Output Rechts-Memo Genehmigungsweg, Netzanschluss-Anspruch, Foerder-Check. Abgrenzung: Planfeststellung Energietrassen siehe energietrassen-planfeststellung-rechtsschutz; Vergabe siehe verkehr-infrastrukturrecht-foerderung-vergabe.

# Ladeinfrastruktur Elektromobilitaet

## Triage zu Beginn

1. **Oeffentliche oder private Ladeinfrastruktur?** — Oeffentlich zugaenglich (§ 2 Nr. 5 AFIR-VO): Pflichten zur Interoperabilitaet, ad-hoc-Laden, Preistransparenz; Private: Hausanschluss, WEG-Zustimmung.
2. **Standort?** — Privatgrundstuck, oeffentliche Verkehrsflaeche (Sondernutzung!), Parkhaus.
3. **Genehmigungspflicht nach Baurecht?** — Ladesaeulen an Gebaeuden oft genehmigungsfrei; grössere Anlagen oder bauliche Aenderungen koennen LBO-pflichtig sein.
4. **Netzanschlusspflicht des Netzbetreibers?** — § 8 EnWG: Anschlusspflicht des Netzbetreibers; Verweigerung nur aus tatsaechlichen oder rechtlichen Gruenden (Kapazitaet, Sicherheit).
5. **Foerderung moeglich?** — BAFA-Foerderung fuer Ladeinfrastruktur (Programme regelmaessig aktualisiert); KfW 439.

## Zentrale Normen

- **AFIR-VO (EU) 2023/1804** — Verordnung zum Aufbau alternativer Kraftstoffinfrastruktur; ab 13.04.2024 unmittelbar anwendbar
- **§ 2 LSV** — Ladesaeulenverordnung: Anforderungen an oeffentlich zugaengliche Ladepunkte
- **§ 8 EnWG** — Netzanschlusspflicht des Netzbetreibers; Anschluss und Zugang
- **§ 9a GEG** — Neubau und wesentliche Renovierung: Ladeinfrastruktur-Anforderungen
- **§ 20 WEG** — Bauliche Veraenderung; Ladesaeule auf WEG-Gemeinschaftseigentum erfordert Zustimmung oder Mehrheitsbeschluss
- **§ 554 BGB** — Mietrecht: Mieter hat Anspruch auf Zustimmung des Vermieters zur Ladestation (n.F. seit 01.12.2020)
- **§ 13 FStrG** — Sondernutzung an Bundesstrassen fuer Ladesaeulen

## Aktuelle Rechtsprechung

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Ladeinfrastruktur

```
Standort der Ladeinfrastruktur?
├─ Privates Einzelhausgrundstuck
│ ├─ Eigentuemerfall → direkt anschliessen (nur Netzanschluss § 8 EnWG)
│ └─ Mieterfall → § 554 BGB-Antrag an Vermieter
├─ WEG-Gemeinschaftseigentum
│ └─ § 20 WEG-Antrag auf Beschluss oder Zustimmung aller
├─ Oeffentliche Strassenflaeche
│ └─ Sondernutzungserlaubnis (§ 13 FStrG / LStrG)
└─ Gewerbliche Anlage (Parkhaus, Shopping-Center)
 ├─ Baurecht pruefen (LBO-Genehmigungspflicht?)
 ├─ AFIR-Pflichten (oeffentlich zugaenglich?)
 └─ Foerderung BAFA/KfW beantragen
```

## Harte Leitplanken

- AFIR-VO seit April 2024 unmittelbar anwendbar — EU-Recht prufen.
- Sondernutzungserlaubnis fuer oeffentliche Flaechen niemals vergessen.
- WEG-Beschluss sorgfaeltig dokumentieren.
- Anwaltliche Endkontrolle bei komplexen Konstellationen.

## 3. `verkehr-infrastrukturrecht-planfeststellung`

**Fokus:** Planfeststellung für Strassenbau, Schienenstrecken und OEPNV-Infrastruktur begleiten oder anfechten: Vorhabentraeger benoetigt Planfeststellungsbeschluss oder Anlieger klagt dagegen. Normen: § 17 FStrG (Bundesstrasse), § 18 AEG (Eisenbahn), § 28 PBefG (Strassenbahn), § 17 VwVfG (Abwaegungsgebot), BVerwG-Rspr Abwaegungsfehler. Prüfraster: Einwendungsfristen, Eroerrterungstermin, Klagebefugnis § 42 Abs. 2 VwGO, UmwRG-Verbandsklage, Eilrechtsschutz. Output Einwendungsschrift oder Klageschrift-Entwurf. Abgrenzung: Normenkontrolle Bauleitplan siehe normenkontrolle-bauleitplanung-Plugin; Energietrassen siehe energietrassen-planfeststellung-rechtsschutz.

# Planfeststellung und Plangenehmigung — Verkehrsinfrastruktur

## Triage zu Beginn

1. **Welcher Infrastrukturtraeger?** — Bundesstrasse (§ 17 FStrG), Landesstrasse (LStrG), Schiene (§ 18 AEG), Strassenbahn (§ 28 PBefG), Wasserstrasse (§ 14 WaStrG)?
2. **Welche Rolle hat der Mandant?** — Vorhabentraeger, betroffener Grundeigentuemer, anerkannter Umweltverband, kommunale Koerperschaft?
3. **Phase des Verfahrens?** — Linienplanung, Planfeststellung, Genehmigung, Oeffentlichkeitsbeteiligung, Eroerrterungstermin, Entscheidung, Klage?
4. **Einwendungsfristen?** — § 17a FStrG i.V.m. § 73 VwVfG: 6 Wochen nach Bekanntmachung der Auslegung.
5. **Ausschlusswirkung nicht vergessen!** — § 73 Abs. 4 Satz 3 VwVfG: nicht fristgerecht erhobene Einwendungen sind ausgeschlossen (Praeklusion).
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 17 FStrG** — Planfeststellung fuer Bundesfernstrassen
- **§ 18 AEG** — Planfeststellung fuer Schienenverkehr
- **§ 28 PBefG** — Planfeststellung fuer Strassenbahnlinien
- **§ 73 VwVfG** — Verfahren der Planfeststellung; Beteiligung der Behoerden und der Oeffentlichkeit
- **§ 74 VwVfG** — Planfeststellungsbeschluss; Bestandskraft; Nebenbestimmungen
- **§ 75 VwVfG** — Rechtswirkungen des Planfeststellungsbeschlusses; Konzentrationswirkung
- **§ 17 Abs. 1 Satz 2 VwVfG** — Abwaegungsgebot
- **§ 42 Abs. 2 VwGO** — Klagebefugnis; subjektive Rechte
- **§ 2 UmwRG** — Klagebefugnis anerkannter Umweltverbaende

## Aktuelle Rechtsprechung (Stand 05/2026, verifiziert bverwg.de)

- **BVerwG 23.06.2020, 9 A 22.19** (A 49 Mittelhessen): Klimaschutz und Klimawandelfolgen sind in der Abwaegung zu beruecksichtigen; Planfeststellungsbeschluss aufgehoben. Quelle: bverwg.de — Pressemitteilung 41/2020.
- **BVerwG 04.05.2022, 9 A 7.21** (A 14): UVP-Anforderungen; sektorale Klimaschutzpruefung. Quelle: bverwg.de.
- **BVerwG 11.10.2017, 9 A 14.16** (A 33): Planergaenzungsverfahren bei Heilung von Abwaegungsfehlern; Massstab fuer "fehlerhafte Abwaegung". Quelle: bverwg.de.
- **BVerwG 09.02.2017, 7 A 2.15** (Elbvertiefung): Anforderungen an FFH-Vertraeglichkeitspruefung. Quelle: bverwg.de.
- **EuGH 28.05.2020, C-535/18** (IL u.a.): UVP-Richtlinie 2011/92/EU; oeffentliche Beteiligung; sektoraler Schutz. Quelle: curia.europa.eu.

**Gesetzeslage 2026:** LNG-Beschleunigungsgesetz und Planungsbeschleunigungsgesetze (Genehmigungsbeschleunigungsgesetz Energie BGBl. I 2023 S. 1565); Wind-an-Land-Gesetz (BGBl. I 2022 S. 1353); Solarpaket I (BGBl. I 2024). Vor Mandatsanwendung aktuellen Stand pruefen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Mandantenrolle klaeren:** Vorhabentraeger, Betroffener, Verband — unterschiedliche Rechte und Pflichten.
2. **Fristen pruefen:** Auslegungsfrist (§ 73 Abs. 2 VwVfG); Einwendungsfrist 6 Wochen (§ 73 Abs. 4 VwVfG).
3. **Einwendung formulieren:** Konkrete betroffene Belange (Laerm, Eigentumseingriff, Wertminderung, Artenschutz); ohne Praeklusion riskieren.
4. **Eroerrterungstermin vorbereiten:** § 73 Abs. 6 VwVfG; muendliche Vertiefung der Einwendungen.
5. **Planfeststellungsbeschluss erhalten und prufen:** Abwaegungsfehler? Nebenbestimmungen korrekt?
6. **Rechtsbehelfe:** Widerspruch (wenn statthaft) → Anfechtungsklage BVerwG (§ 50 VwGO) oder OVG.

## Entscheidungsbaum Rechtsschutz

```
Planfeststellungsbeschluss erlassen?
├─ Eigentuemerin/Eigentuemer unmittelbar betroffen?
│ ├─ § 14 GG-Verletzung geltend machen
│ └─ Anfechtungsklage beim OVG / BVerwG
├─ Kommunale Koerperschaft?
│ └─ Art. 28 Abs. 2 GG (Gemeindeautonomie) als Klagebefugnis
├─ Anerkannter Umweltverband (§ 3 UmwRG)?
│ └─ § 2 UmwRG-Klage ohne subjektive Rechtsverletzung
└─ Sonstiger Betroffener?
 └─ Klagebefugnis nach § 42 Abs. 2 VwGO; subjektive Rechtsverletzung geltend machen
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Einwendungsschreiben gegen Planfeststellungsbeschluss | Einwendung nach Schema; Template unten |
| Variante A — Einwendungsfrist bereits abgelaufen Praeklusion | Nachholung der Einwendung nicht moeglich; andere Rechtsmittel pruefen |
| Variante B — Mandant ist Traeger oeffentlicher Belange | Einwendung als ToEB; anderes Gewicht und Verfahren |
| Variante C — Planfeststellung hat UVP-Fehler | UVP-Fehler-Ruege als staerkster Angriffspunkt |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Einwendungsschreiben

```
An die Planfeststellungsbehoerde [ORT]
Az.: [AKTENZEICHEN DES PLANFESTSTELLUNGSVERFAHRENS]

Einwendung gegen den Planfeststellungsantrag
[PROJEKTBEZEICHNUNG]

Ich/Wir [Name, Adresse] erheben folgende Einwendungen:

1. Eigentumseingriff: Das Vorhabenflaeche [FlSt. Nr.] tangiert
 unser Eigentumsrecht nach Art. 14 GG. [Begruendung]

2. Laermbeeintraechtigung: Die prognostizierten Laermwerte
 ueberschreiten [X] dB(A) und liegen ueber den zulaeassigen
 Grenzwerten der 16. BImSchV.

3. [Weiterer Aspekt]

Wir beantragen: [Planänderung / Auflagen / Entschaedigung].

[NAME] [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Harte Leitplanken

- Einwendungsfrist 6 Wochen streng beachten — Praeklusion ist absolut.
- Einwendungen muessen konkret und auf eigene Betroffenheit bezogen sein.
- Klagebefugnis nach § 42 Abs. 2 VwGO muss sorgfaeltig begruendet werden.
- Anwaltliche Endkontrolle bei allen Fristen und Einwendungen.
