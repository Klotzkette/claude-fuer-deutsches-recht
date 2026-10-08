# Systemexporte, Beweiszugang und Beweiskette des Konkurrenten

Diese Referenz laden, wenn ein Konkurrent Portalstände, eigene Angebotsdaten, öffentliche Bekanntmachungen, Akteneinsichtsauszüge, LV-/Preisdateien, E-Mails, Logs oder sonstige Systemexporte für Rüge, Vergabekammer oder OLG verwenden will. Sie schafft keine Zugriffsrechte auf fremde Systeme.

## Vier unverhandelbare Regeln

1. **Zugang vor Inhalt:** Für jeden Beleg zuerst klären, ob er öffentlich, aus eigener Sphäre, im Verfahren offengelegt oder sonst rechtmäßig erlangt wurde. Kein Zugriff auf fremde interne Systeme ohne Befugnis.
2. **Original vor Lesefassung:** Originaldatei und Metadaten unverändert sichern. OCR, Konvertierung, Tabellenbereinigung und Screenshot sind abgeleitete Arbeitsstände.
3. **Tatsache vor Schlussfolgerung:** Ein Portalzeitstempel belegt einen Portalvorgang, nicht automatisch die Rechtsverletzung. Angriff, Norm, Kausalität und Zuschlagschance gesondert begründen.
4. **Geheimnisschutz mitdenken:** Eigenes Geheimnis, mögliches fremdes Geheimnis, notwendige Offenlegung und Schwärzung bei jeder Anlage kennzeichnen.

## Zulässige Quellenzonen

| Zone | Beispiele | Verwendung |
|---|---|---|
| A Eigene Sphäre | eigenes ERP/CRM/AVA/DMS, Angebot, Portalaccount, Uploadlog, Bieterfrage, Rüge, E-Mail | unmittelbar sichern und als eigenen Beleg anbieten |
| B Öffentlich | TED/eForms, DVAL, Vergabeportal ohne Zugangshürde, amtliche Register, Gesetze, Rechtsprechung | URL, Abrufzeit, Notice-/Dokument-ID und Snapshot sichern |
| C Verfahrenszugang | Vergabeunterlagen, Portalnachrichten, § 134-Schreiben, Akteneinsicht nach § 165 GWB, VK-/OLG-Verfügung | Nutzungsumfang, Schwärzung, Aktenstelle und Verfahrenszweck beachten |
| D Dritte mit Befugnis | Sachverständiger, Nachunternehmer, Referenzgeber, Zeuge, befugter Datenhalter | Herkunft, Einwilligung/Befugnis und Aussageumfang dokumentieren |
| E Nur Indiz | Marktpreis, öffentliche Produktdaten, eigene Messung, auffällige Dateidifferenz | als Indiz kennzeichnen und Akteneinsicht/Ermittlung konkret beantragen |
| X Unzulässig oder ungeklärt | fremdes Behördenkonto, fremdes Bietersystem, nicht autorisierter Datenbankzugang | nicht abrufen, nicht verwenden; rechtmäßigen Beweisweg suchen |

## Typische System- und Beweisfamilien

| Quelle | möglicher Tatsachenkern | Angriffspfad | Gegenprüfung |
|---|---|---|---|
| TED/eForms/DVAL/Portal | veröffentlichter Text, Frist, Link, Version, Berichtigung | Bekanntmachung, Unterlagenzugang, § 135 GWB | veröffentlichte gegen interne Version, Abrufbarkeit, Zeitbezug |
| eigener Portalaccount/Uploadlog | Download, Nachricht, Fehler, Upload, Serverzeit, Quittung | Zugangsstörung, Frist, Gleichbehandlung, Abgabe | lokaler Fehler, Nutzerrolle, vollständiger Log, Supportticket |
| GAEB/XML/Excel/PDF | OZ, Menge, Einheit, Pflichtfeld, Sperre, Widerspruch | Produkt-/Formatsperre, Vergleichbarkeit, Transparenz | Leitformat, Lesefassung, Schema, Berichtigung, Roundtrip |
| eigene SAP-/ERP-/AVA-Kalkulation | eigener Preis, Menge, Vergleichsaufwand, technische Alternative | Preis-/Kausalitätsdarlegung, Gleichwertigkeitsangebot | Geschäftsgeheimnis, Leistungsidentität, Preisstand |
| Akteneinsicht/Wertungsmatrix | Kriterien, Punktzahl, Begründung, Aufklärung, Konkurrentennachweis | Wertungs-, Eignungs-, Preis- oder Dokumentationsangriff | Schwärzung, Begründungsersatz, Einzelfallbezug |
| Bestands-/Schnittstellendaten | vorhandene Architektur, Kompatibilität, Migration, Ausfallrisiko | Produktbindung, Losbildung, Lock-in | Aktualität, Fachfreigabe, realistische Alternative |
| DMS/E-Mail/Support | Version, Zugang, Antwort, Abhilfe, Zustellung | Kenntnis, Rügefrist, Verfahrensfehler | vollständiger Header/Verlauf, Zustellnachweis |

## Kanonischer Beweisdaten-Umschlag

| Feld | Inhalt |
|---|---|
| Herkunftszone | A, B, C, D, E oder X; Rechts-/Zugangsgrund |
| Quellsystem | System, Portal, Modul, Nutzerrolle, Datenhalter, Exportweg |
| Beweisobjekt | Bekanntmachung, Unterlage, LV-Position, Preis, Nachricht, Upload, Wertung oder Vertrag |
| Schlüssel | Vergabenummer, TED-/Notice-/Portal-ID, Los, OZ, Dokument-ID, Nachrichten-ID |
| Zeitbezug | Ereigniszeit, Serverzeit, Exportzeit, Zeitzone, gültig ab/bis |
| Originalschutz | Pfad/URL/Endpunkt, Format, Version, SHA-256, Signatur/Siegel |
| Ableitung | OCR, Konvertierung, Filter, Berechnung, Vergleich, manuelle Markierung |
| Tatsachenkern | Was belegt die Quelle unmittelbar, ohne rechtliche Wertung? |
| Angriff | Norm, behaupteter Fehler, Kausalität, Zuschlagschance, begehrte Abhilfe |
| Quellenstatus | gesichert, bestritten, nur Indiz, Akteneinsicht nötig, unzulässig/ungeklärt |
| Geheimnisschutz | eigenes/fremdes Geheimnis, Schwärzung, Ersatzbegründung, Zugriffskreis |
| Verfahrensziel | Rüge, VK-Anlage, Akteneinsicht, Eilantrag, OLG-Anlage, Vergleich |

## Beweiskette

1. Original erfassen: Quelle, Zugang, Pfad/URL, Datum, Zeitzone, Version und Hash.
2. Arbeitskopie bilden: OCR, PDF-Lesefassung, Tabellenansicht oder markierter Auszug; Transformation protokollieren.
3. Tatsachenkern in einem neutralen Satz formulieren.
4. Gegenhypothese bilden: Welche harmlose Erklärung könnte die Vergabestelle oder der Zuschlagsprätendent geben?
5. Angriff und Norm zuordnen.
6. Kausalität und plausible Zuschlagschance darlegen.
7. Fehlenden Beleg als genaues Akteneinsichts- oder Ermittlungsziel benennen.
8. Anlage mit Dateiname, Seiten-/Zell-/OZ-Fundstelle, Hash und Geheimnisschutz bilden.
9. Übermittlung erst nach Freigabe; Empfangs- oder Gerichtsquittung sichern.

## Rechtsprechungs- und Normengates

| Gate | Angriff und Grenze |
|---|---|
| § 31 VgV; EuGH, 16.04.2026, C-568/24, *Sof Medica*, ECLI:EU:C:2026:305 | Bei Typ-, System-, Größen- oder Schnittstellenvorgabe fragen, ob sie unvermeidbar aus dem Auftragsgegenstand folgt. Fehlt `oder gleichwertig`, funktionale Alternative und konkrete Wettbewerbswirkung belegen. |
| EuGH, 16.01.2025, C-424/23, *DYKA Plastics* | Nicht nur Markenwort suchen: auch Schema, Pflichtfeld, API, Dateiformat oder technische Referenz kann Gleichwertigkeit faktisch sperren. |
| OLG Düsseldorf, 10.07.2024, Verg 2/24 | Bestandskompatibilität und Systemsicherheit können die Vorgabe verteidigen. Angriff braucht daher belastbare Alternative, Migrationspfad und Widerlegung der behaupteten Schnittstellen-/Gewährleistungsrisiken. |
| § 41 VgV; OLG Düsseldorf, 13.05.2019, Verg 47/18 | Unvollständiger, verstreuter oder nur auf Anforderung erreichbarer Unterlagenbestand kann den Zugang verletzen. Versionen, Klickweg und fehlende Anlage beweissicher festhalten. |
| EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, ECLI:EU:C:2025:523 | Unmittelbar EU-Eigenvergabe nach der EU-Haushaltsordnung; im deutschen Verfahren Integritätsanker neben § 53 VgV und Portalvorgabe. Für den Angriff beweisen, was nach dem konkreten Übermittlungsweg hochzuladen war und tatsächlich angenommen wurde. |
| § 8 VgV; OLG Düsseldorf, 24.03.2021, Verg 34/20 | Punktwerte ohne konkrete Gründe und dokumentierte Antworten tragen eine qualitative Wertung nicht. Akteneinsicht auf Eingabedaten, Einzelgründe, Quervergleich und Gremienaufzeichnungen richten. |
| OLG Düsseldorf, 12.06.2024, Verg 36/23 | Bei internen Vorgängen oder Konkurrenzangeboten darf der Bieter wegen begrenzten Einblicks aus redlich für wahrscheinlich gehaltenen Tatsachen vortragen; bloße Behauptung ohne Tatsachenkern und Quelle reicht nicht. |
| § 165 GWB; EuGH C-54/21 *Antea Polska* | Fehlender Zugriff wird nicht durch Spekulation ersetzt. Entscheidungserhebliches Akteneinsichtsziel, Geheimnisschutz und möglichen Begründungsersatz konkret benennen. |

## Beweiswert und Angriffstiefe

| Status | Formulierung | Nächster Schritt |
|---|---|---|
| gesichert | Quelle belegt den Tatsachenkern unmittelbar | Anlage bilden und Kausalität ausarbeiten |
| bestritten | Original vorhanden, Bedeutung oder Zuordnung streitig | Gegenhypothese, Zeuge/Sachverständiger, ergänzende Quelle |
| Indiz | Quelle macht Fehler plausibel, beweist ihn aber nicht vollständig | konkrete Akteneinsicht/Ermittlung beantragen |
| Lücke | entscheidendes Feld fehlt oder ist geschwärzt | § 165-Antrag und Begründungsersatz verlangen |
| unzulässig/ungeklärt | Herkunft oder Zugriffsrecht nicht tragfähig | nicht verwenden; rechtmäßige Ersatzquelle suchen |

## Stoppsignale

- Zugriff auf fremde interne Systeme oder Konten wäre nötig.
- Screenshot liegt ohne URL, Zeit, Kontext oder Originalexport vor.
- OCR-/Excel-Bereinigung wurde nicht protokolliert.
- Behauptung geht weiter als der unmittelbare Tatsachenkern.
- Geschäftsgeheimnis wird für den Angriff nicht benötigt oder ist nicht geschützt.
- Portal-/Gerichtsversand ist nicht ausdrücklich freigegeben.

## Pflichtoutput

- Herkunftszonen- und Beweisinventar.
- Original-/Arbeitskopien- und Hashmanifest.
- Tatsachenkern-, Gegenhypothesen- und Angriffsmatrix.
- Akteneinsichts- und Ermittlungsziele.
- Anlagenverzeichnis mit Geheimnisschutz.
- Ausgefüllte Vorlage [`beweiskette-systemexport.md`](../assets/templates/beweiskette-systemexport.md).
