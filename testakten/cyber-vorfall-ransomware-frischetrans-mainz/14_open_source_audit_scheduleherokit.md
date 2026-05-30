# Open-Source-Compliance-Audit — „TourPlanner" / scheduleHero (AGPL-3.0)

**Aktenstück:** 14  
**Datum:** 12.–14.05.2026  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Bearbeiter:** RA Lukas Drosten, Fachanwalt für IT-Recht

---

## 1. Hintergrund

Die Frischetrans Mittelrhein GmbH hat intern eine Softwareanwendung namens **„TourPlanner"** entwickelt. TourPlanner dient der Verwaltung und Planung von Fahrer-Touren und integriert sich mit dem (nunmehr angegriffenen) SAP S/4HANA-System. Die Eigenentwicklung wurde vom IT-Team der Frischetrans über mehrere Jahre aufgebaut.

Während der forensischen Analyse des Ransomware-Angriffs wurde festgestellt, dass TourPlanner eine Open-Source-Komponente namens **„scheduleHero"** verwendet. scheduleHero ist eine Scheduling-Engine für Ressourcenplanung, lizenziert unter der **GNU Affero General Public License Version 3 (AGPL-3.0)**.

---

## 2. Bedeutung der AGPL-3.0-Lizenz

### 2.1 Grundprinzipien der AGPL-3.0

Die GNU Affero General Public License 3.0 (AGPL-3.0) ist eine Copyleft-Lizenz mit folgenden Kernpflichten:

1. **Copyleft-Wirkung:** Wird AGPL-3.0-lizenzierter Code in ein Software-Werk integriert, muss das gesamte Werk bei Weitergabe unter AGPL-3.0 (oder einer kompatiblen GPL-Lizenz) veröffentlicht werden.

2. **Netzwerk-Copyleft (§ 13 AGPL-3.0):** Die AGPL-3.0 erweitert den Copyleft-Effekt auf den **Netzwerkbetrieb**: Wenn ein Dritter über ein Computernetzwerk mit der Software interagiert, muss der Quellcode der Anwendung denjenigen Nutzern zur Verfügung gestellt werden. Dies ist der entscheidende Unterschied zur GPL-3.0.

3. **Quelltextpflicht:** Bei Weitergabe muss der vollständige korrespondierende Quellcode mitgeliefert oder über einen Netzwerkzugang zugänglich gemacht werden.

4. **Keine proprietären Zusätze:** Eine proprietäre Überlizenzierung (Relizenzierung zu einer nicht-copyleft-Lizenz) ist ohne Zustimmung aller Rechteinhaber nicht zulässig.

### 2.2 Kritischer Punkt: Netzwerk-Nutzung durch Dritte

TourPlanner wird als Webapplikation betrieben und ist über das interne Netzwerk für folgende Nutzergruppen zugänglich:
- Dispositionsabteilung (intern, ca. 8 Benutzer)
- Fahrer (über Mobilgeräte / Telematik-App — **externe Netzwerkinteraktion**)
- ggf. Kunden (keine aktuellen Belege gefunden)

Sobald **externe Nutzer** (Fahrer über Smartphone-App oder Kunden) über das Netzwerk mit dem TourPlanner interagieren, gilt die Netzwerk-Copyleft-Pflicht des § 13 AGPL-3.0. In diesem Fall wäre Frischetrans verpflichtet, den gesamten Quellcode des TourPlanner (einschließlich aller mit scheduleHero integrierten Teile) zur Verfügung zu stellen.

---

## 3. Befunde des Audits

### 3.1 Verwendung von scheduleHero

| Parameter | Befund |
|---|---|
| Komponente | scheduleHero v2.4.1 |
| Lizenz | AGPL-3.0 |
| Einbindung | Direkte Einbindung als Java-Bibliothek (JAR) in TourPlanner-Backend |
| Integrationstiefe | Tiefe Integration — scheduleHero-Klassen werden extensiv genutzt (>150 Aufrufe im Quellcode) |
| Abgetrennte Module | Nein — keine Trennung durch API/Middleware-Schicht |
| Weitergabe des TourPlanners | Nein (reine Eigennutzung bisher) |
| Netzwerknutzung durch Externe | Ja — Fahrer-App interagiert über REST-API mit TourPlanner |

### 3.2 Compliance-Status

| Pflicht (AGPL-3.0) | Erfüllt? | Begründung |
|---|---|---|
| Urheberrechtshinweis scheduleHero beibehalten | Nein | Keine NOTICE-Datei in TourPlanner-Deployment |
| Lizenztext AGPL-3.0 beigelegt | Nein | Nicht in Deployment-Paket |
| Netzwerk-Nutzern Quellcode angeboten | Nein | Fahrer-App bietet keinen Quellcode-Zugang |
| Vollständiger Quellcode TourPlanner offengelegt | Nein | TourPlanner ist proprietär behandelt |

**Ergebnis:** Frischetrans befindet sich in mehrfacher Verletzung der AGPL-3.0-Lizenzpflichten.

---

## 4. Rechtliche Risiken

### 4.1 Urheberechtsverletzung

Die Nicht-Einhaltung der AGPL-3.0-Bedingungen führt zum Erlöschen der Nutzungslizenz (sog. automatischer Lizenzterminus gemäß AGPL-3.0 § 8). Ohne gültige Lizenz stellt die Nutzung von scheduleHero eine **Urheberrechtsverletzung** dar:

- § 97 UrhG: Unterlassungsanspruch der Rechteinhaber von scheduleHero
- § 97a UrhG: Abmahnanspruch (anwaltliche Abmahnung mit Kostentragungspflicht)
- § 97 Abs. 2 UrhG: Schadensersatzanspruch (Lizenzanalogie oder tatsächlicher Schaden)

Die Rechteinhaberin von scheduleHero (nach Repository-Auswertung: ScheduleHero Foundation, registriert in den Niederlanden) hat Erfahrung mit der Durchsetzung von AGPL-Rechten. Entsprechende Durchsetzungsmuster sind aus vergleichbaren Fällen bekannt (vgl. GPL Enforcement News — gpl-violations.org).

### 4.2 Schadensersatz nach Lizenzanalogie

Im Falle einer Klage würde der Schadensersatz nach der Lizenzanalogiemethode berechnet: Was hätte der Rechteinhaber für eine kommerzielle Lizenz verlangt? Für vergleichbare Scheduling-Bibliotheken mit kommerziellem Einsatz sind Lizenzgebühren von 5.000–50.000 EUR p.a. marktüblich.

### 4.3 Reputationsrisiko

Eine erfolgreiche Abmahnung oder Klage durch die ScheduleHero Foundation würde zu öffentlicher Aufmerksamkeit führen und das ohnehin durch den Ransomware-Vorfall belastete Image von Frischetrans weiter schädigen.

---

## 5. Sofortmaßnahmen und Sanierungsoptionen

### Option A: Quellcode offenlegen (AGPL-Compliance)

TourPlanner wird vollständig unter AGPL-3.0 veröffentlicht, Quellcode auf einem öffentlichen Repository (z.B. GitHub) bereitgestellt, Nutzern der Fahrer-App ein Hinweis auf den Quellcode-Zugang gegeben.

**Vorteil:** Vollständige Compliance, keine Kosten für kommerzielle Lizenz.  
**Nachteil:** Offenlegung des TourPlanner-Quellcodes; kompetitiver Nachteil, wenn Konkurrenten die Anwendung analysieren.

### Option B: Kommerzielle Lizenz (Dual-Licensing)

Frischetrans erwirbt von der ScheduleHero Foundation eine kommerzielle Lizenz für scheduleHero, die die Nutzung in proprietären Anwendungen gestattet.

**Empfehlung:** RA Drosten nimmt Kontakt mit der ScheduleHero Foundation auf.

### Option C: Austausch der Komponente

scheduleHero wird durch eine funktional gleichwertige Scheduling-Bibliothek mit permissiver Lizenz (MIT, Apache 2.0) ersetzt.

**Vorteil:** Langfristige Unabhängigkeit.  
**Nachteil:** Entwicklungsaufwand (geschätzt 3–6 Monate, ca. 40.000–80.000 EUR Entwicklungskosten).

---

## 6. Empfehlung

RA Drosten empfiehlt folgendes Vorgehen:

1. **Sofortmaßnahme (binnen 7 Tagen):** Aussetzen der externen Netzwerkerreichbarkeit des TourPlanners für Fahrer-App (Trennung REST-API von extern) — damit entfällt die Netzwerk-Copyleft-Pflicht vorerst.

2. **Kurzfristig (30 Tage):** Aufnahme von Lizenzverhandlungen mit der ScheduleHero Foundation (Option B oder freiwillige Offenlegung).

3. **Mittelfristig (3–6 Monate):** Prüfung und ggf. Austausch der AGPL-Komponente (Option C), um eine dauerhaft risikofreie Nutzung zu gewährleisten.

4. **Sofort:** Durchführung eines vollständigen Open-Source-License-Audits des gesamten TourPlanner und aller weiteren Frischetrans-Eigenentwicklungen. Bekannte Audit-Tools: FOSSA, Black Duck, TLDR Legal.

---

## 7. Muster-Compliance-Hinweis für NOTICE-Datei (falls Option A gewählt)

```
This software includes scheduleHero v2.4.1
Copyright (C) 2022 ScheduleHero Foundation, Amsterdam (NL)
Licensed under the GNU Affero General Public License v3.0
https://www.gnu.org/licenses/agpl-3.0.html

The complete source code of this application (TourPlanner),
including the scheduleHero integration, is available at:
[URL — TBD]
```
