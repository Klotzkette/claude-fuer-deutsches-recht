---
name: persoenlicher-anwendungsbereich-polizeiliche
description: "Persoenlicher Anwendungsbereich Polizeiliche: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Persoenlicher Anwendungsbereich Polizeiliche

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Persoenlicher Anwendungsbereich Polizeiliche** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `persoenlicher-anwendungsbereich-rollen-art-3` | Erster Schritt der KI-VO-Prüfung: Wer ist betroffen? Unternehmen fragt welche Rolle es in der KI-VO einnimmt. Art. 3 KI-VO Rollendefinitionen. Prüfraster: Anbieter Art. 3 Nr. 3 Betreiber Art. 3 Nr. 4 Einführer Art. 3 Nr. 6 Haendler Art. 3 Nr. 7 Produkthersteller Art. 25 Bevollmaechtigter Art. 22. Output: Rollenzuordnungsentscheidung als Einstieg für alle weiteren Pflichten-Skills. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 und rolle-betreiber-prüfen-art-3-nr-4 (detaillierte Rollenentscheidungsbaeume). |
| `polizeiliche-ki-vertrauenswuerdigkeit-din-spec` | Polizeiliche KI-Anwendungen: Vertrauenswuerdigkeit, Datenqualitaet, Bias, Auditierbarkeit, menschliche Kontrolle, Grundrechtsschutz, Zweckbindung, Beschaffung und Dokumentation fuer Predictive Policing, Bildanalyse, Lagezentren und Ermittlungsassistenz. |
| `public-sector-ai-procurement-ausschreibung` | KI-Beschaffung der oeffentlichen Hand: Leistungsbeschreibung, KI-VO-Hochrisiko, Datenschutz, Vergaberecht, Transparenz, Open-Source/Lock-in, Audit, Grundrechte-Folgenabschaetzung, Testbetrieb und Abnahme. |
| `rechtsabteilung-general-purpose-ai-im-konzern-und-zweckbestimmun` | Rechtsabteilungs-Fachmodul für General Purpose AI im Konzern und Zweckbestimmung: Chatbots werden nicht pauschal Hochrisiko, sondern nach Zweckbestimmung, Einsatzkontext und Fehlgebrauch geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Persoenlicher Anwendungsbereich Polizeiliche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `persoenlicher-anwendungsbereich-rollen-art-3`

**Fokus:** Erster Schritt der KI-VO-Prüfung: Wer ist betroffen? Unternehmen fragt welche Rolle es in der KI-VO einnimmt. Art. 3 KI-VO Rollendefinitionen. Prüfraster: Anbieter Art. 3 Nr. 3 Betreiber Art. 3 Nr. 4 Einführer Art. 3 Nr. 6 Haendler Art. 3 Nr. 7 Produkthersteller Art. 25 Bevollmaechtigter Art. 22. Output: Rollenzuordnungsentscheidung als Einstieg für alle weiteren Pflichten-Skills. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 und rolle-betreiber-prüfen-art-3-nr-4 (detaillierte Rollenentscheidungsbaeume).

# Persönlicher Anwendungsbereich — Rollen nach Art. 3 KI-VO

## Zweck

Die Pflichten nach der KI-VO hängen entscheidend von der Rolle des Nutzers in der KI-Wertschöpfungskette ab. Dieser Skill gibt einen Überblick über alle Rollen und leitet zur detaillierten Rollenprüfung weiter. Mehrere Rollen können gleichzeitig bestehen.

## Rollen im Überblick

### Anbieter (provider) — Art. 3 Nr. 3 KI-VO

Wer ein KI-System oder ein GPAI-Modell entwickelt oder entwickeln lässt und es unter seinem eigenen Namen oder seiner Marke in Verkehr bringt oder in Betrieb nimmt — entgeltlich oder unentgeltlich.

Detailprüfung: `rolle-anbieter-pruefen-art-3-nr-3`

### Betreiber (deployer) — Art. 3 Nr. 4 KI-VO

Wer ein KI-System in eigener Verantwortung verwendet, es sei denn, das System wird für persönliche, nicht berufliche Tätigkeiten genutzt.

Detailprüfung: `rolle-betreiber-pruefen-art-3-nr-4`

### Einführer (importer) — Art. 3 Nr. 6 KI-VO

Wer ein in einem Drittland in Verkehr gebrachtes KI-System in der EU in Verkehr bringt.

Detailprüfung: `einfuehrer-importer-pflichten-art-23`

### Händler (distributor) — Art. 3 Nr. 7 KI-VO

Wer ein KI-System in der Lieferkette zur Verfügung stellt, ohne Anbieter oder Einführer zu sein, und wer das System nicht wesentlich verändert.

Detailprüfung: `haendler-distributor-pflichten-art-24`

### Bevollmächtigter — Art. 3 Nr. 5 KI-VO

Eine in der EU ansässige natürliche oder juristische Person, die vom Anbieter eines in einem Drittland ansässigen schriftlich bevollmächtigt wurde, in seinem Namen bestimmte Aufgaben zu erfüllen.

Detailprüfung: `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

### Produkthersteller — Art. 3 in Verbindung mit Art. 25 Abs. 1 KI-VO

Wer ein KI-System als Sicherheitsbauteil in ein Produkt integriert, das unter Anhang I gelistete Unionsvorschriften fällt, und das Produkt unter eigenem Namen in Verkehr bringt.

Detailprüfung: `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

## Mehrfachrollen

In der Praxis sind Mehrfachrollen häufig:

- Wer ein fremdes KI-System wesentlich verändert und unter eigenem Namen in Verkehr bringt, wird zum Anbieter (Art. 25 KI-VO) → `anbieter-werden-art-25`
- Wer ein System selbst entwickelt und auch selbst einsetzt, ist gleichzeitig Anbieter und Betreiber.
- Einführer können unter bestimmten Bedingungen als Anbieter behandelt werden (Art. 23 Abs. 4 KI-VO).

## Routing

| Rolle | Nächster Skill |
|---|---|
| Anbieter | `rolle-anbieter-pruefen-art-3-nr-3` |
| Betreiber | `rolle-betreiber-pruefen-art-3-nr-4` |
| Einführer | `einfuehrer-importer-pflichten-art-23` |
| Händler | `haendler-distributor-pflichten-art-24` |
| Bevollmächtigter / Produkthersteller | `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25` |
| Unklare Rolle / Rollenwechsel möglich | `anbieter-werden-art-25` |

## Wichtiger Hinweis

Die Rollenzuordnung bestimmt den gesamten weiteren Prüfverlauf. Falsche Rolleneinschätzungen können dazu führen, dass wesentliche Pflichten übersehen werden. Im Zweifel sind alle in Betracht kommenden Rollen zu prüfen.

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
PRUEFERGEBNIS — PERSOENLICHER ANWENDUNGSBEREICH ROLLEN ART 3
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 3 Nr. 3/4 Rn. 12]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `polizeiliche-ki-vertrauenswuerdigkeit-din-spec`

**Fokus:** Polizeiliche KI-Anwendungen: Vertrauenswuerdigkeit, Datenqualitaet, Bias, Auditierbarkeit, menschliche Kontrolle, Grundrechtsschutz, Zweckbindung, Beschaffung und Dokumentation fuer Predictive Policing, Bildanalyse, Lagezentren und Ermittlungsassistenz.

# Polizeiliche KI: Vertrauenswürdigkeit und Auditierbarkeit

## Einsatzfälle

- Bild- oder Videoanalyse.
- Lagebild- und Einsatzpriorisierung.
- Ermittlungsassistenz.
- Mustererkennung in Massendaten.
- Übersetzung, Transkription, Kommunikationsanalyse.
- Prognose- oder Risikomodelle.

## Prüffragen

1. Rechtsgrundlage und Zweck: Gefahrenabwehr, Strafverfolgung, Verwaltung?
2. KI-VO: Anhang III Strafverfolgung oder Biometrie betroffen?
3. Daten: Herkunft, Qualität, Bias, Aktualität, Löschung.
4. Menschliche Kontrolle: Wer darf übersteuern und wie wird das dokumentiert?
5. Audit: Logs, Modellversion, Trainings-/Testdaten, Fehlerraten.
6. Grundrechte: Einschüchterung, Diskriminierung, Versammlungsfreiheit, Datenschutz.
7. Beschaffung: Anforderungen in Leistungsbeschreibung und Vertrag.

## Mindestanforderungen

- Zweckbindung statt Datenstaubsauger.
- dokumentierte Fehlerraten und Grenzen.
- unabhängige Überprüfung kritischer Treffer.
- klare Nichtnutzungsszenarien.
- Betroffenen- und Rechtsschutzperspektive.

## Output

Ein Beschaffungs- oder Einsatzvermerk mit Ampel und Abhilfen.

## Warnung

Bei Polizei-KI ist "Treffer" nur ein Hinweis. Er darf nicht unbemerkt zum Beweis, zur Verdachtsbegründung oder zur Einsatzentscheidung mutieren.

## 3. `public-sector-ai-procurement-ausschreibung`

**Fokus:** KI-Beschaffung der oeffentlichen Hand: Leistungsbeschreibung, KI-VO-Hochrisiko, Datenschutz, Vergaberecht, Transparenz, Open-Source/Lock-in, Audit, Grundrechte-Folgenabschaetzung, Testbetrieb und Abnahme.

# Öffentliche KI-Beschaffung

## Ziel

Behörden sollen KI nicht blind einkaufen. Dieser Skill baut Ausschreibungs- und Abnahmeanforderungen, die KI-VO, Datenschutz, Grundrechte und technische Wirklichkeit zusammenbringen.

## Normanker

- KI-VO Art. 3 Nr. 1, Art. 6 Abs. 2 und Anhang III für KI-System, Hochrisiko und Zweckbestimmung.
- KI-VO Art. 9 bis 15 und Art. 26 für Hochrisiko-Anforderungen und Betreiberpflichten; Art. 27 für Grundrechte-Folgenabschätzung, soweit einschlägig.
- KI-VO Art. 50 für Transparenzpflichten bei bestimmten KI-Systemen, insbesondere Interaktion, synthetische Inhalte und Deepfakes.
- DSGVO Art. 5, 6, 22, 25, 28, 32, 35; BDSG/Landesdatenschutzrecht je nach Behörde.
- GWB §§ 97 ff., VgV/UVgO und Haushaltsrecht für Vergabe, Wirtschaftlichkeit, Eignung, Zuschlagskriterien und Dokumentation.
- BSI-IT-Grundschutz, Cloud-/Souveränitätsvorgaben, Barrierefreiheit und Open-Source-/Exit-Anforderungen nur konkret nach Beschaffungsgegenstand einbauen.

## Ausschreibungsfragen

1. Welcher Verwaltungsprozess soll unterstützt werden?
2. Gibt es Entscheidungsvorbereitung mit Bürgerwirkung?
3. Ist Anhang III betroffen?
4. Welche Daten werden verarbeitet?
5. Gibt es Transparenz gegenüber Betroffenen?
6. Wie wird menschliche Kontrolle organisiert?
7. Welche Abnahme- und Testdaten gibt es?
8. Wie wird Vendor Lock-in verhindert?
9. Welche Zweckänderungen sind verboten und wie werden sie technisch verhindert?
10. Welche Nachweise muss der Anbieter vor Zuschlag, vor Abnahme und laufend liefern?
11. Welche Mindestanforderungen sind Ausschlusskriterien und welche nur Wertungskriterien?
12. Wie werden Beschwerden, Akteneinsicht, IFG-Anfragen und gerichtliche Kontrolle später bedient?

## Vertragsanforderungen

- Zweckbestimmung und verbotene Zweckänderungen.
- KI-VO-Dokumentation.
- Audit- und Einsichtsrechte.
- Modelländerungsanzeige.
- Incident-Meldung.
- Daten- und Exit-Rechte.
- Barrierefreiheit und Nachvollziehbarkeit.
- Unterauftragnehmer- und Modellkettenoffenlegung.
- Testdaten-Governance, Bias-/Fehleranalyse und Regressionsprüfung vor Produktivsetzung.
- Auditierbare menschliche Aufsicht: wer darf überstimmen, stoppen, freigeben, protokollieren?
- Change-Control für Modellupdates, Prompt-/Systemänderungen, neue Datenquellen und neue Einsatzbereiche.

## Output

- Ausschreibungsklauseln.
- Bewertungsmatrix.
- Abnahmeprotokoll.
- Grundrechte- und Datenschutz-Gate.

## Merksatz

Der öffentliche Auftraggeber beschafft nicht nur Software, sondern Verwaltungsmacht. Die muss prüfbar bleiben.

## 4. `rechtsabteilung-general-purpose-ai-im-konzern-und-zweckbestimmun`

**Fokus:** Rechtsabteilungs-Fachmodul für General Purpose AI im Konzern und Zweckbestimmung: Chatbots werden nicht pauschal Hochrisiko, sondern nach Zweckbestimmung, Einsatzkontext und Fehlgebrauch geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: General Purpose AI im Konzern und Zweckbestimmung

## Spezialkern: Rechtsabteilung: General Purpose AI im Konzern und Zweckbestimmung

- **Konkretes Problem:** Chatbots werden nicht pauschal Hochrisiko, sondern nach Zweckbestimmung, Einsatzkontext und Fehlgebrauch geprüft.
- **Norm-/Quellenanker:** KI-Verordnung (EU) 2024/1689, Art. 3, 5, 6, 9-15, 16 ff., 26, 50, 53 ff., Anhänge I und III; DSGVO; Produktsicherheits-/Produkthaftungsrecht; nationale Aufsichtspraxis.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

VO EU 2024/1689 Art. 3, 6, 53 ff.; Anhang III

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Chatbots werden nicht pauschal Hochrisiko, sondern nach Zweckbestimmung, Einsatzkontext und Fehlgebrauch geprüft.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.
