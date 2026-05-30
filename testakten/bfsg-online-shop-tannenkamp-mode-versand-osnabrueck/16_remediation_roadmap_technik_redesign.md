# Aktenstück 16 — Remediation-Roadmap: Technik und Redesign

**Bearbeitungsstand:** April 2026 (Koordination Dr. Friedrichs / IT-Leiter Wörmann / AccessCheck GmbH)

---

## 1. Überblick und Zielsetzung

Ziel ist die vollständige WCAG 2.1 AA-Konformität des Online-Shops tannenkamp-mode.de (inkl. PDF-Kataloge Herbst/Winter 2025) bis spätestens 30.09.2026. Die Roadmap ist in drei Phasen gegliedert:

- **Phase 1 (Sofortmaßnahmen):** Kritische Verstöße beheben — bis 30.06.2026
- **Phase 2 (Tiefensanierung):** Systemische Korrekturen — bis 31.08.2026
- **Phase 3 (Verifikation):** Audit und Zertifizierung — bis 30.09.2026

---

## 2. Phase 1 — Sofortmaßnahmen (bis 30.06.2026)

| ID | Maßnahme | WCAG SC | Aufwand | Status |
|---|---|---|---|---|
| P1-01 | Fokus-CSS wiederherstellen (`:focus-visible`) | 2.4.7 | 4 h | Implementiert 20.04.2026 |
| P1-02 | Skip-Link Hauptinhalt einfügen | 2.4.1 | 2 h | Implementiert 20.04.2026 |
| P1-03 | Schriftfarbe Fließtext auf #595959 | 1.4.3 | 2 h | Implementiert 25.04.2026 |
| P1-04 | Schriftfarbe Navigation auf #5a5a5a | 1.4.3 | 1 h | Implementiert 25.04.2026 |
| P1-05 | Erklärung zur Barrierefreiheit veröffentlichen | § 19 BFSG-DV | 2 h | Erledigt 06.04.2026 |
| P1-06 | Feedback-E-Mail einrichten | § 16 BFSG-DV | 1 h | Erledigt 06.04.2026 |
| P1-07 | PDF H/W 2024 und FS 2025 offline nehmen | § 38 BFSG | 1 h | Geplant 01.05.2026 |

---

## 3. Phase 2 — Tiefensanierung (bis 31.08.2026)

| ID | Maßnahme | WCAG SC | Aufwand | Dienstleister |
|---|---|---|---|---|
| P2-01 | `<div role="button">` auf `<button>` umstellen (ca. 1.800 Instanzen) | 4.1.2, 2.1.1 | 40 h | Lavendelhaus / intern |
| P2-02 | ARIA-Labels für Icon-Buttons (Warenkorb, Suche, Konto) | 4.1.2 | 4 h | intern |
| P2-03 | HTML5-Landmark-Elemente (`<main>`, `<nav>`, `<header>`) | 1.3.1 | 8 h | Lavendelhaus |
| P2-04 | `aria-live`-Regionen für dynamische Inhalte | 4.1.3 | 6 h | intern |
| P2-05 | Alt-Texte für 2.317 Produktbilder (Bulk + KI-gestützt) | 1.1.1 | extern ca. 3.000 EUR | Spezialagentur |
| P2-06 | Heading-Hierarchie korrigieren (H1 auf Kategorieseiten) | 1.3.1 | 8 h | intern |
| P2-07 | Formular-Labels und Fehlermeldungen ARIA-konform | 3.3.1, 3.3.2 | 12 h | intern |
| P2-08 | PDF H/W 2025 PDF/UA-konform überarbeiten | WCAG 2.1 | 10 h extern | PDF-Dienstleister |
| P2-09 | Mobile View Accessibility (Hamburger-Menü) | 2.1.1 | 6 h | Lavendelhaus |

---

## 4. Phase 3 — Audit und Zertifizierung (bis 30.09.2026)

| ID | Maßnahme | Dienstleister |
|---|---|---|
| P3-01 | Vollständiger Re-Audit WCAG 2.1 AA (automatisiert + manuell) | AccessCheck GmbH |
| P3-02 | Screenreader-Abnahmetest (NVDA, VoiceOver) | AccessCheck GmbH |
| P3-03 | Auditbericht als Grundlage für aktualisierte Erklärung zur Barrierefreiheit | intern |
| P3-04 | Vorlage Abschlussbericht an MüNI | Dr. Friedrichs |
| P3-05 | Vorlage Compliance-Nachweis an LG Hannover | Dr. Friedrichs |

---

## 5. Zeitplan (Gantt-Übersicht)

```
April 2026:  [P1-01 ✓][P1-02 ✓][P1-03 ✓][P1-04 ✓][P1-05 ✓][P1-06 ✓]
Mai 2026:    [P1-07][P2-05 Start]
Juni 2026:   [P2-01..P2-04, P2-06, P2-07][P2-08 Start]
Juli 2026:   [P2-09][P2-08 abschl.][P2-05 abschl.]
August 2026: [P3-01 Re-Audit][P3-02 Screenreader]
September:   [P3-03..P3-05 Abschluss]
```

---

## 6. Ressourcen und Verantwortlichkeit

| Phase | Interner Aufwand | Externer Aufwand | Kostenschätzung |
|---|---|---|---|
| Phase 1 | 13 h | — | intern 1.300 EUR |
| Phase 2 | 84 h | ca. 12.000 EUR | gesamt ca. 20.400 EUR |
| Phase 3 | 20 h | ca. 9.500 EUR | gesamt ca. 11.500 EUR |
| **Gesamt** | **117 h** | **ca. 21.500 EUR** | **ca. 33.200 EUR** |

---

*Die Roadmap ist Anlage zur Stellungnahme an MüNI (02.05.2026) und wird dem LG Hannover als Anlage zur Klageerwiderung vorgelegt.*
