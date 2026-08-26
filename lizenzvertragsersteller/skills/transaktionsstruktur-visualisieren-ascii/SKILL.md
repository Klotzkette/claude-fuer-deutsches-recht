---
name: transaktionsstruktur-visualisieren-ascii
description: "Für Transaktionsstruktur visualisieren — ASCII: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Transaktionsstruktur visualisieren — ASCII

## Konstellation 1 — Einfache Lizenz

```
 +-----------------+        Lizenz (IP-Typ)         +-----------------+
 |  Lizenzgeber    | ---> Anlage A IP-Liste -----> |  Lizenznehmer   |
 |  (Licensor)     |                                |  (Licensee)     |
 |                 | <----- Royalty / Pauschale --- |                 |
 +-----------------+                                +-----------------+
```

## Konstellation 2 — Konzernlizenz

```
 +-----------+    Lizenz     +-----------+   Sub-Lizenz   +------------+
 | IP-Holding |--->|  Konzern- |--->| Konzern-   |
 |  GmbH      |              |  Mutter   |              |  Tochter   |
 +-----------+              +-----------+              +------------+
   (Lizenzgeber)            (Hauptlizenz-              (Sub-License,
                             nehmer)                   Definition Paragraf 15 AktG)
```

## Konstellation 3 — Cross-License (Patentaustausch)

```
 +-----------------+   Lizenz Patent A   +-----------------+
 |   Partei A     | -------------------> |   Partei B     |
 |                 | <------------------- |                 |
 +-----------------+   Lizenz Patent B   +-----------------+
   Cross-License, gegenseitig, optional mit Ausgleichszahlung
```

## Konstellation 4 — Lizenz mit Sicherheiten

```
                       +-------------------------+
                       |   Bank (Sicherheiten-   |
                       |   nehmer)               |
                       +-------------------------+
                                   ^
                                   | Sicherungsabtretung / Pfandrecht
                                   |
 +-----------------+        Lizenz                +-----------------+
 |  Lizenzgeber    | ---------------------------> |  Lizenznehmer   |
 |  (zugleich      |                              |                 |
 |   Sicherheits-  | <--- Royalty + Sicherheit -- |                 |
 |   geber)        |                              |                 |
 +-----------------+                              +-----------------+
```

## Konstellation 5 — Source-Code-Escrow

```
 +-----------------+        Lizenz Software       +-----------------+
 |  Lizenzgeber    | ---------------------------> |  Lizenznehmer   |
 +-----------------+                              +-----------------+
       |                                                 ^
       | Hinterlegung Source Code                        | Release bei
       v + Build-Anweisungen                             | Trigger:
 +-------------------+                                   | - Insolvenz LG
 |   Escrow Agent    | --- Release bei Trigger ----------+ - Wartungs-
 |   (Verwahrer)     |                                   |   ausfall
 +-------------------+                                   | - VertragsendeBruch
```

## Konstellation 6 — Patent Pool (FRAND)

```
                 +-------------------------+
                 |   Pool-Administrator    |
                 +-------------------------+
                     |        |        |
                   ----------       ----
            +-----+|+-----+ +-----+|+-----+
            | Pat |||| Pat ||| Pat ||| ... |
            | A   |||| B   ||| C   |||     |
            +-----+|+-----+ +-----+|+-----+
                     |        |
            FRAND-Lizenz an   Streitschlichtung
            Implementierer    + Kartellrecht
```

## Hinweise

- Pfeile sind Lizenz-/Geldflusse, gerichtet.
- Boxen sind Parteien mit Rolle.
- Sicherheiten/Pfandrechte gestrichelt (mit `^/v`).
- Insolvenz-Kette explizit beschriften.

## Anschluss

- Output-Modul: `output-vertrag-deutsch-fertigentwurf` (uebernimmt das Schema in die Praeambel)
- Bilingual: `output-zweisprachig-bilingual-deutsch-englisch`
