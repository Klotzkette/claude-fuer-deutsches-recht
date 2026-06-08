---
name: batterie-ladeinfrastruktur-und-brandschutz
description: "Prüft Batterie, Ladeinfrastruktur, Brandschutz, Transport, Lagerung, Rückruf und Versicherungsfragen bei mobilen Robotern."
---

# Batterie, Ladeinfrastruktur und Brandschutz bei mobilen Robotern

## Fachkern: Batterie, Ladeinfrastruktur und Brandschutz bei mobilen Robotern
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Mobile Roboter (AMR, AGV, Liefer-, Reinigungs-, Mähroboter) werden überwiegend mit Lithium-Ionen-Akkus betrieben. Die Folge: erhebliche Anforderungen aus der Batterie-VO (EU) 2023/1542, dem Gefahrgutrecht (ADR/UN 38.3), dem vorbeugenden Brandschutz (Landesbauordnungen, Sachversicherer-Bedingungen VdS), der ProdSG/MaschinenVO sowie spezifische Pflichten bei Rückruf und Versicherung. Dieser Skill ordnet die Schichten und gibt praxisnahe Vorlagen für Lagerkonzept und Rückruf.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, Distributor, Betreiber, Versicherer, Feuerwehr, Berufsgenossenschaft.
2. **Zellchemie:** Li-Ion (NMC, LFP), Festkörper, Bleisäure, NiMH; Spannung, Kapazität (kWh)?
3. **Lebenszyklus-Phase:** Entwicklung, Inverkehrbringen, Betrieb, Wartung, Defekt, Rücknahme.
4. **Anlass:** Brandvorfall, Versicherer-Audit, neue Lagerhalle, Rückrufentscheidung, Transportgenehmigung.
5. **Unterlagen:** Batterie-Datenblatt, Zertifikate UN 38.3, Sicherheitsdatenblatt, Konformitätserklärung, Versicherungsbedingungen, VdS-Auflagen.

## Rechtlicher Rahmen

- **Batterie-VO** VO (EU) 2023/1542; gestaffeltes Inkrafttreten, Kennzeichnungspflichten ab 18.08.2026, CE für bestimmte Batteriekategorien.
- **MaschinenVO** VO (EU) 2023/1230 als Gesamtmaschine; Schnittstelle zur Batterie als Komponente.
- **ProdSG** allgemeine Produktsicherheit; **GPSR** VO (EU) 2023/988 seit 13.12.2024 Geltung.
- **CRA** VO (EU) 2024/2847 bei vernetztem Batterie-Management-System.
- **ADR** Gefahrgutrecht (UN 3480 Li-Ionen, UN 3481 Li-Ionen mit Ausrüstung), UN-Tests 38.3.
- **Landesbauordnungen / Verkaufsstättenverordnungen / IndBauR** Brandabschnitte, Löschanlagen.
- **VdS-Bedingungen** (VdS 3103, VdS 3856) zu Li-Ion-Lagerung.
- **ProdHaftG / VO (EU) 2024/2853** Produkthaftung, § 823 BGB.

## Schritt für Schritt

1. **Zellklassifizierung.** Energie pro Zelle und Pack, Chemie, Brandverhalten (Thermal Runaway).
2. **Konformität.** Batterie-VO, MaschinenVO, ggf. CRA, UN 38.3 Transportsicherheit.
3. **Brandschutzkonzept.** Trennung Lager und Betrieb, Brandlasten, Sprinkler/Inertgas, Quarantäne-Container für defekte Akkus.
4. **Lade-/Ruheorte.** Idealerweise im Außenbereich oder eigenem Brandabschnitt; Trennung von hochbelegten Bereichen.
5. **Wartung.** Periodische Kapazitäts- und Innenwiderstandsmessung; Austauschintervalle; Logging.
6. **Transport.** ADR-Klassifizierung, Verpackung, Begleitdokumente.
7. **Rückruf-Vorbereitung.** Wenn Defektmuster erkennbar: Vigilanz-Meldung, Markträcknahme; nach Safety-Gate-Portal.
8. **Versicherung.** VdS-Auflagen früh klären; Selbstbehalt bei Li-Ion oft erheblich.
9. **Entsorgung.** Annahmeverpflichtung, Rücknahmesystem Batterie-VO Art. 54 ff.

## Trade-off-Matrix

| Frage | Sicher | Wirtschaftlich | Empfehlung |
|---|---|---|---|
| Lagerkapazität pro Brandabschnitt | gering | hoch | nach VdS 3103 abstufen; großzügig dimensionieren |
| Inert-Löschanlage | teuer, sicher | konventionell | bei großen Lägern Inert; sonst Wasser-Mist mit Detektion |
| Zellchemie | LFP (sicherer) | NMC (höhere Energie) | für stationäre/sicherheitssensible Anwendungen LFP bevorzugen |
| Cloud-Telemetrie BMS | proaktiv, Datenschutzrisiko | offline, blinder Fleck | hybrid: Telemetrie nur sicherheitsrelevant, datensparsam |

## Praxistipps

- **Quarantäne-Container** mit Sandfüllung für defekte Akkus.
- **Frühwarnindikatoren BMS**: Temperatur, Innenwiderstand, Spannungsdrift; Schwellwerte protokollieren.
- **Feuerwehr informieren** vor Erstbetrieb; Übungen.
- **Sachverständige (Brandschutz, VdS)** einbinden.
- **Logistik**: ADR-Schulung der Fahrer; Sicherheitsdatenblatt im LKW.

## Mustertexte

**Lagerordnung Li-Ion (Auszug):**

> 1. Lagerung ausschließlich im Brandabschnitt "Akku-Lager Halle 7" gemäß Brandschutzkonzept Stand [Datum].
> 2. Maximale Lagermenge: 250 kWh nominale Energie.
> 3. Defekte oder geblähte Zellen werden unverzüglich im Quarantäne-Container Stellplatz Q1 isoliert. Verständigung der Sicherheitsfachkraft binnen 15 Minuten.
> 4. Ladeplätze: ausschließlich an gekennzeichneten Stationen; nie über Nacht ohne automatische Trennung.
> 5. Brandschutzeinrichtungen: Rauchmelder, Wärmemelder, Wassernebellöschanlage, Brandfrüherkennung über BMS-Telemetrie.

**Rückrufankündigung (Auszug):**

> Nach Hinweisen auf erhöhte Thermal-Runaway-Quote bei Serie [XYZ] zwischen [Produktionsdatum von/bis] rufen wir die betroffenen Akku-Packs zurück. Bitte stellen Sie den Betrieb der betroffenen Roboter unverzüglich ein und kontaktieren Sie uns über [Hotline]. Wir senden eine ADR-konforme Versandbox und stellen einen Austausch-Akku binnen 5 Werktagen bereit.

## Typische Fehler

- **Lagerung von Li-Ion bei sonstiger Lagerware** ohne Brandabschnitt.
- **Ladestationen in Fluchtwegen** – LBO-Verstoß.
- **Kein Rückrufprozess** vorab definiert – im Ernstfall Eskalation.
- **Versicherer nicht informiert** bei neuer Lagermenge – Deckungsausschluss.
- **ADR-Verstöße** beim Versand defekter Zellen.

## Querverweise

- `ce-zeichen-fehlgebrauch-und-abmahnung`
- `cra-produkt-mit-digitalen-elementen`
- `robotik-recht-allgemein`

## Quellen Stand 06/2026

- VO (EU) 2023/1542 (Batterie-VO).
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2023/988 (GPSR).
- VO (EU) 2024/2847 (CRA).
- ADR 2025; UN 38.3.
- Landesbauordnungen; IndBauR; VdS 3103, VdS 3856.
- VO (EU) 2024/2853 (neue ProdHaftRL); § 823 BGB.
- Live-Verifikation auf eur-lex.europa.eu, baua.de, vds.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EU) 2023/1230 (Maschinenverordnung)
- Art. 6 AI-Act (Hochrisiko-KI)
- §§ 1-19 ProdHaftG
- RL (EU) 2024/2853 (neue Produkthaftungs-RL)
