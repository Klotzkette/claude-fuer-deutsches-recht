---
name: kanzlei-allgemein-mandatsvereinbarung
description: "Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis Honorarvereinbarung und Vorschuss. Anwendungsfall neues Mandat soll foermlich begründet werden mit allen Pflichtdokumenten nach BRAO. Normen § 3a RVG Honorarvereinbarung § 49b BRAO Verbot Erfolgshonorar Art. 13 DSGVO § 43a BRAO Verschwiegenheit. Prüfraster Mandatsumfang RVG vs. Stundensatz Haftungsbegrenzung Vorschuss Rechtsschutzversicherer KI-Hinweis berufsrechtliche Punkte. Output Mandatsvereinbarungsentwurf Vollmacht Datenschutzhinweis Honorarblatt mit Markierung offener Prüfpunkte. Abgrenzung zu kanzlei-allgemein-mandatsannahme-gwg und kanzlei-allgemein-akte."
---

# Mandatsvereinbarung und Honorarstart

## Zweck

Dieser Skill bereitet Mandatsvereinbarung, Vollmacht, Datenschutzhinweis und Honorarunterlagen vor.

## Bausteine

- Mandatsumfang und ausgeschlossene Tätigkeiten.
- Vollmacht.
- Datenschutzhinweis.
- Honorargrundlage: RVG, Stundenhonorar, Pauschale, Beratungshonorar.
- Vorschuss.
- Haftungsbegrenzung, sofern zulässig und gewünscht.
- Rechtsschutzversicherung und Deckungsanfrage.
- KI-Einsatz-Hinweis und Verweis auf Datenschutzhinweise.
- GwG-Mitwirkung, Identifizierung und Dokumentationspflichten, soweit einschlägig.
- Kündigung und Mandatsbeendigung.

## Haftungsbegrenzung

Immer als prüfpflichtig markieren:

- individuelle Vereinbarung oder AGB-Klausel,
- gesetzliche Mindestanforderungen,
- Versicherungssumme,
- Transparenz,
- keine versteckte Beschränkung.

## Ablauf

1. Mandatsart und Mandatsumfang klären.
2. Honorarweg auswählen.
3. Pflichtinformationen abfragen.
4. Mandatsannahme- und GwG-Status aus `kanzlei-allgemein-mandatsannahme-gwg` übernehmen.
5. Entwurf erzeugen.
6. Prüfpunkte markieren.
7. Freigabe durch Berufsträger verlangen.

## KI- und Datenschutzhinweise

Der Entwurf soll einen knappen, transparenten Hinweis enthalten, dass die Kanzlei technische Hilfsmittel einschließlich KI-gestützter Systeme zur Strukturierung, Recherche, Entwurfsunterstützung, Qualitätskontrolle, Fristen- und Aktenorganisation einsetzen kann. Nicht behaupten, dass bestimmte Anbieter, Schutzmaßnahmen oder Drittlandtransfers geprüft sind, wenn das nicht aktenkundig ist. Auf die Datenschutzhinweise der Kanzlei verweisen.

## GwG-Hinweise

Wenn das Mandat GwG-relevant ist, in Mandatsvereinbarung oder Begleitschreiben aufnehmen:

- Mitwirkung bei Identifizierung.
- Angaben zu auftretenden Personen und wirtschaftlich Berechtigten.
- Nachweise zu Register, Vertretung und Mittelherkunft, soweit erforderlich.
- Dokumentation und Aufbewahrung nach gesetzlichen Pflichten.

## Ausgabe

- Mandatsvereinbarung als Markdown-Entwurf.
- Vollmachtstext.
- Datenschutzhinweis.
- KI- und Datenschutzbaustein aus `assets/templates/mandatsvereinbarung-ki-datenschutz-hinweis.md`.
- Honorarblatt.
- Liste offener Entscheidungen.
