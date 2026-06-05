---
name: case-management-grundbuchanalyse-immo
description: "Case Management Grundbuchanalyse Immo: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Case Management Grundbuchanalyse Immo

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Case Management Grundbuchanalyse Immo** im Plugin Immobilienrechtspraxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `case-management` | Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output: Case-Management-Übersicht Immobilienrecht. Abgrenzung: nicht Einzelvertragsprüfung. |
| `grundbuchanalyse` | Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Prüfraster: Abteilung I bis III, Widersprueche, Rangverhältnisse, Löschungsansprüche. Output: Grundbuchanalyse-Bericht mit Handlungsempfehlung. Abgrenzung: nicht Kaufvertragsprüfung. |
| `immo-aufteilungsplan-weg` | Aufteilungsplan WEG: Voraussetzungen § 8 WEG, Teilungserklaerung, Aufteilungsplan, Gemeinschaftsordnung. Pruefraster und Hinweise fuer den Notar. |

## Arbeitsweg

Im Plugin Immobilienrechtspraxis gilt für **Case Management Grundbuchanalyse Immo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `case-management`

**Fokus:** Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output: Case-Management-Übersicht Immobilienrecht. Abgrenzung: nicht Einzelvertragsprüfung.

# Case Management Immobilienrecht

## Fachkern: Case Management Immobilienrecht
- **Spezialgegenstand:** Case Management Immobilienrecht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Eine Rechtsabteilung verliert mehr Zeit mit Suchen und
Status-Reproduktion als mit der eigentlichen rechtlichen Arbeit. Der
Skill konsolidiert pro Fall den aktuellen Stand auf einer Seite,
führt einen Fristenkalender und eine Ereignistabelle und schreibt
beides bei jedem neuen Eingang fort.

## Inputs

- Aktenbestandteile in beliebiger Form: Verträge Schriftsätze
 Korrespondenz Gutachten Fotos Hausverwaltungs-Berichte
- Optional: bestehende Fallübersicht zur Fortschreibung
- Optional: Recherche-Auftrag für aktuelle Rechtsprechung

## Output je Fall

- `Fall_<Aktenzeichen>.md` — eine Seite Fallübersicht mit
 - Beteiligte (Mandant Gegenseite Vertreter Gericht)
 - Streitgegenstand und Streitwert
 - Aktueller Verfahrensstand
 - Nächste Schritte mit Verantwortlichem
 - Risiko-Ampel
- `Fristen_<Aktenzeichen>.md` — Tabelle Frist — Datum —
 Rechtsgrundlage — Status
- `Ereignisse_<Aktenzeichen>.md` — chronologische Tabelle aller
 Vorgänge mit Quellenverweis auf Aktenstelle
- Optional `Rechtsprechung_<Aktenzeichen>.md` — kuratierte
 BGH-Entscheidungen zum Fall mit Pinpoint-Zitat und
 Risiko-Einordnung

## Methodik

1. Eingangsdokument klassifizieren (Schreiben Vertrag Schriftsatz
 Urteil Gutachten Foto)
2. Tatsachen extrahieren mit Quellenangabe in eckigen Klammern
3. Fristen und Termine berechnen — gesetzliche Fristen aus
 Vorschrift abgeleitet, gerichtliche aus Verfügung
4. Risiko-Ampel pro Fall: GRUEN beherrschbar, GELB beobachten,
 ROT Eskalation
5. Bei Nachlieferung: bestehende Markdown-Dateien werden ergänzt,
 neue Einträge mit `[NEU]` markiert
6. Auf Wunsch: aktuelle Rechtsprechung recherchieren und mit
 Pinpoint-Zitierung anhängen (juengere zuerst Randnummer)

## Zusammenfassung umfangreicher Dokumente

Der Skill kann lange Schriftsätze Gutachten und Urteile
zusammenfassen. Format pro Dokument:

- Kernaussage in zwei Sätzen
- Relevante Tatsachen mit Quellenangabe (Randnummer Seite)
- Rechtliche Würdigung in Stichpunkten
- Bezug zum eigenen Fall mit Ampel

Bei Urteilen wird die Pinpoint-Zitierung sauber gesetzt — Gericht
Datum Aktenzeichen Fundstelle Randnummer.

## Rechtsprechungs-Recherche mit Risiko-Einordnung

Auf Anfrage sucht der Skill aktuelle Rechtsprechung zum
Streitgegenstand. Format pro Entscheidung:

- BGH oder OLG mit Datum Aktenzeichen Fundstelle Randnummer
- Sachverhalts-Kern in zwei Sätzen
- Rechtssatz wortgetreu mit Anführungszeichen und Randnummer
- Bezug zum eigenen Fall — staerkt oder schwaecht die eigene
 Position
- Ampel ROT GELB GRUEN aus Sicht des Mandanten

Halluzinations-Regel: nur Entscheidungen die existieren und mit
verifizierbarer Fundstelle vorliegen. Bei Unsicherheit Markierung
`[Quelle zu verifizieren]`.

## Typische Fristen im Immobilienrecht

- Widerspruch Eigenbedarfskündigung § 574b BGB — spätestens zwei
 Monate vor Beendigung
- Mieterhöhungsverlangen § 558b BGB — Zustimmungsfrist zwei
 Monate
- Schönheitsreparaturen-Endabrechnung — Abrechnung der
 Betriebskosten § 556 Abs. 3 BGB binnen zwölf Monaten
- Mietkautionsrückforderung — angemessene Prüfungsfrist nach
 Auszug
- Anfechtung WEG-Beschluss § 45 WEG — ein Monat ab Beschlussfassung
- Schriftform Gewerbemietvertrag § 550 BGB bei Nachtraegen
- Verjährung Mietminderung § 548 BGB — sechs Monate nach
 Rückgabe der Mietsache
- Auskunftsverlangen Mietpreisbremse § 556g Abs. 3 BGB

## Beispielformulierungen

- "Lege Fall Mueller gegen Hausverwaltung Berlin an. Hier sind
 alle Unterlagen."
- "Schreibe Fall ABC GmbH gegen XY fort. Hier ist die neue
 Klageerwiderung."
- "Recherchiere aktuelle BGH-Rechtsprechung zu Schimmel und
 Beweislast. Ordne jede Entscheidung mit Ampel ein."
- "Fasse das 80-Seiten-Gutachten in einer Seite zusammen mit
 Bezug zum Fall."

## Aktuelle Rechtsprechung — Leitsaetze fuer Case-Management

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 45 WEG: Anfechtungsklage muss innerhalb eines Monats ab Beschlussfassung erhoben und innerhalb zweier Monate ab Beschlussfassung begruendet werden; beide Fristen sind materiell-rechtliche Ausschlussfristen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Relevante Fristen im Immobilienrecht

| Frist | Norm | Dauer |
|-------|------|-------|
| WEG-Beschlussanfechtung | § 45 WEG | 1 Monat ab Beschlussfassung |
| Betriebskosten-Einwendung | § 556 Abs. 3 Satz 5 BGB | 12 Monate nach Zugang |
| Vorkaufsrecht Gemeinde | §§ 24 ff. BauGB | 2 Monate nach Mitteilung |
| Mietkaution-Abrechnung | § 551 Abs. 3 BGB | Ca. 6 Monate nach Auszug |
| Verjaehrung Mietforderung | §§ 195, 199 BGB | 3 Jahre ab Jahresende |

<!-- AUDIT 27.05.2026 — Bundle 033 —
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

## 2. `grundbuchanalyse`

**Fokus:** Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Prüfraster: Abteilung I bis III, Widersprueche, Rangverhältnisse, Löschungsansprüche. Output: Grundbuchanalyse-Bericht mit Handlungsempfehlung. Abgrenzung: nicht Kaufvertragsprüfung.

# Grundbuchanalyse

## Fachkern: Grundbuchanalyse
- **Spezialgegenstand:** Grundbuchanalyse wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Leitidee

Grundbuchdaten kommen in der Praxis als Stapel von PDF-Auszügen, oft
gescannt, mit dazwischengewürfelten Baulastenverzeichnissen, Flurkarten
und Altlastenausweisen. Der Skill normalisiert alles auf eine
Objekttabelle und ein einheitliches Risikoschema.

## Inputs

- Grundbuchauszüge (.pdf, gescannt oder digital)
- Optional: Baulastenverzeichnis-Ausdrucke
- Optional: Altlastenkataster-Auskuenfte
- Optional: Flurkarten und Lageprüfungen
- Objektliste als .xlsx oder .csv

## Methodik

1. OCR auf gescannten PDFs
2. Pro Auszug Identifikation Bestandsverzeichnis Abteilung I II III
3. Strukturierte Extraktion:
 - Bestandsverzeichnis: Gemarkung Flur Flurstück Wirtschaftsart
 Größe
 - Abteilung I: Eigentümerkette mit Erwerbsgrund
 - Abteilung II: Lasten und Beschraenkungen (Dienstbarkeiten
 Reallasten Vorkaufsrechte Nacherbenvermerk Sanierungsvermerk)
 - Abteilung III: Grundpfandrechte mit Rang Betrag Gläubiger
 Löschungserleichterung Brieftyp
4. Querverweis mit Baulastenverzeichnis (Baulasten existieren NICHT
 im Grundbuch)
5. Risikobewertung pro Objekt und Aggregation auf Portfolio
6. Generierung Risikomatrix Excel-Tabelle und Memo

## Output

- `Grundbuch_Portfolio.xlsx` — eine Zeile pro Flurstück, Spalten je
 Risikofeld
- `Risikomatrix.md` mit Ampel pro Objekt und Aggregat-Statistik
- `Auffaelligkeiten.md` — Objekte mit ungewöhnlichen Vermerken
 (Insolvenzvermerk Zwangsversteigerungsvermerk Nacherbenvermerk
 Sanierungsvermerk § 144 BauGB Vorkaufsrecht nach BauGB)

## Typische Risikofelder

- Briefgrundschuld ohne Löschungsbewilligung
- Rangverhältnis Abteilung III nicht eindeutig
- Dienstbarkeit zugunsten unbekannter Dritter (Leitungsrechte
 Wegerechte)
- Vorkaufsrecht der Gemeinde nach §§ 24 ff. BauGB
- Sanierungsvermerk § 144 BauGB — Genehmigung erforderlich
- Nacherbenvermerk § 2113 BGB
- Insolvenz- oder Zwangsversteigerungsvermerk
- Baulast nicht im Grundbuch aber gegen Eigentümer wirksam
- Altlastenverdachtsfläche und mietminderungsrelevante Schadstoffe

## Beispielformulierungen

- "Werte alle Grundbuchauszüge aus diesem Ordner aus. Erzeuge
 Portfoliosicht und markiere Objekte mit Sanierungsvermerk."
- "Ich habe 87 PDF-Auszüge. Zeig mir Objekte mit offenen
 Briefgrundschulden und Baulasten."
- "Prüfe diese 15 Objekte auf Vorkaufsrechte der Gemeinde nach
 Paragraph 24 BauGB."

## Relevante Normen

| Norm | Inhalt |
|------|--------|
| §§ 873, 877, 885 BGB | Grundbucheintragung als Entstehungsvoraussetzung dinglicher Rechte |
| §§ 892, 893 BGB | Oeffentlicher Glaube des Grundbuchs — gutglaeubiger Erwerb |
| § 883 BGB | Auflassungsvormerkung — schuetzt Eigentuemsverschaffungsanspruch |
| § 1113 ff. BGB | Hypothek und Grundschuld — Unterschied pruefen |
| § 1192 BGB | Briefgrundschuld — Loeschungsbewilligung + Grundschuldbrief erforderlich |
| §§ 24 ff. BauGB | Gemeindliches Vorkaufsrecht — Ausnahmen pruefen |
| § 144 BauGB | Sanierungsvermerk — Genehmigungspflicht saemtlicher Verfuegungen |
| § 2113 BGB | Nacherbenvermerk — eingeschraenkte Verfuegungsbefugnis des Vorerben |
| GBO | Grundbuchordnung — Verfahren und Eintragungsvoraussetzungen |

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- **BGH 15.04.2021, V ZB 175/20**: Grundbucheintragung — Bewilligung muss bestimmten Inhalt aufweisen; bei Auflassungsvormerkung Konkretisierung des gesicherten Anspruchs erforderlich. Quelle: dejure.org/2021,14528.
- **BGH 17.09.2021, V ZR 12/21**: WEMoG-Reform; Bauliche Veraenderungen § 20 WEG; Folgen fuer Grundbucheintragungen bei Sondernutzungsrechten. Quelle: dejure.org/2021,30989.
- **BGH 25.02.2016, V ZR 244/14**: Loeschungsfaehiges Grundpfandrecht — Voraussetzungen § 1183 BGB. Quelle: dejure.org/2016,5478.
- **BGH 07.07.2022, V ZB 21/22**: Notarielle Beurkundungsbefugnis ueber Grundstuecksgeschaefte gem. § 311b BGB. Quelle: dejure.org/2022,18504.

Konkrete Entscheidungen vor Ausgabe per dejure.org / bundesgerichtshof.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## — Schritt fuer Schritt

1. **Grundbuchauszuege anfordern** — aktuell (ggf. amtliches Datumsstempel pruefen); bei Portfolio: Grundbuchamts-CSV abrufen
2. **Abt. I — Eigentuemerkette** — Luecken im Eigentumsuebergang? Erbfolgenachweis (Erbschein/Erbvertrag) aktuell?
3. **Abt. II — Lasten und Beschraenkungen** — Vorkaufsrechte, Dienstbarkeiten, Nacherbenvermerk, Sanierungsvermerk?
4. **Abt. III — Grundpfandrechte** — Brief- oder Buchgrundschuld? Loeschungsbewilligung beschaffbar? Zession geprueft?
5. **Baulastenverzeichnis** — separat beim Baurechtsamt anfragen (NICHT im Grundbuch)
6. **Altlastenkataster** — Umweltamt; PFAS/BTEX-Belastung?
7. **Risikomatrix erzeugen** — Ampel je Risikofeld

## Adressat und Tonfall

- **Asset-Management**: praegnante Risikomatrix, Handlungsempfehlung pro Objekt
- **Finanzierung/Bank**: Sicherheitenwertanalyse, Rangfragen Abt. III
- **Gericht/Notar**: formell, mit Grundbuchblattnummer und Eintragungsdatum

## Grenzen

Der Skill ersetzt nicht die Pruefung durch einen Immobilienjuristen.
Er liefert Vorstrukturierung und Risiko-Heatmap, damit der Mensch
seine Zeit dort einsetzt, wo es wirklich brennt.

<!-- AUDIT 27.05.2026 — Bundle 033 —
 Kein gesicherter Ersatz verfügbar; Eintrag gelöscht. § 892 BGB bleibt als Normverweis erhalten.
-->

## 3. `immo-aufteilungsplan-weg`

**Fokus:** Aufteilungsplan WEG: Voraussetzungen § 8 WEG, Teilungserklaerung, Aufteilungsplan, Gemeinschaftsordnung. Pruefraster und Hinweise fuer den Notar.

# Aufteilungsplan WEG

## Fachkern: Aufteilungsplan WEG
- **Spezialgegenstand:** Aufteilungsplan WEG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
