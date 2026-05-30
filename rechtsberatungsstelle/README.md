# Plugin für die studentische Rechtsberatungsstelle


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Rechtsberatungsstelle Köln-Kalk — Monatsmix August 2026, Dr. Pellbach-Tannenfels** (`rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach`) | [Gesamt-PDF lesen](../testakten/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach/gesamt-pdf/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

*KI-gestützte Unterstützung für universitäre Refugee Law Clinics, studentische Rechtsberatungen und Pro-Bono-Initiativen – mit klaren RDG-Grenzen.*

Ein Plugin für Einrichtungen, in denen Studierende – unter Anleitung zur Anleitung berechtigter Volljuristen – unentgeltliche Rechtsberatung für Menschen leisten, die sich anwaltliche Hilfe nicht leisten können oder keinen Zugang dazu haben: Aufenthalts- und Asylrecht, Sozialrecht (SGB II/XII, SGB IX), Mietrecht, Verbraucherrecht, Familienrecht.

**Jede Ausgabe ist ein Entwurf für die Analyse durch Studierende und die Freigabe durch den anleitenden Volljuristen – gekennzeichnet, gestuft und protokolliert. Das Plugin gibt Struktur; die Studierenden denken juristisch; der Anleiter prüft und gibt frei. Nichts verlässt die Beratungsstelle ohne Durchlaufen dieses Aufsichtsmodells.**

---

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Rechtsberatungsstelle (`rechtsberatungsstelle`, dieses Plugin) | [rechtsberatungsstelle.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Wichtiger Hinweis: Rechtliche Grenzen nach dem RDG

> **Diese Beratungsstelle erbringt Rechtsdienstleistungen ausschließlich im Rahmen von § 6 Abs. 2 Nr. 2 RDG (unentgeltliche Rechtsdienstleistungen durch Volljuristen anleitungsberechtigt) oder § 8 RDG (Verbraucherzentralen, Sozialberatung). Jede entgeltliche Rechtsdienstleistung durch Nicht-Zugelassene ist nach § 3 RDG untersagt und nach § 20 RDG bußgeldbewehrt.**

**Für Studierende gilt:**
- Rechtliche Auskünfte dürfen nur unter Anleitung und Aufsicht eines zur Anleitung berechtigten Volljuristen erteilt werden (§ 6 Abs. 2 Nr. 2 RDG).
- Schriftsätze, Stellungnahmen und Widersprüche sind **Entwürfe** – keine fertigen, abzusendenden Dokumente.
- Jede strategische Entscheidung (Klage ja/nein, Rücknahme, Vergleich) liegt beim anleitenden Anwalt.
- Das Mandat liegt formal beim Anleiter, nicht beim Studierenden.
- Verschwiegenheit nach § 43a Abs. 2 BRAO analog, § 203 StGB – auch nach Semesterende.

---

## Das Problem, das dieses Plugin löst

Beratungsstellen sind strukturell kapazitätsbeschränkt. Ein anleitender Jurist betreut 5–12 Studierende. Jede Studierende trägt eine Handvoll Mandate, während sie gleichzeitig Lehrveranstaltungen besucht. Studierende wechseln jedes Semester. Verwaltungsaufgaben – Intake-Protokoll, Erstentwürfe, Rechercheansätze, Statusberichte, Semesterübergaben – verschlingen Stunden, die besser in die juristische Analyse investiert wären. Das Ergebnis: lange Wartelisten, begrenzte Fallzahlen, Ratsuchende, die aufgeben.

Dieses Plugin senkt die Zeitkosten für alles **rund um die Rechtsarbeit**, damit dieselben Studierenden und ihr Anleiter deutlich mehr Mandanten sinnvoll betreuen können – und die Studierenden mehr Zeit für Analyse und Strategie haben, die das Kernanliegen studentischer Rechtsbildung ausmacht.

**Es beschleunigt die nicht-lehrenden Teile. Es bewahrt die analytische Arbeit.** Das ist das Gestaltungsprinzip.

---

## Wer nutzt das Plugin?

| Rolle | Startet | Erhält |
|---|---|---|
| **Anleitender Volljurist** | `/kaltstart-interview` (einmalig), `/anleiter-pruefwarteschlange` (wenn formelle Prüfung aktiviert) | Konfigurierter Beratungsstellenkontext, Prüfung studentischer Arbeit |
| **Studierende** | `/einarbeitung` (Semesterbeginn), dann `/mandant-aufnahme`, `/entwurf`, `/memo`, `/recherche-start`, `/status`, `/mandantenbrief` | Strukturierte Arbeitshilfen, Entwürfe, Rechercheeinstiege |
| **Mandant** | – | Empfängt fertig geprüfte Briefe (Studierender + Anleiter haben freigegeben) |

---

## Schnellstart

```
/rechtsberatungsstelle:rechtsberatungsstelle-kaltstart-interview   # Anleiter: Beratungsstelle konfigurieren
/rechtsberatungsstelle:einarbeitung                   # Studierender: Einarbeitung zum Semesterbeginn
/rechtsberatungsstelle:mandant-aufnahme          # Neues Mandat aufnehmen
/rechtsberatungsstelle:memo                   # Gutachtenstil-Memo erstellen
/rechtsberatungsstelle:entwurf                  # Schriftsatz entwerfen
/rechtsberatungsstelle:fristen              # Fristen prüfen
/rechtsberatungsstelle:mandantenbrief          # Mandantenbrief in einfacher Sprache
/rechtsberatungsstelle:semester-uebergabe       # Semesterübergabe vorbereiten
```

---

## Beratungsstellentypen, die dieses Plugin unterstützt

### Universitäre Refugee Law Clinics (RLC)

Hochschulverankerte Kliniken wie die **Refugee Law Clinic Berlin** (HU Berlin/FU Berlin), die **Refugee Law Clinic Bremen** (Universität Bremen) oder die **Refugee Law Clinic Köln** (Universität zu Köln) beraten Asylsuchende und Geduldete zu Fragen des AsylG, AufenthG und SGB II. Besonderheiten:
- Kurze Fristen (§§ 36, 74 AsylG): Klagen gegen BAMF-Bescheide oft binnen 1–2 Wochen nach Zustellung.
- Sprachbarrieren: Dolmetscher-Koordination ist Teil des Intakes.
- Schnittstellen zu § 76b SGB IX (Eingliederungshilfe für Geflüchtete).

### Studentische Rechtsberatung nach § 6 Abs. 2 Nr. 2 RDG

Allgemeine studentische Beratungsstellen an Universitäten (oft "JuRI", "Jura hilft" o. ä.). Fokus: SGB II (Bürgergeld), Mietrecht, Verbraucherrecht, Familienrecht. Betrieb ausschließlich unter Aufsicht zugelassener Anwälte oder habilitierter Volljuristen.

### AnwVer/DAV Pro-Bono-Initiativen

Anwaltsverein-getragene Pro-Bono-Programme (z. B. **Pro Bono Berlin e. V.**, **DAV Pro Bono**): hier beraten zugelassene Anwälte direkt, die Plugin-Komponenten `entwurf`, `memo` und `recherche-start` unterstützen die Mandatsarbeit.

### Verbraucherzentralen (§ 8 RDG)

Verbraucherzentralen besitzen eine Sondererlaubnis nach § 8 Abs. 1 Nr. 4 RDG. Das Plugin unterstützt Standardfälle: Mieterhöhung, Kündigung, AGB-Kontrolle (§§ 305 ff. BGB), Energiekosten-Nachforderungen.

### Sozialberatung

Anerkannte Beratungsträger (AWO, Caritas, Diakonie, DRK, Paritätischer) arbeiten nach § 8 Abs. 1 Nr. 4 RDG. Schwerpunkte: SGB II, SGB XII, SGB IX, Rentenrecht (§ 109 SGB VI), Pflegegeld (§ 76b SGB IX).

---

## Beispiele: Pro-Bono-Initiativen in Berlin und Bremen

| Initiative | Ort | Schwerpunkt | Rechtsgrundlage |
|---|---|---|---|
| Refugee Law Clinic Berlin (HU/FU) | Berlin | AsylG, AufenthG, SGB II | § 6 II Nr. 2 RDG |
| Pro Bono Berlin e. V. | Berlin | Zivilrecht, Mietrecht, Familienrecht | Zugelassene Anwälte |
| Berliner Mieterverein – Rechtsberatung | Berlin | Mietrecht | § 8 I Nr. 3 RDG (Verband) |
| Refugee Law Clinic Bremen | Bremen | AsylG, AufenthG | § 6 II Nr. 2 RDG |
| Verbraucherzentrale Bremen | Bremen | Verbraucherrecht, Mietrecht | § 8 I Nr. 4 RDG |
| JuRI – Juristische Interessenvertretung (Uni Bremen) | Bremen | SGB II, allg. Zivilrecht | § 6 II Nr. 2 RDG |
| Caritas Berlin – Migrationsberatung | Berlin | AufenthG, SGB II | § 8 I Nr. 4 RDG |

---

## Fachbereiche und Skills

| Skill | Zweck | Primäre Normen |
|---|---|---|
| `leitfaden-erstellen` | Leitfaden zum Aufbau einer Beratungsstelle | RDG, BRAO |
| `mandanten-kommunikations-log` | Mandantenkommunikations-Logbuch | § 43a BRAO, § 203 StGB |
| `mandant-aufnahme` | Intake mit RDG-Konfliktprüfung | § 6 II Nr. 2 RDG |
| `mandantenbrief` | Mandantenbrief in einfacher Sprache | BORA |
| `rechtsberatungsstelle-kaltstart-interview` | Ersteinrichtung der Beratungsstelle | RDG, BRAO |
| `rechtsberatungsstelle-anpassen` | Beratungsstellenprofil anpassen | – |
| `fristen` | Fristenkontrolle | § 84 SGG, § 74 VwGO, §§ 36, 74 AsylG |
| `entwurf` | Schriftsatzentwurf | ZPO, VwGO, SGG |
| `formular-erzeugung` | Formularerstellung (PKH, BerHG, KSchG) | §§ 114 ff. ZPO, BerHG |
| `memo` | Memo im Gutachtenstil | – |
| `einfache-sprache-briefe` | Einfache Sprache | BORA |
| `einarbeitung` | Einarbeitung Studierende | § 6 II Nr. 2 RDG |
| `recherche-start` | Rechercheeinstieg | juris, Beck-Online, gesetze-im-internet.de |
| `semester-uebergabe` | Semesterübergabe | – |
| `status` | Statusbericht | – |
| `anleiter-pruefwarteschlange` | Aufsichts-Reviewqueue | § 6 II Nr. 2 RDG, § 43a BRAO |

---

## Qualitätssicherung

Alle studentischen Outputs tragen den Vermerk:

> **[KI-GESTÜTZTER ENTWURF – Analyse durch Studierende und Freigabe durch anleitenden Volljuristen erforderlich. Kein Versand ohne Prüfung.]**

Nur der anleitende Jurist kann diesen Vermerk entfernen. Dokumente, die diesen Vermerk tragen, dürfen nicht unmittelbar an Mandanten oder Behörden gesendet werden.

---

## Zitierweise

Alle juristischen Quellen folgen `../references/zitierweise.md`. Beispiele:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 45.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 17 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Rechtsberatungsstelle-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `anleiter-pruefwarteschlange` | 'Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell "formelle Prüfwarteschlange" gewählt wurde; an... |
| `einarbeitung` | 'Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte Handbuch und vermitte... |
| `einfache-sprache-briefe` | Anwalts- und Behoerdenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behoerde Gericht oder Gegenseite verstehen. BeratungsHiG... |
| `entwurf` | Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6 RDG-konforme Formulieru... |
| `formular-erzeugung` | Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behoerde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozia... |
| `fristen` | Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überf... |
| `leitfaden-erstellen` | Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache. BeratungsHiG niedr... |
| `mandant-aufnahme` | Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen. BeratungsHiG § 2 Beratun... |
| `mandanten-kommunikations-log` | Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO Datenschutz studentisch... |
| `mandantenbrief` | Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behoerde oder Gericht vorbereiten. BeratungsHiG niedrigschwellige... |
| `memo` | Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit RECHERCHE ERFORDERLIC... |
| `recherche-start` | Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, verifizierbare Quellen, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Stud... |
| `rechtsberatungsstelle-anpassen` | Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezif... |
| `rechtsberatungsstelle-kaltstart-interview` | Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet werden. BeratungsHiG §... |
| `semester-uebergabe` | Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des Mandatsgeheimnisses sauber an di... |
| `status` | Fallstatuszusammenfassung nach Zielgruppe — mandantengerichtet (verständliche Sprache), intern (für den Supervisor) oder gerichts-/behördengerichtet (formale Schriftsatzform per Verfahrensordnung). Gleiche Fakten, unterschiedliche Darste... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
