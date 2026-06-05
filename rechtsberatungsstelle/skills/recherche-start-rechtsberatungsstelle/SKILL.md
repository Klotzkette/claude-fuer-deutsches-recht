---
name: recherche-start-rechtsberatungsstelle
description: "Recherche Start Rechtsberatungsstelle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Recherche Start Rechtsberatungsstelle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Recherche Start Rechtsberatungsstelle** im Plugin Rechtsberatungsstelle (RDG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `recherche-start` | Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, verifizierbare Quellen, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Studierende recherchieren und verifizieren eigenständig. Lädt, wenn ein Studierender fragt, wo er mit einer Recherche anfangen soll, einen Fahrplan für eine Rechtsfrage benötigt oder Lücken in bestehender Recherche identifizieren möchte. |
| `rechtsberatungsstelle-anpassen` | Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezifische Beratungsordnung. Prüfraster Rechtsgebiete einstellen, Zielgruppe und Sprachstil, Beratungsschein-Regelungen, Anleiter-Kontakte und Eskalationspfade konfigurieren. Output konfiguriertes Plugin-Profil mit angepassten Workflows für die jeweilige Stelle. Abgrenzung zu Kaltstart-Interview für Erst-Einrichtung und zu Einarbeitung-Skill. |
| `semester-uebergabe` | Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des Mandatsgeheimnisses sauber an die nächste übergibt. Liest Fristendatei, Mandantenkommunikationslog und Fallhistorie. Lädt, wenn der Supervisor oder abgehende Studierende den Semesterabschluss koordinieren, Übergabenotizen erstellen oder einen ausscheidenden Studierenden abmelden müssen. |

## Arbeitsweg

Im Plugin Rechtsberatungsstelle (RDG) gilt für **Recherche Start Rechtsberatungsstelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `recherche-start`

**Fokus:** Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, verifizierbare Quellen, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Studierende recherchieren und verifizieren eigenständig. Lädt, wenn ein Studierender fragt, wo er mit einer Recherche anfangen soll, einen Fahrplan für eine Rechtsfrage benötigt oder Lücken in bestehender Recherche identifizieren möchte.

# Recherchefahrplan: Orientierung, keine Recherche

## Zweck

Juristische Recherche ist ein Kernbestandteil der klinischen Ausbildung. Die Initialphase — die richtige Norm finden, den Rahmen verstehen, den Einstieg schaffen — ist jedoch oft die zeitintensivste und bildungsmäßig geringwertigste Phase. Studierende verbringen Stunden damit, den Startpunkt zu finden, bevor sie eigentlich forschen können.

Diese Skill liefert den Startpunkt: Normen zum Nachschlagen, Rechtsprechungsbereiche zum Untersuchen, Suchbegriffe für amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang und dejure. **Nichts davon ist verifiziert. Nichts davon ist zitierfähig. Alles ist ein Hinweis, dem der Studierende nachgehen muss.**

**Dies ist eine pädagogische Absicherung, keine bloße Zeitersparnis.** Studierende lernen weiterhin zu recherchieren — sie beginnen nur von einem besseren Ausgangspunkt.

## Eingaben

- **Rechtsfrage** — so präzise wie möglich formuliert; nicht "Mietrecht", sondern "Kann die Mieterin die Miete mindern, weil die Heizung seit November defekt ist und der Vermieter nicht reagiert hat?"
- **Rechtsgebiet** (optional, falls nicht aus der Frage erkennbar)
- **Bisherige Recherche** (optional) — bereits gefundene Normen oder Entscheidungen für Lückenanalyse

## Rechtlicher Rahmen

### Primärquellen-Hierarchie im deutschen Recht

- **Bundesrecht** geht Landesrecht vor (Art. 31 GG).
- **EU-Recht** hat Vorrang vor nationalem Recht; bei europarechtlichem Bezug (z. B. Verbraucherrecht, Datenschutz, Wettbewerbsrecht) immer auch EU-Rechtsakte und EuGH-Rspr. prüfen.
- **Gesetzliche Grundlage → Ausführungsverordnung → Verwaltungsvorschrift** — Hierarchie im Verwaltungsrecht.
- Für studentische Beratungsstellen besonders relevant: **BGB, ZPO, VwVfG, VwGO, AGG, KSchG, BerHG, RDG**.

### Leitentscheidungen zur Recherchemethodik (exemplarisch)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 0: Klinik-Vorlagendokumente zuerst lesen

Bevor der Fahrplan aufgebaut wird: Die eigenen Vorlagendokumente der Klinik lesen. Der Supervisor hat beim Kalt-Start Handbücher, Einreichungsanleitungen, Musterakten und Altgutachten hinterlegt — sie sind fachlich geprüft, spezifisch für die Klinik und schlagen jede Datenbanksuche in den ersten zwanzig Minuten.

1. Klinik-Konfiguration (CLAUDE.md) → `## Vorlagendokumente` lesen. Gibt es Dokumente, deren Zweck oder Dateiname zur Rechtsfrage passt (z. B. "Mietrecht-Einreichungsleitfaden" für eine Mietminderungsfrage)?
2. Für jeden Treffer: als **Vorlagendokumente zuerst lesen**-Block an den Anfang des Fahrplans stellen. Dokumentnamen angeben, warum relevant, was es abdeckt und wo außerhalb davon noch recherchiert werden muss.
3. Falls keine Vorlagendokumente zur Frage passen: ausdrücklich benennen ("Keine Klinik-Vorlagendokumente zu dieser Frage — direkt zu den Primärquellen").

### Schritt 1: Frage präzisieren

Was ist die Rechtsfrage? Präzise formulieren. Nicht "Kündigung" — sondern: "Ist die fristlose Kündigung des Arbeitsvertrags vom 15.04.2026 rechtswirksam, obwohl dem Arbeitgeber keine Abmahnung vorausgegangen ist?"

Bei zu breiter Frage mit dem Studierenden eingrenzen: "Das sind drei Rechtsfragen. Welche zuerst?"

### Schritt 2: Fahrplan aufbauen

**Gesetzliche Ausgangspunkte:**
Wahrscheinlich einschlägige Normen nennen. Ausdrücklich als ungeprüft kennzeichnen.

> **Wahrscheinlich einschlägig** (UNGEPRÜFT — Aktualität und Einschlägigkeit verifizieren):
> - § 626 BGB — Außerordentliche Kündigung aus wichtigem Grund; Zweiwochenfrist (§ 626 Abs. 2 BGB)
> - § 314 BGB — Außerordentliche Kündigung von Dauerschuldverhältnissen
> - §§ 1, 2 KSchG — Soziale Rechtfertigung; Anwendbarkeit prüfen (Betriebsgröße, Beschäftigungsdauer)
> - `[PRÜFEN: Paragraphennummern gegen aktuelle Fassung verifizieren — Gesetze werden umnummeriert]`

**Rechtsprechungsbereiche:**
Nicht Entscheidungen — Bereiche. Die Entscheidungen findet der Studierende selbst.

> **Rspr.-Bereiche:**
> - BAG-Rspr. zu Abmahnungserfordernis vor fristloser Kündigung — Leitentscheidung des BAG suchen
> - BAG-Rspr. zum "wichtigen Grund" i. S. d. § 626 BGB — Fallgruppen (Diebstahl, Arbeitsverweigerung, etc.)
> - Rspr. zum Verhältnismäßigkeitsgrundsatz bei Kündigung ohne vorherige Abmahnung
> - Rspr. zu den Anforderungen an die Anhörung des Betriebsrats (§ 102 BetrVG) — falls Betriebsrat vorhanden

**Kommentare und Sekundärquellen:**

> **Kommentare (zum Einstieg, nicht als Quelle zitieren):**
> - Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
> - Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
> - Praxishandbuch Arbeitsrecht (beck-online) — Einstieg für typische Fallkonstellationen

**Suchbegriffe:**

> **Suchbegriffe für juris / beck-online / dejure:**
> - juris: `fristlose Kündigung Abmahnung Erfordernis Arbeitnehmer § 626`
> - beck-online: `außerordentliche Kündigung ohne Abmahnung BAG`
> - dejure.org: `§ 626 BGB Rechtsprechung — Abmahnungserfordernis`
> - Ergebnisse verfeinern basierend auf den Treffern — diese sind Einstiegsabfragen

### Schritt 3: Unsicherheiten kennzeichnen

Wenn die Skill unsicher ist, ob eine Quelle einschlägig oder aktuell ist:

> `[UNSICHER: ob § 314 BGB hier neben § 626 BGB anwendbar ist — die Rspr. wird es zeigen]`

Unsicherheit wird benannt, nicht verschwiegen.

**Kein stilles Ergänzen:** Diese Skill liefert Hinweise, keine geprüften Quellen — das ist so gewollt. Falls eine Suchanfrage in einer konfigurierten Datenbank wenige oder keine Treffer ergibt, dies ausdrücklich sagen und aufhören. Lücken nicht durch Modellwissen oder Websuche ohne Rückfrage füllen. Stattdessen: "Die Suche ergab [N] Treffer in [Datenbank]. Die Abdeckung scheint dünn für [Frage/Norm]. Optionen: (1) Suchabfrage erweitern, (2) andere Datenbank probieren, (3) Websuche — Treffer werden als `[Websuche — verifizieren]` markiert und sind vor der Verwendung gegen Primärquellen zu prüfen, oder (4) Lücke dem Supervisor melden. Welche Option bevorzugen Sie?" Der Supervisor entscheidet über weniger verlässliche Quellen.

### Schritt 4: Bestehende Recherche analysieren (wenn vorhanden)

Wenn der Studierende bereits Recherchematerial hochgeladen hat: lesen, was abgedeckt ist, was fehlt.

> **Aus Ihrer bisherigen Recherche:**
> - Vorhanden: [Zusammenfassung des Abgedeckten]
> - Lücke: [Was der Fahrplan oben nahelegt, aber noch nicht gefunden wurde]
> - `[PRÜFEN: Die zitierte Entscheidung [Name] — per Datenbank-Zitieranalyse prüfen, ob sie nicht durch spätere Rspr. eingeschränkt wurde]`

## Ausgabeformat

```markdown
═══════════════════════════════════════════════════════════════════════
 RECHERCHEFAHRPLAN — HINWEISE, KEINE QUELLEN
 Nichts unten ist ein geprüfter Beleg. Jede Norm, jeder Rspr.-Bereich,
 jeder Suchbegriff ist ein Startpunkt für IHRE Recherche. Sie verifizieren
 Aktualität, Einschlägigkeit und Richtigkeit. Sie finden die tatsächlichen
 Entscheidungen. Wenn etwas unten unzutreffend oder veraltet ist, liegt
 das in der Natur des Instruments — es ist eine Karte, kein Ergebnis.
═══════════════════════════════════════════════════════════════════════

# Recherchefahrplan: [Rechtsfrage]

**Rechtsgebiet:** [Gebiet] | **Bearbeiter/-in:** [Studierender]

## Vorlagendokumente der Klinik (zuerst lesen)

[Per Schritt 0. Passende Klinikdokumente mit Erläuterung benennen.
Falls keine passen: "Keine Klinik-Vorlagendokumente zu dieser Frage — direkt zu den Primärquellen."]

## Gesetzliche Ausgangspunkte (UNGEPRÜFT)

[Liste mit PRÜFEN-Flags]

## Rechtsprechungsbereiche

[Bereiche, keine Entscheidungen]

## Kommentare und Sekundärquellen (zum Orientieren, nicht als Quelle)

[Liste]

## Suchbegriffe

**juris:** [Abfragen]
**beck-online:** [Abfragen]
**dejure:** [Abfragen]

## Unsicherheitsmarkierungen

[Stellen, an denen der Fahrplan genuinely unsicher ist]

---

## Nächste Schritte

1. Mit einem Kommentar einsteigen, um den Rahmen zu verstehen
2. Die gesetzlichen Normen suchen — verifizieren, ob die Angaben oben aktuell sind
3. Suchbegriffe in den Datenbanken starten, Leitentscheidungen finden
4. Jede Entscheidung per Zitieranalyse (juris: "Rechtsprechung zu diesem Urteil") auf Aktualität prüfen
5. Zurückgehen und `/memo` nutzen, um die Analyse zu strukturieren, sobald die Normen feststehen

## Was dieser Fahrplan nicht leistet

- **Er liefert keine zitierfähigen Belege.** Jeder Hinweis oben ist zu verifizieren.
- **Er ersetzt nicht die Recherche.** Sie recherchieren. Der Fahrplan bringt Sie schneller an den Startpunkt.
- **Er deckt keine Spezialmaterie ab.** Für Nischenrechtsgebiete (z. B. spezifisches Landesrecht, Sondergerichtsbarkeit) ggf. Supervisor fragen.

---
```

## Beispiel

**Szenario:** Studierende Hofer recherchiert für Mandantin Erdem: Kann sie die Miete mindern, weil die Heizung seit November defekt ist?

Fahrplan enthält:
- Gesetzliche Ausgangspunkte: `§ 536 BGB (Mietminderung), § 536a BGB (Schadensersatz), § 536c BGB (Anzeigepflicht) [UNGEPRÜFT — verifizieren]`
- Rspr.-Bereiche: "AG/LG München und Hamburg Rspr. zu Heizungsausfall als erheblicher Mangel; Minderungsquoten-Rspr.; Anzeigepflicht-Rspr."
- Suchbegriffe: `juris: "§ 536 BGB Heizung Mietminderung erheblicher Mangel"`
- Unsicherheit: `[UNSICHER: ob Frau Erdems mündliche Anzeige am 05.11.2025 die Formerfordernisse des § 536c BGB erfüllt — Rspr. prüfen]`

## Risiken und typische Fehler

- **Fahrplan-Hinweise als fertige Belege behandeln:** Die häufigste Fehlerquelle. Normen und Rspr.-Bereiche müssen in den Datenbanken nachgeschlagen, auf Aktualität geprüft und korrekt zitiert werden.
- **Nur eine Datenbank nutzen:** Verschiedene Datenbanken decken unterschiedliche Quellen ab. amtliche/freie Quellen oder lizenzierte Datenbanken ergänzen sich; dejure eignet sich für schnelle Normensuche.
- **Keine Zitieranalyse:** Eine Entscheidung, die in einer neueren höchstrichterlichen Entscheidung eingeschränkt wurde, kann nicht mehr als Beleg verwendet werden. Zitieranalyse in juris (Rubrik "Rechtsprechung zu diesem Urteil") ist Pflicht.
- **Lücke schweigend überbrücken:** Wenn eine Suchanfrage wenige Treffer ergibt, nicht durch Modellwissen ergänzen. Den Supervisor informieren und auf eine verlässlichere Quelle warten.

## Quellenpflicht

Jeder im Fahrplan vorgeschlagene Hinweis ist mit der Herkunft zu kennzeichnen: `[juris]`, `[beck-online]`, `[dejure]` für datenbankgestützte Hinweise; `[Websuche — verifizieren]` für webbasierte Hinweise; `[Modellwissen — verifizieren]` für aus dem Modell stammende Hinweise. Hinweise mit "verifizieren" tragen höheres Fehlerrisiko und sind zuerst gegen Primärquellen zu prüfen. Tags nicht entfernen — sie sind das schnellste Signal für den Supervisor, welche Stellen besonderer Aufmerksamkeit bedürfen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

## 2. `rechtsberatungsstelle-anpassen`

**Fokus:** Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezifische Beratungsordnung. Prüfraster Rechtsgebiete einstellen, Zielgruppe und Sprachstil, Beratungsschein-Regelungen, Anleiter-Kontakte und Eskalationspfade konfigurieren. Output konfiguriertes Plugin-Profil mit angepassten Workflows für die jeweilige Stelle. Abgrenzung zu Kaltstart-Interview für Erst-Einrichtung und zu Einarbeitung-Skill.

# /anpassen

1. Lade `CLAUDE.md` → aktuelles Profil anzeigen.
2. Frage: Welcher Abschnitt soll geändert werden?
3. Führe die gezielte Änderung durch – kein Full-Redo.
4. Aktualisierte Datei ausgeben.

---

# Beratungsstellenprofil anpassen


## Triage zu Beginn
1. Welcher Abschnitt des Profils soll angepasst werden: Semesterwechsel, Fachbereich, Prüfungsgates, Anleiter-Kontakt oder Gesetzesaenderung?
2. Hat sich die Rechtsgrundlage der Beratungsstelle geaendert (z.B. neues RDG, neue Kooperationsvereinbarung)?
3. Sind neue Studierende aufgenommen worden, die in die CLAUDE.md eingetragen werden muessen?
4. Soll gleichzeitig ein Fachbereichsleitfaden angepasst werden oder nur das Hauptprofil?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Anleitungsstruktur muss aktuell und wirksam sein; Semesterwechsel erfordert Profil-Update
- Art. 30 DSGVO — Verarbeitungsverzeichnis: bei Aenderung des Verarbeitungsumfangs zu aktualisieren
- §§ 43, 43a BRAO — Berufspflichten des Anleiters: kontinuierliche Aktualitaet der Organisationsunterlagen
- § 203 Abs. 4 StGB — Einbeziehung Dritter: bei Wechsel von Studierenden neue Verschwiegenheitsvereinbarungen pruefen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Nach der Ersteinrichtung (`/kaltstart-interview`) müssen Beratungsstellenprofile regelmäßig aktualisiert werden:
- Semesterwechsel: Neue Studierende, neuer Anleiter.
- Neuer Fachbereich hinzugefügt.
- Gesetzesänderung (z. B. neue Regelbedarfsstufen SGB II, neues BAMF-Merkblatt).
- Neue örtliche Kooperationspartner.
- Prüfungsgates angepasst (erfahrene Studierende brauchen weniger Gateways).

Dieser Skill macht gezielte Änderungen, ohne das gesamte Profil neu aufzurollen.

**Nur für den anleitenden Volljuristen.**

## Häufige Anpassungsszenarien

### 1. Semesterwechsel

> Welche Studierenden sind neu? Welche gehen? Wer übernimmt laufende Mandate?

Änderungen in `CLAUDE.md`:
- `Semester: [WS 2024/25]` → `[SS 2025]`
- Liste der aktiven Studierenden aktualisieren.
- Mandate-Übergabe: Verweis auf `/rechtsberatungsstelle:semester-übergabe`.

### 2. Neuen Fachbereich hinzufügen

Fachbereich in `CLAUDE.md` unter `Fachbereiche` ergänzen. Dann sofort:
> "Soll für den neuen Bereich auch ein Leitfaden erstellt werden? → `/rechtsberatungsstelle:leitfaden-erstellen [fachbereich]`"

### 3. Prüfungsgates ändern

> Welche Gates sollen geändert werden? Verschärfen oder lockern?

Tabelle in `CLAUDE.md` → `Aufsichtsmodell` anpassen. Hinweis: Lockerung nur bei nachgewiesener Erfahrung der Studierenden. § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche Anleitung.

### 4. Gesetzesänderungen einpflegen

Häufige Anlässe:
- Neue Regelbedarfsstufen SGB II ab 1. Januar (jährliche Anpassung per Regelbedarfsermittlungsgesetz).
- Neues BAMF-Merkblatt oder Entscheidungspraxis zu einem Herkunftsland.
- BGH-Urteil zur Schönheitsreparatur / Mieterhöhung.
- Änderungen im AsylG / AufenthG.

Pflegen Sie in `CLAUDE.md` → `Wichtige Normen` die relevante Änderung ein. Datum der Änderung festhalten.

### 5. Örtliche Kontakte aktualisieren

Jobcenter, Ausländerbehörde, BAMF-Außenstelle, Gericht, Dolmetscherdienste – Telefon, Zuständigkeit, Sprechzeiten.

### 6. Pädagogikhaltung ändern

Für ein bestimmtes Semester oder einen bestimmten Studierenden die Default-Haltung anpassen. Z. B.: "Für dieses Semester soll der Skill primär im Modus 'Anleiten' arbeiten, da alle Studierenden im ersten Klinik-Semester sind."

## Ablauf

### Schritt 1: Aktuelles Profil anzeigen

Gesamte `CLAUDE.md` ausgeben als Referenz.

### Schritt 2: Gezielter Abschnitt

Welcher Abschnitt? Optionen:
- `[A]` Beratungsstellentyp und Rechtsgrundlage
- `[B]` Fachbereiche
- `[C]` Aufsichtsmodell / Prüfungsgates
- `[D]` Pädagogikhaltung
- `[E]` Verschwiegenheitsorganisation
- `[F]` Örtliche Besonderheiten / Kontakte
- `[G]` Wichtige Normen (Gesetzesänderung)
- `[H]` Semester / Studierende
- `[L]` Fachbereichsleitfaden `guides/<name>.md`

### Schritt 3: Änderung durchführen

Nur den angegebenen Abschnitt bearbeiten. Alle übrigen Abschnitte unverändert lassen.

### Schritt 4: Änderungshistorie

Am Ende der `CLAUDE.md` einen Änderungseintrag hinzufügen:
```
## Änderungshistorie
- [Datum] Abschnitt [B] geändert: SGB IX / § 76b hinzugefügt. [Kürzel Anleiter]
- [Datum] Abschnitt [H] geändert: Semesterwechsel SS 2025. [Kürzel Anleiter]
```

## Ausgabeformat

Vollständige, aktualisierte `CLAUDE.md` (oder `guides/<name>.md`). Kein `[KI-GESTÜTZTER ENTWURF]`-Vermerk.

## Risiken / typische Fehler

- **Versehentliches Löschen:** Beim Anpassen einzelner Abschnitte nie den Rest des Profils löschen. Immer vollständige Datei ausgeben, nicht nur den geänderten Abschnitt.
- **Gesetzesänderungen nicht eingepflegt:** Veraltertes Profil führt dazu, dass der Skill mit überholten Normen arbeitet (z. B. falsche Regelbedarfsstufen, falsche Fristen).
- **Mandate ohne Übergabe:** Beim Semesterwechsel sicherstellen, dass alle laufenden Mandate über `/rechtsberatungsstelle:semester-übergabe` übergeben werden, bevor das Profil auf das neue Semester umgestellt wird.

## 3. `semester-uebergabe`

**Fokus:** Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des Mandatsgeheimnisses sauber an die nächste übergibt. Liest Fristendatei, Mandantenkommunikationslog und Fallhistorie. Lädt, wenn der Supervisor oder abgehende Studierende den Semesterabschluss koordinieren, Übergabenotizen erstellen oder einen ausscheidenden Studierenden abmelden müssen.

# Semesterübergabe

## Zweck

Jedes Semester verliert die Rechtsberatungsstelle ihre gesamte studentische Belegschaft und baut sie neu auf. `/einarbeitung` löst die eine Hälfte des Problems — Onboarding der neuen Kohorte. Diese Skill löst die andere Hälfte: Sie verabschiedet die abgehende Kohorte, indem sie Übergabenotizen erstellt, die alle für den Fortgang notwendigen Informationen zu jedem laufenden Mandat enthalten.

Ohne diese Übergabe verlässt das Fallwissen die Beratungsstelle mit den Studierenden. Die neue Kohorte beginnt mit der Fallakte und der Aktennotiz — das reicht nie. Zwei Wochen gehen für die Wiedereinarbeitung verloren; der Mandant erlebt dies als Rückschritt: Anrufe bleiben unbeantwortet, bereits beantwortete Fragen werden erneut gestellt.

**Mandatsgeheimnis:** Übergabenotizen enthalten vertrauliche Mandantendaten (§ 43a Abs. 2 BRAO, § 203 StGB). Sie werden ausschließlich innerhalb der Beratungsstelle zwischen beteiligten Studierenden und dem Supervisor ausgetauscht — niemals per privater E-Mail, Chat-Dienst oder sonstiger ungesicherter Verbindung.

## Eingaben

- **Semester** (Standard: laufendes Semester)
- **Einzelner Fall** (optional: `--fall=[fall-id]`) für Einzelfall-Übergabe (z. B. bei vorzeitigem Ausscheiden)
- **Aktive Fallliste** — wenn die Klinik kein zentrales Fallregister führt, muss diese als Eingabe übergeben werden; die Skill erfindet keine Fälle
- **Zuordnung:** Wer geht, wer kommt — falls bekannt; sonst "TBD — Supervisor weist zu"

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht des Rechtsanwalts; gilt sinngemäß für Studierende der Beratungsstelle. Die Übergabenotiz enthält nur Informationen, die für die Fallfortführung unbedingt notwendig sind.
- **§ 203 Abs. 1, Abs. 3 StGB** — Verletzung von Privatgeheimnissen: Die Weitergabe von Mandantendaten an nicht-befugte Dritte ist strafbar. Studierende als "berufsmäßig tätige Gehilfen" i. S. d. § 203 Abs. 3 S. 2 StGB.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Fallübergaben sind ein Aufgabenbereich, der der Supervisorenkontrolle bedarf; der begleitende Rechtsanwalt/die begleitende Rechtsanwältin zeichnet die Übergabe ab.
- **§ 50 BRAO** — Aufbewahrungspflicht für Handakten: Der Supervisor hat Unterlagen nach Mandatsende mindestens 5 Jahre aufzubewahren; die Übergabenotizen sind Teil der Handakte im Rechtssinne.
- **DSGVO Art. 5 Abs. 1 lit. f** (Integrität und Vertraulichkeit), **Art. 32 DSGVO** — Technische und organisatorische Maßnahmen für die Datensicherheit; sichere Übertragungswege für Übergabenotizen.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1: Fälle und Zuständigkeiten identifizieren

- Alle aktiven Fälle erfassen (aus Fallregister + `deadlines.yaml` Fall-IDs + Kommunikationslogs)
- Für jeden Fall: Wer ist der aktuelle/die aktuelle Bearbeiter/-in? Bleibt diese Person oder scheidet sie aus?
- Zuordnung: Ausscheidende/-r → Nachfolger/-in (falls bekannt; sonst "TBD — Supervisor weist zu")

Falls kein zentrales Fallregister existiert: Eingabe einer Fallliste erforderlich. Nicht raten.

### Schritt 2: Fallbezogene Übergabenotiz

Für jeden Fall:

```markdown
# Fallübergabe — [Fallbezeichnung] — [Semester-Ende]

**Fall-ID:** [fall-id]
**Rechtsgebiet:** [Gebiet]
**Ausscheidende/-r Studierende/-r:** [Name]
**Nachfolger/-in:** [Name oder "TBD"]
**Begleitender Supervisor:** [Name]
**Mandant:** [Name oder Mandanten-ID — kein Klarname in unsicheren Systemen]

---

## Aktueller Stand

[Ein Absatz: Verfahrensstand. Was ist getan, was steht aus, wo geht der Fall hin.
Falls der Fall an einem natürlichen Haltepunkt steht (zwischen Einreichungen, wartend
auf Behördenantwort), dies benennen.]

## Offene Fristen

*Aus `deadlines.yaml`. Erste Aufgabe der/des Nachfolger/-in: Fristen bestätigen und übernehmen.*

| Fällig | Typ | Beschreibung | Hinweise |
|---|---|---|---|
| [Datum] | [Typ] | [Einzeiler] | [bei Dringlichkeit: "DRINGEND — fällig innerhalb von [N] Tagen nach Semesterbeginn"] |

## Was getan wurde

- [Wichtige Schritte dieses Semesters: Erstberatung, Einreichungen, Termine, wesentliche Schriftstücke]
- [Erstellte Dokumente — mit Verweis auf Ablageort]

## Was noch offen ist

- [Ausstehende Entscheidungen: z. B. "Mandantin hat noch nicht über das Vergleichsangebot entschieden"]
- [Recherche-Lücken: z. B. "§ 556g BGB Mietpreisbremse — Ausnahmen noch nicht abschließend geprüft"]
- [Offene Kommunikation: z. B. "Antwort der Behörde auf Widerspruch ausstehend"]

## Mandantenbeziehung

- [Wie oft Kontakt? Telefon, E-Mail, persönlich?]
- [Relevanter Beziehungskontext für Nachfolger/-in: Sprache, besondere Lebensumstände, Kommunikationspräferenzen]
- [Nächster geplanter Kontakt oder Termine]

## Erstellte und eingereichte Schriftstücke

*Verweise, kein Inhalt.*

- [Datum] [Schriftstücktyp] — [Ablagepfad] — [Status: eingereicht / Entwurf / in Supervisor-Prüfung]

## Kommunikationshistorie-Zusammenfassung

*Aus dem Kommunikationslog. Dreizeilige Zusammenfassung hier; Nachfolger/-in liest den vollständigen Log.*

[Kurze Zusammenfassung des jüngsten Kommunikationsmusters — z. B. "3 Telefonate seit Erstberatung, alle auf Russisch, Mandantin bevorzugt abends. Letzter Kontakt: 15.04.2026, Adresse für Schriftstück bestätigt."]

## Hinweise des Supervisors an Nachfolger/-in

*Vom Supervisor vor Weiterleitung der Übergabenotiz ergänzt. Kann enthalten: "Dieser Fall hat eine sensible Familiensituation — Akte vor dem ersten Kontakt genau lesen"; "Mandant hat gebeten, alle Post an Postfach, nicht Hausadresse"; "Es gibt noch eine offene Scoping-Frage — erste Woche mit mir besprechen."*

[Hinweise, oder "keine"]

## Erste-Woche-Prioritäten für Nachfolger/-in

1. [Konkret — z. B. "Mandantin innerhalb von 48 Stunden nach Fallübernahme anrufen. Sich vorstellen, Fallübernahme bestätigen."]
2. [Fristenbezogen — z. B. "Widerspruchsfrist endet am [Datum]. Entwurf des abgehenden Studierenden prüfen, überarbeiten, einreichen."]
3. [Wissenslücke — z. B. "Gutachten des abgehenden Studierenden zur Mietpreisbremse lesen, bevor am [Datum] die Verhandlung stattfindet."]

---

**Übergabe erstellt von:** [Ausscheidende/-r Studierende/-r]
**Datum:** [JJJJ-MM-TT]
**Geprüft von:** [Supervisor, sofern Supervisionsmodell dies vorsieht]
```

### Schritt 3: Kohorten-Gesamtübersicht

Nach allen fallbezogenen Notizen, `handoffs/[semester]/_zusammenfassung.md` erstellen:

```markdown
# Kohortenübergabe-Zusammenfassung — [Semester-Ende]

**Ausscheidende Studierende:** [N]
**Eintretende Studierende:** [N]
**Laufende, zu übergebende Fälle:** [N]
**Fälle, die zum Semesterende abgeschlossen werden (keine Übergabe):** [N]

---

## Übergaben

| Fall | Ausscheidend | Nachfolge | Rechtsgebiet | Dringlichkeit |
|---|---|---|---|---|
| [fall-id] | [Name] | [Name oder TBD] | [Gebiet] | [normal / Frist innerhalb 2 Wochen / dringend] |

## Nicht zugewiesen

[Fälle, für die "TBD" als Nachfolger/-in eingetragen ist — Supervisor weist vor Semesterstart zu]

## Fristen innerhalb von 30 Tagen nach Semesterbeginn

[Aus deadlines.yaml — das sind die Fälle, in die die neue Kohorte sofort einarbeiten muss]

## Hinweise für den Supervisor

- [Falls in diesem Semester besondere Leistungsprobleme bei Studierenden aufgefallen sind — für engere Begleitung im Folgesemester notieren]
- [Falls ausscheidende Studierende bereit sind, für den Nachfolger/die Nachfolgerin zur Verfügung zu stehen — z. B. Absolvent/-in, der/die die Übergabe begleiten möchte]
- [Muster über Fälle hinweg — z. B. "Drei von sechs Fällen haben Fristen in den ersten 14 Tagen des neuen Semesters; ggf. Onboarding-Übungen auf diese Rechtsgebiete fokussieren"]
```

### Schritt 4: Supervisoren-Prüfung

Das Schließen oder Übergeben eines Falls ist eine folgenschwere Handlung. Das Gate ist das Supervisionsmodell der Beratungsstelle (§ 6 Abs. 2 RDG). Fallabschluss-Notizen werden immer vom Supervisor abgezeichnet, bevor der Fall im Übergabedokument als geschlossen markiert wird — unabhängig vom gewählten Supervisionsmodell.

- **Formelle Prüfwarteschlange:** Jede Übergabenotiz geht in die Warteschlange, bevor sie an den/die Nachfolger/-in weitergeleitet wird.
- **Konfigurierbare Flags:** Notizen erhalten "VOR WEITERLEITUNG MIT [SUPERVISOR] PRÜFEN"; Supervisor prüft informell.
- **Leichtere Begleitung:** Standard-KI-Label; Supervisor prüft über bestehende Betreuungsstruktur. Fallabschlüsse gehen dennoch vor Markierung als geschlossen an den Supervisor.

### Schritt 5: Übergabe vollziehen

Nach Supervisoren-Prüfung liegen die Übergabenotizen unter `handoffs/[semester]/[fall-id].md`. Der/die Nachfolger/-in liest sie im `/einarbeitung`-Durchlauf zu Semesterbeginn — `/einarbeitung` soll die Notizen für die zugewiesenen Fälle surfacen.

## Ausgabeformat

Per-Fall-Übergabenotiz (Markdown) plus Kohortenübersicht, beide nach dem Schema oben. Alle Notizen werden ausschließlich innerhalb der Beratungsstelle über sichere, bestellungsführende Systeme ausgetauscht.

## Beispiel

**Szenario:** Studierende Müller beendet das Semester und gibt Fall `erdem-mietrecht-2026` an nachfolgende Studierende Schulze weiter. Frist: Widerspruch gegen Mieterhöhung am 08.06.2026.

Übergabenotiz enthält: aktueller Stand (Widerspruchsentwurf fertig, wartet auf Supervisoren-Freigabe), Fristtabelle (08.06.2026 — DRINGEND), Was getan wurde (Erstberatung 15.03.2026, Entwurf 01.04.2026), Hinweis Supervisor: "Mandantin spricht nur Türkisch — Schulze soll Dolmetscher organisieren."

## Risiken und typische Fehler

- **Übergabe ohne Mandatsgeheimniswahrung:** E-Mail-Versand von Übergabenotizen über private Konten oder Chat-Dienste verstößt gegen § 203 StGB und DSGVO Art. 5. Nur bestellungsführende, gesicherte Systeme.
- **Fristenübergabe vergessen:** Die gefährlichste Lücke. Alle aktiven Fristen müssen in der Notiz erscheinen; Nachfolger/-in muss sie in `/fristen` als eigene Fristen neu eintragen.
- **Übergabe ohne Supervisoren-Abzeichnung:** § 6 Abs. 2 RDG verlangt effektive Aufsicht. Auch "formlose" Übergaben sind dem Supervisor zu melden.
- **Zu dünne Übergabenotiz:** "Fall läuft gut" ist keine Übergabe. Die Notiz muss so vollständig sein, dass jemand ohne Vorkenntnisse den Fall übernehmen kann.
- **Mandantenkontakt während der Übergabephase nicht gesichert:** Zwischen Ausscheiden der alten und Übernahme durch neue Studierende muss der Supervisor Ansprechbarkeit für den Mandanten sicherstellen.

## Quellenpflicht

Übergabenotizen sind interne Arbeitsdokumente, keine zitierten Rechtsgutachten. Alle darin enthaltenen offenen Rechtsfragen sind in den entsprechenden Skills (`/memo`, `/recherche-start`) mit Quellenangaben zu hinterlegen. Die Übergabenotiz verweist auf das zugrundeliegende Gutachten, zitiert aber keine Normen eigenständig ohne Verifizierung.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
