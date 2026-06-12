---
name: dsfa-fuer-internationale-datentransfers
description: "DSFA bei internationalen Datentransfers nach Kapitel V DSGVO: Integration der Transfer Impact Assessment (TIA) in die DSFA, Prüfung Angemessenheit SCC BCR Ausnahmen Art. 49. Output: erweiterte DSFA-Sektion für Drittlandbezug."
---

# DSFA bei internationalen Datentransfers

## Wann dieses Modul hilft

- Bei Auftragsverarbeiter mit Sitz oder Unterauftrag im Drittland
- Bei eigener Niederlassung im Drittland
- Bei US-Cloud-Diensten (auch bei EU-Hosting wegen Zugriffsmoeglichkeit US-Behörden)
- Bei Konzernintern-Transfers über Landesgrenzen
- Bei KI-Anbietern mit Training oder Inferenz im Drittland
- Bei nationalen Sicherheitsgesetzen des Drittlands (z. B. CLOUD Act, FISA 702, China DSL)

## Rechtlicher Rahmen

- Art. 44 DSGVO Grundsatz: jeder Transfer muss eine Rechtsgrundlage in Kapitel V haben.
- Art. 45 DSGVO Angemessenheitsbeschluss der Kommission.
- Art. 46 DSGVO geeignete Garantien (SCC, BCR, Verhaltensregeln, Zertifizierungen).
- Art. 47 DSGVO Binding Corporate Rules.
- Art. 49 DSGVO Ausnahmen für besondere Faelle (Einwilligung, Vertragserfuellung, öffentliche Interessen).
- Schrems II — EuGH Urt. v. 16.07.2020, C-311/18 — Transfer-Prüfungspflicht; TIA erforderlich. (Aktenzeichen verifiziert; sonstige Folgeentscheidungen verifizierungspflichtig.)
- EDSA Leitlinien 04/2022 zu personenbezogenen Datentransfers (Nutzer sollte Aktualitaet prüfen).
- Angemessenheitsbeschluss EU-US Data Privacy Framework (DPF) 10.07.2023, Implementing Decision (EU) 2023/1795.
- SCC Implementing Decision (EU) 2021/914 vom 04.06.2021 mit Modulen 1 bis 4.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welche Daten gehen wohin, an wen, in welcher Form, wie oft, in welchem Umfang?
2. **Verhältnismäßigkeitspruefung.** Ist der Drittlandtransfer für den Zweck erforderlich, oder gaebe es EU-Alternativen?
3. **Risikoanalyse.**
 - Drittlandrecht: Zugriffsbefugnisse von Behörden, Rechtsbehelfe Betroffener.
 - Anbieter-Risiko: Branche, Datentyp, Subunternehmer.
 - Daten-Risiko: Sensitivitaet, Aggregation, Identifizierbarkeit.
4. **Maßnahmen.**
 - Rechtsgrundlage: Angemessenheitsbeschluss, SCC mit passendem Modul, BCR, Ausnahme Art. 49.
 - Ergaenzende Maßnahmen nach EDSA Empfehlungen 01/2020 (verifizierungspflichtig): technisch (Verschluesselung, Schlüsselhoheit), vertraglich (Information über Behördenanfragen), organisatorisch (Audit, Schulung).
5. **Restrisiko.** Prüfung ob die ergaenzenden Maßnahmen das Schutzniveau auf das EU-Niveau anheben oder ob das Restrisiko hoch bleibt.
6. **Konsultation / Genehmigung.** DSB-Anhörung; bei verbleibendem hohem Restrisiko Art. 36 DSGVO Vorabkonsultation; bei US-Anbietern Prüfung DPF-Zertifizierung.

## Mustertext / Template (Transfer-Sektion einer DSFA)

```
TRANSFER IMPACT ASSESSMENT [DATUM]
(Erweiterung der DSFA Sektion 4 / Anlage zur DSFA)

Verantwortlicher: [NAME]
Empfaenger im Drittland: [Name, Land, Konzernverbund]
Sub-AVs: [Liste mit Land]

1. Transferbeschreibung
- Datenkategorien: [...]
- Datenmenge: [...]
- Betroffenenkreise: [...]
- Uebermittlungsweg: [API / SFTP / DB-Replikation]
- Verschluesselung: [Transport / Ruhe / Ende-zu-Ende]
- Schluesselhoheit: [EU / Drittland / Hybrid]

2. Rechtsgrundlage des Transfers
[ ] Angemessenheitsbeschluss Art. 45 DSGVO: [Land, Beschlussdatum]
[ ] SCC Modul: [1 C-C / 2 C-P / 3 P-P / 4 P-C], Datum [...]
[ ] BCR: [Genehmigung, Datum]
[ ] Ausnahme Art. 49 Abs. 1 lit. [a/b/c/...] mit Begruendung
[ ] DPF-Zertifizierung Empfaenger: ja / nein, Stand [Datum]

3. Drittlandrechtspruefung
- Zugriffsbefugnisse Behörden: [CLOUD Act / FISA 702 / Section 702 / China DSL / Russland TK-Gesetz]
- Rechtsbehelfe Betroffener: [vorhanden / nicht aequivalent]
- Aufsichtsstruktur: [unabhaengig / nicht unabhaengig]
- Pruefung Schrems-II-Standard erfuellt: ja / nein
- Quelle: [EDSA-Länderbericht, Anbietererklaerung, Stand]

4. Ergaenzende Massnahmen
- Technisch:
 [ ] Ende-zu-Ende-Verschluesselung mit EU-Schluesselhoheit
 [ ] Pseudonymisierung vor Transfer
 [ ] Tokenisierung
 [ ] Split-Processing (sensitive Felder in EU)
- Vertraglich:
 [ ] Transparenz-Pflicht ueber Behördenanfragen
 [ ] Audit-Recht
 [ ] Loeschpflicht nach Vertragsende
- Organisatorisch:
 [ ] Anbieterschulung Datenschutz
 [ ] Notfallplan bei Behördenzugriff

5. Restrisikobewertung
[GRUEN / GELB / ORANGE / ROT]
Begruendung: [...]

6. Entscheidung
[ ] Transfer zulaessig — Massnahmen umgesetzt
[ ] Transfer zulaessig mit Auflagen
[ ] Vorabkonsultation Art. 36 DSGVO erforderlich
[ ] Transfer nicht zulaessig — Alternative pruefen

7. Ueberwachung
- Naechste Re-Pruefung: [Datum]
- Trigger: [Schrems-III-Folgeurteil / DPF-Status-Aenderung / Anbieterwechsel]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Typische Fehler

- TIA wird separat vom DSFA-Prozess gefuehrt — Schnittstellen gehen verloren.
- US-Cloud mit EU-Hosting wird als reiner EU-Verarbeitung behandelt — Zugriffsbefugnis US-Behörden uebersehen.
- SCC-Modul falsch gewaehlt (C-P statt C-C oder umgekehrt).
- Ergaenzende Maßnahmen werden nur rechtlich, nicht technisch dokumentiert.
- Ausnahme Art. 49 wird als Daueroption verwendet, obwohl sie nur für Einzelfaelle gedacht ist.
- Re-Prüfung nach Schrems-Folgeurteil unterbleibt.
- DPF-Zertifizierung des Anbieters wird nicht jaehrlich nachgeprueft.

## Quellen Stand 06/2026

- Art. 44 bis 49 DSGVO
- EuGH Urt. v. 16.07.2020, C-311/18 (Schrems II)
- Durchfuehrungsbeschluss (EU) 2021/914 vom 04.06.2021 (SCC)
- Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023 (DPF)
- EDSA Leitlinien 04/2022 (Aktualitaet prüfen)
- EDSA Empfehlungen 01/2020 zu ergaenzenden Maßnahmen (Aktualitaet prüfen)
- Rechtsprechung: weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
