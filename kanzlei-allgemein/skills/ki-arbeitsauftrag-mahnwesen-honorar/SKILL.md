---
name: ki-arbeitsauftrag-mahnwesen-honorar
description: "KI Arbeitsauftrag Mahnwesen Honorar: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KI Arbeitsauftrag Mahnwesen Honorar

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **KI Arbeitsauftrag Mahnwesen Honorar** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ki-arbeitsauftrag-briefing` | Kanzleiweiter Skill, der aus einer unklaren Bitte, einem Dokumentenpaket oder einer Sprachnotiz einen praezisen KI-Arbeitsauftrag macht. Klaert Ziel, Kontext, Outputformat, Grenzen, Quellenstandard, Datenschutz, Fristen und Abnahmekriterien. |
| `mahnwesen-honorar` | Mahnwesen für eigene Honorarforderungen der Kanzlei gegenüber Mandanten. Anwendungsfall Mandant hat Rechnung nicht bezahlt und Kanzlei muss mahnen oder klagen. Normen § 286 BGB Verzugsbeginn § 288 BGB Verzugszinsen § 23 Nr. 1 GVG AG-Zuständigkeit bis 10000 EUR ab 01.01.2026 § 688 ff. ZPO Mahnverfahren. Prüfraster Stufen Zahlungserinnerung erste Mahnung zweite Mahnung dritte Mahnung Inkassouebergabe AG-Klage. Output Gestuftes Mahnschreibenpaket mit Verzugszinsen Mahnkosten Klagedrohung und Klageentwurf. Abgrenzung zu forderungsmanagement-klagewerkstatt-Plugin und kanzlei-allgemein-rechnung. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **KI Arbeitsauftrag Mahnwesen Honorar**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ki-arbeitsauftrag-briefing`

**Fokus:** Kanzleiweiter Skill, der aus einer unklaren Bitte, einem Dokumentenpaket oder einer Sprachnotiz einen praezisen KI-Arbeitsauftrag macht. Klaert Ziel, Kontext, Outputformat, Grenzen, Quellenstandard, Datenschutz, Fristen und Abnahmekriterien.

# KI-Arbeitsauftrag Briefing

## Zweck

Dieser Skill verwandelt unscharfe Arbeitsauftraege in eine praezise, juristisch brauchbare Arbeitsanweisung. Er ist hilfreich, wenn Aktenstuecke, E-Mails, Screenshots, Tabellen und ein vager Wunsch zusammenfallen.

## Vier Pflichtbausteine

1. Ziel klaeren: Was soll entschieden, geprueft, entworfen, verbessert oder verhandelt werden?
2. Kontext sichern: Rolle, Frist, Dokumente, Beteiligte, Vorgeschichte und Belege.
3. Grenzen setzen: keine Blindzitate, keine erfundenen Tatsachen, keine ungewollten Zugestaendnisse.
4. Ausgabeformat bestimmen: Memo, Tabelle, Schriftsatz, Brief, Beschluss, TOP, Checkliste oder Red-Team-Liste.

## Workflow

1. Material erfassen und sichtbar zwischen Tatsache, Behauptung und Bewertung trennen.
2. Eilige Punkte vorziehen.
3. Schwachstellen und Gegenargumente benennen.
4. Passende Folge-Skills aus demselben Plugin vorschlagen.
5. Einen verwendbaren Output liefern und offene Punkte mit `[noch klaeren]` markieren.

## Ausgabe

| Punkt | Befund | Risiko | Naechster Schritt |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Qualitaetsgate

Ist die Antwort handlungsorientiert, knapp, respektvoll, belegnah und ohne erfundene Quellen? Sind Fristen und offene Tatsachen sichtbar? Ist der naechste Schritt eindeutig?

## Berufsrechtliche Mindestpruefung vor KI-Einsatz

- **§ 43a Abs. 2 BRAO Verschwiegenheit, § 203 StGB:** Mandatsdaten nur in Tools mit Auftragsverarbeitungsvertrag (AVV) nach Art. 28 DSGVO. Keine Mandatsdaten in Tools ohne EU-Hosting oder ohne dokumentierte Verschwiegenheitssicherung.
- **§ 50 BRAO Handakte:** Der KI-generierte Output ist Arbeitsergebnis; relevante Zwischenstaende sind aktenfest zu speichern.
- **BORA und KI-Richtlinie:** Mandantenseitige Aufklaerung bei KI-Einsatz im Mandat erwaegen; Pseudonymisierung von Personendaten vor Promptuebergabe.
- **Halluzinations-Sperre:** Jede juristische Aussage muss vor Versand verifiziert sein (Rechtsprechung mit Az., Norm in aktueller Fassung). Modell-Wissen ohne Verifizierung ist nicht zitierfaehig.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `mahnwesen-honorar`

**Fokus:** Mahnwesen für eigene Honorarforderungen der Kanzlei gegenüber Mandanten. Anwendungsfall Mandant hat Rechnung nicht bezahlt und Kanzlei muss mahnen oder klagen. Normen § 286 BGB Verzugsbeginn § 288 BGB Verzugszinsen § 23 Nr. 1 GVG AG-Zuständigkeit bis 10000 EUR ab 01.01.2026 § 688 ff. ZPO Mahnverfahren. Prüfraster Stufen Zahlungserinnerung erste Mahnung zweite Mahnung dritte Mahnung Inkassouebergabe AG-Klage. Output Gestuftes Mahnschreibenpaket mit Verzugszinsen Mahnkosten Klagedrohung und Klageentwurf. Abgrenzung zu forderungsmanagement-klagewerkstatt-Plugin und kanzlei-allgemein-rechnung.

# Mahnwesen für Kanzleihonorar


## Triage zu Beginn
1. Auf welcher Stufe befindet sich das Mahnverfahren: Zahlungserinnerung, erste, zweite oder dritte Mahnung?
2. Wann ist die Forderung faellig geworden und wann ist der Verzug eingetreten (§ 286 BGB)?
3. Besteht ein laufendes Mandatsverhältnis das die Eskalation taktisch beeinflusst?
4. Ist ein Inkasso- oder gerichtliches Mahnverfahren (§§ 688 ff. ZPO) bereits eingeleitet oder geplant?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 286 BGB — Verzug: Voraussetzungen (Faelligkeit, Mahnung oder Kalendertermin)
- § 288 Abs. 1, 2 BGB — Verzugszinsen: 5 Prozentpunkte (B2C) bzw. 9 Prozentpunkte (B2B) ueber Basiszinssatz
- §§ 688-703 ZPO — Gerichtliches Mahnverfahren: schnelles Inkasso-Instrument
- § 23 Nr. 1 GVG — Sachliche Zustaendigkeit des AG bis 10.000 EUR (ab 01.01.2026)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Disclaimer

Honorarforderungen gegen Mandanten sind besonders sensible Eskalationen — das laufende Mandatsverhältnis kann darunter leiden. Vor jeder Eskalation Rücksprache mit dem zuständigen Anwalt; nichts ohne anwaltliche Freigabe versenden.

## Stufenmodell

### Stufe 0 — Zahlungserinnerung (vor Verzug)

- Etwa zehn Tage nach Fälligkeit der Rechnung.
- Höflicher Hinweis dass die Rechnung noch nicht beglichen ist.
- Kein Verzug; keine Mahnkosten; keine Verzugszinsen.

```
Sehr geehrter Herr Mueller,

unsere Rechnung Nr. 2026/00123 vom (Datum) über (Betrag) EUR ist noch
nicht ausgeglichen. Sicher haben Sie die Fälligkeit lediglich uebersehen.

Bitte überweisen Sie den Betrag bis zum (zwei Wochen) auf unser Konto
(IBAN). Sollte sich die Zahlung mit diesem Schreiben gekreuzt haben
betrachten Sie dieses Schreiben als gegenstandslos.

Mit freundlichen Grüßen
[Kanzlei]
```

### Stufe 1 — Erste Mahnung (Verzug nach § 286 BGB)

- Etwa 30 Tage nach Rechnung.
- Verzug liegt vor — Verzugszinsen § 288 BGB beginnen.
- Verzugszinsen: bei Verbraucher 5 Prozentpunkte über Basiszinssatz § 288 Abs. 1 BGB; bei Unternehmer 9 Prozentpunkte § 288 Abs. 2 BGB. Bei B2B-Mandanten ggf. Pauschale 40 EUR § 288 Abs. 5 BGB.
- Mahnkosten zulässig (z. B. 2,50 EUR Sachkosten).

```
Sehr geehrter Herr Mueller,

unsere Rechnung Nr. 2026/00123 vom (Datum) über (Betrag) EUR ist trotz
unserer Zahlungserinnerung vom (Datum) bis heute nicht beglichen.

Sie befinden sich in Verzug. Wir berechnen ab dem (Datum) Verzugszinsen
in Höhe von (Prozent) über dem Basiszinssatz gemäß § 288 BGB.

Wir bitten Sie um Zahlung des Gesamtbetrags von (Betrag) EUR bis spaetestens
(Frist) auf unser Konto (IBAN).

Mit freundlichen Grüßen
[Kanzlei]
```

### Stufe 2 — Zweite Mahnung (mit konkreter Konsequenz)

- Etwa zwei Wochen nach erster Mahnung.
- Klare Konsequenzandrohung — gerichtliches Mahnverfahren / Klage.

```
Sehr geehrter Herr Mueller,

trotz unserer Mahnung vom (Datum) ist die Rechnung Nr. 2026/00123 vom
(Datum) über (Betrag) EUR bis heute nicht ausgeglichen.

Wir setzen Ihnen eine letzte Zahlungsfrist bis zum (zehn Tage). Sollte
die Zahlung bis dahin nicht auf unserem Konto eingegangen sein werden
wir das gerichtliche Mahnverfahren einleiten oder Klage zum zuständigen
Amtsgericht erheben.

Rückstand und Verzugszinsen:
- Rechnungsbetrag: (Betrag) EUR
- Verzugszinsen seit (Datum): (Betrag) EUR
- Mahnkosten: (Betrag) EUR
- Gesamtsumme: (Betrag) EUR

Mit freundlichen Grüßen
[Kanzlei]
```

### Stufe 3 — Klage oder Mahnbescheid

- **Eigenes Mahnverfahren** über zentrales Mahngericht (online über www.online-mahnantrag.de).
- **Direkte Klage** zum Amtsgericht — sachliche Zuständigkeit § 23 Nr. 1 GVG (bis 10.000 EUR seit 01.01.2026); über 10.000 EUR LG nach § 71 GVG.
- **Inkasso** alternativ über externes Inkassounternehmen mit Kostenrisiko.

## Sonderfälle

### Pflicht zur Akteneinsicht des Mandanten

Mandant kann verlangen Einsicht in die Akte (§ 50 Abs. 5 BRAO). Bei Streit über Honorar zuständig prüfen.

### Vergütungsklage gegen früheren Mandanten

- Sachliche Zuständigkeit § 23 Nr. 1 GVG (bis 10.000 EUR seit 01.01.2026); darüber LG § 71 GVG.
- Örtliche Zuständigkeit allgemeiner Gerichtsstand des Mandanten (§§ 12 13 ZPO).
- Streitwert: Honorarforderung mit Nebenforderungen.

### Verjährung der Honorarforderung

- Regelmäßige Verjährungsfrist drei Jahre (§ 195 BGB).
- Beginn Ende des Jahres in dem die Forderung entstanden ist und der Anwalt Kenntnis hatte (§ 199 BGB).

## Audit

- Eintrag pro Mahnstufe mit Datum und Versand.
- Verbindung zur Akte des Mandanten.
- Anteil der Honorarrückstaende kanzleiweit monatlich auswerten.

## Ausgabe

- Mahnentwurf je Stufe.
- Eintrag im Honorar-Tracker.
- Eskalation an Anwalt bei Stufe 2 oder 3.
