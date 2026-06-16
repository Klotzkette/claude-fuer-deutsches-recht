---
name: aktenbestand-pflege-bea-versand
description: "Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50 BRAO sechs Jahre nach Mandatsende) Wiedervorlagen. Monatliche und jaehrliche Au..."
---

# Aktenbestandspflege

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aktenstatus

| Status | Bedeutung |
|---|---|
| **laufend** | aktive Bearbeitung |
| **ruhend** | wartet auf Reaktion Gegenseite Behörde oder Mandant |
| **abgeschlossen** | Mandat beendet — Schlussrechnung gestellt |
| **archiviert** | im Archiv abgelegt — Zugriff nur für Aufbewahrung |
| **vernichtet** | nach Ablauf der Aufbewahrungsfrist vernichtet (Audit-Eintrag) |

## Wartung pro Akte

```yaml
mandat-az: 2026/0042
status: laufend
letztes-ereignis: 2026-05-20 — Versand Berufung
letzte-pflege: 2026-05-21
naechstes-ereignis-erwartet: 2026-06-20 (Berufungsbegründungsfrist)
ruhend-seit: null
abgeschlossen-am: null
abgeschlossen-begruendung: null
archivierung-faellig: null # bei Abschluss berechnen: + 6 Jahre § 50 BRAO
vernichtung-faellig: null # 6 Jahre nach Mandatsende
```

## Mandatsende

Bei Abschluss:

1. **Schlussrechnung** über Skill `rechnungserstellung-rvg`.
2. **Aktenherausgabe** an Mandanten falls gewünscht (Originalbelege Restmaterial — Akteneinsichtsrecht des Mandanten § 50 Abs. 5 BRAO).
3. **Aufbewahrungspflicht** sechs Jahre nach Mandatsende (§ 50 Abs. 1 BRAO).
4. **Status** auf `abgeschlossen` setzen.
5. **Archivierungsdatum** und **Vernichtungsdatum** berechnen.

## Wiedervorlagen

Pro Akte: Wiedervorlagedatum erfassen — z. B. bei ruhenden Mandaten ein Drei-Monats-Check ob das Mandat noch aktuell ist.

## Lange ruhende Mandate

Skript prüft alle drei Monate:

- Welche Mandate sind seit mehr als sechs Monaten in Status `ruhend`?
- Liste an zuständigen Anwalt — Klärung ob Mandat weiter offen ist abgeschlossen werden kann oder vergessen wurde.

## Datenschutz und Löschung

- **Aufbewahrungsfrist** § 50 Abs. 1 BRAO sechs Jahre nach Mandatsende.
- **Steuerlich** § 147 AO bei Buchhaltungsunterlagen acht oder zehn Jahre.
- **Nach Ablauf** vernichten — physisch durch Aktenvernichter oder digital durch sicheres Löschen.
- **DSGVO Art. 5 Abs. 1 lit. e** Speicherbegrenzung: Daten nicht laenger als notwendig.

## Auswertung

### Monatlich

| Anwalt | Laufende Akten | Neu | Abgeschlossen |
|---|---|---|---|
| ... | ... | ... | ... |

### Jaehrlich

- Aktenanzahl gesamt
- Aktenverteilung nach Rechtsgebieten
- Durchschnittliche Mandatsdauer
- Schwellen: Wenn ein Anwalt mehr als X laufende Akten hat — Auslastungsalarm.

## Archivierung

- Physisch: Archivraum mit beschrifteten Aktenkartons (Az Jahr Mandant Vernichtungsdatum).
- Digital: separates Archiv-Verzeichnis `_archiv/` mit eingeschraenkten Zugriffsrechten.

## Audit-Trail

- Statusänderungen mit Datum und ausführender Person.
- Archivierung und Vernichtung mit Audit-Eintrag.

## Ausgabe

- Aktualisierter Aktenbestand.
- Monatlicher und jaehrlicher Report.
- Liste lang ruhender Mandate zur Klärung.
- Wiedervorlagen-Einträge im Tagesbrief.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 10 RVG
- § 3a RVG
- Art. 13 DSGVO
- § 14 UStG
- Art. 28 DSGVO
- § 18 UStG
- § 7 BUrlG
- Art. 32 DSGVO
- § 65d SGG
- § 55a VwG
- Art. 35 DSGVO
- Art. 21 DSGVO

### Leitentscheidungen

- BGH VI ZB 59/18
- BGH VI ZR 286/21
