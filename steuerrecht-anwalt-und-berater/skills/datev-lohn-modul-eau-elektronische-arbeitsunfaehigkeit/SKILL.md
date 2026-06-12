---
name: datev-lohn-modul-eau-elektronische-arbeitsunfaehigkeit
description: "DATEV LODAS und Lohn und Gehalt LUG. Anwendungsfall Lohnabrechnung in DATEV-Welt Konfiguration ELSTER ELStAM sv.net Schnittstellen. Methodik Unterschiede LODAS vs Lohn und Gehalt Praxis-Tipps. Output Lohnprogramm konfiguriert im Steuerrecht Anwalt Und Berater."
---

# DATEV LODAS und Lohn und Gehalt

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DATEV LODAS und Lohn und Gehalt` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Kernsachverhalt

DATEV bietet zwei Lohnprogramme: LODAS (Lohnbuchhaltungs- und Datenerfassungs-System; haeufiger in Steuerberater-Buros) und Lohn und Gehalt (LUG; vorwiegend bei Mandanten selbst). Beide Programme decken Lohnabrechnung, SV-Meldungen, ELStAM, ELSTER, Jahresmeldungen ab. Der Steuerberater waehlt das passende System für die Mandantenstruktur und konfiguriert die Schnittstellen.

## Kaltstart-Rueckfragen

1. Welche Mandantengroesse — bis 50 AN, über 50 AN?
2. Welche Branche und Sondersituationen (Sonn-/Feiertag, Schichtarbeit)?
3. Welche Schnittstellen erforderlich (Bank, ERP)?
4. Welche Module aktiv (BG, bAV, JobRad)?
5. Welche Mandanten-Sicht (Mandant selbst sieht Lohnabrechnungen)?
6. Welche Zertifikate (ITSG, ELSTER)?
7. Welche Kanzlei-Praeferenz (LODAS oder LUG)?
8. Welche Schulungsbedarf Sachbearbeiter?

## Workflow

### Phase 1 — System-Wahl

| Kriterium | LODAS | Lohn und Gehalt |
|---|---|---|
| Anwendungsumgebung | StB-Kanzlei | Mandant selbst |
| Mandantenzahl | viele Mandanten parallel | Einzelmandant |
| Datenstruktur | Multimandant | Einzelmandant |
| ITSG-Zertifikat | pro Mandant | pro Mandant |
| Module | BG, bAV, JobRad, Werkstudent etc. | gleich |

### Phase 2 — Mandanten-Anlage

- Mandanten-Stammdaten: Branche, BG, KK, Tarifvertrag.
- AN-Stammdaten: SV, ELStAM, Lohnform.
- Konten-Konfiguration im Hauptbuch.

### Phase 3 — Monatslauf

- Datenimport (Variabler Lohn, Krankheit, Sonderzahlungen).
- ELStAM-Abruf.
- Lohnabrechnung erstellen.
- Prüfliste durchgehen.
- ELSTER-Anmeldung.
- SV-Meldungen.
- Buchungssatz an Hauptbuch.

### Phase 4 — Schnittstellen

- ELStAM: Standard.
- ELSTER: Standard.
- DAKOTA (sv.net Alternative): empfohlen.
- BG-Schnittstelle.
- DATEV-Banking: überweisung Loehne und SV.

### Phase 5 — Sondermodule

- BG-Lohnnachweis.
- bAV mit Versicherer-Schnittstelle.
- JobRad mit Leasing-Vertraegen.
- Werkstudent mit Immatrikulations-Prüfung.

### Phase 6 — Updates und Wartung

- Jaehrliche Updates zum 1. Januar (Beitragssaetze, BBG).
- ITSG-Zertifikate erneuern.
- Mandanten-Stammdaten aktualisieren.

## Strategie und Praxis-Tipps

- LODAS ist Standard für StB-Kanzleien — multimandantenfaehig.
- Lohn und Gehalt für Mandanten, die selbst Loehne abrechnen, aber StB-Schnittstelle wuenschen.
- Schulungen DATEV-Akademie jaehrlich empfehlenswert.
- Bei Änderungen am ELStAM-Verfahren: Updates zwingend.

## Quellen und Updates

Stand: 05/2026.

- DATEV LODAS und Lohn und Gehalt Programm- und Bedienungs-Dokumentation (aktuelle Version prüfen).
- DATEV-Programm-Updates jaehrlich (Stand 01.01.) sowie unterjaehrige Reform-Updates (SV-Beitragsbemessungsgrenzen, Mindestlohn).
- Verifikations-Hinweis: konkrete Programmpfade und Menue-Bezeichnungen ggf. abweichend in aktueller DATEV-Version.
