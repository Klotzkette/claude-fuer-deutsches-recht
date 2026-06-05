---
name: risikoklassen-uebersicht-rolle-anbieter
description: "Risikoklassen Uebersicht Rolle Anbieter: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Risikoklassen Uebersicht Rolle Anbieter

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Risikoklassen Uebersicht Rolle Anbieter** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `risikoklassen-uebersicht-und-triage` | Schnelle Risikoklassen-Triage nach KI-VO mit Fokus auf Art. 6 Abs. 2 und Anhang III. Prueft verboten, Hochrisiko nach Art. 6 Abs. 1/2, Rueckausnahme Art. 6 Abs. 3, begrenztes Risiko Art. 50, GPAI und minimales Risiko. Behandelt allgemeine Chatbots/GPAI: nicht automatisch Hochrisiko, sondern zweck- und einsatzbezogen. Output: Risikoklassen-Erstdiagnose mit passenden Folge-Skills und Dokumentationshinweisen. |
| `rolle-anbieter-pruefen-art-3-nr-3` | Unternehmen das Software oder KI entwickelt fragt: Sind wir Anbieter im Sinne der KI-VO und welche Pflichten treffen uns deshalb? Art. 3 Nr. 3 KI-VO Anbieter-Definition. Prüfraster: Entwicklung oder Beauftragung Entwicklung Inverkehrbringen unter eigenem Namen Inbetriebnahme. Abgrenzung zu Betreiber Einführer Haendler. Output: Rollenentscheidung Anbieter ja/nein mit Begründung und Liste der Anbieter-Pflichten. Abgrenzung zu anbieter-werden-art-25 (Rollenwechsel) und persoenlicher-anwendungsbereich-rollen-art-3 (Übersicht). |
| `rolle-betreiber-pruefen-art-3-nr-4` | Unternehmen kauft oder lizenziert ein KI-System von einem Anbieter und fragt: Sind wir Betreiber im Sinne der KI-VO und was muessen wir tun? Art. 3 Nr. 4 KI-VO Betreiber-Definition. Prüfraster: Verwendung in eigener Verantwortung Abgrenzung zu persoenlicher nicht beruflicher Nutzung Abgrenzung zu Anbieter. Output: Rollenentscheidung Betreiber ja/nein und Liste der Betreiber-Pflichten. Abgrenzung zu betreiber-deployer-pflichten-art-26 (Detailpflichten) und anbieter-werden-art-25 (Rollenwechsel zu Anbieter). |
| `rueckausnahme-art-6-abs-3` | Prueft nach positiver Anhang-III-Zuordnung, ob ein KI-System ausnahmsweise nicht Hochrisiko ist. Art. 6 Abs. 3 KI-VO: kein erhebliches Risiko fuer Gesundheit, Sicherheit oder Grundrechte, vier enge Fallgruppen, Profiling-Sperre, Begruendungs- und Dokumentationspflicht nach Art. 6 Abs. 4. Besonders wichtig fuer allgemeine Assistenzsysteme, Chatbots und vorbereitende Tools in Personal, Justiz, Bildung, Kredit und Verwaltung. Output: begruendeter Rueckausnahme-Vermerk mit Risikobegruendung und Folge-Skills. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Risikoklassen Uebersicht Rolle Anbieter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `risikoklassen-uebersicht-und-triage`

**Fokus:** Schnelle Risikoklassen-Triage nach KI-VO mit Fokus auf Art. 6 Abs. 2 und Anhang III. Prueft verboten, Hochrisiko nach Art. 6 Abs. 1/2, Rueckausnahme Art. 6 Abs. 3, begrenztes Risiko Art. 50, GPAI und minimales Risiko. Behandelt allgemeine Chatbots/GPAI: nicht automatisch Hochrisiko, sondern zweck- und einsatzbezogen. Output: Risikoklassen-Erstdiagnose mit passenden Folge-Skills und Dokumentationshinweisen.

# Risikoklassen-Übersicht und Triage — KI-VO

## Zweck

Dieser Skill gibt eine schnelle, aber dokumentierbare Ersteinschätzung der KI-VO-Risikoklasse. Der Schwerpunkt liegt auf der richtigen Abzweigung zwischen allgemeinem KI-System/GPAI, begrenztem Risiko und Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III.

## Vorfrage: Ist es ein KI-System?

Wenn das nicht sicher ist, zuerst:
- `liegt-ki-system-vor-art-3-nr-1`
- bei Grenzfällen `abgrenzung-konventionelle-software-vs-ki-system`

## Reihenfolge der Risikoprüfung

### 1. Verbotene Praktiken nach Art. 5

Nur kurz screenen. Wenn ein Treffer möglich ist, in `verbotene-praktiken-art-5` vertiefen. Der Nutzer hat den Schwerpunkt hier nicht gesetzt, aber Art. 5 darf nicht übersehen werden.

### 2. Hochrisiko nach Art. 6 Abs. 1

Prüfe, ob das KI-System Sicherheitsbauteil eines Produkts ist oder selbst ein Produkt, das unter Anhang-I-Sektorrecht fällt und einer Dritt-Konformitätsbewertung unterliegt.

Weiter: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

### 3. Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III

Das ist der zentrale Praxisschritt.

Immer prüfen:
- konkrete Zweckbestimmung
- Betreiberzweck und tatsächlicher Organisationsgebrauch
- natürliche Personen oder kritische Infrastruktur betroffen?
- Entscheidungseinfluss: Zugang, Bewertung, Ranking, Priorisierung, Rechtsanwendung, Risiko, Leistung
- allgemeiner Chatbot/GPAI nur theoretisch nutzbar oder tatsächlich eingebettet?

Weiter: `hochrisiko-art-6-abs-2-anhang-iii`

### 4. Rückausnahme Art. 6 Abs. 3

Wenn Anhang III passt, nicht sofort stoppen. Prüfe eng:
- Profiling natürlicher Personen?
- erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte?
- eine der vier Fallgruppen?
- Dokumentation nach Art. 6 Abs. 4?

Weiter: `rueckausnahme-art-6-abs-3`

### 5. Begrenztes Risiko nach Art. 50

Prüfe insbesondere:
- Interaktion natürlicher Personen mit KI-System
- KI-generierte oder manipulierte Inhalte
- Deepfake-Kennzeichnung
- Emotionserkennung oder biometrische Kategorisierung, soweit nicht verboten/hochrisikorelevant

Weiter: `begrenztes-risiko-art-50-transparenzpflichten`

### 6. GPAI

Bei LLMs, Foundation Models, APIs und allgemeinen Chatbots:
- GPAI-Modell oder GPAI-System prüfen
- systemisches Risiko prüfen, falls Modellanbieter betroffen
- Hochrisiko nur bei konkreter Anhang-III-Zweckbestimmung

Weiter: `gpai-vorliegen-art-3-nr-63`

### 7. Minimales Risiko

Wenn keine der obigen Kategorien greift:
- KI-VO-Restpflichten prüfen, insbesondere Art. 4 KI-Kompetenz, interne Governance, Datenschutz, Berufsrecht, Urheberrecht, Produktsicherheit.
- Negativdiagnose dokumentieren.

Weiter: `nicht-hochrisiko-bestaetigt-end-to-end-roadmap`

## Chatbot-/GPAI-Leitsatz

Ein allgemeiner Chatbot ist nicht deshalb Hochrisiko, weil er technisch in Hochrisiko-Bereichen einsetzbar wäre. Entscheidend ist, ob Anbieter oder Betreiber ihn für einen Anhang-III-Zweck bestimmen, integrieren, erlauben, systematisch dulden oder durch fehlende Kontrollen naheliegenden Hochrisiko-Fehlgebrauch nicht beherrschen.

## Output-Template — Risikoklassen-Erstdiagnose

```text
RISIKOKLASSEN-ERSTDIAGNOSE KI-VO
Datum: [DATUM]
System: [NAME]

1. KI-System-Status
[Ja/Nein/Unklar] — [Begründung oder Verweis]

2. Zweck und Nutzung
[Anbieter-Zweck, Betreiber-Zweck, tatsächliche Nutzung, Off-label-Risiken]

3. Risiko-Screening
- Art. 5 Verbot: [Treffer/kein Treffer/unklar]
- Art. 6 Abs. 1: [Treffer/kein Treffer/unklar]
- Art. 6 Abs. 2/Anhang III: [Treffer/kein Treffer/unklar]
- Art. 6 Abs. 3 Rückausnahme: [prüfen/nicht einschlägig]
- Art. 50 begrenztes Risiko: [Treffer/kein Treffer/unklar]
- GPAI: [Modell/System/nein/unklar]

4. Vorläufiges Ergebnis
[verboten / Hochrisiko / nicht Hochrisiko wegen Rückausnahme / begrenztes Risiko / GPAI-Pflichten / minimales Risiko / offen]

5. Nächste Skills
[konkrete Skill-Reihenfolge]

6. Dokumentation
[Welche Tatsachen und Unterlagen fehlen? Welche Annahmen müssen belegt werden?]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3, 5, 6, 50, 51 bis 55 und Anhang III KI-VO. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `rolle-anbieter-pruefen-art-3-nr-3`

**Fokus:** Unternehmen das Software oder KI entwickelt fragt: Sind wir Anbieter im Sinne der KI-VO und welche Pflichten treffen uns deshalb? Art. 3 Nr. 3 KI-VO Anbieter-Definition. Prüfraster: Entwicklung oder Beauftragung Entwicklung Inverkehrbringen unter eigenem Namen Inbetriebnahme. Abgrenzung zu Betreiber Einführer Haendler. Output: Rollenentscheidung Anbieter ja/nein mit Begründung und Liste der Anbieter-Pflichten. Abgrenzung zu anbieter-werden-art-25 (Rollenwechsel) und persoenlicher-anwendungsbereich-rollen-art-3 (Übersicht).

# Rolle-Check: Anbieter — Art. 3 Nr. 3 KI-VO

## Zweck

Die Anbieter-Rolle begründet den umfangreichsten Pflichtenkatalog der KI-VO. Dieser Skill klärt durch einen Entscheidungsbaum, ob die Nutzer-Rolle als Anbieter qualifiziert.

## Legaldefinition — Art. 3 Nr. 3 KI-VO

Anbieter (provider) ist eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System oder ein GPAI-Modell entwickelt oder entwickeln lässt und dieses KI-System oder GPAI-Modell unter ihrem eigenen Namen oder ihrer eigenen Marke — entgeltlich oder unentgeltlich — in Verkehr bringt oder in Betrieb nimmt.

## Entscheidungsbaum

### Schritt 1 — Entwicklung

**Frage A:** Haben Sie selbst das KI-System entwickelt (Eigenentwicklung) oder haben Sie jemanden damit beauftragt (Auftragsentwicklung)?

- Eigenentwicklung → weiter zu Schritt 2
- Auftragsentwicklung (Dritter entwickelt, aber nach Ihren Vorgaben) → weiter zu Schritt 2
- Sie nutzen ein fertiges, unmodifiziertes Drittsystem → Sie sind kein Anbieter im Sinne von Art. 3 Nr. 3 KI-VO; weiter zu `rolle-betreiber-pruefen-art-3-nr-4`

**Hinweis zu Auftragsentwicklung:** Wenn Sie als Auftraggeber die wesentlichen Spezifikationen vorgeben und das System unter Ihrem Namen in Verkehr bringen, sind Sie Anbieter — nicht der beauftragte Entwickler. Der Auftragnehmer kann ebenfalls Anbieter sein, wenn er das System eigenständig gestaltet und unter eigenem Namen verbreitet.

### Schritt 2 — Inverkehrbringen unter eigenem Namen

**Frage B:** Bringen Sie das System unter Ihrem eigenen Namen oder Ihrer eigenen Marke in Verkehr?

- Ja → starkes Indiz für Anbieter-Rolle; weiter zu Schritt 3
- Nein (Sie stellen das System dem Auftraggeber bereit, der es unter eigenem Namen vermarktet) → Sie sind möglicherweise nur Auftragsentwickler ohne Anbieter-Status; der Auftraggeber ist Anbieter

**Variante "in Betrieb nehmen":** Auch wer ein KI-System nicht vermarktet, sondern selbst in eigenen Prozessen erstmals einsetzt (Inbetriebnahme), gilt als Anbieter — z.B. ein Unternehmen, das ein intern entwickeltes System für die eigene Personalentscheidung nutzt.

**Prüffragen:**
- Erscheint Ihr Unternehmensname auf der Produktseite, in der Gebrauchsanweisung oder im Vertrag als Anbieter des KI-Systems?
- Tragen Sie das wirtschaftliche Risiko des Systems?

### Schritt 3 — Entgeltlichkeit oder Unentgeltlichkeit

**Frage C:** Spielt die Frage, ob Sie das System entgeltlich oder unentgeltlich bereitstellen, eine Rolle?

Nein — Art. 3 Nr. 3 KI-VO gilt ausdrücklich für entgeltliche und unentgeltliche Bereitstellung. Auch kostenlose KI-Systeme, Open-Source-Systeme (soweit nicht unter Art. 2 Abs. 12 KI-VO ausgenommen) und intern genutzte Systeme können unter die Anbieter-Definition fallen.

## Ergebnis

**Anbieter bestätigt, wenn:**
- Sie das System entwickelt oder entwickeln lassen haben UND
- Sie es unter eigenem Namen in Verkehr bringen oder in Betrieb nehmen

**Folge-Skills:**
- Wenn Hochrisiko: → Alle Pflichten Art. 9 bis 15, Art. 16 bis 19, Art. 43 bis 49, Art. 49 und 71 KI-VO
- Wenn GPAI-Modell: → Art. 51 bis 55 KI-VO
- Wenn begrenztes Risiko: → Art. 50 KI-VO (Transparenzpflichten)
- Rollenwechsel möglich: Wenn Sie später das System wesentlich verändern oder unter neuem Namen herausbringen → Art. 25 KI-VO → `anbieter-werden-art-25`

## Wichtige Fallstricke

**Fallstrick 1 — Interne Systeme:** Auch wer ein KI-System nur für interne Zwecke entwickelt und einsetzt, kann Anbieter sein. Die Anbieter-Rolle erfordert kein Angebot an Dritte.

**Fallstrick 2 — Fine-Tuning:** Wer ein fremdes Grundmodell mit eigenen Daten feinabstimmt und das resultierende System unter eigenem Namen in Verkehr bringt, ist Anbieter.

**Fallstrick 3 — Open-Source-Ausnahmen:** Die Open-Source-Ausnahme nach Art. 2 Abs. 12 KI-VO gilt nur unter engen Voraussetzungen; Hochrisiko-Systeme und Systeme mit systemischem Risiko sind nicht ausgenommen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — ROLLE ANBIETER PRUEFEN ART 3 NR 3
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 3 Nr. 3 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 3. `rolle-betreiber-pruefen-art-3-nr-4`

**Fokus:** Unternehmen kauft oder lizenziert ein KI-System von einem Anbieter und fragt: Sind wir Betreiber im Sinne der KI-VO und was muessen wir tun? Art. 3 Nr. 4 KI-VO Betreiber-Definition. Prüfraster: Verwendung in eigener Verantwortung Abgrenzung zu persoenlicher nicht beruflicher Nutzung Abgrenzung zu Anbieter. Output: Rollenentscheidung Betreiber ja/nein und Liste der Betreiber-Pflichten. Abgrenzung zu betreiber-deployer-pflichten-art-26 (Detailpflichten) und anbieter-werden-art-25 (Rollenwechsel zu Anbieter).

# Rolle-Check: Betreiber — Art. 3 Nr. 4 KI-VO

## Zweck

Die Betreiber-Rolle ist die zweithäufigste Rolle in der KI-Wertschöpfungskette. Dieser Skill klärt durch einen Entscheidungsbaum, ob die Nutzer-Rolle als Betreiber qualifiziert.

## Legaldefinition — Art. 3 Nr. 4 KI-VO

Betreiber (deployer) ist eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System in eigener Verantwortung verwendet, es sei denn, das KI-System wird im Rahmen einer persönlichen, nicht beruflichen Tätigkeit verwendet.

## Entscheidungsbaum

### Schritt 1 — Verwendung eines fremden KI-Systems?

**Frage A:** Nutzen Sie ein KI-System, das nicht von Ihnen entwickelt wurde, und haben Sie es nicht wesentlich verändert?

- Ja → weiter zu Schritt 2
- Nein (eigene Entwicklung oder wesentliche Veränderung) → möglicherweise Anbieter; → `rolle-anbieter-pruefen-art-3-nr-3` oder `anbieter-werden-art-25`

### Schritt 2 — Verwendung in eigener Verantwortung

**Frage B:** Verwenden Sie das System in eigener Verantwortung — das heißt, Sie entscheiden selbst über Einsatzzweck, Bedingungen und Kontext?

- Ja → weiter zu Schritt 3
- Nein (Sie agieren ausschließlich als technischer Dienstleister für einen Dritten, der alle Entscheidungen trifft) → möglicherweise kein Betreiber; Klärung erforderlich

### Schritt 3 — Ausnahme: Persönliche, nicht berufliche Nutzung

**Frage C:** Handelt es sich um eine ausschließlich persönliche, nicht berufliche Nutzung?

- Nein (berufliche, gewerbliche, behördliche Nutzung) → Betreiber-Rolle bestätigt
- Ja (rein private Nutzung durch natürliche Person) → kein Betreiber; KI-VO gilt nicht (Art. 2 Abs. 10 KI-VO)

**Grenzfälle:**
- Freelancer, Selbstständige, Freiberufler, die das System für ihre Arbeit nutzen → Betreiber (nicht rein privat)
- Unternehmen, das das System für interne Prozesse nutzt → Betreiber
- Öffentliche Stellen, die das System für ihre Aufgaben nutzen → Betreiber (mit verschärften Pflichten nach Art. 27 KI-VO)

## Ergebnis

**Betreiber bestätigt, wenn:**
- Sie ein fremdes (nicht selbst entwickeltes, nicht wesentlich verändertes) KI-System nutzen UND
- die Nutzung in eigener Verantwortung erfolgt UND
- die Nutzung nicht ausschließlich privat ist

## Pflichten als Betreiber (Überblick)

Bei Hochrisiko-KI:
- Bestimmungsgemäße Verwendung nach Gebrauchsanweisung des Anbieters (Art. 26 Abs. 1 KI-VO)
- Menschliche Aufsicht sicherstellen (Art. 26 Abs. 2 KI-VO)
- Eingabedaten-Qualität sicherstellen (Art. 26 Abs. 3 KI-VO)
- Protokollaufbewahrung sechs Monate (Art. 26 Abs. 6 KI-VO)
- Informationspflicht gegenüber betroffenen Personen (Art. 26 Abs. 7 KI-VO)
- Meldung schwerwiegender Vorfälle an Anbieter (Art. 26 Abs. 5 KI-VO)
- Grundrechte-Folgenabschätzung für öffentliche Stellen und bestimmte Privatbetreiber (Art. 27 KI-VO)

Detail: → `betreiber-deployer-pflichten-art-26`

## Wann wird der Betreiber zum Anbieter?

Wenn der Betreiber:
- Das System unter eigenem Namen vermarktet
- Das System wesentlich verändert (technisch, im Einsatzzweck, in der Zielgruppe)
- Einen bestimmungsgemäßen Zweck hinzufügt, der sich erheblich vom ursprünglichen unterscheidet

→ dann greift Art. 25 KI-VO: Betreiber wird zum Anbieter → `anbieter-werden-art-25`

## Betreiber und GPAI-Systeme

Wer ein GPAI-System (z.B. einen Chatbot auf Basis eines Foundation-Modells) als Betreiber einsetzt, unterliegt in der Regel den Betreiber-Pflichten nach Art. 26 KI-VO. Die KI-VO-Pflichten des GPAI-Modell-Anbieters liegen beim Modellanbieter — aber der Betreiber muss sicherstellen, dass er das System bestimmungsgemäß einsetzt.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — ROLLE BETREIBER PRUEFEN ART 3 NR 4
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 3 Nr. 4 Rn. 6]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 4. `rueckausnahme-art-6-abs-3`

**Fokus:** Prueft nach positiver Anhang-III-Zuordnung, ob ein KI-System ausnahmsweise nicht Hochrisiko ist. Art. 6 Abs. 3 KI-VO: kein erhebliches Risiko fuer Gesundheit, Sicherheit oder Grundrechte, vier enge Fallgruppen, Profiling-Sperre, Begruendungs- und Dokumentationspflicht nach Art. 6 Abs. 4. Besonders wichtig fuer allgemeine Assistenzsysteme, Chatbots und vorbereitende Tools in Personal, Justiz, Bildung, Kredit und Verwaltung. Output: begruendeter Rueckausnahme-Vermerk mit Risikobegruendung und Folge-Skills.

# Rückausnahme vom Hochrisiko — Art. 6 Abs. 3 KI-VO

## Zweck

Dieser Skill wird nur genutzt, wenn zuvor ein Anhang-III-Tatbestand nach Art. 6 Abs. 2 KI-VO möglich oder wahrscheinlich ist. Er prüft, ob das System ausnahmsweise nicht als Hochrisiko-KI-System gilt, weil es kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte darstellt und in eine der eng auszulegenden Fallgruppen fällt.

Der Skill ist besonders wichtig bei allgemeinen Assistenzsystemen, LLM-Tools, Chatbots und Dokumentationshilfen, die in sensiblen Bereichen eingesetzt werden, aber nur vorbereitende oder eng begrenzte Aufgaben erfüllen sollen.

## Prüfungsreihenfolge

1. Anhang-III-Treffer konkret benennen.
2. Profiling natürlicher Personen ausschließen.
3. Erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte bewerten.
4. Eine der vier Fallgruppen prüfen.
5. Tatsächliche Nutzung und vorhersehbaren Fehlgebrauch gegen die behauptete Rückausnahme halten.
6. Dokumentationspflicht nach Art. 6 Abs. 4 vorbereiten.

## Sperre: Profiling natürlicher Personen

Wenn das System Profiling natürlicher Personen vornimmt, greift die Rückausnahme nicht.

Prüfe:
- Werden personenbezogene Daten automatisiert verarbeitet?
- Werden persönliche Aspekte bewertet, analysiert oder vorhergesagt?
- Geht es um Leistung, wirtschaftliche Lage, Gesundheit, Präferenzen, Interessen, Zuverlässigkeit, Verhalten, Aufenthaltsort oder Bewegung?
- Hat der Output individualisierende Wirkung?

Bei Bewerberranking, Beschäftigtenbewertung, Kredit-Scoring, individueller Risikobewertung, Eignungsbewertung oder personalisiertem Leistungsmonitoring ist die Profiling-Sperre besonders sorgfältig zu prüfen.

## Erhebliches Risiko

Die Rückausnahme setzt voraus, dass das System kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte darstellt. Nicht nur technische Sicherheit zählt, sondern auch Gleichbehandlung, Datenschutz, Menschenwürde, Zugang zu Leistungen, Bildung, Arbeit, Rechtsschutz und effektiver menschlicher Kontrolle.

Risikofaktoren:
- Output beeinflusst Zugang, Ablehnung, Priorität, Score, Ranking oder Sanktion.
- Betroffene können Output kaum erkennen, bestreiten oder korrigieren.
- Menschliche Kontrolle ist nur formal oder faktisch überfordert.
- Datenqualität, Bias, Halluzinationen oder Fehlklassifikationen können Personen treffen.
- Nutzung erfolgt in Machtasymmetrie: Arbeitgeber, Schule, Behörde, Bank, Versicherung, Gericht.
- Off-label-Nutzung ist naheliegend und nicht wirksam abgesichert.

## Vier Fallgruppen

### 1. Enge Verfahrensaufgabe

Das System führt eine eng begrenzte Verfahrensaufgabe aus und hat keinen wesentlichen Einfluss auf das Ergebnis der Entscheidung.

Beispiele:
- Vollständigkeitsprüfung eines Formulars
- Erkennung fehlender Anlagen
- Termin- oder Fristenhinweis ohne Bewertung des Anspruchs

Nicht ausreichend:
- "nur Vorprüfung", wenn die Vorprüfung praktisch über Weiterleitung, Ablehnung oder Ranking entscheidet
- automatische Priorisierung von Personenfällen mit realer Entscheidungswirkung

### 2. Verbesserung einer bereits abgeschlossenen menschlichen Tätigkeit

Das System verbessert das Ergebnis einer zuvor von einem Menschen erbrachten Tätigkeit, ohne dieses Ergebnis wesentlich zu verändern oder zu ersetzen.

Beispiele:
- sprachliche Glättung eines bereits entschiedenen Bescheids
- Barrierefreiheits- oder Lesbarkeitsverbesserung ohne Inhaltsänderung
- Formatierung, Übersetzung oder Zusammenfassung zur Nachvollziehbarkeit

Nicht ausreichend:
- das System schreibt die eigentliche Bewertung, Begründung oder Entscheidung
- der Mensch übernimmt die KI-Ausgabe regelmäßig ungeprüft

### 3. Mustererkennung ohne Ersetzung oder Beeinflussung menschlicher Bewertung

Das System erkennt Entscheidungsmuster oder Abweichungen von früheren Entscheidungsmustern, ohne eine bereits abgeschlossene menschliche Bewertung zu ersetzen oder zu beeinflussen.

Beispiele:
- Qualitätskontrolle, die auffällige Abweichungen für interne Audit-Zwecke markiert
- statistische Konsistenzprüfung ohne Einfluss auf Einzelfallentscheidung

Nicht ausreichend:
- Anomaliehinweis löst faktisch Ablehnung, Eskalation oder Benachteiligung aus
- System gibt einen Risikoscore aus, der die menschliche Bewertung prägt

### 4. Vorbereitende Aufgabe

Das System bereitet eine Bewertung vor, die für einen Anhang-III-Zweck relevant ist, ohne selbst die bewertungsrelevanten Aspekte zu beurteilen.

Beispiele:
- Dokumente sortieren, OCR, Dubletten erkennen
- Akten chronologisch strukturieren
- Lebenslaufdaten in Felder übertragen, ohne Eignung zu bewerten

Nicht ausreichend:
- das System extrahiert nicht nur, sondern bewertet Eignung, Glaubhaftigkeit, Risiko, Bedürftigkeit, Leistung oder Rechtsfolge
- die vorbereitende Ausgabe wird als Empfehlung oder Entscheidungsvorschlag genutzt

## Allgemeiner Chatbot im sensiblen Bereich

Bei ChatGPT-ähnlichen oder GPAI-basierten Tools:

- Reine Textentwürfe, Zusammenfassungen oder Übersetzungen können unter die Rückausnahme fallen, wenn sie keine individuelle Bewertung steuern.
- Prompt-Vorlagen wie "bewerte die Eignung", "ranke Bewerber", "prognostiziere Prozessrisiko für Richter", "entscheide Leistungsanspruch" sprechen gegen die Rückausnahme.
- Wenn die Fachabteilung das Tool faktisch für Bewertungen nutzt, reicht eine schöne Richtlinie allein nicht. Prüfe Nutzung, Logs, Schulung, Freigabe und Kontrollen.

## Dokumentationspflicht nach Art. 6 Abs. 4

Wenn ein Anbieter ein Anhang-III-System wegen Art. 6 Abs. 3 nicht als Hochrisiko einstuft, ist die Bewertung vor dem Inverkehrbringen oder der Inbetriebnahme zu dokumentieren. Die Dokumentation muss belastbar genug sein, um sie zuständigen Behörden auf Anfrage vorzulegen.

Dokumentieren:
- Anhang-III-Tatbestand
- konkrete Zweckbestimmung
- warum kein erhebliches Risiko besteht
- welche Fallgruppe greift
- warum kein Profiling natürlicher Personen vorliegt
- welche Kontrollen Fehlgebrauch verhindern
- Re-Evaluation-Trigger

## Ergebnis und Routing

- **Rückausnahme greift wahrscheinlich:** `nicht-hochrisiko-bestaetigt-end-to-end-roadmap`, zusätzlich Art. 50, GPAI und Art. 4 prüfen.
- **Rückausnahme greift nicht:** `hochrisiko-bestaetigt-end-to-end-roadmap`.
- **Fehlgebrauch oder Zweckänderung unklar:** `betreiber-deployer-pflichten-art-26`, `anbieter-werden-art-25`, ggf. `mandatsabbruch-empfehlung-komplexe-faelle`.

## Output-Template — Rückausnahme-Vermerk

```text
RUECKAUSNAHME-VERMERK — ART. 6 ABS. 3 KI-VO
Datum: [DATUM]
System: [NAME]
Anhang-III-Treffer: [NR. / BEREICH / KONKRETER TATBESTAND]

1. Profiling-Sperre
[Profiling natürlicher Personen: JA/NEIN/UNKLAR]
[Begründung]

2. Erhebliches Risiko
[Gesundheit/Sicherheit/Grundrechte betroffen?]
[Wirkpfad, betroffene Personen, Entscheidungseinfluss, Kontrollen]

3. Fallgruppe
[enge Verfahrensaufgabe / Verbesserung menschlicher Tätigkeit / Mustererkennung / vorbereitende Aufgabe / keine]

4. Tatsächliche Nutzung und Fehlgebrauch
[Zweckbestimmung, Richtlinie, Logs, Schulung, technische Sperren, bekannte Abweichungen]

5. Ergebnis
[Rückausnahme greift wahrscheinlich / greift nicht / offen]

6. Dokumentations- und Re-Evaluation-Punkte
[Was muss in der Art. 6 Abs. 4-Dokumentation stehen? Wann neu prüfen?]

7. Nächster Skill
[nicht-hochrisiko-bestaetigt-end-to-end-roadmap / hochrisiko-bestaetigt-end-to-end-roadmap / betreiber-deployer-pflichten-art-26 / anbieter-werden-art-25]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 6 Abs. 3 und 4 KI-VO, Art. 3 Nr. 12/13/23 KI-VO und Anhang III. Keine Rechtsberatung; die Rückausnahme ist eng und tatsachenabhängig.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
