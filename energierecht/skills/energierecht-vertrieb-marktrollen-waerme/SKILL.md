---
name: energierecht-vertrieb-marktrollen-waerme
description: "Vertrieb Marktrollen Waerme: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertrieb Marktrollen Waerme

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Vertrieb Marktrollen Waerme** im Plugin Energierecht (EnWG, EEG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `energierecht-vertrieb-marktrollen` | Energievertrieb und Marktrollen im liberalisierten Energiemarkt: Lieferant, Netzbetreiber, Bilanzkreis. Normen: §§ 4 ff. EnWG, MaBiS-Prozesse. Prüfraster: Marktrollen, Bilanzkreisvertrag, Lieferantenwechsel. Output: Marktrollenanalyse und Vertriebsstruktur. Abgrenzung: nicht Energieliefervertrag (eigener Skill). |
| `energierecht-waerme-quartier` | Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende. Normen: AVBFernwaermeV, GEG, EnWG, EEG. Prüfraster: Konzessionspflicht, Preisanpassungsklauseln, GEG-Anforderungen. Output: Waermenetz-Rechtsgutachten. Abgrenzung: nicht allgemeine Energieliefervertraege. |
| `energierecht-wettbewerb` | Wettbewerbs- und Kartellrecht im Energiesektor prüfen: Marktmacht, Diskriminierung, Missbrauch. Normen: §§ 18 ff. GWB, Art. 101 102 AEUV, EnWG. Prüfraster: Marktabgrenzung, Marktmacht, Diskriminierungsverbot, Entflechtung. Output: Kartellrechtliche Risikoeinschaetzung Energiemarkt. Abgrenzung: nicht allgemeines Wettbewerbsrecht. |
| `er-bess-abfall-recycling-rueckbau` | Prüft Rückbaupflichten, Batterieentsorgung, Recycling, Herstellerpflichten und Grundstücksrückgabe. |

## Arbeitsweg

Im Plugin Energierecht (EnWG, EEG) gilt für **Vertrieb Marktrollen Waerme**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `energierecht-vertrieb-marktrollen`

**Fokus:** Energievertrieb und Marktrollen im liberalisierten Energiemarkt: Lieferant, Netzbetreiber, Bilanzkreis. Normen: §§ 4 ff. EnWG, MaBiS-Prozesse. Prüfraster: Marktrollen, Bilanzkreisvertrag, Lieferantenwechsel. Output: Marktrollenanalyse und Vertriebsstruktur. Abgrenzung: nicht Energieliefervertrag (eigener Skill).

# Vertrieb und Marktrollen

## Zweck

Behandelt die Stromlieferungs-/Gasversorgungs-Sphäre: Grundversorger, Sonderkunden, Tarif-Änderung, Direktvermarktung, Endkundenrechte und Marktrollen-Pflichten.

## Eingaben

- Mandant (Versorger / Endkunde / Direktvermarkter / Bilanzkreis-Verantwortlicher)
- Vertragsart (Grundversorgung / Sondervertrag / Industrie-Sondervertrag / PPA)
- Streit-Anlass (Preiserhöhung, Vertragsende, Wechsel-Verzögerung, AGB-Klausel)
- Bei Versorger: Bilanzkreis-Vereinbarungen, GPKE-Prozesse-Stand

## Schritt 1 — Grundversorgung § 36 EnWG

### Grundversorger-Pflicht

- Jeder zugelassene Energieversorger mit größtem Marktanteil im Netzgebiet Niederspannung / Gas-Niederdruck
- Versorgungs-Pflicht für jeden Haushaltskunden, der sich nicht aktiv für einen anderen Vertrag entschieden hat
- Grundversorgungs-Verordnung (StromGVV / GasGVV) als AGB

### Tarif-Höhe

- Wirtschaftlich angemessen
- Veröffentlichungs-Pflicht im Internet und im Versorgungsgebiet
- BNetzA-Marktmonitoring
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Tarif-Änderung

- Schriftliche Mitteilung an Kunden mit 6 Wochen Vorlauf § 5 Abs. 2 StromGVV / GasGVV
- Sonder-Kündigungs-Recht des Kunden
- Vorab Plausibilisierungs-Berechnung

## Schritt 2 — Sonderkunden / Sonderverträge

### Anwendungsbereich

- Haushaltskunden mit aktiver Anbieter-Wahl
- Gewerbe-/Industrie-Kunden

### Vertrags-AGB

- AGB-Kontrolle §§ 305 ff. BGB
- Spezial-Recht des EnWG (insbesondere § 41 EnWG)
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Tarif-Anpassungs-Klauseln

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Transparenz-Erfordernis
- Begrenzungs- und Ausgleichs-Mechanismen
- Bei AGB-Unwirksamkeit: Vertrag mit ursprünglichem Preis fortgesetzt — erheblicher Schaden Versorger

### Vertragslaufzeit § 41 EnWG

- Mindest-Laufzeit max. 2 Jahre Haushalts-Stromverträge
- Verlängerungs-Klauseln eingeschränkt
- Kündigungs-Frist max. 1 Monat

## Schritt 3 — Strompreisbremse 2023-2024 (Nachlauf-Verfahren)

### Strompreisbremse-Gesetz (StromPBG) und Erdgas-Wärme-Preisbremse-Gesetz (EWPBG)

- Anwendungs-Zeitraum 01.01.2023 — 31.12.2023, verlängert teilweise bis 31.03.2024
- Pauschal-Entlastung Versorger an Endkunden
- Übermittlung an Bund

### Nachlauf-Streitigkeiten

- Versorger-Erstattung durch Bund
- BAFA / BNetzA-Prüfungen
- Streit über Auslegung Härtefall-Regelungen

### Verfahren

- BAFA-Prüfung mit Bescheid
- Widerspruch / Klage VG
- Bei großen Streitwerten OLG-Beschwerde

## Schritt 4 — Bilanzkreis und GPKE-Prozesse

### Bilanzkreis-Verantwortlicher (BKV)

- Wirtschafts-Beauftragter mit Bilanzkreis-Vertrag ÜNB
- Ausgleichsenergie bei Abweichungen
- Sicherheits-Hinterlegung

### GPKE / GeLi-Gas

- Standardisierte Marktrollen-Prozesse Lieferanten-Wechsel
- Aufgaben zwischen alter Lieferant, neuer Lieferant, Netzbetreiber, Messstellenbetreiber
- BNetzA-Festlegung MaBiS / WiM

### Wechsel-Erleichterung

- Bei Kunden-Wechsel: 24-Stunden-Wechsel (seit 06/2025)
- Vorher 3 Wochen
- Sicherstellung Versorgung
- Datenschutz-Verzahnung

## Schritt 5 — Lieferanten-Insolvenz und Ersatzversorger

### Versorgungs-Unterbrechung-Schutz

- Bei Insolvenz Lieferant Grundversorger übernimmt § 38 EnWG
- Bei Gewerbe / Industrie Ersatzversorger
- Versorgung läuft ohne Unterbrechung

### Konsequenzen für Kunden

- Tarif-Sprung (Grundversorgung typisch teurer)
- Wechsel-Möglichkeit jederzeit ohne Mindest-Laufzeit
- Schadensersatz gegen insolvenz Lieferant Insolvenz-Forderung

### Massierungs-Konstellationen

- 2022 Energiekrise: zahlreiche Lieferanten in Insolvenz
- Grundversorger-Last extrem
- Sanktions-Aspekt § 24 EnSiG

## Schritt 6 — Direktvermarktung Erzeugung

### Direktvermarkter-Modell

- EEG-Anlage verkauft Strom an Direktvermarkter
- Direktvermarkter zahlt anzulegenden Wert minus Vermarktungs-Marge
- Marktprämie wird von Direktvermarkter an Netzbetreiber abgewickelt

### Bilanzkreis-Zuordnung

- Anlage in Bilanzkreis Direktvermarkter
- Datenmeldung WiM-Format
- Stunden-Werte-Übertragung

### PPA-Variante

- Direkt zwischen Anlage und Industriekunden
- Kein EEG-Pfad mehr
- Bilanzkreis-Strukturen aufzubauen
- Skill `energierecht-projektfinanzierung`

## Schritt 7 — Stromkennzeichnung § 42 EnWG

### Pflicht

- Jeder Lieferant muss Stromherkunft-Mix offenlegen
- Anteile: erneuerbar, fossil, Kernenergie, sonstig
- Pro Tarif separate Kennzeichnung

### Herkunftsnachweis (HKN)

- UBA-Register HKN
- Pro MWh erneuerbarer Strom ein HKN
- Lieferant kauft HKN, um Tarif als "Ökostrom" auszuweisen

### Greenwashing-Risiko

- Ökostrom-Tarife mit fragwürdiger HKN-Herkunft
- UWG-Streit Wettbewerbszentrale
- Skill `esg-greenwashing-csrd` im `umweltrecht`

## Schritt 8 — Endkundenrechte

### Widerruf

- Fernabsatz-Vertrag: 14 Tage Widerruf
- Bei Telefonverkauf zusätzliche Bestätigungs-Anforderung

### Schlechtleistung

- Strom-/Gas-Lieferung unterbrochen
- Mängelanspruch § 280 BGB
- Schadenshöhe oft begrenzt durch AGB

### Höhere Rechnung als erwartet

- Verbrauchs-Schätzung vs. tatsächlicher Zähler-Stand
- Schlechtschätzung-Widerspruch
- Schiedsstelle Energie

### Schiedsstelle Energie

- Außergerichtliche Streitbeilegung
- Kostenfrei für Verbraucher
- Verbindlich für Lieferant (bis 10.000 €)

## Schritt 9 — Marktstammdatenregister und Sanktionen

### Eintragungs-Pflichten

- Erzeugungs-Anlage § 5 MaStRV
- Marktakteur § 5 Abs. 2 MaStRV
- Speicher

### Sanktionen § 35 MaStRV

- Bei Nicht-Eintragung Bußgeld
- EEG-Vergütungs-Sperre § 33 Abs. 6 EEG
- Strenge BNetzA-Verwaltungspraxis

## Schritt 10 — Mandanten-Strategie

### Versorger / Lieferant

- AGB-Kontrolle strikt
- Tarif-Änderungs-Mitteilung mit Sonder-Kündigungs-Recht ordnungsgemäß
- Bilanzkreis-Compliance sicherstellen
- HKN-Quoten dokumentieren

### Endkunde

- Tarif-Vergleich nutzen
- Bei Mängeln Schiedsstelle einschalten
- Lieferanten-Wechsel jederzeit prüfen

### Direktvermarkter

- Anlagen-Portfolio strukturiert
- Bilanzkreis-Pflichten sicherstellen
- PPA-Optionen erschließen

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 36-38 EnWG (Grundversorgung, Ersatzversorgung) — § 41 EnWG (Vertragsaenderung Haushaltskunden) — § 42 EnWG (Stromkennzeichnung) — §§ 305-310 BGB (AGB-Kontrolle) — § 315 BGB (billiges Ermessen Preisbestimmung) — § 5 MaStRV (Marktstammdatenregister Pflichten)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-eeg-kwkg-erzeugung`
- `energierecht-netz-speicher-zugang`
- `energierecht-industriekunden`
- `energierecht-projektfinanzierung`
- `esg-greenwashing-csrd` (Umweltrecht-Plugin)
- `verbraucherrecht`

## Quellen

- EnWG 2024 §§ 36-42, 35a-f, 65, 75
- StromGVV / GasGVV
- StromPBG / EWPBG (Nachlauf)
- MaStRV
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BNetzA-Marktmonitoring-Berichte
- UBA HKN-Register
- Schiedsstelle Energie

## 2. `energierecht-waerme-quartier`

**Fokus:** Waermenetze und Quartiersversorgung rechtlich strukturieren: Fernwaerme, GEG-Erfuellung, lokale Waermewende. Normen: AVBFernwaermeV, GEG, EnWG, EEG. Prüfraster: Konzessionspflicht, Preisanpassungsklauseln, GEG-Anforderungen. Output: Waermenetz-Rechtsgutachten. Abgrenzung: nicht allgemeine Energieliefervertraege.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 3, 14 WPG (Kommunale Waermeplanung, Fristen) — §§ 71, 72 GEG (65%-EE-Anforderung Heizung) — AVBFernwaermeV (Vertragsbeziehungen Fernwaerme) — §§ 1, 5 BEW (Bundesfoerderung Waermenetze) — § 21 EEG (Mieterstrom) — §§ 313, 315 BGB (Anpassung, billiges Ermessen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- KfW-BEW-Förderrichtlinie 442
- BMWK-Hinweise Wärmeplanung
- Bayerische, NRW, Hessische GO-Vorschriften zu AuB-Satzung

## 3. `energierecht-wettbewerb`

**Fokus:** Wettbewerbs- und Kartellrecht im Energiesektor prüfen: Marktmacht, Diskriminierung, Missbrauch. Normen: §§ 18 ff. GWB, Art. 101 102 AEUV, EnWG. Prüfraster: Marktabgrenzung, Marktmacht, Diskriminierungsverbot, Entflechtung. Output: Kartellrechtliche Risikoeinschaetzung Energiemarkt. Abgrenzung: nicht allgemeines Wettbewerbsrecht.

# Wettbewerb und Beihilfen im Energierecht

## Zweck

Behandelt wettbewerbsrechtliche Aspekte im Energie-Bereich: Marktbeherrschung, BNetzA-Missbrauchskontrolle, Kartellamts-Fusionen, EU-Beihilfen, Entflechtungs-Vorschriften.

## Eingaben

- Mandant (Versorger, Netzbetreiber, Industrie, Behörde)
- Verfahrens-Anlass (Fusion, Marktbeherrschungs-Vorwurf, Beihilfen-Streit, Sektor-Untersuchung)
- Behörde involviert (Bundeskartellamt, BNetzA, EU-Kommission, BAFA)
- Marktanteil / Konzern-Struktur
- Beihilfen-Bestand

## Schritt 1 — Marktbeherrschungs-Prüfung EnWG § 33

### Tatbestand

- Marktbeherrschende Stellung
- Missbrauchs-Tatbestände § 19 GWB analog
- BNetzA-Zuständigkeit für Netz-Bereich; Bundeskartellamt für Lieferanten-Bereich

### Typische Konstellationen

- **Übertragungs-Netzbetreiber** als Monopolist
- **Verteilnetzbetreiber** als regionaler Monopolist
- **Konzern-Verbund** (Stadtwerk-Lieferant + Stadtwerk-Netzbetreiber)
- **Speicher- / Gas-Speicher-Anbieter** mit hoher regionaler Konzentration

### Missbrauchs-Verbot

- Preis-Missbrauch (überhöhte Preise)
- Konditionen-Missbrauch (Diskriminierung)
- Lieferungs-Verweigerung

### Verfahren

- BNetzA-Festlegung / Klage OLG Düsseldorf
- Bundeskartellamt-Verfahren mit Sektor-Untersuchung
- Skill `energierecht-verfahren`

## Schritt 2 — Bundeskartellamt-Verfahren Energie

### 9. Beschlussabteilung

- Spezialisiert auf Energie-Wirtschaft
- Sektor-Untersuchungen
- Fusions-Kontrolle Energie-Märkte
- Missbrauchs-Verfahren

### Sektor-Untersuchungen Bestand

- Strompreis-Bildung
- Gasversorgung-Endkunden
- Fernwärme-Markt (jüngst 2023/2024)
- Wasserstoff (laufend)

### Fusions-Kontrolle

- Anmeldepflicht ab Umsatz-Schwellen
- Bei Konzern-Konsolidierung Energie-Unternehmen
- Phase-I- und Phase-II-Verfahren
- Verbots-Entscheidung möglich (E.ON / Innogy umstritten)

### Aktuelle Praxis

- Kommunal-/Stadtwerk-Verbund häufig prüfungs-bedürftig
- Bei Erneuerbaren-Portfolio-Aufbau

## Schritt 3 — EU-Wettbewerbsrecht

### Art. 101 AEUV Kartellverbot

- Bei Lieferanten-/Vertriebs-Absprachen
- Wartungs-Konsortien
- PPA-Konsortien

### Art. 102 AEUV Marktbeherrschungs-Missbrauch

- Bei dominantem Netzbetreiber
- Bei dominantem Energie-Lieferanten

### Anwendungs-Praxis

- Großverfahren EU-Kommission gegen Gaz de France, ENEL etc.
- Diskriminierungs-Vorwürfe
- Aufnahme von Auflagen statt Geldbuße

## Schritt 4 — EU-Beihilfen Art. 107 AEUV

### Tatbestand

- Staatliche Leistung
- Selektive Begünstigung
- Wettbewerbs-Verfälschung
- Handels-Beeinträchtigung

### Energie-typische Beihilfen

- **EEG-Förderung** (als Beihilfe akzeptiert)
- **Strompreiskompensation Industrie** (Carbon Leakage)
- **KfW BEW**
- **Klimaschutzverträge (CCfD)**
- **Konzessionsabgabe-Reduktion**

### Verfahren

- Notifizierung EU-Kommission
- AGVO 651/2014 als Vereinfachung
- De-minimis-VO
- Bei Verstoß Rückforderung mit Zinsen

### EU-Kommissions-Linien

- Beihilfen für CO2-Reduktion grundsätzlich akzeptiert
- Aber: Zusätzlichkeit muss nachweisbar sein
- Bei "Free-Rider"-Effekt Rückforderung

## Schritt 5 — Entflechtungs-Vorschriften §§ 6-10 EnWG

### Hintergrund

- Vertikale Integration Netz und Lieferung problematisch
- EU-Richtlinien fordern Entflechtung
- Verschiedene Modelle (ITO, OU, ISO)

### ITO-Modell (Independent Transmission Operator)

- Netz-Gesellschaft mit Eigenständigkeit
- Konzern-Verbund mit Lieferanten möglich, aber strenge Trennung
- Insbesondere für TenneT, 50Hertz, Amprion, TransnetBW (Übertragungs-Netzbetreiber)

### Verteilnetz-Entflechtung § 8 EnWG

- Buchhalterische / Organisatorische Trennung
- Bei kleineren Verteilnetzbetreibern Befreiung möglich

### Mess- und Markt-Entflechtung

- MsbG (Messstellenbetriebs-Gesetz)
- Strikte Trennung Messstellen-Betreiber vom Lieferanten

### Streit-Verfahren

- BNetzA-Anordnungen zur Entflechtungs-Compliance
- Klage OLG Düsseldorf

## Schritt 6 — Strompreiskompensation als Beihilfe

### Hintergrund

- Kompensation indirekter ETS-CO2-Kosten
- EU-Leitlinien Beihilfen für Carbon Leakage (CL)
- Bewilligungs-Bescheid BAFA

### EU-Notifizierungs-Pflicht

- Programm-Genehmigung EU-Kommission
- Aktuelle Verlängerung bis 2030 (mit Anpassungen)
- Ressourcen-/Substitut-Kompensation reduziert

### Bei Verstoß

- Rückforderung mit Zinsen
- Bei systematischer Verletzung EU-Verfahren

## Schritt 7 — Kommunaler Versorger und Marktbeherrschung

### Sonderkonstellation

- Stadtwerk = Lieferant + (oft) Verteilnetzbetreiber + (oft) Erzeugungs-Anlagen
- Vertikale Integration in lokalem Markt
- Marktbeherrschungs-Position möglich

### Konzessions-Vergabe

- Eigene Vergabe an eigene Tochter-Gesellschaft?
- Wettbewerbs-Verfahren erforderlich
- Konkurrenten-Klage möglich
- Skill `energierecht-energievertraege`

### Re-Kommunalisierung

- Übernahme von Privatlieferanten durch Kommune
- Wettbewerbs-Aspekt
- BGH-Linien

## Schritt 8 — Fernwärme-Sektor-Untersuchung Bundeskartellamt

### Hintergrund

- 2023/2024 Untersuchung wegen Energie-Krise
- Frage: marktbeherrschende Stellung Fernwärme-Versorger?
- Preisanpassungs-Praxis prüfbar

### Mögliche Folgen

- Auflagen zu Preisanpassungs-Klauseln
- Anschluss-Pflicht-Modifikationen
- Sondernormen-Vorschlag

## Schritt 9 — Wasserstoff-Markt-Aufbau

### Spezielle Wettbewerbs-Themen

- Anfangs natürliche Monopol-Strukturen
- Förder-getriebene Anlagen
- Beihilfen-Genehmigung erforderlich

### EU-Bezug

- IPCEI (Important Projects of Common European Interest) Wasserstoff
- Hy2Tech-, Hy2Use-Initiativen
- Beihilfen-Notifizierung gesammelt

### Klimaschutzverträge

- EU-Genehmigung im Programm
- Einzel-Bewilligungs-Sicherheit

## Schritt 10 — Mandanten-Strategie

### Versorger / Netzbetreiber

1. Marktanteil-Analyse
2. Entflechtungs-Compliance
3. Bei großem Konzern Fusions-Anmeldepflicht
4. Beihilfen-Bezug dokumentieren

### Industrie-Kunde

1. Strompreiskompensation-Antrag rechtzeitig
2. CCfD-Beteiligung prüfen
3. CBAM-Compliance
4. Skill `energierecht-industriekunden`

### Kommune

1. Konzessions-Vergabe wettbewerbs-konform
2. Beihilfen-Aspekte bei Stadtwerk
3. Re-Kommunalisierung mit Rechtsberatung

### Behörde

1. Sektor-Untersuchungs-Beteiligung
2. Beihilfen-Notifizierung sicherstellen

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bundeskartellamt, Beschl. v. 22.09.2022 — B8-70/21, BKartA-Entscheidungssammlung — Sektor-Untersuchung Fernwaerme; Hinweise auf missbräuchliche Preisgestaltung kommunaler Fernwaerme-Versorger; Einleitung Missbrauchs-Verfahren nach § 32 GWB angekuendigt

## Zentrale Normen (Paragrafenkette)

§§ 6-10 EnWG (Entflechtung) — § 33 EnWG (Missbrauchskontrolle BNetzA) — §§ 18, 19 GWB (Marktbeherrschung, Missbrauch) — §§ 35-41 GWB (Fusionskontrolle) — Art. 101, 102 AEUV (Kartellverbot, Missbrauch) — Art. 107, 108 AEUV (Beihilfen) — § 46 EnWG (Konzessionsvertrag)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-verfahren` (BNetzA / OLG Düsseldorf)
- `energierecht-vertrieb-marktrollen`
- `energierecht-industriekunden` (Strompreiskompensation)
- `europarecht-kompass` (EU-Beihilfen)
- `fachanwalt-internationales-wirtschaftsrecht`

## Quellen

- EnWG §§ 6-10, 33
- GWB §§ 18, 19, 32
- AEUV Art. 101, 102, 107, 108
- EU-AGVO 651/2014
- EU-De-minimis-VO 1407/2013
- EU-Beihilfen-Verfahrens-VO 2015/1589
- EU-Leitlinien Beihilfen Klima- und Umweltschutz 2022
- Bundeskartellamt Sektor-Untersuchungen Energie
- BNetzA-Festlegungen Entflechtung
- BGH KZR-Linie
- OLG Düsseldorf VI-3 Kart
- EuGH-Linien zu Energie-Wettbewerb

## 4. `er-bess-abfall-recycling-rueckbau`

**Fokus:** Prüft Rückbaupflichten, Batterieentsorgung, Recycling, Herstellerpflichten und Grundstücksrückgabe.

# Rückbau, Recycling und Batterierecht

## Wofür dieser Arbeitsgang da ist

Fokus auf End-of-Life schon im Projektvertrag.

## Rechts- und Praxisanker

Batterierecht/EU-Batterieverordnung live prüfen, KrWG, Grundstücksvertrag, Sicherheitsleistung.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.
