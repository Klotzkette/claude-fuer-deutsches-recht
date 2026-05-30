# 04 — Versionierung: Übersicht v18 bis v23

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Datum:** 10. Januar 2026

---

## Versionshistorie

| Version | Datum | Bearbeiter | Hauptänderung | Status beim WP |
|---|---|---|---|---|
| v18 | 14.08.2025 | Pellbach-Roosendaal | Erstmodell nach Krisendiagnose; Basisparameter | Zur Prüfung eingereicht |
| v19 | 02.09.2025 | Pellbach-Roosendaal | Personalplan aktualisiert (Abfindungen Q4 2025 eingefügt) | Zurückgewiesen: Bilanzsumme nicht ausgeglichen |
| v20 | 19.09.2025 | Pellbach-Roosendaal + ext. Berater | Bilanzsummenformel korrigiert; Kapex-Plan überarbeitet | Vorläufig akzeptiert, WP-Vorbehalt Zinslast |
| v21 | 07.10.2025 | Pellbach-Roosendaal | Sanierungsmaßnahmen konkretisiert; Umsatzplan 2027 angehoben | Unter Review Birkholz |
| v22 | 28.11.2025 | Pellbach-Roosendaal | Zinssatz Kontokorrent 6,2 % (marktkonform); Stress-Notiz eingefügt (ohne Berechnung) | Letzte akzeptierte Basis WP |
| v23 | 05.01.2026 | Pellbach-Roosendaal | Zinssatz auf 4,9 % reduziert (Finding 4); Zusammenfassung optisch überarbeitet | Versagung angedroht |

---

## Kritischer Befund: Versionsvergleich v22 → v23

**Finding 4** basiert auf folgendem Versionsvergleich:

| Zelle | Blatt | Wert v22 | Wert v23 | Delta |
|---|---|---|---|---|
| ZS!B5 | ZINS-SCHULDEN | 6,20 % | 4,90 % | –1,30 Pp |
| ZS!C5 | ZINS-SCHULDEN | Formel: =PARAM!B12 | Hardcoded: 0,049 | Formel entfernt |
| PARAM!B12 | PARAM | 6,20 % | 6,20 % | unverändert |

Die Zinssatzänderung wurde nicht durch eine geänderte Parameterannahme in PARAM vorgenommen, sondern durch direktes Überschreiben der Formel mit einem Hardcoded-Wert in ZS!C5. Dies entkoppelt den Zinssatz von der zentralen Parametersteuerung und ist nicht im offiziellen Änderungsprotokoll dokumentiert.

**Auswirkung:** Zinsaufwand 2026–2027 im Modell v23 um ca. 186 TEUR zu niedrig ausgewiesen. Bei Korrektur auf 6,2 % ergibt sich kumulativ ein um 186 TEUR schlechteres Liquiditätsergebnis.

---

## Manipulationsverdacht

Der Reviewer hält fest:

1. Die Zinssatzabsenkung in v23 bewirkt, dass das Modell ein knappes positives Fortbestehensergebnis zeigt (+418 TEUR).
2. Bei Korrektur auf v22-Zinssatz (6,2 %) reduziert sich der Überschuss auf ca. +232 TEUR.
3. In Kombination mit den Korrekturen aus Finding 1 (Zirkularität) und Finding 5 (Doppelbuchung Rückstellung, –145 TEUR) würde das Modell in den negativen Bereich kippen (ca. –89 TEUR kumuliert 2026–2027).
4. Die Kombination aus entkoppelter Formel und nicht dokumentierter Änderung begründet einen hinreichenden Anfangsverdacht auf bewusste Ergebnismanipulation im Modell.

**Rechtliche Einordnung:** § 283b StGB (Verletzung der Buchführungspflicht), ggf. § 283 StGB (Bankrott), abrufbar unter [https://dejure.org/gesetze/StGB/283b.html](https://dejure.org/gesetze/StGB/283b.html) und [https://dejure.org/gesetze/StGB/283.html](https://dejure.org/gesetze/StGB/283.html).

---

## Empfehlung

Der Reviewer empfiehlt:
- Alle Versionen v18–v23 zu sichern und die Revisionskette lückenlos zu dokumentieren.
- Ein externes strafrechtliches Gutachten zur Bewertung des Manipulationsverdachts einzuholen.
- Das Modell v23 in dieser Form nicht als Grundlage für den Jahresabschluss 2025 oder den Sanierungskreditantrag zu verwenden.

**Quellen:** HGB § 252 (Going-Concern): [https://dejure.org/gesetze/HGB/252.html](https://dejure.org/gesetze/HGB/252.html); StGB §§ 283, 283b: [https://dejure.org/gesetze/StGB/283.html](https://dejure.org/gesetze/StGB/283.html).
