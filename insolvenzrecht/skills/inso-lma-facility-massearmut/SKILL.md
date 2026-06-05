---
name: inso-lma-facility-massearmut
description: "Inso LMA Facility Massearmut: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inso LMA Facility Massearmut

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Inso LMA Facility Massearmut** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inso-lma-facility-agent-und-syndikat` | Prüft syndizierte LMA-Finanzierung in Insolvenz/StaRUG: Facility Agent, Security Agent, Majority Lenders, Waiver, Standstill, Acceleration und Forderungsanmeldung. |
| `inso-massearmut-massekostenmangel-spezial` | Spezialfall Massearmut und Massekostenmangel § 207 InsO: Einstellung mangels Masse, Verfahrenskostenstundung, Restschuldbefreiung. Pruefraster fuer Schuldner und Verwalter. |
| `inso-negativeintrag-bestreiten-belegpaket` | Belegpaket gegen negative Auskunfteieinträge: Beschlüsse, Registerauszüge, Erledigungsnachweise, Löschfristen, Auskunft und Versandnachweis. |
| `inso-neustart-bonitaet-konto-kredit` | Praktischer Neustart nach Restschuldbefreiung: Basiskonto, Kreditfähigkeit, Vermieter-/Bankauskunft, Löschung, Berichtigung und Dokumentation. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Inso LMA Facility Massearmut**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `inso-lma-facility-agent-und-syndikat`

**Fokus:** Prüft syndizierte LMA-Finanzierung in Insolvenz/StaRUG: Facility Agent, Security Agent, Majority Lenders, Waiver, Standstill, Acceleration und Forderungsanmeldung.

# Insolvenz: LMA Facility, Agent und Syndikat

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenz: LMA Facility, Agent und Syndikat` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Wofür dieser Arbeitsgang da ist

Der Skill trennt vertragliche Syndikatslogik von insolvenzrechtlicher Gläubigerstellung.

## Rechts- und Praxisanker

InsO, StaRUG, BGB, Sicherheitenrecht, hochgeladener Kreditvertrag.

## Workflow

1. Hochgeladenes Finanzierungsdokument, Schuldschein, Transfer Notice, LMA Facility Agreement oder NPL-Portfolio zuerst identifizieren.
2. Parteiperspektive, Deal-Ziel, Fristen, Consent-Erfordernisse, Sicherheiten und Datenschutzfragen klären.
3. Übertragungsweg, Rechtswirkung, offene Dokumente und Risiken in einer Closing-/Verfahrensmatrix darstellen.
4. Bei Insolvenz-/Krisenbezug Rang, Anfechtung, Planrechte, Enforcement und Geschäftsleiterpflichten gesondert prüfen.

## Output

- Transfer-Memo
- Closing-Checkliste
- Risikoampel mit Unterlagenliste
- Notice-/Q&A-Entwurf, falls genügend Angaben vorliegen

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 2. `inso-massearmut-massekostenmangel-spezial`

**Fokus:** Spezialfall Massearmut und Massekostenmangel § 207 InsO: Einstellung mangels Masse, Verfahrenskostenstundung, Restschuldbefreiung. Pruefraster fuer Schuldner und Verwalter.

# Inso: Massearmut Massekostenmangel

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Inso: Massearmut Massekostenmangel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Inso: Massearmut Massekostenmangel
- **Spezialgegenstand:** Inso: Massearmut Massekostenmangel / inso massearmut massekostenmangel spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO.
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

## 3. `inso-negativeintrag-bestreiten-belegpaket`

**Fokus:** Belegpaket gegen negative Auskunfteieinträge: Beschlüsse, Registerauszüge, Erledigungsnachweise, Löschfristen, Auskunft und Versandnachweis.

# Negativeintrag bestreiten: Belegpaket

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Negativeintrag bestreiten: Belegpaket` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Einsatz

Für die praktische Durchsetzung gegenüber Auskunftei, Bank, Vermieter oder Plattform.

## Norm- und Quellenanker

- InsO-Beschlüsse: Eröffnung, Restschuldbefreiung, Aufhebung/Einstellung, Insolvenzbekanntmachungen und Registerauszüge als Primärbelege.
- DSGVO Art. 5, 12, 15, 16, 17, 18, 21 für Auskunft, Berichtigung, Löschung/Einschränkung und Widerspruch.
- EuGH/BGH-/OLG-Rechtsprechung zu Auskunfteien, Restschuldbefreiung und Speicherfristen nur mit Datum, Aktenzeichen und freier Quelle zitieren.
- ZPO-Beweislogik: Zugang, Inhalt, Versandweg und Identität der betroffenen Person beweisbar halten.

## Arbeitsfragen

1. Welche Originalnachweise sind nötig?
2. Welche Stellen müssen gleichzeitig angeschrieben werden?
3. Wie wird Zugang bewiesen?
4. Welcher Eintrag ist falsch: Person, Datum, Forderung, Erledigung, Insolvenzereignis, Score-Grundlage oder Dublette?
5. Ist die gesetzliche Veröffentlichung bereits gelöscht/abgelaufen und welche private Speicherlogik behauptet die Auskunftei?
6. Welche Folgeadressaten brauchen Korrektur: Bank, Vermieter, Leasing, Plattform, Arbeitgeber, Versicherung?

## Output

Belegpaket mit Anlagenverzeichnis, Auskunftsantrag, Lösch-/Berichtigungsverlangen, Versandmatrix, Fristenkontrolle und Eskalation an Datenschutzaufsicht/Gericht.

## Red Flags

- nur Screenshot statt Beschluss
- Zugang nicht beweisbar
- verschiedene Namens-/Adressvarianten

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 4. `inso-neustart-bonitaet-konto-kredit`

**Fokus:** Praktischer Neustart nach Restschuldbefreiung: Basiskonto, Kreditfähigkeit, Vermieter-/Bankauskunft, Löschung, Berichtigung und Dokumentation.

# Neustart nach Insolvenz: Konto, Kredit, Bonität

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Neustart nach Insolvenz: Konto, Kredit, Bonität` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Einsatz

Für Verbraucher und ehemals Selbstständige, die nach Insolvenz wieder handlungsfähig werden wollen.

## Norm- und Quellenanker

InsO §§ 286 ff., 301; ZKG Basiskonto; DSGVO Art. 15–22; BGB.

## Arbeitsfragen

1. Welche Verträge scheitern an Bonität?
2. Welche Daten sind falsch/alt?
3. Welche Mindestversorgung wie Basiskonto?

## Output

Neustart-Checkliste, Auskunftskaskade und Musterschreiben an Bank/Vermieter/Auskunftei.

## Red Flags

- neue Ablehnung ohne Grund
- alte erledigte Forderungen
- Basiskonto verweigert

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.
