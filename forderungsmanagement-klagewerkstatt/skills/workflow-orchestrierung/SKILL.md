---
name: workflow-orchestrierung
description: "Steuert den Gesamtablauf einer Forderungsakte vom Eingang bis zur Vollstreckung oder Abschreibung. Definiert Workflow-Stufen Eingang Pruefung Mahnung Mahnbescheid Klage Titel Vollstreckung Erloesverwertung. Pinpoints ZPO 91 Kostenfolge ZPO 167 Rueckwirkung Zustellung ZPO 696 Abgabe nach Widerspruch. Liefert Checkliste je Stufe und Wiedervorlage-Trigger."
---

# Workflow-Orchestrierung

Eine Forderungsakte durchlaeuft typischerweise sechs Stufen. Dieser Skill haelt die Stufen aus und definiert Eingangs- und Ausgangskriterien.

## Stufen-Modell

| Stufe | Eingangskriterium | Hauptarbeit | Ausgangsdokument | Wiedervorlage |
|---|---|---|---|---|
| 1 Eingang | neue Akte | kaltstart-triage forderungsaufnahme | Aktenanlage Vollmacht | 7 Tage |
| 2 Pruefung | Akte angelegt | verjaehrung-pruefen klagefreigabe-belegte-forderung | Memo Klagefreigabe | 3 Tage |
| 3 Mahnung | gruenes Licht und Verzug fehlt | mahnung-aussergerichtlich-stufenmodell | Mahnschreiben | 14 Tage Zahlungsfrist |
| 4 Mahnbescheid oder Klage | Verzug eingetreten oder Mahnung erfolglos | mahnbescheid-online oder zahlungsklage-erstellen | MB-Antrag oder Klageschrift | 4 bis 8 Wochen |
| 5 Titel | Vollstreckungsbescheid oder Urteil rechtskraeftig | vollstreckungsbescheid-folgen | titel mit Vollstreckungsklausel | sofort |
| 6 Vollstreckung | Titel vorhanden | zwangsvollstreckung-ueberblick | Pfaendungsergebnis | je Schritt 14 Tage |

## Kostenfolge

- ZPO 91 Unterliegender traegt Kosten
- ZPO 93 sofortiges Anerkenntnis Klaeger traegt Kosten
- ZPO 269 Klageruecknahme Klaeger traegt Kosten

## Wiedervorlage-Trigger

| Trigger | Aktion |
|---|---|
| Zahlungsfrist abgelaufen ohne Eingang | naechste Stufe |
| Schuldner-Brief eingegangen | sofort Auswertung mandantenkommunikation |
| Gericht setzt Termin | Tatbestand-beweis-belege aktualisieren |
| Vollstreckung erfolglos | Vermoegensauskunft ZPO 802c veranlassen |
| Insolvenzantrag bekannt | Wechsel in forderung-gegen-insolventen-schuldner |

## Zustellung Rueckwirkung ZPO 167

Wird die Klage demnaechst zugestellt wirkt die Hemmung der Verjährung auf den Tag der Anhaengigkeit zurueck. In Eilfaellen Klage bei Gericht einreichen und Gerichtskostenvorschuss sofort einzahlen.

## Norm-Pinpoints

- ZPO 91 93 269 Kostenfolge
- ZPO 167 Zustellung rueckwirkend
- ZPO 696 MB-Abgabe an Streitgericht
- BGB 204 Hemmung durch Klageerhebung

## Quellen

- [ZPO 167](https://www.gesetze-im-internet.de/zpo/__167.html)
- [ZPO 696](https://www.gesetze-im-internet.de/zpo/__696.html)
- [BGB 204](https://www.gesetze-im-internet.de/bgb/__204.html)
