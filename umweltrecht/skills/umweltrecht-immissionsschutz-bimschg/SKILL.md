---
name: umweltrecht-immissionsschutz-bimschg
description: "Immissionsschutz Bimschg: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Immissionsschutz Bimschg

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Immissionsschutz Bimschg** im Plugin Umweltrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `umweltrecht-immissionsschutz-bimschg` | Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot. Prüfraster Genehmigungspflicht UVP-Pflicht Drittschutz Nachbarklage Verbandsklage UmwRG. Output Genehmigungsantrag-Struktur Schriftsatz OVG. Abgrenzung zu umweltrecht-naturschutz-artenschutz (Naturschutz) und umweltrecht-stoerfall-anlagen (Stoerfall). |
| `umweltrecht-kommandocenter` | Umweltmandat-Einstieg: Intake Anlagenkarte Behoerdenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster Mandanten-Typ-Identifikation Sachgebiets-Routing Triage-Matrix. Output Mandat-Karte Routing-Empfehlung Naechste-Schritte-Plan. Abgrenzung zu allen Fach-Skills (nur Master-Routing). |
| `umweltrecht-naturschutz-artenschutz` | Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL 92/43/EWG Vogelschutz-RL. Prüfraster Eingriffs-Ausgleichs-Regelung saP-Gutachten FFH-Vertraeglichkeit Verbandsklagebefugnis. Output Artenschutz-Prüfung Kompensationskonzept. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (Anlagengenehmigung) und umweltrecht-verfahren (Klage). |

## Arbeitsweg

Im Plugin Umweltrecht gilt für **Immissionsschutz Bimschg**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `umweltrecht-immissionsschutz-bimschg`

**Fokus:** Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot. Prüfraster Genehmigungspflicht UVP-Pflicht Drittschutz Nachbarklage Verbandsklage UmwRG. Output Genehmigungsantrag-Struktur Schriftsatz OVG. Abgrenzung zu umweltrecht-naturschutz-artenschutz (Naturschutz) und umweltrecht-stoerfall-anlagen (Stoerfall).

# Immissionsschutz und BImSchG

## Triage — klaere vor Verfahrens-Einstieg

1. Welche Anlage (Typ, installierte Leistung, Emissionspotenzial) — Spalte 1 oder 2 der 4. BImSchV?
2. Formelles (§ 10 BImSchG, mit Oeffentlichkeitsbeteiligung) oder vereinfachtes Verfahren (§ 19 BImSchG)?
3. Ist eine UVP-Pflicht gemaess UVPG-Anlage 1 ausgeloest?
4. Wer ist Mandant — Betreiber/Investor oder klagender Dritter (Nachbar, Umweltverband)?
5. Liegt ein Ausgangsbescheid vor oder steht Antrag am Anfang?
6. Welche Fristen laufen (Widerspruch § 70 VwGO, Klage § 74 VwGO je 1 Monat)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 4 BImSchG** — Genehmigungspflicht fuer Anlagen der 4. BImSchV
- **§ 5 Abs. 1 Nr. 1 BImSchG** — Betreiberpflicht Schutz vor schaedlichen Umwelteinwirkungen (Drittschutz-Norm)
- **§ 5 Abs. 1 Nr. 2 BImSchG** — Vorsorge-Pflicht Emissionsminimierung
- **§ 6 BImSchG** — Genehmigungsvoraussetzungen; gebundene Entscheidung
- **§ 10 BImSchG i.V.m. 9. BImSchV** — Foermliches Verfahren mit Oeffentlichkeitsbeteiligung
- **§ 16 BImSchG** — Wesentliche Aenderung genehmigungsbeduerftiger Anlagen
- **§ 17 BImSchG** — Nachtraegliche Auflagen
- **§ 19 BImSchG** — Vereinfachtes Verfahren ohne Oeffentlichkeitsbeteiligung
- **§ 48 BImSchG i.V.m. TA Luft, TA Laerm** — Verwaltungsvorschriften als antizipierte Sachverstaendigen-Gutachten
- **§ 1 UmwRG** — Klagebefugnis anerkannter Umweltvereinigungen
- **§ 113 Abs. 1 VwGO** — Aufhebungsklage gegen Genehmigung

## Leitentscheidungen (Stand 05/2026, verifiziert bverwg.de / curia.europa.eu)

- **BVerwG 17.12.2020, 4 C 5.19**: BImSchG-Genehmigung Windkraftanlage; Anforderungen an artenschutzrechtliche Pruefung (saP). Quelle: bverwg.de.
- **BVerwG 18.07.2019, 7 C 26.17**: UVP-Vorpruefung; Aufhebung nur bei kausalen Verfahrensmaengeln. Quelle: bverwg.de.
- **BVerwG 28.11.2017, 7 A 17.12**: TA Laerm als antizipiertes Sachverstaendigengutachten — bindet Behoerde nicht bei abweichenden Erkenntnissen im Einzelfall. Quelle: bverwg.de.
- **EuGH 15.10.2009, C-263/08 (Djurgården)**: Beteiligungsrechte und Aarhus-Konvention; Begriff „betroffene Oeffentlichkeit". Quelle: curia.europa.eu.
- **EuGH 16.04.2015, C-570/13 (Gruber)**: Klagebefugnis Drittbetroffener auch ohne foermliche Beteiligung am Verfahren. Quelle: curia.europa.eu.

Konkrete Aktenzeichen weiterer Entscheidungen (insb. OVG / VGH) vor Ausgabe ueber bverwg.de bzw. landesrecht-[bundesland].de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Betreiber-Perspektive: Genehmigungsantrag

1. **Anlage einordnen**: 4. BImSchV Spalte 1 oder 2, UVP-Screening nach UVPG Anlage 1.
2. **Verfahrensart bestimmen**: § 10 (foermlich) oder § 19 BImSchG (vereinfacht).
3. **Antragsunterlagen zusammenstellen**: § 4 9. BImSchV — Erlauterungsbericht, Immissionsprognosen (Schall, Staub, Luft), Lageplaeane, Betriebsbeschreibung, Sicherheitsbericht bei Stoerfallanlage.
4. **Behoerde benennen**: Genehmigungsbehoerde (Landes-Immissionsschutzbeh.), beteiligte Fachbehoerden (Wasserbeh., Naturschutz, Arbeitsschutz).
5. **Oeffentlichkeitsbeteiligung**: Auslegung 1 Monat; Einwendungsfrist; Eroerterungstermin.
6. **Bescheid pruefen**: Nebenbestimmungen angreifen wenn unverhaltsnismassig (§ 12 BImSchG).
7. **Vollzug sichern**: Nebenbestimmungen erfuellen, Betrieb anzeigen, Emissionsberichte.

### B) Nachbar-/Dritter-Perspektive: Drittanfechtung

1. **Drittschutz pruefen**: § 5 Abs. 1 Nr. 1 BImSchG (Schutz vor schaedlichen Umwelteinwirkungen), TA-Laerm, TA-Luft-Richtwerte; Eigentumsverletzung benennen.
2. **Klagebefugnis**: Analogie § 42 Abs. 2 VwGO; Betroffenheit in eigenen Rechten.
3. **Frist**: 1 Monat nach Bekanntgabe Genehmigung (Widerspruch, soweit Widerspruchsverfahren erhalten, ansonsten direkt Klage VG).
4. **Eilantrag**: § 80a Abs. 3, § 80 Abs. 5 VwGO bei bereits vollziehbarer Genehmigung.
5. **Gruende**: Schallgutachten falsch (Methodik, Pegelbewertung), UVP-Fehler, fehlende Behoerden-Beteiligung, Drittschutz-Verstoss.
6. **Verband**: UmwRG-Vereinigung — Verbandsklage § 2 UmwRG bei UVP-pflichtigen Vorhaben.

### Entscheidungsbaum Klage

```
Liegt ein BImSchG-Bescheid vor?
 JA → Bin ich Adressat (Betreiber)?
 JA → Nebenbestimmungsanfechtung oder Aufhebungsklage
 NEIN → Dritter (Nachbar/Verband)?
 JA → Drittschutz § 5 Abs. 1 Nr. 1? TA-Laerm-Grenzwert ueberschritten?
 JA → Anfechtungsklage VG + ggf. § 80a Eilantrag
 NEIN → Zulassungsklage aussichtsarm
 NEIN → Antragsverfahren laueft → Beteiligungsrechte wahren, Einwendungen erheben
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch oder Klage gegen Drittanfechtung BImSchG | Klage-Schriftsatz nach Schema; Template unten |
| Variante A — Genehmigung noch nicht bestandskraeftig Einwendung moeglich | Einwendung im Verfahren zuerst; Klage erst nach Abschluss |
| Variante B — Mandant will nur bestimmte Auflagen anfechten | Teilanfechtung nur der belastenden Nebenbestimmungen |
| Variante C — Drittanfechtung Nachbar klagt gegen Genehmigung | Beiladungsantrag stellen; Verteidigung der Genehmigung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Widerspruch/Klage Drittanfechtung

**Adressat:** Widerspruchsbehoerde / Verwaltungsgericht — Tonfall: sachlich-juristisch

```
An die [Behoerde / das Verwaltungsgericht [ORT]]

Widerspruch / Klage

des/der [NAME MANDANT], [ADRESSE]
— Widersprechende/r / Klaeger/in —

gegen

Genehmigungsbescheid der [BEHOERDE] vom [DATUM], Az. [AZ.]
— zugunsten [BETREIBER] —

I. Wir erheben Widerspruch / Klage und beantragen:
1. Der Bescheid vom [DATUM] wird aufgehoben.
2. [BEHOERDE] traegt die Kosten.

II. Begruendung
Der/die Klaeger/in ist Eigentuemerinn des Grundstuecks [FLUR].
Die Genehmigung verletzt drittschuetzende Normen (§ 5 Abs. 1 Nr. 1 BImSchG):
- Schallpegel: Prognostizierter Nachtwert [X] dB(A) ueberschreitet TA-Laerm-Richtwert
 von 40 dB(A) im Reinen Wohngebiet / 45 dB(A) im Allgemeinen Wohngebiet.
- Gutachten-Maengel: [Konkrete Maengel benennen — Messpunkt, Methodik, Kumulation]
- UVP-Verfahrensfehler: [Falls UVP-pflichtig — Oeffentlichkeitsbeteiligung unterblieben]

Anlagen: Eigentumsnachweis, Schallgutachten-Gegengutachten, Lageplan
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Fristen und Verfahrenseckpunkte

| Schritt | Frist | Grundlage |
|---|---|---|
| Einwendungen im Genehmigungsverfahren | Auslegungsfrist + 2 Wochen | § 10 Abs. 3 BImSchG |
| Widerspruch | 1 Monat ab Bekanntgabe | § 70 VwGO |
| Anfechtungsklage (ohne Widerspruchsverfahren) | 1 Monat | § 74 VwGO |
| Eilantrag § 80a | Unverzueglich | § 80a VwGO |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Vertiefung: Typische Fehler und Verteidigung

- **TA-Laerm-Anwendung**: Zu optimistische Ausbreitung, fehlende Impulshaltigkeit, Tageszeit-Staffelung fehlt → Gegengutachten beauftragen.
- **Kumulation**: Andere vorhandene Anlagen als Vorbelastung nicht beruecksichtigt.
- **Praeventions-Gebot**: Nebenbestimmungen statt Ablehnung — Verhaeltnismaessigkeit pruefen.
- BVerwG 17.12.2020, 4 C 5.19 — saP-Pruefung Wind (bverwg.de); BVerwG 18.07.2019, 7 C 26.17 — UVP-Vorpruefung (bverwg.de); EuGH C-243/15 / C-664/15 — Aarhus-Klagebefugnis Umweltverband (curia.europa.eu).

## Anschluss-Skills

- `fachanwalt-verwaltungsrecht-drittanfechtung-umwelt` — Drittanfechtungs-Strategie
- `umweltrecht-verfahren` — Klageverfahren Geruestvorbereitung
- `energieanlagen-bimschg-genehmigung-verfahren` — Spezial-Energieanlagen
- `eilantrag-80-abs-5-vwgo` — Eilrechtsschutz nach Genehmigung

## 2. `umweltrecht-kommandocenter`

**Fokus:** Umweltmandat-Einstieg: Intake Anlagenkarte Behoerdenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster Mandanten-Typ-Identifikation Sachgebiets-Routing Triage-Matrix. Output Mandat-Karte Routing-Empfehlung Naechste-Schritte-Plan. Abgrenzung zu allen Fach-Skills (nur Master-Routing).

# Umweltrecht-Kommandocenter

## Triage-Matrix — welcher Fachmodul?

| Sachverhalt | Fachmodul |
|---|---|
| BImSchG-Genehmigung beantragen oder anfechten | `umweltrecht-immissionsschutz-bimschg` |
| Emissionshandel TEHG, BEHG, DEHSt | `umweltrecht-emissionshandel-tehg` |
| Abfallstatus, KrWG, Nebenprodukt, Circular Economy | `umweltrecht-abfall-circular-economy` |
| Naturschutz, FFH, Artenschutz § 44 BNatSchG | `umweltrecht-naturschutz-artenschutz` |
| Stoerfall-Anlage, 12. BImSchV, Seveso | `umweltrecht-stoerfall-anlagen` |
| Wasser-Erlaubnis, Altlasten, BBodSchG | `umweltrecht-wasser-bodenschutz` |
| M&A-Transaktion, Umwelt-DD, Red Flags | `umweltrecht-transaktionen-dd` |
| UIG/IFG-Informationsantrag, Ablehnung | `umweltrecht-umweltinformation-uig-ifg` |
| VG-Klage, Eilantrag, Beschwerde OVG | `umweltrecht-verfahren` |
| Bussgeld-Bescheid, Anhoerung, Sanktionen | `umweltrecht-bussgeld-sanktionen` |
| Compliance, Beauftragte, Schulungsplan | `umweltrecht-compliance-schulung` |
| ESG, CSRD, Greenwashing | `esg-greenwashing-csrd` |
| Klimaklage, Verbandsklage UmwRG | `klimaklagen-verbandsklage-umwrg` |
| Lieferkette, LkSG, CSDDD | `lksg-csddd-lieferkettensorgfalt` |

## Intake-Fragen (fuer jeden Mandat)

1. **Mandantenrolle**: Betreiber, Investor, Betroffener Dritter, Umweltverband, Behoerde?
2. **Rechtsgebiet**: BImSchG, KrWG, WHG, BBodSchG, TEHG, BNatSchG — oder mehrere?
3. **Verfahrensstand**: Noch kein Verfahren / Antragsverfahren laufend / Bescheid ergangen / Klage anhangig?
4. **Fristen akut**: Widerspruch 1 Monat, Klage 1 Monat, Eilantrag unverzueglich — Eingang Bescheid?
5. **Beweismaterial**: Welche Dokumente — Genehmigung, Gutachten, Behoerdenkorrespondenz, Fotos?
6. **Wirtschaftliches Ziel**: Betrieb sichern, Anlage verhindern, Entschaedigung, Informationszugang, Reputationsschutz?

## Zentrale Querschnitts-Normen Umweltrecht

- **§§ 3-10 BImSchG** — Grundpflichten Emissionsschutz
- **§§ 4 9 10 BBodSchG** — Altlasten-Verantwortung und Sanierung
- **§§ 8 9 10 WHG** — Wasserrechtliche Erlaubnisse
- **§§ 14 15 34 44 BNatSchG** — Eingriff, FFH, Artenschutz
- **§ 2 UmwRG** — Verbandsklage-Befugnis
- **§ 4 UmwRG** — Verfahrensfehler als Aufhebungsgrund
- **§ 80 Abs. 5 VwGO** — Eilrechtsschutz gegen vollziehbare Genehmigung

## Leitentscheidungen (Ueberblick)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ampelmatrix Risikobewertung (Standard-Output)

| Risiko | Ampel | Fristen | Verantwortlich | Naechste Handlung |
|---|---|---|---|---|
| [THEMA 1] | ROT | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 2] | ORANGE | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 3] | GRUEN | — | [PERSON] | Monitoring |

## Output-Template: Mandatskarte Umweltrecht

**Adressat:** Akte / Interne Notiz — Tonfall: strukturiert, stichwortartig

```
MANDATSKARTE UMWELTRECHT
Stand: [DATUM]
Akte: [AKTENZEICHEN]

MANDANT: [NAME], [ROLLE: Betreiber/Nachbar/Verband]
GEGNER/BEHOERDE: [NAME/STELLE]
ANLAGE: [BEZEICHNUNG], [ORT], [TYP]

RECHTSRAHMEN:
- Hauptnorm: § [X] [GESETZ]
- Nebenrecht: [weitere Normen]

VERFAHRENSSTAND:
- [DATUM]: Genehmigung erteilt / Antrag gestellt / Bescheid erhalten
- [DATUM]: Widerspruch eingelegt / Klage erhoben
- [DATUM]: Naechster Termin [Erörterungstermin / VG / OVG]

FRISTEN:
- [DATUM]: Klagefrist / Einwendungsfrist / TEHG-Abgabe

RISIKEN:
- ROT: [Konkrete Gefahr, z.B. Praeklusion mangels Einwendung]
- ORANGE: [Risiko mit Einschaetzung Wahrscheinlichkeit]

NAECHSTE HANDLUNG:
1. [Konkrete Massnahme, Verantwortlich, Deadline]
2. [Weitere Massnahme]

OFFENE FRAGEN / BENOETIGT:
- [Dokument / Information]
```

## Schnittstellen-Skills

- `fachanwalt-verwaltungsrecht-orientierung` — allgemeine Verwaltungsrechtspruefung
- `energieanlagen-bimschg-genehmigung-verfahren` — Energie-Spezial-BImSchG
- `energietrassen-planfeststellung-rechtsschutz` — Energie-Planfeststellung
- `esg-greenwashing-csrd` — Nachhaltigkeitsberichte
- `klimaklagen-verbandsklage-umwrg` — Klimaklagen

## 3. `umweltrecht-naturschutz-artenschutz`

**Fokus:** Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL 92/43/EWG Vogelschutz-RL. Prüfraster Eingriffs-Ausgleichs-Regelung saP-Gutachten FFH-Vertraeglichkeit Verbandsklagebefugnis. Output Artenschutz-Prüfung Kompensationskonzept. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (Anlagengenehmigung) und umweltrecht-verfahren (Klage).

# Naturschutz und Artenschutz

## Triage — klaere vor Eingriffs-Beurteilung

1. Liegt ein Eingriff in Natur und Landschaft vor (§ 14 BNatSchG)?
2. Befindet sich das Vorhaben im oder in der Naehe eines FFH-/Vogelschutz-Gebiets?
3. Koennen besonders/streng geschuetzte Arten betroffen sein (§ 44 BNatSchG)?
4. Ist ein naturschutzrechtlicher Fachbeitrag (saP, FFH-VS) erforderlich?
5. Wer ist Mandant — Vorhabentraeger oder klagender Umweltverband?
6. Liegt bestandskraeftige Genehmigung vor oder laeuft Verfahren?

## Zentrale Normen und Paragrafenkette

- **§ 14 BNatSchG** — Eingriffsbegriff (Veraenderung Gestalt/Nutzung Grundflaeche)
- **§ 15 BNatSchG** — Eingriffs-Ausgleichs-Regelung (Vermeidung, Ausgleich, Ersatz, Ausnahme)
- **§ 34 BNatSchG** — FFH-Vertraeglichkeitspruefung (erhebliche Beeintraechtigung Schutzzweck)
- **§ 36 BNatSchG** — Ausnahme FFH (zwingende Gruende oeffentliches Interesse, Ausgleichsmasnnahmen)
- **§ 44 Abs. 1 BNatSchG** — Verbotstatbestaende Artenschutz (Toeten, Stoeren, Entnahme, Zerstoerung Fortpflanzungsstaetten)
- **§ 45 BNatSchG** — Befreiung und Ausnahme Artenschutz
- **§ 69 BNatSchG** — Ordnungswidrigkeiten (Bussgeld bis 50.000 EUR)
- **§ 1 UmwRG** — Klagebefugnis anerkannter Umweltvereinigungen
- **§ 2 UmwRG** — Verbandsklage ohne Selbstbetroffenheit
- **Art. 12 FFH-Richtlinie 92/43/EWG** — Europaeischer Artenschutz strenge Verbote

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

### A) Vorhabentraeger: Artenschutzpruefung und FFH-VS

1. **Screening**: Lage in FFH-/VS-Gebiet oder signifikante Naehe? LANA-Hinweise zur Erheblichkeit.
2. **saP in Auftrag geben**: Spezieller artenschutzrechtlicher Fachbeitrag; Begehungen Fruehling und Herbst; Zielarten (Feldvogel, Fledermaus, Reptilien) kartieren.
3. **FFH-Vertraeglichkeitspruefung**: Screening-Stufe (erhebliche Beeintraechtigung moeglich?) → Hauptpruefung (alle Wirkpfade; Mafsnahmen zur Schadensbegrenzung).
4. **Ausnahme § 45 BNatSchG beantragen** (wenn Verbotstatbestand nicht vermeidbar): Oeffentliches Interesse, keine Alternativen, Ausgleich durch vorgezogene Ausgleichsmafsnahmen (CEF-Mafsnahmen).
5. **Eingriffsregelung § 15 BNatSchG**: Gruenplan mit Ausgleichsflaechen; Verhaeltnis Eingriff/Ausgleich 1:1 bis 1:3.
6. **Dokumentation**: Bestandteil des Genehmigungsantrags; Aktualisierung bei laenger als 2 Jahre zurueckliegenden Kartierungen.

### B) Umweltverband: Verbandsklage

1. **Klagebefugnis pruefen**: UmwRG-Anerkennung BUND, NABU, DUH; § 2 UmwRG kein Selbstbetroffenheitserfordernis.
2. **Ruege im Verwaltungsverfahren**: Pflicht zur Beteiligung; Unterlassen fuehrt zu Praeklusion im Klageverfahren (§ 5 UmwRG).
3. **Angriffspunkte**: Fehlerhafte saP, unzureichende FFH-VS, Artenschutz-Ausnahme nicht gerechtfertigt.
4. **Eilantrag § 80a VwGO**: Bei vollziehbarer Genehmigung sofort stellen.

### Entscheidungsbaum

```
Ist streng geschuetzte Art betroffen (§ 44 Abs. 1 BNatSchG)?
 JA → Vermeidung technisch moeglich?
 JA → Vermeidungsmafsnahme festlegen und dokumentieren
 NEIN → Ausnahme § 45 BNatSchG:
 Oeffentliches Interesse? JA → CEF-Mafsnahmen + Behoerdenentscheidung
 NEIN → Vorhaben in dieser Form nicht genehmigungsfaehig
 NEIN → Eingriffs-Ausgleichs-Regelung § 15 BNatSchG genuegt
```

## Output-Template: Einwendung im Genehmigungsverfahren (Verband)

**Adressat:** Genehmigungsbehoerde — Tonfall: sachlich-juristisch

```
An die [GENEHMIGUNGSBEHOERDE]

Einwendung des [VERBAND] gemaess § 10 Abs. 3 BImSchG / § 73 Abs. 4 VwVfG

Vorhabentraeger: [NAME]
Vorhaben: [BESCHREIBUNG]
Auslegung vom [DATUM] bis [DATUM]

I. Grundlage
[VERBAND] ist anerkannte Vereinigung i.S.d. § 3 UmwRG (Anerkennungsbescheid Anlage).

II. Artenschutz § 44 BNatSchG
Die saP vom [DATUM] genuegt nicht den Anforderungen:
1. Kartierung Fledermaeuse: Nur [X] Begehungen, keine Auswertung Horchboxen.
2. Brutvoegel: Brutvogel-Kartierung fehlt fuer Bereich [X] vollstaendig.
3. Stoerungsverbot § 44 Abs. 1 Nr. 2 BNatSchG: Laermimmission waehrend Brutzeit
 nicht bewertet.

III. FFH-Vertraeglichkeit § 34 BNatSchG
Das FFH-Gebiet [NAME] liegt [X] m entfernt. Eine FFH-VS liegt nicht vor,
obwohl erhebliche Beeintraechtigung des Schutzzwecks [ZIELART] nicht
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

IV. Antrag
Die Genehmigung darf erst erteilt werden, wenn aktuelle saP und FFH-VS
vorgelegt und ausgelegt werden.
```

## Vertiefung: CEF-Mafsnahmen

- CEF = Continuous Ecological Functionality; muessen vor Eingriff wirksam sein.
- Typische CEF: Nisthilfen, alternative Bruthabitate, Amphibien-Leitwaende.
- Monitoring-Pflicht: Regelmaessige Kontrolle Wirksamkeit; bei Versagen: Anordnung Nachbesserung.

## Anschluss-Skills

- `umweltrecht-verfahren` — Klageverfahren Naturschutz
- `klimaklagen-verbandsklage-umwrg` — Verbandsklage Klimaschutz
- `energieanlagen-bimschg-genehmigung-verfahren` — Artenschutz bei Energieanlagen
- `fachanwalt-verwaltungsrecht-drittanfechtung-umwelt` — Drittanfechtung Naturschutz
