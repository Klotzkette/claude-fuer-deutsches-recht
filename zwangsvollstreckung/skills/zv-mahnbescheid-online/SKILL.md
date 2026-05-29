---
name: zv-mahnbescheid-online
description: "Gläubiger will Forderung ohne Klage per Mahnbescheid titulieren lassen. §§ 688 ff. ZPO Online-Mahnverfahren. Prüfraster: Schlüssigkeitsprüfung Antragstyp Gerichtsstand Hauptforderung Nebenforderungen Zinsen Kostenansatz beA EGVP Verjährungshemmung § 204 Abs. 1 Nr. 3 BGB. Output: Mahnbescheid-Antrag komplett ausgefuellt für Online-Portal. Abgrenzung zu zv-vollstreckungsbescheid-folge (Folgeschritt nach MB) und zv-kommandocenter."
---

# Mahnbescheid online


## Triage zu Beginn

1. Ist die Forderung eine Geldforderung aus Vertrag und nicht von Gegenleistung abhängig (§ 688 ZPO)?
2. Droht Verjährung — wenn ja, bis wann muss der Mahnbescheid eingereicht sein (§ 204 Abs. 1 Nr. 3 BGB)?
3. Hat der Schuldner einen Wohnsitz in Deutschland — Auslandszustellung schwierig?
4. Ist der Antragsgegner Verbraucher oder Kaufmann — B2C erfordert strengere Prüfung?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 688 ZPO — Statthaftigkeit des Mahnverfahrens
- § 689 ZPO — Zuständigkeit (zentrales Mahngericht im jeweiligen Bundesland)
- § 690 ZPO — Antragsinhalt (Individualisierung der Forderung)
- § 692 ZPO — Erlass des Mahnbescheids; Zustellung von Amts wegen
- § 694 ZPO — Widerspruchsfrist (2 Wochen ab Zustellung)
- § 204 Abs. 1 Nr. 3 BGB — Verjährungshemmung durch Zustellung des Mahnbescheids
- § 167 ZPO — Rückwirkung der Zustellung bei "demnächst"-Zustellung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill führt durch das automatisierte Mahnverfahren, das in Deutschland ausschließlich über das gemeinsame Mahnportal der Länder läuft: [www.online-mahnantrag.de](https://www.online-mahnantrag.de). Anwälte sind seit 1.1.2018 zur elektronischen Einreichung verpflichtet (§ 702 Abs. 2 ZPO i.V.m. § 130d ZPO).

## Rechtsgrundlagen

- **§ 688 ZPO** – Statthaftigkeit: Geldforderungen aus Vertrag, gerichtlich oder schiedsgerichtlich nicht bereits erhoben, Forderung nicht von Gegenleistung abhängig (Ausnahme: Gegenleistung erbracht).
- **§ 689 ZPO** – Zuständigkeit: AG, in dessen Bezirk Antragsteller bei Antragstellung allgemeinen Gerichtsstand hat. In den meisten Ländern zentrales Mahngericht (z. B. Stuttgart, Coburg, Berlin-Wedding, Aschersleben).
- **§ 690 ZPO** – Antragsinhalt: Parteien, Anspruchsbezeichnung, Hauptforderung, Nebenforderungen, Erklärung über Gegenleistung; verbindlich elektronisch durch Anwälte.
- **§ 691 ZPO** – Zurückweisung bei Unschlüssigkeit oder Unzulässigkeit.
- **§ 692 ZPO** – Erlass des Mahnbescheids, Zustellung von Amts wegen.
- **§ 694 ZPO** – Widerspruchsfrist: 2 Wochen ab Zustellung, formfrei.
- **§ 696 ZPO** – nach Widerspruch wird Verfahren auf Antrag an Streitgericht abgegeben.
- **§ 700 ZPO** – Vollstreckungsbescheid, wenn binnen Widerspruchsfrist kein Widerspruch.
- **§ 204 Abs. 1 Nr. 3 BGB** – Verjährungshemmung durch Zustellung des Mahnbescheids; rückwirkend auf Einreichung, wenn "demnächst" zugestellt § 167 ZPO.

## Schlüssigkeitsprüfung vor Antrag

Anwalt darf nur Mahnbescheid beantragen, wenn die Forderung **schlüssig** ist. Das Mahngericht prüft nicht materiell – aber Anwalt haftet bei Schludereien.

1. **Anspruchsgrundlage** benennbar (Vertrag, gesetzliche Schuld).
2. **Höhe** bezifferbar und nicht von Gegenleistung abhängig (oder Gegenleistung erbracht und im Antrag erklärt).
3. **Fälligkeit** eingetreten.
4. **Verjährung** nicht offensichtlich, sonst kann Schuldner widersprechen und Verjährungseinrede erheben.
5. **Verbraucher**-Geschäft erkennen: § 688 Abs. 2 Nr. 1 ZPO: Bagatellgrenze entfallen seit 1.7.2014; aber Bestimmungen zum Verbraucherdarlehen § 688 Abs. 2 Nr. 1 ZPO – Mahnverfahren ausgeschlossen wenn effektiver Jahreszins über Eckzins.

## Workflow auf www.online-mahnantrag.de

### Schritt 1: Antragsart wählen

- "Mahnbescheid einreichen" – Standard.
- "Mahnbescheid weiterleiten" – wenn Antrag bereits gedruckt vorliegt.
- "Vollstreckungsbescheid beantragen" – wenn Mahnbescheid bereits zugestellt und Widerspruchsfrist verstrichen (→ Skill `zv-vollstreckungsbescheid-folge`).

### Schritt 2: Antragsteller / Verfahrensbevollmächtigter

- Bei Anwaltsantrag: Kanzlei mit SAFE-ID des beA. Mandant ist Antragsteller.
- Bei Inkassodienstleister: Registrierungsnummer nach § 10 Abs. 1 Nr. 1 RDG.

### Schritt 3: Antragsgegner

- Vollständige Anschrift mit Straße, Hausnummer, PLZ, Ort. Postfach reicht nicht (Zustellung muss möglich sein).
- Bei juristischer Person: HRB-Nummer und gesetzlicher Vertreter angeben.
- Bei minderjährigem Schuldner: gesetzliche Vertreter angeben, sonst Zurückweisung.

### Schritt 4: Hauptforderung

- Katalog-Anspruchsgrundlage wählen (z. B. "Werklohn aus Bauvertrag", "Kaufpreis aus Kaufvertrag", "Mietzins").
- Anspruchsbezeichnung muss individualisierbar sein – Rechnungsnummer und Datum, Vertragsdatum, sonst Zurückweisung § 690 Abs. 1 Nr. 3 ZPO.
- Hauptforderung in Cent eintragen.

### Schritt 5: Nebenforderungen und Zinsen

- Zinsen: gesetzlich (§ 288 BGB: 5 Prozentpunkte über Basiszins bei Verbraucher, 9 Prozentpunkte über Basiszins bei B2B) oder vertraglich.
- Zinsbeginn ist genau anzugeben (i. d. R. ab Verzug, Mahnung oder Fälligkeit nach § 286 BGB).
- Kosten der Rechtsverfolgung: Mahnkosten, Inkassokosten (nach RVG-Tabelle 1,3-fach Geschäftsgebühr Nr. 2300 VV RVG).
- Verfahrenskosten: Gerichtskosten Nr. 1100 KV GKG (0,5 Gebühr, mindestens 36 EUR) – werden automatisch berechnet.

### Schritt 6: Gegenleistung

- "Gegenleistung ist erbracht" – Standardfall.
- "Anspruch ist von Gegenleistung nicht abhängig" – z. B. bei Schadensersatz.
- "Mahnbescheid ist trotz Abhängigkeit zulässig nach § 688 Abs. 2 Nr. 1 ZPO" – Sonderfall.

### Schritt 7: Übermittlung

Anwalt: nur über beA mit angehängtem strukturiertem Datensatz (EDA = elektronischer Datensatzaustausch). Das Portal generiert die EDA-XML-Datei zum Download. Diese wird im beA als Anhang versendet.

Privatperson oder Vereine ohne beA: über das Online-Portal anlegen, dann ausdrucken und per Post einreichen ("Barcode-Variante") oder per De-Mail / EGVP einreichen.

### Schritt 8: Quittung speichern

- EDA-XML, Aktenzeichen-Barcode, beA-Versandnachweis archivieren.
- Wiedervorlage 2 Wochen nach voraussichtlicher Zustellung an Antragsgegner.

## Anhängigkeit und Verjährungshemmung

- **Anhängigkeit** mit Eingang bei Gericht § 696 Abs. 3 ZPO.
- **Verjährungshemmung** § 204 Abs. 1 Nr. 3 BGB greift mit **Zustellung** des Mahnbescheids; rückwirkend auf Eingang bei "demnächst"-Zustellung nach § 167 ZPO (i. d. R. innerhalb von 1 Monat).
- Wichtig zum Jahresende: bei Verjährungsbedrohung bis spätestens **24.12.** einreichen, damit Zustellung "demnächst" wahrscheinlich vor Jahreswechsel erfolgt.

## Was tun bei Widerspruch des Schuldners

- **Vollständiger Widerspruch**: Verfahren ruht; auf Antrag des Antragstellers Abgabe an Streitgericht § 696 ZPO (Termin- und Klagebegründungsgebühren werden fällig).
- **Teilwiderspruch**: nur über bestrittenen Teil wird ans Streitgericht abgegeben; Restteil → Vollstreckungsbescheid möglich.
- **Verspäteter Widerspruch** nach VB-Antrag: behandelt als Einspruch gegen den VB § 700 Abs. 3 ZPO.

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
MAHNANTRAG-VORBEREITUNG [Mandant] gegen [Schuldner]

Schlüssigkeit:        [JA – Anspruchsgrundlage XYZ / NEIN – Klage statt Mahnverfahren]
Anhängigkeit-Termin:  [Verjährung droht zum DD.MM.JJJJ – Einreichung bis ...]

Antragsdaten:
- Antragsteller:      [Name, Anschrift, ggf. ges. Vertreter]
- Antragsgegner:      [Name, Anschrift, ggf. ges. Vertreter, HRB-Nr.]
- Hauptforderung:     [EUR ...,..]
- Anspruchsbezeichn.: [Katalog-Nr. ...; Individualisierung: Rechnungsnr. ... v. DD.MM.JJJJ]
- Zinsen:             [X % seit DD.MM.JJJJ – Anspruchsgrundlage § 288 BGB / Vertrag]
- Nebenforderungen:   [Mahnkosten EUR ..; Inkassokosten EUR .. (Anwaltskosten Verzug)]
- Gegenleistung:      [erbracht / nicht abhängig]
- Verfahrensgebühr:   [EUR .. nach Nr. 1100 KV GKG]

Übermittlung:         [beA mit EDA-XML / EGVP / Druck]
Wiedervorlage:        [DD.MM.JJJJ (2 Wo nach voraussichtl. Zustellung)]
```

## Qualitätsgates

- Verbraucherdarlehen mit überhöhtem Zinssatz – Mahnverfahren unzulässig.
- Anspruchsbezeichnung muss eindeutig sein – sonst keine Verjährungshemmung.
- Bei Auslands-Schuldner ist Mahnverfahren oft nicht zulässig oder Europäisches Mahnverfahren (EuMahnVO) statt deutsches Mahnverfahren.

## Querverweise

- `zv-vollstreckungsbescheid-folge` – nach Widerspruchsfrist-Ablauf.
- `zv-titel-klausel-zustellung` – VB trägt Klausel kraft Gesetzes.
- `forderungsmanagement-klagewerkstatt/klagevorlage-aus-eigenen-mustern` – wenn Widerspruch und Übergang ins streitige Verfahren.
