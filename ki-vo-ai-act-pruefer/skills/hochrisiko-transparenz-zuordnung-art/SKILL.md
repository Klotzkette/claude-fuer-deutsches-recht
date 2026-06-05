---
name: hochrisiko-transparenz-zuordnung-art
description: "Hochrisiko Transparenz Zuordnung ART: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Hochrisiko Transparenz Zuordnung ART

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Hochrisiko Transparenz Zuordnung ART** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13` | Anbieter von Hochrisiko-KI fragt: Welche Informationen muessen wir dem Betreiber in der Gebrauchsanweisung zur Verfuegung stellen? Art. 13 KI-VO Transparenz und Informationspflichten. Prüfraster: Gebrauchsanweisung Mindestinhalt Art. 13 Abs. 3 Systembeschreibung Zweck Genauigkeitsmetriken Risiken menschliche Aufsicht Verstaendlichkeitsanforderungen Sprachanforderungen Aktualisierungspflichten. Output: Vorlage Gebrauchsanweisung Hochrisiko-KI. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (interne Doku) und begrenztes-risiko-art-50-transparenzpflichten (Endnutzer-Transparenz). |
| `hochrisiko-zuordnung-art-6-und-anhang-i-iii` | Gesamtuebersicht zur Hochrisiko-Zuordnung nach Art. 6 KI-VO: Art. 6 Abs. 1 Sicherheitsbauteil/Anhang I und Art. 6 Abs. 2/Anhang III. Erklaert Zweckbestimmung, allgemeine Chatbots/GPAI, Mitarbeitenden-Fehlgebrauch, Rueckausnahme Art. 6 Abs. 3 und Pflichtenfolge. Output: Hochrisiko-Landkarte mit Routing zu Detail-Skills. |
| `hochschule-ki-detektor-menschliche-pruefung` | KI-Detektoren in Schule, Hochschule und Auswahlverfahren: methodische Grenzen, False Positives, Transparenz, Anhoerung, menschliche Plausibilitaetspruefung, Datenschutz und Beweisakte. Baut einen belastbaren Entscheidungsvermerk statt Detektor-Automatismus. |
| `hochschule-ki-taeuschung-anscheinsbeweis` | KI-Nutzung in Hochschulpruefungen: Taeschungsvorwurf, Anscheinsbeweis, Indizienbuendel, Beweislast der Hochschule, subjektives Element, Anhoerung, Pruefungsrecht und DSGVO-Schnittstelle. Erzeugt Verteidigungs- oder Hochschulvermerk ohne blinde Detektor-Glaeubigkeit. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Hochrisiko Transparenz Zuordnung ART**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Welche Informationen muessen wir dem Betreiber in der Gebrauchsanweisung zur Verfuegung stellen? Art. 13 KI-VO Transparenz und Informationspflichten. Prüfraster: Gebrauchsanweisung Mindestinhalt Art. 13 Abs. 3 Systembeschreibung Zweck Genauigkeitsmetriken Risiken menschliche Aufsicht Verstaendlichkeitsanforderungen Sprachanforderungen Aktualisierungspflichten. Output: Vorlage Gebrauchsanweisung Hochrisiko-KI. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (interne Doku) und begrenztes-risiko-art-50-transparenzpflichten (Endnutzer-Transparenz).

# Transparenz und Informationen für Betreiber — Art. 13 KI-VO

## Zweck

Art. 13 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, Betreibern ausreichende Informationen zu liefern, damit diese das System sicher und bestimmungsgemäß einsetzen können. Die Gebrauchsanweisung ist damit ein zentrales Compliance-Instrument.

## Grundprinzip: Transparenz durch Design

Hochrisiko-KI-Systeme müssen so konzipiert und entwickelt werden, dass ihr Betrieb für Betreiber in ausreichendem Maß transparent ist, sodass diese die Ausgaben des Systems interpretieren und angemessen nutzen können.

## Mindestinhalt der Informationen für Betreiber (Art. 13 Abs. 3 KI-VO)

### Pflichtinhalt 1 — Identität und Kontaktdaten des Anbieters

Name und Anschrift des Anbieters sowie gegebenenfalls seines in der EU ansässigen Bevollmächtigten.

### Pflichtinhalt 2 — Merkmale, Fähigkeiten und Grenzen

- Verwendungszweck des Systems
- Leistungsniveau, einschließlich Genauigkeitsmetriken und Robustheit
- Bekannte Grenzen und Einschränkungen
- Umstände, die die Leistung des Systems beeinflussen können
- Auswirkungen auf betroffene Personen oder Gruppen, die als relevant erkannt wurden

### Pflichtinhalt 3 — Eingaben und Ausgaben

- Eingabedaten, für die das System ausgelegt ist
- Beschreibung der Ausgaben und ihrer Bedeutung
- Hinweise zur Interpretation der Ausgaben

### Pflichtinhalt 4 — Menschliche Aufsicht

- Beschreibung der erforderlichen menschlichen Aufsichtsmaßnahmen
- Technische Maßnahmen für menschliche Aufsicht (Stopp-Funktion, manuelle Übersteuerung)
- Anweisungen für das Eingreifen

### Pflichtinhalt 5 — Änderungen nach Inverkehrbringen

Wenn das System nach dem Inverkehrbringen verändert wurde oder werden kann, sind die Auswirkungen auf die Informationen für Betreiber entsprechend anzupassen.

### Pflichtinhalt 6 — Computerressourcen und IT-Sicherheit

Anforderungen an Hardware und Software sowie bekannte Cybersicherheitsmaßnahmen.

## Sprache und Format

Die Informationen müssen:
- In einer für Betreiber verständlichen Sprache verfasst sein — in der oder den Sprachen, die im jeweiligen Mitgliedstaat vorgeschrieben oder üblich sind
- Klar und prägnant formuliert sein
- In maschinenlesbarer Form vorliegen (soweit technisch sinnvoll)
- Klare Anweisungen für den sicheren Einsatz enthalten

**Prüffragen:**
- In welcher Sprache ist die Gebrauchsanweisung verfasst?
- Ist sie für Betreiber ohne Fachjargon verständlich?
- Enthält sie alle Pflichtinhalte nach Art. 13 Abs. 3 KI-VO?

## Abgrenzung — Betreiber versus Endnutzer

Die Informationspflicht nach Art. 13 KI-VO richtet sich an Betreiber (Organisationen, Unternehmen), nicht an Endnutzer (natürliche Personen, die das System nutzen). Informationspflichten gegenüber Endnutzern können aus Art. 50 KI-VO (Chatbot-Hinweis, Deepfake-Kennzeichnung) oder der DSGVO folgen.

## Verhältnis zur menschlichen Aufsicht

Die Informationen für Betreiber sind die Grundlage, damit Betreiber die menschliche Aufsicht nach Art. 14 KI-VO wirksam ausüben können. Eine Gebrauchsanweisung, die keine konkreten Anweisungen zur Aufsicht enthält, erfüllt Art. 13 KI-VO nicht vollständig.

## Typische Praxisprobleme

- Gebrauchsanweisung beschreibt nur technische Funktionen, nicht die Grenzen und Risiken.
- Informationen sind auf Englisch, obwohl Betreiber in Deutschland sitzen (nationale Sprachanforderungen beachten).
- Angaben zu Genauigkeit und Leistung fehlen oder sind zu allgemein.
- Keine Anweisungen für menschliche Aufsicht oder für den Fall von Systemfehlern.

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
PRUEFERGEBNIS — HOCHRISIKO TRANSPARENZ UND INFORMATIONEN FUER BETREIBER ART 13
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 13 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `hochrisiko-zuordnung-art-6-und-anhang-i-iii`

**Fokus:** Gesamtuebersicht zur Hochrisiko-Zuordnung nach Art. 6 KI-VO: Art. 6 Abs. 1 Sicherheitsbauteil/Anhang I und Art. 6 Abs. 2/Anhang III. Erklaert Zweckbestimmung, allgemeine Chatbots/GPAI, Mitarbeitenden-Fehlgebrauch, Rueckausnahme Art. 6 Abs. 3 und Pflichtenfolge. Output: Hochrisiko-Landkarte mit Routing zu Detail-Skills.

# Hochrisiko-Zuordnung — Art. 6 KI-VO und Anhang I/III

## Zweck

Dieser Skill gibt die Gesamtübersicht zur Hochrisiko-Einstufung. Er entscheidet nicht endgültig, sondern leitet in die passenden Detailprüfungen.

## Zwei Hochrisiko-Pfade

### Pfad 1 — Art. 6 Abs. 1

Ein KI-System ist Hochrisiko, wenn:
1. es Sicherheitsbauteil eines Produkts ist oder selbst ein Produkt, das unter Anhang-I-Sektorrecht fällt, und
2. dieses Produkt oder Sicherheitsbauteil einer Dritt-Konformitätsbewertung unterliegt.

Detail: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

### Pfad 2 — Art. 6 Abs. 2 i.V.m. Anhang III

Ein KI-System ist Hochrisiko, wenn es für einen in Anhang III genannten Zweck bestimmt ist oder entsprechend eingesetzt wird.

Die acht Bereiche:
1. Biometrie
2. Kritische Infrastruktur
3. Bildung und berufliche Ausbildung
4. Beschäftigung, Arbeitnehmermanagement und Zugang zur Selbständigkeit
5. Zugang zu wesentlichen privaten und öffentlichen Diensten und Leistungen
6. Strafverfolgung
7. Migration, Asyl und Grenzkontrolle
8. Rechtspflege und demokratische Prozesse

Detail: `hochrisiko-art-6-abs-2-anhang-iii`

## Zweckbestimmung statt Tool-Label

Ein allgemeiner Chatbot oder ein GPAI-System ist nicht automatisch Hochrisiko. Entscheidend ist:
- Wofür wird es vom Anbieter bestimmt?
- Wofür nimmt der Betreiber es in Betrieb?
- Welche Nutzung ist organisatorisch erlaubt, geduldet oder technisch nahegelegt?
- Werden natürliche Personen bewertet, gerankt, priorisiert oder in Rechten/Chancen betroffen?

Wenn Mitarbeitende ein allgemeines Tool entgegen klarer Regeln missbrauchen, ist das zunächst ein Governance- und Incident-Thema. Wenn die Nutzung aber systematisch ist, geduldet wird oder der Betreiber sie in Prozesse einbaut, kann die Hochrisiko-Prüfung neu kippen.

## Rückausnahme Art. 6 Abs. 3

Auch bei Anhang-III-Treffer ist die Rückausnahme zu prüfen:
- kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte
- eine der vier Fallgruppen
- keine Profiling-Sperre
- Dokumentation nach Art. 6 Abs. 4

Detail: `rueckausnahme-art-6-abs-3`

## Pflichtenfolge

Bei bestätigtem Hochrisiko:
- Anbieter: Art. 9 bis 15, Art. 17, Art. 43 bis 49, Registrierung, Marktbeobachtung
- Betreiber: Art. 26, ggf. Art. 27, bestimmungsgemäße Verwendung, menschliche Aufsicht, Logging, Informationspflichten
- Zweckänderung: Art. 25 Anbieterwerden prüfen

## Output-Template — Hochrisiko-Landkarte

```text
HOCHRISIKO-LANDKARTE ART. 6 KI-VO
System: [NAME]

Art. 6 Abs. 1: [ja/nein/unklar] — [Grund]
Art. 6 Abs. 2/Anhang III: [ja/nein/unklar] — [Bereich/Zweck]
Allgemeiner Chatbot/GPAI: [ja/nein] — [warum nicht automatisch / warum konkret relevant]
Mitarbeitenden-Fehlgebrauch: [kein Thema / vorhersehbar / geduldet / systematisch]
Art. 6 Abs. 3: [prüfen / fernliegend / greift wahrscheinlich]
Nächste Skills: [...]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 12/13/23, Art. 6 und Anhang I/III KI-VO. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `hochschule-ki-detektor-menschliche-pruefung`

**Fokus:** KI-Detektoren in Schule, Hochschule und Auswahlverfahren: methodische Grenzen, False Positives, Transparenz, Anhoerung, menschliche Plausibilitaetspruefung, Datenschutz und Beweisakte. Baut einen belastbaren Entscheidungsvermerk statt Detektor-Automatismus.

# KI-Detektor plus menschliche Prüfung

## Problem

KI-Detektoren können Hinweise liefern, aber sie sind fehleranfällig. In Prüfungsverfahren, Bewerbungen und akademischen Zulassungen darf ein Detektorbefund nicht die sorgfältige menschliche Entscheidung ersetzen.

## Prüfraster

| Ebene | Prüfung |
|---|---|
| Technik | Welches Tool, welche Version, welche Schwellenwerte, welche Fehlerquote, welche Sprache, welcher Texttyp? |
| Verfahren | Wurde die betroffene Person informiert, angehört und konnte sie Gegenindizien liefern? |
| Inhalt | Gibt es echte Auffälligkeiten im Text, Quellen, Stil, Argumentationsgang, Zitierweise? |
| Vergleich | Liegen frühere Arbeiten, Entwürfe, Notizen, Versionsverläufe oder mündliche Erläuterungen vor? |
| Datenschutz | Welche Daten wurden verarbeitet, auf welcher Grundlage, wurden Texte an Drittanbieter übertragen? |
| Entscheidung | Hat ein Mensch die Indizien eigenständig gewürdigt? |

## Arbeitsweise

1. Detektorbefund in die Akte aufnehmen, aber nicht als Beweisersatz behandeln.
2. Plausibilitätsmatrix erstellen.
3. Betroffene Person anhören.
4. Alternative Erklärungen prüfen: Sprachstil, Übersetzung, Schreibassistenz, Lektorat, Stress, Vorlagen, Gruppenarbeit.
5. Entscheidung so begründen, dass sie ohne Detektor noch verständlich ist.

## Output

Ein zweiseitiger Vermerk mit:

- Indizien pro/contra KI-Nutzung.
- Verfahrensfehlern.
- Datenschutzrisiken.
- Entscheidungsoptionen: einstellen, nachprüfen, mildere Maßnahme, Sanktion.

## Schnittstelle KI-VO

Wenn ein System im Bildungsbereich Lern- oder Prüfungsentscheidungen beeinflusst, immer Art. 6 Abs. 2 i.V.m. Anhang III KI-VO prüfen.

## 4. `hochschule-ki-taeuschung-anscheinsbeweis`

**Fokus:** KI-Nutzung in Hochschulpruefungen: Taeschungsvorwurf, Anscheinsbeweis, Indizienbuendel, Beweislast der Hochschule, subjektives Element, Anhoerung, Pruefungsrecht und DSGVO-Schnittstelle. Erzeugt Verteidigungs- oder Hochschulvermerk ohne blinde Detektor-Glaeubigkeit.

# Hochschule: KI-Täuschung und Anscheinsbeweis

## Ziel

Der Skill hilft bei Fällen, in denen eine Hochschule eine Prüfungsleistung wegen angeblicher KI-Nutzung beanstandet oder eine Studentin sich gegen einen solchen Vorwurf verteidigt. Es geht nicht darum, KI-Nutzung zu verharmlosen, sondern darum, den Vorwurf beweisbar, fair und prüfungsrechtlich sauber zu prüfen.

## Leitgedanken

- Ein KI-Detektor ist kein Urteil.
- Die Hochschule trägt grundsätzlich die Verantwortung, den Täuschungsvorwurf tragfähig zu begründen.
- Ein Indizienbündel kann stark sein, muss aber nachvollziehbar, reproduzierbar und individuell auf die Arbeit bezogen sein.
- Das subjektive Element nicht vergessen: Was wusste oder wollte die geprüfte Person?

## Prüffragen

1. Welche Prüfungsordnung gilt und welche Hilfsmittelregel wurde verletzt?
2. War KI-Nutzung ausdrücklich verboten, eingeschränkt erlaubt oder unklar geregelt?
3. Welche Indizien gibt es: Stilbruch, Quellenfehler, Prompt-Artefakte, Metadaten, Versionshistorie, mündliche Nachbefragung, Detektor, Zeugen?
4. Hat die Hochschule eine eigenständige menschliche Prüfung vorgenommen?
5. Wurde die betroffene Person angehört und konnte sie Entstehungsprozess, Notizen, Zwischenstände oder Rechercheweg erklären?
6. Drohen Nebenfolgen: Nichtbestehen, Exmatrikulation, Zulassungssperre, spätere Täuschungsfeststellung?

## Output

Erstelle wahlweise:

- **Verteidigungsvermerk** mit Angriffspunkten gegen ein schwaches Indizienbündel.
- **Hochschulvermerk** mit fairer Beweisführung, Anhörung und Entscheidungsvorschlag.
- **Eilrechtsschutz-Check** bei Zulassungs-, Frist- oder Karrierefolgen.

## Mindeststandard

Nie schreiben: "Detektor sagt KI, also Täuschung." Immer schreiben: "Detektorbefund ist nur ein Indiz; entscheidend ist die tragfähige Gesamtwürdigung."
