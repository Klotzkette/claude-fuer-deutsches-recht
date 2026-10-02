---
name: regeln-beurteilen
description: "Bewertet jede anwendbare Regel belegt als erfüllt, nicht erfüllt oder nicht prüfbar; rote Linien behalten dieselbe wörtliche Logik und werden als erkannt oder nicht erkannt angezeigt."
---

# Jede Playbook-Regel beurteilen

## 1. Zweck und Anwendungsfall

Subsumiere jede anwendbare Regel unter den konkreten Vertragstext. Der Skill liefert vollständige Einzelbewertungen; Themenrisiko und Gesamtfreigabe folgen erst aus der getrennten Aggregation.

## 2. Eingaben

Benötigt werden Playbook-Version, eindeutiger Vertragsverbund, Belegkarten und begründete Anwendungsbereiche. Eine unbelegte Behauptung aus dem Vorlauf bleibt zu prüfen.

## 3. Ablauf und Checkliste

1. Vergleiche das positive Regelprädikat mit dem gesamten relevanten Klauselinhalt. Entscheide intern `met`, `not_met` oder `not_verifiable`. `pending` bezeichnet nur noch unbearbeitete Regeln im Zwischenstand.
2. Zeige Ausgangs- und Rückfallregeln als Erfüllt/Nicht erfüllt an. Zeige rote Linien als Erkannt/Nicht erkannt an. Drehe ihre Bedeutung nicht um: zwei erkannte verbotene Merkmale bleiben zwei erfüllte Redline-Prädikate.
3. Begründe jeden Befund mit Vertragssatz, Fundort und konkretem Soll-Ist-Vergleich. Eine Zahl ohne Bezugszeitraum oder eine Ausnahme ohne vollständigen Verweis reicht nicht.
4. Unterscheide nachgewiesenes Fehlen von fehlender Prüfbarkeit. Bei vollständigem Vertrag kann das Fehlen einer verlangten Klausel ein entschiedenes `not_met` begründen. Bei fehlender Vertragsanlage bleibt der betroffene Punkt offen.
5. Bewerte alle Regeln, auch nach dem ersten schwerwiegenden Treffer. Überspringe Rückfälle nicht allein deshalb, weil die Ausgangsposition erfüllt scheint; sie gehören zum angeforderten vollständigen Positionsvergleich.
6. Führe ausgeschlossene Regeln mit Grund getrennt. Halte die Regel-ID-Menge vollständig. Ein finaler Lauf enthält keine `pending`-Regeln; ein unklarer Sachverhalt wird ausdrücklich `not_verifiable` mit konkretem Klärungsbedarf.
7. Nutze [die verbindliche Prüflogik](../../references/prueflogik.md). Eine Rechenroutine kann Zähler prüfen, aber keine unbelegte juristische Subsumtion ersetzen.

## 4. Quellenpflicht

Es gilt die [Zitierweise](../../references/zitierweise.md). Vertragsbefunde belegen den tatsächlichen Text; Playbookregeln belegen den Maßstab. Tragende Rechtsaussagen benötigen einschlägige aktuelle Normen und tatsächlich verifizierte Entscheidungen. Verwende [die Rechtsanker](../../references/rechtsprechungsanker.md) nur bei passender Frage und nach Prüfung des Originals; keine erfundenen Randnummern, Parallelfundstellen oder Literaturzitate.

## 5. Ausgabeformat

Liefere je anwendbarer Regel eine vollständige Regelkarte mit Status, Originalbeleg, ausformulierter Subsumtion und gegebenenfalls gezielter Rückfrage. Stelle Prüfmaßstab und Rechtskontrolle getrennt dar.

Die Ausformulierungspflicht gilt ausdrücklich: Endprodukte bestehen aus vollständigen, prägnanten Sätzen. Skelette, Halbsätze und reine Aufzählungs-Auswürfe sind als Endprodukt unzulässig. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Ohne echte Dateiformatierung steht dieser Wunsch in einem getrennten Exporthinweis. Eine nicht erzeugte Word- oder PDF-Datei wird nicht behauptet.

## 6. Beispiele

Die rote Linie lautet „Das NDA erlaubt die Nutzung zu beliebigen Geschäftszwecken“. Steht diese Erlaubnis eindeutig im Vertrag, lautet ihr Ergebnis „Erkannt“, nicht „Nicht erfüllt, weil unerwünscht“.
