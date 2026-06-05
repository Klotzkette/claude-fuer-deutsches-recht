---
name: ins-sanierung-insolvenzreife
description: "Ins 049 Sanierung Und Starug, Ins 050 Insolvenzreife: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 049 Sanierung Und Starug, Ins 050 Insolvenzreife

## Arbeitsbereich

Dieser Skill bündelt **Ins 049 Sanierung Und Starug, Ins 050 Insolvenzreife** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-049-sanierung-und-starug` | Prueft Insiderrecht-Pflichten in Restrukturierungsverfahren (StaRUG, Schutzschirm, Insolvenzplan): Insiderinformations-Zeitpunkte, Ad-hoc und Glaeubiger-Informationsfluss. |
| `ins-050-insolvenzreife` | Prueft Insiderrecht-Pflichten bei drohender oder eingetretener Insolvenzreife: Ad-hoc-Pflicht, Handelsverbot, Koordination mit InsO-Antragsfristen. |

## Arbeitsweg

Für **Ins 049 Sanierung Und Starug, Ins 050 Insolvenzreife** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-049-sanierung-und-starug`

**Fokus:** Prueft Insiderrecht-Pflichten in Restrukturierungsverfahren (StaRUG, Schutzschirm, Insolvenzplan): Insiderinformations-Zeitpunkte, Ad-hoc und Glaeubiger-Informationsfluss.

# Sanierung und StaRUG – Insiderrecht bei Restrukturierung

## Rechtlicher Rahmen

Außergerichtliche Restrukturierungen, StaRUG-Verfahren (Gesetz über den Stabilisierungs-
und Restrukturierungsrahmen für Unternehmen), Schutzschirm und Insolvenzplan sind
insiderrechtlich komplex: Sie erzeugen mehrstufige Insiderinformationen (Geltl/Daimler-Test),
erfordern aber gleichzeitig Gläubiger-Kommunikation unter NDA. MAR und InsO-Vertraulichkeit
müssen koordiniert werden.

Rechtsgrundlagen:
- Art. 7, 17 MAR (Zwischenschritte): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- StaRUG: https://www.gesetze-im-internet.de/starug/
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die insiderrechtliche Compliance in Restrukturierungsverfahren, von der
ersten Restrukturierungsüberlegung bis zum abgeschlossenen Sanierungsplan.

## Arbeitsprogramm

### Schritt 1 – Frühe Restrukturierungsphase (Erste Analyse)

- Geltl/Daimler-Test: Wann ist Restrukturierungsbedarf als präzise Information erkennbar?
 (Erste konservative Finanzprognose, die Covenant-Verletzung prognostiziert?)
- Kursrelevanz: Restrukturierungsbedarf ist für börsennotierte Unternehmen regelmäßig
 kursrelevant
- Aufschub: Legitimes Interesse (laufende Verhandlungen mit Gläubigern) möglich, aber:
 Öffentliche Aussagen des Vorstands dürfen nicht widersprüchlich sein

### Schritt 2 – Gläubiger-Kommunikation und Insiderlisten

- Banken/Anleihegläubiger, die in den Restrukturierungsprozess eingebunden sind, werden
 Insider (Art. 18 MAR: Insiderliste)
- NDA und Insiderbelehrung für alle eingebundenen Gläubiger
- Kreditverträge und NDA müssen Insiderrecht-Klauseln enthalten

### Schritt 3 – StaRUG-Anzeige und Ad-hoc-Pflicht

- Anzeige des Restrukturierungsvorhabens beim Restrukturierungsgericht: In der Praxis
 Insiderinformation (kursrelevant)
- Abstimmung: Muss die Anzeige ad-hoc veröffentlicht werden?
 → Ja, wenn der Markt die Restrukturierungsnotwendigkeit noch nicht kennt
- StaRUG-Verfahren ist grundsätzlich vertraulich (§ 84 StaRUG), aber MAR-Pflicht geht vor

### Schritt 4 – Plan-Abstimmung und Ad-hoc-Kaskade

- Jeweils neue Insiderinformation bei: Planeinreichung, Abstimmungsergebnis,
 Gericht-Bestätigung, Planvollzug
- Ad-hoc nach jeder wesentlichen Stufe
- Insiderliste: Wer kennt welche Stufe?

### Schritt 5 – Post-Restrukturierung

- Nach Abschluss: Insiderlisten schließen (Austrittsdaten)
- Neues Management, neue PDMRs: Directors' Dealings-Pflichten auffrischen
- Compliance-Policy nach Restrukturierung aktualisieren

## Red-Team-Fragen

- Wurde der frühestmögliche Entstehungszeitpunkt der Insiderinformation bestimmt?
- Ist der Aufschub während der Restrukturierungsverhandlungen vollständig dokumentiert?
- Wurden alle Gläubiger als Sekundärinsider behandelt und belehrt?
- Werden Ad-hoc-Mitteilungen bei jeder wesentlichen Stufe des Verfahrens veröffentlicht?
- Widersprechen öffentliche Aussagen des Vorstands der verschwiegenen Insiderinformation?

## Ausgabeformat

Erzeuge:
1. Restrukturierungs-Meilensteinmatrix mit Insiderinformations-Prüfung je Stufe
2. Gläubiger-Insiderlisten-Framework
3. Ad-hoc-Kaskade (StaRUG-Verfahren: Trigger × Ad-hoc-Inhalt)
4. Aufschub-Prüfprotokoll (laufende Verhandlungen)

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, dejure.org.

## 2. `ins-050-insolvenzreife`

**Fokus:** Prueft Insiderrecht-Pflichten bei drohender oder eingetretener Insolvenzreife: Ad-hoc-Pflicht, Handelsverbot, Koordination mit InsO-Antragsfristen.

# Insolvenzreife – Insiderrecht und Ad-hoc-Pflicht

## Rechtlicher Rahmen

Wenn ein börsennotierter Emittent zahlungsunfähig (§ 17 InsO) oder überschuldet (§ 19 InsO)
ist oder Zahlungsunfähigkeit droht (§ 18 InsO), ist dies regelmäßig eine kursrelevante
Insiderinformation. Ad-hoc-Pflicht nach Art. 17 MAR besteht unabhängig von der InsO-Antrags-
pflicht. Beide Pflichten (Ad-hoc und InsO-Antrag) laufen parallel.

Rechtsgrundlagen:
- Art. 7, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- §§ 15a, 17–19 InsO: https://www.gesetze-im-internet.de/inso/__15a.html
- § 97 WpHG: https://www.gesetze-im-internet.de/wphg/__97.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill koordiniert die Ad-hoc-Pflicht mit der InsO-Antragsfristen bei drohender oder
eingetretener Insolvenzreife und verhindert die typischen Haftungsfallen.

## Arbeitsprogramm

### Schritt 1 – Insolvenzreife als Insiderinformation

- Präzision: Bestätigung durch WP, Steuerberater oder Controller, dass Insolvenzgründe vorliegen
- Kursrelevanz: Nahezu immer kursrelevant; drohende Insolvenz schon bei erheblicher
 Wahrscheinlichkeit
- Nichtöffentlichkeit: Bis zur Ad-hoc-Veröffentlichung nicht bekannt

### Schritt 2 – Parallele Fristen

- InsO § 15a: Antragspflicht innerhalb von 6 Wochen bei Zahlungsunfähigkeit oder
 Überschuldung (Schnittstelle zum Strafrecht: § 15a Abs. 6 InsO)
- MAR Art. 17: Veröffentlichung „so bald wie möglich" = unverzüglich
- Praxis: Ad-hoc-Pflicht entsteht i.d.R. früher als InsO-Antrag (schon bei drohender
 Zahlungsunfähigkeit), InsO-Antrag kann später folgen

### Schritt 3 – Aufschub bei Sanierungsverhandlungen

- Legitimes Interesse: Laufende Sanierungsverhandlungen mit Gläubigern oder Investoren
- Strenge Anforderungen: Sanierungschance muss realistisch sein, nicht nur hypothetisch
- Trigger für Aufhebung: Scheitern der Sanierung, Insolvenzantrag, Leak

### Schritt 4 – PDMR-Eigengeschäfte und Handelsverbote

- PDMRs, die von der Insolvenzreife wissen: Sofortiges Handelsverbot (Art. 14 MAR)
- Typische Fehlkonstellation: CFO verkauft Aktien kurz bevor Insolvenzreife ad-hoc
 kommuniziert wird → Strafbarkeit nach § 119 WpHG
- Compliance muss PDMR-Transaktionen im kritischen Zeitraum sofort überprüfen

### Schritt 5 – Ad-hoc-Inhalt bei Insolvenzreife

- Tatsachenbasis: Welche Insolvenzgründe? (Zahlungsunfähigkeit, drohend, Überschuldung)
- Maßnahmen: Was wird unternommen? (Insolvenzantrag, Sanierungsplan, Suche nach Investor)
- Ausblick: Soweit möglich (kein Irreführungsrisiko)
- Insolvenzantrag: Separate Ad-hoc nach Antragstellung

## Red-Team-Fragen

- Wurde die Insolvenzreife als Insiderinformation korrekt und zeitnah identifiziert?
- Wurden PDMR-Eigengeschäfte im kritischen Zeitraum geprüft?
- Ist der Aufschub (falls Sanierungsverhandlungen) mit realistischer Sanierungschance begründet?
- Wurden Ad-hoc-Pflicht und InsO-Antragsfristen koordiniert?
- Ist der Ad-hoc-Inhalt präzise und nicht irreführend?

## Ausgabeformat

Erzeuge:
1. Insolvenzreife-Insiderinformations-Prüfprotokoll
2. Parallel-Fristen-Tabelle (MAR × InsO)
3. Aufschub-Prüfprotokoll bei Sanierungsverhandlungen
4. Ad-hoc-Entwurf Insolvenzreife / Insolvenzantrag

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Bei einer Unternehmensanleihe, die neben der Aktie börsennotiert ist, gelten MAR-Pflichten
für beide Instrumente. Die Insiderinformation der Insolvenzreife betrifft nicht nur die Aktie,
sondern auch die Anleihe (Kurssturz auf Recovery-Value). Compliance muss beide Instrumente
in der Kursrelevanz-Analyse berücksichtigen und die Ad-hoc-Mitteilung adressiert beide
Anlegergruppen (Aktionäre und Anleihegläubiger).

Weitere Quellen:
- Art. 2 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- §§ 15a, 17–19 InsO: https://www.gesetze-im-internet.de/inso/__15a.html
