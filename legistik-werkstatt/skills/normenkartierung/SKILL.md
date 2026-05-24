---
name: normenkartierung
description: "Kartiert alle bestehenden Normen die durch das geplante Vorhaben beruehrt werden. Stammgesetz Verordnungsverordnungen Folgenormen Verweisnetz. Such-Strategie BGBl-Online Bundesrecht.de Landesrecht-Portal Juris BeckOnline. Aufbau einer Aenderungsliste je Norm Paragraf Aenderungsart Einfuegen Aendern Aufheben Folgeaenderung. Identifiziert Verweisketten und Domino-Wirkungen. Pruefung ob Bezugsnormen aktuell gelten oder bereits in anderem Verfahren geaendert werden. Endet mit Aenderungsmatrix als Grundlage fuer Referentenentwurf und Synopse. Anschluss `terminologie-konsistenz` und `zirkelschluss-pruefen`."
---

# Normenkartierung

> Ein Eingriff geschieht nie isoliert. Jede Norm steht in einem Verweisnetz.

## Schritt 1 - Hauptzielgesetz finden

Wo soll die neue Regelung leben? Stammgesetz identifizieren (z.B. HGB, BGB, ZPO, FamFG, GO, BauGB).

## Schritt 2 - Direkte Folgenormen suchen

In welchen anderen Gesetzen wird auf das Hauptzielgesetz verwiesen? Im Internet:

- gesetze-im-internet.de
- buzer.de (Änderungsgeschichte)
- DIP des Bundestages
- BeckOnline-Verweisindex
- Juris-Linkliste
- Landesrecht-Portale (Bayern, NRW etc.)

## Schritt 3 - Verordnungs- und Satzungsstrecke

Welche Verordnungen sind auf dem Hauptzielgesetz erlassen? Welche Satzungen rekurrieren auf das Gesetz?

## Schritt 4 - Begriffsdefinitionen

Wenn das Vorhaben einen Begriff einführt: existiert dieser Begriff schon woanders? Mit gleicher Definition? Mit abweichender Definition? Kollidiert?

## Schritt 5 - Änderungsmatrix aufbauen

| Lfd | Norm | Paragraf | Änderungsart | Inhalt | Grund |
|---|---|---|---|---|---|
| 1 | HGB | 33 | Änderung | Pflicht-Postfach | Hauptregelung |
| 2 | HGB | 13d | Änderung | Zweigniederlassungen einbezogen | Folgeaenderung |
| 3 | ZPO | 130d | Erweiterung | Zustellung an Pflicht-Postfach | Anpassung Zustellrecht |
| 4 | FamFG | 14 | Änderung | Bekanntgabe an Postfach | Anpassung |
| 5 | DSGVO-Anpassungs-G | - | - | Verweis prüfen | Datenschutz |

## Schritt 6 - Verweisketten prüfen

Wenn Norm A auf Norm B verweist und sich B aendert, muss Norm A prüfen, ob der Verweis noch passt. Verweisketten über mehrere Gesetze sind heimtueckisch.

## Schritt 7 - Paralleles Gesetzgebungsverfahren?

Wird eine der zu aendernden Normen zur gleichen Zeit in einem anderen Gesetzgebungsverfahren geändert? Dann Abstimmung mit dem anderen Verfahren über Reihenfolge oder Änderungsbefehl.

## Schritt 8 - EU-Normen, internationale Bezüge

Welche EU-Richtlinien oder Verordnungen werden beruehrt? Welche völkerrechtlichen Verträge sind betroffen?

## Ausgabe

Änderungsmatrix als Markdown- und Excel-Vorlage. Eintrag in das Auftragsblatt: Liste der zu aendernden Normen.

## Anschluss

`terminologie-konsistenz`, `zirkelschluss-pruefen`, dann `referentenentwurf-bauen`.
