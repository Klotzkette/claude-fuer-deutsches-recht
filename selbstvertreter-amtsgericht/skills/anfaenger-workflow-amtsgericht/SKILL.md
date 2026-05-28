---
name: anfaenger-workflow-amtsgericht
description: "Geführter Anfänger-Workflow für Bürgerinnen und Bürger vor dem Amtsgericht: fragt Rolle, Fristen, Streitwert, Gericht, Verfahrensstand und Unterlagen ab; erklärt jeden Schritt in einfacher Sprache; routet zu Klage, Klageerwiderung, Beweis, PKH, Termin, Urteil und Rechtsmittel."
---

# Anfänger-Workflow Amtsgericht

## Zweck

Dieser Skill ist der sehr geführte Einstieg für Menschen, die noch nie vor Gericht waren. Er soll nicht einschüchtern, sondern ordnen: Was liegt vor? Was läuft gerade? Was muss heute passieren? Was kann später kommen? Welche Spezial-Skills aus diesem Plugin helfen als nächstes?

Der Skill arbeitet in Sie-Form, mit kurzen Sätzen und ohne Juristenjargon. Fachbegriffe werden erst dann erklärt, wenn sie gebraucht werden.

## Sofortfrage

Fragen Sie zu Beginn knapp:

**Wie viel Führung wünschen Sie gerade?**

- **Sehr geführt:** Bitte jeden Schritt erklären und nur eine Aufgabe auf einmal.
- **Normal geführt:** Bitte klare Reihenfolge, Fristen und passende Skills.
- **Kurzmodus:** Bitte nur Risiken, nächster Schritt und Output.

Wenn ein Gerichtsschreiben, eine Klage, ein Urteil, eine Ladung oder eine Frist sichtbar ist, kommt der Fristenscan immer zuerst.

## Erste Triage

Erfassen Sie nur diese Punkte:

| Punkt | Frage |
|---|---|
| Rolle | Sind Sie Kläger, Beklagter oder noch vor der Klage? |
| Verfahrensstand | Mahnung, Mahnbescheid, Klage, Klageerwiderung, Termin, Urteil, Vollstreckung? |
| Frist | Welches Datum steht auf dem Umschlag oder Schreiben, wann kam es an? |
| Streitwert | Um wie viel Geld oder welchen Gegenstand geht es? |
| Gericht | Amtsgericht, Landgericht, Familiengericht oder etwas anderes? |
| Unterlagen | Bescheid, Vertrag, Rechnung, Fotos, Chats, Zeugen, Urteil, Ladung? |
| Ziel | Klage einreichen, verteidigen, Termin vorbereiten, Vergleich prüfen, Rechtsmittel überlegen? |

## Arbeitslogik

### 1. Gefahr zuerst

Markieren Sie zuerst:

- Notfrist oder gerichtliche Frist;
- drohendes Versäumnisurteil;
- falsches Gericht oder Anwaltszwang;
- drohende Verjährung;
- Termin in den nächsten 14 Tagen;
- Vollstreckung oder Kontopfändung;
- Familiensache mit möglichem Anwaltszwang.

### 2. In Alltagssprache erklären

Formulieren Sie immer ein Kurzbild:

- **Was ist das Schreiben?**
- **Was will das Gericht oder die Gegenseite?**
- **Was müssen Sie jetzt tun?**
- **Was passiert, wenn Sie nichts tun?**

### 3. Nur ein nächster Schritt

Geben Sie dem Nutzer am Ende genau einen nächsten Arbeitsschritt, wenn die Lage angespannt ist. Bei ruhiger Lage dürfen drei Schritte genannt werden.

## Skill-Routing

| Lage | Nächster Skill |
|---|---|
| Erste Orientierung | `orientierung-selbstvertreter-amtsgericht` |
| Zuständigkeit oder Streitwert unklar | `zulassungsgrenzen-check-amtsgericht` |
| Anwaltspflicht möglich | `anwaltszwang-pruefen-78-zpo` |
| Klage vorbereiten | `klage-zusammenstellen-komplettes-bundle-amtsgericht` |
| Klage bekommen | `klageerwiderung-checkliste-alle-punkte` |
| Beweise fehlen | `beweismittel-vorab-sammeln-checkliste` |
| Kosten unklar | `kostenrisiko-streitwert-berechnen-gkg` |
| Gerichtstermin | `terminvorbereitung-checkliste` |
| Urteil liegt vor | `urteil-pruefen-313-zpo` und `berufung-amtsgericht-511-zpo` |
| Unsichere Argumentation | `rechtsprechungschat-amtsgericht` |
| Vor Einreichung | `sanity-check-selbstvertretung-amtsgericht` |

## Ausgabeformat

**Kurzbild**
- Stand:
- Frist:
- Gericht:
- Rolle:
- Risiko:

**Ihr nächster Schritt**
1. [konkrete Handlung]

**Warum**
[Ein bis drei einfache Sätze.]

**Passender Plugin-Skill**
| Skill | Warum jetzt? | Ergebnis |
|---|---|---|
| `skill` | Grund | Output |

**Bitte nicht vergessen**
- Datum der Zustellung sichern.
- Alles kopieren oder fotografieren.
- Nichts nur telefonisch klären, wenn eine Frist läuft.

## Qualitätsregeln

- Keine falsche Sicherheit geben.
- Keine Rechtsmittel, Fristen oder Wertgrenzen erfinden.
- Bei Rechtsmittel, Landgericht, Familiengericht, Vollstreckung, hoher Gegenforderung oder unklarer Zustellung immer auf anwaltliche Prüfung oder Rechtsantragsstelle hinweisen.
- Trotzdem handlungsfähig bleiben: immer sagen, welcher sichere nächste Schritt jetzt möglich ist.
