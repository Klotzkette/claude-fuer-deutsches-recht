# E-Mail-Systeme und Audit — Kanzlei Outlook 365

Technischer Befund und Maßnahmenplan nach den Vorfällen vom Februar/März 2026

---

## Ausgangslage

Die Kanzlei Rosenmühle & Partner betreibt Microsoft 365 Business Premium (Outlook 365) als primäre Kommunikationsplattform. Alle 18 Mitarbeiter (7 Rechtsanwälte, 3 Referendare, 8 Verwaltungsmitarbeiter) sind im selben Tenant konfiguriert. Der IT-Betrieb erfolgt durch den externen Dienstleister NetWork-Recht GmbH, Frankfurt.

---

## Identifizierte technische Schwachstellen

### Schwachstelle 1: Keine Nachtzeitsperre für ausgehende externe E-Mails

Das System enthält keine Regel, die ausgehende E-Mails an externe Empfänger in der Zeit zwischen 21:00 und 07:00 Uhr automatisch zurückhält oder zur Überprüfung markiert. RA Dr. Kröll konnte die problematische E-Mail ungehindert um 01:47 Uhr versenden.

**Status nach Audit:** Implementierung einer optionalen „Nacht-Quarantäne-Regel" (Outlook-Transport-Regel) für alle Partner-Accounts geplant. Die Regel würde E-Mails für 12 Stunden in einer Quarantäne-Queue halten und dem Absender eine Rückrufmöglichkeit geben.

### Schwachstelle 2: Kein Data Loss Prevention (DLP)

Microsoft 365 enthält integrierte DLP-Policies, die sensible Daten (z.B. persönliche Adressen, IBAN, Personalausweisnummern) in ausgehenden E-Mails erkennen und den Versand blockieren oder zur Überprüfung markieren können. Diese Funktion war nicht aktiviert.

**Status nach Audit:** DLP-Policy eingerichtet am 15.03.2026. Enthält Erkennungsregeln für Wohnadressen (Straßenmuster), IBAN und Sozialversicherungsnummern.

### Schwachstelle 3: Fehlende Trennung privater und geschäftlicher E-Mail-Konten

RA Dr. Kröll nutzte sein privates Gmail-Konto für die Versendung der kritischen E-Mail. Dieses Konto ist weder im Mandatssystem noch im Outlook-Tenant der Kanzlei integriert.

**Status nach Audit:** Kanzleirichtlinie „Kommunikation ausschließlich über Kanzleisysteme" erlassen (Datum: 22.03.2026). Unterschriften aller Partner eingeholt.

### Schwachstelle 4: Fehlerhafter Verteiler-Anhang

Frau Bischoff hatte Zugriff auf ein geteiltes Verzeichnis mit internen Dokumenten (darunter das fehlerhafte Dokument mit der Adresse RAin Tannenkamps). Das externe Dokument und das interne Dokument hatten ähnliche Namen.

**Status nach Audit:** Umbenennung aller internen Verzeichnisse auf strikte Namenskonvention (Präfix `[INTERN]`). Zugriffsbeschränkung für geteilte Dokumente nach Benutzerrolle.

---

## Outlook-Add-in für das Plugin `email-umformulierer-berufsrecht`

Im Rahmen des Audits wurde die Integration eines Outlook-Add-ins für das Plugin `email-umformulierer-berufsrecht` evaluiert. Das Add-in würde:

1. Jede ausgehende E-Mail an externe Empfänger automatisch analysieren
2. Problematische Formulierungen (Stufen 1–3 gem. Aktenstück 06) markieren
3. Bei Stufe-1-Befunden einen Pflichtdialog auslösen: „Diese E-Mail enthält möglicherweise berufsrechtlich riskante Formulierungen. Möchten Sie die Umformulierungs-Vorschläge sehen?"
4. Bei Nachtversand (21:00–07:00 Uhr) einen zusätzlichen Warnhinweis geben

**Status:** Technisches Konzept erstellt; Beschluss der Partner über Implementierung ausstehend.

---

## Auditbefunde Übersicht

| Nr. | Befund | Risikostufe | Maßnahme | Status |
|---|---|---|---|---|
| 1 | Kein Nachtzeitschutz für E-Mail-Versand | Hoch | Transport-Quarantäne-Regel | In Planung |
| 2 | Kein DLP aktiv | Hoch | DLP-Policy aktiviert | Umgesetzt 15.03.2026 |
| 3 | Private E-Mail im Mandatsbetrieb | Mittel | Kanzleirichtlinie | Umgesetzt 22.03.2026 |
| 4 | Fehlende Verzeichnistrennung | Mittel | Namenskonvention + ACL | Umgesetzt 20.03.2026 |
| 5 | Kein Plugin-Add-in | Mittel | Konzept erstellt | Ausstehend |
| 6 | Fehlende E-Mail-Archivierung Privatkonto | Hoch | Policy-Erweiterung | Ausstehend |

---

## Quellen

- Microsoft 365 Compliance Center — DLP-Dokumentation: [learn.microsoft.com](https://learn.microsoft.com/de-de/microsoft-365/compliance/dlp-learn-about-dlp)
- [Art. 32 DSGVO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)

---

Bearbeitungsstand: 22.04.2026 — RAin Yvonne Tannenkamp / IT-Beauftragter Kanzlei (NetWork-Recht GmbH)
