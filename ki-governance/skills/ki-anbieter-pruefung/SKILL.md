---
name: ki-anbieter-pruefung
description: "Prüft KI-Anbieterverträge gegen die unternehmenseigenen Governance- Positionen; kennzeichnet Training auf Daten, Haftung, Modelländerungen und KI-Richtlinien-Konsistenz. Unterscheidet Anbieter/Betreiber-Rolle nach Art. 3 KI-VO; prüft Vertragspflichten nach Art. 25 KI-VO. Lädt, wenn der Nutzer „KI-Vertrag prüfen\", „Anbietervertrag KI\", „AI Act Art. 25 Vertragspflichten\" oder „KI-AGB prüfen\" sagt."
---

# KI-Anbieterprüfung

## Zweck

KI-Anbieterverträge sind der Ort, an dem Governance-Positionen tatsächlich
auf die Probe gestellt werden. Das Erstgespräch erfasst, was das Unternehmen
*will*. Diese Skill prüft, was es *vereinbart hat*.

Blickwinkel: Wir sind Betreiber/Käufer. Kein Rollenwechsel.

**AI Act Art. 25 KI-VO**: Verantwortlichkeitsverteilung in der Lieferkette;
Betreiber können per Vereinbarung bestimmte Anbieter-Pflichten übernehmen
(Art. 25 Abs. 1 KI-VO). Art. 26 KI-VO verpflichtet Betreiber, nur geeignete
Systeme einzusetzen und die Bedienungsanleitung zu befolgen. Beide Punkte
müssen im Vertrag explizit geregelt sein.

Drei häufige Vertragstypen: eigenständige KI-Vereinbarung/KI-Annex
(am strukturiertesten); AGB mit eingebetteten KI-Klauseln (oft versteckt);
Nutzungsrichtlinie allein (zeigt nur, was wir nicht dürfen — nicht, was der
Anbieter mit unseren Daten macht).

## Eingaben

- KI-Vertrag, KI-Annex oder AGB-KI-Abschnitt (Datei oder eingefügter Text)
- Praxisprofil aus `CLAUDE.md` (Anbieter-Governance-Positionen, KI-Richtlinien-
  Verpflichtungen, Anwendungsfall-Register)
- Anbieter-Name und Verwendungszweck

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 3 Nr. 3/4 KI-VO**: Definitionen Anbieter/Betreiber; maßgeblich
  für Pflichtenzuordnung.
- **AI Act Art. 25 KI-VO**: Verantwortlichkeiten in der Lieferkette; vertragliche
  Pflichten-Übertragung; Betreiber darf keine Art. 5-Verbote veranlassen
  (Art. 25 Abs. 2 KI-VO).
- **AI Act Art. 26/29 KI-VO**: Betreiberpflichten (Eignung prüfen, Anleitung
  befolgen, menschliche Aufsicht sicherstellen, Protokollierung).
- **DSGVO Art. 28**: AVV-Pflichten bei KI-Auftragsverarbeitung; Prüfungsrecht
  Art. 28 Abs. 3 lit. h DSGVO.
- **GeschGehG §§ 2, 4**: Eingabe vertraulicher Daten in externe KI kann
  Geheimnisschutz gefährden, wenn Anbieter für Training nutzt.
- **BGB §§ 305 ff. (§ 307)**: AGB-Kontrolle; unangemessene
  Haftungsbeschränkungen können unwirksam sein.
- **Produkthaftungs-RL 2024/2853/EU**: KI-Systeme als Produkte; relevant bei
  Haftungsklauseln im Anbietervertrag.
- **UrhG § 44b**: Text-und-Data-Mining-Schranke; relevant bei Training auf
  lizenzierten Inhalten.

**Leitentscheidungen**

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 (Schufa-Score):
  Vertragsgestaltung muss DSGVO Art. 22 Widerspruchs- und Prüfungsrechte
  operationalisieren.
- BGH, Urt. v. 17.05.2018 – VII ZR 157/17, NJW 2018, 2412: AGB-Kontrolle
  von Haftungsausschlüssen bei komplexen IT-Systemen; Maßstab für KI-
  Anbieter-Haftungsklauseln.
- BGH, Urt. v. 25.03.2021 – I ZR 37/20, GRUR 2021, 896: GeschGehG-
  Anforderungen an Vertragsgestaltung zum Schutz von Geschäftsgeheimnissen.
- BAG, Urt. v. 26.08.2021 – 8 AZR 253/20, NZA 2022, 1: Datenschutz bei
  Datenübermittlung an externe Dienstleister; übertragbar auf KI-AVV.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 25 Rn. 5
  (Verantwortlichkeitsverteilung; vertragliche Pflichten-Übertragung; Doppelautoren-Kommentar).
- Hoffmann, in: Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
  Teil IV Rn. 120 (Vertragsgestaltung bei KI-Diensten).
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 80 (AGB-Kontrolle
  bei IT-/Softwareverträgen; KI-Haftungsklauseln).
- Bertermann, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 28 Rn. 30.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Playbook und Stack klären**

`CLAUDE.md` → `## KI-Anbieter-Governance` und `## KI-Richtlinien-Verpflichtungen`.

KI-Stack kartieren vor Klausel-Prüfung:
1. End-User-SaaS (z. B. Legal-Tech-Tool)
2. API-Gateway/Orchestrierung (z. B. Azure OpenAI, AWS Bedrock, Vertex)
3. Modellanbieter (z. B. Anthropic, OpenAI, Google)
4. Wissensbasis/RAG-Quelle
5. Weitere Unterauftragnehmer

Bei gestapelten Anbietern: beide Vertragswerke prüfen. Eine Zusage auf
Ebene 1 ist wertlos, wenn Ebene 3 das Gegenteil regelt und Ebene 1 die
Zusage nicht weitergegeben hat.

**Schritt 2 — Klausel-für-Klausel-Prüfung**

| Klausel | Anbieter sagt | Unsere Position | Lücke | Schweregrad |
|---|---|---|---|---|
| Training auf unseren Daten | | | | |
| Vertraulichkeit der Eingaben | | | | |
| Modelländerungen | | | | |
| Ausgabe-IP / Rücklizenz | | | | |
| Haftung für Ausgaben (§ 307 BGB) | | | | |
| Vorfallbenachrichtigung | | | | |
| Menschliche Überprüfungsrechte | | | | |
| Nutzungsbeschränkungen | | | | |
| Prüfrechte / SOC 2 (Art. 28 Abs. 3 lit. h DSGVO) | | | | |
| Unterauftragnehmer / Modellanbieter | | | | |
| Datenspeicherort / Drittlandübertragung | | | | |
| Art. 25 KI-VO — Pflichten-Zuordnung | | | | |

Schweregrad (gegen CLAUDE.md-Positionen):
- ✅ **Aligned** — Standard oder besser
- ⚠️ **Hinweis** — innerhalb Fallback, schlechter als Standard
- 🟠 **Erheblich** — außerhalb Standard, innerhalb Fallback; Redline nötig
- ❌ **Kritisch** — außerhalb Fallback; Eskalation; kein Einsatz ohne Klärung

**Weitergabetest** bei gestapelten Anbietern: Vertrag auf Flow-Down-Klauseln
prüfen. Bei fehlender Weitergabe: konkrete Redline produzieren:
> „Ergänzen in § [X]: Anbieter stellt sicher, dass Unterauftragnehmer
> Pflichten zu [Datennutzung/Training/Vertraulichkeit] eingehen, die nicht
> weniger schützend sind als diese Vereinbarung."

**Schritt 3 — KI-Annex-Lückenprüfung**

AVV vorhanden, aber kein KI-Annex → kennzeichnen: bei Standard-Tier
tolerierbar; bei erhöhter/hoher Stufe ein ❌-Blocker (keine Regelung zu
Training, Modelländerungen, Art. 25 KI-VO, Haftung).

Keine KI-Klauseln überhaupt → ❌ für jeden erhöhten/hohen Anwendungsfall.

**Schritt 4 — KI-Richtlinien-Konsistenzprüfung**

Häufige Konflikte: Unsere Richtlinie verbietet Training → Anbieter erlaubt
es standardmäßig; unsere Richtlinie verlangt Human-Review → Anbieter-
Ausgaben sind final; Anbieter nicht auf Freigabeliste; DSGVO Art. 22
Widerspruchsrecht nicht operationalisiert. Jeden Widerspruch kennzeichnen.

**Schritt 5 — Redline-Granularität**

So klein wie möglich. Wort → Phrase → Unterklausel → Satz → Klausel.
Chirurgische Redlines signalisieren: wir haben sorgfältig gelesen.

## Ausgabeformat

```markdown
# KI-Anbieterprüfung: [Anbietername]
Geprüftes Dokument: [Typ] | Datum: [heute]
Anwendungsfall(e): [Zweck] | Governance-Stufe: [Standard/Erhöht/Hoch]

## Ergebnis
[2 Sätze: Können wir einsetzen? Was muss sich zuerst ändern?]
Befunde: [N]❌ [N]🟠 [N]⚠️ [N]✅

## Klausel-für-Klausel [Tabelle gem. Schritt 2]
## KI-Annex-Status [Vorhanden/Fehlend + Konsequenz]
## KI-Richtlinien-Konsistenz [✅/⚠️ Liste]
## Empfohlene Redlines [konsolidiert; vor Übermittlung mit Anwalt abstimmen]
## Wenn der Anbieter nicht nachgibt [Fallback oder Eskalation je Punkt]
```

Bei Nicht-Jurist-Rolle vor Unterzeichnungsempfehlung: anwaltliche Prüfung
abfragen; 1-seitigen Kurzüberblick generieren.

## Beispiel

**Anfrage:** „OpenAI Enterprise für interne Rechtsrecherche prüfen."
**Vorgehen:** Stack: OpenAI ist Modell- und SaaS-Ebene in einem.
Training: OpenAI Enterprise sieht kein Training auf Eingaben vor —
bestätigen; GeschGehG prüfen. Haftung: AGB-Ausschluss → § 307 BGB prüfen.
Art. 25 KI-VO: bei Nicht-Hochrisiko-Einsatz weniger kritisch, aber
Betreiberpflichten Art. 26/29 dokumentieren. AVV: DSGVO Art. 28 prüfen.

## Risiken und typische Fehler

- Training-auf-Daten-Klausel ist die am häufigsten übersehene: nie aus
  Reputation annehmen; in Schriftform bestätigen lassen.
- Stack nicht kartieren: modern KI ist geschichtet; nur die Oberfläche zu
  prüfen ist der häufigste Fehler.
- Nutzungsrichtlinie mit Datennutzungsklausel verwechseln: AUP ≠ Data Terms.
- Verlängerungen als Hebel nutzen: Lücken jetzt dokumentieren.

## Quellenpflicht

- **AI Act Art. 3 Nr. 3/4, Art. 25, Art. 26/29** — VO (EU) 2024/1689.
- **DSGVO Art. 28** bei Auftragsverarbeitung.
- **GeschGehG § 2 Nr. 1** bei Training-auf-Daten.
- **BGB §§ 305 ff. (§ 307)** bei AGB-Haftungsklauseln.
- **EuGH C-634/21 (Schufa-Score)** bei Scoring-/Entscheidungssystemen.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 25 Rn. 5** (Doppelautoren-Kommentar).
- **Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 80.**
- **Bertermann, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 28 Rn. 30.**
