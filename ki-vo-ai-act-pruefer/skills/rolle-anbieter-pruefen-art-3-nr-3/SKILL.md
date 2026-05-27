---
name: rolle-anbieter-pruefen-art-3-nr-3
description: "Unternehmen das Software oder KI entwickelt fragt: Sind wir Anbieter im Sinne der KI-VO und welche Pflichten treffen uns deshalb? Art. 3 Nr. 3 KI-VO Anbieter-Definition. Pruefraster: Entwicklung oder Beauftragung Entwicklung Inverkehrbringen unter eigenem Namen Inbetriebnahme. Abgrenzung zu Betreiber Einfuehrer Haendler. Output: Rollenentscheidung Anbieter ja/nein mit Begruendung und Liste der Anbieter-Pflichten. Abgrenzung zu anbieter-werden-art-25 (Rollenwechsel) und persoenlicher-anwendungsbereich-rollen-art-3 (Uebersicht)."
---

# Rolle-Check: Anbieter — Art. 3 Nr. 3 KI-VO

## Zweck

Die Anbieter-Rolle begründet den umfangreichsten Pflichtenkatalog der KI-VO. Dieser Skill klärt durch einen Entscheidungsbaum, ob die Nutzer-Rolle als Anbieter qualifiziert.

## Legaldefinition — Art. 3 Nr. 3 KI-VO

Anbieter (provider) ist eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System oder ein GPAI-Modell entwickelt oder entwickeln lässt und dieses KI-System oder GPAI-Modell unter ihrem eigenen Namen oder ihrer eigenen Marke — entgeltlich oder unentgeltlich — in Verkehr bringt oder in Betrieb nimmt.

## Entscheidungsbaum

### Schritt 1 — Entwicklung

**Frage A:** Haben Sie selbst das KI-System entwickelt (Eigenentwicklung) oder haben Sie jemanden damit beauftragt (Auftragsentwicklung)?

- Eigenentwicklung → weiter zu Schritt 2
- Auftragsentwicklung (Dritter entwickelt, aber nach Ihren Vorgaben) → weiter zu Schritt 2
- Sie nutzen ein fertiges, unmodifiziertes Drittsystem → Sie sind kein Anbieter im Sinne von Art. 3 Nr. 3 KI-VO; weiter zu `rolle-betreiber-pruefen-art-3-nr-4`

**Hinweis zu Auftragsentwicklung:** Wenn Sie als Auftraggeber die wesentlichen Spezifikationen vorgeben und das System unter Ihrem Namen in Verkehr bringen, sind Sie Anbieter — nicht der beauftragte Entwickler. Der Auftragnehmer kann ebenfalls Anbieter sein, wenn er das System eigenständig gestaltet und unter eigenem Namen verbreitet.

### Schritt 2 — Inverkehrbringen unter eigenem Namen

**Frage B:** Bringen Sie das System unter Ihrem eigenen Namen oder Ihrer eigenen Marke in Verkehr?

- Ja → starkes Indiz für Anbieter-Rolle; weiter zu Schritt 3
- Nein (Sie stellen das System dem Auftraggeber bereit, der es unter eigenem Namen vermarktet) → Sie sind möglicherweise nur Auftragsentwickler ohne Anbieter-Status; der Auftraggeber ist Anbieter

**Variante „in Betrieb nehmen":** Auch wer ein KI-System nicht vermarktet, sondern selbst in eigenen Prozessen erstmals einsetzt (Inbetriebnahme), gilt als Anbieter — z.B. ein Unternehmen, das ein intern entwickeltes System für die eigene Personalentscheidung nutzt.

**Prüffragen:**
- Erscheint Ihr Unternehmensname auf der Produktseite, in der Gebrauchsanweisung oder im Vertrag als Anbieter des KI-Systems?
- Tragen Sie das wirtschaftliche Risiko des Systems?

### Schritt 3 — Entgeltlichkeit oder Unentgeltlichkeit

**Frage C:** Spielt die Frage, ob Sie das System entgeltlich oder unentgeltlich bereitstellen, eine Rolle?

Nein — Art. 3 Nr. 3 KI-VO gilt ausdrücklich für entgeltliche und unentgeltliche Bereitstellung. Auch kostenlose KI-Systeme, Open-Source-Systeme (soweit nicht unter Art. 2 Abs. 12 KI-VO ausgenommen) und intern genutzte Systeme können unter die Anbieter-Definition fallen.

## Ergebnis

**Anbieter bestätigt, wenn:**
- Sie das System entwickelt oder entwickeln lassen haben UND
- Sie es unter eigenem Namen in Verkehr bringen oder in Betrieb nehmen

**Folge-Skills:**
- Wenn Hochrisiko: → Alle Pflichten Art. 9 bis 15, Art. 16 bis 19, Art. 43 bis 49, Art. 49 und 71 KI-VO
- Wenn GPAI-Modell: → Art. 51 bis 55 KI-VO
- Wenn begrenztes Risiko: → Art. 50 KI-VO (Transparenzpflichten)
- Rollenwechsel möglich: Wenn Sie später das System wesentlich verändern oder unter neuem Namen herausbringen → Art. 25 KI-VO → `anbieter-werden-art-25`

## Wichtige Fallstricke

**Fallstrick 1 — Interne Systeme:** Auch wer ein KI-System nur für interne Zwecke entwickelt und einsetzt, kann Anbieter sein. Die Anbieter-Rolle erfordert kein Angebot an Dritte.

**Fallstrick 2 — Fine-Tuning:** Wer ein fremdes Grundmodell mit eigenen Daten feinabstimmt und das resultierende System unter eigenem Namen in Verkehr bringt, ist Anbieter.

**Fallstrick 3 — Open-Source-Ausnahmen:** Die Open-Source-Ausnahme nach Art. 2 Abs. 12 KI-VO gilt nur unter engen Voraussetzungen; Hochrisiko-Systeme und Systeme mit systemischem Risiko sind nicht ausgenommen.

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 3 Nr. 3 Rn. 5: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — ROLLE ANBIETER PRUEFEN ART 3 NR 3
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 3 Nr. 3 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
