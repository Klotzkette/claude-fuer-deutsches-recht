---
name: stb-liquiditaetsvorschau-3wochen
description: "Kurzfristige Drei-Wochen-Liquiditaetsvorschau fuer GmbH oder UG zur wochentlichen Krisenfrueherkennung. Anwendungsfall Steuerberater will schnell pruefen ob Zahlungsunfaehigkeit nach § 17 InsO droht oder schon vorliegt. BGH-Schema 10-Prozent-Luecke und drei Wochen Schliessbarkeit BGHZ 163. Hinweispflicht Steuerberater § 102 StaRUG bei roter Ampel. Output Drei-Wochen-Tabelle Ampel-Bewertung Uebergang zu Langfristplanung oder insolvenzrechtlichem Schwester-Plugin bei roter Ampel. Abgrenzung zu stb-liquiditaetsvorschau-3-6-12-monate Langfristversion."
---

# Drei-Wochen-Liquiditätsvorschau (§ 17 InsO Vorprüfung, § 1 StaRUG)

## Powerplugin-Hinweis

**Die vollständige, fachlich autarke Version dieses Skills lebt im Plugin Liquiditätsplanung (`liquiditaetsplanung`)** (Power-Plugin Liquiditätsvorschau) — mit BGH-Schema Passiva II (BGHZ 217, 129), Volumeneffekt der Quote, titulierten Forderungen mit Nennwert (BGH IX ZR 229/22), objektiver Beurteilung (BGH II ZR 139/23), Excel-Vorlage, optionalem HTML-Padlet oder Markdown-Artefakt und Banking-Wahl. Wenn `liquiditaetsplanung` installiert ist, dorthin übergeben.

Wenn nicht installiert, hier nach dem Steuerberater-spezifischen Schema arbeiten und am Ende ausdrücklich die Hinweispflicht nach § 102 StaRUG dokumentieren.

## Zweck

Dieser Skill erstellt für eine GmbH/UG/AG eine **kurzfristige Drei-Wochen-Liquiditätsvorschau** — die kleinste sinnvolle Einheit der laufenden Krisenfrüherkennung nach § 1 StaRUG und die direkte Ableitung des BGH-Schemas zur Zahlungsunfähigkeit (§ 17 InsO).

Er ist als **wöchentliche Routine** gedacht: jeden Montag mit aktualisierten Banksalden und Fälligkeitsdaten in fünf bis zehn Minuten durchlaufen, Ampel ablesen, dokumentieren. Für die vollständige rollierende Planung über 13/26/52 Wochen siehe den Schwester-Skill `stb-liquiditaetsvorschau-3-6-12-monate` (gleiches Plugin) bzw. das Plugin Liquiditätsplanung (`liquiditaetsplanung`).

Anwendungsfälle:

- Wöchentliche Geschäftsführer-Sitzung in einer KMU-GmbH mit angespannter Liquidität.
- Dauermandat des Steuerberaters mit Krisenfrüherkennungsauftrag.
- Vorprüfung vor dem Bankgespräch oder vor einer StaRUG-Anzeige.
- Erstindikation, ob ein Antragspflicht-Check nach § 15a InsO ausgelöst werden muss.

## Eingaben

Minimum (für die Schnellrunde):

- **Eröffnungsbestand liquider Mittel** zum Stichtag (Mo): Bank, Kasse, ungenutzte zugesagte Kreditlinien (nicht ausgeschöpfte und nicht gekündigte!).
- **Fällige Verbindlichkeiten** der nächsten 3 Kalenderwochen, getrennt nach: Lohn/Gehalt + AG-Anteil SV, Lohnsteuer, Umsatzsteuer-Vorauszahlung, Sozialversicherungsbeiträge (monatliche Drittellast), Miete/Leasing, kritische Lieferanten, Zins+Tilgung, sonstige.
- **Erwartete Zahlungseingänge** der nächsten 3 Wochen aus Debitoren (mit realistischem Ausfallrisiko / Skonto).
- **Stundungen, Mahnstand, Lastschriftrückläufer** der letzten 4 Wochen (Indizien nach BGH NJW 2007, 78 Rn. 16 ff.).

Wenn Daten fehlen: Annahmen explizit dokumentieren und im Worst Case rechnen.

## Rechtlicher Rahmen

### Primärnormen

- **§ 17 InsO** – Zahlungsunfähigkeit (Hauptmaßstab).
- **§ 18 InsO** – drohende Zahlungsunfähigkeit (24-Monats-Prognose, hier nur Hinweisfunktion).
- **§ 15a InsO** – Insolvenzantragspflicht: 3 Wochen ab Eintritt § 17 InsO.
- **§ 1 StaRUG** – fortlaufende Krisenüberwachungspflicht der Geschäftsleitung.
- **§ 102 StaRUG** – Hinweispflicht beratender Berufe (Steuerberater, Wirtschaftsprüfer, Rechtsanwälte).

### Leitentscheidungen

1. BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 12–19: Definition Zahlungsunfähigkeit; **Liquiditätslücke ≥ 10 %** und **nicht binnen 3 Wochen schließbar**; Abgrenzung zur bloßen Zahlungsstockung.
2. BGH, Urt. v. 12.10.2006 – IX ZR 228/03, NJW 2007, 78 Rn. 16–22: Indizienkatalog der Zahlungsunfähigkeit (SV-Rückstände, Stundungen, Mahnverfahren, Lastschriftrückläufer).
3. BGH, Urt. v. 26.01.2017 – IX ZR 285/14, BGHZ 213, 374: Hinweispflicht des Steuerberaters bei Anzeichen einer Insolvenzreife (Vorläufer § 102 StaRUG).

### Kommentarliteratur

1. *K. Schmidt/Herchen*, in: K. Schmidt, Insolvenzordnung, 20. Aufl. 2023, § 17 InsO Rn. 5–35: Liquiditätsbilanz nach BGH-Konzept, 10-%-Grenze, 3-Wochen-Horizont, Behandlung von Stundungen und Kreditlinien.
2. *Pape/Schaltke*, in: Pape/Uhländer, StaRUG, 1. Aufl. 2021, § 1 StaRUG Rn. 10–30: Geschäftsleiterpflichten zur Krisenfrüherkennung; integrierte Planung als Pflichtprogramm.
3. *BeckOK StaRUG/Skauradszun*, 8. Ed. Stand 04.2025, § 102 StaRUG: Hinweispflicht beratender Berufe, Auslöser, Dokumentation.

## Ablauf

**Schritt 1 – Stichtag und Eröffnungsbestand**
- Stichtag = Montag der laufenden KW.
- Anfangsbestand = Banksalden + Kasse + zugesagte, ziehungsfähige Kreditlinie (nicht ausgeschöpft, nicht gekündigt).

**Schritt 2 – Wochenraster (3 Spalten)**
- Spalten KW *t*, *t+1*, *t+2*.
- Pro Spalte: Anfangsbestand, Einzahlungen je Bucket, Auszahlungen je Bucket, Endbestand, fällige Verbindlichkeiten der Folgewoche.

**Schritt 3 – 3-Wochen-Test (BGH BGHZ 163, 134)**
- `Lücke_t = max(0, fällige Verbindlichkeiten in t − verfügbare Mittel in t)`
- `Lücke_3W = Summe aller offen bleibenden fälligen Verbindlichkeiten in t, t+1, t+2 abzüglich erwarteter Zugänge in t+1, t+2`
- `Quote = Lücke_3W / fällige Verbindlichkeiten in t`
- **Ampel**:
  - 🟢 **Grün**: Quote < 10 % (Zahlungsfähigkeit gegeben).
  - 🟡 **Gelb (Zahlungsstockung)**: Quote ≥ 10 %, aber Lücke_3W am Ende von *t+2* gleich null (binnen 3 Wochen schließbar).
  - 🔴 **Rot (Zahlungsunfähigkeit § 17 InsO indiziert)**: Quote ≥ 10 % **und** Lücke_3W am Ende von *t+2* > 0 (nicht binnen 3 Wochen schließbar) — BGH BGHZ 163, 134 Rn. 14.

**Schritt 4 – Indizienprüfung (BGH NJW 2007, 78)**
- Hinweise auf Zahlungsunfähigkeit auch bei 🟡: SV-Rückstände, Lastschriftrückläufer, Stundungsanfragen, eingestellte Zahlungen an Finanzamt/Krankenkasse. Falls ≥ 2 Indizien → Eskalation wie 🔴.

**Schritt 5 – Ergebnis und Eskalation**
- 🟢: Routine dokumentieren, nächste Woche erneut.
- 🟡: Engpasswoche identifizieren, Maßnahmen (Skontofinanzierung, Stundungsverhandlung, Avalziehung, Forderungsbeschleunigung); Dokumentation in Geschäftsleiter-Protokoll nach § 1 StaRUG.
- 🔴: **Hinweispflicht § 102 StaRUG** prüfen (bei Mandant). Übergabe an Skill `zahlungsunfaehigkeit-pruefung-17-inso` und `antragspflicht-15a-inso` aus Plugin `insolvenzrecht`. Frist § 15a InsO (3 Wochen) läuft ab tatsächlichem Eintritt der Zahlungsunfähigkeit — nicht ab Erstellung des Plans.

## Ausgabeformat

1. **Kompakte Tabelle** (3 Spalten t, t+1, t+2) mit Anfangsbestand, Einzahlungen, Auszahlungen, Endbestand, Lücke, Quote, Ampel.
2. **Indizienliste** (Häkchenliste BGH NJW 2007, 78).
3. **Kurzfazit im Gutachtenstil** mit Zitat BGH BGHZ 163, 134 und konkreter Wochenangabe für den frühesten Roteintritt.
4. **Handlungsempfehlung** je Ampelfarbe.
5. **Hinweis nach § 102 StaRUG** als Textbaustein, wenn 🔴 und Mandantenverhältnis besteht.

## Beispiel

**Sachverhalt**: Edelholz Manufaktur Berlin GmbH, Stichtag Mo 18.05.2026, Bank 18.500 EUR, Kontokorrent 150.000 EUR zu 92 % ausgeschöpft (12.000 EUR Rest), keine Kasse. Fällige Verbindlichkeiten KW 21: Lohn + AG-SV 42.000 EUR, Lieferant kritisch 19.500 EUR. KW 22: SV-Beitrag 14.800 EUR, Miete 7.200 EUR. KW 23: USt-VZ 14.200 EUR, Leasing 3.400 EUR. Erwartete Eingänge: KW 22 18.000 EUR (Skonto-Sicherheit 80 %), KW 23 9.500 EUR.

**Auswertung**:
- KW 21: Verfügbar 30.500 EUR vs. Fällig 61.500 EUR → Lücke 31.000 EUR (Quote 50 %).
- KW 22: Eingang 14.400 EUR (80 % von 18.000), verbleibende Lücke kumuliert 38.600 EUR.
- KW 23: Eingang 9.500 EUR, verbleibende Lücke 50.700 EUR plus neue Fälligkeit 17.600 EUR.

**Ergebnis**: Quote in KW 21 = 50 % (≥ 10 %), Lücke_3W am Ende von KW 23 ≈ 68.300 EUR (≠ 0). Damit **nicht binnen 3 Wochen schließbar** → 🔴 **Zahlungsunfähigkeit § 17 InsO indiziert ab KW 21** (BGH BGHZ 163, 134 Rn. 14).

**Handlung**: Übergabe an `antragspflicht-15a-inso` und `zahlungsunfaehigkeit-pruefung-17-inso`. Steuerberater löst Hinweis nach § 102 StaRUG aus (BGH BGHZ 213, 374). Frist § 15a InsO (3 Wochen) läuft ab tatsächlichem Eintritt.

## Typische Fehler

- **Kontokorrent voll als Liquidität ansetzen**: Nur ungenutzter, zugesagter und ziehungsfähiger Teil zählt.
- **Stundungen als Liquidität werten**: Verschieben die Fälligkeit, sind aber Indiz für Zahlungsunfähigkeit (BGH NJW 2007, 78 Rn. 18).
- **Aussetzung der Vollziehung (§ 361 AO / § 69 FGO) wie eine Stundung behandeln**: AdV hemmt nur die Vollziehung; die Fälligkeit der Steuerforderung bleibt unberührt. AdV-Beträge sind weiter **Passiva I**, soweit nicht zusätzlich eine schriftliche § 222 AO-Stundung mit Fälligkeitsverschiebung über den Stichtag hinaus vorliegt. Eine Herausnahme von AdV-Beträgen aus Passiva I führt zu falschem "nicht zahlungsunfähig"-Ergebnis.
- **3-Wochen-Frist statisch ab Planerstellung rechnen**: Sie läuft ab **Eintritt** der Zahlungsunfähigkeit.
- **Erwartete Großeingänge zu 100 % ansetzen**: Realistische Ausfall- und Skontoquote, im Zweifel Worst Case.
- **SV-Rückstände kleinreden**: Starkes Indiz und Anzeigequelle (§ 15a Abs. 4 InsO; BGH NJW 2007, 78).
- **Lohnsteuer aufschieben**: Lohnsteuer-Rückstände sind ein klassisches Insolvenzindiz und persönlich haftungsauslösend.

## Quellenpflicht

Mindestens zwei Belege im BGH-Stil und zwei Kommentarbelege im Bearbeiter-Stil. Berufsständische Verlautbarungen (StaRUG-Kommentare) gesondert zitieren. Zitierweise siehe Repository-`references/zitierweise.md`.

## Übergabe

Bei roter Ampel sofort auf das Plugin `insolvenzrecht` umschwenken:
- `zahlungsunfaehigkeit-pruefung-17-inso` — formale Subsumtion und gerichtsfähiger Liquiditätsstatus.
- `antragspflicht-15a-inso` — Fristenlauf, Haftung Geschäftsleiter, § 15b InsO Zahlungsverbote.
- `liquiditaetsvorschau-insolvenzrechtlich` — gerichtsfähige Liquiditätsbilanz als Beweismittel.

Für die mittel- und langfristige Sicht: Schwester-Skill `stb-liquiditaetsvorschau-3-6-12-monate` aus diesem Plugin oder gebündelt im Plugin Liquiditätsplanung (`liquiditaetsplanung`).
