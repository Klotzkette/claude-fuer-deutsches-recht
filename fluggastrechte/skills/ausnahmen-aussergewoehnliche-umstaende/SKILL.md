---
name: ausnahmen-aussergewoehnliche-umstaende
description: "Ausnahmen Aussergewoehnliche Umstaende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ausnahmen Aussergewoehnliche Umstaende

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ausnahmen Aussergewoehnliche Umstaende** im Plugin Fluggastrechte (VO 261/2004). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ausnahmen-aussergewoehnliche-umstaende-pruefen` | Prüffeld für ausnahmen aussergewoehnliche umstaende pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `aussergewoehnliche-umstaende-strikt` | Streng auszulegende aussergewoehnliche Umstaende Art. 5 Abs. 3 VO 261: Wetter, Streik nicht eigener Mitarbeiter, gerichtlich verfuegte Flugverbote, Wildschlag in Triebwerk. Keine aussergewoehnlichen Umstaende: technische Defekte (EuGH Wallentin-Hermann), Krankheit Crew, ATC-Engpaesse mit Routine. Pruefraster mit Belegen. |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich oder 1500 bis 3500 km nicht-innergemeinschaftlich / 600 EUR mehr als 3500 km nicht-innergemeinschaftlich. Halbierung des Ausgleichs bei kurzer Verspaetungs-Beifoerderung. Bei mehreren Passagieren pro Person eigenständig. Pro Anspruchsfall ein Berechnungsdokument. |

## Arbeitsweg

Im Plugin Fluggastrechte (VO 261/2004) gilt für **Ausnahmen Aussergewoehnliche Umstaende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ausnahmen-aussergewoehnliche-umstaende-pruefen`

**Fokus:** Prüffeld für ausnahmen aussergewoehnliche umstaende pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Außergewöhnliche Umstände prüfen (Art. 5 Abs. 3 VO 261/2004)

## Norm

Art. 5 Abs. 3 VO 261/2004: Ein ausführendes Luftfahrtunternehmen ist nicht verpflichtet Ausgleichszahlungen zu leisten wenn es nachweisen kann dass die Annullierung **auf außergewöhnliche Umstände zurückgeht** die sich auch dann nicht hätten vermeiden lassen wenn alle zumutbaren Maßnahmen ergriffen worden waeren.

**Beweislast** liegt bei der Airline (Wortlaut "nachweisen kann"). Pauschale Behauptung reicht nicht.

## Zwei-Stufen-Prüfung

### Stufe 1 — Liegt überhaupt ein außergewöhnlicher Umstand vor?

Maßgeblich ist die st. Rspr. des EuGH. Die Definition (1) nicht Teil der normalen Tätigkeit des Luftfahrtunternehmens und (2) tatsächlich nicht beherrschbar — st. Rspr., bestätigt u.a. in EuGH C-549/07 (Wallentin-Hermann) und Folgeentscheidungen. Vor Versand jeden konkreten Sachverhalt mit einer offenen Quelle aus curia.europa.eu belegen.

### Stufe 2 — Hätten zumutbare Maßnahmen den Schaden verhindert?

Auch wenn ein außergewöhnlicher Umstand vorliegt, muss die Airline beweisen, dass alle zumutbaren Maßnahmen ergriffen wurden (Art. 5 Abs. 3 VO 261/2004; st. Rspr. EuGH C-549/07 und nachfolgende Entscheidungen — curia.europa.eu).

## Katalog typischer Sachverhalte (Stand Mai 2026)

### Ja regelmäßig außergewöhnlich

| Sachverhalt | Rspr. (offene Quelle) |
|---|---|
| Vulkanasche / Naturkatastrophe | EuGH st. Rspr. (curia.europa.eu) |
| Sicherheitsrisiken Terrordrohung | EuGH st. Rspr. (curia.europa.eu) |
| Streik der Flugsicherung (externer Dienstleister) | EuGH st. Rspr. (curia.europa.eu) |
| Blitzschlag mit sicherheitsbedingter Kontrolle | EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag kann außergewöhnlicher Umstand sein (curia.europa.eu) |
| Versteckter Konstruktionsfehler Triebwerk | EuGH, Urt. v. 13.6.2025, C-411/23 — versteckter Konstruktionsfehler ist außergewöhnlicher Umstand (curia.europa.eu) |
| Fluchtversuche Passagiere mit Behinderung des Bordbetriebs | EuGH-Linie je Einzelfall — Volltext in curia.europa.eu verifizieren |
| Krieg Embargo Luftraumsperrung | EuGH st. Rspr. (curia.europa.eu) |

### Nein regelmäßig keine außergewöhnlichen Umstände

| Sachverhalt | Rspr. (offene Quelle) |
|---|---|
| Technischer Defekt aus Wartungsversäumnis | EuGH, Urt. v. 22.12.2008, C-549/07 (Wallentin-Hermann) — curia.europa.eu |
| Streik der eigenen Mitarbeiter (Crew, Bodendienst) | st. Rspr. EuGH — Volltext in curia.europa.eu |
| Personalmangel am Flughafen (eigene Ground-Crew) | EuGH, Urt. v. 16.5.2024, C-405/23 — je nach Konstellation; gepäckabhängige Personalverknappung kann außergewöhnlich sein (curia.europa.eu) |
| Personalmangel / Krankenstand eigene Crew | st. Rspr. — Teil normalen Betriebs (curia.europa.eu) |
| Computer-Störungen des Buchungssystems | st. Rspr. EuGH (curia.europa.eu) |
| Wartung / TBO-Erreichung | Routine; kein außergewöhnlicher Umstand |

### Differenziert

| Sachverhalt | Differenzierung |
|---|---|
| Vorverlegung der Abflugzeit | EuGH, Urt. v. 9.1.2025, C-394/23 — Vorverlegung über eine Stunde gilt als Annullierung mit Entschädigungsanspruch (curia.europa.eu) |
| Wetter | bei wirklich extremen Bedingungen ja; bei normalen Wintern oder gemäßigtem Schneefall nein — EuGH-Linie konkret prüfen (curia.europa.eu) |
| Slot-Verschiebung Flugverkehrsleitung | je nach Ursache (kapazitätsbezogen vs sicherheitsbezogen) |

## Prüfraster

```
Frage 1: Welche Begründung hat die Airline angegeben?
 - Keine Begründung → Beweislast nicht erfüllt → Anspruch erhalten
 - Pauschale Begründung ohne Detail → Beweislast nicht erfüllt → Anspruch erhalten

Frage 2: Faellt der angegebene Sachverhalt in den Katalog
"regelmäßig außergewöhnlich"?
 - Nein → Anspruch erhalten; ggf. Sachverhalt kategorisieren als
 technischen Defekt
 - Ja → Stufe 2

Frage 3: Hat die Airline alle zumutbaren Maßnahmen ergriffen?
 - Eckdaten: rechtzeitige Information Ersatzflugzeug Reserve-Crew
 Umbuchung auf andere Airline Hotel
 - Wenn nicht dargelegt: Beweislast nicht erfüllt → Anspruch erhalten

Frage 4: Kausalitaet — beruht die Annullierung tatsächlich auf dem
außergewöhnlichen Umstand?
 - Folgeverspätungen aus dem Vortag werden regelmäßig nicht mehr
 als außergewöhnlich gewertet (EuGH-Verfahren zur kettenartigen
 Verspätung)
```

## Gegenargumente bei typischen Airline-Standardausreden

Siehe Skill `airline-standardausreden-pruefen` mit detaillierten Standardgegenargumenten.

## Ausgabe

- `aussergewoehnlich-pruefung.md` mit:
 - Begründung der Airline (Zitat)
 - Subsumtion unter Katalog
 - Prüfung zumutbarer Maßnahmen
 - Pinpoint-Zitate EuGH-Rechtsprechung
 - Ergebnis (Anspruch erhalten / Anspruch entfaellt / weitere Sachverhaltsaufklärung noetig)
- Hinweis: Bei strittiger Beweisfrage ist die Beweislast der Airline ein wichtiger Hebel.

---
<!-- AUDIT 27.05.2026 bundle_004 -->
**Halluzinations-Audit 27.05.2026**

## 2. `aussergewoehnliche-umstaende-strikt`

**Fokus:** Streng auszulegende aussergewoehnliche Umstaende Art. 5 Abs. 3 VO 261: Wetter, Streik nicht eigener Mitarbeiter, gerichtlich verfuegte Flugverbote, Wildschlag in Triebwerk. Keine aussergewoehnlichen Umstaende: technische Defekte (EuGH Wallentin-Hermann), Krankheit Crew, ATC-Engpaesse mit Routine. Pruefraster mit Belegen.

# Aussergewoehnliche Umstaende

## Spezialwissen: Aussergewoehnliche Umstaende
- **Spezialgegenstand:** Aussergewoehnliche Umstaende / aussergewoehnliche umstaende strikt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 5, VO, ATC.
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

## 3. `distanz-und-ausgleich-berechnen`

**Fokus:** Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich oder 1500 bis 3500 km nicht-innergemeinschaftlich / 600 EUR mehr als 3500 km nicht-innergemeinschaftlich. Halbierung des Ausgleichs bei kurzer Verspaetungs-Beifoerderung. Bei mehreren Passagieren pro Person eigenständig. Pro Anspruchsfall ein Berechnungsdokument.

# Distanz und Ausgleichszahlung berechnen

## Norm

Art. 7 VO 261/2004 — Ausgleichsanspruch in drei Stufen:

| Stufe | Distanz | Höhe pro Passagier |
|---|---|---|
| 1 | bis 1500 km | 250 EUR |
| 2 | mehr als 1500 km innergemeinschaftlich | 400 EUR |
| 2 | 1500 bis 3500 km nicht-innergemeinschaftlich | 400 EUR |
| 3 | mehr als 3500 km nicht-innergemeinschaftlich | 600 EUR |

## Distanzberechnung

- **Großkreisrechnung** (Great Circle Distance) zwischen Abflug- und Zielflughafen.
- IATA-Standardkoordinaten der Flughaefen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anschlussflug über Drittstaat als Umweg zählt nicht (Direktverbindungs-Maßstab).

## Begriff innergemeinschaftlich vs nicht-innergemeinschaftlich

- **Innergemeinschaftlich** Flug zwischen zwei Flughaefen die in der EU liegen.
- **Nicht-innergemeinschaftlich** mindestens ein Flughafen außerhalb der EU.
- **Sondergebiete** Kanaren Madeira Azoren EU-Außengebiete EU-Recht gilt (innergemeinschaftlich).
- **Norwegen Schweiz Island Liechtenstein** mehrere bilaterale Abkommen — beachten ob VO 261/2004 anwendbar.

## Beispielberechnungen

- **Berlin (BER) — Madrid (MAD)** ca. 1872 km innergemeinschaftlich → Stufe 2 → 400 EUR
- **München (MUC) — Lissabon (LIS)** ca. 2280 km innergemeinschaftlich → Stufe 2 → 400 EUR
- **Frankfurt (FRA) — Mallorca (PMI)** ca. 1245 km innergemeinschaftlich → Stufe 1 → 250 EUR
- **Hamburg (HAM) — New York (JFK)** ca. 6125 km nicht-innergemeinschaftlich → Stufe 3 → 600 EUR
- **Wien (VIE) — Dubai (DXB)** ca. 4275 km nicht-innergemeinschaftlich → Stufe 3 → 600 EUR

## Halbierungsregel (Art. 7 Abs. 2 VO 261/2004)

Die Airline kann den Ausgleich **um 50 Prozent kuerzen** wenn dem Fluggast eine **anderweitige Beförderung** angeboten wurde **und** die tatsächliche Ankunftszeit am Endziel nicht überschreitet:

- Bei Distanz **bis 1500 km** die geplante Ankunftszeit um **mehr als zwei Stunden**.
- Bei Distanz **1500 bis 3500 km nicht-innergemeinschaftlich oder über 1500 km innergemeinschaftlich** die geplante Ankunftszeit um **mehr als drei Stunden**.
- Bei Distanz **mehr als 3500 km nicht-innergemeinschaftlich** die geplante Ankunftszeit um **mehr als vier Stunden**.

Folge: Stufe 1 → 125 EUR; Stufe 2 → 200 EUR; Stufe 3 → 300 EUR.

## Mehrere Passagiere

- **Eigenständiger Anspruch pro Passagier** (Art. 7 VO 261/2004 ist persönlich).
- **Auch Kinder** mit eigener Beförderung (eigenes Ticket) haben den vollen Anspruch — auch bei Kindertarif.
- **Babys ohne eigenen Sitzplatz** (Lap-Infant) haben i. d. R. keinen eigenen Ausgleichsanspruch wenn nicht gesondert befoerdert.

## Nebenforderungen

- **Verzugszinsen** ab Mahnung (§§ 286 288 BGB) — Verbraucher 5 Prozentpunkte über Basiszinssatz.
- **Auslagen** wenn Verbraucher selbst Auslagen getragen hat (Hotel Verpflegung Telefon) bei verletzter Betreuungspflicht (Art. 9 VO 261/2004) — separat zur Ausgleichszahlung.

## Pauschalreise

- Bei Pauschalreise greifen zusätzliche Ansprueche gegen den Reiseveranstalter nach §§ 651a ff. BGB.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

```
Berechnung Ausgleich
Fall-ID: FG-2026-0042
Flug: LH 1234 MUC-LIS
Distanz: 2280 km (innergemeinschaftlich)
Stufe: 2 (mehr als 1500 km innergemeinschaftlich)
Ausgleich pro Passagier: 400 EUR
Anzahl Passagiere: 3
Gesamtausgleich: 1200 EUR

Halbierungsregel prüfen:
- Ersatzflug am 13.05.2026 LH 1234
- Tatsächliche Ankunft 13.05.2026 12:00 statt geplant 12.05.2026 11:00
- Verspätung: 25 Stunden über drei Stunden → keine Halbierung
- → 1200 EUR Anspruch in voller Hoehe
```

## Leitentscheidungen Distanz und Ausgleich

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Hinweise

- Beweislast für Distanzangaben liegt nicht beim Fluggast (Standard-Flugplandaten frei zugänglich).
- Bei strittiger Distanz: Gericht stellt anhand IATA-Daten fest.
