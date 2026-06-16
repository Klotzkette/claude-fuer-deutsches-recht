---
name: produktmandat-workspace-kontexttrennung
description: "Verwaltung von Produktmandats-Workspaces — Anlegen, Auflisten, Wechseln, Schließen oder Deaktivieren (auf Kanzleiebene). Lädt, wenn der Nutzer ein neues Mandat anlegen, zwischen Mandaten wechseln, ein Mandat abschließen oder den mandatsbezogenen Kontext trennen möchte, insbesondere bei mehreren parallelen Produktrechtsmandaten."
---

# Produktmandat-Workspace und Kontexttrennung

## Zweck

Anwälte und In-house-Juristen arbeiten gleichzeitig an mehreren Produkten, Mandaten und Vorgängen. Der Kontext eines Mandats darf nicht in ein anderes überlaufen — sowohl aus Mandatsgeheimnisgründen (§ 43a Abs. 2 BRAO, § 203 StGB) als auch zur sachlichen Trennung der Produktrechtsanalysen. Diese Skill ist die schlanke Dateiverwaltungsebene, die diese Trennung sicherstellt.

**Standardmäßig deaktiviert.** In-house-Juristen mit einem einzigen Unternehmenskontext benötigen diese Skill nicht — sie arbeiten ausschließlich auf Kanzlei-/Unternehmensebene. Mandats-Workspaces aktivieren sich beim Ersteinrichtungsinterview für externe Kanzleien (Einzel-, kleine und große Kanzleien) oder durch Bearbeitung von `## Gesellschaftsrechtlicher Mandatsworkspace und Kontexttrennungs` in der Kanzlei-CLAUDE.md. Wenn `Aktiviert` auf `✗` steht, erklärt der `/mandat-workspace`-Befehl den deaktivierten Zustand und empfiehlt `/kaltstart-interview --redo` für Nutzer, die tatsächlich Mandatsisolierung benötigen.

Die Skill lädt, wenn der Nutzer Mandate anlegen, wechseln, auflisten, schließen oder den Mandatskontext deaktivieren möchte.

## Eingaben

- **Unterbefehl:** `neu`, `liste`, `wechsel`, `schließen` oder `keine` — gefolgt von einem Slug, wo erforderlich
- **Slug:** Kleinbuchstaben mit Bindestrichen (z. B. `mustermann-gmbh-launch-2026`, `klindt-prüfung-q3`)
- **Für `neu`:** Mandantendaten aus dem Aufnahmeinterview (siehe Ablauf, Schritt 2)

**Unterbefehle im Überblick:**
- `/produktrecht:produktrecht-mandat-arbeitsbereich neu <slug>` — neuen Mandat-Workspace anlegen, Kurzinterview durchführen, `mandat.md` schreiben
- `/produktrecht:produktrecht-mandat-arbeitsbereich liste` — Mandate mit Status und aktivem Mandat auflisten
- `/produktrecht:produktrecht-mandat-arbeitsbereich wechsel <slug>` — aktives Mandat setzen
- `/produktrecht:produktrecht-mandat-arbeitsbereich schließen <slug>` — Mandat archivieren (nie löschen)
- `/produktrecht:produktrecht-mandat-arbeitsbereich keine` — Mandatskontext deaktivieren, nur auf Kanzleiebene arbeiten

## Rechtlicher Rahmen

### Mandatsgeheimnis und berufsrechtliche Grundlagen

- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht des Rechtsanwalts als Kernpflicht des Berufsrechts; gilt für alle Mandatsinformationen ohne zeitliche Begrenzung
- § 2 BORA: Konkretisierung der Verschwiegenheitspflicht, Pflicht zur Einweisung von Mitarbeitern
- § 203 StGB: Verletzung von Privatgeheimnissen — strafrechtliche Sanktion bei unbefugter Weitergabe von Mandatsinformationen
- § 43a Abs. 4 BRAO: Interessenkollisionsverbot — Mandat-Workspace-Trennung unterstützt die Konfliktprüfung, ersetzt sie jedoch nicht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Aufbewahrungspflichten

- § 50 BRAO: Aufbewahrungspflicht für Handakten — grundsätzlich 5 Jahre ab Ende des Mandats; Archivierung ist keine Löschung
- §§ 257 HGB, 147 AO: Allgemeine Aufbewahrungsfristen für kaufmännische und steuerliche Unterlagen (6–10 Jahre)

## Ablauf

### Schritt 0: Aktivierungsstatus prüfen

`CLAUDE.md` der Kanzlei lesen und `## Mandats-Workspaces` prüfen.

- Wenn `Aktiviert: ✗` → dem Nutzer mitteilen: "Mandats-Workspaces sind deaktiviert — Sie sind als In-house-Praxis mit einem einzigen Mandanten konfiguriert; das Plugin arbeitet automatisch auf Basis des Kanzleikontexts. Wenn Sie tatsächlich mandantenübergreifend tätig sind, führen Sie `/produktrecht:produktrecht-kaltstart-interview --redo` durch und wählen eine externe Kanzlei-Einstellung. Andernfalls benötigen Sie `/mandat-workspace` nicht."
- Wenn `Aktiviert: ✓` → weiter mit dem angegebenen Unterbefehl.

### Schritt 1: Unterbefehl erkennen und ausführen

Auf das erste Argument (Unterbefehl) reagieren:
- `neu` → Aufnahmeinterview durchführen, `mandat.md` anlegen
- `liste` → alle `mandate/*/mandat.md` aufzählen und Tabelle ausgeben
- `wechsel` → aktives Mandat in der CLAUDE.md aktualisieren
- `schließen` → Mandat in `_archiviert/` verschieben
- `keine` → `Aktives Mandat:` auf `keine — nur Kanzleikontext` setzen

### Schritt 2: Aufnahmeinterview (nur bei `neu`)

1. Prüfen, ob der Slug nicht bereits in `mandate/<slug>/` oder `mandate/_archiviert/<slug>/` vorhanden ist. Bei Wiederverwendung anderen Slug wählen lassen.
2. Interview durchführen:
   - **Mandant** (vertretene Partei oder interner Unternehmensbereich bei In-house)
   - **Gegenseite / Beteiligte** (andere Partei — können mehrere sein)
   - **Mandatstyp** (aus dem Kanzleiprofil; für Produktrecht: Produkt-Launch | Feature-Review | Marketingaussagen-Prüfung | Risikoanalyse | Produktbereich dauerhaft | Sonstiges)
   - **Vertraulichkeitsstufe** (standard | erhöht | Clean-Team — erhöhte Stufe erfordert besondere Vorsicht bei mandatsübergreifenden Einstellungen)
   - **Kernsachverhalt** (2–5 Sätze: Worum geht es? Wer sind die Beteiligten? Was steht auf dem Spiel?)
   - **Mandatsspezifische Abweichungen** vom Standardprozess (z. B. "Mandant besteht auf 24 Monaten Haftungsbeschränkung statt 12", "Ton: partnerschaftlich — Gegenseite ist strategischer Partner")
   - **Zusammenhängende Mandate** (Slugs verbundener Vorgänge)
3. `mandate/<slug>/mandat.md` mit der unten beschriebenen Vorlage anlegen.
4. `mandate/<slug>/verlauf.md` mit einem "Eröffnet"-Eintrag anlegen.
5. Leere `mandate/<slug>/notizen.md` anlegen.
6. **Nicht automatisch wechseln.** Fragen: "Möchten Sie jetzt zu `<slug>` wechseln? (`/produktrecht:produktrecht-mandat-arbeitsbereich wechsel <slug>`)"

### Schritt 3: Liste ausgeben (nur bei `liste`)

Alle `mandate/*/mandat.md` einlesen. Kurze Titelzeile und Statusfelder extrahieren. Tabelle ausgeben:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. Archivierte Mandate unter einer separaten Überschrift "Archiviert" aufführen.

### Schritt 4: Mandat wechseln (nur bei `wechsel`)

1. Prüfen, ob `mandate/<slug>/mandat.md` existiert. Falls nicht, `/produktrecht:produktrecht-mandat-arbeitsbereich neu <slug>` vorschlagen.
2. Die Zeile `Aktives Mandat:` in der Kanzlei-CLAUDE.md auf `Aktives Mandat: <slug>` aktualisieren.
3. Zusammenfassung aus `mandat.md` anzeigen, damit der Nutzer das richtige Mandat bestätigen kann.

### Schritt 5: Mandat schließen (nur bei `schließen`)

1. Prüfen, ob `mandate/<slug>/` existiert.
2. Einen "Geschlossen"-Eintrag mit dem heutigen Datum an `mandate/<slug>/verlauf.md` anhängen.
3. `mandate/<slug>/` nach `mandate/_archiviert/<slug>/` verschieben (§ 50 BRAO: Aufbewahrungspflicht beachten — nie löschen).
4. Wenn das geschlossene Mandat das aktive Mandat war: `Aktives Mandat:` auf `keine — nur Kanzleikontext` setzen.

### Schritt 6: Mandatskontext deaktivieren (nur bei `keine`)

`Aktives Mandat:` in der Kanzlei-CLAUDE.md auf `keine — nur Kanzleikontext` setzen. Dem Nutzer bestätigen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** §§ 611-630 BGB (Dienstvertrag, Mandatsrecht) — §§ 1-4 ProdHaftG — §§ 3, 3a UWG

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

### `mandat.md`-Vorlage

```markdown
# Mandat: [Mandant] — [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / Clean-Team]

---

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Parteien

**Mandant:** [Name]
**Gegenseite / Beteiligte:** [Name(n)]

## Mandatstyp

[Produkt-Launch | Feature-Review | Marketingaussagen-Prüfung | Risikoanalyse | Produktbereich dauerhaft | Sonstiges — mit einzeiliger Begründung]

## Kernsachverhalt

[2–5 Sätze. Worum geht es? Wer sind die Beteiligten? Was steht auf dem Spiel? Was unterscheidet dieses Mandat vom Standardfall?]

## Mandatsspezifische Abweichungen

*Jede Abweichung vom kanzleiweiten Standard, die nur für dieses Mandat gilt.*

- [z. B. "Haftungsbeschränkung: Mandant besteht auf 24 Monaten statt Kanzleistandard 12 Monate."]
- [z. B. "Ton: partnerschaftlich — Gegenseite ist strategischer Partner."]
- [z. B. "Rechtsstand: österreichisches Recht statt deutschem."]

## Zusammenhängende Mandate

- [Slug — einzeilige Begründung der Verbindung]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf Mandatsdateien einsehen? Ist mandatsübergreifender Kontext auch bei globaler Aktivierung zulässig?]
```

### `verlauf.md`-Starteintrag

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Anhängendes Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Anfangskontext, der über mandat.md hinausgeht — z. B. "Eröffnet auf Basis des eingehenden PRD-Entwurfs von [Gegenseite]."]
```

## Beispiel

**Sachverhalt:** Kanzlei betreut drei Produktrechtsmandate gleichzeitig: Hersteller A (Maschinenlauf-Review), Hersteller B (Health-Claims-Prüfung Nahrungsergänzung), Unternehmen C (dauerhafter Produktrechtsberater).

```
/produktrecht:produktrecht-mandat-arbeitsbereich neu hersteller-a-maschinen-2026
/produktrecht:produktrecht-mandat-arbeitsbereich neu hersteller-b-health-claims
/produktrecht:produktrecht-mandat-arbeitsbereich neu unternehmen-c-dauerberatung
/produktrecht:produktrecht-mandat-arbeitsbereich liste
/produktrecht:produktrecht-mandat-arbeitsbereich wechsel hersteller-a-maschinen-2026
```

Nach dem Wechsel zu `hersteller-a-maschinen-2026` liest jede Skill ausschließlich die `mandat.md` dieses Mandats und schreibt Ausgaben in den zugehörigen Ordner. Kontextüberlauf auf `hersteller-b-health-claims` ist ausgeschlossen.

## Risiken und typische Fehler

- **Mandatskontext-Überlauf:** Werden Prüfvermerke für Mandant A mit Informationen aus Mandat B angereichert, liegt ein potenziellerVerstoß gegen § 43a Abs. 2 BRAO und § 203 StGB vor. Der Cross-Mandats-Kontext-Flag darf nur auf explizite Nutzeranfrage aktiviert werden.
- **Slug-Wiederverwendung:** Ein neuer Slug `acme-launch` nach Archivierung von `_archiviert/acme-launch` erzeugt Verwirrung über welche Version aktiv ist. Die Skill prüft beide Pfade.
- **Zu frühe Mandatsschließung:** Fristen nach § 50 BRAO (5 Jahre) dürfen nicht durch frühzeitiges Schließen ausgehebelt werden. Schließen archiviert; es löscht nie.
- **Vergessener Mandatswechsel:** Wenn nach der Arbeit an Mandat A kein expliziter Wechsel erfolgt, arbeitet die nächste Skill weiter im Kontext von Mandat A. Regelmäßig `/mandat-workspace liste` aufrufen, um zu prüfen, welches Mandat aktiv ist.
- **Keine automatische Interessenkonfliktprüfung:** Diese Skill kann keine Interessenkonflikte i. S. d. § 43a Abs. 4 BRAO feststellen. Das ist Aufgabe des Anwalts. Das Aufnahmeinterview erfasst, was der Nutzer erklärt — nicht was wirklich zutrifft.
- **Clean-Team-Mandate:** Bei Clean-Team-Vertraulichkeit ist mandatsübergreifender Kontext auch bei globalem `Ein` nicht zulässig. Explizit in der `mandat.md` unter Vertraulichkeitshinweise vermerken.

## Quellenpflicht

- **Berufsrecht:** BRAO-Volltext (gesetze-im-internet.de), BORA, FAO
- **Aufbewahrung:** § 50 BRAO, ggf. §§ 257 HGB, 147 AO
- **Rechtsprechung:** amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang — BGH-Entscheidungen zum Mandatsgeheimnis und Interessenkonflikt in der Form `BGH, Urt. v. TT.MM.JJJJ – Az., Fundstelle Rn. X`

Quellen, die nur aus Modellwissen stammen, nicht als zitierfähige Fundstelle ausgeben. Pinpoint-Zitate nur verwenden, wenn Randnummer, Seite oder amtlicher Leitsatz aus der konkreten Quelle geprüft wurde.

Hinweis: Dieser Skill hält Produktmandate sauber getrennt und stärkt damit die anwaltliche Arbeitsorganisation; Interessenkonflikte bewertet weiterhin der verantwortliche Rechtsanwalt.


<!-- AUDIT 27.05.2026 bundle_040
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
