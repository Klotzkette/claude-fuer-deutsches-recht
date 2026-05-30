# 06 DSGVO — Art. 28 DSGVO, AVV und JuristAssist Pro Cloud

**Akte:** Berufsrecht / KI-Vertragsprüfung — Kanzlei Rotbruch, Köln
**Stichtag Aktenstück:** 15. April 2026

---

## 1. Ausgangslage: Mandantendaten in der Cloud-KI

Am 21. März 2022 lud Dr. Rotbruch den 14-seitigen Ehevertragsentwurf als PDF in die Cloud-Plattform von JuristAssist Pro 5 hoch. Das Dokument enthielt folgende personenbezogene Daten i.S.d. Art. 4 Nr. 1 DSGVO:

- Vor- und Nachname beider Vertragsparteien (Ulrike und Hans-Dieter Habernau)
- Geburtsdaten und Geburtsort
- Wohnadressen
- Vermögensangaben (Immobilienwert, Kontoguthaben, Rentenpunkte)
- Angaben zum Arbeitgeber und Einkommen

Beim Hochladen dieser Daten in das Cloud-System der LegalTech GmbH (Hamburg) handelt es sich um eine Übermittlung personenbezogener Daten an einen Auftragsverarbeiter i.S.d. Art. 28 DSGVO. Ohne einen wirksamen Auftragsverarbeitungsvertrag (AVV) ist diese Übermittlung datenschutzrechtlich unzulässig.

---

## 2. Anforderungen des Art. 28 DSGVO

Art. 28 DSGVO schreibt vor, dass ein Verantwortlicher (hier: Kanzlei Rotbruch als datenschutzrechtlich Verantwortlicher) personenbezogene Daten nur an Auftragsverarbeiter übermitteln darf, mit denen ein schriftlicher Vertrag nach Art. 28 Abs. 3 DSGVO geschlossen wurde. Dieser Vertrag muss mindestens folgende Inhalte haben:

- Weisungsgebundenheit des Auftragsverarbeiters
- Verpflichtung zur Vertraulichkeit
- Technische und organisatorische Maßnahmen (TOM) nach Art. 32 DSGVO
- Regelung zu Unterauftragsverarbeitern (Art. 28 Abs. 4 DSGVO)
- Unterstützung bei Betroffenenrechten (Art. 12–22 DSGVO)
- Regelung zur Datenlöschung nach Auftragsende
- Recht auf Kontrolle durch den Verantwortlichen

---

## 3. Situation bei der LegalTech GmbH (JuristAssist Pro 5)

Zum Zeitpunkt der Nutzung im März 2022 hatte die LegalTech GmbH keinen standardisierten AVV im Angebotsprozess integriert. Stattdessen enthielten die AGB der LegalTech GmbH (Version 3.2, gültig ab 1. Januar 2022) unter Ziffer 9.4 folgenden Passus:

> „LegalTech GmbH verarbeitet Nutzerdaten ausschließlich zur Erbringung der vertraglich vereinbarten Dienste. Eine Weitergabe an Dritte oder Nutzung für Trainingszwecke erfolgt nicht ohne ausdrückliche Zustimmung."

Diese AGB-Klausel ist kein wirksamer AVV i.S.d. Art. 28 DSGVO, da:

- sie nicht die vollständige, von Art. 28 Abs. 3 DSGVO geforderte Regelungstiefe aufweist,
- sie die konkret eingesetzten Unterauftragsverarbeiter nicht benennt (AWS EU-Central-1 war nicht gesondert aufgeführt),
- sie keine Verpflichtung zu TOMs nach Art. 32 DSGVO enthält,
- sie kein Audit-Recht des Verantwortlichen vorsieht.

Die LegalTech GmbH hat auf Anfrage von RAin Dr. Wiesmann (Schreiben vom 15. März 2026) bestätigt, dass erst ab Oktober 2022 ein Standard-AVV für Kanzleikunden angeboten wurde. Zudem ist die E-Mail vom 24. März 2026 der LegalTech GmbH an die Kanzlei Rotbruch zu AVV-Fragen in der Anlage enthalten (`emails/2026-03-24_juristassist_an_kanzlei_avv.eml`).

---

## 4. Datenschutzrechtliche Rechtsfolgen

### 4.1 Verstoß gegen Art. 28 DSGVO

Die Übermittlung ohne AVV ist ein Verstoß gegen Art. 28 Abs. 1 DSGVO (Pflicht zur Vereinbarung) i.V.m. Art. 5 Abs. 1 lit. f DSGVO (Integrität und Vertraulichkeit). Dieser Verstoß kann durch den LDI NRW (Beschwerde bereits eingeleitet, Az. LDI-NRW-2026-0392) mit einem Bußgeld belegt werden.

Der Bußgeldrahmen nach Art. 83 Abs. 4 DSGVO beträgt bis zu 10 Mio. EUR oder 2 Prozent des weltweit erzielten Jahresumsatzes. Bei einer Einzelkanzlei mit einem Jahresumsatz von ca. 220.000 EUR (geschätzt nach Aktenlage) ist der Prozent-Wert nicht einschlägig; ein spürbares Bußgeld zwischen 5.000 EUR und 30.000 EUR erscheint nach vergleichbaren Entscheidungen (LDI NRW, Entscheidung v. 15. Oktober 2021, Az. LDI-NRW-2021-0714) realistisch.

### 4.2 Verstoß gegen § 43a Abs. 2 BRAO

§ 43a Abs. 2 BRAO verpflichtet den Anwalt zur Verschwiegenheit über alle ihm anvertrauten Informationen. Die Übermittlung von Mandantendaten an einen Cloud-KI-Anbieter ohne hinreichende Absicherung ist eine Verletzung dieser Verschwiegenheitspflicht. Der Anwalt ist verpflichtet, sicherzustellen, dass auch Dritte, denen er Daten anvertraut, zur Vertraulichkeit verpflichtet sind — was einen wirksamen AVV voraussetzt.

### 4.3 Mögliche Strafbarkeit nach § 203 StGB

Die Übergabe von Mandantendaten an einen nicht zur Verschwiegenheit verpflichteten Dritten kann tatbestandlich unter § 203 Abs. 1 Nr. 3 StGB (Verletzung von Privatgeheimnissen durch Rechtsanwälte) fallen. Die Strafbarkeit entfällt, wenn der Auftragsverarbeiter wirksam zur Verschwiegenheit verpflichtet wurde. Ohne AVV fehlt eine solche wirksame Verpflichtung. Im Ergebnis besteht ein Anfangsverdacht, der strafrechtlich bisher nicht verfolgt wird, jedoch eine erhebliche Relevanz im Berufsrechtsverfahren hat (dazu Aktenstück 07).

---

## 5. Verbesserungsmaßnahmen

| Maßnahme | Beschreibung | Priorität |
|---|---|---|
| AVV abschließen | Sofortige Vereinbarung mit LegalTech GmbH (Muster erhältlich) | Hoch |
| Datenschutz-Folgenabschätzung | DSFA nach Art. 35 DSGVO für Cloud-KI-Einsatz | Hoch |
| Datenlöschung prüfen | Anforderung Nachweis Löschung Habernau-Daten bei LegalTech GmbH | Mittel |
| Information Betroffener | Art. 34 DSGVO — Benachrichtigung Frau und Herr Habernau | Mittel |
| Kanzlei-Datenschutzkonzept | Internes Datenschutzkonzept für KI-Einsatz | Mittel |
| DSB benennen | Prüfung Benennungspflicht gem. Art. 37 DSGVO (Schwellenwert) | Niedrig |

---

## 6. Abschluss-AVV (aktueller Stand)

Die LegalTech GmbH hat mit Datum 20. März 2026 retroaktiv einen AVV angeboten. Dieser deckt jedoch nicht die Verarbeitung aus dem Jahr 2022 ab, da ein AVV datenschutzrechtlich prospektiv wirkt. Die nachträgliche Unterzeichnung ist für zukünftige Nutzungen sinnvoll, heilt den Verstoß von 2022 nicht.

---

**Quellen:**
- [Art. 28 DSGVO (EUR-Lex)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)
- [Art. 83 DSGVO (EUR-Lex)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)
- [§ 43a Abs. 2 BRAO (dejure.org)](https://dejure.org/gesetze/BRAO/43a.html)
- [§ 203 StGB (dejure.org)](https://dejure.org/gesetze/StGB/203.html)
- [Art. 35 DSGVO (EUR-Lex)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)
