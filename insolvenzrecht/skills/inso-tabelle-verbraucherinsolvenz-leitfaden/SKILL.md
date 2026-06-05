---
name: inso-tabelle-verbraucherinsolvenz-leitfaden
description: "Inso Tabelle Verbraucherinsolvenz Leitfaden: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inso Tabelle Verbraucherinsolvenz Leitfaden

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Inso Tabelle Verbraucherinsolvenz Leitfaden** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inso-tabelle-und-feststellung-spezial` | Spezialfall Tabelle und Feststellung: § 175 InsO Tabelle, § 176 InsO Pruefungstermin, § 178 InsO Wirkungen festgestellter Forderungen, Widerspruch durch Insolvenzverwalter oder anderen Glaeubiger. Pruefraster und Mustertexte. |
| `inso-verbraucherinsolvenz-leitfaden` | Leitfaden Verbraucherinsolvenz §§ 304 ff. InsO: aussergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, Restschuldbefreiung, Sperrfristen. Pruefraster Schuldnerberatung. |
| `insol-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg-im-plan` | Rangruecktritt und Paragraph 5 Absatz 2a EStG im Insolvenz- und StaRUG-Plan. Qualifizierter Rangruecktritt verhindert Passivierung. Abgrenzung zum Forderungsverzicht: bei Rangruecktritt bleibt die Verbindlichkeit zivilrechtlich, faellt aber bilanziell weg, wenn Tilgung nur aus kuenftigen Gewinnen/Liquidationserloesen erfolgt. Beziehung zu Sanierungsertrag. Mustertexte Rangruecktrittsvereinbarung. |
| `insolvenzgeld-165-sgb-iii` | Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei Monate vor Insolvenz-Ereignis. Insolvenz-Ereignis § 165 Abs. 1 SGB III Eroeffnung Abweisung mangels Masse Vollstreckungs-Aussichtslosigkeit. Antragsfrist zwei Monate § 324 SGB III Vor-Finanzierung Banken bis 75 Prozent. Output Antragsentwurf Bescheinigung Abrechnung Schnittstelle Sozialversicherungs-Beitraege. Abgrenzung: forderungsanmeldung-gläubiger für allgemeine Forderungsanmeldung. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Inso Tabelle Verbraucherinsolvenz Leitfaden**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `inso-tabelle-und-feststellung-spezial`

**Fokus:** Spezialfall Tabelle und Feststellung: § 175 InsO Tabelle, § 176 InsO Pruefungstermin, § 178 InsO Wirkungen festgestellter Forderungen, Widerspruch durch Insolvenzverwalter oder anderen Glaeubiger. Pruefraster und Mustertexte.

# InsO: Tabelle und Feststellung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `InsO: Tabelle und Feststellung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: InsO: Tabelle und Feststellung
- **Spezialgegenstand:** InsO: Tabelle und Feststellung / inso tabelle und feststellung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 2. `inso-verbraucherinsolvenz-leitfaden`

**Fokus:** Leitfaden Verbraucherinsolvenz §§ 304 ff. InsO: aussergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, Restschuldbefreiung, Sperrfristen. Pruefraster Schuldnerberatung.

# Inso: Verbraucherinsolvenz

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Inso: Verbraucherinsolvenz` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Inso: Verbraucherinsolvenz
- **Spezialgegenstand:** Inso: Verbraucherinsolvenz / inso verbraucherinsolvenz leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, BGH, BVerfG.
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

## 3. `insol-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg-im-plan`

**Fokus:** Rangruecktritt und Paragraph 5 Absatz 2a EStG im Insolvenz- und StaRUG-Plan. Qualifizierter Rangruecktritt verhindert Passivierung. Abgrenzung zum Forderungsverzicht: bei Rangruecktritt bleibt die Verbindlichkeit zivilrechtlich, faellt aber bilanziell weg, wenn Tilgung nur aus kuenftigen Gewinnen/Liquidationserloesen erfolgt. Beziehung zu Sanierungsertrag. Mustertexte Rangruecktrittsvereinbarung.

# Sanierungsgewinn — Rangruecktritt und Paragraph 5 Absatz 2a EStG im Plan

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Rangruecktritt und Paragraph 5 Absatz 2a EStG im Plan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der **qualifizierte Rangruecktritt** ist eine Alternative oder Ergaenzung zum Forderungsverzicht. Bei richtiger Gestaltung bleibt die Verbindlichkeit zivilrechtlich bestehen, faellt aber **bilanziell** als Verbindlichkeit weg, weil sie nur aus kuenftigen Gewinnen, freien Liquiditaetsueberschuessen oder einem Liquidationsueberschuss zu tilgen ist (Paragraph 5 Absatz 2a EStG). Steuerlich kann das einen Effekt aehnlich dem Forderungsverzicht haben — aber **ohne** sofortigen Sanierungsertrag, wenn die Vereinbarung sauber formuliert ist.

Dieser Skill zeigt die Mechanik und grenzt sie zum Forderungsverzicht ab. Adressat: Plan-Anwalt, IV/Sachwalter, StB.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Plan sieht statt Verzicht eine Rangruecktrittsvereinbarung vor.
- Glaeubiger will nicht endgueltig verzichten, aber bilanziell Erleichterung verschaffen.
- Steuerlich soll vermieden werden, dass ein Sanierungsertrag entsteht, falls Paragraph 3a EStG-Voraussetzungen unsicher sind.

Kaltstart-Fragen:

1. Wer trifft die Rangruecktrittsvereinbarung (Drittglaeubiger, Gesellschafter, Bank)?
2. Hoehe der betroffenen Forderung?
3. Soll die Vereinbarung qualifiziert oder nur einfach sein?
4. Existiert bereits eine Insolvenzantragspflicht (Paragraph 15a InsO) — Rangruecktritt zur Vermeidung der Ueberschuldung?
5. Wird der Rangruecktritt mit Forderungsverzicht kombiniert?

## Rechtlicher Rahmen

- Paragraph 5 Absatz 2a EStG — Passivierungsverbot fuer Verbindlichkeiten, die nur aus kuenftigen Einnahmen oder Liquidationsueberschuessen zu tilgen sind.
- Paragraph 19 Absatz 2 Satz 2 InsO — qualifizierter Rangruecktritt im Ueberschuldungsstatus.
- Paragraph 39 Absatz 2 InsO — vereinbarter Nachrang.
- Paragraph 39 Absatz 1 Nr. 5 InsO — Gesellschafterdarlehen.
- Paragraph 3a EStG — Sanierungsertrag (Abgrenzung).
- BFH-Linie: "qualifizierter Rangruecktritt" als steuerliche Anerkennungsschwelle.

## / Schritt fuer Schritt

1. **Zweck klaeren.** Geht es um Beseitigung der Ueberschuldung (insolvenzrechtlich) oder um Sanierungsertrag-Vermeidung (steuerlich) oder beides?
2. **Qualifizierten Rangruecktritt formulieren** mit drei Elementen:
 - Nachrang hinter alle Insolvenzglaeubiger.
 - Tilgung nur aus kuenftigen Gewinnen, freien Liquiditaetsueberschuessen oder Liquidationsueberschuss.
 - Glaeubiger verpflichtet sich, nicht in einer Weise Tilgung zu verlangen, die einen Insolvenzgrund ausloest.
3. **Pruefen Paragraph 5 Absatz 2a EStG.** Wenn Tilgung **nur** aus kuenftigen Einnahmen / Liquidationsueberschuss zu erfolgen hat, ist Passivierung verboten. Wenn Tilgung "auch" aus laufenden Mitteln moeglich ist, ist die Passivierungspflicht zu pruefen.
4. **Plan-Klausel formulieren.**
5. **Abgrenzung zum Verzicht: Bei Rangruecktritt bleibt die Forderung; bei Verzicht erlischt sie.** Steuerlich kann der Rangruecktritt im Ergebnis zu einem aehnlichen Effekt fuehren, ohne dass sofort ein Sanierungsertrag entsteht.
6. **Spaetere Tilgung pruefen:** Wenn die Tilgung tatsaechlich erfolgt, ist die Bilanz wieder zu korrigieren.

## Trade-off-Matrix

| Gestaltung | Wirkung | wann sinnvoll |
|---|---|---|
| Qualifizierter Rangruecktritt mit Passivierungsverbot Paragraph 5 Absatz 2a EStG | bilanziell wie Verzicht, kein Sanierungsertrag | wenn Paragraph 3a EStG-Voraussetzungen unsicher |
| Einfacher Nachrang (Paragraph 39 Absatz 2 InsO ohne Paragraph 5 Absatz 2a-Wirkung) | Verbindlichkeit bleibt passiviert | wenn nur Ueberschuldungsstatus-Wirkung gewuenscht |
| Verzicht endgueltig | Sanierungsertrag, Paragraph 3a EStG erforderlich | wenn Paragraph 3a-Voraussetzungen sicher und Glaeubiger einverstanden |
| Verzicht mit Besserungsschein | Sanierungsertrag im Verzichtsjahr; Rueckbuchung bei Eintritt | wenn Hoffnungswert besteht |
| Kombination Rangruecktritt + Teilverzicht | Mischung, Steuerung des Sanierungsertrags-Volumens | bei groesseren Volumen sinnvoll |

## Praxistipps der alten Hasen

1. **Formulierung "nur aus kuenftigen Gewinnen oder Liquidationsueberschuss"** ist der Schluessel fuer Paragraph 5 Absatz 2a EStG. Wer "auch aus freien Mitteln" zulaesst, faellt aus dem Passivierungsverbot.
2. **Insolvenzrechtliche Wirkung allein kommt aus Paragraph 19 Absatz 2 Satz 2 InsO.** Steuerliche Wirkung kommt aus Paragraph 5 Absatz 2a EStG. Beide Wirkungen brauchen unterschiedliche Klauseln.
3. **Bei Gesellschafterdarlehen** ist Paragraph 39 Absatz 1 Nr. 5 InsO ohnehin Nachrang — eine zusaetzliche Vereinbarung gibt aber die steuerlich gewuenschte Wirkung.
4. **Rangruecktritt fuer kuenftige Tilgung schreibfest machen.** Wenn der Schuldner spaeter wieder profitabel ist, soll die Tilgung nicht aus Versehen Steuerfolgen ausloesen.
5. **Rangruecktritt im Insolvenzplan-Text aufnehmen.** Im Plan ist Bestimmtheit Paragraph 221 InsO Pflicht; nur dann wirkt Paragraph 254 Absatz 1 InsO.
6. **Wichtiger Sonderfall:** Wenn die Rangruecktrittsvereinbarung erst nach Verfahrenseroeffnung getroffen wird, sind Paragraphen 80, 81 InsO zu beachten.

## Mustertexte / Berechnungsbeispiele

**Muster qualifizierter Rangruecktritt (kombinierte Wirkung Paragraph 19 InsO und Paragraph 5 Absatz 2a EStG):**

```
RANGRUECKTRITTSVEREINBARUNG

zwischen
[Glaeubiger] (Glaeubiger)
und
[Schuldnerin] (Schuldnerin)

§ 1 Gegenstand
Die Schuldnerin schuldet dem Glaeubiger aus [Vertrag] vom [Datum] einen
Betrag von EUR [Betrag] nebst Zinsen.

§ 2 Rangruecktritt
1. Der Glaeubiger tritt mit seinen Forderungen aus § 1 im Rang hinter alle
gegenwaertigen und zukuenftigen Forderungen anderer Glaeubiger der
Schuldnerin im Sinne von § 39 Absatz 2 InsO zurueck.

2. Die Forderungen des Glaeubigers werden nur aus
a) kuenftigen Gewinnen der Schuldnerin,
b) einem etwaigen Liquidationsueberschuss oder
c) sonstigem freien Vermoegen der Schuldnerin, soweit Aufzehrung des
 Stammkapitals oder Insolvenzantragspflicht nach § 15a InsO nicht
 ausgeloest wird,
befriedigt.

3. Der Glaeubiger verpflichtet sich, Tilgung oder Befriedigung nicht zu
verlangen, wenn dies einen Insolvenzgrund nach § 17 oder § 19 InsO
ausloesen wuerde.

§ 3 Steuerliche Behandlung
Die Parteien sind sich einig, dass diese Vereinbarung sowohl
insolvenzrechtlich (Vermeidung der Ueberschuldung im Sinne von § 19
Absatz 2 Satz 2 InsO) als auch steuerlich (Passivierungsverbot nach § 5
Absatz 2a EStG) wirken soll. Sie ist als qualifizierter Rangruecktritt
auszulegen.

§ 4 Befristung
Diese Vereinbarung ist unbefristet. Sie kann nur einvernehmlich oder im
Rahmen eines bestaetigten Plans (InsO/StaRUG) aufgehoben werden.

[Ort, Datum, Unterschriften]
```

**Plan-Klausel im gestaltenden Teil:**

```
VII. Rangruecktritte

1. Die Forderungen der in Anlage R aufgefuehrten Glaeubiger gegen die
Schuldnerin treten mit Bestaetigung dieses Plans und Rechtskraft des
Bestaetigungsbeschlusses im Rang hinter alle gegenwaertigen und
zukuenftigen Forderungen der uebrigen Glaeubiger zurueck (Paragraph 39
Absatz 2 InsO).

2. Tilgung erfolgt ausschliesslich aus kuenftigen Gewinnen oder einem
etwaigen Liquidationsueberschuss der Schuldnerin.

3. Die in Anlage R aufgefuehrten Glaeubiger verzichten darauf, Tilgung zu
verlangen, wenn dies einen Insolvenzgrund nach Paragraph 17 oder
Paragraph 19 InsO ausloesen wuerde.

4. Diese Vereinbarung ist als qualifizierter Rangruecktritt im Sinne von
Paragraph 5 Absatz 2a EStG zu verstehen. Die betroffenen Verbindlichkeiten
werden bilanziell aufgeloest; der hieraus resultierende Ertrag ist im
Rahmen der Steuererklaerung als Sanierungsertrag nach Paragraph 3a EStG
zu behandeln, soweit die dortigen Voraussetzungen erfuellt sind.
```

## Typische Fehler

1. Rangruecktritt nur insolvenzrechtlich gestaltet — steuerliche Passivierungswirkung verfehlt.
2. Klausel laesst Tilgung auch aus laufenden Mitteln zu — Paragraph 5 Absatz 2a EStG greift nicht.
3. Annahme, Rangruecktritt loese **keinen** Effekt aus — bei Aufloesung der Verbindlichkeit kann ein Ertrag entstehen, der dann ggf. Paragraph 3a EStG-Pruefung braucht.
4. Verwechslung mit Verzicht.
5. Spaetere Tilgung nicht buchhalterisch dokumentiert.
6. Bei Gesellschafterdarlehen vergessen, dass Paragraph 39 Absatz 1 Nr. 5 InsO ohnehin Nachrang vorsieht — die Vereinbarung verstaerkt das nur.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-verzicht-bilanz-im-plan` — Verzichts-Variante.
- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Sanierungsertrag.
- `insol-sanierungsgewinn-debt-equity-swap-im-plan` — DES.
- `ueberschuldung-pruefung-19-inso` — Ueberschuldungspruefung.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — allgemeine Steuerthemen.
- `fortbestehensprognose` — Fortbestehensprognose und Rangruecktritt.

## Quellen Stand 06/2026

### Normen

- Paragraph 5 Absatz 2a EStG, `gesetze-im-internet.de/estg/__5.html`.
- Paragraph 19 InsO, `gesetze-im-internet.de/inso/__19.html`.
- Paragraph 39 InsO, `gesetze-im-internet.de/inso/__39.html`.
- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraph 254 InsO, `gesetze-im-internet.de/inso/__254.html`.
- Paragraph 6 Absatz 1 Nummer 3 EStG i.V.m. Paragraph 12 Absatz 1 BewG (Nennwert).
- Paragraph 11 KStG (Liquidationsbesteuerung).

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — Kernentscheidung zur Anwendung des Paragraph 5 Absatz 2a EStG bei Rangruecktritt mit Tilgungsvorbehalt aus zukuenftigen Gewinnen. Maszgeblich fuer die Gestaltungspraxis.
- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Passivierung nur bei wirtschaftlicher Belastung. Begruendet die Pruefungstrias: bestimmter Verpflichtungsinhalt, durchsetzbar, wirtschaftliche Belastung.
- **FG Koeln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** — Os. 7: Rangruecktrittsbehaftete Verbindlichkeit bleibt bis Loeschung passiviert; rechtstheoretisch entstehender Gewinn mangels Steuersubjekt nicht steuerpflichtig (vorgehend zu BFH I R 34/12).
- **BFH, Beschl. v. 05.02.2014 — I R 34/12, BFH/NV 2014, 1014** — bestaetigt FG-Koeln-Linie als „nicht evident rechtsfehlerhaft".

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfuegung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782**, Tz. 1.2-1.4 — ertragsteuerliche Beurteilung von Darlehensverbindlichkeiten der Mutter im Abwicklungsendvermoegen der Tochter; bei laufender Aktualisierung mit Bund-Laender-Abstimmung.
- **OFD Frankfurt a. M., Rundverfuegung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560** — Vorgaengerverfuegung.
- **OFD Nordrhein-Westfalen, Kurzinformation ESt Nr. 46/2014, akt. 22.09.2017, DB 2017, 2580** — Sichtweise NRW (insbesondere Insolvenz).

### Literatur

- Bergmann, Liquidationsbesteuerung von Kapitalgesellschaften, Diss., 2012, S. 145 ff.
- Dietrich/Weber, DStR 2019, 966, 970.
- Hageboeke, in: Roedder/Herlinghaus/Neumann, KStG, 1. Aufl. 2015, Paragraph 11 Rn. 78.
- Stalbold, in: Gosch, KStG, Paragraph 11 Rn. 72.

### Querverweise

- `stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` (Drei-Phasen-Analyse fuer die Liquidation).

Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 4. `insolvenzgeld-165-sgb-iii`

**Fokus:** Arbeitnehmer eines insolventen Unternehmens will Insolvenzgeld beantragen oder Insolvenzverwalter bearbeitet Insolvenzgeld-Anmeldungen. Prüfraster § 165 ff. SGB III Anspruchs-Voraussetzungen Arbeitsentgelt letzte drei Monate vor Insolvenz-Ereignis. Insolvenz-Ereignis § 165 Abs. 1 SGB III Eroeffnung Abweisung mangels Masse Vollstreckungs-Aussichtslosigkeit. Antragsfrist zwei Monate § 324 SGB III Vor-Finanzierung Banken bis 75 Prozent. Output Antragsentwurf Bescheinigung Abrechnung Schnittstelle Sozialversicherungs-Beitraege. Abgrenzung: forderungsanmeldung-gläubiger für allgemeine Forderungsanmeldung.

# Insolvenzgeld nach § 165 SGB III

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzgeld nach § 165 SGB III` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Insolvenzgeld ist zentrale Arbeitnehmer-Sicherung in Insolvenz. Mandanten oft Arbeitnehmer oder Insolvenzverwalter im Lohn-Abrechnungs-Streit. Dieses Skill prüft Anspruch und Antrags-Verfahren.

## Eingaben

- Insolvenz-Status Arbeitgeber (Antrag Eröffnung)
- Arbeitsverhältnis-Daten (Dauer Lohn Stunden)
- Lohnverzug-Zeitraum
- Bisher gezahlter Lohn
- Bei Mandant=Insolvenzverwalter: Mitarbeiter-Liste

## Schritt 1 — Anspruchs-Voraussetzungen § 165 SGB III

### Persönlich Berechtigte

- **Arbeitnehmer** im Sinne § 7 SGB IV
- **Auszubildende**
- **Heimarbeiter**
- Einschluss Mini-Job-Beschäftigte
- Einschluss Teilzeit

### Nicht berechtigt

- Geschäftsführer ohne Arbeitnehmer-Status
- Selbstständige
- Arbeitnehmer in Drittland-Filialen ohne deutschen Sozial-Versicherungs-Bezug

## Schritt 2 — Insolvenz-Ereignis § 165 Abs. 1 SGB III

### Drei Tatbestände

a) **Eröffnung des Insolvenz-Verfahrens** über Vermögen des Arbeitgebers

b) **Abweisung mangels Masse** § 26 InsO

c) **Vollständige Betriebs-Einstellung** im Inland, wenn ein Insolvenz-Antrag nicht gestellt worden ist und ein Insolvenz-Verfahren offensichtlich mangels Masse nicht in Betracht kommt

### Zeit-Punkt

- **Eröffnungs-Datum** als Insolvenz-Ereignis-Datum
- Bei Abweisung mangels Masse: Abweisungs-Beschluss
- Bei Betriebs-Einstellung: tatsächliche Einstellungs-Datum

## Schritt 3 — Anspruchs-Inhalt § 167 SGB III

### Lohn der letzten drei Monate

- **Rückwärts vom Insolvenz-Ereignis-Datum**
- Nur **noch nicht gezahltes Arbeitsentgelt**
- Brutto-Forderung bis Beitrags-Bemessungs-Grenze West / Ost

### Beispiel

```
Insolvenz-Ereignis (Eröffnung): 15.05.2026
Lohn-Forderungen:
- Februar 2026: bezahlt
- März 2026: nicht bezahlt (EUR 3.500)
- April 2026: nicht bezahlt (EUR 3.500)
- Mai 2026 anteilig: nicht bezahlt (EUR 1.700)

Anspruch Insolvenzgeld: 3 Monate
- Februar nicht relevant (bezahlt)
- Mitte Feb bis Mitte Mai = drei Monate
- Berechnung: EUR 3.500 × 2 + EUR 1.700 = EUR 8.700

Bei Beitrags-Bemessungs-Grenze (West EUR 7.550/Monat
in 2026) liegt EUR 3.500 darunter — voller Anspruch
```

### Brutto vs. Netto

- Insolvenzgeld in Höhe Netto-Anspruch
- Steuer und SV-Anteile separat berechnet
- Lohnsteuer-Klassen-bezogen

### Sonderzuwendungen

- Urlaubsgeld Weihnachtsgeld nur anteilig
- Bei Fälligkeit innerhalb der drei Monate
- Provisionen bei Fälligkeit

## Schritt 4 — Antragsverfahren

### Frist § 324 SGB III

- **Zwei Monate** ab Insolvenz-Ereignis
- **Nach-Antragsfrist sechs Monate** bei unverschuldeter Versäumnis
- Frist-Beginn bei Bekanntwerden Insolvenz-Ereignis

### Antragstellung

- **Agentur für Arbeit** zuständig
- **Online-Antrag** über BA-Webportal
- **Schriftlich** möglich

### Pflicht-Anlagen

- Arbeitsvertrag
- Lohn-Abrechnungen
- Bescheinigung Insolvenz-Verwalter (Lohn-Forderung)
- Lohn-Steuer-Karte / Identifikations-Nummer

### Bescheinigung Insolvenz-Verwalter

- **Pflicht** des Insolvenz-Verwalters auf Anfrage
- Inhalt: Lohn-Höhe Fälligkeit Erfüllungs-Stand
- Schnittstelle zur Forderungs-Anmeldung

## Schritt 5 — Insolvenzgeld-Anspruchs-Übergang § 169 SGB III

### Cessio Legis

- **Lohn-Forderung geht auf BA über** mit Zahlung Insolvenzgeld
- **Anmeldung zur Insolvenz-Tabelle** durch BA
- Insolvenz-Verwalter rechnet mit BA ab

### Folge für Insolvenz-Verwalter

- BA wird Gläubiger anstelle Arbeitnehmer
- Pflicht-Vermerk in Tabelle
- Quoten-Auszahlung an BA

### Folge für Arbeitnehmer

- **Insolvenzgeld** ohne Anmeldung in Tabelle
- Bei Differenz Lohn über Beitrags-Bemessungs-Grenze — Differenz selbst anmelden

## Schritt 6 — Vor-Finanzierung

### Praktische Konstellation

- Insolvenz-Verfahren dauert
- Arbeitnehmer braucht Geld sofort
- Vor-Finanzierung durch Bank

### Vor-Finanzierungs-Vereinbarung § 170 SGB III

- **Banken-Vorfinanzierung** bis 75 Prozent Insolvenzgeld
- **Abtretung** an Bank
- BA zahlt direkt an Bank

### Vorteil Arbeitnehmer

- Schnelle Liquidität
- Schon vor Insolvenz-Ereignis möglich (in der drei-Monats-Phase)

### Vorteil Insolvenz-Verfahren

- **Fortführungs-Möglichkeit** durch Lohn-Sicherung
- **Mitarbeiter-Bindung**
- Sanierungs-Chance

## Schritt 7 — Bei Eigenverwaltung

- Anspruch Insolvenzgeld bleibt
- Sachwalter unterstützt Anträge
- Schnellere Auszahlung möglich

## Schritt 8 — Sozial-Versicherungs-Beiträge § 173 SGB III

### Pflicht-Beiträge auf Insolvenzgeld

- **Renten-Versicherung** Krankenversicherung Pflege-Versicherung Arbeitslosen-Versicherung
- **BA übernimmt** Arbeitgeber-Anteil
- **Anwartschafts-Schutz** Arbeitnehmer

### Folge

- Keine Lücke in Sozial-Versicherungs-Karriere
- Renten-Punkte werden weitergeführt

## Schritt 9 — Anspruchs-Konkurrenz

### Kurzarbeitergeld

- Bei vor Insolvenz Kurzarbeit
- Anspruch Kurzarbeitergeld parallel möglich
- Anrechnung-Mechanismen

### Krankengeld

- Bei Erkrankung in Drei-Monats-Phase
- Krankengeld plus Insolvenzgeld theoretisch
- Vorrang-Regelungen

### Mutterschaftsgeld / Elterngeld

- Spezifische Regelungen
- Sozial-Versicherungs-Karten

### Vorruhestand / Frühverrentung

- Anspruch endet mit Renteneintritt
- Insolvenzgeld dazwischen möglich

## Schritt 10 — Praktische Konstellationen

### Konstellation A — Insolvenz-Verfahren eröffnet

- Klar: Antragsfrist läuft
- Insolvenz-Verwalter-Bescheinigung anfordern
- Antrag stellen

### Konstellation B — Insolvenz-Antrag gestellt aber noch nicht eröffnet

- Vor-Finanzierungs-Vereinbarung möglich
- Antragsfrist beginnt erst mit Eröffnung

### Konstellation C — Eröffnung verzögert sich

- Eilbedürftigkeits-Erklärung an Insolvenz-Gericht
- Vor-Finanzierung erwägen

### Konstellation D — Abweisung mangels Masse

- Insolvenz-Ereignis ist Abweisung
- Antragsfrist ab Abweisungs-Beschluss
- Häufig parallel zu fehlender Insolvenz-Verwalter-Bescheinigung — Eigenbescheinigung-Eskalation

### Konstellation E — Lohn-Verzug ohne Insolvenz-Antrag

- Kein Insolvenzgeld
- Lohn-Klage Arbeitsgericht
- Bei Vermögens-Aussichts-Losigkeit Insolvenz-Antrag möglicherweise

## Schritt 11 — Aufgaben Insolvenz-Verwalter

### Lohn-Erfassung

- Lohnkonten der letzten Monate prüfen
- Lohn-Forderungen exakt aufstellen
- Lohnsteuerkarten und SV-Daten besorgen

### Bescheinigung Insolvenzgeld

- Auf Anfrage Mitarbeiter
- Standardisiertes Formular
- Frist-eng (sieben Werktage)

### Lohn-Buchhaltung Übergang

- Übernahme der Lohn-Buchhaltung
- Steuer- und SV-Anmeldungen ggf.
- Pension-Verpflichtungen-Übergang an PSVaG

### Massearm-Konstellation

- Bei Abweisung mangels Masse keine Bescheinigung-Pflicht
- Arbeitnehmer-Eigenangabe möglich

## Schritt 12 — Bei Streit über Insolvenzgeld-Anspruch

### Widerspruch BA-Bescheid

- **Ein Monat** ab Bekanntgabe, § 84 Abs. 1 SGB X i. V. m. §§ 78 ff. SGG
- Begründung
- An BA selbst

### Klage SG

- Bei Widerspruchs-Bescheid abgelehnt
- **Ein Monat** Klage-Frist § 87 Abs. 1 SGG (drei Monate wäre § 88 SGG Untätigkeitsklage)
- PKH-Antrag empfohlen → Skill `pkh-erfolgsaussicht-pruefen`

### Häufige Streit-Punkte

- **Persönlicher Anwendungsbereich** (echte Arbeitnehmer-Eigenschaft?)
- **Berechnungs-Grundlage** (Pauschalen Provisionen)
- **Drei-Monats-Phase** korrekt berechnet?
- **Bezogen-Frist** § 324 versäumt?

## Schritt 13 — Schnittstelle Forderungs-Anmeldung Tabelle

### Forderungs-Anmeldung § 174 InsO

- Bei Insolvenzgeld-Übergang BA als Gläubiger
- Restbetrag Lohn (über Beitrags-Bemessungs-Grenze) Arbeitnehmer selbst
- Skill `glaeubigerantrag-pruefung`

### Rang (wichtige Korrektur)

- **Lohn-Forderungen aus der Zeit VOR Eröffnung** sind grundsätzlich **einfache Insolvenz-Forderungen** § 38 InsO mit Quoten-Risiko — auch wenn sie aus den letzten Monaten stammen
- **Masseverbindlichkeiten** sind nur:
 - Lohn aus **fortbestehendem** Arbeitsverhältnis NACH Verfahrens-Eröffnung → § 55 Abs. 1 Nr. 2 InsO
 - im Eröffnungs-Verfahren begründete Lohn-Ansprüche bei starkem vorläufigen Verwalter mit Verfügungs-Befugnis → § 55 Abs. 2 InsO
- Für Rückstände aus den drei Monaten vor Insolvenz-Ereignis greift das Insolvenzgeld § 165 SGB III; die Forderung selbst geht auf die BA über (§ 169 SGB III) und wird als § 38 InsO-Forderung angemeldet
- § 55 Abs. 2 InsO hilft NICHT pauschal für die "letzten sechs Monate vor Eröffnung" — das ist ein verbreiteter Irrtum

## Verzahnung mit anderen Skills

- `mandat-triage-insolvenzrecht` — Einstieg
- `arbeitsrecht-kaltstart-interview` — Arbeitsrechtliche Aspekte
- `kuendigungsschutzklage` — wenn parallel Kündigung
- `pkh-erfolgsaussicht-pruefen` — bei SG-Klage gegen BA-Bescheid
- `glaeubigerantrag-pruefung` — Forderungs-Anmeldung

## Ausgabe

- `insolvenzgeld-{az}.md` mit Anspruchs-Prüfung Antragsstellung
- BA-Antragsschrift
- Insolvenz-Verwalter-Bescheinigungs-Anforderung
- Bei Streit: Widerspruchs-/Klage-Vorbereitung
- Vor-Finanzierungs-Beratung
- Frist im Fristenbuch (zwei Monate Antrag, ein Monat Widerspruch, ein Monat Klage)

## Quellen

- SGB III §§ 165 167 169 170 173 324
- SGB IV § 7
- SGG §§ 87 88; SGB X § 84
- InsO §§ 26 38 55 174
- BSG-Linien zu Insolvenzgeld
- Standes-Vorgaben Insolvenz-Verwalter zu Lohn-Bescheinigung


## Aktuelle Leitentscheidungen — Insolvenzgeld

- Konkrete BSG- und LSG-Entscheidungen zum Insolvenzgeld (insb. Anspruchsberechtigung Gesellschafter-Geschäftsführer, Drei-Monats-Frist, Vorfinanzierung) vor Ausgabe über sozialgerichtsbarkeit.de oder dejure.org mit Datum und Aktenzeichen verifizieren.
- Zur Schnittstelle § 142 InsO (Bargeschäft Lohnzahlungen) und Anfechtung: **BGH IX ZR 122/23 vom 05.12.2024** stellt klar, dass Lohnzahlungen ohne starre 30-Tage-Grenze auf engen zeitlichen Zusammenhang zu prüfen sind; bei Anfechtung des Verwalters gegen vorinsolvenzliche Lohnzahlungen ist die Unlauterkeit konkret darzulegen.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>

## Paragrafenkette Insolvenzgeld

§ 165 SGB III (Anspruchsvoraussetzungen) → § 166 SGB III (Hoehe) → § 167 SGB III (Vorfinanzierung) → § 168 SGB III (Erloesch-Gruende) → § 26 InsO (Abweisung mangels Masse als Insolvenzereignis) → § 113 InsO (Kuendigungsrecht des IV)

## Triage — Insolvenzgeld

1. **Insolvenzereignis?** Datum der Verfahrenseroffnung oder Abweisung mangels Masse exakt festlegen.
2. **3-Monats-Zeitraum?** Welche Monate werden vom Insolvenzgeld abgedeckt? Lohnrueckstaende inventarisieren.
3. **Vorfinanzierung?** Haushausbank ansprechen; Abtretungserklaerungen der Arbeitnehmer einholen; Zeitplan Vorfinanzierung → Auszahlung BA.
4. **GF-Anspruch?** GF ist nur Arbeitnehmer wenn tatsaechlich weisungsgebunden; bei Gesellschafter-GF selten Insolvenzgeld.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
