---
name: liquiditaetsvorschau-3-6-12-monate
description: "Rollierende Liquiditaetsvorschau für 3/6/12 Monate mit Fortfuehrungsprognose, Wochenraster, Excel-Export und Quellenhygiene. Rechtsprechung nur nach Live-Pruefung."
---

# Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose (§§ 17, 19 InsO)

## Fachkern: Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose (§§ 17, 19 InsO)
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

## Zweck

Dieser Skill erzeugt aus dem typischerweise vorhandenen, oft unstrukturierten Material einer kleinen Kapitalgesellschaft (offene Rechnungen, Bankauszüge, BWA, SuSa, Zahlungserwartungen, Kreditverträge, Daueraufträge, Sozialversicherungs- und Steuerbescheide) eine **rollierende Liquiditätsvorschau** mit folgenden Funktionen:

1. **Wochenraster (Mo–So)** über drei Horizonte:
 - **Kurzfristhorizont 13 Wochen (3 Monate)** – primär für § 17 InsO (Zahlungsunfähigkeit).
 - **Mittelfristhorizont 26 Wochen (6 Monate)** – Brücke zwischen Zahlungsfähigkeit und Fortführungsprognose.
 - **Langfristhorizont 52 Wochen (12 Monate)** – Grundlage Fortbestehensprognose nach § 19 Abs. 2 InsO und Fortführungsprognose nach IDW S 6.

2. **Automatische Insolvenzreife-Ampel** für jede Woche:
 - **Grün**: Liquide Mittel > 110 % der in der Folgewoche fällig werdenden Verbindlichkeiten.
 - **Gelb (Zahlungsstockung)**: Lücke < 10 % oder Lücke ≥ 10 %, aber innerhalb von 3 Wochen schließbar.
 - **Livecheck:** Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; die Ampel selbst funktioniert zunächst mit Zahlen und Normtext.

3. **Fortbestehens- und Sanierungsbrücke**: 12-Monats-Auswertung für § 19 InsO plus Übergabe in eine Sanierungsplanung auf IDW-S-6-Niveau. Die Liquiditätsvorschau allein ist noch kein Sanierungskonzept; sie muss bei Bedarf mit GuV, Planbilanz, Maßnahmenlog und Leitbild verzahnt werden.

4. **Excel-Export**: Die Tabelle wird über `werkzeuge/build_liquiditaetsplan.py` als `liquiditaetsplan.xlsx` exportiert. Cloud-Bedienung über interaktive Tabelle möglich; Werte mit Excel-Formeln, nicht hartcodiert. Das Skript läuft mit reiner Python-Standardbibliothek — kein `pip install` nötig. PyYAML wird automatisch erkannt, sonst kommt ein eingebauter Mini-YAML-Parser zum Einsatz.

Anwendungsfälle: Krisen-GmbH/UG, Mittelstand mit Bugwellen-Liquidität, Vorbereitung Sanierungsgespräch mit Hausbank, Dokumentation Fortbestehensprognose für § 19 InsO, Vorbereitung StaRUG-Restrukturierungsverfahren, regelmäßige wöchentliche Geschäftsführer-Sitzung.

## Bezugsquellen der Eingabedaten

Bevor Werte geschätzt werden, dem Nutzer zuerst genau diese Frage stellen:

> Wie sollen die Bankdaten und offenen Posten einfließen — manuell, per Datei-Import (CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS), oder über einen verbundenen Bankzugang (PSD2 / FinTS / vorhandener Connector)?

- **Manuell**: Nutzer trägt Werte im Padlet, Markdown-Artefakt oder Chat ein. Stets zulässig.
- **Datei-Import**: Akzeptiert werden CAMT.053, MT940, CSV des Onlinebankings, DATEV-OPOS-Exporte (Offene Posten Debitoren/Kreditoren). Der Skill liest die Daten ein und ordnet sie nach Fälligkeitsdatum den Wochenbuckets zu.
- **Connector**: Vor jedem Versuch `list_external_tools` mit Suchbegriffen wie `banking`, `psd2`, `fintap`, `gocardless` aufrufen. Wenn ein Connector verfügbar ist, dem Nutzer Datenherkunft und Drittlandtransfer-Risiken (DSGVO Art. 44 ff.) transparent erläutern. Wenn nicht, höflich auf manuell oder Datei-Import zurückfallen.

Mandatsgeheimnis (§§ 203/204 StGB, § 43e BRAO) beachten.

## Format- und Padlet-Wahl

Einmalig am Anfang fragen:

> Ergebnisformat: nur Excel-Tabelle (Standard), Excel + interaktives HTML-Padlet zur fortlaufenden Pflege, oder Excel + Markdown-Artefakt? Memo erst auf Anfrage.

Antwort merken, nicht erneut fragen. Default bei Schweigen: Excel + HTML-Padlet.

## Eingaben

Strukturiert oder unstrukturiert; das Modell soll robust extrahieren:

- **Stammdaten Gesellschaft**: Rechtsform, Branche, Mitarbeiterzahl, Jahresumsatz, Hausbank, Stichtag.
- **Eröffnungsbestand liquider Mittel**: Kontostände, Kasse, Tagesgeld, ungenutzte Kreditlinien (mit Laufzeit und Konditionen).
- **Offene Verbindlichkeiten** (Kreditorenliste): Lieferant, Fälligkeitsdatum, Betrag, Mahnstufe, Stundungen.
- **Offene Forderungen** (Debitorenliste): Kunde, Rechnungsdatum, Fälligkeit, voraussichtlicher Zahlungseingang, Ausfallrisiko.
- **Dauerverpflichtungen**: Miete, Pacht, Leasing, Personal (Lohn, Gehalt, AG-Anteil SV), Krankenkassenbeiträge (monatliche Drittellast), Lohnsteuer, Strom/Gas, Versicherungen.
- **Steuern**: Umsatzsteuer-Vorauszahlung/-Erstattung (mit Voranmeldungsturnus, ggf. Dauerfristverlängerung), Körperschaftsteuer-Vorauszahlung, Gewerbesteuer-Vorauszahlung, Rückstände beim Finanzamt.
- **Kreditverträge**: Tilgung, Zins, Sondertilgung, Covenants (z.B. EK-Quote, Leverage), Avalrahmen.
- **Geplante Investitionen/Desinvestitionen**: CapEx, Maschinenverkauf, Sale-and-Lease-back.
- **Auftragsbestand**: zugesagte Aufträge mit Lieferzeitpunkt, voraussichtlichem Zahlungsziel, Abschlagszahlungen.
- **Bankauszüge** der letzten 3–6 Monate (für saisonale Muster und Plausibilität).
- **BWA und SuSa** (siehe Schwester-Skill `bwa-sus-bilanz-pruefung`).

Wenn Daten lückenhaft sind: Annahmen explizit dokumentieren, sensitivitätsanalysieren (Best/Base/Worst).

## Rechtlicher Rahmen

### Primärnormen

- **§ 17 InsO – Zahlungsunfähigkeit**: Der Schuldner ist zahlungsunfähig, wenn er nicht in der Lage ist, die fälligen Zahlungspflichten zu erfüllen; in der Regel anzunehmen, wenn er seine Zahlungen eingestellt hat.
- **§ 18 InsO – Drohende Zahlungsunfähigkeit**: Voraussichtliche Unfähigkeit zur Erfüllung im Zeitraum **24 Monate** (Prognose).
- **§ 19 InsO – Überschuldung**: Vermögen deckt Verbindlichkeiten nicht, **es sei denn** Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich (positive Fortbestehensprognose). **Prognosehorizont 12 Monate** — die SanInsKG-Verkürzung auf 4 Monate galt nur bis 31.12.2023; seit 01.01.2024 wieder Regelfall 12 Monate. Eine erneute Verkürzung ist Stand Mai 2026 nicht in Kraft.
- **§ 15a InsO – Insolvenzantragspflicht**: 3 Wochen ab Eintritt der Zahlungsunfähigkeit, 6 Wochen ab Eintritt der Überschuldung.
- **§ 15b InsO – Zahlungsverbote nach Insolvenzreife**.
- **§ 1 StaRUG – Krisenfrüherkennung**: Pflicht der Geschäftsleitung zur fortlaufenden Krisenüberwachung; Frühwarnsystem mit 24-Monats-Horizont.

### Leitentscheidungen (Stand Mai 2026, vor Verwendung über amtliche/freie Quelle live verifizieren)

1. **BGH, Urteil vom 24.05.2005 - IX ZR 123/04** — Abgrenzung Zahlungsstockung/Zahlungsunfähigkeit; Liquiditätslücke von 10 Prozent oder mehr regelmäßig kritisch, wenn sie nicht kurzfristig nahezu vollständig geschlossen werden kann.
2. **BGH, Urteil vom 19.12.2017 - II ZR 88/16** — Liquiditätsstatus und Liquiditätsbilanz; Einbeziehung der innerhalb von drei Wochen fällig werdenden und eingeforderten Verbindlichkeiten (Passiva II).
3. **BGH, Urteil vom 28.06.2022 - II ZR 112/21** — Darlegung der Zahlungsunfähigkeit mit geordneter Liquiditätsgegenüberstellung und Buchhaltungsunterlagen; Belege und Zahlenbasis wichtiger als Scheingenauigkeit.
4. **Livecheck-Regel:** keine Entscheidung aus Modellwissen zitieren; vor Ausgabe Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer/Sachverhalt und tragende Aussage über `bundesgerichtshof.de`, `dejure.org` oder eine Nutzerquelle verifizieren.

Zitierweise: Pinpoint mit Randnummer; jüngere BGH-Entscheidungen zuerst; keine US-stare-decisis-Logik; keine pretrial discovery.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Berufsständischer Hintergrund (nicht im Vordergrund zitieren)

- **IDW S 11** (Stand 12.08.2021), Tz. 16 f., 31–37 — Beurteilung des Eröffnungsgrundes der Zahlungsunfähigkeit.
- **IDW S 6** — Anforderungen an Sanierungskonzepte und integrierte Planung. Hier nur Hintergrundmaßstab, der die BGH-Belege nicht ersetzt.

## Ablauf

**Schritt 0 – Format und Datenquelle**
Format-Wahl (Abschnitt *Format- und Padlet-Wahl*) und Banking-Wahl (Abschnitt *Bezugsquellen der Eingabedaten*) klären. Antworten merken.

**Schritt 1 – Datenaufnahme**
- Nutzer-Input parsen: PDFs (Bankauszüge, Rechnungen), CSV (Buchhaltungsexport), freier Text.
- Strukturieren in: (a) Anfangsbestand, (b) Einzahlungs-Buckets (Kundenforderungen, USt-Erstattungen, sonstige), (c) Auszahlungs-Buckets (Personal, SV, Lohnsteuer, USt-Zahlung, KSt/GewSt, Lieferanten, Miete, Leasing, Zins+Tilgung, sonstiges).
- Ausfallrisiko-Score für Debitoren (Top-Kunden, Mahnstand, Branche).

**Schritt 2 – Wochenraster bauen**
- Spalten: KW (Mo–So) ab KW Stichtag, Anfangsbestand Bank, + Einzahlungen je Bucket, − Auszahlungen je Bucket, **Endbestand**, **fällige Verbindlichkeiten in Folgewoche**, **3-Wochen-Lücke (kumuliert)**, **Lücken-Quote in %**, **Ampel**.
- Drei Sheets: `13-Wochen`, `26-Wochen`, `52-Wochen`. Letzteres monatlich aggregiert ab Monat 4.

**Schritt 3 – 3-Wochen-Test (§ 17 InsO)**
- Pro Woche: berechne `Lücke = max(0, fällige Verbindlichkeiten − verfügbare Mittel)`.
- Berechne `Lücke_3W = Summe der ungedeckten fälligen Verbindlichkeiten in t, t+1, t+2 minus erwartete Zugänge in t+1, t+2`.
- Berechne `Quote = Lücke_3W / fällige Verbindlichkeiten in t`.
- `Ampel = rot` wenn Quote ≥ 10 % und Lücke_3W am Ende der Periode nicht null; `gelb` wenn Quote ≥ 10 %, aber binnen 3 Wochen schließbar; sonst `grün`.

**Schritt 4 – Sensitivität (Best/Base/Worst)**
- Drei Spalten parallel: Zahlungseingang 100 %, 80 %, 60 % der Forderungen.
- Drei Spalten parallel: Auftragsausführung wie geplant, −10 %, −25 %.
- Ergebnis: Ampel je Szenario.

**Schritt 5 – Fortbestehensprognose und Sanierungsbrücke (12 Monate)**
- Aggregation auf Monatsebene; Übergang zu Ertrags- und Bilanzplanung (verzahnt).
- Prüfe zuerst die insolvenzrechtliche Fortbestehensprognose: bleibt die Zahlungsfähigkeit im Prognosezeitraum überwiegend wahrscheinlich erhalten?
- Prüfe danach, ob die Vorschau in eine Sanierungsplanung überführt werden muss. Das ist regelmäßig der Fall bei Bankgespräch, StaRUG, Schutzschirm, Eigenverwaltung, Insolvenzplan oder wenn Gläubiger einen Sanierungsnachweis verlangen.
- Für die Sanierungsbrücke sind diese Kernelemente abzuhaken:
 1. **Ausgangslage:** Unternehmensstruktur, Vermögens-, Finanz- und Ertragslage, Datenstand.
 2. **Krisenstadium und Ursachen:** Stakeholder-, Strategie-, Produkt-/Absatz-, Erfolgs-, Liquiditäts- oder Insolvenzkrise; Ursachen nicht nur Symptome.
 3. **Leitbild des sanierten Unternehmens:** Geschäftsmodell, Markt, Kostenbasis, Organisation, Finanzierung und Risikoprofil nach Sanierung.
 4. **Maßnahmen:** Innenfinanzierung, Außenfinanzierung, leistungswirtschaftliche und finanzwirtschaftliche Beiträge mit Kosten, Timing, Effekt und Belegstatus.
 5. **Integrierte Planung:** GuV, Planbilanz und Liquidität; Working Capital, Steuern, Zinsen, Tilgung, Mindestliquidität.
 6. **Szenarien:** Base Case und plausible Downside; bei hoher Unsicherheit weitere Sensitivitäten.
 7. **Ergebnis:** positive/negative Fortbestehensprognose und getrennt davon tragfähige/nicht tragfähige Sanierungsfähigkeit.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; wenn der konkrete Nachweis nicht live geprüft ist, als Prüfpunkt markieren.

Wenn ein Sanierungskonzept oder eine Bankunterlage gewünscht ist, nach dem Excel-Export an `idw-s6-integrierte-sanierungsplanung` übergeben. Die Vorschau liefert dann die Cash-Seite, nicht die gesamte Sanierungsbegründung.

**Schritt 6 – Abgrenzung handelsbilanzielle vs. insolvenzrechtliche Überschuldung**
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; wenn der konkrete Nachweis nicht live geprüft ist, als Prüfpunkt markieren.
- Qualifizierter Rangrücktritt (§ 39 Abs. 2 InsO) eliminiert Verbindlichkeit aus dem Status.
- Stille Reserven (insb. Sachanlagen, selbst erstellte immaterielle WG) sind zu aktivieren.
- Stille Lasten (Rückstellungsbedarf, Prozessrisiken, Bürgschaften) sind anzusetzen.
- Ergebnis: **Insolvenzfähige Überschuldung** nur, wenn rechnerische Unterdeckung **und** negative Fortführungsprognose.

**Schritt 7 – Ergebnis ausliefern**
- **Immer**: Excel-Datei `Liquiditaetsplan-<Firma>-KW<t>.xlsx` auf Basis von `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx` befüllen. Vorgegebenes Layout (Kategorien-Zeilen × KW-Spalten) **nicht verändern**. BGH-Block ab Zeile 42 (Aktiva I/II, Passiva I/II, Lücke abs., Lücke %, Ampel) und Block "Offene Forderungen" behalten. Formeln verwenden, nicht hartcodieren.
- **Wenn HTML-Padlet gewählt**: zusätzlich `liquiditaets-padlet-<Firma>-KW<t>.html` aus `assets/padlet/liquiditaets-padlet.html` ableiten (single-file, autark, localStorage, JSON-Export/Import, Live-Ampel nach BGH-Schema).
- **Wenn Markdown-Artefakt gewählt**: `liquiditaets-artefakt-<Firma>-KW<t>.md` auf Basis von `assets/markdown/liquiditaets-artefakt-vorlage.md` ausfüllen.
- Bei jeder Folgemeldung des Nutzers das gewählte Artefakt aktualisieren und die neue Version unter demselben Asset-Namen liefern.

**Schritt 8 – Memo (nur auf Anfrage)**
Erst nach Auslieferung der Vorschau anbieten:

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Subsumtion nach §§ 17, 19 InsO erstellen?

Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; wenn der konkrete Nachweis nicht live geprüft ist, als Prüfpunkt markieren.

## Ausgabeformat

1. **Excel** (immer) auf Basis von `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`. KW-Spalten × Kategorien-Zeilen wie in der Vorlage; BGH-Block (Aktiva I/II, Passiva I/II, Lücke abs., %, Ampel) ab Zeile 42; Block "Offene Forderungen"; Hinweise zur BGH-Rspr. Sheet `Liquiditätsplan` (Werte) und Sheet `BGH-Schema` (Erläuterung). Wochenstichtag = Freitag.
2. **HTML-Padlet** (auf Wunsch): autarke single-file HTML aus `assets/padlet/liquiditaets-padlet.html`, live rechnend, localStorage-Speicher, JSON-Export/-Import.
3. **Markdown-Artefakt** (auf Wunsch): `assets/markdown/liquiditaets-artefakt-vorlage.md` als Vorlage; bei jeder Folgemeldung neu geschrieben.
4. **Memo** (nur auf Anfrage): Kurz-Gutachten im Gutachtenstil, höchstens zwei Seiten, DOCX oder Markdown nach Wahl.
5. **Hinweispflicht § 102 StaRUG** wenn nicht-Geschäftsleiter beauftragt (z. B. Steuerberatermandat) — Textbaustein anbieten.

## Beispiel

**Sachverhalt**: Edelholz Manufaktur Berlin GmbH, 20 Mitarbeiter, Jahresumsatz 2,1 Mio. EUR, Stichtag 18.05.2026, Kontostand 18.500 EUR, Kontokorrent 150.000 EUR zu 92 % ausgeschöpft, offene LuL 187.000 EUR (davon 64.000 EUR überfällig), SV-Rückstand 38.000 EUR, USt-Vorauszahlung 14.200 EUR fällig 10.06.2026, Großauftrag 145.000 EUR mit Lieferung KW 28 und Zahlungsziel 30 Tage netto.

**Gutachtenstil**:

Die Prüfung stützt sich auf die BGH-Linie zur Liquiditätslücke, zum Drei-Wochen-Zeitraum und zu Passiva II; konkrete Zitate werden erst nach Livecheck ausgegeben.

*Handlungsempfehlung*: Antragspflicht 3 Wochen ab Eintritt § 17 InsO (KW 22) bzw. 6 Wochen ab § 19 InsO. Parallel Prüfung StaRUG-Restrukturierungsrahmen nur möglich bei rein **drohender** Zahlungsunfähigkeit – nicht mehr eröffnet, wenn § 17 InsO bereits eingetreten ist. Hinweis nach § 102 StaRUG durch beauftragten Steuerberater zu erteilen.

## Risiken und typische Fehler

- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; wenn der konkrete Nachweis nicht live geprüft ist, als Prüfpunkt markieren.
- **3-Wochen-Frist statisch rechnen**: Die Frist läuft ab dem **Eintritt** der Zahlungsunfähigkeit, nicht ab Erstellung des Liquiditätsplans.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; wenn der konkrete Nachweis nicht live geprüft ist, als Prüfpunkt markieren.
- **Kreditlinien unkritisch ansetzen**: Nur **zugesagte und ziehungsfähige** Linien zählen; gekündigte oder ausgeschöpfte Linien nicht.
- **Großaufträge ohne Zahlungseingangsrisiko ansetzen**: Realistische Annahmen mit Ausfall- und Skonto-Quoten; immer Sensitivität (Worst Case).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; wenn der konkrete Nachweis nicht live geprüft ist, als Prüfpunkt markieren.
- **USt- und LSt-Rückstände kleinreden**: Diese sind starke Insolvenzindizien und führen oft zur Anzeige durch Finanzamt/Krankenkasse (§ 15a Abs. 4 InsO).
- **Personalkosten unterschätzen**: Lohn + AG-Anteil SV + KK-Beiträge = ca. 1,28× Bruttolohn; monatliche Drittellast SV-Beiträge.
- **SanInsKG-Stand übersehen**: Prognosehorizont § 19 InsO war zwischen 09.11.2022 und 31.12.2023 auf 4 Monate verkürzt. Seit 01.01.2024 gilt wieder der reguläre Prognosezeitraum von 12 Monaten. Stand Mai 2026: keine erneute Verkürzung in Kraft. Am Bewertungsstichtag dennoch verifizieren.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

- Bei 🔴 § 17 InsO sofort an `zahlungsunfaehigkeit-pruefung-17-inso` und `antragspflicht-15a-inso` (Plugin `insolvenzrecht`).
- Bei indizierter insolvenzrechtlicher Überschuldung an `überschuldung-prüfung-19-inso` (Plugin `insolvenzrecht`).
- Für die wochenaktuelle Kurzfrist-Sicht: Schwester-Skill `liquiditaetsvorschau-3wochen` (dieses Plugin).
- Für die gerichtsfeste Liquiditätsbilanz als Beweismittel: `liquiditaetsvorschau-insolvenzrechtlich` (dieses Plugin).
- Für Sanierungskonzept- und Bankfähigkeit: `idw-s6-integrierte-sanierungsplanung` (dieses Plugin).

## Triage — Liquiditaetsvorschau Einordnung

Bevor losgelegt wird, klaere:

1. **Zweck der Vorschau?** ZU-Pruefung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Glaeubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) für insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) für langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Fuer InsO-Beurteilung tag-genau festlegen; für Prognose ab aktuellem Tag.
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
