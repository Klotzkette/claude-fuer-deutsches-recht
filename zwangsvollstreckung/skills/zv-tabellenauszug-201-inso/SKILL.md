---
name: zv-tabellenauszug-201-inso
description: "Vollstreckung aus dem Tabellenauszug nach § 201 Abs. 2 InsO nach Aufhebung oder Beendigung des Insolvenzverfahrens. Klärt Voraussetzungen (festgestellt, nicht vom Schuldner bestritten, kein Restschuldbefreiungs-Versagungsgrund), Klausel- und Zustellungsformalia, 30-Jahres-Verjährung § 197 BGB und Schranken bei Restschuldbefreiung § 301 InsO. Lädt, sobald ein Tabellenauszug als Titel vorliegt."
---

# Vollstreckung aus Tabellenauszug § 201 InsO

## Aufgabe

Der vollstreckbare Tabellenauszug ist ein eigener Titel (§ 201 Abs. 2 Satz 1 InsO). Dieser Skill prüft, ob aus ihm vollstreckt werden darf, und steuert die nächste Pfändung.

## Startet bei

- Insolvenzverfahren ist aufgehoben (§ 200 InsO) oder eingestellt (§§ 207, 211 InsO)
- Forderung wurde zur Tabelle festgestellt und vom Schuldner nicht (wirksam) bestritten
- Restschuldbefreiung nicht erteilt oder Forderung von ihr ausgenommen (§ 302 InsO)

## Rechtsgrundlagen

- § 201 InsO – Rechte der Insolvenzgläubiger nach Verfahrensaufhebung
- § 178 Abs. 3 InsO – Wirkung der Feststellung
- § 197 Abs. 1 Nr. 5 BGB – 30 Jahre Verjährung
- § 301 InsO – Wirkung der Restschuldbefreiung
- § 302 InsO – Ausnahmen (Deliktsforderung, Unterhalt, hinterzogene Steuern)
- §§ 727, 750 ZPO – Klausel und Zustellung
- § 794 Abs. 1 Nr. 1 ZPO i.V.m. § 201 InsO – Titelqualität

## Workflow

1. **Tabellenauszug prüfen**: Ist die Forderung mit dem Vermerk „festgestellt" eingetragen, nicht „bestritten"? Bestreitet der Insolvenzverwalter, aber nicht der Schuldner – Titel gegen Schuldner trotzdem entstanden.
2. **Verfahrensstand**: Verfahren aufgehoben/eingestellt? Vollstreckung erst danach zulässig (§ 89 InsO greift bis dahin).
3. **Restschuldbefreiung**:
   - **Nicht erteilt** (versagt oder Verfahren nach IK-Plan): freie Vollstreckung.
   - **Erteilt**: § 301 InsO – Vollstreckung grundsätzlich gesperrt; **Ausnahmen § 302 InsO** (vorsätzliche unerlaubte Handlung mit Eintrag in der Tabelle, Unterhaltsrückstände aus pflichtwidriger Verletzung, hinterzogene Steuern).
   - **Wohlverhaltensphase**: Vollstreckung gegen den pfändbaren Teil des Schuldnereinkommens nur eingeschränkt zulässig.
4. **Klausel** beim Insolvenzgericht (§ 201 Abs. 2 Satz 2 InsO, § 727 ZPO) bzw. wenn Insolvenzgericht das Verfahren geführt hat – aus der vollstreckbaren Ausfertigung.
5. **Zustellung** an Schuldner § 750 ZPO.
6. **Pfändung** durchziehen über `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt` oder `zv-mobiliar-gv-auftrag`.
7. **Verjährung** beachten: 30 Jahre ab Eintragung (§ 197 Abs. 1 Nr. 5 BGB) – Zinsen separat (§ 197 Abs. 2 BGB drei Jahre regelmäßig, aber bei rechtskräftig festgestellten Zinsen 30 Jahre für ab Feststellung entstandene, drei Jahre für nach Feststellung entstehende künftige Zinsen).

## Schranken der Restschuldbefreiung

§ 302 InsO listet die nicht erfassten Forderungen:

1. Deliktische Forderungen aus vorsätzlich unerlaubter Handlung – **Eintragung mit Vermerk „aus vorsätzlich begangener unerlaubter Handlung"** ist Voraussetzung.
2. Geldstrafen, Geldbußen, Ordnungs- und Zwangsgelder.
3. Hinterzogene Steuern, sofern Verurteilung.
4. Pflichtwidrige Unterhaltsforderungen.
5. Zinslose Darlehen für die Verfahrenskosten.

Nur diese Forderungen lassen sich nach Restschuldbefreiung weiterhin vollstrecken – Skill prüft das ausdrücklich.

## Leitentscheidungen

- BGH 18.5.2006 – IX ZR 187/04 (Wirkung der Feststellung)
- BGH 13.10.2009 – XI ZR 18/09 (Verjährung § 197 Abs. 1 Nr. 5 BGB)
- BGH 17.1.2008 – IX ZR 220/06 (§ 302 InsO Eintragungserfordernis)
- BGH 18.12.2008 – IX ZR 124/08 (Forderung aus Tabelle nach Restschuldbefreiung)
- BGH 28.9.2017 – IX ZR 144/16 (Zinsen aus Tabellenauszug)

## Ausgabeformat

```
TABELLENAUSZUG § 201 InsO [Mandant] gegen [Schuldner]

InsO-Verfahren:        AG [Ort] Az [IN/IK ...]
Aufhebung/Einstellung: am DD.MM.JJJJ
Forderung Tabelle:     lfd Nr x, EUR y, "festgestellt"
Bestritten von:        [niemand / Insolvenzverwalter / Schuldner]
Restschuldbefreiung:   [nicht erteilt / erteilt / versagt / verfahrensgegenstand]
§ 302-Privileg:        [nein / Deliktsforderung mit Eintrag / Unterhalt / ...]
Verjährung:            30 Jahre ab Feststellung, ab DD.MM.JJJJ
Klausel:               [vorhanden / beim AG Insolvenzgericht beantragen]
Zustellung § 750:      [erfolgt am DD.MM.JJJJ / offen]

NÄCHSTER SKILL:        [zv-pfueb-bank / zv-pfueb-arbeitsentgelt / ...]
```

## Qualitätsgates

- Niemals vor Aufhebung/Einstellung des Verfahrens vollstrecken.
- Niemals nach Restschuldbefreiung vollstrecken, wenn § 302 InsO nicht greift – Schadensersatzrisiko.
- Niemals deliktische Privilegierung ohne Eintragungsvermerk in der Tabelle annehmen.
- Verjährung 30 Jahre: jüngere Forderungen aus laufender Tabelle möglich.
- Klausel und Zustellung wie bei jedem Titel.

## Querverweise

- `insolvenzforderungsanmeldungspruefung/ifap-tabellenauszug-178` – wenn der Auszug erst beschafft wird (anderes Plugin, eng verzahnt)
- `zv-titel-klausel-zustellung`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-abwehr-schuldner` – Vollstreckungsgegenklage nach Restschuldbefreiung
