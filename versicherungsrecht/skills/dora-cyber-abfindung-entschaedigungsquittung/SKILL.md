---
name: dora-cyber-abfindung-entschaedigungsquittung
description: "Dora Cyber Abfindung Entschaedigungsquittung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dora Cyber Abfindung Entschaedigungsquittung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Dora Cyber Abfindung Entschaedigungsquittung** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dora-cyber-ikt-versicherer` | DORA-Compliance für Versicherer/Vermittler: IKT-Risikomanagement, Ausgliederung, Incident Reporting, Register of Information und Drittanbietersteuerung. |
| `vergleich-abfindung-entschaedigungsquittung` | Vergleich mit Versicherern: Abfindungserklärung, Erledigungsklausel, Nachschäden, Regress, Steuer, Kosten und Widerruf/Anfechtung. |
| `bu-abstrakte-konkrete-verweisung` | Abstrakte/konkrete Verweisung in der BU: Lebensstellung, Ausbildung, Erfahrung, Einkommen, Arbeitsmarkt und tatsächliche Tätigkeit sauber prüfen. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Dora Cyber Abfindung Entschaedigungsquittung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dora-cyber-ikt-versicherer`

**Fokus:** DORA-Compliance für Versicherer/Vermittler: IKT-Risikomanagement, Ausgliederung, Incident Reporting, Register of Information und Drittanbietersteuerung.

# DORA für Versicherer und Vermittler

## Einsatz

Der Skill ist für Versicherer, Maklerpools und Dienstleister, die Cyber- und Ausgliederungsrisiken aufsichtsrechtlich dokumentieren müssen.

## Norm- und Quellenanker

DORA (VO (EU) 2022/2554); VAG; BaFin/EIOPA/ESA-Regeln live prüfen; DSGVO/NIS2-Schnittstelle.

## Arbeitsfragen

1. Welche regulierte Einheit und welche IKT-Funktion?
2. Ist ein kritischer Drittanbieter oder eine Ausgliederung betroffen?
3. Welche Incident-Meldekette gilt?
4. Welche Vertragsklauseln fehlen?

## Output

DORA-Lückenliste, Vertragsklausel-Check, Incident-Playbook und Vorstandsvorlage.

## Red Flags

- SaaS-Dienst als normale Beschaffung behandelt
- Incident nur datenschutzrechtlich gemeldet
- Register of Information unvollständig
- Business Continuity nicht getestet

## Anschluss-Skills

- cyberversicherung-ransomware-sanktionsrecht
- solvency-ii-scr-orsa-aufsichtsrecht

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `vergleich-abfindung-entschaedigungsquittung`

**Fokus:** Vergleich mit Versicherern: Abfindungserklärung, Erledigungsklausel, Nachschäden, Regress, Steuer, Kosten und Widerruf/Anfechtung.

# Vergleich, Abfindung und Entschädigungsquittung

## Einsatz

Der Skill verhindert, dass ein schneller Vergleich spätere Ansprüche ungewollt abschneidet.

## Norm- und Quellenanker

BGB §§ 779, 133, 157; VVG; ZPO; RVG; Steuerrecht als Hinweis.

## Arbeitsfragen

1. Welche Ansprüche sollen endgültig erledigt sein?
2. Gibt es unbekannte Spätfolgen oder Folgeschäden?
3. Wer trägt Kosten, Gutachten, Regress und Steuern?
4. Ist die Klausel verständlich und passend?

## Output

Vergleichs-Redline, Risikoaufklärung, Reservierungsklauseln und Mandantenentscheidung.

## Red Flags

- Globalquittung bei unklaren Spätfolgen
- Regressrechte nicht geregelt
- Kosten unklar
- Steuer-/Sozialleistungsschnittstelle vergessen

## Anschluss-Skills

- vvg-falligkeit-14-abschlagszahlung
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `bu-abstrakte-konkrete-verweisung`

**Fokus:** Abstrakte/konkrete Verweisung in der BU: Lebensstellung, Ausbildung, Erfahrung, Einkommen, Arbeitsmarkt und tatsächliche Tätigkeit sauber prüfen.

# BU: abstrakte und konkrete Verweisung

## Einsatz

Wenn der Versicherer sagt „Sie können doch etwas anderes machen“, zerlegt dieser Skill die Verweisung.

## Norm- und Quellenanker

VVG §§ 172 ff.; AVB BU; BGB Auslegung; Rechtsprechung nur verifiziert.

## Arbeitsfragen

1. Erlauben die AVB abstrakte Verweisung überhaupt?
2. Welche Vergleichstätigkeit wird konkret benannt?
3. Passt sie zu Ausbildung, Erfahrung und Lebensstellung?
4. Bei konkreter Tätigkeit: ist sie stabil, zumutbar und vollwertig?

## Output

Verweisungsabwehr mit Vergleichsprofil, Einkommensmatrix und Mandantenfragen.

## Red Flags

- Vergleichsberuf bleibt wolkig
- Lebensstellung nur am Einkommen gemessen
- Umschulung wird unterstellt
- Teilzeit/Schonarbeitsplatz übersehen

## Anschluss-Skills

- bu-berufsbild-50-prozent-substantiierung
- bu-nachpruefung-anerkenntnis-leistungseinstellung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
