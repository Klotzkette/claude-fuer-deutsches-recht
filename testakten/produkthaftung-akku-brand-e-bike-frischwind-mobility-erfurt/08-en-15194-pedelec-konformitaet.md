# 08 — EN 15194:2017 Pedelec-Konformität — Prüfbericht und Abweichungen

**Dokument-Typ:** Normprüfungs-Analyse
**AZ Kanzlei:** MR-2026-0822
**Norm:** EN 15194:2017 — Cycles — Electrically power assisted cycles (EPAC Bicycles)

---

## 1. Normstruktur EN 15194:2017

Die EN 15194:2017 ist die maßgebliche harmonisierte europäische Norm für Pedelecs (EPAC) und regelt technische Anforderungen an elektrische Antriebssysteme, Batteriesysteme, Sicherheitsfunktionen und Konformitätsnachweise. Die wichtigsten Abschnitte im Kontext des Wind-X7:

| Abschnitt | Inhalt | Relevanz Wind-X7 |
|---|---|---|
| Abschn. 4 | Allgemeine Anforderungen | Grundlegend |
| Abschn. 4.3.4 | Anforderungen Batterie-System | Kritisch — BMS-Bug |
| Abschn. 4.3.4.3 | Schutz gegen Überladung | Direkt verletzt |
| Abschn. 4.3.4.4 | Thermische Schutzfunktionen | Direkt verletzt |
| Abschn. 4.3.5 | Elektrisches Antriebssystem | Relevant |
| Abschn. 5 | Prüfmethoden | Basis Baumusterprüfung |
| Abschn. 5.4 | Batterie-Sicherheitsprüfungen | Basis Baumusterprüfung |
| Anhang B | Übereinstimmungserklärung | Formale Anforderungen |

---

## 2. Prüfbericht TÜV Rheinland (Auszug)

**Prüfbericht-Nr.:** TR-2022-LF-4412-PT
**Geprüftes Produkt:** Wind-X7 Prototyp (LiFePO4-Zellen)
**Prüfdatum:** 02.–04. Februar 2023

Relevante Prüfergebnisse (Prototyp — bestanden):
- Abschn. 4.3.4.3 (Überladeschutz): **BESTANDEN** — Schutz bei 4,22 V/Zelle ausgelöst
- Abschn. 4.3.4.4 (Thermischer Schutz): **BESTANDEN** — Abschaltung bei 68 °C Zelltemperatur
- Abschn. 4.3.5 (Antrieb): **BESTANDEN**

**Kritische Diskrepanz Serienprodukt:**

Mit NMC-Zellen (Serienproduktion) gelten andere thermische Grenzwerte:
- Thermisches Durchgehen NMC: ab ca. 150 °C Zelltemperatur (vs. LiFePO4: > 270 °C)
- Bei BMS-Bug V3.9.1: Überladeschutz nicht ausgelöst → Zellen auf 4,35 V überladen
- Konsequenz: Abschn. 4.3.4.3 und 4.3.4.4 sind im Serienbetrieb **NICHT EINGEHALTEN**

---

## 3. Bewertung der Normabweichungen

Die im Serienprodukt festgestellten Abweichungen von EN 15194:2017 sind:

**Abweichung 1 — Überladeschutz (§ 4.3.4.3):**
Überladeschutz wird bei Umgebungstemperatur > 38 °C und Schnellladung nicht aktiviert. Gemessene maximale Zellspannung: 4,35 V (Soll: max. 4,20 V). Schweregrad: **kritisch**.

**Abweichung 2 — Thermischer Schutz (§ 4.3.4.4):**
Thermischer Interrupt-Handler triggert nicht korrekt. Bei Zelltemperaturen > 55 °C keine zuverlässige Abschaltung. Schweregrad: **kritisch**.

**Abweichung 3 — Zellchemie (§ 4.3.4):**
Verwendete Zellchemie (NMC) weicht von der im Prüfprotokoll dokumentierten Zellchemie (LiFePO4) ab, ohne erneute Konformitätsbewertung. Schweregrad: **erheblich**.

---

## 4. Konsequenzen

- Die CE-Kennzeichnung des Serienprodukts ist auf Basis dieser Abweichungen nicht aufrechtzuerhalten.
- Frischwind muss die benannte Stelle (TÜV Rheinland, NB 0035) unverzüglich informieren.
- Eine neue Baumusterprüfung ist nach Behebung des BMS-Bugs und Klärung der Zellenspezifikation durchzuführen.
- Bis zur erfolgreichen erneuten Zertifizierung darf das Produkt nicht in Verkehr gebracht werden.
