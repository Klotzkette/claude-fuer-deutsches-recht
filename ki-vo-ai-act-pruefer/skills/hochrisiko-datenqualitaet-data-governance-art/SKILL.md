---
name: hochrisiko-datenqualitaet-data-governance-art
description: Prüft Herkunft und Eignung von Entwicklungsdaten sowie die enge Erlaubnis für sensible Daten zur Verzerrungskorrektur nach Artikel 4a. Erstellt einen belegten Datenfreigabevermerk mit Alternativenprüfung, Zugriffsschutz und Löschereignis.
---

# 1. Dateneignung und Verzerrungskorrektur

## 1. Zweck und Anwendungsfall

Prüfe Datenqualität nach Artikel 10 und die seit 27. Juli 2026 geltende Erlaubnis des neuen Artikels 4a der Verordnung (EU) 2024/1689. Artikel 10 Absatz 5 ist nicht als unveränderte parallele Erlaubnis fortzuschreiben. Der Geltungsbeginn der Hochrisikoanforderungen und der bereits geltenden Datenregel sind verschieden.

## 2. Eingaben

Lies Datenkatalog, Modellzweck, Gruppenmerkmale, Erhebungsquellen, Nutzungsrechte, Validierung, Qualitätsberichte und Zugriffskonzept. Keine sensiblen Rohdaten allein zur Vervollständigung einer Checkliste anfordern. Fehlt ein Datenfluss, zunächst genau den fraglichen Import oder Empfänger klären.

## 3. Ablauf

1. Anbieter- oder Betreiberrolle sowie System- oder Modellbezug bestimmen. Artikel 4a Absatz 1 betrifft Hochrisikoanbieter; Absatz 2 auch andere Anbieter und Betreiber unter zusätzlichen Voraussetzungen.
2. Entwicklungszweck, Datenherkunft, Aufbereitung, Annahmen, Repräsentativität, fehlende Teilgruppen und Fehlerraten nach Artikel 10 erfassen. Überlappungen zwischen Training und Prüfung als Qualitätsrisiko belegen, nicht pauschal eine technisch unmögliche Fehlerfreiheit fordern.
3. Sensible Daten nach Artikel 9 Absatz 1 der Datenschutz-Grundverordnung einzeln identifizieren. Geschlecht, Alter und jede betriebliche Kennzahl sind nicht automatisch besondere Kategorien.
4. Bestimmte Verzerrung und deren Gefahren- oder Diskriminierungsbezug beschreiben. Eine allgemeine Produktoptimierung reicht nicht. Belegen, warum andere, synthetische oder anonymisierte Daten die Erkennung und Korrektur nicht gleich wirksam ermöglichen.
5. Sämtliche Sicherungen aus Artikel 4a Absatz 1 prüfen: Zweckbeschränkung und technische Weiterverwendungsgrenzen, geeignete Sicherheit einschließlich Pseudonymisierung, dokumentierte strenge Zugriffe, keine Weitergabe oder Zugriffseröffnung an andere Parteien, Löschung bei Korrektur oder früherem Ablauf der Speicherfrist und dokumentierte Unerlässlichkeit im Verarbeitungsverzeichnis.
6. Bei Absatz 2 zusätzlich die dort genannten Risiken für Gesundheit, Sicherheit, Grundrechte oder verbotene Diskriminierung prüfen, einschließlich möglicher Rückkopplung von Ausgaben in künftige Verarbeitung.
7. Datenschutzrechtliche Rechtsgrundlage, Informationspflichten, Betroffenenrechte, Dienstleister und gegebenenfalls Folgenabschätzung daneben prüfen. Die spezielle Ausnahme erlaubt nicht sämtliche Trainingszwecke oder uneingeschränkte Auftragsverarbeiterzugriffe.
8. Freigabe nach Zweck und Datenumfang begrenzen; Korrekturerfolg und Löschung nachhalten. Erfolgloser Test rechtfertigt keine endlose Vorratsspeicherung.

## 4. Quellenpflicht

[Rechtsstandkarte, Abschnitte 1.1, 1.2 und 1.4](../../references/digitaler-omnibus-2026.md), [Zitierweise](../../references/zitierweise.md). Verordnung (EU) 2026/1744, Artikel 1 Nummer 6; Datenschutz-Grundverordnung Artikel 5, 6, 9, 30, 32 und 35. Kein älteres Datenschutzurteil als Entscheidung über den neuen Artikel 4a ausgeben.

## 5. Ausgabeformat

Vollständig ausformulierter Datenfreigabevermerk mit Tabelle: Datenkategorie, Bias-Frage, Alternative, Unerlässlichkeit, Zugriff, Löschereignis, Beleg und verbleibende Sperre. Technische Lücken konkret benennen. Times New Roman 11 pt und dezimale Gliederung; bei Textausgabe Exporthinweis. Keine Datenübermittlung oder Freigabe ohne Auftrag.

## 6. Beispiele

Ein Recruiting-Anbieter will gruppenbezogene Benachteiligung untersuchen: erst Aussagekraft anonymer Auswertungen prüfen, dann gegebenenfalls eng begrenzte sensible Merkmale. Ein allgemeiner Chatbot-Anbieter darf Artikel 4a nicht als unbegrenzte Erlaubnis zum Training auf Gesundheitsakten behandeln.
