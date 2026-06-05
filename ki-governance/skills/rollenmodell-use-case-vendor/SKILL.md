---
name: rollenmodell-use-case-vendor
description: "Rollenmodell USE Case Vendor: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rollenmodell USE Case Vendor

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rollenmodell USE Case Vendor** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-rollenmodell-formular-portal-und-einreichung` | Rollenmodell: Formular, Portal und Einreichungslogik im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-use-case-risk-classification` | Use-Case-Risikoklassifizierung nach KI-VO und DSGVO: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-vendor-behoerden-gericht-und-registerweg` | Vendor: Behörden-, Gerichts- oder Registerweg im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Rollenmodell USE Case Vendor**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-rollenmodell-formular-portal-und-einreichung`

**Fokus:** Rollenmodell: Formular, Portal und Einreichungslogik im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Rollenmodell: Formular, Portal und Einreichungslogik

## Spezialwissen: Rollenmodell: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Rollenmodell: Formular, Portal und Einreichungslogik / rollenmodell formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **KI-VO-Rollenmodell** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## KI-VO-Rollen und Einreichungswege
- **Anbieter (Art. 3 Nr. 3 KI-VO):** entwickelt und bringt KI-System in Verkehr; Hauptverpflichteter Art. 9-15, 16-22.
- **Betreiber (Art. 3 Nr. 4):** verwendet KI-System unter eigener Verantwortung; Art. 26 Pflichten.
- **Importeur (Art. 3 Nr. 6):** bringt KI aus Drittland in EU; Art. 23.
- **Händler (Art. 3 Nr. 7):** macht KI auf Markt verfügbar; Art. 24.
- **Bevollmächtigter (Art. 3 Nr. 5):** Vertreter eines Drittland-Anbieters; Art. 22.

## Einreichungswege Behördenkommunikation
- **Konformitätserklärung:** Aufbewahrung 10 Jahre durch Anbieter (Art. 47 Abs. 4); Anhang V definiert Mindestinhalt.
- **EU-Datenbank Registrierung** Art. 49 KI-VO: für Hochrisiko-Systeme nach Anhang III; öffentlich einsehbar bei EU-Kommission.
- **CE-Kennzeichnung** Art. 48 KI-VO bei Hochrisiko.
- **Vorfallmeldung** Art. 73 KI-VO an Marktüberwachungsbehörde: 15 Tage Standard, 2 Tage bei schwerwiegend, sofort bei Tod.
- **Marktüberwachungsbehörden in DE:** je nach Sektor; BNetzA für Telekommunikation, BSI für Cybersicherheit, BfDI für Datenschutzaspekte. National wird die KI-VO-Aufsicht (Stand 2026) etabliert.

## Praxis-Tipp
Die KI-VO unterscheidet zwischen Anbieter und Betreiber sehr strikt — bei Substantieller Modifikation eines Hochrisiko-Systems (z. B. Fine-Tuning, neuer Anwendungszweck) wird der Betreiber zum Anbieter (Art. 25 KI-VO) und übernimmt deren Pflichten. Frühzeitig prüfen, ob unternehmensinterner Feintuning-Prozess Anbieterstellung auslöst.

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

## 2. `spezial-use-case-risk-classification`

**Fokus:** Use-Case-Risikoklassifizierung nach KI-VO und DSGVO: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Use-Case-Risikoklassifizierung nach KI-VO und DSGVO

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `ki-governance`. Kontext des Plugins: EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Use-Case-Risikoklassifizierung nach KI-VO und DSGVO** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## KI-VO-Klassifizierungslogik (VO (EU) 2024/1689)
- **Verboten (Art. 5 KI-VO, gilt ab 02.02.2025)**: u. a. Social Scoring durch öffentliche Stellen, manipulative Techniken, biometrische Kategorisierung nach sensiblen Merkmalen, Echtzeit-Fernidentifikation im öffentlichen Raum.
- **Hochrisiko (Art. 6 i. V. m. Anhang III, gilt ab 02.08.2026)**: u. a. Bildung, Beschäftigung (Recruiting, Performance), kritische Infrastruktur, Strafverfolgung, biometrische Identifikation, Migration, Justiz und demokratische Prozesse, Gesundheits-/Lebensversicherungs-Risikoscoring.
- **Begrenztes Risiko mit Transparenzpflicht (Art. 50)**: Chatbots, Emotionserkennung, biometrische Kategorisierung, Deepfakes.
- **Minimales Risiko**: alle übrigen Systeme.

## Schnittstelle zur DSGVO
- **Art. 35 DSGVO DSFA** ist regelmäßig erforderlich, wenn Hochrisiko-KI-VO-System personenbezogene Daten verarbeitet.
- **Art. 22 DSGVO** Verbot automatisierter Einzelentscheidungen mit rechtlicher Wirkung; Ausnahmen (Vertragserfordernis, Einwilligung, gesetzliche Erlaubnis) erfordern menschliche Aufsicht.
- **Art. 27 KI-VO**: Folgenabschätzung für Grundrechte durch Betreiber (Fundamental Rights Impact Assessment, FRIA) zusätzlich zur DSGVO-DSFA.

## Klassifizierungs-Trade-offs
- "Empfehlungssystem im HR" — meistens **Hochrisiko** nach Anhang III Nr. 4 ("Beschäftigung, Personalverwaltung").
- "Reiner Übersetzer" mit Kundendaten — typischerweise **minimales Risiko**, aber DSGVO-Schiene voll relevant.
- "RAG-System mit Mandantenakten in Kanzlei" — kein KI-VO-Hochrisiko, aber Berufsrecht und § 203 StGB greifen.
- "Foundation Model intern aufgesetzt" — als GPAI nach Art. 51 ff. KI-VO eigene Kategorie, ab 10²⁵ FLOP systemisches Risiko.

## Output für Inventar
- Use-Case-ID, Kurzbeschreibung, Geschäftsbereich
- KI-VO-Klassifizierung mit Norm und Begründung
- DSGVO-Rechtsgrundlage Art. 6, ggf. Art. 9
- Rolle (Anbieter Art. 3 Nr. 3 vs. Betreiber Art. 3 Nr. 4)
- Status DSFA, FRIA
- Verantwortliche Person und Review-Frist

## Trade-off
Frühzeitige sorgfältige Klassifizierung ist günstiger als spätere Reklassifizierung; ein als "minimal" eingestuftes System, das später als Hochrisiko erkannt wird, erzwingt nachträgliche Konformitätsbewertung (Art. 43 KI-VO), Logging-Aufbau (Art. 12) und technische Dokumentation (Art. 11) — oft mit Marktrückzug oder kostspieliger Anpassung.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-vendor-behoerden-gericht-und-registerweg`

**Fokus:** Vendor: Behörden-, Gerichts- oder Registerweg im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vendor: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Vendor: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Vendor: Behörden-, Gerichts- oder Registerweg / vendor behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vendor** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Behördenweg KI-VO
- **Marktüberwachung Art. 70 KI-VO**: jeder Mitgliedstaat benennt eine oder mehrere Behörden; in Deutschland Bundesnetzagentur als zentrale Marktüberwachung vorgesehen, plus sektorale Stellen.
- **Anzeige Art. 73 KI-VO**: Anbieter Hochrisiko-KI muss schwerwiegende Vorfälle an die Marktüberwachungsbehörde melden **innerhalb von 15 Tagen** nach Kenntnis; bei Tod oder schwerer Gesundheitsschädigung **2 Tage**; bei breit angelegten Verletzungen Sicherheit Personen **10 Tage**.
- **Untersagungsverfügung Art. 79-80**: Marktüberwachung kann Inverkehrbringen untersagen, Rückruf anordnen.
- **EU-Datenbank Art. 71**: öffentliche Datenbank für Hochrisiko-Systeme; Eintrag durch Anbieter (Anhang VIII) und Betreiber (öffentliche Stellen, Art. 49 Abs. 1a) erforderlich.

## DSGVO-Behördenweg parallel
- **Auskunftsersuchen Aufsicht Art. 58 Abs. 1 lit. a DSGVO**: Vorlagepflicht der DSFA, Auftragsverarbeitungsverträge, technisch-organisatorischen Maßnahmen.
- **Vorherige Konsultation Art. 36**: bei verbleibendem hohem Risiko trotz Schutzmaßnahmen; Reaktionsfrist 8 Wochen, verlängerbar 6 Wochen.
- **Bußgeldverfahren Art. 83**: parallele Zuständigkeit zu KI-VO bei personenbezogenen Daten.

## Gerichtsweg
- **Drittklage**: Betroffene können nach Art. 79 DSGVO klagen; nach KI-VO Art. 85 hat eine Person, die der Auffassung ist, dass ihre Rechte verletzt wurden, **Beschwerderecht bei der Marktüberwachungsbehörde**.
- **Klage gegen Untersagung**: Verwaltungsgerichtsweg gegen Behördenmaßnahmen; bei Bußgeld OWi-Verfahren.
- **Streit zwischen Anbieter und Betreiber**: Zivilrechtsweg, Vertragsrecht.

## Registerweg
- **EU AI Database** (Art. 71 / Anhang VIII KI-VO): Pflicht zur Eintragung für Anbieter Hochrisiko-KI vor Inverkehrbringen; Datenpunkte (Name, Trust-Mark, Konformitätsverfahren, Ergänzungen).
- **Betreiber-Eintrag**: öffentliche Stellen tragen sich nach Art. 49 Abs. 1a für eingesetzte Hochrisiko-KI ein.
- **Bevollmächtigte** (Art. 22): in der Datenbank verzeichnet.

## Vendor-spezifische Pflichtenkette
- **Vendor-Onboarding**: Self-Assessment Anbieter, Konformitätserklärung Anhang V, technische Doku Auszüge.
- **Laufende Überwachung**: jährlicher Vendor-Review, Aktualität Konformitätsdokumente, Vorfallhistorie.
- **Off-Boarding**: Datenlöschung beim Anbieter, Bestätigung der Löschung, ggf. Rückführung an Verantwortlichen.

## Trade-off
Eigene Konformitätsbewertung des Betreibers ist begrenzt, da der Anbieter die Last trägt. Sorgfältige Vendor-Auswahl mit dokumentierten Selbstauskünften und Verträgen ist regelmäßig der wirksamste Schutz; eigene erneute Bewertung ist nicht zwingend, wenn der Anbieter Anhang IV / Anhang V vollständig liefert.

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
