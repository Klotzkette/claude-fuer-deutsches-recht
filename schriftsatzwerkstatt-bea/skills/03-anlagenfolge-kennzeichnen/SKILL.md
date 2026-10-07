---
name: 03-anlagenfolge-kennzeichnen
description: 'Ordnet vorhandene Anlagen technisch zum fertigen Schriftsatz, setzt eine bestehende K- oder B-Nummerierung fort und bereitet die sichtbare Kennzeichnung rechts oben vor. Verwenden bei Klage, Erwiderung, Replik oder weiterem Schriftsatz mit gemischten Belegen. Prüft Anlagenzitate, Dubletten, Seitenfolge und fehlende Dateien, ohne Beweiswert oder juristischen Inhalt neu zu bewerten.'
---

# Anlagenfolge ordnen und kennzeichnen

## Zweck und Anwendungsfall

Dieser Skill bringt Schriftsatzzitate, Quelldateien, sichtbare Anlagenbezeichnungen und spätere Dateinamen in eine widerspruchsfreie Reihenfolge. Er entscheidet nicht, ob eine Anlage rechtlich erforderlich oder beweiskräftig ist.

## Eingaben

- gesperrter Hauptschriftsatz aus Skill 02.
- Quelleninventar und alle für den Versand vorgesehenen Anlagen.
- relative Quellenpfade und aktuelle SHA256-Werte aus der Ordnerannahme.
- Parteirolle K oder B.
- Liste bereits eingereichter Anlagen und höchste vergebene Nummer.
- vorhandenes Anlagenverzeichnis oder Konvolutstruktur.

## Ablauf / Checkliste

1. Sämtliche Anlagenzitate im Hauptschriftsatz in Reihenfolge erfassen.
2. Jedes Zitat genau einer Quelldatei oder einem klar benannten Konvolut samt relativem Quellenpfad und SHA256 zuordnen.
3. Bereits eingereichte Nummern sperren. Neue Anlagen beginnen nach der höchsten vergebenen K-/B-Nummer; bei Replik oder Folgeschriftsatz niemals bei 1 neu starten.
4. Fehlende Zitate, nicht zitierte Dateien, doppelte Inhalte, widersprüchliche Nummern und unechte Konvolute markieren.
5. Unterschiedliche Dokumente nur dann als Konvolut führen, wenn der Schriftsatz sie so bezeichnet und ein Inhaltsblatt/Seitenplan vorhanden ist.
6. Sichtbare Kennzeichnung planen: erste Seite rechts oben `Anlage K 7` oder `Anlage B 4`.
7. Ist dort kein freier Platz, weißen Rand oder Anlagen-Deckblatt vorsehen. Briefkopf, Datum, Barcode, Seitenzahl, Inhalt und Signatur nicht verdecken.
8. Bereits elektronisch signierte PDF weder stempeln noch mit Rand oder Deckblatt verbinden. Signiertes Original unverändert bewahren und jeden Kennzeichnungsweg vor einer Änderung durch die verantwortliche Person entscheiden lassen.
9. Anlagenplan für Konvertierung und Dateinamen sperren. Spätere Änderung startet den Abgleich erneut.

## Quellenpflicht

Verbindlich sind der Abschnitt zur Anlagenkennzeichnung im [Dateinamen- und Manifeststandard](../../references/dateinamen-und-manifest.md), die unveränderbare Quellenkette aus [Inhaltstreue und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md) und die Anlagenpunkte im [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Es werden keine materiell-rechtlichen oder gerichtlichen Rechtsprechungsanker ergänzt.

## Ausgabeformat

| Reihenfolge | Zitat im Schriftsatz | Quelle mit SHA256 | Bereits eingereicht | Zielanlage | Kennzeichnungsweg | Status |
|---:|---|---|---|---|---|---|
| 02 | Anlage K 7 | `mietkonto.xlsx` | nein | K 7 | Rand rechts oben | bereit |

Zusätzlich: fehlende/zuviel vorhandene Dateien, gesperrte Altanlagen und genau ein Übergabestatus an Skill 04. Das Ergebnis erläutert jede Abweichung in vollständigen Sätzen.

## Beispiele

- K 1 bis K 6 sind bereits eingereicht: neue Anlagen beginnen mit K 7.
- Schriftsatz nennt K 8, Ordner enthält zwei verschiedene Dateien `K8`: roter Zuordnungskonflikt.
- Bild füllt erste Seite vollständig: Anlagen-Deckblatt statt Überstempelung des Bildinhalts.
