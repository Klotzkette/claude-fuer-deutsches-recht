---
name: scope-bfsg-screenreader-semantik-abnahme
description: "Scope BFSG Screenreader Semantik Abnahme: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Scope BFSG Screenreader Semantik Abnahme

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Scope BFSG Screenreader Semantik Abnahme** im Plugin Barrierefreiheit Web (BFSG/WCAG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `scope-bfsg-bitv-wad` | Prüft den Rechtsrahmen digitaler Barrierefreiheit: BFSG, BFSGV, BITV 2.0, Web Accessibility Directive, European Accessibility Act, öffentlicher Sektor, B2C-E-Commerce, Kleinstunternehmen und freiwilliger Standard. Output: Scope-Memo. |
| `screenreader-semantik-aria` | Prüft Screenreader-Nutzbarkeit, HTML-Semantik, Landmarken, Überschriften, Labels, Alt-Texte, ARIA, Live-Regionen, Fehlermeldungen und dynamische Komponenten. Output: Screenreader-Prüfprotokoll. |
| `spezial-abnahme-formular-portal-und-einreichung` | Abnahme: Formular, Portal und Einreichungslogik im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Barrierefreiheit Web (BFSG/WCAG) gilt für **Scope BFSG Screenreader Semantik Abnahme**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `scope-bfsg-bitv-wad`

**Fokus:** Prüft den Rechtsrahmen digitaler Barrierefreiheit: BFSG, BFSGV, BITV 2.0, Web Accessibility Directive, European Accessibility Act, öffentlicher Sektor, B2C-E-Commerce, Kleinstunternehmen und freiwilliger Standard. Output: Scope-Memo.

# Scope: BFSG, BITV, WAD, freiwilliger Standard

Dieser Einstieg öffnet den Arbeitsgang, wenn unklar ist, ob eine Website rechtlich barrierefrei sein muss und nach welchem Maßstab.

## Prüffragen

1. Wer betreibt das Angebot?
2. Richtet sich das Angebot an Verbraucherinnen und Verbraucher?
3. Wird online ein Vertrag angebahnt oder geschlossen?
4. Handelt es sich um eine öffentliche Stelle oder um ein privates Unternehmen?
5. Ist es Website, mobile App, Webshop, Banking, Verkehr, Telekommunikation, E-Book, Ticketing oder nur Information?
6. Gibt es Kleinstunternehmens-, Altbestands- oder Übergangsfragen?
7. Gibt es Vergabe-, Fördermittel- oder vertragliche Anforderungen unabhängig vom Gesetz?

## Ergebnisformat

| Frage | Befund | Folge |
| --- | --- | --- |
| Öffentliche Stelle? | [...] | BITV/WAD prüfen |
| BFSG-Dienstleistung? | [...] | BFSG/BFSGV prüfen |
| E-Commerce? | [...] | Checkout und Vertragsstrecke prüfen |
| Nur B2B/Information? | [...] | Pflicht offen/freiwillig |
| Standardmaßstab | [...] | EN 301 549 / WCAG |

## Wichtig

Nicht jede Website fällt automatisch unter das BFSG. Aber wenn eine Website Teil einer erfassten Dienstleistung ist, insbesondere einer elektronischen Geschäftsverkehrsdienstleistung, reicht ein hübscher statischer Auftritt nicht. Der gesamte digitale Weg bis zum Vertrag muss nutzbar sein.

## Erfasste Dienstleistungen nach § 1 Abs. 3 BFSG
- Telekommunikationsdienste (außer Maschine-zu-Maschine)
- Personenbeförderungs-Webseiten und -Apps (Echtzeitinformationen, Buchung, Tickets)
- Bankdienstleistungen für Verbraucher
- E-Books und Lesesoftware
- Dienstleistungen im elektronischen Geschäftsverkehr (Online-Shops, Marktplätze)
- Audiovisuelle Mediendienste (Zugang zu Inhalten, nicht die Inhalte selbst)

## Erfasste Produkte nach § 1 Abs. 2 BFSG
- Hardware/Betriebssysteme für Universal-Computer für Verbraucher
- Selbstbedienungsterminals (Geldautomaten, Ticketautomaten, Check-in-Automaten)
- Verbraucher-Endgeräte für Telekommunikations- und audiovisuelle Mediendienste
- E-Book-Lesegeräte

## Ausnahmen
- **Kleinstunternehmen** (§ 3 Nr. 17 BFSG: < 10 Beschäftigte und ≤ 2 Mio. EUR Jahresumsatz/-bilanzsumme), die **Dienstleistungen** erbringen — diese Ausnahme gilt nicht für Produkte!
- **Unverhältnismäßige Belastung** (§ 17 BFSG): nur mit dokumentierter Bewertung anhand der in § 17 Abs. 2 BFSG genannten Kriterien.
- **Grundlegende Veränderung** (§ 16 BFSG): wenn die Anforderung das Wesen des Produkts/der Dienstleistung verändern würde.

## Übergangsfristen (§§ 38, 39 BFSG)
- 28.06.2025: Pflicht für neu in Verkehr gebrachte Produkte und neu erbrachte Dienstleistungen.
- Selbstbedienungsterminals: Übergangsfrist bis längstens 27.06.2040 für bestehende Geräte.
- Vor 28.06.2025 geschlossene Dienstleistungsverträge: Geltung erst zum Vertragsende oder nach 5 Jahren.

## Marktüberwachung und Sanktionen
- Zuständige Marktüberwachungsbehörde nach § 19 BFSG ist je nach Bundesland geregelt; bundesweit koordinierend ist die Bundesanstalt für Arbeitsschutz und Arbeitsmedizin (BAuA) für Produkte; für Dienstleistungen das Eisenbahn-Bundesamt bzw. die Landesbehörden.
- Bußgeld nach § 37 BFSG bis 100.000 EUR; bei Verstößen gegen Kennzeichnungspflichten bis 10.000 EUR.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `screenreader-semantik-aria`

**Fokus:** Prüft Screenreader-Nutzbarkeit, HTML-Semantik, Landmarken, Überschriften, Labels, Alt-Texte, ARIA, Live-Regionen, Fehlermeldungen und dynamische Komponenten. Output: Screenreader-Prüfprotokoll.

# Screenreader, Semantik, ARIA

Dieses Fachmodul greift, wenn die Website optisch funktioniert, aber semantisch unklar ist.

## Prüfschritte

1. Seitentitel und Sprache.
2. Landmarken: header, nav, main, footer, aside.
3. Überschriftenstruktur.
4. Links und Buttons mit verständlichem Namen.
5. Formularlabels und Fehlermeldungen.
6. Bilder und Icons mit sinnvollen Alternativen oder dekorativer Ausblendung.
7. ARIA nur dort, wo native HTML-Semantik nicht reicht.
8. Live-Regionen für dynamische Statusmeldungen.

## Merksatz

Schlechtes HTML wird durch ARIA selten besser. Erst native Semantik, dann ARIA gezielt.

## Output

```text
Problem:
Betroffene Komponente:
Screenreader-Auswirkung:
Empfohlener Fix:
Prüfung nach Fix:
```

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

## Ausgabeformat

- Befund.
- Nutzerwirkung.
- Norm-/Kriteriumsbezug.
- Konkreter Fix.
- Prioritaet und Nachweis fuer die Dokumentation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-abnahme-formular-portal-und-einreichung`

**Fokus:** Abnahme: Formular, Portal und Einreichungslogik im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Abnahme: Formular, Portal und Einreichungslogik

## Spezialwissen: Abnahme: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Abnahme: Formular, Portal und Einreichungslogik / abnahme formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BFSG, BFSGV, BITV, EN, WCAG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Abnahme** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
