---
name: ins-incident
description: "INS Incident: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat."
---

# INS Incident

## Arbeitsbereich

Dieser Skill arbeitet **INS Incident** als zusammenhängenden Arbeitsgang im Plugin Insiderrecht / Compliance (WpHG, MAR) ab — nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ins-055-incident-drill` | Fuehrt einen Tabletop-Drill fuer Insiderrecht-Krisenfaelle durch: simulierte Ad-hoc-Entscheidung, Aufschub-Pruefer und BaFin-Kommunikation unter Zeitdruck. |

## Arbeitsweg

Im Plugin Insiderrecht / Compliance (WpHG, MAR) gilt für **INS Incident**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ins-055-incident-drill`

**Fokus:** Fuehrt einen Tabletop-Drill fuer Insiderrecht-Krisenfaelle durch: simulierte Ad-hoc-Entscheidung, Aufschub-Pruefer und BaFin-Kommunikation unter Zeitdruck.

# Incident Drill – Insiderrecht-Krisenübung (Tabletop Exercise)

## Konzept

Ein Insiderrecht-Incident Drill ist eine strukturierte Übungseinheit, in der das Compliance-
Team und das Management einen realistischen Insiderrecht-Krisenfall simulieren – ohne reale
Konsequenzen, aber mit echtem Entscheidungsdruck. Ziel ist es, Schwachstellen im Prozess zu
entdecken, bevor ein realer Fall eintritt. Erfahrungsgemäß decken Drills Lücken auf, die bei
regulären Schulungen nicht sichtbar werden.

Rechtsgrundlagen:
- Art. 7, 17, 18 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- ESMA MAR-Leitlinien: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill führt einen vollständigen Incident Drill durch: Er liefert das Szenario,
moderiert den Entscheidungsprozess, wertet die Ergebnisse aus und erstellt die Drill-
Dokumentation.

## Arbeitsprogramm

### Phase 1 – Szenario-Auswahl

Wähle eines der folgenden Szenarien (oder erstelle ein unternehmens-spezifisches):
a) Profit Warning: CFO erhält Monatszahlen, die erheblich von Guidance abweichen.
 → Entscheidung: Ad-hoc sofort oder Aufschub bis Quartalsabschluss?
b) M&A-Leak: Medien berichten über bevorstehende Übernahme des Emittenten.
 → Entscheidung: Sofortveröffentlichung oder Dementierung?
c) PDMR-Verdacht: Compliance erhält Hinweis, dass ein Vorstandsmitglied Aktien
 kurz vor einer Profit-Warning verkauft hat.
 → Entscheidung: Interne Untersuchung, BaFin-Meldung, externe Kanzlei?
d) Cyberangriff: IT meldet schwerwiegendes Datenleck in der Nacht.
 → Entscheidung: Wann ist Insiderinformation entstanden? Ad-hoc unverzüglich?

### Phase 2 – Drill-Durchführung (120 Minuten)

Rollen:
- Moderator (Compliance oder externe Kanzlei)
- CFO
- General Counsel
- Compliance-Officer
- IR-Leiter
- Ggf. CEO (bei C-Level-Drill)

Ablauf (pro Szenario):
T+0: Moderator präsentiert Ausgangssachverhalt
T+5 min: Teams treffen erste Einschätzung (Insiderinformation ja/nein?)
T+15 min: Folgeentscheidung (Ad-hoc sofort / Aufschub / Weitere Sachverhaltsaufklärung)
T+30 min: Neuer Sachverhalt (Komplikation: BaFin fragt an, Kurssprung, Medien berichten)
T+60 min: Finalentscheidung und Kommunikationsplan
T+90 min: Nachbesprechung: Wo lagen die Entscheidungslücken?

### Phase 3 – Entscheidungsprotokoll

Protokolliere für jede Drill-Entscheidung:
- Wer hat welche Entscheidung getroffen?
- Auf welcher Grundlage (Norm, Leitfaden)?
- Wurde die Entscheidung widerspruchsfrei begründet?
- Welche Informationen fehlten?
- Welche Schritte wurden vergessen?

### Phase 4 – Auswertung und Verbesserungsplan

- Schwachstellen identifizieren: Wo war der Prozess unklar?
- Verbesserungsmaßnahmen: Richtlinienänderung, Schulung, Eskalationsweg
- Verantwortliche und Fristen für Umsetzung
- Follow-up-Drill in 6–12 Monaten planen

### Phase 5 – Dokumentation

- Drill-Protokoll archivieren (Szenario, Teilnehmer, Entscheidungen, Ergebnisse)
- Verbesserungsplan mit Umsetzungs-Tracking
- Nachweis für Compliance-Committee und Aufsichtsrat

## Red-Team-Fragen

- Waren alle relevanten Entscheidungsträger beim Drill anwesend?
- Wurden die realen Entscheidungsabläufe simuliert (kein „ideal case" spielen)?
- Wurden Schwachstellen unverschönt dokumentiert?
- Gibt es einen verbindlichen Verbesserungsplan mit Fristen?

## Ausgabeformat

Erzeuge:
1. Drill-Szenario (vollständig ausgearbeiteter Sachverhalt mit Komplikations-Inject)
2. Rollen-Instruktionskarten (je Teilnehmer eine Seite)
3. Entscheidungsprotokoll-Vorlage (für den Drill selbst)
4. Auswertungs-Formular (Schwachstellen × Maßnahme × Verantwortlicher × Frist)
5. Management-Summary für Compliance-Committee

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, bgh.de,
dejure.org, openjur.de.
