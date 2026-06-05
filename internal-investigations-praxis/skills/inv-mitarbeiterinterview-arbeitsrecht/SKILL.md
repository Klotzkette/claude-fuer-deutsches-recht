---
name: inv-mitarbeiterinterview-arbeitsrecht
description: "Inv 004 Mitarbeiterinterview, Inv 005 Arbeitsrecht Mitwirkung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 004 Mitarbeiterinterview, Inv 005 Arbeitsrecht Mitwirkung

## Arbeitsbereich

Dieser Skill bündelt **Inv 004 Mitarbeiterinterview, Inv 005 Arbeitsrecht Mitwirkung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-004-mitarbeiterinterview` | Leitet Mitarbeiterinterviews in Internal Investigations rechtskonform durch – Belehrung, Protokoll, Verwertbarkeit, Schweigerecht. |
| `inv-005-arbeitsrecht-mitwirkung` | Klärt arbeitsrechtliche Mitwirkungspflichten, Auskunftspflichten und Grenzen bei Mitarbeiterbefragungen in Internal Investigations. |

## Arbeitsweg

Für **Inv 004 Mitarbeiterinterview, Inv 005 Arbeitsrecht Mitwirkung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-004-mitarbeiterinterview`

**Fokus:** Leitet Mitarbeiterinterviews in Internal Investigations rechtskonform durch – Belehrung, Protokoll, Verwertbarkeit, Schweigerecht.

# Mitarbeiterinterviews

## Rechtlicher Rahmen

Mitarbeiterinterviews im Rahmen von Internal Investigations bewegen sich im Spannungsfeld zwischen arbeitsrechtlicher Mitwirkungspflicht, strafprozessualen Schweigerechten und datenschutzrechtlichen Anforderungen. Grundlegend ist die Unterscheidung zwischen dem Mitarbeiter als **Zeuge** (Mitwirkungspflicht aus dem Arbeitsvertrag, §§ 242, 611a BGB) und als **Beschuldigtem** (Schweigerecht analog §§ 136, 163a StPO, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__136.html)). Die Verwertbarkeit von Interviewaussagen in einem späteren Strafverfahren hängt maßgeblich von der ordnungsgemäßen Belehrung ab. Die BGH-Linie zu „Siemens/Neubürger" (BGH II ZR 234/09, [openjur.de](https://openjur.de/o/577696.html)) setzt voraus, dass Aufklärungsmaßnahmen tatsächlich effektiv sind – das verlangt auch sachgerecht geführte Interviews.

## Ziel dieses Skills

Dieser Skill strukturiert die Vorbereitung, Durchführung und Nachbereitung von Mitarbeiterinterviews so, dass Aussagen verwertbar sind, Fehler bei der Belehrung keine Verfahrenshindernisse schaffen und der Interviewte weiß, in welcher Rolle er spricht.

## Arbeitsprogramm

### 1. Rollendefinition vor dem Interview
- Ist der Interviewte **Zeuge**, **Betroffener** oder **Beschuldigter**?
- Unterschied: Zeuge hat Mitwirkungspflicht aus dem Arbeitsvertrag; Beschuldigter kann die Aussage verweigern (nemo tenetur se ipsum accusare).
- Rollenwechsel während des Interviews dokumentieren und Interview ggf. unterbrechen.

### 2. Belehrung des Mitarbeiters
- **Zeugen**: Hinweis auf arbeitsrechtliche Mitwirkungspflicht, kein allgemeines Schweigerecht, aber Zeugnisverweigerungsrecht bei selbstbelastenden Aussagen (analog § 55 StPO, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__55.html)).
- **Betroffene/Beschuldigte**: Belehrung über Schweigerecht, Recht auf Hinzuziehung eines eigenen Anwalts (§ 136 StPO analog), Hinweis auf mögliche strafrechtliche Relevanz.
- **Upjohn-Warnung** (US-Praxis): Klarstellen, dass der ermittelnde Anwalt das Unternehmen, nicht den Mitarbeiter, vertritt; der Mitarbeiter sollte einen eigenen Anwalt hinzuziehen.
- Belehrungstext schriftlich festhalten und von Interviewtem unterzeichnen lassen.

### 3. Betriebsratsbeteiligung
- § 82 Abs. 2 BetrVG: Arbeitnehmer kann Betriebsratsmitglied als Beistand hinzuziehen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__82.html)).
- § 87 Abs. 1 Nr. 1 BetrVG: Mitbestimmung bei Ordnungsmaßnahmen; gilt das Interview als Vorstufe zu einer Abmahnung oder Kündigung?
- Betriebsrat darf nicht zum Kronzeugen gegen eigene Mitglieder gemacht werden.

### 4. Interviewvorbereitung
- Faktenanalyse: Welche Dokumente, E-Mails, Transaktionen wurden bereits forensisch gesichert?
- Hypothesenkatalog: Welche Versionen des Sachverhalts sind möglich?
- Fragenkatalog: offen → geschlossen → konfrontativ (sog. PEACE-Methode oder Reid-Kritik beachten).
- Keine Vorhaltungen ohne Dokumentengrundlage – jede Konfrontation muss belegbar sein.

### 5. Durchführung
- Zwei Interviewer (Fragender + Protokollant), kein Einzelinterview.
- Keine Tonaufnahme ohne informierte Einwilligung (§ 201 StGB, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__201.html)); schriftliches Protokoll ist Standard.
- Zeitstempel, Ort, Anwesende, Rollendefinition im Protokoll festhalten.
- Pausen dokumentieren; Druckausübung oder Täuschung vermeiden (Verwertungsverbot!).

### 6. Protokoll und Freigabe
- Zusammenfassung vs. wörtliches Protokoll: Letzteres für Schlüsselpersonen empfohlen.
- Interviewter erhält Gelegenheit zur Korrektur (Gegendarstellung); keine Pflicht zur Unterschrift.
- Privilegiertes Dokument: Protokoll unter Anwaltsgeheimnis halten.
- DSGVO: Interviewprotokoll ist personenbezogenes Datum; Zugangsbeschränkung und Löschplan festlegen.

### 7. Verwertbarkeit und Beweisverwertungsverbote
- Aussage unter Drohung (Kündigung) erzwungen → Beweisverwertungsverbot in Strafverfahren (BGH-Grundsatz; vgl. BGH, Urt. v. 3.5.2018 – 3 StR 390/17, [bgh.de](https://www.bgh.de/)).
- Keine unmittelbare Weitergabe von Interviewprotokollen an Staatsanwaltschaft ohne Prüfung der eigenen Interessen.
- § 161a StPO: Zeugenpflicht gegenüber Staatsanwaltschaft; Arbeitgeber kann Mitarbeiter nicht anweisen, gegenüber Staatsanwalt zu schweigen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__161a.html)).

## Red-Team-Fragen

- Wurde die Rolle des Interviewten klar definiert und dokumentiert – vor Beginn des Gesprächs?
- Hat der betroffene Mitarbeiter Gelegenheit gehabt, einen eigenen Anwalt hinzuzuziehen?
- Enthält das Protokoll Formulierungen, die in einem Strafverfahren als erzwungenes Geständnis gewertet werden könnten?
- Wurde der Betriebsrat über die Interviewserie informiert, und hat er Mitbestimmungsrechte geltend gemacht?
- Ist das Protokoll unter Anwaltsgeheimnis gehalten, und wurde der Verteiler auf Need-to-know beschränkt?
- Wurden alle Interviewten gleich behandelt, oder entsteht ein Selektionsverdacht?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 136 StPO | Belehrung Beschuldigter | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__136.html) |
| § 55 StPO | Auskunftsverweigerungsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__55.html) |
| § 161a StPO | Zeugenpflicht gegenüber StA | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__161a.html) |
| § 82 BetrVG | Recht auf Betriebsratsbeistand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__82.html) |
| § 201 StGB | Verletzung der Vertraulichkeit | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__201.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |

## Ausgabeformate

- **Belehrungsvorlage** (Zeuge / Betroffener / Beschuldigter)
- **Interviewleitfaden** mit Fragenkatalog (offen → konfrontativ)
- **Protokollvorlage** (Zeitstempel, Anwesende, Rollenklarstellung)
- **Upjohn-Warnung** (Mustertext Englisch/Deutsch)
- **Beweisverwertungsanalyse** für vorliegende Protokolle

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-005-arbeitsrecht-mitwirkung`

**Fokus:** Klärt arbeitsrechtliche Mitwirkungspflichten, Auskunftspflichten und Grenzen bei Mitarbeiterbefragungen in Internal Investigations.

# Arbeitsrechtliche Mitwirkungspflichten

## Rechtlicher Rahmen

Die arbeitsrechtliche Mitwirkungspflicht des Arbeitnehmers ergibt sich aus §§ 242, 241 Abs. 2 BGB (Nebenpflicht aus dem Arbeitsverhältnis, Treuepflicht) sowie aus § 666 BGB analog (Auskunfts- und Rechenschaftspflicht), soweit der Mitarbeiter mit fremden Mitteln umgegangen ist ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__242.html)). Das BAG hat mehrfach bestätigt, dass Arbeitnehmer im Rahmen des Arbeitsverhältnisses verpflichtet sind, wahrheitsgemäß Auskunft über ihre Tätigkeit zu erteilen (BAG, Urt. v. 7.9.1995 – 8 AZR 828/93). Diese Pflicht findet ihre Grenze dort, wo Aussagen zur eigenen Strafverfolgung führen würden (nemo tenetur se ipsum accusare), was das BVerfG als verfassungsrechtlich geschützten Grundsatz anerkannt hat.

## Ziel dieses Skills

Dieser Skill klärt, welche Mitwirkungspflichten Mitarbeiter haben, wie weit diese reichen und wo sie enden – insbesondere bei drohender Selbstbelastung, Zeugnisverweigerungsrechten und der Kollision mit strafprozessualen Rechten.

## Arbeitsprogramm

### 1. Grundlage der Mitwirkungspflicht
- § 242 BGB: allgemeine Treuepflicht aus dem Arbeitsverhältnis.
- § 666 BGB: Auskunftspflicht für Tätigkeiten, die der Mitarbeiter für den Arbeitgeber ausgeführt hat.
- § 611a BGB i. V. m. Arbeitsvertrag: Pflicht zur Unterstützung bei betriebsinternen Untersuchungen, soweit dies zumutbar ist.
- Grenzen: Verhältnismäßigkeit, Zumutbarkeit, Selbstbelastungsfreiheit.

### 2. Grenzen der Mitwirkungspflicht: Nemo tenetur
- Drohende strafrechtliche Selbstbelastung: Mitarbeiter muss keine Aussagen machen, die zur eigenen Strafverfolgung führen könnten (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG; § 55 StPO analog, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__55.html)).
- Stufenlösung: Auskunftspflicht besteht, aber Auskunft darf in Strafverfahren nicht verwendet werden (§ 97 InsO als Parallelwertung).
- Praktische Konsequenz: Arbeitgeber kann Aussage verlangen, aber Mitarbeiter darf „Fünfte nehmen" (Fifth Amendment-Analogie).

### 3. Belehrungspflichten des Arbeitgebers / Ermittlers
- Vor dem Interview muss klar sein, ob der Mitarbeiter als Zeuge oder als Betroffener befragt wird.
- Fehlende oder falsche Belehrung kann zur Unverwertbarkeit der Aussage führen (Beweisverwertungsverbot).
- Bei gleichzeitiger Drohung mit arbeitsrechtlichen Konsequenzen: Aussage unter Zwang, ggf. strafrechtlich unverwertbar.
- BAG, Urt. v. 23.10.2008 – 2 AZR 483/07: Kündigung wegen Aussageverweigerung kann unverhältnismäßig sein, wenn berechtigte Selbstbelastungsgefahr besteht.

### 4. Zeugnisverweigerungsrechte
- § 383 ZPO: Zeugnisverweigerung wegen Angehörigeneigenschaft ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__383.html)) – für interne Interviews nur mittelbar relevant.
- § 53 StPO: Zeugnisverweigerungsrecht von Berufsgeheimnisträgern (Anwalt, Arzt, Steuerberater) – relevant, wenn Dritte hinzugezogen werden ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__53.html)).
- § 53 ZPO: Zeugnisverweigerung wegen Selbstbelastungsgefahr (in Zivilverfahren; [gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__384.html)).

### 5. Sanktionsrisiken bei Verweigerung
- Abmahnung und Kündigung bei grundloser Verweigerung der Mitwirkung.
- Außerordentliche Kündigung bei Verdacht auf schwerwiegende Straftaten, auch ohne vollständige Sachverhaltsaufklärung (BAG-Rechtsprechung zur Verdachtskündigung, z. B. BAG, Urt. v. 21.11.2013 – 2 AZR 797/11, [openjur.de](https://openjur.de/o/750010.html)).
- Warnung: Kündigung aufgrund von Aussageverweigerung bei berechtigter Selbstbelastungsgefahr ist angreifbar.

### 6. Kollision mit § 203 StGB (Schweigepflicht)
- Mitarbeiter mit beruflicher Schweigepflicht (z. B. Arzt im Unternehmen, Bankmitarbeiter) können sich auf § 203 StGB berufen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html)).
- Abwägung: Schweigepflicht gegenüber Dritten vs. Auskunftspflicht gegenüber Arbeitgeber.
- In der Regel überwiegt die Auskunftspflicht, wenn es um eigene Handlungen im Arbeitsverhältnis geht.

### 7. Besondere Konstellation: Leitungspersonen
- § 130 OWiG: Leitungspersonen haben eigene Aufsichtspflicht; Mitwirkung an der Aufklärung kann Bußgeldrisiko mindern ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html)).
- BGH II ZR 234/09 (Siemens/Neubürger): Vorstandsmitglied hat persönliche Aufklärungspflicht ([openjur.de](https://openjur.de/o/577696.html)).

## Red-Team-Fragen

- Wurde dem Mitarbeiter vor dem Interview klar kommuniziert, ob er als Zeuge oder Betroffener gilt?
- Wurde er über das nemo-tenetur-Prinzip belehrt – schriftlich und nachweisbar?
- Ist die Kündigung bei Verweigerung der Aussage verhältnismäßig, wenn berechtigte Selbstbelastungsgefahr vorliegt?
- Haben Mitarbeiter mit Berufsgeheimnis (§ 203 StGB) auf ihre Schweigepflicht hingewiesen?
- Wurde zwischen echter Mitwirkungsverweigerung und berechtigtem Schweigen unterschieden?
- Ist die Dokumentation der Belehrungen vollständig und gerichtsfest?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 242 BGB | Treuepflicht, Mitwirkungspflicht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__242.html) |
| § 55 StPO | Auskunftsverweigerungsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__55.html) |
| § 53 StPO | Zeugnisverweigerungsrecht Berufsgeheimnisträger | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__53.html) |
| § 203 StGB | Verletzung von Privatgeheimnissen | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |

## Ausgabeformate

- **Mitwirkungspflicht-Analyse** für konkrete Mitarbeitersituation
- **Belehrungsvorlage** (Zeugen / Betroffene / Leitungspersonen)
- **Sanktionsmatrix** (Verweigerungsszenarien × Konsequenzen)
- **Stellungnahme** zur Zulässigkeit einer Verdachtskündigung nach Aussageverweigerung

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
