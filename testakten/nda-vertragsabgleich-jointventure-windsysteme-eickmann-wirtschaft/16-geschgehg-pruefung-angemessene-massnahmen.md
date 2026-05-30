# 16 — GeschGehG-Prüfung: Angemessene Geheimhaltungsmaßnahmen

**AZ:** MR-2026-1118
**Thema:** GeschGehG §§ 2–3 Compliance-Prüfung für Windsysteme Norderhof AG
**Stand:** Februar 2026
**Rechtsgrundlagen:** GeschGehG §§ 2, 3, 4; RL (EU) 2016/943; BGH-Rspr. zu UWG § 17 a.F.

---

## 1. Rechtlicher Rahmen

Das Gesetz zum Schutz von Geschäftsgeheimnissen (GeschGehG, in Kraft seit 26.04.2019) setzt die EU-Richtlinie 2016/943 um. Zentrale Voraussetzung für den Geheimnisschutz nach § 2 Nr. 1 GeschGehG:

> Eine Information ist ein Geschäftsgeheimnis, wenn sie:
> (a) geheim ist (nicht allgemein bekannt oder zugänglich),
> (b) kommerziellen Wert hat, weil sie geheim ist, und
> (c) Gegenstand von den Umständen nach angemessenen Geheimhaltungsmaßnahmen durch ihren rechtmäßigen Inhaber ist.

**Merkmal (c) — „angemessene Geheimhaltungsmaßnahmen"** ist das entscheidende operative Kriterium: Wer keine angemessenen Maßnahmen trifft, verliert den GeschGehG-Schutz, auch wenn die Information faktisch geheim bleibt.

---

## 2. Audit-Ergebnis Windsysteme (Januar/Februar 2026)

RA Dr. Roosendaal hat zusammen mit der IT-Abteilung und dem CISO von Windsysteme (Ralf Derstappen) eine Prüfung der bestehenden Geheimhaltungsmaßnahmen durchgeführt.

### 2.1 Technische Maßnahmen

| Maßnahme | Status | Bewertung |
|---|---|---|
| Zugangskontrolle Produktionsanlagen | Vorhanden (Chipkarte + PIN) | Angemessen |
| CAD-Datenverschlüsselung (AES-256) | Vorhanden | Angemessen |
| Need-to-know-Zugriffssteuerung (IT) | Teilweise vorhanden (nur F&E) | Verbesserungsbedarf |
| DLP (Data Loss Prevention) für E-Mail | Nicht vorhanden | Kritisch |
| Verschlüsselung Dateiserver | Vorhanden (BitLocker) | Angemessen |
| VPN-Pflicht für Remote-Zugriff | Vorhanden | Angemessen |
| Penetrationstest (zuletzt) | November 2024 | Regelmäßig erneuern (Q2 2026) |

### 2.2 Organisatorische Maßnahmen

| Maßnahme | Status | Bewertung |
|---|---|---|
| Geheimhaltungsvereinbarungen mit Mitarbeitern | Vorhanden für F&E (80 %); fehlt für Produktion (55 %) | Nachholbedarf |
| Geheimhaltungsrichtlinie (intern) | Vorhanden (2021, veraltet) | Aktualisierung erforderlich |
| Schulungen Geheimhaltung | Letzte Schulung 2023 | Erneuern Q1 2026 |
| Klassifizierungssystem für Dokumente | Teilweise (nur VERTRAULICH/ÖFFENTLICH, kein STRENG VERTRAULICH) | Dreistufiges System einführen |
| Visitor-Management inkl. NDA-Pflicht | Vorhanden | Angemessen |

---

## 3. GeschGehG-Konformitätslücken

| Lücke | Priorität | Maßnahme |
|---|---|---|
| Fehlende DLP-Lösung | HOCH | Einführung bis Q2 2026 (z.B. Microsoft Purview) |
| Mitarbeiter-NDA fehlt für 45 % der Produktion | HOCH | Nachrüstung bis Ende März 2026 |
| Veraltetem Geheimhaltungsrichtlinie (2021) | MITTEL | Aktualisierung bis Ende Februar 2026 |
| Fehlendes dreistufiges Klassifizierungssystem | MITTEL | Einführung VERTRAULICH / STRENG VERTRAULICH / ÖFFENTLICH |
| Schulungen veraltet (2023) | MITTEL | Pflichtschulung Q1 2026 |
| Kein regelmäßiger Pentest (Fälligkeit Q2 2026) | NIEDRIG | Terminierung Pentest-Vergabe |

---

## 4. Empfehlungen RA Dr. Roosendaal

Die im NDA vereinbarten Geheimhaltungsmaßnahmen (Need-to-know, Verschlüsselung, Zugangskontrolle) korrespondieren mit den bestehenden technischen Maßnahmen von Windsysteme — soweit diese vorhanden sind. Damit der GeschGehG-Schutz auch im Schadensfall standhalten kann (z.B. bei Klage gegen Eickmann wegen Geheimnisverrat), muss Windsysteme nachweisen können, dass „angemessene Maßnahmen" tatsächlich bestanden.

**Empfohlenes Maßnahmenpaket:**

1. Sofortige Einführung DLP für E-Mail und Dateiserver (Q2 2026).
2. Vollständige Nachrüstung Mitarbeiter-NDAs bis Ende März 2026.
3. Aktualisierung der internen Geheimhaltungsrichtlinie bis Ende Februar 2026.
4. Einführung dreistufiges Dokumentenklassifizierungssystem.
5. Pflichtschulung Geheimhaltung für alle Mitarbeiter mit NDA-Zugang, Q1 2026.

---

## 5. NDA-Konsequenz

Die GeschGehG-Konformitätsanalyse floss in die NDA-Verhandlungen ein: § 16 NDA v7 verpflichtet beide Parteien, während der NDA-Laufzeit einen Mindeststandard an Geheimhaltungsmaßnahmen (definiert in Annex C) einzuhalten. Windsysteme nutzt diesen Annex als internen Compliance-Fahrplan.
