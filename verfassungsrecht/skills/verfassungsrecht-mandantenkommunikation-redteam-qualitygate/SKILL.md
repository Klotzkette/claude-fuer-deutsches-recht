---
name: verfassungsrecht-mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation Redteam Qualitygate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenkommunikation Redteam Qualitygate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenkommunikation Redteam Qualitygate** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin verfassungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin verfassungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `bverfg-rechtsprechung-recherchieren` | BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Output: Rechtsprechungsueberblick Zitatliste Leitentscheidungen. Abgrenzung: nicht für Verfassungsbeschwerde-Entwurf (verfassungsbeschwerde-entwurf). |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Mandantenkommunikation Redteam Qualitygate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin verfassungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin verfassungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Verfassungsbeschwerde — Erwartungsmanagement an die Mandantschaft

- **Annahmequote ist niedrig:** Über 95 Prozent der Verfassungsbeschwerden werden nicht zur Entscheidung angenommen (§ 93a BVerfGG). Mandantschaft offen darauf hinweisen — keine Erfolgsgarantie suggerieren.
- **Subsidiarität (§ 90 Abs. 2 BVerfGG):** Vor der Verfassungsbeschwerde muss der Fachgerichtsrechtsweg ausgeschöpft sein; klären, ob ein zulässiges Fachgerichtsverfahren übergangen wurde.
- **Substantiierung:** Bereits der Schriftsatz muss die Grundrechtsverletzung schlüssig darlegen; Beweis im engeren Sinne wird nicht erhoben (Aktenverfahren).
- **Kostenrisiko:** Keine Kostenerstattung im Erfolgsfall regelmäßig (§ 34a BVerfGG nur ausnahmsweise). RVG-Hinweis und Honorarvereinbarung sind Pflicht (§ 49b BRAO).
- **Sie-Form, nüchterner Ton:** Keine Kampagnenrhetorik. Verfassungsgerichtliche Sprache ist sachlich, dogmatisch begründet, ohne Polemik.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin verfassungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin verfassungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Red-Team-Checks speziell für Verfassungsrecht

- **Zulässigkeit zuerst:** Beschwerdeberechtigung (eigene, unmittelbare, gegenwärtige Betroffenheit), Beschwerdegegenstand (Akt öffentlicher Gewalt), Rechtswegerschöpfung, Subsidiarität, Frist (§§ 90, 93 BVerfGG).
- **Substantiierung-Test:** Wird der einschlägige Grundrechtsschutzbereich, der Eingriff und seine fehlende Rechtfertigung konkret subsumiert (§§ 23, 92 BVerfGG)?
- **Halluzinations-Check:** Jedes BVerfG-Az. (1 BvR/1 BvL/2 BvE …) auf bundesverfassungsgericht.de verifizieren; keine erfundenen Randnummern.
- **Keine Präjudizienbindung:** Argumentationsfigur "BVerfG hat entschieden, also …" nur, soweit § 31 BVerfGG greift (Tenor + tragende Gründe).
- **Verhältnismäßigkeit dreistufig:** Geeignetheit, Erforderlichkeit, Angemessenheit jeweils gesondert prüfen; bei Schranken-Schranken auch Wesensgehaltsgarantie (Art. 19 Abs. 2 GG) ansprechen.
- **EMRK-/Unionsrechtsbezug:** Wenn Mandant auf Art. 6 EMRK oder GRCh stützt, völkerrechts- und unionsrechtskonforme Auslegung anführen.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `bverfg-rechtsprechung-recherchieren`

**Fokus:** BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Output: Rechtsprechungsueberblick Zitatliste Leitentscheidungen. Abgrenzung: nicht für Verfassungsbeschwerde-Entwurf (verfassungsbeschwerde-entwurf).

# BVerfG-Rechtsprechung recherchieren

## Fachkern: BVerfG-Rechtsprechung recherchieren
- **Spezialgegenstand:** BVerfG-Rechtsprechung recherchieren wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
