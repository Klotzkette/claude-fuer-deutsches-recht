---
name: zv-vollstreckungsbescheid-folge
description: "Steuert das Verfahren nach Erlass des Mahnbescheids: Beantragung des Vollstreckungsbescheids nach § 699 ZPO über das Online-Mahnportal, Reaktion auf Einspruch nach § 700 ZPO, Übergang ins streitige Verfahren. Erläutert die Wirkung des VB als Vollstreckungstitel mit Klausel kraft Gesetzes § 796 Abs. 1 ZPO und die Vollstreckung aus dem VB. Lädt nach Mahnbescheid oder vor VB-Antrag."
---

# Vollstreckungsbescheid und Folgeverfahren

## Aufgabe

Der Vollstreckungsbescheid (VB) ist der Titel, den die meisten Mahnverfahren in Deutschland produzieren. Der Skill begleitet den Antrag, die Reaktion auf Einspruch und die Vollstreckung aus dem VB.

## Rechtsgrundlagen

- **§ 699 ZPO** – Vollstreckungsbescheid auf Antrag nach Ablauf der Widerspruchsfrist; nicht früher als 14 Tage nach Zustellung des Mahnbescheids (§ 699 Abs. 1 S. 2 ZPO).
- **§ 700 ZPO** – Einspruch innerhalb von 2 Wochen ab Zustellung des VB; Verfahren wird auf Antrag ans Streitgericht abgegeben (§ 700 Abs. 3 ZPO).
- **§ 796 Abs. 1 ZPO** – VB ist Vollstreckungstitel mit Klausel von Gesetzes wegen; gesonderte Klauselerteilung nicht erforderlich.
- **§ 700 Abs. 1 ZPO** – VB wirkt wie ein für vorläufig vollstreckbar erklärtes Versäumnisurteil; Sicherheitsleistung nicht erforderlich.
- **§ 705 ZPO** – Rechtskraft tritt ein mit Ablauf der Einspruchsfrist (§ 700 Abs. 1 i.V.m. § 705 S. 2 ZPO).

## Workflow VB beantragen

1. **Voraussetzungen prüfen**:
   - Mahnbescheid erlassen und dem Antragsgegner zugestellt
   - Frist von 14 Tagen ab Zustellung verstrichen
   - Kein Widerspruch eingelegt (oder nur Teilwiderspruch – dann VB nur über unbestrittenen Teil)
   - VB-Antrag innerhalb von 6 Monaten nach Mahnbescheid-Zustellung gestellt § 701 ZPO – sonst Verfall des Mahnbescheids
2. **Antrag stellen** über [online-mahnantrag.de](https://www.online-mahnantrag.de): Antragsart "Vollstreckungsbescheid beantragen", Aktenzeichen des Mahnbescheids angeben, Versandverlust meldet System eigenständig.
3. **Erlass und Zustellung** des VB an Antragsgegner von Amts wegen § 699 Abs. 4 ZPO.
4. **Wiedervorlage** 3 Wochen nach VB-Erlass: Einspruch erfolgt? Wenn nicht: Rechtskraft, vollstrecken.

## Vollstreckung aus dem VB

Der VB ist sofort vollstreckbar (§ 700 Abs. 1 ZPO) **ohne** Sicherheitsleistung. Er trägt die Klausel kraft Gesetzes § 796 Abs. 1 ZPO. Es genügt:

1. **Ausfertigung des VB** mit Zustellnachweis als Vollstreckungstitel.
2. **Vollstreckung beginnen**: PfÜB, Mobiliarvollstreckung, Vermögensauskunft, je nach Zielobjekt – Skill `zv-kommandocenter` einsteigen lassen.

## Reaktion auf Einspruch nach VB

- **Einspruch innerhalb der 2-Wochen-Frist § 700 Abs. 1 ZPO**: Verfahren geht auf Antrag eines Beteiligten ans Streitgericht. Eingang dort = Klagebegründungspflicht innerhalb von 2 Wochen § 697 ZPO. Gerichtsgebühren werden fällig (3,0-Verfahrensgebühr Nr. 1210 KV GKG abzüglich der 0,5 aus dem Mahnverfahren).
- **Verspäteter Einspruch**: gilt als Einspruch und ist als unzulässig zu verwerfen, wenn nicht Wiedereinsetzung in den vorigen Stand § 233 ZPO begehrt und gewährt wird.
- **Teileinspruch**: nur der bestrittene Teil geht ins Streitverfahren; der unbestrittene Teil bleibt rechtskräftig und vollstreckbar.

## Häufige Stolpersteine

- **6-Monats-Frist** § 701 ZPO – nicht der Mahnbescheid, sondern der VB-Antrag muss innerhalb dieser Frist gestellt werden. Versäumnis = Antrag erneut.
- **Zustellungsnachweis fehlt**: VB darf nicht erlassen werden, wenn Mahnbescheid nicht zugestellt wurde; bei Auslandszustellung oft Verzögerung.
- **Einspruch nicht gegen VB, sondern gegen "Anspruch" formuliert** – wird vom Gericht als Einspruch ausgelegt § 133 BGB, wenn Wille erkennbar.
- **Mahnbescheid an falsche Anschrift zugestellt**: Heilung § 189 ZPO nur bei tatsächlichem Zugang; sonst muss erneut zugestellt werden, dann läuft Frist neu.

## Leitentscheidungen

- BGH, Urt. v. 19.04.2012 – IX ZR 233/09, NJW 2012, 2502: Wirkung des VB bei Insolvenzeröffnung – Forderungsanmeldung erforderlich, VB allein nicht ausreichend.
- BGH, Beschl. v. 20.04.2017 – VII ZB 19/16, NJW 2017, 1972: Wiedereinsetzung in Einspruchsfrist bei Verschulden des Anwalts.
- BGH, Urt. v. 06.05.2014 – XI ZR 217/12: Verjährungshemmung endet 6 Monate nach Erlass des VB, wenn Verfahren nicht weiter betrieben § 204 Abs. 2 S. 1 BGB.

## Ausgabeformat

```
VB-STATUS [Mandant] gegen [Schuldner]

Mahnbescheid:
  Zugestellt am:        [DD.MM.JJJJ]
  Frist 14 Tage ablauf: [DD.MM.JJJJ]
  Widerspruch:          [NEIN / JA Volltext: ...]

VB-Antrag:
  Beantragt am:         [DD.MM.JJJJ]
  6-Monats-Frist § 701: [eingehalten]
  VB erlassen am:       [DD.MM.JJJJ]
  VB zugestellt am:     [DD.MM.JJJJ]

Einspruchsfrist:        [Ende DD.MM.JJJJ]
Einspruch eingegangen:  [NEIN / JA – Übergang Streitverfahren]

Status:                 [Rechtskraft eingetreten am DD.MM.JJJJ – VOLLSTRECKBAR]

Nächster Skill:         [zv-kommandocenter / zv-pfueb-bank / ...]
```

## Qualitätsgates

- Niemals VB vollstrecken, ohne Zustellnachweis vorzulegen § 750 ZPO.
- Bei Insolvenz nach VB-Erlass: keine Einzelzwangsvollstreckung mehr § 89 InsO, Forderung zur Tabelle anmelden.

## Querverweise

- `zv-mahnbescheid-online` – Mahnantrag.
- `zv-titel-klausel-zustellung` – VB-Klausel kraft Gesetzes.
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`, `zv-mobiliar-gv-auftrag` – Vollstreckungsmaßnahmen.
- `forderungsmanagement-klagewerkstatt/klagevorlage-aus-eigenen-mustern` – nach Einspruch Klagebegründung.
