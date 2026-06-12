---
name: liquiditaetsvorschau-3wochen
description: "Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Prüfung."
---

# Drei-Wochen-Liquiditätsvorschau (§ 17 InsO, wochenaktuell)

## Fachkern: Drei-Wochen-Liquiditätsvorschau (§ 17 InsO, wochenaktuell)
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

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

1. **Zweck der Vorschau?** ZU-Prüfung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Gläubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) für insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) für langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Für InsO-Beurteilung tag-genau festlegen; für Prognose ab aktuellem Tag.
5. **Sanierungsmassnahmen einbeziehen?** Stundungen, Zuschuss, neue Kreditlinie — nur wenn verbindlich zugesagt.

## Output-Template 13-Wochen-Liquiditaetsvorschau

**Adressat:** Insolvenzgericht / Gläubigerausschuss / Bank — Tonfall: sachlich-betriebswirtschaftlich

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

