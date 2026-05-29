---
name: bverfg-rechtsprechung-recherchieren
description: "BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Output: Rechtsprechungsueberblick Zitatliste Leitentscheidungen. Abgrenzung: nicht für Verfassungsbeschwerde-Entwurf (verfassungsbeschwerde-entwurf)."
---

# BVerfG-Rechtsprechung recherchieren

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
