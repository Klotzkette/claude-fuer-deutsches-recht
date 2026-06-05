---
name: zwangsvollstreckung-zv-mahnbescheid-online-mobiliar-gv
description: "ZV Mahnbescheid Online Mobiliar GV: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZV Mahnbescheid Online Mobiliar GV

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZV Mahnbescheid Online Mobiliar GV** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zv-mahnbescheid-online` | Gläubiger will Forderung ohne Klage per Mahnbescheid titulieren lassen. §§ 688 ff. ZPO Online-Mahnverfahren. Prüfraster: Schlüssigkeitsprüfung Antragstyp Gerichtsstand Hauptforderung Nebenforderungen Zinsen Kostenansatz beA EGVP Verjährungshemmung § 204 Abs. 1 Nr. 3 BGB. Output: Mahnbescheid-Antrag komplett ausgefuellt für Online-Portal. Abgrenzung zu zv-vollstreckungsbescheid-folge (Folgeschritt nach MB) und zv-kommandocenter. |
| `zv-mobiliar-gv-auftrag` | Gläubiger beauftragt Gerichtsvollzieher mit Sachpfaendung beweglicher Gegenstaende beim Schuldner. §§ 808 ff. ZPO Mobiliar-Pfaendung. Prüfraster: GV-Auftrag Modulwahl § 802a ZPO Anlaufstellen Wohnung Geschäftsräume Unpfaendbarkeitskatalog § 811 ZPO Austauschpfaendung § 811a ZPO Verwertung § 825 ZPO Internet-Versteigerung. Output: GV-Auftrag fertig zum Versand. Abgrenzung zu zv-pfueb-arbeitsentgelt (Lohnpfaendung) und zv-räumung-885 (Räumung). |
| `zv-notarielle-urkunde-grundschuld` | Gläubiger hat notarielle Grundschuld-Urkunde und will vollstrecken. § 794 Abs. 1 Nr. 5 ZPO Zwangsvollstreckung aus notarieller Urkunde. Prüfraster: Unterwerfungsklausel dinglich und persoenlich Klauselumschreibung § 727 ZPO bei Abtretung Sicherungsabrede Kündigung § 1193 BGB 6-Monats-Frist Vollstreckung Grundstueck ZVG vs. persoenliches Vermögen PfUeB. Output: Vollstreckungsstrategie und Schriftsatz-Entwurf. Abgrenzung zu zv-zvg-antrag-gläubiger (Versteigerung) und zv-titel-klausel-zustellung. |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZV Mahnbescheid Online Mobiliar GV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zv-mahnbescheid-online`

**Fokus:** Gläubiger will Forderung ohne Klage per Mahnbescheid titulieren lassen. §§ 688 ff. ZPO Online-Mahnverfahren. Prüfraster: Schlüssigkeitsprüfung Antragstyp Gerichtsstand Hauptforderung Nebenforderungen Zinsen Kostenansatz beA EGVP Verjährungshemmung § 204 Abs. 1 Nr. 3 BGB. Output: Mahnbescheid-Antrag komplett ausgefuellt für Online-Portal. Abgrenzung zu zv-vollstreckungsbescheid-folge (Folgeschritt nach MB) und zv-kommandocenter.

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

## auf www.online-mahnantrag.de

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

Schlüssigkeit: [JA – Anspruchsgrundlage XYZ / NEIN – Klage statt Mahnverfahren]
Anhängigkeit-Termin: [Verjährung droht zum DD.MM.JJJJ – Einreichung bis ...]

Antragsdaten:
- Antragsteller: [Name, Anschrift, ggf. ges. Vertreter]
- Antragsgegner: [Name, Anschrift, ggf. ges. Vertreter, HRB-Nr.]
- Hauptforderung: [EUR ...,..]
- Anspruchsbezeichn.: [Katalog-Nr. ...; Individualisierung: Rechnungsnr. ... v. DD.MM.JJJJ]
- Zinsen: [X % seit DD.MM.JJJJ – Anspruchsgrundlage § 288 BGB / Vertrag]
- Nebenforderungen: [Mahnkosten EUR ..; Inkassokosten EUR .. (Anwaltskosten Verzug)]
- Gegenleistung: [erbracht / nicht abhängig]
- Verfahrensgebühr: [EUR .. nach Nr. 1100 KV GKG]

Übermittlung: [beA mit EDA-XML / EGVP / Druck]
Wiedervorlage: [DD.MM.JJJJ (2 Wo nach voraussichtl. Zustellung)]
```

## Qualitätsgates

- Verbraucherdarlehen mit überhöhtem Zinssatz – Mahnverfahren unzulässig.
- Anspruchsbezeichnung muss eindeutig sein – sonst keine Verjährungshemmung.
- Bei Auslands-Schuldner ist Mahnverfahren oft nicht zulässig oder Europäisches Mahnverfahren (EuMahnVO) statt deutsches Mahnverfahren.

## Querverweise

- `zv-vollstreckungsbescheid-folge` – nach Widerspruchsfrist-Ablauf.
- `zv-titel-klausel-zustellung` – VB trägt Klausel kraft Gesetzes.
- `forderungsmanagement-klagewerkstatt/klagevorlage-aus-eigenen-mustern` – wenn Widerspruch und Übergang ins streitige Verfahren.

## 2. `zv-mobiliar-gv-auftrag`

**Fokus:** Gläubiger beauftragt Gerichtsvollzieher mit Sachpfaendung beweglicher Gegenstaende beim Schuldner. §§ 808 ff. ZPO Mobiliar-Pfaendung. Prüfraster: GV-Auftrag Modulwahl § 802a ZPO Anlaufstellen Wohnung Geschäftsräume Unpfaendbarkeitskatalog § 811 ZPO Austauschpfaendung § 811a ZPO Verwertung § 825 ZPO Internet-Versteigerung. Output: GV-Auftrag fertig zum Versand. Abgrenzung zu zv-pfueb-arbeitsentgelt (Lohnpfaendung) und zv-räumung-885 (Räumung).

# Mobiliar-Pfändung durch den Gerichtsvollzieher

## Aufgabe

Bewegliche Sachen des Schuldners pfänden, in Verwahrung nehmen und verwerten. Oft die ergiebigste Methode bei Selbstständigen oder Unternehmen, aber bei Privathaushalten in der Praxis selten lukrativ.

## Startet bei

- Titel + Klausel + Zustellung grün
- Bewegliche Sachen vermutet (Geschäftsausstattung, KFZ, hochwertige Privatgegenstände)
- Schuldner nicht in Insolvenz

## Rechtsgrundlagen

- §§ 803-882 ZPO – Mobiliarvollstreckung
- § 808 ZPO – Pfändung in der Wohnung
- § 809 ZPO – Pfändung bei Dritten
- § 811 ZPO – unpfändbare Sachen
- § 811a ZPO – Austauschpfändung
- § 811b ZPO – Verwertungsverbot bei Unpfändbarkeit
- § 813a ZPO – Vorpfändung
- § 815 ZPO – Geldpfändung
- § 825 ZPO – andere Verwertung, Internet-Versteigerung
- § 802a Abs. 2 Nr. 4 ZPO – Modulauftrag

## Workflow

1. **Drei-Säulen-Prüfung**.
2. **Auftrag an GV** über das Vollstreckungsportal oder Geschäftsstelle Amtsgericht (Wohnsitz Schuldner).
3. **Modulwahl § 802a ZPO**: regelmäßig Modul 3 (Sachpfändung) kombiniert mit Modul 1 (Zahlungsaufforderung). Modul 2 (Vermögensauskunft) zusätzlich, wenn Sachpfändung erfolglos.
4. **Anlaufort**: Wohnung des Schuldners (§ 808 ZPO), Geschäftsräume, KFZ-Standort. Bei Dritten nur mit Herausgabebereitschaft (§ 809 ZPO).
5. **Wohnungsbetretung**: ohne richterliche Anordnung Einwilligung nötig; bei Verweigerung Durchsuchungsanordnung § 758a ZPO.
6. **Unpfändbarkeitskatalog § 811 ZPO** beachten: Hausrat des täglichen Bedarfs, Berufsausübungsgegenstände, Hilfen für behinderte Menschen, religiöse Gegenstände, Tiere des Hauses, Gegenstände bis 500 EUR Wert für die Berufsausübung.
7. **Austauschpfändung § 811a ZPO**: Gläubiger stellt Ersatzsache zur Verfügung – pfändet Original, lässt Ersatz.
8. **Verwertung** § 814 ZPO (Versteigerung), § 825 ZPO (freihändig, Internet) – Wertgutachten bei KFZ.
9. **Vorpfändung § 813a ZPO**: schriftliche Ankündigung der Pfändung – ein Monat Schutzwirkung.

## Unpfändbarkeitskatalog § 811 ZPO – Top-Falle

Die häufigsten Fehlbewertungen:

- **Hochwertige Möbel/Kunst**: pfändbar, wenn ersetzbar durch einfachere Ware.
- **PC, Laptop**: Berufsausübungsschutz nur, wenn beruflich genutzt UND keine Ersatzmöglichkeit.
- **Hochzeitsringe**: regelmäßig pfändungsfrei aus Pietätsgründen.
- **KFZ**: pfändbar, soweit nicht für Beruf zwingend (Pendler in unzureichend angebundenem ÖPNV-Gebiet ggf. geschützt).
- **Tiere**: § 811 Abs. 1 Nr. 8b ZPO – Haustiere unpfändbar.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
MOBILIAR-AUFTRAG [Mandant] gegen [Schuldner], GV [Bezirk]

Titel: [Art, Datum]
Forderung: EUR Haupt + EUR Zinsen + EUR Kosten
Modul: [1 / 1+2 / 1+2+3]
Anlaufstelle: [Wohnung Adresse / Geschäft / KFZ]
Durchsuchungsanordn: [nicht erforderlich / § 758a ZPO beantragt]
Erwartete Pfandstücke: [KFZ, Maschinen, Lager, ...]
Voraussichtliche Kost: EUR x (GvKostG)

NÄCHSTER SCHRITT: GV-Termin abwarten
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals Mobiliarauftrag, wenn offensichtlich nur § 811-Gegenstände vorhanden – Kostenfalle.
- Niemals Durchsuchung ohne § 758a ZPO Anordnung, wenn Schuldner Einlass verweigert.
- Niemals Verwertung von Hochzeitsringen oder Tieren.
- Bei Selbstständigen: Berufsausübungsschutz bedenken, sonst Existenzgefährdung mit § 765a-Risiko.

## Querverweise

- `zv-titel-klausel-zustellung`
- `zv-vermoegensauskunft-gv` – wenn Sachpfändung erfolglos
- `zv-pfaendungstabelle-2025` (für Bargeld)
- `zv-abwehr-schuldner` – Schuldnersicht
- `zv-raeumung-885` – ähnliche GV-Logik

## 3. `zv-notarielle-urkunde-grundschuld`

**Fokus:** Gläubiger hat notarielle Grundschuld-Urkunde und will vollstrecken. § 794 Abs. 1 Nr. 5 ZPO Zwangsvollstreckung aus notarieller Urkunde. Prüfraster: Unterwerfungsklausel dinglich und persoenlich Klauselumschreibung § 727 ZPO bei Abtretung Sicherungsabrede Kündigung § 1193 BGB 6-Monats-Frist Vollstreckung Grundstueck ZVG vs. persoenliches Vermögen PfUeB. Output: Vollstreckungsstrategie und Schriftsatz-Entwurf. Abgrenzung zu zv-zvg-antrag-gläubiger (Versteigerung) und zv-titel-klausel-zustellung.

# Vollstreckung aus notarieller Grundschuldurkunde

## Aufgabe

Banken und Investoren stützen die Vollstreckung in Immobilien fast immer auf eine notarielle Urkunde mit Grundschuld und Unterwerfungsklausel. Dieser Skill koordiniert beide Vollstreckungsrichtungen: dinglich in das Grundstück, persönlich in das sonstige Vermögen.

## Startet bei

- Notarielle Urkunde mit Grundschuld vorhanden
- Unterwerfung des Eigentümers/Schuldners "in sein gesamtes Vermögen" und/oder "in den jeweiligen Grundbesitz"
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
 - **Titel**: notarielle Urkunde mit Unterwerfung – wurde sie als "Vollstreckungstitel" ausgestellt (in der Regel formularmäßig "der Eigentümer unterwirft sich ...").
 - Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - **Zustellung** der vollstreckbaren Ausfertigung an den Schuldner; bei dinglicher Vollstreckung an den Eigentümer (auch Dritter) nach § 800 Abs. 2 ZPO.
2. **Kündigung Grundschuld § 1193 BGB**: sechs Monate Kündigungsfrist, abdingbar nur eingeschränkt (AGB-Kontrolle gem. § 307 BGB). Kündigungsschreiben zustellen.
3. **Sicherungsabrede prüfen**: Welche Forderungen sichert die Grundschuld? Aktuelle Höhe? Zinsen? Übersicherung? Einrede § 1192 Abs. 1a BGB bei Abtretung.
4. **Dingliche Vollstreckung**: ZVG-Antrag → `zv-zvg-antrag-glaeubiger`.
5. **Persönliche Vollstreckung**: zusätzlich PfÜB Bank/Lohn → `zv-pfueb-bank` / `zv-pfueb-arbeitsentgelt`.
6. **Insolvenz**: Bei Schuldner-Insolvenz wird der Grundschuldgläubiger Absonderungsberechtigter (§ 49 InsO) – Vollstreckung außerhalb der Insolvenztabelle weiterhin möglich, aber Verwertung über Insolvenzverwalter ggf. günstiger.

## Klauselumschreibung § 727 ZPO bei Forderungsabtretung

Wird die gesicherte Forderung an einen neuen Gläubiger abgetreten (typisch bei Forderungskäufen, Loan-Sale), muss der neue Gläubiger:

- die Abtretung im notariell beglaubigtem Wege nachweisen
- den Klauselantrag beim ausstellenden Notar (oder hilfsweise § 797 ZPO) stellen
- die Klauselzustellung an den Schuldner durchführen, bevor er aus der Urkunde vollstrecken darf.

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sicherungsgrundschuld – Einreden § 1192 Abs. 1a BGB

Schuldner kann gegenüber neuem Erwerber alle Einreden geltend machen, die ihm gegen den ursprünglichen Sicherungsgeber zustanden – auch wenn der neue Erwerber gutgläubig war (Einschränkung des § 1157 Satz 2 BGB).

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
NOTAR. URKUNDE / GRUNDSCHULD [Mandant] gegen [Schuldner], Az [Notar]

Urkunde: Notar [Name], URNr [Nr/Jahr]
Grundschuld: EUR x, Zinsen x %, GB [Ort, Bl, lfd Nr]
Unterwerfung: [dinglich / persönlich / beides]
Sicherungsabrede: [Datum, Gegenstand]
Kündigung § 1193: [erforderlich? ja, am DD.MM.JJJJ erklärt]
Klausel § 727: [nicht erforderlich / umschrieben am DD.MM.JJJJ]
Zustellung § 750: [erfolgt an DD.MM.JJJJ]
Vollstreckungswege: [ZVG / PfÜB Bank / PfÜB Lohn]

NÄCHSTE SKILLS: zv-zvg-antrag-glaeubiger, zv-pfueb-bank
WIEDERVORLAGE: DD.MM.JJJJ + 6 Monate (Kündigungsfrist)
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
