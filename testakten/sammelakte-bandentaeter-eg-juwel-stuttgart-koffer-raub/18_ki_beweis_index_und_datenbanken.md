# Aktenstück 18 — Sonderpaket Effizienz-Tools: KI-Beweis-Index und Datenbanken

**Verfahren:** KLs 4 Js 18.422/26  
**Bearbeitung:** RA Dr. Magnus Schorlemmer / Kanzlei-IT (intern)  
**Gegenstand:** Digitale Aufbereitung der Ermittlungsakte mit KI-gestütztem Beweis-Index und Datenbank-Management  
**Stand:** 10.02.2026

---

## 1. Herausforderung: Beweisverwaltung in Gross-Strafverfahren

Das vorliegende Verfahren umfasst (Stand Februar 2026):
- **4.847 Seiten** Hauptakte (12 Bande)
- **1.247 Seiten** TKUe-Sonderband
- **487 Observationsfotos**
- **34 Videostandbilder** (Stadtcam) + **22 Videostandbilder** (Cafe Westermann)
- **Unzählige EncroChat-Nachrichten** (noch nicht vollständig zugänglich)
- **Mehrere Sachverstaendigengutachten**
- **Internationale Rechtshilfe-Korrespondenz**

Ohne systematische digitale Aufbereitung ist eine effektive Verteidigung in der Hauptverhandlung mit 22 geplanten Verhandlungstagen kaum möglich.

---

## 2. KI-Beweis-Index — Konzept

### 2.1 Technische Umsetzung

Die Kanzlei Dr. Schorlemmer hat ein internes Werkzeug entwickelt, das auf dem Prinzip eines semantischen Such-Index basiert:

**Schritt 1 — OCR und Digitalisierung:**
Alle Aktenbände wurden eingescannt und per OCR (ABBYY FineReader) digitalisiert. Die digitalisierten Texte wurden in ein internes Dokumentenverwaltungssystem (Kanzlei-DMS auf Basis OpenSearch) geladen.

**Schritt 2 — Beweis-Tagging:**
Jedes Dokument erhielt manuelle und semi-automatische Tags:
- Beschuldigter (Korbiel / Drebenstedt / Iordache / Krasniqi / Unbekannt)
- Beweismittelkategorie (Zeuge / Urkunde / Lichtbild / TKUe / FZA / EncroChat / DNA)
- Zeitstempel (Datum des Ereignisses, Datum der Erstellung)
- Beweiswert (belastend / entlastend / neutral)
- Tatbestandselement (Raub / Bande / Verletzung / Geldwaesche / Flucht)

**Schritt 3 — Verknüpfung:**
Automatische Verknüpfung von Dokumenten, die dieselben Personen, Orte, Zeitpunkte oder Spurennummern erwähnen. Ergebnis: Ein Graph der Beweis-Zusammenhänge.

### 2.2 Abfragebeispiele

Anfrage: "Alle belastenden Beweise gegen Korbiel am Tatortbezug 18.10.2025"
→ Index liefert: OB-Lichtbild 141–168; TKUe G-14; FZA-Zelle Korbiel PL-SIM; DNA SP-001; Stadtcam STG-CAM-044 Frame 10:44; Fingerabdruck SP-002.

Anfrage: "Alle Beweise mit zeitlichem Widerspruch oder Einschränkungen"
→ Index liefert: TKUe G-41 (Krasniqi post-Verhaftung); Drebenstedt-Videoidentifizierung 72%; Sternkopf-Gutachten Gegenüberstellung Krasniqi.

---

## 3. Interne Beweis-Datenbank (Zeugenmatrix)

*(Vollständige Tabelle in xlsx/zeugen_beweismittel_matrix.xlsx, Tabellenblatt "Zeugenmatrix")*

Die Zeugenmatrix erfasst alle Zeugen und ihre Aussagerelevanz für jeden Tatbestandsaspekt:

| Zeuge | Korbiel-Ident. | Drebenstedt-Ident. | Krasniqi-Ident. | Tatablauf | Verletzungen | Bandenabrede |
|-------|---------------|-------------------|--------------|-----------|--------------|----|
| Z-01 (Goldhofer-Egenter) | Ja | Nein | Ja | Ja | Ja (eigene) | Nein |
| Z-02 (Aydin) | Nein | Nein | Ja | Ja | Ja (eigene) | Nein |
| Z-04 (Wauer) | Ja | Ja (?) | Nein | Nein | Nein | Nein |
| Z-06 (Zimmermann) | Nein | Nein | Ja | Nein | Nein | Nein |
| Z-08 (KHK Felber) | Ja (indirekt) | Ja | Ja | Ja | Nein | Ja (EG-Ergebnis) |
| Z-11 (KHK Ruoff) | Ja (OB) | Ja (OB-Fahrzeug) | Ja (OB) | Nein | Nein | Ja (Ulm-Treffen) |
| SV-01 (Dr. Reissmann) | Nein | Nein | Nein | Nein | Ja (Gutachten) | Nein |

---

## 4. Risikoanalyse-Modul

Das interne System enthalt ein einfaches Risikoanalyse-Modul, das den Beweisstatus jedes Tatbestandselements bewertet:

| Tatbestandselement | Belastende Beweise | Entlastende Beweise | Risikograd (Verurteilung) |
|-------------------|-------------------|--------------------|----|
| Wegnahme (§ 249 StGB) | DNA, Fingerabdruck, Video | Korbiel bestreitet | Hoch |
| Gefahrl. Werkzeug (§ 250 Abs. 2 Nr. 1) | SP-001 Brecheisen, SP-002 Pfefferspray | — | Sehr hoch |
| Bandenabrede (§ 244a StGB) | TKUe, FZA, OB Ulm-Treffen | EncroChat-Verwertbarkeit unklar | Mittel-hoch |
| Verletzungen (§ 226 StGB Qualifikation) | SV-01 Gutachten, Krankenhausunterlagen | Korbiel: nicht Schläger | Hoch |
| Mittäterschaft Drebenstedt | TKUe G-07, FZA, Video (72%) | Videoidentifizierung angreifbar | Mittel |
| Mittäterschaft Krasniqi | TKUe G-14, Video, Gegenüberstellung | Sternkopf-Gutachten, Zeitwiderspruch G-41 | Mittel |
| Geldwaesche (§ 261 StGB) | BTC-Wallets, TKUe G-58 | EncroChat-Verwertbarkeit | Mittel |

---

## 5. Nutzungsregeln und Datenschutz

Das interne Beweis-Index-System unterliegt strengen Vertraulichkeitsregeln:
- Zugriff nur für beauftragte Kanzlei-Mitarbeiter (Anwälte, Referendare mit Schweigepflicht)
- Keine Cloud-Speicherung; rein lokaler Kanzlei-Server
- Alle Dateien sollen nach Abschluss des Verfahrens gelöscht werden (§ 50 BRAO: Handaktenaufbewahrung 5 Jahre; danach Löschung)
- DSGVO-Konformitaet: Die Verarbeitung von Beschuldigten-/Zeugendaten ist durch § 45 BDSG (Strafverfolgungszweck) zulässig

**Quellen:** § 50 BRAO (dejure.org); § 45 BDSG (dejure.org); DSGVO Art. 10 (Verarbeitung strafrechtlicher Daten); BGH NStZ 2021, 118 (Datenschutz im Strafverfahren).
