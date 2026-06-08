---
name: richtlinien-monitor-vorlage-anbieter
description: "Überwacht die interne KI-Richtlinie auf Abweichungen von der gelebten Praxis — wöchentlicher Abgleich gespeicherter Folgenabschätzungen, Triage-Ergebnisse und Anbieterprüfungen, oder direkte Prüfung einer geplanten neuen KI-Praxis. Lädt, wenn der Nutzer Richtlinien-Sweep, KI-Richtlinie prüfen, deckt unsere Richtlinie das ab, wir wollen X einführen — brauchen wir eine Richtlinienänderung oder Policy-Monitor starten sagt im Ki Governance."
---

# KI-Richtlinien-Monitor

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

**Sweep-Modus:** `CLAUDE.md` (Ausgabeordner-Pfad, Richtlinienstandort,
letztes Sweep-Datum); alle Ausgabedateien seit letztem Sweep.

**Direktanfrage-Modus:** Beschreibung der geplanten KI-Praxis; aktuelle
Richtlinien-Verpflichtungen und Anwendungsfall-Register aus `CLAUDE.md`.

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 17 KI-VO**: Anbieter von Hochrisiko-KI müssen ein Qualitäts-
 managementsystem unterhalten inkl. laufender Überprüfung. Für Betreiber:
 Art. 29 Abs. 1–4 KI-VO (Überwachungs- und Meldepflichten).
- **DSGVO Art. 5 Abs. 2 (Rechenschaftspflicht)**: Verantwortliche müssen
 Einhaltung der Grundsätze nachweisen; Richtlinie und gelebte Praxis
 müssen übereinstimmen.
- **DSGVO Art. 22 i.V.m. Art. 13/14**: Betroffene müssen über automatisierte
 Entscheidungen informiert werden; Richtlinie muss Offenlegungspflichten
 widerspiegeln.
- **DSA Art. 27, 38 (VO (EU) 2022/2065)**: Transparenzpflichten für
 algorithmische Empfehlungssysteme sehr großer Plattformen.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 KI-Richtlinie ohne Adressierung von Scoring-Systemen schafft materielle
 Lücke, wenn entsprechende Systeme operativ eingesetzt werden.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Vergessen I): Grundrechtliche Schutzpflichten gegenüber algorithmischen
 Systemen; Transparenzgebot beim KI-Einsatz.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 17 Rn. 8 ff.
 (Qualitätsmanagementsystem; laufende Richtlinienüberprüfung).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 5 Rn. 62 ff.
 (Rechenschaftspflicht; Dokumentation der Verarbeitungspolitik).
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 95 ff. (Transparenzpflichten bei Algorithmen).
- Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 89 ff.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Modus-Erkennung:** kein Argument oder `--sweep` → Sweep-Modus;
Beschreibung einer Praxis → Direktanfrage-Modus.

### Sweep-Modus

1. `CLAUDE.md` laden: `## KI-Richtlinien-Verpflichtungen`, `## KI-Anwendungsfall-
 Register`, `## Ausgaben` (Ordner-Pfad, Richtlinienstandort, letztes Sweep-Datum).
2. Ausgabedateien seit letztem Sweep scannen. Bei keinen neuen Dateien:
 "Keine neuen Ausgaben seit [Datum]. Nächster Sweep: [Datum]."
3. Aus jeder Ausgabe extrahieren: freigegebener Anwendungsfall, Einsatzmodus
 (assistiv/automatisiert), Auflagen, betroffene Parteien, Anbieter-Datennutzung.
4. Kennzeichnen: neue Anwendungsfälle ohne Richtlinienabdeckung; automatisierte
 Entscheidungen wo Richtlinie menschliche Aufsicht impliziert; Anbieter-
 Datennutzung die Richtlinie referenzieren sollte.
5. Lücken klassifizieren: **ERFORDERLICH** (Richtlinie widerspricht Praxis,
 Nicht-Aktualisierung = materielle Falschdarstellung) oder **EMPFOHLEN**
 (Richtlinie schweigt, Praxis vertretbar aber klarer mit Aktualisierung).
6. Ergebnisse vorlegen; erst nach Bestätigung durch den Nutzer:
 `Letztes Sweep-Datum` und `gefundene_Lücken` in `CLAUDE.md` aktualisieren.

### Direktanfrage-Modus

Aus der Beschreibung extrahieren: KI-System; Funktion (assistiv/automatisiert/
Inhaltsgenerierung); Betroffene; Anbieter; menschliche Überprüfung?; Offenlegung?;
unerwartete Datenweitergabe? — bei vager Beschreibung eine Rückfrage.

Abgleich gegen Richtlinie und Register:

| Prüfpunkt | Aktuelle Richtlinie / Register | Geplante Praxis | Ergebnis |
|---|---|---|---|
| Anwendungsfall-Kategorie | [Register-Eintrag] | [neu] | ✅/⚠️/❌ |
| Automatisierte Entscheidung | [DSGVO Art. 22 Position] | [automatisiert?] | |
| Offenlegung ggü. Betroffenen | [Richtlinien-Zusage] | [erforderlich?] | |
| Anbieter-Datennutzung | [Playbook-Position] | [Anbieter-Bedingungen] | |

## ERFORDERLICHE Änderungen
### [Lücke]
Quelle: [Datei] | Was geschieht: [Beschreibung]
Aktuelle Richtlinie: [Zitat oder "Keine Abdeckung"]
Lücke: [was fehlt]
Formulierungsvorschlag: "[Richtlinientext]" — ergänzen in [Abschnitt]

## EMPFOHLENE Änderungen [gleiche Struktur]

## Kein Handlungsbedarf [Liste]

## Anwendungsfall-Register-Abgleich [neue Einträge vorschlagen]
```

**Direktanfrage-Ausgabe:**
```
### KI-Richtlinienprüfung: [Praxis]
Ergebnis: [RICHTLINIENÄNDERUNG ERFORDERLICH / EMPFOHLEN / KEINE ÄNDERUNG]

## Was abgedeckt ist | ## Was fehlt | ## Was im Widerspruch steht

## Anwendungsfall-Register [Vorschlag falls neu]

## Zeitplan [vor Inbetriebnahme / beim nächsten Update]
```

## Beispiel

**Direktanfrage:** "Wir wollen KI-gestützte Zusammenfassungen von
Kundenbeschwerden einführen. Ein Mitarbeiter überprüft sie vor Weiterleitung."

**Ausgabe:** Register-Eintrag "Kundenseitige KI-Assistenz" → bedingt →
Offenlegung erforderlich. Richtlinie schweigt zur KI-gestützten Beschwerde-
bearbeitung. EMPFOHLENE Ergänzung: Abschnitt zu assistierter Kunden-
kommunikation. DSGVO Art. 13/14: Datenschutzinformation muss KI-Einsatz
nennen. Ergebnis: RICHTLINIENÄNDERUNG EMPFOHLEN.

## Risiken und typische Fehler

- Sweep-Datum vor Bestätigung aktualisieren: unterdrückt beim nächsten Lauf
 die Aufmerksamkeit für dieselben Lücken.
- Zu vage Formulierungsvorschläge: "KI-gestützt" bevorzugen statt
 konkreter Modellnamen; keine Zusagen formulieren, die das Team nicht
 einhalten kann.
- Richtlinie selbst aktualisieren: nur nach menschlicher Prüfung und Freigabe.
- Eingehende Regelungsänderungen: das ist `regulierungs-luecken-analyse`. Dieser Skill
 überwacht nur interne Praxis-Abweichungen.

## Quellenpflicht

- **AI Act Art. 17** (Qualitätsmanagement) bei Hochrisiko-Anwendungsfällen.
- **AI Act Art. 29** (Betreiberpflichten, Überwachung).
- **DSGVO Art. 5 Abs. 2** (Rechenschaftspflicht) bei Richtlinien-Dokumentation.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 17.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 5 Rn. 62 ff.**

## Triage zu Beginn
1. Sweep-Modus oder Direktanfrage — neue Praxis oder regelmäßiger Policy-Abgleich?
2. Wann war der letzte Sweep — sind neue Anwendungsfaelle oder Folgenabschaetzungen seit dann dazugekommen?
3. Gibt es bereits bekannte Richtlinien-Praxis-Kluft (z.B. Anwendungsfall ohne Richtlinien-Deckung)?
4. Betrifft die neue Praxis einen Hochrisiko-Bereich (Art. 9 KI-VO Qualitaetsmanagement)?
5. Ist eine Betriebsrats-Beteiligung nach § 87 Abs. 1 Nr. 6 BetrVG relevant?

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template — Richtlinien-Monitor-Bericht
**Adressat:** KI-Governance-Verantwortlicher — Tonfall: sachlich-strukturiert
```
RICHTLINIEN-MONITOR-BERICHT
[DATUM] — Modus: [SWEEP / DIREKTANFRAGE] — Zeitraum: [DATUM BIS DATUM]

BEFUNDE:
| Nr. | Thema | Richtlinien-Position | Gelebte Praxis | Status | Empfehlung |
|---|---|---|---|---|---|
| 1 | [THEMA] | [RICHTLINIENTEXT] | [PRAXIS] | ERFORDERLICH/EMPFOHLEN | [FORMULIERUNGSVORSCHLAG] |

ZUSAMMENFASSUNG: [N] ERFORDERLICH / [N] EMPFOHLEN / [N] konform

NAECHSTE SCHRITTE:
1. Richtlinienaktualisierung: [ABSCHNITT] — Verantwortlicher: [NAME] — bis: [DATUM]
2. [WEITERE MASSNAHME]

Naechster Sweep: [DATUM]
Erstellt: [NAME], [DATUM]
```

