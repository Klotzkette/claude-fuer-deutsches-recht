---
name: neuheit-pruefen
description: "Prueft Neuheit nach § 3 PatG und Art. 54 EPUe. Methodisches Schema: ein Anspruch wird in seine Merkmale zerlegt und Merkmal-fuer-Merkmal gegen genau eine Entgegenhaltung verglichen. Neuheitsschaedlich ist nur die vollstaendige Vorwegnahme aller Merkmale in einer einzigen Entgegenhaltung (kein Mosaik). Beruecksichtigt die EPA-Konzepte unmittelbare und eindeutige Offenbarung implizite Offenbarung und unzulaessige Auswahlerfindungen. Erzeugt Merkmalsanalyse-Tabelle pro Entgegenhaltung. Bewertet jedes Merkmal als offenbart nicht offenbart oder implizit offenbart mit Pinpoint. Gibt Gesamtergebnis und Empfehlung an die Patentanwaeltin. Disclaimer keine amtliche Pruefung."
---

# neuheit-prüfen

## Zweck

Prüft, ob ein konkreter Anspruch (Mandantin oder Drittpatent) gegenüber konkreten Entgegenhaltungen **neu** ist. Genaues Werkzeug, das auf den Vorrecherche-Treffern aufsetzt.

## Rechtsrahmen

- **§ 3 PatG.** Eine Erfindung gilt als neu, wenn sie nicht zum Stand der Technik gehört.
- **Art. 54 EPÜ.** Wortgleich für das EPA.
- **EPA-Beschwerdekammern-Doktrin:**
  - **Unmittelbare und eindeutige Offenbarung** — eine Entgegenhaltung nimmt einen Anspruch nur dann vorweg, wenn alle Merkmale **direkt und unmittelbar erkennbar** sind (G 2/88, T 305/87).
  - **Implizite Offenbarung** — ein Merkmal ist implizit offenbart, wenn der Fachmann es zwingend mitliest (G 2/10 zu Disclaimern, T 6/80).
  - **Auswahlerfindungen** — Auswahl eines Sub-Bereichs aus einem offenbarten Bereich kann neu sein, wenn (1) der Sub-Bereich eng ist, (2) abseits des präferierten Bereichs der Entgegenhaltung liegt, (3) eine eigene technische Lehre vermittelt (T 198/84, T 279/89).
- **Kein Mosaik** — anders als bei der erfinderischen Tätigkeit darf bei der Neuheitsprüfung **nicht** kombiniert werden. Ein Anspruch wird gegen **genau eine** Entgegenhaltung geprüft. Mehrere Entgegenhaltungen lassen sich nur kombinieren, wenn die eine ausdrücklich auf die andere verweist und der Fachmann beide unmittelbar zusammenliest (T 153/85).

## Ablauf

### Schritt 1: Anspruch zerlegen

Aufbau einer Merkmalsanalyse-Tabelle. Der Hauptanspruch wird in **Merkmale** zerlegt — jeder grammatikalisch und technisch eigenständige Bestandteil ist ein Merkmal. Beispiel:

```
Anspruch 1 — Vorrichtung zum Lastmanagement in einem Energieversorgungsnetz:
M1: ein Energieversorgungsnetz mit mindestens einer Quelle und mindestens einem Verbraucher,
M2: ein Steuergerät, das mit der Quelle und dem Verbraucher verbunden ist,
M3: wobei das Steuergerät einen Speicher für historische Lastdaten umfasst,
M4: wobei das Steuergerät eingerichtet ist, anhand eines Prognosemodells einen Soll-Lastpfad zu bestimmen,
M5: wobei das Steuergerät eingerichtet ist, bei Abweichung des Ist-Lastpfads vom Soll-Lastpfad einen Eingriff in den Verbraucher auszuloesen,
M6: dadurch gekennzeichnet, dass das Prognosemodell ein neuronales Netzwerk mit mindestens drei Schichten umfasst.
```

### Schritt 2: Pro Entgegenhaltung eine Tabelle

Pro Entgegenhaltung Spalte „offenbart / nicht offenbart / implizit offenbart" mit Pinpoint:

| Merkmal | EP 3 456 789 A1 | Pinpoint |
| --- | --- | --- |
| M1 | offenbart | Abs. [0001], Fig. 1 (Bezugszeichen 1, 2, 3) |
| M2 | offenbart | Abs. [0012], Fig. 1 (Bezugszeichen 4) |
| M3 | offenbart | Abs. [0014], Bezugszeichen 5 |
| M4 | offenbart | Abs. [0016]: „Prognosemodell" |
| M5 | offenbart | Abs. [0020]–[0022] |
| M6 | **nicht offenbart** | — Modell ist linear, kein neuronales Netz |

### Schritt 3: Bewertung pro Entgegenhaltung

- **Alle Merkmale offenbart** → Anspruch ist gegenüber dieser Entgegenhaltung **nicht neu**, neuheitsschädlich.
- **Mindestens ein Merkmal nicht offenbart** → Anspruch ist gegenüber dieser Entgegenhaltung **neu**. Die Entgegenhaltung kann aber für die erfinderische Tätigkeit (§ 4 PatG) relevant bleiben.
- **Implizite Offenbarung** kennzeichnen — kritisch bewerten (Beweislast hoch).
- **Auswahlerfindung** — wenn der Anspruch einen Sub-Bereich aus einem in der Entgegenhaltung offenbarten Bereich auswählt, prüfen, ob die T-198/84-Kriterien greifen.

### Schritt 4: Gesamt-Bewertung

Tabelle aller Entgegenhaltungen mit Bewertungsspalte:

| Entgegenhaltung | Neuheitsschaedlich? | Bemerkung |
| --- | --- | --- |
| EP 3 456 789 A1 | nein | M6 nicht offenbart, lineares Modell statt neuronalem Netz |
| US 2020/0123456 A1 | ja | alle Merkmale Anspruch 1 + Abs. [0034] |
| WO 2019/123456 A1 | nein | M4 und M6 nicht offenbart |

### Schritt 5: Folgen

- **Mindestens eine neuheitsschädliche Entgegenhaltung** → Empfehlung an Patentanwältin: Anspruch umformulieren (Aufnahme weiterer Merkmale aus der Beschreibung, Beschränkung auf Sub-Konfigurationen), oder Anmeldung in dieser Form nicht aufrechterhalten.
- **Keine neuheitsschädliche Entgegenhaltung** → weiter zu `erfinderische-taetigkeit-pruefen`. Neuheit allein reicht nicht.

## Hinweise

- **Sprache des Anspruchs** spielt eine Rolle. „Umfassend" ist offen (weitere Bauteile möglich), „bestehend aus" ist abgeschlossen. Bei der Merkmalsanalyse exakt am Wortlaut bleiben.
- **Funktionale Merkmale** (z. B. „eingerichtet, X zu tun") sind in der Auslegung delikat. EPA-Praxis: Eine Vorrichtung, die geeignet ist, X zu tun, nimmt das funktionale Merkmal vorweg (T 219/89, T 1090/12) — die Mandantin sollte daher nicht zu weit funktional formulieren.
- **Zahlenbereiche** (M6 „mindestens drei Schichten") — eine Entgegenhaltung mit „zwei Schichten" nimmt M6 nicht vorweg. Eine Entgegenhaltung mit „beliebige Anzahl von Schichten" nimmt M6 vorweg.
- **Kombinationen aus zwei Entgegenhaltungen** sind in der Neuheitsprüfung verboten (T 153/85). Wenn die Mandantin nur dann neuheitsschädlich getroffen wird, wenn man Entgegenhaltung A mit Entgegenhaltung B mosaikartig zusammenfügt → Neuheit ist gegeben, Frage verschiebt sich zur erfinderischen Tätigkeit.

## Disclaimer

> **Hinweis zur Prüfung.** Diese Neuheitsprüfung ist eine KI-gestützte Vorprüfung und keine amtliche Prüfung durch DPMA oder EPA. Die Bewertung als „neu" oder „nicht neu" ist eine Einschätzung anhand der Recherche-Treffer; die amtliche Prüfung kann zu anderen Ergebnissen kommen, weil weitere oder andere Entgegenhaltungen gefunden werden oder die Auslegung des Anspruchs anders ausfällt.
