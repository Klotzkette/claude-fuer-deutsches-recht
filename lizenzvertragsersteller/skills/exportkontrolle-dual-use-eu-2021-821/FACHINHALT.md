---
name: exportkontrolle-dual-use-eu-2021-821
description: "Für Exportkontrolle — Dual-Use und Lizenz: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck."
---

# Exportkontrolle — Dual-Use und Lizenz

## Normenanker

- VO (EU) 2021/821 - Dual-Use-Verordnung (loest VO 428/2009 ab)
- AWG (Aussenwirtschaftsgesetz) - nationale Umsetzung
- AWV (Aussenwirtschaftsverordnung) - Verordnung
- VO (EU) 833/2014 + Folgeverordnungen - Russland-Sanktionen
- VO (EU) 765/2006 - Belarus-Sanktionen
- US-EAR (Export Administration Regulations) - bei US-Touch (Re-Export)
- ITAR (US-Militaergueterregeln)

## Was loest Exportkontrollpflicht aus?

| Tatbestand | Folge |
|---|---|
| **Tatsaechliche koerperliche Ausfuhr** des Lizenzgegenstands | klassischer Export, AWV-Genehmigung |
| **Elektronische Uebermittlung** Source Code, Daten | gilt als Ausfuhr |
| **Sicherheitstechnologie** auf Dual-Use-Anhang I VO 2021/821 | genehmigungspflichtig |
| **Sanctioned Country** (Russland, Belarus, Iran, Nordkorea) | Verbot oder umfangreiche Genehmigungspflicht |
| **Sanktionierte Person** (EU-Listen, OFAC) | Verbot |
| **Cloud-Lizenz** mit Zugriff auf Server in sanctioned country | Prüfen |

## Dual-Use-Anhang I (Stichworte)

- **Kategorie 0:** Nukleare Materialien
- **Kategorie 1:** Werkstoffe, Chemikalien, biologische Mittel
- **Kategorie 3:** Elektronik
- **Kategorie 4:** Computer + Software
- **Kategorie 5 Teil 1:** Telekommunikation
- **Kategorie 5 Teil 2:** Informationssicherheit (Kryptografie!) - haeufigster Trigger für Lizenz
- **Kategorie 9:** Luft- und Raumfahrt

→ Software/Quellcode mit Krypto-Funktionen, KI-Modelle mit dual-use-Anwendung, Datenanalyse-Tools für Ueberwachung: regelmaessig erfasst.

## Klausel-Bausteine

**A. Export-Compliance allgemein:**
> "Paragraf 17 Exportkontrolle.
> (1) Die Parteien beachten saemtliche anwendbaren exportkontrollrechtlichen Vorschriften, insbesondere die VO (EU) 2021/821 (Dual-Use), das AWG/AWV, die jeweiligen EU-Sanktionsverordnungen sowie - soweit anwendbar - das US-EAR und ITAR.
> (2) Der Lizenznehmer wird den Lizenzgegenstand und etwaige darin enthaltene Technologie nicht in Sanctioned Countries oder an Sanctioned Persons exportieren, weitergeben, lizenzieren oder bereitstellen."

**B. Genehmigungsvorbehalt:**
> "(3) Falls für den Lizenzgegenstand eine Ausfuhrgenehmigung erforderlich ist, wird der Lizenzgeber den Lizenznehmer hierueber informieren. Die Lizenz tritt erst mit Erteilung der erforderlichen Genehmigungen in Kraft. Vorab können Vorbereitungshandlungen erfolgen."

**C. Sanctioned Persons:**
> "(4) Die Parteien sichern zu, dass weder sie selbst noch ihre Konzernunternehmen, Anteilseigner oder Mitarbeiter auf Sanktionslisten der EU, der USA oder der Vereinten Nationen gefuehrt werden. Bei Aufnahme auf eine Sanktionsliste ist die jeweils andere Partei zur sofortigen Vertragsbeendigung berechtigt."

**D. Cloud-/Cross-Border-Klausel:**
> "(5) Der Lizenznehmer wird den Lizenzgegenstand nicht über Server in Sanctioned Countries betreiben, hosten oder verarbeiten."

## Praktische Prüfung

```
1. Pruefe Anhang I Dual-Use-VO: ist Lizenzgegenstand erfasst?
2. Pruefe Empfaengerstandort: Sanktionsland?
3. Pruefe Empfaengerperson: auf Sanktionsliste?
4. Pruefe Endverbleib: Ist Re-Export wahrscheinlich?
5. Bei US-Touch: pruefe US-EAR / ITAR.
6. Genehmigung bei BAFA beantragen, falls erforderlich.
```

## Anschluss

- Datenschutz: `datenschutz-dsgvo-im-lizenzvertrag`
- Sanktionen sind Compliance-Querschnitt; siehe `aussenwirtschaft-zoll-sanktionen`-Plugin im Repo
