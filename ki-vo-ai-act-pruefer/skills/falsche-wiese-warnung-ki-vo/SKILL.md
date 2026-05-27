---
name: falsche-wiese-warnung-ki-vo
description: "Nutzer fragt eine KI-VO-Frage die eigentlich unter DSGVO Produkthaftung MDR oder Maschinenverordnung faellt. Warnt vor typischen Rechtsgebiets-Verwechslungen KI-VO versus DSGVO versus Produkthaftungsrichtlinie versus Medizinprodukteverordnung versus Maschinenverordnung versus Cyber Resilience Act. Pruefraster: Schluesselmerkmale zur Abgrenzung der Regelwerke. Output: Orientierungsmemo mit konkretem Verweis auf das tatsaechlich einschlaegige Recht. Abgrenzung zu verhaeltnis-zu-anderen-unionsrechtsakten (systematische Kumulationspruefung) und territorialer-anwendungsbereich-art-2."
---

# Warnung: Falsche Wiese — Verwechslung der Rechtsgebiete

## Zweck

Ein häufiger Fehler in der Praxis besteht darin, die KI-VO auf Sachverhalte anzuwenden, die tatsächlich von einem anderen Rechtsgebiet erfasst werden — oder umgekehrt: KI-spezifische Pflichten zu übersehen, weil der Nutzer glaubt, DSGVO-Konformität genüge. Dieser Skill klärt die Abgrenzung.

## Verwechslungsfall 1 — KI-VO versus DSGVO

**Häufiges Szenario:** Nutzer fragt nach Datenschutzpflichten beim Einsatz eines KI-Systems.

**Richtigstellung:**
- Die DSGVO (Verordnung (EU) 2016/679) regelt den Schutz personenbezogener Daten und gilt für jede Verarbeitung personenbezogener Daten, unabhängig davon, ob KI eingesetzt wird.
- Die KI-VO (Verordnung (EU) 2024/1689) regelt zusätzliche Anforderungen an KI-Systeme als solche: Risikoklassen, Konformitätsbewertung, Transparenzpflichten, menschliche Aufsicht.
- Beide Regelwerke können gleichzeitig gelten und ergänzen sich. DSGVO-Konformität ersetzt keine KI-VO-Konformität.
- Praktische Schnittstelle: Art. 27 KI-VO (Grundrechte-Folgenabschätzung für Betreiber) ist eng verzahnt mit Datenschutz-Folgenabschätzung nach Art. 35 DSGVO.

**Routing:** Wenn primär Datenschutzfragen bestehen → anderes Plugin (Datenschutzrecht). Wenn KI-spezifische Pflichten geprüft werden sollen → weiter in diesem Workflow.

## Verwechslungsfall 2 — KI-VO versus Produkthaftungsrichtlinie

**Häufiges Szenario:** Nutzer fragt nach Haftung für Schäden durch ein KI-System.

**Richtigstellung:**
- Die KI-VO ist keine Haftungsregelung. Sie begründet öffentlich-rechtliche Pflichten und Sanktionen, aber keine privatrechtlichen Schadensersatzansprüche.
- Die neue EU-Produkthaftungsrichtlinie (2024/2853) und die KI-Haftungsrichtlinie (Entwurf) betreffen Haftungsfragen. Diese sind vom KI-VO-Workflow zu trennen.
- Compliance mit der KI-VO kann jedoch haftungsmindernd wirken, wenn ein Verstoß zugleich eine Sorgfaltspflichtverletzung darstellt.

**Routing:** Haftungsfragen → Fachanwalt IT-Recht / Produkthaftung; KI-VO-Compliance → dieser Workflow.

## Verwechslungsfall 3 — KI-VO versus Medizinprodukteverordnung (MDR/IVDR)

**Häufiges Szenario:** KI-System in einem Medizinprodukt oder für Diagnose/Behandlung.

**Richtigstellung:**
- Die MDR (Verordnung (EU) 2017/745) und IVDR (Verordnung (EU) 2017/746) gelten für Medizinprodukte und In-vitro-Diagnostika.
- Ein KI-System, das in einem Medizinprodukt eingesetzt wird, kann gleichzeitig der MDR und der KI-VO unterliegen.
- Für KI-Systeme, die als Sicherheitsbauteil eines Medizinprodukts eingestuft werden, gilt Art. 6 Abs. 1 KI-VO i.V.m. Anhang I Nr. 1 KI-VO (MDR ist dort gelistet).
- Konformitätsbewertung nach MDR durch benannte Stelle kann teilweise auf KI-VO-Anforderungen angerechnet werden (Art. 43 Abs. 3 KI-VO).

**Routing:** Medizinprodukt-Konformität → Fachanwalt Medizinrecht; KI-VO-Schicht → weiter in diesem Workflow.

## Verwechslungsfall 4 — KI-VO versus Maschinenverordnung

**Häufiges Szenario:** KI-System in einer Maschine (Roboter, Produktionsanlage, Fahrzeug).

**Richtigstellung:**
- Die Maschinenverordnung (Verordnung (EU) 2023/1230) regelt die Sicherheit von Maschinen.
- KI-Systeme in Maschinen können gleichzeitig der KI-VO unterliegen, wenn sie Sicherheitsbauteile sind.
- Anhang I Nr. 7 KI-VO listet die Maschinenverordnung als relevanten Unionsrechtsakt; damit kann das KI-System als Hochrisiko nach Art. 6 Abs. 1 KI-VO einzustufen sein.

## Verwechslungsfall 5 — KI-VO versus Cyber Resilience Act

**Häufiges Szenario:** Nutzer fragt nach Cybersicherheitspflichten für KI-Produkte.

**Richtigstellung:**
- Der Cyber Resilience Act (Verordnung (EU) 2024/2847) regelt Cybersicherheitsanforderungen für Produkte mit digitalen Elementen.
- Für KI-Systeme, die unter den Cyber Resilience Act fallen, können beide Rechtsakte gleichzeitig gelten.
- Art. 15 KI-VO (Genauigkeit, Robustheit, Cybersicherheit für Hochrisiko-KI) greift unabhängig vom Cyber Resilience Act.

## Checkliste — Welches Recht gilt?

| Situation | Relevantes Recht |
|---|---|
| Datenschutzverletzung durch KI | DSGVO + ggf. KI-VO |
| Schaden durch KI-Fehler | Produkthaftung + ggf. KI-VO |
| KI in Medizinprodukt | MDR/IVDR + KI-VO |
| KI in Maschine/Roboter | Maschinenverordnung + KI-VO |
| KI-Produktsicherheit allgemein | Produktsicherheits-VO + KI-VO |
| KI-spezifische Risikopflichten | KI-VO primär |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 49: KI-Scoring-System als automatisierte Einzelentscheidung nach Art. 22 DSGVO — Masstab fuer Hochrisiko-Klassifikation und Betreiberpflichten nach KI-VO.
- EuGH, Urt. v. 04.10.2024 — C-203/22 (Dun & Bradstreet), NJW 2025, 56 Rn. 38: Betreiber muss Entscheidungslogik offenlegen — Art. 13 KI-VO Transparenzpflicht und Art. 26 Abs. 6 Korrekturrecht.
- BGH, Urt. v. 19.06.2018 — VI ZR 184/17, NJW 2018, 2877 Rn. 15: Organisationspflichten bei technischen Systemen — massgeblich fuer KI-VO Betreiberpflichten und interne Governance.
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 87: Drittlandtransfer bei KI-APIs erfordert Schutzgarantien; Art. 28 DSGVO AVV in KI-Lieferkette.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Kommentarliteratur
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 10: Anwendungsbereich und Pflichten.
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10: Wechselwirkung KI-VO und DSGVO.

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — FALSCHE WIESE WARNUNG KI VO
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Rn. 10]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
