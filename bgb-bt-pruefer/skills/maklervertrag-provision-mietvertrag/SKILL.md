---
name: maklervertrag-provision-mietvertrag
description: "Maklervertrag Provision Mietvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Maklervertrag Provision Mietvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Maklervertrag Provision Mietvertrag** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `maklervertrag-und-provision` | Maklervertrag §§ 652 ff. BGB: Provisionsanspruch, Kausalität, Doppelmakler und Bestellerprinzip. |
| `mietvertrag-grundschema-paragraph-535` | Mietvertrag § 535 BGB: Pflichten, Gebrauchsüberlassung, Kündigung, Kaution und Schönheitsreparaturen. |
| `reisevertrag-pauschalreise` | Reisevertrag §§ 651a ff. BGB und Pauschalreiserichtlinie: Mängel, Abhilfe, Minderung, Rücktritt. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Maklervertrag Provision Mietvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `maklervertrag-und-provision`

**Fokus:** Maklervertrag §§ 652 ff. BGB: Provisionsanspruch, Kausalität, Doppelmakler und Bestellerprinzip.

# Maklervertrag und Provision §§ 652 ff. BGB

## Fachkern: Maklervertrag und Provision §§ 652 ff. BGB
- **Spezialgegenstand:** Maklervertrag und Provision §§ 652 ff. BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Maklerrechtliche Ansprüche prüfen: Entstehung des Provisionsanspruchs nach § 652 BGB, Kausalität zwischen Maklertätigkeit und Hauptvertragsschluss, Verwirkung und Bestellerprinzip bei Wohnraumvermittlung.

## Normanker

- § 652 BGB: Entstehung des Maklerlohnanspruchs (Nachweis oder Vermittlung)
- § 653 BGB: Höhe des Maklerlohns
- § 654 BGB: Verwirkung des Maklerlohns bei vertragswidrigem Verhalten
- § 655 BGB: Herabsetzung des Maklerlohns (bei unverhältnismäßig hoher Provision)
- §§ 2 ff. WoVermG: Bestellerprinzip bei Wohnraumvermittlung (Verbraucherschutz)
- Amtliches BGB: https://www.gesetze-im-internet.de/bgb/

## Intake

- Welche Art von Maklervertrag liegt vor (Wohnraumvermittlung, Gewerbeimmobilien, sonstiges)?
- Wie lautet die Provisionsvereinbarung (Höhe, Fälligkeit, Bedingungen)?
- Wurde der Hauptvertrag tatsächlich geschlossen?
- Besteht eine Kausalverknüpfung zwischen Maklertätigkeit und Vertragsschluss?
- Doppelmakler oder Eigenprovision?

## Prüfraster

1. Maklervertrag: wirksam geschlossen (konkludent möglich nach § 652 BGB)?
2. Tätigkeitsart bestimmen: Nachweis eines Vertragspartners oder Vermittlung des Vertrags
3. Hauptvertrag: geschlossen, wirksam und dem Makler kausal zuzurechnen?
4. Kausalität: Mitursächlichkeit der Maklertätigkeit für den Abschluss des Hauptvertrags
5. Verfristung: Vertragsschluss muss in angemessenem Zeitraum nach Maklertätigkeit erfolgen
6. Verwirkung nach § 654 BGB: Doppelmakler, Interessenkollision, vertragswidrige Bevorzugung der Gegenseite
7. Bestellerprinzip nach WoVermG bei Wohnraummakler: Provision nur vom Auftraggeber (Vermieter)
8. Herabsetzungsrecht nach § 655 BGB bei offensichtlichem Missverhältnis

## Fallstricke

- Kausalität: Eigene Kenntnis des Kaufinteressenten vom Objekt vor Einschaltung des Maklers schließt Provision aus.
- Doppelmaklertätigkeit ohne Einverständnis beider Parteien führt nach § 654 BGB zur Verwirkung der Provision.
- Bei Wohnraumanmietung darf Makler vom Mieter keine Provision verlangen (§ 2 WoVermG); Rückforderungsrecht.
- Alleinauftrag versus einfacher Maklervertrag: Unterschied für Haftung bei Nichtabschluss.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Provisionsanspruch-Analyse (Entstehungsvoraussetzungen, Kausalität)
- Verwirkungs-Risikoprüfung
- Bestellerprinzip-Compliance-Check bei Wohnraum
- Handlungsempfehlung für Makler oder Auftraggeber

## Qualitätsregeln

- Kausalität zwischen Maklertätigkeit und Hauptvertragsschluss immer sachverhaltsnah prüfen.
- WoVermG bei Wohnraumvermittlung immer neben BGB prüfen.
- Doppelmakler-Konstellation aktiv auf Verwirkungsrisiko untersuchen.

## Anschluss-Skills

- geschaeftsbesorgung-auftrag-mandat
- auftrag-und-unentgeltliche-taetigkeit
- vertragstypen-mischvertrag-router
- bt-vertragsentwurf-modellvertrag


## Quellen

- https://www.gesetze-im-internet.de/bgb/__652.html
- https://www.gesetze-im-internet.de/bgb/__654.html
- https://www.gesetze-im-internet.de/wovermg/
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `mietvertrag-grundschema-paragraph-535`

**Fokus:** Mietvertrag § 535 BGB: Pflichten, Gebrauchsüberlassung, Kündigung, Kaution und Schönheitsreparaturen.

# Mietvertrag Grundschema § 535 BGB

## Fachkern: Mietvertrag Grundschema § 535 BGB
- **Spezialgegenstand:** Mietvertrag Grundschema § 535 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Mietvertrag nach § 535 BGB vollständig prüfen: gegenseitige Hauptleistungspflichten, Vertragsgestaltung, Kündigungsrecht und typische AGB-Klauseln in Mietverträgen.

## Normanker

- § 535 BGB: Vertragstypische Pflichten beim Mietvertrag
- §§ 536 ff. BGB: Mängel der Mietsache
- §§ 537 und 538 BGB: Verschlechterung durch vertragsgemäßen Gebrauch
- § 542 BGB: Ende des Mietverhältnisses
- §§ 573 und 574 BGB: Kündigung und Widerspruchsrecht bei Wohnraum
- § 551 BGB: Begrenzung der Mietsicherheit
- § 556d BGB: Mietpreisbremse (Wohnraum)
- § 556g BGB: Rechtsfolgen bei Verstößen gegen Mietpreisbremse

## Intake

- Wohnraum- oder Gewerberaummietvertrag?
- Was ist der konkrete Streitpunkt (Kündigung, Kaution, Schönheitsreparaturen, Mieterhöhung, Mangel)?
- Wer ist Mandant (Vermieter oder Mieter)?
- Gilt die Mietpreisbremse (Ort, Wohnraum, Datum)?
- Welche Fristen laufen (Kündigungsfrist, Widerspruchsfrist)?

## Prüfraster

1. Vertragsschluss: Formerfordernis (Schriftform bei mehr als 1 Jahr § 550 BGB), AGB-Einbeziehung
2. Hauptpflichten des Vermieters: Gebrauchsüberlassung in vertragsgemäßem Zustand (§ 535 Abs. 1 BGB)
3. Hauptpflichten des Mieters: Mietzahlung (§ 535 Abs. 2 BGB), pfleglicher Gebrauch
4. Nebenkosten: Umlage nach Betriebskostenverordnung, formelle Anforderungen Betriebskostenabrechnung
5. Schönheitsreparaturen-Klauseln: AGB-Kontrolle nach §§ 307 ff. BGB (BGH-Linie zu starren Fristen)
6. Kaution: Höchstbetrag § 551 BGB, Anlage auf Treuhandkonto, Rückgabe
7. Kündigung: ordentlich (§§ 568 und 573 BGB) oder außerordentlich (§ 543 BGB); Fristen und Form
8. Mieterhöhung: §§ 558 ff. BGB (ortsübliche Vergleichsmiete), Mietpreisbremse §§ 556d ff. BGB

## Fallstricke

- Schönheitsreparaturklauseln sind häufig nach BGH-Rechtsprechung unwirksam; Prüfung im Einzelfall.
- Formverstoß bei Schriftform (§ 550 BGB) führt zu unbefristetem Mietvertrag mit 1-Jahres-Kündigung.
- Betriebskostenabrechnung muss innerhalb von 12 Monaten nach Abrechnungszeitraum erfolgen (§ 556 Abs. 3 BGB).
- Eigenbedarfskündigung muss konkrete Nutzungsabsicht nennen; Vorspiegelung begründet Schadensersatz.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Mietvertragsstruktur-Checkliste (Pflichten, Form, Nebenkosten, Kündigung)
- AGB-Klausel-Scan (Schönheitsreparaturen, Kaution, Haftung)
- Kündigungsschema (Voraussetzungen, Fristen, Form)
- Risikoampel für Vermieter und Mieter

## Qualitätsregeln

- Wohnraum- und Gewerberaummietrecht unterscheiden; Mietpreisbremse gilt nur bei Wohnraum.
- Schönheitsreparaturklauseln grundsätzlich auf BGH-Wirksamkeit prüfen.
- Betriebskostenabrechnung-Formalia immer mitprüfen.

## Anschluss-Skills

- mietrecht-mangel-minderung
- workflow-fristen-ruecktritt-kuendigung
- bt-vertragsentwurf-modellvertrag
- schnittstelle-bgb-at-methodenlehre-agb

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `reisevertrag-pauschalreise`

**Fokus:** Reisevertrag §§ 651a ff. BGB und Pauschalreiserichtlinie: Mängel, Abhilfe, Minderung, Rücktritt.

# Reisevertrag und Pauschalreise §§ 651a ff. BGB

## Fachkern: Reisevertrag und Pauschalreise §§ 651a ff. BGB
- **Spezialgegenstand:** Reisevertrag und Pauschalreise §§ 651a ff. BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Reiserechtliche Ansprüche nach §§ 651a ff. BGB prüfen: Mangelrüge, Abhilfeverlangen, Minderung, Rücktritt und Schadensersatz bei Pauschalreisen nach der Pauschalreise-RL.

## Normanker

- § 651a BGB: Pauschalreisevertrag (Grundnorm)
- § 651c BGB: Abhilfe bei Reisemängeln
- § 651d BGB: Minderung des Reisepreises
- § 651e BGB: Kündigung des Reisevertrags aus wichtigem Grund
- § 651f BGB: Schadensersatz und Entschädigung wegen nutzlos aufgewendeter Urlaubszeit
- § 651h BGB: Rücktritt vor Reisebeginn
- Richtlinie (EU) 2015/2302: Pauschalreise-RL

## Intake

- Liegt eine Pauschalreise im Sinne des § 651a BGB vor (mindestens zwei verbundene Reiseleistungen)?
- Welche Mängel sind aufgetreten (Hotel, Flug, Transfer, Verpflegung)?
- Wurde Abhilfe verlangt und durch den Reiseveranstalter geleistet?
- Was ist das Ziel (Minderung, Schadensersatz, Rücktritt, Entschädigung)?
- Welche Fristen für Mangelrüge und Klage wurden eingehalten?

## Prüfraster

1. Pauschalreise-Begriff bestimmen: verbundene Reiseleistungen nach § 651a Abs. 2 BGB
2. Reisemangel: Abweichung der tatsächlichen von der vertraglichen Reiseleistung
3. Mangelrüge am Urlaubsort: Voraussetzung für Gewährleistungsansprüche
4. Abhilfeverlangen nach § 651c BGB: Fristsetzung, Zurückweisung berechtigt zur Selbsthilfe
5. Minderung nach § 651d BGB: Herabsetzung des Reisepreises nach Minderungsquote
6. Schadensersatz nach § 651f BGB: Verlorene Urlaubszeit als immaterieller Schaden
7. Kündigung aus wichtigem Grund: erhebliche Beeinträchtigung der Reise (§ 651e BGB)
8. Rücktritt vor Reisebeginn nach § 651h BGB: unvermeidbare außergewöhnliche Umstände
9. Verjährung: § 651j BGB (zwei Jahre ab Rückkehr)

## Fallstricke

- Mangelrüge am Urlaubsort ist keine Formalität; Unterlassen kann Minderungsanspruch reduzieren.
- Entschädigung für nutzlos aufgewendete Urlaubszeit ist Sonderform des immateriellen Schadens.
- COVID-19-Fälle: unvermeidbare außergewöhnliche Umstände nach § 651h Abs. 3 BGB; Rücktrittsrecht für beide Seiten.
- Verbundene Reiseleistungen nach § 651c BGB (neue Kategorie): andere Rechtslage als Pauschalreise.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Mängelübersicht mit Minderungsquoten-Empfehlung
- Anspruchsmatrix (Abhilfe, Minderung, Schadensersatz, Kündigung)
- Fristen-Checkliste (Rüge, Klage, Verjährung)
- Risikoampel

## Qualitätsregeln

- Pauschalreise-Definition immer sorgfältig prüfen; einzelne Reiseleistungen unterliegen allgemeinem Schuldrecht.
- Mangelrüge-Obliegenheit am Urlaubsort dokumentieren.
- Pauschalreise-RL-Umsetzungsstand mitprüfen.

## Anschluss-Skills

- werkvertrag-grundschema-paragraph-631
- schadensrecht-paragraphen-249-253
- workflow-fristen-ruecktritt-kuendigung


## Quellen

- https://www.gesetze-im-internet.de/bgb/__651a.html
- https://www.gesetze-im-internet.de/bgb/__651f.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2302
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
