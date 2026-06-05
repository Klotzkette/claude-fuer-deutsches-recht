---
name: orientierung-triage-paragraph-stgb-besonders
description: "Orientierung Triage Paragraph Stgb Besonders: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Orientierung Triage Paragraph Stgb Besonders

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Orientierung Triage Paragraph Stgb Besonders** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `orientierung-strafzumessung-triage` | Einstieg und Triage im Plugin Strafzumessung. Ordnet das Mandat (Strafverteidiger, Staatsanwaltschaft, Beistand) nach Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe), erkennt Eilfristen, schlaegt passende Fachmodule aus diesem Plugin vor und liefert bei klarer Faktenlage sofort einen ersten Strafzumessungsentwurf mit Platzhaltern. |
| `paragraph-46-stgb-grundsatz-strafzumessung` | Grundsatznorm der Strafzumessung § 46 StGB. Schuld als Grundlage (Abs. 1 Satz 1), praeventive Wirkungen auf das kuenftige Leben des Taeters (Abs. 1 Satz 2), Katalog der Strafzumessungstatsachen (Abs. 2), Doppelverwertungsverbot (Abs. 3). Anwendung in Hauptverhandlung, Urteilsbegruendung und Revision. Schnittstelle zu §§ 46a 47 49 56 StGB und § 267 Abs. 3 StPO. |
| `spezial-besonders-formular-portal-und-einreichung` | Besonders: Formular, Portal und Einreichungslogik im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Orientierung Triage Paragraph Stgb Besonders**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `orientierung-strafzumessung-triage`

**Fokus:** Einstieg und Triage im Plugin Strafzumessung. Ordnet das Mandat (Strafverteidiger, Staatsanwaltschaft, Beistand) nach Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe), erkennt Eilfristen, schlaegt passende Fachmodule aus diesem Plugin vor und liefert bei klarer Faktenlage sofort einen ersten Strafzumessungsentwurf mit Platzhaltern.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, hoechstens **eine** unverzichtbare Rueckfrage, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankuendigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klaeren: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, eine Rueckfrage falls noetig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausfuehrlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklaerungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausfuehrlich. Sonst nicht.

# Strafzumessung — Orientierung und Triage

## Worum geht es?

Strafzumessung ist die richterliche Bestimmung von Strafart und Strafhoehe innerhalb des gesetzlichen Strafrahmens. Grundlage ist die Schuld des Taeters (§ 46 Abs. 1 Satz 1 StGB). Dieser Allgemein-Skill ist der Eingang in das Plugin: er ordnet den Stand des Verfahrens, identifiziert Fristen und schlaegt den passenden Fachmodul vor.

## Wann brauchen Sie diese Skill?

- Mandant hat Strafbefehl erhalten, Strafzumessung soll angegriffen oder beschraenkter Einspruch erwogen werden.
- Anklageschrift liegt vor, Strafzumessungs-Verteidigung in der Hauptverhandlung wird vorbereitet.
- Verstaendigungs-Gespraech (§ 257c StPO) mit Gericht und Staatsanwaltschaft steht an, Strafrahmen wird sondiert.
- Urteil ist ergangen, Strafzumessungsruege wird vorbereitet (§ 267 Abs. 3 StPO).
- Mehrere Verurteilungen liegen vor, nachtraegliche Gesamtstrafenbildung (§ 55 StGB) oder Haerteausgleich pruefen.

## Rolle abklaeren (Pflicht)

| Rolle | Typischer Fokus |
|---|---|
| Strafverteidiger | Strafmilderung, Bewaehrung, TOA, Verstaendigung, Strafzumessungsruege |
| Staatsanwaltschaft | Antragsstrafe, Strafzumessungsrichtlinien, Schwere-Argumente |
| Mandant / Betroffener (mit Anwalt) | Verstaendnis der Strafzumessungslogik; Tagessatzpruefung |
| Nebenklaegervertreter | Strafzumessungs-Aspekte zugunsten des Opfers |

Wenn die Rolle unklar ist, **frage zuerst** — die Argumentationsrichtung haengt davon ab.

## Verfahrensstadium-Triage

| Stadium | Primaerer Skill |
|---|---|
| Strafbefehl liegt vor | `strafbefehl-strafzumessung-407-stpo`, ggf. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` |
| Einstellungsangebot § 153a StPO | `153a-stpo-einstellung-gegen-auflage` |
| Anklage liegt vor, Hauptverhandlung vorbereiten | `strafrahmen-und-strafzumessungsstufen`, dann `paragraph-46-stgb-grundsatz-strafzumessung` |
| Verstaendigung steht an | `verstaendigung-257c-stpo-strafzumessung` |
| TOA mit dem Opfer moeglich | `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` |
| Mehrere Taten in einem Verfahren | `gesamtstrafenbildung-53-54-stgb-erste-instanz` |
| Mehrere Verurteilungen, eine Anlasstat | `nachtraegliche-gesamtstrafenbildung-55-stgb`, ggf. `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` |
| Urteil liegt vor, Strafzumessungsruege | `267-iii-stpo-begruendungsanforderungen-strafurteil` |
| Mandant unter 21 Jahren | `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` |

## Schritt-fuer-Schritt-Anleitung

1. Rolle und Verfahrensstadium erfragen oder aus Material erkennen.
2. Eilfristen pruefen (Einspruchsfrist § 410 StPO, Revisionsbegruendung § 345 StPO, Bewaehrungsstellungnahme).
3. Strafrahmen-Frage stellen: Welche Norm, welcher Strafrahmen, gibt es Regelbeispiele oder minder schweren Fall?
4. Strafzumessungs-Tatsachen sammeln (§ 46 Abs. 2 StGB): Vorleben, Tat, Nachtatverhalten.
5. Passenden Fachmodul auswaehlen; bei klarer Faktenlage sofort ersten Entwurf mit Platzhaltern liefern.
6. Quellenpflicht beachten: § 46 StGB, einschlaegige Spezialnormen, BGH-Linie nur mit verifiziertem Aktenzeichen.

## Typische Fehler

- Strafzumessung wird ohne Sortierung des Strafrahmens diskutiert: erst Strafrahmen pruefen, dann konkretisieren.
- Verstaendigung wird abgeschlossen, bevor die Belehrungspflicht (§ 257c Abs. 4 und 5 StPO) sauber gepruefte ist.
- TOA wird als reine Schadenswiedergutmachung verstanden; nach BGH ist ein friedensstiftender kommunikativer Prozess noetig.
- Tagessatzhoehe wird ohne Einkommensnachweis akzeptiert; Gericht schaetzt sonst zu Lasten des Mandanten.
- Nachtraegliche Gesamtstrafe wird vergessen; Haerteausgleich nicht thematisiert.

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Schuld als Grundlage; tragender Norm-Einstieg.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik vor jeder konkreten Zumessung.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — bei Geldstrafe.
- `verstaendigung-257c-stpo-strafzumessung` — bei Deal-Verhandlung.
- `nachtraegliche-gesamtstrafenbildung-55-stgb` — bei Mehrfachverurteilten.
- Plugin `strafbefehl-verteidiger` — wenn Verfahren noch im Strafbefehlsstadium ist.
- Plugin `fachanwalt-strafrecht` — gesamtstrafrechtliche Verteidigungssicht.

## Quellen und Stand 05/2026

- StGB §§ 38 ff. (Strafarten, Strafrahmen), § 46 (Grundsatz), §§ 47, 49, 56, 56b–f, 53–55 StGB.
- StPO §§ 153, 153a, 257c, 267 Abs. 3, 407 ff., 460 StPO.
- JGG §§ 5 ff., 17, 18, 105.
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; vgl. `references/zitierweise.md`.

## 2. `paragraph-46-stgb-grundsatz-strafzumessung`

**Fokus:** Grundsatznorm der Strafzumessung § 46 StGB. Schuld als Grundlage (Abs. 1 Satz 1), praeventive Wirkungen auf das kuenftige Leben des Taeters (Abs. 1 Satz 2), Katalog der Strafzumessungstatsachen (Abs. 2), Doppelverwertungsverbot (Abs. 3). Anwendung in Hauptverhandlung, Urteilsbegruendung und Revision. Schnittstelle zu §§ 46a 47 49 56 StGB und § 267 Abs. 3 StPO.

# § 46 StGB — Grundsatz der Strafzumessung

## Worum geht es?

§ 46 StGB ist die zentrale Norm der Strafzumessung. Abs. 1 Satz 1 bestimmt die **Schuld** als Grundlage. Abs. 1 Satz 2 verlangt, die Wirkungen der Strafe auf das **kuenftige Leben** des Taeters zu beruecksichtigen. Abs. 2 fuehrt einen nicht abschliessenden Katalog von Strafzumessungstatsachen auf. Abs. 3 enthaelt das **Doppelverwertungsverbot**.

## Wann brauchen Sie diese Skill?

- Sie bereiten einen Schlussvortrag oder ein Plaedoyer vor und muessen die Strafzumessungslogik aufbauen.
- Sie schreiben eine Strafzumessungsruege im Revisionsverfahren und brauchen den Norm-Anker.
- Sie verfassen ein Urteil und muessen die Strafzumessungsgruende nach § 267 Abs. 3 StPO formulieren.
- Sie pruefen, ob das Tatgericht das Doppelverwertungsverbot verletzt hat (Tatbestandsmerkmale werden noch einmal strafschaerfend angefuehrt).

## Rechtliche Grundlagen

- **§ 46 Abs. 1 Satz 1 StGB** — "Die Schuld des Taeters ist Grundlage fuer die Zumessung der Strafe."
- **§ 46 Abs. 1 Satz 2 StGB** — Die Wirkungen, die von der Strafe fuer das kuenftige Leben des Taeters in der Gesellschaft zu erwarten sind, sind zu beruecksichtigen (Spezialpraevention).
- **§ 46 Abs. 2 StGB** — Bei der Zumessung waegt das Gericht die Umstaende, die fuer und gegen den Taeter sprechen, gegeneinander ab. Genannt sind insbesondere:
 - Beweggruende und Ziele des Taeters, **besonders auch rassistische, fremdenfeindliche, antisemitische, geschlechtsspezifische, gegen die sexuelle Orientierung gerichtete oder sonstige menschenverachtende** Beweggruende und Ziele;
 - Gesinnung, die aus der Tat spricht, und der bei der Tat aufgewendete Wille;
 - Mass der Pflichtwidrigkeit;
 - Art der Ausfuehrung und verschuldete Auswirkungen der Tat;
 - Vorleben des Taeters, seine persoenlichen und wirtschaftlichen Verhaeltnisse;
 - Verhalten nach der Tat, namentlich Bemuehen, den Schaden wiedergutzumachen, und das Bemuehen des Taeters, einen Ausgleich mit dem Verletzten zu erreichen.
- **§ 46 Abs. 3 StGB** — **Doppelverwertungsverbot**: Umstaende, die schon Merkmale des gesetzlichen Tatbestandes sind, duerfen nicht beruecksichtigt werden.

## Strafzumessungs-Grundsatz

- **Schuldrahmen**: Die Strafe darf den Schuldrahmen nicht ueberschreiten (Obergrenze) und nicht so weit zurueckbleiben, dass sie der Schuld nicht mehr gerecht wird (Untergrenze).
- **Praevention** kommt innerhalb des Schuldrahmens hinzu, ueberschreitet ihn aber nicht.
- Spielraumtheorie: Innerhalb des "Spielraums schuldangemessener Strafe" wird die Strafe nach praeventiven Erwaegungen bestimmt (so die st. Rspr. seit BGH GS BGHSt 7, 28; verifizieren in dejure.org).
- **Keine Praejudizienbindung** im deutschen Strafrecht (Ausnahme § 31 BVerfGG); jede Strafzumessung ist konkret zu begruenden.

## Schritt-fuer-Schritt-Anleitung

1. **Schuld bestimmen**: Welche Tatbestaende verwirklicht? Welche Schuldform (Vorsatz, Fahrlaessigkeit)? Schuldminderungs- oder -ausschlussgruende (§§ 17, 20, 21 StGB)?
2. **Strafrahmen bestimmen**: Grundtatbestand, Qualifikation, Privilegierung, Regelbeispiele, minder schwerer Fall, Strafmilderungs-/Schaerfungsgruende (§§ 49, 23 Abs. 2, 28 StGB).
3. **Strafzumessungstatsachen sammeln** (§ 46 Abs. 2 StGB):
 - Vorleben: Vorstrafen (BZRG, Tilgung), Erziehung, soziale Verhaeltnisse;
 - Taterscheinung: Beweggrund, Ausfuehrung, Folgen, Pflichtwidrigkeit;
 - Nachtatverhalten: Reue, Gestaendnis, TOA (§ 46a StGB), Schadenswiedergutmachung.
4. **Abwaegung**: Strafmildernde gegen strafschaerfende Faktoren; das Gewicht muss explizit werden.
5. **Doppelverwertungsverbot pruefen**: Wenn etwa § 224 Abs. 1 Nr. 2 StGB (gefaehrliches Werkzeug) verwirklicht ist, darf die Tatsache "Messer verwendet" nicht noch einmal strafschaerfend angefuehrt werden.
6. **Begruendung**: Im Urteil muss die Strafzumessung so dargelegt werden, dass das Revisionsgericht sie ueberpruefen kann (§ 267 Abs. 3 StPO).

## Strafmildernde Faktoren (Standardkatalog)

- Gestaendnis (besonders bei prozessoekonomischem Wert)
- Reue, Einsicht, Selbstanzeige
- Schadenswiedergutmachung, TOA (§ 46a StGB)
- Lange Verfahrensdauer (Art. 6 EMRK; rechtsstaatswidrige Verzoegerung kann als Kompensation Strafabschlag begruenden)
- Beruflicher und sozialer Status, intakte familiaere Bindungen
- Keine Vorstrafen oder lange straffreie Zeit
- Tatumstaende (Provokation des Opfers, Notlage)
- Auslaender-/Auslieferungs-Folgen, falls einschlaegig

## Strafschaerfende Faktoren (Standardkatalog)

- Vorstrafen, einschlaegige Vorbelastung
- Hoher Schaden, intensive Tatfolgen
- Brutale, demuetigende, ueberlange Ausfuehrung
- Menschenverachtende Motive (§ 46 Abs. 2 StGB ausdruecklich; Gesetz 2015 erweitert um geschlechtsspezifische und gegen sexuelle Orientierung gerichtete Motive)
- Vertrauensbruch (Amtstraeger, Pflegende, Eltern)
- Tatbeteiligung mehrerer (Bandenstruktur)
- Verhalten waehrend der Hauptverhandlung (Verleumdung der Geschaedigten)

## Typische Fehler

- **Doppelverwertung**: Tatbestandsmerkmal wird nochmal als Schaerfungsgrund herangezogen. Revisionsangriff: Verletzung § 46 Abs. 3 StGB.
- **Unzulaessige Schaerfung wegen Schweigen**: Schweigen des Angeklagten (§ 136 StPO, § 243 Abs. 5 StPO) darf nicht zum Nachteil verwertet werden (st. Rspr.). Wohl aber Lueg-Verhalten oder Verleumdung in der Verteidigung.
- **Vorstrafen ohne Bezug** wahllos zitiert: erforderlich ist konkrete Bezugnahme auf die Gefaehrlichkeit oder einschlaegige Naehe.
- **Praevention vor Schuld**: Wenn die Strafe ueber den Schuldrahmen hinaus aus Generalpraevention erhoeht wird, verletzt das § 46 Abs. 1 StGB.
- **Strafzumessung pauschal**: "unter Beruecksichtigung aller Umstaende" ohne Einzelabwaegung ist revisionsanfaellig (§ 267 Abs. 3 StPO).

## Querverweise

- `strafzumessungs-tatsachen-46-ii-stgb` — Detail-Katalog des Abs. 2.
- `strafrahmen-und-strafzumessungsstufen` — vor der konkreten Zumessung.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — wie Urteilsbegruendung aussehen muss.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — Sondernorm.
- `gestaendnis-und-strafmilderung` — typischer Milderungsgrund.

## Quellen und Stand 05/2026

- § 46 StGB in der seit 01.08.2015 geltenden Fassung (Erweiterung um geschlechtsspezifische, gegen sexuelle Orientierung gerichtete Beweggruende).
- BGH GS BGHSt 7, 28 (Spielraumtheorie) — Aktenzeichen vor Zitat in dejure.org/openjur.de verifizieren.
- Quellenregel: Kommentar-/Aufsatzfundstellen nur auf Nutzerquellenbasis oder lizenzierten Live-Zugriff; vgl. `references/zitierweise.md`.

## 3. `spezial-besonders-formular-portal-und-einreichung`

**Fokus:** Besonders: Formular, Portal und Einreichungslogik im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Besonders: Formular, Portal und Einreichungslogik

## Spezialwissen: Besonders: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Besonders: Formular, Portal und Einreichungslogik / besonders formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, TOA, JGG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Besonders** prüfen.
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

## Strafzumessungs-Formular / Portal / Einreichung Bausteine
- **Formal-Einreichungen im Strafverfahren:**
 - **Pladoyer-Notizen** schriftlich vorbereitet (Strafrahmen, § 46 StGB-Bilanz, Antrag).
 - **Antrag auf nachtraegliche Gesamtstrafe § 460 StPO** an Vollstreckungsbehoerde mit Auflistung aller Verurteilungen.
 - **Antrag auf Strafaussetzung Strafrest § 57 StGB / § 57a StGB** mit Sozialprognose-Tatsachen.
 - **Antrag auf Bewaehrungswiderruf-Abwehr § 56f StGB** mit Stellungnahme zu neuen Vorwuerfen.
 - **Antrag auf Bewaehrungserlass § 56g StGB** nach Bewaehrungszeit-Ende.
- **Sachverstaendigengutachten beantragen:**
 - **Schuldfaehigkeitsgutachten §§ 20, 21 StGB:** Antrag in Hauptverhandlung; Pflicht bei Anhaltspunkten Schuldminderung.
 - **Therapieprognose-Gutachten § 56 StGB:** fuer Sozialprognose.
 - **§ 109 SGG-Gutachten** ist Sozialgerichts-Spezialitaet, nicht im Strafverfahren - statt dessen § 73 StPO Sachverstaendiger.
- **Eingaben Vollstreckungsverfahren:**
 - **Antrag bei StA als Vollstreckungsbehoerde § 451 StPO:** Stundung, Ratenzahlung § 42 StGB, gemeinnuetzige Arbeit § 43 StGB.
 - **Strafaussetzungsverfahren §§ 57, 57a StGB** beim Strafvollstreckungsgericht (StVG-Kammer).
 - **Massregelvollzug-Antraege §§ 67d ff. StGB** beim StVG.
- **Gerichts-Portale:**
 - **beA / EGVP** fuer Anwaltskommunikation (im Strafrecht § 32a StPO freiwillig).
 - **Vollstreckungsstelle StA:** Schriftverkehr per Post / Fax / E-Mail.
 - **BZRG-Auszug** ueber Bundeszentralregister, online beantragbar.
- **Standardvorlage Strafmass-Antrag (Pladoyer-Schluss):**
 ```
 Antraege der Verteidigung:

 Hauptantrag: Freispruch.

 Hilfsantrag: Verurteilung wegen ... (§ ... StGB) zu einer Strafe von ...
 - ... Tagessaetzen Geldstrafe a ... EUR; bzw.
 - ... Monaten Freiheitsstrafe, deren Vollstreckung zur Bewaehrung ausgesetzt wird (§ 56 StGB), bei einer Bewaehrungszeit von ... Jahren.

 Bewaehrungsauflagen / -weisungen:
 - Zahlung von ... EUR an gemeinnuetzige Einrichtung (§ 56b II Nr. 2 StGB).
 - Wiedergutmachung des Schadens an Geschaedigte (§ 56b II Nr. 1 StGB).
 - Therapeutische Betreuung (§ 56c II Nr. 5 StGB).
 ```
- **Praxis-Tipp:** Antraege schriftlich formulieren; bei Hauptverhandlung kopieren fuer Gericht und Mandant; Belege Strafmilderung in Hauptverhandlung vorlegen.

## Qualitätsanker: Strafrahmen, Schuldprinzip und Gesamtstrafe

- **Verifizierte Rechtsprechungsanker:** BGH, Beschluss vom 14.05.2024 - 6 StR 502/23 zur Strafrahmenlogik/Sperrwirkung und gerechten Schuldstrafe; BGH, Beschluss vom 23.01.2024 - 3 StR 455/23 zum Doppelverwertungsverbot und Begründungsanforderungen; BGH, Beschluss vom 24.04.2024 - 5 StR 123/24 sowie BGH, Beschluss vom 03.06.2025 - 2 StR 333/24 zur nachträglichen Gesamtstrafenbildung, Zäsurwirkung und Härteausgleich.
- **Prüfreihenfolge:** Nie sofort ein „gefühltes Strafmaß“ bilden. Erst Tatbestand und anwendbares Recht, dann Strafrahmen, minder/ besonders schwerer Fall, vertypte Milderung, § 49 StGB, Doppelverwertungsverbot, § 46 StGB, Nebenfolgen, Bewährung, Gesamtstrafe.
- **§ 55-StGB-Disziplin:** Bei Vorverurteilungen immer Tatzeiten, Entscheidungsdaten, Rechtskraft, Vollstreckungsstand, erledigte/nicht erledigte Strafen und Zäsurwirkung als Tabelle verlangen. Unklare Gesamtstrafenlagen nicht glattbügeln, sondern als Risiko mit Alternativen ausgeben.
- **Output-Pflicht:** Strafzumessungsmemo mit Strafrahmenbaum, Zumessungstatsachen pro/contra, Revisionsrisiken und nächstem taktischem Schritt; bei Aktenbezug zusätzlich BZRG-/Urteils-/Vollstreckungsdaten-Lückenliste.
