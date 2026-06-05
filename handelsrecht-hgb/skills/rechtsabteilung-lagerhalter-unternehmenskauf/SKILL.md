---
name: rechtsabteilung-lagerhalter-unternehmenskauf
description: "Rechtsabteilung Lagerhalter Unternehmenskauf: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsabteilung Lagerhalter Unternehmenskauf

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Rechtsabteilung Lagerhalter Unternehmenskauf** im Plugin Handelsrecht (HGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsabteilung-lagerhalter-und-speditionshaftung` | Rechtsabteilungs-Fachmodul für Lagerhalter- und Speditionshaftung: Schaden, Haftungsgrenzen und Regressketten werden schnell berechnet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `unternehmenskauf-hgb-haftung` | Prüft Firmenfortführung, Handelsgeschäft, Prokura, Vertragsübernahme und Haftungsrisiken im Asset Deal. |

## Arbeitsweg

Im Plugin Handelsrecht (HGB) gilt für **Rechtsabteilung Lagerhalter Unternehmenskauf**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsabteilung-lagerhalter-und-speditionshaftung`

**Fokus:** Rechtsabteilungs-Fachmodul für Lagerhalter- und Speditionshaftung: Schaden, Haftungsgrenzen und Regressketten werden schnell berechnet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: Lagerhalter- und Speditionshaftung

## Fachkern: Rechtsabteilung: Lagerhalter- und Speditionshaftung
- **Spezialgegenstand:** Rechtsabteilung: Lagerhalter- und Speditionshaftung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Spezialkern: Rechtsabteilung: Lagerhalter- und Speditionshaftung

- **Konkretes Problem:** Schaden, Haftungsgrenzen und Regressketten werden schnell berechnet.
- **Norm-/Quellenanker:** HGB Handelsstand, Prokura, Handelskauf § 377 HGB, Kommission, Lager/Spedition/Fracht, kaufmännische Bestätigung und BGB-Schnittstellen.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

HGB §§ 453 ff., 467 ff.; ADSp nur als Vertragswerk

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Schaden, Haftungsgrenzen und Regressketten werden schnell berechnet.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.

## 2. `unternehmenskauf-hgb-haftung`

**Fokus:** Prüft Firmenfortführung, Handelsgeschäft, Prokura, Vertragsübernahme und Haftungsrisiken im Asset Deal.

# Unternehmenskauf HGB-Haftung

## Fachkern: Unternehmenskauf HGB-Haftung
- **Spezialgegenstand:** Unternehmenskauf HGB-Haftung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** HGB, BGB, MoPeG-Schnittstellen, Handelsregister/FamFG, Prokura/Handlungsvollmacht, Handelsgeschäfte, Kommission/Fracht/Lager und Gesellschaftsrecht.
- **Entscheidende Weiche:** Kaufmannseigenschaft, Registerlage, Vertretungsmacht, Handelsbrauch, Rüge-/Untersuchungsobliegenheit, Sicherheiten und Prozessbeweis trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Besonders § 25 HGB und Register-/Bekanntmachungslogik.

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
