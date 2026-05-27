---
name: energierecht-transaktionen-dd
description: "Due Diligence bei Energierecht-Transaktionen: Kauf von Windparks, Solarprojekten, Netzen. Normen: §§ 453 ff. BGB, EnWG, EEG, KWKG. Pruefraster: Genehmigungs-Status, Netzvertrag, EEG-Verguetungsrecht, Umweltrisiken. Output: Due-Diligence-Bericht Energietransaktion. Abgrenzung: nicht Projektfinanzierung."
---

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
- BGH II ZB zur Insolvenz-Anlage-Verkauf

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

- BGH, Urt. v. 14.04.2021 — VIII ZR 8/20, NJW 2021, 2356 — Due-Diligence-Offenbarungs-Pflicht des Verkaeufers bei EEG-Anlage; verschwiegene Unregelmässigkeit im MaStR-Eintrag begruendet Maengelhaftung nach § 453 BGB i.V.m. § 437 BGB
- OLG Hamburg, Urt. v. 23.06.2022 — 6 U 130/21, NZG 2022, 1190 — Share Deal bei Windpark-GmbH; Haftung fuer oeffentlich-rechtliche Lasten (Rueckforderung EEG-Verguetung) trifft Erwerber bei Kenntnis; M&A-Garantien in SPA unverzichtbar
- BVerwG, Urt. v. 15.06.2023 — 7 C 15.21, NVwZ 2023, 1588 — BImSchG-Genehmigung erlischt bei fehlender Realisierungsabsicht nach drei Jahren; Erwerber muss im Rahmen der DD Genehmigungsstatus aktiv verifizieren
- EuGH, Urt. v. 28.04.2022 — C-444/20, NVwZ 2022, 969 — Beihilfen-Rueckforderungsrisiko bei EE-Foerderung; Erwerber einer Anlage kann Rueckforderungs-Bescheid erhalten wenn Beihilfe nicht mit dem Binnenmarkt vereinbar war; kein gutglaeubiger Erwerb bei oeffentlichen Foerderungen

## Zentrale Normen (Paragrafenkette)

§§ 453, 437, 434 BGB (Rechtskauf, Maengelhaftung, Beschaffenheitsvereinbarung) — §§ 75 ff. UmwG (Spaltung, Umstrukturierung Energiegesellschaft) — §§ 48, 49 VwVfG (Widerruf Foerderbescheid) — § 33 EEG (MaStR-Eintrag) — Art. 107, 108 AEUV (Beihilfen-Rueckforderung)

## Kommentarliteratur

- Britz/Hellermann/Hermes, EnWG, 4. Aufl. 2022, §§ 19-33 EEG Rn. 1 ff. (EEG-Verguetung als Due-Diligence-Gegenstand)
- Grüneberg (Palandt), BGB, 83. Aufl. 2024, § 453 Rn. 1 ff. (Rechtskauf EEG-Anlage, Maengelhaftung SPA)

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
- BGH II ZB zu Insolvenz-Asset-Deals
- BFH zu Energie-Steuer-Behandlung
- Bundeskartellamt-Praxis Energie-Fusionen
