---
name: 10-leistungsverzeichnis-bepreisen
description: "Positionen des LV einzeln bepreisen und im verlangten Format liefern: GAEB, XML, Excel, PDF oder Portalformular. Vollständigkeit, Pflichtfelder, Roundtrip und keine Strukturveränderung. Output bepreistes LV plus Format- und Uploadcheck."
---

# Leistungsverzeichnis bepreisen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Rechtsgrundlage

§ 16 EU VOB/A, § 13 EU VOB/A.

## Pflichtschritte

1. Alle Pos-Nummern bepreist
2. Einheitspreise und Gesamtpreise
3. Bedarfspositionen markiert
4. Pauschalisierungen begründet
5. Anlagen unterschrieben
6. Format wie vorgegeben (GAEB XML usw)
7. Native Datei nur nach Format- und Roundtrip-Prüfung erzeugen

## Anker-Rechtsprechung

- BGH, Urteil vom 19.06.2018, X ZR 100/16, Uferstützmauer: Preisverlagerungen und spekulative Kalkulation können die geforderte Preisangabe verfehlen; jede LV-Position und ihre Kalkulationszuordnung deshalb unverändert und prüfbar halten.
- Rechtsprechung zu fehlenden Preisangaben nur nach Prüfung von Vergaberegime, konkreter Preisposition und amtlicher Fundstelle zitieren.

## Output

Bepreistes LV im Originalformat zur Abgabe.

## Format-Workflow

Bei GAEB, XML, Excel oder PDF zuerst die Datei mit `unterlagen-und-lv-datenformate-auslesen` normalisieren. Danach mit `angebot-in-vorgegebenem-format-erstellen` das verbindliche Abgabeformat bauen. Positionen, Ordnungszahlen, Mengen, Einheiten und Formeln nicht verändern.
