---
name: richtlinien-vergleich
description: Richtlinien-Diff – vergleicht eine neue Aufsichtsnorm oder -verlautbarung gegen eine bestehende interne Richtlinie. Laden, wenn eine konkrete Norm oder Verlautbarung gegen ein Bestandsdokument verglichen werden soll.
language: de
triggers:
  - "richtlinien-vergleich"
  - "Richtlinien-Diff"
  - "Diff"
  - "Richtlinie vergleichen"
  - "was hat sich geändert"
  - "neue Norm gegen Richtlinie"
---

# Richtlinien-Diff

## Zweck

Dieser Skill vergleicht eine neue oder geänderte Aufsichtsnorm / Verlautbarung mit einer bestehenden internen Richtlinie. Das Ergebnis ist ein strukturierter Diff: Welche Anforderungen der neuen Norm sind in der Richtlinie abgedeckt? Wo weicht die Richtlinie ab? Wo hat die Norm Neues hinzugefügt oder Altes gestrichen?

Typische Einsatzfelder:
- Neue MaRisk-Novelle gegen bestehende Risikomanagement-Richtlinie
- Geändertes BaFin-Rundschreiben BAIT/VAIT gegen IT-Sicherheitsrichtlinie
- Neue EBA-Leitlinien gegen interne Compliance-Policies
- Geändertes BMF-Schreiben gegen steuerliche Richtlinien / AO-Verfahrenshandbuch

## Eingaben

- **Neue Norm / Verlautbarung:** Text oder Link (BaFin-Rundschreiben, MaRisk-Modul, EBA-Leitlinie, Gesetzestext)
- **Bestehende Richtlinie:** Bestandsdokument (hochgeladen oder aus Bibliothek)
- **Scope:** Optional – nur bestimmte Abschnitte vergleichen
- Optional: Vorheriger Diff-Lauf zum Vergleich

## Ablauf

### 1. Neue Norm strukturieren

Neue Norm / Verlautbarung lesen und in nummerierte Anforderungen zerlegen:

| Nr. | Abschnitt | Anforderungstext (Kurzfassung) | Verbindlichkeit |
|---|---|---|---|
| A01 | AT 4.3.2 | Aufbewahrung von Daten mind. 10 Jahre | Verbindlich |
| A02 | AT 4.3.2 | Backup-Konzept mit Wiederherstellungstest | Verbindlich |
| A03 | AT 4.3.2 | Dokumentation der Datenklassifizierung | Empfehlung |

Verbindlichkeitskennzeichnung:
- **Verbindlich:** „hat sicherzustellen", „muss", „sind zu"
- **Empfehlung/Best Practice:** „sollte", „kann", „wird empfohlen"

### 2. Bestehende Richtlinie strukturieren

Bestehende Richtlinie lesen und relevante Abschnitte den neuen Anforderungen zuordnen.

### 3. Diff-Tabelle erstellen

| Anforderung (Norm) | Deckung in Richtlinie | Status | Differenz |
|---|---|---|---|
| A01: Datenhaltung 10 J. | § 4 Abs. 2 IKS-Richtlinie: 7 Jahre | 🔴 Abweichung | Frist 3 J. kürzer |
| A02: Backup-Konzept | § 5 IKS-Richtlinie: vollständig | 🟢 Gedeckt | – |
| A03: Datenklassifizierung | Keine Regelung | 🟡 Lücke (Best Practice) | Empfehlung fehlt |
| – | § 7 IKS-Richtlinie: Prüfprotokoll | ⚪ Überschuss | Norm enthält keine solche Pflicht |

Status-Legende:
- 🔴 **Abweichung:** Richtlinie weicht von verbindlicher Anforderung ab
- 🟡 **Lücke:** Anforderung fehlt in Richtlinie (verbindlich: 🔴 potentiell; Best Practice: 🟡)
- 🟢 **Gedeckt:** Anforderung vollständig und korrekt abgebildet
- ⚪ **Überschuss:** Richtlinie enthält Regelung, die die Norm nicht fordert (kein Problem, aber zur Kenntnis)

### 4. Zusammenfassung

```
Diff-Zusammenfassung: [Normtitel] vs. [Richtlinientitel]
Analysiert: N Normabschnitte | N Richtlinienabschnitte

Handlungsbedarf:
🔴 N Abweichungen (verbindliche Anforderungen, Richtlinie weicht ab)
🟡 N Lücken (neue Anforderungen ohne Entsprechung)
🟢 N gedeckt
⚪ N Überschüsse (Richtlinie enthält Mehr als die Norm fordert)
```

### 5. Empfehlung

Für jede 🔴-Abweichung und jede wesentliche 🟡-Lücke:
- Konkrete Formulierungsänderung vorschlagen (Ausgangspunkt für `/richtlinien-neufassung`)
- Frist aus der Verlautbarung angeben
- Eskalationsbedarf markieren (`[prüfen]` bei Unklarheit)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen und Verlautbarungen:
- BaFin-Rundschreiben 09/2017 (BA) – MaRisk, alle Novellen [Modellwissen – prüfen auf aktuelle Fassung]
- BaFin-Rundschreiben 10/2018 (BA) – BAIT [Modellwissen – prüfen]
- BaFin-Rundschreiben 10/2017 (VA) – VAIT [Modellwissen – prüfen]
- BaFin-Rundschreiben 05/2021 (IO) – ZAIT (Zahlungsdienstleister IT) [Modellwissen – prüfen]
- EBA-Leitlinien EBA/GL/2019/04 – IKT-Risikomanagement [Modellwissen – prüfen]
- DORA Art. 5 ff. (EU) 2022/2554 (ICT Risk Management)
- § 25a KWG (Ordnungsgemäße Geschäftsorganisation)

Kommentarliteratur:
- Boos/Fischer/Schulte-Mattler, KWG, 5. Aufl. 2016, § 25a Rn. 44 ff. (Risikomanagementsystem).

## Ausgabeformat

- **Diff-Tabelle:** Alle Anforderungen mit Deckungsgrad
- **Zusammenfassung:** Kennzahlen
- **Empfehlungen:** Konkrete Formulierungsänderungen als Ausgangspunkt für Neufassung
- Reviewer-Header und Prüfernotiz wie in CLAUDE.md definiert

## Beispiel

**Eingabe:** `/regulatorisches-recht:richtlinien-vergleich MaRisk-AT-4.3.2-Novelle-2023`

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], IKS-Richtlinie v. 01.03.2023 [Nutzer-Input]
> - **Gelesen:** AT 4.3.2 vollständig; IKS-Richtlinie §§ 1–12
> - **Zu Ihrer Einschätzung:** 2 Positionen mit 🔴 markiert `[prüfen]`

---

**Diff: MaRisk AT 4.3.2 (Novelle 2023) vs. IKS-Richtlinie (Stand: 01.03.2023)**

| Anforderung (Norm) | Deckung in Richtlinie | Status | Differenz |
|---|---|---|---|
| Datenhaltung ≥ 10 Jahre | § 4 Abs. 2: 7 Jahre | 🔴 | Verlängerung um 3 Jahre erforderlich `[prüfen]` |
| Backup-Konzept mit Test | § 5 Abs. 1–3 | 🟢 | – |
| Datenklassifizierungsdoku. | Keine Regelung | 🟡 | Abschnitt zu ergänzen |

**Empfohlene Änderung für 🔴:**
> § 4 Abs. 2 IKS-Richtlinie: „Aufbewahrungsfrist von 7 Jahren" → **„mindestens 10 Jahren"** (Anpassung an MaRisk AT 4.3.2 Novelle 2023).

**Nächster Schritt:** `/regulatorisches-recht:richtlinien-neufassung` für den vollständigen Neufassungsentwurf.

## Risiken / typische Fehler

- **Nur Wortlaut-Vergleich:** Eine Richtlinie kann die Norm wörtlich übernehmen, sie aber organisatorisch nicht umsetzen. Hinweis, dass der Diff nur den Dokumenteninhalt vergleicht, nicht die gelebte Praxis.
- **Verlautbarungsversion:** MaRisk und BAIT werden novelliert; stets Version und Datum der verwendeten Norm angeben und prüfen, ob aktuell.
- **Best-Practice vs. verbindlich:** EBA-Leitlinien sind nach Art. 16 EBA-VO „comply or explain" – nicht 1:1 verbindlich. Status klar kennzeichnen.
- **Proportionalitätsgrundsatz:** Nicht jede Norm gilt für jede Institutsgröße gleich (§ 25a Abs. 1 S. 3 KWG). Adressatenkreis prüfen und im Diff ausweisen.
