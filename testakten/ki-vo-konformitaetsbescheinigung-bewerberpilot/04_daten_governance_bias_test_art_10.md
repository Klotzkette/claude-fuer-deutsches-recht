# Daten-Governance und Bias-Test Art. 10 KI-VO

Stand: 16.05.2026

## 1. Datensätze

| Datensatz | Quelle | Umfang | Zweck | Status |
|---|---|---|---|---|
| D-Train-2024-HR | Historische Bewerbungen aus drei Pilotkunden, bereinigt | 48.200 Profile | Merkmalsextraktion und Rankingkalibrierung | Dokumentation unvollständig |
| D-Val-2025-General | Synthetisch angereicherte Lebensläufe | 12.000 Profile | Validierung | Plausibel |
| D-Test-2026-Care | Pflege- und Klinikprofile | 4.800 Profile | Domänentest Elbtal | Neu, noch nicht final freigegeben |
| D-Adverse-Set | Randfälle, Lücken, ungewöhnliche Lebensläufe | 1.200 Profile | Robustheit | In Aufbau |

## 2. Qualitätsmaßnahmen

- Duplikatprüfung.
- Entfernung direkter Merkmale wie Foto, Geburtsdatum, Familienstand, Religionsangabe.
- Maskierung sensibler Passagen.
- Labelprüfung durch zwei unabhängige Reviewer.
- Dokumentation von Datenherkunft und Einwilligungs-/Rechtsgrundlagenprüfung.

## 3. Bias-Test

Getestete Vergleichsgruppen sind nicht als Entscheidungsmerkmale im Modell enthalten. Sie werden nur für Fairnessanalyse und Qualitätskontrolle verwendet, soweit rechtlich zulässig und datenschutzrechtlich freigegeben.

Vorläufige Ergebnisse:

| Test | Ergebnis | Bewertung |
|---|---|---|
| Geschlechtsnahe Vornamen als Surrogat | Scoreabweichung 2,8 Prozentpunkte | Beobachten |
| Nicht-lineare Karriereverläufe | Scoreabweichung 7,4 Prozentpunkte | Maßnahme erforderlich |
| Sprachliche Nicht-Muttersprachlichkeit | Scoreabweichung 5,1 Prozentpunkte | Maßnahme erforderlich |
| Pflegeauslandserfahrung | Scoreabweichung 3,2 Prozentpunkte | Beobachten |

## 4. Offene Punkte

Die Trainingsdatenherkunft 2024 ist nicht für alle Pilotkunden gleich gut dokumentiert. Für eine finale Konformitätsbehauptung müssen die Datenliefervereinbarungen, Lösch-/Pseudonymisierungsprotokolle und Reviewer-Guidelines nachgelegt werden.

## 5. Entscheidung

Art.-10-Nachweis ist **noch gelb**. Das System kann nicht final bescheinigt werden, bevor die zwei Bias-Maßnahmen umgesetzt und die Datenherkunft geschlossen sind.
