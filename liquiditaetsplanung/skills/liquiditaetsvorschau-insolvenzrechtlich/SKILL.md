---
name: liquiditaetsvorschau-insolvenzrechtlich
description: "Prüfungslinie für liquiditaetsvorschau insolvenzrechtlich im Liquiditaetsplanung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
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
- Insolvenzverwaltermandat (insb. nach BGH IX ZR 129/22 vom 18.04.2024 zur konkreten Darlegung der Liquiditätsunterdeckung im Anfechtungsprozess).
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

**Schritt 4 — Subsumtion nach BGH-Schema**

- **Liquiditätsquote < 10 % und Lücke binnen drei Wochen schließbar**: nur Zahlungsstockung.
- **Liquiditätsquote ≥ 10 % und Lücke nicht binnen drei Wochen schließbar**: regelmäßig Zahlungsunfähigkeit.
- Konkretes Az. der grundlegenden BGH-Entscheidung zum 10-%-/3-Wochen-Schema vor Ausgabe verifizieren.

**Schritt 5 — Würdigung der Indizien § 17 Abs. 2 S. 2 InsO**

Indizienkatalog für die Zahlungseinstellung umfasst insb. verspätete Lohnzahlungen, offene SV-Beiträge, erfolglose Stundungsbitten, Pfändungsmaßnahmen anderer Gläubiger, Wechselproteste und eigenen Insolvenzantrag. Konkrete BGH-Linie über offene Quellen verifizieren.

**Schritt 6 — Titulierte Forderungen**

Titulierte Forderungen sind regelmäßig fällig und in Passiva I aufzunehmen; ausnahmsweise kann eine streitige Titulierung im Anfechtungsprozess Indizwirkung mindern. Konkrete BGH-Entscheidung vor Ausgabe verifizieren.

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

### Leitentscheidungen (Stand Mai 2026; vor Ausgabe konkrete Aktenzeichen über dejure.org / openjur.de / bundesgerichtshof.de prüfen)

1. **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung der Vorsatzanfechtung: bei objektiv festgestellter Zahlungsunfähigkeit kein Automatik-Schluss auf Vorsatz; konkrete Bedrohungslage darzulegen. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
2. **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit beim Bargeschäft (§ 142 Abs. 1 Hs. 2 InsO). <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
3. **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers (§ 823 II BGB iVm § 15a InsO). <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
4. **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Wissentlichkeitsausschluss; positive Kenntnis pro Pflichtverletzung erforderlich.
5. **BGH 5 StR 287/24 vom 27.02.2025** — Faktischer Geschäftsführer / Firmenbestattung. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=27.02.2025&Aktenzeichen=5+StR+287/24>
6. Grundlegende ältere BGH-Linie zum 10-%-/3-Wochen-Schema und zur Zahlungseinstellung: konkrete Az. (insb. zur Liquiditätsbilanz, zu Stundungen, zu titulierten Forderungen, zur Erkennbarkeit der Insolvenzreife) vor Ausgabe in offener Quelle prüfen.

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

1. **Zweck der Vorschau?** ZU-Pruefung § 17 InsO (3-Wochen-Fenster) → insolvenzrechtliche Vorschau; Fortbestehensprognose § 19 InsO (12 Monate); Glaeubigernachweis (13-Wochen-Vorschau); Bankverhandlung (24 Monate)?
2. **Methode?** Direkte Methode (Cash-In / Cash-Out) fuer insolvenzrechtliche Zwecke; indirekte Methode (EBIT-Ableitung) fuer langfristige Unternehmensplanung.
3. **Datenbasis?** OPOS (offene Posten), Kontoauszuege, Steuer- und SV-Verbindlichkeiten — alle aktuell?
4. **Stichtag?** Fuer InsO-Beurteilung tag-genau festlegen; fuer Prognose ab aktuellem Tag.
5. **Sanierungsmassnahmen einbeziehen?** Stundungen, Zuschuss, neue Kreditlinie — nur wenn verbindlich zugesagt.

## Output-Template 13-Wochen-Liquiditaetsvorschau

**Adressat:** Insolvenzgericht / Glaeubigerausschuss / Bank — Tonfall: sachlich-betriebswirtschaftlich

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
