---
name: fachanwalt-urheber-medienrecht-tdm-44b-urhg-ki-training-opt-out
description: "Text- und Data-Mining-Ausnahme § 44b UrhG bei Training von KI-Modellen. Maschinenlesbares Opt-out durch Rechteinhaber Art. 4 Abs. 3 DSM-RL. LG Hamburg LAION-Urteil 9.10.2024 (310 O 227/23) — Trainings-Daten verwertet bis Opt-out. Vergleich USA Fair Use Doctrine. Schreibvorlage Robots.txt TDM Reservation Notice Beweisaufnahme."
---

# TDM § 44b UrhG bei KI-Training — Opt-out

## Zweck

Spezial-Mandat: Mandant (Verlag, Fotograf, Urheber, Newsmedien) findet, dass sein Werk für das Training eines kommerziellen KI-Modells (ChatGPT, LAION, Stable Diffusion etc.) ohne Erlaubnis verwendet wurde. Anwaltliche Verteidigung über § 44b UrhG (TDM-Ausnahme) und maschinenlesbares Opt-out nach Art. 4 Abs. 3 DSM-RL (EU 2019/790).

## Eingaben

- Werk-Typ (Text, Bild, Musik, Video, Datenbank)
- Verwendung im KI-Modell (Training, Output, RAG)
- KI-Anbieter (OpenAI, Anthropic, Stability AI, LAION, Mistral)
- Bestehendes Opt-out (Robots.txt, TDM Reservation Notice, AGB)
- Datum der Trainings-Daten-Erhebung
- Beweisbarkeit der Verwendung (Modell-Output, Wasserzeichen-Detektion)

## Rechtlicher Rahmen

- **§ 44b UrhG** — Text- und Data-Mining-Erlaubnis (umgesetzt aus Art. 4 DSM-RL)
- **§ 44b Abs. 3 UrhG** — Vorbehalts-Möglichkeit Rechteinhaber: "in maschinenlesbarer Form"
- **§ 60d UrhG** — TDM für wissenschaftliche Forschung (Sonderfall)
- **Art. 4 DSM-RL 2019/790** — Vorlage für § 44b UrhG
- **§ 97 UrhG** — Unterlassungsanspruch
- **§ 97a UrhG** — Abmahnung
- **§ 53 KI-VO 2024/1689** — Pflichten Anbieter General-Purpose-AI (Training-Daten-Transparenz)

### Leitentscheidungen

- LG Hamburg, Urt. v. 9.10.2024 — **310 O 227/23** "LAION" (TDM für Forschung greift; kommerzielle Lizenz separat zu prüfen)
- OLG Köln, Urt. v. 14.6.2024 — 6 U 156/23 (TDM Reservation Notice Anforderungen)
- BGH-anhängig zu KI-Training und § 44b UrhG (2025)
- US-Federal Court NY-District (Thomson Reuters vs. Ross Intelligence 2025) — Fair Use abgelehnt

## Drei-Stufen-Analyse

### Stufe 1 — Greift § 44b Abs. 1 UrhG?

- TDM = automatisierte Analyse mit Daten-Reproduktion
- KI-Training fällt typischerweise unter TDM (umstritten)
- Voraussetzung: rechtmäßiger Zugang zum Werk
- Ausnahme: nicht-wissenschaftlich = § 44b (allgemein)

### Stufe 2 — Opt-out / Vorbehalt § 44b Abs. 3 UrhG

- Maschinenlesbar (Robots.txt, TDM Reservation Notice, Meta-Tag)
- Vor Trainings-Datenerhebung wirksam
- Konkret: "No-AI", "noai", "noimageai"
- HTML-Meta-Tag: `<meta name="robots" content="noai">`

### Stufe 3 — Bei Verstoß — Rechtsfolgen

- § 97 UrhG Unterlassung
- § 97 Abs. 2 Schadensersatz (Lizenzanalogie)
- § 97a Abmahnung (Anwaltskosten)
- § 101 UrhG Auskunftsanspruch (über Trainings-Daten)

## Workflow

### Phase 1 — Beweis-Erhebung

- KI-Output testen mit eigenem Werk-Inhalt
- Wasserzeichen / unique Marker im Werk
- Trainings-Daten-Listen prüfen (LAION-5B, Common Crawl, Books3)
- Forensische KI-Analyse-Dienstleister (Patronus, Adversa)

### Phase 2 — Opt-out-Status klären

- Webseite-Stand zum Trainings-Zeitpunkt (Wayback Machine)
- Robots.txt-Historie
- AGB-Recherche
- Bei fehlendem Opt-out: pre-Opt-out-Training-Datum prüfen

### Phase 3 — Abmahnung § 97a UrhG

- Strafbewehrte Unterlassungserklärung verlangen
- Auskunftsanspruch über Umfang der Verwendung
- Schadensersatz-Berechnung (Lizenzanalogie)
- Fristsetzung 14 Tage

### Phase 4 — Verfahren

- Bei Verweigerung: einstweilige Verfügung § 935 ZPO oder Klage
- Mandanten-Sammelaktion möglich (mehrere Urheber gegen KI-Anbieter)
- Verband-Klagebefugnis bei VG-Wort, GEMA, VG Bild-Kunst

### Phase 5 — Vergleich / Lizenzierung

- Häufig: rückwirkende Lizenz + Kostenanteil
- KI-Anbieter führen "Opt-in"-Programme (z. B. OpenAI Media Manager)
- Anwaltliche Verhandlung über Lizenzhöhe (ca. 0,5 % bis 5 % des KI-Anbieter-Umsatzes pro Schöpferkreis)

## TDM Reservation Notice — Vorlage

```html
<!-- HTML Meta-Tag -->
<meta name="robots" content="noai, noimageai">
<meta name="googlebot" content="noai">

<!-- Robots.txt (Domain-Wide) -->
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Claude-Web
Disallow: /

User-agent: cohere-ai
Disallow: /

<!-- Werk-Einzelnachweis (z. B. EXIF) -->
TDM Reservation: § 44b Abs. 3 UrhG; Art. 4 Abs. 3 DSM-RL
Generative AI training prohibited.
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Kein Opt-out vor Training | § 44b Abs. 1 UrhG greift | Klärung Zeitachse | Opt-out vor Trainings-Datum |
| Opt-out nicht maschinenlesbar | Streit über "Wirksamkeit" | Standard-Format | klar HTML/Robots |
| US-anbieter mit Drittstaat-Sitz | Erschwerte Durchsetzung | EU-Filiale klagen | EU-Beklagte |
| Trainings-Daten-Geheimhaltung | § 101 UrhG-Auskunftsanspruch | Klage läuft | Anbieter-Transparenz |

## Querverweise

- `fachanwalt-urheber-medienrecht-orientierung` — Triage
- `fachanwalt-urheber-medienrecht-lizenzvertrag-verhandlung` — bei nachträglicher Lizenz
- `fachanwalt-gewerblicher-rechtsschutz-ki-vo-art-50-generative-ai-transparenz` — Output-Kennzeichnung
- `fachanwalt-it-recht-ki-vo-hochrisiko-konformitaetsbewertung` — bei KI-Anbieter

## Quellen und Updates

Stand: 05/2026. § 44b UrhG seit 7.6.2021. LG Hamburg 310 O 227/23 (LAION). KI-VO 2024/1689 (insb. Art. 53 Transparenz). BGH-Linie 2025/2026 erwartet. Bei BGH-Entscheidung dringend Update.
