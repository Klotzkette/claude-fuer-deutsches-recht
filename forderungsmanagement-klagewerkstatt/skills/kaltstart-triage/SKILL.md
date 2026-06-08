---
name: kaltstart-triage
description: "Erste Triage einer neuen Forderungsangelegenheit. Erhebt Rolle Mandantenziel Forderungsgrund Beklagter Belegstand Mahnvorlauf Verjährungslage und Fristen. Ordnet die Sache einer von drei Spuren zu aussergerichtliche Mahnung gerichtliches Mahnverfahren oder Zahlungsklage. Pinpoints ZPO 253 BGB 286 BGB 195 GVG 23 GVG 71. Liefert Arbeitsplan mit konkreten naechsten Skills aus diesem Plugin und Risikoampel."
---

# Kaltstart-Triage Forderungssache

Eingangsroutine für jede neue Forderungsakte. Ziel ist die Zuordnung zu einer von drei Spuren in maximal sieben Pflichtfragen.

## Sieben Pflichtfragen

| Nr | Frage | Warum sie zaehlt |
|---|---|---|
| 1 | Wer ist Mandant Glaeubiger Schuldner Dritter | bestimmt Mandatsrichtung und Honorarbasis |
| 2 | Forderungsart Werklohn Kaufpreis Miete Honorar Darlehen Schadensersatz | bestimmt Spezialskill und Beweislast |
| 3 | Schuldner natuerliche Person Verbraucher Unternehmer GmbH Verein Behörde | bestimmt Zuständigkeit Brief und Klagemuster |
| 4 | Hauptforderung in Euro mit Faelligkeitsdatum | bestimmt sachliche Zuständigkeit GVG 23 oder GVG 71 |
| 5 | Mahnvorlauf vorhanden Datum erste Mahnung Verzugsbegruendung | bestimmt Zinsbeginn nach BGB 286 |
| 6 | Verjährungsstand Forderung aus welchem Jahr | bestimmt Eilbeduerftigkeit nach BGB 195 199 |
| 7 | Vollstreckungsfaehiger Titel vorhanden oder gewuenschtes Endprodukt | bestimmt Ausgang Mahnung Mahnbescheid Klage |

## Routing in drei Spuren

| Befund | Spur | Folgeskill |
|---|---|---|
| Forderung unstreitig faellig Schuldner bekannt zustellfaehig kein Titel | Mahnbescheid | mahnbescheid-online |
| Forderung mit Bestreiten zu rechnen oder Urkundenlage gut | Zahlungsklage | zahlungsklage-erstellen |
| Forderung wackelig Belege unklar Verjährung naht Verbraucher zoegerlich | aussergerichtliche Mahnung mit Vergleichsangebot | mahnung-aussergerichtlich-stufenmodell |

## Risikoampel Erstbewertung

| Ampel | Auslöser |
|---|---|
| gruen | Forderung dokumentiert Schuldner solvent Verjährung in weiter Ferne Zustellung gesichert |
| gelb | Belege luckenhaft Verjährung im laufenden Jahr Schuldner zahlungssaeumig |
| rot | Verjährung tritt in den naechsten sechzig Tagen ein Schuldner verzogen oder insolvent Belegstand schwach |

Rote Ampel triggert sofort Skill verjaehrung-pruefen und gegebenenfalls Mahnbescheid noch am gleichen Werktag.

## Norm-Pinpoints

- ZPO 253 Abs. 2 Klage Pflichtbestandteile
- ZPO 688 ff. Mahnverfahren
- BGB 286 Verzug
- BGB 288 Verzugszinsen
- BGB 195 199 Verjährung
- GVG 23 Nr. 1 ab 2026 Streitwertgrenze AG zehntausend Euro

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [BGB 286](https://www.gesetze-im-internet.de/bgb/__286.html)
- [BGB 195](https://www.gesetze-im-internet.de/bgb/__195.html)
- [GVG 23](https://www.gesetze-im-internet.de/gvg/__23.html)
