---
name: due-diligence-legal
description: "Legal Due Diligence für M&A-Transaktionen: Prüft Corporate, Vertragswerk, HR, IP, Litigation und Compliance im Datenraum. Normen: §§ 311 Abs. 2 und 444 BGB sowie GmbHG, AktG, einschlaegige Sondergesetze. Prüfraster: Risk-Rating (hoch/mittel/niedrig), Red Flags, Vertragsmapping für SPA-Representat..."
---

# Legal Due Diligence

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — klaere vor Beginn der LDD

1. Buy-Side oder Sell-Side DD? (Kaeufer analysiert oder Verkaefer bereitet auf)
2. Full-Scope oder Limited-Scope (Focus Areas)?
3. Zeitrahmen: Wie viele Tage bis zum DD-Report-Deadline?
4. Welche Workstreams sind relevant: Corporate, Verträge, HR, IP/IT, Litigation, Compliance, Real Estate?
5. Gibt es bekannte Deal-Breaker-Themen aus dem Process Letter oder ersten Gespraechen?
6. W&I-Versicherung geplant? (Underwriter stellt eigene DD-Anforderungen)
7. Sind Datenschutz/DSGVO und Exportkontrolle eigene Workstreams?

## Zentrale Anspruchsgrundlagen & Normen

- **§§ 311 II, 241 II BGB** — vorvertragliche Aufklaerungspflichten; Haftung für falsche/unterlassene Information
- **§ 444 BGB** — Arglist schliesst Haftungsfreizeichnung aus; kein Ruckgriff auf Beschraenkungen
- **§ 123 BGB** — Anfechtung wegen arglistiger Taeuschung; 1 Jahr Frist (§ 124 BGB)
- **§ 453 BGB** — Anteilskauf; Maengelhaftung bei Garanieverletzungen
- **§ 15 IV GmbHG** — Vinkulierung von GmbH-Anteilen; Zustimmungserfordernisse bei Abtretung
- **§ 68 II AktG** — Vinkulierung von Namensaktien
- **§ 179a AktG** — Zustimmung HV bei Asset Deal (gesamtes Gesellschaftsvermoegen)
- **§§ 35 ff. GWB** — Fusionskontrolle; anmeldepflichtige Zusammenschluesse
- **Art. 4 DSGVO i.V.m. Art. 28 DSGVO** — Datenschutz im Datenraum und bei Zielgesellschaft

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## LDD-Workstreams — Prüfungsmatrix

| Workstream | Kerndokumente | Hauptrisiken | Vertragsmechanismus |
|---|---|---|---|
| Corporate | Satzung, Handelsregister, Gesellschaftervertraege, Organbeschluesse | Minderheitsrechte, Change-of-Control, Vinkulierung | Corporate Title Warranty, Zustimmungsvorbehalt |
| Verträge | Wesentliche Verträge, Material Contracts, Aufhebungsvereinbarungen | CoC-Klauseln, Kuendigungsrechte, Exklusivitaet | Specific Reps, Indemnity |
| HR/Arbeitsrecht | Arbeitsvertraege, Betriebsvereinbarungen, Pensionszusagen | § 613a BGB, Betriebsrat, Change-of-Control | HR Warranty, Pension Indemnity |
| IP/IT | Marken, Patente, Lizenzen, Domain-Namen, Quellcode | Lizenzkuendigungen, Open-Source-Pflichten, IT-Sicherheit | IP Title Warranty, Source Code Escrow |
| Litigation | Laufende Rechtsstreitigkeiten, Schiedsverfahren, Behördenverfahren | Haftungsvolumen, Rueckstellungsluecken | Litigation Indemnity, Disclosure Schedule |
| Compliance | GwG, Kartellrecht, Exportkontrolle, Korruption (FCPA/UKBA) | Bussgeld, Lizenzentzug, Reputationsrisiko | Compliance Warranty, Anti-Corruption Rep |
| Real Estate | Grundbuchauszuege, Mietvertraege, Altlasten | Umwelthaftung, Sonderkuendigungsrechte | Real Estate Warranty, Environmental Indemnity |
| Tax | Steuererklaerungen, Betriebspruefungsbescheide, Verrechnungspreise | Steuernachforderungen | Tax Indemnity (Separate-Strang), Tax Warranty |

## Red-Flag-Bewertungsmatrix

| Schweregrad | Definition | Konsequenz |
|---|---|---|
| Red Flag / Deal Breaker | Existenzgefaehrdend, nicht heilbar, Strukturaenderung noetig | Separate Empfehlung; ggf. Deal-Abbruch |
| High Risk | Erheblich, heilbar oder abzudecken; ohne Mechanismus Deal-Wert-Minderung | Spezifische Indemnity oder Kaufpreisabschlag |
| Medium Risk | Bedeutsam, vertretbar durch Warranty; kein unmittelbarer Schaden | Disclosure Schedule; General Warranty |
| Low Risk | Marginal; marktkonform | Offenlegung im Disclosure Letter; keine gesonderte Klausel |

## Schritt-für-Schritt-Workflow

1. **DD-Scope festlegen** — Workstreams, Tiefen-Level (Full/Limited), Ressourcen, Zeitplan
2. **IRL (Information Request List) erstellen** — gegliedert nach Workstreams; priorisiert nach Wesentlichkeit
3. **Datenraum strukturieren** — Index-Mapping, Gap-Analyse, fehlende Dokumente als TODO markieren
4. **Workstream-Prüfung** — jedes Dokument mit Datum, Fundstelle (Datenraum-ID) und Risikoklasse erfassen
5. **Red Flag Memo intern** — laufende Zusammenfassung für Deal-Team; taeglich aktualisieren
6. **Rueckfragen (Q&A)** — schriftliche Fragen an Verkaefer über Q&A-Funktion; Antworten dokumentieren
7. **DD-Report finalisieren** — Executive Summary, Workstream-Abschnitte, Risikomatrix, Empfehlungen
8. **SPA-Mapping** — DD-Findings mit konkreten Vertragsklauseln verknuepfen (Reps, Indemnities, Closing Conditions)
9. **W&I-Underwriter-Briefing** — DD-Report und Red Flag Memo an Versicherer; No-Claims Declaration

## Output-Template DD-Red-Flag-Memo

**Adressat:** Deal-Team intern / Managing Partner — Tonfall sachlich, risikopriorisiert

```
LEGAL DUE DILIGENCE — RED FLAG MEMO (INTERN, VERTRAULICH)
Transaktion: [DEAL-NAME]
Zielgesellschaft: [NAME, Sitz]
Datum: [DATUM]
Version: [Nr.]
Bearbeiter: [NAMEN]

1. EXECUTIVE SUMMARY
 Gesamtrisikoeinschaetzung: [Hoch / Mittel / Niedrig]
 Deal-Breaker identifiziert: [Ja/Nein — wenn Ja: Beschreibung]
 Empfehlung: [Weiterverhandeln / Kaufpreisanpassung erforderlich / Abbruch pruefen]

2. RED FLAGS (nach Schweregrad)
 | Nr. | Workstream | Befund | Schweregrad | Vertragsmechanismus |
 |-----|-----------|--------|-------------|---------------------|
 | 1 | [Workstream] | [Befund] | [Red Flag] | [Indemnity / KP-Abschlag] |

3. HIGH-RISK-FINDINGS
 [Strukturierter Ueberblick]

4. OFFENE PUNKTE / Q&A-AUSSTEHEND
 | Nr. | Frage | An Verkaefer seit | Frist |
 |-----|-------|-------------------|-------|
 | 1 | [Frage] | [Datum] | [Datum] |

5. EMPFEHLUNGEN SPA-ADJUSTMENTS
 [Konkrete Klausel-Anpassungen, Indemnity-Empfehlungen]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Output-Template DD-Report Struktur

```
LEGAL DUE DILIGENCE REPORT
Transaktion: [DEAL-NAME]
Zielgesellschaft: [NAME]
Datum: [DATUM]

I. EXECUTIVE SUMMARY
II. SCOPE AND METHODOLOGY
III. CORPORATE / ANTEILSSTRUKTUR
IV. WESENTLICHE VERTRAEGE
V. HR UND ARBEITSRECHT
VI. IP UND IT
VII. LITIGATION UND BESCHWERDEN
VIII.COMPLIANCE UND REGULIERUNG
IX. IMMOBILIEN UND UMWELT
X. STEUERN (Ueberblick; Details im Tax DD Report)
XI. RISIKOMATRIX (konsolidiert)
XII. SPA-EMPFEHLUNGEN
ANLAGEN: Dokumentenindex, Q&A-Log, Organigramm
```

## Rote Schwellen

- DD-Report ohne Risikomatrix und SPA-Mapping-Empfehlung — Red Flags ohne Konsequenz
- Q&A-Antworten nicht dokumentiert — Beweisrisiko bei Arglist-Vorwurf (§ 444 BGB)
- Litigation-Risiken nicht mit Rueckstellungen abgeglichen — Wertluecke im Kaufpreis
- § 613a-Risiken (Betriebsuebergang Asset Deal) nicht identifiziert — unerwarteter Arbeitnehmer-Uebergang
- FDI/Aussenwirtschaftsrechtliche Genehmigungspflicht uebersehen — Closing-Risiko, Nichtigkeit

## Vertiefung: Besondere Risikobereiche

### Change-of-Control-Klauseln
Wesentliche Verträge (Kundenv., Lieferantenv., Bankkredite, Mietvertraege, Lizenzen) enthalten haeufig CoC-Kuendigungsrechte. Im LDD: systematisches Mapping aller wesentlichen Verträge mit CoC-Klauseln; Verhandlung von Consents vor Signing.

### Kartellrecht (§§ 35 ff. GWB; FKVO)
Ab Umsatzschwellen: Anmeldepflicht Bundeskartellamt / EU-Kommission. Vollzugsverbot (Gun Jumping) bis zur Freigabe strikt einhalten — Bussgeld bis 10 % des Weltumsatzes.

### DSGVO-Compliance im Datenraum
Der Datenraum darf keine personenbezogenen Daten enthalten, die nicht für DD-Zwecke erforderlich sind. Anonymisierung oder Pseudonymisierung von HR-Daten vorsehen.

## Quellen

- § 311 II BGB: https://www.gesetze-im-internet.de/bgb/__311.html
- § 444 BGB: https://www.gesetze-im-internet.de/bgb/__444.html
- § 453 BGB: https://www.gesetze-im-internet.de/bgb/__453.html
- § 15 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 179a AktG: https://www.gesetze-im-internet.de/aktg/__179a.html
- §§ 35 ff. GWB: https://www.gesetze-im-internet.de/gwb/__35.html
- AWG § 4-6 (FDI-Prüfung); AWV §§ 55 ff. (sektorale Investitionspruefung): https://www.gesetze-im-internet.de/awv_2013/
- EU-FDI-Screening-VO (EU) 2019/452: https://eur-lex.europa.eu/eli/reg/2019/452
- EU Foreign Subsidies Regulation (FSR) (VO (EU) 2022/2560; in Kraft 12.01.2023; anwendbar ab 12.07.2023; Notifizierungspflicht ab 12.10.2023). M&A-Schwelle: mindestens eine Partei (oder Zielgesellschaft) über EUR 500 Mio. EU-Umsatz UND erworbene Seite hat über EUR 50 Mio. drittstaatliche finanzielle Zuwendungen in letzten drei Jahren erhalten. Bei Vergabeverfahren: über EUR 250 Mio. Auftragswert und über EUR 4 Mio. Drittstaaten-Zuwendungen. VO-Text: https://eur-lex.europa.eu/eli/reg/2022/2560 — Kommission Guidance: https://competition-policy.ec.europa.eu/foreign-subsidies-regulation_en
- MoPeG (BGBl. I 2021, 3436; in Kraft 01.01.2024) — Auswirkungen auf DD bei Personengesellschaften (eGbR, OHG, KG): https://www.gesetze-im-internet.de/bgb/__705.html
- DiRUG/DiREG: Online-Beurkundung Kapitalmassnahmen seit 01.08.2023 — DD-Implikation für Closing-Mechanik
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
