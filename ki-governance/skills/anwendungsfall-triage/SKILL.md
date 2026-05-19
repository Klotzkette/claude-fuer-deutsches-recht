---
name: anwendungsfall-triage
description: >
  Klassifiziert einen vorgeschlagenen KI-Anwendungsfall gegen das
  Unternehmensregister — freigegeben, bedingt oder nicht freigegeben —
  und erstellt Auflagenliste und nächste Schritte. Prüft gegen verbotene
  Praktiken (Art. 5 KI-VO) und Hochrisiko-Kategorien (Anhang III KI-VO).
  Lädt, wenn der Nutzer „KI-Anwendungsfall triage", „dürfen wir KI für X
  einsetzen", „ist das freigegeben" oder „Hochrisiko-KI klassifizieren" sagt.
language: de
triggers:
  - "KI-Anwendungsfall triage"
  - "dürfen wir KI für X einsetzen"
  - "ist das freigegeben"
  - "KI-Use-Case prüfen"
  - "AI Act Risikoklassifikation"
  - "verbotene KI-Praktiken prüfen"
  - "Hochrisiko-KI klassifizieren"
  - "KI-Einsatz genehmigen"
  - "Anhang III KI-VO prüfen"
---

# KI-Anwendungsfall-Triage

## Zweck

Das Gespräch stoppen, das als „Können wir nicht einfach KI dafür einsetzen?"
beginnt. Schnelle, kalibrierte Antwort aus dem Register geben — und bei
bedingter Freigabe die Auflagen konkret und den nächsten Schritt klar machen.

Die Triage-Skill ist ein Eingangstor: klassifizieren, Erforderliches
kennzeichnen, weiterleiten. Die Folgenabschätzungs-Skill erledigt die
Tiefenarbeit. Pflichtprüfung vor allem anderen: Art. 5 KI-VO (verbotene
Praktiken, ab 02.02.2025) und DSGVO Art. 22 (automatisierte Einzelentscheidung).

## Eingaben

- Beschreibung des KI-Anwendungsfalls: was tut die KI, wer ist betroffen,
  gibt es menschliche Überprüfung, welcher Anbieter?
- Praxisprofil aus `CLAUDE.md` (Anwendungsfall-Register, Rote Linien,
  Governance-Stufen, regulatorischer Fußabdruck)

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 5 KI-VO (verbotene Praktiken)**: Social Scoring durch
  öffentliche oder private Stellen (Art. 5 Abs. 1 lit. c); subliminale
  Manipulation (Art. 5 Abs. 1 lit. a/b); Ausnutzung von Vulnerabilität
  (Art. 5 Abs. 1 lit. b); biometrische Kategorisierung nach geschützten
  Merkmalen (Art. 5 Abs. 1 lit. g); Echtzeitfernidentifizierung in
  öffentlichen Räumen (Art. 5 Abs. 1 lit. h); Emotionserkennung am
  Arbeitsplatz/Bildung (Art. 5 Abs. 1 lit. f). Ab 02.02.2025 anwendbar.
- **AI Act Art. 6 i.V.m. Anhang III KI-VO**: Hochrisiko-Kategorien —
  Nr. 1 Biometrie; Nr. 2 Beschäftigung (Bewerbungs-Screening, Leistungs-
  bewertung); Nr. 3 Wesentliche Dienstleistungen (Kredit, Versicherung);
  Nr. 4 Bildung; Nr. 5 Kritische Infrastruktur; Nr. 6 Strafverfolgung;
  Nr. 7 Migration; Nr. 8 Rechtspflege. Hochrisiko: Art. 9–15 (Anbieter),
  Art. 26/29 (Betreiber).
- **DSGVO Art. 22**: Vollautomatisierte Einzelentscheidungen mit Rechtswirkung
  oder erheblicher Beeinträchtigung nur nach Art. 22 Abs. 2 lit. a–c
  (Vertrag, gesetzliche Pflicht, ausdrückliche Einwilligung). Widerspruchs-
  und Transparenzpflichten.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmungsrecht des Betriebsrats bei
  KI-Tools zur Mitarbeiterüberwachung/-bewertung.

**Leitentscheidungen**

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 Rn. 49 (Schufa-Score): Automatisiertes Profiling als Art. 22 Abs. 1 DSGVO-Entscheidung, wenn KI-Note maßgebliche Grundlage für Drittentscheidung; Maßstab für Scoring-/Kredit-/HR-Anwendungsfälle.
- EuGH, Urt. v. 04.10.2024 – C-203/22, NJW 2025, 56 Rn. 38 (Dun & Bradstreet): Betreiber algorithmischer Entscheidungssysteme müssen Entscheidungslogik verständlich offenlegen; Maßstab für Transparenzauflagen bei bedingter Freigabe.
- BAG, Urt. v. 13.01.2004 – 9 AZR 603/02, NZA 2004, 784 Rn. 16: Mitbestimmungspflicht bei technischen Überwachungssystemen; gilt für KI-basierte Mitarbeiterbewertung.
- BGH, Urt. v. 19.06.2018 – VI ZR 184/17, NJW 2018, 2877 Rn. 15: Haftung bei automatisierten Informationssystemen; Organisationspflicht bei KI-Einsatz.

**Kommentare**

- Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5 Rn. 8 (verbotene Praktiken) und Art. 6 i.V.m. Anhang III Rn. 15 (Hochrisiko-Klassifikation).
- Ehmann/Selmayr, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10.
- Müller-Glöge, in: Erfurter Kommentar, 25. Aufl. 2025, § 87 BetrVG Rn. 32.
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
  Teil IV Rn. 88.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Anwendungsfall verstehen**

Bei vager Beschreibung fragen: Was tut die KI genau? Auf wen/was wirkt sie?
Prüft ein Mensch vor Wirkung? Welcher Anbieter? Nur intern oder Kunden/Dritte?

**Schritt 2 — Art. 5-Prüfung (ERSTE PRIORITÄT)**

Vor dem Register prüfen: Liegt ein absolutes Verbot vor?
- Social Scoring, subliminale Manipulation, Vulnerabilitäts-Ausnutzung
- Biometrische Kategorisierung nach geschützten Merkmalen
- Echtzeitbiometrie in öffentlichen Räumen
- Emotionserkennung am Arbeitsplatz/Bildung

Bei Treffer: sofort melden, ohne Abmilderung:
> „Dieser Anwendungsfall berührt [Art. 5 KI-VO]. Verbotene Praktiken sind
> absolute Verbote. Wenn etwas anders ist: anwaltliche Entscheidung nötig,
> keine Triage-Freigabe."

**Schritt 3 — Register-Abgleich**

Direkttreffer → anwenden. Nahes Match → kennzeichnen. Kein Treffer →
BEDINGT (Folgenabschätzung ausstehend); vorläufige Risikoeinschätzung
einschließlich Anhang-III-Prüfung ausgeben.

**Schritt 4 — Jurisdiktionaler Anwendungsbereich und Anhang-III-Prüfung**

Alle Regime aus `## Regulatorischer Fußabdruck` prüfen. Striktest
anwendbare Behandlung bei Mehrfach-Jurisdiktion. Anhang-III-Kategorien
(Nr. 1–8) explizit gegen den Anwendungsfall prüfen; bei Hochrisiko:
Betreiberpflichten Art. 26/29 KI-VO vermerken.

**Schritt 5 — DSGVO Art. 22-Prüfung**

Vollautomatisiert + Rechtswirkung/erhebliche Beeinträchtigung? → Art. 22
Abs. 1 greift; Rechtsgrundlage nach Abs. 2 dokumentieren und Human-in-the-
Loop oder Einwilligung sicherstellen.

**Schritt 6 — Klassifikation und Ausgabe**

Bei Nicht-Jurist-Rolle: vor FREIGEGEBEN-Klassifikation anwaltliche Prüfung
abfragen; 1-seitigen Kurzüberblick für das Anwaltsgespräch generieren.

---

**ANWENDUNGSFALL:** [Anwendungsfall wie verstanden]
**KLASSIFIKATION:** [FREIGEGEBEN / BEDINGT / NICHT FREIGEGEBEN]
**Art. 5 KI-VO:** [Kein Verbot / [Verbotene Praxis] — ABSOLUTES VERBOT]
**Anhang III KI-VO:** [Nicht einschlägig / Hochrisiko Kategorie [Nr.]]
**DSGVO Art. 22:** [Nicht einschlägig / Einschlägig — Rechtsgrundlage: [Abs. 2]]
**Begründung:** [1–3 Sätze]
**Ausgelöste Rote Linien:** [Keine / Liste]

*Bei BEDINGT:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| KI-Folgenabschätzung (ggf. DSFA Art. 35 DSGVO) | [KI-Beauftragter] | ☐ |
| DSGVO Art. 22 Rechtsgrundlage dokumentieren | [DSB] | ☐ |
| Human-in-the-Loop — keine vollautomatisierten Entscheidungen | [Produkt] | ☐ |
| Offenlegung ggü. Betroffenen (Art. 13/14 DSGVO) | [Produkt/Recht] | ☐ |
| Betriebsrats-Beteiligung (§ 87 Abs. 1 Nr. 6 BetrVG) | [HR/Recht] | ☐ |

**Governance-Stufe:** [Standard / Erhöht / Hoch]

## Ausgabeformat

Bei Einzel-Anwendungsfall: wie oben. Bei mehreren Anwendungsfällen:
zuerst Übersichtstabelle (✅ Freigegeben / ⚠️ Bedingt / ❌ Nicht freigegeben
+ Schlüssel-Blocker), dann Detailausführung für bedingte und abgelehnte.

## Beispiel

**Anfrage:** „HR will KI zur automatischen Bewerbungs-Vorselektion einsetzen."
**Triage:** Art. 5: kein Verbot. Anhang III Nr. 2: Hochrisiko (Einstellungs-
entscheidung) `[prüfen-pinpoint]`. DSGVO Art. 22 Abs. 1 bei Vollautomatisierung.
§ 87 Abs. 1 Nr. 6 BetrVG: Betriebsrats-Beteiligung prüfen.
**Klassifikation: BEDINGT.** Folgenabschätzung + DSFA; Human-in-the-Loop;
Betriebsrat einbeziehen; Offenlegung ggü. Bewerber:innen (Art. 13 DSGVO).

## Risiken und typische Fehler

- Art. 5 KI-VO ist Pflichtprüfung — immer zuerst, vor dem Register.
- „Nur intern" reduziert das Risiko nicht: Mitarbeiter-KI oft höheres
  Risiko als kundenseitige KI.
- „Wir testen nur" ist keine Ausnahme bei echten Personen-Daten.
- „Der Anbieter sagt, es ist sicher" ersetzt nicht die eigene Folgenabschätzung.

## Quellenpflicht

- **AI Act Art. 5** und **Art. 6 i.V.m. Anhang III** (mit konkreter Nr.) bei
  jeder Klassifikation.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- **§ 87 Abs. 1 Nr. 6 BetrVG** bei Mitarbeiter-Überwachungs-/Bewertungstools.
- **EuGH C-634/21 (Schufa-Score)** bei Scoring-/Profiling-Anwendungsfällen.
- **Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5 Rn. 8 und Anhang III Rn. 15.**
- **Ehmann/Selmayr, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10.**
- **Müller-Glöge, in: Erfurter Kommentar, 25. Aufl. 2025, § 87 BetrVG Rn. 32.**
