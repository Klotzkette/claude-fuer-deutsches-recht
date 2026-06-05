---
name: registerpublizitaet-paragraph-scheinkaufmann
description: "Registerpublizitaet Paragraph Scheinkaufmann: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Registerpublizitaet Paragraph Scheinkaufmann

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Registerpublizitaet Paragraph Scheinkaufmann** im Plugin Handelsrecht (HGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `registerpublizitaet-paragraph-15-hgb` | Prüft negative und positive Publizität des Handelsregisters. |
| `scheinkaufmann-und-rechtsschein` | Prüft Rechtsschein kaufmännischen Auftretens und Vertrauensschutz. |

## Arbeitsweg

Im Plugin Handelsrecht (HGB) gilt für **Registerpublizitaet Paragraph Scheinkaufmann**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `registerpublizitaet-paragraph-15-hgb`

**Fokus:** Prüft negative und positive Publizität des Handelsregisters.

# Registerpublizität § 15 HGB

## Fachkern: Registerpublizität § 15 HGB
- **Spezialgegenstand:** Registerpublizität § 15 HGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Zeitpunkt, Kenntnis, einzutragende Tatsache, Bekanntmachung.

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

## 2. `scheinkaufmann-und-rechtsschein`

**Fokus:** Prüft Rechtsschein kaufmännischen Auftretens und Vertrauensschutz.

# Scheinkaufmann und Rechtsschein

## Fachkern: Scheinkaufmann und Rechtsschein
- **Spezialgegenstand:** Scheinkaufmann und Rechtsschein; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Trenne Registereintragung, Auftreten und Zurechnung.

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
