---
name: international-cisg-handelsregister
description: "International CISG Handelsregister: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# International CISG Handelsregister

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **International CISG Handelsregister** im Plugin Handelsrecht (HGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `handelsrecht-international-und-cisg-schnittstelle` | Prüft HGB bei internationalem Handelskauf, CISG-Abgrenzung, Rom I und Gerichtsstand. |
| `handelsregister-paragraphen-8-16-hgb` | Prüft Handelsregister, Einsicht, Bekanntmachung, negative/positive Publizität und Eintragungswirkung. |

## Arbeitsweg

Im Plugin Handelsrecht (HGB) gilt für **International CISG Handelsregister**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `handelsrecht-international-und-cisg-schnittstelle`

**Fokus:** Prüft HGB bei internationalem Handelskauf, CISG-Abgrenzung, Rom I und Gerichtsstand.

# Internationaler Bezug und CISG-Schnittstelle

## Fachkern: Internationaler Bezug und CISG-Schnittstelle
- **Spezialgegenstand:** Internationaler Bezug und CISG-Schnittstelle; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Route zu internationalem Wirtschaftsrecht bei Bedarf.

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

## 2. `handelsregister-paragraphen-8-16-hgb`

**Fokus:** Prüft Handelsregister, Einsicht, Bekanntmachung, negative/positive Publizität und Eintragungswirkung.

# Handelsregister §§ 8 ff. HGB

## Fachkern: Handelsregister §§ 8 ff. HGB
- **Spezialgegenstand:** Handelsregister §§ 8 ff. HGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Arbeite mit § 15 HGB und Registerbelegen.

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
