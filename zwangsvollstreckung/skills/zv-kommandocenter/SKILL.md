---
name: zv-kommandocenter
description: "Startpunkt der Zwangsvollstreckung. Fragt nach Titelart und Vollstreckungsziel und entscheidet, welcher Folge-Skill geladen wird: Mahnbescheid, PfÜB, notarielle Urkunde, Tabellenauszug, ZVG, Mobiliar, Räumung, Vermögensauskunft, Kontensuche oder Schuldnerabwehr. Prüft die drei Säulen Titel, Klausel, Zustellung vor jedem weiteren Schritt. Lädt, wenn ein Mandat die Einleitung oder Steuerung einer Vollstreckung betrifft."
---

# Zwangsvollstreckung – Kommandocenter

## Aufgabe

Das Kommandocenter steuert den gesamten Vollstreckungspfad: vom Erstgespräch bis zur Beendigung. Es erkennt, welcher Titel vorliegt, was vollstreckt werden soll, welche Vermögenswerte bekannt sind und welcher Folge-Skill als Nächstes geladen werden muss. Es ist der einzige Skill, der ohne Vorwissen gestartet werden kann.

## Eingaben

1. **Titelart**: Urteil (rechtskräftig oder vorläufig vollstreckbar), Vollstreckungsbescheid, gerichtlicher oder notarieller Vergleich, notarielle Urkunde mit Unterwerfung (§ 794 Abs. 1 Nr. 5 ZPO), vollstreckbare Ausfertigung des Tabellenauszugs (§ 201 InsO), Kostenfestsetzungsbeschluss.
2. **Vollstreckungsziel**: Geld, Räumung, Herausgabe, Handlung, Unterlassung.
3. **Schuldnersituation**: Privatperson, Selbstständige, Unternehmen, Insolvenz, Verbraucherinsolvenz, P-Konto bekannt.
4. **Bekannte Vermögenswerte**: Bankkonten, Arbeitgeber, Grundbesitz, Kfz, Forderungen gegen Dritte.
5. **Bisherige Vollstreckungsversuche**: erfolglos, Vermögensauskunft schon abgegeben, Sperrfrist § 802d ZPO.

## Drei-Säulen-Prüfung vor jedem Vollstreckungsschritt

Niemand darf vollstrecken, ohne **alle drei** Säulen geprüft zu haben:

1. **Titel** § 704 ZPO – formgerechte Ausfertigung vorhanden.
2. **Klausel** § 724 ZPO – vollstreckbare Ausfertigung mit Klauselvermerk (Ausnahme: Vollstreckungsbescheid, der die Klausel von Gesetzes wegen trägt § 796 Abs. 1 ZPO; Tabellenauszug § 201 Abs. 2 InsO).
3. **Zustellung** § 750 ZPO – Titel mit Klausel ist dem Schuldner vor der Vollstreckung zugestellt worden (Wartefrist 2 Wochen für Klauselzustellung bei Klauseln nach §§ 726 ff. ZPO).

Wenn auch nur eine Säule fehlt: **STOPP**. Der Skill bricht die Vollstreckung ab und ruft `zv-titel-klausel-zustellung`.

## Routing-Tabelle

| Wenn vorhanden / gewünscht | Lade Skill |
| --- | --- |
| Forderung noch ohne Titel | `forderungsmanagement-klagewerkstatt/inkasso-zahlungsklage-ersteller` (anderes Plugin) |
| Antrag auf Mahnbescheid | `zv-mahnbescheid-online` |
| Mahnbescheid liegt vor, kein Widerspruch | `zv-vollstreckungsbescheid-folge` |
| Vollstreckungsbescheid in Hand, Konto bekannt | `zv-pfueb-bank` |
| Lohnforderung gepfändet werden soll | `zv-pfueb-arbeitsentgelt` |
| Forderung gegen Mieter, Finanzamt, Krankenkasse | `zv-pfueb-mieter-finanzamt` |
| Kein Vermögen bekannt | `zv-vermoegensauskunft-gv` oder `zv-kontensuche-drittschuldner` |
| Notarielle Urkunde mit Grundschuld vorhanden | `zv-notarielle-urkunde-grundschuld` |
| Vollstreckung in Immobilie | `zv-zvg-antrag-glaeubiger` |
| Tabellenauszug aus aufgehobenem oder beendetem Insolvenzverfahren | `zv-tabellenauszug-201-inso` |
| Mobile Pfändung vor Ort | `zv-mobiliar-gv-auftrag` |
| Räumung von Wohn- oder Geschäftsraum | `zv-raeumung-885` |
| Schuldnerseite: Vollstreckung wehren | `zv-abwehr-schuldner` |
| Pfändungsfreigrenze berechnen | `zv-pfaendungstabelle-2025` |

## Reform-Stand 2026/2027 (ZVollstrDigitG)

Das Gesetz zur weiteren Digitalisierung der Zwangsvollstreckung (BT-Drs. 21/4815) bringt für die Praxis drei zentrale Änderungen, die der Skill bei jeder Beratung mitberücksichtigt:

1. **Inkrafttreten Hauptteile**: 1.10.2026 – neue Pfändungsformulare, XML-Antrag nach § 829 Abs. 5 ZPO n.F. möglich (PDF + XML; XML ist führend).
2. **Pflicht für Kreditinstitute**: ab 1.10.2027 müssen Banken einen sicheren elektronischen Übermittlungsweg eröffnen (§ 173 Abs. 2 Nr. 1 ZPO n.F.) – eBO oder andere Wege nach § 130a Abs. 4 ZPO. Vorher freiwillig.
3. **§ 840 ZPO Drittschuldnererklärung**: Postzustellung zusätzlich zur GV-Zustellung und elektronischen Zustellung.

Stand 25.5.2026: Gesetz im Bundestag beschlossen am 19.3.2026, Bundesrat nicht zustimmungspflichtig, Verkündung im BGBl stand bei letzter Recherche noch aus – `zv-elektronische-zustellung-2027` enthält die operative Umsetzung und prüft, ob das Datum zwischenzeitlich angepasst werden muss.

## Ausgabeformat

```
ZV-KOMMANDOCENTER [Mandant] [Az]

Titel:          [Art, Datum, Aussteller]
Klausel:        [vorhanden / fehlt / wo beantragen]
Zustellung:     [erfolgt am DD.MM.JJJJ / offen]
Drei Säulen:    [GRÜN / GELB / ROT]

Vollstreckungsziel:     [Geld EUR x / Räumung / Herausgabe / ...]
Schuldner:              [Privat / Unternehmen / Insolvenz / sonst]
Bekannte Werte:         [Bank / AG / Immobilie / Kfz / nichts]

NÄCHSTER SKILL:         [zv-...]
Begründung:             [warum dieser Pfad]
Wiedervorlage:          [in N Tagen wegen ...]
```

## Qualitätsgates

- Niemals Folge-Skill laden, wenn eine der drei Säulen rot ist.
- Niemals Mobiliar- oder Forderungspfändung empfehlen, wenn Schuldner in Insolvenz – dann § 89 InsO Vollstreckungsverbot greift.
- Niemals Sperrfrist § 802d ZPO (zwei Jahre Vermögensauskunft) ignorieren.
- Bei Verbraucher: stets Pfändungsfreigrenze nach Tabelle 1.7.2025 mitdenken.

## Arbeitsstil

Disziplinarisch, klar, ohne juristisches Wortgeklingel. Wenn Säulen wackeln, ist das die einzige Botschaft. Wenn der Schuldner offensichtlich vermögenslos ist, sagt der Skill das frühzeitig und schickt nicht in eine teure Mobiliarvollstreckung.
