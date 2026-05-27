---
name: kanzlei-allgemein-schreibcanvas
description: "Bietet ein freies Schreib-Canvas fuer Schriftsaetze Briefe Rechnungen beA-Nachrichten und Mandantenkommunikation. Anwendungsfall Anwalt will einen Entwurf strukturieren oder schwache Stellen in einem laufenden Text aufdecken lassen. Pruefraster Tatsachenvortrag Beweisangebote Antraege Normen Fristen Stilsicherheit juristischer Substanzcheck. Output Kommentierter Entwurf mit Verbesserungsvorschlaegen zu Tatsachen Beweisen Antraegen Normen naechsten Schritten. Abgrenzung zu kanzlei-allgemein-schriftsatz-turbo (Schnellerstellung) und kanzlei-allgemein-qualitaetsgate-hardening."
---

# Schreib-Canvas


## Triage zu Beginn
1. Welcher Dokumenttyp soll im Canvas erstellt werden: Klage, Replik, Mandantenbrief, Notiz, beA-Nachricht?
2. Gibt es Tatsachenluecken oder fehlende Beweisangebote im bisherigen Entwurf?
3. Sollen Rechtsgrundlagen automatisch vorgeschlagen oder manuell eingefuegt werden?
4. Ist eine Frist einzuhalten, die den Schreibprozess zeitlich begrenzt?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Schriftsatz mit lueckenhaftem Sachvortrag begruendet Anwaltshaftung; Canvas-Hinweise auf Tatsachenluecken helfen dieses Risiko zu vermeiden.
- BGH, Urt. v. 29.06.2021 - IX ZR 232/19, NJW 2021, 3112 — Fehlende Beweisangebote im Schriftsatz fuehren zu Beweisfaelligkeit; Canvas soll Beweisangebote aktiv einfordern.
- BVerfG, Beschl. v. 12.01.2016 - 2 BvR 2557/14, NJW 2016, 1155 — Anwalt muss rechtliche Argumentation vollstaendig entwickeln; Canvas-Hinweise auf Normen und Rechtsprechung unterstuetzen dies.
- BGH, Urt. v. 26.04.2018 - I ZR 82/17, NJW 2018, 2329 — Vollstaendiger Klageantrag als Prozessvoraussetzung: vage Antraege fuehren zur Unzulaessigkeit; Canvas-Antragspruefung verhindert dies.

## Zentrale Normen
- § 130 ZPO — Inhalt von Schriftsaetzen: Vollstaendigkeit von Antraegen und Tatsachen
- § 253 Abs. 2 Nr. 2 ZPO — Bestimmtheitsgrundsatz beim Klageantrag
- § 138 ZPO — Wahrheitspflicht und Erklaerungslast: Tatsachen muessen vollstaendig und wahrheitsgemass sein
- § 43 BRAO — Sorgfaltspflicht: Canvas-Pruefung als Teil anwaltlicher Dokumentenerstellung

## Kommentarliteratur
- Zöller/Greger ZPO §§ 130, 253 Rn. 1-20 (Anforderungen an Schriftsatz und Klageantrag)
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Sorgfalt bei Dokumentenerstellung)

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
