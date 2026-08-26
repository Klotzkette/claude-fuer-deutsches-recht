---
name: kopfdaten-und-aussere-form
description: "Prüft Briefkopf, Datum, Überschrift, Beschäftigungszeitraum, Fließtext, Unterzeichner und Papier- oder elektronische Form eines Arbeitszeugnisses."
---

# Kopfdaten und äußere Form

## Ziel

Die Formalia des Zeugnisses korrekt generieren, damit keine Berichtigungsansprüche aus formalen Mängeln entstehen.

## Prüfposten

| Prüfposten | Soll | Typischer Mangel |
|---|---|---|
| Briefkopf | offizielles Firmenpapier mit vollständiger Anschrift | privates Papier, fehlende Anschrift, veraltete Adresse |
| Datum | Ausstellungsdatum plausibel nahe am Austrittsdatum | fehlendes Datum, unplausibel langes Intervall |
| Überschrift | „Arbeitszeugnis" oder „Zeugnis" | fehlt oder lautet „Beurteilung" (andere Signalwirkung) |
| Position | exakte Funktionsbezeichnung, ggf. mit Hierarchiestufe | zu niedrige Bezeichnung, fehlender Titel |
| Beschäftigungszeitraum | vollständig, ohne Lücken | Lücken, falsches Eintrittsdatum |
| Aufgabenkatalog | umfassend, Schlüsselverantwortungen erwähnt | unvollständig |
| Unterschrift | bei Papier eigenhändig durch den erkennbaren Aussteller oder Vertreter | Paraphe, unklarer Aussteller, fehlende Unterschrift |
| Format | Fließtext | Ankreuzschema, Tabelle, Stichpunkte |

## Unterschrift und Aussteller

Bei Papierform muss die Unterschrift den Aussteller oder einen erkennbar für ihn handelnden Vertreter ausweisen. Maschinenschriftlicher Name, Funktion und tatsächliche Unterschrift werden auf Übereinstimmung geprüft. Eine bloße Paraphe genügt der Schriftform nicht. Auffällige Gestaltungen werden nur beanstandet, wenn sie aus Sicht eines objektiven Lesers Distanzierung oder mangelnde Ernstlichkeit vermitteln.

## Fließtextgebot

Ein qualifiziertes Zeugnis in Tabellenform oder als Ankreuzschema erfüllt den Anspruch aus Paragraf 109 GewO regelmäßig nicht (BAG, Urteil v. 27.04.2021 – 9 AZR 262/20).

## Elektronische Form ab 1.1.2025

Seit dem Vierten Bürokratieentlastungsgesetz (in Kraft 1.1.2025) erlaubt Paragraf 109 Abs. 3 GewO die elektronische Form mit Einwilligung des Arbeitnehmers. Voraussetzung: qualifizierte elektronische Signatur (Paragraf 126a BGB). Einfaches PDF, Scan oder E-Mail genügen nicht.

Ohne ausdrückliche Einwilligung gilt: Papierzeugnis mit eigenhändiger Unterschrift.

## Datum-Regeln

- Ausstellungsdatum sollte möglichst nah am Austrittsdatum liegen.
- Das gewünschte Datum muss zum tatsächlichen Ausstellungs- und Beendigungssachverhalt passen; keine automatische Rückdatierung.
- Ausstellungsdatum deutlich nach dem Austrittsdatum kann auf Verweigerung oder Verzögerung hindeuten — kein automatischer Berichtigungspunkt, aber Kontext prüfen.

## Bereitstellung

Arbeitspapiere und damit grundsätzlich auch Zeugnisse sind am Sitz des Arbeitgebers abzuholen, soweit Ort, Vereinbarung oder Zumutbarkeit nichts anderes ergeben. Vor einem Versandverlangen werden Vertrag, betriebliche Handhabung und konkrete Umstände geprüft.

## Rechtsprechungsanker

- BAG, Urteil vom 27.04.2021 - 9 AZR 262/20, Rn. 10 bis 20: Äußere Form und Inhalt folgen dem Zeugniszweck; ein qualifiziertes Zeugnis in schulnotenartiger Tabellenform genügt regelmäßig nicht.
- BAG, Urteil vom 21.09.1999 - 9 AZR 893/98, herangezogen in BAG 9 AZR 262/20, Rn. 11: Das Zeugnis muss den im Geschäftsleben selbstverständlich erwarteten Formanforderungen entsprechen.
- BAG, Urteil vom 14.06.2016 - 9 AZR 8/15, Rn. 12 bis 16: Die Wahrheitspflicht erfasst auch Datumsangaben; ein bestimmtes Rückdatum wird nicht allein wegen seiner Außenwirkung geschuldet.
- BAG, Urteil vom 28.01.2025 - 9 AZR 48/24, Rn. 17: Das Gericht bestätigt unter Hinweis auf BAG 5 AZR 848/93 den Grundsatz der Holschuld bei Arbeitspapieren.

## Generier-Platzhalter für Formalia

```
[Firmenname] | [Straße, PLZ Ort]

Arbeitszeugnis

[Ort], [Datum]

[Unterschrift]
[Vorname Nachname]
[Funktion]
```

## Stolpersteine

- Unterzeichner und Maschinenschrift-Name stimmen nicht überein — häufiger Praxisfehler.
- Datum fehlt — ist ein formaler Mangel.
- Zeugnis auf privatem Briefpapier statt Firmenpapier.

## Anti-Muster

- Datum des Zeugnisses deutlich vor dem Austrittsdatum setzen (noch aktives Arbeitsverhältnis).
- Einen Unterzeichner einsetzen, dessen Name, Funktion oder Vertretungsrolle nicht erkennbar ist.
- Qualifiziertes Zeugnis mit grafischer Tabelle (Schulnoten-Schema) formatieren.

## Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
