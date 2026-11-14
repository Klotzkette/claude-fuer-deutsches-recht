---
name: 11-musterfeststellung-vdug-kollektivklage
description: "Für Musterfeststellung, VDuG, Abhilfeklage oder kollektiven Rechtsschutz. Prüft Anmeldung, Bindung, Hemmung und Vor- oder Nachteile gegenüber der Einzelspur. Keine automatische Empfehlung einer Sammelspur."
---

# Musterfeststellung, VDuG und Kollektivklage

## Zweck und Anwendungsfall

Dieser Skill beantwortet die Frage: allein klagen oder kollektive Spur? Er ordnet die abgeschlossene Musterfeststellungsklage des vzbv gegen die Volkswagen AG ein (Bindungs- und Hemmungswirkung nur für wirksam Angemeldete), prüft die Abhilfeklage nach dem VDuG als heutige kollektive Spur und stellt beides der individuellen Schadensersatzklage gegenüber — mit ehrlicher Bewertung von Tempo, Kosten, Erlöshöhe und Kontrollverlust.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort eine vorläufige, aber vollständig ausformulierte Entscheidungsvorlage: Sie bewertet die kollektive und die individuelle Spur anhand der bekannten Falldaten, begründet die Ampel je Spur und empfiehlt den nächsten Schritt. Eine Tabelle wird nur bei mindestens drei vergleichbaren Kriterien eingesetzt. Als konkrete Lücken werden Hersteller, wirksame Anmeldung mit Datum sowie der live zu prüfende Registerstand mit Abrufdatum ausgewiesen (`[Hersteller]`, `[Anmeldedatum TT.MM.JJJJ]`, `[Registerstand mit Abrufdatum]`), nicht in einer Frageschleife abgearbeitet.

Verboten in der ersten Antwort: Theorie-Vorträge zu VDuG oder Musterfeststellung, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche, mehr als drei Rückfragen sowie jede Rückfrage, wenn ein vorläufiges Ergebnis mit klar markierten Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Ist ein Skript oder der Registerabruf nicht sofort verfügbar, wird ohne Meldungslärm manuell weitergearbeitet; ein Werkzeugfehler blockiert nie die Entscheidungsvorlage.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Strategiekarte aus Skill 06 und Fristenkarte aus Skill 07.
- Historie zur Musterfeststellungsklage: angemeldet, abgemeldet, Vergleich angenommen.
- Laufende oder angekündigte VDuG-Verfahren zum betroffenen Hersteller oder Motor, soweit bekannt.

## Ablauf / Checkliste

1. Historie und Normstand klären: Bei der alten VW-Musterfeststellung Anmeldung, Abmeldung und Vergleichsannahme für § 204 Abs. 1 Nr. 1a BGB a.F. erfassen. Für aktuelle Verfahren § 204a BGB, Art. 229 § 65 EGBGB und §§ 46, 47 VDuG anwenden. Verfahrensgegenstand, wirksame Anmeldung, Rücknahme und Registerbeleg tagesgenau prüfen; historische und aktuelle Regeln nicht vermischen.
2. Vergleichsannahme prüfen: Wer den damaligen Vergleich angenommen hat, hat regelmäßig keine offene Einzelspur mehr; Ausnahmen offen kennzeichnen und anwaltlich eskalieren.
3. VDuG-Spur prüfen: Existiert eine einschlägige Musterfeststellungs- oder Abhilfeklage für Hersteller, Fahrzeug und Lebenssachverhalt? Anmeldevoraussetzungen und Rücknahmefrist nach §§ 46, 47 VDuG sowie die Hemmung nach § 204a BGB dokumentieren; nichts behaupten, was das Verbandsklageregister nicht hergibt — live prüfen.
4. Kollektive Spur und Einzelklage nach Tempo, Kostenrisiko, erwartetem Nettoerlös, Kontrolle über den Fall und Verjährungswirkung vergleichen. Jedes Kriterium erhält einen fallbezogenen Befund und eine Beleg- oder Registerfundstelle; eine Tabelle nur verwenden, wenn mindestens drei Kriterien konkret befüllt werden können.
5. Empfehlung formulieren: fallbezogen, mit Grund und Risiko; kein Automatismus zugunsten einer Spur.
6. Routen: Einzelklage an Skill `13-klageweg-streitwert-zustaendigkeit`; Anmeldung zur kollektiven Spur als dokumentierter Schritt mit Fristenkarte an Skill 03.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Kollektiv- und Individualspur anhand konkreter Teilnahme-, Gleichartigkeits-, Frist- und Bindungswirkungen vergleichen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Keine Kollektivempfehlung ohne aktuellen Verfahrensstatus, konkrete Betroffenheit, Registerfolge und Individualalternative.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

- **Anker:** BGH, Urt. v. 27.01.2022 - VII ZR 303/20; Urt. v. 26.09.2022 - VIa ZR 124/22. Die historische Hemmung der VW-Musterfeststellung setzte eine wirksame Anmeldung und Verbrauchereigenschaft voraus; An- und Abmeldung sind tagesgenau zu prüfen. **Status:** Amtlich geprüft.
- **Anker:** Keine Dieselgate-Leitentscheidung einschlägig. Für aktuelle VDuG-Verfahren trägt keine Dieselgate-Leitentscheidung im Ankerkatalog; maßgeblich sind § 204a BGB, das VDuG und der live geprüfte Stand des Verbandsklageregisters. **Status:** Hinweis.

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine für den Beratungsvermerk

Baustein Empfehlung (Kernabsatz des Beratungsvermerks):

„Nach Abwägung von Tempo, Kostenrisiko, erwartbarem Erlös, Verjährungswirkung und Kontrolle über den Fall wird der Anspruchstellerin empfohlen, [den Anspruch zur Abhilfeklage gegen die [Name des Herstellers] anzumelden / die individuelle Schadensersatzklage zu erheben]. Maßgeblich ist, dass [tragender Grund, z. B. die Anmeldung die Verjährung ohne eigenes Kostenrisiko hemmt / der individuell bezifferte Anspruch die erwartbare kollektive Abhilfe deutlich übersteigt]. Das verbleibende Risiko besteht darin, dass [Risiko, z. B. die Anspruchstellerin die Prozessführung des Verbands nicht steuern kann / das Kostenrisiko der Einzelklage über zwei Instanzen bei ihr liegt]; dieses Risiko wurde erörtert und wird bewusst getragen."

Baustein Hemmung durch Anmeldung (aktuelle VDuG-Spur):

„Die wirksame Anmeldung des Anspruchs zum Verbandsklageregister hemmt die Verjährung nach § 204a BGB. Die Anmeldung wurde am [Datum TT.MM.JJJJ] vorgenommen und ist durch den Registerauszug mit Abrufdatum [Datum TT.MM.JJJJ] belegt (Anlage [Nummer]). Beginn und ein etwaiges Ende der Hemmung, insbesondere durch Rücknahme der Anmeldung nach §§ 46, 47 VDuG, sind tagesgenau in der Fristenkarte dokumentiert."

Baustein historische Musterfeststellung:

„Die Anspruchstellerin hat ihren Anspruch am [Datum TT.MM.JJJJ] zum Klageregister der Musterfeststellungsklage gegen die Volkswagen AG angemeldet und die Anmeldung [nicht zurückgenommen / am [Datum TT.MM.JJJJ] zurückgenommen]. Die Verjährung war deshalb nach § 204 Abs. 1 Nr. 1a BGB a.F. gehemmt; die Hemmungszeit ist anhand des Registerauszugs tagesgenau berechnet und an die Verjährungsprüfung übergeben (Anlage [Nummer])."

Baustein Vergleichsannahme:

„Die Anspruchstellerin hat den im Musterfeststellungsverfahren geschlossenen Vergleich am [Datum TT.MM.JJJJ] angenommen und die Vergleichssumme von [Betrag in EUR] erhalten. Eine erneute Geltendmachung desselben Schadens gegen die [Name des Herstellers] ist damit regelmäßig ausgeschlossen. Ob und in welchem Umfang nicht vom Vergleich erfasste Restansprüche verbleiben, ist eine anwaltlich zu verantwortende Einzelfallprüfung und wird nicht ohne diese Freigabe nach außen vertreten."

### Entscheidungstabelle Individualklage gegen kollektive Spur

| Wenn (Befund) | Dann (Pfad) | Begründung | Nächster Skill |
| --- | --- | --- | --- |
| Einschlägige VDuG-Abhilfeklage läuft, Anmeldung noch möglich, Verjährung drängt | Anmeldung zum Verbandsklageregister prüfen und dokumentieren | Hemmung nach § 204a BGB bei geringem eigenem Kostenrisiko; Rücknahme nach §§ 46, 47 VDuG bleibt fristgebunden möglich | Skill 03 (Fristenkarte) |
| Keine einschlägige Verbandsklage im live geprüften Register | Einzelklage vorbereiten | Ohne registrierte kollektive Spur gibt es weder Hemmung noch Abhilfe aus dem VDuG | Skill 13 |
| Hoher, gut belegter Individualschaden und tragfähige Kostendeckung | Einzelklage auch neben laufender Verbandsklage erwägen | Erwartbarer Erlös und Kontrolle über Vergleich und Beweisführung sprechen gegen den Kollektivautomatismus | Skill 13 |
| Damals wirksam angemeldet, nicht zurückgenommen, kein Vergleich angenommen | Einzelspur mit historischer Hemmungszeit rechnen | § 204 Abs. 1 Nr. 1a BGB a.F. wirkt nur für wirksam Angemeldete und ist tagesgenau zu belegen | Skill 07 |
| Damaliger Vergleich angenommen | Rote Ampel für die Einzelklage, Restansprüche anwaltlich prüfen | Die Vergleichsannahme schließt denselben Schaden regelmäßig aus | Anwaltliche Eskalation |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Registerstände live prüfen und mit Abrufdatum sichern; historische Hemmung nach § 204 Abs. 1 Nr. 1a BGB a.F. und aktuelle Hemmung nach § 204a BGB ausdrücklich auseinanderhalten. Rechtsprechung nur aus `references/gepruefte-anker-dieselgate.md`. Keine erfundenen Aktenzeichen oder Registerstände.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Entscheidungsvorlage mit Gegenüberstellung, Empfehlung und nächstem Schritt in vollständigen, ausformulierten Sätzen; Stichwort-Skelette sind als Endprodukt unzulässig.

## Beispiele

- Eingang: EA189-Golf, Kauf 2014, nie zur Musterfeststellung angemeldet. Kernbefund: keine historische Hemmung. Erste Antwort: Gegenüberstellungstabelle mit roter Verjährungsampel der Einzelspur und Übergabe der Fristfrage an Skill 07.
- Eingang: Beraterin meldet eine laufende VDuG-Abhilfeklage zum betroffenen Motor. Kernbefund: Anmeldung noch möglich, Registerstand ungeprüft. Erste Antwort: Entscheidungsvorlage mit Empfehlungsbaustein pro Anmeldung, dokumentierter Hemmungswirkung nach § 204a BGB und Lückenliste `[Registerstand mit Abrufdatum]`.
- Eingang: Geschädigter hat den VW-Vergleich 2020 angenommen und will erneut klagen. Kernbefund: derselbe Schaden ist regelmäßig verbraucht. Erste Antwort: vorläufiger, aber vollständig ausformulierter Beratungsvermerk mit Vergleichsannahme-Baustein, roter Ampel und präzise bezeichneten, anwaltlich zu prüfenden Restansprüchen.
