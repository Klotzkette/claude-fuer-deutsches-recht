---
name: 49-kontoermittlung-und-drittauskunft
description: "Verwenden nur nach Titel, wenn Bank, Arbeitgeber oder andere pfändbare Spur unbekannt ist und eine konkrete Vollstreckung deshalb stockt. Prüft Voraussetzungen und zulässigen Weg für Drittauskunft nach Paragraf 802l ZPO, Schuldnerverzeichnis und Kontenabruf und erzeugt einen datensparsamen Ermittlungsplan. Nicht für offene Forderungen ohne Titel."
---

# Kontoermittlung und Drittauskunft

## Zweck und Anwendungsfall

Dieser Skill wird nach einem Titel genutzt, wenn die Zahlung nicht freiwillig erfolgt und Vollstreckungsinformationen fehlen.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Vollstreckungstitel.
- Bekannte Schuldnerdaten aus SAP und Mietakte.
- Bisherige Zahlungen und Bankverbindungen.
- Ergebnis früherer Vollstreckungsversuche.
- Vollstreckungsauftrag, Vermögensauskunft oder Nachweis, warum Drittauskunft erforderlich ist.
- Bei Lohnpfändung: Auszahlungszeitraum, bereinigtes Nettoeinkommen, Zahl und Status gesetzlich unterhaltsberechtigter Personen sowie aktuelle amtliche Pfändungstabelle.
- Geplantes Datum und Übermittlungsform eines Pfändungs- und Überweisungsantrags.

## Ablauf / Checkliste

1. Positiven Titelumfang, Zustellung, Vollstreckbarkeit und aktuelle Restforderung vor jeder Ermittlung prüfen; Unterliegensanteile sind tabu.
2. Bekannte Kontodaten aus Mietzahlungen rechtmäßig prüfen und dokumentieren.
3. Vermögensauskunft als Basisweg prüfen. Den Vollstreckungsauftrag und den konkreten Auslöser nach Paragraf 802l Abs. 1 S. 2 ZPO dokumentieren: unzustellbare Ladung trotz der dort vorgeschriebenen aktuellen Anschriftsermittlung, Nichtabgabe der Vermögensauskunft oder voraussichtlich unzureichende Befriedigung aus den dort aufgeführten Vermögensgegenständen.
4. Drittauskünfte nur im gesetzlichen Umfang vorbereiten: derzeitige Arbeitgeberdaten bei Rentenversicherung oder gegebenenfalls bezeichneter berufsständischer Versorgungseinrichtung, Kontenstammdatenabruf über das Bundeszentralamt für Steuern und Fahrzeug-/Halterdaten beim Kraftfahrt-Bundesamt. Die Auskunft liefert keine Kontostände und ersetzt keinen Pfändungsbeschluss.
5. Arbeitgeber-, Renten- oder Sozialleistungshinweise aus der Akte rechtlich vorsichtig behandeln; Herkunft, Aktualität und Verifikationsstatus ausweisen.
6. Bei Arbeitseinkommen die seit 01.07.2026 geltende Pfändungsfreigrenzenbekanntmachung 2026 verwenden. Der monatliche Grundbetrag beträgt 1.587,40 EUR, die Erhöhung für die erste unterhaltsberechtigte Person 597,42 EUR und für die zweite bis fünfte Person jeweils 332,83 EUR; die amtliche Tabelle bleibt maßgeblich. Nettoeinkommen, Auszahlungszeitraum, Unterhaltspflichten, eigene Einkünfte und Sonderregeln prüfen; nie aus dem Grundbetrag allein einen Pfändungsbetrag errechnen.
7. PfÜB-Normstichtag setzen: Bis 30.09.2026 keine Erleichterung des neuen Paragrafen 829a ZPO anwenden. Ab 01.10.2026 bei elektronischem Antrag Übereinstimmung der elektronischen Dokumente mit Titel, Klausel und Urkunden sowie Fortbestand der Forderung versichern, Vollstreckungskosten mit Aufstellung und Belegen nachweisen und Änderungen unverzüglich nachmelden. Das Gericht kann weitere Dokumente oder Schriftstücke anfordern.
8. PDF/XML nach Paragraf 829 Abs. 5 ZPO erst ab 01.01.2027 verwenden. Werden dann PDF und XML parallel übermittelt, ist nach der beschlossenen Fassung XML maßgeblich; vor diesem Stichtag keine XML-Vorranglogik ausgeben.
9. Datenschutz und Zweckbindung dokumentieren.
10. Vollstreckungsstrategie an Skill `48` zurückgeben.
11. Drittauskunft nach Paragraf 802l ZPO nur bei Titel, Vollstreckungsauftrag, Erforderlichkeit und einem belegten Tatbestand des Absatzes 1 Satz 2 vorbereiten.
12. Keine informellen Konto-, Arbeitgeber- oder Sozialdatenrecherchen empfehlen.
13. Keine frühere 500-EUR-Mindestforderung anwenden. Die aktuelle Fassung des Paragrafen 802l ZPO enthält keine solche Wertgrenze; erforderlich bleiben Vollstreckungszweck und einer der Tatbestände des Absatzes 1 Satz 2. Normstand und Formularvorgaben vor dem Auftrag trotzdem live prüfen.
14. Bankdaten aus früheren Mietzahlungen nur für die titulierte Forderungsdurchsetzung und mit Zweckbindungsvermerk verwenden.
15. Drittauskünfte, Schuldnerverzeichnis und Melderegister nicht durch freie Internetrecherche ersetzen.
16. Bei Teilabweisung, offener Rechtsmittelfrist oder unklarem Tenor zuerst Skill `08-eskalation-an-anwalt`, danach erst Ermittlungsplan.
17. Ermittlungs- und Pfändungskarte mit Titelrest, Maßnahme, Normstichtag, Einreicherrolle, Quelle, Freigrenzentabelle, Übermittlungsweg, Datenschutzstatus und genau einer nächsten Aktion ausgeben.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert. Pfändungsfreigrenzen und elektronische PfÜB-Stichtage werden zusätzlich nach `references/rechtsstand-2026-verfahren-vollstreckung.md` geprüft.

ZPO-Vermögensauskunft, Drittauskunft und Datenschutz mit Normanker. Keine Umgehung, keine informellen Ausforschungen, keine Altfassungen ungeprüft übernehmen.

## Ausgabeformat

Ermittlungsplan mit zulässiger Quelle, Zweck, Voraussetzung, Normanker, Formular-/Antragsweg, Titelumfang, Risiko, nächstem Antrag und Datenschutzvermerk.

## Beispiele

- Mieter zahlte früher per SEPA: Bankverbindung für PfÜB prüfen.
- Keine Kontodaten: Vermögensauskunft und Drittauskunft vorbereiten.
- Urteil nur teilweise gewonnen: Drittauskunft nur für den positiv titulierten Betrag.
- Arbeitgeber bekannt und Lohnpfändung ab August 2026: amtliche Tabelle ab 01.07.2026 anwenden; Grundbetrag nicht als fertigen Pfändungsbetrag behandeln.
