---
name: corporate-kanzlei-datenraum-aufbau
description: "Virtuellen Datenraum strukturieren und befuellen für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. Anwendungsfall: Verkaeuferkanzlei richtet DR ein oder Kaeufer hat Zugang erhalten. Normen: DSGVO Art. 28 (Auftragsverarbeitung), GwG, MAR Insider-Abgrenzung. Prüfraster: Index nach Workstreams, Clean-Room-Zonen, Need-to-know-Bereiche, Nutzerrechte. Output DR-Index-Template, Checkliste fehlender Dokumente, Clean-Room-Protokoll. Abgrenzung: Gap-Analyse siehe datenraum-gap-clean-room; Q&A-Bearbeitung siehe qa-information-requests."
---

# Datenraum-Aufbau

## Triage — klaere vor Aufbau

1. Welche Plattform: Intralinks, Merrill Datasite, Ansarada, SharePoint, andere?
2. Art des Prozesses: Auktionsprozess (mehrere Bieter) oder bilateraler Deal?
3. Clean-Room-Anforderung (sensible Personal-/Kundendaten nur fuer ausgewaehlte Bieter)?
4. Jurisdiktionen: Welche Laender-spezifischen Compliance-Anforderungen bestehen?
5. Welche Workstreams sollen separat zugaenglich sein (Full Access vs. Restricted)?
6. W&I-Versicherung geplant? (Underwriter-Zugang zum Datenraum meist erforderlich)
7. Seller-Side: Welche Daten sollen noch nicht offenbart werden (z.B. vor LoI-Unterzeichnung)?

## Zentrale Normen & Anforderungen

- **Art. 28 DSGVO** — Auftragsverarbeitung bei Nutzung externer Datenraum-Plattform; AVV erforderlich
- **Art. 5, 25 DSGVO** — Datensparsamkeit; Privacy by Design; nur notwendige Daten im Datenraum
- **§ 3 I GwG** — wirtschaftlich Berechtigter; Informationen mueglich im Datenraum
- **Art. 18 MAR / § 13 WpHG** — Insider-Liste; Zugriff auf borsenrelevante Informationen protokollieren
- **§ 17 UWG** — Geschaeftsgeheimnis; Schutz vor unbefugter Offenlegung; Need-to-know

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Standard-Datenraum-Index: Corporate M&A

```
1. CORPORATE
   1.1 Handelsregisterauszuege und Satzung
   1.2 Gesellschaftervertraege / Shareholders Agreement
   1.3 Organigramm und Beteiligungsstruktur
   1.4 Gesellschafterbeschluesse (letzte 3 Jahre)
   1.5 Vollmachten und Zeichnungsberechtigungen
   1.6 Transparenzregister-Auszug

2. FINANZEN
   2.1 Jahresabschluesse (letzte 3 Jahre) — ggf. mit Pruefungsvermerk
   2.2 Quartalsberichte / Zwischenabschluesse
   2.3 Budget / Forecast laufendes Jahr
   2.4 Bankverbindlichkeiten, Kreditvertraege, Sicherheiten

3. WESENTLICHE VERTRAEGE
   3.1 Kundenstamm-Vertraege (Top 10)
   3.2 Lieferantenvertraege (wesentlich)
   3.3 JV-Vertraege, Lizenzvertraege
   3.4 Finanzierungsvertraege (Banken, Gesellschafter)
   3.5 Miet- und Pachtvertraege Immobilien

4. PERSONAL / HR [RESTRICTED — nur genehmigter Bieterkreis]
   4.1 Schluesselarbeitsvertraege (anonymisiert)
   4.2 Betriebsvereinbarungen und Tarifvertraege
   4.3 Pensionszusagen / bAV
   4.4 Organigramm mit Funktionen (keine Namen)

5. INTELLECTUAL PROPERTY / IT
   5.1 Marken, Patente, Schutzrechte
   5.2 Lizenzvertraege (in-bound/out-bound)
   5.3 Software-Vertraege; Open-Source-Inventar

6. LEGAL / LITIGATION
   6.1 Laufende Rechtsstreitigkeiten und Schiedsverfahren
   6.2 Behoerdenkorrespondenz (kartellrechtlich, regulatorisch)
   6.3 Versicherungsdeckung (D&O, Haftpflicht, Produkthaftung)

7. COMPLIANCE
   7.1 Compliance-Richtlinien
   7.2 GwG / AML-Pruefungsberichte
   7.3 Zertifikate (ISO, ESG)
   7.4 Behoerdenerlaubnisse und Lizenzen

8. STEUER
   8.1 Steuererklaerungen (letzte 3 Jahre)
   8.2 Betriebspruefungsberichte
   8.3 Steuerliche Bescheide (Vorauszahlungen, Stundungen)

9. IMMOBILIEN [falls relevant]
   9.1 Grundbuchauszuege
   9.2 Gutachten
   9.3 Umweltgutachten / Altlasten

10. SONSTIGES
    10.1 Versicherungsvertraege
    10.2 Presseberichte
    10.3 Sonstiges
```

## Clean-Room-Konzept

Ein Clean Room ist ein abgeschirmter Bereich im Datenraum fuer besonders sensible Informationen:
- **Typische Clean-Room-Inhalte:** Kundennamen und -konditionen, persoenliche HR-Daten (Gehaelter, Krankengeschichte), technische Betriebsgeheimnisse, laufende Angebote
- **Zugangsberechtigung:** nur von Verkaefer benanntes Clean-Team des Kaeufers; kein operatives Deck
- **Protokoll:** Zugangsliste im Datenraum; separate NDA-Erweiterung fuer Clean-Team-Mitglieder
- **Informationsfluss:** Ergebnisse nur als Zusammenfassung (nicht Originaldaten) an Verhandlungs-Team

## Schritt-fuer-Schritt-Workflow

1. **Datenraum-Struktur planen** — Index nach Workstreams; Zugriffsebenen; Clean-Room-Zonen
2. **Plattform aufsetzen** — AVV mit Plattformanbieter (DSGVO Art. 28); Sicherheitseinstellungen
3. **Zugaenge einrichten** — Benutzerkonten; NDA als Voraussetzung; Log-Protokollierung aktivieren
4. **Dokumente hochladen** — chronologisch; Version und Datum sichtbar; Dokument-ID vergeben
5. **IRL abarbeiten** — Gap-Analyse: Was ist noch offen? → Verkaeufer-seitig nachanfordern
6. **Vertraulichkeitszonen setzen** — HR und sensible Daten nur nach Clean-Team-NDA
7. **Q&A-Funktion aktivieren** — Fragen und Antworten protokollieren; Antwort-Owner definieren
8. **Update-Log fuehren** — welche Dokumente neu hochgeladen; Kaeufer informieren
9. **Closing-Sicherung** — nach Closing: Archiv erstellen; Zugaenge schliessen; CD-Backup an Kanzlei

## Output-Template Datenraum-Zugriffsmatrix

**Adressat:** Deal-PMO — Tonfall strukturiert, sicherheitsorientiert

```
DATENRAUM-ZUGRIFFSMATRIX
Transaktion: [DEAL-NAME]
Plattform: [NAME]
Stand: [DATUM]

| Kategorie | Vollzugang Bieter A | Vollzugang Bieter B | Clean-Team Only | Verkaefer Only |
|-----------|---------------------|---------------------|-----------------|----------------|
| Corporate | X | X | | |
| Finanzen | X | X | | |
| HR (anonymisiert) | X | X | | |
| HR (vollstaendig) | | | Clean Team | |
| Litigation | X | X | | |
| Steuer | X | X | | |
| Betriebs-Know-how | | | Clean Team | |

CLEAN-TEAM MITGLIEDER (Bieter A):
- [NAME, Funktion, E-Mail]
Zugangsdatum: [DATUM]
Separate NDA unterzeichnet: [Ja]
```

## Rote Schwellen

- Personenbezogene Daten ohne AVV (Art. 28 DSGVO) im Datenraum → DSGVO-Bussgeld bis 20 Mio. EUR
- Keine Protokollierung wer was heruntergeladen → kein Nachweis Kaeufer-Kenntnis bei Disclosure-Streit
- Sensible HR-Daten ohne Clean-Room-Schutz → Datenschutzverletzung; Betriebsrat-Mitbestimmung
- Dokumente ohne Datum und Version → Unklarheit ueber Stand der Information beim Signing
- Q&A-Antworten nicht archiviert → keine Beweisgrundlage bei spaeterem Warranty-Streit

## Quellen

- Art. 5, 25, 28 DSGVO; Art. 18 MAR; § 13 WpHG; § 17 UWG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 5
