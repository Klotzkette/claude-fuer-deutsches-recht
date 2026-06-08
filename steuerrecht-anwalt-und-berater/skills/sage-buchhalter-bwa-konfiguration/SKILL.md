---
name: sage-buchhalter-bwa-konfiguration
description: "Sage Buchhalter BWA-Konfiguration. Anwendungsfall Mandanten oder Kanzleien mit Sage-Software statt DATEV/Addison. Methodik Unterschiede Konten BWA-Forms. Output BWA in Sage."
---

# Sage Buchhalter BWA

## Fachlicher Anker

- **Normen:** § 6a, § 14 UStG, § 146 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Sage ist eine internationale ERP- und Buchhaltungsplattform, in Deutschland mit Sage 100, Sage 50 für KMU. Insbesondere bei mittelstaendischen Mandanten haeufig im Einsatz. BWA-Module sind aequivalent zu DATEV/Addison, aber mit anderer Bedienlogik. Steuerberater, die mit Sage-Mandanten arbeiten, brauchen Schnittstellen oder Datenuebernahme.

## Kaltstart-Rueckfragen

1. Welche Sage-Version (Sage 100, Sage 50, Sage Office Line)?
2. Wer betreibt Sage — Mandant selbst oder StB?
3. Welche BWA-Form ist konfiguriert?
4. Welcher Kontenrahmen (SKR 03, SKR 04, individuell)?
5. Welche Schnittstellen zu DATEV (falls vorhanden)?
6. Welche Module aktiv?
7. Welche Mandantenbeguenstigung?
8. Welcher Updates-Stand?

## Workflow

### Phase 1 — System-Setup

- Variante A: Mandant betreibt Sage selbst (Sage 50 Cloud, Sage 100, Sage Office Line); StB erhaelt Lese-Zugriff oder Monats-Export.
- Variante B: StB betreibt Sage als Service-Provider (selten; in der Regel DATEV-Bevorzugung in Kanzleien).
- Konten-Konfiguration: Sage unterstuetzt SKR 03/04 sowie eigene Kontenrahmen; Branchenkontenrahmen ueber Sage-Vorlagen.

### Phase 2 — BWA-Konfiguration

- Sage-Standard-BWA gliedert ueblicherweise nach Erloesen, variable Kosten, Deckungsbeitrag, Fixkosten, Betriebsergebnis (vergleichbar mit DATEV BWA 01).
- Vorjahresvergleich automatisch bei vorhandener Historie; Planwerte ueber das Sage-Planungsmodul.
- Anpassung der BWA-Zeilen ueber `Auswertungen → BWA → Konfiguration` (konkreter Programmpfad variiert je Sage-Version — im Zweifelsfall in der Sage-Onlinehilfe unter "BWA-Konfiguration" nachschlagen).

### Phase 3 — Schnittstellen

- Sage-eRechnung-Modul für XRechnung/ZUGFeRD-Empfang und -Versand (§ 14 UStG; siehe Skill `stb-erechnung-pflicht-b2b-2025-2026`).
- Bank-Anbindung ueber PSD2-Schnittstelle (HBCI/FinTS) oder Sage Banking.
- Export im DATEV-CSV-Format (DATEV ASCII-Format) ueber `Stammdaten → Datenexport → DATEV` (Programmpfad version-abhaengig).

### Phase 4 — Datenaustausch mit StB

- Standardisierter Monats-Export aus Sage; Termin- und Format-Vereinbarung schriftlich.
- StB-Seite: Import in DATEV Kanzlei-Rechnungswesen ueber `Datei → Datenuebernahme → Buchungsstapel`.
- Mapping-Tabelle Sage-Konten zu SKR 03/04 vorab abstimmen — Differenzen sonst pro Monat zu klaeren.

### Phase 5 — Lohn

- Sage HR / Sage Lohn als separate Module bzw. externes Lohnprogramm (DATEV LODAS, eGecko, etc.).
- Buchungssatz-Schnittstelle zum Hauptbuch (typischerweise monatlicher Buchungsbeleg).
- Bei Mandantenwechsel zu DATEV: Lohn meist parallel migriert (siehe `stb-lohn-mandantenaufnahme-onboarding`).

### Phase 6 — Updates

- Jaehrliche Programm-Updates zum 1. Januar (LSt/SV-Tabellen, USt-Aenderungen, AfA-Tabellen).
- Sage Cloud-Versionen: automatische Updates ueber den Cloud-Anbieter.
- Update-Pflicht aus § 146 AO (Programm muss aktuelle Tabellen abbilden).

## Output

- Konfigurierte Sage-BWA.

## Strategie und Praxis-Tipps

- Bei Sage-Mandanten Datenaustausch standardisieren — CSV-Export ist Standard.
- Datenuebernahme Sage zu DATEV ist Aufwand — Mandantenwechsel sorgfaeltig planen.
- Sage-Schulung ueber Sage-Akademie.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV.
- `stb-addison-bwa-konfiguration-tipps` — Addison.

## Quellen und Updates

Stand: 05/2026.

- Sage Programm- und Bedienungsdokumentation (aktuelle Version pruefen).
- AO § 146 (Update-Pflicht der Buchfuehrungsprogramme).
- Hinweis: konkrete Programmpfade und Modulbezeichnungen koennen je Sage-Version abweichen; aktuelle Informationen in der Sage-Onlinehilfe pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (Sage-Programmpfad nicht versionsspezifisch belegbar, Verweis auf Sage-Onlinehilfe) -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
