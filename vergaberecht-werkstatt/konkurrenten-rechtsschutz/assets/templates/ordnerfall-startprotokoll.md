# Ordnerfall-Startprotokoll Konkurrentenrechtsschutz

Zweck: Wenn ein Projektordner, ZIP, Akteneinsichtsordner, Portalexport oder Dateistapel übergeben wird, ohne dass ein Skill ausgewählt wurde, startet der Konkurrent direkt mit diesem Protokoll. Nicht zuerst nach Skillnamen fragen.

## 1. Fallkarte

| Feld | Befund |
|---|---|
| Unternehmen/Kanzlei |  |
| Rolle im Verfahren | Konkurrent, unterlegener Bieter, ausgeschlossener Bieter, Zuschlagsprätendent, Kanzlei |
| Verfahren/Los |  |
| Verfahrensstand | Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nichtabhilfe, VK, OLG, Zuschlag, Vertrag |
| Ziel heute | Unterlagen ändern, Zuschlag stoppen, Konkurrent ausschließen, neue Wertung, Akteneinsicht, Kostenmemo |
| Rechtsweg/Schwellenwert | Oberschwelle, Unterschwelle, Sektoren, Konzession, VOB/A, offen |
| Stärkster Angriff | Billigzuschlag, Produkt-/Formatsperre, Wertung, Eignung, de-facto-Vergabe, Akteneinsicht |
| Empfohlener erster Output | Rüge, VK-Antrag, Zuschlagssperre, Akteneinsicht, OLG, Vergleich, Kostenmemo |

## 2. Quelleninventar

| Quelle | Datei/System | Datum/Version | Schlüssel/Hash | Angriff/Bezug | Beweiswert | Lücke |
|---|---|---|---|---|---|---|
| Bekanntmachung/Portal |  |  |  | Fristen, CPV, Eignung, Zuschlag |  |  |
| Unterlagen/LV |  |  |  | GAEB, XML, Excel, PDF, Produkt-/Formatbindung |  |  |
| Wertung/Aufklärung |  |  |  | Preis, Qualität, Dokumentation, § 60 VgV |  |  |
| Konkurrent/Eignung |  |  |  | Referenz, Ausschlussgrund, Register, Selbstreinigung |  |  |
| Streitstoff |  |  |  | Rüge, Nichtabhilfe, VK/OLG, Akteneinsicht |  |  |
| Portal-/Legacy-Beweis |  |  |  | Screenshot, Upload, SAP/ERP/AVA/DMS, API, MCP |  |  |

## 3. Verarbeitungsstatus

| Paket | Dateien/Volumen | Hash geprüft | Status | Ergebnis oder Fehler | Nächster Lauf |
|---|---|---|---|---|---|
| 01 |  |  | offen, läuft, fertig oder fehlerhaft |  |  |

Ab 50 Dateien oder 250 MB höchstens 20 Dateien oder 100 MB je Paket verarbeiten. Frist- und Zugangsbelege zuerst, große PDF- und Office-Dateien einzeln. Unveränderte Dateien mit identischem Hash nicht erneut lesen; nach Fehlern beim letzten vollständigen Paket fortsetzen und die betroffene Datei als Beweislücke markieren.

## 4. Fristenampel

| Frist | Startpunkt | Ablauf | Beleg | Sofortmaßnahme |
|---|---|---|---|---|
| Angebots-/Teilnahmeantragsfrist |  |  |  |  |
| Rügeobliegenheit |  |  |  |  |
| § 134 GWB/Stillhaltefrist |  |  |  |  |
| Nichtabhilfe/15 Kalendertage |  |  |  |  |
| VK/OLG/§ 135 GWB |  |  |  |  |

## 5. Output-Weiche

| Lage | Primärer Output | Spezialskill |
|---|---|---|
| Billigzuschlag oder Preisautomatismus | Preisformeltest und Rüge-/VK-Baustein | `billigzuschlag-angreifen` |
| Produkt-, Material- oder Formatbindung | Gleichwertigkeitsangriff | `produktneutralitaet-und-leistungsbeschreibung`, `unterlagen-lv-formatangriff` |
| Wertungs- oder Dokumentationslücke | Angriffslinie mit Aktenbeleg | `wertungsangriff-und-dokumentationsluecken` |
| Konkurrent ist auszuschließen | Beweis- und Akteneinsichtsplan | `eignungs-und-ausschlussangriff-konkurrent` |
| Zuschlag droht oder Nichtabhilfe liegt vor | VK-Antrag und Zuschlagssperre | `nachpruefungsantrag-konkurrent-vk`, `eilantrag-zuschlagssperre-169` |

## 6. Schlusskontrolle

- Ist die rote Frist berechnet oder als Lücke markiert?
- Hat jeder Angriff einen Beleg, eine Akteneinsichtslücke oder einen Beweisauftrag?
- Ist der beantragte Rechtsschutz eindeutig?
- Gibt es genau eine empfohlene Bedienhandlung?
