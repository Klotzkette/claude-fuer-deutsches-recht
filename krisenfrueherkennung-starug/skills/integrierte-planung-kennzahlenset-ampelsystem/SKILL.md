---
name: integrierte-planung-kennzahlenset-ampelsystem
description: "Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) für StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB §§ 242 ff. (Jahresabschluss), § 1 StaRUG. Prüfraster: GuV-Plan, Bilanzplan, Cash-Flow-Statement, Working-Capital-Modell, Investitions-/Finanzierungsplan, Brucke Ergebnis-Liquiditaet. Output Excel-Modell-Template, Planungsannahmen-Memo. Abgrenzung: Liquiditaetsplanung rolling siehe rollierende-liquiditaetsplanung-24-monate-template; Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform im Krisenfrueherkennung Starug."
---

# Integrierte Planung — GuV, Bilanz und Cashflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StaRUG; § 1 StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Wer nur eine GuV-Planung vorlegt, hat keinen Finanzplan. Wer nur eine Liquiditätsplanung vorlegt, hat kein Steuerungsinstrument. Das Drei-Statement-Modell verknüpft Gewinn- und Verlustrechnung, Bilanz und Kapitalflussrechnung zu einer konsistenten Planung, die jedem Anspruch — ob IDW S 6, IDW S 11 oder § 1 StaRUG — standhält. Ohne diese Verknüpfung sind Restrukturierungskonzepte nicht belastbar und Fortführungsprognosen nicht fundiert.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht, integrierte Planung als Standard)
- IDW S 6 in aktueller Fassung als methodischer Rahmen für Sanierungskonzepte
- IDW S 11 als methodischer Rahmen für Insolvenzeröffnungsgründe und Fortbestehensprognose
- § 18 InsO (drohende Zahlungsunfähigkeit — integrierte Sicht nötig)
- § 252 Abs. 1 Nr. 2 HGB (Going-Concern-Prinzip in der Rechnungslegung)
- DRS 21 (Kapitalflussrechnung nach DRSC-Standard)

---

## Pflichten

### 1. Warum alle drei Statements zwingend sind

Jede der drei Planungsebenen beantwortet andere Fragen:

| Statement | Kernfrage | Relevanz im StaRUG-Kontext |
|---|---|---|
| GuV | Ist das Geschäftsmodell profitabel? | Ertragslage, EBITDA-Coverage |
| Bilanz | Ist das Unternehmen solvent? | Eigenkapital, Überschuldungsstatus |
| Cashflow | Kann das Unternehmen zahlen? | Zahlungsunfähigkeit, Liquidität |

Ein Unternehmen kann bilanziell positives Eigenkapital haben und trotzdem zahlungsunfähig sein (Ergebnis vs. Cash). Ein anderes kann Verluste schreiben, aber noch Liquidität haben (Abschreibungen). Nur die integrierte Sicht zeigt die volle Wahrheit.

### 2. Interlinkage — Die drei Aussagen müssen sich rechnerisch schließen

```
GuV → Jahresergebnis fließt ins Eigenkapital der Bilanz
Bilanz → Veränderung Working Capital ist Cashflow-Treiber
Cashflow → Endbestand ist Kassenposition in der Bilanz

KONTROLLFORMEL:
 Kassenbestand (Bilanz) = Kassenbestand Vorjahr + Cashflow aus lfd. Geschäft
 + Cashflow aus Investitionstätigkeit
 + Cashflow aus Finanzierungstätigkeit
```

---

## Templates

### Muster: Planprämissen-Tabelle (Drei-Statement-Modell)

```
PLANPRÄMISSEN — DREI-STATEMENT-MODELL
Gesellschaft: [Firma]
Basisjahr: [JJJJ]
Planperiode: [JJJJ+1] bis [JJJJ+2]

GuV-TREIBER
 Umsatzwachstum p.a.: Base [x%] / Bear [-x%]
 Materialkostenquote: [x%] des Umsatzes
 Personalkostensteigerung: [x%] p.a. (Tariferhöhung + Headcount)
 Abschreibungsquote: [x% auf Anlagevermögen Ø]
 Effektivzinssatz: [x%] auf Ø Bankverbindlichkeiten

WORKING CAPITAL
 DIO (Vorräte): [x] Tage
 DSO (Forderungen): [x] Tage
 DPO (Verbindlichkeiten): [x] Tage

INVESTITIONEN
 Erhaltungs-CAPEX: EUR [x] p.a.
 Wachstums-CAPEX: EUR [x] (einmalig in [JJJJ])

FINANZIERUNG
 Tilgung Bankkredit: EUR [x] p.a.
 Neue Kreditaufnahme: EUR [x] in [JJJJ]
 Ausschüttung: EUR [x] (oder: keine Ausschüttung in der Planperiode)
```

---

## Fallstricke

1. **GuV-Planung ohne Cashflow** — in der Praxis verbreitet und gefährlich: profitables Unternehmen kann illiquid werden, wenn Working Capital wächst (z.B. Vorratsaufbau bei Umsatzwachstum).

2. **Planbilanzen werden vergessen** — viele Restrukturierungspläne haben GuV und Cash, aber keine Bilanz. IDW S 6 und IDW S 11 verlangen aber explizit die Planbilanz, um Überschuldungsstatus zu beurteilen.

3. **Stichtagsbezogene statt periodengerechte Abgrenzung** — Rückstellungen und Abgrenzungen in der Bilanzplanung vergessen → rechnerische Lücken zwischen GuV und Cashflow.

4. **Investitionsplanungen ohne Finanzierungsquelle** — CAPEX-Pläne, die nicht mit konkreter Finanzierungsstruktur unterlegt sind, sind Wunschlisten, keine valide Planung.

5. **Steuerlast unterschätzen** — Ertragsteuern, Umsatzsteuer, Lohnsteuer, Sozialversicherung und steuerliche Effekte von Sanierungsmaßnahmen müssen bei Wesentlichkeit in Cash und Ergebnis abgebildet werden.

6. **Krisenursachen nicht verknüpfen** — Planung verbessert sich, ohne dass eine Maßnahme die Ursache erklärt. Dann ist es keine Sanierungsplanung, sondern eine Wunschrechnung.

7. **Kleine Unternehmen unterprüfen** — bei geringerer Komplexität darf die Darstellung schlanker sein, aber GuV, Bilanz, Liquidität, Maßnahmen und Belege müssen trotzdem zusammenpassen.

---

## Aktuelle Leitentscheidungen — Integrierte Planung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- IDW S 6 — Anforderungen an Sanierungskonzepte, aktuelle Fassung 2023; integrierte Unternehmensplanung als Kernbaustein jedes belastbaren Sanierungskonzepts.

## Paragrafenkette Integrierte Planung

§ 19 Abs. 2 InsO (Fortbestehensprognose auf Basis integrierter Planung) → IDW S 6 (Sanierungskonzept-Standard) → IDW S 11 (Beurteilung Insolvenzgruende) → § 1 StaRUG (24-Monats-Horizont) → § 43 GmbHG (Sorgfaltspflicht bei Planung)

## Triage — Integrierte Planung

1. **Drei-Sicht-Verknuepfung?** Guv-Planung → Cashflow (direkte Methode) → Bilanz-Planung konsistent?
2. **Annahmen dokumentiert?** Umsatz-Wachstumsraten, Kostenentwicklung, Working-Capital-Annahmen transparent?
3. **Szenarien?** Base-Case, Best-Case, Worst-Case durchgerechnet?
4. **Saldo-Check?** Integrierte Planung muss bilanziell schliessen (Bilanzsumme immer ausgeglichen).
5. **Sanierungsbezug?** Jede tragende Planverbesserung muss auf Ursache, Maßnahme, Timing und Beleg zurückgeführt werden.

