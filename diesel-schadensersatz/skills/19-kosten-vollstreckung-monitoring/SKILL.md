---
name: 19-kosten-vollstreckung-monitoring
description: "Für Urteil, Vergleichstitel, KFA, KFB, Zahlung oder Vollstreckung. Führt Forderung, Kosten, Rechtsbehelf, Zug-um-Zug-Leistung und Wiedervorlage fort. Nicht ohne Titel oder vollstreckbare Grundlage."
---

# Kosten, Vollstreckung und Monitoring

## Zweck und Anwendungsfall

Dieser Skill führt den Fall nach Titelgewinn zu Ende: Kostenfestsetzung, Prüfung des Kostenfestsetzungsbeschlusses, Zahlungsüberwachung, Vollstreckung und Aktenmonitoring. Er arbeitet ausschließlich aus dem vollstreckbaren Tenor — keine neue Anspruchsbegründung. Hersteller sind regelmäßig solvent: Meist genügen qualifizierte Zahlungsaufforderung und Kontopfändung als Drohkulisse; Vermögensauskunft und Drittauskunft bleiben Ausnahmefälle.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort ein Arbeitsprodukt: das Forderungskonto aus dem Tenor (Hauptforderung, Zinslauf, Kosten, Zahlungen, offener Rest) und — je nach Verfahrensstand — den Kostenfestsetzungsantrag mit ausformulierten Antragssätzen oder den nächsten Vollstreckungsschritt aus der Wenn/Dann-Tabelle; fehlende Belege stehen als klar markierte Platzhalter mit Nachlieferungsauftrag. Verboten in der ersten Antwort sind Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen; eine Rückfrage unterbleibt, wenn ein vorläufiges Konto mit Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Sind sie nicht verfügbar oder schlagen sie fehl, wird ohne Meldungslärm manuell gerechnet; ein Werkzeugfehler blockiert nie Forderungskonto oder Antragsentwurf. Fristen werden nie geschätzt.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Urteil, Prozessvergleich oder Kostenfestsetzungsbeschluss mit Zustelldaten.
- Kostenaufstellung: Gerichtskosten, RVG-Gebühren, Auslagen, Sachverständigenkosten, Zahlungen des Herstellers.
- Zahlungseingänge mit Datum und Betrag.

## Ablauf / Checkliste

1. Tenor auslesen: Zahlungsbetrag, Zinsen, Zug-um-Zug-Formel, Annahmeverzugs-Feststellung, Kostengrundentscheidung mit Quote; Rechtskraft oder vorläufige Vollstreckbarkeit trennen.
2. Kostenfestsetzungsantrag stellen (§§ 103, 104 ZPO): erstattungsfähige Positionen mit Beleg (Gerichtskosten, RVG nach Streitwert, Auslagen, Sachverständigenkosten), Zinsantrag ab Antragseingang, Quote anwenden.
3. Eingehenden Kostenfestsetzungsbeschluss prüfen: Abweichung vom Antrag, Betrag, Zinsen, Quote, Zustellung, Rechtsbehelfsfrist; bei Fehlern Erinnerung oder sofortige Beschwerde mit konkreter Frist — Fristen nie schätzen.
4. Forderungskonto führen: Hauptforderung, Zinsen tagesgenau, Kosten; Teilzahlungen in gesetzlicher Reihenfolge verrechnen (§ 367 BGB: Kosten, Zinsen, Hauptforderung); offenen Rest ausweisen.
5. Vollstreckungsvoraussetzungen sichern: vollstreckbare Ausfertigung, Klausel, Zustellung, Wartefristen (§§ 750 ff. ZPO); der Kostenfestsetzungsbeschluss ist eigener Titel.
6. Maßnahme nach Schuldnerprofil wählen: qualifizierte Zahlungsaufforderung mit kurzer Frist, dann Kontopfändung (§§ 829, 835 ZPO). Bei Zug-um-Zug-Titeln § 756 ZPO anwenden: Entweder ist Befriedigung oder Annahmeverzug urkundlich nachgewiesen, oder der Gerichtsvollzieher bietet die Gegenleistung in verzugsbegründender Weise an; ergänzend § 765 ZPO prüfen. Festgestellter Annahmeverzug erleichtert die Vollstreckung, ist aber nicht der einzige gesetzliche Weg. Fahrzeug, Schlüssel, Papiere und Übergabeprotokoll bereithalten.
7. Ausnahmefälle erkennen: insolventer Händler oder Kleinimporteur — dann Vermögensauskunft und Drittauskunft (§§ 802a ff., 802l ZPO) prüfen und anwaltlich eskalieren; bei Insolvenz sofort stoppen.
8. Monitoring führen: Wiedervorlagen für Zahlungsfristen, Zinslauf, Vergleichserfüllung, Verjährung titulierter Forderungen; Monitoring-Tabelle (Titel, Betrag, Zins, Kosten, Zahlung, Rest, Maßnahme, Wiedervorlage) aktuell halten.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Ausschließlich aus Titel, Kostenentscheidung und belegtem Forderungskonto arbeiten und Maßnahmen verhältnismäßig auswählen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Keine Maßnahme ohne Titelprüfung, Klausel/Zustellung, Tilgungsreihenfolge, Schuldneridentität, Kosten und Vier-Augen-Freigabe.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

- **Anker:** Keine Dieselgate-Leitentscheidung einschlägig. Für Kostenfestsetzung und Zwangsvollstreckung trägt keine Dieselgate-Leitentscheidung; aus dem konkreten Titel arbeiten und §§ 91, 103 f., 750 ff., 756 und 765 ZPO sowie § 367 BGB anwenden. **Status:** Hinweis.

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Kostenfestsetzungsantrag (Antragssätze):**

In dem Rechtsstreit [Name der Klägerin] gegen [Name des Herstellers], Az. [Aktenzeichen], wird beantragt,

1

die von der Beklagten an die Klägerin zu erstattenden Kosten auf Grundlage der Kostengrundentscheidung in dem [Urteil / Prozessvergleich] vom [Datum TT.MM.JJJJ] gemäß §§ 103, 104 ZPO auf [Betrag in EUR] festzusetzen;

2

auszusprechen, dass der festgesetzte Betrag ab Eingang dieses Antrags bei Gericht mit fünf Prozentpunkten über dem Basiszinssatz jährlich zu verzinsen ist (§ 104 Abs. 1 Satz 2 ZPO);

3

der Klägerin eine vollstreckbare Ausfertigung des Kostenfestsetzungsbeschlusses zu erteilen.

Zur Festsetzung angemeldet werden im Einzelnen: Gerichtskosten in Höhe von [Betrag in EUR] gemäß Kostenrechnung vom [Datum TT.MM.JJJJ], Rechtsanwaltsgebühren nach dem RVG aus einem Streitwert von [Betrag in EUR] in Höhe von [Betrag in EUR] gemäß beigefügter Berechnung sowie Auslagen und Sachverständigenkosten in Höhe von [Betrag in EUR] gemäß Anlagen [Anlagennummern]. Auf die Summe ist die Kostenquote von [Anteil in Prozent] zulasten der Beklagten angewendet.

**Baustein 2 — qualifizierte Zahlungsaufforderung an den Hersteller:**

In vorbezeichneter Angelegenheit liegt gegen Sie ein vollstreckbarer Titel des [Gericht] vom [Datum TT.MM.JJJJ], Az. [Aktenzeichen], vor. Unter Berücksichtigung Ihrer Zahlung vom [Datum TT.MM.JJJJ] über [Betrag in EUR], die gemäß § 367 Abs. 1 BGB zunächst auf die Kosten, sodann auf die Zinsen und zuletzt auf die Hauptforderung verrechnet worden ist, valutiert die titulierte Forderung per [Datum TT.MM.JJJJ] noch mit [Betrag in EUR]; die tagesgenaue Aufstellung ist beigefügt. Wir fordern Sie auf, den offenen Betrag bis zum [Datum TT.MM.JJJJ] auf das Konto [IBAN] zu zahlen. Nach fruchtlosem Fristablauf werden ohne weitere Ankündigung Zwangsvollstreckungsmaßnahmen eingeleitet, insbesondere die Pfändung Ihrer Geschäftskonten (§§ 829, 835 ZPO); die hierdurch entstehenden Kosten fallen Ihnen nach § 788 ZPO zur Last.

**Baustein 3 — Erinnerung gegen den Kostenfestsetzungsbeschluss:**

Gegen den Kostenfestsetzungsbeschluss vom [Datum TT.MM.JJJJ], zugestellt am [Datum TT.MM.JJJJ], wird Erinnerung eingelegt. Der Beschluss weicht um [Betrag in EUR] von dem Antrag vom [Datum TT.MM.JJJJ] ab, weil die Position [Kostenposition] nicht berücksichtigt worden ist. Die Position ist erstattungsfähig, weil [Begründung, z. B. die Sachverständigenkosten zur zweckentsprechenden Rechtsverfolgung notwendig waren]; der Beleg liegt als Anlage [Anlagennummer] vor. Es wird beantragt, den Beschluss entsprechend abzuändern und weitere [Betrag in EUR] nebst Zinsen festzusetzen.

### Rechenbeispiel: Kostenquote und Verzinsung nach § 104 ZPO

Ausgangswerte: Kostengrundentscheidung 80 Prozent zulasten der Beklagten, 20 Prozent zulasten der Klägerin. Eigene Kosten der Klägerin laut Kostenaufstellung: verauslagte Gerichtskosten 720,00 EUR und Rechtsanwaltsgebühren 2.280,00 EUR, zusammen 3.000,00 EUR (Beträge aus der Akte; die Gebühren sind vor Antragstellung konkret nach RVG und GKG zu belegen).

Schritt 1 — Quote anwenden: 3.000,00 EUR mal 80 Prozent gleich 2.400,00 EUR festsetzungsfähiger Erstattungsbetrag. Meldet auch die Beklagte Kosten an, erfolgt stattdessen die Ausgleichung beider Kostenmassen nach § 106 ZPO.

Schritt 2 — Zinslauf: Verzinsung mit fünf Prozentpunkten über dem Basiszinssatz ab Eingang des Antrags bei Gericht (§ 104 Abs. 1 Satz 2 ZPO), im Beispiel ab dem 01.09.2026. Bei einem beispielhaft angesetzten Basiszinssatz von 2,27 Prozent (tagesaktuellen Wert bei der Deutschen Bundesbank prüfen) ergibt sich ein Zinssatz von 7,27 Prozent jährlich.

Schritt 3 — Zinsbetrag für 90 Tage: 2.400,00 EUR mal 7,27 Prozent mal 90 geteilt durch 365 Tage gleich 43,02 EUR.

Ergebnis-Satz: Festzusetzen sind 2.400,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz seit dem 01.09.2026; nach 90 Tagen Zahlungsverzug sind zusätzlich 43,02 EUR Zinsen in das Forderungskonto einzustellen.

### Entscheidungstabelle: Vollstreckungs-Wenn/Dann

| Befund | Maßnahme / Pfad | Begründung | Nächster Schritt |
| --- | --- | --- | --- |
| Titel vollstreckbar, Klausel und Zustellung liegen vor, reine Zahlungspflicht offen | Qualifizierte Zahlungsaufforderung mit 14-Tage-Frist (Baustein 2) | Hersteller sind regelmäßig solvent; die Drohkulisse genügt meist | Wiedervorlage auf Fristende |
| Zahlungsfrist fruchtlos abgelaufen | Pfändungs- und Überweisungsbeschluss auf Geschäftskonten (§§ 829, 835 ZPO) | Effektivste Maßnahme gegen solvente Schuldner; Vollstreckungskosten nach § 788 ZPO | Antrag beim Vollstreckungsgericht |
| Zug-um-Zug-Titel mit festgestelltem Annahmeverzug | Vollstreckung mit urkundlichem Nachweis des Annahmeverzugs (§ 756 ZPO) | Die Feststellung im Tenor erleichtert den Nachweis gegenüber dem Vollstreckungsorgan | Fahrzeug, Schlüssel, Papiere, Protokoll bereithalten |
| Zug-um-Zug-Titel ohne Annahmeverzugs-Feststellung | Gerichtsvollzieher bietet die Gegenleistung in verzugsbegründender Weise an (§ 756 ZPO); ergänzend § 765 ZPO prüfen | Der festgestellte Annahmeverzug ist nicht der einzige gesetzliche Weg | Auftrag an den Gerichtsvollzieher |
| Titel nur vorläufig vollstreckbar gegen Sicherheitsleistung | Sicherheit stellen oder Rechtskraft abwarten; wirtschaftliche Abwägung dokumentieren | §§ 708 ff. ZPO; Kosten der Sicherheit gegen Zinsvorteil rechnen | Anwaltliche Entscheidung einholen |
| Kostenfestsetzungsbeschluss weicht vom Antrag ab | Erinnerung oder sofortige Beschwerde mit konkreter Frist (Baustein 3) | Der KFB ist eigener Titel; Fehler nie hinnehmen, Fristen nie schätzen | Fristenkarte aktualisieren |
| Schuldner ist insolventer Händler oder Kleinimporteur | Vollstreckung stoppen; Vermögensauskunft und Drittauskunft (§§ 802a ff., 802l ZPO) nur nach anwaltlicher Eskalation | Bei Insolvenz gilt Vollstreckungsverbot; Forderung zur Tabelle anmelden | Anwaltliche Eskalation |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Kosten- und Vollstreckungsrecht mit Normanker (§§ 91, 103 f., 750 ff., 756, 765, 829 ZPO, § 367 BGB, GKG, RVG); keine dieselspezifische Leitentscheidung nötig — keine erfinden. Nur aus positivem, vollstreckbarem Tenor arbeiten.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Forderungskonto, ausformulierter Kostenfestsetzungsantrag, KFB-Prüfvermerk, Vollstreckungsplan und Monitoring-Tabelle in vollständigen, ausformulierten Sätzen; Stichwort-Skelette sind als Endprodukt unzulässig.

## Beispiele

- Eingang: gerichtlicher Vergleichstitel über 8.400 EUR, Hersteller zahlt in Teilbeträgen. Kernbefund: Verrechnung nach § 367 BGB ergibt offenen Rest von 2.150 EUR. Erste Antwort: Forderungskonto mit tagesgenauer Verrechnung und ausformulierte qualifizierte Zahlungsaufforderung mit 14-Tage-Frist.
- Eingang: Kostenfestsetzungsbeschluss, zugestellt mit Rechtsbehelfsbelehrung. Kernbefund: Abweichung von 480 EUR gegenüber dem Antrag, Sachverständigenposition fehlt. Erste Antwort: KFB-Prüfvermerk mit lokalisierter Abweichung und ausformulierter Erinnerung samt Fristberechnung aus dem Zustelldatum.
- Eingang: Zug-um-Zug-Titel mit festgestelltem Annahmeverzug, Hersteller zahlt nicht. Kernbefund: Vollstreckungsvoraussetzungen nach §§ 750 ff. ZPO liegen vor. Erste Antwort: Vollstreckungsplan nach der Wenn/Dann-Tabelle mit §-756-Pfad, Übergabelogistik (Fahrzeug, Schlüssel, Papiere, Protokoll) und Monitoring-Zeile für den Zahlungseingang.
