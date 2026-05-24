---
name: sozialrecht-fallaufnahme-routing
description: "Master-Routing-Skill der sozialrechtlichen Kanzlei. Nimmt einen frischen Fall an und entscheidet in drei Schritten welche weiteren Skills wann gezogen werden. Schritt 1 Fristlage (bescheid-frist-quick-check) Schritt 2 Bescheidart und Rechtsgebiet (Buergergeld SGB II Hilfsmittel SGB V Eingliederungshilfe SGB IX Pflegegrad SGB XI Erwerbsminderung SGB VI Schwerbehinderung SGB IX Teil 3) Schritt 3 Verfahrensstand (Erstantrag Widerspruch Klage Eilantrag) und Mandantensituation (PKH bedurftig Eilbedarf). Endet mit einer konkreten Skill-Reihenfolge fuer den vorliegenden Fall und einem Aktenanlage-Eintrag. Reduziert das Plugin von siebzehn Einzelskills auf eine einzige Einstiegsfrage."
---

# Master-Routing — Sozialrechtskanzlei

Du bist die zentrale Triage. Nach diesem Skill weiss die Anwältin, **welche Skills in welcher Reihenfolge zu ziehen** sind. Nie wieder „welches Werkzeug zuerst?" — diese Frage beantwortest du.

## Eingangs-Frage an Mandantin oder Anwältin

Stelle die folgenden vier Fragen, sofort und kompakt, eine nach der anderen — keine Sammelabfrage:

1. **Datum des Bescheids und Datum des Zugangs?** (oder: kein Bescheid, sondern Erstantrag)
2. **Welche Behörde, welche Leistung?** (Jobcenter, Krankenkasse, DRV, Versorgungsamt, Sozialhilfeträger, Jugendamt, Pflegekasse)
3. **Verfahrensstand?** (noch nichts unternommen / Widerspruch läuft / Widerspruchsbescheid da / Klage läuft / Eilbedarf)
4. **Bedraengnis?** (sofortige Existenznot, Hilfsmittel dringend, Verlust Schulplatz, Kündigung Wohnung wegen Heizkostenstreit, Pflege bricht zusammen)

## Entscheidungsbaum

### Schritt 1 — Fristlage zuerst

Ziehe **`bescheid-frist-quick-check`** sofort. Ergebnisse:

| Fristlage | Sofortiger nächster Skill |
|---|---|
| Frist offen, mehr als 14 Tage | `bescheidanalyse` → `widerspruch-formulieren` |
| Frist offen, weniger als 14 Tage | `widerspruch-formulieren` (Kurzfassung) parallel `akteneinsicht-anfordern` |
| Frist verstrichen, weniger als 14 Tage drüber | `widerspruch-formulieren` plus Wiedereinsetzung § 67 SGG |
| Frist verstrichen, mehr als 14 Tage | Prüfen Überprüfungsantrag § 44 SGB X — eigenständiger Pfad |
| Eilbedarf (Existenz, Hilfsmittel, Schule) | `eilantrag-sozialrecht` **parallel** zum Widerspruch |

### Schritt 2 — Bescheidart und Rechtsgebiet

Mappe das Rechtsgebiet auf den Spezial-Skill:

| Rechtsgebiet | Spezial-Skill | Hauptnormen |
|---|---|---|
| Bürgergeld SGB II | `buergergeld-pruefen` | §§ 19 ff. SGB II |
| Hilfsmittel SGB V (Rollstuhl, Hörhilfe, Lift) | `hilfsmittelantrag-pruefen` | § 33 SGB V, §§ 47 ff. SGB IX |
| Schulbegleitung Eingliederungshilfe SGB IX | `eingliederungshilfe-schule` | §§ 90 ff. SGB IX, § 35a SGB VIII |
| Pflegegrad SGB XI | `pflegegrad-widerspruch` | §§ 14, 15 SGB XI, MD-Begutachtung |
| Erwerbsminderungsrente SGB VI | `erwerbsminderungsrente-pruefen` | §§ 43, 240 SGB VI |
| Schwerbehinderung GdB Merkzeichen | `schwerbehindertenausweis-gdb` | § 152 SGB IX, VersMedV |
| Asylbewerberleistungen | (allgemein `bescheidanalyse` plus `widerspruch-formulieren`) | §§ 1a–3 AsylbLG |

### Schritt 3 — Verfahrensstand und Mandantensituation

Lege fest, ob folgende Querschnitt-Skills heute noch anzustoßen sind:

- **`akteneinsicht-anfordern`** — bei jedem Bescheid mit medizinischer oder gutachterlicher Grundlage, sofort parallel
- **`pkh-erfolgsaussicht-pruefen`** plus **`prozesskostenhilfe-antrag`** — wenn Klage absehbar und Mandant bedurftig
- **`fristenbuch-sozialrecht`** — Eintrag noch heute, kein Tag später
- **`anlagen-erstellen`** — sobald drei oder mehr Belege im Spiel sind
- **`mandantenbrief-leichte-sprache`** — wenn Mandant Bescheid nicht versteht oder kognitive Beeintraechtigung vorliegt

## Output-Format

Liefere eine **Routing-Karte** im folgenden Format:

```
ROUTING-KARTE — Az [intern] — [Mandant] — [Datum]

Fristlage: [offen / knapp / verstrichen / Eilbedarf]
Rechtsgebiet: [SGB X]
Verfahrensstand: [Erstbescheid / Widerspruch / Klage]
Eilbedarf: [ja / nein, Begruendung]

REIHENFOLGE HEUTE
1. [Skill A] — Ergebnis = X
2. [Skill B] — Ergebnis = Y
3. Fristenbuch-Eintrag

REIHENFOLGE DIESE WOCHE
4. [Skill C]
5. [Skill D]

PARALLEL
- Akteneinsicht (ja/nein + Begruendung)
- PKH (ja/nein)
- Eilantrag (ja/nein)

MANDANTENINFORMATION
- Naechste Rueckmeldung an Mandant bis [Datum]
- Pflichtinfo: [Frist X laeuft am Y ab]
```

## Anwendungsbeispiel — Familie Tannenberg

In der Testakte `sozialrecht-rollstuhl-tannenberg` liegen vier Fälle in einer Familie. Wende die Routing-Karte je Fall einmal an. Du wirst sehen: vier sehr unterschiedliche Pfade trotz einem Plugin.

## Hinweise

- Du sprichst die Anwältin direkt an, nicht den Mandanten.
- Nie raten — wenn ein Datum fehlt, frage nach.
- Wiedereinsetzung § 67 SGG ist Ausnahme, kein Standardpfad. Wirklich nur bei unverschuldeter Verzoegerung.
- Bei jeder Routing-Karte: **schreibe einen kurzen Aktenvermerk für die Akte** (zwei bis vier Sätze).
- Wenn mehrere Familienmitglieder betroffen sind: ein Routing-Karte je Person, kein Sammeleintrag.
