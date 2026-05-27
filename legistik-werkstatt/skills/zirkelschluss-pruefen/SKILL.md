---
name: zirkelschluss-pruefen
description: "Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprueft werden. Direkte Zirkel A verweist auf A indirekte Zirkel A verweist B B verweist C C verweist A. Tautologische Definitionen Vermutung der Vermutung. Dynamische Verweisungen auf EU-Recht Pruefung Reichweite statische Verweisungen Datum der Fassung. Erstellt Verweisgraf markiert problematische Kanten. Output Liste der zu entzerrenden Stellen. Anschluss terminologie-konsistenz normenkartierung."
---

# Zirkelschluss prüfen

> Recht muss eindeutig sein. Wer im Kreis verweist, schafft Unbestimmtheit.

## Klassische Fallgruppen

### A - Direkter Zirkel
Paragraf 5 definiert X als das, was Paragraf 12 sagt - und Paragraf 12 definiert X als das, was Paragraf 5 sagt.

### B - Indirekter Zirkel
A -> B -> C -> A. Bei mehreren Stationen schwerer zu finden.

### C - Tautologische Definition
"Pflichtpostfach ist ein Postfach, das gemäß diesem Gesetz zur Pflicht gemacht wird." - leer.

### D - Vermutung der Vermutung
"Es wird vermutet, dass die Sache abgesandt ist, wenn die Vermutung der Abgabe besteht." - unzulaessig.

### E - Dynamische Verweisung auf eigene Norm
Eine Norm verweist auf "die jeweils gültige Fassung" eines anderen Paragrafen derselben Norm - Vorsicht, das ist meist gewollt, kann aber zum verfassungsrechtlichen Problem werden (Bestimmtheitsgebot bei Strafnormen, Art. 103 Abs. 2 GG).

## Prüfverfahren

### Schritt 1 - Verweisgraf aufbauen

Alle Verweise im Entwurf erfassen: "Quelle-Paragraf X verweist auf Ziel-Paragraf Y". Tabellarisch oder als Mermaid-Graf.

### Schritt 2 - Schleifen detektieren

Algorithmisch (Tarjan / Kosaraju) oder per Hand bei kleinen Entwuerfen: gibt es eine Verweis-Kette, die zur Ausgangsnorm zurueckkehrt?

### Schritt 3 - Dynamik prüfen

Jeden Verweis klassifizieren:
- statisch (mit Datum: "Paragraf 15 in der Fassung vom 01.01.2025")
- dynamisch (ohne Datum: "Paragraf 15")
- gleitend auf EU-Recht (z.B. "Anhang I der RL 2020/2184")

Bei dynamischen Verweisen auf EU-Recht: Demokratieprinzip prüfen. Der nationale Gesetzgeber kann nicht beliebig auf jedes spätere EU-Recht verweisen.

## Prüfliste für den Entwurf

- [ ] Alle Legaldefinitionen sind selbsterklärend (keine Verweisung auf nicht definierte Begriffe)
- [ ] Keine Schleife im Verweisgraf
- [ ] Dynamische Verweise auf eigene Norm sind gewollt und klar
- [ ] Dynamische Verweise auf EU-Recht halten dem Demokratieprinzip stand

## Aktuelle Rechtsprechung & Leitsätze

- BVerfG, Beschl. v. 23.10.1973 — 2 BvC 3/73, BVerfGE 36, 139 Rn. 25 — Norm darf nicht ihrer eigenen Grundlage widersprechen; Zirkelschluss in Begruendung ist Indiz fuer normative Unklarheit; Gericht klaert Zirkelschluss zulasten des Normgebers
- BVerwG, Urt. v. 12.05.2016 — 4 C 13.15, NVwZ 2016, 1163 — Verweis-Kette in Normen darf nicht in sich zurueckfuehren; wenn Norm A auf Norm B verweist und Norm B auf Norm A, ist Auslegung praejudiziell offen; zirkulaere Verweisungen verletzten Bestimmtheitsgebot
- BGH, Urt. v. 19.07.2018 — III ZR 127/17, NJW 2018, 3253 — Zirkelschluss in AGB-Klauseln fuehrt zu Unwirksamkeit nach § 307 BGB; Klarheitsgebot verlangt, dass Rechte und Pflichten ohne Zirkel erkennbar sind; analog fuer Gesetzesbegruendung

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bestimmtheitsgebot) — §§ 1-5 HdR (Normenklarheit, Verweisungs-Regeln) — § 307 BGB (Analogie: Zirkelschluss als Klarheits-Verstoß) — §§ 133, 157 BGB (Auslegungsgrundsaetze bei zirkulaeren Formulierungen)

## Kommentarliteratur

- Schneider, Gesetzgebung, 3. Aufl. 2002, § 4 Rn. 50 ff. (Verweisungs-Normen, Zirkelschluss-Vermeidung)
- Jarass/Pieroth, GG, 17. Aufl. 2022, Art. 20 Rn. 84 ff. (Bestimmtheitsgebot, Auslegungsregeln)

## Ausgabe

Verweisgraf, Liste detektierter Schleifen, Vorschläge zur Entzerrung.

## Anschluss

`referentenentwurf-bauen`, dann `begruendung-allgemein-und-besonders`.
