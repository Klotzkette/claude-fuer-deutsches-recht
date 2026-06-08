---
name: tia-edpb-roadmap-6-schritte-deutsch
description: "EDPB-Empfehlung 01/2020 als operative Sechs-Schritte-Roadmap für das Transfer Impact Assessment. Schritt 1 Know your transfers; Schritt 2 Identify transfer tool; Schritt 3 Assess law and practice; Schritt 4 Adopt supplementary measures; Schritt 5 Procedural steps; Schritt 6 Re-evaluate. Mit Checklisten und Beispiel-Eintraegen."
---

# Sechs-Schritte-Roadmap für das Transfer Impact Assessment (EDPB 01/2020)

## Zweck

Dieser Skill arbeitet die Sechs-Schritte-Roadmap aus der EDPB-Empfehlung 01/2020 (Final Version 18.06.2021) als operative Pruefkette ab. Sie ist die Standard-Architektur für das deutsche TIA-Dokument.

## Wann dieses Modul hilft

- Erstes TIA-Dokument für einen konkreten Transfer.
- Aktualisierung eines bestehenden TIA nach Provider-Wechsel oder neuer Behördenpraxis.
- Vorlage gegenueber Aufsichtsbehoerde.
- Vorbereitung einer Vertragsverhandlung mit US-Anbieter.
- Schulung interner Reviewer.

## Rechtlicher Rahmen

- EuGH **C-311/18** Schrems II vom 16.07.2020.
- **EDPB Empfehlung 01/2020** "Recommendations on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data", Final 18.06.2021.
- **EDPB Empfehlung 02/2020** "Recommendations on the European Essential Guarantees for surveillance measures" vom 10.11.2020 – ergaenzt Schritt 3 (Assess law and practice).
- Art. 44 ff. DSGVO.

## Ablauf / Checkliste

### Schritt 1 – Know your transfers

Ziel: alle Transfers erfassen.

Pruefen:

- Welche Daten werden uebermittelt? Direkter Export, Remote Access, Onward Transfers?
- Wer ist Exporteur (Verantwortlicher oder Auftragsverarbeiter)?
- Wer ist Importeur (Land, Rechtstraeger, Konzerneinbindung)?
- Welche Datenarten? Welche besonderen Kategorien (Art. 9 DSGVO)?
- Welche Subprozessoren / Sub-Sub-Prozessoren?
- Verarbeitungszwecke und Datenfluesse (auch innerhalb des Importeurs).

Output: Transfer-Inventar als Tabelle (siehe Skill `ropa-art-30-controller-deutsch-vorlage` für Querverweis).

### Schritt 2 – Identify transfer tool

Ziel: Rechtsgrundlage des Transfers bestimmen.

Optionen:

- **Art. 45 DSGVO – Angemessenheitsbeschluss** (z. B. UK, Schweiz, Japan, Suedkorea, EU-US DPF für gelistete Importeure).
- **Art. 46 DSGVO – Geeignete Garantien**:
 - SCC (Beschluss (EU) 2021/914, Module 1-4),
 - BCR (Art. 47),
 - Genehmigte Verhaltensregeln / Zertifizierungen,
 - Behoerdliche Standardvertragsklauseln.
- **Art. 49 DSGVO – Ausnahmen** (Einwilligung, Vertragserfuellung, Rechtsanspruch) – nur eng auslegen, keine Dauerloesung.

Bei Art. 45 endet die TIA-Pruefung haeufig hier (Schritt 3-5 dann reduziert).

### Schritt 3 – Assess law and practice

Ziel: Drittlandsrecht und tatsaechliche Praxis bewerten.

Pruefen:

- Welche Behörden haben Zugriffsbefugnisse?
- Welche Eingriffstiefe? Welche Garantien (gerichtliche Kontrolle, Anlassbezug)?
- Empfehlung 02/2020 – Europaeische Wesentliche Garantien (EEG):
 - Garantie A: klare, praezise und vorhersehbare Regelungen.
 - Garantie B: Notwendigkeit und Verhaeltnismaessigkeit.
 - Garantie C: unabhaengiger Pruefmechanismus.
 - Garantie D: effektive Rechtsschutzmoeglichkeiten der betroffenen Person.
- Sind die Garantien im Recht **und** in der Praxis erfuellt?

Quellen für Bewertung: offizielle Berichte, Transparenzberichte des Importeurs, EDPB-Empfehlungen, frei zugaengliche Auswertungen.

### Schritt 4 – Adopt supplementary measures

Falls Schritt 3 negativ: ergaenzende Schutzmassnahmen.

Drei Kategorien:

- **Technische Massnahmen** (oft entscheidend): starke Verschluesselung mit Key Management ausserhalb des Drittlands; Pseudonymisierung mit unkorrelierten Schluesseln; Split Processing; ueberhaupt kein Klartext-Zugriff durch Importeur.
- **Vertragliche Massnahmen**: erweiterte Audit- und Transparenzrechte, Behördenanfragen-Berichtspflichten, Warrant Canary, sofortige Aussetzungspflichten.
- **Organisatorische Massnahmen**: Mitarbeiterschulung, klare Eskalationsprozesse, Lieferantenbewertung, dokumentierte Anfechtungspolitik.

EDPB-Anhang 2 zu Empfehlung 01/2020 listet Use Cases 1-7 (Use Case 6 und 7 ohne wirksame Schutzmassnahmen denkbar).

### Schritt 5 – Procedural steps

Wenn ergaenzende Massnahmen erforderlich:

- AVV/DPA anpassen.
- SCC ergaenzende Anhaenge ausfuellen (Annex I, II, III).
- Falls SCC angepasst werden (Klauselzusatz, nicht Streichung) – Konsultation Aufsichtsbehoerde pruefen.
- Bei BCR – Updates an die Lead-Behörde melden.
- Genehmigung beantragen, wo erforderlich.

### Schritt 6 – Re-evaluate

Erneute Pruefung bei Aenderungen:

- Aenderungen im Drittlandsrecht (Gesetze, Urteile).
- Aenderungen in der Behördenpraxis.
- Aenderungen beim Importeur (Konzernstruktur, Subprozessoren, Dienste).
- Aenderungen beim Exporteur (neue Datenarten, neue Zwecke).
- Mindestens jaehrlich.

## Mustertext / Template

Kapitelueberschriften für das TIA-Dokument:

```
1. Know your transfers
 1.1 Transferparteien
 1.2 Datenarten
 1.3 Subprozessoren und Onward Transfers
 1.4 Datenflussdiagramm

2. Transfer tool
 2.1 Gewaehltes Instrument
 2.2 Begruendung der Wahl

3. Bewertung Drittlandsrecht und -praxis
 3.1 Behoerdliche Zugriffsbefugnisse
 3.2 EEG-Pruefung (A, B, C, D)
 3.3 Transparenzberichte und Erfahrungswerte des Importeurs

4. Ergaenzende Schutzmassnahmen
 4.1 Technisch
 4.2 Vertraglich
 4.3 Organisatorisch
 4.4 Wirkungsbewertung

5. Verfahrensschritte
 5.1 Vertraglich umgesetzte Massnahmen
 5.2 Aufsichtsbehoerden-Konsultation (falls erforderlich)
 5.3 Sign-off

6. Re-evaluation
 6.1 Trigger für Neubewertung
 6.2 Naechstes Review-Datum
 6.3 Notfallaussetzungs-Prozess
```

## Typische Fehler

- Schritt 1 unvollstaendig: nur Direkttransfer betrachtet, nicht Onward Transfer.
- Schritt 2: DPF gewaehlt, aber Importeur nicht aktiv gelistet.
- Schritt 3: keine Praxispruefung – nur abstrakte Rechtsanalyse.
- Schritt 4: ausschliesslich vertragliche Massnahmen ohne technische Untermauerung – nach EDPB regelmaessig unzureichend.
- Schritt 5: SCC inhaltlich veraendert (statt nur ergaenzt) – riskant.
- Schritt 6: kein Review-Termin.
- TIA wird gemacht, aber nicht zur Akte genommen.

## Querverweise

- `tia-schrems-ii-eugh-c-311-18-grundlagen` für rechtliche Grundlage.
- `tia-us-fisa-702-und-eo-12333-bewertung` für US-Spezifik.
- `tia-zusaetzliche-schutzmassnahmen-encryption-pseudonymisierung` für Schritt 4.
- `tia-laender-bewertung-china-india-brazil-uk` für weitere Länder.
- `tia-template-deutsch-vollvorlage` für das Vollvorlage-Dokument.
- `tia-en-six-step-roadmap` für englische Fassung.

## Quellen Stand 06/2026

- EuGH C-311/18 vom 16.07.2020 (Schrems II).
- EDPB Empfehlung 01/2020 vom 10.11.2020, Final 18.06.2021.
- EDPB Empfehlung 02/2020 vom 10.11.2020 (EEG).
- Durchfuehrungsbeschluss (EU) 2021/914 vom 04.06.2021 (SCC).
- Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023 (EU-US DPF).
- Art. 44–49 DSGVO.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
