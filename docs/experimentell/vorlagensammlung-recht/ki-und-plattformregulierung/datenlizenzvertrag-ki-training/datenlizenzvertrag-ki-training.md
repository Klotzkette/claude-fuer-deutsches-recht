# Datenlizenzvertrag für KI-Training und Modellvalidierung

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Vertragsbestandteil, nicht mit unterzeichnen]

Trainingsdaten können personenbezogene Daten, Geschäftsgeheimnisse, urheberrechtlich geschützte Inhalte oder Datenbankrechte enthalten. Rechtekette und Löschbarkeit müssen belegt sein.

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch keinen Vertrag, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Vertragseingang und Bearbeitungsstand

Datengeberin ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Datennehmerin ist [vollständiger Name oder Firma, Rechtsform, Register, Sitz, Anschrift, Vertretung].

Weitere Beteiligte / Zustimmungsberechtigte sind [Name, Rolle, Vertretung / keine].

Der Bearbeitungsstand ist [Entwurf / Verhandlung / Unterzeichnung / Vollzug], Datum: [Datum], Akte: [Az.].

## 1. Präambel / Gegenstand

1.1 Die Datengeberin lizenziert der Datennehmerin den in Anlage 1 beschriebenen Datensatz ausschließlich zur Entwicklung, zum Training, zur Validierung und zur Qualitätssicherung des bezeichneten KI-Systems.

1.2 Diese Vereinbarung trennt erlaubte Trainingsnutzung, verbotene Re-Identifizierung, Weitergabe an Modellanbieter, Umgang mit personenbezogenen Daten, Geschäftsgeheimnissen, Urheberrechten, Datenbankrechten und Löschpflichten.

## 2. Vertragsgegenstand und Abgrenzung

2.1 Vertragsgegenstand ist der Datensatz [Bezeichnung] mit Umfang, Herkunft, Datenfeldern, Aktualitätsstand, Bereitstellungsformat, Dokumentation, Ausschlüssen und Rechtekette nach Anlage 1.

2.2 Nicht eingeräumt werden Rechte zur Re-Identifizierung, zum Training fremder Foundation-Modelle außerhalb des vereinbarten Systems, zur Veröffentlichung von Rohdaten, zur Nutzung sensibler Daten ohne Rechtsgrundlage oder zur Weitergabe an Dritte ohne Freigabe nach Anlage 2.

2.3 Datensatzbeschreibung, Rechtekette, Provenienzvermerk, TOM-Matrix, Zweckfreigabe, Modellartefaktliste und Rückrufprotokoll gelten nur in der freigegebenen Fassung. Bei Widersprüchen geht der individuell unterzeichnete Datenlizenzvertrag vor.

2.4 Lizenzierung und Kontrolle des Datensatzes erfolgen nach folgenden Regeln:

2.4.1 Der lizenzierte Datensatz darf nur für die in Anlage 2 bezeichneten Trainings-, Test-, Validierungs- und Evaluationszwecke verwendet werden.

2.4.2 Re-Identifizierung, Profilbildung außerhalb des Projektzwecks, Rohdatenweitergabe und Nutzung zur Erstellung nicht freigegebener Modellartefakte sind ausgeschlossen.

2.4.3 Technische und organisatorische Maßnahmen, Pseudonymisierung, Zugriffskontrolle, Protokollierung, Löschfristen und etwaige Auftragsverarbeitung ergeben sich aus Anlage 3.

2.4.4 Modellartefakte, Gewichte, Embeddings, synthetische Daten, Audit-Rechte und Rückrufmechanismen bei rechtswidrigen Daten werden in Anlage 4 dokumentiert.

## 3. Pflichten: Datengeberin

3.1 Datengeberin stellt die in Anlage 1 bezeichneten Unterlagen vollständig, richtig und aktuell bereit.

3.2 Die Datengeberin informiert die Datennehmerin unverzüglich in Textform über Widerrufe, Sperrvermerke, Löschpflichten, Rechtekettenlücken, Personenbezug, Zweckbindungsbeschränkungen, Drittlandrisiken und jeden Rückrufgrund, der Training, Validierung oder Weiterverwendung der lizenzierten Daten berührt.

3.3 Die Datengeberin steht für die in Anlage 1 dokumentierte Herkunft, Lizenzierbarkeit und Nutzungsbeschränkung des Datensatzes ein. Sie garantiert weder Trainingserfolg noch Modellgüte, Nichtdiskriminierung, regulatorische Zulassung oder Freiheit von allen statistischen Verzerrungen.

3.4 Die Datengeberin führt eine Datenherkunfts- und Rechteakte, in der Quelle, Erhebungszweck, Rechtsgrundlage, Nutzungsrechte, Ausschlüsse, Personenbezug, Pseudonymisierung, Löschfrist, Trainingsfreigabe und Rückrufrisiko jedes Datensatzes dokumentiert werden. Die Akte ist Anlage 2 zuzuordnen und vor Unterzeichnung freizugeben.

## 4. Pflichten: Datennehmerin

4.1 Datennehmerin verarbeitet den Datensatz ausschließlich in den freigegebenen Trainings-, Test- und Validierungsumgebungen, trennt Rohdaten von Modellartefakten und dokumentiert Zugriffe, Kopien, Löschungen und Embedding-Stores.

4.2 Die Datennehmerin prüft Datensatzbeschreibung, Lizenzkette, Ausschlusslisten, Personenbezug, Pseudonymisierungsvorgaben, Löschfristen, Zugriffskontrollen und Modellartefakt-Trennung unverzüglich auf erkennbare Trainingssperren. Beanstandungen, die Training, Audit, Rückruf oder Löschung berühren, meldet sie binnen [fünf Bankarbeitstagen] in Textform.

4.3 Datennehmerin darf Unterlagen, Daten und Rechte nur für den Vertragszweck verwenden und nur an Personen weitergeben, die für Prüfung, Vollzug, Finanzierung, Beratung oder Rechtsdurchsetzung erforderlich sind.

4.4 Modellartefakte, Audit-Rechte und Rückrufmechanismen richten sich zusätzlich nach 2.4.4 und Anlage 4.

## 5. Lizenzentgelt und wirtschaftlicher Ausgleich

5.1 Das Lizenzentgelt beträgt [Betrag in EUR / Berechnungsformel] zuzüglich Umsatzsteuer, soweit diese anfällt; nutzungsabhängige Entgelte, Auditkosten und Rückrufkosten werden nach Anlage 4 abgerechnet.

5.2 Das Lizenzentgelt wird nach Bereitstellung des freigegebenen Datensatzes, Abschluss der in Anlage 3 bezeichneten Sicherheitsprüfung und Zugang einer prüffähigen Rechnung fällig.

5.3 Gerät eine Partei mit einer fälligen Zahlung in Verzug, gelten §§ 286, 288 BGB, soweit deutsches Recht anwendbar ist; weitergehender konkret nachgewiesener Schaden bleibt vorbehalten.

5.4 Aufrechnung und Zurückbehaltung sind nur mit unbestrittenen, rechtskräftig festgestellten oder aus demselben Vertragsverhältnis entscheidungsreifen Ansprüchen zulässig, soweit AGB-rechtlich wirksam.

## 6. Risiko, Haftung und Leistungsstörungen

6.1 Die Lizenzgeberin haftet für schuldhaft unrichtige Herkunfts-, Rechteketten- und Opt-out-Angaben sowie vertragswidrig kontaminierte Datensätze. Die Lizenznehmerin haftet für Nutzung außerhalb von Zweck, Modellfamilie, Laufzeit oder zulässigem Nutzerkreis und für unterlassene Sperrung nach einer konkretisierten Rechte- oder Löschungsmitteilung.

6.2 Haftungsbeschränkungen gelten nicht für Vorsatz, grobe Fahrlässigkeit, Verletzung von Leben, Körper oder Gesundheit, arglistiges Verschweigen, ausdrücklich übernommene Garantien oder zwingende gesetzliche Haftung.

6.3 Die Lizenzgeberin meldet Rechtekettenlücken, Widersprüche betroffener Personen, Löschpflichten, Herkunftsfehler und nachträgliche Nutzungsbeschränkungen datensatz- und versionsbezogen. Die Lizenznehmerin sperrt betroffene Daten für neue Trainingsläufe, kennzeichnet beeinflusste Modellversionen und dokumentiert Entfernung, Retraining oder begründete Nichtentfernbarkeit.

## 7. Compliance und Datenschutz

7.1 Die Parteien dokumentieren Urheber-, Datenbank-, Geschäftsgeheimnis- und Persönlichkeitsrechte, zulässige Text-und-Data-Mining-Nutzung, Opt-outs, KI-rechtliche Daten-Governance sowie Sanktions- und Exportkontrollbezüge. Ungeklärte Quellen werden nicht in produktive Trainingskorpora übernommen.

7.2 Enthält der Datensatz personenbezogene Daten, weist Anlage [Nummer] Zweck, Rechtsgrundlage, Rollen, Betroffeneninformationen, besondere Kategorien, Herkunft, Löschlogik und Drittlandtransfers aus. Auftragsverarbeitung oder gemeinsame Verantwortlichkeit wird nicht pauschal unterstellt, sondern anhand der tatsächlichen Entscheidungsbefugnisse festgelegt.

## 8. Laufzeit, Beendigung und Rückabwicklung

8.1 Die Lizenz beginnt mit Bereitstellung der Dataset-Version [Version] am [Datum] und gilt für [einmaligen Trainingslauf / bezeichnete Modellfamilie / Laufzeit bis Datum]. Neue Dataset- oder Modellversionen sind nur erfasst, wenn sie in einem signierten Versionsblatt aufgenommen werden.

8.2 Bei fehlender Rechtekette, rechtswidrigen Daten, missachteten Opt-outs oder Nutzung außerhalb des Lizenzzwecks kann die betroffene Partei die weitere Verarbeitung der betroffenen Daten sofort aussetzen. Heilbare Metadaten- oder Dokumentationsmängel sind binnen [Anzahl] Bankarbeitstagen datensatzbezogen zu korrigieren.

8.3 Nach Lizenzende löscht oder sperrt die Lizenznehmerin Rohdaten, Kopien und abgeleitete Trainingsartefakte nach der vereinbarten Löschmatrix. Ob bereits trainierte Modellgewichte weiter genutzt werden dürfen, richtet sich ausschließlich nach [Fortbestandsvariante, Modellversion und dokumentierter technischer Trennbarkeit].

## 9. Schlussbestimmungen

9.1 Änderungen und Ergänzungen bedürfen der Textform, soweit nicht gesetzlich strengere Form vorgeschrieben ist. Individualabreden haben Vorrang.

9.2 Es gilt das Recht der Bundesrepublik Deutschland, soweit nicht zwingendes ausländisches Recht, Unionsrecht oder Aufsichtsrecht eingreift.

9.3 Gerichtsstand ist [Ort], soweit gesetzlich zulässig. Zwingende Gerichtsstände, Aufsichtsverfahren und insolvenzrechtliche Zuständigkeiten bleiben unberührt.

9.4 Sollte eine Bestimmung unwirksam sein oder werden, bleibt der Vertrag im Übrigen wirksam. Die Parteien ersetzen die unwirksame Bestimmung durch eine wirksame Regelung, die dem wirtschaftlichen Zweck am nächsten kommt.

### Schluss, Unterzeichnung und Freigabe

[Ort], den [Datum]

| Für Datengeberin | Für Datennehmerin |
|---|---|
| _____________________________ | _____________________________ |
| [Name, Funktion, Vertretungsrolle] | [Name, Funktion, Vertretungsrolle] |

## Anlagen

| Anlage | Bezeichnung |
| --- | --- |
| Anlage 1 | Sachverhalts-, Rechte- und Unterlagenverzeichnis |
| Anlage 2 | Vollzugsvoraussetzungen und Prüfmatrix |
| Anlage 3 | TOM, Pseudonymisierung und Auftragsverarbeitung |
| Anlage 4 | Modellartefakte, Audit und Rückrufmechanismus |

### Anlage 1 — Sachverhalts-, Rechte- und Unterlagenverzeichnis

1. Identifikation

1.1 Akte: [Az.]

1.2 Datum: [JJJJ-MM-TT]

1.3 Beteiligte: [Beteiligte]

1.4 Dokumentenstand: [Entwurf / freigegeben]

2. Unterlagen

2.1 Hauptvertrag oder Term Sheet: [Bezeichnung]

2.2 Dataset-Versionen, Herkunft, Rechtekette, Opt-outs, Datenbankrechte, Metadaten und beeinflusste Modellversionen: [Nachweise je Datenquelle]

2.3 Datenschutz, Text-und-Data-Mining, KI-Daten-Governance, Drittlandtransfer, Sanktionen und Exportkontrolle: [Prüfstatus je Dataset]

2.4 Offene Punkte: [Liste]

3. Freigabe

3.1 Fachliche Prüfung: [Name], [Datum]

3.2 Versand- oder Unterzeichnungsfreigabe: [Name], [Datum]

### Anlage 3 — TOM, Pseudonymisierung und Auftragsverarbeitung

1. Datenbestand

1.1 Datensätze, Quellen, Erhebungszeitraum, Rechtsgrundlagen, Ausschlüsse und Löschfristen werden je Datenkategorie beschrieben.

1.2 Personenbezogene Daten, besondere Kategorien personenbezogener Daten, Geschäftsgeheimnisse, urheberrechtlich geschützte Inhalte und synthetische Daten werden getrennt ausgewiesen.

2. Schutzmaßnahmen

2.1 Pseudonymisierung, Hashing, Zugriffskontrolle, Mandantentrennung, Protokollierung, Verschlüsselung, Löschkonzept und Exportbeschränkung werden vor Übergabe getestet.

2.2 Trainingsdaten dürfen nur in freigegebenen Umgebungen verarbeitet werden; Kopien, Zwischendumps und Embedding-Stores werden mit Speicherort und Löschfrist dokumentiert.

3. Auftragsverarbeitung

3.1 Liegt Auftragsverarbeitung vor, werden Gegenstand, Dauer, Weisungen, Unterauftragnehmer, Kontrollrechte und Rückgabe oder Löschung gesondert dokumentiert.

3.2 Liegt keine Auftragsverarbeitung vor, wird die eigenständige Verantwortlichkeit mit Rechtsgrundlage, Zweckbindung und Interessenabwägung zur Akte genommen.

### Anlage 4 — Modellartefakte, Audit und Rückrufmechanismus

1. Modellartefakte

1.1 Zu dokumentieren sind Modellversion, Trainingslauf, Datensatzversion, Gewichte, Embeddings, Tokenizer, Feature Stores, synthetische Daten und Evaluationsberichte.

1.2 Die Datennehmerin trennt Artefakte, die den lizenzierten Datenbestand reproduzierbar enthalten können, von bloßen statistischen Auswertungen.

2. Audit

2.1 Audit-Rechte bestehen bei konkretem Verdacht auf vertragswidrige Nutzung, unzulässige Datenquelle, fehlende Löschung oder rechtswidrige Reproduktion.

2.2 Das Audit wahrt Geschäftsgeheimnisse, Sicherheitsinteressen und Rechte Dritter; technische Nachweise können durch unabhängige Sachverständige geprüft werden.

3. Rückruf

3.1 Wird ein Datensatz als rechtswidrig, unzulässig lizenziert oder personenbezogen unzulässig verarbeitet erkannt, sperrt die Datennehmerin weitere Nutzung unverzüglich.

3.2 Rückrufmaßnahmen umfassen Entfernung aus Trainingskorpora, Sperre betroffener Artefakte, erneute Bewertung von Modelloutputs, Löschbestätigung und Bericht an die Datengeberin.

---

Lizenz: Apache-2.0 OR MIT.
