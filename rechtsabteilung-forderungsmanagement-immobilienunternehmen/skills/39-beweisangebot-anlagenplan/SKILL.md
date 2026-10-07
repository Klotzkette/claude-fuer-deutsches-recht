---
name: 39-beweisangebot-anlagenplan
description: "Beweisangebote und fortlaufenden Anlagenplan für Klage, Replik und Verteidigung erzeugen. Ordnet jede erhebliche Tatsache einem zulässigen Beweismittel, Beweislast, Original, K- oder B-Nummer, Dateiversion und Beschaffungsstatus zu. Nutzen vor Schriftsatzfinalisierung oder beA-Paket. Output Beweismatrix, Anlagenmanifest und stabile Übergabe an die Dokumentenproduktion."
---

# Beweisangebot und gerichtsfester Anlagenplan

## Zweck und Anwendungsfall

Dieser Skill macht aus Tatsachenvortrag einen prüfbaren Beweis- und Anlagenbestand. Er wird vor Klage, Replik, Verteidigung und jeder Einreichung geladen, wenn Beweise, Anlagen K/B, fehlende Belege oder eine fortlaufende Nummerierung zu ordnen sind. Sein Anlagenmanifest ist die verbindliche Übergabe an Skill `23-klage-egvp-bea-einreichen`.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Nutze Tabellen, klare Lückenfragen und Ampeln. Erfinde keine Zeugen, Anlagen, Zugänge oder Dateiinhalte.

## Eingaben

- Aktueller Klage-, Replik-, Erwiderungs- oder Antragsentwurf.
- Belegmatrix, SAP-/Mietkontoausgaben, Vertrag, Korrespondenz, Zustellnachweise und Gerichtsakte.
- Liste aller bereits eingereichten K- und B-Anlagen mit Schriftsatzdatum.
- Originaldateien, Dokument-IDs, Versionen und Ansprechpartner für fehlende Unterlagen.

## Ablauf / Checkliste

1. Jede entscheidungserhebliche Tatsachenbehauptung im Schriftsatz markieren und in eine Tatsachen-ID überführen.
2. Beweislast und Bestreitensstand festhalten: eigene Darlegung, gegnerisches Bestreiten, sekundäre Darlegungslast oder gerichtlicher Hinweis.
3. Pro Tatsache das passende Beweismittel nach der ZPO bestimmen: Urkunde, Zeuge, Sachverständiger, Augenschein, Parteivernehmung oder Parteianhörung. Unzulässige Ausforschung nicht als Beweisangebot tarnen.
4. Bei Urkunden Originalquelle, Dokument-ID, Datum, Seiten, Lesbarkeit, Vollständigkeit und Hash erfassen. SAP-Ausdruck, DMS-Kopie und Kontoauszug nicht als dasselbe Original behandeln.
5. Parteirolle bestimmen. Klägeranlagen erhalten `K`, Beklagtenanlagen `B`. Bereits eingereichte Nummern bleiben gesperrt; neue Anlagen setzen die höchste vergebene Nummer fort, auch bei Replik oder weiterem Schriftsatz.
6. Eine Anlage darf mehrere Tatsachen belegen. Mehrere unterschiedliche Dokumente werden nicht nur zur Bequemlichkeit unter derselben Anlagenummer vermischt; ein echtes Konvolut erhält Inhaltsblatt und Seitenlogik.
7. Zeugen nur mit Wahrnehmungsthema, Funktion und ladungsfähiger Anschrift oder konkretem Beschaffungsauftrag aufnehmen. Hörensagen und bloße Aktenkenntnis kennzeichnen.
8. Sachverständigenfragen auf beweisfähige Tatsachen begrenzen. Rechtsfragen, Saldenberechnung und Vertragsauslegung nicht an Sachverständige auslagern. Bei Feuchtigkeit und Schimmel tatsächliche Erscheinung, Zeitraum, Bauzustand, konkrete technische Anknüpfungstatsachen, Zutritt, Möblierung sowie Heiz- und Lüftungsdaten getrennt erfassen; Foto-Vorschau, Originalfoto, Loggerauswertung und Rohmessdaten erhalten jeweils einen eigenen Quellenstatus.
9. Vortrag gegen jede Anlage lesen. Abweichende Beträge, Daten, Parteien, Mietflächen, Zugänge oder Buchungen als rotes Widerspruchsrisiko markieren.
10. Für neue Anlagen einen beA-tauglichen Arbeitsnamen vorschlagen, etwa `02_Anlage_K01_Mietvertrag_2022-05-01.pdf`; endgültige Konvertierung und Kennzeichnung übernimmt Skill `23`.
11. Fehlende Anlage erhält keinen Platzhalter im Nummernkreis. Stattdessen Beschaffungsauftrag mit Quelle, zuständiger Person, Frist und Folge ausgeben.
12. Manifest sperren: Stand, Schriftsatzversion, höchste K-/B-Nummer, neue Nummern, zurückgezogene Nummern und offene Lücken dokumentieren. Nummern nie still neu vergeben.

## Beweis- und Anlagenmatrix

| Tatsachen-ID | Behauptung | Beweislast/Bestreiten | Beweismittel | Anlage | Status | Risiko |
|---|---|---|---|---|---|---|
| T-01 | Miete Juli 2026 offen | Klägerin/bestritten | Mietkonto und Kontoauszug | K 3 | gelb | Storno prüfen |

Technische Herkunft und Beschaffung werden getrennt geführt, damit die Nutzeransicht auch auf kleinen Bildschirmen lesbar bleibt:

| Tatsachen-ID | Original/Quelle | Version/Hash | Seiten | Lesbarkeit | Beschaffung |
|---|---|---|---:|---|---|
| T-01 | SAP/DMS-ID | [Hash] | 2 | geprüft | vollständig |

## Anlagenmanifest für Skill 23

| Reihenfolge | Bezeichnung | Bereits eingereicht | Quelldatei | Seiten | Zielname | Status |
|---|---|---|---|---:|---|---|
| 02 | Anlage K 1 | nein | `Mietvertrag_final.docx` | 12 | `02_Anlage_K01_Mietvertrag_2022-05-01.pdf` | bereit |

Kennzeichnung und Datenschutz stehen je Anlage als kurze Prüfzeile unter dem Manifest, wenn der Status nicht uneingeschränkt bereit ist. Das maschinenlesbare Manifest behält sämtliche technischen Felder.

## Quellenpflicht

Es gelten `references/zitierweise.md`, `references/leitentscheidungen-anker.md`, `references/schriftsatz-und-argumentationsstandard.md`, `references/erv-dokumentenproduktion.md` und die Beweisnormen der ZPO. Rechtsprechungsanker werden vor Verwendung in einer amtlichen oder frei zugänglichen Quelle verifiziert. Keine fiktiven Zeugen, Anlagen, Fundstellen oder Beweislastregeln.

## Ausgabeformat

1. Beweislast- und Bestreitenskarte.
2. Beweis- und Anlagenmatrix.
3. Fortlaufendes Anlagenverzeichnis.
4. Anlagenmanifest für Skill `23` mit Quelle, Version, Hash, Seiten und Zielname.
5. Beschaffungsliste mit Zuständigkeit und Frist.
6. Ampel und genau eine nächste Arbeitsaktion in Klartext.

Schriftsatzbausteine werden vollständig ausformuliert. Eine Tabelle ersetzt nicht das konkrete Beweisangebot im Schriftsatz.

## Beispiele

- Zahlungseingang bestritten: Mietkonto und Bankkontoauszug getrennt zuordnen; Storno und Wertstellung prüfen.
- Kündigungszugang bestritten: Kündigungsschreiben, Botenprotokoll, Einwurfbeleg und Zeuge mit Wahrnehmungsthema erfassen.
- Replik mit neuen Anlagen: K 1 bis K 6 bleiben gesperrt; neue Unterlagen beginnen mit K 7.
- Unlesbarer Scan: gelb, Neuanforderung mit Frist; kein fiktiver Inhalt und keine Einreichungsfreigabe.
