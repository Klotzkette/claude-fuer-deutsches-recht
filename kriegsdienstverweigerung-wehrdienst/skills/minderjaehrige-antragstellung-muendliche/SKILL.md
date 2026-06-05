---
name: minderjaehrige-antragstellung-muendliche
description: "Minderjaehrige Antragstellung Muendliche: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Minderjaehrige Antragstellung Muendliche

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Minderjaehrige Antragstellung Muendliche** im Plugin Kriegsdienstverweigerung Wehrdienst. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `minderjaehrige-antragstellung` | Prüft Antrag sechs Monate vor 18 oder vor 17 unter Sondervoraussetzungen. |
| `muendliche-anhoerung-vorbereitung` | Bereitet nichtöffentliche mündliche Anhörung ohne auswendig gelernte Musterantworten vor. |
| `musterung-verweigert-ablehnung` | Erklärt Ablehnungsrisiko bei Musterungsverweigerung. |
| `musterungen-und-eignung` | Erklärt, warum KDV-Antrag Musterung grundsätzlich nicht ersetzt und wie § 13 wirkt. |
| `musterungsbescheid-bestandskraft` | Prüft Bedeutung des Musterungsbescheids für Zuleitung und Entscheidung. |

## Arbeitsweg

Im Plugin Kriegsdienstverweigerung Wehrdienst gilt für **Minderjaehrige Antragstellung Muendliche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `minderjaehrige-antragstellung`

**Fokus:** Prüft Antrag sechs Monate vor 18 oder vor 17 unter Sondervoraussetzungen.

# Minderjährige Antragstellung

## Fachkern: Minderjährige Antragstellung
- **Spezialgegenstand:** Minderjährige Antragstellung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Routet besondere Konstellationen wie Ausland, doppelte Staatsangehörigkeit, Minderjährige, Frauen, frühere Anerkennung und Krisenlagen.

## Fachlicher Kern
Prüft Antrag sechs Monate vor 18 oder vor 17 unter Sondervoraussetzungen. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2 Abs. 4-5

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

## 2. `muendliche-anhoerung-vorbereitung`

**Fokus:** Bereitet nichtöffentliche mündliche Anhörung ohne auswendig gelernte Musterantworten vor.

# Mündliche Anhörung

## Fachkern: Mündliche Anhörung
- **Spezialgegenstand:** Mündliche Anhörung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Bereitet nichtöffentliche mündliche Anhörung ohne auswendig gelernte Musterantworten vor. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG §§ 6, 8

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

## 3. `musterung-verweigert-ablehnung`

**Fokus:** Erklärt Ablehnungsrisiko bei Musterungsverweigerung.

# Musterung verweigert Risiko

## Fachkern: Musterung verweigert Risiko
- **Spezialgegenstand:** Musterung verweigert Risiko; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Erklärt Ablehnungsrisiko bei Musterungsverweigerung. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 3 Abs. 1; § 7 Abs. 1 Nr. 1; § 13

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

## 4. `musterungen-und-eignung`

**Fokus:** Erklärt, warum KDV-Antrag Musterung grundsätzlich nicht ersetzt und wie § 13 wirkt.

# Musterung und Eignung

## Fachkern: Musterung und Eignung
- **Spezialgegenstand:** Musterung und Eignung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Erklärt, warum KDV-Antrag Musterung grundsätzlich nicht ersetzt und wie § 13 wirkt. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG §§ 2, 3, 13; WPflG §§ 3, 8a, 16

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

## 5. `musterungsbescheid-bestandskraft`

**Fokus:** Prüft Bedeutung des Musterungsbescheids für Zuleitung und Entscheidung.

# Bestandskräftiger Musterungsbescheid

## Fachkern: Bestandskräftiger Musterungsbescheid
- **Spezialgegenstand:** Bestandskräftiger Musterungsbescheid; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Prüft Bedeutung des Musterungsbescheids für Zuleitung und Entscheidung. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2 Abs. 6; KDVG § 13

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
