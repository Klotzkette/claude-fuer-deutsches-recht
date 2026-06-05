---
name: rechtsmittelbelehrung-zivil-relation
description: "Rechtsmittelbelehrung Zivil Relation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsmittelbelehrung Zivil Relation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rechtsmittelbelehrung Zivil Relation** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsmittelbelehrung-zivil` | Prüffeld für rechtsmittelbelehrung zivil: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `relation-zivil` | Zivilrechtliche Relation nach klassischer Relationstechnik erstellen: Referendar oder Richter erstellt Entscheidungsunterlage vor Urteilsabfassung. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Streitgegenstand, Zulässigkeitsstation, Schluessigkeitsstation, Klaeger-/Beklagten-/Replikstation, Beweisstation, Tenorierungsstation, Nebenentscheidungen. Output Vollrelation (Schulstandard) oder Kurzfassung (Praxis). Abgrenzung: Vollständige Langfassung siehe vollrelation-langfassung; Familienrichter-Spezifika siehe familienrichter-spezifika. |
| `revisionsfest-pruefen` | Prüfung gegen Aufhebung in der Revision: absolute Revisionsgründe Paragraf 547 ZPO Revisionszulassung Paragraf 543 ZPO grundsaetzliche Bedeutung Rechtsfortbildung Sicherung einheitlicher Rechtsprechung. Begründungstiefe Beweiswürdigung Vollständigkeit Tatsachenfeststellung. Mit BGH-Linien typischen Fallstricken Beispielen aus aktueller Rspr und Selbstprüfliste vor Urteilsversand. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Rechtsmittelbelehrung Zivil Relation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsmittelbelehrung-zivil`

**Fokus:** Prüffeld für rechtsmittelbelehrung zivil: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Rechtsmittelbelehrung Zivil

Paragraf 232 ZPO verlangt eine Rechtsmittelbelehrung bei jeder Entscheidung, gegen die ein selbständiges Rechtsmittel statthaft ist.


## Triage zu Beginn

1. Handelt es sich um ein Endurteil (→ Berufung § 511 ZPO) oder einen Beschluss (→ sofortige Beschwerde § 567 ZPO)?
2. Ist die Beschwer der Berufungsklägerin über 600 EUR (§ 511 Abs. 2 Nr. 1 ZPO)?
3. Hat das Gericht die Berufung zugelassen (§ 511 Abs. 4 ZPO)?
4. Welches Berufungsgericht ist zuständig — LG (bei AG-Urteilen) oder OLG (bei LG-Urteilen)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 232 ZPO — Pflicht zur Rechtsmittelbelehrung
- § 511 ZPO — Berufung (statthaft gegen Endurteile über 600 EUR Beschwer oder bei Zulassung)
- § 517 ZPO — Berufungsfrist (1 Monat nach Zustellung)
- § 520 ZPO — Berufungsbegründungsfrist (2 Monate nach Zustellung)
- § 567 ZPO — sofortige Beschwerde gegen Beschlüsse (Frist 2 Wochen)
- § 78 ZPO — Anwaltszwang vor LG und OLG

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Entscheidungsart bestimmen:** Urteil (→ Berufung) oder Beschluss (→ sofortige Beschwerde)?
2. **Statthaftigkeit prüfen:** Beschwer > 600 EUR oder Berufungszulassung?
3. **Berufungsgericht bestimmen:** AG-Urteil → LG; LG-Urteil → OLG.
4. **Fristen einsetzen:** 1 Monat Einlegung, 2 Monate Begründung — jeweils ab Zustellung.
5. **Standardformel einfügen** (s. unten).

## Output-Template

**Adressat:** Urteil/Beschluss → Rechtsmittelbelehrung — Tonfall: formal-amtlich

```
## Rechtsmittelbelehrung

Gegen dieses Urteil ist die Berufung statthaft.

Die Berufung ist binnen einer Frist von einem Monat nach Zustellung dieses Urteils beim
[Landgericht / Oberlandesgericht] [ORT], [ANSCHRIFT], schriftlich oder zu Protokoll der
Geschäftsstelle einzulegen und binnen einer weiteren Frist von einem Monat nach Zustellung
zu begründen.

Vor dem Berufungsgericht besteht Anwaltszwang.

[Falls keine Berufung statthaft (Beschwer unter 600 EUR, keine Zulassung):]
Gegen dieses Urteil ist ein Rechtsmittel nicht gegeben.
```

## Berufung

Statthaft gegen Endurteile (Paragraf 511 Abs. 1 ZPO). Voraussetzungen:
- Beschwer der Berufungsklägerin / des Berufungsklägers über 600 EUR (Paragraf 511 Abs. 2 Nr. 1 ZPO) ODER
- Zulassung der Berufung durch das erstinstanzliche Gericht (Paragraf 511 Abs. 4 ZPO)

Form und Frist:
- Einlegung binnen einer Frist von einem Monat nach Zustellung des Urteils
- Begründung binnen einer Frist von zwei Monaten nach Zustellung
- Vor dem Berufungsgericht (LG bei AG-Urteilen, OLG bei LG-Urteilen) Anwaltszwang

## Sofortige Beschwerde

Statthaft gegen Beschlüsse (Paragraf 567 ZPO). Voraussetzungen ergeben sich aus der jeweiligen Vorschrift.

Form und Frist:
- Einlegung binnen einer Frist von zwei Wochen nach Zustellung
- Bei dem Gericht, das die Entscheidung erlassen hat, oder beim Beschwerdegericht

## Standardformulierung

"Gegen dieses Urteil ist die Berufung statthaft. Die Berufung ist binnen einer Frist von einem Monat nach Zustellung des Urteils beim Landgericht Hamburg (Sievekingplatz Nummer 1 in 20355 Hamburg) schriftlich oder zu Protokoll der Geschäftsstelle einzulegen und binnen einer Frist von zwei Monaten nach Zustellung schriftlich zu begründen. Vor dem Berufungsgericht besteht Anwaltszwang."


---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

Dieser Skill wurde im Rahmen von Bundle 046 auf halluzinierte Rechtsprechungsnachweise geprüft und korrigiert.

## 2. `relation-zivil`

**Fokus:** Zivilrechtliche Relation nach klassischer Relationstechnik erstellen: Referendar oder Richter erstellt Entscheidungsunterlage vor Urteilsabfassung. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Streitgegenstand, Zulässigkeitsstation, Schluessigkeitsstation, Klaeger-/Beklagten-/Replikstation, Beweisstation, Tenorierungsstation, Nebenentscheidungen. Output Vollrelation (Schulstandard) oder Kurzfassung (Praxis). Abgrenzung: Vollständige Langfassung siehe vollrelation-langfassung; Familienrichter-Spezifika siehe familienrichter-spezifika.

# Relation Zivilprozess - Vollrelation nach deutschem Standard

Methodischer Aufbau der Entscheidungsstruktur vor dem Urteil. Folgt der klassischen Relationstechnik aus der Referendar/-innen-Ausbildung (siehe Anders/Gehle Das Assessorexamen im Zivilrecht; Knoeringer Die Assessorklausur im Zivilprozess; Mahnken Relation in der Praxis).

## WICHTIG - keine Prüfungstaeuschung

**Vorsicht: hiermit bitte nicht mogeln im Studium.** Dieser Skill ist ein Trainings- und Praxiswerkzeug für Referendare/-innen Assessoren/-innen Berufsrichter/-innen und Lehrkraefte. Er darf **nicht** dazu benutzt werden in einer Z- S- V- A-Klausur in einer Hausarbeit in einem Aktenvortrag oder in einer muendlichen Prüfung des juristischen Vorbereitungsdienstes Inhalte als eigene Leistung auszugeben. Das waere ein Taeuschungsversuch im Sinne von Paragraf 14 JAG NRW Paragraf 12 JAPO Bayern und vergleichbarer Vorschriften der anderen Bundesländer; Folge ist regelmäßig Nichtbestehen Aberkennung Disziplinarverfahren. Wer ueben will: erst selbst schreiben dann gegenprüfen lassen.

## Wahlfrage am Anfang - IMMER stellen

Vor Beginn der Relation **immer** fragen:

> Soll ich eine **Vollrelation** im Schulstandard (alle Stationen ausformuliert mit gutachterlichem Stil für Referendar/-innen- und Assessor/-innen-Prüfung) erstellen oder eine **Kurzrelation** im Praxisstandard (Stichworttabelle pro Station wie es Berufsrichter/-innen im Alltag schreiben)?

Wenn die Vollrelation gewuenscht ist dann den Skill `vollrelation-langfassung` zusätzlich laden und nach dessen Schema schreiben.

Unabhängig von der Auswahl muss die Relation **vor** der Urteilsabfassung stehen. Es ist Berufspflicht (siehe Paragraf 313 ZPO und die Prüfungsordnung der Justizprüfungsaemter) den Fall durchgaengig durchgepruegt zu haben bevor das Urteil geschrieben wird.

## Die zehn Stationen der Vollrelation

### 1. Sachbericht

Chronologisch neutral ohne Wertung. Verben im Praesens (Die Klägerin behauptet ...) für streitige Tatsachen im Perfekt (Die Klägerin hat ... geliefert) für Unstreitiges. Reihenfolge: Parteien Vertragsschluss Erfüllung Störung vorgerichtliche Korrespondenz Klaganträge.

### 2. Auslegung des Streitgegenstands

- Welcher Anspruch wird geltend gemacht? (zweigliedriger Streitgegenstandsbegriff: Klagantrag plus zugrundeliegender Lebenssachverhalt)
- Echte oder unechte Klagehaeufung?
- Hilfsantrag Eventualantrag uneigentliche Eventualklage?
- Kläger-Antrag richtig formuliert oder Auslegung nach Paragraf 133 BGB?
- Auslegung des Beklagten-Antrags (in der Regel: die Klage wird abgewiesen)

### 3. Zulässigkeitsstation

| Pruefpunkt | Norm |
|---|---|
| Rechtsweg | Paragraf 13 GVG |
| Internationale Zuständigkeit | EuGVVO Artikel 4 ff oder Artikel 7 Nummer 1 b |
| Örtliche Zuständigkeit | Paragraf 12 ff ZPO |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Streitwert | Paragraf 3 ZPO Paragraf 1 GKG |
| Partei- und Prozessfähigkeit | Paragraf 50 ff ZPO |
| Postulationsfähigkeit | Paragraf 78 ZPO Anwaltszwang |
| Streitgenossenschaft | Paragraf 59 ff ZPO |
| Rechtsschutzbedürfnis | allgemeines Erfordernis |
| Anderweitige Rechtshaengigkeit | Paragraf 261 Absatz 3 Nummer 1 ZPO |

Ergebnis: zulaessig oder nicht.

### 4. Schlüssigkeitsstation - Klägervortrag

Hier wird **ausschließlich der Klägervortrag** unterstellt und gefragt: **Wenn alles wahr ist was die Klägerin sagt ergibt sich aus ihrem Vortrag ein Anspruch?**

Vorgehen:

1. **Anspruchsgrundlage suchen** (Reihenfolge: vertraglich quasivertraglich dinglich deliktisch bereicherungsrechtlich; bei Auslandsbezug Rom-I beziehungsweise CISG vorab).
2. **Tatbestandsmerkmale auflisten** (Wer schuldet was wem woraus warum?).
3. **Subsumtion ausschließlich anhand des Klägervortrags** - keine Erwiderung der Beklagten berücksichtigen keine Streitigkeitsmarkierung.
4. **Rechtsfolge bestimmen** (Erfüllungsanspruch Schadensersatz Rückabwicklung).
5. **Ergebnis**: Schlüssig (Klage ist begründet wenn der Vortrag richtig ist) oder unschlüssig (Klage ist abzuweisen ohne Beweisaufnahme).

Wenn unschlüssig: Hinweis nach Paragraf 139 ZPO erwaegen dann zu Tenorierungsstation. Bei Schlüssigkeit weiter zu Station 5.

### 5. Erheblichkeitsstation - Beklagtenvortrag

Hier wird gefragt: **Hat die Beklagte etwas erheblich vorgetragen das den schlüssigen Klägervortrag erschuettert?**

Drei Kategorien:

- **Einwendungen rechtshindernd** (verhindern Anspruchsentstehung): Geschäftsunfähigkeit Paragraf 105 BGB Anfechtung Paragraf 142 BGB Formmangel Paragraf 125 BGB Sittenwidrigkeit Paragraf 138 BGB.
- **Einwendungen rechtsvernichtend** (zerstören entstandenen Anspruch): Erfüllung Paragraf 362 BGB Aufrechnung Paragraf 389 BGB Erlass Paragraf 397 BGB Rücktritt Paragraf 346 BGB Wandelung Minderung.
- **Einreden durchsetzbarkeitshemmend** (hemmen Durchsetzung): Verjaehrung Paragraf 214 BGB Stundung Zurueckbehaltungsrecht Paragraf 273 BGB Einrede des nicht erfüllten Vertrags Paragraf 320 BGB.

Vorgehen:

1. **Beklagtenvortrag durchgehen** und jede Behauptung klassifizieren (Einwendung Einrede blosses Bestreiten).
2. **Schlüssigkeit der Beklagten-Behauptung prüfen**: Wenn der Vortrag der Beklagten wahr ist würde er den Klägeranspruch hindern vernichten oder hemmen?
3. Wenn ja: Erheblich. Wenn nein: Unerheblich (kein Beweis erforderlich).
4. **Blosses Bestreiten** des Klägervortrags: kein erheblicher Einwand sondern Streitfrage für die Beweisstation.

### 6. Replikstation

Hat die Klägerin auf einen erheblichen Beklagteneinwand etwas erwidert? Beispiele:

- Beklagte beruft sich auf Verjaehrung; Klägerin entgegnet Hemmung nach Paragraf 203 BGB (Verhandlungen).
- Beklagte beruft sich auf Aufrechnung; Klägerin entgegnet Aufrechnungsverbot Paragraf 393 BGB.
- Beklagte beruft sich auf Erfüllung; Klägerin entgegnet Erfüllungsidentitaet nicht gegeben.

Wenn Replik schlüssig dann die Gegen-Replik (Duplik) der Beklagten prüfen und so fort bis ein offener Streitpunkt uebrig bleibt.

### 7. Beweisstation

Nur die nach Station 4 bis 6 noch offenen **streitigen** Tatsachen müssen bewiesen werden.

Für jede streitige Tatsache:

| Element | Inhalt |
|---|---|
| Beweisthema | Was genau ist streitig? |
| Beweisführer | Wer traegt die Beweislast nach den Beweislastregeln (in der Regel die anspruchsbegründende Partei traegt die Beweislast für die Tatbestandsmerkmale ihres Anspruchs die anspruchshemmende Partei für ihre Einwendungen und Einreden) |
| Beweismittel | Zeuge Sachverständiger Urkunde Augenschein Partei (Paragrafen 373 ff ZPO) |
| Beweismass | Paragraf 286 ZPO (volle Überzeugung); Paragraf 287 ZPO (Schadenshöhe und Kausalitaet im Deliktsrecht: überwiegende Wahrscheinlichkeit) |
| Beweisanträge gestellt? | von wem in welchem Schriftsatz |
| Beweisbeschluss erforderlich? | Paragraf 358 ZPO |

Wenn keine Beweisaufnahme noetig (weil entweder unstreitig oder unerheblich) direkt zu Tenorierungsstation.

### 8. Tenorierungsstation

Formuliere den Tenor so **als ob das Beweisergebnis bekannt waere** (vorbereitend). Drei Varianten durchspielen:

- **Variante A** Klage in vollem Umfang begründet
- **Variante B** Klage teilweise begründet (Quoten errechnen)
- **Variante C** Klage in vollem Umfang unbegründet

Für jede Variante: Hauptsache-Tenor Kosten vorläufige Vollstreckbarkeit.

### 9. Nebenentscheidungen

- Kosten: Paragraf 91 ZPO (Grundregel) Paragraf 92 ZPO (teilweises Obsiegen) Paragraf 93 ZPO (sofortiges Anerkenntnis) Paragraf 269 ZPO (Klageruecknahme)
- Vorläufige Vollstreckbarkeit: Paragraf 708 Nummer 11 ZPO (Bagatelltitel bis 1500 EUR) oder Paragraf 709 ZPO (sonst) in Verbindung mit Paragraf 711 ZPO
- Streitwert: Paragraf 63 GKG
- Zinsen: Paragraf 286 BGB Paragraf 288 BGB Artikel 78 CISG
- Rechtsmittelzulassung: Paragraf 511 Absatz 4 ZPO (bei Streitwert unter 600 EUR oder bei Grundsatzbedeutung)

### 10. Selbstkontrolle

- **Berufungsfest?** Sind alle entscheidungserheblichen Tatsachen in den Tatbestand aufgenommen? Sind alle Ansprueche beschieden? Wurden Hinweise nach Paragraf 139 ZPO erteilt wenn der Vortrag der Parteien laeckenhaft war?
- **Revisionsfest?** Wurde abstraktes Recht angewandt oder eine grundsaetzliche Frage entschieden? Dann Zulassung der Revision durch das Berufungsgericht thematisieren.

## Ergebnisausgabe

Die Relation muss am Ende eindeutig sagen:

1. Die Klage ist **zulaessig** (oder nicht).
2. Die Klage ist **schlüssig** (oder nicht).
3. Die Beklagte hat **erhebliche Einwendungen** vorgetragen (oder nicht).
4. Streitig und beweisbedürftig sind: ...
5. Tenor-Vorschlag für die wahrscheinliche Variante: ...

## 3. `revisionsfest-pruefen`

**Fokus:** Prüfung gegen Aufhebung in der Revision: absolute Revisionsgründe Paragraf 547 ZPO Revisionszulassung Paragraf 543 ZPO grundsaetzliche Bedeutung Rechtsfortbildung Sicherung einheitlicher Rechtsprechung. Begründungstiefe Beweiswürdigung Vollständigkeit Tatsachenfeststellung. Mit BGH-Linien typischen Fallstricken Beispielen aus aktueller Rspr und Selbstprüfliste vor Urteilsversand.

# Revisionsfestigkeit prüfen

## Zweck

Bei LG- und OLG-Endurteilen, gegen die Revision möglich ist (Paragraf 542 ZPO), muss das Urteil so geschrieben sein, dass es einer Prüfung durch den BGH standhaelt. "Revisionsfest" ist das Urteil, wenn es weder einen absoluten Revisionsgrund (Paragraf 547 ZPO) noch eine Verletzung von materiellem oder Verfahrensrecht im Sinne der Paragrafen 545, 546 ZPO erkennen laesst, das die Aufhebung tragen koennte.

Dieser Skill liefert die Selbstprüfung **vor** Verkündung — nicht erst, wenn die Revisionsbegründung schon vorliegt.

## 1) Absolute Revisionsgründe Paragraf 547 ZPO

Der Klassiker — bei diesen Gründen ist die Aufhebung zwingend, ohne dass es auf Kausalitaet ankommt:

1. **Nicht vorschriftsmaessige Besetzung** des Gerichts (Nr. 1)
 - Geschäftsverteilungsplan eingehalten?
 - Bei Einzelrichter: Übertragung Paragraf 348a ZPO begründet?
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Mitwirkung eines ausgeschlossenen Richters** (Nr. 2)
 - Selbst-Ausschluss Paragraf 41 ZPO geprüft (Verwandtschaft, Voreintragung)
3. **Mitwirkung eines mit Erfolg abgelehnten Richters** (Nr. 3)
4. **Verletzung der OEffentlichkeit** Paragrafen 169 ff. GVG (Nr. 4)
 - OEffentlichkeitsausschluss richtig begründet?
5. **Vertretungsmangel** Paragraf 51, 56 ZPO (Nr. 5)
 - Prozessunfähiger ohne gesetzlichen Vertreter?
6. **Begründungsmangel** (Nr. 6) — **der haeufigste Fall**:
 - Keine Entscheidungsgründe überhaupt
 - Gründe lassen die wesentliche Erwaegung nicht erkennen
 - Widerspruch zwischen Tatbestand und Gründen
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2) Verfahrensrecht — Paragraf 545 ZPO

### Haeufige Fehler

| Fehler | Verbotsnorm | Vermeidung |
|---|---|---|
| Verfahrensfehler bei Beweisaufnahme | Paragraf 286 ZPO | Beweiswürdigung vollständig, jeder Beweis behandelt |
| Verletzung rechtliches Gehoer | Art. 103 GG, Paragraf 139 ZPO | Hinweise erteilt, vor Urteilsspruch Gelegenheit zur Stellungnahme |
| Präklusion verkannt | Paragraf 296 ZPO | Bei Zurueckweisung verspaeteten Vortrags konkrete Begründung |
| Überraschungsentscheidung | Paragraf 139 II ZPO | Bei tragenden Erwaegungen, mit denen Partei nicht rechnen musste, Hinweis erteilt |

### Beweiswürdigung Paragraf 286 ZPO

Die Beweiswürdigung muss erkennen lassen:
- **welche** Beweise erhoben wurden
- **welches Ergebnis** sie hatten
- **wie** das Gericht zur Überzeugung gelangt ist
- **warum** Gegenbeweise nicht durchgreifen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3) Materielles Recht — Paragraf 546 ZPO

### Prüfen

- Sind die **Anspruchsgrundlagen** vollständig abgearbeitet (V-C-G-D-D-B)?
- Bei mehreren Anspruchsgrundlagen: jeweils Tatbestandsmerkmale und Rechtsfolgen geprüft?
- Bei Streit zwischen Theorien: **eigene Stellungnahme** mit Begründung?
- Wird **einschlaegige BGH-Rspr.** zitiert oder begründet abgewichen?
- Wird einschlaegige BVerfG-Rspr. (insbesondere zu Art. 103 GG) berücksichtigt?
- Wird ggf. EuGH-Rspr. zur Auslegung von EU-Recht berücksichtigt?

### Bei Abweichung von der h.M.

Pflichtargumentation:
1. Warum die h.M. nicht überzeugt
2. Welche bessere Begründung die abweichende Auffassung hat
3. Welche Konsequenz für den Fall folgt

## 4) Tatsachenfeststellung — Paragraf 559 ZPO

Der BGH ist an die festgestellten Tatsachen gebunden, soweit nicht
- begründete Verfahrensruegen erhoben sind, oder
- die Tatsachenfeststellung widerspruechlich, unvollständig oder denkgesetzwidrig ist.

### Vermeiden

- **Lücken im Tatbestand.** Was nicht festgestellt ist, kann der BGH nicht annehmen.
- **Widerspruch Tatbestand <-> Gründe.** Wenn der Tatbestand "A war anwesend" sagt, kann die Beweiswürdigung nicht "A war nicht anwesend" feststellen.
- **Pauschale Tatsachen.** "Der Kläger wurde haeufig provoziert" ist keine Tatsachenfeststellung, sondern eine Wertung.

## 5) Revisionszulassung — Paragraf 543 ZPO

### Zulassungsgründe (alle gleichberechtigt)

1. **Grundsaetzliche Bedeutung** (Abs. 2 S. 1 Nr. 1)
 - Eine bislang ungeklärte oder unterschiedlich beantwortete Rechtsfrage
 - In einer unbestimmten Zahl von Fällen auftretend
2. **Rechtsfortbildung** (Abs. 2 S. 1 Nr. 2)
 - Bedürfnis nach richterlicher Leitsatzbildung
3. **Sicherung einheitlicher Rechtsprechung** (Abs. 2 S. 1 Nr. 2 Alt. 2)
 - Abweichende OLG-Rspr. zu derselben Rechtsfrage
 - Eigene Abweichung vom BGH-Linie

### Tenorierung

```
Die Revision wird zugelassen.
```

mit Begründung in den Entscheidungsgründen — z.B.:

```
Die Revision wird zugelassen, weil die Frage,
ob [...], in der obergerichtlichen Rechtsprechung
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
... und OLG ..., NJW-RR 2023, ...), und damit die
Sicherung einer einheitlichen Rechtsprechung im Sinne des
Paragraf 543 II Nr. 2 Alt. 2 ZPO eine Entscheidung
des Revisionsgerichts erfordert.
```

### Nicht zugelassen — Nichtzulassungsbeschwerde

Wenn die Revision nicht zugelassen ist, ist nach Paragraf 544 ZPO Nichtzulassungsbeschwerde gegeben. Die NZB ist die zweite Hauptfalle: Begründungsmangel und Verletzung Art. 103 GG sind die haeufigsten Erfolgsgründe.

## 6) Aktuelle BGH-Linien zu typischen Fallen

### Begründungsmangel
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Rechtliches Gehoer
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Beweiswürdigung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 7) Selbstpruefliste vor Urteilsversand

### Form
- [ ] Rubrum vollständig (Aktenzeichen, Parteien, Anwälte, Streitwert)
- [ ] Tenor aus sich heraus vollstreckbar
- [ ] Tatbestand und Entscheidungsgründe formal getrennt
- [ ] Unterschriften vollständig (bei Verhinderung Vermerk Paragraf 315 ZPO)

### Tatbestand
- [ ] Unstreitige Tatsachen erkennbar
- [ ] Streitige Tatsachen erkennbar (klägerischer und beklagter Vortrag)
- [ ] Vortrag durch Aktenbezugnahme (Paragraf 313 II 2 ZPO) ggf. zulaessig?
- [ ] Anträge wortlautgetreu (auch Hilfsanträge)

### Entscheidungsgründe
- [ ] Anspruchsgrundlagen vollständig (V-C-G-D-D-B)?
- [ ] Bei jeder Anspruchsgrundlage Tatbestandsmerkmale geprüft?
- [ ] Beweiswürdigung erkennbar und vollständig?
- [ ] Streit-Stand mit eigener Stellungnahme bei kritischen Punkten?
- [ ] BGH-Rspr. zitiert oder begründet abgewichen?
- [ ] Bei Klageabweisung: alle in Betracht kommenden Anspruchsgrundlagen behandelt?

### Verfahren
- [ ] Hinweispflichten Paragraf 139 ZPO erfüllt?
- [ ] Präklusion (Paragraf 296 ZPO) korrekt geprüft, falls Verspätung?
- [ ] Schluss der muendlichen Verhandlung (Paragraf 296a ZPO) eingehalten?
- [ ] Keine Überraschungsentscheidung?

### Zulassung
- [ ] Revisionszulassung Paragraf 543 ZPO erwogen?
- [ ] Falls zugelassen: Begründung im Entscheidungsteil?
- [ ] Falls nicht zugelassen: Konsistenz mit der bestehenden BGH-Linie geprüft?

### Vollstreckbarkeit
- [ ] Vorläufige Vollstreckbarkeit Paragraf 708-711 ZPO?
- [ ] Sicherheitsleistung-Höhe begründet?

## 8) Schnittstelle zu weiteren Skills

- `tatbestand-zivil-schreiben` — vollständig und widerspruchsfrei
- `tenor-bauen-zivil` — vollstreckbar
- `vorlaeufige-vollstreckbarkeit` — Paragraf 708 ff. ZPO
- `relation-zivil` — Gesamtaufbau

## Anschluss

- Wenn revisionsfest: `dokumente-rendern-urteil-docx` zum finalen DOCX-/PDF-Export
- Wenn nicht: zurueck zum mangelhaften Skill (`tatbestand-zivil-schreiben`, `entscheidungsgruende-zivil-schreiben`, `beweiswuerdigung-mit-richter-input` oder `anspruchsgrundlagen-pruefen`, je nach Mangel)
