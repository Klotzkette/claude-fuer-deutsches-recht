# Aktenstück 04 — Systemische Risikobewertung nach Art. 34 DSA: Prüfraster Halmweise.de

**Az. Kanzlei:** KRS-2026-0318-DSA
**Bearbeitung:** RA Felix Wendland
**Stand:** 24. März 2026

---

## 1. Normgrundlage und Zweck

Art. 34 DSA verpflichtet Anbieter von VLOPs, mindestens einmal jährlich eine gründliche Analyse der systemischen Risiken durchzuführen, die von ihrer Plattform ausgehen oder ermöglicht werden. Maßgeblich sind dabei die spezifischen Systeme und Tätigkeiten der Plattform, einschließlich algorithmischer Systeme, Werbesysteme und datenintensiver Prozesse.

Die Risikobewertung ist Voraussetzung für die Risikominderungsmaßnahmen nach Art. 35 DSA und Grundlage des externen Audits nach Art. 37 DSA.

---

## 2. Risikokategorien nach Art. 34 Abs. 1 DSA

Art. 34 Abs. 1 DSA nennt vier Risikokategorien, die zu bewerten sind:

| Nr. | Risikokategorie (Art. 34 Abs. 1 DSA) | Beispiele |
|---|---|---|
| a) | Verbreitung illegaler Inhalte | Hassrede, CSAM, Terrorpropaganda |
| b) | Negative Auswirkungen auf Grundrechte | Meinungsfreiheit, Nichtdiskriminierung, Privatsphäre |
| c) | Beeinträchtigung bürgerlicher Diskurse und demokratischer Prozesse | Desinformation, Manipulation |
| d) | Negative Auswirkungen im Zusammenhang mit geschlechtsbezogener Gewalt, Schutz Minderjähriger, Gesundheit und psychisches Wohlbefinden | Cybermobbing, Essstörungen, Suizidpropaganda |

---

## 3. Prüfraster für Halmweise.de

### 3.1 Risikobewertung Hassrede (Art. 34 Abs. 1 lit. a)

**Ausgangslage:** Halmweise.de ist eine Community-orientierte Plattform. Nutzer können Beiträge erstellen, kommentieren und teilen. Inhalte zu Klimapolitik, Stadtentwicklung und Lebensstildebatten ziehen politisch aufgeladene Diskussionen an.

**Risikofaktoren:**
- Algorithmisches Boosting von Engagement-starken Inhalten (auch bei polarisierendem Ton)
- Pseudonyme Nutzung ermöglicht niedrigschwellige Hassrede
- Notice-and-Action-Verfahren war lt. BNetzA-Mahnung zu langsam

**Risikobewertung:** MITTEL-HOCH. Notice-and-Action-Defizit bestätigt strukturelles Risiko.

**Maßnahmenerfordernis:** Workflow-Optimierung (vgl. Aktenstück 08), KI-gestützte Vorab-Moderation für Hochrisiko-Inhalte.

---

### 3.2 Risikobewertung Empfehlungsalgorithmus (Art. 34 Abs. 1 lit. b, lit. c)

**Ausgangslage:** Halmweise.de verwendet einen personalisierten Empfehlungsalgorithmus (intern: "HalmRank"), der Inhalte auf Basis von Nutzerinteraktionen, Verweildauer und Community-Signalen priorisiert. Eine Option zur Nutzung ohne Profiling war zum Zeitpunkt der BNetzA-Mahnung nicht vorhanden.

**Risikofaktoren:**
- Fehlende Non-Profiling-Option verstößt gegen Art. 27 Abs. 1 lit. b DSA
- Filterblasen-Effekte können demokratische Debatte verzerren
- Potenzielle Verstärkung von Extrempositionen

**Risikobewertung:** HOCH (aufgrund aktiven BNetzA-Verfahrens).

**Maßnahmenerfordernis:** Implementierung der Non-Profiling-Option bis 14.07.2026, Algorithmus-Transparenz nach Art. 27 DSA.

---

### 3.3 Risikobewertung Werbeanzeigen (Art. 34 Abs. 1 lit. b)

**Ausgangslage:** Halmweise.de schaltet gezielte Werbung auf Basis demographischer und verhaltensbezogener Nutzerdaten. Das Werbeanzeigen-Repository nach Art. 39 DSA ist nach Mandantenangaben unvollständig befüllt.

**Risikofaktoren:**
- Targeting auf Basis sensitiver Kategorien (Ernährung, politische Meinungen) möglich
- Unvollständiges Repository verhindert externe Überprüfbarkeit
- Potenzielle Manipulation durch zielgerichtete politische Werbung

**Risikobewertung:** MITTEL. Kein Hinweis auf systemisches Fehlverhalten, aber strukturelles Compliance-Defizit.

**Maßnahmenerfordernis:** Repository-Vervollständigung bis 30.04.2026.

---

### 3.4 Risikobewertung Minderjährigenschutz (Art. 34 Abs. 1 lit. d)

**Ausgangslage:** Halmweise.de erlaubt Nutzung ab 16 Jahren (Allgemeine Nutzungsbedingungen). Keine spezifischen Altersverifikationsmechanismen vorhanden. Nutzerberichte über Minderjährige unter 16 Jahren auf der Plattform liegen vor.

**Risikofaktoren:**
- Fehlendes Altersgatekeeping
- Exposition von Minderjährigen gegenüber Inhalten zu Ernährungsideologien (Fasten-Communities)
- Auswirkungen auf psychisches Wohlbefinden

**Risikobewertung:** MITTEL. Keine akuten Krisenfälle bekannt, aber latentes Risiko.

**Maßnahmenerfordernis:** Altersverifikationskonzept erarbeiten, Inhaltsfilter für Hochrisiko-Kategorien.

---

## 4. Gesamtrisikomatrix

| Risikokategorie | Eintrittswahrscheinlichkeit | Schwere | Gesamtbewertung | Priorität |
|---|---|---|---|---|
| Hassrede / Art. 34 Abs. 1 lit. a | Hoch | Mittel | Mittel-Hoch | 1 |
| Empfehlungsalgorithmus | Mittel | Hoch | Hoch | 1 |
| Werbetargeting | Mittel | Mittel | Mittel | 2 |
| Minderjährigenschutz | Niedrig | Hoch | Mittel | 2 |
| Desinformation | Niedrig | Mittel | Niedrig-Mittel | 3 |

Ausführliche XLSX-Version: siehe `xlsx/risikomatrix_dsa_art34_halmweise.xlsx`

---

## 5. Dokumentation und Aufbewahrung

Art. 34 Abs. 2 DSA verlangt, dass die Risikobewertung dokumentiert und aufbewahrt wird. Sie ist dem DSC auf Anfrage vorzulegen sowie dem externen Auditor nach Art. 37 DSA zur Verfügung zu stellen. Die Erstdokumentation ist bis 14.07.2026 zu erstellen.

---

## 6. Rechtsgrundlagen

- Art. 34 DSA (EU) 2022/2065 — Systemische Risikobewertung
- Art. 27 DSA — Transparenz von Empfehlungssystemen
- Art. 39 DSA — Werbetransparenz

**Quellen:**
- Verordnung (EU) 2022/2065 (DSA), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2065

---

*Bearbeitung: RA Felix Wendland*
*Stand: 24. März 2026*
