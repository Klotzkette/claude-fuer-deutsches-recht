---
name: begruendung-ehemalige-anerkannte-reservisten
description: "Begruendung Ehemalige Anerkannte Reservisten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Begruendung Ehemalige Anerkannte Reservisten

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Begruendung Ehemalige Anerkannte Reservisten** im Plugin Kriegsdienstverweigerung Wehrdienst. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `begruendung-fuer-ehemalige-anerkannte` | Prüft Widerspruch zwischen alter Anerkennung und späterer Bundeswehrnähe. |
| `begruendung-fuer-reservisten` | Spezialwerkstatt für Reservisten mit früherem Dienst und aktueller Heranziehungsnähe. |
| `begruendung-fuer-ungediente` | Spezialwerkstatt für ungediente Antragsteller ohne Umkehrproblem. |
| `begruendung-redaktion-ohne-schablone` | Überarbeitet persönliche Begründung sprachlich, ohne sie zu standardisieren. |
| `beistand-kirchen-beratung` | Ordnet Beistand, kirchliche Beauftragte und anwaltliche Vertretung. |

## Arbeitsweg

Im Plugin Kriegsdienstverweigerung Wehrdienst gilt für **Begruendung Ehemalige Anerkannte Reservisten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `begruendung-fuer-ehemalige-anerkannte`

**Fokus:** Prüft Widerspruch zwischen alter Anerkennung und späterer Bundeswehrnähe.

# Frühere Anerkennung späterer Dienst

## Fachkern: Frühere Anerkennung späterer Dienst
- **Spezialgegenstand:** Frühere Anerkennung späterer Dienst; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Routet besondere Konstellationen wie Ausland, doppelte Staatsangehörigkeit, Minderjährige, Frauen, frühere Anerkennung und Krisenlagen.

## Fachlicher Kern
Prüft Widerspruch zwischen alter Anerkennung und späterer Bundeswehrnähe. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
BAFzA-Hinweise; BVerwG 2012/2018

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

## 2. `begruendung-fuer-reservisten`

**Fokus:** Spezialwerkstatt für Reservisten mit früherem Dienst und aktueller Heranziehungsnähe.

# Begründung Reservisten

## Fachkern: Begründung Reservisten
- **Spezialgegenstand:** Begründung Reservisten; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Behandelt Reserve, Beorderung, Wehrübungen, frühere Dienstzeit und erneute Heranziehung.

## Fachlicher Kern
Spezialwerkstatt für Reservisten mit früherem Dienst und aktueller Heranziehungsnähe. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 4; BVerwG-Maßstab

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

## 3. `begruendung-fuer-ungediente`

**Fokus:** Spezialwerkstatt für ungediente Antragsteller ohne Umkehrproblem.

# Begründung Ungediente

## Fachkern: Begründung Ungediente
- **Spezialgegenstand:** Begründung Ungediente; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Hilft, die höchstpersönliche Gewissensentscheidung gegen den Kriegsdienst mit der Waffe wahrhaftig, konkret und prüfbar darzustellen.

## Fachlicher Kern
Spezialwerkstatt für ungediente Antragsteller ohne Umkehrproblem. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2; KDVG § 5

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Keine fremde Mustervorlage produzieren; die Darstellung muss persönlich, wahrhaftig und aus der eigenen Sprache der Person entwickelt sein.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 4. `begruendung-redaktion-ohne-schablone`

**Fokus:** Überarbeitet persönliche Begründung sprachlich, ohne sie zu standardisieren.

# Redaktion ohne Schablone

## Fachkern: Redaktion ohne Schablone
- **Spezialgegenstand:** Redaktion ohne Schablone; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Hilft, die höchstpersönliche Gewissensentscheidung gegen den Kriegsdienst mit der Waffe wahrhaftig, konkret und prüfbar darzustellen.

## Fachlicher Kern
Überarbeitet persönliche Begründung sprachlich, ohne sie zu standardisieren. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2; BAFzA-Hinweise

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Keine fremde Mustervorlage produzieren; die Darstellung muss persönlich, wahrhaftig und aus der eigenen Sprache der Person entwickelt sein.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 5. `beistand-kirchen-beratung`

**Fokus:** Ordnet Beistand, kirchliche Beauftragte und anwaltliche Vertretung.

# Beistand und Beratung

## Fachkern: Beistand und Beratung
- **Spezialgegenstand:** Beistand und Beratung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Ordnet Behördenrollen, Musterung, Registrierung, Zuleitung, Anhörung, Anerkennung und Ablehnung.

## Fachlicher Kern
Ordnet Beistand, kirchliche Beauftragte und anwaltliche Vertretung. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG §§ 8, 10; VwGO § 67

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
