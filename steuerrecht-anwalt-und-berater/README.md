# Steuerberater und Fachanwalt für Steuerrecht

Konsolidiertes Steuerrecht-Plugin für drei Zielgruppen: Steuerrechtsanwälte, Fachanwälte für Steuerrecht und Steuerberater. Umfasst das vollständige Mandats-Workflow von der Bescheidanalyse über Einspruch und Klage bis zu Selbstanzeige und Außenprüfung — sowie Steuerberater-Werkzeuge für BWA-/SuSa-/Bilanzprüfung und Krisenfrüherkennung.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen bzw. steuerlichen Prüfung — zitiert, mit Prüfhinweisen versehen. Das Plugin erledigt die Recherchearbeit. Die rechtliche Beurteilung und die Entscheidung liegen beim Rechtsanwalt, Fachanwalt für Steuerrecht oder Steuerberater.** Folgenreiche Handlungen — Einreichen, Versenden, Vollziehen — erfordern ausdrückliche Freigabe.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Steuerberater und Fachanwalt für Steuerrecht (`steuerrecht-anwalt-und-berater`) | [steuerrecht-anwalt-und-berater.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/steuerrecht-anwalt-und-berater.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json` und `skills/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus „Code → Download ZIP" verwenden.

---

## Für Steueranwälte (anw-...)

Skills für steuerrechtliche Anwaltskanzleien — streitbezogene Folgebearbeitung von Bescheiden, nicht Steuererklärungserstellung.

| Skill | Funktion |
|---|---|
| `/steuerrecht-anwalt-und-berater:anw-kaltstart-interview` | Ersteinrichtung — Kanzleiprofil, Schwerpunkte, Finanzämter, FG-Bezirke |
| `/steuerrecht-anwalt-und-berater:anw-mandat-triage-steuerrecht` | Eingangs-Triage: Steuerart, Vorgang, Fristen, Eskalation |
| `/steuerrecht-anwalt-und-berater:anw-steuerbescheid-analyse` | Steuerbescheid systematisch auswerten vor Einspruch |
| `/steuerrecht-anwalt-und-berater:anw-einspruch-finanzamt` | Einspruch § 347 AO mit AdV-Antrag und Akteneinsicht |
| `/steuerrecht-anwalt-und-berater:anw-aussetzung-vollziehung` | AdV-Antrag zweistufig: FA § 361 AO + FG § 69 Abs. 3 FGO |
| `/steuerrecht-anwalt-und-berater:anw-klage-finanzgericht` | Klage zum Finanzgericht § 40 ff. FGO |
| `/steuerrecht-anwalt-und-berater:anw-akteneinsicht-steuerakte` | Akteneinsicht § 364 AO / § 78 FGO / Art. 15 DSGVO |
| `/steuerrecht-anwalt-und-berater:anw-aussenpruefung-strategien` | Außenprüfung §§ 193 ff. AO: Begleitung, Strategie, Schlussbesprechung |
| `/steuerrecht-anwalt-und-berater:anw-selbstanzeige-371` | Selbstanzeige § 371 AO — Hochrisikobereich, Pflichtprüfung mehrere Anwälte |
| `/steuerrecht-anwalt-und-berater:anw-verbindliche-auskunft` | Verbindliche Auskunft § 89 Abs. 2 AO |
| `/steuerrecht-anwalt-und-berater:anw-fristenbuch-steuerrecht` | Fristenbuch: Einspruchsfrist, Klagefrist, Vorfristen |
| `/steuerrecht-anwalt-und-berater:anw-betriebsausgaben-werbungskosten-pruefraster` | Prüfraster Betriebsausgaben/Werbungskosten § 4 Abs. 4 / § 9 EStG |
| `/steuerrecht-anwalt-und-berater:anw-umsatzsteuer-vorsteuerabzug-pruefen` | Vorsteuerabzug § 15 UStG — Prüfraster |

### Ersteinrichtung

```
/steuerrecht-anwalt-und-berater:anw-kaltstart-interview
```

Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` gespeichert.

---

## Für Fachanwälte (fa-...)

Skills für Fachanwälte für Steuerrecht nach FAO § 9 — Orientierung, Übersicht, Schnittstellen.

| Skill | Funktion |
|---|---|
| `/steuerrecht-anwalt-und-berater:fa-orientierung` | Orientierung Steuerrecht und FAO § 9 — AO EStG KStG UStG FGO Steuerstrafrecht |

---

## Für Steuerberater (stb-...)

Skills für Steuerberater und GmbH-Geschäftsleitung — BWA-/SuSa-/Bilanzprüfung und Krisenfrüherkennung.

| Skill | Funktion |
|---|---|
| `/steuerrecht-anwalt-und-berater:stb-kaltstart-interview` | Ersteinrichtung — Praxisprofil, Mandanten-Schwerpunkte, Buchhaltungssystem |
| `/steuerrecht-anwalt-und-berater:stb-bwa-sus-bilanz-pruefung` | BWA-/SuSa-/Bilanzprüfung auf Krisensignale (§§ 17, 19 InsO, § 102 StaRUG) |
| `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3wochen` | 3-Wochen-Liquiditätsvorschau § 17 InsO Vorprüfung |
| `/steuerrecht-anwalt-und-berater:stb-liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose |

> **Hinweis:** Die vollständige Power-Version der Liquiditätsvorschau (BGH-Schema Passiva II, Excel-Vorlage, HTML-Padlet) lebt im Plugin [`liquiditaetsplanung`](../liquiditaetsplanung/). Die `stb-`-Skills verweisen bei installiertem `liquiditaetsplanung` dorthin.

---

## Testakten

Drei fiktive Mandatsakten zum Ausprobieren der Skills:

| Testakte | Inhalt | Passt besonders zu |
|---|---|---|
| [`beispielakte-edelholz-berlin`](../testakten/beispielakte-edelholz-berlin/) | Edelholz Manufaktur Berlin GmbH — BWA, SuSa, Liquiditätslage, Steuern/SV-Rückstände | `stb-bwa-sus-bilanz-pruefung`, `stb-liquiditaetsvorschau-3wochen` |
| [`fortbestehensprognose-paragrafix-gmbh`](../testakten/fortbestehensprognose-paragrafix-gmbh/) | Paragrafix GmbH — Legal-AI-Startup, § 102-StaRUG-Hinweis, BWA, SuSa, 13-Wochen-Liquiditätsplanung | `stb-bwa-sus-bilanz-pruefung`, `stb-liquiditaetsvorschau-3-6-12-monate` |
| [`grosskanzlei-corporate-ma-datenraum`](../testakten/grosskanzlei-corporate-ma-datenraum/) | Projekt Silberfalke — Umwandlungs- und Steuerstruktur, verbindliche Auskunft, Außenprüfung im M&A-Kontext | `anw-verbindliche-auskunft`, `anw-aussenpruefung-strategien` |

---

## Voraussetzungen

- **Persistenter Datenpfad.** Konfiguration und Fristenbücher werden unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/` gespeichert. Diese Dateien enthalten mandatsbezogene Daten — Verzeichnis sichern und zugriffsschützen (Art. 5 Abs. 1 lit. f DSGVO, § 43a Abs. 2 BRAO).
- **Rechtsdatenbank-Zugang.** Skills speichern keine konkreten Normtexte. Normen werden zum Zeitpunkt der Prüfung recherchiert und zitiert.
- **Steuerberater für Steuererklärungen.** Dieses Plugin ist auf anwaltlich-streitbezogene Folgebearbeitung und Steuerberater-Krisenprüfung ausgerichtet — nicht auf DATEV-Steuererklärungserstellung.
- **Mandatsgeheimnis.** § 43a Abs. 2 BRAO, § 203 StGB und § 53 StPO gelten für alle Ausgaben. Keine Weitergabe vertraulicher Mandantendaten ohne ausdrückliche Freigabe.
