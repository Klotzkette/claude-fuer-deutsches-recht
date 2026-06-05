---
name: ki-richtlinie-nutzung-mandatsdaten
description: "Nutzung Mandatsdaten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nutzung Mandatsdaten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Nutzung Mandatsdaten** im Plugin KI-Richtlinie für Kanzleien. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-nutzungsrichtlinie-fristen-form-und-zustaendigkeit` | Nutzungsrichtlinie: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `auftragsverarbeitungsvertrag-pruefen` | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO bei KI-Anbietern prüfen: Anwendungsfall Kanzlei schließt Vertrag mit KI-Dienstleister und muss AVV auf DSGVO-Konformität prüfen. Art. 28 DSGVO AVV-Pflicht, § 43e BRAO IT-Dienstleister, AI Act Betreiberpflichten. Prüfraster Subprozessoren-Genehmigung, technisch-organisatorische Massnahmen TOMs, Drittlandtransfer SCC, Auditrrechte, Löschpflichten, Training-Opt-out. Output AVV-Prüfprotokoll mit Lueckenliste und Nachverhandlungsbedarf. Abgrenzung zu Musterklauseln-IT-Vertrag und zu Dienstleister-Due-Diligence. |
| `musterklauseln-it-vertrag` | Musterklauseln für IT-Vertraege mit KI-Dienstleistern in Kanzleien: Anwendungsfall Kanzlei verhandelt Vertrag mit KI-Anbieter und braucht Klauseln zu Verschwiegenheit Training-Opt-out Löschpflichten und Haftung. § 43e BRAO Verschwiegenheits-Erklärung, Art. 28 DSGVO AVV, § 203 StGB Berufsgeheimnis. Prüfraster Verschwiegenheits- und § 43e-Erklärung, Training-Opt-out, Löschpflichten, Auditrrechte, Haftungsregelung, Subprozessoren-Genehmigung. Output Musterklausel-Sammlung für IT-Vertrag mit KI-Dienstleister. Abgrenzung zu Auftragsverarbeitungsvertrag-Prüfen und zu Dienstleister-Due-Diligence. |

## Arbeitsweg

Im Plugin KI-Richtlinie für Kanzleien gilt für **Nutzung Mandatsdaten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-nutzungsrichtlinie-fristen-form-und-zustaendigkeit`

**Fokus:** Nutzungsrichtlinie: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin ki richtlinie kanzleien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Nutzungsrichtlinie: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Nutzungsrichtlinie: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Nutzungsrichtlinie: Fristen, Form, Zuständigkeit und Rechtsweg / nutzungsrichtlinie fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BRAO, BORA, DSGVO, BRAK, DAV.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Nutzungsrichtlinie** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Bestandteile der KI-Nutzungsrichtlinie (Mindestumfang)
1. **Geltungsbereich**: Anwälte, Syndizi, Referendare, Mitarbeiter; alle Kanzlei-IT.
2. **Zweck**: Verschwiegenheit § 43a BRAO, § 203 StGB; DSGVO; KI-VO; Mandatssorgfalt.
3. **Tool-Klassifizierung**: Tool-Liste mit Freigabestatus (freigegeben / mit Auflagen / verboten).
4. **Datenklassifizierung**: öffentlich / intern / vertraulich / hochsensibel (Mandantengeheimnis, besondere Kategorien).
5. **Trainingsausschluss**: vertraglich und in den Einstellungen; Beweis der Konfiguration.
6. **Verifikationspflicht**: KI-Output muss vom Berufsträger geprüft werden (Halluzinationskontrolle, Quellenverifikation).
7. **Mandantenaufklärung**: wann und wie; ggf. Einwilligung.
8. **Vorfallmeldung**: Pflicht zur Meldung von Datenpannen, Halluzinationen mit Mandantenwirkung.
9. **Schulungen**: Onboarding, jährliche Auffrischung.
10. **Reviews**: jährliche Überprüfung der Richtlinie; Anlassbezogen bei neuen Tools.

## Form und Zuständigkeit
- **Erlass**: Sozietätsleitung / Geschäftsführung; Mitbestimmung durch Betriebsrat (§ 87 Abs. 1 Nr. 6, Nr. 7 BetrVG bei technischer Überwachung / Verhaltensregeln).
- **Form**: Textform genügt formell; signierte Empfangsbestätigung der Mitarbeiter empfehlenswert.
- **Verbindlichkeit**: arbeitsrechtliche Weisungsgrundlage; Zuwiderhandlung als Pflichtverletzung abmahnfähig.

## Fristen
- **Erstellung**: vor Einführung von KI-Tools verbindlich vorhalten; spätestens vor erstem produktivem Einsatz mit Mandantendaten.
- **Review-Zyklus**: Jährlich; ad-hoc bei wesentlichen Änderungen (neue KI-VO-Stufen 02.02.2025 für Art. 5 Verbote, 02.08.2026 für Art. 6 Hochrisiko).
- **Aufbewahrung**: Versionsstände mindestens 6 Jahre (§ 50 BRAO-Analogie für mandatsbezogene Dokumentation).

## Rechtsweg bei Streit
- **Intern**: Disziplinarverfahren, Abmahnung, Kündigung (arbeitsrechtlich).
- **Anwaltsgericht**: bei berufsrechtlich relevanten Verstößen (§§ 113 ff. BRAO) — über RAK.
- **Datenschutzaufsicht**: bei DSGVO-Verstößen; LDA/BfDI.
- **Marktüberwachungsbehörde KI-VO**: ab Geltung Art. 6 ff. (02.08.2026); Bundesnetzagentur als Marktüberwachung in Deutschland vorgesehen.

## Trade-off
Verbotsorientierte Richtlinie ("Keine ChatGPT-Nutzung") ist klar, wird aber umgangen ("Schatten-IT"). Erlaubnisorientierte Richtlinie mit gestuften Freigaben und Schulungen erzeugt Akzeptanz und reduziert tatsächlich Risiko — verlangt aber laufende Pflege der Tool-Liste.

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

## 2. `auftragsverarbeitungsvertrag-pruefen`

**Fokus:** Auftragsverarbeitungsvertrag nach Art. 28 DSGVO bei KI-Anbietern prüfen: Anwendungsfall Kanzlei schließt Vertrag mit KI-Dienstleister und muss AVV auf DSGVO-Konformität prüfen. Art. 28 DSGVO AVV-Pflicht, § 43e BRAO IT-Dienstleister, AI Act Betreiberpflichten. Prüfraster Subprozessoren-Genehmigung, technisch-organisatorische Massnahmen TOMs, Drittlandtransfer SCC, Auditrrechte, Löschpflichten, Training-Opt-out. Output AVV-Prüfprotokoll mit Lueckenliste und Nachverhandlungsbedarf. Abgrenzung zu Musterklauseln-IT-Vertrag und zu Dienstleister-Due-Diligence.

# Auftragsverarbeitungsvertrag prüfen

Jeder KI-Dienstleister, der im Auftrag der Kanzlei personenbezogene Daten verarbeitet, muss als Auftragsverarbeiter nach Art. 28 DSGVO vertraglich gebunden werden. Der Auftragsverarbeitungsvertrag (AVV) ist eine datenschutzrechtliche Pflichtgrundlage — sein Fehlen begründet einen DSGVO-Verstoß. Dieser Skill stellt eine strukturierte Prüfcheckliste bereit.

## Rechtlicher Hintergrund

Art. 28 Abs. 1 DSGVO: Beauftragung nur von Auftragsverarbeitern mit hinreichenden Garantien für technisch-organisatorische Maßnahmen. Art. 28 Abs. 3 DSGVO: Pflichtinhalt des AVV (Gegenstand, Dauer, Art, Zweck, Weisungsgebundenheit, Vertraulichkeit, TOMs, Unterauftragsverarbeiter, Betroffenenrechte, Löschung/Rückgabe, Audits). Art. 28 Abs. 4 DSGVO: Unterauftragsverarbeiter müssen denselben Pflichten unterliegen. Art. 46 DSGVO: Anforderungen für Drittlandtransfers (SCC, Angemessenheitsbeschluss). Art. 83 Abs. 4 DSGVO: Bußgelder bis zu 10 Millionen Euro oder 2 % des Jahresumsatzes bei AVV-Verstößen. Art. 82 DSGVO: Schadensersatzhaftung.

## Vorgehen

1. **AVV-Existenz prüfen**: Besteht überhaupt ein schriftlicher (oder elektronischer) AVV mit dem KI-Anbieter?
2. **Pflichtinhalte nach Art. 28 Abs. 3 DSGVO verifizieren**: Sind alle gesetzlich vorgeschriebenen Regelungspunkte enthalten?
3. **Subprozessoren-Liste einholen**: Welche Unterauftragnehmer setzt der KI-Anbieter ein? Sind diese ebenfalls durch AVV gebunden? Wird eine aktuelle Liste bereitgestellt?
4. **TOMs prüfen**: Sind die technisch-organisatorischen Maßnahmen konkret beschrieben und dem Stand der Technik entsprechend?
5. **Drittlandtransfer-Regelung verifizieren**: Verarbeitet der Anbieter Daten außerhalb des EWR? Falls ja: Welche Rechtsgrundlage für den Drittlandtransfer (Angemessenheitsbeschluss, SCC, TIA)?
6. **Audit- und Kontrollrechte sicherstellen**: Räumt der AVV der Kanzlei das Recht ein, die Einhaltung der DSGVO durch den Anbieter zu überprüfen oder überprüfen zu lassen?
7. **Löschfristen definieren**: Verpflichtet der AVV den Anbieter zur Löschung oder Rückgabe aller Daten nach Vertragsende?

## Vorlagentext / Bausteine

**AVV-Prüfcheckliste:**

☐ Schriftliche AVV-Vereinbarung liegt vor (Art. 28 Abs. 9 DSGVO: auch elektronische Form genügt)
☐ Gegenstand, Dauer, Art und Zweck der Verarbeitung sind definiert
☐ Kategorien personenbezogener Daten und betroffener Personen sind spezifiziert
☐ Weisungsgebundenheit des Auftragsverarbeiters ist vereinbart
☐ Vertraulichkeitspflicht für alle zugriffsberechtigten Personen ist geregelt
☐ Konkrete TOMs sind beschrieben oder als Anlage beigefügt
☐ Liste der genehmigten Unterauftragsverarbeiter liegt vor und wird aktuell gehalten
☐ Kanzlei-Genehmigung bei Änderungen der Unterauftragsverarbeiter ist vereinbart
☐ Unterstützungspflicht bei Betroffenenanfragen und Datenschutzbehörden ist geregelt
☐ Meldepflicht bei Datenschutzverletzungen nach Art. 33 DSGVO ist vereinbart
☐ Datenschutz-Folgenabschätzung-Unterstützung nach Art. 35 DSGVO ist zugesagt
☐ Löschung oder Rückgabe aller Daten nach Vertragsende ist geregelt
☐ Audit- und Kontrollrechte der Kanzlei sind vereinbart
☐ Drittlandtransfer-Rechtsgrundlage ist dokumentiert (falls anwendbar)
☐ § 43e-BRAO-Vereinbarung ist zusätzlich abgeschlossen (berufsrechtliche Anforderung)

## Hinweise zur Aktualisierung

Die Anforderungen an AVV können sich durch Entscheidungen der Datenschutzbehörden oder neue EuGH-Rechtsprechung ändern. Ebenso müssen AVV bei wesentlichen Änderungen der Datenverarbeitungstätigkeit aktualisiert werden. Bei Änderungen der Unterauftragsverarbeiter des KI-Anbieters ist zu prüfen, ob eine erneute Risikobeurteilung erforderlich ist.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 28 DSGVO — Auftragsverarbeitung (Pflichtinhalt AVV)
- Art. 46 DSGVO — Drittlandtransfer-Garantien (SCC, Angemessenheitsbeschluss)
- Art. 82 DSGVO — Schadensersatz
- Art. 83 Abs. 4 DSGVO — Bussgelder bis 10 Mio. EUR
- § 43e BRAO — Berufsrechtliche IT-Dienstleister-Anforderungen

## Triage zu Beginn
1. Besteht ein schriftlicher AVV nach Art. 28 DSGVO mit dem KI-Anbieter?
2. Sind alle Pflichtinhalte nach Art. 28 Abs. 3 DSGVO enthalten?
3. Verarbeitet der Anbieter Daten ausserhalb des EWR — ist eine TIA durchgefuehrt?
4. Sind Unterauftragsverarbeiter benannt und durch eigenen AVV gebunden?
5. Sind Auditrechte der Kanzlei nach Art. 28 Abs. 3 lit. h DSGVO vereinbart?

## Output-Template — AVV-Pruefungsprotokoll
**Adressat:** Kanzlei intern / DSB — Tonfall: checklisten-strukturiert
```
AVV-PRUEFUNGSPROTOKOLL
[DATUM] — Anbieter: [ANBIETERNAME] — Anwendungsfall: [BESCHREIBUNG]

Ergebnis: [WIRKSAMER AVV / LUECKEN / KEIN AVV — EINSATZ UNZULAESSIG]

Pflichtinhalte Art. 28 Abs. 3 DSGVO:
☑/☐ Gegenstand und Dauer der Verarbeitung
☑/☐ Weisungsgebundenheit
☑/☐ Vertraulichkeitspflicht
☑/☐ TOMs (konkret oder als Anlage)
☑/☐ Unterauftragsverarbeiter-Liste
☑/☐ Unterstuetzung Betroffenenrechte
☑/☐ Meldepflicht Datenpanne Art. 33 DSGVO
☑/☐ Loeschung / Rueckgabe nach Vertragsende
☑/☐ Auditrecht Art. 28 Abs. 3 lit. h DSGVO
☑/☐ Drittlandtransfer-Rechtsgrundlage (Art. 46 DSGVO)

§ 43e BRAO Berufsrechts-AVV: ☑/☐ vorhanden

Naechste Pruefung: [DATUM]
Geprueft von: [NAME]
```

## 3. `musterklauseln-it-vertrag`

**Fokus:** Musterklauseln für IT-Vertraege mit KI-Dienstleistern in Kanzleien: Anwendungsfall Kanzlei verhandelt Vertrag mit KI-Anbieter und braucht Klauseln zu Verschwiegenheit Training-Opt-out Löschpflichten und Haftung. § 43e BRAO Verschwiegenheits-Erklärung, Art. 28 DSGVO AVV, § 203 StGB Berufsgeheimnis. Prüfraster Verschwiegenheits- und § 43e-Erklärung, Training-Opt-out, Löschpflichten, Auditrrechte, Haftungsregelung, Subprozessoren-Genehmigung. Output Musterklausel-Sammlung für IT-Vertrag mit KI-Dienstleister. Abgrenzung zu Auftragsverarbeitungsvertrag-Prüfen und zu Dienstleister-Due-Diligence.

# Musterklauseln IT-Vertrag

Jeder Vertrag mit einem KI-Dienstleister, der Mandatsdaten verarbeiten soll, muss zwei Säulen aufweisen: einen datenschutzrechtlichen Auftragsverarbeitungsvertrag (AVV) nach Art. 28 DSGVO und eine berufsrechtliche Vereinbarung nach § 43e BRAO. Dieser Skill stellt die wichtigsten Musterklauseln bereit.

## Rechtlicher Hintergrund

§ 43e BRAO: Befugte Weitergabe von Berufsgeheimnissen an IT-Dienstleister setzt einen entsprechenden Vertrag voraus, der den Dienstleister zur Verschwiegenheit verpflichtet. § 203 Abs. 3 Satz 2 StGB: Der Dienstleister wird als "mitwirkende Person" privilegiert und nicht wegen Geheimnisverrats bestraft, wenn eine ordnungsgemäße § 43e-Vereinbarung besteht. § 53a StPO: Zeugnisverweigerungsrecht des Dienstleisters. § 97 Abs. 2 StPO: Beschlagnahmeschutz. Art. 28 DSGVO: AVV-Pflicht. Art. 82 DSGVO: Haftung des Verantwortlichen und Auftragsverarbeiters.

## Vorgehen

1. **Vertragsstruktur festlegen**: Separater AVV nach Art. 28 DSGVO plus separater § 43e-BRAO-Vertrag (oder kombiniert in einem Dokument).
2. **Klauseln anpassen**: Musterklauseln an den konkreten Dienstleister und die konkrete Leistung anpassen (Subprozessoren, Rechenzentrum-Standorte, Löschfristen).
3. **Training-Opt-out separat vereinbaren**: Explizit regeln, dass der Dienstleister Eingaben nicht für das Training seiner Modelle verwendet.
4. **Auditrechte absichern**: Recht der Kanzlei auf Prüfung der Einhaltung durch eigene Prüfer oder externe Auditoren.
5. **Strafrechtliche Belehrung erteilen**: § 43e-BRAO-Vertrag muss auf die strafrechtliche Relevanz eines Verschwiegenheitsbruchs nach § 203 StGB hinweisen.

## Vorlagentext / Bausteine

**Klausel 1 — Anerkennung der Verschwiegenheitspflicht (§ 43e BRAO):**
Der Auftragnehmer ist bekannt, dass die im Rahmen der zu erbringenden Dienste erhaltenen Informationen beruflichen Verschwiegenheitspflichten unterliegen können. Der Auftragnehmer erkennt alle Rechte und Pflichten aus §§ 43a und 43e BRAO an und hält alle im Rahmen der Dienste erlangten Geheimnisse im Sinne von § 203 StGB und §§ 43a, 43e BRAO streng geheim und schützt sie vor unbefugtem Zugriff durch Dritte.

**Klausel 2 — Zweckbindung und Zugangsbeschränkung:**
Der Auftragnehmer hat nur insoweit Zugang zu Geheimen Informationen, als dies für die Erbringung der vereinbarten Dienste erforderlich ist. Eine Nutzung für eigene Zwecke, insbesondere für das Training von KI-Modellen, ist ausdrücklich untersagt.

**Klausel 3 — Training-Opt-out:**
Der Auftragnehmer verpflichtet sich unwiderruflich, die vom Auftraggeber eingegebenen oder hochgeladenen Inhalte (Texte, Dokumente, Prompts und Outputs) nicht zum Training oder zur Weiterentwicklung von KI-Modellen oder KI-Systemen zu verwenden. Diese Verpflichtung gilt auch für alle Unterauftragnehmer.

**Klausel 4 — Unterauftragnehmer:**
Der Auftragnehmer darf Geheime Informationen an Unterauftragnehmer nur weitergeben, wenn (i) der Unterauftragnehmer schriftlich zur Vertraulichkeit verpflichtet wurde, (ii) der Unterauftragnehmer seine Leistungen ausschließlich innerhalb des EWR erbringt oder angemessene Drittland-Garantien bestehen, und (iii) die Genehmigung des Auftraggebers vorliegt.

**Klausel 5 — Strafrechtliche Belehrung nach § 203 StGB:**
Der Auftraggeber belehrt den Auftragnehmer, dass ein Verstoß gegen die Verschwiegenheitspflicht eine Straftat nach § 203 StGB darstellen kann, die mit Freiheitsstrafe bis zu einem Jahr oder Geldstrafe bestraft wird.

**Klausel 6 — Strafprozessuale Privilegien:**
Dem Auftragnehmer ist bekannt, dass Berufsgeheimnisse dem Zeugnisverweigerungsrecht nach § 53a StPO und dem Beschlagnahmeschutz nach § 97 Abs. 2 StPO unterfallen. Im Fall einer behördlichen Vernehmung oder Beschlagnahme wird der Auftragnehmer unverzüglich den Auftraggeber informieren.

**Klausel 7 — Löschpflichten:**
Nach Beendigung des Vertrags oder auf Aufforderung des Auftraggebers löscht der Auftragnehmer alle gespeicherten Geheimen Informationen unwiderruflich und bestätigt dies schriftlich innerhalb von 30 Tagen.

**Klausel 8 — Auditrechte:**
Der Auftraggeber oder ein von ihm beauftragter Dritter ist berechtigt, die Einhaltung dieser Vereinbarung durch den Auftragnehmer zu überprüfen. Der Auftragnehmer unterstützt solche Prüfungen nach Ankündigung mit angemessener Frist.

## Hinweise zur Aktualisierung

Musterklauseln sind bei jeder wesentlichen Änderung der berufsrechtlichen oder datenschutzrechtlichen Anforderungen zu aktualisieren. Neue BRAK-Veröffentlichungen zu § 43e BRAO-Vereinbarungen sind besonders zu beachten. Ebenso sind neue Entscheidungen zu § 203 StGB oder zu den Anforderungen an AVV in die Klauseln einzuarbeiten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 305 BGB — Einbeziehung von AGB
- § 307 BGB — Inhaltskontrolle (unangemessene Benachteiligung)
- Art. 25 KI-VO — Verantwortlichkeitsverteilung in der KI-Lieferkette
- Art. 28 DSGVO — AVV-Klauseln in IT-Vertraegen
- § 2 GeschGehG — Geheimhaltungsmassnahmen

## Triage zu Beginn
1. Handelt es sich um AGB oder Individualvereinbarung (§ 305 Abs. 1 BGB)?
2. Welche Risikoklasse hat das KI-System — bestimmt Art. 25 KI-VO Verantwortlichkeit?
3. Sind Haftungsbeschraenkungen im Vertrag wirksam — § 307 BGB-Pruefung?
4. Enthalten die Klauseln Regelungen zu Training auf Eingabedaten?
5. Sind AVV-Pflichten nach Art. 28 DSGVO in den IT-Vertrag integriert?

## Output-Template — KI-Vertrags-Musterklausel
**Adressat:** Vertragsparteien / Rechtsabteilung — Tonfall: vertragsrechtlich, klar
```
MUSTERKLAUSEL KI-EINSATZ — IT-VERTRAG
[VERTRAG] — Version: [VERSION] — Stand: [DATUM]

§ [X] KI-EINSATZ UND DATENVERARBEITUNG

(1) Verarbeitung auf Daten: Der Auftragnehmer versichert, dass KI-Systeme,
die im Rahmen dieses Vertrages eingesetzt werden, Eingabedaten des Auftrag-
gebers nicht zum Training von Modellen verwenden. Anderslautende Klauseln in
AGB des Auftragnehmers werden hierdurch ausdruecklich ausgeschlossen.

(2) Verantwortlichkeit (Art. 25 KI-VO): Die Parteien sind sich einig, dass
der Auftraggeber als Betreiber nach Art. 3 Nr. 4 KI-VO handelt. Der Auftrag-
nehmer als Anbieter traegt die Pflichten nach Art. 9-15 KI-VO.

(3) Auftragsverarbeitung: Soweit der Auftragnehmer personenbezogene Daten
verarbeitet, gilt Anlage [X] (AVV nach Art. 28 DSGVO).

(4) Haftungsgrenze: Die Haftung des Auftragnehmers fuer Schaden durch
fehlerhafte KI-Ausgaben ist auf [EURO-BETRAG] pro Schadensfall begrenzt,
hoechstens [EURO-BETRAG] pro Jahr. Vorbehaltlich § 307 BGB.

(5) Vertraulichkeit (GeschGehG): Der Auftragnehmer verpflichtet sich, alle
Eingabedaten als Geschaeftsgeheimnisse i.S.d. § 2 GeschGehG zu behandeln.
```
