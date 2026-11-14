---
name: richtlinien-anhoerung-red-aufsichtsrecht
description: "Erstellt einen prüfbaren Diff zwischen aktueller Aufsichtsquelle und interner Richtlinie."
---

# Richtlinien-Diff im Aufsichtsrecht

## 1. Ziel

Vergleiche nicht bloß Schlagwörter. Zerlege die aktuelle Primärquelle und die interne Richtlinie in atomare Anforderungen, verknüpfe jede Deckungsbehauptung mit einer Textstelle und unterscheide Dokumentenlücke, Prozesslücke und Wirksamkeitslücke.

## 2. Start

1. Alle vorhandenen Dateien und Links lesen.
2. Institutsart, Erlaubnis, DORA-Scope und Dokumentversion aus der Akte bestimmen.
3. Gewünschten Scope aus dem Auftrag ableiten.
4. Nur entscheidungserhebliche Lücken nachfragen.
5. Sofort eine Quellen- und Versionskarte liefern.

## 3. Quellen- und Versionskarte

| Dokument | Herausgeber | Fassung | Geltungsstatus | Adressat | Verwendeter Abschnitt |
| --- | --- | --- | --- | --- | --- |
| MaRisk | BaFin | RS 06/2024 (BA) | aktuelle Aufsichtspraxis | erfasste Institute | AT 6 |
| Interne IKS-Richtlinie | Institut | 3.1 | intern verbindlich | benannte Einheiten | 4.2 |

Bei einem älteren Rundschreiben zuerst feststellen, ob es historischer Vergleichsstand oder vermeintlicher Sollmaßstab ist. Historische Fassungen dürfen die aktuelle Soll-Spalte nicht ersetzen.

## 4. Diff-Methode

### 4.1 Soll-Seite

| Soll-ID | Fundstelle | Anforderung | Adressat | Ausnahme oder Proportionalität |
| --- | --- | --- | --- | --- |
| S-001 | MaRisk AT 6 Tz. 2 | wesentliche Handlungen und Festlegungen nachvollziehbar dokumentieren und grundsätzlich fünf Jahre aufbewahren | erfasstes Institut | längere gesetzliche Fristen unberührt |

### 4.2 Ist-Seite

| Ist-ID | Richtlinienstelle | Wortlaut | Prozessbeleg | Wirksamkeitsbeleg |
| --- | --- | --- | --- | --- |
| I-001 | 4.2 | vier Jahre | Archivklasse RM-04 | keine Stichprobe vorgelegt |

### 4.3 Verknüpfung

| Soll-ID | Ist-ID | Wortlaut | Umsetzung | Nachweis | Status | Änderung |
| --- | --- | --- | --- | --- | --- | --- |
| S-001 | I-001 | zu kurz | technisch umgesetzt | offen | ROT | mindestens fünf Jahre und Spezialfristen-Matrix |

Verwende ROT, ORANGE, GELB, GRÜN und GRAU statt Symbole. Ein GRAU-Status verlangt eine begründete Nichtanwendbarkeit; `nicht relevant` genügt nicht.

## 5. DORA- und xAIT-Weiche

1. DORA gilt seit dem 17. Januar 2025 für die in Artikel 2 genannten Finanzunternehmen.
2. Bei IKT-Governance, Vorfällen, Tests und IKT-Drittparteien zuerst DORA und die einschlägigen technischen Standards prüfen.
3. Ältere BAIT-, VAIT-, KAIT- und ZAIT-Texte nur nach dokumentierter Prüfung ihres aktuellen Scopes verwenden.
4. Nationale Organisations- und Auslagerungspflichten, insbesondere Paragrafen 25a und 25b KWG sowie MaRisk, daneben in ihrem verbleibenden Anwendungsbereich prüfen.
5. Doppelzählungen als dieselbe Lücke vermeiden; stattdessen Quellen kumulieren und den strengsten belegten Pflichtinhalt ausweisen.

## 6. Ergebnisformat

### 6.1 Kurzentscheidung

1. Aktuelle Sollquelle und Stichtag.
2. Anzahl der roten und orangen Lücken.
3. Unmittelbarer Handlungsbedarf.
4. Quellen- oder Scope-Restunsicherheit.

### 6.2 Änderungsauftrag

Für jede rote oder orange Zeile liefern:

1. Bestandsstelle.
2. präzisen Ersatz- oder Ergänzungstext.
3. Primärquelle.
4. Prozess- und Systemfolge.
5. Verantwortlichen und Freigabebedarf.
6. belegte Frist oder Kennzeichnung als laufende Pflicht.

## 7. Fachliche Anker

1. MaRisk RS 06/2024 (BA), insbesondere AT 6 für Dokumentation und grundsätzlich fünfjährige Aufbewahrung.
2. Paragraf 25a KWG für ordnungsgemäße Geschäftsorganisation und Risikomanagement.
3. Paragraf 25b KWG und MaRisk AT 9 für Auslagerungen.
4. DORA, Verordnung (EU) 2022/2554, und die einschlägigen technischen Standards für IKT-Risiken seit dem 17. Januar 2025.
5. EBA-Leitlinien nur mit aktueller Fassung, genauem Adressatenkreis und transparentem Rechtsstatus.

## 8. Primärquellen

1. BaFin, Rundschreiben 06/2024 (BA), MaRisk: https://www.bafin.de/SharedDocs/Downloads/DE/Rundschreiben/dl_rs_06_2024_MaRisk_pdf_BA.pdf
2. KWG Paragraf 25a: https://www.gesetze-im-internet.de/kredwg/__25a.html
3. KWG Paragraf 25b: https://www.gesetze-im-internet.de/kredwg/__25b.html
4. Verordnung (EU) 2022/2554: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
5. EBA, aktuelle Leitlinien und technische Standards: https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities

## 9. Fehlerbremsen

1. Aufbewahrungsfristen ausschließlich dem tatsächlich einschlägigen Modul und gegebenenfalls längeren Spezialgesetzen entnehmen.
2. Keine fiktive Datenklassifizierungspflicht oder Übergangsfrist erfinden.
3. Eine wortgleiche Richtlinie nicht ohne Umsetzungs- und Wirksamkeitsbeleg als grün bewerten.
4. BaFin-Verlautbarung, unmittelbar geltendes Unionsrecht und interne Best Practice nicht gleichsetzen.
5. Redline nur ausgeben, wenn sie Rolle, Handlung, Auslöser, Nachweis und Eskalation praktisch abbildet.
