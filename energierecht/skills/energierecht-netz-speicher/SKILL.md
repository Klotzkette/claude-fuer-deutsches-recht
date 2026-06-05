---
name: energierecht-netz-speicher
description: "Netz Speicher: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Netz Speicher

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Netz Speicher** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `energierecht-kommandocenter` | Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output: Skillauswahl-Empfehlung Energierecht. Abgrenzung: kein inhaltlicher Prüf-Skill. |
| `energierecht-netz-speicher-zugang` | Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher prüfen. Normen: §§ 17 ff. 20 ff. EnWG, NAV. Prüfraster: Netzanschlussrecht, Anschlussbegehren, Kapazitaetsprüfung, Diskriminierungsfreiheit. Output: Netzanschluss-Rechtsgutachten. Abgrenzung: nicht EEG-Verguetungsrecht. |
| `energierecht-projektfinanzierung` | Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KWKG, BGB. Prüfraster: Finanzierungsstruktur, Sicherheitenpakete, Cashflow-Analyse, Foerderdarlehen. Output: Projektfinanzierungs-Struktur Energieanlage. Abgrenzung: nicht Betriebsgenehmigung. |
| `energierecht-transaktionen-dd` | Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Prüfraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken. Output: Due-Diligence-Bericht Energietransaktion. Abgrenzung: nicht Projektfinanzierung. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **Netz Speicher**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `energierecht-kommandocenter`

**Fokus:** Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output: Skillauswahl-Empfehlung Energierecht. Abgrenzung: kein inhaltlicher Prüf-Skill.

# Energierecht — Kommandocenter (Eingangs-Routing)

## Zweck

Der Erst-Skill jedes Energiemandats. Sortiert den Eingang nach Mandanten-Rolle und Sachgebiet, identifiziert kritische Fristen, schickt den Fall in den passenden Fachmodul.

## Eingaben

- Mandant (Stadtwerk, Versorger, Industriekunde, Investor, Behörde, Projektgesellschaft, Privater)
- Lebenszyklus-Phase (Projektentwicklung, Genehmigung, Betrieb, Streit, Transaktion, Insolvenz-/Krisennähe)
- Konkrete Anfrage / Bescheid / Vertragsentwurf
- Fristen erkennbar (Behörden-Frist, Marktrollen-Wechsel, BNetzA-Festlegung, Klagefrist)
- Beteiligte (Übertragungs-Netzbetreiber Anbieter Bilanzkreis-Verantwortliche etc.)

## Schritt 1 — Rolle und Hauptpfad bestimmen

| Rolle | Typischer Hauptpfad |
|---|---|
| Kommune / Stadtwerk | Konzessionsvertrag, Wärmeplanung, Mieterstrom, Beihilfe, EEG/KWKG-Vermarktung |
| Versorger / Stromlieferant | Vertrieb, Bilanzkreis, Beschaffungspreise, Endkunden-AGB, Strompreisbremse-Folge |
| Übertragungs-/Verteilnetzbetreiber | Netzentgelt-Festlegung BNetzA, Netzanschluss, Engpass-Management § 13 EnWG, Redispatch 2.0 |
| Industriekunde | Sondernetzentgelt § 19 StromNEV, EEG-Umlage-Befreiung BesAR-Vorgänger, Strompreiskompensation, PPA |
| Erzeugungs-Investor | EEG-Vermarktung, KWKG, Anlagenzulassung, Direktvermarktung, PPA, BImSchG-Genehmigung |
| Wärme-Projektgesellschaft | Wärmeliefervertrag AVBFernwärmeV, Preisanpassung, Quartierskonzept, Wärmenetz-Anschluss-/Benutzungs-Zwang, BEW-Förderung |
| Wasserstoff-Projektgesellschaft | Elektrolyseur-Genehmigung, RED-III-Anforderungen, Wasserstoff-Netzentwicklungsplan, HRG-Verfahren |
| Mobilität / Ladeinfrastruktur | LSV-Regelung, AFIR, Ladeinfrastruktur-Förderung, Mess- und Eichrecht |
| Privatperson / Mieter | Mieterstrom, PV-Anlage Eigenverbrauch, Heizungswechsel GEG, Energiepreis-Streit |
| Behörde | Stellungnahme, Genehmigung, Aufsichts-Anordnung |

## Schritt 2 — Sachgebiet und Skill-Routing

| Sachgebiet | Folge-Skill |
|---|---|
| EEG / KWKG / Direktvermarktung / Anlagenzulassung | `energierecht-eeg-kwkg-erzeugung` |
| Netzanschluss, Netzentgelte, Engpass, Speicher-Zugang | `energierecht-netz-speicher-zugang` |
| Stromlieferung, Bilanzkreis, GPKE-Prozesse, Marktstammdatenregister | `energierecht-vertrieb-marktrollen` |
| Industriestrompreis, BesAR-Nachfolge, Strompreiskompensation, § 19 StromNEV | `energierecht-industriekunden` |
| Fernwärme, AVBFernwärmeV, kommunale Wärmeplanung, Mieterstrom | `energierecht-waerme-quartier` |
| Wasserstoff-Elektrolyseure, E-Mobilität, Ladeinfrastruktur | `energierecht-emobility-wasserstoff` |
| Stromtrasse-Planfeststellung EnLAG/BBPlG, Genehmigung größerer Vorhaben | `energierecht-infrastrukturprojekte` |
| Energiekonzern M&A, Asset Deal Erzeugungspark, DD-Befund | `energierecht-transaktionen-dd` |
| Bankfinanzierung, PPA-Strukturierung, Förderbescheid KfW BEW | `energierecht-projektfinanzierung` |
| BNetzA-Festlegung, Klage VG/OVG/BVerwG, Bußgeld-Sache | `energierecht-verfahren` |
| Marktbeherrschungs-Verfahren, Missbrauchskontrolle, Energie-spezifische Beihilfe | `energierecht-wettbewerb` |

## Schritt 3 — Kritische Fristen-Prüfung beim Erstkontakt

- **§ 75 EnWG Beschwerde-Frist** ein Monat ab Zustellung BNetzA-Beschluss
- **§ 12 Abs. 4 EnWG Frist Engpass-Anordnung**
- **§ 47 VwGO Normenkontrolle** Wärmepläne Satzungen ein Jahr ab Bekanntmachung
- **§ 33 EEG Frist Inbetriebnahme-Anmeldung** Marktstammdatenregister
- **§ 19 Abs. 2 Satz 2 StromNEV** Antrag Sondernetzentgelt jährlich bis 30.09. für Folgejahr
- **EEG-Förderhöchstwert Ausschreibung** unterjährige Termine BNetzA
- **§ 17 GEG Beratungsgespräch** vor Heizungstausch
- **Strompreisbremse-Abwicklungs-Fristen** (auch nach Auslauf wegen Nachläufer)
- **§ 25 KWKG Antragsfrist** Zuschlag für Bestandsanlagen
- **AVBFernwärmeV § 4 Preisanpassungs-Anzeige-Frist**

## Schritt 4 — Eskalations-Trigger

### Versorgungssicherheits-Notlage

- § 24 EnSiG Maßnahmen
- § 13 EnWG-Eingriffsbefugnisse
- BNetzA-Anordnungen Gas-Notfall-Plan

### Insolvenz-Nähe Versorger

- §§ 36c f. EnWG Ersatzversorger-Mechanismen
- Grundversorger-Wechsel
- Skill `mandat-triage-insolvenzrecht`

### Behördliche Sofort-Anordnung

- § 65 EnWG aufschiebende Wirkung Klage
- Eilantrag § 80 Abs. 5 VwGO

### Kommunale Wärmeplanung Pflicht-Frist

- WPG 30.06.2026 (Großstädte)
- WPG 30.06.2028 (sonstige)
- Bei Versäumnis Sanktion / Folge-Pflichten

## Schritt 5 — Schnittstellen zu anderen Plugins

| Anliegen | Plugin |
|---|---|
| Energieanlagen-Genehmigung BImSchG | `umweltrecht`, neu im `fachanwalt-verwaltungsrecht` |
| Klima- und Naturschutz-Konflikte | `umweltrecht` |
| Stromtrassen-Planfeststellung | `fachanwalt-verwaltungsrecht` plus neuer Skill `energieanlagen-planfeststellung-enlag-bbplg` |
| Steuerliche Fragen Energiebesteuerung | `steuerrecht-anwalt-und-berater` |
| Berufsrecht Anwalt bei Energieprojekt | `kanzlei-allgemein` |
| ESG-Reporting CSRD Energie | `umweltrecht` Skill `esg-greenwashing-csrd` |
| Beihilferecht EU | `europarecht-kompass` |
| Bauleitplanung Wärmenetz-Korridore | `normenkontrolle-bauleitplanung` |
| Wettbewerbs-Verfahren Bundeskartellamt | `fachanwalt-internationales-wirtschaftsrecht` ergänzend |

## Schritt 6 — Mandatskarte und Ampel-Prüfung

Standard-Ausgabe Mandatskarte:

```
Mandant: [Name]
Rolle: [Stadtwerk / Versorger / Industriekunde / …]
Lebenszyklus-Phase: [Projektentwicklung / Betrieb / Streit / Transaktion]
Kritische Frist: [Datum + Norm]
Hauptpfad: [Skill]
Ampel: [GRÜN / GELB / ROT]
Risiko-Komponenten: [Versorgung / Genehmigung / Marktrollen / Förderung]
Naechster Schritt: [konkret]
Dokumenten-Stand: [vollstaendig / mit Luecken / fehlt]
Berufsrecht / DS-Pflichten: [Pruefung erfolgt]
```

### Ampel-Kriterien

- **ROT**: Frist binnen 14 Tagen, Versorgungs-Unterbrechung droht, Bußgeld absehbar, Insolvenz-Nähe Vertragspartner
- **GELB**: Frist binnen 3 Monaten, Genehmigungs-Verfahren mit Ausgang offen, Vertrags-Streit eskaliert
- **GRÜN**: Frist über 3 Monate, klare Rechtslage, kooperative Beteiligte

## Schritt 7 — Erstgesprächs-Fragen

1. **Mandant und Gegen-Seite**: Welche Rolle haben Sie? Wer ist Vertragspartner / Gegner / Behörde?
2. **Phase**: Projektentwicklung, Betrieb, Streit, Verkauf?
3. **Konkrete Anlass-Sache**: Bescheid? Vertragsentwurf? Behördlicher Brief? Klage?
4. **Frist erkennbar**: gibt es eine Datums-genannte Frist? Wenn ja, wann?
5. **Beteiligte Behörden**: BNetzA? Landesregulierungsbehörde? Kommune?
6. **Wirtschaftliche Größenordnung**: Volumen, Investitions-Summe, Streitwert?
7. **Strom- vs. Gas- vs. Wärme-/Wasserstoff-Bezug**?
8. **Förderung beantragt / bewilligt / abgewickelt**?
9. **EEG-/KWKG-Bezug**?
10. **Marktstammdatenregister-Eintrag**?

## Schritt 8 — Berufsrecht und Mandatsführung

- **Berufshaftpflicht** muss energierechtliche Beratung abdecken (häufig Ergänzung-Bedarf bei Allgemein-Kanzleien)
- **Spezialisten-Pflicht** wenn komplexes EEG-Vergabe-Verfahren oder BNetzA-Festlegung — ggf. Mit-Mandat Spezial-Kanzlei
- **Mandatsgeheimnis** § 43a Abs. 2 BRAO bei Geschäftsgeheimnissen Energieanlagen
- **Interessenkonflikt** Prüfung — Anbieter / Netzbetreiber / Verbraucher häufig gegenläufige Interessen

## Schritt 9 — Ausgabe-Standard

- Eingangs-Mandatskarte
- Skill-Routing-Empfehlung
- Frist-Tabelle
- Ampel-Bewertung
- Nächster Schritt formuliert
- Berufsrechts-Vermerk

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 31 EnWG (BNetzA-Beschwerde) — § 75 EnWG (OLG-Beschwerde) — §§ 4, 16 BImSchG (Genehmigung, Aenderung) — § 46 EnWG (Konzessionsvertrag) — §§ 72-78 VwVfG (Planfeststellung) — § 80 Abs. 5 VwGO (Eilrechtsschutz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quellen

- EnWG 2024 (Energiewirtschaftsgesetz, Neufassung)
- EEG 2023 + Solarpaket I 2024
- KWKG 2023
- GEG (Gebäudeenergiegesetz, Reform 01/2024)
- WPG (Wärmeplanungsgesetz, ab 01/2024)
- StromNEV / GasNEV / NAV / NDAV
- AVBFernwärmeV
- EnLAG / BBPlG / WindBG / SolarBG
- BNetzA-Beschlüsse (Festlegungs- und Genehmigungs-Verfahren)
- BVerwG- und EuGH-Linien zu Energierecht

## 2. `energierecht-netz-speicher-zugang`

**Fokus:** Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher prüfen. Normen: §§ 17 ff. 20 ff. EnWG, NAV. Prüfraster: Netzanschlussrecht, Anschlussbegehren, Kapazitaetsprüfung, Diskriminierungsfreiheit. Output: Netzanschluss-Rechtsgutachten. Abgrenzung: nicht EEG-Verguetungsrecht.

# Netz- und Speicher-Zugang

## Zweck

Behandelt Konflikte rund um Netzanschluss, Engpass-Management, Netzentgelte und Speicher-Sonderregelungen. Mandant typisch Erzeuger, Industriekunde, Speicher-Betreiber oder Netzbetreiber.

## Eingaben

- Anlagen-Typ und Leistung
- Standort (Netzgebiet, Verteilnetz vs. Übertragungsnetz)
- Aktueller Status (Antrag, Bestätigung, Ablehnung, Streit)
- Anschluss-Kosten geltend gemacht
- Netzentgelt-Festsetzung BNetzA für relevantes Jahr
- Bilanzkreis und Marktrollen

## Schritt 1 — Netzanschluss-Anspruch

### § 17 EnWG / § 8 EEG

- Anschluss-Pflicht Verteilnetzbetreiber für EE-Anlagen vorrangig § 8 EEG
- Sonstige Anlagen § 17 EnWG, Verhältnismäßigkeits-Prüfung
- Pflichtbestätigung mit Kosten-Schätzung binnen 8 Wochen

### Anschluss-Punkt

- Wirtschaftlich günstigster Punkt im technisch geeigneten Netzabschnitt
- Bei Streit Sachverständigen-Verfahren
- BNetzA-Festlegungen zu Anschluss-Standardisierung

### Anschluss-Kosten und Baukostenzuschuss

- Erzeugungs-Anlagen: Anschluss-Kosten typisch Anschluss-Begehrender (Anlage); ab Anschluss-Punkt Netzbetreiber
- Verbrauchs-Anlagen: Baukostenzuschuss nach NDAV / NAV
- BGH-Linie zu Baukostenzuschuss-Höhe

### Anschluss-Verweigerung

- Nur bei wirtschaftlicher Unzumutbarkeit Netzbetreiber
- "Wirtschaftliche Unzumutbarkeit" eng auszulegen — BNetzA-Maßstab
- Bei Verweigerung: Beschwerde BNetzA § 31 EnWG, danach OLG-Beschwerde § 75 EnWG

## Schritt 2 — Engpass-Management § 13 EnWG

### Drei Stufen

1. **Netzbezogene Maßnahmen** (Topologie-Wechsel, Spannungs-Anpassung)
2. **Marktbezogene Maßnahmen** (Redispatch, Bilanzkreis-Intervention)
3. **Notfall-Maßnahmen** (Abschaltungen)

### Redispatch 2.0 (seit 01.10.2021)

- **Alle Anlagen ab 100 kW** in Redispatch-Pflicht (auch EE-Anlagen!)
- Einspeise-Management durch Netzbetreiber bei Engpass
- Entschädigungs-Anspruch des Anlagen-Betreibers nach § 13a EnWG / § 15 EEG
- Daten-Übermittlungspflicht (Netzbetreiber-Vorgabe)

### Spitzenkappung § 11 Abs. 2 EnWG

- Verteilnetzbetreiber darf bis 3 % der jährlichen Energiemenge wegkappen
- Ohne Entschädigung
- BNetzA-Festlegung BK6-21-301

### Streitige Sachverhalte

- Falsche Engpass-Berechnung
- Diskriminierende Reihenfolge der Anlagen-Auswahl
- Entschädigungs-Höhe

## Schritt 3 — Netzentgelte und Anreizregulierung

### ARegV (Anreizregulierungsverordnung)

- Erlös-Obergrenze pro Netzbetreiber für 5-Jahres-Periode
- BNetzA-Festsetzung
- Effizienz-Werte als Vergleichsmaßstab
- Q-Faktor (Qualitätszuschlag/-abzug)

### StromNEV

- Berechnungs-Methodik Netzentgelte
- Netznutzungs-Entgelt für Endkunden
- Differenzierung Last-Profil, Spitzen-Last, Jahreshöchst-Last

### Gas: GasNEV

- Analog Strom, mit Sonder-Mechanismen für Speicher / Saisonale Schwankungen

### Streit BNetzA-Beschluss

- Beschluss BK4/BK6/BK8/BK9 — verschiedene Beschlusskammern
- Anhörungs-Beschluss → Festlegungs-Beschluss → Beschwerde OLG Düsseldorf § 75 EnWG
- Frist ein Monat

## Schritt 4 — Sondernetzentgelte Industrie § 19 StromNEV

### § 19 Abs. 1 StromNEV

- "Atypisches" Nutzungsverhalten
- Reduzierte Netzentgelte für Last-Profile außerhalb der Last-Spitze

### § 19 Abs. 2 Satz 1 StromNEV

- "Stromintensive Verbraucher" — bestimmte Verbrauchsstunden
- Reduzierung bis auf 20 % Standard-Entgelt

### § 19 Abs. 2 Satz 2 StromNEV

- "Bandlast-Privileg"
- Verbrauch ≥ 7.000 Vollbenutzungs-Stunden + ≥ 10 GWh/Jahr
- Ab 7.000 h: 20 % Entgelt; ab 7.500 h: 15 %; ab 8.000 h: 10 %
- **Antragsfrist: 30.09. für Folgejahr** beim Netzbetreiber

### Verfassungsrechtliche Probleme

- EuGH 02.09.2021, C-718/18: Unabhaengigkeit BNetzA als Regulierungsbehoerde; nationaler Gesetzgeber darf die Tarif-Festlegungskompetenz nicht beschraenken (curia.europa.eu).
- BNetzA-Festlegungen zu Anwendungs-Modalitaeten: aktuelle Festlegungs-Aktenzeichen vor Ausgabe ueber bundesnetzagentur.de pruefen

### Streit-Konstellation

- Antrag Sondernetzentgelt zurückgewiesen
- Beschwerde BNetzA → OLG Düsseldorf
- Skill `energierecht-industriekunden` für Detail

## Schritt 5 — Speicher

### Speicher-Doppelnutzungs-Privileg

- Speicher ist gleichzeitig Verbraucher (Lade-Phase) und Erzeuger (Entlade-Phase)
- **Vermeidungs-Vorschrift** § 118 EnWG: keine doppelte Netzentgelt-Belastung
- Stand 2024: zeitlich befristete Privilegierung bis 2029 (in Reform)

### Großspeicher

- Anschluss an Übertragungsnetz möglich
- Vermarktung als Regelenergie-Anbieter (Sekundärregelreserve, Minutenreserve, FCR)
- Netzentgelt-Befreiung gemäß § 118 Abs. 6 EnWG

### Heim-Speicher

- Verteilnetz-Anschluss
- Nutzung für Eigenverbrauch + Netzeinspeisung
- Marktstammdatenregister-Eintrag

### Wasserstoff-Speicher

- Sondernormen Wasserstoff-Netz-Verordnung
- Übergangsregelung Gasnetz-Mit-Nutzung
- Förderung KfW BEW / Klimaschutzverträge

## Schritt 6 — Bilanzkreis und Marktrollen

### Bilanzkreis-Verantwortlicher (BKV)

- Übernimmt Bilanzierung-Pflicht
- ÜNB Bilanzkreis-Vertrag
- Ausgleichsenergie bei Abweichungen

### GPKE / GeLi-Gas-Prozesse

- Standardisierte Marktrollen-Prozesse
- BNetzA-Festlegung MaBiS / WiM

### Marktstammdatenregister

- Zentrale BNetzA-Datenbank
- Eintragungs-Pflicht Anlagen / Marktakteure
- § 5 MaStRV

## Schritt 7 — EU-Bezug

### EU-Strommarktordnung 1227/2011 (REMIT)

- Markt-Transparenz, Insiderhandel-Verbot
- Bilanzkreis-Daten-Übermittlung
- BNetzA-Sanktionen bei REMIT-Verstoß

### EU-Strommarkt-Reform 2024

- Flexibilitäts-Mechanismen verstärken
- Capacity-Markt-Optionen für Mitgliedstaaten

### EuGH-Linie (verifiziert curia.europa.eu)

- EuGH 02.09.2021, C-718/18 — Unabhaengigkeit der Regulierungsbehoerde BNetzA; Tarif-Festlegung Strom und Gas
- Weitere EuGH-Entscheidungen zur Diskriminierungsfreiheit beim Netzzugang vor Ausgabe konkret ueber curia.europa.eu verifizieren

## Schritt 8 — Streit-Strategie

### Bei Netzanschluss-Problem

1. Schriftverkehr mit Netzbetreiber sortieren
2. § 17 EnWG / § 8 EEG-Anspruch prüfen
3. Wirtschaftlichkeits-Argument einbringen
4. BNetzA-Beschwerde § 31 EnWG
5. Vor OLG-Beschwerde (Frist 1 Monat ab BNetzA-Bescheid)

### Bei Netzentgelt-Streit

1. BNetzA-Festlegung studieren
2. Maßstab Anreizregulierung
3. Beschwerde BNetzA
4. OLG-Beschwerde

### Bei Engpass-Entschädigung

1. Daten-Übermittlung verifizieren
2. Entschädigung berechnen nach § 13a EnWG
3. Klage VG bei strittig
4. Skill `energierecht-verfahren`

## Aktuelle Rechtsprechung & Leitsätze (Stand 05/2026)

- **EuGH 02.09.2021, C-718/18** (Kommission ./. Deutschland, Strom- und Gasmarkt): Deutschland hat gegen die Richtlinien 2009/72/EG und 2009/73/EG verstossen — die Bundesnetzagentur muss umfassende Entscheidungsbefugnisse zur Festlegung der Tarife und Netznutzungsbedingungen haben (Unabhaengigkeit der Regulierungsbehoerde). Quelle: curia.europa.eu (CELEX 62018CJ0718).
- **BVerwG 09.06.2010, 9 A 20.08** (Bahnstromleitung): Anforderungen an Planfeststellung; immissionsschutzrechtliche Massgaben. Quelle: bverwg.de.
- **BGH (EnVR-Senat)**: Laufende Senatsrspr. zur ARegV, StromNEV-Anwendung; konkrete Aktenzeichen vor Ausgabe per bundesgerichtshof.de / OLG Duesseldorf (3. Kartellsenat) verifizieren.
- **OLG Duesseldorf VI-3 Kart**: laufende Senatsrspr. zu BNetzA-Beschluessen; oeffentliche Entscheidungsdatenbank olg-duesseldorf.nrw.de.
- **EnWG-Reform 2023/2024** (BGBl. I 2023 S. 1565 — EnWG-Aenderung im Rahmen Solarpaket I; sowie BGBl. I 2024): Umsetzung der EU-Strommarkt-Reform 2024/1747.

Konkrete Beschwerdeentscheidungen vor Ausgabe per olg-duesseldorf.nrw.de / bundesgerichtshof.de verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 17 EnWG (Netzanschluss-Pflicht) — § 8 EEG (Anschluss EE-Anlagen vorrangig) — § 13 EnWG (Engpass-Management) — § 13a EnWG (Redispatch-Entschaedigung) — § 19 StromNEV (Sondernetzentgelte) — § 118 EnWG (Speicher-Privileg) — §§ 31, 75 EnWG (BNetzA-Beschwerde, OLG-Beschwerde)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-eeg-kwkg-erzeugung` — Erzeugungs-Anlagen
- `energierecht-industriekunden` — § 19 StromNEV-Detail
- `energierecht-verfahren` — BNetzA-Beschwerde
- `energierecht-projektfinanzierung` — Speicher-Finanzierung

## Quellen

- EnWG 2024 §§ 8, 11, 13, 13a, 17, 31, 65, 75, 118
- EEG 2023 § 8, § 15
- StromNEV § 19
- GasNEV
- ARegV
- NAV / NDAV
- MaStRV § 5
- BNetzA-Beschlüsse BK4 / BK6 / BK8 / BK9 — bundesnetzagentur.de
- BGH EnVR-Linien — vor Ausgabe konkretes Aktenzeichen ueber bundesgerichtshof.de verifizieren
- OLG Düsseldorf VI-3 Kart-Verfahren — olg-duesseldorf.nrw.de
- EuGH 02.09.2021, C-718/18 — Unabhaengigkeit BNetzA als Regulierungsbehoerde (curia.europa.eu)
- EU REMIT 1227/2011
- EU-Strommarktordnung 2019/943 + Reform VO (EU) 2024/1747

## 3. `energierecht-projektfinanzierung`

**Fokus:** Projektfinanzierung für Energieanlagen strukturieren: Darlehen, Sicherheiten, Ratinganforderungen. Normen: EnWG, EEG, KWKG, BGB. Prüfraster: Finanzierungsstruktur, Sicherheitenpakete, Cashflow-Analyse, Foerderdarlehen. Output: Projektfinanzierungs-Struktur Energieanlage. Abgrenzung: nicht Betriebsgenehmigung.

# Projektfinanzierung Energie

## Zweck

Behandelt die Finanzierungs-Strukturierung von Energie-Projekten: Bank-Finanzierung, KfW-Förderung, PPA-Vermarktung, Sicherheiten-Konstruktion, Refinanzierung.

## Eingaben

- Projekt-Phase (Konzept, Planung, Realisierung, Betrieb)
- Investitions-Volumen
- Vermarktungs-Strategie (EEG / PPA / Eigenverbrauch / Markt)
- Finanzierungs-Mix (Eigenkapital, Banken, Förderung)
- Bonitäts-Lage Offtaker (PPA-Käufer)
- Steuerliche Strukturierung-Pläne

## Schritt 1 — PPA (Power Purchase Agreement) Strukturierung

### Physisches PPA

- Strom-Lieferung direkt Anlage → Käufer
- Bilanzkreis-Strukturen aufzubauen
- On-Site oder Off-Site
- Mess- und Eichrecht beachten

### Finanzielles PPA (Synthetic / Virtual PPA)

- Strom geht in Markt
- Differenz-Zahlung zwischen Festpreis und Marktpreis
- Bilanz-rechtlich anders strukturiert
- Häufig für internationale Mandanten

### Corporate Direct PPA

- Industrie-Käufer langfristig
- Vorteile beidseitig
- Skill `energierecht-industriekunden`

### Standard-Inhalte PPA

```
1. Vertragsdauer (10-20 Jahre)
2. Liefer-Anlage Identifikation
3. Strom-Mengen mit Volumen-Toleranzbändern
4. Preis-Formel (fest / index-gekoppelt / hybrid)
5. Take-or-Pay-Klauseln
6. Force-Majeure-Definition
7. Anpassungs-Klauseln (Markt, Recht, Steuer)
8. Sicherheiten (Bank-Bürgschaften)
9. Beendigungs-Modalitäten
10. Streit-Klausel (Schiedsverfahren oft)
11. Vertraulichkeits-Klausel
```

## Schritt 2 — Bank-Finanzierung Energie-Projekte

### Project Finance vs. Corporate Finance

- **Project Finance**: Anlage als alleinige Sicherheit; Non-Recourse oder Limited Recourse
- **Corporate Finance**: Konzern haftet zusätzlich
- Bei großen Projekten typisch Project Finance

### Sicherheiten-Konstruktion

- Sicherungs-Übereignung Anlagen-Bestandteile
- Forderungs-Abtretung aus PPA / EEG-Vergütung
- Verpfändung Gesellschaftsanteile
- Konten-Verpfändung Projektgesellschaft
- Step-In-Rechte bei Default

### Kreditgeber-Standards (Lender Requirements)

- DSCR (Debt Service Coverage Ratio) ≥ 1,2-1,4
- Risiko-Reserven (Wartungs-Reserve, DSRA)
- Wartungs-Verträge mit anerkannten Service-Anbietern
- Versicherungs-Schutz
- Regelmäßige Reporting-Pflichten

### Typische Bank-Konsortien

- KfW als Erstkredit-Geber
- Mittelständische Banken (Sparkassen-Verbund)
- Spezial-Energiebanken (UmweltBank, GLS Bank)
- Internationale Banken bei Großprojekten

## Schritt 3 — KfW-Förderprogramme

### KfW 442 BEW (Bundesförderung effiziente Wärmenetze)

- Module 1-3 (Studie / Investition / Betrieb)
- Förderung gestaffelt nach EE-Anteil
- Verzahnung mit kommunaler Wärmeplanung

### KfW 269 EE Energie

- Standard-EE-Anlagen-Investitionen
- Zinsverbilligungen
- Direkt-Förderzuschüsse

### KfW 261 / 262 Energieeffizient Bauen / Sanieren

- Gebäude-Energetik
- Zinsverbilligung + Zuschuss

### Klimaschutzverträge (CCfD)

- BAFA als Behörde
- 4 Mrd. € erstes Förderaufrufs-Volumen
- Bevorzugung KMU
- Differenzvertrag CO2

### Voraussetzungen

- Vor Vorhabens-Beginn
- Innovations- oder Effizienz-Komponente
- Realisierung in spezifizierter Zeit
- Reporting-Pflichten

### Rückforderungs-Risiko

- Bei Verstoß gegen Auflagen
- Rückforderung mit Zinsen
- 10-Jahres-Rückblick möglich

## Schritt 4 — Förder-Bescheid und Rechtsmittel

### Bewilligungs-Bescheid

- Verwaltungsakt
- Klage VG bei Ablehnung
- Skill `energierecht-verfahren`

### Auflagen-Compliance

- Dokumentations-Pflichten
- Audit-Termine
- Bei Verstoß Eilantrag möglich

### Bei Widerruf

- Aussetzungs-Antrag § 80 Abs. 5 VwGO
- Frist eng

## Schritt 5 — Sale-and-Leaseback

### Konzept

- Anlage wird an Bank / Leasing-Gesellschaft verkauft
- Leasing-rück an Projektgesellschaft
- Steueroptimierung
- Liquiditäts-Effekt

### Konditionen

- Steuerliche Gestaltung wichtig
- Leasing-Vertrag mit Optionen
- Risiken bei Steuer-Reform

### Sektor-Akzeptanz

- Bei Wind / Solar etabliert
- Bei innovativen Technologien fragwürdig

## Schritt 6 — Bonitäts-Prüfung Offtaker

### PPA-Käufer Risiko

- Insolvenz Offtaker = Vermarktungs-Verlust Anlage
- Long-term Verträge mit Industrie-Käufern üblich
- Bonität A oder besser empfohlen

### Sicherheiten gegen Käufer-Insolvenz

- Bank-Bürgschaft Offtaker
- Eltern-Garantie Mutter-Gesellschaft
- Verbindungs-zu-Vermarktungs-Möglichkeit (Markt-Default)

### Mehrere Offtaker

- Risiko-Streuung
- Komplexere Bilanzkreis-Strukturen

## Schritt 7 — Stranded-Assets-Risiko

### Definition

- Anlage wird vorzeitig wirtschaftlich entwertet
- Z.B. fossile Anlage durch CO2-Preis
- Politik-Risiko

### Mitigation

- Förderung mit Bestandsschutz
- Vertraglich abgesicherte Vermarktung
- Diversifikation Portfolio

### ESG-Aspekt

- Banken-Politik: keine neuen fossilen Kredite
- Insurance retreat (Versicherung)
- Pension-Fund-Aspekte

## Schritt 8 — Spezial-Finanzierungen

### Bürgerwind / Bürgerenergie

- Bürgerenergie-Gesellschaften
- Privilegierungen in EEG-Ausschreibung
- Crowd-Funding-Strukturen
- Genossenschafts-Modelle

### Mezzanine-Kapital

- Hybride zwischen Eigen- und Fremd-Kapital
- Höhere Zinsen, weicherer Rückgriff

### Bond / Schuldschein

- Bei großen Anlagen
- Kapitalmarkt-Zugang
- Wertpapier-Prospekt-Pflichten

### Grüne Anleihen (Green Bonds)

- Spezifische Ratings (CICERO, ISS-Oekom)
- EU-Green-Bond-Standard ab 2024
- ESG-Investoren

## Schritt 9 — Steuerliche Aspekte

### Anlagen-Abschreibung

- AfA-Tabelle für Energie-Anlagen
- Sonder-Abschreibungs-Optionen
- Investitionsabzugsbetrag § 7g EStG

### Investitionsabzugsbetrag

- Mittelständische Investoren
- Vor Anschaffung
- Auflösungs-Pflicht bei nicht-Realisierung

### Stromsteuer-Pflicht

- Eigenstrom-Verbrauch
- Stromsteuer-Vergütung Industrie
- Skill `energierecht-industriekunden`

### Umsatzsteuer Klein-Anlagen

- Kleinunternehmer-Regelung
- Pauschalierung möglich

## Schritt 10 — Mandanten-Strategie

### Projekt-Entwickler

1. Finanzierungs-Mix optimieren
2. PPA-Vermarktung vor Bau verhandeln
3. KfW-/CCfD-Förderung beantragen
4. Sicherheiten-Konstruktion mit Anwalt
5. Closing-Termine straff

### Bank / Kreditgeber

1. DD-Standard hoch
2. Sicherheiten-Bündel umfassend
3. Reporting-Pflichten klar
4. Step-In-Rechte sichern

### Offtaker (PPA-Käufer)

1. Bonitäts-Sicherheit Anlage
2. Vermarktungs-Risiko verteilen
3. ESG-Reporting CSRD-konform

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1191 ff. BGB (Grundschuld als Sicherheit) — §§ 398, 399 BGB (Forderungsabtretung) — § 307 BGB (AGB-Kontrolle Take-or-Pay) — §§ 48, 49 VwVfG (Ruecknahme, Widerruf Foerderbescheid) — §§ 19-21 EEG (Verguetungs-Anspruch als Sicherungs-Gegenstand) — §§ 1 ff. KWG (Finanzierung durch Kreditinstitute)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-eeg-kwkg-erzeugung`
- `energierecht-industriekunden` (PPA-Käufer)
- `energierecht-transaktionen-dd` (Erwerb)
- `energierecht-waerme-quartier` (BEW)
- `europarecht-kompass` (Beihilfen)
- `fachanwalt-bank-kapitalmarktrecht`
- `corporate-kanzlei`

## Quellen

- EEG § 27a (Doppelvermarktungs-Verbot)
- KfW-Förderrichtlinien 442, 269, 261, 262
- Klimaschutzverträge-Programm BMWK / BAFA
- EU-AGVO 651/2014
- EU-Green-Bond-Standard 2023/2631
- BFH zu Energie-Steuer und Abschreibung
- ICMA Green Bond Principles
- TLB / IF-Konzepte zu Project Finance Energie

---
<!-- AUDIT 27.05.2026 -->

## 4. `energierecht-transaktionen-dd`

**Fokus:** Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Prüfraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken. Output: Due-Diligence-Bericht Energietransaktion. Abgrenzung: nicht Projektfinanzierung.

# Energie-Transaktionen und Due Diligence

## Zweck

Behandelt M&A im Energie-Sektor: Asset Deal (Anlagen), Share Deal (Projekt-/Erzeugungs-Gesellschaft), Portfolio-Transfer (Stromvertrieb, Kundenbestand). Inkl. Distressed-Asset-Verkauf.

## Eingaben

- Transaktions-Gegenstand (Anlage, Gesellschaft, Portfolio)
- Verkäufer-/Käufer-Konstellation
- Transaktions-Phase (Letter of Intent, DD, SPA-Verhandlung, Closing)
- Anlagen-Stand (Inbetriebnahme, Förderung, Vertrags-Bindungen)
- Aktive Verfahren bei BNetzA / BAFA / Gerichten

## Schritt 1 — Asset vs. Share Deal

### Asset Deal

- Einzel-Übertragung Anlage(n), Verträge, Genehmigungen
- Verträge müssen einzeln auf Käufer überführt werden
- Genehmigungen über § 16 BImSchG Wechsel-Anzeige
- EEG-Vergütung über § 33 EEG-Wechsel

### Share Deal

- Gesellschafts-Anteile gehen über
- Verträge und Genehmigungen bleiben bei Gesellschaft
- Häufig einfacher zu strukturieren
- Aber: Steuerliche und haftungsrechtliche Erbschaft

### Wahl-Kriterien

- Bei Einzel-Anlage häufig Asset Deal
- Bei Portfolio mit vielen Anlagen Share Deal
- Steuerliche Optimierung (Anschaffungs-Kosten, Abschreibungen)
- Haftungs-Verteilung (Asset Deal sauberer)

## Schritt 2 — Due Diligence Energie-spezifisch

### Technical DD

- Anlagen-Zustand, Wartungs-Historie
- Restlaufzeit-Schätzung
- Service-Verträge

### Regulatory DD

- **EEG-Vergütungs-Anspruch** und Restlaufzeit
- **MaStR-Eintrag** korrekt und aktuell
- **BImSchG-Genehmigung** und Auflagen-Compliance
- **Repowering-Potenzial** und Genehmigungs-Lage
- **Anschluss-Punkt** Bestand und Erweiterungs-Möglichkeit

### Commercial DD

- **PPA-Bestand** Laufzeiten Konditionen
- **Strompreis-Forecast** Sensitivitäten
- **Wartungs-Verträge** und Kostenstruktur
- **Versicherungs-Status**

### Legal DD Schwerpunkte

- **Grundstücks-Verträge** (Eigentum, Pacht, Nießbrauch, Dienstbarkeiten)
- **Anschluss-Vertrag Netzbetreiber**
- **Förder-Bescheide** und Auflagen
- **Streitigkeiten** anhängig
- **Wartungs-/Pacht-/PPA-Verträge**

### Tax DD

- Strom-Steuer-Pflicht
- Bewertung Anlagen-Vermögen
- Sonderabschreibungs-Möglichkeiten
- Eigenstromsteuer-Pflicht

### ESG DD

- CSRD-Berichts-Konformität
- Naturschutz-Compliance
- Sozial-Aspekte (Bürger-Beteiligung)

## Schritt 3 — EEG-Vergütungs-Anspruch im Asset Deal

### § 33 EEG Wechsel

- Anlagen-Betreiber kann wechseln
- Vergütungs-Anspruch geht auf Käufer über
- MaStR-Aktualisierung Pflicht binnen Monat

### Bedingungen Übergang

- Anlage und Stand-Ort bleiben gleich
- Vergütungs-Höhe und -Dauer unverändert
- Bei Repowering: Re-Zulassung erforderlich

### Risiken Käufer

- Vergangenheits-Verstöße des Verkäufers können auf Vergütung wirken
- BNetzA-Prüfung möglich
- Garantien im SPA erforderlich

## Schritt 4 — Distressed-Asset-Verkauf

### Insolvenz-Konstellation

- Anlage in Insolvenz des Verkäufers
- Insolvenz-Verwalter veräußert
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Anfechtungs-Risiko

- Bei Verkauf in Insolvenz-Nähe § 133 InsO
- Skill `vorsatzanfechtung-133-inso` im Insolvenzrecht-Plugin
- Gleichwertigkeits-Prüfung Verkaufs-Preis

### Bewertungs-Komplexitäten

- Anlagen-Wert in Insolvenz häufig deutlich reduziert
- Zukunftserlöse mit Risiko-Aufschlag diskontiert
- LCOE-Vergleich (Levelized Cost of Energy)

## Schritt 5 — Beihilfen-Prüfung

### Förder-Bescheide

- KfW BEW, Klimaschutzverträge, Ausschreibungs-Zuschläge
- Übertragung auf Käufer prüfen
- Häufig Genehmigungs-Pflicht durch Behörde

### De-minimis-Grenze

- EU-Beihilfenrecht
- Bei mehreren Förderungen kumulieren
- 200.000 € in 3 Jahren (allgemein)

### EU-AGVO 651/2014

- Allgemeine Gruppenfreistellungs-Verordnung
- Häufige Rechtsgrundlage Förderungen Energiebereich
- Auflagen-Compliance dokumentieren

### Rückforderungs-Risiko

- Bei Beihilfen-Verstoß EU-Kommission
- Verzinsung bis 10 Jahre rückwirkend
- Skill `europarecht-kompass`

## Schritt 6 — Strompreiskompensation-Rückforderungs-Risiko

### Konstellation

- Bei Strompreiskompensation-Empfänger Verkauf an Käufer
- Voraussetzungen müssen weitergeführt werden (Branche, Stromintensität)
- Bei nicht-Weiterführung Rückforderung BAFA

### SPA-Klausel

- Indemnification für Rückforderungs-Fälle
- Pflicht zur Weiterführung Bedingungen

## Schritt 7 — Bewertungs-Methodik

### DCF-Methode

- Frei-Cashflow-Diskontierung
- Anzulegender Wert / Marktpreis-Forecast als Einnahmen
- Wartungs-Kosten, Steuern, Försterung-Aufwendungen
- WACC-Bestimmung mit Risiko-Aufschlag

### LCOE-Vergleich

- Levelized Cost of Energy
- Vergleich mit Alternativ-Anlagen
- Investitions-Entscheidung

### Sensitivitäten

- Strompreis-Volatilität
- Anlagen-Verfügbarkeit
- Regulierungs-Risiken (Förder-Änderung)

### Multiple-Methode

- Bei Portfolio-Transaktionen
- € pro installierte MW
- € pro EBITDA

## Schritt 8 — SPA-Struktur (Share Purchase Agreement)

### Garantien Verkäufer

- Eigentum unbelastet
- Anlagen funktionsfähig
- EEG-Vergütung Bestand
- MaStR-Eintrag korrekt
- BImSchG-Compliance
- Keine offenen Verfahren

### Garantie-Erfüllungs-Zeitraum

- Typisch 24 bis 36 Monate
- Verlängert bei Steuer-Sachverhalten

### Indemnification

- Spezifische Sachverhalte (z.B. Strompreiskompensation)
- Haftungs-Höchstgrenze

### Conditions Precedent

- BNetzA-Anzeige § 33 EEG
- BImSchG-Wechsel-Anzeige § 16
- Förder-Bescheid-Übertragung
- Kartellamts-Freigabe
- ggf. § 12 BauGB-Übertragungs-Genehmigung

### Closing-Procedure

- Vor-Closing Bedingungen erfüllt
- Übertragungs-Akte
- Zahlungs-Abwicklung

## Schritt 9 — Kartellrechtliche Aspekte

### Marktbeherrschungs-Anmeldung

- Bei größeren Energieanlagen-Transaktionen
- Bundeskartellamt 9. Beschlussabteilung Energie
- Anmeldeschwelle BKartA

### EU-Anmeldepflicht

- Bei größerem Volumen EU-Kommission
- Phase-I- und Phase-II-Verfahren

## Schritt 10 — Mandanten-Strategie

### Verkäufer

1. Vendor DD durchführen
2. Garantie-Risiken minimieren
3. Indemnification-Klauseln verhandeln
4. Tax-Optimierung
5. Closing-Zeitplan straff

### Käufer

1. Sorgfältige DD mit Energie-Spezialisten
2. Bewertungs-Sensitivitäten
3. Garantie-Forderungen
4. Conditions Precedent klar
5. Integrations-Plan vorbereiten

### Investor / PE

1. Portfolio-Aufbau Logik
2. Bei mehreren Anlagen Plattform-Strategie
3. Skalen-Vorteile (Wartung, Vermarktung)
4. Exit-Strategie 5-7 Jahre

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 453, 437, 434 BGB (Rechtskauf, Maengelhaftung, Beschaffenheitsvereinbarung) — §§ 75 ff. UmwG (Spaltung, Umstrukturierung Energiegesellschaft) — §§ 48, 49 VwVfG (Widerruf Foerderbescheid) — § 33 EEG (MaStR-Eintrag) — Art. 107, 108 AEUV (Beihilfen-Rueckforderung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-eeg-kwkg-erzeugung`
- `energierecht-projektfinanzierung`
- `energierecht-industriekunden` (Strompreiskompensation)
- `vorsatzanfechtung-133-inso` (Distressed)
- `europarecht-kompass` (Beihilfen)
- `corporate-kanzlei` / `grosskanzlei-corporate-ma` für M&A-Standards

## Quellen

- EEG § 33 (Anlagen-Wechsel)
- BImSchG § 16
- MaStRV § 5
- UmwG / GmbHG / AktG für Share Deals
- EU-AGVO 651/2014
- EU-Beihilfen-Verfahrens-Verordnung 2015/1589
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BFH zu Energie-Steuer-Behandlung
- Bundeskartellamt-Praxis Energie-Fusionen

---
<!-- AUDIT 27.05.2026 -->
