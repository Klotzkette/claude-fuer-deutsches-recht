---
name: arbeitsrecht-anpassen
description: "Gezielte Anpassung des Arbeitsrechts-Praxisprofils – Standort-Fußabdruck, Risikoeinstellung, Eskalationskontakte, Einstellungsregeln, Kündigungsregeln, Handbuchpositionen oder Untersuchungseinstellungen ändern, ohne das gesamte Kaltstart-Interview neu zu durchlaufen."
---

# /arbeitsrecht:arbeitsrecht-anpassen

## Zweck

Der Nutzer möchte etwas im Praxisprofil ändern – eine Jurisdiktion, eine Risikoeinstellung, einen Eskalationskontakt, eine Handbuchposition – ohne das gesamte Kaltstart-Interview zu wiederholen.

## Eingaben

- Beschreibung der gewünschten Änderung (Freitext oder Abschnittsname)
- Aktuelle Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md`

## Ablauf

### 1. Konfiguration lesen

`~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` und `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` einlesen.

Falls das Plugin noch nicht eingerichtet ist oder `[PLATZHALTER]` enthält:
> Das Plugin wurde noch nicht eingerichtet. Führen Sie `/arbeitsrecht:arbeitsrecht-kaltstart-interview` aus.

### 2. Gewünschte Änderung klären

Wenn die Angabe des Nutzers unklar ist, einen einzigen klärenden Prompt stellen – nicht mehrere Nachfragen hintereinander:

> Was möchten Sie ändern?
> - Neuen Standort / neues Bundesland hinzufügen
> - Tarifvertrag oder Betriebsratssituation aktualisieren
> - Eskalationskontakt ändern
> - Einstellungs- oder Kündigungsregeln anpassen
> - Handbuch-/Betriebsvereinbarungsreferenz aktualisieren
> - Integrationen neu prüfen (`--check-integrations`)
> - Anderes – bitte beschreiben

### 3. Nur den betroffenen Abschnitt aktualisieren

Den relevanten Abschnitt in der Konfigurationsdatei isolieren, die Änderung durchführen, den Rest unberührt lassen. Keine komplette Neugenerierung.

**Besonderheiten:**
- **Neuer Standort / Bundesland:** Eskalationstabelle um das neue Bundesland ergänzen. Auf besondere Landesgesetze hinweisen (z.B. Bayerisches Urlaubsgesetz, abweichendes Landesdatenschutzrecht). KSchG-Schwellenwert neu berechnen.
- **Neuer Tarifvertrag:** Nachwirkung (§ 4 Abs. 5 TVG) und Günstigkeitsprinzip (§ 4 Abs. 3 TVG) berücksichtigen. Ggf. Hinweis auf Allgemeinverbindlichkeit (§ 5 TVG).
- **Betriebsrat neu eingetragen:** § 102 BetrVG-Verpflichtung in Eskalationstabelle aufnehmen; Hinweis auf § 99 BetrVG (Einstellung) und § 87 BetrVG (Mitbestimmung).
- **Eskalationskontakt:** Nur dieses Feld ändern; Risikologik bleibt.

### 4. Änderung schreiben und bestätigen

Die geänderte Konfiguration zurückschreiben und dem Nutzer mitteilen, was geändert wurde (Vorher/Nachher, ein Diff).

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Relevante Normen je nach Änderungsbereich:
- Neues Bundesland: Landesurlaubsgesetze, LDSG des Landes, ggf. Tarifvertrag mit Landesbezug
- Betriebsrat: BetrVG §§ 1, 87, 99, 102, 111 ff.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
Profil-Änderung: [Kürzel der Änderung]
================================================
Geändert:  [Abschnitt in CLAUDE.md]

Vorher:
  [Alt-Wert]

Nachher:
  [Neu-Wert]

Gespeichert: ~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiele

```
/arbeitsrecht:arbeitsrecht-anpassen
Neuen Standort Hamburg hinzufügen, ca. 25 Mitarbeiter, kein Betriebsrat.
```

```
/arbeitsrecht:arbeitsrecht-anpassen
Eskalationskontakt für betriebsbedingte Kündigungen auf Dr. Müller (GC) ändern.
```

```
/arbeitsrecht:arbeitsrecht-anpassen
Wir sind seit Januar diesem Jahr an den Tarifvertrag Einzelhandel NRW gebunden.
```

## Risiken / typische Fehler

- **Landesrecht übersehen.** Bayern, Brandenburg und andere Länder haben eigene Urlaubsgesetze mit abweichenden Mindesturlaubstagen. Bei neuem Bundesland immer Landesspezifika prüfen.
- **Tarifbindung durch Bezugnahmeklausel.** Auch ohne Verbandsmitgliedschaft kann ein Tarifvertrag vertraglich einbezogen sein. Prüfen, ob neue Tarifbindung auch bestehende Verträge erfasst.
- **Betriebsrat-Zuständigkeit.** Bei neuem Betriebsrat: § 102 BetrVG gilt für JEDE Kündigung, § 99 BetrVG für jede Einstellung – sofort in Eskalationstabelle aufnehmen.
