---
name: bverfg-rechtsprechung-recherchieren
description: "BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Output: Rechtsprechungsueberblick Zitatliste Leitentscheidungen. Abgrenzung: nicht für Verfassungsbeschwerde-Entwurf (verfassungsbeschwerde-entwurf) im Verfassungsrecht."
---

# BVerfG-Rechtsprechung recherchieren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: BVerfG-Rechtsprechung recherchieren
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

**Dieser Skill ist der verbindliche Einstieg jeder verfassungsrechtlichen Aussage in diesem Plugin.** Ohne BVerfG-Pinpoint kein verfassungsrechtliches Ergebnis.

## Disclaimer

Verfassungsrechtliche Prüfungen sind hochkomplex und mandantenrelevant. Diese Recherche ist eine Unterstützung, **kein Ersatz** für anwaltliche Bearbeitung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenhierarchie

1. **Primär:** [www.bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) — offizielle Entscheidungssammlung, Pfad `/SharedDocs/Entscheidungen/DE/<Jahr>/<Monat>/<Az.>.html`. Pressemitteilungen unter `/SharedDocs/Pressemitteilungen/`.
2. **Sekundär:** Eigene Kanon-Referenz `references/bverfg-leitentscheidungen.md`.
3. **Ersatzweise:** [servat.unibe.ch/dfr/](https://www.servat.unibe.ch/dfr/) (DFR-Volltextsammlung BVerfGE), [opinioiuris.de](https://opinioiuris.de), [dejure.org](https://dejure.org).
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Modellwissen ohne Quelle ist verboten.** Wo Computer kein Pinpoint-Zitat liefern kann, ist die Aussage als `[zu verifizieren auf bundesverfassungsgericht.de]` zu markieren.

## Workflow

### Schritt 1 — Frage präzisieren

- Welche Norm, welches Verhalten, welcher Akt der öffentlichen Gewalt steht zur Prüfung?
- Welches Grundrecht oder welcher staatsorganisationsrechtliche Aspekt ist betroffen?
- Welche Doktrin könnte einschlägig sein (Drei-Stufen-Theorie, Wesentlichkeit, Verhältnismäßigkeit, Wechselwirkung, intertemporale Freiheitssicherung)?

### Schritt 2 — Kanon-Treffer prüfen

Konsultiere zuerst `references/bverfg-leitentscheidungen.md`. Wenn dort einschlägige Leitentscheidungen aufgeführt sind, nutze deren Az., Datum und URL als Ausgangspunkt.

### Schritt 3 — Live-Recherche auf bundesverfassungsgericht.de

- Volltextsuche auf [www.bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) (Lupe oben rechts).
- Bei Pressefragen: [Pressemitteilungen](https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/DE/_pressemitteilungen.html).
- Bei aktueller Rechtsprechung: Filterung nach Datum.
- URL-Muster der Entscheidung: `https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/<Jahr>/<MM>/<Aktenzeichen-bereinigt>.html`.

### Schritt 4 — Pinpoint extrahieren

Pflichtangaben für jede Aussage:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Datum** der Entscheidung
- **Randnummer** der einschlägigen Passage (z. B. `Rn. 117`)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **URL** der amtlichen Sammlung

### Schritt 5 — Zitat formatieren

Standardformat in allen Outputs dieses Plugins:

```
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2021/03/rs20210324_1bvr265618.html
```

Bei Beschluss statt Urteil entsprechend.

### Schritt 6 — Gegenprüfung

- Ist die Entscheidung nicht teilweise oder vollständig aufgegeben durch spätere Rechtsprechung? Prüfe Folgejudikate.
- Ist sie auf den vorliegenden Sachverhalt übertragbar? Achte auf abweichende Konstellationen.
- Bei älteren Entscheidungen: prüfe, ob die zugrunde liegende Norm noch existiert / aktueller Fassung entspricht.

## Standardroutinen

### Routine A — Grundrecht identifizieren

1. Schutzbereichseröffnung dem Wortlaut nach prüfen (Art. 2–19 GG).
2. Kanon checken: `references/bverfg-leitentscheidungen.md` Sektion zum betroffenen Grundrecht.
3. Live-Recherche für aktuelle Auslegungslinie.

### Routine B — Verhältnismäßigkeit überprüfen

1. Kanon: legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Live-Recherche: BVerfG-Linie der letzten 5 Jahre zum konkreten Grundrechtseingriff.

### Routine C — Gesetzgebungskompetenz prüfen

1. Art. 70–74 GG durchgehen.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Live-Recherche bei Spezialmaterien.

## Output-Vorgaben für andere Skills

Jeder andere Skill dieses Plugins, der eine verfassungsrechtliche Aussage trifft, **muss** vorher diesen Skill aufrufen und mindestens eine Pinpoint-Quelle pro tragender Aussage liefern. Aussagen ohne BVerfG-Pinpoint sind kenntlich zu machen mit `[zu verifizieren auf bundesverfassungsgericht.de]`.

## Disclaimer-Wiederholung

Auch eine sorgfältige Recherche ersetzt nicht die anwaltliche Mandatsbearbeitung. Insbesondere bei Verfassungsbeschwerden ist eine Spezialkanzlei einzuschalten (Fristen § 93 BVerfGG, Begründungsanforderungen § 23 Abs. 1 BVerfGG, Subsidiarität).

## Aktualität — Auswahl 2024/2025/2026 (Pinpoint live verifizieren)

Die folgenden Entscheidungen sind in jüngerer Zeit für die Pluginarbeit besonders relevant. Vor Verwendung im Schriftsatz auf der offiziellen Seite [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) Rn. und Tenor verifizieren.

- 1 BvL 3/22, Beschl. v. 14.11.2024 — Längerfristige Observation/Bildaufnahmen PolG NRW ohne hinreichende Eingriffsschwelle verfassungswidrig; Übergangsfortgeltung bis 31.12.2025 — [URL](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2024/11/ls20241114_1bvl000322.html).
- 1 BvR 2466/19 (Trojaner I) und 1 BvR 180/23 (Trojaner II), beide Beschlüsse vom 07.08.2025 — präventiv-polizeirechtliche und strafprozessuale Quellen-TKÜ/Online-Durchsuchung; präventiv im Wesentlichen verfassungskonform, StPO-Befugnisse für Niedrig-Strafrahmen teilweise nichtig.
- 1 BvR 2656/18 u. a. (Klimabeschluss), Beschl. v. 24.03.2021 — intertemporale Freiheitssicherung Art. 20a GG — [URL](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2021/03/rs20210324_1bvr265618.html).
- Jahresbericht BVerfG 2025 (Polizeikosten Hochrisikospiele u. a.) — [PDF](https://www.bundesverfassungsgericht.de/SharedDocs/Downloads/DE/Jahresbericht/jahresbericht_2025.pdf).

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 93 BVerfGG
- § 32 BVerfGG
- § 90 BVerfGG
- Art. 82 GG
- Art. 73 GG
- Art. 100 GG
- Art. 79 GG
- § 92 BVerfGG
- Art. 93 GG
- Art. 74 GG
- § 93a BVerfGG
- Art. 76 GG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

