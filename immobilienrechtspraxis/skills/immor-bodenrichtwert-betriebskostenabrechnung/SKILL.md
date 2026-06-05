---
name: immor-bodenrichtwert-betriebskostenabrechnung
description: "Immor Bodenrichtwert Betriebskostenabrechnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Immor Bodenrichtwert Betriebskostenabrechnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Immor Bodenrichtwert Betriebskostenabrechnung** im Plugin Immobilienrechtspraxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `immor-bodenrichtwert-bewertung-spezial` | Spezialfall Bodenrichtwert und Bewertung im Erb- und Steuerfall: ImmoWertV 2021, Vergleichswertverfahren, Ertragswertverfahren. Pruefraster fuer Finanzamt und Gutachter. |
| `betriebskostenabrechnung-erstellen-asset-management` | Betriebskostenabrechnung im Asset- und Property-Management erstellen: Mietvertragsklauseln, BetrKV-Mapping, WEG- oder Objektbuchhaltung, HeizkostenV, CO2KostAufG, Gewerbe-Vorwegabzug, Vorauszahlungskonto, Versand und Belegpaket. |
| `betriebskostenabrechnung-pruefen-asset-management` | Betriebskostenabrechnung im Immobilienportfolio prüfen: formelle Mindestangaben, Fristen, Umlagefähigkeit, Buchhaltungsabgleich, WEG-zu-Mieter-Übersetzung, Zahlungsbelege, Wirtschaftlichkeit, HeizkostenV, CO2KostAufG und Streitwertkalkulation. |

## Arbeitsweg

Im Plugin Immobilienrechtspraxis gilt für **Immor Bodenrichtwert Betriebskostenabrechnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `immor-bodenrichtwert-bewertung-spezial`

**Fokus:** Spezialfall Bodenrichtwert und Bewertung im Erb- und Steuerfall: ImmoWertV 2021, Vergleichswertverfahren, Ertragswertverfahren. Pruefraster fuer Finanzamt und Gutachter.

# ImmoR: Bodenrichtwert-Bewertung

## Fachkern: ImmoR: Bodenrichtwert-Bewertung
- **Spezialgegenstand:** ImmoR: Bodenrichtwert-Bewertung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `betriebskostenabrechnung-erstellen-asset-management`

**Fokus:** Betriebskostenabrechnung im Asset- und Property-Management erstellen: Mietvertragsklauseln, BetrKV-Mapping, WEG- oder Objektbuchhaltung, HeizkostenV, CO2KostAufG, Gewerbe-Vorwegabzug, Vorauszahlungskonto, Versand und Belegpaket.

# Betriebskostenabrechnung erstellen

## Fachkern: Betriebskostenabrechnung erstellen
- **Spezialgegenstand:** Betriebskostenabrechnung erstellen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe

Dieser Skill erstellt eine vermieterseitige Betriebskostenabrechnung für Immobilienportfolios, Mischobjekte und WEG-Sondereigentum. Er ist für Property Manager, Asset Manager, Rechtsabteilungen und Kanzleien gedacht, die aus Buchhaltung, WEG-Abrechnung, Dienstleisterrechnungen und Mietvertragsdaten eine versandfähige Abrechnung bauen müssen.

## Einstieg

1. Objektart: Wohnraum, Gewerbe, Mischobjekt, WEG-Sondereigentum, Quartier?
2. Abrechnungsjahr, Mietfläche, Leerstände, Nutzerwechsel, Vorauszahlungen.
3. Mietvertragsklauseln: BetrKV-Verweis, konkrete Kostenliste, Pauschale, Umsatzsteueroption, sonstige Betriebskosten.
4. Datenquellen: Buchhaltung, WEG-Jahresabrechnung, Heizkostenabrechnung, CO2-Angaben, Dienstleisterverträge, Zahlungsbelege.
5. Gewünschtes Ergebnis: Einzelabrechnung, Portfoliomatrix, Mieteranschreiben, Belegepaket, Korrekturworkflow.

## Erstellungsschritte

1. **Umlagegrundlage je Mietvertrag** prüfen. Ohne vertragliche Grundlage keine Nachforderung.
2. **Kostenarten-Mapping** nach BetrKV oder Gewerbemietvertrag: Verwaltung, Instandhaltung und Finanzierungskosten aussondern.
3. **WEG-Daten übersetzen**: Verwalterhonorar, Rücklage und Reparaturen nicht in die Mieterabrechnung übernehmen; umlagefähige Positionen neu schlüsseln.
4. **Gewerbe-Vorwegabzug**: Restaurant, Praxis, Laden, Tiefgarage oder Sondernutzung gesondert prüfen.
5. **Heizkosten** nach HeizkostenV gesondert verarbeiten; Kürzungsrisiken bei fehlender Verbrauchserfassung markieren.
6. **CO2-Kosten** nach CO2KostAufG rechnen; Vermieteranteil herausnehmen.
7. **Vorauszahlungskonto** abgleichen: Soll, Ist, Nutzerwechsel, Guthaben, Nachzahlung.
8. **Versand-Qualitygate**: Zugangsnachweis, Abrechnungsfrist, Belegarchiv, Ansprechpartner.

## Rechenmatrix

| Position | Quelle | Umlagegrundlage | Schlüssel | Betrag brutto/netto | Mieteranteil | Belegstatus |
| --- | --- | --- | --- | --- | --- | --- |
| Grundsteuer | Bescheid | Vertrag/BetrKV | Fläche | [...] | [...] | [...] |
| Versicherung | Police/Rechnung | BetrKV | Fläche/MEA | [...] | [...] | [...] |
| Hausmeister | Vertrag/Stunden | BetrKV anteilig | Fläche | [...] | [...] | Split nötig |
| Heizung | Heizkostenabrechnung | HeizkostenV | Verbrauch/Fläche | [...] | [...] | CO2 prüfen |
| Verwalter | WEG | nicht umlagefähig | - | [...] | 0 | herausnehmen |

## Output

- Abrechnung je Mieter mit Saldo.
- Beleg- und Datenraumindex.
- internes Prüfprotokoll "umlagefähig / nicht umlagefähig / offen".
- separates Schreiben zur Vorauszahlungsanpassung nach § 560 Abs. 4 BGB, wenn Wohnraum betroffen ist.

## Quellenregel

§ 556 BGB, § 556a BGB, BetrKV, HeizkostenV und CO2KostAufG aktuell prüfen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## 3. `betriebskostenabrechnung-pruefen-asset-management`

**Fokus:** Betriebskostenabrechnung im Immobilienportfolio prüfen: formelle Mindestangaben, Fristen, Umlagefähigkeit, Buchhaltungsabgleich, WEG-zu-Mieter-Übersetzung, Zahlungsbelege, Wirtschaftlichkeit, HeizkostenV, CO2KostAufG und Streitwertkalkulation.

# Betriebskostenabrechnung prüfen

## Fachkern: Betriebskostenabrechnung prüfen
- **Spezialgegenstand:** Betriebskostenabrechnung prüfen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe

Dieser Skill prüft Betriebskostenabrechnungen für Mieter, Vermieter, Käufer, Verkäufer, Asset Manager und Prozessanwälte. Er verbindet juristische Prüfung mit Datenprüfung: Buchhaltung, Rechnungen, Zahlungsbelege, Mietvertrag und Abrechnung müssen zusammenpassen.

## Einstieg

1. Wer prüft: Eigentümer, Käufer im Due-Diligence-Prozess, Mieter, Verwaltung, Rechtsabteilung?
2. Was ist das Ziel: Zahlung verhindern, Nachforderung sichern, Kaufpreisrisiko bewerten, Musterfehler im Portfolio finden?
3. Welche Abrechnung und welches Jahr? Zugangsnachweis vorhanden?
4. Welche Daten liegen vor: Mietvertrag, Buchhaltung, WEG-Abrechnung, Rechnungen, Zahlungsbelege, Heizkosten, CO2?
5. Gibt es mehrere Einheiten mit gleichem Fehler?

## Prüfblöcke

1. **Form**: Gesamtkosten, Schlüssel, Rechenweg, Vorauszahlungen, Saldo.
2. **Frist**: Abrechnung binnen Jahresfrist zugegangen? Einwendungsfrist offen?
3. **Kostenart**: BetrKV, Gewerbemietvertrag oder Individualabrede.
4. **Belegtiefe**: Rechnungen plus Zahlungsbelege; bei Abflussprinzip Zahlungsfluss besonders wichtig.
5. **Buchhaltungsabgleich**: Kostenstelle, Leistungszeitraum, Zahlung, Storno, Gutschrift.
6. **Wirtschaftlichkeit**: ungewöhnliche Kostensteigerung, verbundene Unternehmen, Rahmenverträge, Doppelbuchung.
7. **Schnittstellen**: WEG-Abrechnung, HeizkostenV, CO2KostAufG, Umsatzsteueroption, Gewerbe-Vorwegabzug.

## Portfolio-Red-Flags

- Verwalterkosten aus WEG-Abrechnung wurden automatisch auf Mieter umgelegt.
- Reparaturanteile in Wartungsverträgen wurden nicht herausgerechnet.
- CO2-Vermieteranteil fehlt.
- Zahlungsbelege zeigen Skonto/Gutschrift, Abrechnung setzt Bruttorechnung an.
- Gewerbeeinheit verursacht Sonderkosten, aber Wohnmieter tragen alles mit.
- Abrechnung wurde nach Frist versendet, aber ohne Zugangsnachweis behauptet.

## Output

- Fehlerliste mit Betrag je Einheit.
- Ampel: sofort korrigieren, verteidigen, vergleichen, Klagerisiko.
- Mieter-/Vermieterschreiben.
- Due-Diligence-Risikoanhang mit Rückstellungsvorschlag.

## Quellenregel

BGH, Urteil vom 09.04.2008 - VIII ZR 84/07, BGH, Urteil vom 09.12.2020 - VIII ZR 118/19 und BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 nur mit frei prüfbarer Quelle zitieren. Keine BeckRS- oder juris-Blindfundstellen.
