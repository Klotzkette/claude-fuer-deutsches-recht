# Barrierefreiheit Web Checker

Prüf- und Dokumentationsplugin für digitale Barrierefreiheit von Websites, Webshops, Portalen, Apps und eingebetteten Dokumenten. Es verbindet den rechtlichen Scope-Check mit praktischer Webprüfung: BFSG/BFSGV, BITV 2.0, Web Accessibility Directive, European Accessibility Act, EN 301 549, WCAG, Tastaturbedienung, Screenreader, Formulare, Checkout, PDFs, Barrierefreiheitserklärung und Remediation-Roadmap.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Barrierefreiheit Web Checker (`barrierefreiheit-web-checker`, dieses Plugin) | [barrierefreiheit-web-checker.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/barrierefreiheit-web-checker.zip) |

Die URL ist stabil und zeigt nach dem nächsten Release auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Was das Plugin gut kann

- Ermitteln, ob eine Website öffentlich-rechtlich, BFSG-relevant, rein intern oder freiwillig zu prüfen ist.
- Einen Audit nach EN 301 549/WCAG-Prüflogik vorbereiten und dokumentieren.
- Tastatur, Fokus, Semantik, Screenreader, Kontrast, Formulare, Checkout und Downloads prüfen.
- Barrierefreiheitserklärung, Feedbackmechanismus und Maßnahmenplan formulieren.
- Agenturen, Entwicklerteams und Compliance-Verantwortliche mit klaren Abnahmekriterien führen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Kaltstart, Scope, Ziel, Rolle, Prüfobjekt und Workflow-Routing. |
| `scope-bfsg-bitv-wad` | Prüft, welcher Rechtsrahmen einschlägig ist: BFSG/BFSGV, BITV 2.0, EU-WAD, freiwilliger Standard. |
| `en301549-wcag-pruefplan` | Baut einen Prüfkatalog nach EN 301 549 und WCAG mit A/AA-Prioritäten. |
| `automatisierter-audit-axe-lighthouse` | Ordnet automatisierte Checks ein und warnt vor falscher Sicherheit. |
| `tastatur-fokus-navigation` | Prüft Tastaturbedienbarkeit, Fokusreihenfolge, Skiplinks, Menüs, Modale und Overlays. |
| `screenreader-semantik-aria` | Prüft Struktur, HTML-Semantik, Labels, ARIA, Überschriften, Live-Regionen und Fehlermeldungen. |
| `kontrast-farbe-motion-responsive` | Prüft Kontrast, Farbe ohne Farbcodierung, Reflow, Zoom, Animationen und Bewegung. |
| `formulare-checkout-ecommerce` | Prüft Webshop, Login, Warenkorb, Checkout, Fehlertexte, Zahlung und elektronische Verträge. |
| `pdf-downloads-dokumente` | Prüft PDFs, Downloads, eingebettete Dokumente und Alternativen. |
| `erklaerung-feedback-durchsetzung` | Erstellt Barrierefreiheitserklärung, Feedbackweg und Behörden-/Marktüberwachungsreaktion. |
| `remediation-roadmap-dokumentation` | Baut Maßnahmenplan, Priorisierung, Nachweise, Risikoampel und Re-Test-Protokoll. |
| `agentur-abnahme-vergabe` | Formuliert Lastenheft, Abnahmekriterien und Nachbesserungsanforderungen an Agenturen. |

## Quellenstand

Stand: Mai 2026. Rechtsprechung und Behördenpraxis werden nicht aus Modellwissen zitiert. Technische Standards ändern sich; insbesondere ist zwischen fachlich sinnvoller WCAG-2.2-Prüfung und rechtlich harmonisierten EN-301-549-Anforderungen zu unterscheiden.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 12 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agentur-abnahme-vergabe` | Unterstützt Agentursteuerung, Ausschreibung, Lastenheft und Abnahme barrierefreier Websites. Formuliert Anforderungen, Akzeptanzkriterien, Nachweis- und Re-Test-Pflichten, Pflegeprozess und Gewährleistungsfragen. Output: Lastenheft oder... |
| `allgemein` | Kaltstart, Scope und Workflow-Routing für digitale Barrierefreiheit. Fragt Website App Webshop öffentliche Stelle BFSG BITV EN 301 549 WCAG Zielgruppe Audit-Tiefe und Output ab, schlägt passende Skills vor und startet mit Prüfplan. |
| `automatisierter-audit-axe-lighthouse` | Ordnet automatisierte Accessibility-Scans mit axe, Lighthouse, Pa11y oder ähnlichen Tools ein. Erklärt Treffer, False Positives, False Negatives, manuelle Nachprüfung und Entwickler-Tickets. Output: Scanner-Auswertung. |
| `en301549-wcag-pruefplan` | Erstellt Prüfkatalog nach EN 301 549 und WCAG. Trennt rechtlich harmonisierten Standard von fachlicher WCAG-2.2-Erweiterung, definiert Seitentypen, Stichprobe, A/AA-Kriterien, manuelle Checks und Nachweise. Output: Auditplan. |
| `erklaerung-feedback-durchsetzung` | Erstellt Barrierefreiheitserklärung, Feedbackmechanismus, Durchsetzungs- und Behördenreaktion. Trennt öffentliche Stellen, BFSG-relevante Dienste und freiwillige Erklärungen. Output: Erklärung, Antwortbrief oder Maßnahmenvermerk. |
| `formulare-checkout-ecommerce` | Prüft Formulare, Login, Suche, Warenkorb, Checkout, Zahlungsstrecke und elektronische Verträge in Webshops. Fokus BFSG/E-Commerce, Fehlermeldungen, Labels, Pflichtfelder, Zeitlimits und Bestellabschluss. Output: Checkout-Audit. |
| `kontrast-farbe-motion-responsive` | Prüft Kontrast, Farbe ohne Farbcodierung, Zoom, Reflow, Textabstände, responsives Layout, Animationen, Motion-Reduction, Hover-Fallen und mobile Nutzung. Output: visuelle Barrierefreiheitsmatrix. |
| `pdf-downloads-dokumente` | Prüft PDFs, Downloads, eingebettete Dokumente, Preislisten, AGB, Formulare und Bescheide auf Barrierefreiheit: Tags, Lesereihenfolge, Alternativtexte, Tabellen, Formularfelder und HTML-Alternative. Output: Dokumenten-Audit. |
| `remediation-roadmap-dokumentation` | Erstellt Maßnahmenplan für Barrierefreiheits-Fixes: Priorisierung, Nutzerimpact, Rechtsrisiko, Aufwand, Owner, Tickets, Re-Test, Nachweisakte und Management-Reporting. Output: Roadmap und Dokumentation. |
| `scope-bfsg-bitv-wad` | Prüft den Rechtsrahmen digitaler Barrierefreiheit: BFSG, BFSGV, BITV 2.0, Web Accessibility Directive, European Accessibility Act, öffentlicher Sektor, B2C-E-Commerce, Kleinstunternehmen und freiwilliger Standard. Output: Scope-Memo. |
| `screenreader-semantik-aria` | Prüft Screenreader-Nutzbarkeit, HTML-Semantik, Landmarken, Überschriften, Labels, Alt-Texte, ARIA, Live-Regionen, Fehlermeldungen und dynamische Komponenten. Output: Screenreader-Prüfprotokoll. |
| `tastatur-fokus-navigation` | Prüft Tastaturbedienbarkeit, Fokusreihenfolge, sichtbaren Fokus, Skiplinks, Menüs, Modale, Cookie-Banner, Slider, Accordions und Tastaturfallen. Output: Tastaturprotokoll und Fix-Tickets. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
