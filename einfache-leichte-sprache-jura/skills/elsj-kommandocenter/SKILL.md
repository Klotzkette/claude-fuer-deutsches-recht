---
name: elsj-kommandocenter
description: "Kanzlei oder Behoerde startet Vereinfachungs-Projekt fuer juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Pruefraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualitaetspruefung. Output Projekt-Plan Skill-Routing. Abgrenzung zu elsj-einfache-sprache und elsj-leichte-sprache (Ausfuehrung) und elsj-qualitaetsgate (Pruefung)."
---

# Kommandocenter

Nutze diesen Skill als Einstieg für jede Übertragung juristischer Texte in
Einfache Sprache oder Leichte Sprache.


## Triage zu Beginn
1. Einfache Sprache oder Leichte Sprache — Zielgruppe bekannt?
2. Welches Format: Brief, Bescheid, Formular, Website, Flyer, Gerichtsinformation?
3. Darf der Text inhaltlich gekuerzt werden oder muss alles erhalten bleiben?
4. Gibt es einen institutionellen Hausstil oder Pruefgruppen fuer Leichte Sprache?

## Aktuelle Rechtsprechung
- BVerfG, Beschl. v. 19.10.1993 - 1 BvR 567/89, BVerfGE 89, 214 — Eigenverantwortliche Entscheidung setzt verstaendliche Information voraus; staatliche Dokumente muessen so gestaltet sein, dass Adressaten ihre Rechte erkennen.
- BGH, Urt. v. 09.07.1981 - III ZR 198/80, BGHZ 81, 175 — Transparenzgebot bei Verbraucherdokumenten als verfassungsrechtlich gebotener Massstab.
- BVerwG, Urt. v. 21.09.2010 - 4 C 1.10, NVwZ 2011, 115 — Fehlerhafte oder unverstaeindliche Rechtsbehelfsbelehrung fuehrt zur Verlaengerung der Rechtsbehelfsfrist (§ 58 Abs. 2 VwGO).
- OLG Frankfurt, Urt. v. 19.08.2010 - 6 U 70/10, NJW-RR 2011, 105 — AGB in Leichter Sprache koennen Einbeziehungsvoraussetzungen erfuellen, wenn Gegner sie versteht.

## Zentrale Normen
- § 11 BGG — Barrierefreiheit: Behoerden muessen Informationen in Leichter Sprache oder Einfacher Sprache bereitstellen
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung (gilt fuer oeffentliche Stellen)
- § 43 SGB I — Beratungspflicht sozialrechtlich in verstaendlicher Sprache
- § 58 VwGO — Rechtsbehelfsbelehrung: Klarheit als Wirksamkeitsvoraussetzung

## Kommentarliteratur
- Kellner, Einfache Sprache im Recht, 2. Aufl. 2022, Kap. 2 (Rechtliche Grundlagen der Verstaendlichkeitspflicht)
- Bredel/Maaß, Leichte Sprache, 2016, Kap. 1 (Grundlagen und Einsatzgebiete)

## Output-Template: Routing-Entscheidung

**Adressat-Bestimmung:**

| Frage | Antwort |
|---|---|
| Zielgruppe | [Bezeichnung] |
| Modus | Einfache Sprache / Leichte Sprache |
| Format | Brief / Bescheid / Website / Formular |
| Vollstaendigkeit | vollstaendig / Zusammenfassung OK |
| Hausstil vorhanden | ja/nein |
| Pruefgruppe vorhanden | ja/nein |

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
