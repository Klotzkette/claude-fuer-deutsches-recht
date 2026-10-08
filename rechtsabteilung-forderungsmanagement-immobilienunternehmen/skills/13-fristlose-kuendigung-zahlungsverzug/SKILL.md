---
name: 13-fristlose-kuendigung-zahlungsverzug
description: "Fristlose Kündigung wegen Mietzahlungsverzug nach Paragraf 543 und 569 BGB erstellen. Rückstandsschwelle, zwei Termine, längerer Zeitraum, hilfsweise ordentliche Kündigung und Pflicht-Handoff zu Zustellung Skill 15. Output Kündigung."
---

# Fristlose Kündigung wegen Zahlungsverzug

## Zweck und Anwendungsfall

Dieser Skill erstellt die fristlose Kündigung wegen Zahlungsverzugs nebst hilfsweiser ordentlicher Kündigung. Anwendungsfall ist ein Wohnraummietverhältnis mit qualifiziertem Rückstand.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Forderungsaufstellung mit Rückstand pro Monatsmiete aus Skill 03.
- Stammdaten und alle Mietvertragspartner aus Skill 01.
- Angabe etwaiger früherer Schonfristzahlungen der letzten zwei Jahre.

## Ablauf / Checkliste

1. Anspruchsgrundlage prüfen: Paragraf 543 Abs. 2 Nr. 3 BGB in Verbindung mit Paragraf 569 Abs. 3 BGB für Wohnraum.
2. Tatbestand prüfen. Variante a: An zwei aufeinander folgenden Terminen ist der Mieter ganz oder zu einem nicht unerheblichen Teil im Verzug; bei Wohnraum ist der rückständige Teil nach Paragraf 569 Abs. 3 Nr. 1 BGB erst dann nicht unerheblich, wenn er eine Monatsmiete übersteigt. Variante b: In einem Zeitraum, der sich über mehr als zwei Termine erstreckt, erreicht der Rückstand die Miete für zwei Monate.
3. Schonfrist nach Paragraf 569 Abs. 3 Nr. 2 BGB beachten: Die Kündigung wird unwirksam, wenn der Vermieter spätestens bis zum Ablauf von zwei Monaten nach Rechtshängigkeit des Räumungsanspruchs hinsichtlich der fälligen Miete und der fälligen Nutzungsentschädigung nach Paragraf 546a Abs. 1 BGB vollständig befriedigt wird oder eine öffentliche Stelle sich hierzu verbindlich verpflichtet. Eine bloße Zahlungsankündigung genügt nicht. Die Schonfrist greift nicht, wenn schon innerhalb der letzten zwei Jahre eine Kündigung nach dieser Vorschrift unwirksam geworden ist. Sie heilt nicht automatisch die ordentliche Kündigung (BGH 23.07.2025 — VIII ZR 287/23; BGH 09.04.2025 — VIII ZR 145/24; BGH 05.10.2022 — VIII ZR 307/21; BGH, Urteil vom 13.10.2021 — VIII ZR 91/20; BGH 16.02.2005 — VIII ZR 6/04). Die Nachzahlung ist bei Verschulden und Erheblichkeit nach Paragraf 573 Abs. 2 Nr. 1 BGB mitzuwürdigen. Eine hilfsweise ordentliche Kündigung nur aufnehmen, wenn ihre Voraussetzungen gesondert geprüft, begründet und freigegeben sind.
4. Schriftform nach Paragraf 568 BGB in Verbindung mit Paragraf 126 BGB wahren. In der Standardpraxis ein eigenhändig unterschriebenes Original zustellen; eine gewöhnliche E-Mail genügt nicht. Soll eine qualifizierte elektronische Form verwendet werden, deren gesetzliche Gleichwertigkeit und Zugang vorab gesondert prüfen.
5. Für den hilfsweise ordentlichen Kündigungszweig den Hinweis nach Paragraf 568 Abs. 2 BGB auf Möglichkeit, Form und Frist des Widerspruchs nach den Paragrafen 574 bis 574b BGB aufnehmen. Zugleich Paragraf 574 Abs. 1 S. 2 BGB prüfen: Liegt ein Grund vor, der zur außerordentlichen fristlosen Kündigung berechtigt, ist die Sozialklausel ausgeschlossen. Das Unterlassen des Hinweises macht die Kündigung nicht unwirksam, ermöglicht einen an sich eröffneten Widerspruch aber nach Paragraf 574b Abs. 2 S. 2 BGB noch im ersten Termin des Räumungsrechtsstreits.
6. Nächster Pflichtskill vor Fristlauf, Räumungsaufforderung oder Räumungsklage: `15-kuendigung-zustellung-nachweis`. Ohne beweisfesten Zugang bleibt die Kündigungsampel gelb oder rot.
7. Vor der Rückstandsschwelle verspätete Kontoeingänge bereinigen: Bei Wohnraummiete zählt Sonnabend für die Zahlungsfrist nicht; bei gedecktem Konto genügt der rechtzeitige Überweisungsauftrag. BGH VIII ZR 129/09, VIII ZR 291/09 und VIII ZR 222/15 prüfen. Eine bloße SAP-Wertstellung nach dem dritten Werktag trägt keine Kündigung.
8. Getrennte Freigabekarte erstellen: alle Mieter, Wohnung, Kündigungsgrund, Rückstandsberechnung, Zahlungsauftrag/Banklauf, fristlose und hilfsweise ordentliche Erklärung, Beendigungstermin, Widerspruchshinweis, Unterschrift und geplanter Zustellweg. Bis zur realen Freigabe Status `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

## Argumentationsstandard

Der Kündigungsgrund muss im Schreiben aus sich heraus verständlich sein. Für jeden kündigungstragenden Monat werden Bruttomiete, Fälligkeit, Zahlung, Anrechnung und Rest ausgewiesen; anschließend wird getrennt erklärt, welche Variante des § 543 Abs. 2 S. 1 Nr. 3 BGB erfüllt ist. Die hilfsweise ordentliche Kündigung erhält eine eigene Tatsachen- und Verschuldenswürdigung und darf nicht nur an die fristlose Erklärung angehängt werden. Kontrollfolge: `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für die mietrechtliche BGH-Kontrollspur siehe `references/gepruefte-bgh-anker-mietrecht.md`.

## Ausgabeformat

Getrennte interne Freigabekarte und Kündigungsschreiben mit fristloser Aussprache, hilfsweise ordentlicher Kündigung mit Frist nach Paragraf 573c BGB, Begründung des Verzugs Monat für Monat, Widerspruchshinweis samt Ausschlussprüfung nach Paragraf 574 Abs. 1 S. 2 BGB, Hinweis auf die Schonfrist nach Paragraf 569 Abs. 3 Nr. 2 BGB, Herausgabeaufforderung und Pflicht-Handoff zu Skill 15 für alle Mietvertragspartner. Das Schreiben wird in vollständigen, ausformulierten Sätzen geliefert; Stichwort-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht).

## Beispiele

- Rückstand von zwei vollen Monatsmieten an aufeinander folgenden Terminen: fristlose Kündigung nach Variante a, hilfsweise ordentlich.
- Jobcenter verpflichtet sich innerhalb der Schonfrist belegbar zur vollständigen Befriedigung von fälliger Miete und fälliger Nutzungsentschädigung: fristlose Kündigung wird unwirksam; die hilfsweise ordentliche Kündigung wird eigenständig weitergeprüft (siehe Skill 27).
