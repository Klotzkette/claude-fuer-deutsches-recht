---
name: delikt-vertrag-dienstvertrag
description: "Delikt Vertrag Dienstvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Delikt Vertrag Dienstvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Delikt Vertrag Dienstvertrag** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `delikt-vertrag-konkurrenz` | Prüft das Verhältnis von vertraglicher und deliktischer Haftung: Konkurrenz, Anspruchskumulation und Verjährungsunterschiede. |
| `dienstvertrag-und-behandlungsvertrag` | Prüft Dienstvertrag §§ 611 ff. BGB und Behandlungsvertrag §§ 630a ff. BGB: Aufklärung, Dokumentation und Arzthaftung. |
| `kaufvertrag-grundschema-paragraph-433` | Kaufvertrag § 433 BGB: Primär- und Sekundäransprüche, Übergabe, Eigentumsverschaffung, AGB und Verbraucherschutz. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Delikt Vertrag Dienstvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `delikt-vertrag-konkurrenz`

**Fokus:** Prüft das Verhältnis von vertraglicher und deliktischer Haftung: Konkurrenz, Anspruchskumulation und Verjährungsunterschiede.

# Delikt-Vertrag Konkurrenz

## Fachkern: Delikt-Vertrag Konkurrenz
- **Spezialgegenstand:** Delikt-Vertrag Konkurrenz; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Das Konkurrenzverhältnis von vertraglichem Schadensersatz (§ 280 BGB) und Deliktsrecht (§ 823 BGB) prüfen: Anspruchskumulation, Wahlrecht und abweichende Verjährungsfristen.

## Normanker

- § 280 Abs. 1 BGB: vertraglicher Schadensersatz
- § 823 Abs. 1 und Abs. 2 BGB: deliktischer Schadensersatz
- § 241 Abs. 2 BGB: Schutzpflichten im Schuldverhältnis
- § 278 BGB: Haftung für Erfüllungsgehilfen (vertragliche Seite)
- § 831 BGB: Haftung für Verrichtungsgehilfen (deliktische Seite)
- §§ 195 und 199 BGB: dreijährige Verjährungsfrist (Delikt und Vertrag gleich)
- § 852 BGB: Herausgabeanspruch nach Deliktsrecht, längere Sonderregel

## Intake

- Bestand ein Vertrag zwischen den Parteien, und wurde er durch dieselbe Handlung verletzt?
- Welcher Anspruch soll vorrangig geltend gemacht werden?
- Gibt es Unterschiede bei Verjährung, Beweislast oder Haftungsumfang?
- Greift § 278 BGB (Erfüllungsgehilfe) oder § 831 BGB (Verrichtungsgehilfe)?
- Sind Dritte geschädigt, die keinen Vertrag haben?

## Prüfraster

1. Vertraglicher Schadensersatzanspruch nach § 280 Abs. 1 BGB: Schuldverhältnis, Pflichtwidrigkeit, Vertretenmüssen
2. Deliktischer Schadensersatz nach § 823 BGB: Rechtsgutsverletzung, Handlung, Rechtswidrigkeit, Verschulden
3. Anspruchskumulation: beide Ansprüche können nebeneinander bestehen
4. Beweislast: bei § 280 BGB vermutet, bei § 823 BGB liegt Beweislast beim Geschädigten
5. Gehilfenhaftung: § 278 BGB (kein Exkulpationsmöglichkeit) vs. § 831 BGB (Exkulpation möglich)
6. Verjährung: beide Ansprüche verjähren nach §§ 195 und 199 BGB, aber § 852 BGB verlängert Deliktsanspruch nach Verjährung
7. Drittschadensliquidation bei mittelbaren Geschädigten
8. Haftungsausschlüsse: vertragliche Haftungsfreizeichnung wirkt nur für Vertragspartner

## Fallstricke

- Vertraglicher Haftungsausschluss beseitigt nicht die deliktische Haftung gegenüber Dritten.
- Beweislast ist unterschiedlich: § 280 BGB favorisiert den Gläubiger, § 823 BGB den Schuldner.
- § 852 BGB verlängert Deliktsanspruch nach Verjährung auf zehn Jahre in Bereicherungsform.
- Gehilfenhaftung nach § 278 BGB ist strenger als nach § 831 BGB (keine Exkulpation möglich).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Anspruchsvergleich (vertraglich vs. deliktisch) mit Vor- und Nachteilen
- Beweislast-Matrix
- Verjährungskalender
- Handlungsempfehlung (welcher Anspruch vorrangig?)

## Qualitätsregeln

- Immer beide Anspruchsgrundlagen prüfen und vergleichen.
- § 278 BGB und § 831 BGB immer parallel prüfen.
- § 852 BGB nicht vergessen bei bereits verjährten Deliktsansprüchen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- schadensrecht-paragraphen-249-253
- delikt-organisationspflicht
- workflow-anspruchslandkarte


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__280.html
- https://www.gesetze-im-internet.de/bgb/__241.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `dienstvertrag-und-behandlungsvertrag`

**Fokus:** Prüft Dienstvertrag §§ 611 ff. BGB und Behandlungsvertrag §§ 630a ff. BGB: Aufklärung, Dokumentation und Arzthaftung.

# Dienstvertrag und Behandlungsvertrag

## Fachkern: Dienstvertrag und Behandlungsvertrag
- **Spezialgegenstand:** Dienstvertrag und Behandlungsvertrag; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Behandlungsvertragsrecht nach §§ 630a–630h BGB prüfen: Aufklärungspflichten, Einwilligung, Dokumentation, Beweislast und Haftung bei Behandlungsfehlern.

## Normanker

- §§ 630a–630h BGB: Behandlungsvertrag (Kodifizierung der Arzthaftung)
- § 630a BGB: Vertragstypische Pflichten, Behandlungsstandard
- § 630b BGB: Anwendung von Dienstvertragsrecht
- § 630c BGB: Informationspflichten
- § 630d BGB: Einwilligung des Patienten
- § 630e BGB: Aufklärungspflichten
- § 630f BGB: Dokumentationspflicht
- § 630g BGB: Einsichtsrecht in Patientenakte
- § 630h BGB: Beweislast bei Behandlungsfehlern

## Intake

- Welche Behandlung wurde durchgeführt oder unterlassen?
- Hat der Behandelnde den medizinischen Standard eingehalten (§ 630a Abs. 2 BGB)?
- Wurde die Einwilligung wirksam nach § 630d BGB erteilt; lag vollständige Aufklärung vor?
- Ist die Behandlung dokumentiert; bestehen Dokumentationslücken?
- Liegt ein einfacher oder grober Behandlungsfehler vor?

## Prüfraster

1. Behandlungsvertrag: Parteien, Gegenstand, Standardleistung nach § 630a Abs. 2 BGB
2. Einwilligung und Aufklärung: § 630d und § 630e BGB vollständig prüfen
3. Behandlungsfehler: Abweichung vom geschuldeten medizinischen Standard
4. Einfacher vs. grober Behandlungsfehler: grober Fehler kehrt Beweislast nach § 630h Abs. 5 BGB um
5. Dokumentationspflicht nach § 630f BGB: fehlende Dokumentation führt zu Beweislastnachteil nach § 630h Abs. 3 BGB
6. Kausalität: Behandlungsfehler hat Gesundheitsschaden verursacht
7. Schadensersatz und Schmerzensgeld nach §§ 280 und 823 BGB in Verbindung mit §§ 249 ff. BGB
8. Verjährung: §§ 195 und 199 BGB (Kenntniserlangung vom Fehler)

## Fallstricke

- Aufklärung und Einwilligung sind eigenständige Haftungsgrundlagen (keine Heilung durch guten Behandlungserfolg).
- Grober Behandlungsfehler kehrt die Kausalitätsbeweislast um (Patient muss Kausalität nicht beweisen).
- Dokumentationslücken wirken zu Lasten des Behandelnden.
- Für Arzthaftung gilt Verjährungsfrist ab Kenntniserlangung des Patienten vom Fehler.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Aufklärungs- und Einwilligungs-Checkliste
- Behandlungsfehler-Analyse (einfach vs. grob)
- Beweislastmatrix
- Schadensberechnung und Risikoampel

## Qualitätsregeln

- Aufklärungsfehler und Behandlungsfehler immer getrennt prüfen.
- § 630h BGB-Beweislastnormen vollständig auflisten.
- Dokumentation als eigenständigen Haftungsbereich behandeln.

## Anschluss-Skills

- arbeitsnaher-dienstvertrag-bgb
- werk-dienst-abgrenzung-erfolg
- deliktsrecht-paragraph-823-1
- workflow-beweislast-und-belegmatrix

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `kaufvertrag-grundschema-paragraph-433`

**Fokus:** Kaufvertrag § 433 BGB: Primär- und Sekundäransprüche, Übergabe, Eigentumsverschaffung, AGB und Verbraucherschutz.

# Kaufvertrag Grundschema § 433 BGB

## Fachkern: Kaufvertrag Grundschema § 433 BGB
- **Spezialgegenstand:** Kaufvertrag Grundschema § 433 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Den Kaufvertrag nach § 433 BGB vollständig prüfen: Vertragsschluss, gegenseitige Hauptleistungspflichten (Übergabe, Eigentumsverschaffung, Kaufpreiszahlung), Pflichtverletzung und Sekundäransprüche.

## Normanker

- § 433 BGB: Vertragstypische Pflichten beim Kaufvertrag
- § 434 BGB: Sachmangel (subjektive, objektive und Montageanforderungen)
- § 437 BGB: Rechte des Käufers bei Mängeln
- § 439 BGB: Nacherfüllung
- §§ 440 und 441 BGB: Rücktritt und Minderung
- § 442 BGB: Kenntnis des Käufers
- §§ 474 ff. BGB: Verbrauchsgüterkauf
- §§ 305 ff. BGB: AGB-Kontrolle
- § 476 BGB: Abweichende Vereinbarungen

## Intake

- Wer sind die Vertragsparteien (Verbraucher, Unternehmer, Privatperson)?
- Was ist der Kaufgegenstand (bewegliche Sache, Grundstück, digitale Ware)?
- Wurde der Vertrag wirksam geschlossen (Angebot, Annahme, Form)?
- Welche Mängel werden gerügt und zu welchem Zeitpunkt sind sie aufgetreten?
- Welches Arbeitsprodukt wird benötigt (Mängelrüge, Klage, Verhandlung)?

## Prüfraster

1. Vertragsschluss: Angebot und Annahme, Formerfordernis bei Grundstücken (§ 311b BGB), AGB-Einbeziehung
2. Pflichten des Verkäufers: Übergabe und Eigentumsverschaffung (§ 433 Abs. 1 BGB); mangelfreie Sache
3. Pflichten des Käufers: Kaufpreiszahlung und Abnahme (§ 433 Abs. 2 BGB)
4. Gefahrübergang nach § 446 BGB (Übergabe) oder § 447 BGB (Versendungskauf)
5. Sachmangel nach § 434 BGB: subjektive, objektive Anforderungen, Montagemangel
6. Rechtsmangel nach § 435 BGB
7. Käuferrechte nach § 437 BGB: Nacherfüllung, Rücktritt, Minderung, Schadensersatz
8. Verjährung nach §§ 438 und 195 ff. BGB; Ausschluss nach § 442 BGB
9. Verbrauchsgüterkauf-Sonderregeln §§ 474 ff. BGB und Beweislastumkehr § 477 BGB

## Fallstricke

- Gefahrübergang und Mangelentstehungszeitpunkt genau bestimmen; bei Versendungskauf gilt § 447 BGB.
- Kenntnis des Mangels bei Vertragsschluss führt nach § 442 BGB zum Ausschluss der Mängelrechte.
- AGB-Klauseln zu Gewährleistungsausschluss zwischen Unternehmern können wirksam sein; gegenüber Verbrauchern nicht.
- Nacherfüllungsrecht des Verkäufers muss vor Rücktritt gewährt werden (§§ 437 Nr. 2 und 440 BGB).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vertragsstruktur-Übersicht (Parteien, Gegenstand, Pflichten)
- Mängelprüfungsschema (subjektiv, objektiv, Montagemangel)
- Käufer-Rechte-Matrix nach § 437 BGB
- Risikoampel und Empfehlung

## Qualitätsregeln

- Kaufgegenstand-Qualifikation (beweglich, Grundstück, digital) immer als ersten Schritt klären.
- Gefahrübergang und Mangelentstehungszeitpunkt sauber dokumentieren.
- Nacherfüllungsrecht des Verkäufers als Voraussetzung für Rücktritt immer prüfen.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung
- kaufrecht-beweislast-verjaehrung-digitale-elemente
- verbrauchsgueterkauf-digitales

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
