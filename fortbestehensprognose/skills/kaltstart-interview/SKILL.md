---
name: kaltstart-interview
description: "Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steuerliche Ansprechpartner ist welches Geschäftsjahr und welche Rechtsform vorliegt un..."
---

# /fortbestehensprognose:fortbestehensprognose-kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fortbestehensprognose** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Disclaimer (Schlüsselstelle)

Dieses Plugin liefert eine **Selbstdokumentation** der Fortbestehensprognose nach § 19 Abs. 2 InsO. Es ersetzt **nicht** die anwaltliche Prüfung durch einen Insolvenzrechtler bei Anzeichen für Insolvenzreife. Die Antragspflicht nach § 15a InsO (drei Wochen bei Zahlungsunfähigkeit, sechs Wochen bei Überschuldung) ist persönliche Pflicht des Geschäftsleiters mit strafrechtlicher Bewehrung (§ 15a Abs. 4 InsO) und Haftungsrisiko (§ 15b InsO, frühere § 64 GmbHG). Im Zweifel **vor** Ablauf der Frist Insolvenzanwalt konsultieren.

## Ablauf

1. Datei `~/.claude/plugins/config/claude-fuer-deutsches-recht/fortbestehensprognose/CLAUDE.md` prüfen.
2. Falls befüllt: bestätigen, gegebenenfalls --redo für Neu-Interview.
3. Andernfalls Interview unten ausführen.

## Interview

### 1. Wer nutzt das Plugin

- **Rolle:** Geschäftsführer GmbH / Vorstand AG / Geschäftsleiter Personengesellschaft / Gesellschafter mit Eigenverantwortung / Finanzleiter / sonst?
- **Persönliche Antragspflicht** nach § 15a InsO? Wer ist Geschäftsleiter mit Antragspflicht? Bei mehreren ist jeder einzeln verpflichtet (BGH-Rspr.).
- **Anwaltlicher Ansprechpartner** (Insolvenzanwalt) — Name, Erreichbarkeit. Bei negativer Prognose sofort eskalieren.
- **Steuerlicher Ansprechpartner** (Steuerberater / Wirtschaftsprüfer) — Name, Erreichbarkeit.

### 2. Unternehmensprofil

- **Rechtsform** GmbH AG GmbH und Co. KG Aktiengesellschaft Personengesellschaft.
- **Stammkapital** (relevant für Mantel- bzw. Anhalt-Insolvenzreife).
- **Geschäftsjahr** und Bilanzstichtag.
- **Branche** (relevant für Plausibilisierung).
- **Beschäftigte** Anzahl.
- **Umsatz** im laufenden Jahr und Vorjahr.

### 3. Buchhaltung und Bilanzierung

- **Buchhaltungssoftware** DATEV Lexware SAP sevDesk sonst.
- **Bilanzierungsstandard** HGB / IFRS / Mischung.
- **Letzter Jahresabschluss** Datum.
- **Aktueller Stand** unterjaehrige BWA SuSa Konzernreporting verfügbar.

### 4. Ausgangslage

- Was hat den Anlass gegeben für diese Prüfung? (siehe Skill `ausloesendes-ereignis-erfassen`)
- Bilanzielle Überschuldung bereits festgestellt? (Aktiva kleiner als Passiva?)
- Stille Reserven oder Lasten vorhanden?
- Aktuelle Liquiditätslage subjektiv: angespannt? ausreichend? bereits überschritten?

### 5. Eskalationspfad

- **Ab welchem Befund** wird sofort der Insolvenzanwalt eingeschaltet? Empfehlung: bei jedem 🔴-Flag im Verlauf.
- **Drei-Wochen-Frist** § 15a InsO bei Zahlungsunfähigkeit (§ 17 InsO) ist persönliche Pflicht. **Sechs Wochen** bei Überschuldung (§ 19 InsO seit SanInsFoG 2021).
- **Kein Aufschieben** wegen Sanierungsverhandlungen — die Frist beginnt mit Eintritt der Insolvenzreife (objektives Kriterium).

### 6. Standort

- **Sitz und Insolvenzgericht** (Belegenheits-AG nach § 3 InsO).
- **Bundesland** (relevant für Justiznetzwerk).

## Rechtlicher Rahmen

- **InsO** § 15a (Antragspflicht), § 15b (Zahlungsverbot ab Insolvenzreife), § 17 (Zahlungsunfähigkeit), § 18 (drohende Zahlungsunfähigkeit, Prognose 24 Monate seit 2021), § 19 (Überschuldung, Fortbestehensprognose 12 Monate seit 2021).
- **StaRUG** §§ 29 ff. (Restrukturierungsrahmen vor Insolvenzreife), § 102 (Hinweispflicht Steuerberater).
- **IDW S 11** Beurteilung des Vorliegens von Insolvenzeröffnungsgründen.
- **IDW S 6** Anforderungen an Sanierungskonzepte.
- **GmbHG** § 64 a.F. — heute § 15b InsO.

## Ausgabe

Profil wird geschrieben. Empfohlene nächste Skills:

1. `/fortbestehensprognose:ausloesendes-ereignis-erfassen` — Anlass und Vorinformation
2. `/fortbestehensprognose:bilanzieller-status-aufnehmen` — Ausgangsfeststellung
3. `/fortbestehensprognose:annahmen-sammeln-fortfuehrung` — Prognoseannahmen
4. (parallel) `/liquiditaetsplanung` — für die rollierende 12-Monats-Liquidität

Bei aktuten Anzeichen für Zahlungsunfähigkeit (Liquiditätslücke über 10 Prozent seit mehr als drei Wochen) **sofort** Insolvenzanwalt einschalten und mit Plugin `insolvenzrecht` arbeiten — nicht in diesem Plugin weiterarbeiten.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Rechtlicher Rahmen und Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Kaltstart

§ 19 InsO (Ueberschuldungsgrund) → § 15a InsO (Antragspflicht) → § 15b InsO (Zahlungs-/Haftungsrisiko) → § 43 GmbHG (Sorgfaltspflicht GF) → IDW S 11 (Standard Insolvenz-Beurteilung)
