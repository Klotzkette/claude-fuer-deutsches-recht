---
name: kaltstart-interview
description: "Kanzlei oder Unternehmen richtet das gewerbliche-Rechtsschutz-Plugin zum ersten Mal ein und muss Profil und Strategie hinterlegen. Ersteinrichtung Gewerblicher Rechtsschutz. Prüfraster: Kanzleiprofil Schutzrechtsportfolio Durchsetzungsstrategie Genehmigungsmatrix. Output: CLAUDE.md Kanzleiprofil als Grundlage für alle anderen Skills. Abgrenzung zu gewerblicher-rechtsschutz-anpassen (Nachbearbeitung) und mandat-triage-gewerblicher-rechtsschutz."
---

# Ersteinrichtungsinterview

## Zweck

Das Ersteinrichtungsinterview sammelt die kanzleispezifischen Informationen, die alle anderen Skills benötigen: Rechtsgebiets-Mix, Jurisdiktion, Schutzrechtsportfolio, Durchsetzungsstrategie und Genehmigungsmatrix. Ohne dieses Interview liefern alle anderen Skills generische Ergebnisse, die möglicherweise nicht mit der Kanzleipraxis übereinstimmen.

Das Interview schreibt das Kanzleiprofil in:
`~/.claude/plugins/config/claude-fuer-deutsches-recht/gewerblicher-rechtsschutz/CLAUDE.md`

Dieser Pfad überlebt Plugin-Updates.

## Eingaben

Keine Pflicht-Eingaben vor dem Start. Das Interview fragt nacheinander ab.

## Ablauf

### Phase 1: Gemeinsames Kanzleiprofil (5 Minuten)

Falls `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` nicht existiert oder Platzhalter enthält, zunächst diese fünf Fragen stellen:

1. **Vollständiger Name** der Kanzlei / des Unternehmens (vollständige Firma)
2. **Rechtsform und Größe** (Einzelkanzlei, Partnerschaft mbB, GmbH & Co. KG, Inhouse-Rechtsabteilung; Anzahl Anwälte/Mitarbeiter)
3. **Primäre Jurisdiktion** (Deutschland, EU, international; Registrierungsländer)
4. **Branche / Tätigkeitsschwerpunkt** (IP-Boutique, Wirtschaftskanzlei, Technologieunternehmen, Mode, Pharma etc.)
5. **Praxisumfeld** (Einzelkanzlei / kleine Kanzlei / Großkanzlei / Inhouse)

### Phase 2: IP-Praxisprofil (10 Minuten)

Gesprächsorientiert, ein Thema nach dem anderen:

**Block A – Rechtsgebiete**
- Welche IP-Rechtsgebiete bearbeiten Sie tatsächlich? (Markenrecht, Designrecht, Patentrecht, Urheberrecht, Wettbewerbsrecht/UWG, Geschäftsgeheimnisse, Open Source – Mehrauswahl)
- Für welche davon sind Sie intern zuständig, für welche beauftragen Sie externe Anwälte/Patentanwälte?

**Block B – Portfolio**
- Haben Sie ein bestehendes Schutzrechtsverzeichnis? (IP-Verwaltungssystem, Tabellenkalkulation, keines)
 - Falls ja: Können Sie es als CSV/XLSX/PDF teilen? → Wenn geteilt, Extraktion anbieten
 - Falls nein: Gemeinsam ein Basis-Portfolio aufbauen (Name, Typ, Reg.-Nr., Klassen, Ablaufdaten)
- Jurisdiktionen, in denen Sie Schutzrechte halten oder verwalten (DE/DPMA, EU/EUIPO, INT/WIPO-Madrid, EP/EPA, PCT)

**Block C – Durchsetzungsstrategie**
- Wo ordnen Sie Ihre Durchsetzungsstrategie ein?
 - **Offensiv:** Abmahnungen früh bei augenfälliger Verletzung; Klage bereit
 - **Ausgewogen:** Informelle Kontaktaufnahme zuerst; Abmahnung/Klage bei kommerziellem Schaden
 - **Defensiv:** Nur durchsetzen wenn Klage wahrscheinlich und Mandant/Kanzlei bereit sind
- Gibt es Ausnahmen von dieser Standardhaltung? (z. B. bei bestimmten Branchen, Verletzungsarten, Wiederholungstätern)

**Block D – Genehmigungsmatrix**
- Wer muss Abmahnungen genehmigen, bevor sie versendet werden?
- Wer muss Notice-and-Action-Meldungen genehmigen?
- Wer muss Klageerhebungen genehmigen?
- Gibt es automatische Eskalationsauslöser (Streitwert > X €, Gegner ist Mandant, mediales Risiko)?

**Block E – Markenschutz**
- Überwachen Sie Ihre Marken aktiv? (Überwachungsdienst, internes Monitoring, reaktiv)
- Welche Marken werden überwacht?
- In welchen Jurisdiktionen?

**Block F – Externe Berater**
- Externe Patentanwälte / Markenanwälte für Anmeldungen?
- Externe Prozessanwälte für Verletzungsstreitigkeiten?

**Block G – Integrationen**
- IP-Verwaltungssystem angebunden? (Anaqua, CPA Global, PatSnap, Clarivate, Excel, keines)
- Rechtsprechungsdatenbank? (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang, beide, keine)
- Dokumentenspeicher? (SharePoint, Box, Datev DMS, keiner)

**Block H – OSS-Richtlinie**
- Haben Sie eine Open-Source-Richtlinie? Falls ja, teilen Sie sie zur Extraktion.
- Copyleft-Produkte erlaubt? GPLv3-Code in proprietären Produkten erlaubt?

### Phase 3: Profil schreiben

Nach Abschluss des Interviews alle Antworten in das Kanzleiprofil unter
`~/.claude/plugins/config/claude-fuer-deutsches-recht/gewerblicher-rechtsschutz/CLAUDE.md`
schreiben. Alle `[PLATZHALTER]`-Marker durch die tatsächlichen Informationen ersetzen.

Bestätigung ausgeben:
> **Einrichtung abgeschlossen.** Ihr Kanzleiprofil wurde unter `[Pfad]` gespeichert. Alle Skills lesen dieses Profil vor dem Start.
>
> **Bereit für:**
> - `/gewerblicher-rechtsschutz:abmahnung-urheberrecht` – Abmahnung entwerfen oder triagieren
> - `/gewerblicher-rechtsschutz:markenrecherche [Marke]` – Clearance-Prüfung
> - `/gewerblicher-rechtsschutz:schutzrechts-portfolio` – Schutzrechtsfristen prüfen
> - Alle anderen Skills
>
> **Nächster empfohlener Schritt:** Führen Sie `/gewerblicher-rechtsschutz:schutzrechts-portfolio` aus, um Ihre eingetragenen Schutzrechte und fällige Fristen zu prüfen.

### Flags

- `--redo` – Interview komplett neu ausführen (vorhandenes Profil wird überschrieben)
- `--check-integrations` – nur Integrationsprüfung, ohne vollständiges Re-Interview
- `--quick` – nur Pflichtfelder (Blöcke A + C + D); restliche Felder als Platzhalter belassen

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Dieses Interview-Skill zitiert keine primären Rechtsquellen; es konfiguriert das System. Alle nachgelagerten Skills zitieren dann nach dem befüllten Kanzleiprofil.

## Ausgabeformat

Gesprächsorientiertes Q&A (ein Themenblock je Nachricht, nicht alle Fragen auf einmal). Abschluss: Bestätigungsmeldung + Link zum angelegten Profil + Liste der freigeschalteten Befehle.

## Rechtlicher Hintergrund: Relevante Normen bei Kanzleieinrichtung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 43a Abs. 2 BRAO – Verschwiegenheitspflicht: Schutzrechtsportfolio und Genehmigungsmatrix enthalten mandantenbezogene Daten und unterliegen der Verschwiegenheit; nur in gesicherter Umgebung speichern.
- § 203 StGB – Schutz mandantenbezogener Daten: Weitergabe des Kanzleiprofils an Dritte ohne Mandantenzustimmung strafbewehrt.
- FAO § 14k – Fachanwalt gewerblicher Rechtsschutz: Einrichtung des Profils hilft beim Nachweis der Fallzahlen (80 Fälle in 3 Jahren, davon 50 rechtsfoermlich) durch strukturiertes Mandatsmanagement.

## Risiken / typische Fehler

- **Zu early termination:** Wenn das Interview abgebrochen wird, verbleiben Platzhalter im Profil; alle anderen Skills stoppen dann und fordern ein erneutes Interview.
- **Kein Portfolio geteilt:** Ohne Schutzrechtsverzeichnis kann der Portfolio-Skill keine Fristen berechnen; Nutzer auf manuelle Eingabe hinweisen.
- **Durchsetzungsstrategie zu vage:** "Ausgewogen" ohne spezifizierte Auslöser führt zu inkonsistenter Genehmigungsmatrix; nachfragen, bis Auslöser konkret sind.
- **Integrationsstatus nicht verifiziert:** Das Plugin prüft nicht ob eine Datenbank tatsächlich erreichbar ist; Nutzer darauf hinweisen, dass `--check-integrations` dies jederzeit prüfen kann.
- **Vertraulichkeit:** Das Kanzleiprofil enthält mandantenbezogene Strukturinformationen; nicht in Klartext über ungesicherte Kanäle übertragen (§ 43a Abs. 2 BRAO, § 203 StGB).

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Korrektur: GRUR 2019, 748 → GRUR 2019, 746. Verifiziert via damm-legal.de und dejure.org.
-->
