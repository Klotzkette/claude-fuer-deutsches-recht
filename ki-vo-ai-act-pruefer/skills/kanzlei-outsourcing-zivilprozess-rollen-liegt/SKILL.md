---
name: kanzlei-outsourcing-zivilprozess-rollen-liegt
description: "Kanzlei Outsourcing Zivilprozess Rollen Liegt: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kanzlei Outsourcing Zivilprozess Rollen Liegt

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Kanzlei Outsourcing Zivilprozess Rollen Liegt** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-ki-outsourcing-berufsgeheimnis` | KI-Outsourcing fuer Kanzleien und Rechtsabteilungen: Mandatsgeheimnis, Auftragsverarbeitung, Berufsrecht, Datenklassen, Subdienstleister, Drittlandtransfer, Prompt-Logging, Loeschung, Audit und Mandantenfreigabe. |
| `ki-im-zivilprozess-rollen-und-grenzen` | KI im Zivilprozess: Einsatz durch Partei, Anwalt, Gericht, Sachverstaendige und Justizverwaltung. Prueft KI-VO, ZPO, Berufsrecht, Beweisrecht, richterliche Verantwortung, rechtliches Gehoer und Grenzen automatisierter Entscheidungsunterstuetzung. |
| `liegt-ki-system-vor-art-3-nr-1` | Erster Schritt jeder KI-VO-Pruefung: Ist die Software, API, App, Automatisierung oder Modellkette ein KI-System nach Art. 3 Nr. 1 KI-VO? Prueft maschinenbasiertes System, Autonomie, optionale Adaptivitaet, Ziele, Inferenz, Output-Typen und Umweltbeeinflussung nach den Kommissionsleitlinien. Problematisiert Automation und Autonomie statt schematisch abzuhaken. Output: dokumentierbarer KI-System-Einordnungsvermerk mit Tatsachenbasis, Unsicherheiten und Folge-Skills. |
| `mandatsabbruch-empfehlung-komplexe-faelle` | Mechanik-erkennt Anzeichen von Faellen die anwaltliche Spezialkenntnisse erfordern und empfiehlt Eskalation. Indikatoren für Komplexitaet jenseits des KI-VO-Prüfers: multijurisdiktionelle Lieferketten marktbeherrschende Stellung KI und Waettbewerb hochspezialisierte Zertifizierungen Auslegungsstreit. Prüfraster: Schwellenwerte Mehrfachrollen kombinierte Hochrisiko-GPAI-Systeme laufende Vertragsprüfung. Output: Eskalationsempfehlung mit Begründung und Verweis auf IT-Recht Datenschutz Produktsicherheit. Abgrenzung zu triage-ki-vo-vorprüfung (Eingangs-Triage). |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Kanzlei Outsourcing Zivilprozess Rollen Liegt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-ki-outsourcing-berufsgeheimnis`

**Fokus:** KI-Outsourcing fuer Kanzleien und Rechtsabteilungen: Mandatsgeheimnis, Auftragsverarbeitung, Berufsrecht, Datenklassen, Subdienstleister, Drittlandtransfer, Prompt-Logging, Loeschung, Audit und Mandantenfreigabe.

# Kanzlei-KI-Outsourcing und Berufsgeheimnis

## Zweck

Der Skill erzeugt eine belastbare Prüfung, ob eine Kanzlei oder Rechtsabteilung ein KI-System fuer Aktenanalyse, Recherche, Dokumentenentwurf, Übersetzung oder Review einsetzen darf.

## Norm- und Berufsrechtsanker

- StGB § 203 und BRAO § 43a für Berufsgeheimnis/Verschwiegenheit; BRAO § 43e für Dienstleistereinbindung bei anwaltlicher Berufsausübung prüfen.
- BORA, CCBE-/Kammerhinweise und Mandatsvereinbarung nur konkret und aktuell verwenden; keine pauschale "KI erlaubt/verboten"-Aussage.
- DSGVO Art. 5, 6, 28, 32, 44 ff. für Rollen, Auftragsverarbeitung, TOM und Drittlandtransfer.
- GeschGehG und vertragliche NDAs, wenn Mandanten Geschäftsgeheimnisse oder Transaktionsdaten liefern.
- KI-VO Art. 3, Art. 50 und bei Rechtsanwendungs-/Justiznähe Art. 6 Abs. 2 i. V. m. Anhang III Nr. 8 prüfen.

## Prüfraster

1. **Datenklasse:** öffentlich, intern, vertraulich, Mandatsgeheimnis, besondere Kategorien, Straf-/Bußgeldakte.
2. **Toolklasse:** Consumer, Enterprise, eigener Tenant, lokales Modell, Dienstleisterreview.
3. **Verarbeitung:** Training, Prompt-Logging, Auswertung, Speicherung, Subprozessoren.
4. **Rechtsgrundlage:** Datenschutz, Berufsrecht, Geheimnisschutz, Vertrag.
5. **Mandantenbezug:** Braucht es Information, Zustimmung oder Mandatsvereinbarung?
6. **Technik:** Verschlüsselung, Mandantentrennung, Löschung, Export, Audit, Notfall.
7. **Arbeitsprozess:** menschlicher Review, Quellencheck, Freigabe.
8. **Berufsrechtlicher Nachweis:** Dienstleister-Due-Diligence, Weisungen, Zugriffskontrolle, Protokolle, Subdienstleisterkette und Mandantenkommunikation dokumentieren.
9. **Fehler-/Halluzinationsrisiko:** Zitatprüfung, Quellenprüfung, Vier-Augen-Freigabe und Schriftsatzverantwortung explizit regeln.

## Vertragsbausteine

Erstelle bei Bedarf:

- KI-Dienstleister-DD-Fragen.
- Auftragsverarbeitungs- und Subprozessoren-Check.
- Mandantenhinweis zur KI-Nutzung.
- Kanzleiinterne Freigabematrix.
- Verbotene Nutzungen.

## Qualitätsregel

Nicht abstrakt "Cloud ist verboten" oder "Cloud ist erlaubt" sagen. Entscheidend ist die konkrete Datenklasse, technische Kontrolle und berufliche Verantwortlichkeit.

## 2. `ki-im-zivilprozess-rollen-und-grenzen`

**Fokus:** KI im Zivilprozess: Einsatz durch Partei, Anwalt, Gericht, Sachverstaendige und Justizverwaltung. Prueft KI-VO, ZPO, Berufsrecht, Beweisrecht, richterliche Verantwortung, rechtliches Gehoer und Grenzen automatisierter Entscheidungsunterstuetzung.

# KI im Zivilprozess

## Rollen trennen

| Rolle | Zulässiger Nutzen | Risiko |
|---|---|---|
| Partei | Sachverhalt ordnen, Dokumente vorbereiten | ungeprüfte Tatsachen, Geheimnisse |
| Anwalt | Recherchehilfe, Entwurf, Aktenextraktion | Halluzinationen, Berufsrecht, Mandatsgeheimnis |
| Gericht | Organisation, Recherche, Entwurfshilfe | richterliche Verantwortung, rechtliches Gehör |
| Sachverständiger | Datenanalyse, Modellierung | Methodenoffenlegung, Nachvollziehbarkeit |
| Justizverwaltung | Aktenrouting, Übersetzung, Statistik | Anhang III Justiz-Hochrisiko, Grundrechte |

## KI-VO-Fragen

- Ist das Tool ein KI-System nach Art. 3 Nr. 1 KI-VO?
- Wird es fuer Justizverwaltung, Rechtsanwendung oder Entscheidungsunterstützung verwendet?
- Betrifft der Einsatz Anhang III: rechtliche Tatsachen- oder Rechtsbewertung im konkreten Fall?
- Gibt es Transparenz, Logging, menschliche Kontrolle und Dokumentation?

## Prozessuale Leitplanken

- Das Gericht muss verantwortlich entscheiden; KI darf keine heimliche Entscheidungsinstanz werden.
- Parteien müssen erheblichen Vortrag erkennen und bestreiten können.
- Quellen, Datenbasis und Methode müssen bei entscheidungsrelevanter KI nachvollziehbar sein.
- Bei KI-generierten Schriftsätzen bleibt die Verantwortung beim Einreichenden.

## Output

Erzeuge eine Rollenmatrix mit:

- Einsatzart;
- rechtlichem Risiko;
- erforderlichem Hinweis oder Vermerk;
- Beweis- und Akteneinsichtsfrage;
- Vorschlag fuer sichere Nutzung.

## 3. `liegt-ki-system-vor-art-3-nr-1`

**Fokus:** Erster Schritt jeder KI-VO-Pruefung: Ist die Software, API, App, Automatisierung oder Modellkette ein KI-System nach Art. 3 Nr. 1 KI-VO? Prueft maschinenbasiertes System, Autonomie, optionale Adaptivitaet, Ziele, Inferenz, Output-Typen und Umweltbeeinflussung nach den Kommissionsleitlinien. Problematisiert Automation und Autonomie statt schematisch abzuhaken. Output: dokumentierbarer KI-System-Einordnungsvermerk mit Tatsachenbasis, Unsicherheiten und Folge-Skills.

# Liegt ein KI-System vor? — Art. 3 Nr. 1 KI-VO

## Zweck

Dieser Skill ist das Eingangstor der KI-VO-Prüfung. Er klärt, ob der geprüfte Gegenstand überhaupt ein KI-System im Sinne der Verordnung (EU) 2024/1689 ist. Ohne KI-System greifen die KI-VO-Pflichten grundsätzlich nicht; mit KI-System folgen Anwendungsbereich, Rollen und Risikoklasse.

Der Skill arbeitet nicht mit einem starren Alles-oder-Nichts-Schema. Er erstellt eine nachvollziehbare Einordnung anhand der sieben Elemente der Legaldefinition und dokumentiert, welche Tatsachen die Einordnung tragen.

## Prüfgegenstand sauber bestimmen

Vor der Definition immer zuerst klären:

1. Was genau wird geprüft: Modell, API, Chatbot-Oberfläche, Workflow-Automation, SaaS-Modul, eingebettete Komponente oder Gesamtprodukt?
2. Wer setzt es wofür ein: Anbieter, Betreiber, interne Fachabteilung, Kunde, Behörde?
3. Welche Eingaben werden verarbeitet und welche Ausgaben werden erzeugt?
4. Wird die Ausgabe nur angezeigt, als Vorschlag genutzt oder in Entscheidungen/Prozesse eingespeist?
5. Ist die fragliche Funktion selbst KI-basiert oder nur eine Umgebung um ein fremdes KI-System?

Wenn mehrere Komponenten zusammenwirken, trenne:
- KI-Komponente
- Umgebende konventionelle Software
- Menschliche Entscheidungsschritte
- Nachgelagerte Nutzung der Ausgaben

## Legaldefinition — Arbeitsfassung

Ein KI-System ist nach Art. 3 Nr. 1 KI-VO ein maschinenbasiertes System, das für einen Betrieb mit unterschiedlichem Grad an Autonomie ausgelegt ist, nach Einführung anpassungsfähig sein kann und aus Eingaben für explizite oder implizite Ziele ableitet, wie Ausgaben wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen erzeugt werden, die physische oder virtuelle Umgebungen beeinflussen können.

Die Kommissionsleitlinien zur Definition des KI-Systems sind bei Grenzfällen ausdrücklich mitzudenken. Sie sind nicht selbst der Normtext, aber derzeit die wichtigste Auslegungshilfe.

## Sieben Elemente der Prüfung

### 1. Maschinenbasiertes System

Prüfe, ob Software, Hardware, Server, Cloud-Dienst, Edge-Gerät oder eine sonstige technische Infrastruktur die Funktion trägt.

Indizien:
- Ausführung auf Computer, Server, Smartphone, Sensor, Cloud oder eingebettetem Gerät
- API-Aufruf an ein Modell oder einen KI-Dienst
- Softwaremodul in einem Fachverfahren

Nicht ausreichend:
- rein menschliche Entscheidung ohne technische Ausgabegenerierung
- statisches Dokument, Checkliste oder manuelles Formular

### 2. Betrieb mit unterschiedlichem Grad an Autonomie

Autonomie bedeutet nicht, dass das System völlig allein handelt. Es genügt regelmäßig, dass es Ausgaben ohne menschliche Einzelbestimmung jedes Zwischenschritts erzeugt.

Prüffragen:
- Erzeugt das System nach Start oder Eingabe selbst eine Ausgabe, ohne dass ein Mensch jeden Rechenschritt vorgibt?
- Wählt, gewichtet, klassifiziert, generiert, priorisiert oder empfiehlt das System eigenständig?
- Kann ein Mensch die Ausgabe nur noch prüfen, übernehmen oder verwerfen?

Wichtig für die Bewertung:
- Hohe Automation spricht deutlich für ein KI-System, wenn Ausgaben aus Eingaben abgeleitet werden.
- Reine Automation ist nicht allein entscheidend: Ein Skript, das starr kopiert, sortiert oder feste Regeln ausführt, kann konventionelle Software bleiben.
- Autonomie darf nicht überhöht werden. Auch ein System mit menschlicher Freigabe kann KI-System sein, wenn die eigentliche Ausgabegenerierung inferenzbasiert erfolgt.

### 3. Adaptivität nach Einführung

Adaptivität ist optional. Ein System kann KI-System sein, obwohl es nach Deployment nicht weiterlernt.

Indizien:
- Training, Fine-Tuning, Reinforcement Learning, Online Learning
- Anpassung an Nutzerverhalten oder Kontext
- Modellupdates oder Retrieval-/Tool-Konfigurationen, die Verhalten verändern

Bewertung:
- Adaptivität verstärkt die KI-Einordnung.
- Fehlende Adaptivität schließt die KI-Einordnung nicht aus.

### 4. Explizite oder implizite Ziele

Prüfe, welchem Zweck die Ausgaben dienen.

Beispiele:
- Bewerber ranken
- Ausfallwahrscheinlichkeit prognostizieren
- Rechtsfrage zusammenfassen
- Notrufe priorisieren
- Bildinhalt erkennen
- Kundenanfrage beantworten

Auch implizite Ziele zählen, etwa Optimierung von Conversion, Produktivität, Risikosenkung oder Entscheidungsvorbereitung.

### 5. Inferenz aus Eingaben

Inferenz ist der Kern. Das System muss aus Eingaben ableiten, wie es eine Ausgabe erzeugt.

Typische Inferenz:
- maschinelles Lernen, neuronale Netze, Transformer, generative Modelle
- Klassifikation, Scoring, Ranking, Clustering, Regression
- Empfehlungen auf Grundlage gelernter Muster
- Bild-, Sprach-, Text- oder Mustererkennung

Grenzfälle:
- Einfache Suche, Sortierung, SQL-Abfrage oder Formularvalidierung reicht regelmäßig nicht.
- Ein hartcodierter Entscheidungsbaum ist regelmäßig keine KI, wenn alle Regeln und Schwellen ausschließlich menschlich festgelegt sind.
- Statistik ist nicht automatisch KI. Deskriptive Statistik bleibt regelmäßig draußen; Vorhersage-, Klassifikations- oder Empfehlungssysteme überschreiten die Schwelle eher.

### 6. Ausgabetyp

Mindestens ein typischer Ausgabetyp muss vorliegen:
- Vorhersage, Score, Wahrscheinlichkeit, Risikoindikator
- Inhalt, etwa Text, Bild, Audio, Video, Code
- Empfehlung, Ranking, Priorisierung, Next-best-action
- Entscheidung, Klassifikation, Freigabe, Ablehnung, Zuweisung

Der Begriff ist weit. Auch ein "nur vorbereitender" Score kann ein relevanter Output sein.

### 7. Einfluss auf physische oder virtuelle Umgebungen

Die Ausgabe muss physische oder virtuelle Umgebungen beeinflussen können. Ein mittelbarer Einfluss genügt.

Beispiele:
- Mensch übernimmt Empfehlung in Personal-, Kredit-, Versicherungs- oder Verwaltungsentscheidung
- System steuert Prozess, Maschinenlogik, Zugriff, Priorisierung oder Anzeige
- Ausgabe prägt Kommunikation, Sachbearbeitung, Aktenauswertung oder Dokumentation

Wenn eine Ausgabe nur testweise erzeugt und nie verwendet wird, dokumentiere das. Für Produktivsysteme reicht oft schon die reale Möglichkeit, dass Ausgaben in Prozesse einfließen.

## Entscheidungsmatrix

| Befund | Ergebnisrichtung |
|---|---|
| Maschinenbasiert + Inferenz + Output mit möglichem Einfluss | starkes Indiz für KI-System |
| Generatives Modell oder LLM/API im | regelmäßig KI-System-Komponente |
| Nur feste Wenn-Dann-Regeln ohne gelernte Parameter und ohne Inferenz | regelmäßig kein KI-System |
| Nur Suche, Filterung, Formatierung, Kopieren, Validieren | regelmäßig kein KI-System |
| Automation ohne Inferenz | nicht genug, aber genauer prüfen |
| Autonomie gering, aber Output wird inferenzbasiert erzeugt | KI-System häufig trotzdem naheliegend |
| Nur Modell ohne konkrete Anwendung | ggf. GPAI-Modell prüfen, aber KI-System-Einsatz gesondert bestimmen |

## Typische Beispiele

**Regelmäßig KI-System:**
- ChatGPT-ähnlicher Assistent, der Texte generiert oder Entscheidungen vorbereitet
- Bewerberranking mit LLM, Embeddings oder Scoringmodell
- Bonitätsscore per ML-Modell
- Bildklassifikation mit neuronalen Netzen
- Anomalieerkennung durch Clustering oder trainiertes Modell
- RAG-System, das Dokumente auswertet und rechtliche/geschäftliche Empfehlungen erzeugt

**Regelmäßig kein KI-System:**
- starres Makro zur Dokumentenumbenennung
- SQL-Suche ohne Rankingmodell
- Taschenrechner, Fristenrechner oder Steuerrechner mit ausschließlich fixen Regeln
- reines Formular, das Pflichtfelder prüft
- Dashboard mit Summen, Mittelwerten und statischen Filtern

**Prüfungsbedürftige Grenzfälle:**
- Expertensystem mit komplexer Wissensbasis
- scoringartige Excel-Modelle mit manuell gesetzten Gewichtungen
- Prozessautomation mit einzelnen KI-APIs
- LLM nur als Texteditor ohne Entscheidungskontext
- KI-Assistenz in juristischen, Personal-, Bildungs- oder Kreditprozessen

## Routing

- **KI-System wahrscheinlich:** weiter zu `territorialer-anwendungsbereich-art-2`, danach `persoenlicher-anwendungsbereich-rollen-art-3` und `risikoklassen-uebersicht-und-triage`.
- **Konventionelle Software wahrscheinlich:** Ergebnis dokumentieren; bei Grenzfällen zusätzlich `abgrenzung-konventionelle-software-vs-ki-system`.
- **GPAI oder allgemeiner Chatbot betroffen:** zusätzlich `gpai-vorliegen-art-3-nr-63`, `begrenztes-risiko-art-50-transparenzpflichten` und bei Hochrisiko-Kontexten `hochrisiko-art-6-abs-2-anhang-iii`.
- **Unklare Tatsachen:** offene Punkte im Output markieren und nicht mit Scheinsicherheit entscheiden.

## Output-Template — KI-System-Einordnungsvermerk

```text
KI-SYSTEM-EINORDNUNGSVERMERK NACH ART. 3 NR. 1 KI-VO
Datum: [DATUM]
System / Komponente: [NAME]
Geprüfter Funktionszuschnitt: [MODELL / API / APP / WORKFLOW / GESAMTPRODUKT]
Quelle der Tatsachen: [NUTZERANGABEN / DOKUMENTE / TECHNISCHE UNTERLAGEN]

1. Sachverhalt in Kurzform
[Was tut das System, welche Eingaben, welche Ausgaben, welche Nutzung?]

2. Tatbestandsmerkmale
- Maschinenbasiertes System: [JA/NEIN/UNKLAR] — [Begründung]
- Autonomiegrad: [JA/NEIN/UNKLAR] — [nicht überhöhen; menschliche Freigabe einordnen]
- Adaptivität nach Einführung: [JA/NEIN/UNKLAR/NICHT ERFORDERLICH] — [Begründung]
- Explizite oder implizite Ziele: [JA/NEIN/UNKLAR] — [Zweck]
- Inferenz aus Eingaben: [JA/NEIN/UNKLAR] — [Methode/Indizien]
- Ausgabetyp: [Vorhersage/Inhalt/Empfehlung/Entscheidung/anderer Output]
- Einfluss auf physische oder virtuelle Umgebung: [JA/NEIN/UNKLAR] — [Wirkpfad]

3. Würdigung
[Warum spricht die Automation für/gegen KI-System? Warum ist Autonomie hier ausreichend oder nicht? Welche Rolle spielt Adaptivität?]

4. Ergebnis
[KI-System liegt wahrscheinlich vor / liegt wahrscheinlich nicht vor / Grenzfall]

5. Dokumentationshinweis
Diese Einordnung beruht auf den angegebenen Tatsachen. Bei geänderter Zweckbestimmung, Modellwechsel, Integration in Hochrisiko-Prozesse oder neuem Nutzerkreis ist neu zu prüfen.

6. Nächste Skills
[territorialer-anwendungsbereich-art-2 / risikoklassen-uebersicht-und-triage / hochrisiko-art-6-abs-2-anhang-iii / gpai-vorliegen-art-3-nr-63 / abgrenzung-konventionelle-software-vs-ki-system]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Zu berücksichtigen sind Art. 3 Nr. 1, Nr. 12, Nr. 13 und Nr. 23 KI-VO, Erwägungsgrund 12 sowie die Kommissionsleitlinien zur Definition des KI-Systems. Keine Rechtsberatung; die Einordnung bleibt abhängig vom konkreten Tatsachenvortrag.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `mandatsabbruch-empfehlung-komplexe-faelle`

**Fokus:** Mechanik-erkennt Anzeichen von Faellen die anwaltliche Spezialkenntnisse erfordern und empfiehlt Eskalation. Indikatoren für Komplexitaet jenseits des KI-VO-Prüfers: multijurisdiktionelle Lieferketten marktbeherrschende Stellung KI und Waettbewerb hochspezialisierte Zertifizierungen Auslegungsstreit. Prüfraster: Schwellenwerte Mehrfachrollen kombinierte Hochrisiko-GPAI-Systeme laufende Vertragsprüfung. Output: Eskalationsempfehlung mit Begründung und Verweis auf IT-Recht Datenschutz Produktsicherheit. Abgrenzung zu triage-ki-vo-vorprüfung (Eingangs-Triage).

# Mandatsabbruch-Empfehlung bei komplexen KI-VO-Fällen

## Zweck

Dieser Skill erkennt Situationen, in denen ein Mechanik-nicht mehr ausreicht und professionelle juristische Beratung zwingend erforderlich ist. Er gibt klare Indikatoren und benennt die relevanten Fachrichtungen.

## Grundprinzip

Der vorliegende ist ein mechanisches Prüfinstrument. Er kann prüfen, ob bestimmte Tatbestandsmerkmale nach Maßgabe der vom Nutzer geschilderten Tatsachen erfüllt sind. Er kann nicht:
- Sachverhalte würdigen, die rechtlich komplex oder widersprüchlich sind
- Ermessen ausüben, das Rechtsanwendung erfordert
- Strategische Compliance-Beratung leisten
- Haftungsrisiken quantifizieren
- Behördliche Verfahren begleiten
- Verhandlungen mit Aufsichtsbehörden führen

## Indikatoren für zwingenden Fachanwalt-Bedarf

### Indikator 1 — Verbotene Praktiken (Art. 5 KI-VO)

Wenn das System Anzeichen aufweist, dass eine verbotene Praktik nach Art. 5 KI-VO vorliegen könnte, ist sofortiger Rechtsrat erforderlich. Das Inverkehrbringen oder der Betrieb eines verbotenen KI-Systems ist mit Bußgeldern bis zu 35 Mio EUR oder sieben Prozent des weltweiten Jahresumsatzes bedroht.

**Fachrichtung:** Fachanwalt IT-Recht / Öffentliches Recht

### Indikator 2 — Hochrisiko-KI in sensiblen Bereichen

Wenn das System für biometrische Identifizierung, Strafverfolgung, Justiz, kritische Infrastruktur, Bildung oder Beschäftigung eingesetzt wird, reicht eine mechanische Selbsteinschätzung nicht aus. Die Konformitätsbewertung nach Art. 43 bis 49 KI-VO erfordert in vielen Fällen eine benannte Stelle.

**Fachrichtung:** Fachanwalt IT-Recht, ggf. Fachanwalt Öffentliches Recht

### Indikator 3 — GPAI-Modelle mit systemischem Risiko

Wenn das System ein General-Purpose-KI-Modell mit einer Trainingsrechenleistung von mehr als 10e25 FLOP ist oder sein könnte, gelten besondere Pflichten nach Art. 55 KI-VO, deren Ausgestaltung noch durch Leitlinien und Codes of Practice konkretisiert wird.

**Fachrichtung:** Fachanwalt IT-Recht / Urheberrecht (Trainingsdaten)

### Indikator 4 — Grenzüberschreitende Lieferketten

Wenn das System in einer Lieferkette eingesetzt wird, bei der Anbieter, Einführer, Händler und Betreiber in verschiedenen Rechtsordnungen sitzen, ist die Rollenabgrenzung nach Art. 3 KI-VO und die Pflichtenzuweisung komplex.

**Fachrichtung:** Fachanwalt IT-Recht / Fachanwalt Internationales Wirtschaftsrecht

### Indikator 5 — Behördliche Anfragen oder Inspektionen

Wenn die Marktüberwachungsbehörde bereits Anfragen gestellt hat, Informationen angefordert hat oder eine Inspektion ankündigt, ist sofortiger Rechtsrat erforderlich.

**Fachrichtung:** Fachanwalt IT-Recht / Verwaltungsrecht

### Indikator 6 — Zweifelhafte Ausnahmen (Art. 2 Abs. 3 bis 12 KI-VO)

Wenn Ausnahmen wie militärische Nutzung, nationale Sicherheit oder Open-Source in Anspruch genommen werden sollen, ist eine sorgfältige rechtliche Prüfung erforderlich — diese Ausnahmen haben enge Voraussetzungen und können schnell nicht mehr greifen.

**Fachrichtung:** Fachanwalt IT-Recht / Öffentliches Recht

### Indikator 7 — Grundrechte-Folgenabschätzung für öffentliche Stellen

Wenn der Nutzer eine öffentliche Stelle oder ein im öffentlichen Auftrag handelnder Betreiber ist und Hochrisiko-KI einsetzt, ist die Grundrechte-Folgenabschätzung nach Art. 27 KI-VO ein komplexer Prozess, der juristische und technische Expertise erfordert.

**Fachrichtung:** Fachanwalt Öffentliches Recht / Datenschutzrecht

## Empfehlung

Wenn ein oder mehrere dieser Indikatoren vorliegen, empfiehlt dieses System:

1. Den Mechanik-für orientierende Selbsteinschätzung weiter nutzen — aber keine abschließenden Compliance-Entscheidungen darauf stützen.
2. Einen auf IT-Recht, Datenschutz oder Produktsicherheit spezialisierten Anwalt hinzuziehen.
3. Die Fachkenntnisse einer benannten Stelle oder akkreditierten Prüfeinrichtung in Betracht ziehen.

## Keine Einschränkung des Workflows

Die Empfehlung eines Fachanwalts schließt die weitere Nutzung dieses Workflows nicht aus. Der kann als strukturierte Vorbereitung für ein Beratungsgespräch dienen.

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
PRUEFERGEBNIS — MANDATSABBRUCH EMPFEHLUNG KOMPLEXE FAELLE
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 9 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
