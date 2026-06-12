---
name: subsumtions-rewrite-klausurton
description: "Schreibt falsche oder lueckenhafte Subsumtionen in einen knappen juristischen Klausurton um, ohne neue Tatsachen zu erfinden. Vier-Schritt-Schema: Obersatz, Definition, Subsumtion, Ergebnis je Tatbestandsmerkmal im Subsumtions Prüfer."
---

# Subsumtion im Klausurton neu schreiben

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Ziel

Dieser Skill schreibt fehlerhafte oder lückenhafte Subsumtionen in sauberen juristischen Klausurton um. Er fügt keine neuen Tatsachen hinzu und erfindet keine Belege. Er korrigiert Obersatz, Definition, Subsumtion und Ergebnis — je Tatbestandsmerkmal getrennt.

## Klausurton: Stilregeln

### Gutachtenstil (Standard für Klausur und Hausarbeit)

| Element | Stilregel | Beispiel |
|---|---|---|
| Obersatz | Konjunktiv; Anspruchsfrage | "A könnte gegen B einen Anspruch auf Zahlung von EUR X aus § 433 Abs. 2 BGB haben." |
| Definition | Abstrakt, ohne Bezug auf konkreten Fall; mit Quellenhinweis | "Unter einer Sache iSd § 90 BGB versteht man jeden körperlichen Gegenstand." |
| Subsumtion | Tatsachen des Falles unter Definition halten | "Hier ist der Pkw ein körperlicher Gegenstand und damit eine Sache iSd § 90 BGB." |
| Zwischenergebnis | Indikativ; klar | "Dieses Tatbestandsmerkmal ist erfüllt." |
| Gesamtergebnis | Indikativ; klar | "A hat gegen B einen Anspruch aus § 433 Abs. 2 BGB." |

### Urteilsstil (für Schriftsatz und Bescheid)

- Ergebnis steht am Anfang: "Die Klage ist begründet."
- Begründung folgt deduktiv: "Denn A hat gegen B einen Anspruch aus § 433 Abs. 2 BGB, weil ..."
- Kein Konjunktiv im Einstieg

## Typische Rewrite-Muster

### Fehler 1: Sprung-Subsumtion → Rewrite

**Vor:** "§ 433 Abs. 2 BGB: Der Kaufpreis ist zu zahlen. Hier ist er noch nicht gezahlt."

**Nach:** "Nach § 433 Abs. 2 BGB ist der Käufer verpflichtet, dem Verkäufer den vereinbarten Kaufpreis zu zahlen. Kaufpreis ist die im Kaufvertrag als Gegenleistung vereinbarte Geldsumme. Hier haben A und B im Kaufvertrag v. TT.MM.JJJJ einen Kaufpreis von EUR X vereinbart. Dieser ist nach Anlage K1 noch nicht bezahlt worden. Die Zahlungspflicht besteht daher."

### Fehler 2: Zirkelschluss → Rewrite

**Vor:** "Eine Pflichtverletzung liegt vor, weil B seine Pflichten verletzt hat."

**Nach:** "Eine Pflichtverletzung iSd § 280 Abs. 1 BGB ist jedes objektive Abweichen vom geschuldeten Verhalten. B schuldete nach dem Werkvertrag die Herstellung eines mangelfreien Werks (§ 631 Abs. 1 BGB). Die Lieferung erfolgte laut Abnahmeprotokoll (Anlage K2) mit Rissen in der Fassade. Dies weicht vom geschuldeten mangelfreien Zustand ab. Eine Pflichtverletzung liegt vor."

### Fehler 3: Konjunktiv im Schluss → Rewrite

**Vor:** "Das Tatbestandsmerkmal könnte vorliegen."

**Nach:** "Das Tatbestandsmerkmal liegt vor." oder "Das Tatbestandsmerkmal liegt nicht vor, weil [Begründung]."

### Fehler 4: Definition aus dem Sachverhalt → Rewrite

**Vor:** "Vereinbart" im Sinne der Parteienabsprache heißt, dass A und B das vereinbart haben.

**Nach:** "Vereinbart" iSd § 145 BGB setzt voraus, dass ein Angebot auf Abschluss eines Vertrags und eine Annahme vorliegen (§§ 145, 147 BGB). ...

## Rewrite-Workflow

1. **Fehlerdiagnose:** Obersatz, Definition, Subsumtion, Ergebnis je TBM markieren (vorhanden / fehlt / falsch).
2. **Priorität setzen:** Welcher Fehler ist am schwersten? (Sprung-Subsumtion, Zirkelschluss, falscher Stil)
3. **Rewrite:** Je TBM: Obersatz → Definition (mit Norm; Quelle als Prüfpunkt) → Tatsachen aus dem Sachverhalt → Zwischenergebnis.
4. **Stilkontrolle:** Konjunktiv im Obersatz? Indikativ im Zwischenergebnis? Tatsachen aus der Akte?
5. **Quellenkontrolle:** Jede Definition auf Norm oder (als Prüfpunkt) auf BGH-Linie gestützt?

## Quellen-Disziplin beim Rewrite

- Normtext aus gesetze-im-internet.de: live prüfen und exakt zitieren
- Rechtsprechungs-Definitionen: als Prüfpunkt markieren ("nach BGH [live zu prüfen unter dejure.org / bgh.de]")
- Keine Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen

## Ausgabe

Vollständige Rewrite-Passage je TBM; davor kurzer Fehlerhinweis ("Fehler: Sprung-Subsumtion → jetzt korrigiert"). Rechtsprechung nur mit live verifizierbarem Aktenzeichen.
