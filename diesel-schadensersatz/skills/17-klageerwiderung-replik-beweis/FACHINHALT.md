---
name: 17-klageerwiderung-replik-beweis
description: "Für Klageerwiderung, gerichtlichen Hinweis, Widerklage oder Replik. Ordnet Einwendungen und erstellt eine vollständige Replik mit Beweisangeboten. Nicht für bloße vorgerichtliche Herstellerkorrespondenz."
---

# Klageerwiderung, Replik und Beweis

## Zweck und Anwendungsfall

Wertet die Klageerwiderung aus, baut die Einwendungsmatrix, erstellt die Replik mit Beweisangeboten und wehrt Widerklagen ab.

## Bedienmodus

Arbeite für Geschädigte und Berater mit Tabellen, Ampel, Lückenliste und genau einem nächsten Schritt; Schwieriges an Rechtsanwältin oder Rechtsanwalt eskalieren, keine Rechtsberatung ohne anwaltliche Verantwortung.

## Erste Antwort

Die erste Antwort liefert sofort die Einwendungsmatrix und eine vorläufige, aber vollständig ausformulierte Replik mit allen aus dem Arbeitsmaterial tragfähigen Erwiderungen, Subsumtionen und Beweisangeboten. Als konkrete Lücken werden nur fehlende Randnummern oder Fundstellen der Klageerwiderung, Tatsachenbelege, Beweismittel und Fristdaten benannt. Verboten: Theorie-Vorträge, Menü-Aufzählungen, Werkzeug-Fehlersuche, mehr als drei Rückfragen, Rückfragen trotz möglichem Platzhalter-Ergebnis. Werkzeugausfälle blockieren nie den Entwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Klageerwiderung, Hinweisbeschluss, Widerklage oder Berufungsurteil.
- Klage mit Anlagen (Skill 14/15), Beweisplan (05), Fristenkarte (03).
- Replikfrist aus dem Gerichtsanschreiben.

## Ablauf / Checkliste

1. Einwendungsmatrix bauen — vor jedem Schreiben, mit den Spalten Randnummer, Vortrag Hersteller, Norm/Anker, Relevanz, Antwort, Beweis, Risiko.
2. Verteidigungslinien nach der Arbeitsmaterial-Tabelle prüfen; ergänzend Herstellerrolle, Erwerbskausalität, Verbotsirrtum, § 852. Beim Verbotsirrtum die Fehlvorstellung aller §-31-BGB-Repräsentanten bestreiten; eine hypothetische Behördenantwort genügt nicht.
3. Update-Einwand dreistufig: keine Heilung (`VI ZR 452/19`); Kausalketten-Fortsetzung (`VIa ZR 419/21`); eigener Streitgegenstand nur bei späterer Funktion plus Schaden (`C-666/23`, `VII ZR 283/20`), Kenntnis separat; neuer § 826 braucht zusätzliche Verwerflichkeitstatsachen (`VI ZR 889/20`).
4. Replik: Ungefährliches unstreitig stellen, Falsches präzise bestreiten, Primärdarlegung sichern; dann sekundäre Darlegungslast, bei Nichterfüllung § 138 Abs. 3 ZPO — keine Geständnisautomatik.
5. Parallelverfahren: Sechs-Anker-Set mit `diesel-fuenfjahre-query.py`; Quelle, Passage, technische Identität darlegen; günstigen Herstellervortrag hilfsweise übernehmen; korrigierter Vortrag ist nicht offenkundig. `VIa ZR 314/24` nur für Fiat/MIT-Stoff nach Hinweis und Gehör; Prozessbetrugsvorwürfe sind keine Tatsachen.
6. Beweisangebote: Gutachten (Umschaltlogik, Temperaturfenster, Update-Inhalt), Urkunden, Zeugen; Beweis- und Anlagenmatrix.
7. Widerklage/negative Feststellungsklage: Zulässigkeit und Rechtsschutzbedürfnis prüfen, doppelte Nutzungsersatz-Anrechnung zurückweisen.
8. Hinweise in die Matrix; Strategiewechsel über Skill 06. KBA-Nachschub mit Eingangsnachweis und §-156-Antrag sichern; Restwertangebote nur mit voller Merkmalskette.
9. Replik ausformulieren, Fristenkarte aktualisieren; Vergleichssignale an Skill 18. Freigegebene Replik an Skill `21-bea-versandfertig-schriftsatz-anlagen`, erst bei grünem Paket an Skill 16.
10. Nach nachteiliger Entscheidung Rechtsmittel, Anhörungsrüge, Fristen getrennt prüfen; anwaltlich eskalieren. Tatbestandsfehler fristgerecht nach § 320 ZPO angreifen (`VIa ZR 236/25`); die §-551-Rüge ersetzt das nicht. Differenzschaden-Hilfsantrag nach §-522-Hinweis dokumentieren (`VIa ZR 947/23`). § 321a ZPO nur bei Gehörsverletzung mit Passage und Kenntnisdatum.
11. Haupt-, Teil- und Ergänzungsurteil als selbständige Rechtsmittelgegenstände abgleichen. Für jede gesonderte Berufung die tragenden Erwägungen der konkret angefochtenen Entscheidung innerhalb der Begründungsfrist angreifen; Verbindung oder Gegenerklärung ersetzt dies nicht (`VIa ZB 3/24`).

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Jeden erheblichen Einwand der Gegenseite fair erfassen und mit Zugeständnis, Abgrenzung, Gegenbeleg, Beweislast und prozessualer Folge beantworten.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Kein Bestreitensbaustein bleibt ohne Fundstelle, eigene Antwortlinie, Beweisangebot und Fristkontrolle.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | EG-Typgenehmigung oder hypothetische Behördenbestätigung trägt einen daraus hergeleiteten unvermeidbaren Verbotsirrtum nicht; Umfang, Funktion und Informationsgrundlage eines konkreten Behördenkontakts bestreiten. | Amtlich geprüft |
| BGH, Beschl. v. 28.07.2026 - VIa ZR 46/24 | Zentralen KBA-Vortrag in der EA288-§-826-Spur würdigen; der Gehörsbeschluss ist keine §-823-Abs.-2-Entlastung und kein Serienbeweis. | Amtlich geprüft |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Für den deutschen Differenzschaden genügen Fahrlässigkeit und die weiteren Voraussetzungen der BGH-Trilogie; Verschulden, Erwerbskausalität, Quote und Vorteilsausgleich getrennt erwidern. | Bestätigt |
| BGH, Urt. v. 17.12.2020 - VI ZR 739/20 | Die Verjährungseinrede ist anhand konkreter Kenntnis der Fahrzeugbetroffenheit, Anspruchsgrundlage und Zumutbarkeit der Klage zu prüfen; EA189-Wertungen nicht pauschal übertragen. | Amtlich geprüft |
| BGH, Beschl. v. 11.08.2026 - VIa ZB 3/24 | Bei gesonderter Berufung gegen ein Ergänzungsurteil die konkrete Entscheidung und ihre tragenden Erwägungen eigenständig angreifen; Verbindung und Gegenerklärung ersetzen keine §-520-Abs.-3-Begründung. | Amtlich geprüft |
| Fünfjahreskorpus 26.08.2021 bis 26.08.2026: 135 Entscheidungen und Statusakten | Aktuelle OLG-/LG-Gegenlinien und verwaltungsgerichtliche Kontextanker nur mit Fahrzeug-, Funktions- und Verfahrensvergleich einführen. | Kuratierter Arbeitskorpus mit Quellenrängen |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Einwendungstabelle

| Herstellerverteidigung | Antwortlinie | Beweisangebot |
| --- | --- | --- |
| Verjährung §§ 195, 199 BGB | Kenntnis der konkreten Betroffenheit bestreiten (VI ZR 739/20); hilfsweise § 852 BGB bei belegtem Zufluss (VII ZR 365/21) | Rückrufschreiben, KBA-Bescheid |
| Heilung durch Update | Keine Heilung (VI ZR 452/19); Kausalkette (VIa ZR 419/21); eigener Streitgegenstand bei späterer Funktion plus Schaden (C-666/23, VII ZR 283/20) | Gutachten zum Update-Inhalt |
| Thermofenster als Motorschutz | Enge Ausnahme (C-134/20, C-128/20); Temperaturfenster und Alternativtechnik konkretisieren | Gutachten: Umschaltlogik, Temperaturfenster |
| Voll-Aufzehrung | Konkrete Rechenfehler angreifen, keine pauschale EU-Divergenz (VIa ZR 87/24, VIa ZR 613/24); Restwertangebote nur mit voller Merkmalskette | Kilometerstände, Restwertbelege |
| Pauschales Bestreiten | Sekundäre Darlegungslast nach Primärvortrag (VII ZR 286/20, VIa ZR 347/22); Folge § 138 Abs. 3 ZPO | Gutachten zum realen Fahrbetrieb (C-693/18) |

### Formulierungsbausteine

**Baustein 1 — sekundäre Darlegungslast:**

Die Klagepartei hat mit [Motortyp/Baumuster], Rückruf [Rückrufcode] und Funktionsweise der [Abschalteinrichtung] greifbare Anhaltspunkte dargelegt; mehr ist nicht zu verlangen (BGH, Urt. v. 25.09.2024 - VIa ZR 347/22). Die Beklagte trifft die sekundäre Darlegungslast zu Funktionsweise, Aktivierung und Genehmigungslage (BGH, Urt. v. 16.09.2021 - VII ZR 286/20); sonst gilt der Klagevortrag nach § 138 Abs. 3 ZPO als zugestanden. Beweis: Sachverständigengutachten zum realen Fahrbetrieb (EuGH, Urt. v. 17.12.2020 - C-693/18).

**Baustein 2 — Erwiderung auf die Verjährungseinrede:**

Die Verjährungseinrede greift nicht durch. Der Fristbeginn nach §§ 195, 199 Abs. 1 BGB setzt Kenntnis oder grob fahrlässige Unkenntnis der konkreten Betroffenheit des Fahrzeugs [FIN] voraus; EA189-Wertungen sind nicht pauschal übertragbar (BGH, Urt. v. 17.12.2020 - VI ZR 739/20). Kenntnis bestand erst mit [Rückrufschreiben vom TT.MM.JJJJ]; die Frist begann frühestens mit Schluss des Jahres [JJJJ]; sie war bei Klageerhebung nicht abgelaufen. Hilfsweise wird Restschadensersatz nach § 852 BGB geltend gemacht; der Zufluss folgt aus [Neuwagengeschäft/Beleg] (BGH, Urt. v. 10.02.2022 - VII ZR 365/21).

## Quellenpflicht

Es gilt `references/zitierweise.md`. Anker und aktuelle LG-/OLG-Gegenlinien über `references/gepruefte-anker-dieselgate.md` sowie `references/diesel-rechtsprechung-2021-2026.md` verifizieren; Rechtsmittelgrenzen und Übergangsrecht über `references/rechtsstand-2026-gesetzgebung.md` prüfen; KBA-/Gansel-Material nach `references/behoerden-und-praxisquellen-diesel.md` kalibrieren. Parteimaterial und EA288-Kanzleivolltexte bleiben als solche gekennzeichnet.

## Ausgabeformat

1. **Kontrollansicht**

   Der `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt`; nie Bestandteil von Schriftsatz, Anlage oder Exportdatei.

2. **Fachprodukt**

   Prozesskarte, Einwendungsmatrix, ausformulierte Replik in dezimaler Gliederung, Beweis- und Anlagenmatrix; Skelette verboten. Übergabe an Skill 21 mit Freigabestatus, Platzhaltern, Anlagen-Textankern und Haupt-PDF-SHA-256; ein Entwurf gilt nie als Endfassung.

## Beispiele

- Verjährungseinrede plus Genehmigungs-Verteidigung: Matrix und vorläufige, aber vollständig ausformulierte Replik mit Verjährungsabsatz samt Fristrechnung; fehlende Zustell- oder Kenntnisbelege sind am jeweiligen Satz markiert.
- Thermofenster pauschal bestritten: Kernabsatz sekundäre Darlegungslast, Gutachtenbeweis mit drei Beweisthemen.
- Negative Feststellungswiderklage: Matrixzeile Zulässigkeit mit Rüge-Entwurf, Prozesskarte.
- Berufungsurteil gibt Vortrag falsch wieder: §-320-Frist und vorläufiger, aber vollständig ausformulierter Berichtigungsantrag mit genau bezeichneter Urteilsstelle (`VIa ZR 236/25`).
