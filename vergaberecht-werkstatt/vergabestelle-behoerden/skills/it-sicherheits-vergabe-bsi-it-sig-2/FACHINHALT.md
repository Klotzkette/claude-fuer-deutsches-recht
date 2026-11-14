---
name: it-sicherheits-vergabe-bsi-it-sig-2
description: "Auf Auftraggeberseite IT-Sicherheitsvergaben nach geltendem BSIG und NIS2 entwerfen: Statusbeleg, Schutzbedarf, funktionale SOC-Leistung, Eignung, Gleichwertigkeit, Qualitätswertung, Melde-Zuarbeit, Lieferkette, Exit und Vergabeakte."
---

# IT-Sicherheitsvergabe auf Auftraggeberseite

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Ziel

Der Skill übersetzt den realen Schutzbedarf einer Behörde oder eines regulierten Unternehmens in wettbewerbliche, messbare und später kontrollierbare Vergabeunterlagen. Maßgeblich ist das seit 06.12.2025 geltende BSIG; alte Normnummern aus dem IT-Sicherheitsgesetz 2.0 werden nur bei historischen Vorgängen verwendet.

## 1. Startakte

Vor Erstellung des Leistungsverzeichnisses werden sechs Belege abgelegt:

1. Auftraggeber- und Sektorenstatus,
2. begründete Einordnung nach §§ 28 und 29 BSIG oder dokumentiertes Nichtvorliegen,
3. Schutzbedarfs- und Risikoanalyse,
4. Ist-Architektur, Datenflüsse und Abhängigkeiten,
5. Auditfeststellungen, Vorfälle und Zielbetriebsmodell,
6. Marktübersicht zu leistungsfähigen Anbietern und gleichwertigen Nachweisen.

Ohne Status- und Schutzbedarfsbeleg dürfen weder KRITIS noch NIS2 als pauschale Begründung für eine wettbewerbsbeschränkende Muss-Anforderung verwendet werden.

## 2. Normenübersetzung

| Betreiberaufgabe | Norm | Beschaffbare Zuarbeit |
| --- | --- | --- |
| Risikomanagementmaßnahmen | § 30 BSIG | technische Kontrollen, Prozesse, Berichte und Wirksamkeitsnachweise |
| Besondere Pflichten kritischer Anlagen | § 31 BSIG | funktionsfähige Angriffserkennung, Tests, Protokollierung und Verbesserung |
| Gestufte Vorfallmeldung | § 32 BSIG | interne Frühinformation, Faktenpakete, Folgemeldung und Abschlussmaterial |
| Registrierung und Änderungen | § 33 BSIG | Stammdatenpflege und Änderungsmitteilung an Betreiber |
| Nachweisführung | § 39 BSIG | Auditunterstützung, Mängelplan und evidenzfähige Dokumentation |
| Kritische Komponenten | § 41 BSIG | Komponentenregister und risikobezogene Reaktion auf behördliche Entscheidung |

Die gesetzliche Verantwortung bleibt beim jeweiligen Normadressaten. Der Vertrag beschreibt deshalb konkrete Zuarbeit, Daten, Zeitpunkte und Freigaben, statt sämtliche BSIG-Pflichten undifferenziert auf den Auftragnehmer abzuwälzen.

## 3. Anforderungen richtig verorten

| Ebene | Zulässiger Inhalt | Fehlerbremse |
| --- | --- | --- |
| Eignung | Erfahrung, Personal, Managementsystem, technische Leistungsfähigkeit | nur auftragsbezogen und verhältnismäßig, § 122 Abs. 4 GWB |
| Mindestleistung | zwingende Funktionen und SLA | eindeutig, messbar und produktneutral, § 121 GWB, § 31 VgV |
| Zuschlag | nachweisbarer Mehrwert über Mindestniveau | Bewertungsstufen, Gewicht und Beleg vorab, § 127 GWB, § 58 VgV |
| Ausführung | Audit, Meldung, Unterauftragnehmer, Exit, Schwachstellen | kontrollierbar und mit Änderungsmechanik versehen |

Ein ISO-27001-Zertifikat wird nur verlangt, wenn Scope, Zeitpunkt und Gleichwertigkeit definiert sind. C5 wird als Testat mit Berichtstyp und Prüfungszeitraum bezeichnet. Ein bestimmtes Produkt, Rechenzentrum oder Herkunftsland darf nicht allein aus einer pauschalen Sicherheitsannahme vorgeschrieben werden.

## 4. Funktionale SOC-Leistungsbeschreibung

Die Vergabeunterlagen bestimmen mindestens:

- Systeme, Standorte, Protokollquellen und Mengengerüst,
- Abdeckung von IT und betrieblicher Technik,
- Erkennungs-, Priorisierungs- und Eskalationsprozess,
- Reaktionszeiten je Schweregrad mit Beginn, Ende und Ausnahmen,
- Beweissicherung, Aufbewahrung und Manipulationsschutz,
- Testfälle, Abnahme, Kennzahlen und Berichtswesen,
- Datenstandort, Schlüsselverwaltung und privilegierte Zugriffe,
- Unterauftragnehmer, Wechselverfahren und Lieferkettentransparenz,
- Exit, vollständiger Export, Übergabeunterstützung und Löschbeleg.

Ein SOC gilt nicht allein durch 24/7-Besetzung als System zur Angriffserkennung. Die Vergabestelle beschreibt die nach § 31 BSIG benötigten Funktionen und den Wirksamkeitsnachweis.

## 5. Qualitätswertung statt Billigstpreis

Beispielhafte, auftragsbezogene Wertungsdimensionen:

| Kriterium | Messbarer Nachweis | Bewertungsgrenze |
| --- | --- | --- |
| Erkennungsabdeckung | Testdatensatz und Regel-Mapping | keine Punkte für bloße Produktbeschreibung |
| qualifizierte Reaktion | Fallübung mit Zeitstempeln | Mindest-SLA bleibt Ausschlussgrenze |
| Wiederanlaufunterstützung | Szenario und Rollenplan | nur angebotene Ressourcen werten |
| Portabilität | Probeexport in offenem Format | Exit-Mindestanforderung nicht doppelt werten |
| Lieferkettenkontrolle | vollständige Komponenten- und Zugriffsübersicht | Herkunft allein ist kein Qualitätsmerkmal |

Bewertungsleitfaden, erwartete Belege, Gewichtung und Schwellen werden vor Veröffentlichung festgelegt. Die Einzelwertung muss die konkrete Angebotsaussage mit der Bewertungsstufe verbinden.

## 6. Melde- und Auditklausel

Der Auftragnehmer informiert die benannte Betreiberkontaktstelle so früh, dass diese ihre Pflichten nach § 32 BSIG prüfen und erfüllen kann. Die Klausel definiert Mindestinhalt, Aktualisierung, sichere Übertragung, Erreichbarkeit, Freigabe und Nachbereitung. Starre gesetzliche 24-Stunden-, 72-Stunden- und Monatsstufen werden vor Veröffentlichung am aktuellen Normtext geprüft; interne SLA liegen mit Sicherheitsabstand davor.

Nachweise für kritische Anlagen werden nach § 39 BSIG grundsätzlich im Dreijahresrhythmus geplant. Auditrecht, Mängelbeseitigung, Kosten und Zugriff auf Unterauftragnehmer werden verhältnismäßig geregelt.

## 7. Rechtsprechungsanker

- EuGH, Urteil vom 10.05.2012, C-368/10: technische oder qualitative Anforderungen müssen sachlich beschrieben und für gleichwertige Nachweise offen sein.
- EuGH, Urteil vom 04.12.2003, C-448/01: ein Zuschlagskriterium muss überprüfbar sein; die Vergabestelle muss seine Angaben kontrollieren können.
- BGH, Urteil vom 20.11.2012, X ZR 108/10: Anforderungen der Vergabeunterlagen aus Sicht eines fachkundigen Bieters objektiv auslegen; keine nachträgliche Verschärfung aus einem nur intern gemeinten Maßstab.

Jede Fundstelle wird vor Versand im Volltext verifiziert. Nicht bestätigte Vergabekammerentscheidungen werden nicht als Autorität verwendet.

## 8. Vergabeakte und Output

1. Status- und Schutzbedarfsvermerk,
2. Datenquellen- und Architekturmatrix,
3. Markt- und Gleichwertigkeitsanalyse,
4. Eignungs- und Nachweiskatalog,
5. funktionales Leistungsverzeichnis,
6. Qualitätsmatrix mit Bewertungsleitfaden,
7. Vertragsklauseln zu Meldung, Audit, Unterauftragnehmern und Exit,
8. Rügeantwort- und Änderungsvermerk,
9. maschinenlesbares Uploadpaket mit Versionen und Prüfsummen.

## Qualitätskontrolle

- Aktuelle Normen sind §§ 28 bis 33, 39 und 41 BSIG; alte §§ 8a, 8b und 9b werden nicht als geltendes Recht zitiert.
- Status, Schutzbedarf, Anforderung und Nachweis bilden eine belegte Kette.
- Eignung, Mindestleistung, Zuschlag und Ausführung sind nicht vermischt.
- Zertifikate und Testate werden fachlich korrekt bezeichnet und gleichwertige Nachweise behandelt.
- Der Zuschlag ermittelt den besten Sicherheits- und Leistungswert, nicht reflexhaft den niedrigsten Preis.
