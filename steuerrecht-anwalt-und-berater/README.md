# Steuerrecht – Steuerberater und Anwälte

Konsolidiertes Steuerrecht-Plugin für zwei Zielgruppen: **Anwaltschaft im Steuerrecht** (`anw-`) — inkl. Fachanwältinnen und Fachanwälte für Steuerrecht — und **Steuerberatung** (`stb-`). Umfasst das vollständige Mandats-Workflow von der Bescheidanalyse über Einspruch und Klage bis zu Selbstanzeige, Außenprüfung, Strafverteidigung und Haftungs-Warnschreiben — sowie Steuerberater-Werkzeuge für BWA-/SuSa-/Bilanzprüfung, Überschuldungs- und Liquiditätsprüfung mit Krisenfrüherkennung.

> Dieses Plugin ist **gleichzeitig das Fachanwalts-Plugin** für Steuerrecht. Es ersetzt das frühere separate `fachanwalt-steuerrecht`-Plugin: alle Fachanwalts-Skills sind hier mit dem Präfix `anw-` enthalten — die FAO-§-9-Voraussetzungen sind als Anhang im Skill `anw-orientierung` aufgenommen.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen bzw. steuerlichen Prüfung — zitiert, mit Prüfhinweisen versehen. Das Plugin erledigt die Recherchearbeit. Die rechtliche Beurteilung und die Entscheidung liegen beim Rechtsanwalt, Fachanwalt für Steuerrecht oder Steuerberater.** Folgenreiche Handlungen — Einreichen, Versenden, Vollziehen — erfordern ausdrückliche Freigabe.

## Rechtsstand und Quellen-Gate

Für aktuelle steuerrechtliche Aussagen zuerst `/steuerrecht-anwalt-und-berater:rechtsstand-mai-2026-faktenbank` laden. Der Skill enthält geprüfte freie Anker zu E-Rechnung ab 2025, Krypto/BFH/BMF, Grundsteuer-Bundesmodell/Landesmodellen, Grunderwerbsteuer-Share-Deals mit Signing/Closing, § 23 EStG und § 20 EStG/Verlustverrechnung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatzzitate aus Modellwissen. BFH/FG-Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle; Verwaltungsauffassung nur als BMF/BZSt-Quelle und nie als Ersatz für Gesetz und Rechtsprechung.


## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **fortbestehensprognose paragrafix gmbh** | [testakte-fortbestehensprognose-paragrafix-gmbh.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |
| **grundsteuer rosenwinkel bescheidkette** | [testakte-grundsteuer-rosenwinkel-bescheidkette.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundsteuer-rosenwinkel-bescheidkette.zip) |
| **grunderwerbsteuer sharedeal closing waldkrone** | [testakte-grunderwerbsteuer-sharedeal-closing-waldkrone.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grunderwerbsteuer-sharedeal-closing-waldkrone.zip) |

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
| **Grundsteuer Rosenwinkel Bescheidkette** | [testakte-grundsteuer-rosenwinkel-bescheidkette.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundsteuer-rosenwinkel-bescheidkette.zip) |
| **Grunderwerbsteuer Sharedeal Closing Waldkrone** | [testakte-grunderwerbsteuer-sharedeal-closing-waldkrone.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grunderwerbsteuer-sharedeal-closing-waldkrone.zip) |


---

## Für die Anwaltschaft im Steuerrecht (anw-...)

Skills für steuerrechtliche Anwaltskanzleien — streitbezogene Folgebearbeitung von Bescheiden, Steuerstrafverteidigung und Haftungswarnung bei Krisen. **Identisch nutzbar für Fachanwältinnen und Fachanwälte für Steuerrecht** (FAO § 9); die Fachanwaltsausbildungs-Voraussetzungen sind im Skill `anw-orientierung` als Anhang dokumentiert.

| Skill | Funktion |
|---|---|
| `/steuerrecht-anwalt-und-berater:anw-orientierung` | Orientierung Anwalt im Steuerrecht (Normen, Fristen, Quellenprüfung) + FAO § 9-Anhang |
| `/steuerrecht-anwalt-und-berater:rechtsstand-mai-2026-faktenbank` | Quellen-Gate: E-Rechnung, Krypto, Grundsteuer, § 23 EStG, § 20 EStG, BFH/BMF/BZSt ohne Blindzitate |
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
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-kaltstart-bescheidkette` | Grundsteuer-Mandat aufnehmen: Bescheidkette Finanzamt/Gemeinde, Fristen, Modellrouting, Sofortmaßnahmen |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-verfassungscheck-bundesmodell` | Grundsteuer-Reform verfassungsrechtlich einordnen: BVerfG 2018, BFH-AdV 2024, BFH-Bundesmodell 2025/2026 |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-ermittlungsbasis-flaeche-nutzung` | Flächen, Nutzung, Baujahr, wirtschaftliche Einheit, Schätzung und Beleglage prüfen |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuerwert-bewertung-bewg-218ff` | Grundsteuerwert nach BewG §§ 218 ff. prüfen: Ertragswert/Sachwert, Bodenrichtwert, Grundstücksart |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-einspruch-adv-bfh` | Einspruch und AdV in Grundsteuerfällen mit BFH-Linie und Belegstrategie |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-landesmodell-routing` | Bundesmodell und Landesmodelle trennen: Baden-Württemberg, Bayern, Hamburg, Hessen, Niedersachsen |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-hebesatz-zahlungsplan` | Kommunalen Grundsteuerbescheid, Hebesatz, Fälligkeit, Stundung und Zahlung prüfen |
| `/steuerrecht-anwalt-und-berater:anw-grundsteuer-gutachten-gemeiner-wert` | Niedrigeren gemeinen Wert und Gutachtenstrategie für Grundsteuer-AdV vorbereiten |
| `/steuerrecht-anwalt-und-berater:anw-grest-kaltstart-asset-share-deal` | GrESt-Kaltstart: Asset Deal, Share Deal, Signing, Closing, Anzeige und Bescheidroute |
| `/steuerrecht-anwalt-und-berater:anw-grest-asset-deal-kaufvertrag` | GrESt beim Grundstückskauf: Gegenleistung, einheitlicher Erwerbsgegenstand, Kaufvertrag |
| `/steuerrecht-anwalt-und-berater:anw-grest-share-deal-90-prozent-10-jahre` | Share-Deal-Vertiefung: § 1 Abs. 2a/2b/3/3a GrEStG, 90 %, 10 Jahre, RETT-Blocker |
| `/steuerrecht-anwalt-und-berater:anw-grest-signing-closing-doppelfestsetzung` | Signing/Closing-Spezialskill mit BFH II B 13/25, II B 23/25 und II B 47/25 |
| `/steuerrecht-anwalt-und-berater:anw-grest-anzeige-19-closing-check` | § 19-GrEStG-Anzeige, Closing-Checkliste, Anlagen und Zuständigkeiten |
| `/steuerrecht-anwalt-und-berater:anw-grest-spa-tax-clause-indemnity` | SPA-Steuerklauseln, GrESt-Indemnity, Escrow und Mitwirkungspflichten |
| `/steuerrecht-anwalt-und-berater:anw-grest-konzernklausel-6a` | Konzernklausel § 6a GrEStG bei Umwandlung, Einbringung und Konzernumstrukturierung |
| `/steuerrecht-anwalt-und-berater:anw-grest-bescheid-einspruch-adv-16` | GrESt-Bescheid prüfen: Einspruch, AdV, § 16 GrEStG, Doppelbelastung |
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
            ↓  bei Signing/Closing, Anzeige oder Bescheidstreit
  [anw-grest-signing-closing-doppelfestsetzung] + [anw-grest-anzeige-19-closing-check] + [anw-grest-bescheid-einspruch-adv-16]
            ↓  bei Konzern ≥ 750 Mio. EUR Konzernumsatz
  [anw-minbestg-pillar2-konzernbesteuerung]   — Pillar 2 / MinBestG, GIR-Erstabgabe 18 Monate (§ 95 Abs. 1 MinStG)
            ↓  bei grenzüberschreitenden Konstellationen
  Plugin [`aussenwirtschaft-zoll-sanktionen`](../aussenwirtschaft-zoll-sanktionen/)   — DBA-Klauseln, APAs, Verrechnungspreise, Sanktionscompliance
```

### D) Grundsteuer-Workflow

```
  [anw-grundsteuer-kaltstart-bescheidkette]
            ↓  Ebene bestimmen
  Finanzamt: Grundsteuerwert / Messbetrag       Gemeinde: Hebesatz / Zahlung
            ↓                                   ↓
  [anw-grundsteuer-ermittlungsbasis-flaeche-nutzung]     [anw-grundsteuer-hebesatz-zahlungsplan]
            ↓
  [anw-grundsteuerwert-bewertung-bewg-218ff]
            ↓  erhebliche Abweichung?
  [anw-grundsteuer-gutachten-gemeiner-wert]
            ↓
  [anw-grundsteuer-einspruch-adv-bfh]
            ↓
  [anw-grundsteuer-verfassungscheck-bundesmodell] / [anw-grundsteuer-landesmodell-routing]
```

---

## Testakten

Fünf fiktive Mandatsakten zum Ausprobieren der Skills:

| Testakte | Inhalt | Passt besonders zu |
|---|---|---|
| [`beispielakte-edelholz-berlin`](../testakten/beispielakte-edelholz-berlin/) | Edelholz Manufaktur Berlin GmbH — BWA, SuSa, Liquiditätslage, Steuern/SV-Rückstände | `stb-bwa-sus-bilanz-pruefung`, `stb-liquiditaetsvorschau-3wochen`, `stb-ueberschuldungspruefung-19-inso`, `stb-drv-sozialversicherungspruefung`, `stb-warnschreiben-krisensignale`, `anw-insolvenzreife-pruefung-17-19-inso`, `anw-haftungswarn-15a-inso-mandant`, `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern` |
| [`fortbestehensprognose-paragrafix-gmbh`](../testakten/fortbestehensprognose-paragrafix-gmbh/) | Paragrafix GmbH — Legal-AI-Startup, § 102-StaRUG-Hinweis, BWA, SuSa, 13-Wochen-Liquiditätsplanung | `stb-bwa-sus-bilanz-pruefung`, `stb-liquiditaetsvorschau-3-6-12-monate`, `stb-ueberschuldungspruefung-19-inso`, `anw-insolvenzreife-pruefung-17-19-inso`, `anw-stundung-erlass-vollstreckungsaufschub`, `anw-organschaft-konzern-grundlagen` (Holding-Strukturierung), `anw-dac7-dac8-plattformen-krypto` (falls Plattform-/Krypto-Bezug) |
| [`grosskanzlei-corporate-ma-datenraum`](../testakten/grosskanzlei-corporate-ma-datenraum/) | Projekt Silberfalke — Umwandlungs- und Steuerstruktur, verbindliche Auskunft, Außenprüfung im M&A-Kontext | `anw-verbindliche-auskunft`, `anw-aussenpruefung-strategien`, `anw-organschaft-konzern-grundlagen`, `anw-grunderwerbsteuer-share-deal-90-prozent`, `anw-minbestg-pillar2-konzernbesteuerung` (ab Konzernschwelle 750 Mio. EUR), `anw-einspruch-finanzamt`, `anw-klage-finanzgericht` |
| [`grundsteuer-rosenwinkel-bescheidkette`](../testakten/grundsteuer-rosenwinkel-bescheidkette/) | Rosenwinkel 14/16 — Grundsteuerwert, Messbetrag, kommunaler Bescheid, Flächenfehler, Denkmalschutz, gemeiner Wert und AdV | `anw-grundsteuer-kaltstart-bescheidkette`, `anw-grundsteuer-ermittlungsbasis-flaeche-nutzung`, `anw-grundsteuerwert-bewertung-bewg-218ff`, `anw-grundsteuer-gutachten-gemeiner-wert`, `anw-grundsteuer-einspruch-adv-bfh`, `anw-grundsteuer-hebesatz-zahlungsplan` |
| [`grunderwerbsteuer-sharedeal-closing-waldkrone`](../testakten/grunderwerbsteuer-sharedeal-closing-waldkrone/) | Projekt Waldkrone — Share Deal, Signing/Closing, § 19-Anzeige, SPA-Tax-Clause, Doppelbescheid und AdV | `anw-grest-kaltstart-asset-share-deal`, `anw-grest-share-deal-90-prozent-10-jahre`, `anw-grest-signing-closing-doppelfestsetzung`, `anw-grest-anzeige-19-closing-check`, `anw-grest-spa-tax-clause-indemnity`, `anw-grest-bescheid-einspruch-adv-16` |

> **Hinweis zum Testakten-Mapping:** Die obenstehende Spalte ist nicht abschließend. Die drei Akten decken jeweils mehrere Phasen des Krisen-/Außenprüfungs-/M&A-Workflows ab — ein passender Skill ist meistens über das Stichwortverzeichnis ("Mandatsanlass") der jeweiligen Akte schnell zu finden. Skills, die nicht direkt zu einer Akte mappen (z. B. `anw-minbestg-pillar2-konzernbesteuerung` ohne 750 Mio. EUR-Konzern in der Akte), werden anhand ihrer eigenen Beispieldaten innerhalb des Skills demonstriert.

---

## Voraussetzungen

- **Persistenter Datenpfad.** Konfiguration und Fristenbücher werden unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/` gespeichert. Diese Dateien enthalten mandatsbezogene Daten — Verzeichnis sichern und zugriffsschützen (Art. 5 Abs. 1 lit. f DSGVO, § 43a Abs. 2 BRAO).
- **Rechtsdatenbank-Zugang.** Skills speichern keine konkreten Normtexte. Normen werden zum Zeitpunkt der Prüfung recherchiert und zitiert.
- **Steuerberater für Steuererklärungen.** Dieses Plugin ist auf anwaltlich-streitbezogene Folgebearbeitung und Steuerberater-Krisenprüfung ausgerichtet — nicht auf DATEV-Steuererklärungserstellung.
- **Mandatsgeheimnis.** § 43a Abs. 2 BRAO, § 203 StGB und § 53 StPO gelten für alle Ausgaben. Keine Weitergabe vertraulicher Mandantendaten ohne ausdrückliche Freigabe.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 203 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Steuerrecht Anwalt Und Berater-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren... |
| `anw-akteneinsicht-steuerakte` | Akteneinsicht in die Steuerakte beantragen und auswerten — Einspruchsverfahren nach § 364 AO Klageverfahren nach § 78 FGO sowie ergaenzend Art. 15 DSGVO bei personenbezogenen Daten. Anwendungsfall Mandant will Prüfungsbericht Aktenvermer... |
| `anw-aussenpruefung-strategien` | Anwaltliche Begleitung einer Betriebsprüfung Aussenprüfung nach §§ 193 ff. AO. Anwendungsfall Mandant erhaelt Prüfungsanordnung § 196 AO oder Prüfung laeuft bereits. Prüfraster Umfang § 194 AO Mitwirkungspflichten § 200 AO Datenzugriff §... |
| `anw-aussetzung-vollziehung` | Antrag auf Aussetzung der Vollziehung AdV stellen um Steuerzahlung bis zur Streitentscheidung auszusetzen. Anwendungsfall Mandant hat Einspruch eingelegt will aber Nachforderung nicht sofort zahlen. Zweistufig zuerst beim Finanzamt § 361... |
| `anw-betriebsausgaben-werbungskosten-pruefraster` | Workflow-Skill zu anw betriebsausgaben werbungskosten pruefraster. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anw-dac7-dac8-plattformen-krypto` | Beratung zu DAC7-Meldepflichten für digitale Plattformen ab 2023 PStTG und DAC8-Meldepflichten für Krypto-Dienstleister ab 2026 KryptoStG. Anwendungsfall Plattformbetreiber oder Krypto-Dienstleister fragt nach Meldepflichten oder Mandant... |
| `anw-defi-lending-yield-farming-bmf-22-11-2024` | Steuerliche Behandlung von DeFi-Lending Yield Farming Liquidity Mining Staking nach BMF-Schreiben vom 22.11.2024. Anwendungsfall Mandant nutzt DeFi-Protokolle Aave Compound Curve Yearn Uniswap Lido EigenLayer und fragt nach steuerlicher... |
| `anw-einspruch-finanzamt` | Begründeten Einspruch gegen Steuerbescheid nach §§ 347 ff. AO formulieren. Anwendungsfall Mandant erhaelt Steuerbescheid und will Einspruch einlegen. Frist ein Monat ab Bekanntgabe § 355 Abs. 1 AO bzw. ein Jahr bei fehlender Rechtsbehelf... |
| `anw-fristenbuch-steuerrecht` | Fristenbuch für steuerrechtliche Verfahren pflegen und Fristen berechnen. Anwendungsfall neue Bescheide oder Entscheidungen eingegangen Fristen muessen sofort eingetragen und ueberwacht werden. Standardfristen Einspruch § 355 AO ein Mona... |
| `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern` | Verteidigung gegen Haftungsbescheid nach § 69 AO wegen nicht abgeführter Lohnsteuer oder Umsatzsteuer der GmbH oder UG. Anwendungsfall Geschäftsführer erhaelt persoenlichen Haftungsbescheid des Finanzamts für Steuerschulden der Gesellsch... |
| `anw-grest-anzeige-19-closing-check` | Anzeige nach § 19 GrEStG und Closing-Checkliste: wer zeigt was wann welchem Finanzamt an, Inhalt der Anzeige, Grundstücksliste, Beteiligungswechsel, Notar, Gesellschaft, Erwerber, Fristen, Sanktionen und Nachdokumentation. |
| `anw-grest-asset-deal-kaufvertrag` | Grunderwerbsteuer beim Asset Deal pruefen: Grundstückskauf, Gegenleistung, Kaufpreisbestandteile, einheitlicher Erwerbsgegenstand, Bauerrichtung, Inventar, Umsatzsteueroption, Bundesland-Steuersatz, Notar- und Anzeigeablauf. |
| `anw-grest-bescheid-einspruch-adv-16` | GrESt-Bescheid prüfen und angreifen: Einspruch, Aussetzung der Vollziehung, § 16 GrEStG Rueckgaengigmachung/Korrektur, doppelte Festsetzung, falsche Bemessungsgrundlage, falscher Steuersatz, Verfahrensfehler und FG-Strategie. |
| `anw-grest-kaltstart-asset-share-deal` | Grunderwerbsteuer-Kaltstart fuer Immobilien-Transaktionen: Asset Deal, Share Deal, Signing, Closing, 90-Prozent-Schwelle, 10-Jahres-Zeitraum, Steuersatz je Bundesland, Anzeige, Bescheid und AdV routen. |
| `anw-grest-konzernklausel-6a` | § 6a GrEStG Konzernklausel prüfen: Umwandlung, Einbringung, herrschendes Unternehmen, abhaengige Gesellschaft, 95-Prozent-Beteiligung, Vor- und Nachbehaltensfrist, BFH-Rechtsprechung und Risiken bei Umstrukturierungen. |
| `anw-grest-share-deal-90-prozent-10-jahre` | GrESt Share Deal vertieft: § 1 Abs. 2a/2b/3/3a GrEStG, 90-Prozent-Schwelle, 10-Jahres-Zeitraum, unmittelbare und mittelbare Beteiligungen, RETT-Blocker, Altgesellschafter, Kapital- und Personengesellschaften. |
| `anw-grest-signing-closing-doppelfestsetzung` | GrESt Signing/Closing Spezialskill: auseinanderfallendes schuldrechtliches Erwerbsgeschaeft und dingliche Anteilsuebertragung, doppelte Festsetzung nach § 1 Abs. 2b und § 1 Abs. 3 GrEStG, BFH II B 13/25, II B 23/25, II B 47/25, AdV und V... |
| `anw-grest-spa-tax-clause-indemnity` | GrESt im SPA vertraglich absichern: Tax Covenant, GrESt-Indemnity, Käufer-/Verkäufertragung, Signing-Closing-Doppelrisiko, Escrow, Mitwirkungspflichten, Anzeigen, Grundbesitzliste und Post-Closing-Steuerklauseln. |
| `anw-grunderwerbsteuer-share-deal-90-prozent` | Grunderwerbsteuer GrEStG bei Share-Deal-Transaktionen mit grundbesitzhaltenden Gesellschaften berechnen und gestalten. Anwendungsfall M-und-A-Transaktion mit Immobilien-Hintergrund Anteilsuebertragung droht GrESt-Pflicht. 90-Prozent-Schw... |
| `anw-grundsteuer-einspruch-adv-bfh` | Grundsteuer-Einspruch und Aussetzung der Vollziehung: Frist, Bekanntgabe, BFH-AdV-Linie II B 78/23 und II B 79/23, BFH-Hauptsache 12.11.2025, Belegstrategie, Einspruchsbegründung und AdV-Antrag formulieren. |
| `anw-grundsteuer-ermittlungsbasis-flaeche-nutzung` | Grundsteuer-Ermittlungsbasis prüfen: Wohnfläche, Nutzfläche, Grundstücksfläche, wirtschaftliche Einheit, Baujahr, Nutzung, Garagen, Stellplätze, Erbbaurecht, Teileigentum, Leerstand, Denkmalschutz und Schätzungen aus der Grundsteuererklä... |
| `anw-grundsteuer-gutachten-gemeiner-wert` | Grundsteuer-Gegenbeweis mit gemeinem Wert vorbereiten: Kaufpreis, Verkehrswertgutachten, Maklerbewertung, Gutachterausschuss, Sonderfaktoren und BFH-AdV-Linie zu deutlich niedrigerem gemeinem Wert dokumentieren. |
| `anw-grundsteuer-hebesatz-zahlungsplan` | Kommunalen Grundsteuerbescheid prüfen: Hebesatz, Satzung, Fälligkeiten, Zahlungsplan, Stundung, Erlass, Vollstreckungsaufschub, Abgrenzung Finanzamt/Gemeinde und Kommunikation mit Hausverwaltung oder Kommune. |
| `anw-grundsteuer-kaltstart-bescheidkette` | Grundsteuer-Mandat schnell aufnehmen: Grundsteuerwertbescheid, Grundsteuermessbescheid und Grundsteuerbescheid auseinanderhalten, Fristen sichern, Bundesmodell oder Landesmodell routen, Fehlerquellen erkennen und passende Folgeskills lad... |
| `anw-grundsteuer-landesmodell-routing` | Grundsteuer-Landesmodell-Routing: Bundesmodell von Baden-Wuerttemberg, Bayern, Hamburg, Hessen, Niedersachsen und punktuellen Abweichungen trennen; richtige Rechtsquelle, Bescheidart, BFH-/FG-Stand und Argumentationslinie bestimmen. |
| `anw-grundsteuer-verfassungscheck-bundesmodell` | Verfassungsrechtlicher Grundsteuer-Check nach der Reform: BVerfG 10.04.2018 zur alten Einheitsbewertung, BFH 27.05.2024 AdV, BFH 12.11.2025 zum Bundesmodell, Art. 3 GG, Typisierung, gemeiner Wert, Landesmodelle und offene Verfahren saube... |
| `anw-grundsteuerwert-bewertung-bewg-218ff` | Grundsteuerwert nach BewG §§ 218 ff. prüfen: Bundesmodell, Ertragswert, Sachwert, Bodenrichtwert, Grundstücksart, Steuermesszahl, Hauptfeststellung 01.01.2022, Fehlerdiagnose und Bescheidbegründung. |
| `anw-haftungswarn-15a-inso-mandant` | Anwaltliche Beratung und Warnschreiben an GmbH-Geschäftsführung bei festgestellter Insolvenzreife nach §§ 17 19 InsO. Anwendungsfall GmbH-GF spricht beim Anwalt vor weil Steuerberater Krisensignale gemeldet hat. Antragspflicht § 15a InsO... |
| `anw-insolvenzreife-pruefung-17-19-inso` | Workflow-Skill zu anw insolvenzreife pruefung 17 19 inso. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anw-kaltstart-interview` | Kaltstart-Interview für die steuerrechtsanwaltliche Kanzlei um Praxisprofil zu befuellen. Anwendungsfall Erstinstallation Plugin oder Konfiguration enthaelt noch Platzhalter-Marker. Erfragt Schwerpunktbereiche ESt USt KSt GewSt ErbSt Ste... |
| `anw-klage-finanzgericht` | Klageschrift zum Finanzgericht nach §§ 40 ff. FGO entwerfen. Anwendungsfall Einspruch wurde zurückgewiesen Mandant will Klage einreichen oder Untätigkeitsklage nach sechs Monaten ohne Entscheidung. Klagefrist ein Monat nach Bekanntgabe E... |
| `anw-mandat-triage-steuerrecht` | Strukturierte Erstabfrage und Triage bei Eingang eines steuerrechtlichen Mandats. Anwendungsfall Mandant meldet sich mit Steuerproblem Art und Dringlichkeit noch unklar. Klaert Mandantenrolle Steuerart ESt KSt GewSt USt ErbSt GrESt Vorga... |
| `anw-minbestg-pillar2-konzernbesteuerung` | Beratung zur globalen Mindestbesteuerung Pillar Two MinBestG für Konzerne ab 750 Mio EUR Umsatz. Anwendungsfall Konzern fragt nach GloBE-Pflichten Compliance-Aufbau oder Country-by-Country Reporting ab 01.01.2024. MinBestG vom 21.12.2023... |
| `anw-organschaft-konzern-grundlagen` | Workflow-Skill zu anw organschaft konzern grundlagen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anw-orientierung` | Orientierungs-Skill für Anwaeltinnen und Anwaelte im Steuerrecht. Anwendungsfall Einstieg in das Plugin oder Überblick über verfuegbare Skills gewuenscht. Zentrale Gesetze AO EStG KStG UStG GewStG ErbStG GrEStG. Verfahrenswege Einspruch... |
| `anw-selbstanzeige-371` | Selbstanzeige nach § 371 AO als strafbefreiende Berichtigung bei Steuerhinterziehung vorbereiten und einreichen. Anwendungsfall Mandant hat Steuern hinterzogen und will Straffreiheit erlangen bevor Entdeckung droht. Vollständigkeit aller... |
| `anw-steuerbescheid-analyse` | Steuerbescheid strukturiert auswerten und Angriffspunkte für Einspruch identifizieren. Anwendungsfall Mandant hat Steuerbescheid bekommen und fragt ob und wie er sich wehren kann. Bescheidarten Festsetzungsbescheid Aenderungsbescheid Sch... |
| `anw-steuerstrafverteidigung-verstaendigung` | Workflow-Skill zu anw steuerstrafverteidigung verstaendigung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anw-stundung-erlass-vollstreckungsaufschub` | Anträge auf Stundung Erlass und Vollstreckungsaufschub bei Zahlungsproblemen stellen. Anwendungsfall Mandant kann fällige Steuerschulden vorueber-gehend oder dauerhaft nicht zahlen Vollstreckung droht. Stundung erhebliche Haerte § 222 AO... |
| `anw-tatsaechliche-verstaendigung-schlussbesprechung` | Workflow-Skill zu anw tatsaechliche verstaendigung schlussbesprechung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anw-umsatzsteuer-vorsteuerabzug-pruefen` | Workflow-Skill zu anw umsatzsteuer vorsteuerabzug pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `anw-verbindliche-auskunft` | Antrag auf verbindliche Auskunft nach § 89 Abs. 2 AO vor Verwirklichung eines steuerlich unsicheren Sachverhalts stellen. Anwendungsfall Mandant plant Umstrukturierung Holding Wegzug Schenkung Erbschaft oder internationalen Sachverhalt u... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Steuerrechtsmandate — Mandatsannahme von der ersten Kontaktaufnahme bis zur Vollmachtserteilung. Anwendungsfall Mandant ruft erstmals an oder kommt zum Erstgespraech Steuerrecht Beratung oder Pr... |
| `rechtsstand-mai-2026-faktenbank` | Faktenbank und Quellen-Gate für aktuelle steuerrechtliche Aussagen mit Stand 29.05.2026. Nutze diesen Skill vor Ausgaben zu E-Rechnung, Umsatzsteuer, Krypto, Grundsteuer, Mindeststeuer, DBA, Betriebsprüfung, Einspruch, AdV und Steuer-/SV... |
| `schriftsatzkern-substantiierung` | Substantiierten Schriftsatzkern für steuerrechtliche Verfahren aufbauen. Anwendungsfall Einspruch Klage FG Revision BFH Stundungs- und Erlassantrag muessen begründet und mit Beweisen unterfuettert werden. Tatsachenvortrag-Geruest Anspruc... |
| `stb-addison-bwa-konfiguration-tipps` | Addison BWA-Konfiguration. Anwendungsfall Kanzleien mit Wolters Kluwer Addison statt DATEV. Methodik Unterschiede zu DATEV Konten-Konfiguration Branchenanpassung. Output BWA in Addison. |
| `stb-belegtransfer-datev-unternehmen-online` | Belegtransfer DATEV Unternehmen Online. Anwendungsfall systematischer Belegfluss Mandant zu StB Beleg-Scan App Mailpostfach Bank-Anbindung. Methodik Konfiguration Workflow. Output Belegfluss-Standard. |
| `stb-buchhaltungsbutler-mandantencloud` | BuchhaltungsButler und vergleichbare Cloud-Buchhaltung beim Mandanten. Anwendungsfall Mandant arbeitet mit BuchhaltungsButler sevDesk Lexware Office Candis StB-Schnittstelle DATEV-Export Datenqualitaetsprüfung AVV. Methodik Konfiguration... |
| `stb-bwa-aufbau-grundlagen` | Aufbau der Standard-BWA für Steuerberater erlaeutern und konfigurieren. Anwendungsfall monatliche oder quartalsweise BWA-Erstellung für GmbH oder Personenunternehmen mit SKR 03 oder SKR 04. Struktur Umsatzerlöse Material Personal sonstig... |
| `stb-bwa-betriebsergebnis-deckungsbeitrag` | Ausweis Betriebsergebnis vor und nach Zinsen Deckungsbeitragsstruktur in der BWA. Anwendungsfall analytische BWA mit Stufendeckungsbeitrag EBITDA EBIT EBT Mandant aus Industrie Handel Dienstleistung. Methodik fixe und variable Kosten Ide... |
| `stb-bwa-betriebsuebersicht-erstellen` | Betriebsuebersicht als ergaenzende Auswertung zur BWA. Anwendungsfall ausführliche Monats- oder Quartalsauswertung mit allen Sachkonten-Salden ergaenzend zur kompakten BWA. Methodik Konfiguration in DATEV oder Addison als Kontenliste mit... |
| `stb-bwa-bewegungsbilanz-erstellen` | Bewegungsbilanz aus BWA und SuSa erstellen. Anwendungsfall Veranschaulichung Geld- und Mittelfluss zwischen zwei Stichtagen Vermögens- und Kapitalbewegung. Methodik Aktiva und Passiva Vergleich Mittelherkunft Mittelverwendung. Output Bew... |
| `stb-bwa-branchenvergleich-bbe-datev` | Branchenvergleich BWA auf Basis BBE-Datenbank über DATEV. Anwendungsfall Quartals- oder Jahres-BWA mit anonymisierten Branchen-Mittelwerten Median Top-Quartil. Methodik Branche identifizieren Vergleichsperiode waehlen Kennzahlenprüfung.... |
| `stb-bwa-cashflow-laienverstaendlich` | Cashflow-Darstellung für Mandant in laienverstaendlicher Form. Anwendungsfall Quartals-BWA mit vereinfachter Cashflow-Aufstellung für GF ohne Finanz-Hintergrund. Methodik einfache Mittelfluss-Tabelle Brutto-Netto-Cashflow Trennung zahlun... |
| `stb-bwa-erlaeuterungstext-mandant` | Erlaeuterungstext unter der BWA für den Mandanten. Anwendungsfall Monats- oder Quartals-BWA mit kurzem fachlichem Begleittext der die wesentlichen Abweichungen und Risiken benennt. Aufbau Sachverhalt Erlaeuterung Ausblick Empfehlung. Out... |
| `stb-bwa-fehlerquellen-haeufig` | Typische Fehlerquellen in der BWA. Anwendungsfall Qualitaetsprüfung BWA durch Berufstraeger interne Stichprobe Fehler in Periodenabgrenzung Buchungsfehler Bestandsveraenderung Lohnbuchungen. Methodik Checkliste Plausibilitaetsprüfung. Ou... |
| `stb-bwa-jahres-bwa-erstellen` | Jahres-BWA als Ergaenzung zum Jahresabschluss. Anwendungsfall Jahresabschluss-Begleitung mit BWA für das Gesamtjahr inkl Vorjahresvergleich Mehrjahrestrend und Mandantenpraesentation. Methodik kumulierte BWA mit Korrekturen Sondereffekte... |
| `stb-bwa-kapitalflussrechnung-iduk` | Kapitalflussrechnung nach indirekter Methode aus BWA und Bilanz. Anwendungsfall Jahresabschluss Bankreporting Sanierungskonzept Konzernabschluss. Methodik DRS 21 indirekte Ableitung aus Jahresueberschuss Mittelfluss laufende Geschäftstät... |
| `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` | Rentabilitaetskennzahlen Eigenkapitalrendite Gesamtkapitalrendite ROI Umsatzrentabilitaet. Anwendungsfall Quartals- oder Jahresauswertung Beratungsgespraech Investor-Update. Methodik Berechnung Bewertung Branchenvergleich Praktische Auss... |
| `stb-bwa-kontenrahmen-skr03-skr04` | Vergleich Kontenrahmen SKR 03 versus SKR 04 für BWA-Erstellung. Anwendungsfall Mandantenneuaufnahme oder Wechsel des Kontenrahmens Entscheidungsgrundlage Industrie Handel Dienstleistung. Aufbau Bilanz vs Prozess Gliederung GKV vs UKV. Ou... |
| `stb-bwa-mandantengespraech-uebergabe` | BWA-Übergabegespraech mit dem Mandanten. Anwendungsfall persoenliche oder telefonische Besprechung der monatlichen oder quartalsweisen BWA mit dem GF Klaerung der Abweichungen Steuerungsempfehlungen Risikoeskalation. Methodik Vorbereitun... |
| `stb-bwa-mandantenreport-monatlich` | Monatlicher Mandantenreport zusammenführend aus BWA SuSa OPOS Lohn Liquiditaet. Anwendungsfall standardisierter Monatsreport an Mandant per Mail oder Portal. Methodik 4-Seiten-Vorlage Cover BWA Kennzahlen Empfehlung. Output Mandantenrepo... |
| `stb-bwa-monatsabschluss-routine` | Routine für den Monatsabschluss in der Steuerberater-Kanzlei. Anwendungsfall monatliche BWA-Erstellung in einem standardisierten 30-Tage-Zyklus mit Belegabgabe Buchung Abstimmung BWA-Versand. Schritte Belegannahme Buchung GoBD-konform OP... |
| `stb-bwa-soll-ist-vergleich` | Soll-Ist-Vergleich in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Plan-Werten aus Wirtschaftsplan Unternehmensplanung Forecast. Methodik Planeingabe Abweichungsanalyse Steuerungsempfehlung. Output BWA mit Spalte Plan Ist Abweic... |
| `stb-bwa-statische-liquiditaet-kennzahlen` | Statische Liquiditaetskennzahlen Liquiditaet 1 2 3 Grades aus BWA und Bilanz. Anwendungsfall Quartalsauswertung Bankreporting Krisenfrueherkennung. Methodik Working Capital Aufstellung Anlagendeckung Kennzahlen. Output Liquiditaets-Kennz... |
| `stb-bwa-sus-bilanz-pruefung` | Workflow-Skill zu stb bwa sus bilanz pruefung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `stb-bwa-vorlaeufiges-ergebnis-darstellung` | Darstellung vorlaeufiges Ergebnis in Quartals- und Halbjahres-BWA. Anwendungsfall unterjaehrige BWA mit Vorlaeufigkeitsvermerk Bestand-Schaetzung noch nicht abgeschlossene Periodenabgrenzung. Methodik klare Trennung gebuchte versus gesch... |
| `stb-bwa-zeitlicher-vergleich-jahresvergleich` | Zeitvergleich Vorjahr und Vormonat in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Gegenüberstellung Vorjahres-Periode kumulierter Jahresvergleich Abweichungs-Analyse Trendaussage. Methodik gleicher Zeitraum gleiches Geschäftsmo... |
| `stb-bwa-zeitvergleich-vorjahr-darstellung` | Zeitvergleich Vorjahr in der BWA grafisch und tabellarisch. Anwendungsfall optische Aufbereitung der Vorjahresvergleichsdaten für Mandantengespraech mit Liniendiagrammen Balkengrafik. Methodik Standard-Tabelle plus Visualisierung. Output... |
| `stb-datentransfer-mandant-cloud-dsgvo` | Datentransfer Mandant zu Cloud DSGVO-Aspekte. Anwendungsfall Prüfung der DSGVO-Konformität beim Cloud-Datentransfer AVV Auftragsverarbeitung TOM technisch-organisatorische Massnahmen Drittlandtransfer. Methodik Prüfliste. Output DSGVO-Co... |
| `stb-datev-bwa-modul-bedienen-tipps` | DATEV Kanzlei-Rechnungswesen BWA-Modul Bedienung. Anwendungsfall Erstellung BWA in DATEV Auswahl Form Konfiguration Periodenvergleich Branchenvergleich. Methodik Workflow-Tipps. Output BWA-konfiguriert. |
| `stb-datev-lohn-modul-lodas-luh` | DATEV LODAS und Lohn und Gehalt LUG. Anwendungsfall Lohnabrechnung in DATEV-Welt Konfiguration ELSTER ELStAM sv.net Schnittstellen. Methodik Unterschiede LODAS vs Lohn und Gehalt Praxis-Tipps. Output Lohnprogramm konfiguriert. |
| `stb-dba-ansaessigkeit-tie-breaker-rules` | Ansaessigkeit nach Art. 4 OECD-Musterabkommen und Tie-Breaker-Regelungen bei mehrfacher Ansaessigkeit. Anwendungsfall natuerliche Person mit Wohnsitz in mehreren Staaten oder Kapitalgesellschaft mit Sitz und tatsaechlicher Geschäftsleitu... |
| `stb-dba-belgien` | DBA Deutschland Belgien aktuelle Fassung. Anwendungsfall Eupen Malmedy Grenzgaenger Pendler Beteiligungen Lizenzen. Anwendungsbereich Sprachgrenze. Loehne mit 183-Tage-Regelung. Pensionen mit Spezialregelung. Output Mandanten-Memo Berech... |
| `stb-dba-betriebsstaette-art-5-musterabkommen` | Betriebsstaette nach Art. 5 OECD-Musterabkommen einschließlich BEPS- und MLI-Anpassungen. Anwendungsfall Steuerberater prüfen ob auslaendische Aktivitaet eines deutschen Unternehmens oder umgekehrt eine Betriebsstaette begründet. Feste G... |
| `stb-dba-bulgarien` | DBA Deutschland Bulgarien 2010. Anwendungsfall Outsourcing IT Pflege Holding Beteiligungen. EU-MTRL ergaenzend. Niedrige KSt 10 Prozent. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-daenemark` | DBA Deutschland Daenemark aktuelle Fassung. Anwendungsfall Pendler Schleswig-Holstein Daenemark Beteiligungen Pensionen Sozialversicherung Lizenzen. Methodenartikel Freistellung mit Anrechnungswahl. Sonderregelungen Eisenbahn Schiff Luft... |
| `stb-dba-dividenden-quellensteuer-art-10` | Dividenden nach Art. 10 OECD-MA und EU-Mutter-Tochter-Richtlinie. Anwendungsfall Ausschuettungen über Grenze Quellensteuer im Quellenstaat Hoechstsatz Schachtelhoehe. § 43b EStG MTRL § 8b KStG Schachtelprivileg. Anti-Cum-Cum § 50j EStG.... |
| `stb-dba-estland` | DBA Deutschland Estland 1996. Anwendungsfall IT-Branche E-Residency Holding Beteiligungen. EU-MTRL ergaenzend. Besonderheit estnisches Steuersystem mit Besteuerung nur bei Ausschuettung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hin... |
| `stb-dba-finnland` | DBA Deutschland Finnland 2016. Anwendungsfall Maschinenbau IT Telekommunikation Pensionen Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-frankreich-1959` | DBA Deutschland Frankreich aus 1959 mit Aenderungsprotokollen. Anwendungsfall Pendler im Elsass und Lothringen Grenzgaengerregelung 20-km-Zone. Beteiligungen Pensionen Lizenzen. Aelteres DBA mit Sonderkonstruktionen abweichend vom OECD-M... |
| `stb-dba-grenzgaenger-frankreich-vor-allem-elsass` | Grenzgaengerregelung DBA Frankreich mit Schwerpunkt Elsass-Lothringen und 20-km-Zone. Anwendungsfall Arbeitnehmer Wohnsitz und Tätigkeit in Grenzgemeinde. Arbeitstaegliche Rückkehr 45-Tage-Schaedlichkeit. Beweismittel Reisekalender Arbei... |
| `stb-dba-grenzgaenger-oesterreich-rueckkehr` | Grenzgaengerregelung DBA Oesterreich mit Wohnsitz in der Grenznaehe und arbeitstaeglicher Rückkehr. Anwendungsfall Arbeitnehmer Wohnsitz Bayern oder Salzburg/Tirol Tätigkeit auf der anderen Seite. Home-Office-Konsultationsvereinbarung. O... |
| `stb-dba-grenzgaenger-schweiz-60-tage-rueckkehr` | Grenzgaengerregelung DBA Schweiz Art. 15a mit 60-Tage-Schaedlichkeit. Anwendungsfall Arbeitnehmer Wohnsitz Suedbaden Baden-Wuerttemberg Bayern Tätigkeit Schweiz. Arbeitstaegliche Rückkehr maximal 60 Nicht-Rückkehrtage je Kalenderjahr. Sc... |
| `stb-dba-griechenland` | DBA Deutschland Griechenland 1966. Anwendungsfall Schifffahrt Tourismus Pensionen Beteiligungen. EU-MTRL ergaenzend. Aelteres DBA. Methodenartikel Anrechnung Sonderregelungen. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-grossbritannien-2010` | DBA Deutschland Vereinigtes Koenigreich 2010 mit Protokollen 2014 und 2021. Anwendungsfall Brexit-Folgen Holding-Strukturen City-Branchen Pensionen Finanzdienstleistungen. Keine EU-Richtlinien nach Brexit. Methodenartikel Anrechnung. Out... |
| `stb-dba-grundprinzip-oecd-musterabkommen` | Grundprinzipien des OECD-Musterabkommens 2017 inkl. BEPS-Anpassungen und MLI für die Prüfung deutscher Doppelbesteuerungsabkommen. Anwendungsfall Steuerberater oder Steueranwalt arbeitet einen DBA-Sachverhalt vom Prüfungsschema her auf.... |
| `stb-dba-home-office-pandemie-folgeregelung` | Konsultations-Vereinbarungen zu Home-Office wahrend und nach Pandemie. Anwendungsfall Grenzüberschreitender Arbeitnehmer mit Home-Office-Tagen. Konkrete Vereinbarungen DE-Schweiz DE-Oesterreich DE-Luxemburg DE-Niederlande DE-Frankreich D... |
| `stb-dba-irland` | DBA Deutschland Irland 2011. Anwendungsfall IT- und Pharma-Holdings (Apple Google Pfizer), Holding-Strukturen, Lizenzeinkuenfte. EU-MTRL ergaenzend. Substanz Anti-Treaty-Shopping. Methodenartikel Anrechnung. Output Mandanten-Memo Holding... |
| `stb-dba-island` | DBA Deutschland Island. Anwendungsfall Fischerei Geothermie Tourismus Pensionen Beteiligungen. EWR-Status keine MTRL. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-israel-2014` | DBA Deutschland Israel Neufassung 2014 in Kraft 21.5.2016. Anwendungsfall Hightech IT Software-Lizenzen Holdings Pensionen Aliyah-Konstellation. Methodenartikel Anrechnung. MLI relevant. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hin... |
| `stb-dba-italien` | DBA Deutschland Italien aus 1989. Anwendungsfall Mittelstand Maschinenbau Mode Pharma Holding Pensionen Wegzug Suedtirol. EU-MTRL Subject-to-Tax-Klauseln. Methodenartikel Freistellung mit Aktivitaetsklausel. Output Mandanten-Memo Berechn... |
| `stb-dba-kanada-2001` | DBA Deutschland Kanada 2001. Anwendungsfall RRSP RRIF Pensionen Beteiligungen Branch Profits Tax. Auswanderung Quebec. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-kroatien` | DBA Deutschland Kroatien 2006. Anwendungsfall Tourismus Mittelstand Beteiligungen. EU-MTRL seit 2013. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-kuenstler-sportler-art-17-ma` | Kuenstler und Sportler nach Art. 17 OECD-MA mit Auftrittsstaat-Besteuerung. Anwendungsfall Musiker Schauspieler Sportler mit Auftritten in mehreren Staaten. Quellensteuer und BZSt-Anträge Anti-Treaty-Shopping nach § 50d Abs. 3 EStG. Outp... |
| `stb-dba-lettland` | DBA Deutschland Lettland 1997. Anwendungsfall Mittelstand IT Holding Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-litauen` | DBA Deutschland Litauen 1997. Anwendungsfall Mittelstand Logistik Holding Beteiligungen Fintech. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-lizenzgebuehren-art-12-bzst` | Lizenzgebühren nach Art. 12 OECD-MA und EU-Zins-Lizenzgebühren-Richtlinie. Anwendungsfall Software-Lizenz Patent Marken IP-Box-Konstruktionen. § 50g EStG ZinsLizenzRL § 50a EStG Steuerabzug § 50c EStG BZSt-Entlastung. Anti-Treaty-Shoppin... |
| `stb-dba-luxemburg-2012` | DBA Deutschland Luxemburg aktuelle Fassung 2012 mit Aenderungsprotokollen. Anwendungsfall Holding-Konstruktionen Soparfi Fondsstrukturen grenzüberschreitende Arbeitsverhältnisse mit hoher Pendlerzahl. Substanz Anti-Treaty-Shopping MLI Hy... |
| `stb-dba-malta-2001` | DBA Deutschland Malta 2001 mit Protokollen. Anwendungsfall Holding REIT-Strukturen Schifffahrt Online-Glueckspiel. EU-MTRL ergaenzend. Substanz Anti-Treaty-Shopping. Methodenartikel Anrechnung Aktivitaetsklausel. Output Mandanten-Memo Ho... |
| `stb-dba-methodenartikel-anrechnung-vs-freistellung` | Methodenartikel Art. 23A und Art. 23B OECD-Musterabkommen und Wahl zwischen Anrechnung und Freistellung mit Progressionsvorbehalt. Anwendungsfall Steuerberater entscheidet zwischen Anrechnungsmethode mit § 34c EStG und Freistellungsmetho... |
| `stb-dba-niederlande-2012` | DBA Deutschland Niederlande aktuelle Fassung 2012 in Kraft seit 2016. Anwendungsfall grenzüberschreitende Arbeitsverhältnisse Pensionen Beteiligungen Logistikbetriebsstaetten. Aktive Einkuenfte Freistellung mit Aktivitaetsklausel. Passiv... |
| `stb-dba-norwegen` | DBA Deutschland Norwegen. Anwendungsfall Oel und Gas Offshore Schifffahrt Mittelstand Pensionen Beteiligungen. EWR-Status keine MTRL. Methodenartikel Freistellung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-oesterreich` | DBA Deutschland Oesterreich aktuelle Fassung mit Protokollen. Anwendungsfall grenzüberschreitende Beschaeftigung Grenzgaenger Pensionen Beteiligungen Lizenzen Bauausführung. Grenzgaengerregelung Konsultations-Vereinbarungen Home Office.... |
| `stb-dba-polen` | DBA Deutschland Polen aktuelle Fassung 2003. Anwendungsfall Arbeitnehmer Entsendung Pendler Beteiligungen Lizenzen Bauausführung. EU-MTRL EU-ZinsLizenzRL ergaenzend. Methodenartikel Anrechnungsmethode mit Aktivitaetsklausel. Output Manda... |
| `stb-dba-portugal` | DBA Deutschland Portugal. Anwendungsfall Pensionen Algarve NHR-Status Beteiligungen Lizenzen Immobilien. EU-MTRL Madeira-Sondersteuergebiet. Methodenartikel Anrechnung mit Sonderregelungen. Output Mandanten-Memo Berechnungsbeispiel BZSt-... |
| `stb-dba-quellensteuer-erstattung-bzst-50c-estg` | Quellensteuerentlastung nach § 50c EStG beim Bundeszentralamt für Steuern BZSt. Anwendungsfall auslaendischer Empfaenger deutscher Kapitalertraege Lizenzen oder Verguetungen will deutsche Quellensteuer ermäßigen oder erstatten lassen. Fr... |
| `stb-dba-rentner-pensionen-art-18` | Rentenbesteuerung nach Art. 18 OECD-MA und Sonderregelungen einzelner DBA. Anwendungsfall Rentner mit Wohnsitz im Ausland (Spanien Portugal Italien Tuerkei Schweiz Oesterreich) oder auslaendische Rente bei Wohnsitz Deutschland. Wohnsitzs... |
| `stb-dba-rumaenien` | DBA Deutschland Rumaenien 2001. Anwendungsfall Automotive-Produktion IT Pflege Holding Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-russland-suspendierung-2024` | DBA Deutschland Russland Suspendierung wesentlicher Verguenstigungen. Russische Verbalnote vom 08.08.2023 suspendiert von russischer Seite Art. 5 bis 22 und 24. Deutsche Gegenmassnahme nach § 1 Abs. 3 Satz 2 StAbwG mit Aufnahme Russlands... |
| `stb-dba-schweden` | DBA Deutschland Schweden 1992. Anwendungsfall Mittelstand Maschinenbau Pendler Pensionen Beteiligungen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Freistellung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-schweiz` | DBA Deutschland Schweiz mit Schwerpunkt 60-Tage-Grenzgaengerregelung Art. 15a. Anwendungsfall Pendler Suedbaden Bodensee Zuerich Pauschalbesteuerung Wegzug Wegzugsbesteuerung Beteiligungen Lizenzen. Anrechnungsmethode Aktivitaetsklausel... |
| `stb-dba-serbien-montenegro` | Nachfolge-DBA Jugoslawien für Serbien und Montenegro. Anwendungsfall Mittelstand Diaspora Pensionen Bauausführung Beteiligungen. Aelteres DBA mit roemischen Artikelnummern. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbei... |
| `stb-dba-slowakei` | DBA Deutschland Slowakei aus 1980 fortgeltend gegenüber Nachfolgestaat. Anwendungsfall Automotive Zulieferung Beteiligungen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-slowenien` | DBA Deutschland Slowenien 2006. Anwendungsfall Mittelstand Automotive Tourismus Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-spanien-2011` | DBA Deutschland Spanien Neufassung 2011 in Kraft seit 2012. Anwendungsfall Mittelstand Immobilien Mallorca-Konstellation Pensionen Beteiligungen. EU-MTRL Subject-to-Tax-Klausel. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnun... |
| `stb-dba-tschechien` | DBA Deutschland Tschechien aus 1980 fortgeltend gegenüber Nachfolgestaat. Anwendungsfall grenzüberschreitende Arbeitsverhältnisse Bauausführung Beteiligungen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo... |
| `stb-dba-tuerkei-2011` | DBA Deutschland Tuerkei Neufassung 2011 in Kraft seit 1.8.2012 anwendbar ab 2012. Anwendungsfall Familienbande Deutschland-Tuerkei Arbeitseinkuenfte Pensionen Beteiligungen Bauausführung in der Tuerkei Holding. Quellensteuer differenzier... |
| `stb-dba-ukraine` | DBA Deutschland Ukraine. Anwendungsfall Mittelstand IT Pflege Holding Beteiligungen mit Konfliktrelevanz seit 2022. Sanktionen Devisenkontrollen Überweisungssperren. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel B... |
| `stb-dba-ungarn` | DBA Deutschland Ungarn 2011. Anwendungsfall Automotive-Zulieferer Holding Beteiligungen Pensionen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-usa-1989-protokoll-2006` | DBA Deutschland USA 1989 mit Protokollen 1998 2006 2021. LOB-Klausel Limitation on Benefits Substanztest. Pension Protection im Protokoll 2006. Branch Profits Tax. Anwendungsfall US-Holdings IRA 401(k) Roth Beteiligungen Sportler Kuenstl... |
| `stb-dba-zypern-2011` | DBA Deutschland Zypern 2011. Anwendungsfall Holding-Konstruktionen Schifffahrt Beteiligungen Investmentfonds. EU-MTRL ergaenzend. Substanz Anti-Treaty-Shopping. Methodenartikel Anrechnung. Output Mandanten-Memo Holding-Substanz-Memo BZSt... |
| `stb-drv-sozialversicherungspruefung` | Steuerberater-Begleitung der DRV-Sozialversicherungsprüfung nach § 28p SGB IV. Anwendungsfall Mandant-GmbH erhaelt DRV-Prüfankündigung oder Prüfung laeuft bereits. Prüfungsschwerpunkte Statusfeststellung GF Scheinselbstständigkeit Mini-... |
| `stb-eau-elektronische-arbeitsunfaehigkeit-2023` | eAU elektronische Arbeitsunfähigkeitsbescheinigung seit 2023. Anwendungsfall AN-Krankmeldung AG-Abruf bei Krankenkasse Entgeltfortzahlung. Methodik Schnittstelle Konfiguration Workflow. Output eAU-Konfiguration. |
| `stb-erechnung-pflicht-b2b-2025-2026` | eRechnung-Pflicht B2B seit 01.01.2025 § 14 UStG ViDA. Anwendungsfall Prüfung Mandantenbetrieb eRechnungs-Empfang Versand Übergangsfristen PDF reicht nicht mehr. Methodik Format XRechnung ZUGFeRD. Output eRechnungs-Konfiguration. |
| `stb-jahresabschluss-abgrenzungen-rap-rai` | Rechnungsabgrenzungsposten RAP aktiv und passiv. Anwendungsfall Jahresabschluss-Buchung Versicherung Miete Kfz-Steuer Vorauszahlungen periodengerechte Zuordnung. Methodik Identifikation Berechnung Buchung. Output Periodengerechte JA-Best... |
| `stb-jahresabschluss-anlagenverzeichnis-afa` | Anlagenverzeichnis und AfA-Buchung Jahresabschluss. Anwendungsfall vollständige Aktualisierung Anlagen Zugaenge Abgaenge AfA-Methoden Sonderabschreibung 7g 7b 6b EStG. Methodik AfA-Tabellen. Output Anlagenspiegel. |
| `stb-jahresabschluss-bestandskonten-abstimmung` | Bestandskonten-Abstimmung zum Jahresabschluss. Anwendungsfall Endbestaende Bank Kasse Forderungen Verbindlichkeiten Anlagen Eigenkapital abstimmen Inventur-Werte einarbeiten. Methodik Saldenabstimmung Vergleich. Output abgestimmte Bestan... |
| `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` | E-Bilanz § 5b EStG elektronische Übermittlung. Anwendungsfall Bilanzierer Pflicht zur elektronischen Übermittlung der Steuerbilanz an FA Taxonomie-Standard. Methodik DATEV-E-Bilanz Modul. Output E-Bilanz uebermittelt. |
| `stb-jahresabschluss-handels-vs-steuerbilanz` | Handelsbilanz vs Steuerbilanz Massgeblichkeit § 5 EStG. Anwendungsfall Prüfung Abweichungen Handels- und Steuerbilanz Massgeblichkeitsprinzip umgekehrte Massgeblichkeit Wahlrechte. Methodik Differenz-Tabelle Bewertungs-Unterschiede. Outp... |
| `stb-jahresabschluss-kassenfuehrung-gobd-pflichten` | Kassenführung GoBD-Pflichten. Anwendungsfall Mandanten mit Bargeschäft Kasse Aufzeichnungspflichten Kassenbuch elektronische Aufzeichnungssysteme TSE technische Sicherheitseinrichtung. Methodik Prüfung Sorgfalt. Output GoBD-konforme Kass... |
| `stb-jahresabschluss-rueckstellungen-bewertung` | Rückstellungen Bewertung § 249 HGB. Anwendungsfall Jahresabschluss Bildung Rückstellungen Garantie drohende Verluste Tantieme Urlaub Steuern Prozesskosten. Methodik Prüfung Anlass Quantifizierung Auflösung. Output Rückstellungs-Aufstellung. |
| `stb-jahresabschluss-veroeffentlichung-bundesanzeiger` | Jahresabschluss-Veröffentlichung Bundesanzeiger § 325 HGB. Anwendungsfall Pflichtveröffentlichung Kapitalgesellschaft Frist 12 Monate Groessenklassen Erleichterungen. Methodik elektronische Übermittlung. Output Bundesanzeiger-Eintrag. |
| `stb-jahresabschluss-vorbereitung-stichtag` | Jahresabschluss-Vorbereitung Stichtag. Anwendungsfall systematische JA-Vorbereitung Inventur Periodenabgrenzung Rückstellungen Anlagenspiegel. Methodik 8-Wochen-Vorlauf. Output JA-Vorbereitungs-Routine. |
| `stb-jahresabschluss-warenbestand-inventur` | Warenbestand und Inventur für Jahresabschluss. Anwendungsfall jaehrliche Inventur Aufnahme Warenbestand permanente Inventur Stichprobeninventur Bewertung. Methodik § 240 HGB GoBD. Output Inventur-Protokoll Warenbestand-Wert. |
| `stb-jahresgespraech-mandant-bwa-basis` | Jahresgespraech Mandant auf BWA-Basis. Anwendungsfall jaehrliches Bilanzgespraech nach Jahresabschluss-Erstellung Gesamtjahresblick Mehrjahres-Trend Strategie Folgejahr. Methodik intensive Vorbereitung 2-3 Stunden Termin Dokumentation. O... |
| `stb-kaltstart-interview` | Kaltstart-Interview für das Steuerberater-Plugin um Praxisprofil zu befuellen. Anwendungsfall Erstinstallation oder Konfiguration enthaelt noch Platzhalter-Marker oder Re-Interview mit --redo oder Konnektoren-Prüfung mit --integrationen-... |
| `stb-ki-tools-im-stb-betrieb-grenzen-berufsrecht` | KI-Tools im StB-Betrieb Berufsrechtliche Grenzen § 57 StBerG. Anwendungsfall ChatGPT Claude Microsoft Copilot Datev-KI Nutzung Mandantenkommunikation Berufsverschwiegenheit. Methodik Prüfung Compliance KI-VO Prüfraster. Output KI-Richtli... |
| `stb-liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau 3-6-12 Monate für GmbH oder UG erstellen mit insolvenzrechtlicher Fortbestehensprognose. Anwendungsfall Steuerberater begleitet Krisenmandat und benoetigt strukturierte Zahlungsplanung für Insolvenzreife-... |
| `stb-liquiditaetsvorschau-3wochen` | Steuerberaternahe Drei-Wochen-Liquiditaetsvorschau fuer § 17 InsO und § 102 StaRUG mit Wochenraster, Dokumentation und Quellenhygiene. Rechtsprechung nur nach Live-Pruefung. |
| `stb-lohn-abfindungen-besteuerung-funftel-regel` | Abfindungen Besteuerung Fuenftel-Regelung § 34 EStG. Anwendungsfall Aufhebungsvertrag Kündigung mit Abfindung Prüfung Voraussetzungen Fuenftel-Regel Berechnung Vorteilsvergleich. Methodik Berechnung mit DATEV LODAS. Output Lohn-Abrechnun... |
| `stb-lohn-arbeitgeber-arbeitnehmer-anteile` | Arbeitgeber- und Arbeitnehmer-Anteile in der SV. Anwendungsfall Verteilung der SV-Beitraege zwischen AG und AN PV-Zuschlag Kinderlose KV-Zusatzbeitrag Sonderbeitraege Lohnabrechnung. Methodik AG-AN-Aufteilung in DATEV LODAS. Output Lohna... |
| `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` | Arbeitsvertrag aus lohnrelevanter Sicht prüfen. Anwendungsfall Onboarding neuer AN Vertragsaenderungen Stundenlohn Festgehalt Sonderverguetungen Sachbezuege Dienstwagen JobRad bAV Vermögenswirksame Leistungen. Methodik Prüfraster lohnste... |
| `stb-lohn-aufzeichnungspflichten-milog` | Aufzeichnungspflichten nach MiLoG § 17 für Mindestlohn-relevante Branchen Geringfuegige Beschaeftigung. Anwendungsfall Prüfung Aufzeichnungspflicht 2 Jahre Aufbewahrung Schwarzarbeitsbekaempfung. Methodik Form der Aufzeichnung digitale L... |
| `stb-lohn-ausgleichszahlungen-altersteilzeit` | Altersteilzeit Block-Modell Gleichverteilungsmodell Aufstockungsbetrag. Anwendungsfall AN-Antrag Altersteilzeit ab 55 Block-/Gleichverteilungs-Variante AG-Aufstockung 20 Prozent steuerfrei. Methodik Prüfung AltTZG Berechnung. Output Alte... |
| `stb-lohn-bav-doppelversorgung-foerderung` | bAV bei mehreren Durchführungswegen Doppelversorgung Foerderung. Anwendungsfall AN hat Direktversicherung und Pensionskasse Beitragsobergrenzen gemeinsame Prüfung Hoechstforderung. Methodik kumulierte 8-Prozent-Prüfung. Output bAV-Prüfno... |
| `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` | Berufsgenossenschaft Lohnnachweis Jahresende. Anwendungsfall jaehrlicher Lohnnachweis an die zuständige BG Vorauszahlung BG-Beitrag Schluesseldaten Gefahrtarif. Methodik elektronischer Lohnnachweis über sv.net oder DAKOTA. Output BG-Lohn... |
| `stb-lohn-betriebliche-altersversorgung-grundlagen` | Betriebliche Altersversorgung bAV Grundlagen Durchführungswege. Anwendungsfall Beratung Mandant zu bAV Direktversicherung Pensionskasse Pensionsfonds Direktzusage Unterstuetzungskasse steuerliche und SV-rechtliche Behandlung. Methodik Ve... |
| `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro` | Aufmerksamkeiten 60 EUR-Freigrenze pro persoenlichem Anlass. Anwendungsfall Sachgeschenk zu Geburtstag Hochzeit Jubilaeum 60 EUR Hoechstwert LSt-frei. Methodik Abgrenzung zur 50 EUR-Sachbezugs-Freigrenze. Output korrekte Lohn-Behandlung... |
| `stb-lohn-betriebsveranstaltung-110-euro-freibetrag` | Betriebsveranstaltung 110 EUR-Freibetrag § 19 Abs 1 Nr 1a EStG. Anwendungsfall Firmenfeier Sommerfest Weihnachtsfeier Kostenkalkulation 110 EUR pro AN Pauschalierung. Methodik Berechnung Prüfung Belege. Output Lohn-Abrechnung mit Betrieb... |
| `stb-lohn-dienstwagen-1-prozent-fahrtenbuch` | Dienstwagen 1-Prozent-Methode oder Fahrtenbuch. Anwendungsfall geldwerter Vorteil Privatnutzung Dienstwagen E-Auto Hybrid Listenpreis Brutto-Methode. Methodik Prüfung Methode Vergleich Steuerklasse. Output Lohn-Abrechnung mit korrektem S... |
| `stb-lohn-direktversicherung-3-nr-63-estg` | Direktversicherung Steuerfreiheit § 3 Nr 63 EStG bis 8 Prozent BBG SV-frei bis 4 Prozent BBG. Anwendungsfall Entgeltumwandlung Direktversicherung Konfiguration Mandant AG-Zuschuss 15 Prozent. Methodik Beitragsberechnung Beitragsbemessung... |
| `stb-lohn-elternzeit-mutterschutz` | Elternzeit Mutterschutz Mutterschaftsgeld Elterngeld lohnrelevant. Anwendungsfall AN-Schwangerschaft Geburt Antrag Mutterschutz Elternzeit Auswirkung auf Lohn SV-Status Steuerprogression. Methodik Prüfung MuschG Beschaeftigungsverbot BEE... |
| `stb-lohn-firmenrad-leasing-jobrad` | JobRad Dienstrad Leasingmodell steuerliche Behandlung. Anwendungsfall AG-Leasing eines Fahrrads oder E-Bikes Überlassung an AN durch Gehaltsumwandlung Sachbezug von einem Viertel Prozent. Methodik Prüfung Konfiguration Leasingvertrag. Ou... |
| `stb-lohn-gesellschafter-geschaeftsfuehrer-sv` | Gesellschafter-Geschäftsführer GGF SV-Pflicht oder SV-Befreiung. Anwendungsfall Prüfung GGF einer GmbH ob abhaengig beschaeftigt oder selbständig tätig Statusfeststellung. Methodik Kriterienkatalog Beteiligung Weisungsgebundenheit Sperrm... |
| `stb-lohn-jahresmeldungen-ahn-asn-besondere` | Jahresmeldungen DEUEV Jahreslohnsumme Abmelde- und Sondermeldungen. Anwendungsfall Jahresende-Meldungen 15. Februar Folgejahr AN-Jahresarbeitsentgelt-Meldung Sondermeldungen Lohnsteuerbescheinigung. Methodik Standardablauf. Output Jahres... |
| `stb-lohn-jobticket-mobilitaet-deutschlandticket` | Jobticket Deutschlandticket steuerliche Behandlung. Anwendungsfall AG erstattet AN Mobilitaetsticket OePNV oder bietet Jobticket steuerfrei nach § 3 Nr 15 EStG Auswirkung auf Entfernungspauschale. Methodik Prüfung Konfiguration. Output L... |
| `stb-lohn-krankheit-entgeltfortzahlung-efzg` | Krankheit Entgeltfortzahlung 6 Wochen § 3 EFZG eAU. Anwendungsfall Lohnabrechnung bei Krankheit Entgeltfortzahlung 6 Wochen U1-Umlage Krankengeld Krankenkasse-Erstattung elektronische Arbeitsunfähigkeit. Methodik Prüfung Anspruch Berechn... |
| `stb-lohn-kurzarbeit-kug-progression` | Kurzarbeitergeld KUG Anmeldung Berechnung Progressionsvorbehalt. Anwendungsfall Kurzarbeit-Antrag bei der Bundesagentur Lohnabrechnung mit anteiligem Lohn und KUG Steuerprogressionsvorbehalt für AN. Methodik Prüfung Voraussetzungen Berec... |
| `stb-lohn-lohnsteuer-anmeldung-elster` | Elektronische Lohnsteuer-Anmeldung über ELSTER. Anwendungsfall monatliche oder vierteljaehrliche LSt-Anmeldung KiSt SolZ Pauschalierung Anmeldungs-Schema technische Übermittlung. Methodik Daten aus Lohnabrechnung ELSTER-Formular Prüfen S... |
| `stb-lohn-lohnsteuer-monatsabschluss` | Monatlicher Lohnsteuer-Monatsabschluss. Anwendungsfall regulaere Lohnabrechnung Bruttolohn LSt KiSt SolZ pauschalierte Loehne SV-Abrechnung Auszahlung Anmeldung. Methodik Standard-Workflow Abrechnungsschritte 39e Tabelle. Output Lohnabre... |
| `stb-lohn-mandantenaufnahme-onboarding` | Onboarding eines neuen Lohn-Mandanten. Anwendungsfall Erstaufnahme Stammdaten Arbeitnehmer-Liste Sozialversicherungs-Anmeldung Mandantenstamm DATEV LODAS oder Lohn und Gehalt. Methodik Checkliste Datenerfassung Prüfungen Dokumente. Outpu... |
| `stb-lohn-mehrarbeit-zuschlaege-39b-estg` | Sonn- Feiertag- und Nachtarbeitszuschlaege § 3b EStG. Anwendungsfall Lohnabrechnung mit Schichtzuschlaegen Gastronomie Pflege Sicherheitsdienst LSt-Freiheit SV-Freiheit in Grenzen. Methodik Prüfung Begrenzung Grundlohn Pflichtdokumentati... |
| `stb-lohn-meldungen-sv-elstam-zugang` | SV-Meldungen und ELStAM-Verfahren beim AN-Onboarding. Anwendungsfall Beschaeftigungsbeginn und Beendigung Anmeldung Abmeldung Aenderungsmeldung Sofortmeldung Sonderbranchen Elektronische LSt-Merkmale Abruf. Methodik DEUEV-Verfahren ELStA... |
| `stb-lohn-midi-job-uebergangsbereich-2000-euro` | Midi-Job-Übergangsbereich 538 EUR/01 bis 2000 EUR Stand 2023. Anwendungsfall geminderte AN-SV-Beitraege in der Gleitzone Berechnung Faktor F Anpassung 2026. Methodik Berechnungsmodul SV-Beitrag AN Gleitzone. Output Midi-Job-Abrechnung. |
| `stb-lohn-mindestlohn-aktuell-2026-anpassung` | Aktueller Mindestlohn 2026 Anpassung. Anwendungsfall Prüfung des aktuellen MiLo-Wertes Auswirkung auf Mini- Midi-Job-Grenzen Vertragsklauseln Mandanten-Information. Methodik Verifikation amtliche Quellen Mandantenkommunikation. Output Mi... |
| `stb-lohn-mini-midi-grenzen-2026-stand` | Aktuelle Mini- und Midi-Job-Grenzen 2026. Anwendungsfall Prüfung aktueller Schwellenwerte für Geringfuegigkeit und Übergangsbereich Verifikation gegen Mindestlohn-Anpassungen. Methodik Werteprüfung Quellen amtliche Veröffentlichungen. Ou... |
| `stb-lohn-minijob-538-euro-2024-anpassung` | Minijob 538 EUR-Grenze dynamisch an Mindestlohn gekoppelt seit 1.10.2022. Anwendungsfall geringfuegige Beschaeftigung pauschale Abgaben Beitragsbefreiung Steuerklassen-Frage Mehrfachbeschaeftigung. Methodik Prüfung 538 EUR-Grenze Aufzeic... |
| `stb-lohn-monatsende-meldepflichten-checkliste` | Lohn-Meldepflichten zum Monatsende Checkliste LSt-Anmeldung SV-Beitragsnachweis DEUEV BG-Lohnnachweis. Anwendungsfall standardisierter Prüfablauf vor Monatsende und Fristen Auswertung. Methodik Prüfliste Termincontrolling. Output Erledig... |
| `stb-lohn-praktikanten-azubis-loehne` | Praktikanten und Azubis lohnrelevante Sonderregeln. Anwendungsfall Pflichtpraktikum freiwilliges Praktikum Berufsausbildung BBiG Berufsausbildungsbeihilfe SV-Behandlung Vergueteung. Methodik Unterscheidung Pflicht- vs freiwilliges Prakti... |
| `stb-lohn-pruefungen-drv-bp-haftung-stb` | Prüfungen DRV-Prüfung Lohnsteuer-Aussenprüfung Steuerberater-Haftung. Anwendungsfall DRV-Prüfer kommt Prüfkriterien Nachforderung Haftungsrisiken Mandant. Methodik Vorbereitung Begleitung Reaktion. Output Prüfbericht Prüfverhandlung Mass... |
| `stb-lohn-sachbezuege-50-euro-freigrenze` | Sachbezuege 50 EUR Freigrenze § 8 Abs 2 EStG. Anwendungsfall geldwerte Vorteile Gutscheine Sachgeschenke Aufmerksamkeiten Begründung steuerfrei wenn unter 50 EUR/Monat. Methodik Prüfung Sachbezugs-Typ Geldzuwendung-Abgrenzung Loyalitaets... |
| `stb-lohn-statistik-meldungen-destatis` | Statistik-Meldungen Verdienststatistik Destatis. Anwendungsfall jaehrliche oder unterjaehrige Statistik-Meldungen an das Statistische Bundesamt Verdienste Arbeitszeit. Methodik Pflicht-Prüfung Erfassung Übermittlung. Output Statistik-Mel... |
| `stb-lohn-streitfaelle-bag-bsg-haftungsrisiko` | Lohn-Streitfaelle BAG-Linie BSG-Linie StB-Haftungsrisiko. Anwendungsfall typische Streitfaelle Werkvertrag versus AN Status arbeitsrechtlich vs sozialversicherungsrechtlich Klagerisiko. Methodik Rechtsprechungsanalyse Risikobewertung. Ou... |
| `stb-lohn-sv-beitraege-grundlagen` | Sozialversicherungs-Beitraege Grundlagen RV KV PV AV Umlagen. Anwendungsfall monatliche Lohnabrechnung mit SV-Berechnung Beitragsbemessungsgrenzen AG-AN-Aufteilung Sonderfaelle. Methodik Beitragsberechnung mit JAEG BBG Zusatzbeitrag KV.... |
| `stb-lohn-sv-meldungen-dakota-svnet` | SV-Meldungen über sv.net oder DAKOTA. Anwendungsfall Beitragsnachweis Meldung an Krankenkassen elektronische Übermittlung Prüfung Quittungen. Methodik System-Wahl Konfiguration. Output Meldebescheinigungen Quittungen. |
| `stb-lohn-ueberstunden-abbau-arbeitszeitkonto` | Überstunden Arbeitszeitkonto Stundenkonto Auszahlung. Anwendungsfall AN haeuft Überstunden an Bilanzierung im Arbeitszeitkonto Abbau in Freizeit oder Auszahlung lohn- und sv-rechtliche Behandlung. Methodik Aufzeichnung MiLoG Bewertung St... |
| `stb-lohn-umlage-u1-u2-insogeld-umlage` | Umlagen U1 U2 Insolvenzgeld-Umlage. Anwendungsfall AG-Umlagen monatlich Erstattung Krankheit Mutterschaft Insolvenz Berechnung Saetze Variabilitaet KK. Methodik Prüfung Pflicht Kleinunternehmer 30 AN. Output Umlage-Berechnung. |
| `stb-lohn-vermoegenswirksame-leistungen` | Vermögenswirksame Leistungen VL AG-Anteil AN-Sparzulage. Anwendungsfall AG-Zuschuss bis 480 EUR jaehrlich AN-Sparzulage einkommensabhaengig Bausparen Aktien-Fonds. Methodik Prüfung Antrag AN-Sparzulage Beratung. Output VL-Konfiguration. |
| `stb-lohn-werkstudent-pauschalen` | Werkstudent SV-Status 20-Stunden-Grenze pauschale Beitraege. Anwendungsfall Beschaeftigung Student Werkstudentenprivileg KV-Befreiung RV-Pflicht JAEG nicht relevant Klassifizierung. Methodik Prüfung 20-Stunden-Woche vorlesungsfreie Zeit... |
| `stb-mandanten-onboarding-checkliste-vollservice` | Onboarding-Checkliste Neumandant Vollservice. Anwendungsfall Mandatsannahme Standardablauf Mandantenvereinbarung Vollmachten DSGVO-Information Buchführung Lohn Steuererklärung. Methodik strukturierter Checkliste. Output Mandantenakte kom... |
| `stb-mandantenanfrage-reaktion-frist-laufend` | Mandantenanfragen Reaktionsfristen Servicelevel. Anwendungsfall Standardisierte Reaktion auf Mandantenanfragen klare Service-Versprechen Eskalation. Methodik SLA-Festlegung. Output Service-Standard-Dokument. |
| `stb-mandantenfragebogen-jahresabschluss` | Mandantenfragebogen zum Jahresabschluss. Anwendungsfall JA-Vorbereitung systematische Datenerhebung vom Mandanten Bestaende Forderungen Verbindlichkeiten Rückstellungen Sondervorgaenge. Methodik strukturierter Fragebogen Prüfliste. Outpu... |
| `stb-mandantenkommunikation-bwa-uebergabe-quartal` | Quartalsgespraech BWA-Übergabe. Anwendungsfall systematische Quartalskommunikation mit Mandant Ergebnisbesprechung Steuerthemen Investitionsplanung. Methodik Termin-Vorbereitung Agenda Dokumentation. Output Quartalsgespraechs-Protokoll M... |
| `stb-mandantenrechnung-honorar-stbvv` | Mandantenrechnung Honorar StBVV. Anwendungsfall Honorarabrechnung Pauschal- Zeit- und Gegenstandswert-Honorar Steuerberatergebührenverordnung. Methodik Rechnungsschreibung Gebührensaetze § 33 35 35a. Output Mandantenrechnung. |
| `stb-online-portal-datev-mandantenshop` | DATEV Unternehmen Online Mandantenshop. Anwendungsfall Belegtransfer Bank-Abruf Auswertungs-Download Mandantenakte digital für Mandant. Methodik Konfiguration Benutzer Schulung Mandant. Output eingerichtetes Portal. |
| `stb-pruefliste-belegabgabe-monatlich` | Prüfliste monatliche Belegabgabe. Anwendungsfall standardisierte Belegabgabe-Kontrolle Mandant Vollständigkeit Bankauszuege Kasse Eingangsrechnungen Ausgangsrechnungen Lohnauswertung. Methodik Prüfliste Eingangskontrolle Mahnung. Output... |
| `stb-routine-monatsabschluss-30-tage-zyklus` | Routine Monatsabschluss im 30-Tage-Zyklus. Anwendungsfall systematische Steuerung der Monatsabschluss-Routine in der Kanzlei mit klaren Deadlines Belegabgabe Buchung BWA-Versand USt-VA. Methodik Termin-Controlling. Output 30-Tage-Plan. |
| `stb-routine-quartalsabschluss-prozess` | Routine Quartalsabschluss-Prozess. Anwendungsfall vierteljaehrlicher Quartalsabschluss mit Periodenabgrenzung Quartals-BWA Mandantengespraech und Steuerthemen. Methodik strukturierter Quartals-Plan. Output Quartals-BWA Quartalsbericht Ge... |
| `stb-sage-buchhalter-bwa-konfiguration` | Sage Buchhalter BWA-Konfiguration. Anwendungsfall Mandanten oder Kanzleien mit Sage-Software statt DATEV/Addison. Methodik Unterschiede Konten BWA-Forms. Output BWA in Sage. |
| `stb-susa-anlagenkonten-ueberblick` | Anlagenbuchhaltung in der SuSa Anlagenkonten Klasse 0 SKR 03 immaterielle WG Sachanlagen Finanzanlagen Buchwerte. Anwendungsfall Monats- oder Jahres-SuSa mit Anlagenbestand AfA-Aktualisierung Zu- und Abgaenge. Methodik Anlagenspiegel-Abg... |
| `stb-susa-debitorenliste-osa-offene-posten` | Debitoren-Saldenliste und Offene-Posten-Auswertung OPOS. Anwendungsfall Monats- oder Quartalsauswertung Mahnwesen Forderungsanalyse Bilanzvorbereitung. Methodik OPOS-Liste Fälligkeitsstrukur Top-Schuldner Risikoprüfung. Output OPOS-Liste... |
| `stb-susa-erstellen-grundlagen` | Summen- und Saldenliste SuSa erstellen Grundlagen. Anwendungsfall monatliche Erstellung aus Finanzbuchhaltung Hauptbuchkonten Personenkonten Erfolgskonten Bestandsbuchungen. Methodik Aufbau Prüfung Verwendung. Output SuSa-Datei als Excel... |
| `stb-susa-formfehler-pruefen` | SuSa-Prüfung auf Formfehler Plausibilitaet und Differenzen. Anwendungsfall Qualitaetsprüfung der SuSa vor Versand oder Prüfung Buchungsdifferenzen typische Anomalien. Methodik Checkliste Plausibilitaet Differenz-Analyse. Output Fehlerpro... |
| `stb-susa-haupt-und-personenkonten` | SuSa-Auswertung Hauptbuchkonten und Personenkonten separat auswerten. Anwendungsfall Prüfung Hauptbuch Sammelkonten 1400 1500 vs Personenkonten Debitoren Kreditoren OPOS. Methodik Konsistenz Hauptbuch zu Personenkonten Abstimmung. Output... |
| `stb-susa-kreditorenliste-ova` | Kreditoren-Saldenliste OVA Offene-Verbindlichkeiten-Auswertung. Anwendungsfall Monats- oder Quartalsauswertung Zahlungsdisposition Lieferanten-Analyse Bilanzvorbereitung. Methodik Fälligkeitsstaffel Top-Lieferanten Skonti-Optionen. Outpu... |
| `stb-susa-monatlich-quartalsweise` | Periodische SuSa-Erstellung monatlich oder quartalsweise. Anwendungsfall standardisierter Erstellungsprozess Wahl der Periodizitaet Belegvolumen Mandantengroesse. Methodik Wahl der Frequenz Kommunikations-Routine. Output Periodische SuSa... |
| `stb-susa-saldenabstimmung-bestaetigung` | Saldenabstimmung und Saldenbestätigung im Jahresabschluss-Anlass. Anwendungsfall Bilanzvorbereitung Stichtag Forderungen und Verbindlichkeiten Lieferanten Kunden Banken. Methodik Abstimmungsschreiben Antwortauswertung Differenzklaerung.... |
| `stb-susa-saldennullstellung-jahresende` | Erfolgskonten-Saldennullstellung zum Jahresende. Anwendungsfall Jahresabschluss-Vorbereitung Schluss-SuSa GuV-Überleitung Bilanzgewinn auf Konto 800 oder 2000. Methodik Abschlussbuchungen über GuV-Konto. Output Geschlossene Erfolgskonten... |
| `stb-susa-vorperiode-vergleich` | SuSa-Periodenvergleich Vormonat und Vorjahr. Anwendungsfall Prüfung Salden-Konsistenz Saldenentwicklung Vergleich der einzelnen Konten über Perioden. Methodik Differenz-Tabelle Auffälligkeit Hinweis-Liste. Output SuSa mit Vergleichsspalt... |
| `stb-ueberschuldungspruefung-19-inso` | Workflow-Skill zu stb ueberschuldungspruefung 19 inso. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `stb-warnschreiben-krisensignale` | Workflow-Skill zu stb warnschreiben krisensignale. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `vergleichsverhandlung-strategie` | Workflow-Skill zu vergleichsverhandlung strategie. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
