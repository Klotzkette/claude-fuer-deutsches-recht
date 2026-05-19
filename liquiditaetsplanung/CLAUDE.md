# Plugin Liquiditätsplanung (`liquiditaetsplanung`) – Modellhinweise

Dieses Plugin ist **autark**. Es funktioniert als **eigenständiges Power-Plugin Liquiditätsvorschau**. Wenn `insolvenzrecht` und/oder `steuerberater-werkzeuge` ebenfalls installiert sind, werden Übergaben angeboten — sie sind aber keine Voraussetzung.

## Pflichten beim Einsatz der Liquiditäts-Skills

1. **Excel ist Default.** Vorlage `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx` benutzen, Layout (Kategorien-Zeilen × KW-Spalten, Freitag-Stichtag) **nicht verändern**. BGH-Block ab Zeile 42 (Aktiva I/II, Passiva I/II, Lücke abs./%, Ampel) und Block „Offene Forderungen“ ausfüllen. Werte über Formeln, kein Hartcoding.
2. **Format-Wahl** einmal am Anfang erfragen: Excel allein, Excel + HTML-Padlet, oder Excel + Markdown-Artefakt. Antwort merken. Default bei Schweigen: Excel + HTML-Padlet.
3. **Banking-Wahl** einmal am Anfang erfragen: manuell, Datei-Import (CAMT.053, MT940, CSV, DATEV-OPOS) oder Connector (zuvor `list_external_tools` mit `banking`, `psd2`, `fintap`, `gocardless`).
4. **BGH-Schema strikt einhalten**: Passiva II zwingend einbeziehen (BGH II ZR 88/16). Quote = Lücke ÷ Σ(P I + P II) (Volumeneffekt). Titulierte Forderungen mit Nennwert (BGH IX ZR 229/22). Beurteilung allein nach objektiven Umständen (BGH II ZR 139/23).
5. **Memo nur auf Anfrage.** Erst Vorschau ausliefern, dann anbieten.
6. **Wochenaktuell zum Freitag.** Stichtag = Montag der laufenden KW. Vorschau bis Freitag KW *t+2*.
7. **Verhältnis zu offenen Forderungen** ausweisen (Deckungsgrad = offene Forderungen ÷ Lücke).
8. **PDFs als Belege benutzen.** `references/rechtsprechung/` enthält die Volltexte der Leitentscheidungen; davor zitieren, nicht IDW S 6/S 11 in den Vordergrund stellen.

## Sprachregelung

- „Auslöser“ statt „Hooks“, „Agentenrezepte“ statt „Cookbooks“.
- Pinpoint-Zitierweise mit Randnummer; jüngere BGH-Entscheidungen zuerst.
- Deutsche Kommentartradition vor US-stare-decisis-Logik. Keine pretrial discovery.
- Etablierte englische Begriffe (NDA, SPA, MAC, Stakeholder, Compliance) belassen.

## Verhältnis zu Schwester-Plugins

- `steuerberater-werkzeuge` hält Spiegelversionen der 3-Wochen- und 13/26/52-Wochen-Skills (mit Steuerberater-Sicht und Hinweis auf § 102 StaRUG).
- `insolvenzrecht` hält die insolvenzrechtliche Liquiditätsbilanz als Beweismittel sowie die formalen Prüf-Skills (§§ 15a, 17, 18, 19 InsO).
- Bei 🔴: an `zahlungsunfaehigkeit-pruefung-17-inso`, `antragspflicht-15a-inso` (Plugin `insolvenzrecht`) übergeben, sofern installiert.
