# Megaprompt: verfassungsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `verfassungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Verfassungsrecht: ordnet Rolle (Beschwerdeführer, Beschwerdegegner, BVerfG), markiert F…
2. **bverfg-rechtsprechung-recherchieren** — BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BV…
3. **dokumente-intake** — Dokumentenintake für Verfassungsrecht: sortiert Letzter fachgerichtl. Beschluss, Verfassungsbeschwerde-Schriftsatz, Vorl…
4. **formelle-verfassungsmaessigkeit** — Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen A…
5. **gesetzentwurf-gg-konformitaet-pruefen** — Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzi…
6. **gesetzgebungskompetenz-pruefen** — Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompe…
7. **grundrechtspruefung-acht-formelle-interessen** — Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG G…
8. **verfassungsbeschwerde-entwurf-formelle** — Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt…
9. **verfassungsrechtliche-pruefung** — Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisati…
10. **verhaeltnismaessigkeit** — Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BV…
11. **start-chronologie-fristen** — Einstieg, Schnelltriage und Fallrouting im Verfassungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und …
12. **verfassung-grundrechte-uebersicht** — Grundrechte des GG Ueberblick: Art. 1 Wuerde, Art. 2 freie Entfaltung, Art. 3 Gleichheit, Art. 4 Glaubensfreiheit, Art. …
13. **unterlagen-luecken** — Lücken- und Beschaffungsliste für Verfassungsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Letzter fachgericht…
14. **anschluss-routing** — Anschluss-Routing für Verfassungsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 93 BVerfGG 1 Monat Verfassungsb…
15. **vfgr-verfassungsbeschwerde-substantiierung-spezial** — Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittel…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Verfassungsrecht: ordnet Rolle (Beschwerdeführer, Beschwerdegegner, BVerfG), markiert Frist (§ 93 BVerfGG 1 Monat Verfassungsbeschwerde), wählt Norm (GG, BVerfGG, Landesverfassungen) und Zuständigkeit (BVerfG), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Verfassungsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `acht-zahlen-schwellen-und-berechnung` — Acht Zahlen Schwellen und Berechnung
- `bundesverfassungsgericht-quellenkarte-check` — Bundesverfassungsgericht Quellenkarte Check
- `bverfg-rechtsprechung-recherchieren` — Bverfg Rechtsprechung Recherchieren
- `bverfg-verfahrenssicht-und-annahmerisiko` — Bverfg Verfahrenssicht und Annahmerisiko
- `formelle-mehrparteien-konflikt-und-interessen` — Formelle Mehrparteien Konflikt und Interessen
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf GG Konformitaet Pruefen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Pruefen
- `grundgesetz-fristen-form-und-zustaendigkeit` — Grundgesetz Fristen Form und Zustaendigkeit
- `grundrechte-fehlerkatalog` — Grundrechte Fehlerkatalog
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `grundrechtspruefung-und-verhaeltnismaessigkeit` — Grundrechtspruefung und Verhaeltnismaessigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 93 BVerfGG Verfassungsbeschwerde 1 Monat nach Rechtswegerschöpfung / 1 Jahr bei Gesetzen, § 32 BVerfGG einstweilige Anordnung.
- Fachpfad wählen: zentrale Anker im Verfassungsrecht sind GG Art. 1–19, 20, 28, 33, 38, 79, 93, 100, BVerfGG §§ 13, 23, 31, 32, 90–95a, EMRK Art. 6, 8, 10, 13. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `bverfg-rechtsprechung-recherchieren`

_BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Output: Rechtsprechungsueberblick Zitatliste Leitentscheidungen...._

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

---

## Skill: `dokumente-intake`

_Dokumentenintake für Verfassungsrecht: sortiert Letzter fachgerichtl. Beschluss, Verfassungsbeschwerde-Schriftsatz, Vorlagebeschluss, prüft Datum, Absender, Frist und Beweiswert (Tragende Erwägungen Vorinstanzen, Substantiierung Grundrechtsverletzung); markiert Lücken; berücksichtigt Mandatsgehei..._

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Verfassungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Verfassungsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `acht-zahlen-schwellen-und-berechnung` — Acht Zahlen Schwellen und Berechnung
- `bundesverfassungsgericht-quellenkarte-check` — Bundesverfassungsgericht Quellenkarte Check
- `bverfg-rechtsprechung-recherchieren` — Bverfg Rechtsprechung Recherchieren
- `bverfg-verfahrenssicht-und-annahmerisiko` — Bverfg Verfahrenssicht und Annahmerisiko
- `formelle-mehrparteien-konflikt-und-interessen` — Formelle Mehrparteien Konflikt und Interessen
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf GG Konformitaet Pruefen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Pruefen
- `grundgesetz-fristen-form-und-zustaendigkeit` — Grundgesetz Fristen Form und Zustaendigkeit
- `grundrechte-fehlerkatalog` — Grundrechte Fehlerkatalog
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `grundrechtspruefung-und-verhaeltnismaessigkeit` — Grundrechtspruefung und Verhaeltnismaessigkeit
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Verfassungsbeschwerde, Antrag auf einstweilige Anordnung, Annahmebeschluss, BVerfGE-Entscheidung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Verfassungsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: GG Art. 1–19, 20, 28, 33, 38, 79, 93, 100, BVerfGG §§ 13, 23, 31, 32, 90–95a, EMRK Art. 6, 8, 10, 13 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `formelle-verfassungsmaessigkeit`

_Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG Verfahren Art. 76-78 GG Ausfertigung Art. 82 GG. Output: Formelle Prüfmemo mit E..._

# Formelle Verfassungsmäßigkeit prüfen

## Arbeitsbereich

Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG Verfahren Art. 76-78 GG Ausfertigung Art. 82 GG. Output: Formelle Prüfmemo mit Ergebnis. Abgrenzung: nicht für materielle Verfassungsmäßigkeit (grundrechtsprüfung). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Formelle Verfassungsmäßigkeit prüfen
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer

Die formelle Verfassungsmäßigkeit kann im Streitfall nur durch das BVerfG verbindlich geklärt werden (Verwerfungsmonopol Art. 100 Abs. 1 GG). Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Jede Aussage benötigt BVerfG-Pinpoint (Az. + Rn. + URL).

## Prüfungsschritte

### Schritt 1 — Verfahren (Art. 76–82 GG)

#### 1a. Einbringung (Art. 76 GG)

- **Initiativrecht:** Bundesregierung, Bundestag (aus der Mitte, § 76 GOBT: Fraktion oder 5 % der Abgeordneten), Bundesrat.
- **Erster Durchgang:** Bei Initiative aus Bundesregierung oder Bundesrat ist die jeweils andere Seite zur Stellungnahme zu hören (Art. 76 Abs. 2, 3 GG).

#### 1b. Drei Lesungen im Bundestag (§§ 78–86 GOBT)

- **Erste Lesung:** Aussprache (oder Überweisung ohne Aussprache), Überweisung an den federführenden Ausschuss.
- **Zweite Lesung:** Beratung auf Grundlage der Ausschussempfehlung, Einzelabstimmung über Änderungsanträge.
- **Dritte Lesung:** Schlussabstimmung; nur noch Änderungsanträge zu in zweiter Lesung beschlossenen Änderungen.

#### 1c. Bundesrat (Art. 77, 78 GG)

Erste Frage: **Zustimmungs- oder Einspruchsgesetz?**

- **Zustimmungsgesetz** — wenn das GG dies ausdrücklich anordnet (z. B. Art. 84 Abs. 1 GG bei Eingriff in Landesverwaltung, Art. 105 Abs. 3 GG bei Steuern, deren Aufkommen den Ländern zufließt). Ohne Zustimmung des Bundesrats kommt das Gesetz **nicht zustande**.
- **Einspruchsgesetz** — Regelfall. Bundesrat kann nur Einspruch erheben; der Bundestag kann diesen mit absoluter (bzw. Zweidrittel-)Mehrheit zurückweisen (Art. 77 Abs. 4 GG).

**Vermittlungsausschuss** (Art. 77 Abs. 2 GG): Beide Häuser können ihn anrufen; Voraussetzung für Bundesrats-Einspruch in der Regel.

#### 1d. Ausfertigung (Art. 82 Abs. 1 S. 1 GG)

- Ausfertigung durch den **Bundespräsidenten**.
- Prüfungsrecht streitig: hM beschränkt auf formelles und evident materielles Verfassungsrecht; der Bundespräsident hat materielle Prüfungskompetenz nur bei offensichtlichen, schwerwiegenden Verstößen.
- **Gegenzeichnung** (Art. 58 GG): erforderlich.

#### 1e. Verkündung (Art. 82 Abs. 1 S. 1 GG)

- Verkündung im **Bundesgesetzblatt** (BGBl. Teil I bei materiellen Gesetzen).
- **Inkrafttreten** (Art. 82 Abs. 2 GG): der vom Gesetz selbst bestimmte Zeitpunkt; sonst der vierzehnte Tag nach Ablauf des Tages der Verkündung.

### Schritt 2 — Bestimmtheitsgebot

Aus dem **Rechtsstaatsprinzip** (Art. 20 Abs. 3 GG) folgt:

- **Normklarheit** — der Bürger muss die Rechtslage erkennen können.
- **Vorhersehbarkeit** — Eingriffsvoraussetzungen müssen vorhersehbar sein.
- **Justiziabilität** — die Anwendung muss gerichtlich überprüfbar sein.

**Stufenverhältnis:** Je intensiver der Grundrechtseingriff, desto höher die Bestimmtheitsanforderungen. Bei strafrechtlichen Normen verschärft durch Art. 103 Abs. 2 GG (`nullum crimen sine lege`).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 3 — Zitiergebot (Art. 19 Abs. 1 S. 2 GG)

- **Geltung:** bei Grundrechtseinschränkungen durch oder aufgrund eines Gesetzes.
- **Pflicht:** das einschränkende Gesetz muss das eingeschränkte Grundrecht unter Angabe des Artikels nennen.
- **Folge bei Verstoß:** Nichtigkeit der Norm.
- **Reichweite (Auslegung BVerfG):** Zitiergebot gilt **nur** für nachkonstitutionelle, gezielt grundrechtseinschränkende Gesetze. Vorkonstitutionelle Gesetze und solche, die Grundrechte nur ausgestalten (z. B. Eigentumsausgestaltung Art. 14 Abs. 1 S. 2 GG), unterliegen ihm nicht.

**Praktische Anwendung:** Im Eingangsabschnitt des Gesetzes (vor § 1) findet sich häufig die Formulierung "Das Grundrecht auf … (Art. … GG) wird durch dieses Gesetz eingeschränkt."

### Schritt 4 — Wesentlichkeitstheorie und Parlamentsvorbehalt

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kerngedanke:** Wesentliche Entscheidungen muss der Gesetzgeber selbst treffen; sie dürfen nicht der Exekutive (Verordnungsgeber, Verwaltung) überlassen werden.

**Wesentlich** im verfassungsrechtlichen Sinn ist eine Entscheidung insbesondere:

- Grundrechtsrelevanz (je grundrechtsintensiver, desto wesentlicher)
- Politische Bedeutung
- Eingriffsintensität gegenüber Bürger und Gemeinwesen

**Konsequenz:** Der Gesetzgeber muss die wesentlichen Voraussetzungen, Maßstäbe und Verfahrensregeln **selbst** im förmlichen Gesetz festlegen — keine Generalklauseln, keine pauschale Delegation an die Exekutive.

**Verhältnis zu Art. 80 Abs. 1 S. 2 GG** (Inhalt, Zweck und Ausmaß der Verordnungsermächtigung): das Zitiergebot des Art. 80 ist ein Sonderfall der Wesentlichkeitstheorie für Rechtsverordnungen.

### Schritt 5 — Allgemeinheit des Gesetzes (Art. 19 Abs. 1 S. 1 GG)

- **Einzelfallgesetz-Verbot:** Ein Grundrecht einschränkendes Gesetz muss "allgemein und nicht nur für den Einzelfall" gelten.
- **Folge bei Verstoß:** Verfassungswidrigkeit.

### Schritt 6 — Wesensgehaltsgarantie (Art. 19 Abs. 2 GG)

- In keinem Fall darf ein Grundrecht in seinem **Wesensgehalt** angetastet werden.
- Diese "Schranken-Schranke" bildet die absolute Untergrenze jeder Grundrechtseinschränkung.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 76-78 GG (Gesetzgebungsverfahren) — Art. 79 GG (Verfassungsaenderung) — Art. 19 Abs. 1 Satz 2 GG (Zitiergebot) — Art. 80 GG (Verordnungsermaechtigung, formelle Anforderungen) — Art. 82 GG (Ausfertigung und Verkuendung)

## Output-Format

```
FORMELLE VERFASSUNGSMÄSSIGKEIT

Prüfungsgegenstand: <Gesetz / Norm>

1. Verfahren
 - Initiativrecht (Art. 76 GG): ___
 - Erste Lesung: ___
 - Ausschussüberweisung: ___
 - Zweite Lesung: ___
 - Dritte Lesung / Schlussabstimmung: ___
 - Bundesrat (Art. 77, 78 GG): [Zustimmung / Einspruch] — Ergebnis: ___
 - Vermittlungsausschuss: ___
 - Ausfertigung (Art. 82 GG): ___
 - Verkündung BGBl.: ___

2. Form
 - Bestimmtheitsgebot: ___
 - Zitiergebot (Art. 19 Abs. 1 S. 2 GG): ___
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - Einzelfallverbot (Art. 19 Abs. 1 S. 1 GG): ___
 - Wesensgehalt (Art. 19 Abs. 2 GG): ___

BVerfG-Pinpoints
- ___

Ergebnis: [formell verfassungsgemäß / formell verfassungswidrig — Grund: ___]
```

## Disclaimer-Wiederholung

Auch eine sorgfältige Prüfung der formellen Verfassungsmäßigkeit ersetzt nicht die anwaltliche Mandatsbearbeitung. Die verbindliche Verwerfung obliegt allein dem BVerfG.

---

## Skill: `gesetzentwurf-gg-konformitaet-pruefen`

_Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip Verhältnismäßigkeit EU-Recht-Konformität. Output: Verfassun..._

# Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht)

## Arbeitsbereich

Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip Verhältnismäßigkeit EU-Recht-Konformität. Output: Verfassungsprüfmemo Risikobewertung. Abgrenzung: nicht für laufende Normenkontrolle (normenkontrolle ist separates Plugin). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht)
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer

Diese Prüfung dient der Gesetzgebungsvorbereitung in Ministerien und Regierungsstellen. Die verbindliche Klärung der Verfassungsmäßigkeit eines Gesetzes erfolgt im Streitfall ausschließlich durch das BVerfG (Art. 100 GG; Art. 93 Abs. 1 Nr. 2, 2a GG). Diese Prüfung ist eine Unterstützung und **kein Ersatz** für externe gutachterliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst. Jede Aussage benötigt BVerfG-Pinpoint.

## Workflow

### Schritt 1 — Regelungsziel und Mittel bestimmen

- **Regelungsziel:** welcher Zustand soll erreicht / welche Gefahr abgewehrt werden?
- **Regelungsmittel:** welche Normen sollen erlassen werden?
- **Adressatenkreis:** wer wird betroffen?
- **Bestehende Regelungslage:** was gibt es bereits?

### Schritt 2 — Gesetzgebungskompetenz (Aufruf Skill `gesetzgebungskompetenz-pruefen`)

- Materiebestimmung (Schwerpunkt)
- Art. 70–74 GG durchgehen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bei Abweichungsgesetzgebung Art. 72 Abs. 3 GG: Verhältnis Bund/Land klären.

### Schritt 3 — Formelle Verfassungsmäßigkeit (Aufruf Skill `formelle-verfassungsmaessigkeit`)

- Verfahren Art. 76–82 GG planen.
- **Zustimmungs- oder Einspruchsgesetz?** Prüfung früh, da Mehrheitsverhältnisse im Bundesrat berücksichtigt werden müssen.
- **Bestimmtheit:** Tatbestandsmerkmale, Rechtsfolgen, Zuständigkeiten klar regeln. Generalklauseln vermeiden, soweit Grundrechtsrelevanz hoch.
- **Zitiergebot Art. 19 Abs. 1 S. 2 GG:** Falls ein Grundrecht eingeschränkt wird, im Eingangsabschnitt das eingeschränkte Grundrecht unter Angabe des Artikels nennen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 4 — Materielle Verfassungsmäßigkeit pro betroffenes Grundrecht

Für jedes betroffene Grundrecht (Aufruf Skill `grundrechtspruefung`):

- Schutzbereich identifizieren.
- Eingriff bestimmen — auch mittelbare und faktische Eingriffe einbeziehen.
- Schranke benennen.
- **Schranken-Schranken** prüfen:
 - **Verhältnismäßigkeit** (Aufruf Skill `verhaeltnismaessigkeit`) — vier Stufen.
 - Wesensgehalt Art. 19 Abs. 2 GG.
 - Zitiergebot.
 - Allgemeinheit Art. 19 Abs. 1 S. 1 GG.
 - Wechselwirkungslehre bei Art. 5 Abs. 2 GG.
- Spezielle Strukturen einzelner Grundrechte berücksichtigen (Drei-Stufen-Theorie bei Art. 12 GG, Eingriffsformen bei Art. 14 GG, usw.).

### Schritt 5 — Sonstige verfassungsrechtliche Bindungen

#### 5a. Rechtsstaatsprinzip (Art. 20 Abs. 3 GG)

- **Bestimmtheitsgebot** (s. Schritt 3).
- **Vertrauensschutz und Rückwirkungsverbot:**
 - **Echte Rückwirkung** (Rückbewirkung von Rechtsfolgen) — grundsätzlich unzulässig.
 - **Unechte Rückwirkung** (tatbestandliche Rückanknüpfung) — zulässig, soweit Vertrauensschutz nicht überwiegt.
- **Faires Verfahren.**

#### 5b. Demokratieprinzip (Art. 20 Abs. 1, 2 GG)

- Lückenlose demokratische Legitimationskette für hoheitliches Handeln.
- Parlamentsvorbehalt (s. Wesentlichkeit).

#### 5c. Sozialstaatsprinzip (Art. 20 Abs. 1 GG)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gleichmäßige Lastenverteilung.

#### 5d. Bundesstaatsprinzip (Art. 20 Abs. 1 GG)

- Beachtung der Länderkompetenzen.
- Bundestreue / Verfassungstreue.

#### 5e. Europarechtsfreundlichkeit

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mit Unionsrecht vereinbar? Verstoß gegen Grundrechtecharta?

### Schritt 6 — Begründung des Entwurfs

Die Gesetzesbegründung sollte folgende Punkte zur Verfassungsmäßigkeit explizit ausführen:

1. **Gesetzgebungskompetenz** — einschlägige Norm benennen; bei Art. 72 Abs. 2 GG: Erforderlichkeit substantiiert dartun.
2. **Eingeschränkte Grundrechte** — explizit benennen, Zitiergebot wahren.
3. **Verhältnismäßigkeit** — Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit pro Grundrecht durchargumentieren.
4. **Bezugnahme auf einschlägige BVerfG-Rechtsprechung** — Pinpoint mit Az. + Rn. + URL.
5. **Alternativen** — geprüfte mildere Mittel und Gründe für ihre Ablehnung.
6. **Folgenabschätzung** — auch zur Wahrung der Verhältnismäßigkeit.

### Schritt 7 — Risikoeinschätzung

- **Klassifikation:**
 - **Niedrig** — keine erkennbaren verfassungsrechtlichen Bedenken.
 - **Mittel** — auslegungsbedürftige Streitfragen; Stellungnahme aus Wissenschaft, Rechtsausschuss erwartbar.
 - **Hoch** — substantielle Bedenken; abstrakte Normenkontrolle oder Verfassungsbeschwerde wahrscheinlich.

- **Empfehlung bei mittlerem/hohem Risiko:** externe verfassungsrechtliche Begutachtung; Anpassungen am Entwurf, um Risiko zu reduzieren.

## Output-Format

```
GG-KONFORMITÄT GESETZENTWURF

Entwurf: ___
Regelungsziel: ___

1. Gesetzgebungskompetenz
 - Einschlägige Norm: Art. ___ GG
 - Bei Art. 72 Abs. 2 GG: Erforderlichkeit ___
 - BVerfG-Pinpoint: ___

2. Formelle Verfassungsmäßigkeit
 - Verfahren: ___
 - Zustimmungs-/Einspruchsgesetz: ___
 - Bestimmtheit: ___
 - Zitiergebot: ___
 - Wesentlichkeit (Kalkar): ___

3. Materielle Verfassungsmäßigkeit
 Pro betroffenes Grundrecht:
 - Art. ___ GG
 - Schutzbereich: ___
 - Eingriff: ___
 - Rechtfertigung: ___
 - Verhältnismäßigkeit: [4 Stufen]
 - BVerfG-Pinpoint: ___

4. Sonstige verfassungsrechtliche Bindungen
 - Rechtsstaat, Rückwirkung: ___
 - Demokratie / Parlamentsvorbehalt: ___
 - Sozialstaat: ___
 - Bundesstaat: ___
 - Unionsrecht: ___

5. Empfehlung Gesetzesbegründung
 - ___

6. Risikoeinschätzung
 - [niedrig / mittel / hoch]
 - Empfehlung: ___

BVerfG-Pinpoints
- ___
```

## Disclaimer-Wiederholung

Diese Prüfung ersetzt nicht die externe verfassungsrechtliche Begutachtung. Insbesondere die abschließende Beurteilung der Verfassungsmäßigkeit obliegt im Streitfall allein dem BVerfG.

---

## Skill: `gesetzgebungskompetenz-pruefen`

_Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung Subsidiaritaet Sperrwirkung. Output: Kompetenzprüfmemo Ergebnis mit Fundstellen. Abg..._

# Gesetzgebungskompetenz prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Gesetzgebungskompetenz prüfen
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer

Die Bestimmung der Gesetzgebungskompetenz ist hochkomplex und im Streitfall vom BVerfG zu entscheiden (Art. 93 Abs. 1 Nr. 2, 2a GG abstrakte Normenkontrolle; Art. 100 Abs. 1 GG konkrete Normenkontrolle). Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Jede Aussage benötigt BVerfG-Pinpoint.

## Prüfungsschritte

### Schritt 1 — Materie bestimmen

Was regelt das Gesetz inhaltlich? Schwerpunkt (Subject-Matter-Test):

- Hauptregelungsgehalt identifizieren
- Bei Überschneidungen: Schwerpunkt der Regelung entscheidet, nicht die formale Benennung (st. Rspr.)

### Schritt 2 — Bund oder Land?

**Grundregel Art. 70 Abs. 1 GG:** Länder haben das Recht der Gesetzgebung, soweit das GG nicht dem Bund Gesetzgebungsbefugnisse verleiht.

### Schritt 3 — Ausschließliche Gesetzgebung des Bundes (Art. 71, 73 GG)

Bei Materie in Katalog Art. 73 GG: nur Bund. Länder nur, wenn ausdrücklich Bundesgesetz sie ermächtigt (Art. 71 GG).

**Kerngebiete Art. 73 GG:**

- Auswärtige Angelegenheiten, Verteidigung (Nr. 1)
- Staatsangehörigkeit (Nr. 2)
- Freizügigkeit, Passwesen, Ein- und Auswanderung (Nr. 3)
- Währungs-, Geld- und Münzwesen, Maße und Gewichte, Zeitbestimmung (Nr. 4)
- Zölle und Handelseinheit (Nr. 5)
- Luftverkehr (Nr. 6) — Eisenbahnen des Bundes (Nr. 6a)
- Post- und Telekommunikation (Nr. 7)
- Bundesbeamte (Nr. 8)
- Gewerblicher Rechtsschutz, Urheberrecht, Verlagsrecht (Nr. 9)
- Zusammenarbeit Bund–Länder Kriminalpolizei, Verfassungsschutz, Schutz vor internationalem Terrorismus (Nr. 9a, 10)
- Statistik für Bundeszwecke (Nr. 11)
- Waffenrecht, Sprengstoffrecht (Nr. 12)
- Versorgung Kriegsbeschädigter (Nr. 13)
- Kernenergiefriedliche Nutzung (Nr. 14)
- Staatshaftung (Nr. 15)
- Reproduktionsmedizin und Gentechnik (Nr. 15a)

### Schritt 4 — Konkurrierende Gesetzgebung (Art. 72, 74 GG)

Bei Materie in Katalog Art. 74 GG: Länder dürfen, soweit Bund nicht.

**Drei Untergruppen** nach Art. 72 Abs. 2 GG und Art. 72 Abs. 3 GG:

#### 4a. Kernbereich — Bund kann ohne weitere Voraussetzungen (Art. 72 Abs. 1 GG)

Alle Nummern Art. 74 Abs. 1 GG, die nicht in 4b oder 4c stehen.

#### 4b. Erforderlichkeitsklausel Art. 72 Abs. 2 GG

Bund darf nur, wenn und soweit die Herstellung gleichwertiger Lebensverhältnisse im Bundesgebiet oder die Wahrung der Rechts- oder Wirtschaftseinheit im gesamtstaatlichen Interesse eine bundesgesetzliche Regelung erforderlich macht.

**Betroffene Nummern Art. 74 Abs. 1 GG:** 4, 7, 11, 13, 15, 19a, 20, 22, 25, 26.

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 4c. Abweichungsgesetzgebung Art. 72 Abs. 3 GG

Länder können vom Bundesrecht abweichende Regelungen treffen bei:

- Nr. 1 Jagdwesen (ohne Recht der Jagdscheine)
- Nr. 2 Naturschutz und Landschaftspflege (ohne allgemeine Grundsätze, Recht des Artenschutzes oder Meeresnaturschutz)
- Nr. 3 Bodenverteilung
- Nr. 4 Raumordnung
- Nr. 5 Wasserhaushalt (ohne stoff- oder anlagenbezogene Regelungen)
- Nr. 6 Hochschulzulassung und Hochschulabschlüsse
- Nr. 7 (eingefügt) Grundsteuer

Lex posterior gilt zwischen Bund und Land bei Abweichungsgesetzen (Art. 72 Abs. 3 S. 3 GG).

### Schritt 5 — Annexkompetenz und Sachzusammenhang

**Ungeschriebene Bundeskompetenzen** (Auslegung):

- **Kraft Sachzusammenhang** (Sachkompetenz): Bund darf eine Materie regeln, wenn sie mit einer ausdrücklich zugewiesenen Materie so verzahnt ist, dass die ausdrückliche Kompetenz ohne sie nicht sinnvoll auszuüben wäre.
- **Kraft Natur der Sache:** Materien, die der Sache nach nur einheitlich auf Bundesebene zu regeln sind.
- **Annex (Annexkompetenz):** Bund darf Verfahrens- und Vollzugsregelungen erlassen, wenn er die Hauptmaterie regelt.

Achtung: Restriktive Anwendung. Pinpoint-Recherche zwingend.

### Schritt 6 — Verwaltungskompetenz prüfen (Art. 83 ff. GG)

Gesetzgebungskompetenz nicht verwechseln mit Verwaltungskompetenz:

- Art. 83 GG: Grundsatz Landeseigenverwaltung
- Art. 85 GG: Bundesauftragsverwaltung
- Art. 86 GG: Bundeseigenverwaltung

### Schritt 7 — Ergebnis und Konsequenzen

- **Kompetenzgemäß:** weiter zur formellen und materiellen Verfassungsmäßigkeit.
- **Kompetenzwidrig:** Gesetz ist insgesamt nichtig (Verwerfungsmonopol BVerfG, Art. 100 Abs. 1 GG).
- **Teilkompetenzwidrigkeit:** nur die kompetenzfremden Regelungen sind nichtig, sofern abtrennbar.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 70-74 GG (Kompetenzverteilung) — Art. 72 Abs. 2 GG (Erforderlichkeitsklausel) — Art. 72 Abs. 3 GG (Abweichungskompetenz) — Art. 31 GG (Bundesrecht bricht Landesrecht) — Art. 93 Abs. 1 Nr. 2 GG (abstrakte Normenkontrolle)

## Output-Format

```
GESETZGEBUNGSKOMPETENZ-PRÜFUNG

Prüfungsgegenstand: <Gesetz / Norm>

1. Materiebestimmung (Schwerpunkt): ___
2. Einschlägige Norm:
 - [ ] Art. 73 GG Nr. ___ (ausschließlich Bund)
 - [ ] Art. 74 GG Nr. ___ (konkurrierend)
 - [ ] Kernbereich Art. 72 Abs. 1 GG
 - [ ] Erforderlichkeitsklausel Art. 72 Abs. 2 GG — Prüfung: ___
 - [ ] Abweichungsgesetzgebung Art. 72 Abs. 3 GG
 - [ ] Ungeschriebene Kompetenz: ___
 - [ ] Art. 70 GG (Landeskompetenz)
3. BVerfG-Pinpoint zur Materie: ___
4. Ergebnis: [kompetenzgemäß / kompetenzwidrig / teilkompetenzwidrig]
```

## Disclaimer-Wiederholung

Diese Kompetenzprüfung ist eine strukturierte Modellauswertung; die verbindliche Verwerfung obliegt allein dem BVerfG (Art. 100 Abs. 1 GG).

---

## Skill: `grundrechtspruefung-acht-formelle-interessen`

_Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff Rechtfertigung verfassungsrechtliche Schranken Wesensgehalt Art. 19 Abs. 2 GG Verhältnismäßi..._

# Grundrechtsprüfung

## Arbeitsbereich

Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff Rechtfertigung verfassungsrechtliche Schranken Wesensgehalt Art. 19 Abs. 2 GG Verhältnismäßigkeit. Output: Grundrechtsprüfschema Prüfergebnis. Abgrenzung: nicht für formelle Verfassungsmäßigkeit (formelle-verfassungsmäßigkeit). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Grundrechtsprüfung
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer

Grundrechtsprüfungen sind hochkomplex und in der konkreten Anwendung nur durch das BVerfG verbindlich klärbar. Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Pinpoint Az. + Rn. + URL pro tragender Aussage.

## Grundschema: Schutzbereich – Eingriff – Rechtfertigung

### Schritt 1 — Schutzbereichseröffnung

#### 1a. Persönlicher Schutzbereich

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Jedermanngrundrechte:** Art. 1, 2, 3, 4, 5, 10, 13, 14, 17 GG — alle natürlichen Personen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 1b. Sachlicher Schutzbereich

Was schützt das Grundrecht? Wortlaut, Systematik, Telos. Bei der Bestimmung **nicht restriktiv** vorgehen (in dubio pro libertate).

**Standard-Schutzbereiche** (mit Pinpoint live nachrecherchieren):

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Art. 4 Abs. 1, 2 GG:** Glaubens-, Gewissens- und Bekenntnisfreiheit — vorbehaltlos.
- **Art. 5 Abs. 1 GG:** Meinungs-, Informations-, Presse-, Rundfunk- und Filmfreiheit.
- **Art. 5 Abs. 3 GG:** Kunst- und Wissenschaftsfreiheit — vorbehaltlos.
- **Art. 8 GG:** Versammlungsfreiheit (Deutsche).
- **Art. 9 GG:** Vereinigungsfreiheit (Deutsche), Art. 9 Abs. 3 GG Koalitionsfreiheit (jedermann).
- **Art. 10 GG:** Brief-, Post- und Fernmeldegeheimnis.
- **Art. 12 GG:** Berufsfreiheit (Deutsche).
- **Art. 13 GG:** Unverletzlichkeit der Wohnung.
- **Art. 14 GG:** Eigentum und Erbrecht — Eigentumsbegriff weit (alle vermögenswerten Rechtspositionen, kraft Gesetz oder Gewohnheit anerkannt).

### Schritt 2 — Eingriff

#### 2a. Klassischer Eingriffsbegriff

Final, unmittelbar, rechtsförmig, mit Befehl und Zwang.

#### 2b. Moderner Eingriffsbegriff

Jede dem Staat zurechenbare Beeinträchtigung des grundrechtlich geschützten Verhaltens. Erfasst auch:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Faktische Eingriffe** (Maßnahmen ohne Zwang, die das geschützte Verhalten erschweren).
- **Schutzpflicht-Verletzungen** (untermaß-Verbot bei Schutz vor Dritten).

#### 2c. Eingriffsqualifikation

- Welcher Grundrechtsträger ist betroffen?
- Wie schwer ist der Eingriff (für Verhältnismäßigkeit relevant)?
- Bei mehreren Grundrechten: spezielleres Grundrecht vorrangig, Art. 2 Abs. 1 GG subsidiär.

### Schritt 3 — Verfassungsrechtliche Rechtfertigung

#### 3a. Schranke

**Klassifikation:**

- **Einfacher Gesetzesvorbehalt** — z. B. Art. 2 Abs. 2 S. 3 GG, Art. 11 Abs. 2 GG (für bestimmte Fälle), Art. 12 Abs. 1 S. 2 GG.
- **Qualifizierter Gesetzesvorbehalt** — Schranke nur unter bestimmten zusätzlichen Voraussetzungen. Z. B. Art. 5 Abs. 2 GG ("allgemeine Gesetze", Schutz der Jugend, Recht der persönlichen Ehre); Art. 8 Abs. 2 GG (Versammlungen unter freiem Himmel); Art. 13 GG (Eingriffsstaffel).
- **Vorbehaltlos gewährtes Grundrecht** — z. B. Art. 4, Art. 5 Abs. 3 GG, Glaubensfreiheit, Kunst- und Wissenschaftsfreiheit. Eingriff nur durch **verfassungsimmanente Schranken** rechtfertigbar (kollidierendes Verfassungsrecht, insbesondere Grundrechte Dritter und Verfassungsgüter mit Verfassungsrang).

#### 3b. Schranken-Schranken

Die Schranke darf ihrerseits nicht gegen Verfassungsrecht verstoßen:

1. **Verhältnismäßigkeit** (Skill `verhaeltnismaessigkeit`): legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit.
2. **Wesensgehaltsgarantie** (Art. 19 Abs. 2 GG): absoluter Kernbereich darf nicht verletzt werden.
3. **Zitiergebot** (Art. 19 Abs. 1 S. 2 GG, nur bei einschränkenden Gesetzen mit Wirkungsabsicht auf das Grundrecht).
4. **Allgemeinheit** (Art. 19 Abs. 1 S. 1 GG).
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
6. **Spezifische Vorgaben des qualifizierten Vorbehalts** (z. B. Allgemeinheit des Gesetzes bei Art. 5 Abs. 2 GG).
7. **Bestimmtheitsgebot, Wesentlichkeit** (siehe Skill `formelle-verfassungsmaessigkeit`).

### Schritt 4 — Spezielle Strukturen einzelner Grundrechte

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Stufe | Charakter | Rechtfertigungsanforderung |
| --- | --- | --- |
| 1 — Berufsausübungsregelung | Wie / Art und Weise der Berufstätigkeit | Jeder vernünftige Gemeinwohlgrund genügt |
| 2 — Subjektive Berufszulassungsschranke | Anknüpfung an persönliche Eigenschaften (Qualifikation, Prüfung) | Schutz wichtiger Gemeinschaftsgüter |
| 3 — Objektive Berufszulassungsschranke | Vom Bewerber unabhängige Voraussetzungen (Bedürfnisprüfung) | Schutz **überragend wichtiger** Gemeinschaftsgüter vor **nachweisbaren oder höchstwahrscheinlichen schweren** Gefahren |

Eingriff stets auf der **geringstmöglichen Stufe**.

#### 4b. Art. 14 GG — Eigentum

- Drei Eingriffsformen: **Inhalts- und Schrankenbestimmung** (Art. 14 Abs. 1 S. 2 GG), **Enteignung** (Art. 14 Abs. 3 GG), **ausgleichspflichtige Inhalts- und Schrankenbestimmung**.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 4c. Art. 8 GG — Versammlung

- Versammlungsbegriff: gemeinsame Erörterung oder Kundgabe auf Teilnahme an öffentlicher Meinungsbildung gerichtet.
- Versammlungen **unter freiem Himmel:** qualifizierter Gesetzesvorbehalt Art. 8 Abs. 2 GG.
- **In geschlossenen Räumen:** vorbehaltlos.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 4d. Art. 5 Abs. 1 GG — Meinungsfreiheit

- Tatsachenbehauptungen sind geschützt, **soweit** sie Voraussetzung der Meinungsbildung sind; **unwahre und bewusst unwahre** Tatsachenbehauptungen sind nicht geschützt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Wechselwirkungslehre Lüth.

### Schritt 5 — Konkurrenzen

- Spezielleres vor allgemeinem Grundrecht (Art. 2 Abs. 1 GG subsidiär).
- Kombinations-Grundrecht aus Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1 GG (APR).
- Bei Idealkonkurrenz: parallele Prüfung beider Grundrechte; Eingriff muss in beiden gerechtfertigt sein.

## Output-Format

```
GRUNDRECHTSPRÜFUNG

Geprüftes Grundrecht: Art. ___ GG

1. Schutzbereich
 - Persönlich: ___
 - Sachlich: ___
 - Eröffnet: [ja / nein]

2. Eingriff
 - Art: [klassisch / mittelbar / faktisch]
 - Maßnahme: ___
 - Vorliegen: [ja / nein]

3. Verfassungsrechtliche Rechtfertigung
 - Schranke: [einfacher / qualifizierter Vorbehalt / vorbehaltlos]
 - Einschränkungsgesetz: ___
 - Schranken-Schranken:
 - Verhältnismäßigkeit: [siehe Skill verhältnismäßigkeit]
 - Wesensgehalt Art. 19 Abs. 2 GG: ___
 - Zitiergebot Art. 19 Abs. 1 S. 2 GG: ___
 - Wechselwirkung (Lüth): ___
 - Bestimmtheit, Wesentlichkeit: ___

BVerfG-Pinpoints
- ___

Ergebnis: [Grundrecht verletzt / nicht verletzt]
```

## Disclaimer-Wiederholung

Diese Prüfung ist eine strukturierte Modellauswertung und **kein Ersatz** für anwaltliche Bearbeitung durch eine verfassungsrechtliche Spezialkanzlei.

---

## Skill: `verfassungsbeschwerde-entwurf-formelle`

_Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster: Beschwerdeführerbefugnis Beschwerdeobjekt Rechtswegerschoepfung Frist Grundrechtsverletzung. Output..._

# Verfassungsbeschwerde-Entwurf

## Arbeitsbereich

Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster: Beschwerdeführerbefugnis Beschwerdeobjekt Rechtswegerschoepfung Frist Grundrechtsverletzung. Output: Verfassungsbeschwerde-Schriftsatz mit Zulässigkeit Begründung. Abgrenzung: nicht für abstrakte oder konkrete Normenkontrolle. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verfassungsbeschwerde-Entwurf
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer (Schlüsselstelle, mehrfach)

Die Verfassungsbeschwerde ist der zentrale Rechtsbehelf zum BVerfG, mit existentiellen Folgen für Mandanten. Sie unterliegt strengen Zulässigkeitsanforderungen, der Monatsfrist nach § 93 Abs. 1 BVerfGG und hohen Substantiierungsanforderungen (§ 23 Abs. 1, § 92 BVerfGG). Dieser Entwurf ist **kein Ersatz** für die Bearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Vor jeder Einreichung ist eine fachanwaltliche Prüfung dringend erforderlich.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Pinpoint pro tragender Aussage.

## Zulässigkeitsprüfung

Die Verfassungsbeschwerde durchläuft eine **strenge Zulässigkeitsprüfung**. Schon ein einziger Mangel führt zur Verwerfung als unzulässig.

### 1. Zuständigkeit des BVerfG (Art. 93 Abs. 1 Nr. 4a GG, § 90 BVerfGG)

Verfassungsbeschwerde gegen Akte der **deutschen öffentlichen Gewalt**.

### 2. Beschwerdefähigkeit

- **Natürliche Personen:** alle Träger von Grundrechten (Art. 19 Abs. 3 GG analog).
- **Juristische Personen des Privatrechts:** soweit das Grundrecht ihrem Wesen nach auf sie anwendbar ist (Art. 19 Abs. 3 GG).
- **Inländische juristische Personen** sowie nach BVerfG-Rspr. auch **juristische Personen aus EU-Mitgliedstaaten** (Pinpoint live nachsehen).
- **Juristische Personen des öffentlichen Rechts:** grundsätzlich **nicht** beschwerdefähig (Confusio); Ausnahmen: Universitäten (Art. 5 Abs. 3 GG), Religionsgemeinschaften (Art. 4 GG), Rundfunkanstalten (Art. 5 Abs. 1 S. 2 GG).

### 3. Beschwerdegegenstand

Akt der **deutschen öffentlichen Gewalt:**

- Gerichtliche Entscheidungen (Urteile, Beschlüsse) — häufigster Fall.
- Verwaltungsakte.
- Gesetze (Rechtssatzverfassungsbeschwerde).
- Realakte.

**Ausschluss:** Akte ausländischer und supranationaler Organe (mit Ausnahme der "Solange-Rechtsprechung" zum Unionsrecht).

### 4. Beschwerdebefugnis

Der Beschwerdeführer muss schlüssig darlegen, durch den angegriffenen Akt **in eigenen Grundrechten oder grundrechtsgleichen Rechten** möglicherweise verletzt zu sein:

- **Selbst** — eigene Grundrechtsbetroffenheit (nicht Popularklage).
- **Gegenwärtig** — schon eingetreten oder mit hinreichender Sicherheit zu erwarten.
- **Unmittelbar** — ohne weiteren Vollzugsakt; bei Gesetzen erfordert dies regelmäßig, dass der Vollzug auf einen Verwaltungsakt erst gewartet werden kann; bei untergesetzlichen Normen Unmittelbarkeit nur, wenn die Norm ohne Umsetzungsakt direkt wirkt.

**Gegenwärtig + unmittelbar bei Gesetzen:** Ausnahmen bei Vorbereitungspflichten oder bei Strafnormen, deren Vollzug nicht abgewartet werden kann (Risiko strafrechtlicher Verfolgung).

### 5. Rechtswegerschöpfung (§ 90 Abs. 2 S. 1 BVerfGG)

- Vor Anrufung des BVerfG muss der **gesamte fachgerichtliche Rechtsweg** ausgeschöpft sein.
- Erfasst alle Instanzen einschließlich Nichtzulassungsbeschwerde, Revision usw.
- Bei Rechtssatzverfassungsbeschwerde gegen ein Gesetz: regelmäßig kein Rechtsweg vorhanden, daher entfällt die Erschöpfung; ggf. **vorrangige Subsidiarität** beachten.

### 6. Subsidiarität (über Rechtswegerschöpfung hinaus)

Beschwerdeführer muss alle ihm zumutbaren Möglichkeiten genutzt haben, eine **Grundrechtsverletzung schon vor den Fachgerichten** zu rügen. Dazu gehört insbesondere, **verfassungsrechtliche Argumente bereits dort vorzutragen** (Rügeobliegenheit).

Bei Gesetzen ohne Rechtsweg: zumutbar muss der Bürger ggf. eine Feststellungsklage erheben, in deren Rahmen die Norm inzident geprüft wird.

### 7. Frist (§ 93 BVerfGG)

- **Einzelakte:** ein Monat ab Zustellung oder Bekanntgabe (§ 93 Abs. 1 BVerfGG).
- **Gesetze und sonstige Rechtsnormen:** ein Jahr nach Inkrafttreten (§ 93 Abs. 3 BVerfGG).
- **Wiedereinsetzung in den vorigen Stand** möglich (§ 93 Abs. 2 BVerfGG, strenge Voraussetzungen).

### 8. Form und Substantiierung (§ 23 Abs. 1, § 92 BVerfGG)

- **Schriftform** mit eigenhändiger Unterschrift (oder elektronisch nach § 23a BVerfGG).
- **Bezeichnung des angegriffenen Hoheitsakts.**
- **Bezeichnung des verletzten Grundrechts/grundrechtsgleichen Rechts.**
- **Vortrag der Tatsachen,** aus denen sich die Verletzung ergibt.
- **Vortrag zum Rechtsweg** und zur Erschöpfung.
- Hohe Anforderungen: Pinpoint-Verweise auf BVerfG-Rspr. erwartet, soweit einschlägig.

### 9. Allgemeines Rechtsschutzbedürfnis

Regelmäßig zu bejahen, wenn die Voraussetzungen 1–8 erfüllt sind. Ausnahmen bei Erledigung (dann ggf. Fortsetzungsfeststellungsinteresse, insbesondere bei Wiederholungsgefahr oder tiefen Eingriffen).

## Annahme zur Entscheidung (§ 93a BVerfGG)

Die Verfassungsbeschwerde wird nur **angenommen**, wenn:

- ihr **grundsätzliche verfassungsrechtliche Bedeutung** zukommt (§ 93a Abs. 2 lit. a BVerfGG), **oder**
- sie zur Durchsetzung der vom BVerfG in seiner Rechtsprechung anerkannten Grundrechte angezeigt ist; das ist insbesondere der Fall, wenn dem Beschwerdeführer durch die Versagung der Entscheidung **ein besonders schwerer Nachteil** entsteht (§ 93a Abs. 2 lit. b BVerfGG).

## Aufbau einer Verfassungsbeschwerde

```
An das Bundesverfassungsgericht
Schlossbezirk 3
76131 Karlsruhe

In dem Verfassungsbeschwerdeverfahren
des Herrn/der Frau [Name]
[Anschrift]
- Beschwerdeführer/in -

Verfahrensbevollmächtigte:
Rechtsanwältin/Rechtsanwalt [Name]
[Kanzleianschrift]

gegen
[Bezeichnung der angegriffenen Maßnahme — z. B. Urteil des BGH vom ... — Az. ... ; Beschluss des OLG ... ; § ... XYZ-Gesetz]

wegen Verletzung von Art. ___ GG

erhebe ich namens und in Vollmacht des Beschwerdeführers/der Beschwerdeführerin

VERFASSUNGSBESCHWERDE

und beantrage,
1. festzustellen, dass [angegriffener Akt] den Beschwerdeführer / die Beschwerdeführerin in seinen / ihren Grundrechten aus Art. ___ GG verletzt;
2. den angegriffenen Akt aufzuheben und die Sache zur erneuten Entscheidung zurückzuverweisen [bei Gerichtsentscheidungen];
 bzw. die angegriffene Norm für nichtig zu erklären [bei Rechtssatzverfassungsbeschwerde];
3. die Kosten des Verfahrens und die notwendigen Auslagen des Beschwerdeführers / der Beschwerdeführerin der Staatskasse aufzuerlegen.

A. Sachverhalt
[Sachverhalt mit Aktenbezug. Pinpoint zu jeder tatsächlichen Aussage aus den Akten.]

B. Zulässigkeit
I. Zuständigkeit
II. Beschwerdefähigkeit
III. Beschwerdegegenstand
IV. Beschwerdebefugnis
 1. Selbst
 2. Gegenwärtig
 3. Unmittelbar
V. Rechtswegerschöpfung (§ 90 Abs. 2 BVerfGG)
VI. Subsidiarität
VII. Frist (§ 93 BVerfGG)
VIII. Substantiierung (§ 23 Abs. 1, § 92 BVerfGG)
IX. Rechtsschutzbedürfnis

C. Begründetheit
Die Verfassungsbeschwerde ist begründet. [Angegriffener Akt] verletzt den Beschwerdeführer in seinem Grundrecht aus Art. ___ GG.

I. Schutzbereich
[Aufruf Skill grundrechtsprüfung]

II. Eingriff

III. Verfassungsrechtliche Rechtfertigung
 1. Schranke
 2. Verhältnismäßigkeit
 [Aufruf Skill verhältnismäßigkeit]
 3. Sonstige Schranken-Schranken

IV. Spezifische verfassungsrechtliche Verstöße
[BVerfG-Pinpoints konkret]

D. Annahmegründe (§ 93a Abs. 2 BVerfGG)
[Begründung grundsätzliche verfassungsrechtliche Bedeutung oder schwerer Nachteil]

E. Eilantrag (§ 32 BVerfGG)
[optional, falls einstweilige Anordnung erforderlich]

Anlagen
1. Vollmacht
2. Kopie des angegriffenen Akts
3. Kopien aller fachgerichtlichen Entscheidungen
4. ...

[Ort, Datum]
[Unterschrift Rechtsanwalt/Rechtsanwältin]
```

## Aktuelle Rechtsprechung & Leitsätze

Stand 05/2026. Vor Verwendung im Schriftsatz Pinpoint (Rn., Tenor) auf [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) verifizieren.

- BVerfG, Beschl. v. 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Eingriffsschwellen bei polizeirechtlicher Datenerhebung; Übergangsfortgeltung bis 31.12.2025; methodisch Pinpoint für Verhältnismäßigkeit/Wesentlichkeit.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 2466/19 (Trojaner I) — präventiv-polizeirechtliche Quellen-TKÜ / Online-Durchsuchung, PolG NRW im Wesentlichen verfassungskonform.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 180/23 (Trojaner II) — strafprozessuale Quellen-TKÜ teilweise nichtig (Niedrig-Strafrahmen).
- BVerfG, Beschl. v. 24.03.2021 — 1 BvR 2656/18 u. a. (Klimabeschluss) — intertemporale Freiheitssicherung; Art. 20a GG; subjektive Schutzpflicht.

## Zentrale Normen (Paragrafenkette)

§§ 90-95 BVerfGG (Verfassungsbeschwerde: Zulässigkeit, Frist, Annahme) — § 93a BVerfGG (Annahme zur Entscheidung) — § 32 BVerfGG (Einstweilige Anordnung) — §§ 1-3 BVerfGG (Zuständigkeit BVerfG)

## Praxishinweise

- **Vollmacht beifügen** — nach § 22 BVerfGG.
- **Eilantrag nach § 32 BVerfGG** parallel erwägen, wenn die Hauptsacheentscheidung nicht abgewartet werden kann.
- **Kostenerstattung:** § 34a BVerfGG bei Erfolg.
- **Frist striktest** überwachen — Wiedereinsetzung bei Verschulden in eigenen Reihen kaum möglich.

## Disclaimer-Wiederholung (vor jedem Output)

Eine Verfassungsbeschwerde ist eine der anspruchsvollsten Schriftsätze der deutschen Rechtsordnung. Dieser Entwurf ist **kein Ersatz** für die anwaltliche Mandatsbearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Insbesondere die Substantiierungsanforderungen und die strenge Subsidiarität führen in der Praxis zu hohen Verwerfungsquoten.

---

## Skill: `verfassungsrechtliche-pruefung`

_Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien Verhältnismäßigkeit EU-Recht. Output: umfassendes Verfassungsprüfmemo. Abgrenzung..._

# Verfassungsrechtliche Prüfung — Master-Workflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verfassungsrechtliche Prüfung — Master-Workflow
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer (Schlüsselstelle, mehrfach)

Verfassungsrechtliche Prüfungen sind hochspezialisiert und haben existentielle Folgen für Mandanten und Allgemeinheit. Diese Prüfung ist **kein Ersatz** für anwaltliche Mandatsbearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Bei konkreten Vorhaben (Verfassungsbeschwerde, Stellungnahme, Gutachten) ist eine Spezialkanzlei einzuschalten.

## Quellenpflicht

Vor jeder verfassungsrechtlichen Aussage ist Skill `bverfg-rechtsprechung-recherchieren` aufzurufen. Jede tragende Aussage benötigt einen BVerfG-Pinpoint (Az. + Rn. + URL).

## Prüfungsgegenstand klären

Vor Beginn der Prüfung ist zu klären, was eigentlich geprüft wird:

- **Formelles Gesetz** (Bundes- oder Landesgesetz)
- **Rechtsverordnung** (Prüfung gegen Ermächtigungsnorm und unmittelbar gegen GG)
- **Satzung**
- **Verwaltungsakt** oder sonstige Maßnahme der vollziehenden Gewalt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Gesamtschema

### A. Formelle Verfassungsmäßigkeit

**Skill aufrufen:** `gesetzgebungskompetenz-pruefen` und `formelle-verfassungsmaessigkeit`.

1. **Zuständigkeit (Gesetzgebungskompetenz)**
 - Art. 70 GG (Grundregel: Länder, soweit GG nicht Bund)
 - Art. 71–72 GG (ausschließliche und konkurrierende Gesetzgebung)
 - Art. 73 GG (Katalog Bund ausschließlich)
 - Art. 74 GG (Katalog konkurrierend) ggf. mit Art. 72 Abs. 2 GG (Erforderlichkeitsklausel) oder Art. 72 Abs. 3 GG (Abweichungsgesetzgebung)
 - Art. 75 GG a.F. (Rahmengesetzgebung) — **seit Föderalismusreform 2006 abgeschafft**
 - Bei Verwaltungskompetenzen: Art. 83 ff. GG

2. **Verfahren (Art. 76–82 GG)**
 - Einbringung (Art. 76 GG)
 - Drei Lesungen im Bundestag (§§ 78–86 GOBT)
 - Beteiligung Bundesrat (Art. 77, 78 GG — Zustimmungs- vs. Einspruchsgesetz)
 - Ausfertigung durch Bundespräsidenten (Art. 82 Abs. 1 S. 1 GG)
 - Verkündung im Bundesgesetzblatt (Art. 82 Abs. 1 S. 1 GG)

3. **Form**
 - Bestimmtheitsgebot (rechtsstaatliches Erfordernis)
 - Zitiergebot (Art. 19 Abs. 1 S. 2 GG bei Grundrechtseinschränkungen)
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### B. Materielle Verfassungsmäßigkeit

**Skill aufrufen:** `grundrechtspruefung` und `verhaeltnismaessigkeit`.

Pro betroffenem Grundrecht und pro betroffener Verfassungsnorm separat:

1. **Schutzbereichseröffnung** — persönlich und sachlich
2. **Eingriff** — modern: jede Beeinträchtigung des Schutzbereichs, klassisch: final, unmittelbar, rechtsförmig, mit Befehl/Zwang
3. **Verfassungsrechtliche Rechtfertigung**
 - Schranke (einfacher Gesetzesvorbehalt, qualifizierter Vorbehalt, verfassungsimmanente Schranken bei vorbehaltlosen Grundrechten)
 - Schranken-Schranken (Verhältnismäßigkeit, Wesensgehalt Art. 19 Abs. 2 GG, Zitiergebot Art. 19 Abs. 1 S. 2 GG, allgemeine Geltung Art. 19 Abs. 1 S. 1 GG, Wechselwirkung)
 - **Verhältnismäßigkeit** (Skill `verhaeltnismaessigkeit`): legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit

4. **Sonstige verfassungsrechtliche Bindungen**
 - Bundesstaatsprinzip Art. 20 Abs. 1 GG
 - Demokratieprinzip Art. 20 Abs. 1, 2 GG
 - Rechtsstaatsprinzip Art. 20 Abs. 3 GG (Vertrauensschutz, Rückwirkungsverbot, Bestimmtheit)
 - Sozialstaatsprinzip Art. 20 Abs. 1 GG
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### C. Gesamtergebnis

- Wenn formell **und** materiell verfassungsgemäß: Norm/Maßnahme bestätigt.
- Wenn ein Prüfungspunkt scheitert: Norm/Maßnahme verfassungswidrig.
- Bei verfassungskonformer Auslegung: Auslegung formulieren, die Norm und GG vereinbart (Grenzen: Wortlaut und gesetzgeberischer Wille).

## Output-Format

```
VERFASSUNGSRECHTLICHE PRÜFUNG

Prüfungsgegenstand: <Norm / Maßnahme>

A. Formelle Verfassungsmäßigkeit
1. Gesetzgebungskompetenz
 - Einschlägig: Art. ___ GG
 - Ergebnis: [vereinbar / unvereinbar]
 - BVerfG-Pinpoint: ___
2. Verfahren
 - Einbringung Art. 76 GG: ___
 - Drei Lesungen: ___
 - Bundesrat (Art. 77, 78 GG): ___
 - Ausfertigung Art. 82 GG: ___
3. Form
 - Bestimmtheit: ___
 - Zitiergebot Art. 19 Abs. 1 S. 2 GG: ___
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

B. Materielle Verfassungsmäßigkeit
1. Grundrecht ___
 - Schutzbereich: ___
 - Eingriff: ___
 - Rechtfertigung: Schranke ___ / Schranken-Schranken
 - Verhältnismäßigkeit:
 - Legitimer Zweck: ___
 - Geeignetheit: ___
 - Erforderlichkeit: ___
 - Angemessenheit: ___
 - BVerfG-Pinpoint: ___

C. Gesamtergebnis
[verfassungsgemäß / verfassungswidrig / verfassungskonform auslegbar]

Quellen
- [Liste aller BVerfG-Entscheidungen mit Az., Rn., URL]
```

## Disclaimer-Wiederholung (vor jedem Output)

Diese Prüfung ist eine strukturierte Modellauswertung und **kein Ersatz** für anwaltliche Mandatsbearbeitung. Insbesondere die Beurteilung der Vereinbarkeit konkreter Normen mit dem GG bleibt im Streitfall dem BVerfG vorbehalten (Verwerfungsmonopol Art. 100 GG).

---

## Skill: `verhaeltnismaessigkeit`

_Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit Dreistufenprüfung Abwaegung. Output: Verhältnismäßigkeitsprüfschema Ergebnis Argument..._

# Verhältnismäßigkeit (Vier-Stufen-Prüfung)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verhältnismäßigkeit (Vier-Stufen-Prüfung)
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer

Verhältnismäßigkeitsprüfungen sind regelmäßig der Kern jeder Grundrechtsprüfung und im Streitfall nur durch das BVerfG verbindlich entscheidbar. Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst. Pinpoint pro tragender Aussage.

## Grundsätzliches

- Die Verhältnismäßigkeit ist die **wichtigste Schranken-Schranke**.
- Sie wurzelt im **Rechtsstaatsprinzip** (Art. 20 Abs. 3 GG) und im Wesen der Grundrechte selbst.
- **Stufenverhältnis:** Die vier Prüfungspunkte stehen in einem Stufenverhältnis. Wird ein Punkt verneint, ist die Prüfung beendet — der Eingriff ist unverhältnismäßig.

## Die vier Stufen

### Stufe 1 — Legitimer Zweck

**Frage:** Verfolgt der Eingriff einen verfassungsrechtlich nicht missbilligten Zweck?

- Bei einfachem Gesetzesvorbehalt: jeder Zweck, der das Grundgesetz nicht verbietet.
- Bei qualifiziertem Vorbehalt: nur Zwecke, die der qualifizierte Vorbehalt erlaubt (z. B. "Schutz der Jugend" und "Schutz der persönlichen Ehre" bei Art. 5 Abs. 2 GG).
- Bei vorbehaltlosem Grundrecht: nur **kollidierendes Verfassungsrecht** (verfassungsimmanente Schranken).
- **Wichtig:** Nicht der subjektive, sondern der **objektive** Zweck der Norm zählt.

**Häufige Fehler:** Zweck als bloße Wiederholung des Eingriffs ("Verbot von X zum Zweck, X zu verbieten") — das ist kein legitimer Zweck.

### Stufe 2 — Geeignetheit

**Frage:** Ist das Mittel zur Erreichung des Zwecks geeignet?

- **Maßstab:** Das Mittel muss den Zweck **fördern können** (nicht: vollständig erreichen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Eingeschränkter Maßstab: **Evident ungeeignet** bedeutet verfassungswidrig.

### Stufe 3 — Erforderlichkeit

**Frage:** Gibt es kein milderes, gleich wirksames Mittel?

- **Maßstab:** ein anderes Mittel muss
 - die Grundrechte des Betroffenen **weniger intensiv** einschränken **und**
 - den Zweck **gleich wirksam** erreichen.
- Strikter Maßstab — Einschätzungsspielraum des Gesetzgebers ist hier geringer als bei Geeignetheit.
- Häufiger Knackpunkt: Sind Selbstregulierung, Aufklärungspflichten, Erlaubnisvorbehalt mit Auflagen, mildere Sanktion etc. gleich wirksam wie das gewählte Mittel?

### Stufe 4 — Angemessenheit (Verhältnismäßigkeit im engeren Sinne)

**Frage:** Steht der Eingriff in angemessenem Verhältnis zum verfolgten Zweck?

**Gesamtabwägung** zwischen:

- Schwere des Eingriffs (Tiefe, Breite, Dauer, Reversibilität)
- Gewicht der durch den Eingriff geschützten Belange
- Wahrscheinlichkeit des Schadenseintritts ohne den Eingriff
- Eingriffsintensität auf Grundrechtsseite

**Indikatoren für hohe Eingriffsintensität** (Verschärfung der Anforderungen):

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Heimliche Eingriffe ohne Kenntnis des Betroffenen
- Streubreite (viele Unbeteiligte betroffen)
- Lange Dauer / Dauerwirkung
- Irreversibilität
- Doppelte oder kumulative Belastung

**Indikatoren für hohes Gewicht des Zwecks:**

- Schutz überragend wichtiger Gemeinschaftsgüter (Leben, Gesundheit, äußere und innere Sicherheit)
- Hohe Wahrscheinlichkeit schwerer Schäden bei Untätigkeit

### Praktische Konkordanz (bei vorbehaltlosen Grundrechten)

Bei Eingriff in ein vorbehaltlos gewährtes Grundrecht und kollidierendem Verfassungsrecht:

- **Praktische Konkordanz** als Methode der Abwägung: Beide Rechtsgüter sind so zu balancieren, dass jedes größtmögliche Wirksamkeit entfaltet.
- Kein vorrangiges Verfassungsgut. Es gibt keine Hierarchie zwischen Grundrechten.

## Spezielle Fallgruppen

### Klimaschutz und intertemporale Freiheitssicherung

BVerfG, Beschl. v. 24.03.2021 — 1 BvR 2656/18 u. a. (Klimabeschluss) — Schutzauftrag aus Art. 20a GG; eingriffsähnliche Vorwirkung gegenwärtiger Untätigkeit auf künftige Freiheitsräume; Maßstab der intertemporalen Freiheitssicherung — [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2021/03/rs20210324_1bvr265618.html). EGMR-Linie ergänzend: KlimaSeniorinnen gegen Schweiz, Urt. v. 09.04.2024 — Bf-Nr. 53600/20 (Verletzung Art. 8 EMRK durch unzureichende Klimamaßnahmen) — [hudoc.echr.coe.int](https://hudoc.echr.coe.int).

### Triage

Rechtsprechung zur "Triage" (Pandemie-Priorisierung) live über [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) verifizieren — keine Aktenzeichen aus Modellwissen. Methodisch zentral: Verhältnismäßigkeit von Schutzpflichten aus Art. 3 Abs. 3 S. 2 GG (Verbot der Benachteiligung wegen Behinderung) und Art. 2 Abs. 2 S. 1 GG.

### Online-Durchsuchung / IT-Grundrecht / Quellen-TKÜ

- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 2466/19 (Trojaner I) — präventiv-polizeirechtliche Quellen-TKÜ und Online-Durchsuchung nach PolG NRW im Wesentlichen verfassungskonform — vor Ausgabe live verifizieren.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 180/23 (Trojaner II) — strafprozessuale Quellen-TKÜ für Niedrig-Strafrahmen teilweise nichtig.
- BVerfG, Beschl. v. 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Eingriffsschwelle für längerfristige Observation mit Bildaufnahmen.

## Output-Format

```
VERHÄLTNISMÄSSIGKEITSPRÜFUNG

Eingriff: ___
Betroffenes Grundrecht: Art. ___ GG

1. Legitimer Zweck
 - Verfolgter Zweck: ___
 - Verfassungsrechtlich nicht missbilligt: [ja / nein]
 - BVerfG-Pinpoint: ___

2. Geeignetheit
 - Zweckförderung: ___
 - Einschätzungsspielraum: ___
 - Ergebnis: [geeignet / evident ungeeignet]

3. Erforderlichkeit
 - Mildere Mittel geprüft: ___
 - Gleich wirksam: [ja / nein]
 - Ergebnis: [erforderlich / nicht erforderlich]

4. Angemessenheit
 - Eingriffstiefe: ___
 - Geschützte Belange: ___
 - Abwägung: ___
 - BVerfG-Pinpoint: ___
 - Ergebnis: [angemessen / unangemessen]

Gesamtergebnis: [verhältnismäßig / unverhältnismäßig auf Stufe ___]
```

## Disclaimer-Wiederholung

Die Verhältnismäßigkeitsabwägung ist im konkreten Einzelfall hochsensibel und wird im Streitfall verbindlich nur durch das BVerfG entschieden.

---

## Skill: `start-chronologie-fristen`

_Einstieg, Schnelltriage und Fallrouting im Verfassungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig:..._

# Verfassungsrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verfassungsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `bverfg-rechtsprechung-recherchieren` | BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung… |
| `formelle-verfassungsmaessigkeit` | Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG… |
| `gesetzentwurf-gg-konformitaet-pruefen` | Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG… |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung… |
| `grundrechtspruefung` | Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff… |
| `verfassungsbeschwerde-entwurf` | Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster:… |
| `verfassungsrechtliche-pruefung` | Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien… |
| `verhaeltnismaessigkeit` | Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit… |

## Worum geht es?

Dieses Plugin unterstuetzt Spezialkanzleien, Wissenschaftler und Rechtsanwaelte bei verfassungsrechtlichen Pruefungen nach dem Grundgesetz. Es deckt alle Kernbereiche ab: Gesetzgebungskompetenz (Art. 70-74 GG), formelle Verfassungsmaessigkeit, Grundrechtspruefung im Drei-Schritt, Verhaeltnismaessigkeitspruefung, Gesetzentwurfs-Pruefung auf GG-Konformitaet und Verfassungsbeschwerde-Formulierung nach §§ 90 ff. BVerfGG.

Das Plugin ist rechtsprechungsgetrieben: Es orientiert sich an BVerfG-Leitentscheidungen und empfiehlt bei aktuellen Fragen die Live-Recherche auf bundesverfassungsgericht.de.

## Wann brauchen Sie diese Skill?

- Sie pruefen einen Gesetzentwurf auf Vereinbarkeit mit dem Grundgesetz vor Einleitung des Gesetzgebungsverfahrens.
- Sie formulieren eine Verfassungsbeschwerde nach §§ 90 ff. BVerfGG und benoetigen strukturierte Zulassungs- und Begruendungsanforderungen.
- Sie pruefen die Gesetzgebungskompetenz des Bundes oder eines Landes für ein konkretes Regelungsvorhaben.
- Eine staatliche Massnahme beeintraechtigt Grundrechte und Sie benoetigen eine strukturierte Pruefung (Schutzbereich, Eingriff, Rechtfertigung).
- Sie benoetigen BVerfG-Rechtsprechung zu einer verfassungsrechtlichen Frage für einen Schriftsatz.

## Fachbegriffe (kurz erklaert)

- **Schutzbereich** — Der sachliche und persönliche Bereich, den ein Grundrecht schuetzt; muss eroeffnet sein, bevor ein Eingriff geprueft wird.
- **Eingriff** — Staatliche Massnahme, die in den Schutzbereich eines Grundrechts einwirkt; klassisch: unmittelbar, final, rechtsaktmaessig.
- **Verhaeltnismaessigkeit** — Verfassungsrechtlicher Grundsatz: Massnahme muss legitimen Zweck verfolgen, geeignet, erforderlich und angemessen sein.
- **Gesetzgebungskompetenz** — Grundsaetzlich bei den Ländern (Art. 70 GG); ausschliessliche Bundeskompetenzen Art. 73 GG; konkurrierende Bundeskompetenzen Art. 74 GG.
- **Wesensgehalt** — Unantastbarer Kernbestand jedes Grundrechts; auch im Kriegszustand nicht einschraenkbar (Art. 19 Abs. 2 GG).
- **Verfassungsbeschwerde** — Rechtsbehelfsmoeglichkeit für jede Person gegen Verletzung eines Grundrechts durch öffentliche Gewalt (Art. 93 Abs. 1 Nr. 4a GG).
- **Normenkontrolle** — Abstrakte (Art. 93 Abs. 1 Nr. 2 GG) oder konkrete (Art. 100 GG) Pruefung von Gesetzen auf Verfassungskonformitaet.

## Rechtsgrundlagen

- Art. 1-19 GG — Grundrechte
- Art. 19 Abs. 2 GG — Wesensgehaltgarantie
- Art. 20 Abs. 3 GG — Rechtsstaatsprinzip und Verhaeltnismaessigkeit
- Art. 70-74 GG — Gesetzgebungskompetenzen Bund und Länder
- Art. 76-82 GG — Gesetzgebungsverfahren
- Art. 93 GG — Zuständigkeit BVerfG
- Art. 100 GG — Konkrete Normenkontrolle
- §§ 90 ff. BVerfGG — Verfassungsbeschwerde

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Pruefungsanlass (Gesetzentwurf, staatliche Massnahme, Verfassungsbeschwerde), Verfahrensstadium.
2. Phase des Mandats bestimmen: Kompetenzpruefung, formelle Pruefung, Grundrechtspruefung, Verhaeltnismaessigkeit oder Beschwerde-Entwurf.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Verfassungsbeschwerde-Frist ein Monat ab Zustellung (§ 93 Abs. 1 BVerfGG) bzw. ein Jahr bei Gesetzesbeschwerden.
5. Anschluss-Skill bestimmen: nach Grundrechtspruefung folgt Verhaeltnismaessigkeitspruefung; nach Gesamtpruefung ggf. Verfassungsbeschwerde-Entwurf.

## Skill-Tour (was gibt es hier?)

**Umfassende Pruefung**

- `verfassungsrechtliche-pruefung` — Umfassende Verfassungspruefung einer Massnahme oder Norm; Oberbegriff-Skill mit Verweis auf Spezialisten-Skills.
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf auf GG-Konformitaet pruefen vor Einleitung des Gesetzgebungsverfahrens.

**Kompetenz und formelle Pruefung**

- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz des Bundes oder Landes: ausschliesslich, konkurrierend, Abweichungsgesetzgebung.
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit pruefen: Kompetenz, Verfahren (Art. 76-78 GG) und Ausfertigung (Art. 82 GG).

**Grundrechte und Verhaeltnismaessigkeit**

- `grundrechtspruefung` — Grundrechtspruefung im Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung mit Wesensgehalt-Pruefung.
- `verhaeltnismaessigkeit` — Verhaeltnismaessigkeitspruefung: legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit.

**Verfassungsbeschwerde**

- `verfassungsbeschwerde-entwurf` — Verfassungsbeschwerde nach §§ 90 ff. BVerfGG: Zulaessigkeit (Beschwerdefuehrer, Objekt, Rechtswegerschoepfung, Frist) und Begruendung.

**Rechtsprechungsrecherche**

- `bverfg-rechtsprechung-recherchieren` — BVerfG-Rechtsprechung zu konkreter Frage recherchieren und für Schriftsatz aufbereiten.

## Worauf besonders achten

- **Rechtswegerschoepfung ist Voraussetzung für Verfassungsbeschwerde.** Vor Einlegung der Verfassungsbeschwerde muessen alle ordentlichen und verwaltungsgerichtlichen Rechtsbehelfe ausgeschoepft sein (§ 90 Abs. 2 BVerfGG).
- **Einmonats-Frist laeuft ab Zustellung, nicht ab Kenntnis.** Verfassungsbeschwerde ist nach § 93 Abs. 1 BVerfGG an harte Fristen gebunden; keine Wiedereinsetzung ohne triftigen Grund.
- **Schutzbereich und Eingriff sorgfaeltig trennen.** Haeufiger Fehler ist es, den Eingriff in der Schutzbereichspruefung zu behandeln; die Struktur des Drei-Schritt ist in Schriftsaetzen streng einzuhalten.
- **Konkrete Normenkontrolle nur durch Gerichte.** Buerger und Behörden koennen keine Normenkontrolle nach Art. 100 GG beantragen; nur Gerichte koennen vorlegen.
- **Aktuelle BVerfG-Rechtsprechung immer live recherchieren.** Das Plugin verweist auf bundesverfassungsgericht.de; jedes Gebiet hat potentiell neuere Entscheidungen als der interne Wissensstand.

## Typische Fehler

- Verhaeltnismaessigkeitspruefung wird ohne Herausarbeitung eines legitimen Zwecks begonnen; Pruefung ist dann unvollstaendig.
- Verfassungsbeschwerde wird eingereicht ohne Rechtswegerschoepfung; BVerfG nimmt sie nicht zur Entscheidung an.
- Grundrechtspruefung vermischt Schutzbereich und Eingriff; strukturelles Problem im Schriftsatz.
- Gesetzgebungskompetenz wird nur für den Bund geprueft ohne Sperrwirkung und Abweichungsgesetzgebung zu beachten.
- BVerfG-Judikatur aus den 1990er Jahren wird ohne Ueberpruefung auf Weitergeltung angewendet; Rechtsprechung kann sich geaendert haben.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (GG, BVerfGG)
- Leitentscheidungen: bundesverfassungsgericht.de (Lueth, Volkszaehlung, Apotheken-Urteil, Kalkar, Elfes); aktuelle Recherche empfohlen

### Aktuelle Linien 2024-2026 (Pinpoint-Recherche vor Verwendung pflicht)

- BVerfG, Beschl. v. 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Längerfristige Observation unter Anfertigung von Bildaufnahmen ohne hinreichende Eingriffsschwelle unvereinbar mit Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG; Übergangsfortgeltung bis 31.12.2025 — [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2024/11/ls20241114_1bvl000322.html).
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 2466/19 (Trojaner I, PolG NRW Quellen-TKÜ / Online-Durchsuchung präventiv) — polizeirechtliche Befugnisse im Wesentlichen verfassungskonform — Pinpoint vor Verwendung [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) verifizieren.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 180/23 (Trojaner II, Quellen-TKÜ / Online-Durchsuchung StPO) — strafprozessuale Quellen-TKÜ für Taten mit niedrigem Strafrahmen teilweise nichtig — Pinpoint vor Verwendung [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) verifizieren.
- BVerfG, Klimabeschluss vom 24.03.2021 — 1 BvR 2656/18 u. a. — intertemporale Freiheitssicherung — [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2021/03/rs20210324_1bvr265618.html).
- BVerfG, Jahresbericht 2025 — [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de/SharedDocs/Downloads/DE/Jahresbericht/jahresbericht_2025.pdf).

---

## Skill: `verfassung-grundrechte-uebersicht`

_Grundrechte des GG Ueberblick: Art. 1 Wuerde, Art. 2 freie Entfaltung, Art. 3 Gleichheit, Art. 4 Glaubensfreiheit, Art. 5 Meinungsfreiheit, Art. 8 Versammlung, Art. 12 Berufsfreiheit, Art. 14 Eigentum. Schutzbereich, Eingriff, Schranken, Schranken-Schranken im Verfassungsrecht._

# Grundrechte Ueberblick

## Arbeitsbereich

Grundrechte des GG Ueberblick: Art. 1 Wuerde, Art. 2 freie Entfaltung, Art. 3 Gleichheit, Art. 4 Glaubensfreiheit, Art. 5 Meinungsfreiheit, Art. 8 Versammlung, Art. 12 Berufsfreiheit, Art. 14 Eigentum. Schutzbereich, Eingriff, Schranken, Schranken-Schranken. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Grundrechte Ueberblick
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `unterlagen-luecken`

_Lücken- und Beschaffungsliste für Verfassungsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Letzter fachgerichtl. Beschluss, Verfassungsbeschwerde-Schriftsatz, Vorlagebeschluss), nennt pro Lücke Beweisthema, Beschaffungsweg (BVerfG), Frist und Ersatznachweis._

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Verfassungsrecht** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `acht-zahlen-schwellen-und-berechnung` — Acht Zahlen Schwellen und Berechnung
- `bundesverfassungsgericht-quellenkarte-check` — Bundesverfassungsgericht Quellenkarte Check
- `bverfg-rechtsprechung-recherchieren` — Bverfg Rechtsprechung Recherchieren
- `bverfg-verfahrenssicht-und-annahmerisiko` — Bverfg Verfahrenssicht und Annahmerisiko
- `formelle-mehrparteien-konflikt-und-interessen` — Formelle Mehrparteien Konflikt und Interessen
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf GG Konformitaet Pruefen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Pruefen
- `grundgesetz-fristen-form-und-zustaendigkeit` — Grundgesetz Fristen Form und Zustaendigkeit
- `grundrechte-fehlerkatalog` — Grundrechte Fehlerkatalog
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `grundrechtspruefung-und-verhaeltnismaessigkeit` — Grundrechtspruefung und Verhaeltnismaessigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Verfassungsrecht-Frage zwingend (Verfassungsbeschwerde, Antrag auf einstweilige Anordnung, Annahmebeschluss, BVerfGE-Entscheidung)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (§ 93 BVerfGG Verfassungsbeschwerde 1 Monat nach Rechtswegerschöpfung / 1 Jahr bei Gesetzen, § 32 BVerfGG einstweilige Anordnung), beweisrelevant, formerheblich.
- Rückfrageschreiben an Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `anschluss-routing`

_Anschluss-Routing für Verfassungsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 93 BVerfGG 1 Monat Verfassungsbeschwerde, Letzter fachgerichtl. Beschluss, Verfassungsbeschwerde-Schriftsatz, Vorlagebeschluss), dokumentiert Router-Entscheidung mit Begründung._

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Verfassungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `acht-zahlen-schwellen-und-berechnung` — Acht Zahlen Schwellen und Berechnung
- `bundesverfassungsgericht-quellenkarte-check` — Bundesverfassungsgericht Quellenkarte Check
- `bverfg-rechtsprechung-recherchieren` — Bverfg Rechtsprechung Recherchieren
- `bverfg-verfahrenssicht-und-annahmerisiko` — Bverfg Verfahrenssicht und Annahmerisiko
- `formelle-mehrparteien-konflikt-und-interessen` — Formelle Mehrparteien Konflikt und Interessen
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf GG Konformitaet Pruefen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Pruefen
- `grundgesetz-fristen-form-und-zustaendigkeit` — Grundgesetz Fristen Form und Zustaendigkeit
- `grundrechte-fehlerkatalog` — Grundrechte Fehlerkatalog
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `grundrechtspruefung-und-verhaeltnismaessigkeit` — Grundrechtspruefung und Verhaeltnismaessigkeit
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Verfassungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 93 BVerfGG Verfassungsbeschwerde 1 Monat nach Rechtswegerschöpfung / 1 Jahr bei Gesetzen, § 32 BVerfGG einstweilige Anordnung), notwendige Dokumente (Verfassungsbeschwerde, Antrag auf einstweilige Anordnung, Annahmebeschluss, BVerfGE-Entscheidung), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

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

---

## Skill: `vfgr-verfassungsbeschwerde-substantiierung-spezial`

_Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittelbar, Rechtswegerschoepfung: Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaerti..._

# Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittelbar, Rechtswegerschoepfung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittelbar, Rechtswegerschoepfung. Pruefraster für Anwalt.

### VfgR: VB-Substantiierung

## Fachkern: VfgR: VB-Substantiierung
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

