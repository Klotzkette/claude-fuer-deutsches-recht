# Kopfdaten und äußere Form

Nutze diese Detailreferenz nur für den konkreten Arbeitsschritt. Quellenstatus und Grenzen älterer Anker stehen in der [Rechtsprüfung](../../../references/rechtsstand.md); für Zitate gilt die [Zitierweise](../../../../references/zitierweise.md).

## 1. Ziel

Die Formalia des Zeugnisses korrekt generieren, damit keine Berichtigungsansprüche aus formalen Mängeln entstehen.

## 2. Prüfposten

| Prüfposten | Soll | Typischer Mangel |
|---|---|---|
| Briefkopf | offizielles Firmenpapier mit vollständiger Anschrift | privates Papier, fehlende Anschrift, veraltete Adresse |
| Datum | Ausstellungsdatum plausibel nahe am Austrittsdatum | fehlendes Datum, unplausibel langes Intervall |
| Überschrift | „Arbeitszeugnis" oder „Zeugnis" | fehlt oder lautet „Beurteilung" (andere Signalwirkung) |
| Position | exakte Funktionsbezeichnung, ggf. mit Hierarchiestufe | zu niedrige Bezeichnung, fehlender Titel |
| Beschäftigungszeitraum | vollständig, ohne Lücken | Lücken, falsches Eintrittsdatum |
| Aufgabenkatalog | umfassend, Schlüsselverantwortungen erwähnt | unvollständig |
| Unterschrift | bei Papier eigenhändig durch den erkennbaren Aussteller oder Vertreter | Paraphe, unklarer Aussteller, fehlende Unterschrift |
| Format | individuelle Beurteilung in Fließtext | schulnotenartiges Ankreuz- oder Tabellenschema; nicht jede Aufgabenliste ist verboten |

## 3. Unterschrift und Aussteller

Bei Papierform muss die Unterschrift den Aussteller oder einen erkennbar für ihn handelnden Vertreter ausweisen. Maschinenschriftlicher Name, Funktion und tatsächliche Unterschrift werden auf Übereinstimmung geprüft. Eine bloße Paraphe genügt der Schriftform nicht. Auffällige Gestaltungen werden nur beanstandet, wenn sie aus Sicht eines objektiven Lesers Distanzierung oder mangelnde Ernstlichkeit vermitteln.

## 4. Fließtextgebot

Ein qualifiziertes Zeugnis in Tabellenform oder als Ankreuzschema erfüllt den Anspruch aus Paragraf 109 GewO regelmäßig nicht (BAG, Urteil vom 27.04.2021 - Az. 9 AZR 262/20).

## 5. Elektronische Form ab 1.1.2025

Seit dem Vierten Bürokratieentlastungsgesetz (in Kraft 1.1.2025) erlaubt Paragraf 109 Abs. 3 GewO die elektronische Form mit Einwilligung des Arbeitnehmers. Voraussetzung: qualifizierte elektronische Signatur (Paragraf 126a BGB). Einfaches PDF, Scan oder E-Mail genügen nicht.

Ohne ausdrückliche Einwilligung gilt: Papierzeugnis mit eigenhändiger Unterschrift.

## 6. Datum-Regeln

- Ausstellungsdatum sollte möglichst nah am Austrittsdatum liegen.
- Das gewünschte Datum muss zum tatsächlichen Ausstellungs- und Beendigungssachverhalt passen; keine automatische Rückdatierung.
- Ausstellungsdatum deutlich nach dem Austrittsdatum kann auf Verweigerung oder Verzögerung hindeuten - kein automatischer Berichtigungspunkt, aber Kontext prüfen.

## 7. Bereitstellung

Arbeitspapiere und damit grundsätzlich auch Zeugnisse sind am Sitz des Arbeitgebers abzuholen, soweit Ort, Vereinbarung oder Zumutbarkeit nichts anderes ergeben. Vor einem Versandverlangen werden Vertrag, betriebliche Handhabung und konkrete Umstände geprüft.

## 8. Rechtsprechungsanker

- BAG, Urteil vom 27.04.2021 - Az. 9 AZR 262/20, Rn. 10 bis 20: Äußere Form und Inhalt folgen dem Zeugniszweck; ein qualifiziertes Zeugnis in schulnotenartiger Tabellenform genügt regelmäßig nicht.
- BAG, Urteil vom 21.09.1999 - Az. 9 AZR 893/98, herangezogen in BAG 9 AZR 262/20, Rn. 11: Das Zeugnis muss den im Geschäftsleben selbstverständlich erwarteten Formanforderungen entsprechen.
- BAG, Urteil vom 14.06.2016 - Az. 9 AZR 8/15, Rn. 14 bis 20 betrifft einheitlich verlangte Änderungen von Beschäftigungs-, Beendigungs- und Ausstellungsdatum bei Prozessbeschäftigung. Keine allgemeine Entscheidung gegen Rückdatierung bei Zeugnisberichtigung.
- BAG, Urteil vom 28.01.2025 - Az. 9 AZR 48/24, Rn. 17: Das Gericht bestätigt unter Hinweis auf BAG 5 AZR 848/93 den Grundsatz der Holschuld bei Arbeitspapieren.

## 9. Generier-Platzhalter für Formalia

```
[Firmenname] | [Straße, PLZ Ort]

Arbeitszeugnis

[Ort], [Datum]

[Unterschrift]
[Vorname Nachname]
[Funktion]
```

## 10. Stolpersteine

- Unterzeichner und Maschinenschrift-Name stimmen nicht überein - häufiger Praxisfehler.
- Datum fehlt - ist ein formaler Mangel.
- Zeugnis auf privatem Briefpapier statt Firmenpapier.

## 11. Anti-Muster

- Ein Datum vor dem Austritt ungeprüft als Fehler behandeln; Zwischenzeugnis, vorläufiges Zeugnis und spätere Endbeurteilung unterscheiden.
- Einen Unterzeichner einsetzen, dessen Name, Funktion oder Vertretungsrolle nicht erkennbar ist.
- Qualifiziertes Zeugnis mit grafischer Tabelle (Schulnoten-Schema) formatieren.

## 12. Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
