---
name: zirkelschluss-pruefen
description: "Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte Zirkel A verweist auf A indirekte Zirkel A verweist B B verweist C C verweist A..."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bestimmtheitsgebot) — §§ 1-5 HdR (Normenklarheit, Verweisungs-Regeln) — § 307 BGB (Analogie: Zirkelschluss als Klarheits-Verstoß) — §§ 133, 157 BGB (Auslegungsgrundsaetze bei zirkulaeren Formulierungen)

## Ausgabe

Verweisgraf, Liste detektierter Schleifen, Vorschläge zur Entzerrung.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Anschluss

`referentenentwurf-bauen`, dann `begruendung-allgemein-und-besonders`.
