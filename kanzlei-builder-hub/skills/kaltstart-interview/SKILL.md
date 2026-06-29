---
name: kaltstart-interview
description: "Kaltstart-Interview für den Kanzlei-Builder-Hub: Kanzleiprofil, Rechtsgebiete, gewuenschte Plugins. Normen: technisch/intern. Prüfraster: Rechtsgebietsabdeckung, Mandantenstruktur, Technikvoraussetzungen. Output: Kanzlei-Profil-Konfiguration. Abgrenzung: nicht Plugin-Installation (Folgeschritt)."
---

# /kaltstart-interview — Kanzleiprofil-Interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Triage zu Beginn
1. Handelt es sich um eine Ersteinrichtung oder ein Wiederholungsinterview (--redo oder --check-integrations)?
2. Welche Rechtsform und welcher Kanzleityp liegen vor (Einzelanwalt, PartG, GmbH, Rechtsabteilung)?
3. Sind datenschutzrechtliche Grundlagen (AVV, TOM, Verarbeitungsverzeichnis) für den KI-Einsatz bereits geprueft?
4. Welche technischen Integrationen (beA, E-Mail, DMS, Buchhaltung) sind vorhanden und angebunden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 28 DSGVO — AVV mit KI-Infrastrukturanbieter: Pflicht bei jeder Auftragsverarbeitung
- Art. 35 DSGVO — Datenschutz-Folgenabschaetzung bei hohem Risiko für Mandantendaten
- §§ 43, 43a BRAO — Allgemeine Berufspflichten: gelten ab erstem Mandatstag und erfordern strukturierte Kanzleiorganisation
- § 203 StGB — Verletzung von Privatgeheimnissen: KI-Skills müssen mandatsgeheimnis-konform konfiguriert sein

## Eingaben

- Kanzleityp, Rechtsgebiet(e), Teamgröße, technische Vertrautheit
- Optional: Bestehende Registry-Liste oder Positivliste
- Optional: `--redo` für erneutes vollständiges Interview; `--check-integrations` nur für Integrationsprüfung; `--full` für vollständige Einrichtung

## Ablauf

### Kaltstart-Prüfung

`~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` lesen:
- **Existiert nicht** → Interview starten.
- **Enthält `<!-- EINRICHTUNG PAUSIERT BEI: -->`** → Nutzer begrüßen und Fortsetzung von diesem Abschnitt anbieten.
- **Enthält `[PLATZHALTER]`-Marker aber keinen Pause-Kommentar** → Template nie abgeschlossen; Neustart oder Fortsetzung von den Platzhaltern anbieten.
- **Vollständig ausgefüllt (keine Platzhalter, kein Pause-Kommentar)** → Bereits konfiguriert; überspringen außer bei `--redo`.

### Installationsumfang-Prüfung

Vor der Orientierung: Falls das Arbeitsverzeichnis sich innerhalb eines Projekts befindet (nicht im Home-Verzeichnis), einmalig hinweisen:

> **Achtung — Es sieht aus, als wäre dieses Plugin projektbegrenzt, was bedeutet, dass nur Dateien in [aktuellem Verzeichnis] gelesen werden können. Für Mandatsdokumente aus anderen Ordnern benutzerbegrenzt installieren. Sie können mit der Projektbegrenzung fortfahren, müssen aber Dateien in diesen Ordner verschieben.**

### Kanzleiprofil prüfen

Prüfen ob `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-profil.md` existiert:
- **Existiert:** Lesen. Einzeilige Bestätigung anzeigen: "Sie sind [Name], [Kanzleityp], [Rechtsgebiete]. Richtig? (Oder sagen Sie 'aktualisieren' um das geteilte Profil zu ändern.)" Bei Bestätigung Kanzlei-Fragen überspringen.
- **Existiert nicht:** Kanzlei-Fragen stellen und in geteiltes Profil schreiben.

### Einstiegstext anzeigen

> **`kanzlei-builder-hub` dient der Entdeckung, Installation und Verwaltung von Community-Kanzlei-Skills.** Suchen Sie einen Praxisbereich-Ablauf? Installieren Sie eines der `kanzlei-*`-Plugins direkt; führen Sie `/kanzlei-builder-hub:verzeichnis-durchsuchen` aus, um zu sehen, was verfügbar ist.
>
> **2 Minuten** ergibt Rolle und Praxisbereich(e) — plus sinnvolle Standardwerte für Registry-Watchlist, Update-Kadenz und eine standardmäßig zulässige Positivliste. **15 Minuten** fügt ein kalibriertes Starter-Paket passend zu Ihrer Kanzlei hinzu, eine in `positivliste.yaml` geschriebene Vertrauensquellen-Richtlinie, Update-Benachrichtigungseinstellungen und Ihre Rechtsgebiets-/Teamgrößeninformation für Empfehlungen.
>
> Schnell oder vollständig? (Jederzeit hochstufen mit `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview --full`.)

### Part 0: Wer nutzt dies, und was ist verbunden

#### Wer nutzt dies?

> Wer wird dieses Plugin täglich nutzen?
>
> 1. **Rechtsanwalt/Rechtsanwältin oder juristisches Fachpersonal** — Rechtsanwalt, Paralegal, Legal Ops unter anwaltlicher Aufsicht.
> 2. **Nicht-Jurist mit Anwaltszugang** — Geschäftsführer, Vertragsmanager, HR, Einkauf; Sie haben einen Anwalt, den Sie konsultieren können.
> 3. **Nicht-Jurist ohne regelmäßigen Anwaltszugang** — Sie bearbeiten dies selbst.

Bei Antwort 3 hinzufügen:
> Falls Sie einen Rechtsanwalt finden möchten: Die zuständige Rechtsanwaltskammer (RAK) oder die Bundesrechtsanwaltskammer (BRAK) bieten Vermittlungsdienste. Viele Anwälte bieten Erstberatungen zu moderaten Kosten an. Rechtsberatungsstellen (z. B. Caritas, VdK) und Verbraucherzentralen helfen bei Standardproblemen.

#### Was ist verbunden?

Prüfen, welche Konnektoren tatsächlich verbunden sind (nicht nur konfiguriert):
- Nur ✓ melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war.
- ⚪ melden für konfiguriert-aber-ungeprüfte Konnektoren.
- Niemals ✓ nur aufgrund von `.mcp.json`-Einträgen melden.

### Die fünf Fragen

1. **Kanzleityp/Tätigkeitsschwerpunkt** — Kanzlei oder Rechtsabteilung? Zivil, Straf, Verwaltung, Handels-/Gesellschaftsrecht, Arbeitsrecht, Datenschutz, IP, M&A, anderes?

2. **Rechtsgebiet(e)** — Welche Rechtsgebiete sind im Fokus? (Beeinflusst Registry-Suche und Starter-Paket-Filterung.)

3. **Teamgröße** — Solo, kleines Team (2–5), große Rechtsabteilung? (Beeinflusst `positivliste.yaml`-Modus-Standard — Solo/klein erhält `permissive`, Mittel/groß/Rechtsabteilung erhält `restrictive`.)

4. **Was machen Sie am häufigsten?** — Vertragsgestaltung und -prüfung, Schriftsatzerstellung, Compliance, M&A Due Diligence, Mandatsbegleitung, Briefe? (Beeinflusst `verwandte-skills-vorschlag`.)

5. **Technische Vertrautheit** — Entwickler (Sie bauen eigene Skills), Anpasser (Sie bearbeiten installierte), Nutzer (Sie wollen, dass es funktioniert)? (Beeinflusst Empfehlungstiefe.)

### TOM-Hinweis im Interview

Nach den fünf Fragen und vor der Starter-Paket-Empfehlung:

> **Hinweis für den Kanzleibetrieb:** Vor dem Einsatz von KI-Skills in der Kanzlei ist zu prüfen, ob Technisch-Organisatorische Maßnahmen (TOM) nach Art. 25 und 32 DSGVO erforderlich sind. Dies betrifft insbesondere:
> - Verschlüsselung übertragener und gespeicherter Mandantendaten
> - Zugriffskontrolle und Berechtigungskonzept für KI-Tools
> - Dokumentation in der Verfahrensübersicht nach Art. 30 DSGVO
> - Ggf. Datenschutz-Folgenabschätzung nach Art. 35 DSGVO bei hohem Risiko
>
> Diese Einrichtung legt Ihren Kanzleityp fest — die konkrete TOM-Prüfung pro Skill erfolgt beim Install über `/kanzlei-builder-hub:skill-installierer`.

### Empfehlung

Profil auf Registry-Skills abbilden:

| Profil | Starter-Paket |
|---|---|
| Kanzlei Zivilrecht/Vertragsrecht | kanzlei-vertragsrecht + lpm-skills (Mandatsplanung, Fristenverwaltung) |
| Datenschutzrecht / Datenschutzbeauftragter | kanzlei-datenschutz + Community-DSE/AV-Vertrag-Skills |
| Arbeitsrecht | kanzlei-arbeitsrecht + Fristen-Tracker-Skills |
| M&A / Gesellschaftsrecht | kanzlei-gesellschaftsrecht + Community-Due-Diligence-Skills |
| Solo / kleines Team | Alles Leichtgewichtige — Triage-Skills vor vollständigen Review-Skills |
| Entwickler | Rohe Registries und das skills-qualitätsprüfung-Framework |

Für jeden empfohlenen Skill: SKILL.md-Beschreibung anzeigen. Nutzer wählt — nichts ohne Ja installieren.

### Deployment-Kontext für Positivliste

> "Wie werden Sie die installierten Skills einsetzen — nur für sich selbst, geteilt in der Kanzlei oder eingebettet in ein Produkt oder eine Dienstleistung, die Sie an Mandanten liefern? (Persönlich / Kanzlei-intern / Produkteinbettung.) Dies beeinflusst die Lizenz-Standardwerte der Positivliste."

Für **Kanzlei-intern** zusätzlich fragen: "Liegt eine Auftragsverarbeitungsvereinbarung (Art. 28 DSGVO) mit dem Anbieter der genutzten KI-Infrastruktur vor?"

### Positivliste schreiben

Nach der Deployment-Kontext-Frage `positivliste.yaml` gemäß Schema in `skill-installierer/references/positivliste.md` schreiben. Lizenzen je nach Kontext:
- **Persönlich** → MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, CC0-1.0
- **Kanzlei-intern** → wie Persönlich plus LGPL-2.1-only, LGPL-3.0-only, MPL-2.0
- **Produkteinbettung** → wie Persönlich; starkes Copyleft (GPL, AGPL) als Kommentar markieren

### Praxisprofil schreiben

Kurz: Profil + installierte Liste + Registry-Präferenzen. Gemäß Template in `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`. Config-Pfad erstellen bei Bedarf.

### Nach dem Schreiben

> **Was möchten Sie als nächstes tun?**
>
> - **Community-Skills durchsuchen** — Sehen Sie, was andere Kanzleien und Rechtsabteilungen gebaut haben. Ausprobieren: `/kanzlei-builder-hub:verzeichnis-durchsuchen`
> - **Einen Skill aus einer Registry installieren** — Einen Community-Skill zur Umgebung hinzufügen — lizenz- und positivliste-geprüft vor der Ausführung. Ausprobieren: `/kanzlei-builder-hub:skill-installierer`
> - **Updates prüfen** — Sehen, welche installierten Skills neuere Versionen in ihrer Quell-Registry haben. Ausprobieren: `/kanzlei-builder-hub:automatischer-aktualisierer`
> - **Skill-Empfehlungen erhalten** — Basierend auf aktueller Tätigkeit relevante Skills empfehlen. Ausprobieren: `/kanzlei-builder-hub:verwandte-skills-vorschlag`
> - **Einen Skill gegen das Framework prüfen** — Skills-QA durchführen. Ausprobieren: `/kanzlei-builder-hub:skills-qualitätsprüfung`

Abschließen mit:
> Fertig. Ihre Konfiguration liegt unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` — eine Klartextdatei, die Sie direkt lesen und bearbeiten können. Alles kann geändert werden:
>
> - Datei direkt bearbeiten für schnelle Änderungen
> - `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview --redo` für vollständiges Wiederholungsinterview
> - `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview --check-integrations` um Verbindungen erneut zu prüfen

## Quellen und Zitierweise

Einschlägige Normen für Datenschutz im Kanzleibetrieb:
- Art. 25, 28, 30, 32, 35 DSGVO
- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht)
- § 203 StGB (Verletzung von Privatgeheimnissen)
- §§ 2 ff. BORA (Grundpflichten)

Zitierweise nach `../references/zitierweise.md`.

## Beispiel

```
Kanzleiprofil erstellt am 2025-01-15:
- Typ: Einzelkanzlei, Schwerpunkt Arbeitsrecht
- Team: Solo
- Rechtsgebiet: Arbeitsrecht, Kündigungsschutz, Betriebsverfassungsrecht
- Eingesetztes Starter-Paket:
 - kanzlei-arbeitsrecht (installiert)
 - kündigungsfristen-tracker (installiert)
- Beobachtete Registries: kanzlei-skills
- TOM-Hinweis: Bitte Verfahrensübersicht nach Art. 30 DSGVO aktualisieren.
```

## Risiken / typische Fehler

- **Platzhalter im Profil:** Nie mit stillen Lücken schreiben — jeder Platzhalter ist ein bewusst bestätigtes Auslassen.
- **Falsche Deployment-Kontext-Angabe:** Kanzlei-intern erfordert AVV mit KI-Infrastrukturanbieter (Art. 28 DSGVO).
- **TOM-Vergessen:** KI-Skills in der Kanzlei erfordern TOM-Prüfung vor dem Einsatz — dieser Schritt darf nicht übersprungen werden.
- **Praxisprofil zu generisch:** Ein generisches Profil ergibt generische Empfehlungen.
