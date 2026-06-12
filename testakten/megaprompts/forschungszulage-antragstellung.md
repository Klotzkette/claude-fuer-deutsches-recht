# Megaprompt: forschungszulage-antragstellung

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 85 Skills des Plugins `forschungszulage-antragstellung`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Forschungszulage FZulG: ordnet Rolle (Unternehmen F&E, BSFZ, Finanzamt), markiert Frist…
2. **kaltstart-triage** — Adaptiver Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Führt Einsteiger, Technikteams, CFOs und Steu…
3. **abgrenzung-compliance** — Abgrenzung: Compliance-Dokumentation und Aktenvermerk im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragen…
4. **ablehnung-nachbesserung-einspruch** — Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-…
5. **adaptiver-dokumentenmatrix** — Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die f…
6. **antrag-zahlen-schwellenwerte** — Antrag: Zahlen, Schwellenwerte und Berechnung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Perso…
7. **beihilfen-beweislast-darlegungslast** — Beihilfen: Beweislast, Darlegungslast und Substantiierung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fr…
8. **bemessungsgrundlage-2026** — Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je S…
9. **bemessungsgrundlage-interessen** — Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix im Forschungszulage-Antragstellung: 1. Welche Rolle hat d…
10. **betriebspruefung-strategie** — Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn kein…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Forschungszulage FZulG: ordnet Rolle (Unternehmen F&E, BSFZ, Finanzamt), markiert Frist (Antrag jederzeit), wählt Norm (FZulG, EStG § 3 Nr. 26b) und Zuständigkeit (Bescheinigungsstelle Forschungszulage (BSFZ)), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Forschungszulage Antragstellung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abgrenzung-adaptiver-antrag` — Abgrenzung Adaptiver Antrag
- `abgrenzung-compliance` — Abgrenzung Compliance
- `ablehnung-nachbesserung-einspruch` — Ablehnung Nachbesserung Einspruch
- `adaptiver-dokumentenmatrix` — Adaptiver Dokumentenmatrix
- `adaptiver-dokumentenmatrix-und-lueckenliste` — Adaptiver Dokumentenmatrix und Lueckenliste
- `antrag-zahlen-schwellen-und-berechnung` — Antrag Zahlen Schwellen und Berechnung
- `antrag-zahlen-schwellenwerte` — Antrag Zahlen Schwellenwerte
- `antragstellung-auszahlung-beihilfen` — Antragstellung Auszahlung Beihilfen
- `auftragsforschung-vertragsgestaltung` — Auftragsforschung Vertragsgestaltung
- `auszahlung-internationaler-bezug` — Auszahlung Internationaler Bezug
- `auszahlung-internationaler-bezug-und-schnittstellen` — Auszahlung Internationaler Bezug und Schnittstellen
- `beihilfen-beweislast-darlegungslast` — Beihilfen Beweislast Darlegungslast
- `beihilfen-beweislast-und-darlegungslast` — Beihilfen Beweislast und Darlegungslast
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Forschungszulage Antragstellung sind FZulG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Adaptiver Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Führt Einsteiger, Technikteams, CFOs und Steuerberater unterschiedlich, klärt Unternehmen, FuE-Vorhaben, Wirtschaftsjahre, BSFZ-Status, Finanzamt-Antrag, Liquidität, Dokumentation und Fachmodule und liefert sofort Kurzbild_

# Forschungszulage — Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Forschungszulage Antragstellung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Worum geht es

Die Forschungszulage nach FZulG ist eine rückzahlungsfreie steuerliche Förderung (Steuergutschrift) für Aufwendungen aus eigenen oder beauftragten FuE-Vorhaben. Sie wird beim Finanzamt festgesetzt, gegen die nächste Einkommen- oder Körperschaftsteuer aufgerechnet; ein Überschuss wird ausgezahlt. Das macht sie für Verlust- und Krisenphasen besonders wertvoll.

Kerneckdaten Stand 2026 (vom Mandanten/Antragsteller mit aktueller Gesetzesfassung und BSFZ-Portal zu verifizieren):

- Fördersatz grundsätzlich 25 Prozent der Bemessungsgrundlage. KMU-Erhöhung um 10 Prozentpunkte unter bestimmten Voraussetzungen.
- Bemessungsgrundlage ab 01.01.2026 maximal 12 Mio. Euro jährlich.
- Eigenleistung des Einzelunternehmers/Gesellschafter-Geschäftsführers: ab 2026 100 Euro je Arbeitsstunde, höchstens 40 Stunden je Woche.
- Auftragsforschung im EU/EWR-Raum mit 70 Prozent der Kosten ansatzfähig.
- Zusätzliche Gemein- und Betriebskostenpauschale 20 Prozent für nach dem 31.12.2025 begonnene Vorhaben.

Konkrete Werte und Fristen aus `references/forschungszulage-quellen-und-zahlen.md` und Live-Prüfung Gesetz/BSFZ/BMF.

## Wann dieses Modul hilft

Sie greifen zu `forschungszulage-antragstellung-allgemein`, wenn:

- Das Mandat erstmals an FZulG-Beratung herangeführt wird.
- Unklar ist, ob ein einzelnes Vorhaben überhaupt FuE ist und ob sich der Aufwand lohnt.
- Mehrere Spezialfragen gleichzeitig auf dem Tisch liegen (BSFZ-Text, Personalkosten, Krise, Einspruch) und Sie eine Reihenfolge brauchen.
- Ein bestehender Antrag stockt und Sie das richtige Anschluss-Skill suchen.

## Adaptiver Modus

Immer zuerst erkennen, wer vor Ihnen sitzt:

| Modus | Erkennbar an | Arbeitsweise |
| --- | --- | --- |
| **Einsteiger / Geschäftsführung** | "Wir entwickeln etwas, keine Ahnung ob förderfähig" | Fachwörter übersetzen, maximal sechs Fragen, sofort grobe Förderchance und Unterlagenliste |
| **Technikteam** | konkrete Entwicklungsprobleme, keine Steuerlogik | aus technischen Risiken BSFZ-Sprache bauen, keine Steuerparagrafen auswalzen |
| **CFO / Steuerberatung** | Kosten, Jahre, Liquidität, Vorauszahlungen | Berechnung, Cashflow, Fristen, Belege, Finanzamt-Route |
| **Krisenmodus** | Verlust, Insolvenz, Liquiditätsloch | § 10 FZulG, Vorauszahlungssenkung, Masse/Aufrechnung/Abtretung, schnelle Dokumentenliste |
| **Ablehnung / Nachforderung** | BSFZ-Rückfrage, negativer Bescheid | Fehlerursache trennen: FuE-Inhalt, Form, Kosten, Belege, Einspruch/Nachbesserung |

Das Plugin soll aus chaotischem Input eine arbeitsfähige Förderstory machen: Problem, Neuheit, Unsicherheit, planmäßiges Vorgehen, Kosten, Belege. Anfänger bekommen Führung; Profis bekommen eine knappe Ampel und Entscheidungsoptionen.

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
- **BSFZ-Sprache ist knapp.** Das Portal will keine 20-Seiten-Story, sondern eine präzise technische Erzählung mit harten Zeichenbudgets. Erst intern ausführlich denken, dann portaltauglich verdichten.

## Verweis-Weiche — der passende Skill

| Anliegen | Skill |
| --- | --- |
| Erste Förderchance grob abschätzen | `fz-foerdercheck-kaltstart` |
| FuE-Eigenschaft sauber abgrenzen (Frascati) | `fz-fue-definition-frascati-abgrenzung` |
| BSFZ-Projektbeschreibung schreiben | `fz-bsfz-bescheinigung-projektbeschreibung` |
| Plädoyer / Begründung für BSFZ, Finanzamt, Einspruch oder Geschäftsführung | `fz-plaedoyer-begruendung-und-verteidigung` |
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
| Antrag jetzt vs. Folgejahr | sofort beantragen, BMG steht | warten, mehr Stunden sammeln | sofort bei klarer FuE und vorhandenen Belegen; kleine Vorhaben schlank abwickeln |
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
3. Wirtschaftlichkeit prüfen: Auch kleine Vorhaben können sinnvoll sein, wenn Stunden ohnehin dokumentiert sind; bei sehr geringem Aufwand schlanken Antrag bauen statt Beraterprojekt aufblasen.
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

**Intelligenzschicht**

- Einsteiger-Erklärung in drei Sätzen:
- Technische FuE-Story in vier Bausteinen:
- Cashflow-Effekt grob:
- Schnellster sauberer Antragspfad:
- Risiko, das vor Einreichung repariert werden muss:

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

## Normenanker

Arbeitsfokus: **Forschungszulage — Allgemein**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Quellen Stand 05/2026

- FZulG: https://www.gesetze-im-internet.de/fzulg/
- BSFZ: https://www.bescheinigung-forschungszulage.de/
- BMF Forschungszulage: https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Steuerliche_Themengebiete/Forschungszulage/forschungszulage.html
- `references/forschungszulage-quellen-und-zahlen.md`
- Zitierweise: `references/zitierweise.md`

Konkrete Beträge, Fristen und KMU-Definition vom Antragsteller vor Einreichung live mit aktueller Gesetzesfassung und BSFZ-Portal abgleichen.

---

## Skill: `abgrenzung-compliance`

_Abgrenzung: Compliance-Dokumentation und Aktenvermerk im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist..._

# Abgrenzung: Compliance-Dokumentation und Aktenvermerk

## Normenanker

Arbeitsfokus: **Abgrenzung: Compliance-Dokumentation und Aktenvermerk**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Abgrenzung: Compliance-Dokumentation und Aktenvermerk
- **Normen-/Quellenanker:** FZulG, BSFZ, FZ.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Abgrenzung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 FZulG
- § 10 FZulG
- § 2 FZulG
- § 5 FZulG
- § 4 FZulG
- § 6 FZulG
- § 1 FZulG
- § 70 VwG
- § 7 FZulG
- § 9 FZulG
- § 28 VwVfG
- § 37 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `ablehnung-nachbesserung-einspruch`

_Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-Widerspruch, Finanzamt-Kürzung, Einspruch nach AO, neue Tatsachen, Beleg- und Textreparatur, Klage Finanzgericht als Ultima Ratio. Mit Fristenmatrix, Reparaturplan und Mustertex..._

# Ablehnung, Nachbesserung, Einspruch

## Worum geht es

Ablehnungen und Nachforderungen kommen vor — die häufigsten Gründe sind nicht "verlorene Fälle", sondern reparable Schwächen in der Projektbeschreibung oder der Belegfähigkeit. Dieser Skill trennt sauber die beiden Ebenen (BSFZ vs. Finanzamt), führt durch den Reparaturprozess, sichert Fristen und liefert Mustertexte.

## Wann dieses Modul hilft

- Bei BSFZ-Rückfrage oder ablehnender Bescheinigung.
- Bei Finanzamt-Bescheid mit Kürzung oder Ablehnung.
- Vor jedem Einspruch.
- Wenn unklar ist, welche Ebene den Bescheid kritisiert (BSFZ vs. Finanzamt).

## Sachrahmen — die zwei Ebenen sauber trennen

| Ebene | Prüft | Rechtsbehelf |
| --- | --- | --- |
| BSFZ | FuE-Eigenschaft des Vorhabens | Widerspruch / neuer Antrag (vom Antragsteller mit BSFZ-Verfahrensregeln zu prüfen) |
| Finanzamt | Höhe, Personalkosten, Bemessungsgrundlage, Festsetzung | Einspruch nach § 347 ff. AO; Klage Finanzgericht |

Einspruchsfrist beim Finanzamt grundsätzlich **ein Monat** ab Bekanntgabe (§ 355 AO — vom Antragsteller mit konkreter Fassung zu prüfen).

## Praxisleitfaden — die häufigsten Ablehnungsgründe

### BSFZ — typische Ablehnungs-/Rückfrage-Gründe

- **Fehlende Neuheit.** "Stand der Technik nicht ausreichend zitiert" / "Vorhaben deckt sich mit bestehenden Verfahren".
- **Unzureichende Beschreibung der Unsicherheit.** Risiko nur allgemein erwähnt, nicht spezifiziert.
- **Routine-Verdacht.** Vorhaben ähnelt zu sehr Wartung, Customizing, Serienpflege.
- **Mangelhafte Abgrenzung.** Routine-Anteile sind im Vorhaben enthalten oder nicht offen gelegt.
- **Marketing-Sprache** ohne technischen Inhalt.

### Finanzamt — typische Kürzungs-/Ablehnungsgründe

- **Personalkosten-Höhe** zweifelhaft: Bruttoansätze, SV-Beiträge, Altersvorsorge nicht ausreichend belegt.
- **FuE-Anteilberechnung** nicht plausibel: keine Stundenaufzeichnung, nur Pauschalannahmen.
- **Auftragsforschung:** Auftragnehmer außerhalb EU/EWR, Vertrag fehlt Leistungsbeschreibung, 70-Prozent-Kürzung nicht angewandt.
- **Eigenleistung:** Gesellschafter-Geschäftsführer doppelt (Lohn + Eigenleistung), 40-Stunden-Cap überschritten.
- **AGVO-Kumulierung:** Höchstintensität überschritten.
- **Wirtschaftsjahr-Zuordnung:** Aufwendungen falschem Jahr zugeordnet.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| BSFZ-Widerspruch vs. neuer Antrag | gleiche AZ-Linie | sauberer Neustart | neuer Antrag, wenn grundlegende Schwächen |
| Nachbesserung vs. Einspruch | informeller Dialog | förmlicher Rechtsbehelf | Nachbesserung zuerst, Einspruch fristwahrend |
| Klage Finanzgericht vs. Verhandlungslösung | grundsätzlich klären | pragmatische Einigung | Verhandlung bevorzugen, Klage Ultima Ratio |
| Vollständige Neufassung vs. Stellungnahme | hoher Aufwand, hohe Erfolgsquote | niedriger Aufwand, geringeres Ergebnis | Neufassung bei tragenden Schwächen |

## Fristen — die wichtigsten Daten

| Vorgang | Frist | Hinweis |
| --- | --- | --- |
| Einspruch Finanzamt-Bescheid | grundsätzlich 1 Monat ab Bekanntgabe | § 355 AO; Bekanntgabefiktion § 122 AO; vom Antragsteller live zu prüfen |
| Klage Finanzgericht | 1 Monat nach Einspruchsentscheidung | § 47 FGO |
| BSFZ-Rückfrage | Frist im Rückfragebrief der BSFZ | unbedingt einhalten, sonst Ablehnung |
| BSFZ-Widerspruch | nach Maßgabe des Bescheinigungsbescheids | Antragsteller mit Bescheid abgleichen |

## Schritt für Schritt — Reparaturplan

1. Bescheid / Rückforderung vollständig auswerten: was wird gerügt, auf welcher Ebene?
2. Ebene zuordnen (BSFZ vs. Finanzamt).
3. Frist eintragen, Mahnung im Kalender setzen.
4. Konkret rugierte Punkte auflisten.
5. Reparatur planen:
 a. Welche Tatsachen sind ergänzungsfähig?
 b. Welche Belege fehlen?
 c. Welche Formulierungen sind missverständlich?
6. Bei BSFZ: ergänzende Stellungnahme oder neuer Antrag.
7. Bei Finanzamt: Einspruch fristwahrend einlegen, Begründung folgt.
8. Verhandlungsgespräch mit Sachbearbeiter prüfen.
9. Bei Stillstand: Klage Finanzgericht erst nach gescheiterter Einspruchsentscheidung.

## Mustertexte

**Einspruch Finanzamt (fristwahrend):**

"Sehr geehrte Damen und Herren,

namens und in Vollmacht der [Mandantin] lege ich gegen den Forschungszulagenbescheid vom [Datum], Steuernummer [...], Einspruch ein.

Die Begründung folgt nach Akteneinsicht. Wir bitten um vorläufige Aussetzung der Vollziehung gemäß § 361 AO, soweit die Festsetzung über den unstreitigen Teil hinausgeht. Akteneinsicht wird beantragt.

Mit freundlichen Grüßen [Berufsbezeichnung]."

**Stellungnahme an BSFZ (Vorlage, bei Rückfrage zur Neuheit):**

"Sehr geehrte Damen und Herren,

zur Rückfrage vom [Datum] in Sachen Antrag [AZ] nehmen wir wie folgt Stellung:

1. Stand der Technik: Wir ergänzen die Quellen [neue Quellen 1, 2]. Die Recherche zeigt, dass die spezifische Kombination [A] mit [B] dort nicht beschrieben ist.

2. Neuheit: Die Neuheit liegt in [konkretes technisches Merkmal]. Im Unterschied zum Stand der Technik [Punkt 1, Punkt 2].

3. Technische Unsicherheit: [konkrete Hürde, Voruntersuchungen, vergleichbare gescheiterte Vorhaben].

4. Abgrenzung zur Routine: Folgende Tätigkeiten gehören nicht zum Vorhaben: [Aufzählung].

Mit freundlichen Grüßen [Verfasser]."

**Reparaturplan-Tabelle:**

| Kritikpunkt | Ebene | Reparatur | Belegnachschub | Fristtag |
| --- | --- | --- | --- | --- |
| Stand der Technik unzureichend | BSFZ | zwei Quellen ergänzen | Patentrecherche | TT.MM.JJJJ |
| Personalkosten nicht belegt | FA | Lohnkonten beifügen | Lohnabrechnung 12/JJJJ | TT.MM.JJJJ |
| FuE-Anteil zu hoch | FA | Stundenaufzeichnung beifügen | Auszug aus Zeiterfassung | TT.MM.JJJJ |

## Typische Fehler

- Frist versäumt, weil Einspruch erst nach interner Beratung formuliert wurde — Einspruch fristwahrend einlegen, Begründung nachreichen.
- BSFZ und Finanzamt verwechselt — Einspruch bei der falschen Stelle.
- Inhaltliche Neufassung statt sachlicher Stellungnahme — wirkt unkooperativ.
- Belege ohne Bezug zum konkreten Kritikpunkt eingereicht.
- Klage Finanzgericht vor Einspruchsentscheidung erhoben.

## Quellen Stand 05/2026

- AO §§ 347 bis 367 (Einspruchsverfahren) und § 355 AO (Frist) — vom Antragsteller mit konsolidierter Fassung zu prüfen.
- FGO § 47 (Klagefrist).
- BSFZ-Verfahrensregeln.
- FZulG.
- `references/forschungszulage-quellen-und-zahlen.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 FZulG
- § 10 FZulG
- § 2 FZulG
- § 5 FZulG
- § 4 FZulG
- § 6 FZulG
- § 1 FZulG
- § 70 VwG
- § 7 FZulG
- § 9 FZulG
- § 28 VwVfG
- § 37 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `adaptiver-dokumentenmatrix`

_Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstuf..._

# Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung

## Normenanker

Arbeitsfokus: **Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung
- **Normen-/Quellenanker:** FZulG, BSFZ.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Adaptiver** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 FZulG
- § 10 FZulG
- § 2 FZulG
- § 5 FZulG
- § 4 FZulG
- § 6 FZulG
- § 1 FZulG
- § 70 VwG
- § 7 FZulG
- § 9 FZulG
- § 28 VwVfG
- § 37 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `antrag-zahlen-schwellenwerte`

_Antrag: Zahlen, Schwellenwerte und Berechnung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisc..._

# Antrag: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: Antrag: Zahlen, Schwellenwerte und Berechnung
- **Normen-/Quellenanker:** FZulG, BSFZ.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Antrag** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## FZulG-Bemessungsgrundlage und Höchstgrenzen (vor Ausgabe live verifizieren)

| Position | Norm | Hinweis |
|---|---|---|
| Lohnaufwendungen FuE-Personal | § 3 Abs. 1, 2 FZulG | tatsächlich gezahlte sv-pflichtige Bruttolöhne der im Vorhaben tätigen Mitarbeiter, anteilig nach FuE-Zeit |
| Personalnebenkosten-Pauschale | § 3 Abs. 1 FZulG | + 25 % auf Lohnaufwendungen |
| Auftragsforschung | § 3 Abs. 4 FZulG | 70 % der entrichteten Entgelte für FuE-Auftragsforschung an Dritte mit Sitz im EWR |
| Eigenleistung Einzelunternehmer / Mitunternehmer | § 3 Abs. 3 FZulG | pauschal 70 EUR/Std., maximal 40 Std./Woche |
| Maximale Bemessungsgrundlage pro Jahr | § 3 Abs. 5 FZulG | ab 2024/2025 auf 10 Mio. EUR erhöht - vor Ausgabe verifizieren auf gesetze-im-internet.de |
| Zulagensatz | § 4 FZulG | regelmäßig 25 % der Bemessungsgrundlage; KMU + 10 % auf Antrag (insgesamt 35 %) |

## KMU-Definition

KMU im Sinne des FZulG nach AGVO (EU) 651/2014 Anhang I:
- < 250 Mitarbeiter UND
- Jahresumsatz <= 50 Mio. EUR ODER Jahresbilanzsumme <= 43 Mio. EUR
- Beteiligungsverhältnisse über 25 % aggregieren (Partnerunternehmen, verbundene Unternehmen)

## Praktischer Tipp

- **Personalzuordnung FuE-Zeit ist der zentrale Streitpunkt mit der Außenprüfung**. Lösung: Stundennachweise (Excel reicht, wenn lückenlos, datiert, mit Vorhaben-Nummer). Pauschale Schätzungen ("der Mitarbeiter macht zu 60 % FuE") werden bei Prüfungen regelmäßig gekürzt.
- **Auftragsforschung 70 %**: nicht 100 % der Rechnung, sondern 70 % als förderfähig. Das ist eine harte Pauschale - kein Spielraum.
- **Eigenleistung Einzelunternehmer / Mitunternehmer**: 70 EUR/Std. ist eine Pauschale, nicht der tatsächliche Stundensatz. Maximal 40 Std./Woche, d.h. 2.080 Std./Jahr × 70 EUR = 145.600 EUR p.a. (vor Ausgabe verifizieren).

## Beispiel-Berechnung

> FuE-Personal Lohnaufwand: 4 Mitarbeiter × 60 % FuE-Zeit × jeweils 80.000 EUR Bruttolohn = 192.000 EUR
> + Personalnebenkosten-Pauschale 25 %: + 48.000 EUR
> = 240.000 EUR förderfähig aus Lohn
>
> Auftragsforschung: Dritter im EWR, Rechnung 100.000 EUR (FuE-Anteil unstreitig) × 70 % = 70.000 EUR förderfähig
>
> Eigenleistung Einzelunternehmer: 800 Std. × 70 EUR = 56.000 EUR förderfähig
>
> Bemessungsgrundlage gesamt: 240.000 + 70.000 + 56.000 = 366.000 EUR
> Forschungszulage bei 35 % (KMU): 128.100 EUR
>
> Verrechnung gegen Körperschaftsteuer; soweit KSt < 128.100 EUR, Auszahlung des überschießenden Betrags nach § 10 Abs. 1 Satz 4 FZulG.

## Typische Fehler

- 100 % der Auftragsforschung angesetzt statt 70 %.
- KMU-Status nicht geprüft - bei Konzernzugehörigkeit unter 250 Mitarbeiter, aber Mutter > 250: kein KMU.
- Personalzuordnung pauschal - bei Außenprüfung Kürzung.
- Eigenleistung Einzelunternehmer ohne Stundennachweis - Pauschale wird gekürzt.

---

## Skill: `beihilfen-beweislast-darlegungslast`

_Beihilfen: Beweislast, Darlegungslast und Substantiierung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe..._

# Beihilfen: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Beihilfen: Beweislast, Darlegungslast und Substantiierung
- **Normen-/Quellenanker:** FZulG, BSFZ.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Beihilfen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Beihilferechtlicher Rahmen FZulG

- Die Forschungszulage ist eine staatliche Beihilfe nach Art. 107 AEUV, die unter die Allgemeine Gruppenfreistellungsverordnung (EU) 651/2014 (AGVO), Artikel 25 fällt: "Beihilfen für Forschungs- und Entwicklungsvorhaben".
- Bei Kumulierung mit anderen staatlichen Beihilfen (Bundes-/Landes-Förderungen, EU-Mittel) sind die Höchstintensitäten nach AGVO Art. 25 Abs. 5-7 einzuhalten:

| FuE-Phase | Höchstintensität (AGVO Art. 25 Abs. 5) | KMU-Bonus |
|---|---|---|
| Grundlagenforschung | 100 % | - |
| Industrielle Forschung | 50 % | + 10 % mittlere Unternehmen, + 20 % Kleinunternehmen |
| Experimentelle Entwicklung | 25 % | + 10 % mittlere, + 20 % Kleinunternehmen |
| Durchführbarkeitsstudien | 50 % | + 10 % mittlere, + 20 % Kleinunternehmen |

## Norm-Bezug konkret

- Art. 107, 108 AEUV: Beihilferahmen.
- AGVO (EU) 651/2014, Art. 25, 28: Vereinbarkeit FuE-Beihilfen / Beihilfen für KMU.
- § 1 Abs. 1 FZulG: Vereinbarkeit mit AGVO als Grundvoraussetzung.
- De-minimis-Verordnung (EU) 2023/2831: irrelevant für FZulG (FZulG fällt unter AGVO, nicht unter De-minimis).
- VO (EU) 1407/2013 (alt) bzw. neue De-minimis-VO: nur für Kumulierung mit De-minimis-Beihilfen relevant.

## Darlegungslast bei Kumulierung

| Punkt | Wer trägt Darlegungslast |
|---|---|
| Höchstintensität eingehalten | Steuerpflichtiger (Antragsteller) |
| KMU-Status | Steuerpflichtiger |
| Konzernzugehörigkeit / verbundene Unternehmen | Steuerpflichtiger |
| Andere Förderungen für dasselbe Vorhaben | Steuerpflichtiger |
| Abgrenzung Förder-fähig / nicht förder-fähig | Steuerpflichtiger; Finanzamt prüft |

## Praktischer Tipp

- **Kumulierungstabelle führen**: pro Vorhaben alle staatlichen Beihilfen mit Quellangabe, Betrag, Förderintensität. Spätestens bei Außenprüfung wird das verlangt.
- **Pflichtangaben im FZulG-Antrag** zu anderweitigen Förderungen: § 9 FZulG verlangt vollständige Offenlegung; Verschweigen führt nicht nur zur Rückforderung der FZulG, sondern kann beihilferechtliche Konsequenzen nach Art. 108 AEUV haben (Rückforderung mit Zinsen).
- **Konzernsicht**: AGVO-Höchstintensitäten gelten konzernweit für verbundene Unternehmen i.S.v. Anhang I AGVO. Mutter und FuE-Tochter sind regelmäßig zusammen zu betrachten.

## Beispiel-Kumulierungsrechnung

> FuE-Vorhaben "X" (experimentelle Entwicklung, Höchstintensität 25 % + 10 % mittlere Unternehmen = 35 %)
> Gesamte förderfähige Kosten: 1.000.000 EUR
> Maximale Beihilfe: 350.000 EUR
>
> Bereits bewilligt:
> - ZIM-Zuschuss BMWK: 200.000 EUR (20 %)
> - FZulG (geplant) bei BMG 800.000 EUR × 35 % KMU: 280.000 EUR (28 %)
>
> Summe: 480.000 EUR / 1.000.000 EUR = 48 % - Überschreitung!
>
> Maßnahme: FZulG-Bemessungsgrundlage reduzieren auf BMG (350.000 - 200.000) / 0,35 = 428.571 EUR, sodass Kumulierung bei 350.000 EUR und damit Höchstintensität 35 % bleibt.

## Typische Fehler

- Anderweitige Förderung im FZulG-Antrag nicht angegeben - Verstoß gegen § 9 FZulG, Rückforderungsrisiko.
- AGVO-Höchstintensität konzernweit nicht aggregiert; bei Tochter-Förderung Mutter-Förderung übersehen.
- "De-minimis" mit AGVO-Förderung verwechselt; FZulG fällt grundsätzlich nicht unter De-minimis.

---

## Skill: `bemessungsgrundlage-2026`

_Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, KMU-Erhöhung. Mit Personalkostenformel, Stundenaufzeichnungss..._

# Bemessungsgrundlage 2026

## Worum geht es

Die Höhe der Forschungszulage hängt nicht von der BSFZ ab, sondern allein von den ansatzfähigen Aufwendungen und dem Höchstbetrag der Bemessungsgrundlage (BMG). Liefere die Berechnungslogik, die Personalkostenformel, die Behandlung von Auftragsforschung und Eigenleistung sowie typische Pitfalls.

Stand 2026 — alle Zahlen vom Antragsteller mit aktueller Gesetzesfassung und BMF-Verwaltungsanweisungen abzugleichen.

## Wann dieses Modul hilft

- Vor dem Finanzamt-Antrag, zur belastbaren Berechnung.
- Bei Sanity-Check der ersten Förderhöhenschätzung.
- Bei der Trennung Eigenforschung / Auftragsforschung.
- Wenn Gesellschafter-Geschäftsführer mitarbeitet (Stolperfalle).
- Bei Mehrjahresvorhaben für die jährliche Aufteilung.

## Sachrahmen — BMG-Komponenten und Caps

| Komponente | Ansatz | Maximum/Bedingung |
| --- | --- | --- |
| Eigene FuE-Personalkosten | Bruttolohn + Arbeitgeberanteil zur Sozialversicherung + Altersvorsorge | nur FuE-Anteil je Mitarbeiter |
| Eigenleistung Einzelunternehmer/persönlich tätiger Gesellschafter | ab 2026 pauschal 100 Euro je Arbeitsstunde | max. 40 Stunden je Woche |
| Auftragsforschung | 70 Prozent der Kosten | Auftragnehmer muss seine Geschäftsleitung in EU/EWR haben; bei EWR-Staaten zusätzlich Amtshilfevoraussetzung nach § 2 Abs. 5 FZulG prüfen; klare Leistungsbeschreibung |
| Wirtschaftsgüter | AfA, soweit dem FuE-Vorhaben zuordenbar | bewegliche abnutzbare Wirtschaftsgüter des Anlagevermögens |
| Gemein- und Betriebskosten | pauschal 20 Prozent der übrigen förderfähigen Aufwendungen | nur für Vorhaben mit Beginn nach 31.12.2025 |

**BMG-Höchstbetrag:** ab 01.01.2026 12 Mio. Euro pro Wirtschaftsjahr (verbundene Unternehmen ggf. gemeinsam — vom Antragsteller live zu prüfen).

**Fördersatz:** 25 Prozent; KMU-Erhöhung um 10 Prozentpunkte möglich (Antragstellervoraussetzungen prüfen).

## Praxisleitfaden — Personalkostenformel und Pitfalls

### Personalkostenformel

Förderfähige Personalkosten je Mitarbeiter und Wirtschaftsjahr:

```
PK_je_MA = (Bruttolohn + Arbeitgeber-SV + Altersvorsorge) × FuE-Anteil
```

FuE-Anteil ist der dokumentierte Zeitanteil aus der Stundenaufzeichnung. Pauschale Annahmen ("Herr X arbeitet zu 60 Prozent in der FuE") halten der Außenprüfung nicht stand.

### Beispiel Brutto-TV-L 13 (rein illustrativ; Werte vom Antragsteller mit aktueller Lohnabrechnung zu ersetzen)

- Bruttojahreslohn: 65.000 Euro
- Arbeitgeber-SV ca. 13.000 Euro
- Altersvorsorge ca. 4.500 Euro
- Personalvollkosten 82.500 Euro
- Dokumentierter FuE-Anteil 70 Prozent
- Förderfähig: 82.500 × 0.70 = 57.750 Euro
- Bei 25 Prozent Fördersatz: Zulage 14.437 Euro je Mitarbeiter
- Bei KMU-Erhöhung 35 Prozent: 20.212 Euro

### Stundenaufzeichnung — die Pflichtspalten

| Datum | Person | Vorhaben/AP | Stunden | Tätigkeit (FuE-konkret) | Kürzel Auftrag/Eigen |
| --- | --- | --- | --- | --- | --- |
| 12.03.2026 | M. Müller | V-1 / AP-2 | 6.5 | Aufbau Messreihe Variante A, Kalibrierung | E |
| 12.03.2026 | M. Müller | Service | 1.5 | Wartung Bestandsanlage | N |

- `E` = Eigenforschung, `A` = Auftragsforschung, `N` = nicht FuE.
- Schon dieses Detail genügt vielen Außenprüfern, weil es Konsistenz zur Projektakte zeigt.

### Eigenleistung Einzelunternehmer / persönlich tätiger Gesellschafter

- Pauschale 100 Euro je Stunde, max. 40 Stunden je Woche, ab 2026 (vom Antragsteller mit aktueller Fassung zu prüfen).
- **Pitfall Gesellschafter-Geschäftsführer:** Wer als GmbH-Gesellschafter-Geschäftsführer ein Gehalt bezieht, fällt nicht automatisch in die Eigenleistung. Die Personalkosten werden über die Lohnabrechnung berücksichtigt. Doppelansatz vermeiden.
- **Pitfall Einzelunternehmer:** Eigenleistung ist die einzige Möglichkeit, weil keine Lohnabrechnung existiert.

### Auftragsforschung — die 70-Prozent-Regel

- Förderfähig nur 70 Prozent der Kosten.
- Auftragnehmer muss seine Geschäftsleitung in einem EU-Mitgliedstaat oder in einem EWR-Staat mit ausreichender Amtshilfe nach § 2 Abs. 5 FZulG haben. Eine außerhalb dieses Rahmens ansässige Forschungseinrichtung ist für die Auftragsforschungsregel nicht förderfähig.
- **Klare Leistungsabgrenzung im Vertrag.** Wer was wann mit welchem Ziel.
- Subunternehmer des Auftragnehmers werden mitgeprüft.
- Verbundene Unternehmen sind kritisch — die BSFZ und das Finanzamt prüfen genau, ob es sich nicht doch um eigene FuE im Konzern handelt.

### Wirtschaftsgüter / AfA

- Nur bewegliche, abnutzbare Wirtschaftsgüter des Anlagevermögens.
- Anteilige AfA, soweit dem FuE-Vorhaben zugeordnet.
- Keine Grundstücke, keine Software-Lizenzen mit Sonderregeln (Einzelfall prüfen).

### 20-Prozent-Gemeinkostenpauschale

- Für Vorhaben mit Beginn nach 31.12.2025.
- 20 Prozent der übrigen förderfähigen Aufwendungen (eigene Personalkosten + Eigenleistung + 70-Prozent-Auftrag + AfA).
- Keine Belegpflicht für die Pauschale selbst — die Pauschale ersetzt die Einzelbelegnahme der Gemeinkosten.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Eigenforschung vs. Auftragsforschung | 100 Prozent BMG | 70 Prozent BMG | Eigen bevorzugen, wenn Personal vorhanden |
| Gesellschafter Eigenleistung vs. Lohn | 100 Euro/Std., 40-Stunden-Cap | reguläre Personalkosten | Lohn meist günstiger ab ca. 30 Euro/Std. Vollkosten |
| Vollverteilung vs. konservativ | maximal anteilig | nur dokumentierte Stunden | konservativ; Außenprüfung honoriert das |
| Sammel-AP vs. detaillierte AP | weniger Verwaltung | bessere Nachvollziehbarkeit | detaillierte AP für Außenprüfung |

## Schritt für Schritt

1. Wirtschaftsjahr und Vorhaben festlegen.
2. Pro Mitarbeiter Lohnkosten + SV + Altersvorsorge ermitteln.
3. FuE-Anteil aus Stundenaufzeichnung ermitteln (Stundenzahl FuE / Stundenzahl gesamt).
4. Auftragsforschungskosten aus Rechnungen sammeln, mit 70 Prozent ansetzen.
5. Eigenleistung Einzelunternehmer / persönlich tätiger Gesellschafter mit 100 Euro × dokumentierte Stunden (max. 40/Woche).
6. AfA für Wirtschaftsgüter anteilig zuordnen.
7. Zwischensumme bilden.
8. 20-Prozent-Gemeinkostenpauschale auf die Zwischensumme aufschlagen (sofern Vorhabensbeginn nach 31.12.2025).
9. BMG-Cap prüfen (12 Mio. Euro/Jahr).
10. Fördersatz anwenden (25 Prozent oder 35 Prozent KMU).
11. Drei Szenarien dokumentieren: konservativ / realistisch / maximal.

## Datenqualitäts-Ampel

| Ampel | Datenlage | Behandlung |
| --- | --- | --- |
| Grün | Lohnkonten, Stunden je AP, BSFZ-Bescheid, Verträge/Rechnungen liegen vor | belastbare Berechnung |
| Gelb | Stunden plausibel, aber nacherfasst; Auftragsvertrag lückenhaft | Berechnung mit Risikoabschlag und Nachforderungsplan |
| Rot | nur Managementschätzung, keine AP-Zuordnung, unklare Auftragnehmer | keine Betragszusage; erst Dokumentation reparieren |

## Mustertexte / Vorlagen

**Berechnungstabelle (Vorlage):**

| Komponente | Brutto | Faktor | Förderfähig |
| --- | --- | --- | --- |
| Personalkosten Mitarbeiter A | 82.500 Euro | 70 Prozent | 57.750 Euro |
| Personalkosten Mitarbeiter B | 75.000 Euro | 50 Prozent | 37.500 Euro |
| Eigenleistung Gesellschafter | 100 Euro × 800 Std. | 100 Prozent | 80.000 Euro |
| Auftragsforschung Institut X | 120.000 Euro | 70 Prozent | 84.000 Euro |
| AfA Maschine M-12 | 40.000 Euro | 60 Prozent | 24.000 Euro |
| Zwischensumme | | | 283.250 Euro |
| 20 Prozent Pauschale | | | 56.650 Euro |
| Bemessungsgrundlage | | | 339.900 Euro |
| Forschungszulage 25 Prozent | | | 84.975 Euro |
| Forschungszulage 35 Prozent (KMU) | | | 118.965 Euro |

**Anteilssatz-Plausibilität:** Wenn ein Mitarbeiter zu 90 Prozent in FuE arbeitet, muss in der Stundenaufzeichnung diese Quote nachweisbar sein. Das Finanzamt vergleicht Lohnkonto, Tätigkeitsbeschreibung und Stundenaufzeichnung.

## Typische Fehler

- Vollkosten ohne Stundennachweis hochgerechnet.
- Auftragsforschung mit 100 Prozent statt 70 Prozent angesetzt.
- Gesellschafter-Geschäftsführer doppelt (Lohn + Eigenleistung).
- Auftragsforschung außerhalb EU/EWR mit angesetzt.
- 20-Prozent-Pauschale auf nicht-zulässige Posten angewendet.
- 12-Mio-Cap übersehen bei verbundenen Unternehmen.

## Normenanker

Arbeitsfokus: **Bemessungsgrundlage 2026**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 3 FZulG` — förderfähige Aufwendungen und Bemessungsgrundlage.
- `§ 4 FZulG` — Höhe der Forschungszulage.
- `§ 5 FZulG` — Antragstellung beim Finanzamt.
- `§ 90 Abs. 1 AO` — Mitwirkungspflichten und Belegvorlage.
- `§ 147 Abs. 1 AO` — Aufbewahrung von Buchführungs- und sonstigen Unterlagen.
- `§ 162 Abs. 1 AO` — Schätzung bei lückenhafter Dokumentation.
- `§ 370 AO` — Grenze zur Steuerhinterziehung bei falschen Angaben.
- `Art. 25 AGVO` — Beihilferahmen für Forschungs- und Entwicklungsbeihilfen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Quellen Stand 05/2026

- FZulG, insbesondere §§ 3, 4, 5 (vom Antragsteller mit konsolidierter Fassung zu prüfen).
- Wachstumschancengesetz, Auftragsforschungsregelung 70 Prozent.
- Steuerliches Investitionssofortprogramm 2025/2026: https://www.bescheinigung-forschungszulage.de/steuerliches-investitionssofortprogramm
- `references/forschungszulage-quellen-und-zahlen.md`.

---

## Skill: `bemessungsgrundlage-interessen`

_Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrens..._

# Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix
- **Normen-/Quellenanker:** FZulG, BSFZ.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bemessungsgrundlage** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Mehrparteien-Konstellationen bei FuE

| Konstellation | Wer ist anspruchsberechtigt? | Norm |
|---|---|---|
| Eigene FuE des Steuerpflichtigen | Steuerpflichtiger selbst | § 1 i.V.m. § 3 Abs. 1 FZulG |
| Auftragsforschung: Auftraggeber im Inland zahlt an EWR-Dritten | nur Auftraggeber, 70 % förderfähig | § 3 Abs. 4 FZulG |
| Auftragsforschung: Auftraggeber im Inland zahlt an Nicht-EWR-Dritten | nicht förderfähig | § 3 Abs. 4 FZulG (EWR-Voraussetzung) |
| Kooperation auf Augenhöhe (Joint Venture FuE) | jeder Partner für eigenen Anteil | § 1 FZulG |
| FuE durch beauftragtes Konzernunternehmen | strittig, je nach Vertragsgestaltung | § 3 Abs. 4 FZulG |
| FuE im Rahmen einer Mitunternehmerschaft (KG, GbR) | Personengesellschaft; Eigenleistung Mitunternehmer nach § 3 Abs. 3 FZulG | §§ 1, 3 FZulG |

## Konflikt: Auftragsforschung vs. Kooperation

| Kriterium | Auftragsforschung (§ 3 Abs. 4 FZulG) | Kooperation auf Augenhöhe |
|---|---|---|
| Risiko/Ergebnisverwertung | Auftraggeber trägt Risiko und verwertet | beide Partner anteilig |
| Vertrag | Werkvertrag mit Vergütung | Kooperationsvereinbarung mit Eigenleistung |
| Begünstigung | nur Auftraggeber, 70 % der Vergütung | jeder Partner für eigenen Aufwand zu 100 % |
| Bemessungsgrundlage | Vergütung × 70 % | tatsächlicher Aufwand |

Die Abgrenzung ist wirtschaftlich relevant: bei Kooperationen können beide Partner FZulG ziehen, bei Auftragsforschung nur der Auftraggeber zu 70 % der Rechnungssumme.

## Norm-Bezug konkret

- § 3 Abs. 4 FZulG: Auftragsforschung, EWR-Voraussetzung, 70 %-Pauschale.
- § 3 Abs. 1, 2 FZulG: Eigene FuE.
- § 3 Abs. 3 FZulG: Eigenleistung Einzelunternehmer / Mitunternehmer.
- AGVO (EU) 651/2014, Art. 25: Beihilferechtliche Höchstintensitäten.
- BMF-Schreiben zum FZulG (Datum/AZ vor Ausgabe verifizieren auf bundesfinanzministerium.de): Verwaltungsauffassung zu Auftragsforschung und Konzernsachverhalten.

## Praktischer Tipp

- **Konzern-Auftragsforschung**: Mutter beauftragt FuE-Tochter; ohne klare Marktüblichkeit (Verrechnungspreise nach § 1 AStG) wird die Außenprüfung den Sachverhalt umqualifizieren. Lösung: belastbare Vergleichsstudie + schriftlicher Werkvertrag mit Risiko- und Ergebnisverwertungsklausel.
- **Kooperation auf Augenhöhe**: Schriftlicher Kooperationsvertrag mit klarer Aufwand- und Ergebnisaufteilung. Sonst Vermutung der Auftragsforschung.
- **EWR-Voraussetzung**: bei Auftragsforschung an US-Dienstleister oder UK-Subunternehmer kein FZulG-Förderpfad. Alternative: Lizenz statt Auftragsforschung; oder Auftrag an EWR-Tochter des Dienstleisters.

## Trade-off: Auftragsforschung vs. eigene FuE

| Pfad | Vorteil | Nachteil |
|---|---|---|
| Eigene FuE, eigenes Personal | volle Bemessungsgrundlage, 100 % Lohnaufwand + 25 % Pauschale | Personalaufbau, Bindung |
| Auftragsforschung an EWR-Dritten | flexibel skalierbar, kein Personalrisiko | nur 70 % der Vergütung förderfähig |
| Kooperation auf Augenhöhe | beide Partner ziehen FZulG, dadurch Gesamtförderung höher | Vertraglich anspruchsvoll; Risiko Außenprüfung-Umqualifizierung |

## Typische Fehler

- "Kooperationsvertrag" ist tatsächlich verkappte Auftragsforschung; Außenprüfung qualifiziert um, FZulG-Förderung wird reduziert.
- Konzernverrechnungspreise nicht marktüblich; Steuerprüfung führt zu Doppelschaden (FZulG-Kürzung + AStG-Anpassung).
- Auftragsforschung an britischen Dienstleister nach Brexit weitergegeben - kein EWR mehr, keine Förderung.

---

## Skill: `betriebspruefung-strategie`

_Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn keine Steuerstraftat), Argumentationspakete, Schlussbesprechung. Pruefraster: Stundennachweise, Auftragsforschungsvertraege, Mitarbeiterzuordnung, FuE-Phasentrennung. Routet in fz-d..._

# FZ: Betriebspruefungs-Strategie

## Normenanker

Arbeitsfokus: **FZ: Betriebspruefungs-Strategie**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Spezialwissen: FZ: Betriebspruefungs-Strategie
- **Normen-/Quellenanker:** FZ.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

