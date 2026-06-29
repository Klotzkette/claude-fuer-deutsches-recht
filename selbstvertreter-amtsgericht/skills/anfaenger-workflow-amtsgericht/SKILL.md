---
name: anfaenger-workflow-amtsgericht
description: "Skill: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Anfänger-Amtsgericht

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

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

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 23 GVG
- § 114 FamFG
- § 156 StGB
- § 185 GVG
- § 41 GKG
- § 12 GKG
- § 7 StVG
- § 17 GKG
- § 48 GKG
- § 71 GVG
- § 23a GVG
- § 63 GKG

### Leitentscheidungen

- BGH VI ZR 67/15
