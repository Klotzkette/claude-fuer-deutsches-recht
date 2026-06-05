---
name: marktaufsicht-behoerdenkommunikation
description: "Marktaufsicht Behoerdenkommunikation: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Marktaufsicht Behoerdenkommunikation

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Marktaufsicht Behoerdenkommunikation** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `marktaufsicht-behoerdenkommunikation-evidence-room` | Marktaufsicht und Behoerdenkommunikation: Evidence Room fuer KI-VO-Pruefungen, Zuständigkeit, Fristen, Dokumentenpakete, technische Erklaerungen, Betriebsgeheimnisse, Schwärzung, Nachforderung und Eskalationsstrategie. |
| `marktueberwachung-meldung-vorfaelle-art-72-bis-79` | Anbieter oder Betreiber hat einen schwerwiegenden Vorfall mit einem Hochrisiko-KI-System und fragt: Was muss gemeldet werden an wen und innerhalb welcher Fristen? Art. 72 bis 79 KI-VO Post-Market-Monitoring und Meldepflichten. Prüfraster: serious incident reporting Definition schwerwiegender Vorfall Art. 3 Nr. 49 Meldefristen Inhalt der Meldung Meldewege nationale Aufsichtsbehoerde. Marktueberwauchungsmassnahmen Rückruf Aussetzen des Betriebs. Output: Melde-Checkliste und Vorlage Vorfallmeldung. Abgrenzung zu governance-aufsichtsbehoerden-art-70 (zuständige Stellen) und hochrisiko-bestätigt-end-to-end-roadmap. |
| `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` | Prüfung hat ergeben: kein Hochrisiko. Unternehmen fragt: Welche KI-VO-Pflichten gelten trotzdem und wie dokumentieren wir das Negativ-Ergebnis rechtssicher? Drei Pfade Anhang I/III nicht zutreffend Rückausnahme Art. 6 Abs. 3 oder verbotene Praktiken ausgeschlossen. Verbleibende Pflichten: Transparenzpflichten Art. 50 GPAI-Pflichten Art. 53 KI-Kompetenz Art. 4 Sanktionen bei Verstoss. Output: Dokumentationspaket Negativ-Diagnose und Restpflichten-Checkliste. Abgrenzung zu hochrisiko-bestätigt-end-to-end-roadmap (Hochrisiko-Roadmap) und risikoklassen-uebersicht-und-triage. |
| `notariat-cloud-ki-nebenakte-verschwiegenheit` | Notariat, Cloud und KI: Nebenakte, Entwurfsarbeit, Urkundenbezug, Verschwiegenheit, Verfuegbarkeit, lokale Aktenherrschaft, Auftragsverarbeitung, Datenabfluss und Notfallbetrieb. Prueft, wann KI/Cloud nur Hilfsmittel ist und wann es berufsrechtlich kippt. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Marktaufsicht Behoerdenkommunikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `marktaufsicht-behoerdenkommunikation-evidence-room`

**Fokus:** Marktaufsicht und Behoerdenkommunikation: Evidence Room fuer KI-VO-Pruefungen, Zuständigkeit, Fristen, Dokumentenpakete, technische Erklaerungen, Betriebsgeheimnisse, Schwärzung, Nachforderung und Eskalationsstrategie.

# Marktaufsicht: Evidence Room

## Ziel

Wenn eine Behörde Unterlagen verlangt, muss das Unternehmen schnell, geordnet und begrenzt liefern. Dieser Skill baut einen Evidence Room, der vollständig genug ist, aber keine unnötigen Risiken produziert.

## Evidence-Kategorien

- Systembeschreibung und Zweckbestimmung.
- Rollen- und Lieferkettenmatrix.
- Art.-3- und Art.-6-Vermerke.
- Risikomanagement, Datenqualität, Logging, Human Oversight.
- Konformitätsbewertung und EU-Konformitätserklärung.
- GPAI-Informationen und Urheberrechtspolitik.
- Post-Market-Monitoring und Incident-Logs.
- Nutzerinformationen und Art.-50-Hinweise.
- Vendor-Verträge und technische Anhänge.

## Kommunikationsregeln

1. Frist prüfen.
2. Zuständigkeit prüfen.
3. Geheimnisse markieren.
4. Unklare Fragen präzisieren lassen.
5. Keine Spekulationen liefern.
6. Nachreichungen sauber versionieren.

## Output

- Behördenbrief.
- Dokumentenindex.
- Schwärzungsliste.
- Fragen-an-Technik-Liste.
- Eskalationsvermerk für Geschäftsleitung.

## 2. `marktueberwachung-meldung-vorfaelle-art-72-bis-79`

**Fokus:** Anbieter oder Betreiber hat einen schwerwiegenden Vorfall mit einem Hochrisiko-KI-System und fragt: Was muss gemeldet werden an wen und innerhalb welcher Fristen? Art. 72 bis 79 KI-VO Post-Market-Monitoring und Meldepflichten. Prüfraster: serious incident reporting Definition schwerwiegender Vorfall Art. 3 Nr. 49 Meldefristen Inhalt der Meldung Meldewege nationale Aufsichtsbehoerde. Marktueberwauchungsmassnahmen Rückruf Aussetzen des Betriebs. Output: Melde-Checkliste und Vorlage Vorfallmeldung. Abgrenzung zu governance-aufsichtsbehoerden-art-70 (zuständige Stellen) und hochrisiko-bestätigt-end-to-end-roadmap.

# Marktüberwachung und Vorfallmeldung — Art. 72 bis 79 KI-VO

## Zweck

Art. 72 bis 79 KI-VO regeln die laufende Überwachung von Hochrisiko-KI-Systemen nach dem Inverkehrbringen sowie die Pflichten zur Meldung schwerwiegender Vorfälle. Compliance endet nicht mit dem Inverkehrbringen.

## Teil 1 — Post-Market-Monitoring (Art. 72 KI-VO)

### Pflicht des Anbieters

Anbieter von Hochrisiko-KI-Systemen müssen ein System für die Überwachung nach dem Inverkehrbringen einrichten, in Betrieb nehmen und aktiv betreiben. Dieses System muss:
- Aktiv und systematisch relevante Daten über die Systemleistung erheben und analysieren
- Bekannte oder neue Risiken und Fehlfunktionen identifizieren
- Die Ergebnisse dokumentieren

### Post-Market-Monitoring-Plan

Der Plan ist Bestandteil der technischen Dokumentation nach Anhang IV. Er muss mindestens enthalten:
- Beschreibung der Überwachungsmethodik
- Art und Umfang der zu erhebenden Daten (unter Beachtung von DSGVO)
- Verfahren zur Auswertung und Rückmeldung
- Kriterien für die Einleitung korrektiver Maßnahmen

### Pflicht des Betreibers

Betreiber müssen den Anbieter mit relevanten Daten über die Systemperformance im Betrieb versorgen, soweit dies vertraglich vereinbart oder gesetzlich vorgeschrieben ist.

**Prüffragen:**
- Gibt es einen dokumentierten Post-Market-Monitoring-Plan?
- Werden Daten systematisch erhoben und ausgewertet?
- Gibt es einen Prozess zur Meldung relevanter Befunde an den Anbieter?

## Teil 2 — Meldung schwerwiegender Vorfälle (Art. 73 KI-VO)

### Was ist ein schwerwiegender Vorfall?

Ein schwerwiegender Vorfall (serious incident) liegt vor, wenn ein Hochrisiko-KI-System:
- Den Tod einer Person verursacht hat oder verursacht haben kann
- Zu einer schwerwiegenden Beeinträchtigung der Gesundheit oder Sicherheit geführt hat
- Die Verletzung von Grundrechten zur Folge hatte
- Erheblichen Sachschaden verursacht hat

**Prüffragen:**
- Gab es Berichte über Systemfehler mit Auswirkungen auf Gesundheit, Sicherheit oder Grundrechte?
- Gibt es ein Verfahren zur Identifikation und Eskalation solcher Vorfälle?

### Meldefristen

**Anbieter** müssen schwerwiegende Vorfälle der nationalen Marktüberwachungsbehörde des Mitgliedstaats melden, in dem der Vorfall aufgetreten ist:
- Unmittelbar nach Kenntnisnahme, wenn der Vorfall lebensbedrohlich oder tödlich war
- Innerhalb von 15 Tagen nach Kenntnisnahme in anderen Fällen
- Innerhalb von 72 Stunden bei Vorfällen, die eine unmittelbare Reaktion erfordern

**Betreiber** müssen schwerwiegende Vorfälle unverzüglich dem Anbieter melden.

### Inhalt der Meldung

- Identifikation des Systems und des Anbieters
- Beschreibung des Vorfalls (Zeitpunkt, Ort, Art)
- Betroffene Personen und Schäden
- Umgehend eingeleitete Maßnahmen
- Ursachenanalyse (soweit bereits verfügbar)

## Teil 3 — Marktüberwachungsmaßnahmen (Art. 74 bis 79 KI-VO)

### Befugnisse der nationalen Behörden

Nationale Marktüberwachungsbehörden können:
- Informationen anfordern und Vor-Ort-Prüfungen durchführen (Art. 74 KI-VO)
- Korrekturmaßnahmen anordnen (Nachbesserung, Rückruf, Marktrücknahme)
- Den Betrieb eines Systems aussetzen oder untersagen
- Im Notfall unverzügliche Schutzmaßnahmen ergreifen (Art. 80 KI-VO)

### Schutzklausel-Verfahren (Art. 76 und 77 KI-VO)

Wenn eine nationale Behörde ein System als Risiko einstuft und Maßnahmen ergreift, informiert sie die Kommission und andere Mitgliedstaaten. Dies kann zu einem EU-weiten Verfahren führen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — MARKTUEBERWACHUNG MELDUNG VORFAELLE ART 72 BIS 79
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 72 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 3. `nicht-hochrisiko-bestaetigt-end-to-end-roadmap`

**Fokus:** Prüfung hat ergeben: kein Hochrisiko. Unternehmen fragt: Welche KI-VO-Pflichten gelten trotzdem und wie dokumentieren wir das Negativ-Ergebnis rechtssicher? Drei Pfade Anhang I/III nicht zutreffend Rückausnahme Art. 6 Abs. 3 oder verbotene Praktiken ausgeschlossen. Verbleibende Pflichten: Transparenzpflichten Art. 50 GPAI-Pflichten Art. 53 KI-Kompetenz Art. 4 Sanktionen bei Verstoss. Output: Dokumentationspaket Negativ-Diagnose und Restpflichten-Checkliste. Abgrenzung zu hochrisiko-bestätigt-end-to-end-roadmap (Hochrisiko-Roadmap) und risikoklassen-uebersicht-und-triage.

# Kein Hochrisiko bestätigt — die End-to-End-Roadmap

## Zweck

Sie haben die Prüfung durchlaufen und das Ergebnis ist: **kein Hochrisiko**. Das ist auch ein Ergebnis — und es will dokumentiert sein. Dieser Skill führt durch die drei Wege, auf denen man dort hin kommt, und zeigt, welche Restpflichten dennoch zu beachten sind.

---

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

## Querverweise

- `entscheidungsbaum-ki-vo-gesamt-workflow` — Master-vorgelagert
- `hochrisiko-bestaetigt-end-to-end-roadmap` — alternative Pfade
- `risikoklassen-uebersicht-und-triage` — Klassenüberblick
- `falsche-wiese-warnung-ki-vo` — was ist KI-VO nicht
- `verbotene-praktiken-art-5` — gilt immer
- `begrenztes-risiko-art-50-transparenzpflichten` — gilt oft auch ohne Hochrisiko
- `gpai-vorliegen-art-3-nr-63` — Separate-Modellschiene
- `sanktionen-art-99-bis-101` — was passiert bei Fehl-Diagnose

---

Hinweis: Keine Rechtsberatung. Mechanische Roadmap. Die Negativ-Diagnose ist nur so belastbar wie die zugrunde liegenden Tatsachenfeststellungen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
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

## 4. `notariat-cloud-ki-nebenakte-verschwiegenheit`

**Fokus:** Notariat, Cloud und KI: Nebenakte, Entwurfsarbeit, Urkundenbezug, Verschwiegenheit, Verfuegbarkeit, lokale Aktenherrschaft, Auftragsverarbeitung, Datenabfluss und Notfallbetrieb. Prueft, wann KI/Cloud nur Hilfsmittel ist und wann es berufsrechtlich kippt.

# Notariat: Cloud, KI und Nebenakte

## Prüfziel

Der Skill hilft Notariaten, KI- und Cloudwerkzeuge so zu strukturieren, dass Entwurfsarbeit, Recherche und Aktenorganisation nicht die notarielle Amtsführung, Verschwiegenheit oder Verfügbarkeit gefährden.

## Leitplanken

- Die maßgebliche elektronische Aktenführung darf nicht faktisch aus der notariellen Kontrolle geraten.
- Cloud- und KI-Dienste sind nur Werkzeuge, keine Ersatzgeschäftsstelle.
- Bei Ausfall des Dienstes muss das Notariat arbeitsfähig bleiben.
- Geheimnisse und Urkundendaten nur in Systeme geben, die berufsrechtlich, datenschutzrechtlich und technisch freigegeben sind.

## Intake

1. Welche Daten: Entwurf, Urkundennummer, Ausweisdaten, Grundbuchdaten, Gesellschafterlisten, Geldwäscheunterlagen?
2. Welcher Dienst: Cloudspeicher, KI-Chat, Diktat, OCR, Dokumentenvergleich, Übersetzung?
3. Wo liegen Daten: EU, Drittstaat, lokale Kanzlei-/Notariatsinfrastruktur?
4. Gibt es Verschlüsselung, Rollenrechte, Backup, Export, Löschkonzept?
5. Kann die führende Akte ohne Cloudzugriff weitergeführt werden?

## Output

Erstelle:

- Freigabevermerk für ein konkretes Tool.
- Datenklassenmatrix.
- Notfall- und Exportplan.
- KI-Prompt-Regel für Notariatsmitarbeitende.
- Liste der Fälle, in denen keine echten Urkundendaten in das Tool dürfen.

## Red Flag

Wenn ein externer Dienst faktisch die einzige Stelle ist, an der aktenrelevante Informationen vollständig vorhanden sind, ist das kein harmloses Hilfsmittel mehr.
