# 12 Anlagenmatrix und Indexerstellung — Methodik

Datum: 18. Januar 2026 (fortlaufend aktualisiert)
Bearbeiter: Lea Stang; Qualitätskontrolle RA Dr. Söhnchen
Az.: 11 O 188/26, 14 U 22/26, DIS-SV-2026/088

---

## Zweck der Anlagenmatrix

Bei drei parallelen Verfahren mit zusammen 247 + 40 + 247 = 534 Gerichtsanlagen (Überschneidungen eingerechnet) und einem Nachlagenkonvolut von 3.600 Dokumenten ist ein strukturiertes Verzeichnis unabdingbar. Die Anlagenmatrix erfüllt mehrere Funktionen:

1. **Eindeutige Identifikation**: Jedes Dokument erhält eine kanzleiinterne Dokument-ID (Format: WBT-DOK-YYYYNNN, z.B. WBT-DOK-2024001), die unabhängig von der verfahrensspezifischen Anlagebezeichnung ist.

2. **Verfahrensübergreifende Zuordnung**: Die Matrix zeigt für jedes Dokument, unter welcher Anlagebezeichnung es in welchem Verfahren einzureichen ist (oder bereits eingereicht wurde).

3. **Versionsmanagement**: Jede Datei ist mit ihrer SHA-256-Prüfsumme und der Versionsnummer hinterlegt.

4. **Anspruchszuordnung**: Jedes Dokument ist mindestens einer Anspruchsposition (§ 631 BGB, § 2 Abs. 3 VOB/B oder § 8 Abs. 2 VOB/B) zugeordnet.

---

## Spaltenstruktur der Matrix (XLSX-Datei)

Die Anlagenmatrix ist als XLSX hinterlegt: `anlagenmatrix_lg_aachen_3847_einzelanlagen.xlsx`. Die Datei enthält folgende Spalten:

| Spalte | Inhalt | Beispiel |
|---|---|---|
| A | Kanzlei-Dok-ID | WBT-DOK-2024001 |
| B | Kurzbezeichnung | Abnahmeprotokoll 04.11.2024 |
| C | Datum | 04.11.2024 |
| D | LG-Anlage (K/B) | K3 |
| E | OLG-Anlage (BB/BK) | BB 12 |
| F | DIS-Anlage (S-W/S-KB) | S-W-003 |
| G | Anspruchsposition | § 631 BGB |
| H | Einreichungsstatus LG | eingereicht 21.01.2026 |
| I | SHA-256-Hash | a3f5b8... |
| J | Seitenzahl | 14 |

---

## Indexerstellungs-Methodik

### Schritt 1: Dokumentenerfassung (abgeschlossen 17.01.2026)

Hofferberth übergab einen USB-Stick mit 3.847 Einzeldateien in unstrukturierten Ordnern (nach Projekt-Phasen gegliedert: `Planung_2023`, `Ausführung_2024-Q1` bis `Ausführung_2024-Q4`, `Abnahme_2024-Q4`). Stang hat alle Dateien in das kanzleiinterne DMS übertragen und jeden Datei einen Anfangs-Rohindex zugewiesen.

### Schritt 2: Kategorisierung (abgeschlossen 20.01.2026)

Jedes Dokument wurde nach Typ kategorisiert (CAD-Plan, Bautagebuch, Aufmaß, Lieferschein etc.) und in die XLSX-Matrix aufgenommen. Für Kategorisierung und Verknüpfung mit Anspruchspositionen wurde eine interne Kategorisierungsanweisung erstellt (2 Seiten A4, liegt im Kanzlei-Intranet).

### Schritt 3: Priorisierung (abgeschlossen 21.01.2026)

Aus den 3.847 Dokumenten wurden 247 als Gerichtsanlagen K1–K247 ausgewählt (Kriterien: unmittelbare Relevanz für Anspruchspositionen, Schlüsseldokumente, nicht substituierbar durch Zusammenfassung). Die verbleibenden 3.600 wurden als NL-Dokumente eingestuft.

### Schritt 4: Hash-Berechnung (abgeschlossen nach PDF/A-Konvertierung, 23.01.2026)

Für alle 247 K-Anlagen wurden SHA-256-Prüfsummen berechnet (nach vollständiger PDF/A-2b-Konvertierung, vgl. Aktenstück 05). Die Prüfsummen sind in Spalte I der Matrix hinterlegt.

### Schritt 5: Fortlaufende Pflege

Die Matrix wird bei jeder Einreichung, jedem Nachtrag und jeder Korrektur aktualisiert. Stand: 31.03.2026 — Revisionsnummer 7 (automatisch protokolliert im DMS).

---

## QR-Code-Index (Querverweissystem)

Parallel zur XLSX-Matrix wurde ein QR-Code-Index entwickelt (Aktenstück 18). Jede Anlage im gedruckten Sammelband für das Schiedsgericht trägt auf dem Deckblatt einen QR-Code, der zur zentralen digitalen Version führt. Dies erleichtert dem Schiedsgericht die Navigation im 1.847-seitigen Sammelband.

---

## Qualitätssicherung

Die Anlagenmatrix unterliegt einem 4-Augen-Prinzip: Jede Zeile (= ein Dokument) wird von Stang eingetragen und von Dr. Söhnchen oder Hofferberth geprüft. Bei mehr als 10 Änderungen täglich wird eine Revisionssitzung einberufen (Protokollpflicht).

Aktueller Fortschritt (Stand 31.03.2026):

| Kategorie | Gesamt | Kanzlei-ID vergeben | K-Anlage zugewiesen | LG eingereicht |
|---|---|---|---|---|
| CAD-Pläne | 842 | 842 | 12 | 12 |
| Aufmaßprotokolle | 387 | 387 | 30 | 30 |
| Lieferscheine | 923 | 923 | 30 | 30 |
| Wiegescheine | 312 | 312 | 15 | 15 |
| Schweißnaht-Protokolle | 441 | 441 | 10 | 10 |
| FAT/SAT-Reports | 47 | 47 | 10 | 10 |
| Zollpapiere | 198 | 198 | 15 | 15 |
| Konformitätserklärungen | 83 | 83 | 25 | 25 |
| Sicherheitsdatenblätter | 247 | 247 | 15 | 15 |
| Sonstiges | 367 | 367 | 85 | 85 |
| **Gesamt** | **3.847** | **3.847** | **247** | **247** |
