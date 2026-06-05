---
name: triage-haftung-versicherung-anwendungsfall
description: "Triage Haftung Versicherung Anwendungsfall: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Triage Haftung Versicherung Anwendungsfall

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Triage Haftung Versicherung Anwendungsfall** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-triage-fristen-form-und-zustaendigkeit` | Triage: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `ki-haftung-und-versicherung` | Haftung beim Einsatz von KI: Anbieter- und Betreiberhaftung KI-VO, Produkthaftungsgesetz neu nach RL EU 2024 2853, ueberschiessende KI-Haftungs-RL (Entwurf), Vertragshaftung. Versicherbarkeit (D and O, Cyber, KI-spezifisch). Pruefraster fuer Versicherungsmakler und Risikomanagement. |
| `anwendungsfall-triage` | Klassifiziert einen vorgeschlagenen KI-Anwendungsfall gegen das Unternehmensregister — freigegeben, bedingt oder nicht freigegeben — und erstellt Auflagenliste und nächste Schritte. Prüft gegen verbotene Praktiken (Art. 5 KI-VO) und Hochrisiko-Kategorien (Anhang III KI-VO). Lädt, wenn der Nutzer "KI-Anwendungsfall triage", "dürfen wir KI für X einsetzen", "ist das freigegeben" oder "Hochrisiko-KI klassifizieren" sagt. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Triage Haftung Versicherung Anwendungsfall**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-triage-fristen-form-und-zustaendigkeit`

**Fokus:** Triage: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Triage: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Triage: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Triage: Fristen, Form, Zuständigkeit und Rechtsweg / triage fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, KI, VO, DSGVO, AIA, DPIA.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Triage** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `ki-haftung-und-versicherung`

**Fokus:** Haftung beim Einsatz von KI: Anbieter- und Betreiberhaftung KI-VO, Produkthaftungsgesetz neu nach RL EU 2024 2853, ueberschiessende KI-Haftungs-RL (Entwurf), Vertragshaftung. Versicherbarkeit (D and O, Cyber, KI-spezifisch). Pruefraster fuer Versicherungsmakler und Risikomanagement.

# KI-Haftung und Versicherung

## Spezialwissen: KI-Haftung und Versicherung
- **Spezialgegenstand:** KI-Haftung und Versicherung / ki haftung und versicherung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, VO, RL, EU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `anwendungsfall-triage`

**Fokus:** Klassifiziert einen vorgeschlagenen KI-Anwendungsfall gegen das Unternehmensregister — freigegeben, bedingt oder nicht freigegeben — und erstellt Auflagenliste und nächste Schritte. Prüft gegen verbotene Praktiken (Art. 5 KI-VO) und Hochrisiko-Kategorien (Anhang III KI-VO). Lädt, wenn der Nutzer "KI-Anwendungsfall triage", "dürfen wir KI für X einsetzen", "ist das freigegeben" oder "Hochrisiko-KI klassifizieren" sagt.

# KI-Anwendungsfall-Triage

## Zweck

Das Gespräch stoppen, das als "Können wir nicht einfach KI dafür einsetzen?"
beginnt. Schnelle, kalibrierte Antwort aus dem Register geben — und bei
bedingter Freigabe die Auflagen konkret und den nächsten Schritt klar machen.

Die Triage-Skill ist ein Eingangstor: klassifizieren, Erforderliches
kennzeichnen, weiterleiten. Die Folgenabschätzungs-Skill erledigt die
Tiefenarbeit. Pflichtprüfung vor allem anderen: Art. 5 KI-VO (verbotene
Praktiken, ab 02.02.2025) und DSGVO Art. 22 (automatisierte Einzelentscheidung).

## Eingaben

- Beschreibung des KI-Anwendungsfalls: was tut die KI, wer ist betroffen,
 gibt es menschliche Überprüfung, welcher Anbieter?
- Praxisprofil aus `CLAUDE.md` (Anwendungsfall-Register, Rote Linien,
 Governance-Stufen, regulatorischer Fußabdruck)

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 5 KI-VO (verbotene Praktiken)**: Social Scoring durch
 öffentliche oder private Stellen (Art. 5 Abs. 1 lit. c); subliminale
 Manipulation (Art. 5 Abs. 1 lit. a/b); Ausnutzung von Vulnerabilität
 (Art. 5 Abs. 1 lit. b); biometrische Kategorisierung nach geschützten
 Merkmalen (Art. 5 Abs. 1 lit. g); Echtzeitfernidentifizierung in
 öffentlichen Räumen (Art. 5 Abs. 1 lit. h); Emotionserkennung am
 Arbeitsplatz/Bildung (Art. 5 Abs. 1 lit. f). Ab 02.02.2025 anwendbar.
- **AI Act Art. 6 i.V.m. Anhang III KI-VO**: Hochrisiko-Kategorien —
 Nr. 1 Biometrie; Nr. 2 Beschäftigung (Bewerbungs-Screening, Leistungs-
 bewertung); Nr. 3 Wesentliche Dienstleistungen (Kredit, Versicherung);
 Nr. 4 Bildung; Nr. 5 Kritische Infrastruktur; Nr. 6 Strafverfolgung;
 Nr. 7 Migration; Nr. 8 Rechtspflege. Hochrisiko: Art. 9–15 (Anbieter),
 Art. 26/29 (Betreiber).
- **DSGVO Art. 22**: Vollautomatisierte Einzelentscheidungen mit Rechtswirkung
 oder erheblicher Beeinträchtigung nur nach Art. 22 Abs. 2 lit. a–c
 (Vertrag, gesetzliche Pflicht, ausdrückliche Einwilligung). Widerspruchs-
 und Transparenzpflichten.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmungsrecht des Betriebsrats bei
 KI-Tools zur Mitarbeiterüberwachung/-bewertung.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kommentare**

- Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5 Rn. 8 (verbotene Praktiken) und Art. 6 i.V.m. Anhang III Rn. 15 (Hochrisiko-Klassifikation).
- Ehmann/Selmayr, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10.
- Müller-Glöge, in: Erfurter Kommentar, 25. Aufl. 2025, § 87 BetrVG Rn. 32.
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 88.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Anwendungsfall verstehen**

Bei vager Beschreibung fragen: Was tut die KI genau? Auf wen/was wirkt sie?
Prüft ein Mensch vor Wirkung? Welcher Anbieter? Nur intern oder Kunden/Dritte?

**Schritt 2 — Art. 5-Prüfung (ERSTE PRIORITÄT)**

Vor dem Register prüfen: Liegt ein absolutes Verbot vor?
- Social Scoring, subliminale Manipulation, Vulnerabilitäts-Ausnutzung
- Biometrische Kategorisierung nach geschützten Merkmalen
- Echtzeitbiometrie in öffentlichen Räumen
- Emotionserkennung am Arbeitsplatz/Bildung

Bei Treffer: sofort melden, ohne Abmilderung:
> "Dieser Anwendungsfall berührt [Art. 5 KI-VO]. Verbotene Praktiken sind
> absolute Verbote. Wenn etwas anders ist: anwaltliche Entscheidung nötig,
> keine Triage-Freigabe."

**Schritt 3 — Register-Abgleich**

Direkttreffer → anwenden. Nahes Match → kennzeichnen. Kein Treffer →
BEDINGT (Folgenabschätzung ausstehend); vorläufige Risikoeinschätzung
einschließlich Anhang-III-Prüfung ausgeben.

**Schritt 4 — Jurisdiktionaler Anwendungsbereich und Anhang-III-Prüfung**

Alle Regime aus `## Regulatorischer Fußabdruck` prüfen. Striktest
anwendbare Behandlung bei Mehrfach-Jurisdiktion. Anhang-III-Kategorien
(Nr. 1–8) explizit gegen den Anwendungsfall prüfen; bei Hochrisiko:
Betreiberpflichten Art. 26/29 KI-VO vermerken.

**Schritt 5 — DSGVO Art. 22-Prüfung**

Vollautomatisiert + Rechtswirkung/erhebliche Beeinträchtigung? → Art. 22
Abs. 1 greift; Rechtsgrundlage nach Abs. 2 dokumentieren und Human-in-the-
Loop oder Einwilligung sicherstellen.

**Schritt 6 — Klassifikation und Ausgabe**

Bei Nicht-Jurist-Rolle: vor FREIGEGEBEN-Klassifikation anwaltliche Prüfung
abfragen; 1-seitigen Kurzüberblick für das Anwaltsgespräch generieren.

---

**ANWENDUNGSFALL:** [Anwendungsfall wie verstanden]
**KLASSIFIKATION:** [FREIGEGEBEN / BEDINGT / NICHT FREIGEGEBEN]
**Art. 5 KI-VO:** [Kein Verbot / [Verbotene Praxis] — ABSOLUTES VERBOT]
**Anhang III KI-VO:** [Nicht einschlägig / Hochrisiko Kategorie [Nr.]]
**DSGVO Art. 22:** [Nicht einschlägig / Einschlägig — Rechtsgrundlage: [Abs. 2]]
**Begründung:** [1–3 Sätze]
**Ausgelöste Rote Linien:** [Keine / Liste]

*Bei BEDINGT:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| KI-Folgenabschätzung (ggf. DSFA Art. 35 DSGVO) | [KI-Beauftragter] | ☐ |
| DSGVO Art. 22 Rechtsgrundlage dokumentieren | [DSB] | ☐ |
| Human-in-the-Loop — keine vollautomatisierten Entscheidungen | [Produkt] | ☐ |
| Offenlegung ggü. Betroffenen (Art. 13/14 DSGVO) | [Produkt/Recht] | ☐ |
| Betriebsrats-Beteiligung (§ 87 Abs. 1 Nr. 6 BetrVG) | [HR/Recht] | ☐ |

**Governance-Stufe:** [Standard / Erhöht / Hoch]

## Ausgabeformat

Bei Einzel-Anwendungsfall: wie oben. Bei mehreren Anwendungsfällen:
zuerst Übersichtstabelle (✅ Freigegeben / ⚠️ Bedingt / ❌ Nicht freigegeben
+ Schlüssel-Blocker), dann Detailausführung für bedingte und abgelehnte.

## Beispiel

**Anfrage:** "HR will KI zur automatischen Bewerbungs-Vorselektion einsetzen."
**Triage:** Art. 5: kein Verbot. Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO: Hochrisiko, wenn das System zweckbestimmt für Auswahl, Filterung oder Bewertung von Bewerbungen eingesetzt wird. DSGVO Art. 22 Abs. 1 bei Vollautomatisierung.
§ 87 Abs. 1 Nr. 6 BetrVG: Betriebsrats-Beteiligung prüfen.
**Klassifikation: BEDINGT.** Folgenabschätzung + DSFA; Human-in-the-Loop;
Betriebsrat einbeziehen; Offenlegung ggü. Bewerber:innen (Art. 13 DSGVO).

## Risiken und typische Fehler

- Art. 5 KI-VO ist Pflichtprüfung — immer zuerst, vor dem Register.
- "Nur intern" reduziert das Risiko nicht: Mitarbeiter-KI oft höheres
 Risiko als kundenseitige KI.
- "Wir testen nur" ist keine Ausnahme bei echten Personen-Daten.
- "Der Anbieter sagt, es ist sicher" ersetzt nicht die eigene Folgenabschätzung.

## Quellenpflicht

- **AI Act Art. 5** und **Art. 6 i.V.m. Anhang III** (mit konkreter Nr.) bei
 jeder Klassifikation.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- **§ 87 Abs. 1 Nr. 6 BetrVG** bei Mitarbeiter-Überwachungs-/Bewertungstools.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5 Rn. 8 und Anhang III Rn. 15.**
- **Ehmann/Selmayr, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10.**
- **Müller-Glöge, in: Erfurter Kommentar, 25. Aufl. 2025, § 87 BetrVG Rn. 32.**

## Triage zu Beginn
1. Was tut die KI genau — assistierend, augmentierend oder vollautomatisiert?
2. Sind Betroffene schutzbeduertige Gruppen (Minderjaerige, Arbeitnehmer, Kreditnehmer)?
3. Liegt eine Hochrisiko-Kategorie nach Anhang III KI-VO vor (Nr. 1-8 pruefen)?
4. Ist eine vollautomatisierte Einzelentscheidung mit Rechtswirkung moeglich (Art. 22 DSGVO)?
5. Besteht ein § 87 Abs. 1 Nr. 6 BetrVG-Mitbestimmungsrecht (Mitarbeiterbewertung)?

## Output-Template — Triage-Ergebnis KI-Anwendungsfall
**Adressat:** Governance-Team / Fachabteilung — Tonfall: klar, strukturiert
```
TRIAGE-ERGEBNIS KI-ANWENDUNGSFALL
[DATUM] — [ANWENDUNGSFALL-ID]

ANWENDUNGSFALL: [BESCHREIBUNG]
KLASSIFIKATION: [FREIGEGEBEN / BEDINGT / NICHT FREIGEGEBEN]

Art. 5 KI-VO (verbotene Praktiken): [Kein Verbot / VERBOTEN: BEGRUENDUNG]
Anhang III KI-VO (Hochrisiko): [Nicht einschlaegig / Hochrisiko Kat. Nr. X]
DSGVO Art. 22: [Nicht einschlaegig / Einschlaegig — Rechtsgrundlage: Art. 22 Abs. 2 lit. X]
§ 87 Abs. 1 Nr. 6 BetrVG: [Nicht einschlaegig / Mitbestimmung erforderlich]

Begruendung: [1-3 Saetze]

Bei BEDINGT — Auflagen:
1. [AUFLAGE + VERANTWORTLICHER + FRIST]
2. [AUFLAGE + VERANTWORTLICHER + FRIST]

Governance-Stufe: [Standard / Erhoeht / Hoch]
Naechste Pruefung: [DATUM]

Erstellt: [NAME], [DATUM]
```
