---
name: liquiditaetsvorschau-insolvenzrechtlich
description: "Gerichtsfähige Liquiditätsbilanz und Liquiditätsvorschau für die Prüfung der Zahlungsunfähigkeit (§ 17 InsO) und die Fortbestehensprognose (§ 19 InsO). Standardergebnis ist eine Excel-Tabelle auf Wochenbasis; auf Wunsch ein HTML-Padlet oder Markdown-Artefakt zur fortlaufenden Pflege. Stützt sich auf die BGH-Rechtsprechung der letzten zehn Jahre (BGHZ 217, 129; BGHZ 163, 134; II ZR 112/21; IX ZR 48/21; IX ZR 229/22; II ZR 139/23). Memo nur auf Anfrage."
---

# Insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau

## Zweck

Dieser Skill erstellt eine **gerichtsfähig dokumentierte Liquiditätsbilanz** auf einen Stichtag und eine zugehörige **wochenaktuelle Liquiditätsvorschau** über mindestens drei Wochen, regelmäßig bis 13 Wochen, in der für § 17 InsO benötigten Form. Das Standardergebnis ist eine Excel-Tabelle auf Wochenbasis nach hinterlegter Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`). Auf Nutzerwunsch wird zusätzlich ein interaktives HTML-Padlet oder ein Markdown-Artefakt geliefert; ein Memo wird nur auf ausdrückliche Anfrage erstellt.

Anwendungsfälle:

- Geschäftsführerhaftung nach § 15b InsO; Insolvenzanfechtung nach §§ 129 ff. InsO.
- Gläubigerantrag § 14 InsO (Substantiierung der Forderung und Zahlungsunfähigkeit).
- Insolvenzverwalter im Haftungsprozess gegen Geschäftsleiter (Liquiditätsstatus aus Buchhaltung, BGH II ZR 88/16).
- Berater im Sanierungs- oder StaRUG-Kontext (Fortbestehensprognose § 19 InsO).

## Eingaben

Der Skill fragt strukturiert die folgenden Felder ab. Was fehlt, wird im Worst Case angesetzt und im Padlet/Artefakt als Annahme protokolliert.

- **Stichtag** (z. B. Tag der Antragstellung, frühester Eintritt § 17 InsO für Anfechtungszwecke).
- **Aktiva I**: Bankguthaben, Kasse, ungenutzter und zugesagter Kontokorrent, sofort verwertbares Vermögen.
- **Aktiva II**: konkret zu erwartende Zahlungseingänge KW *t* bis *t+2* (bzw. *t+12* bei 13-Wochen-Plan), freie Kreditzusagen, schnell verwertbares Umlaufvermögen, mit realistischer Ausfallquote.
- **Passiva I**: alle am Stichtag fälligen und ernsthaft eingeforderten Verbindlichkeiten; Stundungen nur, wenn echt vereinbart und dokumentiert.
- **Passiva II**: binnen drei Wochen fällig werdende Verbindlichkeiten, einzeln aufgeführt nach Gläubiger und Fälligkeitsdatum.
- **Titulierte Forderungen** gegen die Schuldnerin, bei denen Vollstreckung eingeleitet ist (in Höhe des Nennwerts in Passiva I aufnehmen — BGH IX ZR 229/22).
- **Indizien** nach § 17 Abs. 2 S. 2 InsO (Lohnsteuer-Rückstände, SV-Rückstände, Lastschriftrückläufer, Stundungsbitten, eingestellte Zahlungen FA/KK, Pfändungen, Insolvenzanträge anderer Gläubiger, Wechselproteste).
- **Buchhaltungsherkunft**: SuSa/OPOS aus DATEV oder vergleichbar — bei buchhaltungsbasiertem Liquiditätsstatus genügt der schlüssige Vortrag aus der Buchhaltung (BGH II ZR 88/16 Rn. 38 ff.); pauschales Bestreiten der Buchhaltung ist unzureichend.

## Bezugsquellen der Eingabedaten

Vor der Aufstellung folgende Frage stellen:

> Wie sollen die Daten einfließen — manuell, per Datei-Import (CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS-Export), oder über einen verbundenen Bankzugang (PSD2 / FinTS / vorhandener Connector)?

Detailregeln siehe Schwester-Skill `liquiditaetsvorschau-3wochen`, Abschnitt „Bezugsquellen der Eingabedaten" — der Skill selbst baut keinen Open-Banking-Client.

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

Die Bezugsgröße der Quote ist Σ(P I + P II) — BGH, Urt. v. 19.12.2017 – II ZR 88/16, BGHZ 217, 129 Rn. 25 ff. („Volumeneffekt").

**Schritt 4 — Subsumtion nach BGH-Schema**

- **Liquiditätsquote < 10 %**: regelmäßig keine Zahlungsunfähigkeit (BGH BGHZ 163, 134 Rn. 12 ff.); Zahlungsstockung bei prognostisch schließbarer Lücke binnen drei Wochen.
- **Liquiditätsquote ≥ 10 % und Lücke nicht binnen drei Wochen schließbar**: regelmäßig Zahlungsunfähigkeit.
- **Liquiditätsquote ≥ 10 %, Lücke binnen drei Wochen schließbar**: Zahlungsstockung, sofern nicht ausnahmsweise eine alsbaldige (fast) vollständige Schließung mit an Sicherheit grenzender Wahrscheinlichkeit zu erwarten ist und Gläubigern Zuwarten zumutbar ist (BGH BGHZ 217, 129 Rn. 16).
- **Alternative Darlegungsform**: Aneinanderreihung tagesgenauer Liquiditätsstatus zulässig (BGH, Urt. v. 28.06.2022 – II ZR 112/21 Rn. 21 ff.). Bei dieser Methode den Anfangs-Stichtag mit erheblicher Unterdeckung und an keinem Tag im Prognosezeitraum relevante Schließung dokumentieren.

**Schritt 5 — Würdigung der Indizien § 17 Abs. 2 S. 2 InsO**

Indizienkatalog nach BGH, Urt. v. 19.07.2007 – IX ZR 81/06 Rn. 36 ff. Bei Häufung Zahlungseinstellung bejahen — Vermutung des § 17 Abs. 2 S. 2 InsO greift, Beweislast für das Gegenteil beim Schuldner.

**Schritt 6 — Titulierte Forderungen**

Vorläufig vollstreckbare Titel über streitige Forderungen sind in Höhe des Nennwerts in Passiva I einzustellen, wenn die Voraussetzungen für die Vollstreckung vorliegen und der Titelgläubiger die Vollstreckung eingeleitet hat — BGH, Urt. v. 23.01.2025 – IX ZR 229/22 Rn. 18 ff.

**Schritt 7 — Objektivität**

Die Beurteilung erfolgt **allein anhand objektiver Umstände**; auf die innere Vorstellung des Geschäftsleiters kommt es nicht an — BGH, Urt. v. 11.03.2025 – II ZR 139/23.

**Schritt 8 — Ausgabe und Eskalation**

- Excel-Datei aus der Vorlage befüllen (zwingend).
- HTML-Padlet oder Markdown-Artefakt nur, wenn so gewählt.
- Bei Quote ≥ 10 % und fehlender Schließbarkeit: Übergabe an `antragspflicht-15a-inso`; bei Steuerberatermandat Hinweis nach § 102 StaRUG dokumentieren.
- Memo nur auf Anfrage.

## Rechtlicher Rahmen

### Primärnormen

§ 17 InsO, § 15a InsO, § 18 InsO, § 19 InsO, § 102 StaRUG.

### Leitentscheidungen (Volltexte: `references/rechtsprechung/`)

1. BGH, Urt. v. 19.12.2017 – II ZR 88/16, BGHZ 217, 129 Rn. 16 ff., 24 ff., 38 ff. — Passiva II; Substantiierungslast; Volumeneffekt.
2. BGH, Urt. v. 28.06.2022 – II ZR 112/21, ZIP 2022, 1606 Rn. 21 ff. — Aneinanderreihung tagesgenauer Liquiditätsstatus.
3. BGH, Urt. v. 28.04.2022 – IX ZR 48/21, ZIP 2022, 1341 Rn. 14 ff. — 10-%-Schwelle, geordnete Gegenüberstellung.
4. BGH, Urt. v. 23.01.2025 – IX ZR 229/22, DB 2025, 381 Rn. 18 ff. — titulierte Forderungen in Höhe des Nennwerts.
5. BGH, Urt. v. 11.03.2025 – II ZR 139/23 Rn. 12 ff. — Objektivität der Beurteilung.
6. BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 12 ff. — Grundsatzentscheidung.
7. BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 Rn. 36 ff. — Indizienkatalog.
8. BGH, Urt. v. 14.07.2006 – IX ZR 92/04, BGHZ 168, 158 Rn. 21 ff. — echte vs. erzwungene Stundung.

### Kommentarliteratur (Bearbeiter-Stil)

- *Mock*, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 10 ff., 30 ff., 72.
- *K. Schmidt/Herchen*, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 Rn. 5 ff., 22 ff., 32.

### Berufsständischer Hintergrund

- **IDW S 11** (Stand 12.08.2021), Tz. 16 f., 31–37 — Beurteilung des Eröffnungsgrundes der Zahlungsunfähigkeit.
- **IDW S 6** — Anforderungen an Sanierungskonzepte und integrierte Planung.

## Ausgabeformat

1. **Excel** auf Basis von `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx` — Wochenraster, BGH-Block, Block „Offene Forderungen", Hinweise zur BGH-Rechtsprechung.
2. **HTML-Padlet** (auf Wunsch).
3. **Markdown-Artefakt** (auf Wunsch).
4. **Memo** (nur auf Anfrage) im Gutachtenstil: Sachverhalt, Rechtliche Grundlagen, Liquiditätsbilanz, Subsumtion BGH-Schema, Indizienanalyse, Ergebnis, Quellennachweis.

## Beispiel

Siehe Schwester-Skill `liquiditaetsvorschau-3wochen` (Beispielfall Edelholz Manufaktur Berlin GmbH). Für gerichtsfeste Verwendung wird zusätzlich die Buchhaltungsherkunft (SuSa-/OPOS-Stand) protokolliert und die Indizienliste belegt.

## Typische Fehler

- **Stundungen fälschlich aus Passiva I herausnehmen**: nur echte, beiderseits vereinbarte und dokumentierte Stundungen — BGH IX ZR 92/04.
- **SV-Beiträge oder Lohnsteuer übersehen**: gesetzlich sofort fällig, zugleich Indizien.
- **Künftige Verträge / hypothetische Verwertungserlöse einbeziehen**: nicht zulässig in Aktiva I/II.
- **Stichtag im Haftungskontext zu spät ansetzen**: tatsächlicher Eintritt maßgeblich.
- **Pauschal die Buchhaltung bestreiten**: ist unzureichend — BGH II ZR 88/16 Rn. 38 ff. Konkret und einzeln vortragen.

## Quellenpflicht

Mindestens zwei BGH-Belege (jüngere zuerst) und zwei Kommentarbelege im Bearbeiterstil. IDW S 11 / S 6 als Hintergrund.

## Übergabe

Bei 🔴: `antragspflicht-15a-inso` und `zahlungsunfaehigkeit-pruefung-17-inso` (Plugin `insolvenzrecht`). Für mittel- und langfristige Sicht: `liquiditaetsvorschau-3-6-12-monate` (dieses Plugin).
