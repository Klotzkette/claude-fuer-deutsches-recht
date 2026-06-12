---
name: nicht-hochrisiko-bestaetigt-end-to
description: "Prüfung hat ergeben: kein Hochrisiko. Unternehmen fragt: Welche KI-VO-Pflichten gelten trotzdem und wie dokumentieren wir das Negativ-Ergebnis rechtssicher? Drei Pfade Anhang I/III nicht zutreffend Rückausnahme Art. 6 Abs. 3 oder verbotene Praktiken ausgeschlossen. Verbleibende Pflichten: Transpa"
---

# Kein Hochrisiko bestätigt — die End-to-End-Roadmap

## PFLICHT-DISCLAIMER

**Keine Rechtsberatung. Mechanischer Workflow.** Die Negativ-Diagnose ist nur so belastbar wie die zugrunde liegenden Tatsachenfeststellungen.

---

## Die drei Wege zum "Kein Hochrisiko"

### Weg A — Nie ein Anhang-I- oder Anhang-III-Bereich

**Diagnose:** das System ist kein Sicherheitsbauteil eines in Anhang I genannten Produkts (Art. 6 Abs. 1 KI-VO) UND fällt nicht in einen der acht Anhang-III-Bereiche (Art. 6 Abs. 2 KI-VO).

**Anhang-III-Bereiche zur Erinnerung:**
1. biometrische Systeme (Identifizierung, Kategorisierung, Emotionserkennung)
2. kritische Infrastruktur (Verkehr, Wasser, Gas, Wärme, Strom, kritische digitale Infrastruktur)
3. allgemeine und berufliche Bildung (Zugang, Bewertung, Verhalten)
4. Beschäftigung, Personalmanagement, Selbständigkeit (Personalentscheidungen, Aufgabenzuteilung, Leistungsüberwachung)
5. Zugang zu wesentlichen privaten und öffentlichen Diensten (Sozialleistungen, Bonität, Risikobewertung Lebens-/Krankenversicherung, Notruf-Triage)
6. Strafverfolgung (Risikobewertung, Lügendetektor, Beweisbewertung, Profiling, Vorhersagen)
7. Migration, Asyl, Grenzkontrolle
8. Justiz, demokratische Prozesse

**Was tun?**
- → Skill: `hochrisiko-zuordnung-art-6-und-anhang-i-iii` (Negativ-Prüfung dokumentieren)
- → Skill: `hochrisiko-art-6-abs-2-anhang-iii` für jeden der acht Bereiche begründen, warum er nicht greift
- → Skill: `hochrisiko-art-6-abs-1-sicherheitsbauteil` für Anhang-I-Negativ-Begründung

**Ergebnis:** Keine Konformitätsbewertung, keine CE-Kennzeichnung, keine EU-DB-Registrierung als Hochrisiko-System.

---

### Weg B — Rückausnahme nach Art. 6 Abs. 3 KI-VO greift

**Diagnose:** das System fällt zwar in einen Anhang-III-Bereich, erfüllt aber eine der vier Rückausnahmen UND **kein Profiling natürlicher Personen** liegt vor.

**Die vier Rückausnahmen (Art. 6 Abs. 3 KI-VO):**

| Nr. | Tatbestand | typische Beispiele |
|---|---|---|
| (a) | rein vorbereitende Aufgabe einer Bewertung | Dokumentensortierung, Formatprüfung |
| (b) | enge prozedurale Aufgabe | Datenextraktion aus strukturiertem Formular |
| (c) | Verbesserung des Ergebnisses einer zuvor abgeschlossenen menschlichen Tätigkeit | Stilkorrektur, Übersetzungsverbesserung |
| (d) | Erkennung von Entscheidungsmustern, ohne menschliche Bewertung zu ersetzen | Anomalie-Markierung zur menschlichen Nachkontrolle |

**Wichtige Schranke:** Rückausnahme **niemals** anwendbar, wenn das System **Profiling natürlicher Personen** durchführt (Art. 6 Abs. 3 letzter Satz KI-VO).

**Was tun?**
- → Skill: `rueckausnahme-art-6-abs-3` (Tatbestand prüfen und dokumentieren)
- Begründung schriftlich festhalten, warum eine der vier Ausnahmen greift
- Profiling-Negativ-Prüfung dokumentieren
- **Dokumentationspflicht:** Anbieter, der sich auf Rückausnahme beruft, muss die Bewertung vor Inverkehrbringen dokumentieren und auf Anforderung der nationalen Marktaufsichtsbehörde vorlegen (Art. 6 Abs. 4 KI-VO).

**Achtung:** Das Risiko der Fehleinordnung trägt der Anbieter. Bei Streit mit Marktaufsicht: Beweislast für Vorliegen der Rückausnahme.

---

### Weg C — KI-System liegt schon nicht vor / kein territorialer Anwendungsbereich

**Diagnose:** das System ist konventionelle Software (Art. 3 Nr. 1 KI-VO nicht erfüllt) ODER der territoriale Anwendungsbereich (Art. 2 KI-VO) ist nicht eröffnet ODER ein sachlicher Ausschluss greift (Art. 2 Abs. 3-12 KI-VO).

**Sachliche Ausschlüsse (Auswahl):**
- militärische, Verteidigungs- und nationale Sicherheitszwecke (Art. 2 Abs. 3)
- ausschließlich für wissenschaftliche Forschung (Art. 2 Abs. 6)
- Freie und Open-Source-KI (eingeschränkt, Art. 2 Abs. 12)
- rein persönliche Nutzung außerhalb beruflicher Tätigkeit (Art. 2 Abs. 10)

**Was tun?**
- → Skill: `liegt-ki-system-vor-art-3-nr-1` für Negativ-Begründung
- → Skill: `territorialer-anwendungsbereich-art-2`
- → Skill: `sachlicher-ausschluss-art-2-abs-3-bis-12`
- → Skill: `abgrenzung-konventionelle-software-vs-ki-system` bei Grenzfällen

**Ergebnis:** KI-VO-Anwendungsbereich nicht eröffnet. Andere Rechtsrahmen prüfen (DSGVO, Produkthaftung, Sektor-Recht).

---

## Restpflichten — auch ohne Hochrisiko

**Auch wenn Hochrisiko verneint ist, bleiben Pflichten bestehen:**

### 1. Verbot prüfen (Art. 5 KI-VO)

Egal welche Risikoklasse: Verbotene Praktiken nach Art. 5 KI-VO sind **immer** verboten, unabhängig vom Hochrisiko-Status. → Skill: `verbotene-praktiken-art-5`.

| Verbot | Tatbestand |
|---|---|
| (a) | unterschwellige Beeinflussung |
| (b) | Ausnutzung Verletzlichkeit |
| (c) | Social Scoring durch Behörden |
| (d) | Vorhersage Straftaten allein auf Profiling |
| (e) | ungezielte Bildersammlung für Gesichtsdatenbanken |
| (f) | Emotionserkennung am Arbeitsplatz / in Bildung |
| (g) | biometrische Kategorisierung sensibler Merkmale |
| (h) | Echtzeit-biometrische Fernidentifizierung im öffentlichen Raum (mit engen Ausnahmen) |

**Geltung seit:** 2.2.2025.

### 2. Begrenztes Risiko / Transparenzpflichten (Art. 50 KI-VO)

Auch ohne Hochrisiko: wenn das System unter Art. 50 fällt — Transparenz!

| Konstellation | Pflicht |
|---|---|
| direkter Kontakt mit natürlichen Personen | Hinweis, dass mit KI interagiert wird (außer offenkundig) |
| Erzeugung synthetischer Audio-, Bild-, Video-, Text-Inhalte | maschinenlesbare Markierung als KI-generiert |
| Emotionserkennungs- oder biometrisches Kategorisierungssystem (soweit nicht verboten/Hochrisiko) | Information betroffener natürlicher Personen |
| Deepfakes | Kenntlichmachung als KI-generiert/manipuliert |
| KI-generierter Text zu Themen öffentlichen Interesses | Kenntlichmachung als KI-generiert (außer redaktionelle Verantwortung) |

→ Skill: `begrenztes-risiko-art-50-transparenzpflichten`.

### 3. GPAI-Pflichten (Art. 51-55 KI-VO)

Wenn auch ein **GPAI-Modell** vorliegt: separate Pflichten unabhängig vom System-Risiko.

→ Skill: `gpai-modelle-art-51-bis-55`, `gpai-vorliegen-art-3-nr-63`.

### 4. KI-Kompetenz (Art. 4 KI-VO)

**Pflicht für alle Anbieter und Betreiber**, unabhängig von Risikoklasse: ausreichendes Maß an KI-Kompetenz beim Personal, das mit Betrieb und Nutzung der KI-Systeme befasst ist.

**Geltung seit:** 2.2.2025.

### 5. Sektorale Vorgaben

KI-VO ergänzt — ersetzt nicht — andere Rechtsrahmen:
- DSGVO (Datenschutz)
- Produkthaftung
- DSA / DMA
- sektorale Aufsicht (BaFin, BNetzA, BfArM, ...)
- Urheberrecht (insb. § 44b UrhG für Training)
- Arbeitsrecht (Betriebsrat, AGG)

→ Skill: `verhaeltnis-zu-anderen-unionsrechtsakten`, `falsche-wiese-warnung-ki-vo`.

---

## Dokumentations-Checkliste der Negativ-Diagnose

Auch ein "Kein Hochrisiko" will dokumentiert sein:

- [ ] Sachverhalt aus Mandanten-Triage festgehalten
- [ ] KI-System nach Art. 3 Nr. 1 (positiv oder negativ) festgestellt
- [ ] territorialer Anwendungsbereich nach Art. 2 (positiv oder negativ) festgestellt
- [ ] Rolle nach Art. 3 Nr. 3-7 zugeordnet
- [ ] Verbotene Praktik nach Art. 5 ausgeschlossen
- [ ] Anhang I (Sicherheitsbauteil) ausgeschlossen
- [ ] alle acht Anhang-III-Bereiche einzeln ausgeschlossen ODER
- [ ] Anhang-III-Bereich identifiziert + Rückausnahme Art. 6 Abs. 3 dokumentiert + Profiling-Negativ-Prüfung
- [ ] Art. 50-Transparenzpflichten geprüft (positiv oder negativ)
- [ ] GPAI-Modell-Frage geprüft (positiv oder negativ)
- [ ] KI-Kompetenz Art. 4 organisiert
- [ ] Querschnitt zu anderen Rechtsgebieten (DSGVO, sektoral) abgeklärt

→ Output-Skill: `output-pruefdokument-ki-vo-mit-warnhinweisen`

---

## Wichtige Warnung — Statusverlust

Negativ-Diagnose ist nicht "für immer". **Re-Evaluation bei:**

- wesentlicher Änderung des Systems (Art. 43 Abs. 4 KI-VO)
- Erweiterung der bestimmungsgemäßen Verwendung
- neuer Use-Case in einem Anhang-III-Bereich
- neue Daten / neuer Trainingslauf mit erweitertem Funktionsumfang
- Änderung der Rechtslage (Durchführungsrechtsakte, Leitlinien Kommission, harmonisierte Normen)

**Empfehlung:** jährliche Review der Negativ-Diagnose festschreiben.

---

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Maßnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Prüfergebnis
**Adressat:** Prüfer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — NICHT HOCHRISIKO BESTAETIGT END TO END ROADMAP
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
