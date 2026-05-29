---
name: kanzlei-allgemein-schreibcanvas
description: "Bietet ein freies Schreib-Canvas für Schriftsaetze Briefe Rechnungen beA-Nachrichten und Mandantenkommunikation. Anwendungsfall Anwalt will einen Entwurf strukturieren oder schwache Stellen in einem laufenden Text aufdecken lassen. Prüfraster Tatsachenvortrag Beweisangebote Anträge Normen Fristen Stilsicherheit juristischer Substanzcheck. Output Kommentierter Entwurf mit Verbesserungsvorschlaegen zu Tatsachen Beweisen Anträgen Normen naechsten Schritten. Abgrenzung zu kanzlei-allgemein-schriftsatz-turbo (Schnellerstellung) und kanzlei-allgemein-qualitaetsgate-hardening."
---

# Schreib-Canvas


## Triage zu Beginn
1. Welcher Dokumenttyp soll im Canvas erstellt werden: Klage, Replik, Mandantenbrief, Notiz, beA-Nachricht?
2. Gibt es Tatsachenluecken oder fehlende Beweisangebote im bisherigen Entwurf?
3. Sollen Rechtsgrundlagen automatisch vorgeschlagen oder manuell eingefuegt werden?
4. Ist eine Frist einzuhalten, die den Schreibprozess zeitlich begrenzt?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 130 ZPO — Inhalt von Schriftsaetzen: Vollstaendigkeit von Antraegen und Tatsachen
- § 253 Abs. 2 Nr. 2 ZPO — Bestimmtheitsgrundsatz beim Klageantrag
- § 138 ZPO — Wahrheitspflicht und Erklaerungslast: Tatsachen muessen vollstaendig und wahrheitsgemass sein
- § 43 BRAO — Sorgfaltspflicht: Canvas-Pruefung als Teil anwaltlicher Dokumentenerstellung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill stellt ein Arbeitsbrett für Entwürfe bereit: links der Rohtext, rechts Hinweise, darunter offene Tatsachen, Beweise, Fristen, Anlagen, Versand- und Abrechnungspunkte. Das Canvas soll beim Schreiben helfen, ohne ständig zu stören.

## Canvas-Bereiche

- Rohtext.
- Verbesserter Vorschlag.
- Tatsachenlücken.
- Beweisangebote.
- Rechtsgrundlagen.
- Anträge und Tenor.
- Anlagen.
- Fristen.
- Versandweg.
- Zeitnarrativ.
- Rechnungs- oder Kostenfolge.

## Interventionen

Nur intervenieren, wenn:

- ein Text juristisch unsubstantiiert wirkt,
- ein Antrag fehlt,
- ein Beweisangebot fehlt,
- eine Frist oder ein EB berührt ist,
- beA-Versand naheliegt,
- eine Rechnung oder E-Rechnung naheliegt,
- die Sprache unprofessionell, zu scharf oder zu unklar ist,
- Anlagen erwähnt, aber nicht beigefügt sind.

## Hilfston

Formulierungen:

- `Ich glaube, hier fehlt noch der konkrete Tatsachenkern. Wollen wir Datum, Beteiligte und Beweisangebot ergänzen?`
- `Der Satz ist verständlich, aber für das Gericht noch zu abstrakt. Ich würde ihn so nachschärfen: ...`
- `Das ist schon verwendbar. Für den beA-Versand sollten wir noch Anlagen und Signatur prüfen.`
- `Aus diesem Arbeitsschritt kann ich ein Zeitnarrativ vorbereiten.`

## Arbeitsweise

1. Entwurf aufnehmen.
2. Textsorte erkennen.
3. Ziel und Adressat klären.
4. Substanzcheck durchführen.
5. Verbesserungsvorschlag danebenstellen.
6. Offene Punkte als kleine Aufgaben erfassen.
7. Nach Freigabe an Output, Fristen, Zeit oder Rechnung übergeben.
8. Bei Klage, Replik, Antrag oder gerichtlichem Schriftsatz an `kanzlei-allgemein-schriftsatz-turbo` übergeben.
9. Bei Vertrag, Termsheet oder Klauselwunsch an `kanzlei-allgemein-vertragsentwurf` übergeben.
10. Vor Ausgabe `kanzlei-allgemein-qualitaetsgate-hardening` nutzen.

## Ausgabe

`assets/templates/schreibcanvas.md` verwenden.
