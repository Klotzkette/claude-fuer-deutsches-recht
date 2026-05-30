---
name: allgemein
description: "Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Schnelltriage zu Unternehmen, FuE-Vorhaben, Wirtschaftsjahren, BSFZ-Status, Finanzamt-Antrag, Liquidität, Dokumentation und passendem Spezialskill. Liefert in einem Schritt das Kurzbild plus den ersten Arbeitsentwurf."
---

<!-- konvers-stil-v1 -->

# Forschungszulage — Allgemein

## Worum geht es

Die Forschungszulage nach FZulG ist eine rückzahlungsfreie steuerliche Förderung (Steuergutschrift) für Aufwendungen aus eigenen oder beauftragten FuE-Vorhaben. Sie wird beim Finanzamt festgesetzt, gegen die nächste Einkommen- oder Körperschaftsteuer aufgerechnet; ein Überschuss wird ausgezahlt. Das macht sie für Verlust- und Krisenphasen besonders wertvoll.

Kerneckdaten Stand 2026 (vom Mandanten/Antragsteller mit aktueller Gesetzesfassung und BSFZ-Portal zu verifizieren):

- Fördersatz grundsätzlich 25 Prozent der Bemessungsgrundlage. KMU-Erhöhung um 10 Prozentpunkte unter bestimmten Voraussetzungen.
- Bemessungsgrundlage ab 01.01.2026 maximal 12 Mio. Euro jährlich.
- Eigenleistung des Einzelunternehmers/Gesellschafter-Geschäftsführers: ab 2026 100 Euro je Arbeitsstunde, höchstens 40 Stunden je Woche.
- Auftragsforschung im EU/EWR-Raum mit 70 Prozent der Kosten ansatzfähig.
- Zusätzliche Gemein- und Betriebskostenpauschale 20 Prozent für nach dem 31.12.2025 begonnene Vorhaben.

Konkrete Werte und Fristen aus `references/forschungszulage-quellen-und-zahlen.md` und Live-Prüfung Gesetz/BSFZ/BMF.

## Wann brauchen Sie diesen Skill

Sie greifen zu `allgemein`, wenn:

- Das Mandat erstmals an FZulG-Beratung herangeführt wird.
- Unklar ist, ob ein einzelnes Vorhaben überhaupt FuE ist und ob sich der Aufwand lohnt.
- Mehrere Spezialfragen gleichzeitig auf dem Tisch liegen (BSFZ-Text, Personalkosten, Krise, Einspruch) und Sie eine Reihenfolge brauchen.
- Ein bestehender Antrag stockt und Sie das richtige Anschluss-Skill suchen.

## 60-Sekunden-Intake

| Punkt | Frage |
| --- | --- |
| Unternehmen | Rechtsform, Sitz, steuerliche Ansässigkeit, KMU-Status, Einkunftsart |
| Vorhaben | Was wird neu entwickelt oder wesentlich verbessert? Welches technische Problem? |
| Risiko | Was konnte technisch oder wissenschaftlich scheitern? |
| Zeitraum | Wirtschaftsjahre, Beginn, Ende, rückwirkende Jahre |
| Kosten | Eigene Personalkosten p.a., Eigenleistung, Auftragsforschung, Wirtschaftsgüter |
| Verfahren | BSFZ-Antrag schon gestellt? Bescheinigung da? Finanzamt-Antrag offen? |
| Liquidität | Gewinn, Verlust, Krise, drohende Insolvenz, Vorauszahlungen |
| Andere Förderung | ZIM, BMBF, Land, EU/Horizon — wegen Kumulierung |
| Ziel | Fördercheck, BSFZ-Entwurf, Kostenmatrix, Doku-Paket, Einspruch, Roadmap |

## Praxisleitfaden — Quick Wins aus der Praxis

- **Stundenerfassung sofort aktivieren**, auch wenn der Antrag erst 2027 läuft. Wer Personenstunden je Tag und Vorhaben sauber dokumentiert, gewinnt bei der Außenprüfung die Hälfte der Diskussionen.
- **Rückwirkend denken.** Antrag beim Finanzamt grundsätzlich noch für mehrere zurückliegende Jahre möglich (Frist ist vom Antragsteller mit § 5 FZulG und der AO zu prüfen). Erst Wirtschaftsjahre und Festsetzungsfristen klären, dann priorisieren.
- **Parallel statt seriell.** BSFZ-Antrag und Vorbereitung des Finanzamt-Antrags können parallel laufen. So vergeht nach Eingang der Bescheinigung kein weiteres Quartal.
- **Antragstaktung Q1.** BSFZ-Antrag im 1. Quartal des Folgejahres einreichen. Das BSFZ-Aufkommen ist dort tendenziell geringer, Bearbeitungszeiten kürzer (Erfahrungswert, kein offizielles Versprechen).
- **Software-Mittelstand, Maschinenbau, Biotech, Engineering** sind die Hauptklientel. Wer "ERP-Anpassung", "Customizing" oder "Migration" als FuE verkauft, wird abgelehnt — und brennt sich beim Prüfer ab.

## Verweis-Weiche — der passende Skill

| Anliegen | Skill |
| --- | --- |
| Erste Förderchance grob abschätzen | `fz-foerdercheck-kaltstart` |
| FuE-Eigenschaft sauber abgrenzen (Frascati) | `fz-fue-definition-frascati-abgrenzung` |
| BSFZ-Projektbeschreibung schreiben | `fz-bsfz-bescheinigung-projektbeschreibung` |
| Bemessungsgrundlage und Personalkosten rechnen | `fz-bemessungsgrundlage-2026` |
| Finanzamt-Antrag, Festsetzung, Auszahlung | `fz-finanzamt-festsetzung-auszahlung` |
| Doku-Paket für Außenprüfung | `fz-dokumentationspaket-betriebspruefung` |
| AGVO/Kumulierung mit anderen Förderungen | `fz-kumulierung-beihilfen-agvo` |
| Ablehnung BSFZ/FA, Einspruch, Nachbesserung | `fz-ablehnung-nachbesserung-einspruch` |
| Krise, Verlustlage, Insolvenz | `fz-insolvenz-verlust-liquiditaet` |
| Mehrjahresstrategie, Folgeanträge | `fz-roadmap-mehrjahresantrag` |

## Trade-off-Matrix für die Ersteinordnung

| Entscheidung | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Antrag jetzt vs. Folgejahr | sofort beantragen, BMG steht | warten, mehr Stunden sammeln | sofort, wenn BMG mindestens 100k Euro |
| Ein BSFZ-Antrag vs. Bündel | mehrere Einzelanträge | ein Sammelantrag | Sammelantrag, wenn Vorhaben technisch verwandt |
| Eigenforschung vs. Auftrag | 100 Prozent BMG | 70 Prozent BMG | Eigenforschung, wenn Personal vorhanden |
| Sofortauszahlung vs. Verrechnung | jetzt Liquidität | mit künftiger Steuer verrechnen | Auszahlung in Verlustlagen |

## Zwei-Stufen-Verfahren (Pflicht)

1. **BSFZ-Bescheinigung** (Bescheinigungsstelle Forschungszulage) bescheinigt, dass das Vorhaben FuE im Sinne FZulG/AGVO ist. Sie sagt nichts zur Höhe.
2. **Finanzamt** rechnet auf Basis der Bescheinigung die Bemessungsgrundlage durch, setzt die Forschungszulage fest und verrechnet/erstattet sie.

Ohne BSFZ-Bescheinigung keine Festsetzung. Wer die BSFZ-Stufe unterschätzt, verliert ein Jahr.

## Schritt für Schritt — die ersten 30 Minuten

1. 60-Sekunden-Intake oben durchgehen.
2. Förderchance grob beziffern: FuE-Personalkosten p.a. mal 25 Prozent (bzw. 35 Prozent KMU).
3. Faustregel: Unter 100k Euro FuE-Personalkosten ist der Aufwand selten wirtschaftlich.
4. Engpass identifizieren: fehlt BSFZ-Text, Stundenerfassung, KMU-Nachweis, Auftragsforschungs-Vertrag, AGVO-Kumulierung?
5. Den passenden Skill aus der Verweis-Weiche aktivieren.
6. Wenn Fakten klar genug sind: ersten Entwurf direkt produzieren, nicht nochmal nachfragen.

## Antwortformat

**Kurzbild**

- Vorhaben:
- Zeitraum (offene Wirtschaftsjahre):
- Verfahrensstand (BSFZ/FA):
- Förderchance (grobe Bandbreite):
- Hauptlücke:

**Nächste Schritte**

1. ...
2. ...
3. ...

**Passende Skills**

| Skill | Nutzen | Output |
| --- | --- | --- |
| `...` | ... | ... |

## Typische Fehler beim Einstieg

- Mandant beschreibt das Produkt, nicht das technische Problem. Konsequenz: BSFZ lehnt ab.
- Eigenleistung des Gesellschafter-Geschäftsführers nicht abgegrenzt.
- Zu lange auf "perfekten" BSFZ-Text gewartet, statt parallel die Stundenerfassung aufzubauen.
- Andere Förderungen (ZIM, BMBF) nicht abgefragt, dadurch AGVO-Höchstintensität gerissen.

## Output

- Kurzbild plus Auswahl des passenden Spezialskills.
- Erste grobe Förderchance.
- Liste der unverzichtbaren Eingaben für den Folge-Skill.

## Quellen Stand 05/2026

- FZulG: https://www.gesetze-im-internet.de/fzulg/
- BSFZ: https://www.bescheinigung-forschungszulage.de/
- BMF Forschungszulage: https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Steuerliche_Themengebiete/Forschungszulage/forschungszulage.html
- `references/forschungszulage-quellen-und-zahlen.md`
- Zitierweise: `references/zitierweise.md`

Konkrete Beträge, Fristen und KMU-Definition vom Antragsteller vor Einreichung live mit aktueller Gesetzesfassung und BSFZ-Portal abgleichen.
