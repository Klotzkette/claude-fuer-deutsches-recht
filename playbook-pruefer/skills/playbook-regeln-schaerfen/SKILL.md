---
name: playbook-regeln-schaerfen
description: "Überführt vorhandene Verhandlungspositionen in einzelne prüfbare Regeln mit Geltungsbereich, Einheiten, Belegen sowie ausdrücklicher UND- oder ODER-Verknüpfung, ohne Standards stillschweigend zu ändern."
---

# Playbook-Regeln entscheidbar machen

## 1. Zweck und Anwendungsfall

Mache einen vorhandenen oder beauftragten Playbookentwurf prüfbar. Erhalte den materiellen Verhandlungswillen. Der Auftrag zum Strukturieren erlaubt nicht, eine rote Linie abzuschwächen oder eine zusätzliche Rückfallposition zu genehmigen.

## 2. Eingaben

Benötigt werden der vorhandene Wortlaut, Version und Zuständigkeit des Playbooks sowie der konkrete Vertragstyp. Nutze vorhandene Beispiele zur Auslegung; kennzeichne fehlende geschäftliche Entscheidungen.

## 3. Ablauf und Checkliste

1. Zerlege jedes Thema in genau bezeichnete Ausgangsposition, geordnete Rückfälle und mindestens eine rote Linie. Jede Position benötigt mindestens eine Regel. Ausgangs- und Rückfallpositionen verwenden `all`; rote Linien erhalten ausdrücklich `match_mode=all` oder `any`.
2. Formuliere jedes Prädikat positiv und prüfbar. Aus „nicht inakzeptabel unbegrenzt“ wird keine doppelte Negation. Eine rote Linie lautet beispielsweise „Der Vertrag erlaubt unbeschränktes KI-Training mit den erhaltenen Informationen.“
3. Trenne Gegenstand, Schwelle, Einheit, Zeitraum und Ausnahme. „Zehn Überstunden“ ist ohne Monat/Woche und Art der Abgeltung noch unklar. Teile mehrere selbständige Anforderungen in getrennte Regeln.
4. Frage bei „und/oder“ nach der tatsächlichen Verbotslogik, sofern sie sich nicht zuverlässig aus dem Playbook ergibt. Eine rote Linie `any` reagiert auf jedes selbständige verbotene Merkmal; `all` nur auf das vollständige kumulative Bild.
5. Dokumentiere Anwendungsbedingungen. Unbekannter Sachverhalt ist nicht gleich Nichtanwendbarkeit. Begründete Ausschlüsse werden separat geführt und dürfen den Nenner nicht heimlich verkleinern.
6. Prüfe Widersprüche: Kann eine zulässige Position gleichzeitig eine rote Linie erfüllen? Ist ein Rückfall schlechter als die rote Grenze? Stelle die konkrete Kollision zur Entscheidung; die strengere Zahl ist nicht automatisch die gewollte Regel.
7. Liefere eine versionierte Änderungsliste. Verwende [die gemeinsame Logik](../../references/prueflogik.md); soweit maschinenlesbare Ausgabe bestellt ist, halte das tatsächlich mitgelieferte Schema ein.

## 4. Quellenpflicht

Es gilt die [Zitierweise](../../references/zitierweise.md). Vertragsbefunde belegen den tatsächlichen Text; Playbookregeln belegen den Maßstab. Tragende Rechtsaussagen benötigen einschlägige aktuelle Normen und tatsächlich verifizierte Entscheidungen. Verwende [die Rechtsanker](../../references/rechtsprechungsanker.md) nur bei passender Frage und nach Prüfung des Originals; keine erfundenen Randnummern, Parallelfundstellen oder Literaturzitate.

## 5. Ausgabeformat

Erzeuge einen vollständig formulierten Playbookentwurf mit stabilen Themen-, Positions- und Regel-IDs, ausdrücklicher Logik und gezielter Entscheidungsliste. Ein technisches JSON kann zusätzlich erscheinen; es ersetzt die verständliche Beschreibung des Maßstabs nicht.

Die Ausformulierungspflicht gilt ausdrücklich: Endprodukte bestehen aus vollständigen, prägnanten Sätzen. Skelette, Halbsätze und reine Aufzählungs-Auswürfe sind als Endprodukt unzulässig. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Ohne echte Dateiformatierung steht dieser Wunsch in einem getrennten Exporthinweis. Eine nicht erzeugte Word- oder PDF-Datei wird nicht behauptet.

## 6. Beispiele

Die Vorgabe „keine unbegrenzte und verschuldensunabhängige Haftung“ ist mehrdeutig. Kläre, ob bereits jedes der beiden Merkmale verboten ist oder nur deren Kombination. Veröffentliche keine selbst gewählte ODER-Regel als ursprüngliche Mandantenvorgabe.
