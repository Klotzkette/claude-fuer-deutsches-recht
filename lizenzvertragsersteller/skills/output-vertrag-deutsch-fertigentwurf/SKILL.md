---
name: output-vertrag-deutsch-fertigentwurf
description: "Output: vollstaendiger Lizenzvertragsentwurf in deutscher Sprache. Praeambel; 19 Paragraphen; Anlagen A-E; Unterschriftenseite. Aus den Klausel-Bausteinen zusammengestellt; modular je nach IP-Typ und Konstellation."
---

# Output: Lizenzvertrag in deutscher Sprache

## Workflow

1. Eingangsdaten sammeln (Parteien, IP, Verguetungsmodell, Rechtswahl) - siehe Skills A-D.
2. Pro Klausel den passenden Baustein-Skill aufrufen.
3. Vertrag aus dem unten stehenden Geruest zusammensetzen.
4. Anlagen A-E aus den entsprechenden Skills einfuegen.
5. Prüfen mit Self-Test (unten).

## Vertragsgeruest

```
[Briefkopf Lizenzgeber / Lizenznehmer]

LIZENZVERTRAG ueber [IP-Typ]

zwischen

[Lizenzgeber], [Anschrift], vertreten durch [Vertreter]
- "Lizenzgeber" -

und

[Lizenznehmer], [Anschrift], vertreten durch [Vertreter]
- "Lizenznehmer" -

- gemeinsam "Parteien" -

PRAEAMBEL

(1) Der Lizenzgeber ist [allein/Mit-]inhaber der in Anlage A bezeichneten
    [Patente, Marken, Designs, Software, Know-how].
(2) Der Lizenznehmer beabsichtigt, [Beschreibung Geschaeftsmodell] und
    sucht hierfuer eine [Patent-, Marken-, Software-, Know-how-]Lizenz.
(3) Die Parteien haben am [Datum] eine Vertraulichkeitsvereinbarung
    geschlossen und Due Diligence durchgefuehrt.

Dies vorausgeschickt vereinbaren die Parteien:

$ 1 Definitionen
$ 2 Lizenzgegenstand                  -> Baustein 12
$ 3 Lizenzumfang                       -> Baustein 13
$ 4 Exklusivitaet                      -> Baustein 14
$ 5 Verguetung                         -> Baustein 15
$ 6 Sublizenzen                        -> Baustein 17
$ 7 Verbesserungen / Grant-Back        -> Baustein 18
$ 8 Garantien                          -> Baustein 19
$ 9 Haftungsbeschraenkungen            -> Baustein 19
$ 10 Mindestlizenz, Meldungen, Audit  -> Baustein 16
$ 11 Vertragsdauer                     -> Baustein 21
$ 12 Folgen der Vertragsbeendigung    -> Baustein 21
$ 13 Vertraulichkeit                   -> Baustein NDA
$ 14 Source-Code-Escrow (bei SW)       -> Baustein 22
$ 15 Rechtswahl und Streitbeilegung   -> Baustein 20
$ 16 Insolvenzfestigkeit               -> Baustein 23
$ 17 Exportkontrolle                   -> Baustein Compliance
$ 18 Datenschutz                       -> Baustein Compliance
$ 19 Steuern                           -> Baustein Compliance
$ 20 Schlussbestimmungen
    (1) Salvatorische Klausel
    (2) Schriftformerfordernis fuer Aenderungen (Textform mit ausdruecklichem
        Bezug)
    (3) Abtretungsverbot
    (4) Aufrechnungsverbot ausser unstreitiger oder rechtskraeftig festgestellter
        Gegenforderungen
    (5) Gesamtvertragsabrede ("Entire Agreement")
    (6) Anwendbares Recht / Schiedsklausel siehe $ 15

[Ort], den [Datum]

___________________________      ___________________________
Lizenzgeber                       Lizenznehmer

ANLAGEN
- Anlage A: IP-Liste (Lizenzgegenstand) -> Baustein 12
- Anlage B: Anwendungsfelder              -> Baustein 13
- Anlage C: Verguetungsmodell + Reporting -> Baustein 15+16
- Anlage D: AVV (DSGVO)                    -> Baustein DSGVO
- Anlage E: Sub-Lizenznehmer-Liste (falls)
```

## Prüfroutine vor Unterschrift

| Prüfpunkt | Prüfung |
|---|---|
| Parteien | HR-Auszug aktuell? Vertretungsbefugnis nachgewiesen? |
| Anlage A | Alle IP-Reg.-Nr. live verifiziert? |
| Vergütung | Bezugsgroessen definiert? Steuern beruecksichtigt? |
| Rechtswahl | Schiedsklausel klar? Sprache des Verfahrens? |
| Insolvenz | Escrow geregelt? Sicherungsabtretung? |
| Compliance | DSGVO-AVV unterschrieben? Sanktionsprueffung dokumentiert? |
| Anlage A bis E | alle beigefuegt? |

## Anschluss

- Englische Fassung: `output-vertrag-englisch-fertigentwurf`
- Bilingual: `output-zweisprachig-bilingual-deutsch-englisch`
