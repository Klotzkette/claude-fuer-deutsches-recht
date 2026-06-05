---
name: ehegattenvertretung-bgb-ehrenamtlicher
description: "Ehegattenvertretung BGB Ehrenamtlicher: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ehegattenvertretung BGB Ehrenamtlicher

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ehegattenvertretung BGB Ehrenamtlicher** im Plugin Betreuungsrecht (§§ 1814 ff. BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ehegattenvertretung-1358-bgb` | Notvertretungsrecht Ehegatten § 1358 BGB seit 01.01.2023: Voraussetzungen, sechsmonatige Befristung, Pflichten, Abgrenzung zur Betreuung. Vorlage Information Mandanten. |
| `ehrenamtlicher-betreuer-erster-monat` | Start-für ehrenamtliche und familiäre Betreuer in den ersten 30 Tagen: Bestellungsbeschluss verstehen, Aufgabenkreise lesen, Betreuungsgericht kontaktieren, Betreuungsverein/Behörde anbinden, Vermögens- und Gesundheitsunterlagen sichern, Fristenkalender anlegen und Überforderung vermeiden. |
| `familienbetreuer-alltagscockpit` | Alltags-Cockpit für Familienbetreuer: macht aus Post, Pflege, Bank, Arztterminen, Heimkontakt, Behörden und Gericht einen handhabbaren Wochenplan mit Aufgabenliste, Verantwortlichen, Ampel, Gesprächsnotizen und dokumentierten Entscheidungen der betreuten Person. |

## Arbeitsweg

Im Plugin Betreuungsrecht (§§ 1814 ff. BGB) gilt für **Ehegattenvertretung BGB Ehrenamtlicher**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ehegattenvertretung-1358-bgb`

**Fokus:** Notvertretungsrecht Ehegatten § 1358 BGB seit 01.01.2023: Voraussetzungen, sechsmonatige Befristung, Pflichten, Abgrenzung zur Betreuung. Vorlage Information Mandanten.

# § 1358 BGB Ehegattenvertretung

## Spezialwissen: § 1358 BGB Ehegattenvertretung
- **Spezialgegenstand:** § 1358 BGB Ehegattenvertretung / ehegattenvertretung 1358 bgb. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
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

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
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

## 2. `ehrenamtlicher-betreuer-erster-monat`

**Fokus:** Start-für ehrenamtliche und familiäre Betreuer in den ersten 30 Tagen: Bestellungsbeschluss verstehen, Aufgabenkreise lesen, Betreuungsgericht kontaktieren, Betreuungsverein/Behörde anbinden, Vermögens- und Gesundheitsunterlagen sichern, Fristenkalender anlegen und Überforderung vermeiden.

# Ehrenamtlicher Betreuer: erster Monat

## Zweck

Dieser Skill führt nicht berufliche Betreuer Schritt für Schritt durch die ersten vier Wochen nach Bestellung. Er arbeitet beruhigend, praktisch und gerichtstauglich: Was muss sofort passieren, was darf warten, was darf der Betreuer überhaupt, und wann wird Hilfe geholt?

## Einstieg

Frage nur diese Punkte ab:

1. Liegt ein gerichtlicher Beschluss oder nur eine Anregung vor?
2. Welche Aufgabenkreise stehen genau im Beschluss?
3. Ist die betreute Person ansprechbar und kann sie Wünsche äußern?
4. Gibt es Fristen, drohende Kündigungen, Klinikentlassung, Heimvertrag, Konto- oder Zahlungsprobleme?
5. Ist der Betreuer Angehöriger/persönlich verbunden oder ohne persönliche Bindung?

## 30-Tage-Plan

### Tag 1 bis 3: Beschluss und Eilschutz

- Beschluss lesen: Gericht, Aktenzeichen, Aufgabenkreise, Beginn, befristete/einstweilige Anordnung, besondere Genehmigungsvorbehalte.
- Bestellungsurkunde als Arbeitsdokument sichern; nur vorzeigen, nicht unnötig kopieren lassen.
- Fristenampel anlegen: Gerichtstermine, Gutachten, Jahresbericht, Vermögensverzeichnis, Bescheide, Miet-/Heim-/Pflegefristen.
- Die betreute Person sprechen, sofern möglich: Was will sie? Was soll auf keinen Fall passieren?
- Bei Gefahr für Gesundheit, Wohnung, Konto oder Pflege sofort passende Fachmodule routen.

### Woche 1: Hilfe-System aktivieren

- Betreuungsgericht um Einführungsgespräch bitten, falls noch nicht terminiert.
- Betreuungsbehörde und örtlichen Betreuungsverein identifizieren.
- Bei erstmaliger ehrenamtlicher Betreuung: Führungszeugnis und Schuldnerverzeichnis-Auskunft nach § 21 BtOG klären.
- Bei nicht familiärer/persönlicher Bindung: Vereinbarung zur Begleitung und Unterstützung nach § 22 BtOG vorbereiten.
- Bei Familienbetreuung: freiwillige Anbindung trotzdem empfehlen, wenn Vermögen, Gesundheit, Heim, Streit oder Behördenstress vorliegt.

### Woche 2: Unterlagen sichern

Baue eine Akte mit diesen Fächern:

- Gericht: Beschluss, Bestellungsurkunde, Schreiben, Fristen.
- Person: Ausweis, Kontaktliste, Vorsorgevollmacht/Patientenverfügung/Betreuungsverfügung.
- Gesundheit: Arztkontakte, Medikationsplan, Pflegegrad, Klinik/Heim.
- Wohnen: Mietvertrag, Heimvertrag, Nebenkosten, Versicherungen.
- Geld: Konten, Rente, Sozialleistungen, Schulden, Verträge, Bargeld, Wertgegenstände.
- Wünsche: Gesprächsnotizen, frühere Äußerungen, Familienhinweise, rote Linien.

### Woche 3 bis 4: Gerichtstaugliche Ordnung

- Vermögensverzeichnis nur bei Aufgabenkreis Vermögenssorge erstellen und mit Belegen unterlegen (§ 1835 BGB).
- Anfangsbericht prüfen: Bei familiärer/persönlicher ehrenamtlicher Betreuung greift § 1863 Abs. 2 BGB; Vermögensverzeichnis bleibt bei Vermögenssorge trotzdem Thema.
- Jahresbericht-Termin vormerken (§ 1863 Abs. 3 BGB).
- Wiederkehrende Aufgaben in Kalender/Reminder übertragen.
- Offene Risiken als Ampel ausgeben: rot sofort, gelb diese Woche, grün laufend beobachten.

## Output

Erstelle am Ende:

1. `Kurzstatus Betreuung`
2. `30-Tage-Checkliste`
3. `Fristen- und Erinnerungsliste`
4. `Unterlagen-Lückenliste`
5. `Nächste Nachricht an Betreuungsgericht / Behörde / Betreuungsverein`

## Qualitätsregeln

- Nicht bevormundend schreiben: Betreuung ist Unterstützung, nicht Entmündigung.
- Wünsche der betreuten Person zuerst erfassen (§ 1821 BGB).
- Vertretung nur nutzen, soweit sie erforderlich ist (§ 1821 Abs. 1 BGB).
- Bei Grundstück, Erbe, Wohnungsaufgabe, riskanten Geldgeschäften, freiheitsentziehenden Maßnahmen oder Zwangsbehandlung immer Genehmigungspflicht prüfen.
- Keine Rechtsprechung aus Modellwissen zitieren; nur nach Live-Prüfung.

## 3. `familienbetreuer-alltagscockpit`

**Fokus:** Alltags-Cockpit für Familienbetreuer: macht aus Post, Pflege, Bank, Arztterminen, Heimkontakt, Behörden und Gericht einen handhabbaren Wochenplan mit Aufgabenliste, Verantwortlichen, Ampel, Gesprächsnotizen und dokumentierten Entscheidungen der betreuten Person.

# Familienbetreuer-Alltagscockpit

## Zweck

Dieser Skill nimmt Familienbetreuern die Unordnung aus dem Alltag. Er verwandelt Scans, Fotos, E-Mails, Post, Telefonnotizen und Sorgen in eine Woche-für-Woche-Steuerung, ohne die betreute Person zu übergehen.

## Sofortmodus

Wenn Dokumente hochgeladen werden, erstelle ohne lange Rückfragen:

- eine Dokumentenliste,
- eine Fristenliste,
- eine Aufgabenliste,
- eine Risikoampel,
- eine Rückfragenliste an Gericht, Pflegeheim, Bank, Arzt oder Behörde.

## Wochenstruktur

| Bereich | Typische Aufgabe | Output |
| --- | --- | --- |
| Person | Besuch, Telefonat, Wunsch, Stimmung, Konflikt | Kontaktvermerk mit Wunschbezug |
| Gesundheit | Arzttermin, Einwilligung, Medikationsplan, Pflegegrad | Fragenliste und Einwilligungscheck |
| Wohnen | Miete, Heim, Reparaturen, Wohnungsauflösung | Entscheidungsvorlage mit Genehmigungscheck |
| Geld | Rechnungen, Kontostand, Daueraufträge, Versicherungen | Zahlungsplan und Belegliste |
| Behörden | Rente, Pflegekasse, Sozialamt, Krankenkasse | Bescheid- und Fristenmatrix |
| Gericht | Jahresbericht, Vermögensverzeichnis, Genehmigung | Einreichungsplan |

## Arbeitsweise

1. **Alles sammeln:** Post fotografieren/scannen, E-Mails weiterleiten, Kontoauszüge chronologisch ablegen.
2. **Nichts vermischen:** eigenes Geld und Geld der betreuten Person strikt trennen (§ 1836 BGB).
3. **Wünsche dokumentieren:** Nicht nur Ergebnis notieren, sondern wie die betreute Person beteiligt wurde.
4. **Entscheidungen klein halten:** erst unterstützen, dann vertreten; nicht aus Gewohnheit alles selbst entscheiden.
5. **Gericht nur sinnvoll belasten:** echte Genehmigungsfragen, wesentliche Änderungen, Unsicherheiten und Risiken sauber bündeln.

## Praktische Ausgaben

Erzeuge je nach Lage:

- `Wochenplan Betreuung`
- `Heute dringend / diese Woche / beobachten`
- `Telefonnotiz für Heim/Arzt/Bank`
- `Brief an das Betreuungsgericht`
- `Lückenliste Unterlagen`
- `Mini-Jahresbericht-Zwischenspeicher`

## Grenzen

- Keine medizinische Beratung ersetzen.
- Keine freiheitsentziehenden Maßnahmen ohne Genehmigungsprüfung.
- Keine größeren Vermögensentscheidungen ohne Beleglage, Wunschermittlung und gerichtlichen Genehmigungscheck.
