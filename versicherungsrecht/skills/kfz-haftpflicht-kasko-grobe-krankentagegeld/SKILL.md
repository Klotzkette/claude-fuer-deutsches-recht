---
name: kfz-haftpflicht-kasko-grobe-krankentagegeld
description: "KFZ Haftpflicht Kasko Grobe Krankentagegeld: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KFZ Haftpflicht Kasko Grobe Krankentagegeld

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **KFZ Haftpflicht Kasko Grobe Krankentagegeld** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kfz-haftpflicht-regress-alkohol-flucht` | Kfz-Haftpflichtversicherung: Außenregulierung, Innenregress, Obliegenheitsverletzung, Alkohol, Unfallflucht, Fahrerlaubnis und Regresshöchstgrenzen. |
| `kfz-kasko-grobe-fahrlaessigkeit-entwendung` | Kfz-Kaskoversicherung: Entwendung, Unfall, Wild, Alkohol, grobe Fahrlässigkeit, Obliegenheiten, Wiederbeschaffungswert und Sachverständigenstreit. |
| `krankentagegeld-berufsunfaehigkeit-abgrenzung` | Krankentagegeldversicherung: Arbeitsunfähigkeit, Berufsunfähigkeit, Leistungseinstellung, Nachweis, PKV-Schnittstelle und existenzielle Liquidität. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **KFZ Haftpflicht Kasko Grobe Krankentagegeld**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kfz-haftpflicht-regress-alkohol-flucht`

**Fokus:** Kfz-Haftpflichtversicherung: Außenregulierung, Innenregress, Obliegenheitsverletzung, Alkohol, Unfallflucht, Fahrerlaubnis und Regresshöchstgrenzen.

# Kfz-Haftpflicht: Regress bei Alkohol, Flucht, Obliegenheit

## Einsatz

Für Mandate, in denen die Haftpflicht zwar den Dritten bezahlt, dann aber den Versicherungsnehmer regressiert.

## Norm- und Quellenanker

VVG §§ 28, 116; PflVG; AKB; StVG; StGB § 142 als Sachkontext.

## Arbeitsfragen

1. Welche Pflichtverletzung wird regressbegründend behauptet?
2. Welche Regressgrenze und AKB-Regel gilt?
3. War die Pflichtverletzung kausal oder vorsätzlich?
4. Welche Straf-/OWi-Akte beeinflusst die Beweisführung?

## Output

Regressabwehr, Kausalitätsargumente, Zahlungs-/Ratenvergleich und Schnittstelle Strafverfahren.

## Red Flags

- Strafurteil ungeprüft übernommen
- Regresshöchstgrenze übersehen
- Fahrer und Halter verwechselt
- Kausalitätsgegenbeweis nicht genutzt

## Anschluss-Skills

- kfz-kasko-grobe-fahrlaessigkeit-entwendung
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `kfz-kasko-grobe-fahrlaessigkeit-entwendung`

**Fokus:** Kfz-Kaskoversicherung: Entwendung, Unfall, Wild, Alkohol, grobe Fahrlässigkeit, Obliegenheiten, Wiederbeschaffungswert und Sachverständigenstreit.

# Kfz-Kasko: Entwendung, Unfall, grobe Fahrlässigkeit

## Einsatz

Der Skill prüft Kaskoablehnungen und Kürzungen, ohne Haftpflichtregulierung zu vermischen.

## Norm- und Quellenanker

VVG §§ 28, 81, 82; AKB; StVG nur als Sachkontext; ZPO.

## Arbeitsfragen

1. Welche Kaskogefahr und welche AKB-Fassung gilt?
2. Ist Entwendung plausibel und dokumentiert?
3. Welche grobe Fahrlässigkeit wird behauptet?
4. Wie werden Wiederbeschaffungswert, Restwert und Selbstbeteiligung berechnet?

## Output

Kasko-Deckungsmemo, Beweisplan, Wertgutachtenfragen und Regulierungsschreiben.

## Red Flags

- Alkohol/Flucht als Totalablehnung ohne Quote
- Zweitschlüsselproblem
- Wertgutachten dünn
- Obliegenheiten nach Unfall übersehen

## Anschluss-Skills

- kfz-haftpflicht-regress-alkohol-flucht
- vvg-obliegenheit-28-quotelung-kausalitaet

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `krankentagegeld-berufsunfaehigkeit-abgrenzung`

**Fokus:** Krankentagegeldversicherung: Arbeitsunfähigkeit, Berufsunfähigkeit, Leistungseinstellung, Nachweis, PKV-Schnittstelle und existenzielle Liquidität.

# Krankentagegeld vs. Berufsunfähigkeit

## Einsatz

Der Skill klärt die gefährliche Grenze: krankgeschrieben, aber angeblich dauerhaft berufsunfähig.

## Norm- und Quellenanker

VVG §§ 192 ff.; MB/KT; BGB; ZPO; ggf. SGB V Abgrenzung.

## Arbeitsfragen

1. Welche Tätigkeit wird aktuell ausgeübt und seit wann besteht AU?
2. Welche AU-Nachweise liegen vor?
3. Warum behauptet der Versicherer BU und ab wann?
4. Welche Anschlussdeckung oder BU-Police existiert?

## Output

KT/Bu-Abgrenzungsmemo, Liquiditätsplan, Nachweisbrief und Eil-/Klageoption.

## Red Flags

- Versicherer beendet KT ohne tragfähige BU-Begründung
- AU und BU begrifflich verwechselt
- Selbstständige Tätigkeit nicht konkret erfasst
- Lücke zwischen KT und BU-Leistung

## Anschluss-Skills

- bu-berufsbild-50-prozent-substantiierung
- pkv-kostenerstattung-medizinische-notwendigkeit

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
