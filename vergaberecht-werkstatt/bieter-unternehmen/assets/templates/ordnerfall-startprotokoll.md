# Ordnerfall-Startprotokoll Bieter

Zweck: Wenn ein Projektordner, ZIP, Angebotsordner, Portalexport oder Dateistapel übergeben wird, ohne dass ein Skill ausgewählt wurde, startet der Bieter direkt mit diesem Protokoll. Nicht zuerst nach Skillnamen fragen.

## 1. Fallkarte

| Feld | Befund |
|---|---|
| Unternehmen/Kanzlei |  |
| Rolle im Verfahren | Bewerber, Bieter, Zuschlagsprätendent, Beigeladener, Nachunternehmer, Kanzlei |
| Verfahren/Los |  |
| Verfahrensstand | Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, VK, OLG, Vertrag, Schadensersatz |
| Ziel heute | Go-No-Go, Angebot bauen, Qualitätsvorsprung zeigen, Rüge, VK-Antrag, Uploadpaket |
| Rechtsweg/Schwellenwert | Oberschwelle, Unterschwelle, Sektoren, Konzession, VOB/A, offen |
| Stärkste Angebots- oder Rechtsfrage |  |
| Empfohlener erster Output | Bieterfrage, Angebotsmapping, Nachweismatrix, Rüge, VK-Antrag, Uploadpaket |

## 2. Quelleninventar

| Quelle | Datei/System | Datum/Version | Schlüssel/Hash | Angebotsbezug | Beweiswert | Lücke |
|---|---|---|---|---|---|---|
| Bekanntmachung/Portal |  |  |  | Fristen, CPV, Eignung, Zuschlag |  |  |
| Unterlagen/LV |  |  |  | GAEB, XML, Excel, PDF, Pflichtfelder |  |  |
| Angebotsdaten |  |  |  | Kalkulation, Konzept, Referenzen, Nachweise |  |  |
| Qualitätsvorsprung |  |  |  | Tempo, Verfügbarkeit, Personal, Servicelevel, Lebenszyklus |  |  |
| Streitstoff |  |  |  | Bieterfrage, Rüge, Nichtabhilfe, VK/OLG |  |  |
| Upload/Rückkanal |  |  |  | Portal, Signatur, DMS, API, MCP |  |  |

## 3. Verarbeitungsstatus

| Paket | Dateien/Volumen | Hash geprüft | Status | Ergebnis oder Fehler | Nächster Lauf |
|---|---|---|---|---|---|
| 01 |  |  | offen, läuft, fertig oder fehlerhaft |  |  |

Ab 50 Dateien oder 250 MB höchstens 20 Dateien oder 100 MB je Paket verarbeiten. Bekanntmachung und Fristdokumente zuerst, große PDF- und Office-Dateien einzeln. Unveränderte Dateien mit identischem Hash nicht erneut lesen; nach Fehlern beim letzten vollständigen Paket fortsetzen.

## 4. Fristenampel

| Frist | Startpunkt | Ablauf | Beleg | Sofortmaßnahme |
|---|---|---|---|---|
| Angebots-/Teilnahmeantragsfrist |  |  |  |  |
| Bieterfrage/Rügeobliegenheit |  |  |  |  |
| § 134 GWB/Stillhaltefrist |  |  |  |  |
| Nichtabhilfe/15 Kalendertage |  |  |  |  |
| VK/OLG/§ 135 GWB |  |  |  |  |

## 5. Output-Weiche

| Lage | Primärer Output | Spezialskill |
|---|---|---|
| Unterlagen ungeordnet oder lückenhaft | Dokumentenmatrix und Fragenliste | `dokumente-intake`, `unterlagen-und-lv-datenformate-auslesen` |
| Angebot im vorgegebenen Format nötig | Angebotsmapping und Uploadpaket | `angebot-in-vorgegebenem-format-erstellen` |
| Teurer, aber fachlich stärker | Qualitätsbrücke und Punktebeleg | `qualitaetsvorsprung-nachweisen` |
| Fehlerhafte Unterlage oder Formatblockade | Bieterfrage oder Rüge | `bieterfragen-antworten-management`, `21-ruegeschreiben-erstellen` |
| Nichtabhilfe, drohender Zuschlag oder VK | Nachprüfungsfahrplan | `nachpruefungsantrag-powerdraft`, `nachpruefungsverfahren-vk` |

## 6. Schlusskontrolle

- Ist die rote Frist berechnet oder als Lücke markiert?
- Ist der nächste Freigabeinhaber im Bieterteam benannt?
- Ist die nächste Datei, Anlage oder Portalhandlung eindeutig?
- Gibt es genau eine empfohlene Bedienhandlung?
