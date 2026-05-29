---
name: hochrisiko-konformitaetsbewertung-art-43-bis-49
description: "Anbieter von Hochrisiko-KI fragt: Muessen wir eine benannte Stelle einschalten oder koennen wir die Konformitätsbewertung selbst durchführen? Art. 43 bis 49 KI-VO Konformitätsbewertung. Prüfraster: Entscheidungsbaum Selbstbewertung Modul A vs. Drittstellenprüfung Modul H vollständiges QMS. CE-Kennzeichnung EU-Konformitätserklärung Anhang V Registrierung EU-Datenbank. Output: Verfahrensauswahl-Entscheidungsbaum und Zeitplanung. Abgrenzung zu output-konformitaetserklaerung-eu-anhang-v und output-konformitaetsbescheinigung-evidence-pack."
---

# Konformitätsbewertung — Art. 43 bis 49 KI-VO

## Zweck

Vor dem Inverkehrbringen oder der Inbetriebnahme eines Hochrisiko-KI-Systems muss eine Konformitätsbewertung durchgeführt werden. Dieser Skill liefert den Entscheidungsbaum: Wer bewertet? Welches Verfahren? Was ist danach zu tun?

Wenn das Ergebnis anschließend druckreif als Bescheinigung, EU-Konformitätserklärung, Evidence Index und Lückenliste ausgegeben werden soll, an `output-konformitaetsbescheinigung-evidence-pack` übergeben.

## Entscheidungsbaum — Selbstbewertung oder benannte Stelle?

### Schritt 1 — Anhang-I-Systeme oder Anhang-III-Systeme?

**Anhang-I-Systeme (Art. 6 Abs. 1 KI-VO):** KI-Systeme als Sicherheitsbauteil in Produkten, die unter Anhang-I-Sektorrecht fallen.

Für diese Systeme richtet sich das Konformitätsbewertungsverfahren nach dem jeweiligen Sektorrecht (z.B. MDR, Maschinenverordnung). Wenn das Sektorrecht eine Konformitätsbewertung durch Dritte vorschreibt, gilt diese auch für das KI-System. In diesem Fall ist die Einbindung einer benannten Stelle obligatorisch.

**Anhang-III-Systeme (Art. 6 Abs. 2 KI-VO):** KI-Systeme, die in einem der acht Hochrisiko-Bereiche des Anhangs III tätig sind.

→ weiter zu Schritt 2.

### Schritt 2 — Biometrische Fernidentifikation?

Wenn das Hochrisiko-KI-System zur biometrischen Fernidentifikation von Personen verwendet wird:
- **Verpflichtend: Konformitätsbewertung durch benannte Stelle (Modul H)** — keine Selbstbewertung möglich (Art. 43 Abs. 1 lit. a KI-VO)

→ weiter zu Modul H.

### Schritt 3 — Alle anderen Anhang-III-Systeme

Für alle anderen Hochrisiko-KI-Systeme aus Anhang III besteht eine Wahlmöglichkeit:

**Option A — Selbstbewertung (Modul A nach Art. 43 Abs. 2 KI-VO)**
- Der Anbieter bewertet das System selbst anhand der in Art. 9 bis 15 KI-VO und Anhang IV festgelegten Anforderungen
- Interne Kontrolle der technischen Dokumentation
- Erstellung der EU-Konformitätserklärung
- CE-Kennzeichnung

**Voraussetzung:** Das System muss vollständig mit harmonisierten Normen (Art. 40 KI-VO) oder gemeinsamen Spezifikationen (Art. 41 KI-VO) konform sein.

**Option B — Konformitätsbewertung durch benannte Stelle (Modul H)**
- Vollständiges Qualitätsmanagementsystem (QMS) nach Anhang IX KI-VO
- Oder Bewertung der technischen Dokumentation durch benannte Stelle nach Anhang X KI-VO
- Benannte Stelle prüft, ob die Anforderungen erfüllt sind, und stellt eine Bescheinigung aus
- Anbieter erstellt EU-Konformitätserklärung und bringt CE-Kennzeichnung an

**Prüffragen:**
- Liegt für alle wesentlichen Anforderungen eine vollständige Abdeckung durch harmonisierte Normen vor?
- Hat der Anbieter ausreichende interne Kapazitäten für eine belastbare Selbstbewertung?
- Fordern Vertragspartner oder Kunden eine unabhängige Zertifizierung?

## EU-Konformitätserklärung (Art. 47 KI-VO / Anhang V KI-VO)

Nach erfolgter Konformitätsbewertung muss der Anbieter eine EU-Konformitätserklärung ausstellen. Diese enthält:
- Name und Anschrift des Anbieters
- Name und Nummer der benannten Stelle (falls zutreffend)
- Bezeichnung des KI-Systems
- Erklärung, dass das System den Anforderungen der KI-VO entspricht
- Verweis auf angewandte harmonisierte Normen oder gemeinsame Spezifikationen
- Ort und Datum der Ausstellung
- Unterschrift

Die EU-Konformitätserklärung wird zehn Jahre aufbewahrt.

## CE-Kennzeichnung (Art. 48 KI-VO)

Nach ausgestellter Konformitätserklärung ist am Hochrisiko-KI-System die CE-Kennzeichnung anzubringen. Bei rein digital bereitgestellten Systemen ist die CE-Kennzeichnung in der Benutzeroberfläche oder Begleitdokumentation anzubringen. Die Kennzeichnung muss gut sichtbar, lesbar und dauerhaft sein.

## Registrierung in der EU-Datenbank (Art. 49 und 71 KI-VO)

→ Detailskill: `eu-datenbank-registrierung-art-49-und-71`

Kurzüberblick:
- Anbieter registrieren vor Inverkehrbringen
- Betreiber (öffentliche Stellen) registrieren vor Nutzung
- Inhalte nach Anhang VIII KI-VO
- Datenbank ist öffentlich zugänglich (soweit nicht als vertraulich eingestuft)

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — HOCHRISIKO KONFORMITAETSBEWERTUNG ART 43 BIS 49
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 43 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
