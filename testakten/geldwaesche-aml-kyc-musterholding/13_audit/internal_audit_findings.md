# Internes Audit-Memo: AML/GwG-Compliance – Musterholding GmbH

**Memo-Nr.:** AUDIT-MH-2026-01
**Erstellt von:** Interne Revision (Leitung: Petra Hoffmann, Prüferin: Markus Schild)
**Mitwirkung:** Thomas Eckhardt (Geldwäschebeauftragter), RA Dr. Franziska Heller (externe Beraterin)
**Datum des Audits:** 28.05.2026
**Prüfzeitraum:** 01.01.2025 – 26.05.2026
**Adressaten:** Klaus-Dieter Brenner, Sabine Wollner (Geschäftsführung); Thomas Eckhardt (GwB)
**Verteilerstufe:** Streng vertraulich / nur Adressaten
**Rechtsgrundlage:** § 6 Abs. 2 Nr. 2 GwG (interne Grundsätze und Kontrollen); BaFin-AuA GwG

---

## 1. Prüfungsauftrag und Umfang

Die interne Revision hat auf Anordnung der Geschäftsführung und auf Empfehlung der externen Anwältin RA Dr. Heller eine vollständige AML/GwG-Compliance-Prüfung durchgeführt. Anlass war die Häufung compliance-relevanter Sachverhalte im April/Mai 2026 (Danube Trade Solutions SRL, Drittzahlung, Transparenzregister-Unstimmigkeit, Behördenauskunftsersuchen).

**Prüfungslinien:**
1. Vollständigkeit und Aktualität der Risikoanalyse
2. KYC-Prozesse und Dokumentationsqualität
3. PEP/Sanktionsscreening-Prozesse
4. Transaktionsmonitoring
5. Schulungsdokumentation
6. Transparenzregister-Compliance
7. Verdachtsmeldungsprozesse
8. Archivierung und Aufbewahrungsfristen

**Prüfmethodik:** Dokumentenrevision, Stichproben aus KYC-Akten (25 Kunden), Interview mit GwB (Thomas Eckhardt), Interview mit Vertrieb (3 Mitarbeiter), Interview mit Buchhaltung (2 Mitarbeiter), Abgleich Monitoringsystem-Logs (LSEG World-Check, internes TM-System).

---

## 2. Zusammenfassung der Findings

### Überblick

| Finding-Nr. | Prüfungslinie | Schwere | Status |
|---|---|---|---|
| F-1 | Fehlende Vier-Augen-Dokumentation bei False-Positive-Freigaben | Hoch | Offen → Maßnahme eingeleitet |
| F-2 | Veraltete Registerauszüge in KYC-Akten | Mittel | Offen → Prüfung läuft |
| F-3 | Monitoring-Regeln erfassen Drittzahler unzureichend | Hoch | Offen → Systemanpassung geplant |
| F-4 | Schulungsnachweise 2022–2023 unvollständig | Mittel | Geheilt (Schulung 26.05.2026) |
| F-5 | Verdachtsentscheidungen nicht einheitlich dokumentiert | Mittel | Offen → Formular eingeführt |
| F-6 | Transparenzregister Tochtergesellschaft nicht aktuell | Hoch | Geheilt (Meldung 10.05.2026) |
| F-7 | Risikoanalyse 2024 nicht auf aktuellem Stand | Mittel | Geheilt (Neufassung 15.05.2026) |
| F-8 | Keine dokumentierte GF-Genehmigung bei PEP-Freigabe (1 Fall) | Mittel | Offen → Nachholung geplant |

---

## 3. Detailbeschreibung der Findings

### F-1: Fehlende Vier-Augen-Dokumentation bei False-Positive-Freigaben

**Befund:** Bei der Überprüfung der Sanktionsscreening-Protokolle der letzten 12 Monate wurden 10 Screening-Treffer identifiziert. In 7 Fällen erfolgte eine Freigabe als False Positive. In 3 dieser 7 Fälle fehlt eine dokumentierte Vier-Augen-Entscheidung (d.h. kein Protokoll mit Unterschrift zweier zuständiger Personen). Betroffen ist insbesondere der aktuelle Fall Blue Harbor Holdings Ltd., bei dem die Freigabe zunächst nur durch den GwB erfolgte, ohne Unterzeichnung der Geschäftsführung.

**Risikobewertung:** Hoch. Eine nicht belegte Vier-Augen-Entscheidung ist ein typisches Audit-Finding, das Aufsichtsbehörden als systemischen Fehler werten. Es besteht das Risiko, dass im Falle einer BaFin- oder RP-Prüfung ein Bußgeld verhängt wird.

**Ursache:** Das interne Screening-System generiert zwar automatische Alert-E-Mails, enthält aber kein Pflichtfeld für eine Zweit-Genehmigung. Die manuelle Dokumentation wurde nicht konsequent durchgeführt.

**Maßnahme:** Einführung eines standardisierten Freigabeformulars (Anlage A) mit Pflichtfeldern für zwei Unterschriften (GwB + GF oder Stellvertreter). Retrospektive Nachholung fehlender Freigaben. Implementierung einer Workflow-Stufe im Screening-System, die eine Zweit-Freigabe technisch erzwingt.

**Frist:** Retrospektive Nachholung bis 10.06.2026; technische Umsetzung bis 30.06.2026.

---

### F-2: Veraltete Registerauszüge in KYC-Akten

**Befund:** Stichprobenhaft wurden 25 KYC-Akten geprüft. In 9 Akten (36 %) war der Handelsregisterauszug des Kunden älter als 12 Monate. In 3 Akten (12 %) war er älter als 24 Monate. Nach BaFin-AuA GwG (2021) sollen Registerauszüge bei Hochrisikokunden mindestens jährlich und bei Standardrisikokunden mindestens alle drei Jahre erneuert werden.

**Risikobewertung:** Mittel. Veraltete Unterlagen können dazu führen, dass Veränderungen der Eigentümerstruktur oder des Geschäftsgegenstands des Kunden unbemerkt bleiben.

**Maßnahme:** Einrichtung einer automatischen Fälligkeitsliste im CRM-System, die 60 Tage vor Ablauf der Gültigkeitsperiode einen Alert an den GwB sendet. Sofortige Erneuerung der ältesten 3 Registerauszüge (priorisiert nach Risikoeinstufung Hochrisiko).

**Frist:** Fälligkeitsliste bis 30.06.2026; sofortige Erneuerung bis 15.06.2026.

---

### F-3: Monitoring-Regeln erfassen Drittzahler unzureichend

**Befund:** Das interne Transaktionsmonitoring-System enthält keine spezifische Regel, die eine Drittzahlung (Zahlung von einer anderen Person als dem Vertragspartner) automatisch als Hochrisiko-Alert eskaliert. Im aktuellen Fall (Adriatic Commerce Ltd.) wurde der Alert durch eine Kombination aus Betragshöhe und Neukundenregel generiert, nicht durch eine dedizierte Drittzahler-Regel. Die Drittzahlung hätte damit bei einem niedrigeren Betrag oder einem Bestandskunden unter Umständen keinen Alert erzeugt.

**Risikobewertung:** Hoch. Drittzahlungen sind eines der zentralen Geldwäscherisiken und müssen systemseitig klar erfasst werden.

**Maßnahme:** Implementierung einer neuen Monitoring-Regel (TM-R-001-NEW: Auftraggeber ≠ in CRM hinterlegter Vertragspartner → automatischer Hochrisiko-Alert, unabhängig vom Betrag). Test im Sandbox-System durch IT bis 20.06.2026; Produktivschaltung bis 30.06.2026.

**Frist:** 30.06.2026.

---

### F-4: Schulungsnachweise 2022–2023 unvollständig

**Befund:** Für den Schulungszyklus 2022 und 2023 liegen keine vollständigen Teilnehmerlisten vor. Von der E-Learning-Schulung 2022 existieren Auswertungen für 54 von 68 zum damaligen Zeitpunkt relevanten Mitarbeitern; 14 Lücken sind nicht erklärbar. Im Jahr 2023 wurde keine formale AML-Schulung dokumentiert.

**Risikobewertung:** Mittel. Unterlassene Schulungsnachweise sind nach § 56 GwG bußgeldbewehrt. Da die Lücken in der Vergangenheit liegen, können sie nicht rückwirkend geheilt werden; die aktuelle Schulung (26.05.2026) schließt die Lücke prospektiv.

**Maßnahme:** Die Schulung vom 26.05.2026 ersetzt nicht rückwirkend fehlende Nachweise, dient aber als Ausgangspunkt für eine lückenlose Dokumentation ab sofort. Der Maßnahmenplan für 2022/2023 ist mit dem RP Darmstadt im Antwortschreiben offen kommuniziert worden. Einführung eines Pflicht-E-Learning-Systems mit automatischer Protokollierung.

**Status:** Prospektiv geheilt durch Schulung 26.05.2026.

---

### F-5: Verdachtsentscheidungen nicht einheitlich dokumentiert

**Befund:** Bei der Prüfung der internen Entscheidungsdokumentation zu Verdachtsfällen (Zeitraum 01.01.2025–26.05.2026) wurden 4 Fälle identifiziert, bei denen die Entscheidung, keine Verdachtsmeldung zu erstatten, nicht schriftlich begründet wurde. Dies ist ein Risiko, weil im Nachhinein nicht nachweisbar ist, warum der GwB eine Meldung als nicht erforderlich angesehen hat.

**Maßnahme:** Einführung eines standardisierten Entscheidungsformulars (Anlage B) für alle Verdachts­prüfungen mit den Feldern: Sachverhaltsdarstellung, geprüfte Red Flags, Begründung Meldepflicht ja/nein, Vier-Augen-Unterschrift, Datum. Gültigkeit ab sofort; alle laufenden Prüfungen nachzudokumentieren.

**Frist:** Sofort.

---

### F-6: Transparenzregister Tochtergesellschaft nicht aktuell

**Befund:** Die Eintragung im Transparenzregister für die Musterholding Immobilien GmbH entsprach seit dem Treuhandvertrag vom September 2022 nicht mehr den tatsächlichen wirtschaftlichen Eigentumsverhältnissen. Der eingetragene UBO Werner Pfaff (67 %) entsprach nicht mehr der tatsächlichen Struktur (34 % Pfaff, 33 % Pfaff-Lehmann über Treuhand).

**Maßnahme:** Unstimmigkeitsmeldung nach § 23a GwG am 10.05.2026 eingereicht. Korrekturantrag in Vorbereitung (Notartermin 19.05.2026).

**Status:** Geheilt (Meldung erstattet, Korrektur eingeleitet).

---

### F-7: Risikoanalyse nicht auf aktuellem Stand

**Befund:** Die Risikoanalyse vom März 2024 enthielt keine differenzierte Betrachtung der Vertriebskanäle, keine aktuelle Länderrisikobeurteilung und keine separate Betrachtung der Immobilientochter. Eine anlassbezogene Aktualisierung nach dem Auftreten des Hochrisikofalls (April 2026) wurde nicht sofort, sondern erst im Mai 2026 vorgenommen.

**Maßnahme:** Neuversion RA-MH-2026-02 am 15.05.2026 erstellt und von GF genehmigt. Jährliche Aktualisierungspflicht und anlassbezogene Pflicht zur Anpassung werden in interne Richtlinie aufgenommen.

**Status:** Geheilt.

---

### F-8: Fehlende GF-Genehmigung bei PEP-Freigabe

**Befund:** In einem Vorfall aus dem Oktober 2025 (Bestandskunde, PEP-ähnlicher Treffer) wurde die Entscheidung zur Fortführung der Geschäftsbeziehung durch den GwB allein getroffen, ohne dokumentierte GF-Genehmigung. § 15 Abs. 4 Nr. 2 GwG verlangt bei PEP explizit eine Genehmigung durch die Geschäftsführungsebene.

**Maßnahme:** Retrospektive Genehmigung durch GF wird nachgeholt. Schulung des GwB und der GF über Genehmigungspflicht bei PEP.

**Frist:** Nachholung bis 10.06.2026.

---

## 4. Gesamtbewertung AML-Reifegrad

| Bereich | Bewertung | Trend |
|---|---|---|
| Risikoanalyse | Gut (nach Aktualisierung) | Verbessert |
| KYC-Prozesse | Mittel | Verbesserungsbedarf |
| Screening-Prozesse | Mittel | Verbesserungsbedarf |
| Transaktionsmonitoring | Mittel | Verbesserungsbedarf |
| Schulung | Mittel (historische Lücken) | Verbessert |
| Transparenzregister | Gut (nach Korrektur) | Verbessert |
| Verdachtsmeldungsprozess | Mittel | Stabil |
| Dokumentationsqualität | Schwach | Verbesserungsbedarf |

**Gesamtreifegrad:** Mittel (3 von 5) — Verbesserungspotenzial vorhanden, keine systemischen Totalausfälle.

---

## 5. Maßnahmenplan (Übersicht)

| Finding | Maßnahme | Verantwortlich | Frist |
|---|---|---|---|
| F-1 | Vier-Augen-Formular + Systemanpassung | GwB + IT | 30.06.2026 |
| F-2 | Fälligkeitsliste KYC-Erneuerung | GwB | 30.06.2026 |
| F-3 | Neue Monitoring-Regel Drittzahler | IT + GwB | 30.06.2026 |
| F-4 | Pflicht-E-Learning-System | HR + IT | 31.07.2026 |
| F-5 | Verdachtsentscheidungs-Formular | GwB | sofort |
| F-6 | Korrektur Transparenzregister | RA Heller | 22.05.2026 |
| F-7 | Neue Risikoanalyse | GwB | erledigt |
| F-8 | Retrospektive GF-Genehmigung | GwB + GF | 10.06.2026 |

---

*Memo-Nr.: AUDIT-MH-2026-01 — Musterholding GmbH / Interne Revision*
*Verteilung: Streng vertraulich — Geschäftsführung und GwB*
*Aufbewahrungsfrist: 5 Jahre*
