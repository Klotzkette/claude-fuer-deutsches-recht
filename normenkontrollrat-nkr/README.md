# Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`normenkontrollrat-nkr`) | [`normenkontrollrat-nkr.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrollrat-nkr.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Testakte NKR: Elektronische Erreichbarkeit von Handelsregister-Gesellschaften (ElErrHandRegG 2026)** (`nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026`) | [Gesamt-PDF lesen](../testakten/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/gesamt-pdf/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026_gesamt.pdf) | [`testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Plugin für den Nationalen Normenkontrollrat (NKR): Prüfung von Referentenentwürfen Formulierungshilfen und Gesetzentwürfen auf Erfüllungsaufwand Erforderlichkeit Verhältnismäßigkeit One-in-one-out Digitalcheck Mittelstandsfreundlichkeit und Praktikabilitaet im Vollzug.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`normenkontrollrat-nkr.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrollrat-nkr.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/normenkontrollrat-nkr/normenkontrollrat-nkr-werkstatt.md" download><code>normenkontrollrat-nkr-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/normenkontrollrat-nkr/normenkontrollrat-nkr-schnellstart.md" download><code>normenkontrollrat-nkr-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Testakte NKR: Elektronische Erreichbarkeit von Handelsregister-Gesellschaften (ElErrHandRegG 2026): [Gesamt-PDF](../testakten/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/gesamt-pdf/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026_gesamt.pdf), [`testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026.zip), [`testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für die Arbeit eines **Mitglieds oder Referenten / einer Referentin des Nationalen Normenkontrollrats (NKR)** nach dem Gesetz über die Einsetzung eines Nationalen Normenkontrollrats (**NKRG vom 14.08.2006, BGBl. I S. 1866**) in der jeweils geltenden Fassung.

Es bildet den vollständigen Prüfzyklus eines Vorhabens ab: von der **Eingangstriage** eines Referentenentwurfs über die **Erfuellungsaufwand-Berechnung** nach Standardkostenmodell (SKM) und die **Prüfraster** des NKR bis zur **Stellungnahme** nach § 6 NKRG.

## Mandatsperspektive

Das Plugin schreibt aus der Sicht des **NKR-Prüfers**, nicht aus Ressortsicht. Es geht **nicht** darum, einen Entwurf zu verteidigen, sondern darum, ihn nach den NKR-Kriterien zu prüfen und ggf. **kritisch zu kommentieren**.

Leitsatz: *"Wenn nicht noetig, dann nicht regeln; wenn noetig, dann so einfach, so digital, so mittelstandsfreundlich und so evaluationsfest wie möglich."*

## Aufbau

Das Plugin enthaelt 37 Skills in fuenf Clustern:

```
A — Grundlagen, Verfahren, Mandat (7 Skills)
   nkr-orientierung-und-mandatsaufnahme
   nkr-aufgabe-und-kompetenz-nkrg
   nkr-pruefumfang-was-prueft-der-nkr-nicht
   nkr-verfahrensgang-referentenentwurf-bis-bundestag
   nkr-zusammenarbeit-mit-bundesregierung-und-ressorts
   nkr-eu-ebene-und-better-regulation
   nkr-evaluation-und-jahresbericht

B — Erfuellungsaufwand-Methodik (8 Skills)
   nkr-erfuellungsaufwand-grundbegriff
   nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung
   nkr-standardkostenmodell-skm
   nkr-zeitwerttabelle-und-fallzahlen
   nkr-einmalig-vs-jaehrlich-laufend
   nkr-buerokratiekosten-vs-erfuellungsaufwand
   nkr-fallzahlen-schaetzung-bandbreiten
   nkr-leitfaden-ermittlung-und-darstellung

C — Pruefraster (8 Skills)
   nkr-erforderlichkeitspruefung-warum-ueberhaupt-regeln
   nkr-alternativen-pruefung-keine-regelung-soft-law
   nkr-verhaeltnismaessigkeit-aus-nkr-sicht
   nkr-mittelstandsfreundlichkeit-kmu-test
   nkr-praktikabilitaet-vollzug-test
   nkr-evaluierung-befristung-sunset-klausel
   nkr-digital-anschlussfaehigkeit-tauglich
   nkr-one-in-one-out-bilanz-und-buchung

D — Stellungnahme-Drafting (8 Skills)
   nkr-stellungnahme-aufbau-und-format
   nkr-stellungnahme-grundsatzfeststellung
   nkr-stellungnahme-ergebnis-und-empfehlung
   nkr-formulierungshilfe-vs-referentenentwurf-referentenentwurf
   nkr-stellungnahme-zum-bundestag-anhoerung
   nkr-stellungnahme-evaluationsklausel-vorschlag
   nkr-stellungnahme-mahnender-charakter-grenzen
   nkr-stellungnahme-pressepolitik-und-jahresbericht

E — Spezialfaelle / komplexe Themen (6 Skills)
   nkr-digitalcheck-und-onlinezugangsgesetz-ozg
   nkr-eu-richtlinien-umsetzung-und-goldplating
   nkr-handelsregister-und-elektronische-zustellung
   nkr-nachhaltigkeit-klimacheck-und-vereinbarkeit
   nkr-gleichstellungs-und-gendercheck
   nkr-buerokratieabbau-katalog-konkrete-vorschlaege
```

## Methodische Grundlagen (Pflicht-Bezugnahmen)

- **NKRG** vom 14.08.2006 (BGBl. I S. 1866) in der jeweils geltenden Fassung
- **GGO** insbesondere § 44 (Prüfung der Gesetzesfolgen) und § 45 (Erfuellungsaufwand-Darstellung)
- **Handbuch der Rechtsfoermlichkeit (HdR)** als Drafting-Grundlage
- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR)
- **Standardkostenmodell (SKM)** als NKR-Methodik
- **One-in-one-out-Regel** (Beschluss der Bundesregierung 2015)
- **Digitalcheck** (seit 2022)
- **OZG** und OZG-Folgeregulierung (Stand vom Anwender zu verifizieren)
- **EU Better Regulation** der EU-Kommission

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte unter [`nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/`](../testakten/nkr-elektronische-erreichbarkeit-handelsregister-gesellschaften-2026/).

**Sachverhalt**: Referentenentwurf des BMJ vom 14.04.2026 zur Verbesserung der elektronischen Erreichbarkeit im Handelsregister eingetragener Gesellschaften (**ElErrHandRegG**). NKR-Prüfung ergibt: Regelung ist erforderlich, Ausgestaltung jedoch zu komplex; geschaetzter Erfuellungsaufwand 320 Mio EUR jaehrlich für die Wirtschaft. Stellungnahme weist die Notwendigkeit positiv aus, kritisiert die konkrete Ausgestaltung und schlägt eine zentrale Loesung vor.

Die Akte zeigt sowohl die **mahnende** als auch die **konstruktive** Funktion des NKR.

## Quellenhygiene

- Keine erfundenen NKR-Stellungnahme-Aktenzeichen oder Berichte aus Modellwissen.
- NKRG und methodische Grundlagen werden mit Norm und Stand zitiert; NKR-Jahresberichte allgemein als "NKR-Jahresbericht <Jahr>".
- Vor Ausgabe stets Live-Quellen prüfen: [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de), BMI-Leitfaden, Bundesanzeiger.

## Installation

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install normenkontrollrat-nkr@claude-fuer-deutsches-recht
```

## Konversationsstil

Erste Antwort knapp. Maximal eine gezielte Rueckfrage zur Mandatsaufnahme. Sofort in den Prüfraster-Modus übergehen und einen ersten Stellungnahme-Entwurf liefern, sobald Eckdaten vorliegen. Subsumtion und ausführliche Begründung nur dort, wo der Skill dies ausdruecklich vorsieht (Erforderlichkeit, Verhältnismäßigkeit, Alternativenpruefung).

## Verwandte Plugins

- [`legistik-werkstatt/`](../legistik-werkstatt/) — Drafting-Werkstatt für Referenten- und Kabinettsentwuerfe (Ressortsicht; NKR ist der Prüfer dieser Entwuerfe).
- [`normenkontrolle-bauleitplanung/`](../normenkontrolle-bauleitplanung/) — Anfechtung von Bauleitplaenen nach § 47 VwGO (begriffliche Verwandtschaft, nicht inhaltlich).
- [`buerokratieversteher-entbuerokratisierer/`](../buerokratieversteher-entbuerokratisierer/) — operative Entbuerokratisierung in einzelnen Verfahren.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `orientierung-mandatsaufnahme-praktikabilitaet`, `orientierung-und-mandatsaufnahme` |
| 2. Unterlagen, Sachverhalt und Quellen | `stellungnahme-mahnender-charakter-grenzen` |
| 3. Prüfung, Anspruch und Subsumtion | `digital-anschlussfaehigkeit-digitalcheck`, `digitalcheck-und-onlinezugangsgesetz-ozg`, `einmalig-vs-erforderlichkeitspruefung-warum`, `erforderlichkeitspruefung-warum`, `erforderlichkeitspruefung-warum-ueberhaupt-regeln`, `gleichstellungs-gendercheck-handelsregister`, `gleichstellungs-und-gendercheck`, `nachhaltigkeit-klimacheck-one`, `nachhaltigkeit-klimacheck-vereinbarkeit`, `nkr-alternativen-pruefung-keine-regelung-soft-law` |
| 4. Gestaltung, Strategie und Verhandlung | `evaluierung-befristung-sunset-klausel`, `stellungnahme-evaluationsklausel` |
| 5. Verfahren, Behörde und Gericht | `evaluierung-befristung-verfahrensgang`, `handelsregister-elektronische-zustellung`, `handelsregister-und-elektronische-zustellung`, `verfahrensgang-referentenentwurf`, `verfahrensgang-referentenentwurf-bis-bundestag` |
| 6. Ergebnis, Schreiben und Kommunikation | `evaluation-jahresbericht-fallzahlen`, `evaluation-und-jahresbericht`, `nkr-stellungnahme-zum-bundestag-anhoerung`, `stellungnahme-aufbau-ergebnis`, `stellungnahme-aufbau-und-format`, `stellungnahme-ergebnis-und-empfehlung`, `stellungnahme-formulierungshilfe-vs-referentenentwurf`, `stellungnahme-grundsatzfeststellung`, `stellungnahme-pressepolitik-bundestag`, `stellungnahme-pressepolitik-jahresbericht`, `stellungnahme-zum-bundestag-anhoerung` |
| 8. Spezialmodule und Schnittstellen | `allgemein`, `alternativen-keine-aufgabe-kompetenz`, `alternativen-keine-regelung-soft-law`, `aufgabe-und-kompetenz-nkrg`, `buerokratieabbau-katalog-konkrete`, `buerokratiekosten-vs-erfuellungsaufwand`, `digital-anschlussfaehigkeit-tauglich`, `einmalig-vs-jaehrlich-laufend`, `erfuellungsaufwand-buerger-grundbegriff`, `erfuellungsaufwand-buerger-wirtschaft`, `erfuellungsaufwand-grundbegriff`, `eu-ebene-eu-richtlinien`, `eu-ebene-und-better-regulation`, `eu-richtlinien-umsetzung-und-goldplating`, `fallzahlen-schaetzung-bandbreiten`, `leitfaden-ermittlung`, `leitfaden-ermittlung-und-darstellung`, `mittelstandsfreundlichkeit-kmu-test`, ... plus 14 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 63 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Wenn es um Normenkontrollrat-NKR — Einstieg und Routing in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit... |
| `alternativen-keine-aufgabe-kompetenz` | Wenn es um NKR-Alternativen-Prüfung — Verzicht, Soft-Law, Vollzug in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `alternativen-keine-regelung-soft-law` | Wenn es um NKR-Alternativen-Prüfung — Verzicht, Soft-Law, Vollzug in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `aufgabe-und-kompetenz-nkrg` | Wenn es um NKR-Aufgabe und Kompetenz nach NKRG in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `buerokratieabbau-katalog-konkrete` | Wenn es um NKR-Buerokratieabbau-Katalog — konkrete Vorschlaege in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| `buerokratiekosten-vs-erfuellungsaufwand` | Wenn es um NKR-Buerokratiekosten vs. Erfuellungsaufwand in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsproduk... |
| `digital-anschlussfaehigkeit-digitalcheck` | Wenn es um NKR-Digitaltauglichkeit / Digital-Anschlussfaehigkeit in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit S... |
| `digital-anschlussfaehigkeit-tauglich` | Wenn es um NKR-Digitaltauglichkeit / Digital-Anschlussfaehigkeit in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit S... |
| `digitalcheck-und-onlinezugangsgesetz-ozg` | Wenn es um NKR-Digitalcheck und Onlinezugangsgesetz (OZG) in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortsc... |
| `einmalig-vs-erforderlichkeitspruefung-warum` | Wenn es um NKR-Einmalig vs. jaehrlich laufend in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit G... |
| `einmalig-vs-jaehrlich-laufend` | Wenn es um NKR-Einmalig vs. jaehrlich laufend in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüf... |
| `erforderlichkeitspruefung-warum` | Wenn es um NKR-Erforderlichkeitspruefung — Warum ueberhaupt regeln in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `erforderlichkeitspruefung-warum-ueberhaupt-regeln` | Wenn es um NKR-Erforderlichkeitspruefung — Warum ueberhaupt regeln in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `erfuellungsaufwand-buerger-grundbegriff` | Wenn es um NKR-Erfuellungsaufwand für Buerger, Wirtschaft und Verwaltung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoamp... |
| `erfuellungsaufwand-buerger-wirtschaft` | Wenn es um NKR-Erfuellungsaufwand für Buerger, Wirtschaft und Verwaltung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoamp... |
| `erfuellungsaufwand-grundbegriff` | Wenn es um NKR-Erfuellungsaufwand — Grundbegriff in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eu-ebene-eu-richtlinien` | Wenn es um NKR-EU-Ebene und Better Regulation in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und N... |
| `eu-ebene-und-better-regulation` | Wenn es um NKR-EU-Ebene und Better Regulation in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und N... |
| `eu-richtlinien-umsetzung-und-goldplating` | Wenn es um NKR-EU-Richtlinienumsetzung und Goldplating-Vermeidung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `evaluation-jahresbericht-fallzahlen` | Wenn es um NKR-Evaluation und Jahresbericht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kon... |
| `evaluation-und-jahresbericht` | Wenn es um NKR-Evaluation und Jahresbericht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `evaluierung-befristung-sunset-klausel` | Wenn es um NKR-Evaluierung, Befristung, Sunset-Klausel in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschri... |
| `evaluierung-befristung-verfahrensgang` | Wenn es um NKR-Evaluierung, Befristung, Sunset-Klausel in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschri... |
| `fallzahlen-schaetzung-bandbreiten` | Wenn es um NKR-Fallzahlen — Schaetzung und Bandbreiten in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annah... |
| `gleichstellungs-gendercheck-handelsregister` | Wenn es um NKR-Gleichstellungs- und Gendercheck in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. A... |
| `gleichstellungs-und-gendercheck` | Wenn es um NKR-Gleichstellungs- und Gendercheck in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. A... |
| `handelsregister-elektronische-zustellung` | Wenn es um NKR-Handelsregister und elektronische Zustellung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen,... |
| `handelsregister-und-elektronische-zustellung` | Wenn es um NKR-Handelsregister und elektronische Zustellung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen,... |
| `leitfaden-ermittlung` | Wenn es um NKR-Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Ri... |
| `leitfaden-ermittlung-und-darstellung` | Wenn es um NKR-Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Ri... |
| `mittelstandsfreundlichkeit-kmu-test` | Wenn es um NKR-Mittelstandsfreundlichkeit / KMU-Test in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahme... |
| `nachhaltigkeit-klimacheck-one` | Wenn es um NKR-Nachhaltigkeit, Klimacheck und Vereinbarkeit in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| `nachhaltigkeit-klimacheck-vereinbarkeit` | Wenn es um NKR-Nachhaltigkeit, Klimacheck und Vereinbarkeit in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| `nkr-alternativen-pruefung-keine-regelung-soft-law` | Wenn es um NKR-Alternativen-Pruefung — Verzicht, Soft-Law, Vollzug in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung` | Wenn es um NKR-Erfuellungsaufwand fuer Buerger, Wirtschaft und Verwaltung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoam... |
| `nkr-pruefumfang-was-prueft-der-nkr-nicht` | Wenn es um NKR-Pruefumfang — was prueft der NKR nicht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschrit... |
| `nkr-stellungnahme-zum-bundestag-anhoerung` | Wenn es um NKR-Stellungnahme zum Bundestag (Anhoerung) in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschri... |
| `nkr-verhaeltnismaessigkeit-aus-nkr-sicht` | Wenn es um NKR-Verhaeltnismaessigkeit aus NKR-Sicht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nkr-zusammenarbeit-mit-bundesregierung-und-ressorts` | Wenn es um Verhaltens-Skill für die taegliche Zusammenarbeit zwischen NKR-Sekretariat und Ressorts in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefe... |
| `one-in-one-out-bilanz-und-buchung` | Wenn es um NKR-One-in-one-out — Bilanz und Buchung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten... |
| `one-in-out-bilanz-und-buchung` | Wenn es um NKR-One-in-one-out — Bilanz und Buchung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten... |
| `orientierung-mandatsaufnahme-praktikabilitaet` | Wenn es um NKR-Orientierung und Mandatsaufnahme in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. A... |
| `orientierung-und-mandatsaufnahme` | Wenn es um NKR-Orientierung und Mandatsaufnahme in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. A... |
| `praktikabilitaet-vollzug-test` | Wenn es um NKR-Praktikabilitaet im Vollzug in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pruefumfang-was-prueft-der-nicht` | Wenn es um NKR-Prüfumfang — was prüft der NKR nicht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritte... |
| `pruefumfang-was-standardkostenmodell-skm` | Wenn es um NKR-Prüfumfang — was prüft der NKR nicht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritte... |
| `standardkostenmodell-skm` | Wenn es um NKR-Standardkostenmodell (SKM) in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `stellungnahme-aufbau-ergebnis` | Wenn es um NKR-Stellungnahme — Aufbau und Format in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Be... |
| `stellungnahme-aufbau-und-format` | Wenn es um NKR-Stellungnahme — Aufbau und Format in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Be... |
| `stellungnahme-ergebnis-und-empfehlung` | Wenn es um NKR-Stellungnahme — Ergebnis und Empfehlung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschri... |
| `stellungnahme-evaluationsklausel` | Wenn es um NKR-Stellungnahme — Vorschlag einer Evaluationsklausel in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `stellungnahme-formulierungshilfe-vs-referentenentwurf` | Wenn es um NKR-Formulierungshilfe vs. Referentenentwurf in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsproduk... |
| `stellungnahme-grundsatzfeststellung` | Wenn es um NKR-Stellungnahme — Grundsatzfeststellung in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stellungnahme-mahnender-charakter-grenzen` | Wenn es um NKR-Stellungnahme — Mahnender Charakter und seine Grenzen in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-... |
| `stellungnahme-pressepolitik-bundestag` | Wenn es um NKR-Stellungnahme — Pressepolitik und Jahresbericht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| `stellungnahme-pressepolitik-jahresbericht` | Wenn es um NKR-Stellungnahme — Pressepolitik und Jahresbericht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| `stellungnahme-zum-bundestag-anhoerung` | Wenn es um NKR-Stellungnahme zum Bundestag (Anhörung) in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschrit... |
| `verfahrensgang-referentenentwurf` | Wenn es um NKR-Verfahrensgang Referentenentwurf bis Bundestag in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofo... |
| `verfahrensgang-referentenentwurf-bis-bundestag` | Wenn es um NKR-Verfahrensgang Referentenentwurf bis Bundestag in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofo... |
| `verhaeltnismaessigkeit-aus-sicht` | Wenn es um NKR-Verhältnismäßigkeit aus NKR-Sicht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.... |
| `verhaeltnismaessigkeit-sicht-zeitwerttabelle` | Wenn es um NKR-Verhältnismäßigkeit aus NKR-Sicht in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.... |
| `zeitwerttabelle-und-fallzahlen` | Wenn es um NKR-Zeitwerttabelle und Fallzahlen in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und K... |
| `zusammenarbeit-bundesregierung-ressorts` | Wenn es um NKR-Zusammenarbeit mit Bundesregierung und Ressorts in Normenkontrollrat (NKR) — Prüfung von Gesetzentwuerfen geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalatio... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
