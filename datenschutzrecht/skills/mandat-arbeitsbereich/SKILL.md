---
name: mandat-arbeitsbereich
description: "Mandat-Arbeitsbereiche für Mehrmandat-Kanzleien verwalten: anlegen, auflisten, wechseln, schließen. Stellt sicher, dass Datenschutzmandate mandatsübergreifend isoliert bleiben (kein Kontext-Leak zwischen Mandaten). Für internen Unternehmenseinsatz nicht relevant."
---

# Mandat-Arbeitsbereich – Mehrmandat-Kanzlei

## Zweck

Isolation von Datenschutzmandaten in Mehrmandat-Kanzleien: Jeder Mandant erhält einen eigenen Arbeitsbereich mit eigener Mandatsdatei (`mandat.md`). Skills lesen das kanzlei-weite Praxisprofil (`CLAUDE.md`) für kanzleiweite Regeln und die mandatsspezifische Datei für mandatsspezifische Fakten. Kontext, Erkenntnisse und Ausgaben fließen nicht zwischen Mandaten durch.

**Nur relevant für Mehrmandat-Kanzleien.** Bei internem Unternehmenseinsatz (ein Verantwortlicher) ist dieser Skill deaktiviert; Skills verwenden das Praxisprofil direkt.

Beachte: Mandantendaten unterliegen § 43a Abs. 2 BRAO, § 203 StGB. Mandatsisolation ist datenschutz- und berufsrechtliche Pflicht.

## Eingaben

- Befehlsform: `neu | liste | wechsle [Mandat-ID] | schließe [Mandat-ID] | keins`
- Bei `neu`: Mandantenname, kurze Beschreibung des Datenschutzmandats, Mandats-ID (Kürzel)
- Bei `wechsle`: Mandat-ID des Zielmandats

## Ablauf

### `neu` – Neues Mandat anlegen

1. Mandat-ID vergeben (Kürzel, z.B. `mand-2024-04-mueller-dsfa`).
2. Verzeichnis anlegen: `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/mandate/[mandat-id]/`
3. Leere `mandat.md` mit Pflichtfeldern anlegen (s. Struktur unten).
4. Aktives Mandat in Praxisprofil auf neue ID setzen.
5. Bestätigung ausgeben: „Mandat [ID] angelegt. Alle folgenden Skill-Aufrufe arbeiten in diesem Mandatskontext."

### `liste` – Mandatsübersicht

Alle Verzeichnisse unter `mandate/` auflisten:
| Mandat-ID | Mandant | Beschreibung | Status | Letzte Aktivität |
|---|---|---|---|---|
| … | … | … | offen / abgeschlossen | Datum |

### `wechsle [Mandat-ID]` – Mandat wechseln

1. Mandat-ID aus Liste verifizieren.
2. Aktives Mandat in Praxisprofil auf neue ID setzen.
3. Bestätigung ausgeben; laufende offene Aufgaben im alten Mandat nennen, falls vorhanden.

### `schließe [Mandat-ID]` – Mandat abschließen

1. Status in `mandat.md` auf „abgeschlossen" und Abschlussdatum setzen.
2. Aktives Mandat zurücksetzen (auf „keins").
3. Ausgabedateien des Mandats sind weiter zugänglich, werden aber nicht mehr von Skills aktiv gelesen.

### `keins` – Kanzlei-Kontext (kein aktives Mandat)

Skills arbeiten im kanzlei-weiten Praxisprofil ohne mandatsspezifischen Kontext. Sinnvoll für allgemeine Kanzlei-Konfiguration oder Skills die sich auf die gesamte Kanzlei beziehen (z.B. Policy-Monitor für kanzlei-interne Richtlinien).

## Matter.md-Struktur

```markdown
# Mandat: [Mandat-ID]

## Mandant
- **Name:** [Mandantenname]
- **Rechtsform:** [GmbH / AG / Einzelperson / öffentliche Stelle]
- **Branche:** [Branche]
- **Hauptniederlassung:** [Bundesland]
- **Rolle Mandant:** [Verantwortlicher / Auftragsverarbeiter / beides]

## Mandatsbeschreibung
[Kurzbeschreibung: Was ist der Auftrag? Welches datenschutzrechtliche Vorhaben?]

## Zuständige Aufsichtsbehörde (Mandant)
[BfDI / LfDI [Bundesland]]

## Ansprechpartner
- **Mandant:** [Name, E-Mail]
- **DSB Mandant:** [Name oder „nicht bestellt"]
- **Kanzlei intern:** [zuständige·r Anwalt/Anwältin]

## Abweichungen vom Kanzlei-Praxisprofil
[Nur aufführen, was beim Mandanten anders ist als im kanzlei-weiten Profil]
- Rechtsgrundlage: [...]
- AVV-Positionen: [...]
- DSFA-Auslöser: [...]

## Systemliste Mandant (für Betroffenenanfragen Art. 15 DSGVO)
- [System 1]
- [System 2]

## Verarbeitungsverzeichnis
[Pfad oder „noch nicht bereitgestellt"]

## Ausgaben dieses Mandats
[Ordnerpfad oder Auflistung erstellter Dokumente]

## Status
offen / abgeschlossen
**Abgeschlossen am:** [Datum]
```

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht Rechtsanwalt)
- § 203 StGB (Verletzung von Privatgeheimnissen, Berufsgeheimnisträgerpflicht)
- Art. 28, 29 DSGVO (Auftragsverarbeitung bei Nutzung externer Systeme)
- Art. 25 DSGVO (Datenschutz durch Technikgestaltung – Mandatsisolation als TOMs)
- Zuck, in: Zuck/Lenz, Anwaltsrecht, 2. Aufl. 2018, § 43a BRAO Rn. 15 ff. (Berufsgeheimnis).

## Ausgabeformat

- Kurzbestätigungen (angelegt, gewechselt, geschlossen) als einzeilige Statusnachricht
- Mandatsübersicht als Tabelle
- `mandat.md` als vollständig befülltes Dokument

## Risiken / typische Fehler

- **Mandatsisolation nicht gewährleistet:** Wenn Skills ohne aktives Mandat auf mandatsspezifische Daten zugreifen oder mandatsübergreifend aggregieren, verletzt dies § 43a Abs. 2 BRAO und Art. 5 Abs. 1 lit. f DSGVO (Integrität und Vertraulichkeit).
- **Keine Löschung abgeschlossener Mandate:** Ordner nicht löschen – Aktenaufbewahrungspflicht nach § 50 Abs. 1 BRAO (6 Jahre nach Ablauf des Kalenderjahres, in dem das Mandat endete).
- **Mandant ist selbst AV:** Wenn der Mandant selbst Auftragsverarbeiter eines Dritten ist, kann das Datenschutzmandat vertikale Sub-AV-Fragen berühren (Art. 28 Abs. 2 Satz 2 DSGVO). In `mandat.md` explizit vermerken.
- **Aktives Mandat nicht zurückgesetzt:** Nach Mandatswechsel immer prüfen, dass kein unbeabsichtigter Mandatskontext aktiv ist. Standardbefehl `keins` nach Mandatsabschluss empfohlen.
