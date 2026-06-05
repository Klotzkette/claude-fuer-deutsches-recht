---
name: zpo-zwangsvollstreckung-zv-abwehr
description: "ZPO Zwangsvollstreckung ZV Abwehr: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZPO Zwangsvollstreckung ZV Abwehr

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZPO Zwangsvollstreckung ZV Abwehr** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-zpo-tatbestand-beweis-und-belege` | ZPO: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-zwangsvollstreckung-erstpruefung-und-mandatsziel` | Zwangsvollstreckung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `zv-abwehr-schuldner` | Schuldner will sich gegen laufende Zwangsvollstreckung wehren oder hat unrechtmäßigen Pfaendungs-Beschluss erhalten. §§ 766 767 768 771 765a 850k 769 ZPO Schuldnerrechte. Prüfraster: Erinnerung § 766 formale Maengel Vollstreckungsabwehrklage § 767 materielle Einwendungen Klauselgegenklage § 768 Drittwiderspruchsklage § 771 Vollstreckungsschutz § 765a P-Konto-Freigabe § 850k Einstellung § 769. Output: Abwehrstrategie-Memo und passender Schriftsatz-Entwurf. Abgrenzung zu zv-vollstreckungsschutz-haertefall-765a (Haertefall-Schutz) und zv-pfaendungstabelle-2025 (Pfaendungsberechnung). |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZPO Zwangsvollstreckung ZV Abwehr**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-zpo-tatbestand-beweis-und-belege`

**Fokus:** ZPO: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# ZPO: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: ZPO: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** ZPO: Tatbestandsmerkmale, Beweisfragen und Beleglage / zpo tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **ZPO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-zwangsvollstreckung-erstpruefung-und-mandatsziel`

**Fokus:** Zwangsvollstreckung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Zwangsvollstreckung: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Zwangsvollstreckung: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Zwangsvollstreckung: Erstprüfung, Rollenklärung und Mandatsziel / zwangsvollstreckung erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Zwangsvollstreckung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `zv-abwehr-schuldner`

**Fokus:** Schuldner will sich gegen laufende Zwangsvollstreckung wehren oder hat unrechtmäßigen Pfaendungs-Beschluss erhalten. §§ 766 767 768 771 765a 850k 769 ZPO Schuldnerrechte. Prüfraster: Erinnerung § 766 formale Maengel Vollstreckungsabwehrklage § 767 materielle Einwendungen Klauselgegenklage § 768 Drittwiderspruchsklage § 771 Vollstreckungsschutz § 765a P-Konto-Freigabe § 850k Einstellung § 769. Output: Abwehrstrategie-Memo und passender Schriftsatz-Entwurf. Abgrenzung zu zv-vollstreckungsschutz-haertefall-765a (Haertefall-Schutz) und zv-pfaendungstabelle-2025 (Pfaendungsberechnung).

# Schuldnerabwehr in der Zwangsvollstreckung

## Aufgabe

Gegenmittel für Schuldner und betroffene Dritte. Die Vollstreckung ist staatlicher Eingriff – Skill nutzt die zulässigen Verteidigungswege punktgenau.

## Startet bei

- Mandant ist Schuldner einer laufenden Vollstreckung
- Pfändung oder Räumung steht bevor / läuft
- Gläubiger geht aus aufgehobener oder bezahlter Forderung vor / Pfändung verstößt gegen Pfändungsfreigrenzen
- Restschuldbefreiung wurde erteilt und trotzdem wird vollstreckt

## Rechtsgrundlagen

- § 765a ZPO – Vollstreckungsschutz, Härtefall
- § 766 ZPO – Erinnerung gegen Art und Weise der Vollstreckung
- § 767 ZPO – Vollstreckungsabwehrklage (materielle Einwendungen nach Schluss der mündlichen Verhandlung)
- § 768 ZPO – Klauselgegenklage
- § 769 ZPO – einstweilige Einstellung
- § 771 ZPO – Drittwiderspruchsklage
- § 850c-l ZPO – Pfändungsfreigrenze, § 850k ZPO P-Konto-Freigabe
- § 802d ZPO – Sperrfrist Vermögensauskunft
- § 301 InsO – Wirkung Restschuldbefreiung

## Verteidigungslandkarte

| Angriff des Gläubigers | Gegenmittel | Gericht |
| --- | --- | --- |
| Pfändung formal fehlerhaft (z. B. Zustellungsmangel) | Erinnerung § 766 ZPO | Vollstreckungsgericht |
| Forderung erfüllt, gestundet, verjährt, aufgerechnet (nach mündl. Verhandlung) | Vollstreckungsabwehrklage § 767 ZPO | Prozessgericht 1. Instanz |
| Klauselumschreibung § 727 ZPO angreifbar | Klauselgegenklage § 768 ZPO | Prozessgericht |
| Drittgut wird gepfändet (mein Eigentum) | Drittwiderspruchsklage § 771 ZPO | Prozessgericht |
| Existenzbedrohende Härte (Krankheit, Suizid) | § 765a ZPO Antrag | Vollstreckungsgericht |
| Pfändungsfreigrenze unterschritten | Antrag § 850c, § 850k ZPO | Vollstreckungsgericht |
| Pfändung trotz Restschuldbefreiung | § 767 ZPO + § 301 InsO | Prozessgericht |
| Räumung mit Mitbewohnern ohne Titel | Erinnerung § 766 oder Drittwiderspruch | Vollstreckungs- / Prozessgericht |

## Workflow

1. **Lagebild aufnehmen**: Welcher Titel? Welcher Vollstreckungsschritt? Frist?
2. **Sofortmaßnahmen**: einstweilige Einstellung § 769 ZPO mit Antrag, ggf. einstweilige Verfügung.
3. **Hauptweg wählen** (siehe Tabelle).
4. **Bei P-Konto**: Antrag § 850k Abs. 4 ZPO auf höheren Freibetrag (Unterhaltspflichten, einmalige Sozialleistungen).
5. **Insolvenzaspekte**: Verbraucher kann Insolvenzantrag stellen (sechs Monate Vollstreckungssperre nach Eröffnung § 89 InsO; nicht aber im Eröffnungsverfahren regelmäßig).
6. **Restschuldbefreiung**: § 767 ZPO mit Vorlage des Beschlusses; § 302 InsO prüfen, ob doch Privilegierung.

## Vollstreckungsschutz § 765a ZPO

Sehr hohe Hürde – sittenwidrige Härte. Beispiele aus der Rechtsprechung:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- schwere Erkrankung, kurz bevorstehende Operation
- Hochschwangerschaft
- Tod naher Angehöriger
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Antrag muss vor Vollstreckungsmaßnahme gestellt sein; Aussetzung § 769 ZPO mitbeantragen.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
SCHULDNERABWEHR [Mandant Schuldner], Az [Vollstreckungsgericht]

Vollstreckung: [Art, durch wen, Datum]
Mandantenposition: [Schuldner / Dritter / Eigentümer]
Hauptangriff: [Erinnerung § 766 / Klage § 767 / 768 / 771]
Eilantrag § 769: [ja, mit Begründung ... / nein]
Schutzschirm: [§ 765a / § 850k / § 302 InsO]
Beweismittel: [Zahlungsnachweis, Erlassvertrag, Eigentumsurkunde]
Risiko: [Kostenrisiko, Eilrisiko, Zwangsverkauf]

NÄCHSTER SCHRITT: [Antrag heute einreichen / Klage einreichen]
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals materielle Einwendungen über § 766 ZPO geltend machen – falscher Rechtsbehelf.
- Niemals § 767 ZPO ohne Präklusionsprüfung – Einwendungen müssen nach Schluss der mündlichen Verhandlung entstanden sein.
- Niemals Drittgut über § 766 ZPO verteidigen – das ist § 771 ZPO.
- Bei § 765a ZPO niemals nur Standardvortrag – konkrete Härte mit Beweismitteln.

## Querverweise

- `zv-titel-klausel-zustellung` – Gegenstück Gläubiger
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-tabellenauszug-201-inso` – Restschuldbefreiung
- `zv-raeumung-885`
- `zv-pfaendungstabelle-2025`
