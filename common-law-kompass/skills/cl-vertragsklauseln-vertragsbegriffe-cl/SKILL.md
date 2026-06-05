---
name: cl-vertragsklauseln-vertragsbegriffe-cl
description: "CL Vertragsklauseln Vertragsbegriffe CL: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# CL Vertragsklauseln Vertragsbegriffe CL

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **CL Vertragsklauseln Vertragsbegriffe CL** im Plugin Common Law Kompass. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cl-vertragsklauseln-typische-uebersicht` | Typische Common-Law-Klauseln uebersichtlich erklaeren: Indemnification, Representations and Warranties, Limitation of Liability, Entire Agreement, Severability, Governing Law, Boilerplate. Pro Klausel Funktion, deutsche Entsprechung und typische Stolpersteine. |
| `spezial-vertragsbegriffe-risikoampel-und-gegenargumente` | Vertragsbegriffe: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin common law kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `cl-discovery-doc-production-spezial` | Spezialfall US-Discovery / E-Discovery und Document Production: Anforderungen US-Gericht, Hague Evidence Convention, Blocking Statutes (Frankreich), DSGVO. Pruefraster fuer deutsche Mandanten in US-Verfahren. |

## Arbeitsweg

Im Plugin Common Law Kompass gilt für **CL Vertragsklauseln Vertragsbegriffe CL**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cl-vertragsklauseln-typische-uebersicht`

**Fokus:** Typische Common-Law-Klauseln uebersichtlich erklaeren: Indemnification, Representations and Warranties, Limitation of Liability, Entire Agreement, Severability, Governing Law, Boilerplate. Pro Klausel Funktion, deutsche Entsprechung und typische Stolpersteine.

# Common Law: Vertragsklauseln

## Aufgabe
Typische Common-Law-Klauseln uebersichtlich erklaeren: Indemnification, Representations and Warranties, Limitation of Liability, Entire Agreement, Severability, Governing Law, Boilerplate.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Klauseln-Uebersicht — Common Law mit deutscher Entsprechung

| Klausel | Funktion / Inhalt | Deutsche Entsprechung | Typische Stolpersteine |
|---|---|---|---|
| **Consideration** | Wechselseitige "bargained-for exchange" — Voraussetzung der Vertragsbindung in UK/US-Common Law | Keine Entsprechung im BGB; § 311 I BGB kennt keine consideration. Bei UK-Recht: "deed" als consideration-loses Aequivalent | "Nominal consideration of 1 GBP" oft Hinweis auf consideration-Bedarf bei englischem Recht; bei deutschem Recht ueberfluessig |
| **Representations and Warranties (R&W)** | Tatsachenversicherungen (reps) und Garantieversprechen (warranties) zum Stichtag | Unklarer Gleichlauf mit §§ 433 ff., 443 BGB (Garantie); §§ 280, 311 II Nr. 1 BGB (c.i.c.); aber kein 1:1-Pendant | "Misrepresentation" UK = ggf. Anfechtung und/oder rescission und/oder Schadensersatz; im deutschen Recht §§ 119 II, 123 BGB (Anfechtung) vs. § 434 BGB (Mangel) — andere Rechtsfolgen |
| **Indemnification / Indemnity** | Freistellung vom Drittanspruch; auch first-party indemnity (verschuldensunabhaengig) | § 257 BGB (Befreiungsanspruch); kein verschuldensunabhaengiges Aequivalent; bei AGB AGB-rechtlich problematisch (§ 309 Nr. 7 BGB) | Achtung: "indemnify, defend and hold harmless" loest in deutschem Recht keine eigenstaendige Verpflichtung aus; AGB-Kontrolle bei vorformulierten Klauseln |
| **Limitation of Liability** | Haftungsobergrenze fuer Schaeden; oft "Cap" als % vom Vertragswert oder feste Summe | §§ 276 III, 309 Nr. 7 BGB; bei AGB strenge Grenzen (kein Ausschluss fuer Vorsatz/grobe Fahrlaessigkeit, Leben/Koerper/Gesundheit, Kardinalpflichten) | "Aggregate cap" und "per-event cap" unterscheiden; ausgenommen werden typisch IP-Verletzung, indemnification, vertrauliche Information, Vorsatz |
| **Suretyship vs. Guarantee** | UK: "guarantee" = sekundaere Verpflichtung; "indemnity" = primaere | § 765 BGB Buergschaft vs. § 311 BGB Garantievertrag; § 766 BGB Schriftform | "On first demand guarantee" = abstrakte Buergschaft auf erstes Anfordern; bei deutschem Recht streng AGB-rechtlich kontrolliert |
| **Entire Agreement / Merger Clause** | Vertrag enthaelt vollstaendige Einigung; vorvertragliche Erklaerungen unbeachtlich | §§ 133, 157 BGB Auslegung; Andeutungstheorie; Klausel ist im deutschen Recht **wirkungsbeschraenkt**, schliesst Auslegung nicht vollstaendig aus | BGH XI ZR 39/04: Merger Clauses koennen § 305c II BGB nicht ueberwinden; AGB-Kontrolle |
| **No Oral Modification (NOM)** | Aenderungen nur schriftlich | § 125 BGB; doppelte Schriftformklausel im AGB (§ 305b BGB Vorrang Individualabrede) | BGH-Linie: Schriftformklausel kann individualvertraglich durchbrochen werden (Vorrang Individualabrede) |
| **Severability / Salvatorische Klausel** | Bei Unwirksamkeit eines Teils bleibt Rest wirksam | § 139 BGB (Auslegungsregel); Klausel modifiziert nur Auslegung | BGH-Linie: rein deklaratorische Klauseln im AGB unproblematisch; substanziellere Ersetzungsklauseln AGB-rechtlich pruefen |
| **Governing Law** | Anwendbares materielles Recht | Art. 3 Rom I-VO (Vertraege), Art. 14 Rom II-VO (ausservertraglich) | Internationale Verbraucher Art. 6 Rom I-VO, AN Art. 8 Rom I-VO; ordre public Art. 21 Rom I-VO |
| **Jurisdiction / Forum Selection** | Zustaendiges Gericht | Art. 25 Brussel Ia-VO (gerichtliche Zustaendigkeit innerhalb EU); UK seit Brexit: Haager Gerichtsstandsuebereinkommen | Asymmetrische Klauseln (nur eine Partei wahlt) in Frankreich teils unwirksam; Pruefung des AVAG bei Drittstaaten |
| **Arbitration Clause** | Schiedsgerichtsbarkeit (ICC, LCIA, DIS, SIAC, AAA/ICDR) | §§ 1029 ff. ZPO; UNCITRAL Model Law; New York Convention 1958 | Schriftform/Form § 1031 ZPO; Verbraucher § 1031 V ZPO (notarielle Form) |
| **Boilerplate** | Sammelbegriff fuer Standardklauseln (Force Majeure, Notices, Assignment, Counterparts, Headings) | Verteilt im BGB; einzeln pruefen | Force Majeure in UK/US restriktiv (nicht "frustration" = § 313 BGB Pendant); "frustration of contract" UK enger |

## Pruefraster fuer den Skill

1. **Sachverhalt fixieren** — Welche Klauseln, welcher Vertragstyp, welches Recht?
2. **Klauselfunktion identifizieren** ueber die Tabelle.
3. **Deutsche Entsprechung pruefen** und Unterschiede markieren.
4. **AGB-Rechtskontrolle** §§ 305 ff. BGB pruefen, wenn deutsches Recht anwendbar.
5. **Internationale Privatrecht-Kontrolle** Rom I/II, EuGVVO.

## Praxisfallen

- **R&W-Versicherung (W&I)** im M&A: Deckungsausschluesse pruefen, "no claims declaration".
- **Indemnity vs. Garantie** sprachlich oft verwischt; im deutschen Recht klar trennen.
- **Choice of law** beim Verbraucher: Schutz nicht abdingbar (Art. 6 II Rom I-VO).
- **Forum non conveniens** in UK/US verfuegbar, in der EU nicht (EuGH Owusu).

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

## 2. `spezial-vertragsbegriffe-risikoampel-und-gegenargumente`

**Fokus:** Vertragsbegriffe: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin common law kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vertragsbegriffe: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Vertragsbegriffe: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Vertragsbegriffe: Risikoampel, Gegenargumente und Verteidigungslinien / vertragsbegriffe risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UK, US, UCC.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vertragsbegriffe** prüfen.
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

## 3. `cl-discovery-doc-production-spezial`

**Fokus:** Spezialfall US-Discovery / E-Discovery und Document Production: Anforderungen US-Gericht, Hague Evidence Convention, Blocking Statutes (Frankreich), DSGVO. Pruefraster fuer deutsche Mandanten in US-Verfahren.

# Common Law: Discovery-Spezial

## Spezialwissen: Common Law: Discovery-Spezial
- **Spezialgegenstand:** Common Law: Discovery-/ cl discovery doc production spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** US, DSGVO.
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
