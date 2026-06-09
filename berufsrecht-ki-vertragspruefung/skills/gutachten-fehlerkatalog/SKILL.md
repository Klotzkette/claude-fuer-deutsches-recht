---
name: gutachten-fehlerkatalog
description: "Gutachten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Gutachten Fehlerkatalog

## Zweck

Dieser Fehlerkatalog prüft Arbeitsergebnisse für **Berufsrechts-KI bei Vertragsprüfung** vor Abgabe, Versand oder Mandantenfreigabe gegen die im Sachgebiet typischen Fehlerquellen — jeweils mit Symptom, Diagnose und Heilung.

## Fehlerkatalog

### 1. Frist falsch berechnet oder übersehen (Rechtzeitige Mandatsannahme)

- **Symptom:** Frist falsch berechnet oder übersehen (Rechtzeitige Mandatsannahme)
- **Diagnose:** Fristbeginn ab falschem Ereignis gerechnet (Zugang vs. Datum des Schreibens) oder Vorfrist im Kanzleisystem fehlt
- **Heilung:** Fristenkette aus dem Originaldokument rekonstruieren, Zugangsnachweis sichern, Vorfrist mit zwei Wochen setzen

### 2. Parallelfrist vergessen (Schriftform-Erfordernisse)

- **Symptom:** Parallelfrist vergessen (Schriftform-Erfordernisse)
- **Diagnose:** Zweite, unabhängig laufende Frist wird von der ersten verdeckt
- **Heilung:** Alle Fristen des Vorgangs tabellarisch erfassen und einzeln verfügen

### 3. Falsche Zuständigkeit adressiert (richtig: RAK)

- **Symptom:** Falsche Zuständigkeit adressiert (richtig: RAK)
- **Diagnose:** Schriftsatz oder Antrag an unzuständige Stelle — Fristwahrung gefährdet
- **Heilung:** Zuständigkeit vor Versand gegen Gesetz und aktuelle Organisationsverfügung prüfen; bei Zweifel fristwahrend bei beiden Stellen einreichen

### 4. Beweismittel nicht gesichert (Tool-Dokumentation)

- **Symptom:** Beweismittel nicht gesichert (Tool-Dokumentation)
- **Diagnose:** Tatsachenbehauptung im Schriftsatz ohne verfügbares Beweismittel
- **Heilung:** Pro Behauptung Beweismittel und Fundstelle notieren; fehlende Belege als Lücke ausweisen und beschaffen

### 5. Schlüsseldokument fehlt oder veraltet (AVV-Vertrag)

- **Symptom:** Schlüsseldokument fehlt oder veraltet (AVV-Vertrag)
- **Diagnose:** Arbeit mit Entwurfs- oder Altfassung statt der maßgeblichen Version
- **Heilung:** Versionsstand und Datum jedes Dokuments prüfen; maßgebliche Fassung in der Akte markieren

### 6. Normzitat ohne Fassungsprüfung (§ 43a BRAO)

- **Symptom:** Normzitat ohne Fassungsprüfung (§ 43a BRAO)
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
