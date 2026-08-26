---
name: mandantenbrief-memo-rbs-beratungshilfe
description: "Für /mandantenbrief: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik."
---

# /mandantenbrief

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

1. Lade `CLAUDE.md` → Fachbereich, Sprachniveau-Einstellungen, Anleiterpflicht.
2. Ermittle: Was soll der Brief mitteilen? Welchen nächsten Schritt soll der Mandant tun?
3. Schreibe den Brief in einfacher Sprache (Ziel: B1/B2; bei besonderen Bedarfen: leichte Sprache A2).
4. Kein Juristenjargon. Kurze Sätze. Aktive Formulierungen.
5. Ausgabe: Entwurf mit KI-Label. Versand erst nach Anleiterpfreigabe.

---

### Mandantenbrief in einfacher Sprache

## Triage zu Beginn
1. Was soll der Brief mitteilen: Ergebnis einer Prüfung, Verfahrensstand, konkreter naechster Schritt oder Ablehnung?
2. Auf welchem Sprachniveau soll der Brief verfasst werden: B1/B2 Standard oder Leichte Sprache A2 bei besonderem Bedarf?
3. Enthaelt der Brief Angaben über Dritte oder interne Bewertungen, die im Mandantenbrief nicht erscheinen dürfen?
4. Hat der anleitende Volljurist den Briefentwurf bereits freigegeben oder ist das Gate noch ausstehend?

## Zentrale Normen
- BORA § 11 — Mitteilungspflicht: Mandant ist über wesentliche Verfahrensschritte zu informieren
- § 43a Abs. 2 BRAO — Verschwiegenheit: Mandantenbrief darf keine Drittinformationen offenbaren
- § 6 Abs. 2 Nr. 2 RDG — Anleitungspflicht: Mandantenbrief von Studentenn erfordert Anleiterpruefung und -freigabe
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur für Mandanten bestimmte Informationen im Brief

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
Wenden Sie sich an: [Name des Studentenn / der Beratungsstelle]
Telefon: [...] | E-Mail: [...] | Sprechzeiten: [...]

Mit freundlichen Grüßen

[Name des Studentenn / Kürzel]
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

## Risiken / typische Fehler

- **Juristischer Rat im Mandantenbrief ohne Freigabe:** Kein Brief darf Aussagen enthalten wie "Sie werden gewinnen" oder "Die Klage hat gute Chancen" – das ist unzulässige Prognose ohne Anleiterbilligung.
- **Falsches Fristenverständnis beim Mandanten:** Der Brief muss Fristen, die der Mandant wahren muss (z. B. Vorlage von Dokumenten), klar und mit genauen Daten benennen. Keine vagen Formulierungen wie "möglichst bald".
- **Keine Rückfrage-Möglichkeit:** Mandantenbrief ohne Kontaktangabe ist wertlos. Immer Erreichbarkeit der Beratungsstelle angeben.
- **Vertraulichkeit verletzt:** Keine Drittdaten (z. B. Informationen über den Vermieter, den Arbeitgeber) im Brief an den Mandanten – es sei denn, der Mandant hat alle relevanten Informationen ohnehin selbst geliefert.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
