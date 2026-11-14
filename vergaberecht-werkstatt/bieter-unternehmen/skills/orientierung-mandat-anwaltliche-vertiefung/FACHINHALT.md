---
name: orientierung-mandat-anwaltliche-vertiefung
description: 'Vertieft eine bereits inventarisierte Bieterakte anwaltlich: bestimmt Regime, Abgabe- und Rügefristen, Formrisiken, Eignung, Qualitätsstrategie, Rechtsschutzweg, Beleglücken und Arbeitsoutput. Nicht für rohe Ordner oder ZIP-Dateien; dort startet der Master-Orchestrator.'
---

# Bieter: Vergabeakte, Fristen und nächsten Schritt bestimmen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Auftrag

Dieser Skill folgt auf eine dokumentierte Erstinventur durch den Master-Orchestrator. Er ist nicht der Einstieg für rohe Ordner oder ZIP-Dateien. Arbeite aus Sicht des Bewerbers oder Bieters. Bestimme zuerst das nächste irreversible Ereignis und sichere die dazugehörige Frist. Danach entscheide zwischen Bieterfrage, Angebotsarbeit, Rüge, Nachprüfung, Beschwerde oder Schadenssicherung. Sichtbare Unterlagen werden ausgewertet und nicht erneut abgefragt.

## Intake

1. Bekanntmachung, Vergabeunterlagen, Nachsendungen und Bieterkommunikation mit Versionen.
2. Teilnahme-, Angebots-, Bindefrist und Portalzeitzone.
3. Datum und Nachweis der Kenntnis jedes möglichen Verstoßes.
4. Eigene Eignung, Bietergemeinschaft, Eignungsleihe und Nachunternehmen.
5. Preisblatt, LV, Qualitätskonzept, Erklärungen, Signatur- und Rückgabeformat.
6. §-134-Information, Nichtabhilfe, VK- oder OLG-Zustellung.
7. Ziel: zuschlagsfähiges Angebot, Berichtigung, neue Wertung, Zuschlagsstopp, Vertragschance oder Kostenersatz.

## Regime und Fristweiche

| Ereignis | Rechtsanker | Sofortmaßnahme |
|---|---|---|
| Unterlagen erhalten | §§ 103 bis 106 GWB, § 3 VgV, Spezialregime | Auftrag, Wert, Regime und zuständige Stelle bestimmen |
| erkennbarer Bekanntmachungsfehler | § 160 Abs. 3 Satz 1 Nr. 2 GWB | vor Ablauf der benannten Bewerbungs- oder Angebotsfrist rügen |
| erkennbarer Unterlagenfehler | § 160 Abs. 3 Satz 1 Nr. 3 GWB | vor Ablauf der benannten Bewerbungs- oder Angebotsfrist rügen |
| Verstoß tatsächlich erkannt | § 160 Abs. 3 Satz 1 Nr. 1 GWB | zehn Kalendertage ab Kenntnis kontrollieren |
| Nichtabhilfe zugegangen | § 160 Abs. 3 Satz 1 Nr. 4 GWB | 15 Kalendertage bis Eingang des Nachprüfungsantrags kontrollieren |
| §-134-Information | § 134 GWB | 10 beziehungsweise 15 Kalendertage und Zuschlagsrisiko berechnen |
| VK-Entscheidung | §§ 171 bis 173, 187 Abs. 2 GWB | Normfassung, Zwei-Wochen-Frist und Suspensiveffekt bestimmen |

Für ein ab 1. Juli 2026 begonnenes Verfahren § 160 Abs. 3 Satz 1 Nr. 5 GWB als Missbrauchsschranke prüfen; sie ist keine zusätzliche Rügefrist. Altverfahren bleiben nach § 187 Abs. 2 GWB im alten Recht.

## Angebots- und Angriffsprüfung

1. Mussanforderung, Eignungskriterium, Zuschlagskriterium und Vertragsbedingung strikt trennen.
2. Jede Eignungsanforderung nach § 122 GWB mit eigenem Nachweis und Fundstelle schließen.
3. Qualitätsmehrwert nach § 127 GWB und § 58 VgV als Kette darstellen: `Kriterium -> Angebotsaussage -> Anlage -> messbarer Vorteil -> Punktwirkung`.
4. Vor Abgabe Dateiname, Format, LV-Rückgabe, Signatur, Preisblatt, Anlagenvollständigkeit und Portalquittung getrennt prüfen.
5. Eine Rüge mit Vergabeverstoß, Norm, Fundstelle, eigener Rechtsverletzung, drohendem Schaden, Beleg und konkreter Abhilfe formulieren.
6. Keine Tatsachen aus bloßem Verdacht behaupten; Indiz, offene Tatsache und Beweisantrag kennzeichnen.

## Qualitätsangebot statt Preisfalle

Ein höherer Preis ist kein Ausschlussgrund. Zeige, wie Geschwindigkeit, Verfügbarkeit, Personal, Methodik, Lebenszykluskosten, Service, Nachhaltigkeit oder Resilienz die veröffentlichten Kriterien besser erfüllen. Sind Kriterien unbestimmt, nachträglich verändert oder tatsächlich nur der niedrigste Preis gewertet worden, Rüge- und Nachprüfungsbedarf gesondert prüfen.

Rechtsprechungsanker:

- EuGH, Urteil vom 18.10.2001, C-19/00, *SIAC Construction*: objektive und transparente Wertung.
- BGH, Beschluss vom 31.01.2017, X ZB 10/16: strukturierte Aufklärung bei ungewöhnlich niedrigem Angebot; keine starre gesetzliche Prozentgrenze.
- OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24: pauschale Bestandskompatibilität mit einer belastbaren Anschluss-, Migrations- und Sicherheitsalternative angreifen.

## Routing

| Befund | nächster Skill | erster Output |
|---|---|---|
| Bekanntmachung unklar | `01-bekanntmachung-lesen` | Fristen- und Anforderungsmatrix |
| Unterlagen widersprüchlich | `02-vergabeunterlagen-pruefen` | Fundstellen- und Bieterfragenliste |
| Qualitätsvorsprung darzustellen | `qualitaetsvorsprung-nachweisen` | kriterienbezogenes Qualitätskonzept |
| Abgabe vorzubereiten | `15-formgerechte-abgabe-esignatur` | Portal- und Formatcheck |
| Rügefrist läuft | `20-ruegefrist-10-tage-paragraf-160` | belastbare Fristenberechnung |
| Rüge zu senden | `21-ruegeschreiben-erstellen` | vollständige Rüge mit Abhilfeantrag |
| Nichtabhilfe eingegangen | `23-nachpruefungsantrag-paragraf-160` | Nachprüfungsantrag und Anlagenplan |
| VK-Entscheidung liegt vor | `25-sofortige-beschwerde-olg-paragraf-171` | Beschwerde- und Eilstrategie |

## Pflichtoutput

1. Regime, Verfahrensstand und nächstes irreversibles Ereignis.
2. Fristenampel mit Ereignis, Zugang, Norm, Berechnung, Beleg und Verantwortlichem.
3. Angebots- oder Angriffsampel je Streitpunkt.
4. Lückenliste `Dokument -> Beweisthema -> Beschaffungsweg -> Termin`.
5. Genau ein vollständig formulierter nächster Bieteroutput.
6. Quellenstatus und Versand-/Uploadnachweis.
