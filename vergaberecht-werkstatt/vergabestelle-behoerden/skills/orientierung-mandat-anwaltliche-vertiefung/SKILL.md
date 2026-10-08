---
name: orientierung-mandat-anwaltliche-vertiefung
description: 'Vertieft eine vom Master-Orchestrator bereits inventarisierte Vergabeakte: bestimmt Auftraggebertyp, Auftragsart, Wert, Rechtsregime, Übergangsrecht, Verfahrensstand, nächste Freigabe, Aktenlücken und Behördenoutput. Nicht für rohe Ordner oder ZIP-Dateien; dort startet der Master-Orchestrator.'
---

# Vergabestelle: Rechtsregime und nächste Freigabe bestimmen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Auftrag

Dieser Skill folgt auf eine dokumentierte Erstinventur durch den Master-Orchestrator. Er ist nicht der Einstieg für rohe Ordner oder ZIP-Dateien. Arbeite ausschließlich aus Sicht der Vergabestelle. Erzeuge keine allgemeine Rechtskunde, sondern entscheide, welches Regime gilt, welche Behördenentscheidung als Nächstes ansteht und welcher Aktenbeleg vor der Freigabe fehlt. Sichtbare Unterlagen werden ausgewertet und nicht erneut abgefragt.

## Eingangsdaten

Erfasse zuerst:

1. Auftraggeber, Bedarfsträger, Vergabestelle und Entscheidungskompetenz.
2. Liefer-, Dienst-, Bau-, freiberufliche, Sektoren-, Konzessions- oder VS-Leistung.
3. Auftragswert ohne Umsatzsteuer einschließlich Optionen, Laufzeit und Lose.
4. Verfahrensbeginn, Veröffentlichungsstand und nächster unumkehrbarer Termin.
5. Bekanntmachung, Vergabeunterlagen, Portalversionen, Freigaben und bisherige Kommunikation.
6. Qualitätsziel: Funktion, Ausführungszeit, Verfügbarkeit, Lebenszykluskosten, Nachhaltigkeit, Resilienz oder Innovation.
7. Datenquellen und Rückgabeformate einschließlich GAEB, XML, Excel, PDF, SAP oder Fachverfahren.

Unbekanntes bleibt als konkrete Lücke mit Verantwortlichem und Termin sichtbar.

## Regimeweiche

| Prüfschritt | Rechtsanker | Entscheidung |
|---|---|---|
| Auftraggeber | §§ 98 bis 101 GWB; bei Kooperation § 108 GWB | klassisch, Sektor, Konzession, VS oder nur haushaltsrechtlich gebunden |
| Gegenstand | §§ 103 bis 105 GWB | Auftragsart und Spezialregime |
| Wert | § 3 VgV oder Spezialregel | Gesamtwert, Loswert, Optionen und Laufzeit belegen |
| Schwelle | § 106 GWB und aktuelle EU-Verordnung | ober- oder unterschwellig; Landesrecht und Wertgrenze bei Unterschwelle live prüfen |
| Übergang | § 187 Abs. 2 GWB | vor dem 1. Juli 2026 begonnenes Altverfahren oder neues Recht |
| Verfahren | § 119 GWB, VgV, VOB/A, SektVO, KonzVgV oder UVgO | Regelverfahren oder belegbedürftiger Ausnahmetatbestand |

Bei Bauleistungen Abschnitt 1 und Abschnitt 2 VOB/A trennen. UVgO-Regeln nicht auf VOB/A- oder VgV-Fälle übertragen.

## Phasen- und Stopplogik

| Phase | nächste Entscheidung | Stoppsignal |
|---|---|---|
| Planung | Vergabereife und Verfahrenswahl | Bedarf, Wert, Budget oder Zuständigkeit ungeklärt |
| vor Bekanntmachung | Unterlagen- und Veröffentlichungsfreigabe | widersprüchliches LV, unmessbares Kriterium oder fehlende Fristberechnung |
| Angebotsphase | Bieterinformation, Berichtigung und Fristfolge | selektive Information oder nicht veröffentlichte Änderung |
| Wertung | Eignung, Aufklärung und Zuschlagsentscheidung | neuer Maßstab, unbelegte Punkte oder ungeklärter Niedrigpreis |
| §-134-Phase | Vorabinformation und Stillhaltefrist | unvollständige Gründe, Adressat oder Versandbeleg fehlt |
| Rüge/VK/OLG | Abhilfe, Verteidigung oder Rechtsmittel | Zuschlagssperre, Notfrist oder Aktenvorlage ungeklärt |
| Vertrag | Änderung oder Neuvergabe | § 132 GWB nicht subsumiert oder Auftrag bereits beendet |

## Materielle Kernkontrolle

1. Leistungsbeschreibung nach § 121 GWB und § 31 VgV beziehungsweise dem anwendbaren VOB/A-Regime verständlich, vergleichbar und wettbewerbsoffen gestalten.
2. Eignung nach § 122 GWB von Zuschlagskriterien nach § 127 GWB trennen.
3. Das wirtschaftlichste Angebot bestimmen. Preis darf allein entscheiden, ist aber kein gesetzlicher Automatismus. Qualitäts-, Zeit-, Service- und Lebenszykluskriterien mit Auftragsbezug, Nachweis, Gewichtung und vorab festgelegter Wertungsmethode verbinden.
4. Nachforderung nach § 56 VgV von einer unzulässigen materiellen Angebotsänderung abgrenzen.
5. Ungewöhnlich niedrige Angebote ausschließlich im Prüfweg des § 60 VgV aufklären.
6. Jede Wertung mit Angebotsfundstelle, Tatsachenfeststellung, Maßstab, Punkten, Begründung und Freigabe reproduzierbar machen.
7. Vergabeakte nach § 8 VgV fortschreiben; Quelle, Version, Bearbeiter, Zeitpunkt und Entscheidung festhalten.

## Rechtsprechungsanker

- EuGH, Urteil vom 18.10.2001, C-19/00, *SIAC Construction*: transparente, objektive und überprüfbare Zuschlagswertung.
- BGH, Beschluss vom 31.01.2017, X ZB 10/16: Anlass und Verfahren der Aufklärung ungewöhnlich niedriger Angebote; keine erfundene starre Prozentgrenze.
- OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24: Bestandskompatibilität nur mit konkreten Schnittstellen-, Migrations-, Sicherheits- und Gewährleistungsbelegen verwenden.
- EuGH, Urteil vom 04.06.2026, C-820/24, *Strominator Elektro*: § 132 GWB nicht auf einen vollständig erbrachten, endgültig abgenommenen und schlussgerechneten Auftrag stützen.

Vor tragender Verwendung Entscheidungsart, Datum, Aktenzeichen, Aussage und Quellenstatus nach `references/quellenhygiene.md` verifizieren.

## Routing

| Befund | nächster Skill | erster Output |
|---|---|---|
| Wert oder Regime offen | `03-schwellenwert-pruefung` | Schwellen- und Regimevermerk |
| Verfahrensart offen | `verfahrenswahl-kompass` | Tatbestands- und Freigabevermerk |
| Leistungsbeschreibung fehleranfällig | `leistungsbeschreibung-neutralitaet-funktional` | korrigiertes LV mit Abnahmekriterien |
| Bestangebot zu gestalten | `zuschlagskriterien-paragraf-127-gwb` | Preis-Qualitäts-Matrix |
| Rüge eingegangen | `22-ruegeerwiderung` | Abhilfeentscheidung und Antwort |
| VK-Verfahren | `23-stellungnahme-vergabekammer` | Anträge, Stellungnahme und Aktenpaket |
| OLG-Verfahren | `24-vorlage-an-den-vergabesenat` | Beschwerde- oder Erwiderungsbriefing |
| Vertragsänderung | `vertragsaenderung-132-gwb-change-control` | Änderungsklassifikation und Bekanntmachungsentscheidung |

## Pflichtoutput

1. Ein-Satz-Entscheidung zu Rolle, Regime und Verfahrensstand.
2. Fristenampel mit Ereignis, Zugang, Norm, Berechnung und Verantwortlichem.
3. Vergabereife-Ampel mit Stop-/Freigabeentscheidung.
4. Lückenliste `Dokument -> Beweisthema -> Beschaffungsweg -> Termin`.
5. Genau ein vollständig formulierter nächster Behördenoutput.
6. Quellenstatus und Vier-Augen-Freigabe.
