---
name: kanzlei-rechtsprechungsrecherche-fristenbuch
description: "Rechtsprechungsrecherche Fristenbuch: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsprechungsrecherche Fristenbuch

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Rechtsprechungsrecherche Fristenbuch** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-rechtsprechungsrecherche` | Recherchiert Rechtsprechung zu einer konkreten Sache in amtlichen Datenbanken der Bundesgerichte und Länder, ergänzt OpenJur und dejure.org, bewertet Treffer, erstellt Zitier- und Verwertungsnotizen und legt Fundstellen samt Quellenprotokoll in der Akte oder freigegebenen Online-Ablage ab. |
| `fristenbuch-fuehren` | Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei Postzustellung (PostModG seit 1.1.2025; bis 31.12.2024 drei Tage). Trennt Notfristen (BRAO-Haftungsrisiko) von Beobachtungsfristen. Setzt Vorfristen typisch fuenf Werktage vor Hauptfrist; bei BRAO-relevanten Notfristen sieben Werktage. Eskalation an Sekretariat und zuständigen Anwalt bei Vorfristerreichung. Audit-Trail jeder Fristaenderung. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Rechtsprechungsrecherche Fristenbuch**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-rechtsprechungsrecherche`

**Fokus:** Recherchiert Rechtsprechung zu einer konkreten Sache in amtlichen Datenbanken der Bundesgerichte und Länder, ergänzt OpenJur und dejure.org, bewertet Treffer, erstellt Zitier- und Verwertungsnotizen und legt Fundstellen samt Quellenprotokoll in der Akte oder freigegebenen Online-Ablage ab.

# Rechtsprechungsrecherche und Fundstellenablage


## Triage zu Beginn
1. Fuer welche Akte und welches Rechtsgebiet wird die Rechtsprechung benoetigt?
2. Welche amtlichen Datenbanken stehen zur Verfuegung: Bundesgerichtsdatenbank, juris, Beck-online, OpenJur?
3. Muss der Sachverhalt vor der Suche abstrahiert/anonymisiert werden (Mandatsgeheimnis)?
4. Soll die Fundstelle in die Akte oder in einen Schriftsatz eingearbeitet werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43 BRAO — Sorgfaltspflicht: Recherchepflicht als Teil der anwaltlichen Beratung
- § 43a Abs. 2 BRAO — Verschwiegenheit: Abstrahierung des Sachverhalts vor Datenbanksuche
- Art. 3 GG i.V.m. Art. 20 Abs. 3 GG — Bindung an Gesetz und Recht: einschlaegige Rechtsprechung ist massgebend
- § 139 ZPO — Richterliche Hinweispflicht: Gericht nutzt bekannte Rechtsprechung; Anwalt muss vorbereitet sein

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill recherchiert gezielt Rechtsprechung zu einer Akte, einem Schriftsatz, einer Replik, einem Vertragsrisiko oder einer internen Rechtsfrage. Er arbeitet quellenbewusst: zuerst amtliche Quellen, dann freie Ergänzungsdatenbanken, danach nur mit Kennzeichnung weitere Quellen.

## Sicherheitsregeln

- Keine Mandatsgeheimnisse in öffentliche Suchfelder kopieren. Sachverhalt vorher abstrahieren.
- Personen, Gegner, interne Aktenzeichen und vertrauliche Vertragsdetails pseudonymisieren, wenn sie für die Suche nicht nötig sind.
- Amtliche Volltexte und PDF-Dateien bevorzugen.
- OpenJur und dejure.org als Ergänzung nutzen, nicht als alleinige Primärquelle, wenn eine amtliche Fassung erreichbar ist.
- Jede Fundstelle mit URL, Abrufdatum, Quelle, Gericht, Datum, Aktenzeichen, ECLI, Entscheidungsart, Rn./Seite und Relevanz dokumentieren.
- Keine Entscheidung als aktuell oder herrschend darstellen, ohne spätere Rechtsprechung und Gegenansichten zu prüfen.
- Online-Ablage, DMS, Cloud, GitHub oder geteilte Ordner nur nach ausdrücklicher Freigabe verwenden.

## Quellenkaskade

1. **Bundesübergreifend amtlich**: `https://www.rechtsprechung-im-internet.de` und Justizportal `https://www.justiz.de/onlinedienste/rechtsprechung/index.php`.
2. **Bundesgerichte direkt**:
 - Bundesverfassungsgericht: `https://www.bundesverfassungsgericht.de/SiteGlobals/Forms/Suche/Entscheidungensuche_Formular.html`
 - Bundesgerichtshof: `https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen.html`
 - Bundesverwaltungsgericht: `https://www.bverwg.de/rechtsprechung`
 - Bundesarbeitsgericht: `https://www.bundesarbeitsgericht.de/entscheidungen/`
 - Bundesfinanzhof: `https://www.bundesfinanzhof.de/de/entscheidungen/entscheidungen-online/`
 - Bundessozialgericht: `https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen.html`
 - Bundespatentgericht: `https://www.bundespatentgericht.de/DE/Rechtsprechung/Entscheidungen/entscheidungen_node.html`
3. **Länderrechtsprechung**: über das Justizportal und die Rechtsprechungsdatenbanken der Länder, z. B. NRWE für Nordrhein-Westfalen.
4. **Ergänzend**: OpenJur und dejure.org für zusätzliche Treffer, Parallelfundstellen, Verlinkungen, Vorinstanzen, Zitatnetz und Presse-/Literaturhinweise.

## Schnellstart

Bei einer neuen Recherche zuerst fragen:

1. Akte oder Arbeitsergebnis: Klage, Replik, Antrag, Vertrag, Gutachten, Mandantenbrief.
2. Rechtsfrage in einem Satz.
3. Gerichtsbarkeit: Zivil, Straf, Arbeits, Verwaltung, Finanz, Sozial, Verfassungsrecht, Patent/Marke.
4. Relevante Normen, Stichworte und bekannte Aktenzeichen.
5. Zeitraum: aktuell, letzte fünf Jahre, Grundsatzrechtsprechung, historisch.
6. Ziel: Fundstellenliste, Schriftsatzbaustein, Argumentationsmatrix, Warnung vor Gegenrechtsprechung oder Monitoring.
7. Ablageort: nur lokal in der Akte, DMS/Cloud/Online-Akte oder Simulation.

Wenn wenig Zeit ist, sofort eine Suchmatrix aus `Norm + Rechtsproblem + Gerichtsbarkeit + Synonyme` erstellen.

## Suchstrategie

1. Rechtsfrage normalisieren: Anspruch, Einwendung, Prozessfrage, Beweisfrage oder Vertragsrisiko.
2. Suchbegriffe bilden:
 - Normen mit und ohne Paragrafenzeichen.
 - juristische Kernbegriffe.
 - Synonyme und alte Begriffe.
 - Aktenzeichen und ECLI, wenn vorhanden.
 - typische Phrasen aus Leitsätzen.
3. Gerichtshierarchie priorisieren:
 - Bundesgericht oder Verfassungsgericht vor Instanzrechtsprechung.
 - Zuständige Fachgerichtsbarkeit vor allgemeiner Suche.
 - Landesrecht zuerst im betroffenen Bundesland, danach vergleichbare Länder.
4. Treffer sichten:
 - amtlicher Volltext vorhanden?
 - Leitsatz oder Orientierungssatz?
 - Tragende Gründe oder obiter dictum?
 - aktuell oder überholt?
 - passt der Sachverhalt wirklich?
5. Gegenrecherche:
 - abweichende Senate, andere Obergerichte, spätere Entscheidungen, Nichtannahme- oder Nichtzulassungsfragen suchen.
 - dejure/OpenJur nur ergänzend für Verweise und Vernetzung nutzen.

## Bewertung

Jeden Treffer einstufen:

- `A`: zentrale amtliche Entscheidung, direkt verwertbar.
- `B`: hilfreich, aber Sachverhalt oder Gerichtsbarkeit weicht ab.
- `C`: nur Hintergrund, ältere Linie, Vorinstanz oder Randaspekt.
- `GEGEN`: spricht gegen die eigene Position oder begrenzt sie.
- `UNSICHER`: Quelle, Aktualität, Volltext oder Kontext unklar.

## Ablage

Standardordner in der Akte:

```text
rechtsprechung/
 YYYY-MM-DD_recherchefrage-kurz/
 suchplan.md
 fundstellen-register.md
 entscheidungen/
 zitiervorschlaege.md
 verwertungsnotiz.md
 ablageprotokoll.md
```

Wenn eine Online-Ablage gewünscht ist:

- Zielsystem und Berechtigung bestätigen.
- Keine vertraulichen Suchbegriffe oder Volltexte öffentlich ablegen.
- Datei- und Ordnernamen ohne Mandatsgeheimnisse wählen.
- Upload- oder Sync-Protokoll mit Zeit, Ziel, Bearbeiter und Dateiliste erstellen.
- Bei fehlender Integration Simulation anbieten.

## Übergabe an andere Skills

- Für Klage, Replik oder Antrag: Ergebnisse an `kanzlei-allgemein-schriftsatz-turbo` übergeben.
- Für Vertrag: Risiken an `kanzlei-allgemein-vertragsentwurf` übergeben.
- Für finale Ausgabe: `kanzlei-allgemein-qualitaetsgate-hardening` ausführen.
- Für Fristen oder Monitoring: `kanzlei-allgemein-automationen` nur mit ausdrücklicher Zustimmung nutzen.

## Ausgabe

- `assets/templates/rechtsprechungsrecherche-suchplan.md`
- `assets/templates/rechtsprechungsfundstellen-register.md`
- `assets/templates/rechtsprechungsablage-protokoll.md`
- optional `assets/templates/rechtsprechungsmonitor.md`

## 2. `fristenbuch-fuehren`

**Fokus:** Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei Postzustellung (PostModG seit 1.1.2025; bis 31.12.2024 drei Tage). Trennt Notfristen (BRAO-Haftungsrisiko) von Beobachtungsfristen. Setzt Vorfristen typisch fuenf Werktage vor Hauptfrist; bei BRAO-relevanten Notfristen sieben Werktage. Eskalation an Sekretariat und zuständigen Anwalt bei Vorfristerreichung. Audit-Trail jeder Fristaenderung.

# Zentrales Fristenbuch der Kanzlei


## Triage zu Beginn
1. Handelt es sich um eine Notfrist (absolut haftungsrelevant: Rechtsmittelfristen) oder eine einfache gesetzliche Frist?
2. Nach welcher Verfahrensordnung laeuft die Frist (ZPO, StPO, VwGO, SGG, FGO, FamFG, AO)?
3. Gilt die neue Vier-Tages-Fiktion nach PostModG (ab 01.01.2025) oder noch die Drei-Tages-Fiktion?
4. Wer ist verantwortlicher Anwalt und wer ist Vertretung bei Abwesenheit?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung nach dem Zivilprozessrecht
- § 517 ZPO — Berufungsfrist ein Monat ab Zustellung des Urteils (Notfrist)
- § 548 ZPO — Revisionsfrist ein Monat ab Zustellung (Notfrist)
- Art. 7 PostModG — Vier-Tages-Zustellungsfiktion fuer Postsendungen ab 01.01.2025

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflicht

Jede Kanzlei muss ein Fristenbuch führen — die Versäumung einer Notfrist ist anwaltliche Pflichtverletzung mit Haftungsrisiko (§ 51 BRAO).

## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/fristenbuch.yaml`

```yaml
- mandat-az: 2026/0042
 mandant: Mueller GmbH
 vorgang: Kundenklage
 fristart: berufungsfrist
 rechtsgrundlage: "§ 517 ZPO"
 fristbeginn: 2026-03-15
 hauptfrist: 2026-04-15
 vorfrist-tage: 7
 vorfrist: 2026-04-06
 zustaendig: RA Mueller
 status: offen
 bemerkung: Berufungsbegründung gemäß § 520 ZPO innerhalb von zwei Monaten
```

## Fristarten und Standardfristen

### Zivilprozess (ZPO)

| Frist | Norm | Dauer |
|---|---|---|
| Klageerwiderung | § 276 ZPO | nach gerichtlicher Setzung (regelmäßig zwei Wochen Notfrist plus zwei Wochen weitere Frist) |
| Berufung | § 517 ZPO | ein Monat ab Zustellung |
| Berufungsbegründung | § 520 ZPO | zwei Monate ab Zustellung |
| Revision | § 548 ZPO | ein Monat |
| Revisionsbegründung | § 551 ZPO | zwei Monate |
| Sofortige Beschwerde | § 569 ZPO | zwei Wochen Notfrist |
| Einspruch Versäumnisurteil | § 339 ZPO | zwei Wochen Notfrist |

### Arbeitsgericht (ArbGG)

| Frist | Norm | Dauer |
|---|---|---|
| Kündigungsschutzklage | § 4 KSchG | drei Wochen Notfrist |
| Berufung | § 66 ArbGG | ein Monat |

### Strafprozess (StPO)

| Frist | Norm | Dauer |
|---|---|---|
| Berufung | § 314 StPO | eine Woche Notfrist |
| Revision | § 341 StPO | eine Woche Notfrist |
| Revisionsbegründung | § 345 StPO | ein Monat |
| Beschwerde | § 311 StPO | eine Woche |

### Verwaltungsgericht (VwGO)

| Frist | Norm | Dauer |
|---|---|---|
| Widerspruchsfrist | § 70 VwGO | ein Monat |
| Klagefrist | § 74 VwGO | ein Monat |
| Berufungsantrag | § 124a VwGO | ein Monat (Zulassungsbeschwerde) |
| Eilrechtsschutz | § 80 Abs. 5 VwGO | keine eigene Antragsfrist |

### Sozialgericht (SGG) — siehe Plugin `fachanwalt-sozialrecht`

### Finanzgericht (FGO) — siehe Plugin `steuerrecht-anwalt-und-berater`

### Familiengericht (FamFG)

| Frist | Norm | Dauer |
|---|---|---|
| Beschwerde | § 63 FamFG | ein Monat |
| Sofortige Beschwerde | § 64 FamFG | zwei Wochen |

## Notfrist vs Beobachtungsfrist

- **Notfristen** (Versäumnis = Verlust): Berufung Revision Kündigungsschutzklage. Vorfrist sieben Werktage.
- **Beobachtungsfristen** (z. B. Vorlauf zur Stellungnahme): Vorfrist drei bis fünf Werktage.

## Vier-Tages-Fiktionen (PostModG, seit 1.1.2025)

Durch das Postrechtsmodernisierungsgesetz (BGBl. 2024 I Nr. 236) wurden alle Bekanntgabe-Fiktionen einheitlich von drei auf vier Tage verlängert:

- **§ 270 ZPO n.F.** Schriftsatzzustellung
- **§ 122 Abs. 2 Nr. 1 AO n.F.** Steuerbescheid (auch § 122 Abs. 2a / § 122a Abs. 4 AO bei elektronischer Übermittlung)
- **§ 41 Abs. 2 VwVfG n.F.** Verwaltungsakt
- **§ 37 Abs. 2 SGB X n.F.** Sozialleistungsbescheid
- **§ 4 Abs. 2 VwZG n.F.** Zustellung gegen Empfangsbekenntnis (Verwaltungszustellung)

Beim Eintragen automatisch berücksichtigen — bei nachweislich früherem Zugang Zugang maßgeblich. Für Verwaltungsakte / Schriftstücke mit Aufgabe zur Post **vor dem 1.1.2025** gilt weiterhin die alte Drei-Tages-Fiktion.

## Vorfristen

- **Standard** fünf Werktage vor Hauptfrist.
- **Notfristen** sieben Werktage.
- **Berufungs-/Revisionsbegründung** zehn Werktage (zwei-Monats-Fristen).

## Workflow

1. **Eintragen** sofort bei Posteingang Bescheid Urteil Zustellung.
2. **Kontrolle** durch Sekretariat **und** zuständigen Anwalt (Vier-Augen-Prinzip).
3. **Vorfrist** loest Eintrag im Tagesbrief aus (Skill `sekretariats-tagesbrief`).
4. **Erledigung** mit Datum und Unterschrift / Initial.
5. **Audit** bei jeder Änderung Eintrag in Audit-Trail.

## Ausgabe

- `fristenbuch.yaml` aktualisiert
- `fristen-uebersicht.md` Tagesbericht nächste sieben und nächste vierzehn Tage
- Vorfristen-Erinnerung in `sekretariats-tagesbrief`
- Audit-Eintrag bei Änderungen

## Haftungshinweis

Das Fristenbuch ist nur so gut wie seine Pflege. Die Letztverantwortung liegt beim Anwalt. Bei Versäumnis Wiedereinsetzung prüfen (jeweilige Verfahrensordnung).
