---
name: literatur-quellen-prompting-leitfaden-rdg
description: "Literatur Quellen Prompting Leitfaden RDG: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Literatur Quellen Prompting Leitfaden RDG

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Literatur Quellen Prompting Leitfaden RDG** im Plugin KI-Richtlinie für Kanzleien. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `literatur-und-quellen` | Pflicht-Literatur und Aktualisierungsliste für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei will Richtlinie auf dem neuesten Stand halten und benoetigt strukturierte Quellenübersicht. BRAK-Hinweise, DAV-Stellungnahmen, EU-Kommissionsmaterial, BNetzA-Hinweise und KI-VO EU 2024/1689. Prüfraster Kernliteratur Berufsrecht Datenschutz KI-VO, Recherche aktueller Entwicklungen, offene Aktualisierungsliste für neue Entscheidungen. Output kommentierte Quellenliste mit Relevanz-Einordnung und Update-Pflicht. Abgrenzung zu Richtlinien-Update-Zyklus und zu Berufsrecht-Bausteine. |
| `prompting-leitfaden` | Prompting-Leitfaden für juristische KI-Nutzung in Kanzleien: Anwendungsfall Anwalt oder Mitarbeitende wollen KI effektiver nutzen und benoetigen praxiserprobte Prompt-Methoden. Mandantenkommunikation mit KI, Anwaltsgeheimnis beim Prompten. Prüfraster Vier-Elemente-Methode Zielformulierung Ausgabeformat Hintergrundwissen Beispiel, Rollenanweisung, Schritt-fuer-Schritt-Methode, Iteration, Zitate-Verifikation. Output Prompting-Leitfaden mit Vorlagen und Checkliste für juristische Aufgabentypen. Abgrenzung zu Halluzinations-Handhabung und zu Compliance-Regelsatz. |
| `rdg-pruefung-chatbot` | Prüffeld für rdg pruefung chatbot: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin KI-Richtlinie für Kanzleien gilt für **Literatur Quellen Prompting Leitfaden RDG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `literatur-und-quellen`

**Fokus:** Pflicht-Literatur und Aktualisierungsliste für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei will Richtlinie auf dem neuesten Stand halten und benoetigt strukturierte Quellenübersicht. BRAK-Hinweise, DAV-Stellungnahmen, EU-Kommissionsmaterial, BNetzA-Hinweise und KI-VO EU 2024/1689. Prüfraster Kernliteratur Berufsrecht Datenschutz KI-VO, Recherche aktueller Entwicklungen, offene Aktualisierungsliste für neue Entscheidungen. Output kommentierte Quellenliste mit Relevanz-Einordnung und Update-Pflicht. Abgrenzung zu Richtlinien-Update-Zyklus und zu Berufsrecht-Bausteine.

# Literatur und Quellen

Eine fundierte KI-Nutzungsrichtlinie stützt sich auf anerkannte Primärquellen und berufsständische Verlautbarungen. Dieser Skill listet die Kernliteratur, gibt Hinweise zur Recherche aktueller Entwicklungen und enthält eine offene Aktualisierungsliste für neu erscheinende relevante Quellen.

## Rechtlicher Hintergrund

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Primärquellen stets prüfen**: Bei allen Normanwendungen auf den aktuellen Gesetzestext verweisen (gesetze-im-internet.de, EUR-Lex).
2. **BRAK und DAV regelmäßig konsultieren**: Neue Hinweise, Stellungnahmen und Leitfäden werden auf den jeweiligen Websites veröffentlicht.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
4. **Judikatur beobachten**: Neue BGH- und OLG-Entscheidungen zum Thema KI in der Anwaltschaft zeitnah in die Richtlinie einarbeiten.
5. **EU-Instanzen verfolgen**: Leitlinien des EU-KI-Büros (https://digital-strategy.ec.europa.eu/de/policies/ai-office) und FAQ der Europäischen Kommission zur KI-Kompetenz.
6. **Aktualisierungsliste führen**: Neu erscheinende relevante Quellen in einer offenen Liste erfassen, die beim nächsten Halbjahres-Review ausgewertet wird.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Quellenverzeichnis und Verifizierungsprotokoll erstellen | Quellenverzeichnis nach Schema; Template unten |
| Variante A — Quellenangaben aus KI unvollstaendig | Luecken als ungepruefte KI-Angaben markieren; Nachpruefung dokumentieren |
| Variante B — Nur Gerichtsentscheidungen zu zitieren | Rechtsprechungs-Subset; Quellenprüfung weglassen |
| Variante C — Quellenangaben auf Englisch | Englischsprachige Zitierweise; Bluebook oder OSCOLA als Standard |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Pflicht-Literaturliste (Stand 07/2025):**

**Berufsständisches Softlaw:**
- BRAK (Remmertz), Hinweise zum Einsatz von künstlicher Intelligenz (KI), Stand: Dezember 2024. Abrufbar unter: https://www.brak.de/newsroom/newsletter/nachrichten-aus-berlin/2025/ausgabe-1-2025-v-812025/kuenstliche-intelligenz-in-anwaltskanzleien-brak-veroeffentlicht-leitfaden/
- DAV, Initiativ-Stellungnahme zum Einsatz von KI in der Anwaltschaft, Stellungnahme Nr. 32/2025, Berlin, Juli 2025.

**Wissenschaftliche Literatur:**
- Martini/Wendehorst (Hrsg.), KI-VO — Kommentar zur Verordnung (EU) 2024/1689, 1. Aufl.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**EU-Institutionen:**
- Europäische Kommission, FAQ zur KI-Kompetenz (Art. 4 KI-VO). Abrufbar unter: https://digital-strategy.ec.europa.eu
- Bundesnetzagentur, Hinweise zur KI-Kompetenz. Abrufbar unter: https://www.bundesnetzagentur.de

**Rechtsprechung:**
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Primärrechtsquellen:**
- Verordnung (EU) 2024/1689 (KI-VO): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689
- Verordnung (EU) 2016/679 (DSGVO): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679
- BRAO: https://www.gesetze-im-internet.de/brao/
- StGB § 203: https://www.gesetze-im-internet.de/stgb/__203.html

**Offene Aktualisierungsliste (bei nächstem Review zu prüfen):**
- [ ] Neue BRAK-Hinweise nach 07/2025
- [ ] Neue DAV-Stellungnahmen nach 07/2025
- [ ] KI-VO-Durchführungsrechtsakte der EU-Kommission
- [ ] Neue BGH/OLG-Entscheidungen zu KI in Schriftsätzen
- [ ] Neue EuGH-Entscheidungen zu DSGVO und KI

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Die Literaturliste ist beim halbjährlichen Richtlinien-Review vollständig zu überprüfen und um neu erschienene relevante Beiträge zu ergänzen. Sobald ein KI-VO-Durchführungsrechtsakt erscheint, ist er sofort in die Primärquellenliste aufzunehmen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43 BRAO — Sorgfaltspflicht und korrekte Quellenangaben
- § 138 ZPO — Wahrheitspflicht (gilt auch fuer Quellenangaben)
- Art. 5 Abs. 1 lit. d DSGVO — Richtigkeit der verarbeiteten Informationen
- § 44b UrhG — Text-und-Data-Mining-Schranke (fuer KI-Recherche)

## Triage zu Beginn
1. Werden Quellen aus KI-Ausgaben direkt verwendet oder gegen amtliche Quellen verifiziert?
2. Ist ein Verifikationsprozess fuer Rechtsprechungs-Fundstellen (juris, Beckonline, EUR-Lex) etabliert?
3. Werden Kommentare und Monografien aus KI-Ausgaben abgeglichen?
4. Gibt es eine aktuelle Literatursammlung fuer das relevante Rechtsgebiet?
5. Sind Mitarbeiter geschult, zwischen Primaer- und Sekundaerquellen zu unterscheiden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Quellenverzeichnis / Verifizierungsprotokoll
**Adressat:** Kanzlei intern — Tonfall: dokumentierend
```
QUELLENVERZEICHNIS UND VERIFIZIERUNGSPROTOKOLL
[DATUM] — [AKTENZEICHEN] — Dokument: [BEZEICHNUNG]

PRIMÄRQUELLEN (verifiziert):
Rechtsprechung:
- [GERICHT, DATUM — AZ, FUNDSTELLE]: Verifiziert gegen [QUELLE] am [DATUM]
- [WEITERE]

Gesetze und Verordnungen:
- [NORM]: verifiziert gegen [QUELLE] am [DATUM]

SEKUNDÄRQUELLEN (Kommentare / Literatur):
- [AUTOR, Werk, Auflage, Randzahl]: Im Original eingesehen am [DATUM]

KI-GENERIERTE FUNDSTELLEN (Verifikationsstatus):
- [FUNDSTELLE]: [BESTAETIGT / NICHT GEFUNDEN / FEHLERHAFT — Korrektur: BESCHREIBUNG]

Verifiziert von: [NAME], [DATUM]
```

## 2. `prompting-leitfaden`

**Fokus:** Prompting-Leitfaden für juristische KI-Nutzung in Kanzleien: Anwendungsfall Anwalt oder Mitarbeitende wollen KI effektiver nutzen und benoetigen praxiserprobte Prompt-Methoden. Mandantenkommunikation mit KI, Anwaltsgeheimnis beim Prompten. Prüfraster Vier-Elemente-Methode Zielformulierung Ausgabeformat Hintergrundwissen Beispiel, Rollenanweisung, Schritt-fuer-Schritt-Methode, Iteration, Zitate-Verifikation. Output Prompting-Leitfaden mit Vorlagen und Checkliste für juristische Aufgabentypen. Abgrenzung zu Halluzinations-Handhabung und zu Compliance-Regelsatz.

# Prompting-Leitfaden

Ein "Prompt" ist eine Instruktion an ein KI-System — vergleichbar damit, wie man eine Kollegin oder einen Mitarbeiter um Unterstützung bittet. Effektives Prompten ist eine Kernkompetenz beim KI-Einsatz in der juristischen Praxis. Die Qualität des Outputs hängt unmittelbar von der Qualität der Eingabe ab. Dieser Skill vermittelt die Vier-Elemente-Methode und praxiserprobte Tipps für den juristischen Kontext.

## Rechtlicher Hintergrund

Art. 4 KI-VO: Pflicht zur KI-Kompetenz — die Fähigkeit zum effektiven und sicheren Prompten ist eine zentrale Komponente dieser Kompetenz. Art. 3 Nr. 56 KI-VO: KI-Kompetenz umfasst das Wissen, KI-Systeme sachkundig einzusetzen. BRAK-Hinweise 12/2024: Anwälte müssen in der Lage sein, KI-Output zu beurteilen — was voraussetzt, dass der Prompt präzise genug war, um einen beurteilbaren Output zu erzeugen. DAV-Stellungnahme 32/2025: Kompetenter Umgang mit KI-Systemen als berufsrechtliche Anforderung.

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

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

## 3. `rdg-pruefung-chatbot`

**Fokus:** Prüffeld für rdg pruefung chatbot: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# RDG-Prüfung Chatbot

Die Frage, ob ein KI-Chatbot "Rechtsdienstleistungen" im Sinne des Rechtsdienstleistungsgesetzes (RDG) erbringt, ist für Kanzleien in mehrfacher Hinsicht relevant: für die eigene Nutzung durch anwaltliche und nicht-anwaltliche Mitarbeitende sowie für die Beratung von Mandanten, die KI-gestützte Rechtsservices anbieten oder nutzen.

## Rechtlicher Hintergrund

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

1. **Nutzerperspektive bestimmen**: Wer nutzt den Chatbot — ein Anwalt als Werkzeug oder ein Laie als Rechtsberater?
2. **Einzelfall-Bezug prüfen**: Liegt ein konkreter fremder Rechtsfall vor, der einer rechtlichen Einzelfallprüfung unterzogen wird? Allgemeine Rechtsinformationen (§ 2 Abs. 3 Nr. 2 RDG) und Schreibhilfen sind keine Rechtsdienstleistung.
3. **Anwaltliche Nutzung**: Ein Rechtsanwalt, der einen Chatbot als Werkzeug zur Erstellung eigener Schriftsätze nutzt und das Ergebnis eigenverantwortlich prüft und freigibt, erbringt selbst die Rechtsdienstleistung — nicht der Chatbot.
4. **Nicht-anwaltliche Nutzung**: Gibt ein nicht-anwaltlicher Mitarbeiter KI-Output ungeprüft als Rechtsberatung weiter, kann ein RDG-Verstoß vorliegen — sowohl durch den Mitarbeiter als auch ggf. durch den Chatbot-Anbieter.
5. **Disclaimer-Wirkung**: Selbst wenn ein Chatbot-Anbieter erklärt, keine Rechtsberatung zu erbringen, ist dies bei objektiver Betrachtung möglicherweise unbeachtlich — auf die tatsächliche Funktion kommt es an.
6. **Mandantenberatung**: Mandanten, die eigene KI-gestützte Rechtsservices entwickeln oder anbieten wollen, sind auf die RDG-Anforderungen und die BGH-Rechtsprechung hinzuweisen.

## Vorlagentext / Bausteine

**Baustein RDG-Abgrenzung für Mitarbeitende:**
Mitarbeitende ohne Rechtsanwaltszulassung dürfen KI-generierten Output zu rechtlichen Fragen nicht als Rechtsberatung an Mandanten oder sonstige Dritte weitergeben. Die unkritische Weitergabe von KI-generierten Rechtsaussagen an Dritte ohne anwaltliche Prüfung und Freigabe kann als unerlaubte Rechtsdienstleistung nach § 3 RDG qualifizieren. Dies gilt ungeachtet etwaiger Disclaimer des KI-Anbieters.

**Baustein RDG-Konformität bei anwaltlicher Nutzung:**
Rechtsanwältinnen und Rechtsanwälte, die KI-Systeme als Hilfsmittel zur Erstellung von Schriftsätzen, Gutachten oder Beratungsschreiben nutzen und das Ergebnis eigenverantwortlich prüfen und freigeben, verstoßen nicht gegen das RDG. Die Rechtsdienstleistung erbringt in diesem Fall der Anwalt — der Chatbot ist lediglich ein unterstützendes Werkzeug.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Hinweise zur Aktualisierung

Die Rechtsprechung zum RDG im Kontext von KI-Systemen ist noch im Entstehen. Nach neuen BGH-Entscheidungen oder Entscheidungen der Oberlandesgerichte zur Qualifikation von KI-Diensten als Rechtsdienstleistung ist dieser Baustein zu aktualisieren. Auch Gesetzgebungsvorhaben zur Anpassung des RDG an die KI-Realität sind zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 2 RDG — Rechtsdienstleistung (Begriff)
- § 3 RDG — Erlaubte Rechtsdienstleistungen (nur Anwaelte, bestimmte Ausnahmen)
- § 5 RDG — Erlaubte Nebenleistungen
- Art. 50 Abs. 1 KI-VO — Chatbot-Offenlegungspflicht
- § 43 BRAO — Sorgfaltspflicht bei KI-gestuetzter Rechtsberatung

## Triage zu Beginn
1. Gibt der Chatbot rechtliche Einschatzungen oder nur allgemeine Informationen?
2. Basiert die Chatbot-Antwort auf dem konkreten Einzelfall des Nutzers — Subsumtion?
3. Ist ein Rechtsanwalt als Verantwortlicher fuer die Chatbot-Antworten benannt?
4. Wird der Chatbot-Charakter nach Art. 50 Abs. 1 KI-VO offengelegt?
5. Gibt es einen Hinweis, dass der Chatbot keine anwaltliche Beratung ersetzt?

## Output-Template — RDG-Pruefprotokoll Chatbot
**Adressat:** Kanzlei / Compliance — Tonfall: rechtlich, praezise
```
RDG-PRUEFPROTOKOLL — CHATBOT
[DATUM] — Chatbot: [NAME] — Anwendungsfall: [BESCHREIBUNG]

§ 2 RDG — Rechtsdienstleistung:
Chatbot-Funktion: [INFORMATIONSERTEILUNG / SUBSUMTION EINZELFALL / BERATUNG]
Rechtliche Einschaetzung im Einzelfall: [JA — RDG-Pruefung erforderlich / NEIN]
RDG-Risiko: [KEIN / NIEDRIG / HOCH]

Falls RDG anwendbar — Erlaubnisgrundlage:
☑/☐ § 3 RDG: Anwalt als Betreiber/Verantwortlicher
☑/☐ § 5 RDG: Nebenleistung zu erlaubter Hauptleistung
☑/☐ NEIN — Einsatz als Rechtsdienstleistung unzulaessig

Art. 50 Abs. 1 KI-VO — Chatbot-Offenlegung:
☑/☐ Nutzer wird informiert, dass er mit KI-System interagiert

Disclaimer vorhanden: [JA: TEXT / NEIN — NACHRUESTEERFORDERLICH]

Ergebnis: [ZULASSIG / BEDINGT ZULASSIG / UNZULAESSIG]
Auflagen: [BESCHREIBUNG]
Geprueft von: [NAME RA/RAin], [DATUM]
```
