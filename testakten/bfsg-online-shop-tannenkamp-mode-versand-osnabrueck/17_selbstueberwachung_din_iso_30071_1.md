# Aktenstück 17 — Selbstüberwachung nach DIN ISO 30071-1

**Bearbeitungsstand:** Mai 2026
**Bearb.:** Dr. A. Friedrichs / IT-Leiter Wörmann

---

## 1. Ausgangslage und Regulierungsrahmen

§ 17 BFSG-DV sieht vor, dass Dienstleistungserbringer interne Verfahren zur Selbstüberwachung der Barrierefreiheit einrichten sollen. Für Online-Dienste empfiehlt die BFSG-DV-Begründung die Orientierung an ISO 30071-1:2019 (Information technology — Development of user interface accessibility — Part 1: Code of practice for creating accessible ICT products and services).

---

## 2. DIN ISO 30071-1 — Grundstruktur

DIN ISO 30071-1 ist ein Verhaltenskodex für Organisationen, der Barrierefreiheit als integralen Bestandteil des Entwicklungs- und Beschaffungsprozesses verankert. Die Norm gliedert sich in:

- **Abschnitt 4:** Planung — Barrierefreiheitsziele und Ressourcenplanung
- **Abschnitt 5:** Designprozess — WCAG als Mindeststandard, Nutzertests mit behinderten Anwendern
- **Abschnitt 6:** Entwicklung — Entwicklungsstandards, Code-Reviews
- **Abschnitt 7:** Test — Automatisierte und manuelle Tests, Regressionstests
- **Abschnitt 8:** Beschaffung — Anforderungen an Drittprodukte (Themes, Plugins)
- **Abschnitt 9:** Betrieb — Monitoring, Feedbackverarbeitung, Schulung

---

## 3. Defizite bei Tannenkamp (Ist-Zustand)

| DIN ISO 30071-1 Abschnitt | Anforderung | Status Tannenkamp |
|---|---|---|
| 4 — Planung | Barrierefreiheitsziele definiert | Nicht vorhanden |
| 5 — Design | WCAG als Mindeststandard im Design-Briefing | Nicht vereinbart |
| 6 — Entwicklung | Code-Review auf WCAG | Nicht vorhanden |
| 7 — Test | Automatisierter WCAG-Test in CI/CD | Nicht vorhanden |
| 8 — Beschaffung | Barrierefreiheitsanforderungen in Lieferantenverträgen | Nicht im Lavendelhaus-Vertrag |
| 9 — Betrieb | Regelmäßige Audits (mind. jährlich) | Nicht vorhanden |

---

## 4. Empfehlungen für ein BFSG-konformes Selbstüberwachungssystem

### 4.1 Internes Barrierefreiheits-Audit-Programm

Jährlicher Audit durch externen Dienstleister (AccessCheck GmbH oder gleichwertig). Automatisierter Scan (axe DevTools, Lighthouse) monatlich durch IT-Leiter Wörmann. Ergebnisse in Ticket-System (Jira) dokumentieren.

### 4.2 Barrierefreiheit in Entwicklungs-Pipeline

Bei allen künftigen Shopify-Theme-Anpassungen: Vorab-WCAG-Check durch Lavendelhaus Design als Vertragspflicht (Vertragsanpassung erforderlich). Einbau automatisierter WCAG-Tests in die Shopify-Staging-Umgebung vor Go-Live.

### 4.3 Anforderungen an Lieferantenverträge

Künftige IT-Dienstleisterverträge müssen enthalten: explizite WCAG 2.1 AA-Konformitätszusage, Garantie für barrierefreie Auslieferung, Nachbesserungspflicht ohne Mehrkosten bei WCAG-Verstoß, VPAT (Voluntary Product Accessibility Template) bei Auslieferung.

### 4.4 Monitoring und Kennzahlen

| KPI | Messmethode | Ziel |
|---|---|---|
| Anzahl WCAG-Fehler (automatisiert) | axe-Scan monatlich | Null kritische Fehler |
| Kontrastprobleme | Lighthouse CI | Null |
| Fehlende Alt-Texte | Shopify-API-Report | Null neue Bilder ohne Alt |
| Feedback-Eingänge Barrierefreiheit | E-Mail-Zählung | Bearbeitungsrate 100% |
| Audit-Abdeckung | Jährlicher Bericht | 100% aller Seitenkategorien |

---

## 5. Konsequenz für Verfahren

Der Aufbau eines DIN ISO 30071-1-konformen Selbstüberwachungssystems ist kein gesetzliches Muss im Sinne einer sanktionsbewehrten Pflicht. Er ist jedoch der beste Beweis gegenüber MüNI und LG Hannover, dass Tannenkamp Mode-Versand BFSG-Compliance dauerhaft sicherstellt. Für die Klageerwiderung und die Einigung mit der VZ NRW ist die Einrichtung dieses Systems als Verpflichtung zuzusagen.

---

*Quelle: BFSG-DV § 17; DIN ISO 30071-1:2019 (Beuth-Verlag)*
