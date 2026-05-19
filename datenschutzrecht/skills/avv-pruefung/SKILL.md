---
name: avv-pruefung
description: >
  AVV-Prüfung nach Art. 28 DSGVO: Klausel-für-Klausel-Analyse gegen das eigene Playbook,
  Prüfung von Sub-Auftragsverarbeiter-Klauseln, Drittland-Transferfolgenabschätzung (TIA),
  EU-Standardvertragsklauseln (EU-SCC) und EU-US Data Privacy Framework (DPF).
  Richtung (Auftragsverarbeiter oder Verantwortlicher) wird automatisch erkannt.
language: de
triggers:
  - "AVV"
  - "Auftragsverarbeitungsvertrag"
  - "dpa review"
  - "data processing agreement"
  - "Art. 28 DSGVO"
  - "Sub-Auftragsverarbeiter"
  - "Standardvertragsklauseln"
  - "SCC"
---

# AVV-Review – Auftragsverarbeitungsvertrag Art. 28 DSGVO

## Zweck

Strukturierte Prüfung eingehender oder ausgehender Auftragsverarbeitungsverträge gegen Art. 28 DSGVO-Mindestanforderungen, das eigene AVV-Playbook (aus `CLAUDE.md`) und aktuelle EDSA-Leitlinien. Der Skill prüft zusätzlich, ob Drittlandtransfers wirksam abgesichert sind (EU-SCC, DPF, TIA) und ob Sub-Auftragsverarbeiter-Klauseln den Anforderungen entsprechen.

## Eingaben

- AVV-Dokument (Datei oder Paste)
- Richtung (optional): „Wir sind AV" oder „Wir sind Verantwortlicher" – sonst automatische Erkennung
- Optional: Liste bekannter Sub-AVs des Anbieters
- Optional: Land der Datenverarbeitung / Hosting-Region

## Ablauf

1. **Richtungserkennung.** Wer ist „Auftraggeber" / „Verantwortlicher", wer „Auftragnehmer" / „Auftragsverarbeiter" im vorgelegten Dokument? Parteienbezeichnung, Weisungsklauseln und Haftungsstruktur prüfen. Bei Unklarheit fragen.

2. **Art. 28 DSGVO Pflichtklausel-Check.** Jede gesetzlich vorgeschriebene Klausel prüfen:

   | Art. 28 Abs. 3 DSGVO | Pflichtinhalt | Status |
   |---|---|---|
   | lit. a | Weisungsgebundenheit + Weisungsregister | ✓ / ⚠️ / ✗ |
   | lit. b | Vertraulichkeitsverpflichtung verarbeitendes Personal | ✓ / ⚠️ / ✗ |
   | lit. c | Technisch-organisatorische Maßnahmen (TOM) nach Art. 32 DSGVO | ✓ / ⚠️ / ✗ |
   | lit. d | Sub-Auftragsverarbeiter-Regelung (allgemeine oder spezifische Genehmigung) | ✓ / ⚠️ / ✗ |
   | lit. e | Unterstützung bei Betroffenenrechten | ✓ / ⚠️ / ✗ |
   | lit. f | Unterstützung bei Art. 32–36 DSGVO (DSFA, Datenpanne, Vorab-Konsultation) | ✓ / ⚠️ / ✗ |
   | lit. g | Löschung oder Rückgabe nach Vertragsende | ✓ / ⚠️ / ✗ |
   | lit. h | Audit-Recht und Nachweispflichten | ✓ / ⚠️ / ✗ |

3. **Playbook-Abgleich.** Jede Klausel mit der eigenen Standardposition aus `CLAUDE.md` vergleichen:
   - ✅ Standardposition = akzeptabel
   - ⚠️ Fallback-Position = bedingt akzeptabel, mit Bedingungen
   - 🔴 Unter Playbook-Minimum = nicht akzeptabel, Redline-Vorschlag

4. **Sub-Auftragsverarbeiter-Prüfung.**
   - Allgemeine vs. spezifische Genehmigung (Art. 28 Abs. 2 DSGVO)?
   - Wechselbenachrichtigungsfrist vorhanden? (Praxis: 4 Wochen; kürzer = Einspruchsrecht faktisch ausgehöhlt)
   - Haftungsüberleitung auf Sub-AV in gleichem Umfang (Art. 28 Abs. 4 DSGVO)?
   - Liste der Sub-AVs verfügbar / aktuell?
   - Sub-AVs in Drittländern? → Weiterleitung zu Schritt 5 (TIA).

5. **Drittlandtransfer-Check (TIA).**
   - Werden Daten außerhalb EU/EWR verarbeitet oder zugänglich gemacht?
   - Welcher Transfermechanismus: EU-SCC (Beschluss 2021/914), DPF, BCR, Art. 49 Abs. 1 DSGVO Ausnahmen?
   - EU-SCC: Modul korrekt (AV-zu-AV, Verantwortlicher-zu-AV)? Technische Anlage befüllt?
   - DPF: Anbieter auf DPF-Liste eingetragen (data.privacyframework.gov)? `[Modellwissen – prüfen, da DPF ggf. geändert]`
   - TIA nach EDSA-Empfehlungen 01/2020 erforderlich? (Ja, wenn SCC ohne zusätzliche Schutzmaßnahmen nicht ausreichen)
   - Risikobewertung: EuGH Schrems II-Kriterien anwenden (C-311/18, NJW 2020, 2945) `[Modellwissen – prüfen]`

6. **Redline-Vorschläge.** Für jede 🔴-Klausel konkreten Änderungsvorschlag formulieren – in Vertragssprache, nicht als Memo-Kommentar.

7. **Bewertungstabelle und Empfehlung.**
   - Gesamt-Risikobewertung: 🔴 Blockend / 🟠 Hoch / 🟡 Mittel / 🟢 Gering
   - Empfehlung: Unterzeichnen / Mit Redlines unterzeichnen / Ablehnen / Eskalieren

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 28 DSGVO (Auftragsverarbeitung, Mindestinhalt AVV)
- Art. 28 Abs. 2 DSGVO (Sub-Auftragsverarbeiter)
- Art. 28 Abs. 4 DSGVO (Haftungsüberleitung Sub-AV)
- Art. 32 DSGVO (TOM)
- Art. 44–49 DSGVO (Drittlandtransfer)
- Beschluss 2021/914/EU (EU-SCC, neue Standardvertragsklauseln)
- EuGH, Urt. v. 16.07.2020 – C-311/18 (Schrems II), NJW 2020, 2945 (TIA-Grundlage)
- EDSA-Empfehlungen 01/2020 zur Transferfolgenabschätzung (TIA), Stand 2022
- EDSA-Leitlinien 07/2022 zu Zertifizierungen als Transfermechanismus
- Hartung, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 28 Rn. 65 ff. (Sub-AV).
- Schantz, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 28 Rn. 1 ff.
- Werkmeister, in: Gola, DSGVO, 2. Aufl. 2018, Art. 28 Rn. 1 ff.
- Plath, in: Plath, DSGVO/BDSG, 3. Aufl. 2021, Art. 28 Rn. 1 ff.
- Schulze, in: BeckOK DSGVO, 16. Ed. (Stand 01.11.2024), Art. 28 Rn. 1 ff.

## Ausgabeformat

1. **Kopfzeile:** Dokumentbezeichnung, Datum des Reviews, Richtung, Risikobewertung Gesamt
2. **Pflichtklausel-Tabelle** (Art. 28 Abs. 3 DSGVO, alle Buchstaben, Status ✓/⚠️/🔴)
3. **Playbook-Abgleich** (Klausel | Ist-Position | Soll-Position | Bewertung | Empfehlung)
4. **Sub-AV-Abschnitt** (Listenformat)
5. **TIA-Abschnitt** (nur wenn Drittlandexposure vorhanden)
6. **Redline-Vorschläge** (Vertragssprache, nummeriert)
7. **Entscheidungsoptionen**

## Beispiel (Gutachtenstil)

**Sachverhalt:** Ein SaaS-Anbieter aus den USA legt einen AVV vor. Daten werden auf AWS-Servern in der EU (Frankfurt) sowie auf Support-Systemen in den USA verarbeitet.

**Analyse Sub-AV-Klausel:**
Der AVV sieht eine allgemeine Genehmigung für Sub-Auftragsverarbeiter vor (Art. 28 Abs. 2 Alt. 1 DSGVO), jedoch beträgt die Wechselfrist nur 7 Tage. Dies unterschreitet die praxisübliche Mindestfrist von 4 Wochen erheblich. Die EDSA-Leitlinien verlangen zwar keine konkrete Mindestfrist, eine 7-Tage-Frist ermöglicht jedoch faktisch keine sinnvolle Prüfung und Einwendung des Verantwortlichen. Vgl. Hartung, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 28 Rn. 70: Einspruchsfrist muss dem Verantwortlichen eine tatsächliche Prüfung ermöglichen. **Bewertung: 🔴 Blockend.**

**Redline-Vorschlag:**
> „Der Auftragsverarbeiter informiert den Verantwortlichen mindestens **30 (dreißig)** Tage im Voraus über geplante Änderungen an der Sub-Auftragsverarbeiter-Liste. Innerhalb dieser Frist kann der Verantwortliche Einspruch erheben. Bei berechtigtem Einspruch, den der Auftragsverarbeiter nicht durch zumutbare technische oder organisatorische Maßnahmen ausräumen kann, ist der Verantwortliche zur außerordentlichen Kündigung berechtigt."

**Analyse Drittlandtransfer (USA, Support-Systeme):**
Der AVV enthält EU-SCC nach Beschluss 2021/914/EU (Modul 2: Verantwortlicher-zu-AV). Eine TIA nach den EDSA-Empfehlungen 01/2020 ist vorzunehmen. Prüfungsschritte nach Schrems II (EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2945 Rn. 134 ff.):
1. Rechtslage im Empfängerland (USA: FISA Section 702, EO 14086 – PPD-28-Nachfolger) `[Modellwissen – prüfen]`
2. Praktische Wahrscheinlichkeit des Zugriffs (Support-Systeme mit Personalbezug: mittel)
3. Zusätzliche Schutzmaßnahmen erforderlich? (Empfehlung: Pseudonymisierung Support-Daten, Zugriffsprotokolle)

## Risiken / typische Fehler

- **Richtungsverwechslung:** Falsches SCC-Modul hat keine Schutzwirkung. Art. 28 Abs. 4 DSGVO setzt voraus, dass Sub-AV-Kette rechtswirksam abgesichert ist.
- **Veraltete SCC:** Altes SCC-Muster (2001/497/EG, 2004/915/EG) ist seit 27.09.2021 nicht mehr für neue Verträge verwendbar; bestehende Altverträge waren bis 27.12.2022 umzustellen (§ 46 Abs. 5 DSGVO-Beschluss). `[Modellwissen – aktuellen Status prüfen]`
- **DPF-Validität:** Das EU-US Data Privacy Framework steht unter politischem Vorbehalt (vgl. Schrems II zur Vorgänger-Regelung). DPF-Eintrag auf data.privacyframework.gov vor Unterschrift prüfen.
- **TIA nur Formalie:** Eine TIA muss ehrliche Risikobewertung enthalten. Pauschal „Risiko akzeptabel" ohne Begründung genügt Art. 28 DSGVO und den EDSA-Empfehlungen 01/2020 nicht.
- **Sub-AV-Haftungslücke:** Art. 28 Abs. 4 DSGVO verlangt, dass dem Sub-AV „dieselben Datenschutzpflichten" auferlegt werden. Ein AVV, der nur auf die DSGVO verweist, ohne Mindestklauseln zu spiegeln, erfüllt diese Anforderung nicht (str., vgl. Hartung, in: Kühling/Buchner, Art. 28 Rn. 80).
- **Berufsgeheimnisträger:** Bei Mandanten-AVVs (Kanzleien, Ärzte) muss der AVV § 203 StGB und § 43a Abs. 2 BRAO berücksichtigen – unzureichende Vertraulichkeitsklausel kann Strafbarkeit begründen.
