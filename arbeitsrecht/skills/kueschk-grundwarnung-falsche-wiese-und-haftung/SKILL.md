---
name: kueschk-grundwarnung-falsche-wiese-und-haftung
description: "Pflichtkopf fuer jeden Kuendigungsschutzklage-Schriftsatz: Hinweis auf falsche Wiese und Haftungsausschluss; zentraler Warnblock mit Drei-Wochen-Frist nach § 4 KSchG; wird in jeden Laien-Output eingefuegt."
---

# Grundwarnung: Falsche Wiese und Haftung

## Zweck

Dieser Skill liefert den Pflicht-Warnkopf, der jedem Schriftsatz und jeder inhaltlichen Ausgabe vorangestellt wird, die im Rahmen des KüSchK-Laien-Workflows erzeugt wird. Er ist kein eigenständiger Workflow, sondern ein einzufügender Baustein.

## Pflicht-Disclaimer-Kopf (in jeden Laien-Output einfügen)

---

**HAFTUNGSAUSSCHLUSS UND WARNUNG**

Dieses Dokument wurde mit Hilfe eines KI-gestützten Systems erstellt. Es handelt sich um einen **Entwurf zur eigenständigen Verwendung auf eigenes Risiko**. Das System übernimmt keine rechtliche Verantwortung.

**Du könntest auf der falschen Wiese unterwegs sein.**

Das bedeutet: Möglicherweise ist das Kündigungsschutzgesetz (KSchG) auf deinen Fall gar nicht anwendbar — weil dein Betrieb zu klein ist (§ 23 KSchG: weniger als zehn Arbeitnehmer) oder weil du noch keine sechs Monate beschäftigt bist (§ 1 Abs. 1 KSchG). In diesem Fall wäre eine Kündigungsschutzklage nach § 4 KSchG nicht das richtige Rechtsmittel. Das System kann das nicht selbst feststellen.

**Drei-Wochen-Frist — absolute Ausschlussfrist:**

> § 4 KSchG: Will ein Arbeitnehmer geltend machen, dass eine Kündigung sozial ungerechtfertigt oder aus anderen Gründen rechtsunwirksam ist, so muss er innerhalb von **drei Wochen nach Zugang der schriftlichen Kündigung** Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis durch die Kündigung nicht aufgelöst ist.

Die Frist beginnt mit dem Tag des **Zugangs** der Kündigung (nicht dem Datum auf dem Schreiben). Sie kann grundsätzlich nicht verlängert werden. Ein Versäumnis führt nach § 7 KSchG dazu, dass die Kündigung als wirksam gilt — auch wenn sie rechtswidrig war.

**Ausnahme:** Nachträgliche Klagezulassung nach § 5 KSchG bei unverschuldeter Versäumung (z.B. schwere Erkrankung, Abwesenheit ohne Verschulden). Die Frist für den Zulassungsantrag beträgt zwei Wochen nach Wegfall des Hindernisses.

---

## Triage zu Beginn — kläre vor Einbettung des Warnbausteins

1. Handelt es sich um einen Laien-Output (nicht anwaltlicher Nutzer)?
2. Wurde der KSchG-Anwendbarkeitscheck bereits durchgeführt (`kueschk-anwendbarkeit-kschg-pruefen`)?
3. Ist die Drei-Wochen-Frist bereits einkalkuliert (Zugangsdatum bekannt)?

Nur wenn Frage 1 = ja: Warnbaustein zwingend einbetten. Bei Anwält:innen entfällt der Pflicht-Disclaimer-Kopf.

## Zentrale Normen

- **§ 4 KSchG** — Klagefrist drei Wochen ab Zugang der schriftlichen Kündigung
- **§ 5 KSchG** — Nachträgliche Zulassung der Klage bei unverschuldeter Fristversäumung (Antragsfrist: zwei Wochen nach Wegfall des Hindernisses)
- **§ 7 KSchG** — Fiktion der Wirksamkeit bei Fristversäumung
- **§ 23 KSchG** — Betrieblicher Geltungsbereich KSchG (Schwellenwert > 10 Arbeitnehmer)
- **§ 1 Abs. 1 KSchG** — Wartezeit sechs Monate
- **§ 11 Abs. 1 ArbGG** — Kein Anwaltszwang erste Instanz

## Aktuelle Rechtsprechung

- BAG, Urt. v. 26.06.2008 – 2 AZR 264/07, NZA 2008, 1182 — Die Drei-Wochen-Frist des § 4 KSchG ist eine materiell-rechtliche Ausschlussfrist; ihre Versäumung lässt sich nur über § 5 KSchG heilen, nicht durch allgemeine Wiedereinsetzungsregeln.
- BAG, Urt. v. 22.03.2012 – 2 AZR 224/11, NZA 2012, 1101 — Eine Kündigung gilt nach § 7 KSchG als von Anfang an wirksam, wenn der Arbeitnehmer die Klagefrist versäumt; nachträgliche Kenntnis vom Unwirksamkeitsgrund ändert daran nichts.
- BAG, Urt. v. 23.02.2012 – 2 AZR 773/10, NZA 2012, 858 — Der Zugang einer schriftlichen Kündigung richtet sich nach §§ 130 ff. BGB; maßgeblich ist der Zeitpunkt, in dem die Willenserklärung in den Machtbereich des Empfängers gelangt und mit Kenntnisnahme zu rechnen ist.
- BAG, Urt. v. 28.06.2012 – 6 AZR 682/10, NZA 2012, 1090 — § 5 KSchG setzt unverschuldete Verhinderung voraus; grobe Fahrlässigkeit des Arbeitnehmers schließt die nachträgliche Zulassung aus.

## Kommentarliteratur

- ErfK/Kiel, 24. Aufl. 2024, § 4 KSchG Rn. 1-15 — (Klagefrist und Zugang)
- KR/Friedrich, 13. Aufl. 2022, § 4 KSchG Rn. 20 ff. — (Fristbeginn, Ausschlussfrist)
- APS/Dörner/Linck, 6. Aufl. 2022, § 4 KSchG Rn. 5 ff. — (Fiktion § 7 KSchG)

## Wo dieser Baustein erscheint

- Vor jedem Klageschrift-Entwurf (Skill `kueschk-klageschrift-laie-baustein`)
- Vor jedem Schriftsatz-Entwurf für Laien
- In der Ausgabe von `kueschk-output-warnschriftsatz-laie`

## Mechanik des Warnbausteins

Der Warnblock ist kein optionaler Hinweis, sondern Pflichtbestandteil. Er darf weder weggelassen noch verkürzt werden. Anwältinnen und Anwälte erhalten diesen Kopf nicht — für sie gilt der Hinweis in `kueschk-triage-laie-oder-anwalt`.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
