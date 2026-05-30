# Aktenstück 13 — Outsourcing-Regress: Lavendelhaus Design GbR Münster

**Bearbeitungsstand:** April/Mai 2026
**Bearb.:** Dr. A. Friedrichs

---

## 1. Sachverhalt Vertragsbeziehung

Tannenkamp Mode-Versand GmbH schloss im Jahr 2022 mit der Lavendelhaus Design GbR, Münster (Gesellschafter: Petra Lavendel, Jonas Hausmann) einen Dienstleistungsvertrag über:

- Entwicklung und Implementierung des Shopify-Themes „Lavanda Pro"
- Laufende Wartung und Pflege des Themes
- Technische Anpassungen auf Abruf (Time & Material)

Vertragsunterzeichnung: 14. März 2022. Vereinbarte Vergütung: 18.500 EUR einmalig für Entwicklung; monatlich 850 EUR Wartungspauschale. Gesamtzahlungen 2022–2026: ca. 68.500 EUR.

---

## 2. Regressfrage: Wer hat die BFSG-Mängel verursacht?

Die Barrierefreiheitsmängel (fehlendes Fokus-CSS, falsche ARIA-Roles, kein Skip-Link, fehlende Alt-Text-Infrastruktur) sind überwiegend im Shopify-Theme „Lavanda Pro" verankert. Das Theme wurde von Lavendelhaus Design GbR entwickelt und wird laufend gewartet.

**Argumente für Regressanspruch:**

1. Lavendelhaus Design war als IT-Dienstleister verpflichtet, den anerkannten Regeln der Technik zu folgen.
2. Die WCAG 2.1 AA waren bereits seit 2018 bekannt und allgemein anerkannt (vgl. BITV 2.0, die sie seit 2019 implementiert).
3. Das Theme wurde 2022 — vier Jahre vor BFSG-Inkrafttreten — entwickelt. Gute Praxis war bereits WCAG-Konformität bei Shopify-Theme-Entwicklung.
4. Die Wartungspflicht 2022–2026 umfasst nach Treu und Glauben die Anpassung an neue Rechtsanforderungen, die zum Zeitpunkt des Vertragsschlusses bereits absehbar waren (BFSG-Entwurf: 2020, BGBl. I 2021).
5. Lavendelhaus hat Mandantin nicht auf die BFSG-Anforderungen hingewiesen, obwohl das Gesetz 2021 veröffentlicht wurde.

**Gegenargumente Lavendelhaus (zu erwarten):**

1. Tannenkamp hat die konkreten Mängel (fehlende Alt-Texte) selbst durch Upload nicht-beschrifteter Produktbilder verursacht.
2. Wartungsvertrag enthält keine explizite Pflicht zur WCAG-Aufrüstung.
3. BFSG-Konformität war bei Vertragsschluss 2022 keine vertraglich geschuldete Eigenschaft des Themes.

---

## 3. Rechtliche Grundlage Regressanspruch

### 3.1 Werkvertrag (§§ 633 ff. BGB)

Die Theme-Entwicklung ist ein Werkvertrag. Schuldner eines Werkvertrags muss ein Werk herstellen, das frei von Mängeln ist (§ 633 Abs. 1 BGB). Ein Mangel liegt vor, wenn die vereinbarte Beschaffenheit fehlt oder das Werk sich für den nach dem Vertrag vorausgesetzten oder den gewöhnlichen Gebrauch nicht eignet (§ 633 Abs. 2 BGB).

Gewöhnlicher Gebrauch eines kommerziellen Online-Shop-Themes ist die Nutzung als rechtskonformer E-Commerce-Shop im europäischen Markt. Ab 28.06.2025 gehört WCAG 2.1 AA-Konformität zur Mindestanforderung für den gewöhnlichen Gebrauch.

Argument: Das Theme war ab 28.06.2025 mangelhaft im Sinne von § 633 Abs. 2 Nr. 2 BGB, da es für den nach dem Vertrag vorausgesetzten Zweck (Betrieb eines BFSG-konformen Shops) nicht geeignet war.

### 3.2 Verletzung vertraglicher Nebenpflichten (§ 241 Abs. 2 BGB)

Lavendelhaus Design als IT-Dienstleister mit Spezialkenntnissen hatte eine Hinweispflicht auf das BFSG (veröffentlicht 2021, Anwendung ab 2025). Die Nichterfüllung dieser Hinweispflicht begründet Schadensersatzpflicht nach §§ 280 Abs. 1, 241 Abs. 2 BGB.

### 3.3 Mitverschulden Tannenkamp (§ 254 BGB)

Alt-Texte: Tannenkamp ist selbst verantwortlich für den Upload von Produktbildern ohne Alt-Texte. Insoweit ist ein erhebliches Mitverschulden (mind. 50%) anzunehmen. Regressforderung für Alt-Texte-Sanierungskosten reduziert auf Quotenteil.

---

## 4. Regressforderung (Entwurf Quantifizierung)

| Schadensposten | Betrag | Mitverantwortung Lavendelhaus | Regressbetrag |
|---|---|---|---|
| Fokus-CSS-Korrektur | 800 EUR | 100% | 800 EUR |
| ARIA-Roles-Sanierung | 4.500 EUR | 80% | 3.600 EUR |
| Skip-Link-Implementierung | 300 EUR | 100% | 300 EUR |
| WCAG-Audit-Kosten | 8.500 EUR | 50% | 4.250 EUR |
| Rechtsberatungskosten anteilig | 5.000 EUR | 40% | 2.000 EUR |
| Alt-Texte-Sanierung (Theme-Infrastruktur) | 3.000 EUR | 30% | 900 EUR |
| **Gesamt** | **22.100 EUR** | | **11.850 EUR** |

---

## 5. Verfahrensstand

Regressforderungsschreiben wurde am 05.04.2026 per Einschreiben an Lavendelhaus Design GbR übersandt. Frist zur Stellungnahme: 30.04.2026. Reaktion von Lavendelhaus Design am 22.04.2026: Verweigerung jeglicher Haftung (vgl. EML 2026-04-05). Nächster Schritt: Schlichtungsangebot oder Klage vor LG Münster.

---

*Quelle: BGB §§ 241, 280, 633 (dejure.org/gesetze/BGB); BFSG § 14 (dejure.org/gesetze/BFSG)*
