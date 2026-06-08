---
name: tia-laender-bewertung-china-india-brazil-uk
description: "TIA-Länderbewertung jenseits der USA: Vereinigtes Koenigreich (Angemessenheit), China (PIPL, Sicherheitsgesetze), Indien (DPDPA), Brasilien (LGPD). Pruefraster für Drittlandsrecht Behördenzugriff Praxis und Empfehlung Transferinstrument für Schritt 3 der EDPB-Roadmap."
---

# TIA-Länderbewertung: UK, China, Indien, Brasilien

## Zweck

Dieser Skill liefert die operative Drittlandbewertung für vier zentrale Nicht-USA-Ziellaender: das Vereinigte Koenigreich (UK), die Volksrepublik China, Indien und Brasilien. Er ergaenzt die US-Fachmodule um die haeufigsten weiteren Cluster und liefert Pruefraster und Empfehlung für das Transferinstrument.

## Wann dieses Modul hilft

- Konzernweite TIA-Updates mit nicht-amerikanischen Tochtergesellschaften.
- Outsourcing nach Indien (BPO, IT, Software-Entwicklung).
- Geschaeftspartner in China (Mandanten, Joint Ventures, Lieferanten).
- Vertriebs- oder Hosting-Strukturen in Brasilien (LGPD-Region).
- UK-bezogene Mandate nach Brexit; Pruefung des Angemessenheitsbeschlusses.

## Rechtlicher Rahmen je Land

### Vereinigtes Koenigreich (UK)

- **Angemessenheitsbeschluss EU - UK Adequacy Decision** vom **28.06.2021** (Beschluss (EU) 2021/1772 für die DSGVO; Beschluss (EU) 2021/1773 für die JI-Richtlinie).
- Befristet zunaechst bis 27.06.2025; mit Verordnung der Kommission im Sommer 2025 verlaengert (Termin und Aktenzeichen am amtlichen Beschluss verifizieren).
- UK GDPR (Data Protection Act 2018 in geltender Fassung) als nationale Spiegelregelung.
- **Investigatory Powers Act 2016** als kritischer Behördenrahmen; EuGH C-623/17 (Privacy International) hat britische Bulk-Befugnisse vor Brexit beanstandet.
- **Data Use and Access Act 2025** (in UK verabschiedet) – pruefen, ob die Reform am Angemessenheitsbeschluss ruettelt.

**Empfehlung:** Transfer ueber Art. 45 DSGVO grundsaetzlich moeglich; TIA bleibt empfohlen wegen Investigatory Powers Act und Reformdiskussion; Fallback-Klausel auf SCC einbauen.

### Volksrepublik China

- **Personal Information Protection Law (PIPL)**, in Kraft seit 01.11.2021.
- **Data Security Law (DSL)**, in Kraft seit 01.09.2021.
- **Cybersecurity Law (CSL)**, in Kraft seit 01.06.2017.
- **National Intelligence Law (NIL)** vom 27.06.2017: Pflicht zur Kooperation der Buerger und Unternehmen mit Geheimdiensten (Art. 7 NIL) – kritisch für TIA.
- **State Secrets Law** und Anti-Spionage-Gesetz (2023-Novelle) – Zugriff der Behörden ohne effektive Rechtsschutzmoeglichkeit.
- Kein Angemessenheitsbeschluss.

**Empfehlung:** Art. 46 DSGVO (SCC) plus umfassende TIA; technische Massnahmen (starke Verschluesselung mit Key in EU/EWR) regelmaessig erforderlich; Use Case 6/7 EDPB Annex 2 kommt in Betracht; bei Berufsgeheimnistraegern (Anwalt/Arzt) besondere Zurueckhaltung; Art. 49 DSGVO nur für eng begrenzte Einzelfaelle.

### Indien

- **Digital Personal Data Protection Act 2023 (DPDPA)**, verabschiedet 11.08.2023; **Inkrafttreten gestaffelt**; Durchfuehrungsregeln (Rules) 2025 abwarten und am amtlichen Stand pruefen.
- Vor DPDPA: Information Technology Act 2000 mit Reasonable Security Practices Rules (SPDI 2011) als Datenschutzrahmen.
- Behördenzugriff: **Telegraph Act 1885 (§ 5)** und IT-Act § 69 (Interception); Vorbehalt vorrangiger nationaler Sicherheit.
- Kein Angemessenheitsbeschluss.

**Empfehlung:** SCC + TIA; Pruefung des DPDPA-Inkraftsetzungsstands; Schutzlevel des indischen Anbieters genau dokumentieren; Verschluesselung empfehlenswert; vertragliche Behörden-Anfrage-Berichtspflicht.

### Brasilien

- **Lei Geral de Protecao de Dados (LGPD)**, Lei nº 13.709/2018, in Kraft seit 18.09.2020 (Sanktionsregime seit 01.08.2021).
- Aufsicht: **Autoridade Nacional de Protecao de Dados (ANPD)**.
- Behördenzugriff: **Lei Geral de Telecomunicacoes** und Anti-Terror-Gesetz 13.260/2016; Verfahren ueber Justizbehoerden, was im Vergleich zu USA/China engmaschiger ist.
- Kein Angemessenheitsbeschluss; Diskussion ueber moegliche Kommissionsbewertung.

**Empfehlung:** SCC + TIA; Schutzniveau in der Praxis vergleichsweise gut; Restrisiko durch Anti-Terror-Befugnisse dokumentieren.

## Ablauf / Checkliste je Land

1. Land identifizieren.
2. Existenz und Status eines Angemessenheitsbeschlusses pruefen.
3. Bei Art. 45-Beschluss: Coverage- und Befristung pruefen (UK: Reformdiskussion).
4. Bei Art. 46: SCC-Modul waehlen, TIA mit EEG-Pruefung.
5. Behördenzugriff im Drittland qualifiziert bewerten.
6. Praxis und Transparenzberichte des Importeurs einbeziehen.
7. Geeignete supplementary measures festlegen (siehe Skill `tia-zusaetzliche-schutzmassnahmen-encryption-pseudonymisierung`).
8. Restrisiko + Sign-off.

## Mustertext / Template

### Schritt-3-Block (Beispiel China)

> Der Importeur hat seinen Sitz in der Volksrepublik China. Massgebliche Rechtsgrundlagen für behoerdlichen Zugriff sind das Cybersecurity Law (CSL), das Data Security Law (DSL), das Personal Information Protection Law (PIPL), das National Intelligence Law (Art. 7 NIL) sowie das Anti-Spionage-Gesetz in der Fassung der Novelle 2023. Diese Regelungen begruenden weitreichende Zugriffs- und Kooperationspflichten ohne effektive gerichtliche Kontrolle aus Sicht der betroffenen Personen.
>
> Die EDPB-Garantien A-D der Empfehlung 02/2020 werden insbesondere zu Klarheit (A) und effektivem Rechtsschutz (D) nicht erfuellt. Ohne ergaenzende technische Schutzmassnahmen, die einen Klartextzugriff des Importeurs ausschliessen, ist der Transfer mit dem Schutzniveau der DSGVO nicht vereinbar.

### Tabelle Länderbewertung (Kurzform)

| Land | Angemessenheitsbeschluss | Transferinstrument | Hauptrisiko |
|---|---|---|---|
| UK | ja (2021/1772, verlaengert) | Art. 45 DSGVO | Investigatory Powers Act; Reform 2025 |
| China | nein | Art. 46 + TIA + technische Massnahmen | NIL Art. 7; CSL/DSL Datenherausgabepflichten |
| Indien | nein | Art. 46 + TIA | IT Act § 69; DPDPA-Status pruefen |
| Brasilien | nein | Art. 46 + TIA | Anti-Terror-Gesetz; sonst moderat |

## Typische Fehler

- UK pauschal als "wie EU" behandelt; Investigatory Powers Act ignoriert.
- China: PIPL als ausreichendes Schutzlevel angenommen, ohne NIL/State-Secrets-Risiko zu pruefen.
- Indien: DPDPA als "schon in Kraft" angesetzt, obwohl Rules-Phase noch unklar.
- Brasilien: SCC genuegt – ohne TIA dokumentiert.
- Nutzung von Art. 49 DSGVO als Daueroption.
- Konzerninterne Transfers in mehrere Drittlaender ohne differenzierte Bewertung.

## Querverweise

- `tia-edpb-roadmap-6-schritte-deutsch` für Methodik.
- `tia-zusaetzliche-schutzmassnahmen-encryption-pseudonymisierung` für Schritt 4.
- `tia-template-deutsch-vollvorlage` für Vollvorlage.
- `drittlandstransfer-pruefung` für Art. 44 ff. DSGVO Basis.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 44–49.
- Beschluss (EU) 2021/1772 vom 28.06.2021 (UK Adequacy DSGVO).
- Beschluss (EU) 2021/1773 vom 28.06.2021 (UK Adequacy JI-Richtlinie).
- UK Investigatory Powers Act 2016.
- EuGH C-623/17 vom 06.10.2020 (Privacy International).
- China: PIPL (01.11.2021), DSL (01.09.2021), CSL (01.06.2017), NIL (27.06.2017), Anti-Spionage-Gesetz-Novelle 2023.
- Indien: Digital Personal Data Protection Act 2023; IT Act 2000 § 69.
- Brasilien: LGPD Lei nº 13.709/2018; ANPD-Regelungen.
- EDPB Empfehlung 01/2020 Final 18.06.2021.
