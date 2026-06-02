# MiCAR, BaFin-Vorabklärung und KI-Verordnung — Compliance-Vorabbewertung

## 1. Ausgangslage

NeuroChain Labs entwickelt eine Plattform zur Orchestrierung von KI-Agenten und plant, Trainingsdaten und Rechenkapazität on-chain zu tokenisieren. Beides berührt mehrere Regulierungsebenen:

- **MiCAR** (Verordnung (EU) 2023/1114 über Märkte für Kryptowerte) — Anwendbar seit 30.12.2024 für Kryptowerte-Dienstleister und seit 30.06.2024 für stabile Werte.
- **KI-Verordnung** (Verordnung (EU) 2024/1689) — In Kraft getreten am 01.08.2024 mit gestaffelten Anwendungsterminen bis August 2027.
- **GwG** (Geldwäschegesetz) — Anwendung auf Kryptowerteanbieter.
- **WpHG / KWG** — Anwendung auf Wertpapiere und Bankgeschäfte, falls Token Wertpapiercharakter hat.

## 2. Token-Klassifizierung nach MiCAR

MiCAR unterscheidet drei Token-Kategorien:

| Kategorie | Beschreibung | Pflichten |
| --- | --- | --- |
| Asset-Referenced Token (ART) | bezieht Wert von mehreren Werten oder Vermögensgegenständen | Zulassung, Reserveanforderungen, Whitepaper |
| E-Money Token (EMT) | bezieht Wert auf eine einzige Fiatwährung | E-Geld-Lizenz oder Banklizenz, Whitepaper |
| sonstige Kryptowerte (Utility-Token, Sonstige) | nicht ART, nicht EMT | Whitepaper, Anbieterregistrierung, weniger streng |

Unsere geplanten Token (Trainingsdaten-Token, Compute-Token) sind voraussichtlich **sonstige Kryptowerte** (Utility-Token), da sie:

- den Zugang zu einer Plattform-Funktion ermöglichen (Datennutzung, Rechenleistung)
- keinen Stabilitätsanker zu Fiatwährungen haben
- nicht als Anlageprodukt vermarktet werden

Voraussetzung: das Whitepaper nach Artikel 6 MiCAR muss vor öffentlichem Angebot erstellt, bei der BaFin notifiziert und veröffentlicht werden. Mindestinhalte:

- Beschreibung des Emittenten
- Beschreibung des Projekts und der Technologie
- Risiken
- Rechte und Pflichten der Token-Inhaber
- Umweltauswirkungen (insbesondere Energieverbrauch des Konsensmechanismus)

## 3. CASP-Status (Crypto-Asset Service Provider)

Falls NeuroChain Labs neben der Emission auch Dienstleistungen wie:

- Verwahrung von Kryptowerten für Dritte
- Tausch von Kryptowerten gegen Fiat oder andere Kryptowerte
- Betrieb einer Handelsplattform
- Beratung zu Kryptowerten

erbringt, wird sie zum **CASP** und braucht eine BaFin-Zulassung nach Artikel 59 MiCAR. Voraussetzungen:

- Mindestkapital je nach Dienstleistung (50.000 EUR bis 150.000 EUR)
- Geeignete Geschäftsleiter (Fit-and-Proper)
- IT-Sicherheits- und Continuity-Konzepte
- Geldwäschebeauftragter

Wir planen zunächst **keine** CASP-Dienste, sondern nur die Emission von Utility-Token. Damit greift die einfache Anbieter-Notifizierung, kein CASP-Verfahren.

## 4. BaFin-Vorabklärung

Wir holen eine schriftliche BaFin-Vorabklärung ein, sobald die Token-Spezifikation konkreter ist. Dies geschieht voraussichtlich Q4 2026. Vorgehen:

1. Erstellung eines Token-Konzeptpapiers (Use Cases, Token-Mechanik, Rechte der Inhaber)
2. Anschreiben an BaFin, Referat Geldwäscheprävention und Kryptowerte-Aufsicht
3. Antwort innerhalb von ca. acht Wochen
4. Falls negative Einstufung (z.B. Wertpapier statt Utility), Anpassung der Token-Mechanik

Bis zum Vorliegen der Vorabklärung verzichten wir auf jede öffentliche Token-Emission. Geschäftsführerin Aylin trägt dafür die Verantwortung.

## 5. KI-Verordnung — Anwendbarkeit

### 5.1 Anwendungsbereich

Die KI-Verordnung unterscheidet vier Risikoklassen:

| Klasse | Beispiele | Pflichten |
| --- | --- | --- |
| verbotene Praktiken | Social Scoring, manipulative KI | Verbot |
| Hochrisiko-KI | KI in kritischen Bereichen (z.B. Personal, Justiz) | Konformitätsbewertung, Risikomanagement |
| begrenztes Risiko | Chatbots, Deepfakes | Transparenzpflichten Artikel 50 |
| minimales Risiko | Spielautomaten, Spamfilter | keine spezifischen Pflichten |

NeuroChain Labs entwickelt eine Plattform für KI-Agenten, die nicht im Hochrisikobereich (Anhang III) eingeordnet ist. Damit greifen:

- Transparenzpflichten Artikel 50 KI-VO, insbesondere bei Interaktion mit Nutzern (Hinweis "Sie kommunizieren mit einer KI") und bei synthetisch erzeugten Inhalten (Wasserzeichen, Kennzeichnung).
- allgemeine Sorgfaltspflichten

### 5.2 GPAI-Modelle

Wenn wir Allzweck-KI-Modelle (General Purpose AI Models, GPAI) entwickeln oder bereitstellen, greifen die GPAI-Pflichten nach Kapitel V KI-VO:

- technische Dokumentation
- Urheberrechts-Compliance bei Trainingsdaten
- Zusammenfassung der Trainingsinhalte (öffentlich)

Wir planen, ein eigenes Modell zu trainieren. Sobald die Trainings-Compute-Schwelle (10^25 FLOPS für systemische Risiken) überschritten wird, greifen erweiterte Pflichten. Diese Schwelle erreichen wir in der Anfangsphase **nicht**.

### 5.3 Anwendungsdaten und DSGVO

Trainingsdaten unterliegen der DSGVO, wenn sie personenbezogen sind. Wir nehmen folgende Maßnahmen vor:

- Datenherkunft transparent dokumentieren
- Rechtsgrundlage für die Verarbeitung benennen (Einwilligung oder berechtigtes Interesse)
- Möglichkeit der Auskunft, Berichtigung und Löschung für Betroffene
- bei sensiblen Daten (Artikel 9 DSGVO): zusätzliche Anforderungen, in der Regel ausdrückliche Einwilligung

## 6. Roadmap Compliance

| Quartal | Meilenstein |
| --- | --- |
| Q3/2026 | Datenschutz-Verzeichnis, Datenschutzerklärung, AVV-Mustervorlagen |
| Q4/2026 | BaFin-Vorabklärung für Token-Konzept einreichen |
| Q1/2027 | Whitepaper nach MiCAR Artikel 6 erstellen (falls Token-Emission geplant) |
| Q2/2027 | KI-Transparenz-Hinweise in Produkt einbauen |
| Q3/2027 | KI-VO Anwendung vollständig (allgemeine Bestimmungen seit 02.02.2025, GPAI seit 02.08.2025, Hochrisiko ab 02.08.2026) |

## 7. Risiko-Einschätzung

| Risiko | Wahrscheinlichkeit | Auswirkung | Maßnahme |
| --- | --- | --- | --- |
| BaFin stuft Token als Wertpapier ein | mittel | hoch (WpPG-Prospektpflicht) | Vorabklärung vor Emission |
| KI-System fällt unter Hochrisiko | gering | hoch (Konformitätsbewertung erforderlich) | Use Case bewusst halten |
| DSGVO-Verstoß bei Trainingsdaten | mittel | mittel (Bußgeld) | Datenherkunft prüfen |
| GwG-Pflichten bei Token-Geschäft | mittel | mittel | Geldwäschebeauftragter ab CASP-Start |
| Open-Source-Lizenzkonflikt im Repository | gering | mittel | IP-Audit vor Closing |

## 8. Verantwortlich

- Aylin Soeren: Gesamtverantwortung, Kontakt BaFin und Datenschutzbehörden
- Mira Holzbach: Datenschutz und Datenherkunft
- Jonas Kreutzberger: technische Compliance, IT-Sicherheit, Energieverbrauch
- externer Compliance-Berater wird ab Q4 2026 hinzugezogen

## 9. Fazit

NeuroChain Labs bewegt sich an der Schnittstelle dreier Regulierungsregime (Krypto, KI, Datenschutz). Eine vorausschauende, dokumentierte Compliance-Strategie ist Voraussetzung für jede Token-Emission. Bis zur BaFin-Vorabklärung und einem positiven Whitepaper-Check **keine** öffentliche Token-Ausgabe. Bis dahin operiert die Gesellschaft als reines Softwareunternehmen.
