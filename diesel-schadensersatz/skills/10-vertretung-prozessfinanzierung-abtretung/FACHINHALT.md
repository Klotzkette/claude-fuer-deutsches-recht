---
name: 10-vertretung-prozessfinanzierung-abtretung
description: "Für Anwaltszwang, RDG, Rechtsschutz, Prozessfinanzierung, Abtretung oder Kanzleiübergabe. Klärt Rolle, Vollmacht, Kostenmodell und Datenschutz. Nicht für die materielle Anspruchswahl."
---

# Vertretung, Prozessfinanzierung und Abtretung

## Zweck und Anwendungsfall

Dieser Skill klärt, wer den Fall führt und wer ihn bezahlt. Klagen auf großen Schadensersatz gehen wegen des Streitwerts meist an das Landgericht (§ 71 GVG) — dort gilt Anwaltszwang (§ 78 Abs. 1 ZPO); Differenzschaden-Klagen liegen nach aktuellem § 23 Nr. 1 GVG bis einschließlich 10.000 EUR oft beim Amtsgericht ohne Anwaltszwang. Der Skill prüft die Vertretungsoptionen (eigene Kanzlei, Verbraucherschutz im RDG-Rahmen, Legal-Tech per Abtretung), die Finanzierung (Rechtsschutzversicherung, Prozessfinanzierer, Eigenfinanzierung) und baut das Übergabepaket, mit dem eine Kanzlei oder ein Finanzierer sofort entscheiden kann.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort die begründete Vertretungs- und Finanzierungsentscheidung mit Ampel und, je nach Ergebnis, den ausformulierten Entwurf der Deckungsanfrage oder des Übergabeschreibens; fehlende Angaben stehen als präzise Platzhalter im Entwurf. Nur wenn mindestens drei Optionen oder wiederkehrende Entscheidungsfelder verglichen werden, wird die Begründung zusätzlich als Vertretungsweichen-Tabelle dargestellt. Verboten sind Theorie-Vorträge, Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen; keine Rückfrage, wenn ein Entwurf mit Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Bei Ausfall wird ohne Meldungslärm manuell weitergearbeitet; ein Werkzeugfehler blockiert nie Entscheidung oder Entwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Strategiekarte aus Skill 06 (Spur, Streitwert, Erfolgsaussicht, Kostenrisiko).
- Rolle der Geschädigten: vertreten oder unvertreten, Rechtsschutzversicherung vorhanden, Vorsteuerabzug.
- Bei Legal-Tech: Abtretungsvertrag, Quote, AGB, Datenschutzunterlagen.

## Ablauf / Checkliste

1. Rechtsweg nach aktuellem § 23 Nr. 1 GVG feststellen: Bis einschließlich 10.000 EUR ist grundsätzlich das Amtsgericht, darüber grundsätzlich das Landgericht zuständig; Übergangsrecht und besondere Zuweisungen live prüfen. Vor dem Landgericht gilt Anwaltszwang (§ 78 ZPO), vor dem Amtsgericht grundsätzlich nicht.
2. RDG-Grenzen prüfen: Was dürfen Verbraucherschutz und nicht-anwaltliche Berater (Aufklärung, Strukturierung), was nicht (Individualvertretung vor dem Landgericht)? Grenzverletzungen offen benennen.
3. Rechtsschutzversicherung: Versicherungsschein und vollständige Bedingungsfassung, versichertes Fahrzeug/Fahrzeuggruppe, Erwerbs- und Zulassungsdatum, Versicherungsfall, zeitliche Deckung, Wartezeit, Risikoausschlüsse und Obliegenheiten prüfen. Deckungsanfrage mit Sachverhalt, Anspruchsgegner, Streitwert, technischer Beleglage und aktueller Aufzehrungsrechnung formulieren. `IV ZR 30/25` behandelt den Erwerb als Versicherungsfall des deliktischen Erwerbsschadens und legt konkrete Vorsorge-/Ersatzfahrzeugklauseln aus; daraus folgt keine pauschale Deckung für andere Bedingungen. Ablehnungsdatum, damalige höchstrichterliche Lage und Stichentscheid getrennt bewerten.
4. Prozessfinanzierer: nicht nur Bruttoquote, sondern Differenzschaden nach Nutzung-/Restwertausgleich, Gutachtenrisiko und Kosten über zwei Instanzen darstellen; Kostenteilung, Erlösquote, Vergleichs- und Steuerungsrechte offenlegen.
5. Legal-Tech-Abtretung prüfen: Bestimmtheit der Abtretung (welcher Anspruch, welches Fahrzeug), RDG-Erlaubnis des Anbieters, Quote und Nebenkosten, Datenschutz (Weitergabe nur mit wirksamer Abtretung oder Vollmacht), Kontrollverlust ehrlich gegen Bequemlichkeit abwägen.
6. Eskalationstrigger beachten: Berufung, Revision, Sachverständigenstreit, hoher Streitwert, unklare Abtretung — dann zwingend anwaltliche Übernahme.
7. Übergabepaket bauen: Startkarte, Kaufakte, Betroffenheitsmatrix, Schadenstabelle, Chronologie, Fristenkarte, Beleg-Anlagen und konkreter Entscheidungsauftrag (zum Beispiel Deckungszusage einholen, Klage nach Spur A entwerfen); Export als E-Akte über Skill `20-eakte-export-kanzleisoftware`.
8. Entscheidung mit Ampel ausgeben und weiterrouten: Klageweg an Skill 13, kollektive Spur an Skill 11.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Vertretungsmacht, Abtretung, Vergütung, Finanzierung und Interessenkonflikte transparent einer zulässigen Route zuordnen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Kein Mandats- oder Finanzierungsmodell ohne belegte Rollen, Kostenfolge, Verfügungsbefugnis und anwaltliche Eskalationsgrenze.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Die gefestigte EA189-Linie macht die Erfolgsaussicht für Kanzlei, Versicherer und Prozessfinanzierer kalkulierbar. | Bestätigt |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Die Bruttoquote von 5 bis 15 Prozent ist nur Ausgangspunkt; Aufzehrung, Kosten und Beweisrisiko bestimmen den finanzierbaren Nettoerwartungswert. | Bestätigt |
| BGH, Beschl. v. 02.09.2025 - VIa ZR 87/24; Beschl. v. 16.12.2025 - VIa ZR 613/24 | Nutzungsvorteile und Restwert können den Differenzschaden vollständig aufzehren; Finanzierer und Versicherer brauchen die aktuelle Rechnung. | Amtlich geprüft |
| BGH, Urt. v. 05.06.2024 - IV ZR 140/23; Urt. v. 25.03.2026 - IV ZR 30/25 | Bei Rechtsschutzdeckung die bis zum maßgeblichen Entscheidungszeitpunkt fortentwickelte Erfolgsaussicht einbeziehen. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Deckungsanfrage an die Rechtsschutzversicherung:**

Versicherungsschein-Nummer [Nummer], Versicherungsnehmerin [Name], versichertes Fahrzeug [Hersteller, Modell, Kennzeichen].
Wir bitten um Deckungszusage für die außergerichtliche und die erstinstanzliche gerichtliche Geltendmachung von Schadensersatzansprüchen gegen [Name des Herstellers] wegen einer unzulässigen Abschalteinrichtung in dem Fahrzeug mit der FIN [FIN], erworben am [Datum TT.MM.JJJJ] zum Kaufpreis von [Betrag in EUR]. Der Versicherungsfall liegt in dem Erwerb des betroffenen Fahrzeugs; die zeitliche Deckung nach der Bedingungsfassung [ARB-Fassung, Stand] bitten wir zu prüfen.
Geltend gemacht wird [großer Schadensersatz in Höhe von [Betrag in EUR], Zug um Zug gegen Rückgabe des Fahrzeugs / ein Differenzschaden in Höhe von [Betrag in EUR]]; der Streitwert beträgt [Betrag in EUR]. Die Erfolgsaussicht stützt sich auf die gefestigte höchstrichterliche Rechtsprechung; die Betroffenheit ist durch [KBA-Rückruf / Herstellerschreiben] belegt, eine aktuelle Aufzehrungsrechnung ist beigefügt.
Wir bitten um Deckungszusage bis zum [Datum TT.MM.JJJJ]; im Ablehnungsfall bitten wir um Mitteilung der Gründe und weisen auf die Möglichkeit des Stichentscheids nach den Versicherungsbedingungen hin.

**Baustein 2 — Übergabeschreiben an die Kanzlei:**

Sehr geehrte Frau Rechtsanwältin, sehr geehrter Herr Rechtsanwalt, in Sachen [Name der Geschädigten] gegen [Name des Herstellers] zu dem Kaufvertrag über das Fahrzeug mit der FIN [FIN] übergeben wir den Fall zur anwaltlichen Übernahme. Beigefügt sind Startkarte, Kaufakte mit Belegen, Betroffenheitsmatrix, Schadenstabelle mit Stichtag, Chronologie mit Fristenkarte und das Anlagenverzeichnis.
Der Entscheidungsauftrag lautet: [z. B. Deckungszusage einholen und Klage nach der empfohlenen Spur entwerfen]. Fristkritisch ist [drohende Verjährung zum Datum TT.MM.JJJJ / gesetzte Frist aus dem Anspruchsschreiben]. Die Geschädigte ist [rechtsschutzversichert bei [Versicherer], Deckungsanfrage anbei / nicht rechtsschutzversichert; Prozessfinanzierung ist zu prüfen]. Um Eingangsbestätigung und Übernahmeentscheidung bis zum [Datum TT.MM.JJJJ] wird gebeten.

**Baustein 3 — Aufklärung vor einer Legal-Tech-Abtretung:**

Mit der Abtretung geht die Forderung auf den Anbieter über; die Geschädigte verliert die Steuerung über Klageerhebung, Vergleichsabschluss und Rücknahme. Die Erfolgsquote von [Zahl] Prozent wird vom tatsächlich erzielten Erlös berechnet; hinzu kommen gegebenenfalls [Nebenkosten]. Die Abtretung muss den Anspruch und das Fahrzeug bestimmt bezeichnen, der Anbieter muss über eine Registrierung nach dem RDG verfügen, und die Weitergabe personenbezogener Daten ist nur auf Grundlage einer wirksamen Abtretung oder Vollmacht zulässig. Diese Punkte sind vor der Unterschrift zu prüfen; die Bequemlichkeit des Modells ist offen gegen den Kontrollverlust und die Quote abzuwägen.

### Rechenbeispiel: Finanzierungsvergleich

Grundlage ist der große Schadensersatz aus Skill 08 mit 19.708,00 EUR (Kaufpreis 32.500,00 EUR abzüglich Nutzungsentschädigung 12.792,00 EUR). Weg 1, Legal-Tech-Abtretung mit 35-Prozent-Erfolgsquote: Abzug 19.708,00 EUR mal 0,35 gleich 6.897,80 EUR; Auszahlung bei Erfolg 12.810,20 EUR, dafür kein eigenes Kostenrisiko.
Weg 2, eigene Klage mit Rechtsschutzdeckung und Selbstbeteiligung von 300,00 EUR: erwartete Auszahlung bei Erfolg 19.408,00 EUR. Weg 3, eigene Klage ohne Deckung: volle Auszahlung bei Erfolg, aber das Kostenrisiko über zwei Instanzen ist vor der Entscheidung konkret nach RVG und GKG zu beziffern und der Erfolgswahrscheinlichkeit gegenüberzustellen.
Ergebnis-Satz: Bei bestehender Rechtsschutzversicherung ist die Deckungsanfrage wirtschaftlich vorrangig, weil Weg 2 im Erfolgsfall 6.597,80 EUR mehr erwarten lässt als die Abtretung; die Abtretung bleibt die Rückfalloption für risikoscheue Geschädigte ohne Deckung.

### Entscheidungstabelle: Vertretungsweiche

| Befund | Rechtsfolge / Pfad | Begründung | Nächster Skill |
| --- | --- | --- | --- |
| Streitwert über 10.000 EUR, Rechtsschutzversicherung vorhanden | anwaltliche Vertretung zwingend; Deckungsanfrage nach Baustein 1 sofort stellen | § 71 GVG, § 78 Abs. 1 ZPO; Deckung klärt das Kostenrisiko vor Mandatierung | 13 |
| Streitwert über 10.000 EUR, keine Rechtsschutzversicherung | anwaltliche Vertretung zwingend; Prozessfinanzierer oder Legal-Tech-Abtretung nach Rechenbeispiel vergleichen | Anwaltszwang am Landgericht; Nettoerwartungswert entscheidet | 13, kollektive Spur 11 |
| Streitwert bis einschließlich 10.000 EUR, Rechtsschutzversicherung vorhanden | Amtsgericht ohne Anwaltszwang; anwaltliche Vertretung gleichwohl empfohlen, Deckung anfragen | § 23 Nr. 1 GVG; Waffengleichheit gegen die Herstellerkanzlei | 13 |
| Streitwert bis einschließlich 10.000 EUR, keine Rechtsschutzversicherung | Eigenvertretung möglich; Kostenrisiko und Aufzehrung vor Klage klein rechnen | kein Anwaltszwang am Amtsgericht; Wirtschaftlichkeit dominiert | 13, sonst zurück an 06 |
| Legal-Tech-Abtretung erwogen | Bestimmtheit, RDG-Registrierung, Quote und Datenschutz prüfen; Aufklärung nach Baustein 3 | Kontrollverlust und Quote gegen Bequemlichkeit abwägen | 10 Ablauf 5 |
| Verbraucherschutz soll vor dem Landgericht vertreten | RDG-Grenze; anwaltliche Übernahme mit Übergabepaket nach Baustein 2 | Individualvertretung vor dem Landgericht ist nicht-anwaltlichen Beratern verwehrt | 20, dann Kanzlei |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Erlaubnis- und Zuständigkeitsaussagen mit aktuellem Normanker (§ 23 Nr. 1, § 71 GVG, § 78 ZPO, RDG); Rechtsschutz- und Dieselrechtsprechung aus `references/gepruefte-anker-dieselgate.md` und der Obergerichtsmatrix live verifizieren.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Vertretungs- und Finanzierungsentscheidung mit Normbegründung, Deckungsanfrage-Entwurf und Übergabepaket in vollständigen, ausformulierten Sätzen; Stichwort-Skelette sind als Endprodukt unzulässig.

## Beispiele

- Eingang: unvertretene Geschädigte mit Rechtsschutzversicherung, Streitwert 19.708,00 EUR. Kernbefund: Landgericht mit Anwaltszwang, Deckung erreichbar. Arbeitsprodukt der ersten Antwort: ausformulierte Deckungsanfrage nach Baustein 1 mit Platzhaltern für Versicherungsnummer und Bedingungsfassung plus Übergabeschreiben nach Baustein 2, Ampel grün.
- Eingang: Legal-Tech-Angebot mit 35-Prozent-Quote liegt auf dem Tisch. Kernbefund: Abtretung bestimmt, RDG-Registrierung belegt, aber Quote kostet 6.897,80 EUR vom erwartbaren Erlös. Arbeitsprodukt: Finanzierungsvergleich nach dem Rechenbeispiel mit Empfehlung und Aufklärung nach Baustein 3.
- Eingang: Verbraucherzentrale fragt nach Vertretung vor dem Landgericht. Kernbefund: RDG-Grenze verwehrt die Individualvertretung. Arbeitsprodukt: Vertretungsweichen-Tabelle mit begründeter Weiche zur anwaltlichen Übernahme und fertiges Übergabeschreiben nach Baustein 2.
