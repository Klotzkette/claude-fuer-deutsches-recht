---
name: energierecht-energievertraege
description: "Energieliefervertraege pruefen und entwerfen: Strom- und Gasliefervertraege mit Industrie- und Privatkunden. Normen: §§ 41 ff. EnWG, StromGVV, GasGVV. Pruefraster: Preisanpassungsklauseln, Laufzeiten, Sonderkuendigungsrecht, Lieferbedingungen. Output: Vertragspruefergebnis oder Vertragsentwurf. Abgrenzung: nicht Netzanschlussvertrag."
---

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
- BGH VIII ZR-Linien

## Schritt 2 — Preisanpassungs-Klauseln

### Standard-Anforderungen

- **Transparenz** — Anpassungs-Faktor verständlich
- **Bezugnahme auf nachvollziehbare Indizes** (EEX-Preis, Basispreis-Plus, Inflation)
- **Cost-Reflektion** — Anpassung muss tatsächlich Kostenelement abbilden
- **Sonderkündigungs-Recht** bei Anpassung

### Wirksamkeits-Kriterien BGH

- BGH VIII ZR 56/08 zu Grund-Tarif-Anpassung
- BGH VIII ZR 191/18 zu Sondervertrags-Anpassung
- BGH VIII ZR 263/22 (Fernwärme, 2024) — Anwendung auf Energie generell

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

- BGH EnVR 25/16 zu Konzessions-Wettbewerb
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
- BGH VIII ZR 263/22 (2024) zu Klausel-Wirksamkeit
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

## Aktuelle Rechtsprechung & Leitsätze

- BGH, Urt. v. 28.10.2015 — VIII ZR 158/11, NJW 2016, 475 — Preisanpassungsklausel in Energievertraegen muss hinreichend bestimmt und transparent sein; einseitiges Leistungsbestimmungsrecht nach § 315 BGB setzt billiges Ermessen voraus; Billigkeitspruefung durch Gericht moeglich
- BGH, Urt. v. 24.03.2021 — VIII ZR 263/19, NJW 2021, 1596 — AGB-Klauseln in Energievertraegen zur Spotpreis-Indizierung von Fernwaerme-Preisen halten AGB-Inhaltskontrolle stand, wenn Anpassungs-Mechanismus hinreichend transparent und fuer Kunden nachvollziehbar
- BGH, Urt. v. 06.04.2016 — VIII ZR 79/15, NJW 2016, 2101 — Grundversorgungs-Tarif-Aenderung bedarftransparente Bekanntgabe; fehlende Bekanntgabe fuehrt zur Unwirksamkeit der Tarif-Aenderung gegenueber dem Kunden
- OLG Duesseldorf, Urt. v. 09.03.2022 — VI-2 U 5/21, ZNER 2022, 134 — Hardship-Klausel in Energie-Grosskunden-Vertrag begruendet Anpassungspflicht bei dauerhafter wesentlicher Aenderung der Preis-Grundlagen; Gaspreis-Krise 2022 als Ausloese-Ereignis anerkannt

## Zentrale Normen (Paragrafenkette)

§ 315 BGB (billiges Ermessen Leistungsbestimmung) — §§ 305-310 BGB (AGB-Kontrolle) — §§ 36-38 EnWG (Grundversorgung) — § 46 EnWG (Konzessionsvertrag) — AVBEltV / AVBFernwaermeV (Vertragsbeziehungen Grundversorgung) — §§ 313, 314 BGB (Stoerung Geschaeftsgrundlage, Hardship)

## Kommentarliteratur

- Britz/Hellermann/Hermes, EnWG, 4. Aufl. 2022, §§ 36-38 Rn. 1 ff. (Grundversorgung, Sondervertrag)
- Grüneberg (Palandt), BGB, 83. Aufl. 2024, § 315 Rn. 1 ff. (billiges Ermessen) und §§ 305 ff. Rn. 1 ff. (AGB-Kontrolle Energie)

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
- BGH VIII ZR 56/08, 191/18, 263/22, 304/16
- BGH EnVR 25/16 (Konzession)
- DIS / ICC Schieds-Standards
- Schiedsstelle Energie
