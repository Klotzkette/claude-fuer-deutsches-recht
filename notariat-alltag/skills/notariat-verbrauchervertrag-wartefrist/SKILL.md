---
name: notariat-verbrauchervertrag-wartefrist
description: "Verbrauchervertrag Wartefrist: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verbrauchervertrag Wartefrist

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verbrauchervertrag Wartefrist** im Plugin Notariat Alltag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notariat-026-verbrauchervertrag-wartefrist-und-entwurfsversand` | Notariat im Alltag: Verbrauchervertrag, Wartefrist und Entwurfsversand. § 17 Abs. 2a BeurkG, Anwendungsbereich, Fristberechnung, Dokumentation und Rechtsfolgen bei Verstößen. |
| `notariat-035-aufgebotsverfahren-verlorener-grundschuldbrief` | Notariat im Alltag: Aufgebotsverfahren – verlorener Grundschuldbrief. Verfahren nach §§ 1162–1163 BGB i.V.m. FamFG, Antrag beim Amtsgericht, Bekanntmachungspflichten und Kraftloserklärung. |
| `notariat-039-fristenkalender-vollzugsmonitor-wiedervorlage-eskal` | Notariat im Alltag: Fristenkalender, Vollzugsmonitor, Wiedervorlage und Eskalation. Systematisches Fristenmanagement im Notariat, Wiedervorlagepflichten und Eskalationsregeln bei drohenden Vollzugsblockaden. |

## Arbeitsweg

Im Plugin Notariat Alltag gilt für **Verbrauchervertrag Wartefrist**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `notariat-026-verbrauchervertrag-wartefrist-und-entwurfsversand`

**Fokus:** Notariat im Alltag: Verbrauchervertrag, Wartefrist und Entwurfsversand. § 17 Abs. 2a BeurkG, Anwendungsbereich, Fristberechnung, Dokumentation und Rechtsfolgen bei Verstößen.

# Notariat im Alltag: Verbrauchervertrag, Wartefrist und Entwurfsversand

## Zweck und Anwendungsbereich

Die Verbraucherwartefrist (§ 17 Abs. 2a BeurkG) schützt Verbraucher bei Immobiliengeschäften vor übereilten Entscheidungen. Dieser Skill klärt Anwendungsbereich, Fristberechnung, Entwurfsversandpflicht, Ausnahmen und Haftungsfolgen.

Rechtsgrundlagen: § 17 Abs. 2a BeurkG (Verbraucherwartefrist), § 13 BGB (Verbraucher), § 14 BGB (Unternehmer), § 17 BeurkG (allgemeine Belehrungspflicht), § 19 BNotO (Notarhaftung), BGH-Rechtsprechung zu § 17 Abs. 2a BeurkG.

## Anwendungsbereich (§ 17 Abs. 2a BeurkG)

Die Wartefrist gilt bei Beurkundungen von **Verbraucherverträgen über Grundstücke** (§ 311b BGB), wenn:
- eine Vertragspartei Verbraucher (§ 13 BGB) ist, und
- die andere Vertragspartei Unternehmer (§ 14 BGB) ist.

**Verbraucher:** Natürliche Person, die das Geschäft nicht überwiegend gewerblich oder selbständig beruflich tätigt.
**Unternehmer:** Natürliche oder juristische Person, die in Ausübung ihrer gewerblichen oder selbständigen beruflichen Tätigkeit handelt.

**Kein Anwendungsfall:**
- Beide Parteien Verbraucher (str., aber h.M.: keine Wartefrist)
- Reine Unternehmergeschäfte
- Nicht-Grundstücksgeschäfte (GmbH-Gründung, Erbvertrag)

## Fristdauer und Berechnung

Mindestens **14 Tage** zwischen Entwurfsversand und Beurkundungstermin (§ 17 Abs. 2a S. 1 BeurkG). Berechnung nach §§ 187 ff. BGB:
- Tag des Entwurfsversands: Frist beginnt am Folgetag (§ 187 Abs. 1 BGB)
- Frist endet am letzten Tag um 24 Uhr (§ 188 Abs. 2 BGB)
- Beurkundungstermin: frühestens am Tag nach Fristablauf

Beispiel: Entwurfsversand 1. März → Fristbeginn 2. März → Fristende 15. März → frühestmöglicher Termin: 16. März.

## Entwurfsversand

Der Entwurf muss an den Verbraucher übermittelt werden:
- In Textform (§ 126b BGB): E-Mail, Fax, Post
- Empfang beim Verbraucher: Im Zweifel trägt der Notar das Nachweisrisiko
- Empfehlung: E-Mail mit Lesebestätigung oder Einschreiben mit Rückschein
- Inhalt: vollständiger Urkundsentwurf, nicht nur Kurzfassung

## Ausnahmen und Verzicht

- Verbraucher kann auf die Frist verzichten (§ 17 Abs. 2a S. 2 BeurkG), wenn er das ausdrücklich erklärt. Notar dokumentiert dies in der Urkunde. Vorsicht: Verzicht schwächt Schutzfunktion; Dokumentation muss klar zeigen, dass Verzicht freiwillig und informiert.
- Keine Wartefrist bei beurkundeten Verträgen außerhalb des § 311b BGB.

## Rechtsfolgen bei Verstoß

§ 17 Abs. 2a BeurkG ist eine Amtspflichtvorschrift. Verstoß führt nicht automatisch zur Nichtigkeit des Vertrags, aber:
- Schadensersatzpflicht des Notars (§ 19 BNotO), wenn der Verbraucher nachteilige Entscheidung getroffen hat
- Berufsrechtliche Konsequenzen (Dienstaufsichtsbeschwerde)
- Anfechtbarkeit des Vertrags nach §§ 119 ff. BGB (wenn Verstoß zur Irrtumslage führte)?

## Prüfprogramm

- Ist eine Partei Verbraucher und die andere Unternehmer?
- Ist ein Grundstücksvertrag (§ 311b BGB) Gegenstand?
- Entwurfsversand dokumentiert (Datum, Empfänger, Übermittlungsweg)?
- 14-Tage-Frist berechnet und eingehalten?
- Wenn Verzicht: ausdrücklich erklärt und in Urkunde dokumentiert?

## Typische Fallen

- Versand nur an Anwalt des Verbrauchers, nicht an Verbraucher selbst → Fristbeginn fraglich.
- Wesentliche Vertragsänderung nach Versand → erneuter Versand + neue Frist?
- Fristberechnung nach §§ 187 ff. BGB fehlerhaft (Wochentage und Feiertage).
- Verzicht ohne ausreichende Aufklärung des Verbrauchers.
- Urkunde enthält keine Dokumentation des Fristablaufs.

## Rechtsquellen

- § 17 Abs. 2a BeurkG: https://dejure.org/gesetze/BeurkG/17.html
- § 13 BGB (Verbraucher): https://dejure.org/gesetze/BGB/13.html
- § 14 BGB (Unternehmer): https://dejure.org/gesetze/BGB/14.html
- § 19 BNotO: https://dejure.org/gesetze/BNotO/19.html
- BGH zu § 17 Abs. 2a BeurkG: https://www.bgh.de
- BNotK Belehrungspflichten: https://www.bnotk.de

## Output-Formate

- **Fristberechnungsblatt** (Entwurfsversand → Termin)
- **Entwurfsversand-Protokoll** (Datum, Empfänger, Übermittlung)
- **Verzichtserklärung-Muster** (für Urkunde)
- **Mandantenmail** (Entwurfsübersendung mit Fristhinweis)
- **Checkliste Verbrauchervertrag** (alle Schutzpflichten)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

## 2. `notariat-035-aufgebotsverfahren-verlorener-grundschuldbrief`

**Fokus:** Notariat im Alltag: Aufgebotsverfahren – verlorener Grundschuldbrief. Verfahren nach §§ 1162–1163 BGB i.V.m. FamFG, Antrag beim Amtsgericht, Bekanntmachungspflichten und Kraftloserklärung.

# Notariat im Alltag: Aufgebotsverfahren – verlorener Grundschuldbrief

## Zweck und Anwendungsbereich

Ein verlorener oder vernichteter Grundschuldbrief ist ein ernsthaftes Vollzugsproblem: Ohne Brief kann die Briefgrundschuld nicht übertragen oder gelöscht werden. Das Aufgebotsverfahren ermöglicht die Kraftloserklärung des Briefes und die Neubriefung oder Löschung.

Rechtsgrundlagen: § 1162 BGB (Aufgebot Hypothekenbrief), §§ 466–481 FamFG (Aufgebotsverfahren), § 1163 BGB (Eigentümergrundschuld), § 27 GBO (Löschung ohne Brief), § 1192 BGB (Grundschuld-Verweisung auf Hypothek), GBO § 56–68 (Grundbuchberichtigung).

## Wann Aufgebotsverfahren?

Ein Aufgebotsverfahren ist nötig, wenn:
- Grundschuldbrief verloren oder vernichtet (nicht nur verlegt)
- Brief nicht auffindbar und Löschung oder Übertragung der Grundschuld nötig
- Die briefführende Bank oder der Gläubiger kann Brief nicht vorlegen

Alternative: Gläubiger erklärt unter Vorlage eidesstattlicher Versicherung, dass Brief vernichtet wurde → Grundbuchamt kann Briefkraftloserklärung ohne FamFG ermöglichen (§ 67 GBO, Ermessen).

## Verfahrensablauf (§§ 466–481 FamFG)

1. **Antrag beim Amtsgericht** (§ 470 FamFG): Gläubiger oder Grundstückseigentümer stellt Antrag.
2. **Inhalt des Antrags:** Bezeichnung der Grundschuld (Grundbuch, Betrag, Gläubiger), Darlegung des Verlustes.
3. **Aufgebotsbekanntmachung:** Amtsgericht fordert öffentlich auf, dass Inhaber des Briefes sich meldet (§ 474 FamFG). Mindestfrist: 6 Monate.
4. **Ausschlussurteil:** Wenn sich kein Berechtigter meldet, erklärt das Gericht den Brief für kraftlos (§ 478 FamFG). Neuer Brief wird ausgestellt oder Löschung ohne Brief beantragt.
5. **Grundbuchamt:** Nach Kraftloserklärung Antrag auf Neubriefung oder Löschung (§ 27 GBO).

## Notar im Aufgebotsverfahren

- **Antragstellung:** Notar stellt Antrag beim Amtsgericht für den Antragsteller.
- **Koordination:** Vollzugsüberwachung; Kaufpreis und Löschungsunterlagen bis Aufgebot abgeschlossen koordinieren.
- **Eidesstattliche Versicherung:** Notar nimmt eidesstattliche Erklärung des Gläubigers über Verlust des Briefes auf (§ 156 StGB: Strafbarkeit falscher eidesstattlicher Versicherung).

## Zeitrahmen

Das Aufgebotsverfahren dauert i.d.R. 6–12 Monate. Wird in der Zwischenzeit ein Grundstückskauf vollzogen, kann der Notar die Kaufpreisfälligkeit unter den Vorbehalt der Kraftloserklärung stellen oder über Notaranderkonto abwickeln.

## Prüfprogramm

- Liegt wirklich ein Verlust vor (nicht nur Verwahrungsproblem)?
- Ist eine eidesstattliche Erklärung des Gläubigers ausreichend für das Grundbuchamt (§ 67 GBO)?
- Wer stellt Antrag (Gläubiger oder Eigentümer)?
- Wie wird Vollzug in der Wartezeit abgesichert?
- Kosten für Aufgebotsverfahren kommuniziert?

## Typische Fallen

- Aufgebot beantragt, aber Brief ist nur verlegt → unnötige Kosten und Zeitverlust.
- Kraftloserklärung nicht abgewartet, Löschung trotzdem beantragt → Zurückweisung.
- Eidesstattliche Versicherung ohne Notar-Aufnahme → Beweisschwäche.
- Kaufpreisfälligkeit ohne Sicherung während des Aufgebots.

## Rechtsquellen

- § 1162 BGB: https://dejure.org/gesetze/BGB/1162.html
- §§ 466–481 FamFG: https://dejure.org/gesetze/FamFG/466.html
- § 27 GBO: https://dejure.org/gesetze/GBO/27.html
- § 67 GBO: https://dejure.org/gesetze/GBO/67.html
- BGH zum Aufgebotsverfahren: https://www.bgh.de
- BNotK Grundbuchrecht: https://www.bnotk.de

## Output-Formate

- **Aufgebot-Antragsentwurf** (nach § 470 FamFG)
- **Eidesstattliche Versicherung** (Verlust-Erklärung)
- **Vollzugs-Sicherungsplan** (Kaufpreis in Wartezeit)
- **Mandantenmail** (Zeitrahmen, Kosten, Alternativen)
- **Grundbuchantrag nach Kraftloserklärung** (Muster)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de

## Kostenhinweise

Aufgebotsverfahren-Kosten: Gerichtskosten nach FamGKG, i.d.R. 0,5 Gebühr des Grundschuldbetrags. Notar: Antragstellung KV Nr. 22200 GNotKG (0,5 Gebühr). Bekanntmachungskosten trägt Antragsteller. Alternativlösung über § 67 GBO (eidesstattliche Versicherung beim Grundbuchamt): günstiger, schneller, abhängig von Behördenpraxis.

## Eidesstattliche Versicherung als Alternative

Manche Grundbuchämter akzeptieren eine notariell aufgenommene eidesstattliche Versicherung des Gläubigers, dass der Brief vernichtet oder verloren ist, ohne formales Aufgebotsverfahren (§ 67 GBO). Diese schnellere und günstigere Option sollte zuerst geprüft werden. Im Zweifel vorher beim Grundbuchamt anfragen.

## 3. `notariat-039-fristenkalender-vollzugsmonitor-wiedervorlage-eskal`

**Fokus:** Notariat im Alltag: Fristenkalender, Vollzugsmonitor, Wiedervorlage und Eskalation. Systematisches Fristenmanagement im Notariat, Wiedervorlagepflichten und Eskalationsregeln bei drohenden Vollzugsblockaden.

# Notariat im Alltag: Fristenkalender, Vollzugsmonitor, Wiedervorlage, Eskalation

## Zweck und Anwendungsbereich

Das Fristenmanagement ist die operative Lebensader des Notariats. Versäumte Fristen können den Rangverlust im Grundbuch, den Verfall einer Genehmigung oder die Haftung des Notars bedeuten. Dieser Skill strukturiert ein vollständiges Fristensystem für das Notariat.

Rechtsgrundlagen: §§ 186–193 BGB (Fristberechnung), § 17 Abs. 2a BeurkG (Verbraucherwartefrist), § 28 BauGB (Vorkaufsrechtsfrist 2 Monate), § 18 GBO (Zwischenverfügungs-Nachreichungsfrist), § 63 FamFG (Beschwerde 1 Monat), § 1944 BGB (Ausschlagungsfrist 6 Wochen), § 22 GrEStG (GrESt-Unbedenklichkeit), GwG § 8 (5 Jahre Aufbewahrung).

## Fristen-Kategorien im Notariat

| Kategorie | Beispiel | Konsequenz bei Versäumnis |
|---|---|---|
| Rechtsfrist (gesetzlich) | Ausschlagungsfrist § 1944 BGB | Erbschaft gilt als angenommen |
| Vollzugsfrist | Zwischenverfügung-Nachreichung | Antragszurückweisung, Rangverlust |
| Wartefrist | § 17 Abs. 2a BeurkG (14 Tage) | Haftungsrisiko, kein Nichtigkeit |
| Behördenfrist | § 28 BauGB (2 Monate Vorkaufsrecht) | Vollzug blockiert |
| Steuerfrist | GrESt-Bescheid vor Eintragung | § 22 GrEStG-Sperre |
| Archivfrist | GwG-Dokumentation 5 Jahre | Bußgeld |

## Vollzugsmonitor: Felder pro Vorgang

| Feld | Inhalt |
|---|---|
| Urkundenrolle-Nr. | Laufende Nummer |
| Beteiligte | Namen, Rollen |
| Offene Vollzugsblocks | Genehmigung / Negativattest / Löschungsunterlage |
| Nächste Frist | Datum, Art, Konsequenz |
| Verantwortliche Person | Notar / Sachbearbeitung / Mandant |
| Letzter Kontakt | Datum, Inhalt |
| Eskalationsstufe | Grün / Gelb / Rot |

## Wiedervorlagepflichten

Jeder Vorgang, der nicht vollständig abgeschlossen ist, erhält eine Wiedervorlage. Standardintervalle:
- Nach Beurkundung: 2 Wochen (Eingangsbestätigungen, erste Anträge)
- Nach Antrag bei Behörde: 4 Wochen (Erinnerung, falls keine Reaktion)
- Bei Zwischenverfügung: sofort (Fristnotiz, Mandanteninfo)
- Bei abgelaufener Frist ohne Reaktion: eskalieren

## Eskalationsregeln

| Ampel | Auslöser | Maßnahme |
|---|---|---|
| Grün | Fristen mind. 2 Wochen entfernt | Routine-Wiedervorlage |
| Gelb | Frist in < 1 Woche | Mandant aktiv kontaktieren, Sachbearbeitung priorisieren |
| Rot | Frist übermorgen oder abgelaufen | Notar persönlich informieren, Sofortmaßnahme einleiten |
| Schwarz | Frist verpasst | Schadensminimierung, ggf. Beschwerde/Fristverlängerung, Haftungscheck |

## Fristberechnung nach BGB (§§ 186–193 BGB)

- Beginn einer nach Tagen bemessenen Frist: § 187 Abs. 1 BGB – Tag des Ereignisses zählt nicht
- Ende: § 188 Abs. 1 BGB – letzter Tag um 24 Uhr
- Frist endet auf Samstag/Sonntag/Feiertag: § 193 BGB – nächster Werktag

## Prüfprogramm

- Sind alle Vollzugsfälligkeitsvoraussetzungen im Fristenkalender eingetragen?
- Gibt es Vorgänge ohne Wiedervorlage?
- Sind Ampel-Status aktuell?
- Wurde Mandant bei Gelbstufe bereits kontaktiert?
- Haftungsrelevante Fristen (Ausschlagung, Beschwerde) gesondert gekennzeichnet?

## Typische Fallen

- Zwischenverfügungsfrist übersehen → Antragszurückweisung, Rangverlust.
- Vorkaufsrechtsfrist (§ 28 BauGB) abgelaufen → Grundbuchamt fordert Negativattest neu.
- Ausschlagungsfrist versäumt → Erbschaft gilt als angenommen, Haftungsfolgen.
- Keine Wiedervorlage für offene Genehmigung → Kaufvertrag monatelang blockiert.

## Rechtsquellen

- §§ 186–193 BGB: https://dejure.org/gesetze/BGB/186.html
- § 18 GBO: https://dejure.org/gesetze/GBO/18.html
- § 28 BauGB: https://dejure.org/gesetze/BauGB/28.html
- § 1944 BGB: https://dejure.org/gesetze/BGB/1944.html
- BNotK Vollzugshinweise: https://www.bnotk.de

## Output-Formate

- **Vollzugsmonitor-Tabelle** (alle Felder pro Vorgang)
- **Fristenkalender-Vorlage** (nach Fristen-Kategorie sortiert)
- **Ampel-Statusbericht** (tägliche Übersicht)
- **Eskalationsmail-Muster** (Mandant bei Gelbstufe)
- **Notar-Haftungswarnung** (bei verpasster kritischer Frist)

Quellen für Live-Check: https://dejure.org | https://openjur.de | https://www.gesetze-im-internet.de | https://www.bnotk.de | https://www.bgh.de | https://www.bverfg.de
