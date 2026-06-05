---
name: vertragsausfueller-vaf-bsag-mietvertrag-klauselentscheidung
description: "VAF Bsag Mietvertrag Klauselentscheidung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# VAF Bsag Mietvertrag Klauselentscheidung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **VAF Bsag Mietvertrag Klauselentscheidung** im Plugin Vertragsausfüller. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vaf-bsag-mietvertrag` | BSAG-Kiosk-Mietvertrag ausfüllen: Anwendungsfall BSAG-Term Sheet Huckelriede liegt vor und muss in Mietvertragsvorlage übertragen werden. §§ 535 ff. BGB Mietvertrag, § 9 UStG Umsatzsteueroption, § 550 BGB Schriftformerfordernis. Prüfraster BSAG-Handelsregisterprüfung, Term Sheet vollständig Fläche Nutzungsart Miete Laufzeit, USt-Option Vorsteuerabzug, Konkurrenzschutzklausel. Output ausgefüllter BSAG-Mietvertragsentwurf mit Lückenmarkierung und Klauselentscheidungen. Abgrenzung zu allgemeinem Kommandocenter und zu Template-Erkennung. |
| `vaf-klauselentscheidung` | Wahlklauseln und Klauselalternativen im Vertrag entscheiden: Anwendungsfall Vertrag enthält optionale Klauseln wie Umsatzsteueroption Indexierung Konkurrenzschutz Rückbau oder Betriebspflicht die aktiv angekreuzt oder formuliert werden müssen. §§ 307-309 BGB AGB-Kontrolle, § 557b BGB Indexmiete, § 9 UStG USt-Option. Prüfraster B2B vs. B2C Kontrollintensität, AGB vs. Individualklausel, branchenspezifische Pflichtklauseln, Haftungsbeschränkungs-Grenzen. Output Klauselentscheidungs-Protokoll mit Optionsauswahl und Begründung. Abgrenzung zu Feldinventar und zu Plausibilitätscheck. |
| `vaf-konzern-rahmenvertrag-anpassen` | Spezialfall Rahmenvertrag im Konzern anpassen ohne Aenderung der Substanz: typische Stellen wie Vergueng, Laufzeit, Liefermenge. Pruefraster fuer Aenderungsfreigabe und Track-Changes-Diskussion mit Gegenseite. Mustertexte. |

## Arbeitsweg

Im Plugin Vertragsausfüller gilt für **VAF Bsag Mietvertrag Klauselentscheidung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vaf-bsag-mietvertrag`

**Fokus:** BSAG-Kiosk-Mietvertrag ausfüllen: Anwendungsfall BSAG-Term Sheet Huckelriede liegt vor und muss in Mietvertragsvorlage übertragen werden. §§ 535 ff. BGB Mietvertrag, § 9 UStG Umsatzsteueroption, § 550 BGB Schriftformerfordernis. Prüfraster BSAG-Handelsregisterprüfung, Term Sheet vollständig Fläche Nutzungsart Miete Laufzeit, USt-Option Vorsteuerabzug, Konkurrenzschutzklausel. Output ausgefüllter BSAG-Mietvertragsentwurf mit Lückenmarkierung und Klauselentscheidungen. Abgrenzung zu allgemeinem Kommandocenter und zu Template-Erkennung.

# BSAG-Mietvertrag


## Triage zu Beginn

1. Ist die BSAG als Vermieterin im Handelsregister eingetragen und ist die Vertretung aktuell?
2. Liegt das Term Sheet Huckelriede vollständig vor (Fläche, Nutzungsart, Miete, Laufzeit)?
3. Gibt es USt-Option (§ 9 UStG) — ist BSAG als Vermieter zum Vorsteuerabzug berechtigt?
4. Soll eine Konkurrenzschutzklausel aufgenommen werden und welchen Umfang?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 535, 536 BGB — Miete und Mängelgewährleistung
- § 550 BGB — Schriftformerfordernis bei Mietdauer > 1 Jahr
- § 578 BGB — Gewerbemietrecht (entsprechende Anwendung)
- § 9 UStG — Option zur Umsatzsteuer (wichtig für BSAG-Mietvertrag)
- § 305 ff. BGB — AGB-Kontrolle gewerblicher Klauseln

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill setzt den Huckelriede-Term-Sheet-Fall in die BSAG-Vorlage um. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. BSAG-Stammdaten als feste Vermieterdaten übernehmen.
2. Mieter, Mietobjekt, Fläche, Nutzung, Miete, Nebenkosten, Kaution, Laufzeit, Option, Indexierung, Öffnungszeiten und Sonderbedingungen mappen.
3. Sonderpunkte wie Konkurrenzschutz, Fettabscheider, Sauberhaltung, Sortiment, Werbung und Rückbau als Klauselentscheidungen abfragen.
4. Clean-Entwurf, Ausfüllprotokoll und auf Wunsch nach Rückfrage Redline-Fassung vorbereiten.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.

## 2. `vaf-klauselentscheidung`

**Fokus:** Wahlklauseln und Klauselalternativen im Vertrag entscheiden: Anwendungsfall Vertrag enthält optionale Klauseln wie Umsatzsteueroption Indexierung Konkurrenzschutz Rückbau oder Betriebspflicht die aktiv angekreuzt oder formuliert werden müssen. §§ 307-309 BGB AGB-Kontrolle, § 557b BGB Indexmiete, § 9 UStG USt-Option. Prüfraster B2B vs. B2C Kontrollintensität, AGB vs. Individualklausel, branchenspezifische Pflichtklauseln, Haftungsbeschränkungs-Grenzen. Output Klauselentscheidungs-Protokoll mit Optionsauswahl und Begründung. Abgrenzung zu Feldinventar und zu Plausibilitätscheck.

# Klauselentscheidungen


## Triage zu Beginn

1. Handelt es sich um B2B oder B2C — die Kontrollintensität nach § 307 ff. BGB ist unterschiedlich?
2. Welche Klauseln sind verhandelbar (individualvertraglich) und welche sind AGB des Verwenders?
3. Gibt es branchenspezifische Pflichtklauseln (z.B. Indexklausel § 557b BGB bei Wohnraummiete)?
4. Sind Vertragsstrafen, Haftungsbeschränkungen oder Schiedsklauseln vorgesehen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 307 BGB — Inhaltskontrolle Generalklausel (unangemessene Benachteiligung)
- § 308 BGB — Klauselverbote mit Wertungsmöglichkeit
- § 309 BGB — Klauselverbote ohne Wertungsmöglichkeit (Liste)
- § 310 Abs. 1 BGB — B2B: eingeschränkte Inhaltskontrolle
- § 1031 ZPO — Schiedsvereinbarung (Formerfordernis)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill verhindert stilles Auswählen riskanter Optionen. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Jede Wahlklausel als Entscheidung mit kurzer Konsequenz formulieren.
2. Standardeinstellung, Term-Sheet-Wunsch und rechtliches Risiko nebeneinander stellen.
3. Bei fehlender Entscheidung eine neutrale Platzhalterklausel mit Warnhinweis verwenden.
4. Entscheidungen im Ausfüllprotokoll dokumentieren.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.


---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

Dieser Skill wurde im Rahmen von Bundle 046 auf halluzinierte Rechtsprechungsnachweise geprüft und korrigiert.

## 3. `vaf-konzern-rahmenvertrag-anpassen`

**Fokus:** Spezialfall Rahmenvertrag im Konzern anpassen ohne Aenderung der Substanz: typische Stellen wie Vergueng, Laufzeit, Liefermenge. Pruefraster fuer Aenderungsfreigabe und Track-Changes-Diskussion mit Gegenseite. Mustertexte.

# Rahmenvertrag-Anpassung

## Spezialwissen: Rahmenvertrag-Anpassung
- **Spezialgegenstand:** Rahmenvertrag-Anpassung / vaf konzern rahmenvertrag anpassen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
