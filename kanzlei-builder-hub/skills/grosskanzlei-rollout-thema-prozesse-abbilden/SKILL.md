---
name: grosskanzlei-rollout-thema-prozesse-abbilden
description: "Grosskanzlei Rollout Thema Prozesse Abbilden: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Grosskanzlei Rollout Thema Prozesse Abbilden

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Grosskanzlei Rollout Thema Prozesse Abbilden** im Plugin Kanzlei-Builder-Hub. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `grosskanzlei-rollout-spezial` | Grosskanzlei-Rollout: Pilotphase, Rollout-Welle, Trainings, Governance, Approval-fuer Skill-Eintraege, Audit-Trail, Datenschutz-Folgenabschaetzung. Mustertexte und Roadmap. |
| `kanzlei-builder-hub-anpassen` | Kanzlei-Builder-Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows. Normen: technisch/intern. Prüfraster: Anpassungsumfang, Kompatibilitaet, Testbedarf. Output: Anpassungs-Konfigurationsdokument. Abgrenzung: nicht Standardinstallation. |
| `kanzlei-prozesse-abbilden` | Typische Kanzlei-Prozesse mit Plugins und Skills abbilden: Mandatsaufnahme, Akteneinsicht, Schriftsatzentwurf, Fristenkontrolle, Rechnung, Archivierung. Pro Prozess: Welche Plugins (Skills) helfen, in welcher Reihenfolge, mit welchem Output? Vorlage zum Anpassen. |

## Arbeitsweg

Im Plugin Kanzlei-Builder-Hub gilt für **Grosskanzlei Rollout Thema Prozesse Abbilden**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `grosskanzlei-rollout-spezial`

**Fokus:** Grosskanzlei-Rollout: Pilotphase, Rollout-Welle, Trainings, Governance, Approval-fuer Skill-Eintraege, Audit-Trail, Datenschutz-Folgenabschaetzung. Mustertexte und Roadmap.

# Grosskanzlei-Rollout

## Spezialwissen: Grosskanzlei-Rollout
- **Spezialgegenstand:** Grosskanzlei-Rollout / grosskanzlei rollout spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `kanzlei-builder-hub-anpassen`

**Fokus:** Kanzlei-Builder-Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows. Normen: technisch/intern. Prüfraster: Anpassungsumfang, Kompatibilitaet, Testbedarf. Output: Anpassungs-Konfigurationsdokument. Abgrenzung: nicht Standardinstallation.

# /anpassen — Kanzleiprofil und Einstellungen anpassen


## Triage zu Beginn
1. Welcher Abschnitt des Kanzleiprofils soll angepasst werden: Rechtsgebiete, Positivliste, TOM-Dokumentation, Registries oder Update-Einstellungen?
2. Liegt ein konkreter Anlass vor (neue Rechtsgebiet-Erweiterung, Datenschutzaenderung, Teamaenderung)?
3. Ist die bestehende Konfiguration vollstaendig und ohne Platzhalter (sonst Kaltstart-Interview noetig)?
4. Betrifft die Aenderung datenschutzrechtlich relevante Konfiguration (TOM, AVV, Verarbeitungsverzeichnis)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 25 DSGVO — Privacy by Design und Default: Konfigurationsaenderungen muessen Datenschutz beruecksichtigen
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag bei Einsatz externer KI-Infrastruktur
- Art. 30 DSGVO — Verarbeitungsverzeichnis: bei jeder Aenderung des Verarbeitungsumfangs zu aktualisieren
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen: TOM-Dokumentation nach jeder relevanten Aenderung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## Ausgabeformat

Pro Änderung:
- Aktueller Wert (vor der Änderung)
- Vorgeschlagener neuer Wert
- Bestätigungsprompt
- Bestätigung der gespeicherten Änderung mit Pfad

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

## 3. `kanzlei-prozesse-abbilden`

**Fokus:** Typische Kanzlei-Prozesse mit Plugins und Skills abbilden: Mandatsaufnahme, Akteneinsicht, Schriftsatzentwurf, Fristenkontrolle, Rechnung, Archivierung. Pro Prozess: Welche Plugins (Skills) helfen, in welcher Reihenfolge, mit welchem Output? Vorlage zum Anpassen.

# Kanzlei-Prozesse abbilden

## Spezialwissen: Kanzlei-Prozesse abbilden
- **Spezialgegenstand:** Kanzlei-Prozesse abbilden / kanzlei prozesse abbilden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
