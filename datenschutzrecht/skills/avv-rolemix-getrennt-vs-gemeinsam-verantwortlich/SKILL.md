---
name: avv-rolemix-getrennt-vs-gemeinsam-verantwortlich
description: Klärt Datenschutzrollen je Verarbeitungsschritt bei Cloud-Diensten, Agenten und verbundenen Unternehmen. Prüft tatsächliche Zweck- und Mittelentscheidung statt Vertragsüberschrift und liefert Rollenvermerk, Anbieterfragen oder passende Vereinbarung.
---

# 1. Verantwortlichkeit in mehrstufigen Datenwegen bestimmen

## 1. Zweck und Anwendungsfall

Entscheide, wer für welchen Verarbeitungsschritt verantwortlich ist und welche Vereinbarung dazu passt. Weder gemeinsamer wirtschaftlicher Nutzen noch technische Verbindung allein begründet gemeinsame Verantwortlichkeit. Auch ein autonomer Agent wird nicht selbst Verantwortlicher nach Artikel 4 Nummer 7 DSGVO.

## 2. Eingaben

Lies Leistungsbeschreibung, Konfiguration, Weisungen, Datenfluss, Aufbewahrung, Unterauftragnehmerliste und Aussagen zur Trainingsnutzung. Frage bei einer Agentenkette gezielt, welcher Rechtsträger Eingaben, Gedächtnis, Werkzeugaufrufe und Protokolle erhält und wofür. Ein fehlender Nachweis wird als Lücke benannt; keine tatsächlich nicht gelesene Architektur behaupten.

## 3. Ablauf und Checkliste

### 3.1. Verarbeitung abgrenzen

Prüfe zuerst Personenbezug und Verarbeitung nach Artikel 4 Nummern 1 und 2; nicht „immer ja“ annehmen. Trenne Erhebung, Bereitstellung, Inferenz, Weiterleitung, Speicherung und Training. Ein lokales System ohne Personenbezug eröffnet nicht allein wegen der Bezeichnung Agent die DSGVO. Eine lokale Installation mit personenbezogenen API-Aufrufen ist dagegen kein vollständig abgeschotteter Betrieb.

### 3.2. Entscheidungsmacht nachweisen

Ermittle für jeden Schritt Zweck, betroffene Personen, Datenarten, Empfänger und wesentliche Mittel. Technische Detailentscheidungen können dem Auftragsverarbeiter verbleiben. Vergütung und eigene IT-Infrastruktur machen ihn nicht schon zum Verantwortlichen. Tatsächliche eigene Zwecke, etwa produktübergreifendes Training, sind separat einzuordnen; Artikel 28 Absatz 10 bei eigenmächtiger Zweckbestimmung prüfen.

Bei gemeinsamer oder zusammenwirkender Festlegung von Zwecken und wesentlichen Mitteln Artikel 26 prüfen. Gleich starke Einflussnahme oder Zugang jedes Beteiligten zu sämtlichen Daten ist nicht Voraussetzung. Bloßer Datenaustausch oder beiderseitiger Nutzen genügt nicht. Zeitliche und sachliche Reichweite begrenzen: Mitentscheidung über Erhebung belegt nicht automatisch Mitverantwortung für jedes spätere Training.

### 3.3. Modell, Anwendung und Werkzeuge trennen

Ein Agent ist keine zusätzliche juristische Person zwischen Auftraggeber und Lieferant. Bei mehreren Agenten jede delegierte Funktion und den dahinterstehenden Rechtsträger prüfen. Der Entwickler eines lokal verwendeten Modells erhält nicht notwendig Daten; ein Diagnose- oder Suchdienst kann dagegen Empfänger sein. Anbieter-/Betreiberrollen nach Systemrecht sind keine Abkürzung für Datenschutzrollen. Automatische Auswahl eines Werkzeugdienstes beseitigt die Verantwortung für die eingerichtete Auswahl- und Zugriffsmöglichkeit nicht.

### 3.4. Konsequenzen ausformulieren

Bei Auftragsverarbeitung Artikel 28 Absatz 3 und Unterbeauftragung nach Absätzen 2 und 4 umsetzen. Bei gemeinsamer Verantwortlichkeit Pflichten, Betroffenenkontakt und wesentlichen Inhalt der Vereinbarung nach Artikel 26 ordnen; Betroffenenrechte bleiben gegenüber jedem Verantwortlichen bestehen. Bei getrennten Verantwortlichen Übermittlungs- und Empfangsgrundlage, Information und Löschung eigenständig prüfen. Eine Vereinbarung schafft keine fehlende Rechtsgrundlage.

Für Inferenz, Gedächtnis, Protokolle und Training je Zweck Artikel 6, gegebenenfalls Artikel 9 und Kapitel V untersuchen. Berechtigtes Interesse ist kein pauschales Trainingsprivileg; Zweck, Erforderlichkeit und Abwägung getrennt belegen. Nach Anbieterantwort den Rollenvermerk und die konkret betroffene Vertragsklausel abschließen, nicht nur eine neue Fragenliste erzeugen.

## 4. Quellenpflicht

Artikel 4 Nummern 7 und 8, Artikel 5, 6, 9, 26, 28 und 44 folgende [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de); [EDSA-Leitlinien 07/2020](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020-concepts-controller-and-processor-gdpr_en) als nicht gesetzesgleiche Auslegungshilfe.

EuGH, Urteil vom 05.06.2018 - Az. C-210/16, ECLI:EU:C:2018:388, Wirtschaftsakademie: Entscheidung zur Richtlinie 95/46/EG, kein allgemeines Agentenurteil. Aussage und Übertragungsgrenze in der [Quellenprüfung](../../references/fanpage-entscheidung-quellenpruefung.md) beachten. Aktuelle Rollen aus Tatsachen und geltender DSGVO herleiten; kein bloßer Fallnamenbeweis. Prüfstand der Agentenergänzung: 2. Oktober 2026. [Zitierweise](../../references/zitierweise.md).

## 5. Ausgabeformat

Ausformulierter Rollenvermerk, Nachforderung oder Vereinbarung nach Auftrag. Ergänzend eine knappe Tabelle: Verarbeitung, Rechtsträger, Entscheidung, Rolle, Beleg und Konsequenz. Vollständige Sätze statt Skeletten, Times New Roman 11 pt, dezimale Gliederung. Keine Datenübertragung oder verbindliche Freigabe ohne Auftrag.

## 6. Beispiele

Ein Anbieter verarbeitet Kundenanfragen weisungsgebunden, nutzt Diagnosekopien aber für eigene Produktentwicklung: Rollen für beide Zwecke getrennt prüfen. Ein Modell läuft lokal, während ein Agent Adressen an einen Kartenservice übermittelt: nicht aus „On-Premise“ auf fehlenden Empfänger oder Transfer schließen.
