---
name: anpassen
description: "Kanzlei-Builder-Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows. Normen: technisch/intern. Prüfraster: Anpassungsumfang, Kompatibilitaet, Testbedarf. Output: Anpassungs-Konfigurationsdokument. Abgrenzung: nicht Standardinstallation im Kanzlei Builder Hub."
---

# /anpassen — Kanzleiprofil und Einstellungen anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 51 Mindestversicherung sofort, FAO § 4 Fachanwalt-Antrag 3-Jahres-Frist (10 % Mindestumfang), GwG-Risikoanalyse jährlich, beA Pflichtnutzung seit 01.01.2022.
- Tragende Normen verifizieren: BRAO §§ 5, 7, 14, 27, 43 ff., 49b, 51 (Berufshaftpflicht), BORA, FAO, RVG §§ 1 ff., GwG §§ 2, 10, 11, 43 (Kanzlei als Verpflichteter), DSGVO, beA-Bedingungen, Steuerrecht (EStG, UStG, GewStG) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Kanzleigründer, Kammer, BRAK, Versicherer (Berufshaftpflicht), Mandant, Steuerberater, IT-Dienstleister (beA, RA-MICRO/AnNoText).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Kanzleihandbuch, Datenschutz-Konzept, Geldwäsche-Risikoanalyse, Mandatsvertrag, Honorarvereinbarung, Versicherungspolice, Sozietätsvertrag, beA-Konfiguration — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welcher Abschnitt des Kanzleiprofils soll angepasst werden: Rechtsgebiete, Positivliste, TOM-Dokumentation, Registries oder Update-Einstellungen?
2. Liegt ein konkreter Anlass vor (neue Rechtsgebiet-Erweiterung, Datenschutzaenderung, Teamaenderung)?
3. Ist die bestehende Konfiguration vollstaendig und ohne Platzhalter (sonst Kaltstart-Interview noetig)?
4. Betrifft die Änderung datenschutzrechtlich relevante Konfiguration (TOM, AVV, Verarbeitungsverzeichnis)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 25 DSGVO — Privacy by Design und Default: Konfigurationsaenderungen müssen Datenschutz beruecksichtigen
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag bei Einsatz externer KI-Infrastruktur
- Art. 30 DSGVO — Verarbeitungsverzeichnis: bei jeder Änderung des Verarbeitungsumfangs zu aktualisieren
- Art. 32 DSGVO — Technisch-organisatorische Maßnahmen: TOM-Dokumentation nach jeder relevanten Änderung

## Eingaben

- Angabe, welcher Abschnitt angepasst werden soll:
 - `--profil` — Kanzleityp, Rechtsgebiet(e), Teamgröße, technische Vertrautheit
 - `--positivliste` — Registries, Publisher, Konnektoren, Lizenzen hinzufügen/entfernen
 - `--registries` — Registry-Watchlist erweitern oder kürzen
 - `--updates` — Update-Kadenz und Benachrichtigungseinstellungen
 - `--tom` — TOM-Dokumentation und Datenschutzhinweise
 - Oder frei: "Ich möchte Rechtsanwalt X als neuen Ansprechpartner eintragen"
- Aktuelles Kanzleiprofil: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md`
- Geteiltes Kanzleiprofil: `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-profil.md`

## Ablauf

### Schritt 1: Aktuellen Zustand laden

Konfiguration aus dem Config-Pfad lesen. Wenn die Datei nicht existiert oder noch Platzhalter enthält: den Nutzer auf `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview` hinweisen.

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
- Zuständiger Datenschutzbeauftragter (Name oder "kein DSB bestellt")
- Letztes TOM-Review-Datum

### Schritt 5: Positivliste anpassen (bei --positivliste)

Bei Positivliste-Änderungen:

**Registry hinzufügen:**
1. URL validieren (muss `https://` sein, valider Hostname)
2. Prüfen, ob es sich um ein Kanzlei-Skills-Repository handelt (hat `skills/` oder `.claude-plugin/`)
3. Zur `positivliste.yaml` und zum CLAUDE.md-Watchlist-Abschnitt hinzufügen
4. Sicherheitshinweis: "Hinzugefügte Registries können Skills bereitstellen, die auf Mandantendaten zugreifen. Stellen Sie sicher, dass Sie der Registry vertrauen."

**Publisher hinzufügen:**
1. GitHub-Organisation oder Nutzernamen erfassen
2. Kurze Begründung, warum dieser Publisher vertrauenswürdig ist (zur Dokumentation)
3. Zu `publishers` in `positivliste.yaml` hinzufügen

**Modus-Wechsel (restrictive ↔ permissive):**
- Bei Wechsel nach `restrictive`: Alle vorhandenen installierten Skills sind weiterhin nutzbar, aber neue Installationen erfordern Positivliste-Eintrag.
- Bei Wechsel nach `permissive`: **Explizit auf erhöhtes Risiko hinweisen:**
 > "Permissiver Modus warnt bei unbekannten Quellen, blockiert sie aber nicht. Für Kanzleibetrieb mit Mandantendaten wird `restrictive` empfohlen (Art. 32 DSGVO, Datensicherheit). Bestätigen Sie mit 'ja' um fortzufahren."
- Niemals `permissive` ohne explizite Nutzerbestätigung schreiben.

### Schritt 6: Änderung bestätigen und schreiben

Geänderten Abschnitt vollständig anzeigen und Bestätigung einholen: "Änderung speichern? (ja / nein)"

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

## Beispiele

### Beispiel 1: Neues Rechtsgebiet hinzufügen

```
/kanzlei-builder-hub:kanzlei-builder-hub-anpassen --profil

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
/kanzlei-builder-hub:kanzlei-builder-hub-anpassen --tom

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

- Das vollständige Interview ersetzen. Bei Ersteinrichtung `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview` ausführen.
- Konfigurationsänderungen ohne explizite Genehmigung vornehmen.
- Erste Kanzlei-Grunddaten (Kanzleiname, allgemeine Rechtsgebiete) separat von `kanzlei-profil.md` verwalten — diese immer im geteilten Profil ändern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 32 DSGVO
- § 203 StGB
- Art. 28 DSGVO
- Art. 30 DSGVO
- Art. 35 DSGVO
- § 4 KSchG
- Art. 25 DSGVO
- Art. 17 DSGVO
- § 5 KSchG
- § 29 VwVfG
- § 102 BetrVG
- § 17 MuSchG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
