# Normenkontrolle Bauleitplanung — § 47 VwGO

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`normenkontrolle-bauleitplanung.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/normenkontrolle-bauleitplanung.md) (76 KB)
- Im Repo: [`testakten/megaprompts/normenkontrolle-bauleitplanung.md`](../testakten/megaprompts/normenkontrolle-bauleitplanung.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`normenkontrolle-bauleitplanung`) | [`normenkontrolle-bauleitplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrolle-bauleitplanung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte — Bebauungsplan Augsburg-Bahnhofsareal** (`bebauungsplan-augsburg-bahnhofsareal`) | [Gesamt-PDF lesen](../testakten/bebauungsplan-augsburg-bahnhofsareal/gesamt-pdf/bebauungsplan-augsburg-bahnhofsareal_gesamt.pdf) | [`testakte-bebauungsplan-augsburg-bahnhofsareal.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bebauungsplan-augsburg-bahnhofsareal.zip) |
| **Normenkontrolle B-Plan XV-43d „Spreepark Friedrichshain" — Bürgerinitiative Tannengarten gegen Land Berlin** (`normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten`) | [Gesamt-PDF lesen](../testakten/normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten/gesamt-pdf/normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten_gesamt.pdf) | [`testakte-normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-normenkontrolle-bplan-spreepark-friedrichshain-buergerinitiative-tannengarten.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Prüfung und gerichtliche Anfechtung von **Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften** im Normenkontrollverfahren nach § 47 VwGO vor dem **Bayerischen Verwaltungsgerichtshof (BayVGH)** und anderen Oberverwaltungsgerichten.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `normenkontrolle-bauleitplanung.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe diesen Bebauungsplan auf formelle und materielle Fehler.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install normenkontrolle-bauleitplanung@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Normenkontrolle außerhalb der Bauleitplanung

Das Plugin ist nicht nur für Bebauungspläne gedacht. § 47 VwGO kann auch kommunale Satzungen und landesrechtliche Rechtsverordnungen erfassen, soweit das jeweilige Landesrecht die Normenkontrolle eröffnet. Deshalb prüft das Plugin nun ausdrücklich auch Kommunalabgaben-, Beitrags-, Benutzungs-, Friedhofs-, Kita-, Polizei-/Gefahrenabwehr- und sonstige Satzungen sowie die Abgrenzung zur bloßen Inzidentkontrolle im Verfahren gegen einen Einzelbescheid.

## Mandatsperspektive

Anwältin der Antragstellerseite — Eigentümer, Nachbarn, anerkannte Naturschutzverbände, Gemeinden gegen übergeordnete Planung. Schwerpunkt: aus der angegriffenen Satzung die formellen und materiellen Fehler herausarbeiten und vor dem OVG/VGH zur Unwirksamkeitserklärung bringen.

## Aufbau

Der Lebenszyklus eines Normenkontroll-Mandats läuft in vier Phasen:

```
Phase A — Mandat und Zulässigkeit
  └─ Erstgespräch → Statthaftigkeit → Antragsbefugnis → Jahresfrist

Phase B — Verfahrensfehler-Audit (formell)
  └─ Aufstellungsbeschluss → Beteiligungen → Bürgerversammlung
     → Umweltbericht → Planerhaltung §§ 214/215 BauGB

Phase C — Materielle Fehler
  └─ Erforderlichkeit § 1 Abs. 3 → Abwägungsgebot § 1 Abs. 7
     → Stellplätze → Lärm/Immissionsschutz → Artenschutz
     → Anpassung Flächennutzungsplan

Phase D — Verfahren BayVGH/OVG
  └─ Normenkontrollantrag → Eilantrag § 47 Abs. 6 VwGO
     → Mündliche Verhandlung
```

## Enthaltene Skills

### Phase A — Mandat und Zulässigkeit (4 Skills)

| Slug | Beschreibung |
|---|---|
| `mandat-erstgespraech-normenkontrolle` | Erstgespräch, Mandantenbetroffenheit, Erfolgsaussichten-Prognose, Kosten |
| `statthaftigkeit-47-vwgo` | Antragsgegenstand B-Plan/FNP/örtliche Bauvorschrift, Landesrecht im Rang unter Landesgesetz |
| `antragsbefugnis-eigentuemer-nachbar` | § 47 Abs. 2 VwGO Möglichkeitstheorie, Eigentum, abwägungserheblicher Belang, Verbandsklage |
| `jahresfrist-47-abs-2-vwgo` | Fristlauf ab Bekanntmachung, Wiedereinsetzung, Heilung durch ergänzendes Verfahren |

### Phase B — Verfahrensfehler-Audit (5 Skills)

| Slug | Beschreibung |
|---|---|
| `aufstellungsbeschluss-bekanntmachung` | § 2 Abs. 1, § 10 Abs. 3 BauGB Verfahrenskette, Anstoßfunktion |
| `beteiligung-frueh-foermlich` | §§ 3 Abs. 1, 3 Abs. 2, 4 Abs. 1, 4 Abs. 2 BauGB Behörden- und Öffentlichkeitsbeteiligung |
| `buergerversammlung-protokoll-audit` | Erörterungstermin, Behandlung Einwendungen, Vorfestlegungsverbot |
| `umweltbericht-umweltpruefung` | § 2 Abs. 4 BauGB, § 2a BauGB, UVPG-Verzahnung, FFH-Vorprüfung |
| `planerhaltung-214-215-baugb` | Beachtlichkeit, Rügefrist 1 Jahr, ergänzendes Verfahren § 214 Abs. 4 BauGB |

### Phase C — Materielle Fehler (9 Skills)

| Slug | Beschreibung |
|---|---|
| `erforderlichkeit-1-abs-3-baugb` | Planrechtfertigung, städtebauliches Konzept, Gefälligkeitsplanung |
| `abwaegungsgebot-1-abs-7-baugb` | Abwägungsausfall, Abwägungsdefizit, Fehlgewichtung, Disproportionalität |
| `stellplatzsatzung-bay-bauordnung` | Art. 47 BayBO Stellplatzpflicht, Reduzierung durch Satzung, Mobilitätskonzept |
| `immissionsschutz-laerm-bauleitplanung` | DIN 18005, TA Lärm, Trennungsgebot § 50 BImSchG, Schallschutzgutachten-Prüfung |
| `artenschutz-naturschutz-planung` | § 44 BNatSchG saP, FFH-Vorprüfung, Eingriffsregelung § 1a BauGB |
| `anpassungsgebot-flaechennutzungsplan` | § 8 Abs. 2 BauGB Entwicklungsgebot, Parallelverfahren, FNP-Berichtigung |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `festsetzungskatalog-9-baugb-baunvo` | Abschließender § 9-Katalog, BauNVO-Höchstgrenzen, dynamische Verweisungen, Bahnflächen § 38 BauGB |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | § 14 Sperre, § 15 Zurückstellung, Entschädigung § 18, vertraglich-faktische Sperre |

### Phase D — Verfahren BayVGH/OVG (3 Skills)

| Slug | Beschreibung |
|---|---|
| `normenkontrollantrag-schriftsatz` | Aufbau, Antragsformulierung, Begründungsstruktur, Streitwert |
| `einstweilige-anordnung-47-abs-6-vwgo` | Vollzugsfolgenabwägung, Eilbedürftigkeit, Antragsbefugnis im Eilverfahren |
| `muendliche-verhandlung-vgh-strategie` | Vorbereitung, Beweisanträge, Plädoyer, Wirkungsausspruch |

## Vorlagen

- `assets/templates/normenkontrolle-mandatskarte.md` — Übersichtskarte für jedes Normenkontroll-Mandat
- `assets/templates/fehleraudit-checkliste.md` — Systematische Prüfreihenfolge formell vor materiell

## Bedienungshinweis

Das Plugin ist freistehend nutzbar und benötigt keine anderen Plugins des Marketplaces. Für umweltrechtliche Querfragen (FFH, saP, UVP) kann das Plugin `umweltrecht` ergänzend geladen werden, für allgemeine Verwaltungsverfahrensfragen das Plugin `verwaltungsrecht`.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 91 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abwaegung-formular-portal` | Abwaegung: Formular, Portal und Einreichungslogik: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion ode... |
| `abwaegung-formular-portal-und-einreichung` | Abwaegung: Formular, Portal und Einreichungslogik. |
| `abwaegungsgebot-1-abs-7-baugb` | Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vier Abwaegungsfehler-Stufen Abwaegungsausfall Abwaegungsdefizit Abwaegungsfehleinschaetzung Abwaegungsdisproportionali... |
| `anfechtung-antragsbefugnis-red-team-korrektur` | Anfechtung: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `anfechtung-tatbestandsmerkmale` | Anfechtung: Tatbestandsmerkmale, Beweisfragen und Beleglage: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sa... |
| `anpassungsgebot-flaechennutzungsplan` | Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet Konflikt FNP-Darstellung... |
| `anschluss-routing` | Anschluss-Routing für Normenkontrolle Bauleitplanung: wählt den nächsten Spezial-Skill nach Engpass (§ 47 II VwGO 1 Jahr ab Bekanntmachung, Bebauungsplan, Begründung, Abwägungsmaterial), dokumentiert Router-Entscheidung mit Begründung. |
| `antragsbefugnis-eigentuemer-nachbar` | Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Maßstab Eigentümer im Plangebiet im... |
| `antragsbefugnis-fehlerkatalog` | Antragsbefugnis Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `antragsbefugnis-red-team-und-qualitaetskontrolle` | Antragsbefugnis: Red-Team und Qualitätskontrolle. |
| `antragstellervertretung-zahlen-schwellen-und-berechnung` | Antragstellervertretung: Zahlen, Schwellenwerte und Berechnung. |
| `artenschutz-naturschutz-aufstellungsbeschluss` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP) CEF-Maßnahmen Eingri... |
| `artenschutz-naturschutz-planung` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP) CEF-Maßnahmen Eingri... |
| `aufstellungsbeschluss-bekanntmachung` | Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs. 1 Beschluss als Sa... |
| `aufstellungsbeschluss-mandantenentscheidun-02` | Aufstellungsbeschluss: Mandantenkommunikation und Entscheidungsvorlage: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle,... |
| `aufstellungsbeschluss-mandantenentscheidung` | Aufstellungsbeschluss: Mandantenkommunikation und Entscheidungsvorlage. |
| `bauleitplanung-interessen` | Bauleitplanung: Mehrparteienkonflikt und Interessenmatrix: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sank... |
| `bauleitplanung-mehrparteien-konflikt-und-interessen` | Bauleitplanung: Mehrparteienkonflikt und Interessenmatrix. |
| `bauvorschriften-behoerden` | Bauvorschriften: Behörden-, Gerichts- oder Registerweg: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktio... |
| `bauvorschriften-behoerden-gericht-und-registerweg` | Bauvorschriften: Behörden-, Gerichts- oder Registerweg. |
| `bayvgh-bekanntmachung-beweislast-eilantrag` | Bayvgh: Verhandlung, Vergleich und Eskalation. |
| `bayvgh-verhandlung-vergleich` | Bayvgh: Verhandlung, Vergleich und Eskalation: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Ve... |
| `bebauungsplaenen-kommunalabgaben` | Bebauungsplaenen: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `bekanntmachung-beweislast-darlegungslast` | Bekanntmachung: Beweislast, Darlegungslast und Substantiierung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung,... |
| `bekanntmachung-beweislast-und-darlegungslast` | Bekanntmachung: Beweislast, Darlegungslast und Substantiierung. |
| `benutzungssatzung-kommunale-einrichtung` | Benutzungssatzungen kommunaler Einrichtungen: Markthalle, Friedhof, Kita, Bibliothek, Sportanlage, Hausrecht und Grundrechte.; Normanker: VwGO § 47; Kommunalordnungen; Grundrechte; Gebührenrecht; macht § 47 VwGO als allgemeines Satzungs-... |
| `beteiligung-frueh-buergerversammlung` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behördenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1 Monat Behördenbeteil... |
| `beteiligung-frueh-foermlich` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behördenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1 Monat Behördenbeteil... |
| `buergerversammlung-protokoll-audit` | Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege sinngemäße Niederschrift Vo... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `compliance-dokumentation-aktenvermerk` | Normenkontrolle: Compliance-Dokumentation und Aktenvermerk: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, San... |
| `dokumente-intake` | Dokumentenintake für Normenkontrolle Bauleitplanung: sortiert Bebauungsplan, Begründung, Abwägungsmaterial, prüft Datum, Absender, Frist und Beweiswert (Abwägungsfehler-Dokumentation, Bürgerbeteiligung Protokolle); markiert Lücken; berüc... |
| `eilantrag-47-abs-6-ausserhalb-baurecht` | Eilantrag nach § 47 Abs. 6 VwGO außerhalb des Baurechts: schwere Nachteile, wichtige Gründe, Vollzugsfolgen und Antragsstrategie.; Normanker: VwGO § 47 Abs. 6; Grundrechtsbezug; Folgenabwägung; macht § 47 VwGO als allgemeines Satzungs- u... |
| `eilantrag-47-abs-6-vwgo` | Eilantrag nach § 47 Abs. 6 VwGO: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Normenkontrolle Bauleitplanung. |
| `einstieg-routing` | Einstieg, Triage und Routing für Normenkontrolle Bauleitplanung: ordnet Rolle (Antragsteller (Anwohner/Nachbargemeinde), Gemeinde, OVG), markiert Frist (§ 47 II VwGO 1 Jahr ab Bekanntmachung), wählt Norm (BauGB §§ 1/2/10, § 47 VwGO Norme... |
| `einstweilige-anordnung-47-abs-6-vwgo` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Maßstab Eilbedürftigkeit Baugenehmigung b... |
| `einstweilige-anordnung-erforderlichkeit-abs` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Maßstab Eilbedürftigkeit Baugenehmigung b... |
| `erforderlichkeit-1-abs-3-baugb` | Prüfungslinie für erforderlichkeit 1 abs 3 baugb im Normenkontrolle Bauleitplanung. |
| `festsetzungskatalog-9-baugb-baunvo` | Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche Nutzung GRZ GFZ Voll... |
| `flaechennutzungsplaenen-normenkontrolle` | Flaechennutzungsplaenen: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `fristen-und-risikoampel` | Fristen- und Risikoampel: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `immissionsschutz-laerm-bauleitplanung` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik Worstcase Trennungsgrundsat... |
| `immissionsschutz-laerm-mandat-erstgespraech` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik Worstcase Trennungsgrundsat... |
| `jahresfrist-47-abs-2-vwgo` | Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB fehlerhafte Bekanntmac... |
| `jahresfrist-abs-nkbl-verfahren` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Normenkontrolle Bauleitplanung. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `kommunalabgaben-und-beitragssatzungen` | Kommunalabgaben- und Beitragssatzungen: Gebühren, Beiträge, Fremdenverkehr, Abwasser, Elternbeiträge, Kalkulation und Gleichheitssatz.; Normanker: VwGO § 47; KAG der Länder; Art. 3 GG; Äquivalenz- und Kostendeckungsprinzip; macht § 47 Vw... |
| `mandat-erstgespraech-normenkontrolle` | Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist Statthaftigkeit Erstprüfung Plan... |
| `mandatsperspektive-quellenkarte` | Mandatsperspektive Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `muendliche-verhandlung-vgh-strategie` | Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche Beweisanträge Ortsbesichtig... |
| `nkbl-abwaegungsfehler-bauleitplanung` | Spezialfall Abwaegungsfehler in der Bauleitplanung: Abwaegungsausfall, -defizit, -fehleinschaetzung, Disproportionalitaet. Prüfraster für Klage im Normenkontrolle Bauleitplanung. |
| `nkbl-abwaegungsfehler-spezial` | Spezialfall Abwaegungsfehler in der Bauleitplanung: Abwaegungsausfall, -defizit, -fehleinschaetzung, Disproportionalitaet. Prüfraster für Klage. |
| `nkbl-bauleitplanung-bauleiter` | Bauleiter Bauleitplanung BauGB: Flaechennutzungsplan, Bebauungsplan, Verfahrensarten, Beteiligung Oeffentlichkeit. Prüfraster für Gemeinde und Buergerinitiative. |
| `nkbl-buergerentscheid-buergerbegehren-spezial` | Spezialfall Buergerbegehren und Buergerentscheid in der Bauleitplanung: Landesrecht, Quoren, zulaessige Fragen. Prüfraster für Initiative. |
| `nkbl-normenkontrolle-verfahren-leitfaden` | Leitfaden Normenkontrollverfahren § 47 VwGO: Antragsbefugnis, Antragsfrist, Prüfungsumfang. Prüfraster für Antragsteller und Gemeinde. |
| `normenkontrollantrag-normenkontrolle` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis) Verfahrensfehler Erf... |
| `normenkontrollantrag-schriftsatz` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis) Verfahrensfehler Erf... |
| `normenkontrolle-antragstellervertretung-47vwgo` | Antragstellervertretung: Zahlen, Schwellenwerte und Berechnung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung,... |
| `normenkontrolle-bebauungsplan-angriffspunkte` | Bebauungsplaenen: Fristen, Form, Zuständigkeit und Rechtsweg: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, S... |
| `normenkontrolle-compliance-dokumentation-und-akte` | Normenkontrolle: Compliance-Dokumentation und Aktenvermerk. |
| `normenkontrolle-fnp-inzidentkontrolle` | Flaechennutzungsplaenen: Dokumentenmatrix, Lückenliste und Nachforderung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `normenkontrolle-oder-inzidentkontrolle` | Normenkontrolle oder Inzidentkontrolle: wann § 47 VwGO, wann Anfechtung/Verpflichtung/Feststellung gegen Einzelakt.; Normanker: VwGO §§ 42 und 43 und 47; Rechtsschutzbedürfnis; Bestandskraft; macht § 47 VwGO als allgemeines Satzungs- und... |
| `normenkontrolle-satzungsnormenkontrolle` | Allgemeine Satzungsnormenkontrolle nach § 47 VwGO: kommunale Satzungen, Landesrechtsverordnungen, Landesrechtseröffnung und Abgrenzung zur Inzidentkontrolle.; Normanker: VwGO § 47 Abs. 1 Nr. 2; jeweiliges Landesausführungsgesetz; Kommuna... |
| `normenkontrolle-satzungsnormenkontrolle-47-vwgo` | Allgemeine Satzungsnormenkontrolle nach § 47 VwGO: kommunale Satzungen, Landesrechtsverordnungen, Landesrechtseröffnung und Abgrenzung zur Inzidentkontrolle.; Normanker: VwGO § 47 Abs. 1 Nr. 2; jeweiliges Landesausführungsgesetz; Kommuna... |
| `oertlichen-risikoampel` | Oertlichen: Risikoampel, Gegenargumente und Verteidigungslinien: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung... |
| `oertlichen-risikoampel-und-gegenargumente` | Oertlichen: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `output-waehlen` | Output-Wahl für Normenkontrolle Bauleitplanung: stimmt Adressat (Antragsteller (Anwohner/Nachbargemeinde), Gemeinde, OVG), Frist (§ 47 II VwGO 1 Jahr ab Bekanntmachung) und Form auf den Zweck ab — typische Outputs: Normenkontrollantrag,... |
| `planerhaltung-214-215-baugb` | Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche Fehler § 215 BauGB Rue... |
| `planerhaltung-abwaegung` | Planerhaltung, Abwägung und Antragsbefugnis: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Normenkontrolle Bauleitplanung. |
| `planerhaltung-abwaegung-antragsbefugnis` | Planerhaltung, Abwägung und Antragsbefugnis: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `planerhaltung-internationaler` | Planerhaltung: Internationaler Bezug und Schnittstellen: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sankti... |
| `planerhaltung-internationaler-bezug-und-schnittstellen` | Planerhaltung: Internationaler Bezug und Schnittstellen. |
| `polizeiverordnung-gefahrenabwehrsatzung` | Polizeiverordnungen und Gefahrenabwehrsätze: Normadressat, Bestimmtheit, Verhältnismäßigkeit, Ermächtigungsgrundlage und Eilrechtsschutz.; Normanker: VwGO § 47; Polizei-/Ordnungsrecht der Länder; Art. 2 und 8 und 12 und 14 GG; macht § 47... |
| `polizeiverordnung-und-gefahrenabwehrsatzung` | Polizeiverordnungen und Gefahrenabwehrsätze: Normadressat, Bestimmtheit, Verhältnismäßigkeit, Ermächtigungsgrundlage und Eilrechtsschutz.; Normanker: VwGO § 47; Polizei-/Ordnungsrecht der Länder; Art. 2 und 8 und 12 und 14 GG; macht § 47... |
| `pruefung-erstpruefung-und-mandatsziel` | Prüfung: Erstprüfung, Rollenklärung und Mandatsziel. |
| `quellen-livecheck` | Quellen-Live-Check für Normenkontrolle Bauleitplanung: prüft Normen (BauGB §§ 1/2/10, § 47 VwGO Normenkontrolle) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt OVG/VGH und Quellenhygiene nach references/quellenhy... |
| `rechtsfolge-unwirksamkeit-und-bekanntmachung` | Rechtsfolge der Unwirksamkeit: Allgemeinverbindlichkeit, Veröffentlichung, Folgebescheide, Rückabwicklung und Vertrauensschutz.; Normanker: VwGO § 47 Abs. 5; Landesrecht; VwVfG/Spezialrecht; macht § 47 VwGO als allgemeines Satzungs- und... |
| `red-team-satzung-jenseits-baugb` | Red-Team Satzung jenseits BauGB: Ermächtigungsgrundlage, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.; Normanker: VwGO § 47; Kommunalrecht; Art. 3 und 12 und 14 GG; macht § 47 VwGO als allgemei... |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `statthaftigkeit-47-vwgo` | Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12 BauGB § 13a-B-Plan ör... |
| `stellplatzsatzung-bay-bauordnung` | Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch örtliche Bauvorschrif... |
| `umweltbericht-umweltpruefung` | Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden Wasser Luft Klima Landsc... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Normenkontrolle Bauleitplanung: trennt fehlende Tatsachen von fehlenden Belegen (Bebauungsplan, Begründung, Abwägungsmaterial), nennt pro Lücke Beweisthema, Beschaffungsweg (OVG/VGH), Frist und Ersatznac... |
| `veraenderungssperre-zurueckstellung-14-15` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung Dauer 2 plus 1 plus... |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung Dauer 2 plus 1 plus... |
| `vorhabenbezogener-bebauungsplan-12-baugb` | Prüfungslinie für vorhabenbezogener bebauungsplan 12 baugb im Normenkontrolle Bauleitplanung. |
| `vwgo-schriftsatz-brief-memo` | VwGO: Schriftsatz-, Brief- und Memo-Bausteine: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Ve... |
| `vwgo-statthaftigkeit-stellplatzsatzung-bay` | VwGO: Schriftsatz-, Brief- und Memo-Bausteine. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Normenkontrolle Bauleitplanung. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Normenkontrolle Bauleitplanung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
