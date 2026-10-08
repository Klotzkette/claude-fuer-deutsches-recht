---
name: mandat-triage-vergaberecht
description: 'Neue Vergabeakte ohne Skill-Auswahl starten: Bedarf, Datenquellen, Verfahrensstand, Zuständigkeit, Fristen, Vergabereife, Qualitätsziel, Dokumentationslücke, Dateiformat, Rechtsschutzrisiko und nächsten Behördenoutput bestimmen.'
---

# Neue Vergabeakte der Vergabestelle automatisch triagieren

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Kaltstartbefehl

Bei `Hier ist die neue Vergabe, bereite alles vor` wird der Projektordner inventarisiert und der belastbare Aktenstand rekonstruiert. Vorhandene Fach-, Bestands-, Kosten-, Bauwerks-, Klima-, Genehmigungs- und Vergabedaten werden quellengetrennt aufgenommen. Kein Quellsystem wird ersetzt oder ohne Freigabe beschrieben.

## Startreihenfolge

1. Bedarfsträger, Vergabestelle, Entscheidungskompetenz und Freigabekette bestimmen.
2. Beschaffungsgegenstand, Lose, Optionen, Laufzeit und geschätzten Gesamtwert erfassen.
3. Verfahrensstand anhand der Vergabeakte und Portalprotokolle feststellen.
4. anwendbares Regime, Schwellenwert, Landesrecht und aktuelle Wertgrenzen live prüfen.
5. Vergabereife bewerten: Bedarf, Budget, Markterkundung, Leistungsbeschreibung, Eignung, Zuschlagsmodell, Termine, Verträge und Datenformate.
6. Ziel definieren: bestes Preis-Leistungs-Verhältnis, Qualität, Geschwindigkeit, Lebenszykluskosten, Resilienz und rechtssichere Dokumentation.

## Pflichtweichen

- Beschaffungsdaten werden nach Quelle, Stichtag, Qualität und Entscheidungsrelevanz gekennzeichnet.
- Preis ist nur dann alleiniges Zuschlagskriterium, wenn dies zum Gegenstand und Beschaffungsziel passt und dokumentiert ist; sonst werden überprüfbare Qualitäts- und Leistungsmerkmale nach § 127 GWB und § 58 VgV entwickelt.
- Bei Rüge oder Nachprüfung werden § 160-Fristen, § 165-Geheimnisschutz und § 169-Unterrichtung geprüft. Vor der OLG-Planung bestimmt § 187 Abs. 2 GWB anhand des Verfahrensbeginns, ob die alte oder die seit 1. Juli 2026 geltende Fassung der §§ 172 und 173 GWB anzuwenden ist.
- Legacy- und Portalformate erhalten einen Import-, Mapping-, Validierungs- und Rückexportplan.

## Routing

| Befund | primäres Modul | erstes Ergebnis |
|---|---|---|
| Bedarf und Bestandsdaten ungeordnet | `wirklichkeitsdaten-beschaffung-steuern` | Quellen-, Qualitäts- und Szenariomatrix |
| Verfahren auszuwählen | `04-verfahrensart-waehlen` | begründeter Verfahrens- und Ausnahmevermerk |
| Leistungsbeschreibung fehlt | `08-leistungsbeschreibung` | wettbewerbsoffenes LV mit Abnahmekriterien |
| Zuschlagsmodell offen | `zuschlagskriterien-paragraf-127-gwb` | messbare Preis-Qualitäts-Matrix |
| GAEB, XML, Excel, SAP oder Fachverfahren | `legacy-systeme-integration` | Schnittstellen- und Roundtrip-Plan |
| Angebote in Wertung | `17-wertung-leistung-preis` | dokumentierte Wertungs- und Aufklärungsmatrix |
| Rüge eingegangen | `vergaberueg-paragraf-160-gwb` | Abhilfeprüfung und Antwortentwurf |
| VK-Verfahren | `23-stellungnahme-vergabekammer` | Verteidigungsschriftsatz und Aktenpaket |
| OLG-Beschwerde | `24-vorlage-an-den-vergabesenat` | fristgerechte Beschwerde oder Erwiderung |

## Startbildschirm

1. Vergabe in fünf Sätzen.
2. nächster unumkehrbarer Termin und Rechtsfolge.
3. Vergabereife-Ampel je Arbeitspaket.
4. Datenquellen- und Dokumentenmatrix.
5. Qualitätsziel und vorgeschlagenes Zuschlagsmodell.
6. gewähltes Routing und sofort erstellter erster Behördenoutput.
7. Freigaben und höchstens fünf entscheidungserhebliche Rückfragen.

Keine Kanzleiperspektive, keine Bieterkonfliktprüfung und keine bloße Liste möglicher Skills. Die Triage arbeitet aus der Akte und erzeugt den ersten verwendbaren Vermerk.
