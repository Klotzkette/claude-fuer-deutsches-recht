---
name: steuer-datev-lohn-modul-eau-elektronische-arbeitsunfaehigkeit
description: "Steuer Datev Lohn Modul EAU Elektronische Arbeitsunfaehigkeit: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer Datev Lohn Modul EAU Elektronische Arbeitsunfaehigkeit

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer Datev Lohn Modul EAU Elektronische Arbeitsunfaehigkeit** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-datev-lohn-modul-lodas-luh` | DATEV LODAS und Lohn und Gehalt LUG. Anwendungsfall Lohnabrechnung in DATEV-Welt Konfiguration ELSTER ELStAM sv.net Schnittstellen. Methodik Unterschiede LODAS vs Lohn und Gehalt Praxis-Tipps. Output Lohnprogramm konfiguriert. |
| `stb-eau-elektronische-arbeitsunfaehigkeit-2023` | eAU elektronische Arbeitsunfähigkeitsbescheinigung seit 2023. Anwendungsfall AN-Krankmeldung AG-Abruf bei Krankenkasse Entgeltfortzahlung. Methodik Schnittstelle Konfiguration Workflow. Output eAU-Konfiguration. |
| `stb-erechnung-pflicht-b2b-2025-2026` | eRechnung-Pflicht B2B seit 01.01.2025 § 14 UStG ViDA. Anwendungsfall Prüfung Mandantenbetrieb eRechnungs-Empfang Versand Übergangsfristen PDF reicht nicht mehr. Methodik Format XRechnung ZUGFeRD. Output eRechnungs-Konfiguration. |
| `stb-jahresabschluss-anlagenverzeichnis-afa` | Anlagenverzeichnis und AfA-Buchung Jahresabschluss. Anwendungsfall vollständige Aktualisierung Anlagen Zugaenge Abgaenge AfA-Methoden Sonderabschreibung 7g 7b 6b EStG. Methodik AfA-Tabellen. Output Anlagenspiegel. |
| `stb-jahresabschluss-bestandskonten-abstimmung` | Bestandskonten-Abstimmung zum Jahresabschluss. Anwendungsfall Endbestaende Bank Kasse Forderungen Verbindlichkeiten Anlagen Eigenkapital abstimmen Inventur-Werte einarbeiten. Methodik Saldenabstimmung Vergleich. Output abgestimmte Bestandskonten. |
| `stb-jahresabschluss-kassenfuehrung-gobd-pflichten` | Kassenführung GoBD-Pflichten. Anwendungsfall Mandanten mit Bargeschäft Kasse Aufzeichnungspflichten Kassenbuch elektronische Aufzeichnungssysteme TSE technische Sicherheitseinrichtung. Methodik Prüfung Sorgfalt. Output GoBD-konforme Kassenführung. |
| `stb-jahresabschluss-veroeffentlichung-bundesanzeiger` | Jahresabschluss-Veröffentlichung Bundesanzeiger § 325 HGB. Anwendungsfall Pflichtveröffentlichung Kapitalgesellschaft Frist 12 Monate Groessenklassen Erleichterungen. Methodik elektronische Übermittlung. Output Bundesanzeiger-Eintrag. |
| `stb-jahresabschluss-vorbereitung-stichtag` | Jahresabschluss-Vorbereitung Stichtag. Anwendungsfall systematische JA-Vorbereitung Inventur Periodenabgrenzung Rückstellungen Anlagenspiegel. Methodik 8-Wochen-Vorlauf. Output JA-Vorbereitungs-Routine. |
| `stb-jahresabschluss-warenbestand-inventur` | Warenbestand und Inventur für Jahresabschluss. Anwendungsfall jaehrliche Inventur Aufnahme Warenbestand permanente Inventur Stichprobeninventur Bewertung. Methodik § 240 HGB GoBD. Output Inventur-Protokoll Warenbestand-Wert. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer Datev Lohn Modul EAU Elektronische Arbeitsunfaehigkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-datev-lohn-modul-lodas-luh`

**Fokus:** DATEV LODAS und Lohn und Gehalt LUG. Anwendungsfall Lohnabrechnung in DATEV-Welt Konfiguration ELSTER ELStAM sv.net Schnittstellen. Methodik Unterschiede LODAS vs Lohn und Gehalt Praxis-Tipps. Output Lohnprogramm konfiguriert.

# DATEV LODAS und Lohn und Gehalt

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DATEV LODAS und Lohn und Gehalt` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

DATEV bietet zwei Lohnprogramme: LODAS (Lohnbuchhaltungs- und Datenerfassungs-System; haeufiger in Steuerberater-Buros) und Lohn und Gehalt (LUG; vorwiegend bei Mandanten selbst). Beide Programme decken Lohnabrechnung, SV-Meldungen, ELStAM, ELSTER, Jahresmeldungen ab. Der Steuerberater waehlt das passende System fuer die Mandantenstruktur und konfiguriert die Schnittstellen.

## Kaltstart-Rueckfragen

1. Welche Mandantengroesse — bis 50 AN, ueber 50 AN?
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
- Pruefliste durchgehen.
- ELSTER-Anmeldung.
- SV-Meldungen.
- Buchungssatz an Hauptbuch.

### Phase 4 — Schnittstellen

- ELStAM: Standard.
- ELSTER: Standard.
- DAKOTA (sv.net Alternative): empfohlen.
- BG-Schnittstelle.
- DATEV-Banking: ueberweisung Loehne und SV.

### Phase 5 — Sondermodule

- BG-Lohnnachweis.
- bAV mit Versicherer-Schnittstelle.
- JobRad mit Leasing-Vertraegen.
- Werkstudent mit Immatrikulations-Pruefung.

### Phase 6 — Updates und Wartung

- Jaehrliche Updates zum 1. Januar (Beitragssaetze, BBG).
- ITSG-Zertifikate erneuern.
- Mandanten-Stammdaten aktualisieren.

## Output

- Konfiguriertes Lohnprogramm.
- Mandanten gepflegt.
- Schnittstellen aktiv.

## Strategie und Praxis-Tipps

- LODAS ist Standard fuer StB-Kanzleien — multimandantenfaehig.
- Lohn und Gehalt fuer Mandanten, die selbst Loehne abrechnen, aber StB-Schnittstelle wuenschen.
- Schulungen DATEV-Akademie jaehrlich empfehlenswert.
- Bei Aenderungen am ELStAM-Verfahren: Updates zwingend.

## Querverweise

- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-sv-meldungen-dakota-svnet` — sv.net.
- `stb-lohn-meldungen-sv-elstam-zugang` — ELStAM.

## Quellen und Updates

Stand: 05/2026.

- DATEV LODAS und Lohn und Gehalt Programm- und Bedienungs-Dokumentation (aktuelle Version pruefen).
- DATEV-Programm-Updates jaehrlich (Stand 01.01.) sowie unterjaehrige Reform-Updates (SV-Beitragsbemessungsgrenzen, Mindestlohn).
- Verifikations-Hinweis: konkrete Programmpfade und Menue-Bezeichnungen ggf. abweichend in aktueller DATEV-Version.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-eau-elektronische-arbeitsunfaehigkeit-2023`

**Fokus:** eAU elektronische Arbeitsunfähigkeitsbescheinigung seit 2023. Anwendungsfall AN-Krankmeldung AG-Abruf bei Krankenkasse Entgeltfortzahlung. Methodik Schnittstelle Konfiguration Workflow. Output eAU-Konfiguration.

# eAU — Elektronische Arbeitsunfaehigkeitsbescheinigung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `eAU — Elektronische Arbeitsunfaehigkeitsbescheinigung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Seit 01.01.2023 (mit Uebergangsphase) ist die elektronische Arbeitsunfaehigkeitsbescheinigung (eAU) verpflichtend. AN informiert AG ueber Krankheit; AG ruft eAU-Daten bei der Krankenkasse ueber Schnittstelle ab. Die "gelbe Bescheinigung" auf Papier entfaellt. Voraussetzungen: AG-System mit eAU-Schnittstelle, AN mit GKV (PKV-Versicherte aktuell nicht im eAU-Verfahren).

## Kaltstart-Rueckfragen

1. Hat der AG eAU-Schnittstelle eingerichtet?
2. Welches Lohnprogramm (DATEV LODAS, Lohn und Gehalt)?
3. Welche Krankenkassen sind vertreten?
4. Welche AN sind in PKV (Privat-KV; Ausnahme von eAU)?
5. Welche Mandanten-Schulung der HR-Abteilung erfolgt?
6. Welche Fallback bei Schnittstellen-Stoerung?
7. Welche Konsistenz von Krankheits-Zeiten und Entgeltfortzahlung?
8. Welche § 109 SGB IV-Konformitaet?

## Rechtlicher Rahmen

### Primaernormen

**§ 109 SGB IV** — Elektronisches Verfahren bei Arbeitsunfaehigkeit.

**§ 5 EFZG** — AU-Anzeige- und Nachweispflicht.

**§ 3 EFZG** — Entgeltfortzahlung.

**EFZG, § 5 Abs. 1a (durch eAU-Reform)** — Anpassung Nachweisweg.

### Verwaltungsanweisungen

- BMAS zum eAU-Verfahren.
- GKV-Spitzenverband Rundschreiben.

## Workflow

### Phase 1 — Anmeldung des AG zum eAU-Verfahren

- Schnittstelle im Lohnprogramm einrichten (DATEV LODAS / Lohn und Gehalt, Sage HR, eGecko, sage Lohn). Konkrete Programmpfade je Lohnprogramm-Version in der Programm-Onlinehilfe oder Dokumentation nachschlagen.
- ITSG-Zertifikat erforderlich (Sicherheitszertifikat fuer SV-Datenuebermittlung); Verlaengerung jaehrlich.
- Anmeldung des AG zum eAU-Abrufverfahren ueber den GKV-Datenaustausch-Standard (Verfahren der GKV-Spitzenverbaende auf Basis § 109 SGB IV); konkrete technische Konfiguration in der Lohnprogramm-Dokumentation pruefen.

### Phase 2 — Krankmeldungs-Prozess

```
AN meldet sich krank (Telefon, Mail)
 ↓
AG erfaesst Krankheitsbeginn in Lohnprogramm
 ↓
AG-System ruft automatisch eAU-Daten ab
 ↓
Krankenkasse liefert Diagnose-Codes und Dauer
 ↓
Lohnabrechnung mit Entgeltfortzahlung-Anteil
```

### Phase 3 — Datenrueckmeldung

- Krankenkasse liefert: Anfangs- und Enddatum der AU, fortdauernd ja/nein.
- Hinweis: Diagnose-Codes werden seit der eAU-Reform regelmaessig **nicht** mehr an den AG uebermittelt (Datenschutz-Aspekt); konkrete Daten-Felder gemaess GKV-Datenuebermittlungs-Standard pruefen.
- AG-Pflicht: AU-Zeiten in Lohnabrechnung integrieren, Entgeltfortzahlung gemaess § 3 EFZG (bis 6 Wochen).

### Phase 4 — Fallback-Verfahren

- Bei Schnittstellen-Stoerung: traditionelle gelbe Bescheinigung.
- PKV-Versicherte: traditionelle Bescheinigung (eAU bisher nicht).

### Phase 5 — Datenschutz

- Im eAU-Verfahren erhaelt der AG nach geltender Praxis grundsaetzlich nur AU-Beginn, AU-Ende und Information ueber Folgebescheinigung — Diagnose-Codes verbleiben bei der Krankenkasse (DSGVO-konform).
- AG unterliegt Geheimhaltungspflicht hinsichtlich aller AU-bezogenen Daten.
- Keine Weitergabe an Dritte (Ausnahme: gesetzliche Meldungen).

### Phase 6 — Mandantenkommunikation

- HR-Abteilung schulen.
- Schnittstellen-Wartung.

## Output

- eAU-Schnittstelle aktiv.
- Krankheits-Lohnabrechnung automatisch.

## Strategie und Praxis-Tipps

- eAU ist Effizienz-Vorteil — keine Papierabholung mehr.
- Bei PKV-Versicherten: traditionelles Verfahren parallel.
- Schnittstellen-Stoerungen: rechtzeitig Test (insbesondere zum Jahreswechsel).
- DATEV-Tipp: DATEV LODAS eAU-Modul mit automatischem Abruf.

## Querverweise

- `stb-lohn-krankheit-entgeltfortzahlung-efzg` — Krankheit.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.
- `stb-lohn-meldungen-sv-elstam-zugang` — SV-Meldungen.

## Quellen und Updates

Stand: 05/2026.

- SGB IV § 109.
- EFZG §§ 3, 5.
- BMAS zum eAU-Verfahren.
- GKV-Spitzenverband Rundschreiben.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (generischer Programmpfad-Hinweis, nicht versionsspezifisch belegbar, Verweis auf Onlinehilfe) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-erechnung-pflicht-b2b-2025-2026`

**Fokus:** eRechnung-Pflicht B2B seit 01.01.2025 § 14 UStG ViDA. Anwendungsfall Prüfung Mandantenbetrieb eRechnungs-Empfang Versand Übergangsfristen PDF reicht nicht mehr. Methodik Format XRechnung ZUGFeRD. Output eRechnungs-Konfiguration.

# eRechnung-Pflicht B2B seit 01.01.2025

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `eRechnung-Pflicht B2B seit 01.01.2025` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Seit 01.01.2025 sind alle inlaendischen B2B-Unternehmer verpflichtet, **eRechnungen empfangen zu koennen** (§ 14 Abs. 1 i.V.m. Abs. 2 UStG n.F., Wachstumschancengesetz vom 27.03.2024, BMF-Schreiben vom 15.10.2024). Die **Versandpflicht** ist demgegenueber gestaffelt: Bis 31.12.2026 duerfen Rechnungen weiterhin als PDF/sonstige elektronische Form mit Empfaengerzustimmung versendet werden; bis 31.12.2027 bleibt dies fuer Kleinunternehmen mit Vorjahresumsatz bis 800.000 EUR moeglich. Ab 01.01.2028 ist der eRechnungs-Versand zwischen inlaendischen Unternehmern verbindlich. Akzeptierte Formate: XRechnung (CIUS-konform, reines XML) und ZUGFeRD ab Version 2.0.1 (Hybridformat). Der Steuerberater muss Mandanten ueber die Pflicht informieren und insbesondere die Empfangsbereitschaft sicherstellen.

## Kaltstart-Rueckfragen

1. Welche Umsatzgroesse hat der Mandant (Uebergangsfristen)?
2. Welche Kunden — B2B (eRechnung-pflichtig) oder B2C (PDF weiterhin moeglich)?
3. Welche Lieferanten senden bereits eRechnungen?
4. Welche ERP/Faktura-Software wird genutzt?
5. Welche Empfangs-Adresse (Mail-Postfach oder Peppol)?
6. Welche Archivierung GoBD-konform?
7. Welche Format-Praeferenz XRechnung vs. ZUGFeRD?
8. Welche Mandanten-Beratungsbedarf?

## Rechtlicher Rahmen

### Primaernormen

**§ 14 Abs. 1 S. 3 UStG n.F.** — Definition eRechnung als strukturiertes elektronisches Format gemaess EN-16931.

**§ 14 Abs. 2 UStG n.F.** — Ausstellungspflicht in eRechnungsform zwischen inlaendischen Unternehmern (mit Uebergangsregeln § 27 Abs. 38 UStG).

**§ 27 Abs. 38 UStG n.F.** — Uebergangsregeln (sonstige Rechnungsform bis 31.12.2026 / 31.12.2027 fuer Kleinunternehmer mit Umsatz <= 800.000 EUR).

**§ 33 UStDV, § 34 UStDV** — Ausnahmen (Kleinbetrag, Fahrausweis).

**Wachstumschancengesetz vom 27.03.2024** — BGBl. I 2024 Nr. 108.

**EU-RL 2014/55/EU** — eRechnungs-Standard EN-16931.

### Verwaltungsanweisungen

- **BMF v. 15.10.2024**, GZ III C 2 - S 7287-a/23/10001 :007 — Einfuehrungsschreiben zur obligatorischen eRechnung ab 01.01.2025 (verfuegbar unter bundesfinanzministerium.de).
- **BMF v. 15.10.2025**, GZ III C 2 - S 7287-a/00019/007/243 — Zweites (klarstellendes) Schreiben mit Anpassung des Umsatzsteuer-Anwendungserlasses; unterscheidet Format- und Inhaltsfehlerklassen, definiert Pflichten des Empfaengers und Validierungsempfehlung des Senders (verfuegbar unter bundesfinanzministerium.de).
- BMF v. 22.06.2023 ViDA (Hintergrund).

## Workflow

### Phase 1 — Geltungsbereich (Wachstumschancengesetz 2024)

| Phase | Zeitraum | Pflicht |
|---|---|---|
| Empfang | Ab 01.01.2025 | Alle inlaendischen B2B-Unternehmer (zwingende Empfangsbereitschaft, ohne Schwellenwert) |
| Versand sonstige elektr. Rechnungen | 01.01.2025 - 31.12.2026 | Versand als PDF / sonstige elektronische Form weiter zulaessig, sofern Empfaengerzustimmung |
| Versand sonstige elektr. Rechnungen, Kleinunternehmer | 01.01.2025 - 31.12.2027 | Verlaengert fuer Rechnungsausstellung durch Unternehmer mit Vorjahresumsatz <= 800.000 EUR |
| eRechnung-Versand vollumfaenglich | Ab 01.01.2028 | Verbindlich; PDF/Papier zwischen inlaendischen Unternehmern nicht mehr ausreichend |
| Ausgenommen | dauerhaft | Kleinbetragsrechnungen § 33 UStDV (bis 250 EUR), Fahrausweise § 34 UStDV, B2C-Rechnungen |

Stand BMF-Schreiben vom 15.10.2024 (IV D 2 - S 7287-a/23/10001:007); Aktualisierungen laufend ueber bzst.de und BMF-Newsletter abrufen.

### Phase 2 — Format-Wahl

| Format | Eigenschaften |
|---|---|
| XRechnung | Reines XML nach CIUS der KoSIT; Standard fuer oeffentliche Auftraggeber (E-Rech-VO Bund seit 27.11.2020) |
| ZUGFeRD ab Version 2.0.1 | Hybridformat PDF/A-3 mit eingebettetem XML; menschen- und maschinenlesbar; ab Profil EN-16931 eRechnung-konform |
| Sonstige (z.B. EDIFACT) | Nur zulaessig, wenn EN-16931-konforme strukturierte Rechnungsdaten enthalten / extrahierbar sind |

Hinweis: Das ZUGFeRD-Profil MINIMUM und BASIC-WL sind **nicht** eRechnung-konform i.S.d. § 14 Abs. 1 S. 6 UStG.

### Phase 3 — Empfangs-Setup

- Mailpostfach fuer eRechnung definieren.
- Peppol-Anschluss (selten in DACH; wachsend).
- DATEV Empfang ueber DUO oder externes Tool (z.B. Inposia, Coupa).

### Phase 4 — Versand-Setup

- Faktura-Software mit eRechnungs-Ausgabe in XRechnung (XML) und/oder ZUGFeRD (PDF/A-3 + XML).
- Datenmapping: Konten- und Stammdaten zu den Pflichtfeldern nach EN-16931 (BT-Felder); insbesondere Leitweg-ID bei B2G-Rechnungen.
- Test-Rechnungen mit Lieferanten / Kunden vor Echtbetrieb (Validierung ueber KoSIT-Validator fuer XRechnung).

### Phase 5 — Archivierung

- GoBD-konforme Archivierung im Originalformat XML.
- 10 Jahre Aufbewahrung.
- Lesbarkeitserhaltung.

### Phase 6 — Mandanten-Information

Mustertext fuer den Mandantenrundbrief (anzupassen an Mandantenstruktur):

```
Sehr geehrte Damen und Herren,

seit dem 01.01.2025 sind alle inlaendischen B2B-Unternehmer verpflichtet,
eRechnungen empfangen zu koennen (§ 14 UStG i.V.m. Wachstumschancengesetz).
Eine reine PDF-Rechnung erfuellt nicht mehr die Anforderungen an eine eRechnung;
ein Vorsteuerabzug kann gefaehrdet sein.

Wir bitten Sie, folgende Schritte zu pruefen:
1. Empfangs-E-Mail-Adresse fuer eRechnungen festlegen
 (z.B. rechnungen@ihre-firma.de) und Lieferanten mitteilen.
2. Buchhaltungssoftware auf eRechnungs-Empfang konfigurieren
 (XRechnung XML / ZUGFeRD ab Profil EN-16931).
3. GoBD-konforme Archivierung im Originalformat XML sicherstellen.
4. Bis 31.12.2026 (bzw. 31.12.2027 fuer Mandanten mit Umsatz <= 800.000 EUR)
 kann der Versand weiterhin als PDF mit Empfaengerzustimmung erfolgen;
 ab 01.01.2028 ist der eRechnungs-Versand zwingend.

Fuer die Einrichtung des Empfangs- und Versand-Workflows beraten wir Sie gerne.

Mit freundlichen Gruessen
[StB-Kanzlei]
```

- Konfigurationsberatung als separater Auftrag nach § 13 StBVV (Beratungstaetigkeit) oder Pauschalvereinbarung nach § 14 StBVV.
- Bei kleineren Mandanten Software-Empfehlung (z.B. DATEV Unternehmen Online, ZUGFeRD-faehige Faktura-Loesungen).

## Output

- Konfiguration Empfang/Versand eRechnung.
- Archivierungs-Routine.
- Mandanten-Information.

## Strategie und Praxis-Tipps

- Die wichtigste Stufe ist seit 01.01.2025 die **Empfangsbereitschaft** — ohne sie kann ein eRechnungs-pflichtiger Lieferant nicht ordnungsgemaess abrechnen, der Mandant verliert ggf. den Vorsteuerabzug.
- Mindest-Empfangsweg ist ein E-Mail-Postfach, das XML-/PDF-Anhaenge bis ueblicher Groesse annimmt; ein dediziertes eRechnungs-Postfach erleichtert und GoBD-Archivierung.
- ZUGFeRD eignet sich als Einstiegsformat fuer Mittelstand und Kleinunternehmer (PDF bleibt fuer den Anwender lesbar). XRechnung ist Pflichtformat im B2G-Verkehr mit Bundesstellen (E-Rech-VO seit 27.11.2020) und in einigen Laendern.
- DATEV-Hinweis: In DATEV Unternehmen Online laesst sich der eRechnungs-Empfang ueber das Postfach "Eingangsrechnungen" und das ZUGFeRD-Auswertungsmodul konfigurieren; konkrete Programmpfade in DATEV-Onlinehilfe und Versionshinweisen nachschlagen.
- StBVV: Konfigurationsberatung als Beratungsleistung gem. § 21 StBVV oder Pauschalvereinbarung gem. § 14 StBVV (Mandanten frueh per Rundschreiben informieren — Mustertext im Skill `stb-mandantenanfrage-reaktion-frist-laufend`).

## Querverweise

- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.

## Quellen und Updates

Stand: 05/2026.

- UStG §§ 14, 27 Abs. 38; UStDV §§ 33, 34.
- Wachstumschancengesetz vom 27.03.2024 (BGBl. I 2024 Nr. 108).
- BMF-Schreiben vom 15.10.2024, GZ III C 2 - S 7287-a/23/10001 :007 (Einfuehrungsschreiben).
- BMF-Schreiben vom 15.10.2025, GZ III C 2 - S 7287-a/00019/007/243 (Zweites Anwendungsschreiben, Anpassung UStAE).
- EU-RL 2014/55/EU; Norm EN-16931.
- KoSIT XRechnung-Spezifikation Version 3.0.2 (Stand: Winter 2025/26, gueltig ab 31.01.2026; jeweils aktuelle Fassung unter xeinkauf.de abrufbar).
- ZUGFeRD-Spezifikation (FeRD), aktuelle Profile pruefen.
- ViDA (VAT in the Digital Age) — Beschluss Rat der EU v. 11.03.2025; ABl. EU v. 25.03.2025; in Kraft getreten 14.04.2025; stufenweise Umsetzung bis 2035; Digital Reporting Requirements (DRR) ab 01.07.2030 fuer grenzueberschreitende B2B-Lieferungen.
- Hinweis: alle Werte und Fristen laufend gegen BMF-Newsletter und bzst.de abgleichen.

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 1 bestaetigt (BMF-Schreiben 15.10.2024 bestaetigt), 3 ersetzt (DATEV-Programmpfad auf Onlinehilfe verwiesen; KoSIT XRechnung-Spezifikation 3.0.2 Winter 2025/26 bestaetigt; ViDA Ratsbeschluss 11.03.2025 bestaetigt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-jahresabschluss-anlagenverzeichnis-afa`

**Fokus:** Anlagenverzeichnis und AfA-Buchung Jahresabschluss. Anwendungsfall vollständige Aktualisierung Anlagen Zugaenge Abgaenge AfA-Methoden Sonderabschreibung 7g 7b 6b EStG. Methodik AfA-Tabellen. Output Anlagenspiegel.

# Anlagenverzeichnis und AfA — Jahresabschluss-Aktualisierung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anlagenverzeichnis und AfA — Jahresabschluss-Aktualisierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Anlagenspiegel (Anlagenverzeichnis) bildet die Bestandsentwicklung des Anlagevermoegens ueber das Geschaeftsjahr ab: Anfangsbestand, Zugaenge, Abgaenge, Abschreibungen, Zuschreibungen, Endbestand. Im Jahresabschluss ist er Pflicht-Bestandteil bei mittelgrossen und grossen Kapitalgesellschaften (§ 268 Abs. 2 HGB).

## Kaltstart-Rueckfragen

1. Welche Anlagengruppen sind vorhanden (immaterielle WG, Sachanlagen, Finanzanlagen)?
2. Welche Zugaenge im Jahr (Investitionen)?
3. Welche Abgaenge (Verkauf, Verschrottung, Entnahme)?
4. Welche AfA-Methode (linear, degressiv, Leistungs-AfA)?
5. Sonderabschreibungen § 7g, § 7b, § 6b EStG?
6. Welche Nutzungsdauern laut AfA-Tabelle?
7. Welche Investitionsabzugsbetraege § 7g EStG anstehend?
8. Welche GWG-Konfiguration (Wahlrecht 800 EUR oder Pool 1.000 EUR)?

## Rechtlicher Rahmen

### Primaernormen

**§ 247 HGB** — Anlagevermoegen-Definition.

**§ 253 HGB** — Bewertung mit fortgefuehrten Anschaffungs-/Herstellungskosten.

**§ 268 Abs. 2 HGB** — Anlagenspiegel-Pflicht.

**§ 6 EStG** — Bewertung.

**§ 7 EStG** — AfA-Methoden.

**§ 7g EStG** — IAB und Sonderabschreibung.

**§ 7b EStG** — Sonderabschreibung Wohnungsbau (befristet).

**§ 6 Abs. 2 EStG** — GWG bis 800 EUR.

**§ 6 Abs. 2a EStG** — Pool-Abschreibung 250-1.000 EUR.

### Verwaltungsanweisungen

- BMF AfA-Tabellen.
- § 7g EStG in der Fassung des JStG 2020 (massgeblich ab 01.01.2020; Sonder-AfA 40 Prozent, IAB 50 Prozent); aktuelle Gesetzesfassung auf gesetze-im-internet.de.

## Workflow

### Phase 1 — Anlagenspiegel-Struktur

```
ANLAGENSPIEGEL [Geschaeftsjahr]
Position | AHK Anfang | Zugang | Abgang | Umgliederung | Endbestand AHK | Kum. AfA Anfang | AfA des Jahres | Abgang AfA | Kum. AfA Ende | Buchwert Anfang | Buchwert Ende
Immaterielle WG | [X] | [Y] | [Z] | - | [A] | [B] | [C] | [Z] | [D] | [E] | [F]
Sachanlagen | ...
Finanzanlagen | ...
```

### Phase 2 — Zugaenge

- Anschaffungskosten (incl. Anschaffungsnebenkosten).
- Herstellungskosten (Eigenbau).
- Aktivierungswahlrechte fuer immaterielle WG.

### Phase 3 — Abgaenge

- Verkauf: Buchwert ausbuchen, Erloes gegenrechnen.
- Verschrottung: voll abschreiben.
- Entnahme (Personenges): Privatanteil.

### Phase 4 — AfA-Methoden

| Methode | Anwendung |
|---|---|
| Linear (§ 7 Abs. 1 EStG) | Standard nach AfA-Tabelle |
| Degressiv (§ 7 Abs. 2 EStG) | Wachstumschancengesetz 2024: bewegliche WG 01.04.2024-31.12.2024 max. 20 %, 2-fach linear. Ab 01.07.2025 (Investitionsbooster): bewegliche WG max. 30 %, 3-fach linear, befristet bis 31.12.2027 (Koalitionsvertrag 2025). Fuer neue Zugaenge 2026: 30 %-Regel pruefen. |
| Leistungs-AfA (§ 7 Abs. 1 S. 6 EStG) | Bewegliche WG mit messbarer Leistung |
| Sonder-AfA § 7g Abs. 5 EStG | KMU: bis 40 % der AHK (fuer Anschaffungen ab 01.01.2024; fuer Anschaffungen vor 01.01.2024: 20 %; JStG 2020), frei verteilbar auf Anschaffungsjahr und 4 Folgejahre; Gewinngrenze 200.000 EUR im Vorjahr (§ 7g Abs. 6 EStG) |
| Sonder-AfA § 7b EStG | Mietwohnungsneubau: 5 % p.a. fuer 4 Jahre; Bauantrag nach 31.12.2022 und vor 01.10.2029; EH-40-Standard mit QNG-Siegel; Baukostengrenze 5.200 EUR/m²; Foerderhoechstgrenze 4.000 EUR/m² (Stand: Wachstumschancengesetz 2024, BGBl. 2024 I Nr. 108) |

### Phase 5 — Investitionsabzugsbetrag § 7g EStG

- IAB: bis zu 50 % der voraussichtlichen Anschaffungs- oder Herstellungskosten ausserbilanziell gewinnmindernd vor der Anschaffung; Hoechstbetrag 200.000 EUR im Wirtschaftsjahr (Werte aktuellen Stand pruefen).
- Voraussetzung: einheitliche Gewinngrenze 200.000 EUR (durch das JStG 2020 fuer alle Einkunftsarten); aktuellen Stand fortlaufend pruefen.
- IAB ist ausserbilanzielle Gewinnminderung (keine handelsrechtliche Ruecklage; nur in der steuerlichen Gewinnermittlung).
- Investitionsfrist: bis zum Ende des **dritten** auf das Abzugsjahr **folgenden** Wirtschaftsjahres (§ 7g Abs. 3 S. 1 EStG) — insgesamt also rund 4 Jahre Zeit einschliesslich des Abzugsjahres.
- Aufloesung im Jahr der tatsaechlichen Investition gegen Hinzurechnung; bei Wegfall der Voraussetzungen rueckwirkende Aufloesung mit Anpassung des Veranlagungsjahres und Verzinsung gem. § 233a AO.

### Phase 6 — GWG

- Sofortabschreibung bis 800 EUR netto.
- Pool-Abschreibung 250-1.000 EUR (5 Jahre).
- Wahlrecht im Wirtschaftsjahr einheitlich.

## Output

- Anlagenspiegel als Bestandteil JA.
- AfA-Buchung im Hauptbuch.
- IAB-Dokumentation.

## Strategie und Praxis-Tipps

- Anlagenspiegel ist Pflicht bei mittelgrossen/grossen Kapitalgesellschaften (§ 288 HGB).
- AfA-Tabellen sind nicht zwingend (BMF-Tabellen sind Verwaltungsanweisung, aber praktisch verbindlich).
- IAB § 7g EStG: gestaltungsstark, aber 3-Jahres-Frist beachten.
- GWG-Wahlrecht jaehrlich, aber einheitlich im Wirtschaftsjahr.

## Querverweise

- `stb-susa-anlagenkonten-ueberblick` — Anlagen in SuSa.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 247, 253, 268, 288.
- EStG §§ 5, 6, 7, 7b, 7g.
- BMF AfA-Tabellen.
- Hinweis: degressive AfA 2026 nach § 7 Abs. 2 EStG: Investitionsbooster ab 01.07.2025 (max. 30 %, 3-fach linear, bis 31.12.2027) gilt fuer neue Zugaenge. Fuer Zugaenge 01.04.2024-31.12.2024: max. 20 %, 2-fach linear.
- Hinweis: § 7g EStG Sonder-AfA 40 Prozent und IAB 50 Prozent stabil seit JStG 2020 (fuer Anschaffungen ab 01.01.2024); Gewinngrenze 200.000 EUR.

<!-- AUDIT 27.05.2026 | welle 6 | 6 Marker aufgeloest: 5 bestaetigt (degressive AfA 2024/2026, § 7g 40%, § 7b bis 2029 recherchiert), 1 ersetzt (BMF 2007 obsolet, durch aktuelle Gesetzeslage ersetzt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-jahresabschluss-bestandskonten-abstimmung`

**Fokus:** Bestandskonten-Abstimmung zum Jahresabschluss. Anwendungsfall Endbestaende Bank Kasse Forderungen Verbindlichkeiten Anlagen Eigenkapital abstimmen Inventur-Werte einarbeiten. Methodik Saldenabstimmung Vergleich. Output abgestimmte Bestandskonten.

# Bestandskonten-Abstimmung zum Jahresabschluss

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bestandskonten-Abstimmung zum Jahresabschluss` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Vor dem JA-Endlauf muessen alle Bestandskonten (Klasse 0-3 SKR 03 bzw. entsprechende SKR-04-Konten) abgestimmt sein: Bank gegen Bankauszug, Kasse gegen Kassenbericht, Forderungen gegen Personenkonten, Anlagen gegen Anlagenspiegel, Eigenkapital gegen Gesellschaftervereinbarungen. Differenzen muessen aufgeklaert werden.

## Kaltstart-Rueckfragen

1. Welche Bestandskonten sind vorhanden?
2. Welche Saldenabstimmungs-Antworten liegen vor?
3. Liegen Bankbestaetigungen vor (Saldenbestaetigung)?
4. Anlagenspiegel mit Hauptbuch abgestimmt?
5. Liegen Inventur-Werte vor?
6. Welche Korrekturen aus der Saldenabstimmung?
7. Welche Sondervorgaenge (Kapitalbewegungen)?
8. Welche Werterhellung nach Stichtag?

## Rechtlicher Rahmen

### Primaernormen

**§ 240 HGB** — Inventarpflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 253 HGB** — Bewertung Vermoegen.

**§ 246 HGB** — Vollstaendigkeit.

**§ 5 EStG** — Massgeblichkeit Handelsbilanz.

### Standards

- IDW PS 480.
- IDW PS 302 (Saldenbestaetigungen).

## Workflow

### Phase 1 — Bestandskonten-Inventur

| Konto | Abstimmungs-Basis |
|---|---|
| Bank | Bankauszuege, Saldenbestaetigung Bank |
| Kasse | Kassenbericht, Z-Bons |
| Forderungen LuL | Debitoren-OPOS, Saldenbestaetigung Kunden |
| Sonstige Forderungen | Einzelnachweis |
| Vorraete | Inventur-Protokoll |
| Anlagen | Anlagenspiegel |
| Verbindlichkeiten LuL | Kreditoren-OPOS, Saldenbestaetigung Lieferanten |
| Bank-Verbindlichkeiten | Darlehensvertraege, Saldenbestaetigung Bank |
| Steuerverbindlichkeiten | FA-Bescheide |
| SV-Verbindlichkeiten | KK-Beitragsabrechnungen |
| Rueckstellungen | Bewertungsgrundlagen |
| Eigenkapital | Gesellschaftervereinbarungen, Vorjahresvortrag |

### Phase 2 — Differenzen klaeren

- Bei Hauptbuch-Nebenbuch-Differenzen: Personenkonto-Pflege.
- Bei Bankabstimmungs-Differenzen: Cut-off-Buchungen.
- Bei Vorraete-Differenzen: Inventur-Pruefung.

### Phase 3 — Anpassungs-Buchungen

- Endgueltige AfA-Buchung.
- Periodenabgrenzungs-Buchungen.
- Rueckstellungs-Buchungen.

### Phase 4 — Werterhellung

- Wesentliche Ereignisse zwischen Stichtag und Aufstellung pruefen.
- Insolvenz-Antraege bei Schuldnern (Forderungsausfall-Risiko).
- Wesentliche Vertragsabschluesse (Auswirkung auf Risiko/Rueckstellung).

### Phase 5 — Bestand-Bewertung

- Forderungen: Einzelwertberichtigung bei zweifelhaften Schuldnern.
- Vorraete: Niederstwertprinzip; Veraltete Bestaende.
- Anlagen: Ausserplanmaessige Abschreibung bei dauerhafter Wertminderung.

### Phase 6 — Endgueltige Bilanz

- Bestandskonten-Endsalden bilden Bilanzposten.
- Endsalden in Bilanz uebernehmen.
- Konsistenzcheck.

## Output

- Abgestimmte Bestandskonten.
- Anpassungs-Buchungen dokumentiert.
- Bilanz vorbereitet.

## Strategie und Praxis-Tipps

- Bestandskonten-Abstimmung ist Pflicht — nicht abgekuerzte Pruefung.
- Bei Pruefungspflicht: WP fordert Abstimmung formell.
- Bei groesseren Mandanten: Saldenabstimmung mit Lieferanten/Kunden Standard.
- Werterhellung-Pruefung kann erhebliche Auswirkungen haben.

## Querverweise

- `stb-susa-saldenabstimmung-bestaetigung` — Saldenabstimmung.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-warenbestand-inventur` — Inventur.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — AfA.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 246, 252, 253.
- EStG § 5.
- IDW PS 480, IDW PS 302.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-jahresabschluss-kassenfuehrung-gobd-pflichten`

**Fokus:** Kassenführung GoBD-Pflichten. Anwendungsfall Mandanten mit Bargeschäft Kasse Aufzeichnungspflichten Kassenbuch elektronische Aufzeichnungssysteme TSE technische Sicherheitseinrichtung. Methodik Prüfung Sorgfalt. Output GoBD-konforme Kassenführung.

# Kassenfuehrung — GoBD-Pflichten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kassenfuehrung — GoBD-Pflichten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Bei Mandanten mit Bargeschaeft (Gastronomie, Einzelhandel) ist die Kassenfuehrung ein sensibler Pruefpunkt. § 146 AO verlangt Zeitgerechtigkeit und Vollstaendigkeit; § 146a AO erfordert seit 01.01.2020 (BMF-Nichtbeanstandungsregelung bis 30.09.2020) eine zertifizierte Technische Sicherheitseinrichtung (TSE) bei elektronischen Aufzeichnungssystemen. Seit 01.01.2020 besteht zudem die Belegausgabepflicht nach § 146a Abs. 2 AO. Verstoesse koennen zur Schaetzungsbefugnis (§ 162 AO), Bussgeld (§ 379 AO) bzw. zu steuerstrafrechtlicher Bewertung als Steuerhinterziehung fuehren.

## Kaltstart-Rueckfragen

1. Welche Kassenart — offene Ladenkasse, elektronische Kasse, mobile Kasse?
2. TSE eingebaut?
3. Welches Kassensystem (Hersteller, Modell)?
4. Wer fuehrt Kassenbuch (Mandant, StB)?
5. Welche Sondersituation (Trinkgeld, Wechselgeld, Skontoabzug)?
6. Welche Pruefungen Vergangenheit (Kassenpruefung, Aussenpruefung)?
7. Welche Belegpflicht-Vorgaben?
8. Welche taegliche Z-Bon-Routine?

## Rechtlicher Rahmen

### Primaernormen

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit.

**§ 146a AO** — Aufzeichnungspflicht elektronische Aufzeichnungssysteme; TSE.

**§ 146b AO** — Belegausgabepflicht.

**§ 379 AO** — Bussgeld bei Verstoss.

**§ 162 AO** — Schaetzung bei Maengeln.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 zu GoBD.
- **BMF v. 11.03.2024** — 1. Aenderung GoBD (Anpassung an gesetzliche Aenderungen); abrufbar bundesfinanzministerium.de (BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd).
- **BMF v. 14.07.2025** — 2. Aenderung GoBD (Folge von eRechnung, weitere gesetzliche Anpassungen); abrufbar bundesfinanzministerium.de.
- BMF v. 17.06.2019 zu § 146a AO (TSE).
- BMF v. 11.06.2020 zur Kassennachschau § 146b AO.
- **Meldepflicht elektronischer Aufzeichnungssysteme § 146a Abs. 4 AO**: Pflicht seit 01.01.2025 (ELSTER/Mein ELSTER, ERiC-Schnittstelle); Altsysteme vor 01.07.2025 anzumelden bis 31.07.2025; ab 01.07.2025 erworbene Systeme innerhalb 1 Monats nach Anschaffung.

## Workflow

### Phase 1 — Kassensystem pruefen

| System | TSE-Pflicht | Anforderungen |
|---|---|---|
| Offene Ladenkasse (Geldkasten) | Keine TSE; aber tagliche Aufzeichnung in Kassenbericht | Manuelle Kassenfuehrung |
| Elektronische Kasse / Registrierkasse | TSE seit 01.01.2020 | Zertifizierte TSE eingebaut |
| Cloud-Kassensystem | TSE | Auch Cloud-Loesungen brauchen TSE |
| App-Kasse | TSE | Bei elektronischer Speicherung |

### Phase 2 — TSE-Pruefung

- TSE-Modul muss zertifiziert sein (BSI).
- TSE-Daten werden mit jeder Buchung erstellt (Signatur, Zeitstempel).
- Speicherung 10 Jahre.

### Phase 3 — Tagliche Routine

- Z-Bon (Tagesabschluss): am Tagesende ausdrucken.
- Kassensturz: Soll-Bestand vs. Ist-Bestand.
- Differenzen klaeren.
- Kassenbericht oder elektronisch.

### Phase 4 — Belegpflicht § 146b AO

- Seit 01.01.2020: jeder Verkauf Beleg.
- Beleg kann Papier oder elektronisch sein.
- Verstoss: § 379 AO Bussgeld.

### Phase 5 — Bei Pruefung

- Kassennachschau § 146b AO: unangemeldet moeglich.
- Aussenpruefer: Kassenfuehrung vorlegen.
- Bei wesentlichen Maengeln: Schaetzung § 162 AO.

### Phase 6 — Verfahrensdokumentation

- Verfahrensdokumentation des Kassensystems (Pflicht).
- Bedienungsanleitung TSE.
- Beleg-Archivierung GoBD-konform 10 Jahre.

## Output

- GoBD-konforme Kassenfuehrung.
- Verfahrensdokumentation.
- Belegarchiv.

## Strategie und Praxis-Tipps

- Die TSE-Pflicht ist hart durchgesetzt; der Bussgeldrahmen reicht nach § 379 Abs. 6 AO bis 25.000 EUR pro Verstoss.
- Die Verfahrensdokumentation (Konfiguration, Bedienungsanleitung, Aenderungsprotokoll) ist haeufig vernachlaessigt, aber ausdruecklich Pflichtbestandteil nach GoBD (BMF v. 28.11.2019, Rz. 153 ff.).
- Bei Mandanten mit hohem Bargeschaeft ist eine kontinuierliche StB-Begleitung sinnvoll; bei Verdacht auf Manipulation der Aufzeichnungen ist der Mandant nachweisbar (Aktenvermerk, schriftliche Belehrung) auf die Sanktionsrisiken nach § 379 AO bzw. § 370 AO hinzuweisen — vgl. die Eskalations-Routine in `stb-mandantenanfrage-reaktion-frist-laufend` und die berufsrechtliche Hinweispflicht aus § 102 StaRUG bei drohender Insolvenz.
- Die Kassennachschau nach § 146b AO erfolgt unangekuendigt — auch zu Beginn der Geschaeftsoeffnung; Mandanten sollten auf den Umgang mit dem Pruefer (Vorlage Kassen-Z-Bons, TSE-DSFinV-K-Daten) geschult werden.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-fehlerquellen-haeufig` — Fehlerquellen.
- `stb-susa-erstellen-grundlagen` — SuSa.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 146, 146a, 146b, 162, 379.
- BMF v. 28.11.2019 zu GoBD; BMF v. 11.03.2024 (1. Aenderung GoBD); BMF v. 14.07.2025 (2. Aenderung GoBD).
- BMF v. 17.06.2019 (TSE).
- BMF v. 11.06.2020 (Kassennachschau).
- § 146a Abs. 4 AO Meldepflicht (Mein ELSTER) seit 01.01.2025; Altsysteme bis 31.07.2025, Neusysteme ab 01.07.2025 innerhalb 1 Monats.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-jahresabschluss-veroeffentlichung-bundesanzeiger`

**Fokus:** Jahresabschluss-Veröffentlichung Bundesanzeiger § 325 HGB. Anwendungsfall Pflichtveröffentlichung Kapitalgesellschaft Frist 12 Monate Groessenklassen Erleichterungen. Methodik elektronische Übermittlung. Output Bundesanzeiger-Eintrag.

# Jahresabschluss-Offenlegung im Unternehmensregister

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Jahresabschluss-Offenlegung im Unternehmensregister` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Kapitalgesellschaften und KapCoGes (insbesondere GmbH & Co. KG) muessen ihren Jahresabschluss offenlegen (§ 325 HGB). Frist: 12 Monate nach Bilanzstichtag. Groessenklassen (§ 267 HGB) bestimmen Umfang und Veroeffentlichungs- bzw. Hinterlegungsweg. Verspaetung loest ein Ordnungsgeldverfahren des Bundesamts fuer Justiz (BfJ) gemaess § 335 HGB aus (Ordnungsgeld 2.500-25.000 EUR, ggf. mehrfach festsetzbar). Zustaendige Plattform: Seit den Geschaeftsjahren mit Beginn nach dem 31.12.2021 erfolgt die Offenlegung nach dem DiRUG (BGBl. I 2021, 3338) ueber das **Unternehmensregister** (publikations-plattform.de), nicht mehr direkt ueber den Bundesanzeiger; fuer aeltere Geschaeftsjahre gilt noch die Veroeffentlichung im Bundesanzeiger.

## Kaltstart-Rueckfragen

1. Welche Rechtsform — Kapitalgesellschaft oder KapCoGes?
2. Welche Groessenklasse (Kleinst, Klein, Mittel, Gross)?
3. Welcher Bilanzstichtag?
4. Welche Frist 12 Monate (Ende Folgejahr)?
5. Welche Erleichterungen nutzbar?
6. Bestehen Sondersituationen (Vorperioden noch nicht offen)?
7. Wer uebernimmt Uebermittlung — StB oder Mandant?
8. Liegt elektronisches Zertifikat vor?

## Rechtlicher Rahmen

### Primaernormen

**§ 325 HGB** — Offenlegungspflicht (Geschaeftsjahre ab 01.01.2022: Uebermittlung an das Unternehmensregister gem. § 8b HGB).

**§ 8b HGB** — Unternehmensregister als zentrale Plattform.

**§§ 326-329 HGB** — groessenabhaengige Erleichterungen.

**§ 267 HGB, § 267a HGB** — Groessenklassen (inkl. Kleinst-Kapitalgesellschaft).

**§ 264a HGB** — Anwendung auf KapCoGes (z.B. GmbH & Co. KG).

**§ 335 HGB** — Ordnungsgeldverfahren des BfJ (2.500-25.000 EUR pro Festsetzung; mehrfache Festsetzung zulaessig).

### Verwaltungsanweisungen

- BfJ-Merkblaetter zum Ordnungsgeldverfahren.
- DiRUG (Gesetz zur Umsetzung der Digitalisierungsrichtlinie, BGBl. I 2021, 3338) — Umstellung Bundesanzeiger → Unternehmensregister.

## Workflow

### Phase 1 — Groessenklassen § 267 HGB

| Klasse | Bilanzsumme | Umsatz | AN-Zahl |
|---|---|---|---|
| Kleinst (§ 267a HGB) | <= 350.000 EUR | <= 700.000 EUR | <= 10 |
| Klein | <= 6 Mio EUR | <= 12 Mio EUR | <= 50 |
| Mittel | <= 20 Mio EUR | <= 40 Mio EUR | <= 250 |
| Gross | > diese Grenzen | | |

(Bei 2 von 3 Kriterien erfuellt zwei aufeinanderfolgende Jahre.)

### Phase 2 — Veroeffentlichungs-Umfang

| Klasse | Pflichtbestandteile |
|---|---|
| Kleinst | Verkuerzte Bilanz, kein Anhang noetig (mit Anhang-Befreiung) |
| Klein | Verkuerzte Bilanz, verkuerzter Anhang; GuV-Befreiung |
| Mittel | Vollstaendige Bilanz, vollstaendige GuV, Anhang, Lagebericht |
| Gross | Wie Mittel plus zusaetzliche Angaben |

### Phase 3 — Frist und Uebermittlung

- Frist: 12 Monate nach Bilanzstichtag (§ 325 Abs. 1a HGB).
- Form: elektronische Uebermittlung an das Unternehmensregister ueber publikations-plattform.de (Anmeldung mit Nutzerkonto, Authentifizierung via DE-Mail bzw. ELSTER).
- Zertifikat: StB-Berechtigung oder Mandanten-Login; bei Mehrfach-Mandanten Sammelversand moeglich.

### Phase 4 — Ordnungsgeldverfahren bei Verspaetung

- Das BfJ leitet nach Fristablauf das Verfahren nach § 335 HGB ein und droht ein Ordnungsgeld an (Regelhoehe ab 2.500 EUR).
- Wird der Verpflichtung innerhalb der gesetzten sechswoechigen Nachfrist nicht entsprochen, setzt das BfJ das Ordnungsgeld fest und kann es mehrfach in steigender Hoehe festsetzen (bis 25.000 EUR pro Festsetzung).
- Fuer Kleinstkapitalgesellschaften gilt eine reduzierte Ordnungsgeld-Mindestschwelle (§ 335 Abs. 1a HGB).

### Phase 5 — Hinterlegung statt Veroeffentlichung

- Kleinste GmbH: Hinterlegung im Unternehmensregister statt Veroeffentlichung moeglich (§ 326 Abs. 2 HGB).
- Vorteil: Bilanz nicht oeffentlich einsehbar.
- Nachteil: Kosten gleich; nur Vertraulichkeits-Vorteil.

### Phase 6 — Dokumentation

- Veroeffentlichungs-Quittung in Mandantenakte.
- Frist-Wiedervorlage Folgejahr.

## Output

- Veroeffentlichter / hinterlegter Jahresabschluss im Unternehmensregister (fuer Geschaeftsjahre ab 01.01.2022) bzw. im Bundesanzeiger (fuer aeltere Geschaeftsjahre).
- Uebermittlungs-Quittung (Transferticket) als Nachweis in der Mandantenakte.
- Wiedervorlage Folgejahr im Fristenkalender.

## Strategie und Praxis-Tipps

- Die 12-Monats-Frist gemaess § 325 Abs. 1a HGB ist hart; verstreicht sie, leitet das BfJ ohne weitere Mahnung das Ordnungsgeldverfahren ein.
- Die Hinterlegungs-Option fuer Kleinstkapitalgesellschaften (§ 326 Abs. 2 HGB) ist haeufig attraktiv: Bilanz ist dann nur auf Antrag und gegen Gebuehr einsehbar — wesentlicher Vertraulichkeitsvorteil bei vergleichbaren Kosten.
- Bei mehreren offenen Vorperioden: nachholen vor Folgeperiode, da das BfJ Ordnungsgelder mehrfach festsetzen kann.
- Veroeffentlichungskosten variieren mit Umfang und Format; Richtwert pro Geschaeftsjahr 30-200 EUR — konkrete Gebuehren ueber den Tarif des Unternehmensregisters.
- StBVV-Honorar: Offenlegung als Sonderauftrag, in der Praxis ueblich als Pauschalvereinbarung gem. § 14 StBVV oder als Beratungsleistung gem. § 21 StBVV (Erstellung E-Bilanz und Offenlegung sind getrennte Leistungen).

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` — E-Bilanz.
- `stb-mandantenfragebogen-jahresabschluss` — Mandantenfragebogen.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 8b, 264a, 267, 267a, 325-329, 335.
- DiRUG (BGBl. I 2021, 3338).
- BfJ-Verfahrensanweisungen zum Ordnungsgeldverfahren.
- Unternehmensregister: www.unternehmensregister.de bzw. www.publikations-plattform.de.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-jahresabschluss-vorbereitung-stichtag`

**Fokus:** Jahresabschluss-Vorbereitung Stichtag. Anwendungsfall systematische JA-Vorbereitung Inventur Periodenabgrenzung Rückstellungen Anlagenspiegel. Methodik 8-Wochen-Vorlauf. Output JA-Vorbereitungs-Routine.

# Jahresabschluss-Vorbereitung zum Stichtag

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Jahresabschluss-Vorbereitung zum Stichtag` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Jahresabschluss erfordert systematische Vorbereitung 8-12 Wochen vor dem Bilanzstichtag und eine geordnete Abwicklung in den ersten vier Monaten danach. Inventur, Periodenabgrenzung, Rueckstellungen, Anlagenspiegel und Mandantenfragebogen muessen aufeinander abgestimmt sein. Die folgende Standardroutine setzt den Bilanzstichtag (i.d.R. 31.12.) als Anker; die Phasen koennen bei abweichendem Geschaeftsjahr entsprechend verschoben werden.

## Kaltstart-Rueckfragen

1. Welcher Bilanzstichtag?
2. Welche Rechtsform und Groessenklasse?
3. Liegt Pruefungspflicht vor (§ 316 HGB)?
4. Welche besonderen Vorgaenge im Jahr (Anlagenkauf/-verkauf, Gesellschafterwechsel, Kapitalmassnahmen, Umstrukturierung)?
5. Welche Sondersachverhalte mit Erlaeuterungsbedarf (vGA, schwebende Geschaefte, Werterhellung)?
6. Welche externen Fristen (Offenlegung Unternehmensregister 12 Monate, Steuererklaerungen, Bankreporting)?
7. Welche Mandantenkommunikations-Routine?
8. Welche StBVV-Honorarvereinbarung?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — Aufstellungspflicht.

**§ 264 Abs. 1 HGB** — Aufstellungsfrist 3-6 Monate.

**§ 325 HGB** — Veroeffentlichung Bundesanzeiger 12 Monate.

**§ 316 HGB** — Pruefungspflicht groessere Kapitalgesellschaften.

**§ 240 HGB** — Inventarpflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 35 StBVV** — Honorar Jahresabschluss.

## Workflow

### Phase 1 — 8 Wochen vor Stichtag (Anker Stichtag: T-8 Wochen)

- Mandantenfragebogen (siehe `stb-mandantenfragebogen-jahresabschluss`) versenden mit Rueckfrist 4 Wochen.
- Inventur-Termin und -Anweisung mit Mandant schriftlich abstimmen (insbesondere bei Stichtagsinventur am 31.12.).
- Bei Pruefungspflicht (§ 316 HGB): Vor-Pruefungs-Vorbereitung mit dem Wirtschaftspruefer; Pruefungsplanung abstimmen.
- Hinweis an Mandant zu Investitionen, IAB § 7g EStG, Sonder-AfA-Optionen vor Stichtag.

### Phase 2 — Stichtag und Inventur (Bilanzstichtag)

- Inventur vor Ort begleiten oder Beobachterrolle bei groesseren Mandanten; bei kleineren Mandanten Stichprobenbegleitung.
- Inventurprotokolle aufnehmen (Mengen, Bewertungshinweise, Pruefdatum, Bearbeiter).
- Bestandsabweichungen unmittelbar klaeren (Cut-off-Listen Lieferungen / Wareneingang).

### Phase 3 — 1. Quartal nach Stichtag (Wochen 1-4): Bestandskonten abstimmen

- Dezember-Buchungen finalisieren (letzte Belege, Bank-Cut-off, Lohn-Dezember inkl. Boni).
- Bank-Saldenabstimmung Endbestand; Saldenbestaetigungen einholen.
- OPOS-Pflege (Debitoren / Kreditoren); zweifelhafte Forderungen markieren.

### Phase 4 — 1. Quartal nach Stichtag (Wochen 5-10): Abgrenzungen, Rueckstellungen, Anlagen

- Periodenabgrenzung (RAP) gemaess `stb-jahresabschluss-abgrenzungen-rap-rai`.
- Rueckstellungen quantifizieren gemaess `stb-jahresabschluss-rueckstellungen-bewertung`.
- Anlagenspiegel und AfA gemaess `stb-jahresabschluss-anlagenverzeichnis-afa`.
- Saldenabstimmung Forderungen, Verbindlichkeiten, Banken; Werterhellungstatsachen pruefen.

### Phase 5 — 2. Quartal nach Stichtag (Wochen 10-14): Entwurf und Mandantengespraech

- Jahresabschluss-Entwurf (Bilanz, GuV, Anhang); bei Pflichtgesellschaft Lagebericht.
- Wahlrechtsausuebung dokumentieren (Mandantenwahl protokolliert).
- Mandantengespraech zum Entwurf (Brueckenschlag zu `stb-jahresgespraech-mandant-bwa-basis`).

### Phase 6 — 2.-3. Quartal nach Stichtag (Wochen 14-26): Freigabe, Uebermittlung, Offenlegung

- Mandanten-Freigabe schriftlich (Aufstellungserklaerung).
- E-Bilanz-Uebermittlung an FA gemaess `stb-jahresabschluss-elektronische-uebermittlung-ebilanz`.
- Offenlegung im Unternehmensregister (§ 325 HGB) innerhalb 12 Monaten nach Stichtag gemaess `stb-jahresabschluss-veroeffentlichung-bundesanzeiger`.

## Output

- Aufgestellter Jahresabschluss.
- E-Bilanz uebermittelt.
- Bundesanzeiger-Veroeffentlichung.

## Strategie und Praxis-Tipps

- 8-12 Wochen Vorlauf sind Standard.
- Bei Pruefungspflicht: zusaetzliche 4-6 Wochen fuer WP.
- Inventur-Beobachtung beim Mandanten ist wertvoll fuer Bewertung.
- Mandantenfragebogen ist Effizienz-Hebel.
- StBVV § 35: Honorar nach Gegenstandswert; ggf. Pauschal mit Mandant.

## Querverweise

- `stb-mandantenfragebogen-jahresabschluss` — Fragebogen.
- `stb-jahresabschluss-warenbestand-inventur` — Inventur.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandsabstimmung.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — AfA.
- `stb-jahresabschluss-veroeffentlichung-bundesanzeiger` — Bundesanzeiger.
- `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` — E-Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 242, 252, 264, 316, 325.
- StBVV § 35.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-jahresabschluss-warenbestand-inventur`

**Fokus:** Warenbestand und Inventur für Jahresabschluss. Anwendungsfall jaehrliche Inventur Aufnahme Warenbestand permanente Inventur Stichprobeninventur Bewertung. Methodik § 240 HGB GoBD. Output Inventur-Protokoll Warenbestand-Wert.

# Warenbestand und Inventur

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Warenbestand und Inventur` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

§ 240 HGB verpflichtet zur jaehrlichen Inventur (koerperliche Bestandsaufnahme) zum Bilanzstichtag. Bei Handel und Industrie ist der Warenbestand wesentliche Bilanzposition. Vereinfachungen moeglich: permanente Inventur, Stichprobeninventur, vor- oder nachverlegte Inventur. Bewertung zum Niederstwertprinzip (§ 253 HGB).

## Kaltstart-Rueckfragen

1. Welche Branche (Handel, Industrie, Dienstleistung)?
2. Welche Inventur-Form ist vorgesehen?
3. Welcher Stichtag fuer Inventur (Bilanzstichtag oder davor/danach)?
4. Welche Warengruppen (Roh-, Hilfs-, Betriebsstoffe, Halbfertige, Fertige Waren)?
5. Welche Bewertungsmethode (FIFO, LIFO, gleitender Mittelpreis)?
6. Welche Verbrauchsfolgeverfahren (Steuerbilanz nur LIFO unter Voraussetzungen)?
7. Welche Lagerverwaltung-Software?
8. Welche Stichprobenpruefung wird durchgefuehrt?

## Rechtlicher Rahmen

### Primaernormen

**§ 240 HGB** — Inventarpflicht jaehrlich.

**§ 241 HGB** — Inventur-Vereinfachungen.

**§ 252 Abs. 1 Nr. 3 HGB** — Einzelbewertungsgrundsatz.

**§ 253 HGB** — Niederstwertprinzip.

**§ 256 HGB** — Bewertungsmethoden.

**§ 6 EStG** — Steuerliche Bewertung.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 zu GoBD (auch Inventur betreffend).
- IDW PS 480.

## Workflow

### Phase 1 — Inventur-Form waehlen

| Form | Anwendung |
|---|---|
| Stichtagsinventur (Standard) | Koerperliche Aufnahme zum Bilanzstichtag |
| Permanente Inventur | Mit Lagerbuchfuehrung; jaehrliche Stichprobe |
| Stichprobeninventur | Mathematisch-statistisch (Stichprobenpruefverfahren) |
| Vorverlegte Inventur | Bis 3 Monate vor Stichtag mit Fortschreibung |
| Nachverlegte Inventur | Bis 2 Monate nach Stichtag mit Rueckrechnung |

### Phase 2 — Inventur durchfuehren

- Anweisung an Inventur-Personal.
- Aufnahme von Mengen und Beschreibungen je Position.
- Sammelliste oder Inventur-Software.
- Inventur-Protokoll mit Datum, Bearbeiter, Werten.

### Phase 3 — Bewertung

- Mengen x Preis (Anschaffungs-/Herstellungskosten oder niedrigerer Marktwert).
- Bei Mehrfachbeschaffung: Verbrauchsfolge (FIFO, LIFO, gleitender Mittelpreis).
- Niederstwertprinzip: bei dauerhafter Wertminderung Abschreibung.

### Phase 4 — Bewertungsmethoden

| Methode | Charakter | Steuerbilanz |
|---|---|---|
| FIFO (First in, first out) | Aelteste Bestaende zuerst | Steuerbilanz nicht zwingend zulaessig |
| LIFO (Last in, first out) | Neueste Bestaende zuerst | Steuerbilanz unter § 6 Abs. 1 Nr. 2a EStG |
| Gleitender Mittelpreis | Durchschnitt | Steuerbilanz akzeptiert |
| Einzelbewertung | Konkret pro Stueck | Massgeblich |

### Phase 5 — Niederstwertprinzip

- Bei voraussichtlich dauerhaft niedrigerem Wert: Abschreibung.
- Bei voruebergehender Wertminderung: Wahlrecht.
- Steuerlich: § 6 Abs. 1 Nr. 2 EStG.

### Phase 6 — Dokumentation

- Inventur-Protokolle aufbewahren (10 Jahre, § 257 HGB).
- Wertberechnung dokumentieren.
- Bei Pruefungspflicht WP-Inventur-Begleitung.

## Output

- Inventur-Protokoll mit Warenbestand.
- Bewertung mit Methode dokumentiert.
- Bilanzposten "Vorraete".

## Strategie und Praxis-Tipps

- Inventur ist Pflicht — nicht abgekuerzte Pruefung.
- Bei Handel und Industrie Inventur-Tag oft am 31. Dezember (Geschaeftsruhe).
- LIFO steuerlich nur unter Voraussetzungen — aber bei Inflation Steuerstundungs-Vorteil.
- Niederstwertprinzip ist Vorsichtsprinzip — bei zweifelhaften Bestaenden abschreiben.
- Bei Pruefungspflicht: WP beobachtet Inventur (Stichproben).

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandsabstimmung.
- `stb-jahresabschluss-kassenfuehrung-gobd-pflichten` — GoBD.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 241, 252, 253, 256, 257.
- EStG § 6.
- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
