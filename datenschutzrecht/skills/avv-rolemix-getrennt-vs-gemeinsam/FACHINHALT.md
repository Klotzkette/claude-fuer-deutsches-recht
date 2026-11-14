---
name: avv-rolemix-getrennt-vs-gemeinsam
description: "Für Rollenmix – Getrennt versus gemeinsam versus Auftragsverarbeitung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Rollenmix – Getrennt versus gemeinsam versus Auftragsverarbeitung

## Zweck / Purpose

Strukturierte Abgrenzung zwischen drei datenschutzrechtlichen Rollenmodellen in Mehr-Akteur-Konstellationen: getrennte Verantwortliche, gemeinsame Verantwortliche (Art. 26 DSGVO), Auftragsverarbeiter (Art. 28 DSGVO). Purpose (EN): Separate vs. joint vs. processor – role allocation in multi-actor data processing under GDPR.

## Wann dieses Modul hilft

- Zwei oder mehr Akteure verarbeiten dieselben personenbezogenen Daten und es ist unklar, welches Vertragsmodell zu schliessen ist.
- Aufsichtsbehoerde fragt nach Rollenzuordnung im Verarbeitungsverzeichnis (Art. 30 DSGVO).
- Mandant geht davon aus, "wir sind nur Auftragsverarbeiter" – Prüfung, ob nicht in Wahrheit Art. 26 DSGVO einschlaegig ist.
- Vor Abschluss eines Joint-Controller-Agreement oder AVV soll die Einstufung gesichert sein.

## Rechtlicher Rahmen

Die Fanpage-Entscheidung erging zur Richtlinie 95/46/EG. Die heutige Verarbeitung ist gesondert anhand von Artikel 4 Nummer 7 und Artikel 26 DSGVO zu prüfen; der Fallname allein begründet keine gemeinsame Verantwortlichkeit für jeden Verarbeitungsschritt.

- Art. 4 Nr. 7 DSGVO: Verantwortlicher entscheidet allein oder gemeinsam mit anderen über Zwecke und Mittel.
- Art. 26 DSGVO: Gemeinsam Verantwortliche.
- Art. 28 DSGVO: Auftragsverarbeiter.
- Art. 4 Nr. 9 DSGVO: Empfaenger.
- EDSA-Leitlinien 07/2020 zur Abgrenzung Verantwortlicher / Auftragsverarbeiter (Final 07.07.2021).
- EuGH C-25/17 (Zeugen Jehovas) – am Volltext für den konkreten Fall zu prüfen: Mitverantwortung durch organisatorische Mittel auch ohne unmittelbaren Datenzugang.
- EuGH, Urt. v. 05.06.2018 - Az. C-210/16, ECLI:EU:C:2018:388 (Wirtschaftsakademie Schleswig-Holstein / Fanpages); [Quelle und Prüfstand vom 25.09.2026](../../references/fanpage-entscheidung-quellenpruefung.md).
- EuGH C-40/17 (Fashion ID) – am Volltext für den konkreten Fall zu prüfen: Like-Button-Einbinder ist für Erhebung und Uebermittlung mitverantwortlich.

## Ablauf / Checkliste

1. **Zweck- und Mittelprueung.**

 | Frage | Verantwortlicher allein | Gemeinsam Verantwortlich | Auftragsverarbeiter |
 |---|---|---|---|
 | Wer legt Zweck fest? | Akteur A allein | Akteur A und Akteur B gemeinsam | Akteur A allein, Akteur B fuehrt aus |
 | Wer legt Mittel fest? | Akteur A | Beide oder Akteur B als wesentlicher Mitbestimmer | Akteur A bestimmt wesentliche Mittel, Akteur B technische Detailmittel |
 | Eigener Nutzen aus Daten? | Nur Akteur A | Beide ziehen Nutzen | Nur Akteur A |
 | Weisungsgebundenheit? | nicht relevant | nein, kollektive Entscheidung | ja, voll |

2. **EuGH-Indizienreihe.**

 - Wer entscheidet über Zweck der Verarbeitung? (Kerntest)
 - Wer bestimmt wesentliche Mittel (z. B. Tool-Auswahl, Speicherort, Loeschfristen)?
 - Wer profitiert wirtschaftlich von der Verarbeitung?
 - Besteht eine wechselseitige Abhaengigkeit?
 - Wird die Verarbeitung gemeinsam beworben oder organisiert?

3. **Negativindizien gegen Auftragsverarbeitung.**

 - Eigene Verarbeitung für eigene Werbung, eigenes KI-Training, eigene Statistik.
 - Eigene Anonymisierung mit nachgelagerter eigener Nutzung.
 - Eigene Rechtsdienstleistung (Inkasso, Steuerberatung, Rechtsanwaltsleistung) im Auftrag des Mandanten – meist Funktionsuebertragung statt Art. 28 (Querverweis: funktionsuebertragung-vs-auftragsverarbeitung).
 - Schaltung von Tracking-Pixeln auf eigener Webseite (regelmaessig Art. 26 mit dem Tracking-Anbieter).

4. **Negativindizien gegen Joint Control.**

 - Reiner Datenfluss zwischen zwei getrennten Geschäften ohne abgestimmte Verarbeitung.
 - Jeder Akteur hat eigene Rechtsgrundlage und eigenen Zweck.
 - Keine gemeinsame Bewerbung oder Organisation.

5. **Prüfraster (Stufenmodell).**

 - Stufe 1: Liegt eine Verarbeitung im Sinne von Art. 4 Nr. 2 DSGVO vor? (immer ja)
 - Stufe 2: Wer entscheidet über Zweck? Wenn nur einer: weiter Stufe 4. Wenn mehrere: weiter Stufe 3.
 - Stufe 3: Liegt gemeinsame Entscheidung auch über wesentliche Mittel oder gemeinsamer Nutzen vor? Wenn ja: Art. 26 DSGVO. Wenn nein: getrennte Verantwortliche.
 - Stufe 4: Ist der ausfuehrende Akteur weisungsgebunden und ohne eigenen Zweck? Wenn ja: Art. 28 DSGVO. Wenn nein: getrennte Verantwortliche oder Funktionsuebertragung.

## Mustertext / Template

Prüfvermerk-Vorlage zur Rollenzuordnung:

```
Pruefvermerk Rollenzuordnung DSGVO
-----------------------------------
Verarbeitung: [Beschreibung]
Akteur A: [Bezeichnung, Funktion]
Akteur B: [Bezeichnung, Funktion]
Datenkategorien: [Stamm-/Verkehrs-/Inhaltsdaten/Art. 9 DSGVO]
Betroffene: [Kategorien]

1. Zweck der Verarbeitung

 Wer entscheidet? [A allein / A und B gemeinsam / nur für A]
 Begruendung: [Sachverhaltsbasis]

2. Wesentliche Mittel

 Wer entscheidet? [A allein / A und B gemeinsam / A legt fest, B fuehrt aus]
 Indizien: [Tool-Auswahl, Speicherort, Loeschfristen, Sicherheitsmassnahmen]

3. Wirtschaftlicher Nutzen

 [Nur A / beide / A nutzt für Geschaeft, B nur für Entgelt]

4. Weisungsgebundenheit B?

 [voll / teilweise / keine]

5. EuGH-Linie

 Vergleichbar mit: [EuGH, Urt. v. 10.07.2018 - Az. C-25/17 / EuGH, Urt. v. 05.06.2018 - Az. C-210/16 / EuGH, Urt. v. 29.07.2019 - Az. C-40/17 / keine direkte Vergleichbarkeit].

6. Einordnung

 [ ] Akteur A allein verantwortlich (Art. 4 Nr. 7 DSGVO)
 [ ] Akteur A und B gemeinsam verantwortlich (Art. 26 DSGVO)
 [ ] Akteur A Verantwortlicher, Akteur B Auftragsverarbeiter (Art. 28 DSGVO)
 [ ] Getrennte Verantwortliche

7. Folgevertrag

 [ ] Joint-Controller-Vereinbarung Art. 26
 [ ] AVV Art. 28
 [ ] C2C-Datenuebermittlungsklausel
 [ ] kein gesonderter Vertrag erforderlich

Datum, Unterschrift Datenschutzbeauftragter
```

## Typische Drafting-Fehler

- AVV abgeschlossen, obwohl Joint Control vorliegt (Fanpage / Like-Button / Webtracking).
- Joint-Agreement abgeschlossen, obwohl getrennte Verantwortliche vorliegen (typischer Fall: Inkasso-Dienstleister).
- "Standardloesung AVV" ohne Prüfung.
- Berufsgeheimnistraeger als reine Auftragsverarbeiter behandelt (Funktionsuebertragung uebersehen).
- Tracking-Anbieter als Auftragsverarbeiter behandelt, obwohl er Daten für eigene Zwecke nutzt.

## Quellen Stand 06/2026

- Art. 4 Nr. 7, Art. 26, Art. 28 DSGVO.
- EDSA-Leitlinien 07/2020 (Final 07.07.2021), abrufbar über edpb.europa.eu.
- EuGH C-25/17 (Zeugen Jehovas) – konkreten Aussagegehalt am Volltext prüfen.
- EuGH, Urt. v. 05.06.2018 - Az. C-210/16, ECLI:EU:C:2018:388 (Wirtschaftsakademie Schleswig-Holstein / Fanpages); [Quelle und Prüfstand vom 25.09.2026](../../references/fanpage-entscheidung-quellenpruefung.md).
- EuGH C-40/17 (Fashion ID) – konkreten Aussagegehalt am Volltext prüfen.
- Volltexte über curia.europa.eu prüfen.
- Zitierweise: `../../../references/zitierweise.md`.
