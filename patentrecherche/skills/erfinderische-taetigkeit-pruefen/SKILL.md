---
name: erfinderische-taetigkeit-pruefen
description: "Prüft erfinderische Tätigkeit nach § 4 PatG und Art. 56 EPUe mit dem Problem-Solution-Approach der EPA-Beschwerdekammern. Drei Stufen: (1) Bestimmung des naechstliegenden Stands der Technik (closest prior art) anhand technischer Naehe Zweckverwandschaft und gemeinsamer Merkmale; (2) Formulierung der objektiven technischen Aufgabe (objective technical problem) als das was die Erfindung löst und der naechstliegende Stand der Technik nicht; (3) Frage nach could-would am Tag der Anmeldung haette der Fachmann ausgehend vom naechstliegenden Stand der Technik mit Erwartung auf Erfolg die beanspruchte Lösung umgesetzt. Berücksichtigt Sekundaerindizien wie technisches Vorurteil unerwartete Wirkung lange empfundenes Bedürfnis und kommerziellen Erfolg. Disclaimer keine amtliche Prüfung."
---

# erfinderische-tätigkeit-prüfen

## Zweck

Prüft, ob ein Anspruch — typischerweise nachdem die Neuheit bejaht wurde — auf einer **erfinderischen Tätigkeit** beruht. Im EPA-Sprachgebrauch ist die erfinderische Tätigkeit der zentrale Knackpunkt der Patentprüfung.

## Rechtsrahmen

- **§ 4 PatG.** Eine Erfindung gilt als auf einer erfinderischen Tätigkeit beruhend, wenn sie sich für den Fachmann nicht in naheliegender Weise aus dem Stand der Technik ergibt.
- **Art. 56 EPÜ.** Wortgleich für das EPA.
- **Geheime ältere Anmeldungen** (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ) sind **nicht** für die erfinderische Tätigkeit relevant — sondern nur für die Neuheit.
- **EPA-Methodik:** **Problem-Solution-Approach** (PSA). Bindend für die EPA-Prüfung und EPA-Beschwerdekammer-Rechtsprechung; in der DPMA- und BPatG-Praxis ebenfalls maßgeblich, wenn auch nicht so dogmatisch.

## Problem-Solution-Approach in drei Stufen

### Stufe 1: Nächstliegender Stand der Technik (closest prior art)

Aus den Recherche-Treffern wird **eine** Entgegenhaltung als nächstliegender Stand der Technik bestimmt. Kriterien:

- **Gleicher Zweck / gleiches technisches Gebiet** wie die Erfindung.
- **Hohe Übereinstimmung** in den Merkmalen (möglichst viele M1, M2, … sind offenbart).
- **Klare technische Lehre**, von der ausgehend der Fachmann an die Erfindung herangehen könnte.

Wenn mehrere Entgegenhaltungen in Frage kommen: zur Plausibilitätskontrolle den PSA **für jede** durchgehen — wenn ausgehend von **einer** der Anspruch naheliegend ist, fehlt die erfinderische Tätigkeit (EPA-Praxis: T 967/97, T 21/08).

### Stufe 2: Objektive technische Aufgabe

Differenz zwischen Anspruch und nächstliegendem Stand der Technik bilden — die **unterscheidenden Merkmale**. Aus diesen unterscheidenden Merkmalen wird die **technische Wirkung** abgeleitet und als "**objektive technische Aufgabe**" formuliert:

> Wie kann der nächstliegende Stand der Technik so weiterentwickelt werden, dass [technische Wirkung]?

Wichtig: Die Aufgabe wird **objektiv aus der Erfindung heraus** formuliert — nicht aus der Mandanten-Erzählung. Wenn die Mandantin ein Problem nennt, das der nächstliegende Stand der Technik schon löst, ist es nicht die objektive Aufgabe. **Verbot der rückschauenden Betrachtung** (ex-post-facto-Argumentation, T 24/81).

### Stufe 3: Could-Would-Frage

Hätte der **Fachmann** am Anmeldetag / Prioritätstag — **ausgehend vom nächstliegenden Stand der Technik** — die objektive Aufgabe so gelöst, wie der Anspruch sie löst?

Nicht: **könnte** (could). Sondern: **würde** (would). Der Fachmann muss eine **Motivation** gehabt haben, die anderen Entgegenhaltungen heranzuziehen, mit **Erwartung auf Erfolg**.

Die Frage hat zwei Teilaspekte:

1. **Steht es im Stand der Technik?** Gibt es eine andere Entgegenhaltung, die das fehlende Merkmal lehrt?
2. **Hätte der Fachmann zugegriffen?** Gibt es eine Anregung ("pointer", "teaching", "suggestion") in der Entgegenhaltung oder im allgemeinen Fachwissen, die den Fachmann von Entgegenhaltung A zu Entgegenhaltung B führt?

## Ablauf

### 1. Recherche-Treffer aus `stand-der-technik-recherche` einlesen

Mit Recherchezeichen (X, Y, A, P, E). Y-Treffer sind die wichtigsten für die erfinderische Tätigkeit.

### 2. Closest Prior Art bestimmen

Begründete Auswahl mit Erklärung, warum dieser Treffer am nächsten liegt (technisches Gebiet, gemeinsame Merkmale).

### 3. Merkmals-Differenz bilden

Tabelle der unterscheidenden Merkmale gegenüber dem Closest-Prior-Art-Dokument. Beispiel:

| Merkmal | im CPA offenbart? | Unterscheidend? |
| --- | --- | --- |
| M1 — Energieversorgungsnetz | ja | nein |
| M2 — Steuergerät | ja | nein |
| M3 — Speicher für Lastdaten | ja | nein |
| M4 — Soll-Lastpfad über Prognosemodell | ja (linear) | teilweise |
| M5 — Eingriff bei Abweichung | ja | nein |
| M6 — Neuronales Netz mit drei Schichten | **nein** | **ja** |

### 4. Technische Wirkung der unterscheidenden Merkmale

"Was bringt M6?" — z. B.: bessere Vorhersagegenauigkeit bei nicht-linearen Lastprofilen, robuster gegenüber Lastspitzen, Stabilität ohne manuelle Parameter-Tuning.

### 5. Objektive technische Aufgabe formulieren

> Wie kann das Lastmanagement-System aus EP 3 456 789 A1 so weiterentwickelt werden, dass bei nicht-linearen Lastprofilen eine genauere Prognose erzeugt wird?

### 6. Could-Would-Prüfung

Recherche-Treffer durchgehen — gibt es eine Entgegenhaltung, die neuronale Netze für Lastprognose lehrt? Wenn ja:

- **Stand der Technik:** ja, z. B. WO 2017/123 — neuronale Netze für Energieprognose.
- **Motivation:** Stand der Technik nennt explizit, dass neuronale Netze bei nicht-linearen Lastprofilen genauer sind als lineare Modelle.
- **Erwartung auf Erfolg:** ja, weil der Stand der Technik die Anwendung in vergleichbaren Energienetzen schon zeigt.

→ **Ergebnis:** Der Fachmann hätte ausgehend von EP 3 456 789 A1 mit Anregung aus WO 2017/123 mit Erwartung auf Erfolg den Weg von Anspruch 1 beschritten. **Erfinderische Tätigkeit fraglich**, Anspruch sollte engerer gefasst werden (z. B. Spezifikum des Trainingsverfahrens, Kombination mit weiteren Merkmalen).

Oder, wenn keine Anregung besteht: **Erfinderische Tätigkeit liegt vor.**

## Sekundärindizien

Wenn die Could-Would-Prüfung nahelegend ausfällt, aber dennoch Zweifel bestehen — Sekundärindizien einsetzen (EPA-Beschwerdekammern: Vorsicht, Sekundärindizien dürfen die Hauptprüfung nicht ersetzen, T 1212/01):

- **Technisches Vorurteil** überwunden — die Fachwelt hat eine bestimmte Lösung jahrelang abgelehnt.
- **Unerwartete technische Wirkung** — die Erfindung bringt ein Mehr, das der Stand der Technik nicht erwarten ließ (T 21/81).
- **Lang empfundenes Bedürfnis** — das Problem ist seit Jahren bekannt, aber unbehoben.
- **Kommerzieller Erfolg** — schwach, aber zulässig, wenn er auf den technischen Merkmalen beruht (T 270/84).
- **Scheitern anderer** — frühere Anmeldungen oder Veröffentlichungen, die das Problem nicht lösen konnten.

## Hinweise

- **EPA-Standardphrase:** "Could-would-approach." Im DPMA-/BPatG-Verfahren weniger formelhaft, aber inhaltlich gleich.
- **Mehrfach-PSA.** Wenn mehrere CPA-Kandidaten denkbar: PSA für jeden, schwächste Position für die Mandantin maßgeblich.
- **Mosaike** sind hier — anders als bei der Neuheit — **zulässig**, aber nur, wenn der Fachmann eine Verbindung gezogen hätte (Pointer aus CPA, allgemeines Fachwissen).
- **Hindsight-Verbot.** Die Argumentation darf nicht auf die Mandanten-Anmeldung zurückblicken ("wenn man weiß, wie es geht, ist es immer leicht").
- **Fachmann ist Konstrukt** — die für das technische Gebiet zuständige Fachperson mit durchschnittlichen Kenntnissen und Zugang zum gesamten Stand der Technik. Bei interdisziplinären Erfindungen: **Fachteam** (T 32/81).

## Disclaimer

> **Hinweis zur Prüfung.** Diese Prüfung der erfinderischen Tätigkeit ist eine KI-gestützte Vorprüfung und keine amtliche Prüfung durch DPMA oder EPA. Der Problem-Solution-Approach ist methodisch sensibel — die Auswahl des nächstliegenden Stands der Technik kann die Bewertung entscheidend verschieben. Die Prüfung muss durch eigene Bewertung und durch Prüfung der Recherche-Vollständigkeit abgesichert werden.

## Triage-Fragen vor Pruefung erfinderischer Taetigkeit

Bevor der Problem-Solution-Approach angewendet wird, klaere:
1. Welche Entgegenhaltung ist der naechstliegende Stand der Technik (CPA — Closest Prior Art)?
2. Welches technische Problem loest die Erfindung ausgehend vom CPA?
3. Sind Sekundaerindizien vorhanden (unerwarteter technischer Effekt, ueberwundenes technisches Vorurteil, lang empfundenes Beduerfnis)?
4. Sind alle Merkmale des Hauptanspruchs in der PSA beruecksichtigt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Technische Beschwerdekammer, T 21/81 (Unerwarteter technischer Effekt):** Ein unerwarteter technischer Effekt, der ueber das aus dem Stand der Technik Vorhersehbare hinausgeht, ist ein Indiz fuer erfinderische Taetigkeit; er muss im Anspruch oder in der Beschreibung hinreichend offenbart sein.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
