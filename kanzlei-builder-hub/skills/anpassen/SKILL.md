---
name: anpassen
description: "Kanzleiprofil, Positivliste, Registry-Watchlist und Aktualisierungseinstellungen anpassen. Einsetzen, wenn der Nutzer einzelne Profil-Abschnitte ändern möchte, neue Registries hinzufügen, Positivliste-Einträge aktualisieren oder die Update-Benachrichtigungseinstellungen ändern möchte — ohne das vollständige kaltstart-interview zu wiederholen."
---

# /anpassen — Kanzleiprofil und Einstellungen anpassen

## Zweck

Dieser Skill ermöglicht die gezielte Anpassung einzelner Abschnitte des Kanzleiprofils und der Hub-Einstellungen, ohne das vollständige Kaltstart-Interview zu wiederholen. Verwenden Sie ihn, wenn sich Ihre Kanzlei, Rechtsgebiete, Teamzusammensetzung oder Sicherheitseinstellungen geändert haben.

**Änderungshistorie:** Jede Änderung wird mit Zeitstempel protokolliert, damit nachvollziehbar bleibt, was wann und aus welchem Grund geändert wurde.

## Eingaben

- Angabe, welcher Abschnitt angepasst werden soll:
  - `--profil` — Kanzleityp, Rechtsgebiet(e), Teamgröße, technische Vertrautheit
  - `--positivliste` — Registries, Publisher, Konnektoren, Lizenzen hinzufügen/entfernen
  - `--registries` — Registry-Watchlist erweitern oder kürzen
  - `--updates` — Update-Kadenz und Benachrichtigungseinstellungen
  - `--tom` — TOM-Dokumentation und Datenschutzhinweise
  - Oder frei: „Ich möchte Rechtsanwalt X als neuen Ansprechpartner eintragen"
- Aktuelles Kanzleiprofil: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md`
- Geteiltes Kanzleiprofil: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-profil.md`

## Ablauf

### Schritt 1: Aktuellen Zustand laden

Konfiguration aus dem Config-Pfad lesen. Wenn die Datei nicht existiert oder noch Platzhalter enthält: den Nutzer auf `/kanzlei-builder-hub:kaltstart-interview` hinweisen.

### Schritt 2: Änderungsbereich bestimmen

Den gewünschten Änderungsbereich aus dem Argument oder der Nutzeranfrage ableiten. Bei Unklarheit: kurz nachfragen (maximal eine Rückfrage).

### Schritt 3: Aktuellen Wert anzeigen

Vor jeder Änderung den aktuellen Wert des zu ändernden Abschnitts anzeigen:

```
Aktueller Wert:
  Kanzleityp: Einzelkanzlei, Schwerpunkt Arbeitsrecht

Neuer Wert (bitte eingeben oder bestätigen):
```

### Schritt 4: Neuen Wert erfassen

Neuen Wert vom Nutzer einholen. Wenn der Nutzer einen Wert eingibt, der potenziell fachlich unrichtig ist (z. B. eine falsche Gesetzesnummer), kurz darauf hinweisen.

**TOM-Anpassung (--tom):** Wenn dieser Abschnitt gewählt wird, folgende Felder anbieten:
- Verarbeitungsverzeichnis-Eintrag nach Art. 30 DSGVO vorhanden (ja/nein/in Bearbeitung)
- Datenschutz-Folgenabschätzung nach Art. 35 DSGVO durchgeführt (ja/nein/nicht erforderlich)
- AVV nach Art. 28 DSGVO mit KI-Infrastrukturanbieter geschlossen (ja/nein/in Verhandlung)
- Zuständiger Datenschutzbeauftragter (Name oder „kein DSB bestellt")
- Letztes TOM-Review-Datum

### Schritt 5: Positivliste anpassen (bei --positivliste)

Bei Positivliste-Änderungen:

**Registry hinzufügen:**
1. URL validieren (muss `https://` sein, valider Hostname)
2. Prüfen, ob es sich um ein Kanzlei-Skills-Repository handelt (hat `skills/` oder `.claude-plugin/`)
3. Zur `positivliste.yaml` und zum CLAUDE.md-Watchlist-Abschnitt hinzufügen
4. Sicherheitshinweis: „Hinzugefügte Registries können Skills bereitstellen, die auf Mandantendaten zugreifen. Stellen Sie sicher, dass Sie der Registry vertrauen."

**Publisher hinzufügen:**
1. GitHub-Organisation oder Nutzernamen erfassen
2. Kurze Begründung, warum dieser Publisher vertrauenswürdig ist (zur Dokumentation)
3. Zu `publishers` in `positivliste.yaml` hinzufügen

**Modus-Wechsel (restrictive ↔ permissive):**
- Bei Wechsel nach `restrictive`: Alle vorhandenen installierten Skills sind weiterhin nutzbar, aber neue Installationen erfordern Positivliste-Eintrag.
- Bei Wechsel nach `permissive`: **Explizit auf erhöhtes Risiko hinweisen:**
  > „Permissiver Modus warnt bei unbekannten Quellen, blockiert sie aber nicht. Für Kanzleibetrieb mit Mandantendaten wird `restrictive` empfohlen (Art. 32 DSGVO, Datensicherheit). Bestätigen Sie mit 'ja' um fortzufahren."
- Niemals `permissive` ohne explizite Nutzerbestätigung schreiben.

### Schritt 6: Änderung bestätigen und schreiben

Geänderten Abschnitt vollständig anzeigen und Bestätigung einholen: „Änderung speichern? (ja / nein)"

Nur nach explizitem `ja` schreiben.

### Schritt 7: Protokollieren

Änderung in `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/customization-log.md` protokollieren:

```
[YYYY-MM-DD HH:MM] Abschnitt: [Name] | Geändert durch: [Nutzer] | Grund: [optional]
Alter Wert: [...]
Neuer Wert: [...]
```

## Quellen und Zitierweise

Einschlägige Normen bei Profil-/TOM-Änderungen:
- Art. 25 DSGVO (Privacy by Design und Default)
- Art. 28 DSGVO (Auftragsverarbeitung bei Drittanbietern)
- Art. 30 DSGVO (Verarbeitungsverzeichnis)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 35 DSGVO (Datenschutz-Folgenabschätzung)

Zitierweise nach `../references/zitierweise.md`.

## Ausgabeformat

Pro Änderung:
- Aktueller Wert (vor der Änderung)
- Vorgeschlagener neuer Wert
- Bestätigungsprompt
- Bestätigung der gespeicherten Änderung mit Pfad

## Beispiele

### Beispiel 1: Neues Rechtsgebiet hinzufügen

```
/kanzlei-builder-hub:anpassen --profil

Aktueller Wert:
  Rechtsgebiet(e): Arbeitsrecht

Neues Rechtsgebiet hinzufügen: Datenschutzrecht

Neuer Wert:
  Rechtsgebiet(e): Arbeitsrecht, Datenschutzrecht

Änderung speichern? (ja / nein): ja

✅ Gespeichert. Der verwandte-skills-vorschlag wird ab sofort auch Datenschutz-Skills berücksichtigen.
```

### Beispiel 2: TOM-Status aktualisieren

```
/kanzlei-builder-hub:anpassen --tom

TOM-Status aktualisieren:
- Verarbeitungsverzeichnis (Art. 30 DSGVO): in Bearbeitung → vorhanden
- AVV mit KI-Infrastrukturanbieter (Art. 28 DSGVO): nein → ja (Vertrag vom 2025-01-10)
- Letztes TOM-Review: 2025-01-15

Änderung speichern? (ja / nein): ja
✅ TOM-Status aktualisiert und protokolliert.
```

## Risiken / typische Fehler

- **Positivliste-Modus-Wechsel ohne Überlegung:** Permissiver Modus ist bequemer, aber weniger sicher. Für Kanzleibetrieb mit Mandantendaten `restrictive` bevorzugen.
- **Geteiltes Profil vs. Hub-Profil:** Kanzlei-übergreifende Fakten (Name, Standort, Rechtsgebiete) gehören in `kanzlei-profil.md`; Hub-spezifische Einstellungen in die Hub-CLAUDE.md.
- **TOM-Dokumentation vergessen:** Jede Änderung, die neue KI-Verarbeitung von Mandantendaten ermöglicht, erfordert eine Aktualisierung der TOM-Dokumentation.
- **Registry ohne Prüfung hinzufügen:** Jede neue Registry kann potenziell schädliche Skills enthalten. Vertrauenswürdigkeit vor dem Hinzufügen prüfen.

## Was dieser Skill nicht tut

- Das vollständige Interview ersetzen. Bei Ersteinrichtung `/kanzlei-builder-hub:kaltstart-interview` ausführen.
- Konfigurationsänderungen ohne explizite Genehmigung vornehmen.
- Erste Kanzlei-Grunddaten (Kanzleiname, allgemeine Rechtsgebiete) separat von `kanzlei-profil.md` verwalten — diese immer im geteilten Profil ändern.
