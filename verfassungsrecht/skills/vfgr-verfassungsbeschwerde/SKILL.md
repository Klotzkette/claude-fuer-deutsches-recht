---
name: vfgr-verfassungsbeschwerde
description: "Vfgr Verfassungsbeschwerde: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat."
---

# Vfgr Verfassungsbeschwerde

## Arbeitsbereich

Dieser Skill arbeitet **Vfgr Verfassungsbeschwerde** als zusammenhängenden Arbeitsgang im Plugin Verfassungsrecht ab — nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vfgr-verfassungsbeschwerde-substantiierung-spezial` | Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittelbar, Rechtswegerschoepfung. Pruefraster fuer Anwalt. |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Vfgr Verfassungsbeschwerde**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vfgr-verfassungsbeschwerde-substantiierung-spezial`

**Fokus:** Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittelbar, Rechtswegerschoepfung. Pruefraster fuer Anwalt.

# VfgR: VB-Substantiierung

## Fachkern: VfgR: VB-Substantiierung
- **Spezialgegenstand:** VfgR: VB-Substantiierung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
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
