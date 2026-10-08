---
name: workflow-kaltstart-und-routing
description: 'Schnelltriage für ein einzelnes Dokument oder eine konkrete Frage des Bieters: bestimmt Phase, rote Frist, Regime, Fundstelle, Angebotsformat, Qualitätsvorsprung, Ausschluss- oder Rechtsschutzpfad und nächsten Output. Kein vollständiger Ordnerfall; Ordner, ZIP und Mehrfachfragen übernimmt der Master-Orchestrator.'
---

# Kaltstart und Routing

**Arbeitsname:** Einzelnes Bieterstück rein, belastbare Arbeitsweiche und erster Output raus.

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Aufgabe
Dieser Workflow-Skill führt genau ein Dokument oder eine konkrete Frage in den passenden Angebots- oder Rechtsschutzweg. Er extrahiert Rolle, Phase, Fundstelle, Frist, Angebotsfolge und nächsten Output, ohne den gesamten Angebots- oder Aktenbestand zu inventarisieren.

## Abgrenzung

- Vollständiger Ordner, ZIP, Portal-/Unternehmensexport, mehrere Dokumente oder mehrere verbundene Angebots- und Streitfragen: `vergabe-os-master-orchestrator`.
- Ein Dokument, eine LV-Position, eine Bieterantwort, ein Ausschlussschreiben oder eine konkrete Rechtsfrage: dieser Skill.
- Noch keine Unterlagen, nur Rollen-, Regime- oder Zuständigkeitsorientierung: `einstieg-routing`.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Ein-Dokument-Schnelltriage

1. Dokumenttyp, Vergabestelle, Verfahren, Datum, Version, Zugang und zitierfähige Fundstelle erfassen.
2. Aus dem Dokument Mindestanforderung, Wertungswirkung, Nachweisbedarf, Formvorgabe oder behaupteten Vergabefehler extrahieren.
3. Früheste Angebots-, Frage-, Rüge-, Stillhalte- oder Beschwerdefrist mit Norm, Startpunkt und Beleg bestimmen oder als nicht berechenbar kennzeichnen.
4. Genau eine Arbeitsroute wählen: Angebotsbaustein, Bieterfrage, Nachweis, Rüge, VK-Antrag, OLG-Briefing oder Uploadhandlung.
5. Einen sofort nutzbaren Kernoutput plus höchstens drei gezielte Nachforderungen liefern.

## Bedienlogik

- Starte mit einer Ein-Bildschirm-Lage: Kurzlage, rote Fristen, vorhandene Dateien, offene Lücken, empfohlener Output.
- Biete höchstens drei Output-Optionen an und markiere genau eine Empfehlung.
- Nutze Entscheidungsfragen nur als Weiche: Angebot bauen, Unterlagen klären, Rüge sichern, Zuschlag stoppen, Akteneinsicht erzwingen, Vergleich prüfen.
- Gib bei Datei- oder Portalbezug immer den nächsten Bedienhandlungspunkt aus: Datei prüfen, Angebotsmapping bauen, Freigabe einholen, Upload vorbereiten, Quittung sichern.
- Vermeide Beratungstext ohne Arbeitsprodukt. Jeder Abschnitt muss zu Angebotspaket, Matrix, Checkliste, Rüge, VK-Antrag oder Uploadpaket führen.

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Fristenampel, Dokumentenmatrix und Output-Weiche in derselben Antwort liefern.
4. Passende Spezialskills aus diesem Plugin vorschlagen und mit einem Satz begründen.
5. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste, Rüge, Angebotsbaustein oder Uploadpaket.
6. Mit einem Nutzungscheck schließen: Kann der Bieter jetzt anbieten, nachfragen, rügen, hochladen, unterschreiben oder eskalieren?

## Direkt-Routing Aktenstart

| Lage | Primärer Skill |
|---|---|
| ZIP, PDF-Bündel, E-Mails, Screenshots oder Portalexporte liegen ungeordnet vor | `dokumente-intake` |
| Vergabeunterlagen, Wertungsvermerk, Angebotsauszüge oder Portalnachweise fehlen | `unterlagen-luecken` |
| Aus Aktenlücken soll eine Arbeitsliste für Unternehmen oder Kanzlei entstehen | `workflow-unterlagen-lueckenliste` |
| Bekanntmachung, Unterlagen, LV, GAEB, XML, Excel oder PDF müssen zuerst gelesen werden | `unterlagen-und-lv-datenformate-auslesen` |
| Angebotsdaten stammen aus SAP, ERP, CRM, AVA, DMS, SharePoint, E-Mail, SFTP, API, OData, IDoc oder MCP | `legacy-systeme-integration` |

## Direkt-Routing Bestwertung

| Lage | Primärer Skill |
|---|---|
| Bieter ist teurer, aber fachlich stärker | `qualitaetsvorsprung-nachweisen` |
| Bewertungsmatrix enthält Qualitäts-, Tempo-, Personal- oder Servicepunkte | `13-konzeptionelle-anlagen` |
| Preisblatt oder LV muss im vorgegebenen Format abgegeben werden | `angebot-in-vorgegebenem-format-erstellen` |
| Unterlagen entwerten Qualitätsvorteile durch Preisformel oder Scheinqualität | `21-ruegeschreiben-erstellen` |
| Eigenes Angebot ist sehr günstig und erklärungsbedürftig | `18-aufklaerung-niedriges-angebot-paragraf-60` |

## Rechtsprechungsfeste Sofortweichen

| Sichtbarer Sachverhalt | Sofort prüfen | Output |
|---|---|---|
| Bieter ist teurer, aber fachlich stärker | § 127 GWB, § 58 VgV und veröffentlichte Matrix; Mara schafft keine neuen Kriterien | Punktebrücke mit bekannt gemachter Punktestufe, Nachweis, Mehrwert, Preisnachteil und Wertungsauswirkung |
| Unterlage, LV, GAEB/XML/Excel/PDF oder Portalpflichtfeld blockiert Gleichwertigkeit | § 31 VgV; EuGH C-424/23 DYKA Plastics | Bieterfrage oder Rüge mit Fundstelle, Alternativlösung und Berichtigungsantrag |
| Billigkonkurrent gewinnt | § 60 VgV; BGH X ZB 10/16 | Aufklärungsangriff mit Preisabstand, Leistungsrisiko und Zuschlagschance |
| Ausschluss, Nachforderung oder Selbstreinigung | §§ 123 bis 125 GWB, § 56 VgV; Vossloh Laeis, Manova | Nachweismatrix, Antwortentwurf und Selbstreinigungsdossier |
| Bietergemeinschaft mit Problemmitglied | Schlussanträge GA Kokott C-268/25, nicht Urteil | BG-Krisenpfad: Mitglied, Kenntnis, Zurechnung, Austausch ohne wesentliche Änderung |

## Direkt-Routing Bieterfrage vor Rüge

| Lage | Primärer Skill |
|---|---|
| Unterlage ist unklar, widersprüchlich oder unvollständig, aber noch klärbar | `bieterfragen-antworten-management` |
| Portalantwort fehlt, Antwort ist widersprüchlich oder Fristverlängerung ist möglich | `bieterfragen-antworten-management` |
| Antwort der Vergabestelle bestätigt einen Vergabefehler oder die Frist läuft | `21-ruegeschreiben-erstellen` |
| Rüge wurde nicht abgeholfen oder 15-Kalendertage-Frist läuft | `nachpruefungsantrag-powerdraft` oder `nachpruefungsverfahren-vk` |

## Direkt-Routing Legacy-IT

| Lage | Primärer Skill |
|---|---|
| Angebotsdaten kommen aus SAP, ERP, CRM, AVA, DMS, SharePoint, E-Mail, SFTP, API, OData, IDoc oder MCP | `legacy-systeme-integration` |
| Vergabeunterlagen oder LV müssen aus Altsystemen gelesen werden | `unterlagen-und-lv-datenformate-auslesen` |
| Angebot, Nachweise oder Rüge müssen in Portal, DMS oder Kundensystem exportiert werden | `angebot-in-vorgegebenem-format-erstellen` |
| Es gibt mehrere Quellsysteme und Zielsysteme | zuerst `legacy-systeme-integration`, danach passendes Fachmodul |

## Direkt-Routing Rechtsschutz-Sonderlagen

| Lage | Primärer Skill |
|---|---|
| Auftrag ist schon vergeben, Leistung läuft, Vertrag wurde ohne Bekanntmachung geschlossen oder Interimsauftrag bekannt | `de-facto-vergabe-135-gwb-fristen` |
| Nachtrag, Verlängerung, Auftragnehmerwechsel oder wesentliche Vertragsänderung verdrängt Wettbewerb | `de-facto-vergabe-klage` |
| Angebotsöffnung, Preisblatt, Signatur, Dateiformat oder formaler Ausschluss ist streitig | `angebotsoeffnung-formfehler-preisblatt` |
| VK-Termin, Hinweise der Kammer oder Vergleichsgespräch stehen an | `vergabekammer-termin-simulation` und `vergleichsverhandlung-strategie` |
| Mehrparteienlage mit Beigeladenem, Zuschlagsprätendenten oder Nachunternehmer | `verg-mehrparteien-konflikt-und-interessen` |
| Wettbewerbsregister, Vergabesperre, Korruption, Selbstreinigung oder Compliance-Nachweis betroffen | `wettbewerbsregister-abfrage-selbstreinigung` und `vergabesperre-korruption-selbstreinigung` |

## Direkt-Routing Sonderregime

| Lage | Primärer Skill |
|---|---|
| Unterschwelle, Landeswertgrenze, Direktauftrag oder zivilgerichtlicher Rechtsschutz | `uvgo-fristen-form-und-zustaendigkeit` |
| Sektorenauftraggeber Energie, Wasser, Verkehr oder Post | `sektvo-dokumentenmatrix-und-lueckenliste` |
| Konzession, Betriebsrisiko, Laufzeit oder Konzessionswert streitig | `konzvgv-risikoampel-und-gegenargumente` |
| Betrag, Lose, Optionen, Laufzeit oder Rahmenvereinbarung bestimmen Schwellenwert oder Zuständigkeit | zuerst `schnittstelle-zahlen-schwellen-und-berechnung`, danach `schwellenwerte-2026-2027-livecheck` |

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
