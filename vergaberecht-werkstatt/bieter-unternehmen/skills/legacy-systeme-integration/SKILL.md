---
name: legacy-systeme-integration
description: 'Bieter verbinden SAP-, ERP-, CRM-, HR-, AVA-, DMS-, GAEB-, Portal-, API- und MCP-Daten mit Preis, LV, Referenz, Personal, Konzept, Nachweis, Rüge und Abgabe. Bei Altdateien, Live-Systemen, Angebotsfreeze, Datenmapping, Formatkonflikt oder Portalübergabe automatisch einsetzen.'
---

# Unternehmensdaten in ein fristfestes Angebot überführen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Automatisch einsetzen

Dieser Skill ist der Erstpfad, wenn ein Angebotsordner ERP-/CRM-/HR-/AVA-/DMS-Exporte, alte Excel-Kalkulationen, GAEB/XML, Zertifikate, Referenzlisten, Portaldateien, APIs oder MCP-Werkzeugdaten enthält. Nicht warten, bis der Nutzer einen Systemnamen nennt: Dateiformat, Metadaten und Feldstruktur reichen als Trigger.

Sofort [`LEGACY-SYSTEME-INTEGRATION.md`](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden. Für Unterlagenanalyse zusätzlich `unterlagen-und-lv-datenformate-auslesen`, für die fertige Abgabe `angebot-in-vorgegebenem-format-erstellen` einsetzen.

## Erste 90 Sekunden

1. Verbindliche Vergabeunterlagenversion, Los, Angebotsfrist und Rückgabeformat feststellen.
2. Unternehmensquellen read-only inventarisieren: System, Modul, Export, Stichtag, Zeitzone, Schema, Version, Hash und Verantwortlicher.
3. Angebotsfelder bilden: OZ/Preis, Referenz, Personal, Zertifikat, Konzept/SLA, Erklärung, Rügepunkt und Uploadbestandteil.
4. Feldautorität bestimmen: Kalkulation statt Listenpreis, Projektakte statt CRM-Kurztext, Ressourcenfreigabe statt bloßer HR-Stammsatz.
5. Konflikte und Lücken sperren: Einheit, Währung, Steuer, Rundung, Gültigkeit, Verfügbarkeit und Unterlagenversion.
6. Freeze-Zeitpunkt und einen ersten Output festlegen: Preisblatt, Nachweismatrix, Referenzpaket, Konzeptbeleg, Bieterfrage/Rüge oder Uploadpaket.

## Quellkarte

| Quelle | Angebotsziel | Pflichtkontrolle | Output |
|---|---|---|---|
| SAP/ERP/Material/Kondition | Artikel, Preisbasis, Lieferweg | Gültigkeit, Einheit, Währung, Steuer, Konditionsfolge | Kalkulationsbrücke |
| AVA/GAEB/Excel | OZ, Menge, Einheitspreis, Zuschlag/Nachlass | X83/X84, Formel, Rundung, Positionsvollständigkeit | natives Preis-/LV-Paket |
| CRM/Projektakte | Referenz, Ansprechpartner, Leistungsumfang | Vergleichbarkeit, Zeitraum, Bestätigung, Einwilligung | Referenzmatrix und Beleg |
| HR/Ressourcenplanung | Rolle, Qualifikation, Verfügbarkeit | Stichtag, Doppelverplanung, Datenschutz, Bindung | Personaleinsatz- und Nachweismatrix |
| DMS/Zertifikatsablage | Eigenerklärung, Zertifikat, Vollmacht, Konzept | Gültigkeit, Geltungsbereich, Signatur, Version | Anlagen- und Gültigkeitsliste |
| Portal/E-Mail/API/MCP | Unterlage, Frage, Rüge, Upload, Quittung | Nutzerrolle, Frist, Schema, Serverzeit, Eingang | Abgabeauftrag und Beleg |

## Angebotsmapping

| Quellfeld | gefordertes Feld/Fundstelle | Transformation | Nachweis/Freigabe | Risiko | Zieldatei |
|---|---|---|---|---|---|
| [System, ID, Wert] | [Unterlage, Seite, OZ] | [Einheit/Rundung/keine] | [Beleg und Verantwortlicher] | [Ausschluss/Wertung/Geheimnis] | [GAEB/XML/XLSX/PDF] |

Jede Angebotsaussage braucht eine nachvollziehbare Kette bis zur Unternehmensquelle. Bei nicht belastbarer Quelle keine plausible Zahl ergänzen, sondern Lücke und Lösung ausgeben.

## Rechtsprechungsgates

1. **Upload statt Live-Link:** EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, ECLI:EU:C:2025:523, betrifft unmittelbar eine EU-Eigenvergabe. Im deutschen Verfahren nur als Integritätsanker neben § 53 VgV und der konkreten Portalvorgabe nutzen: Verlangte Bestandteile fristfest hochladen, Webdemo und Repository-Link nur ergänzend verwenden.
2. **Gleichwertige Systemlösung:** § 31 VgV, EuGH, 16.04.2026, C-568/24, *Sof Medica*, und EuGH, 16.01.2025, C-424/23, *DYKA Plastics*. Typ-/Schnittstellensperre feldgenau identifizieren, funktionale Gleichwertigkeit und Nachweisweg liefern, Rügefrist sichern.
3. **Bestandskompatibilität ernst nehmen:** OLG Düsseldorf, 10.07.2024, Verg 2/24. Alternative nicht nur behaupten; Anschlussarchitektur, Migrationsschritt, Systemsicherheit, Gewährleistung und Kostenwirkung belegen.
4. **Unterlagenzugang:** § 41 VgV, OLG Düsseldorf, 13.05.2019, Verg 47/18. Fehlende oder nur über Umwege erreichbare Anlagen sofort protokollieren und Bieterfrage/Rüge prüfen.
5. **Indizienangriff:** OLG Düsseldorf, 12.06.2024, Verg 36/23. Bei Konkurrenzangebot oder internem Behördenvorgang darf begrenzter Einblick berücksichtigt werden, aber Tatsachenkern, Erkenntnisquelle und plausible Zuschlagsfolge konkretisieren.

## Freeze- und Abgabepfad

1. Freeze-ID: Vergabenummer, Los, Angebotsversion, Datum/Uhrzeit und Zeitzone.
2. Verbindliche Dateien, Lesefassungen und nur ergänzende Links unterscheiden.
3. Hashliste und Inhaltsverzeichnis erzeugen; jede Anlage einer Unterlagenpflicht zuordnen.
4. Fachfreigaben getrennt sichern: Kalkulation, Vertrieb, Personal, Compliance, Zeichnungsberechtigter.
5. Schema-, Formel-, Viren-, Größen-, Namens-, Signatur- und Roundtrip-Test durchführen.
6. Nach jeder Änderung neues Delta, neue betroffene Hashes und erforderliche Freigaben ausgeben.
7. Produktive Abgabe nur auf ausdrückliche Freigabe; anschließend Portalquittung, Serverzeit, Upload-ID und angenommene Dateiliste gegen Freeze prüfen.

## Last- und Fortsetzungsregel

- Ab 50 Dateien oder 250 MB Metadaten vor Inhalten lesen und in Paketen von höchstens 20 Dateien oder 100 MB arbeiten.
- Große GAEB-, PDF- und Office-Dateien einzeln verarbeiten. Parallel nur Inventar- und Prüfschritte ausführen, die keine Vollkonvertierung benötigen.
- Für jedes Paket `Quelle | Hash | Status | Angebotsfeld | Fehler | Freigabe | nächster Lauf` speichern; unveränderte Quellen nicht erneut auslesen.
- Ein fehlerhafter Export sperrt nur den davon abhängigen Angebotsbestandteil. Fristprüfung und übrige Angebotsarbeit werden fortgesetzt.
- Nach Unterbrechung am letzten vollständigen Paket fortsetzen; Angebotsfreeze oder produktiven Upload nie automatisch wiederholen.

## Stoppsignale

- Angebotsnachweis liegt nur in einem veränderbaren Link.
- ERP-/CRM-/HR-Datum ist veraltet oder widerspricht der Erklärung.
- Preisblatt, GAEB und Angebotsformular haben verschiedene Summen.
- Zertifikat ist abgelaufen oder deckt das Los nicht.
- benannte Person ist nicht freigegeben oder nicht verfügbar.
- produktive Portalaktion ist nicht ausdrücklich autorisiert.

## Pflichtoutput

Liefere in dieser Reihenfolge:

1. Quell- und Angebotsmapping.
2. Nachweis-/Gültigkeits- und Konfliktmatrix.
3. Angebotsfreeze mit Hashliste und Freigabestatus.
4. Format-/Roundtrip-Bericht.
5. Uploadauftrag und Quittungsabgleich.
6. Ausgefüllte Vorlage [`angebotsfreeze-systemuebergabe.md`](../../assets/templates/angebotsfreeze-systemuebergabe.md).
