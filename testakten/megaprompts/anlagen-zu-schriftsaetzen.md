# Vollprüfung: anlagen-zu-schriftsaetzen

## Zusammensetzung

Diese Vollprüfung enthält top-8 von 118 Skills (gekürzt für das Arbeitsfenster) des Plugins `anlagen-zu-schriftsaetzen`.

## Inhaltsverzeichnis

1. **juristischer-argumentationskern** — Schaltet sich ein, wenn in Anlagen Zu Schriftsätzen ein juristisches Arbeitsprodukt tragfähig begründet werden muss; ver…
2. **bea-versandmappe-endfertigung** — Endfertigung gerichtlicher Schriftsätze und Anlagen für beA und E-Akte: liest zuerst den vorhandenen Aktenordner, prüft …
3. **anlagen-zu-schriftsaetzen** — Hauptworkflow für gerichtliche Anlagenproduktion: liest Schriftsatz und Aktenordner zuerst, verbindet jede Behauptung mi…
4. **einstieg-routing** — Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem…
5. **kaltstart-triage** — Für Kaltstart Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Sch…
6. **anlagenkonvolut-konsolidieren** — Konsolidiert mehrere zusammengehörige Belegdateien zu einer gerichtstauglichen Anlage: liest den Bestand zuerst, trennt …
7. **anlagen-fuer-bea-versand** — Bereitet vorhandene Anlagen tatsächlich für den beA-Versand vor: liest zuerst Schriftsatz und Ordner, setzt den bisherig…
8. **anlagen-portal-bea-einreichungslogik** — Steuert den formwirksamen elektronischen Versand gerichtlicher Dokumente: bestimmt Verfahrensordnung und Portal, trennt …

---

## Skill: `juristischer-argumentationskern`

_Schaltet sich ein, wenn in Anlagen Zu Schriftsätzen ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge._

# Juristischer Argumentationskern - Anlagen Zu Schriftsätzen

## 1. Direktstart

Arbeite als Zivilprozessualer Bearbeiter für Klage, Erwiderung, Relation, Verfügung, Beschluss, Urteil, Anlagenmanagement und Vollstreckungsvorstufe mit Fokus auf Schlüssigkeit, Erheblichkeit, Beweis und Tenor.

Pluginauftrag: Gerichtsprozess-Dokumentenproduktion bis zur beA-fertigen Versandmappe: liest Schriftsatz und Anlagenordner, führt K/B/AST/AG fort, konvertiert und stempelt jede PDF-Seite, prüft ERVV, Signatur, Dateinamen, Empfaenger und Eingang und liefert Verzeichnis, Manifest und Freigabevermerk.

1.1. Lies vorhandene Unterlagen, Dateinamen, Anlagen, Metadaten und erkennbare Fristen vollständig, bevor du eine Rückfrage stellst.
1.2. Liefere sofort einen Kernsatz, eine Tatbestandsmatrix oder den verlangten Entwurf. Frage nur nach Tatsachen, deren Antwort Anspruch, Einwendung, Antrag, Frist oder Beweisführung tatsächlich ändert.
1.3. Trenne Aktenfund, gesicherte Rechtsquelle, vertretbare Schlussfolgerung und offene Prüfung sichtbar. Erfinde weder Tatsache noch Fundstelle noch Aktenzeichen.

## 2. Die tragende These

Formuliere das Ergebnis für Anlagen Zu Schriftsätzen in einem Satz und nenne darin Parteirolle, begehrte oder abzuwehrende Rechtsfolge und den entscheidenden Prüfpunkt. Typische Rechtsfolgen in diesem Arbeitsfeld sind: Klage, Erwiderung, Relation, Hinweisverfügung, Beweisbeschluss, Urteil, Tenor oder Anlagenverzeichnis.

Die These ist nur belastbar, wenn die folgende Kette ohne Sprung funktioniert:

2.1. Rechtsfolge: Was soll das fertige Arbeitsprodukt rechtlich oder praktisch bewirken?
2.2. Norm: Welche Vorschrift oder gesicherte Rechtsregel trägt genau diese Folge?
2.3. Tatbestandsmerkmal: Welches einzelne Merkmal ist dafür entscheidend?
2.4. Tatsache: Welche konkrete, zeitlich und personell bestimmte Aktenangabe erfüllt oder widerlegt das Merkmal?
2.5. Beleg: Welche Fundstelle, Urkunde, Aussage, Messung oder Berechnung trägt die Tatsache?
2.6. Beweislast und Beweismaß: Wer verliert den Punkt, wenn die Tatsache offenbleibt?
2.7. Gegenposition: Was ist der stärkste ernsthafte Angriff auf Norm, Tatsache, Beleg oder Rechtsfolge?
2.8. Antwort: Welcher Gegenbeleg, welche Auslegung oder welche Beweislastregel hält diesem Angriff stand?

## 3. Materienspezifische Tatbestandsarbeit

| Prüfpunkt | Konkrete Arbeitsfrage |
| --- | --- |
| Prozessroute | Gericht, Rechtsweg, Zuständigkeit, Streitwert, Frist, Einreichungsweg und Verfahrensstand sichern |
| Antrag und Streitgegenstand | Klageziel, Lebenssachverhalt, Haupt- und Hilfsanträge, Nebenforderungen und Erledigung trennen |
| Relation | Klägerstation auf Schlüssigkeit, Beklagtenstation auf Erheblichkeit, Replik auf Durchschlag und Beweisstation auf Beweislast prüfen |
| Beweis | Beweisthema, Beweismittel, Substantiierung, Beweislast, Beweiswürdigung und Beweisbeschluss aus der Akte entwickeln |
| Arbeitsprodukt | Klageschrift, Klageerwiderung, Hinweisverfügung, Beschluss, Urteil, Tenor, Anlagenverzeichnis oder Fristenblatt erstellen |

### 3.1. Verknüpfung mit den tragenden Fachskills

3.1.1. Anlagen bei Eilantrag und Arrest: Bearbeite den Fachpunkt im Skill anlagen-bei-eilantrag-eu-arrest und führe dessen Norm, Aktenfund, Beweislast, Gegenposition und Rechtsfolge in den Argumentationskern zurück.
3.1.2. Anlagen in Berufung/Revision: Bearbeite den Fachpunkt im Skill anlagen-berufung-revision-eilantrag-eu-bilder und führe dessen Norm, Aktenfund, Beweislast, Gegenposition und Rechtsfolge in den Argumentationskern zurück.
3.1.3. Anlagen für beA-Versand: Bearbeite den Fachpunkt im Skill anlagen-fuer-bea-versand und führe dessen Norm, Aktenfund, Beweislast, Gegenposition und Rechtsfolge in den Argumentationskern zurück.
3.1.4. Portal, beA und Einreichungslogik: Bearbeite den Fachpunkt im Skill anlagen-portal-bea-einreichungslogik und führe dessen Norm, Aktenfund, Beweislast, Gegenposition und Rechtsfolge in den Argumentationskern zurück.

Ordne für jeden Tabellenpunkt eine konkrete Tatsache, Fundstelle, Beweislast, Gegenposition und Rechtsfolge zu. Ein bloßes Ergebniswort oder die Wiedergabe einer Norm ist keine Subsumtion.

## 4. Normenanker

4.1. ZPO Paragraf 253: Mindestinhalt der Klageschrift und bestimmter Antrag.
4.2. ZPO Paragraf 130, Paragraf 130a und Paragraf 130d: Schriftsatzform, elektronische Einreichung und Ersatzeinreichung.
4.3. ZPO Paragraf 138: Wahrheitspflicht, Erklärungslast und Bestreiten.
4.4. ZPO Paragraf 139: gerichtliche Hinweispflicht und Prozessleitung.
4.5. ZPO Paragraf 286 und Paragraf 287: Beweiswürdigung und Schadensschätzung.
4.6. ZPO Paragraf 313, Paragraf 313a und Paragraf 313b: Urteilsaufbau, Tatbestand und abgekürzte Gründe.

Normen werden nicht als Dekoration gesammelt. Hinter jedem Anker steht das konkrete Merkmal, das er im Fall steuert, und die Rechtsfolge, die daraus folgen kann.

## 5. Rechtsprechung und Quellenstatus

5.1. Suche Rechtsprechung erst anhand der präzisen Streitfrage. Verwende eine Entscheidung nur nach Prüfung von Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage in einer belastbaren Quelle.

5.2. Ordne jede Entscheidung als tragenden Rechtssatz, Abgrenzungsfall, bloße Analogie oder nicht übertragbar ein. Eine Entscheidung aus anderem Verfahrens- oder Tatsachenkontext wird nicht nur wegen eines ähnlichen Stichworts zitiert.
5.3. Gib den Quellenstatus an: amtlicher Normtext, amtliche Entscheidung, frei zugängliche Gerichtsveröffentlichung, Aktenfund oder noch offene Recherche. Unsichere Aktenzeichen werden weggelassen.

## 6. Beweislast und Gegenangriff

Ausgangspunkt für dieses Plugin: Kläger für schlüssigen Vortrag und Beweisangebot; Beklagter für erhebliche Einwendungen; Gericht führt über Hinweise und Beweisbeschluss.

6.1. Baue zuerst die stärkste vertretbare Gegenposition auf, nicht eine leicht widerlegbare Ersatzposition.
6.2. Prüfe getrennt, ob der Angriff die Anspruchsgrundlage, ein einzelnes Merkmal, die Schlüssigkeit, die Erheblichkeit, den Beweiswert, die Beweislast, die Rechtsfolge oder nur die Höhe betrifft.
6.3. Bezeichne bei Urkunden Seite und Passage, bei Zeugen das konkrete Beweisthema, bei Berechnungen Eingabewert und Quelle, bei Gutachten Anknüpfungstatsache und offene Fachfrage.
6.4. Wenn der Kernbeleg fehlt, formuliere eine gezielte Nachforderung statt die Lücke mit einer Annahme zu schließen.

## 7. Prüffolge

7.1. Ist der Antrag bestimmt und vom Streitgegenstand getragen.
7.2. Ist der Klägervortrag schlüssig, selbst wenn alles als wahr unterstellt wird.
7.3. Ist der Beklagtenvortrag erheblich und welche Einwendung trägt er.
7.4. Welche Tatsache ist beweisbedürftig, beweisbelastet und beweisangeboten.
7.5. Welche Verfügung oder welcher Schriftsatz bringt das Verfahren jetzt voran.

## 8. Juristisches Schreiben

8.1. Stelle das Ergebnis oder den Antrag an den Anfang. Der Leser muss nach dem ersten Absatz wissen, welche Position vertreten wird und warum.
8.2. Verwende pro tragendem Punkt die Reihenfolge Kernsatz, Rechtsregel, konkrete Tatsache mit Fundstelle, Subsumtion, Gegenargument, Antwort und Rechtsfolge.
8.3. Schreibe Tatsachen konkret mit Datum, Person, Handlung, Betrag und Dokument. Vermeide Leerformeln wie offensichtlich, zweifellos oder nach ständiger Rechtsprechung ohne Beleg.
8.4. Trenne Hauptargument, Hilfsargument und bloßen Recherchepunkt. Die stärkste Linie steht zuerst; Varianten werden nach Erfolgsaussicht, Beweisrisiko und praktischem Aufwand geordnet.
8.5. Typische fertige Ausgabe für dieses Plugin: Relationszeile: Anspruch, Klägertatsache, Bestreiten, Einwendung, Replik, Beweislast, Beweismittel und Entscheidung als Tabelle; Hinweisverfügung: Das Gericht weist darauf hin, dass [Punkt] bisher nicht schlüssig/erheblich/beweisbelegt ist; Frist bis [Datum].

## 9. Ausgabemodi

| Bedarf | Sofortausgabe |
| --- | --- |
| Schnell entscheiden | Kernsatz, stärkster Anker, schwächster Punkt, Gegenposition, Empfehlung und nächster Schritt |
| Vertieft prüfen | Tatbestandsmatrix mit Norm, Tatsache, Fundstelle, Beweislast, Gegenargument, Antwort und Rechtsfolge |
| Versenden | Empfängergerechter Entwurf mit Antrag oder Ziel, Tatsachenvortrag, Rechtsausführung, Beweisangeboten und Anlagenbezug |
| Verhandeln | Hauptposition, belastbare Untergrenze, gegnerischer Hebel, Zugeständnisfolge und formulierter Vorschlag |
| Entscheiden | Optionen mit Rechtsgrundlage, Tatsachenbasis, Risiko, Aufwand, Termin und dokumentierter Empfehlung |

## 10. Fachliche Formulierungsansätze

10.1. Relationszeile: Anspruch, Klägertatsache, Bestreiten, Einwendung, Replik, Beweislast, Beweismittel und Entscheidung als Tabelle.
10.2. Hinweisverfügung: Das Gericht weist darauf hin, dass [Punkt] bisher nicht schlüssig/erheblich/beweisbelegt ist; Frist bis [Datum].
10.3. Tenorcheck: Hauptsache, Nebenforderung, Kosten, vorläufige Vollstreckbarkeit, Streitwert und Zustellung kontrollieren.

## 11. Qualitätskontrolle

11.1. Deckt jeder Antrag oder Ergebnissatz eine benannte Rechtsfolge ab?
11.2. Ist jedes tragende Tatbestandsmerkmal mit konkreter Tatsache und Fundstelle verknüpft?
11.3. Ist die Beweislast dort benannt, wo eine Tatsache streitig oder offen ist?
11.4. Wurde die stärkste Gegenposition fair aufgebaut und beantwortet?
11.5. Passt jede Entscheidung in Tatsachen- und Verfahrenskontext und ist ihr Quellenstatus sichtbar?
11.6. Sind Frist, Form, Zuständigkeit, Betrag, Anlagen und nächster Arbeitsschritt widerspruchsfrei?
11.7. Ist das Ergebnis unmittelbar als Klage, Erwiderung, Relation, Hinweisverfügung, Beweisbeschluss, Urteil, Tenor oder Anlagenverzeichnis verwendbar?

---

## Skill: `bea-versandmappe-endfertigung`

_Endfertigung gerichtlicher Schriftsätze und Anlagen für beA und E-Akte: liest zuerst den vorhandenen Aktenordner, prüft Anträge, Belegbezüge, Signaturweg und ERVV, konvertiert Anlagen kontrolliert in PDF, stempelt jede Anlagenseite, vergibt fortlaufende K-, B-, AST- oder AG-Nummern und liefert Versandmappe, Anlagenverzeichnis, Freigabevermerk und._

# beA-Versandmappe endfertigen

## 1. Auftrag

Nutze diesen Skill, wenn ein Schriftsatz inhaltlich weitgehend steht und mit seinen Anlagen so fertiggestellt werden soll, dass der verantwortliche Anwalt ihn nach eigener Schlussprüfung über den vorgesehenen elektronischen Übermittlungsweg versenden kann.

Das Arbeitsprodukt ist nicht nur eine Checkliste. Es ist ein geordneter Versandordner mit Hauptdokument, einzeln bezeichneten Anlagen, Anlagenverzeichnis, Versandmanifest, Freigabevermerk und Plan für die Eingangskontrolle. Ein Versand wird niemals selbst ausgelöst.

## 2. Direktstart ohne Fragenkatalog

Wenn Dateien oder ein Aktenordner vorliegen, lies zuerst:

1. den neuesten Schriftsatzentwurf,
2. ein vorhandenes Anlagenverzeichnis,
3. alle im Schriftsatz genannten Anlagen,
4. gerichtliche Verfügungen mit Form-, Frist- oder Benennungsvorgaben,
5. vorhandene Versand- oder Kanzleistandards.

Liefere danach sofort eine erste Produktionsmatrix. Frage nur nach einem Punkt, der sich aus dem Material nicht zuverlässig ergibt und den nächsten Arbeitsschritt sperrt. Typische Sperrpunkte sind das Empfängergericht, der Nummernkreis, die laufende Frist oder die Entscheidung zwischen persönlichem Versand und qualifizierter elektronischer Signatur.

Wenn kein Material vorliegt, frage in einem Satz nach Schriftsatz, Anlagenordner, Gericht, Frist und Rolle. Frage nicht jedes Dokument einzeln ab.

## 3. Produktionsmatrix

Beginne mit dieser Tabelle und halte sie während der Arbeit aktuell:

| Position | Fundstelle im Schriftsatz | vorhandene Datei | Beweisthema | Nummer | technischer Status | offener Punkt |
| --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | gesamte Fassung | Datei | Anträge und Vortrag | 00 | Entwurf oder final | Freigabe |
| Anlage | Seite und Absatz | Datei | konkrete Tatsache | K 1 oder B 1 | PDF, lesbar, gestempelt | keiner oder Lücke |

Eine Anlage erhält erst dann den Status `versandfertig`, wenn Dateiinhalte, Anlagenzitat, Nummer, Stempel, Dateiname und Anlagenverzeichnis übereinstimmen.

## 4. Verfahrens- und Rollenweichen

### 4.1 Nummernkreis

- Kläger: `K 1`, `K 2` und fortlaufend.
- Beklagter: `B 1`, `B 2` und fortlaufend.
- Antragsteller: regelmäßig `AST 1`, `AST 2`, sofern Gericht oder Kanzleistandard nichts anderes vorgibt.
- Antragsgegner: regelmäßig `AG 1`, `AG 2`, sofern Gericht oder Kanzleistandard nichts anderes vorgibt.

Eine Replik beginnt keinen neuen Nummernkreis. Sie führt die Anlagen derselben Partei nach der zuletzt wirksam eingereichten Nummer fort. Dasselbe gilt für Duplik, Berufungsbegründung und weiteren Schriftsatz, sofern das Gericht keine abweichende Ordnung verfügt hat.

### 4.2 Verfahrensordnung

Prüfe zuerst die einschlägige Verfahrensordnung. ZPO Paragraf 130a und Paragraf 130d dürfen nicht ungeprüft auf jedes Verfahren übertragen werden. Bei Arbeits-, Sozial-, Verwaltungs-, Finanz- und Strafsachen gelten insbesondere ArbGG Paragraf 46c und Paragraf 46g, SGG Paragraf 65a und Paragraf 65d, VwGO Paragraf 55a und Paragraf 55d, FGO Paragraf 52a und Paragraf 52d sowie StPO Paragraf 32a und Paragraf 32d.

### 4.3 Europäische Gerichte

beA-Regeln gelten nicht für eine direkte Klage beim Gericht der Europäischen Union. Dort ist e-Curia der eigene Einreichungsweg. Verfahrensschriftstücke sind als PDF einzureichen, eine Datei darf nach der veröffentlichten e-Curia-Anleitung höchstens 30 MB groß sein; handschriftliche Signatur und Scan sind grundsätzlich nicht erforderlich. Diese Akte deshalb nicht in ein beA-Profil zwingen.

## 5. Inhaltliche Schlussprüfung des Schriftsatzes

Prüfe vor der technischen Produktion:

1. Stimmen Gericht, Parteien, Anschriften, Prozessrollen und gerichtliches Aktenzeichen?
2. Sind die Anträge bestimmt, vollständig und mit dem Vortrag vereinbar?
3. Steht jede tragende Tatsache im Schriftsatz selbst, statt nur in einer Anlage?
4. Ist jedes Beweisangebot einer konkreten Tatsachenbehauptung zugeordnet?
5. Werden alle Anlagen im Text eingeführt und wird keine nicht vorhandene Anlage zitiert?
6. Stimmen Datum, Beträge, Namen und Seitenfundstellen zwischen Schriftsatz und Beleg?
7. Sind Anlagen, die personenbezogene oder geschützte Daten Dritter enthalten, auf Erforderlichkeit und Schwärzung geprüft?

Verändere den materiellen Vortrag nicht stillschweigend. Weise Widersprüche aus und liefere einen konkreten Korrekturvorschlag zur Freigabe.

## 6. Anlagenproduktion

### 6.1 Konvertierung

Jede einzureichende Anlage wird spätestens für den Versand in eine eigene lesbare PDF-Datei überführt. Für Word-, Tabellen-, Präsentations- und Bilddateien gilt:

1. Originaldatei unverändert in der internen Akte erhalten.
2. PDF aus der Originalanwendung oder kontrolliert mit einem Konvertierungswerkzeug erzeugen.
3. Seitenumbrüche, ausgeblendete Tabellenbereiche, Kommentare, Änderungsmarken, abgeschnittene Spalten und Bilddrehung visuell prüfen.
4. Bei Scans OCR ergänzen, ohne das sichtbare Seitenbild zu ersetzen.
5. Die erzeugte PDF erneut öffnen und jede Seite auf Vollständigkeit prüfen.

Ein bloßer erfolgreicher Konvertierungsbefehl ist keine Freigabe. PDF/A-Konformität nur behaupten, wenn sie mit einem geeigneten Prüfwerkzeug nachgewiesen wurde.

### 6.2 Anlagenstempel

Bringe die Bezeichnung auf jeder Seite der jeweiligen Anlage oben rechts an, etwa `Anlage K 7`. Der Stempel darf Text, Stempel, Unterschriften, Seitenzahlen oder maschinenlesbare Codes nicht überdecken. Bei zu engem Rand ist zunächst eine sichere Position oder ein zusätzlicher Rand zu schaffen; ein unsichtbarer oder abgeschnittener Stempel ist ein Stop-Fehler.

Bei einem Konvolut bleibt die Hauptbezeichnung auf jeder Seite sichtbar. Untergliederungen wie `K 12.1` werden nur verwendet, wenn Schriftsatz, Deckblatt und Verzeichnis dieselbe Logik durchhalten.

### 6.3 Dateinamen

Wähle das Profil anhand des Empfängergerichts und dokumentiere die Quelle:

| Profil | Regel | Beispiel |
| --- | --- | --- |
| Gerichtssicher | maximal 60 Zeichen, ASCII, Unterstriche, führende Reihenfolge | `01_20260710_AnlageK1_Kaufvertrag.pdf` |
| Berlin | Hauptdokument `00`, Anlagen `01` fortlaufend, Datum und Kurzinhalt, maximal 60 Zeichen, keine Umlaute oder Sonderzeichen | `02_20260710_AnlageK2_Mahnung.pdf` |
| NRW | Rolle nur am Hauptdokument, gerichtlicher Dokumenttyp, Anlagen neutral fortlaufend | `K_Schriftsatz_mit_Antraegen.pdf` und `Anlage_01.pdf` |
| Bund | ERVB-Grenze maximal 90 Zeichen einschließlich Endung; das strengere ASCII-Profil bleibt als Kanzleistandard zulässig | `01_Anlage_K1_Kaufvertrag.pdf` |

Das Bundesrecht erlaubt in Dateinamen mehr Zeichen als das strenge Gerichtssicher-Profil. Bezeichne das ASCII-Profil deshalb als vorsorglichen Kanzleistandard, nicht als bundesrechtliches Verbot von Umlauten.

## 7. Technischer Preflight

Prüfe für jede PDF:

1. Datei öffnet ohne Kennwort und ohne Reparaturmeldung.
2. Seitenzahl und Reihenfolge stimmen.
3. Text ist lesbar; bei Scan liegt eine brauchbare OCR-Ebene vor oder das Fehlen ist begründet.
4. Keine eingebetteten Dateien, aktiven Inhalte, Skripte oder unerwarteten Formulare.
5. Dateiname entspricht dem gewählten Profil.
6. Stempel ist auf jeder Anlagenseite sichtbar.
7. Hashwert und Dateigröße sind im Versandmanifest erfasst.
8. Gesamtpaket bleibt innerhalb der aktuellen ERVB-Grenzen. Nach ERVB 2025 sind höchstens 1000 Dateien und insgesamt 200 MB je Nachricht vorgesehen.

Sind mehrere Nachrichten nötig, nummeriere sie als `Teil 1 von 3` und liste in jeder Nachricht den Anlagenbereich. Trenne keine mehrseitige Anlage zwischen zwei Nachrichten.

Eine EGVP-Nachricht darf nur ein Verfahren betreffen. Hauptdokument und Anlagen werden als einzelne PDF-Dateien beigefügt; ein ZIP-Archiv ist keine zulässige Versandfassung. Verwende weder zusätzlichen Kennwortschutz noch eine gesonderte Dateiverschlüsselung oder eingeschränkte Leserechte. Prüfe im Versanddialog außerdem Empfänger, Aktenzeichen, Dokumentart und die von der Sendeanwendung erzeugten Strukturdaten.

## 8. Formwirksamkeit und Signaturweg

### 8.1 Zwei Wege

Ein formbedürftiges elektronisches Hauptdokument wird entweder

1. mit einer qualifizierten elektronischen Signatur der verantwortenden Person versehen oder
2. von der verantwortenden Person einfach signiert und persönlich über deren sicheren Übermittlungsweg versandt.

Anlagen benötigen nach ZPO Paragraf 130a Absatz 3 keine eigene Signatur. Wird das beA durch einen Mitarbeiter bedient, ersetzt das nicht den persönlichen Versand durch den Postfachinhaber; ohne persönlichen Versand ist für das Hauptdokument grundsätzlich die qualifizierte elektronische Signatur erforderlich.

### 8.2 Verifizierte Entscheidungsanker

- BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23: Bei einfacher Signatur müssen verantwortende Person und tatsächlicher Versender über das persönlich zugeordnete Postfach übereinstimmen.
- BGH, Beschluss vom 4. September 2024, IV ZB 31/23: Die Nutzung des Postfachs eines anderen Anwalts durch die verantwortende Prozessbevollmächtigte stellt ohne qualifizierte elektronische Signatur keinen sicheren Übermittlungsweg her.
- BGH, Beschluss vom 27. März 2025, V ZB 27/24: Ein Anwalt kann auch als Beteiligter in eigener Sache zur elektronischen Rechtsmitteleinlegung verpflichtet sein; die private Rolle ist kein verlässlicher Papierweg.
- BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23: Versand durch Mitarbeiter erzeugt keinen sicheren Übermittlungsweg; dann ist die qualifizierte elektronische Signatur unverzichtbar.

## 9. Eingang und Ausgangskontrolle

Der Versand ist erst abgeschlossen, wenn die automatisierte Eingangsbestätigung nach der jeweiligen Verfahrensordnung abgerufen und auf Empfänger, Aktenzeichen, Dateinamen, Anzahl der Anhänge, Zeitstempel und positiven Eingangsstatus geprüft wurde.

- KG, Beschluss vom 22. August 2023, 27 U 40/23: Eingang liegt mit Speicherung auf der für das Gericht bestimmten Empfangseinrichtung vor; eine spätere interne Zuordnung ändert den Eingangszeitpunkt nicht.
- OLG Brandenburg, Beschluss vom 23. August 2022, 12 U 113/22: Die Frist darf erst gelöscht werden, wenn die gerichtliche Eingangsbestätigung `request executed` und den Übermittlungsstatus `erfolgreich` ausweist; bloße Kanzleivermerke genügen nicht.
- BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22: Die Ausgangskontrolle muss den erfolgreichen Eingang und die richtige Übermittlung des fristgebundenen Dokuments erfassen.
- BGH, Beschluss vom 24. April 2025, III ZB 12/24: Die Eingangsbestätigung muss abgerufen und kontrolliert werden; der organisatorische Zeitpunkt ist frei, solange noch eine ausreichende Reaktionsreserve bleibt.

Speichere Exportnachricht, Prüfvermerk, Eingangsbestätigung und endgültige Versanddateien gemeinsam und unveränderbar in der Mandatsakte.

## 10. Technische Störung und ungeeignetes Dokument

Trenne strikt:

1. ZPO Paragraf 130a Absatz 6 betrifft ein bereits eingereichtes, für die Bearbeitung ungeeignetes elektronisches Dokument. Nach gerichtlichem Hinweis kann die frühere Wirkung durch unverzügliche Nachreichung in geeigneter Form erhalten werden, wenn die inhaltliche Übereinstimmung glaubhaft gemacht wird.
2. ZPO Paragraf 130d Sätze 2 bis 4 betreffen die vorübergehende technische Unmöglichkeit der elektronischen Übermittlung und die Ersatzeinreichung nach allgemeinen Vorschriften.

Für eine Ersatzeinreichung erstelle eine geschlossene Minutenchronologie mit Fehlermeldung, betroffener Infrastruktur, Versandversuchen, Störungsquelle, Ersatzweg und Belegen.

- BGH, Beschluss vom 19. Dezember 2024, IX ZB 41/23: Ist die Ersatzeinreichung veranlasst, sind keine fortlaufenden neuen elektronischen Versuche bis zu ihrem Vollzug erforderlich; eine zuverlässige veröffentlichte Serverstörung kann die Glaubhaftmachung tragen.
- BGH, Beschluss vom 25. Februar 2025, VI ZB 19/24: Die Darstellung muss technisch, vorübergehend und aus sich heraus verständlich sein; sie muss Bedienungs- oder persönliche Gründe als Ursache nachvollziehbar zurückdrängen.
- OLG Brandenburg, Urteil vom 28. April 2023, 11 U 244/22: Eine pauschale Störungsmitteilung und ein nicht aussagekräftiger Bildschirmabzug belegen weder Dauer noch Umfang der Störung; die Nachweise sind unverzüglich zu sichern und vorzulegen.
- OLG Hamm, Beschluss vom 25. März 2022, 25 U 70/21: Fehlende einsatzbereite Zugangsmittel sprechen gegen eine nur vorübergehende technische Störung; jedenfalls muss die Glaubhaftmachung bei der Ersatzeinreichung oder unverzüglich danach erfolgen.
- LAG Berlin-Brandenburg, Beschluss vom 23. Dezember 2024, 5 Sa 982/24: Die Formel `wg. beA-Störung` genügt nicht; eine mehr als einwöchige Verzögerung der Glaubhaftmachung ist regelmäßig nicht unverzüglich.
- LG Hagen, Urteil vom 15. Oktober 2024, 4 O 209/24: Eine ohne die Voraussetzungen der Ersatzeinreichung auf Papier erhobene Klage ist unwirksam und wird nicht beliebig später durch elektronische Nachreichung geheilt.

## 11. Auslieferung

Liefere diese Ordnerstruktur:

```text
versandfertig/
  00_..._Schriftsatz_....pdf
  01_..._AnlageK1_....pdf
  02_..._AnlageK2_....pdf
intern/
  Anlagenverzeichnis.md
  Versandmanifest.csv
  Preflight-Bericht.md
  Freigabevermerk.md
  Eingangskontrolle.md
```

Der interne Ordner wird nicht mitgesendet, sofern sein Inhalt nicht ausdrücklich Teil der Einreichung sein soll.

## 12. Freigabeampel

### 12.1 Rot

- Frist, Gericht oder Übermittlungsweg ungeklärt.
- Hauptdokument nicht final oder nicht formwirksam signierbar.
- Anlage fehlt, ist unlesbar, verschlüsselt oder widerspricht dem Schriftsatz.
- Nummernkreis kollidiert mit bereits eingereichten Anlagen.
- Eingebettete Datei, aktiver Inhalt oder nicht erklärter Formfehler.

### 12.2 Gelb

- OCR fehlt bei lesbarem Scan.
- Lokale Namenskonvention ist nicht auffindbar; Gerichtssicher-Profil wird dokumentiert verwendet.
- PDF/A wurde nicht technisch validiert.

### 12.3 Grün

Grün erst, wenn Anwalt, Schriftsatzfassung, Anlagenstand, Signaturweg, Empfänger, Frist und Eingangskontrolle feststehen. Gib dann einen ausformulierten Freigabevermerk aus, aber löse keinen Versand aus.

## 13. Quellen

Nutze die amtlich verlinkte und nach Themen geordnete Referenz unter `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md`. Lokale Gerichtshinweise sind Organisationshilfen und dürfen gesetzliche Formvorschriften nicht ersetzen.

---

## Skill: `anlagen-zu-schriftsaetzen`

_Hauptworkflow für gerichtliche Anlagenproduktion: liest Schriftsatz und Aktenordner zuerst, verbindet jede Behauptung mit ihrem Beleg, hält K-, B-, AST- oder AG-Nummern fort, erkennt Lücken und Dubletten und routet bei bevorstehendem Versand unmittelbar in die beA-Endfertigung mit PDF-, Stempel-, Dateinamen-, Signatur- und Eingangskontrolle._

# Anlagen zu Schriftsätzen bauen

## 1. Direktstart

Wenn Schriftsatz und Dateien vorliegen, lies zuerst den maßgeblichen Schriftsatz und erfasse die Dateinamen. Öffne anschließend die darin zitierten Belege; bei großen Ordnern arbeite abschnittsweise und kennzeichne noch nicht gelesene Unterlagen. Frage nicht erneut nach bereits belegten Angaben. Erzeuge eine Belegmatrix und kennzeichne:

1. Anlagenzitate ohne Datei,
2. Dateien ohne Anlagenzitat,
3. widersprüchliche Nummern oder Bezeichnungen,
4. entscheidungserheblichen Vortrag, der nur in einer Anlage steht,
5. Frist-, Lesbarkeits-, Schwärzungs- oder Formatrisiken.

Frage höchstens nach der Rolle oder dem bisher verwendeten Nummernkreis, wenn diese Weiche nicht aus Schriftsatz und Akte folgt.

## 2. Belegmatrix

| Schriftsatzstelle | Tatsachenbehauptung | Beweisangebot | Anlage | Quelldatei | Status |
| --- | --- | --- | --- | --- | --- |
| Seite und Absatz | ausformulierter Tatsachenkern | Urkunde, Zeuge oder anderes Beweismittel | K 1 oder B 1 | eindeutiger Dateiname | vorhanden, fehlt oder widersprüchlich |

Die Reihenfolge folgt dem Beweisgang des Schriftsatzes, nicht dem zufälligen Ordnernamen. Eine Anlage belegt eine im Schriftsatz vorgetragene Tatsache; sie ersetzt den Vortrag nicht.

## 3. Nummernkreis

Klägeranlagen laufen als `K`, Beklagtenanlagen als `B`, Antragsteller- und Antragsgegneranlagen nach dem erkennbaren Gerichts- oder Kanzleistandard. Replik und Duplik setzen den bisherigen Nummernkreis fort. Beginne nie stillschweigend wieder bei 1.

## 4. Produktionsweiche

Wenn nur die inhaltliche Zuordnung offen ist, arbeite die Belegmatrix und Lückenliste ab. Sobald der Schriftsatz versandt werden soll, wechsle ohne erneutes Vollinterview in `bea-versandmappe-endfertigung`.

Das Werkzeug `werkzeuge/build_anlagenkonvolut.py` erzeugt aus vorbereiteten Dateien einen Versandordner und interne Prüfunterlagen. Es stempelt standardmäßig jede Seite und versendet nichts. Die juristische Zuordnung und die anwaltliche Freigabe bleiben vorgelagert.

Der Office-Lauf verwendet ein eigenes temporäres Profil und akzeptiert nur eine neu erzeugte, lesbare PDF. Nach 120 Sekunden endet die Konvertierung der betroffenen Anlage; unter Linux und macOS werden auch ihre Kindprozesse beendet. Sichere den Fehler in der Stop-Liste, bearbeite die übrigen Belege weiter und verlange gezielt einen Ersatzexport. Keine unveränderte Wiederholungsschleife, kein stilles Weglassen der Anlage und keine Versandfreigabe trotz fehlgeschlagener Konvertierung.

## 5. Ergebnis

Liefere je nach Arbeitsstand:

1. Belegmatrix und Lückenliste,
2. fortgeschriebenes Anlagenverzeichnis,
3. konkrete Umbenennungs- und Konvertierungsanweisung,
4. versandfertige Einzel-PDFs und interne Prüffassung,
5. Freigabevermerk und Eingangskontrollplan.

Die Rechts- und Technikanker stehen in `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md`.

---

## Skill: `einstieg-routing`

_Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Anlagen zu Schriftsätzen._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Anlagen Zu Schriftsaetzen** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anlage-fehlerkatalog` — Anlage Fehlerkatalog
- `anlage-red-anlagen-anlagenkonvolut-sonderfall` — Anlage RED Anlagen Anlagenkonvolut Sonderfall
- `anlagen-an-assistenz-uebersetzungspflicht` — Anlagen AN Assistenz Übersetzungspflicht
- `anlagen-aus-datenraum-und-sharepoint` — Anlagen AUS Datenraum und Sharepoint
- `anlagen-aus-edv-systemen` — Anlagen AUS EDV Systemen
- `anlagen-aus-mandantenmaterial` — Anlagen AUS Mandantenmaterial
- `anlagen-bei-berufung-revision` — Anlagen bei Berufung Revision
- `anlagen-bei-eilantrag-eu-arrest` — Anlagen bei Eilantrag EU Arrest
- `anlagen-berufung-revision-eilantrag-eu-bilder` — Anlagen Berufung Revision Eilantrag EU Bilder
- `anlagen-bilder-screenshots` — Anlagen Bilder Screenshots
- `anlagen-check-zustellung-redaktion-dsgvo` — Anlagen Check Zustellung Redaktion DSGVO
- `anlagen-duplikate-versionen-hashlog` — Anlagen Duplikate Versionen Hashlog
- `anlagen-elektronische-dokumente-format` — Anlagen Elektronische Dokumente Format
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Anlagen Zu Schriftsaetzen sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Für Kaltstart Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Anlagen zu Schriftsätzen._

# Schriftsatzanlagen sichten und die Aufbereitung starten

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Normenanker

Arbeitsfokus: **Anlagen zu Schriftsätzen — Allgemein**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schnelle Eingang in das Plugin **Anlagen zu Schriftsätzen**. Er behandelt Anlagen nicht als Dateiverwaltung, sondern als Prozesswerkzeug: Aus einem Schriftsatz und einem unordentlichen Dokumentenbestand muss ein Gericht, ein Schiedsgericht oder eine Gegenseite ohne Rätsel erkennen können, welche Tatsache durch welche Anlage belegt werden soll.

**Plugin-Fokus:** Schriftsatzlogik, K/B/AST/AG-Nummerierung, K1-Konvolutlogik, Anlagenverzeichnis, beA-/ERV-taugliche Dateinamen, OCR/Lesbarkeit, Duplikat-/Hashkontrolle, Datenschutz-/Geschäftsgeheimnis-Redaktion, Nachreichungen und Qualitygate vor Versand.

### 0. Der erste Satz

Beginne bei neuen Anfragen mit einem knappen Arbeitsversprechen:

> Ich sortiere das als Anlagenpaket. Zuerst kläre ich Nummernkreis und Ziel-Schriftsatz, dann baue ich eine Belegmatrix, dann kommen Dateinamen, Stempel, Konvolute und Versandcheck.

Wenn Material vorliegt, arbeite sofort. Wenn nichts vorliegt, stelle höchstens diese eine Frage:

> Geht es um Kläger-/Antragstelleranlagen (`K`/`AST`) oder Beklagten-/Antragsgegneranlagen (`B`/`AG`), und gibt es schon einen Schriftsatzentwurf?

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Nummernkreis | `K`, `B`, `AST`, `AG`, `BK`, `BB`, `S-W` oder eigenes Schema? | Der Nummernkreis bestimmt Dateinamen, Stempel und Verzeichnis. |
| Ziel-Schriftsatz | Klage, Erwiderung, Replik, Duplik, Eilantrag, Berufung, Schiedsverfahren? | Die Reihenfolge folgt dem Vortrag, nicht dem Dateisystem. |
| Modus | Auto-Benennung, Schriftsatz folgt, Prüfmodus oder Rettung nach Hinweis? | Verhindert unnötige Neuordnung. |
| Material | Einzeldateien, ZIP, Datenraumexport, EML/MSG, XLSX, Fotos, Scans, PDFs? | Dateitypen brauchen unterschiedliche Behandlung. |
| K1/Kernanlage | Gibt es eine Leit-Anlage, z. B. Vertrag/Auftrag/Bescheid/Protokoll? | K1 entscheidet oft die Lesbarkeit der ganzen Akte. |
| Frist/Versand | beA-Abgabe, Gerichtstermin, gerichtlicher Hinweis, Nachreichungsfrist? | Eilsachen zuerst sichern. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Versandfrist, gerichtlicher Hinweis, beA-/ERV-Grenzen, fehlende Kernanlage markieren.
2. **Schriftsatzanker:** Welche Tatsachenbehauptungen brauchen Anlagen? Wo sind die Beweisstellen?
3. **Materialbild:** Welche Dateien liegen vor, welche fehlen, welche sind doppelt oder nur Vorversion?
4. **K1-Entscheidung:** Einzelanlage oder Konvolut? Deckblatt nötig? Welche Fassung ist maßgeblich?
5. **Primärskill wählen:** Genau einen passenden Skill aus diesem Plugin bestimmen und unmittelbar einsetzen. Höchstens zwei Alternativen nur nennen, wenn eine echte Weiche offen ist.
6. **Qualitygate:** Nummern, Verweise, Lesbarkeit, Schwärzung, Dateinamen, Paketgrößen, Lücken.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule gezielt und sparsam laden

1. Wähle zunächst genau einen Primärskill, der zum Auftrag und gewünschten Arbeitsprodukt passt. Weitere Skills kommen nur bei einer konkreten Schnittstelle hinzu.
2. Sind im Arbeitsordner bereits Unterlagen vorhanden, lies zuerst Dateinamen, Metadaten und Inhaltsübersichten. Frage nur nach Informationen, die daraus nicht verlässlich hervorgehen.
3. Grenze Suchen in Microsoft 365 nach Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und prägnantem Suchbegriff ein. Erfasse im ersten Durchgang höchstens 20 Treffer und öffne höchstens fünf tragende Unterlagen.
4. Lies Word- und PDF-Dokumente einmal vollständig, Tabellen nur in den einschlägigen Blättern und Bereichen sowie E-Mails im maßgeblichen Gesprächsverlauf. Verwende gewonnene Extrakte weiter, statt dieselbe Quelle erneut zu öffnen.
5. Die [vollständige Fachmodulkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/anlagen-zu-schriftsaetzen/skills/kaltstart-triage/references/fachmodule.md) wird nur konsultiert, wenn kein eindeutiger Primärskill feststeht oder eine echte Querschnittsfrage verbleibt.

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

---

## Skill: `anlagenkonvolut-konsolidieren`

_Konsolidiert mehrere zusammengehörige Belegdateien zu einer gerichtstauglichen Anlage: liest den Bestand zuerst, trennt Dubletten und Fassungen, bestimmt Eltern- und Unteranlagen, erzeugt Deckblatt, Inhaltsliste, Seitenstempel und Lesezeichen, gleicht jeden Teil mit dem Beweisthema im Schriftsatz ab und liefert Einzelanlage, Prüfkonvolut, Hashprotokoll und._

# Anlagenkonvolut konsolidieren

## 1. Direktstart

Lies zuerst den Schriftsatz, das bisherige Anlagenverzeichnis und sämtliche Kandidatendateien. Liefere ohne vorgeschalteten Fragenkatalog eine Bestandsmatrix mit Dateiname, Datum, Absender, Dokumentart, Seitenzahl, Hashwert, Fassung, Beweisthema und vorgesehener Unteranlage. Frage nur nach einer Zuordnung, die weder aus Datei noch Schriftsatz hervorgeht und die Konsolidierung sperrt.

## 2. Konsolidierungsentscheidung

Mehrere Dokumente dürfen nur dann eine gemeinsame Anlage bilden, wenn sie ein einheitliches Beweisthema nachvollziehbar dokumentieren, etwa eine vollständige E-Mail-Kette mit Anhängen oder einen Vertrag mit Nachträgen. Bloße gemeinsame Herkunft, Dateiformat oder Ordnerlage genügt nicht.

| Entscheidung | Voraussetzung | Ergebnis |
| --- | --- | --- |
| getrennte Anlagen | eigenständige Beweisthemen oder getrennte Schriftsatzbezüge | fortlaufende K- oder B-Nummern |
| Elternanlage mit Unteranlagen | ein Beweisthema, mehrere klar trennbare Dokumente | Deckblatt und K 5/1, K 5/2 fortlaufend |
| eine mehrseitige Anlage | ein Dokument oder untrennbare Dokumentfolge | eine Nummer, jede Seite bezeichnet |
| nur interne Prüffassung | Gesamtüberblick wird gebraucht, Gericht soll Einzeldateien erhalten | Lesezeichen-Konvolut im Ordner `intern/` |

Ein zusammengeführtes Prüfkonvolut ist nicht automatisch die Versandfassung. Gerichtliche Hinweise zur getrennten Einreichung haben Vorrang.

## 3. Produktionslauf

1. Originale unverändert sichern und Hashwerte bilden.
2. Dubletten, Entwürfe, OCR-Fassungen und spätere Endfassungen kennzeichnen; nur eine gerichtliche Fassung je Dokument bestimmen.
3. Beweisthema und genaue Fundstelle im Schriftsatz jeder Datei zuordnen.
4. Elternnummer und Unterfolge ohne Lücken oder Doppelbelegung festlegen.
5. Dateigrenzen, chronologische Reihenfolge und Seitenausrichtung kontrollieren.
6. In PDF konvertieren, Ergebnis visuell gegen das Original prüfen und fehlende OCR kenntlich machen.
7. Deckblatt und kurze Inhaltsliste mit Dokumentdatum, Absender, Empfänger und Seitenbereich erzeugen.
8. Jede Seite oben rechts mit Eltern- und erforderlichenfalls Unteranlagenbezeichnung versehen.
9. Lesezeichen an jeder Dokumentgrenze und eine fortlaufende interne Seitenzählung anlegen.
10. Anlagenzitate, Verzeichnis, Dateinamen und finale PDFs gegeneinander prüfen.

## 4. Normen- und Quellenanker

- ZPO Paragraf 130 Nummer 6: Bezeichnung der beigefügten Urkunden.
- ZPO Paragraf 130a und ERVV Paragraf 2: elektronisches Dokument und technisch geeignete Dateiformate.
- ZPO Paragraf 131: Beifügung von Urkunden, auf die im Schriftsatz Bezug genommen wird.
- ZPO Paragraf 138: konkreter und wahrheitsgemäßer Tatsachenvortrag; ein Anlagenkonvolut ersetzt keinen verständlichen Vortrag im Schriftsatz.
- ZPO Paragraf 253 Absatz 2: bestimmter Antrag und hinreichend bestimmter Klagegrund bleiben im Hauptdokument erforderlich.

Für Format-, Dateinamen- und Versandfragen gelten `references/ANLAGEN-STANDARDS.md` und `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md`. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und geprüfter amtlicher Quelle verwendet.

## 5. Stop-Kriterien

Stoppe die Versandfreigabe bei fehlender oder doppelter Nummer, nicht erklärter Fassung, unterbrochener E-Mail-Kette, unlesbarer Seite, fehlendem Anhang, unstimmigem Schriftsatzbezug, aktivem PDF-Inhalt, Kennwortschutz oder nicht kontrollierter Konvertierung. Beschreibe den Befund datei- und seitengenau und nenne den nächsten Reparaturschritt.

## 6. Output

Liefere eine gerichtliche Einzelanlage oder getrennte Einzelanlagen, ein Anlagenverzeichnis, eine Zuordnungsmatrix Schriftsatzstelle zu Beleg, ein Hash- und Fassungsprotokoll, einen visuellen Prüfvermerk und nur bei Bedarf ein internes Lesezeichen-Konvolut. Übergib die fertigen Dateien anschließend an `bea-versandmappe-endfertigung`.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `anlagen-fuer-bea-versand`

_Bereitet vorhandene Anlagen tatsächlich für den beA-Versand vor: liest zuerst Schriftsatz und Ordner, setzt den bisherigen Nummernkreis fort, konvertiert jede Anlage kontrolliert in eine eigene PDF, stempelt sämtliche Seiten oben rechts, erstellt sichere Dateinamen und liefert Versandordner, Anlagenverzeichnis, Preflight-Bericht und Lückenliste._

# Anlagen für beA-Versand

## 1. Direktstart

Liegt Material vor, beginne mit der Zuordnung und nicht mit einem Interview. Lies sämtliche Anlagenzitate aus dem Schriftsatz, ordne die vorhandenen Dateien zu und liefere die erste Belegmatrix. Frage nur nach der Prozessrolle oder der letzten bereits eingereichten Anlagenziffer, wenn dies nicht aus der Akte folgt.

## 2. Produktionsfolge

1. Schriftsatzbezug und Beweisthema jeder Anlage festhalten.
2. Fehlende, doppelte, alte oder widersprüchliche Dateien ausweisen.
3. K-, B-, AST- oder AG-Nummern fortsetzen; bei Replik oder Duplik nicht neu beginnen.
4. Arbeitsdateien kontrolliert in PDF konvertieren und das Ergebnis visuell prüfen.
5. Auf jeder Seite oben rechts die vollständige Anlagenbezeichnung anbringen.
6. Dateinamen nach Gerichtshinweis oder dokumentiertem Sicherheitsprofil erzeugen.
7. Einzel-PDFs, Anlagenverzeichnis, Hashmanifest und Preflight-Bericht ausgeben.

## 3. Technikwerkzeug

Für lokale Dateien nutze `../anlagen-zu-schriftsaetzen/werkzeuge/build_anlagenkonvolut.py`. Ein typischer Lauf lautet:

```bash
python3 werkzeuge/build_anlagenkonvolut.py \
  --eingang ./anlagen \
  --hauptdokument ./Schriftsatz_final.docx \
  --ausgang ./bea-versandmappe \
  --praefix K \
  --dokumentart Replik \
  --profil berlin \
  --datum 20260710 \
  --gericht "Landgericht Berlin II" \
  --aktenzeichen "12 O 34/26" \
  --strict
```

Der Eingangsname einer Anlage folgt `Anlage_K-01_Kaufvertrag.pdf` oder derselben Kennung mit einer unterstützten Office- oder Bildendung. Das Werkzeug versendet nichts und ersetzt keine Sichtkontrolle.

## 4. Formanker

- ZPO Paragraf 130a Absatz 3: Signatur des Hauptdokuments; Anlagen benötigen keine eigene Signatur.
- ZPO Paragraf 130a Absatz 5: Eingang und automatisierte Eingangsbestätigung.
- ZPO Paragraf 130d: Nutzungspflicht und Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit.
- ERVV Paragraf 2 und ERVB 2025: PDF, technische Eignung und Nachrichtengrenzen.

## 5. Abschluss

Wechsle für Signaturweg, Freigabevermerk und Eingangskontrolle unmittelbar in `bea-versandmappe-endfertigung`. Ein grüner technischer Preflight allein bedeutet noch keine anwaltliche Versandfreigabe.

---

## Skill: `anlagen-portal-bea-einreichungslogik`

_Steuert den formwirksamen elektronischen Versand gerichtlicher Dokumente: bestimmt Verfahrensordnung und Portal, trennt qualifizierte Signatur vom persönlichen sicheren Übermittlungsweg, prüft Empfänger und Aktenzeichen, plant Ersatzeinreichung und kontrolliert nach Versand jede gerichtliche Eingangsbestätigung samt Anhängen und Zeitstempel._

# Portal, beA und Einreichungslogik

## 1. Verfahrensordnung zuerst

Bestimme Zivil-, Arbeits-, Sozial-, Verwaltungs-, Finanz- oder Strafverfahren. Verwende die jeweils einschlägige Pflichtnorm und nicht automatisch ZPO Paragraf 130d. Bei einer direkten Klage vor dem Gericht der Europäischen Union ist e-Curia statt beA zu prüfen.

## 2. Formweg

| Weg | Hauptdokument | tatsächlicher Versand |
| --- | --- | --- |
| qualifizierte elektronische Signatur | qualifiziert von der verantwortenden Person signiert | Mitarbeiter kann technisch versenden |
| sicherer Übermittlungsweg | einfach signiert, regelmäßig durch Namenswiedergabe am Ende | verantwortender Postfachinhaber versendet persönlich |

BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23, und BGH, Beschluss vom 4. September 2024, IV ZB 31/23, verlangen bei einfacher Signatur die Übereinstimmung von verantwortender Person und persönlichem Versender. BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23, bestätigt, dass Mitarbeiter-Versand keinen sicheren Übermittlungsweg herstellt.

## 3. Vor Versand

1. Empfänger aus dem Verzeichnis auswählen und Gericht mit Rubrum abgleichen.
2. Gerichtliches Aktenzeichen exakt in das Empfängerfeld übernehmen; bei Neueingang entsprechend kennzeichnen.
3. Hauptdokument, Anlagenzahl, Dateinamen und Hashmanifest abgleichen.
4. Signaturweg dokumentieren.
5. Bei Eilsache Betreff nach gerichtlichem Hinweis konkret kennzeichnen.
6. Ausreichende Zeitreserve für Übertragung, Eingangsprüfung und erneuten Versand lassen.

## 4. Nach Versand

Nach ZPO Paragraf 130a Absatz 5 liegt Eingang mit Speicherung auf der für das Gericht bestimmten Einrichtung vor. KG, Beschluss vom 22. August 2023, 27 U 40/23, ordnet die spätere interne Aktenzuweisung der Gerichtssphäre zu.

Kontrolliere trotzdem unverzüglich oder innerhalb der noch sicheren Organisationsreserve:

1. positiven Eingangsstatus,
2. richtiges Gericht und gerichtliches Aktenzeichen,
3. Hauptdokument und vollständige Anhangsliste,
4. Eingangszeitpunkt,
5. Prüfvermerk zum sicheren Übermittlungsweg oder zur Signatur.

BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22, und BGH, Beschluss vom 24. April 2025, III ZB 12/24, bilden den Kern der Ausgangskontrolle.

## 5. Störung

ZPO Paragraf 130a Absatz 6 ist keine Ersatzeinreichungsnorm. Für vorübergehende technische Unmöglichkeit gilt ZPO Paragraf 130d Sätze 2 bis 4. Nutze dann `bea-wiedereinsetzung-ersatzeinreichung-2026` aus dem Prozessrechtsplugin und liefere eine geschlossene, belegte Minutenchronologie.

## 6. Output

Liefere Versanddatenblatt, Signaturentscheidung, Vorversandcheck, Ersatzeinreichungsreserve und Eingangskontrollvermerk. Nutze `bea-versandmappe-endfertigung` als abschließenden Gesamtworkflow.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
