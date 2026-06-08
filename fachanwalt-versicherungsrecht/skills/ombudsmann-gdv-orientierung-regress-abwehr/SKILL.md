---
name: ombudsmann-gdv-orientierung-regress-abwehr
description: "Ombudsmann GDV Orientierung Regress Abwehr im Plugin Fachanwalt Versicherungsrecht: prüft konkret Außergerichtliche Schlichtung über Versicherungs-Ombudsmann, Orientierung im Versicherungsvertragsrecht für Mandate und, Regressabwehr gegen Sozialversicherungstraeger und. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Ombudsmann GDV Orientierung Regress Abwehr

## Arbeitsbereich

**Ombudsmann GDV Orientierung Regress Abwehr** ordnet den Fall über die tragenden Prüfungslinien: Außergerichtliche Schlichtung über Versicherungs-Ombudsmann, Orientierung im Versicherungsvertragsrecht für Mandate und, Regressabwehr gegen Sozialversicherungstraeger und. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung` | Außergerichtliche Schlichtung über Versicherungs-Ombudsmann oder PKV-Ombudsmann als Alternative zur Klage. Anwendungsfall Streitwert bis 10000 EUR oder Mandant will Klage vermeiden und Schlichtung versuchen. Normen §§ 214 ff. VVG Schlichtungsverfahren § 204 BGB Hemmung Verjährung VSBG Verbraucherstreitbeilegungsgesetz § 84 VVG Sachverständigenverfahren. Prüfraster Zuständigkeit Ombudsmann Streitwert Schlichtungsantrag Beschwerdewortlaut PKV-Ombudsmann BaFin-Verbraucherbeschwerde. Output Schlichtungsantrag mit Sachverhaltsdarstellung Normbezug und Zuständigkeitsprüfung. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und klage-versicherer-strategie. |
| `fachanwalt-versicherungsrecht-orientierung` | Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung Versicherungsrecht vor. Normen VVG VAG GDV-Musterbedingungen AVB-Sparten BU KV LV Sach-Haftpflicht D-und-O. Prüfraster Sparten Normen FAO-Voraussetzungen verifizierbare Quellen typische Mandate Fristen. Output Rechtsgebietsuebersicht Normen verifizierbare Quellen und Routing zu Versicherungsmandats-Skills. Abgrenzung zu mandat-triage-versicherungsrecht und fachanwalt-versicherungsrecht-deckungsklage. |
| `fachanwalt-versicherungsrecht-regress-abwehr` | Regressabwehr gegen Sozialversicherungstraeger und Versicherungstraeger nach Schadensersatzleistung. Anwendungsfall Sozialversicherungstraeger oder Versicherung macht Regress auf Haftenden geltend. Normen § 116 SGB X Forderungsuebergang § 86 VVG Übergang § 76 LBG Dienstherrenregress. Prüfraster sachliche und zeitliche Kongruenz Quotenvorrecht Geschaedigter § 116 Abs. 3 SGB X Familienprivileg § 86 Abs. 3 VVG Mitverschulden Verjährung Hemmung Verhandlungen. Output Regressabwehrschreiben mit Konkurrenz-Einrede Quotenvorrecht-Argumentation und Verjährungseinrede. Abgrenzung zu klage-versicherer-strategie und schriftsatzkern-substantiierung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`

**Fokus:** Außergerichtliche Schlichtung über Versicherungs-Ombudsmann oder PKV-Ombudsmann als Alternative zur Klage. Anwendungsfall Streitwert bis 10000 EUR oder Mandant will Klage vermeiden und Schlichtung versuchen. Normen §§ 214 ff. VVG Schlichtungsverfahren § 204 BGB Hemmung Verjährung VSBG Verbraucherstreitbeilegungsgesetz § 84 VVG Sachverständigenverfahren. Prüfraster Zuständigkeit Ombudsmann Streitwert Schlichtungsantrag Beschwerdewortlaut PKV-Ombudsmann BaFin-Verbraucherbeschwerde. Output Schlichtungsantrag mit Sachverhaltsdarstellung Normbezug und Zuständigkeitsprüfung. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und klage-versicherer-strategie.

# Versicherungs-Ombudsmann / GDV-Schlichtung

## Zweck

Versicherungsrechts-Streit (Leistung, Anpassung, Kündigung) ist häufig im außergerichtlichen Schlichtungsverfahren günstig zu lösen: **Versicherungs-Ombudsmann e.V.** für PKV/Kompositversicherer, **PKV-Ombudsmann** für private Kranken/Pflege, **BaFin-Beschwerde** als Aufsichts-Eingang, **Sachverständigen-Verfahren § 84 VVG** bei Schadenhöhe-Streit.

## Eingaben

- Versicherungssparte (Sach, Haftpflicht, Leben, BU, PKV, Pflege, Rente)
- Streitgegenstand (Leistungsablehnung, Beitragsanpassung, Kündigung, Schadenhöhe)
- Versicherer (Verband: GDV Mitgliedschaft?)
- Streitwert (≤ 10.000 EUR: Ombudsmann-Verbindlichkeit Versicherer)
- Mandant (Verbraucher / Unternehmer)

## Rechtlicher Rahmen

- **§§ 1 ff. VVG** — Versicherungsvertragsgesetz
- **§ 6 VVG** — Beratungspflicht
- **§ 84 VVG** — Sachverständigen-Verfahren
- **§ 213 VVG** — Anfechtung wegen Anzeigepflichtverletzung
- **§ 203 VVG** — Beitragsanpassung PKV
- **§ 14 UKlaG** — Schlichtungs-Pflicht Verbraucher
- **VSBG** — Verbraucherstreitbeilegungs-Gesetz
- **Versicherungs-Ombudsmann-Verfahrensordnung 2021** (geändert 2024)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## ADR-Pfade

### Pfad 1 — Versicherungs-Ombudsmann (VVR e.V.)

- Bis 10.000 EUR: Versicherer-Bindung an Spruch (sofern Mitglied)
- Bis 100.000 EUR: Schlichtungs-Vorschlag (nicht bindend)
- Zuständigkeit: alle Sparten außer PKV/Pflege (eigener Ombudsmann)
- Kostenfrei für Verbraucher
- Frist Beschwerde: 6 Monate nach Versicherer-Ablehnung

### Pfad 2 — Ombudsmann PKV / Pflege (PKV-Ombudsmann e.V.)

- Privater Kranken/Pflege-Vers.
- Verfahrens-Dauer 3-6 Monate
- Schlichtungs-Vorschlag

### Pfad 3 — BaFin-Beschwerde

- Aufsichts-Behörde
- Kein Einzelfall-Spruch, aber Hinweis-Wirkung
- Bei systemischen Mängeln effektiv

### Pfad 4 — Sachverständigen-Verfahren § 84 VVG

- Bei Schadenhöhe-Streit (Hausrat, Gebäude, Kfz)
- Versicherer + Vers.-Nehmer benennen je 1 Sachverständigen
- Obmann bei Dissens
- Bindend (sofern nicht offenbar erheblich falsch)

## Workflow

### Phase 1 — Versicherer-Korrespondenz

- Schadensanzeige (Fristen je nach Sparte)
- Versicherer-Position abwarten
- Schriftliche Ablehnung als Eingang

### Phase 2 — Beschwerde-Vorbereitung

- Versicherungsbedingungen (AVB) analysieren
- Anzeigepflicht-Erfüllung dokumentieren
- Streitwert ermitteln

### Phase 3 — Ombudsmann-Antrag

- Online-Antrag bei VVR e.V. / PKV-Ombudsmann
- Sachverhalt + AVB + Versicherer-Korrespondenz
- Vollmacht Anwalt (möglich)

### Phase 4 — Schlichtungs-Verfahren

- Versicherer-Stellungnahme (4 Wochen)
- ggf. mündliche Erörterung
- Schlichtungs-Spruch / Vorschlag

### Phase 5 — Klage bei Scheitern

- LG / AG je Streitwert
- Bei PKV-Anpassung: spezialisierte Kammern

## Strategie und Taktik

- **Ombudsmann zuerst** — billig, schnell, oft erfolgreich
- **§ 213 VVG Anfechtung**: Anzeigepflicht-Verletzung sehr genau prüfen — Versicherer hat enge Belehrungs-Pflichten
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Sachverständigen-Verfahren**: bei klar bezifferbarem Schaden günstig; bei rechtlichen Fragen ungeeignet
- **BU-Versicherung**: 50-%-Berufsunfähigkeits-Anforderung; Sachverständigen-Strategie kritisch

## Querverweise

- `fachanwalt-versicherungsrecht-orientierung` — Triage
- `fachanwalt-versicherungsrecht-leistungsklage-vvg` — Klage
- `fachanwalt-versicherungsrecht-cyberversicherung-nis2` — Sonderfall
- `fachanwalt-bank-kapitalmarktrecht-ombudsmann-bafin-schlichtung` — Bank-Variante

## Quellen und Updates

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 214 VVG (Ombudsmann-Schlichtung, Verjährungshemmung) → § 204 Abs. 1 Nr. 4 BGB (Hemmung durch Schlichtungsantrag) → § 84 VVG (Sachverständigen-Verfahren) → VSBG (Verbraucherstreitbeilegungsgesetz) → VomVO (Verordnung über Versicherungsombudsmann) → § 6 VomVO (Bindungswirkung für Versicherer bis 10.000 EUR)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `fachanwalt-versicherungsrecht-orientierung`

**Fokus:** Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung Versicherungsrecht vor. Normen VVG VAG GDV-Musterbedingungen AVB-Sparten BU KV LV Sach-Haftpflicht D-und-O. Prüfraster Sparten Normen FAO-Voraussetzungen verifizierbare Quellen typische Mandate Fristen. Output Rechtsgebietsuebersicht Normen verifizierbare Quellen und Routing zu Versicherungsmandats-Skills. Abgrenzung zu mandat-triage-versicherungsrecht und fachanwalt-versicherungsrecht-deckungsklage.

# Fachanwalt für Versicherungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 40 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Versicherungsvertrag | VVG §§ 1 ff. Anzeigepflicht §§ 19 ff. Praemienpflicht § 33 Leistungspflicht §§ 100 ff. |
| Versicherungsaufsicht | VAG |
| Pflichtversicherung Kfz | PflVG |
| Berufsunfähigkeit | §§ 172 ff. VVG |
| Krankenversicherung privat | §§ 192 ff. VVG MB/KK |
| Lebensversicherung | §§ 150 ff. VVG |
| Allgemeines Vertragsrecht | §§ 305 ff. BGB AGB-Kontrolle |
| Verjährung | § 195 BGB (drei Jahre) — Sonderregel § 12 VVG aufgehoben |

## Typische Mandate

- BU-Streitigkeiten (Leistungsablehnung)
- Krankheitskostenversicherung (Erstattung Pflegestufen)
- Lebensversicherung (Rückkaufswert Auszahlung im Todesfall)
- Hausratversicherung (Einbruchsdiebstahl Wasserschaden)
- Haftpflichtversicherung (Deckungsstreit)
- D-und-O-Versicherung für Organe Geschäftsleiter
- Berufshaftpflicht Anwaltshaftpflicht

## Fristen

- **Klagefrist** keine spezifische — Verjährung drei Jahre (§ 195 BGB).
- **Beschwerdefrist** zum BaFin gegen Versicherer regelmäßig keine Frist.
- **Anzeigepflichten** Versicherungsnehmer Unverzueglich (§ 19 VVG).
- **Frist nach Schadensfall** vertraglich vereinbart (Obliegenheiten § 28 VVG).

## Hauptgerichte

- Amtsgericht Landgericht (regulaere ZPO-Streitwertgrenze 10.000 EUR ab 01.01.2026).
- OLG / BGH IV. Zivilsenat für Versicherungssachen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Versicherungsrecht DAV.

## Schnittstellen

- **kanzlei-allgemein** für Fristen und Versand.
- **fachanwalt-verkehrsrecht** bei Kfz-Haftpflicht.
- **fachanwalt-medizinrecht** bei Krankenversicherung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026; offene Quellen)

Vor Versand jeweils Volltext in offener Quelle aufrufen (juris.bundesgerichtshof.de, dejure.org, openjur.de):

1. **BGH, Urt. v. 12.3.2025, IV ZR 32/24** — Krankentagegeldversicherung: Klauselersetzung nach Unwirksamkeit nicht ohne Weiteres zulässig; Versicherer kann unwirksame Tagessatz-Herabsetzung nicht durch im Kern gleiche neue Klausel ersetzen. Pressemitteilung Nr. 47/25 vom 12.3.2025.
2. **BGH, IV ZR 70/25, 2025** — PKV-Beitragsanpassung: Mitteilungsschreiben muss die konkrete Rechnungsgrundlage benennen (§ 203 Abs. 5 VVG).
3. **BGH, IV ZR 86/24, Urt. v. 15.10.2025** — Beitragsanpassung PKV; Prüfungsmaßstab. Quelle: bundesgerichtshof.de.
4. **BGH, Urt. v. 14.7.2021, IV ZR 153/20** — Versicherungsfall BU: Eintritt nach Ablauf der bedingungsgemäßen sechs-monatigen Prognosezeit.
5. **BGH, Urt. v. 28.1.2025, VI ZR 183/22** — DSGVO-Schadensersatz hat reine Ausgleichsfunktion; SCHUFA-Meldung bei streitiger Forderung unzulässig.

### Paragrafenkette (Überblick VVG-Struktur)

§§ 1–21 VVG (allgemeine Vorschriften, Informationspflichten, Widerruf) → §§ 28–32 VVG (Obliegenheiten, Rechtsfolgen) → §§ 74–99 VVG (Schadensversicherung) → §§ 100–112 VVG (Haftpflichtversicherung) → §§ 150–171 VVG (Lebensversicherung) → §§ 172–177 VVG (Berufsunfähigkeitsversicherung) → §§ 192–215 VVG (Krankenversicherung, Ombudsmann) → §§ 305–310 BGB (AGB-Kontrolle AVB) → § 215 VVG (örtliche Zuständigkeit Klage VN)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Bereich | Frist | Norm |
|---|---|---|
| Verjährung Versicherungsleistung | 3 Jahre ab Schluss Kenntnisjahr | §§ 195, 199 BGB |
| Widerruf (korrekte Belehrung) | 30 Tage | § 8 Abs. 1 VVG |
| Widerruf Lebensversicherung (falsche/fehlende Belehrung) | unbegrenzt (EuGH/BGH-Linie; Volltext vor Versand verifizieren) | § 8 VVG, EuGH C-209/12 (Endress) |
| Anzeigepflicht-Schadensfall | laut AVB (meist unverzüglich) | § 28 VVG |
| Hemmung durch Schlichtungsantrag | bis Entscheidung Ombudsmann | § 204 BGB i.V.m. § 214 VVG |

## Triage — Orientierungs-Routing

1. **Sachgebiet/Sparte identifizieren** (BU → `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`; LV → `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf`; D&O → `fachanwalt-versicherungsrecht-do-deckungsabwehr`; Cyber → `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`).
2. **Ablehnungsschreiben eingegangen?** → `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`.
3. **Klage vorbereiten?** → `fachanwalt-versicherungsrecht-deckungsklage` + `klage-versicherer-strategie`.
4. **Schlichtung zuerst?** → `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`.
5. **Regress-Abwehr gegen Sozialversicherungsträger?** → `fachanwalt-versicherungsrecht-regress-abwehr`.

## 3. `fachanwalt-versicherungsrecht-regress-abwehr`

**Fokus:** Regressabwehr gegen Sozialversicherungstraeger und Versicherungstraeger nach Schadensersatzleistung. Anwendungsfall Sozialversicherungstraeger oder Versicherung macht Regress auf Haftenden geltend. Normen § 116 SGB X Forderungsuebergang § 86 VVG Übergang § 76 LBG Dienstherrenregress. Prüfraster sachliche und zeitliche Kongruenz Quotenvorrecht Geschaedigter § 116 Abs. 3 SGB X Familienprivileg § 86 Abs. 3 VVG Mitverschulden Verjährung Hemmung Verhandlungen. Output Regressabwehrschreiben mit Konkurrenz-Einrede Quotenvorrecht-Argumentation und Verjährungseinrede. Abgrenzung zu klage-versicherer-strategie und schriftsatzkern-substantiierung.

# Regress-Abwehr

## Kernsachverhalt

Ein Schädiger oder dessen Haftpflichtversicherer wird nach einem Schadensereignis (Verkehrsunfall, Körperverletzung, Arbeitsunfall) von einem Sozialversicherungsträger, einem privaten Versicherer oder einem Dienstherrn auf Rückerstattung der erbrachten Leistungen in Anspruch genommen. Der Forderungsübergang erfolgt kraft Gesetzes nach §§ 116 SGB X, 86 VVG, 76 BeamtVG. Gegenüber diesen Regressansprüchen stehen mehrere Verteidigungslinien zur Verfügung: Familienprivileg, fehlende Kongruenz, Quotenvorrecht des Geschädigten bei Mitverschulden sowie die Verjährungseinrede.

## Kaltstart-Rückfragen

1. Wer regressiert — gesetzlicher Krankenversicherer (§ 116 SGB X), Rentenversicherer (§ 119 SGB X), Berufsgenossenschaft (§ 110 SGB VII), privater Versicherer (§ 86 VVG), Dienstherr (§ 76 BeamtVG)?
2. Aus welchem Schadensereignis stammt der Regress — Verkehrsunfall, Körperverletzung, Arbeitsunfall, Berufskrankheit? Welcher Mandant haftet warum?
3. Welche Sozialleistungen wurden für welchen Zeitraum erbracht — Krankenhauskosten, Krankengeld, Reha, Verletztenrente, Hinterbliebenenrente, Heilbehandlung?
4. Ist die zugrundeliegende Schadenshaftung dem Grunde und der Höhe nach bereits geklärt oder noch streitig?
5. Bestehen Verteidigungseinwände wie Familienprivileg (§ 86 Abs. 3 VVG, § 116 Abs. 6 SGB X), Mitverschulden des Geschädigten, fehlende sachliche oder zeitliche Kongruenz?
6. Liegt eine bereits abgelaufene Verjährungsfrist vor? Wann erlangte der Regressnehmer Kenntnis vom Schadensereignis und vom Schädiger?
7. Existiert ein Sozialleistungsvermerk im Schadenersatzprozess — wurde der Sozialversicherungsträger vom Geschädigten benachrichtigt?
8. Sind mehrere Regressnehmer vorhanden (z.B. Krankenkasse + Rentenversicherung + Berufsgenossenschaft) und wurde eine koordinierte Verteidigungsstrategie besprochen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 116 Abs. 1 SGB X** — Ein auf anderen Vorschriften beruhender Anspruch auf Ersatz eines Schadens geht auf den Versicherungsträger oder Träger der Eingliederungshilfe oder der Sozialhilfe über, soweit dieser auf Grund des Schadensereignisses Sozialleistungen zu erbringen hat, die der Behebung eines Schadens der gleichen Art dienen und sich auf denselben Zeitraum wie der vom Schädiger zu leistende Schadensersatz beziehen.

**§ 116 Abs. 3 SGB X (Quotenvorrecht)** — Ist der Anspruch auf Schadensersatz nicht in voller Höhe gedeckt, weil der Geschädigte an dem Schadensereignis mitgewirkt hat, geht der Anspruch nur insoweit über, als der Schädiger verpflichtet ist, denjenigen Teil des Schadens zu ersetzen, dessen Erstattung der Träger nicht verlangen kann. Der übergegangene Anspruch steht im Rang nach dem Anspruch des Geschädigten.

**§ 116 Abs. 6 SGB X (Familienprivileg)** — Ein Übergang ist ausgeschlossen, wenn der Schädiger mit dem Geschädigten oder seinen Hinterbliebenen in häuslicher Gemeinschaft lebt oder dem Geschädigten zur Fürsorge verpflichtet ist, es sei denn, der Schaden wurde vorsätzlich verursacht.

**§ 86 Abs. 1 VVG** — Steht dem Versicherungsnehmer ein Ersatzanspruch gegen einen Dritten zu, geht dieser Anspruch auf den Versicherer über, soweit der Versicherer den Schaden ersetzt.

**§ 86 Abs. 3 VVG (Familienprivileg)** — Der Übergang nach Absatz 1 kann nicht zum Nachteil des Versicherungsnehmers geltend gemacht werden. Insbesondere geht der Anspruch nicht über, wenn der Dritte, gegen den der Anspruch besteht, mit dem Versicherungsnehmer oder einem Versicherten in häuslicher Gemeinschaft lebt, es sei denn, dass dieser den Schaden vorsätzlich verursacht hat.

**§ 110 SGB VII** — Haben Personen, deren Haftung nach §§ 104 bis 107 beschränkt ist, den Versicherungsfall vorsätzlich oder grob fahrlässig herbeigeführt, haften sie den Sozialversicherungsträgern für die infolge des Versicherungsfalls erbrachten Aufwendungen.

**§ 195 BGB** — Die regelmäßige Verjährungsfrist beträgt drei Jahre.

**§ 203 BGB** — Schweben zwischen dem Schuldner und dem Gläubiger Verhandlungen über den Anspruch, so ist die Verjährung gehemmt, bis der eine oder der andere Teil die Fortsetzung der Verhandlungen verweigert.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Regress-Abwehr

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Regressnehmer identifizieren | § 116 SGB X (GKV, DRV, BA), § 110/111 SGB VII (BG), § 86 VVG (privat), § 76 BeamtVG | Zuständige Norm, Klageart, Gericht |
| 2 | Schadensereignis und Haftungsgrund | Unfall, Vorsatz, Fahrlässigkeit; Haftungsgrundlage des Schädigers (§§ 823, 7 StVG, 833 BGB) | Besteht Haftung dem Grunde nach? |
| 3 | Forderungsübergang prüfen | Übergang kraft Gesetzes zum Zeitpunkt des Schadensereignisses; kein rechtsgeschäftlicher Übertrag nötig | Anspruch besteht ab Schadenszeitpunkt |
| 4 | Sachliche Kongruenz | Sozialleistung und Schadensersatzposition müssen gleichartig sein: Heilbehandlung ↔ Krankenversicherungsleistung; Verdienstausfall ↔ Krankengeld/Übergangsgeld | Nicht kongruente Positionen aus Regress heraushalten |
| 5 | Zeitliche Kongruenz | Sozialleistung und Schadensersatz müssen denselben Zeitraum betreffen | Leistungen außerhalb des Schadensersatzzeitraums sind nicht regressfähig |
| 6 | Familienprivileg | § 116 Abs. 6 SGB X, § 86 Abs. 3 VVG: häusliche Gemeinschaft Schädiger/Geschädigter, kein Vorsatz | Kompletter Anspruchsausfall bei Vorliegen |
| 7 | Quotenvorrecht § 116 Abs. 3 SGB X | Mitverschulden des Geschädigten (§ 254 BGB) bestimmt Quote; übergegangener Anspruch nur nach vollständiger Deckung des Eigenanspruchs des Geschädigten | Regressbetrag ggf. erheblich reduziert |
| 8 | Privilegierung § 104 SGB VII | Haftungsbeschränkung des Arbeitgebers/Betriebsangehörigen gegenüber BG-Regress; nur bei Vorsatz oder grober Fahrlässigkeit nach § 110 SGB VII durchbrechbar | Bei leichter/mittlerer Fahrlässigkeit kein BG-Regress |
| 9 | Verjährung | § 195 BGB 3 Jahre; Beginn § 199 BGB Kenntnis Träger von Ereignis + Person des Schädigers; Hemmung § 203 BGB (Verhandlungen), § 204 BGB (Klage) | Verjährungseinrede erheben |
| 10 | Sozialleistungsvermerk | Geschädigter muss Träger benachrichtigen; fehlende Benachrichtigung → Erlöschen des übergegangenen Anspruchs nach § 116 Abs. 7 SGB X | Fehlt Vermerk → Abwehr des gesamten Anspruchs möglich |
| 11 | Höhe der erbrachten Leistungen | Nachweis durch Leistungsbescheid, Abrechnungsunterlagen; Bestreiten mit Nichtwissen zu Detailpositionen | Reduktion auf nachgewiesene Beträge |
| 12 | Mitverschulden des Schädigers geltend machen | § 254 BGB gegen Regressnehmer einwenden; Quote mindert Regressbetrag proportional | Prozesstaktischer Vorteil |
| 13 | Schadensminderungspflicht | Geschädigter hat zumutbare Rehab-Maßnahmen zu ergreifen; Unterlassen führt zur Kürzung auch beim übergegangenen Anspruch | Kürzung wegen Obliegenheitsverletzung |
| 14 | Vorteilsausgleichung | Vorteile die dem Geschädigten durch das Schadensereignis entstanden sind mindern den Schaden; übergegangener Anspruch ebenfalls gemindert | Vorteilsanrechnung geltend machen |
| 15 | Vergleich / Abschluss | Kompromissangebot nach Ermittlung des tatsächlich kongruenten, nicht verjährten, nach Quote bereinigten Restbetrags | Schriftliche Freistellungsbestätigung |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Erbrachte Sozialleistungen und deren Höhe | Regressnehmer (Träger) | Leistungsbescheid, Kontenauszug, Abrechnungsakte |
| Sachliche Kongruenz | Regressnehmer | Vergleich der Schadenspositionen mit Leistungsarten |
| Zeitliche Kongruenz | Regressnehmer | Leistungszeitraum aus Bescheid mit Schadensersatzzeitraum abgleichen |
| Haftung dem Grunde nach | Regressnehmer; bei Rechtskraft des Schadenersatzurteils präjudiziell | Urteil, Haftpflichtbescheid |
| Familienprivileg | Schädiger / Versicherter | Melderegistereintrag, Wohnortbestätigung, Mietvertrag |
| Mitverschulden des Geschädigten (Quote) | Schädiger | Unfallbericht, Sachverständigengutachten, Zeugenaussagen |
| Verjährung | Schädiger (Einredeführer) | Kenntnis des Trägers nachweisen oder glaubhaft machen |
| Grobe Fahrlässigkeit § 110 SGB VII | BG | Sachverständigengutachten, Arbeitsschutzakten |
| Fehlen des Sozialleistungsvermerks | Schädiger | Klärung mit Träger ob Benachrichtigung erfolgte |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Verjährungsfrist Regressanspruch | § 195 BGB | 3 Jahre ab Kenntnis des Trägers von Schadensereignis und Schädiger (§ 199 BGB) | Kenntnis beginnt regelmäßig mit Erhalt des Unfallberichts oder staatsanwaltschaftlicher Ermittlungsakte |
| Hemmung durch Verhandlungen | § 203 BGB | Gehemmt solange Verhandlungen schweben; endet einen Monat nach Abbruch | Kein förmliches Anerkenntniserfordernis; jede ernsthafte Erörterung hemmt |
| Hemmung durch Klage | § 204 BGB | Hemmung ab Zustellung der Klageschrift | |
| Frist für Sozialleistungsvermerk | § 116 Abs. 7 SGB X | Keine gesetzliche Frist; aber praktisch unverzüglich nach Schadensereignis | Fehlender Vermerk kann Anspruch erlöschen lassen |
| Anmeldefrist BG-Regress § 110 SGB VII | — | Keine eigene Ausschlussfrist; aber allgemeine Verjährung | Verjährung beginnt mit Kenntnis des Anspruchs |
| Reaktionsfrist auf Regressschreiben | — | Keine gesetzliche Frist; aber nach § 242 BGB zeitnah abwehren | Zuwarten erzeugt kein Anerkenntnis; Verjährungshemmung durch Verhandlungen aber möglich |

## Typische Gegenargumente

| Gegenargument des Regressnehmers | Gegenstrategie |
|---|---|
| "Kongruenz ist evident — Krankenbehandlungskosten für Unfallverletzung" | Einzelpositionen prüfen: Wahlleistungen, Eigenanteile, nicht unfallbedingte Behandlungen herausrechnen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Quote mindert Regress nicht, weil Gesamtschaden gedeckt ist" | § 116 Abs. 3 SGB X ist zwingend: Quotenvorrecht des Geschädigten geht vor; Übergang nur soweit Haftungsanteil vorhanden |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Hemmung durch Korrespondenz" | Nur echte Verhandlungen hemmen; reine Sachverhaltsaufklärung oder bloße Forderungsübermittlung sind keine Verhandlungen i.S.d. § 203 BGB |
| "Vorteilsausgleichung ist ausgeschlossen" | Vorteilsausgleichung greift nur bei Vorteilen die kausal durch das Schadensereignis entstanden sind und nicht unzumutbar sind |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Regress des Versicherers abwehren | Regress-Abwehrschreiben nach Pruefschema; Template unten |
| Variante A — Regressforderung teilweise berechtigt | Teilanerkenntnis verhandeln; Gesamtbetrag minimieren |
| Variante B — Verjährung des Regressanspruchs eingetreten | Verjährungseinrede erheben; kein inhaltliches Eingehen noetig |
| Variante C — Regress gegen Arbeitnehmer Arbeitgeber haftet | Arbeitgeberhaftung pruefen; Regress auf Arbeitgeber abwaelzen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Abwehr wegen fehlender sachlicher Kongruenz

```
An [Gesetzliche Krankenkasse / Sozialversicherungsträger]
Ihr Zeichen: [Az. Träger]
Unser Zeichen: [Az. Kanzlei]

Regress § 116 SGB X — Ereignis vom [Datum]
Geschädigter: [Name]
Mandant/Schädiger: [Name]

Sehr geehrte Damen und Herren,

wir zeigen an, namens und in Vollmacht [des Mandanten / der
Haftpflichtversicherung] tätig zu sein.

Ihren mit Schreiben vom [Datum] geltend gemachten Regressanspruch
in Höhe von EUR [Betrag] weisen wir dem Grunde und der Höhe nach
zurück.

1. Fehlende sachliche Kongruenz

Die von Ihnen erbrachten Leistungen sind nicht in vollem Umfang
mit den Schadensersatzpositionen unseres Mandanten sachlich
kongruent. Im Einzelnen:

a) Wahlleistungen (EUR [x]) — Krankenhauszusatzleistungen wie
 Zweibettzimmer und Chefarztbehandlung stellen keine durch
 § 116 SGB X regressfähigen Leistungen dar, da sie nicht auf
 den Kernschaden rückführbar sind und von der GKV im Rahmen
 des gesetzlichen Leistungskatalogs nicht gedeckt werden.

b) Behandlungskosten ab [Datum] (EUR [x]) — Die Behandlungen
 nach diesem Zeitpunkt betreffen ausweislich der vorliegenden
 Atteste eine von der Unfallverletzung unabhängige Vorerkrankung.
 Die zeitliche und sachliche Kongruenz fehlt insoweit.

2. Quotenvorrecht § 116 Abs. 3 SGB X

Unabhängig vom Vorstehenden weisen wir darauf hin, dass der
Geschädigte den Unfall zu 40 % mitverursacht hat
(Sachverständigengutachten [Datum], Anlage [X]). Der
Forderungsübergang auf Ihren Träger ist damit auf den durch
den Haftungsanteil unseres Mandanten (60 %) gedeckten Teil
beschränkt. Das Quotenvorrecht des Geschädigten nach § 116 Abs. 3
SGB X geht vor.

Regressfähiger Maximalbetrag: EUR [x] × 60 % = EUR [y].
Davon zunächst der nicht durch Sozialleistungen gedeckte
Eigenanteil des Geschädigten abzuziehen.

3. Verjährungseinrede

Vorsorglich erheben wir die Einrede der Verjährung (§ 214 BGB).
Kenntnis von Schadensereignis und Schädiger bestand Ihrem Träger
nachweislich seit [Datum]. Die Verjährungsfrist von drei Jahren
(§ 195 BGB) ist damit am [Datum + 3 Jahre] abgelaufen. Hemmende
Tatbestände sind nicht ersichtlich.

Wir bitten Sie, den Regressanspruch bis [Frist] zurückzunehmen.
Andernfalls sehen wir uns veranlasst, ein gerichtliches Verfahren
abzuwarten und dort sämtliche Einwände geltend zu machen.

Mit freundlichen kollegialen Grüßen
[Kanzlei]
```

### Baustein 2: Geltendmachung des Familienprivilegs

```
An [Privater Versicherer / Krankenkasse]
Ihr Zeichen: [Az.]

Regress § 116 Abs. 6 SGB X / § 86 Abs. 3 VVG — Ereignis vom [Datum]

Sehr geehrte Damen und Herren,

der geltend gemachte Regressanspruch ist wegen des gesetzlichen
Familienprivilegs vollständig ausgeschlossen.

1. Häusliche Gemeinschaft

Der Schädiger [Name] und die Geschädigte [Name] lebten zum
Zeitpunkt des Schadensereignisses am [Datum] in häuslicher
Gemeinschaft unter der Anschrift [Adresse]. Wir überreichen als
Anlage A die gemeinsame Melderegisterbescheinigung sowie
Anlage B den Mietvertrag, der beide Personen als Mieter ausweist.

2. Kein Vorsatz

Das Schadensereignis beruhte auf [kurze Beschreibung Fahrlässigkeit].
Vorsätzliches Handeln scheidet nach dem Sachverhalt aus.

3. Rechtsfolge

Gemäß § 116 Abs. 6 SGB X geht der Schadensersatzanspruch unter
diesen Voraussetzungen nicht auf Ihren Träger über. Die gesetzliche
Forderungsabtretung ist vollständig ausgeschlossen.
§ 86 Abs. 3 VVG enthält eine inhaltsgleiche Regelung für
privatrechtliche Versicherungsverhältnisse.

Der Regressanspruch besteht nicht. Wir bitten um schriftliche
Bestätigung der Rücknahme bis [Frist].

Mit freundlichen kollegialen Grüßen
[Kanzlei]
```

### Baustein 3: Vergleichsangebot nach Kongruenzprüfung

```
An [Sozialversicherungsträger / Versicherer]
Ihr Zeichen: [Az.]

Regresssache [Geschädigter] / [Schädiger] — Vorläufiges Vergleichsangebot

Sehr geehrte Damen und Herren,

nach eingehender Prüfung Ihres Regressanspruchs ergibt sich
folgende Berechnung des anerkennungsfähigen Betrags:

Ihrer Forderung: EUR [Gesamtforderung Träger]

Abzüge:
– Nicht kongruente Positionen (Wahlleistungen, Vorerkrankung): EUR [x]
– Quotenbereinigung 40 % Mitverschulden des Geschädigten
 gem. § 116 Abs. 3 SGB X: EUR [y]
– Verjährte Teilbeträge (Leistungen vor [Datum]): EUR [z]
Anerkennungsfähiger Betrag: EUR [Restbetrag]

Namens und in Vollmacht unseres Mandanten bieten wir zur
vollständigen und abschließenden Erledigung aller Ansprüche
aus dem Ereignis vom [Datum] einen Vergleich über EUR [Betrag]
an. Dies entspricht dem nach vorstehender Berechnung
anerkennungsfähigen Betrag zuzüglich eines Risikozuschlags von
10 % zur Vermeidung weiterer Rechtskosten.

Das Angebot gilt bis zum [Frist] und erlischt danach ersatzlos.

Mit freundlichen kollegialen Grüßen
[Kanzlei]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert | Regressforderung des Trägers netto nach Abzug unstreitiger Positionen | Keine Erhöhung durch Mitverschuldensquote; diese wirkt auf Hauptsache |
| Gerichtskosten | Nach GKG Anlage 1 Nr. 1210 (Zivilklage): z.B. bei EUR 50.000 Streitwert ca. EUR 3 nach GKG | Beim LG Kammer für Handelssachen bei Versicherern; beim SG bei öffentlich-rechtlichen Trägern |
| Anwaltskosten | RVG nach Streitwert; bei 50.000 EUR Gegenstandswert 1,3 Verfahrensgebühr ca. EUR 1.564 zzgl. MwSt. | Kostenerstattung bei Obsiegen |
| Sachverständigenkosten | Kongruenzgutachten ca. EUR 1.500–3.500 je nach Umfang | Investition lohnt bei Regressforderung über EUR 10.000 |
| Zuständiges Gericht | Zivilklage: AG/LG nach Streitwert; BG-Regress § 110 SGB VII: Arbeitsgericht; GKV/RV-Regress § 116 SGB X: Zivilgericht. Rechtsprechung nur live verifiziert eintragen. | Zuständigkeit prüfen vor Einlassung |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Familienprivileg eindeutig gegeben | Sofortige schriftliche Abwehr mit Melderegisterbescheinigung; kein Vergleich nötig |
| Kongruenz teilweise strittig, Verjährung unklar | Detaillierte Kongruenzanalyse vor Verhandlungseinstieg; Verjährungseinrede hilfsweise erheben |
| Mitverschulden des Geschädigten hoch (>30 %) | Quotenvorrecht offensiv einwenden; Berechnung des Quotendeckelbetrags schriftlich vorlegen |
| Regressforderung über EUR 50.000 | Sachverständigengutachten zur Kongruenz beauftragen; wirtschaftlich sinnvoll |
| BG-Regress § 110 SGB VII | Subjektiven Tatbestand der groben Fahrlässigkeit streng angreifen; BSG-Rechtsprechung nutzen |
| Mehrere Regressnehmer gleichzeitig | Koordination zwischen Haftpflichtversicherer und Fachanwalt; einheitliche Linie zu Mitverschulden und Kongruenz |
| Verjährung klar eingetreten | Reine Einredeschrift; keine inhaltliche Einlassung zur Haftung (würde Hemmung riskieren) |
| Vergleich angestrebt | Erst eigene Maximalposition berechnen; Vergleich nur mit schriftlichem Abfindungserlass ohne weiteren Regress |

## Anschluss-Skills

- `fachanwalt-verkehrsrecht-regulierungsanforderung` — bei zugrundeliegendem Verkehrsunfall Haftungsquote und Schadensabwicklung
- `fachanwalt-versicherungsrecht-deckungsklage` — wenn Haftpflichtversicherer Deckung für Regressfall verweigert
- `unfall-haftungsquote-berechnen` — Berechnung der Mitverschuldensquote als Grundlage für Quotenvorrecht
- `klage-versicherer-strategie` — wenn Regressnehmer Klage erhebt und Prozessstrategie erforderlich ist

## Quellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Geigel, Der Haftpflichtprozess, 28. Aufl. 2022
- Küppersbusch/Höher, Ersatzansprüche bei Personenschaden, 13. Aufl. 2021
- Eichenhofer/Wenner, SGB X, 3. Aufl. 2022

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 116 SGB X (Übergang Schadensersatzansprüche auf Sozialversicherungsträger) → § 116 Abs. 3 SGB X (Quotenvorrecht des Geschädigten) → § 86 VVG (Übergang Schadensersatzanspruch auf Versicherer) → § 86 Abs. 3 VVG (Familienprivileg) → § 67 VVG a.F. (für Altverträge) → § 195 BGB (Verjährung) → § 203 BGB (Hemmung) → § 254 BGB (Mitverschulden, relevant für Quotenvorrecht)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Audit-Hinweis

**Datum:** 27.05.2026
**Bearbeitung:** Halluzinations-Reparatur (Repair-Task 114)

| AZ | Status | Massnahme |
|---|---|---|
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
