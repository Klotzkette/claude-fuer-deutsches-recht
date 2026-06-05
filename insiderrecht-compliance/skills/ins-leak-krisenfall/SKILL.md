---
name: ins-leak-krisenfall
description: "Ins 011 Leak Response, Ins 018 Krisenfall Profit Warning: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 011 Leak Response, Ins 018 Krisenfall Profit Warning

## Arbeitsbereich

Dieser Skill bündelt **Ins 011 Leak Response, Ins 018 Krisenfall Profit Warning** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-011-leak-response` | Steuert die Sofortreaktion auf einen Informationsleck: Veroeffentlichungspflicht, BaFin-Meldung, Medienmanagement und forensische Dokumentation. |
| `ins-018-krisenfall-profit-warning` | Steuert den Compliance-Prozess bei einer Profit Warning: Insiderinformations-Entstehungszeitpunkt, Ad-hoc-Pflicht, Inhalt und Koordination mit Konsensus-Updates. |

## Arbeitsweg

Für **Ins 011 Leak Response, Ins 018 Krisenfall Profit Warning** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-011-leak-response`

**Fokus:** Steuert die Sofortreaktion auf einen Informationsleck: Veroeffentlichungspflicht, BaFin-Meldung, Medienmanagement und forensische Dokumentation.

# Leak Response – Reaktion auf Informationslecks

## Rechtlicher Rahmen

Art. 17 Abs. 7 MAR verpflichtet den Emittenten, eine Insiderinformation unverzüglich zu
veröffentlichen, wenn die Vertraulichkeit nicht mehr gewährleistet werden kann. Kurssprünge
ohne öffentliche Erklärung gelten als Indikator für einen Leak. Die BaFin überwacht den Markt
kontinuierlich auf Handelsauffälligkeiten. Ein Leak beendet automatisch jeden laufenden Aufschub.

Rechtsgrundlagen:
- Art. 17 Abs. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 17 Abs. 4 MAR (Aufschub): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 50 WpHG: https://www.gesetze-im-internet.de/wphg/__50.html
- BaFin-Emittentenleitfaden Kap. VI.4: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die Sofortreaktion auf einen Informationsleak, koordiniert die
Veröffentlichungspflicht, sichert Beweise für die interne Untersuchung und managt die
Kommunikation nach außen.

## Arbeitsprogramm

### Schritt 1 – Leak-Erkennung und Bewertung (0–30 Min.)

Indikatoren für einen Leak:
- Ungewöhnliche Handelsvolumina oder Kurssprünge vor einer geplanten Ad-hoc-Mitteilung
- Medienberichte oder Social-Media-Posts mit kursrelevanten Details
- BaFin-Anfrage zu Handelsauffälligkeiten
- Interne Meldung (Whistleblower, Mitarbeiter)
Sofortmaßnahme: Compliance-Officer, CFO und General Counsel unverzüglich informieren.

### Schritt 2 – Entscheidung über Sofortveröffentlichung (30–60 Min.)

- Besteht ein laufender Aufschub? → Aufschub endet automatisch bei Leak (Art. 17 Abs. 7 MAR)
- Ist die Insiderinformation bereits ausreichend öffentlich (breite Medienberichterstattung)?
 → Wenn ja: Pflicht zur Klarstellung, nicht zwingend neue Ad-hoc
- Wenn nein: Unverzügliche Ad-hoc-Veröffentlichung (Skill ins-003)
- Entscheidung und Begründung mit Zeitstempel festhalten

### Schritt 3 – Medienmanagement und Handelsplatz

- Pressestelle: Keine Bestätigung oder Dementierung bis Ad-hoc veröffentlicht
- Handelsplatz informieren: Ggf. Handelsaussetzung beantragen
- Nach Ad-hoc: Freigabe für IR-Kommunikation

### Schritt 4 – BaFin-Kommunikation

- Proaktive Meldung an BaFin Wertpapieraufsicht (wA-Meldung)
- Inhalt: Sachverhalt des Leaks, Zeitpunkt der Entdeckung, ergriffene Maßnahmen
- BaFin kann eigenständige Untersuchung (§ 4 WpHG) einleiten

### Schritt 5 – Forensische Sicherung und interne Untersuchung

- IT-Forensik: E-Mails, Chat-Protokolle, Datenbankzugriffe sichern (Zeitfenster: 48h vor Leak)
- Insiderliste: Wer hatte Zugang zur Information?
- Befragung der Wissensträger (durch externe Kanzlei, um Vertraulichkeit zu wahren)
- Ergebnis der Untersuchung dokumentieren

## Red-Team-Fragen

- Wurde der Leak rechtzeitig erkannt (Marktmonitoring aktiv)?
- Wurde der laufende Aufschub korrekt beendet?
- Wurde die Ad-hoc-Mitteilung unverzüglich (und nicht erst nach PR-Vorbereitung) veröffentlicht?
- Wurde BaFin proaktiv informiert?
- Wurden Beweise vor Vernichtung gesichert?
- Ist die interne Untersuchung unabhängig (externe Kanzlei)?
- Wurden alle Insider-Listen-Einträge auf Vollständigkeit geprüft?

## Ausgabeformat

Erzeuge:
1. Leak-Response-Checkliste (zeitkritisch, mit Minutenangaben)
2. Ad-hoc-Entwurf (Sofortveröffentlichung)
3. BaFin-Meldungsschreiben
4. Forensische Untersuchungsvorlage
5. Kommunikations-Leitfaden (intern, Presse, Handelsplatz)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-018-krisenfall-profit-warning`

**Fokus:** Steuert den Compliance-Prozess bei einer Profit Warning: Insiderinformations-Entstehungszeitpunkt, Ad-hoc-Pflicht, Inhalt und Koordination mit Konsensus-Updates.

# Krisenfall Profit Warning – Ad-hoc und Insiderrecht

## Rechtlicher Rahmen

Eine Gewinnwarnung (Profit Warning) entsteht, wenn der Emittent erkennt, dass seine aktuell
kommunizierten Prognosen wesentlich unterschritten werden. Ab dem Zeitpunkt, an dem diese
Erkenntnis als präzise Information vorliegt und kursrelevant ist, besteht Ad-hoc-Pflicht nach
Art. 17 MAR. Es gibt keinen Aufschub-Tatbestand für Profit Warnings (keine laufenden
Verhandlungen, keine legitime Geheimnishaltung).

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 97 WpHG (Haftung): https://www.gesetze-im-internet.de/wphg/__97.html
- BaFin-Emittentenleitfaden Kap. VI.2: https://www.bafin.de/dok/8252648
- EuGH C-19/11 (Geltl/Daimler, Zwischenschritte): https://curia.europa.eu/juris/document/document.jsf?docid=123755

## Ziel dieses Skills

Dieser Skill steuert den Compliance-Prozess von der internen Erkenntnis einer Gewinnverfehlung
bis zur ordnungsgemäßen Ad-hoc-Veröffentlichung und der Konsensus-Kommunikation mit Analysten.

## Arbeitsprogramm

### Schritt 1 – Zeitpunkt der Insiderinformation

- Entstehungszeitpunkt: Wann war die Prognoseabweichung als präzise Information erkennbar?
 (Nicht erst beim CFO-Monats-Bericht, sondern ggf. schon bei erstem internen Alert)
- Anwendung des Geltl/Daimler-Tests: Auch ein Zwischenschritt (z. B. erste 2-Monats-Zahlen
 weichen stark ab) kann präzise und kursrelevant sein
- Ergebnis: Frühestmöglicher Zeitpunkt dokumentieren

### Schritt 2 – Kursrelevanz-Beurteilung

- Vergleich: Veröffentlichte Prognose vs. neue Erwartung
- Materiality-Schwelle: Es gibt keine feste prozentuale Grenze; BaFin-Emittentenleitfaden
 gibt Indikatorenliste
- Analyse: Wie stark weicht die neue Erwartung von Markterwartungen (Analystenkonsensus) ab?
- Ex-ante-Beurteilung: Würde ein verständiger Anleger die Information berücksichtigen?

### Schritt 3 – Inhalt der Profit-Warning-Ad-hoc

Pflichtinhalt:
- Frühere Prognose (Zitat aus letzter Veröffentlichung)
- Neue Prognose oder zumindest Angabe der Bandbreite (falls möglich)
- Ursachen der Abweichung (präzise, keine allgemeinen Floskeln)
- Zeitraum (welches Geschäftsjahr / Quartal)
- Ausblick (falls möglich)
Verboten: Verwischende Sprache, Prognose-Widersprüche, irreführende Formulierungen

### Schritt 4 – Koordination mit Analysten und IR

- Keine Advance-Information an Analysten oder Investoren vor Ad-hoc-Veröffentlichung
- Nach Ad-hoc: Analystencall oder IR-Mitteilung zulässig (keine neuen Informationen)
- Konsensus-Update: Analysten passen Schätzungen nach Ad-hoc eigenständig an

### Schritt 5 – Nachgang und Haftungsvorsorge

- Analyse: Wurden zwischen Entstehung der Insiderinformation und Ad-hoc Eigengeschäfte
 von PDMRs getätigt? → Prüfung auf Art. 14/19 MAR-Verstoß
- § 97-WpHG-Haftungsrisiko einschätzen: Wie lange zwischen Entstehung und Veröffentlichung?
- Compliance-Akte: Entstehungszeitpunkt der Insiderinformation belegen

## Red-Team-Fragen

- Wurde der frühestmögliche Entstehungszeitpunkt der Insiderinformation identifiziert?
- Hat ein PDMR zwischen Entstehung der Insiderinformation und Ad-hoc Aktien verkauft?
- Wurde kursrelevanz ex ante beurteilt, nicht erst nach einem Kurseinbruch?
- Enthält die Ad-hoc-Mitteilung eine konkrete neue Prognose oder nur Allgemeinplätze?
- Ist der Zeitraum zwischen interner Erkenntnis und Veröffentlichung dokumentiert
 (Haftungsrisiko § 97 WpHG)?

## Ausgabeformat

Erzeuge:
1. Profit-Warning-Ad-hoc-Entwurf
2. Insiderinformations-Entstehungszeitplan (intern vs. Ad-hoc-Datum)
3. PDMR-Eigengeschäfts-Check (Zeitraum der Insiderinformation)
4. § 97-WpHG-Haftungsrisiko-Einschätzung

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, curia.europa.eu,
bgh.de, dejure.org.
