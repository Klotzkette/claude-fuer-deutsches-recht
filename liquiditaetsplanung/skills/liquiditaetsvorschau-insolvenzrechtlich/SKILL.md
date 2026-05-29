---
name: liquiditaetsvorschau-insolvenzrechtlich
description: "Workflow-Skill zu liquiditaetsvorschau insolvenzrechtlich. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau

## Zweck

Dieser Skill erstellt eine **gerichtsfähig dokumentierte Liquiditätsbilanz** auf einen Stichtag und eine zugehörige **wochenaktuelle Liquiditätsvorschau** über mindestens drei Wochen, regelmäßig bis 13 Wochen, in der für § 17 InsO benötigten Form. Das Standardergebnis ist eine Excel-Tabelle auf Wochenbasis nach hinterlegter Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`). Auf Nutzerwunsch wird zusätzlich ein interaktives HTML-Padlet oder ein Markdown-Artefakt geliefert; ein Memo wird nur auf ausdrückliche Anfrage erstellt.

Anwendungsfälle:

- Geschäftsführerhaftung nach § 15b InsO; Insolvenzanfechtung nach §§ 129 ff. InsO.
- Gläubigerantrag § 14 InsO (Substantiierung der Forderung und Zahlungsunfähigkeit).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Berater im Sanierungs- oder StaRUG-Kontext (Fortbestehensprognose § 19 InsO).

## Eingaben

Der Skill fragt strukturiert die folgenden Felder ab. Was fehlt, wird im Worst Case angesetzt und im Padlet/Artefakt als Annahme protokolliert.

- **Stichtag** (z. B. Tag der Antragstellung, frühester Eintritt § 17 InsO für Anfechtungszwecke).
- **Aktiva I**: Bankguthaben, Kasse, ungenutzter und zugesagter Kontokorrent, sofort verwertbares Vermögen.
- **Aktiva II**: konkret zu erwartende Zahlungseingänge KW *t* bis *t+2* (bzw. *t+12* bei 13-Wochen-Plan), freie Kreditzusagen, schnell verwertbares Umlaufvermögen, mit realistischer Ausfallquote.
- **Passiva I**: alle am Stichtag fälligen und ernsthaft eingeforderten Verbindlichkeiten; Stundungen nur, wenn echt vereinbart und dokumentiert.
- **Passiva II**: binnen drei Wochen fällig werdende Verbindlichkeiten, einzeln aufgeführt nach Gläubiger und Fälligkeitsdatum.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Indizien** nach § 17 Abs. 2 S. 2 InsO (Lohnsteuer-Rückstände, SV-Rückstände, Lastschriftrückläufer, Stundungsbitten, eingestellte Zahlungen FA/KK, Pfändungen, Insolvenzanträge anderer Gläubiger, Wechselproteste).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Bezugsquellen der Eingabedaten

Vor der Aufstellung folgende Frage stellen:

> Wie sollen die Daten einfließen — manuell, per Datei-Import (CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS-Export), oder über einen verbundenen Bankzugang (PSD2 / FinTS / vorhandener Connector)?

Detailregeln siehe Schwester-Skill `liquiditaetsvorschau-3wochen`, Abschnitt "Bezugsquellen der Eingabedaten" — der Skill selbst baut keinen Open-Banking-Client.

## Ablauf

**Schritt 1 — Format- und Padlet-Wahl**: identisch zum Schwester-Skill. Standard: Excel-Tabelle + HTML-Padlet, sofern nicht anders gewünscht.

**Schritt 2 — Stichtagsbestimmung**: konkretes Datum festlegen. Im Haftungs- und Anfechtungskontext ist nicht der Antragstag, sondern der tatsächliche Eintritt der Zahlungsunfähigkeit maßgeblich. Stichtag dokumentieren.

**Schritt 3 — Aufstellung der Liquiditätsbilanz**

```
Aktiva I  (am Stichtag sofort verfügbar)          €
+ Aktiva II (binnen 3 Wochen flüssig)             €
= Σ Liquide Mittel                                €

Passiva I (am Stichtag fällig & eingefordert)     €
+ Passiva II (binnen 3 Wochen fällig)             €
= Σ Fällige Verbindlichkeiten                     €

Liquiditätslücke (absolut) = Σ Fällig − Σ Liquide
Liquiditätsquote          = Liquiditätslücke ÷ Σ Fällig
```

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 4 — Subsumtion nach BGH-Schema**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Liquiditätsquote ≥ 10 % und Lücke nicht binnen drei Wochen schließbar**: regelmäßig Zahlungsunfähigkeit.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 5 — Würdigung der Indizien § 17 Abs. 2 S. 2 InsO**

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 6 — Titulierte Forderungen**

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 7 — Objektivität**

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Schritt 8 — Ausgabe und Eskalation**

- Excel-Datei aus der Vorlage befüllen (zwingend).
- HTML-Padlet oder Markdown-Artefakt nur, wenn so gewählt.
- Bei Quote ≥ 10 % und fehlender Schließbarkeit: Übergabe an `antragspflicht-15a-inso`; bei Steuerberatermandat Hinweis nach § 102 StaRUG dokumentieren.
- Memo nur auf Anfrage.

## Rechtlicher Rahmen

### Primärnormen

§ 17 InsO, § 15a InsO, § 18 InsO, § 19 InsO, § 102 StaRUG.

### Leitentscheidungen (Volltexte: `references/rechtsprechung/`)

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
6. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
7. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
8. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Berufsständischer Hintergrund

- **IDW S 11** (Stand 12.08.2021), Tz. 16 f., 31–37 — Beurteilung des Eröffnungsgrundes der Zahlungsunfähigkeit.
- **IDW S 6** — Anforderungen an Sanierungskonzepte und integrierte Planung.

## Ausgabeformat

1. **Excel** auf Basis von `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx` — Wochenraster, BGH-Block, Block "Offene Forderungen", Hinweise zur BGH-Rechtsprechung.
2. **HTML-Padlet** (auf Wunsch).
3. **Markdown-Artefakt** (auf Wunsch).
4. **Memo** (nur auf Anfrage) im Gutachtenstil: Sachverhalt, Rechtliche Grundlagen, Liquiditätsbilanz, Subsumtion BGH-Schema, Indizienanalyse, Ergebnis, Quellennachweis.

## Beispiel

Siehe Schwester-Skill `liquiditaetsvorschau-3wochen` (Beispielfall Edelholz Manufaktur Berlin GmbH). Für gerichtsfeste Verwendung wird zusätzlich die Buchhaltungsherkunft (SuSa-/OPOS-Stand) protokolliert und die Indizienliste belegt.

## Typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Aussetzung der Vollziehung (§ 361 AO / § 69 FGO) als Stundung behandeln**: AdV hemmt nur die Vollziehung; die Fälligkeit der Steuerforderung bleibt unberührt. AdV-Beträge sind weiter **Passiva I**, soweit nicht zusätzlich eine schriftliche § 222 AO-Stundung mit Fälligkeitsverschiebung über den Stichtag hinaus vorliegt.
- **SV-Beiträge oder Lohnsteuer übersehen**: gesetzlich sofort fällig, zugleich Indizien.
- **Künftige Verträge / hypothetische Verwertungserlöse einbeziehen**: nicht zulässig in Aktiva I/II.
- **Stichtag im Haftungskontext zu spät ansetzen**: tatsächlicher Eintritt maßgeblich.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

Bei 🔴: `antragspflicht-15a-inso` und `zahlungsunfaehigkeit-pruefung-17-inso` (Plugin `insolvenzrecht`). Für mittel- und langfristige Sicht: `liquiditaetsvorschau-3-6-12-monate` (dieses Plugin).


## Triage — Liquiditaetsvorschau Einordnung

Bevor losgelegt wird, klaere:

1. **Zweck der Vorschau?** ZU-Pruefung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Glaeubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) fuer insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) fuer langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Fuer InsO-Beurteilung tag-genau festlegen; fuer Prognose ab aktuellem Tag.
5. **Sanierungsmassnahmen einbeziehen?** Stundungen, Zuschuss, neue Kreditlinie — nur wenn verbindlich zugesagt.

## Output-Template 13-Wochen-Liquiditaetsvorschau

**Adressat:** Insolvenzgericht / Glaeubigerausschuss / Bank — Tonfall: sachlich-betriebswirtschaftlich

```
13-WOCHEN-LIQUIDITAETSVORSCHAU (direkte Methode)
Gesellschaft: [FIRMA]    Erstellt: [DATUM]    Ersteller: [NAME]

Woche | Anfangsbestand | Einzahlungen | Auszahlungen | Endbestand | Kreditlinie | Freie Liqui
  1   |   EUR [XXX]    |  EUR [YYY]   |  EUR [ZZZ]   |  EUR [AAA] |  EUR [BBB]  |  EUR [CCC]
  2   |   ...          |  ...         |  ...         |  ...       |  ...        |  ...
 13   |   ...          |  ...         |  ...         |  ...       |  ...        |  ...

AMPEL-STATUS:
Wochen 1-4 (kurzfristig): [GRUEN / GELB / ROT]
Wochen 5-9 (mittelfristig): [...]
Wochen 10-13 (langfristig): [...]

ENGPAESSE: [Beschreibung kritischer Wochen und Gegenmassnahmen]
ANNAHMEN: [Auflistung der Schluesselannahmen]
```
