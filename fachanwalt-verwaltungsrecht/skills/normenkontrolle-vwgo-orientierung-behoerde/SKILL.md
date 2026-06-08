---
name: normenkontrolle-vwgo-orientierung-behoerde
description: "Normenkontrolle Vwgo Orientierung Behörde im Plugin Fachanwalt Verwaltungsrecht: prüft konkret Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder, Orientierung im Fachanwaltsrecht Verwaltungsrecht, Verwaltungsrechts-Vergleich nach § 106 VwGO und. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Normenkontrolle Vwgo Orientierung Behörde

## Arbeitsbereich

**Normenkontrolle Vwgo Orientierung Behörde** ordnet den Fall über die tragenden Prüfungslinien: Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder, Orientierung im Fachanwaltsrecht Verwaltungsrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-verwaltungsrecht-normenkontrolle-47-vwgo` | Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Betroffener will Bebauungsplan oder kommunale Satzung zu Fall bringen. Normen: § 47 VwGO (Normenkontrolle OVG), Art. 14 GG (Eigentumsschutz), § 1 Abs. 7 BauGB (Abwaegungsgebot). Prüfraster: Antragsfrist 1 Jahr ab Inkrafttreten, Antragsbefugnis, OVG-Zuständigkeit, Abwaegungsfehler. Output Normenkontrollantrag-Entwurf. Abgrenzung: Anfechtungsklage gegen einzelnen VA siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Planfeststellung siehe energietrassen-planfeststellung-rechtsschutz. |
| `fachanwalt-verwaltungsrecht-orientierung` | Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberblicken. Normen: VwGO (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage, Eilrechtsschutz §§ 80 und 123 VwGO), VwVfG, Polizei- und Ordnungsrecht, Baurecht. Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht), Verfahrensarten, Fristen-Überblick. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Detailarbeit in Fachmodule; Mandats-Triage siehe mandat-triage-verwaltungsrecht. |
| `fachanwalt-verwaltungsrecht-vergleich-106-vwgo-behoerde` | Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandant will Streit mit Behörde außergerichtlich beilegen. Normen: § 106 VwGO (Prozessvergleich), § 55 VwVfG (Vergleichsvertrag), § 28 VwVfG (Anhörung). Prüfraster: Vergleichsfähigkeit, Mediation VwG, Eroerrterungstermin, Petitionsweg, Protokoll-Anforderungen. Output Vergleichs-Entwurf, Strategie-Memo. Abgrenzung: Klage-Strategie siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Vergleich Vergabe siehe fachanwalt-vergaberecht-Plugin. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-verwaltungsrecht-normenkontrolle-47-vwgo`

**Fokus:** Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Betroffener will Bebauungsplan oder kommunale Satzung zu Fall bringen. Normen: § 47 VwGO (Normenkontrolle OVG), Art. 14 GG (Eigentumsschutz), § 1 Abs. 7 BauGB (Abwaegungsgebot). Prüfraster: Antragsfrist 1 Jahr ab Inkrafttreten, Antragsbefugnis, OVG-Zuständigkeit, Abwaegungsfehler. Output Normenkontrollantrag-Entwurf. Abgrenzung: Anfechtungsklage gegen einzelnen VA siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Planfeststellung siehe energietrassen-planfeststellung-rechtsschutz.

### Normenkontrolle § 47 VwGO

## Zweck

Prüfung untergesetzlicher Rechtsnormen (Bebauungspläne, Satzungen, Rechtsverordnungen).

## 1) Anwendungs-Bereich

### Pruefbare Normen § 47 I VwGO

- Bauleitpläne (Flächennutzungsplan, Bebauungsplan)
- Rechtsverordnungen Land / Kreis / Gemeinde
- Satzungen Gemeinden

### Nicht prüfbare

- Bundesgesetze (BVerfG-Verfahren)
- Verwaltungsvorschriften (im Wirkungsfeld)

## 2) Antragsbefugnis § 47 II VwGO

### Voraussetzung

- Rechts-Beeintraechtigung erkennbar
- Persönliche Betroffenheit
- Nicht jede Beteiligung

### Beispiele

- Grundeigentuemer im B-Plan-Gebiet
- Nachbar bei B-Plan
- Gewerbe bei Sondernutzungs-Satzung

## 3) Frist § 47 II VwGO

- **1 Jahr** nach Bekanntmachung
- Bei Versäumnis: Antrag unzulaessig
- Änderungs-Anträge erneut Frist

## 4) Zuständigkeit OVG

- Oberverwaltungsgericht / Verwaltungsgerichtshof
- Spezialisierte Senate
- Bei Verfahrens-Mangel: Verweisung an VG

## 5) Verfahren

### Schritt 1 — Antrag

- Schriftlich beim OVG
- Bezug auf konkrete Norm
- Antragsbegründung

### Schritt 2 — Anhörung

- Antragsgegner (Plan-Geber)
- Beteiligte

### Schritt 3 — Beweisaufnahme

- Akten-Einsicht
- ggf. Sachverständige

### Schritt 4 — Urteil

- Normenverwerfungs-Urteil
- Bei Erfolg: Norm tritt rueckwirkend außer Kraft
- Allgemein-Verbindlichkeit

## 6) Bauplanungs-Recht Schwerpunkt

### Prüfungsmaßstab

- Pflicht-Inhalte BauGB
- Abwaegungs-Gebot § 1 VII BauGB
- Verhältnismaessigkeit

### Mangel-Quellen

- Abwaegungs-Defizite
- Verfahrens-Mangel (Beteiligungs-Verletzung)
- Materiell rechtswidrige Inhalte

### Heilung § 215 BauGB

- Bestimmte Mangel sind heilbar
- Bei Mangel-Vortrag im Verfahren: keine Heilung
- Detaillierte Prüfung erforderlich

## 7) Workflow

### Phase 1 — Plan-Prüfung

- Plan-Begründung
- Abwaegungs-Vorgang
- Beteiligungs-Verfahren

### Phase 2 — Antragsbegründung

- Konkrete Mängel
- Eigene Betroffenheit
- Beweisanbote

### Phase 3 — OVG-Verfahren

- Schriftsatz-Wechsel
- Anhörungs-Termin
- Urteil

### Phase 4 — Bei Erfolg

- Norm verworfen
- Plan-Geber muss neu planen
- Folge: Bauverbot

## 8) Einstweiliger Rechtsschutz § 47 VI VwGO

### Voraussetzungen

- Eilbedürftigkeit
- Erfolgsaussicht Hauptverfahren

### Beispiel

- Bei beantragter Baugenehmigung im B-Plan
- Einstweilige Anordnung gegen Plan-Vollzug

## 9) Verfahrensdauer und Kosten

- 1-3 Jahre typisch
- Streitwert nach wirtschaftlichem Interesse
- Bei Verlust: Gerichts- + Anwaltskosten

## 10) Typische Fehler

1. **1-Jahres-Frist verpasst**
2. **Antragsbefugnis nicht ausreichend dargetan**
3. **Mängel pauschal vorgetragen**
4. **Heilungs-Pflicht nach § 215 BauGB ignoriert**

## 11) Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

- `normenkontrolle-bauleitplanung` (Vollplugin) — Vertieftes Verfahren
- `fachanwalt-verwaltungsrecht-orientierung` — Triage
- `widerspruch-oder-klage-erstpruefung` — bei anderer VG-Sache

## 2. `fachanwalt-verwaltungsrecht-orientierung`

**Fokus:** Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberblicken. Normen: VwGO (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage, Eilrechtsschutz §§ 80 und 123 VwGO), VwVfG, Polizei- und Ordnungsrecht, Baurecht. Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht), Verfahrensarten, Fristen-Überblick. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Detailarbeit in Fachmodule; Mandats-Triage siehe mandat-triage-verwaltungsrecht.

### Fachanwalt für Verwaltungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 30 gerichtliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Verwaltungsverfahren | VwVfG (Bund) Landes-VwVfG |
| Verwaltungsprozess | VwGO §§ 40 ff. 80 86b 123 |
| Allgemeines Verwaltungsrecht | Quellenprüfung Hartmann Grundbegriffe |
| Polizei- und Ordnungsrecht | Polizei- und Ordnungsgesetze der Länder (PolG NRW BayPAG) |
| Baurecht | BauGB BauNVO Landesbauordnungen |
| Beamtenrecht | BeamtStG BBG Landesbeamtengesetze |
| Versammlungsrecht | VersG / Landesversammlungsgesetze |
| Datenschutz öffentlich | BDSG Landesdatenschutzgesetze |

## Typische Mandate

- Bauantrag Widerspruch und Klage
- Polizei- und Ordnungsverfügung
- Beamtenrechtliche Streitigkeiten (Beurteilung Versetzung Disziplinarverfahren)
- Sozialhilfe vs Eingliederung (Abgrenzung zu Sozialrecht)
- Versammlungsverbot
- Ausländer- und Asylrechtsstreit (siehe fachanwalt-migrationsrecht)
- Verwaltungsvollstreckung

## Fristen

- **Widerspruchsfrist** § 70 VwGO — ein Monat.
- **Klagefrist** § 74 VwGO — ein Monat ab Bekanntgabe.
- **Berufungsantrag (Zulassung)** § 124a VwGO — ein Monat.
- **Eilrechtsschutz** § 80 Abs. 5 VwGO und § 123 VwGO — keine Frist; aber Eilbedürfnis erforderlich.
- **Normenkontrolle** § 47 VwGO — ein Jahr ab Bekanntmachung der Norm.

## Hauptgerichte

- Verwaltungsgericht erste Instanz (§ 45 VwGO).
- OVG / VGH Berufung und Normenkontrolle.
- BVerwG Leipzig Revision.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Verwaltungsrecht DAV.

## Aktuelle Rechtsprechung (Leitsaetze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Fristen im Ueberblick

| Verfahrensschritt | Frist | Grundlage |
|---|---|---|
| Widerspruch | 1 Monat | § 70 VwGO |
| Klage | 1 Monat | § 74 VwGO |
| Normenkontrolle | 1 Jahr | § 47 Abs. 2 VwGO |
| Untaetigkeitsklage | 3 Monate | § 75 VwGO |
| Berufungsantrag | 1 Monat | § 124a VwGO |
| Verfassungsbeschwerde | 1 Monat | § 93 BVerfGG |
| Revisionsantrag | 1 Monat | § 139 VwGO |

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schnittstellen

- **kanzlei-allgemein** für Fristen Versand.
- **fachanwalt-migrationsrecht** bei Auslaenderrecht.
- **fachanwalt-sozialrecht** bei Abgrenzung Sozialgericht vs. Verwaltungsgericht.

## 3. `fachanwalt-verwaltungsrecht-vergleich-106-vwgo-behoerde`

**Fokus:** Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandant will Streit mit Behörde außergerichtlich beilegen. Normen: § 106 VwGO (Prozessvergleich), § 55 VwVfG (Vergleichsvertrag), § 28 VwVfG (Anhörung). Prüfraster: Vergleichsfähigkeit, Mediation VwG, Eroerrterungstermin, Petitionsweg, Protokoll-Anforderungen. Output Vergleichs-Entwurf, Strategie-Memo. Abgrenzung: Klage-Strategie siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Vergleich Vergabe siehe fachanwalt-vergaberecht-Plugin.

### Verwaltungsrechts-Vergleich / Behördenkommunikation

## Zweck

Verwaltungsstreit kann an mehreren Stellen vergleichsweise beendet werden: **vor Bescheid** durch konsensorientierte Anhörung § 28 VwVfG, **nach Bescheid** durch Vergleichsvertrag § 55 VwVfG, **im Klageverfahren** durch Vergleich § 106 VwGO, **im Erörterungstermin** durch gerichtliche Mitteilung. Behördenkommunikation hat eigene Strategie- und Höflichkeits-Anforderungen.

## Eingaben

- Verwaltungsakt-Typ (begünstigend, belastend, Drittwirkung)
- Behörden-Ebene (Bund, Land, Kommune)
- Verfahrensphase (Anhörung, Widerspruch, Klage)
- Mandant (Bürger, Unternehmen, Konkurrent)
- Streitgegenstand (Genehmigung, Bauantrag, Subvention, Polizei-Verfügung)

## Rechtlicher Rahmen

- **§ 28 VwVfG** — Anhörung vor Verwaltungsakt
- **§ 55 VwVfG** — Vergleichsvertrag öffentlich-rechtlich
- **§§ 54-62 VwVfG** — Öffentlich-rechtlicher Vertrag
- **§ 106 VwGO** — Vergleich im Verwaltungsprozess
- **§ 87 VwGO** — Erörterungstermin
- **§§ 68 ff. VwGO** — Widerspruchsverfahren (Vorverfahren)
- **Art. 17 GG** — Petitionsrecht
- **MediationsG** — Mediation im Verwaltungsverfahren möglich

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## ADR-Pfade

### Pfad 1 — Anhörung § 28 VwVfG strategisch nutzen

- Vor Erlass des belastenden VA
- Anwalts-Stellungnahme mit Lösungs-Vorschlägen
- Behörde kann Modifikation erwägen
- Effektiv bei Ermessens-VAs

### Pfad 2 — Widerspruchs-Vergleich

- Im Widerspruchsverfahren (sofern noch zulässig)
- Verwaltungsbehörde zur Modifikation bewegen
- Schriftliche Verständigung

### Pfad 3 — Öffentlich-rechtlicher Vergleichsvertrag § 55 VwVfG

- Schriftform § 57 VwVfG zwingend
- Verzicht auf Anfechtungsklage gegen Modifikation
- Nur bei Ungewissheit über Sach-/Rechtslage
- Genehmigung Aufsichtsbehörde ggf. erforderlich

### Pfad 4 — Vergleich § 106 VwGO im Klageverfahren

- Im Verwaltungsprozess
- Erörterungstermin § 87 VwGO
- Gerichtlicher Vergleich vollstreckbar (§ 168 I Nr. 3 VwGO)
- Kostenregelung im Vergleich

### Pfad 5 — Mediation (selten, aber möglich)

- Bei Großvorhaben (Infrastruktur, UVP)
- Stuttgart 21-Modell
- Ungebundene Mediatoren
- Konsens als Ziel, nicht Vergleich

## Workflow

### Phase 1 — Verfahrens-Eintritt

- Akteneinsicht § 29 VwVfG
- Behörden-Position erkunden
- Anhörungs-Stellungnahme entwerfen

### Phase 2 — Anhörungs-Stellungnahme

- Sachverhalts-Korrektur
- Rechtsgründe
- Lösungs-Vorschläge (Auflagen, Modifikation)

### Phase 3 — Widerspruch (sofern Vorverfahren noch vorhanden)

- Beachtung: § 80 VwGO Anordnung aufschiebende Wirkung
- Bei Kommunen: häufig kein Vorverfahren (Landesrecht)
- Vergleichs-Ansatz im Widerspruch

### Phase 4 — Klage VG / OVG

- Anfechtungs-/Verpflichtungs-/Feststellungs-Klage
- Erörterungstermin nutzen
- Vergleich § 106 VwGO

### Phase 5 — Vollstreckung

- Bei Verpflichtungs-Klage: § 167 VwGO Vollstreckung
- Zwangsgeld gegen Behörde

## Strategie und Taktik

- **Anhörung ist Schlüsselphase**: hier ist Behörden-Ermessen am offensten
- **Behörden-Sprache**: nüchtern, sachlich, faktisch — keine Polemik
- **§ 55 VwVfG Vergleichsvertrag**: schriftliche Form zwingend, Aufsichts-Genehmigung beachten
- **Erörterungstermin**: VG ist meist vergleichsfreundlich, insb. bei tatsächlichen Streit
- **Petitionsweg parallel**: ergänzend, nicht statt Rechtsbehelf
- **Bei Ermessens-Reduzierung-Argumenten**: vorsichtig — Behörde behält Ermessen häufig

## Querverweise

- `fachanwalt-verwaltungsrecht-orientierung` — Triage
- `fachanwalt-verwaltungsrecht-widerspruch-klage` — Vorverfahren
- `fachanwalt-verwaltungsrecht-ki-automatisierte-verwaltungsakte-35a-vwvfg` — Sonderfall

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen und Updates

Stand: 05/2026. VwVfG/VwGO im Kern stabil. Für die Verifikation öffentlich-rechtlicher Vergleiche und Erörterungstermine vor Ausgabe Rechtsprechungsdatenbank des BVerwG (bverwg.de) konsultieren — keine Aktenzeichen aus Modellwissen.

- VwGO — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwgo/)
- VwVfG — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwvfg/)
- BVerwG-Entscheidungsdatenbank — [bverwg.de](https://www.bverwg.de/entscheidungen)
