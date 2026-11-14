---
name: 07-vergabeunterlagen-erstellen
description: "Vollständigen Satz Vergabeunterlagen mit LV, GAEB/XML/Excel/PDF, Preisblättern, Bewerbungsbedingungen, ESPD, Bewertungsmatrix und Anlagen erstellen. Diskriminierungsfreie Bereitstellung, Roundtrip und Bieterabfrage. Output Unterlagenpaket und Nachweis."
---

# Vergabeunterlagen erstellen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Rechtsgrundlage

§ 29 VgV (Vergabeunterlagen und Zahlung), § 41 VgV (Bereitstellung), § 21 UVgO. Für vor dem 1. Juli 2026 begonnene Verfahren gilt nach § 187 Abs. 2 GWB die alte Fassung fort.

## Pflichtschritte

1. Bewerbungsbedingungen (Verfahrensregeln Fristen)
2. Leistungsbeschreibung (siehe Skill 08)
3. Vertragsentwurf
4. Eignungsformular ESPD (siehe Skill 09)
5. Bewertungsmatrix (siehe Skill 10)
6. Anlagen (Pläne technische Spezifikationen)
7. Bereitstellungsweg (e-Vergabe-Portal)
8. Datenformate, Rückgabeformat und Lesefassungen festlegen
9. Roundtrip aus Bietersicht prüfen
10. Bei Bestands-, Plan-, BIM-, Kosten-, Zustands-, Umwelt- oder Genehmigungsdaten `wirklichkeitsdaten-beschaffung-steuern` nutzen: Mengen, Schnittstellen, Normen, Risiken, Nachtragsursachen und Qualitätskriterien aus der Datenlage ableiten.
11. Für Neuverfahren Zahlungsregel nach § 29 Abs. 3 VgV abbilden: Zahlung nach Leistung, in der Regel binnen 30 Tagen nach Eingang der prüfbaren Rechnung; frühere Zahlung, Abschlag oder Vorauszahlung in geeigneten Fällen innerhalb des Haushaltsrechts prüfen.

## Anker-Rechtsprechung

- EuGH C-336/12 'Manova' zur Heilung von Unterlagen
- OLG Düsseldorf, Beschluss vom 13.05.2019, Verg 47/18: Vergabeunterlagen einschließlich technischer Anlagen vollständig und direkt elektronisch zugänglich machen; sonstige Unklarheiten eigenständig an §§ 121 GWB und 31 VgV prüfen.

## Output

Aktenstruktur als Verzeichnis. Fehlende Anlagen markiert UNVOLLSTÄNDIG.

## Format-Workflow

Bei LV, Preisblatt, GAEB, XML, Excel, PDF oder ZIP `vergabeunterlagen-lv-datenformate-bereitstellen` nutzen. Ziel: Bieter können Unterlagen auslesen, Preise eintragen und im verlangten Format liefern, ohne Strukturbruch oder Portalüberraschung.

## Datenbasierte Unterlagen

Wenn Unterlagen aus Bauwerksregistern, PMS/BMS, Bestandsplänen, BIM-Modellen, Nachträgen, Prüfberichten, Klima-/Umweltdaten, Normen oder früheren Vergaben gespeist werden, immer eine Wirkungszeile bilden: Quelle, Befund, LV-Folge, Kriterium, Risiko, Freigabe. Keine technische Quelle ungeprüft in eine Mindestanforderung oder ein Zuschlagskriterium verwandeln.
