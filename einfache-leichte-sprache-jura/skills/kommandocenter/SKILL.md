---
name: kommandocenter
description: "Kanzlei oder Behörde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualitaetsprüfung. Output Projekt-Plan Skill-Routing. Abgrenzung zu..."
---

# Kommandocenter

Dieser Einstieg führt in jede Übertragung juristischer Texte in
Einfache Sprache oder Leichte Sprache.

## Triage zu Beginn
1. Einfache Sprache oder Leichte Sprache — Zielgruppe bekannt?
2. Welches Format: Brief, Bescheid, Formular, Website, Flyer, Gerichtsinformation?
3. Darf der Text inhaltlich gekuerzt werden oder muss alles erhalten bleiben?
4. Gibt es einen institutionellen Hausstil oder Prüfgruppen für Leichte Sprache?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Barrierefreiheit: Behörden müssen Informationen in Leichter Sprache oder Einfacher Sprache bereitstellen
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung (gilt für öffentliche Stellen)
- § 43 SGB I — Beratungspflicht sozialrechtlich in verstaendlicher Sprache
- § 58 VwGO — Rechtsbehelfsbelehrung: Klarheit als Wirksamkeitsvoraussetzung

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Template: Routing-Entscheidung

**Adressat-Bestimmung:**

| Frage | Antwort |
|---|---|
| Zielgruppe | [Bezeichnung] |
| Modus | Einfache Sprache / Leichte Sprache |
| Format | Brief / Bescheid / Website / Formular |
| Vollstaendigkeit | vollstaendig / Zusammenfassung OK |
| Hausstil vorhanden | ja/nein |
| Prüfgruppe vorhanden | ja/nein |

**Naechster Schritt:** Lade `elsj-einfache-sprache` oder `elsj-leichte-sprache` + immer `elsj-juristische-sicherung`.

## Erste Entscheidung

Frage zuerst:

1. Soll der Text in **Einfache Sprache** oder in **Leichte Sprache**?
2. Wer soll den Text lesen?
3. Was soll die Person danach verstehen oder tun?
4. In welchem Format wird der Text genutzt: Brief, Website, Formular,
 Vertragserklärung, Bescheid, Gerichtsinformation, E-Mail, Flyer oder Video?
5. Darf der Text stark gekürzt werden oder muss alles vollständig bleiben?

Wenn die Nutzerin oder der Nutzer unsicher ist, erkläre knapp:

- Einfache Sprache bleibt näher an Standardsprache.
- Leichte Sprache ist deutlich stärker vereinfacht und braucht idealerweise
 eine Prüfung durch Personen aus der Zielgruppe.

## Workflow

### 1. Ausgangstext sichern

Niemals direkt überschreiben. Arbeite mit vier Ebenen:

- Originaltext,
- Bedeutungs-Matrix,
- verständliche Fassung,
- Prüfprotokoll.

### 2. Bedeutungs-Matrix erstellen

Extrahiere vor der Übertragung:

| Feld | Inhalt |
| --- | --- |
| Wer handelt? | Person, Behörde, Gericht, Gegner, Anwalt |
| Was ist entschieden oder verlangt? | Zahlung, Handlung, Unterlassung, Frist |
| Welche Rechtsfolge droht? | Verlust, Klage, Vollstreckung, Kosten, Sanktion |
| Welche Wahl hat die Person? | zahlen, widersprechen, kündigen, nachfragen |
| Welche Frist gilt? | Datum, Beginn, Zugang, Berechnung |
| Welche Begriffe müssen erklärt werden? | Bescheid, Widerspruch, Rechtskraft, Haftung |
| Was darf nicht vereinfacht werden? | Ausnahme, Voraussetzung, Betrag, Rangfolge |

### 3. Modus wählen

Lade danach:

- `elsj-einfache-sprache`, wenn Einfache Sprache gewünscht ist.
- `elsj-leichte-sprache`, wenn Leichte Sprache gewünscht ist.
- `elsj-juristische-sicherung` immer parallel als Prüfschritt.
- `elsj-qualitaetsgate` vor Herausgabe.

### 4. Rückfragen nur wenn nötig

Stelle höchstens fünf Rückfragen auf einmal. Gute Rückfragen sind:

- Soll die Rechtsgrundlage im Text bleiben oder in eine Box?
- Soll der Text direkt an die betroffene Person gerichtet sein?
- Muss die Fassung vollständig sein oder reicht eine verständliche
 Zusammenfassung?
- Gibt es einen Hausstil für Leichte Sprache?
- Wurde eine Prüfgruppe beauftragt?

### 5. Ausgabe

Liefere bei jedem Ergebnis:

1. **Fassung** in gewähltem Modus.
2. **Kurzprotokoll**, welche juristischen Inhalte erhalten wurden.
3. **Glossar** für schwere Wörter.
4. **Offene Prüfungen**, insbesondere Nutzerprüfung bei Leichter Sprache.
