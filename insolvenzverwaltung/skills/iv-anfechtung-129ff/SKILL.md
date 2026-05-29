---
name: iv-anfechtung-129ff
description: "Insolvenzanfechtungsansprüche nach §§ 129-147 InsO aus Verwaltersicht prüfen und verfolgen. Enthält KI-gestütztes Schuldnerakten-Screening, Kandidatenmatrix, §§ 130/131/133/134/135, Bargeschäft § 142, Rechtsfolgen §§ 143-147, Verjährung § 146 und Grenzen bei § 133-Wertungen sowie Dreiecksverhältnissen."
---

# Insolvenzanfechtung §§ 129 ff. InsO

## Aufgabe

Dieser Skill prüft und verfolgt Insolvenzanfechtungsansprüche aus Sicht des Insolvenzverwalters. Er kann Schuldnerakten KI-gestützt vorsortieren, ersetzt aber keine fachliche Endprüfung bei wertenden Fragen.

## Startet bei

- Zahlungen, Sicherheiten oder Verrechnungen vor Insolvenzantrag auffällig sind.
- Kontoauszüge, OPOS, E-Mails und Schuldnerakten auf Anfechtungskandidaten durchsucht werden sollen.
- Anfechtungsschreiben, Klage, Vergleich oder Gläubigerausschuss-Vorlage vorbereitet wird.

## Eingaben

- Antragsdatum, Eröffnungsbeschluss und Verwalterbestellung.
- Kontoauszüge, Zahlungsjournal, OPOS, Kreditoren-/Debitorenkonten.
- Verträge, Sicherheiten, Ratenzahlungsvereinbarungen, Mahnungen, Vollstreckungen.
- Unterlagen zu Zahlungsunfähigkeit, Sanierung, Liquiditätsstatus und Gesellschafterfinanzierung.

## Workflow

### 1. KI-Screening nur beleggebunden

Erstelle eine Kandidatenliste aus der Akte. Jede Tatsache braucht eine Quelle.

| ID | Datum | Empfänger | Betrag | Vorgang | Quelle | Erstnorm |
|---|---:|---|---:|---|---|---|
| IA-001 | [...] | [...] | [...] EUR | Zahlung | Kontoauszug [...] | § 130 InsO |

KI darf Kandidaten markieren und Belege sortieren. KI darf insbesondere bei § 133 InsO keinen Benachteiligungsvorsatz als bewiesen behaupten, sondern nur Indizien und Gegenindizien ausgeben.

### 2. Tatbestandsrouting

| Sachverhalt | Norm |
|---|---|
| geschuldete Sicherung oder Befriedigung | § 130 InsO |
| nicht geschuldete, nicht so geschuldete oder vorzeitige Deckung | § 131 InsO |
| unmittelbar nachteilige Nicht-Deckungshandlung | § 132 InsO |
| Benachteiligungsvorsatz und Kenntnis | § 133 InsO |
| objektiv unentgeltliche Leistung | § 134 InsO |
| Gesellschafterdarlehen oder gleichgestellte Forderung | § 135 InsO |
| gleichwertiger unmittelbarer Austausch | § 142 InsO als Verteidigung |
| Rückgewähr, Gegenleistung, Rechtsnachfolger, Verjährung | §§ 143-147 InsO |

### 3. § 133 Human Review

Bei § 133 InsO zwingend getrennt ausgeben:

- belegte Zahlungsunfähigkeit oder drohende Zahlungsunfähigkeit.
- Kenntnis des Empfängers.
- Sanierungs- oder Vollbefriedigungsperspektive.
- Zahlungsvereinbarung und § 133 Abs. 3 S. 2 InsO.
- Bargeschäft und erkannte Unlauterkeit nach § 142 InsO.

**Pflicht-Zitate (Stand Mai 2026):**

- **BGH IX ZR 72/20 vom 06.05.2021** — Grundsatzentscheidung Neuausrichtung Vorsatzanfechtung; aus bloßer Zahlungsunfähigkeit allein kein Schluss auf Vorsatz iSd § 133 Abs. 1 InsO.
- **BGH IX ZR 129/22 vom 18.04.2024** — Bestätigung: Verwalter muss konkret darlegen, dass der Schuldner wusste oder billigend in Kauf nahm, andere Gläubiger zu späterer Zeit nicht vollständig zu befriedigen. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 122/23 vom 05.12.2024** — Konkretisierung Unlauterkeit § 142 Abs. 1 Hs. 2 InsO: erfordert gezielt schädigendes Verhalten oder gezielte Bevorzugung; bloße Verlustsituation genügt nicht. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>

### 4. Dreiecksverhältnisse markieren

Human Review ist zwingend bei:

- Drittzahlungen, Cash-Pooling, Zentralregulierung.
- Factoring, Globalzession, Kontokorrent, Aufrechnung.
- Drittdarlehen mit Gesellschaftersicherheit.
- Treuhand, Anderkonto, Sicherheitenpool.

Die Ausgabe muss dann Beteiligte, Forderungswege, Vermögensabfluss und offene Rechtsfragen getrennt darstellen.

### 5. Anspruch und Wirtschaftlichkeit

Rechne nicht nur den Nominalbetrag. Prüfe:

- Rückgewährbetrag nach § 143 InsO.
- Zinsen nur bei Verzug oder nach § 291 BGB.
- Gegenleistung und Wiederaufleben nach § 144 InsO.
- Verjährung nach § 146 InsO in Verbindung mit BGB.
- Prozesskosten, Beweisrisiko und Vergleichskorridor.
- Wirtschaftlichkeitsschwelle: nach BGH IX ZR 129/22 (18.04.2024) sind die Erfolgsaussichten bei kongruenten Deckungen geringer; Vergleichsquote 30 – 60 % typisch.

## Ausgabe

- Anfechtungsmatrix.
- Beleg- und Lückenliste.
- Anspruchsberechnung.
- Entwurf Anfechtungsschreiben oder Klagegerüst.
- Human-Review-Liste für § 133 und komplexe Strukturen.

## Qualitätsgates

- kein Tatbestand ohne Rechtshandlungsdatum.
- keine § 130-Prüfung ohne Kenntnisblock.
- keine § 133-Bewertung ohne Indizien- und Gegenindizienmatrix.
- kein Bargeschäft ohne Gegenleistung und Unmittelbarkeit.
- keine Zinsen ohne Verzug oder Rechtshängigkeit.
- keine finale KI-Bewertung bei Dreiecksverhältnis.

## Interne Vorlagen

- `assets/templates/anfechtungsmatrix-129ff.md`
- `assets/templates/anfechtungsschreiben.md`

---

Hinweis: Keine Rechtsberatung. Die KI kann Anfechtungsrisiken aus Akten sichtbar machen; die rechtliche Endentscheidung bleibt Fachprüfung.
