---
name: orientierung-selbstvertreter-amtsgericht
description: "Triage und Einstieg für Bürger, die sich ohne Anwalt vor dem Amtsgericht vertreten wollen. Klärt Erfahrungslevel, Rolle, Fristen, Streitwert, Zuständigkeit, Anwaltszwang und verweist auf Anfänger-Workflow, Sanity-Check, Rechtsprechungschat, Klage, Verteidigung, Termin und Rechtsmittelgrenzen."
---

# Orientierung: Sie wollen sich selbst vor dem Amtsgericht vertreten

## Worum geht es?

Vor dem Amtsgericht (AG) brauchen Sie als Buerger keinen Rechtsanwalt. Sie koennen also selbst klagen, sich selbst verteidigen, selbst Schriftsaetze einreichen und selbst im Termin auftreten. Das spart Anwaltskosten — kann aber teuer werden, wenn Sie Fristen verpassen oder Antraege falsch formulieren. Diese Skill ordnet Ihre Situation ein und sagt Ihnen, wohin Sie als Naechstes lesen sollten.

## Wann brauchen Sie diese Skill?

- Sie wissen noch nicht, ob Sie klagen oder sich verteidigen.
- Sie wollen verstehen, was vor dem Amtsgericht ueberhaupt passiert.
- Sie wollen wissen, ob ein Anwalt zwingend ist.
- Sie suchen eine Reihenfolge, in der Sie die Skills lesen.
- Sie wollen einen Anfänger-Modus oder einen Sanity-Check vor dem Absenden.

## Fachbegriffe (kurz erklaert)

- **Amtsgericht (AG)**: Das kleinste Gericht der ordentlichen Gerichtsbarkeit. Es entscheidet ueber zivile Streitigkeiten bis zu einer bestimmten Wertgrenze und ueber bestimmte Materien (Miete, Familie, kleine Geldforderungen).
- **Streitwert**: Der Geldwert dessen, worum Sie streiten. Bei einer Forderung von 2.000 EUR ist der Streitwert 2.000 EUR.
- **Klaeger**: Wer eine Klage erhebt.
- **Beklagter**: Wer verklagt wird.
- **Anwaltszwang**: Vorschrift, dass Sie sich nur durch einen Anwalt vertreten lassen koennen. Vor dem AG gibt es ihn **nicht** (mit wenigen Ausnahmen, siehe Skill `anwaltszwang-pruefen-78-zpo`).

## Rechtsgrundlagen

- **§ 78 ZPO** — Anwaltszwang vor Landgericht und hoeher; e contrario kein Anwaltszwang vor AG.
- **§ 23 GVG** — Sachliche Zustaendigkeit des AG.
- **§ 23a, 23b, 23c GVG** — Familiensachen, Betreuungssachen, Nachlasssachen.
- **§§ 12 ff. ZPO** — Oertliche Zustaendigkeit.
- **§ 495a ZPO** — Vereinfachtes Verfahren bis 1.000 EUR Streitwert (Stand 2026, vorher 600 EUR).

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Klaeren Sie Ihre Rolle

Sind Sie

- **Klaeger** (Sie wollen jemand verklagen)? → Block B-E, dann F-L bei Fortschritt.
- **Beklagter** (Sie wurden verklagt)? → Block F, dann G, H, I, J, K.

Wenn Sie Anfänger sind, starten Sie zuerst mit `anfaenger-workflow-amtsgericht`. Dieser Skill erklärt die Reihenfolge in kleineren Schritten.

### Schritt 2 — Streitwert bestimmen

Schaetzen Sie, um welche Geldsumme es geht. Das ist Ihr Streitwert. Bei Sachen ohne Geldforderung (z. B. "Sie sollen die Garage raeumen") schaetzt das Gericht. Skill `klage-streitwert-angabe-3-zpo` hilft.

### Schritt 3 — Zustaendigkeit pruefen

- Streitwert unterhalb der Wertgrenze § 23 Nr. 1 GVG? AG zustaendig. Skill `sachliche-zustaendigkeit-amtsgericht-23-gvg`.
- Mietsache, Reisevertrag, Familiensache? Immer AG, unabhaengig vom Wert. Skill `ausnahmen-streitwertgrenze-23-nr-2-gvg`.
- Welches AG raeumlich? Wohnort Beklagter ist der Hauptfall. Skill `oertliche-zustaendigkeit-12-37-zpo`.

### Schritt 4 — Erfolgsaussichten ehrlich pruefen

Klagen kostet Geld, auch wenn Sie keinen Anwalt brauchen — Gerichtskosten, evtl. Sachverstaendiger, im Verlust-Fall die Kosten der Gegenseite. Skill `vorabklaerung-erfolgsaussichten-selbstcheck`.

### Schritt 5 — Verjaehrung pruefen (Klaeger!)

Forderungen verjaehren in der Regel in **drei Jahren** zum Jahresende. Ist Ihr Anspruch noch durchsetzbar? Skill `verjaehrungsfrist-pruefen-195-bgb`.

### Schritt 6 — Naechsten Skill auswaehlen

- Sie sind Anfänger? → `anfaenger-workflow-amtsgericht`.
- Sie wollen vor Versand prüfen? → `sanity-check-selbstvertretung-amtsgericht`.
- Sie sind unsicher wegen Wertgrenze, Berufung oder Anwaltszwang? → `zulassungsgrenzen-check-amtsgericht`.
- Sie brauchen Rechtsprechung zu einem Argument? → `rechtsprechungschat-amtsgericht`.
- Sie wollen Klage erstellen? → `klageschrift-pflichtbestandteile-253-zpo`.
- Sie haben eine Klage bekommen? → `klageerwiderung-fristen-274-zpo`.
- Sie haben einen Termin? → `terminvorbereitung-checkliste`.
- Sie haben ein Urteil und wollen sich wehren? → `berufung-amtsgericht-511-zpo`.

## Worauf Sie besonders achten muessen

- **Fristen ueberleben Versaeumnisse selten.** Wenn das Gericht eine Frist setzt, ist sie ernst. Eine versaeumte Frist kostet Sie meist den Prozess. Skill `fristen-berechnen-187-188-bgb`.
- **Versand durch Dritte ist Ihr Risiko.** Wenn Sie eine Klage durch einen Boten oder Verwandten zum Gericht schicken und die Sendung verspaetet ankommt, traegt das Risiko nach BVerfG-Linie **Sie**. Skill `zurechnungsproblem-versand-durch-dritte`.
- **Bestimmter Antrag.** Eine Klage ohne klaren Antrag ist unzulaessig. Skill `klageschrift-antrag-bestimmt-formulieren`.
- **Mein Justizpostfach (MJP) seit 2024** ermoeglicht Buergern den elektronischen Versand an Gerichte. Skill `einreichung-mein-justizpostfach-mjp-2024`.

## Typische Fehler

- "Ich schreibe nur, dass ich gewinnen will." → Sie brauchen einen **konkreten** Antrag (z. B. "Der Beklagte wird verurteilt, an mich 1.500 EUR nebst Zinsen zu zahlen.").
- "Beweise reiche ich spaeter ein." → Beweismittel muessen Sie **benennen** (mindestens). Skill `klageschrift-beweisangebote-einbauen-373-zpo`.
- "Ich warte ab, was die Gegenseite schreibt." → Beim Beklagten oft toedlich: Wer in der Frist nicht reagiert, kassiert ein Versaeumnisurteil. Skill `saeumnis-vermeiden-330-ff-zpo`.
- "Ich verklage erstmal, einigen kann ich mich spaeter." → Vorgerichtliche Mahnung und Verzug sind Voraussetzung fuer manche Anspruchspositionen (z. B. Verzugszinsen). Skill `aussergerichtliche-mahnung-286-bgb`.

## Querverweise

- `anwaltszwang-pruefen-78-zpo` — Anwaltszwang-Check.
- `anfaenger-workflow-amtsgericht` — besonders geführter Einstieg.
- `sanity-check-selbstvertretung-amtsgericht` — letzte Ampel vor Versand, Termin oder Rechtsmittel.
- `zulassungsgrenzen-check-amtsgericht` — Streitwert, AG/LG, § 495a ZPO, Berufung, Anwaltszwang.
- `rechtsprechungschat-amtsgericht` — Rechtsprechung finden, prüfen und sauber verwenden.
- `sachliche-zustaendigkeit-amtsgericht-23-gvg` — AG ueberhaupt zustaendig?
- `oertliche-zustaendigkeit-12-37-zpo` — Welches AG raeumlich?
- `vorabklaerung-erfolgsaussichten-selbstcheck` — Lohnt sich der Prozess?
- `kostenrisiko-streitwert-berechnen-gkg` — Was kostet das?
- `wann-doch-anwalt-grenzfaelle` — Wann ist Selbstvertretung kein gutes Ergebnis?

## Quellen und Aktualitaet

Stand: 05/2026. § 23 Nr. 1 GVG: Wertgrenze 10.000 EUR seit 01.01.2026 (Anhebung von 5.000 EUR durch das Justizstandort-Staerkungsgesetz). § 495a ZPO: Wertgrenze 1.000 EUR (Anhebung von 600 EUR). § 511 II Nr. 1 ZPO: Berufungs-Beschwer 1.000 EUR (Anhebung von 600 EUR). MJP (Mein Justizpostfach) ist seit 2024 im Buerger-Betrieb.
