---
name: unterlagenmappe-kdv-verwaltungsakt
description: "Unterlagenmappe KDV Verwaltungsakt: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Unterlagenmappe KDV Verwaltungsakt

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Unterlagenmappe KDV Verwaltungsakt** im Plugin Kriegsdienstverweigerung Wehrdienst. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `unterlagenmappe-kdv` | Strukturiert Antrag, Lebenslauf, Begründung, Belege, Nachweise und Bescheide. |
| `verwaltungsakt-oder-informelles-schreiben` | Unterscheidet Bescheid, Aufforderung, Sachstand und informelle E-Mail. |
| `verwaltungsgericht-kdvg-10` | Routet Klage und gerichtliche Besonderheiten in KDV-Sachen. |
| `vollstaendiger-lebenslauf` | Erstellt einen vollständigen, datensparsamen Lebenslauf mit gewissensrelevanten Stationen. |
| `vollstaendigkeit-kdvg-2` | Prüft Anschreiben, Art.-4-Berufung, Lebenslauf und persönliche Begründung. |

## Arbeitsweg

Im Plugin Kriegsdienstverweigerung Wehrdienst gilt für **Unterlagenmappe KDV Verwaltungsakt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `unterlagenmappe-kdv`

**Fokus:** Strukturiert Antrag, Lebenslauf, Begründung, Belege, Nachweise und Bescheide.

# Unterlagenmappe KDV

## Fachkern: Unterlagenmappe KDV
- **Spezialgegenstand:** Unterlagenmappe KDV; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Führt den Nutzer ruhig durch Status, Ziel, Fristen, Unterlagen und nächste Schritte, ohne die persönliche Gewissensentscheidung zu ersetzen.

## Fachlicher Kern
Strukturiert Antrag, Lebenslauf, Begründung, Belege, Nachweise und Bescheide. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2; KDVG § 12

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

## 2. `verwaltungsakt-oder-informelles-schreiben`

**Fokus:** Unterscheidet Bescheid, Aufforderung, Sachstand und informelle E-Mail.

# Verwaltungsakt oder Hinweis

## Fachkern: Verwaltungsakt oder Hinweis
- **Spezialgegenstand:** Verwaltungsakt oder Hinweis; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Prüft Widerspruch, Klage, § 75 VwGO, § 80 VwGO, § 123 VwGO und besondere KDVG-Fristen.

## Fachlicher Kern
Unterscheidet Bescheid, Aufforderung, Sachstand und informelle E-Mail. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
VwVfG/VwGO live prüfen

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Fristen, Zustellung und Dokumenttyp prüfen, bevor Widerspruch, Klage oder Eilantrag vorgeschlagen werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 3. `verwaltungsgericht-kdvg-10`

**Fokus:** Routet Klage und gerichtliche Besonderheiten in KDV-Sachen.

# Verwaltungsgericht § 10 KDVG

## Fachkern: Verwaltungsgericht § 10 KDVG
- **Spezialgegenstand:** Verwaltungsgericht § 10 KDVG; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Prüft Widerspruch, Klage, § 75 VwGO, § 80 VwGO, § 123 VwGO und besondere KDVG-Fristen.

## Fachlicher Kern
Routet Klage und gerichtliche Besonderheiten in KDV-Sachen. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 10; VwGO

## Output
- Statusampel.
- Unterlagen- und Fristenliste.
- nächster Schriftsatz oder nächste Verfahrenshandlung.
- Warnhinweis, falls der Fall in Totalverweigerung, bloße Politik oder Disziplinarrisiko kippt.

## Rote Linien
Fristen, Zustellung und Dokumenttyp prüfen, bevor Widerspruch, Klage oder Eilantrag vorgeschlagen werden.

## Anschluss-Skills
- `kriegsdienstverweigerung-wehrdienst-allgemein` für Kaltstart und Routing.
- `qualitaetsgate-vor-ausgabe` vor belastbarer Ausgabe.
- `rechtsprechung-livecheck` bei Gerichtsargumentation.

## Quellen- und Aktualitätsregel
- Aktuelle Fassung von GG, KDVG, WPflG, SG und VwGO in amtlichen Quellen prüfen.
- BAFzA-Hinweise zum Antragsweg, zur hohen Antragslast und zu § 13 KDVG n. F. berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Link nennen.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## 4. `vollstaendiger-lebenslauf`

**Fokus:** Erstellt einen vollständigen, datensparsamen Lebenslauf mit gewissensrelevanten Stationen.

# Tabellarischer Lebenslauf

## Fachkern: Tabellarischer Lebenslauf
- **Spezialgegenstand:** Tabellarischer Lebenslauf; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Macht aus einem inneren Anliegen ein vollständiges, nachweisbares Antragspaket nach § 2 KDVG.

## Fachlicher Kern
Erstellt einen vollständigen, datensparsamen Lebenslauf mit gewissensrelevanten Stationen. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2 Abs. 2; KDVG § 12

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

## 5. `vollstaendigkeit-kdvg-2`

**Fokus:** Prüft Anschreiben, Art.-4-Berufung, Lebenslauf und persönliche Begründung.

# Vollständigkeit § 2 KDVG

## Fachkern: Vollständigkeit § 2 KDVG
- **Spezialgegenstand:** Vollständigkeit § 2 KDVG; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** Art. 4 Abs. 3 GG, KDVG, WPflG/Wehrrecht, VwVfG/VwGO, Gewissensprüfung, Soldatenstatus und Eilrechtsschutz.
- **Entscheidende Weiche:** Gewissensentscheidung, politisches Motiv, Status, Zuständigkeit, Bescheid, Untätigkeit, Frist und gerichtlicher Rechtsschutz trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Einsatz
Macht aus einem inneren Anliegen ein vollständiges, nachweisbares Antragspaket nach § 2 KDVG.

## Fachlicher Kern
Prüft Anschreiben, Art.-4-Berufung, Lebenslauf und persönliche Begründung. Die Antwort muss den konkreten Status, das Datum, die Behörde und die aktuelle Verfahrenslage aufnehmen. Bei KDV ist die innere Gewissensentscheidung nicht vollständig beweisbar wie eine äußere Tatsache; sie muss aber persönlich, plausibel und widerspruchsbewusst dargestellt werden.

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
KDVG § 2 Abs. 2; KDVG § 7 Abs. 1 Nr. 2

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
