---
name: geschaeftsbesorgung-zahlungsdienste-goa
description: "Geschaeftsbesorgung Zahlungsdienste GOA: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geschaeftsbesorgung Zahlungsdienste GOA

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Geschaeftsbesorgung Zahlungsdienste GOA** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `geschaeftsbesorgung-und-zahlungsdienste` | Prüft Zahlungsdienstleistungen § 675c ff. BGB: Zahlungsauftrag, Haftung bei Fehlüberweisungen und unautorisierter Zahlung. |
| `goa-entgegenstehender-wille-paragraphen-678-679` | Prüft GoA gegen den Willen des Geschäftsherrn §§ 678 und 679 BGB: erhöhte Haftung und Ausnahmen bei Erfüllung gesetzlicher Pflichten. |
| `goa-grundschema-paragraph-677` | Prüft Geschäftsführung ohne Auftrag §§ 677 ff. BGB: echte GoA, Fremdgeschäftsführungswille, Aufwendungsersatz und Herausgabepflicht. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Geschaeftsbesorgung Zahlungsdienste GOA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `geschaeftsbesorgung-und-zahlungsdienste`

**Fokus:** Prüft Zahlungsdienstleistungen § 675c ff. BGB: Zahlungsauftrag, Haftung bei Fehlüberweisungen und unautorisierter Zahlung.

# Geschäftsbesorgung und Zahlungsdienste

## Fachkern: Geschäftsbesorgung und Zahlungsdienste
- **Spezialgegenstand:** Geschäftsbesorgung und Zahlungsdienste; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Zahlungsdienstrecht nach §§ 675c–676c BGB prüfen: Zahlungsaufträge, Erstattungsansprüche bei unautorisierter Zahlung und Haftung bei Fehlüberweisungen.

## Normanker

- §§ 675c–676c BGB: Zahlungsdienstrecht (Umsetzung der PSD2)
- § 675j BGB: Autorisierung von Zahlungsvorgängen
- § 675u BGB: Erstattungsanspruch bei nicht autorisiertem Zahlungsvorgang
- § 675v BGB: Haftung des Zahlungsdienstnutzers bei unautorisierten Zahlungen
- § 675w BGB: Nachweis der Autorisierung
- § 676a BGB: Ausführungsfrist
- ZAG: Zahlungsdiensteaufsichtsgesetz als öffentlich-rechtlicher Rahmen

## Intake

- Wurde ein Zahlungsvorgang ohne Autorisierung des Zahlers ausgeführt?
- Hat der Zahlungsdienstleister die Transaktion ordnungsgemäß ausgeführt?
- Liegt ein Betrugsfall (Phishing, SIM-Swap) oder ein technischer Fehler vor?
- Wann wurde der nicht autorisierte Zahlungsvorgang bemerkt und gemeldet?
- Hat der Zahlungsnutzer grob fahrlässig oder vorsätzlich gehandelt?

## Prüfraster

1. Autorisierung nach § 675j BGB: hat der Zahler zugestimmt (ausdrücklich oder konkludent)?
2. Nicht autorisierter Zahlungsvorgang: Erstattungsanspruch nach § 675u BGB
3. Haftungsverteilung nach § 675v BGB: grobe Fahrlässigkeit oder Vorsatz des Nutzers?
4. Nachweis der Autorisierung nach § 675w BGB: beweisrechtliche Stellung des Zahlungsdienstleisters
5. Korrekte Ausführung: hat Bank richtige IBAN und richtigen Betrag ausgeführt?
6. Fehlüberweisung: Rückrufverfahren und Schadensersatz
7. Meldefrist für nicht autorisierte Zahlungen: 13 Monate nach Belastung
8. Verjährung: § 195 BGB

## Fallstricke

- Bank muss bei Erstattungsanspruch nach § 675u BGB sofort erstatten, sofern kein Betrugsnachweis.
- Grobe Fahrlässigkeit des Nutzers (PIN-Weitergabe) schließt Erstattungsanspruch nach § 675v Abs. 3 BGB aus.
- Nachweis der Autorisierung liegt nach § 675w BGB beim Zahlungsdienstleister.
- Fehlüberweisung auf falsche IBAN: Bank haftet nur bei eigener Pflichtverletzung.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Autorisierungs-Analyse mit Beweislastprüfung
- Erstattungsanspruch-Berechnung
- Haftungsverteilung Nutzer/Bank
- Fristen- und Meldekalender

## Qualitätsregeln

- Autorisierungs-Nachweis nach § 675w BGB immer auf Bank legen.
- Grobe Fahrlässigkeit des Nutzers nur bei klarem Pflichtenverstoß bejahen.
- PSD2-Umsetzung in nationales Recht immer aktuell prüfen.

## Anschluss-Skills

- geschaeftsbesorgung-auftrag-mandat
- darlehen-und-finanzierung
- schnittstelle-bgb-at-methodenlehre-agb
- workflow-livequellen-rechtsstand


## Quellen

- https://www.gesetze-im-internet.de/bgb/__675.html
- https://www.gesetze-im-internet.de/bgb/__675c.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L2366
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `goa-entgegenstehender-wille-paragraphen-678-679`

**Fokus:** Prüft GoA gegen den Willen des Geschäftsherrn §§ 678 und 679 BGB: erhöhte Haftung und Ausnahmen bei Erfüllung gesetzlicher Pflichten.

# GoA: Entgegenstehender Wille §§ 678 und 679 BGB

## Fachkern: GoA: Entgegenstehender Wille §§ 678 und 679 BGB
- **Spezialgegenstand:** GoA: Entgegenstehender Wille §§ 678 und 679 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Geschäftsführung gegen den Willen des Geschäftsherrn nach §§ 678 und 679 BGB prüfen: erhöhte Haftung des Geschäftsführers und Ausnahme bei gesetzlicher Pflicht oder Notfall.

## Normanker

- § 677 BGB: Pflichten des Geschäftsführers
- § 678 BGB: Übernahme gegen den Willen des Geschäftsherrn (erhöhte Haftung)
- § 679 BGB: Ausnahmen vom entgegenstehenden Willen (Pflicht liegt im öffentlichen Interesse oder gesetzliche Unterhaltspflicht)
- § 680 BGB: Geschäftsführung zur Gefahrenabwehr
- § 683 BGB: Aufwendungsersatz bei berechtigter GoA
- § 684 BGB: Bereicherungsanspruch bei unberechtigter GoA

## Intake

- Hat der Geschäftsführer von einem entgegenstehenden Willen des Geschäftsherrn gewusst oder musste er davon ausgehen?
- War der entgegenstehende Wille nach § 679 BGB unbeachtlich (Erfüllung gesetzlicher Pflicht, Notfall)?
- Liegt eine Geschäftsführung zur Abwehr einer dringenden Gefahr nach § 680 BGB vor?
- Welche Aufwendungen sind entstanden und wer soll sie ersetzen?

## Prüfraster

1. GoA-Grundschema: fremdes Geschäft, Fremdgeschäftsführungswille, ohne Auftrag oder Berechtigung
2. Entgegenstehender Wille des Geschäftsherrn: ausdrücklich oder konkludent; Kenntnis des Geschäftsführers
3. Erhöhte Haftung nach § 678 BGB: auch für Zufall, wenn entgegenstehender Wille bekannt war
4. Ausnahmen nach § 679 BGB: öffentlich-rechtliche Pflicht, gesetzliche Unterhaltspflicht des Geschäftsherrn
5. Gefahrenabwehr nach § 680 BGB: nur Haftung für Vorsatz und grobe Fahrlässigkeit
6. Aufwendungsersatz: bei berechtigter GoA (§ 683 BGB); bei unberechtigter nur Bereicherungsanspruch (§ 684 BGB)
7. Herausgabepflicht des Geschäftsführers nach § 681 BGB
8. Verjährung: §§ 195 und 199 BGB

## Fallstricke

- Erhöhte Haftung nach § 678 BGB greift nur bei Kenntnis oder Kennenmüssen des entgegenstehenden Willens.
- § 679 BGB ist restriktiv auszulegen; bloße Nützlichkeit der Handlung genügt nicht.
- Gefahrenabwehr nach § 680 BGB setzt unmittelbare Gefahr für Person oder Sache voraus.
- Aufwendungsersatz nach § 684 BGB ist ein Bereicherungsanspruch, kein Schadensersatz.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- GoA-Berechtigung-Analyse
- Haftungsumfang (erhöhte Haftung nach § 678 BGB)
- Aufwendungsersatz-Berechnung
- Risikoampel

## Qualitätsregeln

- Entgegenstehenden Willen immer vor Prüfung der Rechtsfolgen feststellen.
- § 679 BGB-Ausnahmen restriktiv auslegen.
- § 680 BGB-Gefahrenabwehr als eigenständigen Tatbestand prüfen.

## Anschluss-Skills

- goa-grundschema-paragraph-677
- unechte-goa-paragraph-687
- auftrag-und-unentgeltliche-taetigkeit
- bereicherungsrecht-leistungskondiktion


## Quellen

- https://www.gesetze-im-internet.de/bgb/__678.html
- https://www.gesetze-im-internet.de/bgb/__679.html
- https://www.gesetze-im-internet.de/bgb/__677.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `goa-grundschema-paragraph-677`

**Fokus:** Prüft Geschäftsführung ohne Auftrag §§ 677 ff. BGB: echte GoA, Fremdgeschäftsführungswille, Aufwendungsersatz und Herausgabepflicht.

# GoA Grundschema § 677 BGB

## Fachkern: GoA Grundschema § 677 BGB
- **Spezialgegenstand:** GoA Grundschema § 677 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Echte Geschäftsführung ohne Auftrag nach §§ 677 ff. BGB vollständig prüfen: Tatbestandsmerkmale, berechtigte GoA und Rechtsfolgen.

## Normanker

- § 677 BGB: Pflichten des Geschäftsführers
- § 678 BGB: Geschäftsführung gegen den Willen des Geschäftsherrn
- § 679 BGB: Unbeachtlichkeit des entgegenstehenden Willens
- § 680 BGB: Geschäftsführung zur Gefahrenabwehr
- § 681 BGB: Benachrichtigungs- und Herausgabepflicht
- § 682 BGB: Haftung des Geschäftsführers
- § 683 BGB: Aufwendungsersatz bei berechtigter GoA
- § 684 BGB: Herausgabe bei unberechtigter GoA (Bereicherungsrecht)

## Intake

- Hat jemand ein Geschäft für einen anderen geführt ohne Auftrag oder sonstige Berechtigung?
- Lag ein Fremdgeschäftsführungswille vor (Wille, für einen anderen zu handeln)?
- War die Übernahme im Interesse und nach dem wirklichen oder mutmaßlichen Willen des Geschäftsherrn?
- Welche Aufwendungen sind entstanden und wie sind sie belegt?
- Ist die Geschäftsführung beendet oder noch im Gange?

## Prüfraster

1. Fremdgeschäft: Abgrenzung eigenes/fremdes/auch-fremdes Geschäft
2. Fremdgeschäftsführungswille: subjektives Element, für einen anderen zu handeln
3. Keine Berechtigung: kein Auftrag, keine gesetzliche Pflicht, kein behördlicher Auftrag
4. Berechtigte GoA (§ 683 BGB): Geschäft entspricht Interesse und Willen des Geschäftsherrn
5. Aufwendungsersatz nach § 683 BGB: notwendige Aufwendungen
6. Herausgabepflicht nach § 681 Satz 2 in Verbindung mit § 667 BGB
7. Unberechtigte GoA: kein Aufwendungsersatz; nur Bereicherungsanspruch nach § 684 BGB
8. Haftung des Geschäftsführers nach § 677 BGB: Pflicht zur ordnungsgemäßen Führung

## Fallstricke

- Auch-fremdes Geschäft reicht für GoA aus, wenn der Fremdgeschäftsführungswille vorhanden ist.
- Auferlegte Handlung (z.B. Pflicht kraft Gesetzes) schließt GoA aus.
- Unberechtigte GoA gibt nur Bereicherungsanspruch, keinen Aufwendungsersatz.
- Fremdgeschäftsführungswille muss nach außen erkennbar sein, nicht nur innerlich vorhanden.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- GoA-Tatbestand-Prüfung
- Berechtigung/Unberechtigung der GoA
- Aufwendungsersatz-Berechnung
- Handlungsempfehlung

## Qualitätsregeln

- Fremdgeschäft und Fremdgeschäftsführungswille immer getrennt prüfen.
- Berechtigte und unberechtigte GoA führen zu unterschiedlichen Rechtsfolgen.
- Herausgabepflicht nach § 681 Satz 2 BGB explizit ansprechen.

## Anschluss-Skills

- goa-entgegenstehender-wille-paragraphen-678-679
- unechte-goa-paragraph-687
- auftrag-und-unentgeltliche-taetigkeit
- bereicherungsrecht-leistungskondiktion

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
