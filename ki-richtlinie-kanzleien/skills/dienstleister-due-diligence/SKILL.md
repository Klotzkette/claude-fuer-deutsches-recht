---
name: dienstleister-due-diligence
description: "KI-Dienstleister Due Diligence fuer Kanzleien durchfuehren: Anwendungsfall Kanzlei moechte neuen KI-Dienst beauftragen und muss eigenverantwortlich Datenschutz Berufsrecht und Sicherheit prüfen. § 43e BRAO Dienstleisterpruefung, Art. 28 Abs. 1 DSGVO Garantiepflichten, ISO 27001 SOC 2. Pruefraster EU-Sitz vs. US-Sitz, Enterprise-Tier mit Training-Opt-out, Verschluesselung, Zertifizierungen, Subprozessoren, Standardvertragsklauseln. Output Dienstleister-Bewertungsmatrix mit Ampelstatus und AVV-Empfehlung. Abgrenzung zu Auftragsverarbeitungsvertrag-Pruefen und zu Musterklauseln-IT."
---

# Dienstleister Due Diligence

Die sorgfältige Auswahl des KI-Dienstleisters ist eine zentrale berufsrechtliche und datenschutzrechtliche Pflicht. § 43e BRAO verpflichtet zur eigenverantwortlichen Prüfung des Dienstleisters; Art. 28 Abs. 1 DSGVO verlangt hinreichende Garantien für technisch-organisatorische Maßnahmen. Dieser Skill stellt strukturierte Auswahlkriterien bereit.

## Rechtlicher Hintergrund

§ 43e BRAO: Sorgfältige Auswahl und vertragliche Bindung des IT-Dienstleisters als Voraussetzung für die befugte Nutzung. § 43e Abs. 4 BRAO: Drittstaaten-Dienstleister zulässig bei vergleichbarem Schutzniveau. Art. 28 Abs. 1 DSGVO: Nur Auftragsverarbeiter mit hinreichenden Garantien beauftragen. Art. 44 ff. DSGVO: Drittlandtransfer nur mit geeigneten Schutzmaßnahmen (Angemessenheitsbeschluss, SCC, TIA). Art. 5 Abs. 1 lit. f DSGVO: Integrität und Vertraulichkeit durch geeignete technisch-organisatorische Maßnahmen. BRAK-Hinweise 12/2024: Sorgfältige Anbieterauswahl als berufsrechtliche Kernpflicht.

## Vorgehen

1. **Sitzland und Rechtsrahmen prüfen**: EU-Anbieter unterliegen direkt der DSGVO. Für US-amerikanische Anbieter: EU-US Data Privacy Framework-Zertifizierung prüfen; alternativ SCC + TIA.
2. **Enterprise-Tier auf Training-Opt-out prüfen**: Standardmäßige Verbraucherversionen vieler Chatbot-Dienste erlauben dem Anbieter, Eingaben zum Training zu nutzen. Enterprise-Verträge schließen dies in der Regel aus. Opt-out schriftlich bestätigen lassen.
3. **Verschlüsselung verifizieren**: Daten at rest (Speicherung) und in transit (Übertragung) müssen verschlüsselt sein. Mindeststandard: TLS 1.2 für Übertragung; AES-256 für Speicherung.
4. **Zertifizierungen prüfen**: ISO 27001 (Informationssicherheit), SOC 2 Type II (Sicherheit, Verfügbarkeit, Vertraulichkeit), ggf. ISO 27701 (Datenschutz). Aktuelle Zertifikate anfordern.
5. **Subprozessoren und Rechenzentrumsstandorte erfassen**: Wo werden die Daten tatsächlich verarbeitet und gespeichert?
6. **Vertragswerk vervollständigen**: AVV nach Art. 28 DSGVO + § 43e-BRAO-Vereinbarung + ggf. SCC abschließen.
7. **Dokumentierte Risikobeurteilung erstellen**: Eigene Prüfung und Abwägung der Risiken schriftlich festhalten.

## Vorlagentext / Bausteine

**Due-Diligence-Checkliste KI-Dienstleister:**

**Allgemeine Informationen:**
☐ Vollständige Firma und Rechtsform des Anbieters
☐ Sitz des Unternehmens (EU / EWR / Drittland)
☐ Standort der Rechenzentren
☐ Zuständige Datenschutzbehörde

**Datenschutz:**
☐ Datenschutzerklärung und Datenschutzrichtlinien liegen vor
☐ AVV nach Art. 28 DSGVO ist verfügbar / wird abgeschlossen
☐ Bei US-Anbietern: EU-US Data Privacy Framework-Zertifizierung oder SCC
☐ Expliziter Training-Opt-out für Kunden-Eingaben ist schriftlich vereinbart
☐ Lösch- und Aufbewahrungsfristen sind dokumentiert

**Technische Sicherheit:**
☐ Verschlüsselung at rest (mindestens AES-256)
☐ Verschlüsselung in transit (mindestens TLS 1.2)
☐ Multi-Faktor-Authentifizierung für Kanzlei-Accounts
☐ Incident-Response-Verfahren dokumentiert

**Zertifizierungen:**
☐ ISO 27001 (aktuelles Zertifikat)
☐ SOC 2 Type II (aktueller Bericht)
☐ Ggf. C5 (BSI Cloud Computing Compliance Criteria Catalogue)

**Berufsrecht:**
☐ § 43e-BRAO-Vereinbarung abgeschlossen
☐ Strafrechtliche Belehrung nach § 203 StGB erteilt

## Hinweise zur Aktualisierung

Die Zertifizierungen und die EU-US-Datenschutzrahmen sind regelmäßig auf Aktualität zu prüfen. Datenschutzbehörden-Entscheidungen zu einzelnen KI-Anbietern (z.B. Untersagungen durch DPAs) sind zu beobachten. Jährliche Neubeurteilung des eingesetzten Dienstleisters empfohlen.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 87: Due Diligence bei US-Anbietern erfordert Transfer Impact Assessment; EU-Sitz-Anforderung nicht absolut.
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 55: Sorgfaltspflicht bei KI-Dienstleister-Auswahl — Verantwortlicher bleibt fuer Entscheidungslogik haftbar.
- BGH, Urt. v. 17.05.2018 — VII ZR 157/17, NJW 2018, 2412 Rn. 18: AGB-Kontrolle von Haftungsausschluessen bei komplexen IT-Systemen; Dienstleister-Due-Diligence muss Haftungsklauseln pruefen.
- OLG Muenchen, Urt. v. 09.11.2021 — 33 U 2023/21, NJW-RR 2022, 85 Rn. 18: Sorgfaltspflichtverletzung bei fehlender Pruefung des Drittlandtransfers durch Cloud-Anbieter.

## Zentrale Normen (Paragrafenkette)
- Art. 28 Abs. 1 DSGVO — hinreichende Garantien des Auftragsverarbeiters
- Art. 46 DSGVO — Drittlandtransfer-Sicherheitsnetz (SCC, Angemessenheitsbeschluss)
- § 43e BRAO — IT-Dienstleister in Kanzleien
- Art. 9 KI-VO — Risikomanagementsystem Anbieter-Anforderungen

## Triage zu Beginn
1. Wo hat der KI-Dienstleister seinen Sitz — EU, USA oder sonstiges Drittland?
2. Gibt es einen Enterprise-Tier mit Training-Opt-out — oder ist Training auf Eingaben Standard?
3. Welche Zertifizierungen weist der Anbieter vor (ISO 27001, SOC 2, BSI C5)?
4. Sind Standardvertragsklauseln und eine Transferfolgenabschaetzung vorhanden?
5. Ist der Anbieter CLOUD Act-Risiken ausgesetzt (US-Muttergesellschaft)?

## Output-Template — Dienstleister-Due-Diligence-Bericht
**Adressat:** Kanzlei-Management / DSB — Tonfall: strukturiert, risikoorientiert
```
DIENSTLEISTER-DUE-DILIGENCE
[DATUM] — Anbieter: [NAME] — Zweck: [BESCHREIBUNG]

SITZ: [LAND]
EU-Datenzentrum: [JA / NEIN — Standort: BESCHREIBUNG]
Training auf Eingaben: [NEIN (Enterprise-Tier) / JA — UNZULAESSIG fuer Mandatsdaten]
CLOUD Act-Risiko: [NIEDRIG / HOCH — Begruendung]

Zertifizierungen:
☑/☐ ISO 27001
☑/☐ SOC 2 Typ II
☑/☐ BSI C5

Datentransfer-Absicherung:
☑/☐ Angemessenheitsbeschluss (EU-US Data Privacy Framework)
☑/☐ Standardvertragsklauseln
☑/☐ Transferfolgenabschaetzung (TIA) durchgefuehrt

Gesamtbewertung: [FREIGEGEBEN / BEDINGT / ABGELEHNT]
Auflagen: [BESCHREIBUNG]
Geprueft von: [NAME], [DATUM]
```
