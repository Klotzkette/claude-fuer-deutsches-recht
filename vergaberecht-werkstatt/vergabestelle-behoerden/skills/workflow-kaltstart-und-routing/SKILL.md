---
name: workflow-kaltstart-und-routing
description: 'Schnelltriage der Vergabestelle für ein einzelnes Dokument oder eine konkrete Frage: bestimmt Rolle, Phase, rote Frist, Regime, Aktenfundstelle, Bestangebot, LV-, Wertungs- oder Rechtsschutzpfad und nächsten Output. Kein vollständiger Ordnerfall; Ordner, ZIP und Mehrfachfragen übernimmt der Master-Orchestrator.'
---

# Kaltstart und Routing

**Arbeitsname:** Einzelnes Behördenstück rein, belastbare Arbeitsweiche und erster Output raus.

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Aufgabe
Dieser Workflow-Skill führt genau ein Dokument oder eine konkrete Frage in den passenden Arbeitsweg. Er extrahiert Rolle, Verfahrensstand, Fundstelle, Frist, Rechtsfrage und nächsten Output, ohne bereits den gesamten Aktenbestand zu inventarisieren.

## Abgrenzung

- Vollständiger Ordner, ZIP, Portal-/DMS-Export, mehrere Dokumente oder mehrere miteinander verbundene Fragen: `vergabe-os-master-orchestrator`.
- Ein Dokument, eine Bieterfrage, eine Rüge, ein Wertungsausschnitt oder eine konkrete Rechtsfrage: dieser Skill.
- Noch keine Unterlagen, nur Rollen-, Regime- oder Zuständigkeitsorientierung: `einstieg-routing`.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Ein-Dokument-Schnelltriage

1. Dokumenttyp, Absender, Empfänger, Datum, Version, Verfahrensbezug und zitierfähige Fundstelle erfassen.
2. Aus dem Dokument nur die entscheidenden Tatsachen und Rechtsbehauptungen extrahieren; offene Aktenfragen als Lücke markieren.
3. Früheste ausgelöste Frist mit Norm, Startpunkt, Zugangsbeleg und sicherem Fristende bestimmen oder als nicht berechenbar kennzeichnen.
4. Genau eine Arbeitsroute wählen: Vermerk, Bieterantwort, Berichtigung, Wertungsprüfung, VK-/OLG-Verteidigung oder Uploadhandlung.
5. Einen sofort nutzbaren Kernoutput plus höchstens drei gezielte Nachforderungen liefern.

## Bedienlogik

- Starte mit einer Ein-Bildschirm-Lage: Kurzlage, rote Fristen, vorhandene Dateien, offene Lücken, empfohlener Output.
- Biete höchstens drei Output-Optionen an und markiere genau eine Empfehlung.
- Nutze Entscheidungsfragen nur als Weiche: Verfahren reparieren, Wertung verteidigen, Berichtigung veröffentlichen, Zuschlag sichern, VK/OLG führen.
- Gib bei Datei- oder Portalbezug immer den nächsten Bedienhandlungspunkt aus: Datei prüfen, Mapping bauen, Freigabe einholen, Upload vorbereiten, Quittung ablegen.
- Vermeide Beratungstext ohne Arbeitsprodukt. Jeder Abschnitt muss zu Vermerk, Matrix, Checkliste, Schriftsatzbaustein oder Uploadpaket führen.

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Fristenampel, Dokumentenmatrix und Output-Weiche in derselben Antwort liefern.
4. Passende Spezialskills aus diesem Plugin vorschlagen und mit einem Satz begründen.
5. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste, Vermerk, Schriftsatzbaustein oder Uploadpaket.
6. Mit einem Nutzungscheck schließen: Kann die Vergabestelle jetzt entscheiden, freigeben, veröffentlichen, verteidigen oder nachfordern?

## Direkt-Routing Aktenstart

| Lage | Primärer Skill |
|---|---|
| Ungeordnete Bedarfsanforderung, Fachbereichsmappe, Portalexport, Ratsvorlage, E-Mail-Ordner oder ZIP | `dokumente-intake` |
| Vergabeakte, Unterlagen, Wertungsvermerk, Bieterfragen, Portalquittungen oder Nachweise fehlen | `unterlagen-luecken` |
| Aus Lücken soll ein Arbeitsauftrag an Fachbereich, Zentrale Vergabestelle, IT oder Kanzlei entstehen | `workflow-unterlagen-lueckenliste` |
| Tragende Norm, Schwellenwert, Rechtsprechung oder Landeswertgrenze ist unsicher | `quellen-livecheck` und `schwellenwerte-2026-2027-livecheck` |

## Direkt-Routing Bestwertung

| Lage | Primärer Skill |
|---|---|
| Vergabestelle will Bestands-, Zustands-, Kosten-, Bauzeit-, Umwelt- oder Rechtsdaten für Bedarf, Bündelung, LV, Budget oder Kriterien nutzen | `wirklichkeitsdaten-beschaffung-steuern` |
| Vergabestelle will Portfolio priorisieren, beschleunigt beauftragen, Tragfähigkeit/Mobilität prüfen, ÖPP/CAPEX oder Fertigteil-/Serienlösung vorsortieren | `wirklichkeitsdaten-beschaffung-steuern` |
| Datensilos wie Bauwerksregister, PMS/BMS, EPING-nahe Planungsdaten, Bestandspläne, BIM, Nachträge, Kosten, Bauzeiten, Behördenfeedback, Normen, Klima-/Umweltdaten oder Rechtsprechung sollen in eine gemeinsame Fachsprache übersetzt werden | `wirklichkeitsdaten-beschaffung-steuern` |
| Vergabestelle will nicht nur den niedrigsten Preis, sondern das beste Auftragsergebnis | `bestangebot-durchsetzen` |
| Zuschlagskriterien oder Matrix sind noch offen | `10-zuschlagsmatrix-aufbauen` |
| Preis, Qualität, Tempo oder Lebenszykluskosten müssen gewichtet werden | `06-eignungs-und-zuschlagskriterien` |
| Rüge behauptet Preisautomatismus, Scheinqualität oder verzerrte Formel | `22-ruegeerwiderung` und danach `23-stellungnahme-vergabekammer` |
| Billigangebot wirkt unrealistisch | `14-aufklaerung-unangemessen-niedrige-preise` |

## Rechtsprechungsfeste Sofortweichen

| Sichtbarer Sachverhalt | Sofort prüfen | Output |
|---|---|---|
| Preis soll allein entscheiden | § 127 GWB, § 58 VgV; Sonderregel prüfen; EuGH C-769/23 Mara schafft kein allgemeines Verbot | Rechtsgrund- und Bestwertungsvermerk: zulässige Nur-Preis-Wahl oder Qualitäts-/Tempo-/LZK-Matrix |
| LV nennt Material, Hersteller, proprietäre Schnittstelle oder fixes Rückgabeformat | § 31 VgV; EuGH C-424/23 DYKA Plastics | LV-Reparaturliste mit oder-gleichwertig, Sachgrund und Format-Roundtrip |
| Vergabestelle will ohne Bekanntmachung vergeben | § 14 VgV, § 135 GWB; EuGH C-578/23 | Lock-in- und Marktsuchevermerk mit Alternativenprüfung |
| Niedrigstes Angebot wirkt unauskömmlich | § 60 VgV; BGH X ZB 10/16 | Aufklärungsanforderung, Geheimnisschutznotiz, Wertungsfolge |
| Rüge/VK/OLG oder Akteneinsicht droht | §§ 160, 165, 169, 171 GWB; Antea/Varec | Fristenampel, Schwärzungsmatrix, Verteidigungslinie |

## Direkt-Routing Legacy-IT

| Lage | Primärer Skill |
|---|---|
| Daten kommen aus SAP, ERP, AVA, DMS, SharePoint, E-Mail, SFTP, API, OData, IDoc oder MCP | `legacy-systeme-integration` |
| Daten kommen aus Bauwerksregistern, PMS/BMS, Planungsdaten, Bestandsplänen, BIM/Fachmodellen, Kosten-/Nachtragsdaten, Genehmigungsplattformen, Netzdaten, Klima-/Umweltdaten, Normen oder Rechtsprechung | zuerst `legacy-systeme-integration`, dann `wirklichkeitsdaten-beschaffung-steuern` |
| Vergabeunterlagen oder LV müssen aus Altsystemen bereitgestellt werden | `vergabeunterlagen-lv-datenformate-bereitstellen` |
| Bekanntmachung, eForms, TED, DVAL, CPV, Unterlagenlink oder Fristen der Veröffentlichung müssen geprüft werden | `eforms-ted-bekanntmachung-check`, danach bei Fehlern `bekanntmachung-berichtigung-und-upload-routing` |
| Berichtigung oder Bekanntmachung muss in TED, DVAL, Portal oder DMS zurückgespielt werden | `bekanntmachung-berichtigung-und-upload-routing` |
| Es gibt mehrere Quellsysteme und Zielsysteme | zuerst `legacy-systeme-integration`, danach passendes Fachmodul |

## Direkt-Routing Verfahrensvorbereitung

| Lage | Primärer Skill |
|---|---|
| Markt, Anbieterfeld, technische Lösung oder Vorbefassung muss vor Veröffentlichung geklärt werden | `markterkundung-und-vorbefassung` |
| Lose, Bündelung, Mittelstandsschutz, regionale Zuschnitte oder Skaleneffekte sind streitig | `losbildung-mittelstandsfoerderung` |
| Bieterfrage, Klarstellung, Fristverlängerung oder Antwortlog steht an | `bieterfragen-antworten-management` |
| Rahmenvereinbarung, Abruf oder Miniwettbewerb ist geplant | `rahmenvereinbarung-abrufe-mini-wettbewerb` |
| Inhouse, interkommunale Zusammenarbeit oder beauftragte Stelle wird erwogen | `inhouse-interkommunal` |
| Bedarf aus Wirklichkeitsdaten soll in LV/GAEB/XML/Excel/PDF oder eine Ausschreibungsstudio-Vorlage fließen | `vergabeunterlagen-lv-datenformate-bereitstellen` |

## Direkt-Routing Sonderregime

| Lage | Primärer Skill |
|---|---|
| Unterschwelle, Landeswertgrenze, Direktauftrag oder Haushaltsvergaberecht | `uvgo-unterschwellenvergabe` und `uvgo-fristen-form-und-zustaendigkeit` |
| Sektorenauftraggeber Energie, Wasser, Verkehr oder Post | `sektorenvergabe-sektvo` und bei Aktenlücken `sektvo-dokumentenmatrix-und-lueckenliste` |
| Konzession, Betriebsrisiko, Laufzeit oder Konzessionswert | `konzessionsvergabe-konzvgv` und `konzession-formular-portal-und-einreichung` |
| Bauleistung, Gewerke, VOB/A oder Bauzeitenkoordination | `vob-a-bauvergabe` und `vertiefung-vob-a-bauvergabe` |
| Fördermittel, Nebenbestimmungen, Rückforderung oder Zuwendungsprüfung | `foerdermittelvergabe-rueckforderung` |

## Direkt-Routing Ausschluss, Register und Compliance

| Lage | Primärer Skill |
|---|---|
| Wettbewerbsregister, Selbstreinigung, Vergabesperre oder Registerabfrage | `wettbewerbsregister-abfrage-selbstreinigung` |
| Korruption, Kartellabrede, Interessenkonflikt oder zwingender Ausschlussgrund | `vergaberecht-anti-korruption-paragraf-123-gwb` und `12-ausschlussgruende-pruefen` |
| Fakultativer Ausschluss, Schlechtleistung, Interessenkonflikt oder Integrität | `ausschluss-bieter-paragraf-124-gwb` |
| Datenschutz, Bieterdaten, Geschäftsgeheimnis oder Akteneinsicht | `30-datenschutz-bieterdaten` und `26-akteneinsicht-vergabekammer` |

## Direkt-Routing Technik, Cloud und Nachhaltigkeit

| Lage | Primärer Skill |
|---|---|
| KI-, Cloud-, Daten-, IT-Sicherheits- oder KRITIS-Anforderung | `ki-beschaffung-ai-act-daten-cloud` und `it-sicherheits-vergabe-bsi-it-sig-2` |
| Nachhaltigkeit, Tariftreue, Lieferketten, CBAM, Klima oder Umweltauflage | `nachhaltigkeit-tariftreue-lksg-cbam` |
| Technische Normen, DIN, Eurocodes, Schnittstellen oder Produktneutralität | `leistungsbeschreibung-neutralitaet-funktional` |
| Mehrere Behörden-, Bau-, Netz- oder Umweltdatenquellen müssen als Szenario gegeneinander gerechnet werden | `wirklichkeitsdaten-beschaffung-steuern` |

## Vergaberechtliches Routing (Schwellenwerte & Rechtswege)

- Oberhalb EU-Schwellenwert (§ 106 GWB; 2026/2027: VO (EU) 2025/2152 klassisch, 2025/2150 Sektoren, 2025/2151 Konzessionen, 2025/2487 Verteidigung/Sicherheit) — GWB-Vergaberecht: Rüge (§ 160 Abs. 3 GWB) → Nachprüfungsantrag Vergabekammer (§ 161 GWB) → sofortige Beschwerde OLG-Vergabesenat (§ 171 GWB).
- Unterhalb EU-Schwellenwert — kein Nachprüfungsverfahren nach §§ 155 ff. GWB; Einführungserlass, Landesrecht, besondere Prüfstellen, Informations- und Wartepflichten sowie zivil- oder verwaltungsgerichtlicher Eilrechtsschutz fallbezogen bestimmen.
- Sektoren (Energie, Wasser, Verkehr): SektVO; Liefer-/Dienstleistungsschwelle 2026/2027 EUR 432000.
- Konzessionen: KonzVgV; Schwellenwert 2026/2027 EUR 5404000.
- Verteidigung/Sicherheit: VSVgV.
- Verfahrensarten (§ 119 GWB): offen, nicht-offen, Verhandlung, wettbewerblicher Dialog, Innovationspartnerschaft.
- De-facto-Vergabe: § 135 Abs. 2 GWB — 30 Kalendertage nur nach qualifizierter Information mit Gründen oder inhaltlich ausreichender EU-Auftragsvergabebekanntmachung; spätestens sechs Monate nach Vertragsschluss.
- Schadensersatz nach Zuschlag: § 181 GWB für nachgewiesene Angebots- und Teilnahmekosten bei beeinträchtigter echter Zuschlagschance; weiterreichende BGB-Ansprüche separat prüfen.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.
- Bedienbar schließen: empfohlener Output, Alternativen, Freigabeinhaber, nächste Datei oder nächster Portalschritt.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
