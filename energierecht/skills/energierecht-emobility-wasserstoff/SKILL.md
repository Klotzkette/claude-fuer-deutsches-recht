---
name: energierecht-emobility-wasserstoff
description: "Emobility Wasserstoff: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Emobility Wasserstoff

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Emobility Wasserstoff** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `energierecht-emobility-wasserstoff` | Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: § 14a EnWG, EEG, GEG, EU-Verordnung Alternative Kraftstoffe. Prüfraster: Netzintegration, Foerderrecht, Liefervertrag, Regulierungsrahmen. Output: Regulierungsrahmen E-Mobilitaet und Wasserstoff. Abgrenzung: nicht allgemeines Netzrecht. |
| `energierecht-energievertraege` | Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Prüfraster: Preisanpassungsklauseln, Laufzeiten, Sonderkündigungsrecht, Lieferbedingungen. Output: Vertragsprüfergebnis oder Vertragsentwurf. Abgrenzung: nicht Netzanschlussvertrag. |
| `energierecht-industriekunden` | Sonderregelungen für Industriekunden im Energierecht: Netzentgeltbefreiungen, Direktleitungen, Eigenerzeugung. Normen: § 19 StromNEV, §§ 17 ff. EnWG, EEG. Prüfraster: atypische Netznutzung, Eigenversorgungsprivileg, Konzerneigenversorgung. Output: Industriekunden-Beratungsmemo. Abgrenzung: nicht Haushaltskunden-Grundversorgung. |
| `energierecht-infrastrukturprojekte` | Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff. EnWG, NABEG, BImSchG, BauGB. Prüfraster: Genehmigungsverfahren, Einwendungen, Planfeststellungsbeschluss, Enteignungsrecht. Output: Genehmigungsverfahrens-Roadmap Energieinfrastruktur. Abgrenzung: nicht Netz- oder Speicherzulassung. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **Emobility Wasserstoff**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `energierecht-emobility-wasserstoff`

**Fokus:** Rechtliche Rahmenbedingungen für Elektromobilitaet und gruenen Wasserstoff prüfen: Ladepunkte, H2-Einspeisung. Normen: § 14a EnWG, EEG, GEG, EU-Verordnung Alternative Kraftstoffe. Prüfraster: Netzintegration, Foerderrecht, Liefervertrag, Regulierungsrahmen. Output: Regulierungsrahmen E-Mobilitaet und Wasserstoff. Abgrenzung: nicht allgemeines Netzrecht.

# E-Mobilität und Wasserstoff

## Zweck

Behandelt die beiden Wachstums-Felder Ladeinfrastruktur (E-Mobilität) und Wasserstoff-Wirtschaft. Recht ist im starken Wandel — RED III, AFIR, BEHG, KSchV-CCfD.

## Eingaben

- Mandant (Ladeinfrastruktur-Betreiber, H2-Projektgesellschaft, Industrie, Versorger)
- Projekt-Phase (Konzept, Genehmigung, Aufbau, Betrieb)
- Standort und Anschluss-Werte
- Förderprogramme angefragt / beantragt
- Verzahnung mit Strombezug und Erzeugung

## Schritt 1 — Ladeinfrastruktur Recht-Rahmen

### LSV (Ladesäulenverordnung) 2023

- Mindest-Standards Ladesäulen öffentlich
- Roaming-Pflicht: jeder Ladepunkt mit Drittanbietern abrechnungsfähig
- Mess- und Eichrecht: Pflicht zur geeichten Messung pro Ladevorgang
- Authentifizierungs-Optionen (App, RFID, Kreditkarte ab 2024)

### AFIR (Alternative Fuels Infrastructure Regulation, VO 2023/1804)

- EU-Verordnung seit 13.04.2024 in Kraft
- Mindest-Dichte Ladepunkte je Streckenkilometer (TEN-T-Korridore)
- Schnelllade-Park-Standards
- Bedienungs-Vereinheitlichung

### Mess- und Eichrecht

- Mess- und Eichgesetz (MessEG)
- Geeichte Messung Kilowattstunden pro Ladevorgang
- Sonderregelungen Eich-Übergang
- BMR (Bundesamt für Messwesen) Aufsicht

## Schritt 2 — Ladeinfrastruktur-Förderung

### Förderprogramme

- **KfW-Förderung Wallbox privat** historisch (ausgelaufen 2024)
- **BMVI / BMDV-Förderung** öffentliche Ladesäulen Schnelllader
- **Bundesförderung Ladeinfrastruktur II** (LIS II)
- **Länderprogramme** (Bayern, NRW, BW spezifisch)

### Antragsverfahren

- Vor Vorhabensbeginn
- Antragsformulare BAFA / BAV
- Beleg-Pflichten

### Compliance

- Mindest-Betriebs-Dauer (typisch 5 Jahre)
- Roaming-Pflicht (AFIR)
- Daten-Übermittlung Ladevorgänge

## Schritt 3 — Standortwahl Ladeinfrastruktur

### Genehmigungs-Bedarf

- Bauantrag bei größeren Anlagen
- Stellplatz-Anrechnung Bauordnungsrecht
- Verkehrsrechtliche Anordnungen

### Netzanschluss

- Anschluss-Werte oft hoch (Schnelllader 150-350 kW)
- Stationäre Speicher als Last-Glättung
- Netzentgelt-Optimierung

### Eigentums-/Pacht-Verhältnisse

- Standorte häufig auf Pachtbasis
- Tankstellen-Konstellationen mit klassischem Mineralöl-Anbieter
- Parkhaus-/Supermarkt-Standorte

## Schritt 4 — THG-Quote § 37a BImSchG

### Konzept

- Treibhausgas-Minderungs-Quote für Kraftstoff-Lieferanten
- Ladestrom (E-Auto) wird angerechnet
- Vermarktung der Quote über THG-Quoten-Pool-Anbieter

### Anwendung

- Anlagen-Betreiber öffentlicher Ladepunkte
- Privater Wallbox-Betreiber (über Pool-Anbieter)
- Erstattungs-Beträge variabel je Marktlage

### Verwaltungsverfahren

- UBA als Behörde
- Antragsfristen jährlich
- Skill `umweltrecht-emissionshandel-tehg` bei größeren Strukturen

## Schritt 5 — Wasserstoff-Wirtschaft

### Hierarchie der Wasserstoff-Erzeugungs-Pfade

- **Grüner H2**: Elektrolyse mit erneuerbarem Strom → RED III-konform
- **Türkiser H2**: Methan-Pyrolyse mit Kohlenstoff-Sequestrierung
- **Blauer H2**: Erdgas-Reformierung mit CCS (Carbon Capture and Storage)
- **Grauer H2**: Konventionelle Methan-Reformierung (nicht förderfähig)

### RED III Erneuerbarkeits-Kriterien

- Direkte Verbindung zwischen Elektrolyseur und EE-Anlage
- Oder: Stundengleichheit (ab 2030 strenger)
- Oder: Bilanzkreis-Methode mit zusätzlichkeit
- Delegierter Akt EU 2023/1184 als Konkretisierung

### Förderung Elektrolyseure

- **KfW BEW** im Wärme-Bezug
- **EEG-Innovationsausschreibung** für Hybrid-Anlagen
- **Klimaschutzverträge (CCfD)** Differenzvertrag für Wasserstoff-Produzenten
- **Wasserstoff-Beschleunigungs-Gesetz** geplant

### Antragsverfahren

- BAFA als Hauptbehörde
- Förder-Dokumentation umfangreich
- Audit-Pflichten

## Schritt 6 — H2-Netz und H2-Stammnetz

### Wasserstoff-Stammnetz § 28r EnWG

- Bundesweites H2-Stammnetz
- Kombination Neu-Bau und Erdgas-Netz-Umstellung
- Genehmigung Bundesfachplanung

### Hochlauf-Phase (Wasserstoff-Hochlaufgesetz)

- Übergangsweise Erdgas-Anteil im H2-Netz möglich
- Förderung Aufbau-Phase

### Bundesnetzentwicklungsplan H2 (BNEP)

- 4-Jahres-Zyklus
- Bedarfs-Identifikation
- BNetzA-Festlegung

## Schritt 7 — H2-Anlagen-Genehmigung

### BImSchG-Genehmigung

- Elektrolyseure > 10 MW: § 4 BImSchG förmliches Verfahren
- Druckwasserstoff-Speicher
- Sicherheits-Anforderungen ATEX-Richtlinie

### Bauleitplanung-Bezug

- Wasserstoff-Tankstellen-Standorte
- Industrielle H2-Anlagen
- Konflikte mit Wohnbebauung

### Strom-Bezug

- Direktversorgung aus EE-Anlage bevorzugt
- PPA-Struktur
- Bilanzkreis-Strukturen

## Schritt 8 — Förderung-Konkurrenz

### Klimaschutzverträge (Carbon Contracts for Difference)

- Differenzvertrag zwischen Bund und Industrie
- Anreiz für Dekarbonisierung
- Auch für H2-Produzenten / -Verbraucher

### Industrie-Strompreis-Diskussion

- Politisch fortlaufend
- Skill `energierecht-industriekunden`

### Wasserstoff-Importe

- H2-Strategie Bundesregierung sieht erhebliche Importe
- Internationale Lieferverträge
- Anrechnungs-Mechanismus RED III

## Schritt 9 — BEHG (Brennstoffemissionshandel)

### Anwendungs-Bereich

- Verkehr und Wärme (außer ETS-pflichtig)
- CO2-Preis ansteigend (2024: 45 €/t)
- Quote für Brennstoffe-Lieferant

### Folge für E-Mobilität

- Indirekter Preis-Druck auf Verbrennungs-Pkw
- E-Auto wirtschaftlich attraktiver

### Folge für Wasserstoff

- Grauer / blauer H2 indirekt CO2-belastet
- Grüner H2 begünstigt

## Schritt 10 — Mandanten-Strategie

### Ladeinfrastruktur-Betreiber

1. Standortwahl strategisch
2. AFIR-Compliance sicherstellen
3. Mess- und Eichrecht
4. Förder-Programm beantragen
5. THG-Quoten-Optimierung

### H2-Projektgesellschaft

1. RED III-Konformität für grünen H2
2. Strom-Bezug PPA / EE-Anlage direkt
3. BImSchG-Genehmigung vorbereiten
4. KfW BEW / CCfD beantragen
5. Industrie-Abnehmer-Vertrag absichern

### Industrie-Mandant

1. H2-Versorgungs-Vertrag mit Lieferant
2. CCfD-Beteiligung
3. CBAM-Aspekte
4. Skill `energierecht-industriekunden`

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 37a BImSchG (THG-Quote) — §§ 7 ff. LSV (Ladesaeulenverordnung) — Art. 3 AFIR 2023/1804 (Mindestanforderungen Ladeinfrastruktur) — §§ 2, 6 MessEG (Eichrecht) — §§ 1, 5 EEG (Erneuerbarkeits-Kriterien RED III) — § 28 EnWG (Wasserstoff-Netz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-eeg-kwkg-erzeugung` (Elektrolyseure-Strom)
- `energierecht-netz-speicher-zugang` (Anschluss Ladeinfrastruktur)
- `energierecht-projektfinanzierung` (KfW BEW / CCfD)
- `energierecht-industriekunden` (H2-Abnehmer)
- `umweltrecht-immissionsschutz-bimschg` (BImSchG-Verfahren)
- `umweltrecht-emissionshandel-tehg` (ETS / BEHG)

## Quellen

- EnWG §§ 17, 28r ff. (H2-Netz), 42a
- LSV (Ladesäulenverordnung 2023)
- AFIR VO (EU) 2023/1804
- MessEG / MessEV
- BImSchG §§ 4, 37a
- BEHG
- RED III Richtlinie 2023/2413/EU + delegierter Akt 2023/1184
- BAFA / KfW Förderrichtlinien
- Klimaschutzvertrags-Programm BMWK
- H2-Stammnetz-Beschluss BNetzA
- UBA THG-Quoten-Verwaltung
- BVerwG-/EuGH-Linien zu E-Mobilität (begrenzt)

## 2. `energierecht-energievertraege`

**Fokus:** Energieliefervertraege prüfen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Prüfraster: Preisanpassungsklauseln, Laufzeiten, Sonderkündigungsrecht, Lieferbedingungen. Output: Vertragsprüfergebnis oder Vertragsentwurf. Abgrenzung: nicht Netzanschlussvertrag.

# Energie-Verträge — Strukturierung und Prüfung

## Zweck

Behandelt die Vertrags-Architektur im Energie-Bereich: Liefer-Verträge Strom / Gas / Wärme, Bilanzkreis-Verträge, Konzessions-Verträge, Industrie-Sonderverträge, PPA-Verträge. Inkl. AGB-Kontrolle und Anpassungs-Klauseln.

## Eingaben

- Vertrags-Typ (Strom / Gas / Wärme / Konzession / Bilanzkreis / PPA)
- Mandant-Rolle (Anbieter / Käufer / Netzbetreiber / Kommune)
- Vertrags-Phase (Verhandlung / Bestand / Streit / Migration)
- Konkrete Streit-Punkte
- AGB-Standard oder Verhandlungs-Vertrag

## Schritt 1 — Stromlieferungs-Vertrag Strukturen

### Standard-Haushaltskunden

- Grundversorgungs-Vertrag (StromGVV)
- Sondervertrag mit Wahl-Lieferant
- Tarif-Übersicht und AGB

### Gewerbe-/Industrie-Kunden

- Sondervertrag mit Anlagen-bezogenen Konditionen
- Tarif-Strukturen (Festpreis, Index, Hybrid)
- Bandlast vs. Last-Profil-Kunde

### Kern-Vertrags-Klauseln

```
1. Vertrags-Parteien und Anlagen-Bezug
2. Vertrags-Beginn und Dauer
3. Liefer-Mengen / Anschluss-Werte
4. Preisformel
5. Anpassungs-Klauseln
6. Bilanzkreis-Zuordnung
7. Force-Majeure / Höhere Gewalt
8. Mängelhaftung
9. Kündigungs-Modalitäten
10. Sicherheiten und Zahlungsbedingungen
11. Vertraulichkeit
12. Gerichtsstand / Schiedsklausel
```

### AGB-Kontrolle

- §§ 305 ff. BGB
- Bei Haushaltskunden besonders streng
- Bei Industrie-Sondervertrag Verhandlungs-Vertrag möglich
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 2 — Preisanpassungs-Klauseln

### Standard-Anforderungen

- **Transparenz** — Anpassungs-Faktor verständlich
- **Bezugnahme auf nachvollziehbare Indizes** (EEX-Preis, Basispreis-Plus, Inflation)
- **Cost-Reflektion** — Anpassung muss tatsächlich Kostenelement abbilden
- **Sonderkündigungs-Recht** bei Anpassung

### Wirksamkeits-Kriterien BGH

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Häufige Klausel-Fehler

- **Spotpreis-Indizierung** ohne Bezug zum Lieferanten-Bedarf
- **Einseitige Anpassungs-Recht** ohne Begründungs-Pflicht
- **Fehlende Cap-Mechanismen** bei extremen Markt-Schwankungen
- **Intransparente Bezugnahmen**

### Folge Unwirksamkeit

- Ausgangs-Preis bleibt
- Rückforderungs-Anspruch Kunden (Verjährung 3 Jahre)
- Schaden für Versorger erheblich

## Schritt 3 — Bilanzkreis-Vertrag

### Vertrags-Parteien

- Übertragungs-Netzbetreiber als Bilanzkreis-Manager
- Bilanzkreis-Verantwortlicher (BKV)

### Inhalte

- Bilanzkreis-Definition (Abgrenzung)
- Ausgleichsenergie-Mechanismus
- Sicherheits-Hinterlegung (oft 6-stelliger Euro-Betrag)
- Sanktion bei nicht-eingelieferten Daten
- Sicherheiten

### Bei Insolvenz BKV

- Bilanzkreis-Auflösung
- Übergang an Standard-BKV
- Kunden bleiben versorgt

## Schritt 4 — Konzessions-Vertrag § 46 EnWG

### Konzept

- Kommune vergibt Wege-Recht (Strom-/Gas-Verteilnetz)
- Konzessionsabgabe ab Endverbraucher
- Vertragsdauer max. 20 Jahre

### Vergabe-Verfahren

- Konzessions-Wettbewerb
- Diskriminierungs-Verbot
- Auswahl-Kriterien BNetzA-Festlegung

### Streit-Konstellationen

- Konkurrenten-Klage gegen Vergabe
- Konzessions-Abgabe-Streit
- Übernahme-Recht der Kommune (Re-Kommunalisierung)

### BGH-Linie

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BGH EnVR-Linie zu Übernahme-Bedingungen

## Schritt 5 — Industrie-Sondervertrag

### Verhandlungs-Vertrag

- Keine AGB-Standard
- Individuelle Konditionen je Anlagen-Profil
- Sicherheiten / Zahlungsbedingungen anlagen-spezifisch

### Sondereinrichtungen

- Bandlast-Privileg § 19 StromNEV
- Strompreiskompensation-Mit-Einbringung
- Atypisches Verbrauchsverhalten

### Risiko-Verteilung

- Strommarkt-Risiko-Übergang
- Brennstoff-Preis-Risiko (Gas)
- CO2-Preis-Risiko
- Regulierungs-Risiko (EEG-Umlage-Reform etc.)

### Vertragsanpassungs-Klauseln (Hardship-Clauses)

- Bei wesentlicher Änderung Marktverhältnisse
- Bei rechtlicher Änderung
- Anpassungs-Verhandlung

## Schritt 6 — Wärmeliefer-Vertrag (AVBFernwärmeV)

Siehe ausführlich Skill `energierecht-waerme-quartier`.

Kern-Punkte hier:

- AVBFernwärmeV als Standard-AGB
- Preisanpassungs-Klauseln nach § 24 Abs. 4 AVBFernwärmeV
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Vertragsdauer max. 10 Jahre + Verlängerung

## Schritt 7 — Mieterstrom-Vertrag

Siehe Skill `energierecht-waerme-quartier` und `energierecht-vertrieb-marktrollen`.

Kern-Punkte:

- EnWG § 42a Mieterstrom-Definition
- Anbieter unterliegt erleichtertem Regime
- Mieter behält Wahlrecht zu anderem Lieferanten
- Vertragsdauer ohne unangemessene Bindung

## Schritt 8 — Vertrags-Migration in Krisen-Zeiten

### Energie-Krise 2022/2023 als Lehrbeispiel

- Massive Preis-Erhöhungen
- Lieferanten-Insolvenzen
- Ersatzversorgung
- Strompreis-/Gaspreis-Bremse 2023

### Vertrags-Reaktion

- Sonderkündigungs-Recht
- Anpassungs-Klauseln aktiviert
- Hardship-Klauseln

### Aktuelle Anwendung

- Nachlauf-Streitigkeiten 2024-2025
- Klage-Wellen über Preisanpassungs-Klauseln
- BGH-Linien stabilisieren

## Schritt 9 — ESG-Verzahnung

### CSRD-Bezug

- Energie-Vertrag Bestandteil ESG-Reporting
- Stromherkunft im Vertrag dokumentieren
- HKN-Lieferung absichern

### Greenwashing-Risiko

- Bei "Ökostrom" ohne HKN-Belege
- UWG-Streit
- Skill `esg-greenwashing-csrd` im Umweltrecht

### CBAM-Auswirkungen

- Indirekt über CO2-Bepreisung Strom
- Vertrags-Anpassungen Industrie-Käufer

## Schritt 10 — Mandanten-Strategie

### Versorger / Lieferant

1. AGB-Audit regelmäßig
2. Preisanpassungs-Klausel-Wirksamkeit absichern
3. Transparenz-Pflichten erfüllen
4. ESG-Reporting CSRD-konform
5. Bilanzkreis-Management strict

### Industrie-Kunde

1. Vertrags-Verhandlung mit Spezialist
2. Risiko-Verteilung optimieren
3. Hardship-Klauseln einbauen
4. Bei Streit AGB-Kontrolle aktiv nutzen

### Kommune (Konzessions-Vergabe)

1. Vergabe-Verfahren EU-konform
2. Übernahme-Optionen sichern
3. Klima-Aspekte einbringen

### Endkunde

1. AGB prüfen vor Vertragsschluss
2. Bei Anpassungs-Mitteilung Plausibilität prüfen
3. Bei Wechsel Vertrags-Übergangs-Modalitäten

## Aktuelle Rechtsprechung & Leitsätze (Stand 05/2026, verifiziert dejure.org / curia.europa.eu)

- **EuGH 23.10.2014, C-359/11 (Schulz)**: Preisanpassungsklauseln in Strom-/Gaslieferungsvertraegen nach AVBEltV/GVV — Aenderungen muessen rechtzeitig mitgeteilt werden, Verbraucher muss Kuendigungsrecht haben. Quelle: curia.europa.eu (CELEX 62011CJ0359).
- **BGH 28.10.2015, VIII ZR 158/11**: Preisanpassung Energielieferungsvertrag — § 5 Abs. 2 GasGVV Transparenz-Anforderungen; AGB-Kontrolle § 307 BGB. Quelle: dejure.org/2015,33580.
- **BGH 24.03.2010, VIII ZR 178/08**: Preisaenderungsklauseln in Sondervertraegen Strom/Gas — wirksame Indexbindung erfordert klare Berechnungsformel. Quelle: dejure.org/2010,5874.
- **BGH 09.02.2011, VIII ZR 295/09**: Billigkeit der Leistungsbestimmung § 315 BGB; Beweislast Versorger fuer Billigkeit. Quelle: dejure.org/2011,4286.
- **EuGH 02.09.2021, C-718/18**: Unabhaengigkeit der Bundesnetzagentur als Regulierungsbehoerde. Quelle: curia.europa.eu.

**Gesetzeslage 2026:** EnSiG (Energiesicherungsgesetz) — § 24 Anpassungsklauseln bei Gasmangellage (BGBl. I 2022 S. 1054); EnWG-Novellen 2023/2024.

Weitere Aktenzeichen vor Ausgabe per dejure.org / curia.europa.eu verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 315 BGB (billiges Ermessen Leistungsbestimmung) — §§ 305-310 BGB (AGB-Kontrolle) — §§ 36-38 EnWG (Grundversorgung) — § 46 EnWG (Konzessionsvertrag) — AVBEltV / AVBFernwaermeV (Vertragsbeziehungen Grundversorgung) — §§ 313, 314 BGB (Stoerung Geschaeftsgrundlage, Hardship)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-vertrieb-marktrollen`
- `energierecht-waerme-quartier`
- `energierecht-industriekunden`
- `energierecht-projektfinanzierung` (PPA)
- `esg-greenwashing-csrd`
- `fachanwalt-bank-kapitalmarktrecht`

## Quellen

- BGB §§ 305 ff. AGB-Kontrolle
- EnWG §§ 36-42a, § 46 (Konzession)
- StromGVV / GasGVV
- AVBFernwärmeV
- EEG § 21 Mieterstrom
- EuGH C-359/11 (Schulz, 23.10.2014); BGH VIII ZR 158/11 (28.10.2015); BGH VIII ZR 178/08 (24.03.2010); BGH VIII ZR 295/09 (09.02.2011); EuGH C-718/18 (02.09.2021)
- DIS / ICC Schieds-Standards
- Schiedsstelle Energie

## 3. `energierecht-industriekunden`

**Fokus:** Sonderregelungen für Industriekunden im Energierecht: Netzentgeltbefreiungen, Direktleitungen, Eigenerzeugung. Normen: § 19 StromNEV, §§ 17 ff. EnWG, EEG. Prüfraster: atypische Netznutzung, Eigenversorgungsprivileg, Konzerneigenversorgung. Output: Industriekunden-Beratungsmemo. Abgrenzung: nicht Haushaltskunden-Grundversorgung.

# Industriekunden — Sonderregelungen

## Zweck

Industriekunden mit hohem Stromverbrauch haben eine Reihe von Sonder-Privilegierungen und entsprechenden Pflichten. Dieser Skill systematisiert.

## Eingaben

- Mandant: Industriekunde
- Stromverbrauch jährlich (MWh)
- Vollbenutzungsstunden
- Branche (energie-intensiv-Liste FFL?)
- Bestehende Privilegierungen (BesAR-Bescheid, § 19 StromNEV-Bescheid)
- Anlagen-Eigenerzeugung

## Schritt 1 — § 19 Abs. 2 Satz 2 StromNEV Bandlast-Privileg

### Tatbestand

Reduzierung des Netzentgelts wenn

- **Vollbenutzungsstunden ≥ 7.000 h/Jahr** und
- **Jahresverbrauch ≥ 10 GWh**

### Reduzierungs-Stufen

| Vollbenutzungsstunden | Netzentgelt-Anteil |
|---|---|
| 7.000 — 7.499 h | 20 % |
| 7.500 — 7.999 h | 15 % |
| ≥ 8.000 h | 10 % |

### Antragsverfahren

- **Antrag bis 30.09. für das Folgejahr** beim Netzbetreiber
- BNetzA-Festlegung BK4-21-049 zu Anwendungs-Modalitäten
- Bei Versäumnis: kein rückwirkender Anspruch

### Voraussetzungen-Prüfung

- Vergangener Verbrauch nachweisen
- Prognose-Verbrauch realistisch
- Bei Unterschreiten Rückforderungs-Risiko

### Historischer Streit

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Neufassung 2023
- Rückforderungs-Welle bei Bestandsanlagen

## Schritt 2 — § 19 Abs. 1 StromNEV atypisches Verbrauchs-Verhalten

### Anwendungs-Bereich

- Verbrauch außerhalb der Jahres-Spitzenzeiten
- Last-Verschiebung nachgewiesen
- Reduzierte Netzentgelte

### Verhandlungs-Spielraum

- Individuelles Netzentgelt mit Netzbetreiber
- BNetzA-Genehmigungs-Vorbehalt
- Häufig komplexere Tarif-Modelle

## Schritt 3 — Strompreiskompensation (Carbon Leakage)

### Hintergrund

- Indirekte CO2-Kosten im Strompreis durch ETS
- Energie-intensive Industrien (CO2-Leakage-Branchen) bekommen Kompensation
- BMWK / BAFA als Behörde

### Voraussetzungen

- Branche auf FFL-Liste (Förderfähigkeits-Liste)
- Stromintensität nachweisen
- ETS-CO2-Preis-Bezug

### Antragsverfahren

- **Antrag jährlich bei BAFA**
- Frist regelmäßig 30. April Folgejahr
- Dokumentations-Pflicht umfangreich

### Reform 2024/2025

- Strompreiskompensation läuft fort, Volumen schrittweise sinkend
- Industrie-Strompreis-Diskussion politisch (CO2-Differenzverträge Klimaschutzverträge CFD)

## Schritt 4 — Klimaschutzverträge (Carbon Contracts for Difference, CCfD)

### Konzept

- Differenzvertrag zwischen Industrie und Bund
- Bund garantiert CO2-Preis-Ergänzung wenn ETS-Preis unter Vereinbarung
- Anreiz für Dekarbonisierung in energieintensiver Industrie

### Förderaufruf 2023/2024

- 4 Mrd. € erstes Förderaufrufs-Volumen
- BAFA-Antrag
- KMU-Bonus

### Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 19 Abs. 1, Abs. 2 StromNEV (Sondernetzentgelte) — § 8 EDL-G (Energie-Audit) — § 10 EWPG / EnEfG (Energieeffizienz-Pflicht) — §§ 3 ff. KWKG (KWK-Strompreiskompensation) — Art. 2 ff. CBAM-VO 2023/956 (Carbon Border Adjustment Mechanism)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- Mit Strompreiskompensation
- Mit EEG/KWKG-Vermarktung

## Schritt 5 — Energie-Audit § 8 EDL-G

### Pflicht

- Energie-intensive Unternehmen jährlich
- Zertifikatsstelle BAFA-Zugang
- Bußgeld bei Nicht-Durchführung

### Audit-Inhalte

- Verbrauchs-Analyse alle Standorte
- Maßnahmen-Vorschläge
- Wirtschaftlichkeits-Berechnungen

### Befreiung

- Bei Anwendung ISO 50001 + Audit-Verifikation
- Reduziert Prüf-Last

## Schritt 6 — EnEfG (Energie-Effizienzgesetz, seit 17.11.2023)

### Pflichten Unternehmen ab 7,5 GWh/Jahr

- Energie- oder Umwelt-Management-System
- Plan zur Hebung wirtschaftlich-realisierbarer Endenergie-Einsparungen
- Pflicht-Maßnahmen-Listen

### Sanktionen

- Bußgeld bis 100.000 € (Sanktionsstaffel BAFA)
- Aufsichts-Anordnungen

### Verzahnung mit GEG und ETS

- Anrechnungs-Mechanismen
- Maßnahmen-Plan integrierbar

## Schritt 7 — PPA Corporate Direct

### Strukturierungs-Varianten

#### Physisches PPA

- Strom-Lieferung Anlage → Industriekunde direkt
- Bilanzkreis-Strukturen
- On-Site (Anlage auf Industrie-Gelände) oder Off-Site

#### Finanzielles PPA (Synthetic PPA)

- Strom-Lieferung an Markt
- Differenz-Zahlungen zwischen Festpreis und Marktpreis
- Bilanz-rechtlich anders strukturiert

### Vorteile Industrie

- Langfristige Preis-Sicherheit
- Grüner Strom-Nachweis (HKN-Lieferung)
- ESG-Reporting CSRD-konform

### Vorteile Anlagen-Betreiber

- Vermarktungs-Sicherheit ohne Markt-Volatilität
- EEG-Förderung-Verzicht möglich (Marktpreis-Vergütung)

### Vertrags-Strukturen

- Laufzeit typisch 10-15 Jahre
- Take-or-Pay-Klauseln
- Volumen-Toleranzbänder
- Force-Majeure-Klauseln
- Kreditrisiko-Absicherung

## Schritt 8 — Eigenerzeugung und § 19 StromNEV

### Eigenerzeugung-Privileg

- Strom für Eigenverbrauch — vermiedene Netzentgelte
- Bei Direktleitung vom Erzeuger zum Verbraucher (gleiches Grundstück / räumlicher Zusammenhang)

### Doppelvermarktung-Verbot

- EEG-geförderter Strom kann nicht zugleich Direktverbrauch + EEG-Förderung erhalten
- § 27a EEG

## Schritt 9 — CBAM (Carbon Border Adjustment Mechanism)

### EU-Verordnung 2023/956

- Stahl, Zement, Aluminium, Düngemittel, Strom, Wasserstoff
- Importeur muss CBAM-Zertifikate kaufen
- Anwendung ab 01.10.2023 Reporting; Zahlungs-Pflicht ab 01.01.2026

### Implikationen für Industrie

- Carbon Leakage-Schutz indirekt
- Anpassung Lieferketten
- Skill `lksg-csddd-lieferkettensorgfalt`

## Schritt 10 — Streit-Konstellationen Industriekunden

### Bei verweigerter Privilegierung

- Bescheid prüfen
- Widerspruch / Klage VG
- Skill `energierecht-verfahren`

### Bei Netzbetreiber-Streit § 19 StromNEV

- Antrag rechtzeitig?
- Voraussetzungen erfüllt?
- BNetzA-Beschwerde § 31 EnWG
- OLG-Beschwerde

### Bei Strompreis-Streit

- AGB-Kontrolle
- Tarif-Anpassungs-Klausel
- Schiedsverfahren

### Bei CO2-/ETS-Bescheid

- DEHSt-Bescheid
- Klage VG Berlin (zentrale Zuständigkeit)
- Skill `umweltrecht-emissionshandel-tehg`

## Schritt 11 — Mandanten-Strategie

### Erstgespräch

1. Verbrauchsprofil und Vollbenutzungsstunden klären
2. Branche FFL-Listen-Prüfung
3. Bestehende Privilegierungen inventarisieren
4. Liefer-Vertrags-Struktur
5. Eigenerzeugung-Pläne

### Fristen-Kalender

- 30.09. § 19 StromNEV-Antrag
- 30.04. Strompreiskompensation BAFA
- Energie-Audit-Termin EDL-G
- ETS-Berichts-Fristen

### Strategie-Optimierung

- PPA-Verhandlung mit langfristiger Preis-Sicherheit
- Eigenerzeugung Solar / Wind / KWK
- EnEfG-Pflichten erfüllen
- CBAM-Compliance

## Verzahnung

- `energierecht-netz-speicher-zugang`
- `energierecht-vertrieb-marktrollen`
- `energierecht-eeg-kwkg-erzeugung`
- `energierecht-projektfinanzierung` PPA-Strukturierung
- `energierecht-transaktionen-dd` bei Erwerb Industrie
- `umweltrecht-emissionshandel-tehg`
- `esg-greenwashing-csrd`

## Quellen

- EnWG 2024 §§ 19, 27, 28, 65
- StromNEV §§ 19 Abs. 1, Abs. 2 Satz 1, Abs. 2 Satz 2
- EDL-G § 8
- EnEfG 17.11.2023
- EEG § 27a (Doppelvermarktung)
- EU-CBAM-VO 2023/956
- EU-ETS-Richtlinie aktualisiert 2023
- BAFA-Merkblätter Strompreiskompensation und Klimaschutzverträge
- BGH EnVR-Linien
- BNetzA BK4-Festlegungen

## 4. `energierecht-infrastrukturprojekte`

**Fokus:** Energieinfrastrukturprojekte rechtlich begleiten: Leitungsgenehmigungen, Planfeststellung, Enteignung. Normen: §§ 43 ff. EnWG, NABEG, BImSchG, BauGB. Prüfraster: Genehmigungsverfahren, Einwendungen, Planfeststellungsbeschluss, Enteignungsrecht. Output: Genehmigungsverfahrens-Roadmap Energieinfrastruktur. Abgrenzung: nicht Netz- oder Speicherzulassung.

# Infrastrukturprojekte und Planfeststellung

## Zweck

Behandelt Großprojekte Energieinfrastruktur: Stromtrassen, Erdgas-Pipelines, LNG-Terminals, H2-Stammnetz, Offshore-Wind. Komplexe Verfahren mit langer Dauer und vielen Beteiligten.

## Eingaben

- Vorhabentyp (Stromtrasse / Gas-Pipeline / LNG-Terminal / Offshore-Wind / H2-Pipeline)
- Mandant (Vorhabenträger / Anlieger / Umweltverband / Behörde)
- Verfahrens-Stand (Bundesfachplanung / Planfeststellung / Bau / Betrieb)
- Behördliche Zuständigkeit (BNetzA / BSH / Land)
- Klage-/Eil-Bedürfnis

## Schritt 1 — EnLAG (Energieleitungsausbaugesetz)

### Anwendungsbereich

- 24 wesentliche Übertragungs-Stromleitungen Bundeskompetenz
- Bestand seit 2009, Aktualisierung über Bundesbedarfsplan

### Verfahren

- Planfeststellung durch zuständige Landesbehörden
- Bundesnetzagentur ggf. eingebunden

### Beschleunigung

- Verkürzte Klage-Fristen (1 Monat statt 1 Jahr)
- Eingeschränkter Rechtsschutz
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 2 — BBPlG (Bundesbedarfsplangesetz)

### Anwendungsbereich

- Bedarfs-Bestätigung großer Energie-Leitungen
- Aktualisierung alle 4 Jahre
- Aktuell: BBP 2024

### Planungs-Ablauf

1. **Bedarfsplan** mit konkreten Vorhaben
2. **Bundesfachplanung** (Korridor-Bestimmung) durch BNetzA
3. **Planfeststellungsverfahren** (konkreter Trassenverlauf) durch BNetzA für vorgebene Trassen

## Schritt 3 — NABEG (Netzausbaubeschleunigungsgesetz)

### Anwendungsbereich

- Übertragungs-Stromleitungen bundesweit (BMK/Pl-NA)
- Sehr lange Strecken über Bundesländer hinweg

### Verfahrens-Phasen

1. **Bundesfachplanung** (§ 4 NABEG) — Korridor-Festlegung
2. **Planfeststellung** (§§ 18 ff. NABEG) — Detail-Trassenführung
3. **Plangenehmigung** statt Planfeststellung in einfachen Fällen
4. **Antragsverfahren** durch BNetzA

### Beschleunigungs-Mechanismen

- Erdkabel-Vorrang (bei bestimmten Konstellationen)
- Vereinfachte Genehmigung von Provisorien
- Verkürzte Klage-Fristen

### Beteiligungsverfahren

- Öffentlichkeits-Beteiligung
- Behörden-Beteiligung
- Anhörungs-Termine

## Schritt 4 — Offshore-Wind-Recht

### Windenergie-auf-See-Gesetz (WindSeeG)

- Bundeszuständigkeit BSH (Bundesamt für Seeschifffahrt und Hydrographie)
- Ausschreibungen für Offshore-Standorte (Flächen-Modell seit 2022)
- Anschluss-Leitungen verantwortet TenneT / 50Hertz

### Planfeststellung BSH

- Verfahren analog NABEG für See-Bereich
- Umwelt-Verträglichkeits-Prüfung
- Artenschutz (Seevögel, Fledermäuse, Schweinswale)
- Klage VG Hamburg

### Anbindungs-Leitungen

- Vom Offshore-Standort zur Küste (HVDC-Konverter)
- Komplexe Bundesfachplanung
- Land-Trassen-Anschluss

## Schritt 5 — Erdgas-Pipelines und LNG-Terminals

### LNG-Beschleunigungsgesetz (2022, im Zuge Energiekrise)

- Sehr starke Verfahrens-Beschleunigung
- Klage-Möglichkeiten eingeschränkt
- Übergangsweise: Direkt-Genehmigung möglich

### Beispiel-Streit

- Anerkannte Umweltverbände gegen Wilhelmshaven-, Brunsbüttel-LNG
- Klimaschutz-Argumentation (BVerfG-Klimaschluss)
- Verbandsklage UmwRG

### EuGH-Bezug

- Bezug zu RePowerEU
- Beihilfen-Recht bei LNG-Subventionen

## Schritt 6 — Wasserstoff-Stammnetz

### Wasserstoff-Beschleunigungs-Gesetz (geplant)

- H2-Netz § 28r ff. EnWG
- Vereinfachte Genehmigung für Umrüstung Erdgas-Pipelines auf H2
- Bedarfsplanung über Bundesfachplanung

### Verfahren

- Bundes-Bedarfsplan H2 (Eingang in BNEP-Strom-Gas-Integration)
- Korridor-Festlegung
- Planfeststellung detailliert

### Streit-Konstellationen

- Anlieger der umgerüsteten Erdgas-Trassen
- Sicherheits-Bedenken Wasserstoff-Druck

## Schritt 7 — Beschleunigungs-Gebiete RED III

### Mitgliedstaat-Pflicht ab 21.02.2026

- Ausweisung von Beschleunigungs-Gebieten für Erneuerbare
- Vereinfachung Genehmigungs-Verfahren
- Standort-Vorprüfung
- Mitgliedstaaten in Deutschland: Länder-Aufgabe

### Auswirkungen Verfahren

- Verkürzte Bearbeitungs-Fristen
- Reduzierte Umwelt-Verträglichkeits-Prüfung
- Bauleitplanung-Bezug

## Schritt 8 — Klagebefugnis und Rechtsschutz

### Anlieger / Grundeigentümer

- Antragsbefugnis bei direkter Betroffenheit
- Enteignungs-rechtlich relevant (Trassen-Servitut)
- Entschädigungs-Ansprüche

### Umweltverbände UmwRG

- § 2 UmwRG-Klagebefugnis
- Beteiligung im Verfahren erforderlich
- Klima- und Naturschutz-Argumentation
- Skill `klimaklagen-verbandsklage-umwrg` im Umweltrecht-Plugin

### Behörden / andere Träger öffentlicher Belange

- Mitwirkungs-Recht im Verfahren
- Eigene Klage-Befugnis eingeschränkt

### Gerichtsweg

- 1. Instanz BVerwG bei NABEG- und EnLAG-Vorhaben (Anteil-Klage)
- BVerwG sonst Revisions-Instanz nach OVG
- Klage-Frist eng (1 Monat in beschleunigten Verfahren)

## Schritt 9 — BVerwG- und EuGH-Linie

### BVerwG-Schlüssel-Urteile

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BVerwG zur Klimaschutz-Berücksichtigung in Planung

### EuGH-Bezug

- C-411/17 zur Umwelt-Verträglichkeits-Prüfung
- C-275/09 (Aarhus-Konvention)
- C-78/14 zur Beteiligungs-Pflicht

### Aktuelle Klimaklage-Linie

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anwendung auf Fossil-Infrastruktur
- LNG- und Pipeline-Streitigkeiten

## Schritt 10 — Mandanten-Strategie

### Vorhabenträger

1. Frühe Bedarfs-Identifikation
2. Bundesfachplanung-Vorbereitung
3. Öffentlichkeits-Strategie
4. Umwelt-Verträglichkeits-Prüfung sorgfältig
5. Bei Klage: Verteidigungs-Strategie BVerwG-Erfahrung

### Anlieger

1. Beteiligungs-Termine wahrnehmen
2. Substantiierte Einwendungen
3. Bei Trassenführung Alternativen vorschlagen
4. Bei Bescheid Klage erwägen
5. Entschädigungs-Anspruch sichern

### Umweltverband

1. Klima- und Naturschutz-Argumentation
2. Verbandsklage vorbereiten
3. Klimaklagen-Linie nutzen
4. Skill `klimaklagen-verbandsklage-umwrg`

## Schritt 11 — Praktische Beschleunigungs-Optionen

### Vorzeitiger Bau-Beginn

- Bei dringend benötigten Vorhaben
- Antragsverfahren BNetzA / Länder
- Risiko Rückbau bei Klage-Erfolg

### Plangenehmigung statt Planfeststellung

- Bei einfacheren Vorhaben
- Schneller, weniger Beteiligung

### Provisorien

- Bei akuten Engpässen
- Auflagen-Begrenzung

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1 ff. NABEG (Bundesfachplanung) — §§ 1 ff. BBPlG (Bundesbedarfsplan) — §§ 1 ff. EnLAG (Energieleitungsausbau) — §§ 72 ff. VwVfG (Planfeststellung) — §§ 3a, 3b UVPG (UVP-Pflicht) — § 2 UmwRG (Verbandsklagebefugnis)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-netz-speicher-zugang`
- `energierecht-eeg-kwkg-erzeugung` (Offshore-Wind)
- `energierecht-emobility-wasserstoff` (H2-Pipeline)
- `klimaklagen-verbandsklage-umwrg` (Umweltrecht)
- `normenkontrolle-bauleitplanung`
- `fachanwalt-verwaltungsrecht` (Klage-Strategie)
- `umweltrecht-verfahren`

## Quellen

- EnLAG / BBPlG / NABEG
- WindSeeG
- LNG-Beschleunigungsgesetz
- Wasserstoff-Beschleunigungs-Gesetz (geplant)
- EnWG § 28r
- UmwRG § 2
- BImSchG §§ 4, 10
- UVPG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BNetzA-Genehmigungs-Beschlüsse
- BSH-Beschlüsse Offshore
- RED III delegierter Akt
