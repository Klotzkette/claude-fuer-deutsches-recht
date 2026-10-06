---
name: bauangebot-steuern
description: Steuert Bauvergabe Bieter über mehrere Phasen und setzt die Bearbeitung nach neuen Unterlagen fort; liefert vollständige Dokumente mit rollengetrennten Entscheidungen und Fristen.
---

# 1. Zweck und Anwendungsfall

Sie bearbeiten öffentliche Bauvergaben aus Sicht des konkret beauftragten Bauunternehmens oder einer Bietergemeinschaft. Liefern Sie das verlangte Arbeitsprodukt vom Teilnahmeentscheid bis zur Übergabe des geschlossenen Bauvertrags. Lesen Sie vorhandene Unterlagen zuerst. Fragen Sie nur nach Tatsachen, die Entscheidung, Frist, Preis oder Formulierung verändern. Eine bereits geklärte Rolle wird nicht erneut aufgenommen. Das Ergebnis ist ein ausformulierter Vermerk, ein konkreter Brief, eine geprüfte Angebotsfassung oder eine belastbare Übergabe. Eine allgemeine Wissenssammlung erledigt keinen Dokumentenauftrag.

Dieses Plugin ist ohne Reporoot und ohne gesonderten Großprompt nutzbar. Der Hauptskill verbindet genau zehn Fachskills und lokal enthaltene Quellen.

# 2. Eingaben

Lies Bekanntmachung, maßgebliche Unterlagenfassungen, eigenes Angebot, Rügen, Antworten, Entscheidungen und Zeitnachweise. Erfasse konkrete Mandatsrolle, gewünschtes Produkt und nächsten fristgebundenen Schritt. Unbekannte Akteninhalte werden nicht erfunden. Die Testakten Klinikum Münster und Wohnhaus Bielefeld bleiben in Namen, Preisen und Zeitabläufen getrennt. Die fiktive Fortsetzung 2027 nutzt den eingefrorenen Stand 06.10.2026.

# 3. Ablauf und Checkliste

## 3.1 Teilnahme und Angebotsbudget entscheiden

Nutze [bid-no-bid-entscheiden](../bid-no-bid-entscheiden/SKILL.md). Benötigt werden Bekanntmachung, vollständiger Unterlagenstand, Lose, Bauzeit, Kapazitäten, Referenzen, Angebotskosten, Sicherheitenrahmen und Entscheidungsbefugnis. Erstellen Sie eine begründete Entscheidung über Teilnahme, Teilnahme nach konkreter Klärung oder Verzicht. Eine intern bedingte Freigabe ist kein zulässiger Vorbehalt im späteren Angebot. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.2 Leistungsverzeichnis, Baugrund und Mengen prüfen

Nutze [lv-baugrund-mengen-pruefen](../lv-baugrund-mengen-pruefen/SKILL.md). Benötigt werden LV, Vorbemerkungen, Pläne, Baugrund- und Schadstoffgutachten, Entsorgungskonzept, Terminplan, Schnittstellen und verbindliche Antworten. Arbeiten Sie positionsbezogen. Ordnen Sie jede Unklarheit einer Ordnungszahl, Planrevision, Nebenleistung, besonderen Leistung oder Vertragsbedingung zu. Menge, Einheit, Leistungsgrenze, Qualität, Ausführungszeit und Abrechnung sind zusammen zu lesen. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.3 Eignung und Bietergemeinschaft sichern

Nutze [eignung-und-bietergemeinschaft-sichern](../eignung-und-bietergemeinschaft-sichern/SKILL.md). Benötigt werden bekanntgemachte Kriterien, Vorlagezeitpunkte, Formblätter, Präqualifikation, Referenzen, Registerdaten, Ausschlusserklärungen, Vollmachten sowie Aufgaben- und Haftungsverteilung. Trennen Sie Eignungskriterium, Nachweismittel und Zeitpunkt. Die interne Matrix ordnet jedem Kriterium eine Belegstelle und einen tatsächlichen Nachweis zu. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.4 Nachunternehmer und Eignungsleihe ordnen

Nutze [nachunternehmer-und-eignungsleihe-steuern](../nachunternehmer-und-eignungsleihe-steuern/SKILL.md). Benötigt werden Eigenleistungsplanung, benannte Unternehmen, konkrete Eignungslücken, Zusagen, Verfügbarkeitsnachweise, Lieferangebote und Vorgaben für kritische Aufgaben. Trennen Sie Unterauftrag von Eignungsleihe. Ein Nachunternehmer kann Teilleistungen ausführen, ohne die Eignung des Hauptbieters zu stützen. Ein finanzieller Kapazitätsgeber muss dagegen nicht jede technische Arbeit übernehmen. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.5 Baukalkulation und Preisblatt erstellen

Nutze [baukalkulation-und-preisblatt-erstellen](../baukalkulation-und-preisblatt-erstellen/SKILL.md). Benötigt werden verbindliches LV, Arbeitsansätze, Lohn-, Geräte- und Stoffkosten, Nachunternehmerangebote, Gemeinkosten, Sicherheiten und Preisgleitklauseln. Bauen Sie die Kalkulation aus dem ausgeschriebenen Leistungssoll auf. Trennen Sie Einzelkosten, Baustellengemeinkosten, allgemeine Geschäftskosten sowie Wagnis und Gewinn. Menge mal Einheitspreis, Rundungen, Überträge, Lose, Gesamtsummen und Umsatzsteuer werden rechnerisch geprüft. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.6 Bieterfragen und Rügen formulieren

Nutze [bieterfragen-und-ruegen-formulieren](../bieterfragen-und-ruegen-formulieren/SKILL.md). Benötigt werden konkrete Unterlagenstelle, Kenntnis- und Erkennenszeitpunkt, Angebotsfrist, bisherige Kommunikation, Betroffenheit und Abhilfeziel. Bestimmen Sie das Schreiben nach seinem Inhalt. Eine Bieterfrage klärt Informationen; eine Rüge beanstandet einen Vergabeverstoß und verlangt Beseitigung. Die Überschrift ist nicht allein entscheidend. Eine freundliche Bitte um Erläuterung ist aber kein verlässlicher Ersatz für eine klare Rechtsbeanstandung. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.7 Hauptangebot, Nebenangebote und Abgabe sichern

Nutze [angebot-nebenangebote-und-abgabe-sichern](../angebot-nebenangebote-und-abgabe-sichern/SKILL.md). Benötigt werden die letzte verbindliche Unterlagenfassung, zulässige Angebotsarten, Mindestanforderungen, Formblätter, Vollmacht, Plattformvorgaben und die Frist mit Zeitzone. Erstellen Sie eine eindeutige Abgabefassung. Ein überholtes GAEB-LV bleibt auch bei richtiger Endsumme überholt. Gleichen Sie Änderungen und Antworten mit Preisdatei, Produktangaben und Erklärungen ab. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.8 Nachforderung und Preisaufklärung beantworten

Nutze [nachforderung-und-preisaufklaerung-beantworten](../nachforderung-und-preisaufklaerung-beantworten/SKILL.md). Benötigt werden Originalangebot, Aufforderung, Zugang, Frist, etwaiger vorab erklärter Nachforderungsausschluss, Ursprungskalkulation und Belege. Ordnen Sie jede Frage einzeln zu: bereits mit Angebot geforderte Unterlage, erst später verlangter Nachweis, fehlende oder fehlerhafte Erklärung, leistungsbezogene Unterlage, Preisangabe oder Erläuterung vorhandenen Inhalts. Die Einordnung bestimmt die zulässige Antwort. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.9 Wertung, Bindefrist und Zuschlag begleiten

Nutze [wertung-bindefrist-und-zuschlag-begleiten](../wertung-bindefrist-und-zuschlag-begleiten/SKILL.md). Benötigt werden Angebot, Aufklärung, Wertungsgründe, Vorabinformation mit Versanddaten, Bindefrist, Verlängerungsersuchen und Zuschlag. Trennen Sie formale Zulässigkeit, Eignung, Preisangemessenheit und Zuschlagswertung. Ein Rangplatz allein erklärt nicht, ob ein Fehler die Zuschlagschance beeinflusst. Rekonstruieren Sie bekanntgemachte Kriterien und Gewichtung sowie die auf das eigene Angebot bezogenen Gründe. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

## 3.10 Vertragsübergabe und Beweissicherung

Nutze [vertragsuebergabe-und-beweissicherung](../vertragsuebergabe-und-beweissicherung/SKILL.md). Benötigt werden Zuschlag und Zugang, Angebot, sämtliche Vertragsunterlagen, verbindliche Antworten, Nebenangebote, Kalkulation und Projektzuständigkeiten. Stellen Sie zuerst fest, ob und mit welchem Inhalt der Vertrag geschlossen wurde. Nur tatsächlich vereinbarte Dokumente werden in das Vertragsverzeichnis aufgenommen. Eine interne Rechnung oder eine nicht angenommene Alternative ist nicht automatisch Vertragsbestandteil. Das Ergebnis wird mit den bisherigen Tatsachen und Fristen abgeglichen und in den nächsten erforderlichen Arbeitsschritt übergeben.

Trennen Sie die Perspektive des Bieters von Auftraggeber, Nachunternehmer und Wettbewerber. Ein interner Risikoentscheid, eine Erklärung an die Vergabestelle und ein Schriftsatz im Nachprüfungsverfahren sind unterschiedliche Produkte. Bei einem Rollenwechsel werden Auftrag und Tatsachenzugang neu abgegrenzt. Verwenden Sie keine vertraulichen Daten eines anderen Mandats. Dieses Plugin ist für öffentliche Bauvergaben entwickelt. Klinik- oder Wohnungsnutzung begründet keine Sektorenvergabe. Die VOB/B ist ein gegebenenfalls vereinbartes Vertragsregelwerk und nicht mit der VOB/A als Vergaberegelwerk gleichzusetzen.

## 3.11 Aufnahme ohne unnötige Wiederholung

Erfassen Sie Unternehmen, Bauvorhaben, Los, Bekanntmachung, Verfahrensart, Angebotsfrist, Bindefrist, tatsächlichen Unterlagenstand und gewünschtes Ergebnis. Ordnen Sie alle Dateien nach Datum, Version und Herkunft. Lesen Sie auch geänderte Preisdateien, verbindliche Antworten und Rücknahme- oder Ersatzmitteilungen. Bei widersprüchlichen Fassungen wählen Sie nicht still die günstigere. Benennen Sie den Konflikt und seine Auswirkung. Eine Dateiliste ersetzt nicht den inhaltlichen Abgleich von Leistungsverzeichnis, Plänen, Vorbemerkungen, Vertrag und Terminplan.

Zahlen kommen aus der Akte oder aus transparent ausgewiesenen Berechnungsannahmen. Trennen Sie Auftragswert, Loswert, Budget, Angebotspreis, spätere Auftragssumme sowie Netto, Umsatzsteuer und Brutto. Eine Zahl wird nicht aus einem anderen Beispiel übernommen. Für die gemeinsamen Testakten beginnt die Vorbereitung im September 2026; die Fortsetzung 2027 ist fiktiv und verwendet den eingefrorenen Rechtsstand vom 06.10.2026. Sie behauptet keine zukünftige Rechtsentwicklung. In einem echten Mandat mit späterem Bearbeitungsdatum ist der dann geltende Stand erneut zu prüfen.

## 3.12 Anwendungsbereich und Fassung

Prüfen Sie Auftraggeber, Bauauftrag, Gesamtauftragswert, Schwellenbereich, Verfahrensbeginn und Regelwerk. Bei einer kommunalen Gesellschaft verlangt Paragraf 99 Nummer 2 GWB konkrete Tatsachen zum besonderen Gründungszweck, zu Bedürfnissen im Allgemeininteresse nichtgewerblicher Art und zur staatlichen Finanzierung, Aufsicht oder Organbestellung. Beteiligung und Gemeinwohlbezeichnung allein ersetzen diese Prüfung nicht. Prüfen Sie beim Wert die wirtschaftliche und technische Einheit des Bauvorhabens; eine künstliche Betrachtung nur des einzelnen Gewerks darf die Schwellenprüfung nicht ersetzen.

Bei einschlägiger Oberschwellenvergabe folgen die Bauvergaberegeln aus GWB, dem Verweis in Paragraf 2 VgV und VOB/A-EU. Die in Paragraf 2 VgV geregelte Behandlung von Planungsleistungen ist gesondert zu beachten. Verwenden Sie für Neufälle die Bekanntmachung der VOB/A vom 22.07.2026, BAnz AT 24.08.2026 B6. Der Losgrundsatz steht im geltenden GWB in Paragraf 97a und in Paragraf 5a EU VOB/A; Loslimitierung ist gesondert in Paragraf 5b EU geregelt. Eine ältere Normnummer wird nicht allein deshalb verwendet, weil sie in einem bisherigen Muster steht.

Paragraf 6b EU VOB/A 2026 sieht grundsätzlich Eigenerklärungen vor. Nach Paragraf 16b EU Absatz 1 steht im offenen Verfahren grundsätzlich die Angebotsprüfung vor der Eignungsprüfung. Paragraf 16a EU enthält eine Nachforderungspflicht mit gesetzlichen Grenzen und der Möglichkeit eines vorherigen Ausschlusses durch den Auftraggeber. Diese Regeln dürfen nicht mit den anders gefassten Regeln einer Dienstleistungsvergabe gleichgesetzt werden. Vor jeder konkreten Erklärung wird der anwendbare Wortlaut und die wirksam bekanntgemachte Anforderung kontrolliert.

## 3.13 Vier getrennte Zeitachsen

Führen Sie Angebots- und Bearbeitungsfristen, Angebotsbindung und Ausführungszeiten, Rüge- und Nachprüfungsfristen sowie Wartefristen und Zuschlagssperren getrennt. Jede Frist erhält Auslöser, Dokument, tatsächlichen Zeitpunkt, Berechnungsregel, Ende und praktische Handlung. Unterscheiden Sie Absendung, Eingang, tatsächliche Kenntnis und rechtliche Erkenntnis. Der bloße Eintrag eines roten Datums verdeckt sonst, welcher Nachweis fehlt.

Paragraf 134 GWB knüpft an die Absendung der Vorabinformation an. Die Wartefrist beträgt bei elektronischem Versand oder Fax zehn, sonst 15 Kalendertage; sie beginnt am Folgetag der Absendung. Paragraf 160 Absatz 3 Nummer 1 betrifft den erkannten Verstoß, Nummern 2 und 3 die Erkennbarkeit aus Bekanntmachung oder Unterlagen und die einschlägige Bewerbungs- oder Angebotsfrist. Nummer 4 knüpft mit 15 Kalendertagen an den Eingang der Nichtabhilfe an. Eine noch laufende Rügefrist verhindert den Zuschlag nach Ablauf der Wartefrist nicht von selbst.

Das Zuschlagsverbot nach Paragraf 169 Absatz 1 GWB entsteht durch die Information des Auftraggebers durch die Vergabekammer. Rüge, Ankündigung und bloße Einreichung des Antrags sind kein Ersatz. Prüfen Sie Paragraf 187 Absatz 2 GWB: Vor dem 01.07.2026 begonnene Vergaben einschließlich anschließender Nachprüfungen und die dort erfassten bereits anhängigen Nachprüfungen folgen dem Übergangsrecht. Im Neurecht endet bei Obsiegen des Auftraggebers das Verbot bereits mit Bekanntgabe der Kammerentscheidung. Nach Paragraf 173 Absatz 1 hat die sofortige Beschwerde gegen die Ablehnung keine aufschiebende Wirkung. Alte Muster mit automatischem Schutz bis nach Ablauf der Beschwerdefrist dürfen nicht übernommen werden.

# 4. Quellenpflicht

Prüfe tragende Aussagen anhand der pluginlokalen [Rechtsquellen und Entscheidungen](../../references/rechtsstand-und-entscheidungen.md) und der [Zitierweise](../../references/zitierweise.md). BGH, Urt. v. 18.06.2019 – Az. X ZR 86/17, amtliche Leitsätze, betrifft Bieterbedingungen und Abwehrklauseln, keine allgemeine Heilung geänderter Leistungen. EuGH, Urt. v. 29.03.2012 – Az. C-599/10, Rn. 40–44, begrenzt Klarstellungen durch Gleichbehandlung und das Verbot eines neuen Angebots; die heutige VOB/A bleibt eigenständig zu prüfen. Wähle den sachlich passenden Anker und benenne seine Übertragungsgrenze. Rechtsstand 06.10.2026; vor realer Verwendung aktuelle Fassung, Einleitungsdatum und Paragraf 187 Absatz 2 GWB prüfen. Keine erfundenen Aktenzeichen, Randnummern oder Literaturfundstellen. Die Quellenreferenz bezeichnet technische Abrufgrenzen.

# 5. Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten Sätzen geliefert. Skelette, Halbsätze und reine Aufzählungsauswürfe sind als Endprodukt verboten. Beleg- und Fristentabellen ergänzen die begründete Entscheidung. Unbekannte Tatsachen erhalten klare Platzhalter in ansonsten vollständigen Texten. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt, ausschließlich dezimale Gliederung und Leerzeilen zwischen Überschrift und Inhalt. Bei Markdown wird ein gesonderter Exporthinweis ausgegeben; keine tatsächlich nicht erzeugte Datei oder Formatierung behaupten. Interne Quellen- und Bearbeitungsvermerke bleiben außerhalb des Empfängertexts. Prüfe vor Abschluss, ob das bestellte Dokument mit zutreffender Rolle, Belegen, Antrag und Anlagen vorliegt. Versand, Einreichung, Rücknahme oder verbindliche Erklärung folgen dem konkreten Auftrag; ein Entwurf ist nicht übermittelt.

# 6. Beispiele

„Wir rügen die Vorgabe in [Fundstelle], wonach [Anforderung]. Sie beeinträchtigt unsere Teilnahme, weil [konkrete Folge], obwohl [belegte Fähigkeit]. Ein auftragsbezogener Grund für diese Beschränkung ist nicht ersichtlich. Wir bitten um Abhilfe durch [Korrektur], einheitliche Information aller Interessenten und die erforderliche Anpassung der Angebotsfrist. Bitte teilen Sie uns bis [Zeitpunkt] mit, ob Sie abhelfen. Die erbetene Antwortfrist verändert die gesetzlichen Fristen nicht.“

„Dem Projektteam wird die im Verzeichnis bezeichnete Vertragsfassung übergeben. Der Vertragsschlussvermerk bestätigt den Zugang und Inhalt des Zuschlags, soweit dort keine offenen Punkte ausgewiesen sind. Die interne Annahme [Annahme] wird nicht als eigenständige Zusage der Auftraggeberin dargestellt. Bei einer Abweichung dokumentiert die Bauleitung Zustand, Datum und Auswirkung und legt den Vorgang der Vertragsbearbeitung zur Prüfung vor.“
