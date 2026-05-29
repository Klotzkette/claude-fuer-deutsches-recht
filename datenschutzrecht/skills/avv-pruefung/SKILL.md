---
name: avv-pruefung
description: "Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Prüfraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit Subauftragsverarbeiter Rückgabe Lösung Audits. Output: AVV-Prüfmemo oder Vertragsentwurf. Abgrenzung: nicht für Joint-Controller-Vereinbarungen (joint-controller-vereinbarung)."
---

# AVV-Review – Auftragsverarbeitungsvertrag Art. 28 DSGVO

## Zweck

Strukturierte Prüfung eingehender oder ausgehender Auftragsverarbeitungsverträge gegen Art. 28 DSGVO-Mindestanforderungen, das eigene AVV-Playbook (aus `CLAUDE.md`) und aktuelle EDSA-Leitlinien. Der Skill prüft zusätzlich, ob Drittlandtransfers wirksam abgesichert sind (EU-SCC, DPF, TIA) und ob Sub-Auftragsverarbeiter-Klauseln den Anforderungen entsprechen.

## Eingaben

- AVV-Dokument (Datei oder Paste)
- Richtung (optional): "Wir sind AV" oder "Wir sind Verantwortlicher" – sonst automatische Erkennung
- Optional: Liste bekannter Sub-AVs des Anbieters
- Optional: Land der Datenverarbeitung / Hosting-Region

## Ablauf

1. **Richtungserkennung.** Wer ist "Auftraggeber" / "Verantwortlicher", wer "Auftragnehmer" / "Auftragsverarbeiter" im vorgelegten Dokument? Parteienbezeichnung, Weisungsklauseln und Haftungsstruktur prüfen. Bei Unklarheit fragen.

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
   - Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EDSA-Empfehlungen 01/2020 zur Transferfolgenabschätzung (TIA), Stand 2022
- EDSA-Leitlinien 07/2022 zu Zertifizierungen als Transfermechanismus
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Schantz, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 28 Rn. 1 ff.
- Werkmeister, in: Gola, DSGVO, 2. Aufl. 2018, Art. 28 Rn. 1 ff.
- Plath, in: Plath, DSGVO/BDSG, 3. Aufl. 2021, Art. 28 Rn. 1 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

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
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

**Redline-Vorschlag:**
> "Der Auftragsverarbeiter informiert den Verantwortlichen mindestens **30 (dreißig)** Tage im Voraus über geplante Änderungen an der Sub-Auftragsverarbeiter-Liste. Innerhalb dieser Frist kann der Verantwortliche Einspruch erheben. Bei berechtigtem Einspruch, den der Auftragsverarbeiter nicht durch zumutbare technische oder organisatorische Maßnahmen ausräumen kann, ist der Verantwortliche zur außerordentlichen Kündigung berechtigt."

**Analyse Drittlandtransfer (USA, Support-Systeme):**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtslage im Empfängerland (USA: FISA Section 702, EO 14086 – PPD-28-Nachfolger) `[Modellwissen – prüfen]`
2. Praktische Wahrscheinlichkeit des Zugriffs (Support-Systeme mit Personalbezug: mittel)
3. Zusätzliche Schutzmaßnahmen erforderlich? (Empfehlung: Pseudonymisierung Support-Daten, Zugriffsprotokolle)

## Risiken / typische Fehler

- **Richtungsverwechslung:** Falsches SCC-Modul hat keine Schutzwirkung. Art. 28 Abs. 4 DSGVO setzt voraus, dass Sub-AV-Kette rechtswirksam abgesichert ist.
- **Veraltete SCC:** Altes SCC-Muster (2001/497/EG, 2004/915/EG) ist seit 27.09.2021 nicht mehr für neue Verträge verwendbar; bestehende Altverträge waren bis 27.12.2022 umzustellen (§ 46 Abs. 5 DSGVO-Beschluss). `[Modellwissen – aktuellen Status prüfen]`
- **DPF-Validität:** Das EU-US Data Privacy Framework steht unter politischem Vorbehalt (vgl. Schrems II zur Vorgänger-Regelung). DPF-Eintrag auf data.privacyframework.gov vor Unterschrift prüfen.
- **TIA nur Formalie:** Eine TIA muss ehrliche Risikobewertung enthalten. Pauschal "Risiko akzeptabel" ohne Begründung genügt Art. 28 DSGVO und den EDSA-Empfehlungen 01/2020 nicht.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- **Berufsgeheimnisträger:** Bei Mandanten-AVVs (Kanzleien, Ärzte) muss der AVV § 203 StGB und § 43a Abs. 2 BRAO berücksichtigen – unzureichende Vertraulichkeitsklausel kann Strafbarkeit begründen.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei neuen EDSA-Leitlinien zur Auftragsverarbeitung, Änderungen des SCC-Beschlusses 2021/914/EU oder neuen DPF-Entwicklungen.

**Hinweis EDSA-Leitlinien zur Auftragsverarbeitung:** Der EDSA hat Leitlinien zur Abgrenzung von Verantwortlichen und Auftragsverarbeitern veröffentlicht (EDSA, Leitlinien 07/2020 zur Abgrenzung Verantwortlicher/Auftragsverarbeiter, angenommen 07.07.2021). Diese sind bei der Richtungserkennung (Schritt 1) und bei der Prüfung der Pflichtklauseln verbindlich heranzuziehen. Insbesondere: Wer weisungsgebunden und ohne eigenen Entscheidungsspielraum verarbeitet, ist Auftragsverarbeiter; eigenständige Zwecksetzung begründet Mit-Verantwortlichkeit (Art. 26 DSGVO). `[Modellwissen – aktuellen EDSA-Leitlinienstand auf edpb.europa.eu prüfen]`

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Vollständige TIA-Methodik und SCC-Modul-Auswahl-Matrix
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — DSFA bei Hochrisiko-AVV-Konstellationen

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **EDSA Guidelines 07/2020 zu Verantwortlichen und Auftragsverarbeitern:** Final-Version verbindliche Auslegungshilfe; bei der Rollenzuordnung beruecksichtigen. Quelle: edpb.europa.eu.
- **EDSA Stellungnahme 22/2024 zu Auftragsverarbeitern und Sub-AV:** Aktuelle Stellungnahmen zur Sub-Verarbeiter-Kette und zur Verantwortlichkeit live ueber edpb.europa.eu pruefen.
- **EuGH-Linie zu Art. 82 DSGVO Mit-Haftung:** Verantwortlicher und Auftragsverarbeiter haften gesamtschuldnerisch nach Massgabe ihrer jeweiligen Pflichtverletzungen (Art. 82 Abs. 4 DSGVO). Konkrete Aktenzeichen vor Zitat ueber curia.europa.eu pruefen.
- **EU-US-DPF-Status:** Vor jedem US-AVV-Abschluss DPF-Listing des Anbieters ueber dataprivacyframework.gov verifizieren. SCC bleiben als Fallback im AVV vorzusehen.
- **KI-Anbieter-AVV:** Bei KI-/LLM-Diensten muessen AVV-Klauseln zusaetzlich zu Art. 28 DSGVO Trainings-Verbote, Output-Verwertung, Modellaenderungen, Logging und KI-VO-Pflichten regeln. Verweis: ki-anbieter-pruefung (Plugin ki-governance).
- **NIS-2-Lieferkette (Art. 21 NIS-2-RL):** Auftraggeber wichtiger / besonders wichtiger Einrichtungen muessen Cyber-Risiken in der Lieferkette beruecksichtigen — AVV mit IT-/Cloud-Dienstleistern entsprechend erweitern.

## Triage-Frage (Entscheidungsbaum AVV)

```
Prüfungsrichtung?
  Eingehender AVV (wir sind Verantwortlicher) → Prüfe: Weisungsrecht vollständig?
  Ausgehender AVV (wir sind Auftragsverarbeiter) → Prüfe: Pflichten Art. 28 Abs. 3 vollständig?
  Unklar → Richtungserkennung über Parteienbezeichnung und Weisungsklausel

Drittlandbezug?
  Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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

