---
name: hochrisiko-genauigkeit-konformitaetsbewertung
description: Bereitet Leistungs- und Sicherheitsnachweise für das konkrete Konformitätsverfahren auf. Ordnet Testmetriken, Versionsstand, Robustheit und Cybersicherheit den Anforderungen des Artikels 15 zu.
---

# Genauigkeit, Robustheit und Cybersicherheit nachweisen

## 1. Zweck und Anwendungsfall

Prüfe tatsächlich gemessene Eigenschaften statt ein abstraktes Qualitätsversprechen. Eine allgemeine Genauigkeitszahl oder ein Zertifikat beantwortet nicht die Leistungsfähigkeit im vorgesehenen Nutzungskontext.

## 2. Eingaben

Zweck, Version, Datenpopulation, Fehlerschäden, Metriken, Testdesign, Ergebnisse, Betriebsanleitung, Bedrohungsmodell, Schnittstellen und Änderungen. Fehlende Werte als fehlend ausweisen; keine Tests simulieren, wenn nur Texte geprüft werden.

## 3. Ablauf und Checkliste

### 3.1. Genauigkeit und Metriken

Artikel 15 Absatz 1 verlangt ein angemessenes Niveau von Genauigkeit, Robustheit und Cybersicherheit und beständiges Funktionieren im Lebenszyklus. Absatz 2 betrifft die Förderung von Benchmarks und Messmethoden durch die Kommission. Absatz 3 verlangt Angaben zu Genauigkeitsmaßen und relevanten Metriken in der Betriebsanleitung; er regelt nicht die Robustheit.

Metriken an Zweck, Datenpopulation und Fehlerschaden ausrichten. Präzision, Trefferquote oder falsch negative Ergebnisse nur verwenden, wenn sie die betreffende Gefahr abbilden. Aggregierte Erfolgsquoten können relevante Teilgruppen verdecken. Grenzwerte, Datentrennung, Stichprobenumfang und Auswertung vorab festlegen, nicht nach dem Ergebnis zurechtschneiden. Fehlende konkrete gesetzliche Zahlenwerte erlauben keine unbegründete Selbstfreigabe.

### 3.2. Robustheit nach Absatz 4

Fehler, Störungen und Unstimmigkeiten im System und in der Umgebung einschließlich Interaktion mit Menschen und anderen Systemen erfassen. Technische und organisatorische Maßnahmen prüfen: Sicherung, geordnetes Fehlverhalten, Redundanz und Störungspläne, soweit passend. Bei weiterlernenden Systemen verzerrte Rückkopplungsschleifen ausdrücklich untersuchen. Eine technisch mögliche Rückfallebene hilft nur, wenn sie erreichbar, sicher und tatsächlich erprobt ist.

### 3.3. Cybersicherheit nach Absatz 5

Angriffe auf Trainingsdaten, vortrainierte Komponenten, manipulierte Eingaben, vertrauliche Daten und Modellschwachstellen berücksichtigen. Schutz muss Verhinderung, Erkennung, Reaktion, Behebung und Kontrolle angemessen verbinden. Bei Agenten Werkzeugberechtigungen und nicht vertrauenswürdige Eingaben am realen Handlungspfad testen; konkrete Maßnahmen aus der Bedrohungsanalyse ableiten.

Andere Produkt- und Cybersicherheitsregime gesondert auf sachliche Ausnahmen, Übergangsrecht und Schnittstellen prüfen. Nicht allein aus der Bezeichnung Software ungeprüft alle Pflichten eines anderen Rechtsakts übernehmen.

### 3.4. Nachweise in die Freigabe überführen

Version, Testgrundlage, Ergebnis und Abweichung an Artikel-9-Risikomaßnahmen und die technische Dokumentation knüpfen. Bei fehlendem Test einen ausführbaren Testauftrag mit Erfolgskriterium und Verantwortlichem erstellen. Bei tatsächlich gemessener Abweichung die offene Konformitätsfrage benennen. Artikel 40 setzt für Vermutungswirkung eine passende veröffentlichte Norm und tatsächliche Abdeckung voraus; ein beliebiger Penetrationstest ist keine vollständige KI-Konformitätsbewertung. Anwendungsdatum nach Artikel 111 und 113 separat bestimmen.

## 4. Quellenpflicht

Artikel 9, 11, 15 Absätze 1 bis 5, 40 und 43. [Rechtsstand vom 9. Oktober 2026](../../references/rechtsstand-2026-10-09.md); [Zitierweise](../../references/zitierweise.md). Der Normtext wurde am 9. Oktober 2026 geöffnet. Vor späterer Anwendung Änderungen prüfen. Keine Entscheidung aus Modellwissen oder ein Datenschutzurteil als Entscheidung über die KI-Risikoklasse ausgeben.

## 5. Ausgabeformat

Ein Leistungs- und Sicherheitsvermerk mit höchstens vierspaltiger Matrix: Anforderung, Test/Nachweis, Ergebnis/Grenze, Maßnahme. Jede positive Aussage auf die tatsächlich geprüfte Fassung und Testreichweite begrenzen.

Das Endprodukt wird vollständig ausformuliert; Tabellen unterstützen die Begründung, ersetzen sie aber nicht. DOCX/PDF verwenden soweit möglich Times New Roman 11 pt und dezimale Gliederung. Bei Textausgabe den Formatwunsch als getrennten Exporthinweis nennen. Keine tatsächlich nicht erzeugte Datei, Prüfung oder behördliche Freigabe behaupten.

## 6. Beispiele

Ein Diagnostiksystem erreicht eine hohe Gesamtquote, versagt jedoch bei einer kleinen klinisch relevanten Gruppe. Die Gesamtquote schließt eine unzureichende Genauigkeit für den konkreten Zweck nicht aus; Datenlage und Fehlerschaden bestimmen die weitere Prüfung.
