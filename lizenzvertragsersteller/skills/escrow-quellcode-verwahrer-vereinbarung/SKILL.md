---
name: escrow-quellcode-verwahrer-vereinbarung
description: "Source-Code-Escrow-Vereinbarung: drei-Parteien-Vertrag Lizenzgeber - Lizenznehmer - Escrow-Agent; Hinterlegungsumfang; Release-Trigger (Insolvenz, Wartungsausfall); Aktualisierungspflicht; bekannte Escrow-Anbieter; insolvenzfeste Gestaltung."
---

# Escrow / Quellcode-Verwahrer-Vereinbarung

## Anwendungsfall

Lizenznehmer macht sich von der Software des Lizenzgebers abhaengig. Bei Ausfall des Lizenzgebers (Insolvenz, Geschäftsaufgabe) braucht der Lizenznehmer Zugriff auf Source Code, um den Betrieb fortzufuehren. Loesung: Drei-Parteien-Escrow-Vertrag.

## Drei-Parteien-Struktur

```
+---------------+            +---------------+
|  Lizenzgeber  | <--------> |  Lizenznehmer |
+---------------+            +---------------+
        |                            ^
        | Hinterlegung               | Release bei Trigger
        v                            |
        +-------- Escrow-Agent ------+
                  (Verwahrer)
```

## Hinterlegungsumfang

| Bestandteil | Inhalt |
|---|---|
| **Source Code** | Vollstaendiger lauffaehiger Quellcode (Git-Bundle mit Commit-Historie) |
| **Build-Anweisungen** | Wie wird aus Source Code ein Build erstellt? Konfigurationsdateien, Build-Scripts |
| **Dependencies-Liste** | OSS und proprietaere Abhaengigkeiten mit Versionen |
| **Dokumentation** | Architektur-Diagramme, API-Docs, Datenbank-Schema |
| **Schlüssel/Credentials** | (falls für Build noetig) |
| **Test-Suiten** | Automatisierte Tests + Erwartete Ergebnisse |

## Release-Trigger

| Trigger | Definition |
|---|---|
| **Insolvenz Lizenzgeber** | Antrag auf Insolvenzeroeffnung; Geschäftseinstellung |
| **Wartungsausfall** | Nicht-Erfuellung der Wartungs-/Support-Pflicht waehrend > 90 Tagen |
| **Schwere Vertragsverletzung** | Z. B. Verletzung des Lizenzgegenstands oder Insolvenzanmeldung |
| **Verkauf Lizenzgeber** | Verkauf des IP an Dritten ohne Fortfuehrung Wartung |

## Anbieter (Beispiele, marktueblich)

- **Iron Mountain** (Marktfuehrer, USA + Europa)
- **NCC Group** (UK, mit Verification-Services)
- **Escrow Europe** (Niederlande)
- **Deutscher Anwalts-/Notarverwahrer** (kleine Vertragsvolumina)

## Aktualisierungspflicht

> "Der Lizenzgeber hinterlegt einen aktualisierten Source Code mindestens vierteljaehrlich. Bei wesentlichen Änderungen (neue Major-Version) Aktualisierung unverzueglich."

## Verification-Klausel

> "Der Lizenznehmer hat das Recht, einmal pro Jahr durch den Escrow-Agent eine technische Verifikation durchzufuehren: Build aus dem hinterlegten Code reproduzieren und mit der Lizenzversion vergleichen. Die Verifikationskosten traegt der Lizenznehmer."

## Insolvenzfeste Gestaltung

Damit der Verwalter den Escrow nicht "abwaehlen" kann ($ 103 InsO):

1. Source Code befindet sich **rechtlich beim Lizenznehmer** mit aufschiebender Bedingung
2. Hinterlegung beim Escrow-Agent dient nur der Realisierung
3. Trigger-Tatbestand "Insolvenz" als Release-Bedingung

Siehe vertiefend: `insolvenz-fortbestand-paragraf-103-inso-lizenz`.

## Klausel-Baustein

> **$ 14 Source-Code-Escrow.**
>
> (1) Der Lizenzgeber wird den vollstaendigen Source Code zur Lizenzsoftware nebst Build-Anweisungen, Dependencies-Liste, Architektur-Dokumentation und Test-Suite bei einem Escrow-Agent ("Verwahrer") hinterlegen. Verwahrer wird einvernehmlich von den Parteien innerhalb von 30 Tagen nach Vertragsunterzeichnung bestimmt.
>
> (2) Der Lizenzgeber aktualisiert die Hinterlegung mindestens vierteljaehrlich.
>
> (3) Der Verwahrer gibt die Hinterlegung an den Lizenznehmer heraus, wenn einer der folgenden Trigger eintritt: (a) Eroeffnung eines Insolvenzverfahrens über das Vermögen des Lizenzgebers; (b) Wartungsausfall über mehr als 90 zusammenhaengende Tage trotz schriftlicher Mahnung; (c) endgueltige Geschäftsaufgabe des Lizenzgebers.
>
> (4) Mit Herausgabe erwirbt der Lizenznehmer das Recht, den Source Code zu nutzen, zu modifizieren und zur Wartung der Lizenzsoftware einzusetzen. Eine Weitergabe an Dritte ist ausgeschlossen.
>
> (5) Die Kosten des Escrow traegt [der Lizenzgeber / der Lizenznehmer / die Parteien je zur Haelfte].

## Anschluss

- Insolvenzfestigkeit: `insolvenz-fortbestand-paragraf-103-inso-lizenz`
- Software-Lizenz: `lizenz-urheberrecht-und-software-urhg`
