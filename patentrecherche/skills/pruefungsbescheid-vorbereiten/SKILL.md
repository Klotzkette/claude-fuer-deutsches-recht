---
name: pruefungsbescheid-vorbereiten
description: "Bereitet Antwort auf Pruefungsbescheid des DPMA nach § 45 PatG oder des EPA nach Art. 94 EPUe systematisch vor. Liest den Bescheid und die zitierten Entgegenhaltungen ein. Strukturiert pro Beanstandung: Beanstandung wortlautgetreu zitiert betroffener Anspruch zitierte Entgegenhaltung mit Pinpoint Argumentationsvorschlag (Neuheit-Argument erfinderische Taetigkeit Argument Anspruchsanpassung). Beruecksichtigt EPA-Schemata Problem-Solution-Approach und EPA-Hinweise auf clarity (Art. 84 EPUe) added subject-matter (Art. 123(2) EPUe) und unity (Art. 82 EPUe). Liefert Entwurf der Eingabe mit Argumentationsstruktur und Anspruchssatz-Vorschlaegen. Disclaimer Eingabe muss durch Patentanwaeltin gegengelesen und verantwortet werden."
---

# prüfungsbescheid-vorbereiten

## Zweck

Wenn DPMA oder EPA einen **Prüfungsbescheid** erlässt, muss die Patentanwältin innerhalb der gesetzten Frist (typisch 4 Monate, verlängerbar) antworten. Dieses Skill strukturiert die Antwort.

## Rechtsrahmen

- **§ 45 PatG.** DPMA-Prüfungsbescheid.
- **§ 47 PatG.** Anhörung.
- **Art. 94 Abs. 3 EPÜ + Regel 71(3) EPÜ.** EPA-Prüfungsbescheid.
- **Häufige EPA-Beanstandungen:**
  - **Art. 54 EPÜ** — Neuheit
  - **Art. 56 EPÜ** — Erfinderische Tätigkeit
  - **Art. 84 EPÜ** — Klarheit (clarity) und Stütze in der Beschreibung
  - **Art. 123(2) EPÜ** — Verbot der Erweiterung über den ursprünglichen Offenbarungsgehalt (added subject-matter)
  - **Art. 82 EPÜ** — Einheitlichkeit (unity of invention)
  - **Art. 83 EPÜ** — Ausführbarkeit (sufficiency of disclosure)
  - **Art. 76(1) EPÜ** — bei Teilanmeldungen: keine Erweiterung der Stammanmeldung
- **DPMA-Beanstandungen** sind inhaltlich vergleichbar, formal sparsamer.

## Eingaben

- **Prüfungsbescheid** als PDF / Volltext.
- **Anmeldungsunterlagen** in der eingereichten Fassung (Ansprüche, Beschreibung, Zeichnungen).
- **Zitierte Entgegenhaltungen** (X / Y / A im EPA-Bescheid; D1, D2, … in den EPA-Sprachregeln).
- **Bereits geführte Korrespondenz** (vorheriger Bescheid, vorherige Antwort).
- **Frist** für die Antwort.

## Ablauf

### Schritt 1: Bescheid lesen und strukturieren

Jede Beanstandung als eigene Position erfassen:

```
Beanstandung 1: Art. 54 EPUe / Anspruch 1
  D1 = EP 3 456 789 A1, Siemens AG
  Pinpoint: Anspruch 1, Abs. [0023], Fig. 1
  Argument der Prüfungsabteilung: alle Merkmale von Anspruch 1 sind in D1 offenbart.
  
Beanstandung 2: Art. 56 EPUe / Anspruch 2
  D1 + D2 (US 2020/0123456)
  Argument: ausgehend von D1 würde der Fachmann mit Anregung aus D2 zur beanspruchten Lösung gelangen.
  
Beanstandung 3: Art. 84 EPUe / Anspruch 3
  Argument: Merkmal "im Wesentlichen" ist unklar.
  
Beanstandung 4: Art. 123(2) EPUe / Beschreibung Abs. [0034]
  Argument: Änderung gegenüber urspruenglich eingereichter Fassung unzulässig erweitert.
```

### Schritt 2: Pro Beanstandung Strategie wählen

#### Bei Art. 54 (Neuheit)

- Wenn Pinpoint der Prüfungsabteilung **richtig**: Anspruch beschränken (Merkmale aus der Beschreibung aufnehmen, die in D1 nicht offenbart sind). Über `neuheit-pruefen` neue Merkmalsanalyse machen.
- Wenn Pinpoint **falsch**: argumentieren, dass das Merkmal in D1 nicht offenbart ist. Beleg über Verweis auf den genauen Wortlaut von D1.
- **Auswahlerfindung** ggf. argumentieren (T 198/84, T 279/89), wenn der Anspruch einen Sub-Bereich aus einem in D1 offenbarten Bereich auswählt.

#### Bei Art. 56 (Erfinderische Tätigkeit)

- **Closest Prior Art** der Prüfungsabteilung akzeptieren oder begründet bestreiten.
- **Objektive technische Aufgabe** neu / präziser formulieren (häufig hat die Prüfungsabteilung zu allgemein formuliert).
- **Could-Would** widerlegen: keine Anregung in D1 oder D2, gegen die beanspruchte Lösung gerichtetes Vorurteil, unerwartete Wirkung. Sekundärindizien einsetzen, aber **nicht** als Hauptargument (T 1212/01).
- Wenn Argumente nicht tragen: Anspruch beschränken oder Auxiliary Requests (Hilfsanträge) formulieren.

#### Bei Art. 84 (Klarheit)

- **Unklare Begriffe** definieren oder ersetzen (z. B. „im Wesentlichen" → konkrete Toleranz „±5 %").
- **Stütze in der Beschreibung** zeigen — auf Stellen der Beschreibung verweisen.

#### Bei Art. 123(2) (Added Subject-Matter)

- **Goldstandard** (G 2/10): jede Änderung muss in der ursprünglich eingereichten Anmeldung **unmittelbar und eindeutig** offenbart sein.
- Geänderte Stelle auf ursprünglichen Offenbarungsgehalt zurückführen (Pinpoint auf ursprünglich eingereichten Text).
- Wenn nicht möglich: Änderung zurücknehmen, Anspruch anders formulieren.

#### Bei Art. 82 (Einheitlichkeit)

- Argumentieren, dass die unterschiedlichen Ansprüche durch eine **gemeinsame erfinderische Idee** (single inventive concept) verbunden sind.
- Wenn nicht: **Teilanmeldung** (§ 39 PatG / Art. 76 EPÜ) erwägen, bevor die Stammanmeldung erteilt wird.

#### Bei Art. 83 (Ausführbarkeit)

- Zusätzliche Ausführungsbeispiele in der Beschreibung markieren (keine Erweiterung über Art. 123(2)).
- Falls Erfindung tatsächlich nicht ausführbar offenbart ist: kritisch — Anmeldung möglicherweise nicht haltbar.

### Schritt 3: Anspruchssatz-Vorschläge

- **Hauptantrag** (main request): neue Anspruchsfassung, die alle Beanstandungen ausräumt.
- **Hilfsanträge** (auxiliary requests): in EPA-Praxis empfohlen — gestaffelt enger formulierte Fassungen. Erstes Hilfsantrags-Set: nur leichte Einschränkungen. Zweites Hilfsantrags-Set: enger. Drittes: noch enger.
- **Hilfsanträge dokumentieren**, damit die Patentanwältin sie nur freischalten muss.

### Schritt 4: Entwurf der Eingabe

Aufbau der Eingabe an die Prüfungsabteilung:

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht der Anmelderin nehmen wir zu dem Prüfungsbescheid
vom [Datum] wie folgt Stellung. Beigefuegt sind neue Anspruchsfassungen
(Hauptantrag und Hilfsanträge 1-3).

I. Allgemeines
   [Bezugnahme, Änderungen im Überblick]

II. Zu den einzelnen Beanstandungen

   1. Art. 54 EPUe, Anspruch 1
      [Argument, Pinpoint, ggf. Anspruchsbeschraenkung]

   2. Art. 56 EPUe, Anspruch 1
      Problem-Solution-Approach:
      Closest Prior Art: D1 (EP 3 456 789 A1)
      Objektive technische Aufgabe: [neu / präzisiert]
      Could-Would-Analyse: [Argument]
      Sekundaerindizien: [optional]

   3. Art. 84 EPUe, Anspruch 3
      [Klarstellung, neue Anspruchsfassung]

   4. Art. 123(2) EPUe, Beschreibung Abs. [0034]
      [Änderung zurückgenommen / auf urspruenglichen Offenbarungsgehalt zurückgeführt]

III. Anspruchsfassungen
   Hauptantrag - Ansprueche 1-15
   Hilfsantrag 1 - Ansprueche 1-12
   Hilfsantrag 2 - Ansprueche 1-10
   Hilfsantrag 3 - Ansprueche 1-7

IV. Wir beantragen
   Erteilung des Patents auf Grundlage des Hauptantrags, hilfsweise auf
   Grundlage des jeweils nächsten Hilfsantrags.

Mit freundlichen Grüßen
[Patentanwältin]
```

### Schritt 5: Frist-Tracking

- **EPA:** 4 Monate ab Zustellung. Verlängerung um 2 Monate möglich (Art. 132 EPÜ + R. 132 EPÜ). Versäumte Frist: Weiterbehandlungsantrag (Art. 121 EPÜ), Wiedereinsetzung (Art. 122 EPÜ).
- **DPMA:** Frist nach § 45 PatG, in der Regel 2-4 Monate. Verlängerung möglich.

## Hinweise

- **EPA-typische Argumente:** „No pointer in D1 to D2", „D1 teaches away from the claimed solution", „unexpected technical effect".
- **Hilfsanträge** sollten so formuliert sein, dass sie inhaltlich noch sinnvoll bleiben — keine Überengung, die das Patent wirtschaftlich wertlos macht.
- **Auxiliary Requests** sind im EPA-Verfahren Standard. Im DPMA-Verfahren formal nicht zwingend, aber inhaltlich übernehmbar.
- **Bei Anhörung** (§ 47 PatG / Art. 116 EPÜ): die Eingabe ist die schriftliche Grundlage. Hilfsanträge müssen vorab eingereicht werden.

## Disclaimer

> **Hinweis zum Bescheid.** Dieser Entwurf zur Beantwortung des Prüfungsbescheids ist eine KI-gestützte Vorarbeit. Die Argumentationsstruktur und die Anspruchsentwuerfe müssen durch die Patentanwältin vor Absendung sorgfaeltig gegengelesen werden. Insbesondere die Bewertung der erfinderischen Tätigkeit und die Wahl der Hilfsantragsabstufungen erfordern individuelle Bewertung. Diese Vorbereitung ersetzt nicht die anwaltliche Verantwortung gegenüber Amt und Mandant.

## Triage-Fragen bei Pruefungsbescheid

Bevor die Antwort auf den Pruefungsbescheid formuliert wird, klaere:
1. Welche Einwaende werden geltend gemacht — Neuheit, erfinderische Taetigkeit, mangelnde Klarheit (Art. 84 EPU/§ 34 PatG) oder Offenbarung (Art. 83 EPU/§ 35 PatG)?
2. Laeuft die 4-Monats-EPA-Frist (verlängerbar um 2 Monate) noch, oder ist eine Fristverlängerung erforderlich?
3. Wurden Hilfsantraege vorbereitet (abgestufter Schutzbereich fuer den Fall, dass Hauptantrag nicht haltbar)?
4. Sind alle in der Entgegenhaltung genannten Merkmale korrekt in der Anspruchsanalyse beruecksichtigt?

## Aktuelle Rechtsprechung

> **BGH, Urt. v. 12.09.2013 — X ZR 22/10 (Anspruchsaenderung im Pruefungsverfahren):** Im Erteilungsverfahren koennen Patentansprueche geaendert werden, sofern die Aenderung durch die urspruengliche Offenbarung gestuetzt ist (§ 38 PatG / Art. 123 EPU); eine Erweiterung uber den ursprunglich offenbarten Gegenstand hinaus fuehrt zur Nichtigkeit des Patents.

> **EPA, Erweiterte Beschwerdekammer, G 2/21 (Plausibilitaet):** Die technische Wirkung, auf die eine erfinderische Taetigkeit gestuetzt wird, muss in der Anmeldung plausibel offenbart sein; spaetere Versuchsbelege koennen die Plausibilitaet ersetzen, wenn der Fachmann den Effekt nachtraeglich als glaubhaft bestaetigt ansehen kann.

> **BGH, Urt. v. 14.10.2010 — Xa ZR 36/08 (Hilfsantrag EPA):** Im EPA-Beschwerdeverfahren spaetest eingereichte Hilfsantraege koennen als verspaetet zurueckgewiesen werden; die Pruefungstaktik muss daher fruehzeitig eine vollstaendige Hilfsantragsstaffel vorbereiten, auch wenn der Hauptantrag als verteidbar erscheint.
