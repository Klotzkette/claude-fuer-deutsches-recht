---
name: widerspruch-formulieren
description: Entwirft einen begruendeten Widerspruch gegen einen Sozialleistungsbescheid nach § 84 SGG (Widerspruchsfrist ein Monat ab Bekanntgabe — bei fehlender Rechtsbehelfsbelehrung ein Jahr nach § 66 Abs. 2 SGG). Aus der Bescheidanalyse uebernommene formelle und materielle Angriffspunkte werden in Standardstruktur gegossen (Rubrum Antrag Begruendung Anlagenverzeichnis). Inkludiert hilfsweisen Antrag auf Aussetzung der Vollziehung nach § 86a SGG und Antrag auf Akteneinsicht nach § 25 SGB X.
---

# Widerspruch formulieren (Sozialrecht)

## Eingaben

- Analyseprotokoll aus `bescheidanalyse`.
- Mandantenakte mit Belegen.
- Bescheid im Original.

## Struktur

### 1. Rubrum

- Mandant mit Anschrift Geburtsdatum (sozialrechtlich relevant).
- Anwalt mit Adresse beA-/EGVP-Adresse Aktenzeichen.
- Empfangsbehörde mit Adresse.
- Bezug: Az der Behörde Bescheid vom (Datum).

### 2. Antrag

- "Hiermit lege ich gegen den Bescheid vom (Datum), Az (...), Widerspruch ein und beantrage:
  1. den angefochtenen Bescheid aufzuheben;
  2. (oder) den Bescheid abzuändern und mir Leistungen in voller Höhe zuzuerkennen;
  3. hilfsweise Aussetzung der Vollziehung nach § 86a SGG;
  4. Akteneinsicht in die Verwaltungsakte gemäß § 25 SGB X."

### 3. Begründung

Aus dem Analyseprotokoll übernehmen:

- Formelle Mangel zuerst (Anhörung Begründungs- und Rechtsbehelfsbelehrungsfehler).
- Materielle Mangel sortiert nach Erfolgsaussicht.
- Subsumtion zur konkreten Anspruchsgrundlage.
- Rechtsprechung mit Pinpoint (BSG-Urteile mit Az und Rn).
- Vorgreiflichkeit von Verfassungs- und Unionsrecht falls einschlägig.

### 4. Beweis- und Anlagenverzeichnis

Verweis auf den Skill `anlagen-erstellen`. Anlagen W1 W2 W3 mit Inhaltsbeschreibung.

### 5. Form und Frist

- **Frist** ein Monat ab Bekanntgabe (§ 84 Abs. 1 SGG).
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr (§ 66 Abs. 2 SGG).
- **Form** schriftlich oder zur Niederschrift bei der Behörde.
- **Versand** über beA (RA-Pflicht seit 01.01.2022) oder EGVP. Eingang am Tag der Übertragung.

### 6. Vorfrist im Fristenbuch

Drei Tage vor Fristablauf Vorfrist setzen über den Skill `fristenbuch-sozialrecht`.

## Ausgabe

- `widerspruch-<az>-<datum>.docx` und Markdown-Spiegel.
- Eintrag im Fristenbuch.
- Eintrag im Postausgang.

## Versand-Check

Vor Versand der Skill `versand-vor-check` aus dem Plugin `kanzlei-cowork`. Prüft PDF Inhalt Signatur Empfängeradresse und Anlagenvollständigkeit.

## Hinweis Aussetzung der Vollziehung

Bei Bescheiden über Aufhebung Rückforderung Sanktion: Widerspruch hat keine aufschiebende Wirkung wenn die Behörde die sofortige Vollziehung angeordnet hat oder das Gesetz sie vorsieht (§ 86a Abs. 2 SGG). Hilfsantrag auf Aussetzung der Vollziehung an die Behörde — bei Ablehnung Eilantrag § 86b SGG ans Sozialgericht (siehe Skill `eilantrag-sozialrecht`).
