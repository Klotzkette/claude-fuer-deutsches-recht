# Plugin für die studentische Rechtsberatungsstelle

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`rechtsberatungsstelle`) | [`rechtsberatungsstelle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Rechtsberatungsstelle Köln-Kalk — Monatsmix August 2026, Dr. Pellbach-Tannenfels** (`rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach`) | [Gesamt-PDF lesen](../testakten/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach/gesamt-pdf/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach_gesamt.pdf) | [`testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip) |
| **Akte Reimers: Verbraucherinsolvenz, ehemaliger Geschäftsführer und Schuldenbereinigungsplan** (`verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung`) | [Gesamt-PDF lesen](../testakten/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung/gesamt-pdf/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung_gesamt.pdf) | [`testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

*KI-gestützte Unterstützung für universitäre Refugee Law Clinics, studentische Rechtsberatungen und Pro-Bono-Initiativen – mit klaren RDG-Grenzen.*

Ein Plugin für Einrichtungen, in denen Studierende – unter Anleitung zur Anleitung berechtigter Volljuristen – unentgeltliche Rechtsberatung für Menschen leisten, die sich anwaltliche Hilfe nicht leisten können oder keinen Zugang dazu haben: Aufenthalts- und Asylrecht, Sozialrecht (SGB II/XII, SGB IX), Mietrecht, Verbraucherrecht, Familienrecht.

**Jede Ausgabe ist ein Entwurf für die Analyse durch Studierende und die Freigabe durch den anleitenden Volljuristen – gekennzeichnet, gestuft und protokolliert. Das Plugin gibt Struktur; die Studierenden denken juristisch; der Anleiter prüft und gibt frei. Nichts verlässt die Beratungsstelle ohne Durchlaufen dieses Aufsichtsmodells.**

---

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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlaufstellen-beweislast-anleiter-bono` | Anlaufstellen: Beweislast, Darlegungslast und Substantiierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die... |
| `anleiter-formular-portal-und-einreichung` | Anleiter: Formular, Portal und Einreichungslogik; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschlägige... |
| `anleiter-pruefwarteschlange` | 'Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell 'formelle Prüfwarteschlange' gewählt wurde; an... |
| `anpassen` | Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezif... |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Rechtsberatungsstelle-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `bono-erstpruefung-und-mandatsziel` | Bono: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschlägige... |
| `briefe-erstberatung-rdg-konform` | Briefe: Zahlen, Schwellenwerte und Berechnung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschlägigen T... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einarbeitung` | Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte Handbuch und vermittel... |
| `einfache-sprache-briefe` | Anwalts- und Behördenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behörde Gericht oder Gegenseite verstehen. BeratungsHiG ko... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `entwurf-einarbeitung-einfache-sprache` | Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6 RDG-konforme Formulieru... |
| `erstberatung-rdg-grenzen-und-triage` | Erstberatung mit RDG-Grenzen und Triage: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fri... |
| `erzeugung-leitfaden-erstellen-mandanten` | Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behörde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozial... |
| `fristen-fristenkontrolle-rdg` | Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überf... |
| `fristen-risikoampel-mandantenkommunikation` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `fristenkontrolle-behoerden-gericht-und-registerweg` | Fristenkontrolle: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einsc... |
| `kaltstart-interview` | Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet werden. BeratungsHiG §... |
| `konform-dokumentenmatrix-und-lueckenliste` | Konform: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die eins... |
| `leitfaden-erstellen` | Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache. BeratungsHiG niedr... |
| `mandant-aufnahme` | Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen. BeratungsHiG § 2 Beratun... |
| `mandanten-kommunikations-log` | Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO Datenschutz studentisch... |
| `mandantenbrief-memo-rbs-beratungshilfe` | Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behörde oder Gericht vorbereiten. BeratungsHiG niedrigschwellige... |
| `mandantenfreundliche-quellenkarte-check` | Mandantenfreundliche Quellenkarte Check: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mandantenintake-mandatsuebergabe` | Mandantenintake: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konk... |
| `mandatsuebergabe-international-schnittstellen` | Mandatsuebergabe: Internationaler Bezug und Schnittstellen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die ei... |
| `memo` | Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit RECHERCHE ERFORDERLIC... |
| `output-waehlen` | Output wählen im Plugin Rechtsberatungsstelle: Diese Output-Weiche für Rechtsberatungsstelle entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `pro-bono-mandatsuebergabe` | Pro-Bono-Mandatsübergabe mit Fristen und Zuständigkeiten: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbest... |
| `pruefwarteschlange-red-rbst-recherche` | Pruefwarteschlange: Red-Team und Qualitätskontrolle; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschläg... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rbs-beratungshilfe-und-pkh-praxis` | Beratungshilfe BerHG und PKH in der Praxis: Antrag beim Amtsgericht, Berechtigung Einkommen, Vermoegen, Wahrnehmungsbefugnis Anwalt. Schnittstelle PKH-Antrag. Mustertexte und Berechtigungsnachweise im Rechtsberatungsstelle: prüft konkret... |
| `rbs-einfuehrung-rdg-rbst-anlaufstellen` | Rechtsberatungsstelle einfuehrend: typische Beratungsfelder Mietrecht, Sozialrecht, Familienrecht, Arbeitsrecht, Verbraucherrecht. Schutzfunktion für Beratungsberechtigte, Schnittstelle Beratungshilfe BerHG. Entscheidungstabelle im Recht... |
| `rbs-rdg-grenzen-spezial` | Spezialfall RDG-Grenzen: was darf eine Rechtsberatungsstelle, ehrenamtlich vs. Anwalt, Erlaubnistatbestaende. Schnittstelle Verbraucherschuldnerberatung, Mieterverein, Sozialverband. Pruefraster und Mandanteninformation im Rechtsberatung... |
| `rbst-anlaufstellen-bauleiter` | Bauleiter Anlaufstellen Rechtsberatung: Beratungshilfe, Prozesskostenhilfe, Schuldnerberatung, Mietervereine, Verbraucherzentrale. Pruefraster für Mandant und Sozialberatung im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbe... |
| `rbst-beratungshilfe-prozesskostenhilfe` | Leitfaden Beratungshilfe und Prozesskostenhilfe: Antragsvoraussetzungen, Vermoegen, Erfolgsaussicht, Eigenbeitrag. Pruefraster für Mandant und Rechtsanwalt im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fr... |
| `rbst-mandantenkommunikation-entscheidungsvorlage` | Rbst: Mandantenkommunikation und Entscheidungsvorlage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschl... |
| `rbst-niedrigschwellige-onlineberatung-spezial` | Spezialfall niedrigschwellige Onlineberatung mit KI-Unterstuetzung: Hinweispflichten, Verbraucherschutz, Datenschutz, Haftung. Pruefraster für Anbieter im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Friste... |
| `rbst-rdg-grenzen-spezial` | Spezialfall RDG-Grenzen für Nichtanwaelte: Verbraucherzentrale, Mietervereine, Inkassodienstleister, Legal-Tech. Pruefraster für Erlaubnispflicht im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Bel... |
| `rdg-fristen-form-und-zustaendigkeit` | RDG: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschlägigen... |
| `recherche-mehrparteien-konflikt-und-interessen` | Recherche: Mehrparteienkonflikt und Interessenmatrix; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschlä... |
| `recherche-start-rechtsberatungsstelle` | Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, verifizierbare Quellen, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Stud... |
| `rechtsberatung-uebergabe-schriftsatz-brief-memo-bausteine-status` | Uebergabe: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschlägi... |
| `rechtsberatungsstellen` | Rechtsberatungsstelle: Compliance-Dokumentation und Aktenvermerk; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret... |
| `rechtsberatungsstellen-tatbestand-beweis-und-belege` | Rechtsberatungsstellen: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft k... |
| `semester-uebergabe` | Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des Mandatsgeheimnisses sauber an di... |
| `semesterende-verhandlung-vergleich-und-eskalation` | Semesterende: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Rechtsberatungsstelle: prüft konkret die einschläg... |
| `sonderfall-edge-case` | Kaltstart: Sonderfall und Edge-Case-Prüfung im Plugin Rechtsberatungsstelle: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwe... |
| `status` | Fallstatuszusammenfassung nach Zielgruppe — mandantengerichtet (verständliche Sprache), intern (für den Supervisor) oder gerichts-/behördengerichtet (formale Schriftsatzform per Verfahrensordnung). Gleiche Fakten, unterschiedliche Darste... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prioris... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
