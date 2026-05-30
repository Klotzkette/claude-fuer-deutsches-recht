# Aktenstück 05 — Risikominderungsmaßnahmen nach Art. 35 DSA

**Az. Kanzlei:** KRS-2026-0318-DSA
**Bearbeitung:** RA Felix Wendland, RAin Dr. Philippa Groth-Steinberg
**Stand:** 26. März 2026

---

## 1. Normgrundlage

Art. 35 DSA verpflichtet Anbieter von VLOPs, angemessene, verhältnismäßige und wirksame Risikominderungsmaßnahmen zu ergreifen, die auf die in der Risikobewertung nach Art. 34 DSA festgestellten systemischen Risiken zugeschnitten sind. Art. 35 Abs. 1 DSA listet dabei einen nichtabschließenden Katalog möglicher Maßnahmen auf.

---

## 2. Maßnahmenkatalog für Halmweise.de

### 2.1 Maßnahmen gegen Hassrede und illegale Inhalte (Art. 35 Abs. 1 lit. a, k)

**Priorität 1 — Notice-and-Action-Reform**

Die Bundesnetzagentur hat als DSC die verspätete Bearbeitung von Notice-and-Action-Meldungen (Art. 16 DSA) bei Hassrede beanstandet. Folgende Maßnahmen sind erforderlich:

- Einführung eines SLA (Service Level Agreement) für die Bearbeitung von Meldungen: Hassrede-Meldungen müssen innerhalb von 24 Stunden (Hochrisiko) bzw. 72 Stunden (Standardrisiko) bearbeitet werden.
- Erweiterung des Trust & Safety Teams um mindestens 30 Vollzeitstellen.
- KI-gestützte Vorab-Klassifikation von gemeldeten Inhalten zur Priorisierung.
- Einrichtung einer dedizierten Eskalationsschiene für Trusted Flagger nach Art. 22 DSA.

**Erwartete Wirkung:** Signifikante Reduzierung der Bearbeitungszeit; Erfüllung der Anforderungen des Art. 16 Abs. 6 DSA (Bearbeitungspflicht ohne unnötige Verzögerung).

---

### 2.2 Maßnahmen zur Algorithmus-Transparenz (Art. 35 Abs. 1 lit. d)

**Priorität 1 — Non-Profiling-Option HalmRank**

Art. 27 Abs. 1 lit. b DSA verlangt, dass VLOPs mindestens eine nicht auf Profiling basierende Empfehlungsoption anbieten. Diese fehlte bei Halmweise.de und ist Gegenstand der BNetzA-Mahnung.

Maßnahmenplan:
- Technische Implementierung der chronologischen Timeline als Standardalternative bis 15.06.2026.
- Nutzeroberfläche: Klar sichtbare Umschaltmöglichkeit in den Einstellungen.
- Dokumentation des Algorithmus-Grundprinzips nach Art. 27 Abs. 1 DSA im Transparenzbereich.
- A/B-Test zur Nutzungsrate der Non-Profiling-Option; Ergebnisse in den Transparenzbericht aufnehmen.

---

### 2.3 Maßnahmen zum Werbetransparenz-Repository (Art. 35 Abs. 1 lit. j, Art. 39 DSA)

**Priorität 2 — Repository-Vervollständigung**

Das Werbeanzeigen-Repository nach Art. 39 DSA muss sämtliche Werbeanzeigen der vergangenen 12 Monate dokumentieren. Bislang sind Lücken im Zeitraum Januar bis September 2025 bekannt.

Maßnahmenplan:
- Technische Rückfüllung des Repositories für Januar bis September 2025 bis 30.04.2026.
- Implementierung automatisierter Datenpipeline zur laufenden Repository-Befüllung.
- Öffentliche Zugänglichkeit des Repositories nach Art. 39 Abs. 2 DSA herstellen.

---

### 2.4 Maßnahmen zum Minderjährigenschutz (Art. 35 Abs. 1 lit. f)

**Priorität 2 — Altersverifikationskonzept**

- Softgate-Mechanismus: Pflichtangabe des Geburtsdatums bei Neuregistrierung mit Plausibilitätsprüfung.
- Inhaltsfilterung: Automatische Kennzeichnung und altersbasierte Sperrung von Inhalten zu Extremdiäten und Selbstverletzung.
- Eltern-Benachrichtigungssystem für Nutzer unter 16 Jahren (optional, datenschutzkonform).

---

### 2.5 Maßnahmen zur Krisenprävention (Art. 35 Abs. 1 lit. i, Art. 36 DSA)

- Einrichtung eines internen Crisis Response Teams (CRT) aus Trust & Safety, Legal und PR.
- Protokoll für koordinierte inauthentic behavior (CIB): Automatisierte Erkennung und Meldung an Strafverfolgungsbehörden.
- Jährliche Krisenübungen mit dem BNetzA-DSC.

---

## 3. Zeitplan Maßnahmenumsetzung

| Maßnahme | Verantwortlich | Frist |
|---|---|---|
| SLA Notice-and-Action einführen | Trust & Safety, Legal | 15.05.2026 |
| 30 Trust & Safety Stellen ausschreiben | HR, Dr. Erbakan | 01.05.2026 |
| KI-Klassifikation Hassrede | Tech/CTO Schröder | 15.06.2026 |
| Non-Profiling-Option HalmRank | Tech/CTO Schröder | 15.06.2026 |
| Repository Rückfüllung 2025 | Tech, Legal | 30.04.2026 |
| Altersverifikation Konzept | Legal, DPO | 30.05.2026 |
| Crisis Response Team einrichten | Management | 01.06.2026 |
| Gesamtdokumentation Risikominderung | Legal | 01.07.2026 |

---

## 4. Verhältnismäßigkeit

Art. 35 Abs. 1 DSA fordert "angemessene und verhältnismäßige" Maßnahmen. Angesichts von 51 Mio. EU-Nutzern und einem Jahresumsatz von ca. 520 Mio. EUR sind die vorgesehenen Maßnahmen mit einem geschätzten Investitionsvolumen von ca. 8-12 Mio. EUR (inkl. Personalaufbau) verhältnismäßig.

Ausführlicher Risikoreduktionsplan: vgl. DOCX `docx/risikoreduktionsplan_halmweise_art35.docx`

---

## 5. Rechtsgrundlagen

- Art. 35 DSA (EU) 2022/2065 — Risikominderungsmaßnahmen
- Art. 16 DSA — Notice-and-Action
- Art. 27 DSA — Empfehlungssysteme
- Art. 39 DSA — Werbetransparenz

**Quellen:**
- Verordnung (EU) 2022/2065 (DSA), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2065

---

*Bearbeitung: RA Felix Wendland, RAin Dr. Philippa Groth-Steinberg*
*Stand: 26. März 2026*
