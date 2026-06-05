---
name: ins-esg-lieferkettenereignis
description: "Ins 051 Esg Schock, Ins 052 Lieferkettenereignis: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 051 Esg Schock, Ins 052 Lieferkettenereignis

## Arbeitsbereich

Dieser Skill bündelt **Ins 051 Esg Schock, Ins 052 Lieferkettenereignis** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-051-esg-schock` | Prueft Insiderinformations-Qualitaet und Ad-hoc-Pflicht bei ESG-Schockereignissen (Umweltvorfaelle, Governance-Skandale, Social-Misstaende). |
| `ins-052-lieferkettenereignis` | Prueft Insiderinformations-Qualitaet und Ad-hoc-Pflicht bei wesentlichen Lieferkettenereignissen (Lieferantenausfall, Rohstoffengpass, Geopolitik). |

## Arbeitsweg

Für **Ins 051 Esg Schock, Ins 052 Lieferkettenereignis** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-051-esg-schock`

**Fokus:** Prueft Insiderinformations-Qualitaet und Ad-hoc-Pflicht bei ESG-Schockereignissen (Umweltvorfaelle, Governance-Skandale, Social-Misstaende).

# ESG-Schockereignis – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

ESG-relevante Ereignisse (Umweltkatastrophen, Governance-Skandale, Menschenrechtsverletzungen,
Greenwashing-Vorwürfe) können Insiderinformationen nach Art. 7 MAR darstellen, wenn sie
kursrelevant sind. Die Kursrelevanz von ESG-Informationen ist durch zunehmenden ESG-Fokus
institutioneller Anleger und durch CSRD-Berichtspflichten gestiegen. MAR enthält keine
ESG-spezifischen Ausnahmen.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- CSRD-Richtlinie (EU) 2022/2464: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464
- SFDR (EU) 2019/2088: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019R2088
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob ein ESG-Schockereignis eine Insiderinformation darstellt, und steuert
die Ad-hoc-Entscheidung sowie die Koordination mit Nachhaltigkeits- und Kommunikationsabteilung.

## Arbeitsprogramm

### Schritt 1 – ESG-Ereignis-Klassifizierung

- Environmental: Umweltunfall, Chemikalien-Austritt, CO₂-Bilanzskandale, Greenwashing-
 Ermittlung, Verlust von Umweltzertifizierungen
- Social: Arbeitnehmerrechtsverletzungen, Lieferkettenskandale, Diskriminierungsvorwürfe,
 schwere Arbeitsunfälle
- Governance: Korruptionsvorwürfe, Vorstandsabgang aus ethischen Gründen, Aufsichtsrats-
 Interessenkonflikte, Whistleblower-Berichte über Fehlverhalten

### Schritt 2 – Kursrelevanz-Beurteilung

- Institutionelle Anleger: Viele haben ESG-Ausschlusslisten → ESG-Ereignis kann zur Erzwungenen
 Abgabe von Anteilen durch ESG-Fonds führen
- Regulatorisch: Drohende Bußgelder (CSRD-Verletzungen, Lieferkettensorgfaltspflichtengesetz)
- Reputationsschaden: Quantifizierung schwierig, aber kursrelevant bei breiter
 Medienberichterstattung
- Vergleich mit Marktreaktionen auf ähnliche ESG-Ereignisse in der Branche

### Schritt 3 – Insiderinformations-Zeitpunkt

- Wann war das ESG-Ereignis intern bekannt?
- Interne Reports, HSE-Berichte, Sustainability-Team-Berichte als frühestmögliche Zeitpunkte
- Dokumentiere den Informationsfluss im Unternehmen

### Schritt 4 – Koordination Ad-hoc und Nachhaltigkeitskommunikation

- Ad-hoc und Nachhaltigkeitskommunikation müssen inhaltlich konsistent sein
- Keine Minimierung in der Ad-hoc, die durch NGO- oder Medienberichte widerlegt wird
- CSRD-Berichtspflichten: Parallele Dokumentation für Nachhaltigkeitsbericht

### Schritt 5 – Eigengeschäfts-Prüfung

- PDMRs, die vom ESG-Ereignis wissen: Handelsverbot
- Sustainability-Manager: Falls sie Zugang zu kursrelevanten ESG-Informationen haben,
 müssen sie auf der Insiderliste stehen

## Red-Team-Fragen

- Wurde die Kursrelevanz des ESG-Ereignisses explizit begründet (nicht abgetan)?
- Wurde der frühestmögliche Zeitpunkt des Insiderwissens identifiziert (inkl. HSE-Reports)?
- Sind ESG-Experten des Unternehmens auf Insiderlisten erfasst?
- Ist die Ad-hoc mit der Nachhaltigkeitskommunikation koordiniert?

## Ausgabeformat

Erzeuge:
1. ESG-Ereignis-Kursrelevanz-Matrix (Event-Typ × Anleger-Reaktion × Regulatorische Folge)
2. Insiderinformations-Zeitstrahl (interne Kenntnis → Ad-hoc)
3. Ad-hoc-Entwurf ESG-Schockereignis
4. Koordinationsplan: Ad-hoc × CSRD × Pressemitteilung

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-052-lieferkettenereignis`

**Fokus:** Prueft Insiderinformations-Qualitaet und Ad-hoc-Pflicht bei wesentlichen Lieferkettenereignissen (Lieferantenausfall, Rohstoffengpass, Geopolitik).

# Lieferkettenereignis – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Ein wesentlicher Lieferantenausfall, ein gravierender Rohstoffengpass oder ein geopolitisches
Ereignis, das die Lieferkette des Emittenten erheblich beeinträchtigt, kann eine kursrelevante
Insiderinformation sein. Die Kursrelevanz hängt vom Grad der Beeinträchtigung und der
Fähigkeit des Emittenten ab, Auswirkungen zu kompensieren.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-628/13 (Lafonta, Kursrichtung): https://curia.europa.eu/juris/document/document.jsf?docid=162388
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob ein Lieferkettenereignis eine Insiderinformation darstellt, bestimmt
den Entstehungszeitpunkt und koordiniert die Ad-hoc-Entscheidung mit dem Krisenmanagement.

## Arbeitsprogramm

### Schritt 1 – Lieferkettenereignis bewerten

- Art des Ereignisses: Lieferanteninsolvenz, Naturkatastrophe, Geopolitik (Embargo, Krieg),
 Qualitätsproblem, Transportunterbrechung
- Betroffene Waren: Wie kritisch sind die betroffenen Materialien / Komponenten?
- Substitute: Gibt es kurzfristig verfügbare Alternativen?
- Zeitlicher Horizont: Kurze Unterbrechung (< 4 Wochen) vs. struktureller Ausfall

### Schritt 2 – Kursrelevanz-Beurteilung

- Finanzielle Modellierung: Auswirkungen auf Umsatz, Marge, Lagerhaltung
- Vergleich mit Prognose: Wird die aktuelle Guidance noch haltbar sein?
- Abweichung vom Analystenkonsensus
- Lafonta-Test: Kursrichtung muss nicht vorhersagbar sein; verständiger Anleger würde die
 Information dennoch berücksichtigen

### Schritt 3 – Insiderinformations-Zeitpunkt

- Wann wurde die Beeinträchtigung intern erstmals als wesentlich eingeschätzt?
- Interne Alerts (Supply-Chain-Management-System), Lieferanten-Meldungen
- Frühestmöglicher Zeitpunkt: Erste konservative Schadensprognose, nicht erst beim
 vollständigen Überblick

### Schritt 4 – Aufschub-Prüfung

- Laufende Verhandlungen mit Alternativlieferanten: Legitimes Interesse möglich
- Aber: Wenn Lieferkettenproblem zu Prognoseabweichung führt → kein Aufschub mehr zulässig
 (keine laufenden Verhandlungen über das Kernproblem)

### Schritt 5 – Koordination mit Krisenmanagement

- Compliance und Krisenmanagement-Team gleichzeitig informieren
- Kommunikationsfreiheit: Nach Ad-hoc können Details mit Journalisten und Analysten
 besprochen werden
- LkSG-Meldepflichten: Parallel prüfen (Lieferkettensorgfaltspflichtengesetz)

## Red-Team-Fragen

- Wurde der frühestmögliche Zeitpunkt der Insiderinformation identifiziert?
- Wurde die finanzielle Wesentlichkeit modelliert (nicht nur qualitativ)?
- Wurde der Lafonta-Test korrekt angewendet (keine Pflicht zur Kursrichtungsangabe)?
- Werden LkSG-Meldepflichten parallel zur MAR-Compliance geprüft?

## Ausgabeformat

Erzeuge:
1. Lieferkettenereignis-Kursrelevanz-Matrix
2. Finanzielle Auswirkungsmodellierung (Umsatz × Marge × Prognose)
3. Insiderinformations-Zeitstrahl
4. Ad-hoc-Entwurf Lieferkettenstörung

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, dejure.org.

## Weitere Hinweise

Das LkSG (Lieferkettensorgfaltspflichtengesetz) verpflichtet große Unternehmen zu Risikoanalysen
und Präventionsmaßnahmen in der Lieferkette. Ein durch das LkSG ausgelöstes Audit oder eine
festgestellte Verletzung kann selbst eine kursrelevante Information sein (Bußgeldrisiko,
Reputationsschaden). Compliance muss LkSG-Monitoring und MAR-Compliance-Prozesse systematisch
verknüpfen, damit LkSG-Feststellungen automatisch auf Insiderinformations-Qualität geprüft werden.

Weitere Quellen:
- LkSG: https://www.gesetze-im-internet.de/lksg/
- Art. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
