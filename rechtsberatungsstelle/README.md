# Claude für die studentische Rechtsberatungsstelle

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
/rechtsberatungsstelle:kaltstart-interview   # Anleiter: Beratungsstelle konfigurieren
/rechtsberatungsstelle:einarbeitung                   # Studierender: Onboarding zum Semesterbeginn
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

Allgemeine studentische Beratungsstellen an Universitäten (oft „JuRI", „Jura hilft" o. ä.). Fokus: SGB II (Bürgergeld), Mietrecht, Verbraucherrecht, Familienrecht. Betrieb ausschließlich unter Aufsicht zugelassener Anwälte oder habilitierter Volljuristen.

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
| `kaltstart-interview` | Ersteinrichtung der Beratungsstelle | RDG, BRAO |
| `anpassen` | Beratungsstellenprofil anpassen | – |
| `fristen` | Fristenkontrolle | § 84 SGG, § 74 VwGO, §§ 36, 74 AsylG |
| `entwurf` | Schriftsatzentwurf | ZPO, VwGO, SGG |
| `formular-erzeugung` | Formularerstellung (PKH, BerHG, KSchG) | §§ 114 ff. ZPO, BerHG |
| `memo` | Memo im Gutachtenstil | – |
| `einfache-sprache-briefe` | Einfache Sprache | BORA |
| `einarbeitung` | Onboarding Studierende | § 6 II Nr. 2 RDG |
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
- BSG, Urt. v. 14.03.2018 – B 14 AS 17/17 R, BSGE 125, 210 Rn. 18 – „Sanktionsrecht".
- BVerwG, Urt. v. 20.02.2020 – 1 C 1.19, BVerwGE 167, 319 Rn. 24.
- Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 45.
