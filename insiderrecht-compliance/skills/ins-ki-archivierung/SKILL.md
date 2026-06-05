---
name: ins-ki-archivierung
description: "Ins 053 Ki Prognosemodell, Ins 054 Archivierung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 053 Ki Prognosemodell, Ins 054 Archivierung

## Arbeitsbereich

Dieser Skill bündelt **Ins 053 Ki Prognosemodell, Ins 054 Archivierung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-053-ki-prognosemodell` | Prueft Insiderrecht-Risiken beim Einsatz von KI-Prognosemodellen: Informationsasymmetrie, Modell-Output als Insiderinformation und Compliance-Anforderungen. |
| `ins-054-archivierung` | Sichert MAR-konforme Archivierung aller Insiderrecht-Compliance-Dokumente: Fristen, Formate, Zugriffssicherung und Loeschkonzept. |

## Arbeitsweg

Für **Ins 053 Ki Prognosemodell, Ins 054 Archivierung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-053-ki-prognosemodell`

**Fokus:** Prueft Insiderrecht-Risiken beim Einsatz von KI-Prognosemodellen: Informationsasymmetrie, Modell-Output als Insiderinformation und Compliance-Anforderungen.

# KI-Prognosemodelle und Insiderrecht

## Rechtlicher Rahmen

Der Einsatz von KI-Modellen (maschinelles Lernen, LLMs, Forecasting-Modelle) zur Prognose
von Unternehmensergebnissen, Marktentwicklungen oder zur Entdeckung von Insiderinformationen
ist insiderrechtlich nicht explizit geregelt. MAR Art. 7 gilt unabhängig davon, wie die
Information gewonnen wurde. Wenn ein KI-Modell auf Basis nicht-öffentlicher Eingangsdaten
eine kursrelevante Prognose generiert, kann der Modell-Output eine Insiderinformation sein.

Rechtsgrundlagen:
- Art. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-628/13 (Lafonta): https://curia.europa.eu/juris/document/document.jsf?docid=162388
- KI-Verordnung (EU) 2024/1689 (AI Act): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt, unter welchen Umständen KI-generierte Prognosen oder Analysen
Insiderinformationen darstellen und wie der Zugang zu solchen Modellen kontrolliert werden muss.

## Arbeitsprogramm

### Schritt 1 – KI-Modell-Input-Analyse

- Welche Daten werden in das Modell eingespeist?
 - Ausschließlich öffentliche Daten: Kein Insiderrecht-Problem beim Output
 - Nicht-öffentliche Unternehmensdaten (interne Finanzdaten, Vertriebsdaten, Produktionsdaten):
 Modell-Output kann Insiderinformation sein

### Schritt 2 – Modell-Output als Insiderinformation

- Generiert das Modell eine Prognose, die erheblich von der veröffentlichten Guidance oder
 dem Analystenkonsensus abweicht?
- Ist der Modell-Output hinreichend präzise? (nicht nur Wahrscheinlichkeiten, sondern
 konkrete Zahlenwerte)
- Würde ein verständiger Anleger diesen Output bei seiner Investitionsentscheidung nutzen?
 Wenn ja → Modell-Output ist Insiderinformation

### Schritt 3 – Zugangskontrollen

- Wer hat Zugang zu dem KI-Modell und seinen Outputs?
- Alle Zugangspersonen sind potenzielle Insider → Insiderliste, Handelsverbot
- Chinese Walls: Handelsabteilung darf keinen Zugang zu internen Forecasting-Modellen haben

### Schritt 4 – Modell-Governance und Dokumentation

- AI-Act-Anforderungen für Hochrisiko-KI: Falls das Modell für Investitions- oder
 Finanzentscheidungen eingesetzt wird, können AI Act Art. 9 ff. gelten
- Modell-Dokumentation: Input-Daten, Algorithmus-Beschreibung, Output-Interpretation
- Audit-Trail: Wer hat wann welche Prognosen aus dem Modell abgerufen?

### Schritt 5 – Compliance-Empfehlungen

- Trennung: Internes Forecasting-System (Insiderinformation) vs. extern veröffentlichte Prognose
- Ad-hoc-Pflicht: Wenn Modell-Output wesentliche Abweichung von Guidance signalisiert →
 Prüfung ob Profit-Warning-Ad-hoc erforderlich
- Schulung der Modell-Nutzer auf Insiderrecht

## Red-Team-Fragen

- Verarbeitet das Modell nicht-öffentliche Daten, die zu einer Insiderinformation führen?
- Haben alle Modell-Nutzer eine Insiderrecht-Schulung erhalten?
- Gibt es Chinese Walls zwischen Modell-Zugang und Handelsabteilung?
- Wird der Modell-Output auf Ad-hoc-Relevanz geprüft?
- Sind AI-Act-Anforderungen bekannt und berücksichtigt?

## Ausgabeformat

Erzeuge:
1. KI-Modell-Risikobewertung (Input × Output × Insiderinformationsrisiko)
2. Zugangskontrollen-Matrix (Nutzergruppe × Zugangsberechtigung × Insiderstatus)
3. Modell-Governance-Dokumentationsvorlage
4. Schulungsmodul: „KI-Prognosen und Insiderrecht"

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, dejure.org.

## 2. `ins-054-archivierung`

**Fokus:** Sichert MAR-konforme Archivierung aller Insiderrecht-Compliance-Dokumente: Fristen, Formate, Zugriffssicherung und Loeschkonzept.

# Archivierung – MAR-konforme Aufbewahrung

## Rechtlicher Rahmen

Art. 18 Abs. 5 MAR schreibt eine Aufbewahrungsfrist von mindestens 5 Jahren für Insiderlisten
vor. Weitere Compliance-Dokumente (Ad-hoc-Mitteilungen, Aufschubakten, Directors'-Dealings-
Meldungen, Market-Sounding-Protokolle) unterliegen ebenfalls Aufbewahrungspflichten aus MAR,
WpHG und allgemeinen handelsrechtlichen Vorschriften. Unveränderbarkeit und Zugriffssicherung
sind Pflicht.

Rechtsgrundlagen:
- Art. 18 Abs. 5 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 257 HGB (Aufbewahrungsfristen): https://www.gesetze-im-internet.de/hgb/__257.html
- § 147 AO (Aufbewahrungspflichten): https://www.gesetze-im-internet.de/ao_1977/__147.html
- DSGVO Art. 5 (Datenminimierung): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill erstellt ein vollständiges Archivierungskonzept für alle insiderrechtlich
relevanten Dokumente, das Aufbewahrungsfristen, Formate, Zugriffssicherung und
DSGVO-konformes Löschkonzept umfasst.

## Arbeitsprogramm

### Schritt 1 – Dokumentenkatalog

Folgende Dokumente sind aufzubewahren (Mindestfristen):
- Insiderlisten (Art. 18 MAR): 5 Jahre nach letztem Eintrag
- Aufschubakten (Art. 17 MAR): 5 Jahre
- Ad-hoc-Mitteilungen: 5 Jahre (Art. 4 DVO 2016/1055)
- Market-Sounding-Protokolle (Art. 11 MAR, DVO 2016/960): 5 Jahre
- Directors'-Dealings-Meldungen (Art. 19 MAR): 5 Jahre
- Pre-Clearance-Entscheidungen: 5 Jahre
- Schulungsnachweise: 5 Jahre
- Compliance-Dossiers für BaFin-Anfragen: 5 Jahre

### Schritt 2 – Aufbewahrungsformat

- Elektronische Archivierung bevorzugt (revisionssicher, unveränderbar)
- Anforderungen: Zeitstempelzertifizierung, Versionierung, keine nachträgliche Änderung
- Akzeptierte Formate: PDF/A für Dokumente, XLSX/CSV für Listen
- Backup: Off-Site-Backup mindestens monatlich, inkl. Wiederherstellungstest

### Schritt 3 – Zugriffssicherung

- Zugriff auf Compliance-Archiv: Nur Compliance-Officer, CFO, General Counsel
- Kein Zugriff für Handelsabteilungen oder IR-Teams
- Protokollierung aller Zugriffe (Audit Trail)
- Bei BaFin-Anfrage: Zugriff durch externe Kanzlei auf definierten Umfang

### Schritt 4 – DSGVO-Konformität

- Insiderlisten enthalten personenbezogene Daten (Art. 18 MAR: Name, Adresse, Geburtsdatum)
- Aufbewahrung auf der Basis von Art. 6 Abs. 1 lit. c DSGVO (rechtliche Verpflichtung)
- Löschung nach Ablauf der Aufbewahrungsfrist (automatisiertes Löschkonzept)
- Keine Zweckentfremdung der Insiderlisten-Daten

### Schritt 5 – Löschkonzept

- Automatisches Lösch-Flag: 5 Jahre + 1 Monat nach letztem Eintrag
- Löschbestätigung dokumentieren
- Ausnahme: Laufende BaFin-Ermittlung oder gerichtliches Verfahren → Einfrierung der Löschung

## Red-Team-Fragen

- Sind alle im Dokumentenkatalog genannten Dokument-Typen vollständig archiviert?
- Ist die Archivierung revisionssicher (kein nachträgliches Überschreiben möglich)?
- Ist der Zugriff auf Compliance-Archiv ausreichend beschränkt?
- Werden Aufbewahrungsfristen systemgestützt überwacht?
- Ist das Löschkonzept DSGVO-konform und mit laufenden Ermittlungen koordiniert?

## Ausgabeformat

Erzeuge:
1. Dokumentenkatalog mit Aufbewahrungsfristen und Format-Anforderungen
2. Archivierungssystem-Anforderungsprofil (für IT-Ausschreibung oder System-Check)
3. DSGVO-Löschkonzept-Vorlage
4. BaFin-Anfragen-Bereitstellungsprotokoll

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.
