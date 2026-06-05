---
name: flug-massenklage-einfuehrung-vo
description: "Flug Massenklage Einfuehrung VO: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Flug Massenklage Einfuehrung VO

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Flug Massenklage Einfuehrung VO** im Plugin Fluggastrechte (VO 261/2004). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `flug-massenklage-prozessfinanzierung-spezial` | Spezialfall Massenklage und Prozessfinanzierung in Fluggastrechten: Abtretung, Inkasso-Modelle, RDG-Grenzen, Anti-Claim-Klausel. Pruefraster fuer Verbraucher und Legal-Tech. |
| `fluggastrechte-einfuehrung-vo-261` | Einfuehrung VO (EG) 261/2004: Anwendungsbereich (Abflug aus EU, Ankunft in EU mit EU-Carrier), Annullierung, Verspaetung ab 3 Stunden (EuGH-Sturgeon), Nichtbefoerderung. Ausgleichsstufen 250 Euro / 400 Euro / 600 Euro. Betreuungsleistungen Art. 9. Erstattungs- vs. Umbuchungswahlrecht. |
| `forderungsschreiben-erste-stufe` | Prüffeld für forderungsschreiben erste stufe: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Fluggastrechte (VO 261/2004) gilt für **Flug Massenklage Einfuehrung VO**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `flug-massenklage-prozessfinanzierung-spezial`

**Fokus:** Spezialfall Massenklage und Prozessfinanzierung in Fluggastrechten: Abtretung, Inkasso-Modelle, RDG-Grenzen, Anti-Claim-Klausel. Pruefraster fuer Verbraucher und Legal-Tech.

# Flug: Massenklage RDG

## Spezialwissen: Flug: Massenklage RDG
- **Spezialgegenstand:** Flug: Massenklage RDG / flug massenklage prozessfinanzierung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** RDG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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

## 2. `fluggastrechte-einfuehrung-vo-261`

**Fokus:** Einfuehrung VO (EG) 261/2004: Anwendungsbereich (Abflug aus EU, Ankunft in EU mit EU-Carrier), Annullierung, Verspaetung ab 3 Stunden (EuGH-Sturgeon), Nichtbefoerderung. Ausgleichsstufen 250 Euro / 400 Euro / 600 Euro. Betreuungsleistungen Art. 9. Erstattungs- vs. Umbuchungswahlrecht.

# Fluggastrechte VO 261: Einfuehrung

## Spezialwissen: Fluggastrechte VO 261: Einfuehrung
- **Spezialgegenstand:** Fluggastrechte VO 261: Einfuehrung / fluggastrechte einfuehrung vo 261. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VO, EG, EU, Art. 9.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `forderungsschreiben-erste-stufe`

**Fokus:** Prüffeld für forderungsschreiben erste stufe: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Forderungsschreiben — Erste Stufe

## Empfänger

- **Operating Carrier** (ausführendes Luftfahrtunternehmen) — Hauptanspruchsgegner nach VO 261/2004.
- **Kundenservice-Postfach** der Airline (in Deutschland regelmäßig im Impressum / AGB der Airline angegeben).
- **Niederlassung in Deutschland** wenn vorhanden (Zustellungsort).

## Struktur

### 1. Briefkopf

```
[Vor- und Nachname Hauptansprechender]
[Strasse Hausnummer]
[PLZ Ort]
[Tel] [E-Mail]

[Datum]

An: [Airline-Name]
 [Kundenservice-Postfach]
 [Adresse]
 [Land]

Betreff: Forderung Ausgleichszahlung gemäß Art. 7 VO (EG) Nr. 261/2004
 Flug [Flugnummer] vom [Datum]
 Buchungscode [PNR]
```

### 2. Sachverhalt knapp

```
Sehr geehrte Damen und Herren,

ich nehme Bezug auf den unter dem Buchungscode [PNR] gebuchten Flug [Flugnummer]
am [Datum] von [Abflughafen] nach [Zielflughafen] mit Ihrer Fluggesellschaft.

Folgende Passagiere waren betroffen:
 - [Name 1], geboren [Datum 1]
 - [Name 2], geboren [Datum 2]
 - [Name 3], geboren [Datum 3] (minderjährig, vertreten durch
 die unterzeichnenden Erziehungsberechtigten)

Vollmachten der Mitreisenden sind beigefuegt (Anlagen K1 K2 ...).

Der genannte Flug wurde durch Sie [annulliert / mit X Stunden Verspätung
durchgeführt / wir wurden trotz gültigem Ticket nicht befoerdert].
```

### 3. Rechtliche Begründung

```
1. Der Anspruch auf Ausgleichszahlung gemäß Art. 7 VO (EG) Nr. 261/2004
folgt aus [Art. 5 (Annullierung) / Art. 6 + EuGH-Rechtsprechung Sturgeon
(Verspätung am Endziel mehr als drei Stunden) / Art. 4 (Nichtbefoerderung)].

2. Der Flug fiel unter den Anwendungsbereich der VO 261/2004 — Abflug aus
einem Mitgliedstaat der Europaeischen Union (Art. 3 Abs. 1 lit. a VO 261/2004).

3. Die Distanz zwischen [Abflughafen] und [Zielflughafen] betraegt nach
Grosskreisrechnung [X] km. Dies entspricht der Stufe [1 / 2 / 3] des
Art. 7 VO 261/2004 mit einem Ausgleichsanspruch in Höhe von [250 / 400 / 600]
EUR pro Passagier.

4. Bei [drei] Passagieren ergibt sich ein Gesamtausgleich von [Gesamtbetrag]
EUR.

5. Eine Befreiung wegen außergewöhnlicher Umstaende gemäß Art. 5 Abs. 3
VO 261/2004 ist nicht ersichtlich. Sie tragen die Beweislast hierfür.
[Falls Airline bereits eine Begründung wie technischer Defekt geliefert hat,
hinzufügen: Technische Defekte sind nach st. Rspr. des EuGH (Urt. v.
22.12.2008, C-549/07 — Wallentin-Hermann; curia.europa.eu) regelmäßig
NICHT als außergewöhnliche Umstaende zu werten.]

[Bei Verspätung am Endziel mehr als drei Stunden bei Anschlussflug:]
6. Maßgeblich ist die Ankunftsverspätung am Endziel der Reise nach EuGH
C-11/11 (Folkerts). Die tatsächliche Ankunft am Endziel erfolgte mit
[X] Stunden Verspätung gegenüber der geplanten Ankunftszeit.
```

### 4. Forderung

```
Hiermit fordere ich Sie auf den Gesamtausgleich in Höhe von [X] EUR sowie
gegebenenfalls Auslagenersatz für [Hotel Verpflegung Telefon] in Höhe von
[Y] EUR — Belege beiliegend — auf folgendes Konto zu überweisen:

 Inhaber: [Name]
 IBAN: DE [...]
 BIC: [...]

bis spaetestens [Datum + 14 Tage].

Bei Nichtzahlung werde ich zur weiteren Geltendmachung die Schlichtungsstelle
für den öffentlichen Personenverkehr (SOEP) anrufen — kostenfrei für
Verbraucher (vgl. § 14 Abs. 1 UKlaG). Bei weiterer Erfolglosigkeit werde ich
Klage zum zuständigen Amtsgericht erheben mit den hieraus folgenden Mehrkosten
(Verzugszinsen Gerichtskosten Anwaltskosten).
```

### 5. Anlagen

```
Anlagen:
 K1 Buchungsbestätigung Flug [Flugnummer] vom [Datum]
 K2 Boardingpaesse aller Passagiere
 K3 Stoerungsmitteilung der Airline (sofern vorhanden)
 K4 Belege Auslagen Hotel Verpflegung Telefon
 K5 Vollmacht [Name Passagier 2]
 K6 Vollmacht [Name Passagier 3]
```

### 6. Schluss

```
Mit freundlichen Grüßen

[Unterschrift]
[Name]
```

## Versand

- **Einschreiben mit Rückschein** — beste Beweisform für Zustellung.
- **E-Mail mit Empfangsbestätigung** an das offizielle Kundenservice-Postfach.
- **Airline-Reklamationsportal** wenn als Eingangsweg vorgesehen — Eingangsnummer dokumentieren.
- Keine Falle: bei einigen Airlines (z. B. Ryanair) ist der ausschließlich vorgegebene Eingangsweg ein Online-Formular; mehrfach versuchen und parallel auch postalisch.

## Verzugszinsen

- Bei Nichtzahlung tritt Verzug spätestens mit Fristablauf ein (§ 286 Abs. 1 BGB).
- Verzugszinsen Verbraucher 5 Prozentpunkte über Basiszinssatz (§ 288 Abs. 1 BGB).
- Bei einer Pauschalreise mit Unternehmer-Stellung kann § 288 Abs. 2 BGB (9 Prozentpunkte) einschlägig sein — selten relevant für Verbraucher.

## Leitentscheidungen Forderungsschreiben (Stand Mai 2026)

Vor Versand jeweils Volltext in curia.europa.eu aufrufen:

- EuGH, Urt. v. 19.11.2009, C-402/07 und C-432/07 (Sturgeon u.a.) — 3-Stunden-Schwelle
- EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — techn. Defekt kein außergewöhnlicher Umstand
- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspätung Anschlussflüge
- EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung als Annullierung
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag

## Ausgabe

- `forderung-erste-stufe-<datum>.docx` und PDF.
- Eintrag in Tagesnotizen — Reaktionsfrist ist vorgemerkt für Mahnung.
- Hinweis: bei Reaktion der Airline auf Fall warten und Skill `airline-standardausreden-pruefen` ausführen.

## Anlagen-Übergabe

Unmittelbar nach Erstellung des Schreibens den Skill `fluggastrechte-anlagen-bauen` aufrufen.

Übergabe-Schema:

```yaml
schriftsatz: forderung-erste-stufe-<datum>.docx
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true # erzeugt zusätzlich Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

Der Skill `fluggastrechte-anlagen-bauen` liest die im Schriftsatz erwähnten Anlagen in Reihenfolge der Erwähnung, konvertiert jede Rohdatei zu PDF, stempelt oben rechts in Arial 12 FETT (= Helvetica-Bold 12pt) den Bezeichner "Anlage K 1", "Anlage K 2" usw. und benennt die Ausgabedatei nach demselben Schema (`Anlage_K_1.pdf`). Optional wird ein Sammel-PDF mit Schriftsatz vorne und durchlaufenden Lesezeichen erzeugt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
