---
name: ueberwachung-konkurrenten
description: "Laufende Überwachung neuer Patentanmeldungen von Konkurrenten der Mandantin. Definiert Watch-Profile pro Mandant mit Anmelder-Namen (inklusive Konzern-Toechter und ehemaliger Schreibweisen), CPC-IPC-Klassen, Schlagwoerter, Territorien. Laeuft als woechentlicher oder monatlicher Job in Espacenet S..."
---

# überwachung-konkurrenten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Watch-Profil

Pro Mandant ein Watch-Profil. Felder:

```yaml
mandant: Beispiel GmbH
profil_name: Watch_Beispiel_2026
anmelder:
 - "Siemens AG"
 - "Siemens Aktiengesellschaft" # alte Schreibweise
 - "Siemens Energy AG" # ehemalige Tochter, ggf. relevant
 - "Siemens Mobility GmbH"
 - "Siemens Healthineers AG"
klassen_cpc:
 - H02J 3/14
 - H02J 3/00
 - Y02E 60/00
schlagworte_und:
 - "lastmanagement"
 - "demand response"
schlagworte_oder:
 - "smart grid"
 - "intelligentes Netz"
territorien: [DE, EP, US, JP, CN, KR, WO]
zeitfenster: ab Anmeldetag 01.01.2024
publikationsstatus: [Anmeldung, Erteilung]
intervall: woechentlich
naechste_iteration: 27.05.2026
```

## Ablauf

### Initial-Lauf

1. Watch-Profil mit der Mandantin durchgehen — Konkurrenten benennen, Konzern-Töchter dazu, ehemalige Namen und Schreibvarianten ergänzen.
2. Klassen über `klassifikation-cpc-ipc` festlegen.
3. Schlagwörter aus dem Mandanten-Technikfokus.
4. Territorien aus den Märkten der Mandantin.
5. Erste Vollrecherche der letzten 24 Monate als Baseline — Treffer dokumentieren.
6. Intervall festlegen (wöchentlich / monatlich / vierteljährlich).

### Iteration

Pro Iteration (z. B. wöchentlich):

1. Espacenet Smart Search mit Anmelder + Klassen + Schlagwörter, Datumsfilter "neu seit letzter Iteration".
2. Google Patents Alert (wenn registriert) — Alternative: direkter Aufruf mit Filtern `assignee=`, `cpc=`, `after=`.
3. WIPO PATENTSCOPE für PCT-Anmeldungen.
4. USPTO PPUBS für US-Anmeldungen (mit `.AN.`-Feld für Assignee).
5. Delta-Liste bilden — nur **neue** Treffer seit letzter Iteration.

### Bewertung pro Treffer

Pro Treffer:

- **Relevant** (rot): Trifft Mandanten-Produkt direkt — Verletzungsrisiko, Einspruchschance.
- **Beobachtung** (gelb): Konkurrent ist in benachbartem Gebiet aktiv — Trendindikator.
- **Hintergrund** (grün): Nicht relevant, dokumentiert.

### Einspruchsfrist-Tracker

Bei Treffern mit Status "erteilt" Frist berechnen:

- **EP-Patent:** Art. 99 EPÜ — neun Monate ab Veröffentlichung der Erteilung.
- **DE-Patent:** § 59 PatG — drei Monate ab Veröffentlichung der Erteilung.

Frist im Output mit Stichtag dokumentieren.

### Quartalsbericht

Aggregierter Bericht alle drei Monate mit:

- Anzahl neuer Treffer je Konkurrent
- Schwerpunkt-Klassen
- Auffällige Anmeldetrends
- Aktuelle Einspruchsfristen
- Empfehlungen (Einspruch / FTO-Recherche / Beobachtung)

## Hinweise

- **Konzern-Töchter.** Konkurrenten melden oft über Tochterfirmen an. Vor jedem Lauf prüfen, ob neue Töchter entstanden sind, die ergänzt werden sollten.
- **Strohmann-Anmeldungen.** Manche Konzerne melden über Anwaltskanzleien oder Trustees an, um die Verbindung zu verschleiern. Hier hilft nur Recherche über Klassen + Schlagwörter, nicht über Anmeldername.
- **Bezahl-Alerts.** PatBase Alert, Orbit, Patsnap und IPlytics bieten leistungsfähigere Alerts — vor allem für große Mandanten lohnt sich die Kombination mit dem frei zugänglichen Watch.
- **Datenverzögerung.** Veröffentlichung erfolgt 18 Monate nach Prioritätstag. Konkurrenz-Anmeldungen werden also erst 1,5 Jahre nach dem Anmeldetag sichtbar.
- **Nicht-Patent-Literatur.** Ergänzend Google Scholar Alerts und Konferenz-Listings (IEEE, ACM) — Konkurrenten reden oft schon auf Konferenzen, bevor die Anmeldung publiziert ist.

## Disclaimer

> **Hinweis zur Überwachung.** Diese laufende Überwachung ist eine KI-gestützte Vorrecherche. Vollständigkeit kann nicht garantiert werden — insbesondere bei Konzern-Konstruktionen mit Tochterfirmen ohne klare Namens-Bindung, bei Strohmann-Anmeldungen und bei Anmeldungen in nicht durchsuchten Klassen oder Sprachen. Einspruchsfristen sind durch die Patentanwältin in einer eigenständigen Prüfung der Veröffentlichungsdaten zu verifizieren bevor die Frist als verbindlich eingetragen wird.

## Triage-Fragen vor Konkurrenten-Ueberwachung

Bevor die Monitoring-Konfiguration eingerichtet wird, klaere:
1. Sind alle relevanten Konkurrenten-Anmelder-Namen (inkl. Tochtergesellschaften und Strohmann-Kanzleien) erfasst?
2. Welche CPC/IPC-Klassen und Schlüsselbegriffe sollen für das Keyword-Monitoring eingesetzt werden?
3. Ist eine Einspruchsfrist-Ueberwachung (9 Monate nach Erteilung, § 59 PatG / Art. 99 EPU) eingerichtet?
4. Wird die 18-Monats-Veroeffentlichungsverzoegerung in der Strategieplanung beruecksichtigt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Technische Beschwerdekammer, T 328/87 (Drittbeobachtungen):** Im EPA-Erteilungsverfahren können Dritte Beobachtungen (Art. 115 EPU) einreichen, ohne am Verfahren beteiligt zu werden; durch fruehzeitige Beobachtung können relevante Entgegenhaltungen in das Prüfungsverfahren eingebracht werden, bevor ein formeller Einspruch noetig wird.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Maßnahme: Datum und Leitsatz korrigiert auf tatsaechlichen Inhalt.
Quelle: dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.09.2017&Aktenzeichen=X+ZB+1%2F17
-->
