# Konformitätsprüfung RecruitAI — Auditbericht (Zwischenbericht)

**Aktenzeichen:** TI-KI-2026-012
**Prüfender:** WPG Hagedorn & Partner, Frankfurt am Main (Prüfungsleitung: Dr. Miriam Hagedorn)
**Auftraggeber:** Thalheim Industries SE, CCO Annegret Kühnhausen
**Prüfungszeitraum:** 15. Januar 2026 – laufend (Abschlussbericht geplant: 31. Juli 2026)
**Berichtsdatum:** 28. Februar 2026
**Berichtstyp:** Zwischenbericht

---

## 1. Auftrag und Prüfungsumfang

Hagedorn & Partner wurde durch Thalheim Industries SE mandatiert, die Konformitätsbewertung für das Hochrisiko-KI-System **RecruitAI** (Vendor: Synaptec Analytics GmbH) nach Art. 43 Abs. 2 KI-VO zu begleiten. RecruitAI fällt unter Anhang III Nr. 4 lit. a KI-VO (Personalauswahl/-priorisierung) und ist damit als Hochrisiko-System eingestuft.

**Prüfungsgrundlage:**
- Art. 9–17 KI-VO (Hochrisiko-Pflichten)
- Art. 43 KI-VO (Konformitätsbewertungsverfahren)
- ISO/IEC 42001 (KI-Managementsystem, informativ)
- NIST AI RMF (informativ)
- Interne Vorgaben Thalheim Industries SE (KI-Governance-Leitlinie v2.1)

**Prüfungsumfang:**
1. Risikomanagementsystem (Art. 9)
2. Daten-Governance (Art. 10)
3. Technische Dokumentation (Art. 11)
4. Protokollierung (Art. 12)
5. Transparenz / Gebrauchsanweisung (Art. 13)
6. Menschliche Aufsicht (Art. 14)
7. Genauigkeit, Robustheit, Cybersicherheit (Art. 15)
8. Qualitätsmanagementsystem (Art. 17)

---

## 2. Prüfungsergebnisse im Überblick

| Prüfbereich | Rechtsgrundlage | Ergebnis | Kritikalität |
|---|---|---|---|
| Risikomanagementsystem | Art. 9 KI-VO | Vorhanden; Aktualisierung erforderlich | Mittel |
| Daten-Governance | Art. 10 KI-VO | Teilweise dokumentiert | Mittel |
| **Bias-Tests** | **Art. 9 Abs. 7 KI-VO** | **Fehlen vollständig** | **Kritisch** |
| Technische Dokumentation | Art. 11 KI-VO | Teilweise (Vendor); Nachforderung läuft | Hoch |
| Protokollierung | Art. 12 KI-VO | Implementiert; Protokolltiefe prüfen | Niedrig |
| Gebrauchsanweisung | Art. 13 KI-VO | Vorhanden (DE); ausreichend | Niedrig |
| Menschliche Aufsicht | Art. 14 KI-VO | Konzept vorhanden; SOP fehlt | Mittel |
| Override-Mechanismus | Art. 14 Abs. 4 KI-VO | Technisch möglich; SOP fehlt | Mittel |
| Automatische Ablehnung | Art. 14 / Art. 22 DSGVO | Ohne HR-Aktiv-Bestätigung möglich | **Kritisch** |
| Genauigkeit / Robustheit | Art. 15 KI-VO | Herstellerangaben; unabhängige Prüfung fehlt | Hoch |
| Cybersicherheit | Art. 15 KI-VO | Pentest Synaptec-Server ausstehend | Hoch |
| QMS | Art. 17 KI-VO | ISO 9001 Thalheim; Synaptec ISO 27001 | Ausreichend |

---

## 3. Kritische Feststellungen (Detail)

### Feststellung F-001 — Fehlende Bias-Tests (KRITISCH)

**Sachverhalt:** Die Hagedorn-Prüfung hat ergeben, dass Synaptec Analytics GmbH für das RecruitAI-Modell keine dokumentierten Tests zur Erkennung und Minimierung verzerrter Ausgaben (Bias) nach Art. 9 Abs. 7 KI-VO vorgelegt hat. Synaptec hat auf Anfrage lediglich ein Whitepaper aus dem Jahr 2022 vorgelegt, das allgemeine Fairness-Prinzipien beschreibt, aber keine aktuellen, modellspezifischen Testergebnisse enthält.

**Rechtliche Bewertung:** Art. 9 Abs. 7 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, diese auf Bias (Verzerrungen) zu testen, die zu einem in Art. 5 Abs. 1 lit. b GrCh verbotenen Ergebnis führen könnten, namentlich diskriminierende Ergebnisse bei Entscheidungen in Bereichen wie Beschäftigung. Ohne nachweisliche Bias-Tests kann die Konformitätsbewertung nicht mit positivem Ergebnis abgeschlossen werden.

**Risikobewertung:** KRITISCH. Ohne positive Bias-Test-Ergebnisse:
- Kann die Konformitätserklärung nicht ausgestellt werden (Art. 48 KI-VO).
- Darf das System nach dem 02.08.2026 nicht weiterbetrieben werden.
- Besteht ein erhebliches Diskriminierungsrisiko gegenüber Bewerbern.

**Empfehlung:** Parallel zu Synaptec sind unabhängige Bias-Tests durch einen spezialisierten Dienstleister zu beauftragen. Dringlichkeit: SOFORT.

---

### Feststellung F-002 — Automatische Ablehnung ohne HR-Bestätigung (KRITISCH)

**Sachverhalt:** Technische Analyse der Systemlogs zeigt, dass zwischen September 2024 und Februar 2026 in 143 Fällen Bewerberinnen und Bewerber automatisch abgelehnt wurden (Score unter 40), ohne dass eine HR-Mitarbeiterin oder ein HR-Mitarbeiter aktiv eine Ablehnung bestätigt hat. Stattdessen wurde eine automatisierte Ablehnungs-E-Mail durch das System versendet.

**Rechtliche Bewertung:** Dies stellt einen Verstoß gegen Art. 14 KI-VO (menschliche Aufsicht) und möglicherweise gegen Art. 22 DSGVO (https://dejure.org/gesetze/DSGVO/22.html) dar. Art. 22 DSGVO gibt betroffenen Personen das Recht, nicht einer ausschließlich automatisierten Entscheidung unterworfen zu werden, die rechtliche oder ähnlich erhebliche Wirkung entfaltet. Eine Ablehnung einer Bewerbung hat ähnlich erhebliche Wirkung.

**Risikobewertung:** KRITISCH. Mögliche Haftung gegenüber betroffenen Bewerbern. Meldepflicht nach Art. 35 DSGVO (DPIA) für dieses Verarbeitungsmerkmal. Empfehlung zur Überprüfung der 143 Fälle durch DSB.

**Empfehlung:** Sofortige technische Sperre der automatischen Ablehnung; aktiver HR-Override als Pflichtschritt.

---

### Feststellung F-003 — Unvollständige technische Dokumentation (HOCH)

Synaptec hat die technische Dokumentation nach Art. 11 i.V.m. Anhang IV KI-VO nur teilweise vorgelegt. Fehlende Abschnitte: Modellarchitektur, Trainingsverfahren, verwendete Datensätze (Herkunft, Umfang, Preprocessing). Nachforderung ist gestellt; Frist 30.04.2026.

---

## 4. Positiv bewertete Aspekte

- Protokollierung (Art. 12): Aktiviert und ausreichend tief für Nachvollziehbarkeit.
- Gebrauchsanweisung (Art. 13): In verständlichem Deutsch vorhanden.
- AVV mit Synaptec: Vorhanden und DSGVO-konform.
- IT-Sicherheit Thalheim-Seite: ISO 27001 zertifiziert (gültig bis 06/2027).

---

## 5. Weiteres Vorgehen

| Maßnahme | Verantwortlich | Frist |
|---|---|---|
| Unabhängige Bias-Tests beauftragen (F-001) | CCO / CDO | 31.03.2026 ✓ (Beschluss KI-Komitee) |
| Technische Sperre automatische Ablehnung (F-002) | IT / Synaptec | 30.04.2026 |
| Überprüfung 143 Betroffene (F-002) | DSB Dr. Eichenmüller | 31.05.2026 |
| Nachforderung Technikdokumentation (F-003) | CIO / Synaptec | 30.04.2026 |
| SOP menschliche Aufsicht erstellen | HR | 30.04.2026 |
| Pentest Synaptec-Server | IT-Security | 31.05.2026 |
| Abschluss Konformitätsprüfung | Hagedorn & Partner | 31.07.2026 |

---

*Zwischenbericht, Aktenzeichen TI-KI-2026-012. WPG Hagedorn & Partner, Frankfurt. Prüfungsleitung Dr. M. Hagedorn. 28.02.2026.*
