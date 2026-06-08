---
name: tempo-messung-unfallregulierung-quoten
description: "Tempo Messung Unfallregulierung Quoten im Plugin Fachanwalt Verkehrsrecht: prüft konkret Mandant bestreitet korrekte Geschwindigkeitsmessung in, Mandant hat Unfall mit Mitverschulden und fragt welche, Versicherer hat Regulierung angeboten und Anwalt verhandelt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Tempo Messung Unfallregulierung Quoten

## Arbeitsbereich

**Tempo Messung Unfallregulierung Quoten** ordnet den Fall über die tragenden Prüfungslinien: Mandant bestreitet korrekte Geschwindigkeitsmessung in, Mandant hat Unfall mit Mitverschulden und fragt welche, Versicherer hat Regulierung angeboten und Anwalt verhandelt. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-verkehrsrecht-tempo-messung-beweis` | Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid. Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova PTB-Zulassung Eichschein Messdokumentation Messverfahren-Verzeichnis. Output: Beweisanfechtungs-Strategie und Beweisantrag auf Sachverständigen. Abgrenzung zu fachanwalt-verkehrsrecht-bußgeldbescheid-prüfen (Gesamtprüfung) und bußgeld-einspruch-prüfen. |
| `fachanwalt-verkehrsrecht-unfallregulierung-quoten` | Mandant hat Unfall mit Mitverschulden und fragt welche Schadensposten zu welcher Quote durchsetzbar sind. § 254 BGB Mitverschulden Quoten-Modelle. Prüfraster: Schadenstabellen Reparatur Mietwagen Wertminderung Nutzungsausfall Schmerzensgeld 130-Prozent-Grenze Reparaturkosten vs. Wiederbeschaffungswert. Output: Schadensquoten-Berechnung und Vergleichsangebot. Abgrenzung zu fachanwalt-verkehrsrecht-regulierungsanforderung (Erstforderung) und fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich. |
| `fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich` | Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich. Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote § 254 BGB vorgerichtliche Korrespondenz Schmerzensgeld-Tabellen gerichtlicher Vergleich § 278 Abs. 6 ZPO Mediation Personenschaden. Output: Verhandlungspaket und Vergleichsentwurf. Abgrenzung zu fachanwalt-verkehrsrecht-unfallregulierung-quoten (Berechnung) und vergleichsverhandlung-strategie (Strategie). |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-verkehrsrecht-tempo-messung-beweis`

**Fokus:** Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid. Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova PTB-Zulassung Eichschein Messdokumentation Messverfahren-Verzeichnis. Output: Beweisanfechtungs-Strategie und Beweisantrag auf Sachverständigen. Abgrenzung zu fachanwalt-verkehrsrecht-bußgeldbescheid-prüfen (Gesamtprüfung) und bußgeld-einspruch-prüfen.

# Tempo-Messung Beweisanfechtung

## Zweck

Verteidigung bei OWi wegen Geschwindigkeitsüberschreitung.

## 1) Standardisierte Messverfahren

### PTB-Zulassung

- Physikalisch-Technische Bundesanstalt-Zulassung
- Bei zugelassenem Gerät: Standardisiertes Messverfahren
- Beweis-Erleichterung

### Gemeinsame Liste

| Gerät | Hersteller |
|---|---|
| PoliScan Speed | Vitronic |
| ES 3.0, ES 8.0 | eso |
| LeivTec XV-3 | Leivtec (Stand: Zulassung umstritten) |
| Multanova 6F | Multanova |
| Riegl FG21-P | Riegl |
| TraffiStar S350 / S360 | Jenoptik |

## 2) Toleranz-Abzug

- Bei Geschwindigkeit < 100 km/h: 3 km/h Abzug
- Bei > 100 km/h: 3 % Abzug
- Bei Nachfahrmessung: 4 km/h bzw. 5 %

## 3) Akteneinsicht-Strategie

### Standard-Akteneinsicht

- Bußgeldbescheid
- Bei Anfechtung: vollständige Akten

### Mess-Spezifische Unterlagen

- Eichschein-Original
- Mess-Protokoll
- Bedienungsanleitung
- Pruefberichte / Fehlerbild

### Verdachts-Punkte

- Reflektionsfehler
- Mess-Position
- Bedien-Fehler

## 4) Standardisiertes Messverfahren

### Bedeutung

- Tatrichter darf von Richtigkeit ausgehen
- Beweis-Erleichterung Ordnungsbehoerde

### Erschuetterung

- Konkrete Anhaltspunkte für Fehler
- Sachverständigen-Gutachten

### Pflicht zur Sachverständigenauskunft

- BGH-Linie zur erforderlichen Mess-Sicherheit
- Bei Zweifel: SV-Pflicht Gericht

## 5) Typische Fehler-Quellen

### Mess-Fehler

- Reflektionsobjekt (Hochhaus, Tunnel)
- Falsche Mess-Position
- Pruefintervall überschritten
- Software-Update nicht durchgeführt

### Bedienfehler

- Ausbildungs-Mangel
- Gerät falsch positioniert
- Mess-Modus falsch

### Geräte-Spezifika

- LeivTec XV-3: laufende Diskussion
- ES 3.0: bekannte Schwachstellen bei niedrigen Geschwindigkeiten

## 6) Einspruch

### Phase 1 — Bußgeldbescheid

- Frist 2 Wochen Einspruch
- Bei Versäumnis: Rechtskraft

### Phase 2 — Akteneinsicht

- Antrag schriftlich
- Vollständige Mess-Unterlagen

### Phase 3 — Verteidigungs-Strategie

- Mangel-Analyse
- Sachverständigen-Einbindung
- Verfahrens-Strategie

### Phase 4 — Hauptverhandlung

- AG (Amtsgericht)
- Beweisaufnahme
- Plaedoyer

### Phase 5 — Rechtsbeschwerde

- OLG bei Rechtsfehlern
- Frist 1 Woche

## 7) Punkte / Fahrverbot

### Punkte FAER

- Bei zugelassener Fahreignung-Registers
- 1-3 Punkte je Verstoß
- 8 Punkte: MPU

### Fahrverbot

- Ab > 25 km/h innerorts / 26 km/h außerorts
- Bei zweimaliger 21+ innerhalb 12 Monaten: 1 Monat
- Dauer 1-3 Monate

## 8) Typische Fehler

1. **Einspruchsfrist 2 Wochen verpasst**
2. **Akteneinsicht oberflaechlich**
3. **Sachverständigen-Prüfung versäumt**
4. **Geräte-spezifische Schwachstellen** nicht angeführt

## 9) BVerfG- / BGH- / OLG-Linien (Stand Mai 2026)

| Aktenzeichen | Datum | Kernaussage | Offene Quelle |
|---|---|---|---|
| BVerfG 2 BvR 1167/20 | 20.6.2023 | Keine Pflicht zur Speicherung von Rohmessdaten; Recht auf erweiterten Informationszugang besteht aber im Einzelfall | bundesverfassungsgericht.de |
| BVerfG 2 BvR 1616/18 | 12.11.2020 | Recht auf Akteneinsicht / Informationszugang im OWi-Verfahren (Tempo-Messung) | bundesverfassungsgericht.de |
| OLG Saarbruecken (LeivTec XV-3) | 2021 / 2022 | Diskussion zur Zulassung; Live-Volltext (saarland.de oder openjur.de) vor Verwendung verifizieren | saarland.de bzw. openjur.de |

Hinweis: Standardisierung nach BGH-Linie bedeutet nur eine Beweis-Erleichterung. Konkrete Anhaltspunkte für Mess-Fehler im Einzelfall erschüttern die Beweis-Wirkung. Volltext jeder Entscheidung vor Versand in offener Quelle aufrufen; keine Modellwissen-Zitate.

## Anschluss

- `fachanwalt-verkehrsrecht-unfallregulierung-quoten` — bei verbundener Unfallfrage
- `bussgeld-einspruch-pruefen` (Power-Tool) — Prüfraster
- `verkehrsowi-verteidiger` — bei vertieftem OWi-Verfahren

## 2. `fachanwalt-verkehrsrecht-unfallregulierung-quoten`

**Fokus:** Mandant hat Unfall mit Mitverschulden und fragt welche Schadensposten zu welcher Quote durchsetzbar sind. § 254 BGB Mitverschulden Quoten-Modelle. Prüfraster: Schadenstabellen Reparatur Mietwagen Wertminderung Nutzungsausfall Schmerzensgeld 130-Prozent-Grenze Reparaturkosten vs. Wiederbeschaffungswert. Output: Schadensquoten-Berechnung und Vergleichsangebot. Abgrenzung zu fachanwalt-verkehrsrecht-regulierungsanforderung (Erstforderung) und fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich.

# Unfallregulierung — Quoten

## Zweck

Schadensregulierung nach Verkehrsunfall mit Mitverschuldens-Bewertung.

## 1) Schadens-Positionen

| Position | Inhalt |
|---|---|
| Reparaturkosten | Werkstatt-Rechnung netto |
| Wertminderung | Merkantiler Minderwert |
| Nutzungs-Ausfall | Tagessatz nach EurotaxSchwacke / DAT |
| Mietwagen | Tagessätze Schwacke-Liste |
| Anwaltskosten | Anrechnung auf Schaden |
| Schmerzensgeld | bei Personenschaden |
| Verdienst-Ausfall | bei Erwerbs-Ausfall |
| Sachverständigen-Kosten | bei Streit |

## 2) Mitverschulden § 254 BGB

### Prüfung

- Eigene Pflichtverletzung
- Anteil am Schaden
- Quoten-Bildung (z.B. 70/30, 50/50)

### Praxis-Quoten

- Auffahr-Unfall: meist 100 % Hintermann
- Vorfahrt-Verstoß: 70-100 % Verursacher
- Spurwechsel: 60-80 % Verursacher
- Unaufmerksamkeits-Fall: gemischt

## 3) 130-%-Grenze

### BGH-Linie

- Reparatur zulaessig, wenn Reparaturkosten **bis 130 %** des Wiederbeschaffungswerts
- Verifizierte Entscheidungen vor Ausgabe in offener Quelle prüfen (BGH-Datenbank, dejure.org, openjur.de):
 - BGH, Urt. v. 12.3.2024, VI ZR 280/22 — Werkstatt- bzw. Sachverstaendigenrisiko (Übertragung auf überhöhte Sachverstaendigenkosten); offene Quelle: https://juris.bundesgerichtshof.de
 - BGH, Urt. v. 5.11.2024, VI ZR 12/24 — fiktive Berechnung Haushaltsfuehrungsschaden (Mindestlohn als Untergrenze, nachvollziehbare Begründung erforderlich)
- Über 130 %: nur Wiederbeschaffungswert (Totalschaden)

### Fiktive Abrechnung

- Bei Reparatur: tatsächliche Werkstatt-Kosten
- Bei Verkauf Restwert: WBW abzueglich Restwert
- Bei fiktiver Abrechnung: 6 Monate Bindungs-Frist
- Werkstattrisiko-Doktrin (BGH, Urt. v. 16.1.2024, VI ZR 253/22 und VI ZR 239/22): Geschädigter trägt grundsätzlich nicht das Risiko überhöhter Werkstattkosten. Übertragung auf Sachverstaendigenkosten: BGH VI ZR 280/22

## 4) Werkstatt-Bindung

### Frei oder Vertragswerkstatt

- Bei Vollkasko: meist Vertragswerkstatt
- Bei Haftpflicht: freie Werkstattwahl
- Stundensätze: BGH-Linie

## 5) Workflow

### Phase 1 — Sofort am Unfall-Ort

- Polizei bei Personenschaden
- Foto-Dokumentation
- Zeugen
- Unfallbericht ausfuellen
- Versicherungs-Daten austauschen

### Phase 2 — Erstanwalts-Beratung

- Sachverhalts-Aufnahme
- Schadens-Sichtung
- Sachverständiger

### Phase 3 — Versicherer-Schadensmeldung

- Mit Anwalt
- Vollständige Position
- Bei Streit: Klage AG / LG

### Phase 4 — Bei Streit

- Klage gegen Versicherer (Direkt-Klage möglich)
- Sachverständigen-Beweis
- Vergleich oder Urteil

## 6) Schmerzensgeld

### BGH-Linien

- Tabelle nach Verletzungsschwere
- Beispiele:
 - HWS-Schleudertrauma leicht: 500-1.500 EUR
 - Knochenbruch ohne Folgen: 2.000-5.000 EUR
 - Bleibender Schaden / Querschnitt: 100.000+ EUR

### Praxis

- Hacks Becker Schmerzensgeld-Tabelle
- Vergleichs-Fälle

## 7) Verjährung

- 3 Jahre § 195 BGB
- Ab Kenntnis von Schaden und Schaedger
- Hoechstens 30 Jahre

## 8) Typische Fehler

1. **Unfallort nicht dokumentiert**
2. **Werkstatt-Vertragsbindung übersehen**
3. **130-%-Grenze ignoriert**
4. **Schmerzensgeld zu niedrig** verhandelt

## 9) BGH-Linien (Stand Mai 2026; nur offene Quellen)

| Aktenzeichen | Datum | Thema | Offene Quelle |
|---|---|---|---|
| BGH VI ZR 280/22 | 12.3.2024 | Werkstattrisiko-Grundsätze auf überhöhte Sachverstaendigenkosten übertragen | juris.bundesgerichtshof.de |
| BGH VI ZR 253/22 | 16.1.2024 | Werkstattrisiko Grundsatzurteil; Geschädigter trägt nicht Risiko überhöhter Werkstattkosten | juris.bundesgerichtshof.de |
| BGH VI ZR 239/22 | 16.1.2024 | Werkstattrisiko parallel | juris.bundesgerichtshof.de |
| BGH VI ZR 12/24 | 5.11.2024 | Fiktiver Haushaltsfuehrungsschaden; Mindestlohn als Untergrenze; nachvollziehbare Begründung erforderlich | juris.bundesgerichtshof.de |
| BGH VI ZR 165/25 | 24.3.2026 | Schadensrecht Wiederherstellungskosten; vor Verwendung Volltext live verifizieren | bundesgerichtshof.de |
| BGH VI ZR 25/24 | 8.4.2025 | Schadensrecht Folgefall Werkstattrisiko; Live-Volltext prüfen | juris.bundesgerichtshof.de |

Hinweis: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen. Tabelle ist nur Recherche-Anker — vor Versand jedes Aktenzeichen erneut in offener Quelle aufrufen.

## Anschluss

- `fachanwalt-verkehrsrecht-mpu-vorbereitung` — bei Fahrerlaubnis
- `unfall-haftungsquote-berechnen` (Power-Tool) — Berechnung
- `deckungsanfrage-pruefen` — bei Versicherer-Streit

## 3. `fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich`

**Fokus:** Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich. Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote § 254 BGB vorgerichtliche Korrespondenz Schmerzensgeld-Tabellen gerichtlicher Vergleich § 278 Abs. 6 ZPO Mediation Personenschaden. Output: Verhandlungspaket und Vergleichsentwurf. Abgrenzung zu fachanwalt-verkehrsrecht-unfallregulierung-quoten (Berechnung) und vergleichsverhandlung-strategie (Strategie).

# Versicherer-Verhandlung / Quotenstreit im Verkehrsrecht

## Zweck

Verkehrsunfall-Mandate enden zu ca. 80 % in Vergleich mit Kfz-Versicherer. Verhandlungs-Strategie ist Kern: Mitverschuldensquote § 254 BGB, Schmerzensgeld-Tabellen, vermehrte Bedürfnisse.

## Eingaben

- Unfallhergang (Polizei, Foto, Zeugen)
- Mandant (geschädigter Insasse / Fahrer / Halter)
- Versicherer-Reaktion (Anerkenntnis %, Ablehnung)
- Schadensart (Sachschaden, Personenschaden, Unterhaltsausfall)
- Streitwert

## Rechtlicher Rahmen

- **§ 7 StVG** — Halter-Gefährdungshaftung
- **§ 18 StVG** — Fahrer-Verschulden
- **§ 254 BGB** — Mitverschulden
- **§ 11 StVG** — Schmerzensgeld
- **§ 843 BGB** — Renten-Ersatz vermehrte Bedürfnisse
- **PflVG** — Pflicht-Versicherung
- **§ 17 StVG** — Quotelung Halter

## ADR-Pfade

### Pfad 1 — Versicherer-Verhandlung

- Schadensanzeige binnen 7 Tagen
- Quotenangebot Versicherer
- Verhandlung mit Sachbearbeiter
- Vergleichs-Quote 70-90 %

### Pfad 2 — Schiedsgutachten Mitverschuldensquote

- Bei unstreitiger Quote-Frage
- Sachverständigen-Gutachten DEKRA / TÜV
- Bindend für Versicherer

### Pfad 3 — Gerichtlicher Vergleich § 278 ZPO

- Güteverhandlung § 278 Abs. 2 ZPO als Pflicht-Termin vor Beweisaufnahme
- Vergleichsabschluss zu Protokoll § 160 Abs. 3 Nr. 1 ZPO oder per Beschluss § 278 Abs. 6 ZPO (schriftlicher Vergleich)
- Vor Amts-/Landgericht; bei mittlerem Streitwert besonders effizient
- Erörterungstermin mit Quotenvorschlag Gericht

### Pfad 4 — Mediation bei Schwerstverletzung

- DGFM-Mediator
- Bei Querschnitt, Hirnschaden, lebenslange Pflege
- Lebenslange Renten-Vereinbarung

### Pfad 5 — Versicherungs-Ombudsmann

- Bei Verbraucher mit Versicherer
- VVR e.V.

## Workflow

### Phase 1 — Unfall-Aufnahme

- Polizei (zwingend bei Personenschaden)
- Foto-/Zeugen-Dokumentation
- Krankenhaus-/Werkstatt-Belege

### Phase 2 — Schadensanzeige Versicherer

- Schriftliche Schadensmeldung
- Schadenshöhe-Beziferung
- Fragenkatalog Versicherer beantworten

### Phase 3 — Verhandlung

- Versicherer-Quotenvorschlag
- Gegenangebot
- Schriftliche Niederlegung

### Phase 4 — Vergleich

- Erledigungs-Klausel
- Abfindungsbetrag
- Bei Personenschaden: Renten-Vereinbarung

### Phase 5 — Bei Scheitern Klage

- AG/LG je Streitwert
- Sachverständigen-Beweis
- Vergleichstermin vor Gericht

## Strategie und Taktik

- **Mitverschuldensquote nie vor Akteneinsicht akzeptieren**
- **Schmerzensgeld-Tabelle Hacks / Beck** als Orientierungsmaßstab
- **130 %-Grenze bei Fahrzeugschaden**: Reparatur kann teurer als Marktwert sein
- **Vermehrte Bedürfnisse** § 843 BGB lebenslang-Rente bei Schwerstverletzung
- **Versicherer-Vergleichsdruck**: Klage-Drohung oft Quotenerhöher

## Querverweise

- `fachanwalt-verkehrsrecht-orientierung` — Triage
- `fachanwalt-verkehrsrecht-unfallregulierung-quoten` — Quote
- `fachanwalt-verkehrsrecht-mpu-vorbereitung` — MPU
- `fachanwalt-verkehr-autonom-1d-stvg` — Sonderfall

## Quellen und Updates

Stand: 05/2026. StVG, § 254 BGB. BGH-Linie zu Schmerzensgeld stabil.

## Aktuelle Rechtsprechung Quotenverhandlung (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand jeweils Volltext aufrufen):

- BGH VI ZR 253/22, Urt. v. 16.1.2024 — Werkstattrisiko liegt im Regelfall beim Schädiger. Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 239/22, Urt. v. 16.1.2024 — Werkstattrisiko bei fiktiver Abrechnung. Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 280/22, Urt. v. 12.3.2024 — Sachverstaendigenrisiko (Übertragung Werkstattrisiko auf Gutachterkosten). Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 12/24, Urt. v. 5.11.2024 — Fiktiver Haushaltsfuehrungsschaden; Mindestlohn als Untergrenze, konkrete Stundensatzbegründung erforderlich. Quelle: juris.bundesgerichtshof.de
- BGH VI ZR 24/25, Urt. v. 14.10.2025 — Substantiierungsanforderungen Schaden; Art. 103 Abs. 1 GG. Quelle: juris.bundesgerichtshof.de

Keine Modellwissen-Zitate. Vor Versand offene Quelle prüfen (juris.bundesgerichtshof.de, dejure.org, openjur.de).

<!-- audit: 27.05.2026 — VI ZR 73/22 (NOT_FOUND auf dejure.org) geloescht; VI ZR 233/19 (NOT_FOUND auf dejure.org) geloescht; VI ZR 286/19 WRONG_TOPIC korrigiert: Thema Anhaenger-Gefaehrdungshaftung § 7 StVG, NJW-Zitat 2020 2116 (nicht 1876), Quelle dejure.org/2020,9266. -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
