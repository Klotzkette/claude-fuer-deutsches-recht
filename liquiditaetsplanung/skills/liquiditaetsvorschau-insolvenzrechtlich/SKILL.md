---
name: liquiditaetsvorschau-insolvenzrechtlich
description: "Prüft insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau mit Passiva-Logik, streitigen Forderungen, Titeln, Stundungen und Sanierungsübergabe."
---

# Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau

## Fachkern: Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

## Zweck

Dieser Skill erstellt eine **gerichtsfähig dokumentierte Liquiditätsbilanz** auf einen Stichtag und eine zugehörige **wochenaktuelle Liquiditätsvorschau** über mindestens drei Wochen, regelmäßig bis 13 Wochen, in der für § 17 InsO benötigten Form. Das Standardergebnis ist eine Excel-Tabelle auf Wochenbasis nach hinterlegter Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`). Auf Nutzerwunsch wird zusätzlich ein interaktives HTML-Padlet oder ein Markdown-Artefakt geliefert; ein Memo wird nur auf ausdrückliche Anfrage erstellt.

Anwendungsfälle:

- Geschäftsführerhaftung nach § 15b InsO; Insolvenzanfechtung nach §§ 129 ff. InsO.
- Gläubigerantrag § 14 InsO (Substantiierung der Forderung und Zahlungsunfähigkeit).
- Insolvenzverwaltermandat, Anfechtungsabwehr und Gläubigerantrag, insbesondere nach BGH IX ZR 129/22 vom 18.04.2024 zur konkreten Darlegung von Liquiditätsstatus, Einzelposten und Belegen.
- Berater im Sanierungs- oder StaRUG-Kontext (Fortbestehensprognose § 19 InsO).
- Sanierungskonzept-Vorarbeit, wenn aus der kurzfristigen Liquiditätsbilanz eine integrierte Sanierungsplanung werden soll.

## Eingaben

Der Skill fragt strukturiert die folgenden Felder ab. Was fehlt, wird im Worst Case angesetzt und im Padlet/Artefakt als Annahme protokolliert.

- **Stichtag** (z. B. Tag der Antragstellung, frühester Eintritt § 17 InsO für Anfechtungszwecke).
- **Aktiva I**: Bankguthaben, Kasse, ungenutzter und zugesagter Kontokorrent, sofort verwertbares Vermögen.
- **Aktiva II**: konkret zu erwartende Zahlungseingänge KW *t* bis *t+2* (bzw. *t+12* bei 13-Wochen-Plan), freie Kreditzusagen, schnell verwertbares Umlaufvermögen, mit realistischer Ausfallquote.
- **Passiva I**: alle am Stichtag fälligen und ernsthaft eingeforderten Verbindlichkeiten; Stundungen nur, wenn echt vereinbart und dokumentiert.
- **Passiva II**: binnen drei Wochen fällig werdende Verbindlichkeiten, einzeln aufgeführt nach Gläubiger und Fälligkeitsdatum.
- **Echte Stundung** (mit beiderseitigem Einvernehmen und Fälligkeitsverschiebung) beseitigt Passiva I; faktische Duldung des Zahlungsverzugs nicht. Konkrete BGH-Linie über offene Quellen verifizieren.
- **Streitige oder titulierte Forderungen**: materieller Bestand, Fälligkeit, Titel, Vollstreckungsbeginn, Einstellung der Vollstreckung und Beleg getrennt erfassen; keine Prozentquote nach Prozessrisiko. Summen-OPOS ohne Einzelposten, Rechtsgrund und Beleg wird als Darlegungslücke markiert.
- **Indizien** nach § 17 Abs. 2 S. 2 InsO (Lohnsteuer-Rückstände, SV-Rückstände, Lastschriftrückläufer, Stundungsbitten, eingestellte Zahlungen FA/KK, Pfändungen, Insolvenzanträge anderer Gläubiger, Wechselproteste).

## Bezugsquellen der Eingabedaten

Vor der Aufstellung folgende Frage stellen:

> Wie sollen die Daten einfließen — manuell, per Datei-Import (CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS-Export), oder über einen verbundenen Bankzugang (PSD2 / FinTS / vorhandener Connector)?

Detailregeln siehe Schwester-Skill `liquiditaetsvorschau-3wochen`, Abschnitt "Bezugsquellen der Eingabedaten" — der Skill selbst baut keinen Open-Banking-Client.

## Ablauf

**Schritt 1 — Format- und Padlet-Wahl**: identisch zum Schwester-Skill. Standard: Excel-Tabelle + HTML-Padlet, sofern nicht anders gewünscht.

**Schritt 2 — Stichtagsbestimmung**: konkretes Datum festlegen. Im Haftungs- und Anfechtungskontext ist nicht der Antragstag, sondern der tatsächliche Eintritt der Zahlungsunfähigkeit maßgeblich. Stichtag dokumentieren.

**Schritt 3 — Aufstellung der Liquiditätsbilanz**

```
Aktiva I (am Stichtag sofort verfügbar) €
+ Aktiva II (binnen 3 Wochen flüssig) €
= Σ Liquide Mittel €

Passiva I (am Stichtag fällig & eingefordert) €
+ Passiva II (binnen 3 Wochen fällig) €
= Σ Fällige Verbindlichkeiten €

Liquiditätslücke (absolut) = Σ Fällig − Σ Liquide
Liquiditätsquote = Liquiditätslücke ÷ Σ Fällig
```

Maßstab: BGH-Linie zur Liquiditätsbilanz; konkrete Aktenzeichen und Randnummern vor Ausgabe über dejure.org / openjur.de verifizieren.

Sonderlogik für streitige Posten: Eine streitige Verbindlichkeit wird nicht geschätzt. Wenn sie materiell besteht und fällig ist, gehört sie mit Nennwert in Passiva I oder Passiva II. Wenn sie materiell nicht besteht, nicht fällig ist oder wirksam gestundet wurde, gehört sie nicht in die Passiva. Wenn ein vorläufig vollstreckbarer Titel vorliegt und die Vollstreckung eingeleitet ist, wird der Nennwert angesetzt. Wenn eine Einstellung der Zwangsvollstreckung erreicht wurde, wird die Beweiswirkung des Titels gesondert bewertet und die Forderung in einem Szenarioblock geführt. Aktivseitig werden eigene Forderungen nur angesetzt, wenn der Zahlungseingang binnen drei Wochen realistisch belegt ist. Für die gerichtliche Darlegung wird jeder Posten einzeln mit Gläubiger, Fälligkeit, Rechtsgrund, Beleg, Bestreitensstand und Vollstreckungsstand geführt; pauschale Summenlisten sind nach BGH IX ZR 129/22 angreifbar.

**Schritt 4 — Subsumtion nach BGH-Schema**

- **Liquiditätsquote < 10 % und Lücke binnen drei Wochen schließbar**: nur Zahlungsstockung.
- **Liquiditätsquote ≥ 10 % und Lücke nicht binnen drei Wochen schließbar**: regelmäßig Zahlungsunfähigkeit.
- Konkretes Az. der grundlegenden BGH-Entscheidung zum 10-%-/3-Wochen-Schema vor Ausgabe verifizieren.

**Schritt 5 — Würdigung der Indizien § 17 Abs. 2 S. 2 InsO**

Indizienkatalog für die Zahlungseinstellung umfasst insb. verspätete Lohnzahlungen, offene SV-Beiträge, erfolglose Stundungsbitten, Pfändungsmaßnahmen anderer Gläubiger, Wechselproteste und eigenen Insolvenzantrag. Konkrete BGH-Linie über offene Quellen verifizieren.

**Schritt 6 — Titulierte Forderungen**

Bei titulierten Forderungen nicht bei "streitig" stehen bleiben. Das Prüfraster lautet:

1. Besteht die Forderung materiell und ist sie fällig? Dann mit Nennwert passivieren, auch wenn sie bestritten wird.
2. Besteht die Forderung materiell nicht oder ist sie aus Rechtsgründen nicht fällig? Dann nicht passivieren, auch wenn sie behauptet wird.
3. Gibt es einen vorläufig vollstreckbaren Titel, liegen die Vollstreckungsvoraussetzungen vor und hat der Gläubiger Vollstreckung eingeleitet? Dann Nennwert passivieren; kein Abschlag nach Prozessrisiko.
4. Ist die Zwangsvollstreckung aus dem Titel einstweilen eingestellt? Dann Beweiswirkung für den Gläubigerantrag und Liquiditätsabfluss gesondert würdigen.
5. Ist der Titel nur ein Indiz in einer breiteren Liquiditätslage? Dann den titulierten Betrag und die sonstigen fälligen Verbindlichkeiten getrennt ausweisen.

**Schritt 7 — Objektivität**

Maßstab der Zahlungsunfähigkeit ist objektiv; das Bewusstsein des Schuldners ist nur für die Verschuldensfrage relevant (§ 15a InsO). Konkrete BGH-Linie zur "Erkennbarkeit der Insolvenzreife" vor Ausgabe über offene Quellen prüfen.

**Schritt 8 — Ausgabe und Eskalation**

- Excel-Datei aus der Vorlage befüllen (zwingend).
- HTML-Padlet oder Markdown-Artefakt nur, wenn so gewählt.
- Bei Quote ≥ 10 % und fehlender Schließbarkeit: Übergabe an `antragspflicht-15a-inso`; bei Steuerberatermandat Hinweis nach § 102 StaRUG dokumentieren.
- Wenn die Vorschau für Bank, StaRUG, Schutzschirm, Eigenverwaltung oder Insolvenzplan genutzt werden soll: ausdrücklich festhalten, dass die Liquiditätsbilanz nur die Cash-Seite liefert. Danach an `idw-s6-integrierte-sanierungsplanung` übergeben, um GuV, Planbilanz, Maßnahmenwirkung, Leitbild und nachhaltige Sanierungsfähigkeit zu prüfen.
- Memo nur auf Anfrage.

## Rechtlicher Rahmen

### Primärnormen

§ 17 InsO, § 15a InsO, § 18 InsO, § 19 InsO, § 102 StaRUG.

### Leitentscheidungen (Stand Juni 2026; vor Ausgabe konkrete Aktenzeichen über dejure.org / openjur.de / bundesgerichtshof.de prüfen)

1. **BGH IX ZR 229/22 vom 23.01.2025** — vorläufig vollstreckbar titulierte streitige Forderung bei eingeleiteter Vollstreckung mit Nennwert in den Liquiditätsstatus; keine anteilige Bewertung nach Prozessrisiko.
2. **BGH II ZR 139/23 vom 11.03.2025** — Verbindlichkeit zählt nach materiellem Bestand; Zahlungsunfähigkeit ist objektiv zu bestimmen.
3. **BGH IX ZB 38/24 vom 22.05.2025** — bei allein auf einen Titel gestütztem Gläubigerantrag kann die Beweiswirkung entfallen, wenn die Zwangsvollstreckung aus dem Urteil eingestellt ist.
4. **BGH IX ZR 129/22 vom 18.04.2024** — Liquiditätsstatus gegenüber außenstehenden Dritten konkret darlegen; ohne Einzelheiten und Belege kann einfaches Bestreiten genügen. Außerdem in der Vorsatzanfechtung konkrete Bedrohungslage darlegen. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22
5. **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit beim Bargeschäft nach Paragraf 142 Absatz 1 Halbsatz 2 InsO. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23
6. **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers nach Paragraf 823 Absatz 2 BGB in Verbindung mit Paragraf 15a InsO. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22
7. Grundlegende ältere BGH-Linie zum 10-%-/3-Wochen-Schema und zur Zahlungseinstellung: konkrete Az. zur Liquiditätsbilanz, zu Stundungen, zu titulierten Forderungen und zur Erkennbarkeit der Insolvenzreife vor Ausgabe in offener Quelle prüfen.

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

- **Faktische Duldung als Stundung behandeln**: nur echte schriftliche Stundungsvereinbarung mit Fälligkeitsverschiebung beseitigt Passiva I. Konkrete BGH-Linie über offene Quellen verifizieren.
- **Aussetzung der Vollziehung (§ 361 AO / § 69 FGO) als Stundung behandeln**: AdV hemmt nur die Vollziehung; die Fälligkeit der Steuerforderung bleibt unberührt. AdV-Beträge sind weiter **Passiva I**, soweit nicht zusätzlich eine schriftliche § 222 AO-Stundung mit Fälligkeitsverschiebung über den Stichtag hinaus vorliegt.
- **Titulierte Forderung nur anteilig nach Prozessrisiko ansetzen**: bei eingeleiteter Vollstreckung aus vorläufig vollstreckbarem Titel Nennwert, nicht Wahrscheinlichkeitswert.
- **Liquiditätsstatus nur als Summenblock übernehmen**: nach BGH IX ZR 129/22 braucht die beweissichere Fassung Einzelposten, Fälligkeit, Rechtsgrund und Beleg; sonst kann ein außenstehender Gegner einfach bestreiten.
- **SV-Beiträge oder Lohnsteuer übersehen**: gesetzlich sofort fällig, zugleich Indizien.
- **Künftige Verträge / hypothetische Verwertungserlöse einbeziehen**: nicht zulässig in Aktiva I/II.
- **Stichtag im Haftungskontext zu spät ansetzen**: tatsächlicher Eintritt maßgeblich.
- **Konkrete Erwartung dauerhafter Unterdeckung nicht dokumentiert**: nach BGH IX ZR 129/22 (18.04.2024) ist die bloße Liquiditätsunterdeckung allein für die Vorsatzanfechtung nicht ausreichend; Verwalter muss die Erwartung dauerhafter Nichtbefriedigung anderer Gläubiger konkret darlegen.
- **Liquiditätsbilanz mit Sanierungskonzept verwechselt**: Für Sanierungsfähigkeit reicht die insolvenzrechtliche Cash-Prüfung nicht. Es braucht zusätzlich Krisenursachenanalyse, Leitbild, Maßnahmenprogramm, GuV-/Bilanzplanung, Szenarien und Dokumentation.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

Bei 🔴: `antragspflicht-15a-inso` und `zahlungsunfaehigkeit-pruefung-17-inso` (Plugin `insolvenzrecht`). Für mittel- und langfristige Sicht: `liquiditaetsvorschau-3-6-12-monate` (dieses Plugin). Für Sanierungskonzept-/Bankfähigkeit: `idw-s6-integrierte-sanierungsplanung` (dieses Plugin).

## Triage — Liquiditaetsvorschau Einordnung

Bevor losgelegt wird, klaere:

1. **Zweck der Vorschau?** ZU-Prüfung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Gläubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) für insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) für langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Für InsO-Beurteilung tag-genau festlegen; für Prognose ab aktuellem Tag.
5. **Sanierungsmassnahmen einbeziehen?** Stundungen, Zuschuss, neue Kreditlinie — nur wenn verbindlich zugesagt.

## Output-Template 13-Wochen-Liquiditaetsvorschau

**Adressat:** Insolvenzgericht / Gläubigerausschuss / Bank — Tonfall: sachlich-betriebswirtschaftlich

```
13-WOCHEN-LIQUIDITAETSVORSCHAU (direkte Methode)
Gesellschaft: [FIRMA] Erstellt: [DATUM] Ersteller: [NAME]

Woche | Anfangsbestand | Einzahlungen | Auszahlungen | Endbestand | Kreditlinie | Freie Liqui
 1 | EUR [XXX] | EUR [YYY] | EUR [ZZZ] | EUR [AAA] | EUR [BBB] | EUR [CCC]
 2 | ... | ... | ... | ... | ... | ...
 13 | ... | ... | ... | ... | ... | ...

AMPEL-STATUS:
Wochen 1-4 (kurzfristig): [GRUEN / GELB / ROT]
Wochen 5-9 (mittelfristig): [...]
Wochen 10-13 (langfristig): [...]

ENGPAESSE: [Beschreibung kritischer Wochen und Gegenmassnahmen]
ANNAHMEN: [Auflistung der Schluesselannahmen]
```
