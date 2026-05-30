# Aktenstück 15 — Bußgeldverteidigung § 37 BFSG: Strategie und Bemessungsargumente

**Bearbeitungsstand:** Mai 2026
**Bearb.:** Dr. A. Friedrichs

---

## 1. Bußgeldrahmen § 37 BFSG

§ 37 Abs. 1 BFSG: Ordnungswidrigkeit, Geldbuße bis 100.000 EUR für vorsätzliche oder fahrlässige Verstöße gegen die materiellen Barrierefreiheitsanforderungen (§ 14 BFSG).

§ 37 Abs. 2 BFSG: Verstöße gegen Verfahrenspflichten (Erklärung zur Barrierefreiheit § 19 BFSG-DV, Feedback-Mechanismus § 16 BFSG-DV): Geldbuße bis 50.000 EUR.

Kumulation: Mehrere Verstöße können kumulativ geahndet werden, jedoch gelten die allgemeinen Grundsätze des OWiG (Tateinheit, Tatmehrheit, Gesamtgeldbuße).

---

## 2. Bemessungsfaktoren § 17 OWiG

| Faktor | Wirkung | Bewertung Tannenkamp |
|---|---|---|
| Schwere des Verstoßes | Erhöhend | Mehrere gleichzeitige Verstöße, aber kein totaler Shop-Ausfall |
| Dauer des Verstoßes | Erhöhend | 9,5 Monate (28.06.2025–Meldung 12.03.2026) |
| Vorsatz vs. Fahrlässigkeit | Erhöhend bei Vorsatz | Fahrlässigkeit (keine Kenntnis BFSG-Details) |
| Wirtschaftliche Verhältnisse | Variabel | 18 Mio. EUR Umsatz; GF persönlich nicht haftbar |
| Vorteil aus Verstoß | Erhöhend | Einsparung WCAG-Conformance-Entwicklung ca. 35.000 EUR |
| Nachtatverhalten | Mindernd | Sofortige Kooperation, Audit, Sanierungsplan, Erklärung veröffentlicht |
| Keine Vorstrafe | Mindernd | Erstverstoß |

---

## 3. Verteidigungsargumente gegen Maximalbußgeld

### 3.1 Keine Vorsatz-Komponente

Tannenkamp hatte keine positive Kenntnis der konkreten WCAG-Verstöße bis zur VZ-NRW-Meldung. Das BFSG war 2021 in Kraft getreten, aber eine offizielle Konkretisierung für private Online-Shops durch staatliche Stellen fehlte. MüNI hat vor März 2026 keine Abmahnung oder Hinweis erteilt. Fahrlässigkeit ist anzunehmen, nicht Vorsatz (§ 10 OWiG).

### 3.2 Verantwortungsverschiebung: Lavendelhaus Design

Kernmängel (ARIA-Roles, Fokus-CSS, Skip-Link) sind im Theme verankert — Verantwortung liegt primär beim Theme-Entwickler. Tannenkamp als Laie durfte auf die Fachkompetenz des beauftragten IT-Dienstleisters vertrauen (§ 11 OWiG — Verbotsirrtum, zumindest bei Fahrlässigkeitsbemessung relevant).

### 3.3 Kooperationsbereitschaft und Selbst-Abhilfe

Mandantin hat unverzüglich nach Kenntniserlangung:
- Vollständigen Audit beauftragt und Ergebnis offen gelegt
- Erklärung zur Barrierefreiheit veröffentlicht
- Feedback-Mechanismus eingerichtet
- Detaillierten Sanierungsplan vorgelegt
- Erste technische Fixes implementiert (Kontrast-CSS am 20.04.2026)

Dieses Nachtatverhalten ist nach § 17 Abs. 3 OWiG strafmindernd zu berücksichtigen.

### 3.4 Unverhältnismäßigkeit des Maximalrahmens

Das Maximalbußgeld von 100.000 EUR entspricht ca. 0,56% des Jahresumsatzes. Im Vergleich zu den Kosten der WCAG-Sanierung (ca. 35.000–80.000 EUR, vgl. Aktenstück 20) wäre das Maximalbußgeld ein weiteres äquivalentes Sanierungsprojekt. Die Praxis der Bußgeldbehörden zeigt, dass bei erstmaligen, fahrlässigen Verstößen mit sofortiger Abhilfe Bußgelder von 10–25% des Rahmens realistisch sind.

---

## 4. Realistisches Verhandlungsziel

| Szenario | Bußgeld | Bedingung |
|---|---|---|
| Optimistisch | 8.000–12.000 EUR | MüNI akzeptiert Sanierungsplan; Erstverstoß; Fahrlässigkeit |
| Realistisch | 15.000–22.000 EUR | Standardfall |
| Pessimistisch | 35.000–50.000 EUR | MüNI wertet als systematischen Verstoß; Tatmehrheit |
| Worst Case | 75.000–100.000 EUR | Untersagungsverfügung + Bußgeld; nur bei Nichtkooperation |

---

## 5. Vorgehen

Schriftlicher Antrag an MüNI auf Anwendung des Mindestmaßes gemäß § 17 Abs. 3 OWiG, verbunden mit Nachweis: Sanierungsfortschritt bis 31.07.2026 (Meilenstein 1: Kontrast, Fokus, Skip-Link) als Anlage zur Stellungnahme. Bei Bußgeldbescheid: Einspruch innerhalb der Frist (§ 67 OWiG: zwei Wochen); Antrag auf mündliche Verhandlung vor dem AG.

---

*Quelle: BFSG § 37 (dejure.org/gesetze/BFSG/37.html); OWiG §§ 10, 11, 17 (dejure.org/gesetze/OWiG); BFSG-DV §§ 16, 19*
