---
name: mandantenbrief-memo-rbs-beratungshilfe
description: "Mandantenbrief Memo RBS Beratungshilfe: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenbrief Memo RBS Beratungshilfe

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenbrief Memo RBS Beratungshilfe** im Plugin Rechtsberatungsstelle (RDG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandantenbrief` | Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behoerde oder Gericht vorbereiten. BeratungsHiG niedrigschwellige Beratung, Mandantenkommunikation in verstaendlicher Sprache. Prüfraster Empfaenger und Zweck klaeren, Sachverhalts-Zusammenfassung, rechtliche Einordnung, naechste Schritte für Mandant. Output Mandantenbrief in verstaendlicher oder juristisch foermlicher Sprache je nach Empfaenger. Abgrenzung zu Einfache-Sprache-Briefe für barrierefreie Kommunikation und zu Entwurf für Schriftsaetze. |
| `memo` | Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit RECHERCHE ERFORDERLICH markiert, die Subsumtion mit STUDENTISCHE ANALYSE, das Ergebnis ist bewusst offen gelassen. Lädt, wenn ein Studierender ein internes Rechtsgutachten strukturieren, eine Fallanalyse aufschreiben oder ein Kurz-Gutachten für einen Fall erstellen muss. |
| `rbs-beratungshilfe-und-pkh-praxis` | Beratungshilfe BerHG und PKH in der Praxis: Antrag beim Amtsgericht, Berechtigung Einkommen, Vermoegen, Wahrnehmungsbefugnis Anwalt. Schnittstelle PKH-Antrag. Mustertexte und Berechtigungsnachweise. |

## Arbeitsweg

Im Plugin Rechtsberatungsstelle (RDG) gilt für **Mandantenbrief Memo RBS Beratungshilfe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandantenbrief`

**Fokus:** Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behoerde oder Gericht vorbereiten. BeratungsHiG niedrigschwellige Beratung, Mandantenkommunikation in verstaendlicher Sprache. Prüfraster Empfaenger und Zweck klaeren, Sachverhalts-Zusammenfassung, rechtliche Einordnung, naechste Schritte für Mandant. Output Mandantenbrief in verstaendlicher oder juristisch foermlicher Sprache je nach Empfaenger. Abgrenzung zu Einfache-Sprache-Briefe für barrierefreie Kommunikation und zu Entwurf für Schriftsaetze.

# /mandantenbrief

1. Lade `CLAUDE.md` → Fachbereich, Sprachniveau-Einstellungen, Anleiterpflicht.
2. Ermittle: Was soll der Brief mitteilen? Welchen nächsten Schritt soll der Mandant tun?
3. Schreibe den Brief in einfacher Sprache (Ziel: B1/B2; bei besonderen Bedarfen: leichte Sprache A2).
4. Kein Juristenjargon. Kurze Sätze. Aktive Formulierungen.
5. Ausgabe: Entwurf mit KI-Label. Versand erst nach Anleiterpfreigabe.

---

# Mandantenbrief in einfacher Sprache


## Triage zu Beginn
1. Was soll der Brief mitteilen: Ergebnis einer Pruefung, Verfahrensstand, konkreter naechster Schritt oder Ablehnung?
2. Auf welchem Sprachniveau soll der Brief verfasst werden: B1/B2 Standard oder Leichte Sprache A2 bei besonderem Bedarf?
3. Enthaelt der Brief Angaben ueber Dritte oder interne Bewertungen, die im Mandantenbrief nicht erscheinen duerfen?
4. Hat der anleitende Volljurist den Briefentwurf bereits freigegeben oder ist das Gate noch ausstehend?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- BORA § 11 — Mitteilungspflicht: Mandant ist ueber wesentliche Verfahrensschritte zu informieren
- § 43a Abs. 2 BRAO — Verschwiegenheit: Mandantenbrief darf keine Drittinformationen offenbaren
- § 6 Abs. 2 Nr. 2 RDG — Anleitungspflicht: Mandantenbrief von Studierenden erfordert Anleiterpruefung und -freigabe
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur fuer Mandanten bestimmte Informationen im Brief

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Viele Mandanten der Beratungsstelle haben wenig oder keine juristische Vorbildung. Bei Geflüchteten kommen Sprachbarrieren und ein anderes Verständnis von Behörden und Rechtssystem hinzu. Ein unverständlicher Brief ist genauso wertlos wie kein Brief.

Dieser Skill erzeugt Briefe, die der Mandant versteht – und die ihn in die Lage versetzen, selbst zu handeln, wo das möglich ist.

**Was der Skill nicht tut:** strategische Rechtsberatung im Brief. Konkrete Rechtsratschläge nur in der Formulierung, die der Anleiter freigegeben hat.

## BORA-Pflichten bei Mandantenmitteilungen

- BORA § 11 (Handakten / Mitteilungspflichten): Der Anwalt (hier: der Anleiter) hat den Mandanten über wesentliche Verfahrensschritte zu informieren.
- BORA § 14: Rücksendung von Unterlagen und Abrechnung (hier: da unentgeltlich, primär Aktenführung).
- § 43a Abs. 2 BRAO: Keine Informationen über Dritte im Brief an den Mandanten preisgeben.
- Datenschutz: Im Brief nur Informationen, die für den Mandanten bestimmt sind. Keine internen Bewertungen, keine Drittdaten.

## Sprach- und Verständlichkeitsprinzipien

### Grundregeln (Ziel B1/B2)

| Regel | Schlecht | Besser |
|---|---|---|
| Kurze Sätze (max. 15 Wörter) | "Die Frist zur Einlegung des Widerspruchs beträgt nach § 84 SGG einen Monat ab Bekanntgabe des Bescheids." | "Sie haben einen Monat Zeit, um Widerspruch einzulegen. Die Frist beginnt mit dem Datum auf dem Bescheid." |
| Aktiv statt Passiv | "Der Widerspruch wird eingelegt." | "Wir legen Widerspruch ein." |
| Bekannte Wörter | "Klagefrist", "Begründetheit", "Subsumtion" | "Frist", "Grund für den Widerspruch" |
| Keine Abkürzungen ohne Erklärung | "SGB II § 22" | "Bürgergeld-Gesetz (Abschnitt über Wohnen)" |
| Handlungsorientierung | Nur Information | "Was Sie jetzt tun müssen: ..." |
| Freundlicher Ton | Amtsdeutsch | Persönliche, respektvolle Ansprache |

### Bei Geflüchteten / mehrsprachigem Kontext
- Brief auf Deutsch schreiben; wenn möglich parallel auf Arabisch / Dari / Tigrinya (mit Hinweis, dass dies kein Rechtsrat in der Zielsprache ist, sondern eine Orientierungshilfe).
- Keine Terminologie verwenden, die kulturell unterschiedlich verstanden wird (z. B. "Widerspruch" → erklären, was das ist).
- Ansprechperson und Erreichbarkeit der Beratungsstelle immer angeben.

## Briefstruktur (Standard)

```
[Briefkopf Beratungsstelle]
[Ort, Datum]

Betreff: [Ihr Verfahren – kurze, klare Beschreibung]

Guten Tag [Vorname Mandant],

wir beraten Sie in Ihrer Sache: [kurze Stichwortbeschreibung, 1 Satz].

**Was ist passiert?**
[1–3 Sätze: Was haben wir geprüft / Was ist zuletzt vorgefallen]

**Was bedeutet das für Sie?**
[1–3 Sätze: Ergebnis der Prüfung in verständlicher Sprache]

**Was passiert jetzt?**
[Konkrete nächste Schritte – nummeriert]
1. ...
2. ...

**Was müssen SIE tun?**
[Wenn der Mandant etwas tun muss – klar hervorgehoben, Frist nennen]
→ Bitte schicken Sie uns bis [TT.MM.JJJJ]: [Dokument / Information]
→ Bitte kommen Sie zu unserem nächsten Termin am: [Datum, Uhrzeit, Ort]

**Was darf ich nicht?**
[Ggf. Hinweis, was der Mandant nicht ohne uns tun sollte – z. B. "Bitte unterschreiben Sie keine neuen Dokumente des Jobcenters, ohne uns zu fragen."]

**Bei Fragen:**
Wenden Sie sich an: [Name des Studierenden / der Beratungsstelle]
Telefon: [...] | E-Mail: [...] | Sprechzeiten: [...]

Mit freundlichen Grüßen

[Name des Studierenden / Kürzel]
[Beratungsstelle]
[Rechtlicher Hinweis: Dieser Brief ist ein Entwurf, geprüft von [Anleiter].]
```

## Häufige Briefanlässe und Formulierungshilfen

### Widerspruch eingelegt (SGB II / SGB XII)
> "Wir haben für Sie am [Datum] Widerspruch gegen den Bescheid vom [Datum] eingelegt. Der Widerspruch heißt, dass wir dem Jobcenter schreiben: Der Bescheid ist nicht korrekt. Das Jobcenter muss jetzt prüfen, ob es recht hat. Das kann einige Wochen dauern. Wir informieren Sie, sobald eine Antwort kommt."

### Klage erhoben (Verwaltungsgericht / Sozialgericht)
> "Wir haben für Sie am [Datum] Klage beim [Gericht, Ort] eingereicht. Das Aktenzeichen ist: [AZ]. Sie erhalten möglicherweise einen Brief vom Gericht – bitte leiten Sie diesen sofort an uns weiter."

### Mietmangel-Schreiben an Vermieter
> "Wir haben Ihrem Vermieter am [Datum] geschrieben, dass die Wohnung [Mangel] hat. Wir haben ihn aufgefordert, das bis zum [Datum] zu reparieren. Wenn er das nicht tut, können Sie die Miete mindern. Das bedeutet: Sie zahlen weniger Miete, weil die Wohnung nicht in Ordnung ist. Wie viel weniger – das besprechen wir mit Ihnen."

### BAMF-Klage eingereicht
> "Wir haben fristgerecht Klage gegen den Bescheid des BAMF vom [Datum] eingereicht. Das Verwaltungsgericht [Ort] prüft jetzt Ihren Fall. Das Aktenzeichen der Klage ist: [AZ]. Der Aufenthalt ist während des Klageverfahrens sichergestellt (§ 81 Abs. 3 AufenthG). Bitte informieren Sie uns sofort, wenn Sie Post vom Gericht oder der Ausländerbehörde bekommen."

### Termin-Erinnerung
> "Ihr nächster Termin bei uns ist: [Datum], [Uhrzeit], [Adresse, Raum]. Bitte bringen Sie mit: [Aufzählung der Unterlagen]. Wenn Sie nicht kommen können: Bitte rufen Sie uns vorher an unter [Nummer]."

## Ausgabeformat

Brief im obigen Standardformat. Kurzform erlaubt bei einfachen Mitteilungen (z. B. reine Terminbestätigung).

Jede Ausgabe trägt:
> **[KI-GESTÜTZTER ENTWURF – Analyse durch Studierenden und Freigabe durch anleitenden Volljuristen erforderlich. Kein Versand ohne Prüfung.]**

## Risiken / typische Fehler

- **Juristischer Rat im Mandantenbrief ohne Freigabe:** Kein Brief darf Aussagen enthalten wie "Sie werden gewinnen" oder "Die Klage hat gute Chancen" – das ist unzulässige Prognose ohne Anleiterbilligung.
- **Falsches Fristenverständnis beim Mandanten:** Der Brief muss Fristen, die der Mandant wahren muss (z. B. Vorlage von Dokumenten), klar und mit genauen Daten benennen. Keine vagen Formulierungen wie "möglichst bald".
- **Keine Rückfrage-Möglichkeit:** Mandantenbrief ohne Kontaktangabe ist wertlos. Immer Erreichbarkeit der Beratungsstelle angeben.
- **Vertraulichkeit verletzt:** Keine Drittdaten (z. B. Informationen über den Vermieter, den Arbeitgeber) im Brief an den Mandanten – es sei denn, der Mandant hat alle relevanten Informationen ohnehin selbst geliefert.

## 2. `memo`

**Fokus:** Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit RECHERCHE ERFORDERLICH markiert, die Subsumtion mit STUDENTISCHE ANALYSE, das Ergebnis ist bewusst offen gelassen. Lädt, wenn ein Studierender ein internes Rechtsgutachten strukturieren, eine Fallanalyse aufschreiben oder ein Kurz-Gutachten für einen Fall erstellen muss.

# Internes Rechtsgutachten: Gutachten-Gerüst

## Zweck

Das interne Rechtsgutachten ist das Herzstück studentischen Arbeitens in der Beratungsstelle. Diese Skill liefert das Gerüst nach der deutschen Gutachtenmethode (Obersatz — Norm/Definition — Subsumtion — Ergebnis) und kennzeichnet die Recherchelücken. Die Analyse selbst kommt vom Studierenden.

**Die Analyse ist Aufgabe des Studierenden.** Diese Skill strukturiert; sie schlussfolgert nicht.

Hinweis: Die Gutachtenmethode entspricht dem deutschen juristischen Standard. Kurzgutachten (direkter Einstieg mit Ergebnis, dann Begründung) sind für interne Berichte möglich; für die Ausbildung innerhalb der Beratungsstelle wird die volle Gutachtenform bevorzugt.

## Eingaben

- **Sachverhaltsnotizen / Aktennotiz** — Fakten des Falls; fehlende Angaben werden markiert
- **Rechtsgebiet** — z. B. Mietrecht, Arbeitsrecht, Verwaltungsrecht, Verbraucherrecht
- **Spezifische Rechtsfrage** (optional) — falls der Fokus auf einer bestimmten Frage liegen soll
- **Forschungsstand** (optional) — bereits recherchierte Normen oder Urteile, die eingeflossen sind

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 6 RDG** — Rechtsdienstleistungen durch studentische Beratungsstellen: zulässig als unentgeltliche Rechtsdienstleistung unter anwaltlicher Aufsicht. Das Gutachten ist ein internes Arbeitsmittel und kein Rechtsgutachten im Sinne eines anwaltlichen Leistungsprodukts.
- **§ 43a Abs. 2 BRAO / § 203 StGB** — Mandatsgeheimnis: Das Gutachten enthält vertrauliche Mandanteninformationen und darf die Beratungsstelle nicht ohne Supervisoren-Freigabe verlassen.
- Materialrecht des jeweiligen Rechtsgebiets (wird im Gutachten konkretisiert).

### Leitentscheidungen (exemplarisch für häufige Rechtsgebiete)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1: Rechtsfragen formulieren

Aus den Fallnotizen: Welche rechtlichen Fragen stellt dieser Fall?

Jede Frage als Obersatz formulieren. Nicht "Mietrecht" — sondern: "Kann die Mandantin die Miete mindern, weil die Heizung seit November defekt ist, und wenn ja, in welcher Höhe?"

Wenn mehrere Fragen vorliegen, bekommt jede ihren eigenen Prüfungsblock.

### Schritt 2: Gutachten-Gerüst aufbauen

Für jede Frage:

**Obersatz:** Als Fragesatz formuliert (aus Schritt 1).

**Norm/Definition:** Dies ist eine Recherche-Lücke, keine Schlussfolgerung. Was der/die Studierende finden muss:

> `[RECHERCHE ERFORDERLICH: § 536 BGB — Mietminderung wegen Sachmangel;
> Voraussetzungen: erheblicher Mangel, Anzeige durch Mieter (§ 536c BGB),
> keine Kenntnis bei Vertragsschluss (§ 536b BGB). Starten Sie mit:
> § 536 BGB, dann Rspr. zu Heizungsausfall als erheblicher Mangel.
> Vgl. /recherche-start für einen Recherchefahrplan.]`

Falls der Skill einen allgemeinen Normrahmen mit hoher Sicherheit kennt, kann dieser als Ausgangspunkt benannt werden — aber ausdrücklich als ungeprüft markiert:

> *Normrahmen (ungeprüft — für [Bundesland/Gericht] verifizieren):* § 536 Abs. 1 BGB
> gibt dem Mieter einen Anspruch auf verhältnismäßige Herabsetzung der Miete,
> wenn die Mietsache zu Mietbeginn oder während der Mietzeit mit einem Mangel
> behaftet ist, der ihre Tauglichkeit zum vertragsmäßigen Gebrauch aufhebt oder
> mindert. Die Minderung tritt kraft Gesetzes ein; einer Erklärung bedarf es nicht.
> `[PRÜFEN: aktuelle Fassung und einschlägige Rspr. für diesen Sachverhalt]`

**Subsumtion:** Hier steht die Analyse des Studierenden. Gerüst strukturieren, nicht ausfüllen:

> `[STUDENTISCHE ANALYSE: Norm auf Sachverhalt anwenden. Relevante Tatsachen:
> - Heizung seit November defekt — seit wann ist dies ein "erheblicher" Mangel?
> - Wann und wie hat die Mandantin den Vermieter informiert (§ 536c BGB)?
> - Ist ein Minderungsausschluss nach § 536b BGB möglich?
> - Wie hoch ist der Minderungsprozentsatz (Rspr. zu Heizungsausfall prüfen)?]`

**Ergebnis:** Bewusst offen lassen:

> `[STUDENTISCHES ERGEBNIS: Welche Schlussfolgerung ergibt sich aus Norm und
> Subsumtion? Wie stark ist der Anspruch? Welche Gegenargumente sind zu erwarten?]`

### Schritt 3: Stärken, Schwächen, offene Fragen

Separater Abschnitt nach den Prüfungsblöcken:

**Stärken (aus dem Sachverhalt — Studierende/-r soll diese testen):**
- [Hilfreiche Tatsache und warum]

**Schwächen (aus dem Sachverhalt — Studierende/-r soll Gewicht abschätzen):**
- [Problematische Tatsache und warum]
- `[UNSICHER: ob [X] tatsächlich eine Schwäche ist — hängt von [Norm/Rspr.] zu [Y] ab]`

**Offene Fragen (aus dem Gutachten nicht beantwortbar):**
- Sachverhaltlich: [Was wissen wir nicht über den Mandanten/die Mandantin?]
- Rechtlich: [Was erfordert Recherche?]
- Strategisch: [Ermessensentscheidungen für Studierenden/Supervisor]

## Ausgabeformat

```markdown
═══════════════════════════════════════════════════════════════════════
 KI-GESTÜTZTES GERÜST — DIE ANALYSE IST VON IHNEN ZU VERFASSEN
 Jeder [RECHERCHE ERFORDERLICH]- und [STUDENTISCHE ANALYSE]-Block ist
 eine Aufgabe, kein Platzhalter zum Löschen. Der Bildungswert liegt
 im Ausfüllen dieser Blöcke.
═══════════════════════════════════════════════════════════════════════

# Internes Rechtsgutachten: [Mandant] — [Rechtsfrage]

**Datum:** [Datum] | **Verfasser/-in:** [Studierender] | **Für:** [Supervisor]

---

## Kurzergebnis

[Mandat annehmen / Ablehnen, weil X / Weitere Informationen zu Y erforderlich —
nächster Schritt: Z]

---

## Geprüfte Fragen

1. [Frage als Obersatz]
2. [Frage als Obersatz]

---

## Frage 1: [Obersatz]

### Norm / Definition

[Normrahmen als Ausgangspunkt mit PRÜFEN-Flags und RECHERCHE ERFORDERLICH-Blöcken]

### Subsumtion

[STUDENTISCHE ANALYSE — Gerüst mit den relevanten Tatsachen]

### Ergebnis

[STUDENTISCHES ERGEBNIS — bewusst offen]

---

[Wiederholung für jede weitere Frage]

---

## Stärken

[Liste mit Vorbehalten]

## Schwächen

[Liste mit UNSICHER-Flags, wo zutreffend]

## Offene Fragen

**Sachverhaltlich:** [Liste]
**Rechtlich:** [Liste — diese fließen in /recherche-start ein]
**Strategisch:** [Liste — dies ist die Agenda für das Supervisorengespräch]

---

## Recherchelücken-Zusammenfassung

[Alle RECHERCHE ERFORDERLICH-Blöcke in einer Liste, damit der/die Studierende
sie systematisch abarbeiten kann — und /recherche-start für jede starten kann]

═══════════════════════════════════════════════════════════════════════
```

## Beispiel

**Szenario:** Mandant Koch, Mieter einer 3-Zimmer-Wohnung. Heizung defekt seit 01.11.2025. Vermieter nach mündlicher Anzeige vom 05.11.2025 untätig. Mandant zahlt weiter volle Miete 1.200 €/Monat.

Obersatz: "Hat Herr Koch einen Anspruch auf Mietminderung nach § 536 Abs. 1 BGB und wenn ja, in welcher Höhe?"

Normblock enthält: `[RECHERCHE ERFORDERLICH: § 536 BGB, § 536c BGB (Anzeigepflicht), Rspr. zu Heizungsausfall als erheblicher Mangel — AG/LG München, AG Hamburg; Höhe des Minderungsprozentsatzes]`. Subsumtionsblock enthält: `[STUDENTISCHE ANALYSE: Anzeigepflicht am 05.11.2025 erfüllt? Schriftform? Wie viele Monate betroffen?]`. Ergebnisblock offen.

## Risiken und typische Fehler

- **Analyse ohne Recherche ausfüllen:** Die RECHERCHE ERFORDERLICH-Blöcke sind keine Formalität. Ein Gutachten mit ungefüllten oder voreilig abgehakten Normblöcken ist noch kein Gutachten.
- **Unsicherheiten stillschweigend übergehen:** Wenn ein UNSICHER-Flag gesetzt ist, ist das ein Hinweis zur Recherche oder zum Supervisorengespräch, kein Tippfehler.
- **Kurzergebnis ohne Analyse:** Das Kurzergebnis am Anfang des Gutachtens ist eine Orientierung; es muss durch die Prüfungsblöcke belegt sein.
- **Gutachten verlässt Klinik ohne Freigabe:** Das interne Gutachten enthält vertrauliche Mandanteninformationen (§ 203 StGB, § 43a Abs. 2 BRAO). Kein Versand ohne Supervisoren-Freigabe.
- **Falsches Prüfungsschema:** Das Gerüst folgt der üblichen deutschen Gutachtenreihenfolge. Abweichende Prüfungsreihenfolgen (z. B. Prozessvoraussetzungen zuerst im Verwaltungsrecht) müssen vom Studierenden eigenständig berücksichtigt werden.

## Quellenpflicht

Jeder im Gerüst vorgeschlagene Normrahmen oder Entscheidungshinweis ist mit der Herkunft zu kennzeichnen: `[juris]`, `[beck-online]`, `[dejure]` für datenbankgestützte Belege; `[Modellwissen — verifizieren]` für aus dem Modell stammende Hinweise. Hinweise mit "verifizieren" tragen ein höheres Fehlerrisiko und sind zuerst zu prüfen. Tags nicht entfernen — sie sind das schnellste Signal für den Supervisor, welche Stellen besonderer Aufmerksamkeit bedürfen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund: KORRIGIERT. Skill hatte falschen Thementext: "Verbraucherrecht: Widerruf nach § 355 BGB". Echtes Thema: Eigenbedarfskündigung; Suizidgefahr des Mieters als Haertegrund (§ 574 BGB); Fortsetzung des Mietverhaeltnisses auf unbestimmte Zeit. Fundstelle korrigiert: NZM 2023 35 Rn. 24 (statt NJW 2023 142 Rn. 20). Quelle: dejure.org/2022,33020.
-->

## 3. `rbs-beratungshilfe-und-pkh-praxis`

**Fokus:** Beratungshilfe BerHG und PKH in der Praxis: Antrag beim Amtsgericht, Berechtigung Einkommen, Vermoegen, Wahrnehmungsbefugnis Anwalt. Schnittstelle PKH-Antrag. Mustertexte und Berechtigungsnachweise.

# Rbs: Beratungshilfe-Praxis

## Spezialwissen: Rbs: Beratungshilfe-Praxis
- **Spezialgegenstand:** Rbs: Beratungshilfe-Praxis / rbs beratungshilfe und pkh praxis. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BerHG, PKH.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
