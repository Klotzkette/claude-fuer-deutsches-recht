---
name: mandanten-kommunikations-log
description: >
  Erstellt und pflegt ein strukturiertes Kommunikationslogbuch für ein Mandat.
  Protokolliert jede Kontaktaufnahme mit dem Mandanten, dem Jobcenter, dem BAMF,
  Gerichten oder anderen Stellen – mit Datum, Inhalt, nächsten Schritten und
  Verschwiegenheitshinweisen. Aufrufen bei jeder neuen Kommunikation oder zur
  Erstellung des Semesterübergabe-Protokolls.
argument-hint: "[optional: Aktenzeichen oder Mandantenkennung]"
language: de
when_to_use: |
  Trigger phrases and example requests:
  - kommunikation protokollieren
  - kontakt loggen
  - mandantenkontakt
  - mandanten-kommunikations-log
  - kommunikationsverlauf
  - kontaktprotokoll erstellen
---

# /mandanten-kommunikations-log

1. Lade `CLAUDE.md` → Fachbereich, Aufsichtsmodell, Verschwiegenheitspflichten.
2. Prüfe: Handelt es sich um eine neue Kommunikation (→ Eintrag hinzufügen) oder um Abruf/Export (→ strukturierte Übersicht ausgeben)?
3. Erfasse alle relevanten Metadaten (Datum, Art, Beteiligte, Inhalt, Ergebnis, nächste Schritte).
4. Gib den neuen Logeintrag formatiert aus.
5. Weise auf offene Fristen und ausstehende Antworten hin.

---

# Mandantenkommunikations-Logbuch

## Zweck

Lückenlose Dokumentation aller Kontakte in einem Mandat ist aus mehreren Gründen unverzichtbar:

1. **Semesterübergabe:** Nachfolgende Studierende müssen den Stand des Mandats vollständig nachvollziehen können (`/rechtsberatungsstelle:semester-uebergabe`).
2. **Haftungssicherung:** Im Streitfall muss nachgewiesen werden können, wann welche Mitteilung erging (§ 127 BGB analog für Fristwahrung).
3. **Qualitätssicherung:** Der anleitende Volljurist prüft, ob der Mandant korrekt informiert und keine unzulässige Rechtsberatung erteilt wurde.
4. **Verschwiegenheit:** Das Logbuch enthält personenbezogene Daten und fällt unter § 43a Abs. 2 BRAO (Anleiter), § 203 StGB (alle Beteiligten), DSGVO Art. 5, 9. Kein Zugang für Dritte ohne Freigabe.

## Berufsrechtlicher Rahmen

- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht des anleitenden Anwalts.
- § 203 Abs. 1 Nr. 3 StGB: Unbefugte Offenbarung von Mandantengeheimnissen.
- § 50 BRAO: Aufbewahrungspflicht Mandantenakte mindestens 5 Jahre.
- DSGVO Art. 5 Abs. 1 lit. e: Speicherbegrenzung – keine unnötig langen Aufbewahrungszeiten.
- DSGVO Art. 9: Besondere Kategorien (Asylstatus, Gesundheitsdaten) – erhöhte Sorgfalt.

**Intern bleiben:** Logeinträge werden nicht an den Mandanten weitergegeben. Sie sind interne Arbeitsdokumentation.

## Eingaben

- Aktenzeichen oder anonyme Mandantenkennung (z. B. „M-2024-17")
- Datum und Uhrzeit des Kontakts
- Art des Kontakts: persönlich | telefonisch | schriftlich (Brief/E-Mail/Fax) | durch Dritte (Dolmetscher)
- Beteiligte: Studierender, Anleiter, Mandant, Behörde/Gericht, Dolmetscher
- Inhalt: Was wurde mitgeteilt / besprochen / vereinbart?
- Ergebnis: Was ist entschieden, was bleibt offen?
- Nächste Schritte und Fristen

## Logstruktur (Standardformat)

```
### Eintrag [Nummer] – [Datum] [Uhrzeit]

**Art:** [persönlich | telefonisch | schriftlich]
**Beteiligte:** [Studierender: Name/Kürzel] | [Anleiter: ✓ anwesend / – nicht anwesend] | [Mandant: ✓] | [Dolmetscher: Name/Sprache oder –]
**Gegenüber:** [Jobcenter Mitte Berlin | BAMF Bremen | VG Berlin | Mandant direkt | Sonstiges: ]
**Thema:** [Kurzbeschreibung, 1–2 Sätze]

**Inhalt:**
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

**Ergebnis / Stand:**
[Was ist beschlossen? Was wurde mitgeteilt? Was bleibt offen?]

**Offene Fristen:**
| Frist | Datum | Status |
|---|---|---|
| [z. B. Widerspruch SGB II] | [TT.MM.JJJJ] | [offen] |

**Nächste Schritte:**
1. [Aktion – verantwortlich: Studierender / Anleiter – bis: TT.MM.JJJJ]
2. …

**Verschwiegenheitshinweis:** Dieser Eintrag enthält vertrauliche Mandantendaten (§ 203 StGB, § 43a BRAO). Kein Zugang für Externe.
```

## Typische Kontaktarten und besondere Hinweise

### Erstgespräch / Intake
- Immer das Datum festhalten → Ausgangspunkt für Fristen (z. B. Jahresfrist AsylG § 74: Klagefrist läuft ab Bescheidzustellung, nicht ab Erstgespräch).
- Dokumentieren, ob Dolmetscher anwesend war und ob dieser selbst Verständlichkeit bestätigt hat.
- Datenschutz-Einwilligung des Mandanten nach Art. 13 DSGVO eingeholt?

### Behördenkontakt (Jobcenter, BAMF, Ausländerbehörde)
- Aktenzeichen der Behörde notieren.
- Bei telefonischen Auskünften: Name des Sachbearbeiters, Uhrzeit, Inhalt – wegen späterer Beweisbarkeit.
- Schriftliche Bestätigung mündlicher Auskünfte anfordern (Schreiben / E-Mail als Nachbeweis).

### Gerichtskontakt
- Geschäftsnummer des Gerichts notieren.
- Fristen aus dem Beschluss/Urteil sofort in `/rechtsberatungsstelle:fristen` eintragen.
- Termin für nächste Sitzung festhalten.

### Mandantenbrief / Schriftsatz
- Versanddatum und -weg (Brief mit Einschreiben / Fax mit Sendebericht / E-Mail mit Lesebestätigung) notieren.
- Anlagen auflisten.
- Freigabe durch Anleiter vor Versand? → Status „Freigabe erteilt von [Name/Kürzel] am [Datum]".

## Ablauf

### Schritt 1: Neuer Eintrag oder Abruf?

- Neue Kommunikation dokumentieren → Eingaben abfragen (Datum, Art, Beteiligte, Inhalt, Fristen).
- Bestehendes Log abrufen → Alle Einträge chronologisch ausgeben; Summary der offenen Fristen und nächsten Schritte.
- Log für Semesterübergabe exportieren → `/rechtsberatungsstelle:semester-uebergabe` aufrufen.

### Schritt 2: Fristen prüfen

Nach jedem Eintrag automatisch prüfen:
- Gibt es neue Fristen aus diesem Kontakt?
- Sind bestehende Fristen durch diesen Kontakt beeinflusst (Hemmung, Verlängerung, Verkürzung)?
- Liegt eine kritische Frist innerhalb der nächsten 14 Tage?

Wenn ja: sofortige Benachrichtigung des Anleiters empfehlen.

### Schritt 3: Ausgabe

Strukturierter Logeintrag nach obigem Format. Immer mit Verschwiegenheitshinweis. Immer mit offenem Fristenstatus.

## Ausgabeformat

Markdown-Tabellen für Fristen. Bullet-Lists für Inhalt. Standardformat wie oben. Kein Fließtext-Protokoll – Bullets und Tabellen sind beim Semesterübergabe-Scan leichter zu lesen.

Jede Ausgabe trägt:
> **[INTERNES DOKUMENT – Vertraulich nach § 43a BRAO / § 203 StGB. Nicht für Mandanten oder Dritte bestimmt.]**

## Beispiel

### Eintrag 3 – 14.01.2025 14:30

**Art:** telefonisch
**Beteiligte:** Studierende: AS | Anleiter: – | Mandant: ✓ | Dolmetscher: Hamid Y. (Dari)
**Gegenüber:** Mandant direkt
**Thema:** Besprechung Widerspruchsergebnis Jobcenter – Bescheid vom 10.01.2025 erhalten

**Inhalt:**
- Mandant hat Bescheid vom Jobcenter Mitte Berlin (Az. 012345/24) am 12.01.2025 erhalten.
- Leistungen für Februar 2025 um 30 % abgesenkt (Sanktionsbescheid § 31a SGB II).
- Mandant versteht Bescheid nicht; Dolmetscher erklärt Inhalt auf Dari.
- Widerspruch soll eingelegt werden.

**Ergebnis / Stand:**
Mandant wünscht Widerspruch. Kopie des Bescheids wird per Post zugesandt. Frist läuft bis 12.02.2025 (1 Monat ab Bekanntgabe, § 84 SGG).

**Offene Fristen:**
| Frist | Datum | Status |
|---|---|---|
| Widerspruch SGB II § 84 SGG | 12.02.2025 | offen – dringend |

**Nächste Schritte:**
1. Entwurf Widerspruchsschreiben – verantwortlich: AS – bis: 20.01.2025
2. Freigabe durch Anleiter – bis: 28.01.2025
3. Versand per Einschreiben – bis: 10.02.2025 (Puffer)

**Verschwiegenheitshinweis:** Dieser Eintrag enthält vertrauliche Mandantendaten (§ 203 StGB, § 43a BRAO). Kein Zugang für Externe.

## Risiken / typische Fehler

- **Kein Versanddatum notiert:** Im Nachhinein nicht mehr beweisbar, ob eine Frist gewahrt wurde. Immer Einschreibebeleg aufbewahren und im Log festhalten.
- **Dolmetscher nicht dokumentiert:** Bei Sprachbarrieren ist der Nachweis, dass der Mandant den Inhalt verstanden hat, entscheidend (Aufklärungspflicht).
- **Offene Fristen nicht weitergegeben:** Beim Semesterwechsel sind nicht übergebene Fristen das größte Haftungsrisiko. Das Log ist die Grundlage für `/rechtsberatungsstelle:semester-uebergabe`.
- **Personenbezogene Daten unverschlüsselt gespeichert:** DSGVO Art. 9 verlangt erhöhten Schutz für Asylstatus, Gesundheitsdaten. Kein Upload in unkonfigurierte Cloud-Systeme ohne Auftragsverarbeitungsvertrag (Art. 28 DSGVO).
