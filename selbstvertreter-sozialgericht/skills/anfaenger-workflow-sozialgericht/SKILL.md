---
name: anfaenger-workflow-sozialgericht
description: "Geführter Anfänger-Workflow für Bürgerinnen und Bürger vor dem Sozialgericht: erklärt Bescheid, Widerspruch, Klage, Eilantrag, Amtsermittlung, Kostenfreiheit, Belege und Termin in einfacher Sprache und routet zu passenden Sozialgerichts-Skills."
---

# Anfänger-Workflow Sozialgericht

## Zweck

Dieser Skill ist der ruhige Einstieg für Menschen, die mit Jobcenter, Krankenkasse, Rentenversicherung, Pflegekasse, Versorgungsamt oder Berufsgenossenschaft streiten und noch nie vor dem Sozialgericht waren.

Er führt Schritt für Schritt, in einfacher Sprache, mit Fristen zuerst und ohne falsche Scheu: Vor dem Sozialgericht darf man sich selbst vertreten.

## In einfacher Sprache

Sie haben einen Bescheid bekommen. Sie sind nicht einverstanden. Dann gibt es meistens zuerst den Widerspruch. Danach kann eine Klage zum Sozialgericht kommen. Wenn es dringend ist, gibt es einen Eilantrag.

## Sofortfrage

**Wie viel Hilfe brauchen Sie gerade?**

- **Sehr geführt:** Bitte alles einfach erklären und nur eine Aufgabe auf einmal.
- **Normal geführt:** Bitte Frist, Weg und passende Skills.
- **Kurzmodus:** Bitte nur Risiko, nächster Schritt und Muster.

Wenn eine Frist sichtbar ist, kommt die Frist zuerst.

## Erste Triage

| Punkt | Frage |
|---|---|
| Schreiben | Bescheid, Widerspruchsbescheid, Klageantwort, Gutachten, Ladung, Urteil? |
| Behörde | Jobcenter, Krankenkasse, DRV, Pflegekasse, Versorgungsamt, BG, Sozialamt? |
| Thema | Bürgergeld, Krankengeld, Hilfsmittel, Pflegegrad, EM-Rente, GdB, Unfallversicherung? |
| Datum | Wann kam das Schreiben an? Was steht in der Rechtsbehelfsbelehrung? |
| Notlage | Fehlt Geld, Behandlung, Wohnung, Pflege oder existenzielle Leistung? |
| Ziel | Widerspruch, Klage, Eilantrag, Stellungnahme, Terminvorbereitung, Berufung? |

## Arbeitslogik

### 1. Frist und Notlage zuerst

Prüfen Sie:

- Widerspruchsfrist nach § 84 SGG;
- Klagefrist nach § 87 SGG;
- falsche oder fehlende Rechtsbehelfsbelehrung nach § 66 SGG;
- Eilbedarf nach § 86b SGG;
- laufende Leistungen, Gesundheit, Wohnung, Pflege oder Existenzminimum.

### 2. Den richtigen Weg wählen

| Lage | Weg |
|---|---|
| Bescheid gerade erhalten | Widerspruch |
| Widerspruchsbescheid erhalten | Klage |
| Behörde entscheidet nicht | Untätigkeitsklage |
| Geld/Leistung fehlt sofort | Eilantrag |
| SG-Urteil erhalten | Berufung oder Zulassung prüfen |
| Medizinisches Gutachten negativ | Stellungnahme und Beweisantrag |

### 3. Passende Skills

| Lage | Nächster Skill |
|---|---|
| Orientierung | `orientierung-selbstvertreter-sozialgericht` |
| Frist | `widerspruchsfrist-84-sgg` oder `fristen-berechnen-sgg-laien` |
| Widerspruch | `widerspruch-ohne-anwalt-einreichen` und `widerspruch-begruendung-laienleitfaden` |
| Klage | `klagearten-uebersicht-sgg` und `klage-zusammenstellen-bundle-sozialgericht` |
| Eilfall | `eilantrag-86b-sgg-grundlagen` |
| Belege | `arztberichte-vorlegen-laien-leitfaden` oder `beweismittel-im-sozialgericht-uebersicht` |
| Vor Abgabe | `sanity-check-selbstvertretung-sozialgericht` |
| Rechtsprechung | `rechtsprechungschat-sozialgericht` |
| Rechtsmittel | `zulassungsgrenzen-check-sozialgericht` |

## Ausgabeformat

**Kurzbild**
- Schreiben:
- Thema:
- Frist:
- Dringlichkeit:
- Nächster Weg:

**Jetzt tun**
1. [konkrete Handlung]

**Warum**
[Einfach erklären.]

**Passender Skill**
| Skill | Warum jetzt? |
|---|---|

**Bitte sammeln**
- Bescheid und Umschlag.
- Widerspruchsbescheid, falls vorhanden.
- Arztberichte, Rechnungen, Bescheinigungen, Kontoauszüge oder Pflegeprotokoll je nach Thema.

## Qualitätsregeln

- Keine komplizierten Gutachten am Anfang.
- Nicht sagen "das Gericht macht alles", sondern erklären: Amtsermittlung hilft, aber gute Unterlagen helfen noch mehr.
- Bei existenzieller Not immer Eilantrag prüfen.
- Bei BSG, Nichtzulassungsbeschwerde, schwieriger Medizin oder hoher Nachzahlung anwaltliche Hilfe/Sozialverband/PKH ansprechen.
