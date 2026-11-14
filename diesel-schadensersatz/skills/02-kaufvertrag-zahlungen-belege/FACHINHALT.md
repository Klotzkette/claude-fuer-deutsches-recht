---
name: 02-kaufvertrag-zahlungen-belege
description: "Für unklare Kauf-, Finanzierungs-, Leasing-, Zahlungs-, Kilometer- oder Anlagenbelege. Rekonstruiert die beleggebundene Erwerbs- und Zahlungslage. Nicht für Anspruchswahl oder Schriftsatzproduktion."
---

# Kaufvertrag, Zahlungen und Belege

## Zweck und Anwendungsfall

Dieser Skill baut das wirtschaftliche Fundament des Falls: Er rekonstruiert Kaufvertrag mit Anlagen, Finanzierungs- oder Leasingvertrag und den vollständigen Zahlungsverlauf, erfasst Kilometerstände und Restwert und ordnet jedem späteren Schadensposten einen Beleg-Anker zu. Ergebnis ist die Belegmatrix, aus der Anspruchsschreiben (Skill 09) und Klage (Skills 14, 15) ihre Anlagen K1 bis Kn ziehen.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst den beleggebundenen Erwerbs- und Zahlungsbefund mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei ergebnisrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern, sonst vollständige Absätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort liefert sofort einen vorläufigen, aber vollständig ausformulierten Erwerbs- und Zahlungsbefund: belegte Vertragsparteien, Kaufpreis, Zahlungs- oder Finanzierungsverlauf, datierte Kilometerstände, vorläufiges Anlagenverzeichnis K1 bis Kn, Konflikte und eine präzise Lückenliste. Jede Lücke nennt den fehlenden Wert oder Beleg, den Beschaffungsweg und die Auswirkung auf Anspruch oder Rechnung. Ab mindestens drei Belegen, Zahlungsereignissen oder wiederkehrenden Feldern werden die Angaben tabellarisch verglichen; sonst genügen vollständige Absätze oder eine kurze Liste. Leere Tabellenzeilen sind unzulässig.

Verboten in der ersten Antwort: Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen. Python-Werkzeuge sind Beschleuniger: Sind sie nicht verfügbar oder schlagen sie fehl, läuft die Rekonstruktion ohne Meldungslärm manuell weiter; ein Werkzeugfehler blockiert nie die Aktenaufnahme oder den Entwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Kaufakte aus Skill 01 (Stammdaten, Inventar).
- Kaufvertrag, Rechnung, Übergabeprotokoll, Fahrzeugpapiere.
- Finanzierungs- oder Leasingvertrag, Tilgungsplan, Kontoauszüge, Ablösebescheinigung.
- Kilometerstandsnachweise (Werkstattrechnung, TÜV-Bericht, Foto mit Datum).

## Ablauf / Checkliste

1. Vertragskette prüfen: Käufer, Verkäufer (Händler oder privat), Hersteller, finanzierende Bank oder Leasinggeber; Neuwagen- oder Gebrauchtkauf mit Händlerkette dokumentieren.
2. Kaufpreis, Anzahlung, Raten und Sondertilgungen chronologisch erfassen; jede Zahl mit Quelle, Belegdatum und Sicherheit.
3. Abweichungen zwischen Kaufvertrag, Rechnung und Kontoauszug nicht glätten, sondern als Konfliktzeile ausweisen.
4. Kilometerstandsjournal führen: Datum, Kilometerstand, Quelle, Beleg — Grundlage der Nutzungsentschädigung in Skill 08.
5. Bei Finanzierung: verbundenes Geschäft und Widerrufsinformation vormerken und an Skill `12-finanzierungswiderruf-verbundgeschaeft` melden; die Spur läuft getrennt vom Deliktsanspruch.
6. Belegmatrix aufbauen: Für jede Tatsache den konkreten Beleg samt Fundstelle, die Anlagenummer, die Quellenrolle, die Sicherheit und entweder „keine Lücke“ oder eine präzise Beleglücke mit Beschaffungsweg nennen. Bei mindestens drei Belegen oder wiederkehrenden Feldern diese Angaben in den Spalten `Tatsache`, `Beleg und Fundstelle`, `Anlage`, `Quellenrolle`, `Sicherheit` und `Lücke mit Beschaffungsweg` vergleichen; bei weniger Einträgen vollständig ausformulieren. Keine leeren Zeilen erzeugen.

7. Anlagenverzeichnis K1 bis Kn nummerieren; fehlende Pflichtbelege in die Lückenliste mit Beschaffungsweg.
8. Ampel setzen und übergeben: Zahlenwerk an Skill `08-schadenshoehe-nutzungsentschaedigung`, Chronologie-Ereignisse an Skill `03-chronologie-rueckruf-fristen`.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Vertrag, Zahlung und Erwerb so rekonstruieren, dass Anspruch, Aktivlegitimation und Schadensrechnung auf Primärbelegen statt auf Zusammenfassungen beruhen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Vertragspartei, Kaufpreis, Zahlungsfluss, Eigentums- und Finanzierungsstatus sind belegt oder ausdrücklich offen.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Der Schaden liegt im ungewollten Vertragsschluss; Vertragsdatum, Vertragsparteien und Kilometerstände tragen Anspruch und Nutzungsrechnung. | Bestätigt |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19; Urt. v. 09.04.2024 - VI ZR 660/20 | Gebrauchtwagenkauf schließt Ansprüche nicht aus; die Händlerkette ist zu dokumentieren. | Bestätigt |
| EuGH, Urt. v. 14.07.2022 - C-145/20 | Eine verbotene Abschalteinrichtung kann einen kaufrechtlichen Mangel begründen, der nicht allein wegen bestehender Typgenehmigung als geringfügig gilt; Verkäufer- und Herstelleransprüche strikt trennen. | Amtlich geprüft |
| BGH, Urt. v. 08.12.2021 - VIII ZR 190/19; Beschl. v. 13.12.2022 - VIII ZR 298/21 | Für die Verkäuferspur sind gewählte Nacherfüllung, Aufforderungen, Fristen und Update-Angebote vollständig zu belegen; die Entscheidungen tragen keinen pauschalen merkantilen Minderwert. | Amtlich geprüft |
| EuGH, Urt. v. 17.12.2020 - C-693/18 | Die Software-Funktionsweise ist zentrales Beweisthema; Rückrufschreiben und Update-Nachweise gehören priorisiert in die Belegmatrix. | Bestätigt |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

Baustein 1 — Beleganforderung an das Autohaus (Zweitschriften der Kaufunterlagen):

„Sehr geehrte Damen und Herren, zu dem Kaufvertrag über das Fahrzeug [Hersteller und Modell] mit der Fahrzeug-Identifizierungsnummer [FIN], geschlossen am [Datum TT.MM.JJJJ], bitten wir um Übersendung einer Zweitschrift des vollständigen Kaufvertrags einschließlich aller Anlagen, der Rechnung sowie des Übergabeprotokolls mit dem bei Übergabe dokumentierten Kilometerstand. Der Anspruch auf Vorlage und Zweitschrift folgt aus § 810 BGB sowie aus der nachvertraglichen Nebenpflicht gemäß § 242 BGB. Wir bitten um Zugang der Unterlagen bis zum [Datum TT.MM.JJJJ]."

Baustein 2 — Beleganforderung an die finanzierende Bank:

„Sehr geehrte Damen und Herren, zu dem Darlehensvertrag Nr. [Vertragsnummer] über die Finanzierung des Fahrzeugs mit der FIN [FIN] bitten wir um Übersendung einer Kopie des Darlehensvertrags einschließlich der Widerrufsinformation, des vollständigen Tilgungsplans, einer Aufstellung sämtlicher geleisteter Zahlungen sowie — soweit vorhanden — der Ablösebescheinigung. Soweit personenbezogene Daten betroffen sind, stützen wir das Verlangen zugleich auf Art. 15 DSGVO; die Auskunft ist danach unentgeltlich zu erteilen. Wir bitten um Erledigung bis zum [Datum TT.MM.JJJJ]."

Baustein 3 — Konfliktzeilen-Ergebnissatz für die Belegmatrix:

„Der Kaufpreis ist im Kaufvertrag vom [Datum TT.MM.JJJJ] mit [Betrag in EUR] ausgewiesen, während der Kontoauszug vom [Datum TT.MM.JJJJ] lediglich eine Zahlung von [Betrag in EUR] belegt; die Differenz von [Betrag in EUR] wird als offene Konfliktzeile geführt und nicht geglättet, bis [fehlender Beleg, zum Beispiel Quittung über die Baranzahlung] vorliegt."

### Rechenbeispiel: Zahlungsabgleich und Nutzungsvorschau

Ausgangswerte: Kaufpreis laut Kaufvertrag 32.500,00 EUR; Anzahlung 6.500,00 EUR; Finanzierung mit 48 Monatsraten zu je 420,00 EUR und einer Schlussrate von 8.900,00 EUR; Kilometerstand bei Übergabe 20.000 km, aktueller Kilometerstand 118.400 km.

1. Zahlungsabgleich

   Anzahlung 6.500,00 EUR plus 48 Raten mal 420,00 EUR gleich 20.160,00 EUR plus Schlussrate 8.900,00 EUR ergibt eine gezahlte Gesamtsumme von 35.560,00 EUR. Die Differenz zum Kaufpreis von 32.500,00 EUR beträgt 3.060,00 EUR und ist als Finanzierungskostenanteil (Zinsen und Kosten) gesondert auszuweisen; sie erhöht nicht den Kaufpreis, kann aber als eigener Finanzierungsschaden eine Position der Schadensrechnung sein.

2. Nutzungsvorschau für Skill 08

   Gefahrene Strecke: 118.400 km minus 20.000 km gleich 98.400 km. Erwartete Restlaufleistung beim Kauf: 250.000 km minus 20.000 km gleich 230.000 km. Nutzungsentschädigung nach der Formel Kaufpreis mal gefahrene Kilometer geteilt durch erwartete Restlaufleistung beim Kauf: 32.500,00 EUR mal 98.400 km geteilt durch 230.000 km gleich 13.904,35 EUR. In der 300.000-km-Variante beträgt die Restlaufleistung 280.000 km und die Nutzungsentschädigung 11.421,43 EUR.

Ergebnis-Satz: Auf Basis der belegten Zahlen liegt der vorläufige Nutzungsvorteil zwischen 11.421,43 EUR und 13.904,35 EUR; die verbindliche Rechnung mit tagesaktuellem Kilometerstand führt Skill `08-schadenshoehe-nutzungsentschaedigung`.

### Beleg-Beweiswert-Tabelle

| Beleg | Beweiswert | Bemerkung |
| --- | --- | --- |
| Kaufvertrag im Original mit Unterschriften | hoch (Privaturkunde, § 416 ZPO) | trägt Vertragsparteien, Kaufpreis und Vertragsdatum |
| Rechnung des Autohauses | hoch | trägt Kaufpreis und Fahrzeugidentität, ersetzt aber nicht den Vertrag |
| Kontoauszug oder Überweisungsbeleg | hoch | trägt den tatsächlichen Zahlungsfluss; Abweichungen als Konfliktzeile |
| Tilgungsplan und Bankbestätigung | hoch | trägt Raten, Zinsanteil und Ablösung |
| Übergabeprotokoll, TÜV-Bericht, Werkstattrechnung | mittel bis hoch | trägt datierte Kilometerstände für das Kilometerjournal |
| Tachofoto mit Datumsnachweis | mittel | Indiz, möglichst mit weiterem Beleg koppeln |
| Eigene Erklärung der Geschädigten | niedrig | Parteivortrag, nur als Lückenfüller mit Beschaffungsauftrag |

### Entscheidungstabelle

| Wenn (Befund) | Dann (Pfad) | Begründung | Nächster Skill |
| --- | --- | --- | --- |
| Kaufvertrag, Rechnung und Zahlungsnachweis vollständig und widerspruchsfrei | Ampel grün, Zahlenwerk freigeben | Primärbelege tragen Anspruch und Schadensrechnung | 08 |
| Kaufpreis belegt, Kilometerstände lückenhaft | Ampel gelb, Kilometerjournal aus TÜV- und Werkstattbelegen ergänzen | ohne Kilometerkette keine belastbare Nutzungsrechnung | 08 mit Vorbehalt |
| Finanzierungsvertrag mit Widerrufsinformation vorhanden | Widerrufsspur getrennt vormerken | verbundenes Geschäft läuft neben dem Deliktsanspruch | 12 |
| Beleg fehlt vollständig, nur Parteivortrag | Ampel rot, Baustein 1 oder 2 mit Frist versenden | Endprodukte dürfen nicht auf unbelegten Zahlen aufbauen | 02 (Wiedervorlage) |
| Kaufvertrag und Kontoauszug widersprechen sich | Konfliktzeile nach Baustein 3 ausweisen, nicht glätten | Glättung zerstört die Auditierbarkeit der Matrix | Eskalation an Anwältin oder Anwalt |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Beträge nur aus Kaufvertrag, Rechnung, Finanzierung und Kontoauszug bilden; Rechtsprechung nur aus `references/gepruefte-anker-dieselgate.md`. Keine erfundenen Aktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Anlagenverzeichnis sowie beleggebundener Zahlungs-, Nutzungs- und Konfliktbefund in vollständig ausformulierten Sätzen. Ab mindestens drei Belegen, Zahlungsereignissen oder wiederkehrenden Feldern wird eine ausgefüllte Belegmatrix verwendet; sonst werden dieselben Angaben in Absätzen oder einer kurzen Liste ausgegeben. Bloße Stichwortsammlungen und leere Tabellenzeilen sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Neuwagenkauf 2014 mit Bankfinanzierung, Tilgungsplan und Kontoauszüge liegen vor. Kernbefund: Zahlungsverlauf vollständig rekonstruierbar, Widerrufsinformation vorhanden. Erste Antwort: vollständige Belegmatrix mit Anlagenverzeichnis K1 bis K7, Zahlungsabgleich nach dem Rechenbeispiel und Meldung der Widerrufsspur an Skill 12.
- Eingang: Gebrauchtkauf mit zwei Vorbesitzern, nur Kaufvertrag und zwei TÜV-Berichte vorhanden. Kernbefund: Händlerkette belegt, Kilometerjournal zwischen Erstzulassung und Kauf lückenhaft. Erste Antwort: Belegmatrix mit gelber Ampel, Kilometerjournal aus den TÜV-Berichten und Lückenliste mit Beschaffungsweg Werkstatthistorie.
- Eingang: Rechnung fehlt, die Käuferin erinnert eine Baranzahlung ohne Quittung. Kernbefund: Kaufpreis nur durch Parteivortrag gedeckt, rote Konfliktzeile. Erste Antwort: Beleganforderung an das Autohaus nach Baustein 1 mit Frist [Datum TT.MM.JJJJ] und Belegmatrix mit markierten Platzhaltern.
