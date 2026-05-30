# Aktenstück 11 — Werbeanzeigen-Repository nach Art. 39 DSA: Lückenanalyse

**Az. Kanzlei:** KRS-2026-0318-DSA
**Bearbeitung:** RA Felix Wendland
**Stand:** 07. April 2026

---

## 1. Normgrundlage

Art. 39 DSA verpflichtet VLOPs und sehr große Online-Suchmaschinen (VLOSE), eine durchsuchbare Datenbank (Repository) aller auf der Plattform angezeigten Werbeanzeigen bereitzustellen und diese für mindestens ein Jahr nach der letzten Anzeige zugänglich zu halten. Das Repository dient der Überwachbarkeit durch Behörden, Forscher und die Öffentlichkeit.

---

## 2. Pflichtinhalte des Repositories (Art. 39 Abs. 2 DSA)

Für jede Werbeanzeige sind folgende Daten zu dokumentieren:

| Pflichtfeld | Beschreibung |
|---|---|
| Anzeigeninhalt | Text, Bild, Video der Anzeige |
| Werbetreibender | Name und Kontaktdaten |
| Zeitraum der Ausspielung | Von/bis Datum |
| Targeting-Parameter | Demographische und sonstige Parameter, die zur Ausspielung geführt haben |
| Anzahl der Empfänger | Aufgeschlüsselt nach Mitgliedstaaten |
| Zahlender Auftraggeber | Sofern abweichend vom Werbetreibenden |

---

## 3. Lückenanalyse

Körnerstrom Social GmbH betreibt das Repository seit Oktober 2024. Eine interne Revision vom 25. März 2026 hat folgende Lücken identifiziert:

### 3.1 Zeitliche Lücken

| Zeitraum | Art der Lücke | Betroffene Anzeigen (geschätzt) |
|---|---|---|
| Januar 2025 | Vollständiger Datenausfall (Server-Migration) | ca. 18.000 |
| Februar 2025 | Lückenhafte Targeting-Parameter (70% der Einträge) | ca. 14.000 |
| März–Juli 2025 | Fehlende "Anzahl Empfänger per Mitgliedstaat" | ca. 85.000 |
| August–September 2025 | Fehlende Angaben zum zahlenden Auftraggeber bei 12% der Anzeigen | ca. 9.000 |

### 3.2 Inhaltliche Lücken

- **Targeting-Parameter-Vollständigkeit:** In 23% der Einträge (Stand: Audit März 2026) fehlen vollständige Targeting-Parameter; insbesondere verhaltensbasiertes Retargeting ist nicht immer dokumentiert.
- **Mehrsprachige Anzeigen:** Anzeigen, die in mehreren Sprachen ausgespielt wurden, sind nur in der Standardsprache gespeichert.
- **Video-Anzeigen:** Das Repository enthält nur Thumbnail-Screenshots, keine vollständigen Videodateien (Video-Format noch nicht implementiert).

---

## 4. Rückfüllungsplan

Zur Schließung der identifizierten Lücken wird folgender Rückfüllungsplan vorgeschlagen:

| Maßnahme | Priorität | Frist |
|---|---|---|
| Rekonstruktion Januar 2025 aus Backup-Logs | Hoch | 30.04.2026 |
| Nachpflege Targeting-Parameter Feb. 2025 | Hoch | 30.04.2026 |
| Nachpflege "Empfänger per Mitgliedstaat" (März–Juli 2025) | Mittel | 15.05.2026 |
| Nachpflege Auftraggeber-Angaben (Aug.–Sept. 2025) | Mittel | 15.05.2026 |
| Implementierung Video-Format im Repository | Niedrig | 15.06.2026 |
| Automatisierte Vollständigkeitsprüfung (Monitoring) | Mittel | 01.06.2026 |

**Verantwortlich:** Legal (Lena Maaßen), Adtech-Team, CTO Fatima Schröder.

---

## 5. Öffentliche Zugänglichkeit

Art. 39 Abs. 2 DSA verlangt, dass das Repository "leicht und direkt" zugänglich ist. Die Kommission hat in ihren Leitlinien vom März 2025 folgende Mindestanforderungen konkretisiert:

- Volltext-Suche nach Werbetreibenden, Zeiträumen und Targeting-Parametern
- Maschinenlesbare Schnittstelle (API) für Forscher und akkreditierte Institutionen
- Keine Registrierungspflicht für einfache Lesezugriffe
- Aktualität: tägliche Aktualisierung

**Status Halmweise.de:** Repository ist unter https://halmweise.de/ads-transparency öffentlich zugänglich. Suchfunktion vorhanden, aber API für Forscher fehlt noch (geplant für 01.07.2026).

---

## 6. Verhältnis zu DSGVO und Datenschutz

Die Repository-Pflicht des Art. 39 DSA steht in Spannung zum Datenschutzrecht. Targeting-Parameter können personenbezogene Daten sein. Lösung nach Erwägungsgrund 99 DSA: Targeting-Parameter sind so zu dokumentieren, dass keine Rückschlüsse auf individuelle Nutzer möglich sind (aggregierte oder pseudonymisierte Angaben).

---

## 7. Empfehlungen an Mandantin

1. Rückfüllungsplan unverzüglich umsetzen; Nachweis gegenüber BNetzA mit Sachstandsbericht bis 05.05.2026.
2. API-Implementierung für Forscher bis 01.07.2026 priorisieren.
3. Automatisiertes tägliches Monitoring für Repository-Vollständigkeit einrichten.
4. Datenschutzrechtliche Prüfung der Repository-Inhalte mit DPO abstimmen.

---

## 8. Rechtsgrundlagen

- Art. 39 DSA (EU) 2022/2065 — Werbeanzeigen-Repository
- Art. 26, 35 DSGVO (EU) 2016/679 — Datenschutz bei Werbedaten

**Quellen:**
- Verordnung (EU) 2022/2065 (DSA), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2065

---

*Bearbeitung: RA Felix Wendland*
*Stand: 07. April 2026*
