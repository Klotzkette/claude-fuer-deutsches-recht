---
name: liquiditaetsplanung-liquiditaetsvorschau-3wochen
description: "Liquiditaetsvorschau 3wochen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Liquiditaetsvorschau 3wochen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Liquiditaetsvorschau 3wochen** im Plugin Liquiditätsplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `liquiditaetsvorschau-3wochen` | Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Prüffeld für liquiditaetsvorschau insolvenzrechtlich: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `spezial-ampel-zahlen-schwellen-und-berechnung` | Ampel: Zahlen, Schwellenwerte und Berechnung im Plugin liquiditaetsplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Liquiditätsplanung gilt für **Liquiditaetsvorschau 3wochen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `liquiditaetsvorschau-3wochen`

**Fokus:** Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Pruefung.

# Drei-Wochen-Liquiditätsvorschau (§ 17 InsO, wochenaktuell)

## Fachkern: Drei-Wochen-Liquiditätsvorschau (§ 17 InsO, wochenaktuell)
- **Spezialgegenstand:** Drei-Wochen-Liquiditätsvorschau (§ 17 InsO, wochenaktuell) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Dieser Skill erstellt für eine GmbH/UG/AG/Einzelunternehmen eine **wochenaktuelle Drei-Wochen-Liquiditätsvorschau** und dokumentiert die insolvenzrechtliche Vorprüfung nach § 17 InsO. Rechtsprechung wird nur nach Live-Prüfung verwendet. Das Standardergebnis ist eine **Excel-Tabelle nach der hinterlegten Vorlage** (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`) auf Wochenbasis (Freitag = Wochenstichtag). Zusätzlich auf Nutzerwunsch ein **interaktives HTML-Padlet** oder ein **Markdown-Artefakt**, das im Verlauf des Gesprächs fortlaufend gepflegt wird. Ein Memo wird **nur auf ausdrückliche Anfrage** erstellt.

Anwendungsfälle:

- Wöchentliche Geschäftsführer-Sitzung in einer KMU-GmbH mit angespannter Liquidität.
- Dauermandat des Steuerberaters mit Krisenfrüherkennungsauftrag.
- Vorprüfung vor dem Bankgespräch oder vor einer StaRUG-Anzeige.
- Erstindikation, ob ein Antragspflicht-Check nach § 15a InsO ausgelöst werden muss.

## Eingaben — minimaler Datensatz

Der Skill fragt diese Felder strukturiert ab. Fehlt etwas, wird der Worst Case angesetzt und die Annahme im Padlet/Artefakt protokolliert.

- **Unternehmen** (Firma, Rechtsform).
- **Stichtag**: Montag der laufenden KW; Wochenende der Vorschau ist jeweils Freitag derselben Woche.
- **Aktiva I (zum Stichtag)**: Bank (verfügbarer Saldo), Kasse, ungenutzter und zugesagter Kontokorrent. Gekündigte Linien zählen nicht, voll ausgeschöpfte Kontokorrents zählen nicht.
- **Aktiva II (KW *t* bis *t+2*)**: erwartete Einzahlungen aus Debitoren, freie Kreditzusagen, schnell verwertbares Umlaufvermögen — je Woche.
- **Passiva I (zum Stichtag)**: alle am Stichtag fälligen, eingeforderten und nicht echt gestundeten Verbindlichkeiten.
- **Passiva II (KW *t* bis *t+2*)**: binnen drei Wochen fällig werdende Verbindlichkeiten je Woche, sortiert nach Buckets (Lohn/SV/Lohnsteuer/USt-VZ/Miete/Lieferanten kritisch/Zins+Tilgung/Sonstiges).
- **Offene Forderungen gesamt** (Nominal, davon binnen 3 Wochen erwartet, davon tituliert, davon zweifelhaft).
- **Indizien** § 17 Abs. 2 S. 2 InsO (Lohnsteuer-Rückstände, SV-Rückstände, Lastschriftrückläufer, Stundungsbitten, eingestellte Zahlungen FA/KK, Pfändungen, Insolvenzanträge, Wechselproteste).

## Bezugsquellen der Eingabedaten

Bevor mit Schätzungen gearbeitet wird, dem Nutzer in dieser Reihenfolge konkret folgende Frage stellen:

> Wie sollen die Bankdaten und offenen Posten einfließen — manuell, per Datei-Import (CAMT.053, MT940, CSV-Bankexport, DATEV-Export), oder über einen verbundenen Bankzugang (PSD2 / FinTS / vorhandener Connector)?

- **Manuell**: Nutzer trägt Werte direkt im Padlet, Markdown-Artefakt oder Chat ein. Stets zulässig.
- **Datei-Import**: Akzeptiert werden bankübliche Exporte (CAMT.053, MT940, CSV des Onlinebankings) und DATEV-OPOS-Exporte (Offene Posten Debitoren/Kreditoren). Der Skill liest sie ein und bucht sie in Aktiva I/II bzw. Passiva I/II nach Fälligkeitsdatum.
- **Connector**: Vor jedem Versuch `list_external_tools` mit Suchbegriffen wie `banking`, `psd2`, `fintap`, `gocardless` aufrufen. Wenn ein Connector verfügbar ist, dem Nutzer die Verbindung und Datenherkunft transparent erläutern und die Aktiva I direkt aus den Salden, Aktiva II aus geplanten Eingängen, Passiva I/II aus offenen Posten ableiten. Wenn kein Connector verfügbar ist, höflich darauf hinweisen, dass der Skill selbst keinen Open-Banking-Zugang aufbaut, und auf die manuelle oder Datei-Import-Variante zurückfallen.

Datenschutz: Bei Mandantendaten auf das Mandatsgeheimnis (§§ 203/204 StGB, § 43e BRAO) hinweisen. Bei Banking-Daten zusätzlich auf Drittlandtransfer-Risiken (DSGVO Art. 44 ff.) und auf die Notwendigkeit einer eigenen DSFA hinweisen, sofern eine vorliegt.

## Ablauf

**Schritt 1 — Format und Padlet-Wahl**
Erst genau eine Rückfrage:

> Ergebnisformat: nur Excel-Tabelle (Standard), Excel + interaktives HTML-Padlet zur fortlaufenden Pflege, oder Excel + Markdown-Artefakt? Memo erst auf Anfrage.

Die Antwort merken und nicht erneut nachfragen. Default bei Schweigen ist Excel + HTML-Padlet.

**Schritt 2 — Datenquelle**
Banking-Frage nach Abschnitt *Bezugsquellen der Eingabedaten* stellen. Erst danach Eingaben einsammeln.

**Schritt 3 — Stichtag und Wochenraster**
- Stichtag = Montag der laufenden KW *t*.
- Wochenraster: KW *t*, *t+1*, *t+2* mit Freitag als Wochenstichtag. Die Vorschau zeigt für jede Woche: Liquidität Wochenanfang (Montag), Σ Einnahmen, Σ Ausgaben, Cashflow, Liquidität Wochenende (Freitag).
- Spaltenformat wie in der Vorlage `Liquiditaetsplan-Wochenbasis.xlsx`: Kategorien-Zeilen × KW-Spalten, keine andere Anordnung.

**Schritt 4 — BGH-Test § 17 InsO (Liquiditätsbilanz)**
- Aktiva I = Bank + Kasse + freier zugesagter Kontokorrent (zum Stichtag).
- Aktiva II = Σ Einnahmen KW *t* bis *t+2*.
- Passiva I = am Stichtag fällig, eingefordert, nicht echt gestundet (überwiegend in KW *t* aufgeführt).
- Passiva II = binnen 3 Wochen fällig werdend (KW *t+1* + KW *t+2* und gegebenenfalls Resterfüllung der Passiva I).
- Σ Liquide = Aktiva I + Aktiva II.
- Σ Fällig = Passiva I + Passiva II.
- **Liquiditätslücke (absolut) = max(0, Σ Fällig − Σ Liquide)**.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 5 — Ampel und 3-Wochen-Schließbarkeit**
- 🟢 **Grün**: Liquiditätsquote < 10 % und am Ende von *t+2* ist die Liquidität nicht negativ und weniger als zwei Indizien gesetzt.
- 🟡 **Gelb**: Liquiditätsquote ≥ 10 %, am Ende von *t+2* aber Liquidität ≥ 0 (Lücke binnen drei Wochen schließbar) und weniger als zwei Indizien.
- 🔴 **Rot**: Liquiditätsquote ≥ 10 % **und** Liquidität am Ende von *t+2* negativ (nicht binnen drei Wochen schließbar) **oder** zwei und mehr Indizien gesetzt — Zahlungsunfähigkeit § 17 InsO indiziert.

**Schritt 6 — Verhältnis zu offenen Forderungen**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 7 — Ergebnis ausliefern**
- **Immer**: Excel-Datei `Liquiditaetsplan-<Firma>-KW<t>.xlsx` aus der Vorlage befüllen. Sheet `Liquiditätsplan` (Werte und Wochenraster) und Sheet `BGH-Schema` (Erläuterungs-Sheet) unverändert lassen.
- **Wenn HTML-Padlet gewählt**: zusätzlich `liquiditaets-padlet-<Firma>-KW<t>.html` aus `assets/padlet/liquiditaets-padlet.html` ableiten, in `localStorage` werden die Eingaben gespeichert und die Datei kann offline genutzt werden.
- **Wenn Markdown-Artefakt gewählt**: `liquiditaets-artefakt-<Firma>-KW<t>.md` auf Basis von `assets/markdown/liquiditaets-artefakt-vorlage.md` ausfüllen.
- Bei jeder Folgemeldung des Nutzers (weitere Belege, Beträge, Korrekturen, neue Indizien) das gewählte Artefakt-Format aktualisieren und die neue Version unter demselben Asset-Namen liefern.

**Schritt 8 — Memo (nur auf Anfrage)**
Erst nach Auslieferung der Vorschau anbieten:

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Subsumtion nach § 17 InsO erstellen?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 9 — Eskalation**
Bei 🔴: ausdrücklich auf die Skills `zahlungsunfaehigkeit-pruefung-17-inso` und `antragspflicht-15a-inso` aus dem Plugin `insolvenzrecht` hinweisen und — falls Steuerberatermandat — den Hinweis nach § 102 StaRUG textbausteinartig formulieren. Die 3-Wochen-Frist § 15a InsO läuft ab tatsächlichem Eintritt der Zahlungsunfähigkeit, nicht ab Erstellung des Plans.

## Rechtlicher Rahmen

### Primärnormen

- **§ 17 InsO** Zahlungsunfähigkeit.
- **§ 18 InsO** drohende Zahlungsunfähigkeit (24-Monats-Prognose, Hinweisfunktion).
- **§ 15a InsO** Antragspflicht (3 Wochen).
- **§ 1 StaRUG** Krisenfrüherkennungspflicht der Geschäftsleitung.
- **§ 102 StaRUG** Hinweispflicht beratender Berufe.

### Leitentscheidungen (Volltexte im Plugin: `references/rechtsprechung/`)

1. **BGH II ZR 139/23 vom 11.03.2025** — Beurteilung der Zahlungsunfähigkeit allein anhand objektiver Umstände; auf den materiellen Bestand der Verbindlichkeit kommt es an. Volltext lokal als PDF in `references/rechtsprechung/BGH_II_ZR_139-23_vom_2025-03-11.pdf`; online über die BGH-Rechtsprechungsdatenbank (Aktenzeichensuche II ZR 139/23) verifizieren.
2. **BGH IX ZR 229/22 vom 23.01.2025** (DB 2025, 381) — Titulierte streitige Forderung in Höhe des Nennwerts in der Liquiditätsbilanz, wenn Vollstreckung eingeleitet wurde. Volltext lokal als PDF in `references/rechtsprechung/BGH_IX_ZR_229-22_vom_2025-01-23.pdf`.
3. **BGH II ZR 112/21 vom 28.06.2022** (ZIP 2022 S. 1606; NZI 2022 S. 787; GmbHR 2022 S. 1036) — Darlegung auch durch Aneinanderreihung tagesgenauer Liquiditätsstatus (Bugwellenrechtsprechung); Liquiditätsbilanz nicht zwingend. Volltext lokal als PDF in `references/rechtsprechung/BGH_II_ZR_112-21_vom_2022-06-28.pdf`.
4. **BGH IX ZR 48/21 vom 28.04.2022** (ZIP 2022 S. 1341; GmbHR 2022 S. 908) — Bestätigung der 10-%-Schwelle; geordnete Gegenüberstellung erforderlich (Liquiditätsbilanz oder Finanzplan). Volltext lokal als PDF in `references/rechtsprechung/BGH_IX_ZR_48-21_vom_2022-04-28.pdf`.
5. **BGH II ZR 88/16 vom 19.12.2017** (BGHZ 217 S. 129; ZIP 2018 S. 283; NJW 2018 S. 1089) — Passiva II zwingend einzubeziehen; Absage an die Bugwellentheorie; Symmetrie- und Gläubigerschutzargument; Substantiierung beim Bestreiten durch den Geschäftsführer. Volltext lokal als PDF in `references/rechtsprechung/BGH_II_ZR_88-16_vom_2017-12-19.pdf`.
6. **BGH II ZR 296/05 vom 24.05.2005** — Klassisches Prüfraster für Liquiditätsstockung versus Zahlungsunfähigkeit; Drei-Wochen-Schließbarkeit der Lücke. Vor Übernahme über die BGH-Datenbank verifizieren (Aktenzeichensuche II ZR 296/05).
7. **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung der Vorsatzanfechtung: bei objektiv festgestellter Zahlungsunfähigkeit kein Automatik-Schluss auf den Vorsatz; konkrete Bedrohungslage darzulegen. Vor Übernahme über die BGH-Datenbank oder dejure.org verifizieren.

Zitierweise: Pinpoint mit Randnummer; Reihenfolge BGH-Datum (jüngere zuerst), keine US-stare-decisis-Logik, keine pretrial discovery.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Berufsständischer Hintergrund (nicht im Vordergrund zitieren)

- **IDW S 11** (Stand 12.08.2021), Tz. 16 f., 31–37 — Beurteilung des Eröffnungsgrundes der Zahlungsunfähigkeit.
- **IDW S 6** — Anforderungen an Sanierungskonzepte und integrierte Planung (hier nur Hintergrundmaßstab).

## Ausgabeformat

1. **Excel** auf Basis der Vorlage `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`: Wochenraster KW *t*…*t+15* in Spalten (Vorgabe beibehalten), BGH-Block ab Zeile 42 mit Aktiva I/II, Passiva I/II, Lücke abs., Lücke %, Ampel; Block "Offene Forderungen" und Hinweise zur BGH-Rechtsprechung. Datei wird unter dem Namen `Liquiditaetsplan-<Firma>-KW<t>.xlsx` zurückgegeben.
2. **HTML-Padlet** (auf Wunsch): autarke single-file HTML aus `assets/padlet/liquiditaets-padlet.html`, das im Browser lebt, im `localStorage` speichert und auf JSON exportiert/importiert werden kann. Editierbare Felder rechnen die Ampel live nach BGH-Schema. KW-Header werden aus der eingegebenen KW abgeleitet.
3. **Markdown-Artefakt** (auf Wunsch): Vorlage `assets/markdown/liquiditaets-artefakt-vorlage.md`, mit Tabellen, Indizienliste und Kurzfazit, das bei jeder Folgemeldung neu geschrieben wird.
4. **Memo** (nur auf Anfrage): Kurz-Gutachten im Gutachtenstil, höchstens zwei Seiten, DOCX oder Markdown nach Wahl.

## Beispiel

**Sachverhalt**: Edelholz Manufaktur Berlin GmbH, Stichtag Mo 18.05.2026, Bank 18.500 €, Kasse 0 €, Kontokorrent 150.000 € zu 92 % ausgeschöpft (12.000 € frei). Fällig KW 21: Lohn + AG-SV 42.000 €, Lieferant kritisch 19.500 €. KW 22: SV-Beitrag 14.800 €, Miete 7.200 €. KW 23: USt-VZ 14.200 €, Leasing 3.400 €. Erwartete Eingänge: KW 22 18.000 € (Skonto-Sicherheit 80 % = 14.400 €), KW 23 9.500 €.

**Auswertung**:
- Aktiva I = 30.500 €. Aktiva II = 23.900 €. Σ Liquide = 54.400 €.
- Passiva I (KW 21) = 61.500 €. Passiva II (KW 22 + KW 23) = 39.600 €. Σ Fällig = 101.100 €.
- Liquiditätslücke absolut = 46.700 €. Quote = 46,2 %.
- Liquidität Wochenende KW 23: Start 30.500 € − Σ CF (− 61.500 + 14.400 − 21.500 + 9.500 − 17.600) = −46.200 €.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Handlung**: Übergabe an `antragspflicht-15a-inso` und `zahlungsunfaehigkeit-pruefung-17-inso`. Bei Steuerberatermandat Hinweis nach § 102 StaRUG dokumentieren. Die 3-Wochen-Frist § 15a InsO läuft ab tatsächlichem Eintritt.

## Typische Fehler

- **Voll ausgeschöpften Kontokorrent als Liquidität ansetzen**: Nur ungenutzter, zugesagter und ziehungsfähiger Teil zählt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Großeingänge zu 100 % ansetzen**: Realistische Ausfall- und Skontoquote, im Zweifel Worst Case.
- **3-Wochen-Frist statisch ab Planerstellung rechnen**: Sie läuft ab Eintritt der Zahlungsunfähigkeit.
- **SV- und Lohnsteuer-Rückstände kleinreden**: Starke Indizien und persönlich haftungsauslösend.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Vorlage verändern**: Die Excel-Vorlage hat eine vorgegebene Form (Kategorien-Zeilen × KW-Spalten). Nicht in ein anderes Layout umbauen.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

Bei 🔴 sofort:

- `zahlungsunfaehigkeit-pruefung-17-inso` (Plugin `insolvenzrecht`) — formales Prüfgutachten und gerichtsfester Liquiditätsstatus.
- `antragspflicht-15a-inso` (Plugin `insolvenzrecht`) — Fristenlauf, Haftung Geschäftsleiter, § 15b InsO Zahlungsverbote.
- `liquiditaetsvorschau-insolvenzrechtlich` (dieses Plugin) — Liquiditätsbilanz als Beweismittel mit IDW-S-11-Würdigung.

Für die mittel- und langfristige Sicht: Schwester-Skill `liquiditaetsvorschau-3-6-12-monate` (dieses Plugin).


## Triage — Liquiditaetsvorschau Einordnung

Bevor losgelegt wird, klaere:

1. **Zweck der Vorschau?** ZU-Pruefung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Glaeubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) fuer insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) fuer langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Fuer InsO-Beurteilung tag-genau festlegen; fuer Prognose ab aktuellem Tag.
5. **Sanierungsmassnahmen einbeziehen?** Stundungen, Zuschuss, neue Kreditlinie — nur wenn verbindlich zugesagt.

## Output-Template 13-Wochen-Liquiditaetsvorschau

**Adressat:** Insolvenzgericht / Glaeubigerausschuss / Bank — Tonfall: sachlich-betriebswirtschaftlich

```
13-WOCHEN-LIQUIDITAETSVORSCHAU (direkte Methode)
Gesellschaft: [FIRMA] Erstellt: [DATUM] Ersteller: [NAME]

Woche | Anfangsbestand | Einzahlungen | Auszahlungen | Endbestand | Kreditlinie | Freie Liqui
 1 | EUR [XXX] | EUR [YYY] | EUR [ZZZ] | EUR [AAA] | EUR [BBB] | EUR [CCC]
 2 | ... | ... | ... | ... | ... | ...
 13 | ... | ... | ... | ... | ... | ...

AMPEL-STATUS:
Wochen 1-4 (kurzfristig): [GRUEN / GELB / ROT]
Wochen 5-9 (mittelfristig): [...]
Wochen 10-13 (langfristig): [...]

ENGPAESSE: [Beschreibung kritischer Wochen und Gegenmassnahmen]
ANNAHMEN: [Auflistung der Schluesselannahmen]
```

## 2. `liquiditaetsvorschau-insolvenzrechtlich`

**Fokus:** Prüffeld für liquiditaetsvorschau insolvenzrechtlich: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau

## Fachkern: Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau
- **Spezialgegenstand:** Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Dieser Skill erstellt eine **gerichtsfähig dokumentierte Liquiditätsbilanz** auf einen Stichtag und eine zugehörige **wochenaktuelle Liquiditätsvorschau** über mindestens drei Wochen, regelmäßig bis 13 Wochen, in der für § 17 InsO benötigten Form. Das Standardergebnis ist eine Excel-Tabelle auf Wochenbasis nach hinterlegter Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`). Auf Nutzerwunsch wird zusätzlich ein interaktives HTML-Padlet oder ein Markdown-Artefakt geliefert; ein Memo wird nur auf ausdrückliche Anfrage erstellt.

Anwendungsfälle:

- Geschäftsführerhaftung nach § 15b InsO; Insolvenzanfechtung nach §§ 129 ff. InsO.
- Gläubigerantrag § 14 InsO (Substantiierung der Forderung und Zahlungsunfähigkeit).
- Insolvenzverwaltermandat (insb. nach BGH IX ZR 129/22 vom 18.04.2024 zur konkreten Darlegung der Liquiditätsunterdeckung im Anfechtungsprozess).
- Berater im Sanierungs- oder StaRUG-Kontext (Fortbestehensprognose § 19 InsO).
- Sanierungskonzept-Vorarbeit, wenn aus der kurzfristigen Liquiditätsbilanz eine integrierte Sanierungsplanung werden soll.

## Eingaben

Der Skill fragt strukturiert die folgenden Felder ab. Was fehlt, wird im Worst Case angesetzt und im Padlet/Artefakt als Annahme protokolliert.

- **Stichtag** (z. B. Tag der Antragstellung, frühester Eintritt § 17 InsO für Anfechtungszwecke).
- **Aktiva I**: Bankguthaben, Kasse, ungenutzter und zugesagter Kontokorrent, sofort verwertbares Vermögen.
- **Aktiva II**: konkret zu erwartende Zahlungseingänge KW *t* bis *t+2* (bzw. *t+12* bei 13-Wochen-Plan), freie Kreditzusagen, schnell verwertbares Umlaufvermögen, mit realistischer Ausfallquote.
- **Passiva I**: alle am Stichtag fälligen und ernsthaft eingeforderten Verbindlichkeiten; Stundungen nur, wenn echt vereinbart und dokumentiert.
- **Passiva II**: binnen drei Wochen fällig werdende Verbindlichkeiten, einzeln aufgeführt nach Gläubiger und Fälligkeitsdatum.
- **Echte Stundung** (mit beiderseitigem Einvernehmen und Fälligkeitsverschiebung) beseitigt Passiva I; faktische Duldung des Zahlungsverzugs nicht. Konkrete BGH-Linie über offene Quellen verifizieren.
- **Indizien** nach § 17 Abs. 2 S. 2 InsO (Lohnsteuer-Rückstände, SV-Rückstände, Lastschriftrückläufer, Stundungsbitten, eingestellte Zahlungen FA/KK, Pfändungen, Insolvenzanträge anderer Gläubiger, Wechselproteste).

## Bezugsquellen der Eingabedaten

Vor der Aufstellung folgende Frage stellen:

> Wie sollen die Daten einfließen — manuell, per Datei-Import (CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS-Export), oder über einen verbundenen Bankzugang (PSD2 / FinTS / vorhandener Connector)?

Detailregeln siehe Schwester-Skill `liquiditaetsvorschau-3wochen`, Abschnitt "Bezugsquellen der Eingabedaten" — der Skill selbst baut keinen Open-Banking-Client.

## Ablauf

**Schritt 1 — Format- und Padlet-Wahl**: identisch zum Schwester-Skill. Standard: Excel-Tabelle + HTML-Padlet, sofern nicht anders gewünscht.

**Schritt 2 — Stichtagsbestimmung**: konkretes Datum festlegen. Im Haftungs- und Anfechtungskontext ist nicht der Antragstag, sondern der tatsächliche Eintritt der Zahlungsunfähigkeit maßgeblich. Stichtag dokumentieren.

**Schritt 3 — Aufstellung der Liquiditätsbilanz**

```
Aktiva I (am Stichtag sofort verfügbar) €
+ Aktiva II (binnen 3 Wochen flüssig) €
= Σ Liquide Mittel €

Passiva I (am Stichtag fällig & eingefordert) €
+ Passiva II (binnen 3 Wochen fällig) €
= Σ Fällige Verbindlichkeiten €

Liquiditätslücke (absolut) = Σ Fällig − Σ Liquide
Liquiditätsquote = Liquiditätslücke ÷ Σ Fällig
```

Maßstab: BGH-Linie zur Liquiditätsbilanz; konkrete Aktenzeichen und Randnummern vor Ausgabe über dejure.org / openjur.de verifizieren.

**Schritt 4 — Subsumtion nach BGH-Schema**

- **Liquiditätsquote < 10 % und Lücke binnen drei Wochen schließbar**: nur Zahlungsstockung.
- **Liquiditätsquote ≥ 10 % und Lücke nicht binnen drei Wochen schließbar**: regelmäßig Zahlungsunfähigkeit.
- Konkretes Az. der grundlegenden BGH-Entscheidung zum 10-%-/3-Wochen-Schema vor Ausgabe verifizieren.

**Schritt 5 — Würdigung der Indizien § 17 Abs. 2 S. 2 InsO**

Indizienkatalog für die Zahlungseinstellung umfasst insb. verspätete Lohnzahlungen, offene SV-Beiträge, erfolglose Stundungsbitten, Pfändungsmaßnahmen anderer Gläubiger, Wechselproteste und eigenen Insolvenzantrag. Konkrete BGH-Linie über offene Quellen verifizieren.

**Schritt 6 — Titulierte Forderungen**

Titulierte Forderungen sind regelmäßig fällig und in Passiva I aufzunehmen; ausnahmsweise kann eine streitige Titulierung im Anfechtungsprozess Indizwirkung mindern. Konkrete BGH-Entscheidung vor Ausgabe verifizieren.

**Schritt 7 — Objektivität**

Maßstab der Zahlungsunfähigkeit ist objektiv; das Bewusstsein des Schuldners ist nur für die Verschuldensfrage relevant (§ 15a InsO). Konkrete BGH-Linie zur "Erkennbarkeit der Insolvenzreife" vor Ausgabe über offene Quellen prüfen.

**Schritt 8 — Ausgabe und Eskalation**

- Excel-Datei aus der Vorlage befüllen (zwingend).
- HTML-Padlet oder Markdown-Artefakt nur, wenn so gewählt.
- Bei Quote ≥ 10 % und fehlender Schließbarkeit: Übergabe an `antragspflicht-15a-inso`; bei Steuerberatermandat Hinweis nach § 102 StaRUG dokumentieren.
- Wenn die Vorschau für Bank, StaRUG, Schutzschirm, Eigenverwaltung oder Insolvenzplan genutzt werden soll: ausdrücklich festhalten, dass die Liquiditätsbilanz nur die Cash-Seite liefert. Danach an `idw-s6-integrierte-sanierungsplanung` übergeben, um GuV, Planbilanz, Maßnahmenwirkung, Leitbild und nachhaltige Sanierungsfähigkeit zu prüfen.
- Memo nur auf Anfrage.

## Rechtlicher Rahmen

### Primärnormen

§ 17 InsO, § 15a InsO, § 18 InsO, § 19 InsO, § 102 StaRUG.

### Leitentscheidungen (Stand Mai 2026; vor Ausgabe konkrete Aktenzeichen über dejure.org / openjur.de / bundesgerichtshof.de prüfen)

1. **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung der Vorsatzanfechtung: bei objektiv festgestellter Zahlungsunfähigkeit kein Automatik-Schluss auf Vorsatz; konkrete Bedrohungslage darzulegen. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
2. **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit beim Bargeschäft (§ 142 Abs. 1 Hs. 2 InsO). <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
3. **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers (§ 823 II BGB iVm § 15a InsO). <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
4. **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Wissentlichkeitsausschluss; positive Kenntnis pro Pflichtverletzung erforderlich.
5. **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
6. Grundlegende ältere BGH-Linie zum 10-%-/3-Wochen-Schema und zur Zahlungseinstellung: konkrete Az. (insb. zur Liquiditätsbilanz, zu Stundungen, zu titulierten Forderungen, zur Erkennbarkeit der Insolvenzreife) vor Ausgabe in offener Quelle prüfen.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Berufsständischer Hintergrund

- **IDW S 11** (Stand 12.08.2021), Tz. 16 f., 31–37 — Beurteilung des Eröffnungsgrundes der Zahlungsunfähigkeit.
- **IDW S 6** — Anforderungen an Sanierungskonzepte und integrierte Planung.

## Ausgabeformat

1. **Excel** auf Basis von `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx` — Wochenraster, BGH-Block, Block "Offene Forderungen", Hinweise zur BGH-Rechtsprechung.
2. **HTML-Padlet** (auf Wunsch).
3. **Markdown-Artefakt** (auf Wunsch).
4. **Memo** (nur auf Anfrage) im Gutachtenstil: Sachverhalt, Rechtliche Grundlagen, Liquiditätsbilanz, Subsumtion BGH-Schema, Indizienanalyse, Ergebnis, Quellennachweis.

## Beispiel

Siehe Schwester-Skill `liquiditaetsvorschau-3wochen` (Beispielfall Edelholz Manufaktur Berlin GmbH). Für gerichtsfeste Verwendung wird zusätzlich die Buchhaltungsherkunft (SuSa-/OPOS-Stand) protokolliert und die Indizienliste belegt.

## Typische Fehler

- **Faktische Duldung als Stundung behandeln**: nur echte schriftliche Stundungsvereinbarung mit Fälligkeitsverschiebung beseitigt Passiva I. Konkrete BGH-Linie über offene Quellen verifizieren.
- **Aussetzung der Vollziehung (§ 361 AO / § 69 FGO) als Stundung behandeln**: AdV hemmt nur die Vollziehung; die Fälligkeit der Steuerforderung bleibt unberührt. AdV-Beträge sind weiter **Passiva I**, soweit nicht zusätzlich eine schriftliche § 222 AO-Stundung mit Fälligkeitsverschiebung über den Stichtag hinaus vorliegt.
- **SV-Beiträge oder Lohnsteuer übersehen**: gesetzlich sofort fällig, zugleich Indizien.
- **Künftige Verträge / hypothetische Verwertungserlöse einbeziehen**: nicht zulässig in Aktiva I/II.
- **Stichtag im Haftungskontext zu spät ansetzen**: tatsächlicher Eintritt maßgeblich.
- **Konkrete Erwartung dauerhafter Unterdeckung nicht dokumentiert**: nach BGH IX ZR 129/22 (18.04.2024) ist die bloße Liquiditätsunterdeckung allein für die Vorsatzanfechtung nicht ausreichend; Verwalter muss die Erwartung dauerhafter Nichtbefriedigung anderer Gläubiger konkret darlegen.
- **Liquiditätsbilanz mit Sanierungskonzept verwechselt**: Für Sanierungsfähigkeit reicht die insolvenzrechtliche Cash-Prüfung nicht. Es braucht zusätzlich Krisenursachenanalyse, Leitbild, Maßnahmenprogramm, GuV-/Bilanzplanung, Szenarien und Dokumentation.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

Bei 🔴: `antragspflicht-15a-inso` und `zahlungsunfaehigkeit-pruefung-17-inso` (Plugin `insolvenzrecht`). Für mittel- und langfristige Sicht: `liquiditaetsvorschau-3-6-12-monate` (dieses Plugin). Für Sanierungskonzept-/Bankfähigkeit: `idw-s6-integrierte-sanierungsplanung` (dieses Plugin).


## Triage — Liquiditaetsvorschau Einordnung

Bevor losgelegt wird, klaere:

1. **Zweck der Vorschau?** ZU-Pruefung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Glaeubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) fuer insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) fuer langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Fuer InsO-Beurteilung tag-genau festlegen; fuer Prognose ab aktuellem Tag.
5. **Sanierungsmassnahmen einbeziehen?** Stundungen, Zuschuss, neue Kreditlinie — nur wenn verbindlich zugesagt.

## Output-Template 13-Wochen-Liquiditaetsvorschau

**Adressat:** Insolvenzgericht / Glaeubigerausschuss / Bank — Tonfall: sachlich-betriebswirtschaftlich

```
13-WOCHEN-LIQUIDITAETSVORSCHAU (direkte Methode)
Gesellschaft: [FIRMA] Erstellt: [DATUM] Ersteller: [NAME]

Woche | Anfangsbestand | Einzahlungen | Auszahlungen | Endbestand | Kreditlinie | Freie Liqui
 1 | EUR [XXX] | EUR [YYY] | EUR [ZZZ] | EUR [AAA] | EUR [BBB] | EUR [CCC]
 2 | ... | ... | ... | ... | ... | ...
 13 | ... | ... | ... | ... | ... | ...

AMPEL-STATUS:
Wochen 1-4 (kurzfristig): [GRUEN / GELB / ROT]
Wochen 5-9 (mittelfristig): [...]
Wochen 10-13 (langfristig): [...]

ENGPAESSE: [Beschreibung kritischer Wochen und Gegenmassnahmen]
ANNAHMEN: [Auflistung der Schluesselannahmen]
```

## 3. `spezial-ampel-zahlen-schwellen-und-berechnung`

**Fokus:** Ampel: Zahlen, Schwellenwerte und Berechnung im Plugin liquiditaetsplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Ampel: Zahlen, Schwellenwerte und Berechnung

## Fachkern: Ampel: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Ampel: Zahlen, Schwellenwerte und Berechnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ampel** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Berechnungsschemata Liquiditätsstatus / -planung

### Liquiditätsstatus zum Stichtag (§ 17 InsO)
| Position | Anmerkung |
|---|---|
| Liquide Mittel (Kasse, Bank, Tagesgeld) | Saldo zum Stichtag |
| + Innerhalb 3 Wochen eingehende Forderungen | OPOS Debitoren mit Fälligkeit |
| + Frei verfügbare Kreditlinien | nur ungekündigt und nicht ausgeschöpft |
| **= Aktiva I** | „Verfügbare Mittel" |
| Fällige Verbindlichkeiten zum Stichtag | OPOS Kreditoren |
| + Innerhalb 3 Wochen fällig (Lohn, USt, KSt, SV) | streng |
| **= Passiva I** | „Fällige Verbindlichkeiten" |
| **Liquiditätslücke = P1 − A1** | wenn ≥ 10 Prozent und 3 Wochen: § 17 InsO |

### 13-Wochen-Liquidität (operativ Krisensteuerung)
- Granularität: wöchentlich.
- Cash-Inflows: Debitoren-Eingänge (Aging), Vorauszahlungen, Erstattungen.
- Cash-Outflows: Lohn/Gehalt mit Auszahlungstag, Lohnsteuer/SV-Abgaben (§ 266a StGB nicht stunden), USt-Vorauszahlung, Miete, Tilgung/Zinsen, Lieferanten nach Fälligkeit, sonstige Betriebsausgaben.
- Endbestand pro Woche: Anfang + Inflow − Outflow.

### 24-Monats-Liquiditätsplan (§ 18 InsO und § 1 StaRUG)
- Granularität: monatlich, integriert mit GuV-Forecast und Bilanzplanung.
- Sensitivität: Base/Best/Worst.

## Schwellenwerte und Ampel

- **GRÜN:** Liquiditätsdeckung > 110 Prozent in jeder Periode des 24-Monats-Horizonts; 13-Wochen-Cash-Reichweite > 6 Wochen Puffer.
- **GELB:** Liquiditätsdeckung 100–110 Prozent oder Worst-Case unter 100 Prozent — Frühwarnpflicht § 1 StaRUG, Maßnahmenplan.
- **ROT:**
 - Liquiditätslücke ≥ 10 Prozent über 3 Wochen → § 17 InsO Zahlungsunfähigkeit, Antragsfrist § 15a InsO.
 - 24-Monats-Plan zeigt Lücke → § 18 InsO drohende ZU, StaRUG-Tor offen.

## Berechnungs-Plausibilitäten
- Anfangsbestand Periode n+1 = Endbestand Periode n (Saldenkonsistenz).
- Working Capital (Debitoren/Kreditoren/Vorräte) realistisch zur Vergangenheit (DSO, DPO, DIO)?
- Kreditlinien-Inanspruchnahme realistisch? Kündigungsrisiko bei Krise eingerechnet?
- Steuern und SV: keine Stundungen ohne schriftliche Zusage Finanzamt / SV-Träger einplanen.

## Anti-Halluzinations-Hinweis
- 10-Prozent / 3-Wochen-Schwelle ist BGH-Linie zu § 17 InsO — keine erfundenen Az.
- Prognosezeitraum § 18 InsO: **24 Monate**; § 19 InsO Fortbestehensprognose: **12 Monate**.
