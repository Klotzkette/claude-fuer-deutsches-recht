---
name: zv-notarielle-urkunde-grundschuld
description: "Glaeubiger hat notarielle Grundschuld-Urkunde und will vollstrecken. § 794 Abs. 1 Nr. 5 ZPO Zwangsvollstreckung aus notarieller Urkunde. Pruefraster: Unterwerfungsklausel dinglich und persoenlich Klauselumschreibung § 727 ZPO bei Abtretung Sicherungsabrede Kuendigung § 1193 BGB 6-Monats-Frist Vollstreckung Grundstueck ZVG vs. persoenliches Vermoegen PfUeB. Output: Vollstreckungsstrategie und Schriftsatz-Entwurf. Abgrenzung zu zv-zvg-antrag-glaeubiger (Versteigerung) und zv-titel-klausel-zustellung."
---

# Vollstreckung aus notarieller Grundschuldurkunde

## Aufgabe

Banken und Investoren stützen die Vollstreckung in Immobilien fast immer auf eine notarielle Urkunde mit Grundschuld und Unterwerfungsklausel. Dieser Skill koordiniert beide Vollstreckungsrichtungen: dinglich in das Grundstück, persönlich in das sonstige Vermögen.

## Startet bei

- Notarielle Urkunde mit Grundschuld vorhanden
- Unterwerfung des Eigentümers/Schuldners „in sein gesamtes Vermögen" und/oder „in den jeweiligen Grundbesitz"
- Sicherungsabrede (Zweckerklärung) liegt vor
- Forderung fällig (gekündigt, Zahlungsverzug)

## Rechtsgrundlagen

- § 794 Abs. 1 Nr. 5 ZPO – notarielle Urkunde als Titel
- § 800 ZPO – Vollstreckung gegen Rechtsnachfolger im Eigentum
- § 727 ZPO – Titelumschreibung bei Forderungsabtretung
- § 1192 Abs. 1a BGB – Einreden bei Sicherungsgrundschuld
- § 1193 BGB – Kündigung Grundschuld, sechs Monate
- § 1147 BGB – Befriedigung aus dem Grundstück
- § 750 Abs. 1 ZPO – Zustellung
- §§ 15 ff. ZVG – Anordnung der Zwangsversteigerung / Zwangsverwaltung

## Workflow

1. **Drei-Säulen-Prüfung speziell**:
   - **Titel**: notarielle Urkunde mit Unterwerfung – wurde sie als „Vollstreckungstitel" ausgestellt (in der Regel formularmäßig „der Eigentümer unterwirft sich ...").
   - **Klausel** § 795 i.V.m. § 724 ZPO durch den Notar oder beim Amtsgericht. Bei Forderungsabtretung Klauselumschreibung § 727 ZPO – zwingend (BGH 30.3.2010 – XI ZR 200/09).
   - **Zustellung** der vollstreckbaren Ausfertigung an den Schuldner; bei dinglicher Vollstreckung an den Eigentümer (auch Dritter) nach § 800 Abs. 2 ZPO.
2. **Kündigung Grundschuld § 1193 BGB**: sechs Monate Kündigungsfrist, abdingbar nur eingeschränkt – AGB-Kontrolle (BGH 8.12.2009 – XI ZR 181/08). Kündigungsschreiben zustellen.
3. **Sicherungsabrede prüfen**: Welche Forderungen sichert die Grundschuld? Aktuelle Höhe? Zinsen? Übersicherung? Einrede § 1192 Abs. 1a BGB bei Abtretung.
4. **Dingliche Vollstreckung**: ZVG-Antrag → `zv-zvg-antrag-glaeubiger`.
5. **Persönliche Vollstreckung**: zusätzlich PfÜB Bank/Lohn → `zv-pfueb-bank` / `zv-pfueb-arbeitsentgelt`.
6. **Insolvenz**: Bei Schuldner-Insolvenz wird der Grundschuldgläubiger Absonderungsberechtigter (§ 49 InsO) – Vollstreckung außerhalb der Insolvenztabelle weiterhin möglich, aber Verwertung über Insolvenzverwalter ggf. günstiger.

## Klauselumschreibung § 727 ZPO bei Forderungsabtretung

Wird die gesicherte Forderung an einen neuen Gläubiger abgetreten (typisch bei Forderungskäufen, Loan-Sale), muss der neue Gläubiger:

- die Abtretung im notariell beglaubigtem Wege nachweisen
- den Klauselantrag beim ausstellenden Notar (oder hilfsweise § 797 ZPO) stellen
- die Klauselzustellung an den Schuldner durchführen, bevor er aus der Urkunde vollstrecken darf.

BGH 30.3.2010 – XI ZR 200/09: Ohne wirksame Klauselumschreibung keine Vollstreckung.

## Sicherungsgrundschuld – Einreden § 1192 Abs. 1a BGB

Schuldner kann gegenüber neuem Erwerber alle Einreden geltend machen, die ihm gegen den ursprünglichen Sicherungsgeber zustanden – auch wenn der neue Erwerber gutgläubig war (Einschränkung des § 1157 Satz 2 BGB).

## Leitentscheidungen

- BGH 30.3.2010 – XI ZR 200/09 (Klauselumschreibung Zessionar)
- BGH 8.12.2009 – XI ZR 181/08 (Kündigung § 1193 BGB AGB-Kontrolle)
- BGH 26.11.2009 – VII ZR 11/09 (Reichweite Unterwerfung in das gesamte Vermögen)
- BGH 5.12.2013 – VII ZR 56/13 (Bestimmtheit der Sicherungszweckerklärung)
- BGH 9.7.2020 – V ZR 60/19 (Auslegung der Sicherungsabrede)

## Ausgabeformat

```
NOTAR. URKUNDE / GRUNDSCHULD [Mandant] gegen [Schuldner], Az [Notar]

Urkunde:               Notar [Name], URNr [Nr/Jahr]
Grundschuld:           EUR x, Zinsen x %, GB [Ort, Bl, lfd Nr]
Unterwerfung:          [dinglich / persönlich / beides]
Sicherungsabrede:      [Datum, Gegenstand]
Kündigung § 1193:      [erforderlich? ja, am DD.MM.JJJJ erklärt]
Klausel § 727:         [nicht erforderlich / umschrieben am DD.MM.JJJJ]
Zustellung § 750:      [erfolgt an DD.MM.JJJJ]
Vollstreckungswege:    [ZVG / PfÜB Bank / PfÜB Lohn]

NÄCHSTE SKILLS:        zv-zvg-antrag-glaeubiger, zv-pfueb-bank
WIEDERVORLAGE:         DD.MM.JJJJ + 6 Monate (Kündigungsfrist)
```

## Qualitätsgates

- Niemals dingliche Vollstreckung ohne wirksame Kündigung § 1193 BGB (Sechs-Monats-Frist).
- Niemals aus Urkunde ohne Klauselumschreibung § 727 ZPO vollstrecken, wenn Forderung abgetreten.
- Niemals persönliche Vollstreckung ohne Unterwerfung in das Vermögen prüfen.
- Bei Verbraucher-Sicherungsgrundschuld AGB-Kontrolle der Unterwerfungsklausel.

## Querverweise

- `zv-titel-klausel-zustellung`
- `zv-zvg-antrag-glaeubiger`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-abwehr-schuldner`
- `insolvenzforderungsanmeldungspruefung/ifap-tabellenauszug-178` – falls Schuldner Insolvenz
