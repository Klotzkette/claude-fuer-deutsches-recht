---
name: ins-aktienr-anleiheemission
description: "Ins 022 Aktienr Ckkauf, Ins 023 Anleiheemission: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 022 Aktienr Ckkauf, Ins 023 Anleiheemission

## Arbeitsbereich

Dieser Skill bündelt **Ins 022 Aktienr Ckkauf, Ins 023 Anleiheemission** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-022-aktienr-ckkauf` | Prueft Aktienrueckkaufprogramme auf MAR-Konformitaet: Safe Harbour DVO 2016/1052, Handelsverbote, Ad-hoc und Offenlegungspflichten. |
| `ins-023-anleiheemission` | Prueft insiderrechtliche Anforderungen bei Anleiheemissionen: Emittenten-Pflichten, Arranger-Pflichten, Market Sounding, Ad-hoc und Dual-Listing-Aspekte. |

## Arbeitsweg

Für **Ins 022 Aktienr Ckkauf, Ins 023 Anleiheemission** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-022-aktienr-ckkauf`

**Fokus:** Prueft Aktienrueckkaufprogramme auf MAR-Konformitaet: Safe Harbour DVO 2016/1052, Handelsverbote, Ad-hoc und Offenlegungspflichten.

# Aktienrückkaufprogramme – MAR Safe Harbour und Compliance

## Rechtlicher Rahmen

Aktienrückkaufprogramme können unter den Safe Harbour der DVO (EU) 2016/1052 fallen, wenn
Volumen-, Preis- und Timing-Beschränkungen eingehalten werden. Außerhalb des Safe Harbour
gelten die allgemeinen MAR-Verbote. Art. 5 MAR und DVO 2016/1052 regeln die Ausnahme
abschließend. Ankündigung des Programms ist in der Regel ad-hoc-pflichtig.

Rechtsgrundlagen:
- Art. 5 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/1052: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1052
- §§ 71–71e AktG: https://www.gesetze-im-internet.de/aktg/__71.html
- BaFin-Emittentenleitfaden Kap. VII: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Aktienrückkaufprogramme rechtskonform konzipiert,
angekündigt und durchgeführt werden, und prüft laufend Safe-Harbour-Konformität.

## Arbeitsprogramm

### Schritt 1 – Beschluss und Ermächtigung

- Hauptversammlungsermächtigung nach § 71 Abs. 1 Nr. 8 AktG vorhanden?
- Volumen (max. 10 % des Grundkapitals), Laufzeit (max. 5 Jahre) und Preisspanne definiert?
- Board-Beschluss zur Durchführung dokumentiert

### Schritt 2 – Ad-hoc-Ankündigung

- Bekanntgabe des Programms ist typischerweise ad-hoc-pflichtig, sobald Board-Beschluss
 vorliegt (nicht erst bei Start der Käufe)
- Inhalt: Volumen, Preisspanne, Zweck, Laufzeit, beauftragtes Institut

### Schritt 3 – Safe-Harbour-Bedingungen (DVO 2016/1052)

Tageskauf-Limit: max. 25 % des durchschnittlichen Tagesvolumens der letzten 20 Handelstage
Preislimit: Höchstkurs = letzter unabhängiger Abschlusskurs oder höchstes aktuelles unabhängiges
 Gebot (je nachdem, welches höher ist)
Keine Käufe:
 - Während eines Aufschubs nach Art. 17 Abs. 4 MAR (außer im Rahmen eines vorgefassten Plans)
 - In Closed Periods (Art. 19 Abs. 11 MAR, aber nur für PDMR, nicht für Emittenten-Programm direkt)
 - An Tagen, an denen Ad-hoc-Veröffentlichungen geplant sind

### Schritt 4 – Handelsverbote für PDMRs

- Emittent führt Rückkauf → keine MAR-Verletzung durch den Emittenten im Safe Harbour
- PDMRs: Eigene Handelsverbote bei Insiderinformation bleiben unberührt
- Keine PDMR-Eigengeschäfte parallel zum Rückkauf, wenn Insiderinformation besteht

### Schritt 5 – Laufende Offenlegung und Nachgang

- Tägliche Meldung der Rückkäufe an Handelsplatz (Art. 5 Abs. 3 MAR)
- Wöchentliche Veröffentlichung der aggregierten Rückkäufe auf Website
- Abschlussmitteilung am Ende des Programms
- Eigene Aktien: Eintrag ins Aktienregister, §§ 71 ff. AktG

## Red-Team-Fragen

- Wurde die Safe-Harbour-Bedingungen an jedem Handelstag eingehalten?
- Wurde das Programm bei Vorliegen einer Insiderinformation ausgesetzt?
- Enthält die Ad-hoc-Ankündigung alle Pflichtangaben?
- Werden Tages- und Wochenmeldungen rechtzeitig veröffentlicht?
- Liegt ein vorgefasster Rückkaufplan vor, der Käufe während Aufschub ermöglicht?

## Ausgabeformat

Erzeuge:
1. Safe-Harbour-Compliance-Checkliste (tagesaktuell)
2. Ad-hoc-Entwurf für Programmankündigung
3. Melde-Protokoll (tägliche und wöchentliche Offenlegung)
4. Programm-Abschlussprotokoll

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Aktienrückkäufe über ein separates Handelsmandat (Beauftragung eines unabhängigen
Intermediärs nach DVO 2016/1052) bieten zusätzlichen Safe-Harbour-Schutz, da die
Kaufentscheidung nicht mehr vom Emittenten direkt gesteuert wird. Das Mandat muss jedoch
vor Beginn einer Insiderphase erteilt worden sein und darf während der Insiderphase nicht
modifiziert werden. Compliance muss das Mandat regelmäßig auf Übereinstimmung mit dem
Safe Harbour prüfen.

Weitere Quellen:
- DVO (EU) 2016/1052: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1052
- §§ 71 ff. AktG: https://www.gesetze-im-internet.de/aktg/__71.html

## 2. `ins-023-anleiheemission`

**Fokus:** Prueft insiderrechtliche Anforderungen bei Anleiheemissionen: Emittenten-Pflichten, Arranger-Pflichten, Market Sounding, Ad-hoc und Dual-Listing-Aspekte.

# Anleiheemission – Insiderrechtliche Anforderungen

## Rechtlicher Rahmen

Bei Anleiheemissionen (Corporate Bonds, Schuldscheindarlehen, MTN-Programme) gelten MAR-
Pflichten für Emittenten, deren Schuldtitel an einem regulierten Markt oder MTF zugelassen sind.
Banken als Arrangeure oder Bookrunner unterliegen Art. 10 und Art. 11 MAR. Für nicht gelistete
Anleihen gilt MAR nicht unmittelbar, wohl aber für verbundene Aktien oder Derivate.

Rechtsgrundlagen:
- Art. 7, 11, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 2 MAR (Anwendungsbereich): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/960 (Market Sounding): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0960
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt, ob und in welchem Umfang MAR bei der Anleiheemission gilt, und steuert
die Compliance für Emittenten und Arrangeure.

## Arbeitsprogramm

### Schritt 1 – Anwendungsbereich MAR prüfen

- Ist die Anleihe an einem regulierten Markt (Frankfurter Wertpapierbörse, Euronext, etc.)
 oder einem MTF (Freiverkehr) zum Handel zugelassen?
- Falls ja: MAR gilt vollumfänglich für den Emittenten
- Falls nein (Schuldscheindarlehen, privat platziert): MAR gilt nicht direkt für die Anleihe,
 aber prüfe ob Aktien oder Derivate des Emittenten betroffen sind

### Schritt 2 – Insiderinformationen vor der Emission

- Hat der Emittent eine aktuelle Insiderinformation (z. B. Gewinnwarnung, M&A-Gespräche)?
- Wenn ja: Ad-hoc-Pflicht nach Art. 17 MAR kann Emissionsplanung konterkarieren
- Kein Aufschub möglich, wenn keine legitimen Gründe vorliegen
- Timing der Emission: Insiderinformation muss zuerst veröffentlicht werden

### Schritt 3 – Market Sounding für Anleihe

- Sondierung von institutionellen Investoren vor der Emission: Art. 11 MAR-Verfahren
- Welche Informationen im Sounding sind UPSI? (Typisch: Emissionsvolumen, Verwendungszweck,
 finanzielle Kennzahlen, die noch nicht öffentlich sind)
- Wall-Crossing-Dokumentation für alle gesoundeten Investoren

### Schritt 4 – Arrangeur-Pflichten

- Arrangeur als Sekundärinsider: Unterliegt Art. 14 MAR-Handelsverboten
- Chinese Wall zwischen Arrangeur-Team und anderen Bankbereichen
- Keine Eigengeschäfte in Aktien oder Derivaten des Emittenten auf Basis von UPSI
- Insiderliste des Arrangeurs muss alle informierten Mitarbeiter enthalten

### Schritt 5 – Ad-hoc und Prospekt

- Anleihe-Emission: Kein automatischer Ad-hoc-Auslöser, aber alle wesentlichen Umstände
 der Emission (Kondiktionen, Ergebnis) sind im Rahmen der allgemeinen Pflichten zu melden
- Prospektpflicht nach EU-Prospektverordnung: Parallel zu MAR-Compliance prüfen
- Ongoing-Disclosure: Kupon-Änderungen, Covenant Breaches → ggf. ad-hoc-pflichtig

## Red-Team-Fragen

- Wird MAR korrekt auf den Anwendungsbereich (gelistete vs. nicht-gelistete Anleihe) angewendet?
- Gibt es eine aktuelle Insiderinformation, die vor der Emission veröffentlicht werden muss?
- Wurden Arrangeur-Teams ordnungsgemäß über Insiderstatus informiert?
- Wurden Market-Sounding-Investoren in Insiderlisten aufgenommen?
- Besteht neben MAR auch Prospektpflicht (EU-Prospektverordnung)?

## Ausgabeformat

Erzeuge:
1. MAR-Anwendungsbereichs-Prüfung (Anleihe × Handelsplatz × MAR-Pflicht)
2. Market-Sounding-Protokoll für Anleihe (Art. 11 MAR-konform)
3. Arrangeur-Compliance-Checkliste
4. Zeitplan Insiderinformation → Ad-hoc → Emission

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.
