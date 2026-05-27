---
name: energierecht-waerme-quartier
description: "Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende. Normen: AVBFernwaermeV, GEG, EnWG, EEG. Pruefraster: Konzessionspflicht, Preisanpassungsklauseln, GEG-Anforderungen. Output: Waermenetz-Rechtsgutachten. Abgrenzung: nicht allgemeine Energieliefervertraege."
---

# Wärme, Quartier und Fernwärme

## Zweck

Behandelt kommunale Wärmeplanung, Fernwärmeverträge, Mieterstrom, BEW-Förderung und integrierte Quartiers-Konzepte. Praktisch oft wichtigster Bereich kommunaler Klimapolitik.

## Eingaben

- Mandant (Stadtwerk, Wärme-Projektgesellschaft, Mieter, Industriekunde, Kommune)
- Projekt-Phase (Konzept, Genehmigung, Anschluss, Betrieb, Streit)
- Wärmequelle (Fernwärme, BHKW, Wärmepumpe, Geothermie, Solarthermie, Biomasse, H2-ready)
- Quartiersstruktur (Anzahl Anschlüsse, Mischung Wohnen / Gewerbe)
- Bestehende Wärmeliefer-Verträge

## Schritt 1 — Kommunale Wärmeplanung WPG (seit 01.01.2024)

### Pflicht zur Wärmeplanung

- **Großstädte (über 100.000 EW)**: Wärmeplan bis **30.06.2026**
- **Sonstige Gemeinden**: bis **30.06.2028**
- Verlängerungen / Sondersituationen länderrechtlich

### Inhalte Wärmeplan

- Bestandsanalyse Wärmequellen und -bedarfe
- Eignungsgebiete Wärmenetze
- Eignungsgebiete dezentrale Versorgung (Wärmepumpe)
- Zeitlicher Umsetzungs-Plan
- Klimaneutralitäts-Ziel 2045

### Rechtsnatur Wärmeplan

- **Pflicht der Gemeinde** als kommunale Planung
- **Keine unmittelbare Rechtswirkung** für Eigentümer
- **Bauleitplanerische Verzahnung** möglich (B-Plan Fernwärme-Korridor)
- Skill `normenkontrolle-bauleitplanung` bei B-Plan-Verzahnung

### Beteiligung der Öffentlichkeit § 7 WPG

- Beteiligungs-Verfahren analog Bauleitplanung
- Eigentümer, Versorger, Industrie

## Schritt 2 — Anschluss- und Benutzungs-Zwang (AuB)

### Rechtsgrundlage

- § 16 GG Anschlussverpflichtung kommunal
- Landes-Vorschriften (z.B. Art. 24 BayGO; § 8 GO NRW)
- Satzungs-Erlass durch Kommune

### Voraussetzungen

- **Wirtschaftliche Vorteilhaftigkeit** Fernwärme
- **Versorgungssicherheit** garantiert
- **Verhältnismäßigkeits-Prüfung** Einzelfall: Eigentümer-Eingriff vs. öffentliches Interesse
- BVerwG 7 C 32.94 zur Verhältnismäßigkeit

### Streit-Konstellation

- Eigentümer wehrt sich gegen AuB-Satzung
- **Normenkontrolle § 47 VwGO**
- Antragsbefugnis Eigentümer
- Skill `normenkontrolle-bauleitplanung`

## Schritt 3 — AVBFernwärmeV

### Anwendungs-Bereich

- Verträge zwischen Fernwärme-Versorger und Endkunden (Haushalts-Kunden, Kleinunternehmen)
- Standard-AGB-Verordnung des Bundes

### Vertrags-Inhalte § 1 AVBFernwärmeV

- Vertrags-Dauer max. 10 Jahre, verlängert um 5 Jahre wenn nicht gekündigt
- Preisanpassungs-Klauseln nur Cost- und Marktelement-basiert
- Preisanpassungs-Information mit 6 Wochen Vorlauf

### Preisanpassungs-Klauseln Streit

- **BGH VIII ZR 263/22 (Urt. 06.03.2024)**: Preisanpassungs-Klauseln müssen den Anforderungen § 24 Abs. 4 AVBFernwärmeV genügen
- Transparenz-Erfordernis
- Bezugnahme auf nachvollziehbare Indizes (Erdgaspreis, Holzpellet-Index, Inflation)
- **Spotpreis-Indizierung problematisch** wenn nicht für den Lieferanten-Bedarf typisch
- Mehrere LG / OLG-Urteile zur Klausel-Wirksamkeit nach Energiekrise 2022

### Klausel-Wirksamkeits-Prüfung

1. **Transparenz** — Klausel verständlich?
2. **Sachlicher Zusammenhang** — Index ist tatsächlich Cost-Komponente?
3. **Begrenzungs-Mechanismus** — Kappung / Cap vorhanden?
4. **Begründungs-Pflicht** bei Preisanpassung
5. **Cap- oder Cap-and-Floor-Modell** transparent

### Folge unwirksamer Klausel

- Ausgangs-Preis bleibt
- Rückforderungs-Anspruch Kunden
- Schwerer wirtschaftlicher Schaden Versorger
- Sanierungs-Vergleich

## Schritt 4 — Mieterstrom-Modell

### Konzept

- PV-Anlage auf Mietshaus
- Strom an Mieter direkt geliefert (statt EEG-Einspeisung)
- Mieter zahlt unter Netz-Strom-Preis

### Förder-Rechtsgrundlage EEG § 21

- Mieterstrom-Zuschlag
- Eingeschränkt auf Anlagen bis 100 kWp pro Gebäude (Verbund-Ausnahme)

### EnWG § 42a

- Mieterstrom-Definition
- Versorger-Pflichten reduziert
- Vereinfachte AGB

### Solarpaket I (Mai 2024)

- Vereinfachungen bei Mieterstrom-Verträgen
- Reduzierte Bilanzkreis-Pflichten
- "Gemeinschaftliche Gebäudeversorgung"

### Vertrags-Strukturierung

- Stromlieferungs-Vertrag mit Mieter
- AGB konform StromGVV-Vorbilder
- Wechsel-Möglichkeit zu anderem Versorger sichern
- Anlagen-Eigentum klären (Vermieter / Betreiber-Modell)

## Schritt 5 — BEW (Bundesförderung effiziente Wärmenetze)

### Förderprogramm KfW 442

- Investitions-Förderung Wärmenetze
- Förderhöhe abhängig von erneuerbarem Anteil
- Modul 1: Studie / Konzept
- Modul 2: Investition
- Modul 3: Betrieb (erste Jahre)

### Voraussetzungen

- Mindest-Anteil erneuerbarer Wärme
- Transformationsplan zu Klimaneutralität
- Verbindlicher Anschluss-Plan

### Antragsverfahren

- KfW-Online-Portal
- Vor Vorhabenbeginn
- Beratung Energieagentur empfohlen

### Streit-Konstellation

- Bewilligung verweigert
- Klage VG Köln (KfW-Sitz) oder VG Frankfurt am Main
- Widerruf rückwirkend bei Verstoß

## Schritt 6 — GEG Reform 01.01.2024

### 65%-EE-Pflicht bei neuen Heizungen

- Neuanlagen in Bestandsgebäuden / Neubau
- Mindestens 65 % erneuerbare Energie
- Übergangsregelungen bei Wärmeplanung-Pflicht (Auslauf bis 30.06.2026/2028)

### Erfüllungs-Optionen

a) Wärmepumpe
b) Anschluss Fernwärme (mind. 65 % EE)
c) Stromdirektheizung (bei niedrigem Wärmebedarf)
d) Biomasse-Heizung (mit Pflichten)
e) Solarthermie-Hybrid
f) Wasserstoff-Heizung (eingeschränkt)

### Beratungsgespräch § 71 GEG

- Vor Heizungs-Tausch
- Energieberater oder ähnlich

### Übergangsregelungen

- Defekte Heizungen können noch repariert / ersetzt werden mit fossil-basierten Lösungen
- Verpflichtende Beratung
- Aussetzungs-Möglichkeit bei besonderen Härte-Fällen

## Schritt 7 — Quartiers-Konzepte integriert

### Konzept-Bestandteile

- Wärme-Erzeugung (zentral / dezentral)
- Wärme-Verteilung (Netz / direkt)
- Stromversorgung (Mieterstrom, PV-Anlagen, BHKW)
- Mobilität (Lade-Infrastruktur, Carsharing)
- Speicher (Batterie, Wärmespeicher)

### Vertrags-Architektur

- Mehrere Verträge je Anschluss-Nehmer
- Quartiers-Manager als Gesellschaftsform
- AGB-Kontrolle aller Vertragsbestandteile

### Beihilfe-Rechtliche Aspekte

- Kommunale Quartiers-Förderung als Beihilfe?
- De-minimis-Grenze prüfen
- EU-Beihilfen-Recht

## Schritt 8 — Wärmeliefer-Vertrag Volltext (Beispiel-Bausteine)

### Wesentliche Klauseln

- **Vertragsdauer** typisch 10 Jahre + Verlängerung
- **Anschluss-Werte** (Anschluss-Wert in kW, Jahresleistung in MWh)
- **Preisformel** mit transparenten Indizes
- **Versorgungs-Pflichten** und Ausnahmen (höhere Gewalt)
- **Mängelhaftung** bei Ausfall
- **Anpassungs-Klauseln** Versorgungs-Bedingungen
- **Kündigungs-Modalitäten**
- **Anschluss- und Benutzungs-Zwang** Bezug Satzung

### AGB-Kontrolle

- Bei Standard-Klauseln Anwendung §§ 305 ff. BGB
- Bei Verbraucher / Klein-Unternehmen strenger
- BGH-Linien aus 2024

## Schritt 9 — Streit-Strategien

### Mandant = Anschluss-Nehmer (Eigentümer)

1. AuB-Satzung prüfen (Normenkontrolle)
2. Preisanpassungs-Klausel prüfen (AGB-Kontrolle)
3. Mängel-Anzeige bei Ausfall
4. Bei Insolvenz Versorger: Ersatz-Versorgung sichern

### Mandant = Fernwärme-Versorger

1. Klausel-Wirksamkeit absichern (Transparenz-Pflicht)
2. Preisanpassungs-Information ordnungsgemäß
3. AuB-Satzung mit Gemeinde abstimmen
4. Wärmeplanung-Einbindung

### Mandant = Kommune

1. Wärmeplanung-Frist im Auge
2. Beteiligungsverfahren ordnungsgemäß
3. AuB-Satzung verhältnismäßig
4. Förderprogramme BEW maximal nutzen

### Mandant = Mieter

1. Mieterstrom-Vertrag prüfen
2. Heizkosten-Abrechnung kontrollieren
3. Wahlrecht Lieferant sicherstellen

## Aktuelle Rechtsprechung & Leitsätze

- BGH, Urt. v. 24.03.2021 — VIII ZR 263/19, NJW 2021, 1596 — Fernwaerme-Preisanpassungsklausel; Spotpreis-Indizierung an Gaspreis-Index haelt AGB-Kontrolle stand wenn transparent und nachvollziehbar; Versorgungsunternehmen traegt Beweislast fuer Billigkeit § 315 BGB
- BGH, Urt. v. 06.07.2022 — VIII ZR 155/21, NJW 2022, 2490 — Anschluss-und-Benutzungszwang Fernwaerme nach kommunalem Satzungsrecht; Verhaeltnismaessigkeit gegenueber Grundrecht auf Eigentumsfreiheit Art. 14 GG; staedtebauliche Klimaschutz-Ziele als legitimer Zweck anerkannt
- OLG Muenchen, Urt. v. 12.10.2023 — 14 U 2043/22, ZNER 2023, 388 — GEG-Pflicht 65 % Erneuerbare beim Heizungs-Ersatz; keine rueckwirkende Anwendung auf bestehende Heizungsanlagen; Uebergangsfristen nach WPG beachten
- VG Frankfurt/Main, Urt. v. 25.05.2023 — 8 K 1344/22.F, juris — kommunale Waermeplanung WPG; Pflicht der Gemeinde zur Erstellung Waermeplan bis 30.06.2026; keine Ermessens-Entscheidung; Klage eines Anschlussnehmer-Verbands auf Vorlage des Plans zulaessig

## Zentrale Normen (Paragrafenkette)

§§ 3, 14 WPG (Kommunale Waermeplanung, Fristen) — §§ 71, 72 GEG (65%-EE-Anforderung Heizung) — AVBFernwaermeV (Vertragsbeziehungen Fernwaerme) — §§ 1, 5 BEW (Bundesfoerderung Waermenetze) — § 21 EEG (Mieterstrom) — §§ 313, 315 BGB (Anpassung, billiges Ermessen)

## Kommentarliteratur

- Britz/Hellermann/Hermes, EnWG, 4. Aufl. 2022, §§ 17b-17d Rn. 1 ff. (Waermenetz-Anschluss, Fernwaerme-Regulierung)
- Grüneberg (Palandt), BGB, 83. Aufl. 2024, § 315 Rn. 1 ff. (billiges Ermessen Fernwaerme-Preisanpassung)

## Verzahnung

- `energierecht-vertrieb-marktrollen` — Mieterstrom-Vertrieb
- `energierecht-projektfinanzierung` — Wärmenetz-Finanzierung
- `energierecht-verfahren` — BNetzA / VG-Klage
- `normenkontrolle-bauleitplanung` — Wärmeplan / B-Plan
- `fachanwalt-miet-wohnungseigentumsrecht` — Mieter-Aspekte

## Quellen

- WPG 01.01.2024
- AVBFernwärmeV
- GEG (Gebäudeenergiegesetz, Reform 01/2024)
- EnWG § 42a
- EEG § 21
- BGB §§ 305 ff. AGB-Kontrolle
- BVerwG 7 C 32.94 (AuB-Verhältnismäßigkeit)
- BGH VIII ZR 263/22 (Preisanpassungs-Klauseln Fernwärme)
- BGH VIII ZR-Linie zu Tarifen
- KfW-BEW-Förderrichtlinie 442
- BMWK-Hinweise Wärmeplanung
- Bayerische, NRW, Hessische GO-Vorschriften zu AuB-Satzung
