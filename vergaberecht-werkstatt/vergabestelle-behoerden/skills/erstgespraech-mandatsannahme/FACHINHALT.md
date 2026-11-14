---
name: erstgespraech-mandatsannahme
description: 'Internen Beratungsauftrag der Vergabestelle eröffnen: Bedarfsträger, Zuständigkeit, Beschaffungsziel, Aktenstand, Budget, Termine, Datenquellen, Interessenkonflikte, Freigaben, Rechtsschutzrisiko und ersten Vermerk festlegen.'
---

# Internen Beratungsauftrag der Vergabestelle eröffnen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Einsatzbereich

Der Verzeichnisname bleibt aus Kompatibilitätsgründen bestehen. Inhaltlich handelt es sich nicht um eine anwaltliche Mandatsannahme, sondern um den dokumentierten Start eines internen Beschaffungs-, Rüge- oder Rechtsschutzauftrags der Vergabestelle.

## Eingang aufnehmen

1. Auftraggeber, Vergabestelle, Bedarfsträger, Projektleitung, Haushalt, Datenschutz, Informationssicherheit und Freigabegremium benennen.
2. Vergabeakte und Fachakten getrennt inventarisieren; Portalprotokolle, Freigaben und Kommunikation unveränderbar sichern.
3. Beschaffungsgegenstand, Lose, Optionen, Laufzeit, Gesamtwert und Terminzwang erfassen.
4. Datenquellen mit Eigentümer, Stichtag, Qualität und erlaubter Nutzung kennzeichnen.
5. Beteiligte Berater, frühere Auftragnehmer und Marktteilnehmer auf Vorbefassung oder Interessenkonflikt prüfen.

## Auftragsklärung

### Beschaffungsziel

Beschreibe den messbaren Bedarf statt eines gewünschten Produkts. Lege fest, welche Wirkung das Angebot erreichen soll: Qualität, Geschwindigkeit, Verfügbarkeit, Lebenszykluskosten, Nachhaltigkeit, Resilienz oder Innovation. Der niedrigste Preis wird nicht als Standardziel vorausgesetzt.

### Verfahrensstand

| Stand | sofort zu sichern |
|---|---|
| vor Bekanntmachung | Vergabereife, Markterkundung, Verfahrenswahl, Fristen- und Freigabeplan |
| Angebotsphase | Bieterfragen, Änderungsbedarf, Gleichbehandlung, neue Frist und Portalversion |
| Wertung | unveränderter Maßstab, Aufklärung, Preisprüfung, Beleg- und Entscheidungsmatrix |
| Rüge | Eingang, Kenntnisvortrag, konkrete Beanstandung, Abhilfeoption und § 160-Uhr |
| VK | Unterrichtung nach § 169 GWB, Vergabeakte, Geheimnisse, Stellungnahme und Beiladung |
| OLG | Zustellung, Zwei-Wochen-Notfrist, gleichzeitige Begründung, § 173-Ausgang und § 176-Bedarf |

### Zuständigkeit und Integrität

Lege Bearbeiter, Entscheidungsträger, Vier-Augen-Prüfung und Befangenheitserklärungen fest. Ein möglicher Interessenkonflikt wird anhand § 6 VgV und der konkreten Einflussmöglichkeit geprüft; bloße organisatorische Nähe wird weder ignoriert noch automatisch als Ausschluss behandelt.

## Rechts- und Datenweichen

- Regime und Wertgrenze gelten zum maßgeblichen Beschaffungszeitpunkt und werden aus Primärquellen belegt.
- § 8 VgV steuert die Vergabedokumentation; Fachentscheidungen bleiben mit Quelle, Annahme und Freigabe nachvollziehbar.
- § 127 GWB und § 58 VgV ermöglichen das beste Preis-Leistungs-Verhältnis; Kriterien müssen bekannt gemacht, auftragsbezogen und überprüfbar sein.
- GAEB, XML, Excel, PDF, SAP- oder Fachverfahrensdaten werden nur über ein dokumentiertes Mapping mit Validierung und Rückexport übernommen.

## Verbindlicher Startvermerk

1. Auftrag, Zuständigkeit und Freigaben.
2. Bedarf und messbares Beschaffungsziel.
3. Verfahrensstand und nächster unumkehrbarer Termin.
4. Datenquellen- und Dokumentenmatrix.
5. Vergabereife- und Rechtsrisikoampel.
6. Qualitäts- und Wirtschaftlichkeitsziel.
7. Arbeitsplan mit Verantwortlichem, Frist und Output.

## Routing

- Bedarf und Realitätsdaten: `wirklichkeitsdaten-beschaffung-steuern`.
- Marktansprache und Vorbefassung: `markterkundung-und-vorbefassung`.
- Zuschlagsmodell: `zuschlagskriterien-paragraf-127-gwb`.
- Rüge: `vergaberueg-paragraf-160-gwb`.
- VK: `23-stellungnahme-vergabekammer`.
- OLG: `24-vorlage-an-den-vergabesenat`.

Keine Kanzleivollmacht, kein GwG- oder Honorarworkflow und keine arbeitsrechtlichen Vergleichsbegriffe erzeugen.
