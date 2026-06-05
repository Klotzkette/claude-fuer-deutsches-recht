---
name: amtlicher-bgb-auftrag-unentgeltliche
description: "Amtlicher BGB Auftrag Unentgeltliche: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Amtlicher BGB Auftrag Unentgeltliche

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Amtlicher BGB Auftrag Unentgeltliche** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `amtlicher-bgb-bt-normcheck` | Amtlicher Normcheck für BGB-BT-Fälle: prüft Vertragstypen, Leistungsstörung, AGB, Verbraucherrecht, digitale Produkte, Kauf, Miete, Dienst, Werk, Auftrag, GoA, Bürgschaft, Bereicherung und Delikt gegen die aktuelle BGB-Fassung. |
| `auftrag-und-unentgeltliche-taetigkeit` | Prüft Auftrag §§ 662 ff. BGB, Weisungen, Auskunft, Rechenschaft, Aufwendungsersatz, Herausgabe und Kündigung. |
| `bereicherungsrecht-entreicherung-und-saldotheorie` | Prüft Entreicherung § 818 Abs. 3 BGB, Bösgläubigkeit, Saldotheorie und Zweikondiktionenlehre. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Amtlicher BGB Auftrag Unentgeltliche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `amtlicher-bgb-bt-normcheck`

**Fokus:** Amtlicher Normcheck für BGB-BT-Fälle: prüft Vertragstypen, Leistungsstörung, AGB, Verbraucherrecht, digitale Produkte, Kauf, Miete, Dienst, Werk, Auftrag, GoA, Bürgschaft, Bereicherung und Delikt gegen die aktuelle BGB-Fassung.

# Amtlicher BGB-BT-Normcheck

## Zweck

Dieser Skill verhindert, dass BGB-BT-Fälle mit veralteten Normgruppen oder zu groben Anspruchsformeln gelöst werden. Er zwingt den Fall in die aktuelle BGB-Struktur und trennt Vertragstyp, Anspruchsgrundlage, Rechtsfolge, Frist und Beweis.

## Prüfroute

1. Vertragliche Beziehung bestimmen: Kauf, Miete, Darlehen, Dienst, Werk, Auftrag/Geschäftsbesorgung, Bürgschaft, Vergleich oder Mischvertrag.
2. Gesetzliche Beziehung bestimmen: GoA, Bereicherung, Delikt, Gesamtschuld/Regress.
3. BGB AT als Vorfrage prüfen: Vertragsschluss, Form, Stellvertretung, Anfechtung, Verjährung.
4. Aktuelle Norm live prüfen, wenn sie trägt.
5. ZPO-Durchsetzung prüfen, wenn ein Schriftsatz, Mahnbescheid, Eilantrag oder Beweisverfahren entstehen soll.

## Normlandkarte

| Bereich | Normen | Typischer Output |
| --- | --- | --- |
| Leistungsstörung | §§ 241, 249, 253, 275-304 BGB | Pflichtverletzungs- und Schadensmatrix |
| AGB | §§ 305-310 BGB | Klauselampel |
| Verbraucher/Fernabsatz | §§ 312 ff. BGB | Informations-/Widerrufscheck |
| Digitale Produkte | §§ 327 ff. BGB | Bereitstellungs- und Updateprüfung |
| Kauf | §§ 433-479 BGB | Mängelrechte, Nacherfüllung, Rücktritt, Minderung, Schadensersatz |
| Ware mit digitalen Elementen | §§ 475b, 475c, 476, 477 BGB | Update-, Beweislast- und Abweichungsvereinbarung |
| Miete/Pacht | §§ 535 ff., 581 ff. BGB | Gebrauch, Mangel, Minderung, Kündigung, § 550 BGB |
| Dienst/Behandlung | §§ 611, 611a, 630a ff. BGB | Dienstpflicht, Arbeitnehmerabgrenzung, Behandlungsvertrag |
| Werk/Bau | §§ 631 ff. BGB | Abnahme, Mängelrechte, Kündigung, Vergütung |
| Auftrag/Geschäftsbesorgung | §§ 662 ff., 675 ff. BGB | unentgeltlich/entgeltlich, Geschäftsbesorgung, Zahlungsschnittstelle |
| GoA | §§ 677-687 BGB | berechtigte/unberechtigte/unechte GoA |
| Bürgschaft | §§ 765 ff. BGB | Akzessorietät, Schriftform, Einreden |
| Bereicherung | §§ 812-822 BGB | Leistung/Nichtleistung, Rechtsgrund, Entreicherung |
| Delikt | §§ 823-853 BGB | Rechtsgut, Schutzgesetz, § 826, Verrichtungsgehilfe, Gefährdungsnähe |

## Output

Erzeuge:

- Anspruchslandkarte.
- Normenmatrix mit aktueller Normprüfung.
- Rechtsfolgenbaum.
- Fristen- und Verjährungsmatrix.
- ZPO-Durchsetzungspfad, falls der Nutzer ein Prozessprodukt braucht.

## Referenz

Nutze `references/amtlicher-bgb-bt-normkern.md`.

## 2. `auftrag-und-unentgeltliche-taetigkeit`

**Fokus:** Prüft Auftrag §§ 662 ff. BGB, Weisungen, Auskunft, Rechenschaft, Aufwendungsersatz, Herausgabe und Kündigung.

# Auftrag und unentgeltliche Tätigkeit

## Fachkern: Auftrag und unentgeltliche Tätigkeit
- **Spezialgegenstand:** Auftrag und unentgeltliche Tätigkeit; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Auftragsverhältnisse nach §§ 662 ff. BGB prüfen: Unentgeltlichkeit, Weisungsbindung, Aufwendungsersatz und Beendigung durch freie Kündigung.

## Normanker

- § 662 BGB: Auftragsdefinition, Unentgeltlichkeit als Wesensmerkmal
- § 663 BGB: Anzeigepflicht bei Ablehnung
- § 665 BGB: Abweichung von Weisungen
- § 666 BGB: Auskunfts- und Rechenschaftspflicht
- § 667 BGB: Herausgabepflicht
- § 670 BGB: Aufwendungsersatz
- § 671 BGB: Widerruf und Kündigung
- § 672 BGB: Erlöschen des Auftrags bei Tod oder Geschäftsunfähigkeit
- § 675 BGB: Geschäftsbesorgungsvertrag (entgeltlich)

## Intake

- Liegt eine unentgeltliche Geschäftsbesorgung vor oder ist ein Entgelt versprochen?
- Welche Weisungen wurden erteilt und wurden sie befolgt?
- Hat der Beauftragte Auskunft und Rechenschaft erteilt?
- Welche Aufwendungen sind entstanden und wie sind sie belegt?
- Hat der Auftraggeber den Auftrag widerrufen oder der Beauftragte gekündigt?
- Gibt es Herausgabeansprüche (Geld, Dokumente, Erlöse)?

## Prüfraster

1. Abgrenzung: Auftrag (§ 662 BGB) vs. Geschäftsbesorgung (§ 675 BGB) vs. Gefälligkeit
2. Weisungsbindung nach § 665 BGB: Wann darf der Beauftragte abweichen?
3. Auskunfts- und Rechenschaftspflicht nach § 666 BGB: Umfang und Durchsetzung
4. Herausgabepflicht nach § 667 BGB: Was muss herausgegeben werden?
5. Aufwendungsersatz nach § 670 BGB: erforderliche Aufwendungen, Vorschusspflicht
6. Kündigung: Widerruf durch Auftraggeber (§ 671 Abs. 1 BGB) und Kündigung durch Beauftragten (§ 671 Abs. 2 BGB)
7. Schadensersatz bei Pflichtverletzung: §§ 280 und 241 Abs. 2 BGB
8. Verjährung nach §§ 195 und 199 BGB

## Fallstricke

- Entgelt oder Erwartung von Gegenleistung schließt Auftrag aus; dann § 675 BGB prüfen.
- Eigenmächtige Abweichung von Weisungen begründet Schadensersatzpflicht nach § 665 BGB.
- Herausgabepflicht nach § 667 BGB umfasst auch rechtswidrig erlangte Vorteile.
- Freie Kündigung durch den Beauftragten kann nach § 671 Abs. 2 BGB Schadensersatzpflicht auslösen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kurzantwort mit Risikoampel
- Anspruchsmatrix (Aufwendungsersatz, Herausgabe, Schadensersatz)
- Prüfvermerk zum Vertragstypus
- Fristenliste und Lückenkatalog

## Qualitätsregeln

- Abgrenzung Auftrag/Geschäftsbesorgung/Gefälligkeit immer explizit vornehmen.
- Herausgabepflicht und Aufwendungsersatz getrennt prüfen.
- Keine BGH-Entscheidung ohne Live-Verifikation verwenden.

## Anschluss-Skills

- geschaeftsbesorgung-auftrag-mandat
- goa-grundschema-paragraph-677
- unechte-goa-paragraph-687
- geschaeftsbesorgung-und-zahlungsdienste

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `bereicherungsrecht-entreicherung-und-saldotheorie`

**Fokus:** Prüft Entreicherung § 818 Abs. 3 BGB, Bösgläubigkeit, Saldotheorie und Zweikondiktionenlehre.

# Bereicherungsrecht: Entreicherung und Saldotheorie

## Fachkern: Bereicherungsrecht: Entreicherung und Saldotheorie
- **Spezialgegenstand:** Bereicherungsrecht: Entreicherung und Saldotheorie; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Verteidigungsrechte des Bereicherten und die Abwicklung gegenseitiger Leistungen nach §§ 818 und 819 BGB prüfen; Saldotheorie und Zweikondiktionenlehre methodisch sauber einsetzen.

## Normanker

- § 818 Abs. 1–4 BGB: Umfang des Bereicherungsanspruchs
- § 818 Abs. 3 BGB: Wegfall der Bereicherung (Entreicherung)
- § 819 BGB: verschärfte Haftung bei Bösgläubigkeit
- § 820 BGB: Leistung auf unsicheren Rechtsgrund
- §§ 346 ff. BGB: Rücktrittsfolgen (bei Abgrenzung zur Saldotheorie)
- BGH-Rechtsprechung zur Saldo- und Zweikondiktionenlehre: nur nach Live-Prüfung zitieren

## Intake

- Was hat der Bereicherte tatsächlich erlangt und was davon noch bei ihm vorhanden?
- Hat er Aufwendungen im Vertrauen auf den Bestand des Erlangten gemacht?
- Wann und wie erlangte er Bösgläubigkeit im Sinne des § 819 BGB?
- Liegt ein gegenseitiger Vertrag vor, der nach Rücktritt oder Nichtigkeit rückabgewickelt wird?
- Soll die Saldotheorie oder die Zweikondiktionenlehre angewandt werden?

## Prüfraster

1. Entreicherungseinwand nach § 818 Abs. 3 BGB: Was ist noch vorhanden?
2. Entreicherung durch Verbrauch, Verlust, Weitergabe oder vergebliche Aufwendungen?
3. Bösgläubigkeit nach § 819 BGB: Zeitpunkt und Umfang der Kenntniserlangung
4. Verschärfte Haftung nach § 819 Abs. 1 BGB: Pflicht zur Herausgabe wie Besitzer nach § 292 BGB
5. Saldotheorie bei gescheiterten gegenseitigen Verträgen: Saldierung der gegenseitigen Leistungspflichten
6. Zweikondiktionenlehre: beide Seiten haben eigenständige Kondiktionsansprüche
7. Anwendungsbereich abgrenzen: Saldotheorie nur bei nichtigen Verträgen, nicht bei § 817 Satz 2 BGB
8. Verjährung nach §§ 195 und 199 BGB

## Fallstricke

- Entreicherungseinwand scheidet aus, wenn der Bereicherte bösgläubig war (§ 819 BGB).
- Die Saldotheorie schützt den Entreicherten, kann aber zur vollständigen Haftung bei Unmöglichkeit führen.
- Bei § 817 Satz 2 BGB (sittenwidrige Leistung) greift die Saldotheorie nach h.M. nicht.
- Keine der Theorien ohne Prüfung der konkreten Fallkonstellation pauschal anwenden.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Entreicherungsmatrix mit Belegen
- Saldotheorie-Rechenweg oder Zweikondiktionenlehre-Prüfung
- Bösgläubigkeitszeitlinie
- Risikoampel und Lückenliste

## Qualitätsregeln

- Entreicherung und Bösgläubigkeit immer zeitlich verankern.
- Saldotheorie und Zweikondiktionenlehre nicht mischen; Wahl begründen.
- Keine BGH-Formeln ohne Live-Verifikation übernehmen.

## Anschluss-Skills

- bereicherungsrecht-leistungskondiktion
- bereicherungsrecht-nichtleistungskondiktion
- schadensrecht-paragraphen-249-253
- workflow-beweislast-und-belegmatrix


## Quellen

- https://www.gesetze-im-internet.de/bgb/__818.html
- https://www.gesetze-im-internet.de/bgb/__817.html
- https://www.gesetze-im-internet.de/bgb/__816.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
