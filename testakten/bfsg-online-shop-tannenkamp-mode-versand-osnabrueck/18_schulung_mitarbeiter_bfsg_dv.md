# Aktenstück 18 — Schulungspflicht Mitarbeiter und BFSG-DV

**Bearbeitungsstand:** Mai 2026
**Bearb.:** Dr. A. Friedrichs

---

## 1. Gesetzliche Grundlage

§ 18 BFSG-DV sieht vor, dass Dienstleistungserbringer sicherstellen, dass die mit der Erbringung der Dienstleistung beschäftigten Mitarbeiter über ausreichende Kenntnisse der Barrierefreiheitsanforderungen verfügen. Dies umfasst:

- Mitarbeiter, die den Online-Shop pflegen und Inhalte einstellen (Content-Management)
- IT-Mitarbeiter, die Anpassungen am Shop vornehmen
- Einkäufer und Produktmanager, die Produktinformationen und Bilder beschaffen

---

## 2. Schulungsbedarf bei Tannenkamp

Bei Befragung der Mitarbeiter (Abteilung E-Commerce, 12 Personen) am 25.03.2026 stellte sich heraus:

- Kein Mitarbeiter kannte das BFSG oder seine Anforderungen
- Alt-Texte für Produktbilder waren in der Shopify-Upload-Routine nicht als Pflichtfeld konfiguriert
- Das interne Style-Guide-Dokument für Produktbilder enthielt keine Anforderungen zu Alt-Texten
- IT-Leiter Wörmann kannte WCAG dem Namen nach, nicht in technischen Details

---

## 3. Schulungskonzept

### 3.1 Zielgruppen und Inhalte

| Zielgruppe | Umfang | Inhalte |
|---|---|---|
| Geschäftsführung (Tannenkamp, Hüsing) | 2 h | BFSG-Überblick, Haftungsrisiken, Compliance-Pflichten, Sanktionen |
| IT-Leiter Wörmann + IT-Team (4 Pers.) | 8 h | WCAG 2.1 AA technisch, ARIA, Tastatur-Navigation, axe-Tool, CI/CD-Integration |
| Content-Team (6 Pers.) | 4 h | Alt-Texte schreiben, Kontrast-Check, barrierefreie PDF-Erstellung, Shopify-Upload |
| Einkauf/Produktmanagement (8 Pers.) | 2 h | Bild-Beschaffungsstandards, Lieferantenanforderungen, Alt-Text-Pflicht |

### 3.2 Schulungsformat

- Interne Schulung durch AccessCheck GmbH (Präsenz in Osnabrück): IT-Team und Content-Team
- E-Learning-Modul (intern entwickelt): Geschäftsführung und Einkauf
- Jährliche Auffrischung: 1-stündiges Update zu WCAG-Neuerungen

---

## 4. Alt-Texte als Prozessthema

Der häufigste und volumenreichste Verstoß — 2.317 Produktbilder ohne Alt-Text — ist kein technisches Theme-Problem, sondern ein Prozessversagen: Mitarbeiter haben jahrelang Bilder ohne Alt-Text hochgeladen, weil dieses Feld als optional galt.

**Sofortmaßnahme:** Shopify-Admin-Konfiguration: Alt-Text-Feld als Pflichtfeld im Upload-Workflow (durch Shopify-Validator-Script). Ausgabe einer Warnung bei leerem Alt-Text.

**Mittelfristig:** Styleguide für Produktbildbeschreibungen erstellen. Muster-Beschreibungen (z.B. „[Produktname], [Farbe], [Material], [Detailansicht/Hauptansicht]"). Schulung aller Content-Mitarbeiter.

---

## 5. Dokumentation der Schulungen

§ 18 BFSG-DV verlangt keine explizite Dokumentationspflicht, aber das allgemeine Compliance-Gebot erfordert Nachweisfähigkeit. Empfehlung: Schulungsnachweise (Teilnahmeliste, Zertifikate) in der Personalakte ablegen. Bei MüNI-Kontrolle als Nachweis vorlegen.

---

## 6. Schulungskosten

| Posten | Kosten |
|---|---|
| AccessCheck GmbH — Schulung IT + Content (1 Tag) | 2.400 EUR |
| E-Learning-Modul-Entwicklung (extern) | 1.800 EUR |
| Interne Koordination (Wörmann) | 8 h × 65 EUR/h = 520 EUR |
| **Gesamt** | **4.720 EUR** |

---

*Quelle: BFSG-DV § 18 (dejure.org/gesetze/BFSG-DV); WCAG 2.1 (W3C 2018)*
