# 1. Nachprüfung Wirtschaftsanwalt

Sechs vormals offene Dateien wurden vollständig gelesen und inhaltlich geprüft. Die Prüfung vom 14.11.2026 ersetzt keine historischen Prüffakten. Neue SHA-256-Werte binden die konkret geprüften Fassungen; sie sind nicht selbst die fachliche Evidenz.

## 1.1. Änderungen und Grenzen

Die Prompts trennen den Geheimnisschutz nach Paragraf 43e BRAO von einer AVV. Die Überschuldungsprüfung nennt die Ausnahme der positiven Fortführungsprognose ausdrücklich. Die Werkstatt konkretisiert verifizierte BGH-Aussagen zu Liquiditätsstatus, Aktiva II und Passiva II sowie vorläufig vollstreckbaren Forderungen. Die Aktualitätssuche ergänzt BAG, Urteil vom 07.05.2026, 2 AZR 184/25, zur fehlenden Beweisvermutung im konkret festgestellten Scan-Verfahren. Zehn Skills und sämtliche Fachrouten bleiben bestehen.

Die amtlichen BGH-PDF-Texte waren im Recherchewerkzeug lesbar; direkte HTTP-Downloads lieferten Suchseiten. Es wird kein frischer Original-PDF-Download behauptet. Die DSGVO-Passagen wurden am amtlichen BfDI-Normtext geprüft. Eine vollständige EUR-Lex-Konsolidierungsprüfung und Live-Modellausführung werden nicht behauptet.

## 1.2. Einzeldateien

### 1.2.1. `wirtschaftsanwalt/.claude-plugin/plugin.json`

Vollständig gelesen: ja. Ergebnis: revised. 19 Zeilen, 600 Bytes.

Vorher: `8c972ea35d2e4cfc4c49ff000e44e34654d7115f812a96b11f67e6c760c9bf98`.

Geprüfte Fassung: `02ead4cd8f95e86010a112aef16ba4d8cc3ad270d05adea40f5fe097981a89b0`.

- Manifest vollständig gelesen: Pluginidentität, Autor, Lizenz und fachliche Beschreibung stimmen mit dem Paket überein.
- Version 445.36.1 nach dem root-Update erneut vollständig gelesen; einziges Manifestdelta gegenüber der Ausgangsfassung ist die Versionsnummer.
- Die Beschreibung nennt zehn ausführende Skills; tatsächlich bestehen zehn unmittelbare SKILL.md-Dateien. Keine nicht vorhandene technische Funktion versprochen.

Quelle: Manifest und lokaler Paketbestand; keine eigenen Rechtsprechungsbehauptungen.

### 1.2.2. `wirtschaftsanwalt/.codex-plugin/plugin.json`

Vollständig gelesen: ja. Ergebnis: revised. 34 Zeilen, 1160 Bytes.

Vorher: `50a7b0c291e27cef4ec60c02ef9e7bac6d0e35b16dfe50e872d1ebb4ae5ee154`.

Geprüfte Fassung: `dcbccc26c254d50b86ea19d94a881f263e1cdec76cfb59557dd6084bd930ff27`.

- Manifest vollständig gelesen: Version 445.36.1 und Beschreibung stimmen mit dem Claude-Manifest überein.
- Der skills-Pfad ./skills/ ist vorhanden; zehn unmittelbare Skillordner bleiben vollständig enthalten.
- Anzeigename, Kurz- und Langbeschreibung sowie defaultPrompt beschreiben laufende Unternehmensberatung. Die Interface-Metadaten versprechen keine bereits ausgeführte Handlung; die Werkstatt prüft die tatsächliche Werkzeugverfügbarkeit.

Quelle: Manifest und lokaler Paketbestand; keine eigenen Rechtsprechungsbehauptungen.

### 1.2.3. `wirtschaftsanwalt/README.md`

Vollständig gelesen: ja. Ergebnis: revised. 232 Zeilen, 35433 Bytes.

Vorher: `63bf2c6367fb3c83ea925fc076a69d77d7e0bd8a1eaab5a3998bbad59f1bda4e`.

Geprüfte Fassung: `56e5d2cfad225c0c5191497ddfa50e1808b0db38047f205aee99aa73cf86431d`.

- Vollständige Anleitung einschließlich aller manuellen und automatischen Downloadabschnitte, zehn Skills und drei zugeordneter Testakten gelesen.
- Eigenständige Verwendung der Prompts und separate Bereitstellung der Testakten korrekt getrennt.
- Zitierweise-Datei tatsächlich bytegleich mit der zentralen Referenz (SHA-256 134a0dd88187582587142f592497ca0d08f55a3d2b9b6dad8ccb91ea23ef7c9e).
- Quellenabschnitt trennt historischen lokalen PDF-Check, heutigen amtlichen PDF-Textzugriff und gescheiterte direkte Downloads; keine Gesamtaktualitätsgarantie.
- Root-Metadatendelta nachgelesen: manuelle Version nun 445.36.1; beide nativen Plugin-ZIP-Links verwenden qualitaetsrunde-v445.36.1. Quellenabschnitt ergänzt die amtlich geprüfte neuere BAG-Entscheidung 2 AZR 184/25.
- Aktualitätssuche ergänzt BAG, Urteil vom 07.05.2026, 2 AZR 184/25: amtliche Gründe gelesen; auch ein vor dem Einwurf erzeugter Auslieferungsbeleg genügte im festgestellten Scan-Verfahren nicht. Frühere/offene und spätere abweichende Verfahren sowie Zeugenbeweis ausdrücklich abgegrenzt.

Quellen-IDs: `bag-2-azr-68-24`, `bgh-ii-zr-112-21`, `bgh-ii-zr-88-16`, `bgh-ix-zr-229-22`, `brao-43e`, `inso-19`, `bfdi-dsgvo`, `bag-2-azr-184-25`.

### 1.2.4. `wirtschaftsanwalt/references/fachquellen.md`

Vollständig gelesen: ja. Ergebnis: revised. 69 Zeilen, 16306 Bytes.

Vorher: `b36959f3570de42d1794c604bc4e9b02c9643d165258f406c9e89a26d39a28b9`.

Geprüfte Fassung: `7e2f394df985fcedc2146f0f57e509ac441ffac18191e3526ebdf222443f0e3f`.

- Alle Abschnitte 1.1 bis 1.8 einschließlich jeder Abrufgrenze vollständig gelesen.
- Interessenkollision, organschaftliche Vertretung gegenüber interner Zustimmung und aktuelle Textformregel des Paragrafen 48 GmbHG bestätigt.
- Paragraf 308 Nummern 1a und 1b BGB bleibt im Unternehmerverkehr relevant; 30 und 15 Tage sind Zweifelsgrenzen und kein starres Totalverbot.
- Paragraf 623 BGB und die Prozessformfiktion des Paragrafen 46h ArbGG getrennt; BAG-Aussage zum Zugang mit offengelassener Konstellation in Randnummer 18 bestätigt.
- Dienstleister-Geheimnisschutz nach Paragraf 43e BRAO ergänzt; AVV als alleinige Freigabe ausgeschlossen.
- Ausnahme der positiven Fortführungsprognose bei Paragraf 19 InsO präzisiert; drei und sechs Wochen als Höchstfristen, 24 und zwölf Monate getrennt.
- BGH-Passagen neu gelesen; II ZR 88/16 mit belegtem amtlichem Volltextanker und IX ZR 229/22 mit fallbegrenzter positiver Aussage ergänzt.
- DSGVO-Berichtigungen anhand des BfDI-Normtextes kontrolliert; vollständige EUR-Lex-Konsolidierungsprüfung weiter ausdrücklich nicht behauptet.
- Keine Literaturfundstelle aus dem Gedächtnis hinzugefügt; historische Prüffakten nicht rückwirkend als neue Prüfung umetikettiert.
- Aktualitätssuche ergänzt BAG, Urteil vom 07.05.2026, 2 AZR 184/25: amtliche Gründe gelesen; auch ein vor dem Einwurf erzeugter Auslieferungsbeleg genügte im festgestellten Scan-Verfahren nicht. Frühere/offene und spätere abweichende Verfahren sowie Zeugenbeweis ausdrücklich abgegrenzt.

Quellen-IDs: `brao-43a`, `brao-43e`, `stgb-203`, `gmbhg-35`, `gmbhg-37`, `gmbhg-46`, `gmbhg-47`, `gmbhg-48`, `gmbhg-49`, `gmbhg-50`, `gmbhg-51`, `gmbhg-51a`, `hgb-377`, `bgb-308`, `bgb-310`, `bgb-623`, `bgb-637`, `bgb-640`, `kschg-1`, `kschg-4`, `kschg-23`, `betrvg-102`, `arbgg-46h`, `inso-15a`, `inso-15b`, `inso-17`, `inso-18`, `inso-19`, `starug-1`, `zpo-253`, `zpo-130a`, `zpo-130d`, `zpo-485`, `gvg-23`, `bgb-130`, `bgb-177`, `bgb-180`, `bgb-181`, `bgb-195`, `bgb-199`, `bgb-203`, `bgb-204`, `bgb-212`, `bgb-271a`, `bgb-276`, `bgb-286`, `bgb-288`, `bgb-305b`, `bgb-306`, `bgb-307`, `bgb-362`, `bgb-366`, `bgb-367`, `bgb-387`, `bgb-397`, `bgb-779`, `zpo-794`, `bag-2-azr-68-24`, `bgh-ii-zr-112-21`, `bgh-ii-zr-88-16`, `bgh-ix-zr-229-22`, `bfdi-dsgvo`, `bag-2-azr-184-25`.

### 1.2.5. `wirtschaftsanwalt/wirtschaftsanwalt-schnellstart.md`

Vollständig gelesen: ja. Ergebnis: revised. 53 Zeilen, 7497 Bytes.

Vorher: `3efef574d3214593afd671267fd8d1651dd4e003def5d1d56fdf4dc0dabd4f24`.

Geprüfte Fassung: `fa43056f942c2f2032e86333be618eaa184eee8e646da31c5c07d8a18a18eb05`.

- Alle 53 Zeilen gelesen; die acht Fachrouten, Intake, Entscheidung und Fortsetzung bleiben erhalten.
- Paragrafen 43e BRAO und 203 StGB ergänzen die Datenschutzprüfung; keine automatische Freigabe durch AVV.
- Paragraf 19 InsO als Vermögensunterdeckung mit Ausnahme der überwiegend wahrscheinlichen Fortführung für zwölf Monate formuliert; Rechtsträgerkreisprüfung ergänzt.
- BAG-Aussage, rechtzeitige Absendung nach Paragraf 377 HGB, AGB-Kontrolle im Unternehmerverkehr, Prozessformfiktion und Amtsgerichtsgrenze von 10.000 EUR nachgeprüft.
- Nachprüfung am 14.11.2026 bezeichnet statt einer veralteten pauschalen Aussage über Quellenzugriff; kein vollständiger Konsolidierungsnachweis behauptet.
- 7497 UTF-8-Bytes und weniger als 7500 Zeichen; keine fachlichen Routen wegen des Längenlimits entfernt.
- Aktualitätssuche ergänzt BAG, Urteil vom 07.05.2026, 2 AZR 184/25: amtliche Gründe gelesen; auch ein vor dem Einwurf erzeugter Auslieferungsbeleg genügte im festgestellten Scan-Verfahren nicht. Frühere/offene und spätere abweichende Verfahren sowie Zeugenbeweis ausdrücklich abgegrenzt.

Quellen-IDs: `brao-43a`, `brao-43e`, `stgb-203`, `gmbhg-35`, `gmbhg-37`, `gmbhg-47`, `gmbhg-51a`, `hgb-377`, `bgb-637`, `kschg-1`, `kschg-23`, `betrvg-102`, `bgb-623`, `arbgg-46h`, `bag-2-azr-68-24`, `bgb-308`, `bgb-310`, `bfdi-dsgvo`, `inso-17`, `inso-18`, `inso-19`, `inso-15a`, `inso-15b`, `zpo-253`, `gvg-23`, `bag-2-azr-184-25`.

### 1.2.6. `wirtschaftsanwalt/wirtschaftsanwalt-werkstatt.md`

Vollständig gelesen: ja. Ergebnis: revised. 317 Zeilen, 70143 Bytes.

Vorher: `9d41c86689b0069b14da7d196b62184c530c0c4f9542c2374aef20aaace98aba`.

Geprüfte Fassung: `d1609f015791b6fbd2286225f9c30b8b7842f9271aa4e71d8460b72b05be24c2`.

- Gesamte Werkstatt mit Abschnitten 1.1 bis 1.22 und Abschnitt 2 zur Visualisierung vollständig gelesen, nicht nur Suchtreffer.
- Rollen, Mandantin und Vertretung, Dokumentstatus, Folgeauftrag, interne Notiz, Empfängerfassung und vollständiges Arbeitsprodukt auf Kohärenz geprüft.
- Interaktive Ansichten setzen tatsächliche Werkzeugverfügbarkeit voraus; keine fingierte Datei, Speicherung oder Einreichung.
- Vertragsleistung und Haftung, Fälligkeit und Verzug, Tilgung und Aufrechnung sowie AGB-Gegenrechte anhand ihrer getrennten Voraussetzungen geprüft.
- Kündigungsschutz, Form und Zugang, GmbH-Beschluss, Textform, Auskunft und Minderheitenrechte mit Primärnormen abgeglichen.
- Eigenständige Prüfung des Dienstleisterzugriffs nach Paragraf 43e BRAO und Prüfungsreihenfolge des Paragrafen 19 InsO konkret ergänzt.
- BGH II ZR 112/21: aussagekräftige Status als zulässige Darlegungsalternative; II ZR 88/16: Aktiva II und Passiva II; IX ZR 229/22: Titel und Vollstreckung mit präzisen Voraussetzungen.
- Gerichtsvorbereitung: bestimmter Antrag, keine allgemeine Ausforschung, Amtsgerichtsgrenze 10.000 EUR, Einreichung nicht mit Zustellung gleichgesetzt; privater Vergleich nicht automatisch Vollstreckungstitel.
- Quellenkapitel trennt historische und heutige Abrufart; gezielte BfDI-Normprüfung statt unbelegter EUR-Lex-Konsolidierung.
- Vollständiger Fachinhalt, zehn Skills und Fachrouten bleiben erhalten; kein Live-Modelllauf behauptet.
- Aktualitätssuche ergänzt BAG, Urteil vom 07.05.2026, 2 AZR 184/25: amtliche Gründe gelesen; auch ein vor dem Einwurf erzeugter Auslieferungsbeleg genügte im festgestellten Scan-Verfahren nicht. Frühere/offene und spätere abweichende Verfahren sowie Zeugenbeweis ausdrücklich abgegrenzt.

Quellen-IDs: `brao-43a`, `brao-43e`, `stgb-203`, `gmbhg-35`, `gmbhg-37`, `gmbhg-46`, `gmbhg-47`, `gmbhg-48`, `gmbhg-49`, `gmbhg-50`, `gmbhg-51`, `gmbhg-51a`, `hgb-377`, `bgb-308`, `bgb-310`, `bgb-623`, `bgb-637`, `bgb-640`, `kschg-1`, `kschg-4`, `kschg-23`, `betrvg-102`, `arbgg-46h`, `inso-15a`, `inso-15b`, `inso-17`, `inso-18`, `inso-19`, `starug-1`, `zpo-253`, `zpo-130a`, `zpo-130d`, `zpo-485`, `gvg-23`, `bgb-130`, `bgb-177`, `bgb-180`, `bgb-181`, `bgb-195`, `bgb-199`, `bgb-203`, `bgb-204`, `bgb-212`, `bgb-271a`, `bgb-276`, `bgb-286`, `bgb-288`, `bgb-305b`, `bgb-306`, `bgb-307`, `bgb-362`, `bgb-366`, `bgb-367`, `bgb-387`, `bgb-397`, `bgb-779`, `zpo-794`, `bag-2-azr-68-24`, `bgh-ii-zr-112-21`, `bgh-ii-zr-88-16`, `bgh-ix-zr-229-22`, `bfdi-dsgvo`, `bag-2-azr-184-25`.

## 1.3. Gelesene Quellen

- [brao-43a](https://www.gesetze-im-internet.de/brao/__43a.html): Absätze 2 und 4: Verschwiegenheit, eigene Interessenkollision gegenüber Erstreckung auf Berufsausübungsgemeinschaft. Methode: amtlicher Normvolltext gelesen.
- [brao-43e](https://www.gesetze-im-internet.de/brao/__43e.html): Absätze 1 bis 5 und 8: Dienstleisterzugriff, Textformvertrag, Ausland und mandatsbezogene Einwilligung; DSGVO bleibt gesondert. Methode: amtlicher Normvolltext gelesen.
- [stgb-203](https://www.gesetze-im-internet.de/stgb/__203.html): Absätze 1, 3 und 4: berufliches Geheimnis und erforderlicher Zugriff mitwirkender Personen. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-35](https://www.gesetze-im-internet.de/gmbhg/__35.html): Absätze 1 bis 3: organschaftliche Vertretung, Gesamtvertretung, Insichgeschäft. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-37](https://www.gesetze-im-internet.de/gmbhg/__37.html): Absätze 1 und 2: interne Schranken, Außenwirkung. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-46](https://www.gesetze-im-internet.de/gmbhg/__46.html): Aufgabenkreis der Gesellschafter. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-47](https://www.gesetze-im-internet.de/gmbhg/__47.html): Abstimmung und konkrete Stimmverbote. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-48](https://www.gesetze-im-internet.de/gmbhg/__48.html): Versammlung, Video/Telefon, Einverständnis sämtlicher Gesellschafter in Textform, Dokumentation des Alleingesellschafters. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-49](https://www.gesetze-im-internet.de/gmbhg/__49.html): Einberufung und Verlust der Hälfte des Stammkapitals. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-50](https://www.gesetze-im-internet.de/gmbhg/__50.html): Minderheitsrechte. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-51](https://www.gesetze-im-internet.de/gmbhg/__51.html): Einberufungsform und Fristen. Methode: amtlicher Normvolltext gelesen.
- [gmbhg-51a](https://www.gesetze-im-internet.de/gmbhg/__51a.html): Information, Einsicht, gesetzliche Versagungsvoraussetzungen. Methode: amtlicher Normvolltext gelesen.
- [hgb-377](https://www.gesetze-im-internet.de/hgb/__377.html): Absätze 1 bis 5, besonders rechtzeitige Absendung und Arglistgrenze. Methode: amtlicher Normvolltext gelesen.
- [bgb-308](https://www.gesetze-im-internet.de/bgb/__308.html): Nummern 1a und 1b: Zweifelsgrenzen 30/15 Tage. Methode: amtlicher Normvolltext gelesen.
- [bgb-310](https://www.gesetze-im-internet.de/bgb/__310.html): Absätze 1 und 1a: keine pauschale Ausnahme von Paragraf 308 Nummern 1a/1b im B2B-Verkehr; VOB/B- und Finanzgeschäftssonderregeln. Methode: amtlicher Normvolltext gelesen.
- [bgb-623](https://www.gesetze-im-internet.de/bgb/__623.html): Schriftform und Ausschluss elektronischer Form. Methode: amtlicher Normvolltext gelesen.
- [bgb-637](https://www.gesetze-im-internet.de/bgb/__637.html): Selbstvornahme im Werkvertragsrecht. Methode: amtlicher Normvolltext gelesen.
- [bgb-640](https://www.gesetze-im-internet.de/bgb/__640.html): Abnahme, Fiktion, Vorbehalt. Methode: amtlicher Normvolltext gelesen.
- [kschg-1](https://www.gesetze-im-internet.de/kschg/__1.html): Soziale Rechtfertigung, anderweitige Beschäftigung, Beweislast. Methode: amtlicher Normvolltext gelesen.
- [kschg-4](https://www.gesetze-im-internet.de/kschg/__4.html): Dreiwochenfrist, schriftliche Kündigung, behördliche Zustimmungsfälle. Methode: amtlicher Normvolltext gelesen.
- [kschg-23](https://www.gesetze-im-internet.de/kschg/__23.html): Schwellenwert, Teilzeit und Alt-Arbeitnehmer. Methode: amtlicher Normvolltext gelesen.
- [betrvg-102](https://www.gesetze-im-internet.de/betrvg/__102.html): Anhörung vor Kündigung; Fristen und Widerspruch. Methode: amtlicher Normvolltext gelesen.
- [arbgg-46h](https://www.gesetze-im-internet.de/arbgg/__46h.html): Formfiktion bei normgerechtem elektronischem Schriftsatz und Zustellung/Mitteilung, auch bei sonst ausgeschlossenem elektronischem Formersatz. Methode: amtlicher Normvolltext gelesen.
- [inso-15a](https://www.gesetze-im-internet.de/inso/__15a.html): Pflichtenkreis, ohne schuldhaftes Zögern, Höchstfristen drei und sechs Wochen. Methode: amtlicher Normvolltext gelesen.
- [inso-15b](https://www.gesetze-im-internet.de/inso/__15b.html): Zahlungen nach Insolvenzreife und gesetzliche Sorgfaltsausnahmen. Methode: amtlicher Normvolltext gelesen.
- [inso-17](https://www.gesetze-im-internet.de/inso/__17.html): Fällige Zahlungspflichten, Zahlungseinstellung. Methode: amtlicher Normvolltext gelesen.
- [inso-18](https://www.gesetze-im-internet.de/inso/__18.html): Eigenantrag und regelmäßig 24 Monate. Methode: amtlicher Normvolltext gelesen.
- [inso-19](https://www.gesetze-im-internet.de/inso/__19.html): Vermögensunterdeckung, Ausnahme positive Prognose für zwölf Monate und Nachrangvoraussetzungen. Methode: amtlicher Normvolltext gelesen.
- [starug-1](https://www.gesetze-im-internet.de/starug/__1.html): Krisenfrüherkennung und zuständiger Personenkreis. Methode: amtlicher Normvolltext gelesen.
- [zpo-253](https://www.gesetze-im-internet.de/zpo/__253.html): Bestimmter Antrag, Parteien, Lebenssachverhalt und Zustellung. Methode: amtlicher Normvolltext gelesen.
- [zpo-130a](https://www.gesetze-im-internet.de/zpo/__130a.html): Signatur/Übermittlungsweg, Eingang und technische Anforderungen. Methode: amtlicher Normvolltext gelesen.
- [zpo-130d](https://www.gesetze-im-internet.de/zpo/__130d.html): Nutzungspflicht und vorübergehende technische Unmöglichkeit. Methode: amtlicher Normvolltext gelesen.
- [zpo-485](https://www.gesetze-im-internet.de/zpo/__485.html): Tatbestandsgebundene vorprozessuale Beweissicherung. Methode: amtlicher Normvolltext gelesen.
- [gvg-23](https://www.gesetze-im-internet.de/gvg/__23.html): Allgemeine Wertgrenze 10.000 EUR und Sonderzuständigkeiten. Methode: amtlicher Normvolltext gelesen.
- [bgb-130](https://www.gesetze-im-internet.de/bgb/__130.html): Zugang. Methode: amtlicher Normvolltext gelesen.
- [bgb-177](https://www.gesetze-im-internet.de/bgb/__177.html): Vertreter ohne Vertretungsmacht. Methode: amtlicher Normvolltext gelesen.
- [bgb-180](https://www.gesetze-im-internet.de/bgb/__180.html): Einseitige Rechtsgeschäfte. Methode: amtlicher Normvolltext gelesen.
- [bgb-181](https://www.gesetze-im-internet.de/bgb/__181.html): Insichgeschäft. Methode: amtlicher Normvolltext gelesen.
- [bgb-195](https://www.gesetze-im-internet.de/bgb/__195.html): Regelverjährung. Methode: amtlicher Normvolltext gelesen.
- [bgb-199](https://www.gesetze-im-internet.de/bgb/__199.html): Beginn Regelverjährung. Methode: amtlicher Normvolltext gelesen.
- [bgb-203](https://www.gesetze-im-internet.de/bgb/__203.html): Verhandlungen als Hemmung. Methode: amtlicher Normvolltext gelesen.
- [bgb-204](https://www.gesetze-im-internet.de/bgb/__204.html): Rechtsverfolgungsmaßnahmen. Methode: amtlicher Normvolltext gelesen.
- [bgb-212](https://www.gesetze-im-internet.de/bgb/__212.html): Neubeginn. Methode: amtlicher Normvolltext gelesen.
- [bgb-271a](https://www.gesetze-im-internet.de/bgb/__271a.html): Zahlungs-, Überprüfungs- und Abnahmefristen. Methode: amtlicher Normvolltext gelesen.
- [bgb-276](https://www.gesetze-im-internet.de/bgb/__276.html): Vorsatzhaftung nicht im Voraus erlassen. Methode: amtlicher Normvolltext gelesen.
- [bgb-286](https://www.gesetze-im-internet.de/bgb/__286.html): Verzugsvoraussetzungen. Methode: amtlicher Normvolltext gelesen.
- [bgb-288](https://www.gesetze-im-internet.de/bgb/__288.html): B2B-Verzugszinsen und Pauschale. Methode: amtlicher Normvolltext gelesen.
- [bgb-305b](https://www.gesetze-im-internet.de/bgb/__305b.html): Individualabrede. Methode: amtlicher Normvolltext gelesen.
- [bgb-306](https://www.gesetze-im-internet.de/bgb/__306.html): Unwirksamkeitsfolgen. Methode: amtlicher Normvolltext gelesen.
- [bgb-307](https://www.gesetze-im-internet.de/bgb/__307.html): Inhaltskontrolle. Methode: amtlicher Normvolltext gelesen.
- [bgb-362](https://www.gesetze-im-internet.de/bgb/__362.html): Erfüllung. Methode: amtlicher Normvolltext gelesen.
- [bgb-366](https://www.gesetze-im-internet.de/bgb/__366.html): Tilgungsbestimmung. Methode: amtlicher Normvolltext gelesen.
- [bgb-367](https://www.gesetze-im-internet.de/bgb/__367.html): Kosten/Zinsen/Hauptforderung. Methode: amtlicher Normvolltext gelesen.
- [bgb-387](https://www.gesetze-im-internet.de/bgb/__387.html): Gegenseitigkeit und Fälligkeit bei Aufrechnung. Methode: amtlicher Normvolltext gelesen.
- [bgb-397](https://www.gesetze-im-internet.de/bgb/__397.html): Erlassvertrag. Methode: amtlicher Normvolltext gelesen.
- [bgb-779](https://www.gesetze-im-internet.de/bgb/__779.html): Vergleichsbegriff und Irrtum über Vergleichsgrundlage. Methode: vollständiger amtlicher Normtext im Suchergebnis gelesen. Grenze: Direktabrufe zeitweise Timeout; kein erfolgreicher Einzel-HTTP-Abruf behauptet.
- [zpo-794](https://www.gesetze-im-internet.de/zpo/__794.html?level=1): Absatz 1 Nummern 1 und 5; private Einigung nicht automatisch Vollstreckungstitel. Methode: amtlicher Normtext im Suchergebnis gelesen. Grenze: Direktabruf ohne Query zeitweise Timeout.
- [bag-2-azr-68-24](https://www.bundesarbeitsgericht.de/entscheidung/2-azr-68-24/): BAG, Urteil vom 30.01.2025, 2 AZR 68/24, Randnummern 15 bis 21, besonders offene Konstellation in Randnummer 18. Methode: amtlicher Entscheidungsvolltext gelesen. Grenze: Kein allgemeines Verbot von Einwurf-Einschreiben; keine Aussage über Kündigungsgründe.
- [bgh-ii-zr-112-21](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Art=en&Blank=1.pdf&Datum=Aktuell&Gericht=bgh&Sort=12288&anz=846&nr=130746&pos=10): BGH, Urteil vom 28.06.2022, II ZR 112/21, Randnummern 12 bis 17 zum Liquiditätsstatus und Randnummern 18 folgende zum alten Paragraf 64 GmbHG. Methode: einschlägige amtliche PDF-Volltextpassagen im Recherchewerkzeug gelesen. Grenze: Direkter HTTP-Download leitete auf Suchseite um; Wiederholungsabruf teils 403; keine neuen Original-PDF-Bytes oder Bytegleichheit behauptet.
- [bgh-ii-zr-88-16](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Art=en&Blank=1.pdf&Datum=2017&Gericht=bgh&Seite=1&anz=3127&nr=80774&pos=38): BGH, Urteil vom 19.12.2017, II ZR 88/16, Randnummern 17 bis 27 und 31 bis 36: Gegenvortrag und Passiva II. Methode: einschlägige amtliche PDF-Volltextpassagen im Recherchewerkzeug gelesen. Grenze: Alter Suchankerzugriff mit 403 gesperrt; neuer amtlicher Text sichtbar; direkter HTTP-Abruf lieferte Suchseite.
- [bgh-ix-zr-229-22](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Art=en&Blank=1.pdf&Datum=Aktuell&Gericht=bgh&Sort=12288&anz=1152&nr=140413&pos=16): BGH, Urteil vom 23.01.2025, IX ZR 229/22, Randnummern 34 bis 41: objektiver Bestand und Nachweiswirkung vorläufig vollstreckbarer Titel. Methode: einschlägige amtliche PDF-Volltextpassagen im Recherchewerkzeug gelesen. Grenze: Kein allgemeiner Beweislastsatz gegen Geschäftsführer; direkter HTTP-Abruf lieferte Suchseite; kein neuer Original-PDF-Hash.
- [bfdi-dsgvo](https://www.bfdi.bund.de/SharedDocs/Downloads/DE/Broschueren/INFO1.pdf?__blob=publicationFile&v=27): Normtext der Artikel 12, 15, 26, 28, 32 bis 34 und 44; Kopienlöschung nach Artikel 28 Absatz 3 Buchstabe g, Zuständigkeitsverweis des Artikels 33 Absatz 1 auf Artikel 55. Methode: amtlicher BfDI-Normtext gezielt gelesen. Grenze: EUR-Lex-Konsolidierungsabrufe lieferten keinen nutzbaren Volltext; keine Gesamtprüfung aller Änderungsakte und keine vollständige aktuelle EU-Rechtsprechungsinventur.
- [bag-2-azr-184-25](https://www.bundesarbeitsgericht.de/entscheidung/2-azr-184-25/): BAG, Urteil vom 07.05.2026, 2 AZR 184/25, ECLI:DE:BAG:2026:070526.U.2AZR184.25.0: kein Anscheinsbeweis im konkret festgestellten Scan-Verfahren mit Bestätigung vor dem Einwurf; Zeugenbeweis im Einzelfall unergiebig.. Methode: amtliche Entscheidungsgründe gelesen, insbesondere Randnummern 21 bis 30. Grenze: Zugang einer bEM-Einladung; früheres Peel-off-Verfahren in Randnummer 25 weiter offengelassen. Kein allgemeines Einschreibenverbot und keine pauschale Aussage über später geänderte Zustellverfahren..

## 1.4. Technische Nachkontrolle

Mini-Prompt: 7497 UTF-8-Bytes, weniger als 7500 Zeichen. Die Zitierweise ist byteidentisch zur zentralen Referenz. Manifestfassungen 445.36.1 wurden vollständig gelesen; die Versionszeile und beide nativen ZIP-Links im README wurden nach dem root-Delta erneut geprüft. Diff-Prüfung ohne Whitespace-Fehler bestanden. Der Bestandsbewahrungstest bestand; der Navigationstest erwartete noch einen Einzel-Downloadlink im inzwischen auf den Promptindex verweisenden Root-README. Root wurde zur Anpassung dieser vorbestehenden Testannahme informiert. Die sechs Datei-Hashes sind nach allen inhaltlichen und Metadatenänderungen gebunden.
