---
name: ki-system-betriebsfreigabe-entscheiden
description: "Prüft die Betriebsfreigabe einer konkreten KI-Systemversion für Pilot, Produktivstart, Update oder Wiederanlauf. Bewertet die Wirkung auf Entscheidungen sowie Hochrisiko, Übergangsrecht, KI-Kompetenz, Aufsicht, Datenschutz und Beteiligung. Liefert einen Freigabe- oder Aussetzungsvermerk mit Abnahmetests, Zuständigkeiten und Fristen."
---

# Über die Betriebsfreigabe eines KI-Systems entscheiden

## 1 Zweck und Anwendungsfall

Entscheiden Sie für Legal und Compliance, welche konkrete Systemversion in welchem Verfahren, an welchem Standort und mit welchen Daten tatsächlich eingesetzt werden kann. Der Skill eignet sich für einen ersten Piloten, den Wechsel in die Produktion, ein Funktionsupdate und die erneute Freigabe nach einem Vorfall. Nennen Sie zuerst die engste verantwortbare Einsatzoption und den entscheidenden Nachweis. Für die allgemeine Werkzeugauswahl oder eine isolierte Personalmaßnahme nutzen Sie den passenden Fachweg in [KI-Einsatz und Freigabe](../ki-einsatz-und-freigabe/SKILL.md).

## 2 Eingaben

- Bestimmen Sie verantwortlichen Rechtsträger, Standort, System- und Konfigurationsstand, Herstellerzweck, tatsächlichen Verwendungszweck, betroffene Gruppen, Freigabebefugnis und geplanten ersten Einsatz. Erfassen Sie auch Datenquellen, Schnittstellen, Übermittlungen, Berechtigungen und die Stelle, an der ein Ergebnis Wirkung entfaltet.
- Verlangen Sie die Bedien- und Anbieterunterlagen, Verträge und Freigaben, Datenfluss, Regel- und Berechtigungsexporte, Protokolle, eine Arbeitsprobe mit gewöhnlichen Benutzerkonten, den Beteiligungsstand und die geplante Rückfallebene. Ziehen Sie Vorversion und Änderungsliste heran, wenn sich der Einsatzzweck oder die Systemwirkung geändert hat.
- Bei knapper Akte beginnen Sie mit belegten Befunden, einer vorläufigen Entscheidung und der wichtigsten offenen Nachforderung. Trennen Sie Nutzerauftrag, Aktenbehauptung, Primärbeleg und Annahme. Arbeiten Sie neue Stücke in den laufenden Vermerk ein und halten Sie fest, welche Bedingung dadurch erfüllt, verschärft oder weiterhin offen ist.

## 3 Ablauf und Checkliste

### 3.1 Einsatzgrenze und tatsächliche Wirkung

Rekonstruieren Sie den Weg von Eingabe und Verarbeitung bis zur menschlichen Prüfung, Übernahme und Außenwirkung. Lesen Sie Konfiguration, Logs und Fachablauf zusammen. Halten Sie für Test und Produktion fest, wer Ergebnisse sehen kann und wohin sie geschrieben oder exportiert werden können. Prüfen Sie insbesondere unsichtbare Vorauswahl, automatisch ausgelöste Nachrichten, Datenexporte und nachgelagerte Änderungen an Listen, Schichten, Entgelt oder Kundenakten. Stützen Sie sich auf einen protokollierten Test des tatsächlichen Ablaufs mit gewöhnlicher Rolle, Standort und Schicht. Dokumentieren Sie Anzeige, verfügbare Entscheidungsalternativen, Korrekturmöglichkeit, Befugnis und Zeit bis zur Wirkung.

| Betriebsart | Was vor dem Start nachzuweisen ist |
| --- | --- |
| Isolierter Test mit synthetischen Daten | Erlaubte Testumgebung, ausschließlich freigegebene Testdaten, getrennte Konten und technisch gesperrte Produktiv- und Ausgabepfade. |
| Paralleltest mit echten Daten | Zulässiger Datenfluss und Beteiligungsstand, definierte Vergleichsgrundlage und wirksame Abschottung vom operativen Ablauf. Prüfen Sie auch manuelle Übernahmen und Exportrechte. |
| Erprobung vor Inverkehrbringen oder Inbetriebnahme unter Realbedingungen | Prüfen Sie, ob ein Test unter Realbedingungen nach Art. 60 und 61 KI-VO vorliegt. Prüfen Sie bei Anwendbarkeit Rolle des Anbieters, Testplan, behördliches Verfahren, Registrierung, Einwilligung und Reversibilität. |
| Produktiver Betrieb | Abnahme genau der eingesetzten Konfiguration und aller zugelassenen Rollen, Daten und Ausgabepfade. |

### 3.2 Rolle, Risikoklasse und Zeitpunkt

1. Bestimmen Sie den Anbieter und jeden Betreiber für das konkrete System nach Art. 3 KI-VO. Prüfen Sie bei Umwidmung, erheblicher Änderung oder Betrieb unter eigenem Namen gesondert die Voraussetzungen eines Rollenwechsels nach Art. 25. Dokumentieren Sie zuerst etwaige Verbote nach Art. 5 mit dem jeweiligen Anwendungsbeginn.
2. Prüfen Sie bei Auswahl und Einstellung Anhang III Nr. 4 Buchst. a und bei Arbeitsbedingungen, Beförderung, Beendigung, verhaltens- oder merkmalsbezogener Aufgabenzuweisung und Leistungsüberwachung Buchst. b. Ordnen Sie den tatsächlichen Zweck und Einfluss zu. Bei behaupteter Ausnahme nach Art. 6 Abs. 3 prüfen Sie, ob ein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte ausgeschlossen werden kann und eine der konkreten Ausnahmealternativen erfüllt ist. Bei Profiling natürlicher Personen greift diese Ausnahme für ein in Anhang III aufgeführtes System nicht. Fordern Sie bei Berufung auf die Ausnahme die Anbieterbewertung nach Art. 6 Abs. 4 an.
3. Führen Sie je Version getrennt das belegte Datum des Inverkehrbringens oder der Inbetriebnahme, das Änderungsdatum und den Beginn der jeweiligen Pflicht. Nach Art. 113 Abs. 3 Buchst. c KI-VO in der Fassung der VO (EU) 2026/1744 gelten die dort bezeichneten Vorschriften, darunter Art. 26 für Systeme nach Art. 6 Abs. 2 in Verbindung mit Anhang III, grundsätzlich ab 2. Dezember 2027. Prüfen Sie für ein davor in Verkehr gebrachtes oder in Betrieb genommenes System Art. 111 Abs. 2 und eine spätere erhebliche Änderung der Konzeption. Ein Wechsel von einer Anzeige verfügbarer Schichten zur personenbezogenen Zugangssperre verlangt einen eigenen Funktionsvergleich. Prüfen Sie den aktuellen Rechtsstand für das Falldatum.
4. Erfassen Sie für anwendbaren Art. 26 insbesondere Betriebsanleitung, befugte und sachkundige menschliche Aufsicht mit Unterstützung, Eignung und Repräsentativität der vom Betreiber kontrollierten Eingabedaten, Betriebsüberwachung, Protokollzugriff und Aufbewahrung. Prüfen Sie nach Abs. 6 die mindestens sechsmonatige Aufbewahrung der automatisch erzeugten Protokolle unter Kontrolle des Betreibers unter Berücksichtigung abweichender anwendbarer Vorgaben. Legen Sie bei Beschäftigungs-KI den Zeitpunkt und Empfängerkreis der Information nach Art. 26 Abs. 7 fest. Die Information muss bei Anwendbarkeit vor Inbetriebnahme oder Verwendung die Arbeitnehmervertretung und die betroffenen Arbeitnehmer erreichen. Prüfen Sie bei Entscheidungen über natürliche Personen auch Art. 26 Abs. 11.
5. Planen und dokumentieren Sie nach dem einschlägigen Stand des Art. 4 KI-VO Maßnahmen zur Unterstützung der KI-Kompetenz. Kapitel I gilt seit dem 2. Februar 2025. Prüfen Sie am Falltag den Wortlaut, einschließlich der Änderung durch die VO (EU) 2026/1744. Ordnen Sie sie den tatsächlichen Aufgaben, Vorkenntnissen, Risiken und betroffenen Personen zu. Testen Sie im jeweiligen Arbeitsablauf, ob Anwender falsche Ergebnisse erkennen, korrigieren und die Nutzung unterbrechen können. Teilnahme und dokumentierte praktische Leistung haben verschiedene Aussagekraft. [KI-VO in konsolidierter Lesefassung](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/deu/pdf) · [Änderungsverordnung (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/deu/pdf)

### 3.3 Beschäftigte, Datenschutz und Beteiligung

Prüfen Sie Verarbeitung, Zweck, Verantwortlichen, Rechtsgrundlage, Datenminimierung, Transparenz, besondere Datenkategorien, Auftragsverarbeitung, Drittlandtransfer und Schutzmaßnahmen. Halten Sie fest, ob und bis wann der Verantwortliche eine Datenschutz-Folgenabschätzung vor Verarbeitung vorlegen muss. Klären Sie gegebenenfalls vorab die Konsultation nach Art. 36 DSGVO. Ein Schattenbetrieb mit echten Daten bleibt insoweit eine Verarbeitung.

Prüfen Sie Art. 22 DSGVO am tatsächlichen Ergebnis für die Person. Wer sieht die vorab ausgeschlossenen Kandidaten oder Beschäftigten, kann die Datenbasis hinterfragen, kann rechtzeitig korrigieren und tut dies in der Praxis? Welche Schicht-, Vergütungs- oder Beschäftigungsfolgen treten ein? Untersuchen Sie Ausschließlichkeit und rechtliche oder ähnlich erhebliche Wirkung gesondert. Besteht eine Ausnahme nach Art. 22 Abs. 2, prüfen Sie die jeweils vorgeschriebenen Garantien sowie Abs. 4. Der EuGH erfasst in C-634/21 den dortigen Score bei maßgeblicher Abhängigkeit der Entscheidung eines Dritten. Übertragen Sie den Maßstab nur nach Prüfung der tatsächlichen Rolle des Scores. [DSGVO, insbesondere Art. 22 und 35–36](https://eur-lex.europa.eu/eli/reg/2016/679/oj/deu) · [EuGH C-634/21, Rn. 43–50 und 73](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A62021CJ0634)

Führen Sie § 90 Abs. 1 Nr. 3 und Abs. 2 BetrVG für rechtzeitige Unterrichtung und Beratung bei der Planung, § 87 Abs. 1 Nr. 6 BetrVG für die einschlägige technische Überwachung und § 95 Abs. 2a BetrVG bei KI-gestützter Aufstellung von Auswahlrichtlinien als getrennte Prüfschritte. Prüfen Sie je nach Projekt Berufsbildung, Arbeitszeit und Betriebsänderung gesondert. Nennen Sie je Schritt den zuständigen Betriebsrat, erforderliche Unterlagen, belegten Stand und den letzten sinnvollen Termin. Der Entscheidungsvermerk unterscheidet die Beteiligungsart von der Information nach Art. 26 Abs. 7 KI-VO. [BetrVG](https://www.gesetze-im-internet.de/betrvg/BJNR000130972.html)

### 3.4 Abnahme, Gegenprobe und Vollkosten

Vereinbaren Sie Abnahmekriterien vor der Messung mit Fachprozess und zuständiger Freigabestelle. Verwenden Sie je Test einen Beleg mit Versionsstand, Szenario, Erwartung und Fehlerschwere, gewöhnlicher Rolle, Stichprobenbasis, Ist-Ergebnis, Prüfer, Zeitpunkt und Nachtest. Die Fälle sollen den Regelbetrieb sowie Fehler mit schwerer Wirkung abdecken. Prüfen Sie insbesondere fehlende Daten, eine plausible Falschausgabe, verborgene Vorauswahl, widersprüchliche Quellen, nachgelagerten Versionswechsel, Ausfall des Freigebenden und den manuellen Rückfall. Ermitteln Sie die tatsächlich geprüften Fälle je Schicht, Standort und Risikoklasse. Kennzeichnen Sie getrennt, wo nur Protokolle, synthetische Läufe oder Administratorkonten vorliegen.

- Führen Sie bei einem Produktivlauf mindestens eine unabhängige Gegenprobe mit der normalen Betriebsrolle durch. Der Prüfer soll einen kritischen Fehler erkennen, die Wirkung rechtzeitig blockieren und den Vorgang ohne das KI-System geordnet übernehmen können. Halten Sie die Belege jedes Schritts fest.
- Vergleichen Sie die wirkliche Nettoentlastung auf vergleichbaren Fällen mit dem bisherigen oder einem risikoärmeren Ablauf. Legen Sie Bearbeitung, Prüfung, Nacharbeit und Ausnahmebehandlung getrennt offen. Medianvorteile im Standardfall und schwere Fehler in der kleinen Randfallprobe bleiben getrennt sichtbar. Geben Sie ausdrücklich an, was sich aus der Stichprobe über den Regelbetrieb ableiten lässt.
- Stellen Sie der Anbieterangabe oder dem günstigsten Betriebsszenario die stärkste Gegenprobe gegenüber. Prüfen Sie etwa, ob ein angeblicher Override nur mit Adminrechten funktioniert oder der Pilotzugang bereits mit der Personaleinsatzplanung verbunden ist. Bei ungeklärtem Befund zeigen Sie die konkrete Freigabefolge.

### 3.5 Entscheidung, Aussetzung und Wiederanlauf

Wählen Sie je Einsatzumfang eine klar bezeichnete Empfehlung. Ein isolierter Test kann mit nachgewiesener Abschottung freigegeben werden. Eine Produktiventscheidung bleibt zurückgestellt, solange notwendige Rechts-, Beteiligungs- oder Testnachweise fehlen. Eine produktive Freigabe bezeichnet abschließend Version, Daten, Standorte, Rollen, Zweck, Rückfallweg, verantwortliche Betriebsstelle und Prüfdatum. Halten Sie erforderliche Freigaben und deren Entscheidungsgrundlage getrennt von Fachstellungnahmen fest. Der Prozesseigner belegt fachliche Eignung und Rückfallweg. Der Systembetrieb legt Konfiguration und Protokolle vor. Der Verantwortliche klärt den Datenschutz mit Beratung durch den Datenschutzbeauftragten. HR oder die zuständige Arbeitgeberstelle führt die Beteiligung durch. Ordnen Sie die Entscheidung der nach Akte befugten Stelle zu und prüfen Sie Stellvertretung und Erreichbarkeit.

Empfehlen Sie bei kritischer Abweichung eine sofortige Aussetzung des betroffenen Pfads. Benennen Sie die befugte Person für Sperre, manuelle Weiterführung, Sicherung der betroffenen Entscheidungen und Schutz der Betroffenen. Halten Sie fest, wer offene Vorgänge prüft und fehlerhafte Wirkungen korrigieren kann. Bei anwendbarem Art. 26 Abs. 5 prüfen Sie das Risiko im Sinne des Art. 79 Abs. 1 mit Aussetzungs- und Unterrichtungspflicht sowie einen schwerwiegenden Vorfall mit eigenem Unterrichtungspfad. Bewerten Sie etwaige Datenschutzmeldungen gesondert nach Art. 33 und 34 DSGVO. Weisen Sie Fristen, Empfänger, Grundlage und zuständige Stelle aus. Entwerfen Sie Mitteilungen im beauftragten Umfang. Die befugte Person entscheidet und handelt.

Lassen Sie den Wiederanlauf von einer dokumentierten Ursachenbehebung, einem bestandenen Nachtest im ursprünglichen Fehlerpfad sowie im Rückfallpfad und einer erneuten Freigabe abhängen. Änderungen an Zweck, Daten, Modell, Filtern, Rolle oder Schnittstellen werden auf Freigaberelevanz geprüft. Bestimmen Sie in der Vorlage für jeden Beleg einen verantwortlichen Lieferanten, eine Frist, den unabhängigen Prüfer und die Stelle für die nächste Entscheidung.

## 4 Quellenpflicht

Belegen Sie technische Tatsachen mit Originaldatei und Fundstelle, etwa Logereignis mit Uhrzeit und Zeitzone, Testlauf, Tabellenzeile oder Versions-ID. Geben Sie für Rechtsfragen Norm, Fassung, Anwendungsdatum, amtliche Quelle und Prüftag an. Nennen Sie die Grenze jeder entscheidungstragenden Schlussfolgerung. Kennzeichnen Sie Rechtsquellen, die mangels Zugriffs am Falltag noch geprüft werden müssen. Beachten Sie die [Zitierweise](../../references/zitierweise.md) und bei Personalfolgen den [Prüfpfad KI und Arbeit](../../references/ki-arbeit-pruefpfad.md).

## 5 Ausgabeformat

Liefern Sie einen unterschriftsreifen **internen Entscheidungsentwurf** mit Entscheidungssatz, beantragtem Umfang, Begründung aus Akten und Gegenbeleg, Rechtsstand, Bedingungen, Zuständigen, Fristen, Sperre und Wiederanlauf. Fügen Sie für die Abnahme eine kurze Belegmatrix bei. Nutzen Sie dafür die Spalten »Anforderung«, »Soll und Test«, »Ist mit Fundstelle«, »Freigabefolge« und »Verantwortung und Termin«. Benennen Sie im Entscheidungssatz jede unzulässige oder offene Teilfunktion und die zulässige Zwischenlösung.

Für das Endprodukt gilt die Ausformulierungspflicht. Schreiben Sie in vollständigen Sätzen. Skelette, Halbsätze und reine Aufzählungen genügen als Endprodukt nicht. Formatieren Sie das Enddokument soweit technisch möglich in Times New Roman 11 pt mit ausschließlich dezimaler Gliederung. Geben Sie den Formatstandard bei reiner Textausgabe als getrennten Exporthinweis an.

## 6 Beispiele

| Hamelner Fall | Konkrete Betriebsfrage |
| --- | --- |
| ME-05 | Weisen Sie nach, ob die Vorauswahl den Zugang zum nächsten Auswahlschritt begrenzt. Prüfen Sie Alternativsicht, Pilotvertrag und gewöhnliche Rolle. |
| ME-29 | Legen Sie Standardfallvorteil und aufwendige Fehlerkorrekturen aus dem Paralleltest nebeneinander. Entwerfen Sie den engen Betriebsumfang oder die Zwischenlösung mit Nachtest. |
| ME-30 | Verfolgen Sie den Versionswechsel zwischen Prüfung und Ausgang. Testen Sie, ob die tatsächlich versandte Fassung an ihre Freigabe gebunden ist. |
| ME-31 | Sichern Sie den tatsächlichen Uploadpfad und begrenzen Sie die Wiederfreigabe auf belegte Konten, Datentypen und Berechtigungen. |
| ME-32 | Lassen Sie die Nachtschicht mit ihren tatsächlichen Rechten die Nutzung unterbrechen und den Ersatzablauf ausführen. |
| ME-33 und ME-34 | Legen Sie Qualifizierungs-, Weiterbeschäftigungs- und Beteiligungsfragen gesondert vor und machen Sie ihre Folgen für die Umstellung sichtbar. |
| ME-35 | Vergleichen Sie die Version zur Anzeige freier Schichten mit der personenbezogenen Filterversion. Prüfen Sie die Wirkung auf Prämien- oder Schichtzugang, den echten Override, den Stichtag und den Zeitpunkt der Information. |

Ein möglicher Entscheidungssatz für einen fehlerhaften Schichtfilter folgt.

»Die Einsatzplanung verwendet den personenbezogenen Filter bis zur erneuten Entscheidung nicht. Sie besetzt offene Schichten im dokumentierten manuellen Verfahren. Der Systembetrieb weist bis zum nächsten Freigabetermin in einem Test mit dem regulären Schichtkonto nach, dass die Einsatzplanung ausgeschlossene Personen rechtzeitig sehen, den Vorschlag ändern und den gesamten Vorgang ohne Filter abschließen kann. HR prüft parallel, ob frühere Schichtentscheidungen neu bewertet werden müssen.«
