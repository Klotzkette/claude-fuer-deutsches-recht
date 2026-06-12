---
name: tia-schrems-ii-eugh-c-311-18-grundlagen
description: "Schrems II als Grundlage des Transfer Impact Assessment. EuGH Urteil C-311/18 vom 16.07.2020 Facebook Ireland und Schrems. Tragende Aussagen, Folgen für Art. 46 DSGVO, Pflicht zur Prüfung der Schutzgleichwertigkeit (essentially equivalent), EDPB-Empfehlung 01/2020 als Konkretisierung."
---

# Schrems II – Grundlagen für Transfer Impact Assessment

## Wann dieses Modul hilft

- Mandant fragt: "Warum brauchen wir ein TIA?"
- Aufsichtsbehoerde verlangt Nachweis, dass die Schrems-II-Folgen geprueft wurden.
- Schulung der eigenen Datenschutzorganisation.
- Strategische Entscheidung Cloud-Provider EU vs. USA.
- Argumentation gegenueber US-Mutterhaus.

## Rechtlicher Rahmen

### Das Urteil

- **EuGH**, Urteil der Großen Kammer vom **16. Juli 2020**, Rechtssache **C-311/18**, Data Protection Commissioner gegen Facebook Ireland Ltd und Maximillian Schrems (ECLI:EU:C:2020:559).

### Tragende Aussagen (vereinfacht, Nachweise direkt am Urteil prüfen)

1. **Privacy Shield ungueltig** (Tenor Nr. 5): Der Angemessenheitsbeschluss 2016/1250 der EU-Kommission ist wegen fehlender Schutzgleichwertigkeit ungueltig.
2. **SCC bleiben grundsätzlich gueltig** (Tenor Nr. 2 und 3): Beschluss 2010/87/EU (jetzt durch 2021/914 ersetzt) ist gueltig, doch der Datenexporteur trifft eine Pflicht zur Einzelfallpruefung.
3. **Schutzgleichwertigkeit** (Rn. 96, 105): Der Schutz im Drittland muss "essentially equivalent" (im Wesentlichen gleichwertig) zum unionsrechtlichen Schutzniveau sein. Massgeblich sind Drittlandsrecht **und** -praxis.
4. **Zugriffsbefugnisse der Behörden** (Rn. 168 ff.): Insbesondere FISA 702 und Executive Order 12333 lassen massenhafte und auch von Nichtbuergern erfassende Zugriffe ohne ausreichenden Rechtsschutz zu – das ist der Kern der Unvereinbarkeit.
5. **Suspendierungspflicht** (Rn. 142): Datenexporteur und ggf. Aufsichtsbehoerde müssen den Transfer aussetzen, wenn die SCC im Zielland nicht eingehalten werden können.
6. **Zusaetzliche Maßnahmen (supplementary measures)** (Rn. 133): Wenn das Drittlandsrecht den SCC-Schutz nicht traegt, sind ergaenzende Schutzmassnahmen erforderlich.

### EDPB-Empfehlung 01/2020 als Folgepapier

- EDPB **Empfehlung 01/2020** "Recommendations on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data", verabschiedet **10.11.2020**, Final Version **18.06.2021**.
- Sechs-Schritte-Roadmap (siehe Skill `tia-edpb-roadmap-6-schritte-deutsch`).

### Folgeentwicklungen

- **SCC neu** (Durchfuehrungsbeschluss (EU) **2021/914** vom **04.06.2021**) – ersetzen alte SCC; Modulstruktur 1-4.
- **EU-US Data Privacy Framework (DPF)**: Durchfuehrungsbeschluss (EU) **2023/1795** vom **10.07.2023** – Angemessenheitsbeschluss als Folgeschritt; loest US-Defizite nicht vollstaendig auf, sondern stuetzt sich auf Executive Order 14086 und Schaffung des Data Protection Review Court.
- Wiederholte Klage **Schrems III** kann zu DPF-Folgeentscheidung fuehren – Rechtsentwicklung beobachten.

## Ablauf / Checkliste

1. Lies das Urteil C-311/18 in der EuGH-Sammlung oder unter curia.europa.eu im Original.
2. Identifiziere für den konkreten Transfer: Importeur, Land, Datenart.
3. Beziehe die EDPB-Empfehlung 01/2020 in die Prüfung ein.
4. Vermeide Verkuerzung "USA = unzulaessig" – differenziere nach DPF-Listing, Datenart, Schutzmassnahmen.
5. Dokumentiere die Prüfung – ohne TIA-Dokument keine Schrems-II-konforme Compliance.
6. Beobachte Folgeentwicklungen (Schrems III, DPR-Court-Entscheidungen, neue Adequacy Decisions).

## Mustertext / Template

Kurzvermerk-Baustein für das TIA:

> Hintergrund der Prüfung ist das Urteil des Europaeischen Gerichtshofs vom 16. Juli 2020 in der Rechtssache C-311/18 (Schrems II), nach dem für Datenuebermittlungen in Drittlaender auf Grundlage von Art. 46 DSGVO eine einzelfallbezogene Bewertung erforderlich ist, ob im Zielland ein der Union "im Wesentlichen gleichwertiges" Schutzniveau gewaehrleistet ist. Soweit das Drittlandsrecht oder die Drittlandspraxis das vertraglich vereinbarte Schutzniveau nicht traegt, sind ergaenzende Schutzmassnahmen vorzusehen oder die Uebermittlung auszusetzen.

## Typische Fehler

- "Schrems II hat das Privacy Shield gekippt – wir brauchen jetzt nur SCC." Falsch: SCC alleine genügen ohne TIA und ggf. zusaetzliche Maßnahmen nicht.
- Verwechslung Schrems I (C-362/14, Safe Harbor) und Schrems II.
- Annahme, der EU-US Data Privacy Framework habe Schrems II "ueberholt". Tatsaechlich: DPF basiert auf neuem Angemessenheitsbeschluss; SCC-Pfad bleibt parallel relevant, und das EuGH-Prüfraster bleibt Maßstab für SCC-Faelle.
- TIA nur für USA gemacht; UK, China, Indien, Brasilien werden vergessen.
- TIA-Dokument als Einmal-Prüfung; keine Wiedervorlage.
- "Essentially equivalent" mit "identisch" gleichgesetzt – nicht zutreffend, ein "im Wesentlichen gleichwertiger" Schutz genuegt.

## Quellen Stand 06/2026

- EuGH, Urteil der Großen Kammer vom 16.07.2020, C-311/18, ECLI:EU:C:2020:559 (Schrems II).
- EuGH, Urteil vom 06.10.2015, C-362/14, ECLI:EU:C:2015:650 (Schrems I, Safe Harbor).
- EDPB Empfehlung 01/2020 vom 10.11.2020, Final 18.06.2021.
- EDPB Empfehlung 02/2020 zum Europaeischen Wesentlichen Garantien (EEG) vom 10.11.2020.
- Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021 (SCC).
- Durchfuehrungsbeschluss (EU) 2023/1795 der Kommission vom 10.07.2023 (EU-US DPF).
- US Executive Order 14086 vom 07.10.2022.
