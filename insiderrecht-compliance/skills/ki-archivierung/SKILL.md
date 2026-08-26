---
name: ki-archivierung
description: "Für digitale Werkzeuge-Prognosemodelle und Insiderrecht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# KI-Prognosemodelle und Insiderrecht

## Arbeitsweg

- Emittent, Instrument, Handelsplatz, Zeitpunkt und Informationskette feststellen: Wer wusste wann was, war die Information präzise, nicht öffentlich und potenziell erheblich kursrelevant?
- MAR-Pflichten getrennt prüfen: Insiderinformation nach Art. 7 MAR, Handels-/Empfehlungs-/Weitergabeverbot nach Art. 14 MAR, Ad-hoc-Publizität nach Art. 17 MAR, Aufschub nach Art. 17 Abs. 4 MAR, Insiderliste nach Art. 18 MAR, Eigengeschäfte von Führungskräften nach Art. 19 MAR.
- Deutsche Sanktions- und Verfahrensspur live verifizieren: WpHG §§ 119 ff., BaFin-Zuständigkeit, Börsenrecht, ggf. WpÜG/AktG bei Übernahme, Delisting, Kapitalmaßnahme oder Hauptversammlung.
- Beweise aktenfest sichern: Timeline, Board-/AR-Unterlagen, Datenraum-Log, Insiderlisten-Versionen, Handelsdaten, Kommunikationskanäle, Aufschubvermerk, Veröffentlichungszeitpunkt und BaFin-/DGAP-/EQS-Belege.
- Strategische Ausgabe wählen: Ad-hoc-Entscheidungsvorlage, Aufschubvermerk, Leak-Response, Handelsstopp-Empfehlung, Insiderlisten-Audit, PDMR-Meldecheck, BaFin-Antwort oder Verteidigungsnotiz.
- Rechtsprechung und Behördenpraxis nur mit frei prüfbarer Quelle zitieren; keine BeckRS-/juris-Blindzitate und keine alten WpHG-Paragrafen als Ersatz für die unmittelbar geltende MAR verwenden.

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

Kläre, unter welchen Umständen KI-generierte Prognosen oder Analysen
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
