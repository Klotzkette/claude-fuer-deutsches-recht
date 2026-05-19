---
name: streitwert
description: >
  Berechnung und Darlegung des Streitwerts nach GKG und RVG für Zivil-, Handels-
  und Gesellschaftssachen; Kostenfestsetzungsanträge nach § 104 ZPO. Lädt, wenn
  es um Streitwert, Gegenstandswert, Gerichtskosten, Anwaltsgebühren oder die
  Kostenfestsetzung geht.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Streitwert
  - Gegenstandswert
  - GKG
  - RVG
  - Kostenfestsetzung
  - Kostenausgleichung
  - Streitwertbeschwerde
  - Mehrwert Hilfsantrag
---

# Streitwertfestsetzung – GKG / RVG

## Zweck

Dieser Skill unterstützt bei der Berechnung des Streitwerts für gerichtliche
Verfahren (§§ 39 ff. GKG), des anwaltlichen Gegenstandswerts (§ 23 RVG) sowie
bei der Erstellung von Kostenfestsetzungsanträgen (§ 104 ZPO). Er dient ferner
der Überprüfung vorläufiger Streitwertfestsetzungen des Gerichts und der
Vorbereitung von Streitwertbeschwerden (§ 68 GKG).

Typischer Mandatskontext: Klagepartei oder Beklagte möchten die voraussichtlichen
Prozesskosten einschätzen; Kostenerstattungsstreit nach obsiegendem Urteil;
Gebührennote im Außerverhältnis.

## Eingaben

Das Modell benötigt folgende Informationen:

1. **Streitgegenstand** – Leistungsklage (§ 3 ZPO), Feststellungsklage (§ 256 ZPO;
   Abschlag i. d. R. 20–25 % vom Leistungsantrag), einstweilige Verfügung
   (i. d. R. 1/3 bis 1/2 des Hauptsachewerts).
2. **Gericht und Instanz** – Landgericht (Kammer für Handelssachen), Oberlandesgericht,
   BGH; Instanz bestimmt Gerichtsgebühr (Anlage 1 GKG).
3. **Hauptantrag und Hilfsantrag** – Wert der Hilfsanträge bleibt außer Betracht,
   solange sie nicht beschieden werden (§ 45 Abs. 1 Satz 2 GKG; Mehrwert nur bei
   Entscheidung, § 45 Abs. 1 Satz 3 GKG).
4. **Nebenforderungen** – Zinsen und Früchte nach § 43 Abs. 1 GKG nicht streitwerterhöhend
   (außer wenn sie Hauptgegenstand sind).
5. **Aufrechnung** – § 45 Abs. 3 GKG: Aufrechnung erhöht den Streitwert bis zur
   Höhe des Klageanspruchs, nicht darüber hinaus.
6. **Anwaltsgebühren** – Gegenstandswert nach § 23 Abs. 1 Satz 1 RVG entspricht
   dem Streitwert; § 23 Abs. 3 RVG bei Sonderregeln (z. B. Wohnraum).

## Rechtlicher Rahmen

### Zentrale Normen

- **§§ 39–48 GKG** – Allgemeine Grundsätze der Streitwertberechnung im Zivilprozess.
- **§ 3 ZPO** – Streitwertschätzung durch das Gericht nach freiem Ermessen.
- **§ 45 GKG** – Hilfsanträge und Aufrechnung.
- **§ 43 GKG** – Zinsen, Früchte, Nutzungen nicht streitwerterhöhend.
- **§ 68 GKG** – Streitwertbeschwerde; Frist: 6 Monate nach Rechtskraft.
- **§ 23 RVG** – Gegenstandswert für anwaltliche Vergütung.
- **§ 104 ZPO** – Kostenfestsetzungsverfahren; Antrag beim Urkundsbeamten.
- **§ 103 ZPO** – Kostenfestsetzungsantrag, Kostentitel Voraussetzung.

### Leitentscheidungen

1. BGH, Beschl. v. 04.07.2018 – IV ZR 200/16, NJW-RR 2018, 1140 Rn. 5 – Zur
   Streitwertbemessung bei Feststellungsanträgen neben Leistungsanträgen: kein
   Mehrwert, wenn Feststellungsantrag wirtschaftlich in Leistungsantrag aufgeht.

2. BGH, Beschl. v. 10.04.2014 – I ZB 22/13, NJW 2014, 2280 Rn. 12 – Zur
   Streitwertbemessung im Unterlassungsrechtsstreit: bei Kerntheorie-Reichweite
   ist der wirtschaftliche Wert des Verbots maßgeblich, nicht nur der konkret
   angegriffene Verletzungsfall.

### Kommentarliteratur

1. Hartmann, in: Hartmann, KostenG, 54. Aufl. 2024, § 45 GKG Rn. 18 – Mehrwert
   von Hilfsanträgen setzt Bescheidung voraus; bis dahin kein Ansatz.

2. Mayer, in: Mayer/Kroiß, RVG, 8. Aufl. 2023, § 23 Rn. 34 – Gegenstandswert
   folgt grundsätzlich dem prozessualen Streitwert; Sonderregelungen in § 23
   Abs. 3 RVG (nichtvermögensrechtliche Gegenstände: Mindest- und Höchstwerte).

## Ablauf

1. **Hauptforderung bestimmen** – Nennwert bei Leistungsklage; bei Feststellungsklage
   Abschlag von i. d. R. 20 % (Ermessen, vgl. § 3 ZPO).

2. **Nebenforderungen ausscheiden** – Zinsen, Früchte, Kosten des Verfahrens nach
   § 43 Abs. 1 GKG nicht mitrechnen, sofern Nebenforderungen.

3. **Hilfsanträge prüfen** – Kein Ansatz im Ausgangsverfahren (§ 45 Abs. 1 Satz 2
   GKG); bei Stattgabe des Hilfsantrags Mehrwert nach § 45 Abs. 1 Satz 3 GKG
   nachträglich festsetzen.

4. **Aufrechnung einbeziehen** – Widerklageforderung oder Aufrechnungsforderung erhöht
   Streitwert nach § 45 Abs. 3 GKG nur bis zur Klageforderungshöhe.

5. **Gerichtsgebühren berechnen** – Aus dem festgesetzten Streitwert die Gerichtsgebühr
   nach GKG Anlage 1 und 2 ermitteln (Tabelle §§ 34, 35 GKG).

6. **Anwaltsgebühren berechnen** – Gegenstandswert für Verfahrensgebühr (Nr. 3100 VV
   RVG), Terminsgebühr (Nr. 3104 VV RVG), Einigungsgebühr (Nr. 1000 VV RVG)
   aus der Vergütungstabelle (Anlage 2 RVG) ableiten.

7. **Kostenfestsetzungsantrag stellen** – Nach Vorliegen eines zur Zwangsvollstreckung
   geeigneten Kostentitels (§ 103 ZPO) Antrag nach § 104 ZPO beim Urkundsbeamten;
   Glaubhaftmachung der Auslagen durch Kostenrechnung und Belege.

8. **Streitwertbeschwerde** – Binnen 6 Monaten nach Rechtskraft (§ 68 Abs. 1 Satz 3
   GKG); beschwerdeberechtigt: Parteien und Staatskasse; Gericht, das die
   angegriffene Entscheidung erlassen hat, entscheidet zuerst (§ 68 Abs. 1
   Satz 1 GKG); dann ggf. Beschwerdegericht.

## Ausgabeformat

- **Streitwert-Memo** (Gutachtenstil): Struktur Hauptantrag → Hilfsanträge →
  Nebenforderungen → Ergebniswert; mit Norm- und Rspr.-Nachweisen.
- **Kostennote** (Tabelle): Gebührenart | Gegenstandswert | Gebührensatz
  (VV-Nr.) | Betrag | USt.; Gesamt.
- **Kostenfestsetzungsantrag** (Schriftsatz): Adressat Urkundsbeamter; Bezugnahme
  auf Kostentitel; Auflistung erstattungsfähiger Kosten; Unterschrift.

## Beispiel

*Sachverhalt:* Klägerin macht 80.000 € Schadensersatz geltend (Leistungsklage).
Hilfsantrag auf Feststellung künftiger Schadensersatzpflicht. Beklagte rechnet
mit einer Gegenforderung von 30.000 € auf.

*Streitwertberechnung (Urteilsstil):*

Der Streitwert beläuft sich auf 110.000 €. Die Leistungsklage hat einen Wert
von 80.000 € (§ 3 ZPO). Der Hilfsantrag bleibt nach § 45 Abs. 1 Satz 2 GKG
außer Betracht, da das Gericht über ihn nicht zu entscheiden hat, solange der
Hauptantrag Erfolg verspricht. Die Aufrechnung mit 30.000 € erhöht den
Streitwert gemäß § 45 Abs. 3 GKG um 30.000 €, da sie 80.000 € nicht übersteigt.
Zinsen auf die Klageforderung sind nach § 43 Abs. 1 GKG nicht anzusetzen.

Gerichtsgebühr (3,0-fach, § 34 GKG, Nr. 1210 KV GKG): aus einem Streitwert
von 110.000 € = 3 × 1.476 € = 4.428 €.

Anwaltsgebühren (Verfahrensgebühr 1,3 aus 110.000 € = 1,3 × 2.471 € = 3.212,30 €
zzgl. USt.) nach Nr. 3100 VV RVG i. V. m. Anlage 2 RVG.

*(BGH, Beschl. v. 04.07.2018 – IV ZR 200/16, NJW-RR 2018, 1140 Rn. 5; Hartmann,
in: Hartmann, KostenG, 54. Aufl. 2024, § 45 GKG Rn. 18.)*

## Risiken und typische Fehler

- **Frist Streitwertbeschwerde:** § 68 Abs. 1 Satz 3 GKG – 6 Monate nach
  Rechtskraft der Hauptsacheentscheidung; Versäumnis führt zum Verlust des
  Rechtsbehelfs.
- **Hilfsantragsmehrwert:** Wird irrtümlich sofort angesetzt, obwohl das Gericht
  über ihn nicht entschieden hat – Fehler mit Kostennachforderungsrisiko.
- **Aufrechnung überschreitet Klageforderung:** § 45 Abs. 3 GKG begrenzt den
  Mehrwert auf die Klageforderungshöhe; Überschreitung wird nicht berücksichtigt.
- **Zinsen als Hauptforderung:** Sind Zinsen ausnahmsweise selbst Streitgegenstand
  (z. B. Zinsklage), sind sie streitwertrelevant – § 43 Abs. 1 GKG greift dann
  nicht.
- **Berufsrecht:** Fehlerhafte Gebührennoten können eine Pflichtverletzung
  (§ 43a BRAO) darstellen; Vergütungsvereinbarungen müssen § 3a RVG entsprechen.
- **Datenschutz:** Mandantenunterlagen dürfen nicht ohne Einwilligung in externe
  KI-Tools eingegeben werden (§ 43a Abs. 2 BRAO, § 203 StGB).
- **Keine KI-Garantie:** Gebührentabellen und Gegenstandswerte sind anhand der
  aktuellen GKG-Anlage und RVG-Anlage 2 manuell zu prüfen.

## Quellenpflicht

Jede Aussage zu Streitwert, Gebühren oder Kostenerstattung ist zu belegen nach
den Vorgaben in `references/zitierweise.md`. Gesetz vor Rechtsprechung vor
Kommentar. Bei streitiger Streitwertbemessung (z. B. Feststellungsabschlag)
h. M. und Gegenauffassung kenntlich machen. Tabellenwerte (GKG Anlage 2, RVG
Anlage 2) stets auf Aktualität prüfen – Gesetzesänderungen fließen nicht
automatisch ein.
