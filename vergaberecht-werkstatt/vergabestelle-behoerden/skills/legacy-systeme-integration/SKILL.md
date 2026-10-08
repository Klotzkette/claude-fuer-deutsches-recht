---
name: legacy-systeme-integration
description: 'Vergabestellen verbinden Bauwerks-, Zustands-, Planungs-, BIM-, Kosten-, SAP-, AVA-, DMS-, eForms-, Portal- und MCP-Daten mit Bedarf, Schätzung, Los, LV, Kriterium, Wertung und Vergabeakte. Bei Dateien, API-Exporten, Systemkonflikten, Rückschreiben oder Uploads automatisch einsetzen.'
---

# Systemquellen in eine vergabefeste Entscheidung überführen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Automatisch einsetzen

Dieser Skill ist der Erstpfad, sobald ein Fallordner Fachsystemexporte, alte Tabellen, Scans, GAEB/XML, SAP-Daten, Bauwerks-/Zustandsdaten, Plan-/BIM-Modelle, Kosten-/Nachtragsdaten, Portalstände, API-Antworten oder MCP-Werkzeugdaten enthält. Nicht auf eine ausdrückliche Bitte um Integration warten.

Für die Feld- und Übergaberegeln sofort [`LEGACY-SYSTEME-INTEGRATION.md`](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden. Wenn die Daten Bedarf, Priorisierung, Bündelung, LV oder Bestwertung tragen, zusätzlich `wirklichkeitsdaten-beschaffung-steuern` nutzen.

## Erste 90 Sekunden

1. Eingänge unverändert inventarisieren: Datei/Endpunkt, System, Modul, Datenhalter, Exportzeit, Zeitzone, Schema, Version und Hash.
2. Rolle jedes Datensatzes bestimmen: führende Fachquelle, veröffentlichter Stand, Aktenbeleg, Arbeitshypothese oder technische Rückmeldung.
3. Feldautorität festlegen: Welches System darf Objekt-ID, Zustand, Menge, Preisbasis, Frist, Kriterium, Punktzahl oder Bekanntmachungsstand führen?
4. Rechtszweck zuordnen: Bedarf, Schätzung, Los, LV, Eignung, Zuschlag, Aufklärung, Veröffentlichung oder Dokumentation.
5. Konflikte sperren: widersprüchliche Versionen, Einheiten, Mengen, Nullwerte und Datumsfelder nicht still auflösen.
6. Einen ersten Output wählen: Quellenmatrix, Datenqualitätsbericht, LV-Übergabe, Kriterienvermerk, eForms-Paket oder Vergabeaktenvermerk.

## Rollenbezogene Quellenkarte

| Eingang | Erstes Mapping | Pflichtkontrolle | Behördenoutput |
|---|---|---|---|
| SIB-/Anlagenregister, PMS/BMS, Prüfbericht | Objekt, Bauteil, Zustand, Schaden, Prüfung | Objekt-ID, Prüfdatum, Messmethode, Fachfreigabe | Bedarfs- und Priorisierungsvermerk |
| EPING-nahe Planung, Bestandsplan, BIM/IFC, VESTRA/OKSTRA | Arbeitsblock, Menge, Schnittstelle, Korridor, Sperrfenster | Plan-/Modellstand, Einheit, Geometrie, Genehmigung | LV-Vorbereitungsblatt und Loskarte |
| SAP/MACH/proDoppik, Kosten, Nachträge, Bauzeiten | Budget, Preisbasis, Option, Risiko, Lebenszyklus | Leistungsidentität, Index, Umsatzsteuer, Laufzeit, Ausreißer | Auftragswert- und Szenariovermerk |
| iTWO/ORCA/California, GAEB | Los, OZ, Menge, Einheit, Langtext, Preisfeld | Austauschphase, Rundung, Bedarfsposition, Lesefassung | validiertes X83-/LV-Paket |
| DMS/eAkte/SharePoint/E-Mail | Version, Freigabe, Aktenstelle, Kommunikation | führender Stand, Rechte, Header, Hash | Aktenverzeichnis und Freigabekette |
| eForms/TED/DVAL/E-Vergabe | Notice, CPV, Los, Frist, Link, Nachricht | veröffentlichter Stand, Pflichtfeld, direkte Zugänglichkeit | Notice-/Uploadpaket und Quittung |
| Klima, Umwelt, Normen, Recht | externer Befund, Stichtag, Geltungsbereich | amtliche Quelle, räumlicher/sachlicher Bezug, Lizenz | Kriterien- oder Risikovermerk |

## Entscheidungsbrücke

Für jedes tragende Feld genau eine Zeile erzeugen:

| Quelle/Feld | gesicherte Tatsache | Annahme oder Transformation | Norm/Fallanker | Entscheidung | Aktenbeleg |
|---|---|---|---|---|---|
| [System und Feld] | [Wert, Einheit, Stand] | [Regel und Unsicherheit] | [Norm/Entscheidung] | [Bedarf, Los, LV, Kriterium] | [Datei, Seite, Hash] |

Keine Entscheidung ausgeben, wenn Quelle, Zeitbezug, Einheit oder Transformation fehlen. Dann stattdessen eine gezielte Fachfreigabe oder Datenanforderung formulieren.

## Rechtsprechungsgates

1. **Technische Detailvorgabe:** Nach § 31 VgV und EuGH, 16.04.2026, C-568/24, *Sof Medica*, prüfen, ob Typ-, System- oder Schnittstellenbezug unvermeidbar aus dem Auftragsgegenstand folgt. Sonst `oder gleichwertig`, Funktionsanforderung und prüfbaren Nachweisweg vorsehen.
2. **Bestandskompatibilität:** OLG Düsseldorf, 10.07.2024, Verg 2/24, erlaubt eine konkrete Kompatibilitäts- und Systemsicherheitsbegründung. Deshalb Bestandsarchitektur, Schnittstelle, Migrationsaufwand, Fehlfunktions- und Gewährleistungsrisiko belegen; bloßes `Legacy-System vorhanden` genügt nicht.
3. **Unterlagenzugang:** § 41 VgV und OLG Düsseldorf, 13.05.2019, Verg 47/18, verlangen vollständigen, direkten und im Kern medienbruchfreien Zugang. Abhängige Pläne, Normauszüge oder Modelle als erreichbaren Unterlagenbestand und Version ausweisen.
4. **Datenbasierte Wertung:** §§ 127 GWB, 58 VgV und OLG Düsseldorf, 24.03.2021, Verg 34/20: Rechenwert, Punktzahl oder Systemlog nie ohne konkrete qualitative Erwägung, Eingabebeleg und Quervergleich übernehmen.
5. **Unveränderbarer Angebotsstand:** EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, betrifft unmittelbar eine EU-Eigenvergabe. Im deutschen Verfahren nur als Integritätsanker neben § 53 VgV und der konkreten Portalvorgabe verwenden: verlangte Uploads fristfest und der Bieterkontrolle nach Fristablauf entzogen gestalten.

## Rückschreib- und Uploadpfad

1. Zielobjekt und Operationsart benennen: anlegen, ergänzen, ersetzen, berichtigen oder nur validieren.
2. Idempotenzschlüssel festlegen: Vergabenummer, Los, Dokument-ID, Version und Hash.
3. Native Datei plus Lesefassung, Mapping-Manifest, Delta und Freigabeblatt bilden.
4. Schema-, Pflichtfeld-, Roundtrip- und Berechtigungstest durchführen.
5. Fach-, Vergabe- und Systemfreigabe getrennt protokollieren.
6. Upload/Import/Veröffentlichung erst nach ausdrücklicher Freigabe ausführen.
7. Empfangs-ID, Zielhash, Zeitstempel, Fehler, Teilannahme und Rollbackstatus in die Vergabeakte zurückführen.

## Last- und Fortsetzungsregel

- Ab 50 Dateien oder 250 MB Metadaten vor Inhalten lesen und in Paketen von höchstens 20 Dateien oder 100 MB arbeiten.
- Große Modelle, GAEB-, PDF- und Office-Dateien einzeln verarbeiten. Parallel nur Inventar- und Prüfschritte ausführen, die keine Vollkonvertierung benötigen.
- Für jedes Paket `Quelle | Hash | Status | Mapping | Fehler | Freigabe | nächster Lauf` speichern; unveränderte Quellen nicht erneut auslesen.
- Ein fehlerhafter Export sperrt nur die davon abhängige Behördenentscheidung. Andere Quellen und Entscheidungen werden weiterbearbeitet.
- Nach Unterbrechung am letzten vollständigen Paket fortsetzen; Rückschreiben und produktiven Upload nie automatisch wiederholen.

## Stoppsignale

- Quelle oder Nutzerrecht unklar: nur lesen, nicht verbinden oder exportieren.
- Personen-/Geschäftsgeheimnisse ohne Rechtszweck: separieren und Zugriff begrenzen.
- Historische Anbieterbewertung soll verdeckt werten: stoppen und transparentes Kriterium oder Nichtverwendung empfehlen.
- Systemkonflikt betrifft Menge, Auftragswert, Frist, Los oder Zuschlag: Entscheidung bis zur Fachklärung sperren.
- Native Datei kann nicht schemafest erzeugt werden: fachliche Datentabelle liefern und Konverter-/Portalvalidierung ausdrücklich offenlassen.

## Pflichtoutput

Liefere in dieser Reihenfolge:

1. Quellen- und Systeminventar.
2. Feldautoritäts- und Datenqualitätsmatrix.
3. Entscheidungsbrücke mit Norm und Aktenbeleg.
4. Konflikt-/Delta-Liste.
5. Export- oder Uploadauftrag mit Freigabe und Rückkanal.
6. Ausgefüllte Vorlage [`systemuebergabe-entscheidungsdaten.md`](../../assets/templates/systemuebergabe-entscheidungsdaten.md).
