# 09 — PEP-Screening-Fehler

**Rechtsgrundlage:** § 10 Abs. 1 Nr. 4, § 15 Abs. 3 Nr. 1, Abs. 5 GwG; BaFin-Auslegungshinweise GwG (Oktober 2021)
**Betroffene Kunden:** HR-11 (Georgien), HR-23 (Moldau), HR-31 (Nordmazedonien)
**PEP-Screening-Anbieter:** SymphonyAI Sensa (Vertrag seit 2021, zuletzt aktualisiert Oktober 2022)

---

## Rechtlicher Rahmen

Politisch exponierte Personen (PEP) i.S.d. § 1 Abs. 12 GwG unterliegen nach § 15 Abs. 3 Nr. 1 GwG verschärften Anforderungen. Dazu zählen:
- Einholung der Zustimmung der Geschäftsleitung vor Begründung der Geschäftsbeziehung (§ 15 Abs. 5 Nr. 2 GwG)
- Feststellung der Herkunft der eingesetzten Vermögenswerte (§ 15 Abs. 5 Nr. 3 GwG)
- Laufende, verstärkte Überwachung der Geschäftsbeziehung (§ 15 Abs. 5 Nr. 4 GwG)

Der Begriff "PEP" umfasst nach § 1 Abs. 12 Nr. 4 GwG auch Mitglieder von Leitungsorganen staatseigener Unternehmen sowie deren unmittelbare Familienangehörige (§ 1 Abs. 13 GwG) und bekannte enge Mitarbeiter (§ 1 Abs. 14 GwG).

---

## Technische Ursache des Screening-Fehlers

Das SymphonyAI-Sensa-System wird von Thalvenia für alle Kunden beim Onboarding und danach jährlich eingesetzt. Der Vertrag mit SymphonyAI sieht folgende Leistungen vor:
- Weltweite PEP-Datenbank: Tier 1 (Staatsoberhäupter, Minister, Parlamentarier)
- Sanktionslisten: EU, USA (OFAC), UN, Großbritannien

**Nicht enthalten:** Tier 2 (Vize-Minister, Staatssekretäre, mittlere Beamtenebene, regionale Politiker nicht-westlicher Staaten). Dies betrifft besonders Länder der früheren Sowjetunion und des Balkans, wo PEP-Definitionen breiter sind und die BaFin-Auslegungshinweise eine entsprechend erweiterte Datenabdeckung verlangen.

---

## Einzelfälle

### Kunde HR-11 — Georgischer Ministerialbeamter
- Onboarding: März 2022
- Funktion bei Onboarding: Leiter der Abteilung für Haushalt und Finanzen im georgischen Wirtschaftsministerium (Ministerialebene II, nicht Tier 1)
- PEP-Screening-Ergebnis 2022: "Kein Treffer"
- Entdeckung: August 2025, durch Pressebericht (Ermittlungsverfahren in Georgien)
- Nachträgliche Einschätzung: PEP-Status nach § 1 Abs. 12 Nr. 4 GwG seit Onboarding gegeben

**Konsequenz:** Sämtliche Transaktionen seit März 2022 (EUR 6,3 Mio.) wurden ohne GF-Genehmigung und ohne verstärkte Überwachung abgewickelt.

### Kunde HR-23 — Moldauischer Bürgermeister a.D.
- Onboarding: Juli 2023
- Funktion: Ehemaliger Bürgermeister einer Stadt mit über 50.000 Einwohnern (Moldova); amtlich bis 2021
- PEP-Screening-Ergebnis 2023: "Kein Treffer"
- Technische Ursache: Bürgermeister mittelgroßer Städte in Moldova nicht in Tier-1-Datenbank erfasst
- Nachträgliche Einschätzung: PEP-Status nach § 1 Abs. 12 Nr. 5 GwG (kommunale Leitungsorgane)

### Kunde HR-31 — Nordmazedonischer Richter am Obersten Gericht
- Onboarding: Januar 2024
- Funktion: Aktiver Richter am Obersten Gericht Nordmazedoniens
- PEP-Screening-Ergebnis 2024: "Kein Treffer"
- Technische Ursache: Justizbehörden Nordmazedoniens nicht in Tier-1-Datenbank
- Nachträgliche Einschätzung: PEP-Status nach § 1 Abs. 12 Nr. 6 GwG (leitende Mitglieder der Judikative)

---

## Bewertung durch BaFin

Prüferin Wunderwald beurteilte die drei PEP-Fälle als systematischen Mangel, nicht als Einzelversagen. Das Institut hätte bei Aufnahme von Geschäftsbeziehungen mit natürlichen Personen aus osteuropäischen Ländern mit erhöhtem Korruptionsrisiko (CPI-Score < 45) proaktiv eine erweiterte Datenbank verwenden müssen.

Die BaFin verweist auf ihre Auslegungshinweise GwG (Oktober 2021), Abschnitt zu § 1 Abs. 12, wonach Institute verpflichtet sind, die Qualität der verwendeten PEP-Datenbanken risikoadäquat zu prüfen und ggf. mehrere Datenbanken zu kombinieren.

---

## Sofortmaßnahmen (Remediation)

1. Upgrade SymphonyAI-Sensa-Vertrag auf Tier-1 + Tier-2-Abdeckung (beauftragt April 2026).
2. Retrograde PEP-Überprüfung aller Hochrisikokunden aus Tier-2-relevanten Ländern (abgeschlossen Mai 2026).
3. Drei betroffene Kunden: formelle Nacherfüllung der PEP-Pflichten; GF-Genehmigungen nachgeholt; verstärkte Überwachung aktiviert.
4. Compliance-Schulung PEP-Erkennung: alle AML-relevanten Mitarbeiter (Juni 2026).

**Vgl.:** 08-kundenidentifikation-kyc-mangel.md; 07-aml-pflichten-gwg-katalog.md
