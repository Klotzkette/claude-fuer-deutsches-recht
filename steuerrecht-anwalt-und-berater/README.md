# Steuerrecht – Steuerberater und Anwälte

Konsolidiertes Steuerrecht-Plugin für zwei Zielgruppen: **Anwaltschaft im Steuerrecht** (`anw-`) — inkl. Fachanwältinnen und Fachanwälte für Steuerrecht — und **Steuerberatung** (`stb-`). Umfasst das vollständige Mandats-Workflow von der Bescheidanalyse über Einspruch und Klage bis zu Selbstanzeige, Außenprüfung, Strafverteidigung und Haftungs-Warnschreiben — sowie Steuerberater-Werkzeuge für BWA-/SuSa-/Bilanzprüfung, Überschuldungs- und Liquiditätsprüfung mit Krisenfrüherkennung.

> Dieses Plugin ist **gleichzeitig das Fachanwalts-Plugin** für Steuerrecht. Es ersetzt das frühere separate `fachanwalt-steuerrecht`-Plugin: alle Fachanwalts-Skills sind hier mit dem Präfix `anw-` enthalten — die FAO-§-9-Voraussetzungen sind als Anhang im Skill `anw-orientierung` aufgenommen.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen bzw. steuerlichen Prüfung — zitiert, mit Prüfhinweisen versehen. Das Plugin erledigt die Recherchearbeit. Die rechtliche Beurteilung und die Entscheidung liegen beim Rechtsanwalt, Fachanwalt für Steuerrecht oder Steuerberater.** Folgenreiche Handlungen — Einreichen, Versenden, Vollziehen — erfordern ausdrückliche Freigabe.


## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **fortbestehensprognose paragrafix gmbh** | [testakte-fortbestehensprognose-paragrafix-gmbh.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Steuerberater und Fachanwalt für Steuerrecht (`steuerrecht-anwalt-und-berater`) | [steuerrecht-anwalt-und-berater.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/steuerrecht-anwalt-und-berater.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json` und `skills/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **Edelholz Manufaktur Berlin (Liquiditaet/Steuer/Insolvenz)** | [testakte-beispielakte-edelholz-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beispielakte-edelholz-berlin.zip) |


---

## Für die Anwaltschaft im Steuerrecht (anw-...)

Skills für steuerrechtliche Anwaltskanzleien — streitbezogene Folgebearbeitung von Bescheiden, Steuerstrafverteidigung und Haftungswarnung bei Krisen. **Identisch nutzbar für Fachanwältinnen und Fachanwälte für Steuerrecht** (FAO § 9); die Fachanwaltsausbildungs-Voraussetzungen sind im Skill `anw-orientierung` als Anhang dokumentiert.

| Skill | Funktion |
|---|---|
| `/steuerrecht-anwalt-und-berater:anw-orientierung` | Orientierung Anwalt im Steuerrecht (Normen, Fristen, Quellenprüfung) + FAO § 9-Anhang |
| `/steuerrecht-anwalt-und-berater:anw-kaltstart-interview` | Ersteinrichtung — Kanzleiprofil, Schwerpunkte, Finanzämter, FG-Bezirke |
| `/steuerrecht-anwalt-und-berater:anw-mandat-triage-steuerrecht` | Eingangs-Triage: Steuerart, Vorgang, Fristen, Eskalation |
| `/steuerrecht-anwalt-und-berater:anw-steuerbescheid-analyse` | Steuerbescheid systematisch auswerten vor Einspruch |
| `/steuerrecht-anwalt-und-berater:anw-einspruch-finanzamt` | Einspruch § 347 AO mit AdV-Antrag und Akteneinsicht |
| `/steuerrecht-anwalt-und-berater:anw-aussetzung-vollziehung` | AdV-Antrag zweistufig: FA § 361 AO + FG § 69 Abs. 3 FGO |
| `/steuerrecht-anwalt-und-berater:anw-klage-finanzgericht` | Klage zum Finanzgericht § 40 ff. FGO |
| `/steuerrecht-anwalt-und-berater:anw-akteneinsicht-steuerakte` | Akteneinsicht § 364 AO / § 78 FGO / Art. 15 DSGVO |
| `/steuerrecht-anwalt-und-berater:anw-aussenpruefung-strategien` | Außenprüfung §§ 193 ff. AO: Begleitung, Strategie, Schlussbesprechung |
| `/steuerrecht-anwalt-und-berater:anw-selbstanzeige-371` | Selbstanzeige § 371 AO — Hochrisikobereich, Pflichtprüfung mehrere Anwälte |
| `/steuerrecht-anwalt-und-berater:anw-haftungswarn-15a-inso-mandant` | Anwaltliche Belehrung GF bei Insolvenzreife (§ 15a InsO, § 15b InsO) — Schreibvorlage mit Eingangsbestätigung |
| `/steuerrecht-anwalt-und-berater:anw-insolvenzreife-pruefung-17-19-inso` | Anwaltliche Insolvenzreife-Prüfung §§ 17, 19 InsO mit steuerspezifischem Schwerpunkt (§ 222 AO Stundung, § 361 AO AdV, § 69 AO GF-Haftung, § 266a StGB) |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `/steuerrecht-anwalt-und-berater:anw-stundung-erlass-vollstreckungsaufschub` | Stundung § 222 AO, Erlass § 227/§ 163 AO, Vollstreckungsaufschub § 258 AO — Antrag mit Liquiditätsbeleg, Ratenplan, Sicherheitsleistung — **NEU** |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `/steuerrecht-anwalt-und-berater:anw-grunderwerbsteuer-share-deal-90-prozent` | GrESt beim Share Deal — 90-%-Schwelle ab 1.7.2021, 10-Jahres-Frist, RETT-Blocker, § 19 GrEStG Anzeigepflicht — **NEU** |
| `/steuerrecht-anwalt-und-berater:anw-dac7-dac8-plattformen-krypto` | DAC7 (PStTG, 1.1.2023) und DAC8 (KryptoStG, 1.1.2026) — Meldepflichten Plattformen und Krypto-Dienstleister, MiCA-VO — **NEU** |
| `/steuerrecht-anwalt-und-berater:anw-minbestg-pillar2-konzernbesteuerung` | Pillar Two / MinBestG ab 1.1.2024 — globaler Mindeststeuersatz 15 % für Konzerne ab 750 Mio EUR; IIR/UTPR/QDMTT, GloBE Information Return — **NEU** |
| `/steuerrecht-anwalt-und-berater:anw-steuerstrafverteidigung-verstaendigung` | Strafverteidigung Steuerstrafsache (§§ 369 ff. AO) mit Einstellung § 153a StPO und Verständigung § 257c StPO |
| `/steuerrecht-anwalt-und-berater:anw-verbindliche-auskunft` | Verbindliche Auskunft § 89 Abs. 2 AO |
| `/steuerrecht-anwalt-und-berater:anw-fristenbuch-steuerrecht` | Fristenbuch: Einspruchsfrist, Klagefrist, Vorfristen |
| `/steuerrecht-anwalt-und-berater:anw-betriebsausgaben-werbungskosten-pruefraster` | Prüfraster Betriebsausgaben/Werbungskosten § 4 Abs. 4 / § 9 EStG |
| `/steuerrecht-anwalt-und-berater:anw-umsatzsteuer-vorsteuerabzug-pruefen` | Vorsteuerabzug § 15 UStG — Prüfraster, eRechnung-Pflicht ab 1.1.2025 |

### Ersteinrichtung

```
/steuerrecht-anwalt-und-berater:anw-kaltstart-interview
```

Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` gespeichert.

---

## Für die Steuerberatung (stb-...)

Skills für Steuerberater und GmbH-Geschäftsleitung — BWA-/SuSa-/Bilanzprüfung, Überschuldungs- und Liquiditätsprüfung mit Krisenfrüherkennung und Haftungs-Warnschreiben.

| Skill | Funktion |
|---|---|
| `/steuerrecht-anwalt-und-berater:stb-kaltstart-interview` | Ersteinrichtung — Praxisprofil, Mandanten-Schwerpunkte, Buchhaltungssystem |
| `/steuerrecht-anwalt-und-berater:stb-bwa-sus-bilanz-pruefung` | BWA-/SuSa-/Bilanzprüfung auf Krisensignale (§§ 17, 19 InsO, § 102 StaRUG) |
| `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3wochen` | 3-Wochen-Liquiditätsvorschau § 17 InsO Vorprüfung |
| `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose |
| `/steuerrecht-anwalt-und-berater:stb-ueberschuldungspruefung-19-inso` | Stichtagsbezogene Überschuldungsprüfung § 19 InsO mit Fortführungsprognose nach IDW S 6/S 11 — **NEU** |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `/steuerrecht-anwalt-und-berater:stb-drv-sozialversicherungspruefung` | Begleitung der DRV-Sozialversicherungsprüfung § 28p SGB IV — Statusfeststellung, Phantomlohn, Mindestlohn, § 266a StGB-Risiken — **NEU** |

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **Power-Plugin Liquidität:** Die vollständige Power-Version der Liquiditätsvorschau (BGH-Schema Passiva II, Excel-Vorlage, HTML-Padlet, insolvenzrechtliche Stichtagsbilanz) lebt im Plugin [`liquiditaetsplanung`](../liquiditaetsplanung/). Die `stb-`-Skills hier sind die Steuerberater-Sicht zur Krisenfrüherkennung und triggern die Power-Version bei tiefergehender Begutachtung.

---

## Skill-Workflows

### A) Krisen-Workflow (Steuerberater → Anwalt)

```
  [stb-bwa-sus-bilanz-pruefung]
            ↓  Krisensignal erkannt
  [stb-ueberschuldungspruefung-19-inso] + [stb-liquiditaetsvorschau-3wochen]
            ↓  gelbe / rote Ampel
  Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
            ↓  Mandantin sucht Anwalt auf
  [anw-insolvenzreife-pruefung-17-19-inso]  — Diagnose
            ↓
  [anw-haftungswarn-15a-inso-mandant]      +  [anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern]
  (§ 11 BORA-Belehrung)                       (§§ 34, 69 AO, § 266a StGB)
            ↓  bei Vollmandat Sanierung / Antrag
  Übergabe an Fachanwalt Insolvenz-/Sanierungsrecht (Plugin `insolvenzrecht`)
```

### B) Außenprüfung-Workflow

```
  [anw-aussenpruefung-strategien]
            ↓  Prüfungsanordnung / Schlussbesprechung mit Mehrergebnis
  [anw-einspruch-finanzamt]
            ↓  Vollziehung droht
  [anw-aussetzung-vollziehung]  (§ 361 AO / § 69 FGO)
            ↓  Einspruch erfolglos
  [anw-klage-finanzgericht]
            ↓  parallel bei Strafverdacht (z. B. § 370 AO, § 26c UStG)
  Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

### C) M&A-Steuer-Workflow

```
  [anw-mandat-triage-steuerrecht]
            ↓
  [anw-verbindliche-auskunft]   — § 89 Abs. 2 AO, vor Strukturmaßnahme
            ↓
  [anw-organschaft-konzern-grundlagen]   — ertragst. / USt-/GewSt-Organschaft (§ 14 KStG, § 2 Abs. 2 UStG, § 2 Abs. 2 GewStG)
            ↓  bei Immobilien im Organkreis / share-deal
  [anw-grunderwerbsteuer-share-deal-90-prozent]   — § 1 Abs. 2a/3/3a GrEStG, Konzernklausel § 6a GrEStG
            ↓  bei Konzern ≥ 750 Mio. EUR Konzernumsatz
  [anw-minbestg-pillar2-konzernbesteuerung]   — Pillar 2 / MinBestG, GIR-Erstabgabe 18 Monate (§ 95 Abs. 1 MinStG)
            ↓  bei grenzüberschreitenden Konstellationen
  Plugin [`aussenwirtschaft-zoll-sanktionen`](../aussenwirtschaft-zoll-sanktionen/)   — DBA-Klauseln, APAs, Verrechnungspreise, Sanktionscompliance
```

---

## Testakten

Drei fiktive Mandatsakten zum Ausprobieren der Skills:

| Testakte | Inhalt | Passt besonders zu |
|---|---|---|
| [`beispielakte-edelholz-berlin`](../testakten/beispielakte-edelholz-berlin/) | Edelholz Manufaktur Berlin GmbH — BWA, SuSa, Liquiditätslage, Steuern/SV-Rückstände | `stb-bwa-sus-bilanz-pruefung`, `stb-liquiditaetsvorschau-3wochen`, `stb-ueberschuldungspruefung-19-inso`, `stb-drv-sozialversicherungspruefung`, `stb-warnschreiben-krisensignale`, `anw-insolvenzreife-pruefung-17-19-inso`, `anw-haftungswarn-15a-inso-mandant`, `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern` |
| [`fortbestehensprognose-paragrafix-gmbh`](../testakten/fortbestehensprognose-paragrafix-gmbh/) | Paragrafix GmbH — Legal-AI-Startup, § 102-StaRUG-Hinweis, BWA, SuSa, 13-Wochen-Liquiditätsplanung | `stb-bwa-sus-bilanz-pruefung`, `stb-liquiditaetsvorschau-3-6-12-monate`, `stb-ueberschuldungspruefung-19-inso`, `anw-insolvenzreife-pruefung-17-19-inso`, `anw-stundung-erlass-vollstreckungsaufschub`, `anw-organschaft-konzern-grundlagen` (Holding-Strukturierung), `anw-dac7-dac8-plattformen-krypto` (falls Plattform-/Krypto-Bezug) |
| [`grosskanzlei-corporate-ma-datenraum`](../testakten/grosskanzlei-corporate-ma-datenraum/) | Projekt Silberfalke — Umwandlungs- und Steuerstruktur, verbindliche Auskunft, Außenprüfung im M&A-Kontext | `anw-verbindliche-auskunft`, `anw-aussenpruefung-strategien`, `anw-organschaft-konzern-grundlagen`, `anw-grunderwerbsteuer-share-deal-90-prozent`, `anw-minbestg-pillar2-konzernbesteuerung` (ab Konzernschwelle 750 Mio. EUR), `anw-einspruch-finanzamt`, `anw-klage-finanzgericht` |

> **Hinweis zum Testakten-Mapping:** Die obenstehende Spalte ist nicht abschließend. Die drei Akten decken jeweils mehrere Phasen des Krisen-/Außenprüfungs-/M&A-Workflows ab — ein passender Skill ist meistens über das Stichwortverzeichnis ("Mandatsanlass") der jeweiligen Akte schnell zu finden. Skills, die nicht direkt zu einer Akte mappen (z. B. `anw-minbestg-pillar2-konzernbesteuerung` ohne 750 Mio. EUR-Konzern in der Akte), werden anhand ihrer eigenen Beispieldaten innerhalb des Skills demonstriert.

---

## Voraussetzungen

- **Persistenter Datenpfad.** Konfiguration und Fristenbücher werden unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/` gespeichert. Diese Dateien enthalten mandatsbezogene Daten — Verzeichnis sichern und zugriffsschützen (Art. 5 Abs. 1 lit. f DSGVO, § 43a Abs. 2 BRAO).
- **Rechtsdatenbank-Zugang.** Skills speichern keine konkreten Normtexte. Normen werden zum Zeitpunkt der Prüfung recherchiert und zitiert.
- **Steuerberater für Steuererklärungen.** Dieses Plugin ist auf anwaltlich-streitbezogene Folgebearbeitung und Steuerberater-Krisenprüfung ausgerichtet — nicht auf DATEV-Steuererklärungserstellung.
- **Mandatsgeheimnis.** § 43a Abs. 2 BRAO, § 203 StGB und § 53 StPO gelten für alle Ausgaben. Keine Weitergabe vertraulicher Mandantendaten ohne ausdrückliche Freigabe.
