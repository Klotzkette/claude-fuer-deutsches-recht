---
name: richtlinien-vorlage
description: >
  Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter
  Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool,
  dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist,
  keine fertige Richtlinie. Lädt, wenn der Nutzer „KI-Richtlinie entwerfen",
  „wir brauchen eine KI-Richtlinie", „AI-Act-konforme Richtlinie" oder
  Ähnliches sagt.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - KI-Richtlinie entwerfen
  - KI-Nutzungsrichtlinie erstellen
  - AI-Act-konforme Richtlinie
  - wir brauchen eine KI-Richtlinie
  - interne KI-Governance-Richtlinie
  - KI-Richtlinie aktualisieren
  - GenAI-Richtlinie aufsetzen
  - Acceptable-Use-Policy KI
---

# KI-Richtlinien-Starter

## Zweck

Viele Unternehmen haben noch keine schriftliche KI-Nutzungsrichtlinie, oder
arbeiten mit einer veralteten Fassung, die den AI Act (VO (EU) 2024/1689),
DSGVO Art. 22 und den tatsächlichen Tool-Einsatz nicht abbildet.

Dieser Skill produziert einen **Entwurf** — keinen fertigen Text. Disziplin:
(1) aus veröffentlichten Musterquellen sourcing, nicht aus dem Nichts;
(2) Umfang vor Entwurf klären; (3) jeden Ermessensspielraum mit `[prüfen]`
kennzeichnen; (4) Adoptionstatus-Signale nicht abschwächen.

Dieser Skill schließt keine Richtlinie ab, verteilt sie nicht und empfiehlt
keine konkrete Position zu den schwierigen Entscheidungspunkten.

## Eingaben

- Praxisprofil aus `CLAUDE.md` (KI-Rolle, regulatorischer Fußabdruck,
  bestehendes Register, Governance-Team, ggf. bestehende Richtlinie)
- Scopegespräch: welche Abschnitte? welche Zielgruppe? welcher Kontext?

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 4 KI-VO**: KI-Kompetenzverpflichtung — Anbieter und Betreiber
  müssen hinreichende KI-Kompetenz ihres Personals sicherstellen; Richtlinie
  muss Schulungspflicht abbilden.
- **AI Act Art. 9 KI-VO**: Risikomanagementsystem für Hochrisiko-KI; interne
  Richtlinien müssen Risikoidentifikations- und Mitigationsverfahren beschreiben.
- **AI Act Art. 26/29 KI-VO**: Betreiberpflichten — menschliche Aufsicht,
  Protokollierung, Meldeobliegenheiten; müssen in der Richtlinie operationalisiert
  werden.
- **DSGVO Art. 22**: Vollautomatisierte Einzelentscheidungen nur unter Art. 22
  Abs. 2 lit. a–c zulässig; Richtlinie muss Rechtsgrundlage und
  Widerspruchsrecht klären.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmungsrecht des Betriebsrats bei KI-
  Tools zur Mitarbeiterüberwachung/-bewertung; vor Richtlinienabschnitt prüfen.
- **GeschGehG §§ 2, 4**: Schutz von Geschäftsgeheimnissen bei Eingabe
  vertraulicher Daten in externe KI-Systeme.
- **UrhG § 44b**: Text-und-Data-Mining-Schranke; relevant bei KI-Training.

**Leitentscheidungen**

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 (Schufa-Score):
  Richtlinie muss Art. 22 Abs. 3 DSGVO-Widerspruchsrecht bei automatisierten
  Entscheidungen operationalisieren.
- EuGH, Urt. v. 04.10.2024 – C-203/22 (Dun & Bradstreet): Offenlegungspflicht
  bei algorithmischen Entscheidungen in verständlicher Sprache; maßgeblich
  für den Transparenz-Abschnitt einer Richtlinie.
- BAG, Urt. v. 13.01.2004 – 9 AZR 603/02, NZA 2004, 784: Mitbestimmungs-
  pflicht bei technischen Überwachungssystemen; gilt auch für KI-basierte
  Mitarbeiterbewertung.
- BGH, Urt. v. 19.06.2018 – VI ZR 184/17, NJW 2018, 2877: Interne
  Organisationspflichten bei technischen Systemen; übertragbar auf
  KI-Governance-Richtlinien.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 4 Rn. 3 ff.
  (KI-Kompetenzverpflichtung; interne Richtliniengestaltung).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 1 ff.
- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 87 BetrVG Rn. 32 ff.
  (Mitbestimmung bei KI-Tools).
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
  Teil IV Rn. 100 ff. (Compliance-Anforderungen für KI-Nutzungsrichtlinien).

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Praxisprofil laden**

`CLAUDE.md` lesen. Wenn `## KI-Richtlinien-Verpflichtungen` ausgefüllt:
Update-Modus (bestehende Richtlinie als Basis). Wenn leer: Erstfassung.

**Schritt 2 — Scopegespräch (VOR dem Entwurf)**

> **Welche Abschnitte soll die KI-Richtlinie enthalten?**
> 1. Anwendungsbereich (wer, welche Tools, welche Daten)
> 2. Erlaubte und verbotene Nutzungen (inkl. Art. 5 KI-VO-Verbote)
> 3. Freigabe und Prüfung (Genehmigungsworkflow)
> 4. Offenlegung (Kunden, Mitarbeitende, Dritte; DSGVO Art. 13/14)
> 5. Datenhandhabung (vertrauliche Daten, Anbieter-Training; GeschGehG)
> 6. Schulung und Zertifizierung (Art. 4 KI-VO)
> 7. Vorfälle und Meldung (Art. 73 KI-VO Betreiber-Meldeobliegenheiten)
> 8. Durchsetzung (Verweis auf Disziplinarrahmen)
> 9. Überprüfungsrhythmus und Verantwortung (mind. jährlich)
> 10. Glossar (Hochrisiko-KI gem. Anhang III, DSGVO Art. 22, GeschGeh usw.)
>
> Empfohlenes Startpaket für Erstfassungen: 1, 2, 3, 4, 5, 9.

Dann: Zielgruppe (alle MA / Rechtsabteilung / mit Betriebsrat?) und
Anwendungskontext (Unternehmen / Konzern / Kanzlei / Behörde).

**Schritt 3 — Musterquellen recherchieren**

Aktuelle veröffentlichte Muster-KI-Richtlinien und Leitlinien suchen:
- Deutschland/EU: AI Act direkt (Art. 4, 9, 26, 29); EDPB Guidelines 01/2022
  (Art. 22 DSGVO); DSK-Orientierungshilfen; BSI-Empfehlungen; Bitkom/DAV-
  Leitlinien; veröffentlichte Unternehmensrichtlinien aus DAX-Umfeld.
- Jeden verwendeten Quellennachweis im **Quellenblock** dokumentieren:
  Name, URL, Zugriffsdatum, was der Entwurf daraus entnommen hat.

**Schritt 4 — Entwurf erstellen**

Kopfzeile:
```
ENTWURF ZUR INTERNEN RECHTLICHEN PRÜFUNG — NICHT ZUR VERTEILUNG
Erstellt für: [Unternehmensname] | Datum: [heute]
Nicht zur Beschlussfassung bis von [Syndikusrechtsanwalt / GC / Compliance
Officer] geprüft, angepasst und freigegeben.
```

Für jeden Abschnitt: materielle Regeln aus Musterquellen, inline-
Quellenattribution, jeder Schwellenwert/Tool/Anbieter/Kontakt als `[prüfen]`.

Freigabe-Checkliste am Ende:
- [ ] Syndikusrechtsanwalt / GC `[prüfen — Name]`
- [ ] IT / Informationssicherheit `[prüfen]`
- [ ] HR (für Durchsetzungs-/Schulungsabschnitte) `[prüfen]`
- [ ] Betriebsrat (§ 87 Abs. 1 Nr. 6 BetrVG) `[prüfen — erforderlich?]`
- [ ] Datenschutzbeauftragter (Art. 38 Abs. 1 DSGVO) `[prüfen]`
- [ ] Inkrafttretungsdatum und Überprüfungsrhythmus `[prüfen]`

## Ausgabeformat

Strukturiertes Markdown-Dokument: Kopfzeile, Quellenblock, Zusammenfassung
(max. 3 Abs.), gewählte Abschnitte (materielle Regeln + inline-Quellen +
offene Fragen je Abschnitt), Freigabe-Checkliste, Prüfhinweis. Sprache
klar genug für Nicht-Juristen; Präzision liegt in den `[prüfen]`-Markern.

## Beispiel

**Anfrage:** KI-Richtlinie für 200-Personen-Unternehmen mit Betriebsrat,
Abschnitte 1, 2, 3, 5 und 9. **Vorgehen:** Betreiberrolle, Deutschland;
AI Act Art. 4/26/29; EDPB Guidelines 01/2022; § 87 Abs. 1 Nr. 6 BetrVG.
Abschnitt 3 (Freigabe): Hinweis, dass neue KI-Tools ggf. Betriebsrats-
Zustimmung erfordern `[prüfen — § 87 BetrVG; anwaltliche Prüfung empfohlen]`.

## Risiken und typische Fehler

- Richtliniensprache erfinden: jede materielle Regel aus einer Quelle
  belegen oder `[prüfen — adaptiert, keine Direktquelle]` kennzeichnen.
- Schwierige Entscheidungen vorwegnehmen: das ist ein `[prüfen]`, keine
  empfohlene Position.
- § 87 BetrVG vergessen: bei Unternehmen mit Betriebsrat immer prüfen.
- Scope-Gespräch überspringen: „einfach alles" ist die Hauptfehlerquelle.

## Quellenpflicht

- **AI Act Art. 4, 9, 26/29** — VO (EU) 2024/1689.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- **§ 87 Abs. 1 Nr. 6 BetrVG** bei Mitarbeiter-KI.
- **GeschGehG §§ 2, 4** bei Abschnitt zu vertraulichen Daten.
- **EuGH C-634/21 (Schufa-Score)** beim Abschnitt zu automatisierten
  Entscheidungen.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 4.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22.**
- **Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 87 BetrVG Rn. 32 ff.**
