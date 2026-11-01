---
name: steuern-quellensteuer-und-dba-lizenz
description: "Für Steuern und Quellensteuer — Lizenz: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen."
---

# Steuern und Quellensteuer — Lizenz

## 1. Steuerthemen

### 1.1. Quellensteuer auf Royalties

| Norm | Inhalt |
|---|---|
| Paragraf 49 EStG | Zunächst die inländischen Einkünfte und die einschlägige Einkunftsart feststellen; ein ausländischer Sitz allein begründet keinen Steuerabzug. |
| Paragraf 50a Absatz 1 Nummer 3, Absatz 2 und Absatz 5 EStG | Bei erfassten Lizenzvergütungen beträgt der Steuerabzug grundsätzlich 15 % der gesamten Einnahmen. Der Lizenznehmer als Vergütungsschuldner behält die Steuer für Rechnung des Lizenzgebers ein und führt sie ab; ein anfallender Solidaritätszuschlag ist gesondert zu berücksichtigen. |
| Paragraf 50c Absatz 2 und Absatz 3 EStG | Das Bundeszentralamt für Steuern (BZSt) entscheidet über die Freistellungsbescheinigung nach Absatz 2 und die Erstattung bereits entrichteter Abzugsteuer nach Absatz 3. |
| Paragraf 50d Absatz 3 EStG | Bei abkommensrechtlicher Entlastung die persönlichen und wirtschaftlichen Voraussetzungen sowie die gesetzlichen Ausnahmen der Missbrauchsregelung prüfen. Die Vorschrift ersetzt nicht das Entlastungsverfahren nach Paragraf 50c EStG. |

Amtliche Prüfgrundlagen: [Paragraf 50a EStG](https://www.gesetze-im-internet.de/estg/__50a.html), [Paragraf 50c EStG](https://www.gesetze-im-internet.de/estg/__50c.html), [Paragraf 50d EStG](https://www.gesetze-im-internet.de/estg/__50d.html), die [BZSt-Information zum Steuerabzug und Solidaritätszuschlag](https://online.portal.bzst.de/SharedDocs/Leistungsbeschreibung/DE/steuerabzugsverfahren_nach_50_a.html?nn=25056) und die [BOP-Hilfe zu Freistellung und Erstattung bei Lizenzvergütungen](https://www.elster.de/bportal/helpGlobal?themaGlobal=help_stabentlastung). Den materiellen DBA-Anspruch, das Entlastungsverfahren und vertragliche Mitwirkungspflichten getrennt prüfen.

### 1.2. DBA-Reduktion

Doppelbesteuerungsabkommen reduzieren regelmaessig die Quellensteuer:

| DBA | Lizenz-Quellensteuer |
|---|---|
| DE-USA | 0 % (Art. 12 DBA-USA bei Antragsverfahren) |
| DE-CH | 0 % (Art. 12 DBA-CH) |
| DE-UK | 0 % (Art. 12 DBA-UK) |
| DE-FR | 0 % (EU-Zinsen-Lizenz-RL 2003/49/EG bei Konzernschwester) |
| DE-NL | 0 % (Art. 12 DBA-NL) |
| DE-China | 10 % |
| DE-Indien | 10 % |

→ Vor Vertragsschluss: DBA prüfen, Freistellungsbescheinigung beantragen.

### 1.3. EU-Zinsen-Lizenzgebühren-Richtlinie (2003/49/EG)

Bei Lizenzen zwischen verbundenen Unternehmen (mindestens 25 % Beteiligung) in EU-Mitgliedstaaten: Quellensteuer 0 %.

### 1.4. Umsatzsteuer

- B2B Lizenz innerhalb EU: Reverse-Charge (Paragraf 13b UStG)
- B2C Lizenz: USt-Pflicht im Empfaengerland
- Aussergewoehnliche Geschäftsveraeusserung im Ganzen: Paragraf 1 Ia UStG - bei IP-Voll-Uebertragung ggf. einschlaegig (siehe EuGH Zita Modes C-497/01)

## Klausel-Bausteine

**A. Quellensteuer-Klausel (Groß-up):**
> "Paragraf 19 Steuern.
> (1) Lizenzgebuehren sind ohne Abzug von Steuern, Gebuehren oder anderen Abgaben zu zahlen.
> (2) Sofern der Lizenznehmer kraft Gesetzes verpflichtet ist, von der Lizenzgebuehr Quellensteuer einzubehalten, erhoeht sich die Lizenzgebuehr um den Betrag der Quellensteuer (Groß-up), so dass der Lizenzgeber den vertraglich vereinbarten Nettobetrag erhaelt.
> (3) Sofern der Lizenzgeber durch DBA-Anwendung oder die EU-Zinsen-Lizenz-Richtlinie einen reduzierten Quellensteuersatz oder Steuerbefreiung beanspruchen kann, wirkt er bei der Beschaffung der erforderlichen Bescheinigungen mit."

**B. Umsatzsteuer:**
> "(4) Die Lizenzgebuehren sind Nettobetraege. Auf die Lizenzgebuehr ist die gesetzliche Umsatzsteuer hinzuzurechnen. Bei B2B-Konstellationen innerhalb der EU gilt das Reverse-Charge-Verfahren (Paragraf 13b UStG)."

**C. Steuer-Erstattung:**
> "(5) Wird die Quellensteuer rueckwirkend reduziert oder erstattet, fliesst der Erstattungsbetrag dem Lizenzgeber zu, soweit dieser den Groß-up bereits getragen hat."

## Prüfroutine vor Vertragsschluss

```
1. Ist der Lizenzgeber beschraenkt steuerpflichtig (Sitz im Ausland)?
2. Welches DBA gilt?
3. Quellensteuer-Reduktion moeglich?
4. Freistellungsbescheinigung BZSt vorhanden?
5. Gross-up-Klausel im Vertrag?
6. Verbundene Unternehmen? Dann EU-Zinsen-Lizenz-RL pruefen.
7. USt-Behandlung in Anlage E festhalten.
```

## Anschluss

- Verguetungsstruktur: `klausel-verguetung-pauschale-royalty-tiered`
- Rechtswahl bei Cross-Border: `klausel-rechtswahl-gerichtsstand-schiedsklausel`
