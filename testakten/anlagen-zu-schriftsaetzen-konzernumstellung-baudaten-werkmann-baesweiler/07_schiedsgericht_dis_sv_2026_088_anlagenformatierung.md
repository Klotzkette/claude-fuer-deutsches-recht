# 07 Schiedsgericht DIS-SV-2026/088 — Anlagenformatierung und Logistik

Datum: 15. März 2026
Bearbeiter: RA Dr. Bertram Söhnchen LL.M.
Az.: DIS-SV-2026/088

---

## Hintergrund

Das DIS-Schiedsverfahren (Deutsche Institution für Schiedsgerichtsbarkeit, Emil-von-Behring-Straße 35, 60439 Frankfurt am Main) wurde von K+B als Kläger initiiert. K+B behauptet Mangelfolgeschäden aus der Lackieranlage Eschweiler in Höhe von 1.200.000 EUR. Werkmann hat am 28.02.2026 fristgemäß Klageerwiderung eingereicht und gleichzeitig Widerklage auf 2.400.000 EUR (identisch mit LG-Klage) erhoben. Die Schiedsrichterin (Prof. Dr. Schwartze, Frankfurt) hat mit Verfahrensanordnung Nr. 3 vom 05.03.2026 detaillierte Formatierungsanforderungen für den Anlagen-Sammelband festgelegt.

---

## Anforderungen des Schiedsgerichts (Verfahrensanordnung Nr. 3)

Das Schiedsgericht verlangt für die Schriftsätze:

1. **4 Originale** jedes Schriftsatzes (für: Schiedsgericht-Vorsitz, Beisitzerin 1, Beisitzer 2, Gegenseite)
2. **1 USB-Stick je Originalexemplar** (4 USB-Sticks) mit allen Anlagen als durchsuchbare PDF/A-Dateien
3. Anlagen-Sammelband: gebunden, Register, fortlaufende Seitenzählung
4. Maximale Seitenbreite: DIN A4, keine Querformat-Auszüge ohne ausdrückliche Genehmigung
5. Fremdsprachige Anlagen: Übersetzung (beglaubigt) und Original nebeneinander
6. Jede Anlage: Deckblatt mit Anlage-Nummer, Bezeichnung, Seitenzahl, Datum, Sprache

Der geschätzte Umfang des Anlagen-Sammelbands für die Widerklage: **1.847 Seiten** (Kernkonvolut, ohne Nachlagenkonvolut).

---

## Logistische Herausforderungen

### Problem 1: Druckkosten und Bindung

4 Originale × 1.847 Seiten = 7.388 Seiten. Hinzu kommen Deckblätter, Register und Trenner: geschätzt 7.600 Druckseiten. Bei einem Druckpreis von ca. 0,12 EUR/Seite (Kanzlei-Dienstleister Kopierzentrale Aachen) und 15 EUR pro Bindung:

| Position | Berechnung | Kosten (EUR) |
|---|---|---|
| Druck 7.600 Seiten | 7.600 × 0,12 | 912 |
| Bindung 4 Exemplare | 4 × 15 | 60 |
| USB-Sticks (8 GB) | 4 × 8 | 32 |
| Kopierkosten interne QK | pauschal | 150 |
| **Gesamt** | | **1.154** |

Diese Kosten sind nach § 91 ZPO i.V.m. § 23 RVG erstattungsfähig (dazu Aktenstück 21).

### Problem 2: Querformat und Plandokumente

Von den 842 CAD-Plänen, die für das Schiedsverfahren relevant sind, liegen 617 im Format DIN A1 oder DIN A0 vor. Das Schiedsgericht erlaubt kein Querformat ohne Genehmigung. Dr. Söhnchen beantragt mit dem Widerklage-Schriftsatz die Genehmigung, CAD-Pläne auf DIN A3 gefaltet (nicht gerollt) einzureichen — je 4 Exemplare, ohne Bindung dieser Seiten, aber mit fortlaufender Seitennummerierung.

### Problem 3: USB-Stick-Integrität

Das Schiedsgericht verlangt, dass die USB-Sticks nach Einreichung durch das Schiedsgericht versiegelt und archiviert werden. Die Kanzlei muss eine SHA-256-Prüfsummen-Liste für alle Dateien auf den USB-Sticks einreichen (separate Anlage zum Schriftsatz). Dies erfordert ein automatisiertes Prüfsummen-Skript für 1.847 Dateien.

---

## Anlagekonzept für das Schiedsverfahren

### Anlage-Nummerierung

Schiedsgericht verwendet Präfix S-W (Werkmann) und S-KB (K+B). Die Werkmann-Widerklage-Anlagen werden als S-W-001 bis S-W-247 nummeriert — bewusst in Anlehnung an die K1–K247-Struktur des LG-Verfahrens, um interne Verwechslungen zu minimieren. Abweichungen sind in der Anlagenmatrix (Aktenstück 12) dokumentiert.

### Inhalt des Anlagen-Sammelbands (Grobstruktur)

| Band | Inhalt | Seitenumfang |
|---|---|---|
| S-W-001 bis S-W-015 | Vertragsunterlagen | ca. 180 Seiten |
| S-W-016 bis S-W-080 | Baunachweise | ca. 620 Seiten |
| S-W-081 bis S-W-140 | Liefernachweise | ca. 410 Seiten |
| S-W-141 bis S-W-180 | CE/Konformität | ca. 220 Seiten |
| S-W-181 bis S-W-247 | Mehrkosten | ca. 417 Seiten |
| **Gesamt** | | **1.847 Seiten** |

---

## Zeitplanung

| Datum | Aufgabe |
|---|---|
| 20.03.2026 | Anlagen-Sammelband vollständig zusammengestellt (digital) |
| 25.03.2026 | Qualitätskontrolle (4-Augen-Prinzip: Söhnchen + Stang) |
| 28.03.2026 | Druckauftrag Kopierzentrale |
| 30.03.2026 | USB-Sticks bespielt und versiegelt |
| 31.03.2026 | Einreichung beim DIS Frankfurt (Einschreiben mit Rückschein) |

Der Schiedsgerichtsschriftsatz (inkl. Anlagenverzeichnis) ist als DOCX in der Akte abgelegt: `schiedsgerichtsschriftsatz_dis_anlagenkonvolut.docx`.

---

## Hinweis: DIS-Schiedsregeln

Einschlägige Regelungen: DIS-Schiedsgerichtsordnung 2018 (DIS-SchO), §§ 14 ff. (Schriftsätze und Anlagen). Zu Anlagenformat und -einreichung: § 14 Abs. 3 DIS-SchO. Abrufbar auf der Website der DIS: https://www.dis-arb.de/
