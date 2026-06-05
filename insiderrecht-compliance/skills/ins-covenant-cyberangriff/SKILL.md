---
name: ins-covenant-cyberangriff
description: "Ins 024 Covenant Breach, Ins 025 Cyberangriff: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 024 Covenant Breach, Ins 025 Cyberangriff

## Arbeitsbereich

Dieser Skill bündelt **Ins 024 Covenant Breach, Ins 025 Cyberangriff** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-024-covenant-breach` | Prueft Ad-hoc-Pflicht und Insiderrecht bei Covenant-Verletzungen in Kreditvertraegen: Wesentlichkeit, Kursrelevanz, Aufschub und Glaeubiger-Kommunikation. |
| `ins-025-cyberangriff` | Prueft Insiderinformations-Qualitaet eines Cyberangriffs: Kursrelevanz, Ad-hoc-Pflicht, Aufschub wegen laufender Strafverfolgung und Koordination mit IT-Forensik. |

## Arbeitsweg

Für **Ins 024 Covenant Breach, Ins 025 Cyberangriff** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-024-covenant-breach`

**Fokus:** Prueft Ad-hoc-Pflicht und Insiderrecht bei Covenant-Verletzungen in Kreditvertraegen: Wesentlichkeit, Kursrelevanz, Aufschub und Glaeubiger-Kommunikation.

# Covenant Breach – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Eine Verletzung von Kreditvertragsklauseln (Financial Covenants, Cross-Default, Change-of-
Control) kann eine Insiderinformation nach Art. 7 MAR begründen, wenn sie kursrelevant ist.
Kursrelevanz hängt von der Wesentlichkeit der Verletzung ab: Drohende Kündigung, Fälligkeit
oder Restrukturierungsbedarf sind regelmäßig kursrelevant.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 97 WpHG: https://www.gesetze-im-internet.de/wphg/__97.html
- BaFin-Emittentenleitfaden Kap. VI.2: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft, ob eine Covenant-Verletzung eine Insiderinformation und Ad-hoc-Pflicht
auslöst, und entwickelt die Compliance-Strategie für Emittent und Kreditgeber.

## Arbeitsprogramm

### Schritt 1 – Art und Wesentlichkeit der Verletzung

- Welcher Covenant wurde verletzt? (z. B. Leverage Ratio, DSCR, ICR)
- Ist die Verletzung manifest oder nur drohend?
- Welche Rechtsfolge sieht der Kreditvertrag vor? (Kündigung, Cure-Period, Waiver)
- Ist die Verletzung reversibel (Einmaltransaktion, saisonaler Effekt) oder strukturell?

### Schritt 2 – Insiderinformations-Prüfung

- Kursrelevanz: Würde ein verständiger Anleger die Covenant-Verletzung bei der
 Investitionsentscheidung berücksichtigen?
- Hohe Kursrelevanz-Indikation bei: drohender Kreditkündigung, Cross-Default,
 Restrukturierungsbedarf, Liquiditätsgefährdung
- Niedrige Kursrelevanz: Technische Verletzung ohne materielle Konsequenz, bereits
 laufende Waiver-Verhandlungen mit sehr hoher Erfolgswahrscheinlichkeit

### Schritt 3 – Aufschub nach Art. 17 Abs. 4 MAR

- Mögliches legitimes Interesse: Laufende Waiver-Verhandlungen mit Kreditgebern
- Voraussetzung: Waiver-Verhandlungen sind fortgeschritten und Abschluss wird
 mit hinreichender Wahrscheinlichkeit erwartet
- Vertraulichkeit: Kreditgeber unter NDA, Informationskreis begrenzt
- Trigger: Scheitern der Verhandlungen → Sofortveröffentlichung

### Schritt 4 – Kreditgeber-Kommunikation

- Information an Kreditgeber ist reguläre Geschäftskommunikation (Art. 10 Abs. 1 MAR)
- Kreditgeber werden Sekundärinsider: Müssen auf Handelsverbote hingewiesen werden
- Kreditgeber sind in Insiderliste aufzunehmen, wenn sie Insiderinformationen erhalten

### Schritt 5 – Ad-hoc und Sanierungsankündigung

- Nach Entscheid: Ad-hoc-Mitteilung zu Covenant-Verletzung und Maßnahmen
- Inhalt: Art der Verletzung, Zeitpunkt, ergriffene Maßnahmen, Ausblick
- Koordination mit Sanierungsankündigung (falls zutreffend)

## Red-Team-Fragen

- Wurde die Kursrelevanz der Covenant-Verletzung unvoreingenommen beurteilt?
- Erfüllen Waiver-Verhandlungen die Aufschub-Voraussetzungen?
- Wurden Kreditgeber als Sekundärinsider behandelt und belehrt?
- Ist der Aufschub mit einer widerspruchsfreien öffentlichen Kommunikation vereinbar?
- Wurde ein Trigger für den Aufschub-Ende definiert?

## Ausgabeformat

Erzeuge:
1. Insiderinformations-Prüfprotokoll Covenant Breach
2. Aufschub-Prüfmatrix (legitimes Interesse × Widerspruchsfreiheit × Vertraulichkeit)
3. Kreditgeber-Belehrungsschreiben (Insiderstatus)
4. Ad-hoc-Entwurf (Covenant Breach)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Bei syndizierten Krediten ist die Koordination mit allen Banken der Kreditgebergruppe
besonders wichtig: Werden alle Kreditgeber gleichzeitig und auf demselben Informationsstand
gehalten? Unterschiedliche Informationsstände innerhalb des Kreditsyndikats können zu
ungleichem Insider-Status der Bankvertreter führen und das Koordinationsrisiko erhöhen.
Die Insiderliste muss alle informierten Bankvertreter namentlich erfassen.

Weitere Quellen:
- Art. 18 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## 2. `ins-025-cyberangriff`

**Fokus:** Prueft Insiderinformations-Qualitaet eines Cyberangriffs: Kursrelevanz, Ad-hoc-Pflicht, Aufschub wegen laufender Strafverfolgung und Koordination mit IT-Forensik.

# Cyberangriff – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Ein wesentlicher Cyberangriff auf einen börsennotierten Emittenten kann eine Insiderinformation
nach Art. 7 MAR darstellen. Kursrelevanz ist anzunehmen bei: erheblichem Datenverlust,
Betriebsunterbrechung, Reputationsschaden, Haftungsrisiken oder regulatorischen Konsequenzen.
NIS-2-Richtlinie (Umsetzungsfrist 2024) schafft zusätzliche Meldepflichten, die parallel zu
MAR bestehen.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- NIS-2-Richtlinie (EU) 2022/2555: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2555
- DSGVO Art. 33 (Datenschutzverletzung): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill prüft die Insiderinformations-Qualität eines Cyberangriffs, entwickelt die
Ad-hoc-Strategie und koordiniert die parallelen Meldepflichten (MAR, DSGVO, NIS-2).

## Arbeitsprogramm

### Schritt 1 – Initialerkennung und Schadensbewertung

- Zeitpunkt: Wann war dem Emittenten der Angriff bekannt?
- Art: Datenverlust, Ransomware, Systemaufall, Datenleck, IP-Diebstahl?
- Umfang: Betroffene Systeme, betroffene Daten (Kundendaten, Finanzdaten, Geschäftsgeheimnisse)
- Quantifizierung: Geschätzter finanzieller Schaden, Wiederherstellungskosten, Haftungsrisiko

### Schritt 2 – Insiderinformations-Prüfung

- Kursrelevanz: Würde ein verständiger Anleger die Information berücksichtigen?
 Indikation für hohe Kursrelevanz: erhebliche Betriebsunterbrechung, große Kundendaten-
 verluste, behördliche Ermittlungen, drohende Schadensersatzklagen
- Zeitpunkt: Ab wann lag präzise Information vor (erster sicherer Kenntnisstand)?
- Unsicherheit: Frühe Phasen eines Angriffs können noch unpräzise sein; laufende
 Forensik kann den Eintritt von Schäden als noch unbekannt qualifizieren

### Schritt 3 – Aufschub wegen laufender Strafverfolgung / IT-Forensik

- Legitimes Interesse: Laufende strafrechtliche Ermittlungen oder Forensik können
 durch frühzeitige Veröffentlichung beeinträchtigt werden
- ESMA-Guidance: Aufschub möglich, wenn Behörden (BSI, BKA) bestätigen, dass
 Veröffentlichung Ermittlungen gefährdet
- Praktisch: Emittent sollte BSI/BKA schriftlich anfragen und Antwort dokumentieren
- Aufschub endet: Wenn kein behördlicher Vorbehalt mehr besteht oder Öffentlichkeit
 durch Dritte informiert wurde

### Schritt 4 – Parallele Meldepflichten

- DSGVO Art. 33: Datenschutzbehörde (BfDI / Landesbehörde) innerhalb 72 Stunden
- NIS-2: BSI innerhalb 24 Stunden (Early Warning) und 72 Stunden (Notification)
- BaFin: Ggf. KWG-Meldepflicht für Finanzinstitute (§ 25a KWG)
- Koordination aller Meldepflichten mit einheitlicher Kommunikationsstrategie

### Schritt 5 – Ad-hoc-Veröffentlichung

- Inhalt: Art des Angriffs (soweit bekannt), betroffene Systeme, geschätzte Auswirkungen,
 ergriffene Maßnahmen, Ausblick
- Keine Offenlegung von Informationen, die laufende Ermittlungen gefährden
- Aktualisierungs-Ad-hoc: Wenn neue wesentliche Informationen bekannt werden

## Red-Team-Fragen

- Wurde der Zeitpunkt der Insiderinformations-Entstehung korrekt bestimmt?
- Liegen die Aufschub-Voraussetzungen vor (Behördenbestätigung)?
- Werden DSGVO- und NIS-2-Meldepflichten parallel und koordiniert erfüllt?
- Gibt es Eigengeschäfte von PDMRs zwischen Angriffs-Erkenntnis und Ad-hoc?
- Ist die Ad-hoc-Mitteilung ausreichend informativ ohne Ermittlungsgefährdung?

## Ausgabeformat

Erzeuge:
1. Schadensbewertungs-Matrix (System × Schadensart × Kursrelevanz-Indikation)
2. Parallele Meldepflichten-Übersicht (MAR × DSGVO × NIS-2 × KWG)
3. Aufschub-Prüfprotokoll
4. Ad-hoc-Entwurf Cyberangriff

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.
