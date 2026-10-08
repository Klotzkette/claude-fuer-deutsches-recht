# Ordnerfall-Startprotokoll Vergabestelle

Zweck: Wenn ein Projektordner, ZIP, DMS-Export, Portalexport oder Dateistapel übergeben wird, ohne dass ein Skill ausgewählt wurde, startet die Vergabestelle direkt mit diesem Protokoll. Nicht zuerst nach Skillnamen fragen.

## 1. Fallkarte

| Feld | Befund |
|---|---|
| Auftraggeber/Fachbereich |  |
| Rolle im Verfahren | Vergabestelle, Fachbereich, Zentrale Vergabestelle, Justiziariat, Fördermittelempfänger, beauftragte Stelle |
| Verfahren/Los |  |
| Verfahrensstand | Planung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, VK, OLG, Vertrag |
| Ziel heute | Bedarf klären, LV bauen, Bestangebot sichern, Rüge behandeln, VK/OLG verteidigen, Berichtigung/Upload |
| Rechtsweg/Schwellenwert | Oberschwelle, Unterschwelle, Sektoren, Konzession, VOB/A, Fördermittel, offen |
| Stärkste Rechtsfrage |  |
| Empfohlener erster Output | Vermerk, Matrix, Bieterfragenantwort, Rügeerwiderung, VK-Stellungnahme, Uploadpaket |

## 2. Quelleninventar

| Quelle | Datei/System | Datum/Version | Schlüssel/Hash | Verfahrensbezug | Beweiswert | Lücke |
|---|---|---|---|---|---|---|
| Bekanntmachung/Portal |  |  |  | Fristen, CPV, Eignung, Zuschlag |  |  |
| Unterlagen/LV |  |  |  | GAEB, XML, Excel, PDF, Leistungsbeschreibung |  |  |
| Wirklichkeitsdaten |  |  |  | Bauwerk, Zustand, Kosten, Bauzeit, Klima, Norm |  |  |
| Wertung/Akte |  |  |  | Zuschlagsmatrix, Preis, Qualität, Aufklärung |  |  |
| Streitstoff |  |  |  | Bieterfrage, Rüge, Nichtabhilfe, VK/OLG |  |  |
| Upload/Rückkanal |  |  |  | eForms, TED, DVAL, Portal, DMS, MCP |  |  |

## 3. Verarbeitungsstatus

| Paket | Dateien/Volumen | Hash geprüft | Status | Ergebnis oder Fehler | Nächster Lauf |
|---|---|---|---|---|---|
| 01 |  |  | offen, läuft, fertig oder fehlerhaft |  |  |

Ab 50 Dateien oder 250 MB höchstens 20 Dateien oder 100 MB je Paket verarbeiten. Fristdokumente zuerst, große PDF- und Office-Dateien einzeln. Unveränderte Dateien mit identischem Hash nicht erneut lesen; nach Fehlern beim letzten vollständigen Paket fortsetzen.

## 4. Fristenampel

| Frist | Startpunkt | Ablauf | Beleg | Sofortmaßnahme |
|---|---|---|---|---|
| Angebots-/Teilnahmeantragsfrist |  |  |  |  |
| Bieterfragen/Klarstellung |  |  |  |  |
| § 134 GWB/Stillhaltefrist |  |  |  |  |
| Nichtabhilfe/15 Kalendertage |  |  |  |  |
| VK/OLG/§ 135 GWB |  |  |  |  |

## 5. Output-Weiche

| Lage | Primärer Output | Spezialskill |
|---|---|---|
| Unterlagen ungeordnet oder lückenhaft | Dokumentenmatrix und Lückenliste | `dokumente-intake`, `unterlagen-luecken` |
| Bestes Angebot statt Billigpreis absichern | Bestwertungsvermerk und Wertungsmatrix | `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen` |
| Daten aus Legacy-Systemen nutzbar machen | Mapping-Manifest und Freigabeauftrag | `legacy-systeme-integration`, `wirklichkeitsdaten-beschaffung-steuern` |
| LV/Format/Upload vorbereiten | LV-Roundtrip und Uploadpaket | `vergabeunterlagen-lv-datenformate-bereitstellen` |
| Rüge, VK oder OLG | Streitdashboard und Schriftsatzfahrplan | `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer` |

## 6. Schlusskontrolle

- Ist die rote Frist berechnet oder als Lücke markiert?
- Ist der nächste Freigabeinhaber benannt?
- Ist die nächste Datei, Aktenstelle oder Portalhandlung eindeutig?
- Gibt es genau eine empfohlene Bedienhandlung?
