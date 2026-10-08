---
name: vergaberechtliche-pruefung-anwaltlich
description: "Führt die vergaberechtliche Vollprüfung ausschließlich aus Sicht der Vergabestelle. Einsetzen vor Verfahrensfreigabe vor Zuschlag bei Rüge oder Nachprüfung und vor Vertragsänderung. Prüft Regime Bedarf Verfahren Unterlagen Eignung Nachforderung Wertung Niedrigpreis Rechtsschutz und Vergabeakte. Liefert Freigabeampel Entscheidungsvermerk Maßnahmenliste und verteidigungsfähiges Aktenpaket."
---

# Vergaberechtliche Vollprüfung der Vergabestelle

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Auftrag und Stopplogik

Prüfe die konkrete Vergabe ausschließlich aus Sicht der Vergabestelle. Ziel ist
nicht ein abstraktes Gutachten, sondern eine freigabefähige Entscheidung mit
reproduzierbarer Akte. Stoppe die Freigabe, sobald Regime, Frist, veröffentlichter
Maßstab, Aktenbeleg oder Rechtsfolge offen sind.

Beginne mit einer Ampel:

| Gate | Grün | Gelb | Rot |
|---|---|---|---|
| Regime | Auftraggeber, Gegenstand, Wert und Stichtag belegt | Einzelangabe offen | falsches oder ungeklärtes Regime |
| Unterlagen | vollständig, widerspruchsfrei, zugänglich | heilbare Unklarheit | wettbewerbsbeschränkende oder nicht veröffentlichte Vorgabe |
| Wertung | Maßstab veröffentlicht und reproduzierbar | Begründung ergänzen | neuer Maßstab oder Ergebnissteuerung |
| Rechtsschutz | Fristen und Anträge kontrolliert | Rückfrage/Aktenlücke | drohender Zuschlag trotz Sperre |

## 1. Intake und Quelleninventar

Erfasse zuerst:

1. Auftraggeber, Bedarfsträger, Vergabestelle und Freigabeverantwortliche.
2. Bekanntmachung, Vergabeunterlagen, Nachsendungen, Bieterfragen und Portalstand.
3. Auftragswertschätzung, Lose, Optionen, Laufzeit und Schwellenwertquelle.
4. Angebote, Eignungsunterlagen, Öffnungsprotokoll, Aufklärungen und Wertungsstände.
5. Rügen, §-134-Informationen, Zustellbelege, VK-/OLG-Unterlagen und Vertrag.
6. Bei Systemdaten: Quellsystem, Originalschlüssel, Einheit, Version, Hash, Transformation und Zielsystem.

Fehlende Dokumente als konkrete Anforderung mit Verantwortlichkeit und Termin
ausgeben. Sichtbare Daten nicht erneut erfragen.

## 2. Gate Regime und Übergangsrecht

Prüfe in dieser Reihenfolge:

1. Auftraggebereigenschaft nach §§ 98 bis 101 GWB oder Unterschwellenbindung.
2. Liefer-, Dienst-, Bau-, freiberufliche, Sektoren-, Konzessions- oder VS-Leistung.
3. Schätzung nach § 3 VgV beziehungsweise Spezialregime: Optionen, Lose, Laufzeit, keine künstliche Aufteilung.
4. EU-Schwelle nach § 106 GWB und aktueller EU-Verordnung; unterhalb Haushalts- und Landesrecht.
5. Beginn des Vergabeverfahrens. Vor Anwendung geänderter Rechtsschutzregeln § 187 Abs. 2 GWB vorschalten: Vor dem 1. Juli 2026 begonnene Verfahren und ihre anschließende Nachprüfung bleiben im alten Recht.

Output: ein Regimevermerk mit Norm, Stichtag, Beleg und zuständigem Rechtsweg.

## 3. Gate Bedarf, Markt und Verfahren

1. Bedarf funktional, mengen- und termingerecht beschreiben; Lösung nicht vorwegnehmen.
2. Markterkundung nach § 28 VgV von einer bloßen Preisermittlung zur Vorbereitung der Unterlagen trennen.
3. Losbildung und Ausnahme nach § 97a GWB mit Markt-, Schnittstellen- und Steuerungsbelegen dokumentieren.
4. Nach § 119 Abs. 2 GWB stehen offenes und nichtoffenes Verfahren mit Teilnahmewettbewerb nach Wahl zur Verfügung. Andere Verfahrensarten brauchen ihren Tatbestand.
5. Ausnahmen des § 14 Abs. 4 VgV tatsachenbezogen belegen; selbst geschaffene Exklusivität oder Dringlichkeit nicht als Leerformel verwenden.

Bei einem ab 1. Juli 2026 begonnenen dringlichen Verhandlungsverfahren ohne
Teilnahmewettbewerb nach § 14 Abs. 4 Nr. 3 VgV die Ausnahme des § 17 Abs. 15 VgV
von §§ 53 Abs. 1, 54 und 55 VgV gesondert prüfen. § 187 Abs. 2 GWB bleibt
vorgeschaltet.

## 4. Gate Leistungsbeschreibung und Bekanntmachung

1. § 121 Abs. 1 GWB und § 31 VgV: möglichst eindeutige, gleich verständliche und vergleichbare Beschreibung.
2. Typ-, Marken-, Material-, Format- oder Systembezug auf funktionale Notwendigkeit und Gleichwertigkeit prüfen. Sof Medica, EuGH C-568/24, und DYKA Plastics, EuGH C-424/23, nur mit der tragenden Aussage und verifizierter Quelle einsetzen.
3. Bestandskompatibilität mit Bestand, Schnittstelle, Migration, Sicherheit und Gewährleistung belegen; OLG Düsseldorf Verg 2/24 als fallbezogenen Prüfanker verwenden.
4. Eignungsanforderungen, Zuschlagskriterien, Gewichtung, Nachweise, Fristen und Form in Bekanntmachung und Unterlagen widerspruchsfrei halten.
5. Berichtigung, Fristverlängerung und erneuten Upload als zusammenhängenden Vorgang dokumentieren.

Output: Widerspruchsmatrix `Fundstelle -> Risiko -> Korrektur -> Veröffentlichung -> Fristfolge`.

## 5. Gate Eignung, Ausschluss und Nachforderung

1. Eignung nach § 122 GWB und §§ 42 bis 48 VgV: Auftragsbezug, Verhältnismäßigkeit, bekannt gemachter Nachweis.
2. Zwingende und fakultative Ausschlussgründe nach §§ 123 und 124 GWB getrennt subsumieren; Selbstreinigung nach § 125 GWB eigenständig prüfen.
3. Bietergemeinschaft, Eignungsleihe und Nachunternehmen nach tatsächlicher Leistungszuordnung prüfen.
4. § 56 Abs. 2 und 3 VgV unterscheiden: unternehmensbezogene Unterlagen, leistungsbezogene Unterlagen, unwesentliche Einzelpreispositionen und Verbot materieller Angebotsänderung.
5. Eine einheitliche Nachforderungsentscheidung und Frist dokumentieren; keine selektive Heilung.

Nicht form- oder fristgerecht eingegangene Angebote sind nach § 57 Abs. 1 Nr. 1 VgV
auszuschließen, es sei denn, der Bieter hat den Mangel nicht zu vertreten.
Ursache, Portalprotokoll, Verantwortungsbereich und Kausalität vor
der Rechtsfolge feststellen. Nachgereichte Unterlagen nicht mit einem
verspäteten Angebot gleichsetzen; ihre Zulässigkeit richtet sich nach § 56 VgV.

## 6. Gate Bestangebot und Preisaufklärung

1. Zuschlag nach § 127 GWB und § 58 VgV auf das wirtschaftlichste Angebot, nicht automatisch auf den niedrigsten Preis.
2. Jedes Qualitäts-, Zeit-, Organisations-, Lebenszyklus- oder Servicekriterium mit Auftragsbezug, Nachweis und vorab festgelegter Wertungsmethode verbinden.
3. SIAC Construction, EuGH C-19/00, als Anker für Transparenz und objektive Kriterien nutzen; keine nachträglichen Unterkriterien bilden.
4. Einzelwertung aus Angebotsfundstelle, Tatsachenfeststellung, Maßstab, Begründung und Punkten reproduzierbar machen.
5. Ungewöhnlich niedrige Angebote nach § 60 VgV aufklären. BGH X ZB 10/16 trägt Anlass, Aufklärung und Geheimnisschutz, aber keine starre gesetzliche Prozentgrenze.

Output: Wertungsmatrix plus Entscheidungsbrücke für jedes streitige Kriterium.

## 7. Gate Vorabinformation, Rüge und Nachprüfung

1. § 134 GWB: Adressaten, Gründe, vorgesehener Zuschlagsempfänger, frühester Vertragsschluss, Versandweg und Frist prüfen.
2. § 160 Abs. 3 Satz 1 Nr. 1 bis 5 GWB je Verstoß getrennt prüfen; Nichtabhilfezugang und 15-Kalendertage-Frist sichern.
3. Rügeentscheidung als `Vorwurf -> Fundstelle -> Norm -> Aktenbefund -> Abhilfe/Nichtabhilfe -> Folgeschritt` ausgeben.
4. Bei VK-Antrag § 160 Abs. 2 GWB, Zuständigkeit, Zuschlagssperre, Aktenvorlage, Beiladung und Geheimnisschutz prüfen.
5. Für Neuverfahren endet das Zuschlagsverbot nach § 169 Abs. 1 GWB bei Obsiegen des Auftraggebers bereits mit Bekanntgabe der VK-Entscheidung. Für Altverfahren gilt § 187 Abs. 2 GWB.
6. Nach Ablehnung hat die sofortige Beschwerde im neuen Recht nach § 173 Abs. 1 GWB keine aufschiebende Wirkung; Eil- und Zuschlagsstrategie deshalb ausdrücklich behandeln.

Output: Fristenampel, Rügeerwiderung oder VK-Stellungnahme mit Anträgen,
Sachverhalt, Rechtsprüfung, Beweisangebot, Schwärzungsmatrix und Anlagenliste.

## 8. Gate Vertrag und Änderung

1. Zuschlag, Vertragsinhalt und Rangfolge gegen das bezuschlagte Angebot prüfen.
2. Änderung nach § 132 Abs. 1 bis 3 GWB klassifizieren; Wert, Laufzeit und kumulierte Änderungen berechnen.
3. Auftragnehmerwechsel nach § 132 Abs. 2 Satz 1 Nr. 4 Buchstabe b GWB auf Umstrukturierung, Eignung, weitere wesentliche Änderung und Umgehung prüfen.
4. Strominator, EuGH C-820/24, nur verwenden, wenn Leistung, endgültige Abnahme und Schlussrechnung für die Frage des noch laufenden Auftrags belegt sind.
5. Bekanntmachungspflicht nach § 132 Abs. 5 GWB und gegebenenfalls Neu- oder Interimsvergabe getrennt entscheiden.

## 9. Rechtsprechungs- und Quellenkontrolle

Rechtsprechung nur mit Gericht, Entscheidungsart, Datum, Aktenzeichen, ECLI
soweit vorhanden, Quelle und tragender Aussage verwenden. Schlussanträge nicht
als Urteil bezeichnen. Vergabekammerentscheidungen als Praxisanker, nicht als
höchstrichterliche Bindung darstellen. Primärquellen und die plugininternen
Referenzen zur Quellenhygiene vor jeder tragenden Verwendung prüfen.

## 10. Pflichtoutput

Liefere in dieser Reihenfolge:

1. Managemententscheidung in höchstens zehn Sätzen.
2. Ampel je Gate mit Stop-/Freigabeentscheidung.
3. Fristen- und Verantwortlichkeitsliste.
4. Vollständige Prüfmatrix `Tatsache -> Norm -> Subsumtion -> Beleg -> Gegenargument -> Rechtsfolge`.
5. Das benötigte Arbeitsprodukt vollständig.
6. Offene Punkte mit Dokumentanforderung und Termin.
7. Vier-Augen-Freigabe und nächster Portal-, DMS- oder Übergabeschritt.
