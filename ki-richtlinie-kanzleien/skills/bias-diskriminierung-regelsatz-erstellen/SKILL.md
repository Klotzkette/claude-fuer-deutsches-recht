---
name: bias-diskriminierung-regelsatz-erstellen
description: "Bias Diskriminierung Regelsatz Erstellen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bias Diskriminierung Regelsatz Erstellen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bias Diskriminierung Regelsatz Erstellen** im Plugin KI-Richtlinie für Kanzleien. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bias-und-diskriminierung-pruefung` | Bias und Diskriminierung in KI-Outputs für Kanzleien prüfen: Anwendungsfall Kanzlei nutzt KI-System bei Personalentscheidungen Mandantenberatung oder Rechercheaufgaben und muss sicherstellen dass keine diskriminierenden Ergebnisse entstehen. AGG Allgemeines Gleichbehandlungsgesetz, Anhang III Nr. 4 KI-VO Hochrisiko-Personalwesen. Prüfraster Bias-Quellen identifizieren, AGG-relevante Kategorien prüfen, diskriminierende Outputs erkennen, Schulungsanforderungen. Output Bias-Prüfprotokoll mit Kategorien und Korrekturmassnahmen. Abgrenzung zu KI-VO-Hochrisiko-Personalwesen und zu Compliance-Regelsatz. |
| `compliance-regelsatz-erstellen` | Compliance-Regelsatz Zehn Gebote für KI-Einsatz in Kanzleien erstellen: Anwendungsfall Kanzlei benoetigt praegnante Verhaltensregeln für alle Mitarbeitenden zu erlaubten und verbotenen KI-Nutzungen. § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz. Prüfraster kein Privat-Account, keine Mandatsdaten ohne Anonymisierung, kein PDF-Upload ohne AVV, Korrekturlesung Pflicht, KI-Kennzeichnung. Output standardisierter Zehn-Gebote-Regelsatz anpassbar an Kanzlei-Profil. Abgrenzung zu Richtlinien-Skelett für vollständige Richtlinie und zu Berufsrecht-Bausteine. |
| `dienstleister-due-diligence` | KI-Dienstleister Due Diligence für Kanzleien durchführen: Anwendungsfall Kanzlei moechte neuen KI-Dienst beauftragen und muss eigenverantwortlich Datenschutz Berufsrecht und Sicherheit prüfen. § 43e BRAO Dienstleisterprüfung, Art. 28 Abs. 1 DSGVO Garantiepflichten, ISO 27001 SOC 2. Prüfraster EU-Sitz vs. US-Sitz, Enterprise-Tier mit Training-Opt-out, Verschluesselung, Zertifizierungen, Subprozessoren, Standardvertragsklauseln. Output Dienstleister-Bewertungsmatrix mit Ampelstatus und AVV-Empfehlung. Abgrenzung zu Auftragsverarbeitungsvertrag-Prüfen und zu Musterklauseln-IT. |

## Arbeitsweg

Im Plugin KI-Richtlinie für Kanzleien gilt für **Bias Diskriminierung Regelsatz Erstellen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bias-und-diskriminierung-pruefung`

**Fokus:** Bias und Diskriminierung in KI-Outputs für Kanzleien prüfen: Anwendungsfall Kanzlei nutzt KI-System bei Personalentscheidungen Mandantenberatung oder Rechercheaufgaben und muss sicherstellen dass keine diskriminierenden Ergebnisse entstehen. AGG Allgemeines Gleichbehandlungsgesetz, Anhang III Nr. 4 KI-VO Hochrisiko-Personalwesen. Prüfraster Bias-Quellen identifizieren, AGG-relevante Kategorien prüfen, diskriminierende Outputs erkennen, Schulungsanforderungen. Output Bias-Prüfprotokoll mit Kategorien und Korrekturmassnahmen. Abgrenzung zu KI-VO-Hochrisiko-Personalwesen und zu Compliance-Regelsatz.

# Bias und Diskriminierung Prüfung

KI-Systeme werden auf Basis großer Textmengen trainiert, die Verzerrungen und gesellschaftliche Vorurteile enthalten können. Diese "Bias" können sich in den Outputs der KI-Systeme widerspiegeln und zu Diskriminierungen führen — besonders kritisch bei Personalentscheidungen, aber auch bei der Mandantenberatung zu diskriminierungsrechtlichen Fragen. Kanzleien müssen ihre Mitarbeitenden befähigen, Bias zu erkennen und zu korrigieren.

## Rechtlicher Hintergrund

§§ 1, 7 AGG (Allgemeines Gleichbehandlungsgesetz): Diskriminierungsverbot aufgrund von Rasse, Geschlecht, Religion, Behinderung, Alter oder sexueller Identität — gilt für Beschäftigung und privatrechtliche Verträge, damit auch für Mandatsbeziehungen. Art. 9 DSGVO: Besonders sensible Datenkategorien — rassische/ethnische Herkunft, religiöse Überzeugungen etc. — dürfen nicht Grundlage von Entscheidungen sein. Art. 10 Abs. 5 KI-VO: Hochrisiko-KI-Systeme müssen auf Bias geprüft werden; für Kanzleien gilt dies indirekt beim Einsatz von KI im Personalwesen (Anhang III Nr. 4). Art. 22 DSGVO: Keine ausschließlich automatisierten Entscheidungen mit diskriminierender Wirkung. BAG-Rechtsprechung zum AGG: Der Nachweis einer Benachteiligung kann durch statistische Indizien erbracht werden.

## Vorgehen

1. **Bias-Quellen verstehen**: KI-Systeme können systematisch bestimmte Gruppen bevorzugen oder benachteiligen — je nach Trainingsdaten, Aufgabenstellung und Prompt-Formulierung.
2. **Kritische Kontexte identifizieren**: Besonders anfällig: Bewerberauswahl, Beurteilung von Vertragsparteien, Formulierung von Texten zu diskriminierungsrechtlichen Themen.
3. **KI-Output auf Bias prüfen**: Enthält der Text unangemessene Verallgemeinerungen, stereotypische Formulierungen oder einseitige Bewertungen bestimmter Gruppen?
4. **AGG-Compliance bei Personalentscheidungen**: Stellt eine KI-Vorauswahl von Bewerbungen sicher, dass alle nach AGG geschützten Merkmale ausgeschlossen werden? Prüfung durch beauftragte Personalverantwortliche.
5. **Mitarbeitende schulen**: Schulungsmodul zu Bias-Erkennung entwickeln; konkrete Beispiele aus der juristischen Praxis verwenden.
6. **Interne Meldepflicht**: Bei festgestelltem Bias im KI-Output ist dieser intern zu melden und der Output nicht zu verwenden.

## Vorlagentext / Bausteine

**Baustein Bias-Sensibilisierung:**
KI-Systeme können aufgrund ihrer Trainingsdaten vorurteilsbehaftete Inhalte erzeugen, die gegen das AGG oder andere Diskriminierungsverbote verstoßen. Mitarbeitende sind angewiesen, KI-generierte Texte auf diskriminierende Formulierungen, Stereotypen oder einseitige Bewertungen zu prüfen. Derartige Inhalte sind zu löschen und intern zu melden. Eine Weiterverwendung ist nicht zulässig.

**Baustein AGG-Compliance Personalwesen:**
Beim Einsatz von KI-Systemen bei der Vorauswahl von Bewerbungen oder bei sonstigen Personalentscheidungen stellt die Kanzlei sicher, dass die nach § 1 AGG geschützten Merkmale (Rasse, ethnische Herkunft, Geschlecht, Religion oder Weltanschauung, Behinderung, Alter, sexuelle Identität) keine Rolle spielen. KI-generierte Bewerbungsbewertungen werden ausnahmslos von einer qualifizierten Personalverantwortlichen oder einem qualifizierten Personalverantwortlichen überprüft, bevor eine Entscheidung getroffen wird.

**Baustein Meldeverfahren:**
Stellt eine Mitarbeiterin oder ein Mitarbeiter fest, dass KI-generierter Output diskriminierende oder anderweitig problematische Inhalte enthält, ist dies unverzüglich an [Name Datenschutzbeauftragter/Compliance-Verantwortlicher] zu melden. Der fehlerhafte Output ist zu dokumentieren und nicht zu verwenden.

## Hinweise zur Aktualisierung

Die KI-Forschung zum Thema Bias entwickelt sich rasch weiter. Neue Erkenntnisse zur Bias-Anfälligkeit bestimmter KI-Systeme sollten in Schulungen aufgenommen werden. BAG-Entscheidungen zum AGG im Kontext von KI-Personalauswahl sowie Leitlinien der EU-Kommission zur Gleichbehandlung beim KI-Einsatz sind zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 1 AGG — Schutz vor Diskriminierung (Rasse, Geschlecht, Alter, Behinderung, Herkunft)
- § 15 AGG — Schadensersatz und Entschaedigung bei Diskriminierung
- Art. 22 DSGVO — Automatisierte Entscheidungen mit moeglichem Diskriminierungspotenzial
- Art. 5 Abs. 1 lit. c KI-VO — Verbot biometrischer Kategorisierung nach geschuetzten Merkmalen
- Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 KI-VO — Hochrisiko bei Bewerbungs-Screening, Personalauswahl und Beschäftigtenmanagement nach Zweckbestimmung

## Triage zu Beginn
1. Fuer welchen Zweck wird das KI-System eingesetzt — Bewerberauswahl, Mandatszuordnung, Leistungsbewertung?
2. Koennen Trainingsdaten historische Diskriminierungsmuster enthalten?
3. Sind schutzbeduerfte Gruppen nach AGG unverhältnismaessig betroffen?
4. Wurde ein Bias-Test durchgefuehrt — und sind die Ergebnisse dokumentiert?
5. Gibt es einen Widerspruchsmechanismus fuer Betroffene (Art. 22 Abs. 3 DSGVO)?

## Output-Template — Bias-Pruefprotokoll
**Adressat:** HR / Compliance — Tonfall: strukturiert, sachlich
```
BIAS-PRUEFPROTOKOLL
[DATUM] — System: [SYSTEMNAME] — Anwendungsfall: [BESCHREIBUNG]

Geschuetzte Merkmale (§ 1 AGG) — Analyse:
| Merkmal | Risiko | Nachweis | Massnahme |
|---|---|---|---|
| Geschlecht | [NIEDRIG/MITTEL/HOCH] | [TESTERGEBNIS] | [MASSNAHME] |
| Alter | [NIEDRIG/MITTEL/HOCH] | [TESTERGEBNIS] | [MASSNAHME] |
| Herkunft / Nationalitaet | [NIEDRIG/MITTEL/HOCH] | [TESTERGEBNIS] | [MASSNAHME] |
| Behinderung | [NIEDRIG/MITTEL/HOCH] | [TESTERGEBNIS] | [MASSNAHME] |

KI-VO Art. 5 Abs. 1 lit. c: Biometrische Kategorisierung: [NICHT VORHANDEN / PRUEFUNG ERFORDERLICH]
Anhang III Nr. 4 KI-VO: Hochrisiko: [JA / NEIN — je nach Zweckbestimmung]

Bias-Test durchgefuehrt: [JA — Methode: BESCHREIBUNG / NEIN — ERFORDERLICH]
Gesamtbewertung: [KEIN MATERIALLES BIAS / BIAS GEFUNDEN — MASSNAHMEN ERFORDERLICH]
Geprueft von: [NAME], [DATUM]
```

---

<!-- AUDIT 27.05.2026 -->
> **Audit-Hinweis (27.05.2026):** BGH VI ZR 273/16, NJW 2019, 2385 entfernt. Urteil existiert nicht — Suchanfrage auf dejure.org ergab keinen Treffer fuer BGH VI ZR 273/16 vom 26.03.2019. Beanspruchtes Thema (Produkthaftung fuer fehlerhafte Algorithmen) ist nicht durch diese Fundstelle belegt. Quelle: dejure.org Vernetzungssuche (NOT_FOUND).

## 2. `compliance-regelsatz-erstellen`

**Fokus:** Compliance-Regelsatz Zehn Gebote für KI-Einsatz in Kanzleien erstellen: Anwendungsfall Kanzlei benoetigt praegnante Verhaltensregeln für alle Mitarbeitenden zu erlaubten und verbotenen KI-Nutzungen. § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienstleister, Art. 4 KI-VO KI-Kompetenz. Prüfraster kein Privat-Account, keine Mandatsdaten ohne Anonymisierung, kein PDF-Upload ohne AVV, Korrekturlesung Pflicht, KI-Kennzeichnung. Output standardisierter Zehn-Gebote-Regelsatz anpassbar an Kanzlei-Profil. Abgrenzung zu Richtlinien-Skelett für vollständige Richtlinie und zu Berufsrecht-Bausteine.

# Compliance-Regelsatz erstellen

Ein klarer, prägnanter Compliance-Regelsatz ist das operative Herzstück jeder KI-Nutzungsrichtlinie. Er muss so formuliert sein, dass alle Mitarbeitenden — unabhängig von juristischem Hintergrund — die Kernregeln sofort verstehen und anwenden können. Dieser Skill erzeugt einen standardisierten Zehn-Gebote-Regelsatz, der an das Kanzlei-Profil angepasst werden kann.

## Rechtlicher Hintergrund

Der Regelsatz operationalisiert die zentralen Rechtspflichten: § 43a Abs. 2 BRAO (Verschwiegenheit), § 43e BRAO (IT-Dienstleister), Art. 5 DSGVO (Grundsätze der Verarbeitung: Zweckbindung, Datenminimierung), Art. 28 DSGVO (Auftragsverarbeitung), § 2 Abs. 2 UrhG (Urheberrecht am KI-Output), Art. 50 Abs. 4 KI-VO (Kennzeichnung), § 203 StGB (Geheimnisverrat), Art. 22 DSGVO (Verbot automatisierter Entscheidungen).

## Vorgehen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Zielgruppe definieren**: Unterschiedliche Regeln für anwaltliche und nicht-anwaltliche Mitarbeitende oder einheitlicher Regelsatz für alle?
2. **Zehn Gebote formulieren**: Aus den rechtlichen Anforderungen konkrete Handlungsregeln ableiten.
3. **Ausnahmen definieren**: Wann sind Ausnahmen zulässig (z.B. Upload mit AVV)?
4. **Kommunikation sicherstellen**: Regelsatz in Schulungen erklären, schriftlich quittieren lassen.
5. **Regelsatz plakativ aufbereiten**: Auf einer DIN-A4-Seite oder als Poster für Kanzleiräume aufbereiten.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — KI-Compliance-Regelsatz fuer Kanzlei erstellen | Regelsatz nach 10-Gebote-Schema; Template unten |
| Variante A — Kleine Kanzlei max drei Seiten | Kurzfassung Regelsatz; nur Kernregeln |
| Variante B — Mandant will Regelsatz in Englisch | Englischsprachige Vorlage; Terminologie anpassen |
| Variante C — Vorhandener Regelsatz aktualisieren | Nur geaenderte Stellen ueberarbeiten; Version-Tracking |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Vorlagentext / Bausteine

**Die Zehn Gebote für den KI-Einsatz in [Name der Kanzlei]:**

**1.** Wir nutzen beim Einsatz von KI-Systemen in der Kanzlei ausschließlich autorisierte Kanzlei-Accounts — niemals private Accounts.

**2.** Wir kopieren keine personenbezogenen Daten von Mandanten oder Mitarbeitenden in KI-Systeme, es sei denn, die Daten wurden zuvor vollständig anonymisiert.

**3.** Wir laden keine Dokumente, Akten oder Schriftstücke als Datei in einen KI-Dienst hoch, ohne diese zuvor anonymisiert zu haben — außer bei Anbietern, mit denen ein wirksamer Auftragsverarbeitungsvertrag nach Art. 28 DSGVO und eine § 43e-BRAO-Vereinbarung bestehen.

**4.** Wir korrekturlesen und prüfen jeden KI-generierten Text eigenverantwortlich auf inhaltliche Richtigkeit, bevor er intern oder extern weiterverwendet wird.

**5.** Wir verifizieren ausnahmslos jede Fundstelle, jedes Zitat und jeden Gesetzeshinweis aus KI-generiertem Output anhand der originalen Quelle. KI-Systeme können Fundstellen erfinden.

**6.** Wir kennzeichnen KI-generierte Inhalte in internen und externen Dokumenten, soweit dies die Transparenz erfordert. Bei anwaltlichen Schriftsätzen tragen wir durch unsere Unterschrift die volle redaktionelle Verantwortung.

**7.** Wir delegieren keine Letztentscheidung an ein KI-System. Jede rechtliche Bewertung und jede mandatsbezogene Entscheidung verbleibt beim Menschen.

**8.** Wir verarbeiten keine besonders sensiblen personenbezogenen Daten nach Art. 9 Abs. 1 DSGVO mit KI-Systemen, es sei denn, eine ausdrückliche Rechtfertigung nach Art. 9 Abs. 2 DSGVO liegt vor.

**9.** Wir laden keine urheberrechtlich geschützten Texte (Kommentare, Fachaufsätze, Datenbankexporte) in KI-Systeme hoch, ohne die erforderlichen Nutzungsrechte zu besitzen. Gesetze und Gerichtsentscheidungen von offiziellen Portalen sind frei nutzbar.

**10.** Wir melden jeden Verdachtsfall einer Compliance-Verletzung beim KI-Einsatz unverzüglich an [Name Datenschutzbeauftragter/Berufsrechtsbeauftragter/Geschäftsführung].

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Hinweise zur Aktualisierung

Der Regelsatz ist mindestens halbjährlich zu überprüfen. Bei wesentlichen Änderungen der genutzten KI-Dienste, bei neuen Gerichtsentscheidungen zur Haftung oder bei neuen BRAK/DAV-Hinweisen ist eine Aktualisierung geboten. Alle Mitarbeitenden müssen über Änderungen informiert und neu geschult werden.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a Abs. 2 BRAO — Verschwiegenheit
- § 43e BRAO — IT-Dienstleister-Anforderungen
- Art. 28 DSGVO — AVV-Pflicht
- Art. 5 Abs. 1 lit. c KI-VO — Verbotene biometrische Praktiken
- § 87 Abs. 1 Nr. 6 BetrVG — Mitbestimmung bei technischen Ueberwachungssystemen

## Triage zu Beginn
1. Welche KI-Systeme werden in der Kanzlei eingesetzt — ist eine Freigabeliste vorhanden?
2. Gibt es bereits einen Compliance-Regelsatz oder wird er neu erstellt?
3. Ist ein Betriebsrat vorhanden — wurde nach § 87 Abs. 1 Nr. 6 BetrVG eingebunden?
4. Sind alle Mitarbeiter ueber das Privat-Account-Verbot und die Anonymisierungspflicht informiert?
5. Gibt es Schulungsunterlagen zum Compliance-Regelsatz?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — Compliance-Regelsatz KI (10 Gebote)
**Adressat:** Alle Kanzlei-Mitarbeiter — Tonfall: verbindlich, klar
```
COMPLIANCE-REGELSATZ KI-EINSATZ — [KANZLEI]
Stand: [DATUM] — Version: [VERSIONSNUMMER]
VERBINDLICH FUER ALLE MITARBEITERINNEN UND MITARBEITER

1. KEIN PRIVAT-ACCOUNT: Nur freigegebene Kanzlei-Accounts verwenden.
2. KEINE MANDATSDATEN OHNE ANONYMISIERUNG: Vor jeder KI-Eingabe pseudonymisieren.
3. KEIN PDF-UPLOAD OHNE AVV: Dokumente nur in Systeme mit Art. 28 DSGVO-AVV hochladen.
4. KEINE UNKRITISCHE UEBERNAHME: Jede KI-Ausgabe ist vor Verwendung menschlich zu pruefen.
5. KENNZEICHNUNGSPFLICHT: KI-generierte Inhalte im Schriftsatz als solche kennzeichnen.
6. QUELLENVERIFIZIERUNG: Jede Rechtsprechungs-Fundstelle gegen amtliche Quellen pruefen.
7. KEINE VERTRAULICHEN DATEN IN NICHT-FREIGEGEBENE SYSTEME.
8. MELDEPFLICHT: Sicherheitsvorfall oder ungewoehnliches KI-Verhalten sofort melden an: [KONTAKT].
9. SCHULUNGSPFLICHT: Jaehrliche KI-Pflichtschulung erforderlich.
10. COMPLIANCE-OFFICER KONTAKTIEREN bei Unsicherheit: [KONTAKT].

Verabschiedet von: [GESCHAEFTSFUEHRUNG], [DATUM]
```

## 3. `dienstleister-due-diligence`

**Fokus:** KI-Dienstleister Due Diligence für Kanzleien durchführen: Anwendungsfall Kanzlei moechte neuen KI-Dienst beauftragen und muss eigenverantwortlich Datenschutz Berufsrecht und Sicherheit prüfen. § 43e BRAO Dienstleisterprüfung, Art. 28 Abs. 1 DSGVO Garantiepflichten, ISO 27001 SOC 2. Prüfraster EU-Sitz vs. US-Sitz, Enterprise-Tier mit Training-Opt-out, Verschluesselung, Zertifizierungen, Subprozessoren, Standardvertragsklauseln. Output Dienstleister-Bewertungsmatrix mit Ampelstatus und AVV-Empfehlung. Abgrenzung zu Auftragsverarbeitungsvertrag-Prüfen und zu Musterklauseln-IT.

# Dienstleister Due Diligence

Die sorgfältige Auswahl des KI-Dienstleisters ist eine zentrale berufsrechtliche und datenschutzrechtliche Pflicht. § 43e BRAO verpflichtet zur eigenverantwortlichen Prüfung des Dienstleisters; Art. 28 Abs. 1 DSGVO verlangt hinreichende Garantien für technisch-organisatorische Maßnahmen. Dieser Skill stellt strukturierte Auswahlkriterien bereit.

## Rechtlicher Hintergrund

§ 43e BRAO: Sorgfältige Auswahl und vertragliche Bindung des IT-Dienstleisters als Voraussetzung für die befugte Nutzung. § 43e Abs. 4 BRAO: Drittstaaten-Dienstleister zulässig bei vergleichbarem Schutzniveau. Art. 28 Abs. 1 DSGVO: Nur Auftragsverarbeiter mit hinreichenden Garantien beauftragen. Art. 44 ff. DSGVO: Drittlandtransfer nur mit geeigneten Schutzmaßnahmen (Angemessenheitsbeschluss, SCC, TIA). Art. 5 Abs. 1 lit. f DSGVO: Integrität und Vertraulichkeit durch geeignete technisch-organisatorische Maßnahmen. BRAK-Hinweise 12/2024: Sorgfältige Anbieterauswahl als berufsrechtliche Kernpflicht.

## Vorgehen

1. **Sitzland und Rechtsrahmen prüfen**: EU-Anbieter unterliegen direkt der DSGVO. Für US-amerikanische Anbieter: EU-US Data Privacy Framework-Zertifizierung prüfen; alternativ SCC + TIA.
2. **Enterprise-Tier auf Training-Opt-out prüfen**: Standardmäßige Verbraucherversionen vieler Chatbot-Dienste erlauben dem Anbieter, Eingaben zum Training zu nutzen. Enterprise-Verträge schließen dies in der Regel aus. Opt-out schriftlich bestätigen lassen.
3. **Verschlüsselung verifizieren**: Daten at rest (Speicherung) und in transit (Übertragung) müssen verschlüsselt sein. Mindeststandard: TLS 1.2 für Übertragung; AES-256 für Speicherung.
4. **Zertifizierungen prüfen**: ISO 27001 (Informationssicherheit), SOC 2 Type II (Sicherheit, Verfügbarkeit, Vertraulichkeit), ggf. ISO 27701 (Datenschutz). Aktuelle Zertifikate anfordern.
5. **Subprozessoren und Rechenzentrumsstandorte erfassen**: Wo werden die Daten tatsächlich verarbeitet und gespeichert?
6. **Vertragswerk vervollständigen**: AVV nach Art. 28 DSGVO + § 43e-BRAO-Vereinbarung + ggf. SCC abschließen.
7. **Dokumentierte Risikobeurteilung erstellen**: Eigene Prüfung und Abwägung der Risiken schriftlich festhalten.

## Vorlagentext / Bausteine

**Due-Diligence-Checkliste KI-Dienstleister:**

**Allgemeine Informationen:**
☐ Vollständige Firma und Rechtsform des Anbieters
☐ Sitz des Unternehmens (EU / EWR / Drittland)
☐ Standort der Rechenzentren
☐ Zuständige Datenschutzbehörde

**Datenschutz:**
☐ Datenschutzerklärung und Datenschutzrichtlinien liegen vor
☐ AVV nach Art. 28 DSGVO ist verfügbar / wird abgeschlossen
☐ Bei US-Anbietern: EU-US Data Privacy Framework-Zertifizierung oder SCC
☐ Expliziter Training-Opt-out für Kunden-Eingaben ist schriftlich vereinbart
☐ Lösch- und Aufbewahrungsfristen sind dokumentiert

**Technische Sicherheit:**
☐ Verschlüsselung at rest (mindestens AES-256)
☐ Verschlüsselung in transit (mindestens TLS 1.2)
☐ Multi-Faktor-Authentifizierung für Kanzlei-Accounts
☐ Incident-Response-Verfahren dokumentiert

**Zertifizierungen:**
☐ ISO 27001 (aktuelles Zertifikat)
☐ SOC 2 Type II (aktueller Bericht)
☐ Ggf. C5 (BSI Cloud Computing Compliance Criteria Catalogue)

**Berufsrecht:**
☐ § 43e-BRAO-Vereinbarung abgeschlossen
☐ Strafrechtliche Belehrung nach § 203 StGB erteilt

## Hinweise zur Aktualisierung

Die Zertifizierungen und die EU-US-Datenschutzrahmen sind regelmäßig auf Aktualität zu prüfen. Datenschutzbehörden-Entscheidungen zu einzelnen KI-Anbietern (z.B. Untersagungen durch DPAs) sind zu beobachten. Jährliche Neubeurteilung des eingesetzten Dienstleisters empfohlen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 28 Abs. 1 DSGVO — hinreichende Garantien des Auftragsverarbeiters
- Art. 46 DSGVO — Drittlandtransfer-Sicherheitsnetz (SCC, Angemessenheitsbeschluss)
- § 43e BRAO — IT-Dienstleister in Kanzleien
- Art. 9 KI-VO — Risikomanagementsystem Anbieter-Anforderungen

## Triage zu Beginn
1. Wo hat der KI-Dienstleister seinen Sitz — EU, USA oder sonstiges Drittland?
2. Gibt es einen Enterprise-Tier mit Training-Opt-out — oder ist Training auf Eingaben Standard?
3. Welche Zertifizierungen weist der Anbieter vor (ISO 27001, SOC 2, BSI C5)?
4. Sind Standardvertragsklauseln und eine Transferfolgenabschaetzung vorhanden?
5. Ist der Anbieter CLOUD Act-Risiken ausgesetzt (US-Muttergesellschaft)?

## Output-Template — Dienstleister-Due-Diligence-Bericht
**Adressat:** Kanzlei-Management / DSB — Tonfall: strukturiert, risikoorientiert
```
DIENSTLEISTER-DUE-DILIGENCE
[DATUM] — Anbieter: [NAME] — Zweck: [BESCHREIBUNG]

SITZ: [LAND]
EU-Datenzentrum: [JA / NEIN — Standort: BESCHREIBUNG]
Training auf Eingaben: [NEIN (Enterprise-Tier) / JA — UNZULAESSIG fuer Mandatsdaten]
CLOUD Act-Risiko: [NIEDRIG / HOCH — Begruendung]

Zertifizierungen:
☑/☐ ISO 27001
☑/☐ SOC 2 Typ II
☑/☐ BSI C5

Datentransfer-Absicherung:
☑/☐ Angemessenheitsbeschluss (EU-US Data Privacy Framework)
☑/☐ Standardvertragsklauseln
☑/☐ Transferfolgenabschaetzung (TIA) durchgefuehrt

Gesamtbewertung: [FREIGEGEBEN / BEDINGT / ABGELEHNT]
Auflagen: [BESCHREIBUNG]
Geprueft von: [NAME], [DATUM]
```

<!-- AUDIT 27.05.2026
Halluzinations-Reparatur Bundle 035:
-->
