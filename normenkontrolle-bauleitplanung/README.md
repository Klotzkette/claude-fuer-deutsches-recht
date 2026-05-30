# Normenkontrolle Bauleitplanung — § 47 VwGO

Freistehendes Plugin für die Prüfung und gerichtliche Anfechtung von **Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften** im Normenkontrollverfahren nach § 47 VwGO vor dem **Bayerischen Verwaltungsgerichtshof (BayVGH)** und anderen Oberverwaltungsgerichten.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| normenkontrolle-bauleitplanung | [normenkontrolle-bauleitplanung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/normenkontrolle-bauleitplanung.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **— Bebauungsplan Augsburg-Bahnhofsareal** ([`testakten/bebauungsplan-augsburg-bahnhofsareal/`](../testakten/bebauungsplan-augsburg-bahnhofsareal/)).

Direkt-Download als ZIP: [testakte-bebauungsplan-augsburg-bahnhofsareal.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bebauungsplan-augsburg-bahnhofsareal.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 22 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abwaegungsgebot-1-abs-7-baugb` | Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vier Abwaegungsfehler-Stufen Abwaegungsausfall Abwaegungsdefizit Abwaegungsfehleinschaetzung Abwaegungsdisproportionali... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren... |
| `anpassungsgebot-flaechennutzungsplan` | Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet Konflikt FNP-Darstellung... |
| `antragsbefugnis-eigentuemer-nachbar` | Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Massstab Eigentuemer im Plangebiet im... |
| `artenschutz-naturschutz-planung` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP) CEF-Massnahmen Eingri... |
| `aufstellungsbeschluss-bekanntmachung` | Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs. 1 Beschluss als Sa... |
| `beteiligung-frueh-foermlich` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behoerdenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1 Monat Behoerdenbete... |
| `buergerversammlung-protokoll-audit` | Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege sinngemäße Niederschrift Vo... |
| `einstweilige-anordnung-47-abs-6-vwgo` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Massstab Eilbedürftigkeit Baugenehmigung b... |
| `erforderlichkeit-1-abs-3-baugb` | Workflow-Skill zu erforderlichkeit 1 abs 3 baugb. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `festsetzungskatalog-9-baugb-baunvo` | Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche Nutzung GRZ GFZ Voll... |
| `immissionsschutz-laerm-bauleitplanung` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik Worstcase Trennungsgrundsat... |
| `jahresfrist-47-abs-2-vwgo` | Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB fehlerhafte Bekanntmac... |
| `mandat-erstgespraech-normenkontrolle` | Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist Statthaftigkeit Erstprüfung Plan... |
| `muendliche-verhandlung-vgh-strategie` | Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche Beweisanträge Ortsbesichtig... |
| `normenkontrollantrag-schriftsatz` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis) Verfahrensfehler Erf... |
| `planerhaltung-214-215-baugb` | Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche Fehler § 215 BauGB Rue... |
| `statthaftigkeit-47-vwgo` | Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12 BauGB § 13a-B-Plan ör... |
| `stellplatzsatzung-bay-bauordnung` | Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch örtliche Bauvorschrif... |
| `umweltbericht-umweltpruefung` | Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden Wasser Luft Klima Landsc... |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung Dauer 2 plus 1 plus... |
| `vorhabenbezogener-bebauungsplan-12-baugb` | Workflow-Skill zu vorhabenbezogener bebauungsplan 12 baugb. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
