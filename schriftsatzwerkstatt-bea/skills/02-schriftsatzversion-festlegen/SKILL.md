---
name: 02-schriftsatzversion-festlegen
description: 'Sperrt die richtige, bereits fachlich freigegebene Schriftsatzfassung vor PDF-Konvertierung. Verwenden bei mehreren DOCX-, ODT- oder PDF-Versionen, Änderungsverfolgung, Kommentaren, Platzhaltern, verstecktem Text oder unklarem Unterschriftsblock. Prüft nur Version und technische Vollständigkeit, verändert keine juristischen Inhalte und liefert eine eindeutige Quellen- und Renderfassung.'
---

# Schriftsatzversion festlegen

## Zweck und Anwendungsfall

Dieser Skill verhindert, dass ein falscher Entwurf oder eine kommentierte Arbeitsfassung versendet wird. Er bestimmt gemeinsam mit der verantwortlichen Person genau eine Hauptquelle und friert ihren Hash für die weitere Werkstatt ein.

## Eingaben

- Quelleninventar aus Skill 01.
- mögliche Hauptfassungen und vorhandene Freigabevermerke.
- gewünschter Briefkopf beziehungsweise bestehendes Layout.
- Name/Funktion der verantwortlichen Person und Dokumenttyp.

## Ablauf / Checkliste

1. Versionen nach Dateiname, internem Dokumentdatum, Änderungsstand, Inhalt und Hash vergleichen. Das jüngste Dateidatum ist kein Freigabenachweis.
2. Bei Word/ODT prüfen: Änderungsverfolgung, Kommentare, ausgeblendeter Text, dynamische und externe Felder, verknüpfte Bilder, nicht eingebettete Schriften, Kopf-/Fußzeilen, Inhaltssteuerelemente, interne Notizen, Metadaten und ungelöste Platzhalter.
3. Bei PDF prüfen: Entwurfswasserzeichen, abweichende Seiten, Kommentare, Formulare, Signaturen, Passwortschutz und bereits vorhandene Anlagenkennzeichnungen.
4. Unklare Änderungen nicht annehmen oder verwerfen. Eine reale Person benennt die freigegebene Hauptfassung.
5. Antrag, Tatsachentext und Rechtsausführung nicht redigieren. Offensichtliche technische Platzhalter wie `[Datum]` oder `[Anlage]` nur melden.
6. Freigegebene Quelle mit relativem Pfad, Hash, Seiten-/Abschnittsstand und Freigabeperson dokumentieren.
7. Eine Render-Arbeitskopie erzeugen beziehungsweise für Skill 04 vormerken. Eine Cache-Fassung nur bei vollständigem Fingerprint-Treffer übernehmen; Quelle unverändert lassen.
8. Jede spätere Änderung am Hauptdokument hebt Versionssperre, PDF-Prüfung, Signaturstatus und Freigabe auf.

## Quellenpflicht

Es gelten der [ERV-Versandstandard](../../references/erv-versandstandard.md), die unveränderte Quellenführung aus dem [Dateinamen- und Manifeststandard](../../references/dateinamen-und-manifest.md), der [Inhaltstreue- und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md) und die Versionspunkte im [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Keine Rechtsprechungsprüfung.

## Ausgabeformat

1. Versionsvergleich mit Pfad, Hash, Dokumentdatum, Markup-Status und Entscheidung.
2. gesperrte Hauptquelle mit Versions-ID.
3. technische Lückenliste.
4. Übergabe an Skill 03 und 04.

Der Versionsvermerk wird in vollständigen Sätzen ausgegeben und nennt ausdrücklich, wer die Fassung festgelegt hat. Der Skill erteilt selbst keine fachliche Freigabe.

## Beispiele

- `Replik_final.docx` enthält Kommentare, `Replik_final_2.docx` nicht: reale Bestätigung einholen; nicht still `final_2` wählen.
- Hauptschriftsatz ist bereits eine signierte PDF: Signaturstatus erfassen und keine inhaltsändernde Konvertierung vornehmen.
- Briefkopf fehlt, Inhalt ist freigegeben: Gestaltungsentscheidung fragen; keine neue Kanzleiidentität erfinden.
