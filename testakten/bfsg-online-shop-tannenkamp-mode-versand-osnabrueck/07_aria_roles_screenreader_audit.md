# Aktenstück 07 — ARIA-Roles und Screenreader-Audit

**Bearbeitungsstand:** April 2026
**Bearb.:** Dr. A. Friedrichs / AccessCheck GmbH (Audit)

---

## 1. Gegenstand

Dieser Bericht dokumentiert die ARIA-Rollen-Fehler (Accessible Rich Internet Applications) im Shop tannenkamp-mode.de auf Basis des manuellen Screenreader-Tests vom 24.03.2026. Testsystem: NVDA 2024.1 + Firefox 124 unter Windows 11; VoiceOver + Safari unter macOS Sonoma.

---

## 2. ARIA-Grundlagen

ARIA ist eine W3C-Spezifikation (WAI-ARIA 1.2), die HTML-Elementen semantische Rollen zuweist, damit Screenreader interaktive Elemente korrekt ansagen. Fehlerhafte ARIA-Verwendung ist oft schlimmer als gar keine ARIA (sog. „ARIA misuse"-Problem). WCAG 2.1 SC 4.1.2 (Name, Role, Value) ist der normative Anker.

---

## 3. Befunde

### 3.1 `<div role="button">` ohne Tastaturhandler

Im Produktlisting werden Schaltflächen als `<div>`-Elemente mit `role="button"` kodiert. Problem: `<div>` ist von Haus aus nicht fokussierbar und erhält keine Tastaturereignisse (`keydown`, `keypress`). Tastaturnutzende können diese Schaltflächen nicht aktivieren.

**Betroffene Stellen:**
- „In den Warenkorb"-Button auf Produktkacheln (betrifft alle ~1.800 Produktseiten)
- „Auf die Merkliste"-Button
- Farbauswahl-Swatches

**Normverstoß:** WCAG 2.1 SC 4.1.2, 2.1.1, 2.4.7.

**Sanierung:** Ersetzen durch `<button>`-Elemente oder `tabindex="0"` + ARIA-Handler hinzufügen.

### 3.2 Fehlende `aria-label` auf Icon-Buttons

Mehrere Schaltflächen bestehen ausschließlich aus SVG-Icons (Warenkorb, Lupe, Nutzerkonto) ohne begleitenden Textinhalt und ohne `aria-label`. Screenreader geben diese als „Schaltfläche" ohne Beschreibung aus.

**Sanierung:** Hinzufügen von `aria-label="Warenkorb anzeigen"` etc.

### 3.3 Landmarks fehlen

Die Seite verwendet keine ARIA-Landmark-Roles (`<header role="banner">`, `<nav role="navigation">`, `<main role="main">`, `<footer role="contentinfo">`). Screenreader-Nutzer können nicht zwischen Seitenbereichen springen.

**Sanierung:** HTML5-semantische Elemente (`<main>`, `<nav>`, `<header>`, `<footer>`) korrekt einsetzen; darüber hinaus ergänzende ARIA-Landmarks.

### 3.4 Dynamische Inhalte ohne `aria-live`

Der Warenkorb-Counter und Fehlermeldungen im Checkout-Formular werden dynamisch aktualisiert, ohne eine `aria-live`-Region zu deklarieren. Screenreader erhalten keine Benachrichtigung über Änderungen.

**Sanierung:** `<div aria-live="polite" aria-atomic="true">` um dynamische Bereiche.

### 3.5 Falsche Heading-Hierarchie

Heading-Analyse ergibt: H1 fehlt auf Kategorie-Unterseiten; direkt H2-Elemente für Produkttitel verwendet. Screenreader-Nutzer, die per Überschriften navigieren (verbreitet), verlieren Orientierung.

**Sanierung:** Seitenstruktur mit korrekter H1 → H2 → H3-Hierarchie aufbauen.

---

## 4. Screenreader-Test-Ergebnis

Gesamtbewertung aus manuellem Test:

| Screenreader | Browser | Ergebnis |
|---|---|---|
| NVDA 2024.1 | Firefox 124 | Shop weitgehend nicht bedienbar; Checkout nicht abschließbar |
| VoiceOver | Safari | Checkout mit erheblichem Mehraufwand; Produktlisting kaum navigierbar |

---

## 5. Rechtliche Einordnung

Die ARIA-Fehler konstituieren zusammen mit den übrigen Befunden (Aktenstück 06) einen schwerwiegenden, systemischen Verstoß gegen WCAG 2.1 AA. Dies erhöht das Bußgeldrisiko, da die Verstöße nicht marginaler Natur sind, sondern die Kernanforderungen der Wahrnehmbarkeit und Bedienbarkeit betreffen.

Für die Klageerwiderung gegenüber VZ NRW (Aktenstück 21) ist zu argumentieren, dass Mandantin die Verstöße nach Kenntnis unverzüglich angegangen hat und ein detaillierter Sanierungsplan vorliegt (vgl. Aktenstück 16). Dies stützt den Verhältnismäßigkeitseinwand gegen eine Untersagungsverfügung.

---

*Quelle: WAI-ARIA 1.2 (W3C 2023, https://www.w3.org/TR/wai-aria-1.2/); WCAG 2.1 SC 4.1.2; Screenreader-Audit AccessCheck GmbH v. 24.03.2026*
