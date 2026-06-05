---
name: kirk-leitfaden-prompts-kr-executive
description: "Kirk Mandantenkommunikation Leitfaden, Kirk Prompts Templates Versionierung Spezial, Kr Richtlinie Executive Summary 1 Pager Template: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Kirk Mandantenkommunikation Leitfaden, Kirk Prompts Templates Versionierung Spezial, Kr Richtlinie Executive Summary 1 Pager Template

## Arbeitsbereich

Dieser Skill bündelt **Kirk Mandantenkommunikation Leitfaden, Kirk Prompts Templates Versionierung Spezial, Kr Richtlinie Executive Summary 1 Pager Template** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `kirk-mandantenkommunikation-leitfaden` | Leitfaden Mandantenkommunikation ueber KI-Einsatz: Hinweis, Einwilligung, Vergleichbarkeit mit Hilfspersonal. Pruefraster fuer Mandatsverhaeltnis. |
| `kirk-prompts-templates-versionierung-spezial` | Spezialfall Prompts und Templates: Versionierung, Reviewprozess, Geheimhaltung, Test. Pruefraster fuer Knowledge-Management. |
| `kr-richtlinie-executive-summary-1-pager-template` | Ein-Seiten-Executive-Summary fuer KI-Nutzungsrichtlinien einer Kanzlei oder Rechtsabteilung; produziert ein druckfertiges 1-Pager-Dokument mit den Bloecken 'Was ist erlaubt', 'Was ist nicht erlaubt', 'Wo Vorsicht', 'Anlaufstellen' und 'Naechste Revision'; deckt KI-VO 2024/1689 Artikel 4 und 5 und 26 sowie BRAO Paragraf 43a und Paragraf 43e und DSGVO Artikel 5 und 6 und 28 und 32 ab und ist als Anlage zur Vollrichtlinie oder als Aushang fuer Onboarding und Schulungen einsetzbar. |

## Arbeitsweg

Für **Kirk Mandantenkommunikation Leitfaden, Kirk Prompts Templates Versionierung Spezial, Kr Richtlinie Executive Summary 1 Pager Template** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `ki-richtlinie-kanzleien` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `kirk-mandantenkommunikation-leitfaden`

**Fokus:** Leitfaden Mandantenkommunikation ueber KI-Einsatz: Hinweis, Einwilligung, Vergleichbarkeit mit Hilfspersonal. Pruefraster fuer Mandatsverhaeltnis.

# KIRK: Mandantenkommunikation

## Spezialwissen: KIRK: Mandantenkommunikation
- **Spezialgegenstand:** KIRK: Mandantenkommunikation / kirk mandantenkommunikation leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, KIRK.
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
Dieser Skill gehoert zum Plugin `ki-richtlinie-kanzleien`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `kirk-prompts-templates-versionierung-spezial`

**Fokus:** Spezialfall Prompts und Templates: Versionierung, Reviewprozess, Geheimhaltung, Test. Pruefraster fuer Knowledge-Management.

# KIRK: Prompts Versionierung

## Spezialwissen: KIRK: Prompts Versionierung
- **Spezialgegenstand:** KIRK: Prompts Versionierung / kirk prompts templates versionierung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KIRK, BGH, BVerfG.
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
Dieser Skill gehoert zum Plugin `ki-richtlinie-kanzleien`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `kr-richtlinie-executive-summary-1-pager-template`

**Fokus:** Ein-Seiten-Executive-Summary fuer KI-Nutzungsrichtlinien einer Kanzlei oder Rechtsabteilung; produziert ein druckfertiges 1-Pager-Dokument mit den Bloecken 'Was ist erlaubt', 'Was ist nicht erlaubt', 'Wo Vorsicht', 'Anlaufstellen' und 'Naechste Revision'; deckt KI-VO 2024/1689 Artikel 4 und 5 und 26 sowie BRAO Paragraf 43a und Paragraf 43e und DSGVO Artikel 5 und 6 und 28 und 32 ab und ist als Anlage zur Vollrichtlinie oder als Aushang fuer Onboarding und Schulungen einsetzbar.

# Executive Summary 1-Pager Template

## Zweck

Dieser Skill erzeugt einen Ein-Seiten-Executive-Summary der KI-Nutzungsrichtlinie. Er liefert das kompakteste Dokument, das eine Kanzlei oder Rechtsabteilung als Aushang, Onboarding-Anlage oder Mandanteninformation einsetzen kann. Das Format ist bewusst auf 1 DIN-A4-Seite begrenzt.

## Wann brauchen Sie diesen Skill

- Onboarding neuer Mitarbeiter und Referendare
- Aushang im Kopierraum oder digitalen Intranet
- Anlage zu Mandatsbestaetigungen, wenn Mandanten nach KI-Politik fragen
- Schulungs-Handout fuer Pflichtfortbildung nach Art. 4 KI-VO

## Kaltstart-Fragen (Abfragesystem)

1. Name und Standort der Kanzlei?
2. Welche KI-Tools sind freigegeben? (Liste oder Hinweis auf Tool-Katalog)
3. Wer ist KI-Beauftragter oder Compliance-Ansprechpartner?
4. Wer ist Datenschutzbeauftragter?
5. Naechster Revisionstermin? (Standard: jaehrlich oder bei Rechtsaenderung)
6. Soll der 1-Pager nur intern oder auch fuer Mandanten freigegeben werden?

## Rechtlicher Rahmen

- KI-VO 2024/1689: Art. 4 KI-Kompetenz (gilt ab 02.02.2025), Art. 5 verbotene Praktiken (ab 02.02.2025), Art. 26 Betreiberpflichten Hochrisiko (ab 02.08.2026), Art. 50 Transparenzpflichten
- BRAO: Paragraf 43a Abs. 2 Verschwiegenheit, Paragraf 43e Auftragsverarbeitung an IT-Dienstleister
- StBerG Paragraf 62a, WPO Paragraf 50a, BNotO Paragraf 26a, PAO Paragraf 39a: Parallelregelungen Schweigepflicht
- StGB Paragraf 203: strafbewehrtes Berufsgeheimnis
- DSGVO Art. 5 Grundsaetze, Art. 6 Rechtmaessigkeit, Art. 28 Auftragsverarbeitung, Art. 32 Sicherheit, Art. 44 ff. Drittlandtransfer

## Ablauf / Schritt fuer Schritt

1. Kaltstart-Fragen beantworten lassen.
2. Mustertext unten uebernehmen und Platzhalter in eckigen Klammern fuellen.
3. Auf eine Seite kuerzen; pro Block max. 4 Stichpunkte.
4. Logo und Datum einsetzen.
5. Vom KI-Beauftragten und der Geschaeftsfuehrung gegenzeichnen lassen.
6. Termin fuer naechste Revision in Kanzlei-Kalender setzen.

## Mustertext / Vorlage

```
KI-NUTZUNG IN [KANZLEI/RECHTSABTEILUNG] — EXECUTIVE SUMMARY
Stand: [MONAT/JAHR] | Version [X.Y] | Naechste Revision: [DATUM]

WAS IST ERLAUBT
- Nutzung der freigegebenen KI-Tools laut Anlage Tool-Katalog
- Recherche, Formulierungshilfe, Zusammenfassungen ohne Mandatsbezug
- Verarbeitung anonymisierter Texte (alle Namen, Aktenzeichen, Mandatsdetails entfernt)
- Eigene Kanzlei-Accounts (keine Privat-Logins)

WAS IST NICHT ERLAUBT
- Upload identifizierender Mandatsdaten ohne Anonymisierung (Paragraf 43a BRAO, Paragraf 203 StGB)
- Nutzung von KI-Diensten ohne abgeschlossenen AVV nach Art. 28 DSGVO
- Verbotene Praktiken nach Art. 5 KI-VO (Social Scoring, manipulative KI etc.)
- Ungepruefte Uebernahme von KI-Output als Rechtsbehauptung oder Zitat

WO VORSICHT GEBOTEN IST
- Drittland-Transfer (USA, China, Indien): nur mit Schrems-II-Pruefung
- Hochrisiko-KI nach Anhang III KI-VO ab 02.08.2026
- Gemeinsame Verantwortlichkeit Art. 26 DSGVO bei Mandanten-eigenen KI-Tools
- KI-Output zu Personalentscheidungen, Bewerbungen, Mitarbeiterbewertungen

ANLAUFSTELLEN
- KI-Beauftragter: [NAME], [TEL], [E-MAIL]
- Datenschutzbeauftragter: [NAME], [TEL], [E-MAIL]
- Geschaeftsfuehrung: [NAME]
- Externe: BfDI, Landesdatenschutzbehoerde, RAK [ORT]

NAECHSTE REVISION
- Plantermin: [DATUM]
- Anlass-Revisionen sofort: KI-VO-Durchfuehrungsrechtsakte, neue BRAK-Hinweise,
 Schrems-III, neue Anbieter-Risiken
- Diese Seite ersetzt nicht die Vollrichtlinie (Anlage 1)

[UNTERSCHRIFT GESCHAEFTSFUEHRUNG] [UNTERSCHRIFT KI-BEAUFTRAGTER]
```

Pro Block maximal 50 Worte, gesamt unter 300 Worte. Schriftgrad 11 Punkt.

## Typische Fehler

- Mehr als eine Seite: dann ist es kein Executive Summary mehr
- Verweis auf Tools, die im Katalog nicht aufgefuehrt sind
- Fehlende Anlaufstelle (Mitarbeiter weiss nicht, wen er fragen kann)
- Keine Datierung und keine Versionsnummer
- Halbsatz-Verweise auf KI-VO-Artikel ohne konkrete Norm

## Querverweise

- `kr-richtlinie-vollvorlage-2026-kanzlei` fuer die Vollvorlage
- `kr-richtlinie-anlagenverwaltung-tool-katalog` fuer den Tool-Katalog
- `kr-richtlinie-mitarbeiter-erklaerung-und-bestaetigung` fuer die Bestaetigung
- `kr-workflow-iterative-richtlinien-revision` fuer den Revisionsprozess

## Quellen Stand 06/2026

- VO (EU) 2024/1689 (KI-VO), insb. Art. 4, 5, 26, 50
- BRAO i. d. F. 2024, Paragraf 43a, Paragraf 43e
- StBerG Paragraf 62a, WPO Paragraf 50a, BNotO Paragraf 26a, PAO Paragraf 39a
- StGB Paragraf 203
- VO (EU) 2016/679 (DSGVO), insb. Art. 5, 6, 28, 32, 44 ff.
- BRAK-Hinweise zur KI-Nutzung (Stand pruefen vor Veroeffentlichung)
- DAV-Stellungnahme zu Legal-AI (Stand pruefen vor Veroeffentlichung)


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
