---
name: iap-rangordnung-ifap-aktenanlage-beleg
description: "Iap Rangordnung Checkliste, Ifap Aktenanlage Batchregister, Ifap Beleg Und Urkundencheck: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Iap Rangordnung Checkliste, Ifap Aktenanlage Batchregister, Ifap Beleg Und Urkundencheck

## Arbeitsbereich

Dieser Skill bündelt **Iap Rangordnung Checkliste, Ifap Aktenanlage Batchregister, Ifap Beleg Und Urkundencheck** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `iap-rangordnung-checkliste` | Checkliste Rangordnung der Insolvenzforderungen § 38 / § 39 InsO: einfach, nachrangig, Massekosten, Masseverbindlichkeiten. Pruefraster fuer Tabellenfuehrer. |
| `ifap-aktenanlage-batchregister` | Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes Register aufbauen. § 175 InsO Tabelle, § 176 InsO Prüfungstermin. Prüfraster Gläubigerstamm, Prüfnummern, Status je Forderung, Wiedervorlagen, Audit-Trail, Fristen. Output Batchregister mit Eingangsprotokoll, Statusuebersicht und Fristenliste. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Kommandocenter. |
| `ifap-beleg-und-urkundencheck` | Belege und Urkunden bei Insolvenzforderungsanmeldung prüfen: Anwendungsfall Gläubiger legt Rechnungen Verträge Titel Lieferscheine Kontoauszüge vor; Insolvenzverwalter oder Prüfungsstelle muss Belegkette aufbauen und Beweiswert einordnen. § 174 InsO Anmeldepflicht Urkunden, § 180 InsO streitige Forderung. Prüfraster vollständige Belegkette prüfen, Originale vs. Kopien, Lesbarkeit, Titel-Nachweis, Zuordnung zur Forderungssumme. Output Belegcheckliste mit Beweiswert-Ampel und Nachforderungsbedarf. Abgrenzung zu Formalprüfung-174 und zu Grund-Betrag-Zinsen. |

## Arbeitsweg

Für **Iap Rangordnung Checkliste, Ifap Aktenanlage Batchregister, Ifap Beleg Und Urkundencheck** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insolvenzforderungsanmeldungspruefung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `iap-rangordnung-checkliste`

**Fokus:** Checkliste Rangordnung der Insolvenzforderungen § 38 / § 39 InsO: einfach, nachrangig, Massekosten, Masseverbindlichkeiten. Pruefraster fuer Tabellenfuehrer.

# IAP: Rangordnung-Checkliste

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IAP: Rangordnung-Checkliste` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: IAP: Rangordnung-Checkliste
- **Spezialgegenstand:** IAP: Rangordnung-Checkliste / iap rangordnung checkliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, IAP.
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
Dieser Skill gehoert zum Plugin `insolvenzforderungsanmeldungspruefung`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## 2. `ifap-aktenanlage-batchregister`

**Fokus:** Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach § 174 InsO und muss strukturiertes Register aufbauen. § 175 InsO Tabelle, § 176 InsO Prüfungstermin. Prüfraster Gläubigerstamm, Prüfnummern, Status je Forderung, Wiedervorlagen, Audit-Trail, Fristen. Output Batchregister mit Eingangsprotokoll, Statusuebersicht und Fristenliste. Abgrenzung zu Intake-Kanalcheck für Eingangserfassung und zu Kommandocenter.

# Aktenanlage und Batchregister

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aktenanlage und Batchregister` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Baut die Arbeitsakte für große Forderungsstapel und hält Status, Zuständigkeit und Nachlauf zusammen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- mehr als fünf Forderungen
- Tabellenimport soll vorbereitet werden
- Prüfteam braucht Statusübersicht

## Workflow

1. Einheitliche Prüfnummern bilden und jeder Anmeldung genau eine Arbeitsakte geben.
2. Gläubigerstamm normalisieren: Name, Rechtsform, Anschrift, Vertreter, Konto, E-Mail, Registerdaten.
3. Statusspalten anlegen: neu, formal geprüft, Nachforderung, materiell geprüft, festgestellt, bestritten, erledigt.
4. Wiedervorlagen für Belege, Prüfungstermin, Feststellungsklage und § 189-Nachweis setzen.
5. Audit-Trail mit Bearbeiter, Datum, Quelle und Entscheidung anlegen.

## Ausgabe

- Batchregister als CSV-Struktur
- Statusdashboard
- Wiedervorlagenliste
- Bearbeitungsprotokoll

## Qualitätsgates

- Eine Forderung kann mehrere Teilbeträge haben, aber nur eine eindeutige Prüfnummernfamilie.
- Gläubigerstamm und Forderungspositionen bleiben getrennt.
- Bearbeitungsstände sind rückverfolgbar.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aktenanlage

§ 174 InsO (Anmeldeform) → § 175 InsO (Eintragung Tabelle) → § 176 InsO (Pruefungstermin) → § 66 InsO (Rechnungslegung und Dokumentation) → § 60 InsO (Verwalterhaftung) → § 61 InsO (persoenliche Haftung IV)

## Triage — Batchregister-Kaltstart

1. **Wieviele Anmeldungen erwartet?** Mittel- bis Grossverfahren (>20 Glaeubiger) → Batch-System zwingend.
2. **Digitale Einreichung?** § 174 Abs. 4 InsO Erleichterungen beachten; E-Mail vs. beA.
3. **Fristen?** Pruefungstermin § 176 InsO: Ladungsfrist 7 Tage; Tabelle muss vorher vollstaendig sein.
4. **Dubletten-Risiko?** Gleicher Glaeubiger mehrfach (z.B. Abtretung) → Deduplication-Logik einbauen.

## 3. `ifap-beleg-und-urkundencheck`

**Fokus:** Belege und Urkunden bei Insolvenzforderungsanmeldung prüfen: Anwendungsfall Gläubiger legt Rechnungen Verträge Titel Lieferscheine Kontoauszüge vor; Insolvenzverwalter oder Prüfungsstelle muss Belegkette aufbauen und Beweiswert einordnen. § 174 InsO Anmeldepflicht Urkunden, § 180 InsO streitige Forderung. Prüfraster vollständige Belegkette prüfen, Originale vs. Kopien, Lesbarkeit, Titel-Nachweis, Zuordnung zur Forderungssumme. Output Belegcheckliste mit Beweiswert-Ampel und Nachforderungsbedarf. Abgrenzung zu Formalprüfung-174 und zu Grund-Betrag-Zinsen.

# Beleg- und Urkundencheck

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beleg- und Urkundencheck` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Bildet die Belegkette der Anmeldung und trennt belastbare Nachweise von bloßem Vortrag.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anlagenstapel ist unübersichtlich
- Rechnungen fehlen
- Titel wird behauptet
- Buchhaltung widerspricht

## Workflow

1. Alle Belege inventarisieren: Typ, Datum, Nummer, Parteien, Betrag, Zeitraum, Datei, Lesbarkeit.
2. Belege der konkreten Forderungsposition zuordnen und Fremdbelege aussortieren.
3. Titelstatus prüfen: vollstreckbarer Titel, Endurteil, Mahnbescheid, Vergleich, Kostenfestsetzung, bloße Rechnung.
4. Schuldnerbuchhaltung und OPOS abgleichen: gebucht, bestritten, bezahlt, storniert, Gegenforderung, Skonto.
5. Lücken markieren und konkrete Nachforderung formulieren.

## Ausgabe

- Belegkettenmatrix
- Titelvermerk
- OPOS-Abgleich
- fehlende Urkunden

## Qualitätsgates

- Ein Titel ersetzt nicht automatisch die Rangprüfung.
- Ein OPOS-Eintrag ersetzt nicht automatisch den Rechtsgrund.
- Unlesbare oder fremdsprachige Belege erhalten eigenen Prüfstatus.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
