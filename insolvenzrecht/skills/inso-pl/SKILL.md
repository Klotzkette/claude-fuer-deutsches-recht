---
name: inso-pl
description: "Inso PL: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inso PL

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Inso PL** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin insolvenzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin insolvenzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `inso-pl-einfuehrung-verfahrenstypen` | Insolvenzrechtsverfahren einfuehrend: Regelinsolvenz, Eigenverwaltung mit und ohne Schutzschirm, Verbraucher-Insolvenz, StaRUG-Restrukturierung. Pro Verfahrenstyp Schwelle, Antrag, Verlauf. Entscheidungstabelle. |
| `insol-sanierungsgewinn-finanzamt-im-insolvenzverfahren` | Finanzamt als Glaeubiger im Insolvenzverfahren. Paragraph 251 AO Aussetzung der Vollziehung, Paragraph 35 InsO Massezugehoerigkeit, Steuerforderungen als Insolvenzforderungen oder Masseverbindlichkeiten. Tabellenanmeldung der FA-Forderungen Paragraphen 174 ff. InsO. Steuerlicher Aufrechnungsschutz Paragraph 96 InsO. Schnittstelle zu Sanierungsgewinn. Mustertexte fuer Kommunikation mit dem Finanzamt. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Inso PL**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin insolvenzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenkommunikation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin insolvenzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Mandantenbrief-Bausteine Insolvenzrecht
- **Adressat:** Geschäftsführer / Vorstand persönlich (Hinweis auf persönliche Haftung), in CC keine Vertraulichkeitsbedenken (§ 43a Abs. 2 BRAO, § 203 StGB).
- **Eröffnung:** "In dem Mandat … / In Sachen Insolvenzantrag/Sanierung … senden wir Ihnen folgende Einschätzung."
- **Inhalt nach Triage-Ergebnis:**
 - Status: liegt eine materielle Insolvenz vor (§§ 17, 18, 19 InsO)?
 - Frist: Antragspflicht § 15a InsO — 3 Wochen ab Zahlungsunfähigkeit, 6 Wochen ab Überschuldung; bei Aussichtslosigkeit der Sanierung kürzer.
 - Haftung: persönliche Haftung Geschäftsführer für verspäteten Antrag (§ 15a Abs. 4 InsO Strafbarkeit; § 15b InsO Zahlungsverbot und Erstattungspflicht für nach Insolvenzreife erfolgte Zahlungen, ehemals § 64 GmbHG).
 - Alternativen: Eigenverwaltung § 270 InsO, Schutzschirm § 270d InsO, StaRUG (nur drohende ZU § 18 InsO).
- **Empfehlung:** klare Handlungsoption — antragstellen, Sanierungskonzept, Beraterhinzuziehung.
- **Nächste Schritte mit konkreter Frist:** Tag der nächsten Besprechung, Liste der benötigten Unterlagen.
- **Kostenhinweis:** Hinweis auf RVG / Honorarvereinbarung; bei Insolvenz Gerichtsverfahren-Wertgebühr nach RVG, vorinsolvenzliche Beratung nach Honorarvereinbarung.

## Heikle Themen
- **Verschwiegenheit § 43a BRAO:** Mandantengeheimnis auch nach Insolvenzeröffnung; Verwalter wird nicht automatisch Mandant.
- **Aufklärungspflicht:** Geschäftsführer ist über § 15a, § 15b InsO und § 266a StGB (Sozialversicherungsbeiträge) ausdrücklich aufzuklären — Beweissicherung der Aufklärung (E-Mail, Protokoll).
- **Eilkommunikation:** Bei akuter Antragspflicht keine Beratung nur per E-Mail; telefonische Aufklärung dokumentieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin insolvenzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Red-Team Qualitygate` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin insolvenzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Insolvenzrecht-Red-Team-Checks
- **Fristen:** § 15a InsO (3 Wochen bei ZU, 6 Wochen bei Überschuldung) korrekt berechnet ab Eintritt der materiellen Insolvenz (nicht ab Erkenntnis)?
- **Eröffnungsgrund-Schwellen:**
 - § 17 InsO Zahlungsunfähigkeit: 10-Prozent-Schwelle und 3-Wochen-Liquiditätslücke (BGH-Linie) explizit geprüft?
 - § 19 InsO Überschuldung: zweistufige Prüfung (rechnerische Überschuldung + negative Fortbestehensprognose) sauber getrennt?
 - § 18 InsO drohende Zahlungsunfähigkeit: Prognosezeitraum 24 Monate (seit SanInsFoG 2021) genannt?
- **Verwechslungsgefahr:**
 - Überschuldung ≠ bilanzielle Unterdeckung — Fortbestehensprognose entscheidet.
 - Zahlungsstockung ≠ Zahlungsunfähigkeit — Drei-Wochen-Grenze.
- **Anfechtung:** Bei § 133 InsO 4-Jahres-Zeitraum (seit Reform 2017 für kongruente Deckungen), bei §§ 130, 131 InsO 3 Monate, bei § 134 InsO 4 Jahre.
- **Strafbarkeit erkannt?** § 15a Abs. 4 InsO, §§ 283 ff. StGB, § 266a StGB Sozialversicherungsbeiträge.
- **EU-Bezug:** COMI-Prüfung (Art. 3 EuInsVO) erfolgt bei grenzüberschreitendem Sachverhalt?

## Halluzinations-Stopps
- Keine erfundenen Az. Falls unsicher: "BGH zu § X InsO, Az. zu verifizieren".
- Keine erfundenen IDW-Standard-Nummern (S6, S11, EPS 11 sind real; höhere Zahlen prüfen).
- Keine Verwechslung von § 64 GmbHG a.F. (vor 2021) und § 15b InsO (seit SanInsFoG).

## 3. `inso-pl-einfuehrung-verfahrenstypen`

**Fokus:** Insolvenzrechtsverfahren einfuehrend: Regelinsolvenz, Eigenverwaltung mit und ohne Schutzschirm, Verbraucher-Insolvenz, StaRUG-Restrukturierung. Pro Verfahrenstyp Schwelle, Antrag, Verlauf. Entscheidungstabelle.

# Insolvenzrecht: Verfahrenstypen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzrecht: Verfahrenstypen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Insolvenzrecht: Verfahrenstypen
- **Spezialgegenstand:** Insolvenzrecht: Verfahrenstypen / inso pl einfuehrung verfahrenstypen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG.
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

## 4. `insol-sanierungsgewinn-finanzamt-im-insolvenzverfahren`

**Fokus:** Finanzamt als Glaeubiger im Insolvenzverfahren. Paragraph 251 AO Aussetzung der Vollziehung, Paragraph 35 InsO Massezugehoerigkeit, Steuerforderungen als Insolvenzforderungen oder Masseverbindlichkeiten. Tabellenanmeldung der FA-Forderungen Paragraphen 174 ff. InsO. Steuerlicher Aufrechnungsschutz Paragraph 96 InsO. Schnittstelle zu Sanierungsgewinn. Mustertexte fuer Kommunikation mit dem Finanzamt.

# Sanierungsgewinn — Finanzamt im Insolvenzverfahren

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Finanzamt im Insolvenzverfahren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Das Finanzamt ist im Insolvenzverfahren ein Glaeubiger wie jeder andere — nicht mehr. Die Privilegierung des Fiskus aus frueheren Zeiten ist abgeschafft. Aber das Finanzamt ist ein Glaeubiger mit besonderen verfahrensrechtlichen Werkzeugen: Aufrechnung, Festsetzungsbescheid, Vollstreckungsanordnung. Im Sanierungs-Kontext kommt eine zusaetzliche Rolle hinzu: das FA entscheidet ueber die Anwendung Paragraph 3a EStG und Paragraph 7b GewStG.

Dieser Skill arbeitet die FA-Schnittstelle im Verfahren durch. Adressat: IV, Sachwalter, StB, Plan-Anwalt.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Verfahren ist eroeffnet; FA-Forderungen sind zu klassifizieren.
- Sanierungsplan wird vorbereitet; FA-Position zum Sanierungsertrag ist zentral.
- FA hat aufgerechnet oder vollstreckt; Pruefung der Zulaessigkeit.

Kaltstart-Fragen:

1. Welche Steuerforderungen sind angemeldet (Art, Hoehe, Zeitraum)?
2. Welche Forderungen entstanden vor Eroeffnung, welche danach?
3. Hat das FA aufgerechnet (Paragraph 96 InsO)?
4. Welche Steuern entstehen aus der Verwaltung der Masse?
5. Liegen bereits Bescheide vor, die strittig sind?

## Rechtlicher Rahmen

- Paragraph 251 AO — Steuerforderungen im Insolvenzverfahren.
- Paragraph 251 Absatz 2 AO — Aufrechnungsbeschraenkungen im Insolvenzverfahren.
- Paragraph 35 InsO — Massezugehoerigkeit.
- Paragraphen 38, 39 InsO — Insolvenzforderungen, Nachrang.
- Paragraph 55 InsO — Masseverbindlichkeiten.
- Paragraphen 174 ff. InsO — Forderungsanmeldung.
- Paragraph 96 InsO — Aufrechnungsverbote.
- Paragraph 226 AO — Aufrechnung mit Steuerforderungen.
- Paragraph 3a EStG, Paragraph 7b GewStG.

## / Schritt fuer Schritt

1. **Steuerforderungen klassifizieren.**
 - Vor Eroeffnung entstanden -> Insolvenzforderung Paragraph 38 InsO, zur Tabelle.
 - Nach Eroeffnung aus Verwaltung -> Masseverbindlichkeit Paragraph 55 InsO.
 - Nicht erfuellt verbliebene Anmeldungen -> Pruefung Paragraph 175 InsO.
2. **Aufrechnung pruefen.** Wenn das FA bereits aufgerechnet hat, Paragraph 96 InsO pruefen — Aufrechnungsverbote.
3. **Vollstreckungsverbot Paragraph 89 InsO** beachten — auch FA darf nicht in die Masse vollstrecken.
4. **Sanierungs-Antraege rechtzeitig stellen.** Vorabauskunft Paragraph 89 AO; mit Steuererklaerung Antrag Paragraph 3a EStG.
5. **Verhandlungslinie mit FA aufbauen.** Erlassantrag Paragraph 227 AO, Stundungsantrag Paragraph 222 AO.
6. **Im Plan**: FA als Glaeubiger der Insolvenzklasse oder eigene Klasse; Restbetraege nach Plan-Bestaetigung erlassen.

## Steuerforderungen klassifizieren

| Forderung | Klassifikation | Hinweis |
|---|---|---|
| KSt fuer Jahr vor Eroeffnung | Insolvenzforderung Paragraph 38 InsO | Anmeldung zur Tabelle |
| GewSt fuer Jahr vor Eroeffnung | Insolvenzforderung Paragraph 38 InsO | Gemeinde meldet an |
| USt aus Geschaeftsbetrieb nach Eroeffnung | Masseverbindlichkeit Paragraph 55 Absatz 1 Nr. 1 InsO | Aus Masse zu zahlen |
| LSt fuer fortgefuehrte Beschaeftigung | Masseverbindlichkeit Paragraph 55 InsO | Lohnzahlung loest LSt aus |
| KSt/GewSt auf Sanierungsertrag (verbleibender Restbetrag) | Masseverbindlichkeit Paragraph 55 InsO | erst nach Plan-Vollzug entstanden |
| GrESt auf Verwertung von Grundstuecken | Masseverbindlichkeit | aus Verwertung |
| Nicht beitreibbar versteuerte alte Schulden | bleibt offen | nach Restschuldbefreiung erlischt |

## Trade-off-Matrix Verhandlungen mit FA

| Option | Wann sinnvoll | Risiko |
|---|---|---|
| Paragraph 3a EStG-Antrag mit Steuererklaerung | Standard | FA pruefte Voraussetzungen genau |
| Vorabauskunft Paragraph 89 AO | bei hohem Volumen | Gebuehr, Zeitverzug |
| Stundungsantrag Paragraph 222 AO | wenn Restbetrag verbleibt | nur Aufschub |
| Erlassantrag Paragraph 227 AO | wenn Steuern unbillig | hohe Begruendungsanforderung |
| Tatsaechliche Verstaendigung Paragraph 78 AO | bei Beweisproblemen | nur fuer Tatfragen |
| Klage Finanzgericht | bei strittiger Rechtsfrage | langwierig |

## Praxistipps der alten Hasen

1. **FA-Forderungen pflegen.** Schnell klassifizieren, Tabellenanmeldung pruefen, Bestreitungen erwaegen.
2. **Aufrechnungsverbot Paragraph 96 InsO** hat enge Voraussetzungen — Pruefung im Einzelfall lohnt sich.
3. **FA-Vorabauskunft schriftlich.** Muendliche Aussagen des Sachbearbeiters sind kein Bindung.
4. **Plan-Klassenbildung pruefen.** FA kann als Glaeubiger in eigene Klasse, was die Mehrheits-Mathematik vereinfacht.
5. **Aktenzeichen-Disziplin.** Im FA-Bereich gibt es Steuernummer + Vorgangs-Az + ggf. Vollstreckungs-Az. Alle zitieren.
6. **Nach Plan-Bestaetigung Schlussrechnung mit FA.** Restbetraege nach Plan-Quote koennen ueber Paragraph 227 AO erlassen werden.

## Mustertexte / Berechnungsbeispiele

**Anschreiben an Finanzamt nach Verfahrenseroeffnung:**

```
[Briefkopf IV/Sachwalter]

An das Finanzamt [Ort]
Steuernummer [...]

In dem Insolvenzverfahren ueber das Vermoegen der [Schuldnerin],
Aktenzeichen Amtsgericht [Ort] [AZ]

Sehr geehrte Damen und Herren,

mit Beschluss des Amtsgerichts [Ort] vom [Datum] wurde ueber das Vermoegen
der oben bezeichneten Schuldnerin das Insolvenzverfahren eroeffnet. Ich
bin zum Insolvenzverwalter / Sachwalter bestellt.

Ich erlaube mir folgende Hinweise:

1. Anmeldung zur Tabelle
Bestehende Steuerforderungen aus Veranlagungszeitraeumen vor dem [Datum]
sind als Insolvenzforderungen Paragraph 38 InsO zur Insolvenztabelle
anzumelden (Paragraph 251 Absatz 3 AO i.V.m. Paragraphen 174 ff. InsO).
Hierzu ist anliegender Anmeldebogen.

2. Aufrechnungsverbot
Soweit Aufrechnungen vor oder nach Eroeffnung erfolgten, weise ich auf die
Aufrechnungsverbote Paragraph 96 InsO hin und bitte um Pruefung.

3. Vollstreckungsverbot
Zwangsvollstreckungsmassnahmen sind nach Paragraph 89 InsO unzulaessig.
Soweit Massnahmen anhaengig sind, bitte ich um Einstellung.

4. Sanierungsplan
Ein Insolvenzplan ist in Vorbereitung. Hierbei wird der Sanierungsertrag
nach Paragraph 3a EStG / Paragraph 7b GewStG beantragt werden. Eine
Vorabauskunft nach Paragraph 89 AO werde ich gesondert beantragen.

Mit freundlichen Gruessen
[Unterschrift]
```

## Typische Fehler

1. Steuerforderungen falsch klassifiziert — z. B. nach Eroeffnung entstandene Steuern als Insolvenzforderung.
2. Aufrechnungsverbot Paragraph 96 InsO uebersehen — FA-Aufrechnung wird nicht angegriffen.
3. Vorabauskunft nur muendlich erfragt.
4. Vollstreckungsverbot Paragraph 89 InsO nicht eingelegt.
5. Bei Plan: FA in keine eigene Klasse — Mehrheitsmathematik verkompliziert.
6. Schluss-Erlassantrag nach Plan-Vollzug vergessen.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — materielle Antragsmechanik.
- `insol-sanierungsgewinn-vergleich-mit-finanzamt-und-stundung` — Stundungs-/Erlassmechanik.
- `insol-sanierungsgewinn-massenpriorisierung-261-vs-3a-estg` — Massenpriorisierung.
- `forderungsanmeldung-glaeubiger-174-177-inso` — Tabellenanmeldung.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — Steuerverfahren.
- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.

## Quellen Stand 06/2026

- Paragraph 251 AO, `gesetze-im-internet.de/ao_1977/__251.html`.
- Paragraph 226 AO, `gesetze-im-internet.de/ao_1977/__226.html`.
- Paragraphen 35, 38, 39, 55, 89, 96, 174 ff. InsO, `gesetze-im-internet.de/inso/`.
- Paragraph 3a EStG.
- Paragraph 7b GewStG.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.
