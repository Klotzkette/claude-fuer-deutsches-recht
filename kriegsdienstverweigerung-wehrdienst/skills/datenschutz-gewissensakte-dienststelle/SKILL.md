---
name: datenschutz-gewissensakte-dienststelle
description: "Datenschutz Gewissensakte Dienststelle: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Datenschutz Gewissensakte Dienststelle

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Datenschutz Gewissensakte Dienststelle** im Plugin Kriegsdienstverweigerung Wehrdienst. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `datenschutz-gewissensakte` | Schützt Gewissensbegründung, Gesundheitsdaten und Personalakten. |
| `dienststelle-kommunikation` | Formuliert sachliche Dienststellenkommunikation ohne Provokation. |
| `disziplinarrisiken-soldaten` | Warnt vor Disziplinar- und Strafrisiken bei eigenmächtigem Verhalten. |
| `disziplinarvorgesetzter-stellungnahme` | Erklärt Stellungnahme der Disziplinarvorgesetzten bei Berufs- und Zeitsoldaten. |
| `doppelte-staatsangehoerigkeit` | Routet deutsche KDV und ausländische Wehrpflichten ohne falsche Auslandsversprechen. |

## Arbeitsweg

Im Plugin Kriegsdienstverweigerung Wehrdienst gilt für **Datenschutz Gewissensakte Dienststelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `datenschutz-gewissensakte`

**Fokus:** Schützt Gewissensbegründung, Gesundheitsdaten und Personalakten.

# Datenschutz Gewissensakte

## Fachkern: Datenschutz Gewissensakte
- **Spezialgegenstand:** Datenschutz Gewissensakte; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Schützt Gewissens-, Gesundheits-, Personal- und Verfahrensdaten vor unnötiger Offenlegung.

## Fachlicher Kern
Schützt Gewissensbegründung, Gesundheitsdaten und Personalakten. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
DSGVO; KDVG § 12

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Keine vollständigen Personal-, Gesundheits- oder Gewissensakten in ungeprüfte Systeme laden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 2. `dienststelle-kommunikation`

**Fokus:** Formuliert sachliche Dienststellenkommunikation ohne Provokation.

# Kommunikation mit Dienststelle

## Fachkern: Kommunikation mit Dienststelle
- **Spezialgegenstand:** Kommunikation mit Dienststelle; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Behandelt aktive Soldatinnen und Soldaten, SaZ, Berufssoldaten, FWDL und soldatenrechtliche Nebenfolgen.

## Fachlicher Kern
Formuliert sachliche Dienststellenkommunikation ohne Provokation. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
KDVG § 2 Abs. 6; § 4; SG

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Nie pauschal zur Befehlsverweigerung raten; akute Dienstpflichten, Disziplinarrisiken und anwaltliche Absicherung sauber trennen.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 3. `disziplinarrisiken-soldaten`

**Fokus:** Warnt vor Disziplinar- und Strafrisiken bei eigenmächtigem Verhalten.

# Disziplinarrisiken

## Fachkern: Disziplinarrisiken
- **Spezialgegenstand:** Disziplinarrisiken; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Behandelt aktive Soldatinnen und Soldaten, SaZ, Berufssoldaten, FWDL und soldatenrechtliche Nebenfolgen.

## Fachlicher Kern
Warnt vor Disziplinar- und Strafrisiken bei eigenmächtigem Verhalten. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
SG; WDO 2025; WStG; KDVG

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Nie pauschal zur Befehlsverweigerung raten; akute Dienstpflichten, Disziplinarrisiken und anwaltliche Absicherung sauber trennen.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 4. `disziplinarvorgesetzter-stellungnahme`

**Fokus:** Erklärt Stellungnahme der Disziplinarvorgesetzten bei Berufs- und Zeitsoldaten.

# Stellungnahme Disziplinarvorgesetzter

## Fachkern: Stellungnahme Disziplinarvorgesetzter
- **Spezialgegenstand:** Stellungnahme Disziplinarvorgesetzter; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Behandelt aktive Soldatinnen und Soldaten, SaZ, Berufssoldaten, FWDL und soldatenrechtliche Nebenfolgen.

## Fachlicher Kern
Erklärt Stellungnahme der Disziplinarvorgesetzten bei Berufs- und Zeitsoldaten. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
KDVG § 2 Abs. 6 Satz 3

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Nie pauschal zur Befehlsverweigerung raten; akute Dienstpflichten, Disziplinarrisiken und anwaltliche Absicherung sauber trennen.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 5. `doppelte-staatsangehoerigkeit`

**Fokus:** Routet deutsche KDV und ausländische Wehrpflichten ohne falsche Auslandsversprechen.

# Doppelte Staatsangehörigkeit

## Fachkern: Doppelte Staatsangehörigkeit
- **Spezialgegenstand:** Doppelte Staatsangehörigkeit; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Routet besondere Konstellationen wie Ausland, doppelte Staatsangehörigkeit, Minderjährige, Frauen, frühere Anerkennung und Krisenlagen.

## Fachlicher Kern
Routet deutsche KDV und ausländische Wehrpflichten ohne falsche Auslandsversprechen. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

## Sofortfragen
1. Welche Personengruppe liegt vor: ungedient, wehrpflichtig, FWDL, SaZ, Berufssoldat, Reservist, frühere Soldatin/früherer Soldat oder Sonderfall?
2. Gibt es bereits Antrag, Eingangsbestätigung, Personenkennziffer, Musterungsbescheid, BAFzA-Schreiben, Anhörung oder Bescheid?
3. Geht es um Kriegsdienst mit der Waffe als Gewissensproblem oder um Politik, Gesundheit, Angst, Karriere, Familie oder Totalverweigerung?
4. Welche Frist läuft und welcher Nachweis liegt für Zugang oder Bekanntgabe vor?

## Arbeitsgang
1. Status und anwendbare Normen festlegen.
2. Pflichtunterlagen und fehlende Dokumente markieren.
3. Gewissenskern von bloßen Randmotiven trennen.
4. Behördenweg BAPersBw -> BAFzA oder Soldaten-/Reservistenpfad bestimmen.
5. Output knapp, würdig und nachweisbar formulieren.

## Norm- und Quellenanker
WPflG § 1; KDVG; ausländisches Recht live prüfen

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Keine schematische Antwort geben; die konkrete Gewissenslage, der Status und die aktuelle Rechtslage müssen sichtbar geprüft werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
