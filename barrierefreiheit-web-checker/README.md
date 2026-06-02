# Barrierefreiheit Web Checker

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`barrierefreiheit-web-checker`) | [`barrierefreiheit-web-checker.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/barrierefreiheit-web-checker.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BFSG-Verstoß Tannenkamp Mode-Versand GmbH — Online-Shop Barrierefreiheit Osnabrück** (`bfsg-online-shop-tannenkamp-mode-versand-osnabrueck`) | [Gesamt-PDF lesen](../testakten/bfsg-online-shop-tannenkamp-mode-versand-osnabrueck/gesamt-pdf/bfsg-online-shop-tannenkamp-mode-versand-osnabrueck_gesamt.pdf) | [`testakte-bfsg-online-shop-tannenkamp-mode-versand-osnabrueck.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bfsg-online-shop-tannenkamp-mode-versand-osnabrueck.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agentur-abnahme-vergabe` | Unterstützt Agentursteuerung, Ausschreibung, Lastenheft und Abnahme barrierefreier Websites. Formuliert Anforderungen, Akzeptanzkriterien, Nachweis- und Re-Test-Pflichten, Pflegeprozess und Gewährleistungsfragen. Output: Lastenheft oder... |
| `allgemein` | Kaltstart, Scope und Workflow-Routing für digitale Barrierefreiheit. Fragt Website App Webshop öffentliche Stelle BFSG BITV EN 301 549 WCAG Zielgruppe Audit-Tiefe und Output ab, schlägt passende Skills vor und startet mit Prüfplan. |
| `automatisierter-audit-axe-lighthouse` | Ordnet automatisierte Accessibility-Scans mit axe, Lighthouse, Pa11y oder ähnlichen Tools ein. Erklärt Treffer, False Positives, False Negatives, manuelle Nachprüfung und Entwickler-Tickets. Output: Scanner-Auswertung. |
| `bf-kanzleiwebsite-konkret` | Kanzleiwebsite konkret pruefen: Pflicht ab BFSG 28.06.2025 fuer aktive E-Commerce-Aktivitaeten, fuer reine Informationswebsites empfohlen, Tooling Axe / WAVE / Lighthouse, Workflow Designer und Entwickler. Konkrete Fix-Liste fuer typisch... |
| `bf-kiosk-und-selbstbedienung-spezial` | Spezialfall Selbstbedienungsterminals (Bankautomat, Ticketautomat, Fahrkartenautomat) nach BFSG: Hardware- und Software-Anforderungen EN 301 549 Kap. 8, Bedienelemente Reichweite, Sprachausgabe, Kontrast. Pruefraster und Bezugnahme zu No... |
| `bf-mediendienste-untertitel-spezial` | Spezialfall Mediendienste: Untertitel, Audiodeskription, Gebaerdensprache, ARD/ZDF-Linie, AVMD-Richtlinie, MStV. Pflichten fuer Streaming-Anbieter und Mediatheken. Pruefraster fuer Eigenproduktionen Kanzlei (Podcasts, Webinare, Videos). |
| `bf-pdf-schriftsaetze-versand` | Spezialfall barrierefreies PDF beim Versand von Schriftsaetzen: getaggte PDF, Lesefolge, Schriftgroesse, OCR-Schicht, Beschreibungen Bilder. Schnittstelle eA und beA. Pruefliste fuer Anwaltskanzlei. Routet in pdf-formulare-und-formulare-... |
| `bfsg-zeitleiste-und-pflichten` | Barrierefreiheitsstaerkungsgesetz BFSG Zeitleiste und Pflichten einfuehrend: Inkrafttreten 28.06.2025, betroffene Produkte (PC, Smartphone, Selbstbedienungsterminal), Dienstleistungen (E-Commerce, E-Books, Bankdienstleistungen, Personenb... |
| `ecommerce-checkout-pruefung-spezial` | Spezialpruefung E-Commerce-Checkout: Warenkorb, Adresseingabe, Bezahlung, Bestaetigung. Typische Stolpersteine: AGB-Modal, dynamische Versandkosten, Coupon-Felder, 3D-Secure-Fenster. Pruefraster Tastatur-only-Bestellung und Screenreader-... |
| `en301549-wcag-pruefplan` | Erstellt Prüfkatalog nach EN 301 549 und WCAG. Trennt rechtlich harmonisierten Standard von fachlicher WCAG-2.2-Erweiterung, definiert Seitentypen, Stichprobe, A/AA-Kriterien, manuelle Checks und Nachweise. Output: Auditplan. |
| `erklaerung-feedback-durchsetzung` | Erstellt Barrierefreiheitserklärung, Feedbackmechanismus, Durchsetzungs- und Behördenreaktion. Trennt öffentliche Stellen, BFSG-relevante Dienste und freiwillige Erklärungen. Output: Erklärung, Antwortbrief oder Maßnahmenvermerk. |
| `formulare-checkout-ecommerce` | Prüft Formulare, Login, Suche, Warenkorb, Checkout, Zahlungsstrecke und elektronische Verträge in Webshops. Fokus BFSG/E-Commerce, Fehlermeldungen, Labels, Pflichtfelder, Zeitlimits und Bestellabschluss. Output: Checkout-Audit. |
| `kontrast-farbe-motion-responsive` | Prüft Kontrast, Farbe ohne Farbcodierung, Zoom, Reflow, Textabstände, responsives Layout, Animationen, Motion-Reduction, Hover-Fallen und mobile Nutzung. Output: visuelle Barrierefreiheitsmatrix. |
| `native-apps-ios-android-pruefung` | Native Apps iOS und Android pruefen: Accessibility-API VoiceOver bzw. TalkBack, Plattform-spezifische Pattern, EN 301 549 Klausel 11. Tooling Xcode Accessibility Inspector, Android Accessibility Scanner. Konkrete Code-Beispiele Swift und... |
| `pdf-downloads-dokumente` | Prüft PDFs, Downloads, eingebettete Dokumente, Preislisten, AGB, Formulare und Bescheide auf Barrierefreiheit: Tags, Lesereihenfolge, Alternativtexte, Tabellen, Formularfelder und HTML-Alternative. Output: Dokumenten-Audit. |
| `pdf-formulare-und-formulare-barrierefrei` | PDF-Formulare und HTML-Formulare barrierefrei: Tag-Struktur, Lesefolge, Formularfeld-Beschriftungen, Fehlertexte, Pflichtfeld-Markierung, autocomplete-Attribute, Tastatursteuerung. Pruefraster PDF mit PAC 2024 und Acrobat. Sanierungsstra... |
| `remediation-roadmap-dokumentation` | Erstellt Maßnahmenplan für Barrierefreiheits-Fixes: Priorisierung, Nutzerimpact, Rechtsrisiko, Aufwand, Owner, Tickets, Re-Test, Nachweisakte und Management-Reporting. Output: Roadmap und Dokumentation. |
| `schulung-und-rolle-accessibility-champion` | Schulungsprogramm und Accessibility-Champion-Modell in der Organisation aufbauen: Rollendefinition, Aufgaben, Zeitbudget, Trainingsplan fuer Design, Entwicklung, QA, Content, Marketing. Pruefraster fuer Reifegrad und Schulungslevel. |
| `scope-bfsg-bitv-wad` | Prüft den Rechtsrahmen digitaler Barrierefreiheit: BFSG, BFSGV, BITV 2.0, Web Accessibility Directive, European Accessibility Act, öffentlicher Sektor, B2C-E-Commerce, Kleinstunternehmen und freiwilliger Standard. Output: Scope-Memo. |
| `screenreader-semantik-aria` | Prüft Screenreader-Nutzbarkeit, HTML-Semantik, Landmarken, Überschriften, Labels, Alt-Texte, ARIA, Live-Regionen, Fehlermeldungen und dynamische Komponenten. Output: Screenreader-Prüfprotokoll. |
| `spezial-abnahme-formular-portal-und-einreichung` | Abnahme: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-audit-schriftsatz-brief-und-memo-bausteine` | Audit: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-barrierefreiheit-red-team-und-qualitaetskontrolle` | Barrierefreiheit: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-barrierefreiheits-erstpruefung-und-mandatsziel` | Barrierefreiheits: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bfsg-tatbestand-beweis-und-belege` | BFSG: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bfsgv-fristen-form-und-zustaendigkeit` | Bfsgv: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bitv-dokumentenmatrix-und-lueckenliste` | BITV: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-checkout-beweislast-und-darlegungslast` | Checkout: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ecommerce-mandantenkommunikation-entscheidungsvorlage` | Ecommerce: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erklaerung-mehrparteien-konflikt-und-interessen` | Erklaerung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-formulare-zahlen-schwellen-und-berechnung` | Formulare: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pdfs-compliance-dokumentation-und-akte` | Pdfs: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefung-sonderfall-und-edge-case` | Pruefung: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-roadmap-internationaler-bezug-und-schnittstellen` | Roadmap: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rolle-abschlussprodukt-und-uebergabe` | Rolle: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schulung-fristennotiz-und-naechster-schritt` | Schulung: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-scope-behoerden-gericht-und-registerweg` | Scope: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-screenreader-livequellen-und-rechtsprechungscheck` | Screenreader: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-tastatur-verhandlung-vergleich-und-eskalation` | Tastatur: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wcag-risikoampel-und-gegenargumente` | Wcag: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `tastatur-fokus-navigation` | Prüft Tastaturbedienbarkeit, Fokusreihenfolge, sichtbaren Fokus, Skiplinks, Menüs, Modale, Cookie-Banner, Slider, Accordions und Tastaturfallen. Output: Tastaturprotokoll und Fix-Tickets. |
| `ueberwachungsstelle-und-rechtsfolgen` | Marktueberwachung und Rechtsfolgen bei BFSG-Verstoss: zustaendige Stellen, Bussgeldrahmen bis 100.000 Euro, Vertriebsverbot, Verbandsklagen UKlaG, Abmahnungen UWG (umstritten). Pruefraster zu Verteidigungslinien und Vergleichsverhandlung... |
| `usability-test-mit-betroffenen` | Usability-Test mit Betroffenen organisieren: Auswahl Teilnehmender (Sehbehinderung, Blindheit, motorische Einschraenkungen, Hoerbehinderung, kognitive Behinderung), Hilfsmittel, Aufgaben-Szenarien, Ethik-Einverstaendnis, Aufwandsentschae... |
| `wcag-vs-en-301-549-mapping` | Mapping WCAG 2.2 zu EN 301 549 V 3.2.1: WCAG-Erfolgskriterien, EN-Klauseln, BITV-Anforderungen in Tabelle. Pruefraster welche Anforderung welche Norm bedient, wo die EN ueber WCAG hinausgeht (mobile, biometrische, mehrteilige Inhalte). T... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin barrierefreiheit-web-checker: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin barrierefreiheit-web-checker: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin barrierefreiheit-web-checker: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin barrierefreiheit-web-checker: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin barrierefreiheit-web-checker: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin barrierefreiheit-web-checker: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin barrierefreiheit-web-checker: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin barrierefreiheit-web-checker: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin barrierefreiheit-web-checker: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin barrierefreiheit-web-checker: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
