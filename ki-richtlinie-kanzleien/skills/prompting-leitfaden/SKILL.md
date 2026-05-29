---
name: prompting-leitfaden
description: "Prompting-Leitfaden für juristische KI-Nutzung in Kanzleien: Anwendungsfall Anwalt oder Mitarbeitende wollen KI effektiver nutzen und benoetigen praxiserprobte Prompt-Methoden. Mandantenkommunikation mit KI, Anwaltsgeheimnis beim Prompten. Prüfraster Vier-Elemente-Methode Zielformulierung Ausgabeformat Hintergrundwissen Beispiel, Rollenanweisung, Schritt-fuer-Schritt-Methode, Iteration, Zitate-Verifikation. Output Prompting-Leitfaden mit Vorlagen und Checkliste für juristische Aufgabentypen. Abgrenzung zu Halluzinations-Handhabung und zu Compliance-Regelsatz."
---

# Prompting-Leitfaden

Ein "Prompt" ist eine Instruktion an ein KI-System — vergleichbar damit, wie man eine Kollegin oder einen Mitarbeiter um Unterstützung bittet. Effektives Prompten ist eine Kernkompetenz beim KI-Einsatz in der juristischen Praxis. Die Qualität des Outputs hängt unmittelbar von der Qualität der Eingabe ab. Dieser Skill vermittelt die Vier-Elemente-Methode und praxiserprobte Tipps für den juristischen Kontext.

## Rechtlicher Hintergrund

Art. 4 KI-VO: Pflicht zur KI-Kompetenz — die Fähigkeit zum effektiven und sicheren Prompten ist eine zentrale Komponente dieser Kompetenz. Art. 3 Nr. 56 KI-VO: KI-Kompetenz umfasst das Wissen, KI-Systeme sachkundig einzusetzen. BRAK-Hinweise 12/2024: Anwälte müssen in der Lage sein, KI-Output zu beurteilen — was voraussetzt, dass der Prompt präzise genug war, um einen beurteilbaren Output zu erzeugen. DAV-Stellungnahme 32/2025: Kompetenter Umgang mit KI-Systemen als berufsrechtliche Anforderung.

## Vorgehen


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

Die **Vier-Elemente-Methode** strukturiert jeden Prompt nach folgenden Elementen:

**Element 1 — Zielformulierung:**
Formulieren Sie ein klares, spezifisches Ziel. Was soll das KI-System tun? Welches Ergebnis soll erzeugt werden? Achten Sie auf Präzision und Direktheit. Vermeiden Sie vage Anweisungen wie "Schreibe etwas über X" — besser: "Erstelle einen ersten Entwurf des Abschnitts zur Haftungsbegrenzung für einen M&A-Vertrag nach deutschem Recht."

**Element 2 — Ausgabeformat:**
Beschreiben Sie genau, wie die Informationen dargestellt werden sollen (Fließtext, Stichpunkte, Tabelle, Gliederung, Absatz-Länge, Sprachstil). Legen Sie strukturelle Anforderungen fest (z.B. "Gliedere nach Abschnitten mit Überschriften", "Verwende juristische Fachsprache", "Schreibe in maximal drei Absätzen").

**Element 3 — Hintergrundwissen:**
Liefern Sie umfassende Kontextinformationen, die das KI-System für die Aufgabe benötigt. Teilen Sie relevante Sachverhaltsdetails mit (anonymisiert!). Nennen Sie anwendbare Normen, auf die das KI-System sich beziehen soll.

**Element 4 — Beispiel:**
Wenn vorhanden: Zeigen Sie dem KI-System ein Beispiel für den gewünschten Output (Stil, Struktur, Tiefe). Dieses "Few-Shot-Prompting" verbessert die Qualität der Ergebnisse erheblich.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Prompting-Leitfaden fuer Kanzlei erstellen | Leitfaden nach Schema; Template unten |
| Variante A — Leitfaden nur fuer Associates nicht Partner | Einstiegs-Version; vereinfachte Prompting-Grundsaetze |
| Variante B — Bestimmtes KI-Tool im Fokus GPT oder anderes | Tool-spezifischer Leitfaden; allgemeine Grundsaetze als Anhang |
| Variante C — Leitfaden soll Pflichten dokumentieren kein How-To | Pflichten-Leitfaden statt Anwendungs-Tutorial |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Tipps und Tricks für juristische Prompts:**

**Rollenanweisung**: Weisen Sie dem KI-System eine Rolle zu: "Du bist ein erfahrener Anwalt im deutschen Gesellschaftsrecht" oder "Schreibe aus der Perspektive der klagenden Partei." Dies verbessert Stil und Fokus.

**Schritt-für-Schritt**: Bei komplexen Aufgaben besser mehrere präzise Einzel-Prompts als ein überladener Mega-Prompt. Ergebnisse schrittweise verfeinern.

**Iteration**: Wenn das Ergebnis nicht passt — nicht aufgeben. Den KI-Chatbot auf Fehler oder Ungenauigkeiten hinweisen und um eine überarbeitete Version bitten.

**Zitate-Verifikation einbauen**: Im Prompt explizit anweisen: "Gib nur Fundstellen an, die du mit hoher Sicherheit kennst, und markiere unsichere Angaben." — Dann trotzdem immer selbst prüfen!

**Kürzere Prompts oft besser**: Ein klar umrissenes Problem führt zu besseren Ergebnissen als eine überladene Anfrage.

**Kontext schaffen**: Für wen ist die Antwort gedacht? Aus welcher Perspektive soll argumentiert werden? Je klarer der Kontext, desto passender das Ergebnis.

**Muster-Prompt juristische Recherche:**
"Du bist ein erfahrener Jurist im deutschen Datenschutzrecht. Erkläre mir die Anforderungen des Art. 28 DSGVO an einen Auftragsverarbeitungsvertrag mit einem KI-Dienstleister. Strukturiere die Antwort in maximal fünf Stichpunkte mit jeweils zwei bis drei Sätzen Erläuterung. Verwende juristische Fachsprache. Gib nur Normen an, die du mit Sicherheit kennst."

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Prompting-Techniken entwickeln sich mit den KI-Systemen weiter. Was heute gut funktioniert, kann bei einem Modell-Update weniger effektiv sein. Die Schulungsunterlagen sollten jährlich mit aktuellen Erfahrungen und neuen Erkenntnissen aus der juristischen KI-Praxis aktualisiert werden.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43 BRAO — Gewissenhafte Berufsausuebung (gilt auch fuer Prompting-Qualitaet)
- Art. 4 KI-VO — KI-Kompetenzverpflichtung (beinhaltet effektiven Umgang mit KI)
- Art. 26 Abs. 1 lit. b KI-VO — Einhaltung der Anleitung des KI-Anbieters
- § 43a Abs. 2 BRAO — Keine mandantenbezogenen Informationen im Prompt ohne Anonymisierung

## Triage zu Beginn
1. Ist der Prompt klar und eindeutig formuliert — wird die gewuenschte Aufgabe praezise beschrieben?
2. Wurden mandantenbezogene Daten vor Aufnahme in den Prompt anonymisiert?
3. Ist das KI-System und seine Grenzen dem Nutzer bekannt (Halluzinationsrisiko bei Rechtsfragen)?
4. Gibt es kanzleiinterne Prompt-Vorlagen fuer haeufige Aufgaben?
5. Werden Prompts und Ergebnisse fuer Protokollzwecke aufbewahrt?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Prompting-Leitfaden Kanzlei
**Adressat:** Alle KI-Nutzenden in der Kanzlei — Tonfall: praktisch, anleitend
```
PROMPTING-LEITFADEN
[KANZLEI] — Stand: [DATUM]

GRUNDREGELN:
1. Anonymisieren: Keine Echtdaten — Platzhalter verwenden (M1, G1, Az-1).
2. Aufgabe klar formulieren: Was soll die KI tun? Welches Ergebnis wird erwartet?
3. Kontext geben: Rechtsgebiet, Rolle der KI (Entwurf / Zusammenfassung / Recherche).
4. Schritt fuer Schritt: Bei komplexen Aufgaben in Teilaufgaben aufteilen.
5. Ergebnis kritisch pruefen: KI-Ausgabe ist Entwurf — kein Endprodukt.

PROMPT-STRUKTUR:
"Du bist ein juristischer Assistent. Erstelle einen [DOKUMENT-TYP] zu folgendem Sachverhalt:
[ANONYMISIERTER SACHVERHALT]. Bitte beruecksichtige [RECHTSNORMEN]. Weise auf Unsicherheiten hin."

VERBOTENE INHALTE IM PROMPT:
- Vollstaendige Namen
- Aktenzeichen (unveraendert)
- Adressen, Geburtsdaten, Finanzdaten

KANZLEI-PROMPT-VORLAGEN: [REFERENZ AUF VORLAGENSAMMLUNG]
FRAGEN: [ANSPRECHPARTNER KI]
```
