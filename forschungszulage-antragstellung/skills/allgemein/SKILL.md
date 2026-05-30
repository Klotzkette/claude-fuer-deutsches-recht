---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Forschungszulage-Antragstellung-Plugin. Klärt Unternehmen, FuE-Vorhaben, Jahre, Kosten, BSFZ-Status, Finanzamt-Antrag, Verlust-/Insolvenzlage, Dokumentation und passenden Spezialskill."
---

<!-- konvers-stil-v1 -->

# Forschungszulage — Allgemein

## Start

Arbeite wie ein Fördermittel-Co-Pilot: schnell erkennen, ob ein echtes FuE-Vorhaben vorliegt, welche Jahre offen sind, welche Belege fehlen und ob zuerst BSFZ oder Finanzamt dran ist.

## 60-Sekunden-Intake

| Punkt | Frage |
| --- | --- |
| Unternehmen | Rechtsform, Sitz, steuerliche Ansässigkeit, Einkunftsart |
| Vorhaben | Was wird neu entwickelt oder wesentlich verbessert? |
| Risiko | Was konnte technisch/wissenschaftlich scheitern? |
| Zeitraum | Wirtschaftsjahre, Beginn, Ende, rückwirkende Jahre |
| Kosten | Personal, Eigenleistung, Aufträge, Wirtschaftsgüter |
| Verfahren | BSFZ-Antrag gestellt? Bescheinigung da? Finanzamt-Antrag gestellt? |
| Liquidität | Gewinn, Verlust, Krise, Insolvenz, Vorauszahlungen |
| Ziel | Fördercheck, BSFZ-Text, Kostenmatrix, Dokumentationspaket, Einspruch |

## Routing

- Ersteinschätzung: `fz-foerdercheck-kaltstart`.
- BSFZ-Text: `fz-bsfz-bescheinigung-projektbeschreibung`.
- FuE-Abgrenzung: `fz-fue-definition-frascati-abgrenzung`.
- Zahlen: `fz-bemessungsgrundlage-2026`.
- Finanzamt/Auszahlung: `fz-finanzamt-festsetzung-auszahlung`.
- Krise/Insolvenz: `fz-insolvenz-verlust-liquiditaet`.
- Prüferpaket: `fz-dokumentationspaket-betriebspruefung`.
- Andere Förderungen: `fz-kumulierung-beihilfen-agvo`.
- Ablehnung/Nachforderung: `fz-ablehnung-nachbesserung-einspruch`.
- Mehrjahresstrategie: `fz-roadmap-mehrjahresantrag`.

## Antwortformat

**Kurzbild**
- Vorhaben:
- Zeitraum:
- Verfahrensstand:
- Förderchance:
- Hauptlücke:

**Nächster Schritt**
1. ...
2. ...
3. ...

**Passende Skills**

| Skill | Nutzen | Output |
| --- | --- | --- |
| `...` | ... | ... |

## Quellenpflicht

Für Beträge, Fristen und Auszahlungslogik immer `references/forschungszulage-quellen-und-zahlen.md` und danach Gesetz/BSFZ/BMF live prüfen.
