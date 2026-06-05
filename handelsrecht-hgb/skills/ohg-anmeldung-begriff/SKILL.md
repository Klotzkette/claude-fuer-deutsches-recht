---
name: ohg-anmeldung-begriff
description: "OHG Anmeldung Begriff: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# OHG Anmeldung Begriff

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **OHG Anmeldung Begriff** im Plugin Handelsrecht (HGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ohg-anmeldung-statuswechsel-paragraph-106` | Prüft Anmeldung, Statuswechsel aus Gesellschaftsregister, Registerlogik und Fehlerfolgen. |
| `ohg-begriff-und-entstehung-paragraph-105` | Prüft OHG nach MoPeG: Betrieb eines Handelsgewerbes unter gemeinschaftlicher Firma und BGB-Verweis. |

## Arbeitsweg

Im Plugin Handelsrecht (HGB) gilt für **OHG Anmeldung Begriff**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ohg-anmeldung-statuswechsel-paragraph-106`

**Fokus:** Prüft Anmeldung, Statuswechsel aus Gesellschaftsregister, Registerlogik und Fehlerfolgen.

# OHG Anmeldung und Statuswechsel § 106 HGB

## Fachkern: OHG Anmeldung und Statuswechsel § 106 HGB
- **Spezialgegenstand:** OHG Anmeldung und Statuswechsel § 106 HGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Notar/Registergericht-Fahrplan.

## Rechts- und Quellenanker

HGB amtlich prüfen: https://www.gesetze-im-internet.de/hgb/. Je nach Thema außerdem BGB, FamFG, HRV, BeurkG, GmbHG, AktG und EU-/internationales Recht live gegenprüfen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kurzvotum
- Register-/Vertrags-/Prozessfahrplan
- Beweis- und Dokumentenliste
- Risikoampel
- Anschluss-Skills


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `ohg-begriff-und-entstehung-paragraph-105`

**Fokus:** Prüft OHG nach MoPeG: Betrieb eines Handelsgewerbes unter gemeinschaftlicher Firma und BGB-Verweis.

# OHG Begriff und Entstehung § 105 HGB

## Fachkern: OHG Begriff und Entstehung § 105 HGB
- **Spezialgegenstand:** OHG Begriff und Entstehung § 105 HGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Besonders Statuswechsel eGbR/OHG.

## Rechts- und Quellenanker

HGB amtlich prüfen: https://www.gesetze-im-internet.de/hgb/. Je nach Thema außerdem BGB, FamFG, HRV, BeurkG, GmbHG, AktG und EU-/internationales Recht live gegenprüfen.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kurzvotum
- Register-/Vertrags-/Prozessfahrplan
- Beweis- und Dokumentenliste
- Risikoampel
- Anschluss-Skills


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
