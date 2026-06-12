---
name: datev-lohn-modul-lodas-luh
description: "DATEV LODAS und Lohn und Gehalt LUG. Anwendungsfall Lohnabrechnung in DATEV-Welt Konfiguration ELSTER ELStAM sv.net Schnittstellen. Methodik Unterschiede LODAS vs Lohn und Gehalt Praxis-Tipps. Output Lohnprogramm konfiguriert."
---

# DATEV LODAS und Lohn und Gehalt

## Fachlicher Anker

- **Normen:** § 6a.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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
