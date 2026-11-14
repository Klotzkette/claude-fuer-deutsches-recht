---
name: 13-klageweg-streitwert-zustaendigkeit
description: "Für Klageweg, Streitwert, Kosten, Amts- oder Landgericht, örtliche Zuständigkeit und Klageform. Liefert eine Antragsempfehlung vor Skill 14 oder 15. Nicht für die eigentliche Klageschrift."
---

# Klageweg, Streitwert und Zuständigkeit

## Zweck und Anwendungsfall

Dieser Skill stellt vor der Klage die formalen und taktischen Weichen: Streitwert und Kostenrisiko, zuständiges Gericht, Anwaltszwang und die richtige Klageform. Er prüft auch die Schnellwege — Mahnverfahren und Urkundsprozess — und sagt ehrlich, wann sie im Dieselfall nicht taugen. Ergebnis ist der Klagewegvermerk, mit dem Skill 14 oder 15 die Klage baut.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort den Klagewegvermerk im Entwurf: Streitwert mit Rechenweg, sachliche Zuständigkeit mit Norm (§ 23 Nr. 1, § 71 GVG, Übergangsrecht § 44 EGGVG), örtliche Zuständigkeit mit Antragskandidat (§ 32 oder § 17 ZPO), Kostenrahmen und Antragsempfehlung. Fehlende Zahlen werden als Platzhalter gesetzt (`[aktueller Kilometerstand]`, `[Sitz des Herstellers]`), der Rechenweg steht trotzdem vollständig da.

Verboten in der ersten Antwort: Theorie-Vorträge zu Zuständigkeitsrecht oder Kostenrecht, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche, mehr als drei Rückfragen sowie jede Rückfrage, wenn ein vorläufiger Vermerk mit klar markierten Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Steht ein Rechen- oder Abfrageskript nicht zur Verfügung, wird ohne Meldungslärm manuell gerechnet; ein Werkzeugfehler blockiert nie den Vermerkentwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Schadenstabelle aus Skill 08 (beide Rechenwege), Strategiekarte aus Skill 06.
- Sitz des Herstellers und Wohnsitz der Geschädigten (örtliche Zuständigkeit).
- Beweislage: feststehende oder offene Betroffenheit (Skill 04/05).
- Datum der Anhängigkeit sowie bei Rechtsmitteln Verkündung/Übergabe, Schluss der mündlichen Verhandlung, Zustellung, Beschwer und Zulassungsausspruch.

## Ablauf / Checkliste

1. Streitwert bestimmen: großer Schadensersatz = bezifferter Zahlungsantrag nach Abzug der bis zum maßgeblichen Stichtag angesetzten Nutzungsentschädigung; Differenzschaden = bezifferter Zahlungsbetrag; sonstiger Feststellungsantrag nach seinem wirtschaftlichen Interesse mit sachgerechtem Abschlag. Die Feststellung des Annahmeverzugs neben einer Zug-um-Zug-Verurteilung hat nach `VIII ZR 290/19` keinen eigenen wirtschaftlichen Wert.
2. Sachliche Zuständigkeit nach aktuellem § 23 Nr. 1 GVG: bis einschließlich 10.000 EUR grundsätzlich Amtsgericht, darüber grundsätzlich Landgericht (§ 71 GVG). Nach § 44 EGGVG bleibt für Verfahren, die vor dem 01.01.2026 anhängig wurden, die bis 31.12.2025 geltende 5.000-EUR-Fassung maßgeblich. Besondere Zuweisungen prüfen. Anwaltszwang besteht vor Landgericht (§ 78 ZPO), nicht allein wegen der Fallart.
3. Rechtsmittelweiche 2026 gesondert rechnen: Die Berufung setzt nach § 511 Abs. 2 Nr. 1 ZPO grundsätzlich eine Beschwer von mehr als 1.000 EUR oder ihre Zulassung voraus. Die Nichtzulassungsbeschwerde setzt nach § 544 Abs. 2 Nr. 1 ZPO grundsätzlich eine Beschwer von mehr als 25.000 EUR voraus; die Alternative des § 544 Abs. 2 Nr. 2 ZPO bei als unzulässig verworfener Berufung getrennt prüfen. § 47 EGZPO erhält die alten Schwellen insbesondere für bis 31.12.2025 verkündete/übergebene Entscheidungen oder bis dahin geschlossene Verhandlungen. Streitwert, Beschwer und Rechtsmittelzulassung nie gleichsetzen.
4. Örtliche und internationale Zuständigkeit getrennt prüfen: Sitz des Herstellers (§ 17 ZPO), deliktischer Gerichtsstand (§ 32 ZPO) und bei grenzüberschreitendem Sachverhalt Art. 7 Nr. 2 Brüssel-Ia-VO. Wohnsitz oder Kaufort nicht schematisch als Erfolgsort behaupten; Erwerb, Zahlung und Übergabe konkret zuordnen.
5. Kostenrechnung aufstellen: Gerichtskostenvorschuss (§ 12 GKG, drei Gebühren), RVG-Gebühren beider Seiten, Sachverständigenkosten; Kostenrisiko über zwei Instanzen ausweisen und gegen den erwartbaren Erlös stellen.
6. Klageform wählen: bezifferte Leistungsklage als Regelfall; Teilklage nur mit eindeutig abgegrenztem Anspruchsteil und dokumentierten Bindungs-/Verjährungsrisiken; Feststellungsklage nach § 256 ZPO nur bei konkretem Feststellungsinteresse und unter Beachtung des Vorrangs möglicher Leistungsklage. Streitige Betroffenheit allein ersetzt das Feststellungsinteresse nicht.
7. Schnellwege rechtlich und taktisch prüfen: Das Mahnverfahren setzt einen Zahlungsanspruch voraus und ist bei einer noch nicht erbrachten Gegenleistung nach § 688 Abs. 2 Nr. 2 ZPO gesperrt; bei absehbarem Widerspruch ist es meist nur ein Umweg. Ein Urkundenprozess nach §§ 592 ff. ZPO ist nur tragfähig, wenn sämtliche beweisbedürftigen anspruchsbegründenden Tatsachen mit zulässigen Urkunden bewiesen werden können; technischer Sachverständigenbedarf spricht regelmäßig dagegen, ist aber kein abstraktes Zulässigkeitsverbot.
8. Klagewegvermerk mit Ampel ausgeben und übergeben: Rückabwicklung an Skill `14-klage-rueckabwicklung-zug-um-zug`, Differenzschaden an Skill `15-klage-differenzschaden`.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Aus Anspruch und Tatsachen die richtige Klageart, das zuständige Gericht, den Streitwert und das Kostenrisiko ableiten.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Gericht, Beklagtensitz, besonderer Gerichtsstand, Antragstyp, Streitwert und Anwaltszwang sind mit Beleg und Norm geprüft.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Für die Zuständigkeitsprüfung den aktuell bezifferten Zahlungsantrag nach Nutzungsabzug verwenden; die Grenze von 10.000 EUR nach § 23 Nr. 1 GVG anwenden, nicht schematisch vom ursprünglichen Kaufpreis ausgehen. | Bestätigt |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Für die Zuständigkeitsprüfung ist der bezifferte Differenzschaden maßgeblich; die aktuelle Amtsgerichtsgrenze und Übergangsrecht prüfen. | Bestätigt |
| BGH, Urt. v. 15.02.2024 - VII ZR 905/21 | Differenzschaden grundsätzlich mit bezifferter Leistungsklage verfolgen; eine Feststellungsklage scheitert ohne eigenständiges Feststellungsinteresse am Vorrang der Leistungsklage. | Amtlich geprüft |
| BGH, Beschl. v. 13.10.2020 - VIII ZR 290/19 | Die Feststellung des Annahmeverzugs neben einer Zug-um-Zug-Verurteilung hat keinen eigenen wirtschaftlichen Wert; nicht zusätzlich auf den Streitwert aufschlagen. | Amtlich geprüft |
| Keine Dieselgate-Leitentscheidung einschlägig | Für Mahn- und Urkundenverfahren trägt keine Dieselgate-Leitentscheidung; Zulässigkeit und Taktik nach §§ 592 ff. und 688 Abs. 2 ZPO sowie der konkreten Gegenleistungs- und Beweislage prüfen. | Hinweis |
| EuGH, Urt. v. 09.07.2020 - C-343/19 | Bei grenzüberschreitendem Erwerb Erfolgsort, Lieferung, Wohnsitz und Beklagtensitz nach Art. 7 Nr. 2 Brüssel-Ia-VO gesondert prüfen. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine für die Zuständigkeitsbegründung

Baustein örtliche Zuständigkeit nach § 32 ZPO (deliktischer Gerichtsstand):

„Die örtliche Zuständigkeit des angerufenen Gerichts folgt aus § 32 ZPO. Der Erfolgsort der unerlaubten Handlung liegt im Bezirk des angerufenen Gerichts, weil die Klägerin dort am [Datum TT.MM.JJJJ] den Kaufvertrag über das Fahrzeug mit der FIN [FIN] abgeschlossen, den Kaufpreis von [Betrag in EUR] gezahlt und das Fahrzeug übernommen hat; dort ist ihr Vermögen durch die Eingehung der ungewollten Verbindlichkeit geschädigt worden."

Baustein örtliche Zuständigkeit nach § 17 ZPO (Sitz des Herstellers):

„Die örtliche Zuständigkeit des angerufenen Gerichts folgt aus § 12 in Verbindung mit § 17 Abs. 1 ZPO. Die Beklagte hat ihren Sitz in [Sitz des Herstellers]; dieser liegt im Bezirk des angerufenen Gerichts."

Baustein sachliche Zuständigkeit:

„Die sachliche Zuständigkeit des Landgerichts folgt aus § 71 Abs. 1, § 23 Nr. 1 GVG, weil der Streitwert 10.000,00 EUR übersteigt. [Alternativ bei Differenzschaden bis einschließlich 10.000,00 EUR: Die sachliche Zuständigkeit des Amtsgerichts folgt aus § 23 Nr. 1 GVG, weil der Streitwert 10.000,00 EUR nicht übersteigt.] Für Verfahren, die vor dem 01.01.2026 anhängig geworden sind, bleibt nach § 44 EGGVG die bis zum 31.12.2025 geltende Wertgrenze von 5.000,00 EUR maßgeblich."

### Rechenbeispiel Zuständigkeits- und Kostenweiche

1 Streitwert großer Schadensersatz

Kaufpreis 32.500,00 EUR, seit dem Erwerb gefahren 98.400 km, erwartete Gesamtlaufleistung 250.000 km (Neuwagen, Restlaufleistung beim Kauf also 250.000 km). Nutzungsentschädigung: 32.500,00 EUR mal 98.400 km geteilt durch 250.000 km gleich 12.792,00 EUR. Streitwert des Zahlungsantrags: 32.500,00 EUR minus 12.792,00 EUR gleich 19.708,00 EUR. Der Antrag auf Feststellung des Annahmeverzugs erhöht den Streitwert nach `VIII ZR 290/19` nicht.

2 Streitwert Differenzschaden

Bei einer Quote von 10 Prozent beträgt der bezifferte Zahlungsantrag 32.500,00 EUR mal 0,10 gleich 3.250,00 EUR; Vorteilsausgleich und Aufzehrung rechnet Skill 15.

3 Zuständigkeitsfolge

19.708,00 EUR übersteigen 10.000,00 EUR: Landgericht (§ 71 Abs. 1, § 23 Nr. 1 GVG), Anwaltszwang nach § 78 Abs. 1 ZPO. 3.250,00 EUR liegen darunter: grundsätzlich Amtsgericht, kein Anwaltszwang aus der Instanz heraus; Übergangsrecht nach § 44 EGGVG bei Anhängigkeit vor dem 01.01.2026 gesondert prüfen.

4 Gerichtskostenvorschuss dem Prinzip nach

Der Vorschuss beträgt drei Verfahrensgebühren (§ 12 Abs. 1 GKG): einfache Gebühr zum Streitwert von 19.708,00 EUR aus der am Einreichungstag geltenden Anlage 2 zum GKG ablesen und mit 3,0 multiplizieren. Der konkrete Tabellenwert wird nie aus dem Gedächtnis gesetzt, sondern stets aus der aktuellen Anlage 2 GKG übernommen; erst dann ist der Vermerk vorschussreif.

5 Ergebnis-Satz

Der große Schadensersatz führt mit 19.708,00 EUR vor das Landgericht mit Anwaltszwang und einem Vorschuss aus drei Gebühren nach Anlage 2 GKG; der Differenzschaden führt mit 3.250,00 EUR grundsätzlich vor das Amtsgericht.

### Entscheidungstabelle Klageweg

| Wenn (Befund) | Dann (Pfad) | Begründung | Nächster Skill |
| --- | --- | --- | --- |
| Bezifferter Antrag über 10.000,00 EUR | Landgericht, anwaltliche Vertretung zwingend | § 71 Abs. 1, § 23 Nr. 1 GVG; § 78 Abs. 1 ZPO | Skill 14 oder 15 |
| Bezifferter Antrag bis einschließlich 10.000,00 EUR | Grundsätzlich Amtsgericht | § 23 Nr. 1 GVG; besondere Zuweisungen prüfen | Skill 15 |
| Anhängigkeit vor dem 01.01.2026 | Alte 5.000-EUR-Grenze anwenden | § 44 EGGVG erhält die bis 31.12.2025 geltende Fassung | Vermerk anpassen |
| Zug-um-Zug-Antrag plus Feststellung Annahmeverzug | Kein Streitwertaufschlag für die Feststellung | `VIII ZR 290/19`: kein eigener wirtschaftlicher Wert | Skill 14 |
| Grenzüberschreitender Erwerb | Internationale Zuständigkeit gesondert begründen | Art. 7 Nr. 2 Brüssel-Ia-VO; Erwerb, Zahlung und Übergabe konkret zuordnen | Anwaltliche Eskalation |
| Gegenleistung (Fahrzeugrückgabe) noch nicht erbracht | Kein Mahnverfahren | § 688 Abs. 2 Nr. 2 ZPO sperrt den Mahnweg | Leistungsklage |

## Quellenpflicht

Es gelten `references/zitierweise.md` und `references/rechtsstand-2026-gesetzgebung.md`. Zuständigkeits-, Rechtsmittel- und Kostenaussagen mit aktuellem Normanker (§ 23 Nr. 1, § 71 GVG, § 44 EGGVG, §§ 17, 32, 78, 256, 511, 544, 592 ff., 688 Abs. 2 ZPO, § 47 EGZPO, Art. 7 Nr. 2 Brüssel-Ia-VO, § 12 GKG); Rechtsprechung nur aus der geprüften Anker- und Obergerichtsmatrix.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Klagewegvermerk mit Streitwert- und Kostenrechnung (Tabelle), Zuständigkeitsentscheidung mit Normbegründung und Antragsempfehlung in vollständigen, ausformulierten Sätzen; Stichwort-Skelette sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Schadenstabelle mit Zahlungsantrag 19.708,00 EUR nach Nutzungsabzug. Kernbefund: über der 10.000-EUR-Grenze. Erste Antwort: Klagewegvermerk-Entwurf mit Landgericht am Herstellersitz (§ 17 ZPO), Anwaltszwang, Vorschussprinzip aus drei Gebühren und Empfehlung der bezifferten Leistungsklage.
- Eingang: Differenzschaden mit 3.250,00 EUR beziffert. Kernbefund: grundsätzlich Amtsgericht. Erste Antwort: Vermerkentwurf mit § 23 Nr. 1 GVG, §-32-ZPO-Baustein für den Wohnsitzgerichtsstand mit konkret zugeordnetem Erwerbsort und bezifferter Klage statt Feststellung.
- Eingang: offene EA288-Betroffenheit, Beraterin erwägt Feststellungsklage. Kernbefund: Vorrang der bezifferbaren Leistungsklage (`VII ZR 905/21`). Erste Antwort: Vermerkentwurf mit geprüftem Feststellungsinteresse und Feststellungsempfehlung nur für den Fall nicht abschließend bezifferbarer Schadensentwicklung.
