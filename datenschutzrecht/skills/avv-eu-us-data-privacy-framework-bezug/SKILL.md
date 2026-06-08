---
name: avv-eu-us-data-privacy-framework-bezug
description: "Behandlung des EU-US Data Privacy Framework (DPF) im AVV. Angemessenheitsbeschluss EU-Kommission vom 10.07.2023 Beschluss (EU) 2023/1795. Anforderungen an Selbstzertifizierung Pruefung der Listung Fallback ueber SCC 2021/914 und Transfer Impact Assessment. Output: AVV-Klauselbausteine für DPF und Fallback."
---

# EU-US Data Privacy Framework (DPF) im AVV

## Zweck / Purpose

Behandlung des EU-US Data Privacy Frameworks im AVV inklusive Selbstzertifizierungspruefung und SCC-Fallback. Purpose (EN): Treatment of the EU-US Data Privacy Framework in DPAs, including self-certification check and SCC fallback.

## Wann dieses Modul hilft

- US-Anbieter wird als Auftragsverarbeiter beauftragt oder eingebunden.
- Pruefung, ob Anbieter unter dem EU-US Data Privacy Framework selbstzertifiziert ist.
- Vertragsklausel für DPF-Nutzung und SCC-Fallback ist erforderlich.
- Aufsichtsbehoerde fragt nach Drittlandtransfer-Absicherung.

## Rechtlicher Rahmen

- Durchfuehrungsbeschluss (EU) 2023/1795 der Kommission vom 10.07.2023 ueber die Angemessenheit des Schutzniveaus personenbezogener Daten nach dem EU-US Data Privacy Framework – verifiziert.
- Art. 45 DSGVO – Angemessenheitsbeschluss.
- Art. 46 DSGVO – Geeignete Garantien (SCC, BCR) als Fallback.
- Art. 49 DSGVO – Ausnahmen für bestimmte Faelle.
- Executive Order 14086 vom 07.10.2022 – US-Schutzgarantien (signal intelligence safeguards, DPRC).
- EuGH C-311/18 (Schrems II) – verifiziert: Vorgaengerregelung Privacy Shield für unwirksam erklaert.

## Ablauf / Checkliste

1. **Selbstzertifizierung pruefen.**
 - Liste pruefen ueber dataprivacyframework.gov.
 - Status: aktiv ("Active") versus inaktiv ("Inactive Participant").
 - Geltungsbereich der Selbstzertifizierung: HR-Daten und/oder Non-HR-Daten?
 - Im Listing für den konkreten Datentypus zertifiziert?

2. **Vertragsabsicherung.**
 - DPF-Selbstzertifizierung des Anbieters wird im AVV ausdruecklich referenziert.
 - SCC nach Beschluss (EU) 2021/914 als Fallback für den Fall, dass der Anbieter die Selbstzertifizierung verliert oder das DPF unwirksam wird.
 - Transfer Impact Assessment auch bei DPF-Nutzung empfohlen, weil DPF politisch und rechtlich angreifbar bleibt (Schrems-Linie).

3. **Sub-AV-Kette pruefen.**
 - Sub-AV des US-Anbieters mit weiterem US-Standort oder Drittland?
 - Eigene DPF-Selbstzertifizierung jedes US-Sub-AV erforderlich.
 - Fuer Nicht-US-Drittland-Sub-AV: SCC oder anderer Transfermechanismus.

4. **Monitoring.**
 - DPF-Listing periodisch (mindestens jaehrlich) ueberpruefen.
 - Pruefung vor jedem Vertragsschluss und vor wesentlicher Vertragsverlaengerung.

5. **Eskalation.**
 - Bei Suspendierung der DPF-Listung: sofortige Aktivierung des SCC-Fallback.
 - Bei Unwirksamkeitserklaerung des DPF durch EuGH (analog Schrems II): umfassende Transferpruefung neu.

## Mustertext / Template

DPF-und-Fallback-Klausel:

> "§ X Drittlandtransfer in die Vereinigten Staaten
>
> (1) Soweit der Auftragsverarbeiter personenbezogene Daten in die Vereinigten Staaten uebermittelt oder dort verarbeitet, erfolgt die Uebermittlung primaer auf Grundlage des Durchfuehrungsbeschlusses (EU) 2023/1795 der Kommission vom 10.07.2023 (EU-US Data Privacy Framework). Der Auftragsverarbeiter sichert zu, dass er gemaess dem Data Privacy Framework wirksam selbstzertifiziert ist und die zertifizierten Datenkategorien die unter diesem Vertrag uebermittelten Daten umfassen.
>
> (2) Der Auftragsverarbeiter teilt dem Verantwortlichen jede Aenderung oder Suspendierung seiner DPF-Selbstzertifizierung unverzueglich, spaetestens innerhalb von zehn (10) Kalendertagen, schriftlich mit.
>
> (3) Fuer den Fall, dass die DPF-Selbstzertifizierung des Auftragsverarbeiters endet, ausgesetzt wird oder der Angemessenheitsbeschluss (EU) 2023/1795 ganz oder teilweise unwirksam wird, gelten ab dem Zeitpunkt des Eintritts und ohne weitere Erklaerung der Parteien die EU-Standardvertragsklauseln gemaess Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021, Modul 2 (Verantwortlicher an Auftragsverarbeiter), mit den in Anlage 6 dargestellten Auswahl- und Anhangsfestlegungen.
>
> (4) Unabhaengig vom DPF fuehrt der Auftragsverarbeiter auf Verlangen des Verantwortlichen ein Transfer Impact Assessment nach den EDSA-Empfehlungen 01/2020 durch und stellt das Ergebnis innerhalb von dreissig (30) Kalendertagen zur Verfuegung.
>
> (5) Setzt der Auftragsverarbeiter Sub-Auftragsverarbeiter in den Vereinigten Staaten ein, gelten die Absaetze (1) bis (4) entsprechend; im Sub-AV-Verzeichnis ist der DPF-Status jedes US-Sub-AV anzugeben."

## Typische Drafting-Fehler

- Verweis auf DPF ohne tatsaechliche Pruefung des Anbieter-Listings.
- DPF ohne SCC-Fallback im Vertrag – bei Ausfall sofortige Kuendigungspflicht.
- US-Sub-AV ohne eigene DPF-Pruefung.
- TIA nicht durchgefuehrt mit der Begruendung "DPF deckt alles ab" – aufsichtsbehoerdliche Erwartung, dass auch unter DPF eine Risikobetrachtung erfolgt.
- Veraltete Verweise auf Privacy Shield – seit Schrems II (EuGH C-311/18) unwirksam.
- DPF-Listing nur einmal geprueft, keine periodische Kontrolle.

## Querverweise

- `datenschutzrecht/skills/avv-cloud-und-subverarbeitung-art-28-iv/SKILL.md`
- `datenschutzrecht/skills/avv-eu-kommission-musterklauseln-2021-915/SKILL.md`
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md`
- `datenschutzrecht/skills/dpa-en-template-controller-processor/SKILL.md`

## Quellen Stand 06/2026

- Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023, ABl. L 231/118 vom 20.09.2023 – verifiziert.
- Durchfuehrungsbeschluss (EU) 2021/914 vom 04.06.2021, ABl. L 199/31 – verifiziert.
- Art. 45, Art. 46, Art. 49 DSGVO.
- US Executive Order 14086 vom 07.10.2022.
- EuGH C-311/18 (Schrems II) – verifiziert; Volltext ueber curia.europa.eu.
- EDSA-Empfehlungen 01/2020 (Version 2.0 Juni 2021).
- DPF-Listing ueber dataprivacyframework.gov pruefen.
- Zitierweise: `../../../references/zitierweise.md`.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.
