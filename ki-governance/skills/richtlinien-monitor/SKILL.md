---
name: richtlinien-monitor
description: >
  Überwacht die interne KI-Richtlinie auf Abweichungen von der gelebten
  Praxis — wöchentlicher Abgleich gespeicherter Folgenabschätzungen,
  Triage-Ergebnisse und Anbieterprüfungen, oder direkte Prüfung einer
  geplanten neuen KI-Praxis. Lädt, wenn der Nutzer „Richtlinien-Sweep",
  „KI-Richtlinie prüfen", „deckt unsere Richtlinie das ab", „wir wollen
  X einführen — brauchen wir eine Richtlinienänderung" oder
  „Policy-Monitor starten" sagt.
language: de
triggers:
  - "Richtlinien-Sweep"
  - "KI-Richtlinie prüfen"
  - "AI-Act-Konformität überwachen"
  - "deckt unsere Richtlinie das ab"
  - "Policy-Drift erkennen"
  - "neue KI-Praxis prüfen"
  - "Policy-Monitor starten"
  - "KI-Governance-Überwachung"
---

# KI-Richtlinien-Monitor

## Zweck

KI-Richtlinien laufen der Praxis schneller hinterher als fast jedes andere
Richtliniendokument — Anwendungsfälle multiplizieren sich, jede freigegebene
Folgenabschätzung begründet neue Verpflichtungen, die die Richtlinie noch
nicht aufgegriffen hat.

Zwei Modi: (1) **Sweep-Modus** — wöchentlicher Abgleich des Ausgabeordners
auf Policy-Drift; (2) **Direktanfrage-Modus** — direkte Antwort auf
„Wir wollen X einführen — was bedeutet das für unsere KI-Richtlinie?"

Ausgabe ist immer: Hier ist die Lücke — ERFORDERLICH (Richtlinie wider-
spricht Praxis) oder EMPFOHLEN (Richtlinie schweigt) — plus Formulierungsvorschlag.

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

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 (Schufa-Score):
  KI-Richtlinie ohne Adressierung von Scoring-Systemen schafft materielle
  Lücke, wenn entsprechende Systeme operativ eingesetzt werden.
- EuGH, Urt. v. 04.10.2024 – C-203/22 (Dun & Bradstreet): Interne Richt-
  linien müssen verständliche Erklärung der algorithmischen Entscheidungs-
  logik vorsehen.
- BGH, Urt. v. 19.06.2018 – VI ZR 184/17, NJW 2018, 2877: Anforderungen
  an interne Organisationspflichten und deren Dokumentation; auf KI-
  Governance-Richtlinien übertragbar.
- BVerfG, Beschl. v. 06.11.2019 – 1 BvR 16/13, NJW 2020, 300 (Recht auf
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
   „Keine neuen Ausgaben seit [Datum]. Nächster Sweep: [Datum]."
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

## Ausgabeformat

**Sweep-Bericht:**
```
# KI-Richtlinien-Monitor — Sweep-Bericht
Datum: [Datum] | Gescannte Ausgaben: [N] | Neu: [N]
Gefundene Lücken: [N] ERFORDERLICH | [N] EMPFOHLEN

## ERFORDERLICHE Änderungen
### [Lücke]
Quelle: [Datei] | Was geschieht: [Beschreibung]
Aktuelle Richtlinie: [Zitat oder „Keine Abdeckung"]
Lücke: [was fehlt]
Formulierungsvorschlag: „[Richtlinientext]" — ergänzen in [Abschnitt]

## EMPFOHLENE Änderungen [gleiche Struktur]

## Kein Handlungsbedarf [Liste]
## Anwendungsfall-Register-Abgleich [neue Einträge vorschlagen]
```

**Direktanfrage-Ausgabe:**
```
# KI-Richtlinienprüfung: [Praxis]
Ergebnis: [RICHTLINIENÄNDERUNG ERFORDERLICH / EMPFOHLEN / KEINE ÄNDERUNG]

## Was abgedeckt ist | ## Was fehlt | ## Was im Widerspruch steht
## Anwendungsfall-Register [Vorschlag falls neu]
## Zeitplan [vor Inbetriebnahme / beim nächsten Update]
```

## Beispiel

**Direktanfrage:** „Wir wollen KI-gestützte Zusammenfassungen von
Kundenbeschwerden einführen. Ein Mitarbeiter überprüft sie vor Weiterleitung."

**Ausgabe:** Register-Eintrag „Kundenseitige KI-Assistenz" → bedingt →
Offenlegung erforderlich. Richtlinie schweigt zur KI-gestützten Beschwerde-
bearbeitung. EMPFOHLENE Ergänzung: Abschnitt zu assistierter Kunden-
kommunikation. DSGVO Art. 13/14: Datenschutzinformation muss KI-Einsatz
nennen. Ergebnis: RICHTLINIENÄNDERUNG EMPFOHLEN.

## Risiken und typische Fehler

- Sweep-Datum vor Bestätigung aktualisieren: unterdrückt beim nächsten Lauf
  die Aufmerksamkeit für dieselben Lücken.
- Zu vage Formulierungsvorschläge: „KI-gestützt" bevorzugen statt
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
- **EuGH C-634/21 (Schufa-Score)** bei Scoring-/Profiling-Lücken.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 17.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 5 Rn. 62 ff.**
