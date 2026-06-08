---
name: netz-speicher
description: "Navigationszentrum für alle Energierecht-Skills: Weiterleitung je Rechtsthema und Anfrageart. Normen: EnWG, EEG, KWKG, GEG. Prüfraster: Themenfeld Erzeugung/Netz/Vertrieb, Kundentyp, einschlaegige Norm. Output: Skillauswahl-Empfehlung Energierecht. Abgrenzung: kein inhaltlicher Prüf-Skill im Energierecht."
---

# Energierecht — Kommandocenter (Eingangs-Routing)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

