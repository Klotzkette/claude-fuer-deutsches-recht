---
name: hochrisiko-zuordnung-art-6-und-anhang-i-iii
description: "Anwalt oder Compliance-Beauftragter benoetigt Gesamtuebersicht der Hochrisiko-Zuordnungsregeln bevor eine Detailpruefung begonnen wird. Art. 6 KI-VO Sicherheitsbauteil plus Anhang I (Art. 6 Abs. 1) vs. eigenstaendige Nennung in Anhang III (Art. 6 Abs. 2). Alle acht Anhang-III-Bereiche und vier Rueckausnahmen Art. 6 Abs. 3 KI-VO. Output: Gesamtuebersichtstabelle Hochrisiko-Kategorien. Abgrenzung zu hochrisiko-art-6-abs-1-sicherheitsbauteil und hochrisiko-art-6-abs-2-anhang-iii (Detailpruefungen)."
---

# Hochrisiko-Zuordnung — Art. 6 KI-VO und Anhang I/III

## Zweck

Dieser Skill ist die erste Orientierung zu Art. 6 KI-VO. Er zeigt beide Pfade zur Hochrisiko-Einstufung und verweist auf die detaillierten Prüfskills für jeden Pfad. Vertiefende Entscheidungsbäume finden sich in `hochrisiko-art-6-abs-1-sicherheitsbauteil`, `hochrisiko-art-6-abs-2-anhang-iii` und `rueckausnahme-art-6-abs-3`.

## Zwei Pfade zur Hochrisiko-Einstufung

### Pfad 1 — Art. 6 Abs. 1 KI-VO: Sicherheitsbauteil + Anhang I + Drittprüfung

Ein KI-System gilt als Hochrisiko-KI-System, wenn beide Voraussetzungen erfüllt sind:
1. Es ist ein Sicherheitsbauteil eines Produkts oder ist selbst ein Produkt, das unter die in Anhang I aufgeführten Unionsvorschriften fällt.
2. Das Produkt (oder die Sicherheitskomponente) muss nach diesen Unionsvorschriften einer Konformitätsbewertung durch Dritte unterzogen werden.

**Anhang I enthält unter anderem:** Maschinen (VO (EU) 2023/1230), Spielzeug (Richtlinie 2009/48/EG), Luftfahrt-Bauteile (VO (EU) 2018/1139), Medizinprodukte (VO (EU) 2017/745), In-vitro-Diagnostika (VO (EU) 2017/746), Druckgeräte, Aufzüge, Funkanlagen, Kraftfahrzeuge, Schifffahrt, Eisenbahn.

→ Detailprüfung: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

### Pfad 2 — Art. 6 Abs. 2 KI-VO: Eigenständige Nennung in Anhang III

Ein KI-System gilt als Hochrisiko-KI-System, wenn es in Anhang III der KI-VO aufgeführt ist oder eine der dort genannten Verwendungsweisen aufweist.

**Anhang III — Acht Bereiche:**

1. Biometrische Identifikation und Kategorisierung natürlicher Personen (außer Ausnahmen)
2. Kritische Infrastruktur: Betrieb und Verwaltung kritischer Infrastruktur (Wasser, Gas, Strom, Verkehr)
3. Bildung und Berufsausbildung: Zulassung, Bewertung, Prüfungsergebnisse, Lernfortschritt
4. Beschäftigung und Arbeitnehmerverwaltung: Personalauswahl, Beförderung, Kündigung, Überwachung
5. Wesentliche private und öffentliche Dienstleistungen: Kreditwürdigkeit, Sozialleistungen, Notfalldienste
6. Strafverfolgung: Risikoabschätzung von Personen, Polygraphen, Zuverlässigkeit von Beweismitteln, Profiling
7. Migration, Asyl, Grenzkontrolle: Risikoabschätzung, Identitätsprüfung, Entscheidungen zu Asyl und Grenzübertritt
8. Justiz und demokratische Prozesse: Anwendung der Rechtsvorschriften, Auslegung von Tatsachen, Wahlbeeinflussung

→ Detailprüfung: `hochrisiko-art-6-abs-2-anhang-iii`

## Rückausnahme Art. 6 Abs. 3 KI-VO

Auch bei Vorliegen eines Anhang-III-Tatbestands können KI-Systeme ausnahmsweise nicht als Hochrisiko eingestuft werden, wenn sie keine erhebliche Risiken für Gesundheit, Sicherheit oder Grundrechte darstellen. Vier Fallgruppen:
1. Enge Verfahrensaufgabe
2. Verbesserung des Ergebnisses einer menschlichen Tätigkeit
3. Erkennung von Mustern ohne Ersetzung menschlicher Bewertung
4. Vorbereitende Aufgabe

**Sicherungsklausel:** Profiling natürlicher Personen ist stets Hochrisiko — keine Rückausnahme.

→ Detailprüfung: `rueckausnahme-art-6-abs-3`

## Folgen der Hochrisiko-Einstufung

Liegt eine Hochrisiko-Einstufung vor, greifen für Anbieter folgende Pflichten:
- Risikomanagementsystem (Art. 9 KI-VO)
- Datenqualität und Data Governance (Art. 10 KI-VO)
- Technische Dokumentation (Art. 11 und Anhang IV KI-VO)
- Logging und Aufzeichnung (Art. 12 KI-VO)
- Transparenz gegenüber Betreibern (Art. 13 KI-VO)
- Menschliche Aufsicht (Art. 14 KI-VO)
- Genauigkeit und Cybersicherheit (Art. 15 KI-VO)
- Konformitätsbewertung und CE-Kennzeichnung (Art. 43 bis 49 KI-VO)
- Registrierung in EU-Datenbank (Art. 49 i.V.m. Art. 71 KI-VO)

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 12: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — HOCHRISIKO ZUORDNUNG ART 6 UND ANHANG I III
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Rn. 12]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
