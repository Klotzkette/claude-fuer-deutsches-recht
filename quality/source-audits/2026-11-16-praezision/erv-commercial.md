# Fachprüfung: englische Schriftsätze und elektronischer Rechtsverkehr

## 1. Umfang und Befund

Am 16. November 2026 wurde ausschließlich die Fachquelle `commercial-courts-deutschland/skills/bea-erv-english-pleadings/FACHINHALT.md` inhaltlich neu gefasst. Die ursprüngliche Fassung enthielt handlungsrelevante Fehler; die Überarbeitung ersetzt sie durch eine ausführbare Einreichungskette. Testakten, Dateibestände und fachfremde Module wurden hierbei nicht verändert.

| Alter Befund | Fachliche Korrektur |
| --- | --- |
| „ZPO §§ 184a“ und Englisch nur bei Akzeptanz durch den Spruchkörper | § 184a GVG: Landesverordnung für Spruchkörper/Sachgebiet und gesetzliche Voraussetzungen der Sprachwahl. Gesonderte Regeln für Urkunden, Drittbeteiligte und den BGH nach §§ 184a/184b GVG, § 142 Abs. 3 ZPO. |
| ZIP als Alternative für Anlagensammlungen | PDF nach § 2 Abs. 1 ERVV; nur bei dessen Voraussetzungen zusätzlich TIFF. Kein ZIP-Ersatz. |
| PDF/A angeblich bei vielen Gerichten zwingend | Keine allgemeine PDF/A-Pflicht aus der ERVB 2025. PDF-Formatvorgabe, Soll-Standards und konkrete Bearbeitungseignung getrennt. |
| 100 MB, angebliche Grundlage RAVPV | ERVB 2025 Nr. 3: höchstens 1.000 Dateien und 200 MB je Nachricht. |
| XML außerhalb Mahnverfahren praktisch bedeutungslos | Soll-Regelung in § 2 Abs. 3 ERVV; aktuelle XJustiz-Nachricht und konsistente Metadaten. |
| qeS oder bloßer sicherer Kanal | qeS der verantwortenden Person oder einfache Signatur plus persönlich ausgeführter sicherer Versand; Anlagenprivileg, keine gemeinsame Containersignatur und besondere Gesellschaftspostfachkonstellationen differenziert. |
| Automatisches Empfangsbekenntnis als Versandnachweis | Automatisierte Eingangsbestätigung nach § 130a Abs. 5 ZPO; eEB nach § 173 Abs. 3 ZPO gehört zur Zustellung an professionelle Empfänger. Formprüfung und Zugangskontrolle bleiben verschieden. |
| Test-Einreichung beim Prozessgericht | Lokale Prüfung; technische Probe ausschließlich in ausdrücklich dafür vorgesehener Testumgebung. |
| Notfall nur Papier und nur „echte Notfälle“ | Vorübergehende technische Unmöglichkeit, zulässiger konkreter Ersatzweg und rechtzeitige Glaubhaftmachung nach § 130d ZPO; § 3 ERVV und Heilungsregel des § 130a Abs. 6 ZPO getrennt. |

Das Arbeitsergebnis ist ein verwendbarer Schriftsatz mit Anlagenverzeichnis und internem Versandvermerk. Die sechs Arbeitsschritte trennen Auftrag, Sprache, Dateien/Signatur, bestätigten Eingang, Störungen und Abschluss. Kein Erfolg wird vor der Eingangsbestätigung behauptet.

## 2. Gelesene Primärquellen

### 2.1 Normtexte und Bekanntmachung

- [§ 130a ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html), besonders Abs. 2–6: Bearbeitungseignung, Signaturalternativen, sichere Übermittlungswege, gerichtliche Speicherung/Bestätigung, Nachreichung einer geeigneten Fassung. Der aktuelle gesamte Einzeltext wurde direkt abgerufen und gelesen; keine alte Nummerierung der beA-Alternative aus den älteren BGH-Entscheidungen in den neuen Text übernommen.
- [§ 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html): elektronische Einreichungspflicht, technische Unmöglichkeit, Glaubhaftmachung und Nachreichung.
- [§ 2 ERVV](https://www.gesetze-im-internet.de/ervv/__2.html): vollständiger Einzeltext; PDF/TIFF, technische Soll-Standards, XML-Mindestinhalt.
- [§ 3 ERVV](https://www.gesetze-im-internet.de/ervv/__3.html): vollständiger Einzeltext; zulässiger Ersatz bei glaubhaft nicht einhaltbaren Datei-/Volumengrenzen.
- [§ 4 ERVV](https://www.gesetze-im-internet.de/ervv/__4.html): vollständiger Einzeltext; qeS-Übermittlungswege und Ausschluss gemeinsamer qeS für mehrere Dokumente.
- [§ 5 ERVV](https://www.gesetze-im-internet.de/ervv/__5.html): vollständiger Einzeltext; Gegenstände der technischen Bekanntmachung.
- [ERVB 2025, BAnz AT 29.07.2025 B2](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf): amtliche PDF, beide Seiten vollständig extrahiert und gelesen. Nr. 1 Dateiformate/aktive Inhalte, Nr. 2 XJustiz, Nr. 3 1.000 Dateien/200 MB, Nr. 4 Datenträger, Nr. 5 Signaturformate, Nr. 6 Dateieigenschaften; Geltung ab dem Tag nach Veröffentlichung, also 30. Juli 2025.
- [§ 184a GVG](https://www.gesetze-im-internet.de/gvg/__184a.html): vollständiger Einzeltext, insbesondere Abs. 3–5. Bei deutschen Urkunden besteht die Möglichkeit einer Übersetzungsanordnung auf Antrag; keine automatische Pflicht.
- [§ 184b GVG](https://www.gesetze-im-internet.de/gvg/__184b.html): vollständiger Einzeltext. Antrag in Rechtsmittelschrift und Stattgabe; § 142 Abs. 3 ZPO bleibt beim BGH anwendbar.
- [§ 142 ZPO](https://www.gesetze-im-internet.de/zpo/__142.html): Einzeltext, besonders Abs. 3 zu qualifizierten Übersetzungen.
- [§ 173 ZPO](https://www.gesetze-im-internet.de/zpo/__173.html): vollständiger Einzeltext; Abs. 3 zur Rückübermittlung des eEB.

Einzelne Abrufe von Gesetze-im-Internet über die Weboberfläche schlugen mit Timeout fehl. Für §§ 130a/130d ZPO und §§ 3/4 ERVV erfolgte deshalb ein erfolgreicher unmittelbarer HTTP-Abruf der amtlichen HTML-Dateien; die gespeicherten Texte wurden gelesen. Es wurde kein Sekundärtext an deren Stelle als amtlicher Volltext ausgegeben.

### 2.2 Rechtsprechung

**BGH, Beschluss vom 30. März 2022 – XII ZB 311/21**, ECLI:DE:BGH:2022:300322BXIIZB311.21.0. [Amtlicher XML-Volltext](https://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/jb-KORE312652022.zip) direkt aus Rechtsprechung-im-Internet abgerufen, Leitsatz und vollständige Gründe gelesen. Maßgeblich Rn. 8–12 (qeS bzw. persönliche sichere Übermittlung) und Rn. 18 (erfolgreiche Übertragung bestätigt nicht die Signaturwirksamkeit). Das Verfahren war eine Familiensache und betraf das persönliche beA. Keine besondere Beschwerde- oder Wiedereinsetzungsfrist und keine pauschale Regel für Gesellschaftspostfächer übernommen.

**BGH, Beschluss vom 9. September 2026 – XII ZB 158/26**, ECLI:DE:BGH:2026:090926BXIIZB158.26.0. [Amtlicher XML-Volltext](https://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/jb-KORE626782026.zip) direkt abgerufen und vollständige Gründe gelesen. Rn. 11–13: ausreichende Zeitreserve, Kontrolle der Eingangsbestätigung und Abschluss des Übermittlungsversuchs. Die dort behandelten ungefähr 20 Minuten werden nicht als allgemeine Freigabe für späten Versand dargestellt. Rn. 14: mögliche Ersatzeinreichung bei Wiedereinsetzung substantiiert behandeln. Der BGH hob auf und verwies zurück; der neue Text behauptet keine bereits endgültig gewährte Wiedereinsetzung. Die familienrechtliche Besonderheit in Rn. 7 wird ausdrücklich nicht auf Handelsstreitigkeiten übertragen.

## 3. Grenzen und Synchronisierung

Die Prüfung enthält keine Vollerhebung sämtlicher Landesverordnungen, keine Zertifizierung einer konkreten Kanzleisoftware und keine Testsendung an ein Gericht. Eine konkrete gerichtliche Einreichung muss Spruchkörper, Land, aktuelle XJustiz-Version, Dateibestand und Signaturweg anhand der echten Akte vervollständigen. Die Fachquelle benennt hierfür die Tatsachen und Entscheidungspunkte; sie behauptet keinen ausgeführten Versand.

Der Quellenpfad bleibt unverändert. Gebundene Prüfsummen in `quality/skill-consolidation/2026-11-14/source-map.json` und gegebenenfalls abgeleitete Werkstattfassungen sind nach Integration durch den Hauptprozess zu aktualisieren. Die außerhalb dieses Teilauftrags liegende Beschreibung in `commercial-courts-deutschland/README.md` enthielt bei der Prüfung noch „Empfangsbekenntnis“ als Gegenstand der Versandkontrolle; der Hauptprozess erhielt den Hinweis, dies zu „Eingangsbestätigung“ zu ändern. Keine globale Neugenerierung in diesem Teilauftrag.

## 4. Prüfungen

- `python3 scripts/test-prompt-openings.py`: 7 Tests erfolgreich nach der Änderung.
- `git diff --check`: erfolgreich.
- Gezielte Prüfung der Fachquelle mit PyYAML: Frontmatter lesbar, unveränderter stabiler Name, Beschreibung unter 1.024 Zeichen und dezimale Überschriften.
- Gezielte Textkontrolle: die fünf alten Fehlerbehauptungen fehlen; 1.000 Dateien/200 MB, XML-Soll, beide GVG-Sprachvorschriften, beide tatsächlich gelesenen BGH-Entscheidungen und § 130a Abs. 6 ZPO vorhanden.

Diese Prüfungen verifizieren Struktur und gezielt korrigierte Aussagen; sie sind keine automatisierte Bestätigung sämtlicher Rechtsfragen und kein Einreichungstest.
