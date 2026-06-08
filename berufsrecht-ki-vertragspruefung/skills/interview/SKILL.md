---
name: interview
description: "Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus den Norm-Adapter (BRAO StBerG WPO PAO BNotO) und entscheide ob Kanzleiinfrastruktur oder Einzelmandats-Tool im Sinne Absatz fuenf vorliegt. Lade dazu die Skill parallelnormen-andere-berufe."
---

# Kaltstart-Interview

## Fachkern: Kaltstart-Interview

- **KI-/Berufsrechtsproblem (Kaltstart-Interview):** Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus den Norm-Adapter (BRAO StBerG WPO PAO BNotO) und entscheide ob Kanzleiinfrastruktur oder Einzelmandats-Tool im Sinne Absatz fuenf vorliegt. Lade dazu die Skill parallelnormen-andere-berufe.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

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

Nach berufsrechtliche KI-Debatte 32/2025 (Seite 15) ist die Einwilligung des Mandanten oder Beteiligten regelmäßig nicht erforderlich, wenn das Tool als allgemeine Kanzleiinfrastruktur eingesetzt wird. Sie ist erforderlich, wenn das Tool unmittelbar einem einzelnen Mandat oder einem einzelnen Amtsgeschäft dient (Abs. 5 der jeweiligen Dienstleisterregelung).

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- § 43a Abs. 2 BRAO, § 43e BRAO — Verschwiegenheitspflicht und Dienstleisterregelung Rechtsanwalt
- § 57 Abs. 1, § 62a StBerG — Steuerberater
- § 43 Abs. 1, § 50a WPO — Wirtschaftsprüfer
- § 39a Abs. 2, § 39c PAO — Patentanwalt
- § 18 BNotO, § 26a BNotO — Notar
- §§ 203, 204 StGB — Straftatbestände Verletzung/Verwertung von Privatgeheimnissen
- §§ 53a, 97 StPO — Zeugnisverweigerungsrecht und Beschlagnahmeverbot für Berufshelfer

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
