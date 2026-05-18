---
name: investigation-summary
description: >
  Entwirft eine zielgruppengerechte Zusammenfassung aus dem vertraulichen
  Untersuchungsvermerk — für HR, Geschäftsführung/Aufsichtsrat oder externe
  Bevollmächtigte. Lädt, wenn ein Untersuchungsvermerk für eine Zielgruppe
  aufbereitet werden soll, die nicht den vollständigen vertraulichen Inhalt
  erhalten darf oder soll.
language: de
triggers:
  - "Untersuchung zusammenfassen"
  - "HR-Zusammenfassung Untersuchung"
  - "Aufsichtsrat briefen"
  - "Geschäftsführung informieren"
  - "externe Anwälte briefen"
  - "zielgruppengerechte Zusammenfassung"
  - "Untersuchungsergebnis kommunizieren"
---

# Untersuchungs-Zusammenfassung für Zielgruppen (Arbeitsrecht)

## Zweck

Entwirft eine auf die jeweilige Zielgruppe zugeschnittene Zusammenfassung
aus dem vertraulichen Untersuchungsvermerk. HR-Zusammenfassungen enthalten
keine anwaltliche Analyse. Zusammenfassungen für Geschäftsführung und
Aufsichtsrat bleiben auf hohem Niveau. Briefings an externe Bevollmächtigte
umfassen den vollständigen Kontext.

Lädt, wenn ein Untersuchungsergebnis an eine Zielgruppe kommuniziert werden
soll, die nicht den vollständigen Vermerk erhalten darf oder soll.

## Eingaben

- Bezeichnung der Untersuchungssache
- Zielgruppe: `hr` / `geschaeftsfuehrung` / `externe-ar`
- Zweck der Zusammenfassung (welche Entscheidung oder Maßnahme soll sie
  unterstützen?)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Zweckbindung bei Beschäftigtendaten — Weitergabe von
  Untersuchungsdaten nur soweit für den jeweiligen Zweck erforderlich;
  bei HR-Zusammenfassungen Datenminimierung nach Art. 5 Abs. 1 lit. c DSGVO
- § 102 BetrVG: Anhörung des Betriebsrats vor Kündigung — HR-Zusammenfassung
  stellt oft die Tatsachengrundlage für die BR-Anhörung; Vollständigkeit
  und Richtigkeit entscheidend (Theorie der subjektiven Determinierung)
- § 22 AGG: Beweislastverteilung — bei AGG-Sachverhalt muss die
  Zusammenfassung für den Arbeitgeber verwertbare Ergebnisse zur
  Enthaftung dokumentieren
- §§ 93, 116 AktG / § 43 GmbHG: Informationspflichten und Haftung der
  Geschäftsleitung — bei der Aufsichtsrats-/GF-Zusammenfassung muss der
  Informationsgehalt ausreichen, um informierte Governance-Entscheidungen
  zu ermöglichen
- §§ 34, 37 HinSchG: Bei Hinweisgebersachen muss die Zusammenfassung
  die Identität der hinweisgebenden Person schützen; keine Rückschlüsse

**Leitentscheidungen:**

- BAG, Urt. v. 23.08.2018 – 2 AZR 133/18, NZA 2018, 1329 Rn. 29 ff.:
  Inhalt der BR-Anhörung — die Anhörung muss den Sachverhalt vollständig
  und richtig wiedergeben; fehlerhafte Grundlage (z. B. aus unvollständiger
  HR-Zusammenfassung) macht die Kündigung unwirksam
- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 Rn. 14 ff.:
  Verdachtskündigung — Ergebnisse müssen auf objektiven Tatsachen beruhen,
  die auch in einer HR-Kommunikation lückenlos nachvollziehbar sind
- BGH, Urt. v. 04.07.2017 – II ZR 319/15, NJW 2017, 3143 Rn. 22 ff.:
  Informationspflichten der Geschäftsleitung gegenüber dem Aufsichtsrat bei
  laufenden Untersuchungen; Dokumentationspflicht für Governance-Entscheidungen

**Kommentarliteratur:**

- Erfurter Kommentar/Kiel, 24. Aufl. 2024, § 102 BetrVG Rn. 50 ff.:
  Inhalt und Anforderungen der BR-Anhörung; Folgen unvollständiger Mitteilung;
  Theorie der subjektiven Determinierung
- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 150 ff.:
  Weitergabe von Untersuchungsdaten an betriebsinterne Stellen;
  Zweckbindung und Datenminimierung
- Bauer/Krieger/Günther, AGG, 5. Aufl. 2022, § 12 Rn. 45 ff.:
  Dokumentation der Untersuchungsergebnisse als Enthaftungsgrundlage;
  Anforderungen an die Schlussfolgerungen

## Ablauf

**Schritt 1 — Referenz-Skill laden**

Lade die Referenz-Skill `internal-investigation` und führe Modus 5
(Zielgruppen-Zusammenfassung) aus.

**Schritt 2 — Vermerk prüfen**

Falls noch kein Vermerk existiert: Anbieten, den Vermerk zuerst zu
erstellen (`/arbeitsrecht:investigation-memo [Sache]`).

**Schritt 3 — Zielgruppe und Zweck klären**

Fragen: Für wen ist die Zusammenfassung und welche Entscheidung oder
Maßnahme soll sie unterstützen?

**Schritt 4 — Zielgruppengerechte Erstellung**

**HR-Zusammenfassung** (für disziplinarische Entscheidung):

Inhalt:
- Was ist passiert (Sachverhaltsdarstellung in klarer Sprache, keine
  Rechtsanalyse)
- Ergebnis zu jedem Vorwurf (Bestätigt / Nicht bestätigt / Unklar)
- Empfohlene Maßnahme
- Verweis auf noch offene Ermittlungsstränge (falls vorhanden)

Nicht enthalten:
- Glaubwürdigkeitsmethodik und anwaltliche Abwägungen
- Rechtsrisikoanalyse und Haftungseinschätzung
- Anwaltliche Arbeitseindrücke und mentale Bewertungen
- Protokoll-Eintrags-IDs oder Dokumentenverweise

Kopfzeile: „Vertraulich — Nur HR — Keine Weitergabe"

**§ 102 BetrVG-Hinweis:** Diese Zusammenfassung wird oft als Grundlage
der BR-Anhörung verwendet. Sachverhaltsdarstellung muss vollständig und
korrekt sein. Fehlende oder falsche Angaben in der BR-Anhörung führen
zur Unwirksamkeit der Kündigung (Theorie der subjektiven Determinierung).

**Geschäftsführung / Aufsichtsrat** (für Governance-Entscheidung):

Inhalt:
- Vorwurf und Untersuchungsumfang (ein Abschnitt)
- Wesentliche Ergebnisse
- Unternehmensrelevanz und Expositionseinschätzung
  (nur grob — keine Detailrechtsanalyse)
- Ergriffene und geplante Maßnahmen

Kopfzeile: „Vertraulich — Interne Untersuchung — Geschäftsleitung"

**§§ 93, 116 AktG / § 43 GmbHG-Hinweis:** Die Zusammenfassung muss den
Informationsgehalt haben, der für eine ordnungsgemäße und haftungsbefreiende
Governance-Entscheidung erforderlich ist. Unterinformation kann
Geschäftsleiterhaftung begründen.

**Externe Bevollmächtigte** (für Prozessvorbereitung oder vertiefende Prüfung):

Inhalt:
- Vollständiger Kontext einschließlich Rechtsrisikoanalyse
- Offene Beweisstränge
- Ungelöste Glaubwürdigkeitsfragen
- Dokumente mit erhöhter Prozessrelevanz
- Eintrags-IDs und Quellendokumentation

Kopfzeile: „Vertraulich — Interne Untersuchung"

**HinSchG-Schutzpflicht (bei Hinweisgebersachen):**
In allen Zielgruppen-Zusammenfassungen: Identität der hinweisgebenden
Person darf nicht erkennbar sein (§§ 8, 37 HinSchG). Zusammenfassung
vor Weitergabe auf Rückschlüsse prüfen.

## Ausgabeformat

Zielgruppengerechte Zusammenfassung mit Kopfzeile, Sachverhaltsdarstellung,
Ergebnistabelle und (falls HR) Handlungsempfehlung. HR-Zusammenfassungen
ohne Eintrags-IDs, Rechtsanalyse und Glaubwürdigkeitsbewertung.

## Beispiel

```
/arbeitsrecht:investigation-summary Sache-Mueller hr
```

```
/arbeitsrecht:investigation-summary Sache-Mueller geschaeftsfuehrung
```

```
/arbeitsrecht:investigation-summary Sache-Mueller externe-ar
```

Beispiel-Ausgabe HR-Zusammenfassung (Ausschnitt):

```
Vertraulich — Nur HR — Keine Weitergabe
Interne Untersuchung — Sache Müller — [Datum]

Hintergrund:
Am [Datum] wurde eine Beschwerde über [Vorwurf] eingereicht.
Die Untersuchung wurde am [Datum] eingeleitet und umfasste [N] Befragungen
sowie die Sichtung von [N] Dokumenten.

Ergebnisse:

| Vorwurf | Ergebnis |
|---|---|
| Unzulässige Benachteiligung nach § 3 AGG | Nicht bestätigt |
| Verstoß gegen Verhaltenskodex | Bestätigt |

Empfehlung:
[HR-Maßnahme — kein Rechtstext, klare Sprache]
```

## Risiken und typische Fehler

- **HR-Zusammenfassung zu reichhaltig**: Anwaltliche Analyse, Credibility-
  Bewertung und Haftungseinschätzung in der HR-Zusammenfassung können
  den vertraulichen Charakter der Untersuchungsunterlagen gefährden
  und müssen dort nicht stehen.
- **BR-Anhörungsgrundlage lückenhaft**: Wenn die HR-Zusammenfassung
  der BR-Anhörung als Tatsachengrundlage dient und unvollständig ist,
  ist die Kündigung unwirksam.
- **HinSchG-Identitätsschutz verletzt**: Rückschlüsse auf die hinweisgebende
  Person in der Zusammenfassung können Repressalie nach § 36 HinSchG
  begründen.
- **Geschäftsleitung unterinformiert**: Eine zu knappe GF/AR-Zusammenfassung
  kann die Grundlage für informierte Governance-Entscheidungen nehmen
  und Geschäftsleiterhaftung auslösen.
- **Externe Bevollmächtigte ohne Prozessrelevanz**: Das Briefing für externe
  AR muss die für Prozessführung wesentlichen offenen Stränge und
  Dokumentenrisiken enthalten — ohne diese ist das Mandat unzureichend.

## Quellenpflicht

Bei allen Ausgaben zitieren (zielgruppenspezifisch):

- Bei HR-Zusammenfassung für BR-Anhörung: § 102 BetrVG;
  Erfurter Kommentar/Kiel, 24. Aufl. 2024, § 102 BetrVG Rn. 50 ff.
- Bei AGG-relevantem Sachverhalt: § 22 AGG;
  Bauer/Krieger/Günther, AGG, 5. Aufl. 2022, § 12 Rn. 45 ff.
- Bei Hinweisgebersachen: §§ 8, 37 HinSchG
- Bei GF/AR-Briefing: §§ 93, 116 AktG / § 43 GmbHG;
  BGH, Urt. v. 04.07.2017 – II ZR 319/15, NJW 2017, 3143
- § 26 BDSG (Zweckbindung, Datenminimierung)

Detaillierte Zielgruppen-Stripping-Regeln und Zusammenfassungs-Templates
befinden sich in der Referenz-Skill `internal-investigation` — diese vor
inhaltlicher Arbeit laden.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
