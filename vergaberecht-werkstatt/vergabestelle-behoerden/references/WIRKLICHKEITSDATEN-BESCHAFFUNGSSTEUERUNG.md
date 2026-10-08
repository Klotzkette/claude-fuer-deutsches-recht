# Wirklichkeitsdaten für Beschaffungssteuerung

Diese Referenz laden, wenn eine Vergabestelle nicht nur ein Einzelverfahren abarbeiten will, sondern vorhandene Datenquellen nutzen soll, um Bedarf, Bündelung, Priorisierung, Ausschreibung, Zuschlagskriterien und Ressourcensteuerung belastbarer zu machen.

## Leitgedanke

Die Vergabestelle ändert nicht das Vergaberecht. Sie nutzt bessere Daten, eine gemeinsame Fachsprache und nachvollziehbare Szenarien, damit das geltende Vergaberecht besser angewandt wird: schneller ausschreiben, Qualitäts- und Zeitkriterien rechtssicher einsetzen, Ressourcen bündeln und Entscheidungen aktenfest begründen.

## Quellfamilien

| Quellfamilie | Beispiele | Zweck im Vergabeverfahren |
|---|---|---|
| Bestands- und Zustandsdaten | Bauwerksregister, Anlagenkataster, SIB-/Straßenbauwerksdaten, Prüfberichte, Zustandsnoten, Schadensbilder | Bedarf, Dringlichkeit, Losbildung und Priorisierung aus realen Objektzuständen ableiten |
| Planungs- und Betriebsdaten | PMS/BMS, EPING-ähnliche Planungsdaten, Bauzeiten, Arbeitsprogramme, Korridore, Sperrpausen, Nutzungsfenster | Termine, Sequenzierung, Ausführungsfristen und Bündelung plausibilisieren |
| Plan- und Modelldaten | Bestandspläne, as-built-Unterlagen, BIM-Modelle, Fachmodelle, AwF-110-/OKSTRA-nahe Daten, Nachrechnungen | LV-Positionen, Mengen, Schnittstellen, Risiken, Tragfähigkeit und technische Alternativen prüfen |
| Kosten- und Nachtragsdaten | historische Kosten, Nachträge, Mehrkosten, Vertragsänderungen, Mengenabweichungen, CAPEX-/OPEX-Annahmen | Auftragswertschätzung, Risikozuschläge, Preisformeln, ÖPP-Vorprüfung und Nachtragsprävention stützen |
| Behörden- und Prüfungsfeedback | Stellungnahmen, Prüfberichte, Genehmigungsauflagen, Fachbereichsrückmeldungen, Rechnungsprüfung, Aufsicht | Nebenbestimmungen, Eignungsanforderungen, Leistungsbeschreibung, Zeitplan und Streitfestigkeit absichern |
| Vergabe- und Marktdaten | TED, Bundes- und Landesportale, Vergabeplattformen, frühere Vergaben, Anbieterprofile, Marktfeedback | Bietermarkt, Bündelungsfähigkeit, Direktauftragsschwellen, Eignung, Wettbewerb und beschleunigte Beauftragung prüfen |
| Genehmigungs- und Plattformdaten | Fachplanungsportale, Genehmigungsplattformen, Planfeststellungsdaten, Behördenpostfächer | Abhängigkeiten, Nebenbestimmungen, Veröffentlichungszeitpunkt und Uploadpakete steuern |
| Netze, Mobilität, Klima und Umwelt | Netzdaten, Schutzgebiete, Pegel, Klimadaten, Umweltauflagen, Tragfähigkeits- und Korridordaten | Standort-, Bauzeit-, Genehmigungs-, Nachhaltigkeits-, Mobilitäts- und Risikoaspekte berücksichtigen |
| Regeln und Recht | technische Normen, DIN 1076, Eurocodes, Gesetze, Rechtsprechung, VK-/OLG-Entscheidungen | Vergaberechtliche Zulässigkeit, technische Mindeststandards, Wertungsspielräume und Streitfestigkeit sichern |

Quellen bleiben führend. Die Auswertung ersetzt keine Fachentscheidung, keine Haushaltsentscheidung und keine vergaberechtliche Freigabe.

## Feldautorität und Verwendungsgrenze

Nicht jedes richtige Datum darf jede vergaberechtliche Entscheidung tragen. Für jedes Feld sind Quelle, Zeitbezug, Einheit, Fachfreigabe und zulässiger Rechtszweck festzulegen.

| Datenbefund | zulässige Erstverwendung | notwendige Brücke | unzulässige Abkürzung |
|---|---|---|---|
| Zustandsnote, Schaden, Prüfbericht | Bedarf und Priorisierung | Objektbezug, Prüfdatum, Ausfallwirkung, Fachfreigabe | alleinige Begründung äußerster Dringlichkeit |
| Budget, BANF oder Kostenstelle | Mittel- und Bedarfsbezug | Gesamtvergütung, Optionen, Laufzeit, Lose, Preisbasis | unmittelbare Schwellenwert- oder Verfahrensentscheidung |
| historische Kosten und Nachträge | Vergleichs- und Risikodaten | Leistungsidentität, Index, Marktstand, Ausreißerprüfung | ungeprüfte aktuelle Auftragswertschätzung |
| BIM-/Planmenge | LV- und Schnittstellenvorbereitung | Modellstand, Einheit, Kollisionsprüfung, Fachfreigabe | vertragliche Menge ohne Planstandsprüfung |
| frühere Anbieterleistung oder Behördenfeedback | Marktkenntnis und Vertragscontrolling | transparentes, bekannt gemachtes und auftragsbezogenes Kriterium | verdeckte Eignungs- oder Zuschlagswertung |
| Systempunktzahl oder Prognose | Rechen- und Szenariohilfe | Eingabebeleg, Kriterienbezug, Begründung, Quervergleich | automatische Zuschlagsentscheidung |

Bei technischen Feldern und Rückgaben zusätzlich [`LEGACY-SYSTEME-INTEGRATION.md`](LEGACY-SYSTEME-INTEGRATION.md) laden. Dort stehen Datenumschlag, Feldautorität, Konfliktregel und Rückschreibvertrag.

## Gemeinsame Fachsprache

Technische Daten müssen in Vergabebegriffe übersetzt werden. Jede Zeile braucht eine prüffähige Verbindung zwischen Quelle, Objekt, fachlicher Aussage und Vergabefolge.

| Technischer Befund | Vergaberechtliche Bedeutung | Möglicher Output |
|---|---|---|
| Bauwerk mit schlechtem Zustand, hoher Ausfallwirkung und naher Sperrpausenlage | dringender Bedarf, Priorisierung, ggf Bündelung mit ähnlichen Objekten | Bedarfsvermerk, Priorisierungsmatrix |
| wiederkehrende Schadensbilder und Nachträge in ähnlichen Leistungen | präzisere Leistungsbeschreibung, Risiko- und Schnittstellenregelung | LV-Check, Vertrags- und Nachtragsprävention |
| stabile Marktdaten für gleichartige Leistungen | Los- und Bündelungsprüfung, Skaleneffekte, Rahmenvereinbarung | Losvermerk, Rahmenvertragsprüfung |
| Klimarisiko, Schutzgebiet oder Genehmigungsauflage | Ausführungszeit, Eignung, technische Mindestanforderung oder Nachhaltigkeitskriterium | Kriterienvermerk, Genehmigungsmatrix |
| hohes Termin- oder Verfügbarkeitsrisiko | Qualitäts-, Tempo-, Servicelevel- oder Ausfallreservekriterium | Zuschlagsmatrix, Bestwertungs-Stresstest |

Jede Übersetzung erhält eine Entscheidungsbrücke: `Quellfeld -> gesicherte Tatsache -> Annahme/Transformation -> Norm -> Behördenentscheidung -> Aktenbeleg`. Fehlt ein Glied, darf der Befund nur als offene Prüfspur erscheinen.

## Vereinheitlichungs- und Entscheidungsebene

Die Vergabestelle braucht zwei getrennte Arbeitsschichten. Erst werden Daten aus Silos in eine gemeinsame Fachsprache gebracht. Danach wird daraus eine belastbare Behördenentscheidung abgeleitet.

| Ebene | Leitfrage | Pflichtfelder | Typischer Output |
|---|---|---|---|
| Vereinheitlichung | Sprechen Quellen über dasselbe Objekt, denselben Schaden, denselben Korridor, dieselbe Leistung oder dasselbe Budget? | Quelle, Schlüssel, Objekt, Bauteil, Prüfung, Tragfähigkeit, Arbeitsblock, Korridor, Niederlassung, Budget, Version, Datenhalter | Quelleninventar, Datenqualitätsmatrix, Dubletten-/Widerspruchsliste |
| Entscheidung | Welche vergaberechtliche Folge hat der Befund? | Priorität, Bündelung, Sequenz, Auftragswert, Los, LV-Position, Eignung, Zuschlagskriterium, Risiko, Freigabe, Aktenstelle | Bedarfsvermerk, Losvermerk, Kriterienvermerk, Uploadpaket, Vergabeaktenvermerk |

## Fach-Applets

Diese Applets nicht als Produktwerbung, sondern als Arbeitsflächen der Vergabestelle verstehen.

| Applet | Eingaben | Vergaberechtliche Leistung | Output |
|---|---|---|---|
| Portfolio und Planung | Zustand, Ausfallwirkung, Korridor, Budget, Bauzeit, Genehmigung | Bedarfe priorisieren, bündeln, sequenzieren und Haushaltsmittel plausibel zuweisen | Portfolioampel, Bündelungs- und Budgetvermerk |
| Beschleunigte Beauftragung | Auftragswert, Landeswertgrenze, Binnenmarktrelevanz, Anbieterfeld, Dringlichkeit | Direktauftrag, Verhandlungsverfahren, Rahmenabruf oder Interimsbedarf rechtssicher prüfen | Verfahrenswahlvermerk, Marktnotiz, Upload-/Dokumentationspaket |
| Vergaberechtsnavigation | Regime, Schwelle, Quelle, Risiko, Rechtsprechung, Portalweg | Zulässigkeit, Rügeanfälligkeit und Reparaturpfad markieren | Risikomatrix, Fristenampel, Abhilfe- oder Verteidigungsvermerk |
| Mobilität und Tragfähigkeit | Netz, Brücke, MLC-/Schwerlastdaten, Sperrpausen, Konvoi-/Routenbedarf | Leistungsbeschreibung, Losbildung, Eignung und Ausführungszeit an realer Nutzbarkeit ausrichten | Korridorvermerk, Tragfähigkeitsmatrix, LV-Risikoblatt |
| Ausschreibungsstudio | Bestandsdaten, BIM, LV, Normen, Nachtragsursachen, Rückgabeformate | LV schneller und bieterfreundlich erstellen, GAEB/XML/Excel/PDF-Roundtrip sichern | LV-Vorbereitungsblatt, Formatexport-Check, Bieterfragenprävention |
| ÖPP-/CAPEX-Vorprüfung | Investitionsbedarf, Betriebskosten, Lebenszyklus, Risiken, Bauzeit, Finanzierung | Beschaffungsvariante und Wertungskriterien vorbereiten, ohne Haushaltsentscheidung vorwegzunehmen | Variantenmatrix, Lebenszykluskostenblatt, Gremienvorlage |
| Fertigteil- und Serienlösung | Standardisierbarkeit, Lieferketten, Bauzeit, Normen, Schnittstellen, Wiederholungsbedarf | Zulässige technische Mindestanforderungen und Qualitätswertung für industrielle Vorfertigung prüfen | Gleichwertigkeitscheck, Kriterienvermerk, Schnittstellen-LV |

## Arbeitsprogramm

1. Fragestellung festlegen: Bedarf klären, Portfolio priorisieren, Leistungen bündeln, LV erstellen, Kriterien bauen, Budget verteilen oder Streit verteidigen.
2. Quelleninventar bilden: System, Datenhalter, Zeitraum, Objektbezug, Format, Version, Aktualität, Rechte, Exportweg.
3. Feldautorität und Datenqualität prüfen: führende Quelle, Vollständigkeit, Dubletten, Aktualität, Plausibilität, Messmethode, Einheit, Nullwertlogik, Fachfreigabe, Widersprüche.
4. Gemeinsame Fachsprache bilden: Objekt, Bauteil, Schaden, Prüfung, Arbeitsblock, Korridor, Budget, Los, LV-Position, Eignung, Zuschlagskriterium; Originalschlüssel erhalten.
5. Szenarien rechnen: einzeln vergeben, bündeln, Rahmenvereinbarung, Abruf, Lose, Bauabschnitte, Beschleunigung, Interimsbedarf, Verschiebung.
6. Anbieter- und Marktabgleich: vorhandene Anbieter, regionale Verfügbarkeit, Fachlose, Bündelungsrisiko, Mittelstandsschutz und Direktauftragsgrenzen prüfen.
7. Vergaberechtliche Wirkung ableiten: Bedarf, Schätzung, Losbildung, Verfahrenswahl, Leistungsbeschreibung, Eignung, Zuschlag, Aufklärung, Dokumentation.
8. Kriterien jenseits des Preises belegen: Qualität, Ausführungszeit, Betriebssicherheit, Verfügbarkeit, Nachhaltigkeit, Lebenszykluskosten, Ausfallrisiko. Historische Lieferanten- oder Betriebsdaten nicht als verdecktes Wertungskriterium verwenden.
9. Systemkonflikte auflösen: abweichende Objekt-ID, Version, Einheit, Menge oder Zeit nicht mitteln, sondern Feldautorität, Delta und Auswirkung auf Unterlagen/Fristen dokumentieren.
10. Aktenfest entscheiden: Entscheidungsbrücke, Annahmen, Datenquelle, Fachfreigabe, Szenario, Rechtsfolge, Freigabeinhaber und nächster Schritt dokumentieren.

## Rechtsprechungsgates für datenbasierte Beschaffung

| Entscheidung | konkrete Arbeitsfolge |
|---|---|
| EuGH, 16.04.2026, C-568/24, *Sof Medica*, ECLI:EU:C:2026:305 | Daten dürfen eine detaillierte technische Anforderung begründen. Führt sie aber auf einen Typ oder eine bestimmte Produktion, Gleichwertigkeit eröffnen, sofern die Anforderung nicht unvermeidbar aus dem Auftragsgegenstand folgt. Die Begründung muss belastbar vorhanden sein, auch wenn sie nicht vollständig in den Vergabeunterlagen veröffentlicht werden muss. |
| EuGH, 16.01.2025, C-424/23, *DYKA Plastics* | Material-, Produkt-, Schema- und Schnittstellenanforderung auf ungerechtfertigte Wettbewerbsverengung prüfen. |
| OLG Düsseldorf, 10.07.2024, Verg 2/24 | Gewachsene Infrastruktur, Kompatibilität und Systemsicherheit können eine Produktvorgabe oder Gesamtvergabe rechtfertigen; dafür konkreten Bestands-, Migrations-, Schnittstellen- und Gewährleistungsbefund dokumentieren. |
| OLG Düsseldorf, 13.05.2019, Verg 47/18 | Abgeleitete Pläne, Modelle, technische Lieferbedingungen und Datenanlagen vollständig und direkt über den bekannt gemachten Unterlagenweg bereitstellen. |
| OLG Düsseldorf, 24.03.2021, Verg 34/20 | Automatische Punktwerte, Mittelwerte oder Dashboardanzeigen ersetzen keine dokumentierten qualitativen Gründe und keine Wiedergabe entscheidender Antworten/Eingaben. |
| EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, ECLI:EU:C:2025:523 | Unmittelbar EU-Eigenvergabe; im deutschen Verfahren nur Integritätsanker neben § 53 VgV und Portalvorgabe. Ist ein Upload verlangt, fristgebundene Bieternachweise als unveränderbare Dateien anfordern. |

## Output

- Quellen- und Datenqualitätsmatrix.
- Feldautoritätsmatrix und Entscheidungsbrücken für alle tragenden Datenfelder.
- Priorisierungs- und Bündelungsmatrix mit Skaleneffekten, Losrisiko und Haushaltsbezug.
- Szenariovergleich: Einzelvergabe, gebündelte Vergabe, Rahmenvereinbarung, Abruf, Verschiebung.
- Applet-Dashboard für Portfolio, Beschleunigung, Vergaberechtsnavigation, Mobilität/Tragfähigkeit, Ausschreibungsstudio, ÖPP/CAPEX und Serienlösung.
- LV-Vorbereitungsblatt mit Mengen, Schnittstellen, Risiken, Normen und Nachtragsprävention.
- Bestwertungs-Vermerk mit Qualitäts-, Tempo-, Servicelevel-, Nachhaltigkeits- und Lebenszyklusbelegen.
- Vergabeaktenvermerk mit Quelle, Annahme, Fachfreigabe, Rechtsfolge und nächstem Portalschritt.
