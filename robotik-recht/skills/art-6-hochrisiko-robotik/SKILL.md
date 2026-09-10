---
name: art-6-hochrisiko-robotik
description: Ordnet Roboterfunktionen nach Sicherheitsbezug, Produktregime und konkretem Einsatz ein. Berücksichtigt den geänderten Maschinenpfad und liefert einen begründeten Klassifikationsvermerk mit getrennten Produkt- und Systemfristen.
---

# 1. Hochrisikoeinstufung von Roboterfunktionen

## 1. Zweck und Anwendungsfall

Bestimme die regulatorische Route einer konkreten Roboterfunktion. Nicht jeder lernende Roboter ist ein Hochrisikosystem und nicht jede Maschine unterliegt zusätzlich sämtlichen Systempflichten. Maßgeblich ist die Verordnung (EU) 2024/1689 in der Fassung 2026/1744.

## 2. Eingaben

Funktionsbeschreibung, Sicherheitskonzept, Fehlermöglichkeiten, Herstellererklärung, Produktregime, Steuerungsversion und Einsatzort lesen. Bei einem Unfall zuerst vorhandene Logs unverändert sichern; keine neue gefährliche Versuchsfahrt veranlassen.

## 3. Ablauf

1. Funktion isolieren: kollisionsvermeidende Steuerung, Navigation, Arbeitsgeschwindigkeit, reine Qualitätskontrolle oder Personenerkennung. Anbieter, Integrator und Betreiber zuordnen.
2. Artikel 6 Absätze 1a bis 1c prüfen. Eine ausschließlich nicht sicherheitsbezogene Optimierungsfunktion ist kein Sicherheitsbauteil. Gefährdet ihr Ausfall aber Gesundheit oder Sicherheit, greift diese Entlastung nicht. Drittprüfung ausschließlich wegen nicht sicherheitsbezogener Funk- oder EMV-Risiken genügt ebenfalls nicht für Absatz 1 Buchstabe b.
3. Maschinenverordnung (EU) 2023/1230 nun in Anhang I Abschnitt B einordnen. Artikel 2 Absatz 2 und die geänderten Maschinenanforderungen anwenden, nicht weiterhin automatisch den Abschnitt-A-Pfad nach Artikel 43 Absatz 3. Keine zusätzliche Pflicht aus einem überholten Anhang ableiten.
4. Andere Produktregime getrennt halten: Ein Medizinroboter kann unter MDR und Anhang I Abschnitt A fallen. Eine Logistikmaschine wird nicht wegen eines Krankenhausstandorts automatisch zum Medizinprodukt.
5. Eigenständigen Anhang-III-Verwendungszweck prüfen, etwa biometrische Klassifikation oder Personalbewertung. Die Produktabgrenzung allein beantwortet nicht jede separat betriebene Bewertungsfunktion.
6. Termine auseinanderhalten: Maschinenverordnung grundsätzlich ab 20. Januar 2027; für die nach Artikel 113 verschobenen Kapitel-III-Abschnitte Anhang III ab 2. Dezember 2027, Anhang I ab 2. August 2028. Artikel 111 und sektorspezifische Übergänge hinzunehmen. Arbeitsschutz, Betriebssicherheit, Datenschutz und bestehende Produktsicherheit laufen weiter.
7. Zuständige Stelle aus dem tatsächlichen Produkt- und Systemregime bestimmen. Nach KI-MIG ist die Bundesnetzagentur Auffangbehörde, nicht pauschal Marktüberwacher aller Maschinen. Sektorale Produktaufsicht und Länderzuständigkeit zuerst abgrenzen.
8. Nachweisproblem präzisieren: Welcher Ausfallpfad und welche Sicherheitsfunktion tragen die Einordnung? Betriebsanleitung gegen tatsächliche Konfiguration und vorhersehbare Fehlanwendung halten. Bei Unklarheit konkrete technische Nachweise anfordern, keine pauschale vorsorgliche Zertifizierung empfehlen.

## 4. Quellenpflicht

[Rechtsstandkarte](../../references/digitaler-omnibus-2026.md), Artikel 2 und 6, Anhänge I und III, Verordnung (EU) 2023/1230 in aktueller Fassung sowie Paragraf 2 KI-MIG. Eine Ermächtigung zu künftigen delegierten Rechtsakten ist noch keine geltende Befreiung.

## 5. Ausgabeformat

Ausformulierter Klassifikationsvermerk mit Funktion, Fehlerfolge, Produktregime, Systemrolle, Termin und zuständiger Stelle. Eine Funktionsmatrix darf ergänzen. Keine CE-Erklärung oder technische Sicherheitsfreigabe ohne Nachweise. Times New Roman 11 pt, dezimale Gliederung; bei fehlendem Export vollständigen Text liefern.

## 6. Beispiele

Eine reine Sortierstatistik und die sichere Geschwindigkeitsregelung desselben Roboters sind getrennt zu betrachten. Eine Softwareänderung, die auf den Bremsweg wirkt, verlangt eine neue Bewertung des Sicherheitsbezugs; das Etikett „Komfortupdate“ genügt nicht.
