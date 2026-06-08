---
name: data-act-roboterdaten
description: "Prüft Data-Act-Fragen bei vernetzten Robotern: Nutzerdatenzugang, B2B-Datenbereitstellung, Geschäftsgeheimnisse und Cloudwechsel."
---

# Data Act bei vernetzten Robotern

## Fachkern: Data Act bei vernetzten Robotern
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Der Data Act (VO (EU) 2023/2854) ist seit 11.01.2024 in Kraft und gilt überwiegend ab 12.09.2025 (Art. 50). Vernetzte Roboter (industriell, im Service, im Haushalt) sind "connected products" i. S. d. Art. 2 Nr. 5 Data Act. Das löst Pflichten aus: Nutzerzugang zu den vom Produkt erzeugten Daten (Art. 4), Bereitstellung an Dritte auf Verlangen des Nutzers (Art. 5), B2G-Datenzugang bei besonderen Notlagen (Art. 14 ff.), Vertragsregeln bei B2B (Art. 13 unlautere Klauseln), Cloud-Switching (Art. 23 ff.) sowie Interoperabilität (Art. 28 ff.). Dieser Skill ordnet die Pflichten und gibt Vertragsbausteine.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller des vernetzten Roboters, Datenhalter, Nutzer (B2B oder B2C), Drittanbieter, Cloud-Anbieter, öffentliche Stelle.
2. **Rolle der Daten:** Predictive Maintenance, Performance-Optimierung, Trainingsdaten für KI, Servicegeschäft.
3. **Anlass:** Auskunftsanspruch des Kunden, Datenfreigabe an Dritten, Cloud-Switch, Vertragsverhandlung, behördlicher Datenzugriff.
4. **Geschäftsgeheimnisse:** Welche Datenkategorien sind Trade Secrets?
5. **Vertragslage:** Bestehende AGB, Lizenzbedingungen, AVV, Datennutzungsbestimmungen.

## Rechtlicher Rahmen

- **Data Act** VO (EU) 2023/2854; Kerngeltung ab 12.09.2025.
- Art. 3 Design- und Transparenzpflicht (Daten vom Produkt unmittelbar zugänglich oder spätestens auf Verlangen).
- Art. 4 Nutzerzugang.
- Art. 5 Datenfreigabe an Dritte.
- Art. 13 Unlautere Vertragsklauseln im B2B.
- Art. 14-22 B2G-Datenzugang bei "exzeptioneller Notwendigkeit".
- Art. 23-31 Cloud-Switching (Wechselrecht innerhalb 30 Tagen, Gebührenstaffel).
- Art. 28-30 Interoperabilität gemeinsamer Datenräume.
- **DSGVO** bleibt unberührt (Art. 1 Abs. 5 Data Act).
- **GeschGehG** §§ 1, 17 GeschGehG / VO Trade Secrets (RL (EU) 2016/943).
- **VO (EU) 2024/1689 (KI-VO)** Art. 10 zur Datenqualität.

## Schritt für Schritt

1. **Klassifizierung.** Ist der Roboter "connected product"? Sind Daten "produktgenerierte Daten" oder rein abgeleitete?
2. **Datenkatalog.** Welche Datenarten entstehen? Welche sind schon heute Bestandteil des Datenmodells?
3. **Datenzugang vorgehalten** Art. 3 Abs. 1: Daten sollen "by design" zugänglich sein; falls nicht praktikabel, Auskunfts- und Bereitstellungs-Pfad definieren.
4. **Vorvertragliche Information** Art. 3 Abs. 2: Datenarten, Speicherort, Zugriffsmöglichkeiten, Drittweitergaben.
5. **Nutzerzugang-Prozess** Art. 4: Anforderung, Identitätsprüfung, "ohne unangemessene Verzögerung", maschinenlesbar wenn möglich.
6. **Dritter-Bereitstellung** Art. 5: nur auf Verlangen des Nutzers, "fair, reasonable, transparent" Bedingungen (FRAND-Logik); Schutz von Geschäftsgeheimnissen Art. 5 Abs. 8.
7. **B2B-Verträge** Art. 13 prüfen auf unlautere Klauseln; Vorsicht bei einseitigen Klauseln gegen KMU.
8. **Cloud-Switching** Art. 23 ff.: Vertragsklauseln auf Wechselrecht und Datenexport; Gebührensenkung nach Übergangsphase.
9. **Geschäftsgeheimnisschutz**: Vereinbarungen mit Drittnutzer auf Schutzmaßnahmen, NDA, technische Schutzvorkehrungen.

## Trade-off-Matrix

| Frage | Restriktiv (Hersteller-Sicht) | Liberal (Nutzer-Sicht) | Empfehlung |
|---|---|---|---|
| Datenzugriff "by design" | nur per Antrag | direkt im Cobot-Display | mind. API auf Wunsch innerhalb 7 Tagen |
| Trade-Secrets-Schutz | breit | eng | konkret bezeichnete TS-Kategorien dokumentieren |
| Drittfreigabe-Bedingungen | hohe Gebühren | kostenfrei | Selbstkosten plus angemessener Aufschlag (Art. 9) |
| Cloud-Switch-Frist | 90 Tage | sofort | gestaffelt; 30 Tage Standard |

## Praxistipps

- **Data Catalog** für jedes Produkt.
- **API-Endpunkt** standardisiert.
- **Geschäftsgeheimnis-Markierung** in der Datenstruktur.
- **Vorlage für Nutzer-Anforderungen** in der Anleitung.
- **AGB** mit Drittnutzungsregeln, FRAND-konform.

## Mustertexte

**Vorvertragliche Information Art. 3 Abs. 2 (Auszug):**

> Daten und Datenarten: Sensor-Telemetrie (Position, Temperatur, Vibration), Bedien-Logs, Wartungsereignisse, KI-Modell-Konfidenzwerte. Speicherung: lokal auf dem Roboter (rolling 30 Tage), zusätzlich beim Anbieter (180 Tage). Zugang: Selbstauskunft des Nutzers via Web-Portal; auf Wunsch Datenexport als CSV/Parquet. Drittweitergabe: nur auf Verlangen des Nutzers gemäß Art. 5 Data Act. Geschäftsgeheimnisse: KI-Modellparameter und Service-Algorithmen ausgenommen.

**Vertragsklausel Drittnutzer:**

> Der Drittnutzer erhält Zugang zu den vom Nutzer freigegebenen Daten zum Zweck [Predictive Maintenance Vertragspartner]. Bedingungen: technische und organisatorische Schutzmaßnahmen (mind. ISO/IEC 27001), Geheimhaltungsverpflichtung, Nutzung ausschließlich für den vereinbarten Zweck. Vergütung: Selbstkosten plus angemessener Aufschlag gemäß Art. 9 Data Act. Bei Verstoß: sofortige Sperrung; Vertragsstrafe 50.000 EUR je Verstoß.

## Typische Fehler

- **"Daten gehören uns"-Klauseln** in B2B-AGB – Art. 13 Data Act-widrig.
- **Vorvertragliche Information fehlt** – Bußgeld nach § 7 ff. BfDI-Vollzugsmodell.
- **Cloud-Switching-Klauseln** mit überhöhten Gebühren oder Sperrfristen.
- **Geschäftsgeheimnis-Vorhaben pauschal** angenommen – Art. 5 verlangt konkrete Schutzbedürftigkeit.
- **Datenexport nur in proprietären Formaten** – Interoperabilitätspflicht verletzt.

## Querverweise

- `datenminimierung-edge-cloud`
- `beweislast-und-offenlegung-produkthaftung`
- `cra-produkt-mit-digitalen-elementen`

## Quellen Stand 06/2026

- VO (EU) 2023/2854 (Data Act), Art. 3, 4, 5, 9, 13, 14-22, 23-31, 50.
- DSGVO.
- GeschGehG; RL (EU) 2016/943.
- VO (EU) 2024/1689 (KI-VO), Art. 10.
- Live-Verifikation auf eur-lex.europa.eu, edpb.europa.eu, BfDI; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
