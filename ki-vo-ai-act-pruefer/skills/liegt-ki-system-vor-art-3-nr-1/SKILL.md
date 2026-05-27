---
name: liegt-ki-system-vor-art-3-nr-1
description: "Erster Schritt jeder KI-VO-Pruefung: Unternehmen fragt ob die eigene Software oder Anwendung ueberhaupt ein KI-System nach der KI-VO ist und ob die Verordnung gilt. Art. 3 Nr. 1 KI-VO Definition KI-System. Pruefraster: maschinengesteuertes System Autonomiegrad Inferenz aus Eingaben Ausgaben Vorhersagen Inhalte Empfehlungen Entscheidungen. EU-Kommissions-Leitlinien Februar 2025. Output: Einordnungsentscheidung mit Begruendung. Abgrenzung zu abgrenzung-konventionelle-software-vs-ki-system (Grenzfaelle) und triage-ki-vo-vorpruefung (Einstiegsinterview)."
---

# Liegt ein KI-System vor? — Art. 3 Nr. 1 KI-VO

## Zweck

Dies ist der wichtigste Qualifikationsschritt des gesamten Workflows. Ohne Vorliegen eines KI-Systems im Sinne von Art. 3 Nr. 1 KI-VO findet die Verordnung (EU) 2024/1689 keine Anwendung. Dieser Skill prüft die Tatbestandsmerkmale der Legaldefinition Schritt für Schritt.

## Normtext — Art. 3 Nr. 1 KI-VO (Kurzfassung)

Ein KI-System ist ein maschinengestütztes System, das für einen in unterschiedlichem Grad autonomen Betrieb ausgelegt ist, nach seiner Einführung anpassungsfähig sein kann und das aus den erhaltenen Eingaben für explizite oder implizite Ziele ableitet, wie es Ausgaben wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen generieren kann, die physische oder virtuelle Umgebungen beeinflussen.

## Tatbestandsmerkmale — Checkliste

### Merkmal 1: Maschinengestütztes System

Frage an den Nutzer: Wird das System von einer Maschine (Computer, Server, Edge-Gerät) betrieben?
- Ja → weiter zu Merkmal 2
- Nein → kein KI-System nach KI-VO; Workflow endet hier

### Merkmal 2: Autonomiegrad

Frage: Trifft das System selbstständig Entscheidungen oder Ausgaben ohne manuelle Einzelsteuerung für jeden Schritt?
- Vollautonomen Betrieb: klar erfüllt
- Partiell autonomen Betrieb (Vorschläge, Scoring, Ranking): in der Regel erfüllt
- Ausschließlich manuelle Steuerung jedes einzelnen Schritts: möglicherweise nicht erfüllt

### Merkmal 3: Anpassungsfähigkeit (optional, aber prüfpflichtig)

Frage: Kann das System sein Verhalten durch Training, Fine-Tuning oder Lernprozesse verändern?
- Ja → deutliches Indiz für KI-System
- Nein → schließt KI-System nicht aus; weiter mit Merkmal 4

### Merkmal 4: Ableitung aus Eingaben (Inferenz)

Frage: Leitet das System aus Eingaben (Daten, Signale, Text, Bilder, Sensordaten) Ausgaben ab, die über eine reine Datenweitergabe hinausgehen?
- Ja → weiter zu Merkmal 5
- Nein → möglicherweise kein KI-System; vgl. Abgrenzung unten

### Merkmal 5: Ausgabentypen

Welcher Typ von Ausgabe wird generiert?
- Vorhersagen (Prognosen, Scores, Wahrscheinlichkeiten) → erfüllt
- Inhalte (Text, Bilder, Audio, Video) → erfüllt
- Empfehlungen (Handlungsvorschläge, Rankings) → erfüllt
- Entscheidungen (Zulassung, Ablehnung, Klassifikation) → erfüllt

### Merkmal 6: Beeinflussung physischer oder virtueller Umgebungen

Frage: Können die Ausgaben reale Folgen für Personen oder Systeme haben?
- Ja → Merkmal erfüllt
- Die Beeinflussung muss nicht unmittelbar sein; mittelbare Wirkungen genügen.

## Abgrenzung — Wann liegt KEIN KI-System vor?

**Rein regelbasierte Software:** Ein Programm, das ausschließlich explizit vom Menschen programmierte Wenn-Dann-Regeln abarbeitet, ohne aus Daten zu lernen oder zu inferieren, ist kein KI-System. Beispiel: eine Steuerberechnungssoftware, die §-Normen deterministisch umsetzt.

**Einfache Automation:** Skripte oder Makros, die Daten formatieren, kopieren oder weiterleiten, ohne Ausgaben zu „ableiten", sind kein KI-System.

**Statistische Methoden ohne Inferenz:** Reine Deskriptivstatistik (Mittelwert, Summe, Histogramm) ohne Vorhersage- oder Empfehlungskomponente gilt nicht als KI-System. Sobald jedoch Regressionsmodelle, Clustering oder Klassifikatoren eingesetzt werden, ist die Grenze in der Regel überschritten.

**Expertensysteme und deterministische Logik:** Klassische Expertensysteme mit vollständig vom Menschen definierten Regeln fallen nach den Leitlinien der Kommission (Februar 2025) typischerweise nicht unter Art. 3 Nr. 1 KI-VO, wenn kein maschinelles Lernen und keine Inferenz aus Daten stattfindet.

## Leitlinien der Kommission (Februar 2025)

Die Kommission hat klargestellt, dass für die Qualifikation als KI-System entscheidend ist, ob das System eine Form von Inferenz — also das Ableiten von Ausgaben aus Eingaben — durchführt. Reine Suche, Filterung oder Datenbankabfrage reicht nicht. Maschinelles Lernen, Deep Learning, neuronale Netze, Bayes-Netze, Entscheidungswälder und ähnliche Methoden erfüllen das Kriterium typischerweise.

## Ergebnis und Routing

- **Alle sechs Merkmale erfüllt oder überwiegend erfüllt:** KI-System nach Art. 3 Nr. 1 KI-VO liegt vor → weiter zu `territorialer-anwendungsbereich-art-2`
- **Zweifelsfälle:** Das System weist auf Unsicherheit hin und empfiehlt juristische Klärung → vgl. `mandatsabbruch-empfehlung-komplexe-faelle`
- **Nicht erfüllt:** Kein KI-System; KI-VO findet keine Anwendung. Andere Rechtsgebiete können trotzdem relevant sein (DSGVO, Produktsicherheit).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 49: Automatisiertes Profiling als Art. 22 Abs. 1 DSGVO-Entscheidung wenn KI-Score massgebliche Grundlage fuer Drittentscheidung; Masstab fuer KI-Scoring-Systeme nach KI-VO.
- EuGH, Urt. v. 04.10.2024 — C-203/22 (Dun & Bradstreet), NJW 2025, 56 Rn. 38: Betreiber algorithmischer Entscheidungssysteme muss Entscheidungslogik verstaendlich offenlegen; Art. 13 KI-VO Transparenzpflicht.
- BGH, Urt. v. 19.06.2018 — VI ZR 184/17, NJW 2018, 2877 Rn. 15: Haftung bei automatisierten Informationssystemen — Organisationspflicht bei KI-Einsatz; massgeblich fuer Art. 26 KI-VO Betreiberpflichten.
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 87: Drittlandtransfer bei KI-Anbieter-APIs erfordert Schutzgarantien; massgeblich fuer Art. 28 DSGVO i.V.m. KI-VO Lieferkette.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 1 KI-VO — Definition KI-System
- Erwaegungsgrund 12 KI-VO — Abgrenzung zu regelbasierter Software
- Art. 2 KI-VO — Anwendungsbereich

## Triage zu Beginn
1. Ist das System maschinengestuetzt und fuer autonomen Betrieb ausgelegt?
2. Leitet das System aus Eingaben Ausgaben ab — Inferenz vorhanden?
3. Werden Vorhersagen, Empfehlungen, Entscheidungen oder Inhalte generiert?
4. Handelt es sich um rein regelbasierte Software ohne Lernkomponente?
5. Sind Leitlinien der Kommission (Februar 2025) auf diesen Fall anwendbar?

## Output-Template — KI-System-Qualifikation
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
KI-SYSTEM-QUALIFIKATION NACH ART. 3 NR. 1 KI-VO
[DATUM] — System: [SYSTEMNAME]

Tatbestandsmerkmal-Check:
☑/☐ Maschinengestuetzt
☑/☐ Autonomiegrad vorhanden
☑/☐ Anpassungsfaehig (optional)
☑/☐ Inferenz aus Eingaben
☑/☐ Ausgabetyp (Vorhersage / Inhalt / Empfehlung / Entscheidung)
☑/☐ Beeinflussung physischer oder virtueller Umgebungen

Ergebnis: [KI-SYSTEM NACH ART. 3 NR. 1 KI-VO LIEGT VOR / LIEGT NICHT VOR / ZWEIFELSFALL]
Naechster Schritt: [territorialer-anwendungsbereich-art-2 / mandatsabbruch-empfehlung-komplexe-faelle / KEINE KI-VO]
Geprueft: [NAME], [DATUM]
```
