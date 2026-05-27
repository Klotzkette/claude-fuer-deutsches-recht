---
name: berufsrecht-ki-vertragspruefung-kaltstart-interview
description: "Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftspruefer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus den Norm-Adapter (BRAO StBerG WPO PAO BNotO) und entscheide ob Kanzleiinfrastruktur oder Einzelmandats-Tool im Sinne Absatz fuenf vorliegt. Lade dazu die Skill parallelnormen-andere-berufe."
---

# Kaltstart-Interview

## Disclaimer

Diese Forprüfung ist keine Rechtsberatung, sondern strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Zweck

Bevor die materielle Prüfung beginnt, brauchen wir saubere Eingangsdaten. Das Interview fixiert Beruf, Anbieter, Datenarten und Vertragstyp. Daraus leitet sich der Norm-Adapter ab — von ihm hängt jede weitere Skill ab.

## Pflichtfragen

### Beruf des Auftraggebers

Welche Berufsgruppe nutzt das Tool?

- Rechtsanwalt — Norm: § 43e BRAO i.V.m. § 43a Abs. 2 BRAO und § 203 Abs. 1 Nr. 3 StGB
- Steuerberater oder Steuerbevollmächtigter — Norm: § 62a StBerG i.V.m. § 57 Abs. 1 StBerG und § 203 Abs. 1 Nr. 3 StGB
- Wirtschaftsprüfer oder vereidigter Buchprüfer — Norm: § 50a WPO i.V.m. § 43 WPO und § 203 Abs. 1 Nr. 3 StGB (bei Wirtschaftsprüfungsgesellschaft zusätzlich § 59c WPO)
- Patentanwalt — Norm: § 39c PAO i.V.m. § 39a Abs. 2 PAO und § 203 Abs. 1 Nr. 3 StGB
- Notar — Norm: § 26a BNotO i.V.m. § 18 BNotO und § 203 Abs. 1 Nr. 1 StGB

Sind mehrere Berufsgruppen in einer Sozietät gemischt vertreten (Anwalts-Steuerberater-Gesellschaft, multidisziplinäre Praxis), gelten die strengsten Anforderungen kumulativ. Beim Notar besonders auf § 26a Abs. 4 BNotO achten — bei Dienstleistungen für ein einzelnes Amtsgeschäft ist die Einwilligung des Beteiligten erforderlich.

### Anbieter und Produkt

- Firmenname und Sitz des Anbieters (juristische Person, vertretungsberechtigte Personen)
- Produktname und Versionsstand (Bsp.: gängige KI-Sprachmodelle und KI-Frontends; eigene Marken-Frontends)
- Eigene KI-Modelle oder API-Aufruf an Drittanbieter (z.B. Microsoft Azure, AWS Bedrock)
- Welche Subunternehmer sind vorgesehen (Hyperscaler, Modellanbieter, Hosting)?

### Datenarten und Verarbeitungszweck

- Welche Datenkategorien werden eingegeben (Mandatsschriftsätze, Vertragsentwürfe, Personalakten, Bilanzdaten, Notariatsurkunden, Patentanmeldungen)?
- Werden besondere Kategorien personenbezogener Daten verarbeitet (Art. 9 DS-GVO)?
- Geht es um Kanzleiinfrastruktur (übergreifend) oder ein Tool, das einem konkreten Mandat dient (Abs. 5 der Dienstleisterregelung)?
- Wer im Haus hat Zugriff?

### Hostingland und Auslandsbezug

- Wo liegen die Server (EU/EWR, USA, sonstiges Drittland)?
- Wo sitzt der Modellanbieter selbst (etwa OpenAI in den USA)?
- Greift der US-CLOUD Act (US-Konzern oder US-Tochter)?

### Vertragsstand

- Liegt ein eigenständiger Vertrag vor, oder nur AGB plus Datenschutzanhang?
- Wann wurde der Vertrag zuletzt geändert?
- Wer hat unterzeichnet?
- Liegt eine Auftragsverarbeitungsvereinbarung nach Art. 28 DS-GVO bei?

## Heuristik Kanzleiinfrastruktur vs. Einzelmandats-Tool

Nach DAV-Stellungnahme 32/2025 (Seite 15) ist die Einwilligung des Mandanten oder Beteiligten regelmäßig nicht erforderlich, wenn das Tool als allgemeine Kanzleiinfrastruktur eingesetzt wird. Sie ist erforderlich, wenn das Tool unmittelbar einem einzelnen Mandat oder einem einzelnen Amtsgeschäft dient (Abs. 5 der jeweiligen Dienstleisterregelung).

Indikatoren für **Kanzleiinfrastruktur** (kein Einzelmandatsbezug, keine Einwilligung erforderlich):

- Mandant-unabhängige Recherche, Vorlagenerzeugung, allgemeine Vertragsanalyse, Wissensmanagement
- Verfügbarkeit für alle Mandate
- keine mandatsspezifische Konfiguration

Indikatoren für **Einzelmandats-Tool** (Einwilligung erforderlich):

- Spezielle Konfiguration für einen Mandanten
- Verarbeitung benannter Beteiligter
- Mandat-spezifische Trainingsdaten oder Embeddings
- Notariatsspezifisch: Tool dient einem konkreten Amtsgeschäft

Bei Unsicherheit: konservativ entscheiden und Einwilligung einholen.

## Output

Strukturierter Eingangsdatensatz im Markdown-Format:

```
## Eingangsdaten
- Beruf: ...
- Norm-Adapter: § ... 
- Anbieter: ...
- Produkt: ...
- Subunternehmer: ...
- Datenarten: ...
- Hostingland: ...
- Auslandsbezug: ...
- Vertragstyp: Kanzleiinfrastruktur / Einzelmandats-Tool
- Vertragsdokumente vorgelegt: ja/nein, Stand, Anlagen
```

Diese Daten werden an alle folgenden Skills weitergereicht.

## Lückenmanagement

Wenn der Auftraggeber Antworten nicht hat, ist das selbst schon ein Befund. Fehlende Anbieter-Sitzangaben, fehlende Subunternehmerliste, unklarer Verarbeitungszweck — alles davon landet ohne weiteres im Rückfragebrief.

## Aktuelle Rechtsprechung zum Berufsgeheimnis

- BGH, Urt. v. 15.06.2021 — AnwSt (R) 1/21, NJW 2021, 2883 Rn. 28: Das anwaltliche Berufsgeheimnis nach § 43a Abs. 2 BRAO schützt alle dem Rechtsanwalt anvertrauten Tatsachen unabhängig davon, ob der Mandant ein Interesse an der Geheimhaltung erkennen lässt; der Schutzbereich ist weit auszulegen.
- BGH, Beschl. v. 22.02.2022 — StB 7/21, NJW 2022, 1524 Rn. 14: § 53a StPO erstreckt das Zeugnisverweigerungsrecht auf Berufshelfer; der KI-Dienstleister kann unter diese Norm fallen, wenn er zur Berufsausübung des Anwalts mitwirkt — Voraussetzung ist vertragliche Mitwirkungspflicht.
- BVerwG, Urt. v. 25.06.2020 — 2 C 12.19, BVerwGE 168, 315 Rn. 42: Zur Reichweite des Verschwiegenheitsschutzes bei Steuerberatern nach § 57 StBerG; der Schutz erfasst auch interne Arbeitsdokumente, die dem Mandatsverhältnis dienen.
- EuGH, Urt. v. 26.06.2007 — C-305/05 (Ordre des barreaux francophones), NJW 2007, 2413 Rn. 31: Das anwaltliche Berufsgeheimnis ist ein grundrechtlich geschütztes Prinzip im Unionsrecht; Eingriffe müssen verhältnismäßig sein.

## Zentrale Normen (Paragrafenkette)

- § 43a Abs. 2 BRAO, § 43e BRAO — Verschwiegenheitspflicht und Dienstleisterregelung Rechtsanwalt
- § 57 Abs. 1, § 62a StBerG — Steuerberater
- § 43 Abs. 1, § 50a WPO — Wirtschaftsprüfer
- § 39a Abs. 2, § 39c PAO — Patentanwalt
- § 18 BNotO, § 26a BNotO — Notar
- §§ 203, 204 StGB — Straftatbestände Verletzung/Verwertung von Privatgeheimnissen
- §§ 53a, 97 StPO — Zeugnisverweigerungsrecht und Beschlagnahmeverbot für Berufshelfer

## Kommentarliteratur

- Henssler/Prütting BRAO, 5. Aufl. 2023, § 43e Rn. 1–55: Ausführlich zu den Voraussetzungen der Dienstleisterregelung, dem Begriff des Dienstleisters und den Anforderungen an die Verpflichtung in Textform.
- Böttcher/Peylo, AnwBl 2024, 124: Zur Einordnung von KI-Sprachmodellen als Dienstleister im Sinne des § 43e BRAO; Praxishinweise zur vertraglichen Ausgestaltung.

## Triage-Frage (Entscheidungsbaum)

```
Beruf bestimmt?
  Nein → Pflichtfrage 1 stellen
  Ja → Norm-Adapter anwenden (BRAO / StBerG / WPO / PAO / BNotO)
       → Kanzleiinfrastruktur oder Einzelmandats-Tool?
           Einzelmandats-Tool → Einwilligungspflicht § 26a Abs. 4 BNotO prüfen
           Kanzleiinfrastruktur → Einwilligung i.d.R. nicht erforderlich (DAV S. 15)
       → Auslandsbezug (US-Anbieter)?
           Ja → Cloud-Act-Prüfung erforderlich → Skill cloud-act-und-drittstaat-pruefen
           Nein → Weiter mit Verschwiegenheitsprüfung
```

## Output-Template — Eingangsdatensatz

**Adressat:** Kanzlei intern — Tonfall: sachlich-strukturiert

```
## Eingangsdaten [DATUM]
- Beruf: [BERUF]
- Norm-Adapter: § [NORM] [GESETZ]
- Anbieter: [NAME, SITZ, LAND]
- Produkt: [NAME, VERSION]
- Subunternehmer: [LISTE ODER "noch nicht bekannt"]
- Datenarten: [BESCHREIBUNG]
- Drittlandbezug: [ja/nein; wenn ja: CLOUD-Act-Risiko: ja/nein]
- Hostingland: [LAND]
- Vertragstyp: Kanzleiinfrastruktur / Einzelmandats-Tool
- Vertragsdokumente vorgelegt: [ja/nein, Datum, Anlagen]
- Nächste Schritte: [Prüfpunkte auflisten]
```
