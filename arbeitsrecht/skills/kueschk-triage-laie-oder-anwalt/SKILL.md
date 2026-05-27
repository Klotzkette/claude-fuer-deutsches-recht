---
name: kueschk-triage-laie-oder-anwalt
description: "KERNEINSTIEG Kuendigungsschutzklage: fragt zuerst ob Anwalt oder Verbraucher-Laie; bei Laie staendige Warnungen und dringende Empfehlung anwaltlicher Beratung; kein Mandatsverhaeltnis; leitet zu passenden Folge-Skills; zentraler Startpunkt fuer das gesamte KueschK-Workflow-Buendel."
---

# KüSchK-Triage: Laie oder Anwalt?

## Zweck

Dieser Skill ist der **Kerneinstieg** für das Kündigungsschutzklage-Bündel. Er klärt zunächst, wer den Workflow nutzt, und leitet dann zielgerichtet weiter. Ohne diese Triage-Frage können nachgelagerte Skills keine angemessene Risikoeinschätzung liefern.

## Eröffnungsfrage (PFLICHT, immer zuerst)

Das System stellt **als erste und wichtigste Frage**:

> „Bist du Rechtsanwältin / Rechtsanwalt oder nutzt du dieses System als Verbraucher / Laie ohne anwaltliche Zulassung?"

Es werden nur zwei Antworten akzeptiert:
- **Anwalt/Anwältin** → Weiterleitung zu anwaltlichen Bausteinen
- **Verbraucher/Laie** → Weiterleitung zu Laien-Bausteinen **mit umfassender Warnung**

## Pfad A: Anwalt / Anwältin

Für Anwältinnen und Anwälte gilt:
- Kein dauernder Warnkopf erforderlich (Berufsrecht und Haftungsbewusstsein vorausgesetzt)
- Anwaltliche Klageschrifts-Bausteine verfügbar (Skill `kueschk-klageschrift-anwalt-baustein`)
- Hinweis auf Dokumentationspflichten nach § 43a BRAO
- Fristencheck § 4 KSchG trotzdem sofort

## Pfad B: Verbraucher / Laie

Bei Angabe „Verbraucher" oder „Laie" erscheint folgender **Pflicht-Warnblock**, der in jedem Folge-Output wiederholt wird:

---

**WICHTIGE WARNUNG – BITTE GENAU LESEN**

Du bist dabei, rechtliche Schritte einzuleiten, ohne Anwalt zu sein. Das ist gesetzlich erlaubt (§ 11 Abs. 1 ArbGG: kein Anwaltszwang in erster Instanz vor dem Arbeitsgericht), birgt aber erhebliche Risiken:

1. **Drei-Wochen-Frist § 4 KSchG**: Verpasst du diese Frist, gilt die Kündigung als wirksam — ohne Ausnahme.
2. **Falsche Anspruchsgrundlage**: Wenn dein Betrieb weniger als zehn Arbeitnehmer hat oder du noch keine sechs Monate beschäftigt bist, gilt das KSchG möglicherweise gar nicht.
3. **Kein Mandatsverhältnis**: Dieses System ist kein Anwalt, übernimmt keine rechtliche Verantwortung und haftet nicht.
4. **Mechanische Prüfung**: Das System prüft nur das, was du eingibst. Falsche oder unvollständige Angaben führen zu falschen Ergebnissen.

**Dringende Empfehlung**: Suche sofort einen Rechtsanwalt oder eine Rechtsanwältin für Arbeitsrecht auf, idealerweise über den Anwaltssuchdienst der Rechtsanwaltskammern oder über Gewerkschaftsberatung (wenn gewerkschaftlich organisiert). Viele Anwältinnen bieten eine Erstberatung zu Festpreisen an.

---

## Folge-Skills nach Triage

| Nächster Schritt | Skill |
|---|---|
| Grundwarnung und Haftungsausschluss | `kueschk-grundwarnung-falsche-wiese-und-haftung` |
| KSchG-Anwendbarkeit prüfen | `kueschk-anwendbarkeit-kschg-pruefen` |
| Frist und Zugang prüfen | `kueschk-frist-und-zugang-pruefen` |
| Sonderkündigungsschutz prüfen | `kueschk-sonderkuendigungsschutz-checkliste` |
| Formfehler prüfen | `kueschk-formfehler-pruefen` |
| Klageschrift Laie | `kueschk-klageschrift-laie-baustein` |
| Klageschrift Anwalt | `kueschk-klageschrift-anwalt-baustein` |

## Zentrale Normen

- **§ 11 Abs. 1 ArbGG** — Kein Anwaltszwang vor dem Arbeitsgericht erste Instanz
- **§ 11 Abs. 4 ArbGG** — Anwaltszwang ab Berufung vor dem LAG
- **§ 4 KSchG** — Drei-Wochen-Klagefrist (absolute Ausschlussfrist)
- **§ 23 KSchG** — Geltungsbereich KSchG (über 10 Arbeitnehmer)
- **§ 1 Abs. 1 KSchG** — Wartezeit sechs Monate
- **§ 43a BRAO** — Dokumentationspflichten für Anwälte (Beratung über Risiken)
- **§ 626 BGB** — Fristlose Kündigung aus wichtigem Grund (besondere Triage: andere Fristen)

## Aktuelle Rechtsprechung

- BAG, Urt. v. 22.03.2012 – 2 AZR 224/11, NZA 2012, 1101 — Verpasst der Laie die Drei-Wochen-Frist, gilt die Kündigung nach § 7 KSchG als wirksam; auch wenn die Kündigung tatsächlich rechtswidrig war, ist sie heilbar unwirksam, aber öffentlich-rechtlich als wirksam zu behandeln.
- BAG, Urt. v. 26.06.2008 – 2 AZR 264/07, NZA 2008, 1182 — Die Fristwahrung des § 4 KSchG erfordert den Eingang der Klageschrift beim Arbeitsgericht, nicht nur deren Absendung; Postlaufzeiten gehen zu Lasten des Klägers.
- BAG, Urt. v. 19.04.2012 – 2 AZR 469/11, NZA 2013, 154 — Das Gericht hat gem. § 139 ZPO i.V.m. § 46 Abs. 2 ArbGG auf einen auch ohne Anwalt vollständigen Sachvortrag hinzuwirken; dies kann aber das fehlende Rechtswissen des Laien nicht vollständig ausgleichen.
- BAG, Urt. v. 26.09.2013 – 2 AZR 682/12, NZA 2014, 289 — Auch im Laienverfahren trifft den Arbeitnehmer die Obliegenheit, die Klagefrist selbst zu überwachen; ein Anwaltsfehler kann nur dann zu Wiedereinsetzung führen, wenn ein Mandatsverhältnis bestand.

## Kommentarliteratur

- ErfK/Koch, 24. Aufl. 2024, § 11 ArbGG Rn. 1-10 — (Parteifähigkeit, Vertretung, kein Anwaltszwang)
- GMP/Germelmann, 9. Aufl. 2017, § 11 ArbGG Rn. 5 ff. — (Parteifähigkeit Laie, Überblick)
- Schaub/Linck, ArbeitsR-HdB, 20. Aufl. 2023, § 176 Rn. 1 ff. — (Kündigungsschutzklage, Triage-Fragen in der Mandatsannahme)

## Keine Vorwegnahme des Ergebnisses

Der Skill liefert noch keine inhaltliche Prüfung der Kündigung. Er stellt ausschließlich die Weichenfrage, welche den gesamten nachfolgenden Workflow prägt.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
