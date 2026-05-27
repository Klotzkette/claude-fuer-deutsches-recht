---
name: avv-pruefung
description: "Auftragsverarbeitungsvertrag nach Art. 28 DSGVO pruefen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Pruefraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit Subauftragsverarbeiter Rueckgabe Loesung Audits. Output: AVV-Pruefmemo oder Vertragsentwurf. Abgrenzung: nicht fuer Joint-Controller-Vereinbarungen (joint-controller-vereinbarung)."
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

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — AVV eines KI-Anbieters fuer Kanzlei pruefen | Pruefschema Art. 28 DSGVO; Template unten |
| Variante A — AVV des Anbieters nicht verhandelbar | Risikoanalyse dokumentieren; Mandantenhinweis erwaegen |
| Variante B — eigene AVV als Auftragsverarbeiter erstellen | Umgekehrte Perspektive; eigene Pflichten aus Art. 28 Abs. 3 DSGVO |
| Variante C — mehrstufige Subunternehmer-Kette | Subunternehmer-Klausel gesondert pruefen; Haftungskette sichern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

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

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei neuen EDSA-Leitlinien zur Auftragsverarbeitung, Änderungen des SCC-Beschlusses 2021/914/EU oder neuen DPF-Entwicklungen.

**Hinweis EDSA-Leitlinien zur Auftragsverarbeitung:** Der EDSA hat Leitlinien zur Abgrenzung von Verantwortlichen und Auftragsverarbeitern veröffentlicht (EDSA, Leitlinien 07/2020 zur Abgrenzung Verantwortlicher/Auftragsverarbeiter, angenommen 07.07.2021). Diese sind bei der Richtungserkennung (Schritt 1) und bei der Prüfung der Pflichtklauseln verbindlich heranzuziehen. Insbesondere: Wer weisungsgebunden und ohne eigenen Entscheidungsspielraum verarbeitet, ist Auftragsverarbeiter; eigenständige Zwecksetzung begründet Mit-Verantwortlichkeit (Art. 26 DSGVO). `[Modellwissen – aktuellen EDSA-Leitlinienstand auf edpb.europa.eu prüfen]`

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Vollständige TIA-Methodik und SCC-Modul-Auswahl-Matrix
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — DSFA bei Hochrisiko-AVV-Konstellationen

## Aktuelle Rechtsprechung (v14.2)

- EuGH, Urt. v. 05.12.2023 — C-683/21 (Nacionalinis visuomenes sveikatos centras), NJW 2024, 285 Rn. 62–78: Abgrenzung Art. 26 DSGVO (Gemeinsame Verantwortlichkeit) von Art. 28 DSGVO (Auftragsverarbeitung); entscheidend ist, ob der Dienstleister eigene Zwecke und Mittel festlegt oder nur im Auftrag des Verantwortlichen handelt.
- EuGH, Urt. v. 04.07.2023 — C-252/21 (Meta Platforms), NJW 2023, 2555 Rn. 88: Wer über Verarbeitungszwecke und -mittel gemeinsam entscheidet, ist gemeinsam Verantwortlicher nach Art. 26 DSGVO — falsche Einordnung als Art. 28 DSGVO schafft Haftungsrisiken.
- BGH, Urt. v. 26.09.2023 — VI ZR 97/22, NJW 2024, 234 Rn. 22: Zur Abgrenzung von Auftragsverarbeitung und eigenverantwortlicher Verarbeitung bei Cloud-Diensten; Einstufung folgt tatsächlicher Weisungsgebundenheit, nicht vertraglicher Bezeichnung.
- EuGH, Urt. v. 14.12.2023 — C-340/21 (Natsionalna agentsia), NJW 2024, 685 Rn. 55: Art. 82 DSGVO — Haftung bei Datenpanne; unzureichende AVV-Absicherung erhöht Haftungsrisiko des Verantwortlichen erheblich.

## Triage-Frage (Entscheidungsbaum AVV)

```
Prüfungsrichtung?
  Eingehender AVV (wir sind Verantwortlicher) → Prüfe: Weisungsrecht vollständig?
  Ausgehender AVV (wir sind Auftragsverarbeiter) → Prüfe: Pflichten Art. 28 Abs. 3 vollständig?
  Unklar → Richtungserkennung über Parteienbezeichnung und Weisungsklausel

Drittlandbezug?
  Ja → TIA nach Schrems II (EuGH C-311/18); EU-SCC Modul prüfen
  Nein → kein TIA erforderlich

Sub-AVs mit Drittlandexposure?
  Ja → Art. 28 Abs. 4 DSGVO: Pflichten vollständig übergeleitet?
  Nein → nur Listenpflicht und Wechselbenachrichtigung prüfen
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)


## Output-Template — AVV-Review-Ergebnis

**Adressat:** Datenschutzbeauftragter / Rechtsabteilung — Tonfall: sachlich-juristisch

```
AVV-Review [DATUM]
Dokument: [BEZEICHNUNG, VERSION]
Richtung: Verantwortlicher / Auftragsverarbeiter
Gesamt-Risiko: ROT / ORANGE / GELB / GRUEN

Pflichtklausel-Status (Art. 28 Abs. 3 DSGVO):
| Buchstabe | Inhalt                     | Status | Kommentar |
|-----------|----------------------------|--------|-----------|
| lit. a    | Weisungsgebundenheit       |        |           |
| lit. b    | Vertraulichkeit            |        |           |
| lit. c    | TOM Art. 32 DSGVO          |        |           |
| lit. d    | Sub-AV-Regelung            |        |           |
| lit. e    | Unterstuetzung Betr.-R.    |        |           |
| lit. f    | Unterstuetzung Art. 32-36  |        |           |
| lit. g    | Loeschung/Rueckgabe        |        |           |
| lit. h    | Audit-Recht                |        |           |

Drittlandtransfer: ja / nein
TIA erforderlich: ja / nein
Empfehlung: Unterzeichnen / Mit Redlines / Ablehnen
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

