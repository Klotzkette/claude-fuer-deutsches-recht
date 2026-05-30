# Aktenstück 05 — Standardkonflikt: BITV 2.0 vs. WCAG 2.1 AA vs. EN 301 549

**Bearbeitungsstand:** April 2026
**Bearb.:** Dr. A. Friedrichs

---

## 1. Problemaufriss

Im Verfahren MüNI-BFSG-2026/0188 und im Schriftsatz VZ NRW beziehen sich Behörde und Klägerin auf unterschiedliche technische Standards. Die Behörde verweist auf BITV 2.0, die VZ NRW auf WCAG 2.1 AA. Der BFSG-Text selbst nennt EN 301 549. Welcher Standard ist rechtsverbindlich?

---

## 2. Rechtliche Normenhierarchie

### 2.1 BFSG und BFSG-DV

Das BFSG verweist in § 3 Abs. 1 S. 2 BFSG auf die harmonisierten Normen und die BFSG-Durchführungsverordnung (BFSG-DV) als Konkretisierungsebene. Die BFSG-DV enthält in § 2 BFSG-DV i.V.m. Anlage 1 die technischen Anforderungen für E-Commerce-Dienste.

### 2.2 Harmonisierte Norm EN 301 549

Die Europäische Kommission hat EN 301 549 v3.2.1 (2021) als harmonisierte Norm veröffentlicht. Wer die EN 301 549 erfüllt, genießt die sog. Konformitätsvermutung nach § 6 BFSG: Es wird unwiderleglich vermutet, dass die BFSG-Anforderungen erfüllt sind. EN 301 549 inkorporiert WCAG 2.1 AA in Abschnitt 9 für Web-Content vollständig. Die EN 301 549 ist damit der rechtsverbindliche Prüfmaßstab.

### 2.3 WCAG 2.1 AA

WCAG 2.1 (Web Content Accessibility Guidelines, W3C 2018) ist eine technische Leitlinie des W3C. Über die Inkorporation in EN 301 549 erhält WCAG 2.1 AA quasi-Gesetzeskraft im BFSG-Regime. Die vier Grundprinzipien — Wahrnehmbarkeit (Perceivable), Bedienbarkeit (Operable), Verständlichkeit (Understandable), Robustheit (Robust) — sind der inhaltliche Maßstab.

### 2.4 BITV 2.0

Die Barrierefreie-Informationstechnik-Verordnung 2.0 (BITV 2.0) gilt nur für Einrichtungen des öffentlichen Sektors (§ 12 BGG). Für private Wirtschaftsakteure wie Tannenkamp Mode-Versand GmbH ist BITV 2.0 nicht unmittelbar anwendbar. Die MüNI-Referenz auf BITV 2.0 in der Anhörung ist rechtlich ungenau. Dies ist in der Stellungnahme zu korrigieren: Maßstab ist allein EN 301 549 i.V.m. BFSG-DV Anlage 1.

---

## 3. Konsequenz für die Verteidigung

Die Feststellung, dass BITV 2.0 nicht der korrekte Maßstab ist, nützt der Mandantin prozessual: Sie kann rügen, dass die Behörde einen falschen Prüfmaßstab angelegt hat. Dies hat Auswirkungen auf:

- Die Bestimmtheit des Bußgeldbescheids (Art. 103 Abs. 2 GG analog; § 17 OWiG)
- Den Umfang der Untersagungsverfügung
- Die Bindungswirkung des behördlichen Feststellungsbeschlusses im Verbandsklage-Verfahren

Inhaltlich sind die Verstöße jedoch nach allen drei Regelwerken identisch bemängelt. Die Kontrast-Anforderung (4,5:1 für Fließtext) findet sich in WCAG 2.1 SC 1.4.3, EN 301 549 Abschnitt 9.1.4.3 und BITV 2.0 Anforderung 1.4.3.

---

## 4. Konkrete Prüfmatrix

| WCAG 2.1 SC | EN 301 549 | Tannenkamp-Befund | Erfüllt? |
|---|---|---|---|
| 1.1.1 Non-text Content | 9.1.1.1 | Alt-Texte bei ~2.300 Produktbildern fehlen | Nein |
| 1.3.1 Info and Relationships | 9.1.3.1 | ARIA-Roles fehlerhaft | Nein |
| 1.4.3 Contrast (Minimum) | 9.1.4.3 | Kontrast 2,8:1 statt 4,5:1 | Nein |
| 2.1.1 Keyboard | 9.2.1.1 | Tastatur-Navigation ohne sichtbaren Fokus | Nein |
| 2.4.1 Bypass Blocks | 9.2.4.1 | Kein Skip-Link | Nein |
| 2.4.3 Focus Order | 9.2.4.3 | Tab-Reihenfolge inkonsistent | Nein |
| 4.1.2 Name, Role, Value | 9.4.1.2 | `<div role="button">` ohne Handler | Nein |

---

## 5. Bedeutung von WCAG 2.2 (Oktober 2023)

Seit Oktober 2023 ist WCAG 2.2 veröffentlicht. EN 301 549 ist noch auf WCAG 2.1 Basis; eine Aktualisierung ist angekündigt. Für das BFSG-Regime gilt derzeit noch WCAG 2.1 AA als maßgeblich. Empfehlung an Mandantin: Im Rahmen der Sanierung direkt auf WCAG 2.2 AA heben, um Zukunftssicherheit zu gewährleisten.

---

*Quelle: BFSG § 3, § 6 (dejure.org/gesetze/BFSG); EN 301 549 v3.2.1 (ETSI-Standard, online); RL EU 2019/882 Art. 15 Abs. 3 (EUR-Lex 32019L0882)*
