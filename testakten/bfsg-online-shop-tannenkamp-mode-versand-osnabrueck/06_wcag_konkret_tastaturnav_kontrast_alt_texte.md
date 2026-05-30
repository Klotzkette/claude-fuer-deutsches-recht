# Aktenstück 06 — WCAG-Befunde konkret: Tastatur-Navigation, Kontrast, Alt-Texte

**Bearbeitungsstand:** April 2026 (auf Basis WCAG-Audit-Bericht vom 25.03.2026)
**Bearb.:** Dr. A. Friedrichs / IT-Leiter Benedikt Wörmann (techn. Teil)

---

## 1. Grundlage: Externer WCAG-Audit

Mandantin beauftragte am 20.03.2026 die Agentur AccessCheck GmbH, Bielefeld, mit einem kombinierten automatisierten und manuellen Audit nach WCAG 2.1 AA / EN 301 549. Auditbericht vom 25.03.2026 (vgl. Anlage: wcag_audit_bericht_executive_summary_redacted.pdf).

---

## 2. Befund 1 — Tastatur-Navigation (WCAG SC 2.1.1, 2.4.3, 2.4.7)

### 2.1 Beschreibung

Beim Navigieren mit der Tab-Taste ist kein sichtbarer Fokusrahmen erkennbar. CSS-Regel `.focus-visible { outline: none; }` unterdrückt systemweit den Browser-Standardfokus. Für Tastaturnutzende (z.B. Motorik-Einschränkungen) sowie Screenreader-Nutzer ist der Shop faktisch nicht bedienbar.

### 2.2 Betroffene Elemente

- Navigationsmenü (Hauptnavigation, Megamenü)
- Produktlisten-Filter (Größe, Farbe, Preis)
- Warenkorb-Schaltfläche
- Checkout-Formular (Lieferadresse, Zahlungsart)
- Suchfeld

### 2.3 Normverstoß

WCAG 2.1 SC 2.1.1 (Keyboard): Alle Funktionen müssen per Tastatur bedienbar sein. SC 2.4.7 (Focus Visible): Tastaturfokus muss sichtbar sein. Verstoß ist schwerwiegend (Kategorie A und AA).

### 2.4 Sanierung

Fokus-CSS wiederherstellen: `*:focus-visible { outline: 3px solid #005fcc; outline-offset: 2px; }`. Geschätzter Aufwand: 4 Stunden Frontend-Arbeit nach Freigabe des Theme-Quellcodes durch Lavendelhaus Design.

---

## 3. Befund 2 — Alt-Texte (WCAG SC 1.1.1)

### 3.1 Beschreibung

Systematische Analyse ergibt: 2.317 Produktbilder im Shopify-Katalog haben kein `alt`-Attribut oder haben `alt=""` (leerer Alt-Text). Screenreader lesen bei leerem Alt-Text „image" oder die Dateinamen (z.B. „IMG_47832_bluse_hellgruen.jpg").

### 3.2 Normverstoß

WCAG 2.1 SC 1.1.1 (Non-text Content): Nicht-Text-Inhalte müssen mit einer Textalternative versehen sein. Bei Produktbildern ist eine beschreibende Alternative erforderlich (z.B. „Bluse aus Bio-Baumwolle, Hellgrün, Langarm, Damengröße 38").

### 3.3 Sanierung

Shopify ermöglicht Bulk-Upload von Alt-Texten über die Admin-API. Entweder manuelle Pflege aller 2.317 Einträge (ca. 80 Stunden) oder KI-gestützte Beschreibungsgenerierung (extern, Kosten ca. 2.500–4.000 EUR). Für neue Produktbilder: Prozess zur Pflichteingabe im PIM-System einzuführen.

---

## 4. Befund 3 — Kontrast (WCAG SC 1.4.3)

### 4.1 Beschreibung

Farbmessung mit dem Tool axe DevTools (v4.8):

| Element | Vordergrund | Hintergrund | Verhältnis | Erforderlich |
|---|---|---|---|---|
| Fließtext Produktbeschreibung | #7a7a7a | #f8f8f8 | 2,8:1 | 4,5:1 |
| Navigationslinks (nicht aktiv) | #aaaaaa | #ffffff | 2,3:1 | 4,5:1 |
| Preis-Angaben | #c0392b | #f8f8f8 | 3,1:1 | 4,5:1 |
| Kategorie-Header | #888888 | #eeeeee | 2,5:1 | 3:1 (groß) |

### 4.2 Normverstoß

WCAG 2.1 SC 1.4.3 (Contrast Minimum): Normaler Text muss 4,5:1, großer Text (ab 18pt/14pt fett) 3:1 erfüllen.

### 4.3 Sanierung

Schriftfarben im Theme auf #595959 (statt #7a7a7a) ändern — Kontrast steigt auf 7,0:1 gegenüber #f8f8f8. Für Preiselemente: #a93226 ergibt 4,6:1. CSS-Änderungen betreffen ca. 12 Variablen im Theme. Aufwand: 2 Stunden.

---

## 5. Befund 4 — Skip-Link (WCAG SC 2.4.1)

Skip-Link zum Hauptinhalt fehlt vollständig. Screenreader-Nutzer müssen bei jedem Seitenaufruf alle Navigationselemente (ca. 47 Tab-Stopps) durchqueren, bevor sie den Produktbereich erreichen.

Sanierung: `<a href="#main-content" class="skip-link">Zum Hauptinhalt springen</a>` als erstes Element im `<body>`; CSS: sichtbar bei Fokus.

---

## 6. Technische Zusammenfassung

Alle vier oben genannten Befunde sind klassische, weit verbreitete Fehler bei Shopify-Themes. Das „Lavanda Pro"-Theme der Lavendelhaus Design GbR ist in diesen Punkten nicht WCAG 2.1 AA-konform ausgeliefert worden. Dies stützt den Regressanspruch (vgl. Aktenstück 13).

---

*Quelle: WCAG 2.1 (W3C, https://www.w3.org/TR/WCAG21/); EN 301 549 v3.2.1 Abschnitt 9; Audit-Bericht AccessCheck GmbH v. 25.03.2026*
