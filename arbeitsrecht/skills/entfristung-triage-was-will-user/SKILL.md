---
name: entfristung-triage-was-will-user
description: "Einstieg Entfristungsklage-Workflow: Erkennung ob Nutzer Befristungskontrollklage oder Entfristungsklage anstrebt; Abgrenzung zu Kuendigungsschutzklage; Ueberblick Pruefprogramm TzBfG; Weiterleitung zu passenden Folge-Skills."
---

# Entfristungsklage: Was will der Nutzer?

## Zentrale Normen (Überblick)

- § 17 TzBfG — 3-Wochen-Klagefrist (kritischste Frist; läuft auch bei Weiterbeschäftigung)
- § 14 Abs. 4 TzBfG — Schriftformerfordernis (häufig übersehener Unwirksamkeitsgrund)
- § 14 Abs. 2 Satz 2 TzBfG — Vorbeschäftigungsverbot
- § 16 TzBfG — Rechtsfolge: Vertrag gilt als unbefristet
- § 4 KSchG — Klagefrist Kündigungsschutz (zur Abgrenzung)
- § 623 BGB — Schriftformerfordernis Kündigung (zur Abgrenzung)

## Aktuelle Rechtsprechung (Kurzüberblick für Triage)

- BAG, Urt. v. 16.04.2008 – 7 AZR 1048/06, NZA 2008, 999 — Häufigster Unwirksamkeitsgrund: elektronische Unterzeichnung des Arbeitsvertrags (DocuSign, E-Mail-Signatur) verletzt § 14 Abs. 4 TzBfG — Befristung automatisch unwirksam, Rechtsfolge § 16 TzBfG.
- BAG, Urt. v. 23.01.2019 – 7 AZR 733/16, NZA 2019, 1042 — Vorbeschäftigungsverbot gilt zeitlich unbegrenzt; auch mehrere Jahre zurückliegende frühere Tätigkeiten beim selben Arbeitgeber sperren die sachgrundlose Befristung.

## Zweck

Dieser Skill ist der Einstieg in den Entfristungs-Workflow. Er klärt, ob das Ziel des Nutzers ist, festzustellen, dass ein angeblich befristeter Vertrag in Wirklichkeit **unbefristet** ist (Befristungskontrollklage / Entfristungsklage).

## Abgrenzung: Entfristungsklage vs. Kündigungsschutzklage

| | Entfristungsklage | Kündigungsschutzklage |
|---|---|---|
| Ausgangssituation | Befristeter Vertrag läuft aus | Kündigung durch Arbeitgeber |
| Ziel | Feststellung: Vertrag ist unbefristet | Feststellung: Kündigung ist unwirksam |
| Rechtsgrundlage | §§ 17, 16 TzBfG | § 4 KSchG |
| Frist | 3 Wochen ab vereinbartem Ende | 3 Wochen ab Zugang der Kündigung |
| Norm Schriftform | § 14 Abs. 4 TzBfG | § 623 BGB |

## Typische Einstiegssituation

Der Nutzer sagt zum Beispiel:
- „Mein befristeter Vertrag läuft am [DATUM] aus, ich glaube er war gar nicht wirksam befristet"
- „Mein Arbeitsvertrag wurde per E-Mail unterschrieben, gilt die Befristung überhaupt?"
- „Ich arbeite schon seit drei Jahren auf Basis aufeinanderfolgender befristeter Verträge"
- „Mein Arbeitgeber hat mir einen neuen Vertrag gegeben ohne dass ich unterschrieben habe"

## Erkennungsmerkmale Entfristungsklage

Das System erkennt den Entfristungs-Bedarf wenn:
- Ein schriftlicher (oder angeblich elektronischer) Vertrag mit Endtermin vorliegt
- Der Arbeitnehmer behauptet, die Befristung sei unwirksam
- Das Ende des Vertrags noch nicht eingetreten ist oder erst kürzlich eingetreten ist

## Kritische Sofortfrage: Dreiwochenfrist § 17 TzBfG

**Sofort prüfen:**

> § 17 TzBfG: Will der Arbeitnehmer geltend machen, dass die Befristung eines Arbeitsvertrags rechtsunwirksam ist, so muss er innerhalb von **drei Wochen nach dem vereinbarten Ende des befristeten Arbeitsvertrags** Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis auf Grund der Befristung nicht beendet ist.

**Wann läuft die Frist?** Ab dem **vereinbarten** (nicht tatsächlichen) Vertragsende. Sie läuft auch wenn der Arbeitnehmer tatsächlich weiterbeschäftigt wird.

## Folge-Skills

| Schritt | Skill |
|---|---|
| Laie oder Anwalt? | `entfristung-laie-oder-anwalt-frage` |
| Dreiwochenfrist § 17 TzBfG | `entfristung-grundwarnung-drei-wochen-frist` |
| Sachgrund prüfen | `entfristung-sachgrund-pruefen-14-abs-1` |
| Schriftform prüfen | `entfristung-schriftform-14-abs-4-erkennen` |
| Elektronische Signatur | `entfristung-elektronische-signatur-vorsicht` |
| Rechtsfolge | `entfristung-rechtsfolge-16-tzbfg-unbefristet` |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
