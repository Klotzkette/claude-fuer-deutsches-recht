---
name: sanktionen-art-bussgeldverteidigung-bildung
description: "Sanktionen ART Bussgeldverteidigung Bildung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sanktionen ART Bussgeldverteidigung Bildung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Sanktionen ART Bussgeldverteidigung Bildung** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `sanktionen-art-99-bis-101` | Unternehmen moechte die Kostenrisiken einer KI-VO-Verletzung einschaetzen oder Vorstand über Bußgelddimensionen informieren. Art. 99 bis 101 KI-VO Sanktionen. Prüfraster: bis 35 Mio EUR oder 7 Prozent Konzernumsatz bei verbotenen Praktiken bis 15 Mio EUR oder 3 Prozent bei sonstigen Verstoszen bis 7.5 Mio EUR oder 1 Prozent bei falschen Angaben. KMU-Privilegierung. Strafbarkeit natuerlicher Personen. Output: Sanktionsrahmen-Übersicht und Compliance-ROI-Argumentation. Abgrenzung zu governance-aufsichtsbehoerden-art-70 (Behoerden) und marktueberwachung-meldung-vorfaelle-art-72-bis-79 (Meldepflichten). |
| `sanktionen-bussgeldverteidigung-art-99` | Art. 99 KI-VO als Bußgeld- und Verteidigungsworkflow: Sanktionstier, Unternehmensbezug, Vorsatz/Fahrlaessigkeit, Aufsichtsbehoerdenkontakt, Akteneinsicht, Abhilfe, Vergleichsstrategie, Vorstandsvorlage und Litigation Hold. |
| `bildung-pruefungsrecht-anhang-iii-monitoring` | Anhang III KI-VO fuer Bildung, Pruefung, Zulassung und Lernsteuerung: Hochrisiko-Check fuer KI in Hochschulen, Schulen, EdTech, Proctoring, Zulassungsranking, Plagiats-/KI-Erkennung und Lernstandsdiagnostik. |
| `hochrisiko-menschliche-aufsicht-art-14` | Anbieter oder Betreiber fragt: Wie stellen wir sicher dass Menschen das Hochrisiko-KI-System wirksam beaufsichtigen und uebersteuerung ist möglich? Art. 14 KI-VO menschliche Aufsicht. Prüfraster: Verstehen der Systemfähigkeiten und Grenzen Überwachungspflichten Stop-Button-Konzept Nicht-Blinding-Schutz Kompetenzanforderungen Aufsichtspersonen Dokumentation. Output: Aufsichtskonzept und Muster-Schulungsplan für Betreiber. Abgrenzung zu betreiber-deployer-pflichten-art-26 (Betreiber-Gesamtpflichten) und hochrisiko-technische-dokumentation-art-11-und-anhang-iv. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Sanktionen ART Bussgeldverteidigung Bildung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `sanktionen-art-99-bis-101`

**Fokus:** Unternehmen moechte die Kostenrisiken einer KI-VO-Verletzung einschaetzen oder Vorstand über Bußgelddimensionen informieren. Art. 99 bis 101 KI-VO Sanktionen. Prüfraster: bis 35 Mio EUR oder 7 Prozent Konzernumsatz bei verbotenen Praktiken bis 15 Mio EUR oder 3 Prozent bei sonstigen Verstoszen bis 7.5 Mio EUR oder 1 Prozent bei falschen Angaben. KMU-Privilegierung. Strafbarkeit natuerlicher Personen. Output: Sanktionsrahmen-Übersicht und Compliance-ROI-Argumentation. Abgrenzung zu governance-aufsichtsbehoerden-art-70 (Behoerden) und marktueberwachung-meldung-vorfaelle-art-72-bis-79 (Meldepflichten).

# Sanktionen — Art. 99 bis 101 KI-VO

## Zweck

Art. 99 bis 101 KI-VO enthalten das Bußgeldsystem der KI-VO. Die Sanktionen sind nach Schwere des Verstoßes gestaffelt und erreichen für die schwersten Verstöße (verbotene Praktiken) sehr hohe Höchstbeträge. Dieser Skill gibt einen vollständigen Überblick.

## Bußgeldstufe 1 — Verbotene Praktiken (Art. 99 Abs. 3 KI-VO)

**Tatbestand:** Verstoß gegen Art. 5 KI-VO (verbotene KI-Praktiken).

**Bußgeldhöhe:**
- Bis zu 35 000 000 EUR, oder
- Bei Unternehmen: bis zu sieben Prozent des gesamten weltweiten Jahresumsatzes des vorausgegangenen Geschäftsjahres — je nachdem, welcher Betrag höher ist.

**Hinweis zur Berechnung:** Der Jahresumsatz bezieht sich auf den Konzernumsatz (Muttergesellschaft), nicht nur auf den Umsatz der handelnden Tochtergesellschaft. Dies macht die Sanktion besonders empfindlich für Konzerne.

**KMU-Privilegierung:** Für kleine und mittlere Unternehmen (KMU) gelten die niedrigeren Absolutbeträge, wenn diese niedriger sind als der prozentuale Wert.

## Bußgeldstufe 2 — Sonstige wesentliche Verstöße (Art. 99 Abs. 4 KI-VO)

**Tatbestand:** Verstöße gegen:
- Die Anforderungen an Hochrisiko-KI-Systeme (Art. 9 bis 15 KI-VO)
- Die Pflichten von Anbietern, Betreibern, Einführern und Händlern (Art. 16 bis 27 KI-VO)
- Die Anforderungen an GPAI-Modelle (Art. 51 bis 55 KI-VO)
- Die Transparenzpflichten (Art. 50 KI-VO)

**Bußgeldhöhe:**
- Bis zu 15 000 000 EUR, oder
- Bei Unternehmen: bis zu drei Prozent des gesamten weltweiten Jahresumsatzes — je nachdem, welcher Betrag höher ist.

## Bußgeldstufe 3 — Falsche Informationen an Behörden (Art. 99 Abs. 5 KI-VO)

**Tatbestand:** Übermittlung unrichtiger, unvollständiger oder irreführender Informationen an benannte Stellen oder nationale Behörden.

**Bußgeldhöhe:**
- Bis zu 7 500 000 EUR, oder
- Bei Unternehmen: bis zu ein Prozent des gesamten weltweiten Jahresumsatzes — je nachdem, welcher Betrag höher ist.

## Bußgelder für GPAI-Anbieter (Art. 101 KI-VO)

**Tatbestand:** Verstöße von Anbietern von GPAI-Modellen gegen die Pflichten aus Art. 51 bis 55 KI-VO.

**Bußgeldhöhe:**
- Bis zu 15 000 000 EUR, oder
- Bei Unternehmen: bis zu drei Prozent des gesamten weltweiten Jahresumsatzes — je nachdem, welcher Betrag höher ist.

**Besonderheit:** Bei Verstößen gegen Auskunftspflichten gegenüber dem Europäischen KI-Büro kann ein Tagegeld verhängt werden (Art. 101 Abs. 3 KI-VO).

## KMU-Privilegierung (Art. 99 Abs. 6 KI-VO)

Bei der Bemessung der Bußgelder berücksichtigen die Behörden die Interessen und wirtschaftliche Lage kleiner und mittlerer Unternehmen. Für KMU und Start-ups gelten die niedrigeren der jeweils anwendbaren Beträge (absoluter Betrag oder prozentualer Wert).

**Definition KMU:** Weniger als 250 Mitarbeiter und Jahresumsatz bis zu 50 Mio EUR oder Bilanzsumme bis zu 43 Mio EUR (nach Empfehlung 2003/361/EG der Kommission).

## Strafschärfungs- und Milderungsgründe

Die Behörden berücksichtigen bei der Bemessung des Bußgelds:
- Art, Schwere, Dauer und Auswirkungen des Verstoßes
- Vorsatz oder Fahrlässigkeit
- Maßnahmen des Unternehmens zur Schadensbegrenzung
- Kooperationsbereitschaft mit der Behörde
- Vorangehende Verstöße
- Grad der Verantwortlichkeit

## Verhältnis zu nationalen Sanktionen (Art. 100 KI-VO)

Mitgliedstaaten können für Verstöße durch natürliche Personen, die keine Unternehmen sind, eigene Sanktionsregelungen einführen. In Deutschland sind die entsprechenden nationalen Durchführungsregelungen abzuwarten.

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
PRUEFERGEBNIS — SANKTIONEN ART 99 BIS 101
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 99 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `sanktionen-bussgeldverteidigung-art-99`

**Fokus:** Art. 99 KI-VO als Bußgeld- und Verteidigungsworkflow: Sanktionstier, Unternehmensbezug, Vorsatz/Fahrlaessigkeit, Aufsichtsbehoerdenkontakt, Akteneinsicht, Abhilfe, Vergleichsstrategie, Vorstandsvorlage und Litigation Hold.

# Sanktionen und Bußgeldverteidigung nach Art. 99 KI-VO

## Ziel

Der Skill strukturiert die Verteidigung, wenn eine Aufsichtsbehörde wegen KI-VO-Verstößen nachfragt, ermittelt oder Sanktionen androht.

## Sofortmaßnahmen

1. Eingang dokumentieren: Behörde, Datum, Frist, Aktenzeichen.
2. Litigation Hold: Logs, Modellversionen, Freigaben, Tickets, Trainingsdaten, Vendor-Kommunikation sichern.
3. Kommunikation kanalisieren: eine verantwortliche Stelle, keine unkoordinierten Sachverhaltsgeständnisse.
4. Vorwurf clustern: Art. 5, Hochrisiko-Pflichten, GPAI, Transparenz, falsche Behördeninformation.
5. Abhilfe prüfen: Abschalten, Einschränken, Nutzerhinweis, Nachdokumentation, Rückruf, Incident-Report.

## Art.-99-Matrix

Erstelle eine aktuelle Matrix aus dem Verordnungstext:

- Verbotene Praktiken.
- Sonstige KI-VO-Pflichten.
- Falsche/unvollständige Informationen gegenüber zuständigen Stellen.
- Besonderheiten für KMU/Start-ups.
- Bemessungsfaktoren und Milderungsargumente.

## Verteidigungslinien

- kein KI-System;
- falsche Rolle;
- keine Zweckbestimmung für Hochrisiko;
- Art. 6 Abs. 3 dokumentiert;
- Betreiberfehlgebrauch statt Anbieterpflicht;
- nachweisbares Compliance-System;
- schnelle Abhilfe;
- unklare Leitlinienlage.

## Output

- Behördenantwort.
- Vorstandsvorlage.
- Bußgeldrisikomatrix.
- Abhilfe- und Kommunikationsplan.

## Quellenregel

Bußgeldhöhen immer am aktuellen Art. 99 KI-VO prüfen; keine Zahlen aus Sekundärmaterial blind übernehmen.

## 3. `bildung-pruefungsrecht-anhang-iii-monitoring`

**Fokus:** Anhang III KI-VO fuer Bildung, Pruefung, Zulassung und Lernsteuerung: Hochrisiko-Check fuer KI in Hochschulen, Schulen, EdTech, Proctoring, Zulassungsranking, Plagiats-/KI-Erkennung und Lernstandsdiagnostik.

# Bildung und Prüfungsrecht nach Anhang III

## Einsatzfälle

Dieser Skill prüft KI-Systeme in:

- Hochschulzulassung und Studienplatzvergabe.
- Prüfungsaufsicht, Proctoring, Täuschungs- und Plagiatserkennung.
- Bewertung von Prüfungen, Essays, Portfolios oder mündlichen Leistungen.
- Lernstandsdiagnostik, Kurszuweisung, Förderbedarfsprognose.
- Auswahlentscheidungen für Stipendien, Austauschprogramme oder Masterzulassungen.

## Hochrisiko-Logik

Prüfe nicht nach Produktnamen, sondern nach Wirkung:

1. Beeinflusst das System Zugang, Bewertung, Fortkommen oder Ausschluss?
2. Wird eine Person individuell gerankt, bewertet oder prognostiziert?
3. Ist die KI nur Hilfsmittel oder praktisch entscheidungsleitend?
4. Gibt es menschliche Kontrolle, die echte Abweichung erlaubt?
5. Ist die Zweckbestimmung des Anbieters bildungsbezogen oder wird das System off-label verwendet?

## Risikopunkte

- Diskriminierung durch Trainingsdaten oder Sprachmuster.
- Falsche Täuschungsverdächtigungen.
- Intransparente Score-Werte.
- Überautomatisierte Zulassungsentscheidungen.
- Fehlende Akteneinsicht oder unzureichende Begründung.

## Output

Erzeuge:

- Hochrisiko-Vermerk nach Art. 6 Abs. 2 i.V.m. Anhang III.
- Betreiberpflichtenliste nach Art. 26 KI-VO.
- Grundrechte- und Datenschutz-Check.
- Entscheidungsbausteine für Prüfungsamt oder Rechtsbehelf.

## Quellenregel

Bei konkreten gerichtlichen Entscheidungen nur Gericht, Datum, Aktenzeichen und frei überprüfbare Quelle verwenden. Keine Datenbankfundstellen aus geschlossenen Systemen erfinden.

## 4. `hochrisiko-menschliche-aufsicht-art-14`

**Fokus:** Anbieter oder Betreiber fragt: Wie stellen wir sicher dass Menschen das Hochrisiko-KI-System wirksam beaufsichtigen und uebersteuerung ist möglich? Art. 14 KI-VO menschliche Aufsicht. Prüfraster: Verstehen der Systemfähigkeiten und Grenzen Überwachungspflichten Stop-Button-Konzept Nicht-Blinding-Schutz Kompetenzanforderungen Aufsichtspersonen Dokumentation. Output: Aufsichtskonzept und Muster-Schulungsplan für Betreiber. Abgrenzung zu betreiber-deployer-pflichten-art-26 (Betreiber-Gesamtpflichten) und hochrisiko-technische-dokumentation-art-11-und-anhang-iv.

# Menschliche Aufsicht — Art. 14 KI-VO

## Zweck

Art. 14 KI-VO ist eine der zentralen Schutzvorschriften für Hochrisiko-KI-Systeme: Kein Hochrisiko-KI-System darf ohne die Möglichkeit menschlicher Aufsicht betrieben werden. Dies schließt nicht aus, dass das System weitgehend automatisiert arbeitet — aber es muss jederzeit die Möglichkeit geben, einzugreifen, zu korrigieren oder zu stoppen.

## Pflicht 1 — Systemseitige Maßnahmen zur menschlichen Aufsicht (Art. 14 Abs. 1 KI-VO)

Anbieter müssen Hochrisiko-KI-Systeme so konzipieren, dass sie durch natürliche Personen wirksam beaufsichtigt werden können. Die Maßnahmen zur menschlichen Aufsicht müssen in das System integriert sein, bevor es in Verkehr gebracht oder in Betrieb genommen wird.

**Maßnahmen können umfassen:**
- Schnittstellen, über die Aufsichtspersonen die Leistung des Systems beobachten können
- Mechanismen zur Deaktivierung (Stop-Button) oder zum Eingriff in die Systementscheidungen
- Anzeigen und Warnmeldungen bei ungewöhnlichen Ergebnissen oder Konfidenzunterschreitungen

## Pflicht 2 — Verstehen der Systemfähigkeiten und -grenzen (Art. 14 Abs. 4 lit. a KI-VO)

Aufsichtspersonen müssen in der Lage sein, die Fähigkeiten und Grenzen des Systems vollständig zu verstehen. Der Anbieter muss sicherstellen, dass das System so gestaltet ist, dass dieses Verständnis möglich ist (Erklärbarkeit, Transparenz der Ausgaben).

**Prüffragen:**
- Liefert das System ausreichende Erklärungen oder Konfidenzwerte zu seinen Ausgaben?
- Können Aufsichtspersonen die Ausgaben sinnvoll bewerten, ohne das System zu "blind" zu vertrauen?

## Pflicht 3 — Schutz vor Over-Reliance / Automation Bias (Art. 14 Abs. 4 lit. b KI-VO)

Das System muss so gestaltet sein, dass das Phänomen der übermäßigen Abhängigkeit von automatisierten Ausgaben (Automation Bias) erkannt und verhindert werden kann. Aufsichtspersonen dürfen nicht durch die Systemgestaltung dazu verleitet werden, Ausgaben unkritisch zu übernehmen.

**Prüffragen:**
- Gibt es Mechanismen, die Aufsichtspersonen aktiv zur Überprüfung von Ausgaben auffordern?
- Sind Ausgaben so präsentiert, dass eine kritische Bewertung erleichtert wird?

## Pflicht 4 — Erkennung von Anomalien (Art. 14 Abs. 4 lit. c KI-VO)

Aufsichtspersonen müssen in der Lage sein, Anomalien, Funktionsstörungen und unerwartetes Verhalten des Systems zu erkennen und darauf zu reagieren. Das System muss entsprechende Signale liefern.

## Pflicht 5 — Eingriffs- und Stopp-Möglichkeit (Art. 14 Abs. 4 lit. d KI-VO) — Stop-Button-Konzept

Das System muss jederzeit deaktiviert, abgebrochen oder seine Entscheidung durch eine Aufsichtsperson überschrieben werden können. Diese Funktion muss technisch zuverlässig und für Aufsichtspersonen zugänglich sein.

**Prüffragen:**
- Gibt es eine technische Möglichkeit, das System jederzeit zu stoppen?
- Ist diese Funktion dokumentiert und für zuständige Aufsichtspersonen erreichbar?

## Pflicht 6 — Kompetenzanforderungen an Aufsichtspersonen (Art. 14 Abs. 5 KI-VO)

Für biometrische Identifikationssysteme und andere Hochrisiko-KI-Systeme mit hohem Grundrechtseingriff gelten besondere Anforderungen: Die Aufsichtspersonen müssen über ausreichende Kompetenzen, Ausbildung und Befugnisse verfügen, um wirksam eingreifen zu können.

**Prüffragen:**
- Sind Aufsichtspersonen ausreichend geschult?
- Haben sie die Befugnis, Systementscheidungen zu überschreiben?

## Verantwortungsverteilung

**Anbieter:** Muss die technischen Mittel zur menschlichen Aufsicht bereitstellen und in der Gebrauchsanweisung beschreiben (Art. 13 i.V.m. Art. 14 KI-VO).

**Betreiber:** Muss die menschliche Aufsicht tatsächlich organisieren, qualifizierte Aufsichtspersonen einsetzen und dafür sorgen, dass diese die Aufsichtsfunktion wahrnehmen (Art. 26 Abs. 1 und 2 KI-VO).

## Typische Praxisprobleme

- System hat einen theoretischen Stopp-Button, aber keine klaren Verfahren, wann und wie er verwendet wird.
- Aufsichtspersonen wurden nicht ausreichend geschult.
- System präsentiert Ausgaben so, dass eine unabhängige Überprüfung schwierig ist.
- Kein dokumentierter Eskalationsprozess für den Fall, dass Aufsichtspersonen Ausgaben anzweifeln.

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
PRUEFERGEBNIS — HOCHRISIKO MENSCHLICHE AUFSICHT ART 14
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 14 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
