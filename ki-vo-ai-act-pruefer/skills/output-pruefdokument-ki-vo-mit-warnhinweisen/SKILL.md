---
name: output-pruefdokument-ki-vo-mit-warnhinweisen
description: "Am Ende des KI-VO-Workflows wird ein abschliessendes Pruefdokument benoetigt das alle Ergebnisse zusammenfasst und dokumentiert. Art. 2 bis 55 KI-VO Gesamtpruefung. Pruefraster: Pflicht-Header keine Rechtsberatung Ergebnistabelle Risikoklasse Rolle Pflichten offene Punkte Warnhinweise. Output: strukturierter PDF/Word-Pruefbericht mit Disclaimer und Handlungsempfehlungen fuer Anwalt oder Compliance-Team. Abgrenzung zu nicht-hochrisiko-bestaetigt-end-to-end-roadmap (spezifisch Kein-Hochrisiko) und hochrisiko-bestaetigt-end-to-end-roadmap."
---

# Output: Prüfdokument KI-VO mit Warnhinweisen

## Zweck

Dieser Skill generiert das abschließende Prüfdokument am Ende des KI-VO-Workflows. Es fasst alle ermittelten Erkenntnisse zu Risikoklasse, Rolle, Pflichten und offenen Punkten zusammen.

## Pflicht-Header (IMMER voranstellen)

```
══════════════════════════════════════════
MECHANISCHES PRÜFDOKUMENT — KI-VO
Verordnung (EU) 2024/1689 des Europäischen
Parlaments und des Rates

ACHTUNG: Dieses Dokument ist KEINE
Rechtsberatung. Es handelt sich um eine
mechanische Prüfung anhand der vom Nutzer
behaupteten Tatsachen. Die Richtigkeit der
Tatsachenangaben wurde nicht überprüft.

Für verbindliche Rechtsauskunft wenden Sie
sich an einen zugelassenen Rechtsanwalt.
══════════════════════════════════════════
```

## Ergebnistabelle — Risikoklasse

| Prüfpunkt | Ergebnis | Fundstelle |
|---|---|---|
| KI-System nach Art. 3 Nr. 1 KI-VO | Ja / Nein / Unklar | Art. 3 Nr. 1 KI-VO |
| Territorialer Anwendungsbereich | Gegeben / Nicht gegeben / Unklar | Art. 2 KI-VO |
| Sachliche Ausnahme | Ja (welche) / Nein | Art. 2 Abs. 3-12 KI-VO |
| Verbotene Praktik Art. 5 | Ja (welche) / Nein / Unklar | Art. 5 KI-VO |
| Hochrisiko Art. 6 Abs. 1 | Ja / Nein / Unklar | Art. 6 Abs. 1 i.V.m. Anhang I KI-VO |
| Hochrisiko Art. 6 Abs. 2 | Ja (Anhang-III-Bereich) / Nein / Unklar | Art. 6 Abs. 2 i.V.m. Anhang III KI-VO |
| Rückausnahme Art. 6 Abs. 3 | Greift / Greift nicht / Unklar | Art. 6 Abs. 3 KI-VO |
| Begrenztes Risiko Art. 50 | Ja / Nein | Art. 50 KI-VO |
| GPAI-Modell Art. 3 Nr. 63 | Ja / Nein / Unklar | Art. 3 Nr. 63 KI-VO |
| Systemisches Risiko Art. 51 | Ja / Nein / Unklar | Art. 51 KI-VO |

## Ergebnistabelle — Rolle

| Rolle | Trifft zu | Fundstelle |
|---|---|---|
| Anbieter | Ja / Nein / Unklar | Art. 3 Nr. 3 KI-VO |
| Betreiber | Ja / Nein / Unklar | Art. 3 Nr. 4 KI-VO |
| Einführer | Ja / Nein / Unklar | Art. 3 Nr. 6 KI-VO |
| Händler | Ja / Nein / Unklar | Art. 3 Nr. 7 KI-VO |
| Bevollmächtigter | Zu benennen / Nicht erforderlich | Art. 22 KI-VO |
| Produkthersteller | Ja / Nein | Art. 25 Abs. 1 KI-VO |
| Anbieter durch Rollenwechsel | Ja / Nein / Prüfen | Art. 25 KI-VO |

## Pflichtenkatalog nach Rolle und Risikoklasse

Das System listet die einschlägigen Pflichten auf Basis der ermittelten Risikoklasse und Rolle:

**Bei Hochrisiko-Anbieter:**
- Risikomanagementsystem Art. 9 KI-VO
- Datenqualität Art. 10 KI-VO
- Technische Dokumentation Art. 11 / Anhang IV KI-VO
- Logging Art. 12 KI-VO
- Transparenz gegenüber Betreibern Art. 13 KI-VO
- Menschliche Aufsicht Art. 14 KI-VO
- Genauigkeit/Robustheit/Cybersicherheit Art. 15 KI-VO
- Konformitätsbewertung Art. 43 bis 49 KI-VO
- EU-Konformitätserklärung Art. 47 / Anhang V KI-VO
- CE-Kennzeichnung Art. 48 KI-VO
- Registrierung EU-Datenbank Art. 49 / 71 KI-VO
- Post-Market-Monitoring Art. 72 KI-VO

## Offene Punkte — Klärungsbedarf

Das System listet Punkte auf, die nicht abschließend bewertet werden konnten:
- Nicht beantwortete Fragen des Nutzers
- Unklare Sachverhalte
- Punkte, die fachanwaltliche Prüfung erfordern

## Zeitplan-Hinweis

Das System weist auf anwendbare Übergangsfristen hin:
- Verbote Art. 5: seit 2. Februar 2025 anwendbar
- GPAI: seit 2. August 2025 anwendbar
- Hochrisiko Anhang III: ab 2. August 2026 anwendbar

## Abschluss-Disclaimer

```
Dieses Prüfdokument wurde auf Basis der vom
Nutzer gemachten Angaben erstellt. Es ersetzt
keine anwaltliche Beratung. Die KI-VO und ihre
Auslegung durch Leitlinien und Rechtsprechung
sind laufend im Blick zu behalten.
```

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 9 Rn. 1: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — OUTPUT PRUEFDOKUMENT KI VO MIT WARNHINWEISEN
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 9 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
