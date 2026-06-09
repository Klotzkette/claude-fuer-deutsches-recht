---
name: barrierefreiheit-fehlerkatalog
description: "Barrierefreiheit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Barrierefreiheit Fehlerkatalog

## Zweck

Dieser Fehlerkatalog prüft Arbeitsergebnisse für **Barrierefreiheit Web BFSG/WCAG** vor Abgabe, Versand oder Mandantenfreigabe gegen die im Sachgebiet typischen Fehlerquellen — jeweils mit Symptom, Diagnose und Heilung.

## Fehlerkatalog

### 1. Frist falsch berechnet oder übersehen (Gilt ab 28.06.2025)

- **Symptom:** Frist falsch berechnet oder übersehen (Gilt ab 28.06.2025)
- **Diagnose:** Fristbeginn ab falschem Ereignis gerechnet (Zugang vs. Datum des Schreibens) oder Vorfrist im Kanzleisystem fehlt
- **Heilung:** Fristenkette aus dem Originaldokument rekonstruieren, Zugangsnachweis sichern, Vorfrist mit zwei Wochen setzen

### 2. Parallelfrist vergessen (BFSG-Berichtspflichten)

- **Symptom:** Parallelfrist vergessen (BFSG-Berichtspflichten)
- **Diagnose:** Zweite, unabhängig laufende Frist wird von der ersten verdeckt
- **Heilung:** Alle Fristen des Vorgangs tabellarisch erfassen und einzeln verfügen

### 3. Falsche Zuständigkeit adressiert (richtig: BFA (Bundesfachstelle Barrierefreiheit))

- **Symptom:** Falsche Zuständigkeit adressiert (richtig: BFA (Bundesfachstelle Barrierefreiheit))
- **Diagnose:** Schriftsatz oder Antrag an unzuständige Stelle — Fristwahrung gefährdet
- **Heilung:** Zuständigkeit vor Versand gegen Gesetz und aktuelle Organisationsverfügung prüfen; bei Zweifel fristwahrend bei beiden Stellen einreichen

### 4. Beweismittel nicht gesichert (Audit-Tools axe/Lighthouse)

- **Symptom:** Beweismittel nicht gesichert (Audit-Tools axe/Lighthouse)
- **Diagnose:** Tatsachenbehauptung im Schriftsatz ohne verfügbares Beweismittel
- **Heilung:** Pro Behauptung Beweismittel und Fundstelle notieren; fehlende Belege als Lücke ausweisen und beschaffen

### 5. Schlüsseldokument fehlt oder veraltet (Konformitätserklärung)

- **Symptom:** Schlüsseldokument fehlt oder veraltet (Konformitätserklärung)
- **Diagnose:** Arbeit mit Entwurfs- oder Altfassung statt der maßgeblichen Version
- **Heilung:** Versionsstand und Datum jedes Dokuments prüfen; maßgebliche Fassung in der Akte markieren

### 6. Normzitat ohne Fassungsprüfung (BFSG)

- **Symptom:** Normzitat ohne Fassungsprüfung (BFSG)
- **Diagnose:** Zitierte Norm wurde geändert, verschoben oder aufgehoben
- **Heilung:** Vor Abgabe jeden Paragraphen gegen gesetze-im-internet.de prüfen; Übergangsvorschriften beachten

### 7. Rechtsprechung aus Modellwissen zitiert

- **Symptom:** Rechtsprechung aus Modellwissen zitiert
- **Diagnose:** Aktenzeichen oder Fundstelle nicht live verifiziert — Risiko halluzinierter Zitate
- **Heilung:** Jede Entscheidung mit Gericht, Datum, Az und frei prüfbarer Quelle gegenchecken; sonst als Prüfpunkt markieren

### 8. Mandantengeheimnis bei Tool-Einsatz verletzt

- **Symptom:** Mandantengeheimnis bei Tool-Einsatz verletzt
- **Diagnose:** Klartext-Mandantendaten in Werkzeug ohne Auftragsverarbeitungsvertrag
- **Heilung:** Vor Upload anonymisieren oder AVV-gedeckte Umgebung nutzen (§ 43a Abs. 2 BRAO, § 203 StGB)

## Ausgabe

Roter/gelber/grüner Befund je Fehlerachse; jeder rote Punkt mit konkreter Korrektur und verbleibendem Restrisiko. Quellenhygiene nach `references/quellenhygiene.md`.
