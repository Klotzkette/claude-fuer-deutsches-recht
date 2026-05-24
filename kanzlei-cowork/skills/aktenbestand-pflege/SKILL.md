---
name: aktenbestand-pflege
description: Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50 BRAO sechs Jahre nach Mandatsende) Wiedervorlagen. Monatliche und jaehrliche Auswertung Aktenanzahl je Anwalt. Markiert lange ruhende Mandate zur Klaerung. Verhindert Datenlecks bei abgeschlossenen Mandaten (DSGVO Art. 5 Speicherbegrenzung).
---

# Aktenbestandspflege

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
archivierung-faellig: null  # bei Abschluss berechnen: + 6 Jahre § 50 BRAO
vernichtung-faellig: null  # 6 Jahre nach Mandatsende
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
