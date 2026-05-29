# verfassungsrecht

Deutsches Verfassungsrecht unter dem Grundgesetz aus der Sicht einer verfassungsrechtlichen Spezialkanzlei. **Rechtsprechungsgetrieben** mit verpflichtender Live-Recherche auf [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) und einem internen Kanon der ca. 50 wichtigsten Leitentscheidungen mit Aktenzeichen, Randnummer und URL.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Verfassungsrecht (`verfassungsrecht`, dieses Plugin) | [verfassungsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verfassungsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Wofür

- Prüfung, ob ein Gesetz vom **zuständigen Gesetzgeber** erlassen wurde (Art. 70–74 GG).
- Prüfung der **formellen Verfassungsmäßigkeit** (Verfahren Art. 76–82 GG, Zitiergebot Art. 19 I 2 GG, Bestimmtheitsgebot, Wesentlichkeitstheorie/Parlamentsvorbehalt).
- Prüfung der **materiellen Verfassungsmäßigkeit** der Grundrechte (Schutzbereich, Eingriff, verfassungsrechtliche Rechtfertigung mit Verhältnismäßigkeit).
- Begleitung im konkreten Mandat: Verfassungsbeschwerde nach § 90 BVerfGG, Stellungnahmen, Gutachten.
- Begleitung des Gesetzgebers: GG-Konformitätscheck eines Entwurfs vor Einbringung.

## Disclaimer

Verfassungsrecht ist ein hochspezialisiertes Rechtsgebiet mit existentiellen Folgen für Mandanten und Allgemeinheit. Die Ausgaben dieses Plugins sind **kein Ersatz** für die anwaltliche Mandatsbearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Insbesondere Verfassungsbeschwerden unterliegen strengen Zulässigkeits­anforderungen und Fristen (§§ 90 ff. BVerfGG, § 93 BVerfGG).

## Skills

- **`bverfg-rechtsprechung-recherchieren`** — Live-Recherche auf bundesverfassungsgericht.de plus Kanon-Referenz (Az., Rn., URL). Verbindlicher Einstiegspunkt vor jeder verfassungsrechtlichen Aussage.
- **`verfassungsrechtliche-pruefung`** — Master-Workflow: Gesamtschema formelle + materielle Verfassungsmäßigkeit.
- **`gesetzgebungskompetenz-pruefen`** — Art. 70–74 GG, ausschließliche/konkurrierende/Rahmen, Erforderlichkeitsklausel Art. 72 II GG.
- **`formelle-verfassungsmaessigkeit`** — Verfahren Art. 76–82 GG (drei Lesungen, Bundesrat, Ausfertigung), Zitiergebot Art. 19 I 2 GG, Bestimmtheitsgebot, Wesentlichkeitstheorie/Parlamentsvorbehalt.
- **`grundrechtspruefung`** — Schutzbereich-Eingriff-Rechtfertigung mit Drei-Stufen-Theorie (Apothekenurteil), Schranken-Schranken, Wechselwirkungslehre (Lüth).
- **`verhaeltnismaessigkeit`** — Vier-Stufen-Prüfung: legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit, jeweils mit BVerfG-Pinpoint.
- **`verfassungsbeschwerde-entwurf`** — § 90 BVerfGG: Beschwerdebefugnis, Rechtswegerschöpfung, Subsidiarität, Begründungsanforderungen, Frist.
- **`gesetzentwurf-gg-konformitaet-pruefen`** — Gesetzgeber-/Ministeriumssicht: GG-Check vor Einbringung des Entwurfs.

## Referenzen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenstrategie

1. **Primär:** Live-Suche auf [www.bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) (offizielle Entscheidungssammlung). Zitat immer mit Aktenzeichen, Randnummer und URL.
2. **Sekundär:** Eigene Kanon-Referenz unter `references/bverfg-leitentscheidungen.md` als Schnellzugriff.
3. **Ersatzweise:** [servat.unibe.ch/dfr/](https://www.servat.unibe.ch/dfr/) (DFR-Volltextsammlung BVerfGE), [opinioiuris.de](https://opinioiuris.de), [dejure.org](https://dejure.org) — nur wenn auf bundesverfassungsgericht.de nicht greifbar.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Jede verfassungsrechtliche Aussage benötigt eine BVerfG-Pinpoint-Quelle (Az. + Rn.). Modellwissen ohne Quelle wird als `[zu verifizieren auf bundesverfassungsgericht.de]` markiert.

## Hinweis zum berufsrechtlichen Rahmen (Stand Mai 2026)

Anwältinnen und Anwälte sind nach **§ 203 StGB** (Verletzung von Privatgeheimnissen) und **§ 43a BRAO** (anwaltliche Verschwiegenheitspflicht) zur Verschwiegenheit verpflichtet. Eine unmittelbare Weitergabe mandatsbezogener Daten an außereuropäische KI-Anbieter ohne datenschutzkonformes Setup ist berufsrechtlich riskant und kann strafrechtliche Folgen haben. Deshalb empfiehlt sich der Betrieb über einen **deutschen Zwischenanbieter** (z. B. § 203-konformes Cowork-Setup; siehe [README im Repo-Root](../README.md#einrichtungsleitfaden-fuer--203-konformes-cowork-ueber-deutschen-zwischenanbieter)), der als Auftragsverarbeiter nach Art. 28 DSGVO eingebunden ist und die Weiterleitung an den KI-Anbieter pseudonymisiert/anonymisiert handhabt.

**Disclaimer:** technische, **keine juristische** Auskunft; die Tool-Landschaft entwickelt sich seit Frühjahr 2026 sehr dynamisch. Die berufsrechtlichen Pflichten nach § 203 StGB und § 43a BRAO bleiben in jedem Fall in der Verantwortung der jeweiligen Anwältin / des jeweiligen Anwalts.
