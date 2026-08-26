---
name: avv-pruefung
description: "Für AVV-Review – Auftragsverarbeitungsvertrag Art. 28 DSGVO: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# AVV-Review – Auftragsverarbeitungsvertrag Art. 28 DSGVO

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
- EDSA-Empfehlungen 01/2020 zur Transferfolgenabschätzung (TIA), Stand 2022
- EDSA-Leitlinien 07/2022 zu Zertifizierungen als Transfermechanismus
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Schantz, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 28 Rn. 1 ff.
- Werkmeister, in: Gola, DSGVO, 2. Aufl. 2018, Art. 28 Rn. 1 ff.
- Plath, in: Plath, DSGVO/BDSG, 3. Aufl. 2021, Art. 28 Rn. 1 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — AVV eines KI-Anbieters für Kanzlei prüfen | Prüfschema Art. 28 DSGVO; Template unten |
| Variante A — AVV des Anbieters nicht verhandelbar | Risikoanalyse dokumentieren; Mandantenhinweis erwaegen |
| Variante B — eigene AVV als Auftragsverarbeiter erstellen | Umgekehrte Perspektive; eigene Pflichten aus Art. 28 Abs. 3 DSGVO |
| Variante C — mehrstufige Subunternehmer-Kette | Subunternehmer-Klausel gesondert prüfen; Haftungskette sichern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Beispiel (Gutachtenstil)

**Sachverhalt:** Ein SaaS-Anbieter aus den USA legt einen AVV vor. Daten werden auf AWS-Servern in der EU (Frankfurt) sowie auf Support-Systemen in den USA verarbeitet.

**Analyse Sub-AV-Klausel:**
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

**Redline-Vorschlag:**
> "Der Auftragsverarbeiter informiert den Verantwortlichen mindestens **30 (dreißig)** Tage im Voraus über geplante Änderungen an der Sub-Auftragsverarbeiter-Liste. Innerhalb dieser Frist kann der Verantwortliche Einspruch erheben. Bei berechtigtem Einspruch, den der Auftragsverarbeiter nicht durch zumutbare technische oder organisatorische Maßnahmen ausräumen kann, ist der Verantwortliche zur außerordentlichen Kündigung berechtigt."

**Analyse Drittlandtransfer (USA, Support-Systeme):**
1. Rechtslage im Empfängerland (USA: FISA Section 702, EO 14086 – PPD-28-Nachfolger) `[Modellwissen – prüfen]`
2. Praktische Wahrscheinlichkeit des Zugriffs (Support-Systeme mit Personalbezug: mittel)
3. Zusätzliche Schutzmaßnahmen erforderlich? (Empfehlung: Pseudonymisierung Support-Daten, Zugriffsprotokolle)

## Risiken / typische Fehler

- **Richtungsverwechslung:** Falsches SCC-Modul hat keine Schutzwirkung. Art. 28 Abs. 4 DSGVO setzt voraus, dass Sub-AV-Kette rechtswirksam abgesichert ist.
- **Veraltete SCC:** Die Entscheidungen 2001/497/EG in der durch 2004/915/EG geänderten Fassung und 2010/87/EU wurden zum 27. September 2021 aufgehoben. Für unveränderte Altverträge endete die Übergangsmöglichkeit am 27. Dezember 2022 nach Artikel 4 Absatz 4 des Durchführungsbeschlusses (EU) 2021/914; Änderungen der Verarbeitung oder unzureichende Garantien konnten sie schon vorher entfallen lassen.
- **DPF-Validität:** Das EU-US Data Privacy Framework steht unter politischem Vorbehalt (vgl. Schrems II zur Vorgänger-Regelung). DPF-Eintrag auf data.privacyframework.gov vor Unterschrift prüfen.
- **TIA nur Formalie:** Eine TIA muss ehrliche Risikobewertung enthalten. Pauschal "Risiko akzeptabel" ohne Begründung genügt Art. 28 DSGVO und den EDSA-Empfehlungen 01/2020 nicht.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- **Berufsgeheimnisträger:** Bei Mandanten-AVVs (Kanzleien, Ärzte) muss der AVV § 203 StGB und § 43a Abs. 2 BRAO berücksichtigen – unzureichende Vertraulichkeitsklausel kann Strafbarkeit begründen.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei neuen EDSA-Leitlinien zur Auftragsverarbeitung, Änderungen des SCC-Beschlusses 2021/914/EU oder neuen DPF-Entwicklungen.

**Hinweis EDSA-Leitlinien zur Auftragsverarbeitung:** Die Endfassung der Leitlinien 07/2020 zu den Begriffen des Verantwortlichen und des Auftragsverarbeiters wurde am 7. Juli 2021 angenommen. Sie ist eine fachlich gewichtige, aber nicht bindende Orientierungshilfe. Die Rollen sind anhand der tatsächlichen Entscheidung über Zwecke und wesentliche Mittel zu bestimmen; Vertragsbezeichnungen allein entscheiden nicht.

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Vollständige TIA-Methodik und SCC-Modul-Auswahl-Matrix
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — DSFA bei Hochrisiko-AVV-Konstellationen

## Faktische Updates (Stand 05/2026)

- **EDSA Guidelines 07/2020 zu Verantwortlichen und Auftragsverarbeitern:** Die Endfassung ist eine nicht bindende, fachlich gewichtige Orientierungshilfe; bei der Rollenzuordnung berücksichtigen, aber nicht als Rechtsnorm behandeln. Quelle: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020-concepts-controller-and-processor-gdpr_en
- **EDSA Stellungnahme 22/2024 vom 9. Oktober 2024:** Der Verantwortliche muss Identität aller Auftragsverarbeiter und Unterauftragsverarbeiter verfügbar haben und ausreichende Garantien risikoadäquat prüfen. Er muss nicht ausnahmslos jeden Unterauftragsvertrag anfordern; Umfang und Nachweis der Kontrolle richten sich nach der konkreten Verarbeitung. Quelle: https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-222024-certain-obligations-following_en
- **Haftung nach Artikel 82 Absatz 4 DSGVO:** Die gesamtschuldnerische Außenhaftung mehrerer an derselben Verarbeitung Beteiligter folgt aus dem Verordnungstext. Sie nicht ohne verifizierte Fundstelle als besondere EuGH-Entscheidung ausgeben; Regress und Verantwortungsanteile nach Artikel 82 Absatz 5 getrennt prüfen.
- **EU-US-DPF-Status:** Vor jedem US-AVV-Abschluss DPF-Listing des Anbieters über dataprivacyframework.gov verifizieren. SCC bleiben als Fallback im AVV vorzusehen.
- **NIS-2-Lieferkette (Art. 21 NIS-2-RL):** Auftraggeber wichtiger / besonders wichtiger Einrichtungen müssen Cyber-Risiken in der Lieferkette beruecksichtigen — AVV mit IT-/Cloud-Dienstleistern entsprechend erweitern.

## Triage-Frage (Entscheidungsbaum AVV)

```
Prüfungsrichtung?
 Eingehender AVV (wir sind Verantwortlicher) → Prüfe: Weisungsrecht vollständig?
 Ausgehender AVV (wir sind Auftragsverarbeiter) → Prüfe: Pflichten Art. 28 Abs. 3 vollständig?
 Unklar → Richtungserkennung über Parteienbezeichnung und Weisungsklausel

Drittlandbezug?
 Nein → kein TIA erforderlich

Sub-AVs mit Drittlandexposure?
 Ja → Art. 28 Abs. 4 DSGVO: Pflichten vollständig übergeleitet?
 Nein → nur Listenpflicht und Wechselbenachrichtigung prüfen
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — AVV-Review-Ergebnis

**Adressat:** Datenschutzbeauftragter / Rechtsabteilung — Tonfall: sachlich-juristisch

```
AVV-Review [DATUM]
Dokument: [BEZEICHNUNG, VERSION]
Richtung: Verantwortlicher / Auftragsverarbeiter
Gesamt-Risiko: ROT / ORANGE / GELB / GRUEN

Pflichtklausel-Status (Art. 28 Abs. 3 DSGVO):
| Buchstabe | Inhalt | Status | Kommentar |
|-----------|----------------------------|--------|-----------|
| lit. a | Weisungsgebundenheit | | |
| lit. b | Vertraulichkeit | | |
| lit. c | TOM Art. 32 DSGVO | | |
| lit. d | Sub-AV-Regelung | | |
| lit. e | Unterstuetzung Betr.-R. | | |
| lit. f | Unterstuetzung Art. 32-36 | | |
| lit. g | Loeschung/Rueckgabe | | |
| lit. h | Audit-Recht | | |

Drittlandtransfer: ja / nein
TIA erforderlich: ja / nein
Empfehlung: Unterzeichnen / Mit Redlines / Ablehnen
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
