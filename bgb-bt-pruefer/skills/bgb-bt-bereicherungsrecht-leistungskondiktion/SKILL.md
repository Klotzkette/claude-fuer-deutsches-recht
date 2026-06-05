---
name: bgb-bt-bereicherungsrecht-leistungskondiktion
description: "Bereicherungsrecht Leistungskondiktion: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bereicherungsrecht Leistungskondiktion

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bereicherungsrecht Leistungskondiktion** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bereicherungsrecht-leistungskondiktion` | Prüft Leistungskondiktion §§ 812 ff. BGB: Kondiktionstypen, Leistungsbegriff, Rechtsgrund und Subsidiarität. |
| `bereicherungsrecht-nichtleistungskondiktion` | Prüft Nichtleistungskondiktion §§ 812 ff. BGB: Eingriffskondiktion, Rückgriffskondiktion und Verwendungskondiktion. |
| `buergschaft-einreden-und-akzessorietaet` | Prüft Akzessorietät der Bürgschaft, Einreden des Bürgen §§ 768–770 BGB und Auswirkungen von Hauptschuld-Veränderungen. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Bereicherungsrecht Leistungskondiktion**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bereicherungsrecht-leistungskondiktion`

**Fokus:** Prüft Leistungskondiktion §§ 812 ff. BGB: Kondiktionstypen, Leistungsbegriff, Rechtsgrund und Subsidiarität.

# Bereicherungsrecht: Leistungskondiktion

## Fachkern: Bereicherungsrecht: Leistungskondiktion
- **Spezialgegenstand:** Bereicherungsrecht: Leistungskondiktion; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Leistungskondiktionen nach § 812 Abs. 1 BGB systematisch prüfen: condictio indebiti, condictio ob causam finitam, condictio ob rem und Leistungsbegriff nach Zweckbestimmung.

## Normanker

- § 812 Abs. 1 Satz 1 Alt. 1 BGB: condictio indebiti (Leistung ohne Rechtsgrund)
- § 812 Abs. 1 Satz 2 Alt. 1 BGB: condictio ob causam finitam (Rechtsgrund entfällt nachträglich)
- § 812 Abs. 1 Satz 2 Alt. 2 BGB: condictio ob rem (Zweck wird nicht erreicht)
- § 813 BGB: Leistung auf einredebehaftete Forderung
- § 814 BGB: Kenntnis der Nichtschuld (Kondiktionssperre)
- § 815 BGB: Kondiktionssperre bei vorsätzlicher Zweckvereitelung
- § 816 BGB: Nichtberechtigter verfügt wirksam
- § 817 BGB: Leistung zu verbotenem Zweck

## Intake

- Was wurde geleistet (Geld, Sache, Dienstleistung, Grundstück)?
- Bestand ein Rechtsgrund bei Leistung; ist er später entfallen?
- Kannte der Leistende die Nichtschuld (§ 814 BGB)?
- Handelt es sich um eine Leistung zwischen den Parteien oder gegenüber Dritten?
- Welcher Kondiktionstyp ist einschlägig?

## Prüfraster

1. Leistung: bewusste und zweckgerichtete Mehrung fremden Vermögens bestimmen
2. Auf Kosten des Bereicherungsgläubigers: unmittelbare Vermögensverschiebung prüfen
3. Ohne Rechtsgrund (§ 812 Abs. 1 Satz 1 Alt. 1 BGB): fehlender Rechtsgrund bei Leistung
4. Nachträglicher Wegfall (§ 812 Abs. 1 Satz 2 Alt. 1 BGB): Rücktritt, Anfechtung, Bedingungseintritt
5. Zweckverfehlung (§ 812 Abs. 1 Satz 2 Alt. 2 BGB): Zweck nicht eingetreten
6. Kondiktionssperren: §§ 814 und 815 BGB prüfen
7. Höhe: §§ 818 und 819 BGB; Entreicherungseinwand; Herausgabe oder Wertersatz
8. Verjährung: §§ 195 und 199 BGB

## Fallstricke

- § 814 BGB sperrt die condictio indebiti, wenn der Leistende die Nichtschuld kannte.
- Leistungskondiktion hat Vorrang vor Nichtleistungskondiktion im Mehrpersonenverhältnis.
- Nichtigkeit nach § 134 oder § 138 BGB kann zu § 817 Satz 2 BGB und Kondiktionssperre führen.
- Keine Leistungskondiktion, wenn gültiger Rechtsgrund besteht; Anfechtung oder Rücktritt zuerst prüfen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kondiktionstyp-Einordnung
- Anspruchsmatrix mit Höhe und Entreicherungseinwand
- Kondiktionssperren-Checkliste
- Risikoampel und nächste Schritte

## Qualitätsregeln

- Leistungsbegriff immer nach Zweckbestimmung des Leistenden bestimmen.
- Im Mehrpersonenverhältnis Leistungskondiktion vor Nichtleistungskondiktion prüfen.
- § 817 Satz 2 BGB gesondert auf Sittenwidrigkeitsfälle anwenden.

## Anschluss-Skills

- bereicherungsrecht-nichtleistungskondiktion
- bereicherungsrecht-entreicherung-und-saldotheorie
- kaufrecht-sachmangel-paragraph-434
- workflow-anspruchslandkarte

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `bereicherungsrecht-nichtleistungskondiktion`

**Fokus:** Prüft Nichtleistungskondiktion §§ 812 ff. BGB: Eingriffskondiktion, Rückgriffskondiktion und Verwendungskondiktion.

# Bereicherungsrecht: Nichtleistungskondiktion

## Fachkern: Bereicherungsrecht: Nichtleistungskondiktion
- **Spezialgegenstand:** Bereicherungsrecht: Nichtleistungskondiktion; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Nichtleistungskondiktionen systematisch prüfen: Eingriffskondiktion bei unbefugtem Eingriff in fremde Rechtsgüter, Rückgriffskondiktion und Verwendungskondiktion.

## Normanker

- § 812 Abs. 1 Satz 1 Alt. 2 BGB: Nichtleistungskondiktion (in sonstiger Weise)
- § 816 Abs. 1 BGB: Verfügung eines Nichtberechtigten
- § 816 Abs. 2 BGB: Leistung an einen Nichtberechtigten
- § 822 BGB: Herausgabepflicht des unentgeltlichen Erwerbers
- §§ 994–1003 BGB: Verwendungsersatz (Abgrenzung zur Verwendungskondiktion)
- § 687 Abs. 2 BGB: unechte Geschäftsführung ohne Auftrag als Konkurrenz

## Intake

- Hat der Bereicherte durch eigene Handlung oder durch Zufall etwas erlangt?
- Liegt eine unberechtigte Nutzung eines fremden Rechts (Patent, Marke, Grundstück) vor?
- Hat ein Dritter eine Verbindlichkeit des Bereicherten getilgt?
- Wurden Verwendungen auf eine fremde Sache gemacht?
- Ist der Eingriff in einen zugewiesenen Vermögensbereich geschützt?

## Prüfraster

1. Abgrenzung zur Leistungskondiktion: kein bewusster Leistungszweck des Kondiktionsgläubigers
2. Eingriffskondiktion: Eingriff in zugewiesenen Vermögenswert (Eigentum, Immaterialgüterrecht, Persönlichkeitsrecht)
3. Zuweisungsgehalt des Rechts bestimmen: gibt das Recht dem Inhaber das Recht zur Nutzung ausschließlich?
4. Rückgriffskondiktion: Dritter tilgt Schuld des Bereicherten ohne Anweisung
5. Verwendungskondiktion: Aufwendungen auf fremde Sache; Subsidiarität gegenüber § 994 ff. BGB prüfen
6. § 816 BGB: Verfügung eines Nichtberechtigten, die wirksam wird
7. Höhe nach §§ 818 und 819 BGB; Herausgabe oder Wertersatz (Lizenzanalogie)
8. Verjährung: §§ 195 und 199 BGB

## Fallstricke

- Nichtleistungskondiktion scheidet aus, wenn eine Leistungskondiktion zwischen anderen Parteien greift.
- Bei Immaterialgüterrechtsverletzungen kann die Eingriffskondiktion neben Schadensersatz bestehen.
- Verwendungskondiktion ist gegenüber §§ 994 ff. BGB subsidiär; Eigentümer-Besitzer-Verhältnis zuerst prüfen.
- § 822 BGB setzt unentgeltlichen Erwerb voraus; Schenkung von entgeltlicher Weitergabe abgrenzen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kondiktionstyp-Einordnung mit Normverknüpfung
- Wertersatz-Berechnung (Nutzungsherausgabe, Lizenzanalogie)
- Subsidiaritätsprüfung
- Risikoampel und offene Beweisfragen

## Qualitätsregeln

- Zuweisungsgehalt des verletzten Rechts ausdrücklich bestimmen.
- Nichtleistungskondiktion immer nach Prüfung der Leistungskondiktion anwenden.
- Verwendungskondiktion nur nach Abgrenzung zu §§ 994 ff. BGB prüfen.

## Anschluss-Skills

- bereicherungsrecht-leistungskondiktion
- bereicherungsrecht-entreicherung-und-saldotheorie
- deliktsrecht-paragraph-823-1
- goa-grundschema-paragraph-677


## Quellen

- https://www.gesetze-im-internet.de/bgb/__812.html
- https://www.gesetze-im-internet.de/bgb/__816.html
- https://www.gesetze-im-internet.de/bgb/__823.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `buergschaft-einreden-und-akzessorietaet`

**Fokus:** Prüft Akzessorietät der Bürgschaft, Einreden des Bürgen §§ 768–770 BGB und Auswirkungen von Hauptschuld-Veränderungen.

# Bürgschaft: Einreden und Akzessorietät

## Fachkern: Bürgschaft: Einreden und Akzessorietät
- **Spezialgegenstand:** Bürgschaft: Einreden und Akzessorietät; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Akzessorietätsprinzip und Einreden des Bürgen nach §§ 768–770 BGB prüfen: welche Einreden stehen dem Bürgen zu und wie wirken Veränderungen der Hauptschuld auf die Bürgschaft.

## Normanker

- § 765 BGB: Bürgschaftsvertrag (Grundnorm)
- § 767 BGB: Akzessorietät, Umfang der Bürgschaftsschuld
- § 768 BGB: Einreden des Bürgen aus der Hauptschuld
- § 769 BGB: Mitbürgschaft
- § 770 BGB: Einrede der Anfechtbarkeit und Aufrechenbarkeit
- § 771 BGB: Einrede der Vorausklage
- § 772 BGB: Klage gegen Bürgen
- § 776 BGB: Aufgabe von Sicherheiten durch den Gläubiger

## Intake

- Welche Hauptschuld liegt zugrunde und welche Einreden bestehen gegen sie?
- Wurde auf die Einrede der Vorausklage nach § 771 BGB verzichtet (selbstschuldnerische Bürgschaft)?
- Hat der Gläubiger Sicherheiten aufgegeben; greift § 776 BGB?
- Sind mehrere Bürgen vorhanden (Mitbürgschaft nach § 769 BGB)?
- Wurde die Hauptschuld angepasst oder erhöht nach Abschluss des Bürgschaftsvertrags?

## Prüfraster

1. Akzessorietät prüfen: Bürgschaftsschuld folgt Hauptschuld in Entstehung und Erlöschen
2. Einreden aus der Hauptschuld nach § 768 BGB: Verjährung, Anfechtung, Rücktritt
3. Einrede der Anfechtbarkeit nach § 770 Abs. 1 BGB: Bürge kann Einrede solange erheben, wie Hauptschuldner anfechten kann
4. Einrede der Aufrechenbarkeit nach § 770 Abs. 2 BGB: Bürge kann Aufrechnung geltend machen, die dem Hauptschuldner zusteht
5. Einrede der Vorausklage nach § 771 BGB: Voraussetzungen und Verzicht bei selbstschuldnerischer Bürgschaft
6. § 776 BGB: Bürgschaftseinrede bei Aufgabe von Sicherheiten durch den Gläubiger
7. Mitbürgschaft: Innenausgleich nach § 774 Abs. 2 und § 426 BGB
8. Verjährung der Bürgschaftsforderung: § 195 BGB

## Fallstricke

- Selbstschuldnerische Bürgschaft schließt Einrede der Vorausklage aus; § 771 BGB nicht mehr anwendbar.
- § 776 BGB: Aufgabe von Pfandrecht oder anderen Sicherheiten befreit Bürgen nur anteilig.
- Bürgschaftsschuld kann über die ursprüngliche Hauptschuld hinausgehen, wenn Zinsen und Nebenforderungen vereinbart wurden.
- Einreden aus der Hauptschuld sind vom Bürgen eigenständig geltend zu machen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einreden-Matrix (Hauptschuld-Einreden und bürgschaftsspezifische Einreden)
- Akzessorietätsprüfung mit Zeitlinie
- Selbstschuldnerische vs. subsidiäre Bürgschaft: Unterschiede und Rechtsfolgen
- Risikoampel und Handlungsempfehlungen

## Qualitätsregeln

- Akzessorietät immer als Grundsatz voranstellen und Ausnahmen gesondert markieren.
- § 776 BGB-Einrede nur bei tatsächlichem Sicherheitenausfall prüfen.
- Mitbürgschaft-Innenausgleich gesondert behandeln.

## Anschluss-Skills

- buergschaft-grundschema-paragraph-765
- buergschaft-form-und-verbraucherbuerge
- gesamtschuld-und-regress-bgb-bt
- workflow-anspruchslandkarte

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
