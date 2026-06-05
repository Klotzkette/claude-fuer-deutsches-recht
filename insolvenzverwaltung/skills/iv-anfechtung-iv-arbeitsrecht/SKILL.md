---
name: iv-anfechtung-iv-arbeitsrecht
description: "IV Anfechtung IV Arbeitsrecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Anfechtung IV Arbeitsrecht

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Anfechtung IV Arbeitsrecht** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-anfechtung-129ff` | Insolvenzanfechtungsansprüche nach §§ 129-147 InsO aus Verwaltersicht prüfen und verfolgen. Enthält KI-gestütztes Schuldnerakten-Screening, Kandidatenmatrix, §§ 130/131/133/134/135, Bargeschäft § 142, Rechtsfolgen §§ 143-147, Verjährung § 146 und Grenzen bei § 133-Wertungen sowie Dreiecksverhältnissen. |
| `iv-arbeitsrecht-insolvenzgeld` | Personalthemen im Insolvenzverfahren bearbeiten: Lohnrückstaende Insolvenzgeld Kündigungen Betriebsuebergang Betriebsrat. §§ 113 125 InsO § 165 SGB III Insolvenzgeld. Prüfraster: Arbeitnehmerbestand Rückstaende Insolvenzgeldzeitraum Vorfinanzierung Kündigungsfristen Sozialplan. Output: Massnahmenplan Insolvenzgeldanträge Kündigungsschreiben Betriebsratsunterlagen. Abgrenzung: nicht für uebergreifende Betriebsfortführung (iv-sicherung-betriebsfortführung). |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Anfechtung IV Arbeitsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-anfechtung-129ff`

**Fokus:** Insolvenzanfechtungsansprüche nach §§ 129-147 InsO aus Verwaltersicht prüfen und verfolgen. Enthält KI-gestütztes Schuldnerakten-Screening, Kandidatenmatrix, §§ 130/131/133/134/135, Bargeschäft § 142, Rechtsfolgen §§ 143-147, Verjährung § 146 und Grenzen bei § 133-Wertungen sowie Dreiecksverhältnissen.

# Insolvenzanfechtung §§ 129 ff. InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzanfechtung §§ 129 ff. InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `iv-arbeitsrecht-insolvenzgeld`

**Fokus:** Personalthemen im Insolvenzverfahren bearbeiten: Lohnrückstaende Insolvenzgeld Kündigungen Betriebsuebergang Betriebsrat. §§ 113 125 InsO § 165 SGB III Insolvenzgeld. Prüfraster: Arbeitnehmerbestand Rückstaende Insolvenzgeldzeitraum Vorfinanzierung Kündigungsfristen Sozialplan. Output: Massnahmenplan Insolvenzgeldanträge Kündigungsschreiben Betriebsratsunterlagen. Abgrenzung: nicht für uebergreifende Betriebsfortführung (iv-sicherung-betriebsfortführung).

# Arbeitsrecht, Personal und Insolvenzgeld

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Arbeitsrecht, Personal und Insolvenzgeld` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Bearbeitet Personalthemen in Insolvenzverfahren: Lohnrückstände, Insolvenzgeld, Fortführung, Kündigung, Betriebsrat, Betriebsübergang und Haftungsrisiken.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Arbeitnehmer vorhanden sind
- Lohnrückstände, Insolvenzgeld oder Kündigungen anstehen
- Betriebsfortführung mit Personal geplant ist

## Eingaben

- Personalliste, Lohnjournal, Verträge
- Betriebsrat, Tarifbindung, Arbeitszeitdaten
- Fortführungs- oder Stilllegungsplan

## Workflow

1. **Bestand erfassen** - Arbeitnehmer, Rückstände, Sonderrechte, Betriebsrat und Schlüsselpersonen kartieren.
2. **Insolvenzgeld** - Zeitraum, Vorfinanzierung, Anträge und Kommunikation planen.
3. **Maßnahmen** - Fortführung, Kündigung, Transfer, Betriebsübergang und Sozialplan prüfen.
4. **Kommunikation** - Arbeitnehmerinformation und Rückfragen vorbereiten.

## Ausgabe

- Personalmatrix
- Insolvenzgeld-Check
- Maßnahmen- und Kommunikationsplan

## Qualitätsgates

- Lohnarten und Zeiträume getrennt
- Betriebsrat eingebunden, wenn erforderlich
- keine arbeitsrechtliche Maßnahme ohne Fristprüfung

## Rote Schwellen

- Masselöhne ohne Deckung
- Betriebsänderung
- Schlüsselpersonen verlassen Betrieb

## Interne Vorlagen

- assets/templates/personal-insolvenzgeld.md
- assets/templates/betriebsfortfuehrung-wochenplan.md

## Amtliche Erstquellen

- InsO und SGB III als Schnittstelle
- § 113 InsO als zu prüfende Norm

## Rechtliche Grundlagen und BGH-/BSG-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 122/23 vom 05.12.2024** — Bei Anfechtung vorinsolvenzlicher Lohnzahlungen: Unlauterkeit beim Bargeschäft (§ 142 InsO) konkret nachweisen; keine starre 30-Tage-Grenze, sondern enger zeitlicher Zusammenhang. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- BSG- und LSG-Linien zu § 165 SGB III (Insolvenzgeld), insbesondere zur Vorfinanzierung (§ 170 SGB III) und zur Cessio Legis (§ 169 SGB III), vor Ausgabe über sozialgerichtsbarkeit.de oder dejure.org verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
